# Research instructions

Author: Nicholas Ham. This is a mathematical research project, not a rewrite.

- Read research/roadmap.md, research/theorem-audit.md and reviews/review-log.md before research changes.
- Fix the permutation convention before any argument: (P_pi s)_j=s_{pi^{-1}(j)}; compose right to left.
- Label every result as literature, previously established by Ham, candidate extension, conjecture, disproved conjecture, or open question. Independent rediscovery is not evidence of novelty.
- Keep candidates in research/ until a complete proof, source comparison and adversarial review exist. Never silently promote conjectures to manuscript theorems.
- Inventory and cite actual identifiers and source versions. Document assumptions, dependencies, boundary cases and evidence for each status change.
- Use exact arithmetic. Finite checks can refute a universal statement but do not prove it generally.
- For major results use three initially separate agent reviews where practical: inference checking, counterexamples, strengthening. Record supplied context, shared-model limitations, disagreements, and actual findings. Agreement is not proof or external peer review.
- Do not invent primary-source access, historical priority, thesis contents, credentials, human review, or AI models used.
- Do not copy third-party PDFs into Git; use the ignored .local/references cache. Check licensing before any redistribution.
- Manuscript author is Nicholas Ham; log actual AI assistance without attributing unperformed author review.
- Run scripts/build.sh and python3 -m unittest discover -s experiments before pushing relevant changes. Inspect rendered pages after manuscript layout edits.
- Do not submit to arXiv or any journal without explicit author approval. Recheck applicable disclosure policies at submission time.
