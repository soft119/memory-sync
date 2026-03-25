# 转换QFunction-0.txt为GBK编码
$files = @(
    "D:\MirServer\Mir200\Envir\Market_Def\QFunction-0.txt",
    "D:\MirServer\Mir200\Envir\MapQuest_Def\QManage.txt"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        try {
            # 尝试以UTF-8读取
            $content = Get-Content -Path $file -Raw -Encoding UTF8
            # 以GBK保存
            [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::GetEncoding("GBK"))
            Write-Host "已转换: $file" -ForegroundColor Green
        } catch {
            Write-Host "转换失败: $file" -ForegroundColor Red
        }
    }
}

Write-Host "编码修复完成！"
pause
