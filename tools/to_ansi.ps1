param(
    [string]$Path = "D:\MirServer\Mir200\Envir"
)

$ansi = [System.Text.Encoding]::GetEncoding(936)
$converted = 0
$skipped = 0

function Convert-ToAnsi {
    param([string]$FilePath)
    $bytes = [System.IO.File]::ReadAllBytes($FilePath)
    if ($bytes.Length -eq 0) { return }

    $srcEncoding = $null

    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        $srcEncoding = [System.Text.Encoding]::UTF8
        Write-Host "[CONVERT] UTF-8 BOM -> GBK: $FilePath"
    }
    elseif ($bytes.Length -ge 2 -and $bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) {
        $srcEncoding = [System.Text.Encoding]::Unicode
        Write-Host "[CONVERT] UTF-16 LE -> GBK: $FilePath"
    }
    elseif ($bytes.Length -ge 2 -and $bytes[0] -eq 0xFE -and $bytes[1] -eq 0xFF) {
        $srcEncoding = [System.Text.Encoding]::BigEndianUnicode
        Write-Host "[CONVERT] UTF-16 BE -> GBK: $FilePath"
    }
    else {
        $isUtf8 = $false
        for ($i = 0; $i -lt ($bytes.Length - 2); $i++) {
            $b = $bytes[$i]
            if ($b -ge 0xC2 -and $b -le 0xDF -and $bytes[$i+1] -ge 0x80 -and $bytes[$i+1] -le 0xBF) {
                $isUtf8 = $true; break
            }
            if ($b -ge 0xE0 -and $b -le 0xEF -and ($i+2) -lt $bytes.Length) {
                if ($bytes[$i+1] -ge 0x80 -and $bytes[$i+1] -le 0xBF -and $bytes[$i+2] -ge 0x80 -and $bytes[$i+2] -le 0xBF) {
                    $isUtf8 = $true; break
                }
            }
        }
        if ($isUtf8) {
            $srcEncoding = [System.Text.Encoding]::UTF8
            Write-Host "[CONVERT] UTF-8 -> GBK: $FilePath"
        }
        else {
            Write-Host "[SKIP] Already ANSI/GBK: $FilePath"
            $script:skipped++
            return
        }
    }

    $text = $srcEncoding.GetString($bytes)
    $newBytes = $ansi.GetBytes($text)
    [System.IO.File]::WriteAllBytes($FilePath, $newBytes)
    $script:converted++
}

if (Test-Path $Path -PathType Leaf) {
    Convert-ToAnsi -FilePath $Path
}
elseif (Test-Path $Path -PathType Container) {
    $files = Get-ChildItem -Path $Path -Recurse -Include "*.txt","*.ini"
    foreach ($file in $files) {
        Convert-ToAnsi -FilePath $file.FullName
    }
}
else {
    Write-Host "Path not found: $Path"
    exit 1
}

Write-Host ""
Write-Host "Done: converted=$converted skipped=$skipped"
