# -*- coding: utf-8 -*-
# 修改登录提示显示详细时间

# 读取文件
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    text = f.read()

# 旧的显示部分
old_display = '''; 有游戏时间，显示剩余时间
#IF
#ACT
DIV N2 <$HUMAN(点卡时间)> 86400
SENDMSG 6 您好！当前剩余游戏时间：<$HUMAN(点卡时间)>秒（约<$STR(N2)>天）
SETONTIMER 50 3600'''

# 新的显示部分 - 计算天/小时/分钟
new_display = '''; 有游戏时间，计算并显示剩余时间
#IF
#ACT
; 计算天数
DIV N2 <$HUMAN(点卡时间)> 86400
; 计算剩余秒数 = 总秒数 - 天数*86400
MUL N3 <$STR(N2)> 86400
MOV N4 <$HUMAN(点卡时间)>
DEC N4 <$STR(N3)>
; 计算小时 = 剩余秒数 / 3600
DIV N5 <$STR(N4)> 3600
; 计算剩余秒数2 = 剩余秒数 - 小时*3600
MUL N6 <$STR(N5)> 3600
MOV N7 <$STR(N4)>
DEC N7 <$STR(N6)>
; 计算分钟 = 剩余秒数2 / 60
DIV N8 <$STR(N7)> 60
; 显示
SENDMSG 6 您好！当前剩余游戏时间：<$STR(N2)>天<$STR(N5)>小时<$STR(N8)>分钟
SETONTIMER 50 3600'''

if old_display in text:
    text = text.replace(old_display, new_display)
    print("已修改登录时间显示")
else:
    print("未找到原始显示部分")

# 写回
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'w', encoding='gbk') as f:
    f.write(text)

print("文件已保存")

# 验证
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    verify = f.read()

idx = verify.find('; 有游戏时间，计算并显示')
if idx >= 0:
    end_idx = verify.find('SETONTIMER 50 3600', idx)
    if end_idx > 0:
        end_idx = verify.find('\n', end_idx) + 1
    else:
        end_idx = min(idx + 800, len(verify))
    print()
    print("验证新内容:")
    print(verify[idx:end_idx])
