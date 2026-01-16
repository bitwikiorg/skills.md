---
id: anthropic.order-details
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:61060a9bc92d64a74bbf92608986f51179b20e3451762c522224479b14603332
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlplJMACgkQicnEBsaH
U1+r+w/9FSY3TU5vVgid3je0NQ9j03T81N8hHJXoBX0xeqS6R/bCLrNiRgVOsGlk
G9yTVQCfprDNZ6PwjjPO8E6cickdWcQVCftHInS9OenqFElkY/16di0bp1t0iHdR
hZDTOI/kH7md6W0zO0WCiya2P8O/1mtmN2IplRxUftTC2daaZvaGF8R1DIwJoCjL
7fzKEIJ4uSaEgXAIqb1mMd7BzLHGLux+lY51lZCbDUY6V7yA0APvNgZ/HXazbVRu
w31cRTUHtD7b8rO8n5sSBOJVCIhFIr1qlLqu+8Whko2vPGbeTQo/Qs4C2FVIIzQz
AfgLFIgDXVW8UEJ8I9hHamGJnoXbn7xpTJI1R3DyMAu02kq/0J4its+CN6hEnCKj
2TVFnEOkCRxCUbpG2+lDj8vlhEcM+RmAwcxVTrV8F/kVq9SBVCi0zXvHpY6Zfmw6
lpTTtCyidCfmyVEWvGGBClyNhM+DCNdQRX7Wzrsszow2gEqV3gYL0zGxSB3XuUOL
6J/O/+dLXFiKgFd2BWnSIX/xQqP1dFqzdiN5Mt5CY9i5v3zpxAjkeRyjSm3veSHL
jfNPeBr/SegVAg/U9eOQLRQnupWwSjTWfmxhulobLkXTiE74siz7vZ7euJVNsjIY
y96p04XtxoPviUFyAur9ioo/mRz05t1fE5UgI4LiZM9bw4x7jew=
=ct/C
-----END PGP SIGNATURE-----
---
export function getOrderDetails(id) { const db = { "O1": {product: "Widget", price: 19.99} }; return db[id] || "Not found"; }
