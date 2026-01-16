import os
import sys
# Minimal valid implementation
valid_licenses = ["Apache-2.0", "MIT", "BSD-3-Clause", "GPL-3.0-or-later", "Proprietary"]
failed = False
for root, dirs, files in os.walk("sources"):
    for file in files:
        if file.endswith(".js"):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            # Simple parsing to avoid external deps for now if possible, or use regex
            import re
            match = re.search(r'spdx-id:\s*([\w\.\-]+)', content)
            if not match or match.group(1) not in valid_licenses:
                print(f"Invalid License in {path}: {match.group(1) if match else 'None'}")
                failed = True
if failed: sys.exit(1)
