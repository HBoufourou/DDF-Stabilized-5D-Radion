# General weak-backreaction coefficients and scalar stability

Original calculations for the proposed first article, 2026-09-05. No priority claim is implied. The formulas below extend the previous x=2 calculation and are independently checked by quadrature in `weak_backreaction_general.py`.

## Scope and definitions

The action is the physical-interval action with gravitational coefficient M5^3/2, canonical bulk scalar, V=Lambda5+mu^2 sigma^2/2, GHY term, and linear brane potentials U_i=T_i+J_i sigma. There are no brane kinetic terms, induced Einstein terms, extra bulk fields, or direct sigma couplings to source matter. For the reflection-symmetric branch, sigma is odd about the midpoint, A is even, sigma'>0, and A'=sigma=0 at the midpoint. Matter lives on either boundary, normalized by A_b=0. The finite-backreaction backgrounds reconstruct Lambda5 and brane tensions as the shooting parameters change; they are a family of actions/backgrounds, not variations of L with every action parameter held fixed.

For the perturbative derivation only, set L=M5^3=1, t=y-1/2 in [-1/2,1/2], x=mu L>0, epsilon=qL/sqrt(12M5^3), q=sigma'(boundary)>0. All statements at small epsilon hold at fixed x>0.

Define C=cosh^2(x/2), T=tanh(x/2), and the full-interval average <h>=integral from -1/2 to 1/2 of h(t) dt.

## Background and light-mode expansion

Write sigma'=epsilon v1+O(epsilon^3), A=epsilon^2 a2+O(epsilon^4). Then

    v1(t) = sqrt(12) cosh(xt)/sqrt(C),
    a2''(t) = -4 cosh^2(xt)/C,
    a2'(t) = -[2t+sinh(2xt)/x]/C.

The additive constant in a2 fixes A_b=0 and cancels from the coupling coefficient.

For the even light mode let f=1+epsilon^2 f2+O(epsilon^4), with f2(0)=0, and m_r^2 L^2=kappa epsilon^2+O(epsilon^4). The metric/scalar constraint gives s=-3 epsilon b/v1+O(epsilon^3), where b=f2'+2a2'. The regular fluctuation equation and its linear-brane boundary condition give

    b' - 2x tanh(xt) b = 8 cosh^2(xt)/C - kappa,
    b(0)=0,
    x T b(1/2)=kappa.

The first two imply

    b(t)=8t cosh^2(xt)/C - kappa sinh(2xt)/(2x).

Using 1+T sinh(x)/2=C in the last condition yields the closed result

    kappa(x)=4x tanh(x/2) sech^2(x/2).

Integration of f2'=b-2a2' yields

    f2(t)=[4t^2+2t sinh(2xt)/x]/C
          -kappa[cosh(2xt)-1]/(4x^2).

This light root is the continuation of the flat gravitational radion at fixed x>0. The limit epsilon=0 must be taken after this regular expansion: the sigma'-based exact variable is undefined if sigma' is identically zero.

## Canonical coupling and exact perturbative simplification

The mode kinetic coefficient is Z=2N, with

    N=integral e^(2A)[3M5^3 f^2+s^2/2]dy,
    Mbar_Pl^2=M5^3 integral e^(2A)dy,
    alpha=Mbar_Pl^2 f_b^2/N.

The last quantity is relative to the massless tensor Newton potential for minimal matter on the same brane. Expansion gives

    alpha_r=(1/3)[1+c_alpha epsilon^2+O(epsilon^4)],
    c_alpha=2[f2(1/2)-<f2>] - <s1^2>/6,
    s1=-3b/v1.

The required elementary integrals reduce to

    f2(1/2)=(1+2T/x)/C,
    <f2>=[1/3+1/x^2-sinh(x)/x^3+T/x]/C,
    <s1^2>=(12/C)[1/6-T^2/2-1/x^2+sinh(x)/x^3].

Substitution cancels all sinh(x)/x^3 and 1/x^2 terms, giving

    c_alpha(x)=sech^2(x/2)[1+tanh^2(x/2)+2tanh(x/2)/x].

Therefore kappa(x)>0 and c_alpha(x)>0 for every fixed x>0. In this precisely specified branch, switching on sufficiently weak stabilization increases both the squared radion mass and its brane Yukawa amplitude above its flat limit 1/3. This is a perturbative sign theorem; it is not a theorem of global monotonicity at finite epsilon, and not a statement about arbitrary stabilizing potentials or brane terms.

Eliminating epsilon gives the useful local mass-coupling relation

    3 alpha_r - 1 = D(x) (m_r L)^2 + O(epsilon^4),
    D(x)=c_alpha/kappa
        =[1+T^2+2T/x]/(4xT)>0.

The notation O((m_r L)^4) is equivalent only at fixed x with nonzero kappa. Do not use a uniform expansion as x tends to zero or infinity without controlling the remainders. Formally kappa~2x^2 and c_alpha~2 as x->0+, while kappa~16x exp(-x) and c_alpha~8(1+1/x)exp(-x) as x->infinity. Both endpoint limits are degenerate and are not covered by the fixed-x stability proof at q=0.

## Independent effective-potential check of the light mass

At leading weak backreaction, solve the scalar equation on a flat physical interval while holding the action parameters mu, q, Lambda5 and T_i fixed:

    sigma_L(y)=q sinh[mu(y-L/2)]/[mu cosh(mu L/2)],
    J_0=q, J_L=-q.

