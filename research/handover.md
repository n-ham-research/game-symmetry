# Initial research handover — 16 October 2026

Repository: https://github.com/n-ham-research/symmetric-games
Local working copy: `/home/nick/Repositories/n-ham-research/symmetric-games`.
Author: Nicholas Ham. Branch: `main`.

## Delivered

- Public repository under the requested organisation; local clone and origin configured.
- Six-page LaTeX research manuscript with introduction, conventions, symmetry/anonymity definitions, exact isomorphisms, known inverse-condition characterization, boundary examples and structured fairness questions. It is a foundation, not a finished publication.
- BibTeX bibliography, reproducible build, reference register, private ignored downloads and public source checksums.
- All **74 numbered environments**, including **41 formal results**, extracted from Ham v5 with source locations, ambient assumptions, exact statements and explicit references. Definitions/examples and formal results have separate audit tables. Hidden dependencies and complete prose/diagram coverage remain work in progress; the unnumbered-claims index records those limits.
- First mathematical audit: Ham v5 Theorem 3.21 and original proof checked; shorter proof and two-player/variable-common-payoff examples. No novelty claim. Three internal agent review records, plus a targeted follow-up.
- Exact standard-library Python tools for payoff equality partitions, player symmetries and full small-game automorphisms with strategy relabeling. Nine tests pass; nine finite-domain partition comparisons recorded in experiments/results.json.
- Historical work based on actual Wikipedia API revisions, the publicly located 2011-dated thesis, Vester's institutional report, Ham v1/v5 and a visually inspected third-edition von Neumann–Morgenstern scan.
- Roadmap, fairness notebook, conjecture/open-question registers, review protocol and actual AI contribution log.

## Principal findings

1. The D iff total symmetry plus identical-payoff-functions equivalence is already Ham v5 Theorem 3.21, with Vester's earlier public common-payoff proof. A shorter proof works without action-set finiteness; abstract extensions remain in research notes.
2. The 2011-dated thesis is available as arXiv:1905.00636v1 (posted 2019); §5.8 diagnoses the mismatch but does not prove the later common-payoff theorem. Wikipedia revisions confirm the May 4 correction and May 8 revert; anonymous-edit authorship remains a separately attributed claim.
3. In the 1953 third-edition text, §28.2.2 fairness concerns coalition values depending only on coalition size. Footnote 4 at pp.256–257 warns about index placement and composition. The scan's metadata incorrectly suggests 1944; no first-edition conclusion is drawn.
4. Proposition 2.2's non-surjectivity claim fails with singleton strategy-set degeneracies. Corollary 4.24 is false under its explicit automorphism-subgroup notation. The increasing-map subgroup assertion is false without surjectivity. Theorem 5.11's statement survives in finite games but its printed proof needs strategy maps and mixed values. Concrete evidence and candidate repairs are in audit-evidence.md.

## Validation

`./scripts/build.sh` succeeds with pdfLaTeX/BibTeX/latexmk, no unresolved citations/references and no overfull/underfull warnings in the final log. All six rendered pages were inspected. `python3 -m unittest discover -s experiments` passes nine tests. Full equality partitions, not just their class counts, are compared on nine domains. Downloaded copyrighted works are excluded from Git.

The built-in `open_in_codex` / `compile_latex_document` tools were not exposed in this session. Local TeX Live was used successfully; the source is saved at paper/main.tex and PDF at paper/build/main.pdf. The native editor was not opened. No local TeX installation or plugin installation was needed.

## Remaining uncertainty

- Original Dasgupta–Maskin scan is located but not successfully inspected; download returned 403. The effects on existence proofs remain an explicit hypothesis.
- Plan's linked author PDF is dated 2017; final 2023 journal body/version comparison is pending.
- The relevant 1944 edition pages are not yet inspected.
- Most source results, separating examples, diagram edges and hidden assumptions are still unverified. AI reports are internal criticism with shared context, not fully blinded external peer review.
- Journal/arXiv disclosure policies and the author's final licensing choice remain for a later submission/release stage. Current LICENSE reserves rights.

## Recommended next investigation

First repair Corollary 4.24 and fully audit the matching/strategy-triviality chain
(Theorem 4.23 and Corollaries 5.1–5.3). In parallel source work, obtain the
original 1986 pages and Plan's final article. The already checked inverse
condition provides a stable first result; the classification repairs and
Plan comparison should precede claims of new fairness equivalences.

No submission to arXiv or a journal has been made or authorized. Human author
review is pending. See Git history and the chat's final handover for publication
of this repository pass; repository publication is distinct from paper submission.
