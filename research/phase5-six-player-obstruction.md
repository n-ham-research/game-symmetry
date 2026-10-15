# Six-player ternary nonsplitting: an explicit binary game

Status: **candidate game construction and minimal-boundary theorem**, with
exact finite certificates and independent reconstructions. The abstract
nonsplit group `3.S6` and its 18-point representation are prior group theory,
not new constructions. The source generators below are from the
[ATLAS representation 3S6G1-p18aB0](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/3S6G1-p18aB0),
with separate [first](https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/gap/3S6G1-p18aB0.g1)
and [second](https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/gap/3S6G1-p18aB0.g2)
permutation-generator files. Related Hadamard realizations and nonsplitting
are prior work, as the Phase 5 source-comparison note specifies. The game
result's priority is unresolved. No appeal to the label `3.S6` is needed
for the independent certificate proof below.

## The game and result

Use six players, each with strategy set `F3={0,1,2}`. Let `C` be the 18-word
code obtained by adding a common constant in `F3` to each of these six rows:

    000100
    002221
    011122
    012010
    020212
    021001

Set `u_i(s)=1` when `s in C`, and `u_i(s)=0` otherwise, for every player.
This gives a completely explicit common-interest binary-payoff game on
729 profiles. Its definition requires no orbit labels or generic parameters.

**Candidate P5-S7.** This game's complete exact automorphism group has order
2160, projects onto `S6`, and has kernel the three common translations.
It contains a player-transitive strategy-trivial subgroup of order 60, but
its player projection has no section. In particular it is not fully
symmetric under any matching. These statements also hold for the cardinal
and ordinal groups: both canonical utility normalizations equal the game.
Six is the least number of players for a three-strategy game with standard
symmetry, full player image, and nonsplitting projection.

Compose right to left, and write a typed map as `(p;(f_i))`, acting by
`(g s)_{p(i)}=f_i(s_i)`. Permutation tuples list images, starting at zero.

## Exact automorphisms: a short analytic reduction

Every local permutation of `F3` is affine, `f_i(x)=a_i x+b_i`, with
`a_i in {1,-1}`. Every typed map preserves Hamming distance. Directly from
the six displayed rows, two distinct codewords have distance four or six.
The distance-six triples are exactly the common-translation triples
`{r,r+1,r+2}`. This is verified by 153 unordered pairs, or by the six-by-six
row comparison and common translation.

First consider an automorphism fixing all players. It permutes those triples.
For a fixed `r`, the images of `r,r+1,r+2` must therefore form a
common-translation triple; their coordinatewise increments are `a_i`.
Consequently all `a_i` equal one common slope `a`.

Common translations preserve `C`. Modulo one such translation, arrange that
the image of the first displayed row `r0=000100` has first coordinate zero.
It must then be one of the six displayed rows, say `r`. The translation
vector is forced: `b=r-a r0`. Thus only twelve candidates remain, indexed
by `a=+/-1` and the six rows. Only `a=1,r=r0` preserves the code. A tiny
explicit rejection certificate is the following table; each entry is a
codeword whose image under the candidate is absent from `C`.

| Target row r | a=1 | a=-1 |
|---|---|---|
| 000100 | identity | 002221 |
| 002221 | 002221 | 011122 |
| 011122 | 002221 | 002221 |
| 012010 | 002221 | 002221 |
| 020212 | 002221 | 002221 |
| 021001 | 002221 | 002221 |

The pointwise-player automorphism kernel is therefore precisely the common
translations `x -> x+k`, of order three. This checks the actual full group,
including potential extra payoff symmetries introduced by binary coarsening.

The following two typed maps preserve the 18-word code:

- `a` has player permutation `(0,3,2,1,4,5)`, with local maps
  `(021),(021),(102),(021),(021),(102)` in image-tuple notation.
- `b` has player permutation `(1,4,0,3,5,2)` and all local maps the identity.

Here `(021)` denotes `0->0,1->2,2->1`, not cycle notation; `(102)` denotes
`0->1,1->0,2->2`. The player image of `a` is `(1 3)` in cycle notation;
that of `b` is the five-cycle `(0 1 4 5 2)` fixing player 3. Conjugating
`(1 3)` by powers of that five-cycle supplies all five transpositions joining
player 3 to the other players, and these generate `S6`. Thus the actual
player image is `S6`. Together with the kernel computation this proves
that the actual full group has order `3*720=2160`.

The certificate independently generates `<a,b>` and obtains 2160 elements;
therefore these two maps generate the whole actual group `G`, rather than
just a full-image proper subgroup.

