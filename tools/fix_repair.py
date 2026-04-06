import xlrd
from xlutils.copy import copy
import shutil

# Backup
shutil.copy(r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls', r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls.bak5')

# Open
rb = xlrd.open_workbook(r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls')
wb = copy(rb)
ws = wb.get_sheet(0)

# Find repair water (row index in sheet, col index = 1 for name, col = 8 for DuraMax)
nrows = rb.sheet_by_index(0).nrows
for row in range(1, nrows):
    name = rb.sheet_by_index(0).cell_value(row, 1)
    if isinstance(name, str) and 'Repair' in name:
        print(f'Found: {name} at row {row+1}')
        ws.write(row, 8, 500)  # 5 uses
        break

wb.save(r'D:\MirServer\Mir200\Envir\DATA\cfg_item.xls')
print('Done')