from pathlib import Path
import re,json,hashlib,argparse
parser=argparse.ArgumentParser(description='Inventory numbered environments from Ham arXiv v5; does not verify claims.')
parser.add_argument('source_dir',type=Path)
parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
a=parser.parse_args(); root=a.root
names=['section-background.tex','section-label-dependent-symmetric-games.tex','section-bijections.tex','section-label-independent-symmetric-games.tex']
items=[]
for sec,name in enumerate(names,2):
 raw=(a.source_dir/name).read_text()
 # Strip LaTeX comments while preserving original line numbering.
 clean=re.sub(r'(?<!\\)%[^\n]*','',raw)
 clean=re.sub(r'\\begin\{comment\}.*?\\end\{comment\}',lambda m:'\n'*m.group().count('\n'),clean,flags=re.S)
 pattern=r'\\begin\{(theorem|lemma|proposition|corollary|definition|example)\}(.*?)\\end\{\1\}'
 for number,m in enumerate(re.finditer(pattern,clean,re.S),1):
  typ,body=m.group(1,2)
  statement='\n'.join(line.expandtabs(4).rstrip() for line in body.split(r'\begin{proof}')[0].strip().splitlines())
  labels=re.findall(r'\\label\{([^}]+)\}',statement)
  # Labels on examples may occur far into diagrams; keep all, resolve the first.
  refs=list(dict.fromkeys(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',body)))
  cites=list(dict.fromkeys(re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',body)))
  items.append(dict(id=f'{sec}.{number}',kind=typ.title(),source=name,line=clean[:m.start()].count('\n')+1,statement=statement,labels=labels,explicit_refs=refs,citations=cites))
labels={label:f"{i['kind']} {i['id']}" for i in items for label in i['labels']}
# Known labels outside numbered environments describe sections and examples, not proof dependencies.
ambient={2:'Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.',3:'Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.',4:'Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.',5:'Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.'}
head=['# Original manuscript inventory','', 'Source: Nicholas Ham, arXiv:1311.4766v5 (5 May 2021). Retrieved 16 October 2026.', '',f'Extracted **{len(items)} numbered environments**: all numbered theorems, propositions, lemmas, corollaries, definitions and examples in source Sections 2--5. Numbering is shared within each section. Statements below reproduce the author-owned source with comments removed and whitespace normalized, not a certified translation. Proofs are not reproduced here; the priority proof is extracted separately in dasgupta-maskin.md.', '', 'The ambient assumptions and explicit source references are recorded for each item. Explicit dependencies include references appearing inside the statement/proof; implicit dependencies and hidden assumptions remain to be audited. A missing explicit reference does not mean a result has no dependencies. Bibliography keys are the original source keys. External-source verification is separate from verification of Ham\'s statement.', '', '## Coverage', '', '| Section | Numbered environments |', '|---|---:|']
for sec in range(2,6): head.append(f'| {sec} | {sum(i["id"].startswith(str(sec)+".") for i in items)} |')
for i in items:
 sec=int(i['id'].split('.')[0]); deps=[labels.get(x,'source label '+x) for x in i['explicit_refs']]
 head+=['',f'## {i["kind"]} {i["id"]}', '',f'Source: `{i["source"]}:{i["line"]}`. Ambient assumptions: {ambient[sec]}','', 'Explicit assumptions/conclusion (source statement):','','```latex',i['statement'],'```','', 'Explicit dependencies: '+('; '.join(deps) if deps else 'none cited inside this environment; ambient definitions still apply.')+' Original citation keys: '+(', '.join(i['citations']) or 'none')+'.','', 'Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.']
(root/'research/original-result-inventory.md').write_text('\n'.join(head)+'\n')
(root/'research/inventory.json').write_text(json.dumps(items,indent=2)+'\n')
print(len(items),'environments',sum(i['kind'] in ['Theorem','Lemma','Proposition','Corollary'] for i in items),'results')
