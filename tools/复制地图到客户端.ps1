# 996PC引擎 - 复制地图文件到客户端
# 解决自定义地图黑屏问题

param(
    [Parameter(Mandatory=$false)]
    [string]$ClientPath = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$AutoDetect
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
    "D:\996M2",
    "$env:USERPROFILE\Desktop\热血传奇",
    "$env:USERPROFILE\Desktop\传奇客户端"
)

function Find-ClientPath {
    Write-Host "正在搜索客户端目录..." -ForegroundColor Yellow
    
    foreach ($path in $CommonPaths) {
        if (Test-Path $path) {
            # 检查是否是有效的传奇客户端（包含Map或dev/scene/map目录）
            $mapPath1 = Join-Path $path "Map"
            $mapPath2 = Join-Path $path "dev\scene\map"
            
            if (Test-Path $mapPath1 -PathType Container) {
                Write-Host "找到客户端: $path (Map目录)" -ForegroundColor Green
                return $path, "Map"
            }
            elseif (Test-Path $mapPath2 -PathType Container) {
                Write-Host "找到客户端: $path (dev/scene/map目录)" -ForegroundColor Green
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
    
    Write-Host "`n目标路径: $targetPath" -ForegroundColor Cyan
    
    # 确保目标目录存在
    if (!(Test-Path $targetPath)) {
        New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
        Write-Host "创建目录: $targetPath" -ForegroundColor Yellow
    }
    
    # 复制所有地图文件
    $mapFiles = Get-ChildItem -Path $ServerMapPath -Filter "*.map"
    $copied = 0
    $skipped = 0
    
    Write-Host "`n开始复制地图文件..." -ForegroundColor Yellow
    
    foreach ($file in $mapFiles) {
        $targetFile = Join-Path $targetPath $file.Name
        
        if (Test-Path $targetFile) {
            $sourceSize = $file.Length
            $targetSize = (Get-Item $targetFile).Length
            
            if ($sourceSize -eq $targetSize) {
                Write-Host "  [跳过] $($file.Name) (已存在且大小相同)" -ForegroundColor Gray
                $skipped++
                continue
            }
        }
        
        Copy-Item -Path $file.FullName -Destination $targetFile -Force
        Write-Host "  [复制] $($file.Name)" -ForegroundColor Green
        $copied++
    }
    
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "复制完成!" -ForegroundColor Green
    Write-Host "  已复制: $copied 个文件" -ForegroundColor Green
    Write-Host "  已跳过: $skipped 个文件" -ForegroundColor Gray
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "`n请重启客户端后进入游戏测试。" -ForegroundColor Yellow
}

# 主程序
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  996PC引擎地图复制工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($ClientPath) {
    # 使用用户指定的路径
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
            Write-Host "错误: 无法找到客户端的Map目录" -ForegroundColor Red
            Write-Host "请确认路径正确，或尝试使用 -AutoDetect 参数自动检测" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "错误: 指定的路径不存在: $ClientPath" -ForegroundColor Red
    }
}
else {
    # 自动检测
    $detectedPath, $mapType = Find-ClientPath
    
    if ($detectedPath) {
        $confirm = Read-Host "`n是否复制地图文件到该客户端? (Y/N)"
        if ($confirm -eq "Y" -or $confirm -eq "y") {
            Copy-MapFiles -ClientPath $detectedPath -MapType $mapType
        }
        else {
            Write-Host "操作已取消" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "`n未能自动找到客户端目录。" -ForegroundColor Red
        Write-Host "`n请手动指定客户端路径，例如:" -ForegroundColor Yellow
        Write-Host "  .\复制地图到客户端.ps1 -ClientPath 'D:\热血传奇'" -ForegroundColor Cyan
        Write-Host "`n常见客户端路径:" -ForegroundColor Yellow
        foreach ($path in $CommonPaths) {
            Write-Host "  $path" -ForegroundColor Gray
        }
    }
}

Write-Host "`n按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
