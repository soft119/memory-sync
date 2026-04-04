# -*- coding: utf-8 -*-
import xlrd

wb = xlrd.open_workbook('d:/MirServer/Mir200/Envir/data/cfg_item.xls', formatting_info=True)
ws = wb.sheet_by_index(0)

print("搜索包含'神水'的物品：")
print("=" * 80)
for row in range(1, min(ws.nrows, 500)):
    name = ws.cell_value(row, 1)  # xlrd 列索引从 0 开始
    if name and '神水' in str(name):
        idx = ws.cell_value(row, 0)
        stdmode = ws.cell_value(row, 6)
        anicount = ws.cell_value(row, 7)
        duramax = ws.cell_value(row, 8)
        desc = ws.cell_value(row, 5)
        print(f"Idx: {idx} | Name: {name} | StdMode: {stdmode} | AniCount: {anicount} | DuraMax: {duramax}")
        if desc:
            print(f"  描述：{desc}")
