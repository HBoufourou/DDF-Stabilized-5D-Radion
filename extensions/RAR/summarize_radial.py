"""Compact diagnostics and a figure for the conditional radial calculation."""
from pathlib import Path
import json
import os
ROOT=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'mpl-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data=json.loads((ROOT/'rar_radial_bvp.json').read_text())
alternatives=data['alternative_seed_cases']
def find(seq,A,ell):return next(r for r in seq if r['A']==A and r['ell_over_rb']==ell)
comparisons=[]
for ell in (.1,.03):
    old=find(data['cases'],10,ell);new=find(alternatives,10,ell)
    delta=new['reduced_static_energy']['energy']-old['reduced_static_energy']['energy']
    assert delta<0
    comparisons.append(dict(A=10,ell=ell,energy_positive_minus_central_zero=delta,
        central_zero_eigenvalue=old['reduced_radial_jacobian']['eigenvalues'][0],
        central_positive_eigenvalue=new['reduced_radial_jacobian']['eigenvalues'][0]))
refinements=data['refinements_and_source_variations']
base=find(alternatives,10,.1)
common=np.geomspace(.05,10,500)
def hp(row):return np.interp(common,row['profiles']['s'],row['profiles']['h'])
variations=[]
for row in refinements:
    if row['ell_over_rb']!=.1:continue
    variations.append(dict(outer=row['outer_over_rb'],f=row['f'],
                           max_h_fractional_change_vs_base=float(np.max(np.abs(hp(row)/hp(base)-1))),
                           h_ratio_at_r_equals_10rb=float(hp(row)[-1]/hp(base)[-1])))
report=dict(energy_comparisons=comparisons,source_and_domain_variations=variations,
    domains='Comparisons on 0.05<=r/rb<=10; interpolation of saved profiles for variation diagnostics.',
    software=dict(numpy=np.__version__,matplotlib=matplotlib.__version__),
    branch_count_converged=sum(r['status'].startswith('CONVERGED') for r in data['cases']+alternatives),
    branch_attempts=len(data['cases'])+len(alternatives))
(ROOT/'radial_summary.json').write_text(json.dumps(report,indent=2)+'\n')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,
                     'axes.spines.right':False,'svg.fonttype':'none'})
fig,(ax,bx)=plt.subplots(2,1,figsize=(10.8,8.2),sharex=True,gridspec_kw={'height_ratios':[1.25,1]})
fig.subplots_adjust(left=.11,right=.97,top=.84,bottom=.14,hspace=.13)
fig.text(.11,.95,'RAR : les gradients sélectionnent des branches différentes',fontsize=17,weight='bold',color='#173d54')
fig.text(.11,.902,'Source de Plummer imposée, A = 10 • conditions extérieures identiques • problème radial conditionnel',fontsize=10.2,color='#506170')
for ell,col in ((.3,'#c77615'),(.1,'#137991'),(.03,'#783a83')):
    row=find(alternatives,10,ell)
    p=row['profiles'];s=np.array(p['s']);keep=s>0
    ax.semilogx(s[keep],np.array(p['chi'])[keep],lw=2,color=col,label=f'Branche retenue : ℓχ/rᵦ = {ell:g}')
    bx.semilogx(s[keep],np.array(p['h'])[keep]/np.array(p['h_adiabatic'])[keep]-1,lw=2,color=col)
old=find(data['cases'],10,.1);p=old['profiles'];s=np.array(p['s']);keep=s>0
ax.semilogx(s[keep],np.array(p['chi'])[keep],ls='--',color='#b23840',lw=1.5,label='Branche à cœur instable : ℓχ/rᵦ = 0,1')
bx.semilogx(s[keep],np.array(p['h'])[keep]/np.array(p['h_adiabatic'])[keep]-1,ls='--',color='#b23840',lw=1.5)
ax.set_ylabel('Champ supplémentaire χ');ax.set_ylim(-.08,4.6)
ax.legend(loc='upper left',framealpha=.96,fontsize=9.7)
bx.axhline(0,color='#566673',lw=.8);bx.set_ylabel('g / g adiabatique − 1')
bx.set_ylim(-.55,.25);bx.set_xlabel('Rayon r / rayon de la source rᵦ')
bx.set_xlim(.008,20)
for axis in (ax,bx):axis.grid(alpha=.15)
fig.text(.11,.06,'La densité du condensat et sa frontière ne sont pas résolues. a₀ et ℓχ sont des entrées ; aucun rayon R n’est prédit.',fontsize=9.1,color='#506170')
fig.text(.11,.032,'Branches retenues : contrôle radial positif. Deux comparaisons d’énergie favorables ; aucune stabilité relativiste globale établie.',fontsize=9.1,color='#506170')
out=ROOT/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'rar_branches.png',dpi=170)
fig.savefig(out/'rar_branches.svg')
print(json.dumps(report,indent=2))
