# Phase 5 mechanisms and cross-review

Internal Codex agent instance p5_mechanisms, shared project history and model
family; not blinded, not external peer review. The initial supplied lead was
the proposed opposite-face orientation construction, explicitly unproved.

## Initial work

Derived the exact full typed group of the signed opposite-face array for
n=m+1 players and m≥2 strategies. The root subsequently supplied the inspected
Hao–Cheng primary-source comparison; the signed array and its zero-sum
property are credited as prior rather than claimed new.

Found that binary coarsening retains exactly the same full group. Independently
proved the surjective-profile completion-count invariant for arbitrary m,
then checked all ambient typed bijections at m=2 and m=3. The binary theorem,
section, non-matching obstruction and clone-free argument are analytic.

A provisional stronger irreducibility inference was rejected before reporting
it as a result: full local stabilizer transitivity excludes rectangles
invariant under the entire group, but not rectangles invariant under some
full-player-image subgroup. The displayed section fixes proper strategy
orbits. The retained minimal-witness statement instead uses binary rigidity
to exclude proper restrictions retaining standardness, full image and absence
of full matching, at fixed four-player size.

## Cross-review of reductions and publication proofs

Read phase5-reductions.md and independently checked R1 and R2, including the
multiplicity-preserving quotient group, the number-preserving lift section,
and preservation of strategy-triviality. Requested explicit row/column sets
for the 2×2 restriction example; no mathematical defect in the propositions
was found.

Read phase5-publication-proofs.md. Checked the binary K=0,T,E,V cases, global
flip twist of a section, beta/gamma matching obstruction, ternary orbit-closure
argument, and all six listed profile-orbit utilities in the nonsplit witness.
The two excluded reflections send012 to032 and210 as stated. No defect found.

## Independent attack on the four-player splitting argument

Before reading a completed new proof, received and independently analyzed its
algebraic outline. Checked the (4,3,2) presentation and C4 normalization search.
An order-four player-cycle lift in the binary sign quotient lifts to an
element of order four or twelve; its ninth power has order four and the same
player permutation. This bridge is needed before using the C4 certificate.

For the determinant binary quotient, the even-sign group E acts on F3^4 by
four distinct nontrivial characters. Averaging character projections is valid
because8 is invertible in F3. Thus its invariant translation kernel is a sum
of coordinate axes, and player transitivity forces zero or the full space.
Full translations force all profile utilities constant and full player image
makes those constants equal. With zero translation kernel, averaging the
cocycle over E kills its restriction; normality then makes every cocycle value
E-fixed, hence zero. Averaging over the whole quotient would be invalid,
because its order is divisible by3; the stated argument uses E only.

Finally checked the payoff-closure contradiction. A profile with an inactive
strategy coordinate permits a parity adjustment on that coordinate without
changing it, so even-sign flips realize every active-coordinate flip. On the
all-active face, even flips give the two parity classes; an odd player
transposition fixing the focal player has odd sign flips and merges those
classes. Hence every focal utility is invariant under all local sign flips.
Combining these with determinant lifts gives all bare player permutations,
contradicting the proposed exceptional sign quotient of the full actual group.
The binary-kernel reduction can use the prior algebraic K=0,T,E,V proof;
the35-subgroup calculation should remain an independent finite check rather
than an unexplained completeness assertion.

After the full draft `research/phase5-splitting.md` was written, read it in
full. The K=0,T,E,V reduction is now analytic. The two adjacent braid defects
in the central-line case can be killed successively without changing distant
commutators; the standard double-transposition exclusion is correctly used.
The eight player three-cycles are covered by powers of the regular cycle and
inversion, and the simultaneous-local-conjugacy Burnside count is251. The
finite section certificate additionally generates the alleged section and
checks order24. No unsupported inference from abstract group possibility to
actual payoff realizability was found. No defect found in the completed
P5-S1/P5-S2/P5-S3 proofs, conditional on reproducing their specified finite
certificate. Exact/cardinal/ordinal transfers use normalized exact groups.

Actually ran `python3 experiments/phase5_splitting.py --verify` after reading
the completed draft: saved certificate reproduced exactly,251 representatives,
21 generated groups, zero without sections. This is a rerun of that author's
implementation, distinct from an independent implementation; the independent
contribution here is the proof attack described above.

## Final arbitrary-player sufficient conditions

Read the appended P5-S4/P5-S5 and independently checked them. For n≥3 the
coordinate characters of E are distinct and nontrivial, including at n=3;
all averaging denominators remain powers of two. The large-kernel result
correctly uses actual payoff realizability in the parity-graph case, where
inactive-coordinate absorption and a focal-fixed transposition force the
missing local sign symmetries. Undoing translation conjugation transports
bare player permutations to a full matching.

