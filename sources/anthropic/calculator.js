---
id: anthropic.calculator
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:917ef6c93a50ef027f2ab913910110ab4a579620807c15db149bfe3b20158407
signature: |
  -----BEGIN PGP SIGNATURE-----
  
  iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpl0EACgkQicnEBsaH
  U19rixAAsyV1flLHrEwgcbB9bHiPY8gHW1PO8ai4QyEGjExDBDUICSXPzijNVqNN
  N9JDWcigv2NtmIE05QA5wc3TZFKTOuhELGG7MtbqBsUFwaUE9VfVhE/ldd+1CGiy
  pwrfEB9AuIBOOUl5MUNoUBv1lVfJc83BKcdj+MW/DFg+/dazTMAzzimo7TwGJ1BN
  iCeExSDIOwb3jkU0H0Mj+VpZPjf1PrhzEbx4LsDbQqN2NFAzWjRMxnBlWmiVBwtE
  KmX7U1jQrmJWjAWwEqIC1om43D1FEgyelEHdxuGLxQKJlxzL7mJhZrPnXCXftmVs
  qU2uJF/xDKRTfOyn71/HVZNdUMI5b9Nzj+GxTqTxwJ1s1Oaz3oITHPYRVrJSCAe3
  c6zAXbfQQ1WFVEabolsJql6DbpgRE7XuTHctB9LRnWNE95x3Ff2bDega50gLT9Mj
  NSvFcuJLwG7K9b87nK45G5yMrQM17sncrwffBYkZaAQzDeCW/6PyPCX8UuaEDy42
  UiWHNzoZq3qlMxRpBNII2iaHAzNlJEPDRWf3PvcTdJE1GVzOVunPspYThQEYMXaa
  EyVHruhaU6qcLhgZ/jlbhhgzLmIlp+Ve+fX/csYxASmNh+QwaAWR8blcgtN8wy1/
  jl2S8ilJPuNoL5yz7Mb2+3P3Qb2jJ4zAX0MKMppDlYvNno6Onxg=
  =ptuB
  -----END PGP SIGNATURE-----
---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch(e) { return 'Error'; } }
