# Evidence for initial audit findings

Source identifiers refer to Ham arXiv:1311.4766v5, not the numbering in the new manuscript.

## U2-M: strictly increasing maps (background p.3)

The statement that strictly increasing R->R maps form a subgroup of the bijections of R is false: f(x)=exp(x) is strictly increasing, but its image is (0,infinity). Repair by requiring increasing bijections; positive affine maps with positive slope do form a subgroup. The cited honours-thesis propositions have not been inspected. This is an error in the manuscript assertion as written, independent of their contents.

## Proposition 2.2: product distributions

Well-definedness follows by multiplying the sums of marginal probabilities. Injectivity follows by taking marginals, condensing the source's repeated elimination argument.
The assertion that the product map is never surjective is false under the stated nonempty-finite strategy-set assumptions. If every player but possibly one has a singleton strategy set, every joint distribution is product. In particular all singleton sets give a one-element domain and codomain.
Correct characterization: the product map is not onto iff at least two players have at least two actions. For the nontrivial direction place probability 1/2 on profiles differing in exactly two players' actions, and 0 on the two crossed profiles. The two marginals are each (1/2,1/2), whose product gives positive mass 1/4 to a crossed profile, contradiction. If at most one coordinate varies, its marginal specifies the whole distribution.
The source's lengthy non-surjectivity argument divides by terms not guaranteed positive; this is an additional proof issue besides its missing nondegeneracy hypothesis. The injectivity argument itself proceeds by elimination, not those divisions.

## Theorem 3.18: source-version difference

The v1 Theorem 3.15 implication (ii)=>(i) asserts u_i=u_i composed with pi for arbitrary pi, which weak anonymity does not supply. The v5 proof instead uses tau^{-1}pi, which fixes i. That repaired proof is valid: u_i=u_i P_{tau^{-1}pi}=(u_tau(i)P_tau)P_{tau^{-1}pi}=u_pi(i)P_pi. The other directions follow from inversion, generation by transpositions and self-inversion of transpositions. The v5 acknowledgement credits Plan for identifying a proof error; that acknowledgement is source evidence of what Ham reports, not correspondence independently inspected here.

## Corollary 4.24: subgroup domain

In §4.3 the author defines G<=Gamma to mean G<=Aut(Gamma). Under that definition condition (ii) is too strong. Take n=2 and A_1=A_2={0,1}, with u_1=0 and u_2=1 constantly. The game is weakly anonymous (trivially for n=2); the identity proves (i), and any matching satisfies (iii) because both payoff functions are individually constant. No exact automorphism can swap players, since the equality 0=1 would be required. Thus (ii) fails. The same construction works for n>=3 with pairwise distinct player constants. Condition (ii) should plausibly use the full game-bijection group S_Gamma; this proposed repair needs its own proof and review before use. The counterexample disproves the printed equivalence under the explicitly stated notation.

## Theorem 5.11: statement versus printed proof

The statement for finite two-person zero-sum games and exact player-transitive automorphisms is true. The source proof writes a bare player swap as an automorphism, omitting allowed strategy bijections, and uses pure-strategy min/max expressions even though the zero-sum value is a mixed-strategy value. Matching pennies, already the source's Example 5.5, distinguishes these notions. Thus the proof needs replacement; this is not a counterexample to the theorem.
Repair: transport independent mixed strategies by the component bijections of a player-swapping automorphism. This gives equal maximin values to the two players by change of variables. Finite two-player zero-sum minimax gives opposite values; hence both are zero. The new manuscript defers this theorem until the relevant value conventions and primary historical attribution have been checked.

## Theorems 4.7 and 4.9: typed checks

For g:G->H, h:H->K, the strategy component of hg at i is h_{pi(i)} o g_i. It has domain A_i and codomain C_{rho pi(i)}. The inverse at j is g_{pi^{-1}(j)}^{-1}; its source is B_j. Component identities and function associativity give the groupoid axioms. Exact payoff equalities substitute under composition, and applying g^{-1} proves closure under inversion. These checks justify the treatment in manuscript §5; they do not verify all subsequent matching and classification results.

## Further flagged unnumbered assertions (not yet verdicts)

- The background claim that rational preferences on any set have real utility representations needs domain/cardinality conditions; the finite setting avoids the issue.
- §4.3 writes S_N wr S_M for the bijection group. With the usual imprimitive convention the expected group is S_M wr S_N, of order (m!)^n n!. Determine whether the author uses a reverse convention before classifying this as an error.
- An abstract group being isomorphic to some transitive subgroup is not automatically equivalent to its particular player action being transitive. Audit the unnumbered statement after Example 5.5 with its precise degree and representation specified.
- Corollary 4.10 uses isomorphism notation for hom-sets, which are generally torsors rather than groups without selected base arrows. Clarify intended structure before assigning a verdict.

## Second-pass resolution

This first-pass evidence is retained. Complete replacement statements/proofs are
now in corrections.md, with all41 formal-result statuses in audit.json and
separate source/proof verdicts. See handover-pass-2.md for updated counts and
new action/parameter/ordinal counterexamples. Previously pending matching and
counting derivations have been completed; source-access gaps remain explicit.
