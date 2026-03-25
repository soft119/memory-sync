import xlrd

wb = xlrd.open_workbook(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls')
ws = wb.sheet_by_index(0)

print(f'总列数: {ws.ncols}')
print('\n前25列的所有值（前5行）:')
for col_idx in range(min(25, ws.ncols)):
    print(f'\n列{col_idx}:', end=' ')
    for row_idx in range(min(5, ws.nrows)):
        try:
            val = ws.cell_value(row_idx, col_idx)
            print(val, end=' | ')
        except:
            print('-', end=' | ')
