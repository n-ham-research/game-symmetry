# Exact reductions and inherited symmetry

Status: **candidate framework and elementary preservation propositions**.
Novelty is unresolved. Games are finite, all strategy sets are nonempty, and
utilities are retained exactly. An automorphism g=(p;(f_i)) satisfies
u_{p(i)}(g s)=u_i(s), where (g s)_{p(i)}=f_i(s_i). Composition is right to left.
The group under discussion is always the complete exact automorphism group.

## Three different objects

A numerical game, its represented player projection q:Aut(u)→S_n, and a
specified symmetry subgroup are different objects. Exact isomorphism retains
all three when the subgroup is transported. A reduction of payoff tables
need not retain their complete represented groups. We therefore record both
the inherited group and the complete group after every reduction.

Write I for full player image, C for existence of a section of q, M for a
strategy-trivial full-image section, and S for existence of a player-transitive
strategy-trivial subgroup. Here strategy trivial means that an element fixing
a player acts identically on that player's strategy set. Thus M⇒C⇒I and M⇒S;
C⇒S follows by using an n-cycle in the section (n=1 is immediate). The
matching theorem identifies M with full symmetry under some matching.

## Rectangular restrictions

Choose nonempty B_i⊆A_i. Let

D_B={g∈Aut(u): f_i(B_i)=B_{p(i)} for every i}.

Restriction defines a homomorphism D_B→Aut(u|B) preserving the actual player
permutation. Its kernel consists of elements acting identically on the
restricted typed sets; this kernel cannot change the player permutation.
The image need not be the complete automorphism group of the restricted game.

**Proposition R1.** If D_B contains a subgroup witnessing any of I,C,M,S,
then u|B has that property. In particular a section remains a section after
restriction, since its player projection remains injective. A strategy-trivial
subgroup remains strategy trivial, since an identity map restricts to identity.
There is no analogous argument transporting nonsplitting or absence of M:
new automorphisms can appear, and restriction can kill strategy actions.

**Proof.** Restrict each component and substitute profiles in ∏B_i into the
original payoff identities. Composition commutes with restriction. The
resulting subgroup has the same player image. For a section, any element
killed by restriction has identity player permutation and was already identity
in the section. The fixed-player identity condition is preserved. ∎

An arbitrary rectangle need not preserve I or S: the Phase 4 exact census of
the four-action witness has 210 of its 216 binary rectangles lacking both.
Even equal-size restrictions can lose full symmetry. Take the two-player,
three-action common-interest game given by the symmetric matrix

    [[1,2,3],[2,4,5],[3,5,6]].

Restrict rows to {0,1} and columns to {1,2}, giving [[2,3],[4,5]]. A player swap up to local bijections
would require its off-diagonal entries to agree after suitable row/column
bijections; with four distinct entries, the transpose's cell permutation would
have to fix every cell, which a typed player swap cannot do on a 2×2 rectangle.
Thus its player image is trivial. The source is ordinary fully symmetric.

For an inherited-full-image restriction require q(D_B)=S_n, or retain an
explicit full-image H≤D_B. For an inherited-standard restriction separately
require a transitive strategy-trivial subgroup in D_B. The first requirement
alone does not imply the second. Allowing arbitrary rectangles and then
computing Aut(u|B) is a different reduction relation, admitting emergent
symmetry. Neither convention should be silently substituted for the other.

## Canonical full-payoff clone quotient

For a,b∈A_i define a∼_i b if

    (u_j(a,s_{-i}))_j = (u_j(b,s_{-i}))_j for every s_{-i}.

This is an equivalence relation, invariant under every exact automorphism.
Let Q_i=A_i/∼_i and let v be the unique game satisfying u_j(s)=v_j([s]).
Equality for all single-coordinate replacements makes this factorization
well defined. Quotienting successively by arbitrary full-vector clone
relations reaches this same maximal clone-free quotient, up to exact
isomorphism: a pair of distinct classes becoming clones would already have
been clones before quotienting, by surjectivity in all opponent coordinates.
Thus this quotient supplies a canonical, nontrivial first reduction step.

Set m_i(c)=|c| for c∈Q_i, and define the multiplicity-preserving subgroup

D={ (p;(h_i))∈Aut(v): m_{p(i)}(h_i(c))=m_i(c) for all i,c }.

**Proposition R2.** There is a split exact sequence

    1 → ∏_{i,c} Sym(m_i(c)) → Aut(u) → D → 1.

The map to D preserves the player permutation. Consequently Aut(u) has each
of I,C,M,S if and only if D does. Each of these four properties of Aut(u)
therefore passes to Aut(v), but a converse requires control of multiplicities.
If all fibre sizes are the same, D=Aut(v), so the four properties are
preserved in both directions, including splitting versus nonsplitting.

