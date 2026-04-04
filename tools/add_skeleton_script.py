#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
添加骷髅精灵刷新脚本到QFunction-0.txt
"""
import os
import sys

def main():
    qf_path = r"D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt"
    skeleton_script = """
;========================================
; 击杀骷髅概率刷新骷髅精灵
;========================================
[@OnKillMob]
#IF
#OR
EQUAL <$KILLMONNAME> 骷髅
EQUAL <$KILLMONNAME> 骷髅战士
EQUAL <$KILLMONNAME> 掷斧骷髅
#ACT
SENDMSG 6 你击杀了<$KILLMONNAME>，检测触发中...
GOTO @骷髅精灵概率检测

[@骷髅精灵概率检测]
#IF
RANDOM 10
#ACT
MonGenEx <$PLAYERMAP> <$PLAYERX> <$PLAYERY> 骷髅精灵 5 1 0 251
SENDMSG 6 触发稀有事件！骷髅精灵出现了！（10%概率）
#ELSEACT
SENDMSG 6 骷髅精灵未触发（90%概率）
"""
    
    try:
        # 读取原文件
        with open(qf_path, 'r', encoding='gbk') as f:
            content = f.read()
        
        # 确保脚本只添加一次
        if "[@OnKillMob]" in content:
            print("脚本已存在，跳过添加")
            return
        
        # 在文件末尾添加脚本
        new_content = content + skeleton_script
        
        # 写入文件（GBK编码）
        with open(qf_path, 'w', encoding='gbk', newline='\r\n') as f:
            f.write(new_content)
        
        print("脚本添加成功")
        
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()