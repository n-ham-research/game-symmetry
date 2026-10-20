# First-priority human-review packet — 20 October 2026

**Proposed title:** *Symmetry and Player Interchangeability in Finite Games*.
**Author:** Nicholas Ham. **Recommendation:** focused symmetry paper with a short
section of closely related fairness consequences; retain the broader fairness
manuscript separately. This is a human-review draft, not submission approval.

## Precise results and hypotheses

1. **Theorem 2.1, established Vester/Ham result.** With a common nonempty action
   set, all player permutations quantified, and at least three players, pairing
   the recipient p(i) with forward profile indices is equivalent to correctly
   indexed symmetry together with identical payoff functions. The proof, converse,
   two-player boundary, distinguishing examples and zero-sum consequence are
   included. The assertion concerns the explicit displayed formula; it does not
   invalidate uninspected equilibrium-existence arguments.
2. **Theorem 6.2, candidate structural extension.** For standard three-player,
   three-strategy games with full player image, coherent lifts exist; the
   non-full complete groups have the stated order-six/order-eighteen forms.
   The complete game group, rather than an arbitrarily chosen subgroup, matters.
3. **Theorem 7.1, candidate structural extension.** For complete exact groups of
   ternary n-player games with full player image, the projection splits if
   n>=3, 3 does not divide n and standardness holds; it also splits for n>=5,
   n!=6 without standardness. Together with the three-player case, six is the
   only possible player count for standard ternary nonsplitting.
4. **Theorem 8.1, attaining construction.** A six-player, three-strategy game
   with common binary-valued payoffs has complete group of order 2160, full
   player image, kernel C3 and standardness, but no section or full matching.
   Finite group closure/perfectness certificates are explicitly identified.

The binary benchmark is Ham's existing Example 5.13/Figure 4 classification,
not a new classification. The short assignment-calibration and invariant-CE
arguments are elementary/standard consequences, not new general fairness
theorems. No unresolved general fairness question is a dependency.

## Novelty and attribution

The indexing correction is already public: Vester (2012), Ham (2013, revised
2021), and related treatment by Tohmé–Viglizzo. The 2011 thesis date must not be
used as the date of a public common-payoff proof. The current draft gives a
self-contained synthesis under Ham's name with explicit attribution.
New-priority claims must concern the exact payoff-realizable structural
classification and sharp boundary, subject to further specialist comparison.
The covering method, triple cover, degree-18 action and multiplier input are
credited literature. Internal review cannot establish exhaustive originality.

## Verification and presentation

- Complete mathematical arguments reviewed in MATHEMATICAL-REVIEW.md; no
  theorem-level defect found. This is shared-context internal AI review, not
  external peer review or author approval.
- Separate publication review: PUBLICATION-REVIEW.md; presentation approved for human review.
- Existing 88 tests pass; pinned-source audit checks all five files and retains
  the pre-existing unresolved Corollary 4.10 record, which is not a premise here.
- LaTeX builds with TeX Live 2025; semantic references, bibliography links,
  captions, metadata and restrained article formatting implemented.
- Actual rendered pages inspected, using the East–Ham v3 PDF as presentation
  benchmark. Machine destination checks are recorded in pdf-audit.json.
- Self-contained source archive includes main.bbl and the finite certificate
  scripts/data. Clean compilation and certificate verification are recorded
  separately in VERIFICATION.md. HTTP availability is not inferred from a
  syntactically valid hyperlink.

## Outstanding human decisions / blockers to submission

1. Nicholas Ham must approve the exact statements, proofs, attribution, author
   details and actual AI-assistance disclosure.
2. Decide whether this synthesis and structural extension should be a new
   submission or a revision of arXiv:1311.4766; explicitly disclose overlap.
   The known indexing theorem alone cannot support a new discovery claim.
3. Original Dasgupta–Maskin Definition 7 has not been directly visually checked
   in this campaign. Attribution is expressly through inspected primary
   discussions. Obtain the original if stronger source-level accusations are
   intended; no such accusation is required for the explicit-formula theorem.
4. Specialist comparison of the game-realizable classifications against
   code/design/group-action literature remains advisable before strong novelty
   claims. No external expert has reviewed this packet.

**Classification:** ready for final human mathematical/editorial review;
not cleared for arXiv submission. No unresolved fairness research blocks this
review. Agent Games is second priority; its editorial/readiness work proceeds
after this packet. The general fairness manuscript remains separate.

## Deliverables

- `output/pdf/game-symmetry.pdf` — review PDF.
- `output/pdf/game-symmetry-source.tar.gz` — self-contained source and ancillary
  finite certificates, with SHA-256 manifest.
- `paper/main.tex` — maintained editable source; build with `bash scripts/build.sh`.

No submission, repository visibility change or journal contact was made.

## Consolidated campaign disposition

| Manuscript | Current status | Publication priority |
|---|---|---|
| Symmetry and Player Interchangeability in Finite Games | 15-page focused paper, proofs and presentation internally reviewed; clean build, 88 tests, source audit and certificates pass. Ready for final human review, with originality/overlap/author decisions above. | First |
| Information, Incentives and Symmetric Equilibria in Finite Coordination Games | 11-page Agent Games draft polished and sequentially reviewed; 244 tests, three frozen imports, clean build and source-bundle compile pass. Binary query prior-domain omission repaired and reviewed. Human originality/narrative scope decision remains before submission. | Second |
| Game Fairness | Broader standalone manuscript retained; limited proved calibration/recommendation consequences integrated into the first paper. General fairness remains unresolved, and substantive standalone significance needs further assessment. No claim of a new full publication-polish review of that whole manuscript. | Separate, does not delay symmetry |

The Agent Games review packet is maintained in `../agent-games/publication/`.
These are existing manuscripts; no extra papers were created from later notes.
Both polished PDFs are review artifacts, not submission clearance. The existing
private repositories retain their visibility; only authorized source commits
are pushed. Generated artifacts stay local and are rebuildable from source.
