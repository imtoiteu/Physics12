# -*- coding: utf-8 -*-
"""Dựng toàn bộ tài liệu Word cho ngân hàng đề THPT 2026."""
import os
import sys
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build

SPEC = [
    ("de_12c1", "LOP12_CHUONG1_VAT_LI_NHIET_DE.docx", "LOP12_CHUONG1_VAT_LI_NHIET_LOI_GIAI.docx"),
    ("de_12c2", "LOP12_CHUONG2_KHI_LI_TUONG_DE.docx", "LOP12_CHUONG2_KHI_LI_TUONG_LOI_GIAI.docx"),
    ("de_12mix", "LOP12_TONG_HOP_CHUONG_1_VA_2_DE.docx", "LOP12_TONG_HOP_CHUONG_1_VA_2_LOI_GIAI.docx"),
    ("de_11c1", "LOP11_CHUONG1_DAO_DONG_DE.docx", "LOP11_CHUONG1_DAO_DONG_LOI_GIAI.docx"),
]


def main(only=None):
    for modname, fde, fgiai in SPEC:
        if only and modname not in only:
            continue
        try:
            mod = importlib.import_module(modname)
        except ModuleNotFoundError:
            print("  (chưa có %s – bỏ qua)" % modname)
            continue
        g = mod.NHOM
        spread = build.rebalance_group(g)
        p1 = build.build_de(g, fde)
        p2 = build.build_giai(g, fgiai)
        n = sum(len(t["P1"]) + len(t["P2"]) + len(t["P3"]) for t in g["tests"])
        print("✓ %-10s %2d đề / %3d câu | đáp án %s\n    %s\n    %s"
              % (modname, len(g["tests"]), n, spread,
                 os.path.basename(p1), os.path.basename(p2)))


if __name__ == "__main__":
    main(sys.argv[1:] or None)
