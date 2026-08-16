# -*- coding: utf-8 -*-
"""Kiểm tra chất lượng hai bộ đề: cấu trúc, hình vẽ, đáp án và TÍNH LẠI ĐỘC LẬP mọi con số.

Chạy:  python3 qc.py
"""
import os
import re
import sys
import math
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
FIGS = os.path.abspath(os.path.join(HERE, "..", "figs"))

import book1
import book2

LETTERS = ["A", "B", "C", "D"]
PROB = []          # danh sách lỗi
WARN = []


def err(msg):
    PROB.append(msg)


def warn(msg):
    WARN.append(msg)


def kind(it):
    if "o" in it:
        return "mc"
    if "items" in it:
        return "ds"
    return "sa"


# --------------------------------------------------------------- 1. cấu trúc
def check_structure(book, name):
    for part, items in (("I", book.P1), ("II", book.P2), ("III", book.P3)):
        for i, it in enumerate(items, 1):
            ref = "%s – Phần %s – Câu %d" % (name, part, i)
            k = kind(it)
            if part == "I" and k != "mc":
                err("%s: phải là câu nhiều phương án lựa chọn" % ref)
            if part == "II" and k != "ds":
                err("%s: phải là câu đúng/sai" % ref)
            if part == "III" and k != "sa":
                err("%s: phải là câu trả lời ngắn" % ref)
            if not it.get("tag"):
                warn("%s: thiếu nhãn kĩ năng (tag)" % ref)
            if it.get("fig"):
                p = os.path.join(FIGS, it["fig"] + ".png")
                if not os.path.exists(p):
                    err("%s: không tìm thấy hình %s" % (ref, it["fig"]))
            if it.get("tbl"):
                cap, head, rows = it["tbl"]
                for r in rows:
                    if len(r) != len(head):
                        err("%s: bảng số liệu lệch số cột" % ref)
            if k == "mc":
                if len(it["o"]) != 4:
                    err("%s: phải có đúng 4 phương án" % ref)
                if it["a"] not in LETTERS:
                    err("%s: đáp án không hợp lệ" % ref)
                if len(set(o.strip().lower() for o in it["o"])) != 4:
                    err("%s: có phương án trùng nhau" % ref)
                if not it.get("sol", "").strip():
                    err("%s: thiếu lời giải" % ref)
            elif k == "ds":
                if len(it["items"]) != 4:
                    err("%s: câu đúng/sai phải có đúng 4 ý (đang có %d)"
                        % (ref, len(it["items"])))
                for j, (txt, val, ex) in enumerate(it["items"]):
                    if not isinstance(val, bool):
                        err("%s ý %d: giá trị đúng/sai không phải kiểu bool" % (ref, j + 1))
                    if not ex.strip():
                        err("%s ý %d: thiếu giải thích" % (ref, j + 1))
                vals = [v for _t, v, _e in it["items"]]
                if all(vals):
                    warn("%s: cả 4 ý đều ĐÚNG" % ref)
                if not any(vals):
                    warn("%s: cả 4 ý đều SAI" % ref)
            else:
                if not it.get("ans", "").strip():
                    err("%s: thiếu đáp số" % ref)
                if not it.get("sol", "").strip():
                    err("%s: thiếu lời giải" % ref)


# --------------------------------------------------------------- 2. trùng lặp
def check_duplicates(book, name):
    texts = []
    for part, items in (("I", book.P1), ("II", book.P2), ("III", book.P3)):
        for i, it in enumerate(items, 1):
            t = it.get("q") or it.get("stem")
            texts.append(("%s – Phần %s – Câu %d" % (name, part, i), t))
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            r = SequenceMatcher(None, texts[i][1], texts[j][1]).ratio()
            if r > 0.82:
                warn("Trùng lặp cao (%.0f%%): %s  ↔  %s" % (r * 100, texts[i][0], texts[j][0]))


# --------------------------------------------------------------- 3. phân bố đáp án
def answer_spread(book, name):
    c = {L: 0 for L in LETTERS}
    for it in book.P1:
        c[it["a"]] += 1
    return c


