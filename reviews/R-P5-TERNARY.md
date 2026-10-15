# R-P5-TERNARY: final boundary audit and separate cross-checks

Status: **internal review; no mathematical defect found in P4-T1/T2/T3**.
This agent received the full prior project context and the assignment to audit
standard-cycle normalization, finite exhaustion, actual-group classification
and utility-level transfer. It read AGENTS.md, roadmap, theorem-audit,
review-log, the Phase 4 boundary proof and its generating implementation.
The agent independently implemented tuple composition, conjugation, generation,
cell orbits, closures, sections and matchings without importing any Phase 4
module. This is same-family AI assistance, not blinded or human peer review.

## Independent findings

The three-player standard subgroup can indeed be normalized to contain a bare
three-cycle. No section containing that specific cycle is assumed. Full actual
player image supplies an odd lift, with no payoff-genericity assumption.

The normalizer of the bare cycle subgroup has order36, consisting precisely
of a common strategy permutation and an arbitrary player permutation.
Normalize the odd player image to one transposition, then quotient216 local
triples by its twelve-element normalizer stabilizer. This yields32 lift
classes, independently counted by Burnside. Their generated groups form11
normalizer-conjugacy classes, comprising19 embedded groups. The new verifier
reconstructs the Phase 4 order histogram and sections, independently of the
previous certificate; full payoff closure leaves only the three twisted
order-six groups as possible generating obstructions.

The proof forcing a nonfull actual automorphism group into the parity fibre
product is valid: apply closure separately to every odd element, then multiply
by one fixed odd element to constrain all even elements. The remaining kernel
has order1 or3, giving actual full groups of order6 or18. This covers accidental
parameter equalities. Confusing the subgroup with its payoff closure would
invalidate the argument; neither proof does so.

Min-max and distinct-level-rank normalization give literal group equalities,
including constants. Standardness, projection, section and matching questions
therefore transfer exactly to cardinal and ordinal groups. The four-action
binary-payoff nonsplitting witness is unchanged by either normalization. The
strategy-count minimality statement remains limited to three players.

Outputs: research/phase5-ternary-audit.md,
experiments/phase5_ternary_audit.py,
experiments/phase5-ternary-audit-results.json,
experiments/test_phase5_ternary_audit.py. The two dedicated tests pass, including
complete certificate regeneration and the separate Burnside count. The proof
still includes an eleven-case finite lemma; no computation-free symbolic
classification is claimed.

## Separate review of P5-M1

After completing the ternary audit, the agent read
research/phase5-mechanisms.md. The arbitrary-m opposite-face construction's
analytic exact-group proof is sound. For the binary coarsening, surjectivity
of the profile is detectable from the payoff-vector sum. Fixing two equal
coordinate labels leaves exactly (m−1)! surjective completions. Fixing unequal
labels leaves 2(m−1)! completions with an already fixed label duplicated and
(m−2)(m−1)!/2 with a new label duplicated. The resulting counts differ for
all m≥2, including m=2, forcing every local map to coincide. Opposite parity
then sends a positive utility to a negative one and cannot preserve the binary
game. The full group, splitting, standardness and no-full-matching statements
follow, without extrapolating the m=2,3 enumeration. No defect found.

## Separate review of R2

The agent read research/phase5-reductions.md and independently checked the
clone-quotient extension. Full-vector clones form a well-defined canonical
quotient; induced maps preserve fibre multiplicities. The kernel is exactly
the product of symmetric groups within fibres. Fixed numbering of each fibre
supplies a homomorphic section onto the multiplicity-preserving quotient group,
not necessarily onto the complete automorphism group after forgetting
multiplicity. Its fixed-player identity components remain identities, proving
the claimed I/C/M/S equivalences. Sections descend injectively because player
projection is retained. No defect found. A minor expository suggestion was to
specify the row/column subsets in the rectangular-restriction example.

Novelty and source priority were not adjudicated in this review. A symbolic
replacement of the finite ternary lemma, and all arbitrary-player ternary
splitting claims, remain outside its conclusions.

## Separate adversarial review of P5-S1/S2/S3

After the previous reviews the agent read research/phase5-splitting.md in full.
The quotient reduction is valid. An order-four binary quotient lift gives an
order-four ternary lift by cubing when needed. The binary player kernel is
0,T,E orV; the central-T involution, braid-defect and distant-commutator
analysis excludes both alternatives using the descended standard subgroup.
The only residual quotient is the determinant-even E-kernel group.

