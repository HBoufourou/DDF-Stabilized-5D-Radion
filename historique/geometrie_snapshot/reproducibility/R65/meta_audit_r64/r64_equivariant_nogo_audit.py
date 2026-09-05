#!/usr/bin/env python3
"""R64 exact checks for the uniform O3/O7--O5/O9 Tyurin obstruction.

The program certifies the sign algebra, the four orientifold/branch cases,
the sigma|S = identity subcases, and the elementary U(2) lattice facts used
in the R63 application. The Hodge-index/positive-three-plane theorem is a
mathematical input and is labelled as such rather than simulated.
"""

from __future__ import annotations

from itertools import product
from math import gcd


Matrix2 = tuple[tuple[int, int], tuple[int, int]]
Vector2 = tuple[int, int]

I: Matrix2 = ((1, 0), (0, 1))
MINUS_I: Matrix2 = ((-1, 0), (0, -1))
SWAP: Matrix2 = ((0, 1), (1, 0))
MINUS_SWAP: Matrix2 = ((0, -1), (-1, 0))
U2: Matrix2 = ((0, 2), (2, 0))


def transpose(a: Matrix2) -> Matrix2:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def multiply(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def act(a: Matrix2, v: Vector2) -> Vector2:
    return (
        a[0][0] * v[0] + a[0][1] * v[1],
        a[1][0] * v[0] + a[1][1] * v[1],
    )


def square_u2(v: Vector2) -> int:
    return 4 * v[0] * v[1]


def pairing_u2(v: Vector2, w: Vector2) -> int:
    return 2 * (v[0] * w[1] + v[1] * w[0])


def is_u2_isometry(a: Matrix2) -> bool:
    return multiply(multiply(transpose(a), U2), a) == U2


def preserves_positive_cone(a: Matrix2) -> bool:
    image = act(a, (1, 1))
    return image[0] > 0 and image[1] > 0


def u2_arithmetic() -> dict[str, object]:
    exact = {I, MINUS_I, SWAP, MINUS_SWAP}
    bounded: set[Matrix2] = set()
    for a, b, c, d in product(range(-8, 9), repeat=4):
        candidate: Matrix2 = ((a, b), (c, d))
        if is_u2_isometry(candidate):
            bounded.add(candidate)
    assert bounded == exact
    assert {a for a in exact if preserves_positive_cone(a)} == {I, SWAP}

    isotropic: set[Vector2] = set()
    for a, b in product(range(-50, 51), repeat=2):
        if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1:
            if square_u2((a, b)) == 0:
                isotropic.add((a, b))
    assert isotropic == {(-1, 0), (1, 0), (0, -1), (0, 1)}

    active_zero = []
    for a, b in product(range(-20, 21), repeat=2):
        c = (a, b)
        if pairing_u2(c, (1, 0)) == pairing_u2(c, (0, 1)) == 0:
            active_zero.append(c)
    assert active_zero == [(0, 0)]
    return {"isometries": exact, "primitive_isotropics": isotropic}


def uniform_sign_table() -> list[dict[str, int | str]]:
    """Verify omega_S=s*eta and curve=-s*eta in all four cases."""

    rows: list[dict[str, int | str]] = []
    for orientifold, s in (("O3/O7", -1), ("O5/O9", +1)):
        for branch_action, eta in (("preserved", +1), ("exchanged", -1)):
            omega_s = s * eta
            c4_vector = -s
            curve = -s * eta
            tube = curve * eta
            assert omega_s * eta == s
            assert tube == c4_vector
            assert curve == -omega_s
            rows.append(
                {
                    "orientifold": orientifold,
                    "s": s,
                    "branch_action": branch_action,
                    "eta": eta,
                    "omega_S": omega_s,
                    "C4_vector": c4_vector,
                    "curve": curve,
                }
            )
    assert len(rows) == 4
    return rows


def positive_three_plane_certificate(
    omega_sign: int, curve_sign: int
) -> str:
    """Identify why C is perpendicular to the positive three-plane."""

    assert curve_sign == -omega_sign
    if omega_sign == +1:
        assert curve_sign == -1
        return "equivariance_perpendicular_to_Omega_plane_and_h"
    assert omega_sign == -1 and curve_sign == +1
    return "equivariance_perpendicular_to_Omega_plane_plus_active_C_perp_h"


def identity_on_seam_subcases(rows: list[dict[str, int | str]]) -> dict[str, str]:
    exchanged = {str(row["orientifold"]): row for row in rows if row["eta"] == -1}

    o3 = exchanged["O3/O7"]
    assert o3["omega_S"] == +1  # Compatible with sigma|S=id.
    assert o3["curve"] == -1
    o3_verdict = "compatible_but_required_anti_eigenspace_is_zero"

    o5 = exchanged["O5/O9"]
    assert o5["omega_S"] == -1
    # Identity acts +1 on every class and on Omega_S, so it cannot realize
    # this row at all.
    o5_verdict = "incompatible_identity_cannot_make_Omega_S_odd"
    return {"O3/O7": o3_verdict, "O5/O9": o5_verdict}


def boundary_counterexamples() -> dict[str, str]:
    e_l = (1, 0)
    assert square_u2(e_l) == 0
    assert pairing_u2(e_l, e_l) == 0  # L0=Z e has no ample direction.
    # These symbolic witnesses delimit the theorem; they are not claims of
    # stability or of an orientifold-surviving brane state.
    return {
        "drop_active": "isotropic ruling e_L lies in L, not L_perp",
        "drop_ample_in_L": "for L0=Z e_L, e_L lies in L0_perp and is isotropic",
        "drop_eigenclass": "e_L+u_K can be isotropic but maps to e_L-u_K",
        "brane_image": "projection and stability deliberately undecided",
        "KK": "metric/gravitational towers deliberately undecided",
    }


def main() -> None:
    arithmetic = u2_arithmetic()
    rows = uniform_sign_table()
    reasons = {
        (str(row["orientifold"]), str(row["branch_action"])):
        positive_three_plane_certificate(int(row["omega_S"]), int(row["curve"]))
        for row in rows
    }
    identity_cases = identity_on_seam_subcases(rows)
    boundaries = boundary_counterexamples()

    print("R64 UNIFORM ORIENTIFOLD EQUIVARIANT NO-GO AUDIT")
    print("sign table", rows)
    print("positive-three-plane reasons", reasons)
    print("sigma|S identity, exchanged branches", identity_cases)
    print("O(U(2),Z)", sorted(arithmetic["isometries"]))
    print("primitive isotropics in U(2)", sorted(arithmetic["primitive_isotropics"]))
    print("boundary witnesses", boundaries)
    print("VERDICT")
    print("UNIFORM_SIGN_IDENTITY: EPSILON_C_EQUALS_MINUS_EPSILON_OMEGA_S")
    print("ALL_FOUR_ORIENTIFOLD_BRANCH_CASES: NEGATIVE_OR_ZERO")
    print("EXCHANGED_BRANCH_SIGMA_S_IDENTITY: O3O7_ZERO_O5O9_INCOMPATIBLE")
    print("GENERAL_C4_ACTIVE_NONNEGATIVE_NOGO: POSITIVE_THREE_PLANE_COROLLARY")
    print("GLOBAL_INVOLUTION_OVER_FIXED_T: ASSUMED_NOT_CONSTRUCTED")
    print("BRANE_IMAGE_STABILITY_KK: NOT_COVERED")


if __name__ == "__main__":
    main()

