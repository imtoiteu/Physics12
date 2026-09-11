# -*- coding: utf-8 -*-
"""SLIDE BÀI GIẢNG — CHƯƠNG I: VẬT LÍ NHIỆT.  Năm buổi dạy."""
from deck import Deck

TH = 1
CH = "Chương I – Vật lí nhiệt"
MT = "Ôn thi tốt nghiệp THPT 2026  •  Lớp 12"


# =====================================================================  BUỔI 1
def buoi1(d):
    d.title_slide(
        sub="Buổi 1 — Mô hình động học phân tử, ba thể của chất và sự chuyển thể",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được ba nội dung của mô hình động học phân tử chất",
                "Giải thích được đặc điểm của thể rắn, lỏng, khí bằng lực tương tác phân tử",
                "Đọc được đồ thị nhiệt độ – thời gian của quá trình chuyển thể"])

    d.section(1, "Mô hình động học phân tử", "Mọi hiện tượng nhiệt đều bắt nguồn từ chuyển động của phân tử",
              items=["Ba luận điểm cơ bản", "Lực tương tác giữa các phân tử",
                     "Giải thích đặc điểm ba thể"])

    d.content("Ba luận điểm của mô hình động học phân tử",
              [("num", ("1.", "Các chất được cấu tạo từ những hạt riêng biệt là phân tử, nguyên tử. "
                              "Giữa chúng có khoảng cách.")),
               ("num", ("2.", "Các phân tử chuyển động hỗn loạn không ngừng. Chuyển động này gọi là "
                              "chuyển động nhiệt.")),
               ("num", ("3.", "Nhiệt độ của vật càng cao thì các phân tử chuyển động càng nhanh.")),
               ("rule", None),
               ("head", "Hai bằng chứng thực nghiệm"),
               ("b", "Hiện tượng khuếch tán: nhỏ mực vào nước, mực tự lan ra dù không khuấy."),
               ("b", "Chuyển động Brown: hạt phấn hoa trong nước chuyển động gấp khúc ngẫu nhiên."),
               ("note", "Đây là mô hình, không phải điều hiển nhiên. Mọi công thức của chương "
                        "đều được suy ra từ ba luận điểm này.")],
              sub="Bài 1 — Cấu trúc của chất", tag="LÍ THUYẾT",
              note="Hỏi mở đầu: vì sao khi mở lọ nước hoa ở cuối lớp, một lúc sau cả lớp đều ngửi thấy? "
                   "Dẫn dắt tới luận điểm 2.")

    d.figure("Lực tương tác giữa các phân tử", "n_sd_luc_phan_tu",
             items=[("head", "Hai lực luôn cùng tồn tại"),
                    ("b", "Lực hút — chiếm ưu thế khi hai phân tử ở xa nhau."),
                    ("b", "Lực đẩy — chiếm ưu thế khi hai phân tử ở rất gần nhau."),
                    ("b", "Ở khoảng cách r₀ hai lực cân bằng, hợp lực bằng 0."),
                    ("note", "Đây là lí do vật rắn vừa khó kéo giãn vừa khó nén lại: "
                             "kéo ra thì lực hút chống lại, nén vào thì lực đẩy chống lại.")],
             cap="Hợp lực tương tác giữa hai phân tử theo khoảng cách", tag="TRỌNG TÂM",
             figw=5.9,
             note="Nhấn mạnh: r₀ cỡ 10⁻¹⁰ m. Ở thể khí khoảng cách trung bình lớn gấp khoảng 10 lần r₀ "
                  "nên lực tương tác coi như bằng 0 — đó chính là giả thiết của khí lí tưởng ở chương II.")

    d.figure("Ba thể của chất", "n_sd_cautruc",
             items=[("head", "So sánh nhanh"),
                    ("b", "Rắn: r ≈ r₀, lực mạnh, trật tự xa, hạt chỉ dao động quanh vị trí cân bằng CỐ ĐỊNH."),
                    ("b", "Lỏng: r hơi lớn hơn r₀, trật tự gần, vị trí cân bằng LUÔN THAY ĐỔI."),
                    ("b", "Khí: r ≫ r₀, lực ≈ 0, hạt chuyển động tự do khắp bình chứa."),
                    ("note", "Bẫy hay gặp: “chất lỏng không có trật tự” là SAI — chất lỏng có trật tự gần.")],
             cap="Mô hình sắp xếp hạt ở ba thể", tag="SO SÁNH", figw=6.4, side="right")

    d.table("Đặc điểm ba thể — bảng chốt",
            ["Tính chất", "Thể rắn", "Thể lỏng", "Thể khí"],
            [["Thể tích riêng", "Có, xác định", "Có, xác định", "Không"],
             ["Hình dạng riêng", "Có, xác định", "Không (theo bình)", "Không (theo bình)"],
             ["Khoảng cách hạt", "≈ r₀ (rất gần)", "Hơi lớn hơn r₀", "Rất lớn so với r₀"],
             ["Lực tương tác", "Rất mạnh", "Trung bình", "Rất yếu, bỏ qua được"],
             ["Chuyển động hạt", "Dao động quanh nút mạng", "Dao động + trượt lên nhau", "Tự do, hỗn loạn"],
             ["Khả năng nén", "Rất khó nén", "Khó nén", "Dễ nén"]],
            widths=[1.5, 1.15, 1.3, 1.3], tag="BẢNG CHỐT",
            foot="Học theo cột dọc thì rời rạc; học theo hàng ngang để thấy quy luật: mọi khác biệt "
                 "đều do khoảng cách và lực tương tác giữa các hạt.")

    d.section(2, "Sự chuyển thể", "Khi nhiệt độ thay đổi, chất có thể đổi từ thể này sang thể khác",
              items=["Sáu quá trình chuyển thể", "Nóng chảy và đông đặc",
                     "Hoá hơi: bay hơi và sôi", "Đọc đồ thị chuyển thể"])

    d.figure("Sơ đồ các quá trình chuyển thể", "n_sd_chuyenthe",
             items=[("head", "Nhớ theo cặp"),
                    ("b", "Nóng chảy (rắn → lỏng) THU nhiệt ↔ đông đặc (lỏng → rắn) TOẢ nhiệt."),
                    ("b", "Hoá hơi (lỏng → khí) THU nhiệt ↔ ngưng tụ (khí → lỏng) TOẢ nhiệt."),
                    ("b", "Thăng hoa (rắn → khí) THU nhiệt ↔ ngưng kết (khí → rắn) TOẢ nhiệt."),
                    ("note", "Đi sang PHẢI trên sơ đồ luôn là thu nhiệt, đi sang TRÁI luôn là toả nhiệt.")],
             cap="Sáu quá trình chuyển thể", tag="SƠ ĐỒ", figw=6.3,
             note="Ví dụ thăng hoa quen thuộc: băng phiến (long não) để trong tủ quần áo nhỏ dần rồi biến mất.")

    d.content("Nóng chảy và đông đặc",
              [("head", "Đặc điểm chung"),
               ("b", "Mỗi chất kết tinh có một NHIỆT ĐỘ NÓNG CHẢY xác định ở áp suất cho trước; "
                     "nhiệt độ đông đặc bằng đúng nhiệt độ nóng chảy."),
               ("b", "Trong suốt quá trình nóng chảy, nhiệt độ của chất KHÔNG ĐỔI dù vẫn liên tục thu nhiệt."),
               ("b", "Nhiệt lượng thu vào lúc đó dùng để phá vỡ trật tự mạng tinh thể, tức làm tăng "
                     "thế năng tương tác chứ không làm tăng động năng phân tử."),
               ("gap", 0.06),
               ("head", "Phân biệt chất kết tinh và chất vô định hình"),
               ("sub", "Chất kết tinh (nước đá, kim loại, muối ăn): nóng chảy ở nhiệt độ xác định."),
               ("sub", "Chất vô định hình (thuỷ tinh, nhựa đường, sáp): mềm dần rồi chảy, không có "
                       "nhiệt độ nóng chảy xác định."),
               ("note", "Vì nhiệt độ không đổi mà nội năng vẫn tăng, nên nhiệt độ KHÔNG phải thước đo "
                        "của nội năng — chỉ là thước đo của động năng trung bình.")],
              sub="Bài 1 — Sự chuyển thể", tag="TRỌNG TÂM")

    d.figure("Bay hơi và sôi — hai hình thức hoá hơi", "n_sd_bayhoi_soi",
             items=[("head", "Điểm khác nhau cốt lõi"),
                    ("b", "Bay hơi xảy ra ở mọi nhiệt độ, chỉ trên mặt thoáng."),
                    ("b", "Sôi chỉ xảy ra ở nhiệt độ sôi, diễn ra cả trong lòng chất lỏng."),
                    ("b", "Trong khi sôi, nhiệt độ chất lỏng không đổi."),
                    ("note", "Nhiệt độ sôi phụ thuộc áp suất: trên núi cao áp suất thấp nên nước "
                             "sôi dưới 100 °C, vì thế luộc thức ăn lâu chín.")],
             cap="So sánh bay hơi và sôi", tag="PHÂN BIỆT", figw=6.0, side="left")

    d.bigfigure("Đọc đồ thị nhiệt độ – thời gian", "n_dt_nuocda",
                cap="Đun một khối nước đá với nguồn nhiệt có công suất không đổi",
                items=[("head", "Quy tắc đọc"),
                       ("b", "Đoạn NGHIÊNG: chất chưa đổi thể, nhiệt độ tăng — dùng Q = mcΔT. "
                             "Độ dốc càng nhỏ thì nhiệt dung riêng càng lớn."),
                       ("b", "Đoạn NẰM NGANG: chất đang chuyển thể, nhiệt độ không đổi — dùng Q = mλ "
                             "(nóng chảy) hoặc Q = mL (hoá hơi).")],
                tag="ĐỒ THỊ",
                note="Yêu cầu học sinh chỉ ra trên đồ thị: tại t = 200 s trong bình có gì? "
                     "Đáp: hỗn hợp nước đá và nước, cùng ở 0 °C.")

    d.quiz("Kiểm tra nhanh 1",
           "Khi đun nước đá đang ở 0 °C, nhiệt độ không tăng trong một khoảng thời gian. Vì sao?",
           ["Nguồn nhiệt tạm thời ngừng cung cấp nhiệt.",
            "Nhiệt lượng thu vào dùng để phá vỡ mạng tinh thể, làm tăng thế năng tương tác.",
            "Nước đá phản xạ lại toàn bộ nhiệt lượng nhận được.",
            "Nhiệt dung riêng của nước đá lúc đó trở nên vô cùng lớn."],
           "B",
           "Nhiệt vẫn được cấp liên tục nhưng chuyển hoàn toàn thành thế năng tương tác giữa các phân tử "
           "để phá vỡ trật tự tinh thể; động năng trung bình không đổi nên nhiệt độ không đổi.")

    d.quiz("Kiểm tra nhanh 2",
           "Phát biểu nào sau đây về chất lỏng là ĐÚNG?",
           ["Có thể tích riêng và hình dạng riêng xác định.",
            "Các phân tử hoàn toàn không có trật tự nào.",
            "Có trật tự gần; vị trí cân bằng của mỗi phân tử luôn thay đổi.",
            "Khoảng cách giữa các phân tử lớn hơn nhiều lần kích thước phân tử."],
           "C",
           "Chất lỏng có trật tự gần (mỗi phân tử sắp xếp có quy luật với vài phân tử lân cận) nhưng "
           "vị trí cân bằng dịch chuyển liên tục, nhờ đó chất lỏng chảy được. "
           "Phương án cuối mô tả thể khí.")

    d.media("Mô phỏng và thí nghiệm nên dùng cho buổi này",
            [("States of Matter: Basics", "PhET – phet.colorado.edu",
              "Đổi giữa rắn – lỏng – khí, tăng giảm nhiệt độ và quan sát trực tiếp chuyển động phân tử.",
              "Khi chuyển từ rắn sang lỏng, các hạt bắt đầu trượt lên nhau chứ không chỉ dao động tại chỗ."),
             ("Đun nước đá trong cốc thuỷ tinh có nhiệt kế", "Thí nghiệm làm trực tiếp tại lớp",
              "Bỏ nước đá vụn vào cốc, đun đều, đọc nhiệt kế mỗi 30 giây rồi vẽ đồ thị.",
              "Nhiệt kế đứng yên ở 0 °C trong nhiều phút dù ngọn lửa vẫn cháy."),
             ("Băng phiến thăng hoa", "Quan sát tại lớp",
              "Đặt viên băng phiến trong lọ thuỷ tinh đậy kín vài ngày.",
              "Viên băng phiến nhỏ dần, tinh thể bám lại trên thành lọ — rắn → khí → rắn.")],
            lead="Ba tài nguyên thay cho việc mô tả hiện tượng bằng lời.")

    d.wrapup("Tổng kết buổi 1",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Ba luận điểm của mô hình động học phân tử."),
              ("b", "Mọi khác biệt giữa ba thể đều quy về khoảng cách và lực tương tác giữa các hạt."),
              ("b", "Đi sang phải trên sơ đồ chuyển thể là thu nhiệt, sang trái là toả nhiệt."),
              ("b", "Trong khi chuyển thể, nhiệt độ không đổi nhưng nội năng vẫn thay đổi.")],
             todo=["Làm Đề 1 – Chương 1 (mức Dễ).",
                   "Vẽ lại sơ đồ sáu quá trình chuyển thể vào vở.",
                   "Tìm 3 ví dụ thực tế cho sự bay hơi và 3 ví dụ cho sự ngưng tụ."])


