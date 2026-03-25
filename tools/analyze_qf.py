# -*- coding: utf-8 -*-
import os

file_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

with open(file_path, 'rb') as f:
    content = f.read()

# 统计实际字符
print('File size:', len(content), 'bytes')
print('Contains 0x0d (CR):', content.count(b'\r'))
print('Contains 0x0a (LF):', content.count(b'\n'))

# 尝试不同的分割方式
if b'\r\n' in content:
    lines = content.split(b'\r\n')
    print('Split by \\r\\n:', len(lines), 'lines')
elif b'\n' in content:
    lines = content.split(b'\n')
    print('Split by \\n:', len(lines), 'lines')
else:
    print('File has no line breaks!')
    lines = [content]

# 检查前200个字符
print('\nFirst 200 bytes:')
for i, b in enumerate(content[:200]):
    if b == 0x0d:
        print(f'[{i}] CR')
    elif b == 0x0a:
        print(f'[{i}] LF')
    elif 32 <= b < 127:
        print(f'[{i}] {chr(b)}', end=' ')
    else:
        print(f'[{i}] 0x{b:02x}', end=' ')
    if (i + 1) % 20 == 0:
        print()