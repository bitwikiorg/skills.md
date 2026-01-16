---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:9d9b978e86e950d544397e6d712a756e4ec236d870489fb41d70e1a6fc8a17dd
version: 1.0.0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlplJMACgkQicnEBsaH
U1+w2Q/+KTStPdbouBshnwHOsoipxDAIGWGyL6rBqSflkklClUQl7ix7/xV+elYa
DvfSSdGglFAU/BzjafIwGUSQXZYuEuaH3tr+eWQfz/vkZ+GZqVALj0wX4S8VlfJL
P98QPJaCvFha6dpYPXUGoNKuNLt75Afguf4rpbupS2qSoKDZN/om1aXgbMJcDGt1
XTBcwC6RsL5TOmqvrlBp/4NHGTTxm72mOCSEKz2EpeR7hezT+YDvyiPK2PJCW245
gMlicZcZoe3uul2PM3RpKSmRzhCalcNh0mzEZCO53kSRBqHj9ojtMaBbNs0l4mqr
/J0ihwLqp62+62eOG9vrbnjdxmnl92eC/cHn0auwvCIJKqVD2MIBS4EbLY34rh+J
PceTeMOJ7r3D3XY43h4/Kj3Q+lfxd//FkacRj+I2CQRASlyzYJnni1AATLdZhx4q
mxXCGSYODkcHk/ptaB60/zK1gZK2+mStuOQOz8y0sQ0Z7O/9xHwNa1lJdJIIN+xO
7QmUJbpJUayK58tieKCtzlmTnzkHC9a6CLgtzyx7nv6Im69pvTsgw133Ez6KeRTf
lGXhqP8mAk6+to52A7BySqmNmUMOz4cKwmvY6A1hFZRYQkGKFMxucecAWrs5hP7t
g0Krsi4hcUguXjFZu2BN7AS15LVswAOpwqQEoleLUi9uLb2uowI=
=dsC6
-----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
  return Deno.readTextFile(path);
}
