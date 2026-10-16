# Review log — 16 October 2026

## R-DM-001: known inverse-permutation characterization

Statement: common nonempty A, finite n>=3, left profile action
(P_pi s)_j=s_{pi^{-1}(j)}. D for all permutations iff total symmetry and identical
payoff functions. Source: Ham v5 Theorem 3.21 / Vester Theorem 32 (consequence).

Three additional OpenAI Codex agent instances were actually used. They inherited
full chat context, including the theorem setup and the coordinating agent's
candidate proof. They did not receive another reviewer's completed report before
their own first report. A was explicitly given the proof; B/C were instructed
to derive independently and avoid consulting the candidate proof or other
reviews, but their inherited context means the process was **not fully blinded**.
No exact model build identifier was exposed; do not infer three different models
or external peer review. The source and explicit derivations, not consensus,
justify the mathematical conclusion.

| Record | Role | Finding | Evidence/limits |
|---|---|---|---|
| [A](R-DM-001-A.md) | Inference checking | No defect in candidate proof or Ham's original proof | Expanded composition, surjectivity and 3-cycle step; inspected source |
| [B](R-DM-001-B.md) | Counterexample search | No counterexample within stated scope; false strengthenings refuted | Own-action, common asymmetric and variable common-payoff examples; exact partitions on nine domains |
| [C](R-DM-001-C.md) | Strengthening | Same equivalence, no action-set finiteness needed | Abstract S_n-set formulation; coherent identification caveat; novelty unestablished |

The coordinator reproduced the nine equality-partition computations in tracked
experiments/constraint_audit.py and tested action composition and explicit
examples. Actual output is experiments/results.json. The existing finite-game
theorem enters the manuscript with attribution; the abstract extension stays
in research/dasgupta-maskin.md.

## R-AUDIT-002: targeted follow-up by A

The coordinator supplied four findings for criticism. Reviewer A confirmed the
counterexamples to Proposition 2.2, Corollary 4.24 and the increasing-function
subgroup assertion, and the two proof gaps in Theorem 5.11. Record:
[R-AUDIT-002-A.md](R-AUDIT-002-A.md). This is a follow-up review by the same
instance, not a fourth independent review.

A initially queried whether the source allowed infinite games for Theorem 5.11.
The coordinator checked the background's explicit declaration that all games
are finite and supplied that passage; A withdrew the scope objection. The
infinite-game counterexample is not evidence against v5's scoped statement.
The proof defects remain. This correction illustrates why reviewer agreement
is insufficient and source assumptions must be checked directly.

## Outstanding reviews

- Full verification of all 41 numbered results, particularly strategy triviality and matchings.
- Audit of all diagram edges, constructions and parameter restrictions.
- Primary-source audit of Dasgupta–Maskin's existence proofs.
- Full final Plan article comparison.
- Human author review and external mathematical scrutiny.

## R-MATCH-003 / R-FOUND-003: second full formal audit

The author approved the foundation and explicitly requested continued adversarial
review, repairs and logical commits without substantial manuscript expansion.
The coordinating instance assigned two new agents with `fork_turns=none`:
matching_proofs (A) and matching_search (B). They received the source locations,
existing audit records, original counterexample and proposed ambient-group
repair, but no new candidate proof or other new reviewer's endorsement. They
read the existing repository records, so this was not a blind rediscovery of
the suspected error. A third review used the earlier proof_review instance (C),
whose prior exposure is explicit. All three independently reconstructed the
Corollary 4.24 repair before their new reports were compared. All are Codex
instances sharing a model family, not external peer reviewers.

- [A](R-MATCH-003-A.md): matching/strategy-triviality chain, 4.10 hom-set ambiguity, 4.19 indexed groupoid qualification and 5.1–5.3.
- [B](R-MATCH-003-B.md): independent corrected proof, exact all-subgroup/equality-partition challenge on seven domains, minimal counterexamples, later independent ordinal/Burnside and domain checks.
- [C](R-FOUND-003-C.md): independent corrected proof; all remaining foundational/formal results; mixed-value repairs; supplementary source checks of the twelve previously verified formal IDs.

