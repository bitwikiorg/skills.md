import sys
import re
import subprocess
import textwrap

def verify(path):
    print(f"Verifying {path}...")
    with open(path, 'r') as f:
        content = f.read()

    parts = content.split('\n---\n')
    if len(parts) < 2: 
        print(f"Skipping {path}: Invalid format")
        # Actually, let's return False to be safe.
        return False

    front = parts[0]
    code = parts[1]

    # Extract signature block
    match = re.search(r'signature: ([\s\S]*)', front)
    if not match: 
        print(f"No signature in {path}")
        return False

    # Clean signature: remove 'signature: ' prefix if captured, strip, and dedent
    raw_sig = match.group(1)
    # Remove leading newlines/spaces
    sig = textwrap.dedent(raw_sig).strip()

    # Write sig to temp file
    with open('temp.sig', 'w') as f: f.write(sig)

    # Verify
    # echo code | gpg --verify temp.sig -
    proc = subprocess.run(['gpg', '--verify', 'temp.sig', '-'], input=code.encode(), capture_output=True)

    if proc.returncode != 0:
        print(f"Failed {path}: {proc.stderr.decode()}")
        return False

    print(f"Verified {path} successfully.")
    return True

if __name__ == '__main__':
    import glob
    import os
    # Only check .js files in sources/
    files = glob.glob('sources/**/*.js', recursive=True)
    failed = False
    for f in files:
        if not verify(f): failed = True

    if os.path.exists('temp.sig'): os.remove('temp.sig')
    if failed: sys.exit(1)
