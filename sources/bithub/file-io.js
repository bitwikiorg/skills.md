---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:9d9b978e86e950d544397e6d712a756e4ec236d870489fb41d70e1a6fc8a17dd
version: 1.0.0
signature: |
  -----BEGIN PGP SIGNATURE-----
  
  iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpl0EACgkQicnEBsaH
  U19FIA//ex7ETa1qKfd6VoranVbTBbW3GCs3iHzpHncqqBaPtGg2RS8mWDVSvP+0
  uiyDotCK8a9NduwP973izMmpF0it1kdesKXx7LSzvjdEBZdwu6M+IYnIsrZ6yb1O
  QASJjt3GiEj9Xu97Bpr2mKfgufCG1tgLw5PXb30MNx6JWv4A95zUdxDyevVZweDC
  lKMCKcurbK4aUg/Oi1mzARzXTiPszpZqgsvWygECQ3EZJwJO/YR7FUqbr5AQ29Kb
  gkJoZHS6sbHMALuLVEQWtaQQn/Ig83m09Ewr2w+N4t/S3mClJ21Iz2OMStFf6X/K
  aMoiWXqbhmuf01S53QES+6gCz2YoA2Dqw0LWQugFlQZ/xXzRuk+qFU8j1lJFu/LA
  XlUzU6YsdG9yCrbC1Gw3da/YCjzmV/PFyFq1X/JLzgnfVNzYidPLEkr8WylIYnXK
  0YAw4ZaSRHx0UFQtA/XFNxeSyJIbe/+kcXNNGqVb+c9geKQeO6weZzDNaij04pnQ
  jjKfu07QCeB/bhaiz63ykiLprWr5/iUdYxjdYYaMCVoNg84vP0y0IQXDThAXrMgk
  4ohkgXA6TNbipUFCwz5xmCSD84QimLLdEWwRANMHUUu7VzdAcFw9NNBofi92FcDA
  OqKDJfBP4NpDEfEaiCUntXvg7YF/b9hCTQQeV6JjBHE2S+4ezXI=
  =vQi+
  -----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
  return Deno.readTextFile(path);
}
