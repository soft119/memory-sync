# -*- coding: utf-8 -*-
import os

# 重新构建 NPC 脚本
# 关键修改：先读取到普通变量，再用 $STR 显示

lines = []

# [@main]
lines.append(b'[@main]')
lines.append(b'#SAY')
lines.append(b'\xbb\xb6\xd3\xad\xc0\xb4\xb5\xbd\xb5\xe3\xbf\xa8\xb9\xdc\xc0\xed\xcf\xb5\xcd\xb3!\\')  # 欢迎来到点卡管理系统!
lines.append(b'<\xb2\xe9\xbf\xb4\xb5\xe3\xbf\xa8\xd7\xb4\xcc\xac/@\xb2\xe9\xbf\xb4>\\')  # <查看点卡状态/@查看>
lines.append(b'<\xb4\xab\xcb\xcd\xbb\xd8\xb3\xc7/@\xbb\xd8\xb3\xc7>\\')  # <传送回城/@回城>
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')  # <关闭/@exit>
lines.append(b'')

# [@查看] - 用普通变量中转
lines.append(b'[@\xb2\xe9\xbf\xb4]')  # [@查看]
lines.append(b'#IF')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')  # VAR Integer HUMAN 点卡时间
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 ..\\..\\QuestDiary\\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
lines.append(b'MOV N0 <$HUMAN(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>')  # MOV N0 <$HUMAN(点卡时间)>
lines.append(b'SENDMSG 6 \xc4\xfa\xb5\xc4\xb5\xb1\xc7\xb0\xca\xa3\xd3\xe0\xd3\xce\xcf\xb7\xca\xb1\xbc\xe4\xa3\xba<$STR(N0)>\xc3\xeb')  # SENDMSG 6 您的当前剩余游戏时间：<$STR(N0)>秒
lines.append(b'SENDMSG 6 \xc7\xeb\xb2\xe9\xbf\xb4\xc1\xc4\xcc\xec\xbf\xf2\xa3\xa1')  # 请查看聊天框！
lines.append(b'#SAY')
lines.append(b'\xc4\xfa\xb5\xc4\xb5\xe3\xbf\xa8\xd0\xc5\xcf\xa2\xd2\xd1\xcf\xd4\xca\xbe\xd4\xda\xc1\xc4\xcc\xec\xbf\xf2!\\')  # 您的点卡信息已显示在聊天框!
lines.append(b'<\xb7\xb5\xbb\xd8/@main>\\')  # <返回/@main>
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')  # <关闭/@exit>
lines.append(b'')

# [@回城]
lines.append(b'[@\xbb\xd8\xb3\xc7]')  # [@回城]
lines.append(b'#IF')
lines.append(b'CHECKMAPNAME 600')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 ..\\..\\QuestDiary\\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
lines.append(b'#IF')
lines.append(b'CHECKVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 > 0')
lines.append(b'#ACT')
lines.append(b'MAPMOVE 3 330 330')
lines.append(b'SENDMSG 6 \xd2\xd1\xb4\xab\xcb\xcd\xbb\xd8\xcd\xc1\xb3\xc7\xb0\xb2\xc8\xab\xc7\xf8\xa3\xa1')  # 已传送回土城安全区！
lines.append(b'#ELSEACT')
lines.append(b'SENDMSG 5 \xc4\xfa\xb5\xc4\xd3\xce\xcf\xb7\xca\xb1\xbc\xe4\xd2\xd1\xd3\xc3\xcd\xea\xa3\xac\xce\xde\xb7\xa8\xb4\xab\xcb\xcd\xa3\xa1')  # 您的游戏时间已用完，无法传送！
lines.append(b'')
lines.append(b'[@\xb7\xb5\xbb\xd8]')  # [@返回]
lines.append(b'#ACT')
lines.append(b'GOTO @main')

# 写入文件 (CRLF换行)
file_path = r'D:\MirServer\Mir200\Envir\Market_Def\系统功能\点卡管理员-600.txt'
with open(file_path, 'wb') as f:
    for line in lines:
        f.write(line + b'\r\n')

print(f'NPC脚本已更新: {file_path}')
print(f'文件大小: {os.path.getsize(file_path)} 字节')

# 验证
with open(file_path, 'rb') as f:
    content = f.read()
    if b'MOV N0 <$HUMAN' in content and b'$STR(N0)' in content:
        print('OK: 使用 N0 变量中转显示')
    print('关键行:')
    for line in content.split(b'\r\n'):
        if b'MOV N0' in line or (b'SENDMSG' in line and b'$STR(N0)' in line):
            print(f'  {line}')