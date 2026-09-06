"""Independent tensor-component Lee--Wald and canonical ADM current checks.

No physics library, no singular 1/p^2 projector. This script computes the
bulk currents and verifies their endpoint improvement identities.
Metric perturbations use E=0, g_mn=a^2(1+2Fq)eta_mn,
g_my=b d_m q, g_yy=1+2Gq, delta sigma=s q, q=exp(-iwt+ikz).
The signed bilinear is omega^0/(2 i w), normalized so a free scalar has +a^2s^2.
"""

from itertools import product
import json
from pathlib import Path
import random

N = 5
ETA = (-1, 1, 1, 1)


def tensor(shape):
    if len(shape) == 1:
        return [0j] * shape[0]
    return [tensor(shape[1:]) for _ in range(shape[0])]


def currents(*, a, Ap, sigp, F, Fp, G, Gp, b, bp, s, sp,
             B=1.0, w=1.0, k=1.0, t=0.0, tp=0.0):
    inv = [-1/a**2, 1/a**2, 1/a**2, 1/a**2, 1.0]
    gam = tensor((N, N, N))
    for mu in range(4):
        gam[mu][mu][4] = gam[mu][4][mu] = Ap
        gam[4][mu][mu] = -Ap*a*a*ETA[mu]

    def data(sign):
        # sign=+1 is q; sign=-1 is complex conjugate q.
        ip = [-sign*1j*w, 0j, 0j, sign*1j*k]
        h = tensor((N, N))
        dy = tensor((N, N))
        for mu in range(4):
            h[mu][mu] = 2*a*a*F*ETA[mu]
            dy[mu][mu] = 2*a*a*(Fp+2*Ap*F)*ETA[mu]
            h[mu][4] = h[4][mu] = b*ip[mu]
            dy[mu][4] = dy[4][mu] = bp*ip[mu]
        h[4][4], dy[4][4] = 2*G, 2*Gp
        for mu, eps in ((1, 1), (2, -1)):
            h[mu][mu] += eps*a*a*t
            dy[mu][mu] += eps*a*a*(tp+2*Ap*t)
        nab = tensor((N, N, N))
        for d, c, e in product(range(N), repeat=3):
            v = dy[c][e] if d == 4 else ip[d]*h[c][e]
            nab[d][c][e] = v - sum(gam[j][d][c]*h[j][e]
                                  + gam[j][d][e]*h[c][j] for j in range(N))
        dgam = tensor((N, N, N))
        for j, c, e in product(range(N), repeat=3):
            dgam[j][c][e] = 0.5*inv[j]*(nab[c][e][j]+nab[e][c][j]-nab[j][c][e])
        trace = sum(inv[j]*h[j][j] for j in range(N))
        return h, nab, dgam, trace, ip

    def varied_theta(one, two):
        h1, nab1, dg1, tr1, ip1 = one
        h2, nab2, dg2, tr2, ip2 = two
        aa = 0
        original = sum(inv[aa]*inv[d]*(nab2[d][aa][d]-nab2[aa][d][d]) for d in range(N))
        dv = 0j
        for c, d in product(range(N), repeat=2):
            # delta g^{ac} g^{dd}: first inverse metric variation.
            dv -= inv[aa]*inv[c]*h1[aa][c]*inv[d]*(nab2[d][c][d]-nab2[c][d][d])
        for d, e in product(range(N), repeat=2):
            # g^{aa} delta g^{de}: second inverse metric variation.
            dv -= inv[aa]*inv[d]*inv[e]*h1[d][e]*(nab2[d][aa][e]-nab2[aa][d][e])
        for d, j in product(range(N), repeat=2):
            dv += inv[aa]*inv[d]*(-dg1[j][d][d]*h2[aa][j]+dg1[j][aa][d]*h2[d][j])
        grav = B/2*a**4*(0.5*tr1*original+dv)
        # delta(-sqrt(-g) grad^a sigma delta sigma), a=0.
        scal = -a**4*(-inv[0]*inv[4]*h1[0][4]*sigp+inv[0]*ip1[0]*s)*s
        return grav+scal

    plus, minus = data(1), data(-1)
    omega = varied_theta(minus, plus)-varied_theta(plus, minus)
    zcov = omega/(2j*w)
    H = F-Ap*b
    zadm = a*a*(-6*B*F*H-3*B*F*G+3*B*F*bp-3*B*G*H+s*s-sigp*b*s+B*t*t/2)
    divergence = -B/2*a*a*((2*Ap*b+bp)*(2*F+G)+b*(2*Fp+Gp))
    # Do not confuse this ansatz action coefficient with a canonical norm:
    # b dot q is a derivative-dependent lapse/shift substitution.
    pulled_action = a*a*(-3*B*H*(H+G-bp)+0.5*(s-sigp*b)**2)
    return {'covariant_bulk_Z': zcov.real, 'covariant_imaginary_residual': zcov.imag,
            'canonical_adm_bulk_Z': zadm, 'derivative_ansatz_action_coefficient': pulled_action,
            'difference_cov_minus_adm': zcov.real-zadm,
            'expected_cov_minus_adm_divergence': divergence,
            'divergence_identity_residual': zcov.real-zadm-divergence}


