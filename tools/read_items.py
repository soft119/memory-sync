# -*- coding: utf-8 -*-
import xlrd

wb = xlrd.open_workbook('D:/MirServer/Mir200/Envir/data/cfg_item.xls')
ws = wb.sheet_by_index(0)

# 读取列名（第 1 行）
headers = [cell.value for cell in ws.row(0)]
print("列名:", headers)
print()

# 查找点卡物品 (Idx >= 10345)
for i in range(ws.nrows):
    row = ws.row_values(i)
    try:
        idx = int(row[0]) if row[0] else 0
        if idx >= 10345 and idx <= 10360:
            print(f"行{i}, Idx={idx}: {row}")
    except:
        continue