# =====================================================================  BUỔI 2
def buoi2(d):
    d.title_slide(
        sub="Buổi 2 — Nội năng, công, nhiệt lượng và định luật I của nhiệt động lực học",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được nội năng là gì và phụ thuộc những yếu tố nào",
                "Vận dụng được ΔU = A + Q với quy ước dấu chính xác",
                "Giải được bài toán nén / giãn khí và truyền nhiệt cơ bản"])

    d.section(1, "Nội năng", "Năng lượng bên trong vật, không phải năng lượng chuyển động của cả vật",
              items=["Định nghĩa", "Nội năng phụ thuộc gì", "Hai cách làm biến đổi nội năng"])

    d.content("Nội năng là gì?",
              [("head", "Định nghĩa"),
               ("p", "Nội năng U của một vật là tổng động năng chuyển động nhiệt của các phân tử "
                     "cấu tạo nên vật và thế năng tương tác giữa các phân tử đó."),
               ("fx", r"U = \sum W_{\mathrm{d}} + \sum W_{\mathrm{t}}"),
               ("head", "Nội năng phụ thuộc vào"),
               ("b", "Nhiệt độ T — quyết định động năng trung bình của phân tử."),
               ("b", "Thể tích V — quyết định khoảng cách giữa các phân tử, tức thế năng tương tác."),
               ("note", "Nội năng KHÔNG bao gồm động năng chuyển động của cả vật, cũng không bao gồm "
                        "thế năng trọng trường của vật. Một viên đạn bay nhanh không vì thế mà có nội "
                        "năng lớn hơn khi nó nằm yên."),
               ("sub", "Với khí lí tưởng, lực tương tác bị bỏ qua nên U chỉ còn phụ thuộc nhiệt độ.")],
              sub="Bài 2 — Nội năng", tag="LÍ THUYẾT",
              note="Câu hỏi kiểm tra hiểu: hai cốc nước giống hệt nhau, một cốc đặt yên trên bàn, "
                   "một cốc đặt trên ô tô chạy 20 m/s. Nội năng khác nhau không? (Không.)")

    d.split("Hai cách làm biến đổi nội năng",
            left=[("b", "Ép pit-tông nén khí trong xi lanh."),
                  ("b", "Cọ xát hai vật vào nhau."),
                  ("b", "Búa đập vào miếng kim loại."),
                  ("gap", 0.08),
                  ("note", "Có sự chuyển hoá dạng năng lượng: cơ năng → nội năng.")],
            right=[("b", "Thả vật nóng vào nước lạnh."),
                   ("b", "Đun vật trên bếp."),
                   ("b", "Phơi vật dưới nắng."),
                   ("gap", 0.08),
                   ("note", "Chỉ có sự TRUYỀN năng lượng, không chuyển hoá dạng.")],
            lhead="① THỰC HIỆN CÔNG  (A)", rhead="② TRUYỀN NHIỆT  (Q)",
            sub="Bài 2 — Nội năng", tag="SO SÁNH",
            note="Nhấn mạnh khác biệt bản chất: thực hiện công có chuyển hoá dạng năng lượng, "
                 "truyền nhiệt thì không.")

    d.figure("Quy ước dấu — chỗ mất điểm nhiều nhất", "n_sd_quy_uoc_dau",
             items=[("head", "Một câu để nhớ"),
                    ("b", "Mũi tên hướng VÀO vật thì đại lượng mang dấu DƯƠNG."),
                    ("sub", "Khí bị nén ⇒ nhận công ⇒ A > 0."),
                    ("sub", "Khí giãn nở ⇒ sinh công ⇒ A < 0."),
                    ("sub", "Vật thu nhiệt ⇒ Q > 0; vật toả nhiệt ⇒ Q < 0."),
                    ("note", "Luôn xác định rõ đang xét VẬT NÀO trước khi gán dấu.")],
             cap="Quy ước dấu của công và nhiệt lượng", tag="TRỌNG TÂM", figw=6.2, side="right")

    d.formulas("Định luật I của nhiệt động lực học",
               [(r"\Delta U = A + Q",
                 "Độ biến thiên nội năng của vật bằng tổng công và nhiệt lượng mà vật nhận được."),
                (r"\Delta U = Q",
                 "Quá trình ĐẲNG TÍCH: thể tích không đổi nên A = 0, toàn bộ nhiệt lượng làm đổi nội năng."),
                (r"\Delta U = A",
                 "Quá trình ĐOẠN NHIỆT: không trao đổi nhiệt (Q = 0), chỉ có công làm đổi nội năng.")],
               lead="Định luật I chính là định luật bảo toàn năng lượng áp dụng cho hiện tượng nhiệt.",
               foot="Với quá trình đẳng nhiệt của khí lí tưởng: ΔU = 0 nên Q = −A, "
                    "khí nhận bao nhiêu nhiệt thì sinh ra bấy nhiêu công.",
               tag="TRỌNG TÂM", sub="Bài 2 — Định luật I")

    d.figure("Công của chất khí", "n_sd_cong_cua_khi",
             items=[("head", "Khi nào khí sinh công?"),
                    ("b", "Chỉ khi THỂ TÍCH thay đổi. Áp suất thay đổi mà thể tích giữ nguyên thì A = 0."),
                    ("b", "Khí giãn nở: đẩy pit-tông ra, khí sinh công, A < 0."),
                    ("b", "Khí bị nén: pit-tông ép vào, khí nhận công, A > 0."),
                    ("note", "Bài toán bình kín thành cứng: dù đun nóng bao nhiêu, A vẫn luôn bằng 0.")],
             cap="Nén và giãn khí trong xi lanh", tag="TRỌNG TÂM", figw=6.4, side="left")

    d.example("Ví dụ 1 — Nén khí trong xi lanh",
              "Người ta nén một lượng khí trong xi lanh, thực hiện lên khí một công 250 J. Trong quá trình "
              "nén, khí toả ra môi trường nhiệt lượng 80 J. Nội năng của khí tăng hay giảm và biến thiên "
              "bao nhiêu?",
              [("num", ("1.", "Vật khảo sát là lượng khí. Khí bị nén ⇒ khí NHẬN công ⇒ A = +250 J.")),
               ("num", ("2.", "Khí TOẢ nhiệt ra môi trường ⇒ Q = −80 J.")),
               ("num", ("3.", "Định luật I:  ΔU = A + Q = 250 + (−80) = +170 J.")),
               ("p", "ΔU > 0 nên nội năng khí tăng; với khí lí tưởng điều đó kéo theo nhiệt độ tăng.")],
              "ΔU = +170 J — nội năng tăng 170 J",
              tip="Sai lầm điển hình: cộng 250 + 80 = 330 J vì quên rằng toả nhiệt ứng với Q mang dấu âm.",
              sub="Bài 2 — Định luật I")

    d.example("Ví dụ 2 — Khí giãn nở đẳng nhiệt",
              "Một lượng khí lí tưởng giãn nở ở nhiệt độ không đổi và sinh ra công 400 J. Hỏi trong quá "
              "trình đó khí thu hay toả nhiệt, và nhiệt lượng bằng bao nhiêu?",
              [("num", ("1.", "Đẳng nhiệt ⇒ nhiệt độ không đổi ⇒ với khí lí tưởng thì ΔU = 0.")),
               ("num", ("2.", "Khí SINH công 400 J ⇒ A = −400 J.")),
               ("num", ("3.", "Từ ΔU = A + Q ⇒ 0 = −400 + Q ⇒ Q = +400 J.")),
               ("p", "Q > 0 nên khí THU nhiệt 400 J; toàn bộ nhiệt lượng này chuyển thành công.")],
              "Khí thu nhiệt, Q = +400 J",
              tip="Chỉ được viết ΔU = 0 khi khí là khí LÍ TƯỞNG và quá trình là đẳng nhiệt.",
              sub="Bài 2 — Định luật I")

    d.quiz("Kiểm tra nhanh",
           "Khí trong một bình kín có thành cứng được đun nóng. Kết luận nào đúng?",
           ["A = 0 và ΔU = Q.", "Q = 0 và ΔU = A.",
            "ΔU = 0 vì bình kín.", "A > 0 vì khí nở ra."],
           "A",
           "Thành bình cứng nên thể tích không đổi, khí không nhận và cũng không sinh công: A = 0. "
           "Định luật I rút gọn thành ΔU = Q. Khí không nở được nên phương án cuối sai; bình kín chỉ "
           "ngăn khí thoát ra chứ không ngăn nội năng thay đổi.")

    d.media("Mô phỏng và thí nghiệm nên dùng",
            [("Energy Forms and Changes", "PhET – phet.colorado.edu",
              "Theo dõi dòng năng lượng khi đun, cọ xát, truyền nhiệt giữa các vật.",
              "Năng lượng không mất đi mà chuyển từ dạng này sang dạng khác."),
             ("Nén nhanh bơm xe đã bịt đầu ra", "Thí nghiệm 30 giây tại lớp",
              "Bịt kín đầu bơm xe đạp, nén nhanh vài lần rồi cho học sinh sờ thân bơm.",
              "Thân bơm nóng lên rõ rệt: công nén đã chuyển thành nội năng của khí."),
             ("Xịt nhanh bình gas mini", "Quan sát tại lớp (có giám sát)",
              "Xịt liên tục vài giây, sờ vào vỏ bình.",
              "Vỏ bình lạnh đi vì khí giãn nở sinh công, nội năng giảm.")],
            lead="Hai thí nghiệm cuối cho thấy trực tiếp mối liên hệ giữa công và nội năng.")

    d.wrapup("Tổng kết buổi 2",
             [("head", "Ba ý phải nhớ"),
              ("b", "Nội năng phụ thuộc nhiệt độ và thể tích, không phụ thuộc chuyển động của cả vật."),
              ("b", "ΔU = A + Q; mọi dấu đều xét theo vật đang khảo sát, mũi tên vào vật là dương."),
              ("b", "Đẳng tích ⇒ ΔU = Q; đoạn nhiệt ⇒ ΔU = A; đẳng nhiệt (khí lí tưởng) ⇒ Q = −A.")],
             todo=["Làm Đề 2 – Chương 1.",
                   "Học thuộc quy ước dấu và tự đặt 2 ví dụ cho mỗi trường hợp.",
                   "Đọc trước bài Thang nhiệt độ."])


