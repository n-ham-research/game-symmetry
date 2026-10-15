# Phase 6: adversarial audit of ternary splitting

Status: **candidate game-theoretic extensions, internally checked**. The Schur
multiplier theorem imported below is prior group theory. No novelty or external
peer-review claim follows from this audit. Composition is right to left, with
`(g s)_{p(i)}=f_i(s_i)`.

## Findings

The proofs of P5-S4–S8 survive this reconstruction. Their hypotheses can be
weakened at player counts at least five. A standard covering-group theorem also
closes the remaining larger-player branch without a new search.

**Candidate P6-S1.** If a finite game has exactly three strategies per player,
its complete exact automorphism group has player image `S_n`, and `n>=5` with
`n!=6`, then its player projection has a section. Standardness is unnecessary.
Consequently, among standard full-image ternary games at arbitrary player counts,
nonsplitting can occur **only at six players**, where the explicit eighteen-word
common-interest binary-payoff game realizes it. The analogous statements hold
separately for cardinal and ordinal automorphism groups.

This classifies the possible player count, not all six-player payoff tables,
represented automorphism groups, or notions of equivalence between examples.

## Reconstruction of the reduction

Every local permutation of three actions is affine on `F3`. Write
`W=R semidirect (F2^n semidirect S_n)`, where `R=F3^n`; let `G=Aut(Gamma)`,
`B=rho(G)` forget translations, `K=B intersect F2^n`, and `N=G intersect R`.
Player surjectivity makes `K` invariant under coordinate permutations, so
`K` is one of zero, the constant line `T2`, the even-sum space `E2`, or all
`F2^n`. Indeed a nonconstant vector minus its transposed image supplies a
coordinate-pair vector; conjugates span `E2`.

1. **`K` contains `E2`.** The distinct nontrivial coordinate characters of
   `E2` split the translation module into its coordinate lines. Their orders
   are powers of two, so averaging is valid over `F3`. Transitivity gives
   `N=0` or `R`. If `N=R`, actual payoffs are constant and `G=W`. If `N=0`,
   averaging the extension cocycle over `E2`, then using normality and the
   absence of fixed vectors, conjugates `G` to `B`. A parity-constrained
   sign group has the same payoff invariants as an overgroup containing all
   bare player permutations: zeros absorb sign parity; on all-nonzero
   profiles a transposition fixing the focal player interchanges the two
   product-sign classes. This step uses **actual game invariance** and
   `n>=3`. Hence the game has a full matching.
2. **`K=T2`.** Its central element acts by minus the identity on `R/N`.
   Averaging a cocycle over this order-two subgroup kills it everywhere by
   normality; thus a translation conjugates `G` to `N semidirect B`.
   For `n>=5`, involutory adjacent-transposition lifts of `B` can be adjusted
   by its constant central flip to satisfy the braid relations. Distant
   commutators are supported on four coordinates and constant, hence zero.
   This supplies an `S_n` section. At `n=3` there are no distant relations.
   At `n=4` a nonsplitting binary quotient can occur; standardness excludes
   it because every transitive subgroup of `S4` contains a double
   transposition, whose lifts in that exceptional quotient have order four.
3. **`K=0`.** The sign quotient is a copy of `S_n`. Its local point-stabilizer
   character is trivial or parity, so after local sign relabeling its action
   on `R` is the permutation action or its common-parity twist. Its invariant
   subspaces are `0,T3,E3,R`, by the same transposition-difference argument.
   For `3` not dividing `n`, `R=T3 direct-sum E3`, and lifting the quotient
   cocycle through an invariant complement gives a represented section.
   This is a cocycle lift, not an assertion that the cocycle is a coboundary.
4. **Residual obstruction, `n>=5`.** If nonsplitting remains, `N` cannot be
   zero or all of `R`. If `N=E3`, the quotient cocycle vanishes on perfect
   `A_n` and is a coboundary on `C2`; hence it splits. If `N=T3` with the
   ordinary action, normalize transposition lifts to involutions with zero
   translation at fixed players. Distant commutators and adjacent braid
   defects are constant translations supported on at most four and three
   players respectively; for `n>=5` they vanish. Thus only the parity-twisted
   action with `N=T3` remains, of order `3 n!`, with odd permutations inverting
   the common translation kernel. None of this paragraph needs standardness
   at `n>=5`.

These are reconstructions of P5-S4–S8, not independent rediscoveries claimed new.
They identify exactly where actual payoffs and standardness enter.

## Closing the residual branch

