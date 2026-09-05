# -*- coding: utf-8 -*-
"""Bộ sinh hình vẽ tham số hoá cho toàn bộ ngân hàng đề THPT 2026."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (Rectangle, Circle, Polygon, Ellipse, Arc,
                                FancyBboxPatch, FancyArrowPatch)

from figbase import (save, arrow, clean, frame, hatch_ground,
                     RED, BLUE, GREEN, ORANGE, GREY, PURPLE, TEAL, BROWN, PINK, LGREY)

MADE = []


def _reg(n):
    MADE.append(n)
    return n


def curve(name, series, xlabel, ylabel, xlim=None, ylim=None, xticks=None, yticks=None,
          xticklabels=None, yticklabels=None, size=(6.2, 3.9), annots=(), texts=(),
          hlines=(), vlines=(), grid=True, axhline=False, legend=None):
    """Đồ thị đa đường dùng chung.

    series: [dict(x=[...], y=[...], c=màu, ls='-', lw=2.0, marker=None, ms=6,
                  label=None, fill=False)]
    annots: [(text, (x,y), (xt,yt), màu)]   texts: [(x, y, text, màu, fontsize)]
    """
    fig, ax = plt.subplots(figsize=size)
    for s in series:
        x, y = np.asarray(s["x"], dtype=float), np.asarray(s["y"], dtype=float)
        c = s.get("c", BLUE)
        if s.get("marker"):
            ax.plot(x, y, s["marker"], ms=s.get("ms", 7), mfc=s.get("mfc", "white"),
                    mec=c, mew=1.8, ls=s.get("ls", "none"),
                    color=c, lw=s.get("lw", 1.8), label=s.get("label"), zorder=5)
        else:
            ax.plot(x, y, color=c, ls=s.get("ls", "-"), lw=s.get("lw", 2.2),
                    label=s.get("label"), zorder=4,
                    solid_joinstyle="round")
        if s.get("dots"):
            ax.plot(x, y, "o", ms=5, color=c, zorder=6)
        if s.get("fill"):
            ax.fill(x, y, color=c, alpha=0.07, zorder=1)
    for y0, c, ls in hlines:
        ax.axhline(y0, color=c, lw=1.2, ls=ls, zorder=2)
    for x0, c, ls in vlines:
        ax.axvline(x0, color=c, lw=1.2, ls=ls, zorder=2)
    if axhline:
        ax.axhline(0, color=GREY, lw=1.1, zorder=3)
    for t, xy, xt, c in annots:
        ax.annotate(t, xy=xy, xytext=xt, fontsize=9.2, color=c, ha="center",
                    arrowprops=dict(arrowstyle="->", color=c, lw=1.1), zorder=7)
    for tx in texts:
        x, y, t, c = tx[0], tx[1], tx[2], tx[3]
        fs = tx[4] if len(tx) > 4 else 9.5
        ax.text(x, y, t, fontsize=fs, color=c, ha=tx[5] if len(tx) > 5 else "left",
                va="center", zorder=7, fontweight="bold" if len(tx) > 6 else "normal")
    frame(ax, xlim, ylim, xlabel, ylabel, xticks, yticks, xticklabels, yticklabels,
          grid=grid)
    if legend:
        ax.legend(loc=legend, fontsize=9, framealpha=0.9)
    save(fig, name)
    return _reg(name)


def sinseries(A, T, phi=0.0, tmax=None, n=400, c=BLUE, label=None, lw=2.2, ls="-",
              kind="x"):
    """Chuỗi điểm cho x = A cos(2πt/T + φ) (kind='x'), hoặc v, hoặc a."""
    tmax = tmax if tmax is not None else 2 * T
    t = np.linspace(0, tmax, n)
    w = 2 * np.pi / T
    if kind == "x":
        y = A * np.cos(w * t + phi)
    elif kind == "v":
        y = -A * w * np.sin(w * t + phi)
    else:
        y = -A * w * w * np.cos(w * t + phi)
    return dict(x=t, y=y, c=c, label=label, lw=lw, ls=ls)


def points(xs, ys, c=RED, marker="o", ms=7):
    return dict(x=xs, y=ys, c=c, marker=marker, ms=ms)


# ------------------------------------------------------------------ sơ đồ chung
def piston_cylinder(ax, x0, y0, w, h_gas, h_tot, label="khí", vertical=True,
                    piston_h=0.5, gas_c="#d8e8f8"):
    """Xilanh + pit-tông; trả về toạ độ mặt trên của pit-tông."""
    ax.add_patch(Rectangle((x0, y0), w, h_tot, fc="white", ec="#444444", lw=2.0))
    ax.add_patch(Rectangle((x0, y0), w, h_gas, fc=gas_c, ec="none"))
    ax.add_patch(Rectangle((x0, y0 + h_gas), w, piston_h, fc="#9aa5b1",
                           ec="#5a6470", lw=1.2))
    ax.text(x0 + w / 2, y0 + h_gas / 2, label, fontsize=10, color=BLUE,
            ha="center", va="center")
    return y0 + h_gas + piston_h


def flame(ax, x1, x2, y, n=5, c=ORANGE):
    for k in range(n):
        x = x1 + (x2 - x1) * k / max(1, n - 1)
        ax.plot([x, x + 0.10, x - 0.05, x + 0.07],
                [y, y + 0.20, y + 0.38, y + 0.56], color=c, lw=1.4)


def spring(ax, x1, y1, x2, y2, coils=9, amp=0.28, c="#5a6470", lw=1.6):
    L = np.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    px, py = -uy, ux
    s = np.linspace(0, L, 220)
    off = amp * np.sin(np.linspace(0, coils * 2 * np.pi, 220))
    ax.plot(x1 + ux * s + px * off, y1 + uy * s + py * off, color=c, lw=lw)


def thermometer(ax, x, ytop, ybot, c=GREEN, label=None):
    ax.plot([x, x], [ytop, ybot + 0.18], color=c, lw=2.2)
    ax.add_patch(Circle((x, ybot), 0.17, fc=c, ec=c))
    if label:
        ax.text(x + 0.25, ytop, label, fontsize=8.8, color=c, ha="left", va="top")
