# -*- coding: utf-8 -*-
"""SLIDE BÀI GIẢNG — CHƯƠNG II: KHÍ LÍ TƯỞNG.  Năm buổi dạy."""
from deck import Deck

TH = 2
CH = "Chương II – Khí lí tưởng"
MT = "Ôn thi tốt nghiệp THPT 2026  •  Lớp 12"


# =====================================================================  BUỔI 1
def buoi1(d):
    d.title_slide(
        sub="Buổi 1 — Mô hình động học phân tử chất khí. Chuyển động Brown. Khí lí tưởng",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được các giả thiết của mô hình động học phân tử chất khí",
                "Giải thích được nguồn gốc của áp suất chất khí",
                "Nêu được điều kiện để một chất khí coi là khí lí tưởng"])

    d.section(1, "Chuyển động của phân tử khí", "Bằng chứng thực nghiệm và mô hình lí thuyết",
              items=["Chuyển động Brown", "Bốn giả thiết của mô hình", "Khí lí tưởng là gì"])

    d.figure("Chuyển động Brown — bằng chứng đầu tiên", "k_sd_brown",
             items=[("head", "Quan sát của Robert Brown (1827)"),
                    ("b", "Hạt phấn hoa lơ lửng trong nước chuyển động gấp khúc, hỗn loạn, không bao giờ dừng."),
                    ("b", "Nguyên nhân: các phân tử nước va chạm vào hạt từ mọi phía, số va chạm các "
                          "phía không cân bằng nhau nên hạt bị đẩy ngẫu nhiên."),
                    ("b", "Nhiệt độ càng cao, hạt càng chuyển động mạnh."),
                    ("note", "Đây là bằng chứng gián tiếp nhưng thuyết phục cho luận điểm “phân tử "
                             "chuyển động hỗn loạn không ngừng”.")],
             cap="Quỹ đạo gấp khúc của hạt phấn hoa trong nước", tag="THỰC NGHIỆM", figw=5.6,
             note="Nhấn mạnh: hạt phấn hoa KHÔNG phải phân tử — nó lớn hơn phân tử hàng nghìn lần. "
                  "Ta quan sát hạt để suy ra chuyển động của phân tử.")

    d.content("Mô hình động học phân tử chất khí",
              [("head", "Bốn giả thiết"),
               ("num", ("1.", "Chất khí gồm rất nhiều phân tử; kích thước mỗi phân tử RẤT NHỎ so với "
                              "khoảng cách giữa chúng, có thể coi là chất điểm.")),
               ("num", ("2.", "Các phân tử chuyển động hỗn loạn không ngừng theo mọi phương, "
                              "mọi hướng đều như nhau.")),
               ("num", ("3.", "Khi chưa va chạm, lực tương tác giữa các phân tử là không đáng kể.")),
               ("num", ("4.", "Va chạm giữa các phân tử với nhau và với thành bình là va chạm ĐÀN HỒI: "
                              "động năng được bảo toàn.")),
               ("rule", None),
               ("note", "Giả thiết 3 là điểm mấu chốt tách khí lí tưởng khỏi khí thực. "
                        "Nó đúng khi khí loãng — áp suất không quá lớn, nhiệt độ không quá thấp.")],
              sub="Bài 8 — Mô hình động học phân tử chất khí", tag="LÍ THUYẾT")

    d.figure("Áp suất chất khí sinh ra từ đâu?", "k_sd_vacham_thanh",
             items=[("head", "Cơ chế"),
                    ("b", "Mỗi phân tử đập vào thành bình rồi bật ra, truyền cho thành một xung lượng."),
                    ("b", "Số va chạm trong một giây là vô cùng lớn nên tổng lực tác dụng lên thành "
                          "ổn định — ta đo được nó dưới dạng ÁP SUẤT."),
                    ("gap", 0.05),
                    ("head", "Hai yếu tố quyết định áp suất"),
                    ("sub", "Mật độ phân tử càng lớn ⇒ càng nhiều va chạm ⇒ p càng lớn."),
                    ("sub", "Phân tử chuyển động càng nhanh (T càng cao) ⇒ mỗi va chạm càng mạnh ⇒ p càng lớn."),
                    ("note", "Đây là lí do bơm thêm khí vào săm xe (tăng mật độ) hoặc để xe ngoài nắng "
                             "(tăng nhiệt độ) đều làm áp suất tăng.")],
             cap="Va chạm phân tử lên thành bình", tag="TRỌNG TÂM", figw=5.7, side="left")

    d.content("Khí lí tưởng là gì?",
              [("head", "Định nghĩa"),
               ("p", "Khí lí tưởng là chất khí trong đó các phân tử được coi là chất điểm và chỉ "
                     "tương tác với nhau khi va chạm."),
               ("gap", 0.06),
               ("head", "Khi nào khí thực gần đúng là khí lí tưởng?"),
               ("b", "Áp suất không quá lớn — khoảng cách giữa các phân tử còn đủ xa."),
               ("b", "Nhiệt độ không quá thấp — chưa xảy ra hoá lỏng."),
               ("b", "Không khí, khí hiđrô, khí hêli ở điều kiện thường đều thoả mãn khá tốt."),
               ("gap", 0.06),
               ("head", "Vì sao cần khái niệm này?"),
               ("b", "Vì chỉ với khí lí tưởng, ba định luật chất khí và phương trình trạng thái mới "
                     "đúng chính xác. Toàn bộ Chương II được xây dựng trên khái niệm này."),
               ("note", "Bẫy hay gặp: “khí lí tưởng là khí không có khối lượng” hoặc “không va chạm” — "
                        "cả hai đều SAI. Phân tử vẫn có khối lượng và vẫn va chạm.")],
              sub="Bài 8 — Khí lí tưởng", tag="ĐỊNH NGHĨA")

    d.table("Ba thông số trạng thái và đơn vị",
            ["Thông số", "Kí hiệu", "Đơn vị SI", "Các đơn vị khác thường gặp"],
            [["Áp suất", "p", "pascal (Pa)", "1 atm = 1,013·10⁵ Pa;  1 bar = 10⁵ Pa;  1 mmHg = 133,3 Pa"],
             ["Thể tích", "V", "mét khối (m³)", "1 L = 1 dm³ = 10⁻³ m³;  1 cm³ = 10⁻⁶ m³"],
             ["Nhiệt độ", "T", "kelvin (K)", "T (K) = t (°C) + 273"]],
            widths=[0.9, 0.6, 1.0, 2.6], tag="ĐƠN VỊ",
            foot="Trong các định luật chất khí, p và V được phép giữ nguyên đơn vị miễn là HAI VẾ dùng "
                 "cùng đơn vị; riêng T thì BẮT BUỘC phải đổi sang kelvin.")

    d.figure("Nhiệt độ và tốc độ phân tử", "k_dt_phan_bo_toc_do",
             items=[("head", "Điều cần rút ra"),
                    ("b", "Ở cùng một nhiệt độ, các phân tử không có cùng tốc độ mà phân bố trên "
                          "một dải rộng."),
                    ("b", "Nhiệt độ tăng ⇒ đỉnh của đường phân bố dịch sang phải: tốc độ trung bình tăng."),
                    ("b", "Động năng tịnh tiến trung bình chỉ phụ thuộc nhiệt độ, không phụ thuộc "
                          "loại khí."),
                    ("note", "Hệ quả quan trọng: ở cùng nhiệt độ, phân tử nhẹ (H₂) chuyển động nhanh "
                             "hơn phân tử nặng (O₂), nhưng động năng trung bình của chúng bằng nhau.")],
             cap="Phân bố tốc độ phân tử ở ba nhiệt độ", tag="MỞ RỘNG", figw=5.9)

    d.quiz("Kiểm tra nhanh",
           "Phát biểu nào về khí lí tưởng là ĐÚNG?",
           ["Các phân tử khí lí tưởng không va chạm với nhau.",
            "Các phân tử được coi là chất điểm và chỉ tương tác khi va chạm.",
            "Khí lí tưởng không gây áp suất lên thành bình.",
            "Khí lí tưởng chỉ tồn tại ở nhiệt độ rất thấp."],
           "B",
           "Khí lí tưởng vẫn va chạm — chính va chạm tạo ra áp suất, nên hai phương án đầu và thứ ba "
           "đều sai. Khí thực càng gần khí lí tưởng khi nhiệt độ CAO và áp suất THẤP, "
           "ngược với phương án cuối.")

    d.media("Mô phỏng nên dùng cho buổi này",
            [("Gas Properties", "PhET – phet.colorado.edu",
              "Bơm thêm phân tử, thay đổi nhiệt độ và thể tích; áp kế hiển thị áp suất theo thời gian thực.",
              "Tăng số phân tử hoặc tăng nhiệt độ đều làm áp kế chỉ cao hơn."),
             ("Diffusion", "PhET – phet.colorado.edu",
              "Hai loại khí ban đầu ở hai ngăn, mở vách ngăn và quan sát quá trình khuếch tán.",
              "Phân tử nhẹ khuếch tán nhanh hơn phân tử nặng ở cùng nhiệt độ."),
             ("Bơm bóng bay rồi thả vào nước nóng / nước đá", "Thí nghiệm tại lớp",
              "Buộc kín quả bóng, nhúng lần lượt vào hai chậu nước.",
              "Bóng phồng lên trong nước nóng, xẹp lại trong nước đá — mở đường sang định luật chất khí.")])

    d.wrapup("Tổng kết buổi 1",
             [("head", "Ba ý phải nhớ"),
              ("b", "Chuyển động Brown là bằng chứng thực nghiệm cho chuyển động hỗn loạn của phân tử."),
              ("b", "Áp suất khí là kết quả của vô số va chạm phân tử lên thành bình."),
              ("b", "Khí lí tưởng: phân tử là chất điểm, chỉ tương tác khi va chạm.")],
             todo=["Làm Đề 1 – Chương 2.",
                   "Học thuộc bảng đổi đơn vị áp suất và thể tích.",
                   "Đọc trước ba định luật chất khí."])


