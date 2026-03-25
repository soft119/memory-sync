#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复7天点卡的StdMode为31（触发物品）
"""
import xlrd
from xlutils.copy import copy

def fix_7day_card():
    file_path = r"D:\MirServer\Mir200\Envir\data\cfg_item.xls"
    
    try:
        # 读取xls文件
        book = xlrd.open_workbook(file_path, formatting_info=True)
        sheet = book.sheet_by_index(0)
        
        # 找到7天点卡所在行
        target_row = None
        for row_idx in range(3, sheet.nrows):
            name_val = sheet.cell_value(row_idx, 1)
            if str(name_val) == "7天点卡":
                target_row = row_idx
                print(f"找到7天点卡在第 {row_idx + 1} 行")
                print(f"  当前StdMode: {sheet.cell_value(row_idx, 2)}")  # C列是StdMode
                print(f"  当前Anicount: {sheet.cell_value(row_idx, 5)}")  # F列是Anicount
                print(f"  当前DuraMax: {sheet.cell_value(row_idx, 9)}")  # J列是DuraMax
                break
        
        if target_row is None:
            print("未找到7天点卡！")
            return
        
        # 复制并修改
        new_book = copy(book)
        new_sheet = new_book.get_sheet(0)
        
        # 修改StdMode为31（第3列，索引2）
        new_sheet.write(target_row, 2, 31)
        print(f"\n已修复！StdMode: 2 -> 31")
        
        # 保存
        new_book.save(file_path)
        print(f"文件已保存: {file_path}")
        print(f"\n重要：请重启M2服务端使更改生效！")
            
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_7day_card()
