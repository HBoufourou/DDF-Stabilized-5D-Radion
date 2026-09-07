"""Small numerical counterchecks for claims made in the supplied reviews.

These evaluate elementary formulas, not the background or spectral solvers.
"""
import json
import math
from pathlib import Path

x=4.0
T=math.tanh(x/2)
C=math.cosh(x/2)**2
S=math.sinh(x)
c0=(1+T*T+2*T/x)/C
cinf=4*(math.cosh(x)-S/x)/(S*S)
assert 0 < cinf < c0 < 1/3

mu=1.0
lam=0.5
v=0.3
vacuum=0.01125
B=1.0
a=2*lam/mu
zeta=math.sqrt(2)*lam*v/math.sqrt(vacuum)
Lflat=2/mu*math.log((zeta+math.sqrt(zeta*zeta+a*a-1))/(1+a))
u=mu*Lflat/2
qcenter_flat=2*lam*v/(math.cosh(u)+a*math.sinh(u))
qcenter_exact=math.sqrt(2*vacuum)
assert abs(qcenter_flat-qcenter_exact)<1e-14
h_lower=(vacuum-2*lam*lam*v*v)/(6*B)
h_upper=vacuum/(6*B)
h_bad=-1.0
q_bad=math.sqrt(2*vacuum-12*B*h_bad)
assert h_bad<h_upper and q_bad>2*lam*v

W0=-2*math.tanh(1)
eta0=-1
lambda_hat=20.0
correct_weight=eta0*W0+2*lambda_hat
review_weight=eta0*W0+2*eta0*lambda_hat
assert correct_weight>0 and review_weight<0

out={
    'scope':'Elementary counterchecks of supplied-review claims; no new spectral or physical test.',
    'coupling_coefficient_counterexample':{'x':x,'c_affine':c0,'c_rigid':cinf,
       'all_intermediate_stiffness_coefficients_less_than_one_third':True,
       'manuscript_claimed_bound':'0 < c_infinity <= c_alpha <= c_0; not c_alpha > 1/3'},
    'flat_center_slope_identity':{'mu':mu,'lambda':lam,'v':v,'Lambda5':vacuum,
       'L_flat':Lflat,'q_flat_center':qcenter_flat,'q_exact_center':qcenter_exact},
    'curved_trial_necessary_bounds':{'lower':h_lower,'upper':h_upper,'counterexample_trial_h':h_bad,
       'q_center':q_bad,'2_lambda_v':2*lam*v,'F_at_center':q_bad-2*lam*v,
       'interpretation':'Real central slope alone does not imply a positive scalar boundary event.'},
    'endpoint_weight_sign_counterexample':{'eta0':eta0,'W0':W0,'lambda_hat':lambda_hat,
       'correct_eta_W_plus_2lambda':correct_weight,'review_eta_W_plus_2eta_lambda':review_weight},
    'checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
