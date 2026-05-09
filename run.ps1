# run.ps1 - Run the built Sylpheed application

param(
    [switch]$Debug
)

$EXE_PATH = "dist\mingw64\bin\sylpheed.exe"

if (-not (Test-Path $EXE_PATH)) {
    Write-Error "Executable not found at $EXE_PATH. Please run ./build.ps1 first."
    exit 1
}

Write-Host "Launching Sylpheed..." -ForegroundColor Cyan

# Isolation: Set PATH and Environment
$BIN_DIR = (Resolve-Path (Split-Path $EXE_PATH)).Path
$env:PATH = "$BIN_DIR"
$env:GDK_PIXBUF_MODULE_FILE = ""

Write-Host "DEBUG PATH: $env:PATH" -ForegroundColor Yellow

# Build arguments
$argsList = @()
if ($Debug) {
    $argsList += "--debug"
}

# Run directly within the same process context to avoid lifecycle termination
Push-Location $BIN_DIR
& ".\sylpheed.exe" @argsList
Pop-Location
