# 996PC引擎脚本编码转换工具
# 将修改后的脚本文件批量转换为GBK编码

$files = @(
    "d:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt",
    "d:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        try {
            $content = Get-Content -Path $file -Raw -Encoding UTF8
            [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::GetEncoding("GBK"))
            Write-Host "OK: $file" -ForegroundColor Green
        } catch {
            Write-Host "FAIL: $file - $_" -ForegroundColor Red
        }
    } else {
        Write-Host "NOT FOUND: $file" -ForegroundColor Red
    }
}

Write-Host "`nDone! Please reload M2." -ForegroundColor Cyan
