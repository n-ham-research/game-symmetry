"""Export a self-contained offline verification bundle from canonical files."""
import argparse,hashlib,json,tarfile,tempfile,shutil
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
root=Path(__file__).resolve().parents[1]
paths=['LICENSE','verification/README.md','verification/verify.py']
paths += ['experiments/'+x for x in ['phase5_ternary_audit.py','phase5-ternary-audit-results.json',
 'phase5_splitting_six.py','phase5_splitting-six-results.json','phase5_six_independent.py',
 'phase5_ternary_six_crosscheck.py','phase5_splitting.py','phase5_splitting-c4-results.json',
 'phase5_ternary_four_crosscheck.py']]
paths += ['research/'+x for x in ['phase5-ternary-audit.md','phase5-six-player-obstruction.md',
 'phase5-splitting.md','phase6-sharp-audit.md','phase5-publication-proofs.md','phase5-novelty-comparison.md']]
paths += [str(x.relative_to(root)) for x in (root/'paper').rglob('*') if x.is_file() and 'build' not in x.parts]
with tempfile.TemporaryDirectory() as tmp:
 dest=Path(tmp)/'game-symmetry-verification';dest.mkdir()
 hashes={}
 for name in paths:
  target=dest/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/name,target)
  hashes[name]=hashlib.sha256(target.read_bytes()).hexdigest()
 (dest/'verification/bundle-sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
 with tarfile.open(args.output,'w:gz') as archive:archive.add(dest,arcname=dest.name)
print(args.output)
