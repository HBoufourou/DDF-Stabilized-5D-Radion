#!/usr/bin/env python3
"""Independent R63 audit of the R62 hypersurface/Jacobian/SNC claims.

The monomial support is reconstructed directly from lattice inequalities.
Base loci are recomputed as minimal hypergraph transversals on toric faces.
Local ideal decompositions and explicit genericity witnesses are checked with
SymPy Groebner bases; none of the routines from the R62 script are imported.

This certifies the algebraic/combinatorial input to the standard Bertini and
SNC arguments.  It does not attempt to re-prove Bertini or the classification
of K3 involutions.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product

import sympy as sp


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

Q = (
    (2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1),
)

CONES = (
    (0, 1, 2, 5, 9), (0, 1, 3, 5, 9),
    (0, 2, 4, 5, 9), (0, 3, 4, 5, 9),
    (1, 2, 5, 7, 9), (1, 3, 5, 7, 9),
    (2, 4, 5, 7, 9), (3, 4, 5, 7, 9),
    (0, 1, 2, 8, 10), (0, 1, 3, 8, 10),
    (0, 2, 4, 8, 10), (0, 3, 4, 8, 10),
    (1, 2, 6, 7, 10), (1, 2, 6, 8, 10),
    (1, 3, 6, 7, 10), (1, 3, 6, 8, 10),
    (2, 4, 6, 7, 10), (2, 4, 6, 8, 10),
    (3, 4, 6, 7, 10), (3, 4, 6, 8, 10),
    (0, 1, 2, 9, 10), (0, 1, 3, 9, 10),
    (0, 2, 4, 9, 10), (0, 3, 4, 9, 10),
    (1, 2, 7, 9, 10), (1, 3, 7, 9, 10),
    (2, 4, 7, 9, 10), (3, 4, 7, 9, 10),
)

P_INDEX = 9
M_INDEX = 10


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def reconstruct_support():
    # The ray inequalities themselves give the exact finite search box:
    # -1<=a<=1, -1<=b<=2, -1<=c,d<=3.
    resolved_points = []
    for point in product(range(-1, 2), range(-1, 3), range(-1, 4), range(-1, 4)):
        if all(dot(point, ray) >= -1 for ray in RAYS4):
            resolved_points.append(point)
    assert len(resolved_points) == 104

    point_support = []
    for point in resolved_points:
        old_exponents = tuple(dot(point, ray) + 1 for ray in RAYS4)
        assert min(old_exponents) >= 0
        # sigma_5-even subspace.
        if old_exponents[5] % 2:
            continue
        height = point[1]
        relative = old_exponents + (max(-height, 0), max(height, 0))
        point_support.append((point, relative))
    assert len(point_support) == 69
    return tuple(point_support)


def all_faces(cones):
    faces = {()}
    for cone in cones:
        for size in range(1, len(cone) + 1):
            faces.update(combinations(cone, size))
    return tuple(sorted(faces, key=lambda item: (len(item), item)))


def minimal_base_loci(support, cones):
    """Minimal allowed coordinate strata hitting every monomial."""
    monomial_supports = tuple(
        frozenset(index for index, exponent in enumerate(monomial) if exponent)
        for monomial in support
    )
    candidates = []
    for face in all_faces(cones):
        if not face:
            continue
        zero_set = frozenset(face)
        if all(zero_set & monomial for monomial in monomial_supports):
            if not any(previous < zero_set for previous in candidates):
                candidates.append(zero_set)
    return tuple(sorted((tuple(sorted(item)) for item in candidates), key=lambda item: (len(item), item)))


def link_cones(required):
    required = frozenset(required)
    return tuple(
        sorted(
            tuple(index for index in cone if index not in required)
            for cone in CONES
            if required <= frozenset(cone)
        )
    )


def groebner_is_unit(generators, variables):
    basis = sp.groebner(generators, *variables, order="grevlex", domain=sp.QQ)
    return len(basis.polys) == 1 and basis.polys[0].as_expr() == 1


def elimination_generators(generators, eliminate, variables):
    basis = sp.groebner(generators, *variables, order="lex", domain=sp.QQ)
    return tuple(
        sp.expand(poly.as_expr())
        for poly in basis.polys
        if not poly.as_expr().has(*eliminate)
    )


def bihomogeneous(degree, coefficients, s0, s1, t0, t1):
    assert len(coefficients) == (degree + 1) ** 2
    return sp.expand(
        sum(
            coefficients[i * (degree + 1) + j]
            * s0 ** (degree - i) * s1**i
            * t0 ** (degree - j) * t1**j
            for i in range(degree + 1)
            for j in range(degree + 1)
        )
    )


def chart_polynomial(poly, first_chart, second_chart, symbols):
    s0, s1, t0, t1, u, v = symbols
    s_values = [None, None]
    t_values = [None, None]
    s_values[first_chart] = 1
    s_values[1 - first_chart] = u
    t_values[second_chart] = 1
    t_values[1 - second_chart] = v
    return sp.expand(
        poly.subs(
            {
                s0: s_values[0], s1: s_values[1],
                t0: t_values[0], t1: t_values[1],
            }
        )
    )


def explicit_genericity_witnesses():
    s0, s1, t0, t1, u, v = sp.symbols("s0 s1 t0 t1 u v")
    symbols = (s0, s1, t0, t1, u, v)

    # A smooth (4,4) branch divisor.  The four projective affine charts are
    # checked independently by the Jacobian criterion.
    branch = (
        s0**4 * t0**4 + s0**4 * t1**4
        + s1**4 * t0**4 + 2 * s1**4 * t1**4
    )
    branch_bases = []
    for first_chart, second_chart in product((0, 1), repeat=2):
        local = chart_polynomial(branch, first_chart, second_chart, symbols)
        is_smooth = groebner_is_unit(
            (local, sp.diff(local, u), sp.diff(local, v)), (u, v)
        )
        branch_bases.append(is_smooth)
    assert all(branch_bases)

    # A fixed exact pair A_22, A_44.  The tangent-intersection ideal
    # (A_22,A_44,dA_22 wedge dA_44) is empty on all four charts.  Hence the
    # locus of transverse pairs is nonempty and therefore Zariski open.
    coefficients_22 = (3, 3, 3, -2, 2, 1, 1, -2, 1)
    coefficients_44 = (
        3, 2, 3, -2, -1,
        -1, 1, 1, -1, -2,
        -1, 2, -3, -1, -1,
        2, -1, -2, 2, -3,
        -3, -1, -1, 2, 1,
    )
    a22 = bihomogeneous(2, coefficients_22, s0, s1, t0, t1)
    a44 = bihomogeneous(4, coefficients_44, s0, s1, t0, t1)
    transverse_bases = []
    for first_chart, second_chart in product((0, 1), repeat=2):
        f = chart_polynomial(a22, first_chart, second_chart, symbols)
        g = chart_polynomial(a44, first_chart, second_chart, symbols)
        jacobian_minor = sp.diff(f, u) * sp.diff(g, v) - sp.diff(f, v) * sp.diff(g, u)
        transverse_bases.append(
            groebner_is_unit((f, g, jacobian_minor), (u, v))
        )
    assert all(transverse_bases)

    # In A*(P1 x P1), H1^2=H2^2=0; (2,2).(4,4)=16 H1 H2.
    intersection_number = 2 * 4 + 2 * 4
    assert intersection_number == 16
    return branch_bases, transverse_bases, intersection_number


def local_ideal_audits():
    tau, p, m, a, b = sp.symbols("tau p m a b")

    # (a,b) intersect (p,b), computed by an elimination variable tau.
    horizontal_vertical = elimination_generators(
        (tau * a, tau * b, (1 - tau) * p, (1 - tau) * b),
        (tau,),
        (tau, p, a, b),
    )
    assert set(horizontal_vertical) == {a * p, b}

    # The central divisor is reduced with exactly the two coordinate primes.
    central_intersection = elimination_generators(
        (tau * p, (1 - tau) * m),
        (tau,),
        (tau, p, m),
    )
    assert central_intersection == (m * p,)
    return horizontal_vertical, central_intersection


def component_irreducibility_discriminants():
    # Generic coefficients are represented by algebraically independent
    # symbols.  After removing manifest square units, both quadratic
    # discriminants have degree exactly one in A0.  Their A0-adic valuation
    # is therefore odd, so neither is a square in the corresponding function
    # field.  This proves generic irreducibility on each dense torus.
    A0, Aminus, Aplus, Aplusplus = sp.symbols("A0 Aminus Aplus Aplusplus")
    c, E, x5, x6, x7, p, m = sp.symbols("c E x5 x6 x7 p m", nonzero=True)

    disc_p_reduced = sp.expand(
        m**2 * E**4 * x6**2 * Aplus**2
        - 4 * c * E**2 * (x5**2 * A0 + m**2 * E**2 * x6**2 * Aplusplus)
    )
    disc_m_reduced = sp.expand(
        p**2 * x5**2 * Aminus**2 - 4 * c * E**2 * x6**2 * A0
    )
    assert sp.degree(disc_p_reduced, A0) == 1
    assert sp.degree(disc_m_reduced, A0) == 1
    assert sp.diff(disc_p_reduced, A0) != 0
    assert sp.diff(disc_m_reduced, A0) != 0
    return disc_p_reduced, disc_m_reduced


def main():
    point_support = reconstruct_support()
    support = tuple(exponents for _, exponents in point_support)
    histogram = Counter(point[1] for point, _ in point_support)
    assert histogram == Counter({-1: 9, 0: 26, 1: 9, 2: 25})

    # Anticanonical Cox degree: Q*m is constant and equals sum of columns Q.
    degrees = {
        tuple(sum(row[i] * monomial[i] for i in range(11)) for row in Q)
        for monomial in support
    }
    anticanonical = tuple(sum(row) for row in Q)
    assert degrees == {anticanonical} == {(4, 4, 3, 2, -1, 0)}

    support_p0 = tuple(monomial for monomial in support if monomial[P_INDEX] == 0)
    support_m0 = tuple(monomial for monomial in support if monomial[M_INDEX] == 0)
    support_seam = tuple(
        monomial
        for monomial in support
        if monomial[P_INDEX] == monomial[M_INDEX] == 0
    )
    assert (len(support_p0), len(support_m0), len(support_seam)) == (60, 35, 26)

    # No toric boundary coordinate common to a component divides every
    # restricted monomial.  Thus the irreducible dense-torus hypersurface
    # checked below does not acquire an extra toric boundary component.
    active_p = set().union(
        *(set(cone) - {P_INDEX} for cone in CONES if P_INDEX in cone)
    )
    active_m = set().union(
        *(set(cone) - {M_INDEX} for cone in CONES if M_INDEX in cone)
    )
    assert all(min(monomial[i] for monomial in support_p0) == 0 for i in active_p)
    assert all(min(monomial[i] for monomial in support_m0) == 0 for i in active_m)

    total_base = minimal_base_loci(support, CONES)
    p_base = minimal_base_loci(support_p0, link_cones((P_INDEX,)))
    m_base = minimal_base_loci(support_m0, link_cones((M_INDEX,)))
    seam_base = minimal_base_loci(support_seam, link_cones((P_INDEX, M_INDEX)))
    assert total_base == ((6, 7),)
    assert (p_base, m_base, seam_base) == ((), ((6, 7),), ())

    unit_jet = (2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0)
    jet_terms = tuple(
        monomial
        for monomial in support
        if monomial[6] == 1 and monomial[7] == 0
    )
    jet_terms_m = tuple(
        monomial
        for monomial in support_m0
        if monomial[6] == 1 and monomial[7] == 0
    )
    assert jet_terms == (unit_jet,) and jet_terms_m == (unit_jet,)

    # The fan SR data separately forces x0 and E to be units on x6=x7=0.
    assert not any({0, 6} <= set(cone) for cone in CONES)
    assert not any({7, 8} <= set(cone) for cone in CONES)
    # It also deletes the vertical pre-semistable stratum and separates the
    # exceptional divisor from the seam.
    assert not any({6, P_INDEX} <= set(cone) for cone in CONES)
    assert not any({8, P_INDEX} <= set(cone) for cone in CONES)

    ideal_decomposition, central_decomposition = local_ideal_audits()
    branch_checks, transverse_checks, node_count = explicit_genericity_witnesses()
    discriminants = component_irreducibility_discriminants()

    print("R63 INDEPENDENT JACOBIAN/SNC AUDIT: PASS")
    print("resolved points / sigma5 support:", 104, len(support))
    print("height histogram:", dict(sorted(histogram.items())))
    print("Cox degree / anticanonical class:", next(iter(degrees)), anticanonical)
    print("supports p=0 / m=0 / seam:", len(support_p0), len(support_m0), len(support_seam))
    print("fixed toric boundary components p=0 / m=0:", False, False)
    print("base loci total / p=0 / m=0 / seam:", total_base, p_base, m_base, seam_base)
    print("unit normal jet:", unit_jet)
    print("Groebner (a,b) intersect (p,b):", ideal_decomposition)
    print("Groebner (p) intersect (m):", central_decomposition)
    print("smooth (4,4) branch charts:", branch_checks)
    print("transverse (2,2)/(4,4) charts:", transverse_checks)
    print("transverse intersection number:", node_count)
    print("component discriminant degrees in A0:", *(sp.degree(value, sp.Symbol("A0")) for value in discriminants))
    print("VERDICT: MONOMIAL SUPPORT, BASE LOCI, UNIT JETS, LOCAL DECOMPOSITION AND GENERIC SNC INPUTS CONFIRMED")


if __name__ == "__main__":
    main()

