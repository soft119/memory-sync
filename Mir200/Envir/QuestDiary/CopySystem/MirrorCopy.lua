-- 定义主函数，注意函数名要和 Market_Def.txt 调用的对应
function MirrorCopy_Main()
    -- 在 996 中，PLAYER 全局变量代表当前对话玩家
    if not PLAYER then return end
    
    local pName = PLAYER:GetName()
    local pLevel = PLAYER:GetLevel()
    
    if pLevel < 1 then
        PLAYER:SendMsg(1, "等级不足")
        return
    end
    
    PLAYER:SendMsg(1, "测试：Lua 脚本已成功加载！")
    
    -- 这里放入之前的副本逻辑
    -- local newMap = PLAYER:CreateCopyMap("3", "TEST_"..os.time(), 600)
    -- if newMap then PLAYER:MoveMap(newMap, 50, 50) end
end