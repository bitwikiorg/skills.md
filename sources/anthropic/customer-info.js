---
id: anthropic.customer-info
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:ee8691aaa7e545e3c12ec627853c5d93cd47792b442371e34e255a6e157d1bc0
version: 1.0.0
signature: |
    -----BEGIN PGP SIGNATURE-----
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlrBy8ACgkQicnEBsaH
    U1+8CA/+JYyMn9mynP9EIc+G6ycAMdo3RUXRfxSpTBDcqCvtbN+GV6Po14f4FOIC
    GBXYiKVU1w4dfMRhmK3dGowTZEtH1RcXp5Ns3BHRVMXpJ7wnWEjdSNU/LDIJScdY
    yQVD4CvfkLuZk5oeD3fYggMFDpOEd6DwCm5LGmeOcIv75RxTd9Ec3RC8b+ySXN/A
    VvlqwIdry0mFvLJZKwcfJxViCAOYfJcZG3h08+EwvHK/3nCOAauV5Wvyqn4cNGsn
    z4Ctfo5qrXmbgbzvBm1IBJk5nx765i/g3g0/X1k/p5WbMqIK2DU/vUg5tPtLiLlz
    8bn0vVry6wjExa66bJrY7FvbaUFJRx1/jyV8orNkyxXP+wrkqynDckoaRWfThCAE
    aCvofBaBUed6FTK5rqrjJcozGYst7wwsYmOMmNFcNETq91zzv8qANTdJGuhK9SdS
    /SIwrxwB+2AHkpOQeWgogMmU2vV8yNVRLCBTzuU6YeZpVdy3pd6WjB4dGYlcf7ds
    16zbWgW1gBtG/bSRGbxZn610X5qN8DN9fM2p2bwviEItzF00Z5dLRrunJeomuvqP
    HI33rEQY2HiF+0y1vgMbZ0yHbggIJIB4X2E44Ed3KuvYRNERiEl9FIh4oDaz9WfY
    CDgPyPJeB0w2XBcybY0tbKwNqVW++J8i68W3TWfoGSCZQntoT/w=
    =dfIS
    -----END PGP SIGNATURE-----

---
export function getCustomerInfo(id) { const db = { "C1": {name: "John", email: "j@x.com"} }; return db[id] || "Not found"; }
