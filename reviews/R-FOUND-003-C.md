# R-FOUND-003-C — foundation and selected result audit

16 October 2026. Internal mathematical review by a reused Codex agent instance.
This is not external peer review or author approval. The instance previously
reviewed Theorem 3.21 and the four initial correction findings, and received the
coordinator's proposed Corollary 4.24 correction. It independently reconstructed
the arguments below without reading the new A/B reports. It read AGENTS.md,
roadmap.md, theorem-audit.md, review-log.md, the result inventory, and original
v5 TeX sources under /tmp/ham-v5-source. Prior exposure limits independence.
No novelty claim is made. Existing numbered statements are literature / previously
established by Ham; strengthened scopes below are candidate extensions only.

Convention: (P_pi s)_j=s_{pi^{-1}(j)}, composition right to left. All original
games are finite, explicitly section-background.tex:48. Singleton strategy sets
are allowed. The one-player extensions below are outside the original n>=2 scope.

| ID | Original statement | Original proof / required action |
|---|---|---|
| 2.2 | Incorrect, third assertion | Replace with exact surjectivity criterion; first two assertions valid |
| 2.3 | Verified | Valid proof; choose an optimizer rather than equating an element to an argmax set |
| 2.4 | Verified | Proof (ii) has incorrect player order; replace display |
| 2.5 | Verified | Finite zero-sum minimax theorem; source cites literature without a proof |
| 3.4 | Verified | Interpret focal/opponent pair as reconstruction of the indexed full profile |
| 3.5 | Verified under typed groupoid reading | Tag source/target objects explicitly |
| 3.6 | Verified under typed groupoid reading | Replace malformed inverse-coordinate display with typed inverse |
| 3.23 | Verified | Supply mixed minimax argument |
| 3.25 | Verified | First proof sentence has wrong payoff index; subsequent argument has intended index |
| 4.24 | Incorrect as written | Full typed bijection group, not automorphism group, repairs statement |
| 5.6 | Verified | Injective player projection plus group order and a regular cyclic subgroup |
| 5.11 | Verified statement; defective proof | General swapping bijection and mixed minimax required |

## Corollary 4.24: direct independent derivation

Original source section-bijections.tex:243–250 says G<=Gamma, explicitly
G<=Aut(Gamma) by line 150. Let n=2, A_1=A_2={0,1}, u_1=0, u_2=1.
Every player stabilizer in S_2 is trivial, so the identity relabelling establishes
(i); every matching establishes (iii). In fact all coordinate permutations
preserve each constant payoff separately. But a swapping automorphism would
require u_1(s)=u_2(g(s)), or 0=1. Thus (ii) fails.

The corrected condition is G<=S_Gamma, where S_Gamma consists of typed bijections
(pi;(g_i:A_i->A_pi(i))_i), with full player image S_N, strategy triviality,
and u_i(s)=u_i(g(s)) whenever pi(i)=i. Do not additionally require g to
preserve payoff functions with moved player indices.

For a matching M, set t_ij=M_ij. Then t_ii=id and t_jk t_ij=t_ik.
The lifts M_pi=(pi;(t_i,pi(i))_i) form a group isomorphic to S_N. They
are strategy trivial. Relabel using q_i=t_ir:A_i->A_r for one fixed r.
The conjugated lift is exactly P_pi, so matching stabilizer invariance is
equivalent to weak anonymity after relabelling.

Conversely let G satisfy the corrected condition. If g,h carry i to j,
h^{-1}g fixes i; strategy triviality implies g_i=h_i. Write this unique
map as t_ij. Transitivity supplies every t_ij; composition gives coherence.
Define M={(t_ri(a))_i:a in A_r}. Each coordinate projection M->A_i is
bijective. Every g with player permutation pi has component t_i,pi(i);
full player image therefore gives G=M_SN. The stabilizer condition is precisely
(iii). This proves all directions without using an automorphism assumption.