**Proof.** Automorphisms carry clone classes onto clone classes, preserving
sizes, so induce elements of D. A kernel element fixes every player and
class and is precisely an arbitrary permutation inside each class. Conversely
number the members of every class from 1 to its size. Lift h∈D by sending the
k-th member of c to the k-th member of h_i(c). These lifts preserve u by the
factorization, compose exactly, and induce h, giving a section onto D.
Their player projection is unchanged. A section, or transitive
strategy-trivial subgroup, in Aut(u) descends with the same player image;
a section's injectivity follows from its player projection. Conversely the
number-preserving lifts retain the fixed-player identity condition and lift
all four properties from D. Inclusion D≤Aut(v) proves the forward assertions.
Uniform fibre sizes give D=Aut(v). ∎

The correct inherited object for a clone quotient is therefore the quotient
**with its multiplicities**, or equivalently D. Discarding this data can
create new symmetries. Uniform strategy cloning is harmless for I,C,M,S;
nonuniform cloning must be assessed using D, rather than declared harmless.
This makes the framework less restrictive than banning all cloning, while
retaining an exact preservation theorem.

## Player deletion needs a separate operation

Deleting player d is undefined until that player's behavior is specified.
One exact operation fixes a_d=b, removes its utility, and restricts the other
utilities to that slice. An inherited automorphism must fix d, satisfy
f_d(b)=b, and preserve the surviving domains. Restrict this stabilizer to the
survivors. It preserves the sliced game, but its player image can be much
smaller than S_{n-1}; full image or standardness of the original game alone
provides no preservation theorem. An alternative averages over a prescribed
law of the removed action; that is a different, expectation-based operation.
Neither is identified here with exact rectangular restriction at fixed n.

Common interest survives fixed-action deletion: surviving utilities were equal
on every original profile. Zero-sum generally does not: the removed utility
need not vanish. For instance the constant two-player game (1,-1) leaves a
nonzero one-player payoff after deletion. This explains why a zero-sum
invariant cannot be carried through player deletion without added hypotheses.

## Separating invariants and minimal witnesses

At fixed player count, exact isomorphisms, rectangular restrictions and
full-payoff quotients preserve common interest (all focal utilities agree)
and zero-sum (their sum is zero). They also preserve any specified linear
identity among the utility coordinates, transporting coefficients under
player relabeling. None of these claims uses an inherited group.

The three-player common-interest orientation game cannot reduce through these
operations to non-full Example 5.13: the latter has unequal majority-player
payoffs β≠γ. It is clone-free. Every binary rectangle either loses full player
image or becomes full by the binary characterization. Thus it is a minimal
non-full full-image witness under *arbitrary equal-size rectangular
restrictions and full-vector clone quotients*, within three players. This is
stronger than requiring inherited symmetries, and specifies the target
property rather than excluding reductions by definition. Single-action
restrictions cannot supply non-full games.

In contrast the four-action nonsplit game restricts on common {0,1} to
Example 5.13 with α=γ=δ=0,β=1. Nonsplitting is therefore not preserved by
arbitrary restriction; its extension mechanism changes. No claim that a
unique reduction core exists follows. A useful classification records a
clone-free payoff table, its represented extension, and the reduction
relation separately. Minimal-witness theorems must specify player count,
permitted payoff changes, and which target property is retained.

## A nonsplit common-interest minimal witness

The six-player ternary binary game constructed in
[phase5-six-player-obstruction.md](phase5-six-player-obstruction.md) has eighteen winning profiles C
and gives every player 1_C. Its full represented group has kernel C3 and
nonsplit player projection, unlike the split common-interest order18 witness.
The code C has minimum Hamming distance four, and every label occurs in each
coordinate. Hence it is clone-free: complete any chosen label to a winning
profile; replacing it by a different label changes just one coordinate and
leaves C. This changes the whole payoff vector.

Any proper rectangular restriction with full player image must have the same
number of strategies at every player. Since the source sets have size three,
that number is at most two. At six players the binary rigidity theorem forces
any such full-image restricted game to be fully symmetric under a matching;
singleton domains are full as well. The witness is therefore minimal under
arbitrary rectangles and full-payoff quotients retaining standardness, full
image and non-full symmetry, at fixed six-player count. This uses emergent
symmetry freely, rather than assuming inherited automorphisms.

Moreover common interest survives fixed-action player deletion, exact
isomorphism, rectangles and full-payoff quotients. No finite sequence of even
these operations can turn the six-player nonsplit game into a non-full
specialization of Example5.13, whose majority utilities differ. Thus a
nonsplit mechanism can remain separate from5.13 under a substantially broader
reduction system than the four-strategy example did. Reductions permitting
player-specific utility transformations require a separate analysis.
