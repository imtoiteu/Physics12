# -*- coding: utf-8 -*-
"""SLIDE ĐỊNH HƯỚNG — cấu trúc đề thi tốt nghiệp THPT 2026 và lộ trình ôn tập."""
from deck import Deck

TH = 0
CH = "Định hướng ôn thi tốt nghiệp THPT 2026"


def buoi0(d):
    d.title_slide(
        sub="Cấu trúc đề thi, phạm vi kiến thức và lộ trình ôn tập bốn chương đầu",
        meta="Dùng cho buổi khai giảng lớp ôn thi  •  Thời lượng 45 phút",
        points=["Nắm chính xác cấu trúc và cách tính điểm của đề thi từ năm 2025",
                "Biết rõ phạm vi kiến thức của bốn chương đầu",
                "Có lộ trình học và luyện đề cụ thể cho cả khoá"])

    d.section(1, "Cấu trúc đề thi", "Định dạng áp dụng từ kì thi tốt nghiệp THPT 2025",
              items=["Ba phần của đề", "Cách tính điểm phần đúng/sai", "Tỉ lệ mức độ nhận thức"])

    d.table("Cấu trúc đề thi tốt nghiệp THPT môn Vật lí",
            ["Phần", "Loại câu hỏi", "Số câu", "Điểm mỗi câu", "Tổng điểm"],
            [["Phần I", "Trắc nghiệm nhiều phương án lựa chọn", "18", "0,25", "4,50"],
             ["Phần II", "Trắc nghiệm đúng/sai (mỗi câu 4 ý)", "4", "tối đa 1,00", "4,00"],
             ["Phần III", "Trắc nghiệm trả lời ngắn", "6", "0,25", "1,50"],
             ["TỔNG", "28 câu hỏi / 40 lệnh hỏi", "28", "—", "10,00"]],
            widths=[0.8, 2.4, 0.7, 1.0, 0.9], tag="BẮT BUỘC NHỚ",
            foot="Thời gian làm bài: 50 phút. Trung bình 1 phút 47 giây cho mỗi câu hỏi — "
                 "tốc độ là một phần của kĩ năng thi.")

    d.content("Cách tính điểm phần đúng/sai — điểm khác biệt lớn nhất",
              [("head", "Trong MỖI câu của Phần II"),
               ("kv", ("Đúng 1 ý", "được 0,10 điểm")),
               ("kv", ("Đúng 2 ý", "được 0,25 điểm")),
               ("kv", ("Đúng 3 ý", "được 0,50 điểm")),
               ("kv", ("Đúng cả 4 ý", "được 1,00 điểm")),
               ("rule", None),
               ("head", "Hệ quả chiến thuật"),
               ("b", "Điểm tăng RẤT NHANH ở hai ý cuối: từ 3 ý lên 4 ý được thêm nửa điểm, "
                     "bằng đúng hai câu Phần I."),
               ("b", "Vì vậy khi đã chắc 3 ý, hãy dành thêm thời gian cho ý thứ tư thay vì "
                     "vội vàng sang câu khác."),
               ("note", "Không có điểm âm, nên tuyệt đối không bỏ trống bất kì ý nào.")],
              tag="CHIẾN THUẬT", sub="Phần II — trắc nghiệm đúng/sai")

    d.table("Tỉ lệ theo mức độ nhận thức",
            ["Mức độ", "Mô tả", "Tỉ lệ tham khảo", "Số câu ước tính"],
            [["Biết", "Nhận biết, nhắc lại kiến thức đã học", "≈ 40 %", "≈ 16 lệnh hỏi"],
             ["Hiểu", "Giải thích, so sánh, đọc đồ thị đơn giản", "≈ 30 %", "≈ 12 lệnh hỏi"],
             ["Vận dụng", "Giải bài toán nhiều bước, tình huống mới", "≈ 30 %", "≈ 12 lệnh hỏi"]],
            widths=[0.8, 2.3, 1.1, 1.2], tag="MA TRẬN",
            foot="Muốn đạt 7 điểm, chỉ cần làm chắc phần Biết và Hiểu. "
                 "Từ 8 điểm trở lên bắt buộc phải xử lí tốt phần Vận dụng.")

    d.section(2, "Phạm vi kiến thức bốn chương đầu", "Những gì sẽ học trong khoá này",
              items=["Chương I – Vật lí nhiệt", "Chương II – Khí lí tưởng",
                     "Chương III – Từ trường", "Chương IV – Vật lí hạt nhân"])

    d.split("Chương I và Chương II",
            left=[("b", "Cấu trúc của chất. Sự chuyển thể."),
                  ("b", "Nội năng. Định luật I của nhiệt động lực học."),
                  ("b", "Thang nhiệt độ. Nhiệt kế."),
                  ("b", "Nhiệt dung riêng."),
                  ("b", "Nhiệt nóng chảy riêng."),
                  ("b", "Nhiệt hoá hơi riêng."),
                  ("note", "Trọng tâm: ba công thức Q = mcΔT, Q = mλ, Q = mL và phương trình "
                           "cân bằng nhiệt.")],
            right=[("b", "Mô hình động học phân tử chất khí."),
                   ("b", "Định luật Boyle."),
                   ("b", "Định luật Charles."),
                   ("b", "Định luật Gay-Lussac."),
                   ("b", "Phương trình trạng thái. Phương trình Clapeyron."),
                   ("b", "Áp suất và động năng phân tử."),
                   ("note", "Trọng tâm: phương trình trạng thái, bài toán đồ thị và bài toán pit-tông.")],
            lhead="CHƯƠNG I — VẬT LÍ NHIỆT", rhead="CHƯƠNG II — KHÍ LÍ TƯỞNG",
            tag="PHẠM VI")

    d.split("Chương III và Chương IV",
            left=[("b", "Từ trường. Đường sức từ."),
                  ("b", "Lực từ. Cảm ứng từ."),
                  ("b", "Từ thông. Cảm ứng điện từ."),
                  ("b", "Định luật Faraday và định luật Lenz."),
                  ("b", "Đại cương về dòng điện xoay chiều."),
                  ("note", "Trọng tâm: F = BIℓsinα, Φ = BScosθ, |e| = N·|ΔΦ|/Δt và "
                           "giá trị hiệu dụng.")],
            right=[("b", "Cấu trúc hạt nhân. Đơn vị u."),
                   ("b", "Độ hụt khối. Năng lượng liên kết."),
                   ("b", "Phóng xạ. Định luật phóng xạ."),
                   ("b", "Phản ứng hạt nhân. Phân hạch. Nhiệt hạch."),
                   ("b", "Ứng dụng và an toàn phóng xạ."),
                   ("note", "Trọng tâm: năng lượng liên kết riêng, định luật phóng xạ và "
                            "năng lượng phản ứng hạt nhân.")],
            lhead="CHƯƠNG III — TỪ TRƯỜNG", rhead="CHƯƠNG IV — VẬT LÍ HẠT NHÂN",
            tag="PHẠM VI")

    d.section(3, "Lộ trình ôn tập", "Học tới đâu luyện tới đó, cuối khoá tổng duyệt",
              items=["20 buổi lí thuyết", "40 đề luyện theo chương", "30 đề thi thử tổng hợp"])

    d.table("Lộ trình 4 chương + tổng ôn",
            ["Giai đoạn", "Nội dung", "Tài liệu đi kèm"],
            [["Giai đoạn 1", "Chương I — 5 buổi", "10 đề luyện tập Chương 1"],
             ["Giai đoạn 2", "Chương II — 5 buổi", "10 đề luyện tập Chương 2"],
             ["Giai đoạn 3", "Chương III — 5 buổi", "10 đề luyện tập Chương 3"],
             ["Giai đoạn 4", "Chương IV — 5 buổi", "10 đề luyện tập Chương 4"],
             ["Tổng ôn", "Luyện đề, chữa lỗi, bấm giờ", "30 đề thi thử tổng hợp bốn chương"]],
            widths=[1.0, 1.8, 1.8], tag="LỘ TRÌNH",
            foot="Mỗi bộ 10 đề theo chương được sắp xếp từ Dễ đến Khó: đề 1–2 mức Dễ, "
                 "đề 3–4 Dễ đến Trung bình, đề 5–6 Trung bình, đề 7–8 Trung bình đến Khó, "
                 "đề 9–10 mức Khó và phân loại học sinh giỏi.")

    d.content("Cách sử dụng bộ tài liệu này cho hiệu quả",
              [("num", ("1.", "Học lí thuyết theo slide, ghi lại phần “Ba ý phải nhớ” cuối mỗi buổi.")),
               ("num", ("2.", "Làm ngay đề luyện tập tương ứng trong vòng 24 giờ sau buổi học, "
                              "BẤM GIỜ 50 phút như thi thật.")),
               ("num", ("3.", "Tự chấm bằng bảng đáp án, sau đó đọc lời giải chi tiết của MỌI câu — "
                              "kể cả câu làm đúng.")),
               ("num", ("4.", "Ghi mọi câu sai vào SỔ LỖI theo mẫu: mã đề, số câu, kiến thức bị hổng, "
                              "nguyên nhân sai.")),
               ("num", ("5.", "Sau mỗi chương, đọc lại sổ lỗi và làm lại đúng những câu đã sai.")),
               ("num", ("6.", "Bước vào giai đoạn tổng ôn, mỗi tuần làm 3 đề thi thử bấm giờ.")),
               ("note", "Nguyên tắc quan trọng nhất: một câu SAI được phân tích kĩ có giá trị hơn "
                        "mười câu ĐÚNG làm vội.")],
              tag="HƯỚNG DẪN")

    d.wrapup("Bắt đầu từ hôm nay",
             [("head", "Ba cam kết của lớp học"),
              ("b", "Học đủ 20 buổi lí thuyết, không bỏ buổi nào."),
              ("b", "Làm đủ 40 đề theo chương và 30 đề tổng hợp, tất cả đều bấm giờ."),
              ("b", "Duy trì sổ lỗi từ buổi đầu tiên tới ngày thi.")],
             todo=["Chuẩn bị một quyển sổ lỗi riêng.",
                   "Tải bộ đề và in sẵn bảng đáp án.",
                   "Đọc trước Bài 1 — Cấu trúc của chất."])


SPEC = [
    dict(file="00_Dinh_huong_ky_thi_tot_nghiep_THPT_2026.pptx",
         title="Định hướng kì thi tốt nghiệp THPT 2026 môn Vật lí",
         chapter=CH, th=TH, slides=buoi0),
]