For K=T, N is B-invariant, so quotienting gives a well-defined cocycle graph
in (R/N) semidirect B. The central order-two sign element acts as minus the
identity on R/N, and has no nonzero fixed vector in characteristic three.
Averaging over that subgroup therefore kills the entire cocycle. Lifting
the conjugating quotient vector gives exactly N semidirect B, not merely
an embedding into such a group. The binary central-kernel Coxeter argument
supplies sections at n=3 and n≥5; standardness excludes the exceptional
four-player case as stated. Thus the remaining zero-sign-kernel obstruction
is correctly scoped. No arbitrary-player splitting theorem has been inferred.

The proposed six-player triple-cover route is only a lead. Before claiming
a game example it needs a represented embedding, a genuine strategy-trivial
transitive subgroup, and exact payoff-orbit closure. Checking orders of lifts
of player elements of cycle type3² may already constrain standardness;
no class-order or subgroup-exhaustion claim is established in this review.

## Six-player ternary nonsplitting: independent raw-data reconstruction

After the splitting agent found the ATLAS degree18 group, the root supplied
its two raw generators and the candidate claims. Implemented a new standalone
verifier `experiments/phase5_six_independent.py`, importing no project group
code. This uses right-word closure on the raw18-point permutations, a direct
block-coordinate representation, and union-find for focal-profile orbits.
It receives the explicit six blocks and order60 subgroup generators as data,
then verifies their assertions; no unverified identification with a named
ATLAS group or A5 is needed for the conclusions.

Actually ran the verifier and its two tests. It obtains group order2160,
full player image720, pointwise-player kernel3, seven utility-cell orbits of
sizes108,216,270,540,1080,1080,1080, and a subgroup of order60 that is transitive
on players and acts identically on every strategy fibre at every fixed
player. Exhaustion of all6^6=46656 pointwise-player strategy permutations
finds only three preserving the orbit game. Its full actual group therefore
has order at most720·3=2160, and already contains the computed group of that
order. This proves equality without enumerating all33,592,320 ambient maps.

The even-player preimage has order1080. A commutator of two explicit elements
in it has conjugates generating the entire preimage, verified independently;
thus this preimage is perfect. A section over S6 would give its restriction
over A6, a subgroup of order360 and index3. Its coset action maps the perfect
1080-group into the solvable group S3, hence trivially, contradicting index3.
This proves nonsplitting without relying on ATLAS nomenclature.

Also independently verified the simplified binary common-interest game:
its winning set is the18 words obtained by adding constants in F3 to the six
supplied seed words. Both group generators and both standard-subgroup
generators preserve this set. Exhausting the same46656 pointwise maps again
leaves only three, so its exact automorphism group is the same2160-group.
The previous standardness and nonsplitting proofs apply unchanged.

The seed matrix appears to be a generalized Hadamard GH(3,2) array; this is
a literature lead, not a novelty claim. The raw code/group must be credited
to the actual source. The independently established game consequence is a
standard, full-player-image, nonsplit ternary game with six players, already
with binary common-interest utilities. The earlier universal ternary-splitting
possibility is therefore false; the three/four-player proofs remain valid.

## Final boundary/type and analytic-kernel review

Read final P5-S6 and P5-S8 in full. P5-S6 correctly lifts a cocycle through
an invariant direct summand when3 does not divide n; it does not incorrectly
assume every cocycle is a coboundary. The ordinary and parity-twisted natural
modules have the same invariant subspaces and the stated equivariant direct
sum in this case.

P5-S8 correctly excludes N=E3: its one-dimensional quotient cocycle restricts
to a homomorphism from perfect A_n to the additive F3, hence zero, and the
remaining C2 cocycle is zero or a coboundary for trivial or sign action.
The displayed double-transposition commutator supplies the claimed elementary
proof of A_n perfectness. For ordinary N=T3, shifting each adjacent
transposition lift by a common translation makes it an involution and zeros
all its fixed-coordinate translation entries. The disjoint commutator and
adjacent-product cube have proper coordinate support, hence cannot be
nonzero common translations. The resulting Coxeter section excludes that
case. The retained sign-twisted common-C3 extension type and3|n necessity
are therefore correctly stated as necessary rather than sufficient.

Read the final analytic six-player kernel proof. Hamming-distance-six triples
are intrinsic and force a common affine slope in every pointwise-player
automorphism. Normalizing one codeword image leaves the asserted twelve
candidates. Independently recomputed all eleven rejection-table entries from
the six seeds; every displayed witness indeed maps outside C. This is a
short analytic full-kernel proof supplemented by the previously performed
exhaustive46656-map check. No defect found in the final formulations.
