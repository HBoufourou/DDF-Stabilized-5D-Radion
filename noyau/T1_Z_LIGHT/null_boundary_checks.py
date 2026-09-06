"""Exact rational Laurent-polynomial checks of the null boundary kernel.

Standard library only. All denominators are monomials. No numerical sampling,
tolerance or inverse of p^2 is used. The accompanying analytic proof explains
integration, completeness and gauge quotient. This script computes no norm.
"""
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


class P:
    """Finite Laurent polynomial over exact rational numbers."""
    def __init__(self,value=0):
        if isinstance(value,P):self.terms=dict(value.terms)
        elif isinstance(value,dict):self.terms={m:Fraction(c) for m,c in value.items() if c}
        else:
            c=Fraction(value)
            self.terms={():c} if c else {}

    @staticmethod
    def symbol(name):return P({((name,1),):Fraction(1)})

    def __add__(self,other):
        result=dict(self.terms)
        for monomial,coef in P(other).terms.items():
            result[monomial]=result.get(monomial,Fraction(0))+coef
        return P(result)

    __radd__=__add__

    def __neg__(self):return P({m:-c for m,c in self.terms.items()})
    def __sub__(self,other):return self+(-P(other))
    def __rsub__(self,other):return P(other)+(-self)

    def __mul__(self,other):
        result={}
        for ma,ca in self.terms.items():
            for mb,cb in P(other).terms.items():
                powers=dict(ma)
                for name,power in mb:powers[name]=powers.get(name,0)+power
                monomial=tuple(sorted((name,power) for name,power in powers.items() if power))
                result[monomial]=result.get(monomial,Fraction(0))+ca*cb
        return P(result)

    __rmul__=__mul__

    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('Only integer powers are allowed')
        if n<0:
            if len(self.terms)!=1:raise ValueError('Non-monomial denominator requested')
            monomial,coef=next(iter(self.terms.items()))
            return P({tuple((name,power*n) for name,power in monomial):coef**n})
        result=P(1)
        for _ in range(n):result=result*self
        return result

    def __truediv__(self,other):return self*(P(other)**-1)
    def __rtruediv__(self,other):return P(other)*(self**-1)

    def partial(self,name):
        result={}
        for monomial,coef in self.terms.items():
            powers=dict(monomial)
            exponent=powers.get(name,0)
            if exponent:
                powers[name]=exponent-1
                changed=tuple(sorted((v,e) for v,e in powers.items() if e))
                result[changed]=result.get(changed,Fraction(0))+coef*exponent
        return P(result)

    def __str__(self):
        if not self.terms:return '0'
        return ' + '.join(str(c)+'*'+'*'.join(name+('^'+str(power) if power!=1 else '')
            for name,power in monomial) for monomial,c in sorted(self.terms.items()))


def symbols(names):return [P.symbol(name) for name in names.split()]
def matrix(rows,cols,function):return [[function(i,j) for j in range(cols)] for i in range(rows)]


def determinant(mat):
    result=P(0)
    n=len(mat)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        product=P(-1 if inversions%2 else 1)
        for i,j in enumerate(perm):product*=mat[i][j]
        result+=product
    return result


