# -*- coding: utf-8 -*-
"""Hình vẽ cho CHƯƠNG 1 VẬT LÍ 12 – VẬT LÍ NHIỆT (và dùng lại cho đề tổng hợp)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Ellipse, Arc, FancyBboxPatch

from figbase import (save, arrow, clean, frame, hatch_ground,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)
from figgen import curve, points, flame, thermometer, _reg, MADE


# =============================================================== ĐỒ THỊ NUNG NÓNG
def n_dt_nuocda():
    """0,5 kg nước đá −20 °C, P = 420 W:  t = 50 / 450 / 950 s."""
    return curve("n_dt_nuocda",
          [dict(x=[0, 50, 450, 950], y=[-20, 0, 0, 100], c=RED, dots=True)],
          "t (s)", "T (°C)", (0, 1030), (-35, 120),
          xticks=[0, 50, 450, 950], yticks=[-20, 0, 50, 100],
          texts=[(230, 8, "nước đá đang nóng chảy", GREEN, 9.2, "center"),
                 (700, 42, "nước nóng lên", GREY, 9.2, "center")],
          size=(6.6, 3.8))


def n_dt_chi():
    """1 kg chì từ 27 °C, P = 100 W: nóng chảy ở 327 °C."""
    return curve("n_dt_chi",
          [dict(x=[0, 390, 640, 740], y=[27, 327, 327, 400], c=ORANGE, dots=True)],
          "t (s)", "T (°C)", (0, 810), (0, 460),
          xticks=[0, 390, 640, 740], yticks=[27, 100, 200, 327, 400],
          texts=[(515, 300, "chì đang nóng chảy", GREEN, 9.2, "center")],
          size=(6.4, 3.8))


def n_dt_dongdac():
    """Chất lỏng để nguội, đông đặc ở 80 °C."""
    return curve("n_dt_dongdac",
          [dict(x=[0, 120, 360, 540], y=[90, 80, 80, 60], c=BLUE, dots=True)],
          "t (phút)", "T (°C)", (0, 590), (50, 100),
          xticks=[0, 120, 360, 540], yticks=[60, 70, 80, 90],
          texts=[(240, 83.5, "đang đông đặc", GREEN, 9.2, "center")],
          size=(6.2, 3.6))


def n_dt_QdT():
    """Q theo ΔT của hai chất lỏng cùng khối lượng 0,5 kg."""
    dT = np.array([0, 10, 20, 30, 40, 50])
    return curve("n_dt_QdT",
          [dict(x=dT, y=2.1 * dT, c=RED, label="chất X"),
           dict(x=dT, y=1.2 * dT, c=BLUE, label="chất Y")],
          "ΔT (K)", "Q (kJ)", (0, 55), (0, 118),
          xticks=[0, 10, 20, 30, 40, 50], yticks=[0, 20, 40, 60, 80, 100],
          texts=[(44, 98, "X", RED, 12, "center", 1), (46, 60, "Y", BLUE, 12, "center", 1)],
          size=(5.8, 3.8))


def n_dt_batchat():
    """Ba mẫu chất cùng khối lượng, cùng máy đun: T theo t."""
    t = np.array([0, 100, 200, 300, 400])
    return curve("n_dt_batchat",
          [dict(x=t, y=25 + 0.30 * t, c=RED, label="(1)"),
           dict(x=t, y=25 + 0.15 * t, c=BLUE, label="(2)"),
           dict(x=t, y=25 + 0.10 * t, c=GREEN, label="(3)")],
          "t (s)", "T (°C)", (0, 440), (0, 160),
          xticks=[0, 100, 200, 300, 400], yticks=[25, 50, 100, 150],
          texts=[(405, 148, "(1)", RED, 11, "center", 1),
                 (405, 88, "(2)", BLUE, 11, "center", 1),
                 (405, 68, "(3)", GREEN, 11, "center", 1)],
          size=(6.0, 3.8))


def n_dt_tn_dunnuoc():
    """Số liệu thực nghiệm đun 0,20 kg nước bằng điện trở 42 W (hệ số góc 0,05 K/s)."""
    t = np.array([0, 60, 120, 180, 240, 300])
    T = np.array([24.0, 27.1, 29.9, 33.2, 35.9, 39.0])
    tt = np.linspace(0, 320, 20)
    return curve("n_dt_tn_dunnuoc",
          [dict(x=tt, y=24 + 0.05 * tt, c=BLUE, lw=1.6),
           points(t, T, c=RED)],
          "t (s)", "T (°C)", (0, 330), (20, 46),
          xticks=[0, 60, 120, 180, 240, 300], yticks=[24, 28, 32, 36, 40],
          texts=[(150, 43.5, "đường thẳng khớp số liệu thực nghiệm", BLUE, 9, "center")],
          size=(6.0, 3.7))


def n_dt_hainhietke():
    """Đối chiếu hai thang đo: số chỉ nhiệt kế X theo nhiệt độ Celsius."""
    tc = np.array([0, 20, 40, 60, 80, 100])
    return curve("n_dt_hainhietke",
          [dict(x=tc, y=-10 + 1.5 * tc, c=PURPLE, dots=True)],
          "t (°C)", "Số chỉ nhiệt kế X (°X)", (0, 110), (-25, 155),
          xticks=[0, 20, 40, 60, 80, 100], yticks=[-10, 0, 50, 100, 140],
          axhline=True, size=(5.8, 3.7))


# =============================================================== SƠ ĐỒ
def n_sd_cautruc():
    fig, ax = plt.subplots(figsize=(7.0, 2.7))
    clean(ax, -0.5, 16.5, -1.6, 4.4)
    rng = np.random.default_rng(11)
    # rắn: mạng đều
    for i in range(4):
        for j in range(4):
            ax.plot([0.7 + i * 0.85], [0.5 + j * 0.85], "o", ms=9, color=BLUE)
    ax.add_patch(Rectangle((0.2, 0.0), 4.0, 4.0, fc="none", ec=GREY, lw=1.5))
    ax.text(2.2, -0.75, "THỂ RẮN", fontsize=10, color=BLUE, ha="center", fontweight="bold")
    ax.text(2.2, -1.35, "trật tự xa, dao động\nquanh vị trí cố định", fontsize=8,
            color=GREY, ha="center", va="top")
    # lỏng: sát nhau nhưng lộn xộn
    xs = rng.uniform(6.1, 9.5, 15); ys = rng.uniform(0.4, 3.6, 15)
    ax.plot(xs, ys, "o", ms=9, color=GREEN)
    ax.add_patch(Rectangle((5.8, 0.0), 4.0, 4.0, fc="none", ec=GREY, lw=1.5))
    ax.text(7.8, -0.75, "THỂ LỎNG", fontsize=10, color=GREEN, ha="center", fontweight="bold")
    ax.text(7.8, -1.35, "trật tự gần, các hạt\ntrượt lên nhau", fontsize=8,
            color=GREY, ha="center", va="top")
    # khí: thưa
    xs = rng.uniform(11.7, 15.1, 7); ys = rng.uniform(0.4, 3.6, 7)
    ax.plot(xs, ys, "o", ms=9, color=RED)
    for x, y in zip(xs, ys):
        a = rng.uniform(0, 2 * np.pi)
        arrow(ax, x, y, x + 0.6 * np.cos(a), y + 0.6 * np.sin(a), color=RED, lw=1.0, ms=8)
    ax.add_patch(Rectangle((11.4, 0.0), 4.0, 4.0, fc="none", ec=GREY, lw=1.5))
    ax.text(13.4, -0.75, "THỂ KHÍ", fontsize=10, color=RED, ha="center", fontweight="bold")
    ax.text(13.4, -1.35, "hỗn loạn, khoảng cách\nrất lớn so với kích thước hạt", fontsize=8,
            color=GREY, ha="center", va="top")
    save(fig, "n_sd_cautruc"); return _reg("n_sd_cautruc")


def n_sd_chuyenthe():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    clean(ax, -0.6, 15.0, -2.4, 4.2)
    boxes = [(0.4, "RẮN", BLUE), (6.0, "LỎNG", GREEN), (11.6, "KHÍ", RED)]
    for x, lab, c in boxes:
        ax.add_patch(FancyBboxPatch((x, 1.1), 3.0, 1.5, boxstyle="round,pad=0.1",
                                    fc="white", ec=c, lw=2.0))
        ax.text(x + 1.5, 1.85, lab, fontsize=12, color=c, ha="center", va="center",
                fontweight="bold")
    for x1, x2, up, dn in [(3.5, 5.9, "nóng chảy", "đông đặc"),
                           (9.1, 11.5, "hoá hơi", "ngưng tụ")]:
        arrow(ax, x1, 2.35, x2, 2.35, color=ORANGE, lw=1.8)
        ax.text((x1 + x2) / 2, 2.75, up, fontsize=9.2, color=ORANGE, ha="center")
        arrow(ax, x2, 1.35, x1, 1.35, color=TEAL, lw=1.8)
        ax.text((x1 + x2) / 2, 0.72, dn, fontsize=9.2, color=TEAL, ha="center")
    # thăng hoa / ngưng kết
    ax.annotate("", xy=(13.1, 0.9), xytext=(1.9, 0.9),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.6,
                                connectionstyle="arc3,rad=0.28"))
    ax.text(7.5, -1.35, "thăng hoa (rắn → khí)  •  ngưng kết (khí → rắn)",
            fontsize=9.2, color=PURPLE, ha="center")
    ax.text(7.5, 3.75, "Chiều nhận nhiệt: →   •   Chiều toả nhiệt: ←", fontsize=9,
            color=GREY, ha="center")
    save(fig, "n_sd_chuyenthe"); return _reg("n_sd_chuyenthe")


def n_sd_nhietluongke():
    fig, ax = plt.subplots(figsize=(4.2, 3.6))
    clean(ax, -0.8, 7.2, -1.0, 6.6)
    ax.add_patch(Rectangle((0.3, 0.3), 5.6, 4.7, fc="#f2f4f6", ec="#333333", lw=2.4))
    ax.add_patch(Rectangle((0.95, 0.8), 4.3, 3.7, fc="white", ec=GREY, lw=1.6))
    ax.add_patch(Rectangle((0.95, 0.8), 4.3, 2.5, fc="#d8e8f8", ec="none"))
    ax.text(3.1, 2.0, "nước", fontsize=10.5, color=BLUE, ha="center", va="center")
    ax.text(0.42, 4.68, "vỏ cách nhiệt", fontsize=8, color="#333333", ha="left", va="center")
    thermometer(ax, 4.6, 6.0, 1.5, label="nhiệt kế")
    ax.plot([1.8, 1.8], [5.9, 1.3], color="#5a6470", lw=1.8)
    ax.plot([1.45, 2.15], [1.3, 1.3], color="#5a6470", lw=1.8)
    ax.text(1.2, 5.9, "que khuấy", fontsize=8.5, color="#5a6470", ha="left", va="top")
    save(fig, "n_sd_nhietluongke"); return _reg("n_sd_nhietluongke")


def n_sd_dun_dien():
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    clean(ax, -0.8, 11.6, -1.2, 7.0)
    ax.add_patch(Rectangle((0.6, 0.4), 5.6, 4.4, fc="#f2f4f6", ec="#333333", lw=2.2))
    ax.add_patch(Rectangle((1.15, 0.85), 4.5, 3.2, fc="#d8e8f8", ec=GREY, lw=1.4))
    ax.text(3.4, 1.9, "nước  m, c", fontsize=10, color=BLUE, ha="center", va="center")
    # điện trở nung
    zx = np.linspace(2.0, 4.8, 60)
    ax.plot(zx, 3.2 + 0.22 * np.sin(np.linspace(0, 8 * np.pi, 60)), color=RED, lw=2.2)
    ax.plot([2.0, 2.0], [3.2, 5.9], color=RED, lw=1.6)
    ax.plot([4.8, 4.8], [3.2, 5.9], color=RED, lw=1.6)
    ax.text(3.4, 3.75, "điện trở nung", fontsize=8.6, color=RED, ha="center")
    thermometer(ax, 5.35, 6.2, 1.4, label="nhiệt kế")
    # oát kế / nguồn
    ax.plot([2.0, 7.6], [5.9, 5.9], color=RED, lw=1.6)
    ax.plot([4.8, 7.6], [5.9, 5.9], color=RED, lw=1.6)
    ax.add_patch(Rectangle((7.6, 5.1), 2.6, 1.5, fc="white", ec="#5a6470", lw=1.6))
    ax.text(8.9, 5.85, "oát kế\nP (W)", fontsize=8.8, color="#5a6470", ha="center",
            va="center")
    ax.plot([10.2, 11.0, 11.0, 0.9, 0.9, 2.0], [5.85, 5.85, 0.15, 0.15, 5.9, 5.9],
            color=RED, lw=1.2, ls=":")
    ax.text(5.8, -0.75, "Đo nhiệt dung riêng bằng phương pháp điện", fontsize=9,
            color=GREY, ha="center")
    save(fig, "n_sd_dun_dien"); return _reg("n_sd_dun_dien")


def n_sd_dl1():
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    clean(ax, -1.2, 12.0, -1.8, 5.0)
    ax.add_patch(FancyBboxPatch((4.0, 1.0), 4.0, 2.4, boxstyle="round,pad=0.12",
                                fc="#eef4fb", ec="#333333", lw=2.0))
    ax.text(6.0, 2.2, "HỆ\n(khối khí)", fontsize=11, color="#333333", ha="center",
            va="center", fontweight="bold")
    arrow(ax, 0.6, 2.2, 3.7, 2.2, color=RED, lw=2.2)
    ax.text(2.1, 2.75, "Q > 0: hệ NHẬN nhiệt", fontsize=9.2, color=RED, ha="center")
    arrow(ax, 8.3, 3.9, 11.4, 3.9, color=TEAL, lw=2.2)
    ax.text(9.9, 4.45, "Q < 0: hệ TOẢ nhiệt", fontsize=9.2, color=TEAL, ha="center")
    arrow(ax, 11.4, 0.6, 8.3, 0.6, color=BLUE, lw=2.2)
    ax.text(9.9, 0.05, "A > 0: hệ NHẬN công", fontsize=9.2, color=BLUE, ha="center")
    ax.text(6.0, -1.25, "ΔU = A + Q", fontsize=14, color=DARK if False else "#a61b1b",
            ha="center", fontweight="bold")
    save(fig, "n_sd_dl1"); return _reg("n_sd_dl1")


def n_sd_thang():
    fig, ax = plt.subplots(figsize=(4.0, 4.2))
    clean(ax, -2.6, 7.4, -1.2, 9.4)
    for x, name, c in ((0.6, "Celsius (°C)", BLUE), (5.0, "Kelvin (K)", RED)):
        ax.add_patch(Rectangle((x, 0.4), 0.9, 7.6, fc="white", ec=c, lw=2.0))
        ax.text(x + 0.45, 8.7, name, fontsize=9.6, color=c, ha="center", fontweight="bold")
    marks = [(0.4, "−273", "0"), (2.4, "0", "273"), (4.4, "27", "300"),
             (6.4, "100", "373"), (8.0, "…", "…")]
    for y, cc, kk in marks[:4]:
        ax.plot([0.6, 1.5], [y, y], color=BLUE, lw=1.2)
        ax.plot([5.0, 5.9], [y, y], color=RED, lw=1.2)
        ax.text(0.35, y, cc, fontsize=9.2, color=BLUE, ha="right", va="center")
        ax.text(6.15, y, kk, fontsize=9.2, color=RED, ha="left", va="center")
        ax.plot([1.5, 5.0], [y, y], color=LGREY, lw=0.9, ls=":")
    ax.text(2.8, -0.75, "T (K) = t (°C) + 273", fontsize=10.5, color="#333333",
            ha="center", fontweight="bold")
    ax.text(0.15, 0.4, "độ không\ntuyệt đối", fontsize=7.8, color=GREY, ha="right",
            va="center")
    save(fig, "n_sd_thang"); return _reg("n_sd_thang")


def n_sd_binhnuocnong():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    clean(ax, -1.4, 10.6, -1.4, 7.4)
    ax.add_patch(FancyBboxPatch((1.2, 0.6), 5.0, 5.4, boxstyle="round,pad=0.15",
                                fc="#f2f4f6", ec="#333333", lw=2.2))
    ax.add_patch(Rectangle((1.7, 1.1), 4.0, 4.0, fc="#d8e8f8", ec=GREY, lw=1.2))
    ax.text(3.7, 3.0, "nước\n20 lít", fontsize=10, color=BLUE, ha="center", va="center")
    zx = np.linspace(2.2, 5.2, 50)
    ax.plot(zx, 1.6 + 0.18 * np.sin(np.linspace(0, 7 * np.pi, 50)), color=RED, lw=2.0)
    ax.text(3.7, 0.85, "dây đốt 2500 W", fontsize=8.6, color=RED, ha="center", va="top")
    arrow(ax, 0.0, 4.6, 1.2, 4.6, color=BLUE, lw=1.8)
    ax.text(-0.1, 4.6, "nước lạnh\nvào", fontsize=8.4, color=BLUE, ha="right", va="center")
    arrow(ax, 6.2, 5.4, 7.6, 5.4, color=RED, lw=1.8)
    ax.text(7.8, 5.4, "nước nóng\nra", fontsize=8.4, color=RED, ha="left", va="center")
    ax.text(3.7, -0.9, "Bình nước nóng gia đình", fontsize=9.4, color=GREY, ha="center")
    save(fig, "n_sd_binhnuocnong"); return _reg("n_sd_binhnuocnong")


DARK = "#a61b1b"

ALL = [n_dt_nuocda, n_dt_chi, n_dt_dongdac, n_dt_QdT, n_dt_batchat, n_dt_tn_dunnuoc,
       n_dt_hainhietke, n_sd_cautruc, n_sd_chuyenthe, n_sd_nhietluongke, n_sd_dun_dien,
       n_sd_dl1, n_sd_thang, n_sd_binhnuocnong]

if __name__ == "__main__":
    for f in ALL:
        print("  ", f())
