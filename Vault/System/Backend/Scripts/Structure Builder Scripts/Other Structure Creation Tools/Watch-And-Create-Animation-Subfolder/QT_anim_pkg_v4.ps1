Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create tray icon
$trayIcon = New-Object System.Windows.Forms.NotifyIcon
$trayIcon.Icon = [System.Drawing.SystemIcons]::Information
$trayIcon.Visible = $true
$trayIcon.Text = "Epic Anim Bundler"

function Show-Notification {
    param ($title, $message)
    $trayIcon.BalloonTipTitle = $title
    $trayIcon.BalloonTipText = $message
    $trayIcon.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Info
    $trayIcon.ShowBalloonTip(3000)
}

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

            $sourceMUS = Join-Path $item.FullName "MUS"
            $sourceRDY = Join-Path $item.FullName "RDY"

            if ($baseName.StartsWith("SIB")) {
                $siblingFolders = Get-ChildItem -Path $item.Directory.FullName -Directory
                $stvFolder = $siblingFolders | Where-Object { $_.Name -like "STV*" } | Select-Object -First 1

                if ($stvFolder) {
                    $sibPrefix = ($item.Name -split "-")[0]
                    $stvPrefix = ($stvFolder.Name -split "-")[0]

                    Get-ChildItem -Path $item.FullName -Recurse | Where-Object { $_.FullName -notlike "* (animation)*" } | ForEach-Object {
                        $relativePath = $_.FullName.Substring($item.FullName.Length)
                        $target = Join-Path $stvFolder.FullName $relativePath
                        $targetDir = Split-Path $target -Parent
                        if (-not (Test-Path $targetDir)) {
                            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
                        }
                        Copy-Item $_.FullName -Destination $target -Recurse -Force
                    }

                    Get-ChildItem -Path $stvFolder.FullName -Recurse -File | Where-Object { $_.Name -like "*$sibPrefix*" } | ForEach-Object {
                        $newName = $_.Name -replace [regex]::Escape($sibPrefix), $stvPrefix
                        $newPath = Join-Path $_.DirectoryName $newName
                        Rename-Item -Path $_.FullName -NewName $newPath -Force
                    }

                    Show-Notification -title "Prefix Swap Done" -message "SIB folder merged into STV and all the names got a snazzy makeover."
                } else {
                    Write-Warning "No STV folder found in: $($item.Directory.FullName)"
                }
            }

            $newAnimationPath = Join-Path -Path $item.FullName -ChildPath "$baseName (animation)"
            if (-not (Test-Path $newAnimationPath)) {
                New-Item -Path $newAnimationPath -ItemType Directory | Out-Null
                Show-Notification -title "Animation Nest Ready" -message "Created a cozy little animation folder just for you."
            }

            if (Test-Path $sourceMUS) {
                $destMUS = Join-Path $newAnimationPath "MUS"
                Copy-Item -Path $sourceMUS -Destination $destMUS -Recurse -Force
                Show-Notification -title "MUS Delivered" -message "MUS folder tucked into the animation suite like a VIP."
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
                Show-Notification -title "RDY Imported" -message "RDY folder contents slipped smoothly into place."
            }

            $pourPierreFile = Get-ChildItem -Path $item.FullName -Filter "PourPierre*" -File | Select-Object -First 1
            if ($pourPierreFile) {
                $extension = $pourPierreFile.Extension
                $newFileName = "Questions-Reponses_$theme$extension"
                $destinationPath = Join-Path $item.FullName $newFileName
                Copy-Item -Path $pourPierreFile.FullName -Destination $destinationPath -Force
                Show-Notification -title "Q-R Ready" -message "PourPierre cloned and rebranded like a pro."
            }

            Show-Notification -title "Anim Package Generated" -message "'$rawName' T'es good mon gars! Tu peux aller nettoyer les Questions-Réponses pis l'affaire est Ketchup."
        }
    }
}

Show-Notification -title "Epic Anim Bundler" -message "Watching for new folders like a hawk in shades."
while ($true) { Start-Sleep -Seconds 10 }
