import typescript from "rollup-plugin-typescript2";

export default {
  input: "main.ts",
  output: {
    file: "main.js",
    format: "cjs",
    sourcemap: true
  },
  external: ["obsidian"],
  plugins: [typescript()]
};
