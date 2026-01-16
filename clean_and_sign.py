
import glob
import re
import subprocess
import textwrap
import os

# Ensure we are in the right directory
os.chdir('/root/skills_ops')

files = glob.glob('sources/**/*.js', recursive=True)
print(f"Found {len(files)} files to process.")

for f in files:
    print(f"Cleaning {f}...")
    with open(f, 'r') as file: content = file.read()

    # Extract metadata fields using regex to bypass corruption
    id_m = re.search(r'id: (.*)', content)
    spdx_m = re.search(r'spdx-id: (.*)', content)
    origin_m = re.search(r'origin: (.*)', content)
    hash_m = re.search(r'hash: (.*)', content)
    ver_m = re.search(r'version: (.*)', content)

    # Extract Code: Everything after the LAST '---' or '*/' or 'export'
    # Better: Look for 'export' or 'import' or comments.
    # The corruption is between the first --- block and the code.
    # The code usually starts with 'export' or '/*' or 'import'.
    # Let's find the index of 'export' or '/*' and take everything from there.
    code_start = -1
    match = re.search(r'(export|import|/\*)', content)
    if match:
        code_start = match.start()

    if code_start == -1:
        print(f"Skipping {f}: No code found")
        continue

    code = content[code_start:]

    # Sign Code
    # We need to ensure we use a key that exists. The previous step ensured a key exists.
    proc = subprocess.run(['gpg', '--detach-sign', '--armor'], input=code.encode(), capture_output=True)
    if proc.returncode != 0:
        print(f"Error signing {f}: {proc.stderr.decode()}")
        continue

    sig = proc.stdout.decode().strip()
    indented_sig = '\n'.join(['  ' + line for line in sig.splitlines()])

    # Reconstruct
    new_front = "---\n"
    if id_m: new_front += f"id: {id_m.group(1).strip()}\n"
    if spdx_m: new_front += f"spdx-id: {spdx_m.group(1).strip()}\n"
    if origin_m: new_front += f"origin: {origin_m.group(1).strip()}\n"
    if hash_m: new_front += f"hash: {hash_m.group(1).strip()}\n"
    if ver_m: new_front += f"version: {ver_m.group(1).strip()}\n"
    new_front += f"signature: |\n{indented_sig}\n---\n"

    with open(f, 'w') as file: file.write(new_front + code)
    print(f"Successfully processed {f}")
