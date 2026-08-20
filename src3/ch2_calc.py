# -*- coding: utf-8 -*-
"""Bài tập tính toán và suy luận - Chương II: KHÍ LÍ TƯỞNG.

Hằng số dùng thống nhất:
    R = 8,31 J/(mol·K)      N_A = 6,02·10²³ mol⁻¹      k_B = 1,38·10⁻²³ J/K
    1 atm = 1,013·10⁵ Pa = 76 cmHg          T(K) = t(°C) + 273
"""

D1 = "Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn"
D2 = "Dạng 2 – Câu trắc nghiệm đúng/sai"
D3 = "Dạng 3 – Câu trả lời ngắn"
D4 = "Dạng 4 – Bài tập tự luận và vận dụng cao"

CALC2 = {
    # =============================================================== DẠNG 1
    D1: [
        dict(q="Một lượng khí ở nhiệt độ không đổi có thể tích 6,0 L và áp suất 1,0·10⁵ Pa. "
               "Khi nén tới thể tích 2,0 L thì áp suất khí là",
             o=["3,0·10⁵ Pa.", "2,0·10⁵ Pa.", "0,33·10⁵ Pa.", "1,5·10⁵ Pa."],
             fig="h17_thi_nghiem_boyle",
             a="A",
             sol="Nhiệt độ không đổi nên áp dụng định luật Boyle: p₁V₁ = p₂V₂.\n"
                 "p₂ = p₁V₁/V₂ = 1,0·10⁵ · 6,0/2,0 = 3,0·10⁵ Pa."),

        dict(q="Một lượng khí ở 27 °C có thể tích 3,0 L. Nung nóng đẳng áp tới 127 °C thì thể "
               "tích khí là",
             o=["4,0 L.", "14,1 L.", "2,25 L.", "6,0 L."],
             a="A",
             sol="Đổi ra Kelvin: T₁ = 300 K, T₂ = 400 K.\n"
                 "Định luật Charles: V₂ = V₁·T₂/T₁ = 3,0 · 400/300 = 4,0 L.\n"
                 "Nếu dùng nhầm nhiệt độ Celsius sẽ được 3,0·127/27 ≈ 14,1 L — một sai lầm "
                 "rất phổ biến."),

        dict(q="Một bình kín chứa khí ở 27 °C, áp suất 1,5·10⁵ Pa. Nung bình tới 177 °C "
               "(thể tích bình không đổi). Áp suất khí khi đó là",
             o=["2,25·10⁵ Pa.", "9,83·10⁵ Pa.", "1,00·10⁵ Pa.", "3,00·10⁵ Pa."],
             a="A",
             sol="Đẳng tích: p₁/T₁ = p₂/T₂ với T₁ = 300 K, T₂ = 450 K.\n"
                 "p₂ = p₁·T₂/T₁ = 1,5·10⁵ · 450/300 = 2,25·10⁵ Pa."),

        dict(q="Một lượng khí có p₁ = 2,0·10⁵ Pa, V₁ = 4,0 L, T₁ = 300 K chuyển sang trạng "
               "thái có p₂ = 1,0·10⁵ Pa và T₂ = 450 K. Thể tích V₂ bằng",
             o=["12,0 L.", "8,0 L.", "6,0 L.", "5,3 L."],
             a="A",
             sol="Phương trình trạng thái: p₁V₁/T₁ = p₂V₂/T₂.\n"
                 "V₂ = p₁V₁T₂/(p₂T₁) = 2,0·4,0·450/(1,0·300) = 3600/300 = 12,0 L."),

        dict(q="Số mol khí chứa trong bình 8,31 L ở nhiệt độ 300 K và áp suất 1,0·10⁵ Pa là "
               "(R = 8,31 J/(mol·K))",
             o=["≈ 0,333 mol.", "≈ 3,33 mol.", "≈ 0,033 mol.", "≈ 1,00 mol."],
             a="A",
             sol="Đổi V = 8,31 L = 8,31·10⁻³ m³.\n"
                 "n = pV/(RT) = 1,0·10⁵ · 8,31·10⁻³/(8,31 · 300) = 831/2493 ≈ 0,333 mol."),

        dict(q="Động năng tịnh tiến trung bình của một phân tử khí ở 27 °C là "
               "(k_B = 1,38·10⁻²³ J/K)",
             o=["≈ 6,21·10⁻²¹ J.", "≈ 4,14·10⁻²¹ J.",
                "≈ 5,59·10⁻²¹ J.", "≈ 2,07·10⁻²¹ J."],
             a="A",
             sol="T = 300 K.\n"
                 "W̄ = (3/2)·k_B·T = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J.\n"
                 "Giá trị này không phụ thuộc loại khí."),

        dict(q="Tốc độ căn quân phương của phân tử khí oxygen (M = 32 g/mol) ở 27 °C là "
               "(R = 8,31 J/(mol·K))",
             o=["≈ 483 m/s.", "≈ 1367 m/s.", "≈ 153 m/s.", "≈ 15,3 m/s."],
             a="A",
             sol="Đổi M = 32 g/mol = 0,032 kg/mol; T = 300 K.\n"
                 "v_rms = √(3RT/M) = √(3 · 8,31 · 300/0,032) = √(7479/0,032) = √233 719 "
                 "≈ 483 m/s.\n"
                 "Lỗi hay gặp: để M ở đơn vị g/mol, khi đó kết quả sai lệch √1000 ≈ 31,6 lần."),

        dict(q="Một bình 20 L chứa khí ở áp suất 5,0·10⁵ Pa. Mở van cho khí thoát ra tới khi áp "
               "suất còn 2,0·10⁵ Pa, nhiệt độ giữ không đổi. Phần trăm số mol khí đã thoát ra là",
             o=["60 %.", "40 %.", "30 %.", "250 %."],
             a="A",
             sol="Bình có V và T không đổi nên từ pV = nRT, số mol n tỉ lệ thuận với p.\n"
                 "n₂/n₁ = p₂/p₁ = 2,0/5,0 = 0,40, tức còn lại 40 %.\n"
                 "Vậy đã thoát ra 100 % − 40 % = 60 %."),

        dict(q="Hai bình A và B nối nhau bằng ống có khoá. Bình A thể tích 3,0 L chứa khí ở áp "
               "suất 4,0·10⁵ Pa; bình B thể tích 5,0 L đã hút chân không. Mở khoá cho khí phân "
               "bố đều ở nhiệt độ không đổi. Áp suất cuối cùng là",
             o=["1,5·10⁵ Pa.", "2,4·10⁵ Pa.", "0,8·10⁵ Pa.", "2,0·10⁵ Pa."],
             a="A",
             sol="Lượng khí và nhiệt độ không đổi nên dùng định luật Boyle với thể tích tổng:\n"
                 "p₁V_A = p'·(V_A + V_B) → 4,0·10⁵ · 3,0 = p'·8,0 → p' = 1,2·10⁶/8,0 "
                 "= 1,5·10⁵ Pa.\n"
                 "Sai lầm hay gặp là chỉ lấy thể tích bình B, quên rằng khí chiếm cả hai bình."),

        dict(q="Khối lượng của 5,0 L khí nitrogen (M = 28 g/mol) ở 27 °C và áp suất "
               "2,0·10⁵ Pa là",
             o=["≈ 11,2 g.", "≈ 28,0 g.", "≈ 5,6 g.", "≈ 22,4 g."],
             a="A",
             sol="n = pV/(RT) = 2,0·10⁵ · 5,0·10⁻³/(8,31 · 300) = 1000/2493 ≈ 0,401 mol.\n"
                 "m = n·M = 0,401 · 28 ≈ 11,2 g."),

        dict(q="Một cột khí bị nhốt trong ống thẳng đứng miệng ở trên bởi cột thuỷ ngân cao "
               "15 cm. Áp suất khí quyển là 75 cmHg. Áp suất của cột khí là",
             o=["90 cmHg.", "60 cmHg.", "75 cmHg.", "15 cmHg."],
             a="A",
             sol="Cột thuỷ ngân nằm PHÍA TRÊN nên đè lên khối khí:\n"
                 "p = p₀ + h = 75 + 15 = 90 cmHg.\n"
                 "Nếu lật ngược ống cho miệng xuống dưới thì p = 75 − 15 = 60 cmHg."),

        dict(q="Ở cùng nhiệt độ, tỉ số tốc độ căn quân phương của phân tử hydrogen "
               "(M = 2 g/mol) và của phân tử oxygen (M = 32 g/mol) là",
             o=["4.", "16.", "1/4.", "√2."],
             a="A",
             sol="v_rms = √(3RT/M) nên ở cùng T, v tỉ lệ nghịch với √M.\n"
                 "v_H₂/v_O₂ = √(M_O₂/M_H₂) = √(32/2) = √16 = 4."),

        dict(q="Số phân tử khí chứa trong 2,0 L khí ở 27 °C và áp suất 1,0·10⁵ Pa là "
               "(k_B = 1,38·10⁻²³ J/K)",
             o=["≈ 4,83·10²².", "≈ 4,83·10²⁵.", "≈ 8,03·10⁻².", "≈ 1,21·10²³."],
             a="A",
             sol="Từ pV = N·k_B·T:\n"
                 "N = pV/(k_B·T) = 1,0·10⁵ · 2,0·10⁻³/(1,38·10⁻²³ · 300) = 200/(4,14·10⁻²¹) "
                 "≈ 4,83·10²² phân tử."),

        dict(q="Một khối khí lí tưởng có nhiệt độ 27 °C. Để tốc độ căn quân phương của phân tử "
               "tăng gấp ba lần thì nhiệt độ phải tăng tới",
             o=["2700 K.", "900 K.", "1200 K.", "81 K."],
             a="A",
             sol="Vì v_rms ∝ √T nên T₂/T₁ = (v₂/v₁)² = 3² = 9.\n"
                 "T₂ = 9 · 300 = 2700 K (tương ứng 2427 °C).\n"
                 "Đáp số 900 K ứng với việc chỉ nhân 3 mà quên bình phương."),

        dict(q="Một quả bóng thể tích 2,0 L chứa khí ở áp suất 1,2·10⁵ Pa và 27 °C được đưa "
               "xuống nước sâu, nơi áp suất là 3,0·10⁵ Pa và nhiệt độ 7 °C. Thể tích quả bóng "
               "khi đó là",
             o=["≈ 0,747 L.", "≈ 0,800 L.", "≈ 0,857 L.", "≈ 5,36 L."],
             a="A",
             sol="T₁ = 300 K, T₂ = 280 K.\n"
                 "V₂ = p₁V₁T₂/(p₂T₁) = 1,2 · 2,0 · 280/(3,0 · 300) = 672/900 ≈ 0,747 L.\n"
                 "Nếu chỉ dùng định luật Boyle mà bỏ qua nhiệt độ thì được 0,800 L."),

        dict(q="Áp suất của một khối khí có khối lượng riêng 1,25 kg/m³ và tốc độ căn quân "
               "phương 500 m/s là",
             o=["≈ 1,04·10⁵ Pa.", "≈ 3,13·10⁵ Pa.",
                "≈ 6,25·10² Pa.", "≈ 2,08·10⁵ Pa."],
             a="A",
             sol="p = (1/3)·ρ·v̄² với v̄² = v_rms² = 500² = 250 000 m²/s².\n"
                 "p = (1/3) · 1,25 · 250 000 = 312 500/3 ≈ 1,04·10⁵ Pa."),

        dict(q="Nén đẳng nhiệt một lượng khí làm thể tích giảm 40 %. Áp suất khí sẽ",
             o=["tăng khoảng 66,7 %.", "tăng 40 %.", "giảm 40 %.", "tăng 60 %."],
             a="A",
             sol="Gọi V₁ = V, khi giảm 40 % thì V₂ = 0,60V.\n"
                 "p₂ = p₁V₁/V₂ = p₁·V/(0,60V) = p₁/0,60 ≈ 1,667·p₁.\n"
                 "Vậy áp suất tăng khoảng 66,7 %, không phải 40 % — quan hệ tỉ lệ nghịch "
                 "không cho phép chuyển trực tiếp phần trăm."),

        dict(q="Trong một bình kín thể tích không đổi, người ta bơm thêm khí cho tới khi số mol "
               "tăng gấp rưỡi, đồng thời nhiệt độ tuyệt đối tăng gấp đôi. Áp suất khí trong "
               "bình sẽ",
             o=["tăng gấp 3 lần.", "tăng gấp 2 lần.", "tăng gấp 1,5 lần.", "tăng gấp 4 lần."],
             a="A",
             sol="Dùng pV = nRT với V không đổi: p tỉ lệ thuận với tích n·T.\n"
                 "p₂/p₁ = (n₂/n₁)·(T₂/T₁) = 1,5 · 2 = 3.\n"
                 "Bài này bắt buộc dùng pV = nRT vì lượng khí thay đổi, không dùng được "
                 "pV/T = hằng số."),
    ],

    # =============================================================== DẠNG 2
    D2: [
        dict(stem="Một lượng khí lí tưởng xác định được khảo sát trong hệ toạ độ (p, V) với bốn "
                  "trạng thái M(2 L; 3·10⁵ Pa), N(6 L; 1·10⁵ Pa), P(6 L; 3·10⁵ Pa) và "
                  "Q(2 L; 1·10⁵ Pa) như hình vẽ.",
             fig="h28_do_thi_pV_doc_hieu",
             items=[
                 ("Hai trạng thái M và N có cùng nhiệt độ.", True,
                  "Với cùng lượng khí, T tỉ lệ thuận với tích pV. "
                  "Tại M: 2·3 = 6; tại N: 6·1 = 6. Hai tích bằng nhau nên T_M = T_N, "
                  "và hai trạng thái này nằm trên cùng một đường đẳng nhiệt."),
                 ("Trạng thái P có nhiệt độ cao nhất trong bốn trạng thái.", True,
                  "Tích pV tại P là 6·3 = 18, lớn nhất trong bốn giá trị (6; 6; 18; 2), "
                  "nên P có nhiệt độ cao nhất."),
                 ("Quá trình đi từ Q tới N là quá trình đẳng nhiệt.", False,
                  "Tích pV tại Q là 2·1 = 2, còn tại N là 6·1 = 6, hai giá trị khác nhau nên "
                  "hai trạng thái có nhiệt độ khác nhau. Thực ra hai trạng thái này có cùng áp "
                  "suất 1·10⁵ Pa nên quá trình Q → N là ĐẲNG ÁP, và nhiệt độ tăng gấp ba lần."),
                 ("Nếu nhiệt độ ở trạng thái Q là 100 K thì nhiệt độ ở trạng thái P là 900 K.",
                  True,
                  "T tỉ lệ với pV: T_P/T_Q = 18/2 = 9, nên T_P = 9 · 100 = 900 K."),
             ]),

        dict(stem="Một bình thép kín dung tích 20 L chứa khí oxygen (M = 32 g/mol) ở nhiệt độ "
                  "27 °C và áp suất 4,0·10⁵ Pa. Cho R = 8,31 J/(mol·K).",
             items=[
                 ("Số mol khí trong bình xấp xỉ 3,21 mol.", True,
                  "n = pV/(RT) = 4,0·10⁵ · 20·10⁻³/(8,31 · 300) = 8000/2493 ≈ 3,209 mol."),
                 ("Khối lượng khí trong bình xấp xỉ 103 g.", True,
                  "m = n·M = 3,209 · 32 ≈ 102,7 g ≈ 103 g."),
                 ("Nếu nung bình lên 87 °C thì áp suất khí trở thành 4,8·10⁵ Pa.", True,
                  "Bình thép nên thể tích coi như không đổi, quá trình là đẳng tích. "
                  "T₂ = 87 + 273 = 360 K. p₂ = p₁·T₂/T₁ = 4,0·10⁵ · 360/300 = 4,8·10⁵ Pa."),
                 ("Nếu lấy ra một nửa khối lượng khí và giữ nhiệt độ 27 °C thì thể tích khí còn "
                  "lại trong bình giảm còn 10 L.", False,
                  "Khí luôn chiếm toàn bộ thể tích bình chứa, nên thể tích vẫn là 20 L. "
                  "Cái giảm một nửa là ÁP SUẤT, xuống còn 2,0·10⁵ Pa."),
             ]),

        dict(stem="Một xilanh nằm ngang có pit-tông mỏng, nhẹ, không ma sát, chia xilanh thành "
                  "hai ngăn A và B. Ban đầu mỗi ngăn có thể tích 300 cm³, chứa cùng một lượng "
                  "khí lí tưởng ở cùng nhiệt độ 300 K.",
             fig="h27_pit_tong_hai_ngan",
             items=[
                 ("Ban đầu áp suất của khí trong hai ngăn bằng nhau.", True,
                  "Pit-tông nhẹ, không ma sát và đang đứng yên nên hai lực áp lực từ hai phía "
                  "phải cân bằng: p_A·S = p_B·S, suy ra p_A = p_B."),
                 ("Nếu nung ngăn A lên 450 K và giữ ngăn B ở 300 K thì ở trạng thái cân bằng "
                  "mới, tỉ số thể tích V_A/V_B bằng 1,5.", True,
                  "Ở cân bằng mới p_A = p_B = p'. Với cùng số mol n cho mỗi ngăn: "
                  "p'V_A = nR·450 và p'V_B = nR·300. Chia hai vế: V_A/V_B = 450/300 = 1,5."),
                 ("Ở trạng thái cân bằng mới đó, thể tích ngăn A bằng 360 cm³.", True,
                  "Từ V_A/V_B = 1,5 và V_A + V_B = 600 cm³ (tổng thể tích không đổi): "
                  "1,5V_B + V_B = 600 → 2,5V_B = 600 → V_B = 240 cm³ và V_A = 360 cm³."),
                 ("Trong quá trình đó, áp suất trong ngăn B không thay đổi vì nhiệt độ ngăn B "
                  "giữ nguyên 300 K.", False,
                  "Ngăn B bị nén từ 300 cm³ xuống 240 cm³ ở nhiệt độ không đổi, nên theo định "
                  "luật Boyle áp suất TĂNG: p_B' = p_B·300/240 = 1,25·p_B. "
                  "Nhiệt độ không đổi chỉ có nghĩa là dùng được định luật Boyle, chứ không "
                  "có nghĩa áp suất giữ nguyên."),
             ]),

        dict(stem="Một nhóm học sinh khảo sát quá trình đẳng áp của một lượng khí bằng cách "
                  "nhúng ống nghiệm chứa khí (nút bằng giọt thuỷ ngân di động) vào nước ở các "
                  "nhiệt độ khác nhau và đo chiều dài cột khí, thu được bảng số liệu. "
                  "Tiết diện ống không đổi.",
             fig="h20_do_thi_charles",
             tbl=("Bảng số liệu thí nghiệm đẳng áp",
                  ["t (°C)", "0", "25", "50", "75", "100"],
                  [["ℓ (cm)", "10,0", "10,9", "11,8", "12,7", "13,7"]]),
             items=[
                 ("Thể tích khí tỉ lệ thuận với chiều dài cột khí vì tiết diện ống không đổi.",
                  True,
                  "V = S·ℓ với S không đổi, nên mọi kết luận về V đều có thể phát biểu qua ℓ."),
                 ("Tỉ số ℓ/t (với t tính bằng °C) là một hằng số.", False,
                  "Tại t = 0 °C, tỉ số này là phép chia cho 0 nên vô nghĩa. Tính thử ở hai điểm "
                  "khác: 10,9/25 = 0,436 còn 13,7/100 = 0,137, hoàn toàn khác nhau. "
                  "Quan hệ tỉ lệ thuận chỉ đúng với nhiệt độ TUYỆT ĐỐI."),
                 ("Tỉ số ℓ/T (với T tính bằng kelvin) gần như không đổi, xấp xỉ 0,0366 cm/K.",
                  True,
                  "10,0/273 = 0,0366; 10,9/298 = 0,0366; 11,8/323 = 0,0365; 12,7/348 = 0,0365; "
                  "13,7/373 = 0,0367. Các giá trị trùng nhau trong sai số phép đo, xác nhận "
                  "định luật Charles."),
                 ("Nếu vẽ đồ thị ℓ theo t (°C) và kéo dài đường thẳng về phía trái thì nó cắt "
                  "trục hoành tại khoảng −273 °C.", True,
                  "Hệ số góc của đồ thị: (13,7 − 10,0)/100 = 0,037 cm/°C, tung độ gốc 10,0 cm. "
                  "Đường thẳng cắt trục hoành khi 10,0 + 0,037·t = 0 → t ≈ −270 °C, "
                  "xấp xỉ −273 °C trong phạm vi sai số. Đây chính là cách lịch sử đã dẫn tới "
                  "khái niệm độ không tuyệt đối."),
             ]),

        dict(stem="Một bình khí nén y tế dung tích 50 L chứa oxygen ở áp suất 120 atm, "
                  "nhiệt độ 27 °C. Người ta dùng bình này để cung cấp oxygen cho bệnh nhân với "
                  "lưu lượng 3,0 L/phút ở áp suất 1,0 atm và cùng nhiệt độ. Bình được dùng cho "
                  "tới khi áp suất trong bình còn 10 atm.",
             fig="h25_bom_xe_va_binh_khi",
             items=[
                 ("Thể tích khí sử dụng được, quy về áp suất 1,0 atm, là 5500 L.", True,
                  "Phần khí lấy ra ứng với độ giảm áp suất (120 − 10) = 110 atm.\n"
                  "Quy về 1,0 atm ở cùng nhiệt độ: V = 110 · 50/1,0 = 5500 L."),
                 ("Thời gian sử dụng bình xấp xỉ 1833 phút, tức hơn 30 giờ.", True,
                  "t = 5500/3,0 ≈ 1833 phút ≈ 30,6 giờ."),
                 ("Nếu tính cả lượng khí còn lại trong bình ở 10 atm thì thời gian sử dụng là "
                  "6000 L chia cho 3,0 L/phút.", False,
                  "Phần khí ứng với 10 atm còn lại KHÔNG dùng được, vì khi áp suất trong bình "
                  "bằng áp suất làm việc thì khí không còn tự chảy ra nữa. Lấy 120·50/1,0 "
                  "= 6000 L là quên trừ phần khí dư này — đó là bẫy phổ biến nhất của dạng bài "
                  "bình khí nén."),
                 ("Nếu nhiệt độ phòng tăng lên thì áp suất trong bình chưa dùng sẽ tăng theo.",
                  True,
                  "Bình kín, thể tích không đổi nên đây là quá trình đẳng tích: p/T = hằng số. "
                  "Nhiệt độ tăng kéo theo áp suất tăng. Đó là lí do bình khí nén phải được bảo "
                  "quản nơi thoáng mát, tránh ánh nắng trực tiếp."),
             ]),

        dict(stem="Xét một khối khí lí tưởng gồm N phân tử ở nhiệt độ tuyệt đối T. "
                  "Cho k_B = 1,38·10⁻²³ J/K, R = 8,31 J/(mol·K), N_A = 6,02·10²³ mol⁻¹.",
             fig="h23_phan_bo_toc_do",
             items=[
                 ("Ở 300 K, động năng tịnh tiến trung bình của một phân tử là 6,21·10⁻²¹ J.",
                  True,
                  "W̄ = (3/2)k_B·T = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J."),
                 ("Ở 300 K, tốc độ căn quân phương của phân tử helium (M = 4 g/mol) xấp xỉ "
                  "1368 m/s.", True,
                  "v_rms = √(3RT/M) = √(3 · 8,31 · 300/0,004) = √(7479/0,004) = √1 869 750 "
                  "≈ 1367 m/s ≈ 1368 m/s."),
                 ("Khi nhiệt độ tăng từ 300 K lên 900 K, tốc độ căn quân phương tăng gấp ba "
                  "lần.", False,
                  "v_rms tỉ lệ với √T nên khi T tăng gấp ba thì v_rms chỉ tăng √3 ≈ 1,73 lần. "
                  "Muốn v_rms tăng gấp ba thì T phải tăng gấp chín lần."),
                 ("Ở cùng nhiệt độ, đường phân bố tốc độ của khí nhẹ nằm trải rộng hơn về phía "
                  "tốc độ lớn so với khí nặng.", True,
                  "Vì v_rms tỉ lệ nghịch với √M, khí nhẹ có tốc độ đặc trưng lớn hơn nên toàn bộ "
                  "đường phân bố dịch và trải về phía tốc độ lớn."),
             ]),
    ],

    # =============================================================== DẠNG 3
    D3: [
        dict(q="Một lượng khí ở nhiệt độ không đổi có áp suất 2,0·10⁵ Pa và thể tích 5,0 L. "
               "Khi thể tích tăng lên 8,0 L thì áp suất bằng bao nhiêu (theo 10⁵ Pa)? "
               "(Làm tròn đến hai chữ số thập phân.)",
             ans="1,25",
             sol="p₂ = p₁V₁/V₂ = 2,0 · 5,0/8,0 = 10/8,0 = 1,25 (đơn vị 10⁵ Pa)."),

        dict(q="Nung nóng đẳng áp một lượng khí từ 27 °C lên 327 °C. Thể tích khí tăng gấp "
               "bao nhiêu lần?",
             ans="2",
             sol="T₁ = 300 K, T₂ = 600 K.\n"
                 "V₂/V₁ = T₂/T₁ = 600/300 = 2 lần."),

        dict(q="Một bình kín chứa khí ở 300 K và 1,0·10⁵ Pa. Nung tới nhiệt độ bao nhiêu kelvin "
               "để áp suất đạt 2,5·10⁵ Pa?",
             ans="750",
             sol="Đẳng tích: T₂ = T₁·p₂/p₁ = 300 · 2,5/1,0 = 750 K."),

        dict(q="Tính số mol khí chứa trong bình 10 L ở 27 °C và áp suất 2,0·10⁵ Pa. "
               "Cho R = 8,31 J/(mol·K). (Làm tròn đến hai chữ số thập phân.)",
             ans="0,80",
             sol="n = pV/(RT) = 2,0·10⁵ · 10·10⁻³/(8,31 · 300) = 2000/2493 ≈ 0,802 ≈ 0,80 mol."),

        dict(q="Tính tốc độ căn quân phương (theo m/s) của phân tử khí hydrogen (M = 2 g/mol) "
               "ở 27 °C. Cho R = 8,31 J/(mol·K). (Làm tròn đến hàng đơn vị.)",
             ans="1934",
             sol="v_rms = √(3RT/M) = √(3 · 8,31 · 300/0,002) = √(7479/0,002) = √3 739 500 "
                 "≈ 1934 m/s."),

        dict(q="Một khối khí có p₁ = 3,0·10⁵ Pa, V₁ = 2,0 L, T₁ = 300 K. Sau khi biến đổi, "
               "khí có p₂ = 2,0·10⁵ Pa và V₂ = 4,5 L. Tính T₂ theo kelvin.",
             ans="450",
             sol="T₂ = T₁·p₂V₂/(p₁V₁) = 300 · (2,0 · 4,5)/(3,0 · 2,0) = 300 · 9,0/6,0 = 450 K."),

        dict(q="Một cột khí bị nhốt bởi cột thuỷ ngân cao 20 cm trong ống thẳng đứng miệng ở "
               "dưới. Áp suất khí quyển 76 cmHg. Tính áp suất cột khí theo cmHg.",
             ans="56",
             sol="Miệng ống ở dưới nên cột thuỷ ngân KÉO khối khí xuống:\n"
                 "p = p₀ − h = 76 − 20 = 56 cmHg."),

        dict(q="Tính động năng tịnh tiến trung bình của một phân tử khí ở 127 °C, theo đơn vị "
               "10⁻²¹ J. Cho k_B = 1,38·10⁻²³ J/K. (Làm tròn đến hai chữ số thập phân.)",
             ans="8,28",
             sol="T = 127 + 273 = 400 K.\n"
                 "W̄ = 1,5 · 1,38·10⁻²³ · 400 = 8,28·10⁻²¹ J."),

        dict(q="Một bình 4,0 L chứa khí ở áp suất 6,0·10⁵ Pa được nối với một bình 6,0 L đã hút "
               "chân không. Sau khi mở khoá và ở nhiệt độ không đổi, áp suất chung bằng bao "
               "nhiêu (theo 10⁵ Pa)? (Làm tròn đến hai chữ số thập phân.)",
             ans="2,40",
             sol="p' = p₁V₁/(V₁ + V₂) = 6,0 · 4,0/(4,0 + 6,0) = 24/10 = 2,40 (đơn vị 10⁵ Pa)."),

        dict(q="Khối lượng riêng của một khối khí là 1,2 kg/m³ và tốc độ căn quân phương của "
               "phân tử là 450 m/s. Tính áp suất khí theo 10⁴ Pa. "
               "(Làm tròn đến một chữ số thập phân.)",
             ans="8,1",
             sol="p = (1/3)·ρ·v̄² = (1/3) · 1,2 · 450² = (1/3) · 1,2 · 202 500 = 81 000 Pa "
                 "= 8,1·10⁴ Pa."),

        dict(q="Một lốp xe chứa khí ở 27 °C và áp suất 2,5·10⁵ Pa. Sau khi chạy đường dài, "
               "nhiệt độ khí trong lốp là 57 °C. Coi thể tích lốp không đổi, tính áp suất khí "
               "khi đó theo 10⁵ Pa. (Làm tròn đến hai chữ số thập phân.)",
             ans="2,75",
             sol="T₁ = 300 K, T₂ = 330 K. Đẳng tích: p₂ = p₁·T₂/T₁ = 2,5 · 330/300 = 2,75 "
                 "(đơn vị 10⁵ Pa)."),

        dict(q="Tính số phân tử khí trong 1,0 cm³ khí ở 27 °C và áp suất 1,0·10⁵ Pa, theo đơn "
               "vị 10¹⁹. Cho k_B = 1,38·10⁻²³ J/K. (Làm tròn đến một chữ số thập phân.)",
             ans="2,4",
             sol="V = 1,0 cm³ = 1,0·10⁻⁶ m³.\n"
                 "N = pV/(k_B·T) = 1,0·10⁵ · 1,0·10⁻⁶/(1,38·10⁻²³ · 300) = 0,1/(4,14·10⁻²¹) "
                 "≈ 2,42·10¹⁹ ≈ 2,4·10¹⁹ phân tử."),

        dict(q="Một bình kín thể tích không đổi chứa khí ở áp suất 8,0·10⁵ Pa. Người ta xả bớt "
               "khí ở nhiệt độ không đổi cho tới khi áp suất còn 3,0·10⁵ Pa. Bao nhiêu phần "
               "trăm số mol khí đã bị xả ra? (Làm tròn đến một chữ số thập phân.)",
             ans="62,5",
             sol="Với V và T không đổi, n tỉ lệ thuận với p.\n"
                 "Phần còn lại: 3,0/8,0 = 0,375 = 37,5 %. Phần đã xả: 100 − 37,5 = 62,5 %."),

        dict(q="Nén đẳng nhiệt một lượng khí làm áp suất tăng gấp 4 lần. Thể tích khí giảm bao "
               "nhiêu phần trăm so với ban đầu?",
             ans="75",
             sol="Từ p₁V₁ = p₂V₂ với p₂ = 4p₁: V₂ = V₁/4 = 0,25V₁.\n"
                 "Thể tích giảm đi V₁ − 0,25V₁ = 0,75V₁, tức 75 %."),
    ],

    # =============================================================== DẠNG 4
    D4: [
        dict(q="Một xilanh thẳng đứng, miệng hướng lên, được đậy bởi một pit-tông khối lượng "
               "2,0 kg, tiết diện 50 cm², có thể trượt không ma sát. Bên dưới pit-tông là cột "
               "khí lí tưởng dài 20 cm ở nhiệt độ 27 °C. Áp suất khí quyển là 1,0·10⁵ Pa, "
               "g = 10 m/s².\n"
               "a) Tính áp suất của khí trong xilanh.\n"
               "b) Nung khí lên 87 °C, pit-tông tự do dịch chuyển. Tính chiều dài cột khí mới.\n"
               "c) Nếu thay vì để pit-tông tự do, ta giữ chặt nó rồi nung lên 87 °C thì áp suất "
               "khí bằng bao nhiêu?\n"
               "d) Lật ngược xilanh cho miệng hướng xuống, giữ nhiệt độ 27 °C. Tính chiều dài "
               "cột khí.",
             ans="a) 1,04·10⁵ Pa   b) 24 cm   c) ≈ 1,248·10⁵ Pa   d) ≈ 21,7 cm",
             sol="a) Pit-tông cân bằng: áp lực khí từ dưới cân bằng với áp lực khí quyển và "
                 "trọng lượng pit-tông.\n"
                 "p = p₀ + mg/S = 1,0·10⁵ + (2,0 · 10)/(50·10⁻⁴) = 1,0·10⁵ + 20/0,005 "
                 "= 1,0·10⁵ + 4000 = 1,04·10⁵ Pa.\n\n"
                 "b) Pit-tông tự do nên áp suất giữ nguyên 1,04·10⁵ Pa: đây là quá trình ĐẲNG ÁP. "
                 "Vì tiết diện không đổi, ℓ tỉ lệ với V:\n"
                 "ℓ₂ = ℓ₁·T₂/T₁ = 20 · 360/300 = 24 cm.\n\n"
                 "c) Giữ chặt pit-tông thì thể tích không đổi: quá trình ĐẲNG TÍCH.\n"
                 "p₂ = p₁·T₂/T₁ = 1,04·10⁵ · 360/300 = 1,248·10⁵ Pa.\n\n"
                 "d) Lật ngược, pit-tông nằm dưới cột khí và trọng lượng của nó kéo xuống:\n"
                 "p' = p₀ − mg/S = 1,0·10⁵ − 4000 = 0,96·10⁵ Pa.\n"
                 "Nhiệt độ không đổi nên dùng định luật Boyle: p·ℓ = p'·ℓ“\n"
                 "ℓ” = 1,04·10⁵ · 20/(0,96·10⁵) = 2,08·10⁶/0,96·10⁵ ≈ 21,7 cm.\n"
                 "Cột khí dài ra vì áp suất tác dụng lên nó đã giảm."),

        dict(q="Một ống thuỷ tinh hình trụ dài 100 cm, một đầu kín, đặt thẳng đứng miệng hướng "
               "lên. Trong ống có một cột thuỷ ngân dài 20 cm nhốt một cột khí dài 40 cm ở "
               "nhiệt độ 27 °C. Áp suất khí quyển là 76 cmHg.\n"
               "a) Tính áp suất cột khí bị nhốt.\n"
               "b) Lật ngược ống cho miệng hướng xuống, giữ nguyên nhiệt độ. Tính chiều dài "
               "cột khí mới và kiểm tra xem thuỷ ngân có bị tràn ra không.\n"
               "c) Trở lại tư thế ban đầu rồi nung khí lên 87 °C. Tính chiều dài cột khí.\n"
               "d) Nêu điều kiện để khi lật ngược ống, thuỷ ngân bắt đầu bị tràn ra ngoài.",
             fig="h24_ong_chu_U",
             ans="a) 96 cmHg   b) ≈ 68,6 cm, không tràn   c) 48 cm",
             sol="a) Cột thuỷ ngân nằm trên khối khí nên đè xuống:\n"
                 "p₁ = p₀ + h = 76 + 20 = 96 cmHg.\n\n"
                 "b) Lật ngược, thuỷ ngân nằm dưới khối khí và kéo xuống:\n"
                 "p₂ = p₀ − h = 76 − 20 = 56 cmHg.\n"
                 "Định luật Boyle (tiết diện không đổi nên dùng chiều dài thay thể tích):\n"
                 "ℓ₂ = p₁ℓ₁/p₂ = 96 · 40/56 = 3840/56 ≈ 68,6 cm.\n"
                 "Kiểm tra: tổng chiều dài cần thiết là 68,6 + 20 = 88,6 cm < 100 cm, "
                 "vẫn còn 11,4 cm ống trống nên thuỷ ngân KHÔNG tràn ra.\n\n"
                 "c) Ở tư thế ban đầu, cột thuỷ ngân vẫn nằm trên nên áp suất giữ nguyên "
                 "96 cmHg — đây là quá trình ĐẲNG ÁP:\n"
                 "ℓ₃ = ℓ₁·T₂/T₁ = 40 · 360/300 = 48 cm.\n"
                 "Kiểm tra: 48 + 20 = 68 cm < 100 cm, hợp lệ.\n\n"
                 "d) Thuỷ ngân bắt đầu tràn khi cột khí dãn tới mức ℓ₂ + h = L, tức "
                 "ℓ₂ = L − h = 100 − 20 = 80 cm. Điều kiện: p₁ℓ₁/(p₀ − h) ≥ L − h. "
                 "Với bài này 68,6 < 80 nên chưa tràn. Nếu cột thuỷ ngân dài hơn hoặc cột khí "
                 "ban đầu dài hơn thì có thể xảy ra tràn, khi đó lượng thuỷ ngân giảm đi và "
                 "phải giải lại với h mới."),

        dict(q="Một bóng thám không có vỏ mềm, ở mặt đất chứa 8,0 m³ khí helium ở áp suất "
               "1,0·10⁵ Pa và nhiệt độ 27 °C. Vỏ bóng chỉ chịu được thể tích tối đa 30 m³.\n"
               "a) Ở độ cao nơi áp suất là 0,50·10⁵ Pa và nhiệt độ −3 °C, thể tích bóng bằng "
               "bao nhiêu?\n"
               "b) Ở độ cao nơi áp suất là 0,25·10⁵ Pa và nhiệt độ −33 °C, bóng có bị vỡ không?\n"
               "c) Xác định áp suất tại độ cao mà bóng bắt đầu vỡ, giả sử nhiệt độ tại đó là "
               "−53 °C.\n"
               "d) Giải thích vì sao bóng thám không không được bơm căng ngay từ mặt đất.",
             ans="a) ≈ 14,4 m³   b) chưa vỡ, vì V ≈ 25,6 m³ < 30 m³   c) ≈ 0,196·10⁵ Pa",
             sol="a) T₁ = 300 K, T₂ = 270 K.\n"
                 "V₂ = p₁V₁T₂/(p₂T₁) = 1,0 · 8,0 · 270/(0,50 · 300) = 2160/150 = 14,4 m³.\n\n"
                 "b) T₃ = 240 K.\n"
                 "V₃ = 1,0 · 8,0 · 240/(0,25 · 300) = 1920/75 = 25,6 m³.\n"
                 "Vì 25,6 m³ < 30 m³ nên bóng CHƯA vỡ.\n\n"
                 "c) Bóng vỡ khi V = 30 m³ ở T = 220 K:\n"
                 "p = p₁V₁T/(V·T₁) = 1,0 · 8,0 · 220/(30 · 300) = 1760/9000 ≈ 0,196·10⁵ Pa.\n\n"
                 "d) Vì càng lên cao áp suất khí quyển càng giảm mạnh, khí trong bóng nở ra rất "
                 "nhiều. Nếu bơm căng ngay từ mặt đất thì bóng sẽ vỡ ở độ cao thấp. "
                 "Bơm ít khí để bóng còn nhăn cho phép nó nở dần theo độ cao mà không vượt quá "
                 "thể tích giới hạn của vỏ, nhờ đó đạt được độ cao lớn hơn nhiều."),

        dict(q="Một bình kín dung tích 10 L chứa khí ở 27 °C và áp suất 1,0·10⁵ Pa.\n"
               "a) Tính số mol và số phân tử khí trong bình.\n"
               "b) Người ta bơm thêm khí cùng loại vào bình cho tới khi áp suất đạt "
               "3,0·10⁵ Pa ở cùng nhiệt độ. Tính số mol khí đã bơm thêm.\n"
               "c) Sau đó nung bình lên 127 °C. Tính áp suất khí.\n"
               "d) Bình chỉ chịu được áp suất tối đa 5,0·10⁵ Pa. Tính nhiệt độ tối đa cho phép.",
             ans="a) ≈ 0,401 mol và ≈ 2,41·10²³ phân tử   b) ≈ 0,802 mol   "
                 "c) 4,0·10⁵ Pa   d) 500 K (227 °C)",
             sol="a) n₁ = pV/(RT) = 1,0·10⁵ · 10·10⁻³/(8,31 · 300) = 1000/2493 ≈ 0,401 mol.\n"
                 "N = n·N_A = 0,401 · 6,02·10²³ ≈ 2,41·10²³ phân tử.\n\n"
                 "b) Với V và T không đổi, n tỉ lệ thuận với p. Áp suất tăng gấp ba nên số mol "
                 "cũng tăng gấp ba: n₂ = 3 · 0,401 ≈ 1,203 mol.\n"
                 "Số mol bơm thêm: Δn = 1,203 − 0,401 ≈ 0,802 mol.\n\n"
                 "c) Bây giờ lượng khí không đổi, thể tích không đổi: quá trình đẳng tích.\n"
                 "p = 3,0·10⁵ · 400/300 = 4,0·10⁵ Pa.\n\n"
                 "d) Vẫn đẳng tích, xuất phát từ 3,0·10⁵ Pa ở 300 K:\n"
                 "T_max = 300 · 5,0/3,0 = 500 K, tức 227 °C."),

        dict(q="Một lượng khí lí tưởng thực hiện chu trình khép kín gồm ba giai đoạn: "
               "(1)→(2) đẳng tích giảm áp từ 3,0 atm xuống 1,0 atm với V = 2,0 L; "
               "(2)→(3) đẳng áp dãn nở tới 6,0 L; (3)→(1) đẳng nhiệt. Biết T₁ = 600 K.\n"
               "a) Lập bảng ba thông số p, V, T cho ba trạng thái.\n"
               "b) Chứng minh rằng giai đoạn (3)→(1) thực sự là đẳng nhiệt.\n"
               "c) Vẽ phác chu trình trong hệ (V, T), đánh dấu chiều diễn biến.\n"
               "d) Trong giai đoạn nào khí sinh công, giai đoạn nào khí nhận công? Giải thích.",
             fig="h22_chu_trinh_pV",
             ans="a) (1): 3,0 atm – 2,0 L – 600 K; (2): 1,0 atm – 2,0 L – 200 K; "
                 "(3): 1,0 atm – 6,0 L – 600 K",
             sol="a) Trạng thái (1): p₁ = 3,0 atm, V₁ = 2,0 L, T₁ = 600 K.\n"
                 "Trạng thái (2): đẳng tích nên V₂ = 2,0 L, p₂ = 1,0 atm, "
                 "T₂ = T₁·p₂/p₁ = 600/3 = 200 K.\n"
                 "Trạng thái (3): đẳng áp nên p₃ = 1,0 atm, V₃ = 6,0 L, "
                 "T₃ = T₂·V₃/V₂ = 200 · 3 = 600 K.\n\n"
                 "b) Cách 1: T₃ = 600 K = T₁, hai trạng thái cùng nhiệt độ.\n"
                 "Cách 2 (nhanh hơn): so sánh tích pV. Tại (1): 3,0 · 2,0 = 6,0; "
                 "tại (3): 1,0 · 6,0 = 6,0. Hai tích bằng nhau nên cùng nhiệt độ, và đoạn nối "
                 "chúng có thể là một cung hypebol đẳng nhiệt.\n\n"
                 "c) Trong hệ (V, T) với trục hoành T, trục tung V:\n"
                 "• (1)→(2): V không đổi bằng 2,0 L, T giảm từ 600 K xuống 200 K → đoạn NẰM "
                 "NGANG đi sang trái.\n"
                 "• (2)→(3): đẳng áp, V/T = hằng số → đoạn thẳng ĐI QUA GỐC toạ độ, từ "
                 "(200 K; 2,0 L) tới (600 K; 6,0 L), hướng lên phải.\n"
                 "• (3)→(1): T không đổi bằng 600 K, V giảm từ 6,0 L xuống 2,0 L → đoạn THẲNG "
                 "ĐỨNG đi xuống.\n"
                 "Nhớ đánh mũi tên trên từng đoạn; quên mũi tên là lỗi mất điểm phổ biến.\n\n"
                 "d) Công trao đổi gắn với sự thay đổi thể tích:\n"
                 "• (1)→(2): V không đổi nên khí không trao đổi công, A = 0.\n"
                 "• (2)→(3): V tăng từ 2,0 L lên 6,0 L, khí dãn nở đẩy pit-tông nên khí SINH "
                 "công (A < 0).\n"
                 "• (3)→(1): V giảm từ 6,0 L xuống 2,0 L, khí bị nén nên khí NHẬN công (A > 0). "
                 "Vì đây là đẳng nhiệt của khí lí tưởng nên ΔU = 0, toàn bộ công nhận vào được "
                 "toả ra dưới dạng nhiệt."),

        dict(q="Hai bình giống hệt nhau, mỗi bình dung tích 5,0 L, được nối với nhau bằng một "
               "ống nhỏ có khoá (bỏ qua thể tích ống). Ban đầu khoá đóng, cả hai bình chứa cùng "
               "một loại khí ở 27 °C và áp suất 2,0·10⁵ Pa.\n"
               "a) Tính tổng số mol khí trong hai bình.\n"
               "b) Giữ khoá đóng, nung bình A lên 127 °C, bình B vẫn ở 27 °C. Tính áp suất mỗi "
               "bình.\n"
               "c) Mở khoá, giữ nguyên nhiệt độ mỗi bình như ở câu b. Tính áp suất chung.\n"
               "d) Sau khi mở khoá, số mol khí trong mỗi bình bằng bao nhiêu? Nhận xét.",
             ans="a) ≈ 0,802 mol   b) p_A ≈ 2,67·10⁵ Pa, p_B = 2,0·10⁵ Pa   "
                 "c) ≈ 2,29·10⁵ Pa   d) n_A ≈ 0,344 mol, n_B ≈ 0,459 mol",
             sol="a) Mỗi bình: n = pV/(RT) = 2,0·10⁵ · 5,0·10⁻³/(8,31 · 300) = 1000/2493 "
                 "≈ 0,401 mol.\n"
                 "Tổng: n_tổng ≈ 0,802 mol.\n\n"
                 "b) Khoá đóng nên mỗi bình là một hệ kín thể tích không đổi (đẳng tích):\n"
                 "p_A = 2,0·10⁵ · 400/300 ≈ 2,67·10⁵ Pa; p_B giữ nguyên 2,0·10⁵ Pa.\n\n"
                 "c) Mở khoá, áp suất hai bình bằng nhau (gọi là p') nhưng nhiệt độ vẫn khác "
                 "nhau. Bảo toàn tổng số mol:\n"
                 "p'V/(R·400) + p'V/(R·300) = 0,802\n"
                 "p'·(5,0·10⁻³/8,31)·(1/400 + 1/300) = 0,802\n"
                 "p'·6,017·10⁻⁴·(0,0025 + 0,003333) = 0,802\n"
                 "p'·6,017·10⁻⁴·5,8333·10⁻³ = 0,802\n"
                 "p'·3,510·10⁻⁶ = 0,802 → p' ≈ 2,285·10⁵ Pa ≈ 2,29·10⁵ Pa.\n\n"
                 "d) n_A = p'V/(R·400) = 2,285·10⁵ · 5,0·10⁻³/(8,31 · 400) = 1142,5/3324 "
                 "≈ 0,344 mol.\n"
                 "n_B = 2,285·10⁵ · 5,0·10⁻³/(8,31 · 300) = 1142,5/2493 ≈ 0,458 mol.\n"
                 "Tổng ≈ 0,802 mol, đúng như bảo toàn.\n"
                 "Nhận xét: khí tự động dồn về phía bình LẠNH. Điều này hợp lí vì ở cùng áp "
                 "suất, bình lạnh hơn chứa được nhiều mol hơn (n tỉ lệ nghịch với T)."),
    ],
}
