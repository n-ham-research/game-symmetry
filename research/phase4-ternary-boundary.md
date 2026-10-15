# Phase 4: complete three-player ternary mechanism boundary

Status: **candidate extensions, exact exhaustive group certificates and proofs
below; novelty unverified**. These extend rather than replace Ham's binary
classification. No manuscript edit is made.

Use `(g s)_{p(i)}=f_i(s_i)` for `g=(p;(f_i))`, and compose right to left.
Thus `(P_p s)_j=s_{p^{-1}(j)}`. All strategy sets are finite and nonempty;
utilities and automorphisms are exact numerical ones. "Fully symmetric" below
means fully symmetric under some matching, equivalently isomorphic to a
common-label fully symmetric game, not necessarily fully symmetric in the
current labels.

## Theorems

**Candidate P4-T1 (ternary splitting boundary).** Every three-player,
three-strategy game that is standard symmetric and has full actual player
image has a splitting of its player projection. In particular the Phase 3
four-strategy nonsplitting example is strategy-count minimal among
three-player games satisfying these two hypotheses.

**Candidate P4-T2 (complete ternary nonfull group mechanisms).** For such a
game which is not fully symmetric under any matching, relabel strategies so a
strategy-trivial three-cycle acts without strategy changes. Its full exact
automorphism group is one of the following, up to further simultaneous strategy
relabeling:

1. `H_h = {(p;(h^ε(p),h^ε(p),h^ε(p))) : p in S3}`, where `h` is a strategy
   transposition. This group has order six and trivial player kernel.
2. `L = {(p;(f,f,f)) : p,f in S3, ε(f)=ε(p)}`. This group has order eighteen
   and player kernel the diagonal strategy `A3`.

Here `ε` is permutation parity. Both split and neither admits a
strategy-trivial full-image subgroup. The first extends the fixed-player
transposition action already responsible for binary Example 5.13; on three
strategies that involution has an additional fixed action. The second has a
nontrivial strategy kernel and is a distinct actual-action mechanism. These
are group-mechanism statements, not a claim that their many numerical games
are all isomorphic to one another.

A common-interest orientation game realizes the second group; its construction
and analytic exact-group proof are recorded separately in
`research/phase4-mechanisms.md`.
The first group is realized by assigning different exact values to its fifteen
orbits on focal-profile cells. The exact certificate checks that no additional
typed automorphism preserves this orbit labeling.

## Exact, cardinal, and ordinal scope

**Candidate corollary P4-T3.** P4-T1 and P4-T2 hold separately for the exact,
cardinal, and ordinal typed automorphism groups, interpreting standardness and
full matching symmetry in the selected group. Thus three-player ternary
cardinal-standard/full-cardinal-image games have a cardinal projection section;
the analogous ordinal assertion also holds. A nonfull game at either
preference level has one of the same two actual typed groups `H_h,L`.

**Proof.** The canonical finite utility normalizations in U2 of
`research/utility-invariance.md` give
`Aut_card(u)=Aut_exact(c)` and `Aut_ord(u)=Aut_exact(r)`, as literally equal
subgroups of the same typed bijection group. Min-max normalization `c` and
distinct-level rank normalization `r` change no strategy domain. Therefore
standardness, the actual player projection, its kernel, splitting, and full
matching containment are identical subgroup questions. Apply P4-T1/P4-T2 to
the normalized exact game. This is not a claim about numerical cross-role
welfare or mixed-equilibrium invariance under ordinal transformations. ∎

The three-player four-strategy binary-payoff witness P3-S1b has the same
exact/cardinal/ordinal automorphism group: every player's payoff table has
minimum zero and maximum one, so both canonical normalized games coincide
with the original. Consequently four strategies are minimal for a
three-player nonsplitting counterexample under each of these three utility
notions, with the corresponding standardness and full-image hypotheses.

## Reduction to 648 possible lifts

By the audited strategy-trivial matching theorem (Ham 4.23), any
player-transitive strategy-trivial subgroup can be conjugated into the bare
coordinate permutations. A transitive subgroup of `S3` contains its three-cycle
subgroup. Thus every standard game can be relabeled so

`r=((012);id,id,id)`

belongs to its actual automorphism group `A`. Put `W=S3 wr S3`, of order
`6^3*6=1296`. Surjectivity of the player projection means some odd-player
bijection `g` belongs to `A`. There are exactly `3*6^3=648` possible such `g` in
`W`. Therefore `A` contains at least one `B_g=<r,g>`. No payoff assignments are
enumerated.

For each of these 648 possibilities, the program constructs `B_g` by closing
positive generator words. This terminates in a finite group. Positive words
contain inverses because each generator has finite order, so this computes the
whole subgroup, rather than just a subset. Deduplicating the resulting element
sets yields nineteen groups:

| Group order | Number of distinct groups |
|---:|---:|
| 6 | 4 |
| 18 | 3 |
| 24 | 6 |
| 54 | 3 |
| 162 | 1 |
| 648 | 2 |

For every group a certificate gives elements `a,t` with player images `(012)`
and `(12)`, satisfying `a^3=t^2=1` and `tat=a^-1`. The presentation of `S3`
then supplies a section, since the player projection of this homomorphism is
the identity. Thus any larger `A` containing the group also splits. This
establishes P4-T1 for three strategies. For one or two strategies, embed the
ambient typed-bijection group in the ternary ambient group by adding fixed
strategy labels; a section in a subgroup of this embedding remains a section
in the original group. Hence the three-player four-strategy example really is
minimal in strategy count. No analogous minimality for arbitrary player counts
is asserted.

