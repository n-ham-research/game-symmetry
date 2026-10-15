# R-PH4-BINARY-A: binary reconstruction and later ternary cross-review

Status: internal adversarial review; no external peer review or novelty claim.
Actual worker: a Codex subagent assigned binary theorem reconstruction. No
specific backend model build or unperformed human approval is asserted.

The complete mathematical record is
`research/phase4-binary-verification.md`. Initial work reconstructed the
kernel and lift arguments before reading prior agent reports, then attacked
the existing Phase 3 proof directly. The worker saw the proposed theorem and
repository context and later inspected the beginning of its existing
computational search. It wrote a separate generic quotient-cocycle solver,
with no imports of the old search. Shared mathematical ideas and model family
limit independence.

Findings: no defect in P3-E1/E2/E3. Explicit checks target the even-n module
case; signed stabilizer normal form; all distant Coxeter commutations at
n>=5; the exceptional n=4 opponent normalization; n=3 payoff-orbit potential;
and n=1,2 boundary cases. The new exact solver covers all embedded full-image
subgroups at n=3,4,5,6, counts 15,35,51,99. All arbitrary-real payoff families
pass square circulation. Every n>=5 family forces a full matching; the eight
exceptional n=4 families are own-action indifferent.

Later supplied P4-M2 and the ternary worker's completed certificate, this
worker checked their analytic arguments and independently reconstructed the
finite certificate through permutations of all 81 utility cells, importing
none of the generating code. All 648 odd generators give the same 19 groups;
every complement and orbit-closure verdict checks. Exact orientation-game
Aut has order 18, kernel 3 and no full matching. The reduction obstruction
using common-payoff preservation checks. The conclusion that every standard
full-image three-player ternary game splits follows from the certified
exhaustion, with actual non-full group order 6 or 18. These conclusions are
finite-domain claims, not unrestricted nonbinary classifications.

Validation: six focused tests in
`experiments/test_phase4_binary_verification.py` pass. Negative controls
reject matching pennies and unconstrained utility cells. A serialization
comparison initially failed because JSON keys were strings; key normalization
repaired it. No mathematical disagreement occurred in that failure. Main
manuscript and shared audit registry were not edited by this worker.

## Final targeted assignment-model review

Later task: inspect A4.1–A4.4 in `research/phase4-assignment-model.md`, with
particular attention to utility observations versus typed action histories.
The proposed model and proof were supplied, so this is a targeted cross-review.

One specification gap was found and reported to the coordinator: without
`t_0=1`, the arbitrary-transport converse in A4.2 yields
`u_i(t_i s)=u_0(t_0 s)`, not the printed `u_0(s)`. Explicitly normalizing the
reference transport to the identity repairs the stated equivalence. A4.1
itself is valid even without that normalization because its stronger exact
automorphism assumption preserves the reference focal utility.

The remaining arguments check. The participant has one explicitly calibrated
money utility across positions and sees the role before choosing an action.
Opponents' distributions are explicitly transported, rather than implicitly
assumed to agree across arbitrary role experiments. Individual exact role
realizations therefore suffice for equality of all conditional action values
and maxima; no section is needed for that conclusion. A4.2's all-action tests
and Dirac laws yield exactly the focal transport identity; simultaneous tests
of every recipient are needed to infer an exact automorphism.

For A4.3, two exact history implementations h1,h2 with player permutation p
satisfy `u_(p(j))(h1 s)=u_j(s)=u_(p(j))(h2 s)` at every pure profile.
Thus a common initial law gives the same final payoff distribution, despite
possibly different typed actions. A section is necessary only for the
stronger observation of player map and all strategy coordinates, as the model
explicitly requires. Observing the player map also handles degenerate action
sets where the profile action alone is not faithful. Extra action costs would
change the consequences and require recomputation of the automorphism group.

A4.4 correctly keeps cross-role calibration separate from cardinal or ordinal
normalization. A recommended wording refinement is to state the demonstrated
scope directly: coherence is unnecessary for this one-shot equality, whereas
cardinal or ordinal symmetry alone does not determine cross-role monetary
values. No new experiments were run for this targeted review.

The later full statements P4-T1 and P4-T2 in
`research/phase4-ternary-boundary.md` were also read against that independent
certificate reconstruction. P4-T1's strategy-count minimality handles one or
two strategies correctly by embedding the represented group in the ternary
ambient group with extra fixed actions; a section of a contained subgroup
remains in the original embedded group. P4-T2's two-group classification
correctly uses every odd element of the actual group and payoff-orbit closure,
not merely one chosen generating pair. Both statements pass this independent
review. The displayed groups' section and non-strategy-trivial properties
follow from their common odd strategy maps, exactly as stated.
