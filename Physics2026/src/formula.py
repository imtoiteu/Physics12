# -*- coding: utf-8 -*-
"""Render công thức Toán – Vật lí thành ảnh PNG độ phân giải cao để nhúng vào slide.

Lí do dùng ảnh thay vì gõ trực tiếp: bảo đảm công thức KHÔNG BAO GIỜ bị lỗi font,
mất kí hiệu, hay hiện mã LaTeX thô trên máy của giáo viên — dù mở bằng PowerPoint,
LibreOffice Impress hay Google Slides.

Ảnh nền trong suốt, dựng bằng bộ chữ toán STIX (cùng hệ với Times New Roman) nên
hoà hợp với chữ trên slide.
"""
import hashlib
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "formulas"))
os.makedirs(OUT, exist_ok=True)

DPI = 420           # ~5–6 lần độ phân giải trình chiếu ⇒ nét khi phóng to
BASE_PT = 26.0      # cỡ chữ gốc khi dựng ảnh; deck.py sẽ co giãn theo chiều cao mong muốn

matplotlib.rcParams["mathtext.fontset"] = "stix"
matplotlib.rcParams["font.family"] = "STIXGeneral"

_CACHE = {}

# Bộ chữ toán STIX không có glyph cho nguyên âm tiếng Việt có dấu (ậ, ệ, ơ...).
# Nếu lỡ đưa chữ tiếng Việt vào công thức, PowerPoint sẽ hiện ô vuông.
# Vì vậy chặn ngay tại đây: công thức CHỈ được dùng kí tự ASCII, chữ Hi Lạp
# và kí hiệu toán phải viết bằng lệnh LaTeX (\alpha, \Delta, \circ, \cdot ...).
def guard(tex):
    bad = sorted({c for c in tex if ord(c) > 126})
    if bad:
        raise ValueError(
            "Công thức chứa kí tự ngoài ASCII %r — hãy dùng lệnh LaTeX thay thế "
            "và đưa phần chữ tiếng Việt ra ngoài ảnh công thức.\n  %s" % (bad, tex))
    return tex


def _key(tex, color, pt):
    h = hashlib.md5(("%s|%s|%.2f" % (tex, color, pt)).encode("utf-8")).hexdigest()[:16]
    return h


def render(tex, color="#1A1A1A", pt=BASE_PT):
    """tex: chuỗi LaTeX KHÔNG kèm dấu $ bao ngoài.  Trả về (đường dẫn, rộng_inch, cao_inch)."""
    guard(tex)
    k = _key(tex, color, pt)
    if k in _CACHE:
        return _CACHE[k]
    path = os.path.join(OUT, "f_%s.png" % k)
    meta = path[:-4] + ".txt"
    if os.path.exists(path) and os.path.exists(meta):
        with open(meta, encoding="utf-8") as f:
            w, h = [float(x) for x in f.read().split()]
        _CACHE[k] = (path, w, h)
        return _CACHE[k]

    fig = plt.figure(figsize=(0.1, 0.1))
    t = fig.text(0, 0, "$%s$" % tex, fontsize=pt, color=color)
    fig.canvas.draw()
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    w_in = bb.width / fig.dpi
    h_in = bb.height / fig.dpi
    plt.close(fig)

    pad = 0.03
    fig = plt.figure(figsize=(w_in + 2 * pad, h_in + 2 * pad))
    fig.text(pad / (w_in + 2 * pad), 0.5, "$%s$" % tex, fontsize=pt, color=color,
             ha="left", va="center")
    fig.savefig(path, dpi=DPI, transparent=True, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)

    from PIL import Image
    with Image.open(path) as im:
        pw, ph = im.size
    w_in, h_in = pw / float(DPI), ph / float(DPI)
    with open(meta, "w", encoding="utf-8") as f:
        f.write("%.6f %.6f" % (w_in, h_in))
    _CACHE[k] = (path, w_in, h_in)
    return _CACHE[k]


def check(tex):
    """Thử dựng công thức; trả về None nếu hợp lệ, chuỗi lỗi nếu LaTeX sai."""
    try:
        render(tex)
        return None
    except Exception as e:            # noqa: BLE001 - muốn bắt mọi lỗi cú pháp mathtext
        return "%s: %s" % (type(e).__name__, e)


if __name__ == "__main__":
    tests = [
        r"\Delta U = A + Q",
        r"Q = mc\Delta T",
        r"\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}",
        r"pV = nRT = \frac{m}{M}RT",
        r"\bar{W_{\!d}} = \frac{3}{2}kT",
        r"p = \frac{1}{3}\mu m \overline{v^2}",
        r"F = BIl\sin\alpha",
        r"e_c = -\frac{\Delta\Phi}{\Delta t}",
        r"\Delta m = Zm_p + (A-Z)m_n - m_X",
        r"N = N_0 \cdot 2^{-t/T} = N_0 e^{-\lambda t}",
        r"W_{lk} = \Delta m c^2",
        r"T = 2\pi\sqrt{\frac{l}{g}}",
        r"A^2 = x^2 + \frac{v^2}{\omega^2}",
    ]
    for t in tests:
        err = check(t)
        p, w, h = render(t)
        print(("OK  " if err is None else "LOI "), "%.2f x %.2f in" % (w, h), t, err or "")