## Standard symmetry

The following two translations with player permutations belong to `G`:

`x: p=(1,0,2,4,3,5), local translation vector=(1,2,0,1,2,0)`,

`y: p=(1,3,5,0,2,4), local translation vector=(1,2,1,0,1,1)`.

Exact closure of `<x,y>` gives 60 elements and 60 player images. Its player
image is transitive on all six players. Direct fixed-player component
verification confirms strategy triviality. There is also a structural
explanation for that last check: all local maps of this subgroup are
translations, and a point stabilizer has order `60/6=10`; its homomorphism
to the local translation group `C3` must be trivial because three does not
divide ten. Thus `<x,y>` witnesses standard symmetry.

The order and image checks are part of the specified finite certificate;
no unsupported assertion that the displayed generators satisfy an
abstract presentation is required.

## Nonsplitting

Let `H` be the inverse image of `A6` under `q:G->S6`. The certificate
checks that `H=<b,a b a>` has order 1080, hence is that complete inverse
image. It also checks that `H` is perfect: the normal closure within `H`
of the commutator `[b,a b a]` is all of `H`. Explicitly generate its 1080
conjugates and close their subgroup; it contains 1080 elements. Since all
these generators are commutators, `H'` contains `H`, proving `H'=H`.

If a section `S6->G` existed, its image would meet `H` in a subgroup of
order 360, of index three in `H`. The action of `H` on the three left
cosets would be a transitive homomorphism `H->S3`. The image of a perfect
group is perfect, while `S3` has no nontrivial perfect subgroup. Such a
transitive action is impossible. Therefore no section exists.

This is an independent finite certificate of nonsplitting. It does not
merely infer nonsplitting from the ATLAS name, nor mistake absence of a
strategy-trivial section for absence of every section.

## Verifier and independent checks

`experiments/phase5_splitting_six.py --verify` checks the complete saved
record `phase5_splitting-six-results.json` using only the Python standard
library. Its steps are:

1. Generate the 18-point permutation group from the two primary-source
   generators, obtaining 2160 elements. Recover its six blocks of size three
   from the singleton/two-point orbits of a point stabilizer; order the
   blocks and their members lexicographically. Convert the action to the
   typed generators printed above.
2. Construct the explicit code from its six seed rows and verify its
   preservation by both generators. Check the Hamming-distance triples and
   all twelve analytic kernel candidates. As a separate exhaustive check,
   test all `6^6=46656` tuples of local permutations fixing players; exactly
   the three common translations preserve the binary payoff table.
3. Generate the displayed standard subgroup, check its order 60, membership
   in the full group, transitive player image and every fixed-player local
   identity.
4. Generate the even inverse image and the normal closure of its indicated
   commutator, checking equality of the two order-1080 groups.

No enumeration of the 33,592,320 ambient typed maps is necessary: full
player image means the actual automorphism group is determined by its
pointwise-player kernel and one already known lift per player permutation.
No source downloads or GAP installation are needed to rerun the verifier.
Two additional agent implementations reconstruct the result without
importing this implementation's group operations. Their actual scopes and
shared-model limitations are recorded in the review log.

## Minimality, reductions and scope

For one player a projection section is trivial. For two players a standard
subgroup already supplies a section. Phase 4 proves ternary splitting at
three players; P5-S6 proves it at four and five players. Hence this six-player
example is player-count minimal among ternary games satisfying the target
properties. Its cardinal and ordinal groups are literally its exact group,
because every player already uses both normalized levels zero and one.
The same lower bounds transfer through the canonical normalizations.

The game is full-vector clone-free. Every action occurs in every coordinate
of a codeword, and changing just one coordinate of that codeword produces
Hamming distance one, hence leaves `C`. Such a replacement changes the
entire common payoff vector. Thus no two distinct strategies are clones.
Every proper equal-size rectangular restriction has at most two actions per
player. The binary rigidity theorem makes a standard full-image restriction
fully symmetric under some matching; it cannot retain nonsplitting.
Therefore this is also a minimal witness under arbitrary equal-size
rectangular restrictions and full-vector clone quotients at six players.

Common interest survives those reductions, and also fixed-action player
deletion. A nonfull specialization of Example 5.13 has unequal majority-player
payoffs, so this game cannot reduce to it through those exact payoff-
preserving operations. The six-player obstruction is not a strategy-cloning
version of that binary example. This does not classify every obstruction at
six players or claim an arbitrary-player uniqueness theorem.
