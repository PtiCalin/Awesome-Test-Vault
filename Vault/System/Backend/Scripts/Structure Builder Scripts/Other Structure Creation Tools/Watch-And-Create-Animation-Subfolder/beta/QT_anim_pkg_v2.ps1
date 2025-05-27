Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create tray icon
$trayIcon = New-Object System.Windows.Forms.NotifyIcon
$trayIcon.Icon = [System.Drawing.SystemIcons]::Information
$trayIcon.Visible = $true
$trayIcon.Text = "Ben's Automation Engine"

# Function to show notification
function Show-Notification {
    param ($title, $message)
    $trayIcon.BalloonTipTitle = $title
    $trayIcon.BalloonTipText = $message
    $trayIcon.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Info
    $trayIcon.ShowBalloonTip(3000)
}

# Set up watcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "C:\Users\benny\Desktop\Generation_animation"
$watcher.Filter = "*"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action {
    Start-Sleep -Seconds 3

    $path = $Event.SourceEventArgs.FullPath
    if (Test-Path $path) {
        $item = Get-Item $path
        if ($item.PSIsContainer) {
            $rawName = $item.Name
            $baseName = $rawName -replace '\s*\(.*\)$', ''

            if ($baseName -match "-\d{2}-\d{2}-\d{2}-(.+)$") {
                $themePart = $matches[1]
                $theme = $themePart -replace '\s*\(.*\)$', ''
                $theme = $theme.Trim()
            } else {
                $theme = "Inconnu"
            }

            $newAnimationPath = Join-Path -Path $item.FullName -ChildPath "$baseName (animation)"
            if (-not (Test-Path $newAnimationPath)) {
                New-Item -Path $newAnimationPath -ItemType Directory | Out-Null
            }

            $sourceMUS = Join-Path $item.FullName "MUS"
            $sourceRDY = Join-Path $item.FullName "RDY"

            $tries = 0
            while (!(Test-Path $sourceMUS) -and ($tries -lt 5)) {
                Start-Sleep -Seconds 1
                $tries++
            }
            if (Test-Path $sourceMUS) {
                $destMUS = Join-Path $newAnimationPath "MUS"
                Copy-Item -Path $sourceMUS -Destination $destMUS -Recurse -Force
            }

            $tries = 0
            while (!(Test-Path $sourceRDY) -and ($tries -lt 5)) {
                Start-Sleep -Seconds 1
                $tries++
            }
            if (Test-Path $sourceRDY) {
                Get-ChildItem -Path $sourceRDY -Recurse | ForEach-Object {
                    $destination = Join-Path $newAnimationPath ($_.FullName -replace [regex]::Escape($sourceRDY), "")
                    $destinationDir = Split-Path $destination -Parent
                    if (-not (Test-Path $destinationDir)) {
                        New-Item -ItemType Directory -Path $destinationDir -Force | Out-Null
                    }
                    Copy-Item $_.FullName -Destination $destination -Recurse -Force
                }
            }

            $tries = 0
            $pourPierreFile = $null
            while (-not $pourPierreFile -and ($tries -lt 5)) {
                $pourPierreFile = Get-ChildItem -Path $item.FullName -Filter "PourPierre*" -File | Select-Object -First 1
                if (-not $pourPierreFile) {
                    Start-Sleep -Seconds 1
                    $tries++
                }
            }

            if ($pourPierreFile) {
                $extension = $pourPierreFile.Extension
                $newFileName = "Questions-Reponses_$theme$extension"
                $destinationPath = Join-Path $item.FullName $newFileName
                Copy-Item -Path $pourPierreFile.FullName -Destination $destinationPath -Force
            }

            Show-Notification -title "T'es all set mon gars!" -message "'$rawName' has been processed and animation folder is ready!"
        }
    }
}

Show-Notification -title "Anim Package - Tray App" -message "Watching for new folders..."
while ($true) { Start-Sleep -Seconds 10 }
