# 996PC引擎 项目记忆

## 工作规范（重要！）

3. **禁止删除全部内容重写** - 修改脚本文件时，只改局部内容，绝不能删除全部内容重写！

1. **修改前先备份** — 用 `replace_in_file` 之前先 `read_file` 备份内容
2. **查知识库** — 优先使用 Skill 中的 `996PC引擎知识库`
3. **上网查阅** — 知识库没有的，上网搜索
4. **再问用户** — 网上也找不到的才来问
5. **不乱编造** — 所有命令都要有依据，禁止自己编造引擎不支持的语法
6. **GBK编码** — 脚本文件写入后用 Python 转换编码，或用 `write_gbk.py`，防止乱码
7. **修改TXT必须转GBK** — 每次修改TXT文档后**立即**用Python转换为GBK+CRLF格式，不能等
8. **遇事先查** — 遇到不懂的知识，先查996PC引擎Skill和记忆，查询不到再上网搜索，还找不到才问用户

> 详细知识体系已迁移至 Skill：`996PC引擎知识库`（C:\Users\Administrator\.workbuddy\skills\996PC引擎知识库\SKILL.md）

## 项目信息

- **项目路径**: `D:\MirServer\`
- **Git仓库**: https://gitee.com/xu-san-shi/996-pc-engine
- **记忆备份**: `F:\MirServer_Memory\`
- **同步脚本**: `D:\MirServer\tools\sync_memory_to_f.bat`
- **GBK写入工具**: `D:\MirServer\tools\write_gbk.py`
- **引擎文档**: `D:\MirServer\chm_extract\游戏引擎反外挂系统\`（810个文件）
- **命令清单**: `D:\MirServer\tools\engine_commands.txt`（915个命令）

## 脚本文件固定路径（重要！）

- **QF (QFunction)**: `D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt`
- **QM (QManage)**: `D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt`
- **点卡存储**: `D:\MirServer\Mir200\Envir\QuestDiary\系统功能\点卡时间.txt`
- **物品数据库**: `D:\MirServer\Mir200\Envir\data\cfg_item.xls`
- **在线奖励存储**: `D:\MirServer\Mir200\Envir\QuestDiary\系统功能\在线奖励.txt`
- **点卡管理员NPC**: `D:\MirServer\Mir200\Envir\Market_Def\Npcs\点卡管理员.txt`

## 地图信息

- **欠费等待区**: 地图600，土城安全区坐标: 3 330 330

## 点卡物品配置（DuraMax必须=100才能消失）

| 物品 | Idx | AniCount | 触发标签 | 增加时间 |
|------|-----|----------|----------|----------|
| 7天点卡 | 10350 | 100 | [@StdModeFunc100] | 604800秒 |
| 1小时点卡 | 10351 | 101 | [@StdModeFunc101] | 3600秒 |
| 2小时点卡 | 10352 | 102 | [@StdModeFunc102] | 7200秒 |
| 5小时点卡 | 10353 | 103 | [@StdModeFunc103] | 18000秒 |
| 1天点卡 | 10354 | 104 | [@StdModeFunc104] | 86400秒 |

## 土城安全区

- 地图ID: 3，坐标: 330 330

## 已实现功能

| 功能 | 关键文件 | 状态 |
|------|----------|------|
| 按小时计费点卡系统 | QF[@StdModeFunc100], QM[@OnTimer50] | ✅ |
| 欠费等待区 | 地图600, 点卡管理员NPC | ✅ |
| 7级自动学习技能 | QF[@PlayLevelUp] | ✅ |
| 新人礼包 | QF[@PlayLevelUp] ISNEWHUMAN | ✅ |
| 背包一键回收 | QF[@ItemBagButtonClick2] checkitem+take+give金币 | ✅ |

## 关键踩坑记录

1. **StdMode=31物品** 必须设置 `Shape=1` 才能触发双击脚本
2. **脚本文件编码** 必须GBK+CRLF，用 `write_gbk.py` 写入
3. **LOADVAR路径** 因脚本所在目录而不同（见Skill文档）
4. **A变量未初始化** 时不能直接用EQUAL检测，先 `MOV N1 <$STR(Axxx)>`
5. 引擎**不支持MOD**（取模），用DIV+MUL替代
6. `<$HUMAN(变量名)>` 在SENDMSG中可用，建议先MOV到N变量再显示
7. **DuraMax换算**：DuraMax ÷ 100 = 显示的使用次数（如5次使用=DuraMax=500）
8. **物品叠加**：OverLap=1或2表示可叠加模式，DuraMax=叠加数量（如10个一堆=DuraMax=10）
9. **回收脚本**：ItemBagButtonClick2触发后，必须用checkitem检测后才给奖励，不能直接TAKE+give
10. **give命令**：引擎里"给金币"要用小写`give 金币`，不能用`GIVE`

## 点卡系统关键配置

- 物品: `Idx=10350, Name=7天点卡, StdMode=31, Shape=1, AniCount=100, Looks=266, DuraMax=50000`
- 存储: `QuestDiary\系统功能\点卡时间.txt`
- 定时器: 50号，每3600秒，CHECKVAR>0扣除，=0传送到地图600
- 22级以下免费，升22级时立即检测

## 背包回收配置

- 触发：`[@ItemBagButtonClick2]`
- 物品价格（书店价一半）：
  - 火球术/治愈术/基本剑术/抗拒火环：250金币
  - 施毒术：500金币
  - 木剑：25金币
  - 匕首：250金币
  - 青铜剑：450金币

## 背包一键回收脚本（Loopgoto循环版）

**触发：** `[@ItemBagButtonClick2]`
**优点：** 循环检测不漏物品，累计显示总金币数

```txt
[@ItemBagButtonClick2]
#ACT
MOV N1 0
Loopgoto @回收检测 100
SENDMSG 6 回收完成！共获得<$STR(N1)>金币
BREAK