No defect was found in the repaired 4.24 equivalence. The full bijection ambient
group is necessary; stabilizer invariance and full player image must be retained
(or use the simpler matching/opponent-transposition formulation). All reviewer
proofs were checked by the coordinator against component domains and composition.
Corollaries5.1–5.3 have independent proofs and do not inherit the false 4.24.

New source proof defects are recorded for2.4,3.6,3.25. The source's unspecified
4.10 hom-set isomorphism and inferred4.19 groupoid objects are separated from
their safe corrected formulations. The actual-action counterexample disproves
the unnumbered abstract quotient transitivity criterion. The source's increasing
map assertion remains false; its repair is proved. Current machine-readable
formal counts:33 Verified,7 Verified after correction,1 Unresolved as written.
The two incorrect printed statements remain recorded as incorrect separately;
they have not been overwritten with corrected source text.

The original 74-item inventory remains byte-identical to commit a30c617. The
source/archive hash and selected exact defective proof environments are pinned
by research/original-record.json. The checker reports changed pinned bytes;
this is Git-based tamper evidence, not an external timestamp or write-once store.

## Classification and additional finite checks

A subsequently extracted and checked all actual numeric/symbolic source game
tables, exact automorphisms/matching lifts for5.13–5.16, Euler separations and
all source nodes/cover edges in both binary Hasse diagrams. See
research/classification-audit.md and experiments/classification-results.json.
The coordinator removed reliance on a temporary/cache TeX source for tests by
pinning author-owned diagram excerpts in research/original-diagrams.json.

The coordinator additionally enumerated all 4140 parameter-equality partitions
for5.14a and independently verified the results by compiling each ambient
bijection's payoff conditions into equalities on the 8 parameter names. No
sampling of real values or floating arithmetic is involved. Reviewer B
independently checked the ordinal convention counts by Burnside's lemma; the
coordinator's tracked program also enumerates complete orbits.

An added regression test initially mistranscribed the first component of
Example 4.4's printed composite as identity. Reinspection of the original TeX
showed it is the strategy flip; the test was corrected to match the source.
The source's Example 4.4 composite is valid. This was a test-data error, not a
new error attributed to the paper.

## Primary-source follow-up

B's bounded follow-up retried the actual Harvard/author-upload/publisher links.
No readable DM86 original or Plan final body was obtained. Actual HTTP failures
and cached-response hashes are in research/primary-source-followup.md. Plan's
actual author link still delivers byte-identical2017 draft content. This work
supports no conclusion about Lemmas6–7 or Theorems6/6* of DM86; those original
proofs remain uninspected. Source-access failures did not delay the mathematical
Ham audit. No credentials, external messages or submissions were used.

## R-ANON-004: final targeted source-prose clarification

The coordinator supplied the same explicit anonymous/full-anonymous candidate
formulations independently to A, B and C after their main reports. These were
not blinded reviews: all had reviewed the 4.24 repair, and no different-model
independence is claimed. They were instructed not to read one another's new
responses. All returned complete conjugation proofs and boundary checks by
message; no additional agent-authored files or external review are invented.

Their shared mathematical route: pull back the common-label diagonal under an
arbitrary player-permuting exact isomorphism, conjugate all matching lifts to
all S_N, and use exact-isomorphism invariance of pointwise payoff equality E.
Thus anonymous upiso is all-i/all-permutation matching invariance; fully
anonymous upiso is E plus that condition, equivalently E plus 5.2 full symmetry.
Singleton/unequal-size cases were checked in all responses. The coordinator's
canonical complete proof is corrections.md, section C4.24-A/C4.24-FA. This closes
the previously unstated analogue gap for these exact numerical definitions;
it does not resolve ordinal/cardinal preference or normative fairness concepts.

## Research Phase 3: new questions and cross-review

The user approved Phase2 and explicitly authorized affirmative/counterexample
agents and new mathematical investigation. Three fresh subagents received
full conversation context and the shared repository: A on affirmative splitting,
B on counterexamples, C on binary equilibria. None was a different-model or
blinded human reviewer. Initial discoveries were communicated before later
cross-checks; later reviews were of supplied candidate proofs.

