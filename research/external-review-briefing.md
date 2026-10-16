# Game Symmetry: briefing for an independent mathematical reviewer

Nicholas Ham — research draft, 16 October 2026. Candidate extensions below
have internal proofs and reproducible finite certificates; novelty and human
mathematical approval remain unresolved. This briefing requests criticism,
not endorsement. No external contact or submission has been made.

## Question and exact conventions

Ham's 2021 Example 5.13 and Figure 4 already classify the relevant
three-player binary parameterized mechanisms. They show that standard
symmetry and realization of every player permutation need not give full
symmetry under one matching. The present question separates two failures:
can compatible lifts exist without a matching, and can even compatible
lifts fail to exist?

A game is finite, with nonempty strategy sets A_i and real pure-profile
utilities u_i. A typed map g=(p;(f_i)) has bijections f_i:A_i→A_p(i),
acts by (gs)_p(i)=f_i(s_i), and preserves payoffs exactly when
u_p(i)(gs)=u_i(s) for every i,s. Products act right to left. For pure
player permutations, (P_p s)_j=s_p⁻¹(j). Let G be the **complete** exact
automorphism group and q:G→S_n its player projection.

| Property | Precise requirement |
|---|---|
| Full player image | q(G)=S_n; unrelated choices of lift are allowed. |
| Splitting / coherent lifting | A homomorphism σ:S_n→G with qσ=id. |
| Standard symmetry | A player-transitive subgroup whose elements fixing player i act identically on A_i. |
| Full matching symmetry | A section with this last fixed-player property. Equivalently, coherent bijections c_ij with c_jk c_ij=c_ik whose lifts all preserve payoffs. |

A section need not be strategy-trivial. Thus splitting does not imply full
matching symmetry. Standard symmetry alone concerns a transitive subgroup,
not all player permutations. No assertion concerns mixed-strategy ordinal
invariance or interpersonal fairness.

## Statements to scrutinize

**T3 (candidate extension).** With three players and exactly three strategies
each, standard symmetry plus full player image implies splitting. If full
matching symmetry fails, the complete group, up to local labels, has order
6 or 18. Writing ε for permutation parity and h for a strategy transposition,
these groups are

- H_h={(p;(h^ε(p),h^ε(p),h^ε(p))):p∈S_3};
- L={(p;(f,f,f)):ε(p)=ε(f)}.

Both occur as complete groups. The common-interest orientation payoff
(sign of the permutation on three distinct labels, zero on repeated labels)
realizes L. The proof depends on an explicit 32-representative finite lemma,
not an unreported symbolic classification; its full witnesses are separate.

**Tn (candidate extension).** For a game with exactly three strategies per
player and complete exact group G with q(G)=S_n, the projection splits if
n≥5 and n≠6, without standardness. With standardness imposed at all player
counts, nonsplitting is possible **only at n=6**, and is attained below.
This classifies possible player counts, not all six-player actions or games.
The conclusion uses classical alternating-group multiplier theory.

The exact hypotheses matter: no corresponding claim is made for an
arbitrarily selected preserving typed subgroup. For even n≥4 the signed
subgroup sum_i b_i=ε(p), acting locally by x_i↦(−1)^b_i x_i,
is standard and full-image but nonsplit. An n-cycle lift has order 2n.
Its invariant payoff tables acquire extra automorphisms, so it cannot be
the complete group required by Tn.

## Explicit attained game

Take six players, A_i=F_3, and common utility u_i(s)=1_C(s). Form C by
adding each common constant 0,1,2 to the six rows

```
000100
002221
011122
012010
020212
021001
```

Thus C has 18 words and the game is specified on all 729 profiles.
"Binary" here describes the two payoff values, not the strategy count.
Its complete group has order 2160, player image S_6, and pointwise-player
kernel consisting exactly of the three common translations.

Two preserving maps supply the full image. With zero-based indices and local
permutations written as image strings, their data are

```
a: p=(0,3,2,1,4,5), f=(021,021,102,021,021,102)
b: p=(1,4,0,3,5,2), f=(012,012,012,012,012,012)
```

The image transposition and five-cycle generate S_6. Distance-six triples
of codewords are precisely common-translation triples. Consequently a
pointwise-player automorphism has common local slope ±1; modulo common
translation only twelve candidates remain. Direct rejection leaves the
identity. This proves the full kernel, so image and kernel determine the
**complete** group without trusting its abstract name.

Two translation-only maps generate a strategy-trivial transitive subgroup
of order 60 (their data are in manuscript §6). Point stabilizers have order
10 and map trivially into local C_3, proving standardness. The inverse image
of A_6 has order 1080 and is perfect, verified by explicit commutator normal
closure. If a section existed it would yield an index-three subgroup there;
the corresponding nontrivial transitive image in S_3 contradicts perfectness.
The underlying degree-18 triple-cover action is established group theory,
not a new group construction.

## Short proof route for Tn and precise review questions

Identify every ternary local permutation with x↦ax+b. Write
R=F_3^n, B for the sign/player image, K=B∩F_2^n and N=G∩R.
This avoids manipulating arbitrary ternary permutations throughout.

1. **Actualness step.** K is 0, the constant line T_2, the even-sign module
   E_2, or F_2^n. If K contains E_2, character projections force N=0 or R.
   In the N=0 case normal-subgroup averaging removes translations. Parity
   cancellation at zero coordinates, plus an odd lift fixing the focal
   player on nonzero profiles, then forces additional payoff invariance and
   a matching. Does this use exactly complete payoff invariance, with no
   tacit invariance under a map moving the recipient?
