# -*- coding: utf-8 -*-
"""Sinh toàn bộ hình vẽ gốc cho tài liệu Vật lí 12 - Chương I và Chương II (học kì I)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Rectangle, Circle, FancyArrowPatch, Polygon,
                                FancyBboxPatch, Arc, Ellipse)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

RED, BLUE, GREEN, ORANGE, GREY = "#c0392b", "#1f4e9c", "#1e8449", "#d35400", "#555555"
PURPLE, TEAL = "#6c3483", "#117a65"


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


def axes_xy(ax, xlab, ylab, xmax=1.0, ymax=1.0, lw=1.5):
    """Vẽ hệ trục Ox, Oy dạng mũi tên trong hệ toạ độ dữ liệu 0..1."""
    arrow(ax, 0, 0, xmax, 0, color="k", lw=lw, ms=11)
    arrow(ax, 0, 0, 0, ymax, color="k", lw=lw, ms=11)
    ax.text(xmax, -0.055 * ymax, xlab, ha="right", va="top", fontsize=11)
    ax.text(-0.02 * xmax, ymax, ylab, ha="right", va="top", fontsize=11)
    ax.text(-0.02 * xmax, -0.03 * ymax, "O", ha="right", va="top", fontsize=10)


# ===================================================================
#                       CHƯƠNG I - VẬT LÍ NHIỆT
# ===================================================================

def f01_cau_truc_chat():
    """Mô hình phân tử của chất rắn, chất lỏng, chất khí."""
    fig, axs = plt.subplots(1, 3, figsize=(9.4, 3.5))
    rng = np.random.RandomState(7)

    # --- chất rắn: mạng tinh thể trật tự
    ax = axs[0]
    for i in range(5):
        for j in range(5):
            x, y = i * 0.9, j * 0.9
            ax.add_patch(Circle((x, y), 0.28, fc="#aed6f1", ec=BLUE, lw=1.2, zorder=3))
            if i < 4:
                ax.plot([x + 0.28, x + 0.62], [y, y], color=GREY, lw=1.0, ls="-", zorder=1)
            if j < 4:
                ax.plot([x, x], [y + 0.28, y + 0.62], color=GREY, lw=1.0, ls="-", zorder=1)
    for (i, j) in [(1, 3), (3, 1)]:
        x, y = i * 0.9, j * 0.9
        th = np.linspace(0, 2 * np.pi, 60)
        ax.plot(x + 0.44 * np.cos(th), y + 0.44 * np.sin(th), color=RED, lw=0.9, ls=":")
    ax.set_title("CHẤT RẮN", fontsize=11.5, fontweight="bold", color=BLUE, pad=8)
    ax.text(1.8, -0.95, "Trật tự xa, phân tử chỉ\ndao động quanh vị trí cân bằng",
            ha="center", va="top", fontsize=9.2)
    clean(ax, -0.6, 4.2, -1.9, 4.3)

    # --- chất lỏng: sát nhau nhưng mất trật tự xa
    ax = axs[1]
    pts = []
    for i in range(5):
        for j in range(5):
            x = i * 0.9 + rng.uniform(-0.26, 0.26)
            y = j * 0.85 + rng.uniform(-0.24, 0.24)
            pts.append((x, y))
    for (x, y) in pts:
        ax.add_patch(Circle((x, y), 0.27, fc="#a9dfbf", ec=GREEN, lw=1.2, zorder=3))
    for (x, y) in pts[::4]:
        a = rng.uniform(0, 2 * np.pi)
        arrow(ax, x, y, x + 0.62 * np.cos(a), y + 0.62 * np.sin(a),
              color=RED, lw=1.3, ms=9, zorder=6)
    ax.plot([-0.5, 4.1], [-0.75, -0.75], color=GREY, lw=2.2)
    ax.plot([-0.5, -0.5], [-0.75, 4.2], color=GREY, lw=2.2)
    ax.plot([4.1, 4.1], [-0.75, 4.2], color=GREY, lw=2.2)
    ax.set_title("CHẤT LỎNG", fontsize=11.5, fontweight="bold", color=GREEN, pad=8)
    ax.text(1.8, -1.05, "Phân tử vẫn sát nhau nhưng\ncó thể trượt lên nhau → chảy được",
            ha="center", va="top", fontsize=9.2)
    clean(ax, -0.9, 4.5, -1.9, 4.3)

    # --- chất khí: rất xa nhau, chuyển động hỗn loạn
    ax = axs[2]
    gx = rng.uniform(-0.2, 3.8, 13)
    gy = rng.uniform(-0.5, 3.9, 13)
    for x, y in zip(gx, gy):
        ax.add_patch(Circle((x, y), 0.20, fc="#f5b7b1", ec=RED, lw=1.2, zorder=3))
        a = rng.uniform(0, 2 * np.pi)
        arrow(ax, x, y, x + 0.75 * np.cos(a), y + 0.75 * np.sin(a), color=GREY, lw=1.0, ms=8)
    ax.add_patch(Rectangle((-0.7, -0.9), 5.0, 5.1, fill=False, ec=GREY, lw=2.2))
    ax.set_title("CHẤT KHÍ", fontsize=11.5, fontweight="bold", color=RED, pad=8)
    ax.text(1.8, -1.15, "Khoảng cách rất lớn so với kích thước\nphân tử; chuyển động hỗn loạn",
            ha="center", va="top", fontsize=9.2)
    clean(ax, -1.0, 4.6, -2.1, 4.3)

    fig.subplots_adjust(wspace=0.08)
    save(fig, "h01_cau_truc_chat")


def f02_the_nang_tuong_tac():
    """Lực và thế năng tương tác phân tử theo khoảng cách."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    r = np.linspace(0.92, 3.4, 400)
    r0 = 1.0
    U = 4 * ((r0 / r) ** 12 - (r0 / r) ** 6)
    ax.plot(r, U, color=BLUE, lw=2.2, label="Thế năng tương tác $E_t$")
    ax.axhline(0, color="k", lw=1.0)
    rmin = r0 * 2 ** (1 / 6)
    ax.plot([rmin], [-1.0], "o", color=RED, ms=7, zorder=5)
    ax.annotate("$r = r_0$: lực tương tác bằng 0,\nthế năng cực tiểu → vị trí cân bằng",
                xy=(rmin, -1.0), xytext=(1.75, -0.55), fontsize=9.4, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.annotate("$r < r_0$: đẩy nhau mạnh\n(khó nén chất rắn, chất lỏng)",
                xy=(1.02, 1.6), xytext=(1.15, 2.35), fontsize=9.4, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.annotate("$r > r_0$: hút nhau, lực giảm\nnhanh khi $r$ tăng",
                xy=(2.35, -0.16), xytext=(2.05, 1.15), fontsize=9.4, color=ORANGE,
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
    ax.set_xlabel("Khoảng cách giữa hai phân tử  $r$", fontsize=10.5)
    ax.set_ylabel("Thế năng tương tác  $E_t$", fontsize=10.5)
    ax.set_xlim(0.9, 3.4); ax.set_ylim(-1.5, 3.0)
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.25, ls=":")
    save(fig, "h02_the_nang_tuong_tac")


def f03_so_do_chuyen_the():
    """Sơ đồ sáu quá trình chuyển thể kèm chiều thu/toả nhiệt."""
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    boxes = {"RẮN": (0.9, 0.9, "#aed6f1", BLUE),
             "LỎNG": (4.2, 0.9, "#a9dfbf", GREEN),
             "KHÍ (HƠI)": (7.5, 0.9, "#f5b7b1", RED)}
    for name, (x, y, fc, ec) in boxes.items():
        ax.add_patch(FancyBboxPatch((x - 0.85, y - 0.42), 1.7, 0.84,
                                    boxstyle="round,pad=0.06", fc=fc, ec=ec, lw=1.8))
        ax.text(x, y, name, ha="center", va="center", fontsize=11.5, fontweight="bold", color=ec)

    def pair(x1, x2, up_lbl, dn_lbl, y=0.9):
        arrow(ax, x1 + 0.9, y + 0.15, x2 - 0.9, y + 0.15, color=RED, lw=1.7, ms=13)
        arrow(ax, x2 - 0.9, y - 0.15, x1 + 0.9, y - 0.15, color=BLUE, lw=1.7, ms=13)
        ax.text((x1 + x2) / 2, y + 0.62, up_lbl, ha="center", va="bottom",
                fontsize=9.6, color=RED, fontweight="bold")
        ax.text((x1 + x2) / 2, y - 0.62, dn_lbl, ha="center", va="top",
                fontsize=9.6, color=BLUE, fontweight="bold")

    pair(0.9, 4.2, "NÓNG CHẢY\n(thu $Q$)", "ĐÔNG ĐẶC\n(toả $Q$)")
    pair(4.2, 7.5, "HOÁ HƠI\n(thu $Q$)", "NGƯNG TỤ\n(toả $Q$)")
    # thăng hoa / ngưng kết đi vòng phía dưới
    ax.plot([0.9, 0.9, 7.5, 7.5], [0.48, -1.75, -1.75, 0.48], color=ORANGE, lw=1.7)
    arrow(ax, 6.6, -1.75, 7.5, -1.75, color=ORANGE, lw=1.7, ms=13)
    ax.text(4.2, -1.68, "THĂNG HOA (rắn → hơi, thu $Q$)", ha="center", va="bottom",
            fontsize=9.6, color=ORANGE, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=1.5))
    ax.plot([0.9, 0.9, 7.5, 7.5], [0.48, -2.55, -2.55, 0.48], color=PURPLE, lw=1.7)
    arrow(ax, 1.8, -2.55, 0.9, -2.55, color=PURPLE, lw=1.7, ms=13)
    ax.text(4.2, -2.48, "NGƯNG KẾT (hơi → rắn, toả $Q$)", ha="center", va="bottom",
            fontsize=9.6, color=PURPLE, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=1.5))

    ax.text(4.2, 2.75, "Trong suốt quá trình chuyển thể của chất kết tinh, "
                       "nhiệt độ KHÔNG đổi\nnhưng vật vẫn liên tục thu (hoặc toả) nhiệt lượng",
            ha="center", va="center", fontsize=10, style="italic",
            bbox=dict(fc="#fdf2e9", ec=ORANGE, lw=1.0, boxstyle="round,pad=0.4"))
    clean(ax, -0.4, 8.9, -3.1, 3.5, eq=False)
    save(fig, "h03_so_do_chuyen_the")


