import re

file_path = r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt'

with open(file_path, 'rb') as f:
    content = f.read()

# 修复 <$USERNAME>
wrong1 = bytes([0x3c, 0x5c, 0x3e])  # <\>
correct1 = b'<$USERNAME>'
content = content.replace(wrong1, correct1)

# 修复 <$HUMAN
wrong2 = b'<\$HUMAN'
correct2 = b'<$HUMAN'
content = content.replace(wrong2, correct2)

# 修复 <$STR
wrong3 = b'<\$STR'
correct3 = b'<$STR'
content = content.replace(wrong3, correct3)

with open(file_path, 'wb') as f:
    f.write(content)

print('变量名已修复')

# 验证
with open(file_path, 'rb') as f:
    verify = f.read().decode('gbk')

print()
print('=== 验证新人礼包部分 ===')
lines = verify.split('\n')
for i, line in enumerate(lines[15:40], 16):
    print(f'{i}: {line}')
