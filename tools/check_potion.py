import xlrd

wb = xlrd.open_workbook(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls')
ws = wb.sheet_by_index(0)

print('=== 药品当前配置 ===\n')
for row_idx in range(1, min(40, ws.nrows)):
    name = ws.cell_value(row_idx, 1)
    if '药' in str(name):
        idx = ws.cell_value(row_idx, 0)
        stdmode = ws.cell_value(row_idx, 2)
        duramax = ws.cell_value(row_idx, 9)
        overlap = ws.cell_value(row_idx, 15)
        print(f'{name:15} | ID:{int(idx):5} | StdMode:{int(stdmode):2} | DuraMax:{int(duramax):4} | OverLap:{int(overlap)}')
