# Reviewer A follow-up — R-AUDIT-002

Internal follow-up to the same reviewer; 16 October 2026. Coordinator's record.
The coordinator supplied four concrete criticisms and requested verification.

1. Corollary 4.24 is false under §4.3's explicit notation G<=Gamma meaning G<=Aut(Gamma). Constants u1=0,u2=1 satisfy (i)/(iii), but no player-swapping exact automorphism exists. The intended repair is to use the full bijection group, with a proof via the matching theorem.
2. Proposition 2.2's non-surjectivity assertion fails when at most one coordinate varies. With two varying coordinates, a two-point correlated distribution proves proper inclusion. The marginal argument proves injectivity more simply.
3. The strictly-increasing subgroup assertion fails for exp:R->R, which is not onto. Requiring increasing bijections repairs this statement.
4. Theorem 5.11's printed proof omits strategy bijections and substitutes pure extrema for mixed values. Its finite-game statement is true by mixed-strategy transport and zero-sum minimax, but the proof needs replacement.

The reviewer initially questioned whether finiteness was assumed globally.
The coordinator supplied the background's explicit declaration that only
finite games are considered; the reviewer accepted that correction. An infinite
symmetric zero-sum game without a value is consequently not a counterexample
to the scoped v5 theorem. See audit-evidence.md for actual finite-scope repairs.
