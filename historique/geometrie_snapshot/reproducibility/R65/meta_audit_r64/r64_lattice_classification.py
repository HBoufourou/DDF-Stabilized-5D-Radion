#!/usr/bin/env python3
"""R64 exact and independent lattice/Cox counter-audit.

Scope
-----
* reconstruct the restriction lattice L = U(2) from the R61--R63 toric data;
* solve O(U(2), Z) symbolically and determine the ample-cone subgroup;
* classify primitive isotropic classes in L;
* embed L primitively in the K3 lattice and reconstruct its active orthogonal;
* compute even/odd and active even/odd lattices for three explicit integral
  involutions (deck, Enriques and symplectic Nikulin models);
* exhaust the lattice automorphisms of the seam and resolved ambient fans;
* independently repeat the 2^9 diagonal Cox-sign scan on all 35 seam
  monomials, without importing any R61/R62/R63 Python module.

The program uses exact integer/rational arithmetic.  It does NOT claim to
classify all geometric automorphisms on every Noether--Lefschetz specialization
of the K3 surface; that requires period/Torelli data not present in the corpus.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[1]

# Coordinate order x0,...,x7,E.  These constants are transcribed from the
# R61--R63 data, then cross-checked against R63_DATA_MANIFEST.json below.
RAYS_4D = (
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

# Rows give the classes of D0,...,D8 in B=(D1,D2,D5,D7,E).
DIVISOR_CLASS_MATRIX = Matrix(
    [
        [2, 1, 0, 0, 1, 0, 0, 0, 0],
        [2, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [-1, 0, 0, 0, 0, 0, -1, 0, 1],
    ]
)

U = Matrix([[0, 1], [1, 0]])
U2 = Matrix([[0, 2], [2, 0]])
E8_CARTAN = Matrix(
    [
        [2, -1, 0, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, -1],
        [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 0, 0, 2],
    ]
)


def block_diag(*blocks: Matrix) -> Matrix:
    rows = sum(block.rows for block in blocks)
    cols = sum(block.cols for block in blocks)
    answer = Matrix.zeros(rows, cols)
    r = c = 0
    for block in blocks:
        answer[r : r + block.rows, c : c + block.cols] = block
        r += block.rows
        c += block.cols
    return answer


def dot(left, right):
    return sum(Fraction(x) * Fraction(y) for x, y in zip(left, right, strict=True))


def inertia(form: Matrix) -> tuple[int, int, int]:
    """Exact inertia by symmetric rational congruence elimination."""
    work = [[Fraction(form[i, j]) for j in range(form.cols)] for i in range(form.rows)]

    def recurse(a):
        n = len(a)
        if n == 0:
            return (0, 0, 0)
        diagonal = next((i for i in range(n) if a[i][i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(n) if i != diagonal]
            b = [[a[i][j] for j in order] for i in order]
            pivot = b[0][0]
            schur = [
                [b[i][j] - b[i][0] * b[0][j] / pivot for j in range(1, n)]
                for i in range(1, n)
            ]
            p, m, z = recurse(schur)
            return (p + (pivot > 0), m + (pivot < 0), z)
        pair = next(
            ((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j] != 0),
            None,
        )
        if pair is None:
            return (0, 0, n)
        i, j = pair
        order = [i, j] + [k for k in range(n) if k not in pair]
        b = [[a[x][y] for y in order] for x in order]
        pivot = Matrix([[b[0][0], b[0][1]], [b[1][0], b[1][1]]])
        assert pivot.det() != 0
        cross = Matrix([[b[r][c] for c in range(2, n)] for r in range(2)])
        tail = Matrix([[b[r][c] for c in range(2, n)] for r in range(2, n)])
        schur_matrix = tail - cross.T * pivot.inv() * cross
        # At this branch every diagonal entry of ``a`` is zero, hence the
        # pivot is [[0,b],[b,0]] and has inertia (1,1,0) exactly.
        p0, m0, z0 = (1, 1, 0)
        p1, m1, z1 = inertia(schur_matrix)
        return (p0 + p1, m0 + m1, z0 + z1)

    return recurse(work)


def unit(n: int, index: int, coefficient: int = 1) -> Matrix:
    answer = Matrix.zeros(n, 1)
    answer[index, 0] = coefficient
    return answer


def columns(*vectors: Matrix) -> Matrix:
    if not vectors:
        return Matrix.zeros(22, 0)
    return Matrix.hstack(*vectors)


def vector_divisibility(form: Matrix, vector: Matrix) -> int:
    values = [abs(int(value)) for value in form * vector if value]
    return math.gcd(*values) if values else 0


def matrix_order_from_permutation(p: tuple[int, ...]) -> int:
    identity = tuple(range(len(p)))
    current = identity
    for order in range(1, 100):
        current = tuple(p[current[i]] for i in range(len(p)))
        if current == identity:
            return order
    raise AssertionError("permutation order unexpectedly large")


def manifest_cross_check() -> dict:
    manifest = json.loads((ROOT / "R63_DATA_MANIFEST.json").read_text(encoding="utf-8"))
    projected = tuple(tuple(ray[:4]) for ray in manifest["relative_rays"][:9])
    assert projected == RAYS_4D
    q_manifest = Matrix([row[:9] for row in manifest["cox_charge_matrix"][:5]])
    assert q_manifest == DIVISOR_CLASS_MATRIX
    assert manifest["certified_results"]["restriction_lattice_very_general"] == "U(2)"
    assert manifest["certified_results"]["rational_LMHS_very_general"] == "II_18"
    return manifest


def restriction_lattice_audit() -> dict:
    ray_matrix = Matrix(RAYS_4D).T
    assert DIVISOR_CLASS_MATRIX * ray_matrix.T == Matrix.zeros(5, 4)
    assert DIVISOR_CLASS_MATRIX.rank() == 5

    # Restriction in B=(D1,D2,D5,D7,E); h1 and h2 are the pulled-back rulings.
    rho_b = Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
    rho_d = rho_b * DIVISOR_CLASS_MATRIX
    expected = Matrix(
        [[2, 1, 0, 0, 1, 0, 0, 0, 0], [2, 0, 1, 1, 0, 0, 0, 0, 0]]
    )
    assert rho_d == expected
    smith = smith_normal_form(rho_b, domain=ZZ)
    assert tuple(abs(int(smith[i, i])) for i in range(2)) == (1, 1)
    gram_b = rho_b.T * U2 * rho_b
    assert inertia(U2) == (1, 1, 0)

    records = []
    names = [f"D{i}" for i in range(8)] + ["E"]
    for index, name in enumerate(names):
        cls = Matrix(rho_d[:, index])
        records.append(
            {
                "name": name,
                "class": tuple(int(x) for x in cls),
                "square": int((cls.T * U2 * cls)[0]),
            }
        )
    assert [record["class"] for record in records] == [
        (2, 2), (1, 0), (0, 1), (0, 1), (1, 0),
        (0, 0), (0, 0), (0, 0), (0, 0),
    ]
    return {
        "rho_b": rho_b,
        "rho_d": rho_d,
        "gram_b": gram_b,
        "records": records,
        "kernel": ("D5", "D7", "E"),
    }


def classify_u2_isometries() -> dict:
    # Symbolic solution.  If A=[[a,b],[c,d]], A^t U(2) A=U(2) is exactly
    # ac=0, bd=0, ad+bc=1.  If c=0, then ad=1 and b=0; if a=0,
    # then bc=1 and d=0.  These cases exhaust ac=0.
    matrices = {
        "I": Matrix.eye(2),
        "-I": -Matrix.eye(2),
        "S": Matrix([[0, 1], [1, 0]]),
        "-S": Matrix([[0, -1], [-1, 0]]),
    }
    for matrix in matrices.values():
        assert matrix.T * U2 * matrix == U2
        assert matrix * matrix == Matrix.eye(2)

    # A bounded enumeration is only a regression check; completeness comes
    # from the symbolic case split above, not from this bound.
    bounded = set()
    bound = 4
    for a, b, c, d in product(range(-bound, bound + 1), repeat=4):
        candidate = Matrix([[a, b], [c, d]])
        if candidate.T * U2 * candidate == U2:
            bounded.add(tuple(candidate))
    assert bounded == {tuple(matrix) for matrix in matrices.values()}

    ample_preserving = {}
    eigen = {}
    for name, matrix in matrices.items():
        images = [matrix * Matrix([1, 0]), matrix * Matrix([0, 1])]
        preserves = all(all(int(value) >= 0 for value in image) for image in images)
        if preserves:
            ample_preserving[name] = matrix

        eigendata = {}
        eigencolumns = []
        for sign, label in ((1, "+"), (-1, "-")):
            null = (matrix - sign * Matrix.eye(2)).nullspace()
            integral = []
            for vector in null:
                denominators = [Fraction(value).denominator for value in vector]
                scale = math.lcm(*denominators)
                vals = [int(scale * value) for value in vector]
                divisor = math.gcd(*(abs(value) for value in vals if value)) if any(vals) else 1
                integral.append(Matrix([value // divisor for value in vals]))
            basis = Matrix.hstack(*integral) if integral else Matrix.zeros(2, 0)
            gram = basis.T * U2 * basis
            eigendata[label] = {
                "basis": tuple(tuple(int(x) for x in basis[:, j]) for j in range(basis.cols)),
                "gram": tuple(tuple(int(gram[i, j]) for j in range(gram.cols)) for i in range(gram.rows)),
                "signature": inertia(gram),
            }
            eigencolumns.extend(integral)
        total = Matrix.hstack(*eigencolumns) if eigencolumns else Matrix.zeros(2, 0)
        eigendata["splitting_index"] = abs(int(total.det())) if total.shape == (2, 2) else None
        eigen[name] = eigendata

    assert set(ample_preserving) == {"I", "S"}

    # q(a h1+b h2)=4ab.  Hence q=0 iff a=0 or b=0; primitivity then leaves
    # exactly +/-h1,+/-h2.  The bounded scan checks the implementation only.
    primitive_isotropic = set()
    for a, b in product(range(-50, 51), repeat=2):
        if (a, b) != (0, 0) and math.gcd(abs(a), abs(b)) == 1 and 4 * a * b == 0:
            primitive_isotropic.add((a, b))
    assert primitive_isotropic == {(-1, 0), (1, 0), (0, -1), (0, 1)}

    # Ample integral polarizations are exactly (a,b), a,b>0.  S fixes one
    # precisely when a=b; I fixes all of them.
    assert matrices["S"] * Matrix([1, 2]) != Matrix([1, 2])
    assert matrices["S"] * Matrix([1, 1]) == Matrix([1, 1])
    return {
        "matrices": matrices,
        "ample_preserving": ample_preserving,
        "eigen": eigen,
        "primitive_isotropic": tuple(sorted(primitive_isotropic)),
        "regression_bound": bound,
    }


def resolved_cones() -> tuple[tuple[int, ...], ...]:
    old_sr_pairs = ((0, 7), (1, 4), (2, 3), (5, 6))
    answer = []
    for cone in product(*old_sr_pairs):
        if 0 in cone and 6 in cone:
            answer.append(tuple(sorted((set(cone) - {0}) | {8})))
            answer.append(tuple(sorted((set(cone) - {6}) | {8})))
        else:
            answer.append(tuple(sorted(cone)))
    result = tuple(sorted(answer))
    assert len(result) == 20
    return result


SEAM_GLOBAL = (0, 1, 2, 3, 4, 7)
SEAM_RAYS = tuple((RAYS_4D[i][0], RAYS_4D[i][2], RAYS_4D[i][3]) for i in SEAM_GLOBAL)
SEAM_CONES = (
    (0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4),
    (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5),
)


def fan_automorphisms(rays, maximal_cones) -> dict[tuple[int, ...], Matrix]:
    """Exhaust GL(n,Z) fan automorphisms via images of one ray basis.

    Completeness is exact: a unimodular basis chosen among the rays determines
    a lattice map uniquely, and every fan automorphism sends those basis rays
    to distinct rays.  Thus all ordered target tuples are enumerated.
    """
    dimension = len(rays[0])
    source = next(
        candidate
        for candidate in permutations(range(len(rays)), dimension)
        if abs(int(Matrix.hstack(*(Matrix(rays[i]) for i in candidate)).det())) == 1
    )
    source_matrix = Matrix.hstack(*(Matrix(rays[i]) for i in source))
    ray_to_index = {tuple(ray): i for i, ray in enumerate(rays)}
    cone_set = {tuple(sorted(cone)) for cone in maximal_cones}
    answer = {}
    for target in permutations(range(len(rays)), dimension):
        target_matrix = Matrix.hstack(*(Matrix(rays[i]) for i in target))
        transform = target_matrix * source_matrix.inv()
        if any(Fraction(value).denominator != 1 for value in transform):
            continue
        if abs(int(transform.det())) != 1:
            continue
        image = []
        for ray in rays:
            mapped = tuple(int(value) for value in transform * Matrix(ray))
            if mapped not in ray_to_index:
                break
            image.append(ray_to_index[mapped])
        else:
            permutation = tuple(image)
            if len(set(permutation)) != len(rays):
                continue
            mapped_cones = {
                tuple(sorted(permutation[i] for i in cone)) for cone in cone_set
            }
            if mapped_cones == cone_set:
                answer[permutation] = transform
    return answer


def fan_symmetry_audit() -> dict:
    seam = fan_automorphisms(SEAM_RAYS, SEAM_CONES)
    ambient = fan_automorphisms(RAYS_4D, resolved_cones())
    assert len(seam) == 8 and len(ambient) == 8

    seam_classes = ((2, 2), (1, 0), (0, 1), (0, 1), (1, 0), (0, 0))
    induced = Counter()
    for permutation in seam:
        # h1=[D1], h2=[D2]; a toric permutation sends these coordinate
        # divisor classes to those indexed by permutation[1], permutation[2].
        action = Matrix.hstack(
            Matrix(seam_classes[permutation[1]]), Matrix(seam_classes[permutation[2]])
        )
        assert action.T * U2 * action == U2
        label = "I" if action == Matrix.eye(2) else "S" if action == Matrix([[0, 1], [1, 0]]) else "other"
        induced[label] += 1
    assert induced == Counter({"I": 4, "S": 4})

    height = tuple(ray[1] for ray in RAYS_4D)
    height_behaviour = Counter()
    for permutation in ambient:
        mapped = tuple(height[permutation[i]] for i in range(len(height)))
        if mapped == height:
            height_behaviour["preserved"] += 1
        elif mapped == tuple(-value for value in height):
            height_behaviour["reversed"] += 1
        else:
            height_behaviour["other"] += 1
    assert height_behaviour == Counter({"preserved": 8})
    assert Counter(matrix_order_from_permutation(p) for p in seam) == Counter({2: 5, 4: 2, 1: 1})
    assert Counter(matrix_order_from_permutation(p) for p in ambient) == Counter({2: 5, 4: 2, 1: 1})
    return {
        "seam": seam,
        "ambient": ambient,
        "induced": induced,
        "height_behaviour": height_behaviour,
    }


def polytope_vertices() -> tuple[tuple[Fraction, ...], ...]:
    vertices = set()
    for active in combinations(range(len(RAYS_4D)), 4):
        matrix = Matrix([RAYS_4D[i] for i in active])
        if matrix.det() == 0:
            continue
        point = tuple(Fraction(value) for value in matrix.inv() * Matrix([-1] * 4))
        if all(dot(point, ray) >= -1 for ray in RAYS_4D):
            vertices.add(point)
    return tuple(sorted(vertices))


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def cox_character_audit() -> dict:
    vertices = polytope_vertices()
    assert len(vertices) == 14
    lower = tuple(min(vertex[i] for vertex in vertices) for i in range(4))
    upper = tuple(max(vertex[i] for vertex in vertices) for i in range(4))
    ranges = tuple(
        range(ceil_fraction(lower[i]), math.floor(upper[i]) + 1) for i in range(4)
    )
    points = tuple(
        point for point in product(*ranges) if all(dot(point, ray) >= -1 for ray in RAYS_4D)
    )
    assert len(points) == 104
    assert Counter(point[1] for point in points) == Counter({0: 35, 1: 34, 2: 25, -1: 10})

    def exponents(point):
        return tuple(int(dot(point, ray) + 1) for ray in RAYS_4D)

    sigma5_points = tuple(point for point in points if exponents(point)[5] % 2 == 0)
    assert len(sigma5_points) == 69
    assert Counter(point[1] for point in sigma5_points) == Counter({0: 26, 2: 25, -1: 9, 1: 9})

    seam_points = tuple(point for point in points if point[1] == 0)
    seam_data = tuple((point, exponents(point)) for point in seam_points)
    assert len(seam_points) == 35
    assert Counter(point[0] for point in seam_points) == Counter({-1: 25, 0: 9, 1: 1})
    assert tuple(point for point in seam_points if point[0] == 1) == ((1, 0, -1, -1),)

    patterns = Counter()
    for signs in product((0, 1), repeat=9):
        raw = tuple(
            sum(sign * exponent for sign, exponent in zip(signs, exp, strict=True)) % 2
            for _, exp in seam_data
        )
        normalized = tuple(value ^ raw[0] for value in raw)
        patterns[normalized] += 1
    assert len(patterns) == 8 and set(patterns.values()) == {64}

    formula_patterns = {}
    records = {}
    for character in product((0, 1), repeat=3):
        a_char, c_char, d_char = character
        raw = tuple(
            (a_char * point[0] + c_char * point[2] + d_char * point[3]) % 2
            for point in seam_points
        )
        normalized = tuple(value ^ raw[0] for value in raw)
        formula_patterns[character] = normalized

        # Select the eigenspace containing the unique a=+1 term.  This is the
        # irreducible/smooth candidate used in R62; the opposite eigenspace
        # has a common x7 factor.
        eigenvalue = (a_char + c_char + d_char) % 2
        kept = tuple(
            point
            for point in seam_points
            if (a_char * point[0] + c_char * point[2] + d_char * point[3]) % 2
            == eigenvalue
        )
        opposite = tuple(point for point in seam_points if point not in kept)
        if opposite:
            assert all(1 - point[0] >= 1 for point in opposite)
        # On the dense torus a sign translation fixes the logarithmic volume
        # form.  Poincare residue therefore gives Omega_S the eigenvalue of
        # 1/P, equal to the eigenvalue of P for an order-two action.
        records[character] = {
            "eigenvalue": eigenvalue,
            "omega_sign": -1 if eigenvalue else 1,
            "count": len(kept),
            "by_a": tuple(Counter(point[0] for point in kept).get(a, 0) for a in (-1, 0, 1)),
        }
    assert set(formula_patterns.values()) == set(patterns)
    expected = {
        (0, 0, 0): (35, (25, 9, 1), 1),
        (0, 0, 1): (22, (15, 6, 1), -1),
        (0, 1, 0): (22, (15, 6, 1), -1),
        (0, 1, 1): (19, (13, 5, 1), 1),
        (1, 0, 0): (26, (25, 0, 1), -1),
        (1, 0, 1): (19, (15, 3, 1), 1),
        (1, 1, 0): (19, (15, 3, 1), 1),
        (1, 1, 1): (18, (13, 4, 1), -1),
    }
    for character, (count, by_a, omega) in expected.items():
        assert records[character]["count"] == count
        assert records[character]["by_a"] == by_a
        assert records[character]["omega_sign"] == omega
    return {
        "vertices": vertices,
        "bounds": (lower, upper),
        "points": points,
        "sigma5_points": sigma5_points,
        "seam_points": seam_points,
        "patterns": patterns,
        "records": records,
    }


def make_involution(images: dict[int, Matrix], default_sign: int = 1) -> Matrix:
    answer = default_sign * Matrix.eye(22)
    for source, image in images.items():
        answer[:, source] = image
    return answer


def active_nullity(k3_form: Matrix, l_basis: Matrix, involution: Matrix, sign: int) -> int:
    equations = Matrix.vstack(involution - sign * Matrix.eye(22), l_basis.T * k3_form)
    return 22 - equations.rank()


def verify_involution_model(
    name: str,
    form: Matrix,
    l_basis: Matrix,
    k_basis: Matrix,
    involution: Matrix,
    plus_basis: Matrix,
    minus_basis: Matrix,
    active_plus: Matrix,
    active_minus: Matrix,
) -> dict:
    assert involution * involution == Matrix.eye(22)
    assert involution.T * form * involution == form
    assert (involution - Matrix.eye(22)) * plus_basis == Matrix.zeros(22, plus_basis.cols)
    assert (involution + Matrix.eye(22)) * minus_basis == Matrix.zeros(22, minus_basis.cols)
    assert plus_basis.rank() == len((involution - Matrix.eye(22)).nullspace())
    assert minus_basis.rank() == len((involution + Matrix.eye(22)).nullspace())
    assert involution * l_basis == l_basis

    answer = {"name": name}
    for label, sign, basis in (
        ("plus", 1, plus_basis),
        ("minus", -1, minus_basis),
        ("active_plus", 1, active_plus),
        ("active_minus", -1, active_minus),
    ):
        gram = basis.T * form * basis
        if label.startswith("active"):
            assert l_basis.T * form * basis == Matrix.zeros(2, basis.cols)
            assert basis.rank() == active_nullity(form, l_basis, involution, sign)
        sig = inertia(gram)
        isotropic_witness = None
        for j in range(basis.cols):
            vector = basis[:, j]
            if (vector.T * form * vector)[0] == 0:
                isotropic_witness = tuple(int(x) for x in vector)
                break
        if sig[0] == 0 and sig[2] == 0:
            assert isotropic_witness is None
        answer[label] = {
            "rank": basis.cols,
            "signature": sig,
            "isotropic_witness": isotropic_witness,
        }
    return answer


def k3_active_lattice_audit() -> dict:
    # Lambda_K3 = U^3 + E8(-1)^2 in the ordered basis
    # (e1,f1,e2,f2,e3,f3,E8a[1..8],E8b[1..8]).
    k3 = block_diag(U, U, U, -E8_CARTAN, -E8_CARTAN)
    assert k3.det() == -1 and inertia(k3) == (3, 19, 0)

    e = [unit(22, i) for i in range(22)]
    l_basis = columns(e[0] + e[2], e[1] + e[3])
    k_basis = columns(e[0] - e[2], e[1] - e[3], e[4], e[5], *e[6:22])
    assert l_basis.T * k3 * l_basis == U2
    assert l_basis.T * k3 * k_basis == Matrix.zeros(2, 20)
    assert k_basis.rank() == 20
    k_gram = k_basis.T * k3 * k_basis
    expected_k = block_diag(U2, U, -E8_CARTAN, -E8_CARTAN)
    assert k_gram == expected_k
    assert inertia(k_gram) == (2, 18, 0) and abs(int(k_gram.det())) == 4
    smith_k = smith_normal_form(k_gram, domain=ZZ)
    smith_diag = tuple(abs(int(smith_k[i, i])) for i in range(20))
    assert smith_diag == (1,) * 18 + (2, 2)

    # The embedding L -> Lambda is primitive, while L+K has index four.
    assert math.gcd(
        *(abs(int(l_basis.extract(rows, (0, 1)).det())) for rows in combinations(range(22), 2))
    ) == 1
    combined = Matrix.hstack(l_basis, k_basis)
    assert abs(int(combined.det())) == 4

    # Exact primitive isotropic witnesses in K of both possible divisibilities.
    iso_div2 = unit(20, 0)  # first isotropic ray of the U(2) summand
    iso_div1 = unit(20, 2)  # first isotropic ray of the U summand
    for vector, divisibility in ((iso_div2, 2), (iso_div1, 1)):
        assert math.gcd(*(abs(int(x)) for x in vector if x)) == 1
        assert (vector.T * k_gram * vector)[0] == 0
        assert vector_divisibility(k_gram, vector) == divisibility

    # Deck: exchange U1,U2 and negate U3,E8a,E8b.
    deck = -Matrix.eye(22)
    deck[:, 0], deck[:, 2] = e[2], e[0]
    deck[:, 1], deck[:, 3] = e[3], e[1]
    deck_plus = l_basis
    deck_minus = k_basis

    # Enriques model: exchange U1,U2, negate U3, exchange the E8 copies.
    enriques = Matrix.zeros(22, 22)
    enriques[:, 0], enriques[:, 2] = e[2], e[0]
    enriques[:, 1], enriques[:, 3] = e[3], e[1]
    enriques[:, 4], enriques[:, 5] = -e[4], -e[5]
    for i in range(8):
        enriques[:, 6 + i] = e[14 + i]
        enriques[:, 14 + i] = e[6 + i]
    diag_e8 = [e[6 + i] + e[14 + i] for i in range(8)]
    anti_e8 = [e[6 + i] - e[14 + i] for i in range(8)]
    enriques_plus = columns(*[l_basis[:, j] for j in range(2)], *diag_e8)
    enriques_minus = columns(e[0] - e[2], e[1] - e[3], e[4], e[5], *anti_e8)
    enriques_active_plus = columns(*diag_e8)
    enriques_active_minus = enriques_minus

    # Symplectic Nikulin lattice model: fix U^3 and exchange the E8 copies.
    nikulin = Matrix.zeros(22, 22)
    for i in range(6):
        nikulin[:, i] = e[i]
    for i in range(8):
        nikulin[:, 6 + i] = e[14 + i]
        nikulin[:, 14 + i] = e[6 + i]
    nikulin_plus = columns(*e[:6], *diag_e8)
    nikulin_minus = columns(*anti_e8)
    nikulin_active_plus = columns(e[0] - e[2], e[1] - e[3], e[4], e[5], *diag_e8)
    nikulin_active_minus = nikulin_minus

    models = {
        "deck": verify_involution_model(
            "deck", k3, l_basis, k_basis, deck,
            deck_plus, deck_minus, Matrix.zeros(22, 0), deck_minus,
        ),
        "enriques": verify_involution_model(
            "enriques", k3, l_basis, k_basis, enriques,
            enriques_plus, enriques_minus, enriques_active_plus, enriques_active_minus,
        ),
        "nikulin": verify_involution_model(
            "nikulin", k3, l_basis, k_basis, nikulin,
            nikulin_plus, nikulin_minus, nikulin_active_plus, nikulin_active_minus,
        ),
    }
    assert models["deck"]["active_plus"]["signature"] == (0, 0, 0)
    assert models["deck"]["active_minus"]["signature"] == (2, 18, 0)
    assert models["enriques"]["active_plus"]["signature"] == (0, 8, 0)
    assert models["enriques"]["active_minus"]["signature"] == (2, 10, 0)
    assert models["nikulin"]["active_plus"]["signature"] == (2, 10, 0)
    assert models["nikulin"]["active_minus"]["signature"] == (0, 8, 0)
    return {
        "k3": k3,
        "l_basis": l_basis,
        "k_basis": k_basis,
        "k_gram": k_gram,
        "smith_k": smith_diag,
        "models": models,
        "isotropic_divisibilities": (1, 2),
    }


def main() -> None:
    manifest = manifest_cross_check()
    restriction = restriction_lattice_audit()
    u2 = classify_u2_isometries()
    fan = fan_symmetry_audit()
    cox = cox_character_audit()
    k3 = k3_active_lattice_audit()

    print("R64 EXACT LATTICE / INVOLUTION COUNTER-AUDIT")
    print("manifest:", manifest["schema"], manifest["model"]["polytope_local_id"])
    print("restriction rho_B / SNF:", tuple(map(tuple, restriction["rho_b"].tolist())), (1, 1))
    print("L Gram / signature:", tuple(map(tuple, U2.tolist())), inertia(U2))
    print("restricted coordinate classes:")
    for record in restriction["records"]:
        print(" ", record["name"], record["class"], "square", record["square"])
    print()

    print("O(U(2),Z), symbolic complete:", tuple(u2["matrices"]))
    print("ample-cone subgroup:", tuple(u2["ample_preserving"]))
    print("primitive isotropic vectors in L:", u2["primitive_isotropic"])
    for name in u2["matrices"]:
        data = u2["eigen"][name]
        print(" ", name, "L+", data["+"]["signature"], "L-", data["-"]["signature"],
              "splitting index", data["splitting_index"])
    print()

    print("seam fan GL automorphisms / induced (I,S):", len(fan["seam"]), dict(fan["induced"]))
    print("resolved fan GL automorphisms / top height:", len(fan["ambient"]), dict(fan["height_behaviour"]))
    print("toric top exchange:", "NONE")
    print()

    print("dual lattice points / seam / sigma5 total:", len(cox["points"]), len(cox["seam_points"]), len(cox["sigma5_points"]))
    print("Cox sign lifts / effective seam patterns / multiplicity:", 512, len(cox["patterns"]), sorted(set(cox["patterns"].values())))
    print("character  kept  by_a(-1,0,1)  OmegaS")
    for character, record in sorted(cox["records"].items()):
        print(" ", "".join(map(str, character)), f"{record['count']:>4}", record["by_a"], "+" if record["omega_sign"] == 1 else "-")
    print()

    print("K=L^perp Gram type / signature / determinant:", "U(2)+U+E8(-1)^2", inertia(k3["k_gram"]), abs(int(k3["k_gram"].det())))
    print("K Smith:", k3["smith_k"])
    print("primitive isotropic divisibilities exhibited in K:", k3["isotropic_divisibilities"])
    print("model        active + signature   active - signature")
    for name, model in k3["models"].items():
        print(" ", f"{name:<10}", model["active_plus"]["signature"], model["active_minus"]["signature"])
    print()

    print("VERDICT")
    print("U2_ISOMETRY_AND_AMPLE_CONE_CLASSIFICATION: EXACT_COMPLETE")
    print("SEAM_AND_RESOLVED_FAN_LATTICE_AUTOMORPHISMS: EXACT_COMPLETE")
    print("DIAGONAL_COX_SIGN_SCAN: EXACT_COMPLETE")
    print("BRANCH_PRESERVING_HOLOMORPHIC_NONSYMPLECTIC_ACTIVE_EVEN_ISOTROPIC: NONE")
    print("TOP_EXCHANGING_HOLOMORPHIC_SYMPLECTIC_ACTIVE_ODD_ISOTROPIC: NONE")
    print("ALL_GEOMETRIC_K3_INVOLUTIONS_ON_SPECIAL_NOETHER_LEFSCHETZ_LOCI: NOT_CLASSIFIED")


if __name__ == "__main__":
    main()

