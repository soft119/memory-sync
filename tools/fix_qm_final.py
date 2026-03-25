# -*- coding: utf-8 -*-

file_path = r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

with open(file_path, 'w', encoding='gbk') as f:
    f.write(content)

print('已转为GBK编码')

# 验证
with open(file_path, 'rb') as f:
    raw = f.read()
    text = raw.decode('gbk')
    print()
    print('=== 验证内容 ===')
    print(text)
