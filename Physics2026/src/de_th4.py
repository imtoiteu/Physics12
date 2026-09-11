# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.  Đề 16 – 20 (Khó)."""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 16
DE16 = dict(
ma="TH-Đề 16", ten="ĐỀ THI THỬ SỐ 16", muc="Khó",
trongtam="Bài toán nhiều ràng buộc, bảo toàn động lượng, hệ truyền tải",
P1=[
mc("Một bình cách nhiệt chứa 2,0 kg nước ở 20 °C. Người ta thả vào đó một cục nước đá ở −10 °C. "
   "Khối lượng nước đá lớn nhất để toàn bộ đá tan hết xấp xỉ "
   "(c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg)",
   ["0,49 kg.", "0,465 kg.", "0,52 kg.", "0,58 kg."],
   "B",
   "Nhiệt nước nhả ra tối đa: Q = 2,0 · 4200 · 20 = 168 000 J.\n"
   "Nhiệt cần cho m kg đá: hâm từ −10 °C lên 0 °C rồi tan hết:\n"
   "Q = m·2100·10 + m·3,4·10⁵ = m·(21 000 + 340 000) = 361 000·m.\n"
   "361 000·m ≤ 168 000 ⇒ m ≤ 0,4654 kg, tức khối lượng lớn nhất là 0,465 kg.",
   "Biện luận điều kiện", RK),

mc("Một khối khí lí tưởng thực hiện chu trình gồm ba quá trình: đẳng nhiệt giãn nở từ V tới 3V, "
   "đẳng tích hạ áp suất, đẳng áp nén về trạng thái đầu. Trên đồ thị (p, V), diện tích hình giới hạn "
   "bởi chu trình biểu thị",
   ["nội năng của khí.", "công mà khí sinh ra trong một chu trình.",
    "nhiệt độ trung bình.", "số mol khí."],
   "B",
   "Trên đồ thị (p, V), diện tích dưới đường biểu diễn bằng công. Với chu trình kín, diện tích hình "
   "giới hạn chính là công tổng cộng mà khí sinh ra trong một chu trình.",
   "Chu trình kín", K, fig="k_dt_chutrinh", cap="Chu trình trong hệ (p, V)"),

mc("Hai bình A (thể tích V) và B (thể tích 2V) nối bằng ống nhỏ có khoá, cùng ở 27 °C. "
   "Bình A chứa khí ở 6,0·10⁵ Pa, bình B chân không. Mở khoá, áp suất chung bằng",
   ["3,0·10⁵ Pa.", "2,0·10⁵ Pa.", "1,5·10⁵ Pa.", "4,0·10⁵ Pa."],
   "B",
   "Thể tích tổng là V + 2V = 3V, gấp 3 lần thể tích ban đầu.\n"
   "Đẳng nhiệt: p₂ = p₁·V/(3V) = 6,0·10⁵/3 = 2,0·10⁵ Pa.",
   "Định luật Boyle", K),

mc("Một xi lanh nằm ngang được chia thành hai phần bằng một pit-tông mỏng, mỗi phần dài 40 cm và "
   "chứa cùng một loại khí ở cùng áp suất, cùng nhiệt độ. Nung nóng phần bên trái để nhiệt độ tuyệt "
   "đối tăng gấp đôi, giữ phần bên phải ở nhiệt độ cũ. Pit-tông dịch chuyển một đoạn",
   ["10,0 cm.", "13,3 cm.", "20,0 cm.", "6,7 cm."],
   "B",
   "Gọi x là độ dịch chuyển của pit-tông về phía phải. Áp suất hai bên luôn bằng nhau (gọi là p').\n"
   "Phần phải (đẳng nhiệt): p·40 = p'·(40 − x).\n"
   "Phần trái: p·40/T = p'·(40 + x)/(2T) ⇒ p·80 = p'·(40 + x).\n"
   "Chia hai phương trình: 2 = (40 + x)/(40 − x) ⇒ 80 − 2x = 40 + x ⇒ 3x = 40 ⇒ x ≈ 13,3 cm.",
   "Xi lanh hai ngăn", RK),

mc("Ở cùng nhiệt độ, hai khối khí khác loại có cùng số phân tử trong cùng thể tích. So sánh áp suất "
   "của chúng:",
   ["khí nặng hơn có áp suất lớn hơn.", "hai áp suất bằng nhau.",
    "khí nhẹ hơn có áp suất lớn hơn.", "không so sánh được."],
   "B",
   "p = (2/3)·μ·W̄ₐ. Cùng thể tích và cùng số phân tử nên μ bằng nhau; cùng nhiệt độ nên W̄ₐ bằng "
   "nhau. Vậy áp suất bằng nhau, đúng như phương trình pV = nRT cho thấy.",
   "Áp suất theo mô hình động học", K),

mc("Một thanh dẫn dài 40 cm, khối lượng 100 g trượt trên hai ray nghiêng 30° có hệ số ma sát 0,20, "
   "trong từ trường đều B = 0,50 T vuông góc mặt phẳng nghiêng, điện trở toàn mạch 0,20 Ω. "
   "Tốc độ lớn nhất của thanh bằng (g = 10 m/s²; cos30° ≈ 0,866)",
   ["1,25 m/s.", "1,63 m/s.", "2,50 m/s.", "3,00 m/s."],
   "B",
   "Thành phần trọng lực dọc mặt nghiêng: m·g·sin30° = 0,100 · 10 · 0,50 = 0,50 N.\n"
   "Lực ma sát: μ·m·g·cos30° = 0,20 · 0,100 · 10 · 0,866 = 0,173 N.\n"
   "Hợp lực kéo còn lại: 0,50 − 0,173 = 0,327 N.\n"
   "Lực từ cản ở tốc độ v: B²ℓ²v/R = (0,25 · 0,16/0,20)·v = 0,20v.\n"
   "Tốc độ lớn nhất khi gia tốc bằng 0: 0,20·v = 0,327 ⇒ v ≈ 1,63 m/s.",
   "Thanh dẫn trên mặt nghiêng có ma sát", RK, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trên hai ray nghiêng"),

mc("Điện năng được truyền từ nhà máy tới nơi tiêu thụ qua máy tăng áp tỉ số 1 : 20 và máy hạ áp "
   "tỉ số 25 : 1. Điện áp máy phát 4,0 kV, công suất truyền 2,0 MW, điện trở đường dây 10 Ω. "
   "Điện áp ở đầu ra máy hạ áp xấp xỉ",
   ["3200 V.", "3190 V.", "3000 V.", "3300 V."],
   "B",
   "Điện áp đầu đường dây: 20 · 4,0 = 80 kV.\n"
   "Dòng trên dây: I = 2,0·10⁶/(80·10³) = 25 A.\n"
   "Sụt áp trên dây: ΔU = 10 · 25 = 250 V.\n"
   "Điện áp cuối dây: 80 000 − 250 = 79 750 V.\n"
   "Qua máy hạ áp 25 : 1 ⇒ U(ra) = 79 750/25 = 3190 V.",
   "Hệ truyền tải hai cấp biến áp", RK, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

mc("Một khung dây vuông cạnh a, điện trở R, được kéo đều ra khỏi vùng từ trường đều B với tốc độ v. "
   "Công của lực kéo trong suốt quá trình bằng",
   ["B²a²v/R.", "B²a³v/R.", "B·a·v·R.", "B²a²v²/R."],
   "B",
   "Lực kéo cân bằng lực từ cản: F = B²a²v/R.\n"
   "Quãng đường kéo bằng cạnh khung: s = a.\n"
   "A = F·s = B²a³v/R.",
   "Năng lượng trong cảm ứng điện từ", RK),

mc("Dùng prôtôn động năng 5,45 MeV bắn vào ⁹₄Be đứng yên, sinh ra hạt α (động năng 4,00 MeV, "
   "bay vuông góc với prôtôn) và hạt nhân ⁶₃Li. Động năng hạt liti xấp xỉ",
   ["2,13 MeV.", "3,58 MeV.", "4,00 MeV.", "5,45 MeV."],
   "B",
   "Hạt α vuông góc prôtôn nên p(Li)² = p(p)² + p(α)².\n"
   "Với p² = 2mW và m tỉ lệ A: 6·W(Li) = 1·5,45 + 4·4,00 = 21,45.\n"
   "W(Li) = 21,45/6 ≈ 3,58 MeV.",
   "Bảo toàn động lượng hai chiều", RK),

mc("Với bài toán trên, phản ứng toả ra năng lượng xấp xỉ",
   ["1,13 MeV.", "2,13 MeV.", "3,58 MeV.", "9,45 MeV."],
   "B",
   "ΔE = (W(α) + W(Li)) − W(p) = (4,00 + 3,58) − 5,45 = 7,58 − 5,45 = 2,13 MeV.",
   "Bảo toàn năng lượng trong phản ứng", RK),

mc("Một mẫu chứa hai đồng vị X (T = 2,0 giờ) và Y (T = 6,0 giờ). Ban đầu số hạt nhân X gấp 4 lần Y. "
   "Sau bao lâu thì số hạt nhân hai đồng vị bằng nhau?",
   ["4,0 giờ.", "6,0 giờ.", "8,0 giờ.", "12,0 giờ."],
   "B",
   "4N₀·2^(−t/2) = N₀·2^(−t/6) ⇒ 2² · 2^(−t/2) = 2^(−t/6).\n"
   "So sánh số mũ: 2 − t/2 = −t/6 ⇒ 2 = t/2 − t/6 = t/3 ⇒ t = 6,0 giờ.",
   "Hỗn hợp hai đồng vị", RK),

mc("Một mẫu đá chứa ²³⁸U (T = 4,5 tỉ năm) và ²⁰⁶Pb với tỉ số SỐ HẠT NHÂN Pb/U bằng 1,0. "
   "Tuổi của mẫu đá bằng",
   ["2,25 tỉ năm.", "4,5 tỉ năm.", "9,0 tỉ năm.", "1,5 tỉ năm."],
   "B",
   "Tỉ số con/mẹ bằng 2ⁿ − 1 = 1,0 ⇒ 2ⁿ = 2 ⇒ n = 1 chu kì.\n"
   "t = 1 · 4,5 = 4,5 tỉ năm.",
   "Xác định tuổi mẫu đá", K),

mc("Một nguồn nhiệt đồng vị chứa 0,50 gam ²¹⁰Po (T = 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Công suất ban đầu xấp xỉ (Nₐ = 6,02·10²³; 1 MeV = 1,6·10⁻¹³ J)",
   ["36 W.", "72 W.", "144 W.", "18 W."],
   "B",
   "N₀ = (0,50/210)·6,02·10²³ ≈ 1,433·10²¹ hạt.\n"
   "T = 138 · 86 400 ≈ 1,192·10⁷ s ⇒ λ ≈ 5,81·10⁻⁸ s⁻¹.\n"
   "H₀ = λN₀ ≈ 8,33·10¹³ Bq.\n"
   "P = H₀ · 5,4 · 1,6·10⁻¹³ ≈ 8,33·10¹³ · 8,64·10⁻¹³ ≈ 72 W.",
   "Công suất của nguồn phóng xạ", RK),

mc("Một mẫu chất phóng xạ nguyên chất sau thời gian t₁ còn 60 % số hạt nhân. Sau thời gian 2·t₁, "
   "số hạt nhân còn lại bằng",
   ["30 %.", "36 %.", "40 %.", "20 %."],
   "B",
   "Trong những khoảng thời gian bằng nhau, số hạt giảm theo cùng một TỈ LỆ.\n"
   "Sau 2t₁: (0,60)² = 0,36 = 36 %.",
   "Bản chất hàm mũ của phân rã", K),

mc("Một hạt nhân đứng yên phân rã thành hai hạt có số khối 4 và 218, toả ra năng lượng ΔE. "
   "Tỉ số động năng của hạt nhẹ và hạt nặng bằng",
   ["4 : 218.", "218 : 4.", "1 : 1.", "√(218/4)."],
   "B",
   "Cùng độ lớn động lượng nên W = p²/(2m) tỉ lệ nghịch với khối lượng:\n"
   "W(nhẹ)/W(nặng) = 218/4 = 54,5.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Trong chu trình của một động cơ nhiệt, nếu tăng nhiệt độ nguồn nóng mà giữ nguyên nhiệt độ "
   "nguồn lạnh thì hiệu suất lí thuyết cực đại",
   ["giảm.", "tăng.", "không đổi.", "bằng 100 %."],
   "B",
   "Hiệu suất lí thuyết cực đại của động cơ nhiệt tăng khi chênh lệch nhiệt độ giữa hai nguồn "
   "tăng lên. Đó là lí do các nhà máy nhiệt điện luôn tìm cách nâng nhiệt độ hơi vào tua bin.",
   "Hiệu suất động cơ nhiệt", K),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu H₀. Tổng số phân rã trong toàn bộ quá trình "
   "cho tới khi mẫu phân rã hết bằng",
   ["H₀·ln2.", "H₀·T/ln2.", "H₀·T.", "H₀/T."],
   "B",
   "Tổng số phân rã bằng số hạt nhân ban đầu N₀ = H₀/λ = H₀·T/ln2.",
   "Độ phóng xạ và tổng số phân rã", RK),

mc("Khi so sánh hai phương pháp xác định tuổi bằng ¹⁴C và bằng cặp ²³⁸U – ²⁰⁶Pb, nhận xét nào ĐÚNG?",
   ["Cả hai đều dùng tốt cho mẫu vật vài nghìn năm tuổi.",
    "¹⁴C hợp cho mẫu vài nghìn năm, cặp U–Pb hợp cho đá hàng trăm triệu tới hàng tỉ năm.",
    "Cặp U–Pb hợp cho mẫu gỗ mới chặt.",
    "¹⁴C hợp cho đá hàng tỉ năm."],
   "B",
   "Phương pháp chỉ chính xác khi khoảng thời gian cần đo cùng bậc với chu kì bán rã. "
   "¹⁴C có T = 5730 năm, còn ²³⁸U có T = 4,5 tỉ năm.",
   "Lựa chọn đồng vị xác định tuổi", K, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),
],
P2=[
ds("Thả m kg nước đá ở −10 °C vào 1,5 kg nước ở 25 °C trong bình cách nhiệt. "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng tối đa mà nước có thể nhả ra là 157,5 kJ.", True,
     "Đúng. Q = 1,5 · 4200 · 25 = 157 500 J."),
    ("Nhiệt lượng cần để m kg đá từ −10 °C tan hết là 361 000·m (J).", True,
     "Đúng. m·2100·10 + m·3,4·10⁵ = m·(21 000 + 340 000) = 361 000·m."),
    ("Khối lượng nước đá lớn nhất để đá tan hết xấp xỉ 0,436 kg.", True,
     "Đúng. 361 000·m ≤ 157 500 ⇒ m ≤ 0,4363 kg."),
    ("Nếu thả 0,60 kg nước đá thì nhiệt độ cân bằng vẫn cao hơn 0 °C.", False,
     "Sai. 0,60 kg cần 216 600 J, lớn hơn 157 500 J nên đá chỉ tan một phần và nhiệt độ cân bằng "
     "đúng bằng 0 °C.")],
   "Biện luận điều kiện", RK),

ds("Một xi lanh nằm ngang được chia thành hai phần bằng pit-tông mỏng, mỗi phần dài 30 cm, chứa "
   "cùng một loại khí ở cùng áp suất và cùng nhiệt độ T. Nung phần bên trái lên 2T, giữ phần phải "
   "ở T.",
   [("Áp suất hai bên pit-tông luôn bằng nhau khi pit-tông cân bằng.", True,
     "Đúng. Pit-tông mỏng, tự do nên điều kiện cân bằng đòi hỏi áp suất hai bên bằng nhau."),
    ("Phần bên phải biến đổi theo quá trình đẳng nhiệt.", True,
     "Đúng. Nhiệt độ phần phải giữ nguyên T."),
    ("Pit-tông dịch chuyển về phía bên phải 10 cm.", True,
     "Đúng. Đặt x là độ dịch: p·30 = p'·(30 − x) và p·60 = p'·(30 + x). "
     "Chia hai vế: 2 = (30 + x)/(30 − x) ⇒ 60 − 2x = 30 + x ⇒ x = 10 cm."),
    ("Sau khi cân bằng, áp suất chung nhỏ hơn áp suất ban đầu.", False,
     "Sai. Phần phải bị nén từ 30 cm xuống 20 cm nên áp suất tăng: p' = p·30/20 = 1,5p.")],
   "Xi lanh hai ngăn", RK),

ds("Điện năng truyền từ nhà máy tới khu dân cư qua máy tăng áp tỉ số 1 : 25 rồi máy hạ áp tỉ số "
   "20 : 1. Điện áp máy phát 5,0 kV, công suất truyền 3,0 MW, điện trở đường dây 8,0 Ω.",
   [("Điện áp ở đầu đường dây là 125 kV.", True,
     "Đúng. 25 · 5,0 = 125 kV."),
    ("Cường độ dòng điện trên đường dây là 24 A.", True,
     "Đúng. I = 3,0·10⁶/(125·10³) = 24 A."),
    ("Độ sụt áp trên đường dây là 192 V.", True,
     "Đúng. ΔU = R·I = 8,0 · 24 = 192 V."),
    ("Điện áp ở đầu ra của máy hạ áp là 6250 V.", False,
     "Sai. Điện áp cuối dây là 125 000 − 192 = 124 808 V; qua máy hạ áp 20 : 1 cho "
     "124 808/20 ≈ 6240 V chứ không phải 6250 V.")],
   "Hệ truyền tải hai cấp biến áp", RK, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

ds("Dùng prôtôn có động năng 5,45 MeV bắn vào hạt nhân ⁹₄Be đứng yên, sinh ra hạt α có động năng "
   "4,00 MeV bay vuông góc với phương prôtôn và hạt nhân ⁶₃Li. Coi khối lượng tỉ lệ số khối.",
   [("Phản ứng bảo toàn số khối và điện tích.", True,
     "Đúng. 1 + 9 = 4 + 6 và 1 + 4 = 2 + 3."),
    ("Ba vectơ động lượng tạo thành một tam giác vuông.", True,
     "Đúng. Vì hạt α vuông góc với prôtôn nên p(Li) là cạnh huyền."),
    ("Động năng hạt liti xấp xỉ 3,58 MeV.", True,
     "Đúng. 6·W(Li) = 1·5,45 + 4·4,00 = 21,45 ⇒ W(Li) ≈ 3,58 MeV."),
    ("Vì tổng động năng sau lớn hơn trước nên phản ứng thu năng lượng.", False,
     "Sai. Tổng động năng TĂNG nghĩa là phản ứng TOẢ năng lượng 2,13 MeV, lấy từ phần khối lượng "
     "nghỉ bị hụt đi.")],
   "Bảo toàn động lượng hai chiều", RK),
],
P3=[
sa("Thả m kg nước đá ở −20 °C vào 2,5 kg nước ở 30 °C trong bình cách nhiệt. Khối lượng nước đá "
   "lớn nhất để đá tan hết bằng bao nhiêu kilôgam (làm tròn đến chữ số thập phân thứ ba)? "
   "Cho c(đá) = 2100, c(nước) = 4200 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   "0,825",
   "Nhiệt nước nhả ra tối đa: Q = 2,5 · 4200 · 30 = 315 000 J.\n"
   "Nhiệt cần cho m kg đá: m·2100·20 + m·3,4·10⁵ = m·(42 000 + 340 000) = 382 000·m.\n"
   "382 000·m ≤ 315 000 ⇒ m ≤ 0,8246 ≈ 0,825 kg.",
   "Biện luận điều kiện", RK),

sa("Hai bình A (thể tích V) và B (thể tích 3V) nối bằng ống nhỏ có khoá, cùng nhiệt độ. "
   "Bình A chứa khí ở 8,0·10⁵ Pa, bình B chân không. Mở khoá, áp suất chung bằng bao nhiêu "
   "(viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x)?",
   "2",
   "Thể tích tổng: V + 3V = 4V, gấp 4 lần thể tích ban đầu.\n"
   "Đẳng nhiệt: p₂ = 8,0·10⁵/4 = 2,0·10⁵ Pa.",
   "Định luật Boyle", K),

sa("Một xi lanh nằm ngang chia đôi bằng pit-tông mỏng, mỗi phần dài 50 cm chứa cùng loại khí ở cùng "
   "áp suất, cùng nhiệt độ T. Nung phần trái lên 3T, giữ phần phải ở T. "
   "Pit-tông dịch chuyển bao nhiêu centimét?",
   "25",
   "Đặt x là độ dịch về phía phải.\n"
   "Phần phải (đẳng nhiệt): p·50 = p'·(50 − x).\n"
   "Phần trái: p·50/T = p'·(50 + x)/(3T) ⇒ p·150 = p'·(50 + x).\n"
   "Chia hai phương trình: 3 = (50 + x)/(50 − x) ⇒ 150 − 3x = 50 + x ⇒ 4x = 100 ⇒ x = 25 cm.",
   "Xi lanh hai ngăn", RK),

sa("Một khung dây vuông cạnh 30 cm, điện trở 0,60 Ω, được kéo đều với tốc độ 2,0 m/s ra khỏi vùng "
   "từ trường đều B = 0,60 T. Công của lực kéo trong suốt quá trình bằng bao nhiêu milijun "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "32,4",
   "Lực kéo: F = B²a²v/R = (0,36 · 0,090/0,60) · 2,0 = 0,054 · 2,0 = 0,108 N.\n"
   "Quãng đường: s = a = 0,30 m.\n"
   "A = F·s = 0,108 · 0,30 = 0,0324 J = 32,4 mJ.",
   "Năng lượng trong cảm ứng điện từ", RK),

sa("Một mẫu chứa hai đồng vị X (chu kì bán rã 3,0 giờ) và Y (chu kì bán rã 9,0 giờ). "
   "Ban đầu số hạt nhân X gấp 16 lần Y. Sau bao nhiêu giờ thì số hạt nhân hai đồng vị bằng nhau?",
   "18",
   "16N₀·2^(−t/3) = N₀·2^(−t/9) ⇒ 2⁴ · 2^(−t/3) = 2^(−t/9).\n"
   "So sánh số mũ: 4 − t/3 = −t/9 ⇒ 4 = t/3 − t/9 = 2t/9 ⇒ t = 18 giờ.",
   "Hỗn hợp hai đồng vị", RK),

sa("Một nguồn nhiệt đồng vị chứa 1,5 gam ²¹⁰Po (chu kì bán rã 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Công suất ban đầu của nguồn bằng bao nhiêu oát (làm tròn đến hàng đơn vị)? "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693.",
   "216",
   "N₀ = (1,5/210)·6,02·10²³ ≈ 4,300·10²¹ hạt.\n"
   "T = 138 · 86 400 ≈ 1,192·10⁷ s ⇒ λ = 0,693/1,192·10⁷ ≈ 5,81·10⁻⁸ s⁻¹.\n"
   "H₀ = λN₀ ≈ 2,499·10¹⁴ Bq.\n"
   "P = H₀ · 5,4 · 1,6·10⁻¹³ = 2,499·10¹⁴ · 8,64·10⁻¹³ ≈ 216 W.",
   "Công suất của nguồn phóng xạ", RK),
])