2. **Central sign case.** For K=T_2, average over the normal order-two
   subgroup only, acting by −1 on R/N. This gives N⋊B. Supported Coxeter
   defects vanish for n≥5; standardness excludes the exceptional n=4
   distant defect. Are the support bounds and the use of standardness valid
   independently of the chosen lifts?
3. **Residual module step.** For K=0, stabilizer characters normalize signs
   to ordinary or parity-twisted permutation action. Transposition
   differences give N∈{0,T_3,E_3,R}. An invariant complement splits the
   projection if 3∤n. At n≥5, quotient cocycles and supported Coxeter
   relations eliminate every case except N=T_3 with parity twist. Can
   this be shortened using standard cohomology results with identical
   represented-action hypotheses? We do not claim all cocycles vanish.
4. **Central-extension step.** The remaining group has order 3n!, with
   even permutations centralizing and odd permutations inverting C_3.
   For n≥8, |M(A_n)|=2 gives a perfect complement D in q⁻¹(A_n).
   Since D is its derived subgroup it is normal in G. A transposition
   lift has square fixed and inverted simultaneously, hence is involutory;
   adjoining it to D supplies the section. Does the universal-central-
   extension argument apply without an unmentioned perfectness assumption
   on q⁻¹(A_n)? (The argument needs only perfectness of A_n.)
5. **Finite interfaces.** Please reproduce T3's 32/11-case lemma and the
   six-player perfectness and standard-subgroup certificates separately.
   Can either finite ingredient be replaced by a short conceptual argument?
   No finite experiment proves the unbounded reduction.

Items 1–3, rather than the familiar multiplier conclusion alone, are the
highest-value independent audit. Boundary cases n=1,2,3,4 are separately
accounted for; divisibility excludes n=5,7. Complete proofs are in manuscript
§§4–6 and the Phase 7 audit. This briefing is not a replacement proof.

## Attribution, novelty, and a separate equilibrium programme

Ham's Example 5.13 / binary Figure 4 are prior work. Orbit-preserving closure
and distinct-orbit payoff realization are prior covering-group principles
(Cao–Li–Tan–Yang 2024, with their Peleg–Rosenmüller–Sudhölter attribution).
The code-to-common-interest indicator encoding is immediate. ATLAS and
Gillespie–Ó Catháin–Praeger supply the related triple-cover/Hadamard action.
Lassueur–Mazza §3 recalls the classical multiplier input. Candidate novelty
lies in the exact small-strategy game hypotheses, represented lifting
classification and sharp player-count boundary. These need specialist
comparison with block systems and code/design automorphism groups, not only
searches using game-theory terminology. No priority is claimed.

A distinct active candidate says that a binary-strategy game with n≥3 and
full **actual** exact player image has an exact potential, without requiring
standardness. Its proof separates matching rigidity for n≥5, own-action
indifference in the exceptional n=4 branch, and the signed n=3 case. Ordinary
fully symmetric binary potential is prior (Hofbauer–Sorger, eq. 4.15).
Two-player matching pennies excludes dropping n≥3. Final Cao–Yang2018 and
Cheng–Liu2018 bodies remain comparison gaps. Preserve this programme here;
a short separate note is sensible only after the current lifting review and
these comparisons, not as an already cleared publication claim.

## Review packet and proposed sequence

Start with this briefing and the manuscript. Ask a finite-group specialist
to assess items 1–4 before certificates; ask a second reader with games and
code/design expertise to assess actualness and priority. Then request an
independent certificate reproduction from the tracked guide, without ignored
downloads. Keep responses as criticism of explicit claims, with changed
hypotheses and examples recorded. Author approval must precede any contact.
This is a proposed workflow; no reviewer has been contacted.

- [Manuscript source](../paper/main.tex), built locally by `scripts/build.sh`.
- [Full reduction audit](phase7-final-structural-audit.md).
- [Finite verification guide](../verification/README.md).
- [Novelty comparison](phase8-review-readiness.md).
- [Binary proof](phase4-binary-verification.md) and [source comparison](phase4-novelty-comparison.md).

The paper is ready for serious independent criticism; it is not yet cleared
for submission. Computational reproduction, specialist priority assessment,
author approval and venue-specific disclosure checks remain outstanding.

Selected primary references (versions/access limits are in the novelty record):

- Ham, [arXiv:1311.4766v5](https://arxiv.org/abs/1311.4766v5), revised 5 May 2021.
- Cao–Li–Tan–Yang, [On group structures of strategic-form games](https://doi.org/10.1016/j.fmre.2022.06.015), online 2022, issue 2024.
- Gillespie–Ó Catháin–Praeger, [Construction of the Outer Automorphism of S6 via a Complex Hadamard Matrix](https://doi.org/10.1007/s11786-018-0382-0), 2018.
- [ATLAS A6 representations](https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/), degree-18 representation 3S6G1-p18aB0.
- Lassueur–Mazza, [author manuscript, 18 May 2015](https://eprints.lancs.ac.uk/id/eprint/82264/1/endoSchurAnSn_Revised.pdf), §3.
- Hofbauer–Sorger, [A Differential Game Approach to Evolutionary Equilibrium Selection](https://homepage.univie.ac.at/josef.hofbauer/02igtr_sorger.pdf), 2002, §4.2.2.

Phase9 handover: [targeted specialist checklist, binary proof reconstruction
and newly inspected primary passages](phase9-handover.md). No hypothesis or
manuscript theorem changed. In particular, Cheng–Liu's inspected 2017
negation-symmetry theorem is distinguished from its uninspected final2018
version and from a signed player-action lift.
