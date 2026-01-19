---
id: anthropic.calculator
spdx-id: MIT
origin: https://github.com/anthropics/anthropic-cookbook
hash: sha256:917ef6c93a50ef027f2ab913910110ab4a579620807c15db149bfe3b20158407
version: 1.0.0
signature: |
    -----BEGIN PGP SIGNATURE-----
    
    iQIzBAABCgAdFiEEZ8U4LAM6MxGSR9xCicnEBsaHU18FAmlq+Z4ACgkQicnEBsaH
    U1+h1A/7BNmcrvUQw8uH5cXtS/yNlZQz0y/QCKy8Fxy1f5oqgtuTJFIngYUJQGP5
    dy0FPwJfFCBBp71RV89sPaDsPbkyd0k/bFJN011Sbp/T/V1hK8ioDkFBi+8JRkOv
    g/fJeESPhawRHRyiq2biNNhgUXa24nCr9uoibUsrTt1bAeWvVBPgWHvrtaIP5FwS
    3NnSoylwN8TBPOwpyyAeWz7YsuIwyCFtRg8o1AvlSqtl9wTJAZ49Kg172a63skFw
    6oKrXo1RgsFCPHK2u0yJ2Glo3POa9embBqiJFSwBlYfmea4JVndfSNCodJnkPhfl
    9zHThOHv/8LeOUpJbLHo9bNbzoQUtMQUCUX5IxQSY/iqrcA3IuP+Ju6Im1XXNqoO
    KLkR7rbJas6KvMMQdbL5PBLfuTf3O9s8M42UBXZjP0uPYxCWCyxETOMMXV7pLZ8+
    zMom8oBEVdzLc1t4LYgpGt71s5Ox7IXPJm8psjnTmrNha0nMUM2ExwwHkVEH4+LJ
    3Dhh/9Tl1zZbPgkDvTHmTyfy/xLKqqkG6m1Z/3UUXTUMzWH2tSwVkA0bEXqLL9L+
    +mhZanSdxi9TMAKDQM1AukQaF/KFzndGpI34bVaFM7Hhb0mJNcly+PBowpXMIaVT
    piwUBLrO9MxTZIoMYw7Y99+N/ZLWZocIlaxHLdRPWZM1oOMOKII=
    =6u7d
    -----END PGP SIGNATURE-----

---
export function calculate(expr) { try { return eval(expr.replace(/[^0-9+\-*/().]/g, '')); } catch { return 'Error'; } }
