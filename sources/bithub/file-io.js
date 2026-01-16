---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:3b7ed55a102016a6d1cb390d4f077dfb8e5493765c09180b71b7c36ec81c6d55
version: 1.0.0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlph78ACgkQicnEBsaH
U1+e2Q/+LgyMUNEwElgpPiMJo3yrkHarKp0XnHnvBuX4ysORATymFxXO3ff0Zd//
yC0GQByjFz7vGbkIxt3JYdooi29BX1nXVSg1CmG0DY7ho8bugq+PPzvEliiGezuK
wxjiVjstfP0CdKUN6s6ux7926KGuZdx3Q6XUY/Znmb6dEBWldsQTk3esBrle09q8
OWWAW1qi0QCWOJysb0E4W5ViebqbmuJU50w8qiX27kNLDTgJ7Y86S+8IdL47KrDL
I6o/hNtUO3aSPs4snJTohnUl1WkgoXFlhKJ1mTcFvjPrXa46/oyO5jmuyoynS0lL
fwVoRvPURdLLEb+3ukOC018yQzco37q3fPoGcc2Mc9Pmqoer1U7BEh/Kmv8Lrv2j
RN5/PyYhQjRcPMxbXPTcu9V79lxLxdTemiBu73GKICkn8WvvsWVMOuZOss7w6Mab
a2qMPxlcdaTLZSGrujF23wwtTbgukfUTCyTvJjAsrX93tTyzLiCKlYk3u2uHo9d6
pd8BFjxsfycWDH825MzFUgiD139UTuT/WQ5Ea76TUwdsg0GW4SzOG+rPNuJYcehE
A+O3EFCcf2o1b29Gw0LRxM2Ofa0DPGRP09gvUJ7a5saiRxGzB7wFDT6dW9DOjov8
BZJH73oVAAq8b7ktigYIogGeKr30o8K2lzNlRJNhIyXyYVqlX1A=
=JqEk
-----END PGP SIGNATURE-----
---
/* global Deno */
export async function readFile(path) {
 return Deno.readTextFile(path);
}