[@回收检测]
#IF
checkitem 木剑 1
#ACT
take 木剑 1
give 金币 500
INC N1 500
Loopgoto @回收检测
#ELSEACT
#IF
checkitem 青铜剑 1
#ACT
take 青铜剑 1
give 金币 800
INC N1 800
Loopgoto @回收检测
#ELSEACT
...
#ELSEACT
BREAK
```

**关键点：**
1. 每个 `#IF...#ACT` 后面必须跟 `#ELSEACT` 再接下一个 `#IF`
2. `give 金币` 必须用此格式，不能用 `GIVE`
3. `INC N1 500` 只是累计金额，最后显示用
4. `Loopgoto` 有次数上限，防止死循环

## 在线2小时礼包系统

- 定时器: 55号，每1秒触发一次
- 变量: `在线计时`(秒), `在线礼包已领`(0/1)
- 存储: `QuestDiary\系统功能\在线计时.txt`, `QuestDiary\系统功能\在线礼包已领.txt`
- 抽奖逻辑: `RandomGoto 100 70:@基础礼包|30:@稀有礼包`
- 基础礼包(70%): 超级金创药、超级魔法药、强效太阳水、疗伤药、蜡烛（5选1）
- 稀有礼包(30%): 修复神水、火把、传送石、千里传音、幻境凭证、骰子、双倍卷轴、个性发型、反璞归真、金条、1小时点卡、2小时点卡、5小时点卡、1天点卡（15选1）
- 下线清零: QF[@Logout]处理
- 限制: 每人只能领取一次

## 怪物IDX速查（骷髅系列）

| IDX | 名称 | Race |
|-----|------|------|
| 1020 | 骷髅 | 86 |
| 1023 | 掷斧骷髅 | 87 |
| 1025 | 骷髅战士 | 88 |
| 1029 | 骷髅精灵 | 89 |
| 1030 | 骷髅精灵1 | 89 |
| 1031 | 骷髅精灵2 | 89 |

