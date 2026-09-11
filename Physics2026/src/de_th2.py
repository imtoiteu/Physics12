# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.  Đề 06 – 10 (Trung bình)."""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 06
DE6 = dict(
ma="TH-Đề 06", ten="ĐỀ THI THỬ SỐ 06", muc="Trung bình",
trongtam="Đọc đồ thị, bài toán thực nghiệm và vận dụng công thức nhiều bước",
P1=[
mc("Đồ thị nhiệt lượng Q theo độ tăng nhiệt độ ΔT của hai mẫu chất cùng khối lượng là hai đường "
   "thẳng qua gốc toạ độ. Mẫu có đường DỐC HƠN thì",
   ["nhiệt dung riêng nhỏ hơn.", "nhiệt dung riêng lớn hơn.",
    "khối lượng lớn hơn.", "nhiệt độ sôi thấp hơn."],
   "B",
   "Từ Q = mcΔT, hệ số góc của đường thẳng bằng m·c. Cùng khối lượng nên đường dốc hơn ứng với "
   "nhiệt dung riêng lớn hơn.",
   "Đọc đồ thị Q – ΔT", TB, fig="n_dt_QdT", cap="Nhiệt lượng theo độ tăng nhiệt độ"),

mc("Trong thí nghiệm đo nhiệt dung riêng của nước bằng điện trở đun, công thức xác định c là",
   ["c = U·I·t·m·ΔT.", "c = U·I·t/(m·ΔT).", "c = m·ΔT/(U·I·t).", "c = U·I/(m·ΔT)."],
   "B",
   "Nhiệt lượng điện cung cấp Q = U·I·t phải bằng m·c·ΔT, suy ra c = U·I·t/(m·ΔT).",
   "Thí nghiệm đo nhiệt dung riêng", TB, fig="n_sd_tn_do_c", cap="Bố trí thí nghiệm đo c"),

mc("Trong thí nghiệm trên, nguồn sai số chính khiến giá trị c đo được LỚN hơn thực tế là",
   ["nhiệt kế chỉ sai.", "nhiệt toả ra môi trường và nhiệt mà bình thu vào.",
    "dòng điện không ổn định.", "nước bay hơi nhiều."],
   "B",
   "Một phần nhiệt lượng điện không dùng để làm nóng nước mà thất thoát ra môi trường và làm nóng "
   "bình. Vì vẫn tính toàn bộ U·I·t cho nước nên c tính được lớn hơn giá trị thực.",
   "Sai số thí nghiệm", TB, fig="n_sd_tn_do_c", cap="Bố trí thí nghiệm đo c"),

mc("Một khối khí thực hiện quá trình đẳng áp và sinh công 400 J, đồng thời thu nhiệt 1000 J. "
   "Nội năng của khí biến thiên",
   ["−600 J.", "+600 J.", "+1400 J.", "−1400 J."],
   "B",
   "Khí SINH công nên A = −400 J; khí THU nhiệt nên Q = +1000 J.\n"
   "ΔU = A + Q = −400 + 1000 = +600 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Ba quá trình cùng xuất phát từ một trạng thái M trên đồ thị (p, V): đường thẳng đứng, "
   "đường hypebol và đường nằm ngang. Đường NẰM NGANG ứng với quá trình",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "đoạn nhiệt."],
   "B",
   "Đường nằm ngang trong hệ (p, V) nghĩa là áp suất không đổi khi thể tích thay đổi — "
   "đó là quá trình đẳng áp.",
   "Nhận dạng quá trình từ đồ thị", TB, fig="k_dt_baquatrinh",
   cap="Ba quá trình xuất phát từ trạng thái M"),

mc("Một ống thuỷ tinh một đầu kín đặt thẳng đứng, miệng ở TRÊN, giam cột khí dài 30 cm bằng cột "
   "thuỷ ngân dài 10 cm. Áp suất khí quyển 75 cmHg. Áp suất của cột khí bằng",
   ["65 cmHg.", "85 cmHg.", "75 cmHg.", "10 cmHg."],
   "B",
   "Miệng ống ở TRÊN nên cột thuỷ ngân đè xuống khí, cộng thêm áp suất khí quyển:\n"
   "p = 75 + 10 = 85 cmHg.",
   "Cột khí bị giam bởi thuỷ ngân", K, fig="k_sd_ong_khi", cap="Cột khí trong ống thuỷ tinh"),

mc("Lật ngược ống ở câu trên cho miệng xuống dưới (nhiệt độ không đổi), chiều dài cột khí xấp xỉ",
   ["30 cm.", "39 cm.", "23 cm.", "45 cm."],
   "B",
   "Miệng ở DƯỚI: p₂ = 75 − 10 = 65 cmHg.\n"
   "Đẳng nhiệt: p₁ℓ₁ = p₂ℓ₂ ⇒ 85 · 30 = 65 · ℓ₂ ⇒ ℓ₂ = 2550/65 ≈ 39 cm.\n"
   "Áp suất giảm nên cột khí dài ra — kết quả hợp lí.",
   "Cột khí bị giam bởi thuỷ ngân", K, fig="k_sd_ong_khi", cap="Cột khí trong ống thuỷ tinh"),

mc("Áp suất của chất khí theo mô hình động học phân tử được tính bằng",
   ["p = μ·m₀·v̄².", "p = (1/3)·μ·m₀·v̄².", "p = 3·μ·m₀·v̄².", "p = μ/(m₀·v̄²)."],
   "B",
   "p = (1/3)·μ·m₀·v̄², với μ là mật độ phân tử và m₀ là khối lượng một phân tử. "
   "Kết hợp với W̄ₐ = ½m₀v̄² được p = (2/3)·μ·W̄ₐ.",
   "Áp suất theo mô hình động học", TB, fig="k_sd_vacham_thanh",
   cap="Va chạm phân tử lên thành bình"),

mc("Một đoạn dây dẫn dài 40 cm mang dòng điện 2,5 A đặt trong từ trường đều B = 0,60 T, "
   "hợp với đường sức góc 30°. Lực từ tác dụng lên dây bằng",
   ["0,60 N.", "0,30 N.", "0,15 N.", "1,20 N."],
   "B",
   "F = B·I·ℓ·sin30° = 0,60 · 2,5 · 0,40 · 0,50 = 0,30 N.",
   "Lực từ", TB),

mc("Từ thông qua một vòng dây biến thiên theo đồ thị gồm bốn giai đoạn. Giai đoạn nào có suất "
   "điện động cảm ứng bằng không?",
   ["Giai đoạn (I).", "Giai đoạn (II).", "Giai đoạn (III).", "Giai đoạn (IV)."],
   "B",
   "Suất điện động tỉ lệ với độ dốc của đồ thị Φ(t). Giai đoạn (II) đồ thị nằm ngang nên độ dốc "
   "bằng 0, không có suất điện động.",
   "Đọc đồ thị từ thông", TB, fig="t_dt_phi_t", cap="Từ thông theo thời gian"),

mc("Một khung dây kín được kéo ra khỏi vùng từ trường đều. Lực cần tác dụng để kéo khung đi với "
   "tốc độ không đổi",
   ["bằng không vì không có ma sát.", "phải cân bằng với lực từ cản do dòng cảm ứng gây ra.",
    "hướng ngược chiều chuyển động.", "chỉ phụ thuộc khối lượng khung."],
   "B",
   "Theo định luật Lenz, dòng cảm ứng tạo lực cản trở chuyển động. Muốn khung đi đều, lực kéo phải "
   "cân bằng đúng lực cản đó; công của lực kéo chuyển thành nhiệt trên khung.",
   "Năng lượng trong cảm ứng điện từ", K, fig="t_sd_khung_vao_B",
   cap="Khung dây ra khỏi vùng từ trường"),

mc("Một máy biến áp lí tưởng có tỉ số vòng dây sơ cấp trên thứ cấp là 10 : 1. "
   "Nếu cường độ dòng điện ở cuộn thứ cấp là 5,0 A thì ở cuộn sơ cấp là",
   ["50 A.", "0,50 A.", "5,0 A.", "0,05 A."],
   "B",
   "Máy lí tưởng bảo toàn công suất: I₁/I₂ = N₂/N₁ = 1/10.\n"
   "I₁ = 5,0/10 = 0,50 A. Điện áp tăng thì dòng giảm và ngược lại.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Trong đồ thị cường độ dòng điện xoay chiều theo thời gian, hai đường nét đứt ứng với ±I₀/√2. "
   "Phần thời gian mà |i| lớn hơn giá trị đó chiếm",
   ["một phần tư chu kì.", "một nửa chu kì.",
    "ba phần tư chu kì.", "toàn bộ chu kì."],
   "B",
   "Với dao động hình sin, |i| vượt quá I₀/√2 đúng một nửa thời gian: bốn khoảng mỗi khoảng T/8, "
   "tổng cộng T/2.",
   "Đọc đồ thị dòng xoay chiều", K, fig="t_dt_i_t", cap="Cường độ dòng điện xoay chiều"),

mc("Trên đường cong năng lượng liên kết riêng, phản ứng nhiệt hạch tương ứng với việc đi",
   ["từ vùng A lớn về vùng A ≈ 56.", "từ vùng A rất nhỏ về vùng A ≈ 56.",
    "từ vùng A ≈ 56 ra vùng A lớn.", "từ vùng A ≈ 56 về vùng A nhỏ."],
   "B",
   "Nhiệt hạch kết hợp các hạt nhân RẤT NHẸ thành hạt nhân nặng hơn, tức đi từ vùng A rất nhỏ "
   "tiến về vùng đỉnh A ≈ 56 của đường cong. Vì ε tăng lên nên phản ứng toả năng lượng.",
   "Đường cong năng lượng liên kết riêng", TB, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Một mẫu chất phóng xạ có độ phóng xạ giảm từ 800 kBq xuống 100 kBq trong 12 giờ. "
   "Chu kì bán rã của chất đó bằng",
   ["2,0 giờ.", "4,0 giờ.", "6,0 giờ.", "3,0 giờ."],
   "B",
   "Tỉ số giảm: 800/100 = 8 = 2³ nên n = 3 chu kì.\n"
   "T = 12/3 = 4,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB, fig="h_dt_H_t", cap="Độ phóng xạ theo thời gian"),

mc("Cho phản ứng: ²³⁵₉₂U + ¹₀n → ¹⁴⁰₅₄Xe + ⁹⁴₃₈Sr + k·¹₀n. Giá trị của k bằng",
   ["1.", "2.", "3.", "4."],
   "B",
   "Bảo toàn số khối: 235 + 1 = 140 + 94 + k ⇒ 236 = 234 + k ⇒ k = 2.\n"
   "Kiểm tra điện tích: 92 = 54 + 38 ✓.",
   "Phản ứng phân hạch", TB, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Liều chiếu mà một người nhận từ nguồn phóng xạ điểm sẽ giảm 9 lần nếu người đó",
   ["đứng xa nguồn gấp 9 lần.", "đứng xa nguồn gấp 3 lần.",
    "giảm thời gian tiếp xúc 9 lần rồi tiến lại gần.", "đeo găng tay cao su."],
   "B",
   "Liều chiếu từ nguồn điểm tỉ lệ nghịch với bình phương khoảng cách. Muốn giảm 9 lần thì "
   "khoảng cách phải tăng √9 = 3 lần.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Nếu tính trên cùng một khối lượng nhiên liệu, phản ứng nhiệt hạch toả năng lượng nhiều hơn "
   "phân hạch vì",
   ["mỗi phản ứng nhiệt hạch toả nhiều MeV hơn.",
    "năng lượng tính trên mỗi nuclêôn của nhiệt hạch lớn hơn.",
    "nhiệt hạch cần nhiệt độ cao hơn.",
    "nhiên liệu nhiệt hạch rẻ hơn."],
   "B",
   "Mỗi phản ứng nhiệt hạch chỉ toả 17,6 MeV so với 200 MeV của phân hạch, nhưng tính trên mỗi "
   "nuclêôn thì nhiệt hạch cho khoảng 3,5 MeV còn phân hạch chỉ 0,85 MeV.",
   "So sánh phân hạch và nhiệt hạch", K),
],
P2=[
ds("Trong một thí nghiệm, người ta dùng điện trở đun có U = 12 V, I = 2,5 A để đun 0,20 kg nước "
   "trong bình cách nhiệt. Sau 5,0 phút, nhiệt độ nước tăng thêm 10 °C.",
   [("Nhiệt lượng điện cung cấp trong 5,0 phút là 9000 J.", True,
     "Đúng. Q = U·I·t = 12 · 2,5 · 300 = 9000 J."),
    ("Nhiệt dung riêng của nước tính được từ thí nghiệm là 4500 J/(kg·K).", True,
     "Đúng. c = Q/(m·ΔT) = 9000/(0,20 · 10) = 4500 J/(kg·K)."),
    ("Giá trị đo được lớn hơn giá trị thực 4200 J/(kg·K).", True,
     "Đúng. Nguyên nhân là một phần nhiệt đã thất thoát ra môi trường và làm nóng bình."),
    ("Nếu bọc cách nhiệt tốt hơn thì giá trị c đo được sẽ tăng lên.", False,
     "Sai. Cách nhiệt tốt hơn làm giảm thất thoát nên giá trị đo được sẽ GIẢM, tiến gần tới "
     "giá trị thực 4200 J/(kg·K).")],
   "Thí nghiệm đo nhiệt dung riêng", TB, fig="n_sd_tn_do_c", cap="Bố trí thí nghiệm đo c"),

ds("Một ống thuỷ tinh một đầu kín, tiết diện đều, đặt thẳng đứng với miệng ở trên, giam một cột khí "
   "dài 30 cm bằng cột thuỷ ngân dài 10 cm. Áp suất khí quyển là 75 cmHg, nhiệt độ không đổi.",
   [("Áp suất của cột khí khi miệng ống ở trên là 85 cmHg.", True,
     "Đúng. Cột thuỷ ngân đè xuống nên p = 75 + 10 = 85 cmHg."),
    ("Khi lật ngược ống cho miệng xuống dưới, áp suất cột khí là 65 cmHg.", True,
     "Đúng. Lúc này thuỷ ngân kéo xuống làm giảm áp lên khí: p = 75 − 10 = 65 cmHg."),
    ("Chiều dài cột khí sau khi lật xấp xỉ 39 cm.", True,
     "Đúng. 85 · 30 = 65 · ℓ ⇒ ℓ = 2550/65 ≈ 39,2 cm."),
    ("Sau khi lật, cột khí ngắn lại vì thuỷ ngân dồn xuống.", False,
     "Sai. Áp suất giảm từ 85 xuống 65 cmHg nên theo định luật Boyle cột khí phải DÀI RA.")],
   "Cột khí bị giam bởi thuỷ ngân", K, fig="k_sd_ong_khi", cap="Cột khí trong ống thuỷ tinh"),

ds("Cho đồ thị từ thông qua một vòng dây dẫn kín có điện trở 0,25 Ω theo thời gian, gồm bốn "
   "giai đoạn (I), (II), (III), (IV).",
   [("Giai đoạn (I) có suất điện động cảm ứng độ lớn 0,20 V.", True,
     "Đúng. Từ thông tăng từ 0 lên 0,40 Wb trong 2 s: |e| = 0,40/2 = 0,20 V."),
    ("Giai đoạn (II) không có dòng điện cảm ứng.", True,
     "Đúng. Từ thông không đổi nên độ dốc bằng 0."),
    ("Giai đoạn (III) có cường độ dòng cảm ứng 1,6 A.", True,
     "Đúng. |e| = 0,40/1 = 0,40 V ⇒ i = 0,40/0,25 = 1,6 A."),
    ("Giai đoạn (IV) có suất điện động lớn hơn giai đoạn (III).", False,
     "Sai. Giai đoạn (IV) từ thông giảm 0,60 Wb trong 3 s nên |e| = 0,20 V, nhỏ hơn 0,40 V "
     "của giai đoạn (III).")],
   "Đọc đồ thị từ thông", K, fig="t_dt_phi_t", cap="Từ thông qua vòng dây theo thời gian"),

ds("Một mẫu chất phóng xạ có độ phóng xạ ban đầu 1600 Bq, chu kì bán rã 5,0 giờ.",
   [("Hằng số phóng xạ xấp xỉ 0,139 giờ⁻¹.", True,
     "Đúng. λ = 0,693/5,0 = 0,1386 ≈ 0,139 giờ⁻¹."),
    ("Sau 15 giờ, độ phóng xạ còn 200 Bq.", True,
     "Đúng. n = 3 ⇒ H = 1600/8 = 200 Bq."),
    ("Đồ thị lnH theo thời gian là đường thẳng có hệ số góc −0,139 giờ⁻¹.", True,
     "Đúng. lnH = lnH₀ − λt nên hệ số góc bằng −λ."),
    ("Sau 20 giờ, độ phóng xạ bằng 0.", False,
     "Sai. Sau 20 giờ (4 chu kì) vẫn còn 1600/16 = 100 Bq. Về lí thuyết độ phóng xạ giảm theo "
     "hàm mũ và không bao giờ bằng đúng 0.")],
   "Độ phóng xạ", TB, fig="h_dt_H_t", cap="Độ phóng xạ theo thời gian"),
],
P3=[
sa("Trong thí nghiệm đo nhiệt dung riêng, dùng U = 10 V, I = 3,0 A đun 0,25 kg chất lỏng trong "
   "4,0 phút thì nhiệt độ tăng thêm 8,0 °C. Nhiệt dung riêng đo được bằng bao nhiêu J/(kg·K)?",
   "3600",
   "Nhiệt lượng điện: Q = U·I·t = 10 · 3,0 · 240 = 7200 J.\n"
   "c = Q/(m·ΔT) = 7200/(0,25 · 8,0) = 7200/2,0 = 3600 J/(kg·K).",
   "Thí nghiệm đo nhiệt dung riêng", TB),

sa("Một ống thuỷ tinh một đầu kín đặt thẳng đứng miệng ở dưới, giam cột khí dài 20 cm bằng cột "
   "thuỷ ngân dài 15 cm. Áp suất khí quyển 75 cmHg. Lật ngược ống cho miệng lên trên, "
   "chiều dài cột khí bằng bao nhiêu centimét?",
   "13,3",
   "Miệng ở DƯỚI: p₁ = 75 − 15 = 60 cmHg.\n"
   "Miệng ở TRÊN: p₂ = 75 + 15 = 90 cmHg.\n"
   "Đẳng nhiệt: p₁ℓ₁ = p₂ℓ₂ ⇒ 60 · 20 = 90 · ℓ₂ ⇒ ℓ₂ = 1200/90 ≈ 13,3 cm.",
   "Cột khí bị giam bởi thuỷ ngân", K),

sa("Một vòng dây kín điện trở 0,20 Ω đặt vuông góc với từ trường đều. Từ thông qua vòng dây giảm "
   "đều từ 0,080 Wb về 0 trong 0,40 s. Cường độ dòng điện cảm ứng bằng bao nhiêu ampe?",
   "1",
   "|e| = |ΔΦ|/Δt = 0,080/0,40 = 0,20 V.\n"
   "i = |e|/R = 0,20/0,20 = 1,0 A.",
   "Định luật Faraday", TB),

sa("Một máy biến áp lí tưởng có tỉ số vòng dây sơ cấp trên thứ cấp là 8 : 1. Cường độ dòng điện "
   "hiệu dụng ở cuộn thứ cấp là 6,0 A. Cường độ dòng điện ở cuộn sơ cấp bằng bao nhiêu ampe "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,75",
   "Máy lí tưởng: I₁/I₂ = N₂/N₁ = 1/8.\n"
   "I₁ = 6,0/8 = 0,75 A.",
   "Máy biến áp", TB),

sa("Một hạt nhân có 30 prôtôn và 35 nơtron. Năng lượng liên kết của hạt nhân là 565,5 MeV. "
   "Năng lượng liên kết riêng bằng bao nhiêu MeV trên nuclêôn (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "8,7",
   "Số khối: A = 30 + 35 = 65.\n"
   "ε = W(lk)/A = 565,5/65 = 8,7 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", TB),

sa("Cho phản ứng hạt nhân: ¹⁴₇N + ⁴₂He → ¹⁷₈O + X. Số khối của hạt X bằng bao nhiêu?",
   "1",
   "Bảo toàn số khối: 14 + 4 = 17 + A ⇒ A = 1.\n"
   "Bảo toàn điện tích: 7 + 2 = 8 + Z ⇒ Z = 1. Vậy X là prôtôn ¹₁H.",
   "Phản ứng hạt nhân", TB),
])


