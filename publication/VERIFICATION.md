# Verification record — 20 October 2026

The final symmetry-first draft has 15 pages. `bash scripts/build.sh`
passes with TeX Live 2025; the final log has no undefined references/citations
or overfull/underfull boxes. All 36 labelled LaTeX destinations resolve
on their expected PDF pages. The PDF contains 80 link annotations and
61 checked internal links; external URL syntax/destinations were checked,
not universal HTTP availability. See pdf-audit.json and BIBLIOGRAPHY-AUDIT.md.

All 88 unittest cases pass. `python3 scripts/audit.py check` passes with five
pinned files preserved and the pre-existing unresolved original Cor4.10 record
retained. It is not a prerequisite of the present manuscript.

A fresh working-source checkout at /tmp/symmetry-clean-check-bf7zgpac, containing
Git-tracked plus current nonignored source files but no ignored downloads,
build files or pre-existing ZIP, independently passed unittest discovery,
source audit and manuscript build. This was a clean source copy, not a claim
that uncommitted changes were already present in a remote clone.

The self-contained source bundle was compiled twice using supplied main.bbl
and `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex`.
The ancillary ternary verification regenerated 216 lifts, 32 representatives
and 11 group classes; the independent six-player crosscheck confirmed group
order2160, image720, kernel3, standard subgroup60 and perfect even preimage1080.
These are finite certificates, not an enumeration proof for unrestricted games.

All 15 actual pages were rendered with Poppler and visually inspected.
Representative individual pages were also examined at larger resolution:
title, indexing proof, fairness propositions, six-player witness and bibliography.
After final citation/spacing changes all pages were rerendered and inspected.
The statement of the calibration proposition is kept together. No clipping,
missing glyphs, unreadable tables or unresolved reference markers were found.
The East–Ham benchmark was an actual rendered v3 PDF, not an inferred style.

Final PDF SHA-256: `2cc926ce36a536737bcd0ee87223d52a42481044095c227ec62a818d62f5c448`.
Source archive SHA-256: `ab117e68403bc7ad37e5885cce75cd202aa160baa464e8c3127f643ef6907a9f`.

No external human review, author approval, remote arXiv compilation or submission
is asserted. Metadata retains Nicholas Ham; no affiliation was invented.
