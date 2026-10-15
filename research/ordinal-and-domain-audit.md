# Ordinal and domain qualifications

16 October 2026. Corrections/clarifications to unnumbered Ham v5 claims; no novelty claim. Source statements remain in the original arXiv version. Internal independent check: Reviewer B's appended Burnside calculation in reviews/R-MATCH-003-B.md.

## The 144 ordinal 2x2 classes depend on the equivalence

The source cites Goforth–Robinson's count of 144 without stating the conventions needed to relate it to this paper's player-permuting, preference-preserving isomorphisms. The cited book has **not** been inspected, so no claim that its count is wrong is made.

Direct enumeration in experiments/ordinal_audit.py gives:

| Individual preferences | Labeled normalized games | Strategy relabeling, players fixed | Strategy relabeling plus player interchange |
|---|---:|---:|---:|
| Strict payoff rankings | 24² = 576 | 144 | 78 |
| Weak rankings, including ties | 75² = 5625 | 1413 | 726 |

For one player a strict ranking of four cells is a permutation of 0,1,2,3. A weak ranking is a surjective map from the four cells to {0,...,k-1} for some k<=4, with k ordered rank classes; there are 75. Every finite ordinal preference table has exactly one such normalized rank tuple. Each of the four strategy relabelings (fixed players) or eight typed bijections (player interchange allowed) acts by its precise permutation of payoff cells, moving the player index too. Canonical orbit representatives count the classes; Burnside's average of fixed-table counts independently checks the result.

In the eight-element group ordered by (player permutation, first component permutation, second component permutation), fixed counts are:

- Strict: 576,0,0,0,24,0,0,24; average 78.
- Weak: 5625,9,9,9,75,3,3,75; average 726.

Thus 144 is correct for the explicitly stated strict/fixed-player convention, but cannot be transferred unchanged to the broader equivalence described around the source's groupoid framework. The general assertion of finiteness for fixed finite action sizes remains true: each player has finitely many total preorders on finitely many profiles, and a quotient of that finite set is finite.

## Arbitrary rational preferences need not have a real utility representation

The background's general statement for an unrestricted set X is false under the usual meaning of rational (complete and transitive). Take X=R x {0,1} with lexicographic order. If a real utility u represented it, for every real x the interval `(u(x,0),u(x,1))` would be nonempty. For x<y these intervals are disjoint because u(x,1)<u(y,0). Every interval contains a rational; choosing the first such rational in a fixed enumeration of Q would inject uncountably many real x into Q, a contradiction.

Finite weak orders do have real utility representations: order their finitely many indifference classes and assign increasing integer ranks. This is all that the finite-game framework requires. The counterexample concerns the source's unrestricted wording, not an error attributed to an uninspected proposition in Mas-Colell–Whinston–Green.

## Shape-division analogies require a measurable domain and a player-count boundary

Definitions 5.7–5.10 are analogies, not game theorems. To make area comparisons well defined, specify a measurable shape of finite positive area and a finite partition into measurable pieces. Let the allowed symmetry group be explicitly the Euclidean isometries mapping the shape to itself and permuting those pieces (or explicitly declare a smaller rotation/reflection group). This is a subgroup by composition/inversion; it induces a homomorphism to the permutation group on colors.

With those assumptions, transitivity on the colors implies equal piece areas: an isometry carrying one piece to another preserves Lebesgue area. It does not require a choice of equilibrium or an allocation procedure. For n>=2 a transitive color action supplies a nonidentity color permutation, hence a nonidentity isometry. For n=1, however, the source's unnumbered claim that every transitively symmetric division is symmetric (nontrivial group) fails: a single-color scalene triangle has trivial isometry group, while its action on its sole color is transitive. Its fairness-by-equal-area condition is trivially satisfied. Thus the nontrivial-group conclusion needs n>=2.

The claim that transitivity need not give strong symmetry is witnessed by a disk partitioned into three congruent sectors: the dihedral symmetries act faithfully and transitively on the sectors; only the identity fixes each sector setwise. No game-symmetry theorem follows from this analogy without a defined correspondence between the mathematical objects. Diagrammatic shape illustrations were not used as evidence for the normal-form classification.
