# -*- coding: utf-8 -*-
"""BỘ 2 – BÀI TẬP CỰC KHÓ: CHƯƠNG III (TỪ TRƯỜNG) VÀ CHƯƠNG IV (VẬT LÍ HẠT NHÂN).

Cấu trúc và khoá dữ liệu giống hệt book1.py.
"""

# =====================================================================
# PHẦN I – TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN
# =====================================================================
P1 = [

dict(
tag="Cảm ứng điện từ – trạng thái dừng",
q="Một thanh kim loại MN khối lượng m = 20 g, chiều dài phần nằm giữa hai ray ℓ = 0,5 m, trượt không ma "
  "sát trên hai ray song song đặt trên một mặt phẳng nghiêng góc 30° so với phương ngang. Hai ray được nối "
  "với một điện trở, tổng điện trở của mạch là R = 0,2 Ω. Từ trường đều B = 0,4 T có phương vuông góc với "
  "mặt phẳng nghiêng. Thả cho thanh trượt xuống từ trạng thái nghỉ; lấy g = 10 m/s². Tốc độ lớn nhất mà "
  "thanh đạt được bằng",
fig="b2_ray_nghieng",
cap="Thanh dẫn trượt trên hai ray đặt trên mặt phẳng nghiêng",
o=["0,25 m/s.", "0,50 m/s.", "1,00 m/s.", "2,00 m/s."],
a="B",
sol="Thanh đạt tốc độ lớn nhất khi gia tốc bằng không, tức là lực từ cản trở cân bằng với thành phần trọng "
    "lực dọc theo mặt phẳng nghiêng.\n"
    "• Suất điện động cảm ứng: e = Bℓv.\n"
    "• Cường độ dòng điện: I = Bℓv/R.\n"
    "• Lực từ tác dụng lên thanh (ngược chiều chuyển động, theo định luật Lenz): F = BIℓ = B²ℓ²v/R.\n"
    "Điều kiện cân bằng: mg·sinα = B²ℓ²v_max/R\n"
    "  v_max = mgR·sinα/(B²ℓ²) = (0,02·10·0,2·0,5)/(0,4²·0,5²) = 0,02/0,04 = 0,50 m/s.\n"
    "Kiểm tra bằng năng lượng: ở tốc độ đó công suất trọng lực mg·v·sinα = 0,02·10·0,5·0,5 = 0,05 W, còn "
    "công suất toả nhiệt I²R với I = Bℓv/R = 0,5 A là 0,5²·0,2 = 0,05 W ✓.\n"
    "Bẫy: quên thừa số sinα cho ra 1,00 m/s."),

dict(
tag="Đồ thị Φ(t) – biến đổi sang e(t)",
q="Hình dưới đây là đồ thị từ thông qua MỖI VÒNG dây của một khung dây phẳng theo thời gian, gồm bốn giai đoạn "
  "(I), (II), (III), (IV). Suất điện động cảm ứng trong mỗi vòng dây có độ lớn lớn nhất ở giai đoạn nào và "
  "bằng bao nhiêu?",
fig="b2_do_thi_phi_t",
cap="Từ thông qua mỗi vòng dây theo thời gian",
o=["Giai đoạn (I); 0,20 V.",
   "Giai đoạn (III); 0,40 V.",
   "Giai đoạn (IV); 0,60 V.",
   "Giai đoạn (IV); 0,20 V."],
a="B",
sol="Suất điện động cảm ứng bằng độ lớn HỆ SỐ GÓC của đồ thị Φ(t), chứ không phải độ lớn của ΔΦ:\n"
    "  |e| = |ΔΦ/Δt|.\n"
    "• (I): ΔΦ = 0,4 Wb trong 2 s ⟹ |e| = 0,20 V.\n"
    "• (II): Φ không đổi ⟹ |e| = 0.\n"
    "• (III): ΔΦ = −0,4 Wb trong 1 s ⟹ |e| = 0,40 V.\n"
    "• (IV): ΔΦ = −0,6 Wb trong 3 s ⟹ |e| = 0,20 V.\n"
    "Vậy giai đoạn (III) cho suất điện động lớn nhất, bằng 0,40 V.\n"
    "Bẫy: giai đoạn (IV) có độ biến thiên từ thông LỚN NHẤT (0,6 Wb) nhưng lại diễn ra trong thời gian dài "
    "nhất nên tốc độ biến thiên chỉ ở mức trung bình."),

dict(
tag="Máy biến áp – hệ hai phương trình",
q="Đặt vào cuộn sơ cấp của một máy biến áp lí tưởng một điện áp xoay chiều có giá trị hiệu dụng 200 V "
  "không đổi. Khi cuộn thứ cấp có N₂ vòng thì điện áp hiệu dụng ở hai đầu cuộn thứ cấp để hở là 20 V. Nếu "
  "quấn thêm 60 vòng nữa vào cuộn thứ cấp thì điện áp hiệu dụng ở hai đầu cuộn thứ cấp để hở là 25 V. Số "
  "vòng của cuộn sơ cấp bằng",
fig="b2_may_bien_ap",
cap="Sơ đồ máy biến áp",
o=["240 vòng.", "480 vòng.", "1200 vòng.", "2400 vòng."],
a="D",
sol="Với máy biến áp lí tưởng, U₂/U₁ = N₂/N₁. Lập hệ:\n"
    "  N₂/N₁ = 20/200 = 0,10          (1)\n"
    "  (N₂ + 60)/N₁ = 25/200 = 0,125  (2)\n"
    "Trừ (1) khỏi (2), N₂ bị khử:\n"
    "  60/N₁ = 0,025 ⟹ N₁ = 2400 vòng, và N₂ = 0,10·2400 = 240 vòng.\n"
    "Kiểm tra: 240/2400 = 0,1 ✓ và 300/2400 = 0,125 ✓.\n"
    "Bẫy: 240 vòng là số vòng của cuộn THỨ CẤP, không phải sơ cấp."),

dict(
tag="Dòng xoay chiều – ý nghĩa của giá trị hiệu dụng",
q="Một dòng điện xoay chiều i = I₀cos(ωt) chạy qua một điện trở. Trong một chu kì, khoảng thời gian mà "
  "cường độ dòng điện tức thời có ĐỘ LỚN lớn hơn giá trị hiệu dụng của nó chiếm tỉ lệ bao nhiêu?",
fig="b2_do_thi_i_t",
cap="Đồ thị i(t) và hai mức ±I₀/√2 ứng với giá trị hiệu dụng",
o=["25%.", "33,3%.", "50%.", "70,7%."],
a="C",
sol="Giá trị hiệu dụng của dòng điện xoay chiều hình sin là I = I₀/√2.\n"
    "Yêu cầu: |I₀cos(ωt)| > I₀/√2 ⟺ |cos(ωt)| > √2/2 ⟺ |cos(ωt)| > cos45°.\n"
    "Đặt φ = ωt. Trong một chu kì φ chạy hết 360°. Điều kiện |cosφ| > cos45° được thoả mãn khi φ nằm trong "
    "khoảng ±45° quanh 0° và ±45° quanh 180°, tức bốn cung 45° — tổng cộng 4·45° = 180°.\n"
    "Tỉ lệ thời gian: 180°/360° = 50%.\n"
    "Nhận xét: giá trị hiệu dụng KHÔNG phải giá trị trung bình của |i|; nó là giá trị của dòng không đổi "
    "gây ra cùng công suất toả nhiệt. Con số 70,7% chỉ là tỉ số I/I₀, không phải tỉ lệ thời gian."),

dict(
tag="Máy phát điện xoay chiều",
q="Một khung dây phẳng gồm 200 vòng, diện tích mỗi vòng 100 cm², quay đều với tốc độ 300 vòng/phút quanh "
  "một trục nằm trong mặt phẳng khung và vuông góc với các đường sức của từ trường đều B = 0,2 T. Suất điện "
  "động HIỆU DỤNG xuất hiện trong khung gần nhất với giá trị nào sau đây?",
fig="b2_khung_quay",
cap="Khung dây quay đều trong từ trường đều",
o=["4,0 V.", "8,9 V.", "12,6 V.", "17,8 V."],
a="B",
sol="Bước 1 – tốc độ góc: ω = 2πn = 2π·(300/60) = 10π ≈ 31,42 rad/s (tần số f = 5 Hz).\n"
    "Bước 2 – từ thông cực đại qua khung: Φ₀ = N·B·S = 200·0,2·100·10⁻⁴ = 0,4 Wb.\n"
    "Bước 3 – suất điện động cực đại: E₀ = ω·Φ₀ = 31,42·0,4 ≈ 12,57 V.\n"
    "Bước 4 – giá trị hiệu dụng: E = E₀/√2 ≈ 12,57/1,414 ≈ 8,9 V.\n"
    "Bẫy: dừng lại ở E₀ = 12,6 V (giá trị CỰC ĐẠI, không phải hiệu dụng); hoặc quên đổi vòng/phút sang "
    "rad/s."),

dict(
tag="Lực từ – cân bằng lực",
q="Một thanh kim loại MN khối lượng 20 g, dài 25 cm, được treo nằm ngang bằng hai lò xo giống nhau. Từ "
  "trường đều B = 0,4 T nằm ngang và vuông góc với thanh. Khi cho dòng điện I = 2 A chạy qua thanh thì mỗi "
  "lò xo dãn thêm 1 cm so với khi chưa có dòng điện. Độ cứng của mỗi lò xo bằng",
fig="b2_thanh_lo_xo",
cap="Thanh dẫn treo bằng hai lò xo trong từ trường đều",
o=["5 N/m.", "10 N/m.", "20 N/m.", "40 N/m."],
a="B",
sol="Lực từ tác dụng lên thanh (thanh vuông góc với B nên sinθ = 1):\n"
    "  F = B·I·ℓ = 0,4·2·0,25 = 0,20 N, hướng thẳng đứng xuống dưới (làm lò xo dãn thêm).\n"
    "Trọng lượng của thanh không đổi nên không tham gia vào ĐỘ DÃN THÊM; toàn bộ lực từ được chia đều cho "
    "HAI lò xo:\n"
    "  F_mỗi lò xo = 0,20/2 = 0,10 N.\n"
    "Định luật Hooke cho phần dãn thêm: k = ΔF/Δℓ = 0,10/0,01 = 10 N/m.\n"
    "Bẫy: quên chia cho hai lò xo cho ra 20 N/m; đưa cả trọng lượng thanh vào tính toán cũng sai vì đề chỉ "
    "hỏi độ dãn THÊM."),

dict(
tag="Từ thông – góc nào mới đúng",
q="Một khung dây phẳng hình chữ nhật kích thước 20 cm × 30 cm, gồm 50 vòng dây, được đặt trong một từ "
  "trường đều có cảm ứng từ B = 0,1 T. Mặt phẳng của khung hợp với vectơ cảm ứng từ một góc 30°. Từ thông "
  "qua khung dây bằng",
fig="b2_khung_nghieng_B",
cap="Mặt phẳng khung hợp với vectơ cảm ứng từ góc 30°; α là góc giữa pháp tuyến và B",
o=["0,15 Wb.", "0,26 Wb.", "0,30 Wb.", "0,52 Wb."],
a="A",
sol="Công thức từ thông là Φ = N·B·S·cosα, trong đó α là góc giữa vectơ PHÁP TUYẾN của mặt phẳng khung và "
    "vectơ cảm ứng từ — KHÔNG phải góc giữa mặt phẳng khung và B.\n"
    "Đề cho góc giữa MẶT PHẲNG khung và B là 30°, mà pháp tuyến vuông góc với mặt phẳng khung nên\n"
    "  α = 90° − 30° = 60°.\n"
    "  S = 0,20·0,30 = 0,06 m².\n"
    "  Φ = 50·0,1·0,06·cos60° = 0,3·0,5 = 0,15 Wb.\n"
    "Bẫy: dùng thẳng cos30° cho ra 0,26 Wb — đây là phương án sai được chọn nhiều nhất."),

dict(
tag="Năng lượng liên kết – tính theo ε",
q="Cho năng lượng liên kết riêng của các hạt nhân ²₁H, ³₁H và ⁴₂He lần lượt là 1,11 MeV/nuclôn; "
  "2,83 MeV/nuclôn và 7,07 MeV/nuclôn. Năng lượng toả ra của phản ứng ²₁H + ³₁H → ⁴₂He + ¹₀n gần nhất với "
  "giá trị nào sau đây?",
o=["3,13 MeV.", "11,4 MeV.", "17,6 MeV.", "39,0 MeV."],
a="C",
sol="Năng lượng của phản ứng bằng hiệu tổng NĂNG LƯỢNG LIÊN KẾT (không phải năng lượng liên kết riêng) "
    "của các hạt sau và trước phản ứng. Với mỗi hạt nhân, W_lk = ε·A:\n"
    "  W_lk(²₁H) = 1,11·2 = 2,22 MeV\n"
    "  W_lk(³₁H) = 2,83·3 = 8,49 MeV\n"
    "  W_lk(⁴₂He) = 7,07·4 = 28,28 MeV\n"
    "  W_lk(¹₀n) = 0 (nơtron chỉ có một nuclôn, không có liên kết).\n"
    "  ΔE = 28,28 − (2,22 + 8,49) = 17,57 ≈ 17,6 MeV > 0 ⟹ phản ứng toả năng lượng.\n"
    "Bẫy lớn nhất: cộng trừ trực tiếp các giá trị ε mà quên nhân với số khối A, cho ra "
    "7,07 − 1,11 − 2,83 = 3,13 MeV."),

dict(
tag="Thực nghiệm hạt nhân – đại lượng nào đo được",
q="Dùng một máy đếm đặt gần một mẫu chất phóng xạ để đo số hạt phát ra. Máy chỉ ghi nhận được một tỉ lệ h "
  "(chưa biết, không đổi) của tổng số hạt mà mẫu phát ra. Lần đo thứ nhất, trong 1 phút máy đếm được 4800 "
  "xung. Sau đó 12 giờ, cũng trong 1 phút, máy đếm được 600 xung. Kết luận nào sau đây đúng?",
o=["Không xác định được chu kì bán rã vì chưa biết hiệu suất h của máy đếm.",
   "Xác định được chu kì bán rã T = 4 giờ, nhưng không xác định được số hạt nhân ban đầu của mẫu.",
   "Xác định được cả chu kì bán rã T = 4 giờ và số hạt nhân ban đầu của mẫu.",
   "Xác định được chu kì bán rã T = 3 giờ."],
a="B",
sol="Số xung máy đếm được trong 1 phút tỉ lệ thuận với độ phóng xạ của mẫu: n = h·H = h·H₀·2^(−t/T).\n"
    "Khi lập TỈ SỐ hai lần đo, hệ số h bị khử hoàn toàn:\n"
    "  n₁/n₂ = 4800/600 = 8 = 2³ ⟹ t = 3T ⟹ T = 12/3 = 4 giờ.\n"
    "Ngược lại, muốn tìm số hạt nhân ban đầu N₀ thì phải qua H₀ = λN₀, mà H₀ = n₁/h lại đòi hỏi biết h. "
    "Vì h chưa biết nên N₀ KHÔNG xác định được.\n"
    "Đây là tình huống thực nghiệm rất phổ biến: chu kì bán rã đo được rất chính xác chỉ nhờ tỉ số, còn "
    "hoạt độ tuyệt đối thì luôn cần chuẩn hoá máy đo."),

dict(
tag="Ứng dụng – định tuổi bằng ¹⁴C",
q="Độ phóng xạ của ¹⁴C tính trên mỗi gam cacbon trong một mẫu gỗ cổ bằng 20% giá trị đo được ở một mẫu gỗ "
  "tươi cùng loại. Chu kì bán rã của ¹⁴C là 5730 năm. Tuổi của mẫu gỗ cổ gần nhất với giá trị nào sau đây?",
o=["8,0·10³ năm.", "1,15·10⁴ năm.", "1,33·10⁴ năm.", "2,87·10⁴ năm."],
a="C",
sol="Cơ sở của phương pháp: khi cây còn sống, nó liên tục trao đổi cacbon với khí quyển nên tỉ lệ ¹⁴C giữ "
    "không đổi; khi cây chết, ¹⁴C chỉ còn giảm theo quy luật phóng xạ. Vì tính trên mỗi gam cacbon nên "
    "khối lượng mẫu không ảnh hưởng.\n"
    "  H/H₀ = 2^(−t/T) = 0,20 ⟹ 2^(t/T) = 5 ⟹ t/T = log₂5 = ln5/ln2 ≈ 2,322\n"
    "  t = 2,322·5730 ≈ 13 305 năm ≈ 1,33·10⁴ năm.\n"
    "Bẫy: làm tròn 20% thành 25% để được đúng 2 chu kì bán rã (1,15·10⁴ năm) — sai lệch tới gần 2000 năm."),

dict(
tag="Phân hạch – bài toán năng lượng nhà máy",
q="Một nhà máy điện hạt nhân có công suất điện 500 MW; hiệu suất chuyển hoá từ năng lượng hạt nhân thành "
  "điện năng là 20%. Mỗi phân hạch ²³⁵U toả ra năng lượng 200 MeV. Cho N_A = 6,02·10²³ mol⁻¹, "
  "1 MeV = 1,6·10⁻¹³ J. Khối lượng ²³⁵U bị phân hạch trong một ngày gần nhất với giá trị nào sau đây?",
o=["0,53 kg.", "1,05 kg.", "2,64 kg.", "13,2 kg."],
a="C",
sol="Bước 1 – công suất toả ra trong lò (công suất nhiệt hạt nhân):\n"
    "  P_hn = P_điện/H = 500/0,20 = 2500 MW = 2,5·10⁹ W.\n"
    "Bước 2 – năng lượng hạt nhân cần trong một ngày:\n"
    "  E = P_hn·t = 2,5·10⁹ · 86 400 = 2,16·10¹⁴ J.\n"
    "Bước 3 – số phân hạch (mỗi phân hạch cho 200·1,6·10⁻¹³ = 3,2·10⁻¹¹ J):\n"
    "  N = 2,16·10¹⁴/3,2·10⁻¹¹ = 6,75·10²⁴.\n"
    "Bước 4 – khối lượng:\n"
    "  m = (N/N_A)·A = (6,75·10²⁴/6,02·10²³)·235 ≈ 11,21·235 ≈ 2635 g ≈ 2,64 kg.\n"
    "Bẫy: quên chia cho hiệu suất, tức là dùng ngay 500 MW, cho ra 0,53 kg — nhỏ hơn 5 lần."),

dict(
tag="Định luật Lenz – bối cảnh quen thuộc, bẫy tinh vi",
q="Thả một nam châm rơi thẳng đứng qua một vòng dây kim loại kín đặt nằm ngang. Bỏ qua sức cản không khí. "
  "Phát biểu nào sau đây đúng?",
fig="b2_nam_cham_roi",
cap="Nam châm rơi qua vòng dây kín: lực từ luôn cản trở chuyển động tương đối",
o=["Nam châm rơi tự do với gia tốc g, vì lực từ luôn vuông góc với vận tốc nên không ảnh hưởng đến "
   "chuyển động.",
   "Khi nam châm lại gần, vòng dây đẩy nam châm ra; khi nam châm ra xa, vòng dây kéo nam châm lại; cả hai "
   "trường hợp đều cản trở chuyển động nên gia tốc của nam châm nhỏ hơn g.",
   "Dòng điện cảm ứng đổi chiều khi nam châm đi qua tâm vòng dây, do đó lực từ luôn hướng xuống dưới và "
   "nam châm rơi nhanh hơn.",
   "Nếu vòng dây bị cắt đứt tại một điểm thì trong vòng dây vẫn có dòng điện cảm ứng nhưng nhỏ hơn."],
a="B",
sol="Định luật Lenz: dòng điện cảm ứng có chiều sao cho từ trường của nó CHỐNG LẠI nguyên nhân sinh ra nó, "
    "tức là chống lại sự biến thiên từ thông, tức là chống lại chuyển động tương đối.\n"
    "• Giai đoạn nam châm lại gần: từ thông qua vòng tăng ⟹ dòng cảm ứng sinh từ trường ngược chiều ⟹ vòng "
    "dây và nam châm ĐẨY nhau, lực tác dụng lên nam châm hướng lên.\n"
    "• Giai đoạn nam châm ra xa: từ thông giảm ⟹ vòng dây và nam châm HÚT nhau, lực tác dụng lên nam châm "
    "cũng hướng lên (níu nam châm lại).\n"
    "Cả hai giai đoạn lực từ đều hướng lên nên gia tốc của nam châm nhỏ hơn g.\n"
    "Phương án về vòng dây bị cắt đứt sai vì mạch hở thì không có dòng điện cảm ứng (chỉ còn suất điện động "
    "cảm ứng), do đó cũng không có lực cản. Phương án “lực từ luôn hướng xuống” mâu thuẫn với định luật "
    "Lenz — nếu đúng thì nam châm sẽ tự tăng tốc mãi, vi phạm định luật bảo toàn năng lượng."),

dict(
tag="Máy biến áp – điều kiện áp dụng công thức",
q="Một máy biến áp lí tưởng có cuộn sơ cấp N₁ = 1000 vòng và cuộn thứ cấp N₂ = 200 vòng. Đặt vào hai đầu "
  "cuộn sơ cấp một điện áp xoay chiều có giá trị hiệu dụng 220 V. Nhận định nào sau đây CHẮC CHẮN đúng?",
fig="b2_may_bien_ap",
cap="Máy biến áp với cuộn sơ cấp và cuộn thứ cấp",
o=["Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng 44 V, kể cả khi đặt vào cuộn sơ cấp một điện áp KHÔNG "
   "ĐỔI 220 V.",
   "Khi mạch thứ cấp để hở thì điện áp hiệu dụng ở hai đầu thứ cấp là 44 V và cường độ dòng điện hiệu dụng "
   "trong cuộn sơ cấp bằng 0.",
   "Cường độ dòng điện hiệu dụng trong cuộn sơ cấp luôn bằng 1/5 cường độ dòng điện hiệu dụng trong cuộn "
   "thứ cấp, kể cả khi mạch thứ cấp để hở.",
   "Đây là máy tăng áp, vì cuộn sơ cấp có nhiều vòng dây hơn cuộn thứ cấp."],
a="B",
sol="Máy biến áp chỉ hoạt động với dòng điện XOAY CHIỀU: phải có từ thông biến thiên trong lõi thép thì mới "
    "có suất điện động cảm ứng ở cuộn thứ cấp. Với điện áp không đổi, dòng sơ cấp không đổi, từ thông không "
    "đổi, cuộn thứ cấp không có điện áp — nên phương án nhắc tới “điện áp không đổi 220 V” sai.\n"
    "Tỉ số điện áp: U₂ = U₁·N₂/N₁ = 220·200/1000 = 44 V. Vì N₁ > N₂ nên đây là máy HẠ áp, không phải tăng áp.\n"
    "Khi mạch thứ cấp để hở: I₂ = 0. Với máy lí tưởng (không tổn hao, không dòng từ hoá), công suất vào "
    "bằng công suất ra, U₁I₁ = U₂I₂ = 0 ⟹ I₁ = 0. Đồng thời U₂ vẫn bằng 44 V vì tỉ số vòng dây không đổi.\n"
    "Hệ thức I₁/I₂ = N₂/N₁ = 1/5 chỉ đúng khi thứ cấp CÓ TẢI; khi để hở thì cả hai dòng đều bằng 0 và tỉ số "
    "đó vô nghĩa, nên phương án “kể cả khi để hở” sai."),

dict(
tag="Chuỗi phóng xạ – bảo toàn và tỉ số khối lượng",
q="Hạt nhân ²³⁸₉₂U qua một chuỗi phân rã α và β⁻ liên tiếp biến thành hạt nhân bền ²⁰⁶₈₂Pb; tổng số hạt α "
  "và β⁻ phát ra trong cả chuỗi là 14. Giả sử các hạt nhân trung gian đều có chu kì bán rã rất nhỏ so với "
  "chu kì bán rã của ²³⁸U. Một mẫu ban đầu chỉ chứa ²³⁸U nguyên chất; sau thời gian đúng bằng một chu kì "
  "bán rã của ²³⁸U, tỉ số giữa khối lượng ²⁰⁶Pb và khối lượng ²³⁸U còn lại trong mẫu bằng",
o=["0,433.", "0,866.", "1,000.", "1,155."],
a="B",
sol="Kiểm tra dữ kiện (một bước tự kiểm tra rất đáng làm): ΔA = 238 − 206 = 32 ⟹ số hạt α là 32/4 = 8. "
    "Điện tích: 92 − 8·2 = 76, cần đạt 82 nên số hạt β⁻ là 82 − 76 = 6. Tổng 8 + 6 = 14 ✓ đúng với đề.\n"
    "Vì các hạt nhân trung gian phân rã rất nhanh, cứ một hạt ²³⁸U phân rã thì tạo ra đúng một hạt ²⁰⁶Pb.\n"
    "Sau một chu kì bán rã: số hạt U còn lại N = N₀/2, số hạt Pb tạo thành N_Pb = N₀ − N = N₀/2.\n"
    "  N_Pb/N_U = 1.\n"
    "Đổi sang khối lượng (m = N·A/N_A):\n"
    "  m_Pb/m_U = (N_Pb·206)/(N_U·238) = 206/238 ≈ 0,866.\n"
    "Bẫy: dừng ở tỉ số SỐ HẠT bằng 1,000 mà quên rằng đề hỏi tỉ số KHỐI LƯỢNG; hoặc lật ngược tỉ số số "
    "khối (238/206 ≈ 1,155)."),

dict(
tag="Đọc đồ thị năng lượng liên kết riêng",
q="Hình dưới đây là đồ thị năng lượng liên kết riêng ε theo số khối A của các hạt nhân. Dựa vào đồ thị, phản "
  "ứng nào sau đây TOẢ năng lượng?",
fig="b2_nllk_rieng",
cap="Năng lượng liên kết riêng theo số khối; đỉnh đường cong ở vùng A ≈ 56",
o=["Tách một hạt nhân ⁵⁶₂₆Fe thành hai hạt nhân nhẹ hơn.",
   "Tổng hợp hai hạt nhân ²⁰⁸₈₂Pb thành một hạt nhân nặng hơn.",
   "Tổng hợp hai hạt nhân ²₁H thành một hạt nhân ⁴₂He.",
   "Tách một hạt nhân ⁴₂He thành hai hạt nhân ²₁H."],
a="C",
sol="Nguyên tắc đọc đồ thị: một phản ứng toả năng lượng khi các hạt nhân SAU phản ứng có năng lượng liên "
    "kết riêng LỚN HƠN các hạt nhân trước phản ứng, tức là dịch chuyển về phía đỉnh của đường cong "
    "(vùng A ≈ 56).\n"
    "• Tổng hợp hai ²₁H (ε ≈ 1,11) thành ⁴₂He (ε ≈ 7,07): ε tăng mạnh ⟹ TOẢ năng lượng "
    "(ΔE = 28,28 − 2·2,22 ≈ 23,8 MeV). Đây chính là phương án đúng.\n"
    "• Tách ⁵⁶Fe: sắt nằm đúng ở ĐỈNH đường cong, mọi hạt nhân tạo thành đều có ε nhỏ hơn ⟹ THU năng lượng. "
    "Đây là lí do vì sao sắt là “điểm kết thúc” của chuỗi phản ứng hạt nhân trong các ngôi sao.\n"
    "• Tổng hợp hai ²⁰⁸Pb thành hạt nhân nặng hơn: đi xa khỏi đỉnh về phía phải ⟹ THU năng lượng.\n"
    "• Tách ⁴He thành hai ²H là phản ứng NGƯỢC của phương án đúng ⟹ THU năng lượng."),

dict(
tag="Độ phóng xạ – tính số hạt đã phân rã",
q="Một mẫu chất phóng xạ có chu kì bán rã T = 15 giờ. Tại thời điểm t₁ độ phóng xạ của mẫu là "
  "H₁ = 4,0·10¹⁰ Bq. Số hạt nhân đã phân rã trong khoảng thời gian từ t₁ đến thời điểm t₂ = t₁ + 30 giờ "
  "gần nhất với giá trị nào sau đây?",
o=["7,79·10¹⁴.", "2,34·10¹⁵.", "3,12·10¹⁵.", "4,67·10¹⁵."],
a="B",
sol="Bước 1 – hằng số phóng xạ:\n"
    "  λ = ln2/T = 0,693/(15·3600) = 0,693/54 000 ≈ 1,284·10⁻⁵ s⁻¹.\n"
    "Bước 2 – số hạt nhân tại t₁, dùng H = λN:\n"
    "  N₁ = H₁/λ = 4,0·10¹⁰/1,284·10⁻⁵ ≈ 3,12·10¹⁵.\n"
    "Bước 3 – khoảng thời gian 30 giờ = 2T nên số hạt nhân còn lại giảm 4 lần:\n"
    "  N₂ = N₁/4 ≈ 7,79·10¹⁴.\n"
    "Bước 4 – số hạt đã phân rã:\n"
    "  ΔN = N₁ − N₂ = N₁(1 − 1/4) = 0,75·3,12·10¹⁵ ≈ 2,34·10¹⁵.\n"
    "Bẫy: nhầm ΔN với N₁ (3,12·10¹⁵) hoặc với N₂ (7,79·10¹⁴); cũng dễ quên đổi 15 giờ ra giây khi tính λ."),

dict(
tag="Kết hợp chương III và IV – nhà máy điện hạt nhân",
q="Một nhà máy điện hạt nhân phát ra công suất điện 600 MW ở điện áp hiệu dụng 20 kV. Điện áp này được "
  "nâng lên 500 kV nhờ một máy biến áp lí tưởng rồi truyền đi trên đường dây có điện trở tổng cộng 10 Ω. "
  "Coi hệ số công suất của mạch bằng 1. Công suất hao phí trên đường dây chiếm bao nhiêu phần trăm công "
  "suất truyền đi?",
fig="b2_truyen_tai",
cap="Sơ đồ từ lò phản ứng tới nơi tiêu thụ",
o=["0,24%.", "2,40%.", "4,80%.", "24,0%."],
a="B",
sol="Trên đường dây, cường độ dòng điện hiệu dụng được xác định bởi điện áp TRUYỀN TẢI (sau máy tăng áp), "
    "chứ không phải điện áp của máy phát:\n"
    "  I = P/U = 600·10⁶/(500·10³) = 1200 A.\n"
    "Công suất hao phí do toả nhiệt trên điện trở đường dây:\n"
    "  ΔP = I²R = 1200²·10 = 1,44·10⁷ W = 14,4 MW.\n"
    "Tỉ lệ hao phí: ΔP/P = 14,4/600 = 0,024 = 2,40%.\n"
    "Có thể viết gọn ΔP = P²R/U² — công thức này cho thấy hao phí tỉ lệ NGHỊCH với BÌNH PHƯƠNG điện áp "
    "truyền tải, đó là lí do phải dùng máy tăng áp. Nếu truyền ở 20 kV thì hao phí sẽ lớn gấp "
    "(500/20)² = 625 lần — hoàn toàn không thể thực hiện được."),

dict(
tag="Khung dây đi vào rồi ra khỏi vùng từ trường",
q="Một khung dây dẫn hình vuông cạnh a = 20 cm, điện trở R = 0,5 Ω, chuyển động thẳng đều theo phương "
  "ngang với tốc độ v = 2 m/s, đi vào rồi đi hẳn ra khỏi một vùng từ trường đều B = 0,4 T có bề rộng "
  "d = 50 cm. Vectơ cảm ứng từ vuông góc với mặt phẳng khung. Nhiệt lượng toả ra trên khung trong toàn bộ "
  "quá trình đó bằng",
fig="b2_khung_vao_tu_truong",
cap="Khung dây vuông đi vào rồi ra khỏi vùng từ trường có bề rộng d",
o=["5,12·10⁻³ J.", "1,02·10⁻² J.", "2,05·10⁻² J.", "2,56·10⁻² J."],
a="B",
sol="Quá trình gồm ba chặng, và chặng ở giữa là điểm mấu chốt.\n"
    "• Chặng 1 – khung ĐI VÀO (từ lúc cạnh trước chạm biên đến lúc cạnh sau vào hẳn): chỉ có một cạnh nằm "
    "trong từ trường, từ thông tăng.\n"
    "  e = B·a·v = 0,4·0,2·2 = 0,16 V; I = e/R = 0,32 A; P = I²R = 0,32²·0,5 = 0,0512 W.\n"
    "  Thời gian: t = a/v = 0,2/2 = 0,1 s ⟹ Q₁ = 0,0512·0,1 = 5,12·10⁻³ J.\n"
    "• Chặng 2 – khung NẰM TRỌN trong vùng từ trường (được, vì d = 50 cm > a = 20 cm): từ thông qua khung "
    "không đổi ⟹ không có dòng điện cảm ứng ⟹ không toả nhiệt.\n"
    "• Chặng 3 – khung ĐI RA: hoàn toàn đối xứng với chặng 1 ⟹ Q₃ = 5,12·10⁻³ J.\n"
    "Tổng: Q = 2·5,12·10⁻³ = 1,024·10⁻² J ≈ 1,02·10⁻² J.\n"
    "Bẫy: chỉ tính một lần vào (5,12·10⁻³ J), hoặc tính nhiệt trong suốt cả quãng đường 0,5 + 0,2 m như "
    "thể lúc nào cũng có dòng điện."),
]


