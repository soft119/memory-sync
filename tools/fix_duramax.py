#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复7天点卡的DuraMax值
"""
import openpyxl
from openpyxl import load_workbook

def fix_7day_card():
    file_path = r"D:\MirServer\Mir200\Envir\data\cfg_item.xls"
    
    try:
        # 使用openpyxl读取xlsx格式（如果是xls需要转换）
        # 先尝试用xlrd读取xls
        try:
            import xlrd
            book = xlrd.open_workbook(file_path, formatting_info=True)
            sheet = book.sheet_by_index(0)
            
            # 找到7天点卡所在行（第4行开始是数据）
            target_row = None
            for row_idx in range(3, sheet.nrows):  # 从第4行开始（索引3）
                idx_val = sheet.cell_value(row_idx, 0)
                name_val = sheet.cell_value(row_idx, 1)
                if str(name_val) == "7天点卡":
                    target_row = row_idx
                    print(f"找到7天点卡在第 {row_idx + 1} 行")
                    print(f"  Idx: {idx_val}")
                    print(f"  Name: {name_val}")
                    print(f"  当前DuraMax: {sheet.cell_value(row_idx, 9)}")  # J列是DuraMax
                    break
            
            if target_row is None:
                print("未找到7天点卡！")
                return
                
        except Exception as e:
            print(f"读取失败: {e}")
            return
        
        # 使用xlwt写入xls
        try:
            from xlutils.copy import copy
            
            # 复制原文件
            new_book = copy(book)
            new_sheet = new_book.get_sheet(0)
            
            # 修改DuraMax（第10列，索引9）
            new_sheet.write(target_row, 9, 1)  # DuraMax = 1
            
            # 保存
            new_book.save(file_path)
            print(f"\n已修复！DuraMax设置为 1")
            
        except ImportError:
            print("需要安装xlutils: pip install xlutils")
            
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    fix_7day_card()
