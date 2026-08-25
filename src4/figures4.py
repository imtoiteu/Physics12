# -*- coding: utf-8 -*-
"""Sinh hình vẽ gốc cho HỆ THỐNG ĐỀ KIỂM TRA theo chương (Vật lí 12 - Chương I, II).

Toàn bộ hình đều được vẽ mới bằng matplotlib, số liệu trên hình khớp chính xác với
số liệu trong đề. Quy ước tên: t<chương><số đề><chữ cái>, ví dụ t11a = Chương 1, Đề 1,
hình a.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Rectangle, Circle, FancyArrowPatch, Polygon,
                                FancyBboxPatch, Arc, Ellipse)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.unicode_minus"] = True

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

RED, BLUE, GREEN, ORANGE, GREY = "#c0392b", "#1f4e9c", "#1e8449", "#d35400", "#555555"
PURPLE, TEAL = "#6c3483", "#117a65"
BOX = dict(fc="white", ec="none", alpha=0.88, pad=1.4)


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ", name)


def arrow(ax, x1, y1, x2, y2, color="k", lw=1.6, ms=12, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=ms, color=color, lw=lw, **kw))


def clean(ax, xl, xr, yb, yt, eq=True):
    ax.set_xlim(xl, xr); ax.set_ylim(yb, yt)
    if eq:
        ax.set_aspect("equal")
    ax.axis("off")


from matplotlib.ticker import FuncFormatter

# Dấu thập phân trên trục dùng dấu phẩy theo chuẩn tiếng Việt.
VN = FuncFormatter(lambda v, _p: ("%g" % v).replace(".", ",").replace("-", "−"))


def grid(ax):
    ax.grid(True, ls=":", lw=0.7, color="#b9b9b9")
    ax.set_axisbelow(True)
    ax.xaxis.set_major_formatter(VN)
    ax.yaxis.set_major_formatter(VN)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ===================================================================
#                    CHƯƠNG I - ĐỀ SỐ 1
# ===================================================================

def t11a():
    """Đồ thị nhiệt độ - thời gian khi đun một khối nước đá từ -20 °C."""
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    t = [0, 8, 20, 44, 60]
    T = [-20, 0, 0, 100, 100]
    ax.plot(t, T, color=BLUE, lw=2.6, marker="o", ms=6, mfc="white", mec=BLUE, zorder=4)
    ax.axhline(0, color=GREY, lw=0.9, ls="--")
    ax.axhline(100, color=GREY, lw=0.9, ls="--")
    for x, lab in [(4.0, "I"), (14.0, "II"), (32.0, "III"), (52.0, "IV")]:
        ax.text(x, 118, lab, ha="center", va="center", fontsize=12.5, fontweight="bold",
                color=RED, bbox=dict(boxstyle="round,pad=0.30", fc="#fdecea", ec=RED, lw=1.2))
    for x in (8, 20, 44):
        ax.axvline(x, color="#c9c9c9", lw=0.9, ls=":")
    ax.set_xlabel("Thời gian t", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(-3, 65); ax.set_ylim(-38, 133)
    ax.set_xticks([])
    ax.set_yticks([-20, 0, 25, 50, 75, 100])
    ax.yaxis.set_major_formatter(VN)
    ax.grid(True, axis="y", ls=":", lw=0.7, color="#b9b9b9")
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "t11a")


def t11b():
    """Sơ đồ nhiệt lượng kế đo nhiệt dung riêng của một khối kim loại."""
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    # bình cách nhiệt (hai lớp)
    ax.add_patch(Rectangle((1.0, 0.4), 4.0, 3.0, fc="#f2f4f6", ec="k", lw=2.0))
    ax.add_patch(Rectangle((1.35, 0.62), 3.3, 2.55, fc="#eaf3fb", ec=GREY, lw=1.3))
    # nước
    ax.add_patch(Rectangle((1.35, 0.62), 3.3, 1.75, fc="#bcdcf5", ec="none"))
    ax.plot([1.35, 4.65], [2.37, 2.37], color=BLUE, lw=1.5)
    ax.text(2.05, 1.45, "nước", fontsize=10.5, color=BLUE, style="italic")
    # khối kim loại
    ax.add_patch(Rectangle((3.35, 0.75), 0.85, 0.62, fc="#c9ccd1", ec="k", lw=1.4, zorder=3))
    ax.annotate("khối kim loại", xy=(4.2, 1.06), xytext=(6.05, 0.95),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # nhiệt kế
    ax.add_patch(Rectangle((2.30, 1.05), 0.16, 3.05, fc="white", ec="k", lw=1.2, zorder=4))
    ax.add_patch(Rectangle((2.30, 1.05), 0.16, 0.95, fc=RED, ec="none", zorder=5))
    ax.add_patch(Circle((2.38, 1.02), 0.155, fc=RED, ec="k", lw=1.0, zorder=5))
    ax.annotate("nhiệt kế", xy=(2.46, 3.75), xytext=(0.35, 4.15),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # que khuấy
    ax.plot([3.55, 3.55], [1.55, 4.05], color=GREY, lw=2.0, zorder=4)
    ax.plot([3.30, 3.80], [1.55, 1.55], color=GREY, lw=2.0, zorder=4)
    ax.annotate("que khuấy", xy=(3.55, 3.90), xytext=(5.95, 4.05),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # nắp
    ax.add_patch(Rectangle((0.85, 3.40), 4.30, 0.22, fc="#dfe3e6", ec="k", lw=1.4))
    ax.annotate("vỏ cách nhiệt", xy=(1.05, 2.0), xytext=(-1.35, 1.95),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    clean(ax, -1.5, 8.3, -0.35, 4.7, eq=False)
    ax.set_aspect("equal")
    save(fig, "t11b")


def t11c():
    """So sánh sắp xếp phân tử ở ba thể."""
    fig, axs = plt.subplots(1, 3, figsize=(9.2, 3.1))
    rng = np.random.RandomState(11)
    titles = ["THỂ RẮN", "THỂ LỎNG", "THỂ KHÍ"]
    for k, ax in enumerate(axs):
        if k == 0:
            pts = [(i * 0.86, j * 0.86) for i in range(5) for j in range(5)]
        elif k == 1:
            pts = [(i * 0.86 + rng.uniform(-0.20, 0.20),
                    j * 0.86 + rng.uniform(-0.20, 0.20))
                   for i in range(5) for j in range(4)]
        else:
            pts = []
            while len(pts) < 9:
                q = (rng.uniform(0.1, 3.34), rng.uniform(0.1, 3.34))
                if all((q[0] - a) ** 2 + (q[1] - b) ** 2 > 0.85 ** 2 for a, b in pts):
                    pts.append(q)
        for (x, y) in pts:
            ax.add_patch(Circle((x, y), 0.26, fc="#aed6f1", ec=BLUE, lw=1.1, zorder=3))
        if k == 2:
            for (x, y) in pts[::2]:
                a = rng.uniform(0, 2 * np.pi)
                arrow(ax, x, y, x + 0.62 * np.cos(a), y + 0.62 * np.sin(a),
                      color=RED, lw=1.1, ms=8)
        ax.set_title(titles[k], fontsize=12, fontweight="bold", color=BLUE, pad=6)
        clean(ax, -0.55, 4.0, -1.05, 4.05)
    save(fig, "t11c")


# ===================================================================
#                    CHƯƠNG I - ĐỀ SỐ 2
# ===================================================================

def t12a():
    """Đồ thị Q - Δt của hai chất lỏng X và Y có cùng khối lượng."""
    fig, ax = plt.subplots(figsize=(6.9, 4.3))
    dT = np.linspace(0, 50, 100)
    ax.plot(dT, 2.10 * dT, color=RED, lw=2.4, label="Chất lỏng X")
    ax.plot(dT, 0.84 * dT, color=BLUE, lw=2.4, label="Chất lỏng Y")
    ax.plot([40], [84], "o", color=RED, ms=7, zorder=5)
    ax.plot([40], [33.6], "o", color=BLUE, ms=7, zorder=5)
    ax.annotate("(40 ; 84)", xy=(40, 84), xytext=(20.5, 96),
                fontsize=10, color=RED,
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=RED))
    ax.annotate("(40 ; 33,6)", xy=(40, 33.6), xytext=(43.5, 20),
                fontsize=10, color=BLUE,
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=BLUE))
    ax.set_xlabel("Độ tăng nhiệt độ Δt (°C)", fontsize=11)
    ax.set_ylabel("Nhiệt lượng Q (kJ)", fontsize=11)
    ax.set_xlim(0, 58); ax.set_ylim(0, 112)
    grid(ax)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.95)
    save(fig, "t12a")


def t12b():
    """Đồ thị làm nguội của naphtalene lỏng (đông đặc)."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    t = [0, 4, 14, 22]
    T = [95, 80, 80, 58]
    ax.plot(t, T, color=BLUE, lw=2.4, marker="o", ms=5, mfc="white", mec=BLUE, zorder=4)
    ax.axhline(80, color=GREY, lw=0.9, ls="--")
    ax.text(23.0, 80, "80 °C", fontsize=10, va="center", ha="left", color=GREY)
    ax.annotate("", xy=(4, 72), xytext=(14, 72),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.3, color=RED))
    ax.text(9, 69.5, "10 phút", ha="center", va="top", fontsize=10, color=RED)
    ax.set_xlabel("Thời gian t (phút)", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(-1, 27); ax.set_ylim(52, 100)
    ax.set_xticks([0, 4, 8, 12, 14, 18, 22])
    grid(ax)
    save(fig, "t12b")


def t12c():
    """Bộ thí nghiệm đo nhiệt nóng chảy riêng của nước đá."""
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    # phễu chứa nước đá
    fx = [(1.25, 3.55), (4.05, 3.55), (2.98, 1.75), (2.32, 1.75)]
    ax.add_patch(Polygon(fx, fc="#eaf3fb", ec="k", lw=1.7))

    def inside(x, y):
        half = 0.33 + (y - 1.75) * (1.40 - 0.33) / (3.55 - 1.75)
        return abs(x - 2.65) < half - 0.16
    rng = np.random.RandomState(3)
    placed = 0
    while placed < 18:
        x = rng.uniform(1.35, 3.95); y = rng.uniform(1.90, 3.42)
        if inside(x, y):
            ax.add_patch(Rectangle((x - 0.13, y - 0.11), 0.26, 0.22,
                                   fc="#cfe8fb", ec=BLUE, lw=0.9, zorder=3))
            placed += 1
    ax.annotate("nước đá đang tan", xy=(1.85, 2.95), xytext=(-0.85, 3.30),
                fontsize=10, color=BLUE, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=BLUE))
    # điện trở đun nằm trong khối đá
    ax.plot([2.15, 3.15], [2.55, 2.55], color=RED, lw=3.0, zorder=6)
    ax.plot([2.15, 2.15], [2.55, 4.70], color=RED, lw=1.4, zorder=6)
    ax.plot([3.15, 3.15], [2.55, 4.70], color=RED, lw=1.4, zorder=6)
    ax.annotate("điện trở đun", xy=(2.65, 2.55), xytext=(-0.85, 2.10),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # oát kế
    ax.add_patch(FancyBboxPatch((1.80, 4.70), 1.70, 0.72,
                                boxstyle="round,pad=0.04", fc="#fdf6e3", ec="k", lw=1.5))
    ax.text(2.65, 5.06, "OÁT KẾ", ha="center", va="center", fontsize=10, fontweight="bold")
    # cốc hứng + cân
    ax.add_patch(Rectangle((2.20, 0.60), 0.90, 0.95, fc="#bcdcf5", ec="k", lw=1.5))
    ax.text(2.65, 1.05, "nước", ha="center", va="center", fontsize=9.5, color=BLUE)
    ax.add_patch(Rectangle((1.70, 0.10), 1.90, 0.48, fc="#e8e8e8", ec="k", lw=1.5))
    ax.text(2.65, 0.34, "CÂN ĐIỆN TỬ", ha="center", va="center", fontsize=9, fontweight="bold")
    for y in (1.66, 1.56):
        ax.add_patch(Ellipse((2.65, y), 0.10, 0.15, fc=BLUE, ec="none"))
    # đồng hồ bấm giây
    ax.add_patch(Circle((5.60, 3.05), 0.62, fc="white", ec="k", lw=1.7))
    ax.plot([5.60, 5.60], [3.05, 3.53], color="k", lw=1.5)
    ax.plot([5.60, 5.93], [3.05, 3.05], color=RED, lw=1.4)
    ax.text(5.60, 2.22, "đồng hồ\nbấm giây", ha="center", va="top", fontsize=9.5)
    clean(ax, -1.0, 6.9, -0.1, 5.7, eq=False)
    ax.set_aspect("equal")
    save(fig, "t12c")


# ===================================================================
#                    CHƯƠNG I - ĐỀ SỐ 3
# ===================================================================

def t13a():
    """Đồ thị nhiệt độ - nhiệt lượng cung cấp cho 0,50 kg một chất."""
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    Q = [0, 32.5, 137.5, 190.0]
    T = [-50, 0, 0, 40]
    ax.plot(Q, T, color=BLUE, lw=2.4, marker="o", ms=5.5, mfc="white", mec=BLUE, zorder=4)
    ax.axhline(0, color=GREY, lw=0.9, ls="--")
    for x, y, lab, dx, dy in [(0, -50, "M", -9, -6), (32.5, 0, "N", -8, 6),
                              (137.5, 0, "P", 2, 7), (190.0, 40, "Q", 4, 2)]:
        ax.annotate(lab, xy=(x, y), xytext=(x + dx, y + dy), fontsize=11.5,
                    fontweight="bold", color=RED)
    ax.set_xlabel("Nhiệt lượng đã cung cấp Q (kJ)", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(-14, 215); ax.set_ylim(-62, 55)
    ax.set_xticks([0, 32.5, 137.5, 190])

    ax.set_yticks([-50, -25, 0, 20, 40])
    grid(ax)
    save(fig, "t13a")


def t13b():
    """Hai cách làm thay đổi nội năng: cọ xát và truyền nhiệt."""
    fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.5))
    # (a) cọ xát
    ax = axs[0]
    ax.add_patch(Rectangle((0.8, 1.0), 2.6, 0.9, fc="#d5b895", ec="k", lw=1.6))
    ax.text(2.1, 1.45, "khối kim loại", ha="center", va="center", fontsize=9.5)
    ax.add_patch(Rectangle((1.3, 1.95), 1.5, 0.55, fc="#c9ccd1", ec="k", lw=1.5))
    ax.text(2.05, 2.22, "tấm nhám", ha="center", va="center", fontsize=9)
    arrow(ax, 2.95, 2.85, 3.85, 2.85, color=RED, lw=2.0, ms=13)
    arrow(ax, 1.15, 2.85, 0.25, 2.85, color=RED, lw=2.0, ms=13)
    ax.plot([1.15, 2.95], [2.85, 2.85], color=RED, lw=2.0)
    ax.text(2.05, 3.15, "cọ xát qua lại", ha="center", va="bottom", fontsize=10, color=RED)
    ax.text(2.1, -0.35, "(a)", ha="center", va="top",
            fontsize=13, fontweight="bold", color=BLUE)
    clean(ax, -0.1, 4.3, -1.0, 3.7)
    # (b) truyền nhiệt
    ax = axs[1]
    ax.add_patch(Rectangle((0.8, 1.0), 2.6, 0.9, fc="#d5b895", ec="k", lw=1.6))
    ax.text(2.1, 1.45, "khối kim loại", ha="center", va="center", fontsize=9.5)
    for x in (1.3, 2.1, 2.9):
        th = np.linspace(0, 2.6 * np.pi, 90)
        ax.plot(x + 0.13 * np.sin(th), 0.30 + 0.55 * th / (2.6 * np.pi),
                color=ORANGE, lw=1.6)
    ax.text(2.1, 0.10, "nguồn nhiệt", ha="center", va="top", fontsize=9.5, color=ORANGE)
    ax.text(2.1, -0.35, "(b)", ha="center", va="top",
            fontsize=13, fontweight="bold", color=BLUE)
    clean(ax, -0.1, 4.3, -1.0, 3.7)
    save(fig, "t13b")


