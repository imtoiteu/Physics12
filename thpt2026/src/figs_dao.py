# -*- coding: utf-8 -*-
"""Hình vẽ cho CHƯƠNG 1 VẬT LÍ 11 – DAO ĐỘNG."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Ellipse, Arc, FancyBboxPatch

from figbase import (save, arrow, clean, frame, hatch_ground,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)
from figgen import curve, points, spring, _reg, MADE


def _x(A, T, phi, tmax, n=500):
    t = np.linspace(0, tmax, n)
    return t, A * np.cos(2 * np.pi * t / T + phi)


# =============================================================== ĐỒ THỊ DAO ĐỘNG
def d_dt_xt():
    """A = 4 cm, T = 0,4 s, φ = 0."""
    t, x = _x(4, 0.4, 0.0, 0.8)
    return curve("d_dt_xt", [dict(x=t, y=x, c=RED)],
                 "t (s)", "x (cm)", (0, 0.86), (-5.6, 5.6),
                 xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
                 yticks=[-4, -2, 0, 2, 4], axhline=True, size=(6.4, 3.4))


def d_dt_xt2():
    """A = 5 cm, T = 0,6 s, φ = −π/2 (xuất phát từ VTCB theo chiều dương)."""
    t, x = _x(5, 0.6, -np.pi / 2, 1.2)
    return curve("d_dt_xt2", [dict(x=t, y=x, c=BLUE)],
                 "t (s)", "x (cm)", (0, 1.28), (-6.8, 6.8),
                 xticks=[0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05, 1.2],
                 yticks=[-5, -2.5, 0, 2.5, 5], axhline=True, size=(6.4, 3.4))


def d_dt_lechpha():
    """Hai dao động cùng chu kì 0,4 s, lệch pha π/2."""
    t, x1 = _x(4, 0.4, 0.0, 0.8)
    _, x2 = _x(3, 0.4, -np.pi / 2, 0.8)
    return curve("d_dt_lechpha",
                 [dict(x=t, y=x1, c=RED, label="(1)"), dict(x=t, y=x2, c=BLUE, label="(2)")],
                 "t (s)", "x (cm)", (0, 0.90), (-5.6, 5.6),
                 xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
                 yticks=[-4, -2, 0, 2, 4], axhline=True, legend="upper right",
                 size=(6.4, 3.4))


def d_dt_xva():
    """Ba đồ thị x, v, a của cùng một dao động: A = 5 cm, T = 0,4 s, φ = 0."""
    T, A = 0.4, 0.05
    w = 2 * np.pi / T
    t = np.linspace(0, 0.8, 500)
    fig, axs = plt.subplots(3, 1, figsize=(6.0, 5.2), sharex=True)
    data = [(A * 100 * np.cos(w * t), "x (cm)", RED, [-5, 0, 5]),
            (-A * w * np.cos(w * t + np.pi / 2) * 0 - A * w * np.sin(w * t), "v (m/s)",
             BLUE, [-0.8, 0, 0.8]),
            (-A * w * w * np.cos(w * t), "a (m/s²)", GREEN, [-12, 0, 12])]
    for ax, (y, lab, c, yt) in zip(axs, data):
        ax.plot(t, y, color=c, lw=2.2)
        ax.axhline(0, color=GREY, lw=1.0)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.set_ylabel(lab, fontsize=10)
        ax.set_yticks(yt)
        ax.set_xlim(0, 0.84)
        ax.grid(alpha=0.3, ls=":", lw=0.8)
        ax.tick_params(labelsize=8.5)
    axs[2].set_xlabel("t (s)", fontsize=10)
    axs[2].set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    fig.tight_layout()
    save(fig, "d_dt_xva"); return _reg("d_dt_xva")


def d_dt_nangluong_x():
    """W = 80 mJ, A = 4 cm."""
    x = np.linspace(-4, 4, 200)
    W = 80.0
    return curve("d_dt_nangluong_x",
                 [dict(x=x, y=W * (x / 4) ** 2, c=BLUE, label="Wt"),
                  dict(x=x, y=W * (1 - (x / 4) ** 2), c=RED, label="Wđ"),
                  dict(x=x, y=0 * x + W, c=GREEN, ls="--", lw=1.6, label="W")],
                 "x (cm)", "Năng lượng (mJ)", (-4.8, 5.6), (0, 96),
                 xticks=[-4, -2, 0, 2, 4], yticks=[0, 20, 40, 60, 80],
                 texts=[(4.3, 78, "Wt", BLUE, 10.5, "left", 1),
                        (4.3, 8, "Wđ", RED, 10.5, "left", 1),
                        (4.3, 86, "W", GREEN, 10.5, "left", 1)],
                 size=(5.8, 3.7))


def d_dt_nangluong_t():
    """W = 80 mJ, T = 0,4 s → chu kì năng lượng 0,2 s."""
    t = np.linspace(0, 0.8, 400)
    W = 80.0
    w = 2 * np.pi / 0.4
    return curve("d_dt_nangluong_t",
                 [dict(x=t, y=W * np.cos(w * t) ** 2, c=BLUE),
                  dict(x=t, y=W * np.sin(w * t) ** 2, c=RED)],
                 "t (s)", "Năng lượng (mJ)", (0, 0.90), (0, 98),
                 xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
                 yticks=[0, 20, 40, 60, 80],
                 texts=[(0.82, 78, "Wt", BLUE, 10.5, "left", 1),
                        (0.82, 20, "Wđ", RED, 10.5, "left", 1)],
                 size=(6.2, 3.5))


def d_dt_tatdan():
    t = np.linspace(0, 6.0, 900)
    A0, T, tau = 6.0, 0.6, 2.4
    return curve("d_dt_tatdan",
                 [dict(x=t, y=A0 * np.exp(-t / tau) * np.cos(2 * np.pi * t / T), c=RED, lw=1.6),
                  dict(x=t, y=A0 * np.exp(-t / tau), c=GREY, ls="--", lw=1.3),
                  dict(x=t, y=-A0 * np.exp(-t / tau), c=GREY, ls="--", lw=1.3)],
                 "t (s)", "x (cm)", (0, 6.3), (-8, 8),
                 xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[-6, -3, 0, 3, 6],
                 axhline=True, size=(6.4, 3.4))


def d_dt_conghuong():
    f = np.linspace(0.2, 4.0, 300)
    f0, F = 2.0, 1.0
    A1 = F / np.sqrt((f0 ** 2 - f ** 2) ** 2 + (0.25 * f) ** 2)
    A2 = F / np.sqrt((f0 ** 2 - f ** 2) ** 2 + (0.80 * f) ** 2)
    return curve("d_dt_conghuong",
                 [dict(x=f, y=A1, c=RED, label="ma sát nhỏ"),
                  dict(x=f, y=A2, c=BLUE, label="ma sát lớn")],
                 "f (Hz)", "Biên độ A (cm)", (0, 4.2), (0, 2.4),
                 xticks=[0, 1, 2, 3, 4], yticks=[0, 0.5, 1.0, 1.5, 2.0],
                 vlines=[(2.0, GREEN, ":")],
                 texts=[(2.08, 2.2, "f = f₀", GREEN, 9.5, "left"),
                        (2.9, 1.35, "ma sát nhỏ", RED, 9, "left"),
                        (2.9, 0.55, "ma sát lớn", BLUE, 9, "left")],
                 size=(6.0, 3.7))


def d_dt_T2_l():
    """Thí nghiệm đo g bằng con lắc đơn: T² theo ℓ."""
    l = np.array([0.4, 0.6, 0.8, 1.0, 1.2])
    T2 = 4 * np.pi ** 2 * l / 9.80
    ll = np.linspace(0, 1.35, 20)
    return curve("d_dt_T2_l",
                 [dict(x=ll, y=4 * np.pi ** 2 * ll / 9.80, c=BLUE, lw=1.7),
                  points(l, T2, c=RED)],
                 "ℓ (m)", "T² (s²)", (0, 1.42), (0, 5.6),
                 xticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], yticks=[0, 1, 2, 3, 4, 5],
                 size=(5.8, 3.7))


def d_dt_v_x():
    """Đồ thị v theo x (đường elip) – A = 5 cm, ω = 10 rad/s."""
    th = np.linspace(0, 2 * np.pi, 300)
    A, w = 5.0, 10.0
    return curve("d_dt_v_x",
                 [dict(x=A * np.cos(th), y=A * w * np.sin(th), c=PURPLE)],
                 "x (cm)", "v (cm/s)", (-7.0, 7.0), (-62, 62),
                 xticks=[-5, -2.5, 0, 2.5, 5], yticks=[-50, -25, 0, 25, 50],
                 axhline=True, vlines=[(0, GREY, "-")], size=(5.2, 3.9))


# =============================================================== SƠ ĐỒ
def d_sd_loxo_ngang():
    fig, ax = plt.subplots(figsize=(6.0, 2.6))
    clean(ax, -1.0, 13.0, -2.2, 3.6)
    hatch_ground(ax, 0.0, 12.0, 0.0, h=0.32, n=22)
    ax.add_patch(Rectangle((0.0, 0.0), 0.45, 2.6, fc="#5a6470", ec="none"))
    spring(ax, 0.45, 1.2, 6.4, 1.2, coils=10, amp=0.34)
    ax.add_patch(Rectangle((6.4, 0.35), 1.7, 1.7, fc="#fdece0", ec=RED, lw=2.0))
    ax.text(7.25, 1.2, "m", fontsize=12, color=RED, ha="center", va="center")
    ax.plot([7.25, 7.25], [0.0, 2.9], color=GREEN, lw=1.2, ls=":")
    ax.text(7.25, 3.15, "O (VTCB)", fontsize=8.8, color=GREEN, ha="center")
    arrow(ax, 7.25, -0.9, 10.2, -0.9, color=BLUE, lw=1.5)
    arrow(ax, 7.25, -0.9, 4.3, -0.9, color=BLUE, lw=1.5)
    ax.text(10.45, -0.9, "+x", fontsize=10, color=BLUE, ha="left", va="center")
    ax.text(7.25, -1.75, "Con lắc lò xo nằm ngang (bỏ qua ma sát)", fontsize=9,
            color=GREY, ha="center")
    save(fig, "d_sd_loxo_ngang"); return _reg("d_sd_loxo_ngang")


def d_sd_loxo_doc():
    fig, ax = plt.subplots(figsize=(3.0, 4.4))
    clean(ax, -2.8, 4.4, -1.2, 9.6)
    hatch_ground(ax, -0.6, 2.6, 9.0, h=-0.32, n=10)
    spring(ax, 1.0, 9.0, 1.0, 4.6, coils=9, amp=0.32)
    ax.add_patch(Rectangle((0.15, 3.0), 1.7, 1.6, fc="#fdece0", ec=RED, lw=2.0))
    ax.text(1.0, 3.8, "m", fontsize=12, color=RED, ha="center", va="center")
    ax.plot([-1.4, 3.4], [3.8, 3.8], color=GREEN, lw=1.2, ls=":")
    ax.text(3.55, 3.8, "O", fontsize=10, color=GREEN, ha="left", va="center")
    ax.plot([-1.4, 3.4], [5.6, 5.6], color=LGREY, lw=1.0, ls=":")
    ax.annotate("", xy=(-1.0, 3.8), xytext=(-1.0, 5.6),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.2))
    ax.text(-1.25, 4.7, "Δℓ₀", fontsize=9.5, color=BLUE, ha="right", va="center")
    ax.text(2.2, 5.75, "chiều dài tự nhiên", fontsize=7.8, color=GREY, ha="center")
    arrow(ax, 3.0, 3.8, 3.0, 1.8, color=BLUE, lw=1.4)
    ax.text(3.2, 2.4, "+x", fontsize=9.5, color=BLUE, ha="left")
    save(fig, "d_sd_loxo_doc"); return _reg("d_sd_loxo_doc")


def d_sd_cldon():
    fig, ax = plt.subplots(figsize=(3.4, 3.8))
    clean(ax, -3.6, 3.6, -1.0, 7.6)
    hatch_ground(ax, -1.4, 1.4, 6.8, h=-0.3, n=9)
    L, a = 5.6, np.radians(16)
    bx, by = L * np.sin(a), 6.8 - L * np.cos(a)
    ax.plot([0, 0], [6.8, 6.8 - L], color=LGREY, lw=1.1, ls=":")
    ax.plot([0, bx], [6.8, by], color="#5a6470", lw=1.6)
    ax.add_patch(Circle((bx, by), 0.42, fc="#fdece0", ec=RED, lw=2.0))
    ax.text(bx + 0.62, by, "m", fontsize=11, color=RED, ha="left", va="center")
    ax.add_patch(Arc((0, 6.8), 3.2, 3.2, theta1=270, theta2=270 + 16, color=GREEN, lw=1.4))
    ax.text(0.42, 5.05, "α", fontsize=11, color=GREEN)
    ax.text(-0.9, 4.2, "ℓ", fontsize=12, color="#5a6470", ha="right")
    ax.plot([0], [6.8 - L], "o", ms=5, color=GREEN)
    ax.text(-0.2, 6.8 - L - 0.45, "O", fontsize=10, color=GREEN, ha="right")
    save(fig, "d_sd_cldon"); return _reg("d_sd_cldon")


def d_sd_vongtron():
    fig, ax = plt.subplots(figsize=(3.8, 3.6))
    clean(ax, -4.6, 4.6, -4.4, 4.6)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(3.2 * np.cos(th), 3.2 * np.sin(th), color=LGREY, lw=1.4)
    arrow(ax, -4.2, 0, 4.3, 0, color=GREY, lw=1.2)
    arrow(ax, 0, -3.9, 0, 4.2, color=GREY, lw=1.2)
    ax.text(4.35, -0.35, "x", fontsize=10, color=GREY)
    a = np.radians(55)
    px, py = 3.2 * np.cos(a), 3.2 * np.sin(a)
    arrow(ax, 0, 0, px, py, color=RED, lw=2.0)
    ax.plot([px, px], [py, 0], ls="--", lw=1.1, color=BLUE)
    ax.plot([px], [0], "o", ms=7, color=BLUE)
    ax.text(px + 0.15, 0.42, "P", fontsize=10.5, color=BLUE)
    ax.text(px * 0.55 - 0.2, py * 0.55 + 0.3, "A", fontsize=11, color=RED)
    ax.add_patch(Arc((0, 0), 1.7, 1.7, theta1=0, theta2=55, color=GREEN, lw=1.3))
    ax.text(1.05, 0.42, "φ", fontsize=11, color=GREEN)
    ax.add_patch(Arc((0, 0), 6.8, 6.8, theta1=58, theta2=95, color=ORANGE, lw=1.5))
    arrow(ax, 3.2 * np.cos(np.radians(93)), 3.4 * np.sin(np.radians(93)),
          3.4 * np.cos(np.radians(97)), 3.4 * np.sin(np.radians(97)), color=ORANGE,
          lw=1.4, ms=11)
    ax.text(-1.15, 3.75, "ω", fontsize=12, color=ORANGE)
    ax.text(0, -4.2, "Hình chiếu P dao động điều hoà", fontsize=8.8, color=GREY,
            ha="center")
    save(fig, "d_sd_vongtron"); return _reg("d_sd_vongtron")


def d_sd_do_chuki():
    fig, ax = plt.subplots(figsize=(4.4, 3.8))
    clean(ax, -3.2, 6.2, -1.4, 8.0)
    hatch_ground(ax, -1.2, 1.2, 7.2, h=-0.3, n=8)
    ax.plot([0, 0], [7.2, 2.0], color="#5a6470", lw=1.5)
    ax.add_patch(Circle((0, 1.7), 0.38, fc="#fdece0", ec=RED, lw=1.8))
    for s in (-1, 1):
        ax.plot([0, s * 1.5], [7.2, 7.2 - 5.28], color=LGREY, lw=1.0, ls=":")
        ax.add_patch(Circle((s * 1.5, 7.2 - 5.28 - 0.2), 0.30, fc="none", ec=LGREY, lw=1.2))
    # cổng quang
    ax.add_patch(Rectangle((-0.95, 1.15), 0.42, 1.1, fc=BLUE, ec="none"))
    ax.add_patch(Rectangle((0.53, 1.15), 0.42, 1.1, fc=BLUE, ec="none"))
    ax.plot([-0.53, 0.53], [1.7, 1.7], color=RED, lw=1.0, ls=":")
    ax.text(-1.15, 0.7, "cổng quang điện", fontsize=8.4, color=BLUE, ha="center",
            va="top")
    ax.add_patch(Rectangle((2.6, 0.9), 3.2, 1.6, fc="white", ec="#333333", lw=1.6))
    ax.add_patch(Rectangle((2.95, 1.25), 2.5, 0.9, fc="#1b2a33", ec="none"))
    ax.text(4.2, 1.7, "0,000 s", fontsize=8.6, color="#7ee787", ha="center",
            va="center", family="DejaVu Sans Mono")
    ax.text(4.2, 2.8, "đồng hồ đo\nthời gian hiện số", fontsize=8.2, color="#333333",
            ha="center")
    ax.plot([0.95, 2.6], [1.7, 1.7], color=BLUE, lw=1.2)
    ax.text(0, -1.1, "Đo chu kì con lắc đơn để xác định g", fontsize=9, color=GREY,
            ha="center")
    save(fig, "d_sd_do_chuki"); return _reg("d_sd_do_chuki")


def d_sd_congHuong_thuctien():
    fig, ax = plt.subplots(figsize=(5.6, 2.6))
    clean(ax, -0.6, 13.4, -1.8, 4.6)
    ax.add_patch(Rectangle((0.4, 0.0), 12.6, 0.5, fc="#c9ced3", ec="#5a6470", lw=1.2))
    for x in (2.0, 6.6, 11.2):
        ax.add_patch(Rectangle((x - 0.28, 0.5), 0.56, 2.4, fc="#8e9aa6", ec="none"))
    ax.plot([1.72, 11.48], [2.9, 2.9], color="#5a6470", lw=3.0)
    xs = np.linspace(1.72, 11.48, 200)
    ax.plot(xs, 2.9 + 0.42 * np.sin(np.pi * (xs - 1.72) / (11.48 - 1.72)),
            color=RED, lw=1.6, ls="--")
    ax.text(6.6, 4.0, "Cầu dao động mạnh khi tần số ngoại lực trùng tần số riêng",
            fontsize=9, color=RED, ha="center")
    for k, x in enumerate((3.4, 5.0, 8.2, 9.8)):
        ax.add_patch(Circle((x, 3.55), 0.22, fc=BLUE, ec="none"))
        ax.plot([x, x], [3.33, 3.05], color=BLUE, lw=1.2)
    ax.text(6.6, -1.2, "Đoàn người bước đều qua cầu – hiện tượng cộng hưởng",
            fontsize=9, color=GREY, ha="center")
    save(fig, "d_sd_congHuong_thuctien"); return _reg("d_sd_congHuong_thuctien")


ALL = [d_dt_xt, d_dt_xt2, d_dt_lechpha, d_dt_xva, d_dt_nangluong_x, d_dt_nangluong_t,
       d_dt_tatdan, d_dt_conghuong, d_dt_T2_l, d_dt_v_x, d_sd_loxo_ngang,
       d_sd_loxo_doc, d_sd_cldon, d_sd_vongtron, d_sd_do_chuki,
       d_sd_congHuong_thuctien]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
