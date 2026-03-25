#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
996引擎脚本文件编码修复工具 - 强制使用GBK编码
"""
import os
import sys

def fix_file_gbk(filepath, content):
    """强制写入GBK编码文件"""
    # 确保目录存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # 使用二进制模式写入GBK编码
    gbk_bytes = content.encode('gbk', errors='ignore')
    with open(filepath, 'wb') as f:
        f.write(gbk_bytes)
    
    # 验证写入结果
    with open(filepath, 'rb') as f:
        verify = f.read()
    return verify == gbk_bytes

# QFunction-0.txt 中StdModeFunc100的完整脚本
stdmodefunc100_script = '''[@StdModeFunc100]
#IF
#ACT
INC A500 604800
SENDMSG 6 点卡使用成功！已增加7天游戏时间！
#IF
CHECKMAPNAME 600
#ACT
MAPMOVE 3 330 330
SENDMSG 6 已自动传送回安全区！

'''

if __name__ == "__main__":
    # 修复QFunction-0.txt
    qf_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'
    
    # 读取原文件
    with open(qf_path, 'rb') as f:
        raw = f.read()
    
    # 尝试解码
    text = None
    for enc in ['gbk', 'utf-8', 'gb2312']:
        try:
            text = raw.decode(enc)
            print(f'用{enc}解码成功')
            break
        except:
            continue
    
    if text is None:
        text = raw.decode('gbk', errors='replace')
    
    # 替换StdModeFunc100部分
    import re
    pattern = r'\[@StdModeFunc100\][^\[]*'
    if re.search(pattern, text):
        text = re.sub(pattern, stdmodefunc100_script, text)
        print('已替换StdModeFunc100')
    else:
        # 添加到文件末尾
        text = text.rstrip() + '\n\n' + stdmodefunc100_script
        print('已添加StdModeFunc100')
    
    # 写入GBK编码
    if fix_file_gbk(qf_path, text):
        print('QFunction-0.txt 修复成功！')
    else:
        print('QFunction-0.txt 修复失败！')
    
    # 修复QManage.txt
    qm_path = r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt'
    qm_content = '''[@Startup]

[@Login]
#IF
#act
ChangeBagCount = 126

;================================================
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
SENDMSG 6 您好！当前剩余游戏时间：<$STR(A500)>秒
SETONTIMER 50 3600

;================================================
#IF
; 在副本内被怪物杀死
CHECKMAPNAME BRTL
#ACT
HumanDropUseItem -1 S99
HumanDropUseItem -1 S98
MOV A200 0
MOV A201 0
MAPMOVE 3 330 330
BREAK

#IF
#ACT
BREAK

;================================================
; 死亡前触发 - 复活符
;================================================
[@NextDie]
#IF
CHECKMAPNAME BRTL
EQUAL A202 1
#ACT
MOV A202 0
ChangeModeEx 23 1 1
SENDMSG 5 【复活符】在原地复活了！复活机会已用尽！
BREAK

#IF
#ACT
BREAK

;================================================
; 50号定时器 - 每小时扣减点卡时间
;================================================
[@OnTimer50]
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
SENDMSG 5 您的游戏时间已用完，请充值后使用点卡续费！
'''
    
    if fix_file_gbk(qm_path, qm_content):
        print('QManage.txt 修复成功！')
    else:
        print('QManage.txt 修复失败！')
    
    print('\n所有文件已修复为GBK编码！')
