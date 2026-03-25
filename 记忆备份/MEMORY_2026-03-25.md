# 996PC引擎 完整知识库

## 2026-03-24 更新：点卡系统修复完成

### 编码问题解决
- QFunction-0.txt 和 QManage.txt 必须使用GBK编码
- 用 `tools/fix_qf_final.py` 脚本修复编码问题
- 备份损坏文件到 `QFunction-0.txt.broken`

### 点卡系统配置
1. **地图**：MapInfo.txt `[600 欠费等待区] NORECALL FIGHT`
2. **物品**：cfg_item.xls `Idx=10350, Name=7天点卡, StdMode=31, Shape=1, AniCount=100, Looks=266, DuraMax=50000`
3. **存储**：`QuestDiary\系统功能\点卡时间.txt`（使用自定义变量HUMAN点卡时间）
4. **QFunction-0.txt**：`[@StdModeFunc100]` TAKE消耗物品后用CALCVAR增加604800秒，SAVEVAR保存
5. **QManage.txt**：
   - `[@Login]` VAR声明 → LOADVAR读取 → CHECKVAR检测 → 显示时间
   - `[@OnTimer50]` LOADVAR → CHECKVAR检测 → CALCVAR扣除 → SAVEVAR保存

### 关键调试发现
- **StdMode=31物品必须设置Shape=1** 才能触发双击脚本！
- A变量未初始化时不能直接用EQUAL/LARGE/SMALL检测
- 解决方法：`MOV N1 0` 然后 `MOV N1 <$STR(A500)>` 间接检测
- 物品StdMode=31是功能物品，AniCount对应[@StdModeFuncX]标签编号
- **编码问题**：QFunction-0.txt和QManage.txt必须用GBK编码，换行符用CRLF

### 2026-03-24 新增功能
- **7级自动学习技能**：战士-基本剑术，法师-火球术，道士-治愈术，技能等级3级
- **新人礼包系统**：1级赠送木剑、蜡烛、布衣(按性别)，使用`HUMAN 新人礼包`变量确保只送一次
- **点卡系统优化**：22级以下免费游戏，升级到22级时立即检测点卡并传送欠费区

