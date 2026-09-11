# -*- coding: utf-8 -*-
"""SLIDE BÀI GIẢNG — CHƯƠNG III: TỪ TRƯỜNG.  Năm buổi dạy."""
from deck import Deck

TH = 3
CH = "Chương III – Từ trường"
MT = "Ôn thi tốt nghiệp THPT 2026  •  Lớp 12"


def buoi1(d):
    d.title_slide(
        sub="Buổi 1 — Từ trường. Đường sức từ. Từ trường Trái Đất",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Nêu được từ trường tồn tại ở đâu và được nhận biết bằng cách nào",
                "Vẽ được đường sức từ của nam châm thẳng, dây dẫn thẳng và ống dây",
                "Vận dụng được quy tắc nắm tay phải"])

    d.section(1, "Từ trường và đường sức từ", "Trường tồn tại quanh nam châm và quanh dòng điện",
              items=["Từ trường là gì", "Cảm ứng từ – đại lượng đặc trưng", "Đường sức từ"])

    d.content("Từ trường tồn tại ở đâu?",
              [("head", "Định nghĩa"),
               ("p", "Từ trường là dạng vật chất tồn tại xung quanh nam châm và xung quanh dòng điện, "
                     "tác dụng lực từ lên nam châm khác hoặc lên dòng điện khác đặt trong nó."),
               ("gap", 0.06),
               ("head", "Hai nguồn sinh ra từ trường"),
               ("b", "Nam châm vĩnh cửu."),
               ("b", "Dòng điện — tức các điện tích chuyển động."),
               ("gap", 0.06),
               ("head", "Cách nhận biết"),
               ("b", "Đặt một kim nam châm thử: nếu kim bị lệch khỏi hướng ban đầu thì nơi đó có từ trường."),
               ("b", "Hướng của từ trường tại một điểm là hướng NAM – BẮC của kim nam châm thử "
                     "nằm cân bằng tại điểm đó."),
               ("note", "Bản chất thống nhất: nam châm vĩnh cửu cũng sinh từ trường nhờ chuyển động "
                        "của electron bên trong nó. Mọi từ trường đều do điện tích chuyển động.")],
              sub="Bài 14 — Từ trường", tag="LÍ THUYẾT")

    d.content("Cảm ứng từ — đại lượng đặc trưng cho từ trường",
              [("head", "Vectơ cảm ứng từ B"),
               ("kv", ("Điểm đặt", "tại điểm ta đang xét.")),
               ("kv", ("Phương", "trùng với trục của kim nam châm thử nằm cân bằng tại đó.")),
               ("kv", ("Chiều", "từ cực NAM sang cực BẮC của kim nam châm thử.")),
               ("kv", ("Độ lớn", "đặc trưng cho độ mạnh của từ trường tại điểm đó.")),
               ("gap", 0.05),
               ("head", "Đơn vị"),
               ("b", "Tesla (T). Từ trường Trái Đất cỡ 5·10⁻⁵ T; nam châm tủ lạnh cỡ 5·10⁻³ T; "
                     "máy chụp cộng hưởng từ trong bệnh viện tới 1,5 – 3 T."),
               ("note", "Từ trường ĐỀU là từ trường mà vectơ B tại mọi điểm đều có cùng phương, "
                        "chiều và độ lớn — đường sức là những đường thẳng song song, cách đều.")],
              sub="Bài 14 — Cảm ứng từ", tag="ĐỊNH NGHĨA")

    d.figure("Đường sức từ của nam châm thẳng", "t_sd_duongsuc_ncthang",
             items=[("head", "Bốn tính chất của đường sức từ"),
                    ("num", ("1.", "Qua mỗi điểm chỉ vẽ được MỘT đường sức từ.")),
                    ("num", ("2.", "Đường sức từ là những đường cong KHÉP KÍN hoặc vô hạn ở hai đầu — "
                                   "khác hẳn đường sức điện.")),
                    ("num", ("3.", "Bên ngoài nam châm, đường sức đi RA từ cực Bắc và đi VÀO cực Nam.")),
                    ("num", ("4.", "Nơi từ trường mạnh thì đường sức vẽ MAU (dày), nơi yếu thì vẽ THƯA.")),
                    ("note", "Trong lòng nam châm, đường sức đi từ cực Nam sang cực Bắc, khép kín "
                             "đường đi bên ngoài.")],
             cap="Từ phổ và đường sức từ của nam châm thẳng", tag="TRỌNG TÂM", figw=5.8)

    d.figure("Từ trường của dòng điện thẳng dài", "t_sd_duongsuc_daythang",
             items=[("head", "Quy tắc nắm tay phải"),
                    ("p", "Nắm bàn tay phải, ngón cái choãi ra chỉ chiều dòng điện; bốn ngón khum lại "
                          "chỉ chiều của đường sức từ."),
                    ("gap", 0.05),
                    ("head", "Đặc điểm"),
                    ("b", "Đường sức là những đường tròn đồng tâm nằm trong mặt phẳng vuông góc với dây."),
                    ("b", "Càng xa dây, đường tròn càng thưa: từ trường yếu dần theo 1/r."),
                    ("note", "Ký hiệu quy ước: dấu × là vectơ hướng vào trong trang giấy (nhìn thấy "
                             "đuôi mũi tên); dấu chấm là hướng ra ngoài trang giấy (nhìn thấy đầu mũi tên).")],
             cap="Đường sức từ quanh dòng điện thẳng", tag="TRỌNG TÂM", figw=5.5, side="left")

    d.figure("Từ trường trong lòng ống dây", "t_sd_ongday",
             items=[("head", "Đặc điểm quan trọng"),
                    ("b", "Trong lòng ống dây đủ dài, từ trường gần như ĐỀU: đường sức song song và "
                          "cách đều nhau."),
                    ("b", "Ống dây có dòng điện hoạt động hệt như một nam châm thẳng: một đầu là cực "
                          "Bắc, đầu kia là cực Nam."),
                    ("b", "Xác định cực bằng quy tắc nắm tay phải: khum bốn ngón theo chiều dòng điện "
                          "trong các vòng dây, ngón cái chỉ về phía cực BẮC."),
                    ("note", "Đây là nguyên lí của nam châm điện: ngắt dòng thì từ tính biến mất, "
                             "đảo chiều dòng thì hai cực đổi chỗ.")],
             cap="Ống dây có dòng điện chạy qua", tag="ỨNG DỤNG", figw=6.0)

    d.figure("Từ trường Trái Đất", "t_sd_tutruong_traidat",
             items=[("head", "Ba điều cần nhớ"),
                    ("b", "Trái Đất hoạt động như một nam châm khổng lồ; cực NAM từ nằm gần cực BẮC địa lí."),
                    ("b", "Vì thế đầu Bắc của kim la bàn — vốn bị hút bởi cực Nam từ — chỉ về hướng "
                          "Bắc địa lí."),
                    ("b", "Trục từ lệch khoảng 11,5° so với trục quay, gây ra hiện tượng ĐỘ TỪ THIÊN."),
                    ("note", "Từ trường Trái Đất chắn phần lớn hạt mang điện từ Mặt Trời; "
                             "phần lọt vào vùng cực gây ra cực quang.")],
             cap="Mô hình từ trường của Trái Đất", tag="THỰC TIỄN", figw=4.8, side="left")

    d.quiz("Kiểm tra nhanh",
           "Phát biểu nào về đường sức từ là SAI?",
           ["Các đường sức từ là những đường cong khép kín.",
            "Hai đường sức từ có thể cắt nhau tại một điểm.",
            "Nơi từ trường mạnh thì các đường sức được vẽ dày hơn.",
            "Bên ngoài nam châm, đường sức đi ra từ cực Bắc."],
           "B",
           "Nếu hai đường sức cắt nhau thì tại giao điểm sẽ có hai hướng của vectơ cảm ứng từ — "
           "điều này vô lí vì kim nam châm thử chỉ có thể nằm cân bằng theo một hướng duy nhất. "
           "Ba phát biểu còn lại đều là tính chất đúng của đường sức từ.")

    d.media("Mô phỏng và thí nghiệm nên dùng",
            [("Magnets and Electromagnets", "PhET – phet.colorado.edu",
              "Hiển thị đường sức từ của nam châm thẳng và của ống dây, có kim la bàn kéo thả được.",
              "Kim la bàn luôn tiếp tuyến với đường sức tại vị trí nó đứng."),
             ("Rắc mạt sắt lên tấm bìa đặt trên nam châm", "Thí nghiệm kinh điển tại lớp",
              "Đặt tấm bìa lên nam châm, rắc mạt sắt rồi gõ nhẹ.",
              "Mạt sắt tự sắp thành các đường cong — đó chính là từ phổ."),
             ("Dây dẫn thẳng xuyên qua bìa, rắc mạt sắt", "Thí nghiệm Oersted mở rộng",
              "Cho dòng điện chạy qua dây thẳng đứng xuyên tấm bìa nằm ngang, rắc mạt sắt.",
              "Mạt sắt sắp thành các vòng tròn đồng tâm quanh dây.")])

    d.wrapup("Tổng kết buổi 1",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Từ trường sinh ra bởi nam châm và bởi dòng điện; nhận biết bằng kim nam châm thử."),
              ("b", "Cảm ứng từ B là đại lượng vectơ, đơn vị tesla."),
              ("b", "Đường sức từ khép kín, không cắt nhau, ra ở cực Bắc vào ở cực Nam."),
              ("b", "Quy tắc nắm tay phải xác định chiều từ trường của dòng điện.")],
             todo=["Làm Đề 1 – Chương 3.",
                   "Vẽ từ nhớ đường sức của nam châm thẳng, dây thẳng và ống dây.",
                   "Đọc trước bài Lực từ."])


