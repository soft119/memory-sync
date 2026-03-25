# 写入 GBK 编码文件的通用脚本
# 用法: powershell -File write_gbk.ps1 -FilePath "目标路径" -Content "内容"

param(
    [string]$FilePath,
    [string]$Content
)

# 替换 \r\n 为真实换行符
$Content = $Content -replace '\\r\\n', "`r`n"

# 写入文件，使用 GBK 编码
$encoding = [System.Text.Encoding]::GetEncoding('gb2312')
[System.IO.File]::WriteAllText($FilePath, $Content, $encoding)

Write-Host "OK: $FilePath"