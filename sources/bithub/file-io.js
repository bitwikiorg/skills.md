---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:9d9b978e86e950d544397e6d712a756e4ec236d870489fb41d70e1a6fc8a17dd
version: 1.0.0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpiAEACgkQicnEBsaH
U18P5A/+Pgv34AljOyFYlvHITS33P0QEotQ/THay+GK6DAjT2DU3jYpBOWwlV35J
cnVPPtSiUzJZGqZi4I50jeZYZMbd4zYtbpqBbZrMajZkiG5i/2bP4g7qsXwTCbew
BK7/3rzqgBmHg14GMjm0Rhd3NT2UveYPFZ8rcvKQeZG2UikhkSriV1ri/W3nazvb
R/IxgW+fYfhJEjPRmvC1oycsYaTIBLOhCIMpQDYxp8M1oxxVZdt/ykEbVm26KgNv
4+e4d/BOzPIeTzvQHg+AeI44wV2MniMAUnamltX3WeF7KzaeCkpLiXbttiHRXQrI
xq/U7uDXMVCkWp+RITjeg6UlDbcWf3bD92yqpPUyNKXBfieZVJ2iyr7BbA9VpBx6
72tYA/+ssTaKOC6KTb9kiWMocegA85+MaoS4KZ+13RSS6hKpOU4AG687TKFiUX/3
CKdLKjL9SX1zy3M8Jn96vUxkeTz3PPmRkftO+REvLf0J2meJ8JVMyVmkXANZRm3y
GeUsDagBoJaC54c82a9Cc5lqZG0JEBkgNkrvhKM8hI2eXf5TUs1ypYB93J5F0Xw+
jRx0lO/xwylwlMkV71iyLLx9Nl+1ktHJ72KtK37xmy8tqJUvY6BYZcmVdlHdyGtC
X8ZkQQ2jZPJUbJxWaLuVX+yCrsqU4HXjiAPvPkt3LndjnhNPIEc=
=pQgT
-----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
  return Deno.readTextFile(path);
}
