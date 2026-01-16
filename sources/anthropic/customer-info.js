---
id: anthropic.customer-info
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:ee8691aaa7e545e3c12ec627853c5d93cd47792b442371e34e255a6e157d1bc0
signature: -----BEGIN PGP SIGNATURE-----

iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlpkU8ACgkQicnEBsaH
U18WTxAAosUXYJYIRQ5TXCyHFIVIOjq6ueNpsPEBQ3lARer/4cZCO/ln+5JkQA2s
Jr409aAXAWutEmgcxMujtRbGoc5j17MwwHDITqFo5KLDbWn6shb8youWWK+5ktox
o7T/Ei5d+ZlFpjUG0hytUsqp8u71jkbmNgiP/h/xIdvnii2GII2BnIZB0Bnvk2Ic
hc4vkrnWD6n9iu0W7QQPkcXySdeSudUfpCID1l//u2LwxxdeUqskc152pqCdYtWr
4lDI1lTAqYz6Y4moJ8KvlStXFZMSQEAjM9EoNq97YKXwkfM5I7352JJkdk+9GXtJ
3vCL4HMxr50ZxbD/4aUUXpREWt2/7VbKhPORVz9M908huzXeZm843uP+o0ROoOL3
Rasf27un38CBl4r6HoaG+Sc2mo91jpK7IGUtrqBkUxgTiDon+w8H6aC4ULqoCuOs
AtCZJCtlTRf6rfczgLWnulUc/MyLgt1aWWwD+MCGgVz2yayuIHc7IhQK8HQRuqKe
8ZB3AD9xqbKUr4yZOXP2Y6YbLO2Go9AbDFlgq+RgDI0vq1KbBKhBVmVSw/Fqm1+0
y1QKVNDmEeNrTpvBfHVYUPuEnydE15Jz7rqhKFFvt+ZMa+HAkqwWOta+FJ8cGdRQ
1ascGFnUXH07dAOEBoOcJvb/zuzQ5N5pcCN18jPfEtcM/0vXRM4=
=Npui
-----END PGP SIGNATURE-----
version: 1.0.0
---
export function getCustomerInfo(id) { const db = { "C1": {name: "John", email: "j@x.com"} }; return db[id] || "Not found"; }
