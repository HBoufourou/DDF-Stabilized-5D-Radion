# Controlled Kaluza–Klein reduction of a charged scalar on a stabilized interval

**Research basis for a second article — 6 September 2026.** This document is a structured basis, not a complete manuscript. It uses the derivations in `matiere/Phi/FERMETURE_PHI.md`; the numbers below were checked against `matiere/Phi/phi_projection.json`.

## Provisional abstract

We study a canonical complex scalar with repulsive quartic interaction on a fixed, reflection-symmetric stabilized five-dimensional interval. A spatially constant displacement is not the fundamental Neumann eigenmode when both the bulk mass and warping are nonzero. We quantify its projection onto excited Kaluza–Klein modes and derive a continuum bound using the spectral variance of the constant profile. Quartic interactions generally prevent an exact truncation to the free fundamental mode. We instead construct density-dependent stationary charged profiles, establish their linear stability in the fixed-metric probe sector under the nodeless-profile assumption, and compare their admixtures with perturbation theory. Twelve nonlinear profiles are computed at three positive bulk masses. A separate third-harmonic frequency coincidence illustrates why these results cannot be transferred directly to real, charge-neutral misalignment. Initial charge, cosmological abundance and gravitational backreaction are outside this study.

## Model and exact scope

For `ds²=e^(2A)ημνdxμdxν+dy²`, the additional action is

\[
S_\Phi=-\int d^4x\,dy\sqrt{-g_5}
\left(|\partial\Phi|^2+m_\Phi^2|\Phi|^2+\frac{g_5}{2}|\Phi|^4\right),
\quad m_\Phi^2\ge0,\ g_5\ge0.
\]

Here the interaction coefficient g₅ has mass dimension −1. No Φ boundary potential or portal is included, so Φ′=0 at both ends. The stabilizer and metric are fixed. The numerical benchmark has x=μL=2, ε=0.30 and A(0)=A(L)=0; it is not a scan over gravitating actions. Its fixed geometry may be realized by reconstructed quadratic stabilizer boundary potentials, which must be specified when connecting this study to Article 1. U(1) conserves total charge, not KK level. A finite charged profile is an assumed state, not a calculated thermal condensate.

## Results available for the manuscript

1. **Free projection and continuum control.** With p=e⁴ᴬ, w=e²ᴬ, the operator is H=w⁻¹[−∂y(p∂y)+mΦ²p]. A constant is an eigenfunction only if mΦ=0 or A is constant. Reflection removes odd-mode projections. For a normalized constant at rest, its spectral variance gives a bound on the entire excited tower, independently of truncating a numerical sum.
2. **Nonlinear closure.** The omitted-mode source is g₅λn000|φ₀|²φ₀, with λn000=∫pψnψ₀³dy. Exact cancellation would require e²ᴬψ₀² constant, incompatible with Neumann conditions when A′ is nonzero at a boundary. A stationary charged profile instead solves `H uF + g5 F² e^(2A)uF³ = ω²uF`, with ∫wuF²dy=1. For a positive profile, H₋uF=0 and H₊=H₋+2g₅F²e²ᴬuF² imply a nonnegative conserved perturbation energy, modulo the neutral U(1) phase. This proves linear probe stability, not stability against gravitational collapse.
3. **Distinct dynamical regimes.** A charged rotation has a single temporal phase. Real oscillation sources both m₀ and 3m₀. The benchmark has m₂=3m₀ at mΦL≈2.2285363, with Lλ2000≈−0.00821004. This is a linear-frequency coincidence with a nonzero vertex, not a computed transfer rate or cosmological exclusion.

## Verified benchmark data

Let η=g₄F²L², with g₄=g₅λ0000. All entries are dimensionless; no physical compactification length is selected.

| mΦL | Initial free KK energy fraction | Continuum upper bound | Charged-profile KK norm fraction at η=0.1 |
|---:|---:|---:|---:|
| 0.1 | 3.07414×10⁻⁸ | 3.59289×10⁻⁸ | 7.11028×10⁻¹⁰ |
| 1 | 3.14969×10⁻⁶ | 3.69213×10⁻⁶ | 6.42646×10⁻¹⁰ |
| 3 | 3.38500×10⁻⁵ | 4.05435×10⁻⁵ | 2.16714×10⁻¹⁰ |

The twelve charged profiles use these three masses and η={0.001,0.01,0.1,1}. The massless free case is an additional analytic control: a constant at rest has zero energy, so its energy fraction is undefined. Norm fractions are not particle fractions. Weak shape deformation requires η≪(m₂²−m₀²)L²; a nonrelativistic harmonic interpretation additionally requires η≪m₀²L². At mΦL=0.1 and η=0.1, the latter ratio is about 9.72, so that profile is not a nonrelativistic harmonic condensate.

## Proposed sections and primary comparisons

Suggested structure: (1) model and probe regime; (2) free spectral projection and bounds; (3) quartic source and effective reduction; (4) stationary charged profiles and stability; (5) numerical verification; (6) charge-neutral resonance diagnostic; (7) limitations and conclusions. Figures should display a profile deformation, the projection bound and the η-dependence of perturbative error.

Two references already identified in the technical note have verified metadata: Pons–Talavera, *Consistent and inconsistent truncations. Some results and the issue of the correct uplifting of solutions*, Nucl. Phys. B **678**, 427–454 (2004), [hep-th/0309079](https://arxiv.org/abs/hep-th/0309079); Boyle–Caldwell–Kamionkowski, *Spintessence! New Models for Dark Matter and Dark Energy*, Phys. Lett. B **545**, 17–22 (2002), [astro-ph/0105318](https://arxiv.org/abs/astro-ph/0105318). They establish relevant prior frameworks, not this benchmark. Their detailed results and the related literature on nonlinear mode elimination must be compared before any priority claim. Article 1 supplies the independently cited stabilized-background framework. No originality claim follows from the present targeted bibliography.

## Reproduction and completion

| Repository file | What it supplies |
|---|---|
| `matiere/Phi/FERMETURE_PHI.md` | Action, projection bound, closure criterion, perturbative profile, stability argument and limitations. |
| `matiere/Phi/phi_projection.py` | Independent background integration, cosine Galerkin spectrum, projection, twelve charged solutions and resonance diagnostic; Python standard library plus NumPy. Run `python matiere/Phi/phi_projection.py` from the repository root; it writes the adjacent JSON. |
| `matiere/Phi/phi_projection.json` | Three basis refinements (24, 40, 64 functions), numerical bounds, nonlinear residuals and profile checks. |
| `matiere/Phi/input_data/phi_spectrum.json` | Optional earlier FEM mass references; no external solver is imported. Selected mass comparisons agree within 3.84×10⁻¹¹ relatively, which is not an error bound for every nonlinear observable. |

A complete specialist manuscript needs the proofs written consistently, the benchmark’s stabilizer boundary realization declared, figures generated from the recorded data, convergence and approximation domains displayed, and a focused comparison with prior work. These are proportionate requirements. A cosmological origin of charge, an absolute prediction of L, or a solution of RAR is not required for this explicitly limited probe study. Claims about those subjects would require additional calculations.
