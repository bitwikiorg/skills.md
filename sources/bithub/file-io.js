---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:9d9b978e86e950d544397e6d712a756e4ec236d870489fb41d70e1a6fc8a17dd
version: 1.0.0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlphnAACgkQicnEBsaH
U19RSg/+P/zrI3Aes/04FDAvFmv1+UD6qxxgnY1YYyQVLX6eDOQNcnQxk+jxFtN2
bNYEVide1ldmuPDaM253WxP0eQ+H+tTg1MrpjqbyOxZkCMxVWJhLJCx5Gcp3CVkA
HA35cQDKwKYTbDckTB3RLtSd6uy0Dqj6CtIcmFhYZhNNUysAWdpJAb8nwL97+aKk
6Eej2DYej4PpGj1I7C/TdTrqd3tW4lbGt/21IS8yABKaVDw6KY5X4UnvxX2yWL0A
LzdYB31/fGnCxZWGx7GNtdrqEvHDLWr31beGnEr0TRN2beKUzSQOIWScfB3iu5TB
SZsC3oMhmUJwqAk/9vAAaxL+VyD+IcljKutzSs3oJI0oFc9KWhfOByQgMza8wnK4
wvuHEPQZ+u9aIXPDFvfhL29MQpjLJVtrUZqrRZN1I+3puTn86DObgZeDA/HhirZK
A63LF730fQ7ojtY01S5iBFdw21PfcUaHAt0pEtNiqL/q256mkEqqo6dVxBGsIscy
OjL+pGM6WSXcV9Avc89NdWEbNvEam8SwZE16OdBfM07c1TGFl6oB8qEREYP5z2Ln
ggsj5zxvstr9pDQqZEnl1Ds7IqpL9J3DdF3Uka75ath6aaf8h9+s3J+uuc3cnqFu
x2CL92uwRvufYIfoC0HreRUES8G9kVS8BFgh6ntBaMXZkttBHK8=
=vZ5e
-----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
 return Deno.readTextFile(path);
}