def buoi2(d):
    d.title_slide(
        sub="Buổi 2 — Lực từ tác dụng lên dây dẫn mang dòng điện. Cảm ứng từ",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Vận dụng thành thạo quy tắc bàn tay trái",
                "Tính được lực từ bằng công thức F = BIℓ·sinα",
                "Giải được bài toán cân bằng của đoạn dây trong từ trường"])

    d.section(1, "Lực từ", "Từ trường tác dụng lực lên dòng điện đặt trong nó",
              items=["Quy tắc bàn tay trái", "Công thức F = BIℓsinα", "Bài toán cân bằng"])

    d.figure("Quy tắc bàn tay trái", "t_sd_luctu",
             items=[("head", "Cách đặt tay"),
                    ("num", ("1.", "Đặt bàn tay TRÁI sao cho các đường sức từ xuyên VÀO lòng bàn tay.")),
                    ("num", ("2.", "Chiều từ cổ tay đến ngón giữa là chiều DÒNG ĐIỆN.")),
                    ("num", ("3.", "Ngón cái choãi ra 90° chỉ chiều của LỰC TỪ.")),
                    ("gap", 0.05),
                    ("note", "Lực từ luôn VUÔNG GÓC với cả dây dẫn lẫn vectơ cảm ứng từ. "
                             "Nếu ba đại lượng của em không vuông góc đôi một thì đã xác định sai.")],
             cap="Lực từ tác dụng lên dây dẫn thẳng mang dòng điện",
             tag="TRỌNG TÂM", figw=5.7)

    d.formulas("Độ lớn của lực từ",
               [(r"F = BIl\sin\alpha",
                 "B là cảm ứng từ (T), I là cường độ dòng điện (A), ℓ là chiều dài đoạn dây trong "
                 "từ trường (m), α là góc giữa dây và vectơ B."),
                (r"\alpha = 90^{\circ} \Rightarrow F = BIl",
                 "Dây VUÔNG GÓC với đường sức từ: lực từ đạt giá trị lớn nhất."),
                (r"\alpha = 0^{\circ} \Rightarrow F = 0",
                 "Dây SONG SONG với đường sức từ: không có lực từ tác dụng.")],
               lead="Công thức này cũng là cơ sở để định nghĩa đơn vị của cảm ứng từ: B = F/(Iℓsinα).",
               foot="1 tesla là cảm ứng từ của từ trường mà một đoạn dây dài 1 m mang dòng 1 A "
                    "đặt vuông góc với nó chịu lực 1 N.",
               tag="TRỌNG TÂM", sub="Bài 15")

    d.figure("Vai trò của góc α", "t_sd_goc_alpha",
             items=[("head", "Vì sao có sin α?"),
                    ("b", "Chỉ thành phần của từ trường VUÔNG GÓC với dây mới gây ra lực từ."),
                    ("b", "Thành phần song song với dây không sinh lực."),
                    ("gap", 0.05),
                    ("head", "Ba trường hợp cần nhớ"),
                    ("sub", "α = 90°: F lớn nhất, bằng BIℓ."),
                    ("sub", "α = 30°: F bằng một nửa giá trị lớn nhất."),
                    ("sub", "α = 0° hoặc 180°: F = 0."),
                    ("note", "Bẫy: α là góc giữa DÂY và B, không phải góc giữa dây và mặt phẳng nào đó. "
                             "Nhiều đề cố tình cho “góc giữa dây và mặt phẳng chứa B” để đánh lừa.")],
             cap="Dây dẫn hợp góc α với đường sức từ", tag="LƯU Ý", figw=5.5, side="left")

    d.example("Ví dụ 1 — Tính lực từ",
              "Một đoạn dây dẫn dài 20 cm mang dòng điện 5,0 A đặt trong từ trường đều có "
              "B = 0,40 T. Tính lực từ tác dụng lên đoạn dây khi dây hợp với đường sức từ "
              "góc 30°, và khi dây vuông góc với đường sức từ.",
              [("num", ("1.", "Đổi đơn vị: ℓ = 20 cm = 0,20 m.")),
               ("num", ("2.", "Khi α = 30°:  F = BIℓ·sin30° = 0,40 · 5,0 · 0,20 · 0,50 = 0,20 N.")),
               ("num", ("3.", "Khi α = 90°:  F = BIℓ = 0,40 · 5,0 · 0,20 = 0,40 N.")),
               ("p", "Lực khi vuông góc lớn gấp đôi lực khi hợp góc 30°, đúng theo tỉ số sin.")],
              "F(30°) = 0,20 N;  F(90°) = 0,40 N", sub="Bài 15")

    d.example("Ví dụ 2 — Thanh dẫn nằm trên hai ray",
              "Một thanh kim loại khối lượng 40 g, chiều dài 25 cm nằm ngang trên hai thanh ray đặt "
              "trong từ trường đều thẳng đứng có B = 0,80 T. Cho dòng điện chạy qua thanh. "
              "Tìm cường độ dòng điện nhỏ nhất để thanh bắt đầu trượt, biết hệ số ma sát nghỉ cực đại "
              "giữa thanh và ray là 0,25. Lấy g = 10 m/s².",
              [("num", ("1.", "Trọng lực: P = mg = 0,040 · 10 = 0,40 N.")),
               ("num", ("2.", "Từ trường thẳng đứng, dòng điện nằm ngang ⇒ lực từ NẰM NGANG, "
                              "vuông góc với thanh:  F = BIℓ.")),
               ("num", ("3.", "Điều kiện để thanh bắt đầu trượt:  F ≥ μ·N = μ·P.")),
               ("num", ("4.", "B·I·ℓ ≥ 0,25 · 0,40 = 0,10 N ⇒ 0,80 · I · 0,25 ≥ 0,10.")),
               ("num", ("5.", "I ≥ 0,10 / 0,20 = 0,50 A."))],
              "I(nhỏ nhất) = 0,50 A",
              fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray nằm ngang",
              tip="Chú ý: vì B thẳng đứng nên lực từ nằm ngang và KHÔNG làm thay đổi áp lực N. "
                  "Nếu B nằm ngang thì lực từ sẽ thẳng đứng, làm thay đổi N và bài toán khác hẳn.",
              sub="Bài 15")

    d.example("Ví dụ 3 — Thanh dẫn treo trên hai lò xo",
              "Một thanh dẫn nằm ngang được treo bằng hai lò xo giống nhau trong từ trường đều nằm "
              "ngang, vuông góc với thanh. Khi chưa có dòng điện, mỗi lò xo giãn 2,0 cm. "
              "Cho dòng điện qua thanh theo chiều làm lực từ hướng xuống, mỗi lò xo giãn thêm 0,50 cm. "
              "Hỏi lực từ tác dụng lên thanh bằng bao nhiêu lần trọng lượng thanh?",
              [("num", ("1.", "Ban đầu hai lò xo cân bằng trọng lực:  2k·(2,0 cm) = P.")),
               ("num", ("2.", "Khi có dòng, hai lò xo cân bằng cả trọng lực lẫn lực từ: "
                              "2k·(2,5 cm) = P + F.")),
               ("num", ("3.", "Lấy hiệu hai phương trình:  2k·(0,50 cm) = F.")),
               ("num", ("4.", "Lập tỉ số:  F/P = 0,50/2,0 = 0,25.")),
               ("p", "Vậy lực từ bằng 25 % trọng lượng của thanh.")],
              "F = 0,25·P",
              fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo",
              tip="Không cần biết k hay m: chỉ cần lấy HIỆU hai điều kiện cân bằng. "
                  "Đây là kĩ thuật rất hay dùng trong các câu vận dụng cao.",
              sub="Bài 15")

    d.quiz("Kiểm tra nhanh",
           "Một đoạn dây dẫn mang dòng điện được đặt SONG SONG với các đường sức từ. "
           "Lực từ tác dụng lên đoạn dây có độ lớn bằng bao nhiêu?",
           ["Bằng BIℓ, giá trị lớn nhất.", "Bằng 0.",
            "Bằng BIℓ/2.", "Phụ thuộc chiều dài dây theo cách khác."],
           "B",
           "Với α = 0° thì sinα = 0 nên F = BIℓ·sin0° = 0. Có thể hiểu trực quan: khi dây song song "
           "với B thì không tồn tại thành phần từ trường vuông góc với dây, nên không có lực từ.")

    d.wrapup("Tổng kết buổi 2",
             [("head", "Ba ý phải nhớ"),
              ("b", "Quy tắc bàn tay trái: đường sức xuyên vào lòng bàn tay, cổ tay → ngón giữa là "
                    "chiều dòng điện, ngón cái chỉ lực từ."),
              ("b", "F = BIℓ·sinα; lớn nhất khi vuông góc, bằng 0 khi song song."),
              ("b", "Bài toán cân bằng: lập phương trình cho hai trạng thái rồi lấy hiệu.")],
             todo=["Làm Đề 2 và Đề 3 – Chương 3.",
                   "Luyện 10 câu xác định chiều lực từ bằng quy tắc bàn tay trái.",
                   "Đọc trước bài Từ thông và cảm ứng điện từ."])


