f = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
with open(f, 'rb') as fp:
    raw = fp.read()

# 再次检查是否还有问题
search = b'<$(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>'
idx = raw.find(search)
if idx != -1:
    print('还有问题:', idx)
    # 替换
    correct = b'<$HUMAN(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>'
    raw = raw.replace(search, correct)
    with open(f, 'wb') as fp:
        fp.write(raw)
    print('已修复')
else:
    print('已无问题字符串')

# 验证
with open(f, 'rb') as fp:
    raw = fp.read()

# 查找调试行
idx = raw.find(b'\xb5\xf7\xca\xd4')
if idx != -1:
    print('\n调试行内容:', raw[idx:idx+80])
