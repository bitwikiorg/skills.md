---
id: anthropic.calculator
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:917ef6c93a50ef027f2ab913910110ab4a579620807c15db149bfe3b20158407
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpkU8ACgkQicnEBsaH
U1+1/BAAn5LaLBAIES/V/t5ONJV0T1W8MIHWH5PMuDhfWJZcDyEBTw7k6W7EBiEe
xw2EfNzT+vBEiVJFVsV1Rf7RFpGWGWTX/vftyMzkp8UBtjxHkZt17KAc9g7ZACZE
9Ou692ionfHSx+PAQ6bKGV7lB7THXk1E0SxcRzf3UCQZr0JlgLXtj5LEKIsGhYRJ
jYCNe39ea9BAN6LbhpltZ3uBIo/HvnXC5wKZyl9/ZcozAB4/MeWHq3BVjCLBadaJ
xjZFu03Tum/Gkug4GNllePu1jn2Gk1a00HmIJ3d20Z7lnPaVqaWQyETFgr0Uh4ZE
vwtaWc7qsi6QOQzFntpUAmtm6LLcVKIT4WZOFCTEqlizvX4c6YrsOtX75IGTX+5W
Be16O4xqj4UWwbtdbB3+3DqelejThm6T2tnTR3vLiUMFmwBu/PDtnhC8ulLgmOo2
8HB8rggmehQ+yHe8uayM1yY1qhFhQSsb/VRQFiMpwbksRr1+7g+G8BoUv6z1CreD
CkBb1QPdgHC5E0rQS3pwlmIieZMncHznuj38OCzIEQC//+NkscAtgqG21vg51B2/
NXOmMmaFTLI2WX79LFykpgupDy+4DwfoHSKTTLkBCp4oP17wI+Ezd9UbZvDuF8fX
DWhfgAYGLkpeEP49cYSpsSGMNgxNlh7UYaz9t0GFcPI1BNGKkG4=
=yAox
-----END PGP SIGNATURE-----
version: 1.0.0
---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch(e) { return 'Error'; } }
