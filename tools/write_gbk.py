import codecs

content = """[@点卡测试]
{
欢迎来到点卡管理系统！\\

<查看点卡/@查看点卡>\\
<传送回城/@回城>\\
<关闭/@exit>

[@查看点卡]
#IF
#ACT
VAR Integer HUMAN 点卡时间
#SAY
您的当前剩余游戏时间：<$HUMAN(点卡时间)>秒\\

<返回/@main>\\
<关闭/@exit>

[@回城]
#IF
CHECKMAPNAME 600
CHECKVAR HUMAN 点卡时间 > 0
#ACT
MAPMOVE 3 330 330
SENDMSG 6 已传送回土城安全区！
#ELSEACT
#IF
CHECKMAPNAME 600
#ACT
SENDMSG 5 您的游戏时间已用完，无法传送！
SENDMSG 5 请使用7天点卡续费！
#ELSEACT
SENDMSG 6 您不在欠费等待区，无需传送！
"""

path = r'D:\MirServer\Mir200\Envir\QuestDiary\系统功能\点卡测试.txt'
with codecs.open(path, 'w', 'gbk') as f:
    f.write(content)
print('已生成GBK编码文件')
