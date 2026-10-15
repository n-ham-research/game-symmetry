# Phase 7 focused structural audit and readiness

Status: candidate extensions internally checked; no novelty clearance or external
peer review. This pass deliberately avoids another classification campaign.
The coordinating agent delegated only this repository to a separate Codex
instance, with the current review, prior context and repository available.
The reconstruction is not blinded and shares a model family with earlier work.
Composition is right to left: `(P_p s)_j=s_{p^{-1}(j)}`.

## Complete reduction reconstructed

The object is the complete exact group of a finite ternary payoff table,
not an arbitrarily selected typed subgroup. The player projection is onto.
The affine identification `S3=F3 semidirect C2` is exhaustive, not an
additional restriction. Put `R=F3^n`, `B=rho(G)`, `K=B intersect F2^n`,
and `N=G intersect R`.

1. Conjugation by a player lift permutes the sign kernel. A nonconstant
   vector and its transposed image produce a coordinate pair. Thus the only
   sign kernels are `0,T2,E2,F2^n`; this argument does not presume a direct
   sum in even characteristic.
2. If `K` contains `E2`, the even-sign characters on the translation
   coordinates are distinct and nontrivial for every `n>=3`. Character
   averaging projects `N` onto coordinate lines, so transitivity forces
   `N=0` or `R`. The latter makes actual payoffs constant. In the former,
   normal-subgroup averaging removes the graph cocycle: once it vanishes
   on `L=E2`, the two expansions of `c(lb)` give `l c(b)=c(b)`.
   There are no nonzero fixed vectors. The parity-constrained remaining
   sign group forces extra payoff invariance: zeros absorb parity, while
   on nonzero profiles an odd lift fixing the focal player exchanges the
   two product classes. Hence the complete group contains a full matching.
   These payoff-closure arguments are essential: an arbitrary preserving
   subgroup need not contain the automorphisms its invariant games force.
3. For `K=T2`, average only over the central order-two subgroup, never over
   all of `B`. Its action on `R/N` is minus identity. The resulting graph
   is a coboundary, and lifting the translation yields `N semidirect B`.
   Transposition lifts are involutions: their squares are constant and
   supported on two coordinates. Distant commutators are supported on four
   coordinates, hence zero for `n>=5`; adjacent central braid defects can
   be killed successively. At `n=3` there are no distant relations. At
   `n=4`, standardness excludes the nonzero distant defect because every
   transitive player subgroup contains a double transposition, whose
   lifts would all have order four. No standardness is used for `n>=5`.
4. For `K=0`, stabilizer characters normalize the sign action to ordinary
   permutation or common-parity-twisted permutation. The invariant
   translation subspaces are exactly `0,T3,E3,R`, by transposition
   differences. When `3` does not divide `n`, the constant line and
   sum-zero module are complementary. Lifting through an invariant
   complement gives a section, without claiming that every cocycle is a
   coboundary.
5. At `n>=5`, `N=E3` has a one-dimensional quotient. Its cocycle vanishes
   on perfect `A_n` and is a coboundary on the order-two quotient (or zero
   for trivial action). For `N=T3` with ordinary action, normalize each
   transposition lift to have zero translation at fixed coordinates.
   Distant and braid defects are constant and supported on fewer than
   `n` coordinates, hence vanish. The sole residual case is therefore
   `N=T3`, parity-twisted action, order `3 n!`, and `3|n`.
6. The inverse image of `A_n` is a central `C3` extension. For `n>=8`,
   the classical multiplier theorem eliminates it: the universal cover's
   order-two kernel has trivial image in `C3`. The perfect complement
   is characteristic, hence normal in `G`. Any transposition lift has
   square both fixed and inverted by conjugation, so is an involution.
   It extends that complement to an `S_n` section. The divisibility
   argument separately excludes `n=5,7`. Only `n=6` survives.

Boundary bookkeeping: standardness supplies a section at `n=2`; the quotient
is trivial at `n=1`; the finite three-player theorem and the four-player
argument settle `n=3,4`. The eighteen-word six-player example supplies
attainment. This is a classification of player counts, not a classification
of all six-player represented actions or payoff tables.

## Active counterexample attacks and utility transfer

