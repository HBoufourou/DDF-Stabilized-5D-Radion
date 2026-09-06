"""Review-only independent temporal ADM tensor contraction, stdlib only.

This checker reconstructs the first-order extrinsic curvature of the t=const
four-space and conjugate momenta. It does not reuse the condensed ADM formula
when calculating its own value. Import of the companion calculation serves
only to compare outputs. No equation of motion or endpoint assumption is used.
"""
import importlib.util
import json
from pathlib import Path
import random

PATH = Path(__file__).with_name('covariant_adm_current.py')
SPEC = importlib.util.spec_from_file_location('current_under_review', PATH)
CURRENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CURRENT)


def direct_adm(a, Ap, sigp, F, Fp, G, Gp, b, bp, s, sp,
               B=1., w=1., k=1., t=0., tp=0.):
    # Spatial positions 0,1,2,3 correspond to spacetime x1,x2,x3,y.
    inverse = [1/a**2] * 3 + [1.]
    gamma = [[[0.] * 4 for _ in range(4)] for _ in range(4)]
    for i in range(3):
        gamma[i][i][3] = gamma[i][3][i] = Ap
        gamma[3][i][i] = -a*a*Ap

    def perturbation(sign):
        h = [[0j] * 4 for _ in range(4)]
        ip = [0j, 0j, sign*1j*k]
        for i in range(3):
            h[i][i] = 2*a*a*F
            h[i][3] = h[3][i] = b*ip[i]
        h[0][0] += a*a*t
        h[1][1] -= a*a*t
        h[3][3] = 2*G
        shift = [0j, 0j, 0j, -sign*1j*w*b]
        gradshift = [[0j] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                partial = 0j
                if j == 3:
                    partial = -sign*1j*w*bp if i == 3 else ip[i]*shift[j]
                gradshift[i][j] = partial - sum(gamma[z][i][j]*shift[z] for z in range(4))
        K = [[(-sign*1j*w*h[i][j]-gradshift[i][j]-gradshift[j][i])/(2*a)
              for j in range(4)] for i in range(4)]
        trK = sum(inverse[i]*K[i][i] for i in range(4))
        pi = [[B*a**3/2*(inverse[i]*inverse[j]*K[i][j]
                - (inverse[i]*trK if i == j else 0)) for j in range(4)] for i in range(4)]
        pis = a*a*(-sign*1j*w*s-shift[3]*sigp)
        return h, pi, pis

    hp, pp, psp = perturbation(1)
    hm, pm, psm = perturbation(-1)
    omega = sum(pm[i][j]*hp[i][j]-pp[i][j]*hm[i][j]
                for i in range(4) for j in range(4)) + psm*s-psp*s
    return omega/(2j*w)


def main():
    rng = random.Random(60413)
    residuals = []
    for _ in range(128):
        kw = {key:rng.uniform(-1,1) for key in
              ('Ap','sigp','F','Fp','G','Gp','b','bp','s','sp','t','tp')}
        kw.update(a=rng.uniform(.4,2), B=rng.uniform(.1,3), w=rng.uniform(.2,2))
        kw['k'] = kw['w']
        actual = direct_adm(**kw)
        published = CURRENT.currents(**kw)['canonical_adm_bulk_Z']
        error = abs(actual-published)
        assert error < 2e-12
        residuals.append(error)
    result = {'scope':'Independent time-ADM component review, E=0 scalar ansatz plus TT plus polarization; no boundary/gauge quotient proof.',
              'random_component_comparisons':len(residuals),
              'maximum_absolute_difference':max(residuals),
              'checks_passed':True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
