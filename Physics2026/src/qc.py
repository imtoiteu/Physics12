# -*- coding: utf-8 -*-
"""Kiểm tra chất lượng ngân hàng đề THPT 2026.

Chạy:  python3 qc.py [tên_module ...]
"""
import os
import re
import sys
import importlib
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
FIGS = os.path.abspath(os.path.join(HERE, "..", "figs"))

LETTERS = ["A", "B", "C", "D"]
MUC = {"Dễ", "Trung bình", "Khó", "Rất khó"}
ERRORS, WARNS = [], []

UNIT = (r"(?:\bcm\b|\bmm\b|\bkm\b|\bg\b|\bkg\b|\bs\b|\bJ\b|\bkJ\b|\bK\b|°C|°X|\bPa\b|"
        r"\bN\b|\bW\b|\bmol\b|\bHz\b|\bL\b|%|\bphút\b|\bgiây\b|\bgiờ\b|\bngày\b|\bnăm\b|"
        r"\bvòng\b|\bm/s|\brad/s|\bMeV|\blít\b|\bm³|\bcm³|\bm²|\bBq\b|\bviên\b|\blần\b|"
        r"\bWb\b|\bT\b|\bV\b|\bkV\b|\bA\b|\bmA\b|\bΩ\b|\bkW\b|\bMW\b|\bmJ\b|\bC\b|\bu\b|\bMeV\b)")

NUM = re.compile(r"\d[\d  ]*(?:[,.]\d+)?")


def err(m):
    ERRORS.append(m)


def warn(m):
    WARNS.append(m)


def numbers(text):
    """Tập các số xuất hiện trong một đoạn văn bản tiếng Việt (dấu phẩy thập phân)."""
    out = set()
    for mt in NUM.finditer(str(text)):
        t = mt.group().replace(" ", "").replace(" ", "").replace(",", ".")
        if t.count(".") > 1:
            t = t.replace(".", "", t.count(".") - 1)
        try:
            v = float(t)
        except ValueError:
            continue
        out.add(round(v, 6))
        if v != 0:                      # chấp nhận sai khác về bậc 10 (kJ ↔ J, 10⁵…)
            x = v
            for _ in range(8):
                x *= 10
                out.add(round(x, 6))
            x = v
            for _ in range(8):
                x /= 10
                out.add(round(x, 6))
    return out


def raw_numbers(text):
    """Các số xuất hiện đúng như trong văn bản (không nhân/chia bậc 10)."""
    out = set()
    for mt in NUM.finditer(str(text)):
        t = mt.group().replace(" ", "").replace(" ", "").replace(",", ".")
        if t.count(".") > 1:
            t = t.replace(".", "", t.count(".") - 1)
        try:
            out.add(round(float(t), 6))
        except ValueError:
            pass
    return out


def result_numbers(sol):
    """Các con số KẾT QUẢ trong lời giải: số nằm sau dấu “=” hoặc “⇒” cuối cùng của mỗi dòng.

    Đây là phép kiểm mạnh nhất của bộ QC: nếu đáp số ghi trong đề không trùng với bất kì
    kết quả trung gian nào của lời giải thì gần như chắc chắn đã sai ở khâu ghi đáp án.
    """
    out = set()
    for line in str(sol).split("\n"):
        for sep in ("⟹", "⇒", "→", "≈", "≥", "≤", "="):
            if sep in line:
                out |= raw_numbers(line.rsplit(sep, 1)[1])
        out |= raw_numbers(line.rsplit("=", 1)[-1]) if "=" in line else set()
    return out


SELF_FIX = re.compile(r"tính lại|xét lại|kiểm tra lại phép|— tính|là SAI\.\.\.|\?\s*—|"
                      r"nhận định này|sai sót ở bước|đề chưa nói rõ|chưa nói rõ|phương án đúng là|không khớp|giá trị đúng là", re.IGNORECASE)


def check_prose(ref, text, where):
    """Phát hiện dấu vết tự sửa chữa còn sót trong lời giải (dấu hiệu tác giả tính nhầm)."""
    m = SELF_FIX.search(str(text))
    if m:
        err("%s: %s còn dấu vết tự sửa chữa «…%s…» – cần viết lại cho dứt khoát"
            % (ref, where, str(text)[max(0, m.start() - 25):m.end() + 25].replace("\n", " ")))


def kind_of(it):
    if "o" in it:
        return "mc"
    if "items" in it:
        return "ds"
    return "sa"


