# Second-pass mathematical handover — 16 October 2026

The approved foundation has been followed by a full pass over all 41 numbered
formal results, explicit repairs, a dependency record and substantially stronger
finite checks. The main six-page LaTeX manuscript is **unchanged**. Nothing was
submitted to a journal or arXiv. Research notes and internal reviews are not
external peer review or final human sign-off.

## 1. Verification counts

| Audited formulation | Count |
|---|---:|
| Verified | 33 |
| Verified after correction/clarification | 7 |
| Incorrect without a verified replacement | 0 |
| Redundant or superseded | 0 |
| Unresolved as written | 1 |
| Total formal results | 41 |

These are not 41 unchanged valid source statements/proofs. Original 2.2(iii) and
4.24 are **incorrect**; replacements are proved. The other five corrected items
are 2.4, 3.6, 3.25, 4.19 and 5.11 (proof or typing corrections). Corollary 4.10's
assertion of isomorphic hom-sets is ambiguous as written; a bijection/bitorsor
replacement is proved, while its original intended structure remains unspecified.
See [the full audit](theorem-audit.md), [registry](audit.json) and
[exact correction statements and proofs](corrections.md).

All 33 remaining numbered definitions/examples have been visited in
[definition-audit.md](definition-audit.md), with parameter restrictions and the
remaining 3.24 preference-transport / 5.9 area-domain ambiguities explicit.
This does not certify every philosophical or historical sentence.

## 2. Principal repairs and new defects

**Corollary 4.24.** The proposed ambient-group change is sufficient, with a fresh
proof and three internal derivations. In the corrected statement G is a subgroup
of the full typed game-bijection group, not Aut(Gamma); retain strategy
triviality, full player image and each focal utility's invariance under its
player stabilizer. Equivalently, there is a matching M such that each focal
payoff is invariant under the matching lifts of all opponent transpositions.
The latter formulation dispenses with an existential group. No new payoff
regularity assumption is needed; singleton sets and n=1 extensions are checked;
unequal cardinalities make all common-label/matching clauses false. The explicit
anonymous and fully anonymous analogues are now also stated and proved.

**Product distributions, 2.2.** The map is well-defined and injective for every
finite nonempty family, including one player. It is onto iff at most one
coordinate has more than one action. The proof uses marginals and a two-point
correlated distribution, without division by potentially zero probabilities.

**Theorem 5.11.** Its finite-game statement survives. A player-swapping exact
automorphism may include strategy bijections. Push independent mixed laws
forward along those bijections, equate the players' security values, and use
zero-sum minimax to obtain zero. Bare swaps and pure extrema do not suffice.

**Additional numbered-proof issues.** Proposition 2.4's printed second display
reverses optimization variables; Proposition 3.6's inverse tuple is malformed;
Proposition 3.25's first proof sentence has the wrong payoff index. Their
statements remain valid with explicit replacement arguments. Lemma 4.19 needs
player-indexed groupoid objects, especially when underlying strategy sets agree.

**Additional unnumbered issues.** Abstract group type does not determine the
actual player action; parameter assignments may enlarge full automorphism
groups; the parameter-family relation needs a quotient to be a poset; the wreath
product requires the explicit semidirect-product convention; 144 ordinal 2x2
classes uses a narrower convention than player-swapping/tie-allowing ordinal
isomorphism. Arbitrary rational preferences need not have real utility
representations. The finite-game setting avoids that unrestricted-domain error.
The increasing-map subgroup repair is proved and its downstream uses checked.
See [action/torsor audit](action-and-torsor-audit.md),
[ordinal/domain audit](ordinal-and-domain-audit.md), and
[unnumbered ledger](unnumbered-claims.md).

## 3. Small counterexamples retained or added

- **Minimal printed 4.24 counterexample:** two players, one action each, unique payoff vector `(0,1)`. Weak anonymity and the matching condition hold; no automorphism exchanges the players. The original binary-action example is retained.
- **Nonconstant, non-vacuous version:** three binary-action players, `u_i(s)=10i+s_i` (zero-based i). Opponent anonymity holds, but disjoint player payoff ranges forbid player-moving automorphisms.
- **Actual action vs abstract group:** four singleton-action players with payoff vector `(0,0,1,1)`. Actual image `<(12),(34)>` is intransitive; abstractly it is isomorphic to the regular transitive Klein four group. Degree 4 is minimal for this mismatch.
- **Wrong 2.4 proof display:** `U1=[[0,1],[2,3]]`. The actual upper value is 2, the printed reversed-order expression is 1.
- **Untagged matching maps:** identical four-element strategy sets and a four-cycle p give `{id,p,p^{-1}}`, missing p² under ordinary composition. Explicit player tags repair the intended groupoid.
- **Parameter specialization:** generic 5.12 has Aut order 2; all parameters equal gives order 8. Generic 5.13 has order 6; all equal gives 48. Thus a generic automorphism group need not persist at every specialization.

