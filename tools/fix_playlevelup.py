# -*- coding: gbk -*-
import re

filepath = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

# Read with GBK encoding
with open(filepath, 'r', encoding='gbk', errors='ignore') as f:
    content = f.read()

# Show lines around line 70-90 to understand the structure
lines = content.split('\n')
print(f"Total lines: {len(lines)}")
print("\nLines 70-90:")
for i in range(69, 91):
    if i < len(lines):
        line = lines[i]
        print(f"{i+1}: {repr(line)}")