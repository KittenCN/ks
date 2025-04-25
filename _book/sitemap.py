#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xml.etree.ElementTree as ET

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

def create_sitemap(directory, base_url, extensions):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                url = ET.SubElement(urlset, "url")
                loc = ET.SubElement(url, "loc")

                # 生成文件的完整URL并去掉扩展名
                file_url = os.path.join(subdir, os.path.splitext(file)[0]).replace("\\", "/")
                loc.text = base_url + file_url[len(directory):]

    indent(urlset)

    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)

directory_path = './'
base_url = 'https://wiki.coderfan.com/#/'
extensions = ['.html', '.htm', '.md', '.php']
create_sitemap(directory_path, base_url, extensions)
