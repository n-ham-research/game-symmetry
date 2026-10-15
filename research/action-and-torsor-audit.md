# Action, quotient, wreath-product and hom-set audit

16 October 2026. Literature audit / candidate corrections, no novelty claim.
Source: Ham arXiv:1311.4766v5, inspected local original TeX. Internal reviewer C
is a reused Codex instance; it received the proposed four-player example and
independently checked all its claims. It did not read new A/B reviews.

## A-Q1: abstract quotient type does not determine player transitivity

Source section-label-independent-symmetric-games.tex:48, immediately after
Example 5.5, asserts that Aut(Gamma)/Gamma_N being isomorphic to some
transitive subgroup of S_N is equivalent to the game being symmetric.
This is incorrect if 'isomorphic' means abstract group isomorphism.

Take N={1,2,3,4}, every A_i={*}, and the unique profile's payoff vector
(0,0,1,1). For each pi there is exactly one typed game bijection with that
player permutation. It is an exact automorphism precisely when pi preserves
the two payoff classes {1,2} and {3,4}. Therefore

    Aut(Gamma)=< (12),(34) >,
    Gamma_N={id},
    rho(Aut(Gamma))=< (12),(34) > <= S_4.

The actual player action has two orbits {1,2},{3,4}; the game is not symmetric.
Abstractly this quotient is C_2 x C_2. It is isomorphic to the regular,
transitive subgroup

    V={e,(12)(34),(13)(24),(14)(23)} <= S_4.

For example map the generators (12),(34) of the actual image to (12)(34),
(13)(24), respectively. These commuting independent involutions give an
abstract isomorphism onto V. Thus the source's abstract condition holds while
its claimed symmetry conclusion fails. The construction uses allowed finite
singleton sets, not an extension outside the paper's assumptions. If desired,
using any common nonempty finite action set and player-constant payoffs with
the same vector gives the same player image and quotient, with a nontrivial
strategy kernel; hence the issue does not depend on singleton action sets.

Degree four is the smallest possible counterexample of this type. In degree
two an intransitive subgroup of S_2 is trivial and cannot be abstractly
isomorphic to its transitive subgroup C_2. In degree three an intransitive
subgroup fixes a point and has order at most 2; any transitive subgroup has
order divisible by 3 by orbit-stabilizer. Degree one is automatically
transitive. Since every quotient in question is isomorphic to its actual
player image, these arguments rule out all smaller degrees, not only
singleton-payoff constructions.

Correct replacement: let rho:Aut(Gamma)->S_N be the specified player
projection. The first isomorphism theorem gives the canonical isomorphism

    Aut(Gamma)/Gamma_N -> rho(Aut(Gamma)),  g Gamma_N |-> rho(g).

Equip the quotient with its induced action (g Gamma_N) dot i=rho(g)(i).
The game is symmetric if and only if this induced action is transitive,
equivalently if and only if the actual player image rho(Aut(Gamma)) is
transitive. It is also equivalent to an isomorphism to a transitive subgroup
that intertwines the specified actions (up to a relabelling of N).
The forward abstract-isomorphism implication alone is true, but its converse
fails. State the action, not merely the abstract isomorphism class.

The paragraph's preceding assertion

    Aut(Gamma)/Gamma_N is abstractly isomorphic to S_N
      iff rho(Aut(Gamma))=S_N

is valid in the finite setting: the actual image is a subgroup of S_N of
order n!, hence equals S_N. This argument does not generalize to 'some
transitive subgroup' because equal abstract group types may have distinct
permutation representations. Proposition 5.6 likewise remains valid: its
trivial kernel plus abstract order n! forces the actual image to be S_N.

## A-W1: spell out the semidirect product

Source section-bijections.tex:129 writes S_N wr S_M for the full typed
bijection group of an n-player m-strategy game. After choosing identifications
of all strategy sets with {1,...,m}, the actual group is

    (S_m)^n semidirect S_n,

with S_n permuting n factors; its order is (m!)^n n!. The source's order of
wreath factors is opposite to the usual imprimitive convention
H wr K=H^{|Omega|} semidirect K when K acts on Omega. Under that convention
the group is S_m wr S_n. For n=2,m=3 the actual group has order
(3!)^2 2!=72, while the printed conventional S_2 wr S_3 has order
(2!)^3 3!=48. These cannot be isomorphic.

This diagnoses the formula under an explicitly declared convention; wreath
notation varies. Use the semidirect product and its action, or declare the
wreath convention before calling the displayed order wrong. Coincidental
equalities when n=m do not resolve the general discrepancy. Singleton action
sets give actual group S_n, although its action on the one-point profile
space is trivial. Do not identify full typed bijections with their possibly
nonfaithful image on profile space.

## A-T1: hom-sets, torsors and what is canonical

A typed arrow has a specified source and target, even when underlying action
sets coincide. If Gamma and Lambda are distinct objects, two arrows
Gamma->Lambda cannot generally compose, so their hom-set has no group
operation inherited from groupoid composition. Endomorphisms form groups;
all typed arrows together form a groupoid. Exact isomorphisms form a
subgroupoid of full typed game bijections.

If X=Isom(Gamma,Lambda) is nonempty, Aut(Lambda) acts on X on the left and
Aut(Gamma) on the right by composition. Both actions are free and transitive:
for x,y in X, the unique left multiplier is y x^{-1}, and the unique right
multiplier is x^{-1}y. Thus X is a bitorsor. Choosing x identifies X as a
set with either automorphism group, but no such choice is canonical and it
does not turn inherited hom-set composition into an operation. The identical
argument applies to full game-bijection hom-sets using their full typed
endomorphism groups instead of payoff-preserving automorphism groups.

For isomorphic Gamma_1,Gamma_2,Gamma_3, choose a:Gamma_1->Gamma_2 and
b:Gamma_2->Gamma_3. The map

    Isom(Gamma_1,Gamma_2) -> Isom(Gamma_2,Gamma_3),
    f |-> b f a^{-1}

is a bijection with inverse h |-> b^{-1} h a. This explains the set-level
reading of Corollary 4.10, but not a claimed canonical group isomorphism
between those hom-sets. This entry records representation clarification;
another reviewer is auditing that formal result directly.
