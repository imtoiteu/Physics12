# -*- coding: utf-8 -*-
"""Tiện ích vẽ hình dùng chung cho hai bộ đề VẬN DỤNG CAO."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Rectangle, Circle, FancyArrowPatch, Polygon,
                                Arc, Ellipse, FancyBboxPatch, Wedge)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs"))
os.makedirs(OUT, exist_ok=True)

RED, BLUE, GREEN, ORANGE, GREY = "#c0392b", "#1f4e9c", "#1e8449", "#d35400", "#555555"
PURPLE, TEAL, BROWN, PINK = "#6c3483", "#117a65", "#7b4b1e", "#b03a5b"
LGREY = "#bbbbbb"


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return name


def arrow(ax, x1, y1, x2, y2, color="k", lw=1.6, ms=12, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, **kw))


def clean(ax, xl, xr, yb, yt, eq=True):
    """Khung vẽ sơ đồ: không trục, không viền."""
    ax.set_xlim(xl, xr)
    ax.set_ylim(yb, yt)
    if eq:
        ax.set_aspect("equal")
    ax.axis("off")


def frame(ax, xlim, ylim, xlab, ylab, xticks=None, yticks=None,
          xticklabels=None, yticklabels=None, grid=True):
    """Khung vẽ đồ thị có hai trục mũi tên."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GREY)
        ax.spines[s].set_linewidth(1.2)
    ax.set_xlabel(xlab, fontsize=10.5, labelpad=2)
    ax.set_ylabel(ylab, fontsize=10.5, labelpad=2)
    if xticks is not None:
        ax.set_xticks(xticks)
        if xticklabels is not None:
            ax.set_xticklabels(xticklabels)
    if yticks is not None:
        ax.set_yticks(yticks)
        if yticklabels is not None:
            ax.set_yticklabels(yticklabels)
    if grid:
        ax.grid(alpha=0.30, ls=":", lw=0.8)
    ax.tick_params(labelsize=9, colors=GREY)
    for lb in ax.get_xticklabels() + ax.get_yticklabels():
        lb.set_color("black")


def guide(ax, x, y, color=LGREY, lw=1.0):
    """Hai đoạn nét đứt gióng từ điểm (x, y) về hai trục."""
    ax.plot([x, x], [0, y], ls="--", lw=lw, color=color, zorder=0)
    ax.plot([0, x], [y, y], ls="--", lw=lw, color=color, zorder=0)


def dot(ax, x, y, color="k", s=28, label=None, dx=0.02, dy=0.03, fs=10, **kw):
    ax.plot([x], [y], "o", ms=np.sqrt(s), color=color, zorder=5, **kw)
    if label:
        ax.text(x + dx, y + dy, label, fontsize=fs, color=color,
                ha="left", va="bottom", zorder=6)


def hatch_ground(ax, x1, x2, y, h=0.12, n=14, color=GREY, lw=1.2):
    ax.plot([x1, x2], [y, y], color=color, lw=lw + 0.4)
    for xx in np.linspace(x1, x2 - (x2 - x1) / n, n):
        ax.plot([xx, xx + (x2 - x1) / n * 0.7], [y, y - h], color=color, lw=lw * 0.8)


def cross_field(ax, x1, x2, y1, y2, n=5, m=4, color=BLUE, size=8):
    """Vùng từ trường hướng vào trong trang giấy (dấu ×)."""
    for xx in np.linspace(x1, x2, n):
        for yy in np.linspace(y1, y2, m):
            ax.text(xx, yy, "×", color=color, fontsize=size,
                    ha="center", va="center", zorder=1)


def dot_field(ax, x1, x2, y1, y2, n=5, m=4, color=BLUE, size=6):
    """Vùng từ trường hướng ra ngoài trang giấy (dấu ·)."""
    for xx in np.linspace(x1, x2, n):
        for yy in np.linspace(y1, y2, m):
            ax.plot([xx], [yy], "o", ms=2.6, mfc="white", mec=color, mew=1.1, zorder=1)