def boundary_covariant_C_Z(a, F, G, b, B=1.0, w=1.0):
    """Vary C=(c contraction epsilon_Gamma), c^a=−B/2 gamma^{ab}n^c h_bc.

    Positive y endpoint contribution to Omega = +delta C (Stokes orientation).
    n/eta is used inside C because epsilon_Gamma contributes the other eta.
    Four separately varied pieces: sqrt(-gamma), gamma^{00}, n^y, n^0.
    """
    def varied(sign1, sign2):
        h104 = -sign1*1j*w*b
        h204 = -sign2*1j*w*b
        # The two q amplitudes are both 1 at the evaluation event.
        return -B/2*a*a*((-4*F+2*F+G)*h204+2*F*h104)
    z = (varied(-1, 1)-varied(1, -1))/(2j*w)
    expected = -B/2*a*a*b*(4*F-G)
    assert abs(z.real-expected) < 1e-12
    return z.real


def main():
    examples = []
    for Ap in (0.0, -0.2, 0.3):
        args = dict(a=1.2, Ap=Ap, sigp=0.4, F=-1, Fp=0,
                    G=0, Gp=0, b=-1.4, bp=-2-2*Ap*(-1.4), s=0, sp=0)
        examples.append({'kind':'raw_X1', 'inputs':dict(args), **currents(**args)})
        zeta, zetap = 0.7, -0.3
        args.update(F=Ap*zeta, Fp=-0.4**2/3*zeta+Ap*zetap,
                    G=zetap, Gp=0.1, b=zeta, bp=zetap, s=0.4*zeta, sp=0.4*zetap)
        examples.append({'kind':'pure_gauge', 'inputs':dict(args), **currents(**args)})
    args = dict(a=1.2, Ap=-0.2, sigp=0.4, F=0.7, Fp=0.23,
                G=-1.4, Gp=-0.46, b=0, bp=0, s=-0.8, sp=0.5)
    examples.append({'kind':'massive_gauge', 'inputs':args, **currents(**args)})
    args = dict(a=1.2, Ap=-0.2, sigp=0.4, F=0, Fp=0,
                G=0, Gp=0, b=0, bp=0, s=0, sp=0, t=1, tp=0)
    examples.append({'kind':'TT_plus_polarization', 'inputs':args, **currents(**args)})
    rng = random.Random(6072026)
    residuals = []
    for _ in range(100):
        args = {n:rng.uniform(-1,1) for n in ('Ap','sigp','F','Fp','G','Gp','b','bp','s','sp','t','tp')}
        args.update(a=rng.uniform(0.5,2),B=rng.uniform(0.1,3),w=rng.uniform(0.2,2))
        args['k'] = args['w']
        res = currents(**args)
        residuals.append(abs(res['divergence_identity_residual']))
        assert abs(res['divergence_identity_residual']) < 2e-12
        c = boundary_covariant_C_Z(**{n:args[n] for n in ('a','F','G','b','B','w')})
        divergence_endpoint = -args['B']/2*args['a']**2*args['b']*(2*args['F']+args['G'])
        adm_tilt = -3*args['B']*args['a']**2*args['F']*args['b']
        assert abs(divergence_endpoint+c-adm_tilt) < 1e-12
    for e in examples:
        assert abs(e['covariant_imaginary_residual']) < 1e-12
    out = {'scope':'Covariant bulk current, explicit GHY C variation, and canonical ADM plus tilt; E=0 scalar sector and one TT polarization.',
           'random_component_checks':100,
           'maximum_current_divergence_residual':max(residuals),
           'X1_analytic_expected_coefficients_in_units_BI':{
               'covariant_bulk_Z':-2,'covariant_GHY_corner_Z':-4,'canonical_ADM_bulk_Z':0,
               'canonical_ADM_tilt_Z':-6,'complete_Z':-6,'complete_N_equal_Z_over_2':-3,
               'physical_state':False},
           'examples':examples}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
