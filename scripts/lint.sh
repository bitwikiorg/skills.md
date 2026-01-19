#!/usr/bin/env bash
set -e
echo "Linting JavaScript (stripping frontmatter)..."
for f in sources/**/*.js; do
# Extract code after second '---' and pipe to eslint
awk '/^---$/{c++;next} c>=2' "$f" | npx eslint --stdin --stdin-filename "$f"
done

echo "Linting YAML..."
yamllint -d "{extends: relaxed, rules: {line-length: {max: 120}}}" sources/

echo "Linting JSON Schemas..."
for f in schemas/*.json; do
if [ -f "$f" ]; then npx ajv compile -s "$f"; fi
done
