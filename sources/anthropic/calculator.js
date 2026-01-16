---
id: anthropic.calculator
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:917ef6c93a50ef027f2ab913910110ab4a579620807c15db149bfe3b20158407
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlplJMACgkQicnEBsaH
U18GyRAAq+y18KQX2uqiEsyyWP5+lPusxUePzpZWJzwnD4Hzyubrq2l+AoPeDKvK
JcHoCTtWrunO9QPJfuAMWHJWWfQ9d29E4GE4Donp0/W5hhaWHSBwWzwf5owipJ3D
DqL4CUjVtWFxV+PsQn1pHecFs3APya+AXYpysZ0ZE0EZTHK8Wn7tw2PJbclYs5Ht
AtdPMFyIaN/cu5sxb9gnOIepTetpAMjxDy6pkbGB3eCt7LPB4VS3Olw4mFdTZ7ru
5ezUspTfcJJSYa/yZnhwRlmxYULMHi/iY71XYOdKYQM46KB6kAqBx48lZfzfnAEJ
srkyMtAYfI8FXW+Ao5ARTY2NIWP/Rnh/IRgoQNPMz/5u3gt3nl5I18Cl8I3wAxDq
IgaGslnfNEY1iFiJAW1x1Y5Dqg4KqwO1QAVEhBAV/HE6h3GBK12NgbjwHPFtqFkz
GgmCWdRQ8n4rdZxdx0io7C/J/yfg1sUocPzDEantsMVOtFYZx3t8W7StrlPx70Zt
VcX8IKp4P04zENWM04wikeGMH6mk3Kd/M3YsW/HZDTzSNKTViNFZyZ81ERVuZ571
Ige0LGZU5ChnmSOZfwFaIJ6oub2V9gtrpEK1E5tW4+jT+gCEBRoqAk5nQg/f+Nbs
/yWs7tm/0TeXRO4fK+d+NakOKw/McQSil5XdpCZX6AB7eP4xPjw=
=CbqO
-----END PGP SIGNATURE-----
---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch(e) { return 'Error'; } }
