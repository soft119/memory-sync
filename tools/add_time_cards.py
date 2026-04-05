# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os

# 读取原文件
wb_read = xlrd.open_workbook('D:/MirServer/Mir200/Envir/data/cfg_item.xls')
ws = wb_read.sheet_by_index(0)

# 创建新工作簿
wb_new = xlwt.Workbook(encoding='utf-8')
ws_new = wb_new.add_sheet('Sheet1')

# 复制所有现有行
for row_idx in range(ws.nrows):
    for col_idx in range(ws.ncols):
        cell_value = ws.cell_value(row_idx, col_idx)
        ws_new.write(row_idx, col_idx, cell_value)

# 新点卡物品数据
new_items = [
    [10351, '1 小时点卡', 31, 1, 1, 101, 0, 0, 266, 0],
    [10352, '2 小时点卡', 31, 1, 1, 102, 0, 0, 266, 0],
    [10353, '5 小时点卡', 31, 1, 1, 103, 0, 0, 266, 0],
    [10354, '1 天点卡',   31, 1, 1, 104, 0, 0, 266, 0],
]

# 添加新物品到末尾
start_row = ws.nrows
for row_idx, item in enumerate(new_items):
    for col_idx, value in enumerate(item):
        ws_new.write(start_row + row_idx, col_idx, value)

print(f"已添加 {len(new_items)} 个新点卡物品")
print("新物品列表:")
for item in new_items:
    print(f"  Idx={item[0]}: {item[1]}, AniCount={item[4]}")

# 保存文件
output_path = 'D:/MirServer/Mir200/Envir/data/cfg_item.xls'
bak_path = 'D:/MirServer/Mir200/Envir/data/cfg_item.xls.bak'

# 备份原文件
if os.path.exists(output_path):
    import shutil
    shutil.copy(output_path, bak_path)
    print(f"\n已备份原文件到：{bak_path}")

wb_new.save(output_path)
print("\n[成功] 物品数据库已更新：%s" % output_path)