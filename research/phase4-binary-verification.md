# Phase 4: adversarial reconstruction of binary exact-potential theorem

**Status:** independent internal reconstruction of candidate extensions P3-E1,
P3-E2 and P3-E3; proof withstands the attacks described below. This is not a
novelty conclusion or external peer review. No manuscript changes are proposed
by this report.

## Scope and independence

This worker was assigned a fresh adversarial reconstruction, not a request to
approve the preceding review. I first fixed the binary affine action and
reconstructed the invariant-kernel and lift arguments, then read the existing
`phase3-equilibria.md` proof to target its exceptional cases. I did not read
Phase 3 agent review reports before this reconstruction. Subsequently I read
the beginning of the Phase 3 computational implementation to identify its
coverage boundary. The new solver below imports none of that implementation:
it treats **all four kernels by the same symbolic presentation solver**, rather
than using complement-character representatives for the zero-kernel case.
The arguments necessarily share standard group facts and the existing proposed
theorem. Shared model and repository access limit independence.

The permutation convention is `(P_p s)_j=s_{p^{-1}(j)}` and composition is
right to left. A typed binary strategy bijection is `(b,p)` acting by
`b+P_p s`, with `(b,p)(c,q)=(b+P_p c,pq)` over F2. The group in the theorem is
the **actual** exact game-automorphism group, with its actual projection to
players, not an abstract group isomorphic to a player-transitive group.

## Reconstructed claim and limits

For n>=3, full actual image S_n implies exact potential. For n>=5 it implies
full symmetry after local relabeling. For n=4 either this full symmetry holds
or every player is indifferent to their own action at every opponent profile.
For n=3 the only extra case necessary is a signed S3 complement. Standardness
is unnecessary for the potential assertion at n>=3. With standardness added,
full symmetry follows for every n>=4. At n=2 standardness is essential;
matching pennies is a counterexample to the stronger image-only claim.

These are candidate extensions, whereas Ham's question and Example 5.13 are
prior work. The ordinary fully symmetric binary potential case is established
literature as recorded in the source ledger. This worker inspected no new
primary literature and makes no additional priority claim.

## Attack 1: could there be an omitted binary kernel?

Let V=F2^n and K=G intersect V. Conjugation by a lift of p sends b to P_p b,
so surjectivity makes K an S_n-submodule of V. If it contains a nonconstant
vector b, select coordinates with unequal bits. Then `b+P_(ij)b=e_i+e_j` is
in K. Conjugates span the even-weight subspace E. A vector outside E then
makes K=V. If there is no nonconstant vector, K is 0 or T, where T is the
span of all ones. Therefore exactly `0,T,E,V` need be considered for n>=3.
This proof includes even n, where T is contained in E; it does not silently
assume a direct sum or complete reducibility in characteristic two.