The imported classical theorem is that the Schur multiplier of `A_n` for
`n>=8` has order two. A directly inspected primary research source is
Lassueur and Mazza, *Endotrivial Modules for the Schur Covers of the Symmetric
and Alternating Groups*, author manuscript dated 18 May 2015, §3, printed
page 6, [author PDF](https://eprints.lancs.ac.uk/id/eprint/82264/1/endoSchurAnSn_Revised.pdf).
Their account points to Hoffman–Humphreys, Chapter 2, and Wilson, §2.7.2.
This source's multiplier statement is imported; it is not proved here.

**Lemma.** Let `n>=8`, and suppose `G` fits into an extension of `S_n` by
`C3`, with `A_n` centralizing the kernel and odd player permutations inverting
it. Then the projection splits.

**Proof.** Set `H=q^-1(A_n)`. It is a central `C3` extension of the perfect
group `A_n`. The universal central extension of `A_n` has kernel of order two.
Its map into `H` supplies a subgroup surjecting onto `A_n`; the image of its
central kernel has order dividing both two and three and is therefore trivial.
Thus `H=C3 times D` for a perfect subgroup `D` mapping isomorphically onto
`A_n`. In particular `D=H'`, so `D` is characteristic in `H` and normal in `G`.

Choose any lift `t` of a player transposition. Then `t^2` belongs to `C3`.
Conjugation by `t` fixes its own square and inverts that kernel; hence
`t^2=(t^2)^-1`. Since `C3` has no nonidentity involution, `t^2=1`.
Now `D` is normalized by `t`, and `<D,t>` has order `2|A_n|=n!`, intersects
`C3` trivially, and projects onto `S_n`. It is the required represented
section. ∎

Applying this lemma to the residual branch excludes all `n>=8`. The cases
`n=5,7` already split because `3` does not divide `n`. This proves P6-S1.
For standard games, `n=1` is trivial, and `n=2` has a section supplied by the
standard subgroup. The three-player finite theorem and the four-player
splitting theorem supply `n=3,4`. The six-player game proves attainment.
Min-max and level-rank canonical normalizations respectively transfer the
whole argument to cardinal and ordinal symmetry.

## Why arbitrary subgroups are different

For any even `n>=4`, consider the actual embedded typed subgroup

`D_n={(b,p) in F2^n semidirect S_n : sum_i b_i=parity(p)}`,

where each local sign acts on ternary actions by `x -> (-1)^b x` and fixes
zero. It contains the bare `A_n`, a transitive strategy-trivial subgroup,
and its player projection is onto. But every lift of an `n`-cycle has
`n`th power the nontrivial constant flip: its sign sum is one. Such a lift
has order `2n`, so no section can exist.

At `n=4` this disproves the arbitrary-subgroup version of the sharp lower
bound. At `n=8` it disproves the arbitrary-subgroup version of P6-S1.
There is no contradiction: `D_n` is not an actual complete game group.
The large-sign-kernel payoff argument forces an invariant game to acquire
additional automorphisms. Thus 'actual' cannot simply be deleted from these
results. The three-player finite group lemma and the constant-sign-kernel
semidirect-product lemma themselves are abstract subgroup statements.

## Finite evidence and its limits

The six-player verifier `phase5_six_independent.py` was rerun in this audit.
It found 2160 group elements, 720 player images, pointwise kernel three,
standard subgroup order 60, and even inverse image and derived subgroup both
of order 1080. Its separate binary-code check tested all 46656 pointwise
local maps and found exactly three. The four-player independent tuple verifier
was also rerun: 21 section witnesses checked, covering the 251 normalized
lift classes. Its default invocation verifies saved group representatives;
it does not regenerate every class's group (that requires `--exhaustive`).

These runs corroborate explicit finite constructions; the general arguments
above do not follow from passing tests. No external human review has occurred,
and the source comparison does not establish historical priority.

## Bibliographic metadata for manuscript integration

Caroline Lassueur and Nadia Mazza (2015), *Endotrivial modules for the Schur
covers of the symmetric and alternating groups*, Algebras and Representation
Theory **18**(5), 1321–1335, DOI `10.1007/s10468-015-9542-y`. Metadata verified
against the [Lancaster institutional record](https://research.lancaster-university.uk/en/publications/endotrivial-modules-for-the-schur-covers-of-the-symmetric-and-alt/).
The body actually inspected is the 18 May 2015 accepted author manuscript;
the multiplier claim is in §3, printed page 6. Suggested BibTeX key:
`LassueurMazza2015`.
