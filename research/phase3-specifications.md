# Phase 3: resolved specifications

16 October 2026. Clarifications of Ham v5, not novelty claims. Convention:
`(P_pi s)_j=s_{pi^{-1}(j)}`; composition is right to left. Finite nonempty
strategy sets throughout. This file chooses precise replacement language; it
does not certify an unspecified original meaning retrospectively.

## S1. Corollary 4.10: sets and bitorsors

The natural interpretation is an equipotence assertion about nonempty typed
isomorphism hom-sets. Let games X,Y,Z be isomorphic, choose a:X→Y and b:Y→Z.
Then f↦b f a^{-1} maps Isom(X,Y) bijectively to Isom(Y,Z), with inverse
h↦b^{-1} h a. This proves the intended set-level statement.

More intrinsically Isom(X,Y) is an (Aut(Y),Aut(X))-bitorsor: composition acts
on its two sides, the actions commute, and both are free and transitive.
For f,g:X→Y the unique left multiplier is g f^{-1} and the unique right
multiplier is f^{-1}g. These formulas prove every assertion. A chosen a:X→Y
transfers a group law by f*g=f a^{-1}g, whose identity is a. Without a choice
there is no distinguished identity or inherited hom-set composition. Even a
nontrivial group acting on itself by translations has no translation-invariant
choice of one distinguished element. No canonical group structure is claimed.

Recommendation: use the one-sentence bitorsor description when discussing
choices of lifts; retain the elementary bijection as the replacement of 4.10.
The useful connection to splitting is that each nonempty fiber q^{-1}(pi)
is a kernel bitorsor. Selecting one lift from each fiber is different from
selecting lifts multiplicatively. The latter is the splitting problem.
The original source status remains unresolved as written; the replacement and
its interpretation are now settled.

## S2. Definition 3.24: explicit transported preferences

The source number is **Definition**, not Proposition, 3.24. Its numerical
security-value clauses were already well-defined. For the remaining clauses
use the following precise interpretation on common action labels:

* Exact preservation by pi: for every i and every pure profile s,
  `u_i(s)=u_{pi(i)}(P_pi s)`.
* Pure ordinal preservation by pi: for every i and every pair s,t,
  `u_i(s)≤u_i(t) iff u_{pi(i)}(P_pi s)≤u_{pi(i)}(P_pi t)`.
* Independent-mixed preference preservation by pi: for every i and every
  pair x,y in `product_j Delta(A_j)`,
  `U_i(x)≤U_i(y) iff U_{pi(i)}(P_pi x)≤U_{pi(i)}(P_pi y)`.
  Here U is expectation under the independent product law and P permutes the
  marginal laws. Quantification is over whole profiles, not only unilateral
  deviations and not over correlated joint laws.

In each clause require a transitive subgroup of preserving permutations for
“standard”, or all S_N for “fully”. These are precise replacements for the
source wording, not a claim to have recovered an unrecorded author intention.
For unequal or differently labeled strategy sets replace P by a specified
family of typed bijections; preference preservation alone supplies no such
family and does not supply coherence.

All three preserving sets are subgroups. Identity is immediate. For a product
of two preserving maps apply the first comparison, then the second, moving
the focal index and both profiles at each step. Invert the equivalence and
substitute inverse-transported profiles to prove closure under inverses.
Exact preservation implies independent-mixed preservation by linearity and
bijection of the finite summation indices. Independent-mixed preservation
implies pure preservation by Dirac marginals. Thus the corresponding standard
and full implications hold. No normative claim follows just from these names.

The converses fail. With two players and A={0,1,2}, put u_1(s)=s_1 and
u_2(s)=s_2². Swapping players preserves all pure orders, but not mixed orders:
compare player 1 choosing 1 surely with choosing 0 or 2 equiprobably, while
holding the opponent fixed. Player 1 is indifferent (expectation 1); the
transported player 2 prefers the lottery (expectations 1 and 2). With
u_1(s)=s_1 and u_2(s)=2s_2+1 the swap preserves mixed preferences but not
numerical utilities. Common cardinal scales cannot be inferred from ordinal
or expected-utility preference equivalence.

For clarity, a *different*, stronger variant permits every lottery over pure
profiles, including correlated lotteries. For nonconstant utilities its
preference-preserving transports are exactly positive affine utility changes.
Proof: let a,b be minimum/maximum-utility profiles. Every pure profile z is
indifferent to the lottery giving b probability
`(u(z)-u(a))/(u(b)-u(a))` and a otherwise. Transported indifference gives
`v(z)=v(a)+(v(b)-v(a))(u(z)-u(a))/(u(b)-u(a))`; preserved strict endpoint
order makes the slope positive. Linearity proves the converse. Constant
utilities correspond exactly to constant utilities. This argument uses
correlated profile lotteries and is not silently applied to the independent
mixed quantifiers above.

## S3. Geometry: specify and omit from the central argument

If retained as an illustration, take a Lebesgue-measurable planar shape X
with `0<area(X)<infinity`, partitioned into finitely many measurable pieces
R_i. Define G as the Euclidean isometries mapping X onto itself and permuting
the whole pieces. Say whether boundaries are assigned literally or pieces are
identified modulo null sets; either convention works if used consistently.
The induced color projection is a homomorphism. An isometry carrying R_i to
R_j preserves area, so transitivity implies `area(R_i)=area(R_j)` for all i,j.
For n≥2 the transitive action is nontrivial, hence G is nontrivial; for n=1
this conclusion fails (a single-color scalene triangle). A nontrivial kernel
on colors is an additional condition, not a consequence of transitivity.

These observations introduce no tool needed for the finite-game results.
Recommendation: omit the geometric formal definitions from the eventual
central paper; at most retain a short measurable equal-area illustration.
The current conservative manuscript is unchanged. The original definition
history and the n=1 counterexample remain in the audit notes.
