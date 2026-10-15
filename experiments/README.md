# Exact finite-game checks

Python standard library only; integer equality and Fraction are used. Players
are zero-indexed in code, and local strategies have integer labels.

Run from the repository root:

```sh
python3 -m unittest discover -s experiments
python3 experiments/constraint_audit.py --output experiments/results.json
```

The partition program compares all equality constraints for C, D, and C+E on
nine specified finite domains. It does not sample payoff tables. The finite-game
module also enumerates player permutations and all local strategy bijections
for small exact automorphism searches, including unequal strategy cardinalities.
Its factorial cost is intentional and limits scale. It does not yet implement
all of Ham's symmetry classes or strategy-trivial subgroup classification.

The tests reproduce the key counterexamples, the two-player boundary, action
composition, matching pennies' relabeling symmetry and Proposition 2.2's
correlation distinction. They support the research record; the general theorem
is proved in research/dasgupta-maskin.md, not by finite enumeration.

## Matching and second-pass audits

`matching_audit.py` enumerates every typed bijection, every subgroup and every
matching on seven specified finite domains. It checks equality-partition
implications for all real payoff assignments on each domain; it separately
enumerates all 256 binary-payoff two-player binary games. See
matching-results.json and reviews/R-MATCH-003-B.md for completeness conditions.

```sh
python3 experiments/matching_audit.py
python3 experiments/classification_audit.py
python3 experiments/ordinal_audit.py
python3 experiments/parameter_audit.py
python3 experiments/parameter_audit.py --verify
python3 scripts/audit.py check
python3 scripts/audit.py impact 4.23
```

The classification audit extracts author-owned source tables from the pinned
inventory, uses pinned diagram excerpts (no source cache or network needed),
and exhausts ambient automorphisms/matching lifts for the displayed examples.
Its binary Hasse audit enumerates all 10 or98 subgroups for two or three players.
The separate parameter audit covers all 4140 equality patterns of 5.14a and
verifies them by independently compiled equality constraints. The ordinal audit
enumerates strict/weak preference tables and cross-checks orbit counts by
Burnside. Equality patterns alone do not establish equilibrium claims; the
example 5.13 equilibrium assertion has a direct inequality proof in the notes.

All outputs are deterministic mathematical data. Finite enumeration is conclusive
for these specified finite classifications; it is not a proof for arbitrary n.
The full typed bijection group's action on profiles may be nonfaithful; never
collapse player permutations merely because singleton profiles coincide.
