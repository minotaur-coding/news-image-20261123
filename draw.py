#!/usr/bin/env python3
"""Draw the WORLD NEWS infographic for 23 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (16, 18, 24)
PANEL = (26, 29, 38)
FG = (232, 235, 240)
MUT = (150, 156, 168)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def tw(d, text, font):
    b = d.textbbox((0, 0), text, font=font)
    return b[2] - b[0]


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(d, t, font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 8], fill=(220, 50, 47))
d.text((40, 30), "WORLD NEWS", font=f(SERIF, 58), fill=FG)
d.text((44, 100), "Monday, 23 November 2026", font=f(REG, 22), fill=MUT)
d.text((W - 40 - tw(d, "THE DAY IN ONE IMAGE", f(REG, 18)), 104),
       "THE DAY IN ONE IMAGE", font=f(REG, 18), fill=MUT)
d.line([40, 138, W - 40, 138], fill=(60, 65, 78), width=2)

# ---------- story cards ----------
stories = [
    ("01", "US POLITICS", (86, 156, 214),
     "Democrats win 258 House seats — the biggest midterm wave since 1992. Hakeem Jeffries is set to become the first Black Speaker of the House."),
    ("02", "CLIMATE", (78, 174, 122),
     "COP31 UN climate talks in Turkey collapse without agreement after nations deadlock over fossil-fuel language."),
    ("03", "WAR", (222, 94, 74),
     "Ukraine war spreads: drone strike hits a Russian warship in Benghazi, Libya, while a Kyiv apartment block is hit by Russian fire."),
    ("04", "TECH", (186, 140, 220),
     "California sues OpenAI over model security and public safety in a first-of-its-kind state case."),
]

top = 156
card_h, gap = 150, 16
x0, x1 = 40, W - 40
inner = x0 + 24

for i, (num, tag, color, body) in enumerate(stories):
    y = top + i * (card_h + gap)
    d.rounded_rectangle([x0, y, x1, y + card_h], radius=10, fill=PANEL)
    d.rectangle([x0, y, x0 + 10, y + card_h], fill=color)
    tagf = f(BOLD, 24)
    numf = f(BOLD, 26)
    bodyf = f(REG, 21)

    d.text((inner, y + 16), num, font=numf, fill=color)
    tag_x = inner + 10 + tw(d, num, numf) + 14
    d.text((tag_x, y + 17), tag, font=tagf, fill=FG)
    d.line([x1 - 24 - tw(d, "●", tagf), y + 30, x1 - 24, y + 30], fill=color, width=3)

    lines = wrap(d, body, bodyf, x1 - 24 - inner - 8)
    ly = y + 58
    for ln in lines:
        d.text((inner, ly), ln, font=bodyf, fill=FG)
        ly += 28

# ---------- footer ----------
fy = top + 4 * (card_h + gap) + 8
d.rectangle([0, fy, W, fy + 3], fill=(60, 65, 78))
d.text((40, fy + 16), "ALSO TODAY", font=f(BOLD, 20), fill=(220, 50, 47))
foot = [
    ("Ebola tops 11,000 cases in DR Congo", (86, 156, 214)),
    ("Korea braces for 'Black Monday'", (222, 94, 74)),
    ("Nepal PM visits India", (78, 174, 122)),
]
fnt = f(REG, 20)
avail = W - 80
row, fx = 0, 40
for text, color in foot:
    wtxt = 16 + tw(d, text, fnt) + 36
    if fx + wtxt - 36 > avail and row < 2:
        row += 1
        fx = 40
    d.ellipse([fx, fy + 55 + row * 32, fx + 8, fy + 63 + row * 32], fill=color)
    d.text((fx + 16, fy + 48 + row * 32), text, font=fnt, fill=MUT)
    fx += wtxt

d.text((40, H - 46), "Compiled 23 Nov 2026 · Sources: wire reports", font=f(REG, 16), fill=(110, 116, 128))

img.save("/home/agentuser/newsimage/entry/entry.png", optimize=True)
print("saved", img.size)