# =====================================================================  BUỔI 2
def buoi2(d):
    d.title_slide(
        sub="Buổi 2 — Ba định luật chất khí: Boyle, Charles và Gay-Lussac",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Phát biểu và vận dụng được ba định luật chất khí",
                "Nhận dạng đúng quá trình đẳng nhiệt, đẳng áp, đẳng tích",
                "Đọc và vẽ được đồ thị của ba quá trình trên mọi hệ trục"])

    d.section(1, "Định luật Boyle", "Quá trình đẳng nhiệt: nhiệt độ không đổi",
              items=["Thí nghiệm", "Phát biểu và công thức", "Đồ thị trên ba hệ trục"])

    d.figure("Thí nghiệm khảo sát định luật Boyle", "k_sd_tn_boyle",
             items=[("head", "Cách tiến hành"),
                    ("num", ("1.", "Nhốt một lượng khí xác định trong xi lanh có thang chia thể tích.")),
                    ("num", ("2.", "Ép pit-tông thật CHẬM để nhiệt độ khí kịp cân bằng với môi trường.")),
                    ("num", ("3.", "Ghi lại các cặp giá trị (p, V).")),
                    ("num", ("4.", "Tính tích p·V cho từng cặp — kết quả gần như không đổi.")),
                    ("note", "Phải ép chậm, nếu nén nhanh khí sẽ nóng lên và quá trình không còn "
                             "là đẳng nhiệt nữa.")],
             cap="Bố trí thí nghiệm định luật Boyle", tag="THỰC HÀNH", figw=5.7)

    d.formulas("Định luật Boyle",
               [(r"pV = \mathrm{const}",
                 "Ở nhiệt độ không đổi, tích áp suất và thể tích của một lượng khí xác định là hằng số."),
                (r"p_1V_1 = p_2V_2",
                 "Dạng dùng để giải bài tập khi khí chuyển từ trạng thái 1 sang trạng thái 2."),
                (r"p \sim \frac{1}{V}",
                 "Áp suất tỉ lệ nghịch với thể tích: nén một nửa thể tích thì áp suất tăng gấp đôi.")],
               lead="Điều kiện áp dụng: LƯỢNG KHÍ KHÔNG ĐỔI và NHIỆT ĐỘ KHÔNG ĐỔI.",
               foot="Nếu đề nói khí thoát ra ngoài hoặc bơm thêm khí vào, định luật Boyle không còn "
                    "dùng trực tiếp được — phải dùng phương trình Clapeyron.",
               tag="TRỌNG TÂM", sub="Bài 9 — Định luật Boyle")

    d.split("Hai dạng đồ thị của quá trình đẳng nhiệt",
            left=[("p", "Đường đẳng nhiệt trong hệ (p, V) là một nhánh HYPEBOL."),
                  ("b", "Đường nằm càng xa gốc toạ độ ứng với nhiệt độ càng CAO."),
                  ("b", "Đường không bao giờ cắt trục — p không thể bằng 0 khi V hữu hạn.")],
            right=[("p", "Trong hệ (p, 1/V) đồ thị là ĐƯỜNG THẲNG qua gốc toạ độ."),
                   ("b", "Hệ số góc của đường thẳng chính bằng hằng số p·V."),
                   ("b", "Dạng này dùng để kiểm chứng định luật từ số liệu thí nghiệm.")],
            lhead="Hệ (p, V)", rhead="Hệ (p, 1/V)",
            sub="Bài 9 — Định luật Boyle", tag="ĐỒ THỊ")

    d.figure("Đồ thị đẳng nhiệt trong hệ (p, V)", "k_dt_dangnhiet",
             items=[("head", "Đọc đồ thị"),
                    ("b", "Mỗi đường hypebol ứng với MỘT nhiệt độ."),
                    ("b", "Đường T₂ nằm trên đường T₁ nên T₂ > T₁."),
                    ("note", "Cách kiểm tra nhanh: chọn cùng một giá trị V, đường nào cho p lớn hơn "
                             "thì nhiệt độ cao hơn.")],
             cap="Hai đường đẳng nhiệt ứng với hai nhiệt độ khác nhau",
             tag="ĐỒ THỊ", figw=5.5, side="left")

    d.section(2, "Định luật Charles và Gay-Lussac", "Quá trình đẳng áp và quá trình đẳng tích",
              items=["Định luật Charles (đẳng áp)", "Định luật Gay-Lussac (đẳng tích)",
                     "Độ không tuyệt đối"])

    d.formulas("Hai định luật còn lại",
               [(r"\frac{V_1}{T_1} = \frac{V_2}{T_2}",
                 "ĐỊNH LUẬT CHARLES — quá trình ĐẲNG ÁP: thể tích tỉ lệ thuận với nhiệt độ tuyệt đối."),
                (r"\frac{p_1}{T_1} = \frac{p_2}{T_2}",
                 "ĐỊNH LUẬT GAY-LUSSAC — quá trình ĐẲNG TÍCH: áp suất tỉ lệ thuận với nhiệt độ tuyệt đối.")],
               lead="Trong cả hai công thức, T BẮT BUỘC tính bằng kelvin. Đây là lỗi sai số một của chương.",
               foot="Cách nhớ tên: Charles giữ áp suất (Charles – áp), Gay-Lussac giữ thể tích. "
                    "Tuy nhiên đề thi thường chỉ gọi tên quá trình, không gọi tên nhà bác học.",
               tag="TRỌNG TÂM", sub="Bài 10 – 11")

    d.figure("Thí nghiệm đẳng áp và ý nghĩa của độ không tuyệt đối", "k_dt_charles",
             items=[("head", "Kết quả thí nghiệm"),
                    ("b", "Đồ thị V theo t (°C) là một đường thẳng."),
                    ("b", "Kéo dài đường thẳng về phía trái, nó cắt trục hoành tại khoảng −273 °C."),
                    ("gap", 0.05),
                    ("head", "Ý nghĩa"),
                    ("b", "Tại −273 °C thể tích ngoại suy bằng 0 — không thể có nhiệt độ thấp hơn."),
                    ("b", "Đó là lí do người ta đặt gốc của thang Kelvin tại điểm này."),
                    ("note", "Ngoại suy chứ không phải đo thật: mọi khí đều hoá lỏng trước khi tới "
                             "gần nhiệt độ đó.")],
             cap="Thể tích khí theo nhiệt độ Celsius ở áp suất không đổi",
             tag="Ý NGHĨA", figw=5.8)

    d.bigfigure("Ba quá trình trên ba hệ trục — bảng tra nhanh", "k_dt_ba_he_truc",
                cap="Dạng đồ thị của ba quá trình trên các hệ trục khác nhau",
                items=[("b", "Đường đẳng nhiệt trong hệ (p, V) là hypebol; trong hệ (p, T) và (V, T) "
                             "nó là đường thẳng đứng hoặc nằm ngang tuỳ trục."),
                       ("b", "Đường đẳng tích trong (p, T) và đường đẳng áp trong (V, T) đều là "
                             "ĐƯỜNG THẲNG ĐI QUA GỐC toạ độ.")],
                tag="BẢNG CHỐT",
                note="Câu hỏi kinh điển của đề thi: cho đồ thị trên một hệ trục, yêu cầu vẽ lại trên "
                     "hệ trục khác. Hãy luyện kĩ dạng này.")

    d.example("Ví dụ 1 — Định luật Boyle",
              "Một khối khí có thể tích 6,0 L ở áp suất 1,0·10⁵ Pa. Nén đẳng nhiệt khối khí đến thể "
              "tích 2,5 L. Tính áp suất lúc sau.",
              [("num", ("1.", "Quá trình đẳng nhiệt, lượng khí không đổi ⇒ dùng p₁V₁ = p₂V₂.")),
               ("num", ("2.", "1,0·10⁵ · 6,0 = p₂ · 2,5.")),
               ("num", ("3.", "p₂ = 6,0·10⁵ / 2,5 = 2,4·10⁵ Pa.")),
               ("note", "Thể tích giảm 2,4 lần thì áp suất tăng đúng 2,4 lần — luôn kiểm tra bằng "
                        "tỉ lệ nghịch trước khi chọn đáp án.")],
              "p₂ = 2,4·10⁵ Pa", sub="Bài 9")

    d.example("Ví dụ 2 — Định luật Gay-Lussac (bẫy đơn vị nhiệt độ)",
              "Một bình kín chứa khí ở 27 °C, áp suất 2,0·10⁵ Pa. Đun nóng bình đến 127 °C. "
              "Tính áp suất khí lúc này, coi thể tích bình không đổi.",
              [("num", ("1.", "Bình kín, thể tích không đổi ⇒ quá trình đẳng tích ⇒ p₁/T₁ = p₂/T₂.")),
               ("num", ("2.", "Đổi sang kelvin:  T₁ = 27 + 273 = 300 K;  T₂ = 127 + 273 = 400 K.")),
               ("num", ("3.", "p₂ = p₁ · T₂/T₁ = 2,0·10⁵ · 400/300 ≈ 2,67·10⁵ Pa.")),
               ("note", "Nếu lấy tỉ số 127/27 sẽ ra 9,4·10⁵ Pa — đây chính là phương án nhiễu "
                        "được cài trong hầu hết các đề.")],
              "p₂ ≈ 2,67·10⁵ Pa", sub="Bài 11")

    d.quiz("Kiểm tra nhanh",
           "Nung nóng đẳng áp một lượng khí lí tưởng từ 27 °C lên 327 °C. Thể tích khí thay đổi thế nào?",
           ["Tăng 12,1 lần.", "Tăng 2,0 lần.", "Tăng 1,5 lần.", "Giảm 2,0 lần."],
           "B",
           "Đẳng áp nên V ~ T. Đổi kelvin: T₁ = 300 K, T₂ = 600 K, tỉ số bằng 2,0 nên thể tích tăng "
           "gấp đôi. Đáp án 12,1 lần ứng với việc lấy sai tỉ số 327/27 — bẫy quen thuộc.")

    d.wrapup("Tổng kết buổi 2",
             [("head", "Ba công thức và một quy tắc"),
              ("b", "Đẳng nhiệt:  p₁V₁ = p₂V₂."),
              ("b", "Đẳng áp:  V₁/T₁ = V₂/T₂."),
              ("b", "Đẳng tích:  p₁/T₁ = p₂/T₂."),
              ("b", "Quy tắc vàng: hễ trong công thức có chữ T thì phải đổi sang kelvin.")],
             todo=["Làm Đề 2 và Đề 3 – Chương 2.",
                   "Vẽ lại bảng ba quá trình trên ba hệ trục từ trí nhớ.",
                   "Đọc trước phương trình trạng thái."])


