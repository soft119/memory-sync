import xlrd
import xlwt

# 读取原文件
wb = xlrd.open_workbook(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls', formatting_info=False)
ws_in = wb.sheet_by_index(0)

# 创建新工作簿
wb_out = xlwt.Workbook()
ws_out = wb_out.add_sheet('Sheet7')

# 药品名称列表
potions = ['金创药(小量)', '魔法药(小量)', '金创药(中量)', '魔法药(中量)',
           '强效金创药', '强效魔法药', '疗伤药', '特殊药水']

# 复制所有数据
for row_idx in range(ws_in.nrows):
    for col_idx in range(ws_in.ncols):
        value = ws_in.cell_value(row_idx, col_idx)
        
        # 检查是否为药品行
        if row_idx > 0 and ws_in.cell_value(row_idx, 1) in potions:
            # 第10列（DuraMax）改为999
            if col_idx == 9:
                ws_out.write(row_idx, col_idx, 999)
            # 第16列（OverLap）改为1
            elif col_idx == 15:
                ws_out.write(row_idx, col_idx, 1)
            else:
                ws_out.write(row_idx, col_idx, value)
        else:
            ws_out.write(row_idx, col_idx, value)

# 保存文件（先备份原文件）
import shutil
backup_file = r'D:\MirServer\Mir200\Envir\Data\cfg_item_backup.xls'
shutil.copy2(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls', backup_file)

# 保存修改后的文件
wb_out.save(r'D:\MirServer\Mir200\Envir\Data\cfg_item.xls')

print('[OK] 备份文件已创建：cfg_item_backup.xls')
print('[OK] 药品叠堆已修改为999')
print('\n修改详情：')
print('- DuraMax: 1 → 999')
print('- OverLap: 0 → 1')
print('\n修改的药品：')
for potion in potions:
    print(f'  - {potion}')
print('\n请重启M2引擎以使更改生效！')
