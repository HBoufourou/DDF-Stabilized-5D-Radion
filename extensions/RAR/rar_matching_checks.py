"""Algebra and parameter matching for the proposed 5D/Khoury extension.

Standard library only. This is not a 5D spectrum, halo solution, UV completion,
or cutoff calculation. All numerical examples use a declared FLAT interval.
The accompanying note gives the general warped overlap formulas.
"""
import argparse
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path


# Small exact polynomial ring Q[p,a,b]; used to check the profile-moment
# obstruction without a computer algebra dependency.
class Poly:
    def __init__(self, terms=None):
        self.terms = {k: F(v) for k, v in (terms or {}).items() if v}

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0, 0, 0): other})
        ans = dict(self.terms)
        for k, v in other.terms.items():
            ans[k] = ans.get(k, F(0)) + v
        return Poly(ans)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0, 0, 0): other})
        ans = {}
        for k, v in self.terms.items():
            for l, w in other.terms.items():
                key = tuple(x + y for x, y in zip(k, l))
                ans[key] = ans.get(key, F(0)) + v * w
        return Poly(ans)

    __rmul__ = __mul__

    def __pow__(self, power):
        result = Poly({(0, 0, 0): 1})
        for _ in range(power):
            result = result * self
        return result


def exact_checks():
    p = Poly({(1, 0, 0): 1})
    a = Poly({(0, 1, 0): 1})
    b = Poly({(0, 0, 1): 1})
    mean = p * a + (1 - p) * b
    variance = p * a**2 + (1 - p) * b**2 - mean**2
    factorized = p * (1 - p) * (a - b)**2
    assert not (variance - factorized).terms

    # Same ring, reinterpreted as (m, theta_dot, unused). These expansions
    # display the sign of the term linear in theta_dot before division by 2m.
    m, td = p, a
    plus = (m + td)**2 - m**2
    minus = (m - td)**2 - m**2
    assert plus.terms[(1, 1, 0)] == 2
    assert minus.terms[(1, 1, 0)] == -2
    assert not (plus - (2 * m * td + td**2)).terms
    assert not (minus - (-2 * m * td + td**2)).terms

    # Dimensionless curvature with a positive bare mass: d-u+u^2/9.
    # Its exact minimum is d-9/4 at u=9/2.
    u, d = p, a
    curvature = d - u + F(1, 9) * u**2
    completed_square = F(1, 9) * (u-F(9, 2))**2 + d-F(9, 4)
    assert not (curvature-completed_square).terms

    # At g/a0=1, chi^2=2, in units M4^2*a0^2:
    # V_chichi = 16/27; V_chig^2/V_gg = 16/135.
    schur = F(16, 27)-F(16, 135)
    assert schur == F(64, 135)
    assert schur / F(16, 27) == F(4, 5)

    # In the flat constant-profile mapping, eliminate Z^2=f5^2*L and
    # M4^2=M5^3*L. Rational substitution tests also check the L cancellation.
    volume_tests = []
    for L, M53, f52, mass, D5 in itertools.product(
            [F(1, 3), F(2), F(7)], [F(2), F(5)], [F(3), F(7)],
            [F(1, 2), F(2)], [F(2), F(11)]):
        a04 = M53 * L / (9 * D5 * mass**4 * f52 * L)
        a05 = M53 / (9 * D5 * mass**4 * f52)
        assert a04 == a05
        volume_tests.append(a04 == a05)

    dimensions = {
        "M5_cubed_R5": 3 + 2,
        "bulk_kinetic_H5": 2 * (F(3, 2) + 1),
        "xi5_H5_squared_Rslice": 0 + 3 + 2,
        "D5_H5_squared_Rslice_DY_squared": -6 + 3 + 2 + 6,
        "Z_squared": 3 - 1,
        "M4_squared": 3 - 1,
        "J_zeta_squared": 3 - 1,
        "a0_squared_matching": 2 - (-6 + 4 + 2),
        "density_mZ2chi2": 1 + 2,
        "g6_4D_phi6": -2 + 6,
    }
    for key in ["M5_cubed_R5", "bulk_kinetic_H5", "xi5_H5_squared_Rslice",
                "D5_H5_squared_Rslice_DY_squared"]:
        assert dimensions[key] == 5
    for key in ["Z_squared", "M4_squared", "J_zeta_squared", "a0_squared_matching"]:
        assert dimensions[key] == 2
    assert dimensions["density_mZ2chi2"] == 3
    assert dimensions["g6_4D_phi6"] == 4
    return {
        "profile_variance_polynomial_identity_zero": True,
        "identity": "p*a^2+(1-p)*b^2-[p*a+(1-p)*b]^2=p*(1-p)*(a-b)^2",
        "phase_leading_sign_for_exp[-i*(m*t+theta)]": 1,
        "phase_leading_sign_for_exp[-i*m*t+i*theta]": -1,
        "bare_mass_curvature_completed_square_identity_zero": True,
        "fixed_flux_to_fixed_g_curvature_ratio_at_g_a0": "4/5",
        "flat_volume_cancellation_rational_checks": len(volume_tests),
        "mass_dimensions": {k: str(v) for k, v in dimensions.items()},
    }