def f04_do_thi_dun_nuoc_da():
    """Đồ thị nhiệt độ - thời gian khi đun nước đá từ -20 °C đến hơi."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    # đoạn: đá nóng lên, nóng chảy, nước nóng lên, sôi, hơi nóng lên
    t = [0, 1.0, 6.35, 16.35, 84.2, 90.0]
    T = [-20, 0, 0, 100, 100, 130]
    ax.plot(t, T, color=RED, lw=2.4, solid_joinstyle="round")
    for x, y in zip(t, T):
        ax.plot([x], [y], "o", color=RED, ms=5, zorder=5)
    ax.axhline(0, color=GREY, lw=0.9, ls=":")
    ax.axhline(100, color=GREY, lw=0.9, ls=":")

    # đánh số các giai đoạn ngay trên đường biểu diễn
    mids = [(0.5, -10), (3.7, 0), (11.4, 50), (50.3, 100), (87.1, 115)]
    for i, (x, y) in enumerate(mids, 1):
        ax.plot([x], [y], "o", color="white", ms=15, zorder=6)
        ax.plot([x], [y], "o", mfc="white", mec=BLUE, mew=1.6, ms=15, zorder=7)
        ax.text(x, y, str(i), ha="center", va="center", fontsize=9.5,
                fontweight="bold", color=BLUE, zorder=8)

    ax.annotate("", xy=(1.0, -22), xytext=(6.35, -22),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(3.7, -27, "$Q_2 = \\lambda m$", ha="center", va="top", fontsize=9.6, color=GREEN)
    ax.annotate("", xy=(16.35, 92), xytext=(84.2, 92),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(50.0, 86.5, "$Q_4 = Lm$  —  dài hơn hẳn giai đoạn ② vì $L \\gg \\lambda$",
            ha="center", va="top", fontsize=9.6, color=GREEN)

    ax.text(20, 137, "① Nước đá nóng lên:  $Q_1 = m c_{đá}\\,\\Delta t$\n"
                     "② Nóng chảy ở $0$ °C, nhiệt độ KHÔNG đổi:  $Q_2 = \\lambda m$\n"
                     "③ Nước lỏng nóng lên:  $Q_3 = m c_{nước}\\,\\Delta t$\n"
                     "④ Sôi ở $100$ °C, nhiệt độ KHÔNG đổi:  $Q_4 = Lm$\n"
                     "⑤ Hơi nước tiếp tục nóng lên",
            ha="left", va="top", fontsize=9.4,
            bbox=dict(fc="#fbfcfd", ec=GREY, lw=0.9, boxstyle="round,pad=0.4"))

    ax.set_xlabel("Thời gian đun  $t$ (nhiệt lượng cung cấp đều theo thời gian)", fontsize=10.2)
    ax.set_ylabel("Nhiệt độ  $T$ (°C)", fontsize=10.5)
    ax.set_yticks([-20, 0, 50, 100, 130])
    ax.set_xticks([])
    ax.set_xlim(-4, 95); ax.set_ylim(-42, 145)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.22, ls=":")
    save(fig, "h04_do_thi_dun_nuoc_da")


def f05_dinh_luat_1():
    """Quy ước dấu của định luật I nhiệt động lực học."""
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    ax.add_patch(FancyBboxPatch((-1.25, -0.85), 2.5, 1.7, boxstyle="round,pad=0.08",
                                fc="#eaf2fb", ec=BLUE, lw=2.0))
    ax.text(0, 0.24, "HỆ", ha="center", fontsize=13, fontweight="bold", color=BLUE)
    ax.text(0, -0.28, "$\\Delta U = A + Q$", ha="center", fontsize=13, color=RED)

    arrow(ax, -3.5, 0.45, -1.35, 0.45, color=RED, lw=2.0, ms=15)
    ax.text(-2.45, 0.62, "$Q > 0$", ha="center", fontsize=11, color=RED, fontweight="bold")
    ax.text(-2.45, 0.30, "hệ NHẬN nhiệt", ha="center", va="top", fontsize=9.4, color=RED)

    arrow(ax, -1.35, -0.45, -3.5, -0.45, color=BLUE, lw=2.0, ms=15)
    ax.text(-2.45, -0.62, "$Q < 0$", ha="center", va="top", fontsize=11, color=BLUE, fontweight="bold")
    ax.text(-2.45, -0.95, "hệ TOẢ nhiệt", ha="center", va="top", fontsize=9.4, color=BLUE)

    arrow(ax, 3.5, 0.45, 1.35, 0.45, color=RED, lw=2.0, ms=15)
    ax.text(2.45, 0.62, "$A > 0$", ha="center", fontsize=11, color=RED, fontweight="bold")
    ax.text(2.45, 0.30, "hệ NHẬN công\n(bị nén)", ha="center", va="top", fontsize=9.4, color=RED)

    arrow(ax, 1.35, -0.45, 3.5, -0.45, color=BLUE, lw=2.0, ms=15)
    ax.text(2.45, -0.62, "$A < 0$", ha="center", va="top", fontsize=11, color=BLUE, fontweight="bold")
    ax.text(2.45, -0.95, "hệ SINH công\n(dãn nở)", ha="center", va="top", fontsize=9.4, color=BLUE)

    ax.text(0, 2.05, "ĐỊNH LUẬT I NHIỆT ĐỘNG LỰC HỌC", ha="center",
            fontsize=12, fontweight="bold", color=RED)
    ax.text(0, 1.62, "Độ biến thiên nội năng của hệ bằng tổng công và nhiệt lượng hệ nhận được",
            ha="center", fontsize=9.8, style="italic")
    ax.text(0, -1.75, "Quy ước: mọi đại lượng hệ NHẬN mang dấu (+), hệ MẤT mang dấu (−)",
            ha="center", fontsize=9.6, color=GREY,
            bbox=dict(fc="#f7f7f7", ec=GREY, lw=0.8, boxstyle="round,pad=0.3"))
    clean(ax, -4.4, 4.4, -2.3, 2.5, eq=False)
    save(fig, "h05_dinh_luat_1")


def f06_hai_cach_doi_noi_nang():
    """Hai cách làm biến đổi nội năng: thực hiện công và truyền nhiệt."""
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))

    # --- nén khí trong xilanh (thực hiện công)
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 3.4, 1.8, fill=False, ec="k", lw=2.0))
    ax.add_patch(Rectangle((0.04, 0.04), 1.9, 1.72, fc="#fdebd0", ec="none"))
    ax.add_patch(Rectangle((1.94, 0.04), 0.22, 1.72, fc=GREY, ec="k", lw=1.2))
    ax.plot([2.16, 3.15], [0.9, 0.9], color="k", lw=3.0)
    arrow(ax, 3.15, 0.9, 2.35, 0.9, color=RED, lw=2.2, ms=15)
    ax.text(2.75, 1.15, "$\\vec{F}$", fontsize=12, color=RED, ha="center")
    rng = np.random.RandomState(3)
    for _ in range(14):
        x, y = rng.uniform(0.15, 1.8), rng.uniform(0.15, 1.65)
        ax.add_patch(Circle((x, y), 0.055, fc=RED, ec="none"))
    ax.text(1.7, 2.55, "THỰC HIỆN CÔNG", ha="center", fontsize=11,
            fontweight="bold", color=RED)
    ax.text(1.7, -0.55, "Nén nhanh khí → $A > 0$, $Q \\approx 0$\n"
                        "→ $\\Delta U = A > 0$: khí nóng lên",
            ha="center", va="top", fontsize=9.4)
    clean(ax, -0.4, 3.9, -2.0, 3.0)

    # --- truyền nhiệt
    ax = axs[1]
    ax.add_patch(Rectangle((0.5, 0.35), 2.4, 1.5, fill=False, ec="k", lw=2.0))
    ax.add_patch(Rectangle((0.54, 0.39), 2.32, 1.0, fc="#aed6f1", ec="none"))
    for x in np.linspace(0.9, 2.5, 4):
        ax.plot([x, x - 0.12, x + 0.12, x], [0.05, -0.18, -0.32, -0.55],
                color=ORANGE, lw=2.0)
    ax.text(1.7, -0.72, "nguồn nhiệt", ha="center", va="top", fontsize=9.2, color=ORANGE)
    for x in np.linspace(0.85, 2.55, 3):
        arrow(ax, x, 0.05, x, 0.33, color=RED, lw=1.6, ms=10)
    ax.text(3.15, 1.1, "$Q > 0$", fontsize=11.5, color=RED, fontweight="bold")
    ax.text(1.7, 2.55, "TRUYỀN NHIỆT", ha="center", fontsize=11,
            fontweight="bold", color=RED)
    ax.text(1.7, -1.15, "Đun nóng vật → $Q > 0$, $A = 0$\n"
                        "→ $\\Delta U = Q > 0$: vật nóng lên",
            ha="center", va="top", fontsize=9.4)
    clean(ax, 0.1, 4.4, -2.6, 3.0)
    fig.subplots_adjust(wspace=0.15)
    save(fig, "h06_hai_cach_doi_noi_nang")


def f07_thang_nhiet_do():
    """Đối chiếu ba thang nhiệt độ Celsius, Kelvin, Fahrenheit."""
    fig, ax = plt.subplots(figsize=(6.6, 4.6))
    # trục dọc chung: dùng thang Celsius từ -280 đến 120
    def yc(c):
        return (c + 280) / 400.0 * 6.0

    xs = {"CELSIUS\n(°C)": 0.8, "KELVIN\n(K)": 3.0, "FAHRENHEIT\n(°F)": 5.2}
    cols = {"CELSIUS\n(°C)": BLUE, "KELVIN\n(K)": RED, "FAHRENHEIT\n(°F)": GREEN}
    for name, x in xs.items():
        ax.plot([x, x], [yc(-280), yc(120)], color=cols[name], lw=3.0,
                solid_capstyle="round")
        ax.text(x, yc(120) + 0.30, name, ha="center", va="bottom",
                fontsize=10.5, fontweight="bold", color=cols[name])

    marks = [(-273.15, "−273,15", "0", "−459,67", "Độ không tuyệt đối"),
             (0, "0", "273,15", "32", "Điểm đóng băng của nước"),
             (100, "100", "373,15", "212", "Điểm sôi của nước (1 atm)")]
    for c, sc, sk, sf, note in marks:
        y = yc(c)
        ax.plot([0.93, 5.07], [y, y], color=GREY, lw=0.8, ls=":", zorder=1)
        for x, s, name in [(0.8, sc, "CELSIUS\n(°C)"), (3.0, sk, "KELVIN\n(K)"),
                           (5.2, sf, "FAHRENHEIT\n(°F)")]:
            ax.plot([x - 0.13, x + 0.13], [y, y], color=cols[name], lw=2.2, zorder=4)
            ax.text(x + 0.20, y, s, va="center", fontsize=9.6, color=cols[name],
                    zorder=5, bbox=dict(fc="white", ec="none", pad=1.0))
        ax.text(6.55, y, note, va="center", fontsize=9.0, color=GREY)

    ax.text(3.4, -0.75, "$T(\\mathrm{K}) = t(°\\mathrm{C}) + 273{,}15 \\;\\;\\Rightarrow\\;\\; "
                        "\\Delta T(\\mathrm{K}) = \\Delta t(°\\mathrm{C})$",
            ha="center", fontsize=11, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.0, boxstyle="round,pad=0.35"))
    clean(ax, 0.2, 9.6, -1.5, 7.1, eq=False)
    save(fig, "h07_thang_nhiet_do")


def f08_can_bang_nhiet():
    """Sự truyền nhiệt và trạng thái cân bằng nhiệt."""
    fig, ax = plt.subplots(figsize=(7.4, 3.3))
    for x, T, fc, lbl in [(0.0, "$T_1$ (nóng)", "#f5b7b1", "Vật 1"),
                          (3.6, "$T_2$ (lạnh)", "#aed6f1", "Vật 2")]:
        ax.add_patch(Rectangle((x, 0), 1.9, 1.5, fc=fc, ec="k", lw=1.6))
        ax.text(x + 0.95, 0.95, lbl, ha="center", fontsize=10.5, fontweight="bold")
        ax.text(x + 0.95, 0.45, T, ha="center", fontsize=11)
    ax.add_patch(Rectangle((1.9, 0), 1.7, 1.5, fc="#f7f7f7", ec="k", lw=1.0, ls="--"))
    arrow(ax, 2.0, 0.9, 3.5, 0.9, color=RED, lw=2.2, ms=15)
    ax.text(2.75, 1.12, "nhiệt truyền", ha="center", fontsize=9.4, color=RED)
    ax.text(2.75, 0.45, "$T_1 > T_2$", ha="center", fontsize=10, color=RED)

    arrow(ax, 6.0, 0.75, 7.0, 0.75, color=GREY, lw=1.8, ms=14)
    ax.add_patch(Rectangle((7.3, 0), 1.9, 1.5, fc="#d5dbdb", ec="k", lw=1.6))
    ax.text(8.25, 0.95, "CÂN BẰNG NHIỆT", ha="center", fontsize=9.6, fontweight="bold")
    ax.text(8.25, 0.45, "$T_1 = T_2$", ha="center", fontsize=11, color=BLUE)

    ax.text(4.6, -0.55, "Nhiệt tự truyền từ vật có nhiệt độ CAO sang vật có nhiệt độ THẤP "
                        "(không phụ thuộc vật nào\nchứa nhiều nội năng hơn), "
                        "cho tới khi hai vật có cùng nhiệt độ.",
            ha="center", va="top", fontsize=9.6,
            bbox=dict(fc="#fdf2e9", ec=ORANGE, lw=1.0, boxstyle="round,pad=0.35"))
    clean(ax, -0.4, 9.6, -2.0, 2.0, eq=False)
    save(fig, "h08_can_bang_nhiet")


def f09_do_nhiet_dung_rieng():
    """Bộ thí nghiệm đo nhiệt dung riêng của nước."""
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    # bình nhiệt lượng kế
    ax.add_patch(Rectangle((1.0, 0.0), 3.0, 2.4, fill=False, ec="k", lw=2.2))
    ax.add_patch(Rectangle((1.1, 0.1), 2.8, 1.75, fc="#aed6f1", ec="none"))
    ax.add_patch(Rectangle((0.82, 2.4), 3.36, 0.22, fc="#d5dbdb", ec="k", lw=1.4))
    ax.text(2.5, 0.75, "nước\n$m$, $c$", ha="center", fontsize=10, color=BLUE)
    # vỏ cách nhiệt
    ax.add_patch(Rectangle((0.7, -0.3), 3.6, 3.0, fill=False, ec=ORANGE, lw=1.6, ls="--"))
    ax.text(0.60, 1.2, "vỏ cách nhiệt", rotation=90, ha="right", va="center",
            fontsize=9.0, color=ORANGE)
    # điện trở nung
    ax.plot([1.75, 1.75], [2.62, 1.35], color="k", lw=1.6)
    ax.plot([2.25, 2.25], [2.62, 1.35], color="k", lw=1.6)
    zz = np.linspace(0, 1, 60)
    ax.plot(1.75 + 0.5 * zz, 1.35 - 0.10 * np.sin(zz * 8 * np.pi), color=RED, lw=2.2)
    ax.annotate("điện trở nung", xy=(2.0, 1.32), xytext=(0.05, 0.60),
                fontsize=9.2, color=RED, ha="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    # nhiệt kế
    ax.plot([3.35, 3.35], [2.95, 0.55], color=GREEN, lw=2.2)
    ax.add_patch(Circle((3.35, 0.45), 0.13, fc=GREEN, ec=GREEN))
    ax.annotate("nhiệt kế", xy=(3.35, 2.20), xytext=(4.55, 2.55),
                fontsize=9.2, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
    # nguồn + oát kế
    ax.add_patch(Rectangle((5.1, 1.8), 1.9, 0.95, fc="#f7f7f7", ec="k", lw=1.5))
    ax.text(6.05, 2.28, "NGUỒN ĐIỆN", ha="center", fontsize=9.4, fontweight="bold")
    ax.add_patch(Rectangle((5.1, 0.4), 1.9, 0.95, fc="#f7f7f7", ec="k", lw=1.5))
    ax.text(6.05, 1.02, "OÁT KẾ", ha="center", fontsize=9.4, fontweight="bold")
    ax.text(6.05, 0.66, "đọc $P$ (W)", ha="center", fontsize=8.8)
    ax.plot([5.1, 4.6, 4.6, 2.25], [2.28, 2.28, 3.05, 3.05], color="k", lw=1.3)
    ax.plot([2.25, 2.25], [3.05, 2.62], color="k", lw=1.3)
    ax.plot([5.1, 4.35, 4.35, 1.75], [0.88, 0.88, 3.30, 3.30], color="k", lw=1.3)
    ax.plot([1.75, 1.75], [3.30, 2.62], color="k", lw=1.3)
    ax.plot([6.05, 6.05], [1.35, 1.80], color="k", lw=1.3)

    ax.text(3.7, -0.95, "Nhiệt lượng cung cấp $Q = Pt$;  đo $\\Delta T$ theo thời gian\n"
                        "$\\Rightarrow$  $c = \\dfrac{P\\,t}{m\\,\\Delta T}$  "
                        "(hệ số góc của đồ thị $\\Delta T$ theo $t$)",
            ha="center", va="top", fontsize=10, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.0, boxstyle="round,pad=0.35"))
    clean(ax, 0.2, 7.4, -2.3, 3.7, eq=False)
    save(fig, "h09_do_nhiet_dung_rieng")


def f10_do_thi_Q_deltaT():
    """Đồ thị Q - ΔT để xác định nhiệt dung riêng từ hệ số góc."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    dT = np.array([0, 4.0, 8.0, 12.0, 16.0, 20.0])
    Q = np.array([0, 1.68, 3.36, 5.04, 6.72, 8.40])  # kJ, m = 0,2 kg nước
    ax.plot(dT[1:], Q[1:], "o", color=RED, ms=7, zorder=5, label="số liệu đo")
    ax.plot(dT, Q, color=BLUE, lw=2.0, label="đường thẳng khớp số liệu")
    ax.plot([12, 20], [5.04, 5.04], color=GREY, lw=1.2, ls="--")
    ax.plot([20, 20], [5.04, 8.40], color=GREY, lw=1.2, ls="--")
    ax.text(16, 4.72, "$\\Delta(\\Delta T) = 8{,}0$ K", ha="center", va="top", fontsize=9.4)
    ax.text(20.4, 6.7, "$\\Delta Q = 3{,}36$ kJ", va="center", fontsize=9.4)
    ax.text(4.2, 7.3, "Hệ số góc  $k = \\dfrac{\\Delta Q}{\\Delta(\\Delta T)} = 0{,}42$ kJ/K\n"
                      "$c = \\dfrac{k}{m} = \\dfrac{420}{0{,}20} = 2100$ J/(kg·K)",
            fontsize=10, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.0, boxstyle="round,pad=0.35"))
    ax.set_xlabel("Độ tăng nhiệt độ  $\\Delta T$ (K)", fontsize=10.5)
    ax.set_ylabel("Nhiệt lượng cung cấp  $Q$ (kJ)", fontsize=10.5)
    ax.set_xlim(0, 25); ax.set_ylim(0, 10.2)
    ax.grid(alpha=0.25, ls=":")
    ax.legend(fontsize=9, loc="lower right")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h10_do_thi_Q_deltaT")