For K=V every utility is constant; full player image equates the constants.
For K=E each utility is a function h_i of total parity. If one is constant,
player transitivity makes all constant and equal. Otherwise all are
nonconstant. A transposition has a fixed third player, so any lift of it must
preserve parity (otherwise it equates that player's two values). The same
lift equates h_i and h_j. All h_i are therefore identical, yielding an
ordinary symmetric common-payoff game. This closes both large-kernel cases.

**Verdict:** no missing module, including n=3 and even n.

## Attack 2: could a complement have an unaccounted local action?

A complement H projects isomorphically to S_n. Its stabilizer of player i
acts on that player's binary strategies through a homomorphism
`S_(n-1) -> C2`. For n>=3 it is either trivial or sign. This includes
S2 at n=3; there is no exceptional extra character. Conjugation transports the
same character to every player.

Here is a direct justification for the coherent-label step. If all point
stabilizers act trivially on their own fibres, choose a reference player and
an element carrying it to each player. Transport its two labels using these
elements. A different chosen transport differs by a reference stabilizer and
therefore gives the same labels. Every H-element then transports equal labels,
so these local labels turn H into the ordinary permutation action.

For the nontrivial character apply the ambient group automorphism
`J(b,p)=(b+sign(p)z,p)`. It cancels each stabilizer character. Its transport
argument gives, after local relabeling, the signed action
`P_p s+sign(p)z`. J is **not** asserted to preserve utility. It commutes with
local flip conjugations because z is central, so undoing J proves the stated
normal form for the original H.

For n>=4 even permutations already have exactly the ordinary S_n orbits on
utility cells `(i,s)`: an odd p can be replaced by pr, where r transposes two
equal opponent bits and fixes i. Then r fixes the cell and pr is even.
Consequently either complement type forces ordinary full symmetry after
local labels. The repeated-bit argument requires n-1>=3; applying it at n=3
would be false and would erase Example 5.13.

**Verdict:** normal-form argument valid; the n=3 exception is essential.

## Attack 3: could Coxeter lift relations fail at n>=5?

Assume K=T. A transposition lift t has square with flip support contained in
its two moved coordinates. Its square also lies in T. At n>=3 these facts
force `t^2=1`. For disjoint transposition lifts t=(b,p), u=(c,q), comparing
tu and ut gives the difference
`(I+P_q)b+(I+P_p)c`. Its support is contained in the four moved coordinates.
It belongs to T, and hence is zero when n>=5. Thus distant adjacent lifts
commute. This argument is not valid at n=4.

Choose adjacent lifts t_a. The remaining Coxeter relators are
`(t_a t_(a+1))^3=z^d_a`. Replacing t_a by `z^c_a t_a` changes d_a to
`d_a+c_a+c_(a+1)`. Solve these equations successively along the adjacent
chain. The adjustments preserve involutions and distant commutations because
z is central. The resulting lifts satisfy the complete Coxeter presentation
of S_n; their generated group maps isomorphically to S_n. In particular one
must check all distant commutations, not just adjacent braid relations.
The complement argument proves full symmetry.

At n=3 there are no distant commutations. The same adjustment constructs a
complement. If it is signed, z in G cancels the flip in every odd lift, again
forcing full symmetry after labels.

**Verdict:** the support cutoff n>=5 is correct and the splitting proof does
not omit a presentation relation. No assertion that all central extensions
of S_n split is being made.

## Attack 4: the four-player exceptional extension

At n=4 a distant commutator can be z. Changing a lift by z does not change the
commutator, and conjugacy of pairs of disjoint transpositions makes the
alternative uniform. If all such commutators are trivial, the preceding
Coxeter adjustment splits the extension.

Suppose instead they are z. Fix focal player i, and an opponent transposition
(jk). Normalize its lift t to flip i. Let ell be the remaining opponent and
u a lift of (i ell). The i-coordinate of the difference between tu and ut
is `b_i+b_ell`, where b is t's flip vector. Since this difference is z,
`b_i+b_ell=1`; normalization gives `b_ell=0`. Thus t fixes the other
opponent's strategy, while flipping i. Its two swapped-coordinate flips are
equal because t is an involution.

Take two adjacent transpositions of the three opponents, with those normalized
lifts. Their product does not flip i. Its cube projects to the identity and
belongs to T, but has zero i-flip, so its cube is the identity. The two lifts
are therefore an S3 complement on the opponent players. The nontrivial
stabilizer of any opponent is the normalized lift of the transposition of
the other two opponents; the calculation just made says it fixes that
opponent's strategies. The direct coherent-label argument in Attack 2
therefore labels the opponent fibres so that this S3 acts ordinarily on
them. Odd elements still flip the focal bit.

For any opponent triple, two labeled bits agree. Their transposition fixes
that triple and flips i. Exact invariance forces u_i to be independent of
its own bit. This is a separate argument for each i; simultaneous global
opponent labels are unnecessary. Every deviation gain is zero, so constant
potential works and every pure profile is an equilibrium.

For P3-E3, every lift of a double transposition squares to z, because it is
a product of two anticommuting involutory lifts of its disjoint factors.
Any transitive subgroup L of S4 has order divisible by four and contains a
double transposition: a Sylow 2-subgroup has order at least four; an element
of order four squares to a double transposition, and otherwise two independent
commuting involutions include a double transposition or multiply to one. A strategy-trivial group injects
into its player image and preserves orders, contradicting these order-four
lifts. Thus this exceptional case cannot be standard symmetric.

**Verdict:** the exceptional four-player proof survives. The key local
normalization and cube calculation are both necessary; central-extension
splitting cannot substitute for this argument.

## Attack 5: the three-player signed payoff calculation

Only n=3,K=0 with a signed complement remains outside the ordinary symmetric
cases. Signed S3 puts all focal cells at the two homogeneous profiles in one
orbit, with utility alpha. It puts minority-player cells in one orbit with
utility delta. A majority player's bit flip is itself realized, at that
profile and focal player, by the signed transposition of the other two
players: their unequal bits are fixed by swapping and complementing. This
deviation has zero gain. A minority flip goes to a homogeneous profile, with
gain alpha-delta; the reverse gain is delta-alpha.

Consequently `Phi(s)=alpha` on homogeneous profiles and `Phi(s)=delta`
otherwise is an exact potential. The other payoff parameters need not
coincide: claiming common payoff would be an error. This proves the signed
case for every real payoff specialization, not just injective parameter
assignments. Equality alpha=delta correctly makes all profiles equilibria.

At n=2 a strategy-trivial transitive subgroup already projects onto S2 and
labels the game ordinarily symmetrically. At n=1 the utility itself is an
exact potential. For any ordinarily symmetric binary game, writing v(a,k)
for own bit and opponent-one count gives the potential with increment
`v(1,k)-v(0,k)` between population counts k and k+1.

**Verdict:** the original binary standard-plus-full-image question has an
affirmative answer including all low-player boundaries.

## Independent exact computation through six players

Files:

- `experiments/phase4_binary_verification.py`
- `experiments/phase4-binary-results.json`
- `experiments/test_phase4_binary_verification.py`

For each K in `0,T,E,V`, a full-image subgroup containing K projects modulo
K to the graph of a cocycle `S_n -> V/K`. Conversely each such graph lifts
to exactly one subgroup with kernel K. Assign arbitrary quotient-valued
flips to the n-1 adjacent generators and impose the involution, all distant
commutation, and adjacent braid relators. These are homogeneous linear
conditions over F2. Exact RREF enumerates the entire solution space. This
covers every actual embedded full-image subgroup; it is not a search over
random generators or merely conjugacy-class representatives.

For each solution, union-find on utility cells using the generators and K
computes its exact orbit partition. Each orbit receives an independent
formal real utility symbol. Every two-coordinate square is checked by an
integer coefficient vector, so the check covers **every real invariant
payoff assignment**. Vanishing squares imply a global exact potential by
path integration on the cube: adjacent step swaps preserve the integral,
and backtracking cancels. Full matching is checked separately by testing
all 2^(n-1) local label choices against all adjacent player permutations.

| Players | Kernel 0 groups | Kernel T groups | Kernel E groups | Kernel V groups | Total | Potential families | Families forcing some full matching |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3 | 8 | 4 | 2 | 1 | 15 | 15 | 11 |
| 4 | 16 | 16 | 2 | 1 | 35 | 35 | 27 |
| 5 | 32 | 16 | 2 | 1 | 51 | 51 | 51 |
| 6 | 64 | 32 | 2 | 1 | 99 | 99 | 99 |

These counts are embedded subgroup counts and invariant-family checks,
**not** counts of different exact game-automorphism groups or disjoint
individual-game classes. In particular an invariant game can acquire extra
automorphisms. The eight nonmatching n=4 families are all own-action
indifferent. The four nonmatching n=3 families are precisely local label
versions of the signed case. The n=3,4 subgroup totals agree with the
previous exhaustive search, now using a separate solver. The new n=5,6
checks extend the computational coverage but do not prove the unbounded
claim; Attacks 1–5 provide that proof.

Six focused tests pass (including the ternary cross-check below). The square test rejects both unconstrained utility
cells and the two-player matching-pennies symmetry family. The RREF routine
is checked against direct exhaustive assignments in a separate small linear
system. The saved-data test reruns every n=3,4,5,6 family. An initial test
compared integer dictionary keys with JSON string keys and was repaired;
this was a serialization-test issue, not a mathematical discrepancy.

## Review conclusion

No counterexample or proof defect was found in P3-E1, P3-E2 or P3-E3. The
four-player opponent-label argument is the least immediate step and has now
been expanded above without appealing to an unproved exceptional-case
classification. The n>=5 central-kernel proof is genuinely a bounded-support
and presentation argument, rather than extrapolation from n=3,4. Source
comparison and novelty assessment remain separate, unresolved tasks.


## Independent ternary cross-review

After completing the binary work, this worker was asked to review P4-M2 and
an independent worker's three-player, three-strategy certificate. This later
review was supplied the proposed orientation construction and the completed
certificate; it is a cross-review, not an initial blind derivation.

For the common utility F that is zero on repeated-action profiles and +/-1
on even/odd permutations of (0,1,2), the zero-locus argument forces all three
local strategy maps to coincide. Indeed, unequal images of a common repeated
action in two coordinates can always be completed to an all-distinct image
using the remaining coordinate. This would send a zero to a nonzero value.
A common map f then changes orientation by sign(f), and the player permutation
p by sign(p). Hence exactly pairs with equal sign preserve F. The group has
order 18, kernel diagonal C3, bare A3 rotations, and a section obtained by
using one fixed common strategy transposition for odd p. No strategy-trivial
section exists: a player transposition fixes a player but requires an odd,
nonidentity common strategy map on that player's actions. The game is
standard, full-image and non-full. This confirms P4-M2 independently.

Common payoff is preserved by exact rectangular restrictions, exact
isomorphisms and full-payoff-factor clone quotients. For the quotient case,
surjectivity of every coordinate map makes equality of the pulled-back
utilities imply equality on every quotient profile. Non-full 5.13 with
beta!=gamma is not common-payoff. Consequently no finite composition of
these reductions takes the orientation game to such a 5.13 specialization.
This is a rigorous counterexample for that specified reduction system,
not for reductions permitting player-specific utility transformations.

`experiments/phase4_ternary_crosscheck.py` reconstructs all 1296 typed actions
as permutations of the 81 utility cells. It imports **none** of the original
ternary certificate generator or earlier finite-group code. It independently
closes every one of the 648 odd lifts with the bare player three-cycle,
recovers exactly 19 different groups, checks every listed group element set,
checks every section witness, and recomputes each utility-orbit closure and
full-matching verdict. The group-order histogram is
`6:4, 18:3, 24:6, 54:3, 162:1, 648:2`. The same checker computes the
orientation game's exact order-18 automorphism group directly from F.

The exhaustion implication is sound: standardness supplies a strategy-trivial
transitive subgroup, and its three-cycle becomes bare after coherent local
labels. Full actual image then supplies an odd lift. Every game satisfying
both hypotheses therefore contains one of the 19 certified groups. All 19
contain an S3 section, so every such three-player ternary game has split
projection. This proves the three-strategy boundary computationally with a
fully finite certificate; it is not merely failure to find a counterexample.

For a non-full game, every subgroup generated by that bare cycle and an odd
lift must be one of the three exceptional twisted sections, because every
other orbit closure contains a full matching and hence forces full symmetry
on every invariant game. Their odd elements are exactly the odd elements of
the common-map sign fibre-product group. Fix one odd lift t. Every k in the
actual player kernel gives an odd element kt in that same set, forcing k
into the common diagonal A3. Thus the actual group has kernel 1 or C3, and
order 6 or 18. This last argument uses the actual full group, rather than
incorrectly identifying a generating subgroup with the full group.
