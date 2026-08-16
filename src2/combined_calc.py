# -*- coding: utf-8 -*-
"""BÀI TẬP TỔNG HỢP CHƯƠNG III + CHƯƠNG IV.
Các bài trong phần này gắn hai chủ đề với nhau theo những mạch có ý nghĩa thực tiễn:
nhà máy điện hạt nhân (năng lượng hạt nhân → máy phát điện xoay chiều → máy biến áp → truyền tải),
tác dụng của từ trường lên các tia phóng xạ mang điện, và các thiết bị đo lường hạt nhân."""

CALC34 = {

"Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn": [
dict(q="Một nhà máy điện hạt nhân phát ra công suất điện 600 MW và truyền tải toàn bộ công suất này trên đường "
       "dây có điện trở tổng cộng 5 Ω ở điện áp 500 kV (hệ số công suất bằng 1). Công suất hao phí trên đường "
       "dây bằng",
 o=["1,2 MW.", "7,2 MW.", "12 MW.", "72 MW."],
 a="B",
 sol="Cường độ dòng điện trên đường dây: I = P/U = 6·10⁸/(5·10⁵) = 1200 A.\n"
     "Công suất hao phí: ΔP = I²R = 1200² · 5 = 1,44·10⁶ · 5 = 7,2·10⁶ W = 7,2 MW.\n"
     "Đây là bài toán nối tiếp mạch kiến thức: năng lượng phân hạch tạo ra công suất điện (Chương IV), "
     "còn việc đưa công suất đó đến nơi tiêu thụ lại thuộc Chương III."),

dict(q="Một chùm tia β⁻ có tốc độ 2·10⁷ m/s bay vuông góc vào một từ trường đều có cảm ứng từ B = 0,01 T. "
       "Biết bán kính quỹ đạo tròn của hạt mang điện chuyển động vuông góc với từ trường được tính bằng "
       "r = mv/(|q|B), với khối lượng electron m = 9,1·10⁻³¹ kg và |q| = 1,6·10⁻¹⁹ C. Bán kính quỹ đạo của các "
       "electron trong chùm tia xấp xỉ",
 o=["1,1 mm.", "1,1 cm.", "11 cm.", "1,1 m."],
 a="B",
 sol="r = mv/(|q|B) = (9,1·10⁻³¹ · 2·10⁷)/(1,6·10⁻¹⁹ · 0,01) = 1,82·10⁻²³/1,6·10⁻²¹ ≈ 1,14·10⁻² m ≈ 1,1 cm.\n"
     "Kết quả này cho thấy chỉ cần một từ trường khá yếu cũng đủ làm lệch rõ rệt tia β, "
     "đó là cơ sở của việc dùng từ trường để phân biệt các loại tia phóng xạ."),

dict(q="Hai ion của hai đồng vị uranium ²³⁵U⁺ và ²³⁸U⁺ được phóng vào cùng một từ trường đều với CÙNG tốc độ, "
       "theo phương vuông góc với đường sức từ. Biết bán kính quỹ đạo r = mv/(qB). Tỉ số bán kính quỹ đạo của "
       "ion ²³⁸U⁺ và ion ²³⁵U⁺ xấp xỉ",
 o=["1,0128.", "1,0064.", "0,9874.", "1,0640."],
 a="A",
 sol="Vì hai ion có cùng tốc độ v, cùng điện tích q và cùng từ trường B nên r tỉ lệ thuận với khối lượng m, "
     "mà khối lượng lại tỉ lệ với số khối A.\n"
     "r₂₃₈/r₂₃₅ = 238/235 ≈ 1,0128.\n"
     "Sự chênh lệch nhỏ này chính là nguyên tắc của máy khối phổ dùng để tách các đồng vị — "
     "một ứng dụng trực tiếp của lực từ vào vật lí hạt nhân."),

dict(q="Trong ba loại tia phóng xạ α, β⁻ và γ cùng bay vào một từ trường đều theo phương vuông góc với đường sức, "
       "kết luận nào sau đây là đúng?",
 o=["Cả ba tia đều bị lệch, tia γ lệch nhiều nhất.",
    "Tia α và tia β⁻ bị lệch về hai phía ngược nhau, tia γ truyền thẳng.",
    "Chỉ tia γ bị lệch vì nó có năng lượng lớn nhất.",
    "Cả ba tia đều truyền thẳng vì từ trường không tác dụng lên chúng."],
 a="B",
 sol="Tia α mang điện tích +2e còn tia β⁻ mang điện tích −e, nên lực từ tác dụng lên chúng ngược chiều nhau "
     "(quy tắc bàn tay trái) và chúng lệch về hai phía đối nhau. Tia γ là sóng điện từ, không mang điện, "
     "nên không chịu lực từ và truyền thẳng.\n"
     "Ngoài ra, từ r = mv/(qB), tia β⁻ có khối lượng rất nhỏ nên bán kính quỹ đạo nhỏ, tức bị lệch mạnh hơn tia α "
     "rất nhiều."),
],

"Dạng 2 – Câu trắc nghiệm đúng/sai": [
dict(stem="Một tổ máy của nhà máy điện hạt nhân có công suất điện 800 MW, hiệu suất chuyển hoá năng lượng hạt "
          "nhân thành điện năng là 32%. Máy phát điện tạo ra điện áp hiệu dụng 20 kV; điện áp này được nâng lên "
          "400 kV nhờ một máy biến áp lí tưởng rồi truyền tải trên đường dây có điện trở tổng cộng 4 Ω "
          "(hệ số công suất bằng 1).",
 fig="f13_bien_ap",
 items=[
  ("Công suất nhiệt mà lò phản ứng phải cung cấp là 2500 MW.", True,
   "P_nhiệt = P_điện/H = 800/0,32 = 2500 MW."),
  ("Máy biến áp dùng để nâng điện áp có tỉ số số vòng dây giữa cuộn thứ cấp và cuộn sơ cấp bằng 20.", True,
   "N₂/N₁ = U₂/U₁ = 400/20 = 20. Vì N₂ > N₁ nên đây là máy tăng áp."),
  ("Cường độ dòng điện hiệu dụng trên đường dây tải điện là 40 000 A.", False,
   "I = P/U = 8·10⁸/(4·10⁵) = 2000 A. Giá trị 40 000 A ứng với trường hợp truyền tải ngay ở 20 kV mà "
   "không qua máy tăng áp."),
  ("Công suất hao phí trên đường dây là 16 MW, chiếm 2% công suất phát của tổ máy.", True,
   "ΔP = I²R = 2000² · 4 = 1,6·10⁷ W = 16 MW; tỉ lệ 16/800 = 2%."),
 ]),

dict(stem="Người ta cho ba loại tia phóng xạ α, β⁻ và γ phát ra từ một nguồn đi qua một khe hẹp rồi vào một vùng "
          "có từ trường đều, phương của các tia vuông góc với đường sức từ. Bán kính quỹ đạo của hạt mang điện "
          "được tính bằng r = mv/(|q|B).",
 fig="f21_dam_xuyen",
 items=[
  ("Tia γ không bị lệch khỏi phương ban đầu.", True,
   "Tia γ là sóng điện từ, không mang điện tích nên không chịu tác dụng của lực từ."),
  ("Tia α và tia β⁻ bị lệch về hai phía ngược nhau so với phương ban đầu.", True,
   "Hai tia mang điện trái dấu nên lực từ tác dụng lên chúng ngược chiều nhau."),
  ("Nếu tăng độ lớn cảm ứng từ B thì bán kính quỹ đạo của tia α và tia β⁻ đều giảm, tức chúng bị lệch mạnh hơn.", True,
   "Từ r = mv/(|q|B), r tỉ lệ nghịch với B nên B tăng thì r giảm và độ lệch tăng."),
  ("Có thể dùng từ trường để tách chùm tia γ thành hai chùm mang điện tích trái dấu.", False,
   "Tia γ không mang điện tích nên không thể bị từ trường tách ra; nó chỉ có thể bị suy giảm cường độ khi "
   "đi qua vật liệu che chắn như chì."),
 ]),

dict(stem="Máy phát điện xoay chiều của một nhà máy điện có phần ứng gồm N = 100 vòng dây, diện tích mỗi vòng "
          "S = 2,0 m², đặt trong từ trường đều B = 0,80 T. Rôto quay đều với tốc độ 3000 vòng/phút quanh trục "
          "vuông góc với vectơ cảm ứng từ.",
 fig="f10_may_phat",
 items=[
  ("Tần số của dòng điện do máy phát ra là 50 Hz, phù hợp với tiêu chuẩn mạng điện Việt Nam.", True,
   "n = 3000 vòng/phút = 50 vòng/giây ⟹ f = 50 Hz và ω = 2π·50 ≈ 314,16 rad/s."),
  ("Suất điện động cực đại của máy phát xấp xỉ 50,3 kV.", True,
   "E₀ = NBSω = 100 · 0,80 · 2,0 · 314,16 = 160 · 314,16 ≈ 50 265 V ≈ 50,3 kV."),
  ("Suất điện động hiệu dụng của máy phát xấp xỉ 35,5 kV.", True,
   "E = E₀/√2 ≈ 50 265/1,414 ≈ 35 545 V ≈ 35,5 kV."),
  ("Muốn tăng tần số lên 60 Hz mà vẫn giữ nguyên suất điện động cực đại thì phải đồng thời TĂNG số vòng dây "
   "của phần ứng.", False,
   "E₀ = NBSω. Tăng tần số nghĩa là tăng ω, làm E₀ tăng theo. Muốn giữ E₀ không đổi thì phải GIẢM một trong ba "
   "đại lượng N, B, S (cụ thể giảm đúng theo tỉ lệ 50/60), chứ không phải tăng."),
 ]),
],

"Dạng 3 – Câu trả lời ngắn": [
dict(q="Một nhà máy điện hạt nhân có công suất điện 500 MW, hiệu suất 30%, mỗi phân hạch ²³⁵U toả 200 MeV. "
       "Tính khối lượng ²³⁵U mà nhà máy tiêu thụ trong một năm (365 ngày), làm tròn đến hàng đơn vị "
       "(đơn vị: kg).",
 ans="≈ 642 kg",
 sol="Công suất nhiệt: P_nhiệt = 500/0,30 ≈ 1667 MW = 1,667·10⁹ W.\n"
     "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
     "Số phân hạch mỗi giây: 1,667·10⁹/3,2·10⁻¹¹ ≈ 5,21·10¹⁹.\n"
     "Số phân hạch trong một năm: 5,21·10¹⁹ · 365 · 86400 ≈ 1,64·10²⁷.\n"
     "Số mol: 1,64·10²⁷/6,02·10²³ ≈ 2728 mol ⟹ m ≈ 2728 · 235 ≈ 6,4·10⁵ g ≈ 642 kg."),

dict(q="Một chùm tia β⁻ có tốc độ 1,5·10⁷ m/s bay vuông góc vào từ trường đều B = 0,02 T. Biết r = mv/(|q|B), "
       "m = 9,1·10⁻³¹ kg, |q| = 1,6·10⁻¹⁹ C. Tính bán kính quỹ đạo của các electron "
       "(đơn vị: mm, làm tròn đến một chữ số thập phân).",
 ans="4,3 mm",
 sol="r = (9,1·10⁻³¹ · 1,5·10⁷)/(1,6·10⁻¹⁹ · 0,02) = 1,365·10⁻²³/3,2·10⁻²¹ ≈ 4,27·10⁻³ m ≈ 4,3 mm."),

dict(q="Máy phát điện của một nhà máy điện hạt nhân tạo ra điện áp hiệu dụng 20 kV. Để truyền tải, người ta dùng "
       "máy biến áp lí tưởng nâng điện áp lên 500 kV. Biết cuộn sơ cấp có 800 vòng. Tính số vòng dây của cuộn "
       "thứ cấp.",
 ans="20 000 vòng",
 sol="N₂ = N₁·U₂/U₁ = 800 · 500/20 = 800 · 25 = 20 000 vòng."),
],

"Dạng 4 – Bài tập tự luận và vận dụng cao": [
dict(q="Một nhà máy điện hạt nhân có công suất điện 600 MW với hiệu suất chuyển hoá năng lượng hạt nhân thành "
       "điện năng là 32%. Máy phát điện tạo ra điện áp hiệu dụng 24 kV; điện áp này được nâng lên 480 kV nhờ một "
       "máy biến áp lí tưởng rồi truyền trên đường dây có điện trở tổng cộng 8 Ω (hệ số công suất bằng 1).\n"
       "Cho mỗi phân hạch ²³⁵U toả 200 MeV; 1 MeV = 1,6·10⁻¹³ J; N_A = 6,02·10²³ mol⁻¹.\n"
       "a) Tính công suất nhiệt của lò phản ứng và khối lượng ²³⁵U tiêu thụ trong một ngày.\n"
       "b) Tính tỉ số số vòng dây của máy tăng áp.\n"
       "c) Tính công suất hao phí trên đường dây và hiệu suất truyền tải.\n"
       "d) Nếu bỏ máy tăng áp và truyền tải ngay ở 24 kV thì điều gì xảy ra? Hãy tính toán để chứng minh.",
 fig="f22_phan_hach",
 ans="a) 1875 MW; ≈ 2,0 kg/ngày.  b) N₂/N₁ = 20.  c) ΔP = 12,5 MW; H ≈ 97,9%.  "
     "d) Hao phí lớn gấp 400 lần, vượt xa công suất phát nên không thể truyền tải được.",
 sol="a) Công suất nhiệt: P_nhiệt = P_điện/H = 600/0,32 = 1875 MW = 1,875·10⁹ W.\n"
     "  Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
     "  Số phân hạch mỗi giây: 1,875·10⁹/3,2·10⁻¹¹ ≈ 5,86·10¹⁹.\n"
     "  Số phân hạch mỗi ngày: 5,86·10¹⁹ · 86400 ≈ 5,06·10²⁴.\n"
     "  Số mol: 5,06·10²⁴/6,02·10²³ ≈ 8,41 mol ⟹ m ≈ 8,41 · 235 ≈ 1976 g ≈ 2,0 kg.\n"
     "b) N₂/N₁ = U₂/U₁ = 480/24 = 20.\n"
     "c) I = P/U = 6·10⁸/(4,8·10⁵) = 1250 A.\n"
     "  ΔP = I²R = 1250² · 8 = 1,5625·10⁶ · 8 = 1,25·10⁷ W = 12,5 MW.\n"
     "  H = (600 − 12,5)/600 ≈ 0,979 = 97,9%.\n"
     "d) Nếu truyền ở 24 kV: I' = 6·10⁸/(2,4·10⁴) = 25 000 A.\n"
     "  ΔP' = 25 000² · 8 = 6,25·10⁸ · 8 = 5·10⁹ W = 5000 MW.\n"
     "  Giá trị này lớn hơn cả công suất phát của nhà máy (600 MW), tức là điều đó KHÔNG THỂ xảy ra: "
     "đường dây sẽ bị quá tải và toàn bộ điện năng bị đốt cháy trên đường dây. "
     "Kết luận: bắt buộc phải tăng áp trước khi truyền tải. Hao phí tỉ lệ nghịch với bình phương điện áp, "
     "tăng điện áp 20 lần làm hao phí giảm 400 lần — đúng bằng tỉ số 5000/12,5."),

dict(q="Để phân biệt và nghiên cứu ba loại tia phóng xạ, người ta cho chùm tia phát ra từ một nguồn đi qua một "
       "khe hẹp rồi vào một vùng từ trường đều, sau đó hứng lên một tấm phim đặt phía sau. Cho biết bán kính "
       "quỹ đạo của hạt mang điện chuyển động vuông góc với từ trường là r = mv/(|q|B).\n"
       "a) Mô tả vị trí ba vết trên tấm phim và giải thích bằng quy tắc bàn tay trái.\n"
       "b) Giải thích vì sao vết của tia β lệch xa hơn nhiều so với vết của tia α, mặc dù tia α mang điện tích "
       "có độ lớn gấp đôi.\n"
       "c) Nếu muốn chỉ giữ lại chùm tia γ để chiếu vào mẫu vật nghiên cứu thì phải bố trí thí nghiệm như thế nào?",
 fig="f21_dam_xuyen",
 ans="a) Ba vết: tia γ ở giữa (đi thẳng), tia α và tia β⁻ lệch về hai phía ngược nhau.  "
     "b) Vì khối lượng electron rất nhỏ nên bán kính quỹ đạo nhỏ hơn nhiều.  "
     "c) Dùng từ trường tách chùm rồi chắn hai chùm mang điện.",
 sol="a) Trên tấm phim thu được ba vết:\n"
     "  • Vết ở giữa, đúng theo phương ban đầu: tia γ, vì không mang điện nên không chịu lực từ.\n"
     "  • Hai vết lệch về hai phía ngược nhau: tia α (điện tích +2e) và tia β⁻ (điện tích −e). "
     "Vì hai tia mang điện trái dấu, theo quy tắc bàn tay trái, chiều dòng điện tương ứng ngược nhau nên lực từ "
     "cũng ngược chiều nhau.\n"
     "b) Bán kính quỹ đạo r = mv/(|q|B) tỉ lệ THUẬN với khối lượng và tỉ lệ NGHỊCH với độ lớn điện tích. "
     "Khối lượng hạt α (≈ 4 u ≈ 6,6·10⁻²⁷ kg) lớn hơn khối lượng electron (9,1·10⁻³¹ kg) khoảng 7300 lần, "
     "trong khi điện tích chỉ gấp 2 lần. Tác dụng của khối lượng áp đảo hoàn toàn, nên r của hạt α lớn hơn rất "
     "nhiều, tức quỹ đạo ít cong hơn và vết lệch ít hơn. (Ở đây so sánh với giả thiết hai loại hạt có cùng tốc độ; "
     "thực tế tia β còn có tốc độ lớn hơn nhiều, nhưng kết luận định tính vẫn không đổi.)\n"
     "c) Bố trí một từ trường đủ mạnh để tách chùm tia thành ba nhánh, rồi đặt các tấm chắn (bằng nhôm hoặc "
     "thuỷ tinh hữu cơ) chặn hai nhánh lệch của tia α và tia β; chỉ để hở lối đi thẳng cho tia γ. "
     "Cách này kết hợp kiến thức lực từ của Chương III với tính chất các tia phóng xạ của Chương IV."),

dict(q="So sánh hai nhà máy điện có cùng công suất điện 500 MW:\n"
       "  • Nhà máy A là nhà máy điện hạt nhân, hiệu suất 30%, dùng nhiên liệu ²³⁵U (mỗi phân hạch toả 200 MeV).\n"
       "  • Nhà máy B là nhà máy nhiệt điện than, hiệu suất 40%, mỗi kilôgam than toả 3·10⁷ J.\n"
       "a) Tính khối lượng nhiên liệu mỗi nhà máy tiêu thụ trong một ngày.\n"
       "b) Cả hai nhà máy đều dùng máy phát điện xoay chiều giống nhau. Hãy chỉ ra điểm giống nhau về nguyên tắc "
       "biến đổi năng lượng và điểm khác nhau về nguồn năng lượng sơ cấp.\n"
       "c) Nêu hai ưu điểm và hai nhược điểm của nhà máy điện hạt nhân so với nhà máy nhiệt điện than.",
 ans="a) Nhà máy A: ≈ 1,8 kg ²³⁵U/ngày; nhà máy B: ≈ 3600 tấn than/ngày.",
 sol="a) Điện năng sản xuất trong một ngày: W = 5·10⁸ · 86400 = 4,32·10¹³ J.\n"
     "  • Nhà máy A: nhiệt năng cần = 4,32·10¹³/0,30 = 1,44·10¹⁴ J.\n"
     "    Số phân hạch = 1,44·10¹⁴/(3,2·10⁻¹¹) = 4,5·10²⁴.\n"
     "    m = (4,5·10²⁴/6,02·10²³) · 235 ≈ 7,48 · 235 ≈ 1758 g ≈ 1,8 kg.\n"
     "  • Nhà máy B: nhiệt năng cần = 4,32·10¹³/0,40 = 1,08·10¹⁴ J.\n"
     "    m = 1,08·10¹⁴/(3·10⁷) = 3,6·10⁶ kg = 3600 tấn.\n"
     "    Tỉ số khối lượng nhiên liệu: 3,6·10⁶/1,758 ≈ 2·10⁶ lần.\n"
     "b) Giống nhau: cả hai đều biến đổi năng lượng theo chuỗi nhiệt năng → cơ năng (hơi nước làm quay tuabin) "
     "→ điện năng nhờ hiện tượng cảm ứng điện từ trong máy phát điện xoay chiều. Toàn bộ phần “sản xuất điện” "
     "thuộc Chương III và hoàn toàn như nhau ở hai nhà máy.\n"
     "  Khác nhau: nguồn năng lượng sơ cấp — nhà máy A lấy năng lượng từ phản ứng phân hạch hạt nhân "
     "(biến đổi khối lượng nghỉ thành năng lượng), nhà máy B lấy từ phản ứng hoá học khi đốt than.\n"
     "c) Ưu điểm của nhà máy điện hạt nhân: (1) lượng nhiên liệu cực nhỏ nên chi phí vận chuyển, lưu trữ thấp; "
     "(2) không phát thải khí CO₂ và khí gây ô nhiễm không khí trong quá trình vận hành.\n"
     "  Nhược điểm: (1) tạo ra chất thải phóng xạ có chu kì bán rã dài, đòi hỏi lưu giữ và xử lí an toàn trong "
     "hàng nghìn năm; (2) rủi ro sự cố hạt nhân tuy xác suất thấp nhưng hậu quả rất nghiêm trọng, và chi phí đầu "
     "tư ban đầu cùng chi phí tháo dỡ nhà máy rất lớn."),
],
}
