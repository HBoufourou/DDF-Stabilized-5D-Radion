# Independent finite-element spectral cross-check

Date: 5 September 2026. Status: completed numerical verification of the specified classical model. This is a cross-check of the spectral calculation, not independent evidence for a physical fifth dimension, a UV completion, or the novelty of the model.

## Scope and method

The three lowest scalar modes were computed by a full-interval, continuous, piecewise-linear finite-element method. No shooting residual, parity-sector root bracket, or mass seed from the shooting table was used to locate these eigenvalues. The common input is the background solution, supplied by `calculs/model.py` at tolerance 2e-12. Thus the spectral discretization and eigenfunctions are independently computed; the background equations and background coefficient function are shared.

Using the conventions L=M5^3=1 and u=exp(2A)f, define

p=exp(-2A)/sigma'^2, w=exp(-4A)/sigma'^2, r=2 exp(-2A)/3.

The matrices discretize

K[u,v] = integral (p u'v'+r uv) dy,

H[u,v] = integral w uv dy + [w uv/W]_0^L,

where W=sigma''/sigma'. The spectral problem is K u = m^2 H u. Both endpoint contributions to H are positive in the symmetric backgrounds studied here. Omitting them would change the boundary conditions and the physical spectral problem.

Each element uses eight-point Gauss–Legendre quadrature. Meshes contain 64, 128, 256, 512, 1024, and 2048 elements. The three smallest generalized eigenvalues are obtained by a sparse shift-invert eigensolver. The canonical norm is evaluated through the proven relation N=(9/2)m^2 H[u,u], and the scalar exchange amplitude is alpha=I u(0)^2/N, where I=integral exp(2A)dy. The independently assembled K norm is retained as a residual diagnostic.

The recorded output is `resultats/fem_verification.json`. A new run writes `resultats/fem_verification_recalcule.json`, preserving the recorded results. References are loaded from `resultats/spectre_5d.json` and `resultats/extension_x.json`; the latter contains the extension data originally computed as `extension_x_recalcule.json`.

## Main benchmark: x=2, epsilon=0.53

All three scalar masses and couplings display second-order mesh convergence. The observed orders on the last three meshes are 1.99998–2.00008 for masses and 1.99998–2.00001 for couplings. This is the expected behavior of the P1 approximation for these smooth modes.

| Mode | mL at 2048 elements | alpha at 2048 elements | Richardson mL | Richardson alpha |
|---:|---:|---:|---:|---:|
| 0, even | 0.850123909161 | 0.402266512079 | 0.850123904525 | 0.402266532328 |
| 1, odd | 2.652137080360 | 0.091572146350 | 2.652137036020 | 0.091572159743 |
| 2, even | 4.330346073195 | 0.025640266463 | 4.330345364060 | 0.025640278703 |

Richardson values use (4 Q_2048-Q_1024)/3. For this benchmark, the measured convergence order supports cancelling the leading quadratic mesh error in this way.

Relative to the high-accuracy shooting reference, the largest discrepancies among the three raw 2048-element results are 1.64e-7 for mL and 4.78e-7 for alpha. After Richardson extrapolation, the largest discrepancies are 5.70e-12 for mL and 9.07e-12 for alpha. These discrepancies are numerical comparisons, not rigorous interval error bounds or physical uncertainties. The extra digits in this report are diagnostic; the manuscript should use fewer significant digits.

The agreement includes the ordering and reflection parity of the first three modes. In particular, it independently confirms that the mode with mL approximately 2.65214 is present between the radion and the scalar mode near 4.33035, and that its coupling is nonzero.

## Additional checks

The same procedure was run at x=1 and x=3, for epsilon=0.05 and epsilon=0.4. The following table gives the largest absolute relative discrepancy of the three raw 2048-element modes against their recorded shooting references.

| x | epsilon | Maximum discrepancy in mL | Maximum discrepancy in alpha |
|---:|---:|---:|---:|
| 1 | 0.05 | 1.10e-7 | 2.39e-7 |
| 1 | 0.40 | 1.19e-7 | 2.76e-7 |
| 3 | 0.05 | 2.23e-7 | 6.85e-7 |
| 3 | 0.40 | 2.29e-7 | 7.36e-7 |

At epsilon=0.4, both x values exhibit approximately quadratic convergence for all three masses and couplings on the finest meshes. At epsilon=0.05, the two higher modes retain this behavior, while the very light radion reaches a numerical plateau before the final mesh.

For the light radion at x=1, epsilon=0.05, the final raw discrepancies are approximately 7.6e-10 in mass and 1.3e-9 in alpha. For x=3, epsilon=0.05 they are approximately 2.9e-9 and 5.1e-9. The last-three-mesh convergence orders cease to be two; some are negative. The shrinking discretization error is then comparable to cancellation and roundoff effects in the matrix computation. A negative observed order at this plateau is not evidence for a physical unstable mode, but it does mean that a second-order Richardson error estimate is unjustified there.

The JSON records the formal extrapolations for transparency. They must not be interpreted as validated improved estimates for these two weak-backreaction radions. The raw agreement and the mesh plateau provide the relevant numerical evidence. The binary numerical acceptance flag uses the explicitly declared comparison tolerances; it does not certify second-order convergence or establish a stability theorem.

## Interpretation and limitations

The check supports the implementation of the lowest three masses and brane couplings at five sampled points, using a genuinely different spectral method. The positive continuum forms K and H provide the analytical stability argument; agreement between finite-element and shooting values is a numerical validation of their implementation.

It does not validate all higher modes, all possible parameter values, nonlinear stability, the action's radiative stability, an experimental exclusion, or a predicted compactification radius. Shared errors in the background equations would not be exposed by this spectral comparison. Those questions are separated in the scientific audit.

## Reproduction

Install the packages in `calculs/requirements.txt`, then run from the repository root:

```text
python calculs/fem_verify.py
```

This reproduces the main x=2, epsilon=0.53 check. To include all five cases:

```text
python calculs/fem_verify.py --extended
```

The reference results are retained. Matrix residuals, convergence orders, raw comparisons, and formal Richardson values are all written to the new result file for inspection.
