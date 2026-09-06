# Rebuild the first manuscript

`manuscript.json` is the single authoritative content source. The build script reads it and produces `manuscript.md`, `manuscript.tex`, the two figure formats and `manuscript.pdf`. Numerical table values are frozen in the structured source and verified against their referenced JSON data by the package checker.

From the repository root, in a Python environment with `requirements-article.txt` installed:

```text
python publications/article_1/build_manuscript.py --output-dir work/article_1_rebuild
```

The PDF uses ReportLab with mathematical equations rendered by Matplotlib. Scratch equation images and layout reports stay under `work/`. The delivered PDF was rendered and visually inspected. It is not claimed to be a TeX-engine build.

The editable TeX uses LuaLaTeX or XeLaTeX, `fontspec`, DejaVu Serif, standard AMS packages and the included PNG figure. The TeX source is supplied for adaptation to a journal style; no TeX engine was installed for a separate compilation in this run. The standalone bibliography in TeX and the BibTeX file both contain the verified references; adapting the citation style does not change their scope.

The paper concerns the quadratic Einstein–scalar core; the affine case is an identified comparison. This directory contains the current manuscript. The previous affine manuscript and earlier complete editions are preserved in local backups outside the published tree. Read `audits/REPONSE_AVIS_ARTICLE1.md` from the repository root for the applied scientific corrections.

## Separate T1 supplement

[T1_SUPPLEMENT.md](T1_SUPPLEMENT.md) supplies the new null-shell analysis and links to the full derivations and executable replay. It is an additional authoritative document for that analysis. The main manuscript JSON, MD, TeX, figures and PDF are unchanged by this supplement; rebuilding the main manuscript does not incorporate it. Read and circulate the manuscript together with this supplement until an explicitly integrated manuscript edition is prepared.
