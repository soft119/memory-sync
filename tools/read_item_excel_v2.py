#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys
import os

def read_cfg_item_excel(file_path):
    """读取cfg_item.xls Excel文件"""
    try:
        print(f"正在读取Excel文件: {file_path}")
        
        # 读取时不指定标题行（第一行就是数据）
        df = pd.read_excel(file_path, header=None)
        
        print(f"文件读取成功，共 {len(df)} 行，{len(df.columns)} 列")
        
        # 显示前几行数据
        print("\n" + "="*60)
        print("前5行数据：")
        for i in range(min(5, len(df))):
            print(f"\n行{i+1}:")
            row = df.iloc[i]
            for col_idx, value in enumerate(row):
                if pd.notna(value):
                    # 显示列索引和值
                    print(f"  列{col_idx+1}: {value}")
        
        # 第一行看起来是列说明
        print("\n" + "="*60)
        print("第一行（列说明）：")
        first_row = df.iloc[0]
        for col_idx, value in enumerate(first_row):
            if pd.notna(value):
                print(f"  列{col_idx+1}: {value}")
        
        # 查找包含"幻境凭证"或"凭证"的行（从第二行开始，第一行是注释）
        print("\n" + "="*60)
        print("查找'幻境凭证'或'凭证'相关物品：")
        
        found_items = []
        for i in range(1, len(df)):  # 跳过第一行
            row = df.iloc[i]
            # 列1应该是物品名称
            if pd.notna(row[0]) and isinstance(row[0], str):
                if '幻境' in row[0] or '凭证' in row[0]:
                    found_items.append((i, row))
        
        if found_items:
            print(f"找到 {len(found_items)} 个匹配物品：")
            for idx, (row_num, row) in enumerate(found_items):
                print(f"\n【物品{idx+1}】 (行{row_num+1})")
                print(f"  名称: {row[0]}")
                
                # 显示其他关键列
                # 列2: 分类 (StdMode)
                if pd.notna(row[1]):
                    print(f"  分类(StdMode): {row[1]}")
                
                # 列8: 背包显示 (Looks)
                if len(row) > 7 and pd.notna(row[7]):
                    print(f"  背包显示(Looks): {row[7]}")
                
                # 显示其他非空列
                for col_idx, value in enumerate(row):
                    if col_idx > 0 and pd.notna(value) and str(value).strip():
                        col_desc = first_row[col_idx] if col_idx < len(first_row) else f"列{col_idx+1}"
                        print(f"  {col_desc}: {value}")
        else:
            print("未找到'幻境凭证'，显示几个样本物品：")
            for i in range(1, min(20, len(df))):  # 显示前20个物品
                row = df.iloc[i]
                if pd.notna(row[0]) and isinstance(row[0], str):
                    print(f"\n行{i+1}: {row[0]}")
                    if len(row) > 1 and pd.notna(row[1]):
                        print(f"  分类: {row[1]}")
                    if len(row) > 7 and pd.notna(row[7]):
                        print(f"  背包显示: {row[7]}")
        
        return df
        
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python read_item_excel_v2.py <cfg_item.xls路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        sys.exit(1)
    
    df = read_cfg_item_excel(file_path)
    
    if df is not None:
        print("\n" + "="*60)
        print("列对应说明（根据第一行）：")
        first_row = df.iloc[0]
        for col_idx, value in enumerate(first_row):
            if pd.notna(value):
                print(f"  列{col_idx+1}: {value}")