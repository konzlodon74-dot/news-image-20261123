import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// The entry image is bundled in this repository; the program simply
// places it at /output/entry.png. No network, no randomness: the same
// bytes are written on every run.
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const target = "/output/entry.png";
mkdirSync("/output", { recursive: true });
copyFileSync(source, target);
// Confirm the copy landed intact before exiting.
const written = readFileSync(target);
if (written.length !== readFileSync(source).length) {
  throw new Error("entry.png copy is incomplete");
}
console.log(`wrote ${target} (${written.length} bytes)`);
