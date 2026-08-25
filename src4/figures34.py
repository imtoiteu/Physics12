# -*- coding: utf-8 -*-
"""Hình vẽ gốc cho bộ đề kiểm tra Chương III (Từ trường) và Chương IV (Vật lí hạt nhân).

Quy ước tên: t<chương><số đề><chữ cái>, ví dụ t31a = Chương 3, Đề 1, hình a.
Không hình nào được ghi sẵn kết luận hay đáp án của câu hỏi dùng nó.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (Rectangle, Circle, FancyArrowPatch, Polygon,
                                FancyBboxPatch, Arc, Ellipse, Wedge)

from figures4 import (save, arrow, clean, grid, VN,
                      RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL)


def field_into(ax, xs, ys, size=9, color=BLUE):
    """Kí hiệu × cho từ trường hướng vào trong mặt phẳng hình vẽ."""
    for x in xs:
        for y in ys:
            ax.text(x, y, "×", ha="center", va="center", fontsize=size, color=color)


def field_out(ax, xs, ys, r=0.055, color=BLUE):
    """Kí hiệu • cho từ trường hướng ra ngoài mặt phẳng hình vẽ."""
    for x in xs:
        for y in ys:
            ax.add_patch(Circle((x, y), r, fc=color, ec=color))


def magnet(ax, x, y, w, h, horizontal=True, lw=1.6):
    """Nam châm thẳng: nửa đỏ ghi N, nửa xanh ghi S."""
    if horizontal:
        ax.add_patch(Rectangle((x, y), w / 2, h, fc="#5b8dd6", ec="k", lw=lw))
        ax.add_patch(Rectangle((x + w / 2, y), w / 2, h, fc="#d9534f", ec="k", lw=lw))
        ax.text(x + w * 0.25, y + h / 2, "S", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white")
        ax.text(x + w * 0.75, y + h / 2, "N", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white")
    else:
        ax.add_patch(Rectangle((x, y), w, h / 2, fc="#5b8dd6", ec="k", lw=lw))
        ax.add_patch(Rectangle((x, y + h / 2), w, h / 2, fc="#d9534f", ec="k", lw=lw))
        ax.text(x + w / 2, y + h * 0.25, "S", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white")
        ax.text(x + w / 2, y + h * 0.75, "N", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white")


# ===================================================================
#                    CHƯƠNG III - ĐỀ SỐ 1
# ===================================================================

def t31a():
    """Đường sức từ của một nam châm thẳng."""
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    magnet(ax, -1.1, -0.32, 2.2, 0.64)
    for k in (0.45, 0.95, 1.6, 2.4):
        th = np.linspace(0, 2 * np.pi, 400)
        x = (1.1 + k) * np.cos(th)
        y = k * np.sin(th)
        ax.plot(x, y, color=GREY, lw=1.3, zorder=1)
        # mũi tên: ra ở cực N (bên phải), vào ở cực S (bên trái)
        for t0 in (0.30, np.pi - 0.30, np.pi + 0.30, 2 * np.pi - 0.30):
            xa = (1.1 + k) * np.cos(t0); ya = k * np.sin(t0)
            dx = -(1.1 + k) * np.sin(t0); dy = k * np.cos(t0)
            n = np.hypot(dx, dy)
            arrow(ax, xa, ya, xa + 0.20 * dx / n, ya + 0.20 * dy / n,
                  color=GREY, lw=1.2, ms=10)
    ax.plot([1.1, 3.9], [0, 0], color=GREY, lw=1.3)
    ax.plot([-1.1, -3.9], [0, 0], color=GREY, lw=1.3)
    arrow(ax, 2.4, 0, 2.9, 0, color=GREY, lw=1.2, ms=10)
    arrow(ax, -2.9, 0, -2.4, 0, color=GREY, lw=1.2, ms=10)
    clean(ax, -4.4, 4.4, -2.9, 2.9, eq=False)
    ax.set_aspect("equal")
    save(fig, "t31a")


def t31b():
    """Đoạn dây dẫn mang dòng điện đặt trong từ trường đều hướng vào trang."""
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    field_into(ax, np.linspace(0.5, 5.5, 9), np.linspace(0.5, 3.5, 6))
    ax.plot([0.9, 5.1], [2.0, 2.0], color="k", lw=4.0, zorder=4)
    ax.add_patch(Rectangle((1.6, 1.88), 2.8, 0.24, fc="#c9a227", ec="k",
                           lw=1.4, zorder=5))
    arrow(ax, 2.4, 2.0, 3.6, 2.0, color=RED, lw=0, ms=18)
    ax.text(3.0, 1.55, "I", fontsize=14, color=RED, fontweight="bold", ha="center")
    arrow(ax, 3.0, 2.15, 3.0, 3.45, color=GREEN, lw=2.2, ms=15)
    ax.text(3.22, 3.30, "F", fontsize=14, color=GREEN, fontweight="bold", va="center")
    arrow(ax, 1.6, 2.35, 4.4, 2.35, color=PURPLE, lw=1.2, ms=10, style="<|-|>")
    ax.text(3.0, 2.48, "ℓ", fontsize=13, color=PURPLE, ha="center", va="bottom")
    ax.text(0.35, 3.75, "Từ trường đều B hướng vào trong mặt phẳng hình vẽ",
            fontsize=10, color=BLUE)
    clean(ax, 0.2, 6.0, 0.2, 4.2, eq=False)
    ax.set_aspect("equal")
    save(fig, "t31b")


def t31c():
    """Khung dây phẳng trong từ trường đều, pháp tuyến hợp với B góc α."""
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    for y in np.linspace(0.4, 3.8, 7):
        ax.plot([0.3, 6.3], [y, y], color="#9fc0e8", lw=1.1, zorder=1)
        arrow(ax, 5.3, y, 5.9, y, color="#9fc0e8", lw=1.0, ms=9)
    ax.text(0.35, 4.0, "B", fontsize=13, color=BLUE, fontweight="bold")
    # khung dây nhìn nghiêng (hình bình hành)
    P = [(2.0, 1.1), (3.9, 1.7), (3.9, 3.1), (2.0, 2.5)]
    ax.add_patch(Polygon(P, fc="#fdf1d6", ec="#8a6d1f", lw=2.2, zorder=3))
    ax.text(2.95, 2.10, "S", fontsize=13, fontweight="bold", ha="center",
            va="center", color="#8a6d1f", zorder=4)
    # pháp tuyến
    cx, cy = 2.95, 2.10
    ang = np.deg2rad(35)
    arrow(ax, cx, cy, cx + 1.5 * np.cos(ang), cy + 1.5 * np.sin(ang),
          color=RED, lw=2.0, ms=14)
    ax.text(cx + 1.62 * np.cos(ang), cy + 1.62 * np.sin(ang) + 0.06, "n",
            fontsize=13, color=RED, fontweight="bold")
    arrow(ax, cx, cy, cx + 1.5, cy, color=BLUE, lw=2.0, ms=14)
    ax.add_patch(Arc((cx, cy), 1.5, 1.5, theta1=0, theta2=35, color="k", lw=1.3))
    ax.text(cx + 0.90, cy + 0.20, "α", fontsize=13, fontweight="bold")
    clean(ax, 0.2, 6.6, 0.2, 4.4, eq=False)
    ax.set_aspect("equal")
    save(fig, "t31c")


# ===================================================================
#                    CHƯƠNG III - ĐỀ SỐ 2
# ===================================================================

def t32a():
    """Thí nghiệm Faraday: nam châm chuyển động so với ống dây nối điện kế."""
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    # ống dây
    for k, x in enumerate(np.linspace(2.5, 4.9, 9)):
        ax.add_patch(Ellipse((x, 1.9), 0.30, 1.35, fc="none", ec="#b8860b", lw=2.0))
    ax.text(3.7, 3.00, "ống dây", ha="center", fontsize=10.5)
    # dây nối tới điện kế
    ax.plot([2.5, 1.9, 1.9], [1.24, 1.24, 0.55], color="k", lw=1.5)
    ax.plot([4.9, 5.5, 5.5], [1.24, 1.24, 0.55], color="k", lw=1.5)
    ax.plot([1.9, 3.05], [0.55, 0.55], color="k", lw=1.5)
    ax.plot([4.35, 5.5], [0.55, 0.55], color="k", lw=1.5)
    ax.add_patch(Circle((3.70, 0.55), 0.65, fc="#fdf6e3", ec="k", lw=1.8, zorder=5))
    ax.text(3.70, 0.55, "G", ha="center", va="center", fontsize=13,
            fontweight="bold", zorder=6)
    ax.text(3.70, -0.30, "điện kế", ha="center", va="top", fontsize=10)
    # nam châm
    magnet(ax, 0.15, 1.62, 1.5, 0.56)
    arrow(ax, 1.75, 1.90, 2.30, 1.90, color=RED, lw=2.0, ms=14)
    ax.text(2.02, 2.10, "v", fontsize=13, color=RED, fontweight="bold",
            ha="center", va="bottom")
    clean(ax, -0.2, 6.9, -0.9, 3.5, eq=False)
    ax.set_aspect("equal")
    save(fig, "t32a")


def t32b():
    """Đồ thị từ thông qua một khung dây theo thời gian (gấp khúc ba đoạn)."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    t = [0, 2, 5, 7]
    P = [0, 0.8, 0.8, 0.2]
    ax.plot(t, P, color=BLUE, lw=2.6, marker="o", ms=6.5, mfc="white", mec=BLUE,
            zorder=4)
    for x, y, lab in [(1.0, 0.28, "①"), (3.5, 0.70, "②"), (6.0, 0.40, "③")]:
        ax.text(x, y, lab, fontsize=14, color=RED, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="circle,pad=0.14", fc="white", ec=RED, lw=1.2))
    ax.set_xlabel("Thời gian t (s)", fontsize=11)
    ax.set_ylabel("Từ thông Φ (Wb)", fontsize=11)
    ax.set_xlim(0, 8); ax.set_ylim(0, 1.0)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    grid(ax)
    save(fig, "t32b")


