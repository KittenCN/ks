module.exports = {
    hooks: {
      // 在每本书初始化时注入 markdown-it 插件
      init: function () {
        const md = this.getMarkdownEngine();          // HonKit 的 markdown-it 实例
        const mathjax = require('markdown-it-mathjax3');
        md.use(mathjax, {
          tex: {
            inlineMath:  [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']],
            processEscapes: true,
            processEnvironments: true,
            strict: 'warn'
          }
        });
      }
    }
  };
  