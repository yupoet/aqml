import { readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const extensionDir = resolve(scriptDir, "..");
const repoDir = resolve(extensionDir, "..", "..");
const source = join(repoDir, "spec", "schema.json");
const target = join(extensionDir, "schema", "aqml.schema.json");

const sourceText = readFileSync(source, "utf-8");
const targetText = readFileSync(target, "utf-8");

if (sourceText !== targetText) {
  console.error("AQML schema copy is stale. Run `npm run sync:schema` in editors/vscode.");
  process.exit(1);
}

console.log("AQML schema copy is up to date.");
