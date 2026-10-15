# Foundation corrections and replacement arguments

16 October 2026. Research notes, not manuscript promotion. Existing results are
literature / previously established by Ham, arXiv:1311.4766v5. Weaker-scope
versions here are candidate extensions; no novelty or priority is claimed.
Internal review evidence: reviews/R-FOUND-003-C.md. The review reuses an agent
instance with previous exposure to several findings; it is not fully blinded
or external peer review. The coordinator must reconcile additional reviews.

Use (P_pi s)_j=s_pi^{-1}(j), right-to-left composition. The original paper
explicitly assumes finite games (section-background.tex:48), including
nonempty singleton strategy sets. Expected payoffs below use independent
mixed profiles. A one-player extension uses a singleton empty opponent product.

## C-F01: exact product-distribution criterion (repair of Proposition 2.2)

For finite nonempty N and finite nonempty A_i, the map

    F: product_i Delta(A_i) -> Delta(product_i A_i),
    F(p)(s)=product_i p_i(s_i)

is well defined and injective. It is onto if and only if at most one A_i
contains more than one action. In particular it is onto for one player and
for games with only singleton action sets.

Proof: total mass factors as product_i sum_a p_i(a)=1. Taking the i-th
marginal recovers p_i. With only one varying coordinate, every joint law is
that coordinate's marginal times point masses elsewhere. If two coordinates
vary, choose a_i!=b_i and a_j!=b_j, fix all other coordinates, and give mass
1/2 to each of the two diagonal profiles. Independence would force mass 1/4
on both absent cross profiles. Thus it is not a product law.

The original third assertion is false at the singleton boundary. Its proof
should be replaced rather than patched by a parameter count or division by
potentially zero probabilities. The corrected statement does not assert that
opponents mix jointly when their domain was originally a product of simplexes.

## C-F02: minimax identities and existence

For any finite game set X=Delta(A_i), Y=product_{j!=i}Delta(A_j). Continuity
and compactness give extrema. Select x* attaining max_x min_y U_i(x,y) and
y* attaining min_y max_x U_i(x,y). Then

    lower_i <= U_i(x*,y*) <= upper_i.

This proves Proposition 2.3, including singleton actions, without assuming
convexity of Y. For one player both sides are max_x U_i(x).

In a two-player zero-sum game U_2=-U_1, so

    lower_1 = max_x min_y U_1(x,y)
            = -min_x max_y U_2(x,y) = -upper_2,
    upper_1 = min_y max_x U_1(x,y)
            = -max_y min_x U_2(x,y) = -lower_2.

Proposition 2.4 is correct, but its printed proof (ii), background:269–270,
reverses x and y. For U_1=[[0,1],[2,3]], true upper_1=2, while its printed
min_x max_y expression equals 1. This is a concrete proof counterexample,
not a statement counterexample. Proposition 2.5 is the established finite
zero-sum minimax theorem: lower_i=upper_i. One proof uses strong LP duality
between maximizing v under M^T x>=v1, x>=0, 1^T x=1 and minimizing w under
My<=w1, y>=0, 1^T y=1. Feasibility and boundedness follow from a finite payoff
matrix. No repair to its statement is required.

## C-F03: typed partial-profile transport (Propositions 3.4–3.6)

In the common-label setting let D_i=Delta(A_i), E_i=product_{k!=i}D_k.
Regard these as objects tagged by their player index even when the underlying
sets coincide. Define

    L_pi,i:D_i -> D_pi(i),     L_pi,i(x)=x,
    R_pi,i:E_i -> E_pi(i),     (R_pi,i(y))_j=y_pi^{-1}(j).

Reconstructing the full indexed profile from a focal coordinate and its
complement gives P_pi(x,y)=(L_pi,i x,R_pi,i y). The inverse of R_pi,i is
R_pi^{-1},pi(i), explicitly y |-> (y_pi(k))_{k!=i}. Moreover

    L_tau,pi(i) L_pi,i = L_tau*pi,i,
    R_tau,pi(i) R_pi,i = R_tau*pi,i.

Identities and these inverse/composition formulas prove the two subgroupoid
statements. The original conclusions are valid with typed morphisms. Replace
the badly indexed preimage in source label-dependent:97–100 and the malformed
parentheses in line 108. Do not require distinct permutations to induce
distinct graph maps. For n=1, E_1 is the one-point empty product and the same
identities hold. No action-set finiteness is needed for analogous pure-profile
identities; probability extensions should specify their measure convention.

## C-F04: corrected Corollary 4.24 and weakest scope

Let N be nonempty and finite, with arbitrary nonempty strategy sets A_i and
payoffs u_i:product_i A_i->Y to a common set Y. The following are equivalent:

1. By relabelling strategy sets, the game is exactly isomorphic to a game with
   common labels whose u_i are invariant under all coordinate permutations
   fixing i (weak anonymity).
2. The full group S_Gamma of typed game bijections has a subgroup G with player
   image S_N, strategy triviality, and u_i=u_i composed with g whenever g fixes i.
3. There is a matching M of the strategy sets such that u_i=u_i composed with
   M_pi for every i and pi fixing i.

