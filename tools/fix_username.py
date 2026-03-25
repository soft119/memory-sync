# -*- coding: utf-8 -*-
import os

file_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

with open(file_path, 'rb') as f:
    content = f.read()

# 错误的变量 <\> (实际是 <反斜杠>)
wrong = bytes([0x3c, 0x5c, 0x3e])  # <\>
# 正确的变量 <$USERNAME>
correct = b'<$USERNAME>'

print(f'查找字节: {wrong}')
print(f'替换字节: {correct}')
print(f'文件大小: {len(content)}')
print(f'是否包含错误变量: {wrong in content}')

# 替换
content = content.replace(wrong, correct)

with open(file_path, 'wb') as f:
    f.write(content)

print('替换完成')

# 验证
with open(file_path, 'rb') as f:
    raw = f.read()

print(f'替换后是否还有错误: {wrong in raw}')
print(f'替换后是否包含正确: {correct in raw}')

# 找到7级部分验证
idx = raw.find(b'ADDSKILL')
if idx > 0:
    snippet = raw[idx:idx+150]
    print('\n验证内容:')
    print(snippet.decode('gbk'))
