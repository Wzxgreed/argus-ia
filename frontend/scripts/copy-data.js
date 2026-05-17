const fs = require("fs");
const path = require("path");

const srcDir = path.resolve(__dirname, "../../data");
const destDir = path.resolve(__dirname, "../dist/data");

if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

const files = fs.readdirSync(srcDir).filter((f) => f.endsWith("_latest.json"));
for (const file of files) {
  fs.copyFileSync(path.join(srcDir, file), path.join(destDir, file));
  console.log(`✓ Copied ${file}`);
}

console.log(`Done — ${files.length} files copied to dist/data/`);
