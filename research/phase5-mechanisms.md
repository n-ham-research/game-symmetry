# Phase 5: opposite-face orientation mechanisms

**Status: candidate extension, internally proved; priority unresolved.**
The signed alternating-opponent array belongs to the prior skew-symmetric
game framework of Hao and Cheng, [arXiv:1712.02962v1](https://arxiv.org/html/1712.02962v1), §4.1 (Propositions32–33)
and §4.2 (equations48–49 and Theorem36); its zero-sum property is also prior.
This note identifies its
full typed automorphism group and a binary realization of that group. It does
not assert ternary nonsplitting: the four-player ternary example below splits.
All indices start at zero and permutations compose right to left;
`(P_p s)_j=s_{p^{-1}(j)}`.

## P5-M1: an arbitrary-player realization theorem

For each integer m≥2, let n=m+1, give every player the strategy set
A={0,…,m−1}, and define

u_i(s)=(-1)^i ε(s_0,…,s_{i−1},s_{i+1},…,s_m),

where ε is zero on repeated labels and otherwise the sign of the displayed
permutation of A. Also define the binary-payoff game b_i(s)=1[u_i(s)>0].
Both games have exactly the same full typed automorphism group:

G_m = { (p;(f,…,f)) : p∈S_{m+1}, f∈S_m, sign(p)=sign(f) }.

Consequently its player projection is onto S_{m+1}, its kernel is diagonal A_m,
and its order is (m+1)!m!/2. The projection splits, both games are standard
symmetric, and neither is fully symmetric under any matching.

### Proof for the signed game

A typed automorphism has player permutation p and local bijections f_j.
It preserves whether each focal utility is zero. Fix two distinct coordinates
j,k and choose a focal player i different from both. If f_j(a)≠f_k(a), set
s_j=s_k=a, and choose the remaining m−2 opponents' strategies so their images
are the other m−2 labels. Then the source focal utility is zero but its image
is nonzero, a contradiction. Hence f_j(a)=f_k(a) for all j,k,a, so every local
map is one common permutation f.

The sign of the permutation induced by p on the ordered list omitting i is
sign(p)(-1)^{i+p(i)}. Applying f to all labels contributes sign(f). Thus
u_{p(i)}((p;f,…,f)s)=sign(p)sign(f)u_i(s).
Nonzero utilities exist, so the automorphism condition is precisely equality
of the two signs. This proves the exact group, including exclusion of all
additional local maps.

### Proof that binary coarsening keeps the exact group

At a profile using all m labels, exactly one label is repeated, at positions
r<t. The only nonzero signed utilities are u_r and u_t, and they are opposite:
removing the repeated occurrence moves the other occurrence across t−r−1
positions, while the cofactor signs differ by (-1)^{t−r}. Therefore exactly
one binary utility equals one. At any profile omitting a label all utilities
vanish. Thus the event `sum_i b_i(s)=1` is exactly surjectivity of s onto A,
and any binary-game automorphism preserves that event.

Fix distinct coordinates j,k. The number of surjective completions with
s_j=a,s_k=b is (m−1)! if a=b. If a≠b, it is
(m+2)(m−1)!/2: either the extra occurrence among the remaining m−1 positions
is one of a,b, giving 2(m−1)! completions, or one of the other m−2 labels is
duplicated, giving (m−2)(m−1)!/2. These counts differ for every m≥2.
A typed bijection preserves the completion counts, so a=b if and only if
f_j(a)=f_k(b). Taking a=b forces all f_j to be the same f.
The signed covariance formula then shows that matching signs preserve b,
whereas opposite signs interchange positive and negative utilities and fail
to preserve b. This proves the binary assertion.

### Splitting, standardness, and failure of full symmetry

Fix any transposition h∈S_m. The map p↦(p;h^{ε(p)},…,h^{ε(p)}) is a section,
where ε(p) is permutation parity. Bare A_{m+1} lies in G_m and is transitive
for m+1≥3, supplying a strategy-trivial player-transitive subgroup.
Suppose a matching supplied all player permutations. A player transposition
fixes some player i because n≥3, and its matching lift must have identity
local map at i. But every lift in G_m has the same odd local permutation at
every player, including i. Contradiction. This excludes every matching,
rather than merely the displayed section.

The signed game is zero-sum: the two possible nonzero utilities cancel.
This does not transfer to the binary game, whose payoff sum is zero or one.
The common-interest three-player ternary orientation example from Phase 4 is
a different construction; it is not this opposite-face game.

## Four players and three strategies

For m=3 the theorem gives a small binary game with exact group
S_4×_{C2}S_3, order72 and kernelC3. At all45 profiles using at most two labels
all payoffs vanish. At each remaining profile exactly one player receives1;
each player wins at9 profiles. The signed version instead has utilities
−1,0,1 and sum zero. Neither game is fully symmetric under any matching.

`experiments/phase5_mechanisms.py` independently checks all31,104 ambient
bijections and all216 matchings for both versions. At m=2 it checks all48
bijections and four matchings, recovering the signed-binary mechanism of
Example5.13, rather than claiming a new three-player binary classification.
The arbitrary-m theorem rests on the proof above, not extrapolation from
those computations.

## Scope of reductions

The group/kernel descriptions alone do not establish irreducibility under
arbitrary strategy restrictions: those may acquire emergent automorphisms.
For n=4 a restriction invariant under the entire G_3 must have its coordinate
subsets invariant under each player's stabilizer. That stabilizer induces all
S_3 on its strategies, so no proper nonempty coordinate subset survives.
The same argument works at every m≥2. This is deliberately weaker than
irreducibility under restrictions inheriting some full-image subgroup:
the displayed section uses only a fixed transposition h, and its proper
strategy orbits do give invariant restrictions. For m≥3, a common singleton
fixed by h yields a trivial full-symmetry restriction. Thus no irreducibility
under the broader inherited-full-image notion is claimed.

Exact isomorphism preserves the projection-aware action and hence kernel and
splitting type. The present split family therefore cannot be identified with
the three-player four-strategy nonsplit group by that equivalence. Different
player counts cannot be compared by strategy restriction alone. No universal
minimality or uniqueness follows from these observations.

## Minimality at fixed four-player ternary size

Both versions are full-vector clone-free. Indeed, a player's stabilizer in
G_m induces all S_m on its strategy set. Clone equivalence is invariant under
that action, and S_m is two-transitive, so any nontrivial clone pair would
make every action of that player a clone. Player transitivity would make
all actions of every player clones, forcing the entire payoff table to be
constant. Both displayed games are nonconstant, a contradiction.

For n=4,m=3, every proper equal-size rectangular restriction has at most two
strategies per player. The internally proved binary rigidity theorem says
that a four-player binary game with standard symmetry and full player image
is fully symmetric under a matching. Singleton games are also fully
symmetric. Consequently these ternary games are minimal witnesses of
`standard + full player image + not full matching` under arbitrary equal-size
rectangular restrictions and full-vector clone quotients, at fixed n=4.
This statement concerns retention of all three target properties and depends
on the binary rigidity theorem; it does not assert absence of proper
restrictions or preservation of full automorphism groups.