A found and proved the main nonsplit three-player/four-action game, finally
using only two payoff values. B independently developed a different signed
four-player/six-action obstruction. C derived the full-image binary exact-
potential theorem, strengthening the original standard-symmetry question.
A and B checked C's kernel, Coxeter, stabilizer and exceptional n=4 argument.
B and C checked A's exact-Aut proof, two-payoff reduction and nonsplitting.
The coordinator independently read the complete proofs and checked the same
sensitive steps; exact finite regressions accompany the general arguments.

The coordinator's preference/bitorsor/geometry specifications and operational
fairness notes were checked by A and B, including every counterexample and the
zero coalition-value separation. VNM's original coalition-orbit and
set-transitivity equations were re-read in the previously inspected scan text;
that basic bridge is explicitly attributed. No normative fairness hierarchy or
unverified novelty is promoted to the manuscript. Primary-source retries did
not provide readable DM86 or final Plan proof bodies.

Detailed actual findings: R-P3-SPLIT-A.md, R-P3-SPLIT-B.md,
R-P3-EQ-C.md and R-P3-FAIR-SPEC-B.md. The result/dependency ledger is
research/phase3-results.md. The original41-formal-result registry and pinned
artifacts retain their prior meaning. New contributions remain research
candidates pending targeted literature comparison and human/external scrutiny.

## Utility invariance, historical fairness and assignment models

After two further user briefs, the same A/B/C agents continued rather than
being counted as independent new model instances. A wrote utility-invariance.md
and exact examples; B/C independently reviewed normalization, signature/kernel
lemmas, strictness, equilibrium preservation and potential corollaries. A and
the coordinator independently derived the hybrid-marginal necessity proof;
B/C checked the written argument, its relative-interior polynomial step,
connectedness and endpoint cases. This confirms the old finite-game affinity
statement without assuming product joint laws form a convex set.

The coordinator's assignment-and-solution-rules.md received A/B/C checks.
B identified overbroad wording suggesting ordinal data supplies expected
orbit averages; it was corrected to require a selected expected-utility
representation, while retaining the ordinal factorization/tie conclusion.
Underidentification, timing, uniform assignment and equilibrium-lottery
propositions otherwise passed all checks. Details: R-UTILITY-A.md,
R-P3-UTILITY-B.md, R-P3-ASSIGN-B.md and the appended R-P3-EQ-C.md.

B's primary-literature report R-P3-FAIR-LIT-B.md records complete VNM§28 OCR
and visual inspection in the1953 third edition, and actual published modern
bodies inspected. C's annotated source note records original/reprint/draft
boundaries. The coordinator recorded a bounded1944 search after the Library
Genesis suggestion; no first-edition body was obtained. Neither literature
survey nor AI agreement is described as priority clearance or external review.

## Phase 4: skeptical verification and mechanism classification

A/B/C began with full shared historical context and different fresh assignments;
no blinded/different-model independence is claimed. A reconstructed the binary
kernel, stabilizer and Coxeter proofs, separately tested n≥5 rigidity and n=4
passivity, and supplied an alternate exact GF(2) search through n6. B analyzed
all648 odd lifts after standard-cycle normalization; C investigated reductions
and found the ternary common-interest orientation game.

The order18 orientation group invalidated a temporary only-order6 inference
about actual automorphism overgroups. B replaced it by the correct order6/18
classification. The proof now explicitly uses payoff-orbit closure, not merely
embedded subgroup properties. Another proposed strengthening (section must
contain the given standard cycle) failed in four certificate groups and was
not retained. A/C independently reconstructed the complete finite certificate
with utility-cell permutation actions; A imports no existing group/matching
implementation. The coordinator independently read the full theorem proofs.

All three checked the Phase3 nonsplit witness analytically. C's census shows
S1b restricts to5.13 if emergent symmetries are allowed; the new common-interest
witness provides a stronger reduction obstruction. The assignment note was
reviewed by A/B/C; A/C found the missing reference normalization t0=id, now
fixed. C also checked the finite-range collapse/interchangeability note.