The four distinct nontrivial E-characters over F3 force a translation kernel
of zero or all F3^4. Full translations force a constant game. For zero kernel,
averaging the cocycle over the normal order-eight E is legitimate in
characteristic three, and E has no fixed vectors; the displayed conjugacy
argument kills the whole cocycle. No averaging over the order192 quotient is
used. For the remaining pure sign group, the payoff argument covers profiles
with zeros by parity absorption and profiles without zeros by the two even-sign
orbits joined by a focal-fixing odd player permutation. Thus the actual game
group must be strictly larger. No missing payoff-realizability condition was
found.

The regular-C4 branch also survives: the eight player three-cycles normalize
under cycle conjugation and inversion, and the 1296 local lifts reduce to251
classes by common strategy conjugation. Independently coded tuple operations
reconstructed **all251 generated groups**, obtained exactly the saved21 groups,
and verified every saved section belongs to its group and generates24 elements
with24 distinct player permutations. No project group implementation was
imported. The durable independent implementation is
experiments/phase5_ternary_four_crosscheck.py; its --exhaustive option repeats
all251 closures, while its default quickly checks all21 group/section
witnesses and the251 conjugacy classes. The dedicated unit suite includes the
latter check. The full one-off independent reconstruction completed
successfully during this review; the equivalent durable script was then saved.
No defect found in the candidate four-player ternary splitting theorem.

## Final separate review of unbounded P5-S4/P5-S5

The agent read the newly appended arbitrary-player statements and proofs after
the fixed-size review, without rerunning unchanged finite certificates.
No defect found. The E-character argument includes n=3: its three coordinate
characters are distinct and nontrivial; the same holds for every larger n.
Every averaging denominator is a power of two and invertible in F3. Thus the
translation-kernel dichotomy N=0 or all R remains valid. For N=0, normal E and
its zero fixed space kill the cocycle. The E/V binary-kernel alternatives then
force bare player symmetry: the parity graph's two nonzero-profile orbits are
joined by a transposition fixing the focal player, which exists exactly in
the required range n≥3. Zeros absorb sign parity as claimed. This establishes
P5-S4 for actual full game groups without standardness.

For P5-S5, R/N is legitimately a B-module. The image of G has zero translation
kernel there and is a cocycle graph. The central order-two global sign flip
acts as minus identity on R/N, so its fixed space is zero even when N is a
proper invariant subspace. Averaging over that order-two subgroup, then using
normality, kills the whole cocycle. Lifting the conjugating translation gives
exactly N semidirect B: each residual translation lies in N and can be
cancelled. The binary central-kernel splitting proof is valid at n=3 and
n≥5 by involution lifts and adjustable adjacent braid defects; its n=4
exception cannot contain a descended standard subgroup. Hence the stated
standard groups split in all n≥3.

The resulting necessary condition for an arbitrary-player ternary nonsplit
counterexample, zero local-sign kernel, follows from the complete invariant
subspace list 0,T,E,V. It is only a necessary condition: no existence or
arbitrary-player splitting theorem is inferred. These are algebraic reviews;
novelty and external peer review remain unresolved.

## Final separate review of P5-S6

The agent independently attacked the subsequent nondivisibility theorem and
then read its saved statement/proof. No defect found. When the sign kernel is
zero, the binary quotient is a complement over S_n. Choose reference-player
transversals t_i and let chi_i(p) be its C2 local label. The composition rule
gives

    chi_i(p)=a_i+a_{p(i)}+phi(t_{p(i)}^-1 p t_i),

where a_i=chi_0(t_i) and phi is the reference stabilizer character. That
character is trivial or parity for n≥3; absorbing the transversal parities
into a_i gives exactly the ordinary or global-parity complement. This
independently confirms the normalization invoked in P5-S6.

Over F3 the transposition-difference argument gives the complete invariant
subspace list 0,T3,E3,R, under either permutation or scalar parity-twisted
action. If 3 does not divide n, the displayed constant-line projection is
well defined and equivariant, so every one of these subspaces has an
invariant complement. The quotient cocycle lifts through that complement;
the lifted graph really lies inside G since G contains the whole translation
kernel N. Its player projection is an isomorphism. No invalid averaging over
S_n or assumption of cocycle triviality is used. Combined with P5-S4/S5,
the stated standard/full-image splitting theorem follows, and P4-T1 excludes
n=3 separately. Thus six is correctly identified as the first remaining
player count, rather than as an established counterexample.