### ⚠️ 重要教训
- **写脚本前必须先查阅官方文档！** CHM帮助文档路径：`D:\MirServer\996M2引擎PC端帮助文档.chm` 或 `D:\MirServer\chm_extract\`
- 不要假设命令存在，996引擎不支持MOD（取模）命令
- 正确流程：查文档 → 确认语法 → 参考示例 → 写脚本
- StdMode=31物品DuraMax控制叠加数量，不是持久度

### 2026-03-25 修复记录

#### NPC脚本路径问题修复
- **LOADVAR路径格式因脚本位置而异**：
  - QFunction-0.txt（在`Market_Def\`）：`..\QuestDiary\系统功能\点卡时间.txt`
  - QManage.txt（在`MapQuest_Def\`）：`..\QuestDiary\系统功能\点卡时间.txt`
  - NPC脚本（在`Market_Def\系统功能\`）：`\系统功能\点卡时间.txt`（从QuestDiary目录开始）
- **关键发现**：NPC脚本路径从QuestDiary目录算起，用`\目录\文件.txt`格式
- `<$HUMAN(变量名)>`在SENDMSG中可正常使用，但建议先用MOV传到普通变量再显示

#### 法师7级自动学习火球术
- **问题**：QFunction-0.txt中只有战士和道士有7级自动学习技能，法师缺失
- **修复**：在`[@PlayLevelUp]`标签中添加法师7级学习火球术3级
- **位置**：QFunction-0.txt 第93-99行

---

## 引擎概述
- **引擎名称**: 996PC引擎 (也叫996M2引擎)
- **游戏类型**: 传奇类私服引擎（类似热血传奇 1.76）
- **帮助文档**: `d:\MirServer\996M2引擎PC端帮助文档.chm` (26.9MB，CHM格式)
- **CHM提取目录**: `d:\MirServer\chm_extract\游戏引擎反外挂系统\`
- **服务器结构**: GameCenter → LoginSrv/LoginGate/RunGate/SelGate → DBServer → Mir200

## 关键文件路径
| 文件 | 路径 | 用途 |
|------|------|------|
| 物品数据库 | `Mir200\Envir\data\cfg_item.xls` | Excel格式, 第1-3行注释, 第4行起数据; 关键列: Idx, Name, StdMode, Anicount, Looks, DuraMax |
| 地图信息 | `Mir200\Envir\MapInfo.txt` | 地图配置、标志位、连接点 |
| 全局功能脚本 | `Mir200\Envir\Market_Def\QFunction-0.txt` | 简称QF, 所有功能触发入口 |
| 登录/死亡/定时器 | `Mir200\Envir\MapQuest_Def\QManage.txt` | 简称QM, 服务器启动/登录/定时器 |
| 怪物刷怪 | `Mir200\Envir\MonGen.txt` | 怪物刷新配置 |
| NPC列表 | `Mir200\Envir\Npcs.txt` | 系统管理NPC(固定NPC) |
| 商人NPC | `Mir200\Envir\MerChant.txt` | 商人NPC配置 |
| NPC脚本目录 | `Mir200\Envir\QuestDiary\` | NPC脚本文件根目录 |
| 怪物爆率 | `Mir200\Envir\MonItems\*.txt` | 按怪物名命名的爆率文件 |
| 地图杀怪触发 | `Mir200\Envir\MapQuest.txt` | 杀怪触发配置, 需加ONKILLMON参数 |
| 地图事件 | `Mir200\Envir\MapEvent.txt` | 地图触发事件配置 |
| 等级经验 | `Mir200\Envir\Exps.ini` | 人物等级经验表 |
| 等级属性 | `Mir200\Envir\LevelAbilitys0.ini` | 人物等级属性配置 |
| 系统提示 | `Mir200\Envir\String.ini` | 系统提示信息配置 |
| 用户命令 | `Mir200\Envir\UserCmd.txt` | 自定义用户命令(如@xxx) |
| 出出生点 | `Mir200\Envir\StartPoint.txt` | 安全区及出生点配置 |
| 小地图 | `Mir200\Envir\MiniMap.txt` | 小地图配置 |
| 系统商城 | `Mir200\Envir\ShopItemList.txt` | 商城物品列表 |
| 自定义NPC | `Mir200\Envir\CustomNpc\` | 自定义NPC(非Npcs.txt) |
| 机器人 | `Mir200\Envir\Robot.txt` / `RobotManage.txt` | 机器人配置 |
| 全局变量存储 | `Mir200\Envir\GlobalVal.ini` | 全局变量持久化 |
| 引擎配置 | `MirServer\!Setup.txt` | 引擎核心配置文件 |
| 管理员列表 | `Mir200\Envir\AdminList.txt` | GM账号列表 |
| 禁止列表 | `Mir200\Envir\Deny*.txt` | 禁止IP/帐号/角色名 |

## 脚本系统详解

### 基本语法
```
; 注释
#IF       条件判断开始
#ACT      执行块开始
#ELSEACT  条件不满足时执行
#SAY      NPC对话显示内容
BREAK     跳出当前逻辑
#CALL [\路径\文件.txt] @标签  调用外部脚本(QuestDiary根目录)
GOTO @标签                      脚本内跳转
DELAYGOTO 毫秒 @标签            延时跳转
```

### 变量系统
| 变量类型 | 范围 | 作用域 | 说明 |
|----------|------|--------|------|
| A0-A499 | 个人全局 | 角色唯一, 保存 | 跨脚本共享 |
| G0-G499 | 全局 | 服务器共享, 保存 | 跨玩家共享 |
| D0-D99 | 个人 | 下线不保存 | - |
| P0-P99 | 个人 | 关对话框重置 | - |
| N0-N99 | 个人 | 小退归0 | 临时变量 |
| M0-M99 | 个人 | 换地图清空 | - |
| S0-S99 | 字符串 | 小退归0 | 存储字符串 |
| I0-I499 | 全局 | 不保存 | - |
| U0-U254 | 跨服 | 保存 | 跨服功能 |
| H0-H999 | 英雄 | 英雄变量 | 操作英雄 |
| S$任意字符 | 扩展字符变量 | 如 S$我的人物名称 |
| N$任意字符 | 扩展数字变量 | 如 N$我的杀怪总数 |

### 多级脚本操作
- `角色名.命令` 操作指定玩家
- `H.命令` 操作英雄
- `O.命令` 操作主人(英雄脚本中)
- `M.命令` 操作当前攻击怪物
- `P.命令` 操作对面角色
- `pex.命令` 操作攻击目标
- 英雄扩展: `HM.`攻击怪物, `HP.`对面角色, `HH.`对面英雄, `hpex.`攻击目标

### 自定义变量 (突破A/G限制)
```脚本
; 声明
VAR Integer HUMAN QQQQ
; 读取
LOADVAR HUMAN QQQQ VarSave.txt
; 保存
SAVEVAR HUMAN QQQQ VarSave.txt
; 增加/减少
CALCVAR HUMAN QQQQ + 5
CALCVAR HUMAN QQQQ - 5
; 检测
CHECKVAR HUMAN QQQQ = 5
CHECKVAR HUMAN QQQQ > 5
CHECKVAR HUMAN QQQQ < 5
; 读取值到显示
<$HUMAN(QQQQ)>
```

### 系统变量
| 变量 | 说明 |
|------|------|
| `<$USERNAME>` | 当前玩家名称 |
| `<$CURRRTARGETNAME>` | 当前目标名称(去数字) |
| `<$CURRRTARGETFULLNAME>` | 当前目标完整名称(含数字) |
| `<$CURRTEMNAME>` | 当前操作物品名称 |
| `<$G_CURRTEMNAME>` | 当前物品改名名称 |
| `<$CURRTEMMAKEINDEX>` | 当前物品唯一ID |
| `<$CURRTAKETEMPOS>` | 当前穿脱装备位置 |
| `<$CURRTEMSTDMODE>` | 当前物品StdMode值 |
| `<$CURRTEMSHAPE>` | 当前物品Shape值 |
| `<$CURRTEMANICOUNT>` | 当前物品AniCount值 |
| `<$CURRTEMLOOKS>` | 当前物品Looks值 |
| `<$CURRTEMDURA>` | 当前物品当前持久值 |
| `<$CURRTEMDURAMAX>` | 当前物品最大持久值 |
| `<$CURRTEMINDEX>` | 当前物品Idx值 |
| `<$CURRTEMCOLOR>` | 当前物品Color值 |
| `<$KILLMONNAME>` | 杀死的怪物名称 |
| `<$KILLMONX>` / `<$KILLMONY>` | 杀怪坐标 |
| `<$X>` / `<$Y>` | 当前玩家坐标 |
| `<$MAP>` | 当前地图编号 |
| `<$oldmap>` | 切换前地图名 |
| `<$LEVEL>` | 当前等级 |
| `<$HP>` / `<$MP>` | 当前生命/魔法 |
| `<$MAXHP>` / `<$MAXMP>` | 最大生命/魔法 |
| `<$AC>` / `<$MAC>` | 防御/魔防 |
| `<$DC>` / `<$MC>` / `<$SC>` | 攻击/魔法/道术 |
| `<$GUILDNAME>` | 行会名称 |
| `<$GENMONNAME>` | 刷出的怪物名称 |
| `<$GENMONALLNAME>` | 带数字的怪物名称 |
| `<$GENMONMAP>` | 刷怪地图名称 |
| `<$GENMONX>` / `<$GENMONY>` | 刷怪坐标 |
| `<$STR(N1)>` | 读取数值变量N1为字符串 |
| `<$DAMAGEVALUE>` | 当前伤害值 |
| `<$CURRRUSEMAGICID>` | 当前使用魔法ID |
| `<$MACHINEID>` | 机器码 |
| `%s` | 代表人物名称 |
| `%d` | 代表NPC名称 |
| `%ServerName` | 区名称 |
| `<$BAGCOUNT>` | 当前背包物品数 |
| `<$BAGMAXCOUNT>` | 背包最大数量 |
| `<$PARAM1>` ~ `<$PARAM6>` | 自定义命令参数 |

## 触发标签完整列表

### QManage.txt (登录脚本) 触发
| 标签 | 触发时机 |
|------|----------|
| `[@Startup]` | M2服务端启动时(只执行一次) |
| `[@Login]` | 玩家登录时 |
| `[@OnTimerX]` | 个人定时器触发 (X=0-255) |
| `[@OnTimerExX]` | 全局定时器触发 (X=0-255) |
| `[@LoadGuild]` | 行会变量声明(用VAR Integer GUILD) |
| `[@LoadNatIon]` | 国家变量声明 |

### QFunction-0.txt (功能脚本) 触发
| 标签 | 触发时机 |
|------|----------|
| `[@StdModeFuncX]` | 双击StdMode物品触发 (X=Anicount值, 需StdMode=31或2) |
| `[@PlayDie]` | 玩家死亡时 |
| `[@NextDie]` | 死亡前触发(复活符等) |
| `[@Revival]` | 人物复活时 |
| `[@PlayLevelUp]` | 升级时 |
| `[@GetExp]` | 获得经验时(<$GetExp>=经验值) |
| `[@KillPlay]` | 杀人时 |
| `[@OnKillMob]` | 杀怪触发 (需MapQuest.txt加ONKILLMON, CheckKillMonName判断怪名) |
| `[@GroupKillMon]` | 组队杀死怪物时 |
| `[@KillSlave]` | 杀死人物宝宝时(CheckKillSlaveName, <$darlingpet>=主人) |
| `[@CritTrigger]` | 暴击触发, Return参数可改伤害, <$PARAM1>=暴击伤害, <$PARAM2>=技能ID |
| `[@StartAutoPlayGame]` | 开始挂机 |
| `[@StopAutoPlayGame]` | 停止挂机 |
| `[@StartMyShop]` | 开始摆摊 |
| `[@ShopStall]` | 点击摆摊/停止摆摊 |
| `[@BuyUserShopItem]` | 个人商店购买物品时(买家触发) |
| `[@TakeOnX]` | 穿上指定位置装备 (X=0-28,30-47) |
| `[@TakeOffX]` | 脱下指定位置装备 |
| `[@TakeOnEx]` | 穿上任意装备(通用) |
| `[@TakeOffEx]` | 脱下任意装备(通用) |
| `[@TakeOnBeforeX]` | 穿上指定位置装备前 |
| `[@TakeOffBeforeX]` | 脱下指定位置装备前 |
| `[@TakeOnBeforeEX]` | 穿上任意装备前 |
| `[@TakeOffBeforeEX]` | 脱下任意装备前 |
| `[@HeroTakeOnEx]` | 英雄穿上任意装备 |
| `[@HeroTakeOffEx]` | 英雄脱下任意装备 |
| `[@DropItemX]` / `[@DropItemEX]` | 扔物品后触发(X=Idx) |
| `[@DropItemfrontXX]` / `[@DropItemfrontEX]` | 扔物品前触发 |
| `[@PickUpItemXX]` / `[@PickUpItemEX]` | 捡取物品后触发(XX=Idx) |
| `[@PickUpItemfrontXX]` / `[@PickUpItemfrontEX]` | 捡取物品前触发 |
| `[@PickUpDropItemEX]` | 人物死亡掉落前触发 |
| `[@ScatterBagItems]` | 爆物品触发 (需M2物品规则开启) |
| `[@ItemBagButtonClickX]` | 背包按钮点击(X=1-5) |
| `[@ItemDamageX]` | 装备持久消失时(X=0-18) |
| `[@UpgradeOKX]` / `[@UpgradeFailX]` | 装备升级成功/失败(X=位置) |
| `[@GroupItemOnX]` / `[@GroupItemOffX]` | 套装生效/失效(X=套装编号) |
| `[@FoundryFail]` | 物品合成失败(%Item=物品名) |
| `[@EnterMap]` | 切换地图时(<$oldmap>=旧地图) |
| `[@beforeroute]` | 进入连接点前 |
| `[@Attack]` | 物理攻击时 |
| `[@Struck]` | 被物理攻击时 |
| `[@MagicAttack]` / `[@MagicStruck]` | 魔法攻击/被攻击 |
| `[@AttackDamage]` / `[@StruckDamage]` | 攻击/被攻击掉血前(ChangeDamageValue改伤害) |
| `[@MagicX]` | 使用指定魔法(X=魔法ID, MAGICDISABLED禁止) |
| `[@PlayReconnection]` | 人物小退时 |
| `[@SoftClose]` | 小退前(可DIABLESOFTCLOSE禁止) |
| `[@TitleChanged_XX]` | 改变称号(XX=Shape值) |
| `[@Untitled_XX]` | 取消称号 |
| `[@Help]` | 界面帮助按钮 |
| `[@UsePlugin]` | 检测到外挂时 |
| `[@StartGroup]` | 组队前(CreateGroupFail阻止) |
| `[@GroupCreate]` | 创建队伍(S0=队员名) |
| `[@GroupAddMember]` | 添加队员(S0=队员名) |
| `[@LeaveGroup]` | 离开队伍 |
| `[@GroupDelMember]` | 踢出队员(S0=被踢名) |
| `[@SlaveDie]` | 宝宝被杀死(<$CURRRSLAVENAME>) |
| `[@SlaveAttack]` / `[@SlaveMagicAttack]` | 宝宝攻击(M.HumanHP改怪物HP) |
| `[@GetCastleX]` | 占领沙巴克(X=城堡编号) |

### 英雄触发 (QF中, 操作加H.前缀)
| 标签 | 触发时机 |
|------|----------|
| `[@HeroLogin]` | 英雄上线(由主人执行, H.ISNEWHUMAN判断新英雄) |
| `[@HeroDie]` | 英雄死亡 |
| `[@HeroLevelUp]` | 英雄升级 |
| `[@HeroEnterMap]` | 英雄切换地图 |
| `[@HeroGetExp]` | 英雄获取经验(<$HeroGetExp>) |
| `[@HeroAttack]` / `[@HeroStruck]` | 英雄物理攻击/被攻击 |
| `[@HeroMagicAttack]` / `[@HeroMagicStruck]` | 英雄魔法攻击/被攻击 |
| `[@HeroAttackDamage]` / `[@HeroStruckDamage]` | 英雄攻击/被攻击掉血前 |
| `[@HeroTakeOnX]` / `[@HeroTakeOffX]` | 英雄穿脱指定位置装备 |
| `[@HeroTakeOnEx]` / `[@HeroTakeOffEx]` | 英雄穿脱任意装备 |
| `[@HeroGroupItemOnX]` / `[@HeroGroupItemOffX]` | 英雄套装生效/失效 |
| `[@AddHeroBag]` | 物品进入英雄背包 |
| `[@HeroMobTreachery]` | 英雄宝宝叛变 |

## 操作命令完整列表 (约139+条)

### 传送类
| 命令 | 格式/说明 |
|------|------|
| `MAPMOVE` | `MAPMOVE 地图 X Y [范围]` 传送到指定坐标, 范围参数可随机偏移 |
| `GoHome` | 传送到回城点 |
| `GROUPMAPMOVE` | `GROUPMAPMOVE 地图 X Y [最低等级] [触发字段]` 组队传送 |
| `GROUPMOVE` | `GROUPMOVE 地图 [最低等级] [触发字段]` 组队随机传送 |
| `BREAKTIMERECALL` | 清除延时移动 |
| `batchDelay/addbatch/batchmove` | 按地图列表移动(设定每张地图停留时间) |

### 消息类
| 命令 | 格式/说明 |
|------|------|
| `SENDMSG` | `SENDMSG 类型 [字体色] [背景色] %s信息%d` 0红广播/1+NPC名/2+人NPC名/3 NPC头顶/4头顶另一格式/5红给自己/6绿给自己/7蓝给自己/8跨服/9屏幕中间HTML色 |
| `SendCenterMsg` | `SendCenterMsg 前景色 背景色 文字 模式 时间 [倒计时标签]` 模式0自己/1全服/2行会/3国家/4当前地图/5替换/6跨服 |
| `SENDTOPCHATBOARDMSG` | `SENDTOPCHATBOARDMSG 模式 字体色 背景色 秒 信息 [显示人物名]` 0全服/1自己/2跨服 |
| `SendCustomMsg` | `SendCustomMsg 类型 内容 前景色 背景色 X Y [PC(X)] [PC(Y)]` 任意坐标公告 |
| `GuildNoticeMsg` | `GuildNoticeMsg 字体色 背景色 信息 self` 行会公告 |

### 属性调整类
| 命令 | 格式/说明 |
|------|------|
| `CHANGELEVEL` | `CHANGELEVEL (=,+,-) 等级(1-500)` |
| `CHANGEEXP` | `CHANGEEXP (=,+,-) 经验 [是否同时加聚灵珠(0/1)]` |
| `ChangeHumAbility` | `ChangeHumAbility 属性(1-20) (+,-,=) 值 时间秒` 1防下/2防上/3魔御下/4魔御上/5攻下/6攻上/7魔下/8魔上/9道下/10道上/11MaxHP/12MaxMP/13HP恢复/14MP恢复/15毒恢复/16毒躲避/17魔法躲避/18准确/19敏捷/20幸运; 仅在线有效 |
| `BONUSPOINT` | `BONUSPOINT (=,+) 点数(0-1000)` |
| `USEBONUSPOINT` | `USEBONUSPOINT 位置(1攻/2魔/3道/4防/5魔防/6HP/7MP/8准确/9躲避/10防下/11防上/12魔防下/13魔防上/14吸收) 符号 点数` |
| `HUMANHP` | `HUMANHP (+,-,=) 数字 [飘血ID]` |
| `HUMANMP` | `HUMANMP (+,-,=) 数字 [飘血ID]` |
| `ADDHPPER` | `ADDHPPER 符号 百分比 [0百分比/1千分比] [飘血ID]` |
| `ADDMPPER` | `ADDMPPER 符号 百分比 [0百分比/1千分比] [飘血ID]` |
| `CHANGEPKPOINT` | `CHANGEPKPOINT (=,+,-) PK点数` |
| `CREDITPOINT` | `CREDITPOINT (=,+,-) 声望点` |
| `GAMEGLORY` | `GAMEGLORY (+,-,=) 荣誉值` |
| `GAMEGOLD` | `GAMEGOLD (=,+,-) 游戏币` |
| `GAMEPOINT` | `GAMEPOINT (=,+,-) 游戏点` |
| `GAMEDIAMOND` | `GAMEDIAMOND (=,+,-) 金刚石(0-2147483647)` |
| `GAMEGIRD` | `GAMEGIRD (=,+,-) 灵符` |
| `SETMEMBERLEVEL` | `SETMEMBERLEVEL (=,+,-) 会员等级(1-65535)` |
| `SETMEMBERTYPE` | `SETMEMBERTYPE (=,+,-) 会员类型(1-65535)` |
| `ChangeHumNewValue` | `ChangeHumNewValue 位置(0-16) 百分比(0-255) 秒 [威力倍数]` 0暴击/1攻伤/2物伤减/3魔伤减/4忽视防御/5伤害反弹/6增加目标暴率/7体力/8魔力/9怒气恢复/10合击/11防暴击/12防麻痹/13防复活/14防全毒/15防冰冻/16防蛛网 |
| `CHANGENAMECOLOR` | `CHANGENAMECOLOR 颜色(0-255)` |
| `SETBODYCOLOR` | `SETBODYCOLOR 颜色 [秒]` (255清除) |
| `ChangeSpeed` | `ChangeSpeed 类型(1移动/2攻击/3魔法) 值(-10到10) [秒]` |
| `ChangeAttatckMode` | `ChangeAttatckMode (0-7)` 0全体/1和平/2夫妻/3师徒/4编组/5行会/6红名/7国家 |
| `THROUGHHUM` | `THROUGHHUM 模式(-1恢复/0穿人穿怪/1穿怪/2穿人) 秒` |
| `MAKEPOSION` | `MAKEPOSION 类型(0绿毒/1红毒/5麻痹/12冰冻/13蛛网) 秒 [威力]` |
| `BMAKEPOSION` | 宝宝专用中毒 |
| `Detoxifcation` | 解毒 |
| `REALIVE` | 复活人物 |
| `NotDropItemCount` | `NotDropItemCount (+,-,=) 次数` 死亡不掉装备次数 |
| `ProtectHP` | `ProtectHP 检测血量/百分比 秒杀后血量 秒 是否百分比` 秒杀保护, 触发[@ProtectHP] |

### ChangeModeEx 模式详解 (28种)
| 模式 | 说明 | 附加值 |
|------|------|--------|
| 1 | 无敌 | 0或空=满血, 1=只无敌不回血 |
| 2 | 隐身 | - |
| 3 | HP | 增加HP值 |
| 4 | MP | 增加MP值 |
| 5-7 | 攻击力/魔法力/道术力 | 增加数值 |
| 8 | 攻击速度 | 增加数值 |
| 9 | 禁止攻击 | - |
| 10 | 锁定 | - |
| 11 | 禁锢 | 禁锢范围 |
| 12-13 | 冰冻/蛛网 | 机率, 时长 |
| 14-17 | 防麻痹/防禁锢/防冰冻/防蛛网 | - |
| 18 | 麻痹 | 机率, 时长 |
| 19 | 护身 | 掉蓝比例/100 |
| 20-21 | 吸血/吸蓝 | 机率, 百分比 |
| 22 | 对怪隐身 | - |
| 23-24 | 复活/破复活 | 复活次数 |
| 25 | 定身 | - |
| 26 | 失明 | 可见范围(格), 时长 |
| 27 | 混乱 | 时长(随机走动) |
| 28 | 持续流血 | 持续时间, 间隔秒, 每次损失HP |

### 物品类
| 命令 | 格式/说明 |
|------|------|
| `GIVE` | `GIVE 物品名 数量` |
| `TAKE` | `TAKE 物品名 数量` |
| `GiveStateItem` | `GiveStateItem 物品名 项目1-7 数量 [改名]` 1禁扔/2禁交易/3禁存/4禁修/5禁出售/6禁爆/7丢弃消失 |
| `GiveStateItemex` | `GiveStateItemex 物品名 数量 项目1-8` 项目8=禁止摆摊拍卖 |
| `SetNewItemValue` | `SetNewItemValue 位置(-1~28或30~47) 属性(0-16) (+,-,=) 值(1-100)` 物品元素属性 |
| `ChangeItemNameColor` | `ChangeItemNameColor 位置 颜色(0-255)` 0恢复默认 |
| `ChangeItemUpgradeCount` | `ChangeItemUpgradeCount 位置 (+,-,=) 次数(0-255)` 星星数量 |
| `RECLAIMITEM` | 返回OK框中物品到包裹 |
| `LINKPICKUPITEM` | 关联当前操作物品 |
| `SENDUPGRADEITEM` | 刷新物品属性到客户端 |
| `StartPickUp` | `StartPickUp [中心(0=人物)/范围(最大8)/间隔(最小500ms)]` |
| `StopPickUp` | 停止自动捡取 |
| `PICKUPITEMS` | `PICKUPITEMS X Y 范围 是否按列表 是否捡死亡爆物` |

### 怪物/宝宝类
| 命令 | 格式/说明 |
|------|------|
| `MonGen` | `MonGen 怪物名 数量 范围` 基础刷怪 |
| `MonGenEx` | `MonGenEx 地图 X Y 怪物名 范围 数量 [内功怪(0/1)] [名称颜色] [国家] [同国可攻击]` 扩展刷怪 |
| `CLEARMAPMON` | `CLEARMAPMON 地图号` 清除所有怪物(宝宝和禁止列表除外) |
| `MonItems` | `MonItems [1]` 鞭尸爆物品(仅QF[@KillMon]下, 1=含极品值) |
| `MonItemsex` | `MonItemsex 怪物名 次数(最大20) [延迟毫秒]` 高级鞭尸 |
| `SetMonBurstItems` | `SetMonBurstItems 物品名 数量` 强制爆指定物品(仅[@KillMon]) |
| `ChangeSlaveLevel` | `ChangeSlaveLevel 名字 (+,-,=) 等级(1-7)` 宝宝等级 |
| `ChangeSlavePowerRate` | `ChangeSlavePowerRate 宝宝名 (+,-,=) 威力倍数 秒` 实际=设置值/100 |
| `ChangeSlaveAttackHumPowerRate` | 宝宝不攻击人物(倍率=0) |
| `ChangeSlaveAbil` | `ChangeSlaveAbil 宝宝名 类型(0攻/1防) 百分比 属性(0道/1魔/2攻)` 叠加人物属性给宝宝 |
| `CHANGEMAXTAMMINGSLAVECOUNT` | `CHANGEMAXTAMMINGSLAVECOUNT (=,+,-) 数量` 诱惑宝宝上限, =0不限制 |
| `HighLevelKillMonFixExp` | `HighLevelKillMonFixExp 秒 [是否保存]` 高等级杀怪经验不变 |

### 技能类
| 命令 | 格式/说明 |
|------|------|
| `ADDSKILL` | `ADDSKILL 技能名 [等级] [别名]` |
| `DELSKILL` | `DELSKILL 技能名` |
| `CLEARSKILL` | 清除所有技能 |
| `DELNOJOBSKILL` | 清除非本职业技能 |
| `SKILLLEVEL` | `SKILLLEVEL 魔法名 (+,-,=) 等级 [强化(0/1)]` |
| `CHANGETRANPOINT` | `CHANGETRANPOINT 技能名 (+,-,=) 点数` |
| `CHECKSKILL` | `CHECKSKILL 技能名 (<,>,=,?) 等级` |
| `CheckMagicName` | `CheckMagicName 魔法名` 是否学会 |
| `releasemagic` | `releasemagic 技能ID [强化(0/1)] [等级] [目标(1目标/2自身)] [无动作(0/1)]` 无需蓝/符/CD |
| `SetSkillPower` | `SetSkillPower 技能ID +/-/= 人伤% 人伤值 怪伤% 怪伤值 防御% 防御值 秒(-1永久)` |
| `GetSkillPower` | `GetSkillPower 技能ID 人伤%(变量) 人伤值(变量) 怪伤%(变量) 怪伤值(变量) 防%(变量) 防值(变量) 时间(变量)` |
| `ClearSkillWaitTime` | `ClearSkillWaitTime 技能ID` 清空CD |

### 定时器类
| 命令 | 格式/说明 |
|------|------|
| `SetOnTimer` | `SetOnTimer 索引(0-255) 秒 [次数(0无限)] [跨服(1是)]` |
| `SetOffTimer` | `SetOffTimer 索引(0-255)` |
| `DelayCall` | `DelayCall 毫秒 @触发字段` |

### 变量/运算类
| 命令 | 格式/说明 |
|------|------|
| `MOV` | `MOV 变量 值` / `MOV 变量 +N` |
| `INC` / `DEC` | `INC 变量 N` / `DEC 变量 N` |
| `MUL` | `MUL N1 N2 N3` (N1=N2*N3) |
| `DIV` | `DIV N1 N2 N3` (N1=N2/N3) |
| `PERCENT` | `PERCENT N1 N2 N3` (N1=(N2/N3)*100) |
| `CALCVAR` | `CALCVAR 类型 变量 +/- N` |
| `SAVEVAR` / `LOADVAR` | `SAVEVAR 类型 变量 文件` / `LOADVAR 类型 变量 文件` |

### 文件/文本操作类
| 命令 | 格式/说明 |
|------|------|
| `CreateFile` / `DeleteFile` | `CreateFile 文件名` / `DeleteFile 文件名` |
| `CopyFile` | `CopyFile 源 目标` |
| `AddTextList` | `AddTextList 文件 字符串` 或 `AddTextList 文件 字符串 字符串`(新格式区分大小写) |
| `DelTextList` | `DelTextList 文件 字符串` |
| `CHECKTEXTLIST` | `CHECKTEXTLIST 文件 字符串` 或 `CHECKTEXTLIST 文件 字符串 字符串`(新格式区分大小写) |
| `CheckCacheTextList` | CHECKTEXTLIST缓存版(高效) |
| `CheckContainsTextList` | 列表中是否包含被检测字符 |
| `CheckContainsTextListEx` | 被检测字符是否包含列表中某行 |
| `GETRANDOMLINETEXT` | `GETRANDOMLINETEXT 文件 变量` 随机取一行 |
| `GetCacheRandomLineText` | 缓存版随机取行 |
| `GetRandomText` | `GetRandomText 文件 变量 [行号(0随机)]` |
| `GetCacheRandomText` | 缓存版 |
| `GetRandomTexts` | `GetRandomTexts 文件 数量(最大255) 保存变量 实际数量变量` 随机取多行不重复 |
| `GetListString` | `GetListString 文件 行号 变量1 [变量2]` |
| `GetListStringEx` | `GetListStringEx 文件 行号 变量 [分隔符]` 单行多列 |
| `GetStringPos` | `GetStringPos 路径 字符串` 返回下标到N0, 9999999未找到 |
| `GetTextLineCount` | `GetTextLineCount 路径 变量` |
| `AddTextListEx` | `AddTextListEx 路径 字符串 行(0-65535)` 写入指定行 |
| `DelText` | `DelText 文件 行 [0不保留空行/1保留]` |
| `CLEARNAMELIST` | `CLEARNAMELIST 文件` |
| `CHECKNAMELIST` / `ADDNAMELIST` / `DELNAMELIST` | 人物名单操作 |
| `CHECKACCOUNTLIST` / `ADDACCOUNTLIST` / `DELACCOUNTLIST` | 账号ID操作 |
| `ADDIPLIST` / `DELIPLIST` | IP列表操作 |
| `DELGUILDLIST` | 删除行会名 |
| `WriteConfigFileItem` | `WriteConfigFileItem 路径 区 节 值` 写INI |
| `ReadConfigFileItem` | `ReadConfigFileItem 路径 区 节 变量` 读INI |
| `DelConfigFileSection` / `DelConfigFileItem` | 删除INI区/项 |
| `WriteCacheConfigFileItem` / `ReadCacheConfigFileItem` | 缓存版(高效) |

### OK对话框类
| 命令 | 格式/说明 |
|------|------|
| `OPENUPGRADEDLG` | `OPENUPGRADEDLG 名称` 打开可放物品对话框 |
| `TAKEDLGITEM` | 收回OK框物品 |
| `RECLAIMITEM` | 返回OK框物品到包裹, 点击OK触发[@UpgradeDlgItem] |
| `SETCURRNPC` | `SETCURRNPC ID` 999999996=QM/999999999=QF/999999993=任务NPC |
| `OPENMERCHANTBIGDLG` | `OPENMERCHANTBIGDLG WIL序号 图片序号 可移动(0,1) 位置(0-4) X Y 显示关闭(0,1) 关闭X 关闭Y [独立(0,1)]` |
| `OpenBigDialogBox` | `OpenBigDialogBox WIL编号 图片编号` |
| `CloseBigDialogBox` | 关闭大对话框 |

### 地图/场景类
| 命令 | 格式/说明 |
|------|------|
| `CLEARITEMMAP` | `CLEARITEMMAP 地图 X Y 范围 [物品名/*所有]` |
| `CHECKMAPNAME` | `CHECKMAPNAME 地图` 检测当前地图 |
| `SCREENEFFECT` / `CLEARSCREENEFFECT` | `SCREENEFFECT (0自己/1全服)` 屏幕特效 |

### 特效/声音类
| 命令 | 格式/说明 |
|------|------|
| `PLAYEFFECT` | `PLAYEFFECT WIL序号 开始张 播放张 次数 速度(毫秒) 绘制模式(0特效/1普通) X Y 顺序(0上/1下) [ID组]` |
| `CLEARPLAYEFFECT` | `CLEARPLAYEFFECT [ID组]` |
| `PlayWindowEffect` | `PlayWindowEffect 窗口(0-9) 效果(0-7) WIL序号 开始图 结束图 间隔毫秒 次数 X Y 绘制模式|最上层` |
| `PLAYSOUND` | `PLAYSOUND 文件 循环 模式(0自己/1全服/2同地图/4同屏)` |
| `PlayMusic` / `PlayMP3` | `PlayMP3 路径或URL` 自动搜索客户端Music目录 |

### 行会类
| 命令 | 格式/说明 |
|------|------|
| `ADDGUILDMEMBER` | `ADDGUILDMEMBER 行会名 [人物名]` 空则自己加入 |
| `ADDTOCASTLEWARLIST` | `ADDTOCASTLEWARLIST 城堡 行会(或*所有) [天数]` |
| `CHANGEGUILDMEMBERMAXLIMITCOUNT` | `CHANGEGUILDMEMBERMAXLIMITCOUNT [行会/SELF] (=,+,-) 数量` |
| `AddGuildMemberCount` | `AddGuildMemberCount (=,+,-) 数量(0-1000)` 老大专用 |
| `GuildSaveToList` | `GuildSaveToList 路径 行会名 成员变量或常量` 导出在线成员 |

### 职业/外观/其他
| 命令 | 格式/说明 |
|------|------|
| `CHANGEJOB` | `CHANGEJOB Warrior/Wizard/Taoist` |
| `CHANGEGENDER` | `CHANGEGENDER (男0/女1)` |
| `HAIRSTYLE` | `HAIRSTYLE 类型编号` |
| `HCALL` | `HCALL 角色名 @标签` 远程调用角色脚本 |
| `GMEXECUTE` | `GMEXECUTE 命令` |
| `MESSAGEBOX` | `MESSAGEBOX 内容` 或 `MESSAGEBOX 内容 按钮1 按钮2 @标签1 @标签2` |
| `OPENURL` | `OPENURL 地址 [0游戏外/1游戏内]` |
| `DIABLESOFTCLOSE` | 禁止小退(仅[@SoftClose]下) |
| `CLEARPASSWORD` | 清除仓库密码 |
| `DELMARRY` | 清除结婚信息 |
| `RestRenewLevel` | 清除转生数据 |
| `OpenUrl` / `WebBrowser` | `OpenUrl 地址 [0外/1内]` / `WebBrowser 地址` |

### GOTOLABEL 触发 (对其他玩家触发脚本)
| 模式 | 说明 |
|------|------|
| 0 | 小组成员触发 |
| 1 | 行会成员触发 |
| 2 | 当前地图所有人 |
| 3 | 指定范围(X Y 范围) |
| 4 | 当前地图人物 |
| 5 | 指定范围不同攻击模式 |
| 6 | 小组成员范围 |
| 7 | 行会成员范围 |
| 8 | 当前地图范围 |
| `GOTOLABELEX` | `GOTOLABELEX 模式 X Y 范围 来源(0QF/1NPC) 字段` |

## 脚本检测命令完整参考 (约95条)

### 一、人物基础属性
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKLEVELEX` | `CHECKLEVELEX 符号(=,>,<?,?) 等级(1-65535)` | 等级检测 |
| `CHECKEXP` | `CHECKEXP 符号 经验值(1-4000000000)` | 经验值检测 |
| `CHECKRENEWLEVEL` | `CHECKRENEWLEVEL 符号 转生等级(1-255)` | 转生等级 |
| `CHECKDC` / `CHECKMC` / `CHECKSC` | `CHECKDC 符号 下限 符号 上限` | 攻击/魔法/道术(上下限) |
| `CHECKHP` / `CHECKMP` | `CHECKHP 符号 下限 符号 上限` | HP/MP值 |
| `CHECKHPPER` | `CHECKHPPER 符号 百分比(0-100) 模式(0百分/1千分)` | 血量百分比 |
| `CHECKMPPER` | `CHECKMPPER 符号 百分比(0-100) 模式(0百分/1千分)` | 魔法百分比 |
| `CHECKBONUSPOINT` | `CHECKBONUSPOINT 符号 点数` | 附加属性点 |
| `CHECKCREDITPOINT` | `CHECKCREDITPOINT 符号 声望(1-255)` | 声望点 |
| `CHECKPKPOINTEX` | `CHECKPKPOINTEX 符号 数量` | PK值 |
| `checkjob` | `checkjob warrior/wizard/taoist` | 职业检测 |

### 二、货币/点数
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKGAMEPOINT` | `CHECKGAMEPOINT 符号 点数` | 游戏点数(泡点) |
| `CHECKGAMEGOLD` | `CHECKGAMEGOLD 符号 点数` | 游戏币/元宝 |
| `CHECKGAMEDIAMOND` | `CHECKGAMEDIAMOND 符号 点数` | 金刚石 |
| `CHECKGAMEGIRD` | `CHECKGAMEGIRD 符号 点数` | 灵符 |
| `CHECKGAMEGLORY` | `CHECKGAMEGLORY 符号 点数` | 荣誉值 |
| `CHECKPAYMENT` | `CHECKPAYMENT 参数` | 是否付费 |

### 三、人物状态
| 命令 | 格式 | 说明 |
|------|------|------|
| `ISADMIN` | 无参数 | 是否管理员 |
| `ISNEWHUMAN` | 无参数 | 是否新人(仅首次) |
| `CheckOffline` | 无参数 | 是否离线挂机 |
| `checkonline` | `checkonline` / `H.checkonline` / `角色名.checkonline` / `S1.checkonline` | 是否在线 |
| `CHECKSHOPSTALLSTATUS` | 无参数 | 是否在摆摊 |
| `CHECKMAPMOVE` | `CHECKMAPMOVE 地图 X Y` | 坐标是否可达 |
| `ISONMAP` | `ISONMAP 地图名` | 是否在某地图 |
| `CHECKMAPNAME` | `CHECKMAPNAME 地图名` | 当前地图名检测 |
| `INSAFEZONE` | 无参数 | 是否在安全区 |
| `ONLINELONGMIN` | `ONLINELONGMIN 符号 分钟` | 在线时长(分) |
| `CHECKREVIVAL` | `CheckRevival [变量]` | 是否允许复活(可选存剩余时间) |
| `CheckNotDropItemCount` | `CheckNotDropItemCount 符号 次数` | 死亡不掉装备次数 |
| `IsDupMode` | `IsDupMode 模式(0全部/1仅人物)` | 位置是否重叠 |
| `CheckSuckDamage` | `CheckSuckDamage 符号 数量(1-20亿)` | 伤害吸收值 |

### 四、称号
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKFENGHAOCOUNT` | `CHECKFENGHAOCOUNT 符号 数量(0-30)` | 称号数量 |
| `CHECKTITLE` | `CHECKTITLE 称号名` | 是否拥有某称号 |

### 五、装备/物品
| 命令 | 格式 | 说明 |
|------|------|------|
| `checkitem` | `checkitem 物品名 数量 [部分匹配0/1] [检测改名0/1]` | 背包物品 |
| `CHECKITEMW` | `CHECKITEMW 物品名 数量` | 是否佩戴物品 |
| `CHECKUSEITEM` | `CHECKUSEITEM 位置(0-28,30-47)` | 指定位置是否有物品 |
| `CHECKITEMTYPE` | `CHECKITEMTYPE 位置 物品类型` | 位置物品类型 |
| `CHECKBAGSIZE` | `CHECKBAGSIZE 数量` | 背包空格数 |
| `CheckItemBind` | `CheckItemBind 位置(-1~28,30~47)` | 装备是否已绑定 |
| `CheckItemState` | `CheckItemState 位置 项目(0-6)` | 绑定状态(0禁扔/1禁交易/2禁存/3禁修/4禁出售/5禁爆/6丢弃消失) |
| `CHECKNEWITEMVALUE` | `CHECKNEWITEMVALUE 位置 属性(0-16) 符号 值` | 元素属性(0暴击/1攻伤/2物减/3魔减/4忽视防/5反弹/6增目标暴/7体力/8魔力/9怒气/10合击/11防暴/12防麻/13防复活/14防毒/15防冰/16防蛛) |
| `CHECKITEMADDVALUE` | `CHECKITEMADDVALUE 位置 属性位(0-14) 符号 值 变量` | 附加属性值(盔甲0防1魔御2攻3魔4道; 武器0DC2/1MC2/2SC2/3幸运/4诅咒/5准确/6攻速/7强度/14持久) |
| `GetItemAddValue` | `GetItemAddValue 位置 属性位 变量` | 获取附加属性值到变量 |

### 六、技能
| 命令 | 格式 | 说明 |
|------|------|------|
| `CheckMagicName` | `CheckMagicName 魔法名` | 是否学会魔法 |
| `CHECKTRANPOINT` | `CHECKTRANPOINT 技能名 符号 点数` | 技能修炼点数 |

### 七、对面人物
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKPOSELEVEL` | `CHECKPOSELEVEL 符号 等级(1-65535)` | 对面等级 |
| `CHECKPOSEGENDER` | `CHECKPOSEGENDER MAN/WOMAN` | 对面性别 |
| `CHECKPOSEDIR` | `CHECKPOSEDIR [1同性别/2异性别]` | 对面位置(需面对面) |

### 八、宝宝
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKSLAVENAME` | `CHECKSLAVENAME 宝宝名` | 宝宝名字 |
| `CheckKillSlaveName` | `CheckKillSlaveName 怪物名` | 被杀死的宝宝名字(仅直属) |

### 九、登录/账号/IP
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKACCOUNTLIST` | `CHECKACCOUNTLIST 文件.txt` | 登录账号检测 |
| `CHECKIPLIST` | `CHECKIPLIST 文件.txt` | 登录IP检测 |
| `CHECKACCOUNTIPLIST` | `CHECKACCOUNTIPLIST 文件.txt` | 账号IP匹配(格式: 账号 IP) |
| `CHECKNAMEIPLIST` | `CHECKNAMEIPLIST 文件.txt` | 角色名IP匹配 |
| `CHECKNAMELISTPOSITION` | `CHECKNAMELISTPOSITION 文件 符号 数量 P0` | 列表中排名(P0存排名) |

### 十、会员系统
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKMEMBERTYPE` | `CHECKMEMBERTYPE 符号 类型(1-65535)` | 会员类型 |
| `CHECKMEMBERLEVEL` | `CHECKMEMBERLEVEL 类型 符号 等级(1-65535)` | 会员等级 |
| `CHECKUSERDATE` | `CHECKUSERDATE 文件 符号 天数 p0 p1` | 会员时间(p0已用天数,p1剩余天数) |
| `CHECKNAMEDATETIMELIST` | `CHECKNAMEDATETIMELIST 文件 删除(0/1) S变量 N天 N时 N分` | 精确会员剩余时间 |

### 十一、行会/沙城
| 命令 | 格式 | 说明 |
|------|------|------|
| `HAVEGUILD` | 无参数 | 是否加入行会 |
| `ISGUILDMASTER` | 无参数 | 是否行会老大 |
| `CHECKOFGUILD` | `CHECKOFGUILD 行会名` | 行会名称检测 |
| `CHECKGUILDLIST` | `CHECKGUILDLIST 文件.txt` | 行会是否在列表 |
| `CheckGuildMemberCount` | `CheckGuildMemberCount 符号 数量` | 行会成员人数 |
| `CHECKGUILDMEMBERMAXLIMITCOUNT` | `... 行会名/SELF 符号 数量` | 行会可容纳成员数 |
| `ISCASTLEGUILD` | 无参数 | 是否沙城成员 |
| `ISCASTLEMASTER` | 无参数 | 是否沙城老大 |
| `CHECKCASTLEDOOR` | `CHECKCASTLEDOOR 损坏/开启/关闭` | 沙城门状态 |
| `CASTLECHANGEDAY` | `CASTLECHANGEDAY 符号 天数` | 沙城占领天数(需沙城NPC) |
| `CASTLEWARAY` | `CASTLEWARAY 符号 天数` | 上次攻城天数(需沙城NPC) |
| `CHECKUNDERWAR` | `CHECKUNDERWAR 城堡名` | 是否正在攻城 |
| `CheckInWarArea` | 无参数 | 是否在攻城区域 |
| `CHECKCASTLEWARAREA` | `CHECKCASTLEWARAREA 城堡名` | 是否进入攻城范围 |

### 十二、国家
| 命令 | 格式 | 说明 |
|------|------|------|
| `CheckNational` | `CheckNational 编号(0-100)` | 国家编号(0=未加入) |
| `CheckNationHumCount` | `CheckNationHumCount 符号 人数` | 国家人数 |
| `CheckNationCredit` | `CheckNationCredit 符号 数值` | 国家荣誉值 |

### 十三、组队
| 命令 | 格式 | 说明 |
|------|------|------|
| `ISGROUPMASTER` | 无参数 | 是否组长 |
| `CHECKGROUPMEMBERCOUNT` | `CHECKGROUPMEMBERCOUNT 符号 数量` | 组队人数 |

### 十四、地图/怪物
| 命令 | 格式 | 说明 |
|------|------|------|
| `CheckMapHumanCount` | `CheckMapHumanCount 地图 符号 数量` | 地图人数 |
| `CheckMonMap` | `CheckMonMap 地图 数量` | 地图怪物数 |
| `CheckMapMonCount` | `CheckMapMonCount 地图 符号 数量 [排除宝宝0/1]` | 怪物数(可选排除宝宝) |
| `CheckMapSameMonCount` | `CheckMapSameMonCount 地图 怪名 符号 数量 [忽略数字0/1]` | 同名怪数量 |
| `CHECKRANGEMONCOUNTEX` | `CHECKRANGEMONCOUNTEX 地图 怪名 X Y 范围 符号 数量` | 范围内怪物数 |
| `CheckRangeHumCount` | `CheckRangeHumCount 地图 X Y 范围 符号 数量` | 范围内人数 |

### 十五、战斗/目标
| 命令 | 格式 | 说明 |
|------|------|------|
| `CHECKCURRTARGETRACE` | `CHECKCURRTARGETRACE 符号 Race值` | 目标类型(0=人,1=英雄,60=人形怪); 仅死亡/攻击触发 |

### 十六、字符串/文件
| 命令 | 格式 | 说明 |
|------|------|------|
| `CheckContainsText` | `CheckContainsText 子串 完整串` | 串是否包含子串 |
| `CompareText` | `CompareText 串1 串2` | 字符串比较(不区分大小写) |
| `CHECKTEXTLIST` | `CHECKTEXTLIST 文件 串` 或 `CHECKTEXTLIST 文件 串1 串2` | 文件中是否有字符串(新格式区分大小写) |
| `CheckContainsTextList` | `CheckContainsTextList 文件 关键字` | 文件某行包含关键字 |
| `CheckContainsTextListEx` | `CheckContainsTextListEx 文件 完整串` | 完整串包含文件某行关键字 |
| `GetStringPosEx` | `GetStringPosEx 路径 串 变量(行号) 变量(完整行)` | 包含检测+取行号和内容 |
| `FileExists` | `FileExists 文件路径` | 文件是否存在 |

### 十七、逻辑
| 命令 | 格式 | 说明 |
|------|------|------|
| `RANDOMEX` | `RANDOMEX 分子 分母` | 随机概率(50/100=50%) |
| `NOT` | `NOT 检测命令 参数` | 取反,支持H.前缀 |
| `EQUAL` / `NOT EQUAL` | `EQUAL 变量 值` | 变量比较 |

> 统一控制符: `=` 等于, `>` 大于, `<` 小于, `?` 不等于

## 装备位置代码
| 位置 | 说明 | 位置 | 说明 |
|------|------|------|------|
| 0 | 盔甲 | 15 | 马牌 |
| 1 | 武器 | 16 | 盾牌 |
| 2 | 照明物 | 17-28 | 时装(衣服/武器/项链/头盔/手镯x2/戒指x2/勋章/腰带/鞋子/宝石) |
| 3 | 项链 | 30-41 | 首饰盒装备x12 |
| 4 | 头盔 | 42-47 | 首饰盒装备x6 |
| 5-6 | 右/左手镯 | - | - |
| 7-8 | 右/左戒指 | - | - |
| 9 | 护身符 | - | - |
| 10 | 腰带 | - | - |
| 11 | 鞋子 | - | - |
| 12 | 宝石 | - | - |
| 13 | 斗笠 | - | - |
| 14 | 军鼓 | - | - |
| -1 | OK框中物品 | - | - |

## 服务端配置文件详解

### MapInfo.txt 地图配置
```
[地图编号 地图名称] 标志位1 标志位2 ...
; 标志位: FIGHT, NORECALL, NORECONNECT(地图号), NODRUG, DAY 等
; 镜像地图: [01|0 比奇-1] (用0的地图数据镜像01)
; 连接点: 地图号 X,Y 范围 -> 目标地图号 X,Y
```

### MonGen.txt 刷怪配置
```
地图 X Y 怪物名 范围 数量 间隔 集中机率#刷新模式#显示倒计时 颜色 触发QF字段 内功怪 国家 同国可攻击
; 刷新模式: 0=传统, 1=死后计时
; 数量支持G变量: <$STR(G111)>
; 倒计时: 0不显示, 1显示
; 刷出时可触发QF脚本字段
```

### 爆率配置 (MonItems目录)
```
; 传统格式: 几率 物品名 (数量)
1/1 金币 10000
1/4 天尊头盔

; 新格式1: #CHILD 几率 RANDOM (确保只爆一件)
#CHILD 1/1 RANDOM
(
1/1 天尊头盔
1/1 天尊项链
)

; 新格式2: #CHILD 几率 (子爆率有效)
#CHILD 1/2
(
1/100 火球术
1/1 治愈术
)

; 可用#CALL调用外部爆率脚本
#CALL [\爆率系统\基础爆率.txt] @药水
```

### 脚本调用
```脚本
#CALL [\NPC\shili.txt] @Settings
; 根目录在QuestDiary下
; 被调用文件需用 {} 包裹代码块
[@Settings]
{
#IF
#ACT
  sendmsg 7 调用成功
}
```

## 地图标志位与参数(完整)
| 参数 | 说明 |
|------|------|
| `FIGHT` | 允许PK |
| `FIGHT2` / `FIGHT3` / `FIGHT4` | PK模式变体(不加PK/不掉装备等) |
| `NORECALL` | 禁止回城 |
| `NOGUILDRECALL` | 禁止行会召唤 |
| `NODEARRECALL` | 禁止夫妻召唤 |
| `NOMasterRECALL` | 禁止师徒召唤 |
| `NORECONNECT(X)` | 断线重连传到X地图 |
| `NODRUG` | 禁止吃药 |
| `NODEAL` | 禁止交易 |
| `QUIZ` | 禁止喊话 |
| `NORANDOMMOVE` | 禁止瞬移 |
| `NOPOSITIONMOVE` | 禁止坐标移动 |
| `NOHORSE` | 禁止骑马 |
| `MISSION` | 禁止物品技能,宝宝消失 |
| `NIGHT` / `DARK` / `DAY` | 夜晚/黑暗/白天 |
| `ONKILLMON` | 杀死怪物触发(需MapQuest.txt配置) |
| `HITMON(@触发)` | 攻击怪物触发 |
| `EXPRATE(100)` | 杀怪经验倍数(除以100) |
| `INCGAMEPOINT` | 泡点功能 |
| `RUNMON` / `RUNHUMAN` | 允许穿怪/人 |
| `ALLOWUSEMYSHOP` | 允许摆摊 |
| `REVIVAL(X:N)` | 复活次数和清零间隔 |
| `NODROPUSEITEMS` | 死亡不掉身上物品 |
| `DELDROPITEM` | 死亡掉落物品立即消失 |
| `SAYLEVEL(等级)` | 限制说话等级 |
| `NOMANNOMON(60)` | 无人N秒自动清理怪物 |
| `TimeMap(地图\|分钟\|显示\|@返回)` | 限制地图内时间 |
| `SECRET(参数\|名字\|衣服\|武器)` | 浑水摸鱼模式 |
| `NODROPITEMFILENAME(文件)` | 禁止扔指定物品 |
| `NOTALLOWUSEITEMS(物品)` | 禁止使用物品 |
| `NOTALLOWUSEMAGIC(技能)` | 禁止使用技能 |
| `THUNDER(N)` / `LAVA(N)` | 闪电/岩浆效果 |
| `WEATHER1` / `WEATHER2` / `WEATHER3` | 天气特效 |
| `lightcolor(R\|G\|B)` | 地图光效 |
| `CHECKQUEST(Q001)` | 进入执行任务脚本 |
| `MUSIC(Wav\xx.mp3)` | 播放音乐 |
| `DECHP(N)` / `INCHP(N)` | 自动减/加HP |
| `DECGAMEGOLD` / `INCGAMEGOLD` | 自动减/加游戏币 |
| `NOUSESTORAGE` | 禁止使用仓库 |
| `NOHEROPROTECT` / `NOCALLHERO` | 禁止英雄守护/召唤 |

## 已实现功能
1. **按小时计费点卡系统** (2026-03-22)
   - 7天点卡: Idx=10345, StdMode=2, Anicount=100
   - 欠费等待区: 600.map
   - 50号定时器每小时检测

2. **大逃杀模式** (已存在于QManage.txt)
   - 60号定时器(30秒/次): 主逻辑，5个阶段共30分钟
   - 61号定时器(10秒/次): 毒圈警告
   - 副本地图BRTL, 变量G300/G301/G302控制状态

## 文件编码
- 脚本文件必须使用 **ANSI编码** (非UTF-8)
- 物品数据库 cfg_item.xls 是Excel格式

## 土城安全区
- 地图ID: 3
- 坐标: 330 330

## 帮助文档目录结构
```
chm_extract/游戏引擎反外挂系统/
├── 功能操作命令/     (~190文件) 脚本执行命令
├── 脚本检测命令/     (~90文件)  #IF条件检测
├── 服务端文本结构/   (~64文件)  配置文件说明
├── 特殊触发功能/     (~42文件)  触发标签
├── 新增功能/         (~144文件) 引擎新特性
├── 游戏功能详解/     (~92文件)  系统功能说明
├── 兼容HeroM2/       (~80文件)  HeroM2兼容
├── 英雄功能操作/     (~32文件)  英雄系统
├── 新NPC界面写法/    (~25文件)  NPC UI
├── DB数据库资料/     (~14文件)  数据库说明
├── 部分脚本实例/     (~26文件)  脚本示例
├── 常见问题解答/     (~32文件)  FAQ
└── 其他相关资料/     (~17文件)  其他
```

## DB数据库字段参考 (cfg_item.xls)
**关键列**: Idx(物品ID,建议10000起), Name, StdMode(分类), Anicount(触发/打包Shape), Looks(图标), DuraMax(持久,1000=1点), Shape(外观/特殊功能), Need(限制类型:0级/1攻/2魔/3道), NeedLevel(限制数值), Source(强度,-1~-50神圣), Reserved(特殊功能:8死亡消失/12不可取下), Job(穿戴职业需求)

**StdMode物品分类**: 0=药品, 1=食物, 2=(触发), 3=卷类, 4=技能书, 5=单手武器, 6=双手武器, 10=男衣, 11=女衣, 15=头盔, 16=斗笠, 30=勋章, 31=触发物品, 40=背包, 41=首饰盒, 42=制作原料/镶嵌, 46=项链, 52=腰带, 66-89=时装系列

**极品属性(武器)**: 0=DC2, 1=MC2, 2=SC2, 3=幸运, 4=诅咒, 5=准确, 6=攻击速度, 7=强度

**怪物DB(cfg_monster)关键字段**: Race(怪物AI:81自动攻击/82毒液/90麻痹/92瞬移/95地下爬出/100召唤骷髅/107全屏麻痹), RaceImg(攻击特效:15抛斧/21电火花/40击电/45射箭/49丢火球), MP=伤害封顶

## 动态镜像副本
```
AddMirrorMap 原地图 新地图编号 新地图名 有效时长(秒) 返回地图 小地图编号
DelMirrorMap 地图名
CheckMirrorMap 地图名
MirrorMapTime 地图名 [时间]
AddMapGate 连接 地图1 X Y 方向 地图2 X Y 秒数
```

## 货币系统
| 系统变量 | 说明 | 命令 |
|----------|------|------|
| `<$GAMEGOLD>` | 游戏币/元宝 | CHANGEGOLD +/- N |
| `<$GAMEPOINT>` | 游戏点数 | CHECKGAMEPOINT |
| `<$GAMEDIAMOND>` | 金刚石 | CHECKGAMEDIAMOND |
| `<$GAMEGIRD>` | 灵符 | CHECKGAMEGIRD |
| `<$GAMEGLORY>` | 荣誉 | CHECKGAMEGLORY |

## 英雄系统核心命令
| 命令 | 说明 |
|------|------|
| `CREATEHERO 职业 性别` | 创建英雄(0战1法2道, 0男1女) |
| `DELETEHERO` | 删除英雄 |
| `RecallHero` / `RecallHero 1` | 召唤/收回英雄 |
| `CheckHaveHero` | 检测是否有英雄 |
| `H.CHECKJOB` | 检测英雄职业 |
| `H.CHECKLEVEL` | 检测英雄等级 |
| `SetHeroSta 模式` | 改变英雄模式(0攻击/1跟随/2休息) |
| `HEROLUCK +/- N` | 调整英雄忠诚度 |
| `GetHeroMasterName 英雄名 变量` | 获取英雄主人名字 |

## NPC彩色字体与界面
```
<字体颜色/FCOLOR=69>               ; 变色文字
{FCOLOR=250}/@跳转1                 ; 点击变色
<Img:N:F:X:Y/@Label>               ; 图片按钮
<ImgEx:F:U:H:D:X:Y/@Label>         ; 三态图片(默认/悬停/按下)
<INPUTTEXT:ID:X:Y:宽:高:...>       ; 输入框(获取<$NPCINPUT(ID)>)
<ITEMBOX:N:F:M:X:Y:W:H:S:T>       ; OK框(0~17)
```

## 新NPC面板写法(需M2启用)
```
<Img|wil=NewopUI|pcimg=108|x=0|y=0|width=480|height=360|bg=1|link=@触发>
<Button|wil=NewopUI|pcnimg=140|pcmimg=140|pcpimg=143|text=按钮|x=0|y=0|link=@触发>
<Text|text=文本|color=255|size=18|x=0|y=0|link=@触发>
<EquipShow|index=0|showtips=1|x=0|y=0>                    ; 身上装备
<ItemShow|itemid=Idx|itemcount=N|showtips=1|x=0|y=0>      ; 按IDX显示
<DBItemShow|makeindex=唯一ID|showtips=1|x=0|y=0>          ; 按唯一ID显示
<ListView|children={1,2,3}|direction=1|Slider=1|x=0|y=0>  ; 滑动列表
```
主窗口ID: 2=角色面板, 4-7=状态/属性/技能/背包, 8=小地图, 41=首饰盒, 50002+=英雄面板

## 精准爆率系统
- 物品名后加`|@触发字段`如`1/10 开天|@爆开天触发`
- QF中用`ALLOWDROP 1/0`控制是否允许爆出
- `#CASE N10|1 RANDOM` 检测变量值匹配
- `#IF [N20 > 100, N20 < 110|1] RANDOM` 条件检测
