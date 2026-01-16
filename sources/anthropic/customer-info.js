---
id: anthropic.customer-info
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:ee8691aaa7e545e3c12ec627853c5d93cd47792b442371e34e255a6e157d1bc0
signature: |
  -----BEGIN PGP SIGNATURE-----
  
  iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpl0EACgkQicnEBsaH
  U1+J3xAAlVSnGdzehjcIqXE43abukdNbBx+tEOK0lg5mOUZ5YFCMXgWXk9iH5JqC
  ibBalX4rexmTtIMuTkm+O03jvyfvUewXjOW+IlrTB0CVP3syvWaNPKp1E09/LdHi
  qyRUxsaz0qhY+KJLrvWYPH0Jnu7HQ0ouxaFaEw+/L3h3fI1bVFDqeCVZSmJDvfvq
  BPXuz+hdDv9mLz7lmK8+VaCagzZp4KbJvH9oHWjgdphlhKAmYNGpEFlFBdBlJWSR
  w4aOwgZWP1YYYgVSEQf2Gpwm3mrlrwYRpyqtMbXIrf/NchiztHM17Lys3gmJAqPT
  YHtkZc+x7j7fP+VeJ+wfJ90f/hXaDtKyh2H5ufaQk7AklQA4uaFaywTCoNZeEKRA
  3rCogzDnjPb6bXi4D0YQilcibGi/K9/xYnll4paKVBuH3BetHSVWBdMimpmZNL22
  kxTVW2WpADsZMZojbt9CBnMW0dg5f1PMKqs9b3WwBR2WugA5C554hsVMCQ9QkdQm
  aeAXp4VLIaGqaGHHARiWErapXcMM05QycB7ZXlj0VfobLlwHZJtPijwF9dCQWy4C
  7uUh4KYkH0YyYjBf2R8WthFYYff9hcg3FfmHnTZlDqZdDfnF07OcEnBFEvxnVJDA
  rhB7NqAFaE4LO8FVvzk7uLu22bl/yYoXG79/9MWQtagBJed5QGQ=
  =2KLH
  -----END PGP SIGNATURE-----
---
export function getCustomerInfo(id) { const db = { "C1": {name: "John", email: "j@x.com"} }; return db[id] || "Not found"; }
