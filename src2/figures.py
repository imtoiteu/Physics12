# -*- coding: utf-8 -*-
"""Sinh toàn bộ hình vẽ gốc cho tài liệu Vật lí 12 - Chương III và Chương IV."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, Wedge, Polygon, Arc, Ellipse

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

RED, BLUE, GREEN, ORANGE, GREY = "#c0392b", "#1f4e9c", "#1e8449", "#d35400", "#555555"


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ", name)


def arrow(ax, x1, y1, x2, y2, color="k", lw=1.6, ms=12, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=ms, color=color, lw=lw, **kw))


def clean(ax, xl, xr, yb, yt):
    ax.set_xlim(xl, xr); ax.set_ylim(yb, yt)
    ax.set_aspect("equal"); ax.axis("off")


def cross(ax, x, y, s=0.09, color=BLUE, lw=1.3):
    ax.plot([x - s, x + s], [y - s, y + s], color=color, lw=lw)
    ax.plot([x - s, x + s], [y + s, y - s], color=color, lw=lw)


def dot_out(ax, x, y, r=0.10, color=BLUE):
    ax.add_patch(Circle((x, y), r, fill=False, ec=color, lw=1.3))
    ax.plot([x], [y], marker="o", ms=3, color=color)


# ---------------------------------------------------------------- CHƯƠNG III
def fig_nam_cham_thang():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    Y, X = np.mgrid[-2.0:2.0:240j, -3.0:3.0:240j]
    d = 0.85
    def dip(px, py, q):
        rx, ry = X - px, Y - py
        r = np.sqrt(rx**2 + ry**2) + 1e-9
        return q * rx / r**3, q * ry / r**3
    ux1, uy1 = dip(d, 0, 1.0)
    ux2, uy2 = dip(-d, 0, -1.0)
    U, V = ux1 + ux2, uy1 + uy2
    mask = ((np.abs(X) < d + 0.42) & (np.abs(Y) < 0.30))
    U = np.ma.array(U, mask=mask); V = np.ma.array(V, mask=mask)
    ax.streamplot(X, Y, U, V, color=GREY, density=0.75, linewidth=0.9,
                  arrowsize=1.0, broken_streamlines=False)
    ax.add_patch(Rectangle((-d - 0.42, -0.28), (d + 0.42), 0.56, fc=BLUE, ec="k", zorder=5))
    ax.add_patch(Rectangle((0, -0.28), (d + 0.42), 0.56, fc=RED, ec="k", zorder=5))
    ax.text(-0.62, 0, "S", color="w", ha="center", va="center", fontsize=15, fontweight="bold", zorder=6)
    ax.text(0.62, 0, "N", color="w", ha="center", va="center", fontsize=15, fontweight="bold", zorder=6)
    clean(ax, -3.0, 3.0, -2.0, 2.0)
    ax.set_title("Đường sức từ của nam châm thẳng", fontsize=11.5, fontweight="bold", pad=10)
    fig.text(0.5, -0.02, "Bên ngoài nam châm, đường sức từ đi ra từ cực Bắc (N) và đi vào cực Nam (S)",
             ha="center", fontsize=8.8, style="italic")
    save(fig, "f01_nam_cham_thang")


def fig_dong_dien_thang():
    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    for r in (0.55, 1.0, 1.45, 1.9):
        ax.add_patch(Circle((0, 0), r, fill=False, ec=GREY, lw=1.2))
        th = np.deg2rad(55)
        p = (r * np.cos(th), r * np.sin(th))
        t = (-np.sin(th), np.cos(th))
        arrow(ax, p[0] - 0.02 * t[0], p[1] - 0.02 * t[1],
              p[0] + 0.02 * t[0], p[1] + 0.02 * t[1], color=GREY, ms=13)
        th2 = np.deg2rad(235)
        p = (r * np.cos(th2), r * np.sin(th2))
        t = (-np.sin(th2), np.cos(th2))
        arrow(ax, p[0] - 0.02 * t[0], p[1] - 0.02 * t[1],
              p[0] + 0.02 * t[0], p[1] + 0.02 * t[1], color=GREY, ms=13)
    ax.add_patch(Circle((0, 0), 0.17, fc="w", ec=RED, lw=2.0, zorder=5))
    ax.plot([0], [0], marker="o", ms=5, color=RED, zorder=6)
    ax.text(0.32, 0.05, "I", color=RED, fontsize=13, fontweight="bold")
    ax.annotate("Dòng điện hướng ra\nngoài mặt phẳng hình vẽ",
                xy=(0.05, 0.05), xytext=(1.15, -1.85), fontsize=8.6, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    ax.text(1.55, 1.42, r"$B=$ hằng số trên mỗi đường tròn", fontsize=8.6, color=GREY)
    ax.text(0, 2.25, "Từ trường của dòng điện thẳng dài", ha="center", fontsize=11, fontweight="bold")
    ax.text(0, -2.42, "Quy tắc nắm tay phải: ngón cái chỉ chiều dòng điện,\ncác ngón còn lại khum theo chiều đường sức từ",
            ha="center", fontsize=8.6, style="italic")
    clean(ax, -2.3, 2.6, -2.75, 2.5)
    save(fig, "f02_dong_dien_thang")


def fig_ong_day():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    x1, r = 1.55, 0.60
    for x in np.linspace(-x1, x1, 9):
        ax.add_patch(Ellipse((x, 0), 0.19, 2 * r, fill=False, ec="#8a5a2b", lw=1.9, zorder=4))
    for y in np.linspace(-0.40, 0.40, 5):
        arrow(ax, -x1 - 0.10, y, x1 + 0.10, y, color=GREY, lw=1.0, ms=11, zorder=3)
    th = np.linspace(0, 2 * np.pi, 700)
    for aa, bb in [(x1 + 0.35, r + 0.22), (x1 + 0.78, r + 0.62), (x1 + 1.30, r + 1.05)]:
        xs, ys = aa * np.cos(th), bb * np.sin(th)
        inside = (np.abs(xs) < x1 + 0.02) & (np.abs(ys) < r + 0.02)
        xs = np.where(inside, np.nan, xs); ys = np.where(inside, np.nan, ys)
        ax.plot(xs, ys, color=GREY, lw=1.0, zorder=2)
        for sgn in (1, -1):
            k = int(len(th) * (0.25 if sgn > 0 else 0.75))
            arrow(ax, xs[k - 4], ys[k - 4], xs[k + 4], ys[k + 4], color=GREY, lw=1.0, ms=11, zorder=2)
    ax.text(x1 + 0.20, 0.16, "N", fontsize=14, fontweight="bold", color=RED, zorder=6)
    ax.text(-x1 - 0.42, 0.16, "S", fontsize=14, fontweight="bold", color=BLUE, zorder=6)
    ax.text(0, -0.95, "Bên trong ống dây: từ trường đều", ha="center", fontsize=9, color=GREEN,
            bbox=dict(fc="white", ec="none", pad=1.5), zorder=7)
    arrow(ax, -2.55, -1.55, -2.05, -1.55, color=RED, ms=11)
    ax.text(-2.85, -1.62, "I", color=RED, fontsize=12, fontweight="bold")
    clean(ax, -3.2, 3.2, -1.95, 1.85)
    ax.set_title("Từ trường của ống dây có dòng điện chạy qua", fontsize=11.5, fontweight="bold", pad=8)
    fig.text(0.5, -0.02, "Đường sức từ bên trong gần như song song và cách đều; bên ngoài giống từ trường nam châm thẳng",
             ha="center", fontsize=8.6, style="italic")
    save(fig, "f03_ong_day")


def fig_luc_tu():
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    for x in np.linspace(-1.7, 1.7, 7):
        for y in np.linspace(-1.15, 1.15, 5):
            cross(ax, x, y)
    ax.plot([-1.95, 1.95], [0, 0], color=RED, lw=3.0, zorder=4)
    arrow(ax, 0.25, 0, 0.95, 0, color=RED, lw=2.4, ms=15)
    ax.text(0.55, -0.30, "I", color=RED, fontsize=13, fontweight="bold")
    ax.plot([-0.9, -0.9], [-0.06, 0.06], color="k", lw=1.2)
    ax.plot([0.9, 0.9], [-0.06, 0.06], color="k", lw=1.2)
    ax.annotate("", xy=(0.9, 0.34), xytext=(-0.9, 0.34),
                arrowprops=dict(arrowstyle="<->", color="k", lw=1.0))
    ax.text(0, 0.44, r"$\ell$", ha="center", fontsize=11)
    arrow(ax, 0, 0, 0, 1.35, color=GREEN, lw=2.4, ms=15)
    ax.text(0.10, 1.20, r"$\vec{F}$", color=GREEN, fontsize=14, fontweight="bold")
    ax.text(-2.55, 1.05, r"$\vec{B}$ hướng vào" + "\ntrong mặt phẳng", color=BLUE, fontsize=9)
    ax.text(0, -1.72, r"$F = BI\ell\sin\theta$   ($\theta$ là góc giữa dây dẫn và $\vec{B}$; ở đây $\theta = 90^\circ$)",
            ha="center", fontsize=10.5)
    ax.text(0, -2.12, "Chiều của lực từ xác định bằng quy tắc bàn tay trái",
            ha="center", fontsize=8.6, style="italic")
    ax.text(0, 1.95, "Lực từ tác dụng lên đoạn dây dẫn mang dòng điện",
            ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.7, 2.4, -2.3, 2.1)
    save(fig, "f04_luc_tu")


def fig_goc_theta():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4))
    ax = axes[0]
    for x in np.linspace(-1.3, 1.3, 6):
        arrow(ax, x, -1.0, x, 1.0, color=BLUE, lw=0.9, ms=9)
    th = np.deg2rad(35)
    L = 1.15
    ax.plot([-L * np.cos(th), L * np.cos(th)], [-L * np.sin(th), L * np.sin(th)],
            color=RED, lw=3.0, zorder=5)
    arrow(ax, 0, 0, 0.55 * np.cos(th), 0.55 * np.sin(th), color=RED, lw=2.2, ms=13, zorder=6)
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=np.rad2deg(th), theta2=90, color="k", lw=1.0))
    ax.text(0.30, 0.44, r"$\theta$", fontsize=12)
    ax.text(-1.55, 0.85, r"$\vec{B}$", color=BLUE, fontsize=13)
    ax.text(0.75, 0.30, "I", color=RED, fontsize=12, fontweight="bold")
    ax.set_title("Góc giữa dây dẫn và $\\vec{B}$", fontsize=10)
    clean(ax, -1.7, 1.7, -1.25, 1.35)

    ax = axes[1]
    t = np.linspace(0, 180, 400)
    ax.plot(t, np.sin(np.deg2rad(t)), color=GREEN, lw=2.0)
    ax.set_xticks([0, 30, 60, 90, 120, 150, 180])
    ax.set_xlabel(r"$\theta$ (độ)"); ax.set_ylabel(r"$F/(BI\ell)$")
    ax.grid(alpha=0.35)
    ax.axvline(90, color=GREY, ls="--", lw=0.9)
    ax.annotate(r"$F_{max}=BI\ell$", xy=(90, 1.0), xytext=(96, 0.75), fontsize=9,
                arrowprops=dict(arrowstyle="->", lw=0.9))
    ax.annotate(r"$F=0$ khi dây song song $\vec{B}$", xy=(0, 0), xytext=(12, 0.22), fontsize=8.6,
                arrowprops=dict(arrowstyle="->", lw=0.9))
    ax.set_title(r"Sự phụ thuộc $F(\theta)$", fontsize=10)
    fig.tight_layout()
    save(fig, "f05_goc_theta")


def fig_can_dong_dien():
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    ax.add_patch(Rectangle((-1.5, 0.55), 3.0, 0.42, fc=RED, ec="k"))
    ax.add_patch(Rectangle((-1.5, -0.97), 3.0, 0.42, fc=BLUE, ec="k"))
    ax.text(-1.72, 0.72, "N", fontsize=12, fontweight="bold", color=RED)
    ax.text(-1.72, -0.82, "S", fontsize=12, fontweight="bold", color=BLUE)
    for x in np.linspace(-1.2, 1.2, 7):
        arrow(ax, x, 0.52, x, -0.52, color=BLUE, lw=0.9, ms=9)
    ax.text(1.62, 0.05, r"$\vec{B}$", color=BLUE, fontsize=12)
    ax.plot([-2.3, 2.3], [0, 0], color="#8a5a2b", lw=3.0, zorder=5)
    arrow(ax, -0.4, 0, 0.4, 0, color="#8a5a2b", lw=2.0, ms=13, zorder=6)
    ax.text(0, 0.18, "I", fontsize=11, fontweight="bold", color="#8a5a2b")
    ax.text(-2.05, 0.20, r"đoạn dây $\ell$", fontsize=8.4)
    arrow(ax, 0, 0, 0, -1.7, color=GREEN, lw=2.2, ms=14, zorder=7)
    ax.text(0.10, -1.5, r"$\vec{F}$", color=GREEN, fontsize=13)
    ax.add_patch(Rectangle((-0.75, -2.55), 1.5, 0.55, fc="#eeeeee", ec="k"))
    ax.text(0, -2.28, "CÂN ĐIỆN TỬ", ha="center", fontsize=8.5)
    ax.text(0, -3.0, r"Số chỉ của cân thay đổi $\Delta m$   $\Rightarrow$   $F = \Delta m\,g = BI\ell$   $\Rightarrow$   $B = \dfrac{\Delta m\, g}{I\ell}$",
            ha="center", fontsize=10)
    ax.text(0, 1.35, "Đo cảm ứng từ bằng “cân dòng điện”", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.8, 2.8, -3.3, 1.6)
    save(fig, "f06_can_dong_dien")


def fig_tu_thong():
    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    ax.add_patch(Ellipse((0, 0), 2.4, 1.15, fill=False, ec="#8a5a2b", lw=2.6))
    ax.text(-1.45, -0.45, "S", fontsize=12, color="#8a5a2b", fontweight="bold")
    a = np.deg2rad(35)
    arrow(ax, 0, 0, 1.55 * np.cos(a), 1.55 * np.sin(a), color=BLUE, lw=2.0, ms=14)
    ax.text(1.35, 1.20, r"$\vec{B}$", color=BLUE, fontsize=13)
    for k in (-1, 1):
        arrow(ax, k * 0.75, -0.30, k * 0.75 + 1.25 * np.cos(a), -0.30 + 1.25 * np.sin(a),
              color=BLUE, lw=1.0, ms=10)
    arrow(ax, 0, 0, 0, 1.5, color=GREEN, lw=2.0, ms=14)
    ax.text(-0.30, 1.35, r"$\vec{n}$", color=GREEN, fontsize=13)
    ax.add_patch(Arc((0, 0), 1.5, 1.5, theta1=np.rad2deg(a), theta2=90, color="k", lw=1.0))
    ax.text(0.40, 0.86, r"$\alpha$", fontsize=12)
    ax.text(0, -1.55, r"$\Phi = NBS\cos\alpha$      đơn vị: vêbe (Wb),  $1\ \mathrm{Wb} = 1\ \mathrm{T\cdot m^2}$",
            ha="center", fontsize=10.5)
    ax.text(0, -1.95, r"$\alpha$ là góc giữa pháp tuyến $\vec{n}$ của mặt phẳng khung và vectơ $\vec{B}$",
            ha="center", fontsize=8.6, style="italic")
    ax.text(0, 2.05, "Từ thông qua khung dây N vòng", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.2, 2.2, -2.2, 2.2)
    save(fig, "f07_tu_thong")


def fig_thi_nghiem_faraday():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for i, x in enumerate(np.linspace(0.15, 1.35, 7)):
        ax.add_patch(Ellipse((x, 0), 0.16, 1.25, fill=False, ec="#8a5a2b", lw=1.8))
    ax.plot([0.15, -0.35], [-0.62, -1.15], color="#8a5a2b", lw=1.4)
    ax.plot([1.35, 1.85], [-0.62, -1.15], color="#8a5a2b", lw=1.4)
    ax.plot([-0.35, 1.85], [-1.15, -1.15], color="#8a5a2b", lw=1.4)
    ax.add_patch(Circle((0.75, -1.15), 0.30, fc="w", ec="k", lw=1.6, zorder=5))
    ax.text(0.75, -1.15, "G", ha="center", va="center", fontsize=12, fontweight="bold", zorder=6)
    ax.add_patch(Rectangle((-2.35, -0.22), 0.75, 0.44, fc=BLUE, ec="k"))
    ax.add_patch(Rectangle((-1.60, -0.22), 0.75, 0.44, fc=RED, ec="k"))
    ax.text(-1.97, 0, "S", color="w", ha="center", va="center", fontweight="bold")
    ax.text(-1.22, 0, "N", color="w", ha="center", va="center", fontweight="bold")
    arrow(ax, -0.75, 0.55, -0.05, 0.55, color=GREEN, lw=2.0, ms=14)
    ax.text(-0.55, 0.72, r"$\vec{v}$", color=GREEN, fontsize=12)
    ax.text(0.75, 1.15, "Đưa nam châm lại gần ống dây", ha="center", fontsize=9.5)
    ax.text(-0.3, -1.85, "Kim điện kế lệch $\\Rightarrow$ trong mạch kín xuất hiện dòng điện cảm ứng",
            fontsize=8.8, style="italic")
    ax.text(0.4, 1.75, "Thí nghiệm về hiện tượng cảm ứng điện từ", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.6, 2.6, -2.1, 2.0)
    save(fig, "f08_thi_nghiem_faraday")


def fig_lenz():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.4))
    for k, ax in enumerate(axes):
        for x in np.linspace(0.15, 1.05, 5):
            ax.add_patch(Ellipse((x, 0), 0.14, 1.1, fill=False, ec="#8a5a2b", lw=1.7))
        ax.add_patch(Rectangle((-1.95, -0.20), 0.62, 0.40, fc=BLUE, ec="k"))
        ax.add_patch(Rectangle((-1.33, -0.20), 0.62, 0.40, fc=RED, ec="k"))
        ax.text(-1.64, 0, "S", color="w", ha="center", va="center", fontsize=9, fontweight="bold")
        ax.text(-1.02, 0, "N", color="w", ha="center", va="center", fontsize=9, fontweight="bold")
        if k == 0:
            arrow(ax, -0.62, 0.52, -0.02, 0.52, color=GREEN, lw=1.8, ms=13)
            ax.text(-0.45, 0.70, r"$\vec{v}$", color=GREEN, fontsize=11)
            ax.text(0.15, -1.05, "Φ tăng", fontsize=9.5, color=RED)
            ax.text(0.12, 0.80, "N", fontsize=11, color=RED, fontweight="bold")
            ax.set_title("Nam châm lại gần: ống dây đẩy nam châm", fontsize=9.5)
            ax.text(0.05, -1.45, "Mặt đối diện thành cực N $\\Rightarrow$ lực đẩy", fontsize=8.3)
        else:
            arrow(ax, -0.02, 0.52, -0.62, 0.52, color=GREEN, lw=1.8, ms=13)
            ax.text(-0.45, 0.70, r"$\vec{v}$", color=GREEN, fontsize=11)
            ax.text(0.15, -1.05, "Φ giảm", fontsize=9.5, color=BLUE)
            ax.text(0.12, 0.80, "S", fontsize=11, color=BLUE, fontweight="bold")
            ax.set_title("Nam châm ra xa: ống dây hút nam châm", fontsize=9.5)
            ax.text(0.05, -1.45, "Mặt đối diện thành cực S $\\Rightarrow$ lực hút", fontsize=8.3)
        clean(ax, -2.1, 1.9, -1.75, 1.25)
    fig.suptitle("Định luật Lenz: dòng điện cảm ứng chống lại nguyên nhân sinh ra nó",
                 fontsize=10.5, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "f09_lenz")


def fig_may_phat():
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.add_patch(Rectangle((-2.2, 0.95), 1.2, 0.42, fc=RED, ec="k"))
    ax.add_patch(Rectangle((-2.2, -1.37), 1.2, 0.42, fc=BLUE, ec="k"))
    ax.text(-2.45, 1.05, "N", fontsize=12, fontweight="bold", color=RED)
    ax.text(-2.45, -1.30, "S", fontsize=12, fontweight="bold", color=BLUE)
    for x in np.linspace(-2.05, -1.15, 4):
        arrow(ax, x, 0.92, x, -0.92, color=BLUE, lw=0.9, ms=9)
    ax.add_patch(Rectangle((-1.85, -0.62), 1.55, 1.24, fill=False, ec="#8a5a2b", lw=2.4))
    ax.add_patch(Arc((-1.07, 0), 1.3, 1.3, theta1=-40, theta2=40, color=GREEN, lw=1.5))
    arrow(ax, -0.50, 0.42, -0.44, 0.30, color=GREEN, lw=1.5, ms=11)
    ax.text(-1.07, 0.80, "quay đều " + r"$\omega$", color=GREEN, fontsize=9, ha="center",
            bbox=dict(fc="white", ec="none", pad=1.2), zorder=9)
    for y in (0.22, -0.22):
        ax.add_patch(Ellipse((0.35, y), 0.16, 0.34, fc="#cccccc", ec="k"))
        ax.plot([-0.30, 0.27], [y * 1.6, y], color="#8a5a2b", lw=1.4)
        ax.plot([0.43, 0.95], [y, y], color="k", lw=1.4)
    ax.text(0.42, -0.72, "vành khuyên\n+ chổi quét", ha="center", fontsize=7.8)
    ax.add_patch(Circle((1.45, 0), 0.32, fc="w", ec="k", lw=1.6))
    ax.text(1.45, 0, "R", ha="center", va="center", fontsize=11)
    ax.plot([0.95, 0.95, 1.13], [0.22, 0.22, 0.22], color="k", lw=1.4)
    ax.plot([0.95, 1.13], [-0.22, -0.22], color="k", lw=1.4)
    ax.plot([1.13, 1.13], [0.22, 0.13], color="k", lw=1.4)
    ax.plot([1.13, 1.13], [-0.22, -0.13], color="k", lw=1.4)
    ax.text(0, -1.95, r"$\Phi = NBS\cos\omega t \Rightarrow e = -\frac{\Delta\Phi}{\Delta t} = E_0\sin\omega t$,  $E_0 = NBS\omega$",
            ha="center", fontsize=10)
    ax.text(0, 1.85, "Nguyên tắc máy phát điện xoay chiều", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.8, 2.3, -2.3, 2.1)
    save(fig, "f10_may_phat")


def fig_phi_e():
    fig, axes = plt.subplots(2, 1, figsize=(6.6, 4.2), sharex=True)
    t = np.linspace(0, 2, 500)
    axes[0].plot(t, np.cos(2 * np.pi * t), color=BLUE, lw=2.0)
    axes[0].set_ylabel(r"$\Phi$"); axes[0].grid(alpha=0.35)
    axes[0].axhline(0, color="k", lw=0.8)
    axes[0].set_title(r"$\Phi = \Phi_0\cos\omega t$", fontsize=10)
    axes[1].plot(t, np.sin(2 * np.pi * t), color=RED, lw=2.0)
    axes[1].set_ylabel(r"$e$"); axes[1].set_xlabel(r"$t/T$"); axes[1].grid(alpha=0.35)
    axes[1].axhline(0, color="k", lw=0.8)
    axes[1].set_title(r"$e = E_0\sin\omega t$  (trễ pha $\pi/2$ so với $\Phi$)", fontsize=10)
    for ax in axes:
        ax.axvline(0.25, color=GREY, ls="--", lw=0.9)
        ax.axvline(0.5, color=GREY, ls="--", lw=0.9)
    axes[0].annotate("Φ = 0 nhưng |e| cực đại", xy=(0.25, 0), xytext=(0.42, 0.55),
                     fontsize=8.2, arrowprops=dict(arrowstyle="->", lw=0.8))
    axes[1].annotate("|Φ| cực đại nhưng e = 0", xy=(0.5, 0), xytext=(0.62, 0.55),
                     fontsize=8.2, arrowprops=dict(arrowstyle="->", lw=0.8))
    fig.tight_layout()
    save(fig, "f11_phi_e")


def fig_hieu_dung():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    t = np.linspace(0, 2, 600)
    i = np.cos(2 * np.pi * t)
    ax.plot(t, i, color=RED, lw=2.0, label=r"$i = I_0\cos\omega t$")
    ax.axhline(1, color=GREY, ls=":", lw=1.0)
    ax.axhline(1 / np.sqrt(2), color=GREEN, ls="--", lw=1.4,
               label=r"$I = I_0/\sqrt{2} \approx 0{,}707 I_0$")
    ax.axhline(0, color="k", lw=0.8)
    ax.text(2.02, 1.0, r"$I_0$", color=GREY, fontsize=10, va="center")
    ax.text(2.02, 0.707, r"$I$", color=GREEN, fontsize=10, va="center")
    ax.set_xlabel(r"$t/T$"); ax.set_ylabel("i")
    ax.grid(alpha=0.35); ax.legend(fontsize=8.5, loc="lower right")
    ax.set_title("Giá trị cực đại và giá trị hiệu dụng của dòng điện xoay chiều", fontsize=10.5)
    fig.tight_layout()
    save(fig, "f12_hieu_dung")


def fig_bien_ap():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.add_patch(Rectangle((-1.1, -1.0), 2.2, 2.0, fill=False, ec="#7f8c8d", lw=7))
    for y in np.linspace(-0.62, 0.62, 6):
        ax.add_patch(Arc((-1.1, y), 0.42, 0.20, theta1=90, theta2=270, color="#b7791f", lw=2.0))
    for y in np.linspace(-0.72, 0.72, 8):
        ax.add_patch(Arc((1.1, y), 0.42, 0.18, theta1=-90, theta2=90, color="#b7791f", lw=2.0))
    ax.plot([-1.35, -2.0], [0.62, 0.62], color="k", lw=1.3)
    ax.plot([-1.35, -2.0], [-0.62, -0.62], color="k", lw=1.3)
    ax.add_patch(Circle((-2.0, 0), 0.30, fc="w", ec="k", lw=1.4))
    ax.text(-2.0, 0, "~", ha="center", va="center", fontsize=15)
    ax.plot([-2.0, -2.0], [0.62, 0.30], color="k", lw=1.3)
    ax.plot([-2.0, -2.0], [-0.62, -0.30], color="k", lw=1.3)
    ax.plot([1.35, 2.0], [0.72, 0.72], color="k", lw=1.3)
    ax.plot([1.35, 2.0], [-0.72, -0.72], color="k", lw=1.3)
    ax.add_patch(Rectangle((1.85, -0.30), 0.30, 0.60, fc="w", ec="k", lw=1.4))
    ax.plot([2.0, 2.0], [0.72, 0.30], color="k", lw=1.3)
    ax.plot([2.0, 2.0], [-0.72, -0.30], color="k", lw=1.3)
    ax.text(-1.75, 1.05, r"$U_1,\ N_1$", fontsize=10, color=BLUE)
    ax.text(1.35, 1.05, r"$U_2,\ N_2$", fontsize=10, color=RED)
    ax.text(0, 0, "Lõi sắt\n(khép kín)", ha="center", va="center", fontsize=8.6)
    ax.text(0, -1.62, r"$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$;  nếu hao phí không đáng kể: $U_1I_1 = U_2I_2$",
            ha="center", fontsize=10.5)
    ax.text(0, 1.72, "Máy biến áp", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.7, 2.7, -2.0, 2.0)
    save(fig, "f13_bien_ap")


def fig_song_dien_tu():
    fig = plt.figure(figsize=(6.8, 3.6))
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(0, 4 * np.pi, 300)
    E = np.sin(x); B = np.sin(x)
    ax.plot(x, np.zeros_like(x), E, color=RED, lw=2.0)
    ax.plot(x, B, np.zeros_like(x), color=BLUE, lw=2.0)
    for xi in np.linspace(0, 4 * np.pi, 17):
        ax.plot([xi, xi], [0, 0], [0, np.sin(xi)], color=RED, lw=0.7, alpha=0.55)
        ax.plot([xi, xi], [0, np.sin(xi)], [0, 0], color=BLUE, lw=0.7, alpha=0.55)
    ax.plot(x, np.zeros_like(x), np.zeros_like(x), color="k", lw=1.0)
    ax.text(4 * np.pi + 0.5, 0, 0, "v", fontsize=12, color=GREEN)
    ax.text(1.6, 0, 1.25, "E", fontsize=12, color=RED)
    ax.text(1.6, 1.25, 0, "B", fontsize=12, color=BLUE)
    ax.set_axis_off()
    ax.view_init(elev=18, azim=-62)
    ax.set_title("Mô hình sóng điện từ: $\\vec{E} \\perp \\vec{B} \\perp \\vec{v}$ — sóng ngang",
                 fontsize=10.5, y=0.95)
    save(fig, "f14_song_dien_tu")


def fig_phi_gap_khuc():
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    t = [0, 2, 4, 5, 8]
    p = [0, 0.8, 0.8, 0.2, 0.2]
    ax.plot(t, p, color=BLUE, lw=2.2, marker="o", ms=5)
    ax.set_xlabel("t (s)"); ax.set_ylabel(r"$\Phi$ (Wb)")
    ax.grid(alpha=0.4)
    ax.set_xticks(range(0, 9)); ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.set_ylim(-0.05, 1.0)
    for a, b, lab in [(0, 2, "(1)"), (2, 4, "(2)"), (4, 5, "(3)"), (5, 8, "(4)")]:
        ax.text((a + b) / 2, 0.92, lab, ha="center", fontsize=10, color=RED)
        ax.axvspan(a, b, alpha=0.05, color=RED if lab in ("(1)", "(3)") else GREY)
    ax.set_title(r"Đồ thị từ thông $\Phi$ qua một vòng dây theo thời gian", fontsize=10.5)
    fig.tight_layout()
    save(fig, "f15_phi_gap_khuc")


def fig_thanh_truot():
    fig, ax = plt.subplots(figsize=(6.0, 3.4))
    for x in np.linspace(-1.7, 1.9, 8):
        for y in np.linspace(-0.75, 0.95, 4):
            dot_out(ax, x, y, r=0.07)
    ax.plot([-2.1, 2.1], [1.15, 1.15], color="k", lw=2.2)
    ax.plot([-2.1, 2.1], [-1.05, -1.05], color="k", lw=2.2)
    ax.plot([-2.1, -2.1], [-1.05, 1.15], color="k", lw=2.2)
    ax.add_patch(Rectangle((-2.28, -0.18), 0.36, 0.46, fc="w", ec="k", lw=1.4))
    ax.text(-2.1, 0.05, "R", ha="center", va="center", fontsize=10)
    ax.plot([0.55, 0.55], [-1.05, 1.15], color=RED, lw=3.5)
    arrow(ax, 0.55, 1.42, 1.45, 1.42, color=GREEN, lw=2.0, ms=14)
    ax.text(0.95, 1.58, r"$\vec{v}$", color=GREEN, fontsize=12)
    ax.text(2.25, 0.05, r"$\ell$", fontsize=11)
    ax.annotate("", xy=(2.15, 1.15), xytext=(2.15, -1.05),
                arrowprops=dict(arrowstyle="<->", lw=1.0))
    ax.text(-1.35, 1.55, r"$\vec{B}$ hướng ra ngoài", color=BLUE, fontsize=9.5)
    ax.text(0, -1.62, r"$e = B\ell v$   (thanh trượt đều, tiếp xúc tốt với hai thanh ray)",
            ha="center", fontsize=10)
    ax.text(0, 2.0, "Suất điện động cảm ứng trên thanh dẫn chuyển động",
            ha="center", fontsize=11, fontweight="bold")
    clean(ax, -2.7, 2.8, -2.0, 2.2)
    save(fig, "f16_thanh_truot")


# ---------------------------------------------------------------- CHƯƠNG IV
def fig_cau_tao_hat_nhan():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.text(0.55, 0.30, r"$^{A}_{Z}\mathrm{X}$", fontsize=40)
    ax.annotate("số khối A = số nucleon  (A = Z + N)", xy=(0.66, 0.62), xytext=(1.35, 1.10),
                fontsize=9.5, arrowprops=dict(arrowstyle="->", lw=1.0))
    ax.annotate("kí hiệu hoá học của nguyên tố", xy=(0.90, 0.42), xytext=(1.35, 0.48),
                fontsize=9.5, arrowprops=dict(arrowstyle="->", lw=1.0))
    ax.annotate("số proton Z (số hiệu nguyên tử)", xy=(0.66, 0.22), xytext=(1.35, -0.12),
                fontsize=9.5, arrowprops=dict(arrowstyle="->", lw=1.0))
    rng = np.random.default_rng(3)
    cx, cy, R = -0.75, 0.55, 0.52
    for i in range(14):
        a = rng.uniform(0, 2 * np.pi); r = R * np.sqrt(rng.uniform(0, 0.72))
        c = RED if i % 2 == 0 else BLUE
        ax.add_patch(Circle((cx + r * np.cos(a), cy + r * np.sin(a)), 0.10, fc=c, ec="k", lw=0.6))
    ax.add_patch(Circle((cx, cy), R, fill=False, ec=GREY, ls="--", lw=1.2))
    ax.add_patch(Circle((cx - 0.42, cy - 1.05), 0.075, fc=RED, ec="k", lw=0.6))
    ax.text(cx - 0.30, cy - 1.09, "proton (p)", fontsize=9)
    ax.add_patch(Circle((cx + 0.52, cy - 1.05), 0.075, fc=BLUE, ec="k", lw=0.6))
    ax.text(cx + 0.64, cy - 1.09, "neutron (n)", fontsize=9)
    ax.text(cx, cy + 0.70, "Hạt nhân", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(0.85, -0.95, r"$R \approx 1{,}2\cdot 10^{-15}\,A^{1/3}$ (m): bán kính hạt nhân",
            fontsize=9.5, ha="center")
    clean(ax, -1.6, 3.3, -1.25, 1.45)
    save(fig, "f17_cau_tao_hat_nhan")


def fig_rutherford():
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.add_patch(Arc((0, 0), 5.6, 5.6, theta1=-140, theta2=140, color="#bfc9ca", lw=7))
    ax.annotate("màn huỳnh quang", xy=(2.42, -1.42), xytext=(1.30, -2.35),
                fontsize=8.8, color=GREY,
                arrowprops=dict(arrowstyle="->", color=GREY, lw=0.9))
    ax.add_patch(Rectangle((-2.75, -0.28), 0.60, 0.56, fc="#7f8c8d", ec="k"))
    ax.text(-2.45, -0.62, "nguồn α", ha="center", fontsize=8.8)
    ax.add_patch(Rectangle((-0.03, -1.35), 0.08, 2.7, fc="#f1c40f", ec="k"))
    ax.text(0.01, 1.52, "lá vàng mỏng", ha="center", fontsize=8.8)
    for y in (-0.62, -0.21, 0.21, 0.62):
        arrow(ax, -2.10, y, 2.45, y, color=GREEN, lw=1.0, ms=9)
    ax.plot([-2.10, -0.02], [0.02, 0.02], color=RED, lw=1.3)
    arrow(ax, -0.02, 0.02, 1.72, 1.92, color=RED, lw=1.3, ms=11)
    ax.plot([-2.10, -0.02], [-0.98, -0.98], color=RED, lw=1.3)
    arrow(ax, -0.02, -0.98, -1.62, -2.05, color=RED, lw=1.3, ms=11)
    ax.text(1.35, -0.95, "đa số hạt α truyền thẳng", fontsize=8.6, color=GREEN)
    ax.text(-3.15, -2.35, "rất ít hạt α bị lệch\ngóc lớn, thậm chí\nbật ngược trở lại",
            fontsize=8.4, color=RED)
    clean(ax, -3.3, 3.4, -3.0, 2.35)
    ax.set_title("Thí nghiệm tán xạ hạt α của Rutherford", fontsize=11.5, fontweight="bold", pad=8)
    fig.text(0.5, -0.02, "Kết luận: nguyên tử có hạt nhân rất nhỏ, mang điện dương và tập trung hầu hết khối lượng",
             ha="center", fontsize=8.8, style="italic")
    save(fig, "f18_rutherford")


def fig_nllk_rieng():
    A = np.array([2, 3, 4, 6, 7, 9, 11, 12, 14, 16, 20, 24, 27, 32, 40, 45, 51, 56, 59, 63,
                  75, 84, 98, 107, 120, 133, 141, 152, 165, 178, 190, 197, 208, 220, 232, 235, 238])
    E = np.array([1.11, 2.83, 7.07, 5.33, 5.61, 6.46, 6.93, 7.68, 7.48, 7.98, 8.03, 8.26, 8.33,
                  8.49, 8.55, 8.72, 8.71, 8.79, 8.77, 8.75, 8.71, 8.72, 8.63, 8.55, 8.50, 8.41,
                  8.35, 8.23, 8.13, 8.05, 7.95, 7.91, 7.87, 7.78, 7.62, 7.59, 7.57])
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    ax.plot(A, E, "-o", color=BLUE, ms=3.4, lw=1.6)
    ax.axhline(8.79, color=GREY, ls=":", lw=1.0)
    ax.annotate(r"$^{56}$Fe: 8,79 MeV/nucleon" + "\n(bền vững nhất)", xy=(56, 8.79),
                xytext=(78, 6.7), fontsize=9, arrowprops=dict(arrowstyle="->", lw=1.0))
    ax.annotate(r"$^{4}$He rất bền", xy=(4, 7.07), xytext=(14, 4.4), fontsize=8.6,
                arrowprops=dict(arrowstyle="->", lw=0.9))
    ax.annotate(r"$^{235}$U", xy=(235, 7.59), xytext=(206, 5.9), fontsize=8.6,
                arrowprops=dict(arrowstyle="->", lw=0.9))
    ax.axvspan(0, 56, alpha=0.07, color=GREEN)
    ax.axvspan(56, 245, alpha=0.07, color=ORANGE)
    ax.text(22, 1.15, "TỔNG HỢP\n(nhiệt hạch)", fontsize=8.8, color=GREEN, ha="center", fontweight="bold")
    ax.text(160, 1.15, "PHÂN HẠCH", fontsize=8.8, color=ORANGE, ha="center", fontweight="bold")
    arrow(ax, 12, 2.4, 42, 2.4, color=GREEN, lw=1.4, ms=12)
    arrow(ax, 205, 2.4, 130, 2.4, color=ORANGE, lw=1.4, ms=12)
    ax.set_xlabel("Số khối A"); ax.set_ylabel(r"$E_{lk}/A$ (MeV/nucleon)")
    ax.set_xlim(0, 245); ax.set_ylim(0, 9.6); ax.grid(alpha=0.35)
    ax.set_title("Năng lượng liên kết riêng theo số khối", fontsize=11, fontweight="bold")
    fig.tight_layout()
    save(fig, "f19_nllk_rieng")


def fig_dinh_luat_phong_xa():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    t = np.linspace(0, 5, 500)
    ax.plot(t, 2.0 ** (-t), color=BLUE, lw=2.2)
    for k in range(1, 5):
        ax.plot([k, k], [0, 2.0 ** (-k)], color=GREY, ls="--", lw=0.9)
        ax.plot([0, k], [2.0 ** (-k)] * 2, color=GREY, ls="--", lw=0.9)
        ax.plot([k], [2.0 ** (-k)], "o", color=RED, ms=5)
        ax.text(k + 0.06, 2.0 ** (-k) + 0.025, r"$N_0/%d$" % (2 ** k), fontsize=8.6, color=RED)
    ax.set_xticks(range(0, 6))
    ax.set_xticklabels(["0", "T", "2T", "3T", "4T", "5T"])
    ax.set_yticks([0, 0.125, 0.25, 0.5, 1.0])
    ax.set_yticklabels(["0", r"$N_0/8$", r"$N_0/4$", r"$N_0/2$", r"$N_0$"])
    ax.set_xlabel("Thời gian t"); ax.set_ylabel("Số hạt nhân còn lại N")
    ax.grid(alpha=0.3)
    ax.set_title(r"Định luật phóng xạ:  $N = N_0 2^{-t/T} = N_0 e^{-\lambda t}$,  $\lambda = \dfrac{\ln 2}{T}$",
                 fontsize=11)
    fig.tight_layout()
    save(fig, "f20_dinh_luat_phong_xa")


def fig_dam_xuyen():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.add_patch(Rectangle((0.6, -1.15), 0.10, 2.3, fc="#f7dc6f", ec="k"))
    ax.text(0.65, 1.30, "tờ giấy", ha="center", fontsize=8.6)
    ax.add_patch(Rectangle((2.0, -1.15), 0.28, 2.3, fc="#aeb6bf", ec="k"))
    ax.text(2.14, 1.30, "nhôm\nvài mm", ha="center", fontsize=8.6)
    ax.add_patch(Rectangle((3.6, -1.15), 0.55, 2.3, fc="#5d6d7e", ec="k"))
    ax.text(3.88, 1.30, "chì\nvài cm", ha="center", fontsize=8.6)
    arrow(ax, -0.6, 0.62, 0.58, 0.62, color=RED, lw=2.2, ms=13)
    ax.text(-1.35, 0.55, r"$\alpha$", fontsize=14, color=RED)
    arrow(ax, -0.6, 0.0, 1.98, 0.0, color=GREEN, lw=2.0, ms=13)
    ax.text(-1.35, -0.07, r"$\beta$", fontsize=14, color=GREEN)
    arrow(ax, -0.6, -0.62, 4.55, -0.62, color=BLUE, lw=1.8, ms=13)
    ax.text(-1.35, -0.70, r"$\gamma$", fontsize=14, color=BLUE)
    ax.text(4.75, -0.62, "yếu đi", fontsize=8.4, color=BLUE, va="center")
    ax.text(1.9, -1.72, "Khả năng đâm xuyên tăng dần: α < β < γ", ha="center", fontsize=10)
    ax.text(1.9, -2.05, "Khả năng ion hoá môi trường giảm dần: α > β > γ", ha="center", fontsize=10)
    ax.text(1.9, 1.85, "Khả năng đâm xuyên của các tia phóng xạ", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -1.7, 5.6, -2.3, 2.1)
    save(fig, "f21_dam_xuyen")


def fig_phan_hach():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    def nuc(x, y, lab, c=ORANGE, r=0.20):
        ax.add_patch(Circle((x, y), r, fc=c, ec="k", lw=0.8))
        ax.text(x, y, lab, ha="center", va="center", fontsize=7.6, color="w", fontweight="bold")
    def neu(x, y):
        ax.add_patch(Circle((x, y), 0.075, fc=BLUE, ec="k", lw=0.6))
    neu(-2.35, 0); arrow(ax, -2.2, 0, -1.75, 0, color=BLUE, lw=1.2, ms=10)
    nuc(-1.45, 0, "U-235", ORANGE, 0.26)
    for dy, lab in ((0.62, "Ba"), (-0.62, "Kr")):
        arrow(ax, -1.15, dy * 0.25, -0.35, dy * 0.85, color=GREY, lw=1.0, ms=10)
        nuc(-0.05, dy * 0.95, lab, GREEN, 0.20)
    for dy in (0.30, 0.0, -0.30):
        neu(-0.72, dy * 1.6)
        arrow(ax, -0.62, dy * 1.6, 0.30, dy * 2.1, color=BLUE, lw=0.9, ms=9)
    for k, dy in enumerate((1.05, 0.0, -1.05)):
        nuc(0.95, dy, "U-235", ORANGE, 0.24)
        for s in (1, -1):
            arrow(ax, 1.20, dy + s * 0.10, 2.05, dy + s * 0.55, color=BLUE, lw=0.8, ms=8)
            nuc(2.35, dy + s * 0.62, "", GREEN, 0.13)
    clean(ax, -2.9, 3.1, -2.1, 1.9)
    ax.set_title("Phản ứng phân hạch dây chuyền", fontsize=11.5, fontweight="bold", pad=8)
    fig.text(0.5, 0.02, "Mỗi phân hạch giải phóng khoảng 200 MeV và 2–3 neutron mới",
             ha="center", fontsize=8.8)
    fig.text(0.5, -0.04, "Nếu hệ số nhân neutron k ≥ 1 thì phản ứng dây chuyền tự duy trì",
             ha="center", fontsize=8.8, style="italic")
    save(fig, "f22_phan_hach")


def fig_nhiet_hach():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    def part(x, y, lab, c, r=0.26):
        ax.add_patch(Circle((x, y), r, fc=c, ec="k", lw=0.9))
        ax.text(x, y, lab, ha="center", va="center", fontsize=8.4, color="w", fontweight="bold")
    part(-2.3, 0.45, "D", RED); part(-2.3, -0.45, "T", ORANGE)
    arrow(ax, -1.9, 0.30, -1.15, 0.05, color=GREY, lw=1.3, ms=11)
    arrow(ax, -1.9, -0.30, -1.15, -0.05, color=GREY, lw=1.3, ms=11)
    ax.text(-0.55, 0, "→", fontsize=22, ha="center", va="center")
    part(0.45, 0.42, "He-4", GREEN, 0.30)
    part(0.45, -0.48, "n", BLUE, 0.18)
    arrow(ax, 0.85, 0.42, 1.5, 0.62, color=GREY, lw=1.0, ms=10)
    arrow(ax, 0.70, -0.48, 1.5, -0.68, color=GREY, lw=1.0, ms=10)
    ax.text(2.35, 0, "17,6 MeV", fontsize=12, color=RED, fontweight="bold", ha="center")
    ax.text(0, -1.35, r"$^2_1\mathrm{H} + {}^3_1\mathrm{H} \rightarrow {}^4_2\mathrm{He} + {}^1_0\mathrm{n} + 17{,}6\ \mathrm{MeV}$",
            ha="center", fontsize=12)
    ax.text(0, -1.85, "Điều kiện: nhiệt độ cỡ trăm triệu độ để thắng lực đẩy Coulomb",
            ha="center", fontsize=8.8, style="italic")
    ax.text(0, 1.35, "Phản ứng tổng hợp hạt nhân (nhiệt hạch)", ha="center", fontsize=11, fontweight="bold")
    clean(ax, -3.0, 3.3, -2.2, 1.6)
    save(fig, "f23_nhiet_hach")


def fig_bien_bao():
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    ax.add_patch(Polygon([(0, 1.35), (1.25, -0.85), (-1.25, -0.85)], closed=True,
                         fc="#f1c40f", ec="k", lw=2.2))
    cx, cy = 0, -0.10
    for a in (90, 210, 330):
        ax.add_patch(Wedge((cx, cy), 0.62, a - 30, a + 30, width=0.44, fc="k"))
    ax.add_patch(Circle((cx, cy), 0.115, fc="k"))
    ax.text(0, -1.25, "Cảnh báo khu vực có phóng xạ", ha="center", fontsize=9.5, fontweight="bold")
    clean(ax, -1.5, 1.5, -1.6, 1.6)
    save(fig, "f24_bien_bao")


def fig_semilog():
    t = np.array([0, 1, 2, 3, 4, 5, 6])
    H = np.array([800, 566, 400, 283, 200, 141, 100], dtype=float)
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.4))
    axes[0].plot(t, H, "o-", color=BLUE, ms=5)
    axes[0].set_xlabel("t (giờ)"); axes[0].set_ylabel("H (Bq)")
    axes[0].grid(alpha=0.35); axes[0].set_title("Độ phóng xạ đo được theo thời gian", fontsize=10)
    axes[1].plot(t, np.log(H), "o", color=RED, ms=5)
    c = np.polyfit(t, np.log(H), 1)
    tt = np.linspace(-0.2, 6.2, 50)
    axes[1].plot(tt, np.polyval(c, tt), "-", color=RED, lw=1.4)
    axes[1].set_xlabel("t (giờ)"); axes[1].set_ylabel(r"$\ln H$")
    axes[1].grid(alpha=0.35)
    axes[1].set_title(r"$\ln H = \ln H_0 - \lambda t$  → hệ số góc $= -\lambda$", fontsize=10)
    axes[1].text(0.35, 5.35, "hệ số góc ≈ %.3f giờ$^{-1}$" % c[0], fontsize=8.8, color=RED)
    fig.tight_layout()
    save(fig, "f25_semilog")


def fig_so_do_NZ():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.set_xlabel("Số neutron N"); ax.set_ylabel("Số proton Z")
    ax.grid(alpha=0.35)
    ax.plot([6], [5], "o", color="k", ms=11)
    ax.text(6.12, 5.12, "hạt nhân mẹ", fontsize=9)
    tips = [((4, 3), r"phân rã $\alpha$" + "\n(Z−2, N−2)", RED),
            ((5, 6), r"phân rã $\beta^-$" + "\n(Z+1, N−1)", GREEN),
            ((7, 4), r"phân rã $\beta^+$" + "\n(Z−1, N+1)", BLUE)]
    for (n, z), lab, c in tips:
        arrow(ax, 6, 5, n, z, color=c, lw=1.8, ms=14)
        ax.plot([n], [z], "s", color=c, ms=8)
        ax.text(n + (0.15 if n >= 6 else -0.15), z + (0.25 if z > 5 else -0.55), lab,
                fontsize=8.6, color=c, ha="left" if n >= 6 else "right")
    ax.set_xlim(3, 8.6); ax.set_ylim(2.2, 7.2)
    ax.set_xticks(range(3, 9)); ax.set_yticks(range(3, 8))
    ax.set_title("Sự dịch chuyển của hạt nhân trên giản đồ (N, Z) khi phân rã",
                 fontsize=10.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "f26_so_do_NZ")


if __name__ == "__main__":
    print("Đang vẽ hình...")
    for f in [fig_nam_cham_thang, fig_dong_dien_thang, fig_ong_day, fig_luc_tu, fig_goc_theta,
              fig_can_dong_dien, fig_tu_thong, fig_thi_nghiem_faraday, fig_lenz, fig_may_phat,
              fig_phi_e, fig_hieu_dung, fig_bien_ap, fig_song_dien_tu, fig_phi_gap_khuc,
              fig_thanh_truot, fig_cau_tao_hat_nhan, fig_rutherford, fig_nllk_rieng,
              fig_dinh_luat_phong_xa, fig_dam_xuyen, fig_phan_hach, fig_nhiet_hach,
              fig_bien_bao, fig_semilog, fig_so_do_NZ]:
        f()
    print("Xong:", len(os.listdir(OUT)), "hình trong", OUT)
