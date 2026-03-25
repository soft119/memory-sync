# 996PC引擎 - 复制地图文件到客户端
# 解决自定义地图黑屏问题

param(
    [Parameter(Mandatory=$false)]
    [string]$ClientPath = ""
)

$ServerMapPath = "d:\MirServer\Mir200\Map"

# 自动检测常见客户端路径
$CommonPaths = @(
    "C:\Program Files (x86)\盛大网络\热血传奇",
    "C:\Program Files\盛大网络\热血传奇",
    "D:\热血传奇",
    "D:\传奇客户端",
    "D:\MirClient",
    "D:\996M2_debug",
    "D:\996M2"
)

function Find-ClientPath {
    Write-Host "Searching for client directory..." -ForegroundColor Yellow
    
    foreach ($path in $CommonPaths) {
        if (Test-Path $path) {
            $mapPath1 = Join-Path $path "Map"
            $mapPath2 = Join-Path $path "dev\scene\map"
            
            if (Test-Path $mapPath1 -PathType Container) {
                Write-Host "Found client: $path (Map folder)" -ForegroundColor Green
                return $path, "Map"
            }
            elseif (Test-Path $mapPath2 -PathType Container) {
                Write-Host "Found client: $path (dev/scene/map folder)" -ForegroundColor Green
                return $path, "DevScene"
            }
        }
    }
    
    return $null, $null
}

function Copy-MapFiles {
    param($ClientPath, $MapType)
    
    if ($MapType -eq "Map") {
        $targetPath = Join-Path $ClientPath "Map"
    } else {
        $targetPath = Join-Path $ClientPath "dev\scene\map"
    }
    
    Write-Host "`nTarget: $targetPath" -ForegroundColor Cyan
    
    if (!(Test-Path $targetPath)) {
        New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
        Write-Host "Created directory: $targetPath" -ForegroundColor Yellow
    }
    
    $mapFiles = Get-ChildItem -Path $ServerMapPath -Filter "*.map"
    $copied = 0
    $skipped = 0
    
    Write-Host "`nCopying map files..." -ForegroundColor Yellow
    
    foreach ($file in $mapFiles) {
        $targetFile = Join-Path $targetPath $file.Name
        
        if (Test-Path $targetFile) {
            $sourceSize = $file.Length
            $targetSize = (Get-Item $targetFile).Length
            
            if ($sourceSize -eq $targetSize) {
                Write-Host "  [Skip] $($file.Name)" -ForegroundColor Gray
                $skipped++
                continue
            }
        }
        
        Copy-Item -Path $file.FullName -Destination $targetFile -Force
        Write-Host "  [Copy] $($file.Name)" -ForegroundColor Green
        $copied++
    }
    
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "Done!" -ForegroundColor Green
    Write-Host "  Copied: $copied files" -ForegroundColor Green
    Write-Host "  Skipped: $skipped files" -ForegroundColor Gray
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "`nPlease restart client and test." -ForegroundColor Yellow
}

# Main
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  996PC Engine Map Copy Tool" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($ClientPath) {
    if (Test-Path $ClientPath) {
        $mapPath1 = Join-Path $ClientPath "Map"
        $mapPath2 = Join-Path $ClientPath "dev\scene\map"
        
        if (Test-Path $mapPath1 -PathType Container) {
            Copy-MapFiles -ClientPath $ClientPath -MapType "Map"
        }
        elseif (Test-Path $mapPath2 -PathType Container) {
            Copy-MapFiles -ClientPath $ClientPath -MapType "DevScene"
        }
        else {
            Write-Host "Error: Cannot find Map folder in client" -ForegroundColor Red
        }
    }
    else {
        Write-Host "Error: Path not found: $ClientPath" -ForegroundColor Red
    }
}
else {
    $detectedPath, $mapType = Find-ClientPath
    
    if ($detectedPath) {
        $confirm = Read-Host "`nCopy map files to this client? (Y/N)"
        if ($confirm -eq "Y" -or $confirm -eq "y") {
            Copy-MapFiles -ClientPath $detectedPath -MapType $mapType
        }
        else {
            Write-Host "Cancelled" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "`nCannot auto-detect client directory." -ForegroundColor Red
        Write-Host "`nPlease specify client path manually:" -ForegroundColor Yellow
        Write-Host "  .\copy_map_to_client.ps1 -ClientPath 'D:\MirClient'" -ForegroundColor Cyan
        Write-Host "`nCommon paths:" -ForegroundColor Yellow
        foreach ($path in $CommonPaths) {
            Write-Host "  $path" -ForegroundColor Gray
        }
    }
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
