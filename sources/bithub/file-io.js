---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:9d9b978e86e950d544397e6d712a756e4ec236d870489fb41d70e1a6fc8a17dd
version: 1.0.0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlphuMACgkQicnEBsaH
U18eeg/9HT5T/jXJbNrg04H8NB5qESGzFII0fnHYCpS01BJgPcH/q6daGG8SMa01
A4bvEResaN7I50z0EMaqihZOp4knVdFnHuccCCJetI0Dza6lP2mOf2lWf6404crM
Y9D9duM5aG7nZCB2uufX5gX7nynCzYBBNaKYAbn+etiWE4XZRzHHZqeM4zdRsFHj
hli42krQJZEx11SADbREc86OqoP2zUOdQ3jYwUXpUj9k84OSbxYAUshPlBSpVH8b
i/27p7hor7ZC7l5uQoK7cE9rM8P0ND0Z0MjzMbraQOp27IOEyXDxDczlxuGr4NpC
6y81X9bhdeeaqWHi6zbcgKpDVn4B4KzwZNyqLo8R4wsDIUGDQb6ni/QGfRrWdZse
e7kruf+xXTidPvd6D/rhOU8OzQdlsi+EFPRhRHobtbOi9qSTtBf2WUwU83NQPdvt
BmY5scLy5fDr6eMWNAoxyKbzpRs34hZM06HyntyCDrs0QOpcST4mdu6zsHAIRInF
bG8o9wy2qcaHm03eivnp6kLhvgehCkO/tFYlZQdi99IYn5jTXrmw+XB0R7+QZxHw
SZjIqbfbkc5yku1gFiwE6gzid9rNTsyGEa1B+uzYM4/wygOEqufpDgN/4G4FMcpE
WDjQp7BulB5e+Xo3S0M1mZsbj44yvdi+OCYoSlLR9fwO3iC+wLY=
=fRQ3
-----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
  return Deno.readTextFile(path);
}

