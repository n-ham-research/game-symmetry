# Phase 5 splitting investigator: results and cross-review

This agent was assigned the principal four-player ternary splitting question,
with the shared conversation and repository. It read AGENTS.md, roadmap,
theorem-audit and review-log before edits. It was not a blinded reviewer of
its own results and is not a different-model or external peer reviewer.

## Original investigation

- Derived a local-sign quotient reduction separating the binary signed-
  permutation group from modular translation kernels over F3.
- Exhaustively verified the regular-C4 four-player case using 251 conjugacy
  representatives of one three-cycle lift, yielding 21 recorded groups with
  explicit section witnesses. The analytic determinant-even quotient
  reduction covers the remaining standard case.
- Proved the arbitrary-player large-sign-kernel and constant-sign-kernel
  sufficient conditions. The coordinating agent supplied the further
  non-three-divisible player-count direct-summand argument; this agent
  independently checked and expanded its proof, without claiming sole
  discovery or cocycle coboundary vanishing.
- Obtained the actual primary ATLAS18-point generators for 3.S6, generated
  its 2160-element group, recovered the six ternary blocks, and verified a
  standard transitive order60 subgroup. The 1080-element even inverse image
  is perfect by a directly generated commutator normal closure.
- Verified its seven utility-cell orbits and full payoff-orbit closure, then
  found that each single-orbit binary payoff assignment retains the complete
  group. Chose the common-interest C18 indicator game, giving six literal
  seed rows plus common translation. Added a Hamming-distance analytic
  kernel reduction to twelve candidates, separately checking all46656
  player-fixed local maps.

The first sketch mistakenly described192 as coprime to three. This was caught
before the proof was written: averaging is over the normal even-sign subgroup
of order8, not over the whole determinant-even group. The saved proof uses
the corrected normal-subgroup averaging argument. No false whole-group
averaging claim remains.

The primary ATLAS name or literature nonsplitting claim is not substituted
for actual game realizability: the literal binary game is checked independently.
The abstract group and Hadamard/monomial realization are prior work, and game
novelty remains unresolved. Independent reviewers reconstructed the full C18
game by their own group operations before reports were combined.

## Independent cross-review of other Phase 5 results

I read `phase5-mechanisms.md` after its author supplied the candidate and
independently checked the opposite-face sign identity, full-group zero-locus
argument, binary surjective-completion counts, common-slope group form,
matching obstruction, clone-freeness and fixed-n4 minimality. No defect found.
The binary completion counts were recomputed as (m-1)! versus
2(m-1)!+(m-2)(m-1)!/2, distinct at every m>=2. This is supplied-proof
cross-review, not independent rediscovery of the construction.

I read `phase5-reductions.md` after the coordinating agent supplied it.
The full-vector clone quotient split exact sequence is valid: numbering
members within every clone class gives coherent lifts, and fixed-player
identity is preserved in both directions for the multiplicity-preserving
quotient subgroup. The preservation claims require that subgroup, rather
than the unweighted quotient's entire automorphism group; the text correctly
makes that distinction. The rectangle/player-deletion distinctions and
common-interest/zero-sum preservation limits are sound.

## Evidence and limits

Own certificates: `phase5_splitting.py`, `phase5_splitting_six.py`, their two
saved JSON records and `test_phase5_splitting.py`. Independent reconstruction
files and their authors' actual checks are recorded separately. No formal
proof-assistant certification, external review, author sign-off or priority
clearance is implied. The arbitrary-player theorem leaves divisible-by-three
player counts beyond the proved minimal six-player counterexample open.

Final direct reruns of both saved certificates passed, including every one
of the251 C4 representatives and the explicit binary C18 game. The two
focused regression tests passed in0.95 seconds. The necessary-extension-type
lemma P5-S8 was subsequently added by this investigator and sent to both
other reviewers; their findings are recorded in their own review files.
