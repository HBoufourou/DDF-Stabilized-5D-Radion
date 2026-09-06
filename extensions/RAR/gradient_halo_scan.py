"""Exploratory shooting for a free fluid surface with imposed chi(surface)=0.

This boundary is a declared model problem, not a derived normal-phase matching.
Only a branch with no interior nodes in chi is retained when found.
"""
import argparse
import json
import math
from pathlib import Path
from halo_hydrostatic import solve, summary, make_profiles


def nodes(sol):
    values = [r[3] for r in sol['rows'][1:]]
    return sum(a*b < 0 for a, b in zip(values, values[1:]))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    ap.add_argument('--scan-only', action='store_true')
    args = ap.parse_args()
    scans = []
    for ell in [.3, .1, .03]:
        attempts = []
        for chi0 in [.001, .03, .1, .3, .6, 1., 1.5, 2., 3., 5., 8., 12., 20.]:
            sol = solve(1., 1., 1., 'gradient', tol=2e-8, ell=ell, chi0=chi0, smax=20)
            row = {'chi0': chi0, 'success': sol['success']}
            if sol['success']:
                row.update({'chi_surface': sol['chi_surface'], 'nodes': nodes(sol),
                            'surface': sol['surface'], 'mass': sol['dark_mass']})
            else:
                row['reason'] = sol['reason']
            attempts.append(row)
        print(json.dumps({'ell': ell, 'attempts': attempts}), flush=True)
        scans.append({'ell': ell, 'A': 1., 'B': 1., 'uc': 1., 'attempts': attempts})
    args.output.write_text(json.dumps({'scope': __doc__.strip(), 'scans': scans}, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
