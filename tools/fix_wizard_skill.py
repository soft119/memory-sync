# -*- coding: utf-8 -*-
"""
修复法师7级自动学习火球术功能
"""

file_path = r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt'

# 读取文件
with open(file_path, 'rb') as f:
    content = f.read()

# 解码 GBK
text = content.decode('gbk', errors='replace')
lines = text.split('\r\n')

# 找到道士7级学习治愈术的位置，在后面插入法师7级学习火球术
new_lines = []
i = 0
while i < len(lines):
    new_lines.append(lines[i])
    
    # 找到道士7级治愈术的结束位置（第91行 SENDMSG 0 之后）
    if i == 90 and 'SENDMSG 0' in lines[i] and '治愈术' in lines[i]:
        # 插入法师7级学习火球术
        new_lines.append('')
        new_lines.append('#IF')
        new_lines.append('checkjob wizard')
        new_lines.append('CHECKLEVELEX = 7')
        new_lines.append('#ACT')
        new_lines.append('ADDSKILL 火球术 3')
        new_lines.append('SENDMSG 6 恭喜！你学会了火球术（3级）！')
        new_lines.append('SENDMSG 0 玩家「<$USERNAME>」升到7级，学会了火球术！')
        print(f'在第 {i+1} 行后插入法师7级学习火球术')
    
    i += 1

# 重新组合
new_text = '\r\n'.join(new_lines)

# 编码为 GBK
new_content = new_text.encode('gbk', errors='replace')

# 写入文件
with open(file_path, 'wb') as f:
    f.write(new_content)

print(f'文件已更新: {file_path}')
print(f'原行数: {len(lines)}, 新行数: {len(new_lines)}')