# =====================================================================
# PHẦN II – TRẮC NGHIỆM ĐÚNG/SAI
# =====================================================================
P2 = [

dict(
tag="Thanh trượt trên mặt phẳng nghiêng – từ đầu đến trạng thái dừng",
stem="Thanh kim loại MN khối lượng m = 20 g, chiều dài phần giữa hai ray ℓ = 0,5 m, trượt KHÔNG MA SÁT trên "
     "hai ray song song đặt trên mặt phẳng nghiêng góc 30°. Tổng điện trở của mạch là R = 0,2 Ω. Từ trường "
     "đều B = 0,4 T vuông góc với mặt phẳng nghiêng. Thanh được thả nhẹ từ trạng thái nghỉ; g = 10 m/s².",
fig="b2_ray_nghieng",
cap="Thanh dẫn trượt trên hai ray đặt trên mặt phẳng nghiêng",
items=[
 ("Ngay tại thời điểm được thả, gia tốc của thanh bằng 5 m/s².", True,
  "Đúng. Tại thời điểm thả, v = 0 nên e = Bℓv = 0, không có dòng điện, không có lực từ. Thanh chỉ chịu "
  "thành phần trọng lực dọc mặt nghiêng: a = g·sin30° = 10·0,5 = 5 m/s²."),
 ("Tốc độ lớn nhất mà thanh đạt được là 0,5 m/s.", True,
  "Đúng. Ở tốc độ lớn nhất, gia tốc bằng 0: mg·sinα = B²ℓ²v/R "
  "⟹ v = mgR·sinα/(B²ℓ²) = (0,02·10·0,2·0,5)/(0,16·0,25) = 0,5 m/s."),
 ("Khi thanh đã đạt tốc độ lớn nhất, công suất toả nhiệt trên toàn mạch bằng 0,10 W.", False,
  "Sai; giá trị đúng là 0,05 W, kiểm tra được bằng hai cách. Cách 1: e = Bℓv = 0,4·0,5·0,5 = 0,1 V; "
  "I = e/R = 0,5 A; P = I²R = 0,25·0,2 = 0,05 W. Cách 2 (bảo toàn năng lượng): khi chuyển động đều, toàn "
  "bộ công suất của trọng lực chuyển thành nhiệt: P = mgv·sinα = 0,02·10·0,5·0,5 = 0,05 W.\n"
  "Con số 0,10 W ứng với sai lầm dùng cả trọng lượng mg thay vì thành phần mg·sinα dọc mặt nghiêng."),
 ("Nếu tăng điện trở của mạch lên gấp đôi thì tốc độ lớn nhất của thanh giảm đi một nửa.", False,
  "Sai — ngược hẳn lại. Từ v_max = mgR·sinα/(B²ℓ²), tốc độ lớn nhất TỈ LỆ THUẬN với R. Tăng R gấp đôi thì "
  "v_max tăng gấp đôi (1,0 m/s). Về mặt vật lí: R lớn hơn thì dòng cảm ứng nhỏ hơn, lực hãm nhỏ hơn, nên "
  "thanh phải chạy nhanh hơn mới sinh đủ lực hãm để cân bằng trọng lực."),
]),

dict(
tag="Đồ thị Φ(t) và định luật Lenz",
stem="Đồ thị hình dưới đây biểu diễn từ thông qua MỖI VÒNG dây của một khung dây phẳng theo thời gian, gồm bốn "
     "giai đoạn (I): 0–2 s, (II): 2–5 s, (III): 5–6 s, (IV): 6–9 s.",
fig="b2_do_thi_phi_t",
cap="Từ thông qua mỗi vòng dây theo thời gian",
items=[
 ("Trong giai đoạn (II) không có dòng điện cảm ứng trong khung.", True,
  "Đúng. Trong giai đoạn (II) từ thông giữ nguyên giá trị 0,4 Wb, tức ΔΦ/Δt = 0 nên e = 0 và không có "
  "dòng điện cảm ứng. Lưu ý: từ thông LỚN không sinh ra dòng cảm ứng; chỉ có từ thông BIẾN THIÊN mới sinh."),
 ("Suất điện động cảm ứng trong mỗi vòng dây có độ lớn lớn nhất bằng 0,60 V.", False,
  "Sai. Giá trị 0,60 Wb là độ biến thiên từ thông của giai đoạn (IV), không phải suất điện động. "
  "|e| = |ΔΦ/Δt|: giai đoạn (I) cho 0,4/2 = 0,20 V; (III) cho 0,4/1 = 0,40 V; (IV) cho 0,6/3 = 0,20 V. "
  "Giá trị lớn nhất là 0,40 V ở giai đoạn (III)."),
 ("Dòng điện cảm ứng trong khung ở giai đoạn (I) và ở giai đoạn (IV) có chiều ngược nhau.", True,
  "Đúng. Trong giai đoạn (I), Φ tăng (hệ số góc dương). Trong giai đoạn (IV), Φ giảm từ 0 xuống −0,6 Wb "
  "(hệ số góc âm). Vì e = −ΔΦ/Δt nên hai giai đoạn có suất điện động trái dấu, dòng điện cảm ứng chạy "
  "theo hai chiều ngược nhau."),
 ("Nếu khung có 20 vòng dây và điện trở 2 Ω thì trong giai đoạn (III) cường độ dòng điện cảm ứng bằng 0,2 A.", False,
  "Sai. Đồ thị cho từ thông qua MỖI vòng, nên suất điện động của cả khung phải nhân với số vòng: "
  "e = N·|ΔΦ/Δt| = 20·0,40 = 8 V ⟹ I = e/R = 8/2 = 4 A.\n"
  "Con số 0,2 A ứng với sai lầm quên nhân với N (lấy e = 0,4 V rồi chia cho 2 Ω)."),
]),

dict(
tag="Kết hợp chương III và IV – truyền tải điện năng",
stem="Một nhà máy điện hạt nhân phát công suất điện 600 MW ở điện áp hiệu dụng 20 kV; điện áp được nâng lên "
     "500 kV bằng máy biến áp lí tưởng rồi truyền đi trên đường dây có điện trở tổng cộng 10 Ω. Hệ số công "
     "suất bằng 1.",
fig="b2_truyen_tai",
cap="Sơ đồ truyền tải điện năng từ nhà máy tới khu dân cư",
items=[
 ("Tỉ số giữa số vòng dây cuộn thứ cấp và cuộn sơ cấp của máy tăng áp bằng 0,04.", False,
  "Sai vì đã lập tỉ số ngược. Với máy biến áp lí tưởng, N₂/N₁ = U₂/U₁ = 500/20 = 25 (giá trị 0,04 = 1/25 "
  "là tỉ số N₁/N₂). Máy TĂNG áp luôn có cuộn thứ cấp nhiều vòng hơn cuộn sơ cấp."),
 ("Cường độ dòng điện hiệu dụng trên đường dây truyền tải là 1200 A.", True,
  "Đúng. I = P/U = 600·10⁶/(500·10³) = 1200 A. Chú ý phải dùng điện áp truyền tải 500 kV, không phải "
  "20 kV của máy phát."),
 ("Công suất hao phí trên đường dây là 14,4 MW.", True,
  "Đúng. ΔP = I²R = 1200²·10 = 1,44·10⁷ W = 14,4 MW, chiếm 2,4% công suất truyền đi."),
 ("Nếu truyền tải trực tiếp ở 20 kV (giữ nguyên công suất truyền đi) thì công suất hao phí sẽ tăng 25 lần.", False,
  "Sai. ΔP = P²R/U² tỉ lệ nghịch với BÌNH PHƯƠNG điện áp, nên khi điện áp giảm 25 lần thì hao phí tăng "
  "25² = 625 lần. Khi đó ΔP = 625·14,4 MW = 9000 MW, lớn hơn cả công suất truyền đi — điều này chứng tỏ "
  "việc truyền tải ở 20 kV là bất khả thi, đúng như thực tế."),
]),

dict(
tag="Máy phát điện xoay chiều – phân biệt các đại lượng",
stem="Một khung dây phẳng gồm 200 vòng, diện tích mỗi vòng 100 cm², quay đều với tốc độ 300 vòng/phút "
     "quanh một trục nằm trong mặt phẳng khung và vuông góc với từ trường đều B = 0,2 T.",
fig="b2_khung_quay",
cap="Khung dây quay đều trong từ trường đều",
items=[
 ("Nếu tăng tốc độ quay lên gấp đôi thì từ thông cực đại qua khung cũng tăng gấp đôi.", False,
  "Sai. Từ thông cực đại Φ₀ = N·B·S chỉ phụ thuộc số vòng, cảm ứng từ và diện tích khung — hoàn toàn "
  "không phụ thuộc tốc độ quay. Cái tăng gấp đôi là SUẤT ĐIỆN ĐỘNG cực đại E₀ = ωΦ₀ (và cả tần số)."),
 ("Từ thông cực đại qua khung dây là 0,4 Wb.", True,
  "Đúng. Φ₀ = N·B·S = 200·0,2·100·10⁻⁴ = 200·0,2·0,01 = 0,4 Wb."),
 ("Tần số của suất điện động xoay chiều trong khung là 5 Hz.", True,
  "Đúng. Khung quay 300 vòng/phút = 5 vòng/giây; mỗi vòng quay tạo ra đúng một chu kì của suất điện động "
  "nên f = 5 Hz (ω = 2πf = 10π ≈ 31,4 rad/s)."),
 ("Suất điện động cực đại trong khung xấp xỉ 12,6 V.", True,
  "Đúng. E₀ = ω·Φ₀ = 10π·0,4 = 4π ≈ 12,57 V. Giá trị hiệu dụng tương ứng là "
  "E = E₀/√2 ≈ 8,9 V — hai đại lượng này rất hay bị nhầm lẫn."),
]),

dict(
tag="Phóng xạ α – từ khối lượng đến độ phóng xạ",
stem="Một mẫu ²¹⁰₈₄Po nguyên chất có khối lượng ban đầu m₀ = 1,00 g. Poloni phóng xạ α với chu kì bán rã "
     "T = 138 ngày, biến thành hạt nhân chì bền. Cho N_A = 6,02·10²³ mol⁻¹.",
fig="b2_so_do_phan_ra",
cap="Sơ đồ phân rã của ²¹⁰Po",
items=[
 ("Hạt nhân con tạo thành là ²⁰⁶₈₂Pb.", True,
  "Đúng. Áp dụng hai định luật bảo toàn cho phóng xạ α: bảo toàn số nuclôn 210 = 4 + A ⟹ A = 206; bảo toàn "
  "điện tích 84 = 2 + Z ⟹ Z = 82, tức nguyên tố chì. Vậy ²¹⁰₈₄Po → ⁴₂He + ²⁰⁶₈₂Pb."),
 ("Sau 276 ngày, trong mẫu còn 0,25 g Po và đã tạo thành 0,75 g Pb.", False,
  "Sai ở vế sau. 276 ngày = 2T nên khối lượng Po còn lại đúng bằng 1,00/4 = 0,25 g. Nhưng khối lượng chì "
  "KHÔNG bằng phần khối lượng Po đã mất, vì mỗi phân rã còn giải phóng một hạt α. Phải đi qua số hạt: "
  "số hạt Po đã phân rã là 0,75·N₀, mỗi hạt tạo một hạt Pb nên\n"
  "  m_Pb = 0,75·N₀·206/N_A = 0,75·(1,00/210)·206 ≈ 0,736 g.\n"
  "(Phần chênh lệch 0,014 g chính là khối lượng các hạt α đã bay ra.)"),
 ("Số hạt nhân Po có trong mẫu lúc ban đầu là 2,87·10²¹.", True,
  "Đúng. N₀ = (m₀/A)·N_A = (1,00/210)·6,02·10²³ ≈ 2,867·10²¹ hạt."),
 ("Độ phóng xạ ban đầu của mẫu vào khoảng 1,67·10¹⁴ Bq.", True,
  "Đúng. λ = ln2/T = 0,693/(138·86 400) ≈ 5,81·10⁻⁸ s⁻¹ (phải đổi chu kì bán rã ra GIÂY vì becquerel là "
  "số phân rã mỗi giây). H₀ = λN₀ = 5,81·10⁻⁸ · 2,867·10²¹ ≈ 1,67·10¹⁴ Bq."),
]),

dict(
tag="Phản ứng nhiệt hạch – độ hụt khối và năng lượng liên kết riêng",
stem="Xét phản ứng ²₁H + ²₁H → ³₂He + ¹₀n. Cho khối lượng các hạt nhân và hạt: m(²₁H) = 2,0136 u; "
     "m(³₂He) = 3,0149 u; m(n) = 1,00870 u; m(p) = 1,00728 u; 1 u = 931,5 MeV/c².",
items=[
 ("Tổng khối lượng các hạt sau phản ứng lớn hơn tổng khối lượng các hạt trước phản ứng.", False,
  "Sai, và chính điều ngược lại mới xảy ra. Trước: 2·2,0136 = 4,0272 u. Sau: 3,0149 + 1,00870 = 4,02360 u. "
  "Khối lượng đã GIẢM đi 0,0036 u; phần khối lượng hụt đó chuyển thành năng lượng toả ra."),
 ("Phản ứng toả năng lượng khoảng 3,35 MeV.", True,
  "Đúng. Δm = 4,0272 − 4,0236 = 0,0036 u ⟹ ΔE = Δm·c² = 0,0036·931,5 ≈ 3,35 MeV."),
 ("Đây là một phản ứng nhiệt hạch.", True,
  "Đúng. Hai hạt nhân rất nhẹ (đơteri) kết hợp lại thành một hạt nhân nặng hơn và toả năng lượng — đó là "
  "định nghĩa của phản ứng nhiệt hạch. Muốn xảy ra, phản ứng cần nhiệt độ cực cao để hai hạt nhân thắng "
  "được lực đẩy tĩnh điện giữa chúng."),
 ("Năng lượng liên kết riêng của ³₂He lớn hơn của ²₁H.", True,
  "Đúng. Với ²₁H: Δm = 1,00728 + 1,00870 − 2,0136 = 0,00238 u ⟹ W_lk ≈ 2,22 MeV ⟹ "
  "ε ≈ 2,22/2 = 1,11 MeV/nuclôn.\n"
  "Với ³₂He: Δm = 2·1,00728 + 1,00870 − 3,0149 = 0,00836 u ⟹ W_lk ≈ 7,79 MeV ⟹ "
  "ε ≈ 7,79/3 = 2,60 MeV/nuclôn.\n"
  "Việc ε tăng chính là nguyên nhân sâu xa khiến phản ứng toả năng lượng."),
]),

dict(
tag="Thực nghiệm – cân dòng điện đo cảm ứng từ",
stem="Để đo cảm ứng từ giữa hai cực của một nam châm chữ U, người ta đặt nam châm lên đĩa cân điện tử và "
     "giữ cố định một đoạn dây dẫn thẳng dài ℓ = 5 cm nằm ngang trong khe từ, vuông góc với các đường sức. "
     "Cho dòng điện I chạy qua đoạn dây và ghi lại phần số chỉ TĂNG THÊM Δm của cân. Lấy g = 10 m/s².",
fig="b2_can_dong_dien",
cap="Bộ thí nghiệm “cân dòng điện”",
tbl=("Số liệu đo được",
     ["I (A)", "1,0", "2,0", "3,0", "4,0", "5,0"],
     [["Δm (g)", "1,0", "2,0", "3,0", "4,0", "5,0"]]),
items=[
 ("Đồ thị biểu diễn lực từ theo cường độ dòng điện là một đường thẳng đi qua gốc toạ độ.", True,
  "Đúng. F = Δm·g, mà bảng cho thấy Δm tỉ lệ thuận với I (tỉ số Δm/I = 1,0 g/A ở cả năm lần đo). Điều này "
  "phù hợp với công thức F = BIℓ: khi B và ℓ không đổi thì F tỉ lệ thuận với I, và khi I = 0 thì F = 0."),
 ("Nếu quay đoạn dây trong mặt phẳng ngang đi 30° so với vị trí ban đầu thì ứng với I = 4,0 A số chỉ tăng "
  "thêm của cân là 2,0 g.", False,
  "Sai. Ban đầu dây vuông góc với B (θ = 90°). Quay đi 30° thì góc giữa dây và B còn θ = 60°, nên "
  "F = BIℓ·sin60° = 0,866·F_cũ. Ứng với I = 4,0 A: Δm = 4,0·0,866 ≈ 3,5 g, chứ không phải 2,0 g. "
  "(Giá trị 2,0 g ứng với sai lầm dùng cos60° = 0,5.)"),
 ("Cảm ứng từ trong khe nam châm bằng 0,2 T.", True,
  "Đúng. Lấy một điểm bất kì, chẳng hạn I = 5,0 A: F = Δm·g = 5,0·10⁻³·10 = 0,05 N.\n"
  "  B = F/(I·ℓ) = 0,05/(5,0·0,05) = 0,2 T. Dùng các điểm khác đều cho cùng kết quả."),
 ("Nếu đảo chiều dòng điện thì số chỉ của cân giảm đi so với khi không có dòng điện, và độ giảm đúng bằng "
  "độ tăng trước đó.", True,
  "Đúng. Lực từ tác dụng lên đoạn dây đổi chiều, nên theo định luật III Newton, phản lực mà dây tác dụng "
  "lên nam châm cũng đổi chiều: cân bị “nhấc bớt” đúng một lượng bằng lượng nó bị “đè thêm” trước đó. Độ "
  "lớn không đổi vì F = BIℓ không phụ thuộc chiều dòng điện."),
]),

dict(
tag="Phóng xạ và an toàn bức xạ",
stem="Xét các tính chất của các tia phóng xạ và ứng dụng của chúng.",
items=[
 ("Chu kì bán rã của một chất phóng xạ giảm đi khi tăng nhiệt độ hoặc tăng áp suất tác dụng lên mẫu.", False,
  "Sai. Phóng xạ là quá trình biến đổi tự phát của HẠT NHÂN, hoàn toàn không phụ thuộc các tác động bên "
  "ngoài thông thường như nhiệt độ, áp suất hay trạng thái liên kết hoá học của nguyên tử. Chính tính chất "
  "này làm cho các “đồng hồ phóng xạ” như ¹⁴C hay ²³⁸U trở nên đáng tin cậy trong định tuổi."),
 ("Tia α bị chặn lại bởi một tờ giấy, nhưng nguồn phát tia α lại rất nguy hiểm nếu lọt vào bên trong "
  "cơ thể.", True,
  "Đúng, và đây là một nghịch lí quan trọng về an toàn bức xạ. Tia α có khả năng đâm xuyên rất kém nhưng "
  "khả năng ion hoá rất mạnh: khi ở ngoài cơ thể nó không qua nổi lớp da chết, còn khi ở bên trong thì "
  "toàn bộ năng lượng của nó được giải phóng ngay trong mô sống trên một quãng đường rất ngắn."),
 ("Tia γ có bản chất là sóng điện từ, không mang điện nên không bị lệch trong từ trường.", True,
  "Đúng. Tia γ là sóng điện từ có bước sóng rất ngắn, không mang điện tích nên từ trường không tác dụng "
  "lực lên nó. Ngược lại, tia α (mang điện dương) và tia β (mang điện âm hoặc dương) đều bị lệch trong từ "
  "trường, và lệch theo hai chiều ngược nhau."),
 ("Trong chẩn đoán y học, người ta ưu tiên các đồng vị phóng xạ có chu kì bán rã ngắn.", True,
  "Đúng. Chu kì bán rã ngắn (thường vài giờ tới vài ngày) cho phép thu được tín hiệu đủ mạnh với lượng "
  "chất rất nhỏ, đồng thời hoạt độ trong cơ thể bệnh nhân giảm nhanh sau khi chụp, giảm liều chiếu không "
  "cần thiết."),
]),

dict(
tag="Kết hợp chương III và IV – lò phản ứng nhiệt hạch",
stem="Trong lò phản ứng nhiệt hạch kiểu tokamak, nhiên liệu ở trạng thái plasma (khí bị ion hoá mạnh, gồm "
     "các hạt nhân và electron chuyển động tự do) có nhiệt độ hàng trăm triệu độ, được giữ không cho chạm "
     "vào thành lò bằng một từ trường rất mạnh. Cho biết mỗi phản ứng ²₁H + ³₁H → ⁴₂He + ¹₀n toả 17,6 MeV, "
     "còn mỗi phân hạch ²³⁵U (hấp thụ một nơtron) toả khoảng 200 MeV.",
fig="b2_tokamak",
cap="Nguyên tắc giam giữ plasma bằng từ trường trong lò tokamak",
items=[
 ("Từ trường có thể giam giữ được plasma vì plasma gồm các hạt mang điện đang chuyển động, do đó chịu tác "
  "dụng của lực từ.", True,
  "Đúng. Từ trường tác dụng lực lên các điện tích chuyển động (biểu hiện quen thuộc là lực từ lên dòng "
  "điện — thực chất cũng là lực lên các hạt mang điện chuyển động trong dây dẫn). Nhờ đó các hạt plasma bị "
  "“uốn” quỹ đạo và không thể bay thẳng tới thành lò, tránh được việc làm hỏng thành lò và làm nguội plasma."),
 ("Phản ứng nhiệt hạch cần nhiệt độ rất cao để các hạt nhân có đủ động năng thắng lực đẩy tĩnh điện và "
  "tiến lại đủ gần nhau.", True,
  "Đúng. Hai hạt nhân đều mang điện dương nên đẩy nhau rất mạnh khi lại gần. Chỉ khi động năng chuyển động "
  "nhiệt đủ lớn (tương ứng nhiệt độ hàng trăm triệu độ) chúng mới tới được khoảng cách đủ nhỏ để lực hạt "
  "nhân mạnh phát huy tác dụng."),
 ("Mỗi phản ứng nhiệt hạch toả ra năng lượng lớn hơn mỗi phản ứng phân hạch.", False,
  "Sai. Tính trên MỖI PHẢN ỨNG thì phân hạch toả nhiều hơn hẳn: 200 MeV so với 17,6 MeV, tức gấp khoảng "
  "11 lần. Phát biểu này thường bị nhầm vì người ta hay nghe nói “nhiệt hạch mạnh hơn phân hạch” — điều đó "
  "chỉ đúng khi so sánh theo mỗi nuclôn hoặc theo mỗi kilôgam nhiên liệu."),
 ("Tính trên mỗi nuclôn tham gia, phản ứng nhiệt hạch nói trên toả năng lượng lớn hơn phân hạch ²³⁵U.", True,
  "Đúng, và đây mới là cách so sánh đúng đắn.\n"
  "  Nhiệt hạch: 17,6 MeV cho 2 + 3 = 5 nuclôn ⟹ 3,52 MeV/nuclôn.\n"
  "  Phân hạch: 200 MeV cho 235 + 1 = 236 nuclôn ⟹ ≈ 0,85 MeV/nuclôn.\n"
  "Tỉ số khoảng 4 lần — đó là lí do nhiệt hạch được coi là nguồn năng lượng của tương lai."),
]),

dict(
tag="Bảng số liệu phóng xạ – xử lí bằng đồ thị",
stem="Đo độ phóng xạ H của một mẫu chất phóng xạ theo thời gian, người ta thu được bảng số liệu dưới đây.",
fig="b2_do_thi_H_t",
cap="Độ phóng xạ theo thời gian (trái) và đồ thị lnH theo thời gian (phải)",
tbl=("Kết quả đo độ phóng xạ",
     ["t (giờ)", "0", "2", "4", "6", "8"],
     [["H (kBq)", "800", "566", "400", "283", "200"]]),
items=[
 ("Chu kì bán rã của chất phóng xạ này là 4 giờ.", True,
  "Đúng. Đọc trực tiếp từ bảng: H giảm từ 800 kBq xuống 400 kBq sau 4 giờ, rồi từ 400 kBq xuống 200 kBq "
  "sau 4 giờ nữa. (Kiểm tra thêm: cứ mỗi 2 giờ H lại nhân với 566/800 ≈ 0,707 ≈ 1/√2, đúng bằng hệ số của "
  "nửa chu kì bán rã.)"),
 ("Đồ thị lnH theo t là một đường thẳng có hệ số góc bằng −λ.", True,
  "Đúng. Từ H = H₀·e^(−λt) lấy logarit tự nhiên hai vế: lnH = lnH₀ − λt — hàm bậc nhất của t với hệ số góc "
  "−λ. Đây là kĩ thuật chuẩn để xác định λ (và T = ln2/λ) từ số liệu thực nghiệm có sai số, vì hồi quy "
  "tuyến tính dùng được toàn bộ các điểm đo."),
 ("Sau 12 giờ kể từ lần đo đầu tiên, độ phóng xạ của mẫu còn khoảng 133 kBq.", False,
  "Sai. 12 giờ = 3 chu kì bán rã nên H = 800/2³ = 100 kBq. Giá trị 133 kBq ứng với sai lầm chia cho 6 "
  "(“ba lần chu kì thì chia cho 3·2”) thay vì chia cho 2³."),
 ("Trong 8 giờ đầu, số hạt nhân đã phân rã bằng 1/2 số hạt nhân ban đầu.", False,
  "Sai. 8 giờ = 2T nên số hạt nhân CÒN LẠI là N₀/4, do đó số hạt đã phân rã là N₀ − N₀/4 = (3/4)N₀ chứ "
  "không phải N₀/2. Có thể đọc trực tiếp từ bảng qua độ phóng xạ vì H tỉ lệ thuận với N: H giảm từ 800 "
  "xuống 200 kBq, tức chỉ còn 1/4. Giá trị 1/2 ứng với việc chỉ tính cho MỘT chu kì bán rã."),
]),
]


