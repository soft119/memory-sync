# -*- coding: utf-8 -*-
with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'r', encoding='gbk') as f:
    content = f.read()

old_block = '''[@ItemBagButtonClick2]
;================================================
; 一键回收 - 低级书籍和沃玛以下装备
;================================================
MESSAGEBOX 是否回收全部低级装备？\\n\\n点击确定回收所有垃圾装备！\\n\\n@确认回收\\n@取消
BREAK

[@确认回收]
#IF
checkitem 火球术 1
#ACT
TAKE 火球术 1
GAMEGOLD + 10

#IF
checkitem 治愈术 1
#ACT
TAKE 治愈术 1
GAMEGOLD + 10

#IF
checkitem 基本剑术 1
#ACT
TAKE 基本剑术 1
GAMEGOLD + 10

#IF
checkitem 抗拒火环 1
#ACT
TAKE 抗拒火环 1
GAMEGOLD + 10

#IF
checkitem 施毒术 1
#ACT
TAKE 施毒术 1
GAMEGOLD + 10

#IF
checkitem 木剑 1
#ACT
TAKE 木剑 1
GAMEGOLD + 20

#IF
checkitem 匕首 1
#ACT
TAKE 匕首 1
GAMEGOLD + 30

#IF
checkitem 青铜剑 1
#ACT
TAKE 青铜剑 1
GAMEGOLD + 50

SENDMSG 6 一键回收完成！'''

new_block = '''[@ItemBagButtonClick2]
;================================================
; 一键回收 - 低级书籍和沃玛以下装备
;================================================
#SAY
是否回收全部低级装备？\n\n<确认回收/@确认回收>\n<取消/@取消>\n\n[@确认回收]
#IF
checkitem 火球术 1
#ACT
TAKE 火球术 1
GAMEGOLD + 10

#IF
checkitem 治愈术 1
#ACT
TAKE 治愈术 1
GAMEGOLD + 10

#IF
checkitem 基本剑术 1
#ACT
TAKE 基本剑术 1
GAMEGOLD + 10

#IF
checkitem 抗拒火环 1
#ACT
TAKE 抗拒火环 1
GAMEGOLD + 10

#IF
checkitem 施毒术 1
#ACT
TAKE 施毒术 1
GAMEGOLD + 10

#IF
checkitem 木剑 1
#ACT
TAKE 木剑 1
GAMEGOLD + 20

#IF
checkitem 匕首 1
#ACT
TAKE 匕首 1
GAMEGOLD + 30

#IF
checkitem 青铜剑 1
#ACT
TAKE 青铜剑 1
GAMEGOLD + 50

SENDMSG 6 一键回收完成！'''

if old_block in content:
    content = content.replace(old_block, new_block)
    print('替换成功')
else:
    print('未找到目标')

with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'w', encoding='gbk', newline='\r\n') as f:
    f.write(content)
print('Done')