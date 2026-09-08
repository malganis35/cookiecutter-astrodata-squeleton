#!/usr/bin/env node
// PostToolUse(Write|Edit): formate le fichier Python qui vient d'être modifié.
const fs = require("fs");
const { execSync } = require("child_process");

let data = {};
try {
  data = JSON.parse(fs.readFileSync(0, "utf8") || "{}");
} catch {}

const file = data.tool_input?.file_path || "";
if (!/\.py$/.test(file) || !fs.existsSync(file)) process.exit(0);

try {
  execSync(`uv run ruff check --fix --quiet "${file}"`, { stdio: "ignore" });
  execSync(`uv run ruff format --quiet "${file}"`, { stdio: "ignore" });
  console.log(`ruff: ${file} formaté`);
} catch {
  console.error(`ruff: échec sur ${file} (lint non bloquant)`);
}
process.exit(0);
