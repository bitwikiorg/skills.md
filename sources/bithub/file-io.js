---
id: bithub.file-io
spdx-id: Apache-2.0
origin: https://github.com/bitcoreos/skills.md
hash: sha256:ba2660d75865f45d5c5cc63b36ac48a0146350fe43657c607651fa8216619d15
version: 1.0.0
---
export async function readFile(path) {
  return Deno.readTextFile(path);
}
