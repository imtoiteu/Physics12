# -*- coding: utf-8 -*-
"""Hình minh hoạ CHƯƠNG IV – VẬT LÍ HẠT NHÂN."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, FancyArrowPatch, Ellipse, Polygon, Wedge

from figbase import (save, arrow, clean, frame, RED, BLUE, GREEN, ORANGE, GREY,
                     PURPLE, TEAL, BROWN, PINK, LGREY)

MADE = []
PROT, NEUT = "#e74c3c", "#5d6d7e"


def _reg(n):
    MADE.append(n)
    return n


def _nucleus(ax, cx, cy, nz, nn, r=0.115, spread=0.42, seed=3):
    """Vẽ cụm nuclêôn: proton đỏ (p), nơtron xám (n)."""
    rng = np.random.default_rng(seed)
    pts, tries = [], 0
    while len(pts) < nz + nn and tries < 4000:
        tries += 1
        a, rr = rng.uniform(0, 2 * np.pi), spread * np.sqrt(rng.uniform(0, 1))
        x, y = cx + rr * np.cos(a), cy + rr * np.sin(a)
        if all((x - px) ** 2 + (y - py) ** 2 > (1.85 * r) ** 2 for px, py in pts):
            pts.append((x, y))
    for k, (x, y) in enumerate(pts):
        isp = k < nz
        ax.add_patch(Circle((x, y), r, fc=PROT if isp else NEUT,
                            ec="#7b241c" if isp else "#2c3e50", lw=0.8, zorder=4))
        ax.text(x, y, "p" if isp else "n", fontsize=r * 52, color="white",
                ha="center", va="center", zorder=5)
    return pts


# ------------------------------------------------------------------ 1. cấu trúc hạt nhân
def h_sd_cautruc():
    fig, ax = plt.subplots(figsize=(6.6, 3.5))
    _nucleus(ax, -1.55, 0, 3, 4, r=0.19, spread=0.52, seed=7)
    ax.add_patch(Circle((-1.55, 0), 0.80, fill=False, ec=GREY, ls="--", lw=1.2))
    ax.text(-1.55, -1.05, "Hạt nhân liti  ${}^{7}_{3}$Li", fontsize=12, ha="center",
            va="top", color="#34495e")
    ax.text(-1.55, -1.55, "3 prôtôn + 4 nơtron = 7 nuclêôn", fontsize=9.4, ha="center",
            va="top", color=GREY)
    ax.add_patch(Circle((0.75, 0.62), 0.15, fc=PROT, ec="#7b241c", lw=0.9))
    ax.text(1.05, 0.62, "prôtôn:  điện tích +e,  khối lượng ≈ 1,0073 u", fontsize=9.6,
            va="center", color="#34495e")
    ax.add_patch(Circle((0.75, 0.12), 0.15, fc=NEUT, ec="#2c3e50", lw=0.9))
    ax.text(1.05, 0.12, "nơtron:  không mang điện,  khối lượng ≈ 1,0087 u", fontsize=9.6,
            va="center", color="#34495e")
    ax.text(0.75, -0.62, "Kí hiệu hạt nhân:   ${}^{A}_{Z}$X", fontsize=13, color=GREEN,
            va="center")
    ax.text(0.78, -1.12, "Z = số prôtôn = số thứ tự ô trong bảng tuần hoàn\n"
                         "A = số nuclêôn (số khối);   số nơtron  N = A − Z",
            fontsize=9.4, color=GREY, va="top")
    clean(ax, -2.7, 5.4, -2.0, 1.25, eq=False)
    save(fig, "h_sd_cautruc")
    return _reg("h_sd_cautruc")


# ------------------------------------------------------------------ 2. độ hụt khối
def h_sd_dohutkhoi():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    for k in range(2):
        ax.add_patch(Circle((-2.75 + 0.42 * k, 0.55), 0.17, fc=PROT, ec="#7b241c", lw=0.9))
        ax.text(-2.75 + 0.42 * k, 0.55, "p", fontsize=9, color="white", ha="center", va="center")
        ax.add_patch(Circle((-2.75 + 0.42 * k, 0.05), 0.17, fc=NEUT, ec="#2c3e50", lw=0.9))
        ax.text(-2.75 + 0.42 * k, 0.05, "n", fontsize=9, color="white", ha="center", va="center")
    ax.text(-2.54, -0.45, "2 prôtôn + 2 nơtron\nkhi còn RỜI NHAU", fontsize=9.4,
            ha="center", va="top", color="#34495e")
    ax.text(-2.54, -1.25, r"$2m_p + 2m_n = 4{,}0320$ u", fontsize=11, ha="center",
            va="top", color=RED)
    arrow(ax, -1.45, 0.28, -0.35, 0.28, color=GREEN, lw=2.2, ms=16)
    ax.text(-0.9, 0.48, "kết hợp lại", fontsize=9.4, color=GREEN, ha="center")
    _nucleus(ax, 0.55, 0.28, 2, 2, r=0.17, spread=0.30, seed=5)
    ax.add_patch(Circle((0.55, 0.28), 0.58, fill=False, ec=GREY, ls="--", lw=1.1))
    ax.text(0.55, -0.45, "hạt nhân ${}^{4}_{2}$He", fontsize=10.5, ha="center",
            va="top", color="#34495e")
    ax.text(0.55, -1.25, r"$m_{He} = 4{,}0015$ u", fontsize=11, ha="center", va="top",
            color=BLUE)
    ax.text(2.75, 0.75, "KHỐI LƯỢNG BỊ HỤT ĐI", fontsize=10, color=PURPLE, ha="center",
            fontweight="bold")
    ax.text(2.75, 0.25, r"$\Delta m = 0{,}0305$ u", fontsize=12, color=PURPLE, ha="center")
    ax.text(2.75, -0.35, "đã chuyển thành\nnăng lượng liên kết", fontsize=9.4,
            color=PURPLE, ha="center", va="center")
    ax.text(2.75, -1.15, r"$W_{lk} = \Delta m\,c^2 = 28{,}4$ MeV", fontsize=11,
            color=GREEN, ha="center")
    ax.text(0, 1.55, "Muốn PHÁ VỠ hạt nhân thành các nuclêôn riêng lẻ phải cung cấp đúng "
                     "năng lượng liên kết đó",
            fontsize=9.6, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.3, 4.3, -2.0, 1.9, eq=False)
    save(fig, "h_sd_dohutkhoi")
    return _reg("h_sd_dohutkhoi")


# ------------------------------------------------------------------ 3. ba tia phóng xạ
def h_sd_tia_phongxa():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.add_patch(Rectangle((-3.1, -0.42), 0.85, 0.84, fc="#d5d8dc", ec="#566573", lw=1.5))
    ax.add_patch(Rectangle((-2.85, -0.16), 0.62, 0.32, fc="#2c3e50", ec="none"))
    ax.text(-2.68, -0.62, "nguồn phóng xạ\ntrong hộp chì", fontsize=8.8, color=GREY,
            ha="center", va="top")
    ax.add_patch(Rectangle((-1.6, 1.15), 4.2, 0.26, fc="#f5b7b1", ec="#c0392b", lw=1.2))
    ax.text(-1.75, 1.28, "bản (+)", fontsize=9.4, color=RED, ha="right", va="center")
    ax.add_patch(Rectangle((-1.6, -1.41), 4.2, 0.26, fc="#aed6f1", ec="#2874a6", lw=1.2))
    ax.text(-1.75, -1.28, "bản (−)", fontsize=9.4, color=BLUE, ha="right", va="center")
    x = np.linspace(-2.2, 2.5, 200)
    xa = np.clip(x + 1.6, 0, None)
    ax.plot(x, -0.10 * xa ** 2 * 0.26, color=RED, lw=2.2)
    ax.text(2.70, -0.62, r"$\alpha$  (${}^{4}_{2}$He, điện tích +2e)", fontsize=10.5,
            color=RED, ha="left", va="center")
    ax.plot(x, 0.10 * xa ** 2 * 0.62, color=BLUE, lw=2.2)
    ax.text(2.70, 0.78, r"$\beta^-$  (electron, điện tích −e)", fontsize=10.5,
            color=BLUE, ha="left", va="center")
    ax.plot(x, 0 * x, color=GREEN, lw=2.2, ls="-")
    ax.text(2.70, 0.08, r"$\gamma$  (sóng điện từ, không mang điện)", fontsize=10.5,
            color=GREEN, ha="left", va="center")
    ax.text(0, -2.15,
            "Tia lệch về bản ÂM ⇒ mang điện DƯƠNG (tia α).  Tia lệch về bản DƯƠNG ⇒ mang điện ÂM (tia β⁻).\n"
            "Tia đi thẳng ⇒ không mang điện (tia γ).  Độ lệch còn phụ thuộc khối lượng: α nặng nên lệch ít hơn β.",
            fontsize=9.2, color="#34495e", ha="center", va="center")
    clean(ax, -3.9, 7.2, -2.9, 1.8, eq=False)
    save(fig, "h_sd_tia_phongxa")
    return _reg("h_sd_tia_phongxa")


# ------------------------------------------------------------------ 4. khả năng đâm xuyên
def h_sd_dam_xuyen():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    walls = [(-0.3, "#f7dc6f", "tờ giấy", -1.18), (1.9, "#aab7b8", "lá nhôm\nvài mm", -1.18),
             (4.1, "#5d6d7e", "khối chì /\nbê tông dày", -1.18)]
    for x, c, lab, ly in walls:
        ax.add_patch(Rectangle((x, -1.0), 0.24, 2.0, fc=c, ec="#34495e", lw=1.2))
        ax.text(x + 0.12, ly, lab, fontsize=9.0, color="#34495e", ha="center", va="top")
    for y, col, name, stop in ((0.62, RED, r"$\alpha$", -0.3),
                               (0.0, BLUE, r"$\beta$", 1.9),
                               (-0.62, GREEN, r"$\gamma$", 5.55)):
        ax.plot([-1.55, stop], [y, y], color=col, lw=2.6)
        arrow(ax, stop - 0.45, y, stop - 0.02, y, color=col, lw=2.4, ms=15)
        ax.text(-1.70, y, name, fontsize=14, color=col, ha="right", va="center")
        if stop < 5.0:
            ax.text(stop + 0.34, y, "bị chặn", fontsize=8.8, color=col, ha="left", va="center")
    ax.text(5.70, -0.62, "xuyên qua", fontsize=8.8, color=GREEN, ha="left", va="center")
    ax.text(2.1, 1.62, "Khả năng đâm xuyên tăng dần:  α  <  β  <  γ",
            fontsize=11.5, color="#34495e", ha="center", fontweight="bold")
    ax.text(2.1, -2.05, "Ngược lại, khả năng ION HOÁ môi trường giảm dần:  α  >  β  >  γ",
            fontsize=9.8, color=GREY, ha="center", style="italic")
    clean(ax, -2.6, 7.0, -2.5, 2.0, eq=False)
    save(fig, "h_sd_dam_xuyen")
    return _reg("h_sd_dam_xuyen")


# ------------------------------------------------------------------ 5. đồ thị phân rã
def h_dt_phanra():
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    t = np.linspace(0, 4.3, 400)
    N = 100 * 2.0 ** (-t)
    ax.plot(t, N, color=RED, lw=2.4)
    for k in range(1, 5):
        y = 100 / 2 ** k
        ax.plot([k, k], [0, y], ls="--", lw=1.0, color=LGREY)
        ax.plot([0, k], [y, y], ls="--", lw=1.0, color=LGREY)
        ax.plot([k], [y], "o", ms=6.5, mfc="white", mec=RED, mew=1.8, zorder=5)
    frame(ax, (0, 4.5), (0, 108), "t (theo chu kì bán rã T)", "N (% số hạt ban đầu)",
          xticks=[0, 1, 2, 3, 4], xticklabels=["0", "T", "2T", "3T", "4T"],
          yticks=[0, 6.25, 12.5, 25, 50, 100],
          yticklabels=["0", "6,25", "12,5", "25", "50", "100"])
    ax.text(2.35, 72, r"$N = N_0\,2^{-t/T} = N_0 e^{-\lambda t}$", fontsize=12.5,
            color=GREEN, ha="center")
    ax.text(2.35, 56, r"$\lambda = \dfrac{\ln 2}{T}$", fontsize=12, color=GREEN, ha="center")
    ax.text(2.35, 33, "Sau mỗi chu kì bán rã, số hạt nhân\nchưa phân rã giảm đi MỘT NỬA.",
            fontsize=9.6, color=GREY, ha="center", va="top")
    save(fig, "h_dt_phanra")
    return _reg("h_dt_phanra")


# ------------------------------------------------------------------ 6. quy tắc dịch chuyển
def h_sd_dich_chuyen():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    rows = [(r"$\alpha$", RED, r"${}^{A}_{Z}X \rightarrow {}^{4}_{2}He + {}^{A-4}_{Z-2}Y$",
             "Z giảm 2, A giảm 4", r"${}^{226}_{\;88}Ra \rightarrow {}^{4}_{2}He + {}^{222}_{\;86}Rn$"),
            (r"$\beta^-$", BLUE, r"${}^{A}_{Z}X \rightarrow {}^{\;\;0}_{-1}e + {}^{A}_{Z+1}Y$",
             "Z tăng 1, A không đổi", r"${}^{14}_{\;6}C \rightarrow {}^{\;\;0}_{-1}e + {}^{14}_{\;7}N$"),
            (r"$\beta^+$", PURPLE, r"${}^{A}_{Z}X \rightarrow {}^{0}_{1}e + {}^{A}_{Z-1}Y$",
             "Z giảm 1, A không đổi", r"${}^{11}_{\;6}C \rightarrow {}^{0}_{1}e + {}^{11}_{\;5}B$"),
            (r"$\gamma$", GREEN, r"$X^* \rightarrow X + \gamma$",
             "Z và A đều không đổi", "chỉ giải phóng năng lượng dư")]
    for i, (tia, col, pt, mo, vd) in enumerate(rows):
        y = 1.35 - 0.92 * i
        ax.add_patch(Rectangle((-3.3, y - 0.37), 7.1, 0.76, fc="#fbfbfb", ec=LGREY, lw=1.0))
        ax.add_patch(Rectangle((-3.3, y - 0.37), 0.06, 0.76, fc=col, ec="none"))
        ax.text(-3.05, y, tia, fontsize=15, color=col, ha="left", va="center")
        ax.text(-2.45, y + 0.13, pt, fontsize=11, color="#34495e", ha="left", va="center")
        ax.text(-2.45, y - 0.20, mo, fontsize=8.8, color=GREY, ha="left", va="center")
        ax.text(1.35, y, vd, fontsize=10, color=col, ha="left", va="center")
    ax.text(0.25, 2.15, "QUY TẮC DỊCH CHUYỂN — bảo toàn số khối A và bảo toàn điện tích Z",
            fontsize=10.5, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.5, 4.0, -2.3, 2.5, eq=False)
    save(fig, "h_sd_dich_chuyen")
    return _reg("h_sd_dich_chuyen")


# ------------------------------------------------------------------ 7. phản ứng dây chuyền
def h_sd_phan_hach():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    def U(x, y, r=0.30, lab="U"):
        ax.add_patch(Circle((x, y), r, fc="#d6eaf8", ec="#2874a6", lw=1.4, zorder=3))
        ax.text(x, y, lab, fontsize=9.5, color="#1b4f72", ha="center", va="center", zorder=4)

    def n(x, y, r=0.09):
        ax.add_patch(Circle((x, y), r, fc=NEUT, ec="#2c3e50", lw=0.7, zorder=5))

    n(-3.0, 0)
    arrow(ax, -2.85, 0, -2.35, 0, color=GREY, lw=1.3, ms=11)
    ax.text(-3.0, 0.30, "nơtron\nchậm", fontsize=8.6, color=GREY, ha="center", va="bottom")
    U(-1.95, 0)
    arrow(ax, -1.55, 0, -1.05, 0, color=ORANGE, lw=1.6, ms=12)
    ax.text(-1.30, 0.20, "vỡ", fontsize=8.8, color=ORANGE, ha="center")
    for dy, lab in ((0.52, "Y"), (-0.52, "I")):
        ax.add_patch(Circle((-0.55, dy), 0.21, fc="#fadbd8", ec="#c0392b", lw=1.2, zorder=3))
        ax.text(-0.55, dy, lab, fontsize=9, color="#7b241c", ha="center", va="center", zorder=4)
    for k, dy in enumerate((0.30, 0.0, -0.30)):
        n(-0.05, dy)
        arrow(ax, 0.05, dy, 0.62, dy * 2.4, color=GREY, lw=1.1, ms=10)
    for k, dy in enumerate((0.95, 0.0, -0.95)):
        U(1.05, dy, r=0.26)
        for s in (0.28, 0, -0.28):
            n(1.42, dy + s * 0.9)
            arrow(ax, 1.52, dy + s * 0.9, 2.05, dy + s * 1.6, color=GREY, lw=0.9, ms=8)
    for dy in (1.45, 0.75, 0.25, -0.25, -0.75, -1.45):
        U(2.45, dy, r=0.20)
    ax.text(3.25, 0, "…", fontsize=20, color=GREY, ha="center", va="center")
    ax.text(-0.2, 1.95, "PHẢN ỨNG DÂY CHUYỀN: mỗi phân hạch giải phóng 2–3 nơtron mới",
            fontsize=10, color="#34495e", ha="center", fontweight="bold")
    ax.text(-0.2, -1.95,
            "Hệ số nhân nơtron k < 1: phản ứng tắt  •  k = 1: duy trì ổn định (lò phản ứng)  •  "
            "k > 1: bùng nổ (bom)",
            fontsize=9.2, color=GREY, ha="center")
    ax.text(-0.2, -2.35, "Mỗi phân hạch ²³⁵U toả khoảng 200 MeV", fontsize=9.6,
            color=GREEN, ha="center")
    clean(ax, -3.4, 3.8, -2.7, 2.3, eq=False)
    save(fig, "h_sd_phan_hach")
    return _reg("h_sd_phan_hach")


# ------------------------------------------------------------------ 8. lò phản ứng
def h_sd_lo_phan_ung():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ax.add_patch(Rectangle((-3.2, -1.1), 2.3, 2.3, fc="#eaeded", ec="#566573", lw=1.8))
    for x in np.linspace(-2.95, -1.55, 6):
        ax.add_patch(Rectangle((x, -0.95), 0.13, 1.7, fc="#d6eaf8", ec="#2874a6", lw=1.0))
    for x in np.linspace(-2.80, -1.40, 5):
        ax.add_patch(Rectangle((x, 0.15), 0.10, 1.35, fc="#34495e", ec="#1c2833", lw=1.0))
    ax.text(-2.05, 1.62, "thanh điều khiển\n(hấp thụ nơtron)", fontsize=8.6, color="#34495e",
            ha="center", va="bottom")
    ax.text(-2.05, -1.30, "nhiên liệu urani\ntrong chất làm chậm", fontsize=8.6,
            color="#1b4f72", ha="center", va="top")
    arrow(ax, -0.9, 0.55, -0.15, 0.55, color=RED, lw=2.0, ms=14)
    arrow(ax, -0.15, -0.45, -0.9, -0.45, color=BLUE, lw=2.0, ms=14)
    ax.text(-0.52, 0.75, "chất tải nhiệt nóng", fontsize=8.6, color=RED, ha="center")
    ax.text(-0.52, -0.70, "chất tải nhiệt nguội", fontsize=8.6, color=BLUE, ha="center")
    ax.add_patch(Rectangle((-0.1, -1.1), 1.35, 2.3, fc="#fdf2e9", ec="#ca6f1e", lw=1.6))
    ax.text(0.57, 0.05, "lò sinh\nhơi", fontsize=9.4, color="#ca6f1e", ha="center", va="center")
    ax.text(0.57, -1.30, "nước → hơi nước", fontsize=8.6, color=GREY, ha="center", va="top")
    ax.add_patch(Circle((2.15, 0.35), 0.45, fc="#d5f5e3", ec="#1e8449", lw=1.6))
    ax.text(2.15, 0.35, "tua bin", fontsize=8.6, color="#145a32", ha="center", va="center")
    arrow(ax, 1.25, 0.55, 1.62, 0.45, color=RED, lw=1.6, ms=12)
    ax.add_patch(Circle((3.15, 0.35), 0.40, fc="#fcf3cf", ec="#b7950b", lw=1.6))
    ax.text(3.15, 0.35, "máy\nphát", fontsize=8.4, color="#7d6608", ha="center", va="center")
    arrow(ax, 2.62, 0.35, 2.72, 0.35, color="#7d6608", lw=1.6, ms=12)
    ax.text(3.15, -0.35, "điện năng", fontsize=9.2, color="#7d6608", ha="center", va="top")
    ax.text(0.0, 2.60, "Nhiệt từ phân hạch → hơi nước → tua bin → máy phát điện",
            fontsize=10.5, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.4, 3.9, -2.0, 2.9, eq=False)
    save(fig, "h_sd_lo_phan_ung")
    return _reg("h_sd_lo_phan_ung")


# ------------------------------------------------------------------ 9. nhiệt hạch
def h_sd_nhiet_hach():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    _nucleus(ax, -2.75, 0.60, 1, 1, r=0.17, spread=0.20, seed=2)
    ax.text(-2.75, -0.05, r"${}^{2}_{1}H$  đơteri", fontsize=10.5, ha="center", va="top",
            color="#34495e")
    _nucleus(ax, -2.75, -0.95, 1, 2, r=0.17, spread=0.24, seed=9)
    ax.text(-2.75, -1.60, r"${}^{3}_{1}H$  triti", fontsize=10.5, ha="center", va="top",
            color="#34495e")
    arrow(ax, -2.00, -0.18, -1.10, -0.18, color=ORANGE, lw=2.2, ms=16)
    ax.text(-1.55, 0.08, "nhiệt độ\n~10⁸ K", fontsize=8.8, color=ORANGE, ha="center", va="bottom")
    _nucleus(ax, -0.35, 0.20, 2, 2, r=0.17, spread=0.30, seed=5)
    ax.text(-0.35, -0.45, r"${}^{4}_{2}He$", fontsize=11.5, ha="center", va="top", color="#34495e")
    ax.add_patch(Circle((-0.35, -1.25), 0.14, fc=NEUT, ec="#2c3e50", lw=0.8))
    ax.text(-0.35, -1.55, "nơtron", fontsize=9.0, ha="center", va="top", color=GREY)
    arrow(ax, 0.35, -0.18, 1.05, -0.18, color=GREEN, lw=2.0, ms=14)
    ax.text(2.55, 0.30, "toả 17,6 MeV", fontsize=13, color=GREEN, ha="center", va="center")
    ax.text(2.55, -0.45, "Tính trên MỘT nuclêôn, nhiệt hạch toả\n"
                         "năng lượng nhiều hơn cả phân hạch.\n"
                         "Đây là nguồn năng lượng của Mặt Trời.",
            fontsize=9.2, color=GREY, ha="center", va="top")
    ax.text(-0.2, 1.88, "PHẢN ỨNG NHIỆT HẠCH: hai hạt nhân RẤT NHẸ kết hợp thành hạt nhân nặng hơn",
            fontsize=10.2, color="#34495e", ha="center", fontweight="bold")
    ax.text(-0.2, 1.48, "Điều kiện: nhiệt độ cực cao để thắng lực đẩy Cu-lông giữa hai hạt nhân",
            fontsize=9.2, color=GREY, ha="center")
    clean(ax, -3.6, 4.5, -2.3, 2.2, eq=False)
    save(fig, "h_sd_nhiet_hach")
    return _reg("h_sd_nhiet_hach")


# ------------------------------------------------------------------ 10. ứng dụng phóng xạ
def h_sd_ung_dung():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    cards = [("Y HỌC", "#c0392b",
              "• Xạ trị bằng tia γ từ ⁶⁰Co\n   diệt tế bào ung thư\n"
              "• Chụp PET dùng đồng vị\n   phát β⁺ (¹⁸F)\n• Tiệt trùng dụng cụ y tế"),
             ("CÔNG NGHIỆP", "#1f4e9c",
              "• Đo bề dày tấm kim loại\n   bằng độ hấp thụ tia β\n"
              "• Kiểm tra mối hàn, vết nứt\n   bằng tia γ\n• Dò rò rỉ đường ống ngầm"),
             ("KHẢO CỔ – NÔNG NGHIỆP", "#1e8449",
              "• Xác định tuổi mẫu vật\n   bằng ¹⁴C (T = 5730 năm)\n"
              "• Tạo đột biến giống cây trồng\n• Bảo quản nông sản\n   bằng chiếu xạ")]
    for i2, (ten, col, noi) in enumerate(cards):
        x = -3.65 + i2 * 2.48
        ax.add_patch(Rectangle((x, -1.25), 2.30, 2.45, fc="#fcfcfc", ec=col, lw=1.4))
        ax.add_patch(Rectangle((x, 0.86), 2.30, 0.34, fc=col, ec=col, lw=1.4))
        ax.text(x + 1.15, 1.03, ten, fontsize=7.8 if len(ten) > 14 else 9.4, color="white",
                ha="center", va="center", fontweight="bold")
        ax.text(x + 0.10, 0.70, noi, fontsize=8.4, color="#34495e", ha="left", va="top",
                linespacing=1.45)
    ax.text(-0.35, 1.72, "ỨNG DỤNG CỦA ĐỒNG VỊ PHÓNG XẠ", fontsize=11.5, color="#34495e",
            ha="center", fontweight="bold")
    ax.text(-0.35, -1.50, "Nguyên tắc chung: chọn đồng vị có chu kì bán rã và loại tia phù hợp "
                          "với mục đích sử dụng",
            fontsize=9.2, color=GREY, ha="center", va="top", style="italic")
    clean(ax, -3.85, 3.80, -2.0, 2.0, eq=False)
    save(fig, "h_sd_ung_dung")
    return _reg("h_sd_ung_dung")


# ------------------------------------------------------------------ 11. an toàn phóng xạ
def h_sd_an_toan():
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    ax.add_patch(Circle((-3.05, 0.10), 0.50, fc="#f9e79f", ec="#b7950b", lw=1.6))
    for a in (90, 210, 330):
        ax.add_patch(Wedge((-3.05, 0.10), 0.42, a - 22, a + 22, fc="#7d6608", ec="none"))
    ax.add_patch(Circle((-3.05, 0.10), 0.10, fc="#7d6608", ec="none"))
    ax.text(-3.05, -0.62, "biển cảnh báo\nbức xạ ion hoá", fontsize=8.8, color="#7d6608",
            ha="center", va="top")
    items = [("THỜI GIAN", "Rút ngắn thời gian\ntiếp xúc với nguồn."),
             ("KHOẢNG CÁCH", "Đứng xa nguồn.\nLiều chiếu giảm nhanh\nkhi khoảng cách tăng."),
             ("CHE CHẮN", "Dùng vật liệu chắn\nphù hợp: giấy – nhôm\n– chì / bê tông.")]
    for i2, (ten, noi) in enumerate(items):
        x = -2.20 + i2 * 2.02
        ax.add_patch(Rectangle((x, -1.00), 1.90, 2.05, fc="#eaf2f8", ec="#2874a6", lw=1.3))
        ax.text(x + 0.95, 0.80, ten, fontsize=9.4, color="#1b4f72", ha="center",
                va="center", fontweight="bold")
        ax.text(x + 0.95, 0.46, noi, fontsize=7.9, color="#34495e", ha="center", va="top",
                linespacing=1.5)
    ax.text(-0.35, 1.52, "BA NGUYÊN TẮC AN TOÀN BỨC XẠ", fontsize=11.5, color="#34495e",
            ha="center", fontweight="bold")
    ax.text(-0.35, -1.28, "Đơn vị đo liều hấp thụ: gray (Gy);  liều tương đương: sivơ (Sv)",
            fontsize=9.2, color=GREY, ha="center", va="top")
    clean(ax, -3.7, 4.0, -1.85, 1.85, eq=False)
    save(fig, "h_sd_an_toan")
    return _reg("h_sd_an_toan")


# ------------------------------------------------------------------ 12. xác định tuổi bằng C-14
def h_dt_c14():
    fig, ax = plt.subplots(figsize=(6.4, 3.7))
    t = np.linspace(0, 25000, 500)
    N = 100 * 0.5 ** (t / 5730.0)
    ax.plot(t, N, color=BROWN, lw=2.4)
    ax.plot([0, 11460], [25, 25], ls="--", lw=1.2, color=RED)
    ax.plot([11460, 11460], [0, 25], ls="--", lw=1.2, color=RED)
    ax.plot([11460], [25], "o", ms=7, mfc="white", mec=RED, mew=2, zorder=5)
    ax.text(12200, 30, "mẫu gỗ còn 25 %  ⇒  tuổi ≈ 11 460 năm\n(đúng 2 chu kì bán rã)",
            fontsize=9.6, color=RED, ha="left", va="bottom")
    frame(ax, (0, 25500), (0, 108), "tuổi mẫu vật (năm)", "tỉ lệ ¹⁴C còn lại (%)",
          xticks=[0, 5730, 11460, 17190, 22920],
          xticklabels=["0", "5730", "11460", "17190", "22920"],
          yticks=[0, 12.5, 25, 50, 100], yticklabels=["0", "12,5", "25", "50", "100"])
    ax.text(13500, 78, "Chu kì bán rã của ¹⁴C:  T = 5730 năm", fontsize=10, color=GREEN,
            ha="center")
    ax.text(13500, 64, r"$t = T\,\dfrac{\ln(N_0/N)}{\ln 2}$", fontsize=12, color=GREEN,
            ha="center")
    save(fig, "h_dt_c14")
    return _reg("h_dt_c14")


ALL = [h_sd_cautruc, h_sd_dohutkhoi, h_sd_tia_phongxa, h_sd_dam_xuyen, h_dt_phanra,
       h_sd_dich_chuyen, h_sd_phan_hach, h_sd_lo_phan_ung, h_sd_nhiet_hach,
       h_sd_ung_dung, h_sd_an_toan, h_dt_c14]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
