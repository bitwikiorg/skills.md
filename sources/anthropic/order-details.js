---
id: anthropic.order-details
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:61060a9bc92d64a74bbf92608986f51179b20e3451762c522224479b14603332
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpkU8ACgkQicnEBsaH
U1/00BAArPLTQtsC35SHF4Ihi7zE7D7Tv5HIekaUdtWfvbALAd183hy0djZT8yEO
2hpPkujUp/SBP4ICYV7Mso9/yOmgBu51VNFtWSQvraX132UTJwwTSvibzAPLG944
KwKfbXmpTJ91wUTTby83Tzp2jr57cgCKbrVbgEF0HsBLkNOCJtmqE7aMI8L4n/Cv
kyN5SfNtLKOFIL0GMwlG3Rkkc8Q0+Slv0tIikxulfYO2ltZUarM5TYZqXRgI92is
BX79eIO3Y/04jityN0f+Btle0lvBOg/eHcvh2rZUkETI47fMg1/C3I9VbpMp2B7H
Tr1TZFAgNnYHAe64MHlqwKlGWzXauaG2aKihkNSeO+isodt20VW1KlKhFOVUZp4o
kC9pYJo863KCANKK5nTwVknnuzwlYQ2q2KEHkFjRW31DfkEhEtz+N338gzrrJb5L
u0djuZslQcPe7/k+W53v0tjMeIM0RgsvolGJCFp8uc2pAZGKw+S0U/Bt1KUXIZta
bUfNRZklYZrtAUaZep9B83c/3woh0jDwca6z8KUV53wXjnpkUEPglDSmHTPbfqfG
fXJNHDQSq3Qvd20OQ3J9LX2MUepy7REj3miYGJaJbCt+Wh1OITUjxN+a1V1+Be+S
5As/hK/X/SNFA2AKXq8/2BUJ2966y3A1EwPaYDZVM86CdA9sdVg=
=4EWw
-----END PGP SIGNATURE-----
version: 1.0.0
---
export function getOrderDetails(id) { const db = { "O1": {product: "Widget", price: 19.99} }; return db[id] || "Not found"; }
