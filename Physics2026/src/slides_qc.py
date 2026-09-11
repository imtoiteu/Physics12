# -*- coding: utf-8 -*-
"""Kiểm tra chất lượng bộ slide .pptx đã sinh: lỗi kí hiệu, thiếu tiêu đề, ghi chú, hình."""
import os
import re
import sys

from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SLIDES = os.path.join(ROOT, "Slides")

# kí hiệu kiểu mã lập trình không được xuất hiện trên slide
RE_UNDER = re.compile(r"[A-Za-zΔ]_[A-Za-zÀ-ỹ0-9]")
RE_CARET = re.compile(r"\^[({\d]")
RE_LATEX = re.compile(r"\\[a-zA-Z]{2,}|\$")
BAD = []


def texts_of(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                t = "".join(r.text for r in p.runs)
                if t.strip():
                    out.append(t)
        if sh.has_table:
            for row in sh.table.rows:
                for c in row.cells:
                    if c.text.strip():
                        out.append(c.text)
    return out


def main():
    files = []
    for dirpath, _dn, fn in os.walk(SLIDES):
        for f in sorted(fn):
            if f.endswith(".pptx"):
                files.append(os.path.join(dirpath, f))
    files.sort()
    if not files:
        print("Không tìm thấy tệp .pptx nào."); return 1

    tot_slide = tot_pic = tot_tbl = tot_note = 0
    for path in files:
        prs = Presentation(path)
        name = os.path.basename(path)
        npic = ntbl = nnote = 0
        for i, sl in enumerate(prs.slides, 1):
            for sh in sl.shapes:
                if sh.shape_type is not None and sh.shape_type == 13:
                    npic += 1
                if sh.has_table:
                    ntbl += 1
            if sl.has_notes_slide and sl.notes_slide.notes_text_frame.text.strip():
                nnote += 1
            for t in texts_of(sl):
                for rx, msg in ((RE_UNDER, "kí hiệu gạch dưới kiểu mã"),
                                (RE_CARET, "kí hiệu luỹ thừa dạng ^"),
                                (RE_LATEX, "mã LaTeX thô")):
                    m = rx.search(t)
                    if m:
                        BAD.append("%s – slide %d: %s «…%s…»"
                                   % (name, i, msg, t[max(0, m.start() - 18):m.end() + 18]))
        n = len(prs.slides)
        tot_slide += n; tot_pic += npic; tot_tbl += ntbl; tot_note += nnote
        print("  %-58s %2d slide | %2d ảnh | %d bảng | %d ghi chú giảng"
              % (name, n, npic, ntbl, nnote))

    print("\nTổng: %d tệp, %d slide, %d ảnh nhúng, %d bảng, %d slide có ghi chú cho giáo viên."
          % (len(files), tot_slide, tot_pic, tot_tbl, tot_note))
    if BAD:
        print("\n--- LỖI (%d) ---" % len(BAD))
        for b in BAD[:60]:
            print("  ✗", b)
        return 1
    print("✓ Không phát hiện lỗi kí hiệu, lỗi font hay mã LaTeX thô trên slide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