Details: R-PH4-BINARY-A.md, R-P4-TERNARY-B.md, R-P4-MECHANISMS-C.md.
The coordinator's novelty table distinguishes inspected bodies from previews
and missing final texts; no search failure certifies novelty. Original41-result
counts and pinned artifacts remain unchanged, and the main manuscript has no
Phase4 additions. Internal agreement is not external mathematical review.

## Research Phase 5 adversarial verification

User authorized independent algebraic investigation and logical commits.
Three fresh same-family instances worked initially on separate problems,
with full historical context: p5_ternary_audit (completeness), p5_splitting
(player-count extensions), p5_mechanisms (realizations/reductions). They later
shared findings for explicit cross-review. This is neither blinded review,
three distinct model families, external peer review nor author sign-off.

- [R-P5-TERNARY](R-P5-TERNARY.md): independent32/11-case ternary exhaustion;
  independent four-player251-case reconstruction; general kernel/cocycle proof
  attack; literal eighteen-profile six-player binary-game reconstruction.
- [R-P5-SPLITTING](R-P5-SPLITTING.md): local-sign reductions, four-player
  certificate, arbitrary-player proof development and actual six-player
  nonsplit realization; cross-review of orientation and clone quotient proofs.
- [R-P5-MECHANISMS](R-P5-MECHANISMS.md): signed/binary opposite-face theorem;
  separate six-player group/kernel/standardness/perfectness verifier;
  cross-review of general splitting, reductions and standalone proofs.

The coordinator supplied the direct-summand3∤n idea after the large-sign and
constant-sign lemmas; the splitting agent developed its full proof and other
agents reconstructed it. At n6 the ATLAS group name suggested the search but
was not accepted as a game proof. All three implementations establish a
complete actual group through its full player image and exhaustive pointwise
kernel. Explicit standard subgroup and perfect even-preimage certificates
establish the two other crucial hypotheses and nonsplitting. Binary common-
interest coarsening was separately checked; no reliance on a generic table
remains in the final example.

A whole-group averaging sketch was corrected (192 is divisible by3); only
normal2-subgroup averaging is used in the retained proof. A stronger inherited-
restriction irreducibility inference was rejected; minimality is now proved
for the specified target properties using binary rigidity. Source comparisons
identify covering-group closure and the triple-cover/Hadamard representation
as established prior work. New game/minimal-boundary claims remain candidates.
The main LaTeX manuscript and original audit registry are unchanged.

## Phase 6 consolidation and independent audit

R-PH6-SHARP-A records the fresh proof/counterexample audit, exact hypotheses,
actual-group necessity, regenerated finite table and source-based only-six
corollary. A second fresh agent independently reviewed that corollary in the
companion game-fairness review R-P6-CROSS. Root also checked the extension
argument and both manuscripts. This is two same-family agents plus coordinating
review, not three independently blinded models or external peer review.
The new universal player-count consequence imports established multiplier
theory; the code-to-indicator-game encoding and underlying3.S6are prior
structures. Tests verify finite ingredients, not the general theorem.


## Phase 7 final targeted structural audit

The delegated p7_symmetry instance reconstructed the complete sign-kernel,
translation-module and central-extension reduction, rather than checking
only the final multiplier lemma. No defect in the retained hypotheses was
found. The arbitrary-subgroup D_n counterexample remains decisive evidence
that complete actual groups cannot be replaced by chosen preserving groups.
The agent supplied explicit normalization transfer and manuscript hierarchy
clarifications, refreshed primary multiplier/potential sources, and recorded
limits in research/phase7-final-structural-audit.md. It shared prior context
and a model family; no new independent human review or novelty clearance is
claimed. The coordinating agent was asked to cross-review before push.

## Phase 8 publication-preparation review

The p8_symmetry instance checked fixed-recipient payoff closure and the
universal-central-extension interface conceptually, explicitly avoiding an
assumption that the even preimage is perfect in the general theorem. It
prepared precise specialist review questions and a shorter explanation of
the attained example's nonsplitting. No new classification is claimed.
Source refresh and limitations are in research/phase8-review-readiness.md.
This was shared-context same-family internal work; coordinating cross-review
was requested, not external mathematical approval.
