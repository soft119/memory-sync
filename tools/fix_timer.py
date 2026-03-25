# -*- coding: utf-8 -*-
# 修改QManage.txt的定时器部分

# 读取文件
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    text = f.read()

# 旧的定时器部分（根据实际内容）
old_timer = '''[@OnTimer50]
#IF
#ACT
MOV N1 0
MOV N1 <$STR(A500)>

; 如果时间>3600秒，扣减
#IF
LARGE N1 3600
#ACT
DEC A500 3600
SENDMSG 6 点卡时间已扣除1小时，剩余时间：<$STR(A500)>秒
#ELSEACT
; 时间不足1小时，清零传送
MOV A500 0
MAPMOVE 600 20 20
SENDMSG 5 您的游戏时间已用完，请充值后使用点卡续费！'''

# 新的定时器部分
new_timer = '''[@OnTimer50]
#IF
#ACT
; 读取点卡时间
VAR Integer HUMAN 点卡时间
LOADVAR HUMAN 点卡时间 QuestDiary\\系统功能\\点卡时间.txt

; 检测剩余时间是否大于1小时(3600秒)
#IF
CHECKVAR HUMAN 点卡时间 > 3600
#ACT
; 扣除1小时
CALCVAR HUMAN 点卡时间 - 3600
SAVEVAR HUMAN 点卡时间 QuestDiary\\系统功能\\点卡时间.txt
SENDMSG 6 点卡时间扣除1小时，剩余：<$HUMAN(点卡时间)>秒
#ELSEACT
; 时间不足1小时，清零并传送欠费区
CALCVAR HUMAN 点卡时间 = 0
SAVEVAR HUMAN 点卡时间 QuestDiary\\系统功能\\点卡时间.txt
MAPMOVE 600 20 20
SENDMSG 5 您的游戏时间已用完！'''

if old_timer in text:
    text = text.replace(old_timer, new_timer)
    print("找到并替换定时器部分成功")
else:
    print("未找到原始定时器内容")

# 写回
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'w', encoding='gbk') as f:
    f.write(text)

print("文件已保存")

# 验证
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    verify = f.read()

idx = verify.find('[@OnTimer50]')
if idx >= 0:
    end_idx = verify.find('[@', idx + 5)
    if end_idx < 0:
        end_idx = min(idx + 600, len(verify))
    print()
    print("验证定时器部分:")
    print(verify[idx:end_idx])
