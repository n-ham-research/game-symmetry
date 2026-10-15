# Reference library

The public repository stores bibliographic metadata, source locations, checksums
and research notes. Full downloaded works are in ignored `.local/references/`.
Do not infer permission to redistribute from open access or author hosting.

`paper/references.bib` is the manuscript bibliography. `sources.md` records exact
versions, access status and licensing decisions. `checksums.sha256` identifies
locally inspected files, including original Wikipedia revision responses. These
are retrieval fingerprints, not authenticity certificates or archive services.

Run `python3 scripts/fetch_sources.py` to fetch the core accessible sources into
the ignored cache. An extraction script inventories the author-owned arXiv v5
TeX after unpacking it. All third-party distribution rights remain reserved;
no downloaded PDFs or publisher text are tracked.
