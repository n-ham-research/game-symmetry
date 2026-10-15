# R-MATCH-003-B — adversarial matching review

Status: independent internal AI review, 16 October 2026. Supplied context included the printed Corollary 4.24 counterexample and proposed ambient-group repair. I derived the proof below without reading another new review. Shared model/context limits independence; this is not external peer review. No novelty claim.

Sources inspected: Ham v5 `/tmp/ham-v5-source/section-bijections.tex`, Theorem 4.23 and following corollary; `/tmp/ham-v5-source/section-label-independent-symmetric-games.tex`, first three corollaries; repository inventory, roadmap, theorem audit, review log. Permutations compose right to left and `(P_pi s)_j=s_{pi^{-1}(j)}`. Strategy sets are finite nonempty; original scope n>=2.

## Finding and independent proof

**Previously established by Ham, checked here:** Theorem 4.23 is valid with the full typed bijection group as ambient group. Let G be transitive and strategy trivial. For any i,j, choose g taking i to j and define c_ij as its i-component. This is independent of choice: if g,h both take i to j, h^{-1}g fixes i, so its i-component is identity and g_i=h_i. Composition then gives c_jk c_ij=c_ik, c_ii=id. Fix player r and set M={(c_ri(a))_i:a in A_r}. Each c_ri is bijective, so M is a matching; its induced maps are c_ij. Every g is therefore M_{player(g)}, proving G=M_{player(G)}. Conversely, each element of M_H fixing player i has component M_ii=id, proving strategy triviality. This proof does not require a splitting assumption: strategy triviality also forces the player-action kernel to be trivial.

**Candidate correction to previously established Ham statement:** In Corollary 4.24(ii), require G to be a subgroup of the full typed game-bijection group, with player image S_n and strategy triviality; retain exactly the printed focal-stabilizer payoff condition. These three conditions are equivalent. In particular, the proposed ambient replacement survives adversarial checking; it is not accepted merely by analogy.

Proof (ii)<=> (iii): n-transitivity on n players means player image S_n. Apply Theorem 4.23 to obtain G=M_{S_n}. Its player-i stabilizer consists exactly of M_pi with pi(i)=i, giving the identical payoff equalities in (iii). Conversely a matching gives precisely this subgroup, with strategy triviality and full player image.

Proof (i)<=> (iii), including arbitrary player relabeling: for an exact isomorphism F from Gamma to a common-action game Gamma', let rho be its player permutation and f_i:A_i->B its strategy components. Define M by equality of all labels f_i(a_i). For pi fixing i, the conjugate F M_pi F^{-1} is the pure-coordinate permutation rho pi rho^{-1}, which fixes rho(i). Exact isomorphism gives u'_{rho(i)}(F(s))=u_i(s). Weak anonymity of Gamma' now gives the asserted focal equality. Conversely choose common labels B=A_r and f_i=M_ir. Transport payoffs by this exact relabeling; conjugation turns every M_pi into P_pi, so (iii) becomes weak anonymity. This explicitly handles the potentially omitted player permutation in (i).

**Previously established by Ham, checked here:** Corollaries 5.1 and 5.2 hold when “Gamma has a subgroup” means subgroup of Aut(Gamma), as intended by the Section 5 terminology. Theorem 4.23 proves their subgroup/matching equivalences. The same conjugation above turns M_T automorphisms into label-preserving T symmetries, and conversely, proving the isomorphic-game clauses. For Corollary 5.3 choose M,T from 5.1. Each s in M is fixed by every M_pi. For any i,j, choose pi in T with pi(i)=j; automorphism equality gives u_i(s)=u_j(M_pi(s))=u_j(s). Transitivity of T is essential to this last step.

## Boundary cases and refutations

**Disproved printed statement:** retain the existing binary-action example u_1=0,u_2=1. Every matching satisfies (iii); the game itself is weakly anonymous; no player-moving automorphism exists. A smaller genuine counterexample uses one action for each of two players and the same utilities. Thus n=2 and total strategy-profile count 1 are minimal under the source n>=2, nonempty strategy-set scope. Singleton strategies must not be excluded silently.

