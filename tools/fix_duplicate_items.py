# -*- coding: utf-8 -*-
import xlrd
import xlwt

# 读取文件
wb_read = xlrd.open_workbook('D:/MirServer/Mir200/Envir/data/cfg_item.xls')
ws = wb_read.sheet_by_index(0)

# 创建新工作簿
wb_new = xlwt.Workbook(encoding='utf-8')
ws_new = wb_new.add_sheet('Sheet1')

# 使用字典去重（基于 Idx）
seen_idxs = set()
new_row = 0

for row_idx in range(ws.nrows):
    row_values = ws.row_values(row_idx)
    try:
        idx = int(row_values[0]) if row_values[0] else 0
    except:
        idx = -1
    
    # 如果是重复的 Idx，跳过
    if idx in seen_idxs and idx > 0:
        print("删除重复项：Idx=%d (行%d)" % (idx, row_idx))
        continue
    
    seen_idxs.add(idx)
    for col_idx in range(ws.ncols):
        ws_new.write(new_row, col_idx, row_values[col_idx])
    new_row += 1

print("\n原始行数：%d" % ws.nrows)
print("去重后行数：%d" % new_row)

# 保存文件
output_path = 'D:/MirServer/Mir200/Envir/data/cfg_item.xls'
bak_path = 'D:/MirServer/Mir200/Envir/data/cfg_item.xls.bak2'

import os, shutil
if os.path.exists(output_path):
    shutil.copy(output_path, bak_path)
    print("已备份到：%s" % bak_path)

wb_new.save(output_path)
print("[成功] 物品数据库已修复：重复项已删除")