def check_item(ref, it, part):
    k = kind_of(it)
    want = {"I": "mc", "II": "ds", "III": "sa"}[part]
    if k != want:
        err("%s: sai loại câu (cần %s)" % (ref, want))
        return
    for _f in ("q", "stem", "sol"):
        if it.get(_f):
            check_prose(ref, it[_f], "lời giải" if _f == "sol" else "đề bài")
    if k == "ds":
        for _j, _t in enumerate(it.get("items", [])):
            if len(_t) == 3:
                check_prose(ref, _t[2], "giải thích ý %d" % (_j + 1))
    if it.get("md") not in MUC:
        err("%s: mức độ không hợp lệ (%r)" % (ref, it.get("md")))
    if not it.get("kn", "").strip():
        err("%s: thiếu kiến thức – kĩ năng" % ref)
    if it.get("fig") and not os.path.exists(os.path.join(FIGS, it["fig"] + ".png")):
        err("%s: không có hình %s" % (ref, it["fig"]))
    if it.get("fig") and not it.get("cap"):
        warn("%s: hình chưa có chú thích" % ref)
    if it.get("tbl"):
        _cap, head, rows = it["tbl"]
        for r in rows:
            if len(r) != len(head):
                err("%s: bảng lệch số cột" % ref)

    if k == "mc":
        o = it["o"]
        if len(o) != 4:
            err("%s: phải có 4 phương án" % ref)
        if it["a"] not in LETTERS:
            err("%s: đáp án %r không hợp lệ" % (ref, it["a"]))
            return
        if len(set(x.strip().lower() for x in o)) != 4:
            err("%s: có phương án trùng nhau" % ref)
        if not it.get("sol", "").strip():
            err("%s: thiếu lời giải" % ref)
            return
        # đáp số trong phương án đúng phải xuất hiện trong lời giải
        good = o[LETTERS.index(it["a"])]
        # chỉ kiểm tra với phương án mang tính đáp số (ngắn, chủ yếu là con số)
        # Chỉ kiểm tra những phương án thực sự là ĐÁP SỐ: ngắn, có đơn vị hoặc dấu
        # thập phân. Bỏ qua phương án dạng công thức (T/4, 2A, ωA…) và nhãn “(2) và (4)”.
        core = re.sub(r"\([^)]*\)", " ", good)
        has_unit = re.search(UNIT, core) is not None
        gnums = ({v for v in numbers(core) if v >= 1.5}
                 if len(good) <= 34 and (has_unit or "," in core) else set())
        if gnums:
            snums = numbers(it["sol"]) | numbers(it.get("q", ""))
            exact = {round(v, 6) for v in raw_numbers(core)}
            sol_exact = {round(v, 6) for v in raw_numbers(it["sol"] + " " + it.get("q", ""))}
            if not (gnums & snums):
                err("%s: số trong phương án đúng (%s) không xuất hiện trong lời giải"
                    % (ref, good.strip()[:40]))
            elif exact and not (exact & sol_exact):
                warn("%s: đáp số “%s” chỉ khớp lời giải sau khi đổi bậc 10 – nên kiểm tra lại"
                     % (ref, good.strip()[:40]))
            elif exact and not (exact & result_numbers(it["sol"])):
                warn("%s: phương án đúng “%s” không trùng kết quả nào của lời giải – "
                     "nên đối chiếu lại đáp án" % (ref, good.strip()[:40]))
    elif k == "ds":
        if len(it["items"]) != 4:
            err("%s: câu đúng/sai phải có 4 ý (đang có %d)" % (ref, len(it["items"])))
        vals = []
        for j, tup in enumerate(it["items"]):
            if len(tup) != 3:
                err("%s ý %d: cấu trúc phải là (nội dung, Đúng/Sai, giải thích)" % (ref, j + 1))
                continue
            txt, val, ex = tup
            if not isinstance(val, bool):
                err("%s ý %d: giá trị đúng/sai không phải bool" % (ref, j + 1))
            if not ex.strip():
                err("%s ý %d: thiếu giải thích" % (ref, j + 1))
            head = ex.strip()[:6].lower()
            if val and head.startswith("sai"):
                err("%s ý %d: đánh dấu ĐÚNG nhưng lời giải mở đầu bằng “Sai”" % (ref, j + 1))
            if (not val) and head.startswith("đúng"):
                err("%s ý %d: đánh dấu SAI nhưng lời giải mở đầu bằng “Đúng”" % (ref, j + 1))
            vals.append(val)
        if vals and all(vals):
            warn("%s: cả 4 ý đều ĐÚNG" % ref)
        if vals and not any(vals):
            warn("%s: cả 4 ý đều SAI" % ref)
    else:
        if not str(it.get("ans", "")).strip():
            err("%s: thiếu đáp số" % ref)
        if not it.get("sol", "").strip():
            err("%s: thiếu lời giải" % ref)
        else:
            anums = {v for v in numbers(it.get("ans", "")) if v >= 1.5}
            if anums and not (anums & numbers(it["sol"])):
                err("%s: đáp số %r không xuất hiện trong lời giải" % (ref, it["ans"]))
            # kiểm tra CHẶT: đáp số phải trùng với một con số KẾT QUẢ của lời giải
            # (số đứng sau dấu = hoặc ⇒), không chấp nhận sai khác bậc 10.
            a_exact = {v for v in raw_numbers(it.get("ans", ""))}
            if a_exact:
                if not (a_exact & raw_numbers(it["sol"])):
                    err("%s: đáp số “%s” KHÔNG khớp con số nào trong lời giải"
                        % (ref, str(it["ans"])[:30]))
                elif not (a_exact & result_numbers(it["sol"])):
                    err("%s: đáp số “%s” không trùng kết quả nào của lời giải "
                        "(chỉ trùng số liệu đề bài) – nhiều khả năng ghi sai đáp án"
                        % (ref, str(it["ans"])[:30]))


