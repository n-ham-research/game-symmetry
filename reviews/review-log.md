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
