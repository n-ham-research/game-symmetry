# Phase 3 result and dependency ledger

16 October 2026. All entries remain research candidates or attributed prior
facts. “Proof checked internally” means the argument is written and scrutinized
by same-family Codex agents and the coordinator; it is not external peer
review, author sign-off, or a novelty finding. Original pinned artifacts and
the separate original-statement verdicts are unchanged.

| ID | Classification and conclusion | Proof / dependencies | Internal review |
|---|---|---|---|
| S1/S1b | Candidate extension; disproves universal converse of Ham 5.6. Three players, four strategies, two payoff values; full Aut order12 and nonsplit projection to S3. | phase3-splitting-proof.md; typed composition, explicit payoff table, full-Aut proof, transposition squares | A derived; B and C independently checked; coordinator checked. |
| S2 | Previously established by Ham: strategy-trivial splitting iff full symmetry up to exact isomorphism; ordinary splitting is weaker. | Audited4.23/5.2; existing5.13 separating example | Prior audit plus Phase3 A/B/C checks. |
| S3 | Standard algebra specialized to actual q: splitting iff kernel corrections solve the factor-set equation, equivalently suitable adjacent-transposition lifts satisfy Coxeter relations. | phase3-splitting-proof.md; explicit multiplication, S_n presentation | A derivation and coordinator review; no novelty claim. |
| E1 | Candidate extension: all binary n-transitively standard games have an exact potential, hence a pure equilibrium and finite strict improvement paths. | phase3-equilibria.md; E2 for n≥3; audited full-matching argument for n=2; u1 for n=1 | C derived; A/B independently checked; coordinator checked. |
| E2 | Candidate extension: for n≥3, full actual player image alone suffices for exact potential. For n≥5, full symmetry up to relabeling; n=4 full symmetry or complete own-action indifference. | Binary invariant-kernel classification; complement stabilizer characters; Coxeter lifts; n=4 normalized opponent action; explicit signed n=3 potential | C derived; A/B independently checked; coordinator checked. |
| E3 | Candidate extension: for binary n≥4, n-transitive standard implies fully symmetric up to relabeling. | E2 proof; every transitive subgroup of S4 contains a double transposition; strategy-trivial injectivity | Same A/B/C/coordinator review as E2. |
| F1 | Elementary operational characterization: fixed typed transport passes all conditional-action/product-belief tests iff it preserves focal payoff pointwise. | phase3-fairness.md; Dirac laws and finite linearity | Coordinator derived; A/B checked. |
| F2–F4 | Candidate framework with exact separating examples: focal vs simultaneous tests, optimal values vs menus, aggregate information vs ex post anonymity, selected law vs structural transport. | phase3-fairness.md; exact small payoff tables; test_phase3_fairness.py | Coordinator derived; A/B checked. |
| F5 | Attributed coalition-value transport principle, following von Neumann–Morgenstern28.1–28.2, extended to typed maps; converse fails. | phase3-fairness.md; finite coalition minimax, change of variables, explicit zero-value/nontransitive example | Coordinator derivation; A/B checked; source equations re-read. |

## Finite evidence and its scope

- Both three-player/four-strategy witnesses: all 82,944 typed maps, all 64 profiles,
  exact 12 automorphisms, all 8 subgroups, zero complements. One witness uses
  three payoff values for a simple proof; strengthened witness uses two.
- Binary full-player-image groups: all 5 at n=2, all 15 at n=3, all 35 at n=4.
  Orbit-equality constraints and formal face-square coefficients cover **all
  real invariant payoff assignments** in these finite domains. This is not
  a count of nonisomorphic games. Group-only matching flags are explicitly
  distinguished from extra symmetry forced in every invariant game.
- Alternate four-player/six-strategy witness: analytic color reduction plus
  all 98,304 remaining maps;192 exact automorphisms and no commuting involutory
  lift pair. It is a separate corroborating construction, not the minimized
  main witness and not a second copy of the same game.
- None of these finite checks substitutes for E2's proof at arbitrary n.
  Finite potential-family checks do not sample numerical payoff orders.

## Original audit remains traceable

The original 41-result registry remains 33 verified, 7 corrected/clarified,
1 unresolved original wording (4.10). Phase3-specifications.md settles the
replacement interpretation of 4.10 and supplies the preference and geometry
quantifiers. It does not retroactively claim an original unspecified group
structure. New results have their own IDs here rather than changing the
meaning or denominator of the original audit counts.