def buoi3(d):
    d.title_slide(
        sub="Buổi 3 — Từ thông. Hiện tượng cảm ứng điện từ. Định luật Faraday và Lenz",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Tính được từ thông qua một khung dây",
                "Nêu được điều kiện xuất hiện dòng điện cảm ứng",
                "Xác định được chiều dòng cảm ứng bằng định luật Lenz"])

    d.section(1, "Từ thông", "Đại lượng đo “lượng” đường sức xuyên qua một diện tích",
              items=["Định nghĩa và công thức", "Các trường hợp đặc biệt", "Cách làm biến thiên từ thông"])

    d.figure("Từ thông qua một khung dây", "t_sd_tuthong",
             items=[("head", "Công thức"),
                    ("p", "Φ = B·S·cosθ, trong đó θ là góc giữa vectơ pháp tuyến n của mặt phẳng khung "
                          "và vectơ cảm ứng từ B."),
                    ("gap", 0.05),
                    ("head", "Ba trường hợp cần nhớ"),
                    ("sub", "θ = 0°: B vuông góc mặt phẳng khung ⇒ Φ lớn nhất, bằng B·S."),
                    ("sub", "θ = 90°: B nằm TRONG mặt phẳng khung ⇒ Φ = 0."),
                    ("sub", "θ = 180°: Φ = −B·S, từ thông âm."),
                    ("note", "Đơn vị của từ thông là vêbe (Wb): 1 Wb = 1 T·m². "
                             "Từ thông là đại lượng ĐẠI SỐ, có thể âm.")],
             cap="Từ thông qua khung dây phẳng diện tích S", tag="TRỌNG TÂM", figw=5.5)

    d.content("Ba cách làm biến thiên từ thông",
              [("num", ("1.", "Thay đổi ĐỘ LỚN của cảm ứng từ B — ví dụ đưa nam châm lại gần hoặc "
                              "ra xa khung dây, hoặc thay đổi dòng điện trong nam châm điện.")),
               ("num", ("2.", "Thay đổi DIỆN TÍCH S của mạch — ví dụ kéo thanh dẫn trượt trên hai ray, "
                              "hoặc bóp méo khung dây.")),
               ("num", ("3.", "Thay đổi GÓC θ — ví dụ quay khung dây trong từ trường đều. "
                              "Đây chính là nguyên tắc của máy phát điện xoay chiều.")),
               ("rule", None),
               ("note", "Bẫy kinh điển: một khung dây chuyển động THẲNG ĐỀU nhưng nằm TRỌN VẸN trong "
                        "vùng từ trường đều thì từ thông không đổi ⇒ KHÔNG có dòng điện cảm ứng. "
                        "Dòng chỉ xuất hiện lúc khung đang đi vào hoặc đang đi ra khỏi vùng từ trường.")],
              sub="Bài 16 — Từ thông", tag="TRỌNG TÂM")

    d.figure("Thí nghiệm Faraday", "t_sd_tn_faraday",
             items=[("head", "Kết luận rút ra"),
                    ("b", "Chỉ khi từ thông qua mạch kín BIẾN THIÊN thì trong mạch mới xuất hiện "
                          "dòng điện cảm ứng."),
                    ("b", "Nam châm đứng yên — dù rất mạnh và rất gần — cũng không sinh ra dòng điện."),
                    ("b", "Nam châm chuyển động càng nhanh thì dòng điện cảm ứng càng lớn."),
                    ("note", "Điều quan trọng không phải là từ thông LỚN hay NHỎ, mà là nó "
                             "ĐANG THAY ĐỔI NHANH hay CHẬM.")],
             cap="Thí nghiệm về hiện tượng cảm ứng điện từ", tag="THỰC NGHIỆM", figw=5.8, side="left")

    d.formulas("Định luật Faraday về cảm ứng điện từ",
               [(r"e_c = -\frac{\Delta\Phi}{\Delta t}",
                 "Suất điện động cảm ứng bằng trừ tốc độ biến thiên của từ thông qua mạch."),
                (r"e_c = -N\frac{\Delta\Phi}{\Delta t}",
                 "Với cuộn dây N vòng, từ thông qua mỗi vòng đều đóng góp nên nhân thêm N."),
                (r"i_c = \frac{|e_c|}{R}",
                 "Cường độ dòng điện cảm ứng trong mạch kín có điện trở R.")],
               lead="Dấu trừ trong công thức chính là cách viết gọn của định luật Lenz.",
               foot="Đơn vị: Φ tính bằng vêbe (Wb), Δt tính bằng giây (s), e tính bằng vôn (V). "
                    "Quên nhân N là lỗi mất điểm rất phổ biến.",
               tag="TRỌNG TÂM", sub="Bài 16 — Định luật Faraday")

    d.figure("Định luật Lenz — xác định chiều dòng cảm ứng", "t_sd_lenz",
             items=[("head", "Phát biểu"),
                    ("p", "Dòng điện cảm ứng có chiều sao cho từ trường do nó sinh ra CHỐNG LẠI "
                          "nguyên nhân đã sinh ra nó."),
                    ("gap", 0.05),
                    ("head", "Áp dụng trong ba bước"),
                    ("num", ("1.", "Xác định chiều của B ban đầu qua mạch.")),
                    ("num", ("2.", "Xét từ thông đang TĂNG hay đang GIẢM.")),
                    ("num", ("3.", "Tăng ⇒ B cảm ứng NGƯỢC chiều B;  giảm ⇒ B cảm ứng CÙNG chiều B. "
                                   "Rồi dùng quy tắc nắm tay phải suy ra chiều dòng.")),
                    ("note", "Định luật Lenz chính là biểu hiện của định luật bảo toàn năng lượng: "
                             "nếu dòng cảm ứng “ủng hộ” thay vì chống lại, ta sẽ có động cơ vĩnh cửu.")],
             cap="Hai trường hợp: từ thông tăng và từ thông giảm", tag="TRỌNG TÂM", figw=6.1)

    d.figure("Đọc đồ thị Φ(t) để suy ra e(t)", "t_dt_phi_e",
             items=[("head", "Kĩ thuật đọc đồ thị"),
                    ("b", "Suất điện động bằng TRỪ ĐỘ DỐC của đồ thị từ thông theo thời gian."),
                    ("b", "Đoạn Φ tăng (độ dốc dương) ⇒ e âm."),
                    ("b", "Đoạn Φ không đổi (độ dốc bằng 0) ⇒ e = 0, không có dòng cảm ứng."),
                    ("b", "Đoạn Φ giảm (độ dốc âm) ⇒ e dương."),
                    ("note", "Đoạn Φ nào dốc hơn thì |e| lớn hơn. Đây là dạng câu hỏi đồ thị "
                             "rất hay gặp ở Phần II của đề thi.")],
             cap="Từ thông và suất điện động cảm ứng theo thời gian",
             tag="ĐỒ THỊ", figw=5.4, side="left")

    d.example("Ví dụ — Khung dây trong từ trường biến thiên",
              "Một khung dây phẳng gồm 200 vòng, diện tích mỗi vòng 50 cm², đặt vuông góc với các "
              "đường sức của một từ trường đều. Trong 0,10 s cảm ứng từ giảm đều từ 0,60 T xuống 0,20 T. "
              "Tính suất điện động cảm ứng trong khung.",
              [("num", ("1.", "Đổi đơn vị:  S = 50 cm² = 50·10⁻⁴ m² = 5,0·10⁻³ m².")),
               ("num", ("2.", "Khung vuông góc đường sức ⇒ θ = 0° ⇒ Φ = B·S.")),
               ("num", ("3.", "ΔΦ = (0,20 − 0,60)·5,0·10⁻³ = −2,0·10⁻³ Wb.")),
               ("num", ("4.", "|e| = N·|ΔΦ|/Δt = 200 · 2,0·10⁻³ / 0,10 = 4,0 V.")),
               ("note", "Quên nhân N sẽ ra 0,020 V; quên đổi cm² sang m² sẽ ra 40 000 V. "
                        "Cả hai đều là phương án nhiễu quen thuộc.")],
              "|e| = 4,0 V", sub="Bài 16")

    d.quiz("Kiểm tra nhanh",
           "Một khung dây kín chuyển động thẳng đều và nằm HOÀN TOÀN bên trong một vùng từ trường đều. "
           "Trong khung có dòng điện cảm ứng không?",
           ["Có, vì khung đang chuyển động.",
            "Không, vì từ thông qua khung không đổi.",
            "Có, nhưng rất nhỏ.",
            "Chỉ có nếu khung chuyển động vuông góc với đường sức."],
           "B",
           "Từ trường đều nên B như nhau ở mọi điểm; khung nằm trọn trong vùng đó nên diện tích và "
           "góc đều không đổi. Từ thông Φ = B·S·cosθ không đổi ⇒ ΔΦ = 0 ⇒ không có dòng cảm ứng. "
           "Dòng chỉ xuất hiện lúc khung đi vào hoặc đi ra khỏi vùng từ trường.")

    d.wrapup("Tổng kết buổi 3",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Φ = B·S·cosθ, đơn vị vêbe, là đại lượng đại số."),
              ("b", "Dòng cảm ứng chỉ xuất hiện khi từ thông BIẾN THIÊN."),
              ("b", "|e| = N·|ΔΦ|/Δt — nhớ nhân số vòng dây."),
              ("b", "Định luật Lenz: dòng cảm ứng luôn chống lại nguyên nhân sinh ra nó.")],
             todo=["Làm Đề 4 và Đề 5 – Chương 3.",
                   "Luyện 10 câu xác định chiều dòng cảm ứng.",
                   "Đọc trước bài Dòng điện xoay chiều."])


