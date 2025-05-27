#!/bin/bash

# ┌────────────────────────────────────────┐
# │ Obsidian Plugin Build Script (build.sh)│
# └────────────────────────────────────────┘

# Exit on error
set -e

# Move to script's directory
cd "$(dirname "$0")"

# Output folder
DIST_DIR="dist"
ENTRY_FILE="main.ts"
OUT_FILE="$DIST_DIR/main.js"

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

# Check for watch flag
if [[ "$1" == "--watch" ]]; then
  echo "👀 Watching for changes..."
  npx esbuild "$ENTRY_FILE" \
    --bundle \
    --outfile="$OUT_FILE" \
    --target=es2020 \
    --external:obsidian \
    --watch
else
  echo "🚀 Building plugin..."
  npx esbuild "$ENTRY_FILE" \
    --bundle \
    --outfile="$OUT_FILE" \
    --target=es2020 \
    --external:obsidian
  echo "✅ Build complete: $OUT_FILE"
fi
