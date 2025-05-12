#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Generate a sitemap.xml file.')
parser.add_argument('--choice', type=int, default = 1)
args = parser.parse_args()

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def create_sitemap(directory, base_url, extensions, exceptions, exceptions_dir):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                # 排除指定的文件
                if any(file.endswith(exc) for exc in exceptions):
                    continue
                # 排除目录
                if any(exc in subdir for exc in exceptions_dir):
                    continue
                url = ET.SubElement(urlset, "url")
                loc = ET.SubElement(url, "loc")

                # 生成文件的完整URL并去掉扩展名
                if args.choice == 0:
                    file_url = os.path.join(subdir, os.path.splitext(file)[0]).replace("\\", "/")
                else:
                    file_url = os.path.join(subdir, file).replace("\\", "/")
                loc.text = base_url + file_url[len(directory):]

    indent(urlset)

    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)

directory_path = './'
exceptions = ['_coverpage.md', '_navbar.md', '_sidebar.md']
# 排除目录
exceptions_dir = ['.git', 'node_modules', 'docs/.vuepress', 'docs/.vuepress/dist']
if args.choice == 0:
    base_url = 'https://demo.coderfan.com/#/'
    extensions = ['.html', '.htm', '.md']
else:
    base_url = 'https://wiki.coderfan.com/'
    extensions = ['.html', '.htm']
create_sitemap(directory_path, base_url, extensions, exceptions, exceptions_dir)
