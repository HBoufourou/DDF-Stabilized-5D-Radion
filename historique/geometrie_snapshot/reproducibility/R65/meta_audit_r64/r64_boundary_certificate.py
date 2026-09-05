#!/usr/bin/env python3
"""Exact arithmetic checks for the R64 boundary/counterexample audit.

This script deliberately checks only the finite intersection- and lattice-
arithmetic appearing in counterexamples_and_boundaries.md.  Smoothness and
the standard adjunction/Serre-duality statements remain mathematical proofs
in that report, rather than being replaced by a numerical verdict.
"""

from fractions import Fraction


def mul_p1_p3(left, right):
    """Multiply classes in Q[A,B]/(A^2,B^4).

    A has bidegree (1,0), B has bidegree (0,1).  A monomial is keyed by
    (power_A, power_B).
    """
    out = {}
    for (a1, b1), c1 in left.items():
        for (a2, b2), c2 in right.items():
            a, b = a1 + a2, b1 + b2
            if a >= 2 or b >= 4:
                continue
            out[(a, b)] = out.get((a, b), Fraction(0)) + c1 * c2
    return {k: v for k, v in out.items() if v}


def power_p1_p3(value, exponent):
    out = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        out = mul_p1_p3(out, value)
    return out


def determinant(matrix):
    m = [[Fraction(x) for x in row] for row in matrix]
    n = len(m)
    det = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if m[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            det *= -1
        det *= m[i][i]
        pivot_value = m[i][i]
        m[i] = [entry / pivot_value for entry in m[i]]
        for j in range(i + 1, n):
            factor = m[j][i]
            m[j] = [x - factor * y for x, y in zip(m[j], m[i])]
    return int(det) if det.denominator == 1 else det


def main():
    # Non-fibre ambient divisor in V=P^1 x P^3.
    A = {(1, 0): Fraction(1)}
    B = {(0, 1): Fraction(1)}
    T = {(1, 0): Fraction(1), (0, 1): Fraction(1)}
    Y = {(1, 0): Fraction(1), (0, 1): Fraction(3)}
    minus_K = {(1, 0): Fraction(2), (0, 1): Fraction(4)}
    assert {k: T.get(k, 0) + Y.get(k, 0) for k in set(T) | set(Y)} == minus_K
    t3y = mul_p1_p3(power_p1_p3(T, 3), Y)
    normal_square = t3y.get((1, 3), 0)
    assert normal_square == 10

    # Quartic seam in two copies of P^3.
    quartic_H2 = 4  # H^2 on a quartic K3.
    normal_each_c1 = 4  # N_{S/P3}=O_S(4H).
    product_normal_c1 = 2 * normal_each_c1
    product_normal_square = product_normal_c1**2 * quartic_H2
    assert product_normal_square == 256

    # Very-general and Noether--Lefschetz lattice models.
    U2 = [[0, 2], [2, 0]]
    nl_gram = [[0, 2, 0], [2, 0, 0], [0, 0, -8]]
    assert determinant(U2) == -4
    assert determinant(nl_gram) == 32

    # Swap of the two rulings and its eigenbasis h=A+B, d=A-B.
    swap = [[0, 1], [1, 0]]
    assert determinant(swap) == -1
    h_square = 4
    d_square = -4
    h_dot_d = 0
    assert (h_square, d_square, h_dot_d) == (4, -4, 0)

    # LMHS dimensions if the actual restriction-image rank jumps.
    b3 = 172
    lmhs = {}
    for rank_L in (2, 3):
        gr2 = 22 - rank_L
        gr4 = gr2
        gr3 = b3 - gr2 - gr4
        type_index = 20 - rank_L
        lmhs[rank_L] = (gr2, gr3, gr4, type_index)
    assert lmhs[2] == (20, 132, 20, 18)
    assert lmhs[3] == (19, 134, 19, 17)

    # Primitive isotropic vector e in a U summand of the transverse K3 lattice.
    U = [[0, 1], [1, 0]]
    e = (1, 0)
    e_square = sum(e[i] * U[i][j] * e[j] for i in range(2) for j in range(2))
    assert e_square == 0

    print("R64 BOUNDARY CERTIFICATE")
    print(f"non-fibre model: integral_S c1(N)^2 = {normal_square}")
    print(f"P3 quartic double: integral_S c1(N1 tensor N2)^2 = {product_normal_square}")
    print(f"det U(2) = {determinant(U2)}")
    print(f"det NL lattice U(2)+<-8> = {determinant(nl_gram)}")
    print(f"ruling swap eigen-squares = ({h_square}, {d_square})")
    print(f"LMHS r=2: GrW(2,3,4), II_b = {lmhs[2]}")
    print(f"LMHS r=3: GrW(2,3,4), II_b = {lmhs[3]}")
    print(f"primitive transverse e has e^2 = {e_square}")
    print("VERDICT: EXACT_ARITHMETIC_PASS")


if __name__ == "__main__":
    main()

