# Phase 3: binary player-permutation symmetry and pure equilibria

**Status:** candidate extension, complete proof supplied below; novelty not
established. The original question is Ham's. The ordinary fully symmetric
binary equilibrium theorem is prior literature, not a new claim here.

## The exact original question

Ham, *Notions of Anonymity, Fairness and Symmetry for Finite Strategic-Form
Games*, arXiv:1311.4766v5 (2021),
`section-label-independent-symmetric-games.tex`, lines 464–466, asks whether
Cheng et al.'s pure-equilibrium result weakens to “n-transitively standard
symmetric 2-strategy games.” The source is the locally inspected original
source archive; its provenance is pinned in `original-record.json`.

The hypotheses mean **both** of the following:

- the actual player projection of the exact automorphism group is all of S_n;
- some strategy-trivial subgroup of that automorphism group is player transitive.

They do not require the full-player-image subgroup itself to be strategy
trivial. The second condition alone does not guarantee a pure equilibrium.
No conditions on preferences beyond arbitrary real, finite-game payoffs are
added below. Each player has exactly two pure strategies.

## Results

**P3-E1 (candidate extension).** Every finite binary n-transitively standard
symmetric game is an **exact potential game**. Consequently it has a pure
Nash equilibrium and every sequence of strict unilateral improvements is finite.

In fact the following stronger statements hold.

**P3-E2 (candidate extension).** Every binary game with n >= 3 and surjective
actual player projection Aut(Gamma) -> S_n is an exact potential game, whether
or not it is standard symmetric. For n >= 5 it is fully symmetric up to exact
strategy relabeling. For n = 4, it is either fully symmetric up to relabeling or
each player's payoff is independent of that player's own action. In the latter
case **every** pure profile is a Nash equilibrium. For n = 3, the only additional
case needed in the proof is a signed S_3 action, with the explicit potential
below.

**P3-E3 (candidate extension).** A binary n-transitively standard game is fully
symmetric up to relabeling for every n >= 4. Thus three players are the only
possible degree of a non-fully-symmetric n-transitively standard binary game.
Ham's Example 5.13 already supplies that three-player separation.

An exact potential is a function Phi on pure profiles satisfying
Phi(s'_i,s_-i)-Phi(s_i,s_-i) = u_i(s'_i,s_-i)-u_i(s_i,s_-i).
A global maximizer of this finite function is a pure Nash equilibrium. This
also gives the strict-improvement conclusion. Local action and player
relabelings preserve the property by transporting Phi.

## Proof

Conventions throughout: (P_p s)_j = s_{p^{-1}(j)}; compose right to left.
Identify binary strategies with F_2. A typed bijection is represented by
(b,p), acting as b + P_p s, with multiplication
(b,p)(c,q) = (b + P_p c,pq). Let V=F_2^n, z=(1,...,1),
T=<z>, E={b:sum b_i=0}. Put G=Aut(Gamma) and K=ker(q).
The discussion below with n >= 3 is separate from the n=1,2 boundary cases.

### 1. The four possible kernels

K is an S_n-invariant subspace of V: it is a subgroup of the elementary
abelian flip group, and conjugation by any lift of p permutes its coordinates.
If K contains a nonconstant vector b, choose coordinates i,j with b_i != b_j.
Then b+P_(ij)b=e_i+e_j belongs to K. Conjugation gives every pair sum, whose
span is E. If K also has an odd-weight vector, then K=V; otherwise K=E.
If it contains no nonconstant vector, K is 0 or T. Thus the list is
0,T,E,V. For n=3 these four are distinct; for even n, T is contained in E,
which creates no extra case.

If K=V, every u_i is constant on all profiles; full player projection makes
these constants identical. If K=E, each u_i(s)=h_i(sum s mod 2). Full player
projection makes either all h_i constant or all nonconstant, because it
transports each h_i to some h_j with a possible parity switch. In the constant
case all constants coincide. In the nonconstant case, take a transposition
(ij) and a third player k. Any lift shifts total parity by epsilon. Because it
fixes player k, invariance gives h_k(t)=h_k(t+epsilon); nonconstancy forces
epsilon=0. The same lift now gives h_i=h_j. Hence all h_i are identical.
These games have common payoffs h(parity), are ordinarily fully symmetric,
and possess the common-payoff exact potential.

