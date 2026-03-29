# -*- coding: utf-8 -*-
"""
提取 996PC 引擎文档中的关键知识点（简化版）
"""
import os
import re
from pathlib import Path

def extract_text_from_htm(file_path):
    """从 HTM 文件提取纯文本（简单版）"""
    try:
        with open(file_path, 'r', encoding='gbk', errors='ignore') as f:
            content = f.read()
        
        # 移除 HTML 标签
        text = re.sub(r'<[^>]+>', ' ', content)
        
        # 移除多余空白
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    except Exception as e:
        return ""

def extract_commands(text):
    """从文本中提取命令"""
    # 匹配大写字母组成的命令（至少3个字符）
    commands = re.findall(r'\b([A-Z][A-Z][A-Z]+)\b', text)
    return set(cmd for cmd in commands if 3 <= len(cmd) <= 20)

def main():
    base_dir = r'D:\MirServer\chm_extract\游戏引擎反外挂系统'
    
    all_commands = set()
    file_count = 0
    
    # 遍历所有 HTM 文件
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.htm', '.html')):
                file_path = os.path.join(root, file)
                text = extract_text_from_htm(file_path)
                commands = extract_commands(text)
                all_commands.update(commands)
                file_count += 1
    
    # 过滤并排序
    valid_commands = sorted(cmd for cmd in all_commands if len(cmd) >= 3)
    
    print(f'处理了 {file_count} 个文件')
    print(f'找到 {len(valid_commands)} 个命令')
    
    # 保存命令列表
    output_file = r'D:\MirServer\tools\engine_commands.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for cmd in valid_commands:
            f.write(cmd + '\n')
    
    print(f'命令列表已保存到: {output_file}')
    
    # 显示前50个命令作为示例
    print('\n前50个命令示例:')
    for cmd in valid_commands[:50]:
        print(f'  - {cmd}')

if __name__ == '__main__':
    main()