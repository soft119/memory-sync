f = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
with open(f, 'rb') as fp:
    raw = fp.read()
content = raw.decode('gbk', errors='ignore')

# 找到[@StdModeFunc100]
idx = content.find('[@StdModeFunc100]')
if idx == -1:
    print('未找到[@StdModeFunc100]')
    exit()

# 找到下一个[@
next_idx = content.find('\n[@', idx + 20)
if next_idx == -1:
    next_idx = len(content)

# 新的正确内容（使用正确的换行符）
new_section = '''[@StdModeFunc100]
#IF
#ACT
TAKE 7天点卡 1
VAR Integer HUMAN 点卡时间
LOADVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
CALCVAR HUMAN 点卡时间 + 604800
SAVEVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
SENDMSG 6 点卡使用成功！已增加7天游戏时间！

'''

# 替换
content = content[:idx] + new_section + content[next_idx:]

with open(f, 'w', encoding='gbk') as fp:
    fp.write(content)

print('已修复')

# 验证
with open(f, 'rb') as fp:
    raw = fp.read()
content2 = raw.decode('gbk', errors='ignore')
idx2 = content2.find('[@StdModeFunc100]')
print(content2[idx2:idx2+300])
