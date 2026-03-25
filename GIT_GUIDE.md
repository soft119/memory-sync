# Git 使用说明（游戏存档系统）

## Git 是什么？
就像游戏的"存档"功能：
- `git commit` = 存档
- `git log` = 查看存档列表
- `git restore` = 读档恢复

## 常用命令

### 1. 存档（保存当前进度）
```bash
git add -A                    # 选择所有修改的文件
git commit -m "修改说明"       # 创建存档
```

### 2. 查看存档列表
```bash
git log --oneline             # 简洁显示存档历史
```

### 3. 查看修改内容
```bash
git status                    # 查看哪些文件被修改了
git diff                      # 查看具体修改内容
```

### 4. 读档（恢复到之前的存档）
```bash
git restore 文件名            # 恢复单个文件
git restore .                 # 恢复所有修改
```

### 5. 云端备份（推送到 Gitee/GitHub）
```bash
# 首次设置（需要先在 Gitee 创建仓库）
git remote add origin https://gitee.com/你的用户名/仓库名.git
git push -u origin master

# 之后每次推送
git push
```

## 使用场景

### 场景1：修改脚本前先存档
```bash
git add -A
git commit -m "修改点卡功能前备份"
# 现在可以放心修改，改错了能恢复
```

### 场景2：改错了想恢复
```bash
git restore Mir200/Envir/Market_Def/QFunction-0.txt
# 文件恢复到上一次存档的状态
```

### 场景3：查看某文件的历史修改
```bash
git log --oneline 文件名
```

## 建议
- 每次重要修改前先 `git commit`
- 提交信息写清楚做了什么
- 定期 `git push` 到云端

## 当前状态
- 已初始化 Git 仓库
- 已创建第一次提交（存档点）
- 4290 个文件已保存