def t13c():
    """Đồ thị nhiệt độ theo thời gian của hai vật trao đổi nhiệt."""
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    t = np.linspace(0, 10, 200)
    Ta = 34 + (90 - 34) * np.exp(-0.55 * t)
    Tb = 34 + (20 - 34) * np.exp(-0.55 * t)
    ax.plot(t, Ta, color=RED, lw=2.4, label="Vật A")
    ax.plot(t, Tb, color=BLUE, lw=2.4, label="Vật B")
    ax.axhline(34, color=GREY, lw=1.0, ls="--")
    ax.text(10.25, 34, "34 °C", fontsize=10, color=GREY, va="center")
    ax.plot([0], [90], "o", color=RED, ms=6)
    ax.plot([0], [20], "o", color=BLUE, ms=6)
    ax.text(0.35, 90, "90 °C", fontsize=10, color=RED, va="center")
    ax.text(0.35, 20, "20 °C", fontsize=10, color=BLUE, va="center")
    ax.set_xlabel("Thời gian (phút)", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(0, 12.4); ax.set_ylim(12, 98)
    grid(ax)
    ax.legend(loc="center right", fontsize=10, framealpha=0.95)
    save(fig, "t13c")


# ===================================================================
#                    CHƯƠNG I - ĐỀ SỐ 4
# ===================================================================

def t14a():
    """Đồ thị nhiệt độ - thời gian của hai mẫu chất được đun bằng cùng một bếp."""
    fig, ax = plt.subplots(figsize=(7.2, 4.3))
    t1 = np.array([0, 6]); T1 = np.array([20, 80])
    t2 = np.array([0, 10]); T2 = np.array([20, 80])
    ax.plot(t1, T1, color=RED, lw=2.4, marker="o", ms=5, label="Mẫu I")
    ax.plot(t2, T2, color=BLUE, lw=2.4, marker="s", ms=5, label="Mẫu II")
    ax.plot([0, 10], [80, 80], color=GREY, lw=0.9, ls="--")
    ax.plot([6, 6], [20, 80], color=GREY, lw=0.9, ls=":")
    ax.plot([10, 10], [20, 80], color=GREY, lw=0.9, ls=":")
    ax.set_xlabel("Thời gian đun t (phút)", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(0, 12.5); ax.set_ylim(15, 92)
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12])
    grid(ax)
    ax.legend(loc="lower right", fontsize=10, framealpha=0.95)
    save(fig, "t14a")


