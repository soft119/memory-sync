#!/usr/bin/env python3
# -*- coding: gbk -*-
"""
修复QFunction-0.txt文件的GBK编码和系统变量问题
"""

import os
import sys

def fix_qfunction():
    """修复QF文件的GBK编码和系统变量"""
    
    qf_content = """(@@InPutInteger @@InPutString @@useitemname @@OffLineMsg @@dealgold)

;----------------------------------------------------------------
; QFunction-0.txt - 996PC引擎 全局功能脚本 (GBK编码)
;----------------------------------------------------------------

[@StdModeFunc100]
#IF
#ACT
; 7天点卡双击增加时间
LOADVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
CALCVAR HUMAN 点卡时间 + 604800  ; 增加7天(604800秒)
SAVEVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
TAKE 7天点卡 1
SENDMSG 6 点卡充值成功！增加7天游戏时间。
BREAK

[@PlayLevelUp]
#IF
EQUAL <$LEVEL> 7
CHECKJOB warrior
#ACT
ADDSKILL 基本剑术 3
SENDMSG 6 恭喜升到7级，自动学习基本剑术3级！
BREAK

#IF
EQUAL <$LEVEL> 7
CHECKJOB wizard
#ACT
ADDSKILL 火球术 3
SENDMSG 6 恭喜升到7级，自动学习火球术3级！
BREAK

#IF
EQUAL <$LEVEL> 7
CHECKJOB taoist
#ACT
ADDSKILL 治愈术 3
SENDMSG 6 恭喜升到7级，自动学习治愈术3级！
BREAK

#IF
EQUAL <$LEVEL> 1
ISNEWHUMAN
CHECKJOB warrior
#ACT
MOV HUMAN 新人礼包 1
GIVE 木剑 1
GIVE 蜡烛 1
GIVE 布衣(男) 1
SENDMSG 6 欢迎来到传奇世界！已赠送新人礼包。
BREAK

#IF
EQUAL <$LEVEL> 1
ISNEWHUMAN
CHECKJOB wizard
#ACT
MOV HUMAN 新人礼包 1
GIVE 木剑 1
GIVE 蜡烛 1
GIVE 布衣(男) 1
SENDMSG 6 欢迎来到传奇世界！已赠送新人礼包。
BREAK

#IF
EQUAL <$LEVEL> 1
ISNEWHUMAN
CHECKJOB taoist
#ACT
MOV HUMAN 新人礼包 1
GIVE 木剑 1
GIVE 蜡烛 1
GIVE 布衣(女) 1
SENDMSG 6 欢迎来到传奇世界！已赠送新人礼包。
BREAK

; 22级点卡检测
#IF
EQUAL <$LEVEL> 22
CHECKVAR HUMAN 点卡时间 <= 0
#ACT
MAPMOVE 600 10 10
SENDMSG 6 22级后需要点卡才能继续游戏！请充值后返回土城。
BREAK

[@OnKillMob]
; 击杀骷髅系列怪物概率刷新骷髅精灵
#IF
#OR
EQUAL <$KILLMONNAME> 骷髅
EQUAL <$KILLMONNAME> 掷斧骷髅
EQUAL <$KILLMONNAME> 骷髅战士
#ACT
; 33%概率 (RANDOM 3 = 1/3概率)
RANDOM 3
MonGenEx <$MAP> <$X> <$Y> 骷髅精灵 3 1 0 251
SENDMSG 6 成功击杀骷髅怪物，有概率刷新骷髅精灵！
BREAK

;----------------------------------------------------------------
"""
    
    file_path = r"D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt"
    
    # 备份原文件
    if os.path.exists(file_path):
        import shutil
        backup_path = file_path + ".backup_" + os.path.basename(file_path)
        shutil.copy2(file_path, backup_path)
        print(f"已备份原文件到: {backup_path}")
    
    # 写入GBK编码
    with open(file_path, "w", encoding="gbk") as f:
        f.write(qf_content)
    
    # 转换为Windows换行符
    with open(file_path, "rb") as f:
        content = f.read()
    with open(file_path, "wb") as f:
        f.write(content.replace(b"\n", b"\r\n"))
    
    print(f"QFunction-0.txt 已修复为GBK编码")
    print(f"文件大小: {os.path.getsize(file_path)} 字节")
    
    # 验证
    with open(file_path, "r", encoding="gbk") as f:
        content = f.read()
        checks = [
            ("<$LEVEL>", "等级变量"),
            ("<$KILLMONNAME>", "杀怪名变量"),
            ("<$MAP>", "地图变量"),
            ("RANDOM 3", "随机概率"),
            ("MonGenEx", "刷怪命令"),
        ]
        
        print("验证结果:")
        for pattern, desc in checks:
            if pattern in content:
                print(f"  OK: {desc}")
            else:
                print(f"  ERROR: {desc} 缺失")
    
    return True

if __name__ == "__main__":
    fix_qfunction()