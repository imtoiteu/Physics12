# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.
Đề 26 – 30 (Khó – phân loại học sinh giỏi)."""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 26
DE26 = dict(
ma="TH-Đề 26", ten="ĐỀ THI THỬ SỐ 26", muc="Khó – phân loại",
trongtam="Bài toán nhiều ràng buộc, xi lanh hai ngăn, bảo toàn động lượng hai chiều",
P1=[
mc("Thả m kg nước đá ở −10 °C vào 2,0 kg nước ở 40 °C trong bình cách nhiệt. Khối lượng nước đá "
   "lớn nhất để đá tan hết xấp xỉ (c(đá) = 2100; c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg)",
   ["0,88 kg.", "0,931 kg.", "0,99 kg.", "1,05 kg."],
   "B",
   "Nhiệt nước nhả tối đa: 2,0 · 4200 · 40 = 336 000 J.\n"
   "Nhiệt cần cho m kg đá: m·2100·10 + m·3,4·10⁵ = 361 000·m.\n"
   "361 000·m ≤ 336 000 ⇒ m ≤ 0,9307 kg, tức khối lượng lớn nhất là 0,931 kg.",
   "Biện luận điều kiện", RK),

mc("Một xi lanh nằm ngang chia đôi bằng pit-tông mỏng, mỗi phần dài 40 cm chứa cùng loại khí ở "
   "cùng nhiệt độ T và cùng áp suất. Nung phần trái lên 1,5T, hạ phần phải xuống 0,75T. "
   "Pit-tông dịch chuyển",
   ["6,7 cm về phía phải.", "8,0 cm về phía phải.",
    "8,0 cm về phía trái.", "13,3 cm về phía phải."],
   "D",
   "Đặt x là độ dịch của pit-tông về phía phải, áp suất chung sau cùng là p'.\n"
   "Phần trái: p·40/T = p'·(40 + x)/(1,5T) ⇒ p·60 = p'·(40 + x).\n"
   "Phần phải: p·40/T = p'·(40 − x)/(0,75T) ⇒ p·30 = p'·(40 − x).\n"
   "Chia hai phương trình: 60/30 = (40 + x)/(40 − x) ⇒ 2 = (40 + x)/(40 − x).\n"
   "80 − 2x = 40 + x ⇒ 3x = 40 ⇒ x = 40/3 ≈ 13,3 cm về phía phải.",
   "Xi lanh hai ngăn", RK),

mc("Một khối khí lí tưởng thực hiện quá trình trong đó nhiệt độ tuyệt đối tỉ lệ thuận với bình "
   "phương thể tích. Khi thể tích tăng gấp đôi, áp suất",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "pV/T = hằng số với T = a·V² ⇒ p/(a·V) = hằng số ⇒ p tỉ lệ thuận với V.\n"
   "V tăng gấp đôi thì p cũng tăng gấp đôi.",
   "Quá trình đặc biệt của khí lí tưởng", RK),

mc("Hai bình A (2,0 L) và B (3,0 L) nối bằng ống có khoá. Bình A chứa khí ở 3,0·10⁵ Pa, "
   "bình B chứa cùng loại khí ở 1,0·10⁵ Pa, cùng nhiệt độ. Mở khoá, áp suất chung bằng",
   ["2,0·10⁵ Pa.", "1,8·10⁵ Pa.", "1,5·10⁵ Pa.", "2,4·10⁵ Pa."],
   "B",
   "Số mol tỉ lệ với p·V. Tổng: 3,0·10⁵ · 2,0 + 1,0·10⁵ · 3,0 = 6,0·10⁵ + 3,0·10⁵ = 9,0·10⁵ "
   "(đơn vị Pa·L).\n"
   "Thể tích tổng: 5,0 L ⇒ p = 9,0·10⁵/5,0 = 1,8·10⁵ Pa.",
   "Trộn hai lượng khí", RK),

mc("Ở nhiệt độ T, tốc độ trung bình của phân tử khí là v̄. Ở nhiệt độ 2,25·T, tốc độ trung bình bằng",
   ["1,25·v̄.", "1,50·v̄.", "2,25·v̄.", "4,50·v̄."],
   "B",
   "v̄ tỉ lệ với căn bậc hai của nhiệt độ tuyệt đối.\n"
   "Tỉ số: √2,25 = 1,50 lần.",
   "Động năng phân tử", K),

mc("Một thanh dẫn dài 50 cm, khối lượng 200 g trượt trên hai ray nghiêng 37° "
   "(sin37° = 0,60; cos37° = 0,80) có hệ số ma sát 0,25, trong từ trường đều B = 0,40 T vuông góc "
   "mặt phẳng nghiêng, điện trở toàn mạch 0,20 Ω. Tốc độ lớn nhất của thanh bằng (g = 10 m/s²)",
   ["1,6 m/s.", "4,0 m/s.", "3,0 m/s.", "1,2 m/s."],
   "B",
   "Thành phần trọng lực dọc mặt nghiêng: m·g·sin37° = 0,200 · 10 · 0,60 = 1,20 N.\n"
   "Lực ma sát: μ·m·g·cos37° = 0,25 · 0,200 · 10 · 0,80 = 0,40 N.\n"
   "Hợp lực kéo còn lại: 1,20 − 0,40 = 0,80 N.\n"
   "Lực từ cản ở tốc độ v: B²ℓ²v/R = (0,16 · 0,25/0,20)·v = 0,20v.\n"
   "Tốc độ lớn nhất khi gia tốc bằng 0: 0,20·v = 0,80 ⇒ v = 4,0 m/s.",
   "Thanh dẫn trên mặt nghiêng có ma sát", RK, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trên hai ray nghiêng"),

mc("Một khung dây vuông cạnh 40 cm chuyển động đều 5,0 m/s đi qua vùng từ trường đều rộng 24 cm. "
   "Tổng thời gian CÓ dòng điện cảm ứng trong khung bằng",
   ["0,048 s.", "0,096 s.", "0,128 s.", "0,032 s."],
   "B",
   "Vì d < a nên dòng chỉ xuất hiện khi khung đi vào (quãng đường d = 24 cm) và khi đi ra "
   "(quãng đường d = 24 cm).\n"
   "Tổng quãng đường có dòng: 2 · 0,24 = 0,48 m ⇒ t = 0,48/5,0 = 0,096 s.",
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

mc("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi 240 V. Khi cuộn thứ cấp có N vòng thì "
   "điện áp thứ cấp là 30 V; khi quấn thêm 20 vòng thì điện áp là 35 V. Số vòng cuộn sơ cấp bằng",
   ["720 vòng.", "960 vòng.", "1200 vòng.", "480 vòng."],
   "B",
   "Mỗi vòng ứng với (35 − 30)/20 = 0,25 V.\n"
   "Số vòng ban đầu: N = 30/0,25 = 120 vòng.\n"
   "N₁ = N·U₁/U₂ = 120 · 240/30 = 960 vòng.",
   "Máy biến áp – hệ hai phương trình", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một nhà máy truyền công suất không đổi. Ở điện áp U hiệu suất 84 %, cấp cho 8400 hộ dân. "
   "Tăng điện áp lên 2U thì số hộ được cấp điện bằng",
   ["9200 hộ.", "9600 hộ.", "9000 hộ.", "10 000 hộ."],
   "B",
   "Hao phí ban đầu 16 %. Tăng U gấp đôi ⇒ hao phí giảm 4 lần, còn 4 %.\n"
   "Công suất tới nơi tiêu thụ tăng từ 84 % lên 96 %.\n"
   "Số hộ: 8400 · 96/84 = 8400 · 1,142857 = 9600 hộ.",
   "Truyền tải điện năng – bài toán thực tiễn", RK, fig="t_sd_truyen_tai",
   cap="Truyền tải điện năng"),

mc("Dùng prôtôn có động năng 5,45 MeV bắn vào ⁹₄Be đứng yên, sinh hạt α (động năng 4,00 MeV, "
   "vuông góc phương prôtôn) và ⁶₃Li. Tỉ số động năng của hạt α và hạt liti xấp xỉ",
   ["0,89.", "1,12.", "1,50.", "0,67."],
   "B",
   "6·W(Li) = 1 · 5,45 + 4 · 4,00 = 21,45 ⇒ W(Li) ≈ 3,575 MeV.\n"
   "Tỉ số: 4,00/3,575 ≈ 1,12.",
   "Bảo toàn động lượng hai chiều", RK),

mc("Một mẫu chứa hai đồng vị X (T = 2,0 giờ) và Y (T = 8,0 giờ), ban đầu số hạt nhân bằng nhau. "
   "Sau 8,0 giờ, số hạt nhân Y gấp bao nhiêu lần số hạt nhân X?",
   ["4 lần.", "8 lần.", "2 lần.", "16 lần."],
   "B",
   "X trải qua 4 chu kì nên còn N₀/16; Y trải qua 1 chu kì nên còn N₀/2.\n"
   "Tỉ số: (N₀/2)/(N₀/16) = 8 lần.",
   "Hỗn hợp hai đồng vị", K),

mc("Một mẫu đá chứa ²³⁸U (T = 4,5 tỉ năm) và ²⁰⁶Pb với tỉ số khối lượng Pb/U bằng 0,80. "
   "Tuổi mẫu đá xấp xỉ (ln2 ≈ 0,693)",
   ["3,2 tỉ năm.", "4,0 tỉ năm.", "4,5 tỉ năm.", "5,4 tỉ năm."],
   "B",
   "(206/238)·(2ⁿ − 1) = 0,80 ⇒ 2ⁿ − 1 = 0,80 · 238/206 ≈ 0,9243.\n"
   "2ⁿ = 1,9243 ⇒ n = ln1,9243/ln2 = 0,6546/0,693 ≈ 0,9446.\n"
   "t = 0,9446 · 4,5 ≈ 4,25 tỉ năm, gần nhất với 4,0 tỉ năm.",
   "Xác định tuổi mẫu đá", RK),

mc("Một nguồn nhiệt đồng vị chứa 3,0 gam ²¹⁰Po (T = 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Công suất ban đầu xấp xỉ (Nₐ = 6,02·10²³; 1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693)",
   ["216 W.", "432 W.", "864 W.", "144 W."],
   "B",
   "N₀ = (3,0/210)·6,02·10²³ ≈ 8,60·10²¹ hạt.\n"
   "T = 138 · 86 400 ≈ 1,192·10⁷ s ⇒ λ ≈ 5,81·10⁻⁸ s⁻¹.\n"
   "H₀ = λN₀ ≈ 4,997·10¹⁴ Bq.\n"
   "P = H₀ · 5,4 · 1,6·10⁻¹³ ≈ 4,997·10¹⁴ · 8,64·10⁻¹³ ≈ 432 W.",
   "Công suất của nguồn phóng xạ", RK),

mc("Một chất phóng xạ có chu kì bán rã T. Số hạt nhân phân rã trong khoảng từ 0 đến T so với "
   "khoảng từ T đến 2T và từ 2T đến 3T lập thành dãy",
   ["1 : 1 : 1.", "4 : 2 : 1.", "1 : 2 : 4.", "2 : 1 : 1."],
   "B",
   "Lần lượt bằng N₀/2, N₀/4, N₀/8, tức tỉ lệ 4 : 2 : 1.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Trong phản ứng nhiệt hạch ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV, tỉ số động năng của nơtron "
   "và hạt nhân heli bằng",
   ["1 : 4.", "4 : 1.", "1 : 1.", "5 : 1."],
   "B",
   "Hai hạt sinh ra có động lượng cùng độ lớn nên động năng tỉ lệ nghịch với khối lượng:\n"
   "W(n)/W(He) = m(He)/m(n) = 4/1.",
   "Bảo toàn động lượng trong phản ứng", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Một lò phản ứng có công suất điện 1000 MW, hiệu suất 33 %. Khối lượng ²³⁵U tiêu thụ trong "
   "một năm (365 ngày) xấp xỉ (200 MeV mỗi phân hạch)",
   ["580 kg.", "1166 kg.", "2320 kg.", "390 kg."],
   "B",
   "Công suất nhiệt: 1000/0,33 ≈ 3030 MW = 3,03·10⁹ W.\n"
   "Số phân hạch mỗi giây: 3,03·10⁹/3,2·10⁻¹¹ ≈ 9,47·10¹⁹.\n"
   "Trong một năm: 9,47·10¹⁹ · 3,1536·10⁷ ≈ 2,986·10²⁷ hạt.\n"
   "Khối lượng: (2,986·10²⁷/6,02·10²³) · 235 ≈ 4960 · 235/1000 ≈ 1166 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

mc("Một mẫu chất phóng xạ nguyên chất, sau thời gian t có 36 % số hạt nhân đã phân rã. "
   "Sau thời gian 2t, phần trăm số hạt nhân đã phân rã bằng",
   ["40,96 %.", "59,0 %.", "72,0 %.", "64,0 %."],
   "B",
   "Còn lại sau t: 64 % = 0,64.\n"
   "Sau 2t còn lại (0,64)² = 0,4096 = 40,96 %.\n"
   "Đã phân rã: 100 − 40,96 = 59,04 ≈ 59,0 %.",
   "Bản chất hàm mũ của phân rã", RK),

mc("Khi nói về độ hụt khối và năng lượng liên kết, phát biểu nào SAI?",
   ["Độ hụt khối của mọi hạt nhân bền đều dương.",
    "Hạt nhân có độ hụt khối lớn hơn thì luôn bền vững hơn.",
    "Năng lượng liên kết bằng tích độ hụt khối với bình phương tốc độ ánh sáng.",
    "Năng lượng liên kết riêng là năng lượng liên kết tính trên một nuclêôn."],
   "B",
   "Độ bền vững đo bằng năng lượng liên kết RIÊNG ε = W(lk)/A, không phải bằng độ hụt khối hay "
   "năng lượng liên kết toàn phần. Urani có độ hụt khối rất lớn nhưng kém bền hơn sắt.",
   "So sánh độ bền vững", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),
],
P2=[
ds("Thả m kg nước đá ở −10 °C vào 2,0 kg nước ở 40 °C trong bình cách nhiệt. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng tối đa mà nước nhả ra là 336 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · 40 = 336 000 J."),
    ("Nhiệt lượng cần để m kg đá từ −10 °C tan hết là 361 000·m (J).", True,
     "Đúng. m·2100·10 + m·3,4·10⁵ = m·(21 000 + 340 000)."),
    ("Khối lượng đá lớn nhất để đá tan hết xấp xỉ 0,931 kg.", True,
     "Đúng. 361 000·m ≤ 336 000 ⇒ m ≤ 0,9307 kg."),
    ("Nếu thả 1,2 kg nước đá thì nhiệt độ cân bằng vẫn trên 0 °C.", False,
     "Sai. 1,2 kg cần 433 200 J, lớn hơn 336 000 J nên đá chỉ tan một phần và nhiệt độ cân bằng "
     "đúng bằng 0 °C.")],
   "Biện luận điều kiện", RK),

ds("Hai bình A (2,0 L) và B (3,0 L) nối bằng ống nhỏ có khoá, cùng nhiệt độ. Bình A chứa khí ở "
   "3,0·10⁵ Pa, bình B chứa cùng loại khí ở 1,0·10⁵ Pa.",
   [("Số mol khí trong mỗi bình tỉ lệ với tích p·V của bình đó.", True,
     "Đúng. Từ pV = nRT với T chung."),
    ("Tổng “số mol quy đổi” là 9,0·10⁵ Pa·L.", True,
     "Đúng. 3,0·10⁵·2,0 + 1,0·10⁵·3,0 = 9,0·10⁵ Pa·L."),
    ("Sau khi mở khoá, áp suất chung là 1,8·10⁵ Pa.", True,
     "Đúng. p = 9,0·10⁵/(2,0 + 3,0) = 1,8·10⁵ Pa."),
    ("Áp suất chung bằng trung bình cộng hai áp suất ban đầu, tức 2,0·10⁵ Pa.", False,
     "Sai. Phải lấy trung bình có TRỌNG SỐ theo thể tích chứ không phải trung bình cộng đơn giản; "
     "kết quả đúng là 1,8·10⁵ Pa.")],
   "Trộn hai lượng khí", RK),

ds("Một khung dây vuông cạnh 40 cm, điện trở 0,80 Ω, chuyển động đều 5,0 m/s đi qua vùng từ trường "
   "đều rộng 24 cm, B = 0,50 T.",
   [("Vì bề rộng vùng nhỏ hơn cạnh khung nên có giai đoạn không có dòng cảm ứng.", True,
     "Đúng. Khi khung vắt qua vùng, phần diện tích trong từ trường không đổi."),
    ("Tổng thời gian có dòng cảm ứng là 0,096 s.", True,
     "Đúng. Hai giai đoạn vào và ra, mỗi giai đoạn ứng với quãng đường 24 cm."),
    ("Cường độ dòng cảm ứng lúc khung đi vào là 1,25 A.", True,
     "Đúng. e = 0,50 · 0,40 · 5,0 = 1,0 V ⇒ i = 1,0/0,80 = 1,25 A."),
    ("Giai đoạn không có dòng cảm ứng kéo dài 0,048 s.", False,
     "Sai. Giai đoạn đó ứng với quãng đường 40 − 24 = 16 cm ⇒ t = 0,16/5,0 = 0,032 s.")],
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

ds("Một nguồn nhiệt đồng vị chứa 3,0 gam ²¹⁰Po (chu kì bán rã 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693.",
   [("Số hạt nhân ban đầu xấp xỉ 8,60·10²¹ hạt.", True,
     "Đúng. N₀ = (3,0/210)·6,02·10²³ ≈ 8,60·10²¹ hạt."),
    ("Công suất ban đầu của nguồn xấp xỉ 432 W.", True,
     "Đúng. H₀ = λN₀ ≈ 5,0·10¹⁴ Bq ⇒ P ≈ 5,0·10¹⁴ · 8,64·10⁻¹³ ≈ 432 W."),
    ("Sau 276 ngày, công suất của nguồn còn khoảng 108 W.", True,
     "Đúng. 276 ngày = 2 chu kì ⇒ P = 432/4 = 108 W."),
    ("Tổng năng lượng nguồn toả ra cho tới khi hết hẳn xấp xỉ 3,7·10⁹ J.", False,
     "Sai. E = N₀ · 5,4 · 1,6·10⁻¹³ = 8,60·10²¹ · 8,64·10⁻¹³ ≈ 7,4·10⁹ J, gấp đôi giá trị nêu ra.")],
   "Công suất và năng lượng của nguồn phóng xạ", RK),
],
P3=[
sa("Thả m kg nước đá ở −15 °C vào 3,0 kg nước ở 35 °C trong bình cách nhiệt. Khối lượng nước đá "
   "lớn nhất để đá tan hết bằng bao nhiêu kilôgam (làm tròn đến chữ số thập phân thứ ba)? "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   "1,187",
   "Nhiệt lượng nước nhả ra tối đa: 3,0 · 4200 · 35 = 441 000 J.\n"
   "Nhiệt lượng cần cho m kg đá: m·2100·15 + m·3,4·10⁵ = m·(31 500 + 340 000) = 371 500·m.\n"
   "371 500·m ≤ 441 000 ⇒ m ≤ 1,187 kg.",
   "Biện luận điều kiện", RK),

sa("Hai bình A (3,0 L) và B (5,0 L) nối bằng ống nhỏ có khoá, cùng nhiệt độ. Bình A chứa khí ở "
   "4,0·10⁵ Pa, bình B chứa cùng loại khí ở 2,0·10⁵ Pa. Sau khi mở khoá, áp suất chung bằng "
   "bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ hai)?",
   "2,75",
   "Tổng tích p·V: 4,0·10⁵ · 3,0 + 2,0·10⁵ · 5,0 = 12·10⁵ + 10·10⁵ = 22·10⁵ Pa·L.\n"
   "Thể tích tổng: 8,0 L ⇒ p = 22·10⁵/8,0 = 2,75·10⁵ Pa.",
   "Trộn hai lượng khí", RK),

sa("Một khung dây vuông cạnh 50 cm, chuyển động đều 4,0 m/s đi qua vùng từ trường đều rộng 30 cm. "
   "Tổng thời gian CÓ dòng điện cảm ứng trong khung bằng bao nhiêu giây (làm tròn đến chữ số "
   "thập phân thứ ba)?",
   "0,150",
   "Vì d < a nên dòng chỉ xuất hiện khi khung đi vào và khi đi ra, mỗi lần ứng với quãng đường "
   "d = 30 cm.\n"
   "Tổng quãng đường: 2 · 0,30 = 0,60 m ⇒ t = 0,60/4,0 = 0,150 s.",
   "Khung dây qua vùng từ trường hẹp", RK),

sa("Dùng prôtôn có động năng 6,00 MeV bắn vào hạt nhân ⁹₄Be đứng yên, sinh ra hạt α bay vuông góc "
   "với phương prôtôn và hạt nhân ⁶₃Li. Biết động năng hạt α là 4,50 MeV. Động năng của hạt nhân "
   "liti bằng bao nhiêu MeV?",
   "4",
   "Hạt α vuông góc với prôtôn nên p(Li)² = p(p)² + p(α)².\n"
   "Với p² = 2mW và m tỉ lệ số khối:  6·W(Li) = 1 · 6,00 + 4 · 4,50 = 24,00.\n"
   "W(Li) = 24,00/6 = 4,00 MeV.",
   "Bảo toàn động lượng hai chiều", RK),

sa("Một nhà máy truyền công suất không đổi. Ở điện áp U hiệu suất 75 %, cấp cho 7500 hộ dân. "
   "Tăng điện áp lên 5U thì cấp được cho bao nhiêu hộ dân?",
   "9900",
   "Hao phí ban đầu 25 %. Tăng U gấp 5 lần ⇒ hao phí giảm 25 lần, còn 1 %.\n"
   "Công suất tới nơi tiêu thụ tăng từ 75 % lên 99 %.\n"
   "Số hộ: 7500 · 99/75 = 7500 · 1,32 = 9900 hộ.",
   "Truyền tải điện năng – bài toán thực tiễn", RK),

sa("Một mẫu chất phóng xạ nguyên chất, sau thời gian t có 20 % số hạt nhân đã phân rã. "
   "Sau thời gian 3t, phần trăm số hạt nhân đã phân rã bằng bao nhiêu phần trăm "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "48,8",
   "Còn lại sau t: 80 % = 0,80.\n"
   "Sau 3t còn lại (0,80)³ = 0,512 = 51,2 %.\n"
   "Đã phân rã: 100 − 51,2 = 48,8 %.",
   "Bản chất hàm mũ của phân rã", RK),
])


# =====================================================================  ĐỀ 27
DE27 = dict(
ma="TH-Đề 27", ten="ĐỀ THI THỬ SỐ 27", muc="Khó – phân loại",
trongtam="Bài toán hệ thống, tối ưu hoá và phân tích năng lượng nhiều tầng",
P1=[
mc("Một bình cách nhiệt chứa 1,5 kg nước ở 60 °C. Thả vào đó một khối nước đá ở 0 °C, "
   "nhiệt độ cân bằng là 20 °C. Khối lượng nước đá đã thả xấp xỉ",
   ["0,54 kg.", "0,594 kg.", "0,72 kg.", "0,45 kg."],
   "B",
   "Nhiệt lượng nước nóng nhả ra: 1,5 · 4200 · (60 − 20) = 252 000 J.\n"
   "Nhiệt lượng nước đá thu vào (tan hết rồi hâm lên 20 °C):\n"
   "m·3,4·10⁵ + m·4200·20 = m·(340 000 + 84 000) = 424 000·m.\n"
   "424 000·m = 252 000 ⇒ m = 0,594 kg.",
   "Cân bằng nhiệt có chuyển thể", RK),

mc("Một động cơ nhiệt lí tưởng làm việc giữa nguồn nóng 500 K và nguồn lạnh 300 K. "
   "Hiệu suất lí thuyết cực đại bằng",
   ["30 %.", "40 %.", "60 %.", "80 %."],
   "B",
   "Hiệu suất cực đại lí thuyết: H = 1 − T(lạnh)/T(nóng) = 1 − 300/500 = 1 − 0,60 = 0,40 = 40 %.",
   "Hiệu suất động cơ nhiệt", RK),

mc("Một khối khí lí tưởng thực hiện chu trình gồm hai đẳng nhiệt và hai đẳng tích. "
   "Sau một chu trình, tổng nhiệt lượng khí nhận được",
   ["bằng 0.", "bằng công mà khí sinh ra.",
    "bằng độ tăng nội năng.", "luôn âm."],
   "B",
   "Chu trình kín nên ΔU = 0. Từ ΔU = A + Q ⇒ Q = −A: tổng nhiệt khí NHẬN bằng tổng công "
   "khí SINH ra.",
   "Chu trình kín", K),

mc("Một bình 12 L chứa khí ở 27 °C, áp suất 5,0·10⁵ Pa. Lấy bớt khí và hạ nhiệt độ xuống 7 °C "
   "sao cho áp suất còn 3,0·10⁵ Pa. Phần trăm khối lượng khí còn lại bằng",
   ["60,0 %.", "64,3 %.", "72,0 %.", "55,6 %."],
   "B",
   "Khối lượng khí tỉ lệ với p/T (thể tích không đổi).\n"
   "T₁ = 300 K; T₂ = 280 K.\n"
   "Tỉ số: (3,0/280)/(5,0/300) = (3,0·300)/(5,0·280) = 900/1400 ≈ 0,643 = 64,3 %.",
   "Phương trình Clapeyron", RK),

mc("Một khối khí lí tưởng có 0,50 mol ở 27 °C. Nếu cung cấp nhiệt lượng để nhiệt độ tăng lên "
   "127 °C trong điều kiện đẳng tích thì nội năng tăng, còn thể tích",
   ["tăng.", "không đổi.", "giảm.", "tăng gấp đôi."],
   "B",
   "Quá trình đẳng tích theo định nghĩa có thể tích không đổi; toàn bộ nhiệt lượng làm tăng "
   "nội năng vì A = 0.",
   "Quá trình đẳng tích", TB),

mc("Một thanh dẫn dài 60 cm, khối lượng 180 g nằm trên hai ray nằm ngang có hệ số ma sát 0,20 "
   "trong từ trường đều thẳng đứng B = 0,60 T. Cường độ dòng điện để thanh chuyển động với "
   "gia tốc 2,0 m/s² bằng (g = 10 m/s²)",
   ["1,0 A.", "2,0 A.", "1,6 A.", "2,4 A."],
   "B",
   "Lực ma sát: μ·m·g = 0,20 · 0,180 · 10 = 0,36 N.\n"
   "Lực từ cần thiết: F = m·a + F(ms) = 0,180 · 2,0 + 0,36 = 0,36 + 0,36 = 0,72 N.\n"
   "I = F/(B·ℓ) = 0,72/(0,60 · 0,60) = 0,72/0,36 = 2,0 A.",
   "Lực từ và động lực học", RK, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một khung dây kín rơi thẳng đứng đi ra khỏi vùng từ trường đều. Nếu tăng gấp đôi khối lượng "
   "khung (giữ nguyên kích thước và điện trở) thì tốc độ giới hạn",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "v = m·g·R/(B²a²) tỉ lệ THUẬN với khối lượng. Khung nặng gấp đôi thì tốc độ giới hạn "
   "tăng gấp đôi.",
   "Tốc độ giới hạn của khung rơi", K),

mc("Một máy biến áp lí tưởng có ba cuộn: sơ cấp 1000 vòng nối vào 200 V; hai cuộn thứ cấp 150 vòng "
   "và 250 vòng nối với hai điện trở 9,0 Ω và 25 Ω. Công suất tổng bằng",
   ["100 W.", "200 W.", "150 W.", "250 W."],
   "B",
   "Cuộn 150 vòng: U = 200 · 0,15 = 30 V ⇒ P₁ = 900/9,0 = 100 W.\n"
   "Cuộn 250 vòng: U = 200 · 0,25 = 50 V ⇒ P₂ = 2500/25 = 100 W.\n"
   "Tổng: 100 + 100 = 200 W.",
   "Máy biến áp nhiều cuộn thứ cấp", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Điện năng truyền qua hai cấp biến áp: tăng áp 1 : 30 rồi hạ áp 25 : 1. Điện áp máy phát 6,0 kV, "
   "công suất 4,5 MW, điện trở đường dây 12 Ω. Điện áp đầu ra của máy hạ áp xấp xỉ",
   ["7200 V.", "7188 V.", "7000 V.", "7250 V."],
   "B",
   "Điện áp đầu dây: 30 · 6,0 = 180 kV.\n"
   "Dòng trên dây: I = 4,5·10⁶/(180·10³) = 25 A.\n"
   "Sụt áp: ΔU = 12 · 25 = 300 V.\n"
   "Điện áp cuối dây: 180 000 − 300 = 179 700 V.\n"
   "Qua máy hạ áp 25 : 1 ⇒ U(ra) = 179 700/25 = 7188 V.",
   "Hệ truyền tải hai cấp biến áp", RK, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

mc("Một hạt nhân ²³⁴₉₀Th đứng yên phóng xạ α, toả 4,80 MeV. Động năng hạt α xấp xỉ "
   "(coi khối lượng tỉ lệ số khối)",
   ["4,72 MeV.", "4,60 MeV.", "4,80 MeV.", "0,08 MeV."],
   "A",
   "Hạt nhân con có A = 230.\n"
   "W(α) = ΔE · 230/234 = 4,80 · 230/234 ≈ 4,72 MeV.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một mẫu chất phóng xạ có chu kì bán rã 7,0 ngày. Sau bao lâu thì tỉ số giữa số hạt nhân con "
   "và số hạt nhân mẹ còn lại bằng 3?",
   ["7,0 ngày.", "14,0 ngày.", "21,0 ngày.", "28,0 ngày."],
   "B",
   "2ⁿ − 1 = 3 ⇒ 2ⁿ = 4 ⇒ n = 2 chu kì.\n"
   "t = 2 · 7,0 = 14,0 ngày.",
   "Tỉ số hạt nhân con và mẹ", K),

mc("Một mẫu chứa hai đồng vị phóng xạ có cùng số hạt nhân ban đầu, chu kì bán rã lần lượt 5,0 giờ "
   "và 15 giờ. Sau 15 giờ, tỉ số số hạt nhân đồng vị thứ nhất trên thứ hai bằng",
   ["1 : 2.", "1 : 4.", "1 : 8.", "1 : 3."],
   "B",
   "Đồng vị 1 trải qua 3 chu kì: còn N₀/8.\n"
   "Đồng vị 2 trải qua 1 chu kì: còn N₀/2.\n"
   "Tỉ số: (N₀/8)/(N₀/2) = 1/4 = 1 : 4.",
   "Hỗn hợp hai đồng vị", K),

mc("Cho phản ứng ²³⁵₉₂U + ¹₀n → ⁹⁵₄₀Zr + ¹³⁸₅₂Te + k·¹₀n. Giá trị của k bằng",
   ["2.", "3.", "4.", "1."],
   "B",
   "Bảo toàn số khối: 235 + 1 = 95 + 138 + k ⇒ 236 = 233 + k ⇒ k = 3.\n"
   "Kiểm tra điện tích: 92 = 40 + 52 ✓.",
   "Phản ứng phân hạch", K, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Một nguồn phóng xạ có công suất ban đầu 320 W và chu kì bán rã 18 năm. Sau 54 năm, "
   "công suất còn",
   ["80 W.", "40 W.", "160 W.", "20 W."],
   "B",
   "n = 54/18 = 3 chu kì ⇒ P = 320/2³ = 320/8 = 40 W.",
   "Công suất nguồn phóng xạ", K),

mc("Trong chuỗi phân rã ²³⁸U → ²⁰⁶Pb, số nơtron của hạt nhân giảm nhiều hơn số prôtôn bao nhiêu "
   "đơn vị?",
   ["8.", "12.", "10.", "6."],
   "B",
   "Số prôtôn giảm: 92 − 82 = 10.\n"
   "Số nơtron giảm: (238 − 92) − (206 − 82) = 146 − 124 = 22.\n"
   "Chênh lệch: 22 − 10 = 12 đơn vị.",
   "Chuỗi phân rã", RK),

mc("Một mẫu chất phóng xạ nguyên chất có độ phóng xạ ban đầu H₀ và chu kì bán rã T. "
   "Số phân rã xảy ra trong khoảng thời gian từ 0 đến T bằng",
   ["H₀·T.", "H₀·T/(2·ln2).", "H₀·T/ln2.", "H₀·T/2."],
   "B",
   "Tổng số hạt nhân ban đầu: N₀ = H₀/λ = H₀·T/ln2.\n"
   "Sau một chu kì bán rã, một nửa số đó đã phân rã: N₀/2 = H₀·T/(2·ln2).",
   "Độ phóng xạ và tổng số phân rã", RK),

mc("Nếu năng lượng liên kết riêng của các mảnh vỡ lớn hơn của hạt nhân mẹ 0,85 MeV/nuclêôn thì "
   "phân hạch một hạt nhân ²³⁵U toả ra xấp xỉ",
   ["100 MeV.", "200 MeV.", "300 MeV.", "150 MeV."],
   "B",
   "ΔE ≈ 0,85 · 235 ≈ 200 MeV — đúng với giá trị quen thuộc của phân hạch urani.",
   "Năng lượng phân hạch", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Trong bốn phát biểu sau về nhiệt động lực học, phát biểu nào SAI?",
   ["Nội năng là hàm trạng thái.",
    "Có thể chế tạo động cơ nhiệt chuyển hoàn toàn nhiệt thành công.",
    "Nhiệt truyền tự phát từ vật nóng sang vật lạnh.",
    "Trong chu trình kín, độ biến thiên nội năng bằng không."],
   "B",
   "Nguyên lí thứ hai của nhiệt động lực học khẳng định không thể chế tạo động cơ nhiệt chuyển "
   "hoàn toàn nhiệt lượng nhận được thành công: luôn phải thải một phần cho nguồn lạnh.",
   "Nguyên lí thứ hai nhiệt động lực học", K),
],
P2=[
ds("Một động cơ nhiệt hoạt động giữa nguồn nóng 600 K và nguồn lạnh 300 K, mỗi chu trình nhận "
   "2000 J từ nguồn nóng và sinh công 700 J.",
   [("Hiệu suất thực tế của động cơ là 35 %.", True,
     "Đúng. H = 700/2000 = 0,35."),
    ("Hiệu suất lí thuyết cực đại là 50 %.", True,
     "Đúng. H(max) = 1 − 300/600 = 0,50."),
    ("Hiệu suất thực tế nhỏ hơn hiệu suất lí thuyết cực đại.", True,
     "Đúng. 35 % < 50 %, phù hợp với mọi động cơ thực."),
    ("Có thể cải tiến động cơ để hiệu suất đạt 60 % mà vẫn giữ hai nguồn nhiệt đó.", False,
     "Sai. Không động cơ nào hoạt động giữa hai nguồn 600 K và 300 K có thể vượt quá 50 %.")],
   "Hiệu suất động cơ nhiệt", RK),

ds("Một bình 12 L chứa khí lí tưởng ở 27 °C, áp suất 5,0·10⁵ Pa. Sau khi lấy bớt khí và hạ nhiệt "
   "độ xuống 7 °C, áp suất còn 3,0·10⁵ Pa.",
   [("Nhiệt độ đầu và cuối lần lượt là 300 K và 280 K.", True,
     "Đúng. 27 + 273 = 300 K;  7 + 273 = 280 K."),
    ("Khối lượng khí trong bình tỉ lệ với tỉ số p/T.", True,
     "Đúng. Từ pV = (m/M)RT với V không đổi."),
    ("Khối lượng khí còn lại chiếm khoảng 64,3 % ban đầu.", True,
     "Đúng. (3,0/280)/(5,0/300) = 900/1400 ≈ 0,643."),
    ("Phần khí đã lấy ra chiếm 40 % khối lượng ban đầu.", False,
     "Sai. Đã lấy ra khoảng 100 − 64,3 = 35,7 %. Con số 40 % là kết quả khi chỉ so sánh áp suất "
     "mà bỏ qua thay đổi nhiệt độ.")],
   "Phương trình Clapeyron", RK),

ds("Điện năng truyền qua hai cấp biến áp: máy tăng áp tỉ số 1 : 30 và máy hạ áp tỉ số 25 : 1. "
   "Điện áp máy phát 6,0 kV, công suất truyền 4,5 MW, điện trở đường dây 12 Ω.",
   [("Điện áp ở đầu đường dây là 180 kV.", True,
     "Đúng. 30 · 6,0 = 180 kV."),
    ("Cường độ dòng điện trên đường dây là 25 A.", True,
     "Đúng. I = 4,5·10⁶/(180·10³) = 25 A."),
    ("Công suất hao phí trên đường dây là 7,5 kW.", True,
     "Đúng. ΔP = 12 · 25² = 12 · 625 = 7500 W."),
    ("Điện áp đầu ra của máy hạ áp đúng bằng 7200 V.", False,
     "Sai. Phải trừ độ sụt áp 300 V trên đường dây: (180 000 − 300)/25 = 7188 V.")],
   "Hệ truyền tải hai cấp biến áp", RK, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

ds("Xét chuỗi phân rã từ ²³⁸₉₂U tới hạt nhân bền ²⁰⁶₈₂Pb.",
   [("Số prôtôn giảm 10 đơn vị.", True,
     "Đúng. 92 − 82 = 10."),
    ("Số nơtron giảm 22 đơn vị.", True,
     "Đúng. 146 − 124 = 22."),
    ("Chuỗi gồm 8 lần phân rã α và 6 lần phân rã β⁻.", True,
     "Đúng. (238 − 206)/4 = 8 lần α; Z sau 8 lần α là 76, cần 6 lần β⁻ để đạt 82."),
    ("Mỗi lần phân rã β⁻ làm số nơtron tăng thêm một đơn vị.", False,
     "Sai. Phân rã β⁻ là quá trình một nơtron biến thành prôtôn, nên số nơtron GIẢM một đơn vị "
     "còn số prôtôn tăng một đơn vị.")],
   "Chuỗi phân rã", RK),
],
P3=[
sa("Một bình cách nhiệt chứa 2,0 kg nước ở 70 °C. Thả vào đó một khối nước đá ở 0 °C, nhiệt độ "
   "cân bằng là 25 °C. Khối lượng nước đá đã thả bằng bao nhiêu kilôgam "
   "(làm tròn đến chữ số thập phân thứ ba)? Cho λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K).",
   "0,849",
   "Nhiệt lượng nước nóng nhả ra: 2,0 · 4200 · (70 − 25) = 378 000 J.\n"
   "Nhiệt lượng nước đá thu vào: m·3,4·10⁵ + m·4200·25 = m·(340 000 + 105 000) = 445 000·m.\n"
   "445 000·m = 378 000 ⇒ m = 0,849 kg.",
   "Cân bằng nhiệt có chuyển thể", RK),

sa("Một bình 15 L chứa khí lí tưởng ở 27 °C, áp suất 4,0·10⁵ Pa. Sau khi lấy bớt khí và hạ nhiệt "
   "độ xuống −13 °C, áp suất còn 2,6·10⁵ Pa. Khối lượng khí còn lại chiếm bao nhiêu phần trăm "
   "khối lượng ban đầu (làm tròn đến chữ số thập phân thứ nhất)?",
   "75,0",
   "Khối lượng khí tỉ lệ với p/T khi thể tích không đổi.\n"
   "T₁ = 300 K;  T₂ = 260 K.\n"
   "Tỉ số: (2,6/260)/(4,0/300) = (2,6·300)/(4,0·260) = 780/1040 = 0,750 = 75,0 %.",
   "Phương trình Clapeyron", RK),

sa("Một khung dây vuông cạnh 25 cm, khối lượng 40 g, điện trở 0,20 Ω rơi thẳng đứng đi ra khỏi "
   "vùng từ trường đều B = 0,50 T. Tốc độ giới hạn của khung bằng bao nhiêu mét trên giây? "
   "Lấy g = 10 m/s².",
   "5,12",
   "Ở tốc độ giới hạn: B²a²v/R = m·g.\n"
   "v = m·g·R/(B²a²) = 0,040 · 10 · 0,20/(0,25 · 0,0625) = 0,080/0,015625 = 5,12 m/s.",
   "Tốc độ giới hạn của khung rơi", RK),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 1200 vòng nối vào 240 V và hai cuộn thứ cấp 180 vòng "
   "và 300 vòng nối với hai điện trở 12 Ω và 30 Ω. Công suất tổng mà máy tiêu thụ bằng bao nhiêu oát?",
   "228",
   "Cuộn 180 vòng: U = 240 · 180/1200 = 36 V ⇒ P₁ = 36²/12 = 1296/12 = 108 W.\n"
   "Cuộn 300 vòng: U = 240 · 300/1200 = 60 V ⇒ P₂ = 60²/30 = 3600/30 = 120 W.\n"
   "Tổng: 108 + 120 = 228 W.",
   "Máy biến áp nhiều cuộn thứ cấp", RK),

sa("Một hạt nhân ²³⁰₉₀Th đứng yên phóng xạ α, toả 4,77 MeV. Động năng của hạt α bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)? Coi khối lượng tỉ lệ với số khối.",
   "4,69",
   "Hạt nhân con có A = 226.\n"
   "W(α) = ΔE · 226/230 = 4,77 · 226/230 = 1078,02/230 ≈ 4,69 MeV.",
   "Bảo toàn động lượng trong phân rã", RK),

sa("Một nguồn phóng xạ có độ phóng xạ ban đầu 4,0·10⁵ Bq và chu kì bán rã 6,0 giờ. "
   "Tổng số phân rã xảy ra cho tới khi mẫu phân rã hết bằng bao nhiêu "
   "(viết dưới dạng x·10¹⁰, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)? "
   "Lấy ln2 ≈ 0,693.",
   "1,2",
   "T = 6,0 · 3600 = 21 600 s.\n"
   "N₀ = H₀·T/ln2 = 4,0·10⁵ · 21 600/0,693 = 8,64·10⁹/0,693 ≈ 1,2·10¹⁰ hạt.",
   "Độ phóng xạ và tổng số phân rã", RK),
])


# =====================================================================  ĐỀ 28
DE28 = dict(
ma="TH-Đề 28", ten="ĐỀ THI THỬ SỐ 28", muc="Khó – phân loại",
trongtam="Bài toán ghép nhiều chương, đòi hỏi lập hệ phương trình và biện luận",
P1=[
mc("Trộn ba khối nước: 1,0 kg ở 20 °C, 2,0 kg ở 40 °C và 3,0 kg ở 80 °C. Nhiệt độ cân bằng bằng",
   ["50,0 °C.", "56,7 °C.", "46,7 °C.", "60,0 °C."],
   "B",
   "Nhiệt độ cân bằng là trung bình có trọng số theo khối lượng:\n"
   "t = (1,0·20 + 2,0·40 + 3,0·80)/(1,0 + 2,0 + 3,0) = (20 + 80 + 240)/6,0 = 340/6,0 ≈ 56,7 °C.",
   "Phương trình cân bằng nhiệt", K),

mc("Một bếp cung cấp nhiệt với công suất không đổi. Đun 1,0 kg nước đá ở −20 °C, sau 100 s nước đá "
   "đạt 0 °C. Thời gian tiếp theo để đá tan hết bằng "
   "(c(đá) = 2100 J/(kg·K); λ = 3,4·10⁵ J/kg)",
   ["405 s.", "810 s.", "1620 s.", "202 s."],
   "B",
   "Công suất bếp: P = (1,0 · 2100 · 20)/100 = 42 000/100 = 420 W.\n"
   "Nhiệt để tan hết đá: Q = 1,0 · 3,4·10⁵ = 340 000 J.\n"
   "t = 340 000/420 ≈ 810 s.",
   "Đọc đồ thị chuyển thể", RK),

mc("Một khối khí lí tưởng có 0,20 mol ở 27 °C, thể tích 4,155 L. Nếu nung nóng đẳng áp tới thể tích "
   "8,310 L thì nhiệt độ cuối bằng",
   ["327 °C.", "600 °C.", "54 °C.", "873 °C."],
   "A",
   "Đẳng áp: T₂ = T₁ · V₂/V₁ = 300 · 2 = 600 K.\n"
   "t₂ = 600 − 273 = 327 °C.",
   "Định luật Charles", K),

mc("Trong bài trên, áp suất khí bằng (R = 8,31 J/(mol·K))",
   ["0,60·10⁵ Pa.", "1,2·10⁵ Pa.", "2,4·10⁵ Pa.", "0,30·10⁵ Pa."],
   "B",
   "p = nRT/V = 0,20 · 8,31 · 300/(4,155·10⁻³) = 498,6/4,155·10⁻³ = 1,2·10⁵ Pa.",
   "Phương trình Clapeyron", K),

mc("Hai bình A và B cùng thể tích, cùng nhiệt độ, chứa cùng loại khí với áp suất 2,0·10⁵ Pa và "
   "6,0·10⁵ Pa. Nối hai bình bằng ống nhỏ. Áp suất chung bằng",
   ["3,0·10⁵ Pa.", "4,0·10⁵ Pa.", "8,0·10⁵ Pa.", "2,0·10⁵ Pa."],
   "B",
   "Số mol tỉ lệ với p (cùng V và T). Tổng quy đổi: 2,0 + 6,0 = 8,0 (đơn vị 10⁵ Pa·V).\n"
   "Thể tích tổng gấp đôi nên p = 8,0/2 = 4,0·10⁵ Pa — đúng bằng trung bình cộng vì hai bình "
   "cùng thể tích.",
   "Trộn hai lượng khí", K),

mc("Một đoạn dây dẫn dài 30 cm, khối lượng 45 g được treo nằm ngang bằng hai sợi dây mảnh trong từ "
   "trường đều nằm ngang vuông góc với đoạn dây. Muốn lực căng hai sợi dây giảm còn một nửa so với "
   "khi không có dòng thì tích B·I phải bằng (g = 10 m/s²)",
   ["0,75.", "1,50.", "0,375.", "0,15."],
   "A",
   "Trọng lực: P = 0,045 · 10 = 0,45 N.\n"
   "Muốn lực căng còn một nửa thì lực từ hướng lên và bằng P/2 = 0,225 N.\n"
   "B·I·ℓ = 0,225 ⇒ B·I = 0,225/0,30 = 0,75 (đơn vị SI).",
   "Cân bằng lực có lực từ", RK),

mc("Một khung dây kín hình vuông cạnh a chuyển động đều với tốc độ v đi vào vùng từ trường đều B, "
   "điện trở R. Nếu đồng thời tăng a lên gấp đôi và giảm v còn một nửa thì cường độ dòng cảm ứng",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "A",
   "i = B·a·v/R tỉ lệ với tích a·v. a tăng 2 lần, v giảm 2 lần nên tích không đổi, "
   "do đó dòng cảm ứng không đổi.",
   "Phân tích tỉ lệ", K),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 800 vòng. Khi mắc vào mạng 220 V, cuộn thứ cấp cho "
   "điện áp 55 V. Nếu muốn điện áp thứ cấp là 33 V thì phải BỚT đi bao nhiêu vòng ở cuộn thứ cấp?",
   ["60 vòng.", "80 vòng.", "100 vòng.", "120 vòng."],
   "B",
   "Số vòng thứ cấp ban đầu: N₂ = 800 · 55/220 = 200 vòng.\n"
   "Số vòng cần có: N₂' = 800 · 33/220 = 120 vòng.\n"
   "Phải bớt: 200 − 120 = 80 vòng.",
   "Máy biến áp – bài toán ngược", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 7,2 MW ở điện áp 36 kV trên đường dây có điện trở 9,0 Ω. "
   "Hiệu suất truyền tải bằng",
   ["90,0 %.", "95,0 %.", "97,5 %.", "99,0 %."],
   "B",
   "I = 7,2·10⁶/(36·10³) = 200 A.\n"
   "ΔP = 9,0 · 200² = 9,0 · 4,0·10⁴ = 3,6·10⁵ W = 0,36 MW.\n"
   "H = (7,20 − 0,36)/7,20 = 6,84/7,20 = 0,95 = 95,0 %.",
   "Hiệu suất truyền tải", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Hạt nhân X có số khối A và năng lượng liên kết riêng ε; hạt nhân Y có số khối 2A và năng lượng "
   "liên kết riêng 0,9ε. Tỉ số năng lượng liên kết của Y so với X bằng",
   ["0,90.", "1,80.", "2,00.", "0,45."],
   "B",
   "W(X) = ε·A;  W(Y) = 0,9ε · 2A = 1,8·ε·A.\n"
   "Tỉ số: 1,8.",
   "Năng lượng liên kết", K),

mc("Một mẫu chất phóng xạ nguyên chất. Sau 30 phút, số hạt nhân còn lại bằng 1/8 ban đầu. "
   "Sau 50 phút kể từ lúc đầu, số hạt nhân còn lại chiếm",
   ["3,1 %.", "6,3 %.", "1,6 %.", "12,5 %."],
   "A",
   "Từ 1/8 = 2⁻³ suy ra 30 phút = 3 chu kì ⇒ T = 10 phút.\n"
   "Sau 50 phút: n = 5 chu kì ⇒ còn 2⁻⁵ = 1/32 = 3,125 ≈ 3,1 %.",
   "Định luật phóng xạ", K),

mc("Một hạt nhân đứng yên phân rã thành hai hạt có số khối 4 và 208. Tỉ số tốc độ của hạt nhẹ "
   "so với hạt nặng bằng",
   ["4 : 208.", "52 : 1.", "1 : 52.", "208 : 4 lần bình phương."],
   "B",
   "Bảo toàn động lượng: m₁v₁ = m₂v₂ ⇒ v₁/v₂ = m₂/m₁ = 208/4 = 52.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một lò phản ứng cần thay nhiên liệu khi đã tiêu thụ 1,5 tấn ²³⁵U. Nếu công suất nhiệt là "
   "2500 MW thì thời gian giữa hai lần thay nhiên liệu xấp xỉ (200 MeV mỗi phân hạch)",
   ["285 ngày.", "569 ngày.", "1140 ngày.", "142 ngày."],
   "B",
   "Số hạt nhân trong 1,5 tấn: N = (1,5·10⁶/235)·6,02·10²³ ≈ 3,843·10²⁷ hạt.\n"
   "Tổng năng lượng: E = 3,843·10²⁷ · 3,2·10⁻¹¹ ≈ 1,230·10¹⁷ J.\n"
   "Thời gian: t = 1,230·10¹⁷/(2,5·10⁹) = 4,92·10⁷ s ≈ 569 ngày.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

mc("Một chất phóng xạ có chu kì bán rã T. Sau khoảng thời gian nào thì số hạt nhân đã phân rã "
   "gấp 9 lần số hạt nhân còn lại (ln2 ≈ 0,693)?",
   ["3,00·T.", "3,32·T.", "3,50·T.", "4,00·T."],
   "B",
   "2ⁿ − 1 = 9 ⇒ 2ⁿ = 10 ⇒ n = ln10/ln2 = 2,303/0,693 ≈ 3,32.\n"
   "Vậy t ≈ 3,32·T.",
   "Tỉ số hạt nhân con và mẹ", RK),

mc("Một mẫu chứa hai đồng vị phóng xạ có cùng độ phóng xạ ban đầu, chu kì bán rã 2,0 giờ và "
   "6,0 giờ. Sau 6,0 giờ, độ phóng xạ tổng so với ban đầu chiếm",
   ["31,25 %.", "50,00 %.", "12,50 %.", "62,50 %."],
   "A",
   "Đồng vị 1 (3 chu kì): còn H₀/8. Đồng vị 2 (1 chu kì): còn H₀/2.\n"
   "Tổng: H₀/8 + H₀/2 = 5H₀/8, so với tổng ban đầu 2H₀ là (5/8)/2 = 5/16 = 31,25 %.",
   "Hỗn hợp hai đồng vị", RK),

mc("Trong phản ứng hạt nhân toả năng lượng ΔE, nếu hai hạt tới đứng yên và hai hạt sinh ra có "
   "số khối A₁ và A₂ thì động năng hạt thứ nhất bằng",
   ["ΔE·A₁/(A₁ + A₂).", "ΔE·A₂/(A₁ + A₂).",
    "ΔE/2.", "ΔE·A₁/A₂."],
   "B",
   "Bảo toàn động lượng cho hai hạt cùng độ lớn động lượng.\n"
   "W = p²/(2m) nên W₁/W₂ = A₂/A₁; kết hợp W₁ + W₂ = ΔE được W₁ = ΔE·A₂/(A₁ + A₂).",
   "Bảo toàn động lượng trong phản ứng", K),

mc("Một nguồn phóng xạ dùng trong y tế phải có độ phóng xạ tối thiểu 500 MBq khi sử dụng. "
   "Nếu khi xuất xưởng độ phóng xạ là 8000 MBq và chu kì bán rã 3,0 ngày thì thời hạn sử dụng "
   "tối đa bằng",
   ["9,0 ngày.", "12,0 ngày.", "15,0 ngày.", "6,0 ngày."],
   "B",
   "8000 → 500 là giảm 16 lần = 2⁴ ⇒ n = 4 chu kì.\n"
   "t = 4 · 3,0 = 12,0 ngày.",
   "Ứng dụng thực tiễn của định luật phóng xạ", K),

mc("Trong bốn nhận định sau về nhiệt và công, nhận định nào ĐÚNG?",
   ["Nhiệt lượng là một hàm trạng thái.",
    "Nội năng là hàm trạng thái, còn nhiệt lượng và công phụ thuộc quá trình.",
    "Công là hàm trạng thái.", "Cả nhiệt lượng và công đều là hàm trạng thái."],
   "B",
   "Nội năng chỉ phụ thuộc trạng thái hiện tại của hệ. Nhiệt lượng và công phụ thuộc CÁCH hệ "
   "chuyển từ trạng thái này sang trạng thái khác, nên không phải hàm trạng thái.",
   "Hàm trạng thái", K),
],
P2=[
ds("Một bếp cung cấp nhiệt với công suất không đổi, đun 1,0 kg nước đá ở −20 °C. Sau 100 giây "
   "nước đá đạt 0 °C. Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   [("Công suất của bếp là 420 W.", True,
     "Đúng. P = (1,0 · 2100 · 20)/100 = 420 W."),
    ("Thời gian để nước đá tan hết xấp xỉ 810 giây.", True,
     "Đúng. t = 340 000/420 ≈ 810 s."),
    ("Thời gian đun nước từ 0 °C tới sôi xấp xỉ 1000 giây.", True,
     "Đúng. Q = 1,0 · 4200 · 100 = 420 000 J ⇒ t = 420 000/420 = 1000 s."),
    ("Giai đoạn làm tan nước đá tốn nhiều thời gian nhất trong ba giai đoạn.", False,
     "Sai. Ba giai đoạn lần lượt tốn 100 s, 810 s và 1000 s; giai đoạn ĐUN NƯỚC TỚI SÔI mới "
     "tốn nhiều thời gian nhất.")],
   "Đọc đồ thị chuyển thể", RK, fig="n_dt_nuocda", cap="Đồ thị nhiệt độ theo thời gian"),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 800 vòng mắc vào mạng 220 V, cuộn thứ cấp cho điện áp "
   "55 V.",
   [("Số vòng của cuộn thứ cấp là 200 vòng.", True,
     "Đúng. N₂ = 800 · 55/220 = 200 vòng."),
    ("Đây là máy hạ áp.", True,
     "Đúng. U₂ < U₁ nên điện áp giảm."),
    ("Muốn điện áp thứ cấp còn 33 V thì phải bớt 80 vòng.", True,
     "Đúng. Cần 800 · 33/220 = 120 vòng, tức bớt 200 − 120 = 80 vòng."),
    ("Nếu nối cuộn 200 vòng vào mạng 220 V thì cuộn 800 vòng cho điện áp 55 V.", False,
     "Sai. Lúc đó cuộn 800 vòng đóng vai trò thứ cấp và cho điện áp 220 · 800/200 = 880 V, "
     "tức máy trở thành máy TĂNG áp.")],
   "Máy biến áp – bài toán ngược", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Một lò phản ứng công suất nhiệt 2500 MW dùng ²³⁵U, mỗi phân hạch toả 200 MeV. "
   "Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   [("Số phân hạch mỗi giây xấp xỉ 7,81·10¹⁹.", True,
     "Đúng. 2,5·10⁹/3,2·10⁻¹¹ ≈ 7,81·10¹⁹."),
    ("Số hạt nhân trong 1,5 tấn ²³⁵U xấp xỉ 3,84·10²⁷ hạt.", True,
     "Đúng. N = (1,5·10⁶/235)·6,02·10²³ ≈ 3,843·10²⁷ hạt."),
    ("Thời gian để tiêu thụ hết 1,5 tấn nhiên liệu xấp xỉ 569 ngày.", True,
     "Đúng. t = 3,843·10²⁷/7,81·10¹⁹ ≈ 4,92·10⁷ s ≈ 569 ngày."),
    ("Nếu tăng công suất nhiệt lên gấp đôi thì thời gian giữa hai lần thay nhiên liệu cũng "
     "tăng gấp đôi.", False,
     "Sai. Công suất gấp đôi nghĩa là tiêu thụ nhiên liệu nhanh gấp đôi, nên thời gian giữa hai "
     "lần thay nhiên liệu GIẢM còn một nửa.")],
   "Nhiên liệu của nhà máy điện hạt nhân", RK, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

ds("Một mẫu chứa hai đồng vị phóng xạ độc lập có cùng độ phóng xạ ban đầu H₀, chu kì bán rã "
   "2,0 giờ và 6,0 giờ.",
   [("Sau 6,0 giờ, độ phóng xạ của đồng vị thứ nhất còn H₀/8.", True,
     "Đúng. Đồng vị 1 trải qua 3 chu kì."),
    ("Sau 6,0 giờ, độ phóng xạ của đồng vị thứ hai còn H₀/2.", True,
     "Đúng. Đồng vị 2 trải qua đúng 1 chu kì."),
    ("Sau 6,0 giờ, tổng độ phóng xạ bằng 5H₀/8.", True,
     "Đúng. H₀/8 + H₀/2 = 5H₀/8."),
    ("Sau 6,0 giờ, tổng độ phóng xạ còn đúng một nửa giá trị ban đầu.", False,
     "Sai. Tổng ban đầu là 2H₀; sau 6,0 giờ còn 5H₀/8, tức 31,25 % chứ không phải 50 %.")],
   "Hỗn hợp hai đồng vị", RK),
],
P3=[
sa("Trộn ba khối nước: 2,0 kg ở 15 °C, 3,0 kg ở 45 °C và 5,0 kg ở 75 °C. Nhiệt độ cân bằng bằng "
   "bao nhiêu độ Celsius (làm tròn đến chữ số thập phân thứ nhất)?",
   "54,0",
   "t = (2,0·15 + 3,0·45 + 5,0·75)/(2,0 + 3,0 + 5,0)\n"
   "= (30 + 135 + 375)/10 = 540/10 = 54,0 °C.",
   "Phương trình cân bằng nhiệt", K),

sa("Hai bình cùng thể tích, cùng nhiệt độ, chứa cùng loại khí ở áp suất 3,0·10⁵ Pa và 9,0·10⁵ Pa. "
   "Nối hai bình lại. Áp suất chung bằng bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x)?",
   "6",
   "Hai bình cùng thể tích nên áp suất chung là trung bình cộng:\n"
   "p = (3,0 + 9,0)/2 = 6,0·10⁵ Pa.",
   "Trộn hai lượng khí", K),

sa("Một đoạn dây dẫn dài 40 cm, khối lượng 60 g được treo nằm ngang bằng hai sợi dây mảnh trong "
   "từ trường đều nằm ngang vuông góc với đoạn dây. Muốn lực căng hai sợi dây bằng một phần ba "
   "giá trị khi không có dòng thì tích B·I phải bằng bao nhiêu (đơn vị SI, làm tròn đến chữ số "
   "thập phân thứ nhất)? Lấy g = 10 m/s².",
   "1,0",
   "Trọng lực: P = 0,060 · 10 = 0,60 N.\n"
   "Lực căng còn 1/3 nghĩa là lực từ hướng lên và bằng (2/3)·P = 0,40 N.\n"
   "B·I·ℓ = 0,40 ⇒ B·I = 0,40/0,40 = 1,0 (đơn vị SI).",
   "Cân bằng lực có lực từ", RK),

sa("Truyền công suất 9,6 MW ở điện áp 48 kV trên đường dây có điện trở 12 Ω. "
   "Hiệu suất truyền tải bằng bao nhiêu phần trăm?",
   "95",
   "I = P/U = 9,6·10⁶/(48·10³) = 200 A.\n"
   "ΔP = 12 · 200² = 12 · 4,0·10⁴ = 4,8·10⁵ W = 0,48 MW.\n"
   "H = (9,60 − 0,48)/9,60 = 9,12/9,60 = 0,95 = 95 %.",
   "Hiệu suất truyền tải", K),

sa("Một mẫu chất phóng xạ nguyên chất. Sau 40 phút, số hạt nhân còn lại bằng 1/16 ban đầu. "
   "Sau 70 phút kể từ lúc đầu, số hạt nhân còn lại chiếm bao nhiêu phần trăm "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "0,8",
   "Từ 1/16 = 2⁻⁴ suy ra 40 phút = 4 chu kì ⇒ T = 10 phút.\n"
   "Sau 70 phút: n = 7 chu kì ⇒ còn 2⁻⁷ = 1/128 ≈ 0,0078 = 0,8 %.",
   "Định luật phóng xạ", RK),

sa("Một chất phóng xạ có chu kì bán rã T. Sau khoảng thời gian bằng bao nhiêu lần T thì số hạt nhân "
   "đã phân rã gấp 19 lần số hạt nhân còn lại (làm tròn đến chữ số thập phân thứ hai)? "
   "Lấy ln2 ≈ 0,693.",
   "4,32",
   "2ⁿ − 1 = 19 ⇒ 2ⁿ = 20.\n"
   "n = ln20/ln2 = 2,996/0,693 ≈ 4,32.",
   "Tỉ số hạt nhân con và mẹ", RK),
])


# =====================================================================  ĐỀ 29
DE29 = dict(
ma="TH-Đề 29", ten="ĐỀ THI THỬ SỐ 29", muc="Khó – phân loại",
trongtam="Tổng hợp bốn chương, chú trọng bài toán nhiều giai đoạn và biện luận điều kiện",
P1=[
mc("Thả 0,50 kg nước đá ở 0 °C vào 2,0 kg nước ở 30 °C trong bình cách nhiệt. "
   "Cho c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg. Nhiệt độ cân bằng bằng",
   ["0 °C.", "7,8 °C.", "15,6 °C.", "3,9 °C."],
   "B",
   "Nhiệt lượng nước toả ra khi hạ xuống 0 °C: Q(toả) = 2,0 · 4200 · 30 = 252 000 J.\n"
   "Nhiệt lượng cần để đá tan hết: Q(tan) = 0,50 · 3,4·10⁵ = 170 000 J.\n"
   "Vì 252 000 > 170 000 nên đá tan hết và hỗn hợp nóng lên trên 0 °C.\n"
   "Nhiệt dư: 252 000 − 170 000 = 82 000 J làm nóng 2,5 kg nước:\n"
   "Δt = 82 000/(2,5 · 4200) = 82 000/10 500 ≈ 7,8 °C.",
   "Cân bằng nhiệt có chuyển thể", RK),

mc("Một lượng khí giãn nở đẳng áp ở áp suất 2,0·10⁵ Pa, thể tích tăng từ 3,0 L lên 8,0 L và nhận "
   "nhiệt lượng 1500 J. Độ biến thiên nội năng của khí bằng",
   ["1000 J.", "2500 J.", "500 J.", "−500 J."],
   "C",
   "Công khí thực hiện: A = p·ΔV = 2,0·10⁵ · 5,0·10⁻³ = 1000 J.\n"
   "Nguyên lí I: ΔU = Q − A = 1500 − 1000 = 500 J.",
   "Nguyên lí I nhiệt động lực học", K),

mc("Mỗi lần bơm đưa được 80 cm³ khí ở áp suất 1,0·10⁵ Pa vào một ruột xe có thể tích 2000 cm³ "
   "đang chứa khí ở chính áp suất đó. Sau 50 lần bơm, áp suất khí trong ruột xe bằng "
   "(nhiệt độ và thể tích ruột xe không đổi)",
   ["3,0·10⁵ Pa.", "2,0·10⁵ Pa.", "4,0·10⁵ Pa.", "2,5·10⁵ Pa."],
   "A",
   "Tổng lượng khí quy về áp suất ở thể tích 2000 cm³ (định luật Boyle):\n"
   "p·2000 = 1,0·10⁵ · 2000 + 50 · 1,0·10⁵ · 80 = (2000 + 4000)·10⁵\n"
   "p = 6000·10⁵/2000 = 3,0·10⁵ Pa.",
   "Định luật Boyle – bài toán bơm khí", K),

mc("Động năng tịnh tiến trung bình của một phân tử khí lí tưởng ở 27 °C bằng "
   "(k = 1,38·10⁻²³ J/K)",
   ["4,14·10⁻²¹ J.", "2,07·10⁻²¹ J.", "1,24·10⁻²⁰ J.", "6,21·10⁻²¹ J."],
   "D",
   "T = 300 K.\n"
   "Wđ = (3/2)·k·T = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J.",
   "Động năng phân tử và nhiệt độ", K),

mc("Nung nóng đẳng tích một lượng khí lí tưởng từ 27 °C lên 87 °C. Áp suất khí tăng thêm",
   ["10 %.", "20 %.", "25 %.", "60 %."],
   "B",
   "Đẳng tích: p₂/p₁ = T₂/T₁ = 360/300 = 1,2.\n"
   "Áp suất tăng thêm 0,2 lần giá trị ban đầu, tức 20 %.",
   "Định luật Charles – tỉ lệ phần trăm", K),

mc("Hai dây dẫn thẳng dài song song cách nhau 20 cm mang dòng điện cùng chiều I₁ = 5,0 A và "
   "I₂ = 10 A. Biết cảm ứng từ do dòng thẳng dài gây ra tại điểm cách dây r là B = 2·10⁻⁷·I/r. "
   "Điểm có cảm ứng từ tổng hợp bằng không nằm cách dây thứ nhất",
   ["6,7 cm.", "13,3 cm.", "10,0 cm.", "20,0 cm."],
   "A",
   "Điểm triệt tiêu nằm giữa hai dây (hai dòng cùng chiều), cách dây 1 đoạn x:\n"
   "I₁/x = I₂/(0,20 − x) ⟹ 5,0·(0,20 − x) = 10·x ⟹ 1,0 = 15x\n"
   "x = 1/15 ≈ 0,067 m = 6,7 cm.",
   "Cảm ứng từ tổng hợp", RK, fig="t_sd_duongsuc_daythang", cap="Từ trường của dòng điện thẳng"),

mc("Một đoạn dây dẫn dài 20 cm mang dòng điện 4,0 A đặt trong từ trường đều B = 0,50 T sao cho "
   "dây hợp với đường sức một góc 30°. Lực từ tác dụng lên đoạn dây bằng",
   ["0,40 N.", "0,35 N.", "0,20 N.", "0,10 N."],
   "C",
   "F = B·I·ℓ·sinα = 0,50 · 4,0 · 0,20 · sin30° = 0,40 · 0,5 = 0,20 N.",
   "Lực từ", K, fig="t_sd_goc_alpha", cap="Góc giữa dây dẫn và đường sức"),

mc("Một khung dây 200 vòng, diện tích mỗi vòng 100 cm², đặt vuông góc với từ trường đều. "
   "Cảm ứng từ tăng đều từ 0 đến 0,40 T trong 0,20 s. Suất điện động cảm ứng bằng",
   ["0,40 V.", "1,00 V.", "2,00 V.", "4,00 V."],
   "D",
   "e = N·S·ΔB/Δt = 200 · 0,010 · 0,40/0,20 = 200 · 0,010 · 2,0 = 4,00 V.",
   "Định luật Faraday", K),

mc("Đặt điện áp u = 220√2·cos(100πt) (V) vào hai đầu điện trở R = 110 Ω. "
   "Công suất toả nhiệt trên điện trở bằng",
   ["220 W.", "440 W.", "880 W.", "110 W."],
   "B",
   "Điện áp hiệu dụng: U = 220 V.\n"
   "P = U²/R = 220²/110 = 48 400/110 = 440 W.",
   "Công suất dòng điện xoay chiều", K, fig="t_dt_u_i_hieudung",
   cap="Giá trị hiệu dụng của điện áp xoay chiều"),

mc("Một máy phát điện xoay chiều có rôto gồm 4 cặp cực quay đều với tốc độ 750 vòng/phút. "
   "Tần số của suất điện động do máy phát ra bằng",
   ["50 Hz.", "25 Hz.", "60 Hz.", "12,5 Hz."],
   "A",
   "n = 750 vòng/phút = 12,5 vòng/giây.\n"
   "f = p·n = 4 · 12,5 = 50 Hz.",
   "Máy phát điện xoay chiều", K, fig="t_sd_may_phat", cap="Cấu tạo máy phát điện xoay chiều"),

mc("Hạt nhân ⁷Li có khối lượng 7,0160 u. Cho m(p) = 1,0073 u; m(n) = 1,0087 u; "
   "1 u·c² = 931,5 MeV. Năng lượng liên kết riêng của ⁷Li bằng",
   ["7,08 MeV/nuclôn.", "8,79 MeV/nuclôn.", "5,42 MeV/nuclôn.", "37,9 MeV/nuclôn."],
   "C",
   "⁷Li có 3 prôtôn và 4 nơtron.\n"
   "Δm = 3 · 1,0073 + 4 · 1,0087 − 7,0160 = 3,0219 + 4,0348 − 7,0160 = 0,0407 u.\n"
   "W(lk) = 0,0407 · 931,5 ≈ 37,91 MeV.\n"
   "W(lk riêng) = 37,91/7 ≈ 5,42 MeV/nuclôn.",
   "Năng lượng liên kết riêng", K, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Hạt nhân ²¹⁰Po đứng yên phóng xạ α tạo thành ²⁰⁶Pb, phản ứng toả 5,40 MeV. "
   "Bỏ qua bức xạ γ, động năng của hạt α bằng",
   ["5,40 MeV.", "5,30 MeV.", "0,10 MeV.", "5,50 MeV."],
   "B",
   "Bảo toàn động lượng: động năng chia cho hai hạt tỉ lệ nghịch với số khối.\n"
   "W(α) = ΔE · A(Pb)/(A(α) + A(Pb)) = 5,40 · 206/210 ≈ 5,30 MeV.",
   "Động năng trong phân rã α", RK, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã của Po-210"),

mc("Một mẫu gỗ cổ có độ phóng xạ của ¹⁴C bằng 1/4 độ phóng xạ của mẫu gỗ cùng loại mới chặt. "
   "Biết chu kì bán rã của ¹⁴C là 5730 năm. Tuổi của mẫu gỗ bằng",
   ["5730 năm.", "2865 năm.", "17190 năm.", "11460 năm."],
   "D",
   "H/H₀ = 1/4 = 2⁻² ⟹ số chu kì n = 2.\n"
   "t = 2 · 5730 = 11 460 năm.",
   "Định tuổi bằng cacbon phóng xạ", K, fig="h_dt_c14", cap="Định tuổi bằng C-14"),

mc("Trong phản ứng ²⁷Al + α → ³⁰P + X, hạt X là",
   ["nơtron.", "prôtôn.", "êlectron.", "hạt α."],
   "A",
   "Bảo toàn số khối: 27 + 4 = 30 + A ⟹ A = 1.\n"
   "Bảo toàn điện tích: 13 + 2 = 15 + Z ⟹ Z = 0.\n"
   "Hạt có A = 1, Z = 0 là nơtron.",
   "Định luật bảo toàn trong phản ứng hạt nhân", K),

mc("Biện pháp nào sau đây KHÔNG làm giảm liều chiếu xạ mà người làm việc với nguồn phóng xạ "
   "nhận được?",
   ["Tăng khoảng cách tới nguồn.", "Dùng tấm chì che chắn.",
    "Kéo dài thời gian thao tác gần nguồn.", "Sử dụng nguồn có độ phóng xạ nhỏ hơn."],
   "C",
   "Liều chiếu xạ tỉ lệ thuận với thời gian tiếp xúc, tỉ lệ nghịch với bình phương khoảng cách "
   "và giảm khi có vật liệu che chắn.\n"
   "Kéo dài thời gian thao tác gần nguồn làm TĂNG liều nhận được.",
   "An toàn phóng xạ", K, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn phóng xạ"),

mc("Năng lượng toả ra khi 1,0 g ²³⁵U phân hạch hoàn toàn bằng (mỗi phân hạch toả 200 MeV; "
   "Nₐ = 6,02·10²³ mol⁻¹)",
   ["2,56·10²¹ J.", "8,2·10¹⁰ J.", "3,2·10⁻¹¹ J.", "5,1·10¹³ J."],
   "B",
   "Số hạt nhân: N = (1,0/235) · 6,02·10²³ ≈ 2,562·10²¹ hạt.\n"
   "Mỗi phân hạch toả 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "E = 2,562·10²¹ · 3,2·10⁻¹¹ ≈ 8,2·10¹⁰ J.",
   "Năng lượng phân hạch", K, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Ưu điểm nổi bật của phản ứng nhiệt hạch so với phản ứng phân hạch là",
   ["mỗi phản ứng toả năng lượng lớn hơn.",
    "dễ khống chế trong lò phản ứng hơn.",
    "không cần điều kiện nhiệt độ cao.",
    "nhiên liệu dồi dào và hầu như không tạo chất thải phóng xạ sống lâu."],
   "D",
   "Mỗi phản ứng nhiệt hạch toả năng lượng NHỎ hơn một phân hạch, nhưng tính trên một đơn vị "
   "khối lượng thì lớn hơn. Nhiệt hạch cần nhiệt độ hàng chục triệu độ và rất khó khống chế.\n"
   "Ưu điểm thật sự: nhiên liệu (đơteri trong nước biển) gần như vô tận và sản phẩm không phải "
   "chất thải phóng xạ sống lâu.",
   "So sánh phân hạch và nhiệt hạch", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Nội năng của một lượng khí lí tưởng xác định",
   ["chỉ phụ thuộc vào nhiệt độ của khí.",
    "chỉ phụ thuộc vào thể tích của khí.",
    "chỉ phụ thuộc vào áp suất của khí.",
    "không thay đổi trong mọi quá trình."],
   "A",
   "Với khí lí tưởng, các phân tử không tương tác ở xa nên thế năng tương tác bằng không; "
   "nội năng chỉ gồm động năng chuyển động nhiệt, do đó chỉ phụ thuộc nhiệt độ.",
   "Nội năng của khí lí tưởng", K),
],
P2=[
ds("Thả 0,80 kg nước đá ở −10 °C vào 3,0 kg nước ở 40 °C trong bình cách nhiệt. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng cần để đưa nước đá lên 0 °C là 16 800 J.", True,
     "Đúng. Q = 0,80 · 2100 · 10 = 16 800 J."),
    ("Nhiệt lượng cần để nước đá tan hoàn toàn ở 0 °C là 272 kJ.", True,
     "Đúng. Q = 0,80 · 3,4·10⁵ = 272 000 J = 272 kJ."),
    ("Nước đá tan hết.", True,
     "Đúng. Nước toả ra tối đa 3,0 · 4200 · 40 = 504 000 J, lớn hơn 16 800 + 272 000 = 288 800 J."),
    ("Nhiệt độ cân bằng của hệ là 0 °C.", False,
     "Sai. Sau khi đá tan hết vẫn còn dư 504 000 − 288 800 = 215 200 J, làm 3,8 kg nước nóng "
     "thêm 215 200/(3,8 · 4200) ≈ 13,5 °C. Nhiệt độ cân bằng xấp xỉ 13,5 °C.")],
   "Cân bằng nhiệt có chuyển thể", RK, fig="n_sd_can_bang_nhiet", cap="Trao đổi nhiệt trong bình cách nhiệt"),

ds("Một xilanh có pit-tông nhẹ chuyển động không ma sát chứa 2,0 L khí lí tưởng ở 27 °C và "
   "1,0·10⁵ Pa. Nung nóng khí tới 87 °C, pit-tông tự do nên áp suất không đổi. "
   "Cho R = 8,31 J/(mol·K).",
   [("Thể tích khí sau khi nung là 2,4 L.", True,
     "Đúng. V₂ = V₁·T₂/T₁ = 2,0 · 360/300 = 2,4 L."),
    ("Công khí thực hiện lên pit-tông là 40 J.", True,
     "Đúng. A = p·ΔV = 1,0·10⁵ · 0,4·10⁻³ = 40 J."),
    ("Lượng khí trong xilanh xấp xỉ 0,080 mol.", True,
     "Đúng. n = pV/(RT) = 1,0·10⁵ · 2,0·10⁻³/(8,31 · 300) = 200/2493 ≈ 0,080 mol."),
    ("Nhiệt lượng khí nhận được đúng bằng 40 J.", False,
     "Sai. Nguyên lí I cho Q = ΔU + A. Nhiệt độ tăng nên ΔU > 0, do đó Q phải LỚN HƠN "
     "công 40 J.")],
   "Quá trình đẳng áp và nguyên lí I", K, fig="n_sd_cong_cua_khi", cap="Khí thực hiện công lên pit-tông"),

ds("Một khung dây phẳng 100 vòng, diện tích mỗi vòng 50 cm², quay đều quanh trục vuông góc với "
   "từ trường đều B = 0,20 T với tốc độ 300 vòng/phút.",
   [("Tần số của suất điện động là 5,0 Hz.", True,
     "Đúng. f = 300/60 = 5,0 Hz."),
    ("Từ thông cực đại qua khung là 0,10 Wb.", True,
     "Đúng. Φ₀ = N·B·S = 100 · 0,20 · 0,0050 = 0,10 Wb."),
    ("Suất điện động cực đại xấp xỉ 3,14 V.", True,
     "Đúng. ω = 2πf = 10π ≈ 31,4 rad/s ⟹ E₀ = ω·Φ₀ = 31,4 · 0,10 ≈ 3,14 V."),
    ("Suất điện động hiệu dụng cũng xấp xỉ 3,14 V.", False,
     "Sai. E = E₀/√2 = 3,14/1,414 ≈ 2,22 V, nhỏ hơn giá trị cực đại.")],
   "Khung dây quay trong từ trường", RK, fig="t_sd_may_phat", cap="Khung dây quay trong từ trường"),

ds("Một mẫu ²¹⁰Po nguyên chất khối lượng ban đầu 2,10 g, phóng xạ α với chu kì bán rã 138 ngày. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹.",
   [("Số hạt nhân Po ban đầu là 6,02·10²¹ hạt.", True,
     "Đúng. N₀ = (2,10/210) · 6,02·10²³ = 0,010 · 6,02·10²³ = 6,02·10²¹ hạt."),
    ("Sau 276 ngày, số hạt nhân Po còn lại bằng 1/4 số ban đầu.", True,
     "Đúng. 276 ngày = 2 chu kì ⟹ còn 2⁻² = 1/4."),
    ("Sau 276 ngày, số hạt α đã tạo thành xấp xỉ 4,52·10²¹ hạt.", True,
     "Đúng. Số hạt đã phân rã = (3/4)·6,02·10²¹ ≈ 4,515·10²¹ hạt, mỗi phân rã sinh một hạt α."),
    ("Sau 414 ngày, khối lượng Po còn lại là 0,525 g.", False,
     "Sai. 414 ngày = 3 chu kì ⟹ còn 2⁻³ = 1/8 khối lượng, tức 2,10/8 = 0,2625 g chứ không "
     "phải 0,525 g (giá trị ứng với 2 chu kì).")],
   "Định luật phóng xạ", RK, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),
],
P3=[
sa("Đun 2,0 kg nước từ 20 °C tới sôi ở 100 °C rồi tiếp tục làm hoá hơi hoàn toàn 0,50 kg nước. "
   "Cho c = 4200 J/(kg·K); L = 2,3·10⁶ J/kg. Tổng nhiệt lượng cần cung cấp bằng bao nhiêu MJ "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "1,82",
   "Giai đoạn đun nóng: Q₁ = 2,0 · 4200 · 80 = 672 000 J.\n"
   "Giai đoạn hoá hơi: Q₂ = 0,50 · 2,3·10⁶ = 1 150 000 J.\n"
   "Q = 672 000 + 1 150 000 = 1 822 000 J ≈ 1,82 MJ.",
   "Nhiệt hoá hơi riêng", K, fig="n_sd_bayhoi_soi", cap="Bay hơi và sôi"),

sa("Một bình kín thể tích 20 L chứa khí ôxi (M = 32 g/mol) ở 27 °C và áp suất 1,5·10⁵ Pa. "
   "Khối lượng khí trong bình bằng bao nhiêu gam (làm tròn đến chữ số thập phân thứ nhất)? "
   "Lấy R = 8,31 J/(mol·K).",
   "38,5",
   "n = pV/(RT) = 1,5·10⁵ · 20·10⁻³/(8,31 · 300) = 3000/2493 ≈ 1,203 mol.\n"
   "m = n·M = 1,203 · 32 ≈ 38,5 g.",
   "Phương trình Clapeyron", K),

sa("Một khung dây 50 vòng, diện tích mỗi vòng 200 cm², đặt trong từ trường đều B = 0,10 T sao cho "
   "pháp tuyến của khung hợp với đường sức góc 60°. Từ thông qua khung bằng bao nhiêu mWb?",
   "50",
   "Φ = N·B·S·cosα = 50 · 0,10 · 0,020 · cos60° = 0,10 · 0,5 = 0,050 Wb = 50 mWb.",
   "Từ thông", K, fig="t_sd_tuthong", cap="Từ thông qua khung dây"),

sa("Một bếp từ có công suất 2000 W và hiệu suất 80 % được dùng để đun 1,5 kg nước từ 25 °C lên "
   "100 °C. Thời gian đun bằng bao nhiêu giây (làm tròn đến hàng đơn vị)? "
   "Cho c = 4200 J/(kg·K).",
   "295",
   "Nhiệt lượng nước cần: Q = 1,5 · 4200 · 75 = 472 500 J.\n"
   "Công suất hữu ích: P(ích) = 0,80 · 2000 = 1600 W.\n"
   "t = 472 500/1600 ≈ 295 s.",
   "Ứng dụng dòng Fu-cô – bếp từ", K, fig="t_sd_bep_tu", cap="Nguyên lí bếp từ"),

sa("Tính độ phóng xạ ban đầu của 1,0 mg ²²²Rn có chu kì bán rã 3,8 ngày. "
   "Kết quả viết dưới dạng x·10¹² Bq, hãy ghi giá trị x (làm tròn đến chữ số thập phân thứ nhất). "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; ln2 ≈ 0,693.",
   "5,7",
   "Số hạt nhân: N₀ = (1,0·10⁻³/222) · 6,02·10²³ ≈ 2,712·10¹⁸ hạt.\n"
   "Hằng số phóng xạ: λ = 0,693/(3,8 · 86 400) = 0,693/328 320 ≈ 2,111·10⁻⁶ s⁻¹.\n"
   "H₀ = λ·N₀ = 2,111·10⁻⁶ · 2,712·10¹⁸ ≈ 5,7·10¹² Bq.",
   "Độ phóng xạ", RK),

sa("Cho phản ứng nhiệt hạch ²H + ²H → ³He + n với m(²H) = 2,0136 u; m(³He) = 3,0160 u; "
   "m(n) = 1,0087 u; 1 u·c² = 931,5 MeV. Năng lượng toả ra của phản ứng bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "2,33",
   "Độ hụt khối của phản ứng:\n"
   "Δm = 2 · 2,0136 − (3,0160 + 1,0087) = 4,0272 − 4,0247 = 0,0025 u.\n"
   "ΔE = 0,0025 · 931,5 ≈ 2,33 MeV.",
   "Năng lượng phản ứng nhiệt hạch", RK, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),
])


# =====================================================================  ĐỀ 30
DE30 = dict(
ma="TH-Đề 30", ten="ĐỀ THI THỬ SỐ 30", muc="Khó – phân loại",
trongtam="Đề tổng duyệt: bao phủ cả bốn chương ở mức vận dụng cao, nhiều bẫy điều kiện",
P1=[
mc("Một động cơ nhiệt có hiệu suất 30 %, mỗi giây tiêu thụ 2,0 g nhiên liệu có năng suất toả nhiệt "
   "4,4·10⁷ J/kg. Công suất có ích của động cơ bằng",
   ["26,4 kW.", "88,0 kW.", "61,6 kW.", "13,2 kW."],
   "A",
   "Nhiệt lượng nhiên liệu cung cấp mỗi giây: Q = 2,0·10⁻³ · 4,4·10⁷ = 88 000 W.\n"
   "Công suất có ích: P = H·Q = 0,30 · 88 000 = 26 400 W = 26,4 kW.",
   "Hiệu suất động cơ nhiệt", K, fig="n_sd_hieu_suat", cap="Dòng năng lượng trong động cơ nhiệt"),

mc("Một nhiệt lượng kế bằng đồng khối lượng 0,20 kg chứa 0,30 kg nước ở 20 °C. Thả vào đó 0,10 kg "
   "kim loại ở 100 °C, nhiệt độ cân bằng là 25 °C. Cho c(đồng) = 380, c(nước) = 4200 J/(kg·K). "
   "Nhiệt dung riêng của kim loại bằng",
   ["380 J/(kg·K).", "460 J/(kg·K).", "891 J/(kg·K).", "840 J/(kg·K)."],
   "C",
   "Nhiệt lượng nước và bình thu vào:\n"
   "Q(thu) = (0,30 · 4200 + 0,20 · 380) · 5 = (1260 + 76) · 5 = 1336 · 5 = 6680 J.\n"
   "Kim loại toả ra: Q(toả) = 0,10 · c · 75 = 7,5·c.\n"
   "7,5·c = 6680 ⟹ c = 6680/7,5 ≈ 891 J/(kg·K).",
   "Nhiệt lượng kế – xác định nhiệt dung riêng", RK, fig="n_sd_tn_do_c",
   cap="Thí nghiệm đo nhiệt dung riêng"),

mc("Một ống thuỷ tinh dài 60 cm, một đầu kín, đặt thẳng đứng miệng hướng lên, chứa cột không khí "
   "dài 30 cm bị giam bởi cột thuỷ ngân dài 20 cm. Áp suất khí quyển 75 cmHg. Lật ngược ống cho "
   "miệng hướng xuống, chiều dài cột không khí bằng",
   ["51,8 cm.", "46,4 cm.", "40,0 cm.", "30,0 cm."],
   "B",
   "Trạng thái đầu: p₁ = 75 + 20 = 95 cmHg; L₁ = 30 cm ⟹ p₁L₁ = 2850.\n"
   "Nếu lật ngược mà thuỷ ngân không tràn: p₂ = 75 − 20 = 55 ⟹ L₂ = 2850/55 ≈ 51,8 cm.\n"
   "Khi đó L₂ + 20 = 71,8 cm > 60 cm: vô lí, vậy thuỷ ngân đã TRÀN ra một phần.\n"
   "Gọi h là chiều cao cột thuỷ ngân còn lại, cột khí dài 60 − h và p₂ = 75 − h:\n"
   "(75 − h)(60 − h) = 2850 ⟹ h² − 135h + 1650 = 0 ⟹ h ≈ 13,6 cm.\n"
   "Chiều dài cột khí: L₂ = 60 − 13,6 ≈ 46,4 cm.",
   "Định luật Boyle – bẫy thuỷ ngân tràn", RK),

mc("Một lượng khí thực hiện chu trình kín gồm bốn quá trình: đẳng tích từ 1,0·10⁵ Pa lên "
   "3,0·10⁵ Pa tại 2,0 L; đẳng áp giãn tới 5,0 L; đẳng tích hạ về 1,0·10⁵ Pa; đẳng áp nén về "
   "2,0 L. Công mà khí sinh ra trong một chu trình bằng",
   ["300 J.", "900 J.", "1200 J.", "600 J."],
   "D",
   "Chu trình là hình chữ nhật trên giản đồ p–V.\n"
   "Công sinh ra khi giãn đẳng áp: A₁ = 3,0·10⁵ · 3,0·10⁻³ = 900 J.\n"
   "Công phải tiêu tốn khi nén đẳng áp: A₂ = 1,0·10⁵ · 3,0·10⁻³ = 300 J.\n"
   "Công có ích của chu trình: A = 900 − 300 = 600 J (bằng diện tích hình chữ nhật).",
   "Công trong chu trình kín", RK, fig="k_dt_ba_he_truc", cap="Các giản đồ trạng thái của khí"),

mc("Mật độ phân tử của một chất khí ở áp suất 1,0·10⁵ Pa và nhiệt độ 27 °C bằng "
   "(k = 1,38·10⁻²³ J/K)",
   ["2,4·10²⁵ phân tử/m³.", "4,8·10²⁵ phân tử/m³.",
    "1,2·10²⁵ phân tử/m³.", "7,2·10²⁴ phân tử/m³."],
   "A",
   "Từ p = n·k·T (n là số phân tử trong một đơn vị thể tích):\n"
   "n = p/(k·T) = 1,0·10⁵/(1,38·10⁻²³ · 300) = 1,0·10⁵/4,14·10⁻²¹ ≈ 2,4·10²⁵ phân tử/m³.",
   "Thuyết động học phân tử", RK),

mc("Một thanh kim loại trượt đều với tốc độ 4,0 m/s trên hai ray nằm ngang cách nhau 50 cm, "
   "trong từ trường đều thẳng đứng B = 0,20 T. Điện trở toàn mạch 0,40 Ω, ma sát không đáng kể. "
   "Công suất cơ học cần cung cấp để kéo thanh bằng",
   ["0,10 W.", "0,20 W.", "0,40 W.", "1,00 W."],
   "C",
   "Suất điện động: e = B·ℓ·v = 0,20 · 0,50 · 4,0 = 0,40 V.\n"
   "Dòng điện: I = 0,40/0,40 = 1,0 A.\n"
   "Lực từ cản: F = B·I·ℓ = 0,20 · 1,0 · 0,50 = 0,10 N.\n"
   "Công suất cơ học: P = F·v = 0,10 · 4,0 = 0,40 W (đúng bằng công suất điện e·I).",
   "Thanh trượt trên ray – chuyển hoá năng lượng", RK, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trượt trên hai ray"),

mc("Một khung dây kín 100 vòng, diện tích mỗi vòng 100 cm², điện trở 2,0 Ω, đặt vuông góc với "
   "từ trường đều. Khi cảm ứng từ giảm đều từ 0,50 T về 0, điện lượng chuyển qua khung bằng",
   ["0,50 C.", "0,25 C.", "0,025 C.", "2,5 C."],
   "B",
   "Điện lượng: q = ΔΦ/R với ΔΦ = N·S·ΔB = 100 · 0,010 · 0,50 = 0,50 Wb.\n"
   "q = 0,50/2,0 = 0,25 C. (Kết quả không phụ thuộc thời gian biến thiên.)",
   "Điện lượng cảm ứng", RK),

mc("Khi truyền tải điện năng đi xa, hao phí trên đường dây chiếm 20 % công suất truyền đi. "
   "Nếu tăng điện áp nơi truyền lên gấp đôi mà giữ nguyên công suất truyền thì hiệu suất "
   "truyền tải đạt",
   ["80 %.", "90 %.", "97,5 %.", "95 %."],
   "D",
   "Hao phí ΔP = R·P²/U² tỉ lệ nghịch với U².\n"
   "Tăng U gấp đôi ⟹ hao phí giảm 4 lần: 20 %/4 = 5 %.\n"
   "Hiệu suất: H = 100 % − 5 % = 95 %.",
   "Hiệu suất truyền tải", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng đi xa"),

mc("Một êlectron chuyển động với tốc độ 2,0·10⁶ m/s theo phương vuông góc với từ trường đều "
   "B = 0,010 T. Độ lớn lực từ tác dụng lên êlectron bằng (e = 1,6·10⁻¹⁹ C)",
   ["3,2·10⁻¹⁵ N.", "1,6·10⁻¹⁵ N.", "3,2·10⁻¹³ N.", "6,4·10⁻¹⁵ N."],
   "A",
   "f = |q|·v·B·sin90° = 1,6·10⁻¹⁹ · 2,0·10⁶ · 0,010 = 3,2·10⁻¹⁵ N.",
   "Lực từ tác dụng lên điện tích chuyển động", K),

mc("Một khung dây dẫn kín nằm trọn trong vùng từ trường đều và chuyển động tịnh tiến đều "
   "bên trong vùng đó. Trong khung",
   ["xuất hiện dòng điện cảm ứng không đổi.",
    "xuất hiện dòng điện cảm ứng biến thiên.",
    "không xuất hiện dòng điện cảm ứng.",
    "xuất hiện dòng điện cảm ứng chỉ khi khung đổi hướng."],
   "C",
   "Khung nằm trọn trong vùng từ trường đều nên diện tích, cảm ứng từ và góc giữa pháp tuyến "
   "với đường sức đều không đổi ⟹ từ thông không đổi ⟹ không có suất điện động cảm ứng, "
   "do đó không có dòng cảm ứng.",
   "Điều kiện xuất hiện dòng cảm ứng", K),

mc("Cho năng lượng liên kết của các hạt nhân: ²H là 2,22 MeV; ⁴He là 28,3 MeV; ⁵⁶Fe là 492 MeV; "
   "²³⁵U là 1784 MeV. Hạt nhân bền vững nhất là",
   ["²H.", "⁴He.", "⁵⁶Fe.", "²³⁵U."],
   "C",
   "So sánh năng lượng liên kết RIÊNG:\n"
   "²H: 2,22/2 = 1,11;  ⁴He: 28,3/4 ≈ 7,08;  ⁵⁶Fe: 492/56 ≈ 8,79;  ²³⁵U: 1784/235 ≈ 7,59 "
   "MeV/nuclôn.\n"
   "Giá trị lớn nhất là 8,79 MeV/nuclôn nên ⁵⁶Fe bền vững nhất.",
   "Độ bền vững của hạt nhân", K, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Hạt nhân ²¹⁰Bi (Z = 83) phóng xạ β⁻. Hạt nhân con là",
   ["²¹⁰Pb (Z = 82).", "²¹⁰Po (Z = 84).", "²⁰⁶Tl (Z = 81).", "²⁰⁹Bi (Z = 83)."],
   "B",
   "Phóng xạ β⁻ giữ nguyên số khối và làm điện tích hạt nhân tăng một đơn vị:\n"
   "A = 210 không đổi; Z = 83 + 1 = 84 ⟹ hạt nhân con là ²¹⁰Po.",
   "Quy tắc dịch chuyển phóng xạ", K, fig="h_sd_dich_chuyen",
   cap="Quy tắc dịch chuyển phóng xạ"),

mc("Chuỗi phóng xạ tự nhiên biến ²³⁸U (Z = 92) thành ²⁰⁶Pb (Z = 82) gồm",
   ["6 phân rã α và 8 phân rã β⁻.", "8 phân rã α và 8 phân rã β⁻.",
    "8 phân rã α và 10 phân rã β⁻.", "8 phân rã α và 6 phân rã β⁻."],
   "D",
   "Số phân rã α: (238 − 206)/4 = 8.\n"
   "Nếu chỉ có 8 phân rã α thì Z giảm 16, còn 92 − 16 = 76; để đạt Z = 82 cần tăng thêm 6 "
   "đơn vị ⟹ có 6 phân rã β⁻.",
   "Chuỗi phóng xạ", RK),

mc("Một mẫu đá chứa ²³⁸U và ²⁰⁶Pb với số hạt nhân Pb gấp 3 lần số hạt nhân U còn lại. "
   "Biết chu kì bán rã của ²³⁸U là 4,5·10⁹ năm và mọi hạt Pb đều sinh ra từ U. "
   "Tuổi của mẫu đá bằng",
   ["9,0·10⁹ năm.", "4,5·10⁹ năm.", "13,5·10⁹ năm.", "2,25·10⁹ năm."],
   "A",
   "Số hạt ban đầu N₀ = N(U) + N(Pb) = N + 3N = 4N ⟹ tỉ lệ còn lại N/N₀ = 1/4 = 2⁻².\n"
   "Vậy đã trôi qua 2 chu kì: t = 2 · 4,5·10⁹ = 9,0·10⁹ năm.",
   "Định tuổi bằng tỉ số hạt nhân mẹ – con", RK),

mc("Cho phản ứng ²H + ³H → ⁴He + n với năng lượng liên kết riêng lần lượt là 1,11; 2,83 và "
   "7,07 MeV/nuclôn. Năng lượng toả ra của phản ứng bằng",
   ["2,2 MeV.", "17,6 MeV.", "28,3 MeV.", "8,5 MeV."],
   "B",
   "Năng lượng liên kết: W(²H) = 2 · 1,11 = 2,22; W(³H) = 3 · 2,83 = 8,49; "
   "W(⁴He) = 4 · 7,07 = 28,28 MeV. Nơtron có năng lượng liên kết bằng 0.\n"
   "ΔE = W(sau) − W(trước) = 28,28 − (2,22 + 8,49) = 28,28 − 10,71 ≈ 17,6 MeV.",
   "Năng lượng phản ứng tính theo năng lượng liên kết riêng", RK,
   fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch D–T"),

mc("Một nguồn phóng xạ có độ phóng xạ ban đầu 4,0·10⁸ Bq và chu kì bán rã 8,0 giờ. "
   "Sau 24 giờ, độ phóng xạ của nguồn bằng",
   ["1,0·10⁸ Bq.", "2,0·10⁸ Bq.", "5,0·10⁷ Bq.", "1,3·10⁸ Bq."],
   "C",
   "Số chu kì: n = 24/8,0 = 3.\n"
   "H = H₀ · 2⁻ⁿ = 4,0·10⁸/8 = 5,0·10⁷ Bq.",
   "Độ phóng xạ theo thời gian", K),

mc("Đơn vị đo liều hấp thụ bức xạ là",
   ["becơren (Bq).", "gray (Gy).", "sivơ (Sv).", "curi (Ci)."],
   "B",
   "Becơren và curi đo ĐỘ PHÓNG XẠ của nguồn; sivơ đo liều TƯƠNG ĐƯƠNG (có tính đến mức nguy hại "
   "sinh học của từng loại bức xạ); gray đo LIỀU HẤP THỤ, tức năng lượng bức xạ hấp thụ trên "
   "một đơn vị khối lượng.",
   "Các đại lượng đo bức xạ", K),

mc("Lực hạt nhân là lực",
   ["hút tĩnh điện giữa các prôtôn.",
    "hấp dẫn giữa các nuclôn.",
    "từ giữa các nuclôn chuyển động.",
    "tương tác mạnh giữa các nuclôn, chỉ đáng kể trong khoảng cách cỡ 10⁻¹⁵ m."],
   "D",
   "Lực hạt nhân không phải lực tĩnh điện (các prôtôn đẩy nhau) cũng không phải lực hấp dẫn "
   "(quá yếu). Đó là biểu hiện của tương tác mạnh, có bán kính tác dụng rất ngắn, cỡ kích thước "
   "hạt nhân 10⁻¹⁵ m.",
   "Lực hạt nhân", K, fig="h_sd_cautruc", cap="Cấu trúc hạt nhân"),
],
P2=[
ds("Một nhiệt lượng kế bằng nhôm khối lượng 0,15 kg chứa 0,25 kg nước ở 22 °C. Thả vào đó 0,20 kg "
   "kim loại ở 100 °C, nhiệt độ cân bằng là 28 °C. Cho c(nhôm) = 880, c(nước) = 4200 J/(kg·K).",
   [("Nhiệt dung của nước và bình cộng lại là 1182 J/K.", True,
     "Đúng. 0,25 · 4200 + 0,15 · 880 = 1050 + 132 = 1182 J/K."),
    ("Nhiệt lượng nước và bình thu vào là 7092 J.", True,
     "Đúng. Q = 1182 · (28 − 22) = 1182 · 6 = 7092 J."),
    ("Nhiệt dung riêng của kim loại xấp xỉ 493 J/(kg·K).", True,
     "Đúng. 0,20 · c · (100 − 28) = 7092 ⟹ c = 7092/14,4 ≈ 493 J/(kg·K)."),
    ("Nếu bỏ qua nhiệt dung của bình thì giá trị tính được của c sẽ lớn hơn.", False,
     "Sai. Bỏ qua bình thì nhiệt lượng thu vào nhỏ hơn (1050 · 6 = 6300 J), nên "
     "c = 6300/14,4 ≈ 438 J/(kg·K), tức NHỎ hơn giá trị 493 J/(kg·K).")],
   "Nhiệt lượng kế – xác định nhiệt dung riêng", RK, fig="n_sd_tn_do_c",
   cap="Thí nghiệm đo nhiệt dung riêng"),

ds("Một lượng khí lí tưởng thực hiện chu trình kín dạng hình chữ nhật trên giản đồ p–V với "
   "p thay đổi giữa 1,0·10⁵ Pa và 3,0·10⁵ Pa, V thay đổi giữa 2,0 L và 5,0 L.",
   [("Công khí sinh ra khi giãn đẳng áp ở 3,0·10⁵ Pa là 900 J.", True,
     "Đúng. A = p·ΔV = 3,0·10⁵ · 3,0·10⁻³ = 900 J."),
    ("Công mà khí nhận khi bị nén đẳng áp ở 1,0·10⁵ Pa là 300 J.", True,
     "Đúng. A = 1,0·10⁵ · 3,0·10⁻³ = 300 J."),
    ("Công có ích của cả chu trình là 600 J.", True,
     "Đúng. A = 900 − 300 = 600 J, đúng bằng diện tích hình chữ nhật trên giản đồ p–V."),
    ("Sau một chu trình, nội năng của khí tăng thêm 600 J.", False,
     "Sai. Chu trình kín đưa khí về đúng trạng thái ban đầu nên ΔU = 0; toàn bộ 600 J công có "
     "ích là do khí nhận thêm một nhiệt lượng đúng bằng 600 J.")],
   "Chu trình kín và nguyên lí I", RK, fig="k_dt_ba_he_truc",
   cap="Các giản đồ trạng thái của khí"),

ds("Truyền công suất 500 kW từ nhà máy tới khu dân cư bằng đường dây có điện trở tổng cộng 4,0 Ω. "
   "Điện áp nơi truyền đi là 10 kV, hệ số công suất bằng 1.",
   [("Cường độ dòng điện trên dây là 50 A.", True,
     "Đúng. I = P/U = 5,0·10⁵/1,0·10⁴ = 50 A."),
    ("Công suất hao phí trên đường dây là 10 kW.", True,
     "Đúng. ΔP = R·I² = 4,0 · 2500 = 10 000 W = 10 kW."),
    ("Hiệu suất truyền tải là 98 %.", True,
     "Đúng. H = (500 − 10)/500 = 490/500 = 0,98 = 98 %."),
    ("Nếu tăng điện áp truyền đi lên 20 kV thì hao phí giảm còn 5,0 kW.", False,
     "Sai. Hao phí tỉ lệ nghịch với bình phương điện áp: tăng U gấp đôi thì hao phí giảm 4 lần, "
     "còn 10/4 = 2,5 kW.")],
   "Hiệu suất truyền tải", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng đi xa"),

ds("Cho phản ứng nhiệt hạch ²H + ³H → ⁴He + n. Năng lượng liên kết riêng của ²H, ³H và ⁴He lần "
   "lượt là 1,11; 2,83 và 7,07 MeV/nuclôn.",
   [("Năng lượng liên kết của ⁴He là 28,28 MeV.", True,
     "Đúng. W = 4 · 7,07 = 28,28 MeV."),
    ("Năng lượng liên kết của ³H là 8,49 MeV.", True,
     "Đúng. W = 3 · 2,83 = 8,49 MeV."),
    ("Phản ứng toả năng lượng xấp xỉ 17,6 MeV.", True,
     "Đúng. ΔE = 28,28 − (2,22 + 8,49) = 17,57 ≈ 17,6 MeV."),
    ("Đây là phản ứng phân hạch vì có nơtron sinh ra.", False,
     "Sai. Hai hạt nhân RẤT NHẸ kết hợp thành hạt nhân nặng hơn nên đây là phản ứng NHIỆT HẠCH; "
     "sự có mặt của nơtron trong sản phẩm không phải dấu hiệu của phân hạch.")],
   "Năng lượng phản ứng hạt nhân", RK, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch D–T"),
],
P3=[
sa("Cần cung cấp bao nhiêu MJ nhiệt lượng để nung nóng chảy hoàn toàn 2,0 kg nhôm ban đầu ở 25 °C? "
   "Cho c(nhôm) = 880 J/(kg·K); nhiệt độ nóng chảy 660 °C; λ = 3,9·10⁵ J/kg. "
   "(Làm tròn đến chữ số thập phân thứ hai.)",
   "1,90",
   "Giai đoạn nung nóng tới nhiệt độ nóng chảy:\n"
   "Q₁ = 2,0 · 880 · (660 − 25) = 1760 · 635 = 1 117 600 J.\n"
   "Giai đoạn nóng chảy: Q₂ = 2,0 · 3,9·10⁵ = 780 000 J.\n"
   "Q = 1 117 600 + 780 000 = 1 897 600 J ≈ 1,90 MJ.",
   "Nhiệt nóng chảy riêng", K),

sa("Một bình kín chứa khí ở 27 °C và áp suất 2,0·10⁵ Pa. Van an toàn của bình mở khi áp suất bên "
   "trong đạt 3,0·10⁵ Pa. Van sẽ mở khi nhiệt độ khí đạt bao nhiêu độ Celsius?",
   "177",
   "Thể tích không đổi nên p/T = hằng số:\n"
   "T₂ = T₁ · p₂/p₁ = 300 · 3,0/2,0 = 450 K.\n"
   "t₂ = 450 − 273 = 177 °C.",
   "Định luật Charles – bài toán an toàn", K),

sa("Một máy biến áp lí tưởng dùng để hạ điện áp từ 220 V xuống 12 V có cuộn sơ cấp 1100 vòng. "
   "Cuộn thứ cấp có bao nhiêu vòng?",
   "60",
   "N₂/N₁ = U₂/U₁ ⟹ N₂ = 1100 · 12/220 = 1100/18,33 = 60 vòng.",
   "Máy biến áp", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

sa("Một đoạn dây dẫn dài 25 cm mang dòng điện 6,0 A đặt trong từ trường đều B = 0,40 T, dây hợp "
   "với đường sức góc 30°. Lực từ tác dụng lên đoạn dây bằng bao nhiêu niutơn "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,30",
   "F = B·I·ℓ·sinα = 0,40 · 6,0 · 0,25 · sin30° = 0,60 · 0,5 = 0,30 N.",
   "Lực từ", K, fig="t_sd_luctu", cap="Lực từ tác dụng lên dây dẫn mang dòng điện"),

sa("Một mẫu ²⁴Na nguyên chất có khối lượng ban đầu 200 g và chu kì bán rã 15 giờ. "
   "Sau 60 giờ, khối lượng ²⁴Na còn lại bằng bao nhiêu gam "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "12,5",
   "Số chu kì: n = 60/15 = 4.\n"
   "m = m₀ · 2⁻ⁿ = 200/16 = 12,5 g.",
   "Định luật phóng xạ", K),

sa("Năng lượng tối thiểu cần cung cấp để tách hạt nhân ⁴He thành các nuclôn riêng rẽ bằng bao "
   "nhiêu MeV? Cho m(⁴He) = 4,0015 u; m(p) = 1,0073 u; m(n) = 1,0087 u; "
   "1 u·c² = 931,5 MeV. (Làm tròn đến chữ số thập phân thứ nhất.)",
   "28,4",
   "Năng lượng cần cung cấp đúng bằng năng lượng liên kết của hạt nhân.\n"
   "Δm = 2 · 1,0073 + 2 · 1,0087 − 4,0015 = 2,0146 + 2,0174 − 4,0015 = 0,0305 u.\n"
   "W(lk) = 0,0305 · 931,5 ≈ 28,4 MeV.",
   "Năng lượng liên kết", K, fig="h_sd_dohutkhoi", cap="Độ hụt khối và năng lượng liên kết"),
])

NHOM = dict(
    ten_nhom="BỘ ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – PHẦN VI (ĐỀ 26 → 30)",
    mo_ta="Năm đề cuối của bộ 30 đề, ở mức khó – phân loại học sinh giỏi. "
          "Mỗi đề gồm 18 câu trắc nghiệm nhiều lựa chọn, 4 câu đúng/sai (16 ý) và "
          "6 câu trả lời ngắn, làm trong 50 phút theo đúng cấu trúc đề thi tốt nghiệp THPT 2026.",
    pham_vi="Tổng hợp Chương I (Vật lí nhiệt), Chương II (Khí lí tưởng), "
            "Chương III (Từ trường) và Chương IV (Vật lí hạt nhân).",
    tests=[DE26, DE27, DE28, DE29, DE30],
)
