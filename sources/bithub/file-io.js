/* global Deno */
export async function readFile(path) {
 return Deno.readTextFile(path);
}
