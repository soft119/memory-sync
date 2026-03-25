import os

f = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
with open(f, 'rb') as fp:
    raw = fp.read()
content = raw.decode('gbk', errors='ignore')

# 修复 \( -> $(
content = content.replace('\\(点卡时间)', '$(点卡时间)')

with open(f, 'w', encoding='gbk') as fp:
    fp.write(content)
print('已修复转义')

# 验证
with open(f, 'rb') as fp:
    raw = fp.read()
content = raw.decode('gbk', errors='ignore')
idx = content.find('[@StdModeFunc100]')
print(content[idx:idx+500])