# =====================================================================  BUỔI 3
def buoi3(d):
    d.title_slide(
        sub="Buổi 3 — Nhiệt độ, thang nhiệt độ và nhiệt kế",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Hiểu nhiệt độ là thước đo của động năng trung bình phân tử",
                "Chuyển đổi thành thạo giữa thang Celsius và thang Kelvin",
                "Giải được bài toán xây dựng thang đo của một nhiệt kế bất kì"])

    d.section(1, "Nhiệt độ và cân bằng nhiệt", "Vì sao cần định nghĩa nhiệt độ một cách vật lí",
              items=["Nhiệt độ đo cái gì", "Cân bằng nhiệt", "Nguyên lí hoạt động của nhiệt kế"])

    d.content("Nhiệt độ đo cái gì?",
              [("head", "Định nghĩa vật lí"),
               ("p", "Nhiệt độ là đại lượng đặc trưng cho mức độ chuyển động nhiệt của các phân tử; "
                     "nó tỉ lệ thuận với động năng tịnh tiến trung bình của phân tử."),
               ("fx", r"\overline{W}_{\mathrm{d}} = \frac{3}{2}kT"),
               ("sub", "k = 1,38·10⁻²³ J/K là hằng số Boltzmann; T tính bằng kelvin."),
               ("gap", 0.06),
               ("head", "Cân bằng nhiệt"),
               ("b", "Hai vật tiếp xúc nhau: nhiệt truyền từ vật có nhiệt độ CAO sang vật có nhiệt độ THẤP."),
               ("b", "Quá trình dừng khi hai vật có cùng nhiệt độ — khi đó ta nói chúng ở trạng thái "
                     "cân bằng nhiệt."),
               ("note", "Nhiệt truyền theo chênh lệch NHIỆT ĐỘ, không theo nhiệt lượng hay khối lượng. "
                        "Một cốc nước 90 °C vẫn truyền nhiệt cho cả bể nước 30 °C dù nội năng của bể lớn hơn nhiều.")],
              sub="Bài 3 — Nhiệt độ", tag="TRỌNG TÂM")

    d.figure("Hai thang nhiệt độ trong chương trình", "n_sd_thang",
             items=[("head", "Thang Celsius"),
                    ("sub", "0 °C: nước đá đang tan;  100 °C: nước đang sôi (ở áp suất 1 atm)."),
                    ("head", "Thang Kelvin (thang nhiệt độ tuyệt đối)"),
                    ("sub", "0 K = −273,15 °C là độ không tuyệt đối — nhiệt độ thấp nhất về nguyên tắc."),
                    ("sub", "Một độ chia của hai thang có ĐỘ LỚN BẰNG NHAU: ΔT(K) = Δt(°C)."),
                    ("fx", r"T(\mathrm{K}) = t(^{\circ}\mathrm{C}) + 273"),
                    ("note", "Trong mọi công thức chất khí, T buộc phải tính bằng kelvin. "
                             "Nhưng ĐỘ BIẾN THIÊN nhiệt độ thì dùng °C hay K đều cho cùng một số.")],
             cap="Đối chiếu thang Celsius và thang Kelvin", tag="TRỌNG TÂM", figw=4.6, side="left")

    d.content("Nhiệt kế hoạt động dựa trên nguyên tắc nào?",
              [("head", "Nguyên tắc chung"),
               ("p", "Chọn một đại lượng vật lí biến đổi ĐƠN ĐIỆU theo nhiệt độ, đo đại lượng đó rồi "
                     "quy ra nhiệt độ."),
               ("gap", 0.06),
               ("head", "Các loại thường gặp"),
               ("kv", ("Nhiệt kế chất lỏng", "dựa vào sự nở vì nhiệt của thuỷ ngân hoặc rượu.")),
               ("kv", ("Nhiệt kế điện trở", "dựa vào sự thay đổi điện trở của kim loại theo nhiệt độ.")),
               ("kv", ("Cặp nhiệt điện", "dựa vào suất điện động nhiệt điện ở mối hàn hai kim loại khác nhau.")),
               ("kv", ("Nhiệt kế hồng ngoại", "đo bức xạ nhiệt phát ra, không cần tiếp xúc.")),
               ("note", "Muốn đo chính xác, nhiệt kế phải đạt CÂN BẰNG NHIỆT với vật cần đo. "
                        "Đó là lí do phải giữ nhiệt kế đủ lâu trước khi đọc.")],
              sub="Bài 3 — Nhiệt kế", tag="THỰC TIỄN")

    d.example("Ví dụ 1 — Xây dựng thang đo cho một nhiệt kế lạ",
              "Một nhiệt kế X có số chỉ tỉ lệ bậc nhất với nhiệt độ Celsius. Khi nhúng vào nước đá đang "
              "tan nó chỉ −10 °X, khi nhúng vào hơi nước đang sôi nó chỉ 140 °X. Hỏi khi nhiệt kế X "
              "chỉ 50 °X thì nhiệt độ Celsius là bao nhiêu?",
              [("num", ("1.", "Quan hệ bậc nhất nên hai thang tỉ lệ theo cùng một cách chia đoạn.")),
               ("num", ("2.", "Thang X có 140 − (−10) = 150 độ chia ứng với 100 độ chia của thang Celsius.")),
               ("num", ("3.", "Lập tỉ lệ:  (x − (−10)) / 150 = (t − 0) / 100.")),
               ("num", ("4.", "Thay x = 50:  60/150 = t/100 ⇒ t = 40 °C."))],
              "t = 40 °C",
              fig="n_dt_hainhietke", cap="Quan hệ bậc nhất giữa hai thang",
              tip="Đừng học thuộc công thức riêng cho từng đề. Chỉ cần nhớ: luôn lập tỉ lệ giữa "
                  "khoảng cách tới MỘC DƯỚI và TỔNG số độ chia của mỗi thang.",
              sub="Bài 3 — Nhiệt kế")

    d.example("Ví dụ 2 — Đổi thang và độ biến thiên",
              "Một khối khí được làm nóng từ 27 °C lên 87 °C. Hãy tính: (a) nhiệt độ đầu và cuối theo "
              "kelvin; (b) độ tăng nhiệt độ theo °C và theo K; (c) tỉ số nhiệt độ tuyệt đối cuối / đầu.",
              [("num", ("a.", "T₁ = 27 + 273 = 300 K;  T₂ = 87 + 273 = 360 K.")),
               ("num", ("b.", "Δt = 87 − 27 = 60 °C;  ΔT = 360 − 300 = 60 K. Hai số bằng nhau.")),
               ("num", ("c.", "T₂/T₁ = 360/300 = 1,2 — khí nóng lên 20 % theo thang tuyệt đối.")),
               ("note", "Nếu lấy tỉ số theo Celsius sẽ ra 87/27 ≈ 3,2 — hoàn toàn sai. "
                        "Tỉ số chỉ có ý nghĩa vật lí trên thang Kelvin.")],
              "T₁ = 300 K, T₂ = 360 K;  ΔT = 60 K;  T₂/T₁ = 1,2",
              sub="Bài 3 — Nhiệt kế")

    d.quiz("Kiểm tra nhanh",
           "Nhiệt độ của một vật tăng thêm 25 °C thì theo thang Kelvin nhiệt độ đó tăng thêm bao nhiêu?",
           ["25 K.", "298 K.", "248 K.", "Không xác định được nếu chưa biết nhiệt độ ban đầu."],
           "A",
           "Một độ chia của thang Kelvin bằng đúng một độ chia của thang Celsius, nên ĐỘ BIẾN THIÊN "
           "nhiệt độ tính theo hai thang là như nhau. Việc cộng 273 chỉ cần khi đổi GIÁ TRỊ nhiệt độ, "
           "không dùng cho độ biến thiên.")

    d.media("Mô phỏng và thí nghiệm nên dùng",
            [("States of Matter", "PhET – phet.colorado.edu",
              "Kéo thanh nhiệt độ và quan sát đồng thời nhiệt kế lẫn chuyển động phân tử.",
              "Nhiệt độ càng cao thì phân tử chuyển động càng nhanh — đúng như công thức W̄ₐ = 3/2·kT."),
             ("Đo nhiệt độ cơ thể bằng ba loại nhiệt kế", "Thí nghiệm tại lớp",
              "Dùng nhiệt kế thuỷ ngân, nhiệt kế điện tử và nhiệt kế hồng ngoại trên cùng một người.",
              "Ba kết quả lệch nhau vài phần mười độ — dẫn vào khái niệm sai số của phép đo."),
             ("Nhiệt kế tự chế bằng chai nước và ống hút", "Làm tại nhà",
              "Chai nước màu đậy kín, cắm ống hút xuyên nắp; hơ ấm chai và quan sát mực nước dâng.",
              "Mực chất lỏng dâng lên khi nóng — chính là nguyên tắc của nhiệt kế chất lỏng.")])

    d.wrapup("Tổng kết buổi 3",
             [("head", "Ba ý phải nhớ"),
              ("b", "Nhiệt độ đo động năng trung bình của phân tử, không đo nội năng."),
              ("b", "T(K) = t(°C) + 273; nhưng ΔT(K) = Δt(°C)."),
              ("b", "Bài toán nhiệt kế lạ chỉ cần lập tỉ lệ giữa hai thang, không cần công thức riêng.")],
             todo=["Làm Đề 3 – Chương 1.",
                   "Tự ra một bài nhiệt kế lạ rồi đổi cho bạn cùng bàn giải.",
                   "Đọc trước bài Nhiệt dung riêng."])