The condition in (2) is G<=S_Gamma, not G<=Aut(Gamma). No arithmetic on Y,
strategy-set finiteness or n>=2 is used. Equal strategy cardinalities follow
from any of the conditions and need not be assumed separately. The same
argument extends to arbitrary nonempty N with 'player image S_N' retained
instead of finite 'n-transitivity'. Those are candidate scope extensions.

Proof: a matching gives coherent maps t_ij with t_ii=id,
t_jk t_ij=t_ik. Its lifts M_pi=(pi;(t_i,pi(i))_i) satisfy
M_tau M_pi=M_tau*pi, and pi |-> M_pi has player projection pi, hence is
injective. If pi fixes i, its i component is identity, so M_SN is strategy
trivial. Choose a reference r and q_i=t_ir:A_i->A_r. Conjugating the lift
by these relabellings gives P_pi. This proves (1)<->(3) and (3)->(2).

For (2)->(3), any g,h in G carrying i to j have h^{-1}g in G_i.
Strategy triviality implies their i component maps agree; call this unique
map t_ij. Transitivity supplies all these maps, group composition proves
coherence, and M={(t_ri(a))_i:a in A_r} is a matching. Each g with player
permutation pi has components t_i,pi(i). Full player image implies
G={M_pi:pi in S_N}; the given invariance condition becomes exactly (3).

Original statement counterexample: n=2, A_1=A_2={0,1}, u_1=0 and u_2=1.
The game is already weakly anonymous, and every matching satisfies (3).
No automorphism swaps players because that would require 0=1. This example
does not depend on singleton strategy sets. Singleton versions also work.
For one player all three corrected conditions hold automatically; choose the
identity group and the matching A_1.

## C-F05: payoff-preserving transport and security values

For a typed bijection g=(pi;(t_i)_i), push each probability law forward along
t_i. If g is an exact automorphism and pi(i)=j, the mixed extension satisfies

    U_i(x,y) = U_j(L_g,i x,R_g,i y),

where L_g,i is the individual pushforward Delta(A_i)->Delta(A_j), and
R_g,i independently pushes and reorders all opponent coordinates. Both maps
are bijections. Changing variables in each nested maximum/minimum proves

    lower_i=lower_j,     upper_i=upper_j.

Consequently every finite game with player-transitive exact automorphisms has
equal lower values and equal upper values across players. This is a candidate
extension in scope of the reviewed Proposition 3.25 argument, not a novelty
claim; label-dependent standard symmetry is a special case. Zero-sum is not
needed. The source's first sentence, label-dependent:351, must use
u_i=u_pi(i) composed with pi, rather than u_i=u_i composed with pi.

For a finite symmetric two-player zero-sum game, take a swapping automorphism
g=((12);(f:A_1->A_2,h:A_2->A_1)). Then

    U_1(x,y)=U_2(h_*y,f_*x).

The separate bijective changes of variables give lower_1=lower_2 and
upper_1=upper_2. By zero-sum lower_1=-upper_2, and by minimax
lower_1=upper_1. Therefore all four values are zero. This proves Theorem 5.11
in its declared finite scope; Proposition 3.23 follows when f,h are identities.

Theorem 5.11's original statement is valid, but its proof assumes a bare player
swap is an automorphism and computes with pure strategies. Matching pennies
has a swapping automorphism with one strategy flip, whereas the bare swap
fails. Its pure lower/upper values are -1 and 1; its mixed value is zero.
Use the mixed pushforward argument above. Infinite-game counterexamples are
not counterexamples to v5 because its ambient finite-game assumption is explicit.

## C-F06: Proposition 5.6 and representation data

If G<=Aut(Gamma), abstract G is isomorphic to S_N, and the player-action
kernel G_N is trivial, the actual projection rho:G->S_N is injective.
Both groups have order n!, so rho(G)=S_N. Lift an n-cycle c to g. Injectivity
makes g have order n, and <g> acts regularly on players. Its player stabilizers
are trivial, hence it is strategy trivial. This proves the claimed
n-transitively standard symmetry. The abstract isomorphism alone would not
justify identifying two actions; kernel triviality and finite order do that
work here. The statement and intended proof are valid.

Keep full typed bijections, the player projection, its kernel and the profile
action separate. The profile action need not be faithful: if all action sets
are singletons, player permutations act identically on the one-point profile
space but are distinct typed bijections.

## C-F07: unnumbered foundational repairs

The definition of increasing functions in background:38–44 permits exp:R->R,
which is not onto. Replace the subgroup assertion by: the increasing
bijections R->R form a subgroup of all bijections; positive affine maps form
a subgroup of that group. Increasing bijections have increasing inverses.

For an n-player m-strategy game the full typed bijection group is explicitly
(S_m)^n semidirect S_n with coordinate-permutation action. Under the usual
imprimitive convention it is S_m wr S_n; source bijections:129 prints the
reverse order. n=2,m=3 gives 72 versus the reverse wreath product's 48.
Prefer the explicit semidirect product if convention is unspecified.

An arbitrary hom-set Bij(Gamma,Lambda) is not a group under the existing
composition unless it is an endomorphism set. Nonempty hom-sets are torsors
for the endomorphism groups of the appropriate groupoid; keep source/target
tags even when underlying action sets coincide. A whole category of typed
invertible arrows is a groupoid. This clarification does not negate the
verified typed composition results.
