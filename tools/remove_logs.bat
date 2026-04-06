@echo off
echo 正在从Git缓存中移除所有日志文件...
cd /d "d:\MirServer"

:: 从Git中移除所有日志文件
git ls-files Mir200/Log/ | while read line; do git rm --cached "%line" 2>nul; done
git ls-files Mir200/GameGuard/Log/ | while read line; do git rm --cached "%line" 2>nul; done

echo 清理完成！
pause