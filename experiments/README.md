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