The determinant-even group `D_n` remains a genuine counterexample to deleting
complete actual group from the theorem: for even `n>=4`, lifts of an `n`-cycle
have order `2n`. It contains bare transitive `A_n`. It is not a counterexample
to the retained claim because item 2 forces its invariant payoff tables to
have additional automorphisms. Dropping standardness at small player counts,
confusing a section with a strategy-trivial section, or asking a section to
extend a particular standard subgroup are not permitted strengthenings.
No new counterexample to the stated theorem was found.

Cardinal transport means positive affine utility equivalence; ordinal
transport means equivalence of the complete pure-profile preorder including
ties. Min--max normalized utilities and zero-based distinct-level ranks,
with constants set to zero, respectively identify those groups literally
with exact groups on unchanged domains. Hence all group hypotheses and
section conclusions transfer separately, rather than asserting equality of
the three groups for an arbitrary unnormalized game. The manuscript now
states these formulas and their converse arguments, with canonical companion
source `game-fairness` commit `a5e7f06`, utility results U1--U5.

## Targeted source and binary-potential review

Reopened and inspected the primary accepted author manuscript of Lassueur
and Mazza, dated 18 May 2015, Section 3, printed page 6:
https://eprints.lancs.ac.uk/id/eprint/82264/1/endoSchurAnSn_Revised.pdf .
It explicitly recalls multiplier order two except at `A6,A7`, where the
order is six, and cites Hoffman--Humphreys Chapter 2 and Wilson Section
2.7.2. This is inherited group theory. The six-player triple-cover action,
covering closure, and the indicator encoding of a code as common-interest
payoffs also remain prior structures; the exact game-theoretic hypotheses
and sharp boundary are candidate contributions. No new claim of priority
is warranted by this pass. A bounded search used the exact combinations
`ternary automorphism complement symmetric group`,
`games symmetry six nonsplit`, and
`potential name-irrelevant symmetric games Cao Yang`. The returned material
included the existing Cao--Yang SSRN record and Cheng--Liu arXiv abstract,
not a newly inspected theorem matching the sharp complete-game boundary.
Search outcomes are not absence or priority evidence. The Cao--Yang final
abstract explicitly warns that binary name-irrelevant games need not be
potential; its unqualified statement includes the known two-player matching
pennies case, so it does not itself refute the candidate n>=3 result.
Sources: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2637225 and
https://arxiv.org/abs/1701.06807 . Only their abstract-level claims were used
in this bounded refresh; no new access to the final article body is claimed.

Reopened Hofbauer--Sorger's primary paper, Section 4.2.2, printed page 27,
equation (4.15):
https://homepage.univie.ac.at/josef.hofbauer/02igtr_sorger.pdf .
The recursion gives exact potential for ordinary fully symmetric binary
choice games with unit weights. Coordination assumptions follow later and
are not prerequisites of that existence statement. Thus that ordinary
potential result is prior; the candidate `n>=3` full-actual-player-image
extension cannot be promoted merely by redescribing it. Its proof still
reduces to ordinary potential after matching at `n>=5`, own-action
indifference at the exceptional `n=4` branch, and the explicit signed
three-player payoff table. Existing Phase 4 kernel/lift audit is retained;
no new unrestricted search was started. Final Cao--Yang and other recorded
full-body access gaps remain unresolved. This pass is a source refresh and
proof check, not a replacement for specialist priority assessment.

## Manuscript changes and readiness

The abstract now leads with the unique possible player count. The
introduction explicitly treats Ham's Figure 4 and Example 5.13 as the
established starting point. A terminology table distinguishes standardness,
full image, splitting, strategy-trivial splitting and matching symmetry;
the last two are equivalent. The actualness counterexample and explicit
six-player payoff/code, analytic full-kernel proof and finite perfectness
certificate remain visible in the manuscript. The averaging-normality
identity and normalization transfer are now explicit.

Suitable next milestone: external mathematical scrutiny, subject to author
approval. Remaining limitations are the essential finite three-player and
perfectness certificates, represented-action uniqueness at six players,
specialist coding/design/permutation-group priority comparison, and human
proof review. No submission, external contact or authorship change occurred.

## Validation evidence

All 88 experiment tests passed. The original audit still reports 41 formal
results (33 verified, seven corrected, one unresolved original wording) and
five intact pinned files. The manuscript built with resolved references;
all twelve pages were rendered and visually inspected. A separate clean
`git archive` extraction with the manuscript patch, without ignored downloads,
passed the same 88 tests, audit and fresh build. No new low-impact tests
were added for editorial changes. These checks corroborate the finite
ingredients and document build, not the general theorem by themselves.
