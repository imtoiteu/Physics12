# -*- coding: utf-8 -*-
"""Hình vẽ gốc cho BỘ 1 – Chương I (Vật lí nhiệt) và Chương II (Khí lí tưởng)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyBboxPatch, Ellipse, Arc

from figbase import (save, arrow, clean, frame, guide, dot, hatch_ground,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)

MADE = []


def _reg(name):
    MADE.append(name)
    return name


# ---------------------------------------------------------------- 1. đồ thị đun nóng
def b1_do_thi_dun_nong():
    """Đường cong nung nóng: rắn → nóng chảy → lỏng, công suất không đổi."""
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    t = [0, 120, 420, 520]
    T = [-40, 60, 60, 110]
    ax.plot(t, T, color=RED, lw=2.4, solid_joinstyle="round", zorder=4)
    for x, y in zip(t, T):
        ax.plot([x], [y], "o", ms=5, color=RED, zorder=5)
    for x, y in [(120, 60), (420, 60), (520, 110)]:
        ax.plot([x, x], [-60, y], ls="--", lw=0.9, color=LGREY, zorder=0)
    for y in (-40, 60, 110):
        ax.plot([0, 520], [y, y], ls="--", lw=0.9, color=LGREY, zorder=0)

    ax.annotate("", xy=(120, 88), xytext=(0, 88),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.3))
    ax.text(60, 91, "giai đoạn 1", color=BLUE, fontsize=9.5, ha="center")
    ax.annotate("", xy=(420, 30), xytext=(120, 30),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(270, 33, "giai đoạn 2", color=GREEN, fontsize=9.5, ha="center")
    ax.annotate("", xy=(520, 93), xytext=(420, 93),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.3))
    ax.text(470, 96, "gđ 3", color=ORANGE, fontsize=9.5, ha="center")

    frame(ax, (0, 560), (-60, 130), "t (s)", "T (°C)",
          xticks=[0, 120, 420, 520], yticks=[-40, 0, 60, 110])
    save(fig, "b1_do_thi_dun_nong")
    return _reg("b1_do_thi_dun_nong")


# ---------------------------------------------------------------- 2. chu trình p-V
def b1_chu_trinh_pV():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    V = [2, 2, 5, 5, 2]
    p = [1, 3, 3, 1, 1]
    ax.plot(V, p, color=BLUE, lw=2.2, zorder=3)
    ax.fill(V, p, color=BLUE, alpha=0.07, zorder=1)
    for (x, y, lab, dx, dy) in [(2, 1, "(1)", -0.42, -0.28), (2, 3, "(2)", -0.42, 0.12),
                                (5, 3, "(3)", 0.12, 0.12), (5, 1, "(4)", 0.12, -0.28)]:
        ax.plot([x], [y], "o", ms=6, color=RED, zorder=5)
        ax.text(x + dx, y + dy, lab, fontsize=11, color=RED, fontweight="bold")
    for (x, y, ddx, ddy) in [(2, 2, 0, 0.1), (3.5, 3, 0.1, 0), (5, 2, 0, -0.1), (3.5, 1, -0.1, 0)]:
        ax.annotate("", xy=(x + ddx * 3, y + ddy * 3), xytext=(x, y),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.6, mutation_scale=14))
    frame(ax, (0, 6.4), (0, 4.0), "V (L)", "p (10⁵ Pa)",
          xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[0, 1, 2, 3, 4])
    save(fig, "b1_chu_trinh_pV")
    return _reg("b1_chu_trinh_pV")


# ---------------------------------------------------------------- 3. ống thuỷ ngân
def _tube(ax, x0, y0, ang, L, hg_from, hg_len, air_len, w=1.0, side=1):
    """Vẽ một ống nghiêng góc ang (độ) so với phương ngang, gốc đặt ở đầu kín.

    side = +1/−1 quy định phía đặt các nhãn chú thích."""
    a = np.radians(ang)
    ux, uy = np.cos(a), np.sin(a)
    px, py = -uy, ux

    def pt(s, off):
        return (x0 + ux * s + px * off, y0 + uy * s + py * off)

    poly = [pt(0, -w / 2), pt(air_len, -w / 2), pt(air_len, w / 2), pt(0, w / 2)]
    ax.add_patch(Polygon(poly, closed=True, fc="#dbe9f8", ec="none", zorder=1))
    poly = [pt(hg_from, -w / 2), pt(hg_from + hg_len, -w / 2),
            pt(hg_from + hg_len, w / 2), pt(hg_from, w / 2)]
    ax.add_patch(Polygon(poly, closed=True, fc="#8e9aa6", ec="#5a6470", lw=0.8, zorder=2))
    for off in (-w / 2, w / 2):
        ax.plot([pt(0, off)[0], pt(L, off)[0]], [pt(0, off)[1], pt(L, off)[1]],
                color="#444444", lw=1.8, zorder=3)
    ax.plot([pt(0, -w / 2)[0], pt(0, w / 2)[0]], [pt(0, -w / 2)[1], pt(0, w / 2)[1]],
            color="#444444", lw=3.0, zorder=3)

    off = side * (w / 2 + 0.55)
    q = pt(air_len / 2, off)
    ax.text(q[0], q[1], "cột khí", fontsize=8.6, color=BLUE, ha="center", va="center",
            rotation=ang if abs(ang) < 1 else 0, zorder=4)
    q = pt(hg_from + hg_len / 2, off)
    ax.text(q[0], q[1], "Hg", fontsize=8.6, color="#3d4650", ha="center", va="center",
            zorder=4)
    tip = pt(L + 0.55, 0)
    ax.text(tip[0], tip[1], "hở", fontsize=8.4, color=GREY, ha="center", va="center")
    base = pt(-0.6, 0)
    ax.text(base[0], base[1], "kín", fontsize=8.4, color=GREY, ha="center", va="center")


def b1_ong_thuy_ngan():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    clean(ax, -1.0, 23.0, -2.6, 9.2)
    # (a) thẳng đứng, miệng ở trên: khí 4,0 ; Hg 1,0 ; ống 6,0
    _tube(ax, 1.6, 0.8, 90, 6.0, 4.0, 1.0, 4.0, side=-1)
    ax.text(1.6, -1.6, "(a) miệng hướng lên", fontsize=9.4, color=RED,
            ha="center", fontweight="bold")
    # (b) nằm ngang
    _tube(ax, 6.0, 4.2, 0, 6.0, 4.53, 1.0, 4.53, side=1)
    ax.text(9.0, -1.6, "(b) nằm ngang", fontsize=9.4, color=RED,
            ha="center", fontweight="bold")
    # (c) miệng hướng xuống (trạng thái sau khi một phần Hg đã chảy ra)
    _tube(ax, 19.5, 7.4, -90, 6.0, 5.13, 0.87, 5.13, side=1)
    ax.text(19.5, -1.6, "(c) miệng hướng xuống", fontsize=9.4, color=RED,
            ha="center", fontweight="bold")
    ax.text(21.6, 0.9, "một phần Hg\ncó thể chảy ra", fontsize=8.4, color=RED,
            ha="center", va="center")
    ax.plot([19.5], [0.55], "o", ms=4.5, color="#8e9aa6")
    ax.plot([19.2], [0.05], "o", ms=3.2, color="#8e9aa6")
    save(fig, "b1_ong_thuy_ngan")
    return _reg("b1_ong_thuy_ngan")


# ---------------------------------------------------------------- 4. p-T đẳng tích
def b1_pT_dang_tich():
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    T = np.linspace(0, 500, 50)
    ax.plot(T, 0.0090 * T, color=RED, lw=2.1, label="(1)")
    ax.plot(T, 0.0050 * T, color=BLUE, lw=2.1, label="(2)")
    ax.plot(T, 1.2 + 0.0030 * T, color=GREEN, lw=2.1, ls="--", label="(3)")
    ax.text(430, 4.05, "(1)", color=RED, fontsize=11, fontweight="bold")
    ax.text(455, 2.40, "(2)", color=BLUE, fontsize=11, fontweight="bold")
    ax.text(455, 2.85, "(3)", color=GREEN, fontsize=11, fontweight="bold")
    ax.plot([0], [1.2], "o", ms=5, color=GREEN)
    frame(ax, (0, 520), (0, 4.6), "T (K)", "p (10⁵ Pa)",
          xticks=[0, 100, 200, 300, 400, 500], yticks=[0, 1, 2, 3, 4])
    save(fig, "b1_pT_dang_tich")
    return _reg("b1_pT_dang_tich")


# ---------------------------------------------------------------- 5. thí nghiệm Boyle
def b1_xilanh_boyle():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    clean(ax, 0, 15, -0.6, 5.4)
    # xilanh (kết thúc ngay sau pit-tông để không gợi ra một khoang thừa)
    ax.add_patch(Rectangle((1.2, 1.6), 5.65, 1.8, fc="#d8e8f8", ec=GREY, lw=1.8))
    ax.text(3.8, 2.5, "khí đọc được trên\nthang chia độ:  V", fontsize=9, color=BLUE,
            ha="center", va="center")
    # pit-tông
    ax.add_patch(Rectangle((6.4, 1.5), 0.45, 2.0, fc="#9aa5b1", ec="#5a6470", lw=1.0))
    ax.plot([6.85, 9.6], [2.5, 2.5], color="#5a6470", lw=3.0)
    ax.add_patch(Rectangle((9.6, 1.9), 0.5, 1.2, fc="#5a6470", ec="none"))
    ax.text(6.62, 3.75, "pit-tông", fontsize=8.6, color="#3d4650", ha="center")
    arrow(ax, 10.4, 2.5, 11.9, 2.5, color=RED, lw=1.8)
    ax.text(11.15, 2.9, "lực nén", fontsize=9, color=RED, ha="center")
    # thể tích chết
    ax.add_patch(Rectangle((0.55, 1.85), 0.65, 1.3, fc="#f6dede", ec=RED, lw=1.2))
    ax.annotate("thể tích “chết” V₀\n(đầu xilanh + ống nối)",
                xy=(0.88, 3.15), xytext=(1.6, 4.7), fontsize=9, color=RED, ha="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    # thang chia
    for k in range(11):
        x = 1.2 + k * 0.52
        ax.plot([x, x], [1.6, 1.3], color=GREY, lw=1.0)
    ax.text(4.7, 0.85, "thang chia độ", fontsize=8.5, color=GREY, ha="center")
    # áp kế
    ax.add_patch(Circle((0.88, 4.35), 0.0, fc="none"))
    ax.plot([0.88, 0.88], [1.85, 0.6], color=GREY, lw=1.6)
    ax.add_patch(Circle((0.88, 0.15), 0.42, fc="white", ec=GREY, lw=1.6))
    ax.plot([0.88, 1.10], [0.15, 0.38], color=RED, lw=1.4)
    ax.text(1.5, 0.05, "áp kế: p", fontsize=9, color=GREY, ha="left", va="center")
    save(fig, "b1_xilanh_boyle")
    return _reg("b1_xilanh_boyle")


def b1_V_theo_1p():
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    p = np.array([1.0, 1.2, 1.5, 2.0, 3.0])
    V = np.array([55.0, 45.0, 35.0, 25.0, 15.0])
    x = 1 / p
    xs = np.linspace(-0.06, 1.12, 30)
    ax.plot(xs, 60 * xs - 5, color=BLUE, lw=1.8, zorder=2)
    ax.plot(x, V, "o", ms=7, mfc="white", mec=RED, mew=1.8, zorder=4)
    ax.axhline(0, color=GREY, lw=1.0)
    ax.plot([0], [-5], "s", ms=7, color=GREEN, zorder=5)
    ax.annotate("giao với trục V tại −V₀", xy=(0, -5), xytext=(0.30, -14),
                fontsize=9.5, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    frame(ax, (-0.10, 1.18), (-22, 68), "1/p (10⁻⁵ Pa⁻¹)", "V (cm³)",
          xticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0], yticks=[-20, 0, 20, 40, 60])
    save(fig, "b1_V_theo_1p")
    return _reg("b1_V_theo_1p")


# ---------------------------------------------------------------- 6. xilanh có vấu chặn
def b1_xilanh_chan():
    fig, ax = plt.subplots(figsize=(3.6, 4.8))
    clean(ax, -1.6, 4.6, -0.6, 9.4)
    ax.add_patch(Rectangle((0, 0), 3.0, 8.2, fc="white", ec=GREY, lw=2.0))
    ax.add_patch(Rectangle((0, 0), 3.0, 4.0, fc="#d8e8f8", ec="none"))
    ax.text(1.5, 2.0, "khí", fontsize=11, color=BLUE, ha="center", va="center")
    # pit-tông
    ax.add_patch(Rectangle((0, 4.0), 3.0, 0.55, fc="#9aa5b1", ec="#5a6470", lw=1.2))
    ax.text(3.35, 4.28, "pit-tông", fontsize=9, color="#3d4650", ha="left", va="center")
    # vấu chặn
    for xx, dx in ((0, 0.55), (3.0, -0.55)):
        ax.add_patch(Rectangle((min(xx, xx + dx), 5.55), abs(dx), 0.3,
                               fc=RED, ec=RED))
    ax.text(1.5, 6.15, "vấu chặn", fontsize=9, color=RED, ha="center")
    ax.annotate("", xy=(3.7, 5.55), xytext=(3.7, 4.55),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(3.85, 5.05, "5 cm", fontsize=9, color=GREEN, ha="left", va="center")
    ax.annotate("", xy=(-0.55, 4.0), xytext=(-0.55, 0),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.3))
    ax.text(-0.75, 2.0, "20 cm", fontsize=9, color=BLUE, ha="right", va="center",
            rotation=90)
    # nguồn nhiệt
    for k in range(5):
        x = 0.35 + k * 0.58
        ax.plot([x, x + 0.12, x - 0.05, x + 0.08], [-0.55, -0.35, -0.18, 0.0],
                color=ORANGE, lw=1.4)
    ax.text(1.5, 8.8, "đun nóng chậm", fontsize=9.5, color=ORANGE, ha="center")
    save(fig, "b1_xilanh_chan")
    return _reg("b1_xilanh_chan")


# ---------------------------------------------------------------- 7. V - t (°C)
def b1_VT_hai_duong():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    f1 = lambda t: 0.02 * (t + 273)
    f2 = lambda t: 1.8 + 0.011 * (t + 273)
    td = np.linspace(-273, -20, 30)        # phần ngoại suy
    ts = np.linspace(-20, 160, 30)         # phần đo được
    for f, c, lab, ly in ((f1, RED, "(1)", 9.0), (f2, BLUE, "(2)", 6.6)):
        ax.plot(td, f(td), color=c, lw=1.6, ls="--")
        ax.plot(ts, f(ts), color=c, lw=2.3)
        ax.text(140, ly, lab, color=c, fontsize=11, fontweight="bold")
    ax.plot([-273, -273], [0, 9.4], ls=":", lw=1.1, color=GREY)
    ax.plot([-273], [0], "o", ms=7, color=RED, zorder=5)
    ax.plot([-273], [1.8], "s", ms=7, color=BLUE, zorder=5)
    ax.annotate("kéo dài đường (1)\nvề đúng V = 0", xy=(-273, 0), xytext=(-158, 0.85),
                fontsize=9, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    ax.annotate("kéo dài đường (2)\nvẫn cho V ≠ 0", xy=(-273, 1.8), xytext=(-215, 4.6),
                fontsize=9, color=BLUE,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
    ax.text(30, 0.55, "nét liền: khoảng đã đo   •   nét đứt: phần ngoại suy",
            fontsize=8.6, color=GREY, ha="center")
    ax.axhline(0, color=GREY, lw=1.0)
    frame(ax, (-300, 175), (-0.6, 10.0), "t (°C)", "V (L)",
          xticks=[-273, -200, -100, 0, 100], yticks=[0, 2, 4, 6, 8, 10],
          xticklabels=["−273", "−200", "−100", "0", "100"])
    save(fig, "b1_VT_hai_duong")
    return _reg("b1_VT_hai_duong")


# ---------------------------------------------------------------- 8. khinh khí cầu
def b1_khinh_khi_cau():
    fig, ax = plt.subplots(figsize=(4.2, 5.0))
    clean(ax, -3.4, 3.4, -1.2, 8.6)
    ax.add_patch(Ellipse((0, 5.1), 4.4, 5.0, fc="#fdece0", ec=ORANGE, lw=2.0))
    ax.plot([-1.0, -0.55], [2.85, 1.5], color=GREY, lw=1.2)
    ax.plot([1.0, 0.55], [2.85, 1.5], color=GREY, lw=1.2)
    ax.add_patch(Rectangle((-0.62, 0.75), 1.24, 0.8, fc="#e8d5b7", ec=BROWN, lw=1.4))
    ax.text(0, 5.6, "không khí nóng\ntrong cầu\n(V = 1000 m³)", fontsize=9, color=RED,
            ha="center", va="center")
    # miệng hở
    ax.plot([-0.45, 0.45], [2.62, 2.62], color=RED, lw=2.2)
    ax.text(0.75, 2.45, "miệng hở", fontsize=8.5, color=RED, ha="left")
    for k in range(3):
        ax.plot([-0.22 + k * 0.22, -0.30 + k * 0.22], [2.05, 2.45], color=ORANGE, lw=1.3)
    arrow(ax, 2.6, 3.4, 2.6, 5.6, color=GREEN, lw=2.0)
    ax.text(2.75, 4.5, "$F_A$", fontsize=13, color=GREEN, ha="left", va="center")
    arrow(ax, -2.6, 3.4, -2.6, 1.4, color=BLUE, lw=2.0)
    ax.text(-2.75, 2.4, "$P$", fontsize=13, color=BLUE, ha="right", va="center")
    ax.text(0, -0.85, "không khí ngoài: 27 °C;  p = 10⁵ Pa", fontsize=9, color=GREY,
            ha="center")
    save(fig, "b1_khinh_khi_cau")
    return _reg("b1_khinh_khi_cau")


# ---------------------------------------------------------------- 9. giãn vào chân không
def b1_binh_chan_khong():
    fig, ax = plt.subplots(figsize=(6.6, 2.9))
    clean(ax, -0.4, 15.0, -1.5, 4.4)
    for x0, lab in ((0.4, "TRƯỚC"), (8.2, "SAU")):
        ax.add_patch(Rectangle((x0, 0), 6.0, 3.2, fc="white", ec="#333333", lw=2.6))
        ax.text(x0 + 3.0, -1.05, lab, fontsize=10, color="#333333", ha="center",
                fontweight="bold")
    # trước: ngăn A có khí, ngăn B chân không, có vách
    ax.add_patch(Rectangle((0.4, 0), 3.0, 3.2, fc="#d8e8f8", ec="none"))
    ax.plot([3.4, 3.4], [0, 3.2], color=RED, lw=2.4)
    rng = np.random.default_rng(7)
    xs = rng.uniform(0.7, 3.1, 26); ys = rng.uniform(0.25, 2.95, 26)
    ax.plot(xs, ys, "o", ms=3.0, color=BLUE)
    ax.text(1.9, 3.55, "A: khí lí tưởng", fontsize=9.5, color=BLUE, ha="center")
    ax.text(5.0, 3.55, "B: chân không", fontsize=9.5, color=GREY, ha="center")
    ax.text(3.4, -0.42, "vách ngăn", fontsize=8.5, color=RED, ha="center")
    ax.text(0.55, 2.95, "bình cách nhiệt", fontsize=8.2, color="#333333", ha="left",
            va="top")
    # sau
    ax.add_patch(Rectangle((8.2, 0), 6.0, 3.2, fc="#e7f0f9", ec="none"))
    xs = rng.uniform(8.5, 13.9, 26); ys = rng.uniform(0.25, 2.95, 26)
    ax.plot(xs, ys, "o", ms=3.0, color=BLUE)
    ax.plot([11.2, 11.2], [0, 0.8], color=RED, lw=2.4)
    ax.plot([11.2, 11.2], [2.4, 3.2], color=RED, lw=2.4)
    ax.text(11.2, 1.6, "vách bị\nchọc thủng", fontsize=8.2, color=RED, ha="center",
            va="center")
    arrow(ax, 6.7, 1.6, 7.9, 1.6, color="#333333", lw=1.6)
    save(fig, "b1_binh_chan_khong")
    return _reg("b1_binh_chan_khong")


# ---------------------------------------------------------------- 10. Q theo ΔT
def b1_Q_deltaT():
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    dT = np.linspace(0, 50, 20)
    ax.plot(dT, 2.0 * dT, color=RED, lw=2.1)
    ax.plot(dT, 1.6 * dT, color=BLUE, lw=2.1)
    ax.text(44, 92, "(1)", color=RED, fontsize=11, fontweight="bold")
    ax.text(46, 68, "(2)", color=BLUE, fontsize=11, fontweight="bold")
    frame(ax, (0, 54), (0, 108), "ΔT (K)", "Q (kJ)",
          xticks=[0, 10, 20, 30, 40, 50], yticks=[0, 20, 40, 60, 80, 100])
    save(fig, "b1_Q_deltaT")
    return _reg("b1_Q_deltaT")


# ---------------------------------------------------------------- 11. p-V đường thẳng
def b1_pV_duong_thang():
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    V = np.linspace(1, 4, 40)
    p = 5 - V
    ax.plot(V, p, color=BLUE, lw=2.3, zorder=3)
    ax.plot([1], [4], "o", ms=7, color=RED, zorder=5)
    ax.plot([4], [1], "o", ms=7, color=RED, zorder=5)
    ax.text(1.05, 4.18, "A", fontsize=12, color=RED, fontweight="bold")
    ax.text(4.05, 1.18, "B", fontsize=12, color=RED, fontweight="bold")
    Vh = np.linspace(1.0, 4.4, 80)
    ax.plot(Vh, 4.0 / Vh, color=LGREY, lw=1.4, ls="--", zorder=1)
    ax.text(3.4, 1.42, "đẳng nhiệt qua A", fontsize=8.6, color=GREY, rotation=-16)
    arrow(ax, 2.0, 3.0, 2.6, 2.4, color=BLUE, lw=1.4, ms=13)
    frame(ax, (0, 5.2), (0, 5.0), "V (L)", "p (10⁵ Pa)",
          xticks=[0, 1, 2, 3, 4, 5], yticks=[0, 1, 2, 3, 4, 5])
    save(fig, "b1_pV_duong_thang")
    return _reg("b1_pV_duong_thang")


# ---------------------------------------------------------------- 12. đường nguội lạnh
def b1_do_thi_nguoi_lanh():
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    t = np.linspace(0, 60, 200)
    # T = 20 + 60 exp(-t/tau); tốc độ ban đầu 60/tau
    TA = 20 + 60 * np.exp(-t / 120.0)     # ban đầu 0,50 K/min
    TB = 20 + 60 * np.exp(-t / 300.0)     # ban đầu 0,20 K/min
    ax.plot(t, TA, color=RED, lw=2.1)
    ax.plot(t, TB, color=BLUE, lw=2.1)
    ax.plot([0, 14], [80, 73], ls="--", lw=1.2, color=RED)
    ax.plot([0, 14], [80, 77.2], ls="--", lw=1.2, color=BLUE)
    ax.text(16, 71.5, "hệ số góc ban đầu −0,50 K/min", fontsize=8.8, color=RED)
    ax.text(16, 77.6, "hệ số góc ban đầu −0,20 K/min", fontsize=8.8, color=BLUE)
    ax.text(52, 42, "chất lỏng A", color=RED, fontsize=10, fontweight="bold")
    ax.text(52, 56, "chất lỏng B", color=BLUE, fontsize=10, fontweight="bold")
    ax.axhline(20, color=GREEN, lw=1.2, ls=":")
    ax.text(1, 21.5, "nhiệt độ phòng 20 °C", fontsize=8.8, color=GREEN)
    frame(ax, (0, 62), (10, 88), "t (phút)", "T (°C)",
          xticks=[0, 10, 20, 30, 40, 50, 60], yticks=[20, 40, 60, 80])
    save(fig, "b1_do_thi_nguoi_lanh")
    return _reg("b1_do_thi_nguoi_lanh")


# ---------------------------------------------------------------- 13. nhiệt lượng kế
def b1_nhiet_luong_ke():
    fig, ax = plt.subplots(figsize=(4.0, 3.8))
    clean(ax, -0.6, 6.6, -0.6, 6.4)
    ax.add_patch(Rectangle((0.3, 0.3), 5.4, 4.6, fc="#f2f4f6", ec="#333333", lw=2.4))
    ax.add_patch(Rectangle((0.85, 0.75), 4.3, 3.6, fc="white", ec=GREY, lw=1.6))
    ax.add_patch(Rectangle((0.85, 0.75), 4.3, 2.5, fc="#d8e8f8", ec="none"))
    ax.text(3.0, 1.9, "nước", fontsize=10, color=BLUE, ha="center", va="center")
    ax.text(0.45, 4.55, "vỏ cách nhiệt", fontsize=8, color="#333333", ha="left",
            va="center")
    # nhiệt kế
    ax.plot([4.5, 4.5], [5.8, 1.5], color=GREEN, lw=2.2)
    ax.add_patch(Circle((4.5, 1.35), 0.16, fc=GREEN, ec=GREEN))
    ax.text(4.75, 5.5, "nhiệt kế", fontsize=8.5, color=GREEN, ha="left")
    # que khuấy
    ax.plot([1.7, 1.7], [5.6, 1.2], color="#5a6470", lw=1.8)
    ax.plot([1.35, 2.05], [1.2, 1.2], color="#5a6470", lw=1.8)
    ax.text(1.05, 5.5, "que khuấy", fontsize=8.5, color="#5a6470", ha="left")
    ax.text(3.0, -0.32, "nhiệt dung của bình: C (chưa biết)", fontsize=8.8,
            color=RED, ha="center")
    save(fig, "b1_nhiet_luong_ke")
    return _reg("b1_nhiet_luong_ke")


# ---------------------------------------------------------------- 14. xilanh hai ngăn
def b1_xilanh_hai_ngan():
    fig, ax = plt.subplots(figsize=(6.8, 2.7))
    clean(ax, -0.6, 11.4, -1.9, 3.2)
    ax.add_patch(Rectangle((0.4, 0.3), 10.0, 2.0, fc="white", ec=GREY, lw=2.2))
    ax.add_patch(Rectangle((0.4, 0.3), 5.0, 2.0, fc="#fdece0", ec="none"))
    ax.add_patch(Rectangle((5.4, 0.3), 5.0, 2.0, fc="#d8e8f8", ec="none"))
    ax.add_patch(Rectangle((5.32, 0.24), 0.16, 2.12, fc="#5a6470", ec="#333333", lw=1.0))
    ax.text(2.9, 1.3, "ngăn trái\n(nung nóng 127 °C)", fontsize=9, color=RED,
            ha="center", va="center")
    ax.text(7.9, 1.3, "ngăn phải\n(giữ 27 °C)", fontsize=9, color=BLUE,
            ha="center", va="center")
    ax.text(5.4, 2.62, "pit-tông", fontsize=8.8, color="#333333", ha="center")
    ax.annotate("", xy=(5.4, -0.35), xytext=(0.4, -0.35),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.2))
    ax.text(2.9, -0.72, "50 cm", fontsize=9, color=GREY, ha="center", va="top")
    ax.annotate("", xy=(10.4, -0.35), xytext=(5.4, -0.35),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.2))
    ax.text(7.9, -0.72, "50 cm", fontsize=9, color=GREY, ha="center", va="top")
    arrow(ax, 5.7, 2.85, 6.6, 2.85, color=RED, lw=1.6)
    ax.text(6.9, 2.85, "?", fontsize=11, color=RED, ha="left", va="center")
    for k in range(4):
        x = 1.2 + k * 1.05
        ax.plot([x, x + 0.12, x - 0.05, x + 0.08], [-1.5, -1.3, -1.12, -0.95],
                color=ORANGE, lw=1.3)
    save(fig, "b1_xilanh_hai_ngan")
    return _reg("b1_xilanh_hai_ngan")


# ---------------------------------------------------------------- 15. bơm hút chân không
def b1_bom_hut():
    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    clean(ax, -0.4, 13.0, -1.2, 4.2)
    ax.add_patch(Rectangle((0.4, 0.3), 4.6, 3.0, fc="#d8e8f8", ec=GREY, lw=2.0))
    ax.text(2.7, 1.8, "bình  V = 4 L\np₀ = 10⁵ Pa", fontsize=9.5, color=BLUE,
            ha="center", va="center")
    ax.plot([5.0, 6.6], [1.8, 1.8], color=GREY, lw=2.4)
    ax.add_patch(Circle((5.8, 2.35), 0.28, fc="white", ec=RED, lw=1.4))
    ax.text(5.8, 2.95, "van", fontsize=8.5, color=RED, ha="center")
    ax.add_patch(Rectangle((6.6, 0.9), 3.4, 1.8, fc="#eef4fb", ec=GREY, lw=1.8))
    ax.text(7.6, 1.8, "V₀ = 1 L", fontsize=9, color=GREY, ha="center", va="center")
    ax.add_patch(Rectangle((8.6, 0.85), 0.35, 1.9, fc="#9aa5b1", ec="#5a6470", lw=1.0))
    ax.plot([8.95, 11.4], [1.8, 1.8], color="#5a6470", lw=3.0)
    ax.add_patch(Rectangle((11.4, 1.35), 0.5, 0.9, fc="#5a6470", ec="none"))
    arrow(ax, 9.6, 3.25, 11.4, 3.25, color=RED, lw=1.8)
    ax.text(10.5, 3.55, "kéo pit-tông", fontsize=9, color=RED, ha="center")
    ax.text(6.4, -0.7, "xilanh của bơm hút", fontsize=9, color=GREY, ha="center")
    save(fig, "b1_bom_hut")
    return _reg("b1_bom_hut")


# ---------------------------------------------------------------- 16. nước đá → hơi
def b1_do_thi_da_nuoc_hoi():
    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    t = [0, 21, 191, 401, 1531]
    T = [-20, 0, 0, 100, 100]
    ax.plot(t, T, color=RED, lw=2.3)
    for x in (21, 191, 401, 1531):
        ax.plot([x, x], [-30, 0 if x <= 191 else 100], ls="--", lw=0.9, color=LGREY,
                zorder=0)
    ax.plot(t, T, "o", ms=4.5, color=RED, zorder=5)
    ax.text(100, 6, "nóng chảy", fontsize=9, color=BLUE, ha="center")
    ax.text(940, 106, "hoá hơi", fontsize=9, color=GREEN, ha="center")
    ax.text(300, 42, "nước nóng lên", fontsize=9, color=GREY, ha="center", rotation=52)
    frame(ax, (0, 1650), (-32, 125), "t (s)", "T (°C)",
          xticks=[0, 21, 191, 401, 1531], yticks=[-20, 0, 50, 100])
    for lb in ax.get_xticklabels():
        lb.set_fontsize(8.2)
    save(fig, "b1_do_thi_da_nuoc_hoi")
    return _reg("b1_do_thi_da_nuoc_hoi")


ALL = [b1_do_thi_dun_nong, b1_chu_trinh_pV, b1_ong_thuy_ngan, b1_pT_dang_tich,
       b1_xilanh_boyle, b1_V_theo_1p, b1_xilanh_chan, b1_VT_hai_duong,
       b1_khinh_khi_cau, b1_binh_chan_khong, b1_Q_deltaT, b1_pV_duong_thang,
       b1_do_thi_nguoi_lanh, b1_nhiet_luong_ke, b1_xilanh_hai_ngan, b1_bom_hut,
       b1_do_thi_da_nuoc_hoi]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
