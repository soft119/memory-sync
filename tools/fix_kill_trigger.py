with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    lines = f.readlines()

# 删除第一个 @Kill 块（索引 642-652，包含）
del lines[642:653]

with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'w', encoding='gbk', newline='\r\n') as f:
    f.writelines(lines)

print(f"清理完成，新行数: {len(lines)}")

# 验证末尾内容
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    lines = f.readlines()
print(f'总行数: {len(lines)}')
for i, line in enumerate(lines[-15:], start=len(lines)-14):
    print(f'{i}: {line}', end='')
