# -*- coding: utf-8 -*-
"""Mở thử tệp .pptx bằng LibreOffice, xuất từng slide ra ảnh PNG để soát bằng mắt.

Dùng cho khâu kiểm tra cuối: lỗi font, mất kí hiệu, công thức biến dạng, tràn chữ.
"""
import os
import subprocess
import sys
import tempfile


def to_png(pptx, outdir, dpi=110, first=None, last=None):
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf",
                        "--outdir", tmp, pptx],
                       check=True, capture_output=True, timeout=600)
        pdf = os.path.join(tmp, os.path.splitext(os.path.basename(pptx))[0] + ".pdf")
        if not os.path.exists(pdf):
            raise RuntimeError("LibreOffice không tạo được PDF cho %s" % pptx)
        base = os.path.join(outdir, os.path.splitext(os.path.basename(pptx))[0])
        cmd = ["pdftoppm", "-png", "-r", str(dpi)]
        if first:
            cmd += ["-f", str(first)]
        if last:
            cmd += ["-l", str(last)]
        subprocess.run(cmd + [pdf, base], check=True, capture_output=True, timeout=600)
    return sorted(f for f in os.listdir(outdir)
                  if f.startswith(os.path.basename(base)) and f.endswith(".png"))


if __name__ == "__main__":
    files = to_png(sys.argv[1], sys.argv[2],
                   first=int(sys.argv[3]) if len(sys.argv) > 3 else None,
                   last=int(sys.argv[4]) if len(sys.argv) > 4 else None)
    print("\n".join(files))
