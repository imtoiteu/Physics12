# -*- coding: utf-8 -*-
"""Hình vẽ cho CHƯƠNG 2 VẬT LÍ 12 – KHÍ LÍ TƯỞNG (và dùng lại cho đề tổng hợp)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Ellipse, Arc, FancyBboxPatch

from figbase import (save, arrow, clean, frame, hatch_ground,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)
from figgen import curve, points, flame, thermometer, piston_cylinder, _reg, MADE


# =============================================================== ĐỒ THỊ
def k_dt_dangnhiet():
    V = np.linspace(0.7, 6.2, 120)
    return curve("k_dt_dangnhiet",
                 [dict(x=V, y=4.0 / V, c=BLUE), dict(x=V, y=8.0 / V, c=RED)],
                 "V (L)", "p (10⁵ Pa)", (0, 6.8), (0, 6.5),
                 xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[0, 1, 2, 3, 4, 5, 6],
                 texts=[(5.0, 1.05, "T₁", BLUE, 12, "center", 1),
                        (5.0, 1.95, "T₂", RED, 12, "center", 1)],
                 size=(5.6, 3.9))


def k_dt_dangtich():
    T = np.linspace(0, 500, 40)
    return curve("k_dt_dangtich",
                 [dict(x=T, y=0.0080 * T, c=RED), dict(x=T, y=0.0045 * T, c=BLUE)],
                 "T (K)", "p (10⁵ Pa)", (0, 540), (0, 4.4),
                 xticks=[0, 100, 200, 300, 400, 500], yticks=[0, 1, 2, 3, 4],
                 texts=[(460, 3.85, "(1)", RED, 11, "center", 1),
                        (475, 2.35, "(2)", BLUE, 11, "center", 1)],
                 size=(5.6, 3.8))


def k_dt_dangap():
    T = np.linspace(0, 500, 40)
    return curve("k_dt_dangap",
                 [dict(x=T, y=0.020 * T, c=GREEN), dict(x=T, y=0.012 * T, c=PURPLE)],
                 "T (K)", "V (L)", (0, 540), (0, 11.0),
                 xticks=[0, 100, 200, 300, 400, 500], yticks=[0, 2, 4, 6, 8, 10],
                 texts=[(455, 9.6, "p₁", GREEN, 11, "center", 1),
                        (472, 5.9, "p₂", PURPLE, 11, "center", 1)],
                 size=(5.6, 3.8))


def k_dt_chutrinh():
    return curve("k_dt_chutrinh",
                 [dict(x=[1, 1, 3, 3, 1], y=[1, 3, 3, 1, 1], c=BLUE, fill=True, dots=True)],
                 "V (L)", "p (10⁵ Pa)", (0, 4.2), (0, 4.0),
                 xticks=[0, 1, 2, 3, 4], yticks=[0, 1, 2, 3, 4],
                 texts=[(0.72, 1.0, "(1)", RED, 11, "center", 1),
                        (0.72, 3.0, "(2)", RED, 11, "center", 1),
                        (3.22, 3.0, "(3)", RED, 11, "left", 1),
                        (3.22, 1.0, "(4)", RED, 11, "left", 1)],
                 size=(5.2, 3.8))


def k_dt_baquatrinh():
    V = np.linspace(1.0, 4.4, 80)
    return curve("k_dt_baquatrinh",
                 [dict(x=V, y=2.0 / V, c=BLUE, label="đẳng nhiệt"),
                  dict(x=[2, 2], y=[1.0, 2.6], c=RED, label="đẳng tích"),
                  dict(x=[2, 4], y=[1.0, 1.0], c=GREEN, label="đẳng áp")],
                 "V (L)", "p (10⁵ Pa)", (0, 4.8), (0, 3.0),
                 xticks=[0, 1, 2, 3, 4], yticks=[0, 1, 2, 3],
                 texts=[(2.05, 2.72, "(a)", RED, 11, "center", 1),
                        (3.55, 0.72, "(b)", GREEN, 11, "center", 1),
                        (3.75, 0.62, "", GREEN, 9, "center"),
                        (3.30, 0.80, "(c)", BLUE, 11, "center", 1),
                        (1.75, 1.05, "M", "#333333", 11, "right", 1)],
                 size=(5.6, 3.8))


def k_dt_boyle_1V():
    Vv = np.array([10.0, 12.0, 15.0, 20.0, 30.0])
    p = 60.0 / Vv
    x = np.linspace(0, 0.115, 20)
    return curve("k_dt_boyle_1V",
                 [dict(x=x, y=60.0 * x, c=BLUE, lw=1.7), points(1 / Vv, p, c=RED)],
                 "1/V (cm⁻³)", "p (10⁵ Pa)", (0, 0.122), (0, 7.6),
                 xticks=[0, 0.02, 0.04, 0.06, 0.08, 0.10], yticks=[0, 2, 4, 6],
                 size=(5.6, 3.8))


def k_dt_charles():
    t = np.array([0.0, 20.0, 40.0, 60.0, 80.0])
    V = 20.0 * (1 + t / 273.0)
    td = np.linspace(-273, 0, 20)
    return curve("k_dt_charles",
                 [dict(x=td, y=20.0 * (1 + td / 273.0), c=BLUE, ls="--", lw=1.6),
                  dict(x=np.linspace(0, 90, 20), y=20.0 * (1 + np.linspace(0, 90, 20) / 273.0),
                       c=BLUE, lw=2.2),
                  points(t, V, c=RED)],
                 "t (°C)", "V (cm³)", (-300, 105), (-1.5, 30),
                 xticks=[-273, -200, -100, 0, 100],
                 xticklabels=["−273", "−200", "−100", "0", "100"],
                 yticks=[0, 10, 20, 30], axhline=True,
                 annots=[("kéo dài cắt trục hoành tại −273 °C", (-273, 0), (-115, 14.5), GREEN)],
                 size=(6.2, 3.8))


def k_dt_pV_docso():
    return curve("k_dt_pV_docso",
                 [dict(x=[1, 4, 4], y=[4, 1, 3], c=BLUE, dots=True)],
                 "V (L)", "p (10⁵ Pa)", (0, 5.2), (0, 5.0),
                 xticks=[0, 1, 2, 3, 4, 5], yticks=[0, 1, 2, 3, 4, 5],
                 texts=[(0.72, 4.0, "A", RED, 11, "center", 1),
                        (4.22, 1.0, "B", RED, 11, "left", 1),
                        (4.22, 3.0, "C", RED, 11, "left", 1)],
                 size=(5.2, 3.8))


# =============================================================== SƠ ĐỒ
def k_sd_mohinh():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    clean(ax, -0.6, 9.0, -1.4, 7.4)
    ax.add_patch(Rectangle((0.4, 0.4), 7.4, 6.0, fc="#f7fafd", ec="#333333", lw=2.6))
    rng = np.random.default_rng(5)
    xs = rng.uniform(0.9, 7.3, 14); ys = rng.uniform(0.9, 5.9, 14)
    for x, y in zip(xs, ys):
        ax.plot([x], [y], "o", ms=7, color=BLUE)
        a = rng.uniform(0, 2 * np.pi)
        arrow(ax, x, y, x + 0.75 * np.cos(a), y + 0.75 * np.sin(a), color=BLUE,
              lw=1.0, ms=8)
    # một phân tử va vào thành phải
    ax.plot([6.4], [3.2], "o", ms=8, color=RED)
    arrow(ax, 6.4, 3.2, 7.7, 3.7, color=RED, lw=1.6)
    arrow(ax, 7.7, 2.7, 6.4, 2.2, color=RED, lw=1.6)
    ax.text(8.15, 3.2, "va chạm\nvào thành", fontsize=8.4, color=RED, ha="left",
            va="center")
    ax.text(4.1, -0.9, "Áp suất khí = kết quả va chạm của vô số phân tử lên thành bình",
            fontsize=8.8, color=GREY, ha="center")
    save(fig, "k_sd_mohinh"); return _reg("k_sd_mohinh")


def k_sd_tn_boyle():
    fig, ax = plt.subplots(figsize=(6.0, 2.9))
    clean(ax, -0.4, 14.0, -1.6, 5.0)
    ax.add_patch(Rectangle((1.6, 1.4), 5.4, 1.8, fc="#d8e8f8", ec=GREY, lw=1.8))
    ax.text(4.0, 2.3, "khí bị nhốt", fontsize=9.2, color=BLUE, ha="center", va="center")
    ax.add_patch(Rectangle((7.0, 1.25), 0.45, 2.1, fc="#9aa5b1", ec="#5a6470", lw=1.0))
    ax.plot([7.45, 10.0], [2.3, 2.3], color="#5a6470", lw=3.0)
    ax.add_patch(Rectangle((10.0, 1.75), 0.55, 1.1, fc="#5a6470", ec="none"))
    ax.text(7.2, 3.75, "pit-tông", fontsize=8.6, color="#3d4650", ha="center")
    arrow(ax, 10.9, 2.3, 12.5, 2.3, color=RED, lw=1.9)
    ax.text(11.7, 2.85, "ép", fontsize=9, color=RED, ha="center")
    for k in range(11):
        x = 1.6 + k * 0.5
        ax.plot([x, x], [1.4, 1.1], color=GREY, lw=1.0)
    ax.text(4.3, 0.62, "thang chia thể tích", fontsize=8.4, color=GREY, ha="center")
    ax.plot([1.15, 1.15], [1.55, 0.35], color=GREY, lw=1.5)
    ax.add_patch(Circle((1.15, -0.1), 0.45, fc="white", ec=GREY, lw=1.6))
    ax.plot([1.15, 1.38], [-0.1, 0.15], color=RED, lw=1.4)
    ax.text(1.8, -0.1, "áp kế đo p", fontsize=8.8, color=GREY, ha="left", va="center")
    ax.text(6.5, 4.4, "Thí nghiệm khảo sát định luật Boyle (nhiệt độ không đổi)",
            fontsize=9.2, color="#333333", ha="center")
    save(fig, "k_sd_tn_boyle"); return _reg("k_sd_tn_boyle")


def k_sd_tn_charles():
    fig, ax = plt.subplots(figsize=(4.4, 4.0))
    clean(ax, -1.2, 9.2, -1.2, 10.0)
    # cốc nước
    ax.add_patch(Rectangle((0.6, 0.4), 6.4, 6.4, fc="white", ec="#333333", lw=2.2))
    ax.add_patch(Rectangle((0.6, 0.4), 6.4, 5.4, fc="#d8e8f8", ec="none"))
    ax.text(1.9, 1.3, "nước", fontsize=9, color=BLUE, ha="center")
    # ống nghiệm chứa cột khí
    ax.add_patch(Rectangle((3.4, 1.2), 1.0, 8.0, fc="white", ec="#444444", lw=1.8))
    ax.add_patch(Rectangle((3.4, 1.2), 1.0, 4.2, fc="#eaf2fb", ec="none"))
    ax.add_patch(Rectangle((3.4, 5.4), 1.0, 0.5, fc="#8e9aa6", ec="#5a6470", lw=0.8))
    ax.text(3.9, 3.2, "cột\nkhí", fontsize=8.8, color=BLUE, ha="center", va="center")
    ax.text(4.75, 5.65, "giọt thuỷ ngân", fontsize=8.2, color="#3d4650", ha="left",
            va="center")
    ax.annotate("", xy=(2.95, 5.4), xytext=(2.95, 1.2),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(2.72, 3.3, "ℓ", fontsize=11, color=GREEN, ha="right", va="center")
    thermometer(ax, 6.2, 9.0, 2.0, label="nhiệt kế")
    flame(ax, 2.2, 5.4, -1.0, n=5)
    ax.text(3.8, -1.05, "đun nóng từ từ", fontsize=8.8, color=ORANGE, ha="center",
            va="top")
    save(fig, "k_sd_tn_charles"); return _reg("k_sd_tn_charles")


def k_sd_xilanh_quanang():
    fig, ax = plt.subplots(figsize=(3.4, 4.4))
    clean(ax, -1.8, 5.0, -1.6, 10.0)
    top = piston_cylinder(ax, 0.0, 0.0, 3.0, 4.0, 7.6, label="khí")
    ax.add_patch(Rectangle((0.6, top + 0.1), 1.8, 0.9, fc="#5a6470", ec="none"))
    ax.text(1.5, top + 0.55, "m", fontsize=10, color="white", ha="center", va="center")
    ax.text(3.35, top - 0.2, "pit-tông", fontsize=8.6, color="#3d4650", ha="left")
    ax.annotate("", xy=(-0.6, 4.0), xytext=(-0.6, 0.0),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.3))
    ax.text(-0.85, 2.0, "h", fontsize=11, color=BLUE, ha="right", va="center")
    flame(ax, 0.4, 2.6, -1.3, n=4)
    ax.text(1.5, 9.3, "quả nặng đặt trên pit-tông", fontsize=8.6, color=GREY,
            ha="center")
    save(fig, "k_sd_xilanh_quanang"); return _reg("k_sd_xilanh_quanang")


def k_sd_bomxe():
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    clean(ax, -0.6, 13.4, -1.6, 5.4)
    ax.add_patch(Circle((3.0, 2.0), 2.3, fc="none", ec="#333333", lw=3.0))
    ax.add_patch(Circle((3.0, 2.0), 1.7, fc="none", ec=GREY, lw=1.4))
    ax.text(3.0, 2.0, "lốp xe\nV không đổi", fontsize=8.8, color="#333333",
            ha="center", va="center")
    ax.plot([5.1, 6.2], [2.6, 2.6], color=GREY, lw=2.2)
    ax.add_patch(Circle((5.65, 3.1), 0.26, fc="white", ec=RED, lw=1.3))
    ax.text(5.65, 3.65, "van", fontsize=8.2, color=RED, ha="center")
    ax.add_patch(Rectangle((6.2, 1.7), 3.6, 1.8, fc="#eef4fb", ec=GREY, lw=1.8))
    ax.text(7.1, 2.6, "V₀", fontsize=9.5, color=GREY, ha="center", va="center")
    ax.add_patch(Rectangle((8.4, 1.65), 0.38, 1.9, fc="#9aa5b1", ec="#5a6470", lw=1.0))
    ax.plot([8.78, 11.2], [2.6, 2.6], color="#5a6470", lw=3.0)
    ax.add_patch(Rectangle((11.2, 2.15), 0.5, 0.9, fc="#5a6470", ec="none"))
    arrow(ax, 10.2, 4.2, 8.6, 4.2, color=RED, lw=1.8)
    ax.text(9.4, 4.65, "đẩy", fontsize=9, color=RED, ha="center")
    ax.text(8.0, 0.85, "xilanh của bơm", fontsize=8.6, color=GREY, ha="center")
    save(fig, "k_sd_bomxe"); return _reg("k_sd_bomxe")


def k_sd_binhkhi():
    fig, ax = plt.subplots(figsize=(3.2, 3.8))
    clean(ax, -2.4, 5.6, -1.0, 9.2)
    ax.add_patch(FancyBboxPatch((0.3, 0.4), 3.0, 6.2, boxstyle="round,pad=0.18",
                                fc="#eaf2fb", ec="#333333", lw=2.4))
    ax.add_patch(Rectangle((1.35, 6.6), 0.9, 1.0, fc="#5a6470", ec="none"))
    ax.add_patch(Circle((1.8, 8.0), 0.55, fc="white", ec=RED, lw=1.8))
    ax.text(1.8, 8.0, "van", fontsize=7.6, color=RED, ha="center", va="center")
    ax.text(1.8, 3.4, "khí nén\nV không đổi", fontsize=9.2, color=BLUE, ha="center",
            va="center")
    ax.annotate("van an toàn mở khi p vượt\nngưỡng cho phép", xy=(2.35, 8.0),
                xytext=(4.9, 6.4), fontsize=8.2, color=RED, ha="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    flame(ax, 0.5, 3.0, -0.9, n=4)
    save(fig, "k_sd_binhkhi"); return _reg("k_sd_binhkhi")


def k_sd_ong_khi():
    """Ống nghiệm nằm ngang và thẳng đứng, cột khí bị giam bởi giọt thuỷ ngân."""
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    clean(ax, -1.0, 15.0, -2.2, 6.6)
    # nằm ngang
    ax.add_patch(Rectangle((0.4, 2.0), 6.0, 1.0, fc="white", ec="#444444", lw=1.8))
    ax.add_patch(Rectangle((0.4, 2.0), 3.6, 1.0, fc="#dbe9f8", ec="none"))
    ax.add_patch(Rectangle((4.0, 2.0), 0.7, 1.0, fc="#8e9aa6", ec="#5a6470", lw=0.8))
    ax.text(2.2, 3.55, "cột khí", fontsize=8.8, color=BLUE, ha="center")
    ax.text(4.35, 1.45, "Hg", fontsize=8.8, color="#3d4650", ha="center")
    ax.text(0.15, 2.5, "kín", fontsize=8.2, color=GREY, ha="right", va="center")
    ax.text(6.65, 2.5, "hở", fontsize=8.2, color=GREY, ha="left", va="center")
    ax.text(3.4, -1.4, "(a) ống nằm ngang", fontsize=9.4, color=RED, ha="center",
            fontweight="bold")
    # thẳng đứng miệng lên
    ax.add_patch(Rectangle((10.4, -0.6), 1.0, 6.0, fc="white", ec="#444444", lw=1.8))
    ax.add_patch(Rectangle((10.4, -0.6), 1.0, 3.2, fc="#dbe9f8", ec="none"))
    ax.add_patch(Rectangle((10.4, 2.6), 1.0, 0.7, fc="#8e9aa6", ec="#5a6470", lw=0.8))
    ax.text(9.95, 1.0, "cột khí", fontsize=8.8, color=BLUE, ha="right", va="center")
    ax.text(11.75, 2.95, "Hg", fontsize=8.8, color="#3d4650", ha="left", va="center")
    ax.text(10.9, 5.75, "hở", fontsize=8.2, color=GREY, ha="center")
    ax.text(10.9, -1.05, "kín", fontsize=8.2, color=GREY, ha="center", va="top")
    ax.text(10.9, -1.9, "(b) ống thẳng đứng, miệng ở trên", fontsize=9.4, color=RED,
            ha="center", fontweight="bold")
    save(fig, "k_sd_ong_khi"); return _reg("k_sd_ong_khi")


def k_sd_bongbay():
    fig, ax = plt.subplots(figsize=(4.4, 3.4))
    clean(ax, -1.0, 10.6, -1.4, 8.4)
    ax.add_patch(Ellipse((2.4, 5.2), 3.4, 4.0, fc="#fdece0", ec=ORANGE, lw=2.0))
    ax.plot([2.4, 2.4], [3.2, 0.6], color=GREY, lw=1.2)
    ax.text(2.4, 5.4, "bóng thám không\n(mặt đất)", fontsize=8.4, color=ORANGE,
            ha="center", va="center")
    ax.add_patch(Ellipse((7.8, 5.2), 4.6, 5.4, fc="#fdece0", ec=RED, lw=2.0))
    ax.plot([7.8, 7.8], [2.5, 0.6], color=GREY, lw=1.2)
    ax.text(7.8, 5.4, "ở độ cao lớn:\np giảm, T giảm", fontsize=8.4, color=RED,
            ha="center", va="center")
    arrow(ax, 4.4, 5.2, 5.3, 5.2, color="#333333", lw=1.7)
    ax.text(5.3, -1.0, "Thể tích bóng thay đổi theo áp suất và nhiệt độ khí quyển",
            fontsize=8.8, color=GREY, ha="center")
    save(fig, "k_sd_bongbay"); return _reg("k_sd_bongbay")


ALL = [k_dt_dangnhiet, k_dt_dangtich, k_dt_dangap, k_dt_chutrinh, k_dt_baquatrinh,
       k_dt_boyle_1V, k_dt_charles, k_dt_pV_docso, k_sd_mohinh, k_sd_tn_boyle,
       k_sd_tn_charles, k_sd_xilanh_quanang, k_sd_bomxe, k_sd_binhkhi, k_sd_ong_khi,
       k_sd_bongbay]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())


def k_dt_chutrinh_tg():
    """Chu trình tam giác A(1 L; 1·10⁵) → B(1 L; 3·10⁵) → C(3 L; 1·10⁵) → A."""
    return curve("k_dt_chutrinh_tg",
                 [dict(x=[1, 1, 3, 1], y=[1, 3, 1, 1], c=PURPLE, fill=True, dots=True)],
                 "V (L)", "p (10⁵ Pa)", (0, 4.2), (0, 4.0),
                 xticks=[0, 1, 2, 3, 4], yticks=[0, 1, 2, 3, 4],
                 texts=[(0.72, 1.0, "A", RED, 11, "center", 1),
                        (0.72, 3.0, "B", RED, 11, "center", 1),
                        (3.18, 1.0, "C", RED, 11, "left", 1)],
                 size=(5.2, 3.8))


ALL.append(k_dt_chutrinh_tg)


def k_dt_chutrinh_dn():
    """Chu trình có một chặng đẳng nhiệt: A(1;4) → B(4;1) đẳng nhiệt, B → C(1;1) đẳng áp, C → A đẳng tích."""
    V = np.linspace(1.0, 4.0, 80)
    return curve("k_dt_chutrinh_dn",
                 [dict(x=V, y=4.0 / V, c=RED),
                  dict(x=[4, 1], y=[1, 1], c=GREEN),
                  dict(x=[1, 1], y=[1, 4], c=BLUE)],
                 "V (L)", "p (10⁵ Pa)", (0, 5.0), (0, 5.0),
                 xticks=[0, 1, 2, 3, 4, 5], yticks=[0, 1, 2, 3, 4, 5],
                 texts=[(0.72, 4.0, "A", "#333333", 11, "center", 1),
                        (4.15, 1.05, "B", "#333333", 11, "left", 1),
                        (0.72, 1.0, "C", "#333333", 11, "center", 1),
                        (2.55, 1.95, "đẳng nhiệt", RED, 9, "center"),
                        (2.30, 0.62, "đẳng áp", GREEN, 9, "center"),
                        (1.12, 2.60, "đẳng tích", BLUE, 9, "left")],
                 size=(5.4, 3.9))


ALL.append(k_dt_chutrinh_dn)


def k_dt_chutrinh_xien():
    """Chu trình A(1;1) →(đoạn thẳng)→ B(3;3) →(đẳng tích)→ C(3;1) →(đẳng áp)→ A."""
    return curve("k_dt_chutrinh_xien",
                 [dict(x=[1, 3, 3, 1], y=[1, 3, 1, 1], c=TEAL, fill=True, dots=True)],
                 "V (L)", "p (10⁵ Pa)", (0, 4.4), (0, 4.2),
                 xticks=[0, 1, 2, 3, 4], yticks=[0, 1, 2, 3, 4],
                 texts=[(0.72, 1.0, "A", RED, 11, "center", 1),
                        (3.18, 3.0, "B", RED, 11, "left", 1),
                        (3.18, 1.0, "C", RED, 11, "left", 1)],
                 size=(5.2, 3.8))


ALL.append(k_dt_chutrinh_xien)
