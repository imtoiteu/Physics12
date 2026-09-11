# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.  Đề 11 – 15 (Trung bình → Khó)."""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 11
DE11 = dict(
ma="TH-Đề 11", ten="ĐỀ THI THỬ SỐ 11", muc="Trung bình → Khó",
trongtam="Bài toán nhiều giai đoạn, chu trình khí, điện lượng và năng lượng hạt nhân",
P1=[
mc("Tính nhiệt lượng cần để biến 0,30 kg nước đá ở −20 °C thành nước ở 30 °C. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   ["102 kJ.", "152,4 kJ.", "139,8 kJ.", "116,4 kJ."],
   "B",
   "Giai đoạn 1: 0,30 · 2100 · 20 = 12 600 J.\n"
   "Giai đoạn 2: 0,30 · 3,4·10⁵ = 102 000 J.\n"
   "Giai đoạn 3: 0,30 · 4200 · 30 = 37 800 J.\n"
   "Tổng: 12 600 + 102 000 + 37 800 = 152 400 J = 152,4 kJ.",
   "Bài toán nhiều giai đoạn", K),

mc("Một bếp có hiệu suất 70 % cung cấp nhiệt cho quá trình ở câu trên. Nhiệt lượng bếp phải "
   "toả ra xấp xỉ",
   ["106,7 kJ.", "217,7 kJ.", "152,4 kJ.", "304,8 kJ."],
   "B",
   "Q(tp) = Q(ci)/H = 152,4/0,70 ≈ 217,7 kJ. "
   "Nhân với H thay vì chia sẽ ra 106,7 kJ — đó là bẫy quen thuộc.",
   "Hiệu suất đun nóng", K),

mc("Một khối khí lí tưởng thực hiện chu trình gồm: đẳng tích tăng áp suất 3 lần, "
   "rồi đẳng áp tăng thể tích 2 lần, rồi trở về trạng thái đầu. Nếu nhiệt độ ban đầu là 300 K "
   "thì nhiệt độ cao nhất trong chu trình bằng",
   ["900 K.", "1800 K.", "600 K.", "1500 K."],
   "B",
   "Đẳng tích, p tăng 3 lần: T = 300 · 3 = 900 K.\n"
   "Đẳng áp, V tăng 2 lần: T = 900 · 2 = 1800 K — đây là nhiệt độ cao nhất.",
   "Chu trình khí lí tưởng", K, fig="k_dt_chutrinh", cap="Chu trình trong hệ (p, V)"),

mc("Một bình chứa khí ở áp suất 5,0·10⁵ Pa. Mở van cho khí thoát ra tới khi áp suất còn 2,0·10⁵ Pa "
   "ở nhiệt độ không đổi. Phần trăm khối lượng khí đã thoát ra bằng",
   ["40 %.", "60 %.", "25 %.", "75 %."],
   "B",
   "Với V và T không đổi, khối lượng khí trong bình tỉ lệ thuận với áp suất.\n"
   "Còn lại: 2,0/5,0 = 40 % ⇒ đã thoát ra 60 %.",
   "Phương trình Clapeyron", K),

mc("Hai bình giống hệt nhau nối bằng ống nhỏ có khoá, bình A chứa khí ở 3,0·10⁵ Pa, bình B chân "
   "không. Mở khoá cho khí phân bố đều hai bình ở nhiệt độ không đổi. Áp suất chung bằng",
   ["3,0·10⁵ Pa.", "1,5·10⁵ Pa.", "6,0·10⁵ Pa.", "0,75·10⁵ Pa."],
   "B",
   "Lượng khí không đổi, nhiệt độ không đổi, thể tích tăng gấp đôi nên theo định luật Boyle "
   "áp suất giảm một nửa: p = 3,0·10⁵/2 = 1,5·10⁵ Pa.",
   "Định luật Boyle", K),

mc("Áp suất khí trong một bình tăng gấp đôi khi giữ nguyên thể tích và số phân tử. Điều đó chứng tỏ",
   ["mật độ phân tử tăng gấp đôi.", "động năng trung bình của phân tử tăng gấp đôi.",
    "khối lượng phân tử tăng gấp đôi.", "thể tích bình giảm một nửa."],
   "B",
   "Từ p = (2/3)·μ·W̄ₐ, với mật độ μ không đổi thì p tỉ lệ thuận với động năng trung bình, "
   "tức tỉ lệ thuận với nhiệt độ tuyệt đối.",
   "Áp suất theo mô hình động học", K, fig="k_sd_vacham_thanh",
   cap="Va chạm phân tử lên thành bình"),

mc("Một khung dây kín 50 vòng, điện trở 2,0 Ω, diện tích mỗi vòng 80 cm², đặt vuông góc với từ "
   "trường đều. Cảm ứng từ giảm đều 0,50 T. Điện lượng chuyển qua tiết diện dây bằng",
   ["0,050 C.", "0,10 C.", "0,20 C.", "0,40 C."],
   "B",
   "|ΔΦ| mỗi vòng = 0,50 · 8,0·10⁻³ = 4,0·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 50 · 4,0·10⁻³/2,0 = 0,20/2,0 = 0,10 C.",
   "Điện lượng cảm ứng", K),

mc("Một thanh dẫn nằm ngang treo bằng hai lò xo giống nhau trong từ trường đều nằm ngang vuông góc "
   "với thanh. Khi chưa có dòng, mỗi lò xo giãn 5,0 cm; khi có dòng, mỗi lò xo giãn 6,0 cm. "
   "Tỉ số lực từ trên trọng lượng thanh bằng",
   ["0,17.", "0,20.", "0,25.", "0,83."],
   "B",
   "Chưa có dòng: 2k·5,0 = P.  Có dòng: 2k·6,0 = P + F.\n"
   "Lấy hiệu: 2k·1,0 = F ⇒ F/P = 1,0/5,0 = 0,20.",
   "Thanh dẫn treo trên lò xo", K, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),

mc("Một máy biến áp có cuộn sơ cấp 1000 vòng, cuộn thứ cấp thiết kế 250 vòng nhưng bị quấn ngược "
   "20 vòng. Đặt vào sơ cấp 220 V thì điện áp thứ cấp đo được bằng",
   ["55,0 V.", "46,2 V.", "50,6 V.", "44,0 V."],
   "B",
   "Số vòng có hiệu lực: 250 − 2·20 = 210 vòng.\n"
   "U₂ = 220 · 210/1000 = 46,2 V.\n"
   "Nếu quấn đúng thì U₂ = 55,0 V.",
   "Máy biến áp – quấn ngược", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 1,0 MW ở điện áp 10 kV trên đường dây có điện trở 5,0 Ω. "
   "Muốn hiệu suất đạt 98 % thì phải tăng điện áp lên",
   ["15,8 kV.", "12,5 kV.", "20,0 kV.", "25,0 kV."],
   "A",
   "Ở 10 kV: I = 100 A, ΔP = 5,0 · 10⁴ = 50 kW, chiếm 5 % ⇒ hiệu suất 95 %.\n"
   "Muốn hao phí còn 2 %, tức giảm 2,5 lần, thì U phải tăng √2,5 ≈ 1,58 lần: 10 · 1,58 = 15,8 kV.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây quay đều trong từ trường đều tạo suất điện động e = E₀·sin(100πt). "
   "Trong mỗi giây, suất điện động bằng 0 bao nhiêu lần?",
   ["50 lần.", "100 lần.", "150 lần.", "200 lần."],
   "B",
   "Trong mỗi chu kì, sin(ωt) = 0 đúng hai lần. Tần số f = 50 Hz nên trong một giây có "
   "2 · 50 = 100 lần.",
   "Dòng điện xoay chiều", K),

mc("Cho phản ứng ²¹⁰₈₄Po → ⁴₂He + ²⁰⁶₈₂Pb, toả 5,4 MeV. Hạt nhân Po đứng yên. "
   "Động năng của hạt α xấp xỉ (coi khối lượng tỉ lệ số khối)",
   ["0,10 MeV.", "5,30 MeV.", "2,70 MeV.", "5,40 MeV."],
   "B",
   "Bảo toàn động lượng ⇒ động năng tỉ lệ nghịch với khối lượng.\n"
   "W(α) = ΔE · 206/(206 + 4) = 5,4 · 206/210 ≈ 5,30 MeV.",
   "Bảo toàn động lượng trong phân rã", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

mc("Một mẫu chất phóng xạ có chu kì bán rã 10 giờ. Sau bao lâu thì số hạt nhân còn lại 40 % "
   "ban đầu (ln2 ≈ 0,693)?",
   ["8,0 giờ.", "13,2 giờ.", "16,0 giờ.", "20,0 giờ."],
   "B",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,40 ⇒ n = ln(1/0,40)/ln2 = 0,9163/0,693 ≈ 1,322.\n"
   "t = 1,322 · 10 ≈ 13,2 giờ.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Năng lượng toả ra khi phân hạch hoàn toàn 2,0 gam ²³⁵U xấp xỉ (200 MeV mỗi phân hạch)",
   ["8,2·10¹⁰ J.", "1,64·10¹¹ J.", "4,1·10¹⁰ J.", "3,28·10¹¹ J."],
   "B",
   "Số hạt nhân: N = (2,0/235)·6,02·10²³ ≈ 5,12·10²¹.\n"
   "E = 5,12·10²¹ · 200 · 1,6·10⁻¹³ = 5,12·10²¹ · 3,2·10⁻¹¹ ≈ 1,64·10¹¹ J.",
   "Năng lượng của nhiên liệu hạt nhân", K),

mc("Hạt nhân ²³⁸₉₂U biến thành ²⁰⁶₈₂Pb qua chuỗi phân rã α và β⁻. Số lần phân rã α bằng",
   ["6.", "8.", "10.", "4."],
   "B",
   "Chỉ phân rã α làm giảm số khối, mỗi lần 4 đơn vị:\n"
   "số lần α = (238 − 206)/4 = 32/4 = 8 lần.",
   "Chuỗi phân rã", K),

mc("Một nguồn phóng xạ có công suất ban đầu 80 W, chu kì bán rã 12 năm. "
   "Sau 36 năm, công suất còn",
   ["20 W.", "10 W.", "40 W.", "5 W."],
   "B",
   "Công suất tỉ lệ với độ phóng xạ nên cũng giảm theo cùng quy luật:\n"
   "n = 36/12 = 3 ⇒ P = 80/2³ = 10 W.",
   "Công suất nguồn phóng xạ", K),

mc("Trong quá trình đoạn nhiệt, nếu khí giãn nở thì",
   ["nội năng tăng, nhiệt độ tăng.", "nội năng giảm, nhiệt độ giảm.",
    "nội năng không đổi.", "nhiệt độ tăng rồi giảm."],
   "B",
   "Đoạn nhiệt nên Q = 0; khí giãn nở nên SINH công, A < 0. "
   "Từ ΔU = A + Q = A < 0: nội năng giảm, kéo theo nhiệt độ giảm. "
   "Đó là lí do khí xịt ra khỏi bình nén thì rất lạnh.",
   "Quá trình đoạn nhiệt", TB),

mc("Khi từ thông qua một mạch kín tăng đều theo thời gian thì suất điện động cảm ứng trong mạch",
   ["tăng đều theo thời gian.", "có giá trị không đổi.",
    "giảm dần về 0.", "bằng 0."],
   "B",
   "Suất điện động tỉ lệ với TỐC ĐỘ biến thiên của từ thông. Từ thông tăng ĐỀU nghĩa là tốc độ "
   "biến thiên là hằng số, nên suất điện động không đổi.",
   "Định luật Faraday", K, fig="t_dt_phi_e", cap="Từ thông và suất điện động theo thời gian"),
],
P2=[
ds("Cần biến 0,50 kg nước đá ở −15 °C thành hơi nước ở 100 °C. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg; L = 2,26·10⁶ J/kg.",
   [("Nhiệt lượng làm ấm nước đá lên 0 °C là 15,75 kJ.", True,
     "Đúng. Q₁ = 0,50 · 2100 · 15 = 15 750 J."),
    ("Nhiệt lượng làm tan hết nước đá là 170 kJ.", True,
     "Đúng. Q₂ = 0,50 · 3,4·10⁵ = 170 000 J."),
    ("Nhiệt lượng đun nước từ 0 °C lên 100 °C là 210 kJ.", True,
     "Đúng. Q₃ = 0,50 · 4200 · 100 = 210 000 J."),
    ("Tổng nhiệt lượng cần cung cấp nhỏ hơn 1000 kJ.", False,
     "Sai. Còn phải cộng giai đoạn hoá hơi: Q₄ = 0,50 · 2,26·10⁶ = 1 130 000 J. "
     "Tổng cộng ≈ 1525,75 kJ, lớn hơn 1000 kJ rất nhiều — riêng giai đoạn hoá hơi đã chiếm "
     "gần ba phần tư.")],
   "Bài toán nhiều giai đoạn", K),

ds("Hai bình A và B giống hệt nhau nối bằng ống nhỏ có khoá. Bình A chứa khí lí tưởng ở "
   "4,0·10⁵ Pa, bình B là chân không. Nhiệt độ giữ không đổi trong suốt quá trình.",
   [("Khi mở khoá, khí phân bố đều sang cả hai bình.", True,
     "Đúng. Khí luôn chiếm toàn bộ thể tích bình chứa."),
    ("Thể tích mà lượng khí chiếm tăng gấp đôi.", True,
     "Đúng. Từ một bình sang hai bình giống hệt nhau."),
    ("Áp suất chung sau khi mở khoá là 2,0·10⁵ Pa.", True,
     "Đúng. Định luật Boyle: p₂ = p₁·V₁/V₂ = 4,0·10⁵/2 = 2,0·10⁵ Pa."),
    ("Trong quá trình này khí thực hiện công lên môi trường.", False,
     "Sai. Khí giãn vào CHÂN KHÔNG nên không phải đẩy vật gì, không thực hiện công. "
     "Nhiệt độ không đổi nên nội năng cũng không đổi.")],
   "Giãn khí vào chân không", K),

ds("Một khung dây kín 80 vòng, điện trở 4,0 Ω, diện tích mỗi vòng 50 cm², đặt vuông góc với từ "
   "trường đều. Cảm ứng từ giảm đều từ 0,80 T về 0 trong 0,40 s.",
   [("Độ biến thiên từ thông qua mỗi vòng là 4,0·10⁻³ Wb.", True,
     "Đúng. |ΔΦ| = 0,80 · 5,0·10⁻³ = 4,0·10⁻³ Wb."),
    ("Suất điện động cảm ứng bằng 0,80 V.", True,
     "Đúng. |e| = 80 · 4,0·10⁻³/0,40 = 80 · 0,010 = 0,80 V."),
    ("Cường độ dòng điện cảm ứng bằng 0,20 A.", True,
     "Đúng. i = 0,80/4,0 = 0,20 A."),
    ("Điện lượng chuyển qua tiết diện dây bằng 0,20 C.", False,
     "Sai. q = N·|ΔΦ|/R = 80 · 4,0·10⁻³/4,0 = 0,32/4,0 = 0,080 C. "
     "Giá trị 0,20 C là cường độ dòng điện, không phải điện lượng.")],
   "Điện lượng cảm ứng", K),

ds("Hạt nhân ²¹⁰₈₄Po đứng yên phóng xạ α tạo ²⁰⁶₈₂Pb, toả ra 5,4 MeV. "
   "Coi khối lượng tỉ lệ với số khối.",
   [("Hai hạt sinh ra có động lượng cùng độ lớn, ngược hướng.", True,
     "Đúng. Hạt nhân mẹ đứng yên nên tổng động lượng bằng 0 và được bảo toàn."),
    ("Động năng hạt α xấp xỉ 5,30 MeV.", True,
     "Đúng. W(α) = 5,4 · 206/210 ≈ 5,30 MeV."),
    ("Động năng hạt nhân chì xấp xỉ 0,10 MeV.", True,
     "Đúng. W(Pb) = 5,4 − 5,30 = 0,10 MeV, cũng bằng 5,4 · 4/210."),
    ("Hai hạt sinh ra có cùng tốc độ vì cùng độ lớn động lượng.", False,
     "Sai. Cùng động lượng nhưng khối lượng khác nhau nên tốc độ khác nhau: "
     "v(α)/v(Pb) = 206/4 = 51,5.")],
   "Bảo toàn động lượng trong phân rã", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),
],
P3=[
sa("Thả một miếng sắt khối lượng 0,60 kg ở 150 °C vào 1,2 kg nước ở 25 °C trong bình cách nhiệt. "
   "Nhiệt độ cân bằng bằng bao nhiêu độ Celsius (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho c(sắt) = 460, c(nước) = 4200 J/(kg·K).",
   "31,5",
   "0,60·460·(150 − t) = 1,2·4200·(t − 25)\n"
   "276·(150 − t) = 5040·(t − 25) ⇒ 41 400 − 276t = 5040t − 126 000\n"
   "5316t = 167 400 ⇒ t ≈ 31,5 °C.\n"
   "Kiểm tra: 25 < 31,5 < 150 — hợp lí.",
   "Phương trình cân bằng nhiệt", K),

sa("Một bình chứa khí ở áp suất 8,0·10⁵ Pa. Mở van cho khí thoát ra tới khi áp suất còn "
   "3,0·10⁵ Pa ở nhiệt độ không đổi. Phần trăm khối lượng khí đã thoát ra bằng bao nhiêu phần trăm "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "62,5",
   "Với V và T không đổi, khối lượng khí trong bình tỉ lệ thuận với áp suất.\n"
   "Còn lại: 3,0/8,0 = 0,375 = 37,5 % ⇒ đã thoát ra 62,5 %.",
   "Phương trình Clapeyron", K),

sa("Một khung dây kín 120 vòng, điện trở 3,0 Ω, diện tích mỗi vòng 25 cm², đặt vuông góc với từ "
   "trường đều. Cảm ứng từ giảm đều 0,60 T. Điện lượng chuyển qua tiết diện dây bằng bao nhiêu "
   "culông (làm tròn đến chữ số thập phân thứ hai)?",
   "0,06",
   "|ΔΦ| mỗi vòng = 0,60 · 2,5·10⁻³ = 1,5·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 120 · 1,5·10⁻³/3,0 = 0,18/3,0 = 0,060 C.",
   "Điện lượng cảm ứng", K),

sa("Truyền công suất 600 kW ở điện áp 30 kV trên đường dây có điện trở 9,0 Ω. "
   "Công suất hao phí trên đường dây bằng bao nhiêu kilôoát (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "3,6",
   "I = P/U = 600 000/30 000 = 20 A.\n"
   "ΔP = R·I² = 9,0 · 400 = 3600 W = 3,6 kW.",
   "Hao phí truyền tải", TB),

sa("Hạt nhân ²³²₉₀Th biến thành ²⁰⁸₈₂Pb qua chuỗi phân rã. Số lần phân rã β⁻ trong chuỗi bằng "
   "bao nhiêu?",
   "4",
   "Số lần α: (232 − 208)/4 = 6 lần, làm Z giảm 12: 90 − 12 = 78.\n"
   "Muốn đạt Z = 82 phải tăng thêm 4 đơn vị ⇒ 4 lần phân rã β⁻.",
   "Chuỗi phân rã", K),

sa("Một mẫu chất phóng xạ có chu kì bán rã 6,0 giờ. Sau bao nhiêu giờ thì số hạt nhân còn lại "
   "bằng 30 % ban đầu (làm tròn đến chữ số thập phân thứ nhất)? Lấy ln2 ≈ 0,693.",
   "10,4",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,30 ⇒ n = ln(1/0,30)/ln2 = 1,204/0,693 ≈ 1,737.\n"
   "t = 1,737 · 6,0 ≈ 10,4 giờ.",
   "Định luật phóng xạ – dùng logarit", K),
])


# =====================================================================  ĐỀ 12
DE12 = dict(
ma="TH-Đề 12", ten="ĐỀ THI THỬ SỐ 12", muc="Trung bình → Khó",
trongtam="Bài toán biện luận, khung dây ra vào từ trường, hỗn hợp đồng vị",
P1=[
mc("Thả m kg nước đá ở 0 °C vào 1,0 kg nước ở 20 °C trong bình cách nhiệt. Giá trị lớn nhất của m "
   "để nước đá tan hết là (λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K))",
   ["0,12 kg.", "0,247 kg.", "0,50 kg.", "0,35 kg."],
   "B",
   "Nhiệt nước nhả ra tối đa khi hạ về 0 °C: Q = 1,0 · 4200 · 20 = 84 000 J.\n"
   "Nhiệt cần để tan hết m kg đá: Q = m · 3,4·10⁵.\n"
   "Điều kiện đá tan hết: m · 3,4·10⁵ ≤ 84 000 ⇒ m ≤ 0,247 kg.",
   "Biện luận điều kiện", K),

mc("Nếu khối lượng nước đá trong bài trên lớn hơn giá trị đó thì nhiệt độ cân bằng bằng",
   ["dưới 0 °C.", "đúng 0 °C.", "trên 0 °C.", "20 °C."],
   "B",
   "Khi nhiệt nước nhả ra không đủ làm tan hết đá, trong bình vẫn còn cả nước lẫn nước đá; "
   "hỗn hợp nước và nước đá luôn ở đúng 0 °C.",
   "Biện luận điều kiện", K),

mc("Một khối khí lí tưởng trong xi lanh có pit-tông tự do được đun nóng. Nếu pit-tông chạm vấu chặn "
   "giữa chừng rồi tiếp tục đun thì giai đoạn sau là quá trình",
   ["đẳng áp.", "đẳng tích.", "đẳng nhiệt.", "đoạn nhiệt."],
   "B",
   "Trước khi chạm vấu, pit-tông tự do nên quá trình đẳng áp. Sau khi chạm vấu, thể tích không "
   "thể tăng thêm nên quá trình chuyển thành đẳng tích và áp suất bắt đầu tăng.",
   "Nhận dạng quá trình – bẫy pit-tông", K, fig="k_sd_xilanh_quanang",
   cap="Xi lanh có pit-tông"),

mc("Một lượng khí lí tưởng ở 27 °C, thể tích 4,0 L, áp suất 1,0·10⁵ Pa được nung đẳng áp tới 87 °C "
   "rồi nén đẳng nhiệt về thể tích ban đầu. Áp suất cuối cùng bằng",
   ["1,0·10⁵ Pa.", "1,2·10⁵ Pa.", "1,5·10⁵ Pa.", "2,0·10⁵ Pa."],
   "B",
   "Giai đoạn 1 (đẳng áp): V₂ = 4,0 · 360/300 = 4,8 L, áp suất vẫn 1,0·10⁵ Pa.\n"
   "Giai đoạn 2 (đẳng nhiệt, về 4,0 L): p₃ = 1,0·10⁵ · 4,8/4,0 = 1,2·10⁵ Pa.",
   "Hai quá trình liên tiếp", K),

mc("Ở cùng nhiệt độ, tỉ số tốc độ trung bình của phân tử khí hêli (M = 4) và khí ôxi (M = 32) bằng",
   ["8.", "2√2.", "4.", "√2."],
   "B",
   "Động năng trung bình bằng nhau nên ½m₁v̄₁² = ½m₂v̄₂², suy ra v̄ tỉ lệ nghịch với căn bậc hai "
   "của khối lượng phân tử.\n"
   "v̄(He)/v̄(O₂) = √(32/4) = √8 = 2√2 ≈ 2,83.",
   "Động năng phân tử", K),

mc("Một khung dây hình vuông cạnh 20 cm, điện trở 0,40 Ω, chuyển động đều 5,0 m/s đi vào vùng từ "
   "trường đều B = 0,50 T. Nhiệt lượng toả ra trên khung trong suốt quá trình đi vào bằng",
   ["12,5 mJ.", "25,0 mJ.", "50,0 mJ.", "6,25 mJ."],
   "B",
   "e = B·a·v = 0,50 · 0,20 · 5,0 = 0,50 V;  i = 0,50/0,40 = 1,25 A.\n"
   "Thời gian đi vào: t = a/v = 0,20/5,0 = 0,040 s.\n"
   "Q = R·i²·t = 0,40 · 1,25² · 0,040 = 0,40 · 1,5625 · 0,040 = 0,025 J = 25,0 mJ.",
   "Năng lượng trong cảm ứng điện từ", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

mc("Một thanh dẫn dài 50 cm, khối lượng 200 g nằm trên hai ray nằm ngang có hệ số ma sát 0,25, "
   "trong từ trường đều thẳng đứng B = 0,40 T. Cường độ dòng điện nhỏ nhất để thanh bắt đầu trượt "
   "bằng (g = 10 m/s²)",
   ["1,25 A.", "2,50 A.", "5,00 A.", "0,625 A."],
   "B",
   "Lực ma sát nghỉ cực đại: μ·m·g = 0,25 · 0,200 · 10 = 0,50 N.\n"
   "Điều kiện trượt: B·I·ℓ ≥ 0,50 ⇒ 0,40 · I · 0,50 ≥ 0,50 ⇒ 0,20·I ≥ 0,50 ⇒ I ≥ 2,50 A.",
   "Cân bằng lực có ma sát", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi 200 V. Khi cuộn thứ cấp có 120 vòng thì "
   "điện áp thứ cấp là 24 V; khi quấn thêm 30 vòng thì điện áp thứ cấp là 30 V. "
   "Số vòng cuộn sơ cấp bằng",
   ["600 vòng.", "1000 vòng.", "1200 vòng.", "800 vòng."],
   "B",
   "Mỗi vòng thứ cấp ứng với điện áp (30 − 24)/30 = 0,20 V.\n"
   "Kiểm tra: 120 vòng cho 120 · 0,20 = 24 V ✓.\n"
   "Từ U₂/U₁ = N₂/N₁ ⇒ N₁ = N₂·U₁/U₂ = 120 · 200/24 = 1000 vòng.",
   "Máy biến áp – hệ hai phương trình", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một mẫu chứa hai đồng vị phóng xạ X (chu kì bán rã 2,0 giờ) và Y (chu kì bán rã 4,0 giờ), "
   "ban đầu độ phóng xạ mỗi đồng vị đều bằng H₀. Sau 4,0 giờ, tổng độ phóng xạ bằng",
   ["H₀/2.", "3H₀/4.", "H₀.", "H₀/4."],
   "B",
   "Sau 4,0 giờ: X trải qua 2 chu kì nên còn H₀/4; Y trải qua 1 chu kì nên còn H₀/2.\n"
   "Tổng: H₀/4 + H₀/2 = 3H₀/4.",
   "Hỗn hợp hai đồng vị", K),

mc("Một mẫu chất phóng xạ nguyên chất sau 3 chu kì bán rã có tỉ số giữa số hạt nhân con và "
   "số hạt nhân mẹ còn lại bằng",
   ["3.", "7.", "8.", "15."],
   "B",
   "Sau n chu kì, tỉ số con/mẹ bằng 2ⁿ − 1. Với n = 3: 2³ − 1 = 7.",
   "Tỉ số hạt nhân con và mẹ", TB),

mc("Cho phản ứng: ¹₁H + ⁷₃Li → 2·⁴₂He với m(H) = 1,0073; m(Li) = 7,0160; m(He) = 4,0015 u. "
   "Năng lượng toả ra xấp xỉ",
   ["9,5 MeV.", "18,9 MeV.", "28,4 MeV.", "37,8 MeV."],
   "B",
   "Trước: 1,0073 + 7,0160 = 8,0233 u.  Sau: 2 · 4,0015 = 8,0030 u.\n"
   "Δm = 0,0203 u ⇒ ΔE = 0,0203 · 931,5 ≈ 18,9 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

mc("Một nguồn nhiệt đồng vị chứa ²¹⁰Po có công suất ban đầu 100 W. Sau 138 ngày "
   "(đúng một chu kì bán rã), công suất còn",
   ["100 W.", "50 W.", "25 W.", "0 W."],
   "B",
   "Công suất tỉ lệ thuận với độ phóng xạ. Sau một chu kì bán rã, độ phóng xạ giảm một nửa nên "
   "công suất còn 50 W.",
   "Công suất nguồn phóng xạ", K),

mc("Trong phản ứng hạt nhân, nếu tổng khối lượng nghỉ của các hạt sau LỚN HƠN của các hạt trước thì "
   "phản ứng đó",
   ["toả năng lượng.", "thu năng lượng.",
    "không trao đổi năng lượng.", "không thể xảy ra trong mọi trường hợp."],
   "B",
   "Khối lượng nghỉ tăng nghĩa là phải cung cấp năng lượng để tạo ra phần khối lượng đó: "
   "phản ứng thu năng lượng. Nó vẫn xảy ra được nếu các hạt tới có đủ động năng.",
   "Năng lượng phản ứng hạt nhân", TB),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu 1024 Bq. Sau 5 chu kì bán rã, độ phóng xạ bằng",
   ["64 Bq.", "32 Bq.", "16 Bq.", "128 Bq."],
   "B",
   "H = 1024/2⁵ = 1024/32 = 32 Bq.",
   "Độ phóng xạ", TB),

mc("Đun nóng một khối khí trong bình kín thành cứng. Kết luận nào ĐÚNG?",
   ["Khí sinh công và nội năng giảm.", "Khí không sinh công, toàn bộ nhiệt lượng làm tăng nội năng.",
    "Khí nhận công từ bên ngoài.", "Nội năng không đổi vì bình kín."],
   "B",
   "Thành bình cứng nên thể tích không đổi, A = 0. Định luật I cho ΔU = Q: toàn bộ nhiệt lượng "
   "làm tăng nội năng của khí.",
   "Định luật I nhiệt động lực học", TB),

mc("Một dòng điện xoay chiều i = 2,0·cos(100πt + π/2) (A). Tại thời điểm t = 0, cường độ dòng điện",
   ["bằng 2,0 A.", "bằng 0.", "bằng 1,0 A.", "bằng −2,0 A."],
   "B",
   "i(0) = 2,0·cos(π/2) = 2,0 · 0 = 0 A.",
   "Giá trị tức thời", TB),

mc("Từ thông qua một vòng dây biến thiên theo quy luật Φ = 0,05·cos(20t) (Wb). "
   "Suất điện động cực đại trong vòng dây bằng",
   ["0,05 V.", "1,0 V.", "20 V.", "0,25 V."],
   "B",
   "Biên độ suất điện động E₀ = ω·Φ₀ = 20 · 0,05 = 1,0 V.",
   "Quan hệ giữa Φ và e", K),

mc("Một vòng dây kín được đặt trong từ trường đều rồi được lấy ra khỏi từ trường theo hai cách: "
   "lần đầu nhanh, lần sau chậm. So sánh ĐIỆN LƯỢNG chuyển qua tiết diện dây trong hai lần:",
   ["lần nhanh lớn hơn.", "hai lần bằng nhau.",
    "lần chậm lớn hơn.", "không so sánh được."],
   "B",
   "q = |ΔΦ|/R chỉ phụ thuộc độ biến thiên từ thông và điện trở, không phụ thuộc thời gian. "
   "Chỉ có cường độ dòng điện tức thời là khác nhau.",
   "Điện lượng cảm ứng", K),
],
P2=[
ds("Thả m kg nước đá ở 0 °C vào 2,0 kg nước ở 25 °C trong bình cách nhiệt. "
   "Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng tối đa mà nước có thể nhả ra là 210 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · 25 = 210 000 J."),
    ("Khối lượng nước đá lớn nhất để đá tan hết xấp xỉ 0,618 kg.", True,
     "Đúng. m · 3,4·10⁵ ≤ 210 000 ⇒ m ≤ 0,6176 kg."),
    ("Nếu thả 0,80 kg nước đá thì nhiệt độ cân bằng là 0 °C và vẫn còn đá.", True,
     "Đúng. 0,80 kg cần 272 000 J để tan hết, lớn hơn 210 000 J mà nước có thể nhả, "
     "nên đá chỉ tan một phần."),
    ("Nếu thả 0,40 kg nước đá thì nhiệt độ cân bằng vẫn là 0 °C.", False,
     "Sai. 0,40 kg chỉ cần 136 000 J để tan hết, nhỏ hơn 210 000 J nên đá tan hết và còn dư nhiệt "
     "để hâm nóng cả khối nước lên trên 0 °C.")],
   "Biện luận điều kiện", K),

ds("Một khối khí lí tưởng ở 27 °C, thể tích 5,0 L, áp suất 1,0·10⁵ Pa. Người ta nung nóng đẳng áp "
   "tới 127 °C rồi nén đẳng nhiệt về thể tích ban đầu.",
   [("Sau giai đoạn đẳng áp, thể tích khí là 6,67 L.", True,
     "Đúng. V₂ = 5,0 · 400/300 ≈ 6,67 L."),
    ("Trong giai đoạn đẳng áp, khí sinh công.", True,
     "Đúng. Thể tích tăng nên khí đẩy pit-tông ra, sinh công (A < 0 đối với khí)."),
    ("Sau giai đoạn đẳng nhiệt, áp suất khí là 1,33·10⁵ Pa.", True,
     "Đúng. p₃ = 1,0·10⁵ · 6,67/5,0 ≈ 1,33·10⁵ Pa."),
    ("Nhiệt độ cuối cùng của khí trở về 27 °C.", False,
     "Sai. Giai đoạn hai là ĐẲNG NHIỆT ở 127 °C nên nhiệt độ cuối vẫn là 127 °C, "
     "không trở về giá trị ban đầu.")],
   "Hai quá trình liên tiếp", K),

ds("Một khung dây hình vuông cạnh 25 cm, điện trở 0,50 Ω, chuyển động đều 4,0 m/s đi vào vùng từ "
   "trường đều B = 0,60 T, các đường sức vuông góc mặt phẳng khung.",
   [("Suất điện động cảm ứng khi khung đi vào bằng 0,60 V.", True,
     "Đúng. e = B·a·v = 0,60 · 0,25 · 4,0 = 0,60 V."),
    ("Cường độ dòng cảm ứng bằng 1,2 A.", True,
     "Đúng. i = 0,60/0,50 = 1,2 A."),
    ("Thời gian khung đi hết vào vùng từ trường là 0,0625 s.", True,
     "Đúng. t = a/v = 0,25/4,0 = 0,0625 s."),
    ("Nhiệt lượng toả ra trên khung trong quá trình đi vào bằng 0,090 J.", False,
     "Sai. Q = R·i²·t = 0,50 · 1,2² · 0,0625 = 0,50 · 1,44 · 0,0625 = 0,045 J. "
     "Giá trị 0,090 J là kết quả khi quên chia đôi hoặc nhân nhầm hệ số.")],
   "Năng lượng trong cảm ứng điện từ", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

ds("Một mẫu chứa hai đồng vị phóng xạ độc lập: X có chu kì bán rã 3,0 giờ và Y có chu kì bán rã "
   "6,0 giờ. Ban đầu độ phóng xạ mỗi đồng vị đều là 600 Bq.",
   [("Độ phóng xạ tổng ban đầu là 1200 Bq.", True,
     "Đúng. Hai quá trình độc lập nên độ phóng xạ cộng lại."),
    ("Sau 6,0 giờ, độ phóng xạ của X còn 150 Bq.", True,
     "Đúng. X trải qua 2 chu kì: 600/4 = 150 Bq."),
    ("Sau 6,0 giờ, độ phóng xạ của Y còn 300 Bq.", True,
     "Đúng. Y trải qua đúng 1 chu kì: 600/2 = 300 Bq."),
    ("Sau 6,0 giờ, độ phóng xạ tổng bằng một nửa giá trị ban đầu.", False,
     "Sai. Tổng là 150 + 300 = 450 Bq, bằng 450/1200 = 37,5 % giá trị ban đầu chứ không phải 50 %.")],
   "Hỗn hợp hai đồng vị", K),
],
P3=[
sa("Thả m kg nước đá ở 0 °C vào 1,5 kg nước ở 30 °C trong bình cách nhiệt. Khối lượng nước đá lớn "
   "nhất để đá tan hết bằng bao nhiêu kilôgam (làm tròn đến chữ số thập phân thứ ba)? "
   "Cho λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K).",
   "0,556",
   "Nhiệt tối đa nước nhả ra: Q = 1,5 · 4200 · 30 = 189 000 J.\n"
   "Điều kiện đá tan hết: m · 3,4·10⁵ ≤ 189 000 ⇒ m ≤ 0,5559 ≈ 0,556 kg.",
   "Biện luận điều kiện", K),

sa("Một lượng khí ở 27 °C, thể tích 6,0 L được nung đẳng áp tới 127 °C. Thể tích khí lúc này bằng "
   "bao nhiêu lít?",
   "8",
   "Đẳng áp: V₂ = V₁·T₂/T₁ = 6,0 · 400/300 = 8,0 L.",
   "Định luật Charles", TB),

sa("Một thanh dẫn dài 40 cm, khối lượng 250 g nằm trên hai ray nằm ngang có hệ số ma sát 0,20, "
   "trong từ trường đều thẳng đứng B = 0,50 T. Cường độ dòng điện nhỏ nhất để thanh bắt đầu trượt "
   "bằng bao nhiêu ampe? Lấy g = 10 m/s².",
   "2,5",
   "Lực ma sát nghỉ cực đại: μ·m·g = 0,20 · 0,250 · 10 = 0,50 N.\n"
   "B·I·ℓ ≥ 0,50 ⇒ 0,50 · I · 0,40 ≥ 0,50 ⇒ 0,20·I ≥ 0,50 ⇒ I ≥ 2,5 A.",
   "Cân bằng lực có ma sát", K),

sa("Một khung dây 250 vòng, diện tích mỗi vòng 40 cm², quay đều quanh trục vuông góc với từ trường "
   "đều B = 0,50 T, tần số 50 Hz. Suất điện động hiệu dụng của khung bằng bao nhiêu vôn "
   "(làm tròn đến chữ số thập phân thứ nhất)? Lấy π ≈ 3,1416; √2 ≈ 1,414.",
   "111,1",
   "ω = 2π·50 ≈ 314,16 rad/s;  S = 4,0·10⁻³ m².\n"
   "E₀ = ω·N·B·S = 314,16 · 250 · 0,50 · 4,0·10⁻³ = 314,16 · 0,50 ≈ 157,08 V.\n"
   "E = E₀/√2 = 157,08/1,414 ≈ 111,1 V.",
   "Máy phát điện xoay chiều", K),

sa("Cho phản ứng ²₁H + ⁶₃Li → 2·⁴₂He. Biết m(²H) = 2,0136; m(⁶Li) = 6,0151; m(⁴He) = 4,0015 u; "
   "1 u·c² = 931,5 MeV. Năng lượng toả ra bằng bao nhiêu MeV (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "23,9",
   "Trước: 2,0136 + 6,0151 = 8,0287 u.  Sau: 2 · 4,0015 = 8,0030 u.\n"
   "Δm = 0,0257 u ⇒ ΔE = 0,0257 · 931,5 ≈ 23,9 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

sa("Một nguồn phóng xạ có công suất ban đầu 240 W và chu kì bán rã 15 năm. Sau 45 năm, công suất "
   "của nguồn bằng bao nhiêu oát?",
   "30",
   "Công suất tỉ lệ thuận với độ phóng xạ nên giảm theo cùng quy luật.\n"
   "n = 45/15 = 3 ⇒ P = 240/2³ = 240/8 = 30 W.",
   "Công suất nguồn phóng xạ", K),
])


# =====================================================================  ĐỀ 13
DE13 = dict(
ma="TH-Đề 13", ten="ĐỀ THI THỬ SỐ 13", muc="Trung bình → Khó",
trongtam="Đồ thị nâng cao, bài toán hai vật, xung lượng của lực từ",
P1=[
mc("Hai bình cách nhiệt chứa nước ở 20 °C và 80 °C với khối lượng lần lượt 3,0 kg và 1,0 kg. "
   "Trộn hai bình, nhiệt độ cân bằng bằng",
   ["30 °C.", "35 °C.", "50 °C.", "40 °C."],
   "B",
   "3,0·4200·(t − 20) = 1,0·4200·(80 − t)\n"
   "3(t − 20) = 80 − t ⇒ 3t − 60 = 80 − t ⇒ 4t = 140 ⇒ t = 35 °C.\n"
   "Kết quả gần nhiệt độ của khối nước nhiều hơn — hợp lí.",
   "Phương trình cân bằng nhiệt", TB),

mc("Muốn pha 4,0 kg nước ở 40 °C từ nước sôi 100 °C và nước ở 20 °C thì cần bao nhiêu kilôgam "
   "nước sôi?",
   ["0,80 kg.", "1,00 kg.", "1,33 kg.", "2,00 kg."],
   "B",
   "Gọi m là khối lượng nước sôi, (4,0 − m) là khối lượng nước 20 °C.\n"
   "m·(100 − 40) = (4,0 − m)·(40 − 20) ⇒ 60m = 80 − 20m ⇒ 80m = 80 ⇒ m = 1,00 kg.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Trên đồ thị nhiệt độ – thời gian khi đun một chất rắn, đoạn nghiêng TRƯỚC đoạn nằm ngang dốc "
   "hơn đoạn nghiêng SAU. Điều đó cho biết",
   ["nhiệt dung riêng thể rắn lớn hơn thể lỏng.", "nhiệt dung riêng thể rắn nhỏ hơn thể lỏng.",
    "khối lượng chất thay đổi.", "nguồn nhiệt thay đổi công suất."],
   "B",
   "Với công suất không đổi, độ dốc ΔT/Δt = P/(m·c) tỉ lệ nghịch với nhiệt dung riêng. "
   "Đoạn dốc hơn ứng với c nhỏ hơn, tức nhiệt dung riêng của thể rắn nhỏ hơn thể lỏng.",
   "Đọc đồ thị chuyển thể", K, fig="n_dt_nuocda", cap="Đồ thị nhiệt độ theo thời gian"),

mc("Một lượng khí lí tưởng có đồ thị trong hệ (p, T) là đường thẳng đi qua gốc toạ độ. "
   "Quá trình đó là",
   ["đẳng nhiệt.", "đẳng tích.", "đẳng áp.", "không xác định."],
   "B",
   "Đường thẳng qua gốc trong hệ (p, T) nghĩa là p/T không đổi — đúng là định luật Gay-Lussac "
   "cho quá trình đẳng tích.",
   "Nhận dạng quá trình từ đồ thị", TB, fig="k_dt_ba_he_truc", cap="Ba quá trình trên ba hệ trục"),

mc("Một khối khí lí tưởng có khối lượng riêng 1,2 kg/m³ ở 27 °C và áp suất 1,0·10⁵ Pa. "
   "Khối lượng mol của khí đó xấp xỉ (R = 8,31 J/(mol·K))",
   ["0,018 kg/mol.", "0,030 kg/mol.", "0,044 kg/mol.", "0,032 kg/mol."],
   "B",
   "Từ ρ = pM/(RT) suy ra M = ρRT/p = 1,2 · 8,31 · 300/(1,0·10⁵) = 2991,6/10⁵ ≈ 0,030 kg/mol, "
   "tức khoảng 30 g/mol.",
   "Khối lượng riêng của khí", K),

mc("Nếu nén một khối khí lí tưởng đẳng nhiệt để thể tích còn một nửa thì khối lượng riêng của khí",
   ["giảm một nửa.", "tăng gấp đôi.", "không đổi.", "tăng gấp bốn."],
   "B",
   "Khối lượng khí không đổi, thể tích giảm một nửa nên ρ = m/V tăng gấp đôi.",
   "Khối lượng riêng của khí", TB),

mc("Một thanh dẫn khối lượng m nằm trên hai ray nằm ngang không ma sát trong từ trường đều thẳng "
   "đứng B, dài ℓ. Truyền cho thanh vận tốc v₀ rồi để tự do. Tổng điện lượng qua mạch cho tới khi "
   "thanh dừng bằng",
   ["m·v₀·B·ℓ.", "m·v₀/(B·ℓ).", "B·ℓ/(m·v₀).", "m·v₀²/(B·ℓ)."],
   "B",
   "Xung lượng của lực từ bằng độ biến thiên động lượng: B·ℓ·q = m·v₀ ⇒ q = m·v₀/(B·ℓ). "
   "Kết quả không phụ thuộc điện trở mạch.",
   "Xung lượng của lực từ", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Với bài toán trên, tổng nhiệt lượng toả ra trên mạch cho tới khi thanh dừng bằng",
   ["m·v₀·B·ℓ.", "½·m·v₀².", "B²ℓ²v₀.", "m·v₀²/R."],
   "B",
   "Không có ma sát và không có lực kéo nên toàn bộ động năng ban đầu chuyển thành nhiệt: "
   "Q = ½·m·v₀². Kết quả không phụ thuộc B, ℓ hay R.",
   "Bảo toàn năng lượng", K),

mc("Một khung dây kín rơi thẳng đứng, đi ra khỏi biên ngang của vùng từ trường đều. "
   "Tốc độ giới hạn của khung tỉ lệ",
   ["thuận với B².", "nghịch với B².", "thuận với B.", "không phụ thuộc B."],
   "B",
   "Ở tốc độ giới hạn: B²a²v/R = m·g ⇒ v = m·g·R/(B²a²), tỉ lệ NGHỊCH với B². "
   "Từ trường càng mạnh thì khung rơi càng chậm.",
   "Tốc độ giới hạn của khung rơi", K),

mc("Một máy biến áp lí tưởng cung cấp cho tải công suất 1,1 kW ở điện áp thứ cấp 110 V. "
   "Điện áp sơ cấp 220 V. Cường độ dòng điện ở cuộn sơ cấp bằng",
   ["10,0 A.", "5,0 A.", "2,5 A.", "20,0 A."],
   "B",
   "Máy lí tưởng nên P₁ = P₂ = 1100 W.\n"
   "I₁ = P₁/U₁ = 1100/220 = 5,0 A.",
   "Máy biến áp – công suất", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất không đổi đi xa. Khi điện áp là U thì hiệu suất 90 %; khi điện áp là 3U thì "
   "hiệu suất bằng",
   ["96,7 %.", "98,9 %.", "97,0 %.", "99,5 %."],
   "B",
   "Hao phí ban đầu chiếm 10 %. Tăng U gấp 3 lần thì hao phí giảm 9 lần, còn 10/9 ≈ 1,11 %.\n"
   "Hiệu suất mới: 100 − 1,11 ≈ 98,9 %.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một dòng điện xoay chiều chạy qua điện trở R. Nếu tăng giá trị hiệu dụng lên gấp ba thì nhiệt "
   "lượng toả ra trong cùng thời gian",
   ["tăng gấp ba.", "tăng gấp chín.", "không đổi.", "giảm ba lần."],
   "B",
   "Q = R·I²·t tỉ lệ với BÌNH PHƯƠNG cường độ hiệu dụng. I tăng 3 lần thì Q tăng 9 lần.",
   "Tác dụng nhiệt của dòng xoay chiều", TB),

mc("Hạt nhân ²¹⁰₈₄Po phóng xạ α. Sau bao lâu thì tỉ số số hạt nhân chì và pôlôni còn lại bằng 3? "
   "(chu kì bán rã 138 ngày)",
   ["138 ngày.", "276 ngày.", "414 ngày.", "552 ngày."],
   "B",
   "Tỉ số con/mẹ bằng 2ⁿ − 1 = 3 ⇒ 2ⁿ = 4 ⇒ n = 2 chu kì.\n"
   "t = 2 · 138 = 276 ngày.",
   "Tỉ số hạt nhân con và mẹ", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

mc("Một mẫu chất phóng xạ có độ phóng xạ 500 Bq lúc 7 giờ và 125 Bq lúc 13 giờ cùng ngày. "
   "Chu kì bán rã bằng",
   ["2,0 giờ.", "3,0 giờ.", "4,0 giờ.", "6,0 giờ."],
   "B",
   "Thời gian giữa hai lần đo: 6 giờ. Tỉ số giảm: 500/125 = 4 = 2² ⇒ n = 2 chu kì.\n"
   "T = 6/2 = 3,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB),

mc("Năng lượng liên kết riêng của ²³⁵U là 7,6 MeV/nuclêôn, của các mảnh vỡ trung bình là "
   "8,5 MeV/nuclêôn. Năng lượng toả ra khi phân hạch một hạt nhân ²³⁵U xấp xỉ",
   ["106 MeV.", "212 MeV.", "159 MeV.", "235 MeV."],
   "B",
   "Chênh lệch năng lượng liên kết riêng: 8,5 − 7,6 = 0,9 MeV mỗi nuclêôn.\n"
   "Tổng: 0,9 · 235 ≈ 212 MeV — phù hợp với giá trị quen thuộc khoảng 200 MeV.",
   "Năng lượng phân hạch", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chất phóng xạ nguyên chất, sau thời gian t₁ còn 50 % số hạt nhân. "
   "Sau thời gian 3·t₁, số hạt nhân còn lại bằng",
   ["16,7 %.", "12,5 %.", "25,0 %.", "6,25 %."],
   "B",
   "t₁ = T nên 3t₁ = 3T ⇒ còn lại 2⁻³ = 12,5 %.",
   "Định luật phóng xạ", TB),

mc("Trong lò phản ứng hạt nhân, nếu hệ số nhân nơtron k = 1,05 thì công suất lò sẽ",
   ["giảm dần.", "tăng dần.", "giữ nguyên.", "bằng không."],
   "B",
   "k > 1 nghĩa là số phân hạch mỗi thế hệ tăng lên, nên công suất lò tăng dần. "
   "Người vận hành phải đẩy thanh điều khiển vào để đưa k về 1.",
   "Điều khiển lò phản ứng", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Khi nói về tia γ, phát biểu nào SAI?",
   ["Tia γ là sóng điện từ có bước sóng rất ngắn.",
    "Tia γ bị lệch trong từ trường.",
    "Tia γ có khả năng đâm xuyên lớn nhất trong ba loại tia.",
    "Tia γ thường phát ra kèm theo phóng xạ α hoặc β."],
   "B",
   "Tia γ không mang điện nên không chịu tác dụng của lực từ, do đó không bị lệch trong từ trường "
   "cũng như trong điện trường. Ba phát biểu còn lại đều đúng.",
   "Ba loại tia phóng xạ", TB, fig="h_sd_tia_phongxa", cap="Ba tia trong điện trường"),
],
P2=[
ds("Trộn 2,0 kg nước ở 15 °C với 3,0 kg nước ở 65 °C trong bình cách nhiệt. "
   "Cho c(nước) = 4200 J/(kg·K).",
   [("Khối nước lạnh thu nhiệt, khối nước nóng toả nhiệt.", True,
     "Đúng. Nhiệt luôn truyền từ nơi có nhiệt độ cao sang nơi có nhiệt độ thấp."),
    ("Nhiệt độ cân bằng bằng 45 °C.", True,
     "Đúng. 2,0·(t − 15) = 3,0·(65 − t) ⇒ 2t − 30 = 195 − 3t ⇒ 5t = 225 ⇒ t = 45 °C."),
    ("Nhiệt độ cân bằng gần với nhiệt độ của khối nước có khối lượng lớn hơn.", True,
     "Đúng. 45 °C gần 65 °C hơn 15 °C, phù hợp vì khối nước 65 °C nặng hơn."),
    ("Nếu hai khối nước có khối lượng bằng nhau thì nhiệt độ cân bằng vẫn là 45 °C.", False,
     "Sai. Khi khối lượng bằng nhau, nhiệt độ cân bằng là trung bình cộng: (15 + 65)/2 = 40 °C.")],
   "Phương trình cân bằng nhiệt", TB),

ds("Một khối khí lí tưởng có khối lượng riêng 1,6 kg/m³ ở nhiệt độ 27 °C và áp suất 1,0·10⁵ Pa. "
   "Cho R = 8,31 J/(mol·K).",
   [("Khối lượng mol của khí xấp xỉ 0,040 kg/mol.", True,
     "Đúng. M = ρRT/p = 1,6 · 8,31 · 300/10⁵ = 3988,8/10⁵ ≈ 0,0399 kg/mol."),
    ("Nếu nén đẳng nhiệt để áp suất tăng gấp đôi thì khối lượng riêng cũng tăng gấp đôi.", True,
     "Đúng. Ở nhiệt độ không đổi, ρ = pM/(RT) tỉ lệ thuận với p."),
    ("Nếu nung nóng đẳng áp lên 327 °C thì khối lượng riêng giảm một nửa.", True,
     "Đúng. T tăng từ 300 K lên 600 K, mà ρ tỉ lệ nghịch với T ở áp suất không đổi."),
    ("Khối lượng riêng của khí không phụ thuộc loại khí.", False,
     "Sai. ρ = pM/(RT) tỉ lệ thuận với khối lượng mol M, nên ở cùng p và T, khí nặng hơn thì "
     "khối lượng riêng lớn hơn.")],
   "Khối lượng riêng của khí", K),

ds("Một thanh dẫn khối lượng 200 g, dài 40 cm nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,50 T. Điện trở toàn mạch 0,40 Ω. Truyền cho thanh vận tốc ban đầu "
   "5,0 m/s rồi để tự do.",
   [("Suất điện động cảm ứng ngay sau khi truyền vận tốc là 1,0 V.", True,
     "Đúng. e = B·ℓ·v = 0,50 · 0,40 · 5,0 = 1,0 V."),
    ("Tổng điện lượng chuyển qua mạch cho tới khi thanh dừng là 5,0 C.", True,
     "Đúng. q = m·v₀/(B·ℓ) = 0,200 · 5,0/(0,50 · 0,40) = 1,0/0,20 = 5,0 C."),
    ("Tổng nhiệt lượng toả ra trên mạch là 2,5 J.", True,
     "Đúng. Q = ½·m·v₀² = 0,5 · 0,200 · 25 = 2,5 J."),
    ("Nếu tăng điện trở mạch lên gấp đôi thì tổng nhiệt lượng toả ra giảm một nửa.", False,
     "Sai. Tổng nhiệt lượng luôn bằng động năng ban đầu, không phụ thuộc điện trở. "
     "Điện trở chỉ làm thanh dừng chậm hơn.")],
   "Xung lượng và bảo toàn năng lượng", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

ds("Hạt nhân ²¹⁰₈₄Po phóng xạ α thành ²⁰⁶₈₂Pb với chu kì bán rã 138 ngày.",
   [("Sau 138 ngày, tỉ số số hạt nhân chì và pôlôni còn lại bằng 1.", True,
     "Đúng. Sau một chu kì, số hạt đã rã bằng số hạt còn lại."),
    ("Sau 276 ngày, tỉ số đó bằng 3.", True,
     "Đúng. 2² − 1 = 3."),
    ("Sau 414 ngày, tỉ số đó bằng 7.", True,
     "Đúng. 2³ − 1 = 7."),
    ("Tỉ số này tăng gấp đôi sau mỗi chu kì bán rã.", False,
     "Sai. Tỉ số là 2ⁿ − 1, tăng theo dãy 1, 3, 7, 15… Nếu tăng gấp đôi thì dãy phải là "
     "1, 2, 4, 8 — không đúng.")],
   "Tỉ số hạt nhân con và mẹ", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),
],
P3=[
sa("Muốn pha 6,0 kg nước ở 45 °C từ nước sôi 100 °C và nước ở 25 °C thì cần bao nhiêu kilôgam "
   "nước sôi (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,6",
   "Gọi m là khối lượng nước sôi.\n"
   "m·(100 − 45) = (6,0 − m)·(45 − 25) ⇒ 55m = 120 − 20m ⇒ 75m = 120 ⇒ m = 1,6 kg.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Một khối khí lí tưởng có khối lượng riêng 2,0 kg/m³ ở 27 °C và áp suất 1,5·10⁵ Pa. "
   "Khối lượng mol của khí bằng bao nhiêu gam trên mol (làm tròn đến hàng đơn vị)? "
   "Cho R = 8,31 J/(mol·K).",
   "33",
   "M = ρRT/p = 2,0 · 8,31 · 300/(1,5·10⁵) = 4986/150 000 = 0,03324 kg/mol ≈ 33 g/mol.",
   "Khối lượng riêng của khí", K),

sa("Một thanh dẫn khối lượng 300 g, dài 50 cm nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,60 T. Truyền cho thanh vận tốc ban đầu 4,0 m/s rồi để tự do. "
   "Tổng điện lượng chuyển qua mạch cho tới khi thanh dừng bằng bao nhiêu culông?",
   "4",
   "Xung lượng của lực từ bằng độ biến thiên động lượng:\n"
   "B·ℓ·q = m·v₀ ⇒ q = 0,300 · 4,0/(0,60 · 0,50) = 1,2/0,30 = 4,0 C.",
   "Xung lượng của lực từ", K),

sa("Truyền công suất không đổi đi xa. Ở điện áp U hiệu suất là 90 %. Khi tăng điện áp lên 2U thì "
   "hiệu suất bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ nhất)?",
   "97,5",
   "Hao phí ban đầu chiếm 10 %. Tăng U gấp đôi thì hao phí giảm 4 lần, còn 2,5 %.\n"
   "Hiệu suất mới: 100 − 2,5 = 97,5 %.",
   "Truyền tải – bài toán tỉ lệ", K),

sa("Năng lượng liên kết riêng của ²³⁹Pu là 7,6 MeV/nuclêôn, của các mảnh vỡ trung bình là "
   "8,4 MeV/nuclêôn. Năng lượng toả ra khi phân hạch một hạt nhân ²³⁹Pu xấp xỉ bằng bao nhiêu MeV "
   "(làm tròn đến hàng đơn vị)?",
   "191",
   "Chênh lệch năng lượng liên kết riêng: 8,4 − 7,6 = 0,8 MeV mỗi nuclêôn.\n"
   "Tổng: 0,8 · 239 = 191,2 ≈ 191 MeV.",
   "Năng lượng phân hạch", K),

sa("Một mẫu chất phóng xạ có độ phóng xạ 720 Bq lúc 8 giờ và 90 Bq lúc 20 giờ cùng ngày. "
   "Chu kì bán rã của chất đó bằng bao nhiêu giờ?",
   "4",
   "Thời gian giữa hai lần đo: 20 − 8 = 12 giờ.\n"
   "Tỉ số giảm: 720/90 = 8 = 2³ ⇒ n = 3 chu kì.\n"
   "T = 12/3 = 4,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB),
])


# =====================================================================  ĐỀ 14
DE14 = dict(
ma="TH-Đề 14", ten="ĐỀ THI THỬ SỐ 14", muc="Trung bình → Khó",
trongtam="Hiệu suất, chu trình, tổng hợp cảm ứng điện từ và năng lượng hạt nhân",
P1=[
mc("Một động cơ nhiệt nhận 1000 J nhiệt từ nguồn nóng và thải 700 J cho nguồn lạnh trong mỗi chu "
   "trình. Hiệu suất của động cơ bằng",
   ["70 %.", "30 %.", "43 %.", "143 %."],
   "B",
   "Công sinh ra mỗi chu trình: A = 1000 − 700 = 300 J.\n"
   "H = A/Q(nhận) = 300/1000 = 0,30 = 30 %.",
   "Hiệu suất động cơ nhiệt", K),

mc("Một máy lạnh lấy đi 400 J nhiệt từ buồng lạnh và tiêu tốn 100 J công điện trong mỗi chu trình. "
   "Nhiệt lượng thải ra môi trường bằng",
   ["300 J.", "500 J.", "400 J.", "100 J."],
   "B",
   "Theo định luật bảo toàn năng lượng, nhiệt thải ra bằng tổng nhiệt lấy từ buồng lạnh và công "
   "tiêu tốn: 400 + 100 = 500 J.",
   "Bảo toàn năng lượng trong máy lạnh", K),

mc("Một khối khí lí tưởng thực hiện chu trình gồm ba quá trình: đẳng tích, đẳng áp, đẳng nhiệt. "
   "Sau một chu trình, tổng nhiệt lượng khí nhận được bằng",
   ["không.", "tổng công mà khí sinh ra.",
    "độ biến thiên nội năng.", "luôn dương."],
   "B",
   "Sau chu trình kín, ΔU = 0. Từ ΔU = A + Q suy ra Q = −A: tổng nhiệt lượng khí NHẬN đúng bằng "
   "tổng công khí SINH ra.",
   "Chu trình kín", K, fig="k_dt_chutrinh", cap="Chu trình trong hệ (p, V)"),

mc("Một bình 10 L chứa khí ở 27 °C, áp suất 2,0·10⁵ Pa. Bơm thêm khí cùng loại vào bình tới khi "
   "áp suất đạt 5,0·10⁵ Pa ở cùng nhiệt độ. Khối lượng khí bơm thêm so với khối lượng khí ban đầu",
   ["bằng 0,5 lần.", "bằng 1,5 lần.", "bằng 2,5 lần.", "bằng 2,0 lần."],
   "B",
   "Với V và T không đổi, khối lượng khí tỉ lệ thuận với áp suất.\n"
   "m₂/m₁ = 5,0/2,0 = 2,5 nên khí bơm thêm là 2,5 − 1 = 1,5 lần khối lượng ban đầu.",
   "Phương trình Clapeyron", K),

mc("Ở 27 °C, tốc độ trung bình của phân tử khí nitơ là v. Muốn tốc độ trung bình tăng lên 2v thì "
   "phải nung nóng khí tới",
   ["54 °C.", "927 °C.", "327 °C.", "600 °C."],
   "B",
   "Động năng trung bình tỉ lệ với T và với v̄². Muốn v̄ tăng 2 lần thì T phải tăng 4 lần.\n"
   "T₂ = 4 · 300 = 1200 K ⇒ t₂ = 1200 − 273 = 927 °C.",
   "Động năng phân tử", K),

mc("Một khung dây hình vuông cạnh 30 cm, khối lượng 40 g, điện trở 0,20 Ω rơi thẳng đứng đi ra "
   "khỏi vùng từ trường đều B = 0,40 T. Tốc độ giới hạn của khung bằng (g = 10 m/s²)",
   ["5,6 m/s.", "2,8 m/s.", "11,1 m/s.", "1,4 m/s."],
   "A",
   "v = m·g·R/(B²a²) = 0,040 · 10 · 0,20/(0,40² · 0,30²)\n"
   "= 0,080/(0,16 · 0,090) = 0,080/0,0144 ≈ 5,6 m/s.",
   "Tốc độ giới hạn của khung rơi", K),

mc("Một cuộn dây 600 vòng, điện trở 6,0 Ω, diện tích mỗi vòng 30 cm², đặt vuông góc với từ trường "
   "đều. Muốn cường độ dòng cảm ứng đạt 0,50 A thì tốc độ biến thiên của cảm ứng từ phải bằng",
   ["0,83 T/s.", "1,67 T/s.", "3,33 T/s.", "0,50 T/s."],
   "B",
   "e = i·R = 0,50 · 6,0 = 3,0 V.\n"
   "e = N·S·(ΔB/Δt) ⇒ ΔB/Δt = 3,0/(600 · 3,0·10⁻³) = 3,0/1,8 ≈ 1,67 T/s.",
   "Faraday – bài toán ngược", K),

mc("Một thanh dẫn nằm ngang treo bằng hai lò xo trong từ trường đều nằm ngang vuông góc với thanh. "
   "Khi cho dòng điện theo chiều làm lực từ hướng LÊN, mỗi lò xo giãn ít đi 0,80 cm so với ban đầu "
   "(ban đầu giãn 4,0 cm). Tỉ số lực từ trên trọng lượng bằng",
   ["0,16.", "0,20.", "0,25.", "0,80."],
   "B",
   "Ban đầu: 2k·4,0 = P.  Khi có dòng: 2k·3,2 = P − F.\n"
   "Lấy hiệu: 2k·0,80 = F ⇒ F/P = 0,80/4,0 = 0,20.",
   "Thanh dẫn treo trên lò xo", K, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),

mc("Một nhà máy truyền công suất P đi xa, hiệu suất 80 %. Nếu giữ nguyên điện áp nhưng giảm công "
   "suất truyền còn một nửa thì hiệu suất bằng",
   ["80 %.", "90 %.", "85 %.", "95 %."],
   "B",
   "Hao phí ΔP = R·P²/U² tỉ lệ với P². Ban đầu hao phí bằng 0,20·P.\n"
   "Khi công suất còn P/2, hao phí còn (0,20·P)/4 = 0,05·P, so với công suất truyền P/2 thì "
   "chiếm 0,05P/(0,5P) = 10 %.\n"
   "Hiệu suất mới: 100 − 10 = 90 %.",
   "Hiệu suất truyền tải", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Đặt điện áp xoay chiều u = U₀·cos(ωt) vào hai đầu điện trở R. Công suất trung bình tiêu thụ "
   "trên R bằng",
   ["U₀²/R.", "U₀²/(2R).", "2U₀²/R.", "U₀²/(4R)."],
   "B",
   "Công suất trung bình tính theo giá trị hiệu dụng: P = U²/R với U = U₀/√2.\n"
   "P = (U₀²/2)/R = U₀²/(2R).",
   "Công suất dòng xoay chiều", K),

mc("Một khung dây quay đều trong từ trường đều, từ thông cực đại qua khung là 0,020 Wb, "
   "tần số 50 Hz. Suất điện động cực đại xấp xỉ",
   ["1,0 V.", "6,28 V.", "3,14 V.", "12,6 V."],
   "B",
   "E₀ = ω·Φ₀ = 2π·50 · 0,020 = 314,16 · 0,020 ≈ 6,28 V.",
   "Quan hệ giữa Φ và e", K),

mc("Cho phản ứng ¹⁴₇N + ¹₀n → ¹⁴₆C + ¹₁H, toả 1,21 MeV. Nếu nơtron tới đứng yên thì tổng động năng "
   "của hai hạt sau phản ứng bằng",
   ["0.", "1,21 MeV.", "0,605 MeV.", "2,42 MeV."],
   "B",
   "Phản ứng toả năng lượng nên không cần động năng ban đầu. Toàn bộ năng lượng toả ra chuyển "
   "thành động năng của các hạt sản phẩm: 1,21 MeV.",
   "Bảo toàn năng lượng trong phản ứng", K),

mc("Một mẫu chất phóng xạ nguyên chất sau 4 chu kì bán rã. Số hạt nhân phân rã trong chu kì thứ tư "
   "so với số hạt phân rã trong chu kì thứ nhất bằng",
   ["1/4.", "1/8.", "1/2.", "1/16."],
   "B",
   "Chu kì 1: N₀ − N₀/2 = N₀/2.\n"
   "Chu kì 4: N₀/8 − N₀/16 = N₀/16.\n"
   "Tỉ số: (N₀/16)/(N₀/2) = 1/8.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Một nguồn phóng xạ có chu kì bán rã 20 năm. Sau bao lâu thì độ phóng xạ giảm còn 10 % giá trị "
   "ban đầu (ln2 ≈ 0,693)?",
   ["40 năm.", "66,4 năm.", "100 năm.", "200 năm."],
   "B",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,10 ⇒ n = ln10/ln2 = 2,303/0,693 ≈ 3,32.\n"
   "t = 3,32 · 20 ≈ 66,4 năm.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Trong chuỗi phân rã từ ²³⁵U tới ²⁰⁷Pb, số nơtron của hạt nhân giảm tổng cộng",
   ["14.", "18.", "22.", "28."],
   "B",
   "Số nơtron ban đầu: 235 − 92 = 143. Số nơtron cuối: 207 − 82 = 125.\n"
   "Giảm: 143 − 125 = 18.",
   "Chuỗi phân rã", K),

mc("Muốn tính tổng năng lượng mà một mẫu chất phóng xạ toả ra cho tới khi phân rã hết, ta lấy",
   ["độ phóng xạ ban đầu nhân với chu kì bán rã.",
    "số hạt nhân ban đầu nhân với năng lượng mỗi phân rã.",
    "hằng số phóng xạ nhân với số hạt nhân.",
    "chu kì bán rã chia cho ln2."],
   "B",
   "Mỗi hạt nhân chỉ phân rã một lần nên tổng số phân rã bằng số hạt nhân ban đầu N₀. "
   "Tổng năng lượng bằng N₀ nhân với năng lượng toả ra mỗi phân rã.",
   "Năng lượng tích luỹ của nguồn", K),

mc("Khi nói về phản ứng phân hạch dây chuyền, phát biểu nào SAI?",
   ["Mỗi phân hạch giải phóng 2–3 nơtron mới.",
    "Muốn duy trì phản ứng ổn định phải giữ hệ số nhân nơtron lớn hơn 1.",
    "Khối lượng nhiên liệu phải đạt giá trị tối thiểu gọi là khối lượng tới hạn.",
    "Nơtron chậm dễ gây phân hạch ²³⁵U hơn nơtron nhanh."],
   "B",
   "Muốn phản ứng duy trì ỔN ĐỊNH phải giữ k = 1. Với k > 1 phản ứng sẽ tăng nhanh mất kiểm soát. "
   "Ba phát biểu còn lại đều đúng.",
   "Phản ứng dây chuyền", TB, fig="h_sd_phan_hach", cap="Phản ứng dây chuyền"),

mc("Một chất phóng xạ có hằng số phóng xạ λ. Thời gian trung bình mà một hạt nhân tồn tại trước khi "
   "phân rã (gọi là thời gian sống trung bình) bằng",
   ["ln2/λ.", "1/λ.", "λ.", "λ·ln2."],
   "B",
   "Thời gian sống trung bình bằng 1/λ, lớn hơn chu kì bán rã T = ln2/λ ≈ 0,693/λ khoảng 1,44 lần.",
   "Hằng số phóng xạ", RK),
],
P2=[
ds("Một động cơ nhiệt hoạt động theo chu trình, mỗi chu trình nhận 2000 J từ nguồn nóng và "
   "thải 1400 J cho nguồn lạnh.",
   [("Công mà động cơ sinh ra trong mỗi chu trình là 600 J.", True,
     "Đúng. A = Q(nhận) − Q(thải) = 2000 − 1400 = 600 J."),
    ("Hiệu suất của động cơ là 30 %.", True,
     "Đúng. H = 600/2000 = 0,30."),
    ("Sau mỗi chu trình, nội năng của chất công tác trở về giá trị ban đầu.", True,
     "Đúng. Nội năng là hàm trạng thái, chu trình kín nên ΔU = 0."),
    ("Có thể chế tạo động cơ nhiệt đạt hiệu suất 100 % nếu cách nhiệt thật tốt.", False,
     "Sai. Động cơ nhiệt luôn phải thải một phần nhiệt cho nguồn lạnh, nên hiệu suất luôn nhỏ hơn "
     "100 % — đây là nội dung của nguyên lí thứ hai nhiệt động lực học.")],
   "Hiệu suất động cơ nhiệt", K),

ds("Một bình 20 L chứa khí lí tưởng ở 27 °C, áp suất 3,0·10⁵ Pa. Người ta bơm thêm khí cùng loại "
   "vào bình tới khi áp suất đạt 7,5·10⁵ Pa ở cùng nhiệt độ.",
   [("Khối lượng khí trong bình tỉ lệ thuận với áp suất khi V và T không đổi.", True,
     "Đúng. Từ pV = (m/M)RT, với V và T cố định thì m tỉ lệ thuận với p."),
    ("Khối lượng khí sau khi bơm gấp 2,5 lần khối lượng ban đầu.", True,
     "Đúng. 7,5/3,0 = 2,5."),
    ("Khối lượng khí bơm thêm bằng 1,5 lần khối lượng khí ban đầu.", True,
     "Đúng. 2,5 − 1 = 1,5 lần."),
    ("Trong quá trình bơm, có thể dùng phương trình p₁V₁/T₁ = p₂V₂/T₂.", False,
     "Sai. Phương trình trạng thái chỉ áp dụng cho một LƯỢNG KHÍ KHÔNG ĐỔI; ở đây lượng khí "
     "tăng lên nên phải dùng pV = nRT.")],
   "Phương trình Clapeyron", K),

ds("Một khung dây hình vuông cạnh 25 cm, khối lượng 50 g, điện trở 0,25 Ω rơi thẳng đứng đi ra "
   "khỏi vùng từ trường đều B = 0,50 T nằm ngang, vuông góc mặt phẳng khung. Lấy g = 10 m/s².",
   [("Ở tốc độ v, lực từ cản có độ lớn 0,0625·v (đơn vị SI).", True,
     "Đúng. F = B²a²v/R = (0,25 · 0,0625/0,25)·v = 0,0625v."),
    ("Tốc độ giới hạn của khung là 8,0 m/s.", True,
     "Đúng. 0,0625·v = m·g = 0,050 · 10 = 0,50 N ⇒ v = 8,0 m/s."),
    ("Khi đạt tốc độ giới hạn, khung chuyển động thẳng đều.", True,
     "Đúng. Lực từ cản cân bằng trọng lực nên hợp lực bằng 0."),
    ("Nếu tăng điện trở khung lên gấp đôi thì tốc độ giới hạn giảm một nửa.", False,
     "Sai. v = m·g·R/(B²a²) tỉ lệ THUẬN với R nên tốc độ giới hạn TĂNG gấp đôi.")],
   "Tốc độ giới hạn của khung rơi", K),

ds("Một mẫu chất phóng xạ nguyên chất có N₀ hạt nhân, chu kì bán rã T.",
   [("Số hạt phân rã trong chu kì thứ nhất là N₀/2.", True,
     "Đúng. Từ N₀ giảm còn N₀/2."),
    ("Số hạt phân rã trong chu kì thứ hai là N₀/4.", True,
     "Đúng. Từ N₀/2 giảm còn N₀/4."),
    ("Số hạt phân rã trong chu kì thứ tư là N₀/16.", True,
     "Đúng. Từ N₀/8 giảm còn N₀/16."),
    ("Tổng số hạt phân rã trong bốn chu kì đầu tiên là N₀/2 + N₀/4 + N₀/8 + N₀/16 = N₀.", False,
     "Sai. Tổng đó bằng 15N₀/16, đúng bằng phần đã rã sau 4 chu kì; vẫn còn N₀/16 hạt chưa rã.")],
   "Số hạt phân rã theo từng chu kì", K, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),
],
P3=[
sa("Một động cơ nhiệt nhận 5000 J nhiệt từ nguồn nóng và sinh công 1500 J trong mỗi chu trình. "
   "Nhiệt lượng thải cho nguồn lạnh bằng bao nhiêu jun?",
   "3500",
   "Bảo toàn năng lượng: Q(thải) = Q(nhận) − A = 5000 − 1500 = 3500 J.",
   "Hiệu suất động cơ nhiệt", K),

sa("Ở 27 °C, tốc độ trung bình của phân tử một khối khí là v. Phải nung nóng khí tới bao nhiêu độ "
   "Celsius để tốc độ trung bình tăng lên 3v?",
   "2427",
   "Động năng trung bình tỉ lệ với T và với bình phương tốc độ.\n"
   "Muốn v̄ tăng 3 lần thì T phải tăng 9 lần: T₂ = 9 · 300 = 2700 K.\n"
   "t₂ = 2700 − 273 = 2427 °C.",
   "Động năng phân tử", K),

sa("Một thanh dẫn dài 50 cm trượt đều với tốc độ 6,0 m/s trên hai ray nằm ngang vuông góc với từ "
   "trường đều thẳng đứng B = 0,30 T, điện trở toàn mạch 0,45 Ω. Công suất cơ học cần cung cấp để "
   "duy trì chuyển động bằng bao nhiêu oát (bỏ qua ma sát, làm tròn đến chữ số thập phân thứ nhất)?",
   "1,8",
   "e = B·ℓ·v = 0,30 · 0,50 · 6,0 = 0,90 V.\n"
   "i = e/R = 0,90/0,45 = 2,0 A.\n"
   "Bỏ qua ma sát nên toàn bộ công cơ học chuyển thành nhiệt: P = e·i = 0,90 · 2,0 = 1,8 W.",
   "Chuyển hoá năng lượng", K),

sa("Đặt điện áp xoay chiều có giá trị cực đại 200 V vào hai đầu điện trở 50 Ω. "
   "Công suất trung bình tiêu thụ trên điện trở bằng bao nhiêu oát?",
   "400",
   "Công suất trung bình tính theo giá trị hiệu dụng: P = U₀²/(2R).\n"
   "P = 200²/(2 · 50) = 40 000/100 = 400 W.",
   "Công suất dòng xoay chiều", K),

sa("Một nguồn phóng xạ có chu kì bán rã 30 năm. Sau bao nhiêu năm thì độ phóng xạ giảm còn 5 % "
   "giá trị ban đầu (làm tròn đến hàng đơn vị)? Lấy ln2 ≈ 0,693.",
   "130",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,05 ⇒ n = ln20/ln2 = 2,996/0,693 ≈ 4,322.\n"
   "t = 4,322 · 30 ≈ 130 năm.",
   "Định luật phóng xạ – dùng logarit", K),

sa("Trong chuỗi phân rã từ ²³⁸U tới ²⁰⁶Pb, số nơtron của hạt nhân giảm tổng cộng bao nhiêu đơn vị?",
   "22",
   "Số nơtron ban đầu: 238 − 92 = 146.\n"
   "Số nơtron cuối: 206 − 82 = 124.\n"
   "Giảm: 146 − 124 = 22.",
   "Chuỗi phân rã", K),
])


# =====================================================================  ĐỀ 15
DE15 = dict(
ma="TH-Đề 15", ten="ĐỀ THI THỬ SỐ 15", muc="Trung bình → Khó",
trongtam="Tổng duyệt nhóm Trung bình → Khó trước khi bước sang nhóm đề khó",
P1=[
mc("Một quả cân bằng chì khối lượng 0,50 kg rơi từ độ cao 30 m xuống nền cứng và dừng lại. "
   "Nếu 80 % cơ năng biến thành nội năng của quả cân thì nhiệt độ của nó tăng thêm "
   "(c(chì) = 130 J/(kg·K); g = 10 m/s²)",
   ["1,8 °C.", "2,3 °C.", "0,9 °C.", "3,7 °C."],
   "A",
   "Cơ năng ban đầu: W = m·g·h = 0,50 · 10 · 30 = 150 J.\n"
   "Nội năng tăng: ΔU = 0,80 · 150 = 120 J.\n"
   "ΔT = ΔU/(m·c) = 120/(0,50 · 130) = 120/65 ≈ 1,8 °C.",
   "Chuyển hoá cơ năng thành nội năng", K),

mc("Một khối khí lí tưởng giãn nở đẳng áp ở 2,0·10⁵ Pa, thể tích tăng từ 3,0 L lên 5,0 L. "
   "Công mà khí sinh ra bằng",
   ["200 J.", "400 J.", "600 J.", "1000 J."],
   "B",
   "Công của khí trong quá trình đẳng áp: A = p·ΔV = 2,0·10⁵ · (5,0 − 3,0)·10⁻³ "
   "= 2,0·10⁵ · 2,0·10⁻³ = 400 J.",
   "Công của chất khí", K),

mc("Trong quá trình ở câu trên, nếu khí nhận nhiệt lượng 1000 J thì nội năng của khí",
   ["giảm 400 J.", "tăng 600 J.", "tăng 1400 J.", "không đổi."],
   "B",
   "Khí SINH công nên A = −400 J; khí THU nhiệt nên Q = +1000 J.\n"
   "ΔU = A + Q = −400 + 1000 = +600 J.",
   "Định luật I nhiệt động lực học", K),

mc("Một lượng khí lí tưởng ở 27 °C, áp suất 1,0·10⁵ Pa. Nén đoạn nhiệt làm nhiệt độ tăng lên "
   "127 °C và thể tích giảm còn một nửa. Áp suất lúc sau bằng",
   ["1,33·10⁵ Pa.", "2,67·10⁵ Pa.", "2,00·10⁵ Pa.", "4,00·10⁵ Pa."],
   "B",
   "Dùng phương trình trạng thái (đúng cho mọi quá trình của một lượng khí xác định):\n"
   "p₂ = p₁ · (V₁/V₂) · (T₂/T₁) = 1,0·10⁵ · 2 · (400/300) ≈ 2,67·10⁵ Pa.",
   "Phương trình trạng thái", K),

mc("Một bình kín chứa hỗn hợp hai khí lí tưởng không phản ứng với nhau. Áp suất của hỗn hợp bằng",
   ["áp suất của khí có nhiều mol hơn.", "tổng áp suất riêng phần của hai khí.",
    "trung bình cộng hai áp suất riêng phần.", "hiệu hai áp suất riêng phần."],
   "B",
   "Mỗi khí gây áp suất độc lập lên thành bình; tổng các va chạm cho áp suất tổng bằng tổng "
   "áp suất riêng phần. Có thể suy ra từ pV = nRT với n là TỔNG số mol.",
   "Hỗn hợp khí lí tưởng", K),

mc("Một đoạn dây dẫn dài 60 cm mang dòng điện 5,0 A đặt trong từ trường đều B = 0,30 T. "
   "Khi quay dây trong mặt phẳng chứa B, lực từ lớn nhất tác dụng lên dây bằng",
   ["0,45 N.", "0,90 N.", "1,80 N.", "0,225 N."],
   "B",
   "Lực từ lớn nhất khi dây vuông góc với đường sức (α = 90°):\n"
   "F(max) = B·I·ℓ = 0,30 · 5,0 · 0,60 = 0,90 N.",
   "Lực từ", TB, fig="t_sd_goc_alpha", cap="Dây hợp góc α với đường sức"),

mc("Một khung dây phẳng 200 vòng, diện tích mỗi vòng 40 cm², đặt trong từ trường đều B = 0,50 T "
   "với pháp tuyến song song đường sức. Quay khung 180° trong 0,20 s. Suất điện động trung bình bằng",
   ["2,0 V.", "4,0 V.", "1,0 V.", "8,0 V."],
   "B",
   "Φ mỗi vòng đổi từ +B·S sang −B·S nên |ΔΦ| = 2·0,50·4,0·10⁻³ = 4,0·10⁻³ Wb.\n"
   "|e| = N·|ΔΦ|/Δt = 200 · 4,0·10⁻³/0,20 = 200 · 0,020 = 4,0 V.",
   "Faraday – quay khung", K),

mc("Một máy phát điện xoay chiều có 3 cặp cực, rôto quay 1200 vòng/phút. Tần số dòng điện phát ra "
   "bằng",
   ["20 Hz.", "60 Hz.", "40 Hz.", "120 Hz."],
   "B",
   "n = 1200/60 = 20 vòng/giây.\n"
   "f = p·n = 3 · 20 = 60 Hz.",
   "Máy phát nhiều cặp cực", TB),

mc("Một máy biến áp lí tưởng có hai cuộn thứ cấp độc lập. Cuộn sơ cấp 1000 vòng nối vào mạng 200 V; "
   "hai cuộn thứ cấp 50 vòng và 100 vòng nối với hai điện trở 5,0 Ω và 10 Ω. "
   "Công suất tổng mà máy tiêu thụ bằng",
   ["20 W.", "60 W.", "40 W.", "80 W."],
   "B",
   "Cuộn 50 vòng: U = 200 · 50/1000 = 10 V ⇒ P₁ = 10²/5,0 = 20 W.\n"
   "Cuộn 100 vòng: U = 200 · 100/1000 = 20 V ⇒ P₂ = 20²/10 = 40 W.\n"
   "Tổng: 20 + 40 = 60 W.",
   "Máy biến áp nhiều cuộn thứ cấp", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 2,0 MW đi xa với hiệu suất 95 %. Nếu muốn hiệu suất đạt 99 % mà giữ nguyên "
   "công suất và đường dây thì phải tăng điện áp lên gấp",
   ["2,0 lần.", "2,24 lần.", "5,0 lần.", "4,0 lần."],
   "B",
   "Hao phí giảm từ 5 % xuống 1 %, tức giảm 5 lần.\n"
   "Vì hao phí tỉ lệ nghịch với U² nên U phải tăng √5 ≈ 2,24 lần.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Hạt nhân ⁵⁶₂₆Fe có khối lượng 55,9349 u. Cho m(p) = 1,0073; m(n) = 1,0087 u. "
   "Năng lượng liên kết riêng của hạt nhân này xấp xỉ",
   ["7,9 MeV/nuclêôn.", "8,8 MeV/nuclêôn.",
    "9,6 MeV/nuclêôn.", "6,8 MeV/nuclêôn."],
   "B",
   "Fe-56 có 26 prôtôn và 30 nơtron.\n"
   "Tổng khối lượng nuclêôn: 26 · 1,0073 + 30 · 1,0087 = 26,1898 + 30,2610 = 56,4508 u.\n"
   "Δm = 56,4508 − 55,9349 = 0,5159 u.\n"
   "W(lk) = 0,5159 · 931,5 ≈ 480,6 MeV ⇒ ε = 480,6/56 ≈ 8,6 MeV/nuclêôn, "
   "gần nhất với 8,8 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", K, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chất phóng xạ nguyên chất có tỉ số giữa số hạt nhân đã rã và số hạt còn lại bằng 15. "
   "Thời gian đã trôi qua bằng",
   ["3 chu kì bán rã.", "4 chu kì bán rã.",
    "5 chu kì bán rã.", "15 chu kì bán rã."],
   "B",
   "2ⁿ − 1 = 15 ⇒ 2ⁿ = 16 ⇒ n = 4 chu kì bán rã.",
   "Tỉ số hạt nhân con và mẹ", TB),

mc("Một nguồn phóng xạ có độ phóng xạ 8,0·10¹¹ Bq, mỗi phân rã toả 3,0 MeV. Trong một giờ, "
   "năng lượng mà nguồn toả ra xấp xỉ (1 MeV = 1,6·10⁻¹³ J)",
   ["384 J.", "1382 J.", "230 J.", "3840 J."],
   "B",
   "Công suất: P = 8,0·10¹¹ · 3,0 · 1,6·10⁻¹³ = 8,0·10¹¹ · 4,8·10⁻¹³ = 0,384 W.\n"
   "Năng lượng trong 1 giờ: E = 0,384 · 3600 ≈ 1382 J.",
   "Công suất của nguồn phóng xạ", K),

mc("Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ. Số hạt nhân phân rã trong giờ thứ nhất so với "
   "số hạt phân rã trong 4 giờ đầu tiên chiếm khoảng",
   ["25,0 %.", "32,8 %.", "50,0 %.", "12,5 %."],
   "B",
   "Sau 1 giờ còn 2^(−0,25) ≈ 0,8409 ⇒ đã rã 15,91 % số hạt ban đầu.\n"
   "Sau 4 giờ (1 chu kì) đã rã 50 % số hạt ban đầu.\n"
   "Tỉ lệ: 15,91/50 ≈ 31,8 %, gần nhất với 32,8 %.",
   "Phân rã trong khoảng ngắn", RK),

mc("Trong phản ứng nhiệt hạch trên Mặt Trời, bốn hạt nhân hiđrô tạo thành một hạt nhân heli và "
   "toả 26,7 MeV. Khối lượng hụt đi trong mỗi phản ứng xấp xỉ",
   ["0,0187 u.", "0,0287 u.", "0,0387 u.", "0,0487 u."],
   "B",
   "Δm = ΔE/931,5 = 26,7/931,5 ≈ 0,0287 u.",
   "Hệ thức khối lượng – năng lượng", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Trong lò phản ứng hạt nhân, nếu chất làm chậm bị mất đi (ví dụ nước bị bốc hơi hết) thì "
   "phản ứng dây chuyền sẽ",
   ["mạnh lên.", "yếu đi hoặc dừng lại.",
    "không thay đổi.", "chuyển thành nhiệt hạch."],
   "B",
   "Không còn chất làm chậm thì nơtron giữ tốc độ cao, xác suất gây phân hạch ²³⁵U giảm mạnh, "
   "nên hệ số nhân nơtron giảm và phản ứng yếu đi. Đây là một cơ chế tự bảo vệ của lò dùng nước.",
   "Lò phản ứng hạt nhân", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Khi nói về liều bức xạ, phát biểu nào ĐÚNG?",
   ["Becơren đo mức nguy hại sinh học của bức xạ.",
    "Sivơ đo liều tương đương, có tính tới mức nguy hại sinh học của từng loại tia.",
    "Gray đo số phân rã mỗi giây.",
    "Ba đơn vị becơren, gray và sivơ là như nhau."],
   "B",
   "Becơren đo độ phóng xạ của nguồn; gray đo liều hấp thụ (năng lượng trên một kilôgam); "
   "sivơ đo liều tương đương, có nhân thêm hệ số trọng số tuỳ loại bức xạ.",
   "Đơn vị đo bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Một mẫu chất phóng xạ được chia thành hai phần không bằng nhau. So sánh chu kì bán rã của "
   "hai phần:",
   ["phần lớn có chu kì bán rã dài hơn.", "hai phần có cùng chu kì bán rã.",
    "phần nhỏ có chu kì bán rã dài hơn.", "không so sánh được."],
   "B",
   "Chu kì bán rã là hằng số đặc trưng của từng đồng vị, hoàn toàn không phụ thuộc khối lượng mẫu. "
   "Chỉ có ĐỘ PHÓNG XẠ của hai phần là khác nhau, tỉ lệ với khối lượng.",
   "Đặc điểm của chu kì bán rã", TB),
],
P2=[
ds("Một khối khí lí tưởng giãn nở đẳng áp ở áp suất 1,5·10⁵ Pa, thể tích tăng từ 2,0 L lên 6,0 L. "
   "Trong quá trình đó khí nhận nhiệt lượng 1200 J.",
   [("Công mà khí sinh ra bằng 600 J.", True,
     "Đúng. A = p·ΔV = 1,5·10⁵ · 4,0·10⁻³ = 600 J."),
    ("Nội năng của khí tăng 600 J.", True,
     "Đúng. ΔU = A + Q = (−600) + 1200 = +600 J."),
    ("Nhiệt độ tuyệt đối của khí tăng gấp ba lần.", True,
     "Đúng. Đẳng áp nên V tỉ lệ thuận với T; V tăng 3 lần nên T cũng tăng 3 lần."),
    ("Nếu quá trình là đẳng tích với cùng nhiệt lượng 1200 J thì nội năng cũng chỉ tăng 600 J.", False,
     "Sai. Đẳng tích thì A = 0 nên ΔU = Q = 1200 J, tức tăng gấp đôi so với trường hợp đẳng áp.")],
   "Công của chất khí và định luật I", K),

ds("Một khung dây phẳng 250 vòng, diện tích mỗi vòng 50 cm², đặt trong từ trường đều B = 0,40 T "
   "với pháp tuyến song song đường sức.",
   [("Từ thông qua mỗi vòng lúc đầu là 2,0·10⁻³ Wb.", True,
     "Đúng. Φ = 0,40 · 5,0·10⁻³ = 2,0·10⁻³ Wb."),
    ("Nếu quay khung 90° trong 0,25 s thì suất điện động trung bình bằng 2,0 V.", True,
     "Đúng. |ΔΦ| = 2,0·10⁻³ Wb ⇒ |e| = 250 · 2,0·10⁻³/0,25 = 2,0 V."),
    ("Nếu quay khung 180° trong cùng thời gian thì suất điện động trung bình bằng 4,0 V.", True,
     "Đúng. Từ thông đổi dấu nên |ΔΦ| gấp đôi, suất điện động cũng gấp đôi."),
    ("Nếu quay khung 360° trong cùng thời gian thì suất điện động trung bình bằng 8,0 V.", False,
     "Sai. Quay trọn 360° thì từ thông trở về giá trị ban đầu nên ΔΦ = 0 và suất điện động "
     "TRUNG BÌNH bằng 0 (dù suất điện động tức thời vẫn khác không trong quá trình quay).")],
   "Faraday – quay khung", K),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng nối vào mạng 200 V và hai cuộn thứ cấp độc "
   "lập 50 vòng và 100 vòng, nối lần lượt với hai điện trở 5,0 Ω và 10 Ω.",
   [("Điện áp ở cuộn 50 vòng là 10 V.", True,
     "Đúng. U = 200 · 50/1000 = 10 V."),
    ("Công suất tiêu thụ ở cuộn 50 vòng là 20 W.", True,
     "Đúng. P = U²/R = 100/5,0 = 20 W."),
    ("Công suất tiêu thụ ở cuộn 100 vòng là 40 W.", True,
     "Đúng. U = 20 V ⇒ P = 400/10 = 40 W."),
    ("Cường độ dòng điện ở cuộn sơ cấp là 0,60 A.", False,
     "Sai. Tổng công suất là 60 W nên I₁ = 60/200 = 0,30 A.")],
   "Máy biến áp nhiều cuộn thứ cấp", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Một nguồn phóng xạ có độ phóng xạ 5,0·10¹¹ Bq, mỗi phân rã toả 2,0 MeV, chu kì bán rã 10 giờ. "
   "Cho 1 MeV = 1,6·10⁻¹³ J.",
   [("Công suất ban đầu của nguồn là 0,16 W.", True,
     "Đúng. P = 5,0·10¹¹ · 2,0 · 1,6·10⁻¹³ = 5,0·10¹¹ · 3,2·10⁻¹³ = 0,16 W."),
    ("Sau 10 giờ, công suất của nguồn còn 0,08 W.", True,
     "Đúng. Sau một chu kì bán rã, độ phóng xạ và do đó công suất giảm một nửa."),
    ("Sau 30 giờ, công suất của nguồn còn 0,02 W.", True,
     "Đúng. n = 3 ⇒ P = 0,16/8 = 0,02 W."),
    ("Năng lượng nguồn toả ra trong giờ đầu tiên đúng bằng 0,16 · 3600 = 576 J.", False,
     "Sai. Đó chỉ là giá trị ƯỚC LƯỢNG khi coi công suất không đổi. Thực tế công suất giảm dần "
     "trong giờ đó nên năng lượng thực sự nhỏ hơn 576 J.")],
   "Công suất của nguồn phóng xạ", K),
],
P3=[
sa("Một quả cân bằng chì khối lượng 0,80 kg rơi từ độ cao 26 m xuống nền cứng và dừng lại. "
   "Nếu 65 % cơ năng biến thành nội năng của quả cân thì nhiệt độ của nó tăng thêm bao nhiêu độ "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho c(chì) = 130 J/(kg·K); g = 10 m/s².",
   "1,3",
   "Cơ năng: W = 0,80 · 10 · 26 = 208 J.\n"
   "Nội năng tăng: ΔU = 0,65 · 208 = 135,2 J.\n"
   "ΔT = 135,2/(0,80 · 130) = 135,2/104 = 1,3 °C.",
   "Chuyển hoá cơ năng thành nội năng", K),

sa("Một bình kín chứa hỗn hợp gồm 0,20 mol khí ôxi và 0,30 mol khí nitơ, thể tích 8,31 L, "
   "nhiệt độ 27 °C. Áp suất của hỗn hợp bằng bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, "
   "làm tròn đến chữ số thập phân thứ nhất)? Cho R = 8,31 J/(mol·K).",
   "1,5",
   "Tổng số mol: n = 0,20 + 0,30 = 0,50 mol.\n"
   "p = nRT/V = 0,50 · 8,31 · 300/(8,31·10⁻³) = 1246,5/8,31·10⁻³ = 1,5·10⁵ Pa.",
   "Hỗn hợp khí lí tưởng", K),

sa("Một đoạn dây dẫn dài 80 cm mang dòng điện 4,0 A đặt trong từ trường đều B = 0,25 T. "
   "Lực từ lớn nhất tác dụng lên dây bằng bao nhiêu niutơn?",
   "0,8",
   "Lực từ lớn nhất khi dây vuông góc đường sức: F = B·I·ℓ = 0,25 · 4,0 · 0,80 = 0,80 N.",
   "Lực từ", TB),

sa("Một cuộn dây 400 vòng, điện trở 2,5 Ω, diện tích mỗi vòng 25 cm², đặt vuông góc với từ trường "
   "đều. Cảm ứng từ giảm đều 0,50 T. Điện lượng chuyển qua tiết diện dây bằng bao nhiêu culông "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,20",
   "|ΔΦ| mỗi vòng = ΔB·S = 0,50 · 2,5·10⁻³ = 1,25·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 400 · 1,25·10⁻³/2,5 = 0,50/2,5 = 0,20 C.",
   "Điện lượng cảm ứng", K),

sa("Trong phản ứng nhiệt hạch, mỗi phản ứng toả 17,6 MeV. Khối lượng hụt đi trong mỗi phản ứng bằng "
   "bao nhiêu u (làm tròn đến chữ số thập phân thứ tư)? Cho 1 u·c² = 931,5 MeV.",
   "0,0189",
   "Δm = ΔE/931,5 = 17,6/931,5 ≈ 0,018895 ≈ 0,0189 u.",
   "Hệ thức khối lượng – năng lượng", K),

sa("Một mẫu chất phóng xạ nguyên chất có tỉ số giữa số hạt nhân đã phân rã và số hạt nhân còn lại "
   "bằng 31. Thời gian đã trôi qua bằng bao nhiêu lần chu kì bán rã?",
   "5",
   "2ⁿ − 1 = 31 ⇒ 2ⁿ = 32 = 2⁵ ⇒ n = 5 chu kì bán rã.",
   "Tỉ số hạt nhân con và mẹ", TB),
])


NHOM = dict(
    ten_nhom="ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG  (Đề 11 – 15)",
    mo_ta="Năm đề mức Trung bình đến Khó, tăng dần tỉ trọng câu vận dụng nhiều bước",
    pham_vi=(
        "Chương I. Vật lí nhiệt  •  Chương II. Khí lí tưởng  •  "
        "Chương III. Từ trường  •  Chương IV. Vật lí hạt nhân\n"
        "Mỗi đề gồm 28 câu / 40 lệnh hỏi, thời gian 50 phút, thang điểm 10.\n"
        "Hằng số: c(nước) = 4200, c(chì) = 130, c(sắt) = 460 J/(kg·K); λ(nước đá) = 3,4·10⁵ J/kg; "
        "L(nước) = 2,26·10⁶ J/kg; g = 10 m/s²; R = 8,31 J/(mol·K); Nₐ = 6,02·10²³ mol⁻¹; "
        "1 u·c² = 931,5 MeV; 1 MeV = 1,6·10⁻¹³ J; π ≈ 3,1416; √2 ≈ 1,414; ln2 ≈ 0,693."),
    tests=[DE11, DE12, DE13, DE14, DE15],
)
