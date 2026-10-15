# Symmetric games

Research by **Nicholas Ham** on symmetry, anonymity, player interchangeability
and fairness in finite strategic-form games. Principal starting source:
[Ham, arXiv:1311.4766v5 (2021)](https://arxiv.org/abs/1311.4766v5).

This repository contains a conservative research manuscript, an adversarial audit,
and new mathematical investigations of player symmetry.
It is not a completed paper or a claim of new results. Historical source gaps and fairness interpretations remain under investigation.
The second pass accounts for all 41 formal results: 33 unchanged valid statements,
7 corrected/clarified formulations and 1 unresolved original ambiguity. The source
verdict and corrected-result verdict are kept separate; see the audit ledger.

Phase 3 supplies complete internal proofs of a nonsplitting counterexample and a
binary exact-potential theorem. Novelty and external mathematical review remain
outstanding; see the [Phase 3 handover](research/handover-phase-3.md).

## Build and experiments

Requirements: Python 3.10+ (standard library only), pdfLaTeX, BibTeX and latexmk
(e.g. TeX Live with latex-extra/science packages).

```sh
./scripts/build.sh
python3 scripts/audit.py check
python3 -m unittest discover -s experiments
python3 experiments/constraint_audit.py --output experiments/results.json
```

The manuscript is `paper/main.tex`; the PDF is `paper/build/main.pdf`.
The build fails on unresolved references/citations and LaTeX errors. Source,
not build products, is tracked. To prepare an arXiv source bundle, include
main.tex, preamble.tex, sections/, references.bib and generated main.bbl;
compile the bundle in a clean directory before upload. No upload is authorized.

## Reading order

- [Phase 4 handover](research/handover-phase-4.md): adversarial binary verification, the ternary splitting boundary, two ternary mechanisms, and precise reduction comparisons.

- [Utility invariance and fairness handover](research/fairness-programme-handover.md), [automorphism hierarchy](research/utility-invariance.md), and [assignment models](research/assignment-and-solution-rules.md).

- [Phase 3 results and dependencies](research/phase3-results.md), [splitting proof](research/phase3-splitting-proof.md), and [binary equilibrium theorem](research/phase3-equilibria.md).
- [Assignment/fairness experiments](research/phase3-fairness.md) and [publication outline](research/phase3-publication-outline.md).

- [Roadmap](research/roadmap.md) and [handover](research/handover.md).
- [Second-pass handover](research/handover-pass-2.md), [correction ledger](research/corrections.md), and [dependency graph](research/dependencies.md).
- [Complete numbered inventory](research/original-result-inventory.md): source statements, ambient assumptions and explicit dependencies; this is extraction, not verification.
- [Theorem audit](research/theorem-audit.md), [definition audit](research/definition-audit.md).
- [First mathematical investigation](research/dasgupta-maskin.md) and [reviews](reviews/review-log.md).
- [Source register](references/sources.md) and [historical evidence](research/historical-research.md).

Downloaded sources and raw revision responses live only in `.local/references/`,
which is ignored. Checksums and retrieval instructions are public. No third-party
PDFs are redistributed. Licensing remains reserved pending the author's choice;
see LICENSE. No journal submission, exhaustive priority claim or human sign-off
has occurred.
