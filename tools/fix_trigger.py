# -*- coding: utf-8 -*-
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    content = f.read()

# 找到损坏的触发块并替换
old_block = ''';================================================
;================================================
; 地图击杀触发 - 击杀怪物概率刷新骷髅精灵 (10%测试)
;================================================
[@OnKillMob]
MonGenEx <$MAP> <$X> <$Y> 骷髅精灵 3 1 0
RANDOM 10
#ACT
MonGenEx <\> <\> <\> 骷髅精灵 3 1 0
SENDMSG 6 提示：击杀怪物，骷髅精灵出现了！'''

new_block = ''';================================================
; 地图击杀触发 - 击杀怪物概率刷新骷髅精灵 (10%测试)
;================================================
[@OnKillMob]
#IF
RANDOM 10
#ACT
MonGenEx <$MAP> <$X> <$Y> 骷髅精灵 3 1 0
SENDMSG 6 提示：击杀怪物，骷髅精灵出现了！'''

if old_block in content:
    content = content.replace(old_block, new_block)
    print('替换成功')
else:
    print('未找到目标')

with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'w', encoding='gbk', newline='\r\n') as f:
    f.write(content)
print('Done')