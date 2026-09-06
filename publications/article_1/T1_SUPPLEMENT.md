# Supplement: null-shell admissibility and the T1 test

**Supplement to “Boundary stiffness, radion residues and fixed-action length selection in a five-dimensional interval”**  
Hicham Boufourou — 6 September 2026

This separate supplement supplies the null-shell domain analysis that cannot be inferred from the positive massive-scalar norm alone. The main manuscript PDF has **not** been regenerated with this text. The result below concerns the same classical action and strengthens its stated linear stability domain; it does not establish a complete DDF theory.

## Action and domain

We use one physical interval, outward normals η₀=−1 and ηᴸ=+1, signature −++++, and

\[
S=\int_M\sqrt{-g}\left[\frac B2R-\frac12(\partial\sigma)^2-V(\sigma)\right]
+B\int_{\partial M}\sqrt{-\gamma}K
-\sum_i\int_i\sqrt{-\gamma}\,U_i(\sigma),
\]

where B=M₅³>0, V=Λ₅+μ²σ²/2, and Uᵢ=τᵢ+λᵢ(σ−vᵢ)². Boundary potentials are isotropic; no boundary kinetic operator is added. The background is smooth, has flat four-dimensional slices, and satisfies

\[
ds^2=e^{2A}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2,
\quad q=\sigma_0'\ne0,
\quad A''=-q^2/(3B).
\]

For the null analysis, Dᵢ=Wᵢ+2ηᵢλᵢ must be nonzero, with W=q′/q. Combining this result with the manuscript’s massive-mode positivity requires ηᵢWᵢ+2λᵢ>0. The regular principal symmetric branch with μ,Λ₅,λᵢ>0 satisfies these conditions. We study p²=0, p^μ≠0, using Fourier normalization per unit spatial volume, or wave packets without additional asymptotic charges. No projector containing 1/p² is used.

## Complete null kernel and boundary conditions

A scalar ansatz alone does not prove completeness on the light cone. We first use Gaussian normal bulk coordinates, retaining the boundary displacements, and a null basis (+,−,1,2) with p_μ=(k,0,0,0), k≠0. Let t=(h₁₁+h₂₂)/2. The mixed Einstein equations imply h′₋₋=h′₋ₐ=0. Further components give

