# Symmetric games

Research by **Nicholas Ham** on symmetry, anonymity, player interchangeability
and fairness in finite strategic-form games. Principal starting source:
[Ham, arXiv:1311.4766v5 (2021)](https://arxiv.org/abs/1311.4766v5).

This repository contains an initial research manuscript and an audit programme.
It is not a completed paper or a claim of new results. The historical record,
classification examples and fairness interpretations remain under investigation.

## Build and experiments

Requirements: Python 3.10+ (standard library only), pdfLaTeX, BibTeX and latexmk
(e.g. TeX Live with latex-extra/science packages).

```sh
./scripts/build.sh
python3 -m unittest discover -s experiments
python3 experiments/constraint_audit.py --output experiments/results.json
```

The manuscript is `paper/main.tex`; the PDF is `paper/build/main.pdf`.
The build fails on unresolved references/citations and LaTeX errors. Source,
not build products, is tracked. To prepare an arXiv source bundle, include
main.tex, preamble.tex, sections/, references.bib and generated main.bbl;
compile the bundle in a clean directory before upload. No upload is authorized.

## Reading order

- [Roadmap](research/roadmap.md) and [handover](research/handover.md).
- [Complete numbered inventory](research/original-result-inventory.md): source statements, ambient assumptions and explicit dependencies; this is extraction, not verification.
- [Theorem audit](research/theorem-audit.md), [definition audit](research/definition-audit.md).
- [First mathematical investigation](research/dasgupta-maskin.md) and [reviews](reviews/review-log.md).
- [Source register](references/sources.md) and [historical evidence](research/historical-research.md).

Downloaded sources and raw revision responses live only in `.local/references/`,
which is ignored. Checksums and retrieval instructions are public. No third-party
PDFs are redistributed. Licensing remains reserved pending the author's choice;
see LICENSE. No journal submission, exhaustive priority claim or human sign-off
has occurred.
