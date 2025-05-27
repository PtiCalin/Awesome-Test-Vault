# Set up watcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "C:\Users\benny\Desktop\Generation_animation"
$watcher.Filter = "*"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

# Register folder creation event
Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action {
    if (Test-Path $Event.SourceEventArgs.FullPath) {
        $item = Get-Item $Event.SourceEventArgs.FullPath
        if ($item.PSIsContainer) {
            $folderName = $item.Name
            $newAnimationPath = Join-Path -Path $item.FullName -ChildPath "$folderName (animation)"
            
            if (-not (Test-Path $newAnimationPath)) {
                New-Item -Path $newAnimationPath -ItemType Directory | Out-Null
                Write-Output "Created subfolder: $newAnimationPath"

                # Define dynamic source paths INSIDE the newly dropped folder
                $sourceMUS = Join-Path $item.FullName "MUS"
                $sourceRDY = Join-Path $item.FullName "RDY"

                # Step 1: Copy MUS folder to animation folder
                if (Test-Path $sourceMUS) {
                    $destMUS = Join-Path $newAnimationPath "MUS"
                    Copy-Item -Path $sourceMUS -Destination $destMUS -Recurse -Force
                    Write-Output "Copied MUS folder to $destMUS"
                } else {
                    Write-Warning "MUS folder not found in: $sourceMUS"
                }

                # Step 2: Copy contents of RDY folder to animation folder (not the RDY folder itself)
                if (Test-Path $sourceRDY) {
                    Get-ChildItem -Path $sourceRDY -Recurse | ForEach-Object {
                        $destPath = Join-Path $newAnimationPath $_.Name
                        Copy-Item -Path $_.FullName -Destination $destPath -Recurse -Force
                    }
                    Write-Output "Copied contents of RDY folder to $newAnimationPath"
                } else {
                    Write-Warning "RDY folder not found in: $sourceRDY"
                }
            }
        }
    }
}

Write-Output "Watching for new folders in Generation_animation... Press Ctrl+C to stop."
while ($true) { Start-Sleep -Seconds 10 }