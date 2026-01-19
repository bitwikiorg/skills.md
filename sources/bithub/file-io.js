---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitwikiorg/skills.md
version: 1.0.0
signature: |
    -----BEGIN PGP SIGNATURE-----
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlrA+cACgkQicnEBsaH
    U18lCxAAgevw7oWt/1neN/KLqxL/6Xo9TfSaKt5l+ayBX//yQLxlO5c0NCCC4QYO
    ff1/9GXYe/b4pRUldzsFSecaPDgsei+QXKzgRBUG6EiLvPTDD3I5GEH00/PlVtLj
    cFOZYXm0A0zfhsYXlnPw6nPyYzivf2u9Etb7FwscVtwF4lMHKYVGN3xUEiH9R8yB
    oZyC6kb/iaBSKzkndRwtZWiFOw15INQs9PPQXKYJ5kRZ3FFU8sunrKOO5rpRiW1y
    gWYLABCiGoDDSNZjoYxUTOFAp2muUTOwkk1aV5x+eeB2x95XG1/AWOva+x/iZqpK
    Um0UTxtSbZgMTjSg5ggwdyVRxtb2fythdwvgPaEa604W4T76ruiqjjFikmVb6xv4
    pp1ukNSYPfhRbhvCUGrscz0uRqlsXCO+WBOIQZwIL2mnGb9Iyrw52zn7NfXVOgul
    jYczGpNz+cV9T23mVhslP2FUGdrSWpabt2EPaPvgVLokk+Jc9aFeHeTgkcJCviS5
    AHQHs0G0LEd1t5em85OONsrd6/G6+ossFuTfDHyoC3maNOE9vqoA9TEsIEFWQYzF
    UJI8TnrOMLkBvP3alwDUT9vYgbYjBSHC2JhL+Dm/d6zFD1dq5XkmYCCpZPcygWyJ
    c7MBL2FqKrHuo/jy2kUcP8nZVYx+LoyDSW6Fv2410UdPlxuq6JA=
    =jcDE
    -----END PGP SIGNATURE-----

---
/* global Deno */
// Read file asynchronously
export async function readFile(path) { return Deno.readTextFile(path); }
