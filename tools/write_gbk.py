# -*- coding: utf-8 -*-
"""
通用 GBK 文件写入工具
用法: python write_gbk.py "文件路径" "内容"
"""
import sys
import os

def write_gbk(file_path, content):
    """写入 GBK 编码文件"""
    # 替换转义字符
    content = content.replace('\\r\\n', '\r\n')
    content = content.replace('\\n', '\r\n')
    
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 写入文件
    with open(file_path, 'w', encoding='gbk', errors='replace') as f:
        f.write(content)
    
    return file_path

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python write_gbk.py \"file_path\" \"content\"")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = sys.argv[2]
    
    result = write_gbk(file_path, content)
    print(f"OK: {result}")