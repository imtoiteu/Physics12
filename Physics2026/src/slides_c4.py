# -*- coding: utf-8 -*-
"""SLIDE BÀI GIẢNG — CHƯƠNG IV: VẬT LÍ HẠT NHÂN.  Năm buổi dạy."""
from deck import Deck

TH = 4
CH = "Chương IV – Vật lí hạt nhân"
MT = "Ôn thi tốt nghiệp THPT 2026  •  Lớp 12"


def buoi1(d):
    d.title_slide(
        sub="Buổi 1 — Cấu trúc hạt nhân. Độ hụt khối và năng lượng liên kết",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Đọc và viết đúng kí hiệu hạt nhân, xác định số prôtôn và nơtron",
                "Tính được độ hụt khối và năng lượng liên kết",
                "Dùng năng lượng liên kết riêng để so sánh độ bền vững của hạt nhân"])

    d.section(1, "Cấu trúc hạt nhân", "Từ nguyên tử xuống tới hạt nhân",
              items=["Nuclêôn", "Kí hiệu hạt nhân", "Đồng vị", "Đơn vị khối lượng nguyên tử"])

    d.figure("Hạt nhân được cấu tạo như thế nào?", "h_sd_cautruc",
             items=[("head", "Hai loại nuclêôn"),
                    ("b", "Prôtôn mang điện tích +e, khối lượng ≈ 1,0073 u."),
                    ("b", "Nơtron không mang điện, khối lượng ≈ 1,0087 u — nặng hơn prôtôn một chút."),
                    ("gap", 0.05),
                    ("head", "Kí hiệu"),
                    ("b", "Z là số prôtôn, cũng là số thứ tự của nguyên tố trong bảng tuần hoàn."),
                    ("b", "A là số nuclêôn (số khối); số nơtron N = A − Z."),
                    ("note", "Kích thước hạt nhân chỉ cỡ 10⁻¹⁵ m, nhỏ hơn nguyên tử khoảng 100 000 lần, "
                             "nhưng chứa gần như toàn bộ khối lượng của nguyên tử.")],
             cap="Cấu tạo hạt nhân và ý nghĩa của kí hiệu", tag="TRỌNG TÂM", figw=6.2)

    d.content("Đồng vị và đơn vị khối lượng nguyên tử",
              [("head", "Đồng vị"),
               ("p", "Các đồng vị của cùng một nguyên tố có CÙNG số prôtôn Z nhưng KHÁC số nơtron, "
                     "do đó khác số khối A."),
               ("sub", "Ví dụ hiđrô có ba đồng vị: ¹H (hiđrô thường), ²H (đơteri), ³H (triti)."),
               ("sub", "Cacbon có ¹²C bền và ¹⁴C phóng xạ — chính ¹⁴C dùng để xác định tuổi mẫu vật."),
               ("rule", None),
               ("head", "Đơn vị khối lượng nguyên tử u"),
               ("b", "1 u bằng 1/12 khối lượng của một nguyên tử đồng vị ¹²C."),
               ("b", "1 u = 1,66055·10⁻²⁷ kg."),
               ("b", "Hệ thức quan trọng: 1 u·c² = 931,5 MeV, dùng để đổi trực tiếp từ khối lượng "
                     "sang năng lượng."),
               ("note", "Vì các đồng vị có cùng Z nên chúng có cùng tính chất HOÁ HỌC, "
                        "nhưng tính chất HẠT NHÂN thì rất khác nhau.")],
              sub="Bài 18 — Cấu trúc hạt nhân", tag="ĐỊNH NGHĨA")

    d.figure("Độ hụt khối — khối lượng biến đi đâu?", "h_sd_dohutkhoi",
             items=[("head", "Hiện tượng"),
                    ("p", "Khối lượng của hạt nhân luôn NHỎ HƠN tổng khối lượng các nuclêôn tạo "
                          "thành nó khi còn rời nhau."),
                    ("gap", 0.05),
                    ("head", "Giải thích"),
                    ("b", "Phần khối lượng hụt đi đã chuyển thành năng lượng liên kết, toả ra khi "
                          "các nuclêôn kết hợp lại."),
                    ("b", "Ngược lại, muốn phá vỡ hạt nhân thành các nuclêôn riêng lẻ thì phải "
                          "cung cấp đúng năng lượng đó."),
                    ("note", "Đây là ứng dụng trực tiếp của hệ thức Einstein E = mc²: "
                             "khối lượng và năng lượng là hai mặt của cùng một đại lượng.")],
             cap="Độ hụt khối của hạt nhân heli", tag="TRỌNG TÂM", figw=6.1)

    d.formulas("Ba công thức của bài này",
               [(r"\Delta m = Zm_p + (A-Z)m_n - m_X",
                 "Độ hụt khối: tổng khối lượng nuclêôn riêng lẻ trừ đi khối lượng hạt nhân."),
                (r"W_{\mathrm{lk}} = \Delta m\,c^2",
                 "Năng lượng liên kết. Nếu Δm tính bằng u thì nhân 931,5 để ra MeV."),
                (r"\varepsilon = \frac{W_{\mathrm{lk}}}{A}",
                 "Năng lượng liên kết RIÊNG — năng lượng liên kết tính trên một nuclêôn.")],
               lead="Năng lượng liên kết riêng ε mới là thước đo độ bền vững, không phải W(lk).",
               foot="Hạt nhân có ε càng lớn thì càng bền vững. Các hạt nhân bền nhất nằm quanh "
                    "vùng số khối A ≈ 56 (sắt, niken) với ε ≈ 8,8 MeV/nuclêôn.",
               tag="TRỌNG TÂM", sub="Bài 18")

    d.figure("Đường cong năng lượng liên kết riêng", "h_dt_nllk_rieng",
             items=[("head", "Ba vùng trên đồ thị"),
                    ("b", "A nhỏ (H, He, Li): ε thấp, hạt nhân kém bền — kết hợp lại sẽ toả năng lượng "
                          "⇒ phản ứng NHIỆT HẠCH."),
                    ("b", "A ≈ 56: ε lớn nhất, hạt nhân bền vững nhất."),
                    ("b", "A lớn (U, Th): ε giảm trở lại — vỡ ra sẽ toả năng lượng ⇒ phản ứng PHÂN HẠCH."),
                    ("note", "Toàn bộ nguyên lí của năng lượng hạt nhân nằm gọn trong hình dạng "
                             "của đường cong này: mọi phản ứng đi TỚI đỉnh đều toả năng lượng.")],
             cap="Năng lượng liên kết riêng theo số khối", tag="TRỌNG TÂM", figw=5.8, side="left")

    d.example("Ví dụ — Tính năng lượng liên kết",
              "Tính độ hụt khối, năng lượng liên kết và năng lượng liên kết riêng của hạt nhân "
              "⁴₂He. Cho m(He) = 4,0015 u; m(p) = 1,0073 u; m(n) = 1,0087 u; 1 u·c² = 931,5 MeV.",
              [("num", ("1.", "Hạt nhân ⁴₂He có Z = 2 prôtôn và A − Z = 2 nơtron.")),
               ("num", ("2.", "Tổng khối lượng nuclêôn riêng lẻ:  2·1,0073 + 2·1,0087 = 4,0320 u.")),
               ("num", ("3.", "Độ hụt khối:  Δm = 4,0320 − 4,0015 = 0,0305 u.")),
               ("num", ("4.", "Năng lượng liên kết:  W(lk) = 0,0305 · 931,5 ≈ 28,4 MeV.")),
               ("num", ("5.", "Năng lượng liên kết riêng:  ε = 28,4 / 4 ≈ 7,1 MeV/nuclêôn."))],
              "Δm = 0,0305 u;  W(lk) ≈ 28,4 MeV;  ε ≈ 7,1 MeV/nuclêôn",
              tip="Luôn kiểm tra: Δm phải DƯƠNG. Nếu ra âm thì đã lấy nhầm thứ tự phép trừ.",
              sub="Bài 18")

    d.quiz("Kiểm tra nhanh",
           "Hạt nhân X có năng lượng liên kết 128 MeV và số khối 16; hạt nhân Y có năng lượng liên kết "
           "492 MeV và số khối 56. Hạt nhân nào bền vững hơn?",
           ["X, vì số khối nhỏ hơn.", "Y, vì năng lượng liên kết lớn hơn.",
            "Y, vì năng lượng liên kết riêng lớn hơn (8,79 so với 8,00 MeV/nuclêôn).",
            "Hai hạt nhân bền như nhau."],
           "C",
           "Độ bền vững được so sánh bằng năng lượng liên kết RIÊNG chứ không phải năng lượng liên kết "
           "toàn phần. ε(X) = 128/16 = 8,00 MeV/nuclêôn; ε(Y) = 492/56 ≈ 8,79 MeV/nuclêôn. "
           "Y bền hơn. Chọn theo W(lk) lớn hơn là bẫy được cài rất thường xuyên.")

    d.wrapup("Tổng kết buổi 1",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Kí hiệu ᴬ_Z X: Z là số prôtôn, A là số nuclêôn, N = A − Z."),
              ("b", "1 u = 1,66055·10⁻²⁷ kg;  1 u·c² = 931,5 MeV."),
              ("b", "Δm = Z·m(p) + (A−Z)·m(n) − m(X);  W(lk) = Δm·c²."),
              ("b", "Độ bền vững được đo bằng ε = W(lk)/A, không phải bằng W(lk).")],
             todo=["Làm Đề 1 và Đề 2 – Chương 4.",
                   "Luyện đọc kí hiệu 10 hạt nhân bất kì và xác định Z, N.",
                   "Đọc trước bài Phóng xạ."])


