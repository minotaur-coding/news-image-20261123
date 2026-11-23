// news-image-20261123: writes the day's news image to /output/entry.png.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const OUT = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(OUT, { recursive: true });
writeFileSync(`${OUT}/entry.png`, readFileSync(new URL('./entry.png', import.meta.url)));
