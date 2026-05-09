#!/bin/bash

# build.sh - Build Sylpheed on MSYS2 MinGW64

set -e

# Only run autogen.sh and configure if Makefile doesn't exist
if [ ! -f "Makefile" ]; then
    echo "Makefile not found. Running autogen.sh and configure..."
    ./autogen.sh
    
    echo "Running configure with required libraries..."
    # The LIBS environment variable ensures iconv and OpenSSL are linked properly
    ./configure --prefix=/mingw64 LIBS='-liconv -lssl -lcrypto'
else
    echo "Makefile found. Skipping autogen and configure."
fi

echo "Compiling..."
make LIBS='-liconv -lssl -lcrypto'

echo "Installing..."
make install

echo "Build and installation complete!"