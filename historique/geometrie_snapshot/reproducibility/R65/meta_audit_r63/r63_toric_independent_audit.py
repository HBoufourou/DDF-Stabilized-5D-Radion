#!/usr/bin/env python3
"""Independent R63 recheck of the R62 relative toric construction.

This program intentionally does not import either R61 or R62.  It uses only
the Python standard library and reconstructs the cones, exact determinants,
normal-polyhedron certificates, completion, Stanley--Reisner ideal and the
69-term sigma_5 linear system from the stated rays.

It checks the combinatorial and exact-arithmetic part of the claims.  Generic
smoothness and irreducibility still invoke Bertini and the algebraic arguments
in the written report; those theorem-level steps are not replaced by a finite
Jacobian sampling test here.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd


RAYS4 = (
    (1, 0, 0, 0),
    (-2, 0, -1, 0),
    (-2, 0, 0, -1),
    (0, 0, 0, 1),
    (0, 0, 1, 0),
    (-1, -1, 0, 0),
    (0, 1, 0, 0),
    (-1, 0, 0, 0),
    (1, 1, 0, 0),
)
OLD_SR_PAIRS = ((0, 7), (1, 4), (2, 3), (5, 6))
P = 9
M = 10
INF = 11


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def det_bareiss(rows):
    """Exact determinant for a square integer matrix, without SymPy."""
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def solve_square(rows, rhs):
    """Exact Gauss--Jordan solver over Q; None means singular."""
    n = len(rows)
    aug = [
        [Fraction(value) for value in row] + [Fraction(target)]
        for row, target in zip(rows, rhs, strict=True)
    ]
    for column in range(n):
        pivot = next((i for i in range(column, n) if aug[i][column]), None)
        if pivot is None:
            return None
        aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [value / scale for value in aug[column]]
        for i in range(n):
            if i == column:
                continue
            scale = aug[i][column]
            if scale:
                aug[i] = [
                    left - scale * right
                    for left, right in zip(aug[i], aug[column], strict=True)
                ]
    return tuple(row[-1] for row in aug)


def all_faces(maximal_cones):
    faces = set()
    for cone in maximal_cones:
        for size in range(len(cone) + 1):
            faces.update(combinations(cone, size))
    return faces


def minimal_nonfaces(number_of_rays, maximal_cones):
    faces = all_faces(maximal_cones)
    result = []
    for size in range(1, number_of_rays + 1):
        for candidate in combinations(range(number_of_rays), size):
            if candidate in faces:
                continue
            if all(
                tuple(value for value in candidate if value != removed) in faces
                for removed in candidate
            ):
                result.append(candidate)
    return tuple(result)


def vertices_and_active_sets(rays, heights):
    """Exact vertices of {y | <y,v_i> <= h_i}, independently enumerated."""
    dimension = len(rays[0])
    found = {}
    for selected in combinations(range(len(rays)), dimension):
        candidate = solve_square(
            [rays[index] for index in selected],
            [heights[index] for index in selected],
        )
        if candidate is None:
            continue
        values = tuple(dot(candidate, ray) for ray in rays)
        if not all(value <= bound for value, bound in zip(values, heights, strict=True)):
            continue
        active = tuple(
            i
            for i, (value, bound) in enumerate(zip(values, heights, strict=True))
            if value == bound
        )
        if candidate in found:
            assert found[candidate] == active
        found[candidate] = active
    return found


def walls(maximal_cones):
    return Counter(
        tuple(value for value in cone if value != removed)
        for cone in maximal_cones
        for removed in cone
    )


def resolved_four_fan():
    original = tuple(
        sorted(tuple(sorted(choice)) for choice in product(*OLD_SR_PAIRS))
    )
    assert len(original) == 16
    resolved = []
    for cone in original:
        if 0 in cone and 6 in cone:
            resolved.append(tuple(sorted((set(cone) - {0}) | {8})))
            resolved.append(tuple(sorted((set(cone) - {6}) | {8})))
        else:
            resolved.append(cone)
    resolved = tuple(sorted(resolved))
    assert len(resolved) == len(set(resolved)) == 20
    assert {abs(det_bareiss([RAYS4[index] for index in cone])) for cone in resolved} == {1}
    assert set(walls(resolved).values()) == {2}
    return resolved


def relative_fan():
    fan4 = resolved_four_fan()
    heights4 = tuple(ray[1] for ray in RAYS4)
    upper = tuple(cone for cone in fan4 if all(heights4[i] >= 0 for i in cone))
    lower = tuple(cone for cone in fan4 if all(heights4[i] <= 0 for i in cone))
    mixed = tuple(
        cone
        for cone in fan4
        if any(heights4[i] < 0 for i in cone)
        and any(heights4[i] > 0 for i in cone)
    )
    slice_cones = tuple(
        sorted(
            {
                tuple(index for index in cone if heights4[index] == 0)
                for cone in upper
                if sum(heights4[index] == 0 for index in cone) == 3
            }
        )
    )
    assert (len(lower), len(upper), len(mixed), len(slice_cones)) == (8, 12, 0, 8)

    rays = tuple((*ray, 0) for ray in RAYS4) + (
        (0, -1, 0, 0, 1),
        (0, 0, 0, 0, 1),
    )
    q_rows = (
        (2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1),
    )
    assert all(
        sum(q_rows[row][column] * rays[column][coordinate] for column in range(11)) == 0
        for row in range(6)
        for coordinate in range(5)
    )
    maximal_minor_gcd = 0
    for columns in combinations(range(11), 6):
        minor = det_bareiss(
            [[q_rows[row][column] for column in columns] for row in range(6)]
        )
        maximal_minor_gcd = gcd(maximal_minor_gcd, abs(minor))
    # Nonzero rank-six minor plus gcd one proves rank six and saturated rows.
    assert maximal_minor_gcd == 1
    cones = tuple(
        sorted(
            [tuple(cone) + (P,) for cone in lower]
            + [tuple(cone) + (M,) for cone in upper]
            + [tuple(cone) + (P, M) for cone in slice_cones]
        )
    )
    assert len(cones) == len(set(cones)) == 28
    determinants = tuple(det_bareiss([rays[index] for index in cone]) for cone in cones)
    assert {abs(value) for value in determinants} == {1}

    support_heights = (0, 0, 0, 5, 5, 0, 5, 2, 4, 0, 3)
    vertices = vertices_and_active_sets(rays, support_heights)
    assert len(vertices) == 28
    assert set(vertices.values()) == set(cones)
    assert all(len(active) == 5 for active in vertices.values())
    assert all(value.denominator == 1 for vertex in vertices for value in vertex)
    strict_gaps = {
        support_heights[index] - dot(vertex, rays[index])
        for vertex, active in vertices.items()
        for index in range(len(rays))
        if index not in active
    }
    assert strict_gaps == {1, 2, 3, 4, 5}

    wall_counts = walls(cones)
    assert Counter(wall_counts.values()) == Counter({2: 60, 1: 20})
    boundary = {face for face, count in wall_counts.items() if count == 1}
    assert boundary == set(fan4)

    infinity_ray = (0, 0, 0, 0, -1)
    complete_rays = rays + (infinity_ray,)
    complete_heights = support_heights + (1,)
    complete_vertices = vertices_and_active_sets(complete_rays, complete_heights)
    infinity_cones = {tuple(cone) + (INF,) for cone in fan4}
    complete_cones = set(cones) | infinity_cones
    assert len(complete_vertices) == 48
    assert set(complete_vertices.values()) == complete_cones
    assert all(
        abs(det_bareiss([complete_rays[index] for index in cone])) == 1
        for cone in complete_cones
    )
    complete_walls = walls(complete_cones)
    assert len(complete_walls) == 120
    assert set(complete_walls.values()) == {2}

    # This bounded normal-polytope certificate proves completeness.  Removing
    # precisely the infinity-star leaves the inverse image of the positive
    # base cone under projection to the fifth coordinate.
    assert all(ray[-1] == 0 for ray in rays[:9])
    assert rays[P][-1] == rays[M][-1] == 1
    assert complete_rays[INF][-1] == -1
    assert all(INF not in cone for cone in cones)
    assert all(INF in cone for cone in infinity_cones)

    sr = minimal_nonfaces(len(rays), cones)
    assert sr == (
        (0, 6),
        (0, 7),
        (1, 4),
        (2, 3),
        (5, 6),
        (5, 8),
        (5, 10),
        (6, 9),
        (7, 8),
        (8, 9),
    )

    star_p = tuple(
        tuple(index for index in cone if index != P)
        for cone in cones
        if P in cone
    )
    star_m = tuple(
        tuple(index for index in cone if index != M)
        for cone in cones
        if M in cone
    )
    seam = tuple(
        tuple(index for index in cone if index not in (P, M))
        for cone in cones
        if P in cone and M in cone
    )
    assert (len(star_p), len(star_m), len(seam)) == (16, 20, 8)
    return {
        "rays": rays,
        "cones": cones,
        "fan4": fan4,
        "vertices": vertices,
        "complete_vertices": complete_vertices,
        "sr": sr,
        "star_p": star_p,
        "star_m": star_m,
        "seam": seam,
        "strict_gaps": strict_gaps,
        "gale_maximal_minor_gcd": maximal_minor_gcd,
    }


def matrix_vector(rows, column):
    return tuple(sum(a * b for a, b in zip(row, column, strict=True)) for row in rows)


def monomial_audit(fan):
    # Bounds follow directly from the ray inequalities:
    # -1 <= a <= 1, -1 <= q <= 1-a, and -1 <= c,d <= 1-2a.
    points = tuple(
        point
        for a in range(-1, 2)
        for q in range(-1, 1 - a + 1)
        for c in range(-1, 1 - 2 * a + 1)
        for d in range(-1, 1 - 2 * a + 1)
        for point in ((a, q, c, d),)
        if all(dot(point, ray) >= -1 for ray in RAYS4)
    )
    assert len(points) == 104

    q_rows = (
        (2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1),
    )
    support = []
    q_histogram = Counter()
    for point in points:
        exponents = tuple(dot(point, ray) + 1 for ray in RAYS4)
        assert all(isinstance(value, int) and value >= 0 for value in exponents)
        if exponents[5] % 2:
            continue
        q = point[1]
        relative = exponents + (max(-q, 0), max(q, 0))
        support.append(relative)
        q_histogram[q] += 1
    support = tuple(support)
    assert len(support) == 69
    assert q_histogram == Counter({-1: 9, 0: 26, 1: 9, 2: 25})
    degrees = {matrix_vector(q_rows, exponents) for exponents in support}
    assert degrees == {(4, 4, 3, 2, -1, 0)}
    assert tuple(sum(row) for row in q_rows) == next(iter(degrees))

    def minimal_base_components(local_support, local_cones):
        candidates = []
        for zero_set in all_faces(local_cones):
            if not zero_set:
                continue
            if all(
                any(exponents[index] > 0 for index in zero_set)
                for exponents in local_support
            ):
                candidates.append(frozenset(zero_set))
        minimal = [
            candidate
            for candidate in candidates
            if not any(other < candidate for other in candidates)
        ]
        return tuple(sorted(tuple(sorted(item)) for item in minimal))

    total_base = minimal_base_components(support, fan["cones"])
    p_support = tuple(item for item in support if item[P] == 0)
    m_support = tuple(item for item in support if item[M] == 0)
    seam_support = tuple(item for item in support if item[P] == item[M] == 0)
    assert total_base == ((6, 7),)
    assert (len(p_support), len(m_support), len(seam_support)) == (60, 35, 26)
    component_bases = (
        minimal_base_components(p_support, fan["star_p"]),
        minimal_base_components(m_support, fan["star_m"]),
        minimal_base_components(seam_support, fan["seam"]),
    )
    assert component_bases == ((), ((6, 7),), ())

    unit = (2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0)
    first_jets = tuple(
        exponents
        for exponents in support
        if exponents[6] == 1 and exponents[7] == 0
    )
    assert first_jets == (unit,)
    assert (0, 6) in fan["sr"] and (7, 8) in fan["sr"]
    assert (6, P) in fan["sr"] and (8, P) in fan["sr"]
    return {
        "point_count": len(points),
        "support_count": len(support),
        "q_histogram": q_histogram,
        "degree": next(iter(degrees)),
        "total_base": total_base,
        "component_counts": (len(p_support), len(m_support), len(seam_support)),
        "component_bases": component_bases,
        "unit_jet": unit,
    }


def main():
    fan = relative_fan()
    monomials = monomial_audit(fan)
    print("R63 INDEPENDENT TORIC RECHECK: PASS")
    print("4D/5D maximal cones", len(fan["fan4"]), len(fan["cones"]))
    print("coherence vertices / gaps", len(fan["vertices"]), sorted(fan["strict_gaps"]))
    print("Gale rank/saturation certificate", 6, fan["gale_maximal_minor_gcd"])
    print("smooth projective completion vertices", len(fan["complete_vertices"]))
    print("relative SR", fan["sr"])
    print("central links p/m/seam", len(fan["star_p"]), len(fan["star_m"]), len(fan["seam"]))
    print("dual points / sigma5 support", monomials["point_count"], monomials["support_count"])
    print("q histogram", dict(sorted(monomials["q_histogram"].items())))
    print("anticanonical Cox degree", monomials["degree"])
    print("base loci total / components", monomials["total_base"], monomials["component_bases"])
    print("component supports p/m/seam", monomials["component_counts"])
    print("unit transverse jet", monomials["unit_jet"])


if __name__ == "__main__":
    main()

