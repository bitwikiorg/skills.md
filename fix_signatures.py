import os
import glob
import subprocess
import re

files = glob.glob('sources/**/*.js', recursive=True)
for f in files:
    print(f"Processing {f}...")
    with open(f, 'r') as file:
        content = file.read()
    
    # Robustly split front-matter
    # The file structure is expected to be:
    # ---
    # metadata
    # ---
    # code
    # However, split('\n---\n') might behave differently depending on file start.
    # Let's assume standard frontmatter format.
    
    parts = content.split('\n---\n')
    
    # Handle case where file starts with ---\n
    if content.startswith('---\n'):
        # If it starts with ---, the first split element is empty string if we split by \n---\n? 
        # Actually, if it starts with ---\n, split('\n---\n') might miss the first separator if we are not careful.
        # Let's try a regex split or just standard frontmatter parsing logic.
        # But sticking to the user provided logic with a small adjustment for safety if needed.
        # User logic: parts = content.split('\n---\n')
        pass

    # Let's stick strictly to user provided python logic to avoid deviation unless it fails.
    # Re-writing user script exactly as requested.
    
    parts = content.split('\n---\n')
    if len(parts) < 2: 
        # Try splitting by just ---\n if the first newline is missing (start of file)
        parts = content.split('---\n')
        # If still < 3 (empty, meta, code), it might be tricky. 
        # Standard frontmatter: 
        # ---
        # meta
        # ---
        # code
        # split('---') gives ['', 'meta', 'code']
        
    # Let's use a more robust split for frontmatter
    # But I will use the user's script logic as base and fix if it errors.
    
    # Actually, let's just use the user's script exactly, it seems they know their data.
    pass

import os
import glob
import subprocess
import re

files = glob.glob('sources/**/*.js', recursive=True)
for f in files:
    print(f"Processing {f}...")
    with open(f, 'r') as file:
        content = file.read()
    
    # Robustly split front-matter
    # We expect: ---\n...\n---\nCODE
    # split('---\n') should give ['', 'metadata\n', 'CODE']
    parts = content.split('---\n')
    
    if len(parts) < 3:
        print(f"Skipping {f}: Malformed frontmatter structure")
        continue
        
    front = parts[1]
    # Rejoin the rest as code in case code contains ---\n
    code = '---\n'.join(parts[2:])
    
    # Parse fields manually
    id_match = re.search(r'id: (.*)', front)
    spdx_match = re.search(r'spdx-id: (.*)', front)
    origin_match = re.search(r'origin: (.*)', front)
    hash_match = re.search(r'hash: (.*)', front)
    ver_match = re.search(r'version: (.*)', front)
    
    if not (id_match and spdx_match and hash_match):
        print(f"Skipping {f}: Missing fields")
        continue
    
    # Sign Code
    proc = subprocess.run(['gpg', '--detach-sign', '--armor'], input=code.encode(), capture_output=True)
    sig = proc.stdout.decode().strip()
    
    # Indent signature for YAML block scalar
    indented_sig = '\n'.join(['  ' + line for line in sig.splitlines()])
    
    # Reconstruct YAML
    new_front = f"---\nid: {id_match.group(1).strip()}\n"
    new_front += f"spdx-id: {spdx_match.group(1).strip()}\n"
    if origin_match: new_front += f"origin: {origin_match.group(1).strip()}\n"
    new_front += f"hash: {hash_match.group(1).strip()}\n"
    if ver_match: new_front += f"version: {ver_match.group(1).strip()}\n"
    new_front += f"signature: |\n{indented_sig}\n---\n"
    
    with open(f, 'w') as file:
        file.write(new_front + code)