Weak scope: the proof uses no payoffs arithmetic, finiteness of strategy sets,
or n>=2. It works for finite nonempty N, nonempty arbitrary strategy sets and
a common arbitrary payoff codomain. A further set-theoretic extension to any
nonempty player set works with 'player image equals S_N' replacing the finite
phrase 'n-transitive'; the same unique component maps construct the matching.
These scope extensions are candidate extensions, not priority assertions.
Unequal strategy cardinalities need not be excluded from the statement: each of
the three conditions already forces common cardinality. Empty N is excluded
because the reference-player construction and usual matching interpretation
change. Empty strategy sets are excluded as in the original game definition.

## Propositions 2.2–2.5

2.2, background:94–100: define F(p)(s)=product_i p_i(s_i). Finite sums give
sum_s F(p)(s)=product_i sum_a p_i(a)=1. The i-th marginal is p_i, proving
injectivity. If at most one A_i is non-singleton, any distribution is determined
by that coordinate and is a product. If A_i,A_j each contain two distinct
actions, fix all other coordinates and put mass 1/2 on each diagonal profile.
Both selected marginals give probability 1/2 to each action, so a product would
give mass 1/4 to absent cross profiles. Hence F is nonsurjective exactly when
at least two players have non-singleton action sets. This includes n=1: F is
the identity up to canonical indexing. Singleton-only games have a one-point
simplex. The source's parameter-count argument is unnecessary and its later
divisions need not have nonzero denominators; replace it completely.

2.3, background:243–256: multilinear expected utility is continuous on compact
products of finite simplexes. Inner minima/maxima and outer optima exist.
Choose x* maximizing min_y U(x,y), y* minimizing max_x U(x,y). Then
lower<=U(x*,y*)<=upper. Convexity of the opponents' product domain is neither
used nor asserted. For n=1 take the empty opponent product as a singleton;
both quantities become max_x U(x). The original argmax notation is a routine
element-versus-set imprecision, not a false inequality.

2.4, background:261–273: the statement lower_1=-upper_2 and
upper_1=-lower_2 is correct by U_2=-U_1, including singleton actions.
The printed proof (ii), lines 269–270, instead writes
upper_1=min_x max_y U_1(x,y). The correct expression is
min_y max_x U_1(x,y). For U_1=[[0,1],[2,3]], the true upper_1 is 2,
whereas the printed expression is 1. Correct the whole second chain to
min_y max_x U_1=-max_y min_x U_2=-lower_2. This is a proof error,
not a counterexample to the proposition.

2.5, background:275–277: finite zero-sum minimax is valid, including singleton
actions. An independent standard derivation is LP duality: maximize v subject
to x>=0, 1^T x=1, M^T x>=v1; its dual minimizes w subject to y>=0,
1^T y=1, My<=w1. Both are feasible and have finite optima. Strong duality
identifies lower and upper values. This invokes the established LP duality
theorem, not a new proof of that theorem. No two-player zero-sum conclusion
for one player is needed; a one-player zero-sum game has identically zero payoff.

## Propositions 3.4–3.6

Source label-dependent section:45–115. Use indexed products, or canonical
reconstruction maps rather than literal equality of differently nested tuples.
Let D_i=Delta(A_i), E_i=product_{k!=i}D_k. Write L_pi,i:D_i->D_pi(i)
for the identity on the common action-distribution labels and
R_pi,i:E_i->E_pi(i) for (R_pi,i y)_j=y_pi^{-1}(j), j!=pi(i).
Then P_pi(x,y)=(L_pi,i x,R_pi,i y), proving 3.4.

Both families have identity maps, inverses indexed by pi^{-1}, and composition
L_tau,pi(i)L_pi,i=L_tau*pi,i,
R_tau,pi(i)R_pi,i=R_tau*pi,i. These identities prove 3.5 and 3.6 for typed
morphisms. Distinct permutations may induce the same map; faithfulness is not
required. The source's line 97 candidate preimage has ambiguous/wrong indices;
the correct preimage of y in E_pi(i) is x_k=y_pi(k), k!=i. Line 108 also has
misplaced parentheses. No statement counterexample results after this repair.