def buoi2(d):
    d.title_slide(
        sub="Buổi 2 — Hiện tượng phóng xạ và định luật phóng xạ",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Phân biệt được ba loại tia phóng xạ theo bản chất và khả năng đâm xuyên",
                "Viết đúng phương trình phân rã nhờ quy tắc dịch chuyển",
                "Vận dụng thành thạo định luật phóng xạ"])

    d.section(1, "Ba loại tia phóng xạ", "Bản chất, điện tích và khả năng đâm xuyên",
              items=["Tia alpha, beta, gamma", "Lệch trong điện trường", "Khả năng đâm xuyên"])

    d.content("Phóng xạ là gì?",
              [("head", "Định nghĩa"),
               ("p", "Phóng xạ là quá trình một hạt nhân KHÔNG BỀN tự phát biến đổi thành hạt nhân "
                     "khác, đồng thời phát ra các tia phóng xạ."),
               ("gap", 0.06),
               ("head", "Ba đặc điểm quan trọng"),
               ("b", "Là quá trình TỰ PHÁT, xảy ra hoàn toàn ngẫu nhiên với từng hạt nhân riêng lẻ."),
               ("b", "KHÔNG phụ thuộc các tác động bên ngoài: nhiệt độ, áp suất, trạng thái hoá học "
                     "đều không làm thay đổi tốc độ phân rã."),
               ("b", "Luôn TOẢ năng lượng."),
               ("note", "Đây là điểm khác biệt cốt lõi so với phản ứng hoá học — vốn phụ thuộc rất "
                        "mạnh vào nhiệt độ và chất xúc tác. Câu hỏi này gần như luôn xuất hiện "
                        "trong đề thi.")],
              sub="Bài 19 — Phóng xạ", tag="TRỌNG TÂM")

    d.figure("Ba loại tia trong điện trường", "h_sd_tia_phongxa",
             items=[("head", "Nhận dạng theo độ lệch"),
                    ("b", "Tia α là hạt nhân ⁴₂He, mang điện +2e ⇒ lệch về bản ÂM."),
                    ("b", "Tia β⁻ là dòng electron, mang điện −e ⇒ lệch về bản DƯƠNG."),
                    ("b", "Tia γ là sóng điện từ, không mang điện ⇒ ĐI THẲNG."),
                    ("note", "Tia α nặng hơn tia β khoảng 7000 lần nên tuy điện tích lớn gấp đôi, "
                             "nó vẫn lệch ÍT hơn nhiều so với tia β.")],
             cap="Ba loại tia phóng xạ trong điện trường đều", tag="TRỌNG TÂM", figw=6.3)

    d.figure("Khả năng đâm xuyên", "h_sd_dam_xuyen",
             items=[("head", "Thứ tự cần nhớ"),
                    ("b", "Đâm xuyên tăng dần:  α < β < γ."),
                    ("b", "Ion hoá môi trường giảm dần:  α > β > γ."),
                    ("gap", 0.05),
                    ("head", "Vì sao ngược nhau?"),
                    ("b", "Tia α ion hoá rất mạnh nên mất năng lượng rất nhanh, chỉ đi được vài "
                          "centimét trong không khí và bị tờ giấy chặn lại."),
                    ("b", "Tia γ hầu như không ion hoá nên xuyên qua được lớp chì dày."),
                    ("note", "Hệ quả an toàn: nguồn α nguy hiểm nhất khi bị NUỐT hoặc HÍT vào cơ thể, "
                             "còn nguồn γ nguy hiểm cả khi ở xa.")],
             cap="Khả năng đâm xuyên của ba loại tia", tag="TRỌNG TÂM", figw=6.1, side="left")

    d.figure("Quy tắc dịch chuyển", "h_sd_dich_chuyen",
             items=[("head", "Hai định luật bảo toàn"),
                    ("b", "Bảo toàn số khối A: tổng A trước bằng tổng A sau."),
                    ("b", "Bảo toàn điện tích Z: tổng Z trước bằng tổng Z sau."),
                    ("gap", 0.05),
                    ("note", "Không cần học thuộc bốn dòng của bảng: chỉ cần viết phương trình rồi "
                             "áp dụng hai định luật bảo toàn là tự suy ra được hạt nhân con.")],
             cap="Quy tắc dịch chuyển cho bốn loại phân rã", tag="TRỌNG TÂM", figw=6.4)

    d.formulas("Định luật phóng xạ",
               [(r"N = N_0\,2^{-t/T} = N_0 e^{-\lambda t}",
                 "Số hạt nhân chưa phân rã giảm theo quy luật hàm mũ. T là chu kì bán rã."),
                (r"\lambda = \frac{\ln 2}{T}",
                 "λ là hằng số phóng xạ, đặc trưng cho tốc độ phân rã của mỗi chất."),
                (r"H = \lambda N = H_0\,2^{-t/T}",
                 "Độ phóng xạ H (số phân rã trong một giây), đơn vị becơren (Bq).")],
               lead="Chu kì bán rã T là khoảng thời gian để một nửa số hạt nhân ban đầu bị phân rã.",
               foot="Đặt n = t/T (số chu kì bán rã đã trôi qua) thì N = N₀·2⁻ⁿ. Số hạt nhân ĐÃ phân rã là ΔN = N₀ − N = N₀·(1 − 2⁻ⁿ). "
                    "Nhiều đề hỏi số hạt đã phân rã chứ không hỏi số hạt còn lại.",
               tag="TRỌNG TÂM", sub="Bài 19")

    d.figure("Đồ thị phân rã phóng xạ", "h_dt_phanra",
             items=[("head", "Cách đọc nhanh"),
                    ("b", "Sau 1 chu kì bán rã còn 50 %, sau 2T còn 25 %, sau 3T còn 12,5 %, "
                          "sau 4T còn 6,25 %."),
                    ("b", "Tỉ số giữa số hạt đã phân rã và số hạt còn lại sau nT là (2ⁿ − 1) : 1."),
                    ("note", "Mẹo làm nhanh: nếu đề cho tỉ lệ đẹp như 1/2, 1/4, 1/8, 3/1, 7/1 thì "
                             "t là bội nguyên của T, không cần dùng logarit.")],
             cap="Số hạt nhân chưa phân rã theo thời gian", tag="ĐỒ THỊ", figw=5.7, side="left")

    d.example("Ví dụ 1 — Viết phương trình phân rã",
              "Hạt nhân ²²⁶₈₈Ra phóng xạ α. Viết phương trình phân rã và xác định hạt nhân con.",
              [("num", ("1.", "Phân rã α nghĩa là phát ra hạt ⁴₂He.")),
               ("num", ("2.", "Bảo toàn số khối:  226 = 4 + A ⇒ A = 222.")),
               ("num", ("3.", "Bảo toàn điện tích:  88 = 2 + Z ⇒ Z = 86.")),
               ("num", ("4.", "Nguyên tố có Z = 86 là radon:  ²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn."))],
              "²²⁶₈₈Ra → ⁴₂He + ²²²₈₆Rn", sub="Bài 19")

    d.example("Ví dụ 2 — Định luật phóng xạ",
              "Một mẫu chất phóng xạ có chu kì bán rã 8,0 ngày. Ban đầu mẫu có khối lượng 200 g. "
              "Hỏi sau 24 ngày còn lại bao nhiêu gam, và đã phân rã bao nhiêu gam?",
              [("num", ("1.", "Số chu kì bán rã đã trôi qua:  t/T = 24/8,0 = 3.")),
               ("num", ("2.", "Khối lượng còn lại:  m = m₀·2⁻³ = 200/8 = 25 g.")),
               ("num", ("3.", "Khối lượng đã phân rã:  Δm = 200 − 25 = 175 g.")),
               ("note", "Đề rất hay hỏi khối lượng ĐÃ phân rã. Đọc kĩ câu hỏi trước khi chọn: "
                        "25 g và 175 g thường cùng xuất hiện trong bốn phương án.")],
              "Còn lại 25 g;  đã phân rã 175 g", sub="Bài 19")

    d.example("Ví dụ 3 — Khi t không phải bội của T",
              "Một mẫu phóng xạ có chu kì bán rã T = 10 giờ. Sau bao lâu thì độ phóng xạ của mẫu "
              "giảm còn 30 % giá trị ban đầu?",
              [("num", ("1.", "Đặt n = t/T. Từ H = H₀·2⁻ⁿ và H/H₀ = 0,30 ⇒ 2⁻ⁿ = 0,30.")),
               ("num", ("2.", "Lấy logarit hai vế:  ln0,30 = −n·ln2  ⇒  n = ln(1/0,30)/ln2.")),
               ("num", ("3.", "n = 1,204 / 0,693 ≈ 1,74  ⇒  t = n·T = 1,74 · 10.")),
               ("num", ("4.", "t ≈ 17,4 giờ.")),
               ("note", "Kiểm tra hợp lí: 30 % nằm giữa 50 % (sau 1T) và 25 % (sau 2T), "
                        "nên t phải nằm giữa 10 h và 20 h — kết quả 17,4 h là hợp lí.")],
              "t ≈ 17,4 giờ", sub="Bài 19")

    d.quiz("Kiểm tra nhanh",
           "Tăng nhiệt độ của một mẫu chất phóng xạ từ 20 °C lên 500 °C thì chu kì bán rã của nó "
           "thay đổi thế nào?",
           ["Giảm đi vì phân rã xảy ra nhanh hơn.", "Tăng lên vì các hạt nhân bị kích thích.",
            "Không thay đổi.", "Giảm đúng một nửa."],
           "C",
           "Phóng xạ là quá trình xảy ra bên trong HẠT NHÂN, hoàn toàn không phụ thuộc các tác động "
           "bên ngoài như nhiệt độ, áp suất hay trạng thái liên kết hoá học. "
           "Chu kì bán rã là hằng số đặc trưng của từng đồng vị.")

    d.wrapup("Tổng kết buổi 2",
             [("head", "Bốn ý phải nhớ"),
              ("b", "α là hạt ⁴₂He, β⁻ là electron, γ là sóng điện từ."),
              ("b", "Đâm xuyên α < β < γ; ion hoá α > β > γ."),
              ("b", "Viết phương trình phân rã bằng hai định luật bảo toàn A và Z."),
              ("b", "N = N₀·2⁻ⁿ với n = t/T; phóng xạ không phụ thuộc điều kiện bên ngoài.")],
             todo=["Làm Đề 3, 4, 5 – Chương 4.",
                   "Luyện 10 phương trình phân rã α và β.",
                   "Đọc trước bài Phản ứng hạt nhân."])


