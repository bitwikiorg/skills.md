---
id: anthropic.order-details
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:61060a9bc92d64a74bbf92608986f51179b20e3451762c522224479b14603332
version: 1.0.0
signature: |
    -----BEGIN PGP SIGNATURE-----
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlrBzsACgkQicnEBsaH
    U19HZQ//ZFvgB042R1T8iBy3TV1dsW7boRb0d70EAahfpT3MHns/j/hONV66mElD
    v9ZySpoV8fjEWop0XsIZiHfnAgjhZUZ3n0vcUAaWq+lg64Ur3N4xFUPdN/oC0Ewm
    /Hzn8W/0ffhift2qeVKvqRsebaI8M/TWu0cHyD4+E0bjuWEx+DvcS3Az09EHJX2q
    /c40/mX4RZxe9+Uru96NKbgpcXFZBmBfBOgrf+rJ6EPLEYDSLupLryrqdXNytbv1
    cfuRzgNxvuUyAY6s+4O3JYUpCJVq0ADxiLE9hB55FCeFJ00M0NIitaTGJgpoNq2F
    cHLGRarc54boUkpnVBKt+mysOHBP0SQRJb+ooBw3JC/Ve4a+Hna7fiYn+SooNx1r
    tkBt23CSXJe+6XedT9SJcIvvRuVnkgaiw1YNRkLaUuIOinptDK/8l1hCRsWwUjps
    t0rnFvSPaj1AamUIqtvst/39D8MYRKYZmgOWORcRaKMh+aHqfHcCsJlIL9l+N3K5
    I3L36qRzxsk2aJt+HE25S6mHIQEg2FIatFG9MZKKwSdvFD9vFg9JBBqVj/FVLTHZ
    BZRo/RC61ht3qrJzro6mVao++I775S6MoTWYv58EW7gp50xzd1yGL73l/OYeatsX
    XkCEr1XM8YTSTbdbepIypYyU/6xUGUNhMcZWeoTKGZ5WuG5oaBA=
    =CsEi
    -----END PGP SIGNATURE-----

---
export function getOrderDetails(id) { const db = { "O1": {product: "Widget", price: 19.99} }; return db[id] || "Not found"; }
