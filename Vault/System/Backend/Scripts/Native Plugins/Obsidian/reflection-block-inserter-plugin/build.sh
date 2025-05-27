#!/bin/bash
cd "$(dirname "$0")"
npx esbuild main.ts --bundle --outfile=main.js --target=es2020