def buoi3(d):
    d.title_slide(
        sub="Buổi 3 — Phản ứng hạt nhân. Phân hạch và nhiệt hạch",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Viết được phương trình phản ứng hạt nhân và tính năng lượng toả ra",
                "Phân biệt rõ phân hạch và nhiệt hạch",
                "Giải thích được nguyên lí của nhà máy điện hạt nhân"])

    d.section(1, "Phản ứng hạt nhân", "Biến đổi hạt nhân này thành hạt nhân khác",
              items=["Định luật bảo toàn", "Năng lượng toả ra", "Phân hạch", "Nhiệt hạch"])

    d.content("Bốn định luật bảo toàn trong phản ứng hạt nhân",
              [("num", ("1.", "Bảo toàn SỐ KHỐI A (số nuclêôn) — tổng A trước bằng tổng A sau.")),
               ("num", ("2.", "Bảo toàn ĐIỆN TÍCH Z — tổng Z trước bằng tổng Z sau.")),
               ("num", ("3.", "Bảo toàn NĂNG LƯỢNG TOÀN PHẦN, kể cả năng lượng nghỉ.")),
               ("num", ("4.", "Bảo toàn ĐỘNG LƯỢNG.")),
               ("rule", None),
               ("head", "Hai đại lượng KHÔNG bảo toàn"),
               ("b", "Khối lượng nghỉ — chính phần chênh lệch này chuyển thành năng lượng toả ra."),
               ("b", "Số prôtôn và số nơtron riêng rẽ — chúng có thể chuyển hoá cho nhau, "
                     "chỉ tổng số nuclêôn mới bảo toàn."),
               ("note", "Bẫy rất hay gặp: “trong phản ứng hạt nhân, khối lượng được bảo toàn” — SAI. "
                        "Chỉ có số khối A mới bảo toàn, còn khối lượng nghỉ thì không.")],
              sub="Bài 20", tag="TRỌNG TÂM")

    d.formulas("Năng lượng của phản ứng hạt nhân",
               [(r"\Delta E = (m_{\mathrm{tr}} - m_{\mathrm{sau}})c^2",
                 "ΔE > 0: phản ứng TOẢ năng lượng;  ΔE < 0: phản ứng THU năng lượng."),
                (r"\Delta E = (\Delta m_{\mathrm{sau}} - \Delta m_{\mathrm{tr}})c^2",
                 "Cách tính theo độ hụt khối — tiện khi đề cho sẵn độ hụt khối của từng hạt nhân."),
                (r"\Delta E = W_{\mathrm{lk\,sau}} - W_{\mathrm{lk\,tr}}",
                 "Cách tính theo năng lượng liên kết — tiện khi đề cho năng lượng liên kết riêng.")],
               lead="Ba cách viết cho cùng một đại lượng; chọn cách phù hợp với dữ kiện đề cho.",
               foot="Với khối lượng tính bằng u, nhân kết quả với 931,5 để ra MeV. "
                    "Phản ứng toả năng lượng khi các hạt nhân sau BỀN VỮNG HƠN các hạt nhân trước.",
               tag="TRỌNG TÂM", sub="Bài 20")

    d.figure("Phản ứng phân hạch và phản ứng dây chuyền", "h_sd_phan_hach",
             items=[("head", "Cơ chế"),
                    ("b", "Một hạt nhân RẤT NẶNG (²³⁵U, ²³⁹Pu) hấp thụ một nơtron chậm rồi vỡ thành "
                          "hai hạt nhân trung bình, đồng thời phát ra 2–3 nơtron mới."),
                    ("b", "Các nơtron mới lại gây phân hạch tiếp ⇒ phản ứng DÂY CHUYỀN."),
                    ("gap", 0.05),
                    ("head", "Hệ số nhân nơtron k"),
                    ("sub", "k < 1: phản ứng tắt dần."),
                    ("sub", "k = 1: phản ứng duy trì ổn định — chế độ của lò phản ứng."),
                    ("sub", "k > 1: phản ứng bùng nổ không kiểm soát."),
                    ("note", "Mỗi phân hạch ²³⁵U toả khoảng 200 MeV — gấp hàng chục triệu lần "
                             "năng lượng của một phản ứng hoá học.")],
             cap="Sơ đồ phản ứng dây chuyền", tag="TRỌNG TÂM", figw=6.2)

    d.figure("Nhà máy điện hạt nhân", "h_sd_lo_phan_ung",
             items=[("head", "Chuỗi chuyển hoá năng lượng"),
                    ("p", "Năng lượng hạt nhân → nhiệt năng → cơ năng → điện năng."),
                    ("gap", 0.05),
                    ("head", "Vai trò từng bộ phận"),
                    ("kv", ("Chất làm chậm", "làm chậm nơtron để chúng dễ gây phân hạch (nước, than chì).")),
                    ("kv", ("Thanh điều khiển", "hấp thụ bớt nơtron để giữ k = 1 (bo, cađimi).")),
                    ("kv", ("Chất tải nhiệt", "mang nhiệt từ lò tới lò sinh hơi.")),
                    ("note", "Rút thanh điều khiển ra thì k tăng, đẩy vào thì k giảm — "
                             "đó là cách vận hành lò phản ứng.")],
             cap="Sơ đồ nguyên lí nhà máy điện hạt nhân", tag="ỨNG DỤNG", figw=6.0, side="left")

    d.figure("Phản ứng nhiệt hạch", "h_sd_nhiet_hach",
             items=[("head", "Cơ chế"),
                    ("b", "Hai hạt nhân RẤT NHẸ kết hợp thành một hạt nhân nặng hơn và toả năng lượng."),
                    ("b", "Điều kiện: nhiệt độ cỡ 10⁸ K để các hạt nhân có đủ động năng thắng "
                          "lực đẩy Cu-lông."),
                    ("gap", 0.05),
                    ("head", "Vì sao được quan tâm?"),
                    ("b", "Tính trên MỘT nuclêôn, nhiệt hạch toả nhiều năng lượng hơn phân hạch."),
                    ("b", "Nhiên liệu (đơteri) có sẵn trong nước biển, gần như vô tận."),
                    ("b", "Sản phẩm ít chất thải phóng xạ sống lâu."),
                    ("note", "Nhiệt hạch là nguồn năng lượng của Mặt Trời và các ngôi sao.")],
             cap="Phản ứng nhiệt hạch giữa đơteri và triti", tag="TRỌNG TÂM", figw=6.2)

    d.table("So sánh phân hạch và nhiệt hạch",
            ["Tiêu chí", "Phân hạch", "Nhiệt hạch"],
            [["Hạt nhân tham gia", "Rất nặng (A > 200)", "Rất nhẹ (A < 10)"],
             ["Quá trình", "Một hạt nhân VỠ thành hai", "Hai hạt nhân KẾT HỢP thành một"],
             ["Điều kiện xảy ra", "Nơtron chậm bắn vào", "Nhiệt độ cực cao ~10⁸ K"],
             ["Năng lượng mỗi phản ứng", "≈ 200 MeV", "≈ 17,6 MeV"],
             ["Năng lượng trên 1 nuclêôn", "≈ 0,85 MeV", "≈ 3,5 MeV — LỚN HƠN"],
             ["Đã điều khiển được chưa", "Rồi — nhà máy điện hạt nhân", "Chưa — còn đang nghiên cứu"],
             ["Chất thải phóng xạ", "Nhiều, sống lâu", "Ít hơn nhiều"]],
            widths=[1.4, 1.5, 1.5], pt=12, tag="SO SÁNH",
            foot="Bẫy kinh điển: “phân hạch toả nhiều năng lượng hơn nhiệt hạch”. "
                 "Đúng nếu tính MỖI PHẢN ỨNG, nhưng SAI nếu tính TRÊN MỘT NUCLÊÔN hoặc trên "
                 "một đơn vị khối lượng nhiên liệu. Đọc kĩ đề hỏi theo cách nào.")

    d.example("Ví dụ — Tính năng lượng toả ra",
              "Cho phản ứng nhiệt hạch  ²₁H + ³₁H → ⁴₂He + ¹₀n. "
              "Biết m(²H) = 2,0136 u; m(³H) = 3,0160 u; m(⁴He) = 4,0015 u; m(n) = 1,0087 u; "
              "1 u·c² = 931,5 MeV. Tính năng lượng toả ra của phản ứng.",
              [("num", ("1.", "Tổng khối lượng TRƯỚC:  2,0136 + 3,0160 = 5,0296 u.")),
               ("num", ("2.", "Tổng khối lượng SAU:  4,0015 + 1,0087 = 5,0102 u.")),
               ("num", ("3.", "Độ giảm khối lượng:  Δm = 5,0296 − 5,0102 = 0,0194 u.")),
               ("num", ("4.", "Năng lượng toả ra:  ΔE = 0,0194 · 931,5 ≈ 18,1 MeV.")),
               ("note", "Δm > 0 nên phản ứng TOẢ năng lượng. Nếu ra âm thì phản ứng thu năng lượng "
                        "và sẽ không tự xảy ra.")],
              "ΔE ≈ 18,1 MeV (toả năng lượng)", sub="Bài 20")

    d.quiz("Kiểm tra nhanh",
           "Phát biểu nào sau đây là SAI khi nói về phản ứng hạt nhân toả năng lượng?",
           ["Tổng khối lượng nghỉ của các hạt sau nhỏ hơn tổng khối lượng nghỉ của các hạt trước.",
            "Các hạt nhân sau phản ứng bền vững hơn các hạt nhân trước.",
            "Tổng khối lượng nghỉ được bảo toàn trong phản ứng.",
            "Tổng số nuclêôn trước và sau phản ứng bằng nhau."],
           "C",
           "Trong phản ứng hạt nhân, SỐ KHỐI và ĐIỆN TÍCH được bảo toàn, nhưng KHỐI LƯỢNG NGHỈ thì "
           "không. Chính phần khối lượng hụt đi đã chuyển thành năng lượng toả ra theo E = mc². "
           "Ba phát biểu còn lại đều đúng.")

    d.wrapup("Tổng kết buổi 3",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Bảo toàn A và Z; KHÔNG bảo toàn khối lượng nghỉ."),
              ("b", "ΔE = (m trước − m sau)·c²;  Δm > 0 thì toả năng lượng."),
              ("b", "Phân hạch: hạt nhân nặng vỡ ra, cần nơtron chậm, 200 MeV mỗi phản ứng."),
              ("b", "Nhiệt hạch: hạt nhân nhẹ kết hợp, cần nhiệt độ cực cao, toả nhiều hơn "
                    "TRÊN MỖI NUCLÊÔN.")],
             todo=["Làm Đề 6, 7, 8 – Chương 4.",
                   "Học thuộc bảng so sánh phân hạch – nhiệt hạch.",
                   "Đọc trước bài Ứng dụng và an toàn phóng xạ."])


