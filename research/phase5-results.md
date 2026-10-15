# Phase 5 candidate results and dependencies

16 October2026. All entries are research candidates; mathematical verification
is internal, novelty remains provisional. These are separate from the pinned
original41-result registry. No original result changes status in this phase.

| Identifier | Exact scope and conclusion | Mathematical dependencies | Evidence |
|---|---|---|---|
| P4-T1/T2/T3 final audit | Three-player ternary standard/full-image groups split; actual non-full groups are H_h,L; exact/cardinal/ordinal transfer | Ham matching lemma; finite32lift/11class lemma; prior covering closure; utility normalizations | phase5-ternary-audit.md; independent stdlib certificate |
| P5-S1/S2/S3 | Four-player ternary splitting; abstract regular-C4 group lemma; large-sign kernel dichotomy | Binary invariant subspaces; normal2-group averaging;251lift/21group certificate; actual-payoff closure | phase5-splitting.md; independent four-player verifier |
| P5-S4 | Alln≥3: local-sign kernel containing even-sign group forces full matching for actual full-image ternary groups | Character projections overF3; cocycle averaging; exact utility-cell invariance | Analytic proof in phase5-splitting.md |
| P5-S5 | Alln≥3: constant-sign kernel removes translation obstruction; standard full-image such groups split | Central−I averaging on quotient; binary central-kernel Coxeter proof; n4standard exception exclusion | Analytic proof in phase5-splitting.md |
| P5-S6 | Standard full-image ternary group splits when3∤n; standardness unnecessary atn≥5 | S4/S5; binary complement normalization; F3 permutation-submodule classification; equivariant direct-sum/cocycle lift | Analytic proof; two separate reconstructions |
| P5-S7 | Binary common-interest six-player ternary game, actual group2160, kernelC3, standard and nonsplit; minimum ternary player count6 | Explicit18word code;12case kernel exclusion; full-image generators; standard60subgroup; perfect even-preimage1080; P4-T1 andS6 lower bound | phase5-six-player-obstruction.md; three implementations; exact JSON |
| P5-S8 | Any standard full-image ternary nonsplit group atn≥5 has commonC3 kernel, parity-twisted action, order3n!, and3 dividesn | S4–S6; perfectness ofAn; one-dimensional quotient cocycles; central ordinary-action Coxeter proof | Analytic necessary-type theorem; does not assert existence for all suchn |
| P5-M1 | Allm≥2: signed/binary opposite-face games realize S_(m+1)×_(C2)S_m, split/non-full; n4ternary order72 | Alternating signed array (prior Hao–Cheng); surjective-completion counts; exact group and matching proofs | phase5-mechanisms.md; exactm2/m3checks |
| R1/R2 | Restricted inherited groups retain I,C,M,S when witnessed; clone quotient with multiplicities has split full-group exact sequence | Direct restriction/factorization; canonical within-class numbering | phase5-reductions.md; boundary examples and two agent checks |
| Reduction separations | Common-interest3/6player witnesses do not reduce to non-full5.13 under specified exact operations;6player claim includes fixed-action deletion | Common-interest invariant; binary rigidity; code minimum distance4 | phase5-reductions.md; six-player proof |

The general n4 conclusion now has a computation-free route throughS4–S6;
the251lift certificate is an independent supplementary proof, not an essential
dependency of that route. The three-player finite lemma and the six-player
standard-subgroup/perfectness certificates remain explicitly finite ingredients.
Group names, source search failures and reviewer agreement are not proof inputs.

**Global strategy-count corollary.** Three is the minimum equal number of
strategies per player permitting a standard full-image nonsplit game over
all player counts. P5-S7 gives the upper bound. Singleton games are full;
for two players standardness already supplies a section; the three-player
binary case splits byP4-T1; and the binary standard/full-image rigidity
theorem excludes nonsplitting for every n≥4. This differs from the minimum
of four strategies when the player count is fixed at three.

Canonical exact representatives of cardinal and ordinal groups transfer
P5-S4–S8 to those selected groups, retaining all group hypotheses. The code
witness has the same exact/cardinal/ordinal group because its utilities
already attain precisely0and1.
