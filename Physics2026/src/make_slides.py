# -*- coding: utf-8 -*-
"""Dựng toàn bộ bộ slide bài giảng .pptx vào thư mục Slides/."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

import deck                                                        # noqa: E402
import slides_00, slides_c1, slides_c2, slides_c3, slides_c4       # noqa: E402

GROUPS = [(slides_00, "Slides"),
          (slides_c1, "Slides/Chuong01"),
          (slides_c2, "Slides/Chuong02"),
          (slides_c3, "Slides/Chuong03"),
          (slides_c4, "Slides/Chuong04")]


def main():
    warn, tot, files = [], 0, 0
    for mod, sub in GROUPS:
        outdir = os.path.join(ROOT, sub)
        os.makedirs(outdir, exist_ok=True)
        for sp in mod.SPEC:
            _p, w, n = deck.build(sp, outdir)
            tot += n
            files += 1
            print("  %-58s %2d slide  %s" % (sp["file"], n, "; ".join(w) if w else "OK"))
            warn += w
    print("\n%d tệp .pptx, %d slide." % (files, tot))
    if warn:
        print("--- CẢNH BÁO TRÀN CHỮ (%d) ---" % len(warn))
        for w in warn:
            print("  ✗", w)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
