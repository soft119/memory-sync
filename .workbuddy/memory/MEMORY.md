# 996PC引擎 项目记忆

> 详细知识体系已迁移至 Skill：`996PC引擎知识库`（C:\Users\Administrator\.workbuddy\skills\996PC引擎知识库\SKILL.md）

## 项目信息

- **项目路径**: `D:\MirServer\`
- **Git仓库**: https://gitee.com/xu-san-shi/996-pc-engine
- **记忆备份**: `F:\MirServer_Memory\`
- **同步脚本**: `D:\MirServer\tools\sync_memory_to_f.bat`
- **GBK写入工具**: `D:\MirServer\tools\write_gbk.py`
- **引擎文档**: `D:\MirServer\chm_extract\游戏引擎反外挂系统\`（810个文件）
- **命令清单**: `D:\MirServer\tools\engine_commands.txt`（915个命令）

## 土城安全区

- 地图ID: 3，坐标: 330 330

## 已实现功能

| 功能 | 关键文件 | 状态 |
|------|----------|------|
| 按小时计费点卡系统 | QF[@StdModeFunc100], QM[@OnTimer50] | ✅ |
| 欠费等待区 | 地图600, 点卡管理员NPC | ✅ |
| 7级自动学习技能 | QF[@PlayLevelUp] | ✅ |
| 新人礼包 | QF[@PlayLevelUp] ISNEWHUMAN | ✅ |

## 关键踩坑记录

1. **StdMode=31物品** 必须设置 `Shape=1` 才能触发双击脚本
2. **脚本文件编码** 必须GBK+CRLF，用 `write_gbk.py` 写入
3. **LOADVAR路径** 因脚本所在目录而不同（见Skill文档）
4. **A变量未初始化** 时不能直接用EQUAL检测，先 `MOV N1 <$STR(Axxx)>`
5. 引擎**不支持MOD**（取模），用DIV+MUL替代
6. `<$HUMAN(变量名)>` 在SENDMSG中可用，建议先MOV到N变量再显示

## 点卡系统关键配置

- 物品: `Idx=10350, Name=7天点卡, StdMode=31, Shape=1, AniCount=100, Looks=266, DuraMax=50000`
- 存储: `QuestDiary\系统功能\点卡时间.txt`
- 定时器: 50号，每3600秒，CHECKVAR>0扣除，=0传送到地图600
- 22级以下免费，升22级时立即检测

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

## 最近修改（2026-03-25）

- 修复了点卡NPC脚本LOADVAR路径问题
- 添加了法师7级自动学习火球术
- 创建了Git仓库和Gitee云端备份
- 创建了GBK写入工具 `write_gbk.py`
- 创建了记忆同步脚本 `sync_memory_to_f.bat`
- **2026-03-29**: 将整个知识体系制作成Skill（`996PC引擎知识库`）
- **2026-04-03**: 调试并确认骷髅精灵刷新脚本，#OR写法可用