# =====================================================================  ĐỀ 17
DE17 = dict(
ma="TH-Đề 17", ten="ĐỀ THI THỬ SỐ 17", muc="Khó",
trongtam="Hiệu suất hệ thống, chu trình nhiều giai đoạn, năng lượng tích luỹ của nguồn phóng xạ",
P1=[
mc("Một bình nước nóng năng lượng mặt trời hấp thụ trung bình 600 W. Hiệu suất hấp thụ 60 %. "
   "Thời gian để đun 80 kg nước từ 25 °C lên 45 °C xấp xỉ",
   ["3,1 giờ.", "5,2 giờ.", "1,9 giờ.", "9,3 giờ."],
   "B",
   "Nhiệt lượng có ích: Q = 80 · 4200 · 20 = 6,72·10⁶ J.\n"
   "Công suất có ích: 600 · 0,60 = 360 W.\n"
   "t = 6,72·10⁶/360 ≈ 18 667 s ≈ 5,2 giờ.",
   "Hiệu suất và công suất", K, fig="n_sd_binhnuocnong", cap="Bình nước nóng"),

mc("Một khối khí lí tưởng đi qua ba trạng thái: (1) p = 1,0·10⁵ Pa, V = 2,0 L, T = 300 K; "
   "(2) đẳng tích tới 600 K; (3) đẳng nhiệt tới V = 4,0 L. Áp suất ở trạng thái (3) bằng",
   ["1,0·10⁵ Pa.", "0,50·10⁵ Pa.", "2,0·10⁵ Pa.", "4,0·10⁵ Pa."],
   "A",
   "Trạng thái (2): đẳng tích, T tăng gấp đôi ⇒ p₂ = 2,0·10⁵ Pa, V = 2,0 L.\n"
   "Trạng thái (3): đẳng nhiệt, V tăng gấp đôi ⇒ p₃ = 2,0·10⁵/2 = 1,0·10⁵ Pa.",
   "Chuỗi quá trình", K),

mc("Một xi lanh thẳng đứng chứa khí, pit-tông khối lượng m tiết diện S nằm cân bằng. "
   "Nếu lật ngược xi lanh cho miệng xuống dưới (nhiệt độ không đổi) thì thể tích khí",
   ["giảm.", "tăng.", "không đổi.", "bằng không."],
   "B",
   "Miệng ở trên: p₁ = p₀ + mg/S. Miệng ở dưới: p₂ = p₀ − mg/S < p₁.\n"
   "Áp suất giảm nên theo định luật Boyle thể tích khí tăng.",
   "Bài toán pit-tông", K, fig="k_sd_xilanh_quanang", cap="Xi lanh có pit-tông"),

mc("Một bình chứa 0,50 mol khí lí tưởng ở 27 °C. Nếu bơm thêm 0,25 mol khí cùng loại và đồng thời "
   "nâng nhiệt độ lên 127 °C (thể tích bình không đổi) thì áp suất tăng lên gấp",
   ["1,5 lần.", "2,0 lần.", "2,5 lần.", "1,33 lần."],
   "B",
   "Từ pV = nRT, với V không đổi: p tỉ lệ với tích n·T.\n"
   "Tỉ số: (0,75 · 400)/(0,50 · 300) = 300/150 = 2,0 lần.",
   "Phương trình Clapeyron", K),

mc("Áp suất của một khối khí tăng 44 % khi giữ nguyên thể tích. Nhiệt độ tuyệt đối của khí",
   ["tăng 22 %.", "tăng 44 %.", "tăng 20 %.", "tăng 88 %."],
   "B",
   "Đẳng tích: p tỉ lệ thuận với T nên T cũng tăng 44 %. "
   "Lưu ý phân biệt với trường hợp tốc độ phân tử, vốn chỉ tăng theo căn bậc hai.",
   "Định luật Gay-Lussac", K),

mc("Một thanh dẫn nằm ngang treo bằng hai lò xo giống nhau trong từ trường đều nằm ngang. "
   "Khi dòng điện có chiều làm lực từ hướng xuống, mỗi lò xo giãn 7,0 cm; khi đảo chiều dòng điện "
   "mỗi lò xo giãn 3,0 cm. Khi không có dòng, mỗi lò xo giãn",
   ["4,0 cm.", "5,0 cm.", "6,0 cm.", "2,0 cm."],
   "B",
   "Gọi ℓ là độ giãn khi không có dòng. Lực từ có cùng độ lớn trong hai trường hợp:\n"
   "2k(7,0 − ℓ) = F và 2k(ℓ − 3,0) = F ⇒ 7,0 − ℓ = ℓ − 3,0 ⇒ 2ℓ = 10 ⇒ ℓ = 5,0 cm.",
   "Thanh dẫn treo trên lò xo", RK, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),

mc("Với bài toán trên, tỉ số giữa lực từ và trọng lượng thanh bằng",
   ["0,29.", "0,40.", "0,50.", "0,67."],
   "B",
   "Khi không có dòng: 2k·5,0 = P. Khi có dòng (lực hướng xuống): 2k·7,0 = P + F.\n"
   "Lấy hiệu: 2k·2,0 = F ⇒ F/P = 2,0/5,0 = 0,40.",
   "Thanh dẫn treo trên lò xo", RK, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),

mc("Một khung dây hình vuông cạnh 40 cm chuyển động đều với tốc độ 3,0 m/s đi qua vùng từ trường "
   "đều rộng 25 cm. Thời gian KHÔNG có dòng điện cảm ứng trong khung bằng",
   ["0,050 s.", "0,025 s.", "0,083 s.", "0,133 s."],
   "A",
   "Vì bề rộng vùng (25 cm) nhỏ hơn cạnh khung (40 cm) nên có giai đoạn khung vắt qua vùng mà "
   "từ thông không đổi, ứng với quãng đường 40 − 25 = 15 cm.\n"
   "t = 0,15/3,0 = 0,050 s.",
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

mc("Một máy biến áp lí tưởng có điện áp sơ cấp 220 V không đổi. Khi thứ cấp có N vòng thì điện áp "
   "là 22 V; khi bớt 40 vòng thì điện áp còn 18 V. Số vòng cuộn sơ cấp bằng",
   ["1100 vòng.", "2200 vòng.", "1000 vòng.", "1650 vòng."],
   "B",
   "Mỗi vòng thứ cấp ứng với (22 − 18)/40 = 0,10 V.\n"
   "Số vòng ban đầu: N = 22/0,10 = 220 vòng.\n"
   "N₁ = N·U₁/U₂ = 220 · 220/22 = 2200 vòng.",
   "Máy biến áp – hệ hai phương trình", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất không đổi đi xa, nếu tăng điện áp lên k lần thì công suất TỚI NƠI TIÊU THỤ "
   "tăng từ 80 % lên 95 % công suất truyền. Giá trị của k bằng",
   ["1,5.", "2,0.", "2,5.", "4,0."],
   "B",
   "Hao phí giảm từ 20 % xuống 5 %, tức giảm 4 lần.\n"
   "Vì hao phí tỉ lệ nghịch với U² nên k² = 4 ⇒ k = 2,0.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Tổng năng lượng mà 0,80 gam ²¹⁰Po toả ra cho tới khi phân rã hết xấp xỉ "
   "(5,4 MeV mỗi phân rã; Nₐ = 6,02·10²³; 1 MeV = 1,6·10⁻¹³ J)",
   ["9,9·10⁸ J.", "1,98·10⁹ J.", "3,96·10⁹ J.", "4,95·10⁸ J."],
   "B",
   "N₀ = (0,80/210)·6,02·10²³ ≈ 2,293·10²¹ hạt.\n"
   "E = 2,293·10²¹ · 5,4 · 1,6·10⁻¹³ = 2,293·10²¹ · 8,64·10⁻¹³ ≈ 1,98·10⁹ J.",
   "Năng lượng tích luỹ của nguồn", RK),

mc("Hạt nhân ²²⁶₈₈Ra đứng yên phóng xạ α, toả 4,8 MeV. Động năng của hạt nhân con xấp xỉ",
   ["0,085 MeV.", "0,17 MeV.", "4,71 MeV.", "2,40 MeV."],
   "A",
   "Hạt nhân con là ²²²₈₆Rn.\n"
   "W(con) = ΔE · A(α)/(A(α) + A(con)) = 4,8 · 4/226 ≈ 0,085 MeV.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một mẫu chất phóng xạ nguyên chất, sau 2 giờ thì 19 % số hạt nhân đã phân rã. "
   "Chu kì bán rã của chất đó xấp xỉ (ln2 ≈ 0,693)",
   ["4,6 giờ.", "6,6 giờ.", "2,3 giờ.", "9,2 giờ."],
   "B",
   "Còn lại 81 % = 0,81. Từ 2^(−2/T) = 0,81 ⇒ (2/T)·ln2 = ln(1/0,81) = 0,2107.\n"
   "2/T = 0,2107/0,693 = 0,3041 ⇒ T = 2/0,3041 ≈ 6,6 giờ.",
   "Định luật phóng xạ – dùng logarit", RK),

mc("Trong phản ứng phân hạch, hai mảnh vỡ có số khối 90 và 144 bay ngược chiều nhau. "
   "Tỉ số tốc độ của chúng bằng",
   ["90 : 144.", "144 : 90.", "1 : 1.", "√(144/90)."],
   "B",
   "Bảo toàn động lượng: m₁v₁ = m₂v₂ ⇒ v₁/v₂ = m₂/m₁ = 144/90 = 1,6.\n"
   "Mảnh nhẹ bay nhanh hơn.",
   "Bảo toàn động lượng trong phân hạch", K, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Một lò phản ứng hoạt động ở công suất nhiệt 2500 MW trong 300 ngày mỗi năm. "
   "Khối lượng ²³⁵U tiêu thụ mỗi năm xấp xỉ (200 MeV mỗi phân hạch)",
   ["396 kg.", "790 kg.", "1580 kg.", "198 kg."],
   "B",
   "Số phân hạch mỗi giây: 2,5·10⁹/3,2·10⁻¹¹ ≈ 7,81·10¹⁹.\n"
   "Thời gian: 300 · 86 400 = 2,592·10⁷ s.\n"
   "Tổng số hạt: 7,81·10¹⁹ · 2,592·10⁷ ≈ 2,025·10²⁷.\n"
   "Khối lượng: (2,025·10²⁷/6,02·10²³) · 235 ≈ 3364 · 235/1000 ≈ 790 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

mc("Một chất phóng xạ có chu kì bán rã T. Thời gian để độ phóng xạ giảm từ 80 % xuống 5 % giá trị "
   "ban đầu bằng",
   ["2T.", "4T.", "3T.", "5T."],
   "B",
   "Độ phóng xạ giảm từ 0,80 xuống 0,05, tức giảm 16 lần = 2⁴.\n"
   "Vậy khoảng thời gian đó bằng 4 chu kì bán rã.",
   "Định luật phóng xạ", K),

mc("Trong một mẫu chất phóng xạ, đại lượng nào sau đây KHÔNG giảm theo thời gian?",
   ["Số hạt nhân chưa phân rã.", "Chu kì bán rã.",
    "Độ phóng xạ.", "Công suất toả nhiệt của mẫu."],
   "B",
   "Chu kì bán rã là hằng số đặc trưng của đồng vị, không đổi theo thời gian. "
   "Ba đại lượng còn lại đều tỉ lệ với số hạt nhân nên cùng giảm theo hàm mũ.",
   "Đặc điểm của chu kì bán rã", TB),

mc("Khi nói về hiệu suất của nhà máy điện hạt nhân, phát biểu nào ĐÚNG?",
   ["Hiệu suất bằng 100 % vì năng lượng hạt nhân rất lớn.",
    "Hiệu suất khoảng 30–35 %, bị giới hạn bởi chu trình nhiệt của hơi nước.",
    "Hiệu suất không phụ thuộc nhiệt độ hơi nước.",
    "Hiệu suất bằng hệ số nhân nơtron."],
   "B",
   "Năng lượng hạt nhân trước hết chuyển thành nhiệt, rồi mới qua chu trình hơi nước – tua bin. "
   "Chu trình nhiệt này bị giới hạn bởi chênh lệch nhiệt độ nên hiệu suất chỉ khoảng 30–35 %.",
   "Nhà máy điện hạt nhân", K),
],
P2=[
ds("Một bình nước nóng năng lượng mặt trời nhận trung bình 800 W bức xạ, hiệu suất hấp thụ 55 %. "
   "Bình chứa 100 kg nước. Cho c(nước) = 4200 J/(kg·K).",
   [("Công suất nhiệt có ích của bình là 440 W.", True,
     "Đúng. 800 · 0,55 = 440 W."),
    ("Nhiệt lượng cần để nước tăng 15 °C là 6,3·10⁶ J.", True,
     "Đúng. Q = 100 · 4200 · 15 = 6 300 000 J."),
    ("Thời gian cần thiết xấp xỉ 4,0 giờ.", True,
     "Đúng. t = 6,3·10⁶/440 ≈ 14 318 s ≈ 3,98 giờ."),
    ("Nếu tăng hiệu suất hấp thụ lên 80 % thì thời gian đun cũng tăng theo.", False,
     "Sai. Hiệu suất cao hơn cho công suất có ích lớn hơn nên thời gian đun GIẢM, "
     "còn khoảng 2,7 giờ.")],
   "Hiệu suất và công suất", K, fig="n_sd_binhnuocnong", cap="Bình nước nóng dùng năng lượng mặt trời"),

ds("Một thanh dẫn nằm ngang treo bằng hai lò xo giống nhau trong từ trường đều nằm ngang vuông góc "
   "với thanh. Khi lực từ hướng xuống, mỗi lò xo giãn 9,0 cm; khi đảo chiều dòng điện, mỗi lò xo "
   "giãn 5,0 cm.",
   [("Độ lớn lực từ trong hai trường hợp là như nhau.", True,
     "Đúng. Đảo chiều dòng điện chỉ đổi chiều lực từ, không đổi độ lớn."),
    ("Khi không có dòng điện, mỗi lò xo giãn 7,0 cm.", True,
     "Đúng. 9,0 − ℓ = ℓ − 5,0 ⇒ 2ℓ = 14 ⇒ ℓ = 7,0 cm."),
    ("Tỉ số giữa lực từ và trọng lượng thanh bằng 2/7.", True,
     "Đúng. 2k·2,0 = F và 2k·7,0 = P ⇒ F/P = 2,0/7,0 ≈ 0,286."),
    ("Nếu tăng cường độ dòng điện lên gấp đôi thì độ giãn lò xo khi lực từ hướng xuống là 18 cm.", False,
     "Sai. Lực từ tăng gấp đôi nên độ giãn thêm tăng gấp đôi: 7,0 + 2·2,0 = 11 cm, "
     "không phải 18 cm.")],
   "Thanh dẫn treo trên lò xo", RK, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),

ds("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi 220 V. Khi cuộn thứ cấp có N vòng thì "
   "điện áp thứ cấp là 22 V; khi bớt 40 vòng thì điện áp còn 18 V.",
   [("Mỗi vòng dây thứ cấp ứng với điện áp 0,10 V.", True,
     "Đúng. (22 − 18)/40 = 0,10 V mỗi vòng."),
    ("Số vòng ban đầu của cuộn thứ cấp là 220 vòng.", True,
     "Đúng. N = 22/0,10 = 220 vòng."),
    ("Số vòng cuộn sơ cấp là 2200 vòng.", True,
     "Đúng. N₁ = N₂·U₁/U₂ = 220 · 220/22 = 2200 vòng."),
    ("Muốn điện áp thứ cấp đạt 33 V thì phải quấn thêm 40 vòng nữa.", False,
     "Sai. Cần 33/0,10 = 330 vòng, tức phải quấn thêm 330 − 220 = 110 vòng.")],
   "Máy biến áp – hệ hai phương trình", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Một mẫu 0,80 gam ²¹⁰Po (chu kì bán rã 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   [("Số hạt nhân ban đầu xấp xỉ 2,29·10²¹ hạt.", True,
     "Đúng. N₀ = (0,80/210)·6,02·10²³ ≈ 2,293·10²¹ hạt."),
    ("Tổng năng lượng toả ra cho tới khi phân rã hết xấp xỉ 1,98·10⁹ J.", True,
     "Đúng. E = 2,293·10²¹ · 8,64·10⁻¹³ ≈ 1,98·10⁹ J."),
    ("Một nửa tổng năng lượng đó được toả ra trong 138 ngày đầu tiên.", True,
     "Đúng. Sau một chu kì bán rã, đúng một nửa số hạt nhân đã phân rã."),
    ("Sau 276 ngày, năng lượng còn lại chưa toả ra bằng một nửa tổng năng lượng.", False,
     "Sai. Sau 276 ngày (2 chu kì) mới còn 1/4 số hạt nhân, nên năng lượng chưa toả ra chỉ bằng "
     "một phần tư tổng năng lượng.")],
   "Năng lượng tích luỹ của nguồn", RK),
],
P3=[
sa("Một bình nước nóng năng lượng mặt trời nhận trung bình 500 W bức xạ với hiệu suất hấp thụ 50 %. "
   "Bình chứa 60 kg nước. Thời gian để nước tăng thêm 10 °C bằng bao nhiêu giờ "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho c(nước) = 4200 J/(kg·K).",
   "2,8",
   "Nhiệt lượng cần: Q = 60 · 4200 · 10 = 2 520 000 J.\n"
   "Công suất có ích: 500 · 0,50 = 250 W.\n"
   "t = 2 520 000/250 = 10 080 s = 2,8 giờ.",
   "Hiệu suất và công suất", K),

sa("Một bình chứa 0,40 mol khí lí tưởng ở 27 °C. Bơm thêm 0,20 mol khí cùng loại và nâng nhiệt độ "
   "lên 177 °C (thể tích bình không đổi). Áp suất tăng lên gấp bao nhiêu lần "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "2,25",
   "Với V không đổi, p tỉ lệ với tích n·T.\n"
   "Tỉ số: (0,60 · 450)/(0,40 · 300) = 270/120 = 2,25 lần.",
   "Phương trình Clapeyron", K),

sa("Một thanh dẫn nằm ngang treo bằng hai lò xo giống nhau trong từ trường đều. Khi lực từ hướng "
   "xuống, mỗi lò xo giãn 8,0 cm; khi đảo chiều dòng điện, mỗi lò xo giãn 4,0 cm. "
   "Khi không có dòng điện, mỗi lò xo giãn bao nhiêu centimét?",
   "6",
   "Lực từ có cùng độ lớn trong hai trường hợp, chỉ khác chiều.\n"
   "Gọi ℓ là độ giãn khi không có dòng: 8,0 − ℓ = ℓ − 4,0 ⇒ 2ℓ = 12 ⇒ ℓ = 6,0 cm.",
   "Thanh dẫn treo trên lò xo", RK),

sa("Một khung dây vuông cạnh 25 cm, điện trở 0,50 Ω, được kéo đều với tốc độ 4,0 m/s ra khỏi "
   "vùng từ trường đều B = 0,40 T. Nhiệt lượng toả ra trên khung trong suốt quá trình bằng "
   "bao nhiêu milijun?",
   "20",
   "e = B·a·v = 0,40 · 0,25 · 4,0 = 0,40 V;  i = 0,40/0,50 = 0,80 A.\n"
   "Thời gian ra khỏi vùng: t = a/v = 0,25/4,0 = 0,0625 s.\n"
   "Q = R·i²·t = 0,50 · 0,64 · 0,0625 = 0,020 J = 20 mJ.",
   "Năng lượng trong cảm ứng điện từ", RK),

sa("Một mẫu chất phóng xạ nguyên chất, sau 3,0 giờ thì 28 % số hạt nhân đã phân rã. "
   "Chu kì bán rã của chất đó bằng bao nhiêu giờ (làm tròn đến chữ số thập phân thứ nhất)? "
   "Lấy ln2 ≈ 0,693.",
   "6,3",
   "Còn lại 72 % = 0,72. Từ 2^(−3/T) = 0,72 ⇒ (3/T)·ln2 = ln(1/0,72) = 0,3285.\n"
   "3/T = 0,3285/0,693 = 0,4740 ⇒ T = 3/0,4740 ≈ 6,3 giờ.",
   "Định luật phóng xạ – dùng logarit", RK),

sa("Một lò phản ứng hoạt động ở công suất nhiệt 2000 MW trong 250 ngày. Khối lượng ²³⁵U tiêu thụ "
   "bằng bao nhiêu kilôgam (làm tròn đến hàng đơn vị)? Mỗi phân hạch toả 200 MeV; "
   "1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   "527",
   "Số phân hạch mỗi giây: 2,0·10⁹/3,2·10⁻¹¹ = 6,25·10¹⁹.\n"
   "Thời gian: 250 · 86 400 = 2,16·10⁷ s.\n"
   "Tổng số hạt: 6,25·10¹⁹ · 2,16·10⁷ = 1,35·10²⁷.\n"
   "Số mol: 1,35·10²⁷/6,02·10²³ ≈ 2242 mol.\n"
   "Khối lượng: 2242 · 235 ≈ 526 900 g ≈ 527 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", RK),
])


# =====================================================================  ĐỀ 18
DE18 = dict(
ma="TH-Đề 18", ten="ĐỀ THI THỬ SỐ 18", muc="Khó",
trongtam="Bài toán tổng hợp nhiều chương trong một tình huống thực tiễn",
P1=[
mc("Một ấm điện 2,2 kW dùng mạng 220 V. Cường độ dòng điện hiệu dụng qua ấm bằng",
   ["5,0 A.", "10,0 A.", "20,0 A.", "2,2 A."],
   "B",
   "I = P/U = 2200/220 = 10,0 A.",
   "Công suất dòng xoay chiều", TB),

mc("Ấm điện trên đun 2,5 kg nước từ 20 °C tới sôi với hiệu suất 85 %. Thời gian đun xấp xỉ",
   ["324 s.", "449 s.", "382 s.", "540 s."],
   "B",
   "Q(ci) = 2,5 · 4200 · 80 = 840 000 J.\n"
   "Q(tp) = 840 000/0,85 ≈ 988 235 J.\n"
   "t = 988 235/2200 ≈ 449 s.",
   "Hiệu suất và công suất", K),

mc("Nếu tiếp tục đun để 0,20 kg nước hoá hơi ở 100 °C thì cần thêm thời gian xấp xỉ "
   "(L = 2,26·10⁶ J/kg, hiệu suất vẫn 85 %)",
   ["205 s.", "242 s.", "180 s.", "290 s."],
   "B",
   "Q(ci) = 0,20 · 2,26·10⁶ = 452 000 J.\n"
   "Q(tp) = 452 000/0,85 ≈ 531 765 J.\n"
   "t = 531 765/2200 ≈ 242 s.",
   "Nhiệt hoá hơi riêng", K),

mc("Một khối khí lí tưởng bị nén đẳng nhiệt từ 10 L xuống 2,5 L. Nếu áp suất ban đầu là "
   "0,80·10⁵ Pa thì công mà môi trường thực hiện lên khí có đặc điểm",
   ["bằng 0 vì đẳng nhiệt.", "dương, và bằng nhiệt lượng khí toả ra.",
    "âm, khí sinh công.", "bằng độ tăng nội năng."],
   "B",
   "Đẳng nhiệt với khí lí tưởng nên ΔU = 0 ⇒ Q = −A. Khí bị nén nên A > 0 (khí nhận công), "
   "do đó Q < 0: khí toả ra nhiệt lượng đúng bằng công nhận được.",
   "Quá trình đẳng nhiệt", K),

mc("Áp suất khí sau khi nén ở câu trên bằng",
   ["1,6·10⁵ Pa.", "3,2·10⁵ Pa.", "2,0·10⁵ Pa.", "0,20·10⁵ Pa."],
   "B",
   "p₂ = p₁·V₁/V₂ = 0,80·10⁵ · 10/2,5 = 0,80·10⁵ · 4 = 3,2·10⁵ Pa.",
   "Định luật Boyle", TB),

mc("Một bình 5,0 L chứa khí ở 2,0·10⁵ Pa và 27 °C. Nung nóng bình tới 127 °C rồi mở van cho khí "
   "thoát bớt để áp suất trở về 2,0·10⁵ Pa. Phần trăm khối lượng khí đã thoát ra bằng",
   ["20 %.", "25 %.", "33 %.", "50 %."],
   "B",
   "Nếu không mở van, áp suất ở 400 K sẽ là 2,0·10⁵ · 400/300 ≈ 2,67·10⁵ Pa.\n"
   "Ở cùng 400 K và cùng thể tích, khối lượng khí tỉ lệ thuận với áp suất:\n"
   "còn lại 2,0/2,67 = 0,75 ⇒ đã thoát ra 25 %.",
   "Phương trình Clapeyron", RK),

mc("Một thanh dẫn dài 50 cm, khối lượng 120 g nằm trên hai ray nằm ngang có hệ số ma sát 0,30, "
   "trong từ trường đều thẳng đứng B = 0,60 T. Cho dòng điện 4,0 A. Gia tốc của thanh bằng "
   "(g = 10 m/s²)",
   ["7,0 m/s².", "10,0 m/s².", "12,0 m/s².", "3,0 m/s²."],
   "A",
   "Lực từ: F = 0,60 · 4,0 · 0,50 = 1,20 N.\n"
   "Ma sát: 0,30 · 0,120 · 10 = 0,36 N.\n"
   "a = (1,20 − 0,36)/0,120 = 0,84/0,120 = 7,0 m/s².",
   "Lực từ và động lực học", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một cuộn dây 500 vòng quay đều trong từ trường đều B = 0,20 T, diện tích mỗi vòng 30 cm², "
   "tần số 50 Hz, nối với điện trở 100 Ω. Công suất trung bình tiêu thụ xấp xỉ",
   ["22,2 W.", "44,4 W.", "88,8 W.", "11,1 W."],
   "B",
   "ω = 2πf = 2 · 3,1416 · 50 ≈ 314,16 rad/s.\n"
   "E₀ = ω·N·B·S = 314,16 · 500 · 0,20 · 3,0·10⁻³ = 314,16 · 0,30 ≈ 94,25 V.\n"
   "Công suất trung bình tính theo giá trị hiệu dụng: P = E₀²/(2R).\n"
   "P = 94,25²/(2 · 100) = 8883/200 ≈ 44,4 W.",
   "Máy phát và công suất", RK),

mc("Truyền công suất 5,0 MW ở điện áp 50 kV trên đường dây có điện trở R. Hiệu suất truyền tải "
   "là 96 %. Điện trở R bằng",
   ["10 Ω.", "20 Ω.", "40 Ω.", "5,0 Ω."],
   "B",
   "Hao phí: ΔP = 4 % · 5,0·10⁶ = 2,0·10⁵ W.\n"
   "I = P/U = 5,0·10⁶/(50·10³) = 100 A.\n"
   "R = ΔP/I² = 2,0·10⁵/10⁴ = 20 Ω.",
   "Truyền tải – bài toán ngược", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Hạt nhân ²³⁵₉₂U hấp thụ một nơtron rồi phân hạch thành ²³₉₉₅Mo, ¹³⁹₅₇La, hai nơtron và một số "
   "electron. Số electron phát ra bằng",
   ["5.", "7.", "3.", "0."],
   "B",
   "Bảo toàn số khối: 235 + 1 = 95 + 139 + 2 ⇒ 236 = 236 ✓ (electron có A = 0).\n"
   "Bảo toàn điện tích: 92 + 0 = 42 + 57 + 0 + (−1)·x ⇒ 92 = 99 − x ⇒ x = 7 electron.",
   "Phản ứng phân hạch", RK),

mc("Một mẫu chất phóng xạ có chu kì bán rã 6,0 giờ. Số hạt nhân phân rã trong giờ thứ 7 so với "
   "số hạt nhân ban đầu chiếm khoảng",
   ["4,6 %.", "5,4 %.", "8,0 %.", "10,0 %."],
   "B",
   "Sau 6 giờ còn 2⁻¹ = 0,5; sau 7 giờ còn 2^(−7/6) ≈ 0,4454.\n"
   "Số hạt rã trong giờ thứ 7: 0,5 − 0,4454 = 0,0546 ≈ 5,4 % số hạt ban đầu.",
   "Phân rã trong khoảng ngắn", RK),

mc("Một hạt nhân đứng yên phóng xạ α, hạt α có động năng 4,80 MeV. Nếu số khối hạt nhân mẹ là 222 "
   "thì năng lượng toả ra của phản ứng xấp xỉ",
   ["4,80 MeV.", "4,89 MeV.", "5,00 MeV.", "4,71 MeV."],
   "B",
   "Hạt nhân con có A = 218. W(α)/ΔE = 218/222.\n"
   "ΔE = 4,80 · 222/218 ≈ 4,89 MeV.",
   "Bảo toàn động lượng trong phân rã", RK),

mc("Trong chuỗi phân rã ²³²Th → ²⁰⁸Pb, tổng số hạt α và β⁻ phát ra bằng",
   ["8.", "10.", "12.", "6."],
   "B",
   "Số lần α: (232 − 208)/4 = 6.\n"
   "Sau 6 lần α, Z = 90 − 12 = 78; cần tới Z = 82 nên có 4 lần β⁻.\n"
   "Tổng: 6 + 4 = 10 hạt.",
   "Chuỗi phân rã", K),

mc("Một nguồn phóng xạ có chu kì bán rã 8,0 năm được dùng cho tới khi độ phóng xạ còn 1/8 giá trị "
   "ban đầu. Thời gian sử dụng bằng",
   ["16 năm.", "24 năm.", "32 năm.", "8,0 năm."],
   "B",
   "1/8 = 2⁻³ ⇒ n = 3 chu kì.\n"
   "t = 3 · 8,0 = 24 năm.",
   "Định luật phóng xạ", TB),

mc("Hai mẫu của hai đồng vị khác nhau có cùng độ phóng xạ ban đầu, chu kì bán rã lần lượt là "
   "3,0 giờ và 12 giờ. Sau 12 giờ, tỉ số độ phóng xạ của mẫu thứ nhất so với mẫu thứ hai bằng",
   ["1 : 4.", "1 : 8.", "1 : 2.", "1 : 16."],
   "B",
   "Mẫu 1 trải qua 4 chu kì: H₀/16. Mẫu 2 trải qua 1 chu kì: H₀/2.\n"
   "Tỉ số: (H₀/16)/(H₀/2) = 1/8.",
   "So sánh hai nguồn phóng xạ", K),

mc("Muốn giảm liều chiếu nhận được xuống còn 1/25 giá trị ban đầu bằng cách tăng khoảng cách, "
   "phải đứng xa nguồn gấp",
   ["25 lần.", "5 lần.", "12,5 lần.", "2,5 lần."],
   "B",
   "Liều chiếu tỉ lệ nghịch với bình phương khoảng cách. Muốn giảm 25 lần thì khoảng cách phải "
   "tăng √25 = 5 lần.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Trong phản ứng hạt nhân, đại lượng nào sau đây luôn được bảo toàn nhưng KHÔNG phải là "
   "khối lượng nghỉ?",
   ["Số nơtron riêng rẽ.", "Tổng số nuclêôn.",
    "Số prôtôn riêng rẽ.", "Năng lượng liên kết."],
   "B",
   "Tổng số nuclêôn (số khối) và điện tích luôn được bảo toàn. Số prôtôn và nơtron riêng rẽ có thể "
   "chuyển hoá cho nhau; năng lượng liên kết thì thay đổi — chính sự thay đổi đó cho ra năng lượng "
   "của phản ứng.",
   "Định luật bảo toàn", TB),

mc("Nhận định nào sau đây về nhà máy điện hạt nhân là SAI?",
   ["Không phát thải khí nhà kính trong quá trình vận hành.",
    "Chất thải phóng xạ được xử lí hết ngay sau khi lấy ra khỏi lò.",
    "Cần hệ thống làm mát và che chắn bức xạ nghiêm ngặt.",
    "Lượng nhiên liệu tiêu thụ rất nhỏ so với nhà máy nhiệt điện than."],
   "B",
   "Chất thải phóng xạ phải được lưu giữ và cách li hàng trăm tới hàng nghìn năm do các sản phẩm "
   "phân hạch có chu kì bán rã rất dài. Ba nhận định còn lại đều đúng.",
   "An toàn hạt nhân", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ nhà máy điện hạt nhân"),
],
P2=[
ds("Một ấm điện công suất 2,0 kW, hiệu suất 80 %, dùng đun 3,0 kg nước từ 25 °C. "
   "Cho c(nước) = 4200 J/(kg·K); L = 2,26·10⁶ J/kg.",
   [("Nhiệt lượng có ích để đun nước tới sôi là 945 kJ.", True,
     "Đúng. Q = 3,0 · 4200 · 75 = 945 000 J."),
    ("Thời gian để nước sôi xấp xỉ 591 giây.", True,
     "Đúng. Q(tp) = 945 000/0,80 = 1 181 250 J ⇒ t = 1 181 250/2000 ≈ 591 s."),
    ("Muốn 0,50 kg nước hoá hơi thêm cần khoảng 706 giây nữa.", True,
     "Đúng. Q(ci) = 0,50 · 2,26·10⁶ = 1 130 000 J; Q(tp) = 1 412 500 J ⇒ t ≈ 706 s."),
    ("Giai đoạn hoá hơi 0,50 kg nước tốn ít thời gian hơn giai đoạn đun sôi cả 3,0 kg nước.", False,
     "Sai. 706 s > 591 s: chỉ hoá hơi 0,50 kg nước đã tốn nhiều thời gian hơn đun sôi cả 3,0 kg, "
     "vì nhiệt hoá hơi riêng rất lớn.")],
   "Hiệu suất và chuyển thể", K),

ds("Một bình 5,0 L chứa khí lí tưởng ở 2,0·10⁵ Pa và 27 °C. Nung nóng bình lên 127 °C rồi mở van "
   "cho khí thoát bớt để áp suất trở lại 2,0·10⁵ Pa.",
   [("Nếu không mở van, áp suất ở 127 °C sẽ xấp xỉ 2,67·10⁵ Pa.", True,
     "Đúng. p = 2,0·10⁵ · 400/300 ≈ 2,67·10⁵ Pa."),
    ("Ở cùng nhiệt độ 400 K và cùng thể tích, khối lượng khí tỉ lệ thuận với áp suất.", True,
     "Đúng. Đó là hệ quả trực tiếp của pV = (m/M)RT."),
    ("Phần khối lượng khí đã thoát ra chiếm 25 % khối lượng khí ban đầu.", True,
     "Đúng. Còn lại 2,0/2,67 = 0,75 nên đã thoát ra 25 %."),
    ("Trong toàn bộ quá trình, có thể áp dụng phương trình p₁V₁/T₁ = p₂V₂/T₂.", False,
     "Sai. Khi khí thoát ra, lượng khí thay đổi nên phải dùng phương trình Clapeyron pV = nRT "
     "cho từng thời điểm.")],
   "Phương trình Clapeyron", RK),

ds("Một cuộn dây 500 vòng quay đều trong từ trường đều B = 0,20 T, diện tích mỗi vòng 30 cm², "
   "tần số 50 Hz, nối với điện trở thuần 100 Ω. Lấy π ≈ 3,1416.",
   [("Tần số góc của khung xấp xỉ 314 rad/s.", True,
     "Đúng. ω = 2π·50 ≈ 314,16 rad/s."),
    ("Suất điện động cực đại xấp xỉ 94,2 V.", True,
     "Đúng. E₀ = 314,16 · 500 · 0,20 · 3,0·10⁻³ = 314,16 · 0,30 ≈ 94,25 V."),
    ("Suất điện động hiệu dụng xấp xỉ 66,6 V.", True,
     "Đúng. E = 94,25/1,414 ≈ 66,6 V."),
    ("Công suất trung bình tiêu thụ trên điện trở xấp xỉ 88,8 W.", False,
     "Sai. P = E²/R = 66,6²/100 ≈ 44,4 W. Giá trị 88,8 W là kết quả khi dùng nhầm "
     "giá trị cực đại thay cho giá trị hiệu dụng.")],
   "Máy phát và công suất", RK),

ds("Hạt nhân ²²²₈₆Rn đứng yên phóng xạ α, hạt α thu được động năng 4,80 MeV. "
   "Coi khối lượng tỉ lệ với số khối.",
   [("Hạt nhân con có số khối 218.", True,
     "Đúng. A = 222 − 4 = 218; Z = 86 − 2 = 84, đó là ²¹⁸₈₄Po."),
    ("Động năng hạt α chiếm khoảng 98,2 % năng lượng toả ra.", True,
     "Đúng. W(α)/ΔE = 218/222 ≈ 0,982."),
    ("Năng lượng toả ra của phản ứng xấp xỉ 4,89 MeV.", True,
     "Đúng. ΔE = 4,80 · 222/218 ≈ 4,888 MeV."),
    ("Động năng hạt nhân con lớn hơn động năng hạt α.", False,
     "Sai. Hạt nhân con nặng gấp 54,5 lần nên chỉ mang khoảng 4,89 − 4,80 = 0,09 MeV.")],
   "Bảo toàn động lượng trong phân rã", RK),
],
P3=[
sa("Một ấm điện 1,5 kW, hiệu suất 90 %, đun 2,0 kg nước từ 30 °C tới sôi. Thời gian đun bằng "
   "bao nhiêu giây (làm tròn đến hàng đơn vị)? Cho c(nước) = 4200 J/(kg·K).",
   "436",
   "Q(ci) = 2,0 · 4200 · 70 = 588 000 J.\n"
   "Q(tp) = 588 000/0,90 ≈ 653 333 J.\n"
   "t = 653 333/1500 ≈ 436 s.",
   "Hiệu suất và công suất", K),

sa("Một bình 8,0 L chứa khí ở 1,5·10⁵ Pa và 27 °C. Nung nóng bình lên 177 °C rồi mở van cho khí "
   "thoát bớt để áp suất trở lại 1,5·10⁵ Pa. Phần trăm khối lượng khí đã thoát ra bằng bao nhiêu "
   "phần trăm (làm tròn đến chữ số thập phân thứ nhất)?",
   "33,3",
   "Nếu không mở van, ở 450 K áp suất sẽ là 1,5·10⁵ · 450/300 = 2,25·10⁵ Pa.\n"
   "Ở cùng 450 K và cùng thể tích, khối lượng tỉ lệ thuận với áp suất:\n"
   "còn lại 1,5/2,25 = 0,6667 = 66,7 % ⇒ đã thoát ra 33,3 %.",
   "Phương trình Clapeyron", RK),

sa("Một thanh dẫn dài 60 cm, khối lượng 150 g nằm trên hai ray nằm ngang có hệ số ma sát 0,25, "
   "trong từ trường đều thẳng đứng B = 0,50 T. Cho dòng điện 5,0 A chạy qua. "
   "Gia tốc của thanh bằng bao nhiêu mét trên giây bình phương? Lấy g = 10 m/s².",
   "7,5",
   "Lực từ: F = 0,50 · 5,0 · 0,60 = 1,50 N.\n"
   "Lực ma sát: 0,25 · 0,150 · 10 = 0,375 N.\n"
   "a = (1,50 − 0,375)/0,150 = 1,125/0,150 = 7,5 m/s².",
   "Lực từ và động lực học", K),

sa("Truyền công suất 4,0 MW ở điện áp 40 kV trên đường dây có điện trở R, hiệu suất 95 %. "
   "Điện trở R bằng bao nhiêu ôm?",
   "20",
   "Hao phí: ΔP = 5 % · 4,0·10⁶ = 2,0·10⁵ W.\n"
   "I = P/U = 4,0·10⁶/(40·10³) = 100 A.\n"
   "R = ΔP/I² = 2,0·10⁵/10⁴ = 20 Ω.",
   "Truyền tải – bài toán ngược", K),

sa("Hạt nhân ²³⁵₉₂U hấp thụ một nơtron rồi phân hạch thành ⁹⁵₄₂Mo, ¹³⁹₅₇La, hai nơtron và x electron. "
   "Giá trị của x bằng bao nhiêu?",
   "7",
   "Bảo toàn số khối: 235 + 1 = 95 + 139 + 2 ⇒ 236 = 236 ✓.\n"
   "Bảo toàn điện tích: 92 = 42 + 57 − x ⇒ 92 = 99 − x ⇒ x = 7 electron.",
   "Phản ứng phân hạch", RK),

sa("Một hạt nhân có số khối 210 đứng yên phóng xạ α, hạt α có động năng 5,20 MeV. "
   "Năng lượng toả ra của phản ứng bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)?",
   "5,30",
   "Hạt nhân con có A = 206. W(α)/ΔE = 206/210.\n"
   "ΔE = 5,20 · 210/206 ≈ 5,3010 ≈ 5,30 MeV.",
   "Bảo toàn động lượng trong phân rã", RK),
])


# =====================================================================  ĐỀ 19
DE19 = dict(
ma="TH-Đề 19", ten="ĐỀ THI THỬ SỐ 19", muc="Khó",
trongtam="Bài toán ghép nhiều bước giữa các chương, phân tích tỉ lệ nâng cao",
P1=[
mc("Một máy nước nóng dùng điện công suất 7,0 kW, hiệu suất 90 %, làm nóng nước từ 20 °C lên "
   "45 °C. Lưu lượng nước tối đa mà máy cấp được là",
   ["2,4 lít/phút.", "3,6 lít/phút.", "4,8 lít/phút.", "6,0 lít/phút."],
   "B",
   "Công suất nhiệt có ích: P = 7000 · 0,90 = 6300 W.\n"
   "Với ΔT = 25 °C, lưu lượng khối lượng: m/t = P/(c·ΔT) = 6300/(4200 · 25) = 6300/105 000 "
   "= 0,060 kg/s.\n"
   "Đổi sang lít mỗi phút: 0,060 · 60 = 3,6 lít/phút.",
   "Hiệu suất và công suất", K),

mc("Một khối khí lí tưởng có nội năng tỉ lệ thuận với nhiệt độ tuyệt đối. Nếu nung nóng đẳng tích "
   "làm nhiệt độ tuyệt đối tăng gấp ba thì nội năng",
   ["tăng gấp ba.", "tăng gấp chín.", "tăng gấp sáu.", "không đổi."],
   "A",
   "Nội năng của khí lí tưởng chỉ phụ thuộc nhiệt độ và tỉ lệ thuận với T. "
   "T tăng gấp ba thì nội năng cũng tăng gấp ba.",
   "Nội năng của khí lí tưởng", TB),

mc("Một khối khí lí tưởng thực hiện quá trình trong đó áp suất tỉ lệ thuận với thể tích "
   "(p = a·V). Khi thể tích tăng gấp đôi thì nhiệt độ tuyệt đối",
   ["tăng gấp đôi.", "tăng gấp bốn.", "không đổi.", "giảm một nửa."],
   "B",
   "Từ pV/T = hằng số và p = a·V ta có a·V²/T = hằng số, tức T tỉ lệ với V².\n"
   "V tăng gấp đôi thì T tăng gấp bốn.",
   "Quá trình đặc biệt của khí lí tưởng", RK),

mc("Một bình kín chứa hỗn hợp 0,20 mol hêli và 0,30 mol ôxi ở 27 °C, thể tích 4,155 L. "
   "Áp suất hỗn hợp bằng (R = 8,31 J/(mol·K))",
   ["1,5·10⁵ Pa.", "3,0·10⁵ Pa.", "2,0·10⁵ Pa.", "6,0·10⁵ Pa."],
   "B",
   "Tổng số mol: n = 0,20 + 0,30 = 0,50 mol.\n"
   "p = nRT/V = 0,50 · 8,31 · 300/(4,155·10⁻³) = 1246,5/4,155·10⁻³ = 3,0·10⁵ Pa.",
   "Hỗn hợp khí lí tưởng", K),

mc("Trong hỗn hợp ở câu trên, áp suất riêng phần của khí hêli bằng",
   ["1,8·10⁵ Pa.", "1,2·10⁵ Pa.", "1,5·10⁵ Pa.", "0,60·10⁵ Pa."],
   "B",
   "Áp suất riêng phần tỉ lệ với số mol: p(He) = 3,0·10⁵ · 0,20/0,50 = 1,2·10⁵ Pa.",
   "Hỗn hợp khí lí tưởng", K),

mc("Một khung dây tròn bán kính r, điện trở R, đặt vuông góc với từ trường đều đang biến thiên với "
   "tốc độ dB/dt. Nếu tăng bán kính lên gấp đôi (giữ nguyên tiết diện và vật liệu dây) thì cường độ "
   "dòng cảm ứng",
   ["không đổi.", "tăng gấp đôi.", "tăng gấp bốn.", "giảm một nửa."],
   "B",
   "Diện tích tăng 4 lần nên suất điện động tăng 4 lần.\n"
   "Chu vi tăng 2 lần nên chiều dài dây và điện trở đều tăng 2 lần.\n"
   "i = e/R tăng 4/2 = 2 lần.",
   "Phân tích tỉ lệ trong cảm ứng điện từ", RK),

mc("Một thanh dẫn dài ℓ trượt trên hai ray nằm ngang với tốc độ v, trong từ trường đều B, "
   "điện trở mạch R. Nếu đồng thời tăng gấp đôi B và giảm một nửa v thì công suất toả nhiệt",
   ["không đổi.", "tăng gấp đôi.", "tăng gấp bốn.", "giảm một nửa."],
   "A",
   "P = e²/R = (Bℓv)²/R tỉ lệ với (B·v)². B tăng 2 lần và v giảm 2 lần nên tích B·v không đổi, "
   "do đó công suất không đổi.",
   "Phân tích tỉ lệ", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một máy biến áp lí tưởng đang cấp cho tải. Nếu tăng số vòng cả hai cuộn lên gấp đôi và giữ "
   "nguyên điện áp sơ cấp thì công suất tiêu thụ của tải",
   ["tăng gấp đôi.", "không đổi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "Tỉ số vòng dây không đổi nên điện áp thứ cấp không đổi; tải không đổi nên công suất tiêu thụ "
   "cũng không đổi.",
   "Máy biến áp – phân tích tỉ số", K, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất P đi xa. Nếu đồng thời tăng điện áp lên 2 lần và tăng công suất truyền lên "
   "2 lần thì công suất hao phí",
   ["tăng 4 lần.", "không đổi.", "giảm 4 lần.", "tăng 2 lần."],
   "B",
   "ΔP = R·P²/U². P tăng 2 lần làm ΔP tăng 4 lần; U tăng 2 lần làm ΔP giảm 4 lần. "
   "Hai tác động bù trừ nên hao phí không đổi.",
   "Truyền tải – phân tích tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây quay đều trong từ trường đều nối với điện trở R. Nếu tăng tần số quay lên 3 lần "
   "thì công suất trung bình tiêu thụ trên R",
   ["tăng 3 lần.", "tăng 9 lần.", "không đổi.", "giảm 3 lần."],
   "B",
   "E₀ = ω·N·B·S tỉ lệ với tần số nên tăng 3 lần; công suất P = E₀²/(2R) tỉ lệ với bình phương "
   "suất điện động nên tăng 9 lần.",
   "Máy phát và công suất", K),

mc("Hạt nhân X có Z prôtôn và N nơtron. Nếu X phóng xạ β⁻ rồi hạt nhân con lại phóng xạ α thì "
   "hạt nhân cuối cùng so với X có",
   ["Z giảm 1, A giảm 4.", "Z giảm 2, A giảm 4.",
    "Z tăng 1, A giảm 4.", "Z giảm 3, A giảm 4."],
   "A",
   "β⁻: Z tăng 1, A không đổi. Sau đó α: Z giảm 2, A giảm 4.\n"
   "Tổng hợp: Z thay đổi +1 − 2 = −1; A thay đổi −4.",
   "Chuỗi phân rã", K, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một mẫu chất phóng xạ có chu kì bán rã T. Nếu chia mẫu thành 4 phần bằng nhau thì chu kì bán rã "
   "của mỗi phần và tổng độ phóng xạ của 4 phần lần lượt là",
   ["T/4 và H₀.", "T và H₀.", "T/4 và H₀/4.", "T và H₀/4."],
   "B",
   "Chu kì bán rã là hằng số của đồng vị, không đổi khi chia nhỏ mẫu. "
   "Mỗi phần có độ phóng xạ H₀/4 nên tổng bốn phần vẫn là H₀.",
   "Đặc điểm của chu kì bán rã", K),

mc("Năng lượng liên kết riêng của hạt nhân ²H là 1,11 MeV/nuclêôn và của ⁴He là 7,10 MeV/nuclêôn. "
   "Phản ứng ²H + ²H → ⁴He toả năng lượng xấp xỉ",
   ["11,98 MeV.", "23,96 MeV.", "28,40 MeV.", "4,44 MeV."],
   "B",
   "Năng lượng liên kết trước: 2 hạt ²H, mỗi hạt 2 · 1,11 = 2,22 MeV ⇒ tổng 4,44 MeV.\n"
   "Năng lượng liên kết sau: 4 · 7,10 = 28,40 MeV.\n"
   "ΔE = 28,40 − 4,44 = 23,96 MeV.",
   "Năng lượng phản ứng theo W(lk)", K),

mc("Một mẫu chất phóng xạ có độ phóng xạ giảm 1000 lần sau 100 ngày. Chu kì bán rã xấp xỉ "
   "(ln2 ≈ 0,693)",
   ["8,0 ngày.", "10,0 ngày.", "12,5 ngày.", "20,0 ngày."],
   "B",
   "2ⁿ = 1000 ⇒ n = ln1000/ln2 = 6,908/0,693 ≈ 9,97 chu kì.\n"
   "T = 100/9,97 ≈ 10,0 ngày.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Trong phản ứng phân hạch, phần lớn năng lượng toả ra xuất hiện dưới dạng",
   ["năng lượng của bức xạ γ.", "động năng của hai mảnh vỡ.",
    "động năng của các nơtron.", "năng lượng nghỉ của mảnh vỡ."],
   "B",
   "Khoảng 80 % năng lượng phân hạch nằm ở động năng của hai mảnh vỡ. Chính động năng này "
   "chuyển thành nhiệt khi các mảnh vỡ bị hãm lại trong nhiên liệu.",
   "Năng lượng phân hạch", K, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Một nguồn phóng xạ dùng trong công nghiệp có chu kì bán rã 5,3 năm. Sau bao lâu thì độ phóng "
   "xạ còn 60 % giá trị ban đầu (ln2 ≈ 0,693)?",
   ["2,6 năm.", "3,9 năm.", "5,3 năm.", "1,3 năm."],
   "B",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,60 ⇒ n = ln(1/0,60)/ln2 = 0,5108/0,693 ≈ 0,737.\n"
   "t = 0,737 · 5,3 ≈ 3,9 năm.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Khi nói về tia β⁻ phát ra từ hạt nhân, phát biểu nào ĐÚNG?",
   ["Electron đó vốn có sẵn trong hạt nhân.",
    "Electron đó sinh ra khi một nơtron biến thành prôtôn.",
    "Electron đó bứt ra từ lớp vỏ nguyên tử.",
    "Electron đó là một prôtôn mất điện tích."],
   "B",
   "Hạt nhân không chứa sẵn electron. Trong phân rã β⁻, một nơtron biến thành prôtôn, đồng thời "
   "sinh ra một electron và một phản nơtrinô — điều này giải thích vì sao Z tăng 1 mà A không đổi.",
   "Bản chất của phân rã beta", K),

mc("Trong bốn đại lượng sau, đại lượng nào KHÔNG phụ thuộc vào loại chất khí (với cùng nhiệt độ, "
   "cùng áp suất và cùng thể tích)?",
   ["Khối lượng riêng.", "Số mol khí.",
    "Tốc độ trung bình của phân tử.", "Khối lượng khí."],
   "B",
   "Từ pV = nRT, cùng p, V, T thì n như nhau với mọi khí lí tưởng. "
   "Khối lượng, khối lượng riêng và tốc độ phân tử đều phụ thuộc khối lượng mol.",
   "Phương trình Clapeyron", K),
],
P2=[
ds("Một bình kín thể tích 4,155 L chứa hỗn hợp 0,20 mol khí hêli và 0,30 mol khí ôxi ở 27 °C. "
   "Cho R = 8,31 J/(mol·K).",
   [("Tổng số mol khí trong bình là 0,50 mol.", True,
     "Đúng. 0,20 + 0,30 = 0,50 mol."),
    ("Áp suất hỗn hợp bằng 3,0·10⁵ Pa.", True,
     "Đúng. p = nRT/V = 0,50 · 8,31 · 300/(4,155·10⁻³) = 3,0·10⁵ Pa."),
    ("Áp suất riêng phần của hêli bằng 1,2·10⁵ Pa.", True,
     "Đúng. Tỉ lệ với số mol: 3,0·10⁵ · 0,20/0,50 = 1,2·10⁵ Pa."),
    ("Ở cùng nhiệt độ, phân tử hêli và phân tử ôxi có cùng tốc độ trung bình.", False,
     "Sai. Động năng trung bình bằng nhau nhưng hêli nhẹ hơn ôxi 8 lần nên tốc độ trung bình của "
     "hêli lớn hơn √8 ≈ 2,83 lần.")],
   "Hỗn hợp khí lí tưởng", K),

ds("Một khung dây tròn đặt vuông góc với từ trường đều đang biến thiên đều theo thời gian. "
   "Xét việc thay khung bằng khung khác cùng vật liệu, cùng tiết diện dây nhưng bán kính gấp đôi.",
   [("Diện tích khung mới gấp bốn lần khung cũ.", True,
     "Đúng. Diện tích tỉ lệ với bình phương bán kính."),
    ("Suất điện động cảm ứng trong khung mới gấp bốn lần.", True,
     "Đúng. e = S·(ΔB/Δt) tỉ lệ thuận với diện tích."),
    ("Điện trở của khung mới gấp đôi khung cũ.", True,
     "Đúng. Chu vi gấp đôi nên chiều dài dây gấp đôi, tiết diện không đổi nên R gấp đôi."),
    ("Cường độ dòng điện cảm ứng trong khung mới gấp bốn lần.", False,
     "Sai. i = e/R tăng 4 lần rồi giảm 2 lần, tổng cộng chỉ tăng GẤP ĐÔI.")],
   "Phân tích tỉ lệ trong cảm ứng điện từ", RK),

ds("Xét việc truyền tải điện năng đi xa với công suất P, điện áp U và điện trở đường dây R.",
   [("Công suất hao phí là ΔP = R·P²/U².", True,
     "Đúng. Từ ΔP = R·I² với I = P/U."),
    ("Nếu tăng đồng thời P và U lên gấp đôi thì hao phí không đổi.", True,
     "Đúng. P² tăng 4 lần, U² cũng tăng 4 lần nên tỉ số không đổi."),
    ("Nếu tăng P lên gấp đôi và giữ nguyên U thì hiệu suất truyền tải giảm.", True,
     "Đúng. Hao phí tăng 4 lần trong khi công suất truyền chỉ tăng 2 lần, nên tỉ lệ hao phí "
     "tăng gấp đôi."),
    ("Nếu tăng U lên gấp đôi và giữ nguyên P thì công suất tới nơi tiêu thụ tăng gấp đôi.", False,
     "Sai. Công suất tới nơi tiêu thụ là P − ΔP; tăng U chỉ làm ΔP giảm 4 lần chứ không làm P "
     "tăng lên. Công suất tới nơi tiêu thụ chỉ tăng thêm một lượng nhỏ.")],
   "Truyền tải – phân tích tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

ds("Một hạt nhân X lần lượt phóng xạ β⁻ rồi phóng xạ α.",
   [("Sau phóng xạ β⁻, số khối của hạt nhân không đổi.", True,
     "Đúng. Electron có số khối bằng 0."),
    ("Sau phóng xạ α, số khối giảm 4 đơn vị.", True,
     "Đúng. Hạt α là ⁴₂He."),
    ("So với X, hạt nhân cuối cùng có điện tích giảm 1 đơn vị.", True,
     "Đúng. Z thay đổi +1 (do β⁻) rồi −2 (do α), tổng cộng −1."),
    ("So với X, hạt nhân cuối cùng có số nơtron giảm 2 đơn vị.", False,
     "Sai. β⁻ làm số nơtron giảm 1 (một nơtron biến thành prôtôn); α làm giảm thêm 2 nơtron. "
     "Tổng cộng số nơtron giảm 3 đơn vị.")],
   "Chuỗi phân rã", RK, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),
],
P3=[
sa("Một bình kín 8,31 L chứa hỗn hợp 0,30 mol khí nitơ và 0,20 mol khí cacbonic ở 27 °C. "
   "Áp suất hỗn hợp bằng bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, làm tròn đến "
   "chữ số thập phân thứ nhất)? Cho R = 8,31 J/(mol·K).",
   "1,5",
   "Tổng số mol: n = 0,30 + 0,20 = 0,50 mol.\n"
   "p = nRT/V = 0,50 · 8,31 · 300/(8,31·10⁻³) = 1246,5/8,31·10⁻³ = 1,5·10⁵ Pa.",
   "Hỗn hợp khí lí tưởng", K),

sa("Một khối khí lí tưởng thực hiện quá trình trong đó áp suất tỉ lệ thuận với thể tích. "
   "Khi thể tích tăng gấp ba thì nhiệt độ tuyệt đối tăng gấp bao nhiêu lần?",
   "9",
   "Từ pV/T = hằng số và p = a·V ⇒ a·V²/T = hằng số ⇒ T tỉ lệ với V².\n"
   "V tăng 3 lần thì T tăng 3² = 9 lần.",
   "Quá trình đặc biệt của khí lí tưởng", RK),

sa("Một khung dây tròn đặt vuông góc với từ trường đều biến thiên. Nếu thay bằng khung cùng vật "
   "liệu, cùng tiết diện dây nhưng bán kính gấp ba thì cường độ dòng cảm ứng tăng gấp bao nhiêu lần?",
   "3",
   "Diện tích tăng 9 lần ⇒ suất điện động tăng 9 lần.\n"
   "Chu vi tăng 3 lần ⇒ điện trở tăng 3 lần.\n"
   "i = e/R tăng 9/3 = 3 lần.",
   "Phân tích tỉ lệ trong cảm ứng điện từ", RK),

sa("Trong hỗn hợp gồm 0,30 mol khí nitơ và 0,20 mol khí cacbonic, áp suất riêng phần của khí nitơ "
   "chiếm bao nhiêu phần trăm áp suất tổng của hỗn hợp?",
   "60",
   "Áp suất riêng phần tỉ lệ thuận với số mol.\n"
   "Tỉ lệ của nitơ: 0,30/(0,30 + 0,20) = 0,60 = 60 %.",
   "Hỗn hợp khí lí tưởng", K),

sa("Một mẫu chất phóng xạ có độ phóng xạ giảm 500 lần sau 90 ngày. Chu kì bán rã của chất đó bằng "
   "bao nhiêu ngày (làm tròn đến chữ số thập phân thứ nhất)? Lấy ln2 ≈ 0,693.",
   "10,0",
   "2ⁿ = 500 ⇒ n = ln500/ln2 = 6,215/0,693 ≈ 8,97 chu kì.\n"
   "T = 90/8,97 ≈ 10,0 ngày.",
   "Định luật phóng xạ – dùng logarit", K),

sa("Một hạt nhân lần lượt phóng xạ hai lần β⁻ rồi ba lần α. So với hạt nhân ban đầu, "
   "số nơtron của hạt nhân cuối cùng giảm bao nhiêu đơn vị?",
   "8",
   "Mỗi lần β⁻ làm số nơtron giảm 1 (nơtron biến thành prôtôn): 2 lần ⇒ giảm 2.\n"
   "Mỗi lần α làm số nơtron giảm 2: 3 lần ⇒ giảm 6.\n"
   "Tổng cộng số nơtron giảm 2 + 6 = 8 đơn vị.",
   "Chuỗi phân rã", RK),
])


# =====================================================================  ĐỀ 20
DE20 = dict(
ma="TH-Đề 20", ten="ĐỀ THI THỬ SỐ 20", muc="Khó",
trongtam="Tổng duyệt nhóm đề Khó: đồ thị, biện luận và phân tích tỉ lệ",
P1=[
mc("Một bình cách nhiệt chứa 1,0 kg nước ở 80 °C. Thả vào đó 1,0 kg nước đá ở 0 °C. "
   "Nhiệt độ cân bằng bằng (λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K))",
   ["0 °C.", "0 °C và còn dư nước đá.", "10,5 °C.", "40 °C."],
   "B",
   "Nhiệt nước nóng nhả tối đa: 1,0 · 4200 · 80 = 336 000 J.\n"
   "Nhiệt cần để tan hết 1,0 kg đá: 1,0 · 3,4·10⁵ = 340 000 J > 336 000 J.\n"
   "Nhiệt nhả ra không đủ nên đá chỉ tan một phần, hỗn hợp dừng ở 0 °C và vẫn còn nước đá.",
   "Biện luận điều kiện", RK),

mc("Trong bài trên, khối lượng nước đá đã tan xấp xỉ",
   ["1,00 kg.", "0,988 kg.", "0,500 kg.", "0,800 kg."],
   "B",
   "Khối lượng tan: m = 336 000/3,4·10⁵ ≈ 0,988 kg.\n"
   "Còn lại khoảng 1,000 − 0,988 = 0,012 kg nước đá chưa tan.",
   "Biện luận điều kiện", RK),

mc("Một khối khí lí tưởng thực hiện quá trình mà thể tích tỉ lệ thuận với nhiệt độ tuyệt đối. "
   "Quá trình đó là",
   ["đẳng nhiệt.", "đẳng áp.", "đẳng tích.", "đoạn nhiệt."],
   "B",
   "V tỉ lệ thuận với T chính là nội dung định luật Charles cho quá trình đẳng áp.",
   "Nhận dạng quá trình", TB),

mc("Một khối khí lí tưởng có áp suất tỉ lệ nghịch với bình phương thể tích. Khi thể tích tăng "
   "gấp đôi thì nhiệt độ tuyệt đối",
   ["tăng gấp đôi.", "giảm một nửa.", "không đổi.", "giảm bốn lần."],
   "B",
   "Từ pV/T = hằng số và p = a/V² ta có a/(V·T) = hằng số, tức T tỉ lệ nghịch với V.\n"
   "V tăng gấp đôi thì T giảm một nửa.",
   "Quá trình đặc biệt của khí lí tưởng", RK),

mc("Ở 27 °C, áp suất một khối khí là p. Muốn áp suất tăng 50 % mà giữ nguyên thể tích thì phải "
   "nung nóng khí tới",
   ["127 °C.", "177 °C.", "77 °C.", "227 °C."],
   "B",
   "Đẳng tích: T₂ = 1,50 · T₁ = 1,50 · 300 = 450 K.\n"
   "t₂ = 450 − 273 = 177 °C.",
   "Định luật Gay-Lussac", K),

mc("Một khung dây vuông cạnh a chuyển động đều đi qua vùng từ trường đều rộng d. "
   "Nếu d < a thì trong quá trình đi qua, khung có",
   ["dòng cảm ứng liên tục trong suốt quá trình.",
    "một khoảng thời gian không có dòng cảm ứng.",
    "dòng cảm ứng luôn cùng chiều.", "không có dòng cảm ứng nào."],
   "B",
   "Khi cạnh trước đã ra khỏi vùng mà cạnh sau chưa vào, phần khung nằm trong từ trường luôn là "
   "dải rộng đúng d nên từ thông không đổi, không có dòng cảm ứng. Giai đoạn đó ứng với quãng "
   "đường a − d.",
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

mc("Một thanh dẫn khối lượng 80 g, dài 40 cm nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,50 T. Truyền cho thanh vận tốc 6,0 m/s. "
   "Tổng điện lượng qua mạch cho tới khi thanh dừng bằng",
   ["1,2 C.", "2,4 C.", "4,8 C.", "0,6 C."],
   "B",
   "B·ℓ·q = m·v₀ ⇒ q = 0,080 · 6,0/(0,50 · 0,40) = 0,48/0,20 = 2,4 C.",
   "Xung lượng của lực từ", K, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Với bài toán trên, tổng nhiệt lượng toả ra trên mạch bằng",
   ["0,72 J.", "1,44 J.", "2,88 J.", "0,36 J."],
   "B",
   "Q = ½·m·v₀² = 0,5 · 0,080 · 36 = 1,44 J. Kết quả không phụ thuộc B, ℓ hay R.",
   "Bảo toàn năng lượng", K),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng, hai cuộn thứ cấp 200 vòng và 100 vòng "
   "nối với hai điện trở 20 Ω và 5,0 Ω. Điện áp sơ cấp 220 V. Công suất tổng bằng",
   ["96,8 W.", "193,6 W.", "48,4 W.", "145,2 W."],
   "B",
   "Cuộn 200 vòng: U = 220 · 0,20 = 44 V ⇒ P₁ = 44²/20 = 1936/20 = 96,8 W.\n"
   "Cuộn 100 vòng: U = 220 · 0,10 = 22 V ⇒ P₂ = 22²/5,0 = 484/5,0 = 96,8 W.\n"
   "Tổng: 96,8 + 96,8 = 193,6 W.",
   "Máy biến áp nhiều cuộn thứ cấp", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất 10 MW đi xa. Ở điện áp U₁, hao phí chiếm 8 %. Muốn hao phí chỉ còn 2 % thì "
   "phải tăng điện áp lên gấp",
   ["1,5 lần.", "2,0 lần.", "4,0 lần.", "2,5 lần."],
   "B",
   "Hao phí giảm 4 lần; vì hao phí tỉ lệ nghịch với U² nên U phải tăng √4 = 2,0 lần.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây quay đều trong từ trường đều với tần số f, nối với điện trở R. "
   "Nếu giảm tần số còn f/2 và tăng số vòng dây lên gấp bốn thì công suất trung bình",
   ["không đổi.", "tăng gấp bốn.", "tăng gấp đôi.", "giảm một nửa."],
   "B",
   "E₀ = ω·N·B·S: ω giảm 2 lần, N tăng 4 lần ⇒ E₀ tăng 2 lần.\n"
   "P = E₀²/(2R) tăng 2² = 4 lần.",
   "Máy phát và công suất", RK),

mc("Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ. Nếu ban đầu mẫu có độ phóng xạ 1,6·10⁶ Bq thì "
   "tổng số phân rã xảy ra cho tới khi mẫu phân rã hết xấp xỉ (ln2 ≈ 0,693)",
   ["1,66·10¹⁰.", "3,32·10¹⁰.", "6,64·10¹⁰.", "8,30·10⁹."],
   "B",
   "Tổng số phân rã bằng số hạt nhân ban đầu: N₀ = H₀·T/ln2.\n"
   "T = 4,0 · 3600 = 14 400 s.\n"
   "N₀ = 1,6·10⁶ · 14 400/0,693 ≈ 2,304·10¹⁰/0,693 ≈ 3,32·10¹⁰ hạt.",
   "Độ phóng xạ và tổng số phân rã", RK),

mc("Một mẫu chất phóng xạ nguyên chất, sau thời gian t₁ thì tỉ số giữa số hạt nhân đã rã và còn lại "
   "bằng 1. Sau thời gian 3·t₁, tỉ số đó bằng",
   ["3.", "7.", "9.", "15."],
   "B",
   "Tỉ số bằng 1 ⇒ 2ⁿ − 1 = 1 ⇒ n = 1, tức t₁ = T.\n"
   "Sau 3t₁ = 3T: tỉ số = 2³ − 1 = 7.",
   "Tỉ số hạt nhân con và mẹ", K),

mc("Hạt nhân ⁴₂He có năng lượng liên kết 28,4 MeV; ⁶₃Li có 32,0 MeV. Phản ứng "
   "¹₁H + ⁹₄Be → ⁴₂He + ⁶₃Li (biết ⁹₄Be có năng lượng liên kết 58,2 MeV) toả ra xấp xỉ",
   ["1,1 MeV.", "2,2 MeV.", "3,3 MeV.", "4,4 MeV."],
   "B",
   "Năng lượng liên kết trước: prôtôn có W(lk) = 0; ⁹Be có 58,2 MeV ⇒ tổng 58,2 MeV.\n"
   "Năng lượng liên kết sau: 28,4 + 32,0 = 60,4 MeV.\n"
   "ΔE = 60,4 − 58,2 = 2,2 MeV.",
   "Năng lượng phản ứng theo W(lk)", RK),

mc("Một chất phóng xạ có chu kì bán rã T. Số hạt nhân phân rã trong khoảng thời gian từ 2T đến 3T "
   "so với số hạt phân rã từ 0 đến T bằng",
   ["1/2.", "1/4.", "1/8.", "1/3."],
   "B",
   "Từ 0 đến T: N₀ − N₀/2 = N₀/2.\n"
   "Từ 2T đến 3T: N₀/4 − N₀/8 = N₀/8.\n"
   "Tỉ số: (N₀/8)/(N₀/2) = 1/4.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Trong lò phản ứng, nếu tất cả thanh điều khiển được rút hết ra khỏi vùng hoạt động thì",
   ["phản ứng dừng ngay.", "hệ số nhân nơtron vượt quá 1 và công suất tăng nhanh.",
    "hệ số nhân nơtron giảm về 0.", "nhiên liệu bị đông cứng."],
   "B",
   "Thanh điều khiển hấp thụ nơtron. Rút hết thanh ra thì số nơtron gây phân hạch tăng, "
   "k > 1 và công suất lò tăng rất nhanh — đây là tình huống nguy hiểm cần tuyệt đối tránh.",
   "Điều khiển lò phản ứng", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("So sánh năng lượng toả ra khi phân hạch hoàn toàn 1 kg ²³⁵U với khi đốt cháy 1 kg than "
   "(toả khoảng 3·10⁷ J/kg), tỉ số xấp xỉ",
   ["2,7·10³ lần.", "2,7·10⁶ lần.", "2,7·10⁹ lần.", "2,7·10¹² lần."],
   "B",
   "Phân hạch 1 kg ²³⁵U toả khoảng 8,2·10¹³ J.\n"
   "Tỉ số: 8,2·10¹³/(3·10⁷) ≈ 2,7·10⁶ lần.",
   "So sánh các nguồn năng lượng", K),

mc("Trong quá trình vận hành lò phản ứng, người ta phải kiểm soát nhiệt độ chặt chẽ chủ yếu vì",
   ["nhiệt độ cao làm chu kì bán rã giảm.",
    "nhiệt độ cao có thể làm hỏng thanh nhiên liệu và mất khả năng làm mát.",
    "nhiệt độ cao làm tăng số prôtôn.",
    "nhiệt độ cao làm nơtron biến mất."],
   "B",
   "Chu kì bán rã không phụ thuộc nhiệt độ. Vấn đề thực sự là nhiệt độ quá cao sẽ phá huỷ vỏ bọc "
   "thanh nhiên liệu và làm hệ thống làm mát mất tác dụng, dẫn tới sự cố nghiêm trọng.",
   "An toàn hạt nhân", K),
],
P2=[
ds("Thả 1,0 kg nước đá ở 0 °C vào 1,0 kg nước ở 80 °C trong bình cách nhiệt. "
   "Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng tối đa mà nước nóng nhả ra là 336 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 80 = 336 000 J."),
    ("Nhiệt lượng cần để làm tan hết 1,0 kg nước đá là 340 kJ.", True,
     "Đúng. Q = 1,0 · 3,4·10⁵ = 340 000 J."),
    ("Nước đá chỉ tan một phần và nhiệt độ cân bằng là 0 °C.", True,
     "Đúng. 336 kJ < 340 kJ nên không đủ nhiệt để tan hết đá."),
    ("Khối lượng nước đá còn lại xấp xỉ 0,12 kg.", False,
     "Sai. Khối lượng đá đã tan là 336 000/3,4·10⁵ ≈ 0,988 kg, nên còn lại khoảng 0,012 kg "
     "chứ không phải 0,12 kg.")],
   "Biện luận điều kiện", RK),

ds("Một khung dây vuông cạnh 45 cm, điện trở 0,90 Ω, chuyển động đều 3,0 m/s đi qua vùng từ trường "
   "đều rộng 30 cm, B = 0,60 T, đường sức vuông góc mặt phẳng khung.",
   [("Vì bề rộng vùng nhỏ hơn cạnh khung nên có giai đoạn không có dòng cảm ứng.", True,
     "Đúng. Khi khung vắt qua vùng, phần diện tích nằm trong từ trường không đổi."),
    ("Giai đoạn không có dòng cảm ứng kéo dài 0,050 s.", True,
     "Đúng. Quãng đường tương ứng 45 − 30 = 15 cm ⇒ t = 0,15/3,0 = 0,050 s."),
    ("Suất điện động cảm ứng lúc khung đi vào bằng 0,81 V.", True,
     "Đúng. e = B·a·v = 0,60 · 0,45 · 3,0 = 0,81 V."),
    ("Cường độ dòng cảm ứng lúc khung đi vào bằng 1,8 A.", False,
     "Sai. i = e/R = 0,81/0,90 = 0,90 A chứ không phải 1,8 A.")],
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng nối vào mạng 220 V, hai cuộn thứ cấp độc lập "
   "200 vòng và 100 vòng nối lần lượt với hai điện trở 20 Ω và 5,0 Ω.",
   [("Điện áp ở cuộn 200 vòng là 44 V.", True,
     "Đúng. U = 220 · 200/1000 = 44 V."),
    ("Công suất tiêu thụ ở cuộn 200 vòng là 96,8 W.", True,
     "Đúng. P = 44²/20 = 1936/20 = 96,8 W."),
    ("Công suất tiêu thụ ở cuộn 100 vòng cũng là 96,8 W.", True,
     "Đúng. U = 22 V ⇒ P = 484/5,0 = 96,8 W."),
    ("Cường độ dòng điện ở cuộn sơ cấp xấp xỉ 0,44 A.", False,
     "Sai. Tổng công suất là 193,6 W nên I₁ = 193,6/220 = 0,88 A.")],
   "Máy biến áp nhiều cuộn thứ cấp", RK, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ và độ phóng xạ ban đầu 1,6·10⁶ Bq. "
   "Cho ln2 ≈ 0,693.",
   [("Hằng số phóng xạ xấp xỉ 4,81·10⁻⁵ s⁻¹.", True,
     "Đúng. T = 14 400 s ⇒ λ = 0,693/14 400 ≈ 4,81·10⁻⁵ s⁻¹."),
    ("Số hạt nhân ban đầu xấp xỉ 3,32·10¹⁰ hạt.", True,
     "Đúng. N₀ = H₀/λ = 1,6·10⁶/4,81·10⁻⁵ ≈ 3,33·10¹⁰ hạt."),
    ("Tổng số phân rã cho tới khi mẫu hết hẳn bằng số hạt nhân ban đầu.", True,
     "Đúng. Mỗi hạt nhân chỉ phân rã một lần."),
    ("Sau 4,0 giờ, tổng số phân rã đã xảy ra bằng toàn bộ N₀.", False,
     "Sai. Sau một chu kì bán rã mới có một nửa số hạt nhân phân rã, tức N₀/2.")],
   "Độ phóng xạ và tổng số phân rã", RK),
],
P3=[
sa("Thả 1,0 kg nước đá ở 0 °C vào 1,2 kg nước ở 70 °C trong bình cách nhiệt. Khối lượng nước đá "
   "đã tan bằng bao nhiêu kilôgam (làm tròn đến chữ số thập phân thứ ba)? "
   "Cho λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K).",
   "1",
   "Nhiệt nước nóng nhả ra tối đa khi hạ về 0 °C: 1,2 · 4200 · 70 = 352 800 J.\n"
   "Nhiệt cần để làm tan hết 1,0 kg đá: 1,0 · 3,4·10⁵ = 340 000 J.\n"
   "Vì 352 800 > 340 000 nên đá TAN HẾT: khối lượng đá đã tan = 1 kg.",
   "Biện luận điều kiện", RK),

sa("Một khối khí lí tưởng ở 27 °C có áp suất p. Muốn áp suất tăng 80 % mà giữ nguyên thể tích thì "
   "phải nung nóng khí tới bao nhiêu độ Celsius?",
   "267",
   "Đẳng tích nên p tỉ lệ thuận với T:  T₂ = 1,80 · 300 = 540 K.\n"
   "t₂ = 540 − 273 = 267 °C.",
   "Định luật Gay-Lussac", K),

sa("Một thanh dẫn khối lượng 150 g nằm trên hai ray nằm ngang không ma sát trong từ trường đều "
   "thẳng đứng. Truyền cho thanh vận tốc ban đầu 10 m/s rồi để tự do. Tổng nhiệt lượng toả ra trên "
   "mạch cho tới khi thanh dừng hẳn bằng bao nhiêu jun (làm tròn đến chữ số thập phân thứ nhất)?",
   "7,5",
   "Không có ma sát nên toàn bộ động năng ban đầu chuyển thành nhiệt:\n"
   "Q = ½·m·v₀² = 0,5 · 0,150 · 100 = 7,5 J.\n"
   "Kết quả không phụ thuộc cảm ứng từ, chiều dài thanh hay điện trở mạch.",
   "Bảo toàn năng lượng", K),

sa("Một khung dây quay đều trong từ trường đều nối với điện trở R. Nếu giảm tần số quay còn một nửa "
   "và tăng số vòng dây lên gấp sáu thì công suất trung bình tăng gấp bao nhiêu lần?",
   "9",
   "E₀ = ω·N·B·S: ω giảm 2 lần, N tăng 6 lần ⇒ E₀ tăng 3 lần.\n"
   "P = E₀²/(2R) tăng 3² = 9 lần.",
   "Máy phát và công suất", RK),

sa("Một mẫu chất phóng xạ có chu kì bán rã 5,0 giờ và độ phóng xạ ban đầu 2,0·10⁶ Bq. "
   "Tổng số phân rã xảy ra cho tới khi mẫu phân rã hết bằng bao nhiêu (viết dưới dạng x·10¹⁰, "
   "chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)? Lấy ln2 ≈ 0,693.",
   "5,2",
   "T = 5,0 · 3600 = 18 000 s.\n"
   "N₀ = H₀·T/ln2 = 2,0·10⁶ · 18 000/0,693 = 3,6·10¹⁰/0,693 ≈ 5,2·10¹⁰ hạt.",
   "Độ phóng xạ và tổng số phân rã", RK),

sa("Hạt nhân ⁴₂He có năng lượng liên kết 28,4 MeV; ⁷₃Li có 39,2 MeV. Phản ứng "
   "¹₁H + ⁷₃Li → 2·⁴₂He toả ra bao nhiêu MeV (làm tròn đến chữ số thập phân thứ nhất)?",
   "17,6",
   "Năng lượng liên kết trước: prôtôn có W(lk) = 0; ⁷Li có 39,2 MeV ⇒ tổng 39,2 MeV.\n"
   "Năng lượng liên kết sau: 2 · 28,4 = 56,8 MeV.\n"
   "ΔE = 56,8 − 39,2 = 17,6 MeV.",
   "Năng lượng phản ứng theo W(lk)", RK),
])


NHOM = dict(
    ten_nhom="ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG  (Đề 16 – 20)",
    mo_ta="Năm đề mức Khó, tập trung vào vận dụng nhiều bước và phân tích tỉ lệ",
    pham_vi=(
        "Chương I. Vật lí nhiệt  •  Chương II. Khí lí tưởng  •  "
        "Chương III. Từ trường  •  Chương IV. Vật lí hạt nhân\n"
        "Mỗi đề gồm 28 câu / 40 lệnh hỏi, thời gian 50 phút, thang điểm 10.\n"
        "Hằng số: c(nước) = 4200 J/(kg·K); λ(nước đá) = 3,4·10⁵ J/kg; L(nước) = 2,26·10⁶ J/kg; "
        "g = 10 m/s²; R = 8,31 J/(mol·K); Nₐ = 6,02·10²³ mol⁻¹; 1 u·c² = 931,5 MeV; "
        "1 MeV = 1,6·10⁻¹³ J; π ≈ 3,1416; √2 ≈ 1,414; ln2 ≈ 0,693."),
    tests=[DE16, DE17, DE18, DE19, DE20],
)
