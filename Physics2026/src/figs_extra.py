# -*- coding: utf-8 -*-
"""Hình dạy học bổ sung cho CHƯƠNG I (vật lí nhiệt) và CHƯƠNG II (khí lí tưởng)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, Polygon, FancyArrowPatch, Ellipse

from figbase import (save, arrow, clean, frame, hatch_ground, RED, BLUE, GREEN, ORANGE,
                     GREY, PURPLE, TEAL, BROWN, PINK, LGREY)
from figgen import flame, thermometer

MADE = []


def _reg(n):
    MADE.append(n)
    return n


# ------------------------------------------------------------------ CHƯƠNG I
def n_sd_luc_phan_tu():
    fig, ax = plt.subplots(figsize=(6.4, 3.7))
    r0 = 2 ** (1 / 6.0)
    r = np.linspace(0.93, 3.4, 500)
    F = 12 * (1.0 / r ** 13 - 1.0 / r ** 7)
    ax.plot(r, F, color=BLUE, lw=2.4)
    ax.axhline(0, color=GREY, lw=1.1)
    ax.plot([r0], [0], "o", ms=8, mfc="white", mec=RED, mew=2, zorder=5)
    ax.text(r0 + 0.06, 0.55, "r = r₀ : lực hút và lực đẩy\ncân bằng nhau, F = 0",
            fontsize=9.2, color=RED, ha="left", va="bottom")
    ax.text(1.02, 2.55, "r < r₀\nlực ĐẨY", fontsize=9.6, color=GREEN, ha="left",
            va="center", fontweight="bold")
    ax.text(2.55, -0.95, "r > r₀ : lực HÚT,\ncàng xa càng yếu", fontsize=9.6,
            color=PURPLE, ha="center", va="center", fontweight="bold")
    frame(ax, (0.9, 3.5), (-1.6, 4.0), "khoảng cách giữa hai phân tử  r",
          "lực tương tác  F", xticks=[r0], xticklabels=["r₀"], yticks=[0], grid=False)
    ax.text(2.95, 3.0, "Rắn:  r ≈ r₀, lực rất mạnh\nLỏng: r hơi lớn hơn r₀\n"
                       "Khí:  r ≫ r₀, lực ≈ 0",
            fontsize=9.2, color="#34495e", ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="#f4f6f8", ec=LGREY))
    save(fig, "n_sd_luc_phan_tu")
    return _reg("n_sd_luc_phan_tu")


def n_sd_quy_uoc_dau():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.add_patch(Rectangle((-0.95, -0.72), 1.9, 1.44, fc="#eaf2f8", ec="#2874a6", lw=2.0))
    ax.text(0, 0.12, "VẬT", fontsize=14, color="#1b4f72", ha="center", va="center",
            fontweight="bold")
    ax.text(0, -0.28, "nội năng U", fontsize=10.5, color="#1b4f72", ha="center", va="center")
    arrow(ax, -2.45, 0.42, -1.0, 0.42, color=GREEN, lw=2.4, ms=16)
    ax.text(-2.5, 0.42, "A > 0", fontsize=12, color=GREEN, ha="right", va="center",
            fontweight="bold")
    ax.text(-1.72, 0.62, "nhận công", fontsize=9.2, color=GREEN, ha="center")
    arrow(ax, -1.0, -0.42, -2.45, -0.42, color=RED, lw=2.4, ms=16)
    ax.text(-2.5, -0.42, "A < 0", fontsize=12, color=RED, ha="right", va="center",
            fontweight="bold")
    ax.text(-1.72, -0.70, "sinh công", fontsize=9.2, color=RED, ha="center", va="top")
    arrow(ax, 2.45, 0.42, 1.0, 0.42, color=GREEN, lw=2.4, ms=16)
    ax.text(2.5, 0.42, "Q > 0", fontsize=12, color=GREEN, ha="left", va="center",
            fontweight="bold")
    ax.text(1.72, 0.62, "thu nhiệt", fontsize=9.2, color=GREEN, ha="center")
    arrow(ax, 1.0, -0.42, 2.45, -0.42, color=RED, lw=2.4, ms=16)
    ax.text(2.5, -0.42, "Q < 0", fontsize=12, color=RED, ha="left", va="center",
            fontweight="bold")
    ax.text(1.72, -0.70, "toả nhiệt", fontsize=9.2, color=RED, ha="center", va="top")
    ax.text(0, 1.62, "QUY ƯỚC DẤU — mũi tên hướng VÀO vật thì đại lượng DƯƠNG",
            fontsize=10.5, color="#34495e", ha="center", fontweight="bold")
    ax.text(0, -1.55, r"$\Delta U = A + Q$", fontsize=15, color=GREEN, ha="center")
    ax.text(0, -2.05, "ΔU > 0: nội năng tăng (thường kèm nhiệt độ tăng)", fontsize=9.2,
            color=GREY, ha="center")
    clean(ax, -4.2, 4.2, -2.4, 2.0, eq=False)
    save(fig, "n_sd_quy_uoc_dau")
    return _reg("n_sd_quy_uoc_dau")


def n_sd_cong_cua_khi():
    fig, ax = plt.subplots(figsize=(6.6, 3.3))
    for k, (lab, col, dx, note) in enumerate(
            [("KHÍ BỊ NÉN", GREEN, -0.55, "Pit-tông đi vào, V giảm\nKhí NHẬN công:  A > 0"),
             ("KHÍ GIÃN NỞ", RED, 0.55, "Pit-tông đi ra, V tăng\nKhí SINH công:  A < 0")]):
        x0 = -3.3 + 3.55 * k
        ax.add_patch(Rectangle((x0, -0.75), 2.55, 1.5, fc="white", ec="#444444", lw=1.8))
        gw = 1.55 if k == 0 else 1.05
        ax.add_patch(Rectangle((x0, -0.75), gw, 1.5, fc="#d8e8f8", ec="none"))
        ax.add_patch(Rectangle((x0 + gw, -0.75), 0.16, 1.5, fc="#9aa5b1", ec="#5a6470", lw=1.2))
        ax.text(x0 + gw / 2, 0, "khí", fontsize=10.5, color=BLUE, ha="center", va="center")
        arrow(ax, x0 + gw + 0.75, 0, x0 + gw + 0.30 + (0 if k == 0 else 0.9), 0,
              color=col, lw=2.2, ms=15)
        if k == 1:
            arrow(ax, x0 + gw + 0.30, 0, x0 + gw + 1.20, 0, color=col, lw=2.2, ms=15)
        ax.text(x0 + 1.28, 1.05, lab, fontsize=11, color=col, ha="center", fontweight="bold")
        ax.text(x0 + 1.28, -1.05, note, fontsize=9.4, color="#34495e", ha="center", va="top")
    ax.text(0.1, 2.0, "Công mà khí trao đổi với bên ngoài khi thể tích thay đổi",
            fontsize=10.5, color="#34495e", ha="center", fontweight="bold")
    ax.text(0.1, -2.15, "Nếu thể tích KHÔNG đổi (bình kín, thành cứng) thì A = 0 dù áp suất có thay đổi",
            fontsize=9.4, color=PURPLE, ha="center", style="italic")
    clean(ax, -3.6, 3.9, -2.5, 2.3, eq=False)
    save(fig, "n_sd_cong_cua_khi")
    return _reg("n_sd_cong_cua_khi")


def n_sd_bayhoi_soi():
    fig, ax = plt.subplots(figsize=(6.6, 3.3))
    for k, (tit, col, x0) in enumerate([("SỰ BAY HƠI", TEAL, -3.2), ("SỰ SÔI", RED, 0.45)]):
        ax.add_patch(Rectangle((x0, -1.0), 2.4, 1.55, fc="white", ec="#444444", lw=1.6))
        ax.add_patch(Rectangle((x0, -1.0), 2.4, 1.0, fc="#d6eaf8", ec="none"))
        ax.plot([x0, x0 + 2.4], [0, 0], color="#2874a6", lw=1.4)
        rng = np.random.default_rng(4 + k)
        if k == 0:
            for _ in range(7):
                xx = x0 + rng.uniform(0.2, 2.2)
                arrow(ax, xx, 0.05, xx + rng.uniform(-0.12, 0.12), rng.uniform(0.55, 1.05),
                      color=TEAL, lw=1.1, ms=9)
        else:
            for _ in range(16):
                xx, yy = x0 + rng.uniform(0.15, 2.25), rng.uniform(-0.92, -0.08)
                ax.add_patch(Circle((xx, yy), rng.uniform(0.05, 0.11), fill=False,
                                    ec="#2874a6", lw=1.1))
            for _ in range(5):
                xx = x0 + rng.uniform(0.3, 2.1)
                arrow(ax, xx, 0.05, xx, rng.uniform(0.6, 1.1), color=RED, lw=1.1, ms=9)
            flame(ax, x0 + 0.5, x0 + 1.9, -1.55, n=4)
        ax.text(x0 + 1.2, 1.45, tit, fontsize=11.5, color=col, ha="center", fontweight="bold")
    ax.text(-2.0, -1.95, "• xảy ra ở MỌI nhiệt độ\n• chỉ trên MẶT THOÁNG\n"
                         "• càng nhanh khi nóng, gió,\n  mặt thoáng rộng",
            fontsize=9.2, color="#34495e", ha="center", va="top")
    ax.text(1.65, -1.95, "• chỉ ở NHIỆT ĐỘ SÔI xác định\n• xảy ra cả trong LÒNG chất lỏng\n"
                         "• trong khi sôi, nhiệt độ\n  KHÔNG đổi",
            fontsize=9.2, color="#34495e", ha="center", va="top")
    ax.text(-0.35, 2.25, "Hai hình thức hoá hơi", fontsize=11, color="#34495e",
            ha="center", fontweight="bold")
    clean(ax, -3.5, 3.2, -3.4, 2.5, eq=False)
    save(fig, "n_sd_bayhoi_soi")
    return _reg("n_sd_bayhoi_soi")


def n_sd_tn_do_c():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    ax.add_patch(Rectangle((-1.7, -1.25), 3.0, 2.1, fc="#f2f4f4", ec="#566573", lw=2.0))
    ax.add_patch(Rectangle((-1.48, -1.05), 2.56, 1.60, fc="#d6eaf8", ec="#2874a6", lw=1.2))
    ax.text(-0.20, -0.78, "nước khối lượng m", fontsize=9.4, color="#1b4f72", ha="center")
    ax.add_patch(Rectangle((-1.05, -0.22), 1.05, 0.20, fc="#e59866", ec="#935116", lw=1.2))
    ax.text(-1.62, -0.12, "điện trở đun", fontsize=8.8, color="#935116", ha="right",
            va="center")
    arrow(ax, -1.60, -0.12, -1.10, -0.12, color="#935116", lw=1.0, ms=9)
    thermometer(ax, 0.78, 1.45, 0.05, c=GREEN)
    ax.text(1.05, 1.40, "nhiệt kế", fontsize=8.8, color=GREEN, ha="left", va="center")
    ax.text(-1.75, -1.45, "bình cách nhiệt", fontsize=8.8, color="#566573", ha="left", va="top")
    ax.plot([-0.85, -0.85], [-0.02, 1.30], color=BROWN, lw=1.5)
    ax.plot([-0.20, -0.20], [-0.02, 1.30], color=BROWN, lw=1.5)
    ax.add_patch(Rectangle((-1.32, 1.30), 0.90, 0.42, fc="white", ec="#34495e", lw=1.3))
    ax.text(-0.87, 1.51, "A", fontsize=11, color="#34495e", ha="center", va="center")
    ax.add_patch(Rectangle((-0.63, 1.30), 0.90, 0.42, fc="white", ec="#34495e", lw=1.3))
    ax.text(-0.18, 1.51, "V", fontsize=11, color="#34495e", ha="center", va="center")
    ax.text(1.85, 1.55, "Cách làm:", fontsize=10.5, color="#34495e", fontweight="bold",
            ha="left", va="top")
    ax.text(1.85, 1.20, "① Cân để có khối lượng m\n② Đọc U, I; bấm giờ t\n"
                        "③ Đọc độ tăng nhiệt độ ΔT\n④ Nhiệt lượng cấp:  Q = U·I·t",
            fontsize=9.4, color="#34495e", ha="left", va="top")
    ax.text(3.15, -0.75, r"$c=\dfrac{U I t}{m\,\Delta T}$", fontsize=15, color=GREEN,
            ha="center", va="center")
    ax.text(-0.2, -2.05, "Sai số chính: nhiệt toả ra môi trường và nhiệt mà bình thu vào\n"
                         "⇒ giá trị c đo được thường LỚN hơn giá trị thực.",
            fontsize=9.2, color=PURPLE, ha="center", va="top", style="italic")
    clean(ax, -2.2, 5.0, -2.7, 2.0, eq=False)
    save(fig, "n_sd_tn_do_c")
    return _reg("n_sd_tn_do_c")


def n_sd_can_bang_nhiet():
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.add_patch(Rectangle((-3.0, -0.7), 2.0, 1.4, fc="#fadbd8", ec="#c0392b", lw=1.8))
    ax.text(-2.0, 0.18, "VẬT NÓNG", fontsize=10.5, color="#7b241c", ha="center",
            fontweight="bold")
    ax.text(-2.0, -0.25, "m₁, c₁, t₁", fontsize=11, color="#7b241c", ha="center")
    ax.add_patch(Rectangle((1.0, -0.7), 2.0, 1.4, fc="#d6eaf8", ec="#2874a6", lw=1.8))
    ax.text(2.0, 0.18, "VẬT LẠNH", fontsize=10.5, color="#1b4f72", ha="center",
            fontweight="bold")
    ax.text(2.0, -0.25, "m₂, c₂, t₂", fontsize=11, color="#1b4f72", ha="center")
    arrow(ax, -0.92, 0.35, 0.92, 0.35, color=ORANGE, lw=2.6, ms=17)
    ax.text(0, 0.88, "nhiệt truyền từ vật nóng sang vật lạnh", fontsize=9.2,
            color=ORANGE, ha="center")
    ax.text(0, -0.42, "cho tới khi hai vật\ncùng nhiệt độ t", fontsize=9.0, color=GREY,
            ha="center", va="top")
    ax.text(0, -1.30, r"$Q_{toa} = Q_{thu}$", fontsize=14, color=GREEN, ha="center")
    ax.text(0, -1.90, r"$m_1c_1(t_1-t) = m_2c_2(t-t_2)$", fontsize=13, color=GREEN, ha="center")
    ax.text(0, 1.35, "PHƯƠNG TRÌNH CÂN BẰNG NHIỆT (bình cách nhiệt lí tưởng)",
            fontsize=10.5, color="#34495e", ha="center", fontweight="bold")
    ax.text(0, -2.45, "Luôn kiểm tra:  t₂ < t < t₁ .  Nếu kết quả nằm ngoài khoảng đó thì đã sai dấu.",
            fontsize=9.2, color=PURPLE, ha="center", style="italic")
    clean(ax, -3.3, 3.3, -2.8, 1.7, eq=False)
    save(fig, "n_sd_can_bang_nhiet")
    return _reg("n_sd_can_bang_nhiet")


def n_sd_hieu_suat():
    fig, ax = plt.subplots(figsize=(6.8, 3.0))
    ax.add_patch(Rectangle((-3.55, -1.00), 1.05, 2.00, fc="#fdebd0", ec="#ca6f1e", lw=1.6))
    ax.text(-3.02, 0, "BẾP\ncung cấp", fontsize=9.4, color="#7e5109", ha="center",
            va="center", fontweight="bold")
    ax.text(-3.02, -1.18, r"$Q_{tp}$", fontsize=12, color="#7e5109", ha="center", va="top")
    ax.add_patch(Polygon([(-2.45, 1.00), (0.75, 0.62), (0.75, 0.02), (-2.45, -0.10)],
                         fc="#d5f5e3", ec="#1e8449", lw=1.4))
    ax.text(-0.85, 0.44, "nhiệt nước thực sự nhận", fontsize=9.4, color="#145a32",
            ha="center", va="center")
    ax.text(0.95, 0.32, r"$Q_{ci}$", fontsize=12, color="#145a32", ha="left", va="center")
    ax.add_patch(Polygon([(-2.45, -0.18), (0.75, -0.06), (0.75, -0.62), (-2.45, -1.00)],
                         fc="#fadbd8", ec="#c0392b", lw=1.4))
    ax.text(-0.85, -0.52, "hao phí: nóng nồi, toả ra không khí", fontsize=9.0,
            color="#7b241c", ha="center", va="center")
    ax.text(2.75, 0.45, r"$H=\dfrac{Q_{ci}}{Q_{tp}}$", fontsize=15, color=GREEN,
            ha="center", va="center")
    ax.text(2.75, -0.55, "Q có ích = m·c·ΔT\n(hoặc m·λ, m·L khi chuyển thể)",
            fontsize=9.0, color=GREY, ha="center", va="center")
    ax.text(-0.35, 1.55, "HIỆU SUẤT CỦA QUÁ TRÌNH ĐUN NÓNG", fontsize=11,
            color="#34495e", ha="center", fontweight="bold")
    ax.text(-0.35, -1.70, "Bẫy: đề cho H rồi hỏi nhiệt lượng bếp phải cung cấp — phải CHIA cho H, không nhân.",
            fontsize=9.2, color=PURPLE, ha="center", style="italic")
    clean(ax, -3.8, 4.3, -2.1, 1.9, eq=False)
    save(fig, "n_sd_hieu_suat")
    return _reg("n_sd_hieu_suat")


# ------------------------------------------------------------------ CHƯƠNG II
def k_sd_brown():
    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    rng = np.random.default_rng(11)
    pts = [(0.0, 0.0)]
    for _ in range(9):
        a = rng.uniform(0, 2 * np.pi)
        L = rng.uniform(0.35, 0.72)
        pts.append((pts[-1][0] + L * np.cos(a), pts[-1][1] + L * np.sin(a)))
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=RED, lw=1.8, marker="o", ms=5, mfc="white", mec=RED, zorder=5)
    ax.add_patch(Circle(pts[0], 0.17, fc="#f5b7b1", ec=RED, lw=1.4, zorder=6))
    ax.text(xs[0] - 0.28, ys[0] - 0.22, "hạt phấn hoa", fontsize=9.0, color=RED,
            ha="right", va="top")
    for _ in range(60):
        x, y = rng.uniform(-2.2, 2.2), rng.uniform(-1.5, 1.6)
        ax.plot([x], [y], "o", ms=2.4, color="#85929e", zorder=1)
    ax.text(2.55, 1.25, "Các phân tử nước (chấm nhỏ)\nchuyển động hỗn loạn, va chạm\n"
                        "vào hạt phấn hoa từ mọi phía.",
            fontsize=9.2, color="#34495e", ha="left", va="top")
    ax.text(2.55, -0.15, "Số va chạm các phía không\ncân bằng nhau ⇒ hạt bị đẩy\n"
                         "theo đường gấp khúc ngẫu nhiên.",
            fontsize=9.2, color="#34495e", ha="left", va="top")
    ax.text(2.55, -1.35, "Nhiệt độ càng cao,\nchuyển động Brown càng mạnh.",
            fontsize=9.2, color=GREEN, ha="left", va="top")
    ax.add_patch(Rectangle((-2.45, -1.75), 4.9, 3.55, fill=False, ec=LGREY, lw=1.2))
    clean(ax, -2.6, 6.6, -2.0, 2.0, eq=False)
    save(fig, "k_sd_brown")
    return _reg("k_sd_brown")


def k_sd_vacham_thanh():
    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.add_patch(Rectangle((-2.6, -1.5), 3.4, 3.0, fc="#eef7fb", ec="#2874a6", lw=2.4))
    rng = np.random.default_rng(21)
    for _ in range(14):
        x, y = rng.uniform(-2.45, 0.6), rng.uniform(-1.35, 1.35)
        a = rng.uniform(0, 2 * np.pi)
        ax.plot([x], [y], "o", ms=5, color="#2874a6", zorder=4)
        arrow(ax, x, y, x + 0.34 * np.cos(a), y + 0.34 * np.sin(a), color="#5499c7",
              lw=1.0, ms=8)
    for y in (0.85, 0.1, -0.75):
        ax.plot([0.2, 0.78], [y + 0.20, y], color=RED, lw=1.6)
        ax.plot([0.78, 0.2], [y, y - 0.20], color=RED, lw=1.6)
        arrow(ax, 0.60, y - 0.13, 0.24, y - 0.26, color=RED, lw=1.4, ms=10)
        arrow(ax, 0.82, y, 1.20, y, color=PURPLE, lw=1.8, ms=13)
    ax.text(1.30, 0.10, "mỗi va chạm truyền\ncho thành bình một xung lượng",
            fontsize=9.2, color=PURPLE, ha="left", va="center")
    ax.text(1.30, -1.05, "Tổng của rất nhiều va chạm\n⇒ ÁP SUẤT chất khí",
            fontsize=9.4, color=RED, ha="left", va="center", fontweight="bold")
    ax.text(-0.95, 1.95, "ÁP SUẤT KHÍ SINH RA TỪ VA CHẠM CỦA PHÂN TỬ VÀO THÀNH BÌNH",
            fontsize=9.8, color="#34495e", ha="center", fontweight="bold")
    ax.text(-0.95, -2.05, r"$p=\dfrac{1}{3}\mu m_0 \overline{v^{2}} = \dfrac{2}{3}\mu \overline{W_{d}}$",
            fontsize=13, color=GREEN, ha="center", va="center")
    clean(ax, -2.8, 5.6, -2.6, 2.3, eq=False)
    save(fig, "k_sd_vacham_thanh")
    return _reg("k_sd_vacham_thanh")


def k_dt_phan_bo_toc_do():
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    v = np.linspace(0, 2600, 500)
    for T, c, lab in ((300, BLUE, "T = 300 K"), (600, ORANGE, "T = 600 K"),
                      (1200, RED, "T = 1200 K")):
        a = 1.0 / (2 * 8.314 * T / 0.032)
        f = v ** 2 * np.exp(-a * v ** 2)
        ax.plot(v, f / f.max() * (300.0 / T) ** 0.5, color=c, lw=2.2, label=lab)
    frame(ax, (0, 2600), (0, 1.10), "tốc độ phân tử v (m/s)", "số phân tử (tương đối)",
          xticks=[0, 500, 1000, 1500, 2000, 2500], yticks=[], grid=True)
    ax.legend(fontsize=9, loc="upper right", framealpha=0.9)
    ax.text(1350, 0.62, "Nhiệt độ tăng ⇒ đỉnh dịch\nsang phải và thấp xuống:\n"
                        "phân tử chuyển động nhanh hơn,\ndải tốc độ trải rộng hơn.",
            fontsize=9.2, color="#34495e", ha="left", va="top")
    ax.text(1350, 0.14, r"$\overline{W_{d}}=\dfrac{3}{2}kT$", fontsize=13, color=GREEN,
            ha="left", va="center")
    save(fig, "k_dt_phan_bo_toc_do")
    return _reg("k_dt_phan_bo_toc_do")


def k_dt_ba_he_truc():
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 2.9))
    # đẳng nhiệt
    a = axes[0]
    for T, c, ls in ((1.0, BLUE, "-"), (1.6, RED, "--")):
        V = np.linspace(0.55, 3.0, 200)
        a.plot(V, T / V, color=c, lw=2.2, ls=ls)
    a.text(2.0, 1.35, "T₂ > T₁", fontsize=9, color=RED)
    a.text(1.75, 0.40, "T₁", fontsize=9, color=BLUE)
    frame(a, (0, 3.2), (0, 2.2), "V", "p", xticks=[], yticks=[], grid=False)
    a.set_title("Đẳng nhiệt  (p ~ 1/V)", fontsize=10, color="#34495e", pad=6)
    # đẳng tích
    a = axes[1]
    T = np.linspace(0, 3.0, 100)
    for k, c, ls in ((0.62, BLUE, "-"), (0.34, RED, "--")):
        a.plot(T, k * T, color=c, lw=2.2, ls=ls)
    a.text(2.25, 1.95, "V₁", fontsize=9, color=BLUE)
    a.text(2.55, 0.98, "V₂ > V₁", fontsize=9, color=RED)
    frame(a, (0, 3.2), (0, 2.2), "T (K)", "p", xticks=[], yticks=[], grid=False)
    a.set_title("Đẳng tích  (p ~ T)", fontsize=10, color="#34495e", pad=6)
    # đẳng áp
    a = axes[2]
    for k, c, ls in ((0.62, BLUE, "-"), (0.34, RED, "--")):
        a.plot(T, k * T, color=c, lw=2.2, ls=ls)
    a.text(2.25, 1.95, "p₁", fontsize=9, color=BLUE)
    a.text(2.55, 0.98, "p₂ > p₁", fontsize=9, color=RED)
    frame(a, (0, 3.2), (0, 2.2), "T (K)", "V", xticks=[], yticks=[], grid=False)
    a.set_title("Đẳng áp  (V ~ T)", fontsize=10, color="#34495e", pad=6)
    fig.text(0.5, -0.03, "Đường đẳng nhiệt trong hệ (p, V) là hypebol;  trong hệ (p, T) và (V, T) "
                         "các đường đẳng tích / đẳng áp là ĐƯỜNG THẲNG QUA GỐC toạ độ.",
             fontsize=9.2, color=GREY, ha="center")
    fig.tight_layout()
    save(fig, "k_dt_ba_he_truc")
    return _reg("k_dt_ba_he_truc")


def k_sd_ba_trang_thai():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    boxes = [(-3.25, "TRẠNG THÁI 1", "p₁ , V₁ , T₁", BLUE),
             (-0.55, "TRẠNG THÁI 2", "p₂ , V₂ , T₂", GREEN)]
    for x, t1, t2, c in boxes:
        ax.add_patch(Rectangle((x, -0.55), 2.2, 1.25, fc="#fbfbfb", ec=c, lw=1.8))
        ax.text(x + 1.1, 0.36, t1, fontsize=10, color=c, ha="center", fontweight="bold")
        ax.text(x + 1.1, -0.12, t2, fontsize=12, color="#34495e", ha="center")
    arrow(ax, -0.95, 0.08, -0.6, 0.08, color=ORANGE, lw=2.2, ms=15)
    ax.text(3.35, 0.30, r"$\dfrac{p_1V_1}{T_1}=\dfrac{p_2V_2}{T_2}$", fontsize=15,
            color=GREEN, ha="center", va="center")
    ax.text(3.35, -0.62, "T luôn tính bằng KELVIN", fontsize=9.4, color=RED, ha="center")
    ax.text(-0.3, 1.30, "PHƯƠNG TRÌNH TRẠNG THÁI KHÍ LÍ TƯỞNG",
            fontsize=11, color="#34495e", ha="center", fontweight="bold")
    ax.text(-0.3, -1.25, "Ba định luật Boyle, Charles, Gay-Lussac đều là trường hợp riêng: "
                         "giữ nguyên một đại lượng rồi rút gọn.",
            fontsize=9.2, color=GREY, ha="center", style="italic")
    ax.text(-0.3, -1.68, "T (K) = t (°C) + 273", fontsize=10.5, color=PURPLE, ha="center")
    clean(ax, -3.5, 5.1, -2.0, 1.7, eq=False)
    save(fig, "k_sd_ba_trang_thai")
    return _reg("k_sd_ba_trang_thai")


ALL = [n_sd_luc_phan_tu, n_sd_quy_uoc_dau, n_sd_cong_cua_khi, n_sd_bayhoi_soi,
       n_sd_tn_do_c, n_sd_can_bang_nhiet, n_sd_hieu_suat,
       k_sd_brown, k_sd_vacham_thanh, k_dt_phan_bo_toc_do, k_dt_ba_he_truc,
       k_sd_ba_trang_thai]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
