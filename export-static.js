// export-static.js
const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs-extra');
const globby = require('globby');
const puppeteer = require('puppeteer');

const DOC_ROOT = path.resolve(__dirname);       // index.html 所在目录
const PORT = 4000;
const DIST = path.join(__dirname, '_site');     // 输出目录

(async () => {
  // 1️⃣ 启动 docsify 本地服务器
  const server = spawn('npx', ['docsify-cli', 'serve', DOC_ROOT, '-p', PORT], { stdio: 'inherit' });

  // 等待端口就绪
  await new Promise(res => {
    const timer = setInterval(() => {
      http.get({ host: '127.0.0.1', port: PORT, path: '/' }, () => {
        clearInterval(timer); res();
      }).on('error', () => {});
    }, 300);
  });

  // 2️⃣ 收集所有 Markdown 文件
  const mdFiles = await globby(['**/*.md', '!node_modules/**', '!_*/**'], { cwd: DOC_ROOT });
  // 额外把根目录（README）和 404 也塞进去
  const routes = mdFiles.map(f => f.replace(/\\/g, '/').replace(/\.md$/, ''));

  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  // 3️⃣ 遍历每条路由并保存 HTML
  for (const r of routes) {
    const url = `http://127.0.0.1:${PORT}/#/${encodeURI(r)}`;
    await page.goto(url, { waitUntil: 'networkidle0' });
    const html = await page.evaluate(() => document.documentElement.outerHTML);

    const outDir = path.join(DIST, r);
    await fs.ensureDir(outDir);
    await fs.writeFile(path.join(outDir, 'index.html'), html);
    console.log(`✔  ${r}`);
  }

  await browser.close();
  server.kill();

  // 4️⃣ 复制静态资源（图片 / CSS / JS）
  await fs.copy(path.join(DOC_ROOT, 'img'), path.join(DIST, 'img')).catch(() => {});
  await fs.copy(path.join(DOC_ROOT, 'lib'), path.join(DIST, 'lib')).catch(() => {});
  console.log(`\n✅  All done! Static site in ${DIST}\n`);
})();
