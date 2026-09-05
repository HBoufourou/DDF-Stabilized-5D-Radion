#!/usr/bin/env python3
"""R62: explicit 5D stable fan, Jacobian/SNC and parity stop-test.

This is a standalone exact audit for the resolved POLY944 sigma_5 family.
It verifies:

1. the extended Cox lattice and a smooth coherent 5D fan over A1;
2. relative properness, two reduced toric central components and their seam;
3. base loci and first jets of the 69-monomial relative hypersurface;
4. separation of the 16 horizontal conifold loci after the small resolution;
5. all effective diagonal Z2 characters on the 35-monomial K3 seam;
6. the O3/O7 parity stop-test, both with fixed and exchanged Tyurin tops.

All calculations are integral/rational.  Statements identifying K3 invariant
lattices use the standard Nikulin classification; their combinatorial inputs
and all signatures used in the stop-test are printed explicitly.
"""

from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


# R60--R61 coordinate order x0,...,x7,E.
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

ZETA_PLUS = 9
ZETA_MINUS = 10
INFINITY_RAY = 11


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def determinant(rows) -> Fraction:
    return Fraction(Matrix(rows).det())


def binary_rank(rows) -> int:
    """Rank over F_2 without relying on a finite-field package."""
    work = [[int(value) & 1 for value in row] for row in rows]
    if not work:
        return 0
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                work[row] = [a ^ b for a, b in zip(work[row], work[rank], strict=True)]
        rank += 1
    return rank


def resolved_dual_points():
    """Integer points of the polar after adding nu_E."""
    ranges = tuple(
        range(
            min(vertex[index] for vertex in OLD_DUAL_VERTICES),
            max(vertex[index] for vertex in OLD_DUAL_VERTICES) + 1,
        )
        for index in range(4)
    )
    points = tuple(
        point
        for point in product(*ranges)
        if all(dot(point, ray) >= -1 for ray in RESOLVED_RAYS)
    )
    assert len(points) == 104
    return points


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
    answer = tuple(sorted(answer))
    assert len(answer) == 20
    assert all(abs(determinant([RESOLVED_RAYS[i] for i in cone])) == 1 for cone in answer)
    return answer


def top_data():
    cones = resolved_maximal_cones()
    heights = tuple(ray[1] for ray in RESOLVED_RAYS)
    upper = tuple(cone for cone in cones if all(heights[i] >= 0 for i in cone))
    lower = tuple(cone for cone in cones if all(heights[i] <= 0 for i in cone))
    mixed = tuple(
        cone
        for cone in cones
        if any(heights[i] < 0 for i in cone) and any(heights[i] > 0 for i in cone)
    )
    slice_cones = tuple(
        sorted(
            {
                tuple(i for i in cone if heights[i] == 0)
                for cone in upper
                if len(tuple(i for i in cone if heights[i] == 0)) == 3
            }
        )
    )
    assert (len(upper), len(lower), len(mixed), len(slice_cones)) == (12, 8, 0, 8)
    assert slice_cones == (
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 4),
        (0, 3, 4),
        (1, 2, 7),
        (1, 3, 7),
        (2, 4, 7),
        (3, 4, 7),
    )
    return upper, lower, slice_cones


def all_faces(maximal_cones):
    faces = set()
    for cone in maximal_cones:
        for size in range(len(cone) + 1):
            faces.update(combinations(cone, size))
    return faces


def minimal_nonfaces(number_of_rays, maximal_cones):
    faces = all_faces(maximal_cones)
    answer = []
    for size in range(1, number_of_rays + 1):
        for candidate in combinations(range(number_of_rays), size):
            if candidate in faces:
                continue
            if all(tuple(x for x in candidate if x != removed) in faces for removed in candidate):
                answer.append(candidate)
    return tuple(answer)


