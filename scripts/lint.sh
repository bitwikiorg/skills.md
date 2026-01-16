#!/bin/bash
# Install eslint if not present (for local testing, CI handles it)
if ! command -v eslint &> /dev/null; then
    npm install eslint --save-dev
fi
npx eslint sources/**/*.js