# =====================================================================  BUỔI 3
def buoi3(d):
    d.title_slide(
        sub="Buổi 3 — Phương trình trạng thái và phương trình Clapeyron",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Vận dụng được phương trình trạng thái cho quá trình bất kì",
                "Dùng được phương trình Clapeyron pV = nRT khi bài toán liên quan khối lượng khí",
                "Xử lí được bài toán khí thoát ra hoặc bơm thêm vào"])

    d.section(1, "Phương trình trạng thái", "Công thức duy nhất bao trùm cả ba định luật",
              items=["Xây dựng công thức", "Trường hợp riêng", "Bài tập vận dụng"])

    d.figure("Phương trình trạng thái khí lí tưởng", "k_sd_ba_trang_thai",
             items=[("head", "Điều kiện áp dụng"),
                    ("b", "Áp dụng cho MỘT LƯỢNG KHÍ XÁC ĐỊNH (khối lượng không đổi)."),
                    ("b", "Hai trạng thái bất kì, không cần biết đường đi giữa chúng."),
                    ("gap", 0.05),
                    ("head", "Ba định luật là trường hợp riêng"),
                    ("sub", "T₁ = T₂ ⇒ p₁V₁ = p₂V₂  (Boyle)."),
                    ("sub", "p₁ = p₂ ⇒ V₁/T₁ = V₂/T₂  (Charles)."),
                    ("sub", "V₁ = V₂ ⇒ p₁/T₁ = p₂/T₂  (Gay-Lussac)."),
                    ("note", "Chỉ cần thuộc MỘT công thức này, ba định luật kia tự suy ra.")],
             cap="Liên hệ giữa hai trạng thái của cùng một lượng khí",
             tag="TRỌNG TÂM", figw=6.0)

    d.formulas("Phương trình Clapeyron – Mendeleev",
               [(r"pV = nRT", "n là số mol khí; R = 8,31 J/(mol·K) là hằng số khí lí tưởng."),
                (r"pV = \frac{m}{M}RT", "Dạng dùng khi đề cho khối lượng m và khối lượng mol M."),
                (r"n = \frac{m}{M} = \frac{N}{N_A}",
                 "N là số phân tử; Nₐ = 6,02·10²³ mol⁻¹ là hằng số Avogadro.")],
               lead="Dùng phương trình này khi bài toán liên quan tới KHỐI LƯỢNG, SỐ MOL hoặc "
                    "KHỐI LƯỢNG RIÊNG của khí — những đại lượng mà phương trình trạng thái không chứa.",
               foot="Với R = 8,31 J/(mol·K), bắt buộc dùng p theo Pa, V theo m³, T theo K. "
                    "Đây là chỗ sai đơn vị phổ biến nhất.",
               tag="TRỌNG TÂM", sub="Bài 12")

    d.table("Chọn công thức nào?",
            ["Dấu hiệu trong đề", "Công thức nên dùng"],
            [["Một lượng khí, hai trạng thái, không nhắc khối lượng", "p₁V₁/T₁ = p₂V₂/T₂"],
             ["Đề cho khối lượng m hoặc khối lượng mol M", "pV = (m/M)·R·T"],
             ["Đề hỏi số phân tử hoặc số mol", "pV = nRT với n = N/Nₐ"],
             ["Khí thoát ra hoặc bơm thêm vào bình", "Viết pV = nRT cho từng lượng khí rồi lập hiệu"],
             ["Đề hỏi khối lượng riêng ρ của khí", "ρ = m/V = pM/(RT)"]],
            widths=[2.2, 1.7], tag="ĐỊNH HƯỚNG",
            foot="Quy tắc chung: phương trình trạng thái dùng khi LƯỢNG KHÍ KHÔNG ĐỔI; "
                 "phương trình Clapeyron dùng khi lượng khí thay đổi hoặc đề liên quan tới m, n, ρ.")

    d.example("Ví dụ 1 — Phương trình trạng thái",
              "Một lượng khí có thể tích 10 L ở áp suất 2,0·10⁵ Pa và nhiệt độ 27 °C. Người ta nén khí "
              "xuống còn 4,0 L đồng thời làm nóng tới 127 °C. Tính áp suất lúc sau.",
              [("num", ("1.", "Lượng khí không đổi ⇒ dùng p₁V₁/T₁ = p₂V₂/T₂.")),
               ("num", ("2.", "T₁ = 300 K;  T₂ = 400 K.")),
               ("num", ("3.", "p₂ = p₁ · (V₁/V₂) · (T₂/T₁) = 2,0·10⁵ · (10/4,0) · (400/300).")),
               ("num", ("4.", "p₂ = 2,0·10⁵ · 2,5 · 1,333 ≈ 6,67·10⁵ Pa.")),
               ("note", "Không cần đổi lít sang m³ vì V xuất hiện ở cả hai vế dưới dạng tỉ số.")],
              "p₂ ≈ 6,67·10⁵ Pa", sub="Bài 12")

    d.example("Ví dụ 2 — Bài toán khí thoát ra khỏi bình",
              "Một bình thể tích 20 L chứa khí ở 27 °C, áp suất 4,0·10⁵ Pa. Mở van cho khí thoát bớt "
              "ra ngoài cho tới khi áp suất còn 3,0·10⁵ Pa, nhiệt độ vẫn giữ 27 °C. Hỏi lượng khí đã "
              "thoát ra chiếm bao nhiêu phần trăm lượng khí ban đầu?",
              [("num", ("1.", "Lượng khí THAY ĐỔI nên không dùng được phương trình trạng thái. "
                              "Viết pV = nRT cho khí CÒN LẠI TRONG BÌNH ở hai thời điểm.")),
               ("num", ("2.", "V và T không đổi ⇒ n tỉ lệ thuận với p.")),
               ("num", ("3.", "n₂/n₁ = p₂/p₁ = 3,0/4,0 = 0,75 ⇒ còn lại 75 %.")),
               ("num", ("4.", "Vậy lượng khí đã thoát ra chiếm 25 % lượng khí ban đầu.")),
               ("note", "Mẹo: khi V và T không đổi, số mol khí trong bình tỉ lệ thuận với áp suất. "
                        "Đây là ý tưởng cốt lõi của mọi bài “xả bớt khí”.")],
              "25 % lượng khí ban đầu đã thoát ra", sub="Bài 12")

    d.example("Ví dụ 3 — Tính khối lượng khí",
              "Một bình thể tích 8,31 L chứa khí ôxi (M = 32 g/mol) ở nhiệt độ 27 °C và áp suất "
              "1,0·10⁵ Pa. Tính khối lượng khí trong bình.",
              [("num", ("1.", "Đổi đơn vị:  V = 8,31 L = 8,31·10⁻³ m³;  T = 300 K.")),
               ("num", ("2.", "Số mol:  n = pV/(RT) = (1,0·10⁵ · 8,31·10⁻³)/(8,31 · 300).")),
               ("num", ("3.", "n = 831 / 2493 ≈ 0,333 mol.")),
               ("num", ("4.", "Khối lượng:  m = n·M = 0,333 · 32 ≈ 10,7 g.")),
               ("note", "Quên đổi lít sang m³ sẽ cho kết quả sai lệch đúng 1000 lần — "
                        "một trong bốn phương án nhiễu quen thuộc.")],
              "m ≈ 10,7 g", sub="Bài 12")

    d.quiz("Kiểm tra nhanh",
           "Bơm thêm khí vào một bình kín cho tới khi số mol khí tăng gấp đôi, nhiệt độ giữ nguyên. "
           "Áp suất trong bình thay đổi thế nào?",
           ["Không đổi vì thể tích bình không đổi.", "Tăng gấp đôi.",
            "Giảm một nửa.", "Tăng gấp bốn lần."],
           "B",
           "Từ pV = nRT, với V và T không đổi thì p tỉ lệ thuận với n. Số mol tăng gấp đôi nên áp "
           "suất tăng gấp đôi. Phương án đầu nhầm lẫn giữa thể tích bình và lượng khí trong bình.")

    d.wrapup("Tổng kết buổi 3",
             [("head", "Ba ý phải nhớ"),
              ("b", "Lượng khí không đổi ⇒ p₁V₁/T₁ = p₂V₂/T₂."),
              ("b", "Lượng khí thay đổi, hoặc đề cho m, n, ρ ⇒ pV = nRT = (m/M)RT."),
              ("b", "Dùng R = 8,31 thì bắt buộc p (Pa), V (m³), T (K).")],
             todo=["Làm Đề 4 và Đề 5 – Chương 2.",
                   "Tự lập bảng “dấu hiệu đề – công thức cần dùng”.",
                   "Đọc trước bài Áp suất khí theo mô hình động học phân tử."])


