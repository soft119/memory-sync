#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys
import os

def read_cfg_item_excel(file_path):
    """读取cfg_item.xls Excel文件"""
    try:
        # 读取Excel文件（可能是.xls格式，用xlrd引擎）
        print(f"正在读取Excel文件: {file_path}")
        
        # 尝试不同引擎读取
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
        except:
            try:
                df = pd.read_excel(file_path, engine='xlrd')
            except:
                # 如果都不行，尝试不指定引擎
                df = pd.read_excel(file_path)
        
        print(f"文件读取成功，共 {len(df)} 行，{len(df.columns)} 列")
        print("列名：")
        for i, col in enumerate(df.columns):
            print(f"  {i+1}. {col}")
        
        # 查找包含"幻境凭证"的行
        print("\n" + "="*60)
        print("查找'幻境凭证'或'凭证'相关物品：")
        
        # 尝试在name列中查找
        name_columns = ['name', 'Name', '物品名', '物品名称', '名称']
        found = False
        
        for col in name_columns:
            if col in df.columns:
                mask = df[col].astype(str).str.contains('幻境|凭证', na=False)
                matched_items = df[mask]
                if len(matched_items) > 0:
                    print(f"在列 '{col}' 中找到 {len(matched_items)} 个匹配物品：")
                    for idx, row in matched_items.iterrows():
                        print(f"\n【物品{idx+1}】")
                        # 显示关键列
                        for col_name in df.columns:
                            if pd.notna(row[col_name]) and str(row[col_name]).strip():
                                print(f"  {col_name}: {row[col_name]}")
                    found = True
                    break
        
        if not found:
            print("未找到'幻境凭证'，尝试显示前20行样本：")
            for idx, row in df.head(20).iterrows():
                print(f"\n行{idx+1}:")
                # 只显示非空且有值的列
                for col_name in df.columns:
                    if pd.notna(row[col_name]) and str(row[col_name]).strip():
                        print(f"  {col_name}: {row[col_name]}")
                
                # 如果有name-like列且包含"凭证"
                for col_name in df.columns:
                    if 'name' in col_name.lower() and pd.notna(row[col_name]):
                        if '凭证' in str(row[col_name]):
                            print(f"  *** 发现凭证类物品：{row[col_name]}")
        
        return df
        
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python read_item_excel.py <cfg_item.xls路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        sys.exit(1)
    
    df = read_cfg_item_excel(file_path)
    
    if df is not None:
        print("\n" + "="*60)
        print("数据统计：")
        print(f"总行数: {len(df)}")
        print(f"总列数: {len(df.columns)}")
        print(f"列名列表: {list(df.columns)}")