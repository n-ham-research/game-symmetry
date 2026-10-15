# Mathematical review protocol

For each major result, freeze its statement, convention and explicit assumptions.
Assign three initially separate roles where practical:

- **A: proof verification.** Check every inference, all types/domains, hidden assumptions and circular dependencies.
- **B: adversarial search.** Receive a statement without endorsement; derive independently, try counterexamples, boundary cases and exact computational searches.
- **C: strengthening.** Receive the statement and source leads; seek weaker assumptions, simpler proofs, stronger conclusions and prior art.

Do not circulate endorsements before reports. Record exactly what context each
reviewer inherited; full chat forks are not fully blinded. Separate derivation,
proof review and source confirmation in the report. Agents sharing a model,
context and tools are not independent external referees. Never add a model,
review or human approval that did not occur.

The coordinating researcher compares reports, resolves disagreements using
explicit mathematics, reproduces consequential computations with tracked code,
and updates the theorem audit with evidence. Retain negative results and fixes.
If the statement changes materially, review the changed claim again. A source
or novelty gap cannot be resolved by agreement among agents.

Before promoting a candidate new theorem into the manuscript require:

1. A complete proof with explicit scope and conventions.
2. Provenance/novelty comparison, including possible known special cases.
3. Adversarial scrutiny and boundary examples appropriate to the claim.
4. Resolution or explicit exclusion of all material objections.
5. A recorded status and citation; author approval remains a separate gate
   before final publication or submission.

Finite enumeration may certify a specified finite constraint system or supply
a counterexample; it is not a proof over arbitrary games. Exact numerical
comparisons must use integers/rationals. Check algorithmic representations
against independently written predicates on nontrivial examples.
