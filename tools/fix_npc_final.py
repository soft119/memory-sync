# -*- coding: utf-8 -*-
import os

# 最终版 NPC 脚本 - 正确显示时间
lines = []

# [@main]
lines.append(b'[@main]')
lines.append(b'#SAY')
lines.append(b'\xbb\xb6\xd3\xad\xc0\xb4\xb5\xbd\xb5\xe3\xbf\xa8\xb9\xdc\xc0\xed\xcf\xb5\xcd\xb3!\\')
lines.append(b'<\xb2\xe9\xbf\xb4\xb5\xe3\xbf\xa8\xd7\xb4\xcc\xac/@\xb2\xe9\xbf\xb4>\\')
lines.append(b'<\xb4\xab\xcb\xcd\xbb\xd8\xb3\xc7/@\xbb\xd8\xb3\xc7>\\')
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')
lines.append(b'')

# [@查看] - 显示格式化的时间（天/小时/分钟）
lines.append(b'[@\xb2\xe9\xbf\xb4]')
lines.append(b'#IF')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 \\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
# 计算天/小时/分钟
lines.append(b'MOV N0 <$HUMAN(\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4)>')  # 总秒数
lines.append(b'DIV N1 <$STR(N0)> 86400')  # 天数
lines.append(b'MUL N2 <$STR(N1)> 86400')  # 天数对应的秒数
lines.append(b'MOV N3 <$STR(N0)>')
lines.append(b'DEC N3 <$STR(N2)>')  # 剩余秒数
lines.append(b'DIV N4 <$STR(N3)> 3600')  # 小时数
lines.append(b'MUL N5 <$STR(N4)> 3600')  # 小时对应的秒数
lines.append(b'MOV N6 <$STR(N3)>')
lines.append(b'DEC N6 <$STR(N5)>')  # 剩余秒数
lines.append(b'DIV N7 <$STR(N6)> 60')  # 分钟数
lines.append(b'SENDMSG 6 \xc4\xfa\xb5\xc4\xb5\xe3\xbf\xa8\xd3\xe0\xb6\xee\xa3\xba<$STR(N1)>\xcc\xec<$STR(N4)>\xd0\xa1\xca\xb1<$STR(N7)>\xb7\xd6\xd6\xd3')  # 您的点卡余额：X天X小时X分钟
lines.append(b'#SAY')
lines.append(b'\xc4\xfa\xb5\xc4\xb5\xe3\xbf\xa8\xd0\xc5\xcf\xa2\xd2\xd1\xcf\xd4\xca\xbe\xd4\xda\xc1\xc4\xcc\xec\xbf\xf2!\\')
lines.append(b'<\xb7\xb5\xbb\xd8/@main>\\')
lines.append(b'<\xb9\xd8\xb1\xd5/@exit>')
lines.append(b'')

# [@回城]
lines.append(b'[@\xbb\xd8\xb3\xc7]')
lines.append(b'#IF')
lines.append(b'CHECKMAPNAME 600')
lines.append(b'#ACT')
lines.append(b'VAR Integer HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4')
lines.append(b'LOADVAR HUMAN \xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4 \\\xcf\xb5\xcd\xb3\xb9\xa6\xc4\xdc\\\xb5\xe3\xbf\xa8\xca\xb1\xbc\xe4.txt')
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

print('NPC脚本已更新（最终版）')
print('文件大小:', os.path.getsize(file_path), '字节')
print('功能：')
print('  - 查看点卡：显示 X天X小时X分钟')
print('  - 传送回城：需要点卡时间>0')