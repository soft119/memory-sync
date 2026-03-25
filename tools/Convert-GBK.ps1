function Convert-ToGBK {
    param([string]$filePath)
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::GetEncoding("GBK"))
}

# 转换目标文件
Convert-ToGBK "D:\MirServer\Mir200\Envir\Market_Def\系统功能\点卡测试.txt"
Write-Host "转换完成"
