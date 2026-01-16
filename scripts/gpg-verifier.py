import sys
import re
import subprocess

def verify(path):
    print(f"Verifying {path}...")
    with open(path, 'r') as f:
        content = f.read()
    
    parts = content.split('\n---\n')
    if len(parts) < 2: 
        print(f"Skipping {path}: Invalid format")
        return False
    
    front = parts[0]
    code = parts[1]
    
    # Robust extraction: Find the PGP block directly
    # This ignores YAML indentation, pipes, etc.
    match = re.search(r'(-----BEGIN PGP SIGNATURE-----[\s\S]*?-----END PGP SIGNATURE-----)', front)
    if not match: 
        print(f"No signature block found in {path}")
        return False
    
    raw_sig = match.group(1)
    
    # Clean indentation: Remove leading spaces from each line
    clean_sig = '\n'.join([line.strip() for line in raw_sig.splitlines()])
    
    # Write sig to temp file
    with open('temp.sig', 'w') as f: f.write(clean_sig)
    
    # Verify
    proc = subprocess.run(['gpg', '--verify', 'temp.sig', '-'], input=code.encode(), capture_output=True)
    
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