For a non-vacuous opponent-permutation example, n=3, two actions each, u_i(s)=10i+s_i (zero-based i). It is weakly anonymous, but the three payoff ranges are disjoint, so no automorphism moves any player. Weak anonymity therefore cannot be replaced by full/standard symmetry or imply player-transitive automorphisms, even with nonconstant utility functions.

**Disproved strengthening:** player-transitive automorphisms alone cannot replace the strategy-trivial subgroup in 5.1. Binary matching pennies has a player-transitive automorphism group of order four and no transitive strategy-trivial subgroup; its diagonal profiles have unequal utilities. This is a known Ham example, independently checked here, not a newly discovered counterexample.

Unequal strategy cardinalities admit no matching and no player-transitive typed-bijection group. Nor can an exact isomorphism make them common-action games. Thus all three clauses of the repaired equivalences are false, and 4.23/5.3 premises are impossible. Singleton equal strategy sets are permitted and the proofs apply. The proofs also work for n=1 if definitions are extended, but that is outside the inventoried scope.

## Exact computation and coverage

Owned artifacts: `experiments/matching_audit.py`, `experiments/test_matching_audit.py`, `experiments/matching-results.json`. The utility enumerates all typed bijections, their composition and action; all subgroups by generator adjunction and exact closure; all matchings normalized by player 0; strategy triviality; transitivity; payoff constraint partitions; and implications between finite unions of equality-constraint conditions. No changes to finite_games.py.

Domains and complete counts (sizes; full typed group; subgroups; matchings):

- (1,1): 2; 2; 1.
- (2,2): 8; 10; 2.
- (3,3): 72; 112; 6.
- (1,1,1): 6; 6; 1.
- (2,2,2): 48; 98; 4.
- (1,2): 2; 2; 0.
- (1,1,2): 4; 5; 0.

All domains pass Theorem 4.23 and repaired 4.24(ii)<=> (iii), 5.1(ii)<=> (iii), 5.2(ii)<=> (iii), and the 5.3 implication. These payoff checks cover **all real payoff assignments on each fixed domain**, using equality partitions rather than sampling: a conjunction is represented by its equivalence relation P on payoff cells. It implies a finite disjunction of conjunctions Q exactly when some Q imposes only P-identifications. If none does, assigning distinct integers to distinct P-blocks is an explicit counterexample to the disjunction. Applying this separately to every antecedent partition establishes exact implication for the finite union. This avoids falsely claiming enumeration of 2^24 binary games for n=3,m=2.

In addition all 256 binary payoff games on n=2,m=2 were enumerated: 228 refute printed (i)<=> (ii); 28 satisfy its automorphism-based (ii). Relabeling is independently checked by converting local actions to matching labels, permuting, and converting back for all n=3,m=2 matchings, permutations and profiles. The isomorphic clauses are justified by the general conjugation proof above; the finite partition checks do not separately enumerate arbitrary target labels or claim a new independent finite proof of those clauses.

Tests verify composition on all pairs of typed bijections and profiles for (2,2),(1,2),(2,2,2), known complete subgroup counts, all seven domains, explicit relabeling, preserved and minimal false examples, the nonconstant three-player example, matching pennies, and the partition witness principle. Finite success alone is not proof beyond these domains; the abstract proofs above supply that step.

Final validation: `python3 -m unittest discover -s experiments` ran 18 tests successfully. Added callable `weakly_anonymous` and `relabel_game` helpers, and an additional test transporting canonical weak-anonymity payoff partitions through every binary three-player matching with a nontrivial player permutation. The regenerated JSON includes all three explicit counterexample/failed-strengthening records alongside the preserved binary distinct-constant record.

## Follow-up: ordinal counting conventions and unrestricted real utility claim

