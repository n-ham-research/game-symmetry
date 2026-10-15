# R-P3-SPLIT-B — independent counterexample search

Role: counterexample search, supplied with the Phase 3 request and repository
but no affirmative proof. Same-model internal review; not external peer review.

I reconstructed the actual Section 5.6 question from the immutable original
inventory and the proved 5.1/5.2 matching characterizations. I independently
found the signed-permutation obstruction documented in
`research/phase3-splitting-search.md`: four players, six actions each, nine
integer payoff values. It has exactly 192 automorphisms, player kernel
`C_2^3`, full player image `S_4`, and a pure strategy-trivial transitive `A_4`
subgroup. The actual player extension cannot split because disjoint
transpositions cannot have commuting involutory lifts.

The proof includes full-Aut identification, avoiding the common error of
constructing only a nonsplit automorphism subgroup. A tempting binary version
was rejected explicitly: its payoff-cell action is transitive and forces a
constant game, whose larger full automorphism extension splits.

After finding this candidate I was informed of agent A's smaller
three-player/four-strategy construction. The two constructions are distinct;
my construction was found before receiving its formula. That communication is
recorded here to avoid overstating blind independence. A's construction is
preferable if its full-Aut proof checks out. I have not claimed global
minimality or literary novelty.

## Independent review of the smaller construction

After completing the independent signed-permutation construction, I read
`research/phase3-splitting-proof.md` and its explicit table F. The improved
three-value proof is sound. Its sole zero forces all typed component maps to
be the same permutation f. Repeated-opponent profiles yield
`L(f(b)-f(a))=L(b-a)` with `L^{-1}(1)={1}`, forcing f to be a translation of
Z/4. The unequal entries `F(0,1)` and `F(1,0)` force the translation parity to
equal player-permutation parity. This establishes the claimed full group.
Every lift of a transposition squares to the nonidentity common translation
by 2, excluding every section. The pure A3 subgroup establishes standardness.
No inference here depends on classifying that group by its abstract name.

## Independent review of the binary theorem argument

Agent C communicated the case proof before its full write-up. I checked its
key reductions independently. A permutation-invariant subspace of F2^n is
one of `0`, the global-flip line T, the even-weight space E, or all V: any
nonconstant vector gives a pair-vector by subtracting a transposed copy;
permutations generate E, and any odd vector outside E generates V together
with E. The kernel E payoff-parity reduction is consistent with exact
preservation at a fixed focal player.

For kernel T, a transposition lift's square is supported on its two moved
coordinates, so cannot equal the global flip for n>=3. Disjoint-transposition
commutators are supported on their four moved coordinates, so vanish for
n>=5. Global flips of adjacent-transposition lifts can recursively repair all
braid defects along the Coxeter chain without changing squares or distant
commutation. For n=4, if the disjoint commutator is nontrivial, every lift of
a double transposition has order four. A transitive subgroup of S4 must
contain a double transposition: its Sylow 2-subgroup has order at least four;
an element of order four supplies one by squaring, while a Klein four
subgroup necessarily contains one. Thus a strategy-trivial transitive subgroup
cannot exist in this exceptional case.

Finally, the exceptional three-player twisted complement has a valid exact
potential even though majority-player payoff levels need not coincide.
Homogeneous profiles have one common focal payoff alpha, and minority cells
have one common payoff delta. A majority player's unilateral switch between
nonhomogeneous profiles is exactly an opponent transposition combined with
the global flip, so its utility change is zero. The potential is alpha on
homogeneous profiles and delta elsewhere. This verifies the delicate case
without accidentally replacing exact potential by common interest.

These checks were communicated to C and the coordinator. They support the
proof architecture, but final theorem scope must match C's completed written
proof and its boundary cases. Shared-model internal agreement is not proof or
external review.

## Computation actually run

`python3 experiments/phase3_split_search.py` completed successfully. It checked
all 98,304 color-preserving candidates and obtained exactly 192 automorphisms;
all 5,184 payoff cells were then checked for every survivor. Each of the two
disjoint transpositions has four involutory lifts, and none of the 16 pairs
commutes. No network source was inspected or novelty conclusion drawn in this
subtask.

### Stronger four-player exceptional case

C then supplied a stronger lemma for the nonsplit kernel-T four-player case.
I checked the argument independently. Fix focal i. For every opponent swap
(jk), choose its unique lift t that flips i. The commutator with a lift of the
disjoint swap (i ell) is the global flip, giving
`v_t(i)+v_t(ell)=1`; hence t fixes the remaining opponent ell's bit.
The lift is involutory. For two adjacent opponent swaps, their product has
zero focal flip; its cube lies in T and thus must be identity. These lifts
therefore form an S3 section acting strategy trivially on opponent fibers.
Straighten it using the matching correspondence. Any binary opponent triple
has two equal bits; their transposition fixes all opponent actions and flips
the focal bit. Exact payoff preservation gives independence of the focal
player's own action. Repeating for each focal proves that every profile is a
Nash equilibrium and the zero function is an exact potential. This removes
the need for the standardness hypothesis in the four-player exception.
I communicated approval of this proof architecture to C and the coordinator;
C's final written proof should be read for its full theorem statement.

## Two-payoff strengthening reviewed

I read P3-S1b after A supplied the completed refinement, rather than deriving
it independently. Its proof passes. The six profile-orbit representatives
have the stated utilities and sizes: constants give four profiles; the three
nonzero repeated-to-distinct differences give three disjoint 12-element
orbits; the remaining 24 all-distinct profiles split into the two stated
12-element orbits. The latter representatives cannot be equivalent because
their common three-element action subset admits no nonzero translation and
the required zero-translation player swap would be odd. This verifies the
simultaneous-zero diagonal locus.

The unique positive payoff in each two-equal profile forces the common
strategy map to preserve or reverse action parity according to the player
permutation. For even player permutations, the four parity-preserving maps
are exactly the two even translations and two reflections. The profile
(0,1,2) excludes both reflections with the stated focal payoff comparison.
For odd player permutations, composing with the inverse of the known lift
with the same player permutation and translation 1 correctly reduces to the
even case. Thus the exact full automorphism group remains the nonsplit group
already proved. One global payoff value makes every cell equal, so two payoff
values really are minimal in that explicit alphabet sense. This is not a
claim of binary action sets or minimal strategy count.
