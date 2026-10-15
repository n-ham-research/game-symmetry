# Unnumbered claims — second audit register

All 41 numbered formal results are now accounted for in audit.json. This register
covers the substantive prose/diagram assertions previously indexed and the new
issues found during the second pass. It is not a claim to have proved every
philosophical or historical sentence in the manuscript.

| ID / source location | Verdict | Evidence and corrected scope |
|---|---|---|
| U-increasing, §2 p.3 | Incorrect as printed; repair verified | exp is not onto; increasing bijections form a group; positive affine maps form a subgroup. corrections.md |
| U-real-utility, §2 pp.3–4 | Incorrect for arbitrary domains; finite scope valid | Lexicographic R x {0,1} has no real representation; finite total preorders have integer ranks. ordinal-and-domain-audit.md |
| Product mixed laws, §2 pp.4–7 | Repaired | Product map injective; onto iff at most one player has >1 action. Strict non-surjectivity not used by downstream proofs. |
| Mixed actions, §3.1 | Verified with typed replacement of malformed tuple proof | Focal/opponent maps and inverse identities in foundation-corrections.md. |
| Strict anonymity hierarchy, §3.3 | Verified in variable-game class | Full anonymity=>anonymity=>weak anonymity;3.12 separates first,3.10 separates second; extracted exact tables checked. Not strict for every fixed degenerate domain. |
| Generators suffice for correct equivariance, §3.4 | Verified | Symmetries form subgroup3.8. Does not mean checking D only on transpositions gives D for all permutations. |
| Numeric/ordinal/cardinal fairness identifications, §3.5 | Unresolved | Definition 3.24's preference-preservation maps and utility comparability need explicit specification. Keep exploratory interpretations out of theorem claims. |
| U-ordinal-count, §4.2 | Convention mismatch resolved; cited-book attribution not audited | 144 strict/fixed-player classes;78 allowing player interchange; with ties1413/726. Complete enumeration and independent Burnside check. Does not show the uninspected book is wrong. |
| Finiteness of ordinal equivalence classes, §4.2 | Verified | Finitely many weak orders on a fixed finite profile set; finitely many players; quotient remains finite. |
| Hom-set structures,4.10 | Ambiguous original; safe correction proved | Bijections/bitorsors exist; no inherited group structure on cross-object hom-sets. corrections.md |
| U-wreath, §4.3 | Corrected explicit group verified | Full typed group is (S_m)^n semidirect S_n; under stated usual convention S_m wr S_n. n=2,m=3 gives72 vs reversed48. |
| Strategy triviality/matching relabeling, §4.4 | Verified | Component uniqueness/coherence, reference-player matching, exact conjugation. No false 4.24 used. |
| Matching-count alternative, §4.4 | Verified | Fix one reference coordinate and independently choose n-1 bijections; count (m!)^(n-1). |
| Anonymous/full-anonymous analogues after4.24 | Explicit corrected formulations verified | All-player/all-permutation matching invariance gives anonymity upiso; E plus this gives full anonymity, equivalently E plus 5.2. Complete proofs and three targeted checks in corrections.md/review-log.md. |
| U-abstract-transitivity, prose after5.5 | Incorrect; actual-action repair verified | Singleton four-player payoffs(0,0,1,1); actual image intransitive V4, abstractly isomorphic to regular transitive V4. Degree4 minimal. action-and-torsor-audit.md |
| Abstract quotient is S_N criterion, same paragraph | Verified | Actual quotient image is subgroup S_N of equal order n!, hence all S_N. This special order argument does not apply to “some transitive subgroup.” |
| Cyclic regular-subgroup lift,5.6 | Verified | Faithful player projection preserves n-cycle order; regular player action has trivial stabilizers, hence strategy triviality. |
| Degree6 order 12 group, §5.1 /5.16 | Concrete group and example verified; cited priority not audited | Exact full Aut/image 12, kernel1; all matching-lift subgroups intransitive. External Hulpke source not inspected. |
| Shape analogies, §5.2 | Domain/boundary corrections required | Specify measurable finite positive area and allowed isometry group; n=1 scalene triangle refutes transitive=>nontrivial symmetry. ordinal-and-domain-audit.md. Original drawings not evidence for game results. |
| Classification procedure, §5.3 | Verified as finite decision procedure after quantifiers are explicit | Enumerate every matching and exact induced symmetry subgroup; equal-payoff matching is necessary by5.3, not sufficient alone. Do not restrict player-transitive search to n-cycles; the Klein4 action is a counterexample to that restriction. |
| Gamma(G) orbit construction, §5.4 | Verified | Independent parameters for payoff-cell orbits of generated typed subgroup; every generator preserves them. Full Aut can exceed generated subgroup. |
| U-parameter-aut,5.12 | Incorrect as parameter-uniform assertion; repaired | Merging orbit parameters may enlarge Aut. Generic2x2 family Aut 2 vs all-equal Aut 8. classification-audit.md |
| U-parameter-poset, §5.4 | Preorder clarified; quotient poset verified | Quotient orbit-equality families by relabeling/mutual inclusion. Generic distinct-block assignment detects family inclusion. |
| U-Hasse2, Figure 2 | Verified under precise family quotient | All 10 ambient subgroups, transitive ones,4 family classes; every source node/generator/cover checked. |
| U-Hasse3, Figure 4 | Verified under precise family quotient | All 98 ambient subgroups, transitive ones,7 family classes; every source node/generator/cover checked. |
| U-Euler, Figure 3 | Verified across variable player/strategy counts | Mathematical inclusions via5.1/5.2 and exact generic/numeric separating tables. Not a claim that every region exists for every n,m. |
| 5.13 uniqueness assertion | Corrected quantifiers verified | Exactly one generic Gamma(G) binary-three-player family has the advertised combination. Many concrete payoff assignments are nonisomorphic; some specializations are fully symmetric. |
| 5.13 pure equilibrium for every parameter choice | Verified | Homogeneous profiles are equilibria iff alpha>=delta; other six iff delta>=alpha. At least one set exists, independent of beta/gamma. |
| 5.13–5.15 parameterized examples | Corrected generic/specialization scopes verified | All equality patterns checked:15 each for four-parameter families,2 for5.15,4140 for eight-parameter5.14a. Exact source cells and independent payoff-condition verifier. |
| 5.16 numerical separating example | Verified | All 46080 ambient typed bijections and all 32 matchings checked on its64 profiles. Full automorphism group, not merely supplied generators, used. |

## Remaining substantive work

- Resolve intended hom-set/preference-transport/geometric-domain definitions.
- Inspect remaining original historical/attribution sources and original geometric
  illustrations if they are to be retained.
- The complete hierarchy beyond the displayed definitions, arbitrary player counts
  and possible future fairness notions is not a consequence of the two finite
  Hasse enumerations. Higher-degree or equilibrium extensions remain research.
