"""Run the finite mathematical ingredients; not a proof of general theorems."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'verification/bundle-sha256.json'
if manifest.exists():
    for name,digest in json.loads(manifest.read_text()).items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
commands=[['phase5_ternary_audit.py','--verify'],
          ['phase5_splitting_six.py','--verify'],
          ['phase5_six_independent.py'],['phase5_ternary_six_crosscheck.py']]
if '--exhaustive' in sys.argv:
    commands += [['phase5_splitting.py','--verify'],
                 ['phase5_ternary_four_crosscheck.py','--exhaustive']]
for command in commands:
    print('Checking',command[0],flush=True)
    subprocess.run([sys.executable,str(root/'experiments'/command[0]),*command[1:]],check=True)
print('All requested finite ingredients verified. General proofs require mathematical review.')
