# -*- coding: gbk -*-
import xlrd

wb = xlrd.open_workbook('d:/MirServer/Mir200/Envir/data/cfg_item.xls', formatting_info=True)
ws = wb.sheet_by_index(0)

print("=== 搜索所有药水类物品 ===")
for i in range(ws.nrows):
    name = str(ws.cell(i, 1).value or '')
    if '药' in name:
        idx = ws.cell(i, 0).value
        print(f"Idx={idx} | {name}")
