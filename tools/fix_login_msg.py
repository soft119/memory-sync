# 修改登录脚本显示友好时间

# 读取文件
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    text = f.read()

# 旧内容
old_part = '''SENDMSG 6 您好！当前剩余游戏时间：<'''

# 新内容 - 只替换SENDMSG那一行
new_part = '''; 计算天数 = A500 / 86400
DIV N2 <$STR(A500)> 86400
; 计算剩余小时
MOV N3 <$STR(A500)>
MOD N3 86400
DIV N3 3600
; 计算剩余分钟
MOV N4 <$STR(A500)>
MOD N4 3600
DIV N4 60
SENDMSG 6 您好！当前剩余游戏时间：<'''

# 找到旧的那一行
idx = text.find('SENDMSG 6 您好！当前剩余游戏时间：')
if idx > 0:
    # 找到这一行的结束
    end_idx = text.find('\n', idx)
    old_line = text[idx:end_idx]
    print(f'找到旧行: {old_line}')
    
    # 新内容
    new_content = '''; 计算天数 = A500 / 86400
DIV N2 <$STR(A500)> 86400
; 计算剩余小时
MOV N3 <$STR(A500)>
MOD N3 86400
DIV N3 3600
; 计算剩余分钟
MOV N4 <$STR(A500)>
MOD N4 3600
DIV N4 60
SENDMSG 6 您好！当前剩余游戏时间：<$STR(N2)>天<$STR(N3)>小时<$STR(N4)>分钟'''
    
    # 替换
    text = text[:idx] + new_content + text[end_idx:]
    print('替换成功')
else:
    print('未找到旧行')

# 写回
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'w', encoding='gbk') as f:
    f.write(text)

print('文件已保存')

# 验证
with open(r'D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt', 'r', encoding='gbk') as f:
    verify = f.read()

idx = verify.find('; 计算天数')
if idx < 0:
    idx = verify.find('SENDMSG 6 您好！当前剩余游戏时间：')
end_idx = verify.find('SETONTIMER 50 3600', idx)
if end_idx > 0:
    end_idx = verify.find('\n', end_idx)
print()
print('验证新内容:')
print(verify[idx:end_idx])
