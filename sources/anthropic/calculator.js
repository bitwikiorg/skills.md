---
id: anthropic.calculator
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:917ef6c93a50ef027f2ab913910110ab4a579620807c15db149bfe3b20158407
version: 1.0.0
  -----BEGIN PGP SIGNATURE-----
  
  iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpmMQACgkQicnEBsaH
  U19yaA/+ImLpU2EA2ebP6yYQmxXu4+1XMSBW6VID+Q66cNFPYEuYuGJ3Kvn/bSyd
  MdydRH6Hdcsu8OkXsBdKjUECoXhzB3JpR4szToBNNdtcQ3rdB2p3ZXdoxn7WEYye
  ohpmCnnqubgg9miuu/BKyYyTmGX0+iQ/7qqXegIvgolvsIYAW7jtEIf36PQAar9A
  y02SiGEXtI8yhaxpNyvyz7IC63t1JTSc1hH4leV6LNFxG81RoD8+yRVafcZhTLnW
  6HwuTUXBiGTr3rH0GT2KXaE0p/5JSMQWbr4ffJIc1PNg+u9vq63gdubxEmkpp2Rq
  VCkUx6F9K/+TpIOPOzOhPN9awJ7zEGJwtXYTSHiic+h7FlXlD2mmNpnVnh9wY3Mr
  QJNR5HuMJfLLV5SGXcH8ot+9aQogZgbRNk+Imj+D7/e9oEO7ONLPUEzUCNIB0AMP
  so4deZgnBCNbd3OGHuUc0V1mpeu7J7UU+ts75vEDqNh8z3Te/d0aTm1KwidGnJ7v
  Clr3t3ASMY8wHv2IeSxV/WNltMxn9FDiJR5Q4OTAu4lzDq6cuCchMck+Q1MHFqYA
  FCYGV7oH9pBbVr2q3ePHcMa9kPBum1UJFlw5zYqofbdCVZR5HS909PUHISTml4xE
  kNBrTj0nXWvdrk3KB9dcPDF0jYWn4PuzMZLXbNd4/Ol1zLTwMQk=
  =qeKH
  -----END PGP SIGNATURE-----
signature: |
 -----BEGIN PGP SIGNATURE-----
 
 iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlq9AoACgkQicnEBsaH
 U19w/w//eYLtAHODPjEBU3LPlSP31Qmw31cypGWQScyzHrGS360vpvu5G8vrPxjF
 KM0wu26/VcGFBbk8R0R+6v3yZDdL0CK7Xy+rW6sGbNb5FzAgApHHw7LbrQ3/a+cK
 sSrGUcEHy4GNq4jyLjCegc66qT5dxRC0dU48n+2m6+z9608xmEFfTP1d/1MU28Kw
 R3GiZgsp5nWcPH9kHPJrZdndC5R3NYlygETiykYPXKd1xPXdLVGwlBtNKp1cy/Wi
 afeQ+MvR3KsQcjSBKcwMah4rc9+HXyy4hUWMaeA9C2x/rYbUAI9Y5HVwVc9kBjEc
 w4M9sxWmBwSl2CVtGy2XHPujUmT8JU2MbaqD2SOf+WOlLm5pkPyE0Lw7mmjRHE7k
 mmKv+gENxSXjXFeFiy3GuyPHv/991tTS5ZerDmYJRds/PAzlygNhr4qnyjy0klEw
 TEr2lNQXorucswjRiCtGBI3HrIR6in4mG/R+GgPVPOq/OzNWsl9RVOd8l6QE2bVL
 +qtHw8jZwL6vg4HWlGulXbyqyZuZpiyh1mLqRePDarpOT1hezolX7OTriC5R4mbQ
 fyVS7v72xB0VQDq2XmWfafBSX5SQa9EO0Wgga2qv8doB79q7EjagMwluw05oksOG
 wnslxf1BdIYgOZ4gUL4JNcgq9Ic/U86fJmxliJQ/7mLuHxKkhVY=
 =SqS/
 -----END PGP SIGNATURE-----

---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch { return 'Error'; } }