def t14b():
    """Sơ đồ bình nước nóng dùng điện trở, có tổn hao ra môi trường."""
    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    ax.add_patch(FancyBboxPatch((1.0, 0.6), 3.2, 2.9, boxstyle="round,pad=0.05",
                                fc="#f2f4f6", ec="k", lw=2.0))
    ax.add_patch(Rectangle((1.25, 0.85), 2.7, 2.15, fc="#bcdcf5", ec=BLUE, lw=1.2))
    ax.text(2.6, 1.95, "nước\n5,0 kg", ha="center", va="center", fontsize=10.5, color=BLUE)
    ax.plot([1.75, 3.45], [1.15, 1.15], color=RED, lw=3.0, zorder=5)
    for x in np.linspace(1.85, 3.35, 7):
        ax.plot([x, x], [1.15, 1.30], color=RED, lw=1.6, zorder=5)
    ax.annotate("dây đốt", xy=(2.60, 1.15), xytext=(4.75, 0.95), fontsize=10,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    arrow(ax, 0.95, 2.60, 0.15, 2.60, color=ORANGE, lw=1.8, ms=12)
    arrow(ax, 4.25, 2.60, 5.05, 2.60, color=ORANGE, lw=1.8, ms=12)
    ax.text(2.60, 3.75, "hao phí ra môi trường", ha="center", va="bottom",
            fontsize=10, color=ORANGE)
    ax.text(2.60, 0.20, "công suất điện P = 1500 W", ha="center", va="bottom",
            fontsize=10.5, fontweight="bold", color=RED)
    clean(ax, -0.6, 5.6, -0.05, 4.3, eq=False)
    ax.set_aspect("equal")
    save(fig, "t14b")


def t14c():
    """Đồ thị khối lượng nước đá còn lại theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    t = [0, 10, 15]
    m = [400, 0, 0]
    ax.plot(t, m, color=BLUE, lw=2.6, marker="o", ms=6.5, mfc="white", mec=BLUE, zorder=4)
    ax.plot([10, 10], [0, 400], color=GREY, lw=0.9, ls=":")
    ax.set_xlabel("Thời gian đun t (phút)", fontsize=11)
    ax.set_ylabel("Khối lượng nước đá còn lại m (g)", fontsize=11)
    ax.set_xlim(0, 16.2); ax.set_ylim(-25, 470)
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
    ax.set_yticks([0, 100, 200, 300, 400])
    grid(ax)
    save(fig, "t14c")


# ===================================================================
#                    CHƯƠNG I - ĐỀ SỐ 5
# ===================================================================

def t15a():
    """Đồ thị nhiệt độ - nhiệt lượng của 1,0 kg chất bí ẩn qua đủ ba giai đoạn."""
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    Q = [0, 24, 84, 156]
    T = [-40, 0, 0, 30]
    ax.plot(Q, T, color=BLUE, lw=2.6, marker="o", ms=6.5, mfc="white", mec=BLUE, zorder=4)
    ax.axhline(0, color=GREY, lw=0.8, ls="--")
    for x, y, lab in [(12, -28, "①"), (54, -9, "②"), (120, 8, "③")]:
        ax.text(x, y, lab, fontsize=15, color=RED, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="circle,pad=0.16", fc="white", ec=RED, lw=1.2))
    ax.set_xlabel("Nhiệt lượng đã cung cấp Q (kJ)", fontsize=11)
    ax.set_ylabel("Nhiệt độ (°C)", fontsize=11)
    ax.set_xlim(-9, 180); ax.set_ylim(-56, 46)
    ax.set_xticks([0, 24, 84, 156])
    ax.set_yticks([-40, -20, 0, 30])
    grid(ax)
    save(fig, "t15a")


def t15b():
    """Sơ đồ nguyên lí làm mát bằng bay hơi (bình gốm chứa nước)."""
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.add_patch(Polygon([(1.2, 0.4), (4.0, 0.4), (3.7, 3.0), (1.5, 3.0)],
                         fc="#e8d3b0", ec="k", lw=1.9))
    ax.add_patch(Polygon([(1.62, 0.62), (3.58, 0.62), (3.40, 2.35), (1.80, 2.35)],
                         fc="#bcdcf5", ec="none"))
    ax.text(2.6, 1.35, "nước", ha="center", va="center", fontsize=10.5, color=BLUE)
    ax.text(2.6, 3.15, "bình gốm xốp", ha="center", va="bottom", fontsize=10)
    for x0 in (1.30, 1.70, 3.55, 3.95):
        th = np.linspace(0, 2.4 * np.pi, 70)
        ax.plot(x0 + 0.11 * np.sin(th), 1.0 + 1.55 * th / (2.4 * np.pi),
                color=TEAL, lw=1.4)
    ax.text(0.45, 2.85, "hơi nước\nbay hơi", ha="center", va="bottom",
            fontsize=9.5, color=TEAL)
    ax.text(4.80, 2.85, "hơi nước\nbay hơi", ha="center", va="bottom",
            fontsize=9.5, color=TEAL)
    arrow(ax, 0.15, 1.55, 1.05, 1.55, color=GREY, lw=1.6, ms=12)
    ax.text(0.60, 1.35, "gió khô", ha="center", va="top", fontsize=9.5, color=GREY)
    clean(ax, -0.4, 5.7, -0.3, 4.1, eq=False)
    ax.set_aspect("equal")
    save(fig, "t15b")


def t15c():
    """Đồ thị công suất toả nhiệt của một lò sấy theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    t = [0, 4, 4, 10, 10, 16]
    P = [900, 900, 500, 500, 300, 300]
    ax.plot(t, P, color=RED, lw=2.6, zorder=4)
    ax.fill_between([0, 4], 0, 900, color="#fdecea", zorder=1)
    ax.fill_between([4, 10], 0, 500, color="#eaf3fb", zorder=1)
    ax.fill_between([10, 16], 0, 300, color="#eafaf1", zorder=1)
    ax.plot([4, 4], [0, 900], color=GREY, lw=0.8, ls=":")
    ax.plot([10, 10], [0, 500], color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("Thời gian t (phút)", fontsize=11)
    ax.set_ylabel("Công suất cấp nhiệt P (W)", fontsize=11)
    ax.set_xlim(0, 17.5); ax.set_ylim(0, 1050)
    ax.set_xticks([0, 4, 8, 10, 12, 16])
    ax.set_yticks([0, 300, 500, 700, 900])
    grid(ax)
    save(fig, "t15c")


# ===================================================================
#                    CHƯƠNG II - ĐỀ SỐ 1
# ===================================================================

def t21a():
    """Đường đẳng nhiệt trên giản đồ p - V."""
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    V = np.linspace(1.0, 6.0, 200)
    ax.plot(V, 6.0 / V, color=BLUE, lw=2.4)
    ax.plot([2.0], [3.0], "o", color=RED, ms=7, zorder=5)
    ax.plot([6.0], [1.0], "o", color=RED, ms=7, zorder=5)
    ax.annotate("(1)", xy=(2.0, 3.0), xytext=(2.25, 3.55), fontsize=12,
                color=RED, fontweight="bold")
    ax.annotate("(2)", xy=(6.0, 1.0), xytext=(5.55, 1.55), fontsize=12,
                color=RED, fontweight="bold")
    ax.plot([0, 2.0], [3.0, 3.0], color=GREY, lw=0.8, ls=":")
    ax.plot([2.0, 2.0], [0, 3.0], color=GREY, lw=0.8, ls=":")
    ax.plot([0, 6.0], [1.0, 1.0], color=GREY, lw=0.8, ls=":")
    ax.plot([6.0, 6.0], [0, 1.0], color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("V (lít)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(0, 7.2); ax.set_ylim(0, 4.6)
    ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, 1, 2, 3, 4])
    grid(ax)
    save(fig, "t21a")


def t21b():
    """Bộ thí nghiệm khảo sát định luật Boyle."""
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    # xi lanh nằm ngang
    ax.add_patch(Rectangle((1.0, 1.2), 4.4, 1.3, fc="white", ec="k", lw=2.0))
    ax.add_patch(Rectangle((1.0, 1.2), 2.2, 1.3, fc="#d6eaf8", ec="none"))
    ax.text(2.1, 1.85, "khí", ha="center", va="center", fontsize=11, color=BLUE)
    ax.add_patch(Rectangle((3.20, 1.14), 0.22, 1.42, fc="#95a5a6", ec="k", lw=1.4, zorder=4))
    ax.plot([3.42, 5.9], [1.85, 1.85], color="k", lw=3.0, zorder=3)
    ax.add_patch(Rectangle((5.9, 1.45), 0.45, 0.80, fc="#c9ccd1", ec="k", lw=1.4))
    arrow(ax, 6.55, 1.85, 5.85, 1.85, color=RED, lw=2.0, ms=13)
    ax.text(6.60, 2.25, "lực nén", fontsize=10, color=RED, ha="center")
    ax.annotate("pit-tông", xy=(3.31, 2.56), xytext=(3.15, 3.25), fontsize=10,
                ha="center", arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # áp kế
    ax.add_patch(Ellipse((1.55, 3.25), 1.10, 0.98, fc="#fdf6e3", ec="k", lw=1.8))
    ax.plot([1.55, 1.90], [3.25, 3.55], color=RED, lw=1.6)
    ax.plot([1.55, 1.55], [2.76, 2.50], color="k", lw=2.0)
    ax.text(1.55, 3.88, "áp kế", ha="center", va="bottom", fontsize=10)
    # thước đo
    ax.plot([1.0, 3.31], [0.85, 0.85], color=GREEN, lw=1.6)
    for x in np.linspace(1.0, 3.31, 8):
        ax.plot([x, x], [0.85, 0.98], color=GREEN, lw=1.0)
    ax.text(2.15, 0.62, "thước đo chiều dài cột khí ℓ", ha="center", va="top",
            fontsize=9.8, color=GREEN)
    clean(ax, 0.5, 7.4, 0.05, 4.3, eq=False)
    ax.set_aspect("equal")
    save(fig, "t21b")


def t21c():
    """Đồ thị V - T của quá trình đẳng áp, đường kéo dài qua gốc toạ độ."""
    fig, ax = plt.subplots(figsize=(6.8, 4.1))
    T = np.linspace(0, 400, 100)
    ax.plot(T, 0.010 * T, color=BLUE, lw=1.4, ls="--")
    T2 = np.linspace(270, 380, 60)
    ax.plot(T2, 0.010 * T2, color=BLUE, lw=2.8)
    ax.plot([300], [3.0], "o", color=RED, ms=7, zorder=5)
    ax.plot([360], [3.6], "o", color=RED, ms=7, zorder=5)
    ax.annotate("(1)  300 K ; 3,0 L", xy=(300, 3.0), xytext=(120, 3.35),
                fontsize=10, color=RED,
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=RED))
    ax.annotate("(2)", xy=(360, 3.6), xytext=(330, 4.0),
                fontsize=11, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=RED))
    ax.set_xlabel("T (K)", fontsize=11)
    ax.set_ylabel("V (lít)", fontsize=11)
    ax.set_xlim(0, 430); ax.set_ylim(0, 4.7)
    grid(ax)
    save(fig, "t21c")


# ===================================================================
#                    CHƯƠNG II - ĐỀ SỐ 2
# ===================================================================

def t22a():
    """Đồ thị p - t (°C) của quá trình đẳng tích, cắt trục tại -273 °C."""
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    t = np.linspace(-273.15, 160, 100)
    p = 1.0 * (t + 273.15) / 273.15
    ax.plot(t, p, color=BLUE, lw=1.4, ls="--")
    t2 = np.linspace(0, 150, 60)
    ax.plot(t2, 1.0 * (t2 + 273.15) / 273.15, color=BLUE, lw=2.8)
    ax.plot([0], [1.0], "o", color=RED, ms=7, zorder=5)
    ax.annotate("t = 0 °C ; p = 1,00 atm", xy=(0, 1.0), xytext=(-250, 1.35),
                fontsize=10, color=RED,
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=RED))
    ax.plot([-273.15], [0], "o", color=GREEN, ms=7, zorder=5)
    ax.annotate("−273 °C", xy=(-273.15, 0), xytext=(-262, 0.28),
                fontsize=10, color=GREEN,
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color=GREEN))
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel("t (°C)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(-300, 190); ax.set_ylim(-0.12, 1.85)
    ax.set_xticks([-273, -200, -100, 0, 100])
    grid(ax)
    save(fig, "t22a")


def t22b():
    """Thí nghiệm khảo sát định luật Charles bằng ống nghiệm và giọt thuỷ ngân."""
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    # cốc nước
    ax.add_patch(Rectangle((0.6, 0.4), 3.4, 2.6, fc="#eaf3fb", ec="k", lw=1.8))
    ax.add_patch(Rectangle((0.62, 0.42), 3.36, 2.2, fc="#bcdcf5", ec="none"))
    ax.text(0.95, 1.05, "nước", fontsize=10, color=BLUE, style="italic",
            ha="center", va="center")
    # ống nghiệm chứa khí
    ax.add_patch(Rectangle((2.15, 0.75), 0.38, 3.55, fc="white", ec="k", lw=1.6, zorder=3))
    ax.add_patch(Rectangle((2.15, 0.75), 0.38, 2.10, fc="#d6eaf8", ec="none", zorder=3))
    ax.add_patch(Rectangle((2.15, 2.85), 0.38, 0.14, fc="#7f8c8d", ec="k", lw=0.9, zorder=4))
    ax.annotate("giọt thuỷ ngân", xy=(2.53, 2.92), xytext=(4.35, 3.35), fontsize=9.8,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    ax.annotate("cột khí", xy=(2.34, 1.8), xytext=(4.35, 1.35), fontsize=9.8,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # nhiệt kế
    ax.add_patch(Rectangle((1.35, 0.95), 0.14, 2.85, fc="white", ec="k", lw=1.2, zorder=4))
    ax.add_patch(Rectangle((1.35, 0.95), 0.14, 0.85, fc=RED, ec="none", zorder=5))
    ax.annotate("nhiệt kế", xy=(1.42, 3.60), xytext=(-0.35, 3.85), fontsize=9.8,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    # đèn cồn
    ax.add_patch(Polygon([(2.05, 0.05), (2.65, 0.05), (2.55, 0.32), (2.15, 0.32)],
                         fc="#f5cba7", ec="k", lw=1.2))
    for dx in (-0.14, 0, 0.14):
        ax.add_patch(Ellipse((2.35 + dx, 0.40), 0.10, 0.20, fc=ORANGE, ec="none"))
    ax.text(3.35, 0.14, "đun nóng từ từ", fontsize=9.8, color=ORANGE, va="center")
    # thước
    ax.plot([1.95, 1.95], [0.75, 2.85], color=GREEN, lw=1.5, zorder=5)
    ax.text(1.80, 1.80, "ℓ", fontsize=12, color=GREEN, ha="right", va="center")
    clean(ax, -0.5, 6.4, -0.25, 4.6, eq=False)
    ax.set_aspect("equal")
    save(fig, "t22b")


def t22c():
    """Ba đường đẳng nhiệt ứng với ba nhiệt độ khác nhau."""
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    V = np.linspace(0.8, 6.0, 200)
    for C, T, col in [(3.0, "T₁", BLUE), (5.0, "T₂", GREEN), (7.5, "T₃", RED)]:
        ax.plot(V, C / V, color=col, lw=2.3)
        ax.text(6.12, C / 6.0, T, fontsize=12, color=col, va="center", fontweight="bold")
    ax.set_xlabel("V", fontsize=11)
    ax.set_ylabel("p", fontsize=11)
    ax.set_xlim(0, 7.0); ax.set_ylim(0, 4.6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "t22c")


# ===================================================================
#                    CHƯƠNG II - ĐỀ SỐ 3
# ===================================================================

def t23a():
    """Chu trình ba giai đoạn trên giản đồ p - V (đẳng áp, đẳng tích, đẳng nhiệt)."""
    fig, ax = plt.subplots(figsize=(6.8, 4.3))
    # (1) 2 L, 1 atm -> đẳng áp -> (2) 6 L, 1 atm -> đẳng tích -> (3) 6 L, 3 atm ... không đóng
    # Dùng chu trình đóng nhất quán: (1) 1 atm,6 L -> đẳng tích -> (2) 3 atm,6 L
    # -> đẳng nhiệt -> (3) 9 atm,2 L ... quá lớn. Chọn:
    # (1) 6 L, 1 atm --đẳng tích--> (2) 6 L, 3 atm --đẳng nhiệt--> (3) 2 L, 9 atm : không đẹp
    # Chu trình dùng ở đây: (1) 2 L, 3 atm --đẳng nhiệt--> (2) 6 L, 1 atm
    #                       --đẳng tích--> (3) 6 L, 3 atm --?--> quay lại (1): không đẳng quá trình
    # => Dùng chu trình chuẩn: đẳng nhiệt - đẳng áp - đẳng tích
    # (1) 2 L, 3 atm --đẳng nhiệt (T=600K)--> (2) 6 L, 1 atm
    # (2) --đẳng áp--> (3) 2 L, 1 atm  (T giảm còn 200 K)
    # (3) --đẳng tích--> (1) 2 L, 3 atm  (T tăng lại 600 K)   ✓ khép kín
    ax.plot([2, 2], [1, 3], color=BLUE, lw=2.4)
    ax.plot([6, 2], [1, 1], color=GREEN, lw=2.4)
    V = np.linspace(2, 6, 120)
    ax.plot(V, 6.0 / V, color=RED, lw=2.4)
    arrow(ax, 3.4, 6.0 / 3.4, 3.9, 6.0 / 3.9, color=RED, lw=0, ms=15)
    arrow(ax, 4.4, 1, 3.9, 1, color=GREEN, lw=0, ms=15)
    arrow(ax, 2, 1.9, 2, 2.4, color=BLUE, lw=0, ms=15)
    for (x, y, lab, dx, dy) in [(2, 3, "(1)", -0.62, 0.16), (6, 1, "(2)", 0.14, 0.22),
                                (2, 1, "(3)", -0.62, -0.02)]:
        ax.plot([x], [y], "o", color="k", ms=6, zorder=5)
        ax.text(x + dx, y + dy, lab, fontsize=11.5, fontweight="bold")
    ax.set_xlabel("V (lít)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(0, 7.4); ax.set_ylim(0, 3.9)
    ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, 1, 2, 3])
    grid(ax)
    save(fig, "t23a")


def t23b():
    """Ống chữ U chứa thuỷ ngân, một nhánh kín giam cột khí."""
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    # hai nhánh
    ax.add_patch(Rectangle((1.0, 0.6), 0.42, 3.6, fc="white", ec="k", lw=1.8))
    ax.add_patch(Rectangle((2.6, 0.6), 0.42, 3.9, fc="white", ec="k", lw=1.8))
    ax.add_patch(Rectangle((1.0, 0.6), 2.02, 0.42, fc="white", ec="k", lw=1.8))
    # thuỷ ngân
    ax.add_patch(Rectangle((1.02, 0.62), 0.38, 1.55, fc="#8e9294", ec="none"))
    ax.add_patch(Rectangle((2.62, 0.62), 0.38, 2.35, fc="#8e9294", ec="none"))
    ax.add_patch(Rectangle((1.02, 0.62), 1.98, 0.38, fc="#8e9294", ec="none"))
    # cột khí bị giam ở nhánh trái (kín)
    ax.add_patch(Rectangle((1.02, 2.17), 0.38, 2.01, fc="#d6eaf8", ec="none"))
    ax.plot([1.0, 1.42], [4.20, 4.20], color="k", lw=2.6)
    ax.text(1.21, 3.25, "khí", ha="center", va="center", fontsize=10.5, color=BLUE)
    ax.text(1.21, 4.38, "đầu kín", ha="center", va="bottom", fontsize=9.6)
    ax.text(2.81, 4.62, "đầu hở", ha="center", va="bottom", fontsize=9.6)
    # chênh lệch mực
    ax.plot([1.42, 3.55], [2.17, 2.17], color=GREY, lw=0.8, ls=":")
    ax.plot([3.02, 3.55], [2.97, 2.97], color=GREY, lw=0.8, ls=":")
    arrow(ax, 3.42, 2.17, 3.42, 2.97, color=RED, lw=1.4, ms=10, style="<|-|>")
    ax.text(3.58, 2.57, "h", fontsize=12.5, color=RED, va="center", fontweight="bold")
    clean(ax, 0.5, 4.4, 0.1, 5.2, eq=False)
    ax.set_aspect("equal")
    save(fig, "t23b")


def t23c():
    """Bơm khí từ bình nén vào lốp xe."""
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    # bình khí nén
    ax.add_patch(FancyBboxPatch((0.6, 0.5), 1.3, 2.6, boxstyle="round,pad=0.10",
                                fc="#d5dbdb", ec="k", lw=2.0))
    ax.add_patch(Rectangle((1.10, 3.15), 0.30, 0.42, fc="#7f8c8d", ec="k", lw=1.3))
    ax.text(1.25, 1.80, "BÌNH\nKHÍ NÉN", ha="center", va="center",
            fontsize=10, fontweight="bold")
    ax.text(1.25, 0.18, "V = 20 L", ha="center", va="top", fontsize=10, color=BLUE)
    # ống dẫn
    ax.plot([1.40, 4.10], [3.36, 3.36], color="k", lw=2.4)
    ax.plot([4.10, 4.10], [3.36, 2.35], color="k", lw=2.4)
    # van
    ax.add_patch(Circle((2.75, 3.36), 0.22, fc=RED, ec="k", lw=1.3, zorder=5))
    ax.text(2.75, 3.72, "van", ha="center", va="bottom", fontsize=9.6, color=RED)
    # lốp xe
    ax.add_patch(Circle((4.10, 1.35), 1.05, fc="none", ec="k", lw=8, zorder=3))
    ax.add_patch(Circle((4.10, 1.35), 0.46, fc="#d5dbdb", ec="k", lw=1.5, zorder=4))
    ax.text(4.10, -0.05, "lốp xe", ha="center", va="top", fontsize=10)
    clean(ax, 0.1, 6.4, -0.75, 4.1, eq=False)
    ax.set_aspect("equal")
    save(fig, "t23c")


# ===================================================================
#                    CHƯƠNG II - ĐỀ SỐ 4
# ===================================================================

def t24a():
    """Đồ thị p - 1/V để tuyến tính hoá định luật Boyle."""
    fig, ax = plt.subplots(figsize=(6.9, 4.2))
    invV = np.array([0.20, 0.25, 0.333, 0.50, 1.00])
    p = 3.0 * invV
    ax.plot(invV, p, "o", color=RED, ms=7, zorder=5)
    xx = np.linspace(0, 1.1, 50)
    ax.plot(xx, 3.0 * xx, color=BLUE, lw=2.0)
    ax.set_xlabel("1/V  (L⁻¹)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(0, 1.15); ax.set_ylim(0, 3.6)
    grid(ax)
    save(fig, "t24a")


def t24b():
    """Xi lanh nằm ngang, pit-tông ngăn hai khối khí."""
    fig, ax = plt.subplots(figsize=(7.2, 2.9))
    ax.add_patch(Rectangle((0.6, 0.8), 6.0, 1.5, fc="white", ec="k", lw=2.2))
    ax.add_patch(Rectangle((0.62, 0.82), 2.98, 1.46, fc="#d6eaf8", ec="none"))
    ax.add_patch(Rectangle((3.80, 0.82), 2.78, 1.46, fc="#fdebd0", ec="none"))
    ax.add_patch(Rectangle((3.60, 0.72), 0.20, 1.66, fc="#95a5a6", ec="k", lw=1.5, zorder=4))
    ax.text(2.10, 1.55, "KHÍ A", ha="center", va="center", fontsize=11,
            fontweight="bold", color=BLUE)
    ax.text(5.20, 1.55, "KHÍ B", ha="center", va="center", fontsize=11,
            fontweight="bold", color=ORANGE)
    ax.annotate("pit-tông\nkhông ma sát", xy=(3.70, 0.72), xytext=(3.70, 0.10),
                ha="center", va="top", fontsize=9.6,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    arrow(ax, 0.62, 2.62, 3.58, 2.62, color=GREEN, lw=1.2, ms=10, style="<|-|>")
    ax.text(2.10, 2.72, "ℓ₁", ha="center", va="bottom", fontsize=11.5, color=GREEN)
    arrow(ax, 3.82, 2.62, 6.58, 2.62, color=GREEN, lw=1.2, ms=10, style="<|-|>")
    ax.text(5.20, 2.72, "ℓ₂", ha="center", va="bottom", fontsize=11.5, color=GREEN)
    clean(ax, 0.2, 7.0, -0.55, 3.3, eq=False)
    ax.set_aspect("equal")
    save(fig, "t24b")


def t24c():
    """Đồ thị V - T gồm ba giai đoạn, dùng để nhận dạng quá trình."""
    fig, ax = plt.subplots(figsize=(6.9, 4.2))
    ax.plot([300, 300], [2.0, 4.0], color=BLUE, lw=2.4)
    ax.plot([300, 600], [4.0, 4.0], color=GREEN, lw=2.4)
    ax.plot([600, 300], [4.0, 2.0], color=RED, lw=2.4)
    for x, y, lab, dx, dy in [(300, 2.0, "M", -34, -0.30), (300, 4.0, "N", -34, 0.14),
                              (600, 4.0, "P", 14, 0.14)]:
        ax.plot([x], [y], "o", color="k", ms=6, zorder=5)
        ax.text(x + dx, y + dy, lab, fontsize=12, fontweight="bold")
    ax.set_xlabel("T (K)", fontsize=11)
    ax.set_ylabel("V (lít)", fontsize=11)
    ax.set_xlim(0, 720); ax.set_ylim(0, 5.0)
    ax.set_xticks([0, 300, 600]); ax.set_yticks([0, 2, 4])
    grid(ax)
    save(fig, "t24c")


# ===================================================================
#                    CHƯƠNG II - ĐỀ SỐ 5
# ===================================================================

def t25a():
    """Chu trình bốn giai đoạn trên giản đồ p - V."""
    fig, ax = plt.subplots(figsize=(6.9, 4.3))
    # (1) 1 L, 1 atm -> (2) 1 L, 4 atm -> (3) 4 L, 4 atm -> (4) 4 L, 1 atm -> (1)
    xs = [1, 1, 4, 4, 1]; ys = [1, 4, 4, 1, 1]
    ax.plot(xs, ys, color=BLUE, lw=2.4)
    arrow(ax, 1, 2.3, 1, 2.9, color=BLUE, lw=0, ms=15)
    arrow(ax, 2.3, 4, 2.9, 4, color=BLUE, lw=0, ms=15)
    arrow(ax, 4, 2.7, 4, 2.1, color=BLUE, lw=0, ms=15)
    arrow(ax, 2.7, 1, 2.1, 1, color=BLUE, lw=0, ms=15)
    for x, y, lab, dx, dy in [(1, 1, "(1)", -0.62, -0.05), (1, 4, "(2)", -0.62, 0.10),
                              (4, 4, "(3)", 0.14, 0.16), (4, 1, "(4)", 0.14, -0.05)]:
        ax.plot([x], [y], "o", color=RED, ms=6.5, zorder=5)
        ax.text(x + dx, y + dy, lab, fontsize=11.5, fontweight="bold", color=RED)
    ax.set_xlabel("V (lít)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(0, 5.2); ax.set_ylim(0, 5.0)
    ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3, 4])
    grid(ax)
    save(fig, "t25a")


def t25b():
    """Phân bố tốc độ phân tử ở hai nhiệt độ khác nhau."""
    fig, ax = plt.subplots(figsize=(6.9, 4.1))
    v = np.linspace(0, 2600, 500)

    def maxw(v, a):
        return (v ** 2) * np.exp(-(v ** 2) / (2 * a ** 2)) / a ** 3
    ax.plot(v, maxw(v, 300), color=BLUE, lw=2.4, label="T₁ = 300 K")
    ax.plot(v, maxw(v, 460), color=RED, lw=2.4, label="T₂ = 700 K")
    ax.set_xlabel("Tốc độ phân tử v (m/s)", fontsize=11)
    ax.set_ylabel("Số phân tử ứng với mỗi\nkhoảng tốc độ (đơn vị tuỳ ý)", fontsize=10.2)
    ax.set_xlim(0, 2600); ax.set_ylim(0, None)
    ax.set_yticks([])
    grid(ax)
    ax.legend(loc="upper right", fontsize=10.5, framealpha=0.95)
    save(fig, "t25b")


def t25c():
    """Bóng thám không bay lên cao: thể tích tăng, áp suất và nhiệt độ giảm."""
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    # mặt đất
    ax.add_patch(Rectangle((0.0, 0.0), 7.0, 0.35, fc="#d5dbdb", ec="none"))
    ax.plot([0, 7.0], [0.35, 0.35], color=GREY, lw=1.2)
    # bóng dưới thấp
    ax.add_patch(Ellipse((1.35, 1.25), 0.95, 1.15, fc="#d6eaf8", ec=BLUE, lw=1.8))
    ax.plot([1.35, 1.35], [0.68, 0.35], color=GREY, lw=1.0)
    ax.text(1.35, 2.02, "mặt đất", ha="center", va="bottom", fontsize=9.6)
    ax.text(1.35, 1.25, "V₁", ha="center", va="center", fontsize=12, color=BLUE)
    # bóng trên cao
    ax.add_patch(Ellipse((5.10, 3.05), 1.75, 2.05, fc="#d6eaf8", ec=BLUE, lw=1.8))
    ax.text(5.10, 3.05, "V₂", ha="center", va="center", fontsize=13, color=BLUE)
    ax.text(5.10, 4.28, "độ cao lớn", ha="center", va="bottom", fontsize=9.6)
    arrow(ax, 2.20, 1.65, 4.05, 2.60, color=RED, lw=1.8, ms=13)
    ax.text(3.05, 1.55, "p giảm, T giảm", fontsize=10, color=RED, ha="center", va="top")
    clean(ax, -0.2, 7.2, -0.35, 5.0, eq=False)
    ax.set_aspect("equal")
    save(fig, "t25c")


def t25d():
    """Đồ thị p - V của hai quá trình khác nhau nối cùng hai trạng thái."""
    fig, ax = plt.subplots(figsize=(6.9, 4.2))
    V = np.linspace(1.0, 4.0, 120)
    ax.plot(V, 4.0 / V, color=RED, lw=2.4, label="Quá trình I (đẳng nhiệt)")
    ax.plot([1, 1, 4], [4, 1, 1], color=BLUE, lw=2.4,
            label="Quá trình II (đẳng tích rồi đẳng áp)")
    ax.plot([1, 4], [4, 1], "o", color="k", ms=6.5, zorder=6)
    ax.text(0.75, 4.12, "(1)", fontsize=11.5, fontweight="bold")
    ax.text(4.06, 1.14, "(2)", fontsize=11.5, fontweight="bold")
    ax.set_xlabel("V (lít)", fontsize=11)
    ax.set_ylabel("p (atm)", fontsize=11)
    ax.set_xlim(0, 5.2); ax.set_ylim(0, 5.0)
    ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2, 3, 4])
    grid(ax)
    ax.legend(loc="upper right", fontsize=9.5, framealpha=0.95)
    save(fig, "t25d")


ALL = [t11a, t11b, t11c, t12a, t12b, t12c, t13a, t13b, t13c,
       t14a, t14b, t14c, t15a, t15b, t15c,
       t21a, t21b, t21c, t22a, t22b, t22c, t23a, t23b, t23c,
       t24a, t24b, t24c, t25a, t25b, t25c, t25d]

if __name__ == "__main__":
    print("Đang vẽ hình cho hệ thống đề kiểm tra…")
    for f in ALL:
        f()
    print("Xong: %d hình." % len(ALL))
