import sys
import re
import subprocess

def verify(path):
    print(f"Verifying {path}...")
    with open(path, 'r') as f:
        content = f.read()
    
    # NORMALIZE LINE ENDINGS
    content = content.replace('\r\n', '\n')
    
    parts = content.split('\n---\n')
    if len(parts) < 2:
        print(f"Skipping {path}: Invalid format")
        return False
    
    front = parts[0]
    code = parts[1]
    
    match = re.search(r'(-----BEGIN PGP SIGNATURE-----[\s\S]*?-----END PGP SIGNATURE-----)', front)
    if not match:
        print(f"No signature block found in {path}")
        return False
    
    raw_sig = match.group(1)
    clean_sig = '\n'.join([line.strip() for line in raw_sig.splitlines()])
    
    with open('temp.sig', 'w') as f: f.write(clean_sig)
    
    proc = subprocess.run(['gpg', '--verify', 'temp.sig', '-'], input=code.encode('utf-8'), capture_output=True)
    
    if proc.returncode != 0:
        print(f"Failed {path}: {proc.stderr.decode()}")
        return False
    
    print(f"Verified {path} successfully.")
    return True

if __name__ == '__main__':
    import glob
    import os
    files = glob.glob('sources/**/*.js', recursive=True)
    failed = False
    for f in files:
        if not verify(f): failed = True
    
    if os.path.exists('temp.sig'): os.remove('temp.sig')
    if failed: sys.exit(1)
