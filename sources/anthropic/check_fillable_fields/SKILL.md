---
description: Imported skill check_fillable_fields from anthropic
name: check_fillable_fields
signature: 250d5aa4e8451d6a83d17d3550c14e6c844ac347145f916ebf7980b118312b41
source: /a0/tmp/skills_research/anthropic/skills/pdf/scripts/check_fillable_fields.py
---

import sys
from pypdf import PdfReader


# Script for Claude to run to determine whether a PDF has fillable form fields. See forms.md.


reader = PdfReader(sys.argv[1])
if (reader.get_fields()):
    print("This PDF has fillable form fields")
else:
    print("This PDF does not have fillable form fields; you will need to visually determine where to enter data")
