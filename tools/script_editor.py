#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
996PC 引擎脚本编辑器
用于编辑 ANSI/GBK 编码的 .txt 脚本文件
支持：查找标签、删除行、替换内容、插入代码等常用操作
"""

import os
import sys
from pathlib import Path

# GBK 编码别名（ANSI 在中文 Windows 上就是 GBK）
ENCODING = 'gbk'

def read_script(filepath):
    """读取脚本文件，返回行列表（保留换行符）"""
    try:
        with open(filepath, 'r', encoding=ENCODING) as f:
            return f.readlines()
    except FileNotFoundError:
        print(f'❌ 错误：文件不存在 - {filepath}')
        sys.exit(1)
    except UnicodeDecodeError:
        print(f'❌ 错误：编码问题，请确认文件是 ANSI/GBK 格式')
        sys.exit(1)

def write_script(filepath, lines):
    """写入脚本文件（ANSI/GBK 编码）"""
    try:
        with open(filepath, 'w', encoding=ENCODING) as f:
            f.writelines(lines)
        print(f'✅ 成功保存：{filepath}')
    except Exception as e:
        print(f'❌ 写入失败：{e}')
        sys.exit(1)

def find_label_lines(lines, label):
    """查找标签位置，返回 (起始行索引，结束行索引)"""
    start = None
    for i, line in enumerate(lines):
        if f'[{label}]' in line:
            start = i
            # 找下一段开始或文件末尾
            end = len(lines)
            for j in range(i + 1, len(lines)):
                stripped = lines[j].strip()
                # 遇到下一个标签（以 [@ 开头）
                if stripped.startswith('[@') or stripped.startswith('#['):
                    end = j
                    break
                # 遇到大段注释分隔符
                if stripped.startswith(';--') and '---' in stripped:
                    end = j
                    break
            return start, end
    return None, None

def show_lines(lines, start=None, end=None):
    """显示指定范围的行（带行号）"""
    if start is None:
        start = 0
    if end is None or end > len(lines):
        end = min(len(lines), start + 30)
    
    for i in range(start, end):
        print(f'{i+1:4}: {lines[i]!r}')

def delete_lines_script(filepath, label, keep_first=2, keep_last=3):
    """
    删除标签内的某些行（保留开头和结尾）
    
    Args:
        filepath: 脚本文件路径
        label: 标签名称，如 'OnKillMob'
        keep_first: 保留开头的行数（通常保留标签 + 空行 = 2）
        keep_last: 保留结尾的行数（逻辑代码部分）
    """
    lines = read_script(filepath)
    
    start, end = find_label_lines(lines, label)
    if start is None:
        print(f'❌ 未找到标签：[{label}]')
        return False
    
    print(f'📍 找到标签 [{label}] 在第 {start+1} - {end} 行')
    print('\n修改前:')
    show_lines(lines, start, end)
    
    # 计算要删除的行范围
    delete_start = start + keep_first
    delete_end = end - keep_last
    
    if delete_start >= delete_end:
        print('⚠️  没有需要删除的内容')
        return False
    
    print(f'\n🗑️  将删除第 {delete_start+1} - {delete_end} 行')
    
    # 删除行
    new_lines = lines[:delete_start] + lines[delete_end:]
    
    print('\n修改后:')
    show_lines(new_lines, start, min(end - (delete_end - delete_start), len(new_lines)))
    
    confirm = input('\n确认保存？(y/n): ').strip().lower()
    if confirm == 'y':
        write_script(filepath, new_lines)
        return True
    else:
        print('❌ 取消保存')
        return False

def replace_content_script(filepath, old_text, new_text):
    """替换文件中的内容（精确匹配）"""
    lines = read_script(filepath)
    content = ''.join(lines)
    
    if old_text not in content:
        print(f'❌ 未找到要替换的内容')
        return False
    
    new_content = content.replace(old_text, new_text, 1)  # 只替换第一个匹配
    new_lines = new_content.splitlines(keepends=True)
    if not new_lines[-1].endswith('\n') and content.endswith('\n'):
        new_lines[-1] += '\n'
    
    write_script(filepath, new_lines)
    return True

def insert_after_line(filepath, line_num, text):
    """在指定行号后插入文本（多行）"""
    lines = read_script(filepath)
    
    if line_num < 1 or line_num > len(lines):
        print(f'❌ 无效的行号：{line_num} (文件共 {len(lines)} 行)')
        return False
    
    # 确保文本以换行结尾
    if not text.endswith('\n'):
        text += '\n'
    
    new_lines = lines[:line_num] + [text] + lines[line_num:]
    write_script(filepath, new_lines)
    print(f'✅ 在第 {line_num} 行后插入内容')
    return True

def show_help():
    """显示帮助信息"""
    help_text = """
📝 996PC 引擎脚本编辑器
=======================

用法：python script_editor.py <命令> [参数]

