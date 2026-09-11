# -*- coding: utf-8 -*-
"""Hình minh hoạ CHƯƠNG III – TỪ TRƯỜNG (dùng cho slide bài giảng và đề luyện tập)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, FancyArrowPatch, Ellipse, Polygon

from figbase import (save, arrow, clean, frame, cross_field, dot_field,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)

MADE = []


def _reg(n):
    MADE.append(n)
    return n


def _bar_magnet(ax, x, y, w, h, horizontal=True):
    """Nam châm thẳng: cực Bắc đỏ, cực Nam xanh (quy ước quốc tế)."""
    if horizontal:
        ax.add_patch(Rectangle((x, y), w / 2, h, fc="#e74c3c", ec="#7b241c", lw=1.4))
        ax.add_patch(Rectangle((x + w / 2, y), w / 2, h, fc="#2e86c1", ec="#1b4f72", lw=1.4))
        ax.text(x + w / 4, y + h / 2, "N", color="white", fontsize=15, fontweight="bold",
                ha="center", va="center")
        ax.text(x + 3 * w / 4, y + h / 2, "S", color="white", fontsize=15, fontweight="bold",
                ha="center", va="center")
    else:
        ax.add_patch(Rectangle((x, y + h / 2), w, h / 2, fc="#e74c3c", ec="#7b241c", lw=1.4))
        ax.add_patch(Rectangle((x, y), w, h / 2, fc="#2e86c1", ec="#1b4f72", lw=1.4))
        ax.text(x + w / 2, y + 3 * h / 4, "N", color="white", fontsize=14, fontweight="bold",
                ha="center", va="center")
        ax.text(x + w / 2, y + h / 4, "S", color="white", fontsize=14, fontweight="bold",
                ha="center", va="center")


# ------------------------------------------------------------------ 1. đường sức nam châm thẳng
def t_sd_duongsuc_ncthang():
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    _bar_magnet(ax, -1.5, -0.32, 3.0, 0.64)
    # đường sức khép kín bên ngoài: N (phải của cực bắc) → S
    for k, ry in enumerate([0.55, 1.05, 1.60, 2.25]):
        th = np.linspace(0, np.pi, 300)
        rx = 1.5 + ry * 0.62
        x = rx * np.cos(th)
        y = ry * np.sin(th)
        ax.plot(x, y, color=BLUE, lw=1.5)
        ax.plot(x, -y, color=BLUE, lw=1.5)
        for sgn in (1, -1):
            i = 150
            arrow(ax, x[i], sgn * y[i], x[i - 6], sgn * y[i - 6], color=BLUE, lw=1.4, ms=11)
    # bên trong nam châm: S → N
    ax.text(-2.9, 2.35, "Đường sức từ đi RA ở cực Bắc,\nđi VÀO ở cực Nam", fontsize=9.6,
            color=BLUE, ha="left", va="top")
    ax.text(2.95, -2.3, "Đường sức từ là những đường\ncong KHÉP KÍN", fontsize=9.2,
            color=GREY, ha="right", va="bottom", style="italic")
    clean(ax, -3.0, 3.0, -2.6, 2.6)
    save(fig, "t_sd_duongsuc_ncthang")
    return _reg("t_sd_duongsuc_ncthang")


# ------------------------------------------------------------------ 2. dây thẳng + quy tắc nắm tay phải
def t_sd_duongsuc_daythang():
    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    ax.plot([0, 0], [-2.2, 2.2], color=BROWN, lw=4.0, solid_capstyle="round")
    arrow(ax, 0, 1.55, 0, 2.35, color=BROWN, lw=3.0, ms=16)
    ax.text(0.16, 2.3, "I", fontsize=14, color=BROWN, fontweight="bold", ha="left")
    for r in (0.62, 1.15, 1.72):
        ax.add_patch(Ellipse((0, 0), 2 * r, 2 * r * 0.34, fill=False, ec=BLUE, lw=1.6))
        # phía GẦN người xem (nửa dưới của elip) B hướng sang phải, phía xa hướng sang trái
        arrow(ax, -r * 0.02, -r * 0.34, r * 0.30, -r * 0.325, color=BLUE, lw=1.5, ms=12)
        arrow(ax, r * 0.02, r * 0.34, -r * 0.30, r * 0.325, color=BLUE, lw=1.5, ms=12)
    ax.text(2.0, 0.72, "đường sức từ là những\nđường tròn đồng tâm,\nnằm trong mặt phẳng\n"
            "vuông góc với dây", fontsize=9.2, color=BLUE, ha="left", va="center")
    ax.text(0, -2.55,
            "Quy tắc nắm tay phải: ngón cái chỉ chiều dòng điện I,\n"
            "bốn ngón khum lại chỉ chiều đường sức từ.",
            fontsize=9.6, color=GREY, ha="center", va="center")
    ax.text(-2.0, 1.55, r"$B=2\cdot10^{-7}\,\dfrac{I}{r}$", fontsize=12, color=GREEN,
            ha="center", va="center")
    clean(ax, -3.4, 4.3, -3.1, 2.6, eq=False)
    save(fig, "t_sd_duongsuc_daythang")
    return _reg("t_sd_duongsuc_daythang")


# ------------------------------------------------------------------ 3. ống dây
def t_sd_ongday():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    xs = np.linspace(-2.1, 2.1, 8)
    for x in xs:
        ax.add_patch(Ellipse((x, 0), 0.26, 1.7, fill=False, ec=BROWN, lw=2.0))
    ax.plot([-2.45, -2.2], [-0.85, -0.85], color=BROWN, lw=2.2)
    ax.plot([2.2, 2.45], [0.85, 0.85], color=BROWN, lw=2.2)
    arrow(ax, -2.9, -0.85, -2.45, -0.85, color=BROWN, lw=2.2, ms=14)
    ax.text(-3.0, -0.85, "I", fontsize=13, color=BROWN, fontweight="bold",
            ha="right", va="center")
    for y in (-0.45, 0, 0.45):
        ax.plot([-2.0, 2.0], [y, y], color=BLUE, lw=1.5)
        arrow(ax, 0.0, y, 0.55, y, color=BLUE, lw=1.5, ms=12)
    for sgn in (1, -1):
        for k, amp in enumerate((0.95, 1.45)):
            th = np.linspace(0, np.pi, 200)
            ax.plot(2.0 * np.cos(th) * (1 + 0.25 * k),
                    sgn * (0.45 + amp * np.sin(th)), color=BLUE, lw=1.2, alpha=0.8)
            i = 100
            xx = 2.0 * np.cos(th) * (1 + 0.25 * k)
            yy = sgn * (0.45 + amp * np.sin(th))
            arrow(ax, xx[i], yy[i], xx[i - 5], yy[i - 5], color=BLUE, lw=1.2, ms=10)
    ax.text(2.95, 0, "N", fontsize=17, color="#c0392b", fontweight="bold",
            ha="left", va="center")
    ax.text(-2.95, 0, "S", fontsize=17, color="#1f4e9c", fontweight="bold",
            ha="right", va="center")
    ax.text(0, -2.25, "Trong lòng ống dây từ trường gần như ĐỀU: các đường sức song song, cách đều",
            fontsize=9.6, color=GREY, ha="center", va="center")
    ax.text(3.95, 1.55, r"$B = 4\pi\cdot10^{-7}\,n I$", fontsize=12, color=GREEN,
            ha="center", va="center")
    ax.text(3.95, 1.12, "n = số vòng trên 1 m", fontsize=8.8, color=GREY, ha="center")
    clean(ax, -4.4, 5.4, -2.5, 2.3, eq=False)
    save(fig, "t_sd_ongday")
    return _reg("t_sd_ongday")


# ------------------------------------------------------------------ 4. từ trường Trái Đất
def t_sd_tutruong_traidat():
    fig, ax = plt.subplots(figsize=(5.6, 4.8))
    ang = np.deg2rad(11.5)
    rot = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])

    def R(x, y):
        v = rot @ np.vstack([np.asarray(x, dtype=float), np.asarray(y, dtype=float)])
        return v[0], v[1]

    # đường sức lưỡng cực, vẽ trong hệ trục từ rồi xoay 11,5°
    for L in (1.35, 1.75, 2.35, 3.10):
        th = np.linspace(0.001, np.pi - 0.001, 400)
        r = L * np.sin(th) ** 2
        m = r >= 1.0
        if not m.any():
            continue
        for sx in (1, -1):
            x, y = R(sx * r[m] * np.sin(th[m]), r[m] * np.cos(th[m]))
            ax.plot(x, y, color=BLUE, lw=1.3, zorder=2)
            k = len(x) // 2
            arrow(ax, x[k], y[k], x[k - 3], y[k - 3], color=BLUE, lw=1.2, ms=10)
    ax.add_patch(Circle((0, 0), 1.0, fc="#d6eaf8", ec="#2874a6", lw=1.8, zorder=3))
    # thanh nam châm tương đương, nghiêng 11,5°
    px, py = R([-0.17, 0.17, 0.17, -0.17], [0.0, 0.0, 0.62, 0.62])
    ax.add_patch(Polygon(np.c_[px, py], fc="#2e86c1", ec="#1b4f72", lw=1.2, zorder=4))
    px, py = R([-0.17, 0.17, 0.17, -0.17], [-0.62, -0.62, 0.0, 0.0])
    ax.add_patch(Polygon(np.c_[px, py], fc="#e74c3c", ec="#7b241c", lw=1.2, zorder=4))
    tx, ty = R([0], [0.34])
    ax.text(float(tx[0]), float(ty[0]), "S", color="white", fontsize=12, fontweight="bold",
            ha="center", va="center", zorder=5)
    tx, ty = R([0], [-0.34])
    ax.text(float(tx[0]), float(ty[0]), "N", color="white", fontsize=12, fontweight="bold",
            ha="center", va="center", zorder=5)
    ax.plot([0, 0], [-1.35, 1.35], color=GREY, ls="--", lw=1.1, zorder=5)
    ax.text(0.08, 1.40, "trục quay địa lí", fontsize=8.6, color=GREY, ha="left")
    ax.text(-2.55, 1.95, "cực Bắc địa lí\n≈ cực NAM từ", fontsize=9.2, color=RED,
            ha="center", va="center")
    arrow(ax, -2.05, 1.75, -0.42, 0.92, color=RED, lw=1.0, ms=9)
    ax.text(2.55, -2.05, "cực Nam địa lí\n≈ cực BẮC từ", fontsize=9.2, color=BLUE,
            ha="center", va="center")
    arrow(ax, 2.05, -1.85, 0.42, -0.92, color=BLUE, lw=1.0, ms=9)
    ax.text(0, -3.35, "Kim la bàn chỉ hướng Bắc địa lí vì ở đó là cực NAM của “nam châm Trái Đất”.\n"
                      "Trục từ lệch khoảng 11,5° so với trục quay ⇒ có độ từ thiên.",
            fontsize=9.2, color=GREY, ha="center", va="center", style="italic")
    clean(ax, -3.2, 3.2, -3.8, 2.6)
    save(fig, "t_sd_tutruong_traidat")
    return _reg("t_sd_tutruong_traidat")


# ------------------------------------------------------------------ 5. quy tắc bàn tay trái
def t_sd_luctu():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    for xx in np.linspace(-2.3, 2.3, 9):
        for yy in np.linspace(-1.5, 1.5, 6):
            if abs(xx) < 0.32 and yy > 0:      # chừa chỗ cho mũi tên lực F
                continue
            ax.text(xx, yy, "×", color="#7f8c8d", fontsize=11, ha="center", va="center", zorder=1)
    ax.plot([-2.6, 2.6], [0, 0], color=BROWN, lw=4.0, solid_capstyle="round", zorder=4)
    arrow(ax, 0.4, 0, 1.5, 0, color=BROWN, lw=3.0, ms=16)
    ax.text(1.0, -0.28, "I", fontsize=14, color=BROWN, fontweight="bold", ha="center")
    arrow(ax, 0, 0, 0, 1.45, color=RED, lw=2.6, ms=17)
    ax.text(0.14, 1.5, r"$\vec{F}$", fontsize=15, color=RED, ha="left", va="bottom")
    ax.text(-2.85, 2.05, r"$\vec{B}$ hướng vào trong trang giấy", fontsize=10.8,
            color="#34495e", ha="left")
    ax.text(0, -2.05,
            "Quy tắc bàn tay trái: để đường sức từ xuyên vào lòng bàn tay, chiều từ cổ tay\n"
            "đến ngón giữa là chiều dòng điện, ngón cái choãi 90° chỉ chiều lực từ.",
            fontsize=9.3, color=GREY, ha="center", va="center")
    ax.text(4.05, 0.55, r"$F = BIl\sin\alpha$", fontsize=13, color=GREEN,
            ha="center", va="center")
    ax.text(4.05, 0.05, "α: góc giữa dây và B", fontsize=8.8, color=GREY, ha="center")
    clean(ax, -3.0, 5.6, -2.6, 2.35, eq=False)
    save(fig, "t_sd_luctu")
    return _reg("t_sd_luctu")


# ------------------------------------------------------------------ 6. dây hợp góc alpha với B
def t_sd_goc_alpha():
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    for y in (-1.1, -0.55, 0, 0.55, 1.1):
        ax.plot([-2.4, 2.4], [y, y], color="#95a5a6", lw=1.1, zorder=1)
        arrow(ax, 1.4, y, 1.95, y, color="#95a5a6", lw=1.1, ms=10)
    ax.text(-2.35, 1.35, r"$\vec{B}$", fontsize=14, color="#34495e", ha="left")
    a = np.deg2rad(35)
    L = 2.1
    ax.plot([-L * np.cos(a), L * np.cos(a)], [-L * np.sin(a), L * np.sin(a)],
            color=BROWN, lw=4.0, solid_capstyle="round", zorder=4)
    arrow(ax, 0.5 * np.cos(a), 0.5 * np.sin(a), 1.5 * np.cos(a), 1.5 * np.sin(a),
          color=BROWN, lw=2.6, ms=15)
    ax.text(1.05 * np.cos(a) - 0.18, 1.05 * np.sin(a) + 0.30, "I", fontsize=13,
            color=BROWN, fontweight="bold", ha="center")
    ax.add_patch(Arc((0, 0), 1.5, 1.5, theta1=0, theta2=35, color=RED, lw=1.6))
    ax.text(0.92, 0.18, r"$\alpha$", fontsize=13, color=RED)
    ax.text(0, -1.85, r"Chỉ thành phần vuông góc với dây mới gây ra lực từ: $F = BIl\sin\alpha$",
            fontsize=9.8, color=GREEN, ha="center")
    ax.text(0, -2.25, "α = 90° ⇒ F lớn nhất;   α = 0° (dây song song B) ⇒ F = 0",
            fontsize=9.4, color=GREY, ha="center")
    clean(ax, -2.6, 2.6, -2.5, 1.6, eq=False)
    save(fig, "t_sd_goc_alpha")
    return _reg("t_sd_goc_alpha")


# ------------------------------------------------------------------ 7. từ thông
def t_sd_tuthong():
    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    for y in (-1.25, -0.6, 0.05, 0.7, 1.35):
        ax.plot([-2.9, 1.1], [y, y], color="#95a5a6", lw=1.1)
        arrow(ax, 0.4, y, 0.95, y, color="#95a5a6", lw=1.1, ms=10)
    ax.text(-2.85, 1.62, r"$\vec{B}$", fontsize=14, color="#34495e", ha="left")
    th = np.deg2rad(60)
    cx = 1.45
    ax.add_patch(Ellipse((cx, 0.05), 1.05 * np.cos(np.pi / 2 - th) + 0.5, 2.1,
                         fill=False, ec=BROWN, lw=3.0))
    arrow(ax, cx, 0.05, cx + 1.25 * np.cos(np.pi / 2 - th), 0.05 + 1.25 * np.sin(np.pi / 2 - th),
          color=RED, lw=2.2, ms=15)
    ax.text(cx + 1.3 * np.cos(np.pi / 2 - th), 0.2 + 1.3 * np.sin(np.pi / 2 - th),
            r"$\vec{n}$", fontsize=14, color=RED, ha="left")
    ax.plot([cx, cx + 1.3], [0.05, 0.05], color=GREY, ls="--", lw=1.1)
    ax.add_patch(Arc((cx, 0.05), 1.3, 1.3, theta1=0, theta2=30, color=PURPLE, lw=1.6))
    ax.text(cx + 0.78, 0.22, r"$\theta$", fontsize=12.5, color=PURPLE)
    ax.text(cx, -1.55, "khung dây\ndiện tích S", fontsize=9.4, color=BROWN, ha="center", va="top")
    ax.text(-0.9, -2.25, r"$\Phi = BS\cos\theta$   (đơn vị: vêbe, Wb)", fontsize=12.5,
            color=GREEN, ha="center")
    ax.text(-0.9, -2.72, "θ = 0° ⇒ Φ lớn nhất;  θ = 90° (B nằm trong mặt phẳng khung) ⇒ Φ = 0",
            fontsize=9.2, color=GREY, ha="center")
    clean(ax, -3.1, 3.3, -3.0, 1.9, eq=False)
    save(fig, "t_sd_tuthong")
    return _reg("t_sd_tuthong")


# ------------------------------------------------------------------ 8. thí nghiệm Faraday
def t_sd_tn_faraday():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    # cuộn dây
    for x in np.linspace(-0.55, 0.55, 6):
        ax.add_patch(Ellipse((x, 0), 0.28, 1.5, fill=False, ec=BROWN, lw=2.2))
    ax.plot([-0.55, -1.15], [-0.75, -1.35], color=BROWN, lw=1.8)
    ax.plot([0.55, 1.15], [-0.75, -1.35], color=BROWN, lw=1.8)
    # điện kế
    ax.add_patch(Circle((0, -1.85), 0.46, fc="white", ec="#34495e", lw=1.8))
    ax.plot([-1.15, -0.4], [-1.35, -1.85], color=BROWN, lw=1.8)
    ax.plot([1.15, 0.4], [-1.35, -1.85], color=BROWN, lw=1.8)
    ax.text(0, -1.85, "G", fontsize=13, ha="center", va="center", color="#34495e",
            fontweight="bold")
    arrow(ax, 0, -1.85, 0.26, -1.62, color=RED, lw=1.5, ms=11)
    # nam châm chuyển động vào
    _bar_magnet(ax, -2.75, -0.28, 1.3, 0.56)
    arrow(ax, -1.3, 0, -0.75, 0, color=GREEN, lw=2.2, ms=15)
    ax.text(-1.02, 0.22, "v", fontsize=12, color=GREEN, fontweight="bold", ha="center")
    ax.text(-2.1, 0.85, "đưa nam châm LẠI GẦN", fontsize=9.6, color=GREEN, ha="center")
    ax.text(2.6, 0.6, "Kim điện kế lệch\n⇒ có dòng điện cảm ứng", fontsize=9.6,
            color=RED, ha="center", va="center")
    ax.text(2.6, -0.85, "Giữ nam châm ĐỨNG YÊN\n⇒ kim về 0, không có dòng",
            fontsize=9.6, color=GREY, ha="center", va="center")
    ax.text(0, 1.35, "Dòng điện cảm ứng chỉ xuất hiện khi TỪ THÔNG QUA MẠCH BIẾN THIÊN",
            fontsize=9.8, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.0, 4.3, -2.6, 1.7, eq=False)
    save(fig, "t_sd_tn_faraday")
    return _reg("t_sd_tn_faraday")


# ------------------------------------------------------------------ 9. định luật Lenz
def t_sd_lenz():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    for k, (lab, sgn, col, txt) in enumerate(
            [("Φ TĂNG", 1, RED, "dòng cảm ứng chống lại sự tăng\n⇒ B cảm ứng NGƯỢC chiều B"),
             ("Φ GIẢM", -1, BLUE, "dòng cảm ứng chống lại sự giảm\n⇒ B cảm ứng CÙNG chiều B")]):
        x0 = -1.85 + 3.7 * k
        dot_field(ax, x0 - 0.95, x0 + 0.95, -0.55, 0.75, n=5, m=4, color="#7f8c8d")
        ax.add_patch(Circle((x0, 0.1), 1.02, fill=False, ec=BROWN, lw=3.0))
        ax.text(x0, 1.55, lab, fontsize=11.5, color=col, ha="center", fontweight="bold")
        ax.text(x0 - 1.55, 1.55, r"$\vec{B}$ ra", fontsize=9.4, color="#34495e", ha="left")
        th = np.linspace(0.35, 1.95, 60) if sgn > 0 else np.linspace(1.95, 0.35, 60)
        ax.plot(x0 + 1.22 * np.cos(th), 0.1 + 1.22 * np.sin(th), color=col, lw=2.0)
        arrow(ax, x0 + 1.22 * np.cos(th[-2]), 0.1 + 1.22 * np.sin(th[-2]),
              x0 + 1.22 * np.cos(th[-1]), 0.1 + 1.22 * np.sin(th[-1]), color=col, lw=2.0, ms=14)
        ax.text(x0, -1.35, txt, fontsize=9.0, color=col, ha="center", va="center")
    ax.plot([0, 0], [-1.7, 1.75], color=LGREY, lw=1.0, ls="--")
    ax.text(0, -2.15, "Định luật Lenz: dòng điện cảm ứng có chiều sao cho từ trường nó sinh ra "
                      "CHỐNG LẠI nguyên nhân sinh ra nó",
            fontsize=9.6, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.3, 3.3, -2.4, 1.95, eq=False)
    save(fig, "t_sd_lenz")
    return _reg("t_sd_lenz")


# ------------------------------------------------------------------ 10. máy phát điện xoay chiều
def t_sd_may_phat():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.add_patch(Rectangle((-3.3, -1.3), 0.62, 2.6, fc="#e74c3c", ec="#7b241c", lw=1.4))
    ax.add_patch(Rectangle((0.55, -1.3), 0.62, 2.6, fc="#2e86c1", ec="#1b4f72", lw=1.4))
    ax.text(-2.99, 0, "N", color="white", fontsize=15, fontweight="bold", ha="center", va="center")
    ax.text(0.86, 0, "S", color="white", fontsize=15, fontweight="bold", ha="center", va="center")
    for y in (-0.9, -0.3, 0.3, 0.9):
        ax.plot([-2.68, 0.55], [y, y], color="#95a5a6", lw=1.0, zorder=1)
        arrow(ax, -0.6, y, -0.1, y, color="#95a5a6", lw=1.0, ms=9)
    ax.add_patch(Rectangle((-1.85, -0.72), 1.85, 1.44, fill=False, ec=BROWN, lw=2.8, zorder=4))
    ax.add_patch(Arc((-0.92, 0), 2.35, 1.85, theta1=200, theta2=340, color=GREEN, lw=1.6, zorder=5))
    arrow(ax, -0.02, -0.58, 0.13, -0.36, color=GREEN, lw=1.6, ms=12)
    ax.text(-0.92, -1.12, "ω", fontsize=13, color=GREEN, ha="center", fontweight="bold")
    for y in (0.17, -0.17):
        ax.plot([-1.85, -2.30], [y, y], color=BROWN, lw=1.6, zorder=5)
        ax.add_patch(Circle((-2.42, y), 0.13, fc="#f0c419", ec=BROWN, lw=1.2, zorder=6))
    ax.text(-2.42, -0.55, "vành khuyên\n+ chổi quét", fontsize=8.4, color="#7b4b1e",
            ha="center", va="top", zorder=7,
            bbox=dict(boxstyle="round,pad=0.16", fc="white", ec="none", alpha=0.92))
    # đồ thị e(t) bên phải
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot([1.75, 4.75], [0, 0], color=GREY, lw=1.0)
    ax.plot([1.75, 1.75], [-0.95, 0.95], color=GREY, lw=1.0)
    ax.plot(1.75 + t / (2 * np.pi) * 2.9, 0.8 * np.sin(t), color=RED, lw=2.0)
    ax.text(4.85, 0, "t", fontsize=10, color=GREY, ha="left", va="center")
    ax.text(1.68, 1.0, "e", fontsize=10, color=GREY, ha="right", va="bottom")
    ax.text(3.25, -1.35, "suất điện động\nbiến thiên điều hoà", fontsize=9.2, color=RED,
            ha="center", va="center")
    ax.text(-1.1, 1.95, "Khung dây quay đều trong từ trường ⇒ Φ biến thiên điều hoà\n"
                        "⇒ xuất hiện suất điện động xoay chiều",
            fontsize=9.6, color="#34495e", ha="center", fontweight="bold")
    clean(ax, -3.6, 5.2, -2.1, 2.45, eq=False)
    save(fig, "t_sd_may_phat")
    return _reg("t_sd_may_phat")


# ------------------------------------------------------------------ 11. u, i và giá trị hiệu dụng
def t_dt_u_i_hieudung():
    fig, ax = plt.subplots(figsize=(6.6, 3.7))
    t = np.linspace(0, 2.02, 500)
    u = 311 * np.cos(2 * np.pi * t)
    ax.plot(t, u, color=RED, lw=2.2, label="u(t)")
    ax.axhline(220, color=GREEN, ls="--", lw=1.5)
    ax.axhline(-220, color=GREEN, ls="--", lw=1.5)
    ax.axhline(0, color=GREY, lw=1.0)
    ax.text(2.03, 225, "U = 220 V (hiệu dụng)", fontsize=9.4, color=GREEN, ha="right", va="bottom")
    ax.text(0.02, 318, r"$U_0 = 311$ V", fontsize=9.6, color=RED, ha="left", va="bottom")
    ax.annotate("", xy=(0.5, 311), xytext=(0.5, 0),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.3))
    ax.text(0.55, 160, r"$U_0$", fontsize=11, color=PURPLE)
    ax.annotate("", xy=(0.0, -360), xytext=(1.0, -360),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.3))
    ax.text(0.5, -345, "T = 0,02 s", fontsize=9.4, color=BLUE, ha="center", va="bottom")
    frame(ax, (0, 2.1), (-400, 400), "t (chu kì)", "u (V)",
          xticks=[0, 0.5, 1, 1.5, 2], xticklabels=["0", "T/2", "T", "3T/2", "2T"],
          yticks=[-311, -220, 0, 220, 311])
    ax.text(1.35, 330, r"$U=\dfrac{U_0}{\sqrt{2}}$ ;  $I=\dfrac{I_0}{\sqrt{2}}$",
            fontsize=12, color=GREEN, ha="center", va="center")
    save(fig, "t_dt_u_i_hieudung")
    return _reg("t_dt_u_i_hieudung")


# ------------------------------------------------------------------ 12. dòng Foucault – phanh điện từ
def t_sd_dong_fuco():
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.add_patch(Rectangle((-2.6, -1.0), 2.3, 2.0, fc="#dfe6e9", ec="#636e72", lw=1.6))
    for r in (0.30, 0.52, 0.74):
        ax.add_patch(Circle((-1.45, 0), r, fill=False, ec=RED, lw=1.5))
        arrow(ax, -1.45 + r, 0.02, -1.45 + r * 0.94, 0.30, color=RED, lw=1.4, ms=11)
    ax.text(-1.45, -1.25, "dòng điện xoáy (Foucault)\nkhép kín trong khối kim loại",
            fontsize=9.0, color=RED, ha="center", va="top")
    cross_field(ax, -2.35, -0.55, -0.85, 0.85, n=5, m=4, color="#7f8c8d", size=10)
    arrow(ax, -0.2, 0, 0.75, 0, color=GREEN, lw=2.4, ms=16)
    ax.text(0.28, 0.22, "v", fontsize=12, color=GREEN, fontweight="bold", ha="center")
    arrow(ax, -0.2, -0.5, -1.15, -0.5, color=PURPLE, lw=2.4, ms=16)
    ax.text(-0.7, -0.75, "F cản", fontsize=10.5, color=PURPLE, ha="center")
    ax.text(1.35, 0.95,
            "Ứng dụng:\n• phanh điện từ trên tàu, xe tải\n• bếp từ làm nóng đáy nồi\n"
            "• lò nung cảm ứng\nTác hại: làm nóng lõi biến áp\n⇒ phải ghép từ nhiều lá mỏng cách điện",
            fontsize=9.2, color="#34495e", ha="left", va="top")
    clean(ax, -2.8, 4.6, -2.1, 1.5, eq=False)
    save(fig, "t_sd_dong_fuco")
    return _reg("t_sd_dong_fuco")


# ------------------------------------------------------------------ 13. bếp từ
def t_sd_bep_tu():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    ax.add_patch(Rectangle((-2.2, -1.15), 4.4, 0.95, fc="#2d3436", ec="#000000", lw=1.4))
    ax.add_patch(Rectangle((-2.2, -0.2), 4.4, 0.16, fc="#b2bec3", ec="#636e72", lw=1.2))
    ax.text(2.3, -0.68, "mặt kính\nceramic", fontsize=8.6, color=GREY, ha="left", va="center")
    for x in np.linspace(-1.5, 1.5, 9):
        ax.add_patch(Ellipse((x, -0.62), 0.2, 0.5, fill=False, ec=BROWN, lw=1.8))
    ax.text(-2.35, -0.62, "cuộn dây\ncao tần", fontsize=8.6, color=BROWN, ha="right", va="center")
    ax.add_patch(Rectangle((-1.7, -0.04), 3.4, 0.22, fc="#95a5a6", ec="#2d3436", lw=1.4))
    ax.add_patch(Rectangle((-1.7, 0.18), 3.4, 1.0, fc="#ecf0f1", ec="#2d3436", lw=1.6))
    ax.text(0, 0.68, "nồi có đáy nhiễm từ", fontsize=9.6, color="#2d3436", ha="center", va="center")
    for x in (-0.9, 0, 0.9):
        ax.add_patch(Circle((x, 0.07), 0.12, fill=False, ec=RED, lw=1.6))
    ax.text(0, -1.55, "Từ trường biến thiên ⇒ dòng Foucault trong đáy nồi ⇒ đáy nồi nóng lên.\n"
                      "Mặt kính và tay người không nóng vì không có dòng cảm ứng đáng kể.",
            fontsize=9.2, color="#34495e", ha="center", va="center")
    for k, x in enumerate((-1.2, 0, 1.2)):
        ax.plot([x, x], [0.25, 0.55], color=ORANGE, lw=1.4)
    ax.text(1.85, 0.95, "nhiệt toả ra\nngay tại đáy nồi", fontsize=8.8, color=ORANGE,
            ha="left", va="center")
    clean(ax, -3.2, 3.6, -2.0, 1.5, eq=False)
    save(fig, "t_sd_bep_tu")
    return _reg("t_sd_bep_tu")


# ------------------------------------------------------------------ 14. sạc không dây
def t_sd_sac_khong_day():
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.add_patch(Rectangle((-2.5, -1.1), 2.0, 0.75, fc="#dfe6e9", ec="#636e72", lw=1.5))
    ax.text(-1.5, -1.35, "đế sạc (cuộn sơ cấp)", fontsize=9.0, color=GREY, ha="center", va="top")
    for x in np.linspace(-2.2, -0.8, 6):
        ax.add_patch(Ellipse((x, -0.72), 0.16, 0.44, fill=False, ec=BROWN, lw=1.6))
    ax.add_patch(Rectangle((-2.5, 0.35), 2.0, 0.75, fc="#ecf0f1", ec="#2d3436", lw=1.5))
    ax.text(-1.5, 1.32, "điện thoại (cuộn thứ cấp)", fontsize=9.0, color="#2d3436", ha="center")
    for x in np.linspace(-2.2, -0.8, 6):
        ax.add_patch(Ellipse((x, 0.72), 0.16, 0.44, fill=False, ec=BROWN, lw=1.6))
    for x in (-2.0, -1.5, -1.0):
        arrow(ax, x, -0.35, x, 0.32, color=BLUE, lw=1.5, ms=12)
    ax.text(-1.5, 0.02, r"$\vec{B}$ biến thiên", fontsize=9.4, color=BLUE, ha="center",
            va="center", bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.93))
    ax.text(0.15, 0.95,
            "Không có dây nối, năng lượng truyền qua TỪ TRƯỜNG BIẾN THIÊN:\n"
            "• dòng xoay chiều ở cuộn sơ cấp tạo từ trường biến thiên\n"
            "• từ thông qua cuộn thứ cấp biến thiên ⇒ suất điện động cảm ứng\n"
            "• dòng cảm ứng nạp cho pin",
            fontsize=9.0, color="#34495e", ha="left", va="top")
    clean(ax, -2.8, 5.6, -1.8, 1.7, eq=False)
    save(fig, "t_sd_sac_khong_day")
    return _reg("t_sd_sac_khong_day")


# ------------------------------------------------------------------ 15. Φ(t) bậc thang → e(t)
def t_dt_phi_e():
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.3, 4.6), sharex=True,
                                 gridspec_kw=dict(hspace=0.16))
    tp = [0, 2, 4, 6, 8]
    fp = [0, 0.8, 0.8, 0.2, 0.2]
    a1.plot(tp, fp, color=BLUE, lw=2.4)
    a1.plot(tp, fp, "o", ms=6, mfc="white", mec=BLUE, mew=1.8)
    frame(a1, (0, 8.6), (-0.15, 1.05), "", "Φ (Wb)", xticks=[0, 2, 4, 6, 8],
          yticks=[0, 0.2, 0.8])
    a1.text(1.0, 0.92, "Φ tăng", fontsize=9.2, color=GREEN, ha="center")
    a1.text(3.0, 0.92, "Φ không đổi", fontsize=9.2, color=GREY, ha="center")
    a1.text(5.0, 0.92, "Φ giảm", fontsize=9.2, color=RED, ha="center")
    ep = [(0, 2, -0.4), (2, 4, 0.0), (4, 6, 0.3), (6, 8, 0.0)]
    for x1, x2, e in ep:
        a2.plot([x1, x2], [e, e], color=RED, lw=2.4)
        a2.plot([x1, x1], [0 if x1 == 0 else prev, e], color=RED, lw=1.2, ls=":")
        prev = e
    a2.axhline(0, color=GREY, lw=1.0)
    frame(a2, (0, 8.6), (-0.65, 0.55), "t (s)", "e (V)", xticks=[0, 2, 4, 6, 8],
          yticks=[-0.4, 0, 0.3])
    a2.text(4.3, -0.55, r"$e=-\dfrac{\Delta\Phi}{\Delta t}$ = trừ độ dốc của đồ thị Φ(t)",
            fontsize=10.5, color=GREEN, ha="center")
    save(fig, "t_dt_phi_e")
    return _reg("t_dt_phi_e")


ALL = [t_sd_duongsuc_ncthang, t_sd_duongsuc_daythang, t_sd_ongday, t_sd_tutruong_traidat,
       t_sd_luctu, t_sd_goc_alpha, t_sd_tuthong, t_sd_tn_faraday, t_sd_lenz,
       t_sd_may_phat, t_dt_u_i_hieudung, t_sd_dong_fuco, t_sd_bep_tu,
       t_sd_sac_khong_day, t_dt_phi_e]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