def f11_do_nhiet_nong_chay():
    """Bộ thí nghiệm đo nhiệt nóng chảy riêng của nước đá."""
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    # cốc chứa đá + điện trở nung
    ax.add_patch(Polygon([(1.0, 0.0), (3.2, 0.0), (3.45, 2.4), (0.75, 2.4)],
                         fill=False, ec="k", lw=2.0))
    rng = np.random.RandomState(11)
    for _ in range(16):
        x = rng.uniform(1.05, 3.05); y = rng.uniform(0.15, 1.55)
        ax.add_patch(Rectangle((x, y), 0.26, 0.20, fc="#d6eaf8", ec=BLUE, lw=0.9,
                               angle=rng.uniform(-25, 25)))
    ax.text(2.1, 2.05, "nước đá đang tan  $0$ °C", ha="center", fontsize=9.4, color=BLUE)
    zz = np.linspace(0, 1, 60)
    ax.plot(1.35 + 1.4 * zz, 0.85 - 0.10 * np.sin(zz * 10 * np.pi), color=RED, lw=2.0)
    ax.plot([1.35, 1.35], [0.85, 2.85], color="k", lw=1.4)
    ax.plot([2.75, 2.75], [0.85, 2.85], color="k", lw=1.4)
    ax.text(3.60, 0.85, "điện trở nung\ncông suất $P$", fontsize=9.2, color=RED, va="center")
    # phễu và cốc hứng nước
    ax.plot([1.9, 2.1, 2.1, 2.3], [0.0, -0.55, -0.55, 0.0], color=GREY, lw=1.6)
    ax.add_patch(Rectangle((1.55, -1.85), 1.3, 1.15, fill=False, ec="k", lw=1.8))
    ax.add_patch(Rectangle((1.60, -1.80), 1.2, 0.55, fc="#aed6f1", ec="none"))
    ax.text(3.05, -1.35, "nước tan chảy, cân\nkhối lượng $m$", fontsize=9.2, va="center")
    # nguồn
    ax.add_patch(Rectangle((0.0, 3.1), 4.2, 0.7, fc="#f7f7f7", ec="k", lw=1.4))
    ax.text(2.1, 3.45, "NGUỒN ĐIỆN – OÁT KẾ – ĐỒNG HỒ BẤM GIÂY", ha="center",
            fontsize=9.2, fontweight="bold")
    ax.plot([1.35, 1.35], [2.85, 3.10], color="k", lw=1.3)
    ax.plot([2.75, 2.75], [2.85, 3.10], color="k", lw=1.3)

    ax.text(6.4, 1.1, "Trong thời gian $t$:\n\n"
                      "$Q = P\\,t = \\lambda\\,m$\n\n"
                      "$\\Rightarrow\\;\\; \\lambda = \\dfrac{P\\,t}{m}$\n\n"
                      "Lưu ý: nhiệt độ giữ nguyên\n$0$ °C suốt quá trình đo.",
            ha="center", va="center", fontsize=10.2, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.2, boxstyle="round,pad=0.45"))
    clean(ax, -0.3, 8.6, -2.5, 4.1, eq=False)
    save(fig, "h11_do_nhiet_nong_chay")


