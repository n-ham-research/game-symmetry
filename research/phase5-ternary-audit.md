# Phase 5: final three-player ternary audit and conjugacy proof

Status: **candidate extension, internally verified finite proof; novelty
unverified**. This is an independent reconstruction of P4-T1/T2/T3, with a
smaller finite proof. It does not assert a theorem for four or more players.
No manuscript theorem is promoted. Ham's matching theorem is prior work.

All three strategy sets are identified with `D={0,1,2}`. A typed bijection is
`g=(p;(f_0,f_1,f_2))`, acting by `(gs)_{p(i)}=f_i(s_i)`. Composition is right
to left; hence `(P_p s)_j=s_{p^{-1}(j)}`. Let `q(g)=p`, let `epsilon` denote
parity, and let `W=(S_D)^3 semidirect S_3`.

## Standalone theorem

**Theorem (three-player ternary boundary).** Let a finite three-player game
have at most three strategies per player, with equal strategy-set sizes. If
its exact automorphism group `A` has player image `S_3` and contains a
player-transitive strategy-trivial subgroup, then `q:A -> S_3` has a section.

When there are exactly three strategies per player and the game is not fully
symmetric under any matching, strategy labels can be chosen so its full exact
automorphism group is precisely one of

`H_h = {(p;(h^epsilon(p),h^epsilon(p),h^epsilon(p))):p in S_3}`,

for a strategy transposition `h`, or

`L = {(p;(f,f,f)):p,f in S_3, epsilon(p)=epsilon(f)}`.

The orders are six and eighteen; the player kernels have orders one and three,
respectively. Both occur as full automorphism groups, both split, and neither
contains a strategy-trivial subgroup projecting onto `S_3`. The theorem also
holds for cardinal and ordinal automorphism groups, with all hypotheses and
conclusions interpreted in the selected group.

**Proof.** Ham's strategy-trivial matching theorem supplies coherent strategy
labels making the given transitive subgroup a subgroup of bare player
permutations. Every transitive subgroup of `S_3` contains `C_3`. Consequently
we may assume `r=((012);id,id,id)` belongs to `A`. Surjectivity supplies an
element `g` with odd player image, necessarily a transposition.

The normalizer in `W` of `<r>` is exactly

`N={(p;(f,f,f)):p,f in S_3}`,

of order 36. Indeed every player permutation normalizes the player `C_3`;
conjugation has identity local components exactly when the three conjugating
local maps coincide. Conjugation by a bare player permutation makes `q(g)`
the fixed transposition `t=(12)`. This leaves 216 possible local triples.
Conjugations preserving this player transposition form `S_3 x C_2`: simultaneous
conjugation of all three local maps, and interchange of the two moved-player
components. There are exactly 32 orbits of triples under this action.

For clarity, this count has an independent Burnside derivation. For a strategy
permutation `f`, write `c(f)=|C_{S_3}(f)|`. Without interchange, the number of
fixed triples is `c(f)^3`; with interchange, it is `c(f)c(f^2)`. Summing over
the identity, three transpositions and two three-cycles gives respectively
294 and 90. The orbit count is `(294+90)/12=32`.

The finite lemma below constructs `<r,g>` for one representative of each of
these 32 classes, and identifies eleven conjugacy classes under `N`. Each of
the eleven groups contains elements `a,b` such that

`q(a)=(012), q(b)=(12), a^3=b^2=1, bab=a^-1`.

These relations give a homomorphism `S_3 -> <r,g>` whose composite with `q` is
the identity. Conjugation by `N` preserves existence of a section (conjugate
both the domain and range player actions). Thus `A` splits. For one or two
strategies, regard the local permutation groups as fixing extra labels inside
`S_3`; the constructed section lies inside the original embedded group and
therefore restricts back to the original strategy sets.

For the classification, let `C={(s,i):s in D^3,i in {0,1,2}}` and define

`cl(B)={w in W: w preserves each individual B-orbit on C}`.

Every game invariant under `B` is invariant under `cl(B)`: its payoff at a
cell is constant on each `B`-orbit. Equalities between different orbit values
can add automorphisms, so this implication holds for every numerical
specialization. The finite lemma shows that all but one of the eleven
conjugacy classes have a full matching in `cl(<r,g>)`. The sole exceptional
class consists of the three groups `H_h`; each is orbit-closed.

If `A` is nonfull, apply this implication to every odd element `g in A`.
Every such element must belong to one of the three `H_h`. It therefore has
three equal strategy components, each an odd strategy permutation. Fix an odd
`b in A`. For any element `a in A` with even player image, both `ab` and `b`
have common odd components. Hence `a=(ab)b^-1` has a common even component.
Thus `A <= L`. Its player kernel is a subgroup of the diagonal `A_3`, so has
order one or three. In the latter case `A=L`; in the former, any odd element
and `r` generate a group `H_h` of order six equal to `A`.

Each `H_h` has the evident section. The same section is contained in `L`.
Every odd player transposition fixes a player while its local component there
is a nonidentity odd strategy permutation, so neither group has a
strategy-trivial full-image subgroup. Their orbit closures equal themselves,
providing exact realizations by assigning distinct real values to their
utility-cell orbits. A three-valued common-interest realization of `L`, with
an analytic full-group proof, is given in `phase4-mechanisms.md`.

Finally, cardinal automorphisms are literally the exact automorphisms of the
playerwise min-max-normalized utilities; ordinal automorphisms are literally
the exact automorphisms of the playerwise distinct-level ranks. Constant
utilities are normalized to zero in both cases. Both normalizations preserve
strategy domains and every group property in the statement. Applying the
exact theorem to these normalized games proves both transfers. ∎

