# R-P3-EQ-C: binary equilibrium research and cross-reviews

16 October 2026. Agent C (`/root/phase3_equilibria`), same Codex family as the
coordinator and other agents; no different-model or external peer-review claim.
The task was initially a separate proof/counterexample investigation of Ham's
binary pure-equilibrium question. The agent read existing audited definitions
and source excerpts, and the coordinator later exchanged the kernel approach
and requested cross-review. Therefore the initial derivation was partially
separate, while later discussion and final proof reviews were unblinded.

## Binary investigation

I reconstructed the original question from the original v5 TeX, not from a
changed conjecture. I independently identified the four invariant binary
kernels and then developed the Coxeter lifting argument, the signed complement
classification, the n=4 obstruction to standardness, and the stronger passive
n=4 case. Complete proofs are in `research/phase3-equilibria.md`.

The strongest submitted candidate is: all binary games with n>=3 and actual
full player projection are exact potential games; for n>=5 they are fully
symmetric up to relabeling; for n=4 they are fully symmetric up to relabeling
or all unilateral utility differences vanish. The original question follows,
including n=1,2 under its standardness assumption. Three-player signed games
have an explicit potential and require neither common interests nor identical
majority-player payoffs.

I supplied the key proof steps to A and B before the final file was polished.
B independently checked the invariant kernels, complement classification,
Coxeter relations, n=4 double-transposition exclusion, signed n=3 potential,
and the stronger n=4 no-incentives argument. A and the coordinator were asked
to inspect the completed proof. Their actual findings are recorded separately;
this file does not invent a final response from them.

Exact computations enumerate all full-player-image subgroups at n=2,3 from
all ambient subgroups, and all such subgroups at n=4 using the proved kernel
classification and exact GF(2) quotient cocycles. At n=3 the two constructions
agree. There are 5,15,35 such subgroups respectively; these are representation
coverage counts, not numbers of inequivalent games. Utility-cell partitions
and formal square-cycle coefficient vectors verify all real payoff assignments
within these finite families. The computation finds no nonpotential family
for n=3,4, and correctly detects the n=2 matching-pennies exception. Five
research tests pass, including the directed-cycle standard-only counterexample,
all 81 three-level assignments of signed-game parameters, and the passive
property of Ham's actual Example5.15. No floating arithmetic is used.

## Independent review of A's splitting counterexample

Reviewed `research/phase3-splitting-proof.md`, including P3-S1b (two payoff
values). The proof is valid as written in the inspected draft. In particular:

- Six profile orbits exhaust 64 profiles; the sole all-zero-payoff orbit is
  the four-element diagonal. This forces all three local maps to be one f.
- For repeated action a, the unique positive-payoff repeated player switches
  according to a's parity. An odd player permutation reverses the cyclic
  order, forcing parity(f(a))=parity(a)+parity(p).
- For even p, the four parity-preserving f are id,T2 and the two reflections.
  The two reflections fail at the stated (0,1,2) focal cell. Odd p reduces by
  an already proved parity-matched T1 automorphism.
- The actual group is precisely the twelve parity-matched translations;
  its kernel has order two; all transposition lifts square to the nonidentity
  kernel element. No complement can exist.
- The strategy-trivial C3 proves standardness; full projection proves
  n-transitivity. Two payoff values are minimal because a one-value game has
  the whole typed-bijection group. No strategy-count minimality was inferred.

For an independent computational check I reconstructed the two-value F
formula directly and, after the diagonal argument, enumerated the 6*24=144
possible common-map transports rather than invoking A's exhaustive checker.
Exactly twelve preserve the payoffs, all precisely parity-matched translations;
the simultaneous zero-payoff locus has four profiles. This independently
confirms the crucial reverse-containment step. The larger all-typed-bijection
check is A's separate evidence.

## Review of specification and fairness notes