One must not require this section to contain the original `r`. Four of the
nineteen groups have no complement containing that particular three-cycle,
although they have another complement. The certificate allows all order-three
lifts of `(012)` and avoids this false strengthening.

## Payoff-orbit closure and the complete classification

Let `C={(s,i)}` be the eighty-one focal-profile cells. A group acts by
`g.(s,i)=(g s,p(i))`. Its payoff-orbit closure is

`cl(B)={g in W : g sends each individual B-orbit in C into itself}`.

If a numerical game is invariant under `B`, its payoff function on `C` is
constant on each `B`-orbit. Consequently **every** element of `cl(B)` is an
actual automorphism of that game. Coincident orbit values can only add further
automorphisms. This implication applies to every real payoff assignment; it
is not a generic-parameter approximation.

For sixteen of the nineteen groups, the certificate exhibits a matching whose
full six coordinate-permutation lifts all lie in `cl(B)`. Such a `B` cannot be
contained in the automorphism group of a nonfully symmetric game. The remaining
three groups are exactly the `H_h` for the three strategy transpositions `h`.
Each is orbit-closed, has fifteen cell orbits, and admits no full matching.

Now suppose `A` is nonfull. Applying this argument to **each** odd element
`g in A` forces every such `g` into one of the three `H_h`. In particular every
odd element has common strategy map equal to a transposition. Fix an odd
`t in A`. For every even-player element `a in A`, the element `a t` is odd,
so both `a t` and `t` have common odd strategy permutations. Thus
`a=(a t)t^-1` has a common even strategy permutation. It follows that `A<=L`.
The player kernel is therefore contained in diagonal `A3`, so its order is one
or three. Surjectivity gives `|A|=6` or `18`. In the latter case `A=L`. In the
former, `A=<r,g>=H_h` for any odd element `g`. This proves P4-T2.

Conversely the certificate checks that `L` is orbit-closed. It is generated by
any two distinct `H_h`, has eighteen elements, and admits no full matching.
Both `H_h` and `L` are standard via their bare `C3`. Each `H_h` is a complement
in `L`, proving ordinary splitting for both cases. Neither has a strategy-trivial
full-image subgroup: an odd player permutation fixes one player, and every odd
element has the same nonidentity strategy permutation at that fixed player.

## Reproducible certificate and limits

`experiments/phase4_ternary.py` enumerates the entire finite domain, with exact
integer permutation tuples and no numerical sampling. The JSON certificate
records, for each of the nineteen groups, its odd generator, complete element
list (indices in the deterministic ambient enumeration), complement generators,
cell-orbit count, orbit-closure order, and a full matching when applicable.
`python3 experiments/phase4_ternary.py --verify` regenerates and compares it.
The associated tests check regeneration and the two exceptional mechanisms.
A separate agent implemented the same exhaustion using cell-permutation
composition, union-find orbits, and independently constructed matching maps in
`experiments/phase4_ternary_independent.py`; its nineteen-group histogram and
three exceptional groups agree. See `reviews/R-P4-MECHANISMS-C.md`. These
are internal same-family checks, not external peer review.

This is a finite exhaustive group proof of a theorem about all payoff tables on
this fixed strategy domain. It is not a symbolic classification for arbitrary
numbers of strategies or players. The distinction between `B` and `cl(B)` is
essential: several groups do not themselves admit a full matching, but every
game invariant under them does. In particular subgroup enumeration without
payoff-orbit closure would report spurious potential mechanisms.

## Independent analytic review of Phase 3 binary-payoff nonsplitting proof

The P3-S1b proof in `phase3-splitting-proof.md` was reread without changing its
construction. Its key steps check out:

- The proposed twelve-element parity/translation group preserves the payoff
  rule by cyclic-order reversal and focal-parity cancellation.
- The orbit sizes `4+5*12=64` are correct. Nonconstant stabilizers are trivial:
  a two-equal profile fixes the repeated action value and then translation is
  zero; an all-distinct profile has a three-element subset of `Z4` which no
  nonzero translation stabilizes. The only possible residual transposition in
  the two-equal case has odd parity and is excluded when translation is zero.
- Each listed nonconstant orbit has exactly one positive payoff. Thus the
  simultaneous-zero locus is precisely the diagonal, forcing any typed
  automorphism's three strategy maps to coincide.
- At a profile with two copies of `a` and one of `b`, exactly one of the two
  repeated-action players receives one. Which one it is depends only on the
  parity of `a` and cyclic player orientation. Therefore
  `parity(f(a))=parity(a)+parity(p)` is forced for every `a`.
- For even `p`, only `id,T2,-a,2-a` remain. The latter two send focal player
  zero's payoff at `(0,1,2)` from one to zero. Even player permutations preserve
  the relevant cyclic orientation, so they cannot repair this failure.
- For odd `p`, composing with the inverse known odd/`T1` automorphism reduces
  to the preceding even case, leaving exactly `T1,T3`. Hence the full group,
  not merely a preserving subgroup, is established analytically.
- Every transposition lift squares to the nonidentity common `T2`, so no
  section exists. The two-valued payoff claim does not mean two strategies.

No defect was found. This is an internal review by an agent from the same model
family, not external peer review. The ternary theorem above strengthens only
its three-player strategy-count minimality statement.
