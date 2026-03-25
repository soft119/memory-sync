# -*- coding: utf-8 -*-
# 修正QFunction-0.txt

# 读取文件
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    text = f.read()

# 找到StdModeFunc100部分
import re
pattern = r'\[@StdModeFunc100\].*?(?=\[@|\Z)'
match = re.search(pattern, text, re.DOTALL)

if match:
    print(f"找到StdModeFunc100，位置: {match.start()}-{match.end()}")
    
    # 新脚本
    new_func = '''[@StdModeFunc100]
#IF
#ACT
TAKE 7天点卡 1
VAR Integer HUMAN 点卡时间
CALCVAR HUMAN 点卡时间 + 604800
SAVEVAR HUMAN 点卡时间
SENDMSG 6 点卡使用成功！已增加7天游戏时间！
SENDMSG 6 当前剩余时间：<$HUMAN(点卡时间)>秒
#IF
CHECKMAPNAME 600
#ACT
MAPMOVE 3 330 330
SENDMSG 6 已自动传送回安全区！
'''
    
    text = text[:match.start()] + new_func + text[match.end():]
    print("已替换")

# 写回
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'w', encoding='gbk') as f:
    f.write(text)

print("文件已保存")

# 验证
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    verify = f.read()

idx = verify.find('[@StdModeFunc100]')
if idx >= 0:
    end_idx = verify.find('[@', idx + 5)
    if end_idx < 0:
        end_idx = min(idx + 500, len(verify))
    print()
    print("验证新内容:")
    print(verify[idx:end_idx])
