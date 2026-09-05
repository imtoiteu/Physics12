# -*- coding: utf-8 -*-
"""Sinh tài liệu HƯỚNG DẪN SỬ DỤNG VÀ MA TRẬN cho toàn bộ ngân hàng đề."""
import os, sys, importlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import build, make
from build import P, box, table, set_base, add_page_numbers, DARKRED, DARKBLUE, DARKGREEN, GREYTXT

C = WD_ALIGN_PARAGRAPH.CENTER

NGHIEN_CUU = (
    "1. CẤU TRÚC ĐỀ THI TỐT NGHIỆP THPT 2026 – MÔN VẬT LÍ\n"
    "Năm 2026 tiếp tục áp dụng định dạng đề thi đã được Bộ GD&ĐT công bố và áp dụng từ năm 2025:\n"
    "   • 28 câu hỏi / 40 lệnh hỏi / 50 phút / thang điểm 10.\n"
    "   • Phần I – 18 câu trắc nghiệm nhiều phương án lựa chọn (0,25 điểm/câu → 4,50 điểm).\n"
    "   • Phần II – 4 câu trắc nghiệm đúng/sai, mỗi câu 4 ý (đúng 1 ý: 0,10; 2 ý: 0,25; 3 ý: 0,50; "
    "4 ý: 1,00 điểm → 4,00 điểm).\n"
    "   • Phần III – 6 câu trắc nghiệm trả lời ngắn (0,25 điểm/câu → 1,50 điểm).\n"
    "   • Tỉ lệ mức độ tư duy Biết / Hiểu / Vận dụng khoảng 40% / 30% / 30%.\n"
    "   • Nội dung chủ yếu ở lớp 12, có một số câu dùng kiến thức lớp 10 và lớp 11.\n"
    "   • Đánh giá ba thành phần năng lực vật lí: nhận thức vật lí; tìm hiểu thế giới tự nhiên dưới góc "
    "độ vật lí; vận dụng kiến thức, kĩ năng đã học.\n\n"
    "2. PHẠM VI CHƯƠNG TRÌNH (GDPT 2018)\n"
    "   • Vật lí 12 – Chương 1: VẬT LÍ NHIỆT (Cấu trúc của chất, sự chuyển thể; Nội năng và định luật I "
    "nhiệt động lực học; Nhiệt độ, thang nhiệt độ, nhiệt kế; Nhiệt dung riêng; Nhiệt nóng chảy riêng; "
    "Nhiệt hoá hơi riêng).\n"
    "   • Vật lí 12 – Chương 2: KHÍ LÍ TƯỞNG (Mô hình động học phân tử chất khí; Định luật Boyle; Định "
    "luật Charles; Phương trình trạng thái của khí lí tưởng; Áp suất khí theo mô hình động học phân tử "
    "và quan hệ giữa động năng phân tử với nhiệt độ).\n"
    "   • Vật lí 11 – Chương 1: DAO ĐỘNG (Dao động điều hoà; Mô tả dao động điều hoà; Vận tốc, gia tốc "
    "trong dao động điều hoà; Động năng, thế năng và sự chuyển hoá năng lượng — gồm cơ năng của con lắc "
    "lò xo và con lắc đơn; Dao động tắt dần, dao động cưỡng bức, hiện tượng cộng hưởng)."
)

