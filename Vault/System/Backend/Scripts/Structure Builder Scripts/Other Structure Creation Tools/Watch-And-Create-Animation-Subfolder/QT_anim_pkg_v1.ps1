# Set up watcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "C:\Users\benny\Desktop\Generation_animation"
$watcher.Filter = "*"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action {
    if (Test-Path $Event.SourceEventArgs.FullPath) {
        $item = Get-Item $Event.SourceEventArgs.FullPath
        if ($item.PSIsContainer) {

            # Extract base name (no parentheses at end)
            $rawName = $item.Name
            $baseName = $rawName -replace '\s*\(.*\)$', ''

            # Extract [Theme] after "-MM-DD-YY-" and before any " ("
            if ($baseName -match "-\d{2}-\d{2}-\d{2}-([^\(]+)") {
                $theme = $matches[1].Trim()
            } else {
                $theme = "Inconnu"
            }

            # Create the animation folder
            $newAnimationPath = Join-Path -Path $item.FullName -ChildPath "$baseName (animation)"
            if (-not (Test-Path $newAnimationPath)) {
                New-Item -Path $newAnimationPath -ItemType Directory | Out-Null
                Write-Output "Created subfolder: $newAnimationPath"
            }

            # Define source folders inside the $item
            $sourceMUS = Join-Path $item.FullName "MUS"
            $sourceRDY = Join-Path $item.FullName "RDY"

            # Step 1: Copy MUS folder
            if (Test-Path $sourceMUS) {
                $destMUS = Join-Path $newAnimationPath "MUS"
                Copy-Item -Path $sourceMUS -Destination $destMUS -Recurse -Force
                Write-Output "Copied MUS folder to $destMUS"
            } else {
                Write-Warning "MUS folder not found at: $sourceMUS"
            }

            # Step 2: Copy contents of RDY (not folder itself)
            if (Test-Path $sourceRDY) {
                Get-ChildItem -Path $sourceRDY -Recurse | ForEach-Object {
                    $destination = Join-Path $newAnimationPath ($_.FullName -replace [regex]::Escape($sourceRDY), "")
                    $destinationDir = Split-Path $destination -Parent
                    if (-not (Test-Path $destinationDir)) {
                        New-Item -ItemType Directory -Path $destinationDir -Force | Out-Null
                    }
                    Copy-Item $_.FullName -Destination $destination -Recurse -Force
                }
                Write-Output "Copied contents of RDY to $newAnimationPath"
            } else {
                Write-Warning "RDY folder not found at: $sourceRDY"
            }

            # Step 3: Handle PourPierre document
            $pourPierreFile = Get-ChildItem -Path $item.FullName -Filter "PourPierre*" | Where-Object { -not $_.PSIsContainer } | Select-Object -First 1
            if ($pourPierreFile) {
                $extension = $pourPierreFile.Extension
                $newFileName = "Questions-Reponses_$theme$extension"
                $destinationPath = Join-Path $item.FullName $newFileName
                Copy-Item -Path $pourPierreFile.FullName -Destination $destinationPath -Force
                Write-Output "✔️ Copied PourPierre file as: $destinationPath"
            } else {
                Write-Warning "⚠️ No file starting with 'PourPierre' found in $($item.FullName)"
            }
        }
    }
}

Write-Output "Watching for new folders in Generation_animation... Press Ctrl+C to stop."
while ($true) { Start-Sleep -Seconds 10 }