# =====================================================================  BUỔI 4
def buoi4(d):
    d.title_slide(
        sub="Buổi 4 — Áp suất chất khí theo mô hình động học phân tử. Động năng phân tử",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được ý nghĩa của công thức áp suất theo mô hình động học phân tử",
                "Vận dụng được W̄ₐ = 3/2·kT để so sánh các chất khí",
                "Liên hệ được giữa nhiệt độ vĩ mô và chuyển động vi mô"])

    d.section(1, "Áp suất từ góc nhìn vi mô", "Nối liền thế giới phân tử với đại lượng đo được",
              items=["Công thức áp suất", "Động năng phân tử và nhiệt độ", "Hệ quả và ứng dụng"])

    d.formulas("Hai công thức nối vi mô với vĩ mô",
               [(r"p = \frac{1}{3}\mu m_0 \overline{v^{2}}",
                 "μ là mật độ phân tử (số phân tử trên một đơn vị thể tích); m₀ là khối lượng một phân tử."),
                (r"\overline{W}_{\mathrm{d}} = \frac{3}{2}kT",
                 "Động năng tịnh tiến trung bình của một phân tử chỉ phụ thuộc NHIỆT ĐỘ."),
                (r"p = \frac{2}{3}\mu\,\overline{W}_{\mathrm{d}}",
                 "Kết hợp hai công thức trên: áp suất tỉ lệ với mật độ và động năng trung bình.")],
               lead="Ba công thức này giải thích vì sao các định luật chất khí lại có dạng như vậy.",
               foot="k = 1,38·10⁻²³ J/K là hằng số Boltzmann. Khi đề cho công thức này, "
                    "nó luôn được ghi sẵn trong đề bài.",
               tag="TRỌNG TÂM", sub="Bài 13")

    d.content("Bốn hệ quả cần nắm chắc",
              [("num", ("1.", "Ở CÙNG một nhiệt độ, mọi chất khí đều có động năng tịnh tiến trung bình "
                              "bằng nhau, không phụ thuộc loại khí.")),
               ("num", ("2.", "Vì W̄ₐ = ½m₀v̄² bằng nhau nên phân tử NHẸ hơn sẽ chuyển động NHANH hơn. "
                              "Ở 0 °C, phân tử H₂ nhanh gấp khoảng 4 lần phân tử O₂.")),
               ("num", ("3.", "Nhiệt độ tuyệt đối T tỉ lệ thuận với động năng trung bình. "
                              "T tăng gấp đôi thì W̄ₐ tăng gấp đôi, nhưng tốc độ trung bình chỉ tăng √2 lần.")),
               ("num", ("4.", "Áp suất phụ thuộc ĐỒNG THỜI mật độ phân tử và nhiệt độ. "
                              "Muốn tăng p có thể tăng mật độ (bơm thêm khí, nén nhỏ thể tích) "
                              "hoặc tăng nhiệt độ.")),
               ("note", "Bẫy thường gặp: “khí nào nặng hơn thì động năng trung bình lớn hơn” — SAI. "
                        "Nặng hơn thì chậm hơn, tích ½m₀v̄² vẫn bằng nhau.")],
              sub="Bài 13", tag="HỆ QUẢ")

    d.example("Ví dụ 1 — So sánh hai chất khí",
              "Ở cùng nhiệt độ 27 °C, so sánh động năng tịnh tiến trung bình và tốc độ trung bình "
              "của phân tử khí hiđrô (M = 2 g/mol) và khí ôxi (M = 32 g/mol).",
              [("num", ("1.", "Động năng trung bình W̄ₐ = 3/2·kT chỉ phụ thuộc T ⇒ hai khí có "
                              "động năng trung bình BẰNG NHAU.")),
               ("num", ("2.", "Từ ½m₀v̄² bằng nhau ⇒ v̄ tỉ lệ nghịch với căn bậc hai của khối lượng phân tử.")),
               ("num", ("3.", "v̄(H₂)/v̄(O₂) = √(32/2) = √16 = 4.")),
               ("p", "Vậy phân tử hiđrô chuyển động nhanh gấp 4 lần phân tử ôxi, "
                     "nhưng động năng trung bình của chúng bằng nhau.")],
              "Động năng bằng nhau;  v̄(H₂) = 4·v̄(O₂)",
              tip="Đây là dạng câu hỏi lí thuyết – định tính rất hay xuất hiện ở Phần II (đúng/sai).",
              sub="Bài 13")

    d.example("Ví dụ 2 — Tính động năng trung bình",
              "Tính động năng tịnh tiến trung bình của một phân tử khí ở 27 °C. "
              "Cho k = 1,38·10⁻²³ J/K.",
              [("num", ("1.", "Đổi nhiệt độ:  T = 27 + 273 = 300 K.")),
               ("num", ("2.", "W̄ₐ = 3/2 · k · T = 1,5 · 1,38·10⁻²³ · 300.")),
               ("num", ("3.", "W̄ₐ = 1,5 · 4,14·10⁻²¹ = 6,21·10⁻²¹ J.")),
               ("note", "Con số rất nhỏ, nhưng một mol khí có tới 6,02·10²³ phân tử nên tổng động "
                        "năng lên tới hàng nghìn jun.")],
              "W̄ₐ ≈ 6,21·10⁻²¹ J", sub="Bài 13")

    d.figure("Giải thích các định luật chất khí bằng mô hình phân tử", "k_sd_vacham_thanh",
             items=[("head", "Định luật Boyle"),
                    ("sub", "Nén nhỏ V ⇒ mật độ μ tăng ⇒ nhiều va chạm hơn ⇒ p tăng, T không đổi "
                            "nên mỗi va chạm mạnh như cũ."),
                    ("head", "Định luật Gay-Lussac"),
                    ("sub", "Đun nóng, V cố định ⇒ μ không đổi nhưng phân tử nhanh hơn ⇒ mỗi va chạm "
                            "mạnh hơn và nhiều hơn ⇒ p tăng."),
                    ("head", "Định luật Charles"),
                    ("sub", "Đun nóng, giữ p cố định ⇒ phân tử nhanh hơn nên phải giãn V để mật độ "
                            "giảm, giữ cho p không đổi.")],
             cap="Cơ chế vi mô của áp suất", tag="GIẢI THÍCH", figw=5.4, side="left")

    d.quiz("Kiểm tra nhanh",
           "Hai bình giống hệt nhau, một chứa khí hêli, một chứa khí nitơ, cùng nhiệt độ và cùng số "
           "phân tử. So sánh áp suất trong hai bình.",
           ["Bình nitơ có áp suất lớn hơn vì phân tử nặng hơn.",
            "Bình hêli có áp suất lớn hơn vì phân tử nhanh hơn.",
            "Áp suất hai bình bằng nhau.",
            "Không so sánh được nếu chưa biết khối lượng mol."],
           "C",
           "Áp suất p = 2/3·μ·W̄ₐ. Hai bình có cùng thể tích và cùng số phân tử nên μ bằng nhau; "
           "cùng nhiệt độ nên W̄ₐ bằng nhau. Vậy áp suất bằng nhau. Phân tử hêli tuy nhanh hơn "
           "nhưng lại nhẹ hơn đúng theo tỉ lệ để động năng bù trừ.")

    d.media("Mô phỏng nên dùng",
            [("Gas Properties — chế độ “Energy”", "PhET – phet.colorado.edu",
              "Hiển thị đồng thời biểu đồ phân bố tốc độ và áp kế khi thay đổi nhiệt độ.",
              "Tăng nhiệt độ làm đường phân bố tốc độ dịch sang phải và áp suất tăng theo."),
             ("Gas Properties — hai loại khí nặng nhẹ", "PhET – phet.colorado.edu",
              "Thả đồng thời khí nặng và khí nhẹ vào cùng một bình.",
              "Ở cùng nhiệt độ, khí nhẹ chuyển động nhanh hơn rõ rệt."),
             ("Bơm xe đạp và sờ thân bơm", "Thí nghiệm tại lớp",
              "Bơm liên tục 20–30 nhịp rồi sờ thân bơm.",
              "Thân bơm nóng lên: công nén làm tăng động năng phân tử, tức tăng nhiệt độ.")])

    d.wrapup("Tổng kết buổi 4",
             [("head", "Ba ý phải nhớ"),
              ("b", "Áp suất khí do va chạm phân tử: p = 1/3·μ·m₀·v̄² = 2/3·μ·W̄ₐ."),
              ("b", "W̄ₐ = 3/2·kT chỉ phụ thuộc nhiệt độ, không phụ thuộc loại khí."),
              ("b", "Cùng T: phân tử nhẹ chạy nhanh hơn nhưng động năng trung bình vẫn bằng nhau.")],
             todo=["Làm Đề 6 và Đề 7 – Chương 2.",
                   "Tự giải thích ba định luật chất khí bằng ngôn ngữ phân tử.",
                   "Ôn lại toàn bộ công thức chuẩn bị buổi luyện tập."])


