const fs = require("fs");
const path = require("path");

const srcDir = path.resolve(__dirname, "../../data");
const destDir = path.resolve(__dirname, "../dist/data");

if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

const files = fs.readdirSync(srcDir).filter((f) =>
  f.endsWith("_latest.json") || f === "latest.json" || f.startsWith("ollama_")
);
for (const file of files) {
  const destPath = path.join(destDir, file);
  fs.copyFileSync(path.join(srcDir, file), destPath);
  fs.chmodSync(destPath, 0o644);
  console.log(`✓ Copied ${file}`);
}

// Créer dashboard.html (redirection) après chaque build
const dashboardRedirect = path.resolve(__dirname, "../dist/dashboard.html");
fs.writeFileSync(dashboardRedirect, `<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=/dashboard/" />
  <title>Redirection...</title>
</head>
<body>
  <p>Redirection vers <a href="/dashboard/">Dashboard</a>...</p>
</body>
</html>
`);
fs.chmodSync(dashboardRedirect, 0o644);
console.log("✓ Created dashboard.html redirect");

console.log(`Done — ${files.length} files copied to dist/data/`);