## 脚本踩坑补充（2026-04-03）

- **#CASE/#IF + GOTO 跳转写法**在击杀触发中有BUG，无法正确触发
- 多种怪物共享概率触发，必须用 `#OR` 写法
- `RANDOM N` = 1/N 概率

## 已实现功能补充

| 功能 | 关键文件 | 状态 |
|------|----------|------|
| 击杀骷髅概率刷新骷髅精灵 | QF[@OnKillMob] | ✅ |
| 在线2小时礼包系统 | QM[@OnTimer55] | ✅ |

## 最近修改（2026-03-25）

- 修复了点卡NPC脚本LOADVAR路径问题
- 添加了法师7级自动学习火球术
- 创建了Git仓库和Gitee云端备份
- 创建了GBK写入工具 `write_gbk.py`
- 创建了记忆同步脚本 `sync_memory_to_f.bat`
- **2026-03-29**: 将整个知识体系制作成Skill（`996PC引擎知识库`）
- **2026-04-03**: 调试并确认骷髅精灵刷新脚本，#OR写法可用
- **2026-04-04**: 配置GitHub备份系统，更换远程仓库地址，设置每日23点自动备份
- **2026-04-06**: 修复点卡系统时间显示问题，物品AniCount配置错误，N变量三位数不解析

## ⚠️ 点卡时间显示问题（2026-04-06 重要踩坑）

### 问题现象
使用点卡后，消息显示 `<$STR(N102)>天<$STR(N105)>小时<$STR(N108)>分钟` 原文不变，变量未解析

### 根本原因
1. **物品数据库AniCount全是0**：cfg_item.xls中5种点卡的AniCount配置错误（0而非100-104），导致触发器不匹配
2. **N变量命名限制（关键！）**：996PC引擎**只支持N0-N99**，**不支持N100及以上的变量名**！

### 解决方案
1. 修正物品数据库AniCount：
   - 7天点卡：AniCount=100 → [@StdModeFunc100]
   - 1小时点卡：AniCount=101 → [@StdModeFunc101]
   - 2小时点卡：AniCount=102 → [@StdModeFunc102]
   - 5小时点卡：AniCount=103 → [@StdModeFunc103]
   - 1天点卡：AniCount=104 → [@StdModeFunc104]

2. 统一使用N1-N7变量（不能用N102/N103等三位数）：
   ```
   DIV N1 <$HUMAN(点卡时间)> 86400      ; 计算天数
   MUL N2 <$STR(N1)> 86400             ; 天数×86400
   MOV N3 <$HUMAN(点卡时间)>            ; 总秒数
   DEC N3 <$STR(N2)>                    ; 减天数，剩余数
   DIV N4 <$STR(N3)> 3600              ; 计算小时
   MUL N5 <$STR(N4)> 3600              ; 小时×3600
   MOV N6 <$STR(N3)>                    ; 减小时，剩余数
   DEC N6 <$STR(N5)>
   DIV N7 <$STR(N6)> 60                ; 计算分钟
   ```

3. 智能显示逻辑：
   - ≥1天：显示 `剩余：5天3小时20分钟`
   - <1天但≥1小时：显示 `剩余：3小时20分钟`
   - <1小时：显示 `剩余：25分钟`

### 引擎变量规则（重要！）
| 格式 | 是否支持 | 说明 |
|------|---------|------|
| `<$HUMAN(变量)>` | ✅ | HUMAN自定义变量可直接显示 |
| `<$STR(N1)>` | ✅ | N0-N99变量可正常解析 |
| `<$STR(N102)>` | ❌ | **三位数N变量不解析！** |
| `$N1` | ⚠️ | 在CALCVAR中可能不识别 |
| `<$STR(N$天)>` | ❌ | N$扩展变量格式未验证 |
