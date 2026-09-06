"""Finite-chi interior halos with an imposed Dirichlet value at the fluid edge.

This is not a derived matching to a normal phase. The edge is the first rho=0;
chi(edge)=0 is an additional imposed condition. No dynamical stability or
fixed-charge energy selection is inferred from a nodeless shooting solution.
"""
import argparse
import json
from pathlib import Path
from halo_hydrostatic import solve, summary, make_profiles


def negative_inside(sol):
    return any(row[3] < 0 for row in sol['rows'][1:])


def shoot(ell, lo, hi, tol):
    def calc(ch):
        result = solve(1., 1., 1., 'gradient', tol=tol, ell=ell, chi0=ch, smax=20.)
        if not result['success']:
            raise RuntimeError((ell, ch, result.get('reason')))
        return result
    low, high = calc(lo), calc(hi)
    assert negative_inside(low) and not negative_inside(high)
    best = min([low, high], key=lambda sol: abs(sol['chi_surface']))
    for _ in range(52):
        mid = (lo+hi)/2
        trial = calc(mid)
        if abs(trial['chi_surface']) < abs(best['chi_surface']):
            best = trial
        if negative_inside(trial):
            lo, low = mid, trial
        else:
            hi, high = mid, trial
        if hi-lo < 2e-13*max(1., abs(mid)):
            break
    result = summary(best)
    result.update({'chi0_bracket': [lo, hi], 'chi_surface': best['chi_surface'],
                   'chi_prime_surface': best['rows'][-1][4],
                   'minimum_chi_before_last_row': min(row[3] for row in best['rows'][:-1]),
                   'relative_shooting_residual': abs(best['chi_surface'])/best['chi0'],
                   'profile': make_profiles(best), 'rtol': tol})
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = ap.parse_args()
    cases = []
    for ell, lo, hi in [(.3, .6, 1.), (.1, 1.5, 2.), (.03, 1.5, 2.)]:
        coarse = shoot(ell, lo, hi, 2e-8)
        tight = shoot(ell, lo, hi, 2e-11)
        tight['convergence'] = {
            'relative_chi0_change': tight['chi0']/coarse['chi0']-1,
            'relative_surface_change': tight['surface_over_rK']/coarse['surface_over_rK']-1,
            'relative_mass_change': tight['total_dark_mass_over_total_baryon_mass']/coarse['total_dark_mass_over_total_baryon_mass']-1}
        tight['boundary_numerically_resolved'] = tight['relative_shooting_residual'] < 1e-5
        cases.append(tight)
        print(json.dumps({k: v for k, v in tight.items() if k not in ['profile', 'points']}), flush=True)
    result = {'scope': __doc__.strip(), 'same_inputs_for_all': {'A': 1., 'B': 1., 'uc': 1.},
              'ell_is_a_common_theory_scenario_not_a_galaxy_fit': True,
              'free_density_boundary': 'First u=0, not a derived finite-temperature phase boundary.',
              'outer_chi_boundary': 'Imposed chi(S)=0. Nonzero chi_prime(S) requires exterior or surface matching.',
              'branch_selection': 'Boundary of the positive interior shooting set inside the stated chi0 bracket; uniqueness unproved.',
              'fixed_charge_caveat': 'Different solutions have different total dark mass; no energy comparison at fixed mass has been done.',
              'cases': cases}
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
