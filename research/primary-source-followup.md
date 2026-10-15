# Primary-source retrieval follow-up — 16 October 2026

**Status: open source-access questions.** This bounded follow-up retrieved author-site metadata and independently re-downloaded Plan's old draft, but did not obtain readable Dasgupta–Maskin original pages or Plan's final/accepted article. No original theorem proof has been inferred from secondary quotations. No authentication, paywall circumvention, external correspondence, or public redistribution was attempted. Cached responses remain in ignored `.local/references/`. Main source-register metadata was not edited.

Requests occurred around 2026-10-15 17:37 UTC (16 October in Melbourne). HTTP status and SHA-256 below refer to actual local response bytes, not the browser cache's version.

## Dasgupta–Maskin (1986), Part I: Theory

Primary publication metadata: Partha Dasgupta and Eric Maskin, *The Existence of Equilibrium in Discontinuous Economic Games, I: Theory*, Review of Economic Studies 53(1), January 1986, pp.1–26, DOI [10.2307/2297588](https://doi.org/10.2307/2297588). [Oxford's article page](https://academic.oup.com/restud/article-abstract/53/1/1/1579920) confirms these bibliographic facts and explicitly indicates that access is unavailable. Metadata access does not establish the contents of Definition 7 or any proof.

The [current Harvard author publication page](https://maskin.scholars.harvard.edu/publications/existence-equilibrium-discontinuous-economic-games-part-i-theory) was readable through the web tool. Its actual PDF link is:

<https://maskin.scholars.harvard.edu/sites/g/files/omnuum10606/files/maskin/files/the_existence_of_equilibrium_in_discontinuousgames_i.pdf>

The web tool identified that attachment as a 27-page PDF with zero extracted text lines. Requesting page index 17 as a screenshot produced only an inaccessible image-reference string in this tool environment; no readable page image was delivered. It would be incorrect to record this as inspection of the scan.

A direct normal public HTTP GET of that exact attachment returned **403**, 540 bytes, `text/html`, cached as `dm-harvard-current.html`, SHA-256 `172bedcacf77c86a851ad120812fac9a2918ac27ad8e61b031919fb3642cc2fc`. The current host therefore remains unavailable to the local PDF/OCR workflow. Earlier old-host failures were supplied by the coordinator and were not repeated here.

The [ResearchGate publication page](https://www.researchgate.net/publication/4995362_The_Existence_of_Equilibrium_in_Discontinuous_Economic_Games_I_Theory) is indexed as an author-uploaded full text, uploaded by Eric Maskin on 2 May 2023. Its indexed abstract is unrelated to this paper, so that abstract is not used as evidence. The coordinator supplied the following likely resolved public author-upload link:

<https://www.researchgate.net/profile/Eric-Maskin/publication/4995362_The_Existence_of_Equilibrium_in_Discontinuous_Economic_Games_I_Theory/links/64517a8a97449a0e1a707129/The-Existence-of-Equilibrium-in-Discontinuous-Economic-Games-I-Theory.pdf>

A direct normal GET returned **403**, 20,178 bytes, `text/html; charset=UTF-8`, cached as `dm-researchgate.html`, SHA-256 `98163baf42537ea407dae8ee1f298b2f493370696ce45360af788c140576ce01`. The link's validity as a PDF download is not established because the response is an access-denied page, not a PDF. No alternate headers, cookies, logged-in sessions, proxies, or URL access-control workarounds were attempted.

Bounded web searches using the title, exact Harvard filename, and Definition 7 found the same Harvard/ResearchGate/publication records plus secondary papers, not another verifiable public original scan. Those secondary references were deliberately not used to fill the original-source gap.

**Still unknown from direct original inspection:** Definition 7's exact displayed permutation convention and quantifiers; Lemmas 6 and 7 and their proof steps; Theorems 6 and 6* and their precise dependence on that definition; whether any displayed inverse convention changes in the appendix. No conclusion about the validity or invalidity of these original existence proofs follows from the access failures. These items remain pending a readable original source.

## Plan: actual author links and version check

The live [research page](https://www.asafplan.com/research/) returned **200**, but its HTML response stops at the opening article element and does not display the research text: 5,912 bytes, cached as `plan-research.html`, SHA-256 `41a6450f0b8bc988870ca06fc9acdddda601376f6dc82fbd461ee1ee89006f2d`.

The page itself advertises the public WordPress REST API. Reading its unauthenticated, unprotected page record at [pages/15](https://www.asafplan.com/wp-json/wp/v2/pages/15) recovered the actual public research content: **200**, 9,682 bytes, cached as `plan-research-rest.json`, SHA-256 `af2cd8837e92f3e98c6dedebf5514e6a19610f199db098e1c8bde43a78369b1f`. This is an ordinary public content endpoint; no private revisions or credentials were requested. Its modification timestamp is `2018-03-02T05:26:38`; its symmetry-paper entry still says revise and resubmit and links to `http://www.asafplan.com/files/SymmetricGames.pdf`. There is no final/accepted symmetry-paper link in that retrieved research content.

The corresponding public [home-page record, pages/12](https://www.asafplan.com/wp-json/wp/v2/pages/12) returned **200**, 2,649 bytes, cached as `plan-home-rest.json`, SHA-256 `1c8c4e6e13feae66d533039fbe57811fe0acc990b0128e20446747320e28f505`. Its modification timestamp is `2017-03-14T05:32:11`; it supplies no newer symmetry-paper link. An old author page's current accessibility must not be mistaken for current publication content.

The actual author link, upgraded to HTTPS, [SymmetricGames.pdf](https://www.asafplan.com/files/SymmetricGames.pdf), returned **200**, 766,597 bytes. It was cached as `plan-author-current.pdf`; `pdftotext` extracted a first page explicitly dated **March 13, 2017**, titled *Symmetric n-player games*. SHA-256 is `f8631d14b42215cf10dc30751cd4d25566a0aa561ec98aba809028f9d5ac8eab`, **identical** to the existing `plan-2017.pdf`. This is direct byte-level confirmation that the actual author-site research link currently supplies the same old draft. The text extraction is cached as `plan-author-current.txt`.

The [publisher record](https://www.sciencedirect.com/science/article/pii/S0022053122001399) identifies the final paper as *Symmetry in n-player games*, Journal of Economic Theory **207**, January **2023**, article **105549**, DOI [10.1016/j.jet.2022.105549](https://doi.org/10.1016/j.jet.2022.105549), and notes the previous title. This establishes the final bibliographic identity, not the final body text.

A normal GET of the publisher's public PDF endpoint
`https://www.sciencedirect.com/science/article/pii/S0022053122001399/pdfft?isDTMRedir=true&download=true`
returned **403**, 832,805 bytes, HTML, cached as `plan-publisher.html`, SHA-256 `ee0768e441a41e22bcec5ff6b3cd0f71a886721650cf4b8e9abf2932c5ed5f0b`. Searches by the final title, author and “accepted” found no verified alternate accepted manuscript during this bounded pass.

**Proposed source-register metadata, not applied:** retain separate version entries for Plan's directly inspected 2017-03-13 author draft and 2023 final bibliographic record; mark final body and final/draft comparison uninspected. Record the current author research link as confirmed to serve exactly the 2017 cached bytes. Retain DM86 as bibliographically confirmed but original Definition 7 / Lemmas 6–7 / Theorems 6–6* direct inspection pending. None of these access results supports upgrading any proof-audit status.
