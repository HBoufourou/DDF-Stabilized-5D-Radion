"""Finite bookkeeping and analytic excursion checks; not a string background."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent

def main():
    ends=[]
    for n0 in range(17):
        nL=16-n0
        ends.append(dict(N0=n0,NL=nL,Ninterior=0,
                         net0=n0-8,netL=nL-8,
                         both_strictly_negative=(n0<8 and nL<8)))
    interiors=[]
    for n0 in range(8):
        for nL in range(8):
            interiors.append(dict(N0=n0,NL=nL,Ninterior=16-n0-nL,
                                  net0=n0-8,netL=nL-8))
    profile_checks=[]
    # L=q=1; sigma=q sinh(mu*(y-L/2))/(mu cosh(mu L/2)).
    # This is a flat scalar profile, not an exact Einstein-scalar background.
    for x in [.1,1,2,3,6]:
        kinetic=(.5+math.sinh(x)/(2*x))/math.cosh(x/2)**2
        excursion=2*math.tanh(x/2)/x
        bound=excursion**2
        profile_checks.append(dict(x=x,integral_sigma_prime_squared=kinetic,
                                   excursion_squared_over_L=bound,
                                   ratio_to_Cauchy_bound=kinetic/bound))
    assert not any(r['both_strictly_negative'] for r in ends)
    assert min(r['Ninterior'] for r in interiors)==2
    assert all(r['ratio_to_Cauchy_bound']>1 for r in profile_checks)
    result=dict(convention='Quotient: O8^- charge -8; 16 physical D8. Cover doubles charges and brane count.',
        endpoints_only=ends,
        number_of_integer_occupancy_triplets_with_both_negative=len(interiors),
        minimum_interior_physical_D8_for_two_negative_endpoints=2,
        triplets_with_both_negative=interiors,
        flat_scalar_excursion_examples=profile_checks,
        scope='No new string solution, quantum stability claim or radius prediction.')
    out=ROOT/'uv_matching_checks.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(endpoints_only_cases=len(ends),both_negative_endpoints_only=0,
        interior_triplets=len(interiors),minimum_interior_D8=2,
        excursion_checks=profile_checks),indent=2))

if __name__=='__main__':main()