**Internal independent check, 16 October 2026.** The coordinator supplied candidate counts; I independently recomputed fixed-point counts directly from typed profile/player actions, without using its proposed `ordinal_audit.py`. Read original Ham v5 `section-bijections.tex` lines 104 and 126 and `section-background.tex` lines 46–48. No Goforth–Robinson book or Mas-Colell–Whinston–Green proposition was inspected in this follow-up; conclusions below concern Ham's stated scope, not correctness of the cited primary sources.

**Candidate source-convention clarification, not an accusation against Goforth–Robinson:** The unnumbered finite-count assertion is valid: on a fixed finite profile set, finitely many total preorders exist for each player's preferences. However the following 144-class example needs explicit conventions. Ham's game-isomorphism framework permits player relabeling, and its finite utilities allow indifferences. If “ordinal equivalence” inherits both permissions, 144 is not its count for all two-player two-strategy games. The count 144 is instead exactly obtained for strict preferences and strategy relabelings with player identities fixed. The book could legitimately use these narrower conventions; the mismatch does not refute the cited book. Even when excluding ties, admitting player interchange changes 144 to 78. Allowing ties changes the counts to 1413 (fixed players) or 726 (player interchange allowed). These are normalized pure-profile ordinal preferences, not mixed-strategy/cardinal equivalence or additional outcome/utility reversals.

Independent exact enumeration: assign each player's four profile payoffs a normalized rank vector. Strict orders are all 4!=24 permutations of (0,1,2,3). Weak orders are all surjections from four labelled profiles onto {0,...,k-1}, k=1,...,4: 75 vectors, with rank labels in increasing preference order. There are respectively 24²=576 and 75²=5625 ordered games. Act by independent flips a,b of the two local actions, followed optionally by swapping player identities and coordinates. Utility components move with their players. This realizes the full typed-bijection group of order eight on these ranks, and its player-fixing subgroup has order four.

For group elements listed as `(swap,a,b)` in lexicographic order, independent fixed-game counts were:

- Strict: 576, 0, 0, 0, 24, 0, 0, 24.
- Weak: 5625, 9, 9, 9, 75, 3, 3, 75.

Burnside therefore gives strict fixed-player `(576+0+0+0)/4=144` and full `(576+24+24)/8=78`; weak fixed-player `(5625+9+9+9)/4=1413` and full `(5625+27+150+6)/8=726`. The zero strict fixed counts for nontrivial action-only maps follow because a strict ranking cannot be invariant under any nonidentity permutation of the four profiles. Any nontrivial action-only map has two profile orbits; exactly three weak rank orders are constant on those orbits, so two independently ranked players give 3²=9. For player-swap elements with a=b, the square acts identically on profiles, so one player's arbitrary 24 or 75 ranking uniquely determines the other. For a!=b, the square flips both actions, so only the three compatible weak rankings survive; no strict ranking survives. These analytic checks independently explain every enumerated fixed count.

**Disproved unrestricted claim; finite-game restriction unaffected:** Rationality meaning completeness and transitivity does not guarantee a real-valued utility representation on an arbitrary set X. On `X=R×{0,1}`, use the lexicographic strict order: `(x,0)<(x,1)<(y,0)<(y,1)` whenever x<y. This induces a complete transitive preference relation. If a real representation U existed, each x would give a nonempty real open interval `I_x=(U(x,0),U(x,1))`. For x<y, strict representation gives `U(x,1)<U(y,0)`, so I_x and I_y are disjoint. Each I_x contains a rational; choosing the first such rational in a fixed enumeration of Q yields an injection from the uncountable set R into Q, impossible. No continuity hypothesis is needed for this counterexample. This refutes the broad “for a set X any rational preference relation” sentence as written, while leaving finite games intact: a finite total preorder has finitely many indifference classes, which can be assigned consecutive real ranks. The exact qualifications of the cited MWG Proposition 3.C.1 remain a primary-source question; this argument must not be presented as showing that proposition false.
