@echo off
echo 正在同步记忆文件到 F 盘...
xcopy D:\MirServer\.workbuddy\memory F:\MirServer_Memory /E /I /Y
echo 同步完成！
echo 时间：%date% %time% >> F:\MirServer_Memory\sync_log.txt