def f12_bay_hoi_va_soi():
    """Phân biệt sự bay hơi và sự sôi."""
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))
    rng = np.random.RandomState(5)

    ax = axs[0]
    ax.add_patch(Rectangle((0.4, 0.0), 3.2, 1.5, fill=False, ec="k", lw=1.8))
    ax.add_patch(Rectangle((0.45, 0.05), 3.1, 1.15, fc="#aed6f1", ec="none"))
    for _ in range(9):
        x = rng.uniform(0.6, 3.4)
        arrow(ax, x, 1.22, x + rng.uniform(-0.2, 0.2), 1.22 + rng.uniform(0.5, 1.2),
              color=GREEN, lw=1.2, ms=9)
    ax.set_title("SỰ BAY HƠI", fontsize=11.5, fontweight="bold", color=GREEN, pad=6)
    ax.text(2.0, -0.35, "• Chỉ xảy ra ở MẶT THOÁNG\n"
                        "• Xảy ra ở MỌI nhiệt độ\n"
                        "• Tốc độ phụ thuộc: nhiệt độ, diện tích\n"
                        "  mặt thoáng, gió, độ ẩm",
            ha="center", va="top", fontsize=9.3)
    clean(ax, 0.0, 4.2, -2.5, 3.2)

    ax = axs[1]
    ax.add_patch(Rectangle((0.4, 0.0), 3.2, 1.5, fill=False, ec="k", lw=1.8))
    ax.add_patch(Rectangle((0.45, 0.05), 3.1, 1.15, fc="#f5b7b1", ec="none"))
    for _ in range(16):
        x, y = rng.uniform(0.55, 3.45), rng.uniform(0.15, 1.05)
        ax.add_patch(Circle((x, y), rng.uniform(0.05, 0.13), fill=False, ec=RED, lw=1.1))
    for _ in range(6):
        x = rng.uniform(0.6, 3.4)
        arrow(ax, x, 1.25, x, 1.25 + rng.uniform(0.5, 1.1), color=RED, lw=1.2, ms=9)
    for x in np.linspace(0.8, 3.2, 4):
        ax.plot([x, x - 0.1, x + 0.1, x], [-0.05, -0.25, -0.38, -0.58], color=ORANGE, lw=1.8)
    ax.set_title("SỰ SÔI", fontsize=11.5, fontweight="bold", color=RED, pad=6)
    ax.text(2.0, -0.80, "• Xảy ra ở CẢ trong lòng chất lỏng\n"
                        "• Chỉ xảy ra ở nhiệt độ sôi xác định\n"
                        "• Nhiệt độ sôi phụ thuộc ÁP SUẤT\n"
                        "• Khi sôi, nhiệt độ không đổi",
            ha="center", va="top", fontsize=9.3)
    clean(ax, 0.0, 4.2, -2.9, 3.2)
    fig.subplots_adjust(wspace=0.12)
    save(fig, "h12_bay_hoi_va_soi")


def f13_so_sanh_nhiet_dung():
    """Cột so sánh nhiệt dung riêng của một số chất."""
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    names = ["Nước", "Nước đá", "Rượu\netylic", "Nhôm", "Sắt", "Đồng", "Chì"]
    vals = [4200, 2100, 2500, 880, 460, 380, 130]
    cols = [BLUE, "#5dade2", TEAL, GREY, GREY, ORANGE, "#34495e"]
    b = ax.bar(names, vals, color=cols, edgecolor="k", lw=0.8, width=0.62)
    for r, v in zip(b, vals):
        ax.text(r.get_x() + r.get_width() / 2, v + 90, str(v), ha="center",
                fontsize=9.4, fontweight="bold")
    ax.set_ylabel("$c$  [J/(kg·K)]", fontsize=10.5)
    ax.set_ylim(0, 4900)
    ax.grid(axis="y", alpha=0.25, ls=":")
    ax.set_title("Nhiệt dung riêng của một số chất ở điều kiện thường",
                 fontsize=10.5, pad=8)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.text(3.0, 4400, "Nước có $c$ rất lớn → điều hoà khí hậu, làm chất tải nhiệt",
            ha="center", fontsize=9.4, color=BLUE, style="italic")
    save(fig, "h13_so_sanh_nhiet_dung")