# =====================================================================  BUỔI 5
def buoi5(d):
    d.title_slide(
        sub="Buổi 5 — Luyện tập tổng hợp: đồ thị, chu trình và bài toán pit-tông",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Đọc và chuyển đổi đồ thị giữa các hệ trục",
                "Giải được bài toán chu trình kín nhiều giai đoạn",
                "Xử lí thành thạo bài toán cột khí và pit-tông"])

    d.section(1, "Bài toán đồ thị", "Dạng xuất hiện trong hầu hết các đề thi",
              items=["Đọc đồ thị", "Chuyển hệ trục", "Chu trình kín"])

    d.figure("Ba quá trình xuất phát từ cùng một trạng thái", "k_dt_baquatrinh",
             items=[("head", "Nhận dạng từng đường"),
                    ("b", "(a) thẳng đứng: V không đổi ⇒ quá trình ĐẲNG TÍCH, áp suất tăng."),
                    ("b", "(b) hypebol: p·V không đổi ⇒ quá trình ĐẲNG NHIỆT, khí giãn nở."),
                    ("b", "(c) nằm ngang: p không đổi ⇒ quá trình ĐẲNG ÁP, khí giãn nở."),
                    ("gap", 0.05),
                    ("note", "So sánh nhiệt độ cuối: đẳng áp (c) có T tăng, đẳng nhiệt (b) có T không "
                             "đổi, nên nhiệt độ cuối của (c) lớn hơn của (b).")],
             cap="Ba quá trình cùng xuất phát từ trạng thái M", tag="ĐỒ THỊ", figw=5.6)

    d.example("Ví dụ 1 — Chu trình kín",
              "Một lượng khí lí tưởng thực hiện chu trình (1)→(2)→(3)→(4)→(1) như hình. "
              "Biết ở trạng thái (1): V = 1,0 L, p = 1,0·10⁵ Pa, T₁ = 300 K. "
              "Tính nhiệt độ ở các trạng thái (2), (3) và (4).",
              [("num", ("1.", "(1)→(2) đẳng tích, p tăng từ 1 lên 3 (đơn vị 10⁵ Pa) ⇒ "
                              "T₂ = T₁·p₂/p₁ = 300·3 = 900 K.")),
               ("num", ("2.", "(2)→(3) đẳng áp, V tăng từ 1 lên 3 L ⇒ T₃ = T₂·V₃/V₂ = 900·3 = 2700 K.")),
               ("num", ("3.", "(3)→(4) đẳng tích, p giảm từ 3 xuống 1 ⇒ T₄ = T₃·p₄/p₃ = 2700/3 = 900 K.")),
               ("num", ("4.", "(4)→(1) đẳng áp, V giảm từ 3 xuống 1 L ⇒ T₁ = 900/3 = 300 K — "
                              "đúng bằng giá trị ban đầu, chu trình khép kín."))],
              "T₂ = 900 K;  T₃ = 2700 K;  T₄ = 900 K",
              fig="k_dt_chutrinh", cap="Chu trình kín trong hệ (p, V)",
              tip="Bước cuối luôn dùng để KIỂM TRA: đi hết chu trình phải quay về đúng nhiệt độ ban đầu. "
                  "Nếu không khớp thì có lỗi ở đâu đó.",
              sub="Luyện tập")

    d.example("Ví dụ 2 — Xi lanh có quả nặng trên pit-tông",
              "Một xi lanh thẳng đứng tiết diện S chứa khí, phía trên là pit-tông khối lượng m có thể "
              "trượt không ma sát. Đun nóng khí. Hỏi quá trình biến đổi trạng thái của khí thuộc "
              "loại nào và vì sao?",
              [("num", ("1.", "Pit-tông tự do nên nó luôn cân bằng: áp suất khí đẩy lên bằng áp suất "
                              "khí quyển cộng áp suất do trọng lượng pit-tông.")),
               ("num", ("2.", "p = p₀ + mg/S. Cả ba đại lượng vế phải đều không đổi.")),
               ("num", ("3.", "Vậy áp suất khí KHÔNG ĐỔI ⇒ quá trình ĐẲNG ÁP, dùng V₁/T₁ = V₂/T₂.")),
               ("note", "Bẫy ngược lại: nếu pit-tông bị CHẶN bởi vấu hoặc bị giữ cố định thì thể tích "
                        "không đổi ⇒ quá trình đẳng tích. Luôn đọc kĩ xem pit-tông có tự do hay không.")],
              "Quá trình đẳng áp với p = p₀ + mg/S",
              fig="k_sd_xilanh_quanang", cap="Xi lanh thẳng đứng có quả nặng đặt trên pit-tông",
              sub="Luyện tập")

    d.example("Ví dụ 3 — Cột khí bị giam bởi thuỷ ngân",
              "Một ống thuỷ tinh hình trụ, một đầu kín, đặt thẳng đứng miệng ở TRÊN, giam một cột khí "
              "dài 20 cm bằng một cột thuỷ ngân dài 10 cm. Áp suất khí quyển là 75 cmHg. "
              "Lật ngược ống cho miệng xuống dưới. Tính chiều dài cột khí lúc này, nhiệt độ không đổi.",
              [("num", ("1.", "Miệng ở TRÊN: thuỷ ngân đè xuống khí ⇒ p₁ = 75 + 10 = 85 cmHg.")),
               ("num", ("2.", "Miệng ở DƯỚI: thuỷ ngân kéo xuống, giảm áp lên khí ⇒ p₂ = 75 − 10 = 65 cmHg.")),
               ("num", ("3.", "Nhiệt độ không đổi ⇒ p₁ℓ₁ = p₂ℓ₂  (tiết diện chung triệt tiêu).")),
               ("num", ("4.", "85 · 20 = 65 · ℓ₂ ⇒ ℓ₂ = 1700/65 ≈ 26,2 cm.")),
               ("note", "Vì áp suất giảm nên cột khí phải dài ra — kết quả 26,2 cm > 20 cm là hợp lí. "
                        "Nếu tính ra ngắn hơn thì đã cộng trừ nhầm dấu.")],
              "ℓ₂ ≈ 26,2 cm",
              fig="k_sd_ong_khi", cap="Cột khí bị giam bởi cột thuỷ ngân",
              tip="Quy tắc dấu: khí ở PHÍA DƯỚI cột thuỷ ngân thì CỘNG, khí ở PHÍA TRÊN thì TRỪ.",
              sub="Luyện tập")

    d.table("Bốn dạng câu hỏi thường gặp của Chương II",
            ["Dạng", "Dấu hiệu nhận biết", "Cách xử lí"],
            [["Một quá trình đơn", "Nhắc rõ đẳng nhiệt / đẳng áp / đẳng tích",
              "Dùng đúng một trong ba định luật"],
             ["Hai thông số cùng đổi", "Cả p, V, T đều thay đổi",
              "Dùng phương trình trạng thái p₁V₁/T₁ = p₂V₂/T₂"],
             ["Đồ thị và chu trình", "Đề kèm hình vẽ đường biểu diễn",
              "Nhận dạng từng đoạn, áp dụng định luật tương ứng, kiểm tra khép kín"],
             ["Pit-tông và cột thuỷ ngân", "Có xi lanh, pit-tông, ống chứa thuỷ ngân",
              "Viết điều kiện cân bằng để tìm p, rồi mới áp dụng định luật"]],
            widths=[1.1, 1.7, 1.8], tag="PHÂN DẠNG",
            foot="Dạng cuối là dạng phân loại học sinh giỏi: khó không phải vì tính toán, "
                 "mà vì phải phân tích đúng lực tác dụng lên pit-tông hoặc cột thuỷ ngân.")

    d.quiz("Kiểm tra nhanh",
           "Một lượng khí biến đổi theo đồ thị là đoạn thẳng đi qua GỐC toạ độ trong hệ (p, T). "
           "Quá trình đó là quá trình gì?",
           ["Đẳng nhiệt.", "Đẳng áp.", "Đẳng tích.", "Không xác định được."],
           "C",
           "Đường thẳng qua gốc trong hệ (p, T) nghĩa là p tỉ lệ thuận với T, tức p/T không đổi — "
           "đúng là định luật Gay-Lussac cho quá trình đẳng tích. "
           "Nếu đường thẳng KHÔNG đi qua gốc thì lượng khí đã thay đổi hoặc trục dùng thang Celsius.")

    d.wrapup("Tổng kết Chương II",
             [("head", "Bản đồ kiến thức cả chương"),
              ("b", "Mô hình động học phân tử và khái niệm khí lí tưởng."),
              ("b", "Ba định luật chất khí và dạng đồ thị trên mọi hệ trục."),
              ("b", "Phương trình trạng thái và phương trình Clapeyron pV = nRT."),
              ("b", "Áp suất và động năng phân tử: p = 2/3·μ·W̄ₐ;  W̄ₐ = 3/2·kT.")],
             todo=["Làm trọn bộ 10 đề Chương 2 theo thứ tự.",
                   "Luyện riêng 20 câu đồ thị và 10 câu pit-tông.",
                   "Làm đề tổng hợp số 1 và 2 sau khi học xong bốn chương."])


