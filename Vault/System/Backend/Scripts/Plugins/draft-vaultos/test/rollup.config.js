import typescript from 'rollup-plugin-typescript2';
import resolve from '@rollup/plugin-node-resolve';
import { join } from 'path';

export default {
  input: 'main.ts',
  output: {
    dir: 'dist',
    format: 'cjs',
    sourcemap: true,
    exports: 'default'
  },
  plugins: [
    resolve(),
    typescript({
      tsconfig: join(__dirname, 'tsconfig.json'),
      useTsconfigDeclarationDir: true
    })
  ],
  external: ['obsidian']
};
