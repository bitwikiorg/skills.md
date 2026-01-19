import js from "@eslint/js";
import frontmatter from "eslint-plugin-frontmatter";

export default [
 js.configs.recommended,
 {
 files: ["**/*.js"],
 plugins: {
 frontmatter
 },
 // The plugin exports processors with file extension keys
 processor: frontmatter.processors[".js"]
 },
 {
 ignores: ["node_modules/", "dist/"]
 }
];
