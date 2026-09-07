# Rebuild the revised first manuscript

`manuscript.json` is the scientific content source. `build_manuscript.py` generates the Markdown, LaTeX and coefficient figure, then compiles the PDF with a local **pdfLaTeX or Tectonic** executable. The delivered revision was compiled with **Tectonic 0.17.0 (XeTeX)**. The builder runs three passes with pdfLaTeX, or automatic convergence reruns with Tectonic, and retains logs under `work/article_1_render/`. Tectonic may download its public TeX resources on first use; compilation is local and no online compiler receives the document.

```text
python publications/article_1/build_manuscript.py --output-dir work/article_1_rebuild --engine pdflatex
```

Use `--engine tectonic` for Tectonic, or supply an absolute executable path. The Python dependencies are listed in `requirements-article.txt`; the TeX source uses standard article, AMS, graphics, font and table packages. The bibliography is embedded in the TeX source, so no BibTeX invocation is necessary; `references.bib` remains available for journal-style adaptation. The minimal `article_1_sources.zip` contains the TeX source and its figure. It has not been tested on arXiv's compilation server.

The main PDF now includes the complete null-shell proof in Appendix B. The file `T1_SUPPLEMENT.md` points to that integrated text. The final compilation and visual-review record is stored under `verification/ARTICLE1_BUILD_REVIEW.json`. Local compilation is not a claim that an arXiv upload has been processed or accepted.

`inline_math.json` supplies reviewed mathematical typesetting for exact expressions in the prose. The builder applies it once, longest match first, without changing the scientific text or numbered equations. The generated Markdown preserves the original text; the TeX and PDF use these mathematical indices, radicals and exponents.
