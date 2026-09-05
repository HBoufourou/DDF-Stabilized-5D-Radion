# Manuscript sources and reproduction

The delivered manuscript is an 11-page research draft with 40 displayed equations,
four tables, one two-panel scientific figure, and 12 primary references.

`manuscript.json` is the structured text source. `manuscript.md` allows reading on
GitHub. `manuscript.tex` contains the same text, equations, tables and figure in
editable LaTeX. `references.bib` is also supplied for subsequent journal styles;
the present TeX source uses a self-contained bibliography.

The delivered PDF was composed with ReportLab and equations rendered by Matplotlib
mathtext at 320 dpi; figure data come from the analytic formulas and recorded
spectral results. Equation (8) expands the flat four-dimensional Box symbol as
partial_mu partial^mu in the PDF, with identical meaning. No LaTeX engine was
available for a separate TeX compilation in this run.

From the repository root, install `calculs/requirements-manuscript.txt`, then run:

```text
python calculs/render_manuscript.py
```

Rendering intermediates go to `article/qa/`, ignored by Git. The script regenerates
the PDF and figures. The TeX source is prepared for pdfLaTeX; run from `article/`
if using that route. Layout may differ from the supplied PDF.

All 11 pages of the supplied PDF were visually inspected after Poppler rendering.
Equations, page numbering and table layouts were checked; this visual inspection
does not replace scientific review. Rebuilding files changes their integrity
hashes and requires a new manifest for a new release.
