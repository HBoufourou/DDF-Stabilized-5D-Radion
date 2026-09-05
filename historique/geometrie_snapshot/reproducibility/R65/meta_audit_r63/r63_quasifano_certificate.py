#!/usr/bin/env python3
"""R63 exact combinatorial certificate for the two R62 central components.

The script verifies the toric inputs used in the cohomological argument:

* the stars of p, m and <p,m> are smooth complete fans;
* the common toric threefold T is a P1-bundle over P1 x P1;
* T is a toric fibre in each fourfold component;
* its two normal line bundles, and hence the two normals of the K3 seam,
  are individually trivial.

The final H^i(O) conclusions use standard toric vanishing, Serre duality and
the two displayed Cartier-divisor exact sequences; those theorems are stated
explicitly in the companion report and are not being replaced by a numerical
calculation here.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from sympy import Matrix


# Coordinates are (a,q,c,d,s).  Indices 0,...,8,p=9,m=10.
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
    (0, -1, 0, 0, 1),  # p
    (0, 0, 0, 0, 1),   # m
)

P, M = 9, 10

MAXIMAL_CONES = (
    # lower top with p
    (0, 1, 2, 5, P), (0, 1, 3, 5, P),
    (0, 2, 4, 5, P), (0, 3, 4, 5, P),
    (1, 2, 5, 7, P), (1, 3, 5, 7, P),
    (2, 4, 5, 7, P), (3, 4, 5, 7, P),
    # upper top with m
    (0, 1, 2, 8, M), (0, 1, 3, 8, M),
    (0, 2, 4, 8, M), (0, 3, 4, 8, M),
    (1, 2, 6, 7, M), (1, 2, 6, 8, M),
    (1, 3, 6, 7, M), (1, 3, 6, 8, M),
    (2, 4, 6, 7, M), (2, 4, 6, 8, M),
    (3, 4, 6, 7, M), (3, 4, 6, 8, M),
    # seam cones
    (0, 1, 2, P, M), (0, 1, 3, P, M),
    (0, 2, 4, P, M), (0, 3, 4, P, M),
    (1, 2, 7, P, M), (1, 3, 7, P, M),
    (2, 4, 7, P, M), (3, 4, 7, P, M),
)

EXPECTED_SR_PAIRS = {
    (0, 6), (0, 7), (1, 4), (2, 3), (5, 6),
    (5, 8), (5, M), (6, P), (7, 8), (8, P),
}


def star(ray_indices: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    wanted = set(ray_indices)
    return tuple(
        tuple(sorted(set(cone) - wanted))
        for cone in MAXIMAL_CONES
        if wanted <= set(cone)
    )


def all_codimension_one_faces(cones):
    counts = Counter()
    for cone in cones:
        for face in combinations(cone, len(cone) - 1):
            counts[tuple(sorted(face))] += 1
    return counts


def all_faces(cones):
    faces = {()}
    for cone in cones:
        for size in range(1, len(cone) + 1):
            faces.update(combinations(cone, size))
    return faces


def minimal_nonfaces(number_of_rays, cones):
    """Recompute every minimal non-face instead of trusting a stored SR list."""
    faces = all_faces(cones)
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
    return set(result)


def main() -> None:
    sr_pairs = minimal_nonfaces(len(RAYS), MAXIMAL_CONES)
    assert sr_pairs == EXPECTED_SR_PAIRS
    star_p = star((P,))
    star_m = star((M,))
    star_pm = star((P, M))
    assert (len(star_p), len(star_m), len(star_pm)) == (16, 20, 8)
    assert set(all_codimension_one_faces(star_p).values()) == {2}
    assert set(all_codimension_one_faces(star_m).values()) == {2}

    quotient_p = lambda ray: (ray[0], ray[2], ray[3], ray[1] + ray[4])
    quotient_m = lambda ray: (ray[0], ray[1], ray[2], ray[3])
    assert all(
        abs(int(Matrix([quotient_p(RAYS[i]) for i in cone]).det())) == 1
        for cone in star_p
    )
    assert all(
        abs(int(Matrix([quotient_m(RAYS[i]) for i in cone]).det())) == 1
        for cone in star_m
    )

    # The seam quotient N'/(p,m) keeps coordinates (a,c,d).
    seam_indices = (0, 1, 2, 3, 4, 7)
    seam_rays = {
        i: (RAYS[i][0], RAYS[i][2], RAYS[i][3])
        for i in seam_indices
    }
    assert all(
        abs(int(Matrix([seam_rays[i] for i in cone]).det())) == 1
        for cone in star_pm
    )
    seam_walls = all_codimension_one_faces(star_pm)
    assert len(seam_walls) == 12 and set(seam_walls.values()) == {2}

    # Cube combinatorics: choose one ray from each primitive non-face pair.
    expected_seam_cones = {
        tuple(sorted(choice))
        for choice in (
            (a, b, c)
            for a in (0, 7)
            for b in (1, 4)
            for c in (2, 3)
        )
    }
    assert set(star_pm) == expected_seam_cones

    # Divisor relations on T.  With H1=D1=D4, H2=D2=D3:
    # D0-D7=2H1+2H2, and -K_T=2D0=2D7+4H1+4H2.
    # These are the relations obtained from the quotient ray matrix.
    relation_matrix = Matrix(
        [
            [1, -2, -2, 0, 0, -1],  # D0-2D1-2D2-D7
            [0, -1, 0, 0, 1, 0],    # -D1+D4
            [0, 0, -1, 1, 0, 0],    # -D2+D3
        ]
    )
    seam_ray_matrix = Matrix([seam_rays[i] for i in seam_indices]).T
    assert relation_matrix == seam_ray_matrix
    # Class basis (H1,H2,F=D7), columns ordered 0,1,2,3,4,7.
    classes = Matrix(
        [
            [2, 1, 0, 0, 1, 0],
            [2, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
    )
    assert classes * relation_matrix.T == Matrix.zeros(3, 3)
    minus_k_t = tuple(int(x) for x in classes * Matrix.ones(6, 1))
    assert minus_k_t == (4, 4, 2)
    assert tuple(int(x) for x in 2 * classes[:, 0]) == minus_k_t

    # Toric morphisms of the two fourfold components to P1.
    # On V_p use ell_p=q+s: only x5=-1 and m=+1 occur off zero.
    # On V_m use ell_m=q: p=-1 and x6,E=+1 occur off zero.
    ell_p = tuple(ray[1] + ray[4] for ray in RAYS)
    ell_m = tuple(ray[1] for ray in RAYS)
    rays_in_star_p = set().union(*map(set, star_p))
    rays_in_star_m = set().union(*map(set, star_m))
    assert {i: ell_p[i] for i in rays_in_star_p if ell_p[i]} == {5: -1, M: 1}
    assert {i: ell_m[i] for i in rays_in_star_m if ell_m[i]} == {P: -1, 6: 1, 8: 1}
    # The appearance of coefficients +/-1 makes both quotient characters
    # primitive; their toric fibres have multiplicity one.
    assert {-1, 1} <= set(ell_p)
    assert {-1, 1} <= set(ell_m)
    assert all(
        len({(ell_p[i] > 0) - (ell_p[i] < 0) for i in cone if ell_p[i]}) <= 1
        for cone in star_p
    )
    assert all(
        len({(ell_m[i] > 0) - (ell_m[i] < 0) for i in cone if ell_m[i]}) <= 1
        for cone in star_m
    )

    # Opposite toric fibres are disjoint by the SR pairs.  Therefore the
    # fibre T has trivial normal in each V_j.
    assert (5, M) in sr_pairs
    assert (6, P) in sr_pairs and (8, P) in sr_pairs
    normal_t_in_vp = "O_T  (D_m ~ D_5, and D_m cap D_5 = empty)"
    normal_t_in_vm = "O_T  (D_p ~ D_6+D_E, disjoint fibres)"

    print("R63 TORIC QUASI-FANO CERTIFICATE")
    print("star maximal cones V_p / V_m / T:", len(star_p), len(star_m), len(star_pm))
    print("T smooth complete fan: 8 unimodular cones, 12 paired walls")
    print("T divisor-class basis (H1,H2,F); -K_T:", minus_k_t)
    print("relative minimal SR generators:", tuple(sorted(sr_pairs)))
    print("seam class:", "2D0 = (4,4,2) = -K_T")
    print("V_p -> P1 nonzero ray heights:", {5: -1, M: 1})
    print("V_m -> P1 nonzero ray heights:", {P: -1, 6: 1, 8: 1})
    print("N_{T/V_p}:", normal_t_in_vp)
    print("N_{T/V_m}:", normal_t_in_vm)
    print("N_{S/Y_p}=O_S and N_{S/Y_m}=O_S")
    print("d-semistability product: O_S")
    print("REPORT CONSEQUENCES (toric vanishing + Serre + divisor sequences):")
    print("h^i(O_Yp)=h^i(O_Ym)=(1,0,0,0)")
    print("h^i(O_S)=(1,0,1), K_S=O_S, hence S is K3")
    print("Tyurin/DHT quasi-Fano: YES; weak-Fano (big -K): NO")


if __name__ == "__main__":
    main()