def buoi4(d):
    d.title_slide(
        sub="Buổi 4 — Đại cương về dòng điện xoay chiều",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Giải thích được nguyên tắc tạo ra dòng điện xoay chiều",
                "Phân biệt giá trị cực đại, giá trị tức thời và giá trị hiệu dụng",
                "Tính được các đại lượng của dòng điện xoay chiều từ đồ thị"])

    d.section(1, "Tạo ra dòng điện xoay chiều", "Ứng dụng trực tiếp của cảm ứng điện từ",
              items=["Máy phát điện xoay chiều", "Biểu thức e, u, i", "Giá trị hiệu dụng"])

    d.figure("Nguyên tắc của máy phát điện xoay chiều", "t_sd_may_phat",
             items=[("head", "Cơ chế"),
                    ("num", ("1.", "Khung dây quay đều với tốc độ góc ω trong từ trường đều.")),
                    ("num", ("2.", "Góc θ giữa pháp tuyến khung và B thay đổi theo thời gian: θ = ωt.")),
                    ("num", ("3.", "Từ thông Φ = B·S·cos(ωt) biến thiên điều hoà.")),
                    ("num", ("4.", "Theo định luật Faraday, suất điện động cũng biến thiên điều hoà.")),
                    ("note", "Vành khuyên và chổi quét đưa dòng điện từ khung dây đang quay ra "
                             "mạch ngoài đứng yên.")],
             cap="Sơ đồ nguyên lí máy phát điện xoay chiều", tag="TRỌNG TÂM", figw=6.1)

    d.formulas("Biểu thức của dòng điện xoay chiều",
               [(r"\Phi = NBS\cos(\omega t)", "Từ thông qua cuộn N vòng biến thiên điều hoà theo thời gian."),
                (r"e = \omega NBS\sin(\omega t) = E_0\sin(\omega t)",
                 "Suất điện động cảm ứng, với giá trị cực đại E₀ = ω·N·B·S."),
                (r"i = I_0\cos(\omega t + \varphi)",
                 "Cường độ dòng điện tức thời; I₀ là giá trị cực đại, φ là pha ban đầu.")],
               lead="Suất điện động lệch pha π/2 so với từ thông: khi Φ cực đại thì e bằng 0 và ngược lại.",
               foot="Chu kì T = 2π/ω;  tần số f = 1/T = ω/(2π). Lưới điện Việt Nam có f = 50 Hz, "
                    "tức T = 0,02 s.",
               tag="TRỌNG TÂM", sub="Bài 17")

    d.figure("Giá trị hiệu dụng — con số ghi trên thiết bị", "t_dt_u_i_hieudung",
             items=[("head", "Định nghĩa"),
                    ("p", "Giá trị hiệu dụng của dòng điện xoay chiều bằng cường độ của một dòng điện "
                          "KHÔNG ĐỔI mà nếu cho qua cùng điện trở thì toả ra cùng một nhiệt lượng "
                          "trong cùng thời gian."),
                    ("gap", 0.05),
                    ("head", "Công thức"),
                    ("sub", "U = U₀/√2 ≈ 0,707·U₀;  I = I₀/√2."),
                    ("sub", "Mạng điện “220 V” nghĩa là giá trị HIỆU DỤNG bằng 220 V, "
                            "còn giá trị cực đại lên tới 220·√2 ≈ 311 V."),
                    ("note", "Mọi vôn kế, ampe kế xoay chiều đều chỉ GIÁ TRỊ HIỆU DỤNG. "
                             "Đây là chi tiết rất hay bị hỏi trong câu đúng/sai.")],
             cap="Điện áp tức thời và giá trị hiệu dụng", tag="TRỌNG TÂM", figw=5.9, side="left")

    d.example("Ví dụ 1 — Đọc các đại lượng từ biểu thức",
              "Một dòng điện xoay chiều có biểu thức i = 4,0·cos(100πt + π/3) (A), t tính bằng giây. "
              "Xác định giá trị cực đại, giá trị hiệu dụng, tần số góc, chu kì và tần số.",
              [("num", ("1.", "Giá trị cực đại: I₀ = 4,0 A.")),
               ("num", ("2.", "Giá trị hiệu dụng: I = I₀/√2 = 4,0/1,414 ≈ 2,83 A.")),
               ("num", ("3.", "Tần số góc: ω = 100π rad/s.")),
               ("num", ("4.", "Chu kì: T = 2π/ω = 2π/(100π) = 0,02 s.")),
               ("num", ("5.", "Tần số: f = 1/T = 50 Hz."))],
              "I₀ = 4,0 A;  I ≈ 2,83 A;  T = 0,02 s;  f = 50 Hz", sub="Bài 17")

    d.example("Ví dụ 2 — Suất điện động của máy phát",
              "Một khung dây phẳng gồm 500 vòng, diện tích mỗi vòng 40 cm², quay đều quanh trục "
              "vuông góc với từ trường đều B = 0,20 T, tốc độ 3000 vòng/phút. "
              "Tính suất điện động cực đại và suất điện động hiệu dụng.",
              [("num", ("1.", "Đổi tốc độ quay: 3000 vòng/phút = 50 vòng/s ⇒ f = 50 Hz.")),
               ("num", ("2.", "Tần số góc: ω = 2πf = 100π ≈ 314 rad/s.")),
               ("num", ("3.", "Diện tích: S = 40 cm² = 4,0·10⁻³ m².")),
               ("num", ("4.", "E₀ = ω·N·B·S = 314 · 500 · 0,20 · 4,0·10⁻³ ≈ 125,7 V.")),
               ("num", ("5.", "E = E₀/√2 ≈ 88,9 V.")),
               ("note", "Sai lầm hay gặp: dùng luôn 3000 làm ω. Phải đổi vòng/phút sang vòng/giây "
                        "rồi nhân 2π.")],
              "E₀ ≈ 125,7 V;  E ≈ 88,9 V", sub="Bài 17")

    d.quiz("Kiểm tra nhanh",
           "Một bóng đèn ghi 220 V – 100 W mắc vào mạng điện xoay chiều. "
           "Giá trị cực đại của điện áp đặt vào đèn là bao nhiêu?",
           ["220 V.", "110 V.", "khoảng 311 V.", "khoảng 156 V."],
           "C",
           "Con số 220 V ghi trên đèn là giá trị HIỆU DỤNG. Giá trị cực đại U₀ = U·√2 = "
           "220 · 1,414 ≈ 311 V. Phương án 156 V ứng với việc chia cho √2 thay vì nhân — "
           "nhầm chiều của công thức.")

    d.media("Mô phỏng và quan sát nên dùng",
            [("Generator", "PhET – phet.colorado.edu",
              "Quay tua bin nước làm nam châm quay trước cuộn dây, bóng đèn sáng nhấp nháy theo.",
              "Quay càng nhanh thì đèn càng sáng — suất điện động tỉ lệ với tốc độ góc."),
             ("Faraday's Law", "PhET – phet.colorado.edu",
              "Kéo nam châm qua lại trong cuộn dây, quan sát vôn kế đổi dấu liên tục.",
              "Đảo chiều chuyển động thì dòng điện đổi chiều — nguồn gốc của dòng xoay chiều."),
             ("Quan sát dao động kí hoặc app đo âm thanh", "Thiết bị phòng thí nghiệm hoặc điện thoại",
              "Hiển thị dạng sóng hình sin của điện áp lưới qua biến áp hạ áp an toàn.",
              "Dạng sóng hình sin thực tế, đếm được số chu kì trong 0,1 s để suy ra tần số 50 Hz.")])

    d.wrapup("Tổng kết buổi 4",
             [("head", "Bốn ý phải nhớ"),
              ("b", "Máy phát điện xoay chiều: khung quay đều ⇒ Φ biến thiên điều hoà ⇒ e điều hoà."),
              ("b", "E₀ = ω·N·B·S;  ω = 2πf;  T = 1/f."),
              ("b", "U = U₀/√2;  I = I₀/√2."),
              ("b", "Mọi số liệu ghi trên thiết bị và mọi số chỉ của đồng hồ đo đều là GIÁ TRỊ HIỆU DỤNG.")],
             todo=["Làm Đề 6 và Đề 7 – Chương 3.",
                   "Luyện 10 câu đọc biểu thức i, u.",
                   "Ôn lại toàn chương chuẩn bị buổi luyện tập."])


