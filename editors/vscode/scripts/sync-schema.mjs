import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const extensionDir = resolve(scriptDir, "..");
const repoDir = resolve(extensionDir, "..", "..");
const source = join(repoDir, "spec", "schema.json");
const targetDir = join(extensionDir, "schema");
const target = join(targetDir, "aqml.schema.json");

mkdirSync(targetDir, { recursive: true });
copyFileSync(source, target);

console.log(`Synced AQML schema: ${source} -> ${target}`);
