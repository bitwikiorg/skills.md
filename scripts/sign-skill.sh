#!/usr/bin/env bash
set -euo pipefail
FILE=$1

# Extract the YAML block (everything between the first two --- lines)
FRONT=$(awk '/^---$/{c++;next} c==1' "$FILE")

# Clear-sign the block with your private key (the key must be in your GPG keyring)
SIGNED=$(printf "%s\n" "$FRONT" | gpg --clearsign --armor)

# Replace the original front-matter with the signed block
awk -v signed="$SIGNED" '
 BEGIN{in_front=1}
 /^---$/ && in_front{print signed; in_front=0; next}
 {print}
' "$FILE" > "${FILE}.tmp"
mv "${FILE}.tmp" "$FILE"
