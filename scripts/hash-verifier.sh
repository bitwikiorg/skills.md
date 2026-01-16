#!/usr/bin/env bash
FILE=$1
# extract everything after the closing "---" line
CODE=$(awk '/^---$/{c++;next} c==1' "$FILE")
echo -n "$CODE" | sha256sum | cut -d' ' -f1