HUONG_DAN = (
    "• MỖI ĐỀ là một bài thi hoàn chỉnh theo đúng định dạng đề thi tốt nghiệp THPT: 28 câu / 40 lệnh hỏi "
    "/ 50 phút / 10 điểm. Hãy làm trọn vẹn một đề trong đúng 50 phút để rèn tốc độ và sức bền.\n"
    "• ĐỘ KHÓ TĂNG DẦN từ Đề 1 tới Đề 10 trong mỗi bộ. Nên làm tuần tự; chỉ chuyển sang đề sau khi đã "
    "hiểu trọn vẹn lời giải của đề trước.\n"
    "• MỖI CÂU trong tệp lời giải đều ghi rõ MỨC ĐỘ (Dễ / Trung bình / Khó / Rất khó) và KIẾN THỨC – "
    "KĨ NĂNG được kiểm tra. Sau khi chấm, hãy thống kê những kĩ năng mình hay sai để ôn lại đúng chỗ.\n"
    "• PHẦN LỜI GIẢI không chỉ đưa đáp số: nhiều câu còn phân tích các phương án nhiễu ứng với từng sai "
    "lầm cụ thể. Hãy đọc cả phần đó ngay cả khi bạn đã làm đúng.\n"
    "• VỚI CÂU ĐÚNG/SAI, mỗi ý được chấm độc lập; đừng suy đoán theo kiểu “chắc phải có hai ý đúng, hai "
    "ý sai”. Trong bộ đề này, số ý sai mỗi câu thay đổi (1 hoặc 2 ý) và vị trí ý sai được trải đều.\n"
    "• VỚI CÂU TRẢ LỜI NGẮN, luôn đọc kĩ ĐƠN VỊ và yêu cầu LÀM TRÒN ghi ở cuối câu.\n"
    "• BỘ ĐỀ TỔNG HỢP CHƯƠNG 1 + 2 nên làm sau khi đã hoàn thành hai bộ đề riêng của từng chương, vì "
    "nhiều câu bắt buộc dùng đồng thời định luật I nhiệt động lực học và phương trình trạng thái khí."
)


def build_guide(filename="00_HUONG_DAN_SU_DUNG_VA_MA_TRAN.docx"):
    doc = Document(); set_base(doc); add_page_numbers(doc)
    P(doc, "NGÂN HÀNG ĐỀ LUYỆN THI TỐT NGHIỆP THPT 2026", bold=True, size=12,
      align=C, after=0, color=GREYTXT)
    P(doc, "MÔN VẬT LÍ", bold=True, size=26, align=C, after=1, color=DARKRED)
    P(doc, "HƯỚNG DẪN SỬ DỤNG VÀ MA TRẬN TOÀN BỘ", bold=True, size=15, align=C, after=2,
      color=DARKBLUE)
    P(doc, "40 đề – 1120 câu hỏi – có đáp án và lời giải chi tiết cho từng câu",
      italic=True, size=11.5, align=C, after=10)
    box(doc, "CƠ SỞ BIÊN SOẠN", NGHIEN_CUU, fill="F4F6F8")
    box(doc, "HƯỚNG DẪN SỬ DỤNG", HUONG_DAN, fill="F2F8F0", tcolor=DARKGREEN)
    doc.add_page_break()

    P(doc, "DANH MỤC TÀI LIỆU", bold=True, size=14, align=C, before=4, after=4, color=DARKRED)
    rows = []
    tong = 0
    for modname, fde, fgiai in make.SPEC:
        mod = importlib.import_module(modname)
        g = mod.NHOM
        n = sum(len(t["P1"]) + len(t["P2"]) + len(t["P3"]) for t in g["tests"])
        tong += n
        rows.append([g["ten_nhom"], "%d đề" % len(g["tests"]), "%d câu" % n, fde])
        rows.append(["", "", "", fgiai])
    table(doc, None, ["Bộ đề", "Số đề", "Số câu", "Tên tệp"], rows, size=9)
    P(doc, "Tổng cộng: 40 đề – %d câu hỏi." % tong, bold=True, size=11.5, align=C, after=8)

    for modname, _fde, _fgiai in make.SPEC:
        mod = importlib.import_module(modname)
        g = mod.NHOM
        P(doc, g["ten_nhom"], bold=True, size=13, before=10, after=3, color=DARKBLUE)
        rows = []
        for t in g["tests"]:
            cnt = {m: 0 for m in build.MUC_LIST}
            for _c, _i, it in build.all_items(t):
                cnt[it.get("md", "Trung bình")] += 1
            rows.append([t["ma"], t["muc"]] + [str(cnt[m]) for m in build.MUC_LIST]
                        + [t["trongtam"]])
        table(doc, None, ["Mã đề", "Mức độ chung"] + build.MUC_LIST + ["Trọng tâm"], rows, size=8.5)

    P(doc, "--- HẾT ---", bold=True, align=C, before=10)
    path = os.path.join(ROOT, filename); doc.save(path)
    return path


if __name__ == "__main__":
    print("✓", os.path.basename(build_guide()))
