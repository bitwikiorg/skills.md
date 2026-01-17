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
 
 iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlq9Y4ACgkQicnEBsaH
 U1/mWQ//SwWi+7D8ND/qrToKTV0zvIRRgIjPp3+sQ1rIFuzbjrmgGUVRm0n0g3lE
 Z8CPM8faX6xxc5jkkdqEa4FrhY7BV3uEE3bZlOyMvc4vpmgpYn7tMhN0vWL3kptA
 ac09M2Q1GGA7HinP0VtFrC4VzVGfO+Wy33j5RtNJ5Z8V4+IU1tfNLIrk7FjelvUN
 2pF34dwCEsWOW0gYmda1bP34hVzs8s/IWgernSd/O+AKMu6h2emE78KopU04NBpT
 PeLcOxuNvIjCQlI//oc9+DvDQo9taDr9aLAVoyCX2VUyZMJxtpyd13vlGnj4/f4M
 AIBSzZ6q+yIEnaDhIDxQwRqPNQGYcoG/ak3MYkNobwpkW/IwIRNo0+CreA0CLiSI
 Ca8fEG58zGCJJpFwApRl0MTN6sKVC+dI+7bJgAAFnvsxU4pzdGHsEJuk5z7lCkL3
 uDKM/S3K1i+wnoQCXFk1VZuZjW9KyTUFyCay50166w4vfVXQMJ6Gx5A1i40bpUfl
 mlqR5rXeDUDMFkpVub8esqAfQLclEFKADCkTa20VSYNSzOjJqrEdRdmTRU+GjjsR
 IDgjdaGutGMmwZF28DWrDAs2DTK/EW9gSzm0/r1wOYVm/yELBne77gbu8LSSyPSy
 z+L9Tlj1fX01BQGxvpjGmczQgz+cXlXsdeW8X8YZqLHpL/kgyfQ=
 =p8Uj
 -----END PGP SIGNATURE-----

---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch { return 'Error'; } }
