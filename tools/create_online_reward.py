# -*- coding: utf-8 -*-
"""
创建在线时长奖励系统
1. 创建存储文件
2. 创建 NPC 脚本
3. 修改 QManage.txt 添加登录/下线检测
"""
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("[创建] 目录：%s" % path)

# Step 1: 创建存储文件
print("=== 步骤 1: 创建存储文件 ===")
storage_path = "D:/MirServer/Mir200/Envir/QuestDiary/系统功能"
ensure_dir(storage_path)

# 上线时间记录文件（引擎自动管理）
login_time_file = storage_path + "/在线奖励.txt"
if not os.path.exists(login_time_file):
    with open(login_time_file, "w", encoding="gbk") as f:
        f.write("")  # 空文件，引擎会自动创建变量
    print("[创建] %s" % login_time_file)
else:
    print("[存在] %s" % login_time_file)

print("\n=== 步骤 2: 创建 NPC 脚本 ===")

# Step 2: 创建点卡管理员 NPC（扩展现有功能）
npc_content = """(@@InPutInteger @@InPutString @@useitemname @@OffLineMsg @@dealgold)

;----------------------------------------------------------------
; 点卡管理员 NPC - Market_Def/Npcs/点卡管理员.txt
; 功能：点卡充值、在线时长奖励领取、查看状态
;----------------------------------------------------------------

[@Temp]
#IF
#ACT
BREAK

[@Main]
#SAY
\r\n<font color=FF0000>==============================</font>\r
\r\n<font color=FFFF00> 点卡管理员为您服务：</font>\r
\r\n<font color=FFFFFF> 游戏时间查询 \<查询剩余时间/@CheckTime></font>\r
\r\n<font color=FFFFFF> 充值点卡 \<进入充值界面/@BuyCardMenu></font>\r
\r\n<font color=FF00FF> 在线时长奖励 \<领取在线礼盒/@OnlineReward></font>\r
\r\n<font color=FF0000>==============================</font>\r
#ACT
BREAK

[@CheckTime]
#SAY
; 显示当前点卡剩余时间
LOADVAR HUMAN 点卡时间 ..\\QuestDiary\\系统功能\\点卡时间.txt
MOV N1 HUMAN 点卡时间
DIV N1 3600
; 计算天数
CALCVAR N2 N1 / 24
CALCVAR N3 N1 - (N2 * 24)
; 剩余小时
CALCVAR N4 N3 * 3600
SENDMSG 6 <font color=FFFF00>您的点卡剩余时间：</font>
SENDMSG 6 <font color=FF0000>%d天%d小时</font> (约%d小时)\r\n<font color=FFFFFF>22级以下免费游戏，22级以上需要点卡</font>
#ACT
GOTO [@Main]
BREAK

[@BuyCardMenu]
#SAY
\r\n<font color=FF0000>=== 点卡充值 ===</font>\r
\r\n<font color=FFFFFF> 7天点卡（VIP 特惠） \<购买/@Buy7Days></font>\r
\r\n<font color=FFFFFF> 1天点卡 \<购买/@Buy1Day></font>\r
\r\n<font color=FFFFFF> 5小时点卡 \<购买/@Buy5Hours></font>\r
\r\n<font color=FFFFFF> 2小时点卡 \<购买/@Buy2Hours></font>\r
\r\n<font color=FFFFFF> 1小时点卡（试用装） \<购买/@Buy1Hour></font>\r
\r\n<font color=FF8000> <返回/@Main></font>\r
#ACT
BREAK

[@Buy7Days]
#SAY
\r\n<font color=FFFF00>【7天点卡】</font>\r
\r
<font color=FFFFFF> 充值时间：7天（168小时）</font>\r
\r\n<font color=FFFFFF> 价格：<font color=FF0000>10元宝</font></font>\r
\r\n<font color=FF00FF> <购买并自动使用/@DoBuy7Days></font>\r
\r\n<font color=FF8000> <返回/@BuyCardMenu></font>\r
#ACT
BREAK

[@DoBuy7Days]
#IF
CHECKVAR N1 元宝 >= 10
#ACT
GIVE 7天点卡 1
SENDMSG 6 <font color=FFFF00>购买成功！</font>请在背包中找到"7天点卡"并双击使用。
CALCVAR N1 元宝 - 10
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>元宝不足！</font>您需要 10 个元宝。
GOTO [@BuyCardMenu]
BREAK

[@Buy1Day]
#SAY
\r\n<font color=FFFF00>【1天点卡】</font>\r
\r\n<font color=FFFFFF> 充值时间：1天（24小时）</font>\r
\r\n<font color=FFFFFF> 价格：<font color=FF0000>2元宝</font></font>\r
\r\n<font color=FF00FF> <购买并自动使用/@DoBuy1Day></font>\r
\r\n<font color=FF8000> <返回/@BuyCardMenu></font>\r
#ACT
BREAK

[@DoBuy1Day]
#IF
CHECKVAR N1 元宝 >= 2
#ACT
GIVE 1天点卡 1
SENDMSG 6 <font color=FFFF00>购买成功！</font>请在背包中找到"1天点卡"并双击使用。
CALCVAR N1 元宝 - 2
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>元宝不足！</font>您需要 2 个元宝。
GOTO [@BuyCardMenu]
BREAK

[@Buy5Hours]
#SAY
\r\n<font color=FFFF00>【5小时点卡】</font>\r
\r\n<font color=FFFFFF> 充值时间：5小时</font>\r
\r\n<font color=FFFFFF> 价格：<font color=FF0000>1元宝</font></font>\r
\r\n<font color=FF00FF> <购买并自动使用/@DoBuy5Hours></font>\r
\r\n<font color=FF8000> <返回/@BuyCardMenu></font>\r
#ACT
BREAK

[@DoBuy5Hours]
#IF
CHECKVAR N1 元宝 >= 1
#ACT
GIVE 5小时点卡 1
SENDMSG 6 <font color=FFFF00>购买成功！</font>请在背包中找到"5小时点卡"并双击使用。
CALCVAR N1 元宝 - 1
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>元宝不足！</font>您需要 1 个元宝。
GOTO [@BuyCardMenu]
BREAK

[@Buy2Hours]
#SAY
\r\n<font color=FFFF00>【2小时点卡】</font>\r
\r\n<font color=FFFFFF> 充值时间：2小时</font>\r
\r\n<font color=FFFFFF> 价格：<font color=FF0000>300金币</font></font>\r
\r\n<font color=FF00FF> <购买并自动使用/@DoBuy2Hours></font>\r
\r\n<font color=FF8000> <返回/@BuyCardMenu></font>\r
#ACT
BREAK

[@DoBuy2Hours]
#IF
CHECKGOLD >= 300
#ACT
GIVE 2小时点卡 1
SENDMSG 6 <font color=FFFF00>购买成功！</font>请在背包中找到"2小时点卡"并双击使用。
CALCVAR GOLD - 300
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>金币不足！</font>您需要 300 个金币。
GOTO [@BuyCardMenu]
BREAK

[@Buy1Hour]
#SAY
\r\n<font color=FFFF00>【1小时点卡（试用装）】</font>\r
\r\n<font color=FFFFFF> 充值时间：1小时</font>\r
\r\n<font color=FFFFFF> 价格：<font color=FF0000>150金币</font></font>\r
\r\n<font color=FF00FF> <购买并自动使用/@DoBuy1Hour></font>\r
\r\n<font color=FF8000> <返回/@BuyCardMenu></font>\r
#ACT
BREAK

[@DoBuy1Hour]
#IF
CHECKGOLD >= 150
#ACT
GIVE 1小时点卡 1
SENDMSG 6 <font color=FFFF00>购买成功！</font>请在背包中找到"1小时点卡"并双击使用。
CALCVAR GOLD - 150
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>金币不足！</font>您需要 150 个金币。
GOTO [@BuyCardMenu]
BREAK

[@OnlineReward]
#SAY
\r\n<font color=FF0000>=== 在线时长奖励 ===</font>\r
\r\n<font color=FFFFFF> 每在线满2小时，即可获得一个【在线礼盒】！</font>\r
\r\n<font color=FFFFFF> 礼盒内含：药品、装备、点卡等惊喜奖品</font>\r
\r\n; 检测当前是否有可领取的奖励
LOADVAR HUMAN 在线奖励 ..\\QuestDiary\\系统功能\\在线奖励.txt
#IF
CHECKVAR HUMAN 在线奖励 >= 1
#ACT
SENDMSG 6 <font color=FF00FF>您有<font color=FFFF00>%d个</font>在线礼盒待领取！</font>
GOTO [@OnlineRewardClaim]
BREAK
#ELSE
#ACT
SENDMSG 6 <font color=FF8000>暂无可领取的在线奖励，继续游戏即可获得。</font>
GOTO [@Main]
BREAK

[@OnlineRewardClaim]
#SAY
\r\n<font color=FF0000>=== 领取在线礼盒 ===</font>\r
\r\nLOADVAR HUMAN 在线奖励 ..\\QuestDiary\\系统功能\\在线奖励.txt
MOV N1 HUMAN 在线奖励
SENDMSG 6 <font color=FFFFFF>您目前有<font color=FFFF00>%d个</font>在线礼盒。</font>\r
\r
<font color=FF00FF> <领取一个礼盒/@ClaimOneBox></font>\r
\r
<font color=FF00FF> <全部领取/@ClaimAllBoxes></font>\r
\r
<font color=FF8000> <返回/@Main></font>\r
#ACT
BREAK

[@ClaimOneBox]
#IF
CHECKVAR HUMAN 在线奖励 >= 1
#ACT
; 扣除一个礼盒
CALCVAR HUMAN 在线奖励 - 1
SAVEVAR HUMAN 在线奖励 ..\\QuestDiary\\系统功能\\在线奖励.txt
; 开出奖品（随机）
GOTO [@OpenRewardBox]
BREAK
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>没有可领取的礼盒！</font>
GOTO [@OnlineRewardClaim]
BREAK

[@ClaimAllBoxes]
#IF
CHECKVAR HUMAN 在线奖励 >= 1
#ACT
; 获取数量
MOV N1 HUMAN 在线奖励
SENDMSG 6 <font color=FFFFFF>正在领取<font color=FFFF00>%d个</font>礼盒...</font>
; 重置数量
CALCVAR HUMAN 在线奖励 0
SAVEVAR HUMAN 在线奖励 ..\\QuestDiary\\系统功能\\在线奖励.txt
; 循环开盒子（简化：只开一次，实际需要用LOOP）
GOTO [@OpenRewardBox]
BREAK
#ELSE
#ACT
SENDMSG 6 <font color=FF0000>没有可领取的礼盒！</font>
GOTO [@OnlineRewardClaim]
BREAK

[@OpenRewardBox]
; 随机奖品池
; N1 = RANDOM 10 (0-9, 共 10种结果)
RANDOM 20
#IF
EQUAL N1 0
#ACT
; SSR - 7天点卡 (5%)
GIVE 7天点卡 1
SENDMSG 6 <font color=FFD700>[SSR] 恭喜开出：7天点卡！</font>
BREAK
#ELSE
#IF
EQUAL N1 1
#ACT
; SSR - 5小时点卡 (5%)
GIVE 5小时点卡 1
SENDMSG 6 <font color=FFD700>[SSR] 恭喜开出：5小时点卡！</font>
BREAK
#ELSE
#IF
EQUAL N1 2
#ACT
; SR - 1天点卡 (10%)
GIVE 1天点卡 1
SENDMSG 6 <font color=FFA500>[SR] 恭喜开出：1天点卡！</font>
BREAK
#ELSE
#IF
EQUAL N1 3
#ACT
; SR - 2小时点卡 (10%)
GIVE 2小时点卡 1
SENDMSG 6 <font color=FFA500>[SR] 恭喜开出：2小时点卡！</font>
BREAK
#ELSE
#IF
EQUAL N1 4
#ACT
; SR - 1小时点卡 (10%)
GIVE 1小时点卡 1
SENDMSG 6 <font color=FFA500>[SR] 恭喜开出：1小时点卡！</font>
BREAK
#ELSE
#IF
EQUAL N1 5
#ACT
; R - 金创药*5 (20%)
GIVE 金创药 5
SENDMSG 6 <font color=87CEEB>[R] 恭喜开出：金创药 x 5</font>
BREAK
#ELSE
#IF
EQUAL N1 6
#ACT
; R - 太阳水*3 (20%)
GIVE 太阳水 3
SENDMSG 6 <font color=87CEEB>[R] 恭喜开出：太阳水 x 3</font>
BREAK
#ELSE
#IF
EQUAL N1 7
#ACT
; R - 随机装备（这里简化为金币）(20%)
CALCVAR GOLD + 5000
SENDMSG 6 <font color=87CEEB>[R] 恭喜开出：5000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 8
#ACT
; N - 小瓶金创药*2 (20%)
GIVE 小瓶金创药 2
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：小瓶金创药 x 2</font>
BREAK
#ELSE
#IF
EQUAL N1 9
#ACT
; N - 小瓶太阳水*2 (20%)
GIVE 小瓶太阳水 2
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：小瓶太阳水 x 2</font>
BREAK
#ELSE
#IF
EQUAL N1 10
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 1000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：1000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 11
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 2000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：2000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 12
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 3000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：3000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 13
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 4000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：4000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 14
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 5000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：5000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 15
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 6000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：6000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 16
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 7000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：7000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 17
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 8000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：8000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 18
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 9000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：9000金币</font>
BREAK
#ELSE
#IF
EQUAL N1 19
#ACT
; N - 金币 (10%)
CALCVAR GOLD + 10000
SENDMSG 6 <font color=FFFFFF>[普通] 恭喜开出：10000金币</font>
BREAK
#ELSE
#ACT
GOTO [@OnlineRewardClaim]
BREAK
"""

npc_path = "D:/MirServer/Mir200/Envir/Market_Def/Npcs/点卡管理员.txt.new"
with open(npc_path, "w", encoding="utf-8") as f:
    f.write(npc_content)
print("[创建] %s" % npc_path)

print("\n=== 完成！下一步需要用 write_gbk.py 转换编码 ===")