# =====================================================================
# PHẦN III – TRẮC NGHIỆM TRẢ LỜI NGẮN
# =====================================================================
P3 = [

dict(
tag="Cảm ứng điện từ – lực kéo không đổi",
q="Một thanh kim loại khối lượng 50 g trượt không ma sát trên hai ray nằm ngang cách nhau ℓ = 40 cm, đặt "
  "trong từ trường đều thẳng đứng B = 0,5 T. Tổng điện trở của mạch là R = 0,4 Ω. Kéo thanh bằng một lực "
  "không đổi F = 0,2 N theo phương ngang, dọc theo ray. Tốc độ lớn nhất mà thanh đạt được bằng bao nhiêu "
  "mét trên giây?",
fig="b2_ray_ngang",
cap="Thanh dẫn trên hai ray nằm ngang, kéo bằng lực không đổi",
ans="2",
sol="Khi thanh đạt tốc độ lớn nhất thì gia tốc bằng 0, lực kéo cân bằng với lực từ cản trở:\n"
    "  F = B·I·ℓ = B·(Bℓv/R)·ℓ = B²ℓ²v/R\n"
    "  v_max = F·R/(B²ℓ²) = (0,2·0,4)/(0,5²·0,4²) = 0,08/(0,25·0,16) = 0,08/0,04 = 2 m/s.\n"
    "Kiểm tra bằng năng lượng: ở v = 2 m/s, công suất của lực kéo là F·v = 0,4 W; e = Bℓv = 0,4 V, "
    "I = 1 A, công suất toả nhiệt I²R = 0,4 W ✓ — toàn bộ công của lực kéo chuyển thành nhiệt, đúng như "
    "khi thanh chuyển động đều."),

dict(
tag="Lực từ tác dụng lên khung dây chuyển động",
q="Một khung dây dẫn hình vuông cạnh a = 20 cm, điện trở R = 0,5 Ω, chuyển động thẳng đều với tốc độ "
  "v = 2 m/s đi vào một vùng từ trường đều B = 0,4 T vuông góc với mặt phẳng khung. Trong giai đoạn khung "
  "đang đi vào vùng từ trường, lực từ tác dụng lên khung có độ lớn bằng bao nhiêu (tính theo đơn vị "
  "10⁻² N, làm tròn đến chữ số thập phân thứ hai)?",
fig="b2_khung_vao_tu_truong",
cap="Khung dây đi vào vùng từ trường",
ans="2,56",
sol="Trong giai đoạn khung đang đi vào, chỉ có CẠNH TRƯỚC nằm trong từ trường, nên chỉ cạnh đó chịu lực từ:\n"
    "  e = B·a·v = 0,4·0,2·2 = 0,16 V\n"
    "  I = e/R = 0,16/0,5 = 0,32 A\n"
    "  F = B·I·a = 0,4·0,32·0,2 = 0,0256 N = 2,56·10⁻² N.\n"
    "Lực này ngược chiều chuyển động (định luật Lenz), nên muốn khung chuyển động ĐỀU thì phải có ngoại lực "
    "kéo đúng bằng 2,56·10⁻² N."),

dict(
tag="Máy biến áp – số vòng bị quấn ngược",
q="Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng. Khi đặt vào cuộn sơ cấp điện áp xoay chiều có giá "
  "trị hiệu dụng 220 V thì điện áp hiệu dụng ở hai đầu cuộn thứ cấp để hở là 22 V. Kiểm tra lại thì thấy "
  "người thợ đã quấn tổng cộng 120 vòng cho cuộn thứ cấp, trong đó có một số vòng bị quấn ngược chiều so "
  "với các vòng còn lại. Số vòng bị quấn ngược là bao nhiêu?",
fig="b2_may_bien_ap",
cap="Sơ đồ máy biến áp",
ans="10",
sol="Mỗi vòng dây quấn ngược sinh ra suất điện động ngược pha với các vòng quấn đúng, nên nó vừa TRIỆT TIÊU "
    "đóng góp của chính nó, vừa triệt tiêu đóng góp của một vòng quấn đúng. Nếu có x vòng bị quấn ngược "
    "trong tổng số 120 vòng thì số vòng “có hiệu lực” là\n"
    "  N₂(hiệu lực) = (120 − x) − x = 120 − 2x.\n"
    "Từ tỉ số điện áp:\n"
    "  N₂(hiệu lực)/N₁ = U₂/U₁ = 22/220 = 0,1 ⟹ N₂(hiệu lực) = 0,1·1000 = 100 vòng.\n"
    "  120 − 2x = 100 ⟹ x = 10 vòng.\n"
    "Bẫy: lấy thẳng 120 − 100 = 20 vòng, tức quên rằng mỗi vòng ngược “ăn mất” hai vòng."),

dict(
tag="Dòng xoay chiều – nhiệt lượng toả ra",
q="Cho dòng điện xoay chiều i = 4cos(100πt) (A, t tính bằng s) chạy qua một điện trở R = 25 Ω. Nhiệt lượng "
  "toả ra trên điện trở trong 5 phút bằng bao nhiêu kilôjun?",
ans="60",
sol="Nhiệt lượng toả ra trên điện trở phải tính bằng giá trị HIỆU DỤNG của cường độ dòng điện, chứ không "
    "phải giá trị cực đại:\n"
    "  I = I₀/√2 = 4/√2 = 2√2 A ⟹ I² = 8 A².\n"
    "  P = I²R = 8·25 = 200 W.\n"
    "  Q = P·t = 200·(5·60) = 60 000 J = 60 kJ.\n"
    "Bẫy: dùng I₀ = 4 A cho ra 120 kJ — gấp đôi kết quả đúng. Đây chính là ý nghĩa của giá trị hiệu dụng: "
    "nó là cường độ dòng điện không đổi gây ra CÙNG công suất toả nhiệt."),

dict(
tag="Suất điện động cảm ứng trung bình",
q="Một khung dây phẳng gồm 100 vòng, diện tích mỗi vòng 200 cm², đặt trong từ trường đều B = 0,05 T. Ban "
  "đầu mặt phẳng khung vuông góc với vectơ cảm ứng từ. Quay khung đi 60° quanh một trục nằm trong mặt phẳng "
  "khung trong thời gian 0,2 s. Suất điện động cảm ứng trung bình xuất hiện trong khung bằng bao nhiêu vôn?",
ans="0,25",
sol="Ban đầu mặt phẳng khung vuông góc với B nên PHÁP TUYẾN của khung song song với B, tức α₁ = 0:\n"
    "  Φ₁ = N·B·S·cos0° = 100·0,05·200·10⁻⁴ = 100·0,05·0,02 = 0,1 Wb.\n"
    "Quay khung 60° thì pháp tuyến cũng quay 60°, α₂ = 60°:\n"
    "  Φ₂ = 0,1·cos60° = 0,05 Wb.\n"
    "  |e| = |ΔΦ|/Δt = (0,1 − 0,05)/0,2 = 0,25 V.\n"
    "Chú ý: “quay khung 60°” là quay pháp tuyến 60°, không phải làm cho mặt phẳng khung hợp với B góc 60°."),

dict(
tag="Năng lượng liên kết riêng",
q="Hạt nhân ⁵⁶₂₆Fe có khối lượng hạt nhân là 55,9206 u. Cho m_p = 1,00728 u; m_n = 1,00866 u; "
  "1 u = 931,5 MeV/c². Năng lượng liên kết riêng của hạt nhân ⁵⁶₂₆Fe bằng bao nhiêu MeV/nuclôn (làm tròn "
  "đến chữ số thập phân thứ hai)?",
fig="b2_nllk_rieng",
cap="⁵⁶Fe nằm ở đỉnh đường cong năng lượng liên kết riêng",
ans="8,79",
sol="Hạt nhân ⁵⁶₂₆Fe gồm Z = 26 prôtôn và N = 56 − 26 = 30 nơtron.\n"
    "Độ hụt khối:\n"
    "  Δm = 26·m_p + 30·m_n − m_hn = 26·1,00728 + 30·1,00866 − 55,9206\n"
    "     = 26,18928 + 30,25980 − 55,9206 = 0,52848 u.\n"
    "Năng lượng liên kết:\n"
    "  W_lk = Δm·c² = 0,52848·931,5 ≈ 492,3 MeV.\n"
    "Năng lượng liên kết riêng:\n"
    "  ε = W_lk/A = 492,3/56 ≈ 8,79 MeV/nuclôn.\n"
    "Đây là giá trị lớn nhất trong tất cả các hạt nhân, phù hợp với vị trí đỉnh của ⁵⁶Fe trên đồ thị: sắt "
    "là hạt nhân bền vững nhất."),

dict(
tag="Phóng xạ – suy ra thời gian từ tỉ số khối lượng",
q="Một mẫu ²¹⁰₈₄Po ban đầu nguyên chất, phóng xạ α với chu kì bán rã 138 ngày và tạo thành ²⁰⁶₈₂Pb bền. "
  "Sau thời gian t, tỉ số giữa khối lượng chì tạo thành và khối lượng poloni còn lại trong mẫu bằng 0,25. "
  "Giá trị của t bằng bao nhiêu ngày (làm tròn đến chữ số thập phân thứ nhất)?",
fig="b2_so_do_phan_ra",
cap="Sơ đồ phân rã của ²¹⁰Po",
ans="45,2",
sol="Bước 1 – chuyển từ tỉ số khối lượng sang tỉ số SỐ HẠT (đây là bước hay bị bỏ qua):\n"
    "  m_Pb/m_Po = (N_Pb·206)/(N_Po·210) = 0,25 ⟹ N_Pb/N_Po = 0,25·210/206 ≈ 0,25485.\n"
    "Bước 2 – biểu diễn tỉ số số hạt theo thời gian. Với N_Po = N₀·2^(−t/T) và N_Pb = N₀ − N_Po:\n"
    "  N_Pb/N_Po = N₀/N_Po − 1 = 2^(t/T) − 1.\n"
    "Bước 3 – giải:\n"
    "  2^(t/T) = 1,25485 ⟹ t/T = log₂(1,25485) = ln(1,25485)/ln2 ≈ 0,2270/0,6931 ≈ 0,3275\n"
    "  t = 0,3275·138 ≈ 45,2 ngày.\n"
    "Bẫy: dùng thẳng tỉ số khối lượng 0,25 thay cho tỉ số số hạt sẽ cho t ≈ 44,4 ngày."),

dict(
tag="Phân hạch – từ khối lượng nhiên liệu ra công suất",
q="Một nhà máy điện hạt nhân dùng nhiên liệu ²³⁵U; mỗi phân hạch toả 200 MeV và hiệu suất chuyển hoá thành "
  "điện năng là 25%. Trong một năm (365 ngày) nhà máy tiêu thụ hết 1,00 tấn ²³⁵U. Cho "
  "N_A = 6,02·10²³ mol⁻¹, 1 MeV = 1,6·10⁻¹³ J. Công suất điện của nhà máy bằng bao nhiêu MW (làm tròn đến "
  "hàng đơn vị)?",
ans="650",
sol="Bước 1 – số hạt nhân ²³⁵U bị phân hạch trong một năm:\n"
    "  N = (m/A)·N_A = (1,00·10⁶ g / 235)·6,02·10²³ ≈ 4255,3·6,02·10²³ ≈ 2,562·10²⁷.\n"
    "Bước 2 – năng lượng hạt nhân toả ra:\n"
    "  E = N·200 MeV = 2,562·10²⁷ · 3,2·10⁻¹¹ ≈ 8,197·10¹⁶ J.\n"
    "Bước 3 – điện năng sản xuất được:\n"
    "  E_điện = 0,25·8,197·10¹⁶ ≈ 2,049·10¹⁶ J.\n"
    "Bước 4 – công suất điện (một năm có 365·86 400 = 3,1536·10⁷ s):\n"
    "  P = 2,049·10¹⁶/3,1536·10⁷ ≈ 6,50·10⁸ W = 650 MW."),

dict(
tag="Định tuổi bằng ¹⁴C",
q="Tỉ số ¹⁴C/¹²C trong một mẫu xương cổ bằng 1/3 tỉ số đó trong một mẫu xương mới. Chu kì bán rã của ¹⁴C "
  "là 5730 năm. Tuổi của mẫu xương cổ bằng bao nhiêu năm (làm tròn đến hàng trăm)?",
ans="9100",
sol="Lượng ¹²C trong mẫu không đổi theo thời gian, còn ¹⁴C giảm theo quy luật phóng xạ, nên tỉ số ¹⁴C/¹²C "
    "giảm đúng theo quy luật đó:\n"
    "  2^(−t/T) = 1/3 ⟹ 2^(t/T) = 3 ⟹ t/T = log₂3 = ln3/ln2 ≈ 1,5850.\n"
    "  t = 1,5850·5730 ≈ 9082 năm ≈ 9100 năm.\n"
    "Việc so sánh TỈ SỐ ¹⁴C/¹²C (thay vì độ phóng xạ tuyệt đối) giúp loại bỏ ảnh hưởng của khối lượng mẫu "
    "— hai mẫu không cần có cùng khối lượng."),

dict(
tag="Truyền tải – suy luận ngược từ hiệu suất",
q="Điện năng được truyền từ một nhà máy đến khu dân cư bằng đường dây tải điện với hiệu suất truyền tải "
  "90%. Nếu tăng điện áp truyền tải lên gấp 2 lần và giữ nguyên công suất truyền đi cũng như điện trở "
  "đường dây, thì hiệu suất truyền tải bằng bao nhiêu phần trăm?",
ans="97,5",
sol="Hiệu suất 90% nghĩa là công suất hao phí chiếm 10% công suất truyền đi:\n"
    "  ΔP₁ = 0,10·P.\n"
    "Công suất hao phí ΔP = P²R/(U²cos²φ) tỉ lệ nghịch với BÌNH PHƯƠNG điện áp truyền tải (P và R không "
    "đổi), nên khi U tăng 2 lần:\n"
    "  ΔP₂ = ΔP₁/2² = ΔP₁/4 = 0,025·P, tức 2,5%.\n"
    "Hiệu suất mới: H₂ = 100% − 2,5% = 97,5%.\n"
    "Bẫy: nghĩ rằng hiệu suất cũng tăng gấp đôi, hoặc hao phí chỉ giảm 2 lần (khi đó ra 95%)."),

dict(
tag="Bảo toàn động lượng trong phóng xạ",
q="Hạt nhân ²¹⁰₈₄Po đang ĐỨNG YÊN thì phóng xạ α và biến thành hạt nhân ²⁰⁶₈₂Pb. Năng lượng toả ra của "
  "phản ứng là 5,40 MeV và toàn bộ năng lượng này chuyển thành động năng của hai hạt sinh ra. Lấy khối "
  "lượng mỗi hạt nhân theo đơn vị u bằng số khối của nó. Động năng của hạt α bằng bao nhiêu MeV (làm tròn "
  "đến chữ số thập phân thứ hai)?",
fig="b2_so_do_phan_ra",
cap="Sơ đồ phân rã của ²¹⁰Po",
ans="5,30",
sol="Hạt nhân mẹ đứng yên nên tổng động lượng ban đầu bằng 0. Bảo toàn động lượng cho hai hạt sinh ra bay "
    "ngược chiều nhau với động lượng có cùng độ lớn:\n"
    "  p_α = p_Pb.\n"
    "Liên hệ giữa động năng và động lượng: K = p²/(2m) ⟹ p² = 2mK. Do đó\n"
    "  m_α·K_α = m_Pb·K_Pb ⟹ K_α/K_Pb = m_Pb/m_α = 206/4.\n"
    "Kết hợp với K_α + K_Pb = 5,40 MeV:\n"
    "  K_α = 5,40 · 206/(206 + 4) = 5,40·206/210 ≈ 5,30 MeV.\n"
    "Nhận xét: hạt nhẹ hơn nhận gần như toàn bộ năng lượng (98,1%); hạt chì giật lùi chỉ nhận 0,10 MeV."),

dict(
tag="Kết hợp – số phân hạch mỗi giây",
q="Một nhà máy điện hạt nhân có công suất điện 1000 MW; hiệu suất chuyển hoá năng lượng hạt nhân thành "
  "điện năng là 32%. Lò phản ứng dùng phân hạch ²³⁵U, mỗi phân hạch toả 200 MeV. Cho "
  "1 MeV = 1,6·10⁻¹³ J. Số phân hạch xảy ra trong lò mỗi giây bằng bao nhiêu (tính theo đơn vị 10¹⁹, làm "
  "tròn đến chữ số thập phân thứ hai)?",
ans="9,77",
sol="Bước 1 – công suất nhiệt hạt nhân của lò:\n"
    "  P_hn = P_điện/H = 1000/0,32 = 3125 MW = 3,125·10⁹ W.\n"
    "Bước 2 – năng lượng của một phân hạch:\n"
    "  E₁ = 200·1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
    "Bước 3 – số phân hạch mỗi giây:\n"
    "  n = P_hn/E₁ = 3,125·10⁹/3,2·10⁻¹¹ ≈ 9,77·10¹⁹ phân hạch mỗi giây.\n"
    "Để hình dung: lượng ²³⁵U tiêu thụ tương ứng là "
    "(9,77·10¹⁹/6,02·10²³)·235 ≈ 0,038 g mỗi giây, tức khoảng 3,3 kg mỗi ngày."),
]
