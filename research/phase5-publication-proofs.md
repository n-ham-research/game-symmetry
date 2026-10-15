# Automorphism lifting in finite symmetric games

Nicholas Ham. Research draft, 16 October 2026.

**Status.** The definitions and binary example belong to Ham (2021),
arXiv:1311.4766v5. The ternary classification, small nonsplit realization and
reduction results below are candidate contributions with novelty unresolved.
The ternary exhaustion uses a finite lemma with a fully specified verification
procedure; it is not presented as a computation-free proof. These statements
do not alter the existing manuscript.

## Definitions and the matching lemma

A finite game consists of players N={0,…,n−1}, nonempty finite strategy sets
A_i and real utility functions u_i:∏A_j→R. A typed bijection g=(p;(f_i)) has
p∈S_n and bijections f_i:A_i→A_{p(i)}. Its profile action is
(gs)_{p(i)}=f_i(s_i). Composition is right to left. An exact automorphism
satisfies u_{p(i)}(gs)=u_i(s) for all i,s. Write A=Aut(u) and q(g)=p.

A subgroup H≤A is strategy trivial if every element fixing a player acts
identically on that player's strategies. The game is **standard symmetric**
if such an H acts transitively on players. It has **full player image** if
q(A)=S_n. Its projection **splits** if a homomorphism σ:S_n→A satisfies
qσ=id. A section need not be strategy trivial.

A matching is a family of bijections t_i:B→A_i from one common strategy set.
Its lift of p has components t_{p(i)}t_i^{-1}. The game is **fully symmetric
under a matching** if all these lifts are automorphisms.

