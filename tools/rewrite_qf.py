#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完全重写QFunction-0.txt的StdModeFunc100部分
"""
import shutil

qf_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

# 读取原始文件
with open(qf_path, 'rb') as f:
    raw = f.read()

# 找到StdModeFunc100的位置
idx = raw.find(b'[@StdModeFunc100]')
print(f'StdModeFunc100位置: {idx}')

if idx > 0:
    # 备份
    shutil.copy(qf_path, qf_path + '.bak3')
    
    # 截断到StdModeFunc100之前
    new_raw = raw[:idx]
    
    # 新的StdModeFunc100内容（使用GBK编码）
    new_func = """[@StdModeFunc100]
#IF
#ACT
INC A500 604800
SENDMSG 6 点卡使用成功！已增加7天游戏时间！
#IF
CHECKMAPNAME 600
#ACT
MAPMOVE 3 330 330
SENDMSG 6 已自动传送回安全区！

"""
    new_func_bytes = new_func.encode('gbk')
    
    # 合并并写入
    with open(qf_path, 'wb') as f:
        f.write(new_raw + new_func_bytes)
    
    print('文件已重写！')
    
    # 验证
    with open(qf_path, 'rb') as f:
        verify = f.read()
    verify_idx = verify.find(b'[@StdModeFunc100]')
    print(f'验证: StdModeFunc100在位置 {verify_idx}')
else:
    print('未找到StdModeFunc100')