On the scalar solution, integration by parts reduces its bulk energy to one half of [sigma sigma']_0^L. Adding both linear brane source terms yields -q^2 tanh(mu L/2)/mu. The four-dimensional Jordan-frame potential is therefore

    V_J(L)=Lambda5 L+T_0+T_L-(q^2/mu)tanh(mu L/2),

up to higher gravitational-backreaction terms. At a Minkowski extremum, V_J=V_J'=0, so

    Lambda5=q^2 sech^2(x/2)/2,
    V_J''=q^2 mu tanh(x/2)sech^2(x/2)/2>0.

The Weyl factor from Jordan to Einstein frame contributes no extra second derivative at this tuned extremum because V_J and V_J' vanish. With the flat radion canonical field sqrt(3/2) Mbar_Pl ln(L/L_*), the mass is

    m_r^2=(2L^2/(3Mbar_Pl^2))V_J''
         =kappa(x) epsilon^2/L^2.

This independent computation checks kappa without the coupled spectral equations. The leading conditional radius selection is

    L=(2/mu) arcosh[q/sqrt(2Lambda5)],

provided 0<2Lambda5<q^2 and the tension sum is tuned to V_J=0. This expresses stabilization given independently specified dimensionful parameters. It is not an absolute prediction of L: neither mu nor q/sqrt(2Lambda5) has been derived from the proposed DDF geometry. The relation is leading order in backreaction and cannot replace the exact numerical background at finite epsilon.

## Exact scalar spectral stability on every regular branch point

This section restores dimensions and does not use a small-backreaction expansion. Assume a smooth background on [0,L] with sigma'>0 and finite fields, mu>0, q>0, the stated reflection symmetry and linear brane potentials. The regular scalar equation is

    f''+(2A'-2W)f'+[4A''-4A'W+m^2 e^(-2A)]f=0,
    W=sigma''/sigma',
    W_i(f'_i+2A'_i f_i)-m^2 e^(-2A_i)f_i=0.

It makes no division by A', so the midpoint A'=0 is harmless. It requires sigma' nonzero. Set

    g=e^(2A)f,
    p=e^(-2A)/sigma'^2>0,
    w=e^(-4A)/sigma'^2>0,
    Q=-2A''p=2e^(-2A)/(3M5^3)>0.

Direct substitution gives the regular generalized Sturm-Liouville problem

    -(p g')'+Q g=m^2 w g,
    g'_i=m^2 e^(-2A_i)g_i/W_i.

The background equations imply on the right half that A'<0, sigma>0 and sigma'>0. Thus W=mu^2 sigma/sigma'-4A'>0 away from the midpoint. Reflection gives W_L>0 and W_0<0, so the endpoint denominators are well defined.

Multiply by g* and integrate. The endpoint condition gives the exact identity

    integral[p |g'|^2+Q|g|^2]dy
      = m^2 {integral w|g|^2 dy
               +(w_L/W_L)|g_L|^2-(w_0/W_0)|g_0|^2}.

Both braces and the left-hand side are strictly positive for every nontrivial mode. It follows directly that m^2 is real and strictly positive. In particular this proves absence of scalar tachyons and of a scalar zero eigenfunction in this regular problem; a positive-root numerical scan is not the proof. Eigenvalue-dependent boundary conditions must be kept in the denominator: omitting those boundary terms changes the spectral problem. This argument holds for every regular finite-backreaction point satisfying the stated assumptions, with no weak-epsilon approximation.

It does not assert a uniform positive gap over all action parameters. It does not address nonlinear evolution, additional fields, parameter variations not obeying fixed-action boundary conditions, or singular/degenerate branches. The epsilon=0 limit needs its own variables and contains the massless radion.

The boundary condition follows directly from the scalar junction rather than from any division by m^2. In the fixed-boundary gauge, the perturbed normal derivative for U_i''=0 gives s'+2sigma' f=0. Writing B=f'+2A'f, the bulk equation implies B'=2WB-2A''f-m^2e^(-2A)f. Substitution of s=-3M5^3 B/sigma' and A''=-sigma'^2/(3M5^3) gives precisely WB-m^2e^(-2A)f=0. Thus neither the midpoint nor a putative zero mass has been divided out in obtaining the displayed BVP.

The no-ghost statement follows separately from the canonical kinetic norm N>0. As a consistency identity, using the constraint s=-3M5^3 e^(-2A)g'/sigma' gives

    N=(9 M5^6/2) integral[p g'^2+Q g^2]dy
     =(9 M5^6/2) m^2 D_SL,

where M5^6 means (M5^3)^2 and D_SL is the positive brace in the preceding equation. D_SL is the generalized Sturm-Liouville norm and must not be identified with N without this factor and eigenvalue.

For propagating four-dimensional scalar modes, the momentum constraint is applicable also when m^2=0 (a null four-momentum is not the zero four-momentum). Purely static parameter changes are a different question and are not counted as propagating normal modes. No hidden scalar fields have been included in the action. A manuscript should display the constraint and derivation of the regular BVP to make the completeness of this variable in the single-scalar sector explicit.

## Tensor sector

With Neumann branes the tensor equation is

    -(e^(4A)h')'=m_T^2 e^(2A)h,
    h'(0)=h'(L)=0.

Integration gives m_T^2 integral e^(2A)|h|^2=integral e^(4A)|h'|^2>=0. The only zero mode is constant on the connected interval. Every nonconstant tensor mode has positive m_T^2. Together with the scalar proof this is linear spectral stability of the included scalar and transverse tensor sectors, under the assumed action and boundary conditions.

## Presentation limits

These are conditional predictions of an explicit five-dimensional effective model. They do not select an absolute L or a micrometric radius, do not derive the action from DDF geometry, and do not establish experimental agreement. The sign formula may be a useful analytical result, but a bibliographic priority analysis must precede any novelty claim. The earlier x=2 coefficient is recovered exactly, c_alpha(2)=0.983420239838..., kappa(2)=2.558800033797....