def check_test(t, gname):
    ref0 = "%s/%s" % (gname, t["ma"])
    for key in ("ma", "ten", "muc", "trongtam"):
        if not t.get(key):
            err("%s: thiếu trường %s" % (ref0, key))
    sizes = {"P1": 18, "P2": 4, "P3": 6}
    for key, n in sizes.items():
        if len(t.get(key, [])) != n:
            err("%s: %s phải có %d câu, đang có %d" % (ref0, key, n, len(t.get(key, []))))
    for key, part in (("P1", "I"), ("P2", "II"), ("P3", "III")):
        for i, it in enumerate(t.get(key, []), 1):
            check_item("%s Phần %s câu %d" % (ref0, part, i), it, part)
    # phân bố đáp án phần I
    cnt = {L: 0 for L in LETTERS}
    for it in t.get("P1", []):
        if it.get("a") in cnt:
            cnt[it["a"]] += 1
    if cnt and max(cnt.values()) > 8:
        warn("%s: đáp án Phần I lệch (%s)" % (ref0, cnt))
    if cnt and min(cnt.values()) == 0:
        warn("%s: Phần I không có đáp án %s"
             % (ref0, [L for L in LETTERS if cnt[L] == 0]))
    return cnt


def check_group(mod, gname):
    tests = [getattr(mod, n) for n in dir(mod) if re.fullmatch(r"DE\d+", n)]
    tests.sort(key=lambda t: t["ma"])
    total = {L: 0 for L in LETTERS}
    for t in tests:
        c = check_test(t, gname)
        for L in LETTERS:
            total[L] += c[L]
    # trùng lặp giữa các câu trong cùng nhóm
    texts = []
    for t in tests:
        for key, part in (("P1", "I"), ("P2", "II"), ("P3", "III")):
            for i, it in enumerate(t.get(key, []), 1):
                texts.append(("%s/%s.%d" % (t["ma"], part, i),
                              (it.get("q") or it.get("stem") or "")))
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            r = SequenceMatcher(None, texts[i][1], texts[j][1]).ratio()
            if r > 0.88:
                warn("Trùng %.0f%%: %s ↔ %s" % (r * 100, texts[i][0], texts[j][0]))
    return tests, total


def main(mods):
    grand = 0
    for name in mods:
        mod = importlib.import_module(name)
        tests, total = check_group(mod, name)
        n = sum(len(t["P1"]) + len(t["P2"]) + len(t["P3"]) for t in tests)
        grand += n
        cnt = {}
        for t in tests:
            for key in ("P1", "P2", "P3"):
                for it in t[key]:
                    cnt[it.get("md")] = cnt.get(it.get("md"), 0) + 1
        print("%-12s %2d đề, %4d câu | đáp án Phần I %s | mức độ %s"
              % (name, len(tests), n, total,
                 {k: cnt.get(k, 0) for k in ["Dễ", "Trung bình", "Khó", "Rất khó"]}))
    print("TỔNG SỐ CÂU:", grand)
    if WARNS:
        print("\n--- CẢNH BÁO (%d) ---" % len(WARNS))
        for w in WARNS[:40]:
            print("  •", w)
    if ERRORS:
        print("\n--- LỖI (%d) ---" % len(ERRORS))
        for e in ERRORS:
            print("  ✗", e)
        return 1
    print("\n✓ Không phát hiện lỗi cấu trúc.")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:] or ["de_12c1"]
    sys.exit(main(args))
