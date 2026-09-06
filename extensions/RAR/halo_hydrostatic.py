"""Conditional self-consistent spherical halos, quartic EOS P=K*rho^2.

Standard library only. Baryons are Plummer; the dark density is obtained from
hydrostatic equilibrium and is included in the gravitational source. The first
zero of the dark density is a free Thomas-Fermi surface. No temperature,
formation history, exterior normal phase, 5D derivation, or dynamical stability
is inferred. A gradient-chi shooting option uses an explicitly imposed boundary.
"""
import argparse
import bisect
import json
import math
from pathlib import Path


def h_adiabatic(b):
    if b <= 0:
        return 0.0
    if b >= 3:
        return b
    if b < 1e-5:
        z = math.sqrt(b)
        return z + b/9 + 5*b*z/162 + 8*b*b/729
    return 1.5 + 3*math.cos((math.acos(max(-1., min(1., 1-2*b/3)))+4*math.pi)/3)


def h_chi(b, chi):
    if b <= 0:
        return 0.0
    c2 = chi*chi
    aa = 1/(1+c2)
    bb = 2*c2/9
    linear = b/aa
    if bb == 0 or bb*linear*linear/aa < 1e-12:
        return linear
    return 2*math.sqrt(aa/(3*bb))*math.sinh(math.asinh(3*b/(2*aa)*math.sqrt(3*bb/aa))/3)


def plummer(s, A, B):
    return A*s**3/(s*s+B*B)**1.5


def rhs(s, y, A, B, law, ell=None):
    u, mass = y[:2]
    b = (mass+plummer(s, A, B))/(s*s)
    if law == 'newton':
        h = b
    elif law == 'deep':
        h = math.sqrt(max(0., b))
    elif law == 'adiabatic':
        h = h_adiabatic(b)
    else:
        h = h_chi(b, y[2])
    ans = [-h, s*s*max(u, 0.)]
    if law == 'gradient':
        chi, z = y[2:]
        ans += [z, h*h*chi*(-1/(1+chi*chi)**2+h*h/9)/ell**2-2*z/s]
    return ans


# Dormand-Prince 5(4), with an independently checked exact Newtonian benchmark.
C = [0, 1/5, 3/10, 4/5, 8/9, 1, 1]
AA = [[], [1/5], [3/40, 9/40], [44/45, -56/15, 32/9],
      [19372/6561, -25360/2187, 64448/6561, -212/729],
      [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
      [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84]]
BB5 = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
BB4 = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]


def step(s, y, dt, fun):
    kk = []
    for j in range(7):
        state = [y[i]+dt*sum(AA[j][k]*kk[k][i] for k in range(j)) for i in range(len(y))]
        kk.append(fun(s+C[j]*dt, state))
    y5 = [y[i]+dt*sum(BB5[j]*kk[j][i] for j in range(7)) for i in range(len(y))]
    y4 = [y[i]+dt*sum(BB4[j]*kk[j][i] for j in range(7)) for i in range(len(y))]
    return y5, [a-b for a, b in zip(y5, y4)]


