# Game Symmetry

Research by **Nicholas Ham** on structural symmetry, typed automorphisms,
player permutations, splitting and equilibrium in finite games. This repository
was renamed from `symmetric-games`, preserving its GitHub identity and history.
Canonical URL: https://github.com/n-ham-research/game-symmetry

The companion [Game Fairness](https://github.com/n-ham-research/game-fairness)
is the canonical home for utility invariance, assignment, opponent ordering
and fairness research. Both programmes have independent aims and roadmaps.
Historical copies here are frozen; see [dependencies](research/cross-project-dependencies.md)
and the [migration inventory](research/migration-inventory.json).

The main manuscript is now *Symmetry, Automorphism Groups and Player
Permutations in Finite Games*, an internally audited research draft with
provisional novelty. It includes the three-player ternary classification,
general splitting arguments and an explicit six-player binary common-interest
nonsplit game. A classical multiplier corollary establishes six as the only
possible ternary nonsplitting player count under the stated hypotheses.
The pre-split manuscript is preserved in research/archive/pre-split-paper.

## Build and verify

Python3.10+ standard library; pdfLaTeX, BibTeX and latexmk.

```sh
./scripts/build.sh
python3 -m unittest discover -s experiments
python3 scripts/audit.py check
python3 verification/verify.py --exhaustive
python3 scripts/export_verification.py --output /tmp/game-symmetry-verification.tar.gz
```

Read [the Phase6 handover](research/handover-phase-6.md),
[verification guide](verification/README.md),
[readiness assessment](research/publication-readiness.md), and
[Phase5 evidence](research/handover-phase-5.md).
The original41-result audit remains33verified,7corrected/clarified and1original
ambiguity. The binary exact-potential theorem and its source comparison remain
active research here. No manuscript has been submitted or externally reviewed.
Source downloads and local build products are ignored; no third-party PDF or
pre-existing user zip is published.