def t32c():
    """Nam châm đưa lại gần một vòng dây kín đặt trên giá."""
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.add_patch(Ellipse((4.3, 1.9), 1.05, 2.45, fc="none", ec="#b8860b", lw=3.0))
    ax.plot([4.3, 4.3], [0.68, 0.15], color=GREY, lw=2.0)
    ax.plot([3.7, 4.9], [0.15, 0.15], color=GREY, lw=2.6)
    ax.text(4.30, 3.35, "vòng dây kín", ha="center", fontsize=10.5)
    magnet(ax, 0.9, 1.62, 1.6, 0.56)
    arrow(ax, 2.65, 1.90, 3.45, 1.90, color=RED, lw=2.2, ms=15)
    ax.text(3.05, 2.12, "v", fontsize=13, color=RED, fontweight="bold",
            ha="center", va="bottom")
    ax.text(1.70, 1.28, "nam châm", ha="center", va="top", fontsize=10)
    clean(ax, 0.4, 6.2, -0.2, 3.7, eq=False)
    ax.set_aspect("equal")
    save(fig, "t32c")


# ===================================================================
#                    CHƯƠNG III - ĐỀ SỐ 3
# ===================================================================

def t33a():
    """Thanh dẫn trượt trên hai thanh ray song song trong từ trường đều."""
    fig, ax = plt.subplots(figsize=(7.0, 3.9))
    field_out(ax, np.linspace(1.4, 5.6, 8), np.linspace(0.9, 2.9, 4))
    ax.plot([0.9, 6.0], [0.7, 0.7], color="k", lw=2.6)
    ax.plot([0.9, 6.0], [3.1, 3.1], color="k", lw=2.6)
    ax.plot([0.9, 0.9], [0.7, 3.1], color="k", lw=2.6)
    ax.add_patch(Rectangle((0.62, 1.55), 0.56, 0.70, fc="#e8e8e8", ec="k", lw=1.6,
                           zorder=5))
    ax.text(0.90, 1.90, "R", ha="center", va="center", fontsize=12,
            fontweight="bold", zorder=6)
    ax.plot([3.9, 3.9], [0.55, 3.25], color="#8a6d1f", lw=5.0, zorder=4)
    ax.text(3.90, 3.42, "M", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.text(3.90, 0.38, "N", ha="center", va="top", fontsize=12, fontweight="bold")
    arrow(ax, 4.05, 1.90, 5.15, 1.90, color=RED, lw=2.2, ms=15)
    ax.text(4.60, 2.10, "v", fontsize=13, color=RED, fontweight="bold",
            ha="center", va="bottom")
    arrow(ax, 6.35, 0.7, 6.35, 3.1, color=PURPLE, lw=1.2, ms=10, style="<|-|>")
    ax.text(6.50, 1.90, "ℓ", fontsize=13, color=PURPLE, va="center")
    ax.text(3.50, 4.10, "Từ trường đều B hướng ra ngoài mặt phẳng hình vẽ",
            fontsize=10, color=BLUE, ha="center")
    clean(ax, 0.2, 7.1, 0.1, 4.5, eq=False)
    ax.set_aspect("equal")
    save(fig, "t33a")


def t33b():
    """Đồ thị cường độ dòng điện xoay chiều theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    t = np.linspace(0, 0.05, 800)
    ax.plot(t * 1000, 4.0 * np.cos(100 * np.pi * t), color=RED, lw=2.4)
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel("Thời gian t (ms)", fontsize=11)
    ax.set_ylabel("Cường độ dòng điện i (A)", fontsize=11)
    ax.set_xlim(0, 52); ax.set_ylim(-5.2, 5.2)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    ax.set_yticks([-4, -2, 0, 2, 4])
    grid(ax)
    save(fig, "t33b")


def t33c():
    """Sơ đồ nguyên tắc của máy phát điện xoay chiều một pha."""
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    ax.add_patch(Rectangle((0.5, 1.55), 0.85, 2.60, fc="#d9534f", ec="k", lw=1.6))
    ax.text(0.92, 2.85, "N", ha="center", va="center", fontsize=15,
            fontweight="bold", color="white")
    ax.add_patch(Rectangle((4.65, 1.55), 0.85, 2.60, fc="#5b8dd6", ec="k", lw=1.6))
    ax.text(5.07, 2.85, "S", ha="center", va="center", fontsize=15,
            fontweight="bold", color="white")
    for y in np.linspace(1.80, 3.90, 6):
        ax.plot([1.40, 4.60], [y, y], color="#9fc0e8", lw=1.0, zorder=1)
        arrow(ax, 3.95, y, 4.45, y, color="#9fc0e8", lw=1.0, ms=9)
    ax.add_patch(Polygon([(2.20, 2.20), (3.80, 2.60), (3.80, 3.60), (2.20, 3.20)],
                         fc="none", ec="#b8860b", lw=2.6, zorder=4))
    ax.text(3.00, 4.30, "khung dây quay", ha="center", fontsize=10.5)
    ax.add_patch(Arc((3.00, 2.90), 1.05, 1.05, theta1=205, theta2=335,
                     color=RED, lw=1.6, zorder=5))
    arrow(ax, 3.48, 2.76, 3.52, 2.94, color=RED, lw=0, ms=13)
    # hai đầu khung đi xuống hai vành khuyên
    ax.plot([2.55, 2.55], [2.30, 1.05], color="k", lw=1.5, zorder=5)
    ax.plot([3.45, 3.45], [2.48, 1.05], color="k", lw=1.5, zorder=5)
    for x in (2.55, 3.45):
        ax.add_patch(Ellipse((x, 0.92), 0.46, 0.26, fc="#cfcfcf", ec="k",
                             lw=1.3, zorder=6))
    ax.annotate("hai vành khuyên\nvà chổi quét", xy=(2.55, 0.92), xytext=(0.30, 0.92),
                fontsize=9.5, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    ax.plot([2.32, 1.55, 1.55], [0.92, 0.92, 0.12], color="k", lw=1.5)
    ax.plot([3.68, 4.45, 4.45], [0.92, 0.92, 0.12], color="k", lw=1.5)
    ax.plot([1.55, 2.45], [0.12, 0.12], color="k", lw=1.5)
    ax.plot([3.55, 4.45], [0.12, 0.12], color="k", lw=1.5)
    ax.add_patch(Rectangle((2.45, -0.10), 1.10, 0.44, fc="#e8e8e8", ec="k", lw=1.5))
    ax.text(3.00, 0.12, "R", ha="center", va="center", fontsize=12,
            fontweight="bold")
    clean(ax, -0.9, 6.0, -0.6, 4.7, eq=False)
    ax.set_aspect("equal")
    save(fig, "t33c")


# ===================================================================
#                    CHƯƠNG III - ĐỀ SỐ 4
# ===================================================================

def t34a():
    """Sơ đồ máy biến áp lí tưởng."""
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.add_patch(Rectangle((1.9, 0.6), 2.6, 2.9, fc="#dfe3e6", ec="k", lw=2.0))
    ax.add_patch(Rectangle((2.5, 1.2), 1.4, 1.7, fc="white", ec="k", lw=2.0))
    ax.text(3.20, 3.70, "lõi thép", ha="center", fontsize=10)
    for y in np.linspace(1.0, 3.1, 7):
        ax.add_patch(Ellipse((2.20, y), 0.62, 0.24, fc="none", ec="#b8860b", lw=2.0))
    for y in np.linspace(1.0, 3.1, 11):
        ax.add_patch(Ellipse((4.20, y), 0.62, 0.16, fc="none", ec="#b8860b", lw=1.8))
    ax.text(1.10, 3.42, "N₁", fontsize=13, fontweight="bold", color="#8a6d1f")
    ax.text(5.05, 3.42, "N₂", fontsize=13, fontweight="bold", color="#8a6d1f")
    ax.plot([1.89, 0.85, 0.85], [1.0, 1.0, 3.1], color="k", lw=1.5)
    ax.plot([1.89, 0.85], [3.1, 3.1], color="k", lw=1.5)
    ax.text(0.55, 2.05, "U₁", fontsize=13, fontweight="bold", ha="right", va="center")
    ax.plot([4.51, 5.55, 5.55], [1.0, 1.0, 3.1], color="k", lw=1.5)
    ax.plot([4.51, 5.55], [3.1, 3.1], color="k", lw=1.5)
    ax.text(5.85, 2.05, "U₂", fontsize=13, fontweight="bold", va="center")
    clean(ax, 0.1, 6.5, 0.2, 4.0, eq=False)
    ax.set_aspect("equal")
    save(fig, "t34a")


def t34b():
    """Đồ thị từ thông và suất điện động cảm ứng của khung dây quay đều."""
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    t = np.linspace(0, 0.04, 600)
    ax.plot(t * 1000, np.cos(100 * np.pi * t), color=BLUE, lw=2.4,
            label="Φ (đơn vị tuỳ ý)")
    ax.plot(t * 1000, np.sin(100 * np.pi * t), color=RED, lw=2.4, ls="--",
            label="e (đơn vị tuỳ ý)")
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel("Thời gian t (ms)", fontsize=11)
    ax.set_xlim(0, 42); ax.set_ylim(-1.45, 1.75)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40])
    ax.set_yticks([-1, 0, 1])
    grid(ax)
    ax.legend(loc="upper right", fontsize=10, ncol=2, framealpha=0.95)
    save(fig, "t34b")


def t34c():
    """Sơ đồ truyền tải điện năng đi xa."""
    fig, ax = plt.subplots(figsize=(7.6, 3.2))
    ax.add_patch(FancyBboxPatch((0.2, 1.0), 1.25, 1.05, boxstyle="round,pad=0.05",
                                fc="#fdf6e3", ec="k", lw=1.6))
    ax.text(0.82, 1.52, "NHÀ MÁY\nĐIỆN", ha="center", va="center", fontsize=9.5,
            fontweight="bold")
    ax.add_patch(Rectangle((1.95, 1.05), 0.85, 0.95, fc="#dfe3e6", ec="k", lw=1.6))
    ax.text(2.38, 1.52, "TĂNG\nÁP", ha="center", va="center", fontsize=9)
    ax.add_patch(Rectangle((5.05, 1.05), 0.85, 0.95, fc="#dfe3e6", ec="k", lw=1.6))
    ax.text(5.48, 1.52, "HẠ\nÁP", ha="center", va="center", fontsize=9)
    ax.add_patch(FancyBboxPatch((6.40, 1.0), 1.25, 1.05, boxstyle="round,pad=0.05",
                                fc="#eafaf1", ec="k", lw=1.6))
    ax.text(7.02, 1.52, "NƠI\nTIÊU THỤ", ha="center", va="center", fontsize=9.5,
            fontweight="bold")
    for x0, x1 in [(1.45, 1.95), (2.80, 5.05), (5.90, 6.40)]:
        ax.plot([x0, x1], [1.72, 1.72], color="k", lw=1.4)
        ax.plot([x0, x1], [1.30, 1.30], color="k", lw=1.4)
    ax.add_patch(Rectangle((3.55, 1.60), 0.72, 0.24, fc="#f5b7b1", ec="k", lw=1.3))
    ax.text(3.91, 2.00, "R (điện trở đường dây)", ha="center", va="bottom",
            fontsize=9.5, color=RED)
    for x in (3.30, 4.55):
        ax.plot([x, x], [0.55, 1.30], color=GREY, lw=1.6)
        ax.plot([x - 0.22, x + 0.22], [1.15, 1.15], color=GREY, lw=1.4)
    clean(ax, 0.0, 7.9, 0.3, 2.6, eq=False)
    ax.set_aspect("equal")
    save(fig, "t34c")


# ===================================================================
#                    CHƯƠNG III - ĐỀ SỐ 5
# ===================================================================

def t35a():
    """Đồ thị từ thông dạng tam giác tuần hoàn qua một khung dây."""
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    t = [0, 2, 6, 10, 14]
    P = [0, 0.6, -0.6, 0.6, -0.6]
    ax.plot(t, P, color=BLUE, lw=2.6, marker="o", ms=5.5, mfc="white", mec=BLUE,
            zorder=4)
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel("Thời gian t (s)", fontsize=11)
    ax.set_ylabel("Từ thông Φ (Wb)", fontsize=11)
    ax.set_xlim(0, 15); ax.set_ylim(-0.9, 0.9)
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
    ax.set_yticks([-0.6, -0.3, 0, 0.3, 0.6])
    grid(ax)
    save(fig, "t35a")


def t35b():
    """Ba ứng dụng của hiện tượng cảm ứng điện từ."""
    fig, axs = plt.subplots(1, 3, figsize=(9.4, 3.0))
    # (a) bếp từ
    ax = axs[0]
    ax.add_patch(Rectangle((0.4, 0.4), 3.2, 0.75, fc="#4a4a4a", ec="k", lw=1.6))
    ax.add_patch(Rectangle((0.4, 1.15), 3.2, 0.14, fc="#2c3e50", ec="k", lw=1.2))
    for x in np.linspace(1.0, 3.0, 5):
        ax.add_patch(Ellipse((x, 0.78), 0.30, 0.40, fc="none", ec="#b8860b", lw=1.6))
    ax.add_patch(Rectangle((1.0, 1.29), 2.0, 0.62, fc="#c9ccd1", ec="k", lw=1.6))
    ax.text(2.0, 2.15, "(a)", ha="center", fontsize=12, fontweight="bold", color=BLUE)
    clean(ax, 0.0, 4.0, 0.0, 2.6)
    # (b) sạc không dây
    ax = axs[1]
    ax.add_patch(Rectangle((0.6, 0.4), 2.8, 0.55, fc="#dfe3e6", ec="k", lw=1.6))
    for x in np.linspace(1.2, 2.8, 4):
        ax.add_patch(Ellipse((x, 0.67), 0.28, 0.30, fc="none", ec="#b8860b", lw=1.5))
    ax.add_patch(FancyBboxPatch((1.1, 1.15), 1.8, 1.0, boxstyle="round,pad=0.06",
                                fc="#2c3e50", ec="k", lw=1.6))
    for x in np.linspace(1.5, 2.5, 3):
        ax.add_patch(Ellipse((x, 1.42), 0.26, 0.26, fc="none", ec="#b8860b", lw=1.4))
    ax.text(2.0, 2.35, "(b)", ha="center", fontsize=12, fontweight="bold", color=BLUE)
    clean(ax, 0.0, 4.0, 0.0, 2.8)
    # (c) đèn pin lắc tay
    ax = axs[2]
    ax.add_patch(FancyBboxPatch((0.5, 0.9), 3.0, 0.85, boxstyle="round,pad=0.06",
                                fc="#f2f4f6", ec="k", lw=1.7))
    for x in np.linspace(1.5, 2.4, 4):
        ax.add_patch(Ellipse((x, 1.32), 0.24, 0.62, fc="none", ec="#b8860b", lw=1.6))
    ax.add_patch(Rectangle((0.85, 1.16), 0.45, 0.32, fc="#95a5a6", ec="k", lw=1.3))
    arrow(ax, 0.90, 2.05, 3.05, 2.05, color=RED, lw=1.6, ms=12, style="<|-|>")
    ax.add_patch(Wedge((3.50, 1.32), 0.42, -55, 55, fc="#f9e79f", ec="k", lw=1.3))
    ax.text(2.0, 2.55, "(c)", ha="center", fontsize=12, fontweight="bold", color=BLUE)
    clean(ax, 0.0, 4.3, 0.0, 3.0)
    save(fig, "t35b")


def t35c():
    """Bốn vị trí của khung dây quay đều trong từ trường đều (nhìn từ cạnh)."""
    fig, axs = plt.subplots(1, 4, figsize=(9.8, 3.1))
    angles = [0, 90, 180, 270]
    for k, (ax, a) in enumerate(zip(axs, angles)):
        for y in np.linspace(-1.5, 1.5, 5):
            ax.plot([-1.95, 1.95], [y, y], color="#9fc0e8", lw=0.9, zorder=1)
            arrow(ax, 1.40, y, 1.80, y, color="#9fc0e8", lw=0.9, ms=8)
        th = np.deg2rad(a)
        # mặt phẳng khung nhìn từ cạnh: vuông góc với pháp tuyến
        px, py = -np.sin(th), np.cos(th)
        ax.plot([-1.10 * px, 1.10 * px], [-1.10 * py, 1.10 * py],
                color="#8a6d1f", lw=5.0, zorder=4)
        arrow(ax, 0, 0, 1.25 * np.cos(th), 1.25 * np.sin(th),
              color=RED, lw=2.0, ms=14)
        ax.text(1.40 * np.cos(th) + 0.10, 1.40 * np.sin(th), "n", fontsize=12,
                color=RED, fontweight="bold", ha="center", va="center")
        ax.add_patch(Circle((0, 0), 0.10, fc="k", ec="k", zorder=6))
        ax.text(0, -2.35, ["(1)", "(2)", "(3)", "(4)"][k], ha="center",
                fontsize=12.5, fontweight="bold", color=BLUE)
        if k == 0:
            ax.text(-1.90, 1.95, "B", fontsize=12, color=BLUE, fontweight="bold")
        clean(ax, -2.2, 2.2, -2.9, 2.2)
    save(fig, "t35c")


# ===================================================================
#                    CHƯƠNG IV - ĐỀ SỐ 1
# ===================================================================

def t41a():
    """Mô hình cấu tạo của một hạt nhân và nguyên tử."""
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    rng = np.random.RandomState(5)
    pts = []
    while len(pts) < 7:
        q = (rng.uniform(-0.45, 0.45), rng.uniform(-0.45, 0.45))
        if all((q[0] - a) ** 2 + (q[1] - b) ** 2 > 0.30 ** 2 for a, b in pts):
            pts.append(q)
    for k, (x, y) in enumerate(pts):
        pro = k < 3
        ax.add_patch(Circle((x, y), 0.19, fc="#e6605c" if pro else "#9aa4ad",
                            ec="k", lw=1.0, zorder=4))
        ax.text(x, y, "+" if pro else "", ha="center", va="center",
                fontsize=11, color="white", zorder=5)
    ax.add_patch(Circle((0, 0), 0.78, fc="none", ec=GREY, lw=1.2, ls=":"))
    for r, n in ((1.55, 2), (2.35, 1)):
        ax.add_patch(Ellipse((0, 0), 2 * r, 2 * r, fc="none", ec="#b0b7bd", lw=1.1))
        for j in range(n):
            a = np.pi / 3 + j * 2 * np.pi / max(n, 1)
            ax.add_patch(Circle((r * np.cos(a), r * np.sin(a)), 0.12,
                                fc="#4a90d9", ec="k", lw=0.9, zorder=4))
    ax.annotate("proton", xy=pts[0], xytext=(2.05, 1.35), fontsize=10.5,
                color="#c0392b", arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    ax.annotate("neutron", xy=pts[5], xytext=(2.05, -1.35), fontsize=10.5,
                color="#5d6d7e", arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    ax.annotate("electron", xy=(1.55 * np.cos(np.pi / 3), 1.55 * np.sin(np.pi / 3)),
                xytext=(-3.35, 1.85), fontsize=10.5, color="#2471a3",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    ax.annotate("hạt nhân", xy=(-0.55, -0.55), xytext=(-3.35, -1.85), fontsize=10.5,
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    clean(ax, -3.6, 3.6, -2.7, 2.7)
    save(fig, "t41a")


def t41b():
    """Thí nghiệm tán xạ hạt alpha của Rutherford."""
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.add_patch(Rectangle((3.30, 0.30), 0.13, 3.1, fc="#d4af37", ec="k", lw=1.2))
    ax.text(3.36, 3.55, "lá vàng mỏng", ha="center", fontsize=10, color="#8a6d1f")
    ax.add_patch(Rectangle((0.25, 1.55), 0.95, 0.7, fc="#5d6d7e", ec="k", lw=1.5))
    ax.text(0.72, 1.90, "α", ha="center", va="center", fontsize=13,
            fontweight="bold", color="white")
    ax.text(0.72, 1.30, "nguồn", ha="center", va="top", fontsize=10)
    for y in (1.72, 1.90, 2.08):
        ax.plot([1.25, 3.30], [y, y], color=GREEN, lw=1.4)
        ax.plot([3.43, 6.10], [y, y], color=GREEN, lw=1.4)
        arrow(ax, 5.40, y, 5.85, y, color=GREEN, lw=0, ms=11)
    ax.plot([1.25, 3.36], [2.26, 2.26], color=GREEN, lw=1.4)
    ax.plot([3.36, 5.60], [2.26, 3.15], color=ORANGE, lw=1.6)
    arrow(ax, 5.10, 2.95, 5.50, 3.11, color=ORANGE, lw=0, ms=11)
    ax.plot([1.25, 3.36], [1.54, 1.54], color=GREEN, lw=1.4)
    ax.plot([3.36, 5.20], [1.54, 0.55], color=ORANGE, lw=1.6)
    arrow(ax, 4.75, 0.79, 5.12, 0.59, color=ORANGE, lw=0, ms=11)
    ax.plot([1.25, 3.30], [1.36, 1.36], color=GREEN, lw=1.4)
    ax.plot([3.30, 1.60], [1.36, 0.62], color=RED, lw=1.8)
    arrow(ax, 2.05, 0.82, 1.66, 0.65, color=RED, lw=0, ms=12)
    th = np.linspace(-1.15, 1.15, 60)
    ax.plot(6.35 + 0.55 * np.cos(th), 1.90 + 2.05 * np.sin(th), color=PURPLE, lw=2.2)
    ax.text(6.72, 1.90, "màn\nhuỳnh quang", fontsize=9.8, va="center", color=PURPLE)
    clean(ax, 0.1, 8.4, 0.2, 3.9, eq=False)
    ax.set_aspect("equal")
    save(fig, "t41b")


def t41c():
    """Đồ thị năng lượng liên kết riêng theo số khối."""
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    A = np.array([2, 4, 6, 9, 12, 16, 20, 27, 40, 56, 75, 100, 130, 160, 190, 209, 238])
    eps = np.array([1.11, 7.07, 5.33, 6.46, 7.68, 7.98, 8.03, 8.33, 8.55, 8.79,
                    8.70, 8.50, 8.35, 8.15, 7.95, 7.87, 7.57])
    ax.plot(A, eps, color=BLUE, lw=2.0, marker="o", ms=4.5, mfc="white", mec=BLUE)
    ax.plot([56], [8.79], "o", color=RED, ms=8, zorder=5)
    ax.set_xlabel("Số khối A", fontsize=11)
    ax.set_ylabel("Năng lượng liên kết riêng ε (MeV/nucleon)", fontsize=10.5)
    ax.set_xlim(0, 250); ax.set_ylim(0, 9.6)
    ax.set_xticks([0, 50, 100, 150, 200, 250])
    ax.set_yticks([0, 2, 4, 6, 8])
    grid(ax)
    save(fig, "t41c")


# ===================================================================
#                    CHƯƠNG IV - ĐỀ SỐ 2
# ===================================================================

def t42a():
    """Khả năng đâm xuyên của ba loại tia phóng xạ."""
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.add_patch(Rectangle((0.2, 1.15), 0.85, 1.5, fc="#5d6d7e", ec="k", lw=1.5))
    ax.text(0.62, 1.90, "nguồn", ha="center", va="center", fontsize=9.5,
            color="white", rotation=90)
    walls = [(2.35, "#f5deb3", "tờ giấy", 0.10),
             (4.10, "#c9ccd1", "tấm nhôm\nvài mm", 0.26),
             (5.85, "#7f8c8d", "khối chì\nvài cm", 0.55)]
    for x, c, lab, w in walls:
        ax.add_patch(Rectangle((x, 0.55), w, 2.7, fc=c, ec="k", lw=1.4))
        ax.text(x + w / 2, 3.42, lab, ha="center", va="bottom", fontsize=9.5)
    ax.plot([1.05, 2.35], [2.42, 2.42], color=RED, lw=2.4)
    ax.text(1.68, 2.60, "α", fontsize=13, color=RED, fontweight="bold", ha="center")
    ax.plot([1.05, 4.10], [1.90, 1.90], color=GREEN, lw=2.4)
    ax.text(1.68, 2.06, "β", fontsize=13, color=GREEN, fontweight="bold", ha="center")
    ax.plot([1.05, 7.05], [1.38, 1.38], color=PURPLE, lw=2.4)
    ax.text(1.68, 1.54, "γ", fontsize=13, color=PURPLE, fontweight="bold", ha="center")
    arrow(ax, 6.70, 1.38, 7.15, 1.38, color=PURPLE, lw=0, ms=13)
    clean(ax, 0.0, 7.8, 0.3, 4.1, eq=False)
    ax.set_aspect("equal")
    save(fig, "t42a")


def t42d():
    """Ba chùm tia phóng xạ đi vào một điện trường đều giữa hai bản kim loại."""
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ax.add_patch(Rectangle((2.10, 3.35), 4.30, 0.20, fc="#f5b7b1", ec="k", lw=1.5))
    ax.add_patch(Rectangle((2.10, 0.45), 4.30, 0.20, fc="#aed6f1", ec="k", lw=1.5))
    ax.text(1.90, 3.45, "+", fontsize=20, color=RED, ha="right", va="center")
    ax.text(1.90, 0.55, "−", fontsize=20, color=BLUE, ha="right", va="center")
    # nguồn có màn chắn tạo chùm hẹp
    ax.add_patch(Rectangle((0.15, 1.55), 0.85, 0.90, fc="#5d6d7e", ec="k", lw=1.5))
    ax.text(0.57, 2.00, "nguồn", ha="center", va="center", fontsize=9,
            color="white", rotation=90)
    ax.plot([1.05, 2.10], [2.00, 2.00], color=GREY, lw=1.4)
    # (1) lệch nhẹ xuống dưới ; (2) đi thẳng ; (3) lệch mạnh lên trên
    x = np.linspace(2.10, 6.40, 120)
    u = (x - 2.10) / 4.30
    for yend, lab, col, ly in ((2.00 - 0.75, "(1)", RED, -0.10),
                               (2.00, "(2)", PURPLE, 0.16),
                               (2.00 + 1.15, "(3)", GREEN, 0.14)):
        y = 2.00 + (yend - 2.00) * u ** 2
        ax.plot(x, y, color=col, lw=2.2)
        arrow(ax, x[-6], y[-6], x[-1], y[-1], color=col, lw=0, ms=13)
        ax.text(6.60, y[-1] + ly, lab, fontsize=12.5, fontweight="bold", color=col,
                va="center")
    ax.text(4.25, 4.00, "Ba chùm tia phóng xạ đi vào vùng có điện trường đều",
            ha="center", fontsize=10)
    clean(ax, -0.1, 7.4, 0.0, 4.4, eq=False)
    ax.set_aspect("equal")
    save(fig, "t42d")


def t42b():
    """Đồ thị số hạt nhân còn lại của một mẫu phóng xạ theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    t = np.linspace(0, 24, 400)
    ax.plot(t, 100 * 0.5 ** (t / 6.0), color=BLUE, lw=2.5)
    for k in (1, 2, 3):
        x = 6.0 * k; y = 100 * 0.5 ** k
        ax.plot([0, x], [y, y], color=GREY, lw=0.9, ls=":")
        ax.plot([x, x], [0, y], color=GREY, lw=0.9, ls=":")
        ax.plot([x], [y], "o", color=RED, ms=6.5, zorder=5)
    ax.set_xlabel("Thời gian t (ngày)", fontsize=11)
    ax.set_ylabel("Phần trăm số hạt nhân còn lại (%)", fontsize=10.5)
    ax.set_xlim(0, 25); ax.set_ylim(0, 105)
    ax.set_xticks([0, 3, 6, 9, 12, 15, 18, 21, 24])
    ax.set_yticks([0, 12.5, 25, 50, 75, 100])
    grid(ax)
    save(fig, "t42b")


def t42c():
    """Sơ đồ vị trí các hạt nhân trên giản đồ N - Z."""
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    Z = np.linspace(0, 92, 200)
    ax.plot(Z, Z, color=GREY, lw=1.2, ls="--")
    ax.annotate("đường N = Z", xy=(76, 76), xytext=(80, 55), fontsize=10.5,
                color=GREY, ha="center", va="top",
                arrowprops=dict(arrowstyle="-", lw=1.0, color=GREY))
    N = Z + 0.0085 * Z ** 2
    ax.plot(Z, N, color=BLUE, lw=2.6)
    ax.text(56, 128, "dải bền vững", fontsize=10.5, color=BLUE)
    for z, n, lab, c, dx, dy in [(30, 50, "X", RED, -5.5, 4),
                                 (55, 55, "Y", GREEN, -5.5, 4)]:
        ax.plot([z], [n], "o", color=c, ms=9, zorder=5)
        ax.text(z + dx, n + dy, lab, fontsize=13, fontweight="bold", color=c)
    ax.set_xlabel("Số proton Z", fontsize=11)
    ax.set_ylabel("Số neutron N", fontsize=11)
    ax.set_xlim(0, 100); ax.set_ylim(0, 155)
    grid(ax)
    save(fig, "t42c")


# ===================================================================
#                    CHƯƠNG IV - ĐỀ SỐ 3
# ===================================================================

def t43a():
    """Đồ thị bán logarit ln H theo thời gian của một mẫu phóng xạ."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    t = np.array([0, 2, 4, 6, 8, 10])
    y = 9.20 - 0.1733 * t
    ax.plot(t, y, "o", color=RED, ms=7, zorder=5)
    tt = np.linspace(-0.4, 11, 50)
    ax.plot(tt, 9.20 - 0.1733 * tt, color=BLUE, lw=1.8)
    ax.set_xlabel("Thời gian t (giờ)", fontsize=11)
    ax.set_ylabel("ln H   (H tính theo Bq)", fontsize=11)
    ax.set_xlim(0, 11.5); ax.set_ylim(7.0, 9.8)
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_yticks([7.0, 7.5, 8.0, 8.5, 9.0, 9.5])
    grid(ax)
    save(fig, "t43a")


def t43b():
    """Sơ đồ phản ứng phân hạch dây chuyền."""
    fig, ax = plt.subplots(figsize=(7.4, 4.0))

    def nucleus(x, y, r, lab, c="#f0b27a"):
        ax.add_patch(Circle((x, y), r, fc=c, ec="k", lw=1.3, zorder=4))
        ax.text(x, y, lab, ha="center", va="center", fontsize=9.5,
                fontweight="bold", zorder=5)

    def neutron(x, y):
        ax.add_patch(Circle((x, y), 0.11, fc="#95a5a6", ec="k", lw=0.9, zorder=6))

    # thế hệ 0: một neutron bắn vào một hạt nhân U
    neutron(0.30, 2.20)
    arrow(ax, 0.45, 2.20, 0.92, 2.20, color=GREY, lw=1.2, ms=10)
    nucleus(1.30, 2.20, 0.36, "U")
    # thế hệ 1: hai neutron bay ra, mỗi neutron gặp một hạt nhân U mới
    gen1 = [3.35, 1.05]
    for y in gen1:
        arrow(ax, 1.68, 2.20 + 0.25 * np.sign(y - 2.20), 2.32, y,
              color=BLUE, lw=1.2, ms=11)
        neutron(2.10, (2.20 + y) / 2)
        nucleus(2.70, y, 0.34, "U")
    # thế hệ 2: mỗi hạt nhân lại sinh hai neutron
    gen2 = {3.35: [3.95, 2.75], 1.05: [1.65, 0.45]}
    for y, ys in gen2.items():
        for y2 in ys:
            arrow(ax, 3.06, y + 0.22 * np.sign(y2 - y), 3.72, y2,
                  color=BLUE, lw=1.1, ms=10)
            neutron(3.45, (y + y2) / 2)
            nucleus(4.08, y2, 0.32, "U")
            for dy in (0.34, -0.34):
                arrow(ax, 4.42, y2 + 0.16 * np.sign(dy), 4.98, y2 + dy,
                      color=BLUE, lw=1.0, ms=9)
    ax.text(2.60, 4.55, "mỗi lần phân hạch giải phóng thêm neutron",
            ha="center", fontsize=10, color=RED)
    ax.add_patch(Circle((5.75, 3.95), 0.11, fc="#95a5a6", ec="k", lw=0.9))
    ax.text(6.05, 3.95, "neutron", fontsize=9.5, va="center")
    ax.add_patch(Circle((5.75, 3.45), 0.20, fc="#f0b27a", ec="k", lw=1.1))
    ax.text(6.05, 3.45, "hạt nhân U-235", fontsize=9.5, va="center")
    clean(ax, 0.0, 7.9, 0.0, 4.9, eq=False)
    ax.set_aspect("equal")
    save(fig, "t43b")


def t43c():
    """Đồ thị khối lượng chất phóng xạ còn lại theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    t = np.linspace(0, 40, 400)
    ax.plot(t, 80 * 0.5 ** (t / 8.0), color=GREEN, lw=2.5)
    ax.plot([8, 16, 24], [40, 20, 10], "o", color=RED, ms=6.5, zorder=5)
    for x, y in ((8, 40), (16, 20), (24, 10)):
        ax.plot([0, x], [y, y], color=GREY, lw=0.8, ls=":")
        ax.plot([x, x], [0, y], color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("Thời gian t (ngày)", fontsize=11)
    ax.set_ylabel("Khối lượng chất phóng xạ còn lại (g)", fontsize=10.5)
    ax.set_xlim(0, 42); ax.set_ylim(0, 88)
    ax.set_xticks([0, 8, 16, 24, 32, 40])
    ax.set_yticks([0, 10, 20, 40, 60, 80])
    grid(ax)
    save(fig, "t43c")


# ===================================================================
#                    CHƯƠNG IV - ĐỀ SỐ 4
# ===================================================================

def t44a():
    """Sơ đồ nguyên lí của nhà máy điện hạt nhân."""
    fig, ax = plt.subplots(figsize=(7.8, 3.3))
    boxes = [(0.15, "LÒ PHẢN ỨNG\nhạt nhân", "#f5b7b1"),
             (2.05, "BỘ SINH HƠI", "#fdebd0"),
             (3.95, "TUA BIN\nhơi nước", "#d6eaf8"),
             (5.85, "MÁY PHÁT\nĐIỆN", "#d5f5e3")]
    for x, lab, c in boxes:
        ax.add_patch(FancyBboxPatch((x, 0.85), 1.55, 1.25,
                                    boxstyle="round,pad=0.05", fc=c, ec="k", lw=1.6))
        ax.text(x + 0.78, 1.48, lab, ha="center", va="center", fontsize=9,
                fontweight="bold")
    for x in (1.70, 3.60, 5.50):
        arrow(ax, x, 1.48, x + 0.35, 1.48, color="k", lw=1.6, ms=13)
    arrow(ax, 7.40, 1.48, 7.85, 1.48, color=GREEN, lw=1.8, ms=13)
    ax.text(7.95, 1.48, "điện\nnăng", fontsize=9.5, va="center", color=GREEN)
    ax.text(0.93, 0.62, "nhiệt", ha="center", va="top", fontsize=9, color=RED)
    ax.text(2.83, 0.62, "hơi nước", ha="center", va="top", fontsize=9, color=BLUE)
    ax.text(4.73, 0.62, "cơ năng", ha="center", va="top", fontsize=9, color=GREY)
    clean(ax, 0.0, 9.0, 0.0, 2.5, eq=False)
    ax.set_aspect("equal")
    save(fig, "t44a")


def t44b():
    """Phản ứng nhiệt hạch deuterium - tritium."""
    fig, ax = plt.subplots(figsize=(7.2, 3.3))

    def nu(x, y, r, lab, c):
        ax.add_patch(Circle((x, y), r, fc=c, ec="k", lw=1.4, zorder=4))
        ax.text(x, y, lab, ha="center", va="center", fontsize=10,
                fontweight="bold", zorder=5)

    nu(0.75, 2.25, 0.42, "D", "#7fb3d5")
    nu(0.75, 0.85, 0.42, "T", "#a3e4d7")
    arrow(ax, 1.30, 2.10, 2.15, 1.75, color=GREY, lw=1.4, ms=12)
    arrow(ax, 1.30, 1.00, 2.15, 1.35, color=GREY, lw=1.4, ms=12)
    ax.add_patch(Circle((2.75, 1.55), 0.50, fc="#f9e79f", ec=ORANGE, lw=1.8,
                        ls="--", zorder=3))
    arrow(ax, 3.35, 1.55, 4.10, 1.55, color="k", lw=1.6, ms=13)
    nu(4.70, 1.90, 0.46, "He", "#f5b7b1")
    nu(4.70, 0.70, 0.24, "n", "#95a5a6")
    for a in np.linspace(0.4, 2.2, 5):
        arrow(ax, 5.35 + 0.05, 1.55 + 0.0, 5.95 + 0.35 * np.cos(a),
              1.55 + 0.9 * np.sin(a), color=ORANGE, lw=1.2, ms=10)
    ax.text(6.55, 1.55, "năng lượng\ntoả ra", fontsize=10, va="center", color=ORANGE)
    clean(ax, 0.1, 8.0, 0.1, 3.0, eq=False)
    ax.set_aspect("equal")
    save(fig, "t44b")


def t44c():
    """Đồ thị độ phóng xạ của hai mẫu chất khác nhau theo thời gian."""
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    t = np.linspace(0, 30, 400)
    ax.plot(t, 800 * 0.5 ** (t / 5.0), color=RED, lw=2.4, label="Mẫu X")
    ax.plot(t, 400 * 0.5 ** (t / 15.0), color=BLUE, lw=2.4, label="Mẫu Y")
    ax.set_xlabel("Thời gian t (giờ)", fontsize=11)
    ax.set_ylabel("Độ phóng xạ H (Bq)", fontsize=11)
    ax.set_xlim(0, 31); ax.set_ylim(0, 880)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_yticks([0, 200, 400, 600, 800])
    grid(ax)
    ax.legend(loc="upper right", fontsize=10.5, framealpha=0.95)
    save(fig, "t44c")


# ===================================================================
#                    CHƯƠNG IV - ĐỀ SỐ 5
# ===================================================================

def t45a():
    """Một đoạn chuỗi phân rã biểu diễn trên giản đồ N - Z."""
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    pts = [(92, 146, "U-238", 0.18, 0.0, "left"),
           (90, 144, "Th-234", -0.18, 0.0, "right"),
           (91, 143, "Pa-234", 0.0, 0.55, "center"),
           (92, 142, "U-234", 0.18, 0.0, "left"),
           (90, 140, "Th-230", -0.18, 0.0, "right")]
    for z, n, lab, dx, dy, ha in pts:
        ax.plot([z], [n], "o", color=BLUE, ms=9, zorder=5)
        ax.text(z + dx, n + dy, lab, fontsize=10.5, ha=ha,
                va="bottom" if dy > 0 else "center", zorder=6,
                bbox=dict(boxstyle="round,pad=0.16", fc="white", ec="none",
                          alpha=0.85))
    for u, v in zip(pts[:-1], pts[1:]):
        col = RED if v[0] < u[0] else GREEN
        arrow(ax, u[0], u[1], v[0], v[1], color=col, lw=1.8, ms=13,
              shrinkA=9, shrinkB=9)
    for xy, col, lab in (((89.00, 140.6), RED, "phân rã α"),
                         ((89.00, 139.5), GREEN, "phân rã β⁻")):
        arrow(ax, xy[0] - 0.22, xy[1], xy[0] + 0.10, xy[1], color=col, lw=1.8, ms=12)
        ax.text(xy[0] + 0.20, xy[1], lab, fontsize=9.8, color=col, va="center",
                ha="left")
    ax.set_xlabel("Số proton Z", fontsize=11)
    ax.set_ylabel("Số neutron N", fontsize=11)
    ax.set_xlim(88.5, 93.4); ax.set_ylim(138.4, 148.2)
    ax.set_xticks([89, 90, 91, 92, 93])
    ax.set_yticks([139, 141, 143, 145, 147])
    grid(ax)
    save(fig, "t45a")


def t45b():
    """So sánh năng lượng toả ra trên một kilôgam nhiên liệu."""
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    names = ["Đốt than\nđá", "Phân hạch\nU-235", "Nhiệt hạch\nD–T"]
    vals = [3.3e7, 8.2e13, 3.4e14]
    cols = ["#7f8c8d", "#e67e22", "#c0392b"]
    ax.bar(names, vals, color=cols, ec="k", lw=1.2, width=0.55)
    ax.set_yscale("log")
    ax.set_ylabel("Năng lượng toả ra trên 1 kg nhiên liệu (J)", fontsize=10.5)
    ax.set_ylim(1e6, 1e16)
    ax.grid(True, axis="y", ls=":", lw=0.7, color="#b9b9b9")
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "t45b")


def t45c():
    """Ba nguyên tắc an toàn khi làm việc với nguồn phóng xạ."""
    fig, axs = plt.subplots(1, 3, figsize=(9.2, 3.0))
    titles = ["THỜI GIAN", "KHOẢNG CÁCH", "CHE CHẮN"]
    for k, ax in enumerate(axs):
        ax.add_patch(Circle((0.9, 1.55), 0.24, fc="#f4d03f", ec="k", lw=1.3,
                            zorder=4))
        for a in range(3):
            ax.add_patch(Wedge((0.9, 1.55), 0.62, 90 + a * 120 - 22,
                               90 + a * 120 + 22, fc="#f4d03f", ec="k", lw=1.0,
                               zorder=3))
        if k == 0:
            ax.add_patch(Circle((2.55, 1.55), 0.52, fc="white", ec="k", lw=1.8))
            ax.plot([2.55, 2.55], [1.55, 1.95], color="k", lw=1.6)
            ax.plot([2.55, 2.85], [1.55, 1.55], color=RED, lw=1.5)
        elif k == 1:
            arrow(ax, 1.60, 1.55, 2.85, 1.55, color=GREEN, lw=1.6, ms=12,
                  style="<|-|>")
            ax.add_patch(Circle((3.20, 1.85), 0.16, fc="#d6eaf8", ec="k", lw=1.2))
            ax.plot([3.20, 3.20], [1.68, 1.15], color="k", lw=1.6)
            ax.plot([3.20, 2.98], [1.15, 0.75], color="k", lw=1.4)
            ax.plot([3.20, 3.42], [1.15, 0.75], color="k", lw=1.4)
        else:
            ax.add_patch(Rectangle((2.15, 0.70), 0.42, 1.70, fc="#7f8c8d",
                                   ec="k", lw=1.5))
            ax.text(2.36, 2.55, "chì", ha="center", fontsize=9.5)
            ax.add_patch(Circle((3.25, 1.85), 0.16, fc="#d6eaf8", ec="k", lw=1.2))
            ax.plot([3.25, 3.25], [1.68, 1.15], color="k", lw=1.6)
            ax.plot([3.25, 3.03], [1.15, 0.75], color="k", lw=1.4)
            ax.plot([3.25, 3.47], [1.15, 0.75], color="k", lw=1.4)
        ax.set_title(titles[k], fontsize=11.5, fontweight="bold", color=BLUE, pad=6)
        clean(ax, 0.1, 3.9, 0.3, 3.0)
    save(fig, "t45c")


ALL = [t31a, t31b, t31c, t32a, t32b, t32c, t33a, t33b, t33c,
       t34a, t34b, t34c, t35a, t35b, t35c,
       t41a, t41b, t41c, t42a, t42b, t42c, t42d, t43a, t43b, t43c,
       t44a, t44b, t44c, t45a, t45b, t45c]

if __name__ == "__main__":
    print("Đang vẽ hình cho đề Chương III và Chương IV…")
    for f in ALL:
        f()
    print("Xong: %d hình." % len(ALL))
