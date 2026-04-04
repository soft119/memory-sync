#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速将UTF-8文件转换为GBK编码
用法: python convert_to_gbk.py "文件路径"
"""

import sys
import os

def convert_file_to_gbk(file_path):
    """将文件从UTF-8转换为GBK编码"""
    if not os.path.exists(file_path):
        print(f"错误: 文件不存在 - {file_path}")
        return False
    
    try:
        # 1. 读取UTF-8内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_size = os.path.getsize(file_path)
        print(f"读取成功: {file_path}")
        print(f"  原始大小: {original_size} 字节")
        print(f"  字符数: {len(content)}")
        
        # 2. 保存为GBK编码
        with open(file_path, 'w', encoding='gbk') as f:
            f.write(content)
        
        new_size = os.path.getsize(file_path)
        print(f"转换成功: {file_path} -> GBK编码")
        print(f"  新大小: {new_size} 字节")
        print(f"  大小变化: {new_size - original_size} 字节")
        
        # 3. 验证转换结果
        with open(file_path, 'r', encoding='gbk') as f:
            test_content = f.read(300)
        
        # 检查关键系统变量
        checks = [
            ("<$KILLMONNAME>", "骷髅系列杀怪检测"),
            ("<$MAP> <$X> <$Y>", "位置变量"),
            ("RANDOM 20", "5%概率设置"),
            ("MonGenEx", "刷怪命令"),
            ("[@OnKillMob]", "杀怪触发标签"),
            ("[@StdModeFunc100]", "点卡双击标签"),
        ]
        
        print("\n系统变量检查:")
        for var, desc in checks:
            if var in test_content:
                print(f"  ✓ {var} - {desc}")
            else:
                print(f"  ✗ {var} - {desc} (未找到)")
        
        # 4. 检查中文字符是否正常
        chinese_chars = [char for char in content[:200] if '\u4e00' <= char <= '\u9fff']
        if chinese_chars:
            print(f"\n中文检查: 包含 {len(chinese_chars)} 个中文字符")
            print(f"  示例: {''.join(chinese_chars[:5])}...")
        
        return True
        
    except UnicodeDecodeError as e:
        print(f"编码错误: {e}")
        print("提示: 文件可能不是UTF-8编码，尝试自动检测...")
        
        # 尝试自动检测编码
        try:
            import chardet
            with open(file_path, 'rb') as f:
                raw_data = f.read()
            
            result = chardet.detect(raw_data)
            print(f"检测到的编码: {result['encoding']} (置信度: {result['confidence']:.1%})")
            
            # 使用检测到的编码读取
            encoding = result['encoding'] if result['encoding'] else 'gbk'
            content = raw_data.decode(encoding, errors='ignore')
            
            # 写入GBK
            with open(file_path, 'w', encoding='gbk') as f:
                f.write(content)
            
            print(f"已使用{encoding}编码读取并转换为GBK")
            return True
            
        except Exception as e2:
            print(f"自动检测失败: {e2}")
            return False
            
    except Exception as e:
        print(f"转换失败: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python convert_to_gbk.py \"文件路径\"")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print(f"开始转换: {file_path}")
    print("=" * 50)
    
    success = convert_file_to_gbk(file_path)
    
    print("=" * 50)
    if success:
        print(f"[成功] 转换完成: {file_path}")
    else:
        print(f"[失败] 转换失败: {file_path}")
        sys.exit(1)