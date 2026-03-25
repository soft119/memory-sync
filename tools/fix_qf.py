#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复QFunction-0.txt文件的编码问题
"""
import re
import os

qf_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

# 读取原始字节
with open(qf_path, 'rb') as f:
    raw = f.read()

# 尝试多种编码解码
text = None
for encoding in ['gbk', 'gb2312', 'utf-8', 'latin-1']:
    try:
        text = raw.decode(encoding)
        print(f'[OK] 使用 {encoding} 解码成功')
        break
    except:
        continue

if text is None:
    text = raw.decode('gbk', errors='replace')
    print('[WARN] 使用GBK解码（替换错误字符）')

# 检查并修复StdModeFunc100
old_pattern = r'\[@StdModeFunc100\][^\[]*'
new_func = '''[@StdModeFunc100]
#IF
#ACT
INC A500 604800
SENDMSG 6 点卡使用成功！已增加7天游戏时间！
#IF
CHECKMAPNAME 600
#ACT
MAPMOVE 3 330 330
SENDMSG 6 已自动传送回安全区！

'''

# 检查是否已存在正确的StdModeFunc100
if '[@StdModeFunc100]' in text:
    # 替换现有的
    text = re.sub(old_pattern, new_func, text)
    print('[OK] 已替换StdModeFunc100')
else:
    # 在文件末尾添加
    text = text.rstrip() + '\n\n' + new_func
    print('[OK] 已添加StdModeFunc100')

# 写回GBK编码
with open(qf_path, 'w', encoding='gbk') as f:
    f.write(text)

print('[DONE] QFunction-0.txt 已修复为GBK编码')
