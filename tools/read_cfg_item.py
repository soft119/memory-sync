import xlrd

wb = xlrd.open_workbook(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls')
print('工作表:', wb.sheet_names())
ws = wb.sheet_by_index(0)
print(f'总行数: {ws.nrows}, 总列数: {ws.ncols}')
print('\n表头:')
for i in range(ws.ncols):
    print(f'列{i}: {ws.cell_value(0, i)}')

print('\n=== 药品相关物品 ===')
for row_idx in range(1, min(50, ws.nrows)):
    name = ws.cell_value(row_idx, 1)
    if '药' in str(name) or '药水' in str(name):
        print(f"\n行{row_idx}: {name}")
        for col_idx in range(min(30, ws.ncols)):
            val = ws.cell_value(row_idx, col_idx)
            if val and val != '':
                header = ws.cell_value(0, col_idx)
                print(f"  {header}: {val}")