def numerical_examples():
    c = 299792458.0
    hbar_c_eV_m = 1.973269804593025e-7
    kpc_m = 3.0856775814913673e19
    M4 = 2.435e27
    R_m = 3e-6
    L = math.pi * R_m / hbar_c_eV_m
    M5 = (M4**2 / L)**(1 / 3)
    a0_si = 1.2e-10
    a0 = a0_si * hbar_c_eV_m / c**2
    r_m = 10 * kpc_m
    ar = a0_si * r_m / c**2
    mass = 0.1
    rows = []
    for Z in [1e3, 1e12, 1e15, 1e17, M4]:
        f52 = Z**2 / L
        xi5 = M4**2 / Z**2
        D5 = M4**2 / (9 * mass**4 * a0**2 * Z**2)
        recovered_a0 = math.sqrt(M5**3 / (9 * D5 * f52 * mass**4))
        mchi_r = 4 / (3 * math.sqrt(3)) * M4 / Z * ar
        assert abs(recovered_a0 / a0 - 1) < 2e-14
        rows.append({
            "Z_eV": Z, "f5_squared_eV3": f52, "xi5_required": xi5,
            "D5_required_eV_minus6": D5,
            "a0_recovered_eV": recovered_a0,
            "mchi_times_10kpc_at_g_equals_a0_fixed_g": mchi_r,
            "mchi_times_10kpc_at_g_equals_a0_fixed_flux": mchi_r*math.sqrt(4/5),
        })
    profile_example = {
        "scope": "Two-value profile illustration only, not a DDF eigenfunction",
        "probability_p": 0.5,
        "s_squared_values": [0.5, 1.5],
        "mean_s_squared": 1.0,
        "mean_s_fourth": 1.25,
        "quartic_excess": 0.25,
        "F4_at_chi_1": 0.5 / 1.5 + 0.5 / 2.5,
        "target_F_at_chi_1": 0.5,
    }
    return {
        "scope": "Flat constant-profile coefficient matching; all scales are inputs",
        "R_input_m": R_m, "L_input_eV_minus1": L,
        "M4_input_eV": M4, "M5_from_flat_planck_relation_eV": M5,
        "a0_input_m_s2": a0_si, "a0_input_eV": a0,
        "condensate_mass_input_eV": mass,
        "radius_for_adiabatic_diagnostic_m": r_m,
        "a0_r_over_c_squared": ar,
        "xi5_for_mchi_r_equal_1_at_g_a0": 27 / (16 * ar**2),
        "xi5_for_mchi_r_equal_1_at_g_a0_fixed_flux": (5/4)*27/(16*ar**2),
        "rows": rows,
        "profile_moment_example": profile_example,
        "brane_floor_examples": [{"gamma": g, "F4_chi_infinity": 1-g}
                                  for g in [0.1, 0.5, 0.9, 1.0]],
        "cautions": [
            "D5 is a Wilson coefficient; its inverse sixth root is not proven to be a physical cutoff.",
            "Adiabaticity is a local diagnostic, not a global halo solution or quantum consistency test.",
            "The nonlinear rational profile must be checked at finite chi, not only its quadratic Taylor coefficient.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = {"scope": __doc__.strip(), "algebra": exact_checks(),
              "matching_examples": numerical_examples(), "checks_passed": True}
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"saved": str(args.output), "checks_passed": True,
                      "xi5_for_mchi_r_1": result["matching_examples"]["xi5_for_mchi_r_equal_1_at_g_a0"]}))


if __name__ == "__main__":
    main()
