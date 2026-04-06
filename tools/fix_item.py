import xlrd
from xlutils.copy import copy
import os

src = r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls'
bak = r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls.bak6'

# Read
rb = xlrd.open_workbook(bak)
wb = copy(rb)
ws = wb.get_sheet(0)

# Find '修复神水' row
name_col = 1
dura_col = 8

for row in range(rb.sheet_by_index(0).nrows):
    cell_name = rb.sheet_by_index(0).cell_value(row, name_col)
    if isinstance(cell_name, str) and '修复神水' in cell_name:
        print(f'Found: {cell_name} at row {row+1}')
        ws.write(row, dura_col, 500)
        print(f'DuraMax set to 500 (5 uses)')
        break
else:
    print('Not found')

# Save
wb.save(src)
print('Done')