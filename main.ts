// news-image-20261123: writes the day's news image to $MAKEFUN_OUTPUT_DIR/entry.png.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const OUT = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(OUT, { recursive: true });
writeFileSync(`${OUT}/entry.png`, readFileSync(new URL('./entry.png', import.meta.url)));
console.log('entry.png written to', OUT);
