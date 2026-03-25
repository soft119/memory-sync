#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct
import sys
import os

def parse_stditems_db(file_path):
    """解析StdItems.DB二进制文件，查找物品信息"""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # 996M2引擎StdItems.DB格式：每个物品140字节
        ITEM_SIZE = 140
        items = []
        
        for i in range(0, len(data), ITEM_SIZE):
            chunk = data[i:i+ITEM_SIZE]
            if len(chunk) < ITEM_SIZE:
                break
                
            # 解析字段（996引擎具体格式可能有变化，这是通用解析）
            try:
                # 物品名称通常在固定位置，但需要处理编码
                # 先尝试读取名称（前40字节）
                name_bytes = chunk[0:40]
                # 找到第一个0x00作为结束符
                name_end = name_bytes.find(b'\x00')
                if name_end > 0:
                    name = name_bytes[:name_end].decode('gbk', errors='ignore')
                else:
                    name = name_bytes.decode('gbk', errors='ignore')
                
                # 查找其他字段位置（需要知道996引擎的具体格式）
                # 这里简化处理：只显示包含"幻境"的物品
                if '幻境' in name:
                    print(f"找到物品: {name}")
                    print(f"  字节位置: {i}-{i+ITEM_SIZE}")
                    print(f"  原始数据: {chunk[:60].hex()}...")
                    print()
                    items.append((i, name))
                    
            except Exception as e:
                pass
        
        print(f"总共扫描了 {len(data)//ITEM_SIZE} 个物品")
        return items
        
    except Exception as e:
        print(f"解析失败: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python find_item.py <StdItems.DB路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        sys.exit(1)
    
    print(f"正在解析: {file_path}")
    items = parse_stditems_db(file_path)
    
    if items:
        print(f"找到 {len(items)} 个相关物品")
    else:
        print("未找到相关物品，尝试其他查找方法...")