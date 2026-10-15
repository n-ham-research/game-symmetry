# Theorem audit — Ham v5

**Status meaning:** Verified means a mathematical derivation has been checked within this project, not externally peer-reviewed or approved by the author. Source attribution and historical checks may remain pending. No status is justified by agent agreement alone.

All 41 numbered results are listed. Exact source statements, ambient assumptions and explicit dependencies are in original-result-inventory.md and inventory.json. See audit-evidence.md for evidence behind non-pending statuses.

| Result | Status | Independent proof | Counterexample search | Action |
|---|---|---|---|---|
| Proposition 2.2 | Incorrect | Partial: marginals prove injectivity; surjectivity characterization in audit-evidence.md | Singleton/one varying player refutes non-surjectivity | Replace statement and proof |
| Proposition 2.3 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 2.4 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 2.5 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 3.1 | Verified | Coordinate composition P_tau P_pi=P_tau pi | Composition checked algebraically | Retain with explicit action |
| Lemma 3.2 | Verified | Inverse action reverses multiplication | Algebraic identity | Retain with convention |
| Corollary 3.3 | Verified | Substitute left-action composition and player indices | Type/action check | Retain |
| Proposition 3.4 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 3.5 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 3.6 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 3.8 | Verified | Identity, inverse and composition proof in manuscript §3 | Finite constraint/action checks support proof | Retain |
| Theorem 3.18 | Verified | Stabilizer factorization and generator proof; audit-evidence.md | v1 proof error distinguished from repaired v5 proof | Retain v5 result with new exposition |
| Lemma 3.19 | Verified | Identity permutation gives equal functions; combine with full symmetry; converse direct | Own-action and common asymmetric examples distinguish parts | Retain; inspect original Brandt attribution later |
| Lemma 3.20 | Verified | Two substitutions; inverse product order explicitly checked | Three-cycle permutation identities checked | May omit from shortened manuscript proof |
| Theorem 3.21 | Verified | Complete short and original proofs checked; reviews A–C | Exact constraint partitions and explicit boundary examples | Retain as literature; no novelty claim |
| Proposition 3.23 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 3.25 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.5 | Verified | Coordinate computation using typed components | Index/domain check | Retain |
| Corollary 4.6 | Verified | Payoff composition from Lemma 4.5 | Index/domain check | Retain |
| Theorem 4.7 | Verified | Component identities, inversion and associativity; audit-evidence.md | Domain/codomain checks | Retain |
| Theorem 4.9 | Verified | Payoff equalities closed under composition and inversion; §5 manuscript | Domain/codomain checks | Retain |
| Corollary 4.10 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.11 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 4.12 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.14 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 4.15 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 4.16 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.19 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.20 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 4.21 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.22 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Theorem 4.23 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 4.24 | Incorrect | Printed (i),(iii) true and (ii) false for distinct player constants | Two binary-action players with u1=0,u2=1 | Repair G<=Gamma to appropriate bijection subgroup and prove |
| Lemma 4.26 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Lemma 4.27 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Theorem 4.28 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 5.1 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 5.2 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Corollary 5.3 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Proposition 5.6 | Unverified | Pending; source statement inventoried | Pending | Review assumptions and dependencies |
| Theorem 5.11 | Requires clarification | Replacement mixed-strategy argument in audit-evidence.md | Matching pennies exposes omitted strategy maps and pure/mixed mismatch | Replace proof; inspect historical attribution |

## Assumptions still to audit

Finite nonempty strategy sets are inherited unless a statement says otherwise. In Section 3 common labels are essential. In Sections 4–5 distinguish the full bijection group, exact automorphism group, player image and player-fixing kernel. Zero-sum/minimax claims use independent mixed profiles unless a coalition distribution is explicitly introduced. The inventory records explicit references, not a completed hidden-dependency analysis.

## Unnumbered claims

U2-M is Incorrect with exp as counterexample. Additional candidates in audit-evidence.md (real utility representation on arbitrary domains, wreath-product order, representation-sensitive transitivity, hom-set structure) remain Requires clarification. Classification claims in prose and diagrams are indexed in unnumbered-claims.md; none is silently treated as verified.