Explicit typing matters if underlying simplexes coincide: use objects tagged
by i and morphisms carrying their source and target. A plain union of graph
maps need not retain intended player objects. This is a representation
clarification, not evidence that the intended subgroupoids fail.

## Propositions 3.23, 3.25 and Theorem 5.11

3.23, label-dependent:322–324, follows from the general argument below with
the strategy maps equal to identities. Finite mixed minimax is essential to
the zero value argument; pure best responses need not have a saddle point.

3.25, label-dependent:347–370, is valid for every finite game, without zero-sum.
For pi carrying i to j and preserving payoff pairs, multilinearity extends
U_i(x,y)=U_j(L_pi,i x,R_pi,i y). The separate bijections L,R allow changing
variables in each nested max/min, proving lower_i=lower_j and upper_i=upper_j.
The source first sentence at line 351 incorrectly writes u_i=u_i composed with
pi; the defining identity is u_i=u_pi(i) composed with pi. The displayed proof
then uses the correct latter identity. The appearance of Delta(A)_{-i} in its
first display should remain the independent product domain, not correlated
opponent distributions. For n=1 the fairness comparisons are vacuous.

5.11, label-independent:182–188: symmetry supplies a swapping automorphism
g=((12);(f:A_1->A_2,h:A_2->A_1)), not necessarily the bare swap. Push
probability distributions forward: (f_*x)(b)=x(f^{-1}(b)), likewise h_*.
Then U_1(x,y)=U_2(h_*y,f_*x). Consequently lower_1=lower_2 and
upper_1=upper_2 by independent bijective changes of variables. Zero-sum gives
lower_1=-upper_2; minimax gives lower_1=upper_1. All values are zero.
The source both assumes bare (12) is an automorphism and writes pure-strategy
min/max. Matching pennies exposes both omissions: the bare swap does not
preserve player payoffs, but a swap plus flipping one player's action labels
does; pure lower/upper values are -1 and 1, while mixed value is zero.

I earlier raised an infinite-game concern in a preliminary follow-up. Direct
inspection of background:48 withdraws that concern against v5: finiteness is
unambiguous. Infinite games are outside this audit's original scope.

## Proposition 5.6

Source label-independent:52–57. The player projection rho:G->S_N has kernel
G_N={id}, hence is injective. Since abstract G is isomorphic to S_N,
|rho(G)|=n!, forcing rho(G)=S_N. Choose an n-cycle c and its unique lift g.
Injectivity implies g has order n. The subgroup <g> projects isomorphically
to the regular cyclic subgroup <c>. No nonidentity element fixes any player;
therefore each player stabilizer in <g> is trivial, which implies strategy
triviality. This supplies a player-transitive strategy-trivial automorphism
subgroup and therefore standard symmetry. Combined with full player image,
this is n-transitively standard symmetry as claimed. No assumption on
Aut(Gamma)'s total order is used. For n=1 its trivial analogue also holds.

## Other foundation clarifications

Background:38–44 incorrectly makes all strictly increasing R->R maps a subgroup
of all bijections. exp is strictly increasing and not onto. Increasing
bijections form the required subgroup; positive affine maps are a subgroup.

Section-bijections:129: state the explicit group (S_m)^n semidirect S_n,
with S_n permuting n coordinates. In the usual imprimitive convention this is
S_m wr S_n, opposite to the printed order. n=2,m=3 gives actual order 72,
whereas S_2 wr S_3 has order 48 in that convention. An explicit semidirect
product avoids notation convention disputes.

An abstract isomorphism of groups never by itself identifies a specified
permutation action. Proposition 5.6 works because kernel triviality and finite
order establish surjectivity for the actual player action. In general preserve
the projection rho, its image and its kernel as part of the data. The profile
action can be nonfaithful: with singleton actions, every player permutation
acts on the same one-point profile space, but typed bijections remain distinct.