# =====================================================================  BUỔI 4
def buoi4(d):
    d.title_slide(
        sub="Buổi 4 — Nhiệt dung riêng, nhiệt nóng chảy riêng, nhiệt hoá hơi riêng",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Phát biểu và vận dụng được ba công thức Q = mcΔT, Q = mλ, Q = mL",
                "Nêu được ý nghĩa vật lí và đơn vị của c, λ, L",
                "Trình bày được phương án thí nghiệm đo nhiệt dung riêng của nước"])

    d.section(1, "Ba đại lượng, ba công thức", "Mỗi công thức ứng với một loại quá trình khác nhau",
              items=["Nhiệt dung riêng c", "Nhiệt nóng chảy riêng λ",
                     "Nhiệt hoá hơi riêng L", "Chọn đúng công thức"])

    d.formulas("Ba công thức nền tảng của chương",
               [(r"Q = mc\,\Delta T",
                 "Vật NÓNG LÊN hoặc NGUỘI ĐI mà không đổi thể — c là nhiệt dung riêng, J/(kg·K)."),
                (r"Q = m\lambda",
                 "Vật đang NÓNG CHẢY (hoặc đông đặc) ở nhiệt độ nóng chảy — λ là nhiệt nóng chảy riêng, J/kg."),
                (r"Q = mL",
                 "Vật đang HOÁ HƠI (hoặc ngưng tụ) ở nhiệt độ sôi — L là nhiệt hoá hơi riêng, J/kg.")],
               lead="Câu hỏi đầu tiên khi gặp bài tập: trong giai đoạn này nhiệt độ CÓ đổi hay KHÔNG đổi?",
               foot="Nhiệt độ đổi ⇒ dùng mcΔT.  Nhiệt độ không đổi mà đang chuyển thể ⇒ dùng mλ hoặc mL.",
               tag="TRỌNG TÂM", sub="Bài 4 – 6")

    d.content("Ý nghĩa vật lí của ba đại lượng",
              [("kv", ("c", "nhiệt lượng cần cung cấp cho 1 kg chất để nhiệt độ tăng thêm 1 K. "
                            "Nước có c = 4200 J/(kg·K) — thuộc loại lớn nhất trong các chất thông thường.")),
               ("kv", ("λ", "nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn 1 kg chất "
                            "ĐANG Ở nhiệt độ nóng chảy. Nước đá: λ = 3,4·10⁵ J/kg.")),
               ("kv", ("L", "nhiệt lượng cần cung cấp để làm hoá hơi hoàn toàn 1 kg chất lỏng "
                            "ĐANG Ở nhiệt độ sôi. Nước: L = 2,26·10⁶ J/kg.")),
               ("rule", None),
               ("head", "Vì sao nước có nhiệt dung riêng lớn lại quan trọng?"),
               ("b", "Nước biển giữ cho khí hậu vùng ven biển điều hoà, ngày không quá nóng, đêm không quá lạnh."),
               ("b", "Nước được dùng làm chất tải nhiệt trong động cơ ô tô và nhà máy điện."),
               ("note", "λ và L luôn kèm điều kiện “đang ở đúng nhiệt độ chuyển thể”. "
                        "Nước đá ở −10 °C thì phải làm ấm lên 0 °C trước, rồi mới nói tới λ.")],
              sub="Bài 4 – 6", tag="Ý NGHĨA")

    d.table("Bảng hằng số dùng thống nhất trong cả khoá",
            ["Chất", "c (J/kg·K)", "λ (J/kg)", "L (J/kg)", "Nhiệt độ chuyển thể"],
            [["Nước", "4 200", "—", "2,26·10⁶", "sôi ở 100 °C"],
             ["Nước đá", "2 100", "3,4·10⁵", "—", "nóng chảy ở 0 °C"],
             ["Nhôm", "880", "3,9·10⁵", "—", "nóng chảy ở 660 °C"],
             ["Sắt", "460", "2,7·10⁵", "—", "nóng chảy ở 1538 °C"],
             ["Đồng", "380", "1,8·10⁵", "—", "nóng chảy ở 1083 °C"],
             ["Chì", "130", "0,25·10⁵", "—", "nóng chảy ở 327 °C"]],
            widths=[1.1, 1.0, 1.0, 1.0, 1.3], tag="TRA CỨU",
            foot="Quy luật đáng nhớ: kim loại càng nặng thì nhiệt dung riêng càng nhỏ. "
                 "Vì vậy cùng khối lượng và cùng nhiệt lượng, chì nóng lên nhanh hơn nhôm rất nhiều.")

    d.figure("Đọc đồ thị Q – ΔT để so sánh nhiệt dung riêng", "n_dt_QdT",
             items=[("head", "Ý tưởng"),
                    ("b", "Từ Q = mcΔT suy ra đồ thị Q theo ΔT là đường thẳng qua gốc, hệ số góc bằng m·c."),
                    ("b", "Hai mẫu có cùng khối lượng: mẫu nào dốc hơn thì nhiệt dung riêng lớn hơn."),
                    ("gap", 0.05),
                    ("head", "Trên đồ thị"),
                    ("sub", "Chất X dốc hơn chất Y ⇒ c của X lớn hơn c của Y."),
                    ("note", "Nếu đề cho hai mẫu KHÁC khối lượng thì hệ số góc là tích m·c, "
                             "phải chia cho m rồi mới so sánh c.")],
             cap="Nhiệt lượng cung cấp theo độ tăng nhiệt độ của hai chất", tag="ĐỒ THỊ", figw=5.8)

    d.figure("Đồ thị đun ba chất bằng cùng một bếp", "n_dt_batchat",
             items=[("head", "Cách suy luận"),
                    ("b", "Cùng một bếp ⇒ trong cùng thời gian, ba chất nhận CÙNG một nhiệt lượng."),
                    ("b", "Q = mcΔT không đổi ⇒ chất nào ΔT lớn hơn thì tích m·c nhỏ hơn."),
                    ("sub", "Đường (1) dốc nhất ⇒ m·c nhỏ nhất."),
                    ("sub", "Đường (3) thoải nhất ⇒ m·c lớn nhất."),
                    ("note", "Chỉ khi ba mẫu cùng khối lượng mới kết luận trực tiếp được về c.")],
             cap="Nhiệt độ theo thời gian của ba chất được đun cùng công suất",
             tag="ĐỒ THỊ", figw=5.8, side="left")

    d.figure("Phương án thí nghiệm đo nhiệt dung riêng của nước", "n_sd_tn_do_c",
             items=[("head", "Bốn bước"),
                    ("num", ("①", "Cân để biết khối lượng nước m.")),
                    ("num", ("②", "Đọc hiệu điện thế U và cường độ dòng điện I; bấm giờ đo thời gian t.")),
                    ("num", ("③", "Đọc độ tăng nhiệt độ ΔT trên nhiệt kế.")),
                    ("num", ("④", "Tính c = UIt / (m·ΔT).")),
                    ("note", "Nguồn sai số chính: nhiệt toả ra môi trường và nhiệt mà bình thu vào — "
                             "cả hai đều làm giá trị c đo được LỚN hơn giá trị thực.")],
             cap="Bố trí thí nghiệm đo nhiệt dung riêng", tag="THỰC HÀNH", figw=5.5)

    d.example("Ví dụ — Bài toán nhiều giai đoạn",
              "Tính nhiệt lượng cần cung cấp để biến 0,50 kg nước đá ở −20 °C thành nước ở 40 °C. "
              "Cho c(nước đá) = 2100 J/(kg·K), λ = 3,4·10⁵ J/kg, c(nước) = 4200 J/(kg·K).",
              [("num", ("1.", "Làm ấm nước đá từ −20 °C lên 0 °C:  Q₁ = 0,50·2100·20 = 21 000 J.")),
               ("num", ("2.", "Làm nóng chảy hoàn toàn nước đá ở 0 °C:  Q₂ = 0,50·3,4·10⁵ = 170 000 J.")),
               ("num", ("3.", "Làm nóng nước từ 0 °C lên 40 °C:  Q₃ = 0,50·4200·40 = 84 000 J.")),
               ("num", ("4.", "Cộng lại:  Q = 21 000 + 170 000 + 84 000 = 275 000 J = 275 kJ."))],
              "Q = 275 kJ",
              tip="Luôn tách bài toán thành các GIAI ĐOẠN theo đồ thị nhiệt độ – thời gian. "
                  "Giai đoạn nghiêng dùng mcΔT, giai đoạn ngang dùng mλ hoặc mL. "
                  "Bỏ sót giai đoạn 2 là lỗi phổ biến nhất.",
              sub="Bài 4 – 6")

    d.quiz("Kiểm tra nhanh",
           "Cùng cung cấp 10 kJ cho 1 kg nước và 1 kg nhôm (c(nước) = 4200, c(nhôm) = 880 J/kg·K). "
           "So sánh độ tăng nhiệt độ của hai vật.",
           ["Nước tăng nhiều hơn nhôm.", "Nhôm tăng nhiều hơn nước, khoảng 4,8 lần.",
            "Hai vật tăng như nhau.", "Không so sánh được vì chưa biết nhiệt độ ban đầu."],
           "B",
           "Từ ΔT = Q/(mc), cùng Q và cùng m thì ΔT tỉ lệ nghịch với c. "
           "ΔT(nhôm)/ΔT(nước) = 4200/880 ≈ 4,8. Nhiệt độ ban đầu không ảnh hưởng vì công thức "
           "chỉ liên quan tới độ biến thiên.")

    d.wrapup("Tổng kết buổi 4",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Nhiệt độ đổi ⇒ Q = mcΔT.  Nhiệt độ không đổi mà chuyển thể ⇒ Q = mλ hoặc Q = mL."),
              ("b", "λ và L chỉ dùng khi chất ĐANG Ở đúng nhiệt độ chuyển thể."),
              ("b", "Đồ thị Q–ΔT: hệ số góc bằng m·c."),
              ("b", "Bài toán nhiều giai đoạn: tách theo đồ thị rồi cộng nhiệt lượng từng giai đoạn.")],
             todo=["Làm Đề 4 và Đề 5 – Chương 1.",
                   "Học thuộc bảng hằng số c, λ, L.",
                   "Viết lại lời giải ví dụ nhiều giai đoạn bằng ngôn ngữ của mình."])


