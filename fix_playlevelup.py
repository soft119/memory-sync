f = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
with open(f, 'rb') as fp:
    raw = fp.read()
content = raw.decode('gbk', errors='ignore')

# 找到[@PlayLevelUp]位置
playlevelup_idx = content.find('[@PlayLevelUp]')
if playlevelup_idx == -1:
    print('未找到[@PlayLevelUp]')
    exit()

# 找到22级点卡检测注释的开始
start_idx = content.find('; 22级点卡检测', playlevelup_idx)
if start_idx == -1:
    print('未找到22级点卡检测')
    exit()

# 找到7级技能部分（下一个技能相关注释）
end_idx = content.find('; 7级', start_idx)
if end_idx == -1:
    # 尝试其他方式找到结束
    end_idx = content.find('; #IF', start_idx + 100)
    if end_idx == -1:
        end_idx = start_idx + 800

print(f'替换范围: {start_idx} - {end_idx}')

# 新的正确内容
new_section = ''';================================================
; 22级点卡检测 - 无点卡立即传送欠费区
;================================================
#IF
CHECKLEVELEX = 22
#ACT
VAR Integer HUMAN 点卡时间
LOADVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
#IF
CHECKVAR HUMAN 点卡时间 < 1
#ACT
MAPMOVE 600 20 20
SENDMSG 5 您已达到22级，需要点卡才能继续游戏！
SENDMSG 5 请在商铺使用元宝购买点卡！
BREAK

'''

# 替换
content = content[:start_idx] + new_section + content[end_idx:]

with open(f, 'w', encoding='gbk') as fp:
    fp.write(content)

print('已修复')

# 验证
with open(f, 'rb') as fp:
    raw = fp.read()
content2 = raw.decode('gbk', errors='ignore')
idx2 = content2.find('22级点卡检测')
print('\n修复后内容:')
print(content2[idx2:idx2+600])
