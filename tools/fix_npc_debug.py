# -*- coding: utf-8 -*-
import os

# 重新构建 NPC 脚本 - 添加调试信息
lines = []

# [@main]
lines.append(b'[@main]')
lines.append(b'#SAY')
lines.append(b'\xbb\xb6\xd3\xad\xc0\xb4\xb5\xbd\xb5\xe3\xbf\xa8\xb9\xdc\xc0\xed\xcf\xb5\xcd\xb3!\\')
lines.append(b'<\xb2\xe9\xbf\xb4\xb5\xe3\xbf\xa8\xd7\xb4\xcc\xac/@\xb2\xe9\xbf\xb4>\\')
lines.append(b'<\xb4\xab\xcb\xcd\xbb\xd8\xb3\xc7/@\xbb\xd8\xb3\xc7>\\')
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')
lines.append(b'')

# [@查看] - 添加详细调试
lines.append(b'[@\xb2\xe9\xbf\xb4]')
lines.append(b'#IF')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 ..\\..\\QuestDiary\\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
# 调试：直接显示原始变量值
lines.append(b'SENDMSG 6 ==========DEBUG==========')
lines.append(b'SENDMSG 6 HUMAN raw value: <$HUMAN(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>')
lines.append(b'MOV N0 <$HUMAN(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>')
lines.append(b'SENDMSG 6 N0 value: <$STR(N0)>')
lines.append(b'SENDMSG 6 ========================')
lines.append(b'#SAY')
lines.append(b'\xc7\xeb\xb2\xe9\xbf\xb4\xc1\xc4\xcc\xec\xbf\xf2\xb5\xf7\xca\xd4\xd0\xc5\xcf\xa2!\\')
lines.append(b'<\xb7\xb5\xbb\xd8/@main>\\')
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')
lines.append(b'')

# [@回城]
lines.append(b'[@\xbb\xd8\xb3\xc7]')
lines.append(b'#IF')
lines.append(b'CHECKMAPNAME 600')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 ..\\..\\QuestDiary\\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
lines.append(b'#IF')
lines.append(b'CHECKVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 > 0')
lines.append(b'#ACT')
lines.append(b'MAPMOVE 3 330 330')
lines.append(b'SENDMSG 6 \xd2\xd1\xb4\xab\xcb\xcd\xbb\xd8\xcd\xc1\xb3\xc7\xb0\xb2\xc8\xab\xc7\xf8\xa3\xa1')
lines.append(b'#ELSEACT')
lines.append(b'SENDMSG 5 \xc4\xfa\xb5\xc4\xd3\xce\xcf\xb7\xca\xb1\xbc\xe4\xd2\xd1\xd3\xc3\xcd\xea\xa3\xac\xce\xde\xb7\xa8\xb4\xab\xcb\xcd\xa3\xa1')

# 写入文件
file_path = r'D:\MirServer\Mir200\Envir\Market_Def\系统功能\点卡管理员-600.txt'
with open(file_path, 'wb') as f:
    for line in lines:
        f.write(line + b'\r\n')

print('NPC脚本已更新（含调试信息）')
print('文件大小:', os.path.getsize(file_path), '字节')