# create_release.ps1 - Package Sylpheed as a numbered release

$releaseBase = "release"
$counter = 1

# Find the next available release directory name
while (Test-Path "$releaseBase`_$counter") {
    $counter++
}

$targetDir = "$releaseBase`_$counter"
$zipFile = "Sylpheed-Release_$counter.zip"

Write-Host "Creating release package in: $targetDir" -ForegroundColor Cyan

# Create directory
$binDir = "$targetDir\bin"
New-Item -ItemType Directory -Path $binDir | Out-Null

# Copy binaries and dependencies
# Using -Recurse and -Force to ensure everything is copied
Copy-Item -Path "dist\mingw64\*" -Destination $targetDir -Recurse -Force


# Copy compiled binary from .libs
Copy-Item -Path "src\.libs\*" -Destination $binDir -Force

# Copy other resources from dist if needed
# (Assuming you want to keep your locale/manual files)
Copy-Item -Path "dist\mingw64\share" -Destination $targetDir -Recurse -Force

# Add the portable launch script
$portableScript = @"
# sylpheed_portable.ps1 - Launch portable Sylpheed
param([switch]`$Debug)
`$EXE_PATH = "bin\sylpheed.exe"
if (-not (Test-Path `$EXE_PATH)) {
    Write-Error "Executable not found at `$EXE_PATH. Package seems corrupted."
    exit 1
}
Write-Host "Launching Sylpheed Portable..." -ForegroundColor Cyan
`$BIN_DIR = (Resolve-Path (Split-Path `$EXE_PATH)).Path
`$env:PATH = "`$BIN_DIR"
`$env:GDK_PIXBUF_MODULE_FILE = ""
`$argsList = @()
if (`$Debug) { `$argsList += "--debug" }
Push-Location `$BIN_DIR
& ".\sylpheed.exe" @argsList
Pop-Location
"@

$portableScript | Out-File -FilePath "$targetDir\sylpheed_portable.ps1" -Encoding ascii

# Create ZIP archive
Write-Host "Creating archive: $zipFile" -ForegroundColor Cyan
Compress-Archive -Path "$targetDir\*" -DestinationPath $zipFile -Force

Write-Host "Successfully packaged release as $zipFile" -ForegroundColor Green
