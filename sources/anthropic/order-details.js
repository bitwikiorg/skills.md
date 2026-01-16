---
id: anthropic.order-details
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:61060a9bc92d64a74bbf92608986f51179b20e3451762c522224479b14603332
signature: |
  -----BEGIN PGP SIGNATURE-----
  
  iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpl0EACgkQicnEBsaH
  U180nQ//dcHr4vdeIPZ1nF+x1XjzpuF1YQdIiB9y3dIk3sRi3YJ64MeS6og3jLSA
  ZthbTsVcngrHEsLBQUVQUVwexW2jqLuYeOFVBuAQLECMC06t1B8YuzvnnEAwDy56
  9UGuqpT/+jjMRAA1WpioK6Rrby690bSk3o7mvr5EuprXP6m8ZyBJBUXyRfpFPlXt
  N2jUZzeGjFJFH2CK/w7jxG+iszCS7yJqC952/H4rnXz9YOvzmEz0ioeF+N+538eb
  uZvCu+2vKl+rDP25GEIyWXvJ97jrh6kArxvvQIqlih/uyQ+ahTDRumW9J4XrrQjP
  4V3+v4cgZINUOHkHuvF3YmTJHAh2itcvTnMJwJliJH0yEJfM+GIwwhVvwk3EOyU5
  CrSiH+HjNwBgB2zk7zPNdkuzRAF8IjjvT5rWdkviV+CtTFSY760k6/Z4+WeP5LdJ
  3WZy+MIJFHk0dPFDGPu/y5hqz6PJRzTUaJzA6II3kqiN7yetSYvWt+mvGad1KHWU
  Pf2PHtiK1cNFjaxb2VY8XOjhP5YeH9nI9OpcFln9aH5boEeTr9OTWIF2BpIDRE4s
  w2SvYQBlC4rduAdryFaZtx4hKdFN6BegckXyZ+kGmWxuSAYxDVGhR2gOgjFExNr9
  AQuCcFxI9JnPC0oQmDV095BOW+8xo3uPI200s9DA2rAVcGsy/4A=
  =nSbm
  -----END PGP SIGNATURE-----
---
export function getOrderDetails(id) { const db = { "O1": {product: "Widget", price: 19.99} }; return db[id] || "Not found"; }