### 2. What a complement can do on binary strategies

Suppose H <= V semidirect S_n and q|_H is an isomorphism onto S_n.
For each player i, the action of H_i on its two strategies is a homomorphism
S_{n-1}->C_2. The only possibilities are trivial and sign (for n>=3);
conjugation makes the same alternative hold for every player. If trivial,
H is strategy trivial and the matching theorem (audited 4.23) supplies local
labels making H the ordinary diagonal S_n action.

If nontrivial, apply the group automorphism
J(b,p)=(b+sgn_2(p)z,p). The stabilizer actions of J(H) are now trivial,
because the sign of a permutation fixing i equals its sign in S_{n-1}.
By the same matching theorem, after local relabeling H is the **signed** action
s -> P_p s + sgn_2(p)z. Here sgn_2 is 0 on even permutations and 1 on odd ones.
The twist J is only an algebraic device: we do not assume it preserves game
payoffs. The conclusion concerns the original H after the corresponding
local relabeling; J commutes with such relabeling because z is central.

For n>=4, invariance under the ordinary A_n action already forces ordinary
S_n invariance on utility cells. Indeed, given an odd p and a cell (s,i),
among the n-1 opponent bits two agree. Their transposition r fixes s and i.
Then pr is even and takes (s,i) to exactly the same cell (P_p s,p(i)) as p.
Thus the even and full permutation groups have the same utility-cell orbits.
A game admitting either kind of complement is therefore fully symmetric up
to local relabeling when n>=4. If K=0, G itself is such a complement.

### 3. The global-complement kernel and Coxeter relations

Assume K=T. It is central. Every lift t of a transposition is an involution:
t^2 is a flip supported on the two swapped coordinates, but belongs to T;
for n>=3 the only such element of T is zero.

For lifts t,u of disjoint transpositions p,q, their commutator belongs to T.
The formula comparing tu and ut has flip part
(I+P_q)b + (I+P_p)c, supported on the four moved coordinates. Thus for
n>=5 it is zero: disjoint transposition lifts commute.

Choose lifts t_1,...,t_{n-1} of the adjacent transpositions. Their adjacent
braid defects are (t_i t_{i+1})^3=z^{d_i}. Replacing t_i by z^{a_i}t_i
changes d_i to d_i+a_i+a_{i+1}. Choose a_1=0 and recursively choose a_{i+1}
to make every defect zero. Involutions and the disjoint commutations persist.
All Coxeter relations now hold, giving a homomorphism S_n -> G whose
composition with q is the identity. This is a complement. For n>=5,
Section 2 proves full symmetry up to relabeling. For n=3 there are no distant
commutation relations, so the same adjustment gives a complement as well.
Because z is itself an automorphism, it cancels the global flip in each odd
signed lift if necessary. Therefore n=3,K=T games are fully symmetric up
to relabeling too.

For n=4, the commutator of lifts of disjoint transpositions is either 1 or z.
It is independent of lift choices. All pairs of disjoint transpositions are
conjugate under S_4, and conjugation fixes z; hence the same alternative holds
for every pair. If it is 1, the same Coxeter adjustment splits the extension,
and Section 2 gives full symmetry.

If it is z, every lift of a double transposition has square z: it is a product
of lifts of the two disjoint transpositions, times possibly z. In particular
no such lift has order 2. This excludes standard symmetry. To see this,
any player-transitive subgroup L <= S_4 has order divisible by 4. A Sylow
2-subgroup has order at least 4. If it contains an element of order 4, its
square is a double transposition. Otherwise it has a four-element elementary
abelian subgroup; either that subgroup already contains a double
transposition, or the product of two distinct commuting transpositions is
one. Thus L contains a double transposition. A strategy-trivial subgroup
projects injectively and preserves its order, contradicting the order-4
property of every lift. This proves P3-E3 at n=4.

