# Phase 3 independent counterexample search: a signed-permutation obstruction

**Status: candidate extension with complete proof; novelty unchecked.** This is
an independent second construction. It is not claimed minimal: the parallel
investigation has a smaller three-player, four-strategy construction. No
manuscript claim or original audit status is changed here.

## Question and convention

Ham's Proposition 5.6 states that a subgroup projecting isomorphically onto
`S_N` implies n-transitively standard symmetry. The converse under investigation
means that the actual automorphism group projects onto `S_N` and contains a
player-transitive strategy-trivial subgroup. These may be different subgroups.
The question asks whether the actual projection admits a group section. A
strategy-trivial section is stronger still. We use
`(P_pi s)_j=s_{pi^{-1}(j)}` and compose right to left.

## A four-player, six-strategy, nine-value game

Players are `N={0,1,2,3}`. Every action set is
`A={0,1,2} × F_2`; write an action as `(c_i,b_i)`. The color coordinate is a
strategic label, not a player identity. Let `B=sum_i b_i mod 2`.

For each focal player `i`, read opponents in increasing player order. If their
three colors are not all distinct, put `t_i=0`. If they are all distinct, put

`t_i = 1 + (B + i + inv(c_{-i}) mod 2)`,

where `inv` counts inversions in that ordered length-three color sequence.
Define the integer payoff

`u_i(c,b)=3 c_i+t_i`.

Every payoff lies in `{0,...,8}`; every one of these nine values occurs.

### Exact automorphism group

The full typed automorphism group is

`G={ (pi,v) in S_4 ⋉ F_2^4 : sum_i v_i = parity(pi) }`,

acting by `(c_i,b_i) -> (c_i,b_i+v_i)` from player `i` to player `pi(i)`.
It has order `24·8=192`. Its player kernel consists of the eight even-weight
bit vectors, so the actual extension is

`1 -> C_2^3 -> G -> S_4 -> 1`.

**Proof.** First consider the displayed maps. Repetition or distinctness of
opponent colors is preserved. In the distinct case, let `j_0,j_1,j_2` be the
opponent indices ordered by color. The sign of the list
`(i,j_0,j_1,j_2)` is `i+inv(c_{-i}) mod 2`. Applying `pi` changes this sign by
`parity(pi)`. The sum of bits changes by `sum v`. Thus the required parity
relation preserves every payoff.

Conversely, for any exact automorphism, `floor(u_i/3)=c_i` shows that its
component strategy bijections preserve colors. Each component therefore flips
the bit by some function `f_i:{0,1,2}->F_2`. Its player permutation is some
`pi`. On every color profile having distinct opponent colors for a focal `i`,
the payoff identity gives

`sum_j f_j(c_j)=parity(pi)`.

Fix the three opponent colors as a permutation of `0,1,2`, and vary `c_i`.
The right side and the opponent terms stay fixed, so `f_i` is constant. Doing
this for each focal player proves that all component flips are constants
`v_i`. The same identity then gives `sum v=parity(pi)`. This proves the exact
full-group assertion, not just containment. ∎

### n-transitively standard symmetry

Pure even player permutations, with all component maps identity, form `A_4`
inside `G`. This subgroup is player transitive and strategy trivial. Also
`q(G)=S_4`. Hence the game satisfies precisely the n-transitively standard
hypotheses of the converse question, using Ham's matching characterization.

### The actual extension does not split

**Proof.** Suppose a section existed. The commuting disjoint transpositions
`tau=(01)` and `rho=(23)` would have commuting involutory lifts
`g=(tau,v)` and `h=(rho,w)`.

The condition `g^2=e` forces `v_0=v_1`; the odd parity of `v` therefore forces
`v_2 != v_3`. Likewise `h^2=e` gives `w_2=w_3` and `w_0 != w_1`.

Commutation requires, component by component,

`w_i + v_{rho(i)} = v_i + w_{tau(i)}`.

At `i=0`, since `rho(0)=0`, this gives `w_0=w_1`, a contradiction. There is
therefore no section, and in particular no strategy-trivial section. ∎

This obstruction uses the actual player action. It is stronger than merely
observing that some chosen lifts do not form a group: it rules out every
possible choice of lifts.

## Why the tempting binary version fails

The same abstract group acts on four binary action sets by signed
permutations. It cannot be the full exact automorphism group of a binary game.
Indeed its action on payoff cells `(i,s)` is transitive. Given two cells,
choose any player permutation taking their focal players to one another; bit
flips are then determined by the profile transport. If the parity condition
fails, precompose with a transposition of two nonfocal players and adjust the
bit flips. This reverses permutation parity while leaving the bit-sum change
fixed. Thus a permitted map always exists.

Consequently a game invariant under this binary action has every payoff cell
equal, and therefore has the entire typed-bijection group as automorphisms.
That larger extension splits. This demonstrates why an abstract nonsplit
subgroup is insufficient without verifying the full game's automorphism group.
The added three color labels avoid this orbit collapse.

## Exact computational verification

`experiments/phase3_split_search.py` independently evaluates the explicit
utility formula. The proved color-preservation reduction leaves exactly
`24·8^4=98,304` candidate typed maps. Affine bit dependence means zero-bit
profiles suffice to identify these candidates; the script then checks every
one of the `4·6^4=5,184` payoff cells for each of the 192 surviving maps.
It also enumerates all involutions above `(01)` and `(23)` and checks that no
pair commutes. This is exact integer computation, with no randomized samples.
The analytic proof establishes the counterexample independently of this check.

## Scope and minimization

This construction settles the unrestricted converse negatively, but it does
not settle the binary subclass or classify all obstructions. The six-action
size is not asserted minimal. The separate three-player construction should
be preferred for a main example if its full-group proof survives review.

For two players, n-transitively standard symmetry already supplies a
transitive strategy-trivial subgroup. Its projection is all `S_2`; its player
kernel is trivial by strategy triviality. Hence the desired section exists.
Thus no two-player counterexample can satisfy the exact hypotheses, regardless
of strategy-set size. One player is trivial.