def buoi4(d):
    d.title_slide(
        sub="Buổi 4 — Ứng dụng của đồng vị phóng xạ và an toàn bức xạ",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được các ứng dụng của đồng vị phóng xạ trong y học, công nghiệp, khảo cổ",
                "Giải được bài toán xác định tuổi bằng cacbon-14",
                "Nêu được ba nguyên tắc an toàn bức xạ"])

    d.section(1, "Ứng dụng của đồng vị phóng xạ", "Từ bệnh viện tới bảo tàng",
              items=["Y học", "Công nghiệp", "Khảo cổ và nông nghiệp"])

    d.figure("Ba lĩnh vực ứng dụng chính", "h_sd_ung_dung",
             items=[("head", "Nguyên tắc chọn đồng vị"),
                    ("b", "Loại tia phải phù hợp: cần đâm xuyên thì chọn γ, cần tác dụng nông "
                          "thì chọn β."),
                    ("b", "Chu kì bán rã phải phù hợp: quá ngắn thì hết trước khi dùng, "
                          "quá dài thì tồn lưu gây hại."),
                    ("gap", 0.05),
                    ("note", "Ví dụ: đồng vị dùng trong chẩn đoán hình ảnh thường có chu kì bán rã "
                             "chỉ vài giờ để nhanh chóng thải khỏi cơ thể bệnh nhân.")],
             cap="Ứng dụng của đồng vị phóng xạ", tag="THỰC TIỄN", figw=6.4)

    d.content("Hai ứng dụng cần hiểu sâu",
              [("head", "① Đo bề dày tấm kim loại bằng tia β"),
               ("b", "Nguồn β đặt một bên tấm kim loại, đầu dò đặt bên kia."),
               ("b", "Tấm càng dày thì cường độ tia β xuyên qua càng yếu."),
               ("b", "Máy tự động so sánh với giá trị chuẩn và điều chỉnh máy cán ngay lập tức."),
               ("gap", 0.06),
               ("head", "② Xạ trị ung thư bằng tia γ"),
               ("b", "Nguồn ⁶⁰Co phát tia γ có khả năng đâm xuyên lớn, tới được khối u nằm sâu."),
               ("b", "Chiếu từ nhiều hướng khác nhau, tất cả cùng hội tụ vào khối u: "
                     "mô lành chỉ nhận liều nhỏ, khối u nhận liều tổng cộng lớn."),
               ("note", "Cả hai ứng dụng đều dựa trên đúng một tính chất đã học: "
                        "khả năng đâm xuyên khác nhau của các loại tia.")],
              sub="Bài 21", tag="THỰC TIỄN")

    d.figure("Xác định tuổi bằng cacbon-14", "h_dt_c14",
             items=[("head", "Nguyên lí"),
                    ("num", ("1.", "Trong khí quyển, tỉ lệ ¹⁴C so với ¹²C gần như không đổi.")),
                    ("num", ("2.", "Sinh vật sống liên tục trao đổi chất nên giữ nguyên tỉ lệ đó.")),
                    ("num", ("3.", "Khi sinh vật chết, ¹⁴C không được bổ sung nữa mà chỉ phân rã dần.")),
                    ("num", ("4.", "Đo tỉ lệ ¹⁴C còn lại trong mẫu là suy ra được thời gian đã trôi qua.")),
                    ("note", "Chu kì bán rã của ¹⁴C là 5730 năm nên phương pháp này chỉ dùng tốt cho "
                             "mẫu vật dưới khoảng 50 000 năm tuổi.")],
             cap="Tỉ lệ cacbon-14 còn lại theo tuổi mẫu vật", tag="ỨNG DỤNG", figw=5.8, side="left")

    d.example("Ví dụ — Xác định tuổi mẫu gỗ cổ",
              "Một mẫu gỗ lấy từ di chỉ khảo cổ có độ phóng xạ của ¹⁴C bằng 25 % độ phóng xạ của một "
              "mẫu gỗ tươi cùng khối lượng. Chu kì bán rã của ¹⁴C là 5730 năm. Tính tuổi của mẫu gỗ.",
              [("num", ("1.", "Gỗ tươi có độ phóng xạ H₀; mẫu cổ có H = 0,25·H₀.")),
               ("num", ("2.", "Đặt n = t/T. Từ H = H₀·2⁻ⁿ  ⇒  2⁻ⁿ = 0,25.")),
               ("num", ("3.", "Vì 0,25 = 1/4 = 2⁻² nên n = 2.")),
               ("num", ("4.", "t = 2 · 5730 = 11 460 năm.")),
               ("note", "Nếu tỉ lệ không phải luỹ thừa đẹp của 2, hãy dùng "
                        "t = T·ln(H₀/H)/ln2.")],
              "Tuổi của mẫu gỗ ≈ 11 460 năm", sub="Bài 21")

    d.figure("Ba nguyên tắc an toàn bức xạ", "h_sd_an_toan",
             items=[("head", "Vì sao bức xạ nguy hiểm?"),
                    ("b", "Tia phóng xạ ion hoá các phân tử trong tế bào, có thể phá huỷ ADN, "
                          "gây ung thư hoặc đột biến."),
                    ("gap", 0.05),
                    ("head", "Ba biện pháp"),
                    ("sub", "THỜI GIAN — rút ngắn thời gian tiếp xúc."),
                    ("sub", "KHOẢNG CÁCH — liều chiếu giảm theo bình phương khoảng cách."),
                    ("sub", "CHE CHẮN — chọn vật liệu phù hợp với loại tia."),
                    ("note", "Đơn vị liều hấp thụ là gray (Gy); liều tương đương tính tới mức nguy hại "
                             "sinh học là sivơ (Sv).")],
             cap="Ba nguyên tắc bảo vệ khỏi bức xạ ion hoá", tag="AN TOÀN", figw=6.3)

    d.quiz("Kiểm tra nhanh",
           "Để kiểm tra bề dày của tấm thép mỏng đang cán liên tục trong nhà máy, nên chọn nguồn "
           "phóng xạ phát ra tia nào?",
           ["Tia α, vì ion hoá mạnh nhất.", "Tia β, vì bị hấp thụ vừa phải bởi tấm thép mỏng.",
            "Tia γ, vì xuyên qua hoàn toàn nên dễ đo.",
            "Loại tia nào cũng cho kết quả như nhau."],
           "B",
           "Tia α bị chặn ngay bởi tờ giấy nên không xuyên qua được thép. Tia γ xuyên qua gần như "
           "hoàn toàn nên cường độ hầu như không đổi khi bề dày thay đổi ít — không nhạy. "
           "Tia β bị hấp thụ một phần, cường độ xuyên qua nhạy với bề dày nên là lựa chọn đúng.")

    d.media("Tài nguyên trực quan nên dùng",
            [("Alpha Decay / Beta Decay", "PhET – phet.colorado.edu",
              "Quan sát hạt nhân tự phân rã và phát ra tia; đếm số hạt nhân còn lại theo thời gian.",
              "Phân rã là ngẫu nhiên với từng hạt nhân, nhưng quy luật thống kê thì rất chính xác."),
             ("Radioactive Dating Game", "PhET – phet.colorado.edu",
              "Đo tỉ lệ ¹⁴C của các mẫu vật ảo rồi đoán tuổi, máy chấm ngay.",
              "Cùng một chu kì bán rã mà tuổi mẫu vật khác nhau cho tỉ lệ rất khác nhau."),
             ("Phim tài liệu về chụp PET và xạ trị", "Kho tư liệu của bệnh viện hoặc VTV2",
              "Cho xem 3–4 phút quy trình chụp PET và quy trình xạ trị.",
              "Đồng vị phóng xạ được dùng có kiểm soát chặt chẽ, với liều tính toán chính xác.")])

    d.wrapup("Tổng kết buổi 4",
             [("head", "Ba ý phải nhớ"),
              ("b", "Chọn đồng vị theo LOẠI TIA và CHU KÌ BÁN RÃ phù hợp với mục đích."),
              ("b", "Xác định tuổi bằng ¹⁴C: t = T·ln(H₀/H)/ln2, với T = 5730 năm."),
              ("b", "Ba nguyên tắc an toàn: rút ngắn thời gian, tăng khoảng cách, che chắn.")],
             todo=["Làm Đề 9 – Chương 4.",
                   "Tìm hiểu thêm một ứng dụng của phóng xạ ở địa phương em.",
                   "Ôn toàn chương chuẩn bị buổi luyện tập."])


