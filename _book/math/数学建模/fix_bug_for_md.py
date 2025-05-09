import re
from pathlib import Path

def fix_mathop_nolimits_in_latex(md_root: Path):
    modified_files = []

    for md_file in md_root.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # 匹配形如 e\mathop{}\nolimits^{...} 的结构，并替换为 e^{...}
            def mathop_replacer(match):
                base = match.group(1)
                exponent = match.group(2)
                return f"{base}^{{{exponent}}}"

            content = re.sub(
                r'(\b\w)\s*\\mathop\{\}\s*\\nolimits\^\s*\{(.*?)\}',
                mathop_replacer,
                content
            )

            if content != original_content:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(content)
                modified_files.append(md_file)

        except Exception as e:
            print(f"⚠️ Failed to process {md_file}: {e}")

    return modified_files

# 扫描并修复当前目录及子目录下的 .md 文件
current_dir = Path(".").resolve()
fixed_files = fix_mathop_nolimits_in_latex(current_dir)