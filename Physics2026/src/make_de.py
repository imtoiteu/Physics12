# -*- coding: utf-8 -*-
"""Dựng bộ đề luyện tập theo chương (.docx) vào thư mục BaiTapTheoChuong/."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

import build as B                                                   # noqa: E402
import de_12c1, de_12c2, de_12c3, de_12c4                           # noqa: E402

SPEC = [
    (de_12c1, "Chuong01", "CHUONG1_VAT_LI_NHIET"),
    (de_12c2, "Chuong02", "CHUONG2_KHI_LI_TUONG"),
    (de_12c3, "Chuong03", "CHUONG3_TU_TRUONG"),
    (de_12c4, "Chuong04", "CHUONG4_VAT_LI_HAT_NHAN"),
]


def main():
    for mod, sub, stem in SPEC:
        outdir = os.path.join(ROOT, "BaiTapTheoChuong", sub)
        os.makedirs(outdir, exist_ok=True)
        g = mod.NHOM
        tot = B.rebalance_group(g)          # phân bố lại vị trí đáp án cho đều A–D
        p1 = B.build_de(g, "%s_10_DE_LUYEN_TAP.docx" % stem, outdir)
        p2 = B.build_giai(g, "%s_10_DE_LOI_GIAI_CHI_TIET.docx" % stem, outdir)
        n = sum(len(t["P1"]) + len(t["P2"]) + len(t["P3"]) for t in g["tests"])
        print("  %-26s %2d đề, %3d câu | đáp án %s\n      %s\n      %s"
              % (sub, len(g["tests"]), n, tot,
                 os.path.relpath(p1, ROOT), os.path.relpath(p2, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
