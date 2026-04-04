content = """

;========================================
; 击杀骷髅概率刷新骷髅精灵
;========================================
[@Kill]
#IF
EQUAL %s 骷髅
RANDOM 20
#ACT
MonGenEx <$MAP> <$X> <$Y> 骷髅精灵 0 1 0 251
SENDMSG 6 触发稀有事件！骷髅精灵出现了！

"""

with open(r'D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt', 'a', encoding='gbk', newline='\r\n') as f:
    f.write(content)
print("done")