## 4. Dependency and classification status

Theorem 4.23 and Corollaries 5.1–5.3 survive by complete component/coherence and
conjugation proofs. They do **not** depend on false 4.24. The strict
non-surjectivity component of 2.2 is unused by downstream formal proofs. Security
arguments use only the valid product-law construction and exact transport.

`dependencies.json` records prerequisite-to-dependent review edges and separates
original explicit citations from corrected proof dependencies. For example:

```sh
python3 scripts/audit.py check
python3 scripts/audit.py impact 4.24
python3 scripts/audit.py impact 4.23
```

An error report identifies affected descendants for reconsideration; the script
never silently changes statuses or labels every descendant false. The pinned
74-item source inventory remains byte-identical to first commit a30c617, with
selected original proof environments, diagrams and exact counterexamples preserved. This is a
Git-based immutable baseline/tamper check, not external authentication or a
write-once storage service.

The source Euler diagram's inclusions and separating examples are checked.
Both binary Hasse diagrams are exhaustive under the precise quotient of
Gamma(G) equality families: 4 classes for 2 players and 7 for 3 players, from all 10
and 98 ambient subgroups respectively. Every displayed node, generator constraint
and cover edge matches. This is not an unrestricted classification of all games.

The exact numeric/generic tables 5.13–5.16, all matching lifts and the supplied
generators are checked. Every parameter-equality pattern is covered for the
parameterized examples, including all 4140 patterns of eight-parameter 5.14a,
independently rechecked by compiled equality constraints. The example 5.13 pure
Nash assertion has a direct inequality proof valid for every real parameter
assignment, not merely sampled equality patterns. See
[classification-audit.md](classification-audit.md).

## 5. Validation and source limits

- 38 tests pass, using the Python standard library and exact values.
- The source-integrity checker covers 5 pinned artifacts and all 41 formal IDs.
- Seven exact matching/subgroup domains cover all real payoff assignments within
 each fixed domain by equality partitions; all 256 binary-payoff 2x2 games are
 additionally enumerated (228 refute the printed 4.24 equivalence).
- Source-specific automorphism enumeration is complete; no real-valued sampling
 is used for the symmetry classifications. The largest table has 6 players,
2 actions each, 46080 ambient typed bijections and 64 profiles.
- The unchanged manuscript builds successfully with its existing reproducible
 command. Fresh-checkout validation is recorded in the final chat handover.
- No downloaded copyrighted papers or access-denied HTML responses are tracked.

Original Dasgupta–Maskin pages remain unreadable in the available retrieval
workflow (Harvard/public author-upload requests returned 403). The requested trace
through Definition 7, Lemmas 6–7 and Theorems 6/6* is therefore **still unverified**.
Plan's actual author research link was independently checked and still serves
byte-identical March 2017 content; the 2023 final body remains unavailable.
The access attempts, version evidence and response hashes are recorded in
[primary-source-followup.md](primary-source-followup.md). No proof conclusion
is inferred from these failures, and neither gap delayed the Ham audit.

## 6. Remaining mathematical questions and next investigation

1. Resolve the intended structure in 4.10 and preference-transport quantifiers in
3.24; make geometric area assumptions explicit if those analogies are retained.
 These are editorial/mathematical specification tasks, not reasons to distrust
 the independently proved matching chain.
2. Obtain readable original DM86 and final Plan texts and perform the exact
 proof/version trace. The historical 2011/2012/2013 chronology and 1953 warning
 remain carefully distinguished in the existing primary-source notes.
3. Audit the open converse near 5.6: does n-transitively standard symmetry force
 a subgroup whose player projection is an isomorphism onto S_n? This is a
 splitting question about the **specified** player projection, not abstract
 group transitivity.
4. Investigate the source's pure-Nash question for n-transitively standard
 binary games using the now-checked family classifications and exact
 counterexample search, before trying to generalize any theorem.
5. Only after choosing independently justified decision primitives, compare
 fairness notions with the audited hierarchy. [fairness-preparation.md](fairness-preparation.md)
 keeps assignment, information, strategy correspondences, beliefs and utility
 normalization separate; it does not define fairness to be symmetry.

Recommendation: finish the remaining specification issues and source proof trace,
then prioritize the 5.6 splitting question and binary-equilibrium search. They are
concrete existing open questions. Keep substantial manuscript expansion and new
fairness-equivalence claims deferred until this audit record has been examined
by the author. No new-result priority or external-peer-review claim is made.
