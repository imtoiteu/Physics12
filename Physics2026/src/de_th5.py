# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.  Đề 21 – 25 (Khó)."""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 21
DE21 = dict(
ma="TH-Đề 21", ten="ĐỀ THI THỬ SỐ 21", muc="Khó",
trongtam="Bài toán ghép chương, đọc bảng số liệu và biện luận kết quả",
P1=[
mc("Một bếp từ công suất 1800 W, hiệu suất 90 %, đun 2,0 kg nước từ 20 °C. Sau 5,0 phút, "
   "nhiệt độ nước đạt",
   ["48 °C.", "78 °C.", "92 °C.", "62 °C."],
   "B",
   "Nhiệt lượng có ích: Q = 1800 · 0,90 · 300 = 486 000 J.\n"
   "Độ tăng nhiệt độ: ΔT = 486 000/(2,0 · 4200) = 486 000/8400 ≈ 57,9 °C.\n"
   "Nhiệt độ đạt được: 20 + 57,9 ≈ 78 °C.",
   "Hiệu suất và công suất", K, fig="t_sd_bep_tu", cap="Nguyên lí bếp từ"),

mc("Bảng ghi nhiệt dung riêng của bốn kim loại. Cùng khối lượng và cùng nhiệt lượng, kim loại nào "
   "có độ tăng nhiệt độ lớn gấp khoảng 6,8 lần nhôm?",
   ["Sắt.", "Chì.", "Đồng.", "Kẽm."],
   "B",
   "ΔT tỉ lệ nghịch với c. Tỉ số so với nhôm: 880/c.\n"
   "Với chì: 880/130 ≈ 6,8 — đúng yêu cầu. Với đồng: 880/380 ≈ 2,3; với sắt: 880/460 ≈ 1,9.",
   "Nhiệt dung riêng", K,
   tbl=("Nhiệt dung riêng của bốn kim loại", ["Kim loại", "c (J/kg·K)"],
        [["Nhôm", "880"], ["Sắt", "460"], ["Đồng", "380"], ["Chì", "130"]])),

mc("Một khối khí lí tưởng bị nén đẳng nhiệt, công mà môi trường thực hiện lên khí là 500 J. "
   "Nhiệt lượng khí trao đổi với môi trường là",
   ["thu 500 J.", "toả 500 J.", "thu 250 J.", "không trao đổi."],
   "B",
   "Đẳng nhiệt với khí lí tưởng: ΔU = 0 ⇒ Q = −A. Khí NHẬN công nên A = +500 J, "
   "do đó Q = −500 J: khí TOẢ ra 500 J nhiệt.",
   "Quá trình đẳng nhiệt", K),

mc("Một xi lanh thẳng đứng tiết diện 40 cm², pit-tông khối lượng 8,0 kg. Áp suất khí quyển "
   "1,0·10⁵ Pa, g = 10 m/s². Áp suất khí bên dưới pit-tông bằng",
   ["1,1·10⁵ Pa.", "1,2·10⁵ Pa.", "1,05·10⁵ Pa.", "1,4·10⁵ Pa."],
   "B",
   "Áp suất do pit-tông: mg/S = 8,0 · 10/(40·10⁻⁴) = 80/0,0040 = 2,0·10⁴ Pa.\n"
   "p = p₀ + mg/S = 1,0·10⁵ + 0,2·10⁵ = 1,2·10⁵ Pa.",
   "Bài toán pit-tông", K, fig="k_sd_xilanh_quanang", cap="Xi lanh có pit-tông"),

mc("Nếu lật ngược xi lanh ở câu trên cho miệng xuống dưới (nhiệt độ không đổi) thì thể tích khí "
   "so với ban đầu tăng gấp",
   ["1,25 lần.", "1,5 lần.", "1,2 lần.", "2,0 lần."],
   "B",
   "Miệng xuống dưới: p₂ = 1,0·10⁵ − 0,2·10⁵ = 0,8·10⁵ Pa.\n"
   "Đẳng nhiệt: V₂/V₁ = p₁/p₂ = 1,2/0,8 = 1,5 lần.",
   "Bài toán pit-tông", RK),

mc("Ở cùng nhiệt độ và áp suất, hai bình có thể tích bằng nhau chứa hai khí khác loại. "
   "So sánh SỐ PHÂN TỬ trong hai bình:",
   ["bình chứa khí nặng có nhiều phân tử hơn.", "hai bình có số phân tử bằng nhau.",
    "bình chứa khí nhẹ có nhiều phân tử hơn.", "không so sánh được."],
   "B",
   "Từ pV = nRT, cùng p, V, T thì số mol n bằng nhau, do đó số phân tử cũng bằng nhau — "
   "đây là nội dung định luật Avogadro.",
   "Phương trình Clapeyron", K),

mc("Một khung dây hình vuông cạnh 20 cm, điện trở 0,25 Ω, chuyển động đều 5,0 m/s đi vào vùng từ "
   "trường đều B = 0,50 T. Lực cần thiết để kéo khung đi đều trong lúc vào bằng",
   ["0,10 N.", "0,20 N.", "0,40 N.", "0,05 N."],
   "B",
   "e = B·a·v = 0,50 · 0,20 · 5,0 = 0,50 V;  i = 0,50/0,25 = 2,0 A.\n"
   "Lực từ cản: F = B·i·a = 0,50 · 2,0 · 0,20 = 0,20 N.\n"
   "Kéo đều nên lực kéo cân bằng lực cản: F(kéo) = 0,20 N.",
   "Khung dây vào vùng từ trường", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

mc("Với bài toán trên, công suất cơ học cần cung cấp bằng",
   ["0,50 W.", "1,00 W.", "2,00 W.", "0,25 W."],
   "B",
   "P = F·v = 0,20 · 5,0 = 1,00 W.\n"
   "Kiểm tra bằng công suất điện: P = e·i = 0,50 · 2,0 = 1,00 W — toàn bộ công cơ học chuyển "
   "thành nhiệt trên khung.",
   "Chuyển hoá năng lượng", K),

mc("Một máy biến áp lí tưởng cấp cho một động cơ 1,5 kW ở điện áp 200 V. Cuộn sơ cấp nối vào "
   "mạng 500 V. Cường độ dòng điện hiệu dụng trong cuộn sơ cấp bằng",
   ["7,5 A.", "3,0 A.", "1,5 A.", "5,0 A."],
   "B",
   "Máy lí tưởng nên P₁ = P₂ = 1500 W.\n"
   "I₁ = 1500/500 = 3,0 A.",
   "Máy biến áp – công suất", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 6,0 MW ở điện áp 60 kV, điện trở đường dây 12 Ω. Công suất tới nơi tiêu thụ "
   "bằng",
   ["5,88 MW.", "5,76 MW.", "5,40 MW.", "5,98 MW."],
   "A",
   "I = 6,0·10⁶/(60·10³) = 100 A.\n"
   "ΔP = 12 · 10⁴ = 1,2·10⁵ W = 0,12 MW.\n"
   "Công suất tới nơi tiêu thụ: 6,0 − 0,12 = 5,88 MW.",
   "Truyền tải điện năng", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một hạt nhân ²²⁶₈₈Ra đứng yên phóng xạ α, toả 4,87 MeV. Động năng hạt α xấp xỉ",
   ["4,78 MeV.", "4,96 MeV.", "4,87 MeV.", "0,09 MeV."],
   "A",
   "Hạt nhân con là ²²²₈₆Rn.\n"
   "W(α) = ΔE · 222/226 = 4,87 · 222/226 ≈ 4,78 MeV.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một mẫu chất phóng xạ ban đầu có 4,0·10²⁰ hạt nhân, chu kì bán rã 3,0 giờ. "
   "Số hạt nhân phân rã trong khoảng từ giờ thứ 3 đến giờ thứ 6 bằng",
   ["2,0·10²⁰.", "1,0·10²⁰.", "3,0·10²⁰.", "0,5·10²⁰."],
   "B",
   "Tại t = 3 giờ (1 chu kì): N = 2,0·10²⁰.\n"
   "Tại t = 6 giờ (2 chu kì): N = 1,0·10²⁰.\n"
   "Số hạt phân rã trong khoảng đó: 2,0·10²⁰ − 1,0·10²⁰ = 1,0·10²⁰ hạt.",
   "Số hạt phân rã theo từng khoảng", K),

mc("Một mẫu đá chứa ²³⁸U và ²⁰⁶Pb với tỉ số KHỐI LƯỢNG Pb/U bằng 0,50. Tuổi mẫu đá xấp xỉ "
   "(T = 4,5 tỉ năm; ln2 ≈ 0,693)",
   ["2,4 tỉ năm.", "2,9 tỉ năm.", "3,4 tỉ năm.", "1,9 tỉ năm."],
   "B",
   "(206/238)·(2ⁿ − 1) = 0,50 ⇒ 2ⁿ − 1 = 0,50 · 238/206 ≈ 0,5777.\n"
   "2ⁿ = 1,5777 ⇒ n = ln1,5777/ln2 = 0,4559/0,693 ≈ 0,658.\n"
   "t = 0,658 · 4,5 ≈ 2,9 tỉ năm.",
   "Xác định tuổi mẫu đá", RK),

mc("Cho biết năng lượng liên kết riêng của ⁴He là 7,10 MeV/nuclêôn và của ⁷Li là 5,60 MeV/nuclêôn. "
   "Phản ứng ¹₁H + ⁷₃Li → 2·⁴₂He toả ra xấp xỉ",
   ["11,6 MeV.", "17,6 MeV.", "23,6 MeV.", "5,6 MeV."],
   "B",
   "Năng lượng liên kết trước: prôtôn 0; ⁷Li = 7 · 5,60 = 39,2 MeV.\n"
   "Năng lượng liên kết sau: 2 · 4 · 7,10 = 56,8 MeV.\n"
   "ΔE = 56,8 − 39,2 = 17,6 MeV.",
   "Năng lượng phản ứng theo W(lk)", K),

mc("Một lò phản ứng công suất nhiệt 3000 MW dùng ²³⁵U. Khối lượng nhiên liệu tiêu thụ trong "
   "một giờ xấp xỉ (200 MeV mỗi phân hạch)",
   ["0,13 kg.", "0,39 kg.", "0,26 kg.", "0,06 kg."],
   "A",
   "Số phân hạch mỗi giây: 3,0·10⁹/3,2·10⁻¹¹ = 9,375·10¹⁹.\n"
   "Trong 1 giờ: 9,375·10¹⁹ · 3600 = 3,375·10²³ hạt.\n"
   "Khối lượng: (3,375·10²³/6,02·10²³) · 235 ≈ 0,5607 · 235 ≈ 132 g ≈ 0,13 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

mc("Một nguồn phóng xạ được coi là an toàn để vận chuyển khi độ phóng xạ còn dưới 1/64 giá trị "
   "ban đầu. Nếu chu kì bán rã là 6,0 giờ thì phải chờ ít nhất",
   ["24 giờ.", "36 giờ.", "48 giờ.", "18 giờ."],
   "B",
   "1/64 = 2⁻⁶ ⇒ n = 6 chu kì.\n"
   "t = 6 · 6,0 = 36 giờ.",
   "Định luật phóng xạ", K),

mc("Trong một mẫu chất phóng xạ, tỉ số giữa độ phóng xạ tại thời điểm t và tại thời điểm t + T "
   "(T là chu kì bán rã) bằng",
   ["1.", "2.", "4.", "1/2."],
   "B",
   "Sau thêm một chu kì bán rã, độ phóng xạ giảm một nửa, nên tỉ số H(t)/H(t + T) = 2 "
   "với mọi giá trị của t.",
   "Bản chất hàm mũ của phân rã", K),

mc("Nhận định nào sau đây SAI khi nói về ứng dụng của đồng vị phóng xạ?",
   ["Tia γ dùng trong xạ trị vì đâm xuyên tốt.",
    "Tia α dùng để chiếu xạ khối u nằm sâu trong cơ thể.",
    "Tia β dùng đo bề dày tấm kim loại mỏng.",
    "¹⁴C dùng xác định tuổi mẫu vật khảo cổ."],
   "B",
   "Tia α bị chặn ngay bởi lớp da nên không thể tới khối u nằm sâu. Xạ trị khối u sâu dùng tia γ. "
   "Ba nhận định còn lại đều đúng.",
   "Ứng dụng của đồng vị phóng xạ", TB, fig="h_sd_ung_dung",
   cap="Ứng dụng của đồng vị phóng xạ"),
],
P2=[
ds("Một bếp từ công suất 2000 W, hiệu suất 85 %, đun 2,5 kg nước từ 25 °C. "
   "Cho c(nước) = 4200 J/(kg·K).",
   [("Công suất nhiệt có ích của bếp là 1700 W.", True,
     "Đúng. 2000 · 0,85 = 1700 W."),
    ("Nhiệt lượng cần để nước sôi là 787,5 kJ.", True,
     "Đúng. Q = 2,5 · 4200 · 75 = 787 500 J."),
    ("Thời gian đun tới sôi xấp xỉ 463 giây.", True,
     "Đúng. t = 787 500/1700 ≈ 463 s."),
    ("Bếp từ làm nóng nước nhờ bức xạ nhiệt từ cuộn dây cao tần.", False,
     "Sai. Bếp từ làm nóng ĐÁY NỒI nhờ dòng điện Foucault sinh ra trong đáy nồi nhiễm từ, "
     "rồi nhiệt mới truyền vào nước.")],
   "Hiệu suất và bếp từ", K, fig="t_sd_bep_tu", cap="Nguyên lí bếp từ"),

ds("Một xi lanh thẳng đứng tiết diện 50 cm² chứa khí, pit-tông khối lượng 10 kg trượt không ma sát. "
   "Áp suất khí quyển 1,0·10⁵ Pa; g = 10 m/s²; nhiệt độ không đổi.",
   [("Áp suất do trọng lượng pit-tông gây ra là 2,0·10⁴ Pa.", True,
     "Đúng. mg/S = 10 · 10/(50·10⁻⁴) = 100/0,0050 = 2,0·10⁴ Pa."),
    ("Khi miệng xi lanh ở trên, áp suất khí là 1,2·10⁵ Pa.", True,
     "Đúng. p = 1,0·10⁵ + 0,2·10⁵ = 1,2·10⁵ Pa."),
    ("Khi lật ngược cho miệng xuống dưới, áp suất khí là 0,8·10⁵ Pa.", True,
     "Đúng. p = 1,0·10⁵ − 0,2·10⁵ = 0,8·10⁵ Pa."),
    ("Sau khi lật, thể tích khí giảm đi 1,5 lần.", False,
     "Sai. Áp suất giảm nên thể tích TĂNG 1,5 lần theo định luật Boyle.")],
   "Bài toán pit-tông", RK, fig="k_sd_xilanh_quanang", cap="Xi lanh có pit-tông"),

ds("Một khung dây hình vuông cạnh 20 cm, điện trở 0,25 Ω, chuyển động đều 5,0 m/s đi vào vùng "
   "từ trường đều B = 0,50 T.",
   [("Suất điện động cảm ứng khi khung đi vào là 0,50 V.", True,
     "Đúng. e = B·a·v = 0,50 · 0,20 · 5,0 = 0,50 V."),
    ("Cường độ dòng cảm ứng là 2,0 A.", True,
     "Đúng. i = 0,50/0,25 = 2,0 A."),
    ("Lực kéo cần thiết để khung đi đều là 0,20 N.", True,
     "Đúng. F = B·i·a = 0,50 · 2,0 · 0,20 = 0,20 N."),
    ("Công suất cơ học cần cung cấp là 0,50 W.", False,
     "Sai. P = F·v = 0,20 · 5,0 = 1,00 W, cũng bằng e·i = 0,50 · 2,0 = 1,00 W.")],
   "Năng lượng trong cảm ứng điện từ", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

ds("Một mẫu đá chứa ²³⁸U (chu kì bán rã 4,5 tỉ năm) và sản phẩm bền ²⁰⁶Pb với tỉ số khối lượng "
   "Pb/U bằng 0,50. Lấy ln2 ≈ 0,693.",
   [("Tỉ số SỐ HẠT NHÂN Pb/U xấp xỉ 0,578.", True,
     "Đúng. Nhân tỉ số khối lượng với 238/206: 0,50 · 238/206 ≈ 0,5777."),
    ("Số chu kì bán rã đã trôi qua xấp xỉ 0,658.", True,
     "Đúng. 2ⁿ = 1,5777 ⇒ n = 0,4559/0,693 ≈ 0,658."),
    ("Tuổi của mẫu đá xấp xỉ 2,9 tỉ năm.", True,
     "Đúng. t = 0,658 · 4,5 ≈ 2,96 tỉ năm."),
    ("Có thể dùng trực tiếp tỉ số khối lượng thay cho tỉ số số hạt nhân mà không ảnh hưởng kết quả.", False,
     "Sai. Hai đồng vị có số khối khác nhau (238 và 206) nên phải quy đổi; bỏ qua bước này sẽ cho "
     "tuổi khoảng 2,6 tỉ năm, sai lệch đáng kể.")],
   "Xác định tuổi mẫu đá", RK),
],
P3=[
sa("Một bếp từ công suất 1600 W, hiệu suất 80 %, đun 1,8 kg nước từ 22 °C. Sau 6,0 phút, "
   "nhiệt độ nước đạt bao nhiêu độ Celsius (làm tròn đến hàng đơn vị)? "
   "Cho c(nước) = 4200 J/(kg·K).",
   "83",
   "Nhiệt lượng có ích: Q = 1600 · 0,80 · 360 = 460 800 J.\n"
   "ΔT = 460 800/(1,8 · 4200) = 460 800/7560 ≈ 60,95 °C.\n"
   "Nhiệt độ đạt được: 22 + 60,95 ≈ 83 °C.",
   "Hiệu suất và công suất", K),

sa("Một xi lanh thẳng đứng tiết diện 25 cm², pit-tông khối lượng 5,0 kg trượt không ma sát, "
   "miệng ở trên. Áp suất khí quyển 1,0·10⁵ Pa. Nếu lật ngược xi lanh (nhiệt độ không đổi) thì "
   "thể tích khí tăng gấp bao nhiêu lần (làm tròn đến chữ số thập phân thứ hai)? Lấy g = 10 m/s².",
   "1,5",
   "Áp suất do pit-tông: mg/S = 5,0 · 10/(25·10⁻⁴) = 50/0,0025 = 2,0·10⁴ Pa.\n"
   "Miệng trên: p₁ = 1,2·10⁵ Pa.  Miệng dưới: p₂ = 0,8·10⁵ Pa.\n"
   "V₂/V₁ = p₁/p₂ = 1,2/0,8 = 1,50 lần.",
   "Bài toán pit-tông", RK),

sa("Một khung dây hình vuông cạnh 25 cm, điện trở 0,20 Ω, chuyển động đều 4,0 m/s đi vào vùng "
   "từ trường đều B = 0,40 T. Công suất cơ học cần cung cấp để khung đi đều bằng bao nhiêu oát?",
   "0,8",
   "e = B·a·v = 0,40 · 0,25 · 4,0 = 0,40 V.\n"
   "i = e/R = 0,40/0,20 = 2,0 A.\n"
   "P = e·i = 0,40 · 2,0 = 0,80 W.",
   "Chuyển hoá năng lượng", K),

sa("Truyền công suất 8,0 MW ở điện áp 80 kV trên đường dây có điện trở 15 Ω. Công suất tới nơi "
   "tiêu thụ bằng bao nhiêu mêgaoát (làm tròn đến chữ số thập phân thứ hai)?",
   "7,85",
   "I = P/U = 8,0·10⁶/(80·10³) = 100 A.\n"
   "ΔP = R·I² = 15 · 10⁴ = 1,5·10⁵ W = 0,15 MW.\n"
   "Công suất tới nơi tiêu thụ: 8,00 − 0,15 = 7,85 MW.",
   "Truyền tải điện năng", K),

sa("Một mẫu chất phóng xạ ban đầu có 6,4·10²⁰ hạt nhân, chu kì bán rã 4,0 giờ. Số hạt nhân phân rã "
   "trong khoảng từ giờ thứ 4 đến giờ thứ 12 bằng bao nhiêu (viết dưới dạng x·10²⁰, "
   "chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)?",
   "2,4",
   "Tại t = 4 giờ (1 chu kì): N = 3,2·10²⁰ hạt.\n"
   "Tại t = 12 giờ (3 chu kì): N = 0,8·10²⁰ hạt.\n"
   "Số hạt phân rã: 3,2·10²⁰ − 0,8·10²⁰ = 2,4·10²⁰ hạt.",
   "Số hạt phân rã theo từng khoảng", K),

sa("Một lò phản ứng công suất nhiệt 2400 MW dùng ²³⁵U, mỗi phân hạch toả 200 MeV. "
   "Khối lượng nhiên liệu tiêu thụ trong một giờ bằng bao nhiêu gam (làm tròn đến hàng đơn vị)? "
   "Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   "105",
   "Số phân hạch mỗi giây: 2,4·10⁹/3,2·10⁻¹¹ = 7,5·10¹⁹.\n"
   "Trong 1 giờ: 7,5·10¹⁹ · 3600 = 2,7·10²³ hạt.\n"
   "Số mol: 2,7·10²³/6,02·10²³ ≈ 0,4485 mol.\n"
   "Khối lượng: 0,4485 · 235 ≈ 105 g.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK),
])


# =====================================================================  ĐỀ 22
DE22 = dict(
ma="TH-Đề 22", ten="ĐỀ THI THỬ SỐ 22", muc="Khó",
trongtam="Bài toán thực tiễn nhiều dữ kiện, đồ thị và phân tích năng lượng",
P1=[
mc("Một nồi áp suất kín chứa nước và hơi. Khi nhiệt độ tăng từ 100 °C lên 120 °C, "
   "áp suất hơi trong nồi",
   ["giảm.", "tăng.", "không đổi.", "bằng không."],
   "B",
   "Nồi kín, thể tích không đổi; nhiệt độ tăng làm phân tử chuyển động nhanh hơn và số phân tử "
   "hơi cũng tăng, nên áp suất tăng. Đó là lí do nồi áp suất nấu nhanh hơn nồi thường.",
   "Ứng dụng thực tiễn của chất khí", TB),

mc("Một nhiệt lượng kế bằng nhôm khối lượng 0,20 kg chứa 0,80 kg nước ở 20 °C. Thả vào đó một "
   "miếng kim loại 0,50 kg ở 100 °C, nhiệt độ cân bằng 24 °C. Nhiệt dung riêng của kim loại xấp xỉ "
   "(c(nhôm) = 880; c(nước) = 4200 J/(kg·K))",
   ["330 J/(kg·K).", "372 J/(kg·K).", "420 J/(kg·K).", "290 J/(kg·K)."],
   "B",
   "Nhiệt thu vào: nước 0,80·4200·4 = 13 440 J; nhiệt lượng kế 0,20·880·4 = 704 J.\n"
   "Tổng nhiệt thu: 14 144 J.\n"
   "Nhiệt toả: 0,50·c·(100 − 24) = 38·c.\n"
   "38·c = 14 144 ⇒ c ≈ 372 J/(kg·K).",
   "Thí nghiệm nhiệt lượng kế", RK, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

mc("Trong bài trên, nếu BỎ QUA nhiệt lượng mà nhiệt lượng kế thu vào thì giá trị c tính được sẽ",
   ["lớn hơn giá trị thực.", "nhỏ hơn giá trị thực.",
    "bằng giá trị thực.", "bằng không."],
   "B",
   "Bỏ qua phần nhiệt của nhiệt lượng kế làm tổng nhiệt thu vào tính được nhỏ đi (13 440 J thay vì "
   "14 144 J), kéo theo c = 13 440/38 ≈ 354 J/(kg·K), nhỏ hơn giá trị thực 372 J/(kg·K).",
   "Sai số thí nghiệm", RK),

mc("Một khối khí lí tưởng ở 27 °C được nén đoạn nhiệt làm nội năng tăng 900 J. "
   "Công mà môi trường thực hiện lên khí bằng",
   ["450 J.", "900 J.", "1800 J.", "0 J."],
   "B",
   "Đoạn nhiệt nên Q = 0, do đó ΔU = A. Nội năng tăng 900 J nên khí nhận công A = 900 J.",
   "Định luật I nhiệt động lực học", K),

mc("Một bình 10 L chứa khí ở 27 °C, áp suất 4,0·10⁵ Pa. Nối bình này với bình 30 L chân không "
   "rồi giữ nhiệt độ không đổi. Áp suất chung bằng",
   ["2,0·10⁵ Pa.", "1,0·10⁵ Pa.", "1,33·10⁵ Pa.", "0,50·10⁵ Pa."],
   "B",
   "Thể tích tổng: 10 + 30 = 40 L, gấp 4 lần thể tích ban đầu.\n"
   "Đẳng nhiệt: p₂ = 4,0·10⁵/4 = 1,0·10⁵ Pa.",
   "Định luật Boyle", K),

mc("Nếu sau khi nối hai bình ở câu trên, ta nung nóng toàn hệ lên 127 °C thì áp suất bằng",
   ["1,33·10⁵ Pa.", "0,75·10⁵ Pa.", "1,50·10⁵ Pa.", "2,00·10⁵ Pa."],
   "A",
   "Đẳng tích từ trạng thái (1,0·10⁵ Pa; 300 K) sang 400 K:\n"
   "p = 1,0·10⁵ · 400/300 ≈ 1,33·10⁵ Pa.",
   "Hai quá trình liên tiếp", K),

mc("Một khung dây hình vuông cạnh a đặt trong từ trường đều B vuông góc mặt phẳng khung. "
   "Nếu kéo giãn khung thành hình chữ nhật có cùng chu vi, kích thước 1,5a × 0,5a thì từ thông",
   ["tăng.", "giảm.", "không đổi.", "bằng không."],
   "B",
   "Diện tích ban đầu a²; sau khi kéo giãn là 1,5a · 0,5a = 0,75a² < a².\n"
   "Từ thông Φ = B·S giảm theo diện tích. Với chu vi cho trước, hình vuông có diện tích lớn nhất "
   "trong các hình chữ nhật.",
   "Từ thông và diện tích", RK),

mc("Một thanh dẫn dài 50 cm trượt đều trên hai ray nằm ngang với tốc độ 4,0 m/s, vuông góc với "
   "từ trường đều thẳng đứng B = 0,60 T, điện trở toàn mạch 0,30 Ω. Công suất toả nhiệt bằng",
   ["2,4 W.", "4,8 W.", "1,2 W.", "9,6 W."],
   "B",
   "e = B·ℓ·v = 0,60 · 0,50 · 4,0 = 1,20 V.\n"
   "P = e²/R = 1,44/0,30 = 4,8 W.",
   "Chuyển hoá năng lượng", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 2000 vòng nối vào 400 V. Cuộn thứ cấp 500 vòng nối với "
   "một bóng đèn ghi 100 V – 200 W, đèn sáng bình thường. Cường độ dòng ở cuộn sơ cấp bằng",
   ["2,0 A.", "0,50 A.", "8,0 A.", "1,0 A."],
   "B",
   "Điện áp thứ cấp: U₂ = 400 · 500/2000 = 100 V — đèn sáng bình thường.\n"
   "Công suất: P = 200 W ⇒ I₁ = P/U₁ = 200/400 = 0,50 A.",
   "Máy biến áp có tải", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 1,2 MW ở điện áp 12 kV, hiệu suất 90 %. Muốn nâng hiệu suất lên 97,5 % "
   "mà giữ nguyên công suất thì phải tăng điện áp lên",
   ["18 kV.", "24 kV.", "36 kV.", "48 kV."],
   "B",
   "Hao phí giảm từ 10 % xuống 2,5 %, tức giảm 4 lần ⇒ điện áp tăng √4 = 2 lần.\n"
   "U = 2 · 12 = 24 kV.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Hạt nhân ²³⁸₉₂U có khối lượng 238,0508 u. Cho m(p) = 1,0073; m(n) = 1,0087 u. "
   "Năng lượng liên kết riêng của hạt nhân này xấp xỉ",
   ["6,8 MeV/nuclêôn.", "7,6 MeV/nuclêôn.",
    "8,2 MeV/nuclêôn.", "5,4 MeV/nuclêôn."],
   "B",
   "Số nơtron: 238 − 92 = 146.\n"
   "Tổng khối lượng nuclêôn: 92 · 1,0073 + 146 · 1,0087 = 92,6716 + 147,2702 = 239,9418 u.\n"
   "Δm = 239,9418 − 238,0508 = 1,8910 u.\n"
   "W(lk) = 1,8910 · 931,5 ≈ 1761,5 MeV ⇒ ε = 1761,5/238 ≈ 7,4 MeV/nuclêôn, "
   "gần nhất với 7,6 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", RK),

mc("Một mẫu chất phóng xạ có chu kì bán rã 10 ngày, ban đầu 200 gam. Khối lượng phân rã trong "
   "khoảng từ ngày thứ 10 đến ngày thứ 30 bằng",
   ["75 gam.", "125 gam.", "50 gam.", "100 gam."],
   "A",
   "Tại t = 10 ngày: m = 100 g.  Tại t = 30 ngày: m = 200/2³ = 25 g.\n"
   "Khối lượng phân rã: 100 − 25 = 75 g.",
   "Số hạt phân rã theo từng khoảng", K),

mc("Một nguồn phóng xạ có độ phóng xạ 3,0·10¹⁰ Bq. Nếu mỗi phân rã toả 1,2 MeV thì năng lượng "
   "toả ra trong 8,0 giờ xấp xỉ (1 MeV = 1,6·10⁻¹³ J)",
   ["166 J.", "249 J.", "332 J.", "83 J."],
   "A",
   "Công suất: P = 3,0·10¹⁰ · 1,2 · 1,6·10⁻¹³ = 3,0·10¹⁰ · 1,92·10⁻¹³ = 5,76·10⁻³ W.\n"
   "Thời gian: 8,0 · 3600 = 28 800 s.\n"
   "E = 5,76·10⁻³ · 28 800 ≈ 166 J.",
   "Công suất của nguồn phóng xạ", K),

mc("Trong phản ứng nhiệt hạch ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV, nếu bỏ qua động năng ban đầu "
   "thì động năng của nơtron xấp xỉ",
   ["3,5 MeV.", "14,1 MeV.", "8,8 MeV.", "17,6 MeV."],
   "B",
   "Hai hạt sinh ra có động lượng cùng độ lớn nên động năng tỉ lệ nghịch khối lượng.\n"
   "W(n)/ΔE = A(He)/(A(He) + A(n)) = 4/5 ⇒ W(n) = 17,6 · 4/5 = 14,1 MeV.",
   "Bảo toàn động lượng trong phản ứng", RK, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Một chất phóng xạ có chu kì bán rã T. Khoảng thời gian để độ phóng xạ giảm từ 100 % xuống "
   "6,25 % bằng",
   ["2T.", "4T.", "3T.", "5T."],
   "B",
   "6,25 % = 1/16 = 2⁻⁴ ⇒ n = 4 chu kì bán rã.",
   "Định luật phóng xạ", TB),

mc("Trong lò phản ứng hạt nhân dùng nước nhẹ, nếu nhiệt độ tăng làm nước bốc hơi bớt thì "
   "hệ số nhân nơtron",
   ["tăng, phản ứng mạnh lên.", "giảm, phản ứng yếu đi.",
    "không đổi.", "bằng 0 ngay lập tức."],
   "B",
   "Nước vừa là chất tải nhiệt vừa là chất làm chậm. Nước bốc hơi bớt thì khả năng làm chậm giảm, "
   "nơtron giữ tốc độ cao nên ít gây phân hạch hơn: k giảm và phản ứng tự yếu đi. "
   "Đây là một cơ chế an toàn nội tại của lò dùng nước nhẹ.",
   "Lò phản ứng hạt nhân", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Khi nói về việc lưu giữ chất thải phóng xạ, phát biểu nào ĐÚNG?",
   ["Chỉ cần lưu giữ vài tháng là an toàn.",
    "Phải lưu giữ hàng trăm tới hàng nghìn năm vì nhiều đồng vị có chu kì bán rã rất dài.",
    "Có thể trung hoà chất thải bằng phản ứng hoá học.",
    "Đun nóng chất thải sẽ làm nó mất tính phóng xạ."],
   "B",
   "Phóng xạ không thể bị trung hoà bằng phản ứng hoá học hay tác động nhiệt. Cách duy nhất là "
   "cách li an toàn cho tới khi chất thải tự phân rã hết — với nhiều đồng vị việc đó mất hàng "
   "trăm tới hàng nghìn năm.",
   "An toàn hạt nhân", TB),

mc("Một mẫu chất phóng xạ nguyên chất, sau thời gian t có 75 % số hạt nhân đã phân rã. "
   "Thời gian t bằng",
   ["T.", "2T.", "3T.", "4T."],
   "B",
   "Còn lại 25 % = 1/4 = 2⁻² ⇒ n = 2 chu kì bán rã.",
   "Định luật phóng xạ", TB),
],
P2=[
ds("Một nồi áp suất kín chứa nước, khi đun thì nhiệt độ trong nồi có thể lên tới 120 °C.",
   [("Trong nồi kín, áp suất hơi tăng khi nhiệt độ tăng.", True,
     "Đúng. Thể tích không đổi, phân tử chuyển động nhanh hơn và số phân tử hơi cũng tăng."),
    ("Nhiệt độ sôi của nước tăng khi áp suất tăng.", True,
     "Đúng. Đó là lí do nước trong nồi áp suất sôi ở nhiệt độ cao hơn 100 °C."),
    ("Nhờ nhiệt độ cao hơn nên thức ăn chín nhanh hơn.", True,
     "Đúng. Tốc độ các quá trình làm mềm thực phẩm tăng mạnh theo nhiệt độ."),
    ("Khi mở nắp nồi áp suất đang nóng, nước trong nồi lập tức ngừng sôi.", False,
     "Sai. Áp suất đột ngột giảm về áp suất khí quyển làm nhiệt độ sôi hạ xuống 100 °C, "
     "trong khi nước đang ở 120 °C nên nước SÔI BÙNG rất mạnh — đó là lí do phải xả áp trước "
     "khi mở nắp.")],
   "Ứng dụng thực tiễn của chất khí", K),

ds("Một bình 10 L chứa khí lí tưởng ở 27 °C, áp suất 4,0·10⁵ Pa được nối với bình 30 L chân không. "
   "Sau đó hệ được nung nóng lên 127 °C.",
   [("Ngay sau khi nối, áp suất chung là 1,0·10⁵ Pa.", True,
     "Đúng. Thể tích tăng 4 lần nên áp suất giảm 4 lần."),
    ("Sau khi nung lên 127 °C, áp suất xấp xỉ 1,33·10⁵ Pa.", True,
     "Đúng. Đẳng tích: p = 1,0·10⁵ · 400/300 ≈ 1,33·10⁵ Pa."),
    ("Trong quá trình khí giãn vào bình chân không, khí không thực hiện công.", True,
     "Đúng. Khí giãn vào chân không nên không phải đẩy vật gì."),
    ("Sau khi nối hai bình, số mol khí trong hệ giảm đi 4 lần.", False,
     "Sai. Toàn bộ lượng khí vẫn nằm trong hệ hai bình nên số mol KHÔNG đổi; "
     "chỉ có thể tích tăng và áp suất giảm.")],
   "Giãn khí vào chân không", K),

ds("Một thanh dẫn dài 50 cm trượt đều với tốc độ 4,0 m/s trên hai ray nằm ngang, vuông góc với "
   "từ trường đều thẳng đứng B = 0,60 T, điện trở toàn mạch 0,30 Ω.",
   [("Suất điện động cảm ứng bằng 1,20 V.", True,
     "Đúng. e = 0,60 · 0,50 · 4,0 = 1,20 V."),
    ("Cường độ dòng điện trong mạch bằng 4,0 A.", True,
     "Đúng. i = 1,20/0,30 = 4,0 A."),
    ("Lực từ cản tác dụng lên thanh bằng 1,20 N.", True,
     "Đúng. F = B·i·ℓ = 0,60 · 4,0 · 0,50 = 1,20 N."),
    ("Công suất cơ học cần cung cấp bằng 1,20 W.", False,
     "Sai. P = F·v = 1,20 · 4,0 = 4,8 W, cũng bằng e·i = 1,20 · 4,0 = 4,8 W.")],
   "Chuyển hoá năng lượng", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

ds("Trong phản ứng nhiệt hạch ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV, hai hạt tới có động năng "
   "không đáng kể.",
   [("Hai hạt sinh ra có động lượng cùng độ lớn và ngược hướng.", True,
     "Đúng. Tổng động lượng ban đầu coi như bằng 0."),
    ("Động năng của hai hạt tỉ lệ nghịch với khối lượng của chúng.", True,
     "Đúng. Với cùng độ lớn động lượng, W = p²/(2m)."),
    ("Động năng của nơtron xấp xỉ 14,1 MeV.", True,
     "Đúng. W(n) = 17,6 · 4/(4 + 1) = 14,08 MeV."),
    ("Động năng của hạt nhân heli lớn hơn động năng của nơtron.", False,
     "Sai. Heli nặng gấp 4 lần nơtron nên chỉ mang 17,6 · 1/5 = 3,52 MeV, nhỏ hơn nhiều.")],
   "Bảo toàn động lượng trong phản ứng", RK, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),
],
P3=[
sa("Một nhiệt lượng kế bằng đồng khối lượng 0,30 kg chứa 1,0 kg nước ở 18 °C. Thả vào đó một miếng "
   "kim loại 0,40 kg ở 120 °C, nhiệt độ cân bằng 22 °C. Nhiệt dung riêng của kim loại bằng bao "
   "nhiêu J/(kg·K) (làm tròn đến hàng đơn vị)? Cho c(đồng) = 380; c(nước) = 4200 J/(kg·K).",
   "440",
   "Nhiệt nước thu: 1,0 · 4200 · 4 = 16 800 J.\n"
   "Nhiệt bình đồng thu: 0,30 · 380 · 4 = 456 J.\n"
   "Tổng nhiệt thu: 17 256 J.\n"
   "Nhiệt toả: 0,40 · c · (120 − 22) = 39,2·c.\n"
   "39,2·c = 17 256 ⇒ c ≈ 440 J/(kg·K).",
   "Thí nghiệm nhiệt lượng kế", RK),

sa("Một bình 8,0 L chứa khí lí tưởng ở 27 °C, áp suất 6,0·10⁵ Pa được nối với bình 16 L chân không, "
   "nhiệt độ giữ nguyên. Áp suất chung bằng bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x)?",
   "2",
   "Thể tích tổng: 8,0 + 16 = 24 L, gấp 3 lần thể tích ban đầu.\n"
   "Đẳng nhiệt: p₂ = 6,0·10⁵/3 = 2,0·10⁵ Pa.",
   "Định luật Boyle", K),

sa("Một khung dây hình vuông cạnh 30 cm đặt vuông góc với từ trường đều B = 0,40 T. "
   "Nếu kéo giãn khung thành hình chữ nhật 45 cm × 15 cm (cùng chu vi) thì từ thông giảm đi "
   "bao nhiêu miliweber (làm tròn đến chữ số thập phân thứ nhất)?",
   "9,0",
   "Diện tích ban đầu: 0,30² = 0,090 m² ⇒ Φ₁ = 0,40 · 0,090 = 0,036 Wb.\n"
   "Diện tích sau: 0,45 · 0,15 = 0,0675 m² ⇒ Φ₂ = 0,40 · 0,0675 = 0,027 Wb.\n"
   "Độ giảm: 0,036 − 0,027 = 0,009 Wb = 9,0 mWb.",
   "Từ thông và diện tích", RK),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 1800 vòng nối vào 360 V, cuộn thứ cấp 300 vòng nối "
   "với một bóng đèn ghi 60 V – 120 W và đèn sáng bình thường. Cường độ dòng điện hiệu dụng ở "
   "cuộn sơ cấp bằng bao nhiêu ampe (làm tròn đến chữ số thập phân thứ hai)?",
   "0,33",
   "Điện áp thứ cấp: U₂ = 360 · 300/1800 = 60 V — đèn sáng bình thường.\n"
   "Máy lí tưởng nên P₁ = P₂ = 120 W.\n"
   "I₁ = 120/360 ≈ 0,33 A.",
   "Máy biến áp có tải", K),

sa("Một mẫu chất phóng xạ nguyên chất, sau thời gian t có 93,75 % số hạt nhân đã phân rã. "
   "Thời gian t bằng bao nhiêu lần chu kì bán rã?",
   "4",
   "Số hạt còn lại: 100 − 93,75 = 6,25 % = 1/16 = 2⁻ⁿ.\n"
   "Suy ra 2ⁿ = 16 ⇒ n = 4, tức t = 4·T.",
   "Định luật phóng xạ", K),

sa("Trong phản ứng ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV (bỏ qua động năng ban đầu), "
   "động năng của hạt nhân heli bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)?",
   "3,52",
   "Hai hạt sinh ra có động lượng cùng độ lớn nên động năng tỉ lệ nghịch với khối lượng.\n"
   "W(He) = ΔE · A(n)/(A(He) + A(n)) = 17,6 · 1/5 = 3,52 MeV.",
   "Bảo toàn động lượng trong phản ứng", RK),
])


# =====================================================================  ĐỀ 23
DE23 = dict(
ma="TH-Đề 23", ten="ĐỀ THI THỬ SỐ 23", muc="Khó",
trongtam="Vận dụng cao trên cả bốn chương, nhiều câu đòi hỏi biện luận trước khi tính",
P1=[
mc("Cần cung cấp bao nhiêu nhiệt lượng để biến 1,2 kg nước đá ở −5,0 °C thành nước ở 0 °C? "
   "Cho c(đá) = 2100 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   ["408 kJ.", "420,6 kJ.", "12,6 kJ.", "396 kJ."],
   "B",
   "Giai đoạn 1: Q₁ = 1,2 · 2100 · 5,0 = 12 600 J.\n"
   "Giai đoạn 2: Q₂ = 1,2 · 3,4·10⁵ = 408 000 J.\n"
   "Tổng: Q = 12 600 + 408 000 = 420 600 J = 420,6 kJ.",
   "Bài toán nhiều giai đoạn", K),

mc("Một động cơ nhiệt mỗi chu trình nhận 1500 J từ nguồn nóng, hiệu suất 24 %. "
   "Nhiệt lượng thải cho nguồn lạnh bằng",
   ["360 J.", "1140 J.", "1260 J.", "1176 J."],
   "B",
   "Công sinh ra: A = 0,24 · 1500 = 360 J.\n"
   "Nhiệt thải: Q(thải) = 1500 − 360 = 1140 J.",
   "Hiệu suất động cơ nhiệt", K),

mc("Một khối khí lí tưởng giãn nở đẳng áp ở 1,2·10⁵ Pa, thể tích từ 2,5 L lên 7,5 L. "
   "Công mà khí sinh ra bằng",
   ["300 J.", "600 J.", "900 J.", "150 J."],
   "B",
   "A = p·ΔV = 1,2·10⁵ · (7,5 − 2,5)·10⁻³ = 1,2·10⁵ · 5,0·10⁻³ = 600 J.",
   "Công của chất khí", K),

mc("Một khối khí lí tưởng có khối lượng riêng 1,25 kg/m³ ở 0 °C và 1,0·10⁵ Pa. "
   "Khối lượng mol của khí đó xấp xỉ (R = 8,31 J/(mol·K))",
   ["0,024 kg/mol.", "0,028 kg/mol.", "0,032 kg/mol.", "0,044 kg/mol."],
   "B",
   "T = 273 K.\n"
   "M = ρRT/p = 1,25 · 8,31 · 273/(1,0·10⁵) = 2835,8/10⁵ ≈ 0,0284 kg/mol, "
   "tức khoảng 28 g/mol (khí nitơ).",
   "Khối lượng riêng của khí", K),

mc("Ở 27 °C, động năng tịnh tiến trung bình của phân tử khí là W. Ở 327 °C, giá trị đó bằng",
   ["W.", "2W.", "12W.", "1,5W."],
   "B",
   "W̄ₐ = (3/2)kT tỉ lệ thuận với T (kelvin).\n"
   "T tăng từ 300 K lên 600 K, tức gấp đôi, nên động năng trung bình cũng gấp đôi.",
   "Động năng phân tử", K),

mc("Một đoạn dây dẫn dài 25 cm mang dòng điện 8,0 A đặt trong từ trường đều B = 0,50 T, "
   "hợp với đường sức góc 37° (sin37° = 0,60). Lực từ tác dụng lên dây bằng",
   ["0,80 N.", "0,60 N.", "1,00 N.", "0,40 N."],
   "B",
   "F = B·I·ℓ·sin37° = 0,50 · 8,0 · 0,25 · 0,60 = 1,0 · 0,60 = 0,60 N.",
   "Lực từ", K),

mc("Một khung dây phẳng 300 vòng, diện tích mỗi vòng 60 cm², đặt trong từ trường đều B = 0,50 T "
   "với pháp tuyến hợp đường sức góc 60°. Từ thông qua khung bằng",
   ["0,90 Wb.", "0,45 Wb.", "0,18 Wb.", "0,225 Wb."],
   "B",
   "Từ thông qua cả khung N vòng: Φ = N·B·S·cos60°.\n"
   "Φ = 300 · 0,50 · 6,0·10⁻³ · 0,50 = 300 · 1,5·10⁻³ = 0,45 Wb.",
   "Từ thông qua cuộn nhiều vòng", K),

mc("Một cuộn dây 250 vòng, điện trở 5,0 Ω, diện tích mỗi vòng 40 cm², đặt vuông góc với từ trường "
   "đều. Cảm ứng từ giảm đều từ 0,80 T về 0 trong 0,50 s. Cường độ dòng cảm ứng bằng",
   ["0,20 A.", "0,32 A.", "0,50 A.", "0,80 A."],
   "B",
   "|ΔΦ| mỗi vòng = 0,80 · 4,0·10⁻³ = 3,2·10⁻³ Wb.\n"
   "|e| = 250 · 3,2·10⁻³/0,50 = 250 · 6,4·10⁻³ = 1,60 V.\n"
   "i = 1,60/5,0 = 0,32 A.",
   "Định luật Faraday", K),

mc("Một máy phát điện xoay chiều có khung 400 vòng, diện tích mỗi vòng 50 cm², từ trường "
   "B = 0,25 T, quay 1500 vòng/phút. Suất điện động cực đại xấp xỉ",
   ["39,3 V.", "78,5 V.", "157,1 V.", "19,6 V."],
   "B",
   "n = 1500/60 = 25 vòng/giây ⇒ ω = 2π·25 ≈ 157,08 rad/s.\n"
   "E₀ = ω·N·B·S = 157,08 · 400 · 0,25 · 5,0·10⁻³ = 157,08 · 0,50 ≈ 78,5 V.",
   "Máy phát điện xoay chiều", K),

mc("Một máy biến áp lí tưởng có tỉ số vòng dây sơ cấp trên thứ cấp bằng 12. Nếu điện áp thứ cấp "
   "là 18 V thì điện áp sơ cấp bằng",
   ["108 V.", "216 V.", "1,5 V.", "150 V."],
   "B",
   "U₁ = U₂ · N₁/N₂ = 18 · 12 = 216 V.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Hạt nhân ²⁷₁₃Al có khối lượng 26,9744 u. Cho m(p) = 1,0073; m(n) = 1,0087 u. "
   "Độ hụt khối của hạt nhân này xấp xỉ",
   ["0,1548 u.", "0,2423 u.", "0,3286 u.", "0,0679 u."],
   "B",
   "Số nơtron: 27 − 13 = 14.\n"
   "Tổng khối lượng các nuclêôn riêng lẻ:\n"
   "13 · 1,0073 + 14 · 1,0087 = 13,0949 + 14,1218 = 27,2167 u.\n"
   "Δm = 27,2167 − 26,9744 = 0,2423 u.",
   "Độ hụt khối", K),

mc("Một chất phóng xạ có chu kì bán rã 16 ngày. Sau bao lâu thì độ phóng xạ còn 45 % giá trị "
   "ban đầu (ln2 ≈ 0,693)?",
   ["12,4 ngày.", "18,4 ngày.", "24,0 ngày.", "9,2 ngày."],
   "B",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,45 ⇒ n = ln(1/0,45)/ln2 = 0,7985/0,693 ≈ 1,152.\n"
   "t = 1,152 · 16 ≈ 18,4 ngày.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Cho phản ứng ²³₁₁Na + ¹₁H → ²⁰₁₀Ne + ⁴₂He với m(Na) = 22,9837; m(H) = 1,0073; m(Ne) = 19,9869; "
   "m(He) = 4,0015 u. Năng lượng toả ra xấp xỉ",
   ["1,2 MeV.", "2,4 MeV.", "3,6 MeV.", "4,8 MeV."],
   "B",
   "Trước: 22,9837 + 1,0073 = 23,9910 u.  Sau: 19,9869 + 4,0015 = 23,9884 u.\n"
   "Δm = 23,9910 − 23,9884 = 0,0026 u.\n"
   "ΔE = 0,0026 · 931,5 ≈ 2,4 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

mc("Một nguồn phóng xạ gây liều 24 mSv/giờ ở khoảng cách 1,0 m. Muốn liều chỉ còn 1,5 mSv/giờ "
   "thì phải đứng cách nguồn",
   ["2,0 m.", "4,0 m.", "8,0 m.", "16,0 m."],
   "B",
   "Liều tỉ lệ nghịch với bình phương khoảng cách: 24/1,5 = 16 lần.\n"
   "Khoảng cách tăng √16 = 4 lần ⇒ d = 4,0 m.",
   "An toàn bức xạ", K, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Một mẫu chất phóng xạ có chu kì bán rã T. Tỉ số giữa số hạt nhân phân rã trong chu kì thứ nhất "
   "và trong chu kì thứ ba bằng",
   ["2.", "4.", "8.", "3."],
   "B",
   "Chu kì 1: N₀ − N₀/2 = N₀/2.\n"
   "Chu kì 3: N₀/4 − N₀/8 = N₀/8.\n"
   "Tỉ số: (N₀/2)/(N₀/8) = 4.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Trong phản ứng phân hạch dây chuyền, khối lượng tới hạn là",
   ["khối lượng lớn nhất cho phép của nhiên liệu.",
    "khối lượng tối thiểu để phản ứng dây chuyền tự duy trì.",
    "khối lượng của một hạt nhân urani.",
    "khối lượng của các mảnh vỡ."],
   "B",
   "Nếu khối nhiên liệu quá nhỏ, phần lớn nơtron thoát ra ngoài trước khi kịp gây phân hạch mới, "
   "nên k < 1 và phản ứng tắt. Khối lượng tới hạn là giá trị tối thiểu để k đạt 1.",
   "Phản ứng dây chuyền", TB, fig="h_sd_phan_hach", cap="Phản ứng dây chuyền"),

mc("Trong ba loại bức xạ α, β, γ, loại nào cần lớp che chắn dày nhất để giảm cường độ đáng kể?",
   ["Tia α.", "Tia γ.", "Tia β.", "Cả ba như nhau."],
   "B",
   "Tia γ có khả năng đâm xuyên lớn nhất nên cần lớp chì hoặc bê tông dày. "
   "Tia α bị tờ giấy chặn, tia β bị lá nhôm vài milimét chặn.",
   "Khả năng đâm xuyên", TB, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),

mc("Nội năng của một lượng khí lí tưởng thay đổi khi",
   ["thể tích thay đổi mà nhiệt độ giữ nguyên.", "nhiệt độ thay đổi.",
    "áp suất thay đổi mà nhiệt độ giữ nguyên.", "hình dạng bình chứa thay đổi."],
   "B",
   "Với khí lí tưởng, nội năng chỉ phụ thuộc nhiệt độ. Thay đổi thể tích hay áp suất mà giữ "
   "nhiệt độ không đổi thì nội năng không đổi.",
   "Nội năng của khí lí tưởng", TB),
],
P2=[
ds("Thả 0,30 kg nước đá ở −5,0 °C vào 1,0 kg nước ở 35 °C trong bình cách nhiệt. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   [("Nhiệt cần để đưa nước đá lên 0 °C là 3150 J.", True,
     "Đúng. Q = 0,30 · 2100 · 5,0 = 3150 J."),
    ("Nhiệt cần để làm tan hết nước đá là 102 kJ.", True,
     "Đúng. Q = 0,30 · 3,4·10⁵ = 102 000 J."),
    ("Nhiệt tối đa mà nước nhả ra khi hạ về 0 °C là 147 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 35 = 147 000 J."),
    ("Nước đá chỉ tan một phần nên nhiệt độ cân bằng là 0 °C.", False,
     "Sai. Tổng nhiệt cần là 3150 + 102 000 = 105 150 J, nhỏ hơn 147 000 J nên đá TAN HẾT "
     "và nhiệt độ cân bằng cao hơn 0 °C.")],
   "Biện luận điều kiện", K),

ds("Một khối khí lí tưởng thực hiện chu trình: (1)→(2) đẳng nhiệt giãn từ 2,0 L lên 6,0 L; "
   "(2)→(3) đẳng tích hạ áp suất; (3)→(1) đẳng áp nén về trạng thái đầu. "
   "Trạng thái (1) có p = 3,0·10⁵ Pa, T = 300 K.",
   [("Áp suất ở trạng thái (2) bằng 1,0·10⁵ Pa.", True,
     "Đúng. Đẳng nhiệt: p₂ = 3,0·10⁵ · 2,0/6,0 = 1,0·10⁵ Pa."),
    ("Nhiệt độ ở trạng thái (2) vẫn là 300 K.", True,
     "Đúng. Quá trình (1)→(2) là đẳng nhiệt."),
    ("Ở trạng thái (3), thể tích vẫn là 6,0 L.", True,
     "Đúng. Quá trình (2)→(3) là đẳng tích."),
    ("Sau khi đi hết chu trình, nội năng của khí tăng lên.", False,
     "Sai. Nội năng là hàm trạng thái; chu trình kín đưa khí về đúng trạng thái đầu nên ΔU = 0.")],
   "Chu trình kín", K, fig="k_dt_chutrinh", cap="Chu trình trong hệ (p, V)"),

ds("Một thanh dẫn khối lượng 150 g, dài 40 cm trượt không ma sát trên hai ray nghiêng 30° trong "
   "từ trường đều B = 0,50 T vuông góc mặt phẳng nghiêng, điện trở toàn mạch 0,40 Ω. "
   "Lấy g = 10 m/s².",
   [("Thành phần trọng lực dọc mặt nghiêng là 0,75 N.", True,
     "Đúng. m·g·sin30° = 0,150 · 10 · 0,50 = 0,75 N."),
    ("Lực từ cản ở tốc độ v có độ lớn 0,10·v (đơn vị SI).", True,
     "Đúng. F = B²ℓ²v/R = (0,25 · 0,16/0,40)·v = 0,10v."),
    ("Tốc độ lớn nhất của thanh là 7,5 m/s.", True,
     "Đúng. 0,10·v = 0,75 ⇒ v = 7,5 m/s."),
    ("Khi thanh đạt tốc độ lớn nhất, công suất toả nhiệt bằng 0.", False,
     "Sai. Lúc đó dòng cảm ứng đạt giá trị lớn nhất nên công suất toả nhiệt cũng lớn nhất: "
     "P = F·v = 0,75 · 7,5 = 5,625 W.")],
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng", cap="Thanh dẫn trên ray nghiêng"),

ds("Hạt nhân ²³⁵₉₂U biến thành hạt nhân bền ²⁰⁷₈₂Pb qua chuỗi phân rã α và β⁻.",
   [("Chuỗi gồm 7 lần phân rã α.", True,
     "Đúng. (235 − 207)/4 = 7 lần."),
    ("Chuỗi gồm 4 lần phân rã β⁻.", True,
     "Đúng. Sau 7 lần α, Z = 92 − 14 = 78; cần thêm 4 để đạt 82."),
    ("Tổng cộng có 11 hạt được phát ra (không kể bức xạ γ).", True,
     "Đúng. 7 hạt α và 4 hạt β⁻."),
    ("Trong chuỗi này, số nơtron giảm 14 đơn vị.", False,
     "Sai. Số nơtron ban đầu 143, cuối cùng 125, nên giảm 18 đơn vị chứ không phải 14.")],
   "Chuỗi phân rã", K),
],
P3=[
sa("Một bếp có hiệu suất 65 % dùng để đun 2,4 kg nước từ 28 °C tới 88 °C. Nhiệt lượng mà bếp phải "
   "toả ra bằng bao nhiêu kilôjun (làm tròn đến chữ số thập phân thứ nhất)?",
   "930,5",
   "Nhiệt lượng có ích: Q(ci) = 2,4 · 4200 · 60 = 604 800 J = 604,8 kJ.\n"
   "Nhiệt lượng toàn phần bếp phải toả ra: Q(tp) = Q(ci)/H = 604,8/0,65 ≈ 930,5 kJ.",
   "Hiệu suất đun nóng", K),

sa("Một xi lanh nằm ngang chia đôi bằng pit-tông mỏng, mỗi phần dài 60 cm chứa cùng loại khí ở cùng "
   "áp suất, cùng nhiệt độ T. Nung phần trái lên 2T, giữ phần phải ở T. "
   "Pit-tông dịch chuyển bao nhiêu centimét?",
   "20",
   "Đặt x là độ dịch về phía phải.\n"
   "Phần phải (đẳng nhiệt): p·60 = p'·(60 − x).\n"
   "Phần trái: p·60/T = p'·(60 + x)/(2T) ⇒ p·120 = p'·(60 + x).\n"
   "Chia hai phương trình: 2 = (60 + x)/(60 − x) ⇒ 120 − 2x = 60 + x ⇒ 3x = 60 ⇒ x = 20 cm.",
   "Xi lanh hai ngăn", RK),

sa("Một cuộn dây 200 vòng, điện trở 2,0 Ω, diện tích mỗi vòng 50 cm², đặt vuông góc với từ trường "
   "đều. Cảm ứng từ giảm đều 0,40 T. Điện lượng chuyển qua tiết diện dây bằng bao nhiêu culông "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,20",
   "|ΔΦ| mỗi vòng = ΔB·S = 0,40 · 5,0·10⁻³ = 2,0·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 200 · 2,0·10⁻³/2,0 = 0,40/2,0 = 0,20 C.",
   "Điện lượng cảm ứng", K),

sa("Một khung dây hình vuông cạnh 20 cm, khối lượng 50 g, điện trở 0,25 Ω rơi thẳng đứng đi ra khỏi "
   "vùng từ trường đều B = 0,50 T. Tốc độ giới hạn của khung bằng bao nhiêu mét trên giây? "
   "Lấy g = 10 m/s².",
   "12,5",
   "Ở tốc độ giới hạn: B²a²v/R = m·g.\n"
   "v = m·g·R/(B²a²) = 0,050 · 10 · 0,25/(0,25 · 0,040) = 0,125/0,010 = 12,5 m/s.",
   "Tốc độ giới hạn của khung rơi", K),

sa("Một mẫu gỗ cổ còn 35 % lượng ¹⁴C so với gỗ tươi. Tuổi mẫu gỗ bằng bao nhiêu năm "
   "(làm tròn đến hàng đơn vị)? Cho chu kì bán rã của ¹⁴C là 5730 năm; ln2 ≈ 0,693.",
   "8680",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,35 ⇒ n = ln(1/0,35)/ln2 = 1,0498/0,693 ≈ 1,5148.\n"
   "t = 1,5148 · 5730 ≈ 8680 năm.",
   "Xác định tuổi bằng cacbon-14", K),

sa("Một hạt nhân ²²⁶₈₈Ra đứng yên phóng xạ α, hạt α có động năng 4,78 MeV. Năng lượng toả ra của "
   "phản ứng bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)? "
   "Coi khối lượng tỉ lệ số khối.",
   "4,87",
   "Hạt nhân con là ²²²₈₆Rn.\n"
   "W(α)/ΔE = A(con)/(A(α) + A(con)) = 222/226.\n"
   "ΔE = 4,78 · 226/222 ≈ 4,866 ≈ 4,87 MeV.",
   "Bảo toàn động lượng trong phân rã", RK),
])


# =====================================================================  ĐỀ 24
DE24 = dict(
ma="TH-Đề 24", ten="ĐỀ THI THỬ SỐ 24", muc="Khó",
trongtam="Bài toán nhiều dữ kiện, định luật Lenz nâng cao và năng lượng hạt nhân",
P1=[
mc("Muốn làm bay hơi hoàn toàn 0,30 kg nước ở 100 °C cần nhiệt lượng lớn hơn nhiệt lượng đun "
   "0,30 kg nước từ 0 °C lên 100 °C khoảng",
   ["2,4 lần.", "5,4 lần.", "10,8 lần.", "1,8 lần."],
   "B",
   "Nhiệt hoá hơi: Q₁ = 0,30 · 2,26·10⁶ = 678 000 J.\n"
   "Nhiệt đun nóng: Q₂ = 0,30 · 4200 · 100 = 126 000 J.\n"
   "Tỉ số: 678 000/126 000 ≈ 5,4 lần.",
   "Nhiệt hoá hơi riêng", K),

mc("Trộn 1,0 kg nước ở 90 °C với m kg nước ở 20 °C được hỗn hợp 40 °C. Giá trị của m bằng",
   ["1,75 kg.", "2,50 kg.", "3,50 kg.", "1,25 kg."],
   "B",
   "1,0·(90 − 40) = m·(40 − 20) ⇒ 50 = 20m ⇒ m = 2,50 kg.",
   "Phương trình cân bằng nhiệt", K),

mc("Một khối khí nhận nhiệt lượng 800 J và sinh công 500 J. Nội năng của khí",
   ["giảm 300 J.", "tăng 300 J.", "tăng 1300 J.", "không đổi."],
   "B",
   "Khí THU nhiệt: Q = +800 J; khí SINH công: A = −500 J.\n"
   "ΔU = A + Q = −500 + 800 = +300 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Một bình kín chứa khí ở 17 °C, áp suất 1,0·10⁵ Pa. Nung nóng tới nhiệt độ nào thì áp suất "
   "đạt 1,5·10⁵ Pa?",
   ["25,5 °C.", "162 °C.", "435 °C.", "290 °C."],
   "B",
   "T₁ = 17 + 273 = 290 K.\n"
   "Đẳng tích: T₂ = T₁ · p₂/p₁ = 290 · 1,5 = 435 K.\n"
   "t₂ = 435 − 273 = 162 °C.",
   "Định luật Gay-Lussac", K),

mc("Một bình kín chứa 0,10 mol hêli và 0,20 mol argon ở 27 °C, thể tích 2,493 L. "
   "Áp suất hỗn hợp bằng (R = 8,31 J/(mol·K))",
   ["1,5·10⁵ Pa.", "3,0·10⁵ Pa.", "4,5·10⁵ Pa.", "2,0·10⁵ Pa."],
   "B",
   "Tổng số mol: 0,10 + 0,20 = 0,30 mol.\n"
   "p = nRT/V = 0,30 · 8,31 · 300/(2,493·10⁻³) = 747,9/2,493·10⁻³ = 3,0·10⁵ Pa.",
   "Hỗn hợp khí lí tưởng", K),

mc("Khi khí lí tưởng giãn nở vào chân không (bình cách nhiệt), nhiệt độ khí",
   ["tăng.", "không đổi.", "giảm.", "giảm rồi tăng."],
   "B",
   "Giãn vào chân không nên khí không thực hiện công (A = 0); bình cách nhiệt nên Q = 0. "
   "Vậy ΔU = 0, mà nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên nhiệt độ không đổi.",
   "Giãn khí vào chân không", RK),

mc("Đưa cực Nam của một nam châm lại gần một vòng dây kín. Nhìn từ phía nam châm, dòng điện cảm ứng "
   "trong vòng dây có chiều",
   ["ngược chiều kim đồng hồ.", "cùng chiều kim đồng hồ.",
    "bằng không.", "lúc đầu thuận rồi nghịch."],
   "B",
   "Cực Nam lại gần nên từ thông hướng RA XA người quan sát và đang tăng. Theo định luật Lenz, "
   "dòng cảm ứng phải sinh từ trường hướng về phía người quan sát, tức chạy cùng chiều kim đồng hồ "
   "khi nhìn từ phía nam châm.",
   "Định luật Lenz – xác định chiều", K, fig="t_sd_lenz", cap="Chiều dòng điện cảm ứng"),

mc("Một vòng dây kín điện trở 0,40 Ω. Từ thông qua vòng dây giảm đều 0,32 Wb trong 0,80 s. "
   "Điện lượng chuyển qua tiết diện dây bằng",
   ["0,40 C.", "0,80 C.", "1,00 C.", "0,32 C."],
   "B",
   "q = |ΔΦ|/R = 0,32/0,40 = 0,80 C. Điện lượng không phụ thuộc thời gian biến thiên.",
   "Điện lượng cảm ứng", K),

mc("Một thanh dẫn khối lượng 250 g, dài 50 cm nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,50 T. Truyền cho thanh vận tốc 4,0 m/s. Tổng điện lượng qua mạch "
   "cho tới khi thanh dừng bằng",
   ["2,0 C.", "4,0 C.", "8,0 C.", "1,0 C."],
   "B",
   "B·ℓ·q = m·v₀ ⇒ q = 0,250 · 4,0/(0,50 · 0,50) = 1,0/0,25 = 4,0 C.",
   "Xung lượng của lực từ", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một máy biến áp có cuộn sơ cấp 2000 vòng, cuộn thứ cấp thiết kế 500 vòng nhưng bị quấn ngược "
   "25 vòng. Đặt vào sơ cấp 200 V thì điện áp thứ cấp đo được bằng",
   ["50,0 V.", "45,0 V.", "47,5 V.", "42,5 V."],
   "B",
   "Số vòng có hiệu lực: 500 − 2·25 = 450 vòng.\n"
   "U₂ = 200 · 450/2000 = 200 · 0,225 = 45,0 V.",
   "Máy biến áp – quấn ngược", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một nhà máy truyền công suất không đổi. Ở điện áp U hiệu suất 90 %, cấp điện cho 9000 hộ dân. "
   "Nếu tăng điện áp lên 3U thì số hộ được cấp điện là",
   ["9500 hộ.", "9889 hộ.", "10 000 hộ.", "9700 hộ."],
   "B",
   "Hao phí ban đầu 10 %. Tăng U gấp 3 lần ⇒ hao phí giảm 9 lần, còn 10/9 ≈ 1,111 %.\n"
   "Công suất tới nơi tiêu thụ tăng từ 90 % lên 98,889 %.\n"
   "Số hộ: 9000 · 98,889/90 ≈ 9889 hộ.",
   "Truyền tải điện năng – bài toán thực tiễn", RK, fig="t_sd_truyen_tai",
   cap="Truyền tải điện năng"),

mc("Hạt nhân A có ε = 8,2 MeV/nuclêôn, số khối 60; hạt nhân B có ε = 7,9 MeV/nuclêôn, số khối 120. "
   "So sánh năng lượng liên kết và độ bền vững:",
   ["A có W(lk) lớn hơn và bền hơn.", "B có W(lk) lớn hơn nhưng A bền hơn.",
    "A có W(lk) lớn hơn nhưng B bền hơn.", "Hai hạt nhân như nhau."],
   "B",
   "W(lk) của A = 8,2 · 60 = 492 MeV; của B = 7,9 · 120 = 948 MeV nên B có W(lk) lớn hơn.\n"
   "Nhưng độ bền vững đo bằng ε: A có 8,2 > 7,9 nên A bền vững hơn.",
   "So sánh độ bền vững", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chứa hai đồng vị X (T = 4,0 giờ) và Y (T = 8,0 giờ), ban đầu số hạt nhân bằng nhau. "
   "Sau 8,0 giờ, tỉ số số hạt nhân X trên Y bằng",
   ["1 : 1.", "1 : 2.", "1 : 4.", "2 : 1."],
   "B",
   "X trải qua 2 chu kì nên còn N₀/4; Y trải qua 1 chu kì nên còn N₀/2.\n"
   "Tỉ số: (N₀/4)/(N₀/2) = 1 : 2.",
   "Hỗn hợp hai đồng vị", K),

mc("Một nguồn phóng xạ có độ phóng xạ 2,0·10¹³ Bq, mỗi phân rã toả 0,80 MeV. "
   "Công suất của nguồn bằng (1 MeV = 1,6·10⁻¹³ J)",
   ["1,28 W.", "2,56 W.", "5,12 W.", "0,64 W."],
   "B",
   "P = H · E = 2,0·10¹³ · 0,80 · 1,6·10⁻¹³ = 2,0·10¹³ · 1,28·10⁻¹³ = 2,56 W.",
   "Công suất của nguồn phóng xạ", K),

mc("Khi đi qua một từ trường đều, tia nào trong ba tia α, β⁻, γ KHÔNG bị lệch?",
   ["Tia α.", "Tia γ.", "Tia β⁻.", "Cả ba tia."],
   "B",
   "Tia γ là sóng điện từ, không mang điện nên không chịu lực từ. Hai tia còn lại mang điện nên "
   "chuyển động tròn hoặc cong trong từ trường.",
   "Ba loại tia phóng xạ", TB, fig="h_sd_tia_phongxa", cap="Ba loại tia phóng xạ"),

mc("Một chất phóng xạ có chu kì bán rã 2,5 giờ. Sau bao lâu thì tỉ số giữa số hạt nhân con và "
   "số hạt nhân mẹ còn lại bằng 15?",
   ["7,5 giờ.", "10,0 giờ.", "12,5 giờ.", "5,0 giờ."],
   "B",
   "2ⁿ − 1 = 15 ⇒ 2ⁿ = 16 ⇒ n = 4 chu kì.\n"
   "t = 4 · 2,5 = 10,0 giờ.",
   "Tỉ số hạt nhân con và mẹ", K),

mc("Trong lò phản ứng hạt nhân, việc dùng nước nặng thay nước thường làm chất làm chậm có ưu điểm",
   ["làm chậm nơtron nhanh hơn.", "hấp thụ nơtron ít hơn nên tiết kiệm nơtron.",
    "giá thành rẻ hơn.", "không cần thanh điều khiển."],
   "B",
   "Nước nặng (D₂O) hấp thụ nơtron ít hơn nước thường rất nhiều, nhờ đó lò có thể chạy bằng "
   "urani tự nhiên không cần làm giàu. Bù lại nước nặng đắt hơn nhiều.",
   "Lò phản ứng hạt nhân", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Điều nào sau đây KHÔNG đúng với hiện tượng cảm ứng điện từ?",
   ["Dòng cảm ứng luôn chống lại nguyên nhân sinh ra nó.",
    "Suất điện động cảm ứng phụ thuộc điện trở của mạch.",
    "Suất điện động cảm ứng tỉ lệ với tốc độ biến thiên từ thông.",
    "Điện lượng cảm ứng không phụ thuộc thời gian biến thiên."],
   "B",
   "Suất điện động cảm ứng chỉ phụ thuộc tốc độ biến thiên từ thông và số vòng dây; "
   "điện trở chỉ ảnh hưởng tới CƯỜNG ĐỘ dòng điện. Ba phát biểu còn lại đều đúng.",
   "Cảm ứng điện từ – nhận định", K),
],
P2=[
ds("Một bếp điện công suất 2,5 kW, hiệu suất 75 %, dùng đun 4,0 kg nước từ 20 °C. "
   "Cho c(nước) = 4200 J/(kg·K); L = 2,26·10⁶ J/kg.",
   [("Công suất nhiệt có ích là 1875 W.", True,
     "Đúng. 2500 · 0,75 = 1875 W."),
    ("Nhiệt lượng cần để nước sôi là 1344 kJ.", True,
     "Đúng. Q = 4,0 · 4200 · 80 = 1 344 000 J."),
    ("Thời gian để nước sôi xấp xỉ 717 giây.", True,
     "Đúng. t = 1 344 000/1875 ≈ 717 s."),
    ("Để 1,0 kg nước hoá hơi tiếp cần thêm khoảng 600 giây.", False,
     "Sai. Q(ci) = 1,0 · 2,26·10⁶ = 2 260 000 J ⇒ t = 2 260 000/1875 ≈ 1205 s, "
     "tức khoảng 20 phút chứ không phải 10 phút.")],
   "Hiệu suất và chuyển thể", K),

ds("Một bình kín thể tích 2,493 L chứa 0,10 mol khí hêli và 0,20 mol khí argon ở 27 °C. "
   "Cho R = 8,31 J/(mol·K).",
   [("Tổng số mol khí trong bình là 0,30 mol.", True,
     "Đúng. 0,10 + 0,20 = 0,30 mol."),
    ("Áp suất của hỗn hợp bằng 3,0·10⁵ Pa.", True,
     "Đúng. p = nRT/V = 0,30 · 8,31 · 300/(2,493·10⁻³) = 3,0·10⁵ Pa."),
    ("Áp suất riêng phần của hêli bằng 1,0·10⁵ Pa.", True,
     "Đúng. Tỉ lệ với số mol: 3,0·10⁵ · 0,10/0,30 = 1,0·10⁵ Pa."),
    ("Vì argon nặng hơn hêli nên nó gây áp suất riêng phần lớn hơn gấp mười lần.", False,
     "Sai. Áp suất riêng phần chỉ phụ thuộc SỐ MOL, không phụ thuộc khối lượng phân tử. "
     "Argon có số mol gấp đôi nên áp suất riêng phần chỉ gấp đôi: 2,0·10⁵ Pa.")],
   "Hỗn hợp khí lí tưởng", K),

ds("Một khung dây vuông cạnh 30 cm, khối lượng 60 g, điện trở 0,30 Ω rơi thẳng đứng đi ra khỏi "
   "vùng từ trường đều B = 0,40 T nằm ngang. Lấy g = 10 m/s².",
   [("Lực từ cản ở tốc độ v có độ lớn 0,048·v (đơn vị SI).", True,
     "Đúng. F = B²a²v/R = (0,16 · 0,090/0,30)·v = 0,048v."),
    ("Tốc độ giới hạn của khung là 12,5 m/s.", True,
     "Đúng. 0,048·v = m·g = 0,060 · 10 = 0,60 N ⇒ v = 12,5 m/s."),
    ("Trước khi đạt tốc độ giới hạn, khung chuyển động nhanh dần với gia tốc giảm dần.", True,
     "Đúng. Tốc độ tăng làm lực cản tăng nên hợp lực và gia tốc giảm dần."),
    ("Khi đạt tốc độ giới hạn, khung vẫn tiếp tục tăng tốc chậm.", False,
     "Sai. Lúc đó hợp lực bằng 0 nên khung chuyển động THẲNG ĐỀU.")],
   "Tốc độ giới hạn của khung rơi", K),

ds("Một mẫu chứa hai đồng vị phóng xạ độc lập X (chu kì bán rã 4,0 giờ) và Y (chu kì bán rã "
   "8,0 giờ), ban đầu số hạt nhân bằng nhau và bằng N₀.",
   [("Sau 8,0 giờ, số hạt nhân X còn lại là N₀/4.", True,
     "Đúng. X trải qua 2 chu kì."),
    ("Sau 8,0 giờ, số hạt nhân Y còn lại là N₀/2.", True,
     "Đúng. Y trải qua đúng 1 chu kì."),
    ("Sau 8,0 giờ, tổng số hạt nhân còn lại bằng 3N₀/4.", True,
     "Đúng. N₀/4 + N₀/2 = 3N₀/4, so với tổng ban đầu 2N₀ thì chiếm 37,5 %."),
    ("Sau 16 giờ, số hạt nhân của hai đồng vị bằng nhau.", False,
     "Sai. Sau 16 giờ: X còn N₀/16, Y còn N₀/4. Hai số này khác nhau 4 lần. "
     "Vì hai đồng vị bắt đầu với cùng số hạt nhưng chu kì khác nhau nên chúng không bao giờ "
     "bằng nhau trở lại.")],
   "Hỗn hợp hai đồng vị", K),
],
P3=[
sa("Tính nhiệt lượng cần để biến 0,60 kg nước đá ở −8,0 °C thành nước ở 25 °C, kết quả bằng kilôjun "
   "(làm tròn đến chữ số thập phân thứ nhất). Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); "
   "λ = 3,4·10⁵ J/kg.",
   "277,1",
   "Giai đoạn 1: 0,60 · 2100 · 8,0 = 10 080 J.\n"
   "Giai đoạn 2: 0,60 · 3,4·10⁵ = 204 000 J.\n"
   "Giai đoạn 3: 0,60 · 4200 · 25 = 63 000 J.\n"
   "Tổng: 10 080 + 204 000 + 63 000 = 277 080 J ≈ 277,1 kJ.",
   "Bài toán nhiều giai đoạn", K),

sa("Một bình 4,155 L chứa 0,25 mol khí lí tưởng ở 27 °C. Áp suất khí trong bình bằng bao nhiêu "
   "(viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho R = 8,31 J/(mol·K).",
   "1,5",
   "p = nRT/V = 0,25 · 8,31 · 300/(4,155·10⁻³) = 623,25/4,155·10⁻³ = 1,5·10⁵ Pa.",
   "Phương trình Clapeyron", K),

sa("Một đoạn dây dẫn dài 25 cm, khối lượng 40 g được treo nằm ngang bằng hai sợi dây mảnh trong "
   "từ trường đều nằm ngang vuông góc với đoạn dây, B = 0,40 T. Cho dòng điện 5,0 A theo chiều làm "
   "lực từ hướng xuống. Lực căng tổng cộng của hai sợi dây bằng bao nhiêu niutơn?",
   "0,9",
   "Trọng lực: P = 0,040 · 10 = 0,40 N.\n"
   "Lực từ hướng xuống: F = 0,40 · 5,0 · 0,25 = 0,50 N.\n"
   "T = P + F = 0,40 + 0,50 = 0,90 N.",
   "Cân bằng lực có lực từ", K),

sa("Truyền công suất 5,0 MW ở điện áp 25 kV trên đường dây có điện trở 10 Ω. "
   "Công suất hao phí bằng bao nhiêu kilôoát?",
   "400",
   "I = P/U = 5,0·10⁶/(25·10³) = 200 A.\n"
   "ΔP = R·I² = 10 · 200² = 10 · 4,0·10⁴ = 4,0·10⁵ W = 400 kW.",
   "Hao phí truyền tải", K),

sa("Hạt nhân ²¹⁰₈₄Po phóng xạ α thành ²⁰⁶₈₂Pb với chu kì bán rã 138 ngày. Sau 414 ngày, tỉ số giữa "
   "khối lượng chì và khối lượng pôlôni còn lại bằng bao nhiêu (làm tròn đến chữ số thập phân "
   "thứ hai)?",
   "6,87",
   "Sau 414 ngày = 3 chu kì: Po còn N₀/8; Pb tạo thành 7N₀/8.\n"
   "Tỉ số khối lượng = (7N₀/8 · 206)/(N₀/8 · 210) = 7 · 206/210 = 1442/210 ≈ 6,87.",
   "Tỉ số khối lượng con và mẹ", RK),

sa("Cho phản ứng ⁶₃Li + ¹₀n → ³₁H + ⁴₂He với m(Li) = 6,0151; m(n) = 1,0087; m(³H) = 3,0160; "
   "m(He) = 4,0015 u; 1 u·c² = 931,5 MeV. Năng lượng toả ra bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "5,9",
   "Trước: 6,0151 + 1,0087 = 7,0238 u.  Sau: 3,0160 + 4,0015 = 7,0175 u.\n"
   "Δm = 7,0238 − 7,0175 = 0,0063 u.\n"
   "ΔE = 0,0063 · 931,5 ≈ 5,9 MeV.",
   "Năng lượng phản ứng hạt nhân", K),
])


# =====================================================================  ĐỀ 25
DE25 = dict(
ma="TH-Đề 25", ten="ĐỀ THI THỬ SỐ 25", muc="Khó",
trongtam="Tổng duyệt nhóm Khó, chuẩn bị cho năm đề phân loại cuối cùng",
P1=[
mc("Một khối nước đá 0,80 kg ở 0 °C được đun bằng bếp 500 W. Bỏ qua hao phí, thời gian để đá "
   "tan hết bằng",
   ["272 s.", "544 s.", "816 s.", "136 s."],
   "B",
   "Q = m·λ = 0,80 · 3,4·10⁵ = 272 000 J.\n"
   "t = Q/P = 272 000/500 = 544 s.",
   "Nhiệt nóng chảy riêng", K),

mc("Tiếp tục đun khối nước ở câu trên từ 0 °C tới sôi cần thêm thời gian",
   ["336 s.", "672 s.", "1008 s.", "168 s."],
   "B",
   "Q = 0,80 · 4200 · 100 = 336 000 J.\n"
   "t = 336 000/500 = 672 s.",
   "Nhiệt lượng", K),

mc("Một khối khí lí tưởng bị nén đoạn nhiệt, nhiệt độ tăng từ 300 K lên 375 K và thể tích giảm "
   "còn 60 %. Áp suất khí tăng gấp",
   ["1,25 lần.", "2,08 lần.", "1,67 lần.", "0,75 lần."],
   "B",
   "Phương trình trạng thái đúng cho mọi quá trình của một lượng khí xác định:\n"
   "p₂/p₁ = (V₁/V₂)·(T₂/T₁) = (1/0,60) · (375/300) = 1,667 · 1,25 ≈ 2,08 lần.",
   "Phương trình trạng thái", K),

mc("Một bình 6,0 L chứa khí ở 2,5·10⁵ Pa và 27 °C. Lấy bớt khí ra sao cho áp suất giảm còn "
   "1,5·10⁵ Pa và đồng thời hạ nhiệt độ xuống −23 °C. Phần trăm khối lượng khí đã lấy ra bằng",
   ["40 %.", "28 %.", "60 %.", "20 %."],
   "B",
   "Khối lượng khí tỉ lệ với p/T (thể tích không đổi).\n"
   "Tỉ số còn lại: (1,5/250)/(2,5/300) = (1,5·300)/(2,5·250) = 450/625 = 0,72.\n"
   "Vậy còn 72 %, đã lấy ra 28 %.",
   "Phương trình Clapeyron", RK),

mc("Ở cùng nhiệt độ, tỉ số động năng tịnh tiến trung bình của một phân tử khí ôxi và một phân tử "
   "khí hiđrô bằng",
   ["16.", "1.", "4.", "1/16."],
   "B",
   "W̄ₐ = (3/2)kT chỉ phụ thuộc nhiệt độ, không phụ thuộc loại khí. Ở cùng nhiệt độ, "
   "động năng trung bình của mọi phân tử đều bằng nhau nên tỉ số bằng 1.",
   "Động năng phân tử", K),

mc("Một đoạn dây dẫn dài 40 cm mang dòng điện 6,0 A đặt trong từ trường đều. Khi dây vuông góc "
   "với đường sức, lực từ là 0,72 N. Cảm ứng từ bằng",
   ["0,15 T.", "0,30 T.", "0,60 T.", "0,45 T."],
   "B",
   "B = F/(I·ℓ) = 0,72/(6,0 · 0,40) = 0,72/2,4 = 0,30 T.",
   "Lực từ – bài toán ngược", TB),

mc("Một khung dây 400 vòng, diện tích mỗi vòng 25 cm², quay đều quanh trục vuông góc với từ trường "
   "đều B = 0,60 T. Suất điện động hiệu dụng đo được là 133,3 V. Tần số quay của khung xấp xỉ "
   "(π ≈ 3,1416; √2 ≈ 1,414)",
   ["25 Hz.", "50 Hz.", "60 Hz.", "100 Hz."],
   "B",
   "E₀ = E·√2 = 133,3 · 1,414 ≈ 188,5 V.\n"
   "ω = E₀/(N·B·S) = 188,5/(400 · 0,60 · 2,5·10⁻³) = 188,5/0,60 ≈ 314,2 rad/s.\n"
   "f = ω/(2π) = 314,2/6,283 ≈ 50 Hz.",
   "Máy phát – bài toán ngược", RK),

mc("Một khung dây kín được kéo đều ra khỏi vùng từ trường đều. Nếu tăng gấp đôi cả tốc độ kéo và "
   "cảm ứng từ thì nhiệt lượng toả ra trên khung trong suốt quá trình",
   ["tăng 4 lần.", "tăng 8 lần.", "tăng 2 lần.", "tăng 16 lần."],
   "B",
   "Q = B²a³v/R tỉ lệ với B² và với v.\n"
   "B tăng 2 lần (×4) và v tăng 2 lần (×2) ⇒ Q tăng 8 lần.",
   "Năng lượng trong cảm ứng điện từ", RK),

mc("Một máy biến áp lí tưởng có hai cuộn thứ cấp. Nếu tổng công suất tiêu thụ ở hai cuộn là 440 W "
   "và điện áp sơ cấp là 220 V thì cường độ dòng điện ở cuộn sơ cấp bằng",
   ["1,0 A.", "2,0 A.", "4,0 A.", "0,50 A."],
   "B",
   "Máy lí tưởng nên công suất sơ cấp bằng tổng công suất thứ cấp: P₁ = 440 W.\n"
   "I₁ = 440/220 = 2,0 A.",
   "Máy biến áp nhiều cuộn thứ cấp", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 3,6 MW ở điện áp 36 kV trên đường dây có điện trở 18 Ω. "
   "Hiệu suất truyền tải bằng",
   ["90 %.", "95 %.", "98 %.", "99 %."],
   "B",
   "I = 3,6·10⁶/(36·10³) = 100 A.\n"
   "ΔP = 18 · 10⁴ = 1,8·10⁵ W = 0,18 MW.\n"
   "H = (3,60 − 0,18)/3,60 = 3,42/3,60 = 0,95 = 95 %.",
   "Hiệu suất truyền tải", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Hạt nhân ⁴⁰₂₀Ca có khối lượng 39,9626 u. Cho m(p) = 1,0073; m(n) = 1,0087 u. "
   "Năng lượng liên kết riêng xấp xỉ",
   ["7,6 MeV/nuclêôn.", "8,5 MeV/nuclêôn.",
    "9,2 MeV/nuclêôn.", "6,4 MeV/nuclêôn."],
   "B",
   "Số nơtron: 40 − 20 = 20.\n"
   "Tổng khối lượng nuclêôn: 20 · 1,0073 + 20 · 1,0087 = 20,146 + 20,174 = 40,320 u.\n"
   "Δm = 40,320 − 39,9626 = 0,3574 u.\n"
   "W(lk) = 0,3574 · 931,5 ≈ 332,9 MeV ⇒ ε = 332,9/40 ≈ 8,3 MeV/nuclêôn, "
   "gần nhất với 8,5 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chất phóng xạ nguyên chất có 8,0·10²² hạt nhân, chu kì bán rã 5,0 ngày. "
   "Số hạt nhân phân rã trong 5 ngày đầu tiên bằng",
   ["2,0·10²².", "4,0·10²².", "6,0·10²².", "8,0·10²²."],
   "B",
   "Sau một chu kì, còn lại 4,0·10²² hạt nên đã phân rã 8,0·10²² − 4,0·10²² = 4,0·10²² hạt.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Cho phản ứng ²₁H + ²₁H → ³₂He + ¹₀n toả 3,27 MeV. Nếu hai hạt đơteri tới đứng yên thì "
   "động năng của nơtron xấp xỉ",
   ["0,82 MeV.", "2,45 MeV.", "1,64 MeV.", "3,27 MeV."],
   "B",
   "Hai hạt sinh ra có động lượng cùng độ lớn nên động năng tỉ lệ nghịch với khối lượng.\n"
   "W(n) = ΔE · A(He)/(A(He) + A(n)) = 3,27 · 3/4 ≈ 2,45 MeV.",
   "Bảo toàn động lượng trong phản ứng", RK),

mc("Một chất phóng xạ có chu kì bán rã 30 phút. Nếu ban đầu độ phóng xạ là 6,4·10⁵ Bq thì sau "
   "2,5 giờ độ phóng xạ bằng",
   ["1,0·10⁴ Bq.", "2,0·10⁴ Bq.", "4,0·10⁴ Bq.", "8,0·10⁴ Bq."],
   "B",
   "2,5 giờ = 150 phút ⇒ n = 150/30 = 5 chu kì.\n"
   "H = 6,4·10⁵/2⁵ = 6,4·10⁵/32 = 2,0·10⁴ Bq.",
   "Độ phóng xạ", K),

mc("Trong chuỗi phân rã ²³⁵U → ²⁰⁷Pb, tổng số hạt α và β⁻ phát ra bằng",
   ["9.", "11.", "13.", "7."],
   "B",
   "Số lần α: (235 − 207)/4 = 7.\n"
   "Sau 7 lần α, Z = 92 − 14 = 78; cần thêm 4 lần β⁻ để đạt Z = 82.\n"
   "Tổng: 7 + 4 = 11 hạt.",
   "Chuỗi phân rã", K),

mc("Khi nói về nhiên liệu của phản ứng nhiệt hạch, phát biểu nào ĐÚNG?",
   ["Nhiên liệu là urani làm giàu.",
    "Đơteri có sẵn trong nước biển nên nguồn nhiên liệu gần như vô tận.",
    "Nhiên liệu phải được làm lạnh xuống gần 0 K.",
    "Nhiên liệu là chì và thori."],
   "B",
   "Nhiệt hạch dùng các hạt nhân rất nhẹ, chủ yếu là đơteri và triti. Đơteri chiếm khoảng "
   "một phần 6500 số nguyên tử hiđrô trong nước tự nhiên nên trữ lượng gần như vô hạn.",
   "Nhiệt hạch", TB, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Một mẫu chất phóng xạ có hằng số phóng xạ λ. Sau khoảng thời gian bằng 1/λ, số hạt nhân "
   "còn lại chiếm khoảng",
   ["50 %.", "37 %.", "25 %.", "63 %."],
   "B",
   "N = N₀·e^(−λt) với t = 1/λ cho N = N₀·e⁻¹ ≈ 0,368·N₀, tức khoảng 37 %.\n"
   "Khoảng thời gian 1/λ chính là thời gian sống trung bình của hạt nhân.",
   "Hằng số phóng xạ", RK),

mc("Trong an toàn bức xạ, đại lượng nào phản ánh đúng nhất mức nguy hại sinh học mà một người "
   "phải chịu?",
   ["Độ phóng xạ của nguồn (Bq).", "Liều tương đương (Sv).",
    "Liều hấp thụ (Gy).", "Chu kì bán rã của nguồn."],
   "B",
   "Liều tương đương tính bằng sivơ có nhân thêm hệ số trọng số tuỳ loại bức xạ, phản ánh đúng "
   "mức nguy hại sinh học. Liều hấp thụ (Gy) chỉ tính năng lượng, chưa xét loại tia.",
   "Đơn vị đo bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),
],
P2=[
ds("Một bếp 800 W đun 1,0 kg nước đá ở 0 °C cho tan hết rồi tiếp tục đun tới sôi. Bỏ qua hao phí. "
   "Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng làm tan hết nước đá là 340 kJ.", True,
     "Đúng. Q = 1,0 · 3,4·10⁵ = 340 000 J."),
    ("Thời gian làm tan hết nước đá là 425 giây.", True,
     "Đúng. t = 340 000/800 = 425 s."),
    ("Nhiệt lượng đun nước từ 0 °C tới sôi là 420 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 100 = 420 000 J."),
    ("Thời gian đun nước tới sôi ngắn hơn thời gian làm tan nước đá.", False,
     "Sai. t = 420 000/800 = 525 s, DÀI hơn 425 s. Với nước, nhiệt để đun từ 0 °C tới 100 °C "
     "lớn hơn nhiệt để làm tan hết cùng khối lượng nước đá.")],
   "Bài toán nhiều giai đoạn", K),

ds("Một bình 6,0 L chứa khí lí tưởng ở 2,5·10⁵ Pa và 27 °C. Sau khi lấy bớt khí và hạ nhiệt độ "
   "xuống −23 °C, áp suất còn 1,5·10⁵ Pa.",
   [("Nhiệt độ ban đầu và lúc sau lần lượt là 300 K và 250 K.", True,
     "Đúng. 27 + 273 = 300 K;  −23 + 273 = 250 K."),
    ("Với thể tích không đổi, khối lượng khí tỉ lệ thuận với tỉ số p/T.", True,
     "Đúng. Từ pV = (m/M)RT suy ra m tỉ lệ với p/T khi V không đổi."),
    ("Khối lượng khí còn lại chiếm 72 % khối lượng ban đầu.", True,
     "Đúng. (1,5/250)/(2,5/300) = 450/625 = 0,72."),
    ("Phần khí đã lấy ra chiếm 40 % khối lượng ban đầu.", False,
     "Sai. Đã lấy ra 100 − 72 = 28 %. Giá trị 40 % là kết quả khi chỉ so sánh áp suất mà quên "
     "ảnh hưởng của nhiệt độ.")],
   "Phương trình Clapeyron", RK),

ds("Một khung dây kín được kéo đều ra khỏi vùng từ trường đều với tốc độ v, cảm ứng từ B, "
   "cạnh khung a, điện trở R.",
   [("Suất điện động cảm ứng bằng B·a·v.", True,
     "Đúng. Chỉ cạnh nằm trong từ trường đóng vai trò nguồn."),
    ("Lực kéo cần thiết bằng B²a²v/R.", True,
     "Đúng. Lực kéo cân bằng lực từ cản F = B·i·a với i = B·a·v/R."),
    ("Nhiệt lượng toả ra trong suốt quá trình bằng B²a³v/R.", True,
     "Đúng. Q = F·a = (B²a²v/R)·a = B²a³v/R."),
    ("Nếu tăng gấp đôi tốc độ kéo thì nhiệt lượng toả ra tăng gấp bốn.", False,
     "Sai. Q tỉ lệ THUẬN với v nên chỉ tăng gấp đôi: dòng mạnh gấp đôi nhưng thời gian ngắn "
     "đi một nửa.")],
   "Năng lượng trong cảm ứng điện từ", RK),

ds("Cho phản ứng ²₁H + ²₁H → ³₂He + ¹₀n toả 3,27 MeV, hai hạt tới có động năng không đáng kể.",
   [("Phản ứng bảo toàn số khối: 2 + 2 = 3 + 1.", True,
     "Đúng. Tổng số khối hai vế đều bằng 4."),
    ("Hai hạt sinh ra bay theo hai hướng ngược nhau.", True,
     "Đúng. Tổng động lượng ban đầu coi như bằng 0."),
    ("Động năng của nơtron xấp xỉ 2,45 MeV.", True,
     "Đúng. W(n) = 3,27 · 3/4 ≈ 2,45 MeV."),
    ("Động năng của hạt ³He xấp xỉ 2,45 MeV.", False,
     "Sai. ³He nặng gấp 3 lần nơtron nên chỉ mang 3,27 · 1/4 ≈ 0,82 MeV.")],
   "Bảo toàn động lượng trong phản ứng", RK),
],
P3=[
sa("Một bếp 600 W đun 1,5 kg nước đá ở 0 °C cho tan hết. Bỏ qua hao phí. Thời gian cần thiết bằng "
   "bao nhiêu giây? Cho λ = 3,4·10⁵ J/kg.",
   "850",
   "Q = m·λ = 1,5 · 3,4·10⁵ = 510 000 J.\n"
   "t = Q/P = 510 000/600 = 850 s.",
   "Nhiệt nóng chảy riêng", K),

sa("Một khối khí lí tưởng bị nén làm nhiệt độ tăng từ 300 K lên 450 K và thể tích giảm còn 50 %. "
   "Áp suất khí tăng gấp bao nhiêu lần?",
   "3",
   "p₂/p₁ = (V₁/V₂)·(T₂/T₁) = 2 · (450/300) = 2 · 1,5 = 3 lần.",
   "Phương trình trạng thái", K),

sa("Một khung dây 500 vòng, diện tích mỗi vòng 40 cm², quay đều quanh trục vuông góc với từ trường "
   "đều B = 0,50 T, tần số 20 Hz. Suất điện động hiệu dụng bằng bao nhiêu vôn "
   "(làm tròn đến chữ số thập phân thứ nhất)? Lấy π ≈ 3,1416; √2 ≈ 1,414.",
   "88,9",
   "ω = 2π·20 ≈ 125,66 rad/s;  S = 4,0·10⁻³ m².\n"
   "E₀ = ω·N·B·S = 125,66 · 500 · 0,50 · 4,0·10⁻³ = 125,66 · 1,0 ≈ 125,66 V.\n"
   "E = E₀/√2 = 125,66/1,414 ≈ 88,9 V.",
   "Máy phát điện xoay chiều", K),

sa("Truyền công suất 4,8 MW ở điện áp 48 kV trên đường dây có điện trở 20 Ω. "
   "Hiệu suất truyền tải bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ nhất)?",
   "95,8",
   "I = P/U = 4,8·10⁶/(48·10³) = 100 A.\n"
   "ΔP = 20 · 10⁴ = 2,0·10⁵ W = 0,20 MW.\n"
   "H = (4,80 − 0,20)/4,80 = 4,60/4,80 ≈ 0,9583 = 95,8 %.",
   "Hiệu suất truyền tải", K),

sa("Một mẫu chất phóng xạ có hằng số phóng xạ 2,0·10⁻⁴ s⁻¹. Sau khoảng thời gian bằng 1/λ, "
   "số hạt nhân còn lại chiếm bao nhiêu phần trăm số hạt ban đầu (làm tròn đến hàng đơn vị)? "
   "Lấy e ≈ 2,718.",
   "37",
   "Với t = 1/λ ta có N = N₀·e⁻¹ = N₀/2,718 ≈ 0,368·N₀.\n"
   "Tỉ lệ còn lại ≈ 37 %.",
   "Hằng số phóng xạ", RK),

sa("Một chất phóng xạ có chu kì bán rã 45 phút, độ phóng xạ ban đầu 1,28·10⁶ Bq. "
   "Sau 3,0 giờ, độ phóng xạ bằng bao nhiêu (viết dưới dạng x·10⁴ Bq, chỉ ghi giá trị x)?",
   "8",
   "3,0 giờ = 180 phút ⇒ n = 180/45 = 4 chu kì.\n"
   "H = 1,28·10⁶/2⁴ = 1,28·10⁶/16 = 8,0·10⁴ Bq.",
   "Độ phóng xạ", K),
])


NHOM = dict(
    ten_nhom="ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG  (Đề 21 – 25)",
    mo_ta="Năm đề mức Khó, nhiều câu đòi hỏi biện luận điều kiện trước khi tính toán",
    pham_vi=(
        "Chương I. Vật lí nhiệt  •  Chương II. Khí lí tưởng  •  "
        "Chương III. Từ trường  •  Chương IV. Vật lí hạt nhân\n"
        "Mỗi đề gồm 28 câu / 40 lệnh hỏi, thời gian 50 phút, thang điểm 10.\n"
        "Hằng số: c(nước) = 4200, c(nước đá) = 2100, c(nhôm) = 880, c(đồng) = 380 J/(kg·K); "
        "λ(nước đá) = 3,4·10⁵ J/kg; L(nước) = 2,26·10⁶ J/kg; g = 10 m/s²; R = 8,31 J/(mol·K); "
        "k = 1,38·10⁻²³ J/K; Nₐ = 6,02·10²³ mol⁻¹; 1 u·c² = 931,5 MeV; 1 MeV = 1,6·10⁻¹³ J; "
        "π ≈ 3,1416; √2 ≈ 1,414; ln2 ≈ 0,693; e ≈ 2,718."),
    tests=[DE21, DE22, DE23, DE24, DE25],
)
