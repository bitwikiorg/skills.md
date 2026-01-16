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
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlqQKQACgkQicnEBsaH
    U18XhQ/8Dg/3mVZFs5z5+ZApsdb/4FA8hRicH6+HDMav95z07rOyFpXj4EKWYx95
    AachPd26eFNw2/PyvefMtTD5IoSj1IU4CTdQUIyk1a6TKfRKVBwf7BBrg4gul57o
    cO7l512NuYurC4KfgbIn5U3Q+UtrInOhb1xJ9P85VwfswbDMws8SRdAnJlqZKZA5
    Uw/d9+9lPUOywR+ArJxLZ+8wJHWdXTCWeckpZeAewwczqc5IWWv6+BPHgRKEbqYc
    JESvpI+IVZ76upHt41beTz/SPy2XbB3Cieuf05pbBm4nPpTykvn2Ys+/Nfdl/lk3
    8iavJ8uxVmrez5wGShm33we7qLTD5kREQ3KMWbCD2ObqZdBiSxRcPAh7BD/tipgC
    6cXRwZa+qeD3KOODD0SYz1xO4YRM57K6zwVlJSAWfCGyK5oacIi/GYPYCx7zjI7f
    mj++oe/OLiOsHrefgYm3E4ARcZHz6qVHsU2dcTCEAmZ3qTn0+jDFos2BcA+6pe3G
    VrCsvkKjIFycDF8p0I3yE9bIkam1pxj000mymjpw7NSudeK6/azACki/e/WoSm1W
    oMEO/GZJ814Iz1ZbQXn7DMK2CWhwMmmvOWV7z/11q/GFaGDDWxh7VkPkZ9sViQGu
    l6VsS4rTiCv2AObxOrQPe7ZGEkhU4kF9mXvyyrDgrPBPEq0ZUUI=
    =Mxbr
    -----END PGP SIGNATURE-----

---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch { return 'Error'; } }