# =====================================================================  BUỔI 5
def buoi5(d):
    d.title_slide(
        sub="Buổi 5 — Luyện tập tổng hợp: cân bằng nhiệt, hiệu suất và bài toán đồ thị",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Thành thạo phương trình cân bằng nhiệt và cách kiểm tra kết quả",
                "Giải được bài toán hiệu suất của quá trình đun nóng",
                "Nhận dạng nhanh các kiểu câu hỏi thường gặp trong đề thi"])

    d.section(1, "Phương trình cân bằng nhiệt", "Dạng bài chiếm tỉ trọng lớn nhất của Chương I",
              items=["Nguyên tắc", "Kiểm tra kết quả", "Bài toán có chuyển thể"])

    d.figure("Phương trình cân bằng nhiệt", "n_sd_can_bang_nhiet",
             items=[("head", "Ba bước chuẩn"),
                    ("num", ("1.", "Xác định vật nào TOẢ nhiệt, vật nào THU nhiệt.")),
                    ("num", ("2.", "Viết Q(toả) = Q(thu), mỗi vế là tổng nhiệt lượng của vật đó.")),
                    ("num", ("3.", "Giải phương trình rồi KIỂM TRA: nhiệt độ cân bằng phải nằm giữa "
                                   "hai nhiệt độ ban đầu.")),
                    ("note", "Trong mọi biểu thức, hãy viết hiệu nhiệt độ sao cho luôn DƯƠNG: "
                             "vật toả lấy (t(đầu) − t), vật thu lấy (t − t(đầu)).")],
             cap="Trao đổi nhiệt trong bình cách nhiệt", tag="TRỌNG TÂM", figw=5.9)

    d.example("Ví dụ 1 — Cân bằng nhiệt cơ bản",
              "Thả một miếng đồng khối lượng 0,40 kg ở 100 °C vào 1,0 kg nước ở 20 °C đựng trong bình "
              "cách nhiệt. Tính nhiệt độ khi cân bằng. Cho c(đồng) = 380, c(nước) = 4200 J/(kg·K); "
              "bỏ qua nhiệt lượng mà bình thu vào.",
              [("num", ("1.", "Đồng nóng hơn nên đồng toả nhiệt, nước thu nhiệt.")),
               ("num", ("2.", "Q(toả) = 0,40·380·(100 − t);  Q(thu) = 1,0·4200·(t − 20).")),
               ("num", ("3.", "152·(100 − t) = 4200·(t − 20) ⇒ 15 200 − 152t = 4200t − 84 000.")),
               ("num", ("4.", "4352t = 99 200 ⇒ t ≈ 22,8 °C.")),
               ("p", "Kiểm tra: 20 °C < 22,8 °C < 100 °C — hợp lí. Nước gần như không nóng lên "
                     "vì nhiệt dung riêng của nước lớn hơn đồng hơn 11 lần.")],
              "t ≈ 22,8 °C",
              tip="Nếu kết quả ra ngoài khoảng [20; 100] thì chắc chắn đã sai dấu ở một vế. "
                  "Hãy kiểm tra ngay trước khi tô đáp án.",
              sub="Bài 7 — Luyện tập")

    d.example("Ví dụ 2 — Cân bằng nhiệt có chuyển thể (bẫy kinh điển)",
              "Thả 0,10 kg nước đá ở 0 °C vào 0,50 kg nước ở 30 °C trong bình cách nhiệt. "
              "Tính nhiệt độ cân bằng. Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
              [("num", ("1.", "Trước hết phải KIỂM TRA nước đá có tan hết hay không.")),
               ("num", ("2.", "Nhiệt cần để tan hết đá:  Q(cần) = 0,10·3,4·10⁵ = 34 000 J.")),
               ("num", ("3.", "Nhiệt tối đa nước có thể nhả khi hạ về 0 °C:  "
                              "Q(có) = 0,50·4200·30 = 63 000 J.")),
               ("num", ("4.", "Q(có) > Q(cần) nên đá tan hết, còn dư nhiệt làm nóng cả khối nước.")),
               ("num", ("5.", "0,50·4200·(30 − t) = 34 000 + 0,10·4200·(t − 0)")),
               ("num", ("6.", "63 000 − 2100t = 34 000 + 420t ⇒ 2520t = 29 000 ⇒ t ≈ 11,5 °C."))],
              "t ≈ 11,5 °C  (nước đá tan hết)",
              tip="Nếu Q(có) < Q(cần) thì đá chỉ tan MỘT PHẦN và nhiệt độ cân bằng đúng bằng 0 °C. "
                  "Bỏ qua bước kiểm tra này là lỗi mất điểm phổ biến nhất của cả chương.",
              sub="Bài 7 — Luyện tập")

    d.section(2, "Hiệu suất và bài toán thực tiễn", "Khi không thể bỏ qua hao phí",
              items=["Định nghĩa hiệu suất", "Bẫy nhân – chia", "Bài toán bình nước nóng"])

    d.figure("Hiệu suất của quá trình đun nóng", "n_sd_hieu_suat",
             items=[("head", "Định nghĩa"),
                    ("p", "Hiệu suất H là tỉ số giữa nhiệt lượng CÓ ÍCH và nhiệt lượng TOÀN PHẦN "
                          "mà nguồn cung cấp."),
                    ("b", "Q có ích là phần thực sự làm vật cần đun nóng lên hoặc chuyển thể."),
                    ("b", "Q toàn phần là phần năng lượng nguồn bỏ ra (điện năng, nhiệt do nhiên liệu cháy…)."),
                    ("note", "Đề cho H rồi hỏi năng lượng nguồn phải cung cấp ⇒ CHIA cho H. "
                             "Nhân với H là sai — đó là bẫy được cài rất thường xuyên.")],
             cap="Dòng năng lượng trong quá trình đun nóng", tag="TRỌNG TÂM", figw=6.1, side="left")

    d.example("Ví dụ 3 — Ấm điện và hiệu suất",
              "Một ấm điện công suất 1500 W dùng để đun 2,0 kg nước từ 25 °C đến khi sôi. "
              "Hiệu suất của ấm là 80 %. Tính thời gian đun. Cho c(nước) = 4200 J/(kg·K).",
              [("num", ("1.", "Nhiệt lượng CÓ ÍCH:  Q(có ích) = 2,0·4200·(100 − 25) = 630 000 J.")),
               ("num", ("2.", "Nhiệt lượng TOÀN PHẦN:  Q(toàn phần) = Q(có ích) / H = 630 000 / 0,80 = 787 500 J.")),
               ("num", ("3.", "Thời gian:  t = Q(toàn phần) / P = 787 500 / 1500 = 525 s ≈ 8 phút 45 giây.")),
               ("note", "Nếu nhân 630 000 × 0,80 rồi chia cho 1500 sẽ ra 336 s — đúng là một trong bốn "
                        "phương án nhiễu thường gặp.")],
              "t = 525 s ≈ 8 phút 45 giây",
              sub="Bài 7 — Luyện tập")

    d.table("Bốn dạng câu hỏi thường gặp của Chương I",
            ["Dạng", "Dấu hiệu nhận biết", "Cách xử lí"],
            [["Nhiều giai đoạn", "Có chuyển thể, đề cho cả c và λ (hoặc L)",
              "Tách giai đoạn theo đồ thị, cộng nhiệt lượng"],
             ["Cân bằng nhiệt", "Thả vật này vào vật kia, bình cách nhiệt",
              "Q(toả) = Q(thu); kiểm tra t nằm giữa hai nhiệt độ đầu"],
             ["Có chuyển thể ẩn", "Thả nước đá vào nước",
              "So sánh Q(có) với Q(cần) trước khi lập phương trình"],
             ["Hiệu suất", "Đề nhắc công suất, hao phí, phần trăm",
              "Xác định rõ đâu là Q có ích; chia cho H, không nhân"]],
            widths=[1.0, 1.7, 1.8], tag="PHÂN DẠNG",
            foot="Trong đề thi tốt nghiệp, ba dạng đầu thường xuất hiện ở Phần I và Phần III; "
                 "dạng hiệu suất hay được cài trong câu đúng/sai của Phần II.")

    d.quiz("Kiểm tra nhanh",
           "Thả 0,30 kg nước đá ở 0 °C vào 0,20 kg nước ở 20 °C trong bình cách nhiệt. "
           "Nhiệt độ cân bằng là bao nhiêu? (λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/kg·K)",
           ["0 °C, nước đá chỉ tan một phần.", "Khoảng 8 °C.",
            "Khoảng 12 °C.", "0 °C, toàn bộ nước đóng băng hết."],
           "A",
           "Nhiệt cần để tan hết 0,30 kg đá là 0,30·3,4·10⁵ = 102 000 J, trong khi nước chỉ nhả được "
           "tối đa 0,20·4200·20 = 16 800 J. Nhiệt nhả ra ít hơn nhiều nên đá chỉ tan một phần "
           "và hỗn hợp dừng ở 0 °C. Nước cũng không đóng băng hết vì nước đá ở đúng 0 °C "
           "không thể nhận thêm nhiệt mà vẫn ở 0 °C.")

    d.wrapup("Tổng kết Chương I",
             [("head", "Bản đồ kiến thức cả chương"),
              ("b", "Mô hình động học phân tử → giải thích ba thể và sự chuyển thể."),
              ("b", "Nội năng và định luật I: ΔU = A + Q."),
              ("b", "Nhiệt độ, thang Kelvin và nhiệt kế."),
              ("b", "Ba công thức Q = mcΔT, Q = mλ, Q = mL."),
              ("b", "Phương trình cân bằng nhiệt và hiệu suất.")],
             todo=["Làm trọn bộ 10 đề Chương 1 theo thứ tự.",
                   "Ghi lại mọi câu sai vào sổ lỗi, phân loại theo 4 dạng.",
                   "Chuẩn bị Chương II: ôn lại cách đổi đơn vị áp suất và thể tích."])