**Lemma 1 (Ham's matching lemma).** A player-transitive strategy-trivial
subgroup can be put into bare coordinate-permutation form by local strategy
labels. In particular a strategy-trivial full-image section exists exactly
when the game is fully symmetric under a matching.

**Proof.** Fix a reference player 0. For each i select h∈H with q(h)(0)=i and
let t_i=h_0. This does not depend on h: if k has the same target, k^{-1}h
fixes player 0 and has identity component there. For g∈H, compare g h with
an element carrying 0 to q(g)(i). Their components give
f_i t_i=t_{q(g)(i)}. Thus every component equals
t_{q(g)(i)}t_i^{-1}, the matching formula. Conversely matching lifts compose
as their player permutations and have identity components at fixed players.
This proves both assertions. ∎

## The binary three-player characterization

For binary strategies use common labels F_2 and z=(1,1,1). In the signed
S_3 action, a player permutation p sends s to P_p s+ε(p)z, where ε is parity.
Its focal-profile cells (s,i) have four orbits: all homogeneous cells, all
minority-player cells, and two cyclic orientations of majority-player cells.
Give these orbits utilities α,δ,β,γ, respectively. This is Example 5.13,
with interchange of β,γ permitted by reversal of the cyclic convention.

**Theorem 2 (individual-game formulation of Ham's binary classification).**
Every three-player binary game with full player image that is not fully
symmetric under any matching is isomorphic to this table with β≠γ. Such a
table has exact automorphism group the signed S_3 and is standard symmetric.

**Proof.** Identify local interchanges with V=F_2^3 and put K=ker q≤V.
Conjugation by lifts of player permutations permutes coordinates of V, so K
is S_3-invariant. Let E be the even-weight subspace. If K contains a
nonconstant vector, its sum with a transposed copy is a weight-two vector;
permuting coordinates generates E. It follows that K is one of
0,〈z〉,E,V.

If K=V, every utility is constant on profiles. Full player image makes their
constants equal, giving ordinary full symmetry. If K=E, write u_i(s)=h_i(t)
with t=∑s_j mod2. A transposition lift changes t by one constant c. At its
fixed player k, payoff preservation says h_k(t+c)=h_k(t). If c=1, h_k is
constant, and player transitivity makes every utility constant. Otherwise
all transposition lifts have c=0. They equate the h_i for swapped players;
thus all h_i agree, and bare player permutations preserve the game.

Suppose K=〈z〉. Any transposition lift squares to a base vector supported
only on its two moved coordinates; since this square lies in 〈z〉 it is
identity. For lifts t,u of adjacent transpositions, (tu)^3∈{1,z}. The
central element z commutes with every lift, and replacing t by zt toggles
this cube without changing t²=1. Hence t²=u²=(tu)³=1 can be achieved. The
presentation of S_3 supplies a section. If K=0, q itself is an isomorphism,
so there is already a section.

In any section the stabilizer of a player is C_2. Its action on that player's
two strategies is either trivial or the interchange, with the same choice
at every player by conjugacy. In the trivial case Lemma 1 supplies an ordinary
matching section. In the other case multiply every odd lift by the common
flip z in the ambient typed group. This is again a homomorphism, now strategy
trivial. Lemma 1 conjugates it to the bare permutations, so the original
section becomes the signed action. If K=〈z〉, z is itself an automorphism;
signed lifts then yield bare lifts too, giving full symmetry. Consequently a
non-full game has K=0 and exactly the signed S_3 group.

The four cell orbits give the displayed table, including all coincidences
among its four utility parameters. If β=γ, bare permutations preserve it.
If β≠γ, every nonhomogeneous profile has two majority-player utilities β,γ
that differ. Every profile in a full matching has equal utilities across
players: its lifts fix the profile and act transitively on players. A binary
matching must therefore be {000,111}. Its opponent transposition exchanges
β and γ, a contradiction. Thus precisely β≠γ gives the non-full case. ∎

This is a refinement of the quantifiers and proof of the prior classification,
not a claim to have discovered Example 5.13 or Figure 4 again.

## Three-player ternary classification

Let W=S_3^3⋊S_3 and fix r=((012);id,id,id). For a strategy transposition h set

    H_h={(p;(h^{ε(p)},h^{ε(p)},h^{ε(p)})): p∈S_3},
    L={(p;(f,f,f)): p,f∈S_3, ε(p)=ε(f)}.

The orbit-closure construction below is the prior covering-group principle;
see Cao–Li–Tan–Yang, *On group structures of strategic-form games*, Lemma1
and Theorem3 ([primary text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11197539/)),
and their attribution to Peleg–Rosenmüller–Sudhölter, Corollary3.20.
For B≤W let cl(B) consist of all typed bijections preserving each individual
B-orbit on the 81 focal-profile cells. If B≤Aut(u), then cl(B)≤Aut(u), because
u is constant on every such orbit. Distinct values on the orbits conversely
realize cl(B) as the complete automorphism group. This last statement is a
realizability assertion, not an assumption that every subgroup is realizable.

**Finite lemma 3.** For every odd-player g∈W, B=〈r,g〉 has a section of its
player projection. Either cl(B) contains a full matching section, or
B=H_h for one of the three strategy transpositions h. Each H_h is orbit
closed and contains no full matching section.

**Complete finite verification specification.** Represent every permutation
by its image tuple. For (p;f) and (q;k) use multiplication

    (p;f)(q;k)=(pq;(f_{q(i)}∘k_i)_i).

Enumerate the six player permutations and the six choices independently for
each f_i. For each of the 3·6³=648 odd-player elements close {r,g} under
multiplication. Positive word closure gives a group because generators have
finite order. Deduplicate complete element sets. There are nineteen groups,
with order histogram 6:4,18:3,24:6,54:3,162:1,648:2.

For splitting inspect all pairs a,t in each group with q(a)=(012),q(t)=(12)
and verify a³=t²=1,tat=a^{-1}. At least one pair exists in every group.
There is no requirement that a=r. For closure compute the cell orbits by
applying the generators to (s,i), then inspect every element of W and retain
exactly those mapping every cell to its own orbit. Enumerate all36 matchings
by fixing t_0=id and choosing t_1,t_2∈S_3, and inspect their six lifts for
containment in the closure. Sixteen of the nineteen groups pass this test.
The remaining three element sets are exactly the displayed H_h; their
closures equal themselves and their cell-orbit counts are fifteen.

These bounded instructions specify every input, stopping rule and verification
predicate without reliance on a particular program. The supplementary record
[phase5-ternary-audit.md](phase5-ternary-audit.md) reduces them by conjugacy to
32 lift representatives and 11 generated-group classes and provides an
independent implementation. The finite lemma remains a finite exhaustion;
its table is not claimed to be established by a symbolic argument alone.

**Theorem 4 (ternary splitting and non-full mechanisms).** Every standard
three-player ternary game with full player image has a section. If it is not
fully symmetric under any matching, its complete exact group is conjugate
to H_h or L, of orders six and eighteen, respectively. Both mechanisms occur.

**Proof.** Lemma 1 puts a transitive strategy-trivial subgroup into bare form.
Every transitive subgroup of S_3 contains its three-cycle subgroup, so we may
assume r∈A. Full player image supplies an odd g∈A. The section of 〈r,g〉 in
Lemma 3 is also a section inside A.

If A is non-full, apply the second assertion of Lemma 3 to every odd g∈A.
Every such g lies in some H_h, hence has the same transposition at all three
strategy components. Fix one odd t∈A. For any even a∈A, both at and t have
common odd local maps; therefore a=(at)t^{-1} has a common even map. It follows
that A≤L. Its kernel lies in diagonal A_3, so is trivial or all of A_3. Full
image gives |A|=6 or18. In the first case A=〈r,g〉=H_h; in the second A=L.

The distinct-orbit-value construction realizes H_h by Lemma 3; the next
proposition realizes L. Both contain bare A_3 and sections H_h. Neither has a
strategy-trivial full-image section: a player transposition fixes a player,
whereas its local map at that player must be an odd, nonidentity permutation.
This also proves non-full symmetry. ∎

**Corollary 5 (preference conventions).** Theorem 4 holds separately for the
cardinal and ordinal automorphism groups of a finite game. Cardinal means
playerwise positive affine transport; ordinal means preservation of the
complete pure-profile utility preorder, including ties.

**Proof.** Replace each nonconstant u_i by
c_i=(u_i−min u_i)/(max u_i−min u_i), and replace constants by zero. Positive
affine transport is equivalent to exact equality of these normalized tables.
Alternatively replace each attained utility level by its increasing rank
starting at zero, yielding r_i. Order transport is equivalent to exact equality
of ranks. Thus Aut_card(u)=Aut(c) and Aut_ord(u)=Aut(r) as literal subgroups
of the same W. Apply Theorem 4 to these tables with the corresponding
standardness and full-image hypotheses. ∎

## A common-interest realization and a reduction obstruction

**Proposition 6.** For three players on {0,1,2}, give every player payoff
v(s)=0 on repeated labels, and otherwise the sign of the permutation s of
(0,1,2). Its complete exact group is L. It has no full-payoff strategy clones
and cannot reduce to non-full Example 5.13 through any sequence of exact
isomorphisms, rectangular restrictions and full-payoff clone quotients at
fixed player count.

**Proof.** Suppose (p;(f_i)) preserves the game. If f_j(a)≠f_k(a), put a in
coordinates j,k and choose the third action with image the unused label.
The source payoff is zero and its image nonzero, a contradiction. Thus all
f_i equal a common f. The orientation changes by sign(p)sign(f), proving
Aut(v)=L. Its splitting and non-full properties follow as in Theorem 4.

For distinct a,b at a chosen coordinate, complete a with the other two labels.
The payoff is ±1; replacing a by b makes it zero. This excludes clones.
All three permitted operations preserve equality of all focal utilities.
Non-full Example 5.13 has unequal majority payoffs β≠γ, so cannot be a result
of such operations. Moreover Theorem 2 implies every binary rectangle of v
with full player image is full: the only binary non-full mechanism is not
common interest. This gives a minimal witness under these reductions within
three players; player deletion and utility changes are separate operations. ∎

## A four-strategy nonsplit realization

**Theorem 7.** Three players with four strategies each admit a standard game
with full player image and nonsplit projection, even with utilities in {0,1}.
Four is minimal among equal strategy counts for three players under these
hypotheses, for exact, cardinal and ordinal symmetry separately.

**Proof.** Use players Z/3 and strategies Z/4, represented by 0,1,2,3. Set
F(d,e)=1 when d<e and d≤1, and zero otherwise. For
 d=s_{i+1}−s_i, e=s_{i+2}−s_i modulo4, put

    u_i(s)=F(d,e) if s_i is even, and F(e,d) if s_i is odd.

Writing T_k(a)=a+k modulo4, the following group preserves u: even player
permutations preserve cyclic opponent order; odd ones reverse it; T_k changes
the focal parity exactly when k is odd. Hence

    G={(p;(T_k,T_k,T_k)): k mod2=ε(p)} ≤ Aut(u).

Its profile orbits have representatives 000,001,002,003,012,021, sizes
4,12,12,12,12,12 and utilities respectively
(0,0,0),(1,0,0),(1,0,0),(1,0,0),(1,0,0),(0,0,1).
For repeated-action profiles the difference of their two labels distinguishes
the three orbits. A nonzero translation cannot preserve a three-element
subset of Z/4, and the two displayed all-distinct representatives cannot be
related with translation zero and an even player permutation. Stabilizers in
all five nonconstant orbits are trivial, verifying the sizes and exhaustion.
Thus the simultaneous zero locus is exactly the diagonal.

Any automorphism therefore has one common local permutation f. At a profile
with repeated a and different b, exactly one repeated-action player wins.
It is the one whose next cyclic neighbor has action a when a is even, and
whose previous neighbor has action a when a is odd. Transport forces
parity(f(a))=parity(a)+ε(p). For even p the only possibilities are
id,T_2,−a,2−a. The last two send the player-zero payoff at 012 from one to
zero (to profiles032 and210), and even player permutations do not change
cyclic orientation. Hence f=id or T_2. For odd p divide by a known odd/T_1
lift and reduce to the even case, giving f=T_1 or T_3. This proves Aut(u)=G.

Bare A_3 supplies standardness, and every player permutation has a lift. The
kernel consists of id,T_2. Every transposition lift squares to T_2≠id;
a section would send that transposition to an involution, so is impossible.

For three or fewer strategies Theorem 4 gives a section; for one or two
strategies embed the typed group into W by fixing added labels and apply
Lemma 3 to its normalized standard cycle and an odd lift. Its section remains
inside the embedded original subgroup. Finally all players attain both zero
and one, so cardinal and ordinal normalizations leave this witness unchanged;
Corollary 5 proves the corresponding lower bounds. ∎

## Mechanisms and reductions

The signed binary group, L and G have player kernels 1,C_3,C_2, and only G is
nonsplit. They are distinct represented player projections. Nevertheless the
common restriction {0,1} of the last game is exactly Example 5.13 with
α=γ=δ=0,β=1, by substituting its eight profiles. Structural inequivalence does
not imply irreducibility under restrictions that acquire new automorphisms.

The rigorous preservation framework, including the canonical clone quotient
with multiplicities and a separate definition of player deletion, is in
[phase5-reductions.md](phase5-reductions.md). The arbitrary-player binary
orientation realization and its proof are in
[phase5-mechanisms.md](phase5-mechanisms.md). The latter gives a four-player
ternary split non-full mechanism; the six-player boundary and general splitting reduction are stated below.

## Player counts and the first ternary nonsplitting example

**Theorem 8 (candidate extension).** A standard ternary game with full actual
player image has a section whenever the number of players is not divisible
by three. At three players it also has a section by Theorem4. Six players
are necessary and sufficient for a ternary nonsplitting example under these
hypotheses. Sufficiency holds with binary common-interest utilities.

The proof of the general assertion, including local affine coordinates,
classification of the local-sign kernel, explicit cocycle lifting and all
boundary cases, is given in [phase5-splitting.md](phase5-splitting.md),
P5-S4–S6. Its four-player conclusion has an additional independently verified
finite proof. The six-player construction and its standalone theorem/proof
are in [phase5-six-player-obstruction.md](phase5-six-player-obstruction.md). Both documents use the
definitions above and specify precisely which finite verifications remain
essential. Combining those results with n=1 triviality and the fact that at
n=2 standardness already supplies a full strategy-trivial section proves the
minimum-player statement. For the six-player game no matching is possible,
because every matching would supply a section. Its known triple-cover group
is prior algebra, with the game realization and minimality treated as candidate
applications. A complete classification of four-player ternary mechanisms or
of ternary nonsplitting at other multiples of three is not claimed.

For completeness, the binary-complement normalization used in Theorem8 has
an elementary transport proof. Let χ_i(p)∈F2 be the local sign of a section
above p. Choose player permutations t_i carrying0 to i and put a_i=χ_0(t_i).
On the stabilizer of0 let φ(h)=χ_0(h); this is a homomorphism
S_(n−1)→C2, hence zero or parity. The component composition rule gives

    χ_i(p)=a_i+a_{p(i)}+φ(t_{p(i)}^{-1} p t_i).

If φ=0, local sign relabeling by a_i removes all signs. If φ is parity,
put a'_i=a_i+ε(t_i); the formula becomes
χ_i(p)=ε(p)+a'_i+a'_{p(i)}. Relabeling by a'_i leaves exactly the common
parity sign. Thus the induced translation module is the ordinary permutation
module or its scalar parity twist, as used in the direct-summand argument.
