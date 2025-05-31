📁 src/ → Source
Stands for "source".

This folder contains the raw code you write.

For example: TypeScript files, uncompiled CSS/SCSS, unminified JavaScript, etc.

💡 Think of this as your working folder — everything in here is editable, unprocessed, and meant for humans.

📁 dist/ → Distribution
Stands for "distribution".

This folder holds the final, compiled, production-ready code.

It’s what gets used in production (e.g., the final .js from your TypeScript).

💡 Think of this as the output folder — everything here is optimized for performance, not readability.

🔁 Typical Flow:

'''pgsql
📁 src/
│   └── main.ts         👈 You write this
     ↓
  (Build tool like Rollup or Webpack)
     ↓
📁 dist/
│   └── main.js         👈 This gets compiled and used by Obsidian (or browsers, etc.)
'''