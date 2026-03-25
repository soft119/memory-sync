[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$dir = "d:\MirServer\chm_extract\游戏引擎反外挂系统\功能操作命令"
$outFile = "d:\MirServer\chm_extract\all_commands_htm.txt"
$files = Get-ChildItem -Path $dir -Include "*.htm","*.html" -Recurse
$output = ""
foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw -Encoding Default -ErrorAction SilentlyContinue
    if ($content) {
        $output += "===FILE:" + $f.Name + "===" + "`n" + $content + "`n"
    }
}
[System.IO.File]::WriteAllText($outFile, $output, [System.Text.Encoding]::UTF8)
Write-Host "Done. Total files processed: $($files.Count)"