# =====================================================================  ĐỀ 07
DE7 = dict(
ma="TH-Đề 07", ten="ĐỀ THI THỬ SỐ 07", muc="Trung bình",
trongtam="Bài toán cân bằng nhiệt có chuyển thể, chu trình khí, cảm ứng điện từ và hạt nhân",
P1=[
mc("Thả 0,10 kg nước đá ở 0 °C vào 0,40 kg nước ở 40 °C trong bình cách nhiệt. "
   "Cho λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K). Nhiệt độ cân bằng xấp xỉ",
   ["0 °C.", "15,8 °C.", "25,0 °C.", "32,0 °C."],
   "B",
   "Bước 1 — kiểm tra đá có tan hết không.\n"
   "Nhiệt cần để tan hết đá: Q(cần) = 0,10 · 3,4·10⁵ = 34 000 J.\n"
   "Nhiệt nước nhả ra tối đa khi hạ về 0 °C: Q(có) = 0,40 · 4200 · 40 = 67 200 J.\n"
   "Vì Q(có) > Q(cần) nên đá tan hết và nhiệt độ cân bằng cao hơn 0 °C.\n"
   "Bước 2 — lập phương trình cân bằng nhiệt:\n"
   "0,40·4200·(40 − t) = 34 000 + 0,10·4200·t\n"
   "67 200 − 1680t = 34 000 + 420t ⇒ 2100t = 33 200 ⇒ t ≈ 15,8 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

mc("Trong quá trình đẳng tích, nhiệt lượng cung cấp cho khí",
   ["một phần biến thành công.", "hoàn toàn làm tăng nội năng của khí.",
    "hoàn toàn biến thành công.", "không làm thay đổi gì."],
   "B",
   "Đẳng tích nên A = 0, định luật I cho ΔU = Q: toàn bộ nhiệt lượng làm tăng nội năng.",
   "Định luật I nhiệt động lực học", TB),

mc("Một lượng khí lí tưởng thực hiện chu trình kín gồm hai quá trình đẳng tích và hai quá trình "
   "đẳng áp. Sau một chu trình, độ biến thiên nội năng của khí bằng",
   ["một giá trị dương.", "không.", "một giá trị âm.", "công của chu trình."],
   "B",
   "Nội năng là hàm trạng thái. Đi hết chu trình kín, khí trở về đúng trạng thái ban đầu nên "
   "ΔU = 0, kéo theo tổng nhiệt lượng nhận bằng tổng công sinh ra.",
   "Chu trình kín", K, fig="k_dt_chutrinh", cap="Chu trình kín trong hệ (p, V)"),

mc("Một khối khí lí tưởng ở 27 °C có áp suất 1,0·10⁵ Pa. Nén đẳng nhiệt để thể tích giảm còn "
   "40 % giá trị ban đầu. Áp suất lúc này bằng",
   ["0,40·10⁵ Pa.", "2,5·10⁵ Pa.", "1,4·10⁵ Pa.", "4,0·10⁵ Pa."],
   "B",
   "Đẳng nhiệt: p₁V₁ = p₂V₂ ⇒ p₂ = p₁·V₁/V₂ = 1,0·10⁵/0,40 = 2,5·10⁵ Pa.",
   "Định luật Boyle", TB),

mc("Khối lượng riêng của một chất khí lí tưởng được tính bằng",
   ["ρ = RT/(pM).", "ρ = pM/(RT).", "ρ = pR/(MT).", "ρ = MT/(pR)."],
   "B",
   "Từ pV = (m/M)RT suy ra m/V = pM/(RT), tức ρ = pM/(RT). "
   "Khí càng nén (p lớn) hoặc càng lạnh (T nhỏ) thì càng đặc.",
   "Phương trình Clapeyron", K),

mc("Ở cùng nhiệt độ và áp suất, khối lượng riêng của khí ôxi (M = 32 g/mol) so với khí hiđrô "
   "(M = 2 g/mol) thì",
   ["nhỏ hơn 16 lần.", "lớn hơn 16 lần.", "bằng nhau.", "lớn hơn 4 lần."],
   "B",
   "Từ ρ = pM/(RT), ở cùng p và T thì ρ tỉ lệ thuận với khối lượng mol.\n"
   "ρ(O₂)/ρ(H₂) = 32/2 = 16 lần.",
   "Khối lượng riêng của khí", K),

mc("Một khung dây hình vuông cạnh 25 cm chuyển động đều với tốc độ 4,0 m/s đi vào vùng từ trường "
   "đều B = 0,40 T. Suất điện động cảm ứng trong khung khi đang đi vào bằng",
   ["0,20 V.", "0,40 V.", "0,80 V.", "0,10 V."],
   "B",
   "Chỉ cạnh nằm trong từ trường đóng vai trò nguồn: e = B·a·v = 0,40 · 0,25 · 4,0 = 0,40 V.",
   "Khung dây vào vùng từ trường", TB, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

mc("Một nam châm rơi thẳng đứng qua một vòng dây kim loại kín đặt nằm ngang. So với rơi tự do, "
   "thời gian rơi của nam châm",
   ["ngắn hơn.", "dài hơn.", "không đổi.", "bằng một nửa."],
   "B",
   "Theo định luật Lenz, dòng cảm ứng luôn tạo lực cản trở chuyển động của nam châm — cả lúc lại "
   "gần lẫn lúc ra xa. Vì thế nam châm rơi chậm hơn, thời gian rơi dài hơn.",
   "Định luật Lenz", TB, fig="t_sd_nam_cham_roi", cap="Nam châm rơi qua vòng dây"),

mc("Đặt điện áp u = 220√2·cos(100πt) (V) vào hai đầu điện trở 44 Ω. "
   "Cường độ dòng điện hiệu dụng qua điện trở bằng",
   ["2,5 A.", "5,0 A.", "7,07 A.", "10,0 A."],
   "B",
   "Biểu thức có U₀ = 220√2 nên U = 220 V.\n"
   "I = U/R = 220/44 = 5,0 A.",
   "Mạch điện xoay chiều thuần trở", TB),

mc("Một trạm phát truyền công suất 500 kW ở điện áp 25 kV trên đường dây có điện trở 8,0 Ω. "
   "Công suất hao phí bằng",
   ["1,6 kW.", "3,2 kW.", "6,4 kW.", "0,8 kW."],
   "B",
   "I = P/U = 500 000/25 000 = 20 A.\n"
   "ΔP = R·I² = 8,0 · 400 = 3200 W = 3,2 kW.",
   "Hao phí truyền tải", TB, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây phẳng 150 vòng quay đều trong từ trường đều B = 0,40 T quanh trục vuông góc "
   "với B, diện tích mỗi vòng 20 cm², tần số 50 Hz. Suất điện động cực đại xấp xỉ",
   ["18,8 V.", "37,7 V.", "9,4 V.", "75,4 V."],
   "B",
   "ω = 2π·50 ≈ 314,16 rad/s;  S = 2,0·10⁻³ m².\n"
   "E₀ = ω·N·B·S = 314,16 · 150 · 0,40 · 2,0·10⁻³ = 314,16 · 0,12 ≈ 37,7 V.",
   "Máy phát điện xoay chiều", TB),

mc("Hạt nhân nào sau đây có năng lượng liên kết riêng lớn nhất?",
   ["²₁H.", "⁵⁶₂₆Fe.", "²³⁸₉₂U.", "⁴₂He."],
   "B",
   "Đỉnh của đường cong năng lượng liên kết riêng nằm quanh A ≈ 56, ứng với sắt ⁵⁶₂₆Fe "
   "(ε ≈ 8,8 MeV/nuclêôn). Đơteri chỉ khoảng 1,1 và urani khoảng 7,6 MeV/nuclêôn.",
   "Độ bền vững của hạt nhân", TB, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một chất phóng xạ có chu kì bán rã 20 ngày. Sau 60 ngày, tỉ số giữa số hạt nhân đã phân rã "
   "và số hạt nhân còn lại bằng",
   ["3.", "7.", "8.", "15."],
   "B",
   "n = 60/20 = 3 chu kì ⇒ còn N₀/8, đã rã 7N₀/8.\n"
   "Tỉ số = 7. Công thức chung: 2ⁿ − 1.",
   "Tỉ số hạt nhân con và mẹ", TB),

mc("Trong phản ứng hạt nhân toả năng lượng, tổng độ hụt khối của các hạt sau phản ứng",
   ["nhỏ hơn trước.", "lớn hơn trước.", "bằng trước.", "bằng không."],
   "B",
   "Độ hụt khối lớn hơn nghĩa là năng lượng liên kết lớn hơn, các hạt nhân sau bền vững hơn "
   "nên phản ứng toả năng lượng: ΔE = (Δm sau − Δm trước)·c² > 0.",
   "Năng lượng phản ứng hạt nhân", K),

mc("Tia phóng xạ nào bị lệch NHIỀU NHẤT khi đi qua điện trường đều?",
   ["Tia α.", "Tia β⁻.", "Tia γ.", "Cả ba tia lệch như nhau."],
   "B",
   "Tia γ không mang điện nên không lệch. Giữa α và β⁻: tuy α mang điện tích lớn gấp đôi nhưng "
   "khối lượng lớn hơn electron khoảng 7000 lần nên gia tốc nhỏ hơn nhiều, lệch ít hơn hẳn.",
   "Ba loại tia phóng xạ", TB, fig="h_sd_tia_phongxa", cap="Ba tia trong điện trường"),

mc("Chất thải từ nhà máy điện hạt nhân chủ yếu phát ra tia",
   ["α.", "β và γ.", "chỉ γ.", "không phát tia nào."],
   "B",
   "Các mảnh vỡ phân hạch thừa nơtron nên phóng xạ β⁻, thường kèm theo bức xạ γ khi hạt nhân con "
   "chuyển từ trạng thái kích thích về trạng thái cơ bản.",
   "Chất thải phóng xạ", TB),

mc("Một lượng khí lí tưởng bị nén nhanh trong một bơm xe đã bịt kín đầu ra. Thân bơm nóng lên vì",
   ["ma sát giữa pit-tông và thành bơm là nguyên nhân duy nhất.",
    "công nén chuyển thành nội năng của khí, rồi khí truyền nhiệt cho thân bơm.",
    "khí truyền nhiệt từ môi trường vào.",
    "áp suất khí giảm."],
   "B",
   "Nén nhanh nên gần như đoạn nhiệt: ΔU = A > 0, nội năng và nhiệt độ khí tăng. Khí nóng rồi "
   "truyền nhiệt cho thành bơm. Ma sát có góp phần nhưng không phải nguyên nhân chính.",
   "Định luật I nhiệt động lực học – thực tiễn", TB, fig="k_sd_bomxe", cap="Bơm xe đạp"),

mc("Người ta đo bề dày tấm nhôm mỏng đang cán bằng nguồn phát tia β vì",
   ["tia β không bị hấp thụ.", "cường độ tia β xuyên qua rất nhạy với bề dày tấm.",
    "tia β mang điện dương.", "tia β có chu kì bán rã ngắn."],
   "B",
   "Tia α bị chặn hoàn toàn nên không xuyên qua được; tia γ xuyên qua gần như trọn vẹn nên không "
   "nhạy. Chỉ tia β bị hấp thụ một phần nên cường độ xuyên qua thay đổi rõ theo bề dày.",
   "Ứng dụng trong công nghiệp", TB, fig="h_sd_ung_dung", cap="Ứng dụng của đồng vị phóng xạ"),
],
P2=[
ds("Thả 0,15 kg nước đá ở 0 °C vào 0,60 kg nước ở 35 °C trong bình cách nhiệt. "
   "Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng cần để làm tan hết nước đá là 51 kJ.", True,
     "Đúng. Q = 0,15 · 3,4·10⁵ = 51 000 J = 51 kJ."),
    ("Nhiệt lượng tối đa nước nhả ra khi hạ về 0 °C là 88,2 kJ.", True,
     "Đúng. Q = 0,60 · 4200 · 35 = 88 200 J = 88,2 kJ."),
    ("Nước đá tan hết hoàn toàn.", True,
     "Đúng. 88,2 kJ > 51 kJ nên nhiệt nước nhả ra đủ làm tan hết đá và còn dư."),
    ("Nhiệt độ cân bằng của hỗn hợp bằng 0 °C.", False,
     "Sai. Vì còn nhiệt dư nên nhiệt độ cân bằng cao hơn 0 °C. "
     "Giải: 0,60·4200·(35 − t) = 51 000 + 0,15·4200·t ⇒ 88 200 − 2520t = 51 000 + 630t "
     "⇒ 3150t = 37 200 ⇒ t ≈ 11,8 °C.")],
   "Cân bằng nhiệt có chuyển thể", K),

ds("Một lượng khí lí tưởng khối lượng 8,0 g khí ôxi (M = 32 g/mol) chứa trong bình 8,31 L "
   "ở 27 °C. Cho R = 8,31 J/(mol·K).",
   [("Số mol khí trong bình là 0,25 mol.", True,
     "Đúng. n = m/M = 8,0/32 = 0,25 mol."),
    ("Áp suất khí trong bình xấp xỉ 0,75·10⁵ Pa.", True,
     "Đúng. p = nRT/V = 0,25 · 8,31 · 300/(8,31·10⁻³) = 623,25/8,31·10⁻³ ≈ 7,5·10⁴ Pa."),
    ("Khối lượng riêng của khí trong bình xấp xỉ 0,96 kg/m³.", True,
     "Đúng. ρ = m/V = 8,0·10⁻³/(8,31·10⁻³) ≈ 0,96 kg/m³."),
    ("Nếu thay khí ôxi bằng cùng khối lượng khí hiđrô thì áp suất trong bình không đổi.", False,
     "Sai. Cùng khối lượng nhưng M nhỏ hơn 16 lần nên số mol lớn hơn 16 lần, áp suất cũng lớn "
     "hơn 16 lần.")],
   "Phương trình Clapeyron", K),

ds("Một khung dây hình vuông cạnh 25 cm, điện trở 0,50 Ω, chuyển động đều với tốc độ 4,0 m/s "
   "đi vào rồi đi ra khỏi vùng từ trường đều B = 0,40 T rộng 60 cm.",
   [("Suất điện động cảm ứng lúc khung đi vào bằng 0,40 V.", True,
     "Đúng. e = B·a·v = 0,40 · 0,25 · 4,0 = 0,40 V."),
    ("Cường độ dòng cảm ứng lúc đó bằng 0,80 A.", True,
     "Đúng. i = 0,40/0,50 = 0,80 A."),
    ("Thời gian khung nằm trọn trong vùng từ trường là 0,0875 s.", True,
     "Đúng. Quãng đường tương ứng là 60 − 25 = 35 cm ⇒ t = 0,35/4,0 = 0,0875 s."),
    ("Trong thời gian khung nằm trọn trong vùng, dòng cảm ứng vẫn bằng 0,80 A.", False,
     "Sai. Lúc đó từ thông không đổi nên không có dòng cảm ứng.")],
   "Khung dây ra vào vùng từ trường", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

ds("Hạt nhân ⁵⁶₂₆Fe có năng lượng liên kết riêng 8,8 MeV/nuclêôn; hạt nhân ²³⁵₉₂U có năng lượng "
   "liên kết riêng 7,6 MeV/nuclêôn.",
   [("Năng lượng liên kết của hạt nhân sắt là 492,8 MeV.", True,
     "Đúng. W = 8,8 · 56 = 492,8 MeV."),
    ("Năng lượng liên kết của hạt nhân urani là 1786 MeV.", True,
     "Đúng. W = 7,6 · 235 = 1786 MeV."),
    ("Hạt nhân urani bền vững hơn hạt nhân sắt vì năng lượng liên kết lớn hơn.", False,
     "Sai. Độ bền vững đo bằng năng lượng liên kết RIÊNG: sắt có 8,8 lớn hơn urani 7,6 "
     "MeV/nuclêôn nên sắt bền hơn."),
    ("Khi urani phân hạch thành các mảnh có ε lớn hơn, phản ứng toả năng lượng.", True,
     "Đúng. Các hạt nhân sau bền vững hơn nên phần năng lượng liên kết chênh lệch được giải phóng.")],
   "So sánh độ bền vững", TB, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),
],
P3=[
sa("Thả 0,20 kg nước đá ở 0 °C vào 0,80 kg nước ở 50 °C trong bình cách nhiệt. "
   "Nhiệt độ cân bằng bằng bao nhiêu độ Celsius (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K).",
   "23,8",
   "Nhiệt để tan hết đá: 0,20 · 3,4·10⁵ = 68 000 J.\n"
   "Nhiệt nước nhả tối đa: 0,80 · 4200 · 50 = 168 000 J > 68 000 J nên đá tan hết.\n"
   "0,80·4200·(50 − t) = 68 000 + 0,20·4200·t\n"
   "168 000 − 3360t = 68 000 + 840t ⇒ 4200t = 100 000 ⇒ t ≈ 23,8 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

sa("Một bình 4,155 L chứa 4,0 g khí hêli (M = 4 g/mol) ở 27 °C. Áp suất khí trong bình bằng "
   "bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x)? Cho R = 8,31 J/(mol·K).",
   "6",
   "Số mol: n = 4,0/4 = 1,0 mol.\n"
   "V = 4,155·10⁻³ m³;  T = 300 K.\n"
   "p = nRT/V = 1,0 · 8,31 · 300/(4,155·10⁻³) = 2493/4,155·10⁻³ = 6,0·10⁵ Pa.",
   "Phương trình Clapeyron", K),

sa("Một thanh dẫn dài 60 cm trượt đều với tốc độ 2,5 m/s trên hai ray nằm ngang vuông góc với từ "
   "trường đều thẳng đứng B = 0,40 T. Suất điện động cảm ứng bằng bao nhiêu vôn?",
   "0,6",
   "e = B·ℓ·v = 0,40 · 0,60 · 2,5 = 0,60 V.",
   "Thanh dẫn chuyển động", TB),

sa("Truyền công suất 800 kW ở điện áp 40 kV trên đường dây có điện trở 6,0 Ω. "
   "Hiệu suất truyền tải bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ nhất)?",
   "99,7",
   "I = P/U = 800 000/40 000 = 20 A.\n"
   "ΔP = R·I² = 6,0 · 400 = 2400 W = 2,4 kW.\n"
   "H = (800 − 2,4)/800 = 797,6/800 = 0,997 = 99,7 %.",
   "Hiệu suất truyền tải", TB),

sa("Một hạt nhân có độ hụt khối 0,25 u. Năng lượng liên kết của hạt nhân đó bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)? Cho 1 u·c² = 931,5 MeV.",
   "232,88",
   "W(lk) = 0,25 · 931,5 = 232,875 ≈ 232,88 MeV.",
   "Năng lượng liên kết", TB),

sa("Một mẫu chất phóng xạ nguyên chất sau 5 chu kì bán rã thì tỉ số giữa số hạt nhân con tạo thành "
   "và số hạt nhân mẹ còn lại bằng bao nhiêu?",
   "31",
   "Sau 5 chu kì, mẹ còn N₀/32; con tạo thành N₀ − N₀/32 = 31N₀/32.\n"
   "Tỉ số = 31, đúng theo công thức 2ⁿ − 1 với n = 5.",
   "Tỉ số hạt nhân con và mẹ", TB),
])


# =====================================================================  ĐỀ 08
DE8 = dict(
ma="TH-Đề 08", ten="ĐỀ THI THỬ SỐ 08", muc="Trung bình",
trongtam="Bài toán pit-tông, điện lượng cảm ứng, độ phóng xạ và năng lượng hạt nhân",
P1=[
mc("Một xi lanh nằm ngang có pit-tông nhẹ, tự do, ngăn khí bên trong với khí quyển. "
   "Khi đun nóng khí trong xi lanh, quá trình biến đổi là",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "đoạn nhiệt."],
   "B",
   "Pit-tông nhẹ và tự do nên áp suất khí luôn bằng áp suất khí quyển, không đổi. "
   "Vậy đây là quá trình đẳng áp.",
   "Nhận dạng quá trình", TB),

mc("Một khối khí trong xi lanh nằm ngang có pit-tông tự do được đun nóng từ 27 °C lên 87 °C. "
   "Nếu thể tích ban đầu là 2,0 L thì thể tích lúc sau bằng",
   ["2,2 L.", "2,4 L.", "6,4 L.", "1,7 L."],
   "B",
   "Đẳng áp: T₁ = 300 K, T₂ = 360 K.\n"
   "V₂ = V₁·T₂/T₁ = 2,0 · 360/300 = 2,4 L.",
   "Định luật Charles", TB),

mc("Nội năng của một khối khí lí tưởng chỉ phụ thuộc vào",
   ["áp suất.", "nhiệt độ.", "thể tích.", "khối lượng riêng."],
   "B",
   "Với khí lí tưởng, lực tương tác giữa các phân tử được bỏ qua nên không có thế năng tương tác; "
   "nội năng chỉ còn là tổng động năng chuyển động nhiệt, tức chỉ phụ thuộc nhiệt độ.",
   "Nội năng của khí lí tưởng", TB),

mc("Cần bao nhiêu nhiệt lượng để làm hoá hơi hoàn toàn 0,20 kg nước đang ở 100 °C? "
   "Cho L = 2,26·10⁶ J/kg.",
   ["226 kJ.", "452 kJ.", "113 kJ.", "84 kJ."],
   "B",
   "Q = m·L = 0,20 · 2,26·10⁶ = 4,52·10⁵ J = 452 kJ.\n"
   "Nhiệt hoá hơi riêng rất lớn — đó là lí do làm bay hơi mồ hôi giúp cơ thể toả nhiệt hiệu quả.",
   "Nhiệt hoá hơi riêng", TB),

mc("Một vòng dây kín điện trở 0,50 Ω. Từ thông qua vòng dây giảm đều 0,20 Wb. "
   "Điện lượng chuyển qua tiết diện vòng dây bằng",
   ["0,10 C.", "0,40 C.", "0,80 C.", "0,20 C."],
   "B",
   "q = |ΔΦ|/R = 0,20/0,50 = 0,40 C.\n"
   "Điện lượng chỉ phụ thuộc độ biến thiên từ thông và điện trở, không phụ thuộc thời gian "
   "biến thiên.",
   "Điện lượng cảm ứng", K),

mc("Trong bài toán trên, nếu thời gian biến thiên từ thông giảm đi một nửa thì điện lượng chuyển "
   "qua tiết diện dây",
   ["tăng gấp đôi.", "không đổi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "q = |ΔΦ|/R hoàn toàn không chứa thời gian. Chỉ có suất điện động và cường độ dòng điện tăng "
   "gấp đôi, còn điện lượng giữ nguyên.",
   "Điện lượng cảm ứng", K),

mc("Một cuộn dây 250 vòng, điện trở 2,0 Ω, có từ thông qua mỗi vòng giảm đều 8,0·10⁻³ Wb. "
   "Điện lượng chuyển qua tiết diện dây bằng",
   ["0,50 C.", "1,00 C.", "2,00 C.", "0,25 C."],
   "B",
   "q = N·|ΔΦ|/R = 250 · 8,0·10⁻³/2,0 = 2,0/2,0 = 1,00 C.",
   "Điện lượng cảm ứng", K),

mc("Một đoạn dây dẫn dài 10 cm, khối lượng 20 g được treo nằm ngang bằng hai sợi dây mảnh trong "
   "từ trường đều nằm ngang vuông góc với đoạn dây, B = 0,50 T. Để lực căng hai sợi dây bằng 0, "
   "cường độ dòng điện qua dây phải bằng (g = 10 m/s²)",
   ["2,0 A.", "4,0 A.", "8,0 A.", "1,0 A."],
   "B",
   "Lực từ phải hướng lên và cân bằng trọng lực: B·I·ℓ = m·g.\n"
   "0,50 · I · 0,10 = 0,020 · 10 = 0,20 N ⇒ 0,050·I = 0,20 ⇒ I = 4,0 A.",
   "Cân bằng lực từ – trọng lực", K),

mc("Một máy biến áp lí tưởng cung cấp công suất 880 W ở điện áp thứ cấp 110 V. "
   "Điện áp sơ cấp là 220 V. Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng",
   ["8,0 A.", "4,0 A.", "2,0 A.", "16,0 A."],
   "B",
   "Máy lí tưởng nên P₁ = P₂ = 880 W.\n"
   "I₁ = P₁/U₁ = 880/220 = 4,0 A.",
   "Máy biến áp – công suất", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một dòng điện xoay chiều cường độ hiệu dụng 3,0 A chạy qua điện trở 20 Ω trong 10 phút. "
   "Nhiệt lượng toả ra bằng",
   ["54 kJ.", "108 kJ.", "216 kJ.", "27 kJ."],
   "B",
   "t = 10 phút = 600 s.\n"
   "Q = R·I²·t = 20 · 9,0 · 600 = 108 000 J = 108 kJ.",
   "Tác dụng nhiệt của dòng xoay chiều", TB),

mc("Hạt nhân ²³⁸₉₂U có năng lượng liên kết 1801 MeV. Năng lượng liên kết riêng của nó xấp xỉ",
   ["6,6 MeV/nuclêôn.", "7,6 MeV/nuclêôn.",
    "8,8 MeV/nuclêôn.", "19,6 MeV/nuclêôn."],
   "B",
   "ε = W(lk)/A = 1801/238 ≈ 7,57 ≈ 7,6 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", TB, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chất phóng xạ có 2,0·10²⁰ hạt nhân và hằng số phóng xạ 5,0·10⁻⁶ s⁻¹. "
   "Độ phóng xạ của mẫu bằng",
   ["1,0·10¹³ Bq.", "1,0·10¹⁵ Bq.", "4,0·10²⁵ Bq.", "1,0·10¹⁴ Bq."],
   "B",
   "H = λ·N = 5,0·10⁻⁶ · 2,0·10²⁰ = 1,0·10¹⁵ Bq.",
   "Độ phóng xạ", TB),

mc("Chu kì bán rã của chất phóng xạ trong câu trên xấp xỉ (ln2 ≈ 0,693)",
   ["6,93·10⁴ s.", "1,39·10⁵ s.", "3,47·10⁵ s.", "2,00·10⁵ s."],
   "B",
   "T = ln2/λ = 0,693/(5,0·10⁻⁶) = 1,386·10⁵ ≈ 1,39·10⁵ s (khoảng 1,6 ngày).",
   "Hằng số phóng xạ", TB),

mc("Cho phản ứng ²₁H + ²₁H → ³₂He + ¹₀n. Biết năng lượng liên kết riêng của ²H là "
   "1,11 MeV/nuclêôn và của ³He là 2,57 MeV/nuclêôn. Năng lượng toả ra xấp xỉ",
   ["1,64 MeV.", "3,27 MeV.", "6,54 MeV.", "12,15 MeV."],
   "B",
   "Năng lượng liên kết trước: 2 hạt ²H, mỗi hạt 2·1,11 = 2,22 MeV ⇒ tổng 4,44 MeV.\n"
   "Năng lượng liên kết sau: 3 · 2,57 = 7,71 MeV (nơtron tự do có W(lk) = 0).\n"
   "ΔE = 7,71 − 4,44 = 3,27 MeV.",
   "Năng lượng phản ứng theo W(lk)", K),

mc("Trong lò phản ứng hạt nhân, chất tải nhiệt có nhiệm vụ",
   ["hấp thụ nơtron.", "mang nhiệt từ vùng hoạt động tới lò sinh hơi.",
    "làm chậm nơtron.", "che chắn bức xạ."],
   "B",
   "Chất tải nhiệt (thường là nước áp lực cao hoặc kim loại lỏng) nhận nhiệt từ vùng hoạt động rồi "
   "truyền sang lò sinh hơi. Việc hấp thụ nơtron do thanh điều khiển đảm nhiệm.",
   "Lò phản ứng hạt nhân", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Một nguồn phóng xạ có độ phóng xạ 4,0·10¹² Bq, mỗi phân rã toả 1,5 MeV. "
   "Công suất của nguồn bằng (1 MeV = 1,6·10⁻¹³ J)",
   ["0,48 W.", "0,96 W.", "1,92 W.", "0,24 W."],
   "B",
   "P = H · E = 4,0·10¹² · 1,5 · 1,6·10⁻¹³ = 4,0·10¹² · 2,4·10⁻¹³ = 0,96 W.",
   "Công suất của nguồn phóng xạ", K),

mc("Trong ba loại tia phóng xạ, tia có khả năng ION HOÁ môi trường mạnh nhất là",
   ["tia γ.", "tia α.", "tia β⁻.", "tia β⁺."],
   "B",
   "Tia α mang điện tích lớn và khối lượng lớn nên ion hoá rất mạnh, vì thế mất năng lượng nhanh "
   "và chỉ đi được vài centimét trong không khí. Khả năng đâm xuyên thì ngược lại: α < β < γ.",
   "Ba loại tia phóng xạ", TB, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),

mc("Khi nước sôi, nhiệt độ không tăng dù vẫn đun liên tục vì nhiệt lượng cung cấp được dùng để",
   ["làm tăng động năng phân tử nước.", "tách các phân tử nước khỏi khối chất lỏng.",
    "làm nóng nồi.", "làm tăng áp suất hơi."],
   "B",
   "Trong khi sôi, nhiệt lượng chuyển thành thế năng để tách phân tử khỏi khối chất lỏng "
   "(quá trình hoá hơi), không làm tăng động năng trung bình nên nhiệt độ không đổi.",
   "Nhiệt hoá hơi riêng", TB, fig="n_sd_bayhoi_soi", cap="So sánh bay hơi và sôi"),
],
P2=[
ds("Một xi lanh thẳng đứng tiết diện 20 cm² chứa khí, phía trên là pit-tông khối lượng 4,0 kg "
   "trượt không ma sát. Áp suất khí quyển là 1,0·10⁵ Pa. Lấy g = 10 m/s².",
   [("Áp suất khí trong xi lanh bằng tổng áp suất khí quyển và áp suất do trọng lượng pit-tông.", True,
     "Đúng. Điều kiện cân bằng của pit-tông cho p = p₀ + mg/S."),
    ("Áp suất do trọng lượng pit-tông gây ra là 2,0·10⁴ Pa.", True,
     "Đúng. mg/S = 4,0 · 10/(20·10⁻⁴) = 40/0,0020 = 2,0·10⁴ Pa."),
    ("Áp suất khí trong xi lanh là 1,2·10⁵ Pa.", True,
     "Đúng. p = 1,0·10⁵ + 0,2·10⁵ = 1,2·10⁵ Pa."),
    ("Khi đun nóng khí, áp suất trong xi lanh tăng lên.", False,
     "Sai. Pit-tông tự do nên áp suất vẫn giữ nguyên 1,2·10⁵ Pa; chỉ có thể tích tăng. "
     "Đây là quá trình đẳng áp.")],
   "Bài toán pit-tông", K, fig="k_sd_xilanh_quanang", cap="Xi lanh có quả nặng trên pit-tông"),

ds("Một cuộn dây 400 vòng, điện trở 5,0 Ω, diện tích mỗi vòng 25 cm², đặt vuông góc với từ trường "
   "đều. Cảm ứng từ giảm đều từ 0,60 T về 0 trong 0,20 s.",
   [("Độ biến thiên từ thông qua mỗi vòng là 1,5·10⁻³ Wb.", True,
     "Đúng. |ΔΦ| = ΔB·S = 0,60 · 2,5·10⁻³ = 1,5·10⁻³ Wb."),
    ("Suất điện động cảm ứng trong cuộn dây bằng 3,0 V.", True,
     "Đúng. |e| = N·|ΔΦ|/Δt = 400 · 1,5·10⁻³/0,20 = 400 · 7,5·10⁻³ = 3,0 V."),
    ("Cường độ dòng điện cảm ứng bằng 0,60 A.", True,
     "Đúng. i = 3,0/5,0 = 0,60 A."),
    ("Điện lượng chuyển qua tiết diện dây bằng 0,60 C.", False,
     "Sai. q = N·|ΔΦ|/R = 400 · 1,5·10⁻³/5,0 = 0,60/5,0 = 0,12 C. "
     "Giá trị 0,60 C là kết quả khi nhầm q với cường độ dòng điện.")],
   "Điện lượng cảm ứng", K),

ds("Một mẫu chất phóng xạ có 5,0·10²⁰ hạt nhân và chu kì bán rã 2,0 giờ. "
   "Cho ln2 ≈ 0,693; 1 giờ = 3600 s.",
   [("Hằng số phóng xạ xấp xỉ 9,63·10⁻⁵ s⁻¹.", True,
     "Đúng. T = 2,0 · 3600 = 7200 s ⇒ λ = 0,693/7200 ≈ 9,63·10⁻⁵ s⁻¹."),
    ("Độ phóng xạ ban đầu của mẫu xấp xỉ 4,81·10¹⁶ Bq.", True,
     "Đúng. H₀ = λ·N₀ = 9,63·10⁻⁵ · 5,0·10²⁰ ≈ 4,81·10¹⁶ Bq."),
    ("Sau 6,0 giờ, số hạt nhân còn lại là 6,25·10¹⁹ hạt.", True,
     "Đúng. n = 3 ⇒ N = 5,0·10²⁰/8 = 6,25·10¹⁹ hạt."),
    ("Sau 6,0 giờ, độ phóng xạ của mẫu vẫn giữ nguyên giá trị ban đầu.", False,
     "Sai. H = λN tỉ lệ với số hạt nhân nên cũng giảm 8 lần, còn khoảng 6,01·10¹⁵ Bq.")],
   "Độ phóng xạ", K),

ds("Cho phản ứng nhiệt hạch ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   [("Phản ứng bảo toàn số khối và điện tích.", True,
     "Đúng. Số khối: 2 + 3 = 4 + 1;  điện tích: 1 + 1 = 2 + 0."),
    ("Mỗi phản ứng toả khoảng 2,82·10⁻¹² J.", True,
     "Đúng. 17,6 · 1,6·10⁻¹³ = 2,816·10⁻¹² J."),
    ("Tổng hợp được 1,0 gam heli sẽ toả khoảng 4,24·10¹¹ J.", True,
     "Đúng. N = (1,0/4)·6,02·10²³ = 1,505·10²³ hạt ⇒ E = 1,505·10²³ · 2,816·10⁻¹² ≈ 4,24·10¹¹ J."),
    ("Năng lượng đó nhỏ hơn năng lượng toả ra khi phân hạch hoàn toàn 1,0 gam ²³⁵U.", False,
     "Sai. Phân hạch 1,0 g ²³⁵U chỉ toả khoảng 8,2·10¹⁰ J, nhỏ hơn 4,24·10¹¹ J khoảng 5 lần. "
     "Tính trên cùng khối lượng, nhiệt hạch hiệu quả hơn hẳn.")],
   "Năng lượng nhiệt hạch", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),
],
P3=[
sa("Tính nhiệt lượng cần cung cấp để đưa 0,40 kg nước đá từ −10 °C lên 0 °C rồi làm tan hết. "
   "Kết quả tính bằng kilôjun. Cho c(nước đá) = 2100 J/(kg·K); λ = 3,4·10⁵ J/kg.",
   "144,4",
   "Giai đoạn 1 — làm ấm nước đá: Q₁ = 0,40 · 2100 · 10 = 8400 J.\n"
   "Giai đoạn 2 — làm tan hết đá: Q₂ = 0,40 · 3,4·10⁵ = 136 000 J.\n"
   "Tổng: Q = 8400 + 136 000 = 144 400 J = 144,4 kJ.",
   "Bài toán nhiều giai đoạn", TB),

sa("Một xi lanh thẳng đứng tiết diện 25 cm² chứa khí, pit-tông khối lượng 5,0 kg trượt không ma sát. "
   "Áp suất khí quyển 1,0·10⁵ Pa, g = 10 m/s². Áp suất khí trong xi lanh bằng bao nhiêu "
   "(viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x)?",
   "1,2",
   "Áp suất do pit-tông: mg/S = 5,0 · 10/(25·10⁻⁴) = 50/0,0025 = 2,0·10⁴ Pa.\n"
   "p = p₀ + mg/S = 1,0·10⁵ + 0,2·10⁵ = 1,2·10⁵ Pa.",
   "Bài toán pit-tông", K),

sa("Một cuộn dây 300 vòng, điện trở 4,0 Ω. Từ thông qua mỗi vòng giảm đều 6,0·10⁻³ Wb. "
   "Điện lượng chuyển qua tiết diện dây bằng bao nhiêu culông (làm tròn đến chữ số thập phân "
   "thứ hai)?",
   "0,45",
   "q = N·|ΔΦ|/R = 300 · 6,0·10⁻³/4,0 = 1,8/4,0 = 0,45 C.",
   "Điện lượng cảm ứng", K),

sa("Một đoạn dây dẫn dài 20 cm, khối lượng 50 g được treo nằm ngang bằng hai sợi dây mảnh trong "
   "từ trường đều nằm ngang vuông góc với đoạn dây, B = 0,25 T. Cường độ dòng điện để lực căng "
   "hai sợi dây bằng 0 là bao nhiêu ampe? Lấy g = 10 m/s².",
   "10",
   "Điều kiện: B·I·ℓ = m·g ⇒ 0,25 · I · 0,20 = 0,050 · 10 = 0,50 N.\n"
   "0,050·I = 0,50 ⇒ I = 10 A.",
   "Cân bằng lực từ – trọng lực", K),

sa("Một nguồn phóng xạ có độ phóng xạ 6,0·10¹² Bq, mỗi phân rã toả 2,5 MeV. "
   "Công suất của nguồn bằng bao nhiêu oát (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho 1 MeV = 1,6·10⁻¹³ J.",
   "2,4",
   "Năng lượng mỗi phân rã: 2,5 · 1,6·10⁻¹³ = 4,0·10⁻¹³ J.\n"
   "P = H · E = 6,0·10¹² · 4,0·10⁻¹³ = 2,4 W.",
   "Công suất của nguồn phóng xạ", K),

sa("Một mẫu chất phóng xạ có hằng số phóng xạ 2,5·10⁻⁵ s⁻¹. Chu kì bán rã của chất đó bằng "
   "bao nhiêu giây (viết dưới dạng x·10⁴, chỉ ghi giá trị x, làm tròn đến chữ số thập phân "
   "thứ hai)? Lấy ln2 ≈ 0,693.",
   "2,77",
   "T = ln2/λ = 0,693/(2,5·10⁻⁵) = 2,772·10⁴ ≈ 2,77·10⁴ s.",
   "Hằng số phóng xạ", TB),
])