def solve(A, B, uc, law='adiabatic', tol=1e-8, ell=None, chi0=None, smax=100.):
    if uc <= 0 or B <= 0 or A < 0:
        raise ValueError('Positive central density and radius, nonnegative baryons required.')
    s = min(1e-7, B*1e-7)
    c = uc/3+A/B**3
    if law in ['adiabatic', 'deep']:
        u = uc-2*math.sqrt(c)*s**1.5/3
        v = uc*s**3/3-4*math.sqrt(c)*s**4.5/27
        if law == 'adiabatic':
            u -= c*s*s/18
            v -= c*s**5/90
        y = [u, v]
    else:
        ch = chi0 if law == 'gradient' else 0.
        slope = (1+ch*ch)*c
        y = [uc-slope*s*s/2, uc*s**3/3-slope*s**5/10]
        if law == 'gradient':
            if ell is None or ell <= 0:
                raise ValueError('Positive ell required.')
            y += [ch-c*c*ch*s**4/(20*ell*ell), -c*c*ch*s**3/(5*ell*ell)]
    fun = lambda t, z: rhs(t, z, A, B, law, ell)
    rows = [[0., uc, 0.]+([chi0, 0.] if law == 'gradient' else []), [s]+y]
    dt = 1e-4
    accepted = rejected = 0
    while s < smax and accepted < 150000:
        dt = min(dt, .025*max(B, .2), smax-s)
        yn, err = step(s, y, dt, fun)
        if any(not math.isfinite(t) or abs(t)>1e12 for t in yn):
            return {'success': False, 'reason': 'nonfinite_or_large_state', 'rows': rows}
        scale = max(abs(e)/(tol*1e-3+tol*max(abs(a), abs(b)))
                    for e, a, b in zip(err, y, yn))
        if scale > 1:
            dt *= max(.1, .9*scale**(-.2))
            rejected += 1
            if dt < 1e-13:
                return {'success': False, 'reason': 'step_underflow', 'rows': rows}
            continue
        if yn[0] <= 0:
            lo, hi = 0., dt
            for _ in range(42):
                mid = (lo+hi)/2
                ym, _ = step(s, y, mid, fun)
                if ym[0] > 0:
                    lo = mid
                else:
                    hi = mid
            last = (lo+hi)/2
            yn, _ = step(s, y, last, fun)
            yn[0] = 0.
            rows.append([s+last]+yn)
            return {'success': True, 'A': A, 'B': B, 'uc': uc, 'law': law,
                    'ell': ell, 'chi0': chi0, 'rtol': tol,
                    'surface': s+last, 'dark_mass': yn[1],
                    'chi_surface': yn[2] if law == 'gradient' else None,
                    'accepted': accepted+1, 'rejected': rejected, 'rows': rows}
        s += dt
        y = yn
        rows.append([s]+y)
        accepted += 1
        dt *= min(4., max(.2, .9*scale**(-.2))) if scale else 4.
    return {'success': False, 'reason': 'surface_not_reached', 'rows': rows}


def interpolate(sol, s):
    rows = sol['rows']
    xx = [r[0] for r in rows]
    j = max(0, min(len(xx)-2, bisect.bisect_right(xx, s)-1))
    left, right = rows[j], rows[j+1]
    dt = right[0]-left[0]
    w = (s-left[0])/dt
    # Cubic Hermite interpolation avoids the percent-level central enclosed-
    # mass bias possible with a linear interpolant on otherwise accurate steps.
    dl = (rhs(left[0], left[1:], sol['A'], sol['B'], sol['law'], sol['ell'])
          if left[0] else [0.]*len(left[1:]))
    dr = rhs(right[0], right[1:], sol['A'], sol['B'], sol['law'], sol['ell'])
    return [(2*w**3-3*w*w+1)*a+(w**3-2*w*w+w)*dt*da+
            (-2*w**3+3*w*w)*b+(w**3-w*w)*dt*db
            for a, b, da, db in zip(left[1:], right[1:], dl, dr)]


def summary(sol):
    A, B = sol['A'], sol['B']
    points = []
    for radius_in_rb in [.1, .3, 1., 2., 3.]:
        s = radius_in_rb*B
        if s >= sol['surface']:
            points.append({'r_over_rb': radius_in_rb, 'inside_fluid': False})
            continue
        y = interpolate(sol, s)
        mb = plummer(s, A, B)
        bbar = mb/s**2
        bt = (mb+y[1])/s**2
        h = h_chi(bt, y[2]) if sol['law']=='gradient' else (
            bt if sol['law']=='newton' else math.sqrt(bt) if sol['law']=='deep' else h_adiabatic(bt))
        href = h_adiabatic(bbar)
        points.append({'r_over_rb': radius_in_rb, 'inside_fluid': True,
                       'density_u': y[0], 'mass_dark': y[1], 'mass_baryon_enclosed': mb,
                       'f_enclosed': y[1]/mb if mb else None, 'g_over_a0': h,
                       'baryon_only_khoury': href,
                       'delta_dex_from_baryon_khoury': math.log10(h/href) if href else None,
                       'CDD_baryon_only': math.sqrt(bbar*bbar+bbar)})
    return {'A': A, 'B': B, 'uc': sol['uc'], 'law': sol['law'], 'ell': sol['ell'],
            'chi0': sol['chi0'], 'surface_over_rK': sol['surface'],
            'surface_over_rb': sol['surface']/B,
            'total_dark_mass_over_total_baryon_mass': sol['dark_mass']/A if A else None,
            'points': points}


