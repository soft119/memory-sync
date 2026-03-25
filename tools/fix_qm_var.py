# -*- coding: utf-8 -*-
# 修改QManage.txt使用自定义变量

# 读取文件
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    text = f.read()

# 旧的登录检测部分
old_part = ''';================================================
; 点卡系统 - 登录检测
; A500 = 点卡剩余秒数
;================================================

; 先设置N1为0，再尝试把A500的值赋给N1
#IF
#ACT
MOV N1 0
MOV N1 <$STR(A500)>

; N1=0表示A500为空或0，N1>0表示有时间
#IF
EQUAL N1 0
#ACT
MAPMOVE 600 20 20
SENDMSG 5 您的游戏时间已用完，请充值后使用点卡续费！
BREAK

; 有游戏时间
#IF
#ACT
; 计算天数
DIV N2 <$STR(A500)> 86400
SENDMSG 6 您好！当前剩余游戏时间：<$STR(A500)>秒（约<$STR(N2)>天）
SETONTIMER 50 3600'''

# 新的登录检测部分
new_part = ''';================================================
; 点卡系统 - 登录检测
; 使用自定义变量存储点卡时间
;================================================

; 声明并读取点卡时间变量
#IF
#ACT
VAR Integer HUMAN 点卡时间
LOADVAR HUMAN 点卡时间 QuestDiary\\系统功能\\点卡时间.txt

; 检测是否有游戏时间
#IF
CHECKVAR HUMAN 点卡时间 < 1
#ACT
MAPMOVE 600 20 20
SENDMSG 5 您的游戏时间已用完，请充值后使用点卡续费！
BREAK

; 有游戏时间，显示剩余时间
#IF
#ACT
; 计算天数
DIV N2 <$HUMAN(点卡时间)> 86400
SENDMSG 6 您好！当前剩余游戏时间：<$HUMAN(点卡时间)>秒（约<$STR(N2)>天）
SETONTIMER 50 3600'''

if old_part in text:
    text = text.replace(old_part, new_part)
    print("找到并替换成功")
else:
    print("未找到原始内容")

# 写回
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'w', encoding='gbk') as f:
    f.write(text)

print("文件已保存")

# 验证
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    verify = f.read()

idx = verify.find('; 点卡系统 - 登录检测')
if idx >= 0:
    end_idx = verify.find(';===========', idx + 50)
    if end_idx < 0:
        end_idx = min(idx + 600, len(verify))
    print()
    print("验证登录检测部分:")
    print(verify[idx:end_idx])
