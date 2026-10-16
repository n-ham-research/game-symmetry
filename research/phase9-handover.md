# Phase 9 Game Symmetry handover

16 October 2026. Status: review preparation and independent internal proof
reconstruction of existing candidate extensions. No new classification,
priority claim, external contact or submission. Baseline source commit:
`2b2a9c44ad9ad10284dc265aba4d82e52c6741d5`.

## Sharp ternary theorem retained without expansion

The complete exact automorphism group, exactly three strategies at every
player, full actual player image, and the stated standardness hypothesis
at the small player counts remain essential to the only-six assertion.
Splitting means a section of the player projection; full matching symmetry
additionally requires strategy triviality. Neither is a definition of fairness.
The existing briefing remains the starting review packet. No theorem or
manuscript source changed in this pass.

The following independently checkable interfaces should be reviewed in order.
A multiplier expert's approval of the last line cannot certify the earlier
reduction.

| Interface | Object the reviewer must reconstruct | Falsification target / expected evidence |
|---|---|---|
| Actual group | Fixed-recipient utility cells `(i,s)` and their orbit closure | A claimed extra map must preserve each transported recipient payoff, not merely the profile orbit partition. Replacing the actual group by a selected preserving subgroup is refuted by the recorded `D_n` family. |
| Sign kernel | `K=0,T_2,E_2,F_2^n`, and character projections on translations | Check the exceptional characteristic-two module inclusions, and all support bounds when `n=4`. Do not assume a semisimple permutation module. |
| Payoff closure | Nonzero product classes and zero-coordinate parity adjustment | Verify the correcting opponent transposition fixes the recipient; preserve the zero-coordinate profile itself. |
| Residual module | `N=0,T_3,E_3,R` under ordinary or parity-twisted action | Check normalization of stabilizer characters, the graph-cocycle lift through an invariant complement, and why `3` dividing `n` is necessary for the remaining obstruction. |
| Multiplier | Central extension of perfect `A_n` by `C_3` for `n>=8` | Universal-central-extension image supplies a complement; the entire even preimage need not be perfect. Its derived subgroup is the characteristic complement. Odd transposition lifts invert their square and hence are involutions. |
| Attained action | The 18 listed words, complete kernel, image, standard subgroup, perfectness | Reproduce from tracked data. Identifying an abstract group of order 2160 alone does not prove any of these represented-action facts. |

These are precise outstanding specialist questions, not newly suspected
errors. The full reduction was reread, including the `N=E_3` cocycle
argument: restriction to perfect `A_n` vanishes, the remaining `C_2`
cocycle is zero for trivial action and a coboundary for sign action over
`F_3`. The ordinary-action `N=T_3` branch uses normalized involutions
with zero translation on fixed coordinates; the support bound for distant
relations requires `n>=5`. No defect was found. Existing Phase 7/8 records
contain the full proofs; this handover avoids replacing them with consensus.

## Binary exact-potential contribution remains active

Candidate identifiers P3-E1–E3 retain their original scope and novelty status.
This pass reconstructed the delicate four-player argument from the affine
law `(b,p)(c,q)=(b+P_p c,pq)` rather than inferring it from finite tests.
If the constant flip is the distant commutator, normalize a lift of the
opponent transposition `(jk)` to flip focal player `i`. Comparison with a
lift of `(i ell)` forces its flip at the remaining opponent `ell` to be
zero. Two normalized adjacent opponent lifts both flip `i`, so their
product does not; its cube belongs to the constant kernel and has zero
focal component, hence is identity. Their opponent action is an ordinary
`S_3` after coherent opponent labels. Repeated opponent bits then supply
an odd stabilizer fixing their profile and flipping `i`. Thus every focal
payoff is independent of its own action. Separate focal labels suffice;
a single simultaneous opponent matching is not assumed. Constant potential
works in this branch.

The signed three-player branch was also reconstructed: majority-to-majority
bit changes have zero payoff gain; minority-to-homogeneous changes have gain
`alpha-delta`. The potential is `alpha` on homogeneous profiles and `delta`
on the other profiles, including coincident parameters. This does not assert
common payoffs. The ordinary branch uses the established cumulative
population-count potential. At two players, matching pennies prevents the
image-only extension. These are proof checks of existing candidates, not
newly discovered classifications or fresh independent human review.

### Actual primary source progress

The primary [Cheng–Liu author manuscript](https://arxiv.org/pdf/1701.06807v2),
*Linear Representation of Symmetric Games*, arXiv:1701.06807v2 (8 March 2017),
was inspected in §§8–9, Definition 68, Theorem 71, and Appendix C on PDF
pages 19–20 and 23. Its wrapper is dated 8 March 2017 while the first-page footer says preprint
submitted to Automatica, 4 September 2018; this version discrepancy is
retained rather than silently assigning all passages a 2017 composition date.
Its title is not the final 2018 Automatica title.
Definition 68 specifies a relation between focal and reference utilities
obtained by flipping their two coordinates. Theorem 71 solves the potential
equation for that class. Appendix C verifies the matrix factorization.
This is a substantive prior potential result beyond ordinary/renaming
symmetry and must be included in any binary-potential paper comparison.

That relation flips coordinates without performing the player transposition;
it is not the signed player-action lift used in P3-E2's exceptional branch.
Their separate hypotheses must be compared before transferring either
result. This source supplies no justification for claiming the full-image
classification is new; nor can its special-class result alone discharge
the classification argument. The final 2018 *From Boolean game to potential
game* remains uninspected: the publisher's abstract identifies flipped
symmetry, but its body failed to open this pass. Preprint/final equivalence
is not established. Final Cao–Yang 2018 and Wang–Li–Feng 2024 proof-body gaps
also remain as listed in phase4-source-requests.md.

A bounded refresh of the primary author-hosted long updated version of
[Tewolde et al., *Computing Game Symmetries and Equilibria That Respect Them*](https://emanueltewolde.com/files/symmetries.pdf)
confirmed its introduction's complexity focus and its statement that
Theorem 4 resolves Cao–Yang's name-irrelevant-symmetry **decision-complexity**
conjecture. This is not the binary potential or lifting conjecture. The
version describes itself as a long updated AAAI 2025 paper; no unprinted
revision date or equivalence with earlier arXiv versions is inferred.
This refresh inspected the introduction, not all theorem proofs. It is
relevant context for the proposed agent work but supplies no novelty clearance.

The group-theory/code-design priority comparison remains unresolved. No new
primary text in this pass replaces ATLAS, Gillespie–Ó Catháin–Praeger or
Lassueur–Mazza; their attribution in Phase 8 stands. In particular the code
indicator encoding, classical multipliers and represented triple cover
remain prior mathematics.

## Review and next action

The delegated p9_symmetry Codex instance had the user's brief, inherited
context and existing proofs. It reconstructed selected arguments and read
the named primary passages. This is same-family internal review, not
blind or external peer review. Root cross-review is recorded separately
when actually performed. No third independent reviewer is asserted.

The next valuable work is specialist criticism of interfaces 1–3 above,
followed by independent certificate reproduction and a targeted final-source
comparison for P3-E2. Preserve the existing binary proof, experiments and
source queue; do not open a third publication project from this programme.
No broad enumeration or mathematical generalization is proposed here.

Validation: the 88 experiment tests, original-source audit and unchanged
manuscript build are rerun for this packet; final outcomes are recorded in
the review log. No layout edits occurred, so no fresh rendered-page
inspection is claimed. `games-symmetry.zip` remains untouched and untracked.