SPEC = [
    dict(file="C02_Buoi1_Mo_hinh_dong_hoc_phan_tu_chat_khi.pptx",
         title="Mô hình động học phân tử chất khí. Khí lí tưởng",
         chapter=CH + " • Buổi 1", th=TH, slides=buoi1),
    dict(file="C02_Buoi2_Ba_dinh_luat_chat_khi.pptx",
         title="Định luật Boyle. Định luật Charles. Định luật Gay-Lussac",
         chapter=CH + " • Buổi 2", th=TH, slides=buoi2),
    dict(file="C02_Buoi3_Phuong_trinh_trang_thai_va_Clapeyron.pptx",
         title="Phương trình trạng thái. Phương trình Clapeyron",
         chapter=CH + " • Buổi 3", th=TH, slides=buoi3),
    dict(file="C02_Buoi4_Ap_suat_va_dong_nang_phan_tu.pptx",
         title="Áp suất chất khí. Động năng phân tử và nhiệt độ",
         chapter=CH + " • Buổi 4", th=TH, slides=buoi4),
    dict(file="C02_Buoi5_Luyen_tap_tong_hop_chuong_II.pptx",
         title="Luyện tập tổng hợp Chương II",
         chapter=CH + " • Buổi 5", th=TH, slides=buoi5),
]
