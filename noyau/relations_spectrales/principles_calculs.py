"""Bounded, standard-library checks of radius-free DDF consistency relations.

No spectrum is refitted or recalculated here. Input eigenvalues/couplings are the
archived, independently verified affine-brane results. The analytic relation is
newly assembled from their weak-backreaction limit; it is not valid unchanged
for nonzero quadratic brane curvature. Run from any directory.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math


def coefficient_D(x):
    t = math.tanh(x / 2)
    return (1 + t * t + 2 * t / x) / (4 * x * t)


def read_cases(path, default_x=None):
    rows = json.loads(path.read_text(encoding="utf-8-sig"))
    for row in rows:
        x = row.get("x", default_x)
        scalars, tensors = row["scalar_modes"], row["tensor_modes"]
        if len(scalars) < 3 or not tensors:
            continue
        mr, ms1, ms2 = [m["mL"] for m in scalars[:3]]
        mt = tensors[0]["mL"]
        alpha = scalars[0].get("alpha", scalars[0].get(
            "alpha_scalar_conditional_archive_norm"))
        eps = row["epsilon"]
        x_observed = math.pi * ms1 / mt
        lhs = 3 * alpha - 1
        rhs = math.pi ** 2 * coefficient_D(x_observed) * (mr / mt) ** 2
        closure = (ms2 ** 2 - ms1 ** 2) / mt ** 2 - 1
        yield {
            "source": path.name, "x_actual": x, "epsilon": eps,
            "tolerance": row.get("tolerance"),
            "x_inferred_at_leading_order": x_observed,
            "radion_over_tensor_mass": mr / mt,
            "first_stabilizer_over_tensor_mass": ms1 / mt,
            "three_alpha_minus_one": lhs,
            "observable_relation_rhs": rhs,
            "relation_residual": lhs - rhs,
            "residual_over_epsilon_four": (lhs - rhs) / eps ** 4,
            "relative_residual_to_coupling_shift": (lhs - rhs) / lhs,
            "spectral_closure_residual": closure,
            "closure_over_epsilon_squared": closure / eps ** 2,
        }


def main():
    parser = argparse.ArgumentParser()
    default_data=Path(__file__).resolve().parent/"input_data"
    parser.add_argument("--data", type=Path, default=default_data)
    parser.add_argument("--output", type=Path,
        default=Path(__file__).with_name("principles_calculs.json"))
    args = parser.parse_args()
    files = [(args.data / "spectre_5d.json", 2.0),
             (args.data / "extension_x.json", None)]
    cases = [case for path, x in files for case in read_cases(path, x)]
    cases.sort(key=lambda r: (r["x_actual"], r["epsilon"],
                              r["tolerance"] or 0))
    sensitivity = [{
        "x": x,
        "z_q_over_sqrt_2Lambda5": math.cosh(x / 2),
        "d_log_L_d_log_z": 2 / (x * math.tanh(x / 2)),
        "d_log_L_d_log_mu_at_fixed_z": -1.0,
    } for x in [0.1, 0.5, 1, 2, 3, 6, 10]]
    # Arbitrary demonstration point, not a calibration or DDF prediction.
    # Dimensionless equations fix x, epsilon, I/L and Lambda5*L^2/B.
    B0, L0, mu0, q0, Lambda0 = 7.0, 2.0, 1.0, 0.4, 0.2
    I_over_L = 1.03
    scaling = []
    for s in [0.1, 1, 10]:
        B, L, mu = B0 / s, L0 * s, mu0 / s
        q, lam = q0 / s ** 1.5, Lambda0 / s ** 3
        scaling.append({"scale_s": s, "L": L, "B_M5_cubed": B,
            "mu": mu, "q": q, "Lambda5": lam,
            "MPlanck_squared": B * L * I_over_L,
            "x": mu * L,
            "epsilon": q * L / math.sqrt(12 * B),
            "Lambda5_L_squared_over_B": lam * L ** 2 / B})
    for name in ["MPlanck_squared", "x", "epsilon", "Lambda5_L_squared_over_B"]:
        assert all(math.isclose(p[name], scaling[1][name], rel_tol=1e-14)
                   for p in scaling)
    result = {
        "scope": "Affine branes, fixed x>0, weak backreaction; same-brane minimal matter.",
        "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p, _ in files},
        "formula": "3 alpha_r - 1 = pi^2 D(pi*m_s1/m_T1)*(m_r/m_T1)^2 + O(epsilon^4)",
        "cases": cases, "radius_sensitivity": sensitivity,
        "exact_scale_degeneracy_algebra_check": scaling,
        "scale_demo_note": "Arbitrary algebraic point, not a solved background; the scale symmetry is proved in the accompanying note.",
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
