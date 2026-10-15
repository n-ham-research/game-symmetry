# Independent verification guide

This package verifies the explicit finite ingredients of Nicholas Ham's
research draft *Symmetry, Automorphism Groups and Player Permutations in
Finite Games*. It requires Python3.10+ with only the standard library, no
network, GAP, Sage, source downloads or model service. A typical laptop uses
seconds and modest memory; times vary. To build the manuscript separately,
install pdfLaTeX, BibTeX and latexmk.

## Exact statements and proof locations

1. Three-player ternary standard/full-image games split; their non-full
   complete groups are precisely H_h and L. See manuscript Section4 and
   research/phase5-ternary-audit.md. The proof's finite lemma has32 normalized
   odd-lift classes,11 group-conjugacy classes and19 embedded groups; it is
   not a numerical sampling of payoff tables.
2. The six-seed code in research/phase5-six-player-obstruction.md defines18
   winning profiles and binary common-interest utilities. Complete group
   order2160, full image720, kernel3, standard subgroup60, perfect even-player
   preimage1080 imply nonsplitting. The analytic kernel proof has12 cases.
3. General splitting and the strengthened only-six player-count theorem are
   mathematical proofs, not finite checks. See manuscript Section5 and
   research/phase6-sharp-audit.md. The imported alternating-group Schur
   multiplier theorem is literature, explicitly cited. Passing these programs
   does not verify that infinite-family theorem or its source attribution.

## Reproduce

From the repository root:

```sh
python3 verification/verify.py
python3 verification/verify.py --exhaustive
```

The default runs the independent32case ternary classifier, the primary
six-player certificate, and both independent six-player implementations.
Expected ternary output:32 lifts,11 classes,19 embedded groups, one exceptional
conjugacy class. Six-player output:2160 complete group elements,720 player
images,3 kernel elements,60 standard-subgroup elements and perfect even
preimage1080. Both binary code and generic-orbit checks are distinguished.
Every unexpected count or certificate discrepancy raises an error.

The optional exhaustive run adds the earlier251case four-player regular-cycle
certificate and independent reconstruction, all21 group sections. That finite
argument is supplementary: the four-player conclusion now also follows from
the conceptual general proof. It is not an all-subgroup census.

```sh
python3 scripts/export_verification.py --output /tmp/game-symmetry-verification.tar.gz
```

Extract that archive, enter its sole top directory, and run the same commands.
The exporter includes the exact input data, independent implementations,
research proofs, this guide, a SHA256 manifest and LICENSE. No external cache
is copied. It preserves one canonical code source; generated bundles are not
independently maintained copies. `python3 verification/verify.py` first checks
bundle hashes when the export manifest exists.

## Limitations

The independent implementations use different tuple/cell representations but
were developed by related AI instances with shared project context. They are
not external peer review. Group names from ATLAS do not substitute for the
explicit actual-game checks. No exhaustive novelty clearance, verified1944
edition comparison or human author sign-off follows from successful execution.
The fairness project's transferred tests are independently runnable there.