可用命令:
---------
1. view <文件路径> [标签名]     - 查看文件或特定标签内容
   例：python script_editor.py view QFunction-0.txt OnKillMob

2. delete-inner <文件路径> <标签名> <保留开头行数> <保留结尾行数>
    - 删除标签内部的内容（保留首尾）
   例：python script_editor.py delete-inner QFunction-0.txt OnKillMob 2 15

3. replace <文件路径> "旧内容" "新内容"
    - 替换文本（精确匹配，只替换第一个）
   例：python script_editor.py replace test.txt "old text" "new text"

4. insert-after <文件路径> <行号> "要插入的内容"
    - 在指定行后插入内容
   例：python script_editor.py insert-after test.txt 10 "; 新注释\n"

5. delete-lines <文件路径> <起始行> <结束行>
    - 删除指定范围的行
   例：python script_editor.py delete-lines test.txt 25 35

6. find <文件路径> <搜索文本>
    - 查找包含特定文本的行
   例：python script_editor.py find QFunction-0.txt OnKillMob

注意事项:
---------
- 所有操作都针对 ANSI/GBK 编码的文件
- delete-inner 和 replace 会先显示预览，需要确认才保存
- 行号从 1 开始计数
"""
    print(help_text)

def find_text_in_file(filepath, search_text):
    """在文件中查找包含特定文本的行"""
    lines = read_script(filepath)
    found = False
    for i, line in enumerate(lines):
        if search_text in line:
            print(f'第 {i+1} 行：{line.rstrip()!r}')
            found = True
    if not found:
        print('❌ 未找到匹配内容')
    return found

def delete_lines_range(filepath, start_line, end_line):
    """删除指定范围的行（1-based）"""
    lines = read_script(filepath)
    
    if start_line < 1 or end_line > len(lines) or start_line > end_line:
        print(f'❌ 无效的行号范围：{start_line}-{end_line} (文件共 {len(lines)} 行)')
        return False
    
    print(f'📍 将删除第 {start_line} - {end_line} 行')
    print('\n删除前:')
    show_lines(lines, start_line-1, end_line)
    
    new_lines = lines[:start_line-1] + lines[end_line:]
    
    print(f'\n✅ 将保留 {len(new_lines)} 行')
    
    confirm = input('确认删除？(y/n): ').strip().lower()
    if confirm == 'y':
        write_script(filepath, new_lines)
        return True
    else:
        print('❌ 取消操作')
        return False

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        return
    
    command = sys.argv[1]
    
    # 解析工作目录（支持相对路径）
    work_dir = Path('D:/MirServer/Mir200/Envir/Market_Def')
    
    if command == 'view':
        if len(sys.argv) < 3:
            print('❌ 请指定文件路径')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        lines = read_script(str(filepath))
        print(f'📄 {filepath} (共 {len(lines)} 行)\n')
        
        if len(sys.argv) >= 4:
            # 查看特定标签
            label = sys.argv[3]
            start, end = find_label_lines(lines, label)
            if start is not None:
                print(f'📍 [{label}] 在第 {start+1}-{end} 行:\n')
                show_lines(lines, start, end)
            else:
                print(f'❌ 未找到标签：[{label}]')
        else:
            # 显示前 50 行
            show_lines(lines, 0, min(50, len(lines)))
    
    elif command == 'delete-inner':
        if len(sys.argv) < 6:
            print('❌ 用法：delete-inner <文件> <标签> <保留开头> <保留结尾>')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        label = sys.argv[3]
        keep_first = int(sys.argv[4])
        keep_last = int(sys.argv[5])
        delete_lines_script(str(filepath), label, keep_first, keep_last)
    
    elif command == 'replace':
        if len(sys.argv) < 6:
            print('❌ 用法：replace <文件> "旧内容" "新内容"')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        old_text = sys.argv[3]
        new_text = ' '.join(sys.argv[4:])  # 支持空格
        replace_content_script(str(filepath), old_text, new_text)
    
    elif command == 'insert-after':
        if len(sys.argv) < 5:
            print('❌ 用法：insert-after <文件> <行号> "内容"')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        line_num = int(sys.argv[3])
        text = ' '.join(sys.argv[4:])
        insert_after_line(str(filepath), line_num, text)
    
    elif command == 'delete-lines':
        if len(sys.argv) < 5:
            print('❌ 用法：delete-lines <文件> <起始行> <结束行>')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        start_line = int(sys.argv[3])
        end_line = int(sys.argv[4])
        delete_lines_range(str(filepath), start_line, end_line)
    
    elif command == 'find':
        if len(sys.argv) < 4:
            print('❌ 用法：find <文件> "搜索文本"')
            return
        filepath = sys.argv[2]
        if not os.path.isabs(filepath):
            filepath = work_dir / filepath
        search_text = sys.argv[3]
        find_text_in_file(str(filepath), search_text)
    
    else:
        print(f'❌ 未知命令：{command}')
        show_help()

if __name__ == '__main__':
    main()