\[
[e^{4A}(h_{+-}+t)']'=k^2e^{2A}h_{--},
\qquad(e^{4A}h'_{+a})'=k^2e^{2A}h_{-a}.
\]

The corresponding endpoint derivatives vanish by the complete Israel conditions. Integrating forces h₋₋=h₋ₐ=0. Residual tangential diffeomorphisms remove the remaining constant combinations. This eliminates components absent from the customary scalar decomposition without dividing by p². The transverse, trace-free 2×2 block retains exactly two graviton polarizations; their radial profiles are constant.

For the remaining scalar/longitudinal block, write

\[
\delta g_{\mu\nu}=e^{2A}(2F\eta_{\mu\nu}\varphi
+2\widehat E\partial_\mu\partial_\nu\varphi),\quad
\delta g_{\mu5}=b\partial_\mu\varphi,
\quad\delta g_{55}=2G\varphi,\quad\delta\sigma=s\varphi.
\]

Define χ=b−e²ᴬÊ′ and I(y)=∫₀ʸe²ᴬdu. Direct mixed and normal Einstein equations give

\[
3B(F'-A'G)+qs=0,
\qquad q(s'-qG)-q's=0.
\]

Thus, with z=s/q, the general solution is

\[
F=A'z-c_1,\quad G=z',\quad s=qz,
\qquad\chi=z-(2c_1I+C)e^{-2A}.
\]

The remaining bulk equations follow from the background identities. This is a reconstruction from the equations, not merely a check of one candidate profile.

For normal boundary displacements Zᵢ, the scalar and anisotropic Israel conditions become

\[
q_iD_i(z_i+Z_i)=0,\qquad\chi_i+Z_i=0.
\]

Since qᵢDᵢ≠0, the first pair gives zᵢ+Zᵢ=0. The second pair then gives C=0 and 2c₁Iᴸ+C=0. Positivity of Iᴸ forces c₁=0. The surviving scalar/longitudinal solutions are therefore diffeomorphisms accompanied by the corresponding embedding transformations.

## The candidate X₁ and its negative form

The historical candidate has c₁=1, C=z=0: F=−1, G=s=0 and χ=−2Ie⁻²ᴬ. It solves the bulk equations. At fixed boundaries, however, χ₀=0 while χᴸ=−2Iᴸe⁻²ᴬᴸ≠0. It violates the right anisotropic Israel condition. Its trace and double-divergence projections vanish because p²=0; those vanishing projections do not imply that the tensor condition holds. Moving the boundary to cancel this tensor residual instead violates qᴸDᴸZᴸ=0. The quadratic potentials therefore do not admit this proposed repair.

Nevertheless, the negative quadratic form can and should be reproduced. Define Ω(X*,X)=2iωZ and N=Z/2, with M̄²=BIᴸ. Direct covariant and canonical calculations give:

| Calculation | Bulk Z/(BIᴸ) | Corner Z/(BIᴸ) | Total Z/(BIᴸ) | N/M̄² |
|---|---:|---:|---:|---:|
| Covariant current and GHY corner | −2 | −4 | −6 | −3 |
| Time-ADM momenta and corner angle | 0 | −6 | −6 | −3 |

The covariant route varies Θ and the boundary correction C directly. The ADM route constructs the canonical momenta and retains the angle between the temporal slice and the timelike boundary. These corners matter because δg_ty≠0. Both routes reproduce **N[X₁]=−3BIᴸ**. Boundary-potential Hessians alter admissibility, but supply no independent temporal symplectic current in the fixed-boundary representative. The negative result is an off-domain evaluation of the extended quadratic form, not the norm of an admissible ghost.

## Edge completion and gauge quotient

Introduce boundary embeddings Xᵢ^A with δ_ξXᵢ^A=−ξᵢ^A. Their temporal, spatial longitudinal and normal components are defined without null-singular projectors. Pulling back the same action, including GHY and Uᵢ, yields dressed linear fields h̄=h+ℒ_Xg and s̄=s+X^yq. A combined transformation (ℒ_ξg,ξ^yq,−ξ) has vanishing dressed fields and therefore pairs to zero with every variation in the extended presymplectic form. This establishes the T,L,ζ gauge quotient, rather than checking only a direction’s self-norm.

In fixed-boundary coordinates the explicit mixed pairing is −3B[e²ᴬF_Yζ]₀ᴸ=0, since ζᵢ=0. Extensions of X agreeing at the boundaries differ by an admissible bulk gauge transformation. The two transverse graviton polarizations survive the quotient, each with Z=BIᴸ/2>0 when its polarization tensor has squared norm two. The massive representative likewise reproduces Z_f=2N_f>0.

The methodological identities concerning corners and embeddings follow [Harlow–Wu](https://arxiv.org/html/1906.08616) and [Speranza](https://arxiv.org/html/1706.05061). These references support the method; they are not evidence for the DDF-specific calculation reported here.

## Executed checks and qualified verdict

The replay includes 29 exact algebraic checks; nine fixed-action quadratic backgrounds at three resolutions, with 54 full Israel-tensor evaluations; and three integrations of the two norms at three resolutions. The latter simultaneously check X₁, a gauge representative and the graviton, with final normalized discrepancy at most 3.59×10⁻¹⁰. Independent current and ADM component checks additionally agree to floating-point precision. These numerical precisions describe computational checks, not physical accuracy or experimental confirmation.

**T1 = GREEN in the declared linear propagating domain.** The scalar null quotient is trivial, and the two physical massless graviton polarizations are positive. This verdict does not cover p^μ=0, q=0, Dᵢ=0, curved backgrounds, occupied matter with backreaction, additional boundary operators, nonlinear stability or quantum corrections. It neither closes DDF nor guarantees journal acceptance. Experimental multimode exclusion remains a separate calculation.

Detailed evidence: [qualified verdict](../../noyau/T1_Z_LIGHT/VERDICT_T1.md), [complete null kernel and junctions](../../noyau/T1_Z_LIGHT/DERIVATION_NOYAU_NUL_ET_BORDS.md), and [covariant/ADM currents, corners and quotient](../../noyau/T1_Z_LIGHT/PRESYMPLECTIQUE_ADM_ET_BORDS.md).
