# -*- coding: utf-8 -*-
"""Tiện ích dùng chung cho mọi bộ đề: nhãn mức độ và ba hàm dựng câu hỏi.

Cấu trúc một câu hỏi
--------------------
mc  – trắc nghiệm nhiều phương án: q (đề), o (4 phương án), a (đáp án A–D),
      sol (lời giải), kn (kiến thức – kĩ năng), md (mức độ).
ds  – trắc nghiệm đúng/sai: stem (dẫn đề), items (4 ý, mỗi ý gồm nội dung,
      giá trị Đ/S và lời giải thích riêng), kn, md.
sa  – trắc nghiệm trả lời ngắn: q, ans (đáp số), sol, kn, md.

Tuỳ chọn thêm cho cả ba loại: fig (tên hình), cap (chú thích hình),
tbl (bảng số liệu dạng (chú thích, tiêu đề cột, các hàng)).
"""

D, TB, K, RK = "Dễ", "Trung bình", "Khó", "Rất khó"


def mc(q, o, a, sol, kn, md, **kw):
    return dict(q=q, o=o, a=a, sol=sol, kn=kn, md=md, **kw)


def ds(stem, items, kn, md, **kw):
    return dict(stem=stem, items=items, kn=kn, md=md, **kw)


def sa(q, ans, sol, kn, md, **kw):
    return dict(q=q, ans=ans, sol=sol, kn=kn, md=md, **kw)
