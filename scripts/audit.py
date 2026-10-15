#!/usr/bin/env python3
"""Validate the pinned source record and report mathematical review impact.

Edges point from prerequisite to dependent. Reachability requests reconsideration;
it never automatically labels a theorem false or silently repairs a statement.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMAL = {'Theorem','Lemma','Proposition','Corollary'}


def read(name, root=ROOT):
    return json.loads((root/'research'/name).read_text())


def affected(graph, changed):
    ids = {x['id'] for x in graph['nodes']}
    if changed not in ids:
        raise ValueError('Unknown audit identifier: '+changed)
    found = {changed}
    while True:
        more = {e['target'] for e in graph['edges'] if e['source'] in found} - found
        if not more:
            return sorted(found)
        found.update(more)


def check(root=ROOT):
    manifest = read('original-record.json',root)
    for item in manifest['files']:
        actual = hashlib.sha256((root/item['path']).read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise ValueError('Pinned original changed: '+item['path'])
    inv = read('inventory.json',root)
    audit = read('audit.json',root)
    graph = read('dependencies.json',root)
    expected = {i['id'] for i in inv if i['kind'] in FORMAL}
    actual = {i['id'] for i in audit['results']}
    if expected != actual or len(audit['results']) != 41:
        raise ValueError('Formal result inventory/audit coverage mismatch')
    ids = {n['id'] for n in graph['nodes']}
    if len(ids) != len(graph['nodes']):
        raise ValueError('Duplicate dependency node')
    for e in graph['edges']:
        if e['source'] not in ids or e['target'] not in ids:
            raise ValueError('Unknown dependency endpoint: '+str(e))
    for item in audit['results']:
        if item['status'] not in audit['statuses']:
            raise ValueError('Unknown result status')
        if not item['justification'] or not item['evidence']:
            raise ValueError('Missing mathematical evidence: '+item['id'])
        for path in item['evidence']:
            if not (root/path).is_file():
                raise ValueError('Missing review evidence: '+path)
        if item['status']=='Verified after correction' and not (root/item['correction_record']).is_file():
            raise ValueError('Missing traceable correction')
    return dict(formal_results=len(actual), original_numbered_items=len(inv),
                counts=dict(Counter(x['status'] for x in audit['results'])),
                pinned_files_checked=len(manifest['files']),
                open_impacts={x['id']:affected(graph,x['id']) for x in audit['results'] if x['status'] in {'Incorrect','Unresolved'}})


def render(root=ROOT):
    audit = read('audit.json',root)
    counts = Counter(x['status'] for x in audit['results'])
    lines=['# Theorem audit — second pass, Ham v5','',
           audit['scope'],'',
           '**Counts:** '+', '.join(f'{s}: {counts[s]}' for s in audit['statuses'])+'.','',
           'These are 41 reviewed formulations, **not 41 unchanged source proofs**. Two printed statements are false (2.2 and 4.24), and five further items need proof or typing repair. Corollary 4.10 remains ambiguous as written; an explicit set-bijection/torsor replacement is proved. No status is based only on agent agreement.','',
           'Original statements/proofs are pinned by [original-record.json](original-record.json); the [correction ledger](corrections.md) gives exact corrected statements, proofs and counterexamples. The [machine-readable registry](audit.json) is the source for this table.','',
           '| Result | Original statement | Source proof/action | Reviewed formulation | Mathematical evidence |',
           '|---|---|---|---|---|']
    for item in audit['results']:
        refs='; '.join(f'[{Path(p).stem}](../{p})' for p in item['evidence'])
        lines.append('| '+f"{item['kind']} {item['id']} | {item['original_statement_status']} | {item['original_proof_status']} | {item['status']} | {item['justification']} {refs} |")
    lines += ['', '## Assumptions and limits','',
              'Original finite nonempty strategy-set assumptions are retained, including singletons; Section 3 requires common labels. The original statement of each item, including extra hypotheses, is in the immutable inventory. For groupoids use explicitly typed source/target objects; for transitivity use the specified player action. Security values use independent mixed profiles; the finite two-player minimax theorem is invoked explicitly. One-player and arbitrary-action-set formulations in the notes are separately scoped extensions, not silent changes to Ham v5.','',
              'All 41 formal results now have a derivation or a precise remaining ambiguity recorded. This does not certify every informal statement, historical assertion, geometric illustration or possible parameter coincidence. See [classification-audit.md](classification-audit.md), [definition-audit.md](definition-audit.md), and [unnumbered-claims.md](unnumbered-claims.md). Human review and external scrutiny remain outstanding.','',
              '## Automatic review impact','',
              'Run `python3 scripts/audit.py check` to check pinned source integrity, coverage and evidence paths. Run `python3 scripts/audit.py impact 4.23` after a newly suspected issue to list dependent results requiring reconsideration. Edges request review, not automatic invalidation. The false 4.24 has no edge to 5.1–5.3: their independent proofs use 4.23. Changes to the product-law component of 2.2 propagate to mixed-strategy arguments; its unused strict-non-surjectivity component has no formal downstream edge.']
    (root/'research/theorem-audit.md').write_text('\n'.join(lines)+'\n')
    lines=['# Dependency graph and review-impact policy','',
           'Canonical data: [dependencies.json](dependencies.json). An edge points from prerequisite to dependent and means that a change requires review. Mathematical dependency, source citation and interpretation dependency are distinguished. Original explicit source references are retained separately from the corrected proof graph. This is not an automatic theorem prover.','',
           '```mermaid','graph TD',
           '  A[4.14: component uniqueness] --> B[4.16: coherent maps]',
           '  B --> C[4.23: matching characterization]',
           '  M[4.20: matching lift homomorphism] --> C',
           '  C --> D[4.24: repaired anonymity]',
           '  C --> E[5.1: standard symmetry]',
           '  C --> F[5.2: full symmetry]',
           '  E --> G[5.3: equal payoffs on a matching]',
           '  P[4.22: fixed matching profiles] --> G',
           '  D --> U[Explicit anonymity analogues: reviewed]',
           '```','',
           'No dependency from 4.24 to 5.1–5.3 is inferred merely because the statements occur later in the source. Their conjugation proofs stand without it. The 4.19 typing ambiguity is repaired by explicit player objects; downstream coherence is checked directly.','',
           '```sh','python3 scripts/audit.py check','python3 scripts/audit.py impact 4.24','python3 scripts/audit.py impact 4.23','python3 scripts/audit.py impact 2.2:strict-nonsurjectivity','```','',
           'When finding an error: preserve the pinned original; update its separate source verdict/corrected status in audit.json; add the counterexample and proof record; run the impact command and reconsider every returned descendant. Add a missing edge if a new dependency is found. Run render to regenerate the audit table. No script silently edits mathematical statuses. Source integrity checks are tamper evidence, not external authentication or write-once storage.']
    (root/'research/dependencies.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['check','impact','render'])
    parser.add_argument('identifier',nargs='?')
    args=parser.parse_args()
    if args.command=='impact':
        print(json.dumps(affected(read('dependencies.json'),args.identifier),indent=2))
    elif args.command=='render':
        render()
    else:
        print(json.dumps(check(),indent=2))
