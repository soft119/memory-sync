# -*- coding: utf-8 -*-
import os

file_path = r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt'

with open(file_path, 'rb') as f:
    content = f.read()

print('File size:', len(content), 'bytes')
print('Contains CR+LF:', content.count(b'\r\n'))

if b'\r\n' in content:
    lines = content.split(b'\r\n')
    print('Total lines:', len(lines))
    
    # 查找关键行
    print('\n--- StdModeFunc 相关行 ---')
    for i, line in enumerate(lines):
        if b'LOADVAR' in line and b'xb5\xe3\xbf\xa8' in line:  # 点卡
            print(f'{i+1}: {line}')
        if b'VAR Integer HUMAN' in line:
            print(f'{i+1}: {line}')
        if b'CHECKVAR HUMAN' in line:
            print(f'{i+1}: {line}')