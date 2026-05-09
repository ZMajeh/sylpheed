#!/bin/bash

# run.sh - Run the built Sylpheed application

EXE_PATH="./src/sylpheed"

if [ ! -f "$EXE_PATH" ]; then
    echo "Error: Executable not found at $EXE_PATH. Please run ./build.sh first."
    exit 1
fi

echo "Launching Sylpheed..."

# Isolation: Unset GDK_PIXBUF_MODULE_FILE to prevent loading incompatible system loader cache
export GDK_PIXBUF_MODULE_FILE=""

$EXE_PATH "$@"
