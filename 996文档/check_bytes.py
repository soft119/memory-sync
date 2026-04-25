f = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
with open(f, 'rb') as fp:
    raw = fp.read()

# 查找充值后调试行
idx = raw.find(b'\xb3\xcc\xb1\xd9\xba\xcf')
if idx != -1:
    print('充值后周围:')
    print(raw[idx:idx+80])
else:
    print('未找到充值后')

# 查找$符号
dollar_count = raw.count(b'$')
print('\n文件中$符号数量:', dollar_count)

# 查找SENDMSG
idx = raw.find(b'SENDMSG')
while idx != -1:
    print('\nSENDMSG位置:', idx)
    print('周围:', raw[idx:idx+60])
    idx = raw.find(b'SENDMSG', idx + 1)