SPEC = [
    dict(file="C01_Buoi1_Cau_truc_cua_chat_va_su_chuyen_the.pptx",
         title="Cấu trúc của chất. Sự chuyển thể",
         chapter=CH + " • Buổi 1", th=TH, slides=buoi1),
    dict(file="C01_Buoi2_Noi_nang_va_dinh_luat_I.pptx",
         title="Nội năng. Định luật I của nhiệt động lực học",
         chapter=CH + " • Buổi 2", th=TH, slides=buoi2),
    dict(file="C01_Buoi3_Thang_nhiet_do_va_nhiet_ke.pptx",
         title="Nhiệt độ. Thang nhiệt độ và nhiệt kế",
         chapter=CH + " • Buổi 3", th=TH, slides=buoi3),
    dict(file="C01_Buoi4_Nhiet_dung_rieng_nong_chay_hoa_hoi.pptx",
         title="Nhiệt dung riêng. Nhiệt nóng chảy riêng. Nhiệt hoá hơi riêng",
         chapter=CH + " • Buổi 4", th=TH, slides=buoi4),
    dict(file="C01_Buoi5_Luyen_tap_tong_hop_chuong_I.pptx",
         title="Luyện tập tổng hợp Chương I",
         chapter=CH + " • Buổi 5", th=TH, slides=buoi5),
]