def physical_scales():
    G = 6.67430e-11
    c = 299792458.
    hbar = 1.0545718176461565e-34
    hc = 1.973269804593025e-7
    eV_J = 1.602176634e-19
    kpc = 3.0856775814913673e19
    Msun = 1.98847e30
    a0 = 1.2e-10
    rk = 3*kpc
    rho = a0/(4*math.pi*G*rk)
    K = 2*math.pi*G*rk*rk
    rho_eV4_to_SI = eV_J/(hc**3*c*c)
    K_natural = K*rho_eV4_to_SI/(c*c)
    m_eV = .1
    mass_kg = m_eV*eV_J/(c*c)
    g4 = 8*m_eV**4*K_natural
    a_sc_m = g4/(16*math.pi*m_eV)*hc
    sigma_per_mass_cm2_g = 8*math.pi*a_sc_m*a_sc_m/mass_kg*10
    return {'a0_m_s2': a0, 'rK_kpc': 3., 'K_SI_m5_kgminus1_sminus2': K,
            'density_scale_kg_m3': rho,
            'density_scale_GeV_cm3': rho/(1e9*eV_J/c**2*1e6),
            'mass_scale_Msun': a0*rk*rk/G/Msun,
            'sound_speed_scale_km_s': math.sqrt(a0*rk)/1000,
            'sound_speed_squared_over_c_squared_per_u': a0*rk/(c*c),
            'm4D_input_eV': m_eV, 'quartic_convention': 'V4=(g4/2)*abs(phi)^4; K=g4/(8*m^4)',
            'K_natural_eV_minus4': K_natural, 'g4_from_common_K': g4,
            'scattering_assumptions': 'Dilute identical bosons, tree/Born contact limit, V=(g4/2)|phi|^4; sigma=8*pi*a_sc^2.',
            'scattering_length_m': a_sc_m,
            'sigma_over_m_cm2_g': sigma_per_mass_cm2_g,
            'm4D_eV_at_sigma_over_m_1_cm2_g_same_K': m_eV*sigma_per_mass_cm2_g**(-.2),
            'particle_point_status': '0.1 eV point is a unit-conversion illustration; huge vacuum sigma/m prevents claiming astrophysical viability under standard binary-scattering interpretation.',
            'healing_length_m_at_u_1': hbar/(2*mass_kg*math.sqrt(a0*rk))}


def particle_parameter_window():
    scales = physical_scales()
    hc = 1.973269804593025e-7  # eV m
    L_input_m = 1e-6
    Kn = scales['K_natural_eV_minus4']
    nr = 4*scales['sound_speed_squared_over_c_squared_per_u']
    rows = []
    for m in [.1, 1e-3, 1e-4, 1e-5]:
        rows.append({'m4D_eV': m, 'g4': 8*Kn*m**4,
                     'sigma_over_m_cm2_g_Born': scales['sigma_over_m_cm2_g']*(m/.1)**5,
                     'g4_rho_over_m4_at_rho_star': nr,
                     'm4D_times_L_dimensionless': m*L_input_m/hc,
                     'm4D_over_flat_first_KK_mass': m*L_input_m/(math.pi*hc),
                     'healing_length_m_at_rho_star': scales['healing_length_m_at_u_1']*.1/m})
    return {'status': 'Parametric contact/Born illustration at common K and a0, not an astrophysical viability region.',
            'fixed_rK_kpc': scales['rK_kpc'], 'rho_gal_kg_m3': scales['density_scale_kg_m3'],
            'rho_gal_GeV_cm3': scales['density_scale_GeV_cm3'],
            'L_input_m': L_input_m, 'inverse_L_eV': hc/L_input_m,
            'flat_interval_first_KK_mass_eV': math.pi*hc/L_input_m,
            'KK_caveat': 'L is an independent illustrative input. Warped KK masses and nonlinear truncation require the 5D eigenproblem.',
            'rows': rows}


