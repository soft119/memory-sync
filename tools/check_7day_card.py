#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys

def check_7day_card(file_path):
    """检查7天点卡的配置"""
    try:
        # 读取Excel文件（跳过前3行注释，第4行是列名）
        print(f"正在读取: {file_path}")
        try:
            df = pd.read_excel(file_path, engine='xlrd', header=3)
        except:
            df = pd.read_excel(file_path, engine='openpyxl', header=3)
        
        print(f"共 {len(df)} 行数据")
        print(f"列名: {list(df.columns)}")
        
        # 查找7天点卡
        found = False
        for idx, row in df.iterrows():
            # 检查所有可能的名称列
            for col in df.columns:
                val = str(row.get(col, ''))
                if '7天点卡' in val:
                    print(f"\n=== 找到7天点卡 (第{idx+1}行) ===")
                    # 列映射：根据996引擎cfg_item.xls格式
                    # 第4行是列名，第1列=Idx, 第2列=Name, 第4列=StdMode, 第5列=Anicount, 第7列=Looks, 第10列=DuraMax
                    print(f"  原始数据: {row.values}")
                    
                    # 按列名读取（header=3后，第4行成为列名）
                    idx = row.get('Idx', None)
                    name = row.get('Name', None)
                    stdmode = row.get('StdMode', None)
                    looks = row.get('Looks', None)
                    weight = row.get('Weight', None)
                    anicount = row.get('Anicount', None)
                    
                    duramax = row.get('DuraMax', None)
                    print(f"  Idx: {idx}")
                    print(f"  Name: {name}")
                    print(f"  StdMode: {stdmode}")
                    print(f"  Anicount: {anicount}")
                    print(f"  Looks: {looks}")
                    print(f"  Weight: {weight}")
                    print(f"  DuraMax: {duramax}")
                    
                    if pd.isna(duramax) or duramax == 0:
                        print(f"\n  [警告] DuraMax为空或0，计次物品需要设置DuraMax！")
                    
                    print(f"\n配置检查:")
                    if stdmode == 2:
                        print(f"  [OK] StdMode = 2 (正确，计次物品)")
                    else:
                        print(f"  [ERR] StdMode = {stdmode} (错误！必须是2)")
                    
                    if anicount == 100:
                        print(f"  [OK] Anicount = 100 (正确，对应[@StdModeFunc100])")
                    else:
                        print(f"  [ERR] Anicount = {anicount} (错误！必须是100)")
                    
                    found = True
                    break
            if found:
                break
        
        if not found:
            print("未找到7天点卡！")
            
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    file_path = r"D:\MirServer\Mir200\Envir\data\cfg_item.xls"
    check_7day_card(file_path)
