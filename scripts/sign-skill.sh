#!/bin/bash
FILE=$1

# Extract code body (everything after the second ---)
awk 'BEGIN{p=0} /^---$/{p++;next} p>=2 {print}' "$FILE" > temp_code.js

# Generate detached signature of the code
gpg --batch --yes --armor --detach-sign --output temp.sig temp_code.js

# Read signature, indent it, and prepare for YAML injection
# We use 4 spaces for indentation to match YAML block scalar
SIG=$(cat temp.sig | sed 's/^/    /')

python3 -c "
import sys
import re

file_path = '$FILE'
with open('temp.sig', 'r') as f:
    sig = f.read()

with open(file_path, 'r') as f:
    content = f.read()

# Regex to find frontmatter
match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
if match:
    frontmatter = match.group(1)
    body = match.group(2)
    
    # Remove existing signature field if present
    # This regex looks for 'signature: |' followed by indented lines
    frontmatter = re.sub(r'signature: \|\n(    .*\n)*', '', frontmatter)
    
    # Add new signature
    # We append it to the end of the frontmatter
    new_frontmatter = frontmatter.strip() + '\n' + 'signature: |\n' + ''.join(['    ' + line + '\n' for line in sig.splitlines()])
    
    with open(file_path, 'w') as f:
        f.write('---\n' + new_frontmatter + '\n---\n' + body)
"

rm temp_code.js temp.sig
