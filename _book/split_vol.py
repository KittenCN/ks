# -*- coding: utf-8 -*-
import os
import shutil
import re
import argparse
from pathlib import Path

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, default='.', help='指定目录，默认为当前目录')
args = parser.parse_args()

def safe_filename(name: str):
    return re.sub(r'[<>:"/\\|?*]', '_', name).replace(' ', '_').rstrip(' .') or '_'

if args.directory != '.':
    os.chdir(args.directory)  # 切换到指定目录
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 切换到脚本所在目录

# 读取 SUMMARY.md 文件内容，确保使用 UTF-8 编码来支持中文
summary_path = Path('SUMMARY.md')
if not summary_path.exists():
    print("错误：未找到 SUMMARY.md 文件")
    exit(1)

try:
    with open(summary_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except Exception as e:
    print(f"错误：无法读取 SUMMARY.md 文件: {e}")
    exit(1)

# 用于非法文件名字符的模式，Windows 不允许以下字符&#8203;:contentReference[oaicite:3]{index=3}
# illegal_pattern = re.compile(r'[<>:"/\\|?*]')  # 替换为下划线的字符: < > : " / \ | ? *
# 初始化变量
books = []                # 存储所有书籍的信息
collection_line = None    # 合集名（第一级）的行内容
book_indent = None        # 书名行(第二级)的缩进空格数
current_book = None

for line in lines:
    # 去除行末换行符，但保留行首缩进用于判断层级
    raw_line = line.rstrip('\n')
    if not raw_line.strip():
        continue  # 跳过空行
    indent = len(raw_line) - len(raw_line.lstrip(' '))
    stripped = raw_line.lstrip()
    # 检查是否为列表项（以“-”开头）
    if not stripped.startswith('-'):
        continue  # 非列表项行（不在列表结构中），跳过
    # 使用正则解析列表项格式 "- [标题](链接)"
    match = re.match(r'-\s*\[([^\]]+)\]\(([^)]+)\)', stripped)
    if not match:
        continue  # 格式不符合预期，跳过
    title = match.group(1).strip()
    link = match.group(2).strip()
    # 判断层级：根据缩进确定合集、书名或章节
    if collection_line is None:
        # 第一项默认为合集名（第一级）
        collection_line = line  # 保留合集名整行（含换行符）
        continue
    if book_indent is None or indent == book_indent:
        # 书名级别（第二级）列表项
        if book_indent is None:
            book_indent = indent  # 记录书名层级的缩进
        # 遇到新书，初始化书籍信息
        safe_name = safe_filename(title)  # 替换非法字符为下划线&#8203;:contentReference[oaicite:4]{index=4}    
        # safe_name = illegal_pattern.sub('_', title)       # 替换非法字符为下划线&#8203;:contentReference[oaicite:4]{index=4}
        # safe_name = safe_name.rstrip(' .')                # 去除末尾的空格或点&#8203;:contentReference[oaicite:5]{index=5}
        if safe_name == '':
            safe_name = '_'  # 避免空文件夹名
        current_book = {
            "name": title,
            "safe_name": safe_name,
            "main_file": link,
            "chapters": []
        }
        books.append(current_book)
    elif book_indent is not None and indent > book_indent:
        # 章节级别（第三级）列表项
        if current_book is None:
            continue  # 安全判断
        current_book["chapters"].append({
            "title": title,
            "file": link
        })

# 按照解析结果创建文件夹、移动文件和生成书内 SUMMARY.md
for book in books:
    book_name = book["name"]
    folder_name = book["safe_name"]
    main_file = book["main_file"]
    chapters = book["chapters"]
    folder_path = Path(folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)  # 创建书籍文件夹
    except Exception as e:
        print(f"警告：无法创建文件夹 {folder_name}: {e}")
        continue
    # 尝试复制 book.json 到每本书目录
    book_json_src = Path("book.json")
    if book_json_src.exists():
        try:
            shutil.copy(book_json_src, folder_path / "book.json")
        except Exception as e:
            print(f"警告：复制 book.json 到 {folder_path} 失败: {e}")
    else:
        print("警告：未找到 book.json，跳过复制")
    # 移动书的主文件并重命名为 README.md
    if main_file:
        src_main = Path(main_file)
        if src_main.exists():
            dest_main = folder_path / "README.md"
            try:
                if dest_main.exists():
                    dest_main.unlink()  # 删除已存在的 README.md，防止冲突
                shutil.move(str(src_main), str(dest_main))  # 移动文件&#8203;:contentReference[oaicite:6]{index=6}
            except Exception as e:
                print(f"警告：移动文件 {main_file} 到 {dest_main} 时出错: {e}")
        else:
            print(f"警告：主文件 {main_file} 不存在，跳过移动")
    # 移动所有章节文件到书籍文件夹
    moved_chapters = []
    for chap in chapters:
        src_file = Path(chap["file"])
        if not src_file.exists():
            src_file = Path(src_file.name)  # 尝试只用文件名查找    
        if not src_file.exists():
            print(f"警告：章节文件 {chap['file']} 不存在，跳过")
            continue
        dest_file = folder_path / src_file.name
        try:
            if dest_file.exists():
                dest_file.unlink()  # 删除目标处同名文件，避免冲突
            shutil.move(str(src_file), str(dest_file))
            moved_chapters.append(chap)
        except Exception as e:
            print(f"警告：移动文件 {src_file} 到 {dest_file} 时出错: {e}")
    # 在书籍文件夹内创建 SUMMARY.md 列表
    summary_lines = []
    summary_lines.append(f"- [{book_name}](README.md)\n")
    for chap in moved_chapters:
        chapter_filename = Path(chap['file']).name
        summary_lines.append(f"  - [{chap['title']}]({chapter_filename})\n")
    try:
        with open(folder_path / "SUMMARY.md", 'w', encoding='utf-8') as sf:
            sf.writelines(summary_lines)
    except Exception as e:
        print(f"警告：写入 {folder_name}/SUMMARY.md 时出错: {e}")

# 备份原始 SUMMARY.md 文件
backup_path = Path('SUMMARY_backup.md')
try:
    shutil.copyfile(summary_path, backup_path)
except Exception as e:
    print(f"警告：备份 SUMMARY.md 时出错: {e}")

# 精简并更新原始 SUMMARY.md
try:
    with open(summary_path, 'w', encoding='utf-8') as f:
        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # 跳过第三级目录（章节）
            if book_indent is not None and indent > book_indent:
                continue

            # 更新第二级链接（书名）
            match = re.match(r'-\s*\[([^\]]+)\]\(([^)]+)\)', stripped)
            if match and indent == book_indent:
                title = match.group(1).strip()
                # 查找对应的 book.safe_name
                for b in books:
                    if b['name'] == title:
                        new_link = f"{b['safe_name']}/README.md"
                        new_line = f"{' ' * indent}- [{title}]({new_link})\n"
                        f.write(new_line)
                        break
                else:
                    f.write(line)  # 没找到就原样写
            else:
                f.write(line)  # 保留合集标题或非匹配行
except Exception as e:
    print(f"警告：更新 SUMMARY.md 时出错: {e}")

