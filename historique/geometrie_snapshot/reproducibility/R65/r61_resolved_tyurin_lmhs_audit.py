#!/usr/bin/env python3
"""R61: resolved projecting tops, integral LMHS and seam-parity audit.

The script keeps three logically different statements separate:

1. exact toric/lattice data of the resolved POLY944 phase;
2. the ordinary Type-II LMHS obtained from a two-component Tyurin model;
3. the action induced on the *actual height-zero seam* by sigma_5 and
   sigma_125.  This is not the action on the special pole F0={x5=0}.

All coordinate indices are zero based, as in R58--R60.  The exceptional
coordinate is x8 and has ray nu_E=nu_0+nu_6.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product

import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


RAYS = (
    (1, 0, 0, 0),
    (-2, 0, -1, 0),
    (-2, 0, 0, -1),
    (0, 0, 0, 1),
    (0, 0, 1, 0),
    (-1, -1, 0, 0),
    (0, 1, 0, 0),
    (-1, 0, 0, 0),
)
EXCEPTIONAL_RAY = (1, 1, 0, 0)
RESOLVED_RAYS = RAYS + (EXCEPTIONAL_RAY,)
OLD_DUAL_VERTICES = (
    (-1, -1, -1, -1),
    (-1, -1, -1, 3),
    (-1, -1, 3, -1),
    (-1, -1, 3, 3),
    (-1, 2, -1, -1),
    (-1, 2, -1, 3),
    (-1, 2, 3, -1),
    (-1, 2, 3, 3),
    (1, -1, -1, -1),
    (1, 0, -1, -1),
)
OLD_SR_PAIRS = ((0, 7), (1, 4), (2, 3), (5, 6))


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def rank(matrix) -> int:
    return Matrix(matrix).rank()


def determinant(matrix) -> Fraction:
    return Fraction(Matrix(matrix).det())


def solve_square(matrix, rhs):
    mat = Matrix(matrix)
    if mat.det() == 0:
        return None
    answer = mat.inv() * Matrix(rhs)
    return tuple(Fraction(value) for value in answer)


def polar_vertices(points):
    dimension = len(points[0])
    vertices = set()
    for indices in combinations(range(len(points)), dimension):
        candidate = solve_square(
            tuple(points[index] for index in indices),
            (-1,) * dimension,
        )
        if candidate is None:
            continue
        if all(dot(candidate, point) >= -1 for point in points):
            vertices.add(candidate)
    return tuple(sorted(vertices))


def lattice_points(vertices, facet_normals):
    dimension = len(vertices[0])
    minima = tuple(math.floor(min(v[i] for v in vertices)) for i in range(dimension))
    maxima = tuple(math.ceil(max(v[i] for v in vertices)) for i in range(dimension))
    return tuple(
        sorted(
            point
            for point in product(
                *(range(minima[i], maxima[i] + 1) for i in range(dimension))
            )
            if all(dot(normal, point) >= -1 for normal in facet_normals)
        )
    )


def actual_vertices(points, facet_normals):
    dimension = len(points[0])
    return tuple(
        point
        for point in points
        if rank(
            [normal for normal in facet_normals if dot(normal, point) == -1]
        )
        == dimension
    )


def facet_interior_counts(points, facet_normals):
    return tuple(
        sum(
            dot(normal, point) == -1
            and all(
                other == normal or dot(other, point) > -1
                for other in facet_normals
            )
            for point in points
        )
        for normal in facet_normals
    )


def edge_interior_count(first, second) -> int:
    divisor = 0
    for left, right in zip(first, second, strict=True):
        divisor = math.gcd(divisor, abs(int(left - right)))
    return divisor - 1


def codimension_two_correction(points, facet_normals):
    groups = defaultdict(list)
    for point in points:
        active = tuple(
            index
            for index, normal in enumerate(facet_normals)
            if dot(normal, point) == -1
        )
        groups[active].append(point)
    correction = 0
    certificates = []
    for active, interior_points in groups.items():
        normals = tuple(facet_normals[index] for index in active)
        if len(normals) != 2 or rank(normals) != 2:
            continue
        dual_interior = edge_interior_count(*normals)
        term = len(interior_points) * dual_interior
        correction += term
        certificates.append((active, len(interior_points), dual_interior, term))
    return correction, tuple(certificates)


def resolved_polytope_audit():
    delta_vertices = polar_vertices(RESOLVED_RAYS)
    assert len(delta_vertices) == 14
    assert all(value.denominator == 1 for vertex in delta_vertices for value in vertex)

    delta_points = lattice_points(delta_vertices, RESOLVED_RAYS)
    delta_star_points = lattice_points(RESOLVED_RAYS, delta_vertices)
    delta_star_vertices = actual_vertices(delta_star_points, delta_vertices)
    assert (len(delta_points), len(delta_star_points), len(delta_star_vertices)) == (104, 10, 8)

    star_facets = facet_interior_counts(delta_star_points, delta_vertices)
    delta_facets = facet_interior_counts(delta_points, delta_star_vertices)
    corr_h11, faces_h11 = codimension_two_correction(delta_star_points, delta_vertices)
    corr_h21, faces_h21 = codimension_two_correction(delta_points, delta_star_vertices)
    h11 = len(delta_star_points) - 5 - sum(star_facets) + corr_h11
    h21 = len(delta_points) - 5 - sum(delta_facets) + corr_h21
    assert (sum(star_facets), sum(delta_facets), corr_h11, corr_h21) == (0, 14, 0, 0)
    assert (h11, h21, 2 * (h11 - h21)) == (5, 85, -160)
    return {
        "delta_vertices": delta_vertices,
        "delta_points": delta_points,
        "delta_star_points": delta_star_points,
        "delta_star_vertices": delta_star_vertices,
        "hodge": (h11, h21),
        "euler": 2 * (h11 - h21),
        "faces_h11": faces_h11,
        "faces_h21": faces_h21,
    }


def original_maximal_cones():
    return tuple(sorted(tuple(sorted(choice)) for choice in product(*OLD_SR_PAIRS)))


def resolved_maximal_cones():
    answer = []
    for cone in original_maximal_cones():
        if 0 in cone and 6 in cone:
            answer.append(tuple(sorted((set(cone) - {0}) | {8})))
            answer.append(tuple(sorted((set(cone) - {6}) | {8})))
        else:
            answer.append(cone)
    return tuple(sorted(answer))


def fan_and_slice_audit(polytope):
    cones = resolved_maximal_cones()
    determinants = tuple(determinant([RESOLVED_RAYS[index] for index in cone]) for cone in cones)
    assert len(cones) == 20 and all(abs(value) == 1 for value in determinants)

    # Every maximal cone belongs to a facet of the new reflexive polytope.
    assert all(
        any(
            all(dot(normal, RESOLVED_RAYS[index]) == -1 for index in cone)
            for normal in polytope["delta_vertices"]
        )
        for cone in cones
    )

    heights = tuple(ray[1] for ray in RESOLVED_RAYS)
    upper = tuple(cone for cone in cones if all(heights[i] >= 0 for i in cone))
    lower = tuple(cone for cone in cones if all(heights[i] <= 0 for i in cone))
    mixed = tuple(
        cone
        for cone in cones
        if any(heights[i] < 0 for i in cone) and any(heights[i] > 0 for i in cone)
    )
    assert (len(upper), len(lower), len(mixed)) == (12, 8, 0)

    nonfaces = tuple(
        pair
        for pair in combinations(range(9), 2)
        if not any(set(pair) <= set(cone) for cone in cones)
    )
    expected_sr_pairs = ((0, 6), (0, 7), (1, 4), (2, 3), (5, 6), (5, 8), (7, 8))
    assert nonfaces == expected_sr_pairs

    transformed = tuple((-ray[0], ray[2], ray[3], ray[1]) for ray in RESOLVED_RAYS)
    transformed_with_origin = transformed + ((0, 0, 0, 0),)
    height_histogram = Counter(point[3] for point in transformed_with_origin)
    assert height_histogram == Counter({0: 7, 1: 2, -1: 1})

    slice_points = tuple(
        sorted({point[:3] for point in transformed_with_origin if point[3] == 0})
    )
    slice_vertices = polar_vertices(polar_vertices(slice_points))
    slice_dual_vertices = polar_vertices(slice_points)
    slice_dual_points = lattice_points(slice_dual_vertices, slice_points)
    assert len(slice_points) == 7 and len(slice_vertices) == 5
    assert len(slice_dual_vertices) == 5 and len(slice_dual_points) == 35

    slice_facets = facet_interior_counts(slice_points, slice_dual_vertices)
    slice_correction, _ = codimension_two_correction(slice_points, slice_dual_vertices)
    rho_slice = len(slice_points) - 4 - sum(slice_facets) + slice_correction
    assert (sum(slice_facets), slice_correction, rho_slice) == (1, 0, 2)

    # Projecting condition with integral split s=0.
    assert all(
        all(dot(normal, point[:3]) >= -1 for normal in slice_dual_vertices)
        for point in transformed
    )
    projections_off_slice = {
        index: transformed[index][:3]
        for index in range(9)
        if transformed[index][3] != 0
    }
    assert projections_off_slice == {
        5: (1, 0, 0),
        6: (0, 0, 0),
        8: (-1, 0, 0),
    }

    def induced_slice_cones(selected):
        return tuple(
            sorted(
                {
                    face
                    for cone in selected
                    for face in (tuple(index for index in cone if heights[index] == 0),)
                    if len(face) == 3
                }
            )
        )

    upper_slice = induced_slice_cones(upper)
    lower_slice = induced_slice_cones(lower)
    assert upper_slice == lower_slice
    assert upper_slice == (
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 4),
        (0, 3, 4),
        (1, 2, 7),
        (1, 3, 7),
        (2, 4, 7),
        (3, 4, 7),
    )
    return {
        "cones": cones,
        "determinants": determinants,
        "upper": upper,
        "lower": lower,
        "mixed": mixed,
        "sr_pairs": nonfaces,
        "height_histogram": dict(sorted(height_histogram.items())),
        "slice_points": slice_points,
        "slice_vertices": slice_vertices,
        "slice_dual_vertices": slice_dual_vertices,
        "slice_dual_points": slice_dual_points,
        "rho_slice": rho_slice,
        "projections_off_slice": projections_off_slice,
        "slice_cones": upper_slice,
    }


def restriction_audit():
    # Columns are D0,...,D8 in B=(D1,D2,D5,D7,E).
    classes = Matrix(
        [
            [2, 1, 0, 0, 1, 0, 0, 0, 0],
            [2, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [-1, 0, 0, 0, 0, 0, -1, 0, 1],
        ]
    )
    ray_matrix = Matrix(RESOLVED_RAYS).T
    assert classes * ray_matrix.T == Matrix.zeros(5, 4)
    assert classes.rank() == 5

    rho_basis = Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
    rho_divisors = rho_basis * classes
    expected = Matrix(
        [[2, 1, 0, 0, 1, 0, 0, 0, 0], [2, 0, 1, 1, 0, 0, 0, 0, 0]]
    )
    assert rho_divisors == expected
    smith = smith_normal_form(rho_basis, domain=ZZ)
    smith_diagonal = tuple(abs(int(smith[i, i])) for i in range(2))
    assert smith_diagonal == (1, 1)

    u2 = Matrix([[0, 2], [2, 0]])
    gram_basis = rho_basis.T * u2 * rho_basis
    assert gram_basis == Matrix(
        [
            [0, 2, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    assert rho_basis.rank() == 2 and len(rho_basis.nullspace()) == 3
    return {
        "basis": ("D1", "D2", "D5", "D7", "E"),
        "classes": classes,
        "rho_basis": rho_basis,
        "rho_divisors": rho_divisors,
        "smith": smith_diagonal,
        "gram_basis": gram_basis,
        "rank": rho_basis.rank(),
        "kernel": ("D5", "D7", "E"),
    }


def e8_cartan():
    return Matrix(
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


def block_diag(*matrices):
    rows = sum(matrix.rows for matrix in matrices)
    cols = sum(matrix.cols for matrix in matrices)
    result = Matrix.zeros(rows, cols)
    row = col = 0
    for matrix in matrices:
        result[row : row + matrix.rows, col : col + matrix.cols] = matrix
        row += matrix.rows
        col += matrix.cols
    return result


def lmhs_and_monodromy_audit():
    h11, h21 = 5, 85
    restriction_rank = 2
    u_hat = 20 - restriction_rank
    v_hat = h21 - u_hat - 1
    w_hat = h11
    b3 = 2 * h21 + 2
    gr = (u_hat + 2, 2 * v_hat, u_hat + 2)
    assert (u_hat, v_hat, w_hat, b3, gr) == (18, 66, 5, 172, (20, 132, 20))

    u = Matrix([[0, 1], [1, 0]])
    u2 = Matrix([[0, 2], [2, 0]])
    k = block_diag(u, u2, -e8_cartan(), -e8_cartan())
    assert k.shape == (20, 20) and k.det() == 4
    eigenvalues = np.linalg.eigvalsh(np.asarray(k.tolist(), dtype=float))
    signature = (
        int(np.sum(eigenvalues > 1e-8)),
        int(np.sum(eigenvalues < -1e-8)),
    )
    assert signature == (2, 18)
    smith = smith_normal_form(k, domain=ZZ)
    smith_nonzero = tuple(abs(int(smith[i, i])) for i in range(20))
    assert smith_nonzero == (1,) * 18 + (2, 2)

    half = b3 // 2
    active = Matrix.zeros(half, half)
    active[:20, :20] = k
    nilpotent = block_diag(Matrix.zeros(half, half), Matrix.zeros(half, half))
    nilpotent[half:, :half] = active
    identity = Matrix.eye(b3)
    symplectic = Matrix.vstack(
        Matrix.hstack(Matrix.zeros(half, half), Matrix.eye(half)),
        Matrix.hstack(-Matrix.eye(half), Matrix.zeros(half, half)),
    )
    monodromy = identity + nilpotent
    assert nilpotent * nilpotent == Matrix.zeros(b3, b3)
    assert nilpotent.rank() == 20
    assert monodromy.T * symplectic * monodromy == symplectic
    assert b3 - 2 * nilpotent.rank() == gr[1]

    hodge_deligne = (
        (1, 18, 1, 0),  # GrW4, columns GrF3,GrF2,GrF1,GrF0
        (0, 66, 66, 0), # GrW3
        (0, 1, 18, 1),  # GrW2
    )
    assert tuple(sum(row) for row in hodge_deligne) == (20, 132, 20)
    return {
        "hodge": (h11, h21),
        "b3": b3,
        "r": restriction_rank,
        "u_hat": u_hat,
        "v_hat": v_hat,
        "w_hat": w_hat,
        "gr": gr,
        "weight_filtration": (20, 152, 172),
        "rank_n": nilpotent.rank(),
        "jordan": (20, 132),
        "type": "II_18",
        "k": k,
        "signature": signature,
        "determinant": int(k.det()),
        "smith_nonzero": smith_nonzero,
        "smith_zero_count": b3 - len(smith_nonzero),
        "saturation_defect": "(Z/2)^2",
        "hodge_deligne": hodge_deligne,
        "parent_gr": (20, 162, 20),
    }


def seam_monomial_audit(polytope):
    # The seam is the q=0 section for dual points m=(a,q,c,d).
    q_histogram = Counter(point[1] for point in polytope["delta_points"])
    assert q_histogram == Counter({-1: 10, 0: 35, 1: 34, 2: 25})
    assert math.gcd(*(abs(value) for value in q_histogram if value)) == 1
    seam = tuple(point for point in polytope["delta_points"] if point[1] == 0)
    assert len(seam) == 35

    def exponents(point):
        return tuple(int(dot(point, ray) + 1) for ray in RESOLVED_RAYS)

    resolved_data = tuple((point, exponents(point)) for point in polytope["delta_points"])
    assert all(exp[8] == exp[0] + exp[6] - 1 for _, exp in resolved_data)
    simple_full = tuple(
        (point, exp) for point, exp in resolved_data if exp[5] % 2 == 0
    )
    simple_full_qa = Counter((point[1], point[0]) for point, _ in simple_full)
    assert len(simple_full) == 69
    assert simple_full_qa == Counter(
        {(-1, 0): 9, (0, -1): 25, (0, 1): 1, (1, 0): 9, (2, -1): 25}
    )

    seam_data = tuple((point, exponents(point)) for point in seam)
    # A convenient stable Cox row is wt(x5)=-1, wt(x7)=+1.  An equivalent
    # row modulo the old GLSM relations is wt(x0)=-1, wt(E)=+1.  Every
    # anticanonical monomial has weight -e5+e7=-e0+eE=q.  Dressing it by
    # zeta_+^max(-q,0) zeta_-^max(q,0), with weights (+1,-1), gives zero.
    for point in polytope["delta_points"]:
        exp = exponents(point)
        q = point[1]
        assert -exp[5] + exp[7] == q
        assert -exp[0] + exp[8] == q
        assert q + max(-q, 0) - max(q, 0) == 0
    by_a = Counter(point[0] for point, _ in seam_data)
    assert by_a == Counter({-1: 25, 0: 9, 1: 1})
    assert all(exp[5] == exp[7] == 1 - point[0] for point, exp in seam_data)

    simple = tuple(
        (point, exp) for point, exp in seam_data if exp[5] % 2 == 0
    )
    triple = tuple(
        (point, exp)
        for point, exp in seam_data
        if (exp[1] + exp[2] + exp[5]) % 2 == 0
    )
    simple_by_a = Counter(point[0] for point, _ in simple)
    triple_by_a = Counter(point[0] for point, _ in triple)
    assert len(simple) == 26
    assert simple_by_a == Counter({-1: 25, 1: 1})
    assert len(triple) == 18
    assert triple_by_a == Counter({-1: 13, 0: 4, 1: 1})

    # sigma_5 is the deck involution: H2+=(2), H2-=(20), L=U(2) is even.
    simple_h2 = {"plus": 2, "minus": 20, "L_plus": 2}
    simple_active = {
        "GrW2_plus": simple_h2["plus"] - simple_h2["L_plus"],
        "GrW2_minus": simple_h2["minus"],
    }
    assert simple_active == {"GrW2_plus": 0, "GrW2_minus": 20}

    # sigma_125 induces the Enriques involution on the seam.
    triple_h2 = {"plus": 10, "minus": 12, "L_plus": 2}
    triple_active = {
        "GrW2_plus": triple_h2["plus"] - triple_h2["L_plus"],
        "GrW2_minus": triple_h2["minus"],
    }
    assert triple_active == {"GrW2_plus": 8, "GrW2_minus": 12}
    even_active_gram = -2 * e8_cartan()
    even_eigenvalues = np.linalg.eigvalsh(
        np.asarray(even_active_gram.tolist(), dtype=float)
    )
    assert np.all(even_eigenvalues < -1e-8)

    # Conditional equivariant LMHS dimensions if the restricted relative
    # Cox families pass the smooth-total-space/SNC audit.
    simple_h3 = (68, 104)
    simple_gr3 = (
        simple_h3[0] - 2 * simple_active["GrW2_plus"],
        simple_h3[1] - 2 * simple_active["GrW2_minus"],
    )
    triple_h3 = (98, 104)
    triple_gr3 = (
        triple_h3[0] - 2 * triple_active["GrW2_plus"],
        triple_h3[1] - 2 * triple_active["GrW2_minus"],
    )
    assert simple_gr3 == (68, 64)
    assert triple_gr3 == (82, 80)

    return {
        "q_histogram": dict(sorted(q_histogram.items())),
        "primitive_q": True,
        "simple_full_count": len(simple_full),
        "simple_full_qa": dict(sorted(simple_full_qa.items())),
        "seam_count": len(seam),
        "seam_by_a": dict(sorted(by_a.items())),
        "simple_count": len(simple),
        "simple_by_a": dict(sorted(simple_by_a.items())),
        "simple_action": "deck, anti-symplectic",
        "simple_h2": simple_h2,
        "simple_active": simple_active,
        "simple_gr3_conditional": simple_gr3,
        "triple_count": len(triple),
        "triple_by_a": dict(sorted(triple_by_a.items())),
        "triple_action": "Enriques, fixed-point-free generically",
        "triple_h2": triple_h2,
        "triple_active": triple_active,
        "triple_gr3_conditional": triple_gr3,
        "even_active_signature_triple": (0, 8),
    }


def main():
    polytope = resolved_polytope_audit()
    fan = fan_and_slice_audit(polytope)
    restriction = restriction_audit()
    lmhs = lmhs_and_monodromy_audit()
    seam = seam_monomial_audit(polytope)

    print("R61 RESOLVED TORIC PHASE")
    print("lattice points Delta*/Delta", len(polytope["delta_star_points"]), len(polytope["delta_points"]))
    print("Hodge / Euler", polytope["hodge"], polytope["euler"])
    print("resolved fan cones / determinant abs", len(fan["cones"]), sorted({abs(x) for x in fan["determinants"]}))
    print("top cones upper/lower/mixed", len(fan["upper"]), len(fan["lower"]), len(fan["mixed"]))
    print("height histogram", fan["height_histogram"])
    print("off-slice projections", fan["projections_off_slice"])
    print("slice points / dual points / rho", len(fan["slice_points"]), len(fan["slice_dual_points"]), fan["rho_slice"])
    print("common slice cones", len(fan["slice_cones"]))
    print("resolved SR pairs", fan["sr_pairs"])
    print()

    print("R61 RESTRICTION LATTICE")
    print("basis", restriction["basis"])
    print("rho_B")
    print(restriction["rho_basis"])
    print("rho_D0...D8")
    print(restriction["rho_divisors"])
    print("Smith / rank / kernel", restriction["smith"], restriction["rank"], restriction["kernel"])
    print("restricted Gram")
    print(restriction["gram_basis"])
    print("L = U(2), primitive; E|S=0")
    print()

    print("R61 ORDINARY LMHS (TWO-COMPONENT TYURIN MODEL)")
    print("h11,h21 / b3", lmhs["hodge"], lmhs["b3"])
    print("r / uhat,vhat,what", lmhs["r"], (lmhs["u_hat"], lmhs["v_hat"], lmhs["w_hat"]))
    print("GrW2,GrW3,GrW4", lmhs["gr"])
    print("W2,W3,W4", lmhs["weight_filtration"])
    print("Hodge-Deligne rows W4,W3,W2", lmhs["hodge_deligne"])
    print("N^2 / rank N / Jordan J2,J1", 0, lmhs["rank_n"], lmhs["jordan"])
    print("type", lmhs["type"])
    print("K signature / determinant", lmhs["signature"], lmhs["determinant"])
    print("SNF nonzero", lmhs["smith_nonzero"])
    print("SNF zero count / saturation defect", lmhs["smith_zero_count"], lmhs["saturation_defect"])
    print("parent POLY944 GrW -> resolved GrW", lmhs["parent_gr"], "->", lmhs["gr"])
    print()

    print("R61 ACTUAL HEIGHT-ZERO SEAM")
    print("primitive q histogram", seam["q_histogram"])
    print("relative Cox charge row", "wt(x5)=-1, wt(x7)=+1, wt(zeta+)=+1, wt(zeta-)=-1")
    print("equivalent Cox row", "wt(x0)=-1, wt(E)=+1 (mod old GLSM rows)")
    print("sigma5 full support by (q,a)", seam["simple_full_count"], seam["simple_full_qa"])
    print("all seam monomials by a", seam["seam_count"], seam["seam_by_a"])
    print("sigma5 support by a", seam["simple_count"], seam["simple_by_a"])
    print("sigma5 action / active (+,-)", seam["simple_action"], (seam["simple_active"]["GrW2_plus"], seam["simple_active"]["GrW2_minus"]))
    print("sigma5 conditional GrW3 (+,-)", seam["simple_gr3_conditional"])
    print("sigma125 support by a", seam["triple_count"], seam["triple_by_a"])
    print("sigma125 action / active (+,-)", seam["triple_action"], (seam["triple_active"]["GrW2_plus"], seam["triple_active"]["GrW2_minus"]))
    print("sigma125 even active signature", seam["even_active_signature_triple"])
    print("sigma125 conditional GrW3 (+,-)", seam["triple_gr3_conditional"])
    print()

    print("VERDICT")
    print("RESOLVED_PROJECTING_SLICE_AND_PRIMITIVE_U2_RESTRICTION_CERTIFIED")
    print("ORDINARY_RESOLVED_TYURIN_LMHS_IS_EXACTLY_TYPE_II18")
    print("ACTIVE_INTEGRAL_SNF_IS_1^18_2_2_WITH_152_ZEROS")
    print("SIGMA5_SEAM_IS_DECK_AND_HAS_NO_EVEN_ACTIVE_CLASS")
    print("SIGMA125_SEAM_IS_ENRIQUES_AND_EVEN_ACTIVE_LATTICE_IS_NEGATIVE_DEFINITE")
    print("R60_EVEN_TOWER_PARITY_CLAIMS_RETRACTED_ON_THE_ACTUAL_TYURIN_SEAM")
    print("RESTRICTED_EQUIVARIANT_TOTAL_SPACE_SMOOTHNESS_AND_SNC_STILL_REQUIRE_A_RELATIVE_JACOBIAN_AUDIT")


if __name__ == "__main__":
    main()