def make_profiles(sol, count=240):
    out = []
    for j in range(count+1):
        s = sol['surface']*j/count
        if j == 0:
            out.append({'s': 0., 'u': sol['uc'], 'v': 0., 'h': 0.,
                        'chi': sol['chi0'] if sol['law']=='gradient' else None})
            continue
        y = interpolate(sol, s)
        b = (plummer(s, sol['A'], sol['B'])+y[1])/s**2
        h = h_chi(b, y[2]) if sol['law']=='gradient' else (
            b if sol['law']=='newton' else math.sqrt(b) if sol['law']=='deep' else h_adiabatic(b))
        chi = y[2] if sol['law']=='gradient' else math.sqrt(max(0., 3/h-1)) if sol['law']!='newton' else 0.
        out.append({'s': s, 'u': max(0., y[0]), 'v': y[1], 'h': h, 'chi': chi})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = ap.parse_args()
    checks = {}
    exact = solve(0., 1., 1., 'newton', tol=2e-10)
    assert exact['success']
    checks['newton_dark_only_surface_error'] = exact['surface']-math.pi
    checks['newton_dark_only_mass_error'] = exact['dark_mass']-math.pi
    assert abs(checks['newton_dark_only_surface_error']) < 1e-8
    assert abs(checks['newton_dark_only_mass_error']) < 2e-8
    checks['newton_profile_max_absolute_error'] = max(
        abs(interpolate(exact, s)[0]-math.sin(s)/s)
        for s in [math.pi*j/300 for j in range(1, 300)])
    assert checks['newton_profile_max_absolute_error'] < 2e-8
    deep = solve(0., 1., 1., 'deep', tol=2e-10)
    checks['deep_mond_dark_only_first_zero'] = deep['surface']
    checks['deep_mond_dark_only_surface_slope'] = math.sqrt(deep['dark_mass'])/deep['surface']
    checks['khoury_2016_table1_rounded_comparison'] = 'n=2: radius~2.25, slope~0.46; coarse reference, not numerical tolerance.'
    assert abs(deep['surface']-2.25) < .02
    assert abs(checks['deep_mond_dark_only_surface_slope']-.46) < .02
    cases = []
    for uc in [.1, 1., 10.]:
        for A in [.1, 1., 10.]:
            for B in [.5, 1., 2.]:
                sol = solve(A, B, uc, tol=1e-9)
                if not sol['success']:
                    raise RuntimeError((uc, A, B, sol['reason']))
                item = summary(sol)
                item['profile'] = make_profiles(sol)
                item['solver'] = {k: sol[k] for k in ['accepted', 'rejected', 'rtol']}
                cases.append(item)
    convergence = []
    for A, B, uc in [(1., 1., .1), (1., 1., 1.), (10., .5, 10.)]:
        loose = solve(A, B, uc, tol=1e-8)
        tight = solve(A, B, uc, tol=2e-11)
        convergence.append({'A': A, 'B': B, 'uc': uc,
                            'surface_relative_change': tight['surface']/loose['surface']-1,
                            'dark_mass_relative_change': tight['dark_mass']/loose['dark_mass']-1,
                            'tight_surface': tight['surface'], 'tight_dark_mass': tight['dark_mass']})
    result = {'scope': __doc__.strip(), 'method': 'Dormand-Prince 5(4), adaptive errors, bisection first-zero event; no SciPy/NumPy.',
              'common_physical_scales': physical_scales(),
              'particle_parameter_window': particle_parameter_window(),
              'state_and_galaxy_grid': 'Cartesian grid uc=[0.1,1,10], A=[0.1,1,10], B=[0.5,1,2]; no RAR fitting.',
              'adiabatic_caveat': 'Fluid density and first derivative are finite at the origin; chi~r^(-1/4) is not regular. Chi gradients and edge microphysics are omitted.',
              'mass_definition': 'Integral of material LO source rho=m P_X in the static closure; not a general identity with the improved NLO conserved charge.',
              'checks': checks, 'convergence': convergence, 'cases': cases, 'checks_passed': True}
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'saved': str(args.output), 'cases': len(cases), 'checks': checks, 'convergence': convergence}))


if __name__ == '__main__':
    main()
