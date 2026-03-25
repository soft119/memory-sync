file_path = r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt'

with open(file_path, 'rb') as f:
    content = f.read()

# 修复被破坏的变量
# <\> -> <$USERNAME>
content = content.replace(bytes([0x3c, 0x5c, 0x3e]), b'<$USERNAME>')
# <$HUMAN 
content = content.replace(b'<\\$HUMAN', b'<$HUMAN')
# <$STR
content = content.replace(b'<\\$STR', b'<$STR')

with open(file_path, 'wb') as f:
    f.write(content)

print('已修复QManage.txt')

# 验证
with open(file_path, 'rb') as f:
    verify = f.read().decode('gbk')
print()
print('=== 验证内容 ===')
print(verify)