# --------------------------------------------------------------- 4. tính lại số liệu
def close(a, b, tol=0.012):
    """So khớp tương đối; tol = 1,2% để chấp nhận số liệu đã làm tròn trong đề."""
    if b == 0:
        return abs(a) < 1e-9
    return abs(a - b) / abs(b) <= tol


CHECKS = []


def check(name, computed, stated, tol=0.012):
    ok = close(computed, stated, tol)
    CHECKS.append((name, computed, stated, ok))
    if not ok:
        err("SỐ LIỆU SAI – %s: tính được %.6g, đề/đáp án ghi %.6g" % (name, computed, stated))


def verify_numbers():
    # ---------------- BỘ 1, chương I & II ----------------
    cn, cd, LAM, LHOI = 4200.0, 2100.0, 3.4e5, 2.26e6

    # B1 P1.1 & P3.1 – tỉ số λ/c_rắn từ đồ thị (t1=120 s, ΔT1=100 K, t2=300 s)
    check("B1 λ/c_rắn (K)", 300 * 100 / 120, 250)
    # tỉ số nhiệt dung riêng lỏng/rắn (dùng trong lời giải)
    check("B1 c_lỏng/c_rắn", (100 / 50) / (120 / 100), 5 / 3)

    # B1 P1.2 & P2.5 – chu trình
    check("B1 công chu trình (J)", (3 - 1) * 1e5 * (5 - 2) * 1e-3, 600)
    check("B1 công 2→3 (J)", 3e5 * 3e-3, 900)
    check("B1 công 4→1 (J)", 1e5 * 3e-3, 300)

    # B1 P1.3 – nước đá + nước
    q_toa = 0.3 * cn * 30
    q_ham = 0.2 * cd * 20
    q_conlai = q_toa - q_ham
    q_chayhet = 0.2 * LAM
    check("B1 nhiệt nước toả (J)", q_toa, 37800)
    check("B1 nhiệt hâm đá (J)", q_ham, 8400)
    check("B1 nhiệt còn lại (J)", q_conlai, 29400)
    assert q_conlai < q_chayhet, "đá phải chỉ chảy một phần"
    check("B1 đá đã chảy (g)", q_conlai / LAM * 1000, 86, tol=0.02)
    check("B1 đá còn lại (g)", 200 - q_conlai / LAM * 1000, 114, tol=0.02)
    # đối chứng: giả thiết sai “đá tan hết”
    t_sai = (0.3 * cn * 30 - 0.2 * cd * 20 - 0.2 * LAM) / (0.3 * cn + 0.2 * cn)
    check("B1 nhiệt độ nếu giả thiết sai (°C)", t_sai, -18.4, tol=0.02)
    t_bo_lam = (0.3 * cn * 30 - 0.2 * cd * 20) / (0.3 * cn + 0.2 * cn)
    check("B1 nhiệt độ nếu bỏ nhiệt nóng chảy (°C)", t_bo_lam, 14.0)

    # B1 P1.4 / P2.2 / P3.2 – ống thuỷ ngân
    C = 85 * 40
    check("B1 hằng số Boyle (cmHg·cm)", C, 3400)
    check("B1 ống nghiêng 30° (cm)", C / (75 + 10 * math.sin(math.radians(30))), 42.5)
    check("B1 ống nghiêng dùng cos30 (cm)", C / (75 + 10 * math.cos(math.radians(30))), 40.6, tol=0.02)
    check("B1 ống nằm ngang (cm)", C / 75, 45.3, tol=0.02)
    l_neu_khong_tran = C / (75 - 10)
    check("B1 ống lộn ngược nếu Hg không tràn (cm)", l_neu_khong_tran, 52.3, tol=0.02)
    assert l_neu_khong_tran > 60 - 10, "phải mâu thuẫn thì mới có hiện tượng tràn"
    x = (135 - math.sqrt(135 ** 2 - 4 * 1100)) / 2
    check("B1 Hg còn lại sau khi lộn ngược (cm)", x, 8.7, tol=0.02)
    check("B1 kiểm tra Boyle sau khi tràn", (75 - x) * (60 - x), 3400)

    # B1 P1.6 / P2.6 / P3.6 – thể tích chết
    ps = [1.0, 1.2, 1.5, 2.0, 3.0]
    vs = [55.0, 45.0, 35.0, 25.0, 15.0]
    for p, v in zip(ps, vs):
        check("B1 p(V+5) tại p=%.1f" % p, p * (v + 5.0), 60.0)
    check("B1 V₀ từ hai điểm biên (cm³)", (1.0 * 55 - 3.0 * 15) / (3.0 - 1.0), 5.0)
    check("B1 hằng số Boyle (J)", 1.0e5 * 60e-6, 6.0)
    check("B1 V đọc được khi p=4·10⁵ (cm³)", 60.0 / 4.0 - 5.0, 10.0)

    # B1 P1.7 / P3.9 – xilanh có vấu chặn
    T2 = 300 * 25 / 20
    check("B1 nhiệt độ khi pit-tông chạm vấu (K)", T2, 375)
    check("B1 nhiệt độ để p = 1,8·10⁵ (K)", T2 * 1.8 / 1.2, 562.5)
    check("B1 áp suất tại 500 K (10⁵ Pa)", 1.2 * 500 / T2, 1.6)

    # B1 P1.8 – tỉ số tốc độ căn quân phương
    check("B1 v_He/v_Ar", math.sqrt(40 / 4), 3.16, tol=0.01)

    # B1 P1.12 / P3.10 – nhiệt lượng kế
    Cb = (0.1 * cn * (80 - 38) - 0.2 * cn * (38 - 20)) / (38 - 20)
    check("B1 nhiệt dung bình (J/K)", Cb, 140)
    c_kl = (0.2 * cn * 6 + Cb * 6) / (0.2 * (100 - 26))
    check("B1 nhiệt dung riêng kim loại (J/(kg·K))", c_kl, 397, tol=0.005)
    c_kl_sai = (0.2 * cn * 6) / (0.2 * (100 - 26))
    check("B1 c kim loại nếu bỏ qua bình", c_kl_sai, 341, tol=0.01)

    # B1 P1.13 – Q theo ΔT
    check("B1 c₁ (J/(kg·K))", 2000 / 1.0, 2000)
    check("B1 c₂ (J/(kg·K))", 1600 / 0.4, 4000)
    check("B1 tỉ số c₂/c₁", (1600 / 0.4) / (2000 / 1.0), 2.0)

    # B1 P1.15 / P2.9 – đường thẳng trên p–V
    f = lambda V: (5 - V) * V
    check("B1 pV tại A (10⁵Pa·L)", f(1), 4)
    check("B1 pV tại B (10⁵Pa·L)", f(4), 4)
    check("B1 pV cực đại (10⁵Pa·L)", f(2.5), 6.25)
    check("B1 T_max/T_A", f(2.5) / f(1), 1.5625)
    check("B1 pV cực đại theo J", 2.5e5 * 2.5e-3, 625)

    # B1 P1.16 – tốc độ nguội lạnh
    check("B1 c_B/c_A", 0.50 / 0.20, 2.5)

    # B1 P1.17 / P3.8 – đẳng áp khí đơn nguyên tử
    R = 8.31
    A1 = 0.4 * R * 100
    check("B1 công đẳng áp 0,4 mol (J)", A1, 332.4)
    check("B1 ΔU 0,4 mol (J)", 1.5 * A1, 498.6)
    check("B1 Q 0,4 mol (J)", 2.5 * A1, 831.0)
    A2 = 0.5 * R * 150
    check("B1 Q 0,5 mol 150 K (J)", 2.5 * A2, 1558, tol=0.001)

    # B1 P1.18 / P3.7 – bơm hút chân không
    check("B1 áp suất sau 3 lần bơm (10⁴ Pa)", 10 * 0.8 ** 3, 5.12)
    n = 1
    while 0.8 ** n >= 0.25:
        n += 1
    check("B1 số lần bơm để p < p₀/4", n, 7)

    # B1 P2.1 – đun nước đá thành hơi, P = 200 W
    t1 = 0.1 * cd * 20 / 200
    t2 = 0.1 * LAM / 200
    t3 = 0.1 * cn * 100 / 200
    t4 = 0.1 * LHOI / 200
    check("B1 t hâm đá (s)", t1, 21)
    check("B1 t nóng chảy (s)", t2, 170)
    check("B1 t đun nước (s)", t3, 210)
    check("B1 t hoá hơi (s)", t4, 1130)
    check("B1 tổng thời gian (s)", t1 + t2 + t3 + t4, 1531)

    # B1 P2.3 – mô hình động học phân tử
    k = 1.38e-23
    N = 1.0e5 * 2.0e-3 / (k * 300)
    check("B1 số phân tử (10²²)", N / 1e22, 4.83, tol=0.01)
    check("B1 W̄đ (10⁻²¹ J)", 1.5 * k * 300 / 1e-21, 6.21)
    check("B1 tổng động năng (J)", 1.5 * 1.0e5 * 2.0e-3, 300)
    check("B1 tổng động năng (đối chứng)", N * 1.5 * k * 300, 300)

    # B1 P2.4 / P3.3 – xilanh hai ngăn
    xx = 50 * (400 / 300 - 1) / (400 / 300 + 1)
    check("B1 pit-tông dịch (cm)", xx, 7.1, tol=0.01)
    check("B1 tỉ số thể tích hai ngăn", (50 + xx) / (50 - xx), 4 / 3)
    check("B1 áp suất chung (10⁵ Pa)", 1.0 * 50 / (50 - xx), 1.17, tol=0.01)
    check("B1 áp suất chung (đối chứng ngăn trái)",
          1.0 * (50 / 300) * (400 / (50 + xx)), 1.17, tol=0.01)

    # B1 P2.7 – bình khí nén và van an toàn
    check("B1 nhiệt độ van mở (K)", 300 * 12 / 8, 450)
    check("B1 nhiệt độ van mở (°C)", 300 * 12 / 8 - 273, 177)
    check("B1 áp suất sau rò rỉ (10⁵ Pa)", 0.75 * 8.0, 6.0)
    check("B1 nhiệt độ van mở sau rò rỉ (K)", 300 * 12 / 6, 600)

    # B1 P2.10 – ấm điện
    Pci = 0.8 * 1500
    check("B1 công suất có ích (W)", Pci, 1200)
    check("B1 t đun sôi (s)", 1.5 * cn * 75 / Pci, 393.75)
    check("B1 nước hoá hơi trong 5 phút (kg)", Pci * 300 / LHOI, 0.159, tol=0.01)

    # B1 P3.4 – nước đá 300 g / nước 400 g
    q2 = 0.4 * cn * 25 - 0.3 * cd * 10
    check("B1 nhiệt còn lại cho nóng chảy (J)", q2, 35700)
    assert q2 < 0.3 * LAM
    check("B1 đá còn lại (g)", 300 - q2 / LAM * 1000, 195)

    # B1 P3.5 – khinh khí cầu
    Mkk, Rk = 0.029, 8.31
    ro_ng = 1.0e5 * Mkk / (Rk * 300)
    check("B1 khối lượng riêng không khí ngoài (kg/m³)", ro_ng, 1.1633, tol=0.005)
    ro_tr = ro_ng - 200 / 1000
    check("B1 khối lượng riêng khí trong cầu (kg/m³)", ro_tr, 0.9633, tol=0.005)
    check("B1 nhiệt độ trong cầu (K)", 1.0e5 * Mkk / (Rk * ro_tr), 362, tol=0.005)

    # B1 P3.11 – khí thoát ra
    check("B1 phần trăm khí thoát ra (%)",
          (1 - (1.2e5 / 280) / (2.0e5 / 300)) * 100, 35.7, tol=0.005)

    # B1 P3.12 – bình cứng cách nhiệt
    U1 = 1.5 * 1.5e5 * 0.020
    check("B1 nội năng ban đầu (J)", U1, 4500)
    check("B1 nhiệt độ cuối (K)", 300 * (U1 + 900) / U1, 360)

    # --- các giá trị "bẫy" mới đưa vào phần đúng/sai: phải sai nhưng có nguồn gốc rõ ràng
    check("B1 bẫy tổng thời gian thiếu giai đoạn 3 (s)", t1 + t2 + t4, 1321)
    check("B1 bẫy tổng động năng = pV (J)", 1.0e5 * 2.0e-3, 200)
    check("B1 bẫy công 2→3 lấy nhầm công chu trình (J)", 2e5 * 3e-3, 600)
    check("B1 bẫy hoá hơi khi quên hiệu suất (kg)", 1500 * 300 / LHOI, 0.199, tol=0.01)

    # ---------------- BỘ 2, chương III & IV ----------------
    # B2 P1.1 / P2.1 – ray nghiêng
    m, l, B, Rm, g = 0.02, 0.5, 0.4, 0.2, 10.0
    vmax = m * g * Rm * math.sin(math.radians(30)) / (B ** 2 * l ** 2)
    check("B2 tốc độ cực đại trên ray nghiêng (m/s)", vmax, 0.5)
    check("B2 gia tốc ban đầu (m/s²)", g * math.sin(math.radians(30)), 5.0)
    e = B * l * vmax
    check("B2 suất điện động ở v_max (V)", e, 0.1)
    check("B2 dòng điện ở v_max (A)", e / Rm, 0.5)
    check("B2 công suất toả nhiệt (W)", (e / Rm) ** 2 * Rm, 0.05)
    check("B2 đối chứng bằng công suất trọng lực (W)",
          m * g * vmax * math.sin(math.radians(30)), 0.05)
    check("B2 v_max khi R gấp đôi (m/s)", vmax * 2, 1.0)

    check("B2 bẫy công suất dùng mg thay mg·sinα (W)", m * g * vmax, 0.10)

    # B2 P1.2 / P2.2 – đồ thị Φ(t)
    check("B2 |e| giai đoạn I (V)", 0.4 / 2, 0.20)
    check("B2 |e| giai đoạn III (V)", 0.4 / 1, 0.40)
    check("B2 |e| giai đoạn IV (V)", 0.6 / 3, 0.20)
    check("B2 dòng điện khi N=20, R=2 (A)", 20 * 0.4 / 2, 4.0)
    check("B2 bẫy quên nhân số vòng (A)", 0.4 / 2, 0.2)

    # B2 P1.3 – máy biến áp quấn thêm 60 vòng
    N1 = 60 / (25 / 200 - 20 / 200)
    check("B2 số vòng sơ cấp", N1, 2400)
    check("B2 số vòng thứ cấp", 0.1 * N1, 240)

    # B2 P1.4 – tỉ lệ thời gian |i| > I_hd
    phi = math.degrees(math.acos(1 / math.sqrt(2)))
    check("B2 tỉ lệ thời gian (%)", 4 * phi / 360 * 100, 50.0)

    # B2 P1.5 / P2.4 – khung dây quay
    om = 2 * math.pi * 300 / 60
    P0 = 200 * 0.2 * 100e-4
    check("B2 tốc độ góc (rad/s)", om, 31.42, tol=0.005)
    check("B2 tần số (Hz)", 300 / 60, 5)
    check("B2 từ thông cực đại (Wb)", P0, 0.4)
    check("B2 sđđ cực đại (V)", om * P0, 12.57, tol=0.005)
    check("B2 sđđ hiệu dụng (V)", om * P0 / math.sqrt(2), 8.9, tol=0.005)

    # B2 P1.6 – thanh treo lò xo
    F = 0.4 * 2 * 0.25
    check("B2 lực từ (N)", F, 0.20)
    check("B2 độ cứng mỗi lò xo (N/m)", (F / 2) / 0.01, 10)

    # B2 P1.7 – từ thông và góc
    check("B2 từ thông (Wb)", 50 * 0.1 * 0.06 * math.cos(math.radians(60)), 0.15)
    check("B2 từ thông nếu nhầm cos30 (Wb)",
          50 * 0.1 * 0.06 * math.cos(math.radians(30)), 0.26, tol=0.01)

    # B2 P1.8 – phản ứng D–T theo ε
    check("B2 W_lk(²H) (MeV)", 1.11 * 2, 2.22)
    check("B2 W_lk(³H) (MeV)", 2.83 * 3, 8.49)
    check("B2 W_lk(⁴He) (MeV)", 7.07 * 4, 28.28)
    check("B2 năng lượng D–T (MeV)", 7.07 * 4 - 1.11 * 2 - 2.83 * 3, 17.6, tol=0.01)
    check("B2 bẫy cộng trừ ε (MeV)", 7.07 - 1.11 - 2.83, 3.13, tol=0.01)

    # B2 P1.9 – máy đếm
    check("B2 chu kì bán rã từ tỉ số (giờ)", 12 / math.log2(4800 / 600), 4)

    # B2 P1.10 / P3.9 – định tuổi ¹⁴C
    check("B2 tuổi gỗ (năm, 20%)", 5730 * math.log2(1 / 0.20), 13305, tol=0.005)
    check("B2 tuổi xương (năm, 1/3)", 5730 * math.log2(3), 9082, tol=0.005)

    # B2 P1.11 – nhà máy 500 MW
    NA, MeV = 6.02e23, 1.6e-13
    E = (500e6 / 0.20) * 86400
    Nf = E / (200 * MeV)
    check("B2 năng lượng mỗi ngày (10¹⁴ J)", E / 1e14, 2.16)
    check("B2 số phân hạch mỗi ngày (10²⁴)", Nf / 1e24, 6.75)
    check("B2 khối lượng U mỗi ngày (kg)", Nf / NA * 235 / 1000, 2.64, tol=0.005)
    check("B2 bẫy quên hiệu suất (kg)", Nf / NA * 235 / 1000 * 0.2, 0.53, tol=0.01)

    # B2 P1.14 – chuỗi U-238 → Pb-206
    nalpha = (238 - 206) / 4
    nbeta = 82 - (92 - 2 * nalpha)
    check("B2 số hạt α", nalpha, 8)
    check("B2 số hạt β⁻", nbeta, 6)
    check("B2 tổng số hạt", nalpha + nbeta, 14)
    check("B2 tỉ số khối lượng Pb/U sau 1 chu kì", 206 / 238, 0.866, tol=0.005)

    # B2 P1.16 – số hạt đã phân rã
    lam = math.log(2) / (15 * 3600)
    N1_ = 4.0e10 / lam
    check("B2 λ (10⁻⁵ s⁻¹)", lam / 1e-5, 1.284, tol=0.005)
    check("B2 N₁ (10¹⁵)", N1_ / 1e15, 3.12, tol=0.005)
    check("B2 N₂ (10¹⁴)", N1_ / 4 / 1e14, 7.79, tol=0.005)
    check("B2 ΔN (10¹⁵)", N1_ * 0.75 / 1e15, 2.34, tol=0.005)

    # B2 P1.17 / P2.3 / P3.10 – truyền tải
    I = 600e6 / 500e3
    dP = I ** 2 * 10
    check("B2 dòng trên đường dây (A)", I, 1200)
    check("B2 hao phí (MW)", dP / 1e6, 14.4)
    check("B2 tỉ lệ hao phí (%)", dP / 600e6 * 100, 2.40)
    check("B2 tỉ số vòng dây", 500 / 20, 25)
    check("B2 bẫy lập tỉ số ngược", 20 / 500, 0.04)
    check("B2 hao phí tăng bao nhiêu lần khi hạ áp", (500 / 20) ** 2, 625)
    check("B2 hiệu suất sau khi tăng U hai lần (%)", 100 - 10 / 4, 97.5)

    # B2 P1.18 / P3.2 – khung vào vùng từ trường
    a_, Rk2, v_, B_ = 0.2, 0.5, 2.0, 0.4
    e2 = B_ * a_ * v_
    I2 = e2 / Rk2
    Q1 = I2 ** 2 * Rk2 * (a_ / v_)
    check("B2 sđđ khi vào (V)", e2, 0.16)
    check("B2 dòng khi vào (A)", I2, 0.32)
    check("B2 nhiệt một lần qua biên (10⁻³ J)", Q1 / 1e-3, 5.12)
    check("B2 tổng nhiệt (10⁻² J)", 2 * Q1 / 1e-2, 1.02, tol=0.005)
    check("B2 lực từ lên khung (10⁻² N)", B_ * I2 * a_ / 1e-2, 2.56)

    # B2 P2.5 / P3.7 / P3.11 – ²¹⁰Po
    N0 = (1.00 / 210) * NA
    lam_po = math.log(2) / (138 * 86400)
    check("B2 N₀ của Po (10²¹)", N0 / 1e21, 2.87, tol=0.005)
    check("B2 λ của Po (10⁻⁸ s⁻¹)", lam_po / 1e-8, 5.81, tol=0.005)
    check("B2 H₀ của Po (10¹⁴ Bq)", lam_po * N0 / 1e14, 1.67, tol=0.005)
    check("B2 khối lượng Pb sau 2T (g)", 0.75 * (1.00 / 210) * 206, 0.736, tol=0.005)
    r = 0.25 * 210 / 206
    tt = 138 * math.log2(1 + r)
    check("B2 thời gian để m_Pb/m_Po = 0,25 (ngày)", tt, 45.2, tol=0.005)
    check("B2 bẫy dùng thẳng tỉ số khối lượng (ngày)", 138 * math.log2(1.25), 44.4, tol=0.005)
    check("B2 động năng hạt α (MeV)", 5.40 * 206 / 210, 5.30, tol=0.005)
    check("B2 động năng hạt Pb (MeV)", 5.40 * 4 / 210, 0.103, tol=0.02)

    # B2 P2.6 – phản ứng D–D
    mD, mHe3, mn, mp, u = 2.0136, 3.0149, 1.00870, 1.00728, 931.5
    dm = 2 * mD - (mHe3 + mn)
    check("B2 độ hụt khối D–D (u)", dm, 0.0036, tol=0.02)
    check("B2 năng lượng D–D (MeV)", dm * u, 3.35, tol=0.01)
    eD = (mp + mn - mD) * u / 2
    eHe = (2 * mp + mn - mHe3) * u / 3
    check("B2 ε(²H) (MeV/nuclôn)", eD, 1.11, tol=0.01)
    check("B2 ε(³He) (MeV/nuclôn)", eHe, 2.60, tol=0.01)
    assert eHe > eD

    # B2 P2.7 – cân dòng điện
    for I_, dm_g in zip([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0]):
        check("B2 B từ số liệu I=%.1f A (T)" % I_,
              (dm_g * 1e-3 * 10) / (I_ * 0.05), 0.2)
    check("B2 số chỉ khi quay 30° với I=4 A (g)", 4.0 * math.sin(math.radians(60)), 3.46, tol=0.01)
    check("B2 giá trị bẫy dùng cos60° (g)", 4.0 * math.cos(math.radians(60)), 2.0)

    # B2 P2.9 – nhiệt hạch so với phân hạch
    check("B2 nhiệt hạch mỗi nuclôn (MeV)", 17.6 / 5, 3.52)
    check("B2 phân hạch mỗi nuclôn (MeV)", 200 / 236, 0.85, tol=0.01)

    # B2 P2.10 – bảng độ phóng xạ
    for t_, H_ in zip([0, 2, 4, 6, 8], [800, 566, 400, 283, 200]):
        check("B2 H(t=%d h) (kBq)" % t_, 800 * 2 ** (-t_ / 4.0), H_, tol=0.005)
    check("B2 H sau 12 h (kBq)", 800 / 2 ** 3, 100)

    # B2 P3.1 – ray nằm ngang
    check("B2 v_max ray ngang (m/s)", 0.2 * 0.4 / (0.5 ** 2 * 0.4 ** 2), 2.0)

    # B2 P3.3 – vòng quấn ngược
    check("B2 số vòng quấn ngược", (120 - 0.1 * 1000) / 2, 10)

    # B2 P3.4 – nhiệt lượng dòng xoay chiều
    check("B2 nhiệt lượng AC (kJ)", (4 / math.sqrt(2)) ** 2 * 25 * 300 / 1000, 60)

    # B2 P3.5 – sđđ trung bình khi quay khung
    F1 = 100 * 0.05 * 200e-4
    check("B2 Φ₁ (Wb)", F1, 0.1)
    check("B2 sđđ trung bình (V)", (F1 - F1 * math.cos(math.radians(60))) / 0.2, 0.25)

    # B2 P3.6 – năng lượng liên kết riêng của Fe-56
    dmFe = 26 * 1.00728 + 30 * 1.00866 - 55.9206
    check("B2 độ hụt khối Fe-56 (u)", dmFe, 0.52848, tol=0.001)
    check("B2 W_lk Fe-56 (MeV)", dmFe * 931.5, 492.3, tol=0.002)
    check("B2 ε Fe-56 (MeV/nuclôn)", dmFe * 931.5 / 56, 8.79, tol=0.002)

    # B2 P3.8 – 1 tấn U-235 mỗi năm
    Nt = (1.00e6 / 235) * NA
    Pel = Nt * 200 * MeV * 0.25 / (365 * 86400)
    check("B2 số hạt trong 1 tấn (10²⁷)", Nt / 1e27, 2.562, tol=0.005)
    check("B2 công suất điện (MW)", Pel / 1e6, 650, tol=0.005)

    # B2 P3.12 – số phân hạch mỗi giây
    check("B2 số phân hạch mỗi giây (10¹⁹)",
          (1000e6 / 0.32) / (200 * MeV) / 1e19, 9.77, tol=0.005)