# =====================================================================  ĐỀ 09
DE9 = dict(
ma="TH-Đề 09", ten="ĐỀ THI THỬ SỐ 09", muc="Trung bình",
trongtam="Đồ thị và bảng số liệu, bài toán thực tiễn về năng lượng và bức xạ",
P1=[
mc("Một chất lỏng được đun bằng bếp có công suất không đổi. Trong 4 phút đầu nhiệt độ tăng 20 °C, "
   "trong 4 phút tiếp theo nhiệt độ tăng 20 °C nữa rồi giữ nguyên. Giai đoạn giữ nguyên ứng với",
   ["bếp bị tắt.", "chất lỏng bắt đầu sôi.",
    "chất lỏng đóng băng.", "nhiệt kế hỏng."],
   "B",
   "Nhiệt độ ngừng tăng dù vẫn được cấp nhiệt đều là dấu hiệu của quá trình chuyển thể. "
   "Với chất lỏng đang được đun nóng, đó là lúc nó bắt đầu sôi.",
   "Đọc đồ thị chuyển thể", TB),

mc("Bảng sau ghi nhiệt dung riêng của bốn chất. Chất nào nóng lên nhanh nhất khi nhận cùng một "
   "nhiệt lượng với cùng khối lượng?",
   ["Nước, c = 4200 J/(kg·K).", "Chì, c = 130 J/(kg·K).",
    "Nhôm, c = 880 J/(kg·K).", "Sắt, c = 460 J/(kg·K)."],
   "B",
   "ΔT = Q/(mc) tỉ lệ nghịch với nhiệt dung riêng. Chì có c = 130 J/(kg·K) nhỏ nhất nên nóng lên "
   "nhanh nhất, gấp khoảng 32 lần so với nước.",
   "Nhiệt dung riêng", TB,
   tbl=("Nhiệt dung riêng của một số chất", ["Chất", "c (J/kg·K)"],
        [["Nước", "4200"], ["Nhôm", "880"], ["Sắt", "460"], ["Chì", "130"]])),

mc("Một khối khí giãn nở đẳng nhiệt và sinh công 600 J. Nhiệt lượng khí trao đổi với môi trường là",
   ["thu 600 J.", "thu 300 J.", "toả 600 J.", "không trao đổi nhiệt."],
   "A",
   "Đẳng nhiệt với khí lí tưởng nên ΔU = 0. Từ ΔU = A + Q và A = −600 J (khí sinh công) "
   "suy ra Q = +600 J: khí THU nhiệt 600 J.",
   "Quá trình đẳng nhiệt", TB),

mc("Khi nén khí trong xi lanh rất nhanh, quá trình gần đúng là",
   ["đẳng nhiệt.", "đoạn nhiệt.", "đẳng áp.", "đẳng tích."],
   "B",
   "Nén nhanh nên khí chưa kịp trao đổi nhiệt với môi trường: Q ≈ 0, quá trình gần đúng là "
   "đoạn nhiệt. Muốn quá trình đẳng nhiệt thì phải nén thật chậm.",
   "Nhận dạng quá trình", TB),

mc("Một lượng khí lí tưởng ở 27 °C được nén đẳng nhiệt từ 6,0 L xuống 2,0 L. Áp suất khí",
   ["giảm 3 lần.", "tăng 3 lần.", "không đổi.", "tăng 9 lần."],
   "B",
   "Đẳng nhiệt: pV không đổi. V giảm 3 lần thì p tăng 3 lần.",
   "Định luật Boyle", TB),

mc("Một bình kín chứa khí ở 27 °C. Muốn áp suất khí tăng gấp đôi thì phải nung nóng khí tới",
   ["54 °C.", "327 °C.", "300 °C.", "600 °C."],
   "B",
   "Đẳng tích: p tỉ lệ thuận với T (kelvin).\n"
   "T₂ = 2·T₁ = 2 · 300 = 600 K ⇒ t₂ = 600 − 273 = 327 °C.\n"
   "Đáp án 54 °C là bẫy khi nhân đôi nhiệt độ Celsius.",
   "Định luật Gay-Lussac", TB),

mc("Động năng tịnh tiến trung bình của một phân tử khí ở 27 °C bằng "
   "(k = 1,38·10⁻²³ J/K)",
   ["4,14·10⁻²¹ J.", "6,21·10⁻²¹ J.", "2,07·10⁻²¹ J.", "1,24·10⁻²⁰ J."],
   "B",
   "T = 300 K.\n"
   "W̄ₐ = (3/2)·k·T = 1,5 · 1,38·10⁻²³ · 300 = 1,5 · 4,14·10⁻²¹ = 6,21·10⁻²¹ J.",
   "Động năng phân tử", TB),

mc("Một khung dây phẳng quay đều trong từ trường đều. Tại thời điểm mặt phẳng khung vuông góc với "
   "đường sức từ thì suất điện động cảm ứng",
   ["đạt cực đại.", "bằng không.", "bằng nửa cực đại.", "không xác định."],
   "B",
   "Lúc đó từ thông đạt cực đại nên tốc độ biến thiên của nó bằng 0, do đó e = 0. "
   "Suất điện động và từ thông lệch pha nhau 90°.",
   "Máy phát điện xoay chiều", K, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

mc("Một thanh dẫn dài 40 cm trượt đều trên hai ray nghiêng 30°, không ma sát, trong từ trường đều "
   "B = 0,50 T vuông góc mặt phẳng nghiêng. Điện trở toàn mạch 0,20 Ω, khối lượng thanh 80 g. "
   "Tốc độ lớn nhất của thanh bằng (g = 10 m/s²)",
   ["1,0 m/s.", "2,0 m/s.", "4,0 m/s.", "0,50 m/s."],
   "B",
   "Thành phần trọng lực dọc mặt nghiêng: m·g·sin30° = 0,080 · 10 · 0,50 = 0,40 N.\n"
   "Lực từ cản: F = B²ℓ²v/R = (0,25 · 0,16/0,20)·v = 0,20v.\n"
   "Tốc độ lớn nhất khi gia tốc bằng 0: 0,20·v = 0,40 ⇒ v = 2,0 m/s.",
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng", cap="Thanh dẫn trên ray nghiêng"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 1500 vòng đặt dưới điện áp 220 V. Muốn có điện áp "
   "thứ cấp 22 V thì cuộn thứ cấp phải có",
   ["75 vòng.", "150 vòng.", "300 vòng.", "600 vòng."],
   "B",
   "N₂ = N₁·U₂/U₁ = 1500 · 22/220 = 1500/10 = 150 vòng.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Truyền công suất P đi xa, khi tăng điện áp truyền tải lên 4 lần thì công suất hao phí",
   ["giảm 4 lần.", "giảm 16 lần.", "tăng 4 lần.", "tăng 16 lần."],
   "B",
   "ΔP = R·P²/U² tỉ lệ nghịch với U². U tăng 4 lần thì hao phí giảm 4² = 16 lần.",
   "Hao phí truyền tải", TB, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Trong thí nghiệm cân dòng điện, khi cho dòng điện chạy qua đoạn dây nằm trong khe nam châm, "
   "số chỉ của cân thay đổi vì",
   ["khối lượng đoạn dây thay đổi.", "nam châm chịu phản lực của lực từ tác dụng lên đoạn dây.",
    "dòng điện làm nóng cân.", "đoạn dây bị nhiễm từ."],
   "B",
   "Lực từ tác dụng lên đoạn dây; theo định luật III Niu-tơn, nam châm chịu phản lực ngược lại "
   "nên áp lực lên cân thay đổi. Khối lượng các vật hoàn toàn không đổi.",
   "Cân dòng điện", TB, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

mc("Trong bảng dưới đây, hạt nhân nào bền vững nhất?",
   ["Hạt nhân P.", "Hạt nhân Q.", "Hạt nhân R.", "Hạt nhân S."],
   "B",
   "Tính năng lượng liên kết riêng ε = W(lk)/A cho từng hạt nhân:\n"
   "P: 120/16 = 7,50;  Q: 492/56 = 8,79;  R: 1786/235 = 7,60;  S: 28/4 = 7,00 MeV/nuclêôn.\n"
   "Hạt nhân Q có ε lớn nhất nên bền vững nhất.",
   "So sánh độ bền vững", K,
   tbl=("Năng lượng liên kết của bốn hạt nhân", ["Hạt nhân", "A", "W(lk) (MeV)"],
        [["P", "16", "120"], ["Q", "56", "492"], ["R", "235", "1786"], ["S", "4", "28"]])),

mc("Một chất phóng xạ có chu kì bán rã 8,0 ngày. Ban đầu có 64 gam. Sau 32 ngày, khối lượng "
   "còn lại bằng",
   ["8,0 gam.", "4,0 gam.", "2,0 gam.", "16,0 gam."],
   "B",
   "n = 32/8,0 = 4 chu kì ⇒ m = 64/2⁴ = 64/16 = 4,0 gam.",
   "Định luật phóng xạ", TB),

mc("Hạt nhân ²²⁶₈₈Ra phóng xạ α. Hạt nhân con có số nơtron bằng",
   ["134.", "136.", "138.", "140."],
   "B",
   "Hạt nhân con: A = 226 − 4 = 222; Z = 88 − 2 = 86.\n"
   "Số nơtron: N = 222 − 86 = 136.",
   "Quy tắc dịch chuyển", TB, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một nhà máy điện hạt nhân có công suất nhiệt 1000 MW, mỗi phân hạch toả 200 MeV. "
   "Số phân hạch xảy ra trong một giây xấp xỉ (1 MeV = 1,6·10⁻¹³ J)",
   ["3,13·10¹⁹.", "3,13·10²⁰.", "6,25·10¹⁹.", "1,56·10¹⁹."],
   "A",
   "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "Số phân hạch mỗi giây: 1,0·10⁹/3,2·10⁻¹¹ ≈ 3,13·10¹⁹.",
   "Công suất lò phản ứng", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Nguyên tắc “tăng khoảng cách” trong an toàn bức xạ dựa trên việc liều chiếu",
   ["tỉ lệ thuận với khoảng cách.", "tỉ lệ nghịch với bình phương khoảng cách.",
    "không phụ thuộc khoảng cách.", "tỉ lệ nghịch với khoảng cách."],
   "B",
   "Với nguồn điểm, bức xạ toả đều ra mọi phía nên cường độ giảm theo bình phương khoảng cách. "
   "Đứng xa gấp đôi thì liều chiếu chỉ còn một phần tư.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Hiện tượng nào sau đây KHÔNG liên quan tới cảm ứng điện từ?",
   ["Sạc không dây cho điện thoại.", "Bóng đèn sợi đốt phát sáng.",
    "Phanh điện từ trên tàu hoả.", "Máy phát điện xoay chiều."],
   "B",
   "Bóng đèn sợi đốt hoạt động nhờ tác dụng nhiệt của dòng điện. Ba hiện tượng còn lại đều dựa "
   "trên từ thông biến thiên sinh ra dòng cảm ứng.",
   "Ứng dụng cảm ứng điện từ", TB, fig="t_sd_sac_khong_day", cap="Nguyên lí sạc không dây"),
],
P2=[
ds("Bảng số liệu ghi nhiệt độ của một chất rắn theo thời gian khi được đun bằng bếp có công suất "
   "không đổi.",
   [("Trong giai đoạn nhiệt độ tăng đều, chất đang ở một thể xác định.", True,
     "Đúng. Nhiệt độ tăng nghĩa là chưa xảy ra chuyển thể, dùng công thức Q = mcΔT."),
    ("Giai đoạn nhiệt độ giữ nguyên ứng với quá trình nóng chảy.", True,
     "Đúng. Nhiệt lượng cung cấp lúc này dùng để phá vỡ mạng tinh thể."),
    ("Trong giai đoạn nóng chảy, nội năng của chất không đổi.", False,
     "Sai. Nội năng VẪN TĂNG vì chất liên tục thu nhiệt; phần nhiệt đó làm tăng thế năng tương tác "
     "giữa các hạt. Chỉ có động năng trung bình, tức nhiệt độ, là không đổi."),
    ("Độ dốc của đoạn nhiệt độ tăng tỉ lệ nghịch với nhiệt dung riêng của chất.", True,
     "Đúng. Với công suất không đổi, ΔT/Δt = P/(m·c) nên c càng lớn thì đồ thị càng thoải.")],
   "Đọc đồ thị chuyển thể", TB,
   tbl=("Nhiệt độ của mẫu chất rắn theo thời gian", ["t (phút)", "0", "2", "4", "6", "8", "10"],
        [["T (°C)", "20", "50", "80", "80", "80", "110"]])),

ds("Một khối khí lí tưởng ở 27 °C, áp suất 1,0·10⁵ Pa, thể tích 10 L.",
   [("Nung nóng đẳng tích tới 327 °C thì áp suất tăng lên 2,0·10⁵ Pa.", True,
     "Đúng. T₁ = 300 K, T₂ = 600 K nên p₂ = 2·p₁."),
    ("Nén đẳng nhiệt xuống 4,0 L thì áp suất tăng lên 2,5·10⁵ Pa.", True,
     "Đúng. p₂ = 1,0·10⁵ · 10/4,0 = 2,5·10⁵ Pa."),
    ("Động năng tịnh tiến trung bình của phân tử ở 27 °C xấp xỉ 6,21·10⁻²¹ J.", True,
     "Đúng. W̄ₐ = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J."),
    ("Nếu tăng nhiệt độ lên gấp đôi (theo thang Kelvin) thì tốc độ trung bình của phân tử cũng "
     "tăng gấp đôi.", False,
     "Sai. Động năng trung bình tăng gấp đôi nhưng tốc độ chỉ tăng √2 ≈ 1,41 lần vì W̄ₐ tỉ lệ "
     "với bình phương tốc độ.")],
   "Khí lí tưởng và động năng phân tử", K, fig="k_dt_phan_bo_toc_do",
   cap="Phân bố tốc độ phân tử"),

ds("Một thanh dẫn khối lượng 100 g, dài 50 cm trượt không ma sát trên hai ray nghiêng 30° trong "
   "từ trường đều B = 0,40 T vuông góc mặt phẳng nghiêng, điện trở toàn mạch 0,25 Ω. "
   "Lấy g = 10 m/s².",
   [("Thành phần trọng lực dọc mặt nghiêng là 0,50 N.", True,
     "Đúng. m·g·sin30° = 0,100 · 10 · 0,50 = 0,50 N."),
    ("Lực từ cản ở tốc độ v có độ lớn 0,16·v (đơn vị SI).", True,
     "Đúng. F = B²ℓ²v/R = (0,16 · 0,25/0,25)·v = 0,16v."),
    ("Tốc độ lớn nhất mà thanh đạt được là 3,125 m/s.", True,
     "Đúng. 0,16·v = 0,50 ⇒ v = 3,125 m/s."),
    ("Ngay khi vừa thả, lực từ cản đã đạt giá trị lớn nhất.", False,
     "Sai. Lúc v = 0 thì chưa có suất điện động nên lực từ cản bằng 0; nó tăng dần khi thanh "
     "chạy nhanh lên.")],
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng", cap="Thanh dẫn trên hai ray nghiêng"),

ds("Một nhà máy điện hạt nhân có công suất điện 500 MW và hiệu suất 32 %. Mỗi phân hạch ²³⁵U toả "
   "200 MeV. Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   [("Công suất nhiệt của lò xấp xỉ 1562,5 MW.", True,
     "Đúng. P(nhiệt) = 500/0,32 = 1562,5 MW."),
    ("Số phân hạch mỗi giây xấp xỉ 4,88·10¹⁹.", True,
     "Đúng. 1,5625·10⁹/3,2·10⁻¹¹ ≈ 4,88·10¹⁹ phân hạch mỗi giây."),
    ("Khối lượng ²³⁵U tiêu thụ trong một ngày xấp xỉ 1,65 kg.", True,
     "Đúng. Số hạt trong một ngày ≈ 4,88·10¹⁹ · 86 400 ≈ 4,22·10²⁴; "
     "khối lượng ≈ (4,22·10²⁴/6,02·10²³) · 235 ≈ 1647 g."),
    ("Nếu giữ nguyên công suất điện mà hạ hiệu suất xuống 16 % thì lượng nhiên liệu tiêu thụ "
     "cũng giảm một nửa.", False,
     "Sai. Hiệu suất giảm một nửa thì cần công suất nhiệt gấp đôi, nên lượng nhiên liệu tiêu thụ "
     "TĂNG gấp đôi.")],
   "Nhiên liệu của nhà máy điện hạt nhân", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),
],
P3=[
sa("Một bếp có công suất không đổi đun 0,50 kg chất lỏng. Sau 3,0 phút nhiệt độ tăng từ 20 °C "
   "lên 50 °C. Biết toàn bộ nhiệt lượng bếp toả ra đều truyền cho chất lỏng và nhiệt dung riêng "
   "của chất lỏng là 2400 J/(kg·K). Công suất của bếp bằng bao nhiêu oát?",
   "200",
   "Q = m·c·ΔT = 0,50 · 2400 · 30 = 36 000 J.\n"
   "t = 3,0 phút = 180 s.\n"
   "P = Q/t = 36 000/180 = 200 W.",
   "Nhiệt lượng và công suất", TB),

sa("Một bình kín chứa khí ở 27 °C, áp suất 1,2·10⁵ Pa. Muốn áp suất tăng lên 2,0·10⁵ Pa thì phải "
   "nung nóng khí tới bao nhiêu độ Celsius?",
   "227",
   "Đẳng tích: T₂ = T₁·p₂/p₁ = 300 · 2,0/1,2 = 500 K.\n"
   "t₂ = 500 − 273 = 227 °C.",
   "Định luật Gay-Lussac", TB),

sa("Một thanh dẫn khối lượng 120 g, dài 40 cm trượt không ma sát trên hai ray nghiêng 30° trong "
   "từ trường đều B = 0,50 T vuông góc mặt phẳng nghiêng, điện trở toàn mạch 0,20 Ω. "
   "Tốc độ lớn nhất của thanh bằng bao nhiêu mét trên giây? Lấy g = 10 m/s².",
   "3",
   "Thành phần trọng lực dọc mặt nghiêng: 0,120 · 10 · 0,50 = 0,60 N.\n"
   "Lực từ cản: F = B²ℓ²v/R = (0,25 · 0,16/0,20)·v = 0,20v.\n"
   "Tốc độ lớn nhất: 0,20·v = 0,60 ⇒ v = 3,0 m/s.",
   "Thanh dẫn trên mặt nghiêng", K),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 2400 vòng đặt dưới điện áp 240 V. Cuộn thứ cấp cung cấp "
   "điện áp 6,0 V. Số vòng cuộn thứ cấp bằng bao nhiêu?",
   "60",
   "N₂ = N₁·U₂/U₁ = 2400 · 6,0/240 = 2400/40 = 60 vòng.",
   "Máy biến áp", TB),

sa("Một hạt nhân có số khối 108 và năng lượng liên kết riêng 8,5 MeV/nuclêôn. Năng lượng liên kết "
   "của hạt nhân đó bằng bao nhiêu MeV?",
   "918",
   "W(lk) = ε·A = 8,5 · 108 = 918 MeV.",
   "Năng lượng liên kết", TB),

sa("Một nhà máy điện hạt nhân có công suất nhiệt 1200 MW, mỗi phân hạch toả 200 MeV. "
   "Số phân hạch xảy ra trong một giây bằng bao nhiêu (viết dưới dạng x·10¹⁹, chỉ ghi giá trị x, "
   "làm tròn đến chữ số thập phân thứ hai)? Cho 1 MeV = 1,6·10⁻¹³ J.",
   "3,75",
   "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "Số phân hạch mỗi giây: 1,2·10⁹/3,2·10⁻¹¹ = 3,75·10¹⁹.",
   "Công suất lò phản ứng", K),
])