Inspected `research/phase3-specifications.md` and `research/phase3-fairness.md`.
The hom-set bijection has correctly typed domains and inverse; both bitorsor
actions and the choice-dependent transferred group operation are correct.
The pure/mixed/exact preference distinctions and both counterexamples check.
The lottery-affine proof explicitly uses unrestricted profile lotteries and
is not silently applied to independent product laws. The measurable-area
clarification has the necessary n=1 exception.

F1 is the finite Dirac/expectation characterization under explicit common
participant scales and specified whole-experiment transports. The asymmetric
successor graph in F2 really has trivial player image despite rolewise focal
opportunity equivalence. Optimized-value equality loses dominated options.
Exchangeable histogram tests recover only orbit averages, with the supplied
cyclic example exhibiting a nonzero within-orbit component. The coalition
transport proof is valid with coordinated joint coalition laws; the zero-sum
three-player example has all coalition values zero but no transitive game
symmetry. These comparisons do not establish a normative fairness theorem.
No independent historical verification of the cited von Neumann--Morgenstern
page claims was performed by this reviewer; those remain the coordinator's
source inspection.

## Limitations

These are internal mathematical checks and exact finite evidence, not a
priority determination or external review. Cheng et al.'s ordinary full
symmetry binary equilibrium theorem is prior literature. The author-uploaded Cao--Yang July29,2015 draft was subsequently opened and
its Definitions4/6 and Proposition4 inspected: renaming symmetry is ordinary
full symmetry after local relabeling; its name-irrelevant limitation uses
two-player matching pennies. The final2018 body still requires comparison
before any exact-potential novelty claim. The
unbounded-player result is supported by the complete proof, not by extending
the finite enumeration's scope. No manuscript edits or submissions were made.

## Follow-up: utility invariance and assignment models

After the user's two utility/fairness steering attachments, this reviewer
read `utility-invariance.md` U1--U6 and `assignment-and-solution-rules.md`
A1--A7. The finite-range ordinal/affine descriptions, subgroup laws,
min-max/rank normalizations, common player kernel, range-signature criteria,
and both strict player-transitivity examples check. The rational mixed-NE
counterexample has equilibrium probabilities (2/3,1/2), whose swap fails;
its two pure equilibria are correctly preserved. The weighted and ordinal
potential corollaries of P3-E2 follow by normalization, and the square-face
witnesses show that their potential strengths cannot generally be increased.

A and the coordinator supplied a further proof of necessity of positive
affinity from equality of **all independent mixed-profile weak comparisons**.
I checked the argument independently: continuity on the connected marginal
product domain gives the full interval of utility values. For an interior
value t, the open set U(x)<t<U(y) is nonempty. Each hybrid-profile polynomial
U(hybrid(x,y))-t has a zero set with empty relative interior: on x=y it
reduces to the nonconstant U(x)-t. A pair avoiding their finite union gives
a one-coordinate hybrid edge strictly crossing t. On that edge both U,V
are affine, so their increasing comparison map is locally affine near t.
Overlapping neighborhoods and connectedness force one affine formula;
continuity extends it to the extreme values. Constants are a separate easy
case. This uses neither convexity of the set of joint product laws nor an
unjustified extension from products to correlated lotteries. I requested
explicit relative-coordinate, image-interval and endpoint explanations.

The assignment propositions correctly separate a single participant's global
cross-role preferences from conditional player utilities. Group averaging
has the right inverse/pushforward order and only promises equivariance;
the warning about nonconvex properties is essential. A mixture of pure
numerical Nash equilibria is a correlated equilibrium by linear obedience
inequalities, without being identified with independent marginals. No
substantive defect was found in A1--A7.

`fairness-literature-solutions.md` records this reviewer's primary-source
inspection for Nash1950, Kalai--Smorodinsky1975, an identified original
Shapley1953 paper reprint, Varian1973, Bogomolnaia--Moulin2001, and a
Perry--Powers2008 research preview. Version/access limitations are explicit.
The original Nash fixed-input symmetry axiom differs from KS's globally
quantified equivariance axiom. No original1944 VNM inspection is invented.
