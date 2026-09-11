# -*- coding: utf-8 -*-
"""Ghép nhiều hình thành một tấm liên hoàn để soát bằng mắt."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

FIGS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs"))
FNT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def sheet(names, out, cols=3, cell=680):
    f = ImageFont.truetype(FNT, 20)
    rows = (len(names) + cols - 1) // cols
    W, H = cols * cell, rows * (cell * 3 // 4 + 34)
    canvas = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(canvas)
    ch = cell * 3 // 4
    for i, n in enumerate(names):
        r, c = divmod(i, cols)
        x, y = c * cell, r * (ch + 34)
        d.text((x + 8, y + 6), n, font=f, fill="#c0392b")
        im = Image.open(os.path.join(FIGS, n + ".png")).convert("RGB")
        im.thumbnail((cell - 16, ch - 8))
        canvas.paste(im, (x + 8 + (cell - 16 - im.width) // 2, y + 32))
    canvas.save(out)
    return out


if __name__ == "__main__":
    print(sheet(sys.argv[2:], sys.argv[1]))