# =====================================================================  ĐỀ 10
DE10 = dict(
ma="TH-Đề 10", ten="ĐỀ THI THỬ SỐ 10", muc="Trung bình",
trongtam="Tổng duyệt mức Trung bình trước khi bước sang nhóm đề khó",
P1=[
mc("Một vật có khối lượng 2,0 kg rơi từ độ cao 20 m xuống đất và dừng lại hẳn. Nếu toàn bộ cơ năng "
   "biến thành nội năng của vật thì nội năng vật tăng thêm (g = 10 m/s²)",
   ["200 J.", "400 J.", "40 J.", "800 J."],
   "B",
   "Cơ năng ban đầu: W = m·g·h = 2,0 · 10 · 20 = 400 J.\n"
   "Toàn bộ chuyển thành nội năng nên ΔU = 400 J.",
   "Chuyển hoá cơ năng thành nội năng", TB),

mc("Nhiệt độ của một vật tăng thêm 40 °C thì theo thang Kelvin nhiệt độ đó tăng thêm",
   ["313 K.", "40 K.", "233 K.", "353 K."],
   "B",
   "Một độ chia của thang Kelvin bằng đúng một độ chia của thang Celsius nên ĐỘ BIẾN THIÊN "
   "nhiệt độ tính theo hai thang là như nhau: ΔT = Δt = 40 K.",
   "Thang nhiệt độ", TB),

mc("Nhiệt lượng cần để đun 0,50 kg nước từ 30 °C tới 80 °C bằng "
   "(c = 4200 J/(kg·K))",
   ["52,5 kJ.", "105 kJ.", "168 kJ.", "210 kJ."],
   "B",
   "Q = 0,50 · 4200 · (80 − 30) = 0,50 · 4200 · 50 = 105 000 J = 105 kJ.",
   "Nhiệt lượng", TB),

mc("Một khối khí lí tưởng có áp suất 2,0·10⁵ Pa, thể tích 3,0 L, nhiệt độ 300 K. "
   "Nếu giữ nhiệt độ không đổi và tăng thể tích lên 6,0 L thì áp suất bằng",
   ["4,0·10⁵ Pa.", "1,0·10⁵ Pa.", "2,0·10⁵ Pa.", "0,50·10⁵ Pa."],
   "B",
   "Đẳng nhiệt: p₂ = p₁·V₁/V₂ = 2,0·10⁵ · 3,0/6,0 = 1,0·10⁵ Pa.",
   "Định luật Boyle", TB),

mc("Trong hệ toạ độ (V, T), đường đẳng áp là",
   ["đường hypebol.", "đường thẳng qua gốc toạ độ.",
    "đường thẳng song song trục hoành.", "đường parabol."],
   "B",
   "Đẳng áp cho V/T = hằng số nên V tỉ lệ thuận với T: đồ thị là đường thẳng đi qua gốc toạ độ "
   "trong hệ (V, T).",
   "Đồ thị các quá trình", TB, fig="k_dt_ba_he_truc", cap="Ba quá trình trên ba hệ trục"),

mc("Một bình 20 L chứa 32 g khí ôxi (M = 32 g/mol) ở 27 °C. Áp suất khí trong bình xấp xỉ "
   "(R = 8,31 J/(mol·K))",
   ["0,62·10⁵ Pa.", "1,25·10⁵ Pa.", "2,49·10⁵ Pa.", "4,99·10⁵ Pa."],
   "B",
   "n = 32/32 = 1,0 mol;  V = 20·10⁻³ m³;  T = 300 K.\n"
   "p = nRT/V = 1,0 · 8,31 · 300/(20·10⁻³) = 2493/0,020 ≈ 1,25·10⁵ Pa.",
   "Phương trình Clapeyron", K),

mc("Khi tăng nhiệt độ tuyệt đối của một khối khí lên gấp bốn lần thì tốc độ trung bình của "
   "phân tử khí",
   ["tăng gấp bốn.", "tăng gấp đôi.", "tăng 16 lần.", "không đổi."],
   "B",
   "W̄ₐ = (3/2)kT tỉ lệ thuận với T và cũng tỉ lệ với bình phương tốc độ. "
   "T tăng 4 lần thì v̄² tăng 4 lần nên v̄ tăng √4 = 2 lần.",
   "Động năng phân tử", K),

mc("Một đoạn dây dẫn dài 25 cm mang dòng điện 6,0 A đặt vuông góc với từ trường đều B = 0,20 T. "
   "Lực từ tác dụng lên dây bằng",
   ["0,15 N.", "0,30 N.", "0,60 N.", "1,20 N."],
   "B",
   "F = B·I·ℓ = 0,20 · 6,0 · 0,25 = 0,30 N.",
   "Lực từ", TB),

mc("Một khung dây phẳng 100 vòng đặt vuông góc với từ trường đều. Khi cảm ứng từ tăng đều từ 0,20 T "
   "lên 0,50 T trong 0,25 s, diện tích mỗi vòng 40 cm², suất điện động cảm ứng bằng",
   ["0,24 V.", "0,48 V.", "0,96 V.", "0,12 V."],
   "B",
   "S = 4,0·10⁻³ m²;  ΔB = 0,30 T.\n"
   "|ΔΦ| mỗi vòng = 0,30 · 4,0·10⁻³ = 1,2·10⁻³ Wb.\n"
   "|e| = 100 · 1,2·10⁻³/0,25 = 100 · 4,8·10⁻³ = 0,48 V.",
   "Định luật Faraday", TB),

mc("Trong máy phát điện xoay chiều một pha có p cặp cực, rôto quay n vòng mỗi giây thì tần số "
   "dòng điện phát ra là",
   ["f = n/p.", "f = p·n.", "f = p/n.", "f = 2p·n."],
   "B",
   "f = p·n. Với p = 1 và n = 50 vòng/giây (3000 vòng/phút) ta có f = 50 Hz.",
   "Máy phát điện xoay chiều", TB),

mc("Điện áp hiệu dụng ở hai đầu một thiết bị là 110 V. Giá trị cực đại của điện áp đó xấp xỉ",
   ["78 V.", "156 V.", "110 V.", "220 V."],
   "B",
   "U₀ = U·√2 = 110 · 1,414 ≈ 156 V. Giá trị 78 V là kết quả khi chia cho √2 thay vì nhân.",
   "Giá trị hiệu dụng", TB, fig="t_dt_u_i_hieudung", cap="Điện áp tức thời và giá trị hiệu dụng"),

mc("Một máy biến áp lí tưởng có số vòng cuộn thứ cấp gấp 5 lần cuộn sơ cấp. "
   "Nếu điện áp sơ cấp là 24 V thì điện áp thứ cấp bằng",
   ["4,8 V.", "120 V.", "24 V.", "48 V."],
   "B",
   "U₂ = U₁·N₂/N₁ = 24 · 5 = 120 V. Đây là máy tăng áp.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Hạt nhân ⁴⁰₂₀Ca có bao nhiêu nuclêôn và bao nhiêu nơtron?",
   ["40 nuclêôn và 40 nơtron.", "40 nuclêôn và 20 nơtron.",
    "20 nuclêôn và 20 nơtron.", "60 nuclêôn và 20 nơtron."],
   "B",
   "Số nuclêôn bằng số khối A = 40. Số nơtron N = A − Z = 40 − 20 = 20.",
   "Cấu tạo hạt nhân", TB),

mc("Một hạt nhân có độ hụt khối 0,30 u. Năng lượng liên kết của hạt nhân đó bằng",
   ["139,7 MeV.", "279,5 MeV.", "419,2 MeV.", "93,2 MeV."],
   "B",
   "W(lk) = 0,30 · 931,5 = 279,45 ≈ 279,5 MeV.",
   "Năng lượng liên kết", TB),

mc("Một chất phóng xạ có chu kì bán rã 4,0 ngày. Sau 20 ngày, phần trăm số hạt nhân đã phân rã bằng",
   ["3,125 %.", "96,875 %.", "50 %.", "6,25 %."],
   "B",
   "n = 20/4,0 = 5 chu kì ⇒ còn lại 2⁻⁵ = 3,125 %.\n"
   "Đã phân rã: 100 − 3,125 = 96,875 %.",
   "Định luật phóng xạ", TB),

mc("Trong phản ứng hạt nhân, tổng năng lượng toàn phần (bao gồm cả năng lượng nghỉ)",
   ["không được bảo toàn.", "luôn được bảo toàn.",
    "chỉ bảo toàn khi phản ứng toả năng lượng.", "chỉ bảo toàn khi các hạt đứng yên."],
   "B",
   "Năng lượng toàn phần luôn được bảo toàn trong mọi phản ứng hạt nhân. Điều KHÔNG bảo toàn "
   "là khối lượng nghỉ: phần hụt đi chuyển thành động năng và bức xạ.",
   "Định luật bảo toàn", TB),

mc("Đồng vị ¹⁴C dùng để xác định tuổi mẫu vật có chu kì bán rã",
   ["138 ngày.", "5730 năm.", "4,5 tỉ năm.", "30 năm."],
   "B",
   "Chu kì bán rã của ¹⁴C là 5730 năm, phù hợp để xác định tuổi mẫu vật khảo cổ từ vài trăm tới "
   "khoảng 50 000 năm.",
   "Xác định tuổi bằng cacbon-14", TB, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

mc("Biện pháp nào sau đây KHÔNG giúp giảm liều chiếu khi làm việc với nguồn phóng xạ?",
   ["Rút ngắn thời gian tiếp xúc.", "Tăng cường độ chiếu sáng trong phòng.",
    "Đứng xa nguồn hơn.", "Dùng tấm chì che chắn."],
   "B",
   "Cường độ chiếu sáng không liên quan tới bức xạ ion hoá. Ba biện pháp còn lại chính là "
   "ba nguyên tắc an toàn bức xạ: thời gian, khoảng cách và che chắn.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),
],
P2=[
ds("Một búa máy khối lượng 200 kg rơi từ độ cao 2,0 m đập vào một cọc sắt khối lượng 50 kg. "
   "Giả sử 40 % cơ năng của búa biến thành nội năng của cọc. "
   "Cho c(sắt) = 460 J/(kg·K); g = 10 m/s².",
   [("Cơ năng của búa ngay trước khi va chạm là 4000 J.", True,
     "Đúng. W = m·g·h = 200 · 10 · 2,0 = 4000 J."),
    ("Nội năng của cọc tăng thêm 1600 J sau mỗi lần đập.", True,
     "Đúng. ΔU = 40 % · 4000 = 1600 J."),
    ("Sau một lần đập, nhiệt độ cọc tăng thêm khoảng 0,07 °C.", True,
     "Đúng. ΔT = ΔU/(m·c) = 1600/(50 · 460) = 1600/23 000 ≈ 0,0696 °C."),
    ("Sau 100 lần đập liên tiếp (bỏ qua toả nhiệt), nhiệt độ cọc tăng khoảng 0,7 °C.", False,
     "Sai. Nhiệt độ tăng khoảng 100 · 0,0696 ≈ 7,0 °C chứ không phải 0,7 °C.")],
   "Chuyển hoá cơ năng thành nội năng", K),

ds("Một lượng khí lí tưởng gồm 0,50 mol chứa trong bình 4,155 L ở 27 °C. "
   "Cho R = 8,31 J/(mol·K).",
   [("Áp suất khí trong bình bằng 3,0·10⁵ Pa.", True,
     "Đúng. p = nRT/V = 0,50 · 8,31 · 300/(4,155·10⁻³) = 1246,5/4,155·10⁻³ = 3,0·10⁵ Pa."),
    ("Nếu nung nóng đẳng tích lên 327 °C thì áp suất tăng lên 6,0·10⁵ Pa.", True,
     "Đúng. T₂ = 600 K, gấp đôi T₁ = 300 K nên p₂ = 2·p₁."),
    ("Nếu bơm thêm 0,50 mol khí cùng loại ở nhiệt độ không đổi thì áp suất tăng gấp đôi.", True,
     "Đúng. Với V và T không đổi, p tỉ lệ thuận với số mol."),
    ("Nếu thay bằng 0,50 mol khí khác loại ở cùng nhiệt độ thì áp suất sẽ khác đi.", False,
     "Sai. Phương trình pV = nRT không chứa bản chất khí, nên cùng số mol, cùng V và T thì "
     "áp suất như nhau với mọi khí lí tưởng.")],
   "Phương trình Clapeyron", K),

ds("Một khung dây phẳng 200 vòng, diện tích mỗi vòng 50 cm², đặt trong từ trường đều B = 0,40 T "
   "với pháp tuyến song song đường sức. Người ta quay khung 90° trong 0,40 s.",
   [("Từ thông qua mỗi vòng lúc đầu là 2,0·10⁻³ Wb.", True,
     "Đúng. Φ = B·S = 0,40 · 5,0·10⁻³ = 2,0·10⁻³ Wb."),
    ("Sau khi quay 90°, từ thông qua khung bằng 0.", True,
     "Đúng. Pháp tuyến vuông góc với B nên cosθ = 0."),
    ("Suất điện động cảm ứng trung bình bằng 1,0 V.", True,
     "Đúng. |e| = N·|ΔΦ|/Δt = 200 · 2,0·10⁻³/0,40 = 200 · 5,0·10⁻³ = 1,0 V."),
    ("Nếu quay khung 180° trong cùng thời gian thì suất điện động trung bình cũng bằng 1,0 V.", False,
     "Sai. Quay 180° làm từ thông đổi từ +B·S sang −B·S, độ biến thiên gấp đôi nên suất điện động "
     "trung bình bằng 2,0 V.")],
   "Định luật Faraday – quay khung", K),

ds("Một mẫu chất phóng xạ nguyên chất có chu kì bán rã 6,0 giờ, ban đầu có 3,2·10²⁰ hạt nhân.",
   [("Sau 6,0 giờ, số hạt nhân còn lại là 1,6·10²⁰ hạt.", True,
     "Đúng. Sau một chu kì, số hạt còn một nửa."),
    ("Sau 18 giờ, số hạt nhân đã phân rã là 2,8·10²⁰ hạt.", True,
     "Đúng. n = 3 ⇒ còn 0,4·10²⁰ hạt; đã rã 3,2·10²⁰ − 0,4·10²⁰ = 2,8·10²⁰ hạt."),
    ("Số hạt phân rã trong 6 giờ đầu nhiều hơn số hạt phân rã trong 6 giờ tiếp theo.", True,
     "Đúng. 1,6·10²⁰ so với 0,8·10²⁰ — trong các chu kì liên tiếp, số hạt phân rã giảm một nửa."),
    ("Sau 24 giờ, toàn bộ số hạt nhân đã phân rã hết.", False,
     "Sai. Sau 24 giờ (4 chu kì) vẫn còn 3,2·10²⁰/16 = 0,2·10²⁰ hạt.")],
   "Định luật phóng xạ", TB, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),
],
P3=[
sa("Một vật khối lượng 5,0 kg rơi từ độ cao 16 m xuống đất và dừng lại. Nếu 60 % cơ năng biến "
   "thành nội năng của vật thì nội năng vật tăng thêm bao nhiêu jun? Lấy g = 10 m/s².",
   "480",
   "Cơ năng: W = m·g·h = 5,0 · 10 · 16 = 800 J.\n"
   "Nội năng tăng: ΔU = 60 % · 800 = 480 J.",
   "Chuyển hoá cơ năng thành nội năng", TB),

sa("Một bình 8,31 L chứa 0,40 mol khí lí tưởng ở 27 °C. Áp suất khí trong bình bằng bao nhiêu "
   "(viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho R = 8,31 J/(mol·K).",
   "1,2",
   "V = 8,31·10⁻³ m³;  T = 300 K.\n"
   "p = nRT/V = 0,40 · 8,31 · 300/(8,31·10⁻³) = 997,2/8,31·10⁻³ = 1,2·10⁵ Pa.",
   "Phương trình Clapeyron", K),

sa("Một khung dây 150 vòng, diện tích mỗi vòng 60 cm², đặt trong từ trường đều B = 0,50 T với "
   "pháp tuyến song song đường sức. Quay khung 180° trong 0,50 s. Suất điện động cảm ứng trung bình "
   "bằng bao nhiêu vôn?",
   "1,8",
   "Φ mỗi vòng lúc đầu: 0,50 · 6,0·10⁻³ = 3,0·10⁻³ Wb; sau khi quay 180° là −3,0·10⁻³ Wb.\n"
   "|ΔΦ| = 6,0·10⁻³ Wb.\n"
   "|e| = N·|ΔΦ|/Δt = 150 · 6,0·10⁻³/0,50 = 150 · 0,012 = 1,8 V.",
   "Định luật Faraday – quay khung", K),

sa("Một máy phát điện xoay chiều có 4 cặp cực, rôto quay 900 vòng/phút. Tần số của dòng điện "
   "phát ra bằng bao nhiêu héc?",
   "60",
   "n = 900/60 = 15 vòng/giây.\n"
   "f = p·n = 4 · 15 = 60 Hz.",
   "Máy phát nhiều cặp cực", TB),

sa("Hạt nhân ²⁰⁸₈₂Pb có năng lượng liên kết riêng 7,9 MeV/nuclêôn. Năng lượng liên kết của hạt nhân "
   "này bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ nhất)?",
   "1643,2",
   "W(lk) = ε·A = 7,9 · 208 = 1643,2 MeV.",
   "Năng lượng liên kết", TB),

sa("Một mẫu chất phóng xạ có chu kì bán rã 9,0 ngày. Sau bao nhiêu ngày thì số hạt nhân còn lại "
   "bằng 1/64 số hạt nhân ban đầu?",
   "54",
   "1/64 = 2⁻⁶ nên n = 6 chu kì bán rã.\n"
   "t = 6 · 9,0 = 54 ngày.",
   "Định luật phóng xạ", TB),
])


NHOM = dict(
    ten_nhom="ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG  (Đề 06 – 10)",
    mo_ta="Năm đề mức Trung bình, bắt đầu xuất hiện các câu vận dụng nhiều bước",
    pham_vi=(
        "Chương I. Vật lí nhiệt  •  Chương II. Khí lí tưởng  •  "
        "Chương III. Từ trường  •  Chương IV. Vật lí hạt nhân\n"
        "Mỗi đề gồm 28 câu / 40 lệnh hỏi, thời gian 50 phút, thang điểm 10.\n"
        "Hằng số: c(nước) = 4200 J/(kg·K); λ(nước đá) = 3,4·10⁵ J/kg; L(nước) = 2,26·10⁶ J/kg; "
        "g = 10 m/s²; R = 8,31 J/(mol·K); k = 1,38·10⁻²³ J/K; Nₐ = 6,02·10²³ mol⁻¹; "
        "1 u·c² = 931,5 MeV; 1 MeV = 1,6·10⁻¹³ J; π ≈ 3,1416; √2 ≈ 1,414; ln2 ≈ 0,693."),
    tests=[DE6, DE7, DE8, DE9, DE10],
)
