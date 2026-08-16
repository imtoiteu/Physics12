# -*- coding: utf-8 -*-
"""Hình vẽ gốc cho BỘ 2 – Chương III (Từ trường) và Chương IV (Vật lí hạt nhân)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Ellipse, Arc, FancyBboxPatch

from figbase import (save, arrow, clean, frame, guide, dot, hatch_ground,
                     cross_field, dot_field,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)

MADE = []


def _reg(name):
    MADE.append(name)
    return name


# ---------------------------------------------------------------- 1. ray nghiêng
def b2_ray_nghieng():
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    clean(ax, -0.8, 11.2, -1.4, 6.6)
    a = np.radians(30)
    L = 9.4
    ux, uy = np.cos(a), np.sin(a)
    # mặt phẳng nghiêng
    ax.add_patch(Polygon([(0, 0), (L * ux, L * uy), (L * ux, 0)], closed=True,
                         fc="#f2f4f6", ec=GREY, lw=1.8))
    hatch_ground(ax, -0.4, 9.0, 0, h=0.3, n=18)
    # hai thanh ray
    for off in (0.55, -0.55):
        ax.plot([0.7 * ux - off * 0.30, 8.6 * ux - off * 0.30],
                [0.7 * uy + off * 0.52, 8.6 * uy + off * 0.52],
                color="#5a6470", lw=2.0)
    # thanh MN
    s = 5.4
    ax.plot([s * ux - 0.55 * 0.30, s * ux + 0.55 * 0.30],
            [s * uy + 0.55 * 0.52, s * uy - 0.55 * 0.52], color=RED, lw=5.0,
            solid_capstyle="round")
    ax.text(s * ux + 0.72, s * uy - 0.62, "thanh MN\n(m = 20 g)", fontsize=8.8,
            color=RED, ha="left", va="top")
    # điện trở R ở chân dốc
    ax.add_patch(Rectangle((0.35, 0.28), 0.85, 0.36, fc="white", ec="#5a6470", lw=1.4))
    ax.text(0.78, 0.90, "R", fontsize=10, color="#5a6470", ha="center")
    # cảm ứng từ vuông góc mặt nghiêng
    for k in range(4):
        s2 = 2.2 + k * 1.5
        bx, by = s2 * ux, s2 * uy
        arrow(ax, bx - 0.30 * uy * 1.4, by + 0.30 * ux * 1.4,
              bx - 1.05 * uy, by + 1.05 * ux, color=BLUE, lw=1.3, ms=10)
    ax.text(3.9, 4.7, "$\\vec{B}$ ⊥ mặt phẳng nghiêng", fontsize=10, color=BLUE,
            ha="center")
    # góc
    ax.add_patch(Arc((0, 0), 3.2, 3.2, theta1=0, theta2=30, color=GREEN, lw=1.4))
    ax.text(1.95, 0.32, "30°", fontsize=10, color=GREEN)
    arrow(ax, 4.3 * ux - 1.15 * uy, 4.3 * uy + 1.15 * ux,
          3.1 * ux - 1.15 * uy, 3.1 * uy + 1.15 * ux, color=ORANGE, lw=1.7)
    ax.text(2.35, 2.72, "chiều trượt", fontsize=8.8, color=ORANGE, ha="center")
    save(fig, "b2_ray_nghieng")
    return _reg("b2_ray_nghieng")


# ---------------------------------------------------------------- 2. đồ thị Φ(t)
def b2_do_thi_phi_t():
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    t = [0, 2, 5, 6, 9]
    P = [0, 0.4, 0.4, 0, -0.6]
    ax.plot(t, P, color=RED, lw=2.4, zorder=4)
    ax.plot(t, P, "o", ms=5, color=RED, zorder=5)
    ax.axhline(0, color=GREY, lw=1.1)
    for x, y in zip(t[1:], P[1:]):
        ax.plot([x, x], [0, y], ls="--", lw=0.9, color=LGREY, zorder=0)
    for lab, x in [("(I)", 1.0), ("(II)", 3.5), ("(III)", 5.5), ("(IV)", 7.5)]:
        ax.text(x, -0.78, lab, fontsize=10, color=BLUE, ha="center", fontweight="bold")
    frame(ax, (0, 9.6), (-0.9, 0.62), "t (s)", "Φ (Wb)",
          xticks=[0, 2, 5, 6, 9], yticks=[-0.6, -0.3, 0, 0.3, 0.4])
    save(fig, "b2_do_thi_phi_t")
    return _reg("b2_do_thi_phi_t")


# ---------------------------------------------------------------- 3. máy biến áp
def b2_may_bien_ap():
    fig, ax = plt.subplots(figsize=(6.0, 3.4))
    clean(ax, -0.6, 11.4, -1.0, 6.2)
    # lõi thép
    ax.add_patch(Rectangle((2.6, 0.5), 5.6, 4.6, fc="#e6e9ec", ec="#5a6470", lw=1.8))
    ax.add_patch(Rectangle((3.7, 1.5), 3.4, 2.6, fc="white", ec="#5a6470", lw=1.8))
    ax.text(5.4, 5.55, "lõi thép kín", fontsize=9, color="#5a6470", ha="center")
    # cuộn sơ cấp
    for k in range(6):
        y = 1.05 + k * 0.62
        ax.add_patch(Arc((3.15, y), 1.0, 0.56, theta1=90, theta2=270, color=RED, lw=2.0))
    ax.text(1.55, 3.0, "N₁", fontsize=12, color=RED, ha="center", fontweight="bold")
    # cuộn thứ cấp
    for k in range(4):
        y = 1.35 + k * 0.62
        ax.add_patch(Arc((7.65, y), 1.0, 0.56, theta1=-90, theta2=90, color=BLUE, lw=2.0))
    ax.text(9.35, 3.0, "N₂", fontsize=12, color=BLUE, ha="center", fontweight="bold")
    # nguồn và tải
    ax.plot([2.65, 1.0, 1.0, 2.65], [1.05, 1.05, 4.75, 4.75], color=RED, lw=1.6)
    ax.add_patch(Circle((1.0, 2.9), 0.42, fc="white", ec=RED, lw=1.6))
    ax.text(1.0, 2.9, "~", fontsize=15, color=RED, ha="center", va="center")
    ax.text(0.35, 2.9, "U₁", fontsize=11, color=RED, ha="right", va="center")
    ax.plot([8.15, 10.2, 10.2, 8.15], [1.35, 1.35, 4.45, 4.45], color=BLUE, lw=1.6)
    ax.add_patch(Rectangle((9.85, 2.4), 0.7, 1.0, fc="white", ec=BLUE, lw=1.6))
    ax.text(11.0, 2.9, "U₂", fontsize=11, color=BLUE, ha="left", va="center")
    save(fig, "b2_may_bien_ap")
    return _reg("b2_may_bien_ap")


# ---------------------------------------------------------------- 4. đồ thị i(t)
def b2_do_thi_i_t():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    t = np.linspace(0, 2, 400)
    i = np.cos(2 * np.pi * t)
    ax.plot(t, i, color=RED, lw=2.2, zorder=4)
    ax.axhline(0, color=GREY, lw=1.1)
    for lev, c in ((1 / np.sqrt(2), BLUE), (-1 / np.sqrt(2), BLUE)):
        ax.axhline(lev, color=c, lw=1.2, ls="--")
    ax.fill_between(t, -1 / np.sqrt(2), 1 / np.sqrt(2), color=GREEN, alpha=0.07)
    ax.text(1.72, 0.755, "$+I_0/\\sqrt{2}$", fontsize=10, color=BLUE, va="bottom")
    ax.text(1.72, -0.90, "$-I_0/\\sqrt{2}$", fontsize=10, color=BLUE, va="bottom")
    for x0, x1 in [(0, 0.125), (0.375, 0.625), (0.875, 1.125), (1.375, 1.625),
                   (1.875, 2.0)]:
        ax.fill_between(t, -1.15, 1.15, where=(t >= x0) & (t <= x1),
                        color=ORANGE, alpha=0.13, zorder=0)
    ax.text(1.0, -1.34, "vùng tô đậm: |i| > giá trị hiệu dụng", fontsize=9,
            color=ORANGE, ha="center")
    frame(ax, (0, 2.05), (-1.5, 1.35), "t / T", "i",
          xticks=[0, 0.5, 1.0, 1.5, 2.0], yticks=[-1, 0, 1],
          yticklabels=["−I₀", "0", "I₀"])
    save(fig, "b2_do_thi_i_t")
    return _reg("b2_do_thi_i_t")


# ---------------------------------------------------------------- 5. khung dây quay
def b2_khung_quay():
    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    clean(ax, -1.0, 10.4, -1.6, 6.0)
    # từ trường đều
    for k in range(6):
        y = 0.35 + k * 0.9
        arrow(ax, 0.0, y, 9.6, y, color=BLUE, lw=1.0, ms=9)
    ax.text(0.1, 5.55, "$\\vec{B}$", fontsize=13, color=BLUE)
    # khung dây nghiêng
    cx, cy = 5.0, 2.6
    w, h = 3.0, 3.4
    ang = 28
    a = np.radians(ang)
    pts = []
    for dx, dy in [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]:
        pts.append((cx + dx * np.cos(a) * 0.55, cy + dy + dx * np.sin(a)))
    ax.add_patch(Polygon(pts, closed=True, fc="#fdece0", ec=RED, lw=2.2, zorder=3))
    ax.text(cx + 0.05, cy, "N vòng", fontsize=9.5, color=RED, ha="center",
            va="center", zorder=4)
    # trục quay
    ax.plot([cx, cx], [-0.9, 6.0], color="#5a6470", lw=1.8, ls="--", zorder=2)
    ax.text(cx + 0.2, 5.7, "trục quay", fontsize=9, color="#5a6470", ha="left")
    ax.add_patch(Arc((cx, 5.55), 1.8, 1.0, theta1=200, theta2=340, color=GREEN, lw=1.6))
    arrow(ax, cx + 0.86, 5.17, cx + 0.92, 5.35, color=GREEN, lw=1.4, ms=10)
    ax.text(cx + 1.25, 5.00, "ω", fontsize=12, color=GREEN)
    # vành khuyên + chổi quét
    ax.add_patch(Ellipse((cx, -0.65), 1.5, 0.42, fc="white", ec="#5a6470", lw=1.4))
    ax.plot([cx - 1.35, cx - 0.75], [-0.65, -0.65], color="#5a6470", lw=1.6)
    ax.plot([cx + 0.75, cx + 1.35], [-0.65, -0.65], color="#5a6470", lw=1.6)
    ax.text(cx, -1.35, "vành khuyên và chổi quét", fontsize=8.6, color="#5a6470",
            ha="center")
    save(fig, "b2_khung_quay")
    return _reg("b2_khung_quay")


# ---------------------------------------------------------------- 6. thanh treo lò xo
def b2_thanh_lo_xo():
    fig, ax = plt.subplots(figsize=(4.8, 4.2))
    clean(ax, -1.0, 8.0, -1.4, 8.2)
    hatch_ground(ax, 0.4, 7.0, 7.4, h=-0.35, n=14)
    for x in (1.4, 6.0):
        ys = np.linspace(4.4, 7.4, 120)
        xs = x + 0.28 * np.sin(np.linspace(0, 9 * np.pi, 120))
        ax.plot(xs, ys, color="#5a6470", lw=1.5)
    ax.plot([1.4, 6.0], [4.4, 4.4], color=RED, lw=5.0, solid_capstyle="round")
    ax.text(1.15, 4.4, "M", fontsize=11, color=RED, ha="right", va="center",
            fontweight="bold")
    ax.text(6.25, 4.4, "N", fontsize=11, color=RED, ha="left", va="center",
            fontweight="bold")
    # từ trường nằm ngang, vuông góc thanh -> vẽ dấu chấm (hướng ra ngoài trang)
    dot_field(ax, 1.9, 5.5, 1.6, 3.6, n=5, m=3, color=BLUE)
    ax.text(3.7, 0.95, "$\\vec{B}$ nằm ngang, vuông góc với thanh\n(hướng ra ngoài trang giấy)",
            fontsize=9, color=BLUE, ha="center")
    arrow(ax, 1.4, 5.4, 2.6, 5.4, color=GREEN, lw=1.6)
    ax.text(3.0, 5.4, "I", fontsize=11, color=GREEN, ha="left", va="center")
    arrow(ax, 3.7, 4.15, 3.7, 2.75, color=ORANGE, lw=2.0)
    ax.text(3.9, 3.4, "$\\vec{F}$", fontsize=12, color=ORANGE, ha="left", va="center")
    save(fig, "b2_thanh_lo_xo")
    return _reg("b2_thanh_lo_xo")


# ---------------------------------------------------------------- 7. khung nghiêng với B
def b2_khung_nghieng_B():
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    clean(ax, -1.2, 9.2, -1.0, 5.8)
    a = np.radians(30)
    # mặt phẳng khung (nhìn nghiêng, biểu diễn bằng một đoạn thẳng)
    L = 5.2
    x0, y0 = 1.6, 1.2
    x1, y1 = x0 + L * np.cos(a), y0 + L * np.sin(a)
    ax.plot([x0, x1], [y0, y1], color=RED, lw=4.0, solid_capstyle="round")
    ax.text((x0 + x1) / 2 - 0.4, (y0 + y1) / 2 + 0.55, "mặt phẳng khung",
            fontsize=9.2, color=RED, rotation=30, ha="center")
    # B nằm ngang
    for k in range(3):
        yy = 0.75 + k * 1.55
        arrow(ax, 0.0, yy, 8.4, yy, color=BLUE, lw=1.1, ms=10)
    ax.text(8.55, 3.85, "$\\vec{B}$", fontsize=13, color=BLUE, va="center")
    # pháp tuyến
    nx, ny = np.cos(a + np.pi / 2), np.sin(a + np.pi / 2)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    arrow(ax, cx, cy, cx + 2.0 * nx, cy + 2.0 * ny, color=GREEN, lw=1.8)
    ax.text(cx + 2.1 * nx - 0.15, cy + 2.1 * ny + 0.15, "$\\vec{n}$", fontsize=13,
            color=GREEN, ha="right")
    ax.add_patch(Arc((x0, y0), 2.4, 2.4, theta1=0, theta2=30, color=ORANGE, lw=1.4))
    ax.text(x0 + 1.42, y0 + 0.16, "30°", fontsize=10, color=ORANGE)
    ax.add_patch(Arc((cx, cy), 2.0, 2.0, theta1=0, theta2=120, color=PURPLE, lw=1.3,
                     ls=":"))
    ax.text(cx + 0.30, cy + 1.15, "α", fontsize=11, color=PURPLE)
    save(fig, "b2_khung_nghieng_B")
    return _reg("b2_khung_nghieng_B")


# ---------------------------------------------------------------- 8. năng lượng liên kết riêng
def b2_nllk_rieng():
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    A = np.array([2, 3, 4, 6, 7, 9, 12, 16, 20, 24, 27, 32, 40, 45, 50, 56, 63, 75,
                  90, 107, 120, 140, 160, 180, 200, 209, 220, 235, 238])
    e = np.array([1.11, 2.83, 7.07, 5.33, 5.61, 6.46, 7.68, 7.98, 8.03, 8.26, 8.33,
                  8.49, 8.60, 8.69, 8.75, 8.79, 8.75, 8.70, 8.60, 8.55, 8.50, 8.38,
                  8.21, 8.02, 7.88, 7.85, 7.80, 7.59, 7.57])
    ax.plot(A, e, color=BLUE, lw=1.8, zorder=3)
    ax.plot(A, e, "o", ms=3.2, color=BLUE, zorder=4)
    for lab, xa, ya, dx, dy in [("²H", 2, 1.11, 4, -0.45), ("⁴He", 4, 7.07, -1, 0.35),
                                ("¹²C", 12, 7.68, 2, -0.75), ("⁵⁶Fe", 56, 8.79, -2, 0.30),
                                ("²³⁵U", 235, 7.59, -12, -0.85)]:
        ax.annotate(lab, xy=(xa, ya), xytext=(xa + dx, ya + dy), fontsize=9.5,
                    color=RED, ha="center",
                    arrowprops=dict(arrowstyle="->", color=RED, lw=0.9))
    ax.axvline(56, color=GREEN, lw=1.1, ls="--")
    ax.text(60, 2.3, "vùng bền vững nhất", fontsize=9, color=GREEN, rotation=90)
    ax.annotate("", xy=(50, 1.35), xytext=(4, 1.35),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5))
    ax.text(26, 1.55, "tổng hợp (nhiệt hạch)", fontsize=9, color=ORANGE, ha="center")
    ax.annotate("", xy=(70, 0.55), xytext=(235, 0.55),
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.5))
    ax.text(152, 0.75, "phân hạch", fontsize=9, color=PURPLE, ha="center")
    frame(ax, (0, 250), (0, 10.0), "A (số khối)", "ε = W_lk/A  (MeV/nuclôn)",
          xticks=[0, 50, 100, 150, 200, 250], yticks=[0, 2, 4, 6, 8, 10])
    save(fig, "b2_nllk_rieng")
    return _reg("b2_nllk_rieng")


# ---------------------------------------------------------------- 9. khung vào vùng từ trường
def b2_khung_vao_tu_truong():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    clean(ax, -1.0, 13.5, -1.8, 4.6)
    ax.add_patch(Rectangle((5.0, 0.0), 5.0, 3.6, fc="#eaf2fb", ec=BLUE, lw=1.4))
    cross_field(ax, 5.4, 9.6, 0.35, 3.25, n=7, m=5, color=BLUE, size=10)
    ax.text(7.5, 4.05, "vùng từ trường đều  B = 0,4 T", fontsize=9.2, color=BLUE,
            ha="center")
    ax.annotate("", xy=(10.0, -0.55), xytext=(5.0, -0.55),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.2))
    ax.text(7.5, -1.0, "d = 50 cm", fontsize=9, color=BLUE, ha="center", va="top")
    # khung dây vuông
    ax.add_patch(Rectangle((1.6, 0.9), 2.0, 2.0, fc="none", ec=RED, lw=2.4))
    ax.annotate("", xy=(3.6, 0.45), xytext=(1.6, 0.45),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2))
    ax.text(2.6, 0.05, "a = 20 cm", fontsize=9, color=RED, ha="center", va="top")
    arrow(ax, 3.9, 1.9, 4.9, 1.9, color=ORANGE, lw=2.0)
    ax.text(4.4, 2.25, "v", fontsize=11, color=ORANGE, ha="center")
    # khung ở vị trí đã ra khỏi vùng
    ax.add_patch(Rectangle((10.6, 0.9), 2.0, 2.0, fc="none", ec=RED, lw=1.6, ls=":"))
    ax.text(11.6, 3.25, "khung sau khi\nra khỏi vùng", fontsize=8.4, color=RED,
            ha="center")
    save(fig, "b2_khung_vao_tu_truong")
    return _reg("b2_khung_vao_tu_truong")


# ---------------------------------------------------------------- 10. nam châm rơi qua vòng dây
def b2_nam_cham_roi():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    clean(ax, -1.0, 12.0, -0.8, 6.6)
    for k, (x0, cap) in enumerate([(1.0, "nam châm lại gần"), (7.0, "nam châm ra xa")]):
        # vòng dây
        ax.add_patch(Ellipse((x0 + 1.8, 2.0), 3.4, 0.9, fc="none", ec="#5a6470", lw=2.2))
        # nam châm
        ny = 4.3 if k == 0 else 0.9
        ax.add_patch(Rectangle((x0 + 1.35, ny), 0.9, 1.5, fc=RED, ec="none"))
        ax.add_patch(Rectangle((x0 + 1.35, ny - 0.75), 0.9, 0.75, fc=BLUE, ec="none"))
        ax.text(x0 + 1.8, ny + 0.75, "N", fontsize=10, color="white", ha="center",
                va="center", fontweight="bold")
        ax.text(x0 + 1.8, ny - 0.38, "S", fontsize=10, color="white", ha="center",
                va="center", fontweight="bold")
        arrow(ax, x0 + 2.75, ny + 0.4, x0 + 2.75, ny - 0.9, color=ORANGE, lw=1.7)
        ax.text(x0 + 2.95, ny - 0.3, "v", fontsize=10.5, color=ORANGE, ha="left")
        # lực từ cản
        fy = 2.9 if k == 0 else 1.55
        arrow(ax, x0 + 0.55, fy, x0 + 0.55, fy + (1.1 if k == 0 else -1.1),
              color=GREEN, lw=1.8)
        ax.text(x0 + 0.35, fy + (0.55 if k == 0 else -0.55), "$\\vec{F}$", fontsize=11,
                color=GREEN, ha="right", va="center")
        ax.text(x0 + 1.8, -0.45, cap, fontsize=9.2, color="#333333", ha="center")
        ax.text(x0 + 3.55, 2.0, "vòng dây\nkín", fontsize=8.4, color="#5a6470",
                ha="left", va="center")
    save(fig, "b2_nam_cham_roi")
    return _reg("b2_nam_cham_roi")


# ---------------------------------------------------------------- 11. truyền tải điện
def b2_truyen_tai():
    fig, ax = plt.subplots(figsize=(7.0, 2.9))
    clean(ax, -0.5, 16.5, -1.8, 4.4)
    ax.add_patch(FancyBboxPatch((0.2, 0.9), 2.6, 2.0, boxstyle="round,pad=0.08",
                                fc="#fdece0", ec=ORANGE, lw=1.8))
    ax.text(1.5, 1.9, "lò phản ứng\nhạt nhân", fontsize=9, color=ORANGE, ha="center",
            va="center")
    ax.add_patch(FancyBboxPatch((3.5, 0.9), 2.4, 2.0, boxstyle="round,pad=0.08",
                                fc="#eaf2fb", ec=BLUE, lw=1.8))
    ax.text(4.7, 1.9, "máy phát\n600 MW\n20 kV", fontsize=8.6, color=BLUE,
            ha="center", va="center")
    ax.add_patch(FancyBboxPatch((6.6, 0.9), 2.2, 2.0, boxstyle="round,pad=0.08",
                                fc="#f2f8f0", ec=GREEN, lw=1.8))
    ax.text(7.7, 1.9, "máy tăng áp\n→ 500 kV", fontsize=8.6, color=GREEN,
            ha="center", va="center")
    ax.add_patch(FancyBboxPatch((13.4, 0.9), 2.6, 2.0, boxstyle="round,pad=0.08",
                                fc="#f4eef8", ec=PURPLE, lw=1.8))
    ax.text(14.7, 1.9, "khu dân cư\n(máy hạ áp)", fontsize=9, color=PURPLE,
            ha="center", va="center")
    for x0, x1 in [(2.8, 3.5), (5.9, 6.6)]:
        arrow(ax, x0, 1.9, x1, 1.9, color="#333333", lw=1.5)
    ax.plot([8.8, 13.4], [2.4, 2.4], color="#5a6470", lw=1.8)
    ax.plot([8.8, 13.4], [1.4, 1.4], color="#5a6470", lw=1.8)
    for x in (10.0, 12.2):
        ax.plot([x, x], [1.4, 2.4], color="#5a6470", lw=1.0)
        ax.plot([x - 0.35, x + 0.35], [0.15, 0.15], color=GREY, lw=1.4)
        ax.plot([x, x], [0.15, 1.4], color=GREY, lw=1.6)
    ax.text(11.1, 3.0, "đường dây:  R = 10 Ω", fontsize=9.2, color="#5a6470",
            ha="center")
    ax.text(11.1, 0.55, "hao phí ΔP = ?", fontsize=9.2, color=RED, ha="center")
    save(fig, "b2_truyen_tai")
    return _reg("b2_truyen_tai")


# ---------------------------------------------------------------- 12. đồ thị độ phóng xạ
def b2_do_thi_H_t():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 3.5))
    t = np.array([0, 2, 4, 6, 8])
    H = np.array([800.0, 566.0, 400.0, 283.0, 200.0])
    tt = np.linspace(0, 9, 200)
    ax1.plot(tt, 800 * 2 ** (-tt / 4.0), color=BLUE, lw=1.8, zorder=2)
    ax1.plot(t, H, "o", ms=7, mfc="white", mec=RED, mew=1.8, zorder=4)
    frame(ax1, (0, 9.4), (0, 900), "t (giờ)", "H (kBq)",
          xticks=[0, 2, 4, 6, 8], yticks=[0, 200, 400, 600, 800])
    ax2.plot(tt, np.log(800 * 2 ** (-tt / 4.0)), color=GREEN, lw=1.8, zorder=2)
    ax2.plot(t, np.log(H), "s", ms=6, mfc="white", mec=RED, mew=1.8, zorder=4)
    frame(ax2, (0, 9.4), (5.0, 7.2), "t (giờ)", "ln H  (H tính bằng kBq)",
          xticks=[0, 2, 4, 6, 8], yticks=[5.0, 5.5, 6.0, 6.5, 7.0])
    ax2.text(2.2, 5.35, "hệ số góc = −λ", fontsize=9.5, color=GREEN)
    fig.tight_layout()
    save(fig, "b2_do_thi_H_t")
    return _reg("b2_do_thi_H_t")


# ---------------------------------------------------------------- 13. cân dòng điện
def b2_can_dong_dien():
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    clean(ax, -0.8, 12.6, -1.6, 6.4)
    # cân điện tử
    ax.add_patch(FancyBboxPatch((0.4, 0.0), 4.6, 1.5, boxstyle="round,pad=0.06",
                                fc="#f2f4f6", ec="#5a6470", lw=1.8))
    ax.add_patch(Rectangle((3.3, 0.35), 1.4, 0.75, fc="#1b2a33", ec="none"))
    ax.text(4.0, 0.72, "0,00 g", fontsize=8.6, color="#7ee787", ha="center",
            va="center", family="DejaVu Sans Mono")
    ax.add_patch(Rectangle((1.0, 1.5), 3.4, 0.25, fc="#c9ced3", ec="#5a6470", lw=1.0))
    # nam châm chữ U trên đĩa cân
    ax.add_patch(Rectangle((1.3, 1.75), 2.8, 0.55, fc="#7a8794", ec="none"))
    ax.add_patch(Rectangle((1.3, 2.30), 0.7, 1.9, fc=RED, ec="none"))
    ax.add_patch(Rectangle((3.4, 2.30), 0.7, 1.9, fc=BLUE, ec="none"))
    ax.text(1.65, 3.9, "N", fontsize=10, color="white", ha="center", fontweight="bold")
    ax.text(3.75, 3.9, "S", fontsize=10, color="white", ha="center", fontweight="bold")
    for yy in (2.60, 3.95):
        arrow(ax, 2.05, yy, 3.35, yy, color=GREEN, lw=1.1, ms=9)
    ax.text(2.7, 4.42, "$\\vec{B}$", fontsize=12, color=GREEN, ha="center")
    # đoạn dây cố định vào giá đỡ
    ax.plot([1.4, 4.0], [3.35, 3.35], color=ORANGE, lw=4.0, solid_capstyle="round")
    ax.plot([4.0, 6.4], [3.35, 3.35], color=ORANGE, lw=1.6)
    ax.plot([6.4, 6.4], [3.35, 5.6], color=ORANGE, lw=1.6)
    ax.annotate("ℓ = 5 cm", xy=(2.7, 3.35), xytext=(0.15, 4.30), fontsize=9,
                color=ORANGE, ha="center",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))
    ax.add_patch(Rectangle((6.9, 4.9), 2.3, 1.2, fc="white", ec="#5a6470", lw=1.6))
    ax.text(8.05, 5.5, "nguồn I", fontsize=9, color="#5a6470", ha="center", va="center")
    ax.plot([6.4, 6.9], [5.6, 5.6], color=ORANGE, lw=1.6)
    ax.plot([9.2, 10.2, 10.2, 1.4], [5.5, 5.5, 3.35, 3.35], color=ORANGE, lw=1.0,
            ls=":")
    ax.text(9.9, 2.3, "đoạn dây nằm ngang,\nvuông góc với $\\vec{B}$", fontsize=8.8,
            color=ORANGE, ha="center")
    ax.text(2.7, -1.05, "số chỉ của cân thay đổi khi có dòng điện", fontsize=9,
            color=RED, ha="center")
    save(fig, "b2_can_dong_dien")
    return _reg("b2_can_dong_dien")


# ---------------------------------------------------------------- 14. ray nằm ngang
def b2_ray_ngang():
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    clean(ax, -0.8, 12.2, -1.4, 5.2)
    dot_field(ax, 1.4, 10.6, 0.9, 3.5, n=9, m=4, color=BLUE)
    ax.text(6.0, 4.35, "$\\vec{B}$ thẳng đứng hướng lên (ra ngoài trang giấy),  B = 0,5 T",
            fontsize=8.8, color=BLUE, ha="center")
    for y in (0.6, 3.8):
        ax.plot([1.0, 11.2], [y, y], color="#5a6470", lw=2.2)
    ax.text(11.4, 2.2, "ray", fontsize=9, color="#5a6470", ha="left", va="center")
    ax.plot([5.2, 5.2], [0.6, 3.8], color=RED, lw=5.0, solid_capstyle="round")
    ax.text(5.2, 4.05, "thanh (m = 50 g)", fontsize=9, color=RED, ha="center")
    ax.add_patch(Rectangle((1.0, 1.85), 0.0, 0.0))
    ax.plot([1.0, 1.0], [0.6, 3.8], color="#5a6470", lw=1.8)
    ax.add_patch(Rectangle((0.6, 1.85), 0.8, 0.7, fc="white", ec="#5a6470", lw=1.4))
    ax.text(0.35, 2.2, "R", fontsize=10, color="#5a6470", ha="right", va="center")
    arrow(ax, 5.9, 2.2, 7.6, 2.2, color=ORANGE, lw=2.0)
    ax.text(6.75, 2.55, "$\\vec{F}$ = 0,2 N", fontsize=10, color=ORANGE, ha="center")
    ax.annotate("", xy=(5.2, 0.15), xytext=(1.0, 0.15),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.2))
    ax.text(3.1, -0.25, "ℓ = 40 cm (khoảng cách hai ray)", fontsize=8.8, color=GREEN,
            ha="center", va="top")
    save(fig, "b2_ray_ngang")
    return _reg("b2_ray_ngang")


# ---------------------------------------------------------------- 15. sơ đồ phân rã Po
def b2_so_do_phan_ra():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    clean(ax, -0.6, 13.4, -1.4, 4.0)
    ax.add_patch(FancyBboxPatch((0.4, 1.0), 2.8, 1.6, boxstyle="round,pad=0.08",
                                fc="#fdece0", ec=ORANGE, lw=1.8))
    ax.text(1.8, 1.8, "²¹⁰₈₄Po", fontsize=13, color=ORANGE, ha="center", va="center")
    ax.add_patch(FancyBboxPatch((7.6, 1.0), 2.8, 1.6, boxstyle="round,pad=0.08",
                                fc="#eaf2fb", ec=BLUE, lw=1.8))
    ax.text(9.0, 1.8, "²⁰⁶₈₂Pb", fontsize=13, color=BLUE, ha="center", va="center")
    arrow(ax, 3.5, 1.8, 7.3, 1.8, color="#333333", lw=1.8)
    ax.text(5.4, 2.25, "phóng xạ α", fontsize=10, color=RED, ha="center")
    ax.text(5.4, 1.25, "T = 138 ngày", fontsize=9.5, color=GREY, ha="center")
    ax.add_patch(Circle((5.4, 0.25), 0.42, fc="#f6dede", ec=RED, lw=1.4))
    ax.text(5.4, 0.25, "⁴₂He", fontsize=9, color=RED, ha="center", va="center")
    arrow(ax, 5.4, 1.45, 5.4, 0.75, color=RED, lw=1.3)
    ax.text(11.9, 1.8, "bền", fontsize=10, color=BLUE, ha="center", va="center")
    arrow(ax, 10.7, 1.8, 11.4, 1.8, color=BLUE, lw=1.4)
    save(fig, "b2_so_do_phan_ra")
    return _reg("b2_so_do_phan_ra")


# ---------------------------------------------------------------- 16. tokamak
def b2_tokamak():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    clean(ax, -4.4, 4.4, -3.6, 3.6)
    ax.add_patch(Ellipse((0, 0), 7.2, 4.6, fc="none", ec="#5a6470", lw=2.2))
    ax.add_patch(Ellipse((0, 0), 3.4, 2.0, fc="white", ec="#5a6470", lw=2.2))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(2.63 * np.cos(th), 1.62 * np.cos(th) * 0 + 1.62 * np.sin(th),
            color=PINK, lw=6.0, alpha=0.45)
    ax.text(0, 2.65, "plasma nhiệt độ rất cao", fontsize=9.2, color=PINK, ha="center")
    for a0 in np.linspace(0, 2 * np.pi, 10, endpoint=False):
        cx, cy = 2.63 * np.cos(a0), 1.62 * np.sin(a0)
        ax.add_patch(Ellipse((cx, cy), 1.5, 0.95, angle=np.degrees(a0) + 90,
                             fc="none", ec=BLUE, lw=1.3))
    ax.text(0, -3.15, "cuộn dây tạo từ trường mạnh giam giữ plasma",
            fontsize=9, color=BLUE, ha="center")
    save(fig, "b2_tokamak")
    return _reg("b2_tokamak")


ALL = [b2_ray_nghieng, b2_do_thi_phi_t, b2_may_bien_ap, b2_do_thi_i_t, b2_khung_quay,
       b2_thanh_lo_xo, b2_khung_nghieng_B, b2_nllk_rieng, b2_khung_vao_tu_truong,
       b2_nam_cham_roi, b2_truyen_tai, b2_do_thi_H_t, b2_can_dong_dien, b2_ray_ngang,
       b2_so_do_phan_ra, b2_tokamak]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
