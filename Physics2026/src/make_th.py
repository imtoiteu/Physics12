# -*- coding: utf-8 -*-
"""Dựng 30 đề thi thử tốt nghiệp THPT 2026 (.docx) vào thư mục DeThiTongHop/.

Mỗi đề có một thư mục riêng De01 … De30 gồm hai tệp: đề thi và đáp án + lời giải
chi tiết. Ngoài ra sinh thêm 6 tập gộp (mỗi tập 5 đề) trong DeThiTongHop/TronBo/
để tiện in ấn.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

import build as B                                                   # noqa: E402
import de_th1, de_th2, de_th3, de_th4, de_th5, de_th6               # noqa: E402

MODS = [de_th1, de_th2, de_th3, de_th4, de_th5, de_th6]

TEN_BO = "BỘ 30 ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – MÔN VẬT LÍ"
PHAM_VI = ("Tổng hợp bốn chương của chương trình Vật lí 12: Chương I – Vật lí nhiệt; "
           "Chương II – Khí lí tưởng; Chương III – Từ trường; Chương IV – Vật lí hạt nhân.")


def main():
    out_root = os.path.join(ROOT, "DeThiTongHop")
    tron = os.path.join(out_root, "TronBo")
    os.makedirs(tron, exist_ok=True)

    tests, tot = [], {L: 0 for L in B.LETTERS}
    for mod in MODS:
        g = mod.NHOM
        c = B.rebalance_group(g)                 # cân bằng vị trí đáp án A–D
        for L in B.LETTERS:
            tot[L] += c[L]
        tests += list(g["tests"])
    assert len(tests) == 30, len(tests)

    n_cau = 0
    for i, t in enumerate(tests, 1):
        sub = os.path.join(out_root, "De%02d" % i)
        os.makedirs(sub, exist_ok=True)
        g = dict(ten_nhom=TEN_BO,
                 mo_ta="%s – mức độ %s. Thời gian làm bài 50 phút, thang điểm 10."
                       % (t["ten"], t["muc"].lower()),
                 pham_vi=PHAM_VI, tests=[t])
        p1 = B.build_de(g, "DE%02d_DE_THI.docx" % i, sub)
        p2 = B.build_giai(g, "DE%02d_DAP_AN_VA_LOI_GIAI.docx" % i, sub)
        n = len(t["P1"]) + len(t["P2"]) + len(t["P3"])
        n_cau += n
        print("  %-8s %2d câu  |  %s" % ("De%02d" % i, n, os.path.relpath(p1, ROOT)))
        print("  %-8s %20s  %s" % ("", "", os.path.relpath(p2, ROOT)))

    for k, mod in enumerate(MODS, 1):
        g = mod.NHOM
        a, b = 5 * k - 4, 5 * k
        B.build_de(g, "TAP%d_DE_%02d_DEN_%02d_DE_THI.docx" % (k, a, b), tron)
        B.build_giai(g, "TAP%d_DE_%02d_DEN_%02d_LOI_GIAI.docx" % (k, a, b), tron)
    print("  TronBo   6 tập gộp (mỗi tập 5 đề), 12 tệp .docx")
    print("  TỔNG: %d đề, %d câu hỏi | phân bố đáp án Phần I %s" % (len(tests), n_cau, tot))
    return 0


if __name__ == "__main__":
    sys.exit(main())
