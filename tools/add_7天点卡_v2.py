#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys
import os
import shutil

def add_7day_card(file_path):
    """在cfg_item.xls中添加7天点卡物品"""
    try:
        print(f"正在读取Excel文件: {file_path}")
        
        # 备份原文件
        backup_path = file_path.replace('.xls', '_backup.xls')
        shutil.copy2(file_path, backup_path)
        print(f"已创建备份: {backup_path}")
        
        # 读取Excel文件（第三行是列标题）
        df = pd.read_excel(file_path, header=2)  # header=2表示第三行作为列标题
        
        print(f"原始数据: {len(df)} 行, {len(df.columns)} 列")
        
        # 查找最大Idx
        max_idx = df['Idx'].max()
        print(f"最大物品Idx: {max_idx}")
        
        # 新物品Idx = 最大Idx + 1
        new_idx = int(max_idx) + 1
        
        # 创建7天点卡行
        new_item = {
            'Idx': new_idx,
            'Name': '7天点卡',
            'StdMode': 2,           # 计次物品
            'Shape': 0,             # 外观
            'Weight': 0,            # 重量
            'Anicount': 100,        # 关键！对应[@StdModeFunc100]
            'Source': 0,            # 来源
            'Reserved': 0,          # 保留
            'Looks': 266,           # 幻境凭证图标ID
            'DuraMax': 1000,        # 持久度=1000 → 使用次数=1
            'Attribute': '',        # 属性
            'Need': 0,              # 使用条件
            'NeedLevel': 0,         # 使用等级
            'Price': 0,             # 价格（0=不可购买）
            'Color': 0,             # 颜色
            'OverLap': 0,           # 叠加
            'Suit': 0,              # 套装ID
            'Article': '',          # 物品规则
            'Job': '',              # 使用职业
            'effectParam': '',      # 道具特殊效果参数
            'Desc': '双击增加7天游戏时间',  # 备注
            'Expand1': '',          # 扩展参数1
            'HairShow': '',         # 发型显示
            'auctionby': '',        # 拍卖行分类
            'Insurance': ''         # 装备投保
        }
        
        # 添加新行到DataFrame
        df = pd.concat([df, pd.DataFrame([new_item])], ignore_index=True)
        
        print(f"添加后数据: {len(df)} 行")
        
        # 重新写入Excel文件（保持原始格式）
        # 需要重新创建完整的Excel文件，包含前三行注释
        
        # 先读取原始文件的前三行
        print("读取原始文件的前三行注释...")
        import xlrd
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)
        
        # 获取前三行的数据
        header_rows = []
        for i in range(3):  # 前三行
            row_data = []
            for j in range(sheet.ncols):
                cell_value = sheet.cell_value(i, j)
                row_data.append(cell_value)
            header_rows.append(row_data)
        
        # 使用xlwt写入新文件（兼容.xls格式）
        import xlwt
        new_workbook = xlwt.Workbook(encoding='utf-8')
        new_sheet = new_workbook.add_sheet('cfg_item')
        
        # 写入前三行注释
        for i, row_data in enumerate(header_rows):
            for j, cell_value in enumerate(row_data):
                new_sheet.write(i, j, cell_value)
        
        # 写入数据（从第4行开始）
        data_start_row = 3  # 0-based索引，对应Excel第4行
        
        # 获取所有列名
        columns = list(df.columns)
        
        # 写入列名（第3行，对应Excel第4行）
        for j, col_name in enumerate(columns):
            new_sheet.write(data_start_row, j, col_name)
        
        # 写入数据行
        for i, row in df.iterrows():
            row_num = data_start_row + 1 + i
            for j, col_name in enumerate(columns):
                cell_value = row[col_name]
                # 处理NaN值
                if pd.isna(cell_value):
                    cell_value = ''
                new_sheet.write(row_num, j, cell_value)
        
        # 保存新文件（临时）
        temp_file = file_path.replace('.xls', '_temp.xls')
        new_workbook.save(temp_file)
        
        # 替换原文件
        shutil.move(temp_file, file_path)
        
        print(f"文件已保存: {file_path}")
        
        print("\n" + "="*60)
        print("✅ 7天点卡添加完成！")
        print("关键属性：")
        print(f"  物品ID: {new_idx}")
        print(f"  名称: 7天点卡")
        print(f"  StdMode: 2 (计次物品)")
        print(f"  Anicount: 100 (对应[@StdModeFunc100]标签)")
        print(f"  Looks: 266 (幻境凭证图标)")
        print(f"  DuraMax: 1000 (持久度=1000 → 使用次数=1)")
        print(f"  Price: 0 (不可购买)")
        
        # 简单验证
        print("\n验证添加结果（重新读取）：")
        df_check = pd.read_excel(file_path, header=2)
        new_item_check = df_check[df_check['Name'] == '7天点卡']
        if len(new_item_check) > 0:
            print("✅ 7天点卡已成功添加到数据库！")
        else:
            print("❌ 添加失败，未找到7天点卡")
        
        return True
        
    except Exception as e:
        print(f"添加物品失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python add_7天点卡_v2.py <cfg_item.xls路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        sys.exit(1)
    
    success = add_7day_card(file_path)
    
    if success:
        print("\n✅ 7天点卡添加成功！")
        print("请重启游戏引擎或重新加载物品数据库")
    else:
        print("\n添加失败")