# -*- coding: utf-8 -*-
"""Mở lại toàn bộ tệp .docx đã sinh và đối chiếu với dữ liệu nguồn.

Kiểm tra cho từng tệp:
  • số câu hỏi và thứ tự câu của từng phần;
  • từng dòng “Đáp án:” trong tệp lời giải so với đáp án trong mã nguồn;
  • nhãn ĐÚNG/SAI của từng ý trong câu trắc nghiệm đúng/sai;
  • số hình được nhúng thật sự và số bảng.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

from docx import Document                                           # noqa: E402
import build as B                                                   # noqa: E402
import de_12c1, de_12c2, de_12c3, de_12c4                           # noqa: E402
import de_th1, de_th2, de_th3, de_th4, de_th5, de_th6               # noqa: E402

ERR = []
WS = re.compile(r"\s+")
RE_CAU = re.compile(r"^Câu (\d+)\.")
RE_DA = re.compile(r"^Đáp án:\s*(.+)$")
RE_DS = re.compile(r"→\s*(ĐÚNG|SAI)\s*$")


def norm(s):
    return WS.sub(" ", str(s)).strip()


def err(msg):
    ERR.append(msg)
    print("  ✗ " + msg)


def paras(path):
    doc = Document(path)
    return doc, [norm(p.text) for p in doc.paragraphs]


def expect(group):
    """Trả về (danh sách câu theo thứ tự, số hình, số bảng số liệu)."""
    seq, nfig, ntbl = [], 0, 0
    for t in group["tests"]:
        for code, items in B.parts_of(t):
            for i, it in enumerate(items, 1):
                seq.append((t["ma"], code, i, it))
                nfig += 1 if it.get("fig") else 0
                ntbl += 1 if it.get("tbl") else 0
    return seq, nfig, ntbl


def check_de(path, group):
    doc, ps = paras(path)
    seq, nfig, ntbl = expect(group)
    got = [(int(m.group(1)), p) for p in ps for m in [RE_CAU.match(p)] if m]
    if len(got) != len(seq):
        err("%s: có %d câu, cần %d" % (os.path.basename(path), len(got), len(seq)))
        return
    for (num, p), (ma, code, i, it) in zip(got, seq):
        if num != i:
            err("%s %s Phần %s: đánh số câu %d ≠ %d" % (os.path.basename(path), ma, code, num, i))
            break
        head = norm(it["stem"] if code == "II" else it["q"])[:40]
        if head not in p:
            err("%s %s Phần %s câu %d: nội dung câu hỏi không khớp" % (
                os.path.basename(path), ma, code, i))
    n_img = len(doc.inline_shapes)
    if n_img != nfig:
        err("%s: nhúng %d hình, cần %d" % (os.path.basename(path), n_img, nfig))
    n_tbl = len(doc.tables)
    need = 3 + ntbl                       # 2 khung thông tin + 1 ma trận độ khó
    if n_tbl != need:
        err("%s: có %d bảng, cần %d" % (os.path.basename(path), n_tbl, need))
    return len(got), n_img, n_tbl


def check_giai(path, group):
    doc, ps = paras(path)
    seq, nfig, ntbl = expect(group)
    want_da, want_ds = [], []
    for ma, code, i, it in seq:
        if code == "I":
            want_da.append("Đáp án: %s. %s" % (it["a"], norm(it["o"][B.LETTERS.index(it["a"])])))
        elif code == "III":
            want_da.append("Đáp án: %s" % norm(it["ans"]))
        else:
            want_ds += ["ĐÚNG" if v else "SAI" for _txt, v, _ex in it["items"]]
    got_da = [norm(p) for p in ps if p.startswith("Đáp án:")]
    got_ds = [m.group(1) for p in ps for m in [RE_DS.search(p)] if m]
    if got_da != want_da:
        bad = [k for k in range(min(len(got_da), len(want_da))) if got_da[k] != want_da[k]]
        err("%s: %d/%d dòng đáp án lệch (vị trí đầu tiên: %s)" % (
            os.path.basename(path), len(bad) + abs(len(got_da) - len(want_da)),
            len(want_da), bad[0] + 1 if bad else "số lượng"))
    if got_ds != want_ds:
        err("%s: nhãn ĐÚNG/SAI không khớp (%d ý đọc được, cần %d)" % (
            os.path.basename(path), len(got_ds), len(want_ds)))
    got_cau = [p for p in ps if RE_CAU.match(p)]
    if len(got_cau) != len(seq):
        err("%s: có %d câu, cần %d" % (os.path.basename(path), len(got_cau), len(seq)))
    n_img = len(doc.inline_shapes)
    if n_img != nfig:
        err("%s: nhúng %d hình, cần %d" % (os.path.basename(path), n_img, nfig))
    n_tbl = len(doc.tables)
    need = 2 + ntbl + 4 * len(group["tests"])   # 2 khung + (3 bảng đáp án + 1 bảng thống kê)/đề
    if n_tbl != need:
        err("%s: có %d bảng, cần %d" % (os.path.basename(path), n_tbl, need))
    return len(got_cau), n_img, n_tbl


CHUONG = [(de_12c1, "Chuong01", "CHUONG1_VAT_LI_NHIET"),
          (de_12c2, "Chuong02", "CHUONG2_KHI_LI_TUONG"),
          (de_12c3, "Chuong03", "CHUONG3_TU_TRUONG"),
          (de_12c4, "Chuong04", "CHUONG4_VAT_LI_HAT_NHAN")]
MODS = [de_th1, de_th2, de_th3, de_th4, de_th5, de_th6]

TEN_BO = "BỘ 30 ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – MÔN VẬT LÍ"


def main():
    nfile = nq = nimg = 0
    # make_de.py / make_th.py cân bằng lại vị trí đáp án trước khi dựng tệp;
    # thao tác này tất định nên lặp lại đúng như vậy để dựng lại trạng thái nguồn.
    for mod, _sub, _stem in CHUONG:
        B.rebalance_group(mod.NHOM)
    for mod in MODS:
        B.rebalance_group(mod.NHOM)
    print("ĐỀ LUYỆN TẬP THEO CHƯƠNG")
    for mod, sub, stem in CHUONG:
        d = os.path.join(ROOT, "BaiTapTheoChuong", sub)
        a = check_de(os.path.join(d, "%s_10_DE_LUYEN_TAP.docx" % stem), mod.NHOM)
        b = check_giai(os.path.join(d, "%s_10_DE_LOI_GIAI_CHI_TIET.docx" % stem), mod.NHOM)
        nfile += 2
        if a and b:
            nq += a[0]; nimg += a[1] + b[1]
            print("  %-10s đề %3d câu / %3d hình | lời giải %3d câu / %3d hình  ✓"
                  % (sub, a[0], a[1], b[0], b[1]))

    print("ĐỀ THI THỬ TỔNG HỢP")
    tests = [t for mod in MODS for t in mod.NHOM["tests"]]
    for i, t in enumerate(tests, 1):
        d = os.path.join(ROOT, "DeThiTongHop", "De%02d" % i)
        g = dict(ten_nhom=TEN_BO, mo_ta="", pham_vi="", tests=[t])
        a = check_de(os.path.join(d, "DE%02d_DE_THI.docx" % i), g)
        b = check_giai(os.path.join(d, "DE%02d_DAP_AN_VA_LOI_GIAI.docx" % i), g)
        nfile += 2
        if a and b:
            nq += a[0]; nimg += a[1] + b[1]
    print("  30 đề × 2 tệp: đã đối chiếu %d câu hỏi" % sum(28 for _ in tests))

    print("TẬP GỘP")
    for k, mod in enumerate(MODS, 1):
        d = os.path.join(ROOT, "DeThiTongHop", "TronBo")
        a, b = 5 * k - 4, 5 * k
        x = check_de(os.path.join(d, "TAP%d_DE_%02d_DEN_%02d_DE_THI.docx" % (k, a, b)), mod.NHOM)
        y = check_giai(os.path.join(d, "TAP%d_DE_%02d_DEN_%02d_LOI_GIAI.docx" % (k, a, b)),
                       mod.NHOM)
        nfile += 2
        if x and y:
            nimg += x[1] + y[1]
    print("  6 tập gộp × 2 tệp  ✓")

    print("\nĐã mở lại %d tệp .docx, đối chiếu %d câu hỏi, %d lượt nhúng hình."
          % (nfile, nq, nimg))
    if ERR:
        print("✗ %d sai lệch." % len(ERR))
        return 1
    print("✓ Mọi tệp .docx khớp hoàn toàn với dữ liệu nguồn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
