# Dark Dimension Framework — Corrected Geometry and Spectral Program

> **Research-development repository — not a peer-reviewed theory release.**

This repository supersedes the scientific claims of the initial
**DDF Articles I–VIII** series while preserving that series as a historical
archive. It contains the corrected DDF research program after the R1–R65
adversarial audit.

## What DDF means now

DDF is no longer presented as one established theory deriving an
\(8.2\,\mu\mathrm m\) bulk, a physical KK tower, dark matter, dark energy and a
Fano-plane charge structure at once. It is a staged research program with
three independent branches:

| Branch | Scientific object | Current status |
|---|---|---|
| **DDF-G** | resolved Tyurin degeneration, K3 seam, restriction lattice and LMHS | strongest surviving core; R63 passed |
| **DDF-KK** | neutral metric/gravitation KK spectrum of a finite neck | diagnostic pipeline passed R65; real DDF geometry untested |
| **DDF-BPS** | possible BPS tower in the parent \(\mathcal N=2\) theory | conditional; standard closed-\(C_4\) descent is obstructed under R64 hypotheses |

The Fano plane, dark-matter, dark-energy, baryogenesis and micron-scale claims
remain deferred unless later rounds derive their missing geometric and
physical maps.

## Results retained

- **R63:** a strict, reproducible Tyurin geometry package for the resolved
  POLY944/sigma5 construction, with explicit scope conditions.
- **R64:** a rational conditional parity–Hodge proposition for active closed
  \(C_4\) eigen-tubes; no broad orientifold no-go or standalone paper claim.
- **R65:** a preregistered scalar spectral pipeline that recognizes three 1D
  controls and rejects transverse and Cheeger/tunneling false positives.

These results do **not** yet derive \(R(t)\), a micron value, a spin-2 KK
spectrum, a globally consistent orientifold vacuum or a stable tower.

## Publication tracks replacing Articles I–VIII

The eight initial papers are not replaced one-for-one. They are consolidated
into three stricter tracks:

1. [`article-G-geometry`](articles/article-G-geometry/README.md) — candidate
   geometry paper; substantial but still blocked by explicit completion gates.
2. [`article-KK-spectral`](articles/article-KK-spectral/README.md) — future
   finite-neck spectral paper; blocked until R66 tests one real geometry.
3. [`article-physics`](articles/article-physics/README.md) — possible physical
   compactification/stabilisation paper; blocked until R67–R70.

No folder is labelled “publishable” until its checklist is closed and two
independent expert readings have been recorded.

## Repository map

| Path | Purpose |
|---|---|
| `docs/SCIENTIFIC_STATUS.md` | authoritative status of every surviving branch |
| `docs/LEGACY_DEPRECATION_MAP.md` | disposition of old Articles I–VIII |
| `docs/PUBLICATION_PLAN.md` | three-paper plan and binary submission gates |
| `docs/CLAIM_POLICY.md` | allowed and forbidden formulations |
| `docs/ROADMAP_R66_R70.md` | next falsifiable rounds |
| `reproducibility/R65/` | cumulative runnable R61–R65 release |
| `legacy/` | R1–R62 master audit and historical-package pointer |
| `releases/` | signed ZIP releases R63–R65 |
| `software/` | current spectral pilot entry point and configuration |

## Reproduce the current release

~~~bash
cd reproducibility/R65
python3 r65_release_gate.py
~~~

Expected terminal verdict:

~~~text
R65_SPECTRAL_PIPELINE: GO
R66: AUTHORIZED_AFTER_SINGLE_PLATFORM_LOCK
DDF_METRIC_SPIN2_R_MICRONS_FANO: NOT_DERIVED
~~~

## Historical repository

The original series remains accessible for traceability at
[HBoufourou/DDF_I-VIII_2026-08-29](https://github.com/HBoufourou/DDF_I-VIII_2026-08-29).
It must be read as a deprecated historical archive, not as the current status
of DDF.

## Author and responsibility

Hicham Boufourou — Independent Researcher, Belgium. General-purpose AI systems
were used as computational and analytical assistants. The author remains
responsible for every hypothesis, calculation, interpretation and release.


