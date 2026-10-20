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

The first-priority human-review manuscript is now *Symmetry and Player
Interchangeability in Finite Games*. It leads with a self-contained, explicitly
attributed account of the established Vester/Ham indexing correction, followed
by the ternary classification, splitting boundary and explicit six-player
ternary game with binary common payoffs. Closely related assignment and
invariant-recommendation consequences are included; broader fairness remains
separate. See [publication readiness](publication/READINESS.md) for precise
hypotheses, novelty limits, review records and remaining human decisions.
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