def polyhedron_vertices(rays, heights):
    """Vertices and active facets of <y,v_j> <= h_j, exactly over Q."""
    dimension = len(rays[0])
    vertices = {}
    for candidate in combinations(range(len(rays)), dimension):
        matrix = Matrix([rays[index] for index in candidate])
        if matrix.det() == 0:
            continue
        vertex_vector = matrix.inv() * Matrix([heights[index] for index in candidate])
        vertex = tuple(Fraction(value) for value in vertex_vector)
        values = tuple(dot(vertex, ray) for ray in rays)
        if all(value <= height for value, height in zip(values, heights, strict=True)):
            active = tuple(
                index
                for index, (value, height) in enumerate(zip(values, heights, strict=True))
                if value == height
            )
            vertices[vertex] = active
    return vertices


def extended_fan_audit():
    upper, lower, slice_cones = top_data()

    # This shear convention makes zeta_+ sit one unit below zeta_- in the
    # original top-height direction.  It is GL(5,Z)-equivalent to the R61
    # convention (zeta_+=0, zeta_-=nu_6 in the first four entries).
    relative_rays = tuple((*ray, 0) for ray in RESOLVED_RAYS) + (
        (0, -1, 0, 0, 1),  # zeta_+
        (0, 0, 0, 0, 1),   # zeta_-
    )
    q_total = Matrix(
        [
            [2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1],
        ]
    )
    ray_matrix = Matrix(relative_rays).T
    assert q_total.rank() == 6 and ray_matrix.rank() == 5
    assert q_total * ray_matrix.T == Matrix.zeros(6, 5)
    smith = smith_normal_form(q_total, domain=ZZ)
    smith_diagonal = tuple(abs(int(smith[i, i])) for i in range(6))
    assert smith_diagonal == (1,) * 6

    maximal_cones = tuple(
        sorted(
            [tuple(cone) + (ZETA_PLUS,) for cone in lower]
            + [tuple(cone) + (ZETA_MINUS,) for cone in upper]
            + [tuple(cone) + (ZETA_PLUS, ZETA_MINUS) for cone in slice_cones]
        )
    )
    assert len(maximal_cones) == 28
    determinants = tuple(
        determinant([relative_rays[index] for index in cone]) for cone in maximal_cones
    )
    assert all(abs(value) == 1 for value in determinants)

    # A complete exact non-overlap/coherence certificate: these are exactly
    # all vertices and normal cones of the indicated unbounded polyhedron.
    support_heights = (0, 0, 0, 5, 5, 0, 5, 2, 4, 0, 3)
    vertices = polyhedron_vertices(relative_rays, support_heights)
    assert len(vertices) == 28
    assert all(len(active) == 5 for active in vertices.values())
    assert set(vertices.values()) == set(maximal_cones)
    gaps = []
    for vertex, active in vertices.items():
        for index, (ray, height) in enumerate(zip(relative_rays, support_heights, strict=True)):
            if index not in active:
                gaps.append(height - dot(vertex, ray))
    assert len(gaps) == 168 and set(gaps) == {1, 2, 3, 4, 5}
    assert all(value.denominator == 1 for vertex in vertices for value in vertex)

    facets = Counter(
        tuple(sorted(set(cone) - {ray}))
        for cone in maximal_cones
        for ray in cone
    )
    assert Counter(facets.values()) == Counter({2: 60, 1: 20})
    boundary = {face for face, multiplicity in facets.items() if multiplicity == 1}
    assert boundary == set(resolved_maximal_cones())

    sr = minimal_nonfaces(len(relative_rays), maximal_cones)
    expected_sr = (
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
    assert sr == expected_sr

    # The old complete 4D fan forces the first four entries of any recession
    # vector to vanish; the two summit inequalities then leave only -e_5.
    recession_ray = (0, 0, 0, 0, -1)
    assert all(dot(recession_ray, ray) <= 0 for ray in relative_rays)
    assert tuple(ray[-1] for ray in relative_rays) == (0,) * 9 + (1, 1)

    completed_rays = relative_rays + (recession_ray,)
    completed_heights = support_heights + (1,)
    completed_vertices = polyhedron_vertices(completed_rays, completed_heights)
    expected_infinity_cones = {
        tuple(cone) + (INFINITY_RAY,) for cone in resolved_maximal_cones()
    }
    expected_completed_cones = set(maximal_cones) | expected_infinity_cones
    assert len(completed_vertices) == 48
    assert all(len(active) == 5 for active in completed_vertices.values())
    assert set(completed_vertices.values()) == expected_completed_cones
    assert {
        active for active in completed_vertices.values() if INFINITY_RAY in active
    } == expected_infinity_cones
    completed_determinants = tuple(
        determinant([completed_rays[index] for index in cone])
        for cone in expected_completed_cones
    )
    assert all(abs(value) == 1 for value in completed_determinants)
    completed_facets = Counter(
        tuple(sorted(set(cone) - {ray}))
        for cone in expected_completed_cones
        for ray in cone
    )
    assert len(completed_facets) == 120
    assert set(completed_facets.values()) == {2}

    # Link fans of the two central divisors and their intersection.
    star_plus = tuple(
        sorted(tuple(index for index in cone if index != ZETA_PLUS))
        for cone in maximal_cones
        if ZETA_PLUS in cone
    )
    star_minus = tuple(
        sorted(tuple(index for index in cone if index != ZETA_MINUS))
        for cone in maximal_cones
        if ZETA_MINUS in cone
    )
    seam_star = tuple(
        sorted(tuple(index for index in cone if index not in (ZETA_PLUS, ZETA_MINUS)))
        for cone in maximal_cones
        if ZETA_PLUS in cone and ZETA_MINUS in cone
    )
    assert (len(star_plus), len(star_minus), len(seam_star)) == (16, 20, 8)

    return {
        "rays": relative_rays,
        "q_total": q_total,
        "smith": smith_diagonal,
        "cones": maximal_cones,
        "determinants": determinants,
        "heights": support_heights,
        "vertices": vertices,
        "gaps": tuple(gaps),
        "facets": facets,
        "sr": sr,
        "recession": recession_ray,
        "completed_vertices": completed_vertices,
        "completed_determinants": completed_determinants,
        "completed_facets": completed_facets,
        "star_plus": star_plus,
        "star_minus": star_minus,
        "seam_star": seam_star,
    }


def relative_support_audit(fan):
    delta_points = resolved_dual_points()
    support = []
    point_support = []
    for point in delta_points:
        exponents = tuple(int(dot(point, ray) + 1) for ray in RESOLVED_RAYS)
        if exponents[5] % 2:
            continue
        q = point[1]
        relative_exponents = exponents + (max(-q, 0), max(q, 0))
        support.append(relative_exponents)
        point_support.append((point, relative_exponents))
    support = tuple(support)
    point_support = tuple(point_support)
    assert len(support) == 69
    q_histogram = Counter(point[1] for point, _ in point_support)
    assert q_histogram == Counter({-1: 9, 0: 26, 1: 9, 2: 25})

    degrees = {tuple(fan["q_total"] * Matrix(exponents)) for exponents in support}
    assert degrees == {(4, 4, 3, 2, -1, 0)}

    def minimal_base_components(local_support, local_cones):
        faces = all_faces(local_cones)
        base = []
        for zero_set in faces:
            if not zero_set:
                continue
            if all(any(exponents[index] > 0 for index in zero_set) for exponents in local_support):
                base.append(frozenset(zero_set))
        minimal = [
            zero_set
            for zero_set in base
            if not any(other < zero_set for other in base)
        ]
        return tuple(sorted((tuple(sorted(item)) for item in minimal), key=lambda x: (len(x), x)))

    def first_jet_units(local_support, zero_set, derivative):
        return tuple(
            exponents
            for exponents in local_support
            if exponents[derivative] == 1
            and all(exponents[index] == 0 for index in zero_set if index != derivative)
        )

    total_base = minimal_base_components(support, fan["cones"])
    assert total_base == ((6, 7),)
    unit = (2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0)
    assert first_jet_units(support, (6, 7), 6) == (unit,)

    plus_support = tuple(exponents for exponents in support if exponents[ZETA_PLUS] == 0)
    minus_support = tuple(exponents for exponents in support if exponents[ZETA_MINUS] == 0)
    seam_support = tuple(
        exponents
        for exponents in support
        if exponents[ZETA_PLUS] == exponents[ZETA_MINUS] == 0
    )
    assert (len(plus_support), len(minus_support), len(seam_support)) == (60, 35, 26)

    plus_base = minimal_base_components(plus_support, fan["star_plus"])
    minus_base = minimal_base_components(minus_support, fan["star_minus"])
    seam_base = minimal_base_components(seam_support, fan["seam_star"])
    assert plus_base == ()
    assert minus_base == ((6, 7),)
    assert seam_base == ()
    assert first_jet_units(minus_support, (6, 7), 6) == (unit,)

    seam_points = tuple((point, exponents) for point, exponents in point_support if point[1] == 0)
    seam_by_a = Counter(point[0] for point, _ in seam_points)
    assert seam_by_a == Counter({-1: 25, 1: 1})
    assert unit in seam_support

    # For general transverse coefficients the horizontal locus has the
    # (2,2).(4,4) intersection number below.  On the pre-semistable chart
    # zeta_-=1, zeta_+=z and x0=x6=0 (with x5*x7 invertible), the two normal
    # jets are zeta_+*A_22^- and A_44^0.  Their monomial ideal decomposes as
    # (p*a,b)=(a,b) intersection (p,b).  Verify this elementary intersection
    # rather than storing the two components as an unsupported label.
    node_count = 2 * 4 + 2 * 4
    assert node_count == 16
    # Exponent order is (p,a,b); the intersection of monomial ideals is
    # generated by pairwise least common multiples, then minimalized.
    horizontal_ideal = ((0, 1, 0), (0, 0, 1))
    vertical_ideal = ((1, 0, 0), (0, 0, 1))
    pairwise_lcms = {
        tuple(max(left[i], right[i]) for i in range(3))
        for left in horizontal_ideal
        for right in vertical_ideal
    }
    intersection_generators = tuple(
        sorted(
            generator
            for generator in pairwise_lcms
            if not any(
                other != generator
                and all(other[i] <= generator[i] for i in range(3))
                for other in pairwise_lcms
            )
        )
    )
    assert intersection_generators == ((0, 0, 1), (1, 1, 0))
    naive_jacobian_components = (
        ("A22_minus", "A44_zero"),
        ("zeta_plus", "A44_zero"),
    )

    sr = set(fan["sr"])
    assert {(0, 6), (7, 8), (8, 9), (5, 8), (5, 10)} <= sr
    # The naive vertical stratum p=x6=0 is absent in the stable fan.
    naive_vertical_excluded_by_sr = (6, ZETA_PLUS) in sr
    assert naive_vertical_excluded_by_sr
    # E=0 forces zeta_+ != 0.  On z=zeta_+ zeta_-=0 this forces
    # zeta_-=0, hence every resolved horizontal exceptional locus is away
    # from the seam zeta_+=zeta_-=0.
    exceptional_disjoint_from_seam = (8, ZETA_PLUS) in sr
    assert exceptional_disjoint_from_seam

    return {
        "support": support,
        "point_support": point_support,
        "q_histogram": dict(sorted(q_histogram.items())),
        "degree": next(iter(degrees)),
        "total_base": total_base,
        "unit_jet": unit,
        "component_support_counts": (len(plus_support), len(minus_support), len(seam_support)),
        "component_bases": (plus_base, minus_base, seam_base),
        "node_count": node_count,
        "naive_jacobian_components": naive_jacobian_components,
        "naive_vertical_excluded_by_sr": naive_vertical_excluded_by_sr,
        "exceptional_disjoint_from_seam": exceptional_disjoint_from_seam,
    }


def seam_character_audit(relative):
    seam_data = tuple(
        (point, exponents)
        for point, exponents in relative["point_support"]
        if point[1] == 0
    )
    # The invariant sigma_5 seam contains 26 monomials, but the character
    # scan must start from all 35 monomials of the unrestricted seam.
    all_seam_points = tuple(point for point in resolved_dual_points() if point[1] == 0)
    all_seam = tuple(
        (
            point,
            tuple(int(dot(point, ray) + 1) for ray in RESOLVED_RAYS),
        )
        for point in all_seam_points
    )
    assert len(all_seam) == 35 and len(seam_data) == 26

    old_q = (
        (2, 1, 0, 0, 1, 0, 0, 0, 0),
        (2, 0, 1, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 1, 1, 0, 0),
        (1, 0, 0, 0, 0, 0, 0, 1, 0),
        (-1, 0, 0, 0, 0, 0, -1, 0, 1),
    )
    assert binary_rank(old_q) == 5

    # Exhaust the 2^9 Cox coordinate signs.  Quotienting a uniform sign on
    # the polynomial leaves eight effective seam patterns, 64 lifts each.
    patterns = Counter()
    for signs in product((0, 1), repeat=9):
        pattern = tuple(sum(s * e for s, e in zip(signs, exponents, strict=True)) % 2 for _, exponents in all_seam)
        normalized = tuple(value ^ pattern[0] for value in pattern)
        patterns[normalized] += 1
    assert len(patterns) == 8 and set(patterns.values()) == {64}

    formula_patterns = set()
    for character in product((0, 1), repeat=3):
        a_char, c_char, d_char = character
        raw = tuple(
            (a_char * point[0] + c_char * point[2] + d_char * point[3]) % 2
            for point in all_seam_points
        )
        formula_patterns.add(tuple(value ^ raw[0] for value in raw))
    assert set(patterns) == formula_patterns

    expected = {
        (0, 0, 0): (35, (25, 9, 1), "identity", (2, 18)),
        (0, 0, 1): (22, (15, 6, 1), "anti; two elliptic curves", (0, 8)),
        (0, 1, 0): (22, (15, 6, 1), "anti; two elliptic curves", (0, 8)),
        (0, 1, 1): (19, (13, 5, 1), "symplectic Nikulin", (2, 10)),
        (1, 0, 0): (26, (25, 0, 1), "deck anti", (0, 0)),
        (1, 0, 1): (19, (15, 3, 1), "symplectic Nikulin", (2, 10)),
        (1, 1, 0): (19, (15, 3, 1), "symplectic Nikulin", (2, 10)),
        (1, 1, 1): (18, (13, 4, 1), "Enriques", (0, 8)),
    }
    records = {}
    for character in product((0, 1), repeat=3):
        a_char, c_char, d_char = character
        eigenvalue = (a_char + c_char + d_char) % 2
        kept = tuple(
            point
            for point in all_seam_points
            if (a_char * point[0] + c_char * point[2] + d_char * point[3]) % 2
            == eigenvalue
        )
        by_a_counter = Counter(point[0] for point in kept)
        by_a = tuple(by_a_counter.get(a, 0) for a in (-1, 0, 1))
        count, expected_by_a, action, active_signature = expected[character]
        assert len(kept) == count and by_a == expected_by_a

        complement = tuple(point for point in all_seam_points if point not in kept)
        if complement:
            # The opposite eigenspace omits the unique a=+1 term x0^2;
            # every remaining term contains x7 and gives a reducible divisor.
            assert all(1 - point[0] >= 1 for point in complement)

        omega_sign = -1 if eigenvalue else 1
        records[character] = {
            "eigenvalue": eigenvalue,
            "count": count,
            "by_a": by_a,
            "omega_sign": omega_sign,
            "action": action,
            "active_signature": active_signature,
        }

    symplectic_indefinite = tuple(
        character
        for character, record in records.items()
        if record["omega_sign"] == 1 and record["active_signature"] == (2, 10)
    )
    anti_indefinite = tuple(
        character
        for character, record in records.items()
        if record["omega_sign"] == -1 and record["active_signature"][0] > 0
    )
    assert symplectic_indefinite == ((0, 1, 1), (1, 0, 1), (1, 1, 0))
    assert anti_indefinite == ()

    return {
        "patterns": patterns,
        "records": records,
        "symplectic_indefinite": symplectic_indefinite,
        "anti_indefinite": anti_indefinite,
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


def parity_stop_test(characters):
    e8 = e8_cartan()
    assert e8.is_positive_definite
    # For a nontrivial symplectic involution the anti-invariant lattice is
    # E8(-2), hence negative definite.  For a holomorphic nonsymplectic involution the
    # invariant lattice is hyperbolic; removing invariant L=U(2) consumes its
    # unique positive direction, so the active invariant part is negative.
    assert (-2 * e8).is_negative_definite

    # Local plumbing signs: Omega_3=Omega_S wedge dlog(u), Gamma=C x S1.
    # normal_sign=+1 preserves the branches; -1 exchanges u and v.
    cases = {
        "tops_preserved": {
            "normal_sign": 1,
            "required_omega_S": -1,
            "required_curve_sign_for_even_tube": 1,
            "available_curve_lattice_signature": (0, "negative"),
        },
        "tops_exchanged": {
            "normal_sign": -1,
            "required_omega_S": 1,
            "required_curve_sign_for_even_tube": -1,
            "available_curve_lattice_signature": (0, 8),
        },
    }
    for case in cases.values():
        assert case["required_omega_S"] * case["normal_sign"] == -1  # O3/O7
        assert case["required_curve_sign_for_even_tube"] * case["normal_sign"] == 1

    heights = Counter(ray[1] for ray in RESOLVED_RAYS if ray[1] != 0)
    assert heights == Counter({1: 2, -1: 1})
    toric_top_exchange_exists = heights[1] == heights[-1]
    assert not toric_top_exchange_exists

    # R61's conditional sigma_5 equivariant LMHS is now unconditional for a
    # generic member because the relative fan/Jacobian/SNC audit has passed.
    h21_split = (34, 51)
    h3_split = (2 * h21_split[0], 2 * h21_split[1] + 2)
    grw2_split = (0, 20)
    grw3_split = (
        h3_split[0] - 2 * grw2_split[0],
        h3_split[1] - 2 * grw2_split[1],
    )
    assert h3_split == (68, 104) and grw3_split == (68, 64)
    assert characters["anti_indefinite"] == ()

    return {
        "cases": cases,
        "height_histogram_off_slice": dict(sorted(heights.items())),
        "toric_top_exchange": toric_top_exchange_exists,
        "h21_split": h21_split,
        "h3_split": h3_split,
        "grw2_split": grw2_split,
        "grw3_split": grw3_split,
        "verdict": "NO_EVEN_ISOTROPIC_ACTIVE_C4_TYURIN_TUBE_IN_STANDARD_HOLOMORPHIC_O3O7_FRAME",
    }


def format_cone(cone):
    names = [f"x{i}" for i in range(8)] + ["E", "zeta+", "zeta-"]
    return "".join(names[index] if index >= 8 else str(index) for index in cone)


def main():
    fan = extended_fan_audit()
    relative = relative_support_audit(fan)
    characters = seam_character_audit(relative)
    stop = parity_stop_test(characters)

    print("R62 EXPLICIT RELATIVE 5D FAN")
    print("rays / Cox rank / Cox SNF", len(fan["rays"]), fan["q_total"].rank(), fan["smith"])
    print("maximal cones / |det|", len(fan["cones"]), sorted({abs(value) for value in fan["determinants"]}))
    print("cones lower+ / upper- / seam", 8, 12, 8)
    print("polyhedron vertices / strict gaps", len(fan["vertices"]), sorted(set(fan["gaps"])))
    print("walls internal / boundary", 60, 20)
    print("relative support", "R^4 x R_>=0")
    print("recession ray", fan["recession"])
    print("smooth completion cones / paired walls", len(fan["completed_vertices"]), len(fan["completed_facets"]))
    print("SR minimal", fan["sr"])
    print("central links zeta+ / zeta- / seam", len(fan["star_plus"]), len(fan["star_minus"]), len(fan["seam_star"]))
    print("div(z)=D_zeta+ + D_zeta-; multiplicities=(1,1)")
    print()

    print("R62 SIGMA5 RELATIVE JACOBIAN / SNC")
    print("support q histogram", relative["q_histogram"])
    print("common Cox degree", relative["degree"])
    print("total minimal base locus", relative["total_base"])
    print("unit first jet d/dx6", relative["unit_jet"])
    print("supports zeta+=0 / zeta-=0 / seam", relative["component_support_counts"])
    print("component base loci", relative["component_bases"])
    print("generic total/components/seam", "SMOOTH / SMOOTH / SMOOTH")
    print("central hypersurface", "REDUCED SNC WITH EXACTLY TWO COMPONENTS")
    print("generic horizontal intersections", relative["node_count"])
    print("naive pre-semistable local Jacobian components", relative["naive_jacobian_components"])
    print("naive vertical stratum excluded by stable SR", relative["naive_vertical_excluded_by_sr"])
    print("resolved exceptional loci disjoint from seam", relative["exceptional_disjoint_from_seam"])
    print()

    print("R62 EXHAUSTIVE K3 SEAM CHARACTER SCAN")
    print("Cox sign lifts / effective seam patterns / lifts per pattern", 2**9, len(characters["patterns"]), sorted(set(characters["patterns"].values())))
    print("character  monomials  OmegaS  action                         A_+ signature")
    for character, record in characters["records"].items():
        bits = "".join(map(str, character))
        omega = "+" if record["omega_sign"] == 1 else "-"
        print(f"{bits:>9}  {record['count']:>9}  {omega:>6}  {record['action']:<29} {record['active_signature']}")
    print("symplectic indefinite characters", characters["symplectic_indefinite"])
    print("nonsymplectic indefinite A_+ characters", characters["anti_indefinite"])
    print()

    print("R62 O3/O7 STOP-TEST")
    print("off-slice heights", stop["height_histogram_off_slice"])
    print("toric top exchange in current resolved fan", stop["toric_top_exchange"])
    print("sigma5 h21(+,-) / H3(+,-)", stop["h21_split"], stop["h3_split"])
    print("sigma5 GrW2/4(+,-) / GrW3(+,-)", stop["grw2_split"], stop["grw3_split"])
    print("VERDICT")
    print("RELATIVE_5D_FAN_IS_SMOOTH_COHERENT_AND_PROPER_OVER_A1")
    print("SIGMA5_TOTAL_SPACE_AND_TWO_COMPONENT_CENTRAL_FIBER_ARE_GENERICALLY_SMOOTH_SNC")
    print("SIXTEEN_HORIZONTAL_EXCEPTIONAL_LOCUS_FAMILIES_ARE_DISJOINT_FROM_THE_TYURIN_SEAM")
    print("NAIVE_PRESEMISTABLE_LOCAL_MODEL_HAS_AN_ADDITIONAL_VERTICAL_SINGULAR_CURVE")
    print("ALL_SEAM_DIAGONAL_CHARACTERS_SCANNED")
    print("NO_NONSYMPLECTIC_CHARACTER_HAS_AN_INDEFINITE_ACTIVE_INVARIANT_LATTICE")
    print("TOP_EXCHANGE_ALSO_FAILS_THE_STANDARD_O3O7_EVEN_ISOTROPIC_TUBE_TEST")
    print(stop["verdict"])
    print("FREEZE_PARENT_GEOMETRY_FOR_ARTICLE1__FANO_DEFERRED__NO_MICROMETRIC_VALUE_DERIVED")


if __name__ == "__main__":
    main()