# --------------------------------------------------------------- chạy
def main():
    check_structure(book1, "BỘ 1")
    check_structure(book2, "BỘ 2")
    check_duplicates(book1, "BỘ 1")
    check_duplicates(book2, "BỘ 2")
    verify_numbers()

    n1 = len(book1.P1) + len(book1.P2) + len(book1.P3)
    n2 = len(book2.P1) + len(book2.P2) + len(book2.P3)
    print("Số câu BỘ 1: %d  (I: %d, II: %d, III: %d)"
          % (n1, len(book1.P1), len(book1.P2), len(book1.P3)))
    print("Số câu BỘ 2: %d  (I: %d, II: %d, III: %d)"
          % (n2, len(book2.P1), len(book2.P2), len(book2.P3)))
    print("Tổng số ý đúng/sai: %d"
          % (4 * (len(book1.P2) + len(book2.P2))))
    print("Phân bố đáp án Phần I – BỘ 1:", answer_spread(book1, "BỘ 1"))
    print("Phân bố đáp án Phần I – BỘ 2:", answer_spread(book2, "BỘ 2"))
    print("Số phép kiểm tra số liệu: %d, đạt: %d"
          % (len(CHECKS), sum(1 for c in CHECKS if c[3])))

    if WARN:
        print("\n--- CẢNH BÁO (%d) ---" % len(WARN))
        for w in WARN:
            print("  •", w)
    if PROB:
        print("\n--- LỖI (%d) ---" % len(PROB))
        for p in PROB:
            print("  ✗", p)
        return 1
    print("\n✓ Không phát hiện lỗi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