def buoi5(d):
    d.title_slide(
        sub="Buổi 5 — Luyện tập tổng hợp Chương IV",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Hệ thống toàn bộ công thức của chương",
                "Nhận dạng nhanh bốn dạng bài tập trọng tâm",
                "Tránh được các bẫy quen thuộc trong đề thi"])

    d.section(1, "Hệ thống công thức", "Toàn bộ chương gói trong một bảng",
              items=["Bảng công thức", "Bốn dạng bài tập", "Các bẫy thường gặp"])

    d.table("Tổng hợp công thức Chương IV",
            ["Nội dung", "Công thức", "Lưu ý"],
            [["Số nơtron", "N = A − Z", "Z là số prôtôn, A là số khối"],
             ["Độ hụt khối", "Δm = Z·m(p) + (A−Z)·m(n) − m(X)", "Δm luôn dương"],
             ["Năng lượng liên kết", "W(lk) = Δm·c² = Δm(u)·931,5 MeV", "Đổi u sang MeV bằng 931,5"],
             ["Năng lượng liên kết riêng", "ε = W(lk)/A", "Dùng ε để so sánh độ bền vững"],
             ["Định luật phóng xạ", "N = N₀·2⁻ⁿ  (n = t/T)", "Dạng tương đương: N = N₀·e mũ (−λt), λ = ln2/T"],
             ["Số hạt đã phân rã", "ΔN = N₀·(1 − 2⁻ⁿ)", "Đọc kĩ đề hỏi còn lại hay đã rã"],
             ["Độ phóng xạ", "H = λ·N = H₀·2⁻ⁿ", "Đơn vị becơren (Bq)"],
             ["Năng lượng phản ứng", "ΔE = (m trước − m sau)·c²", "ΔE > 0 là toả năng lượng"]],
            widths=[1.35, 1.8, 1.35], pt=11.5, tag="BẢNG CHỐT",
            foot="Thêm hai hằng số phải thuộc: Nₐ = 6,02·10²³ mol⁻¹ và 1 u = 1,66055·10⁻²⁷ kg.")

    d.example("Ví dụ 1 — Số hạt nhân trong một khối lượng",
              "Tính số hạt nhân có trong 2,0 g đồng vị ²³⁵U. "
              "Cho Nₐ = 6,02·10²³ mol⁻¹ và khối lượng mol của ²³⁵U là 235 g/mol.",
              [("num", ("1.", "Số mol:  n = m/M = 2,0/235 ≈ 8,51·10⁻³ mol.")),
               ("num", ("2.", "Số hạt nhân:  N = n·Nₐ = 8,51·10⁻³ · 6,02·10²³.")),
               ("num", ("3.", "N ≈ 5,12·10²¹ hạt.")),
               ("note", "Công thức gộp:  N = (m/A)·Nₐ, trong đó A là số khối "
                        "(về số trị bằng khối lượng mol tính theo g/mol).")],
              "N ≈ 5,12·10²¹ hạt nhân", sub="Luyện tập")

    d.example("Ví dụ 2 — Năng lượng toả ra từ một khối lượng nhiên liệu",
              "Mỗi phân hạch ²³⁵U toả ra 200 MeV. Tính năng lượng toả ra khi phân hạch hoàn toàn "
              "1,0 g ²³⁵U. Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
              [("num", ("1.", "Số hạt nhân trong 1,0 g:  N = (1,0/235)·6,02·10²³ ≈ 2,56·10²¹ hạt.")),
               ("num", ("2.", "Năng lượng theo MeV:  E = 2,56·10²¹ · 200 ≈ 5,12·10²³ MeV.")),
               ("num", ("3.", "Đổi sang jun:  E = 5,12·10²³ · 1,6·10⁻¹³ ≈ 8,2·10¹⁰ J.")),
               ("p", "Con số này tương đương năng lượng khi đốt khoảng 2,8 tấn than đá — "
                     "từ vỏn vẹn 1 gam urani.")],
              "E ≈ 8,2·10¹⁰ J", sub="Luyện tập")

    d.example("Ví dụ 3 — Tỉ số hạt nhân mẹ và hạt nhân con",
              "Một chất phóng xạ có chu kì bán rã T. Sau bao lâu thì số hạt nhân CON tạo thành "
              "gấp 7 lần số hạt nhân MẸ còn lại?",
              [("num", ("1.", "Gọi N₀ là số hạt nhân mẹ ban đầu, n = t/T; còn lại N = N₀·2⁻ⁿ.")),
               ("num", ("2.", "Mỗi hạt mẹ phân rã tạo ra một hạt con ⇒ số hạt con = N₀ − N.")),
               ("num", ("3.", "Điều kiện:  (N₀ − N)/N = 7  ⇒  N₀/N = 8.")),
               ("num", ("4.", "2ⁿ = 8 = 2³  ⇒  n = 3  ⇒  t = 3T.")),
               ("note", "Quy luật đáng nhớ: sau nT thì tỉ số con/mẹ bằng 2ⁿ − 1. "
                        "n = 1 cho 1:1; n = 2 cho 3:1; n = 3 cho 7:1; n = 4 cho 15:1.")],
              "t = 3T", sub="Luyện tập")

    d.table("Bốn dạng bài tập trọng tâm",
            ["Dạng", "Dấu hiệu nhận biết", "Cách xử lí"],
            [["Cấu tạo hạt nhân", "Hỏi số prôtôn, nơtron, electron",
              "Z là số prôtôn; N = A − Z"],
             ["Năng lượng liên kết", "Đề cho m(p), m(n), m(X)",
              "Tính Δm rồi nhân 931,5; chia A để có ε"],
             ["Định luật phóng xạ", "Đề cho chu kì bán rã T",
              "Viết N = N₀·2⁻ⁿ với n = t/T; nếu tỉ lệ đẹp thì n là số nguyên"],
             ["Phản ứng hạt nhân", "Có phương trình phản ứng",
              "Bảo toàn A và Z; ΔE = (m trước − m sau)·931,5"]],
            widths=[1.2, 1.6, 1.8], tag="PHÂN DẠNG",
            foot="Trong đề thi tốt nghiệp, Chương IV thường có 4–6 câu, "
                 "trong đó ít nhất một câu đúng/sai về phóng xạ hoặc năng lượng hạt nhân.")

    d.content("Bảy bẫy thường gặp của Chương IV",
              [("num", ("1.", "So sánh độ bền vững bằng W(lk) thay vì bằng ε = W(lk)/A.")),
               ("num", ("2.", "Nhầm số hạt CÒN LẠI với số hạt ĐÃ PHÂN RÃ.")),
               ("num", ("3.", "Cho rằng nhiệt độ hoặc áp suất làm thay đổi chu kì bán rã.")),
               ("num", ("4.", "Cho rằng khối lượng nghỉ được bảo toàn trong phản ứng hạt nhân.")),
               ("num", ("5.", "Kết luận phân hạch toả nhiều năng lượng hơn nhiệt hạch mà không xét "
                              "là tính trên mỗi phản ứng hay trên mỗi nuclêôn.")),
               ("num", ("6.", "Cho rằng tia α lệch nhiều hơn tia β trong điện trường "
                              "(thực ra α nặng hơn nên lệch ít hơn).")),
               ("num", ("7.", "Quên rằng tia γ không mang điện nên không lệch trong điện trường "
                              "và cả trong từ trường.")),
               ("note", "Mỗi bẫy trên đều đã từng xuất hiện trong đề thi chính thức hoặc đề tham khảo. "
                        "Hãy tự viết lại bảy dòng này vào sổ tay trước ngày thi.")],
              sub="Luyện tập", tag="CẢNH BÁO")

    d.quiz("Kiểm tra nhanh",
           "Ban đầu có một mẫu chất phóng xạ nguyên chất. Sau thời gian 2T, tỉ số giữa số hạt nhân "
           "đã bị phân rã và số hạt nhân còn lại là bao nhiêu?",
           ["1 : 1.", "2 : 1.", "3 : 1.", "4 : 1."],
           "C",
           "Sau 2T còn lại N = N₀/4, nên số hạt đã phân rã là N₀ − N₀/4 = 3N₀/4. "
           "Tỉ số bằng (3N₀/4) : (N₀/4) = 3 : 1. Công thức chung sau nT là (2ⁿ − 1) : 1.")

    d.wrapup("Tổng kết Chương IV",
             [("head", "Bản đồ kiến thức cả chương"),
              ("b", "Cấu trúc hạt nhân, đồng vị, đơn vị u."),
              ("b", "Độ hụt khối, năng lượng liên kết và năng lượng liên kết riêng."),
              ("b", "Phóng xạ: ba loại tia, quy tắc dịch chuyển, định luật phóng xạ."),
              ("b", "Phản ứng hạt nhân: phân hạch, nhiệt hạch và năng lượng toả ra."),
              ("b", "Ứng dụng và an toàn bức xạ.")],
             todo=["Làm trọn bộ 10 đề Chương 4.",
                   "Học thuộc bảng tổng hợp công thức và bảy bẫy thường gặp.",
                   "Bắt đầu làm 30 đề thi thử tổng hợp bốn chương."])