def f14_do_thi_lam_nguoi():
    """Đồ thị làm nguội một chất lỏng đến khi đông đặc (đọc đồ thị)."""
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    t = [0, 4, 14, 20]
    T = [90, 60, 60, 30]
    ax.plot(t, T, color=BLUE, lw=2.4)
    for x, y in zip(t, T):
        ax.plot([x], [y], "o", color=BLUE, ms=5.5, zorder=5)
    ax.axhline(60, color=GREY, lw=0.9, ls=":")
    ax.annotate("Bắt đầu đông đặc", xy=(4, 60), xytext=(1.2, 40),
                fontsize=9.3, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    ax.annotate("Đông đặc xong", xy=(14, 60), xytext=(14.5, 82),
                fontsize=9.3, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    ax.text(9, 63.5, "Đoạn nằm ngang: chất TOẢ nhiệt\nnhưng nhiệt độ KHÔNG đổi",
            ha="center", fontsize=9.3, color=GREEN)
    ax.set_xlabel("Thời gian  $t$ (phút)", fontsize=10.5)
    ax.set_ylabel("Nhiệt độ  $T$ (°C)", fontsize=10.5)
    ax.set_xlim(0, 21); ax.set_ylim(20, 100)
    ax.set_xticks(range(0, 22, 2))
    ax.grid(alpha=0.25, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h14_do_thi_lam_nguoi")


# ===================================================================
#                       CHƯƠNG II - KHÍ LÍ TƯỞNG
# ===================================================================

def f15_chuyen_dong_brown():
    """Quỹ đạo gấp khúc của hạt trong chuyển động Brown."""
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    rng = np.random.RandomState(21)
    x, y = [0.0], [0.0]
    for _ in range(28):
        a = rng.uniform(0, 2 * np.pi)
        r = rng.uniform(0.25, 1.0)
        x.append(x[-1] + r * np.cos(a)); y.append(y[-1] + r * np.sin(a))
    ax.plot(x, y, color=BLUE, lw=1.5, marker="o", ms=3.5, mfc=RED, mec=RED)
    ax.plot([x[0]], [y[0]], "s", color=GREEN, ms=9, zorder=6)
    ax.text(x[0] + 0.15, y[0] - 0.35, "vị trí đầu", fontsize=9.2, color=GREEN)
    ax.plot([x[-1]], [y[-1]], "*", color=RED, ms=15, zorder=6)
    ax.text(x[-1] + 0.2, y[-1], "vị trí sau", fontsize=9.2, color=RED)
    # vài phân tử nước va chạm
    for _ in range(30):
        px, py = rng.uniform(-4.5, 4.5), rng.uniform(-3.5, 3.5)
        ax.plot([px], [py], ".", color="#bdc3c7", ms=4, zorder=1)
    ax.set_title("Chuyển động Brown: hạt phấn hoa chuyển động hỗn loạn không ngừng",
                 fontsize=10, pad=8)
    ax.text(0, -4.35, "Nguyên nhân: các phân tử nước (chấm xám) va chạm vào hạt "
                      "từ mọi phía một cách không cân bằng",
            ha="center", fontsize=9.2, style="italic", color=GREY)
    clean(ax, -5.0, 5.0, -4.9, 3.9, eq=False)
    save(fig, "h15_chuyen_dong_brown")


def f16_mo_hinh_dong_hoc():
    """Mô hình động học phân tử chất khí: va chạm với thành bình."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.add_patch(Rectangle((0, 0), 6.0, 4.0, fill=False, ec="k", lw=2.5))
    rng = np.random.RandomState(31)
    for _ in range(18):
        x, y = rng.uniform(0.3, 5.7), rng.uniform(0.3, 3.7)
        a = rng.uniform(0, 2 * np.pi)
        ax.add_patch(Circle((x, y), 0.11, fc=BLUE, ec="none", zorder=4))
        arrow(ax, x, y, x + 0.55 * np.cos(a), y + 0.55 * np.sin(a),
              color=GREY, lw=1.0, ms=8)
    # một phân tử va chạm thành phải, minh hoạ đổi dấu vận tốc
    xm, ym = 5.05, 2.5
    ax.add_patch(Circle((xm, ym), 0.14, fc=RED, ec="k", lw=0.9, zorder=6))
    arrow(ax, 4.15, 2.5, 5.85, 2.5, color=RED, lw=2.0, ms=13)
    ax.text(4.55, 2.68, "$+mv$", fontsize=10.5, color=RED)
    arrow(ax, 5.85, 1.95, 4.15, 1.95, color=GREEN, lw=2.0, ms=13)
    ax.text(4.55, 1.60, "$-mv$", fontsize=10.5, color=GREEN)
    ax.text(6.25, 2.25, "Mỗi va chạm truyền cho thành bình\n"
                        "xung lượng $2mv$ → tổng hợp vô số\n"
                        "va chạm tạo thành ÁP SUẤT",
            fontsize=9.4, va="center", color=RED)
    ax.text(3.0, -0.55, "$pV = \\frac{1}{3}Nm\\overline{v^2}$  hay  "
                        "$p = \\frac{1}{3}\\mu\\, m\\, \\overline{v^2}$  "
                        "với $\\mu = N/V$ là mật độ phân tử",
            ha="center", va="top", fontsize=10.5, color=BLUE,
            bbox=dict(fc="#eaf2fb", ec=BLUE, lw=1.0, boxstyle="round,pad=0.35"))
    clean(ax, -0.3, 10.6, -1.6, 4.4, eq=False)
    save(fig, "h16_mo_hinh_dong_hoc")


def f17_thi_nghiem_boyle():
    """Bộ thí nghiệm khảo sát định luật Boyle."""
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.add_patch(Rectangle((0.6, 0.4), 1.2, 3.2, fill=False, ec="k", lw=2.2))
    ax.add_patch(Rectangle((0.66, 0.46), 1.08, 1.8, fc="#d6eaf8", ec="none"))
    ax.add_patch(Rectangle((0.66, 2.26), 1.08, 0.20, fc=GREY, ec="k", lw=1.2))
    ax.plot([1.2, 1.2], [2.46, 4.05], color="k", lw=3.0)
    ax.add_patch(Rectangle((0.55, 4.05), 1.3, 0.22, fc="#34495e", ec="k", lw=1.0))
    arrow(ax, 1.2, 4.95, 1.2, 4.35, color=RED, lw=2.2, ms=15)
    ax.text(1.2, 5.10, "nén / kéo pit-tông", ha="center", fontsize=9.4, color=RED)
    ax.text(1.2, 1.3, "khí\n$V$", ha="center", fontsize=10.5, color=BLUE)
    # thước đo thể tích
    ax.plot([2.05, 2.05], [0.46, 2.26], color=GREEN, lw=1.6)
    for y in np.linspace(0.46, 2.26, 7):
        ax.plot([2.05, 2.22], [y, y], color=GREEN, lw=1.0)
    ax.text(2.35, 1.36, "thang chia\nthể tích", fontsize=9.2, color=GREEN, va="center")
    # áp kế
    ax.add_patch(Circle((4.6, 1.6), 0.85, fc="#f7f7f7", ec="k", lw=1.8))
    for a in np.linspace(200, -20, 9):
        ra = np.radians(a)
        ax.plot([4.6 + 0.68 * np.cos(ra), 4.6 + 0.82 * np.cos(ra)],
                [1.6 + 0.68 * np.sin(ra), 1.6 + 0.82 * np.sin(ra)], color="k", lw=1.0)
    arrow(ax, 4.6, 1.6, 4.6 + 0.55 * np.cos(np.radians(62)),
          1.6 + 0.55 * np.sin(np.radians(62)), color=RED, lw=2.0, ms=10)
    ax.text(4.6, 0.42, "ÁP KẾ – đọc $p$", ha="center", fontsize=9.4, fontweight="bold")
    ax.plot([1.8, 3.0, 3.0, 3.75], [1.0, 1.0, 1.6, 1.6], color="k", lw=1.5)

    ax.text(3.4, -0.75, "Giữ NHIỆT ĐỘ và LƯỢNG KHÍ không đổi, thay đổi $V$ chậm, đọc $p$ tương ứng\n"
                        "→ kiểm tra tích $pV$ = hằng số",
            ha="center", va="top", fontsize=9.8, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.0, boxstyle="round,pad=0.35"))
    clean(ax, 0.0, 6.4, -2.0, 5.6, eq=False)
    save(fig, "h17_thi_nghiem_boyle")


def f18_do_thi_boyle():
    """Đường đẳng nhiệt trong hệ (p,V) và đường thẳng trong hệ (p, 1/V)."""
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.7))
    ax = axs[0]
    V = np.linspace(0.9, 5.0, 300)
    for C, c, lb in [(4.0, BLUE, "$T_1$"), (6.4, RED, "$T_2 > T_1$")]:
        ax.plot(V, C / V, color=c, lw=2.2, label=lb)
    ax.set_xlabel("$V$", fontsize=11.5); ax.set_ylabel("$p$", fontsize=11.5)
    ax.set_xlim(0, 5.4); ax.set_ylim(0, 5.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(fontsize=10, loc="upper right")
    ax.set_title("Hệ $(p,V)$: đường ĐẲNG NHIỆT là HYPEBOL", fontsize=10.3, pad=7)
    ax.text(2.7, 0.45, "$pV = $ hằng số", fontsize=10.5, color=GREY, ha="center")
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    ax = axs[1]
    iv = np.linspace(0, 1.1, 50)
    ax.plot(iv, 4.0 * iv, color=BLUE, lw=2.2, label="$T_1$")
    ax.plot(iv, 6.4 * iv, color=RED, lw=2.2, label="$T_2 > T_1$")
    ax.set_xlabel("$1/V$", fontsize=11.5); ax.set_ylabel("$p$", fontsize=11.5)
    ax.set_xlim(0, 1.15); ax.set_ylim(0, 7.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(fontsize=10, loc="upper left")
    ax.set_title("Hệ $(p,\\,1/V)$: ĐƯỜNG THẲNG qua gốc toạ độ", fontsize=10.3, pad=7)
    ax.text(0.63, 1.2, "Hệ số góc tỉ lệ với $T$\n→ cách kiểm tra định luật\nchính xác nhất",
            fontsize=9.3, color=GREEN)
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.subplots_adjust(wspace=0.25)
    save(fig, "h18_do_thi_boyle")


def f19_thi_nghiem_charles():
    """Bộ thí nghiệm minh hoạ định luật Charles."""
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    # cốc nước có thể đun nóng
    ax.add_patch(Rectangle((0.5, 0.0), 3.4, 2.6, fill=False, ec="k", lw=2.0))
    ax.add_patch(Rectangle((0.56, 0.06), 3.28, 2.1, fc="#aed6f1", ec="none"))
    for x in np.linspace(1.0, 3.4, 4):
        ax.plot([x, x - 0.1, x + 0.1, x], [-0.05, -0.25, -0.38, -0.58], color=ORANGE, lw=1.8)
    ax.text(2.2, -0.75, "đun nóng dần", ha="center", va="top", fontsize=9.3, color=ORANGE)
    # ống nghiệm chứa khí, nút giọt thuỷ ngân
    ax.add_patch(Rectangle((1.85, 0.35), 0.55, 3.4, fill=False, ec="k", lw=1.8))
    ax.add_patch(Rectangle((1.89, 0.39), 0.47, 1.6, fc="#fdebd0", ec="none"))
    ax.add_patch(Rectangle((1.89, 1.99), 0.47, 0.18, fc="#7f8c8d", ec="k", lw=0.8))
    ax.text(2.55, 2.08, "giọt thuỷ ngân (di chuyển tự do\n→ giữ áp suất khí KHÔNG đổi)",
            fontsize=9.2, va="center")
    ax.text(2.12, 1.15, "khí", ha="center", fontsize=10, color=ORANGE, rotation=90)
    arrow(ax, 2.12, 2.35, 2.12, 3.2, color=RED, lw=1.8, ms=12)
    ax.text(1.72, 2.85, "$V$ tăng", fontsize=9.4, color=RED, ha="right")
    # nhiệt kế
    ax.plot([3.35, 3.35], [3.1, 0.6], color=GREEN, lw=2.0)
    ax.add_patch(Circle((3.35, 0.5), 0.12, fc=GREEN, ec=GREEN))
    ax.text(3.50, 3.05, "nhiệt kế", fontsize=9.2, color=GREEN)

    ax.text(7.0, 1.6, "Giữ ÁP SUẤT và LƯỢNG KHÍ\nkhông đổi:\n\n"
                      "$\\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$\n\n"
                      "$T$ luôn tính theo KELVIN",
            ha="center", va="center", fontsize=10.5, color=RED,
            bbox=dict(fc="#fdf2f0", ec=RED, lw=1.2, boxstyle="round,pad=0.45"))
    clean(ax, 0.0, 9.2, -1.6, 4.3, eq=False)
    save(fig, "h19_thi_nghiem_charles")


def f20_do_thi_charles():
    """Đồ thị V - T (K) và V - t (°C): bẫy kinh điển về gốc toạ độ."""
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.8))
    ax = axs[0]
    T = np.linspace(0, 400, 50)
    ax.plot(T, 0.010 * T, color=BLUE, lw=2.2, label="$p_1$")
    ax.plot(T, 0.0062 * T, color=RED, lw=2.2, label="$p_2 > p_1$")
    ax.plot([0], [0], "o", color="k", ms=6, zorder=6)
    ax.set_xlabel("$T$ (K)", fontsize=11); ax.set_ylabel("$V$", fontsize=11.5)
    ax.set_xlim(0, 430); ax.set_ylim(0, 4.6)
    ax.set_yticks([])
    ax.legend(fontsize=9.5, loc="upper left")
    ax.set_title("Hệ $(V, T)$ với $T$ theo KELVIN:\nđường thẳng ĐI QUA gốc toạ độ",
                 fontsize=10.2, pad=7)
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    ax = axs[1]
    tc = np.linspace(-273.15, 130, 60)
    ax.plot(tc, 0.010 * (tc + 273.15), color=BLUE, lw=2.2)
    ax.plot(tc[tc < -240], 0.010 * (tc[tc < -240] + 273.15), color=BLUE, lw=2.2, ls="--")
    ax.axhline(0, color="k", lw=1.0)
    ax.axvline(0, color="k", lw=1.0)
    ax.plot([-273.15], [0], "o", color=RED, ms=7, zorder=6)
    ax.annotate("Cắt trục hoành tại\n$t = -273{,}15$ °C\n(độ không tuyệt đối)",
                xy=(-273.15, 0), xytext=(-250, 1.9), fontsize=9.2, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.plot([0], [2.73], "o", color=GREEN, ms=6, zorder=6)
    ax.text(12, 2.60, "Cắt trục tung tại $V_0 \\ne 0$", fontsize=9.2, color=GREEN)
    ax.set_xlabel("$t$ (°C)", fontsize=11); ax.set_ylabel("$V$", fontsize=11.5)
    ax.set_xlim(-300, 150); ax.set_ylim(-0.4, 4.6)
    ax.set_yticks([])
    ax.set_title("Hệ $(V, t)$ với $t$ theo °C:\nđường thẳng KHÔNG qua gốc toạ độ",
                 fontsize=10.2, pad=7)
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.subplots_adjust(wspace=0.24)
    save(fig, "h20_do_thi_charles")


def f21_ba_dang_qua_trinh():
    """Ba đẳng quá trình trong ba hệ toạ độ (bảng 3x3)."""
    fig, axs = plt.subplots(3, 3, figsize=(8.6, 8.0))
    rows = ["ĐẲNG NHIỆT\n$T$ = const\n$pV$ = const",
            "ĐẲNG TÍCH\n$V$ = const\n$p/T$ = const",
            "ĐẲNG ÁP\n$p$ = const\n$V/T$ = const"]
    cols = ["Hệ $(p, V)$", "Hệ $(p, T)$", "Hệ $(V, T)$"]

    def setup(ax, xl, yl):
        ax.set_xlim(0, 1.08); ax.set_ylim(0, 1.08)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel(xl, fontsize=10.5, labelpad=1)
        ax.set_ylabel(yl, fontsize=10.5, labelpad=1)
        ax.grid(alpha=0.2, ls=":")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    x = np.linspace(0.14, 1.0, 200)
    # --- hàng 1: đẳng nhiệt
    setup(axs[0][0], "$V$", "$p$"); axs[0][0].plot(x, 0.14 / x, color=RED, lw=2.2)
    axs[0][0].text(0.55, 0.72, "hypebol", fontsize=9, color=RED)
    setup(axs[0][1], "$T$", "$p$")
    axs[0][1].plot([0.6, 0.6], [0.12, 0.95], color=RED, lw=2.2)
    arrow(axs[0][1], 0.6, 0.30, 0.6, 0.80, color=RED, lw=1.4, ms=10)
    axs[0][1].text(0.64, 0.55, "$T$ không đổi\n→ thẳng đứng", fontsize=8.6, color=RED)
    setup(axs[0][2], "$T$", "$V$")
    axs[0][2].plot([0.6, 0.6], [0.12, 0.95], color=RED, lw=2.2)
    axs[0][2].text(0.64, 0.55, "thẳng đứng", fontsize=8.6, color=RED)

    # --- hàng 2: đẳng tích
    setup(axs[1][0], "$V$", "$p$")
    axs[1][0].plot([0.55, 0.55], [0.12, 0.95], color=BLUE, lw=2.2)
    axs[1][0].text(0.59, 0.55, "$V$ không đổi\n→ thẳng đứng", fontsize=8.6, color=BLUE)
    setup(axs[1][1], "$T$", "$p$")
    axs[1][1].plot([0, 1.0], [0, 0.92], color=BLUE, lw=2.2)
    axs[1][1].plot([0], [0], "o", color="k", ms=5)
    axs[1][1].text(0.42, 0.18, "thẳng QUA\ngốc toạ độ", fontsize=8.6, color=BLUE)
    setup(axs[1][2], "$T$", "$V$")
    axs[1][2].plot([0.1, 1.0], [0.55, 0.55], color=BLUE, lw=2.2)
    axs[1][2].text(0.4, 0.62, "nằm ngang", fontsize=8.6, color=BLUE)

    # --- hàng 3: đẳng áp
    setup(axs[2][0], "$V$", "$p$")
    axs[2][0].plot([0.12, 1.0], [0.6, 0.6], color=GREEN, lw=2.2)
    axs[2][0].text(0.4, 0.67, "nằm ngang", fontsize=8.6, color=GREEN)
    setup(axs[2][1], "$T$", "$p$")
    axs[2][1].plot([0.1, 1.0], [0.55, 0.55], color=GREEN, lw=2.2)
    axs[2][1].text(0.4, 0.62, "nằm ngang", fontsize=8.6, color=GREEN)
    setup(axs[2][2], "$T$", "$V$")
    axs[2][2].plot([0, 1.0], [0, 0.92], color=GREEN, lw=2.2)
    axs[2][2].plot([0], [0], "o", color="k", ms=5)
    axs[2][2].text(0.42, 0.18, "thẳng QUA\ngốc toạ độ", fontsize=8.6, color=GREEN)

    for j, c in enumerate(cols):
        axs[0][j].set_title(c, fontsize=11.5, fontweight="bold", pad=10)
    for i, r in enumerate(rows):
        axs[i][0].text(-0.42, 0.5, r, transform=axs[i][0].transAxes, ha="center",
                       va="center", fontsize=9.8, fontweight="bold",
                       color=[RED, BLUE, GREEN][i], rotation=0)
    fig.subplots_adjust(left=0.17, hspace=0.38, wspace=0.30)
    save(fig, "h21_ba_dang_qua_trinh")


def f22_chu_trinh_pV():
    """Chu trình ba giai đoạn trên giản đồ p-V (bài toán chuyển hệ toạ độ)."""
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    # 1(1atm,2L,300K) -> 2 đẳng tích tăng p -> 3 đẳng áp -> về 1 theo đẳng nhiệt
    p1, V1 = 1.0, 2.0
    p2, V2 = 2.0, 2.0
    p3, V3 = 2.0, 3.0
    ax.plot([V1, V2], [p1, p2], color=BLUE, lw=2.4)
    ax.plot([V2, V3], [p2, p3], color=GREEN, lw=2.4)
    Vh = np.linspace(V1, V3, 120)
    ax.plot(Vh, p3 * V3 / Vh, color=RED, lw=2.4)
    for (V, p, lb, dx, dy) in [(V1, p1, "(1)", -0.20, -0.16), (V2, p2, "(2)", -0.22, 0.10),
                               (V3, p3, "(3)", 0.10, 0.10)]:
        ax.plot([V], [p], "o", color="k", ms=7, zorder=6)
        ax.text(V + dx, p + dy, lb, fontsize=11.5, fontweight="bold")
    arrow(ax, V1, 1.45, V1, 1.62, color=BLUE, lw=1.6, ms=13)
    arrow(ax, 2.45, p2, 2.62, p2, color=GREEN, lw=1.6, ms=13)
    arrow(ax, 2.55, p3 * V3 / 2.55, 2.40, p3 * V3 / 2.40, color=RED, lw=1.6, ms=13)
    ax.text(1.62, 1.5, "(1)→(2)\nĐẲNG TÍCH", fontsize=9.2, color=BLUE, ha="right")
    ax.text(2.5, 2.12, "(2)→(3) ĐẲNG ÁP", fontsize=9.2, color=GREEN, ha="center")
    ax.text(2.75, 2.55, "(3)→(1)\nĐẲNG NHIỆT", fontsize=9.2, color=RED, ha="center")
    ax.set_xlabel("$V$ (L)", fontsize=11); ax.set_ylabel("$p$ (atm)", fontsize=11)
    ax.set_xlim(1.5, 3.5); ax.set_ylim(0.6, 2.9)
    ax.set_xticks([1.5, 2.0, 2.5, 3.0, 3.5])
    ax.set_yticks([1.0, 1.5, 2.0, 2.5])
    ax.grid(alpha=0.25, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h22_chu_trinh_pV")


def f23_phan_bo_toc_do():
    """Phân bố tốc độ phân tử ở hai nhiệt độ khác nhau."""
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    v = np.linspace(0, 2200, 500)
    def maxw(v, T, m):
        k = 1.380649e-23
        a = m / (2 * k * T)
        return 4 * np.pi * v**2 * (a / np.pi) ** 1.5 * np.exp(-a * v**2)
    m = 32e-3 / 6.022e23   # phân tử O2
    for T, c, lb in [(300, BLUE, "$T_1 = 300$ K"), (900, RED, "$T_2 = 900$ K")]:
        y = maxw(v, T, m)
        ax.plot(v, y / y.max(), color=c, lw=2.2, label=lb)
        vr = np.sqrt(3 * 1.380649e-23 * T / m)
        ax.axvline(vr, color=c, lw=1.1, ls="--")
        ax.text(vr + 18, 0.94 if T == 300 else 0.80, "$v_{rms}$ = %.0f m/s" % vr,
                fontsize=9.0, color=c)
    ax.set_xlabel("Tốc độ phân tử  $v$ (m/s)", fontsize=10.5)
    ax.set_ylabel("Số phân tử (đơn vị tuỳ ý)", fontsize=10.2)
    ax.set_xlim(0, 2200); ax.set_ylim(0, 1.12)
    ax.set_yticks([])
    ax.legend(fontsize=9.5, loc="center right")
    ax.set_title("Phân bố tốc độ phân tử khí oxygen – nhiệt độ càng cao,\n"
                 "đường phân bố càng thấp và trải rộng về phía tốc độ lớn",
                 fontsize=9.8, pad=8)
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h23_phan_bo_toc_do")


def f24_ong_chu_U():
    """Cột khí bị nhốt bởi thuỷ ngân trong ống thẳng đứng - hai tư thế."""
    fig, axs = plt.subplots(1, 2, figsize=(8.0, 4.4))
    for ax, kind in zip(axs, ["mo_len", "mo_xuong"]):
        ax.add_patch(Rectangle((0.0, 0.0), 0.9, 6.0, fill=False, ec="k", lw=2.0))
        if kind == "mo_len":
            # đáy kín dưới: khí dưới, thuỷ ngân trên, miệng mở hướng lên
            ax.add_patch(Rectangle((0.05, 0.05), 0.8, 2.6, fc="#fdebd0", ec="none"))
            ax.add_patch(Rectangle((0.05, 2.65), 0.8, 1.2, fc="#7f8c8d", ec="none"))
            ax.plot([0.0, 0.9], [0.0, 0.0], color="k", lw=3.0)
            ax.text(0.45, 1.35, "khí\n$\\ell_1$", ha="center", fontsize=10.5, color=ORANGE)
            ax.text(1.15, 3.25, "thuỷ ngân\ncột $h$", fontsize=9.6, va="center")
            ax.text(0.45, 6.35, "miệng MỞ ▲", ha="center", fontsize=9.8, color=RED)
            ax.text(0.45, -0.95, "$p_{khí} = p_0 + h$", ha="center", fontsize=11.5,
                    color=RED, fontweight="bold")
            ax.set_title("Ống thẳng đứng, MIỆNG Ở TRÊN", fontsize=10.3, pad=8)
        else:
            # đáy kín trên: khí trên, thuỷ ngân dưới, miệng mở hướng xuống
            ax.add_patch(Rectangle((0.05, 3.35), 0.8, 2.6, fc="#fdebd0", ec="none"))
            ax.add_patch(Rectangle((0.05, 2.15), 0.8, 1.2, fc="#7f8c8d", ec="none"))
            ax.plot([0.0, 0.9], [6.0, 6.0], color="k", lw=3.0)
            ax.text(0.45, 4.65, "khí\n$\\ell_2$", ha="center", fontsize=10.5, color=ORANGE)
            ax.text(1.15, 2.75, "thuỷ ngân\ncột $h$", fontsize=9.6, va="center")
            ax.text(0.45, -0.55, "miệng MỞ ▼", ha="center", fontsize=9.8, color=RED)
            ax.text(0.45, -1.35, "$p_{khí} = p_0 - h$", ha="center", fontsize=11.5,
                    color=RED, fontweight="bold")
            ax.set_title("Ống thẳng đứng, MIỆNG Ở DƯỚI", fontsize=10.3, pad=8)
        clean(ax, -0.6, 3.4, -2.2, 7.0, eq=False)
    fig.text(0.5, -0.02, "Áp suất tính theo cmHg: cột thuỷ ngân ĐÈ lên khí thì cộng, "
                         "KÉO khí thì trừ. Nhiệt độ không đổi → dùng định luật Boyle.",
             ha="center", fontsize=9.6, style="italic", color=GREY)
    fig.subplots_adjust(wspace=0.1)
    save(fig, "h24_ong_chu_U")


def f25_bom_xe_va_binh_khi():
    """Ứng dụng thực tế: bơm xe và bình khí nén."""
    fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.5))
    ax = axs[0]
    ax.add_patch(Rectangle((0.3, 0.2), 0.7, 3.0, fill=False, ec="k", lw=2.0))
    ax.add_patch(Rectangle((0.35, 0.25), 0.6, 1.5, fc="#fdebd0", ec="none"))
    ax.add_patch(Rectangle((0.35, 1.75), 0.6, 0.18, fc=GREY, ec="k", lw=1.0))
    ax.plot([0.65, 0.65], [1.93, 3.55], color="k", lw=3.0)
    ax.add_patch(Rectangle((0.25, 3.55), 0.8, 0.2, fc="#34495e", ec="k", lw=1.0))
    arrow(ax, 0.65, 4.4, 0.65, 3.85, color=RED, lw=2.0, ms=14)
    ax.plot([1.0, 2.2], [0.5, 0.5], color="k", lw=2.0)
    ax.add_patch(Circle((3.1, 1.0), 0.9, fill=False, ec="#34495e", lw=6.0))
    ax.plot([2.2, 2.2], [0.5, 1.0], color="k", lw=2.0)
    ax.plot([2.2, 2.35], [1.0, 1.0], color="k", lw=2.0)
    ax.text(3.1, 1.0, "lốp xe", ha="center", va="center", fontsize=9.6)
    ax.text(2.0, -0.6, "BƠM XE ĐẠP: nén nhanh → khí nóng lên\n"
                       "($A>0$, $Q\\approx0$ → $\\Delta U>0$)",
            ha="center", va="top", fontsize=9.3)
    clean(ax, 0.0, 4.3, -2.0, 4.8)

    ax = axs[1]
    ax.add_patch(FancyBboxPatch((0.6, 0.2), 1.6, 3.0, boxstyle="round,pad=0.14",
                                fc="#d6eaf8", ec=BLUE, lw=2.2))
    ax.add_patch(Rectangle((1.25, 3.30), 0.3, 0.45, fc=GREY, ec="k", lw=1.2))
    ax.add_patch(Circle((1.4, 3.9), 0.22, fill=False, ec="k", lw=1.6))
    ax.text(1.4, 1.7, "KHÍ NÉN\n$p$ lớn\n$V$ nhỏ", ha="center", va="center",
            fontsize=10, color=BLUE, fontweight="bold")
    arrow(ax, 2.9, 2.0, 3.9, 2.0, color=RED, lw=1.8, ms=13)
    ax.text(3.4, 2.25, "mở van", ha="center", fontsize=9.2, color=RED)
    ax.add_patch(Circle((5.1, 2.0), 1.05, fc="#f9e79f", ec=ORANGE, lw=2.0))
    ax.text(5.1, 2.0, "$V$ lớn\n$p$ nhỏ", ha="center", va="center", fontsize=9.6, color=ORANGE)
    ax.text(3.0, -0.6, "BÌNH KHÍ NÉN (khí y tế, bình chữa cháy):\n"
                       "dung tích nhỏ chứa được lượng khí lớn nhờ nén ở áp suất cao",
            ha="center", va="top", fontsize=9.3)
    clean(ax, 0.2, 6.4, -2.0, 4.4)
    fig.subplots_adjust(wspace=0.12)
    save(fig, "h25_bom_xe_va_binh_khi")


def f26_do_thi_p_T_dang_tich():
    """Đồ thị p - T đẳng tích với hai thể tích khác nhau."""
    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    T = np.linspace(0, 500, 60)
    ax.plot(T, 0.0060 * T, color=BLUE, lw=2.2, label="$V_1$")
    ax.plot(T, 0.0034 * T, color=RED, lw=2.2, label="$V_2 > V_1$")
    ax.plot([0], [0], "o", color="k", ms=6, zorder=6)
    ax.plot([300, 300], [0, 1.80], color=GREY, lw=1.0, ls=":")
    ax.plot([0, 300], [1.80, 1.80], color=GREY, lw=1.0, ls=":")
    ax.plot([300], [1.80], "o", color=BLUE, ms=6, zorder=6)
    ax.text(310, 1.72, "$(T_1, p_1)$", fontsize=9.5, color=BLUE)
    ax.set_xlabel("$T$ (K)", fontsize=11); ax.set_ylabel("$p$", fontsize=11.5)
    ax.set_xlim(0, 520); ax.set_ylim(0, 3.4)
    ax.set_yticks([])
    ax.legend(fontsize=9.5, loc="upper left")
    ax.set_title("Đường ĐẲNG TÍCH trong hệ $(p, T)$: thẳng, qua gốc toạ độ.\n"
                 "Thể tích càng LỚN thì đường càng THOẢI (hệ số góc $nR/V$ nhỏ)",
                 fontsize=9.8, pad=8)
    ax.grid(alpha=0.22, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h26_do_thi_p_T_dang_tich")


def f27_pit_tong_hai_ngan():
    """Xilanh nằm ngang chia hai ngăn bởi pit-tông di động."""
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    ax.add_patch(Rectangle((0, 0), 7.0, 1.7, fill=False, ec="k", lw=2.4))
    ax.add_patch(Rectangle((0.05, 0.05), 3.35, 1.6, fc="#fdebd0", ec="none"))
    ax.add_patch(Rectangle((3.60, 0.05), 3.35, 1.6, fc="#d6eaf8", ec="none"))
    ax.add_patch(Rectangle((3.40, 0.05), 0.20, 1.6, fc="#34495e", ec="k", lw=1.0))
    ax.text(1.7, 0.85, "NGĂN A\n$p_A$, $V_A$, $T_A$", ha="center", va="center",
            fontsize=10, color=ORANGE)
    ax.text(5.3, 0.85, "NGĂN B\n$p_B$, $V_B$, $T_B$", ha="center", va="center",
            fontsize=10, color=BLUE)
    ax.text(3.50, 1.95, "pit-tông\nnhẹ, di động", ha="center", fontsize=9.2)
    arrow(ax, 3.05, -0.30, 3.35, -0.30, color=ORANGE, lw=1.6, ms=12)
    arrow(ax, 3.95, -0.30, 3.65, -0.30, color=BLUE, lw=1.6, ms=12)
    ax.text(3.50, -0.62, "Pit-tông cân bằng $\\Rightarrow$  $p_A = p_B$   "
                         "(nếu pit-tông nhẹ và không ma sát)",
            ha="center", va="top", fontsize=9.8, color=RED)
    ax.text(3.50, -1.35, "Ràng buộc thứ hai: tổng thể tích không đổi  "
                         "$V_A + V_B = V$ (hằng số)",
            ha="center", va="top", fontsize=9.8, color=GREEN)
    clean(ax, -0.4, 7.4, -2.4, 2.6, eq=False)
    save(fig, "h27_pit_tong_hai_ngan")


def f28_do_thi_pV_doc_hieu():
    """Đồ thị p-V có bốn điểm trạng thái - dùng cho bài đọc hiểu đồ thị."""
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    pts = {"A": (2.0, 3.0), "B": (6.0, 1.0), "C": (6.0, 3.0), "D": (2.0, 1.0)}
    V = np.linspace(1.4, 7.0, 200)
    ax.plot(V, 6.0 / V, color=GREY, lw=1.4, ls="--")
    ax.text(6.2, 1.15, "đường đẳng nhiệt qua A và B", fontsize=8.8, color=GREY, ha="left")
    for k, (x, y) in pts.items():
        ax.plot([x], [y], "o", color=RED, ms=8, zorder=6)
        ax.text(x + 0.18, y + 0.12, k, fontsize=13, fontweight="bold", color=RED)
    ax.plot([2.0, 6.0], [3.0, 3.0], color=GREEN, lw=1.2, ls=":")
    ax.plot([2.0, 2.0], [1.0, 3.0], color=BLUE, lw=1.2, ls=":")
    ax.plot([6.0, 6.0], [1.0, 3.0], color=BLUE, lw=1.2, ls=":")
    ax.plot([2.0, 6.0], [1.0, 1.0], color=GREEN, lw=1.2, ls=":")
    ax.set_xlabel("$V$ (L)", fontsize=11); ax.set_ylabel("$p$ ($10^5$ Pa)", fontsize=11)
    ax.set_xlim(0, 8); ax.set_ylim(0, 4)
    ax.set_xticks(range(0, 9))
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.grid(alpha=0.28, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    save(fig, "h28_do_thi_pV_doc_hieu")


def f29_noi_nang_khi():
    """Nội năng của khí lí tưởng chỉ gồm động năng phân tử."""
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.add_patch(FancyBboxPatch((0.2, 0.4), 3.1, 2.1, boxstyle="round,pad=0.1",
                                fc="#eaf2fb", ec=BLUE, lw=1.8))
    ax.text(1.75, 2.15, "VẬT THÔNG THƯỜNG", ha="center", fontsize=10.2,
            fontweight="bold", color=BLUE)
    ax.text(1.75, 1.35, "$U = W_{đ\\,phân\\,tử} + W_{t\\,tương\\,tác}$",
            ha="center", fontsize=11.5)
    ax.text(1.75, 0.72, "cả hai thành phần đều có mặt", ha="center", fontsize=9.2,
            style="italic", color=GREY)

    ax.add_patch(FancyBboxPatch((4.4, 0.4), 3.1, 2.1, boxstyle="round,pad=0.1",
                                fc="#fdf2f0", ec=RED, lw=1.8))
    ax.text(5.95, 2.15, "KHÍ LÍ TƯỞNG", ha="center", fontsize=10.2,
            fontweight="bold", color=RED)
    ax.text(5.95, 1.35, "$U = W_{đ\\,phân\\,tử}$  (chỉ phụ thuộc $T$)",
            ha="center", fontsize=11)
    ax.text(5.95, 0.72, "bỏ qua tương tác khi không va chạm\n→ không có thế năng tương tác",
            ha="center", fontsize=9.2, style="italic", color=GREY)

    ax.text(3.85, -0.45, "Hệ quả cực kì hay bị hỏi: với khí lí tưởng, "
                         "quá trình ĐẲNG NHIỆT có $\\Delta U = 0$,\n"
                         "do đó $Q = -A$ — khí nhận bao nhiêu nhiệt thì sinh bấy nhiêu công.",
            ha="center", va="top", fontsize=9.8, color=RED,
            bbox=dict(fc="#fef9e7", ec=ORANGE, lw=1.1, boxstyle="round,pad=0.35"))
    clean(ax, 0.0, 7.9, -1.9, 2.8, eq=False)
    save(fig, "h29_noi_nang_khi")


def f30_do_thi_boyle_thuc_nghiem():
    """Số liệu thí nghiệm Boyle: p theo 1/V với sai số."""
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.7))
    V = np.array([20.0, 25.0, 30.0, 40.0, 50.0])          # cm3
    p = np.array([1.50, 1.20, 1.00, 0.75, 0.60])          # 10^5 Pa (pV = 30)
    ax = axs[0]
    ax.plot(V, p, "o", color=RED, ms=7)
    Vs = np.linspace(17, 55, 200)
    ax.plot(Vs, 30.0 / Vs, color=BLUE, lw=1.8)
    ax.set_xlabel("$V$ (cm³)", fontsize=10.5); ax.set_ylabel("$p$ ($10^5$ Pa)", fontsize=10.5)
    ax.set_xlim(0, 58); ax.set_ylim(0, 1.9)
    ax.set_title("Số liệu thô: khó khẳng định là hypebol", fontsize=10, pad=7)
    ax.grid(alpha=0.25, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    ax = axs[1]
    ax.plot(1000.0 / V, p, "o", color=RED, ms=7)
    xs = np.linspace(0, 58, 50)
    ax.plot(xs, 0.030 * xs, color=BLUE, lw=1.8)
    ax.set_xlabel("$1/V$ ($10^{-3}$ cm$^{-3}$)", fontsize=10.5)
    ax.set_ylabel("$p$ ($10^5$ Pa)", fontsize=10.5)
    ax.set_xlim(0, 58); ax.set_ylim(0, 1.9)
    ax.set_title("Tuyến tính hoá: thẳng, qua gốc → kết luận chắc chắn", fontsize=10, pad=7)
    ax.grid(alpha=0.25, ls=":")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.subplots_adjust(wspace=0.28)
    save(fig, "h30_do_thi_boyle_thuc_nghiem")


ALL = [f01_cau_truc_chat, f02_the_nang_tuong_tac, f03_so_do_chuyen_the,
       f04_do_thi_dun_nuoc_da, f05_dinh_luat_1, f06_hai_cach_doi_noi_nang,
       f07_thang_nhiet_do, f08_can_bang_nhiet, f09_do_nhiet_dung_rieng,
       f10_do_thi_Q_deltaT, f11_do_nhiet_nong_chay, f12_bay_hoi_va_soi,
       f13_so_sanh_nhiet_dung, f14_do_thi_lam_nguoi,
       f15_chuyen_dong_brown, f16_mo_hinh_dong_hoc, f17_thi_nghiem_boyle,
       f18_do_thi_boyle, f19_thi_nghiem_charles, f20_do_thi_charles,
       f21_ba_dang_qua_trinh, f22_chu_trinh_pV, f23_phan_bo_toc_do,
       f24_ong_chu_U, f25_bom_xe_va_binh_khi, f26_do_thi_p_T_dang_tich,
       f27_pit_tong_hai_ngan, f28_do_thi_pV_doc_hieu, f29_noi_nang_khi,
       f30_do_thi_boyle_thuc_nghiem]


if __name__ == "__main__":
    print("Đang vẽ hình:")
    for f in ALL:
        f()
    print("Xong:", len(ALL), "hình")
