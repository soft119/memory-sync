@echo off
echo 同步记忆文件...
xcopy F:\MirServer_Memory D:\MirServer\.workbuddy\memory /E /I /Y
echo 记忆文件已同步到项目目录
pause