SPEC = [
    dict(file="C04_Buoi1_Cau_truc_hat_nhan_va_nang_luong_lien_ket.pptx",
         title="Cấu trúc hạt nhân. Độ hụt khối. Năng lượng liên kết",
         chapter=CH + " • Buổi 1", th=TH, slides=buoi1),
    dict(file="C04_Buoi2_Phong_xa_va_dinh_luat_phong_xa.pptx",
         title="Phóng xạ. Định luật phóng xạ",
         chapter=CH + " • Buổi 2", th=TH, slides=buoi2),
    dict(file="C04_Buoi3_Phan_ung_hat_nhan_phan_hach_nhiet_hach.pptx",
         title="Phản ứng hạt nhân. Phân hạch. Nhiệt hạch",
         chapter=CH + " • Buổi 3", th=TH, slides=buoi3),
    dict(file="C04_Buoi4_Ung_dung_va_an_toan_phong_xa.pptx",
         title="Ứng dụng của đồng vị phóng xạ. An toàn bức xạ",
         chapter=CH + " • Buổi 4", th=TH, slides=buoi4),
    dict(file="C04_Buoi5_Luyen_tap_tong_hop_chuong_IV.pptx",
         title="Luyện tập tổng hợp Chương IV",
         chapter=CH + " • Buổi 5", th=TH, slides=buoi5),
]