### 4. The exceptional four-player case has no incentives

Continue with n=4,K=T and disjoint commutator z. Fix focal player i. For
an opponent transposition (jk), let ell be the remaining opponent and choose
the unique lift t_jk which flips i's bit (multiplication by z exchanges the
two possible lifts). The commutator with a lift of (i ell) is z. Looking at
the i,ell coordinates of the formula above shows that t_jk's flips on these
two fixed coordinates differ. It therefore fixes ell's bit. It is an
involution by Section 3.

Choose adjacent transpositions of the three opponents and their normalized
lifts. Their product has no flip on i, so its cube, which lies in T, cannot
be z. These two involutions therefore satisfy the S_3 Coxeter relations and
generate a subgroup projecting isomorphically onto the permutations of the
three opponents. Its action on each opponent's strategy set has trivial
point stabilizer: the stabilizer is generated by the transposition of the
other two opponents, whose normalized lift fixes this opponent's bit as
just shown. The matching theorem labels the three opponent strategy sets so
that this subgroup ordinarily permutes those bits. Meanwhile its odd
permutations flip i, because its two generating transpositions do so.

In any binary opponent triple two bits agree. Transposing those equal bits
fixes all opponents' actions and flips i's bit. Its exact game invariance
therefore gives u_i(s)=u_i(s with i flipped). This argument holds for each
focal i separately; it does not require the opponent labelings for different
focal players to agree. Every unilateral payoff change is zero, so the
constant function is an exact potential and every profile is an equilibrium.

### 5. The three-player signed case and boundaries

The sole remaining case is n=3,K=0 with the signed S_3 complement. The
ordinary A_3 subgroup and odd complemented permutations put the two
homogeneous profiles and their focal cells in one orbit, with payoff alpha.
Likewise all cells consisting of a nonhomogeneous profile and its unique
minority player form one orbit, with payoff delta.

When a majority player flips, both the original and resulting profiles are
nonhomogeneous. This change is exactly the action of the signed
transposition of the other two players: those two have different bits, so
swapping and complementing them fixes both, while the focal bit flips.
The focal utility is consequently unchanged. Minority flips move a profile
to homogeneous and change its payoff from delta to alpha. At a homogeneous
profile any flip changes alpha to delta. Thus

    Phi(s) = alpha if s is homogeneous, and delta otherwise

is an exact potential. The two homogeneous profiles are equilibria iff
alpha>=delta; all six nonhomogeneous profiles are equilibria iff delta>=alpha.
When alpha=delta every profile is an equilibrium. Majority-player payoff
levels need not coincide: this is not a common-interest assertion.

At n=2, standard symmetry itself supplies a strategy-trivial transitive
subgroup, necessarily projecting onto S_2, so the game is fully symmetric
up to relabeling. At n=1 every finite game has exact potential u_1.

Finally, for any ordinarily fully symmetric binary game write its focal
payoffs as v(a,k), with own bit a and k opponents playing 1. Set
D(k)=v(1,k)-v(0,k) and

    Phi(s) = sum_{r=0}^{|s|-1} D(r), with the empty sum zero.

A 0-to-1 deviation changes Phi by D(k), exactly the deviator's payoff change.
This supplies all the full-symmetry cases above and completes the proofs.

## Exact finite investigation

`experiments/phase3_equilibria.py` checks all full-player-image subgroups at
n=2,3 by an independent all-subgroups enumeration. At n=3 it cross-checks
that list against the kernel/quotient construction used at n=4. The n=4
construction covers every subgroup with full projection, by the four-kernel
classification: all binary complement characters and local relabelings;
all quotient cocycles modulo T from exact GF(2) Coxeter relations; both
homomorphisms S_n->V/E; and the full ambient group.

