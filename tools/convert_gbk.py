"""
convert_gbk.py - 996PC引擎脚本文件UTF-8转GBK工具
使用方法: python convert_gbk.py <文件路径>
"""

import os
import sys

def convert_to_gbk(file_path):
    """将文件从UTF-8转换为GBK编码"""
    try:
        # 备份原文件
        backup_path = file_path + '.utf8_backup'
        if os.path.exists(file_path):
            import shutil
            shutil.copy2(file_path, backup_path)
        
        # 先尝试用UTF-8读取
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 用GBK写入（使用Windows换行符）
        with open(file_path, 'w', encoding='gbk', newline='\r\n') as f:
            f.write(content)
        
        print(f'✓ 转换成功: {os.path.basename(file_path)} (已备份到{os.path.basename(backup_path)})')
        return True
    except Exception as e:
        print(f'✗ 转换失败 {file_path}: {e}')
        return False

def convert_directory(dir_path):
    """转换目录下所有.txt文件"""
    if not os.path.exists(dir_path):
        print(f'目录不存在: {dir_path}')
        return
    
    converted = 0
    failed = 0
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                if convert_to_gbk(file_path):
                    converted += 1
                else:
                    failed += 1
    
    print(f'\n转换完成: 成功 {converted} 个文件，失败 {failed} 个文件')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target) and target.lower().endswith('.txt'):
            convert_to_gbk(target)
        elif os.path.isdir(target):
            convert_directory(target)
        else:
            print(f'无效路径: {target}')
            print('请提供.txt文件路径或目录路径')
    else:
        print('996PC引擎脚本文件UTF-8转GBK工具')
        print('=' * 50)
        print('用法:')
        print('  python convert_gbk.py <文件路径>    # 转换单个文件')
        print('  python convert_gbk.py <目录路径>    # 转换目录下所有.txt文件')
        print('\n示例:')
        print('  python convert_gbk.py "D:\\MirServer\\Mir200\\Envir\\Market_Def\\QFunction-0.txt"')
        print('  python convert_gbk.py "D:\\MirServer\\Mir200\\Envir\\QuestDiary"')