def buoi5(d):
    d.title_slide(
        sub="Buổi 5 — Luyện tập tổng hợp và ứng dụng thực tiễn của cảm ứng điện từ",
        meta="Thời lượng 90 phút  •  " + MT,
        points=["Hệ thống lại toàn bộ công thức của chương",
                "Giải được bài toán thanh dẫn trượt trên ray và máy biến áp",
                "Giải thích được nguyên lí bếp từ, sạc không dây, phanh điện từ"])

    d.section(1, "Các dạng bài tập trọng tâm", "Ba dạng chiếm phần lớn điểm số của chương",
              items=["Thanh dẫn trượt trên ray", "Máy biến áp và truyền tải",
                     "Bài toán đồ thị"])

    d.example("Ví dụ 1 — Thanh dẫn trượt trên hai ray nghiêng",
              "Hai thanh ray song song đặt trên mặt phẳng nghiêng góc 30°, cách nhau 40 cm, "
              "trong từ trường đều B = 0,50 T vuông góc với mặt phẳng nghiêng. Một thanh dẫn khối "
              "lượng 50 g trượt xuống dọc theo hai ray. Bỏ qua ma sát, điện trở toàn mạch là 0,20 Ω. "
              "Tính tốc độ lớn nhất mà thanh đạt được. Lấy g = 10 m/s².",
              [("num", ("1.", "Suất điện động cảm ứng:  e = B·ℓ·v = 0,50 · 0,40 · v = 0,20v.")),
               ("num", ("2.", "Dòng điện trong mạch:  i = e/R = 0,20v / 0,20 = v.")),
               ("num", ("3.", "Lực từ cản trở chuyển động:  F = B·i·ℓ = 0,50 · v · 0,40 = 0,20v.")),
               ("num", ("4.", "Thanh đạt tốc độ lớn nhất khi gia tốc bằng 0, tức lực từ cân bằng "
                              "thành phần trọng lực dọc mặt nghiêng:")),
               ("num", ("5.", "0,20·v = m·g·sin30° = 0,050 · 10 · 0,50 = 0,25 N  ⇒  v = 1,25 m/s.")),
               ("p", "Trước khi đạt giá trị đó thanh vẫn tăng tốc; càng nhanh thì lực cản từ càng lớn "
                     "nên gia tốc giảm dần về 0.")],
              "v(lớn nhất) = 1,25 m/s",
              fig="t_sd_ray_nghieng", cap="Thanh dẫn trượt trên hai ray nghiêng",
              tip="Dạng bài này luôn theo cùng một mạch suy luận bốn bước: "
                  "e = Bℓv → i = e/R → F = Biℓ → cân bằng lực. Hãy thuộc chuỗi này.",
              sub="Luyện tập")

    d.figure("Máy biến áp", "t_sd_may_bien_ap",
             items=[("head", "Công thức"),
                    ("p", "Với máy biến áp lí tưởng:  U₂/U₁ = N₂/N₁  và  I₁/I₂ = N₂/N₁."),
                    ("b", "N₂ > N₁: máy TĂNG áp, điện áp tăng thì dòng điện giảm."),
                    ("b", "N₂ < N₁: máy HẠ áp, điện áp giảm thì dòng điện tăng."),
                    ("gap", 0.05),
                    ("note", "Máy biến áp chỉ hoạt động với dòng XOAY CHIỀU. Mắc vào dòng không đổi "
                             "thì từ thông không biến thiên nên cuộn thứ cấp không có điện áp — "
                             "đây là câu hỏi lí thuyết rất hay gặp.")],
             cap="Sơ đồ máy biến áp", tag="ỨNG DỤNG", figw=5.6)

    d.example("Ví dụ 2 — Truyền tải điện năng",
              "Cần truyền một công suất 100 kW đi xa bằng đường dây có điện trở tổng 4,0 Ω. "
              "So sánh công suất hao phí khi truyền ở điện áp 1,0 kV và ở điện áp 10 kV "
              "(coi hệ số công suất bằng 1).",
              [("num", ("1.", "Công suất hao phí trên đường dây:  P(hao phí) = R·I² với I = P/U.")),
               ("num", ("2.", "Ở U = 1,0 kV:  I = 100 000/1000 = 100 A ⇒ P = 4,0·100² = 40 000 W = 40 kW.")),
               ("num", ("3.", "Ở U = 10 kV:  I = 100 000/10 000 = 10 A ⇒ P = 4,0·10² = 400 W = 0,4 kW.")),
               ("num", ("4.", "Điện áp tăng 10 lần thì hao phí giảm 100 lần.")),
               ("p", "Đó là lí do người ta dùng máy tăng áp ngay tại nhà máy điện và máy hạ áp "
                     "ở gần nơi tiêu thụ.")],
              "40 kW so với 0,4 kW — hao phí giảm 100 lần",
              fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng đi xa",
              tip="Nhớ: hao phí tỉ lệ NGHỊCH với BÌNH PHƯƠNG điện áp truyền tải.",
              sub="Luyện tập")

    d.section(2, "Ứng dụng trong đời sống", "Cảm ứng điện từ có mặt ở khắp nơi",
              items=["Bếp từ", "Sạc không dây", "Phanh điện từ"])

    d.figure("Bếp từ", "t_sd_bep_tu",
             items=[("head", "Nguyên lí"),
                    ("num", ("1.", "Cuộn dây dưới mặt kính mang dòng điện xoay chiều tần số cao.")),
                    ("num", ("2.", "Từ trường biến thiên rất nhanh xuyên qua đáy nồi bằng vật liệu "
                                   "nhiễm từ.")),
                    ("num", ("3.", "Trong đáy nồi xuất hiện dòng điện xoáy (dòng Foucault).")),
                    ("num", ("4.", "Dòng xoáy toả nhiệt ngay trong đáy nồi làm nóng thức ăn.")),
                    ("note", "Vì nhiệt sinh ra ngay trong nồi nên bếp từ có hiệu suất cao và "
                             "mặt kính không nóng — chỉ nóng lên do nồi truyền ngược lại.")],
             cap="Cấu tạo và nguyên lí bếp từ", tag="THỰC TIỄN", figw=5.5, side="left")

    d.figure("Dòng Foucault: lợi và hại", "t_sd_dong_fuco",
             items=[("head", "Ứng dụng có lợi"),
                    ("b", "Phanh điện từ trên tàu hoả, xe tải: nam châm điện tạo dòng xoáy trong "
                          "đĩa kim loại, lực từ cản làm xe chậm lại mà không cần má phanh."),
                    ("b", "Lò nung cảm ứng nấu chảy kim loại."),
                    ("gap", 0.05),
                    ("head", "Tác hại cần khắc phục"),
                    ("b", "Dòng xoáy trong lõi máy biến áp và động cơ làm nóng lõi, gây hao phí."),
                    ("b", "Khắc phục bằng cách ghép lõi từ nhiều lá thép mỏng CÁCH ĐIỆN với nhau, "
                          "cắt nhỏ đường đi của dòng xoáy.")],
             cap="Dòng điện Foucault trong khối kim loại", tag="THỰC TIỄN", figw=5.6)

    d.figure("Sạc không dây", "t_sd_sac_khong_day",
             items=[("head", "Cùng một nguyên lí với máy biến áp"),
                    ("b", "Đế sạc chứa cuộn sơ cấp mang dòng xoay chiều."),
                    ("b", "Điện thoại chứa cuộn thứ cấp; từ thông qua nó biến thiên nên xuất hiện "
                          "suất điện động cảm ứng."),
                    ("b", "Dòng cảm ứng được chỉnh lưu để nạp cho pin."),
                    ("note", "Vì không có lõi sắt nối liền hai cuộn nên phần lớn từ thông bị thất "
                             "thoát — đó là lí do sạc không dây chậm hơn và nóng hơn sạc có dây.")],
             cap="Truyền năng lượng qua từ trường biến thiên", tag="THỰC TIỄN",
             figw=6.0, side="left")

    d.table("Tổng hợp công thức Chương III",
            ["Nội dung", "Công thức", "Lưu ý"],
            [["Lực từ", "F = B·I·ℓ·sinα", "α là góc giữa DÂY và B"],
             ["Từ thông", "Φ = B·S·cosθ", "θ là góc giữa PHÁP TUYẾN và B"],
             ["Suất điện động cảm ứng", "|e| = N·|ΔΦ|/Δt", "Nhớ nhân số vòng N"],
             ["Thanh dẫn trượt", "e = B·ℓ·v", "v vuông góc với thanh và với B"],
             ["Máy phát điện", "E₀ = ω·N·B·S", "ω = 2πf, đổi vòng/phút sang vòng/giây"],
             ["Giá trị hiệu dụng", "U = U₀/√2;  I = I₀/√2", "Đồng hồ đo luôn chỉ giá trị hiệu dụng"],
             ["Máy biến áp", "U₂/U₁ = N₂/N₁ = I₁/I₂", "Chỉ dùng được với dòng xoay chiều"],
             ["Hao phí truyền tải", "P = R·(P₀/U)²", "Hao phí tỉ lệ nghịch với U²"]],
            widths=[1.3, 1.4, 1.6], pt=12, tag="BẢNG CHỐT",
            foot="In bảng này ra và dán vào góc học tập — đây là toàn bộ công thức cần thuộc của Chương III.")

    d.quiz("Kiểm tra nhanh",
           "Vì sao lõi của máy biến áp phải làm bằng nhiều lá thép mỏng ghép cách điện với nhau?",
           ["Để tiết kiệm vật liệu chế tạo.",
            "Để hạn chế dòng điện Foucault, giảm hao phí toả nhiệt trong lõi.",
            "Để tăng từ thông qua cuộn thứ cấp.",
            "Để máy biến áp hoạt động được với dòng điện không đổi."],
           "B",
           "Từ thông biến thiên sinh ra dòng điện xoáy trong khối lõi, làm lõi nóng lên và gây hao phí. "
           "Ghép nhiều lá mỏng cách điện sẽ cắt nhỏ các vòng dòng xoáy, giảm mạnh hao phí. "
           "Máy biến áp không bao giờ hoạt động được với dòng điện không đổi, nên phương án cuối sai.")

    d.wrapup("Tổng kết Chương III",
             [("head", "Bản đồ kiến thức cả chương"),
              ("b", "Từ trường, đường sức từ và cảm ứng từ B."),
              ("b", "Lực từ F = BIℓsinα và quy tắc bàn tay trái."),
              ("b", "Từ thông, cảm ứng điện từ, định luật Faraday và Lenz."),
              ("b", "Dòng điện xoay chiều, giá trị hiệu dụng, máy biến áp và truyền tải điện.")],
             todo=["Làm trọn bộ 10 đề Chương 3 theo thứ tự.",
                   "Học thuộc bảng tổng hợp công thức.",
                   "Chuẩn bị Chương IV: ôn lại khái niệm nguyên tử, đồng vị."])


SPEC = [
    dict(file="C03_Buoi1_Tu_truong_va_duong_suc_tu.pptx",
         title="Từ trường. Đường sức từ. Từ trường Trái Đất",
         chapter=CH + " • Buổi 1", th=TH, slides=buoi1),
    dict(file="C03_Buoi2_Luc_tu_va_cam_ung_tu.pptx",
         title="Lực từ. Cảm ứng từ",
         chapter=CH + " • Buổi 2", th=TH, slides=buoi2),
    dict(file="C03_Buoi3_Tu_thong_va_cam_ung_dien_tu.pptx",
         title="Từ thông. Cảm ứng điện từ. Định luật Faraday và Lenz",
         chapter=CH + " • Buổi 3", th=TH, slides=buoi3),
    dict(file="C03_Buoi4_Dai_cuong_dong_dien_xoay_chieu.pptx",
         title="Đại cương về dòng điện xoay chiều",
         chapter=CH + " • Buổi 4", th=TH, slides=buoi4),
    dict(file="C03_Buoi5_Luyen_tap_va_ung_dung_chuong_III.pptx",
         title="Luyện tập tổng hợp và ứng dụng Chương III",
         chapter=CH + " • Buổi 5", th=TH, slides=buoi5),
]
