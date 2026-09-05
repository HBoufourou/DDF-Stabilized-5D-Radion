"""Independent analytic and quadrature check; Python standard library only.

Units L=M5^3=1, x=mu*L>0, epsilon=q/sqrt(12).
These coefficients are derived, not fitted to numerical spectral data.
Run: python weak_backreaction_general.py
"""
import argparse
import json
import math
from pathlib import Path


def simpson(fun, n=20000):
    """Integrate over the full interval using even symmetry."""
    h = 0.5 / n
    return 2 * h / 3 * (
        fun(0) + fun(0.5)
        + 4 * math.fsum(fun(i * h) for i in range(1, n, 2))
        + 2 * math.fsum(fun(i * h) for i in range(2, n, 2))
    )


def coefficients(x, n=20000):
    if x <= 0:
        raise ValueError('The regular expansion is stated for x>0.')
    C = math.cosh(x / 2) ** 2
    T = math.tanh(x / 2)
    kappa = 4 * x * T / C
    c_alpha = (1 + T*T + 2*T/x) / C

    def v1(t):
        return math.sqrt(12) * math.cosh(x*t) / math.sqrt(C)

    def b(t):
        return 8*t*math.cosh(x*t)**2/C - kappa*math.sinh(2*x*t)/(2*x)

    def f2(t):
        return (4*t*t + 2*t*math.sinh(2*x*t)/x)/C - kappa*(math.cosh(2*x*t)-1)/(4*x*x)

    avg_f2 = simpson(f2, n)
    avg_s1sq = simpson(lambda t: (3*b(t)/v1(t))**2, n)
    quadrature_c = 2 * (f2(0.5) - avg_f2) - avg_s1sq/6
    analytic_avg_f2 = (1/3 + 1/x**2 - math.sinh(x)/x**3 + T/x)/C
    analytic_avg_s1sq = 12/C * (1/6 - T*T/2 - 1/x**2 + math.sinh(x)/x**3)
    errors = {
        'coefficient_quadrature_vs_closed': abs(quadrature_c-c_alpha),
        'f2_mean_quadrature_vs_closed': abs(avg_f2-analytic_avg_f2),
        's1sq_mean_quadrature_vs_closed': abs(avg_s1sq-analytic_avg_s1sq),
        'boundary_condition_coefficient': abs(x*T*b(0.5)-kappa),
    }
    if max(errors.values()) > 2e-10:
        raise ArithmeticError(errors)
    return {
        'x': x, 'kappa': kappa, 'c_alpha': c_alpha,
        'c_alpha_over_kappa': c_alpha/kappa,
        'f2_boundary': f2(0.5), 'mean_f2': avg_f2,
        'mean_s1_squared': avg_s1sq, 'quadrature_c_alpha': quadrature_c,
        'checks_absolute_errors': errors,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    values = [coefficients(x) for x in (0.5, 1.0, 2.0, 3.0, 4.0)]
    encoded = json.dumps(values, indent=2)
    if args.output:
        args.output.write_text(encoded + '\n', encoding='utf-8')
    print(encoded)
