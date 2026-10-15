# R-PH6-SHARP-A — independent sharp-ternary audit

16 October 2026. Reviewer: an additional OpenAI Codex agent instance, with the
same model family and inherited project history. Task supplied: reconstruct
P5-S4–S8, actively seek counterexamples, distinguish actual payoff groups from
arbitrary subgroups, and examine low-player completeness. The agent read the
repository instructions and Phase 5 proofs before reporting. This is internal
AI-assisted review, not external peer review or author sign-off.

**Verdict:** no defect found in the stated P5-S4–S8 proofs. The actual-group
hypothesis is essential. Standardness can be removed from the splitting
conclusion for `n>=5`. A short corollary of a directly checked classical Schur
multiplier theorem strengthens the conclusion: six is the **only** possible
player count for standard ternary nonsplitting, not merely the first.

The complete reconstruction, theorem, proof, source and explicit failed
strengthening are in [phase6-sharp-audit.md](../research/phase6-sharp-audit.md).
The imported group-theoretic step is the absence of three-torsion in the
Schur multiplier of `A_n`, `n>=8`; the game consequence remains candidate
work with priority unresolved.

Concrete adversarial counterexample: for even `n>=4`, the determinant-even
signed subgroup `D_n` of the ternary typed ambient group contains bare `A_n`
and projects onto `S_n`, but every lift of an `n`-cycle has order `2n`.
It is standard and nonsplit as a subgroup. An invariant game's additional
payoff automorphisms prevent it being the complete game group. This locates
the exact failure of the tempting arbitrary-subgroup generalization.

Checks actually run: `python3 experiments/phase5_six_independent.py` and
`python3 experiments/phase5_ternary_four_crosscheck.py` both passed. The
first independently reconstructs the binary six-player example; the second
checks 21 saved section witnesses and all 251 conjugacy keys, without
regenerating every lift-generated group in its default mode. No claim is made
that these are newly independent implementations written in Phase 6.

## Final manuscript integration pass

The reviewer subsequently read all active sections of the new symmetry
manuscript, including the explicit six-player section and the sharpness and
reduction section. No mathematical defect was identified. In particular:

- The six seed words, twelve kernel-rejection candidates, displayed typed
  generators and standard-subgroup generators agree with the inspected
  research proof. The perfect-even-preimage argument distinguishes absence
  of every section from absence of a matching section.
- The three-player manuscript's complete finite table was checked against an
  actual rerun of `python3 experiments/phase5_ternary_audit.py --verify`.
  It regenerated 216 fixed-player-image lifts, 32 classes, 11 subgroup
  classes and 19 embedded groups; every printed table entry matched.
- The strengthened only-six conclusion keeps actualness and the imported
  multiplier theorem explicit. The bibliographic metadata for that input
  matches the inspected institutional record and accepted author manuscript.
- The proof concerning common interest under fixed-action deletion applies
  to surviving players' retained utilities; it makes no interpersonal
  rescaling claim. Binary Example 5.13 is necessarily non-common-interest
  when its two majority utilities differ.

The reviewer also read the companion `game-fairness` manuscript's nine active
sections, read-only with explicit coordinating authorization. Its canonical
group normalizations, finite focal-fixed lemma, global-calibration
underidentification, focal Dirac-law tests, opponent-histogram comparisons,
and stated scope distinctions were checked. The explicit ordinal mixed-game
counterexample was recomputed: row indifference gives opponent probability
one half and column indifference gives two thirds, and swapping these fails.
No mathematical defect was found. This was a review of the migrated and
consolidated arguments, not an independent derivation of every historical
source or an external review of either paper.

One small source-integration improvement was reported to the coordinator:
add the existing Dasgupta--Maskin bibliography entry to the introduction's
sentence about their definition, alongside the thesis citation. Remaining
historical source-access limitations should continue to be stated explicitly.
Typography, rendered-page inspection, the complete offline package, build
and full-suite validation remain the coordinator's separate checks.