The Phase 3 four-strategy witness has binary payoffs, so both normalizations
leave it unchanged. It follows that four strategies are minimal at **three
players** for nonsplitting with the stated hypotheses, separately at each
utility level. No other player count is covered by this minimality assertion.

## Finite lemma and complete verifier specification

**Finite lemma.** The 32 normalized lift classes above generate the eleven
normalizer-conjugacy classes in the following table. Every group splits. The
fourth column counts the 32 lift classes assigned to that row. The closure is
on 81 focal-profile cells, and the final column records whether it contains a
full matching subgroup.

| Class | Group order | Embedded conjugates | Lift classes | Cell orbits | Closure order | Full matching in closure |
|---:|---:|---:|---:|---:|---:|:---:|
| 0 | 6 | 1 | 1 | 18 | 6 | yes |
| 1 | 6 | 3 | 1 | 15 | 6 | no |
| 2 | 18 | 1 | 1 | 6 | 18 | yes |
| 3 | 18 | 2 | 2 | 6 | 18 | yes |
| 4 | 24 | 3 | 2 | 7 | 24 | yes |
| 5 | 24 | 3 | 2 | 6 | 48 | yes |
| 6 | 54 | 1 | 1 | 2 | 108 | yes |
| 7 | 54 | 2 | 2 | 2 | 108 | yes |
| 8 | 162 | 1 | 6 | 1 | 1296 | yes |
| 9 | 648 | 1 | 7 | 1 | 1296 | yes |
| 10 | 648 | 1 | 7 | 1 | 1296 | yes |

Concrete generators are also compact. Write `abc` for the permutation
sending `0,1,2` to `a,b,c`, respectively. The player part of each following
odd generator is `(12)`; its three local maps, before canonicalization, are:

| Class | Local maps of an odd generator |
|---:|:---|
| 0 | `(012,012,012)` |
| 1 | `(021,021,021)` |
| 2 | `(120,120,120)` |
| 3 | `(012,120,201)` |
| 4 | `(012,021,021)` |
| 5 | `(012,012,021)` |
| 6 | `(021,102,210)` |
| 7 | `(021,021,102)` |
| 8 | `(012,012,120)` |
| 9 | `(012,021,102)` |
| 10 | `(012,021,120)` |

Together with `r`, these generate representatives for every row; the JSON
records the complete element sets and section witnesses in canonical labels.

This lemma is a finite computation, not a replacement for the preceding
mathematical reductions. Its entire verifier is
`experiments/phase5_ternary_audit.py`, importing only the standard library.
It imports no Phase 4 implementation or certificate. Its exact domain,
operations and exhaustive assertions are as follows.

1. Enumerate permutations lexicographically as image tuples. Enumerate `W` by
   player permutation and then three local permutations, in lexicographic
   product order. This indexes all 1296 elements, starting with identity.
2. Multiply `(p,f)(q,h)=(pq,(f_{q(i)} h_i)_i)`. Inversion and the cell action
   are direct tuple formulas. These are independently implemented here.
3. Enumerate all 216 lifts of `(12)`. Remove complete conjugacy orbits under
   its twelve-element stabilizer in `N`, always selecting the smallest
   remaining tuple; assert that 32 orbits cover all 216 lifts.
4. Close each pair `r,g` by positive-word breadth-first closure. In a finite
   group positive words contain inverses, so this is the generated subgroup.
   Canonicalize by taking the least sorted element set among all 36
   conjugates. Assert eleven distinct sets, with nineteen total distinct
   embedded conjugates and the table's order histogram.
5. For each canonical group search **all** its elements for the stated section
   relations. Reclose the two selected generators and assert order six.
6. Compute each orbit on all 81 cells. Test all 1296 typed maps for preserving
   every individual orbit. Enumerate the 36 matchings by two reference-player
   bijections; their lifts have local components `m_{p(i)} m_i^-1`. Check all
   six player permutations for containment in the closure.
7. Verify the sole nonfull conjugacy class equals `H_h`, its three conjugates
   are orbit-closed, and their union generates precisely the parity fibre
   product `L`. Verify `L` is orbit-closed and has no full matching.

The committed `experiments/phase5-ternary-audit-results.json` contains all 32
lift representatives and their orbit sizes/class assignments; for each of the
eleven classes it records its representative odd generator, complete canonical
element set by ambient index, section generators, orbit/closure counts and a
full-matching witness when one exists. The representative odd generator is
listed **before** normalizer canonicalization; the complete element list and
section are in the canonical labels. Reproduce and compare with:

`python3 experiments/phase5_ternary_audit.py --verify`.

This provides a shorter, independently coded finite proof than 648 separate
lifts. A wholly symbolic replacement of the eleven-case lemma remains open;
we do not describe this as a computation-free classification.

## Adversarial audit findings

No omission was found in the standard-cycle normalization, the 648-lift
completeness reduction, the nineteen-group certificate, the payoff-orbit
closure implication, or the actual-group order-six/eighteen argument. The
normalizer reduction independently regenerates the same nineteen embedded
groups. Cardinal/ordinal transfer uses equality of normalized-game groups,
not the generally false assertion that original exact and ordinal groups
coincide without additional assumptions.

The section need not extend the chosen bare three-cycle. The verifier searches
all order-three lifts rather than imposing this false strengthening. A closure
may have a full matching even when the original subgroup does not; the table
retains both objects. Numerical specializations are covered by the closure
implication rather than by assuming generic distinct orbit values.

This audit uses another agent instance with shared project history and the
same model family. Independent implementation and derivation are evidence;
agent agreement is neither external peer review nor priority clearance.
