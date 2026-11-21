"""Only run AFTER forecasting. Requires: pip install cryptography"""
import sys
from pathlib import Path
from cryptography.fernet import Fernet
if len(sys.argv)!=4:
 print('Usage: python unlock_2026_after_forecast.py SEALED.zip.enc UNLOCK_KEY.txt OUTPUT_DIR')
 raise SystemExit(1)
archive,keyfile,out=map(Path,sys.argv[1:]);out.mkdir(exist_ok=True,parents=True)
key=keyfile.read_text(encoding='utf-8').split('Fernet key (base64):\n')[1].splitlines()[0].encode()
(out/'Crescent_Gulf_2026_Revealed.zip').write_bytes(Fernet(key).decrypt(archive.read_bytes()))
print('2026 ZIP unlocked in:',out)
