#!/usr/bin/env python3
"""R63: exact weightwise cohomology cross-check for the Tyurin components.

This script is independent of the conceptual exact-sequence proof in
``quasifano_normal_bundles.md``.  For each of the two smooth complete toric
fourfolds V_p and V_m it computes the potentially nonzero graded pieces of
H^i(V_j, O(-Y_j)) by the standard toric Cech/EMS formula.

For a torus character u and a torus-invariant divisor D=sum a_rho D_rho,
put

    I(u) = {rho | <u,v_rho> + a_rho < 0}.

On a complete simplicial fan, the u-graded part of H^i(O(D)) is the reduced
cohomology in degree i-1 of the fan complex induced by I(u).  We enumerate
all 2^8 and 2^9 possible subsets.  Whenever the induced complex has nonzero
reduced cohomology, exact Fourier--Motzkin elimination proves that the
corresponding integral sign cell is empty for D=-Y_j.

All topology and feasibility calculations are exact over Q and use only the
Python standard library.  No finite search box or floating-point LP solver is
used.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm


# Coordinates in N'=Z^5 are (a,q,c,d,s); p=9 and m=10.
RAYS = (
    (1, 0, 0, 0, 0),
    (-2, 0, -1, 0, 0),
    (-2, 0, 0, -1, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 1, 0, 0),
    (-1, -1, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (0, -1, 0, 0, 1),
    (0, 0, 0, 0, 1),
)

P, M = 9, 10

MAXIMAL_CONES = (
    (0, 1, 2, 5, P), (0, 1, 3, 5, P),
    (0, 2, 4, 5, P), (0, 3, 4, 5, P),
    (1, 2, 5, 7, P), (1, 3, 5, 7, P),
    (2, 4, 5, 7, P), (3, 4, 5, 7, P),
    (0, 1, 2, 8, M), (0, 1, 3, 8, M),
    (0, 2, 4, 8, M), (0, 3, 4, 8, M),
    (1, 2, 6, 7, M), (1, 2, 6, 8, M),
    (1, 3, 6, 7, M), (1, 3, 6, 8, M),
    (2, 4, 6, 7, M), (2, 4, 6, 8, M),
    (3, 4, 6, 7, M), (3, 4, 6, 8, M),
    (0, 1, 2, P, M), (0, 1, 3, P, M),
    (0, 2, 4, P, M), (0, 3, 4, P, M),
    (1, 2, 7, P, M), (1, 3, 7, P, M),
    (2, 4, 7, P, M), (3, 4, 7, P, M),
)

# The q=0 anticanonical monomial associated with lattice point (-1,0,-1,-1).
# Entries are ordered x0,...,x7,E,p,m.
REFERENCE_EXPONENT = (0, 4, 4, 0, 0, 2, 1, 2, 0, 0, 0)
REFERENCE_POINT = (-1, 0, -1, -1)

Q_ROWS = (
    (2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1),
)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def determinant(rows):
    """Bareiss determinant over Z."""
    work = [list(map(int, row)) for row in rows]
    size = len(work)
    previous = 1
    sign = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if work[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                assert numerator % previous == 0
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def rational_rank(rows):
    """Rank over Q, with an exact Gauss elimination."""
    if not rows:
        return 0
    work = [[Fraction(value) for value in row] for row in rows]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (candidate for candidate in range(row, len(work)) if work[candidate][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][column]
        work[row] = [value / scale for value in work[row]]
        for candidate in range(len(work)):
            if candidate == row or not work[candidate][column]:
                continue
            scale = work[candidate][column]
            work[candidate] = [
                left - scale * right
                for left, right in zip(work[candidate], work[row], strict=True)
            ]
        row += 1
        if row == len(work):
            break
    return row


def all_faces(maximal_cones):
    faces = {()}
    for cone in maximal_cones:
        for size in range(1, len(cone) + 1):
            faces.update(combinations(cone, size))
    return faces


def reduced_betti(maximal_cones, selected):
    """Reduced Betti numbers b_0,...,b_3 of an induced fan complex."""
    selected = set(selected)
    simplices = {degree: [] for degree in range(4)}
    for face in all_faces(maximal_cones):
        if face and set(face) <= selected:
            simplices[len(face) - 1].append(face)
    if not simplices[0]:
        return (0, 0, 0, 0)

    boundary_ranks = {}
    for degree in range(1, 4):
        rows = simplices[degree - 1]
        row_index = {simplex: index for index, simplex in enumerate(rows)}
        matrix = [[0 for _ in simplices[degree]] for _ in rows]
        for column, simplex in enumerate(simplices[degree]):
            for deleted in range(len(simplex)):
                face = simplex[:deleted] + simplex[deleted + 1 :]
                matrix[row_index[face]][column] = (-1) ** deleted
        boundary_ranks[degree] = rational_rank(matrix)

    return (
        len(simplices[0]) - boundary_ranks[1] - 1,
        len(simplices[1]) - boundary_ranks[1] - boundary_ranks[2],
        len(simplices[2]) - boundary_ranks[2] - boundary_ranks[3],
        len(simplices[3]) - boundary_ranks[3],
    )


def normalize_inequality(coefficients, bound):
    """Normalize a rational inequality coefficients.x <= bound by >0 scaling."""
    values = [Fraction(value) for value in coefficients] + [Fraction(bound)]
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in values]
    divisor = 0
    for value in integers:
        divisor = gcd(divisor, abs(value))
    if divisor:
        integers = [value // divisor for value in integers]
    return tuple(integers[:-1]), integers[-1]


def reduce_inequalities(inequalities):
    """Remove tautologies and retain the tightest duplicate inequality."""
    tightest = {}
    for coefficients, bound in inequalities:
        coefficients, bound = normalize_inequality(coefficients, bound)
        if not any(coefficients):
            if bound < 0:
                return None
            continue
        if coefficients not in tightest or bound < tightest[coefficients]:
            tightest[coefficients] = bound
    return [(coefficients, bound) for coefficients, bound in tightest.items()]


def rational_polyhedron_is_nonempty(inequalities, dimension):
    """Exact Fourier--Motzkin feasibility for A x <= b over Q."""
    current = reduce_inequalities(inequalities)
    if current is None:
        return False
    for eliminated in range(dimension - 1, -1, -1):
        positive, negative, zero = [], [], []
        for coefficients, bound in current:
            coefficient = coefficients[eliminated]
            if coefficient > 0:
                positive.append((coefficients, bound))
            elif coefficient < 0:
                negative.append((coefficients, bound))
            else:
                shortened = coefficients[:eliminated] + coefficients[eliminated + 1 :]
                zero.append((shortened, bound))

        projected = list(zero)
        for upper_coefficients, upper_bound in positive:
            upper_scale = upper_coefficients[eliminated]
            for lower_coefficients, lower_bound in negative:
                lower_scale = lower_coefficients[eliminated]
                coefficients = tuple(
                    (-lower_scale) * upper_coefficients[index]
                    + upper_scale * lower_coefficients[index]
                    for index in range(len(upper_coefficients))
                    if index != eliminated
                )
                bound = (-lower_scale) * upper_bound + upper_scale * lower_bound
                projected.append((coefficients, bound))
        current = reduce_inequalities(projected)
        if current is None:
            return False
    return True


def sign_cell_is_nonempty(bits, rays, thresholds):
    """Feasibility of exactly this bad-ray set for an integral torus weight.

    Because all scalar products are integral, ``<u,v> < threshold`` is
    equivalent to ``<u,v> <= threshold-1``.  We prove the resulting closed
    rational polyhedron empty; this is stronger than absence of lattice points.
    """
    inequalities = []
    for is_bad, ray, threshold in zip(bits, rays, thresholds, strict=True):
        if is_bad:
            inequalities.append((ray, threshold - 1))
        else:
            inequalities.append((tuple(-value for value in ray), -threshold))
    return rational_polyhedron_is_nonempty(inequalities, len(rays[0]))


def component_data(central_ray, active_indices, quotient):
    star = tuple(
        tuple(index for index in cone if index != central_ray)
        for cone in MAXIMAL_CONES
        if central_ray in cone
    )
    relabel = {global_index: local_index for local_index, global_index in enumerate(active_indices)}
    local_cones = tuple(
        tuple(relabel[index] for index in cone)
        for cone in star
    )
    quotient_rays = tuple(quotient(RAYS[index]) for index in active_indices)
    thresholds = tuple(REFERENCE_EXPONENT[index] for index in active_indices)

    assert all(abs(determinant([quotient_rays[index] for index in cone])) == 1 for cone in local_cones)
    walls = Counter(
        cone[:deleted] + cone[deleted + 1 :]
        for cone in local_cones
        for deleted in range(len(cone))
    )
    assert set(walls.values()) == {2}
    return local_cones, quotient_rays, thresholds


def audit_component(name, central_ray, active_indices, quotient):
    cones, rays, thresholds = component_data(
        central_ray, active_indices, quotient
    )
    topology_histogram = Counter()
    nonzero_patterns = []
    for bits in product((0, 1), repeat=len(rays)):
        betti = reduced_betti(cones, [index for index, bit in enumerate(bits) if bit])
        if any(betti):
            topology_histogram[betti] += 1
            nonzero_patterns.append((bits, betti))

    # Every sign pattern that could support H^1,...,H^4 is exactly infeasible.
    feasible_nonzero_patterns = [
        (bits, betti)
        for bits, betti in nonzero_patterns
        if sign_cell_is_nonempty(bits, rays, thresholds)
    ]
    assert feasible_nonzero_patterns == []

    # H^0(O(-Y)) would require the empty bad set; it is infeasible as well.
    empty_bad_set = (0,) * len(rays)
    assert not sign_cell_is_nonempty(empty_bad_set, rays, thresholds)

    return {
        "name": name,
        "rays": len(rays),
        "cones": len(cones),
        "thresholds": thresholds,
        "topology_histogram": topology_histogram,
        "potential_patterns": len(nonzero_patterns),
        "feasible_patterns": len(feasible_nonzero_patterns),
        "line_bundle_cohomology": (0, 0, 0, 0, 0),
    }


def main():
    # Integrity gate: derive the stored monomial from its lattice point and
    # verify that its Cox degree is exactly the anticanonical column sum.
    derived_reference = tuple(
        dot(REFERENCE_POINT, ray[:4]) + 1 for ray in RAYS[:9]
    ) + (0, 0)
    assert derived_reference == REFERENCE_EXPONENT
    reference_degree = tuple(
        sum(row[index] * REFERENCE_EXPONENT[index] for index in range(11))
        for row in Q_ROWS
    )
    anticanonical_degree = tuple(sum(row) for row in Q_ROWS)
    assert reference_degree == anticanonical_degree == (4, 4, 3, 2, -1, 0)
    assert REFERENCE_EXPONENT[5] % 2 == 0

    # Degree-shift unit test: the full induced complex for P1 is two points,
    # so its reduced b0=1 gives H^1(P1,O(-2))=1.
    p1_cones = ((0,), (1,))
    assert reduced_betti(p1_cones, (0, 1)) == (1, 0, 0, 0)
    assert sign_cell_is_nonempty((1, 1), ((1,), (-1,)), (1, 1))
    assert not sign_cell_is_nonempty((0, 0), ((1,), (-1,)), (1, 1))

    plus = audit_component(
        "V_p",
        P,
        (0, 1, 2, 3, 4, 5, 7, M),
        lambda ray: (ray[0], ray[2], ray[3], ray[1] + ray[4]),
    )
    minus = audit_component(
        "V_m",
        M,
        (0, 1, 2, 3, 4, 6, 7, 8, P),
        lambda ray: ray[:4],
    )

    assert plus["topology_histogram"] == Counter(
        {(1, 0, 0, 0): 4, (0, 1, 0, 0): 6,
         (0, 0, 1, 0): 4, (0, 0, 0, 1): 1}
    )
    assert minus["topology_histogram"] == Counter(
        {(1, 0, 0, 0): 12, (0, 1, 0, 0): 22,
         (0, 0, 1, 0): 12, (0, 0, 0, 1): 1}
    )

    print("R63 EMS TORIC COHOMOLOGY CROSS-CHECK")
    print("reference point / Cox degree:", REFERENCE_POINT, reference_degree)
    print("P1,O(-2) degree-shift control: h1=1")
    for result in (plus, minus):
        print(result["name"], "rays / maximal cones:", result["rays"], result["cones"])
        print(result["name"], "reference thresholds:", result["thresholds"])
        print(result["name"], "potential topological patterns:", result["potential_patterns"])
        print(result["name"], "exactly feasible nonzero patterns:", result["feasible_patterns"])
        print(result["name"], "H^0,...,H^4(O(-Y)):", result["line_bundle_cohomology"])
    print("CONSEQUENCE VIA 0 -> O(-Y) -> O_V -> O_Y -> 0")
    print("h^i(O_Yp) = h^i(O_Ym) = (1,0,0,0)")
    print("STRICT_DHT_QUASI_FANO_COHOMOLOGY_GATE: PASS")


if __name__ == "__main__":
    main()

