function Show-FolderTree {
    param (
        [string]$Path = ".",
        [int]$Indent = 0
    )

    # Get subdirectories
    Get-ChildItem -Path $Path -Directory | ForEach-Object {
        # Print current folder with indentation
        Write-Host (" " * $Indent) + $_.Name
        # Recurse into subfolder
        Show-FolderTree -Path $_.FullName -Indent ($Indent + 2)
    }
}

Show-FolderTree