The collection Bij(Gamma,Lambda) for distinct objects is a hom-set, not generally
a group under composition; two arrows Gamma->Lambda cannot generally compose.
When nonempty it is a torsor for the source and target automorphism groups of
the relevant groupoid (full bijections or exact isomorphisms, respectively).
Whole typed collections form groupoids and endomorphisms form groups. These
distinctions prevent importing a group operation into an arbitrary hom-set.

## Supplemental reconstruction of previously verified formal results

Requested after the first report, to close the formal-result audit. The same
instance and independence limitations apply. Original statements and proofs
were checked directly again in the v5 TeX; no new A/B reports were consulted.
All twelve statements below are verified in their original ambient scope.
These are literature / previously established by Ham, not new results.

### 3.1, 3.2, 3.3, 3.8

Source section-label-dependent-symmetric-games.tex:11–41, 124–132.
For every coordinate j,

    (P_tau P_pi s)_j=s_pi^{-1}(tau^{-1}(j))
                     =s_(tau*pi)^{-1}(j)=(P_tau*pi s)_j.

Also P_e=id and P_pi^{-1}=P_pi^{-1} as inverse operators (the first inverse
here denotes the inverse permutation's operator). More unambiguously,
(P_pi)^{-1}=P_(pi^{-1}). This proves the left action in 3.1. Define
Q_pi=P_(pi^{-1}); then Q_tau Q_pi=Q_(pi*tau), so s acted on the right by
pi via Q_pi satisfies (s dot pi) dot tau=s dot (pi*tau). This proves 3.2
under the standard right-action convention. It is an antihomomorphism under
left operator composition, not another left representation.

For 3.3 evaluate either side at s: both give
u_tau(pi(i))(P_tau P_pi s). No invariance assumption is required.

For 3.8 let H={pi:u_i(s)=u_pi(i)(P_pi s) for every i,s}. Identity is in H.
If pi is in H, substituting index pi^{-1}(i) and profile P_pi^{-1}s yields
u_i(s)=u_pi^{-1}(i)(P_pi^{-1}s), so pi^{-1} is in H. If pi,tau are in H,
two substitutions give u_i(s)=u_tau(pi(i))(P_tau P_pi s), so tau*pi is in H.
The source proofs use precisely these identities and have no substantive
defect. All remain valid for singleton action sets; the profile action need
not be faithful. Finiteness of the action set is unused.

### Theorem 3.18

Source label-dependent:254–271. Full symmetry implies both a transitive
invariant subgroup and weak anonymity: the subgroup can be S_N, and for pi
fixing i, full symmetry reduces to u_i=u_i composed with P_pi.
Conversely let H be a transitive invariant subgroup and fix pi,i. Choose
tau in H with tau(i)=pi(i), and put h=tau^{-1}pi. Then h fixes i and
P_tau P_h=P_pi. Weak anonymity and invariance under tau give

    u_i=u_i composed with P_h
       =(u_tau(i) composed with P_tau) composed with P_h
       =u_pi(i) composed with P_pi.

This proves (ii)->(i). Composing u_i=u_pi(i) composed with P_pi on the
right with P_pi^{-1} gives (iii), and reversing this composition proves its
converse. Full symmetry implies the transposition condition (iv); closure of
invariants (3.8) and generation S_N=<transpositions> gives its converse.
Each transposition is its own inverse, giving (iv)<->(v). The v5 proof has
the correct stabilizer factor and correct composition order. No proof defect
was found in this version. The finite-player hypothesis supports the stated
transposition-generation step; strategy-set finiteness is not used.

### Lemmas 3.19, 3.20 and Theorem 3.21

Source label-dependent:187–190, 281–304. Full anonymity is exactly
u_i=u_j composed with P_pi for every i,j,pi. Set pi=e to obtain u_i=u_j;
set j=pi(i) to obtain full symmetry. Conversely full symmetry followed by
pointwise equality of the player functions gives full anonymity. This proves
3.19. The source cites Brandt rather than printing a separate proof; the
source-attribution claim itself is not audited by this algebraic verification.

For 3.20 write D_pi as u_i=u_pi(i) composed with P_pi^{-1}. D_pi and D_tau
give

    u_i=u_pi(i) composed with P_pi^{-1}
       =u_tau(pi(i)) composed with P_tau^{-1} P_pi^{-1}
       =u_tau(pi(i)) composed with P_(pi*tau)^{-1}.

The order pi*tau in the last profile operator, opposite tau*pi in the player
index, is correct. The original proof is valid.

For 3.21, D on transpositions implies C (ordinary full symmetry) on those
generators, hence on S_N by 3.8. Compare D_pi with C_pi^{-1}: surjectivity
of P_pi^{-1} gives u_pi(i)(t)=u_pi^{-1}(i)(t) for every t. Given a!=b,
choose k distinct from a,b and pi=(k a b). Using i=k gives u_a=u_b.
Conversely C_pi^{-1} plus equality of all payoff functions gives D_pi.
The n>=3 assumption is used exactly for k; n=2 merely has D=C. The
original proof is also valid: successive D for (jk),(ijk),(ik) give player
product (ik)(ijk)(jk)=(ijk), while the inverse profile product
((jk)(ijk)(ik))^{-1}=e, yielding u_i=u_j. No defect in the original
permutation identities was found. The n>=3 equality conclusion is not
asserted for n=2. All action sets may be singleton; no action-set finiteness
is used.

### Lemma 4.5 and Corollary 4.6

Source section-bijections.tex:62–81. For g=(pi;(t_i)) from Gamma to Lambda
and h=(eta;(f_j)) from Lambda to Xi, the composite has components
(eta*pi;(f_pi(i) t_i)_i). At target coordinate k,

    ((h g)(s))_k
      =f_eta^{-1}(k)(t_pi^{-1}(eta^{-1}(k))(s_pi^{-1}(eta^{-1}(k))))
      =(h(g(s)))_k.

All domains match: t_pi^{-1}(eta^{-1}(k)) lands in the strategy set for
eta^{-1}(k), the domain of f_eta^{-1}(k). This proves 4.5. Composing any
target payoff function with these equal profile maps proves 4.6. The source
uses u for the last game's payoff function in this corollary; writing w
instead makes the target type explicit. This is a notation issue, not a
false composition identity.

### Theorems 4.7 and 4.9

Source bijections:84–100, 115–121. Objects and endpoints must be retained.
The identity on Gamma is (id_N;(id_Ai)_i). The inverse of g above is
(pi^{-1};(t_pi^{-1}(j)^{-1})_j). The two composites give the respective
identities, both on players and component strategy sets. For a third arrow
k=(xi;(l_r)), either bracketing gives player map xi*eta*pi and component
l_eta(pi(i)) f_pi(i) t_i. Associativity follows from ordinary function
composition. This proves 4.7 as a typed groupoid, without treating an
individual hom-set between distinct objects as a group. The source's
abbreviated game triples in its setup do not affect these computations.

For 4.9 an exact isomorphism satisfies u_i=v_pi(i) composed with g.
Identity is payoff preserving. Setting i=pi^{-1}(j) and composing with g^{-1}
gives v_j=u_pi^{-1}(j) composed with g^{-1}, so inverse arrows preserve
payoffs. If also v_j=w_eta(j) composed with h, then

    u_i=v_pi(i) composed with g
       =w_eta(pi(i)) composed with h g.

Thus compositions are payoff preserving. Associativity and identities are
inherited from 4.7. The original proof is valid; no new statement or proof
defect was found. Singleton strategies cause no exception because player and
component maps remain part of each arrow's typed data.

## Supplemental unnumbered action counterexample

The abstract-quotient/transitivity assertion after Example 5.5 is false; see
research/action-and-torsor-audit.md for the complete counterexample, corrected
representation-sensitive statement and degree-minimality argument. The first
claim in that paragraph, about an abstract quotient isomorphic to S_N itself,
is valid by finite order and should be retained separately.
