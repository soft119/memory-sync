#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys
import os

def find_huangjing_pingzheng(file_path):
    """查找幻境凭证或凭证类物品"""
    try:
        print(f"正在读取Excel文件: {file_path}")
        
        # 读取Excel，第三行是列标题
        df = pd.read_excel(file_path, header=2)  # header=2表示第三行作为列标题
        
        print(f"文件读取成功，共 {len(df)} 个物品")
        print(f"列名: {list(df.columns)}")
        
        # 查找Name列包含"凭证"的物品
        if 'Name' in df.columns:
            print("\n" + "="*60)
            print("查找'凭证'相关物品：")
            
            # 查找包含"凭证"的物品
            mask = df['Name'].astype(str).str.contains('凭证', na=False)
            pingzheng_items = df[mask]
            
            if len(pingzheng_items) > 0:
                print(f"找到 {len(pingzheng_items)} 个凭证类物品：")
                for idx, row in pingzheng_items.iterrows():
                    print(f"\n【{row['Name']}】 (Idx: {row.get('Idx', 'N/A')})")
                    print(f"  StdMode: {row.get('StdMode', 'N/A')}")
                    print(f"  Anicount: {row.get('Anicount', 'N/A')}")
                    print(f"  Looks: {row.get('Looks', 'N/A')}")
                    print(f"  DuraMax: {row.get('DuraMax', 'N/A')}")
            else:
                print("未找到'凭证'类物品，显示所有物品名称：")
                # 显示前50个物品名称
                names = df['Name'].dropna().unique()
                print(f"总共有 {len(names)} 个不同物品")
                print("前50个物品名称：")
                for i, name in enumerate(names[:50]):
                    print(f"  {i+1}. {name}")
        
        # 显示物品的StdMode分布
        print("\n" + "="*60)
        print("物品分类(StdMode)分布：")
        if 'StdMode' in df.columns:
            stdmode_counts = df['StdMode'].value_counts()
            for mode, count in stdmode_counts.head(20).items():
                print(f"  StdMode={mode}: {count}个物品")
        
        # 查找StdMode=2的物品（计次物品）
        print("\n" + "="*60)
        print("StdMode=2的物品（计次物品）：")
        if 'StdMode' in df.columns and 'Name' in df.columns:
            stdmode2_items = df[df['StdMode'] == 2]
            print(f"找到 {len(stdmode2_items)} 个StdMode=2的物品：")
            for idx, row in stdmode2_items.head(20).iterrows():
                print(f"  {row.get('Name', 'N/A')} - Anicount: {row.get('Anicount', 'N/A')}, Looks: {row.get('Looks', 'N/A')}")
        
        return df
        
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python find_幻境凭证.py <cfg_item.xls路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        sys.exit(1)
    
    df = find_huangjing_pingzheng(file_path)