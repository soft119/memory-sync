#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def fix_7day_card():
    """修复7天点卡的DuraMax为1"""
    file_path = r"D:\MirServer\Mir200\Envir\data\cfg_item.xls"
    
    try:
        # 读取Excel文件（跳过前3行注释，第4行是列名）
        print(f"正在读取: {file_path}")
        try:
            df = pd.read_excel(file_path, engine='xlrd', header=3)
        except:
            df = pd.read_excel(file_path, engine='openpyxl', header=3)
        
        print(f"共 {len(df)} 行数据")
        
        # 查找7天点卡
        found_idx = None
        for idx, row in df.iterrows():
            name = str(row.get('Name', ''))
            if '7天点卡' in name:
                found_idx = idx
                print(f"\n找到7天点卡 (第{idx+1}行):")
                print(f"  当前DuraMax: {row.get('DuraMax', 'N/A')}")
                break
        
        if found_idx is None:
            print("未找到7天点卡！")
            return
        
        # 设置DuraMax为1
        df.at[found_idx, 'DuraMax'] = 1
        print(f"  已设置DuraMax为: 1")
        
        # 保存文件
        print(f"\n正在保存...")
        try:
            df.to_excel(file_path, index=False, engine='xlrd')
        except:
            df.to_excel(file_path, index=False, engine='openpyxl')
        
        print("保存成功！")
        print("\n请重启GameCenter和M2服务端使更改生效。")
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_7day_card()
