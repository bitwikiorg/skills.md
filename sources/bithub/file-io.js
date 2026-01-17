---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitwikiorg/skills.md
version: 1.0.0
signature: |
    -----BEGIN PGP SIGNATURE-----
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlrArkACgkQicnEBsaH
    U1+SMBAAk5IxqFMYIESYVOf0N7ZNGIIZVQ8Nc9F6UbVDjBaROEFBbQPf/CXLBlr4
    UOcUONX8sUpqGphrOIxx5GxMhWnBZjblpwVmlgzOkpzxJxvpVfUYM+fLdjOeeXxj
    sSykYAQpzGNZv+6+5qfJ6tCYIegPzXYl6ObleHAOD/rTYhjjjH1CanbrpitW50RX
    IgR3PMC3LVcPb1Whx6em6/tUbMUtrglovDfIF29IFOfSDOq4yLkDl0+ScZrcGxki
    IqRyv9ouukR05ba8kq9d+5SuXuqIZZiQcf38+qdBu8jGg9lO9CzQgLmGy1VUVulW
    YgxAaM4yQmhmzGY+K5vf3J9Rr9DwSJriO8yVE8XVeMoo37O7AuMayWNUNKkF5vaT
    WxAaPmt6vQJONjl9XkpS2FUoMMKTnihxPAdHZLi/uUCrU2liCaKE9Li6r55PEzGT
    qRnDYWDv0FmFbHo74RQ4UnIWfRHXvHIyu1UF0hk2Y/Mbo8MmNF0GNChDtXV+Oq/x
    Y2eMYvdc0BcXom1rt18bF7W9ocUmCSqk1iRIaV3uVMIOZlkZs7G0k08h31gXl+6Y
    28ya2yW2u1sk6aH3lJd1bHcGbht5OMcTH+ElrjaxEsLDY53VZhmaODmeWLminReM
    E1YJ40Lqy71cgm7lpfVCiq6sfcHFXfkeFR/LAvS74Vmgeh/fjqw=
    =NaYk
    -----END PGP SIGNATURE-----

---
// Read file asynchronously
export async function readFile(path) { return Deno.readTextFile(path); }
