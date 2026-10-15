#!/usr/bin/env python3
"""Fetch source documents into a private ignored cache; never publish PDFs.

No credentials required. Failures are reported per source; a failure is not
silently recorded as a successful retrieval. Network access may require the
host application's approval. Recheck rights before redistributing anything.
"""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CORE = {
    'ham-v5.pdf': 'https://arxiv.org/pdf/1311.4766v5',
    'ham-v1.pdf': 'https://arxiv.org/pdf/1311.4766v1',
    'ham-v5-source.tar': 'https://arxiv.org/src/1311.4766v5',
    'ham-thesis.pdf': 'https://arxiv.org/pdf/1905.00636v1',
    'plan-2017.pdf': 'https://asafplan.com/files/SymmetricGames.pdf',
    'vester-2012.pdf': 'https://lsv.ens-paris-saclay.fr/Publis/RAPPORTS_LSV/PDF/rr-lsv-2012-23.pdf',
}
WIKI = dict(action='query', prop='revisions', titles='Symmetric_game',
            rvprop='ids|timestamp|user|comment|content', rvslots='main',
            rvstart='2011-05-09T00:00:00Z', rvend='2011-05-03T00:00:00Z',
            rvlimit='100', format='json')
CORE['wikipedia-symmetric-game-2011.json'] = 'https://en.wikipedia.org/w/api.php?' + urlencode(WIKI)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--include-library-scan', action='store_true', help='Also download 60MB third-edition scan')
    args = parser.parse_args()
    sources = dict(CORE)
    if args.include_library_scan:
        sources['vnm-full.pdf'] = 'https://archive.org/download/in.ernet.dli.2015.215284/2015.215284.Theory-Of.pdf'
    cache = ROOT / '.local/references'
    cache.mkdir(parents=True, exist_ok=True)
    failed = []
    for name, url in sources.items():
        path = cache / name
        if path.exists():
            print('Already cached:', name)
            continue
        temporary = path.with_suffix(path.suffix + '.partial')
        try:
            request = Request(url, headers={'User-Agent': 'SymmetricGamesResearch/0.1 (source-verification)'})
            with urlopen(request, timeout=120) as response, temporary.open('wb') as stream:
                while block := response.read(1024*1024):
                    stream.write(block)
            temporary.replace(path)
            print('Retrieved:', name, hashlib.sha256(path.read_bytes()).hexdigest())
        except Exception as exc:
            failed.append(name)
            temporary.unlink(missing_ok=True)
            print('FAILED:', name, str(exc))
    if failed:
        raise SystemExit('Unretrieved sources: ' + ', '.join(failed))


if __name__ == '__main__':
    main()