For each subgroup its utility-cell orbit partition describes **all real
payoff assignments** invariant under it. Formal integer coefficient vectors
around every two-dimensional face of the strategy cube test the exact
potential identity. Thus this check covers arbitrary payoff levels within
each finite domain, not random integer samples. Every full-image family at
n=3,4 passes. The n=2 matching-pennies family fails, as it should. Distinct
subgroups are coverage of representations, not counts of distinct games.
Some groups impose the same game family or force extra automorphisms; group
properties must not be substituted for properties of every invariant game.

The lists contain 5,15,35 subgroups at n=2,3,4. Canonicalizing the imposed
utility equality partitions under every typed player/strategy relabeling
leaves 4,5,5 equality families respectively. These families may overlap or
specialize to one another; these are not disjoint classifications of individual
games. JSON fields beginning `subgroup_has_` describe the enumerated group;
`family_forces_` and the payoff/potential fields describe all games invariant
under it. In particular a subgroup with no full matching can force additional
payoff symmetries, so its invariant games can still be fully symmetric.

Zero circulation on all square faces suffices for an exact potential: integrate
the unilateral payoff increments along a coordinate path from 0. Swapping two
adjacent distinct-coordinate steps changes its integral by the corresponding
square circulation, hence not at all. Canceling backtracking changes nothing
as well. The resulting path-independent integral has the required increment
on every edge. The formal coefficient test therefore checks the exact identity,
not just an implication toward existence of a pure equilibrium.

No finite computation is offered as proof at unbounded n; the proof above
is independent of those computations.

## Boundary counterexamples and interpretation

- **Standard symmetry alone is insufficient.** On three binary players in a
  directed cycle, let u_i(s)=1 iff s_i != s_{i+1}, indices modulo 3. Rotations
  are strategy trivial and transitive. A pure equilibrium would require every
  adjacent pair of an odd cycle to differ, impossible. Its player image is
  C_3, not S_3; thus it does not satisfy the original question's hypotheses.
- **Two players require the original standard condition.** Matching pennies
  has full player projection but has no pure equilibrium and is not standard.
- **More than two strategies changes the question.** Ordinary fully symmetric
  two-player rock-paper-scissors has no pure equilibrium. The proof uses the
  binary flip group and repeated opponent bits in essential ways.
- Full symmetry is sufficient but not necessary for exact potential or pure
  equilibrium. The signed three-player case and passive four-player case
  show structurally different reasons for existence. No symmetric mixed
  equilibrium theorem is used as a substitute for pure existence.

## Literature boundary

The inspected author-hosted primary paper [Cheng, Reeves, Vorobeychik and
Wellman, *Notes on equilibria in symmetric games*](https://strategicreasoning.org/wp-content/uploads/2016/12/notes-symetric.pdf)
proves the ordinary symmetric binary pure-equilibrium result. Ham explicitly
cites this and poses the weakening above. A bounded web search for
“n-transitively” with “Nash” located Ham's formulation, not an independent
settlement. This is not a comprehensive novelty search.

A readable author-uploaded primary draft is Cao and Yang,
[*Symmetric Games and Symmetry Groups*, July 29, 2015](https://www.researchgate.net/publication/280600867_Symmetric_Games_and_Symmetry_Groups),
uploaded by Cao on August 1, 2015. Its Definition 4 makes name-irrelevant
symmetry the full-image condition; Definition 6 makes renaming symmetry
ordinary full symmetry after local strategy bijections. Thus renaming symmetry
corresponds to audited full symmetry here, not merely Ham's standardness.
Proposition 4 establishes binary exact potential for renaming symmetry and
cites Hofbauer--Sorger (2002), Section 4.2.2, for the ordinary special case.
Its limitation for name-irrelevant symmetry uses two-player matching pennies.
The present n>=3 result avoids that boundary; this comparison establishes a
precise difference in assumptions, not novelty. The 2015 draft is not the
final 2018 article, whose body still requires comparison. The results remain
candidate extensions despite the complete internal proofs.