def main():
    checks={}

    def zero(label,expression):
        if P(expression).terms:raise AssertionError((label,str(expression)))
        checks[label]='PASS'

    aa,bb=symbols('aa bb')
    zero('arithmetic_binomial',(aa+bb)**3-aa**3-3*aa**2*bb-3*aa*bb**2-bb**3)
    zero('arithmetic_inverse',(aa/bb)*bb-aa)
    zero('arithmetic_negative_power_derivative',(aa**-2).partial('aa')+2*aa**-3)

    # Null frame (+,-,1,2): eta_+-=-1 and p_mu=(k,0,0,0).
    k=P.symbol('k')
    eta=[[0,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]]
    p=[k,P(0),P(0),P(0)]
    pup=[sum(eta[i][j]*p[j] for j in range(4)) for i in range(4)]
    pairs=[(i,j) for i in range(4) for j in range(i,4)]
    hvars={pair:P.symbol('h%d%d'%pair) for pair in pairs}
    hpvars={pair:P.symbol('d_h%d%d'%pair) for pair in pairs}
    h=matrix(4,4,lambda i,j:hvars[tuple(sorted((i,j)))])
    hp=matrix(4,4,lambda i,j:hpvars[tuple(sorted((i,j)))])
    trh=sum(eta[i][j]*h[j][i] for i in range(4) for j in range(4))
    trhp=sum(eta[i][j]*hp[j][i] for i in range(4) for j in range(4))
    p2=sum(p[i]*pup[i] for i in range(4))
    ricci=matrix(4,4,lambda i,j:(p2*h[i][j]+p[i]*p[j]*trh
        -p[i]*sum(pup[r]*h[r][j] for r in range(4))
        -p[j]*sum(pup[r]*h[r][i] for r in range(4)))/2)
    momentum=[(sum(pup[r]*hp[i][r] for r in range(4))-p[i]*trhp)/2 for i in range(4)]
    zero('null_p_squared',p2)
    zero('ricci_minus_minus',ricci[1][1])
    zero('ricci_plus_minus',ricci[0][1]-k*k*h[1][1]/2)
    zero('ricci_plus_plus',ricci[0][0]-k*k*(h[2][2]+h[3][3])/2)
    zero('ricci_trace',sum(eta[i][j]*ricci[j][i] for i in range(4) for j in range(4))+k*k*h[1][1])
    zero('momentum_minus',momentum[1]+k*hp[1][1]/2)
    for index in (2,3):
        zero('ricci_minus_%d'%index,ricci[1][index])
        zero('ricci_plus_%d'%index,ricci[0][index]-k*k*h[1][index]/2)
        zero('ricci_%d_%d'%(index,index),ricci[index][index])
        zero('momentum_%d'%index,momentum[index]+k*hp[1][index]/2)

    # Differential algebra modulo the exact flat-background equations.
    B,mu,a,q,r,z,zp,zpp,zppp,I,H,c,C=symbols('B mu a q r z zp zpp zppp I H c C')
    ap=-q*q/(3*B)
    rp=mu*mu*q-4*a*r+4*q**3/(3*B)
    jets={'a':ap,'q':r,'r':rp,'z':zp,'zp':zpp,'zpp':zppp,'I':H,'H':2*a*H}

    def derivative(expression):return sum(P(expression).partial(name)*rhs for name,rhs in jets.items())

    V=q*q/2-6*B*a*a
    Vs=r+4*a*q
    zero('background_potential_chain_rule',derivative(V)-q*Vs)
    F,G,s,chi=a*z-c,zp,q*z,z-(2*c*I+C)/H
    Fp,sp1=derivative(F),derivative(s)
    C1=3*B*(Fp-a*G)+q*s
    H55=12*B*a*(Fp-a*G)-q*(sp1-q*G)+Vs*s
    trace=derivative(Fp)+8*a*Fp-a*derivative(G)-2*G*(ap+4*a*a)+2*Vs*s/(3*B)
    scalar=derivative(sp1)+4*a*sp1-mu*mu*s+4*q*Fp-q*derivative(G)-2*Vs*G
    dd=derivative(chi)+2*a*chi-2*F-G
    for name,expression in [('bulk_mu5_kernel',C1),('bulk_55_kernel',H55),
                            ('bulk_trace_kernel',trace),('bulk_scalar_kernel',scalar),('bulk_dd_kernel',dd)]:
        zero(name,expression)

    fp,gg,ss,spv=symbols('fp gg ss spv')
    hc=12*B*a*(fp-a*gg)-q*(spv-q*gg)+Vs*ss
    cc=3*B*(fp-a*gg)+q*ss
    zero('hamiltonian_minus_four_a_constraint',hc-4*a*cc+q*(spv-q*gg)-r*ss)

    eta_i,upp,Z=symbols('eta_i U_second Z')
    D=r/q+eta_i*upp
    scalar_bc=sp1-q*G+eta_i*upp*s+(r+eta_i*upp*q)*Z
    trace_bc=C1+(3*B*ap+q*q)*Z
    zero('edge_scalar_Robin',scalar_bc-q*D*(z+Z))
    zero('edge_trace_Israel',trace_bc)
    zero('edge_traceless_Israel',(chi+Z)-(z+Z-(2*c*I+C)/H))

    q0,qL,D0,DL,H0,HL,IL=symbols('q0 qL D0 DL H0 HL IL')
    boundary_matrix=[[0,0,q0*D0,0],[0,0,0,qL*DL],
                     [0,-1/H0,1,0],[-2*IL/HL,-1/HL,0,1]]
    det=determinant(boundary_matrix)
    zero('boundary_rank_determinant',det+2*IL*q0*qL*D0*DL/(H0*HL))
    if len(det.terms)!=1:raise AssertionError('Generic determinant must be a nonzero monomial')
    checks['boundary_rank_generic_four']='PASS'

    result={
        'purpose':'Exact algebraic replay of null-frame component reduction and edge-completed boundary kernel',
        'arithmetic':'Laurent polynomials over fractions.Fraction; standard library; no numerical tolerance',
        'assumptions':['B=M5^3>0','p_mu nonzero and p^2=0','smooth finite flat interval',
                       'sigma_prime has no zero','D_i=W_i+eta_i U_i_second nonzero',
                       'pure isotropic brane potentials, no brane kinetic terms','vacuum matter'],
        'checks':checks,
        'number_of_exact_zero_checks':len(checks)-1,
        'boundary_matrix_determinant':str(det),
        'null_frame_remaining_physical_polarizations':'two transverse traceless massless graviton polarizations',
        'scalar_derived_null_quotient':'trivial under the declared domain and edge quotient',
        'presymplectic_norm_computed_by_this_script':False,
        'does_not_claim':'nonlinear, curved-background, experimental or full-theory viability'}
    destination=Path(__file__).with_suffix('.json')
    destination.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','checks':len(checks),'saved':str(destination)},indent=2))


if __name__=='__main__':main()