The zero-sign-kernel part itself does not require standardness. At n≥5 the
constant-sign-kernel Coxeter argument also does not require it; consequently
one could strengthen P5-S6 for n≥5 not divisible by three to require only
actual full player image. The present statement is a valid conservative
formulation. No modular n divisible by three conclusion was checked or
asserted here.

## Independent six-player binary common-interest witness audit

The agent received the proposed ATLAS-derived six-player construction after
finishing the preceding independent reviews. It initially ran the exploratory
script, confirmed the seven-orbit counts, and found that assigning binary
payoffs to its first utility-cell orbit already preserves the exact group.
It then received the smaller common-interest C18 construction and independently
implemented that construction instead: no project group, cell, closure or
matching functions are imported by
experiments/phase5_ternary_six_crosscheck.py.

Using literal eighteen-point generators, fixed block labels, and six literal
codeword seeds, the new implementation verifies all of the following with
its own permutation composition and subgroup closure:

- The preserving group has2160 elements and720 distinct player permutations.
- All2160 elements preserve the eighteen-profile set C18, so preserve every
  utility u_i=1_C18.
- Exhausting all46656 pointwise-player local bijections finds precisely three,
  the common cyclic shifts of all strategies. Forward preservation of C18
  suffices because every tested map is a bijection of the full profile set.
  Thus the full numerical game group has order at most720*3=2160 and is
  exactly the proposed group, with no untested odd-player overgroup.
- The literal supplied standard generators give a subgroup of order60,
  transitive on six players, and every element fixing a player acts identically
  on that player's strategies. Standardness is checked directly; no A5 name
  or advertised ATLAS group identity is used to infer it.
- The even-player preimage has1080 elements. The subgroup generated by all
  conjugates of the commutator of its displayed generators equals the whole
  even preimage. It is therefore perfect.

If a section onto S6 existed, its A6 subgroup would have index three in this
perfect1080-element preimage. The action on the three cosets would give a
nontrivial transitive image in S3. A homomorphic image of a perfect group is
perfect, while S3 has no nontrivial perfect subgroup. This contradiction
establishes nonsplitting, without assuming a group name or Schur multiplier.
The proof and all finite counts survive independent reconstruction. A
meaningful dedicated test now runs this independent witness verifier.

An additional direct distance check found135 unordered C18 pairs at Hamming
distance4 and18 at distance6, with no other pair distances. Common cyclic
translation supplies all three labels in every coordinate. Thus replacing
any displayed coordinate label by either other label at a codeword leaves
the code, proving full-vector clone-freeness. No coding-theory novelty claim
was assessed: the point generators are prior ATLAS data, and identification
and attribution of the code are separate source-comparison questions.

Combined with the independently reviewed ternary splitting results at three,
four and five players, this is a six-player minimality conclusion for the
stated standard/full-image nonsplitting property within ternary games. The
binary utilities imply exact, cardinal and ordinal groups coincide for this
witness. These are internal finite and proof checks, not external peer review.

## Bounded final review of P5-S8 and the analytic C18 kernel proof

Before the final commit, the agent read P5-S8 and the revised standalone
six-player obstruction proof. No defect found. In P5-S8, the sum-zero
translation-kernel quotient is one-dimensional; restriction of its cocycle to
A_n is a homomorphism, killed by perfectness for n≥5. The displayed elementary
commutator argument proves that perfectness without a classification theorem.
The residual C2 cocycle is zero or a coboundary as claimed. In the ordinary
constant-translation-kernel case, normalizing each transposition lift by a
common translation makes it an involution with zero translation on its fixed
coordinates. Distant commutators and adjacent-product cubes then vanish by the
stated support arguments, giving all Coxeter relations. This correctly leaves
only the common-parity action with common-C3 kernel, of order3n!, and the
previous theorem forces3|n. No existence or payoff uniqueness is inferred.

The revised analytic pointwise-kernel proof for C18 is also sound. Hamming
distance-six components are precisely the common-translation triples, forcing
all local affine slopes to coincide. Normalization by one common translation
leaves exactly twelve affine candidates. The agent freshly checked every one
of the eleven rejection-table entries and the precise distance-six/common-
translation characterization with its independent literal-code implementation.
All checks passed. No unchanged exhaustive certificate or full suite was
rerun for this bounded final review. The table and analytic reduction give a
shorter proof of the previously independently exhausted46656-map kernel claim.
