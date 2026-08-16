# -*- coding: utf-8 -*-
"""BỘ 1 – BÀI TẬP CỰC KHÓ: CHƯƠNG I (VẬT LÍ NHIỆT) VÀ CHƯƠNG II (KHÍ LÍ TƯỞNG).

Cấu trúc theo đúng ba phần của đề thi tốt nghiệp THPT từ 2025:
  P1 – trắc nghiệm nhiều phương án lựa chọn
  P2 – trắc nghiệm đúng/sai (mỗi câu 4 ý)
  P3 – trắc nghiệm trả lời ngắn

Khoá dữ liệu của mỗi câu:
  q/o/a/sol            câu nhiều phương án lựa chọn
  stem/items           câu đúng/sai, items = [(nội dung, Đúng?, giải thích) × 4]
  q/ans/sol            câu trả lời ngắn
  fig, cap, tbl, tag   hình vẽ, chú thích hình, bảng số liệu, nhãn kĩ năng
"""

# =====================================================================
# PHẦN I – TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN
# =====================================================================
P1 = [

dict(
tag="Đọc đồ thị – đại lượng nào xác định được",
q="Một mẫu chất rắn khối lượng m được nung bằng một thiết bị có công suất không đổi P. Bỏ qua hao phí "
  "nhiệt ra môi trường và nhiệt dung của dụng cụ. Đồ thị hình dưới đây mô tả nhiệt độ của mẫu theo thời gian. "
  "Người quan sát KHÔNG biết giá trị của m và P. Chỉ từ đồ thị, đại lượng nào sau đây xác định được?",
fig="b1_do_thi_dun_nong",
cap="Nhiệt độ của mẫu chất theo thời gian khi được cung cấp nhiệt với công suất không đổi",
o=["Nhiệt dung riêng của chất ở thể rắn.",
   "Nhiệt nóng chảy riêng của chất.",
   "Tỉ số giữa nhiệt nóng chảy riêng và nhiệt dung riêng ở thể rắn.",
   "Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn mẫu chất."],
a="C",
sol="Gọi t₁ = 120 s (giai đoạn 1, chất rắn nóng lên ΔT₁ = 100 K) và t₂ = 300 s (giai đoạn 2, nóng chảy).\n"
    "Giai đoạn 1: P·t₁ = m·c_rắn·ΔT₁ ⟹ c_rắn = P·t₁/(m·ΔT₁).\n"
    "Giai đoạn 2: P·t₂ = m·λ ⟹ λ = P·t₂/m.\n"
    "Mỗi đại lượng riêng lẻ đều còn chứa thừa số P/m chưa biết nên không tính được. Nhưng khi lập tỉ số thì "
    "P và m đồng thời bị khử:\n"
    "λ/c_rắn = (P·t₂/m) : (P·t₁/(m·ΔT₁)) = t₂·ΔT₁/t₁ = 300 · 100/120 = 250 K.\n"
    "Phương án “nhiệt lượng để làm nóng chảy hoàn toàn mẫu chất” cũng sai, vì Q = P·t₂ vẫn đòi hỏi biết P."),

dict(
tag="Chu trình – dấu của công và nhiệt",
q="Một lượng khí lí tưởng thực hiện chu trình kín 1 → 2 → 3 → 4 → 1 như hình vẽ dưới đây. Trong cả một chu trình, "
  "khối khí đã",
fig="b1_chu_trinh_pV",
cap="Chu trình gồm hai quá trình đẳng tích và hai quá trình đẳng áp",
o=["nhận công 600 J và toả ra nhiệt lượng 600 J.",
   "sinh công 600 J và nhận vào nhiệt lượng 600 J.",
   "nhận công 900 J và nhận vào nhiệt lượng 900 J.",
   "sinh công 900 J và toả ra nhiệt lượng 900 J."],
a="B",
sol="Công khí sinh ra trong một chu trình có độ lớn bằng diện tích hình được chu trình bao quanh trên "
    "giản đồ (p, V):\n"
    "A′ = Δp·ΔV = (3 − 1)·10⁵ · (5 − 2)·10⁻³ = 2·10⁵ · 3·10⁻³ = 600 J.\n"
    "Chiều đi của chu trình là chiều kim đồng hồ (1→2→3→4→1: giãn nở ở áp suất cao 3·10⁵ Pa, bị nén lại ở "
    "áp suất thấp 1·10⁵ Pa) nên công khí sinh ra lớn hơn công khí nhận vào: khối khí SINH công 600 J.\n"
    "Sau một chu trình khí trở về trạng thái đầu nên ΔU = 0. Theo định luật I: ΔU = A + Q với A là công khí "
    "nhận được, ở đây A = −600 J, do đó Q = +600 J: khí NHẬN nhiệt lượng 600 J.\n"
    "Giá trị 900 J là công của riêng quá trình 2→3, không phải công của cả chu trình."),

dict(
tag="Cân bằng nhiệt – điều kiện ẩn",
q="Trong một nhiệt lượng kế cách nhiệt lí tưởng (bỏ qua nhiệt dung của bình), người ta thả 200 g nước đá ở "
  "−20 °C vào 300 g nước ở 30 °C. Cho c_đá = 2100 J/(kg·K), c_nước = 4200 J/(kg·K), nhiệt nóng chảy riêng "
  "của nước đá λ = 3,4·10⁵ J/kg. Trạng thái của hệ khi đã cân bằng nhiệt là",
o=["14 °C, trong bình chỉ còn nước ở thể lỏng.",
   "0 °C, toàn bộ nước đá vừa vặn nóng chảy hết.",
   "0 °C, trong bình còn lại cả nước đá và nước.",
   "−18,4 °C, toàn bộ nước trong bình đã đông đặc."],
a="C",
sol="Không được đặt ngay phương trình cân bằng nhiệt với ẩn t, mà phải so sánh các “ngân sách” nhiệt lượng.\n"
    "• Nhiệt lượng nước toả ra khi hạ từ 30 °C xuống 0 °C: Q_toả = 0,3·4200·30 = 37 800 J.\n"
    "• Nhiệt lượng cần để đưa nước đá từ −20 °C lên 0 °C: Q₁ = 0,2·2100·20 = 8 400 J.\n"
    "• Phần còn lại dùng cho nóng chảy: 37 800 − 8 400 = 29 400 J.\n"
    "• Nhiệt lượng cần để nóng chảy toàn bộ 200 g nước đá: Q₂ = 0,2·3,4·10⁵ = 68 000 J.\n"
    "Vì 29 400 J < 68 000 J nên nước đá chỉ nóng chảy một phần. Khi trong bình đồng thời còn nước đá và nước "
    "thì nhiệt độ của hệ bắt buộc bằng 0 °C.\n"
    "Khối lượng đá đã chảy: Δm = 29 400/3,4·10⁵ ≈ 0,086 kg = 86 g; còn lại khoảng 114 g nước đá.\n"
    "Bẫy: đặt thẳng phương trình cân bằng nhiệt cho giả thiết “đá tan hết” sẽ ra t ≈ −18,4 °C — một kết quả "
    "vô lí (nước đá đã tan hết thì không thể ở dưới 0 °C), chính điều đó báo hiệu giả thiết ban đầu sai. "
    "Bỏ quên nhiệt nóng chảy thì ra 14 °C."),

dict(
tag="Định luật Boyle – áp suất cột thuỷ ngân",
q="Một ống thuỷ tinh dài 60 cm, một đầu kín, chứa một cột thuỷ ngân dài 10 cm. Ban đầu ống được đặt thẳng "
  "đứng, miệng ống hướng lên, cột không khí bị giam trong ống dài 40 cm (hình a). Áp suất khí quyển "
  "p₀ = 75 cmHg, nhiệt độ không đổi. Nghiêng ống sao cho trục ống hợp với phương ngang một góc 30°, miệng "
  "ống vẫn ở phía trên. Chiều dài cột khí bị giam khi đó bằng",
fig="b1_ong_thuy_ngan",
cap="Ba vị trí đặt ống: (a) miệng hướng lên, (b) nằm ngang, (c) miệng hướng xuống",
o=["40,6 cm.", "42,5 cm.", "45,3 cm.", "47,1 cm."],
a="B",
sol="Cột thuỷ ngân chỉ gây thêm áp suất bằng CHIỀU CAO THEO PHƯƠNG THẲNG ĐỨNG của nó, chứ không phải bằng "
    "chiều dài của cột.\n"
    "Trạng thái 1 (ống thẳng đứng, miệng trên): p₁ = p₀ + 10 = 85 cmHg; ℓ₁ = 40 cm ⟹ p₁ℓ₁ = 3400.\n"
    "Trạng thái 2 (ống nghiêng 30° so với phương ngang): chiều cao thẳng đứng của cột thuỷ ngân là "
    "10·sin30° = 5 cm ⟹ p₂ = 75 + 5 = 80 cmHg.\n"
    "Định luật Boyle: ℓ₂ = 3400/80 = 42,5 cm. Kiểm tra: 42,5 + 10 = 52,5 cm < 60 cm nên thuỷ ngân không tràn "
    "ra, kết quả hợp lệ.\n"
    "Bẫy: dùng cos30° cho ra 40,6 cm; quên hẳn góc nghiêng (coi như nằm ngang) cho ra 45,3 cm."),

dict(
tag="Đồ thị p–T – nhận dạng quá trình",
q="Hình dưới đây biểu diễn ba đường (1), (2), (3) trong hệ toạ độ (p, T) của các lượng khí lí tưởng. Hai đường "
  "(1) và (2) là các đường thẳng đi qua gốc toạ độ; đường (3) là đường thẳng cắt trục p tại một giá trị "
  "khác không. Nhận định nào sau đây đúng?",
fig="b1_pT_dang_tich",
cap="Ba đường biểu diễn trong hệ toạ độ (p, T)",
o=["Đường (1) ứng với thể tích khí lớn hơn đường (2).",
   "Đường (1) ứng với thể tích khí nhỏ hơn đường (2).",
   "Đường (3) cũng là một đường đẳng tích, ứng với thể tích lớn nhất trong ba đường.",
   "Cả ba đường đều là đường đẳng tích vì đều là đường thẳng trong hệ (p, T)."],
a="B",
sol="Với một lượng khí lí tưởng xác định, phương trình trạng thái cho p = (nR/V)·T. Trong hệ (p, T), quá "
    "trình đẳng tích là ĐƯỜNG THẲNG ĐI QUA GỐC TOẠ ĐỘ với hệ số góc k = nR/V.\n"
    "Vì k tỉ lệ NGHỊCH với V nên đường càng dốc thì thể tích càng NHỎ. Đường (1) dốc hơn đường (2) nên "
    "V₁ < V₂.\n"
    "Đường (3) tuy thẳng nhưng không qua gốc toạ độ: khi ngoại suy về T = 0 K nó vẫn cho p ≠ 0, điều này "
    "không thể xảy ra với một lượng khí lí tưởng xác định giữ nguyên thể tích. Vậy (3) không phải quá "
    "trình đẳng tích, và phương án “cả ba đều là đường đẳng tích” cũng sai (chẳng hạn nó ứng với quá trình vừa nung nóng vừa cho khí thoát bớt, hoặc thể tích "
    "thay đổi)."),

dict(
tag="Thực nghiệm – phát hiện sai số hệ thống",
q="Một nhóm học sinh dùng xilanh có thang chia độ nối với áp kế để kiểm chứng định luật Boyle ở nhiệt độ "
  "không đổi. Kết quả đo được ghi trong bảng. Nhóm nhận thấy tích p·V không phải là hằng số. Giáo viên gợi ý "
  "rằng ngoài thể tích V đọc được trên thang chia độ, lượng khí bị nhốt còn chiếm thêm một thể tích V₀ không "
  "đổi ở đầu xilanh và trong ống nối (“thể tích chết”). Giá trị của V₀ là",
fig="b1_xilanh_boyle",
cap="Bộ thí nghiệm kiểm chứng định luật Boyle với thể tích chết ở đầu xilanh",
tbl=("Số liệu đo được",
     ["p (10⁵ Pa)", "1,0", "1,2", "1,5", "2,0", "3,0"],
     [["V đọc được (cm³)", "55", "45", "35", "25", "15"],
      ["p·V (10⁵ Pa·cm³)", "55,0", "54,0", "52,5", "50,0", "45,0"]]),
o=["2,5 cm³.", "5,0 cm³.", "7,5 cm³.", "10,0 cm³."],
a="B",
sol="Lượng khí thực sự bị nhốt có thể tích V + V₀, nên định luật Boyle phải viết là p(V + V₀) = C.\n"
    "Lấy hai cặp số liệu ở hai đầu bảng:\n"
    "  1,0·(55 + V₀) = 3,0·(15 + V₀) ⟹ 55 + V₀ = 45 + 3V₀ ⟹ 2V₀ = 10 ⟹ V₀ = 5,0 cm³.\n"
    "Kiểm tra lại với toàn bộ bảng: p(V + 5) lần lượt bằng 1,0·60 = 60; 1,2·50 = 60; 1,5·40 = 60; "
    "2,0·30 = 60; 3,0·20 = 60 (10⁵ Pa·cm³) — hằng số đúng ở cả năm lần đo. Vậy V₀ = 5,0 cm³ và "
    "C = 60·10⁵ Pa·cm³ = 6,0 J.\n"
    "Dấu hiệu nhận biết: p·V giảm đều khi p tăng, tức là thể tích thật luôn LỚN HƠN thể tích đọc được một "
    "lượng không đổi."),

dict(
tag="Hai chặng – điều kiện ẩn",
q="Một xilanh thẳng đứng, tiết diện đều, chứa khí lí tưởng bị nhốt dưới một pit-tông nhẹ, dịch chuyển không "
  "ma sát. Ban đầu cột khí cao 20 cm ở nhiệt độ 27 °C, áp suất khí trong xilanh là 1,2·10⁵ Pa. Phía trên "
  "pit-tông có hai vấu chặn, cách pit-tông 5 cm (hình dưới đây). Đun nóng khí thật chậm. Nhiệt độ của khí khi áp "
  "suất trong xilanh đạt 1,8·10⁵ Pa là",
fig="b1_xilanh_chan",
cap="Xilanh thẳng đứng có vấu chặn giới hạn hành trình của pit-tông",
o=["450 K.", "468,75 K.", "562,5 K.", "600 K."],
a="C",
sol="Quá trình gồm HAI CHẶNG khác hẳn nhau, ranh giới là lúc pit-tông chạm vấu chặn.\n"
    "Chặng 1 – ĐẲNG ÁP (pit-tông còn tự do, p = 1,2·10⁵ Pa không đổi vì trọng lượng pit-tông và áp suất khí "
    "quyển không đổi). Khí giãn từ 20 cm lên 25 cm:\n"
    "  T₂ = T₁·ℓ₂/ℓ₁ = 300·25/20 = 375 K.\n"
    "Chặng 2 – ĐẲNG TÍCH (pit-tông đã tì vào vấu chặn, thể tích không tăng được nữa, áp suất bắt đầu tăng):\n"
    "  T₃ = T₂·p₃/p₂ = 375·1,8/1,2 = 562,5 K.\n"
    "Bẫy: áp thẳng định luật đẳng tích từ trạng thái đầu, T = 300·1,8/1,2 = 450 K — sai vì trong chặng đầu "
    "thể tích đã thay đổi. Bẫy khác: áp phương trình trạng thái trực tiếp từ (1) đến (3) mà quên rằng ở "
    "trạng thái 3 chiều cao cột khí là 25 cm chứ không phải 20 cm."),

dict(
tag="Mô hình động học phân tử – so sánh",
q="Một bình kín chứa hỗn hợp khí heli (M = 4 g/mol) và argon (M = 40 g/mol). Hỗn hợp đã ở trạng thái cân "
  "bằng nhiệt. So sánh nào sau đây là đúng?",
o=["Động năng tịnh tiến trung bình của phân tử heli lớn gấp 10 lần của phân tử argon.",
   "Tốc độ căn quân phương của phân tử heli lớn hơn của phân tử argon khoảng 3,16 lần.",
   "Khí heli có nhiệt độ cao hơn khí argon vì các phân tử heli chuyển động nhanh hơn.",
   "Trong bình nhất định có nhiều phân tử heli hơn phân tử argon."],
a="B",
sol="Ở trạng thái cân bằng nhiệt, hai chất khí có CÙNG nhiệt độ T. Động năng tịnh tiến trung bình của một "
    "phân tử chỉ phụ thuộc nhiệt độ: W̄_đ = (3/2)kT — nó BẰNG NHAU cho cả heli và argon, nên phương án “heli "
    "có động năng trung bình gấp 10 lần” sai; đây là sai lầm phổ biến nhất.\n"
    "Từ (1/2)m·v̄² = (3/2)kT suy ra v_rms = √(3kT/m) ∝ 1/√M. Do đó\n"
    "  v_He/v_Ar = √(M_Ar/M_He) = √(40/4) = √10 ≈ 3,16 — đây là phương án đúng.\n"
    "Phương án “heli có nhiệt độ cao hơn” sai vì hai khí trong cùng một bình ở trạng thái cân bằng nhiệt thì cùng nhiệt độ — “chuyển động "
    "nhanh hơn” ở đây là hệ quả của khối lượng phân tử nhỏ hơn, không phải của nhiệt độ cao hơn.\n"
    "Phương án về số phân tử sai vì đề không cho biết gì về số mol của từng khí."),

dict(
tag="Đồ thị V–t – ngoại suy về −273 °C",
q="Hình dưới đây là hai đường thẳng (1) và (2) biểu diễn thể tích của hai khối khí theo nhiệt độ Celsius. Kéo "
  "dài đường (1) thì nó cắt trục hoành đúng tại −273 °C; kéo dài đường (2) thì tại −273 °C nó vẫn cho một "
  "giá trị thể tích khác không. Kết luận nào sau đây đúng?",
fig="b1_VT_hai_duong",
cap="Hai đường thẳng trong hệ toạ độ (V, t) và phép ngoại suy về −273 °C",
o=["Cả hai đều là quá trình đẳng áp; đường (2) ứng với áp suất lớn hơn.",
   "Chỉ đường (1) là quá trình đẳng áp; đường (2) không thể là quá trình đẳng áp của một lượng khí lí "
   "tưởng xác định.",
   "Chỉ đường (2) là quá trình đẳng áp, vì đồ thị đẳng áp không đi qua gốc toạ độ.",
   "Cả hai đều không phải quá trình đẳng áp, vì trong hệ (V, t) đồ thị đẳng áp phải là đường cong."],
a="B",
sol="Định luật Charles viết theo nhiệt độ Kelvin: V = (nR/p)·T. Đổi sang thang Celsius (T = t + 273):\n"
    "  V = (nR/p)·(t + 273).\n"
    "Đây là một đường thẳng trong hệ (V, t), và điều then chốt là nó phải TRIỆT TIÊU tại t = −273 °C — "
    "nghĩa là phần kéo dài của nó bắt buộc đi qua điểm (−273 °C; 0).\n"
    "Đường (1) thoả mãn điều kiện đó nên là quá trình đẳng áp. Đường (2) khi ngoại suy về −273 °C vẫn còn "
    "V ≠ 0, nên nó không thể là quá trình đẳng áp của một lượng khí lí tưởng xác định (có thể trong quá "
    "trình đó áp suất đã thay đổi, hoặc lượng khí đã thay đổi).\n"
    "Lưu ý: đồ thị đẳng áp trong hệ (V, t) đúng là đường THẲNG, nên phương án cho rằng nó phải là đường cong sai."),

dict(
tag="Bối cảnh thực tế – khinh khí cầu",
q="Khinh khí cầu có phần vỏ mềm nhưng luôn căng, thể tích trong cầu coi như không đổi; đáy cầu để hở nên "
  "áp suất khí bên trong luôn bằng áp suất khí quyển bên ngoài. Khi đốt nóng không khí bên trong cầu, phát "
  "biểu nào sau đây đúng?",
fig="b1_khinh_khi_cau",
cap="Khinh khí cầu có miệng hở ở đáy",
o=["Khối lượng không khí trong cầu không đổi, chỉ có khối lượng riêng của nó giảm.",
   "Một phần không khí bị đẩy ra ngoài qua miệng hở, do đó khối lượng riêng của khí trong cầu giảm.",
   "Nhiệt độ tăng làm áp suất khí trong cầu tăng lên, chính độ chênh áp suất đó nâng cầu lên.",
   "Lực đẩy Archimedes tác dụng lên cầu tăng lên vì thể tích khí trong cầu tăng."],
a="B",
sol="Ba điều kiện của bài toán: V không đổi (vỏ căng), p không đổi (miệng hở thông với khí quyển), T tăng.\n"
    "Từ pV = (m/M)RT suy ra m = pVM/(RT). Khi p, V, M giữ nguyên và T tăng thì m PHẢI GIẢM: một phần không "
    "khí bị đẩy ra ngoài qua miệng hở. Đây chính là điểm mà đa số học sinh bỏ sót — họ mặc định lượng khí "
    "không đổi.\n"
    "Khối lượng riêng ρ = m/V = pM/(RT) giảm khi T tăng, nên trọng lượng của khối khí trong cầu giảm trong "
    "khi lực đẩy Archimedes F_A = ρ_ngoài·V·g giữ nguyên (vì V và ρ_ngoài không đổi). Chính điều đó, chứ "
    "không phải chênh lệch áp suất hay việc F_A tăng, làm cầu bay lên. Chú ý F_A = ρ_ngoài·V·g hoàn toàn không đổi vì cả ρ_ngoài lẫn V đều không đổi."),

dict(
tag="Định luật I – giãn nở vào chân không",
q="Một bình cách nhiệt cứng được chia thành hai ngăn bằng một vách ngăn mỏng. Ngăn A chứa khí lí tưởng, "
  "ngăn B là chân không. Vách ngăn bị chọc thủng, khí tràn sang chiếm toàn bộ bình. Bỏ qua nhiệt dung của "
  "bình và của vách. Kết luận nào sau đây đúng?",
fig="b1_binh_chan_khong",
cap="Khí lí tưởng giãn nở vào chân không trong một bình cách nhiệt",
o=["Khí sinh công khi giãn nở nên nội năng và nhiệt độ của khí đều giảm.",
   "Khí không trao đổi nhiệt và cũng không sinh công với bên ngoài, nên nội năng và nhiệt độ của khí "
   "không đổi.",
   "Áp suất khí giảm bao nhiêu lần thì nhiệt độ của khí cũng giảm bấy nhiêu lần.",
   "Nội năng của khí tăng vì các phân tử chuyển động hỗn loạn hơn trong thể tích lớn hơn."],
a="B",
sol="Áp dụng định luật I nhiệt động lực học ΔU = A + Q cho lượng khí:\n"
    "• Q = 0 vì bình cách nhiệt.\n"
    "• A = 0. Đây là mấu chốt: khí giãn nở vào CHÂN KHÔNG, phía trước không có gì để khí đẩy, tức là không "
    "có lực cản nào để khí thực hiện công. Công chỉ sinh ra khi khí đẩy được một vật (pit-tông, khí quyển…) "
    "dịch chuyển.\n"
    "Suy ra ΔU = 0. Với khí lí tưởng, nội năng chỉ là tổng động năng chuyển động nhiệt của các phân tử và "
    "chỉ phụ thuộc nhiệt độ, nên T không đổi.\n"
    "Phương án “khí sinh công nên nội năng giảm” nhầm “giãn nở” với “sinh công”. Phương án về tỉ lệ p–T sai "
    "vì V cũng thay đổi, không thể dùng định luật đẳng tích. Phương án “nội năng tăng” cũng sai: thể tích "
    "lớn hơn không làm tăng động năng của các phân tử."),

dict(
tag="Nhiệt lượng kế – phần nhiệt bị “giấu”",
q="Một nhiệt lượng kế đang chứa 200 g nước, cả bình và nước cùng ở 20 °C. Đổ thêm vào bình 100 g nước ở "
  "80 °C, khuấy đều thì nhiệt độ cân bằng là 38 °C. Bỏ qua sự trao đổi nhiệt với môi trường; "
  "c_nước = 4200 J/(kg·K). Nhiệt dung của nhiệt lượng kế bằng",
fig="b1_nhiet_luong_ke",
cap="Nhiệt lượng kế: phần vỏ bình cũng thu nhiệt khi nhiệt độ trong bình tăng",
o=["105 J/K.", "140 J/K.", "210 J/K.", "280 J/K."],
a="B",
sol="Nếu bỏ qua bình, phương trình cân bằng nhiệt sẽ cho nhiệt độ cân bằng "
    "t = (0,1·80 + 0,2·20)/0,3 = 40 °C ≠ 38 °C. Chênh lệch đó chính là do vỏ bình cũng thu nhiệt.\n"
    "• Nước nóng toả ra: Q_toả = 0,1·4200·(80 − 38) = 17 640 J.\n"
    "• Nước lạnh thu vào: Q₁ = 0,2·4200·(38 − 20) = 15 120 J.\n"
    "• Phần còn lại do bình thu: Q₂ = 17 640 − 15 120 = 2 520 J.\n"
    "Bình nóng lên cùng với nước, tức là cũng tăng 18 K:\n"
    "  C = Q₂/ΔT = 2 520/18 = 140 J/K."),

dict(
tag="Đồ thị Q–ΔT với khối lượng khác nhau",
q="Hai mẫu chất lỏng khác nhau được đun nóng và người ta ghi lại nhiệt lượng cung cấp Q theo độ tăng nhiệt "
  "độ ΔT, thu được hai đường thẳng (1) và (2) như hình vẽ dưới đây. Mẫu ứng với đường (1) có khối lượng 1,0 kg; mẫu "
  "ứng với đường (2) có khối lượng 0,4 kg. Nhiệt dung riêng của chất (2) lớn hơn của chất (1) bao nhiêu lần?",
fig="b1_Q_deltaT",
cap="Nhiệt lượng cung cấp theo độ tăng nhiệt độ của hai mẫu chất lỏng",
o=["0,50 lần.", "0,80 lần.", "1,25 lần.", "2,00 lần."],
a="D",
sol="Từ Q = m·c·ΔT, hệ số góc của mỗi đường thẳng là k = m·c, tức là NHIỆT DUNG của cả mẫu, chứ không phải "
    "nhiệt dung riêng.\n"
    "Đọc đồ thị: k₁ = 100 kJ/50 K = 2,0 kJ/K;  k₂ = 80 kJ/50 K = 1,6 kJ/K.\n"
    "  c₁ = k₁/m₁ = 2000/1,0 = 2000 J/(kg·K)\n"
    "  c₂ = k₂/m₂ = 1600/0,4 = 4000 J/(kg·K)\n"
    "⟹ c₂/c₁ = 2,00.\n"
    "Bẫy: so sánh trực tiếp độ dốc hai đường sẽ kết luận ngược (chất 2 có nhiệt dung riêng nhỏ hơn, tỉ số "
    "0,80). Đường thoải hơn ở đây lại ứng với chất có nhiệt dung riêng LỚN hơn, chỉ vì mẫu của nó nhẹ hơn."),

dict(
tag="Chọn đúng mô hình – khi lượng khí thay đổi",
q="Một bình kín có thể tích không đổi chứa khí lí tưởng. Người ta vừa đun nóng bình vừa bơm thêm khí cùng "
  "loại vào bình. Gọi (1) là trạng thái đầu và (2) là trạng thái cuối. Nhận định nào sau đây đúng?",
o=["Vì thể tích không đổi nên chắc chắn p₁/T₁ = p₂/T₂.",
   "Vì khí là khí lí tưởng nên chắc chắn p₁V₁/T₁ = p₂V₂/T₂.",
   "Không có hệ thức nào trong các hệ thức pV, p/T, pV/T là hằng số, vì lượng khí trong bình đã thay đổi.",
   "Vì nhiệt độ tăng nên pV không còn là hằng số, nhưng p/T thì vẫn đúng."],
a="C",
sol="Điều kiện áp dụng của cả ba định luật chất khí và của phương trình trạng thái là: MỘT LƯỢNG KHÍ XÁC "
    "ĐỊNH (số mol n không đổi). Đây là điều kiện thường bị bỏ qua nhất.\n"
    "Ở đây khí được bơm thêm vào nên n tăng. Hệ thức tổng quát luôn đúng là pV = nRT, viết cho hai trạng "
    "thái:\n"
    "  p₁V/T₁ = n₁R  và  p₂V/T₂ = n₂R, với n₂ > n₁.\n"
    "Do đó p/T KHÔNG phải hằng số, và pV/T cũng không. Muốn giải bài toán loại này phải dùng trực tiếp "
    "pV = nRT (hoặc pV = (m/M)RT) cho từng trạng thái, coi n (hoặc m) là một ẩn."),

dict(
tag="Suy luận ngược từ đồ thị p–V",
q="Một lượng khí lí tưởng xác định biến đổi từ trạng thái A(1 L; 4·10⁵ Pa) đến trạng thái B(4 L; 1·10⁵ Pa) "
  "theo một ĐƯỜNG THẲNG trên giản đồ (p, V) như hình vẽ dưới đây. Trong quá trình đó, nhiệt độ của khí",
fig="b1_pV_duong_thang",
cap="Quá trình biến đổi theo đường thẳng trên giản đồ (p, V); đường nét đứt là đường đẳng nhiệt qua A",
o=["tăng đều từ A đến B.",
   "giảm đều từ A đến B.",
   "không đổi, vì p_A·V_A = p_B·V_B.",
   "tăng rồi giảm, đạt giá trị lớn nhất khi V = 2,5 L."],
a="D",
sol="Với lượng khí xác định, T tỉ lệ thuận với tích pV. Phải khảo sát tích đó trên cả quá trình chứ không "
    "chỉ ở hai đầu mút.\n"
    "Phương trình đường thẳng AB (p tính theo 10⁵ Pa, V theo L): p = 5 − V, với 1 ≤ V ≤ 4.\n"
    "  pV = V(5 − V) — một tam thức bậc hai có hệ số của V² âm.\n"
    "Đây là parabol quay bề lõm xuống, đạt cực đại tại V = 5/2 = 2,5 L, ở đó pV = 2,5·2,5 = 6,25 "
    "(đơn vị 10⁵ Pa·L = 100 J), tức là 625 J.\n"
    "Ở hai đầu: p_A V_A = 1·4 = 4 và p_B V_B = 4·1 = 4 (tức 400 J).\n"
    "Vậy nhiệt độ tăng từ A đến V = 2,5 L rồi giảm về đúng giá trị ban đầu tại B; T_max/T_A = 6,25/4 = 1,5625.\n"
    "Bẫy tinh vi nằm ở phương án “nhiệt độ không đổi vì p_A·V_A = p_B·V_B”: đúng là T_A = T_B, nhưng KHÔNG có nghĩa quá trình là đẳng nhiệt — đường "
    "đẳng nhiệt qua A là đường hypebol nét đứt, khác hẳn đường thẳng AB. Chỉ hai điểm A và B nằm trên cùng "
    "một đường đẳng nhiệt."),

dict(
tag="Tốc độ nguội lạnh – so sánh nhiệt dung riêng",
q="Hai bình nhiệt lượng kế giống hệt nhau, mỗi bình chứa 200 g chất lỏng, được để nguội trong cùng một "
  "phòng ở 20 °C. Cả hai chất lỏng cùng bắt đầu từ 80 °C. Giả thiết công suất toả nhiệt ra môi trường của "
  "mỗi bình chỉ phụ thuộc vào hiệu nhiệt độ giữa bình và phòng. Từ đồ thị, hệ số góc ban đầu của đường A là "
  "−0,50 K/phút, của đường B là −0,20 K/phút. Tỉ số nhiệt dung riêng c_B/c_A bằng",
fig="b1_do_thi_nguoi_lanh",
cap="Đường nguội lạnh của hai chất lỏng trong hai bình giống hệt nhau",
o=["0,40.", "0,72.", "1,60.", "2,50."],
a="D",
sol="Tại thời điểm ban đầu, cả hai bình cùng ở 80 °C trong cùng một phòng 20 °C, hai bình lại giống hệt "
    "nhau, nên theo giả thiết chúng toả nhiệt ra môi trường với CÙNG một công suất P.\n"
    "Trong một khoảng thời gian ngắn Δt, nhiệt lượng mà chất lỏng mất đi là\n"
    "  P·Δt = m·c·|ΔT| ⟹ P = m·c·|ΔT/Δt| = m·c·|hệ số góc|.\n"
    "Vì P và m như nhau ở hai bình:\n"
    "  c_A·0,50 = c_B·0,20 ⟹ c_B/c_A = 0,50/0,20 = 2,50.\n"
    "Ý nghĩa vật lí: chất lỏng nguội CHẬM hơn là chất có nhiệt dung riêng LỚN hơn, vì cùng mất một nhiệt "
    "lượng thì nó hạ nhiệt độ ít hơn. Bẫy: lấy tỉ số hệ số góc theo chiều ngược lại (0,40)."),

dict(
tag="Kết hợp chương I và II – nhiệt lượng trong quá trình đẳng áp",
q="Một xilanh nằm ngang có pit-tông nhẹ, dịch chuyển không ma sát, chứa 0,4 mol khí lí tưởng ĐƠN NGUYÊN TỬ "
  "ở 27 °C. Nung nóng thật chậm để khí giãn nở đẳng áp đến 127 °C. Cho R = 8,31 J/(mol·K) và biết nội năng "
  "của khí lí tưởng đơn nguyên tử được tính bằng U = (3/2)nRT. Nhiệt lượng khí nhận được trong quá trình "
  "này gần nhất với giá trị nào sau đây?",
o=["332 J.", "499 J.", "831 J.", "1330 J."],
a="C",
sol="Bài toán bắt buộc phải dùng đồng thời phương trình trạng thái (chương II) và định luật I nhiệt động "
    "lực học (chương I).\n"
    "• Công khí SINH ra trong quá trình đẳng áp:\n"
    "  A′ = p·ΔV = p(V₂ − V₁) = nR·T₂ − nR·T₁ = nR·ΔT = 0,4·8,31·100 = 332,4 J.\n"
    "  (Công khí NHẬN là A = −332,4 J.)\n"
    "• Độ tăng nội năng: ΔU = (3/2)nR·ΔT = 1,5·332,4 = 498,6 J.\n"
    "• Định luật I: ΔU = A + Q ⟹ Q = ΔU − A = 498,6 + 332,4 = 831,0 J.\n"
    "Ba phương án còn lại chính là ba đại lượng trung gian: 332 J là công, 499 J là độ tăng nội năng, còn "
    "1330 J là kết quả khi nhầm hệ số (5/2 + 3/2)."),

dict(
tag="Quá trình lặp – tư duy cấp số nhân",
q="Dùng một bơm hút để hút khí ra khỏi một bình có thể tích V = 4 L. Mỗi lần bơm, pit-tông kéo ra làm khí "
  "trong bình giãn chiếm thêm thể tích xilanh V₀ = 1 L, sau đó van đóng lại và toàn bộ khí trong xilanh bị "
  "đẩy ra ngoài. Ban đầu áp suất khí trong bình là 10⁵ Pa. Coi nhiệt độ không đổi. Sau 3 lần bơm, áp suất "
  "khí còn lại trong bình bằng",
fig="b1_bom_hut",
cap="Bơm hút khí ra khỏi bình: mỗi lần bơm khí giãn từ V sang V + V₀",
o=["2,50·10⁴ Pa.", "4,00·10⁴ Pa.", "5,12·10⁴ Pa.", "7,50·10⁴ Pa."],
a="C",
sol="Xét MỘT lần bơm. Lượng khí đang ở trong bình (áp suất p, thể tích V) giãn đẳng nhiệt sang thể tích "
    "V + V₀:\n"
    "  p·V = p′·(V + V₀) ⟹ p′ = p·V/(V + V₀) = p·4/5 = 0,8p.\n"
    "Phần khí nằm trong xilanh bị đẩy ra ngoài, phần còn lại trong bình vẫn có áp suất p′. Như vậy sau mỗi "
    "lần bơm áp suất được NHÂN với cùng một hệ số 0,8 — đây là một cấp số nhân, không phải một hiệu số "
    "không đổi.\n"
    "  p₃ = p₀·0,8³ = 10⁵·0,512 = 5,12·10⁴ Pa.\n"
    "Bẫy: nghĩ rằng mỗi lần bơm “lấy đi 1/4 lượng khí” nên sau 3 lần chỉ còn 1/4 áp suất ban đầu (2,5·10⁴ Pa) "
    "— sai vì mỗi lần chỉ lấy đi 1/5 lượng khí ĐANG CÓ chứ không phải 1/4 lượng khí ban đầu."),
]


# =====================================================================
# PHẦN II – TRẮC NGHIỆM ĐÚNG/SAI
# =====================================================================
P2 = [

dict(
tag="Đường cong nung nóng – bốn giai đoạn",
stem="Dùng một thiết bị đun có công suất không đổi P = 200 W để đun 100 g nước đá ban đầu ở −20 °C cho tới "
     "khi toàn bộ hoá thành hơi ở 100 °C. Bỏ qua hao phí nhiệt và nhiệt dung của dụng cụ. Cho "
     "c_đá = 2100 J/(kg·K), c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg, nhiệt hoá hơi riêng của nước "
     "L = 2,26·10⁶ J/kg.",
fig="b1_do_thi_da_nuoc_hoi",
cap="Nhiệt độ của mẫu nước theo thời gian đun",
items=[
 ("Trong giai đoạn nước đá đang nóng chảy, nội năng của hệ không đổi vì nhiệt độ không đổi.", False,
  "Sai. Nhiệt lượng cung cấp trong giai đoạn nóng chảy dùng để phá vỡ liên kết trong mạng tinh thể, tức là "
  "làm tăng thế năng tương tác giữa các phân tử. Nội năng gồm cả động năng và thế năng phân tử, nên nội "
  "năng TĂNG mạnh (thêm 34 000 J) dù nhiệt độ giữ nguyên 0 °C."),
 ("Sau 21 giây kể từ lúc bắt đầu đun, nước đá bắt đầu nóng chảy.", True,
  "Đúng. Q₁ = m·c_đá·Δt = 0,1·2100·20 = 4 200 J; thời gian t₁ = Q₁/P = 4 200/200 = 21 s."),
 ("Đoạn nằm ngang ứng với quá trình nóng chảy dài 170 s, ngắn hơn nhiều so với đoạn nằm ngang ứng với quá "
  "trình hoá hơi.", True,
  "Đúng. Nóng chảy: Q₂ = m·λ = 0,1·3,4·10⁵ = 34 000 J ⟹ t₂ = 170 s. Hoá hơi: "
  "Q₄ = m·L = 0,1·2,26·10⁶ = 226 000 J ⟹ t₄ = 1 130 s. Tỉ số ≈ 6,6 lần, phù hợp với thực tế là muốn tách "
  "hẳn các phân tử ra khỏi nhau (hoá hơi) cần nhiều năng lượng hơn nhiều so với chỉ phá vỡ trật tự tinh "
  "thể (nóng chảy)."),
 ("Tổng thời gian từ lúc bắt đầu đun đến khi toàn bộ nước hoá hơi hết là 1 321 s.", False,
  "Sai vì đã bỏ sót giai đoạn đun nước từ 0 °C lên 100 °C: Q₃ = 0,1·4200·100 = 42 000 J ⟹ t₃ = 210 s. "
  "Tổng thời gian đúng là 21 + 170 + 210 + 1 130 = 1 531 s. Con số 1 321 s chính là kết quả khi cộng "
  "thiếu giai đoạn 3 — một sai sót rất dễ mắc vì trên đồ thị giai đoạn này chỉ là một đoạn dốc ngắn."),
]),

dict(
tag="Ống thuỷ ngân – điều kiện ẩn “tràn thuỷ ngân”",
stem="Một ống thuỷ tinh dài 60 cm, một đầu kín, chứa cột thuỷ ngân dài 10 cm. Đặt ống thẳng đứng, miệng "
     "hướng lên thì cột không khí bị giam dài 40 cm. Áp suất khí quyển p₀ = 75 cmHg, nhiệt độ không đổi "
     "trong mọi thao tác.",
fig="b1_ong_thuy_ngan",
cap="Ba vị trí đặt ống",
items=[
 ("Áp suất của cột khí bị giam khi ống thẳng đứng, miệng hướng lên là 85 cmHg.", True,
  "Đúng. Khí bị giam ở đáy phải đỡ cả khí quyển lẫn cột thuỷ ngân phía trên: p₁ = p₀ + h = 75 + 10 = 85 cmHg. "
  "Khi đó p₁ℓ₁ = 85·40 = 3400 (cmHg·cm) — hằng số Boyle của bài toán."),
 ("Khi đặt ống nằm ngang, chiều dài cột khí bị giam khoảng 45,3 cm.", True,
  "Đúng. Nằm ngang thì cột thuỷ ngân không gây thêm áp suất theo phương trục ống: p₂ = p₀ = 75 cmHg. "
  "ℓ₂ = 3400/75 ≈ 45,3 cm. Kiểm tra: 45,3 + 10 = 55,3 cm < 60 cm nên thuỷ ngân chưa bị đẩy ra."),
 ("Khi lộn ngược ống cho miệng hướng xuống, cột khí dài khoảng 52,3 cm và cột thuỷ ngân vẫn còn nguyên "
  "10 cm.", False,
  "Sai — đây là điều kiện ẩn quyết định của bài toán. Nếu giữ nguyên 10 cm thuỷ ngân thì p₃ = 75 − 10 = "
  "65 cmHg và ℓ₃ = 3400/65 ≈ 52,3 cm. Nhưng phần ống dành cho khí nhiều nhất chỉ là 60 − 10 = 50 cm. "
  "Vì 52,3 cm > 50 cm nên kết quả này vô lí: khí giãn ra đẩy thuỷ ngân tới miệng ống và một phần thuỷ "
  "ngân chảy ra ngoài."),
 ("Khi lộn ngược ống, cột thuỷ ngân còn lại trong ống dài khoảng 8,7 cm.", True,
  "Đúng. Gọi x (cm) là chiều dài cột thuỷ ngân còn lại; khi đó thuỷ ngân nằm sát miệng ống nên cột khí "
  "dài (60 − x) và áp suất khí là p = 75 − x. Định luật Boyle:\n"
  "  (75 − x)(60 − x) = 3400 ⟺ x² − 135x + 1100 = 0 ⟹ x = (135 − √13825)/2 ≈ 8,71 cm "
  "(nghiệm còn lại x ≈ 126 cm bị loại vì lớn hơn chiều dài ống).\n"
  "Kiểm tra: cột khí 51,29 cm, p = 66,29 cmHg, tích 66,29·51,29 ≈ 3400 ✓."),
]),

dict(
tag="Mô hình động học phân tử – đếm và ước lượng",
stem="Một bình kín thể tích 2,0 L chứa khí lí tưởng ở áp suất 1,0·10⁵ Pa và nhiệt độ 300 K. Cho hằng số "
     "Boltzmann k = 1,38·10⁻²³ J/K.",
items=[
 ("Số phân tử khí trong bình vào khoảng 4,8·10²² phân tử.", True,
  "Đúng. Từ p = (N/V)kT suy ra N = pV/(kT) = (1,0·10⁵ · 2,0·10⁻³)/(1,38·10⁻²³ · 300) = "
  "200/(4,14·10⁻²¹) ≈ 4,83·10²²."),
 ("Động năng tịnh tiến trung bình của một phân tử khí trong bình là 6,21·10⁻²¹ J.", True,
  "Đúng. W̄_đ = (3/2)kT = 1,5·1,38·10⁻²³·300 = 6,21·10⁻²¹ J. Giá trị này chỉ phụ thuộc nhiệt độ, không "
  "phụ thuộc loại khí."),
 ("Tổng động năng tịnh tiến của tất cả các phân tử khí trong bình bằng 200 J.", False,
  "Sai. Giá trị đúng là 300 J: W = N·(3/2)kT = (3/2)·(NkT) = (3/2)pV = 1,5·1,0·10⁵·2,0·10⁻³ = 300 J "
  "(kiểm tra trực tiếp: 4,83·10²² · 6,21·10⁻²¹ ≈ 300 J). Con số 200 J chính là tích pV — đó là sai lầm "
  "khi quên hệ số 3/2 trong hệ thức pV = (2/3)·W."),
 ("Nếu giữ nguyên nhiệt độ và nén khí xuống còn một nửa thể tích thì động năng tịnh tiến trung bình của "
  "mỗi phân tử tăng gấp đôi.", False,
  "Sai. W̄_đ = (3/2)kT chỉ phụ thuộc nhiệt độ. Nén đẳng nhiệt làm áp suất tăng gấp đôi (do mật độ phân "
  "tử N/V tăng gấp đôi, tức số va chạm lên thành bình trong mỗi giây tăng gấp đôi), nhưng động năng "
  "trung bình của MỖI phân tử thì không đổi."),
]),

dict(
tag="Xilanh hai ngăn – pit-tông tự do không có nghĩa là đẳng áp",
stem="Một xilanh nằm ngang dài 100 cm được chia thành hai ngăn bằng một pit-tông mỏng dẫn nhiệt kém, "
     "dịch chuyển không ma sát. Ban đầu hai ngăn có chiều dài bằng nhau (50 cm), cùng chứa khí lí tưởng "
     "ở 27 °C và 1,0·10⁵ Pa. Dùng một bộ phận đốt nóng để nâng nhiệt độ khí ở ngăn trái lên 127 °C rồi "
     "giữ ổn định, trong khi ngăn phải luôn được duy trì ở 27 °C.",
fig="b1_xilanh_hai_ngan",
cap="Xilanh nằm ngang với pit-tông ngăn cách hai lượng khí",
items=[
 ("Ở trạng thái cân bằng mới, áp suất khí ở hai ngăn vẫn bằng 1,0·10⁵ Pa, vì pit-tông dịch chuyển tự do.", False,
  "Sai — đây là bẫy chính. Pit-tông tự do chỉ bảo đảm áp suất hai bên BẰNG NHAU, chứ không bảo đảm áp suất "
  "đó giữ nguyên giá trị cũ. Khí ngăn phải bị nén lại nên áp suất chung phải tăng; tính toán cho "
  "p′ ≈ 1,17·10⁵ Pa."),
 ("Ở trạng thái cân bằng mới, thể tích ngăn trái gấp 4/3 lần thể tích ngăn phải.", True,
  "Đúng, và đây là cách giải nhanh nhất. Hai ngăn ban đầu có cùng thể tích, cùng áp suất, cùng nhiệt độ nên "
  "có CÙNG số mol n. Ở trạng thái cuối hai ngăn có cùng áp suất p′, do đó\n"
  "  V_T/V_P = (nRT_T/p′)/(nRT_P/p′) = T_T/T_P = 400/300 = 4/3."),
 ("Pit-tông dịch chuyển về phía ngăn phải một đoạn khoảng 7,1 cm.", True,
  "Đúng. Với tiết diện S không đổi, tỉ số thể tích cũng là tỉ số chiều dài. Đặt chiều dài hai ngăn là "
  "(50 + x) và (50 − x):\n"
  "  (50 + x)/(50 − x) = 4/3 ⟹ 150 + 3x = 200 − 4x ⟹ 7x = 50 ⟹ x = 50/7 ≈ 7,14 cm."),
 ("Áp suất chung của hai ngăn lúc sau vào khoảng 1,17·10⁵ Pa.", True,
  "Đúng. Xét ngăn phải (đẳng nhiệt, 27 °C): p·50 = p′·(50 − x) ⟹ "
  "p′ = 1,0·10⁵·50/42,86 ≈ 1,17·10⁵ Pa. Kiểm tra bằng ngăn trái: "
  "p·50/300 = p′·57,14/400 ⟹ p′ = 1,0·10⁵·50·400/(300·57,14) ≈ 1,17·10⁵ Pa ✓."),
]),

dict(
tag="Chu trình – phân tích từng chặng",
stem="Một lượng khí lí tưởng thực hiện chu trình 1 → 2 → 3 → 4 → 1 như hình vẽ dưới đây, với "
     "1(2 L; 1·10⁵ Pa), 2(2 L; 3·10⁵ Pa), 3(5 L; 3·10⁵ Pa), 4(5 L; 1·10⁵ Pa). Quy ước của định luật I "
     "nhiệt động lực học: ΔU = A + Q, trong đó A là công mà khí NHẬN được.",
fig="b1_chu_trinh_pV",
cap="Chu trình gồm hai quá trình đẳng tích và hai quá trình đẳng áp",
items=[
 ("Trong giai đoạn 1 → 2, vì thể tích không đổi nên nội năng của khí cũng không đổi.", False,
  "Sai. Thể tích không đổi ⟹ A = 0, chứ không phải ΔU = 0. Áp suất tăng gấp ba trong khi V giữ nguyên nên "
  "tích pV tăng gấp ba, tức nhiệt độ tăng gấp ba, nội năng tăng. Định luật I cho ΔU = Q > 0: khí nhận "
  "nhiệt và toàn bộ nhiệt lượng đó chuyển thành nội năng."),
 ("Trong giai đoạn 2 → 3, khí sinh công 600 J.", False,
  "Sai. Đây là quá trình đẳng áp ở p = 3·10⁵ Pa với thể tích tăng từ 2 L lên 5 L:\n"
  "  A′ = p·ΔV = 3·10⁵ · 3·10⁻³ = 900 J.\n"
  "Con số 600 J là công mà khí sinh ra trong CẢ CHU TRÌNH (diện tích hình chữ nhật), không phải công của "
  "riêng chặng 2 → 3. Phải phân biệt rõ công của một chặng với công của cả chu trình."),
 ("Trong giai đoạn 4 → 1, khí nhận công 300 J và đồng thời toả nhiệt ra ngoài.", True,
  "Đúng. Khí bị nén đẳng áp ở p = 1·10⁵ Pa: A = p·|ΔV| = 1·10⁵·3·10⁻³ = 300 J > 0 (khí nhận công). "
  "Đồng thời pV giảm từ 500 J xuống 200 J nên nhiệt độ giảm, ΔU < 0. Từ Q = ΔU − A với ΔU < 0 và A > 0 "
  "suy ra Q < 0: khí toả nhiệt."),
 ("Trong cả chu trình, khí nhận vào nhiệt lượng 600 J và sinh công 600 J.", True,
  "Đúng. Công khí sinh trong cả chu trình bằng diện tích hình chữ nhật: "
  "A′ = 2·10⁵ · 3·10⁻³ = 600 J. Vì trở về trạng thái đầu nên ΔU = 0, do đó Q = −A = A′ = 600 J."),
]),

dict(
tag="Thực nghiệm Boyle – xử lí số liệu và đồ thị",
stem="Vẫn với bộ số liệu thí nghiệm kiểm chứng định luật Boyle ở Câu 6 Phần I (thể tích chết V₀ = 5,0 cm³): "
     "p (10⁵ Pa) = 1,0; 1,2; 1,5; 2,0; 3,0 và V đọc được (cm³) = 55; 45; 35; 25; 15.",
fig="b1_V_theo_1p",
cap="Đồ thị V theo 1/p: đường thẳng cắt trục V tại −V₀",
items=[
 ("Nếu vẽ đồ thị V theo 1/p thì các điểm thực nghiệm nằm trên một đường thẳng.", True,
  "Đúng. Từ p(V + V₀) = C suy ra V = C·(1/p) − V₀ — một hàm bậc nhất của biến 1/p, hệ số góc C và "
  "tung độ gốc −V₀."),
 ("Kéo dài đường thẳng đó về phía 1/p = 0 thì nó cắt trục V tại giá trị −5,0 cm³.", True,
  "Đúng. Theo hệ thức V = C·(1/p) − V₀, tung độ gốc bằng −V₀ = −5,0 cm³. Đây chính là kĩ thuật thực "
  "nghiệm để đo thể tích chết mà không cần tháo rời dụng cụ."),
 ("Việc tích p·V giảm dần khi p tăng chứng tỏ chất khí trong xilanh không tuân theo định luật Boyle.", False,
  "Sai. Chất khí vẫn tuân theo định luật Boyle; cái sai nằm ở PHÉP ĐO chứ không ở định luật. Đại lượng phải "
  "đưa vào định luật là thể tích thật của lượng khí bị nhốt, V + V₀, chứ không phải số đọc V. Khi dùng "
  "V + V₀ thì tích p(V + V₀) là hằng số ở cả năm lần đo."),
 ("Hằng số của định luật Boyle đối với lượng khí này là 6,0 J.", True,
  "Đúng. C = p(V + V₀) = 1,0·10⁵ · 60 cm³ = 1,0·10⁵ · 60·10⁻⁶ m³ = 6,0 Pa·m³ = 6,0 J. "
  "(Đơn vị của tích pV là jun, đúng như thứ nguyên của một năng lượng.)"),
]),

dict(
tag="An toàn thực tế – định luật đẳng tích",
stem="Một bình thép chứa khí nén, thể tích không đổi. Ở 27 °C áp suất khí trong bình là 8,0·10⁵ Pa. Bình có "
     "van an toàn được thiết kế để tự động xả khí khi áp suất đạt tới 12·10⁵ Pa.",
items=[
 ("Van an toàn sẽ mở khi nhiệt độ khí trong bình đạt 450 K.", True,
  "Đúng. Thể tích không đổi ⟹ p/T = hằng số: T₂ = T₁·p₂/p₁ = 300·(12/8) = 450 K."),
 ("Nếu tính theo thang Celsius thì nhiệt độ van mở là t₂ = t₁·p₂/p₁ = 27·1,5 = 40,5 °C.", False,
  "Sai. Định luật Gay-Lussac p₁/T₁ = p₂/T₂ chỉ đúng với nhiệt độ tuyệt đối (Kelvin). Tỉ lệ thuận giữa p và "
  "t (°C) là vô nghĩa — chỉ cần thử với t₁ = 0 °C là thấy ngay điều vô lí (sẽ suy ra p₂ = 0 với mọi p₁). "
  "Đây là sai lầm kinh điển khi làm bài toán chất khí."),
 ("Nhiệt độ mà van an toàn bắt đầu mở tương ứng với 177 °C.", True,
  "Đúng. T = T₁·p₂/p₁ = 300·(12/8) = 450 K, đổi sang thang Celsius: t = 450 − 273 = 177 °C."),
 ("Nếu bình bị rò rỉ làm mất 25% khối lượng khí ở 27 °C thì sau đó van chỉ mở khi nhiệt độ đạt 600 K.", True,
  "Đúng, và phải xử lí theo hai bước. Bước 1: ở 27 °C, thể tích không đổi, khối lượng khí còn 75% nên áp "
  "suất cũng còn 75%: p₁′ = 0,75·8,0·10⁵ = 6,0·10⁵ Pa (dùng pV = (m/M)RT với V, T không đổi thì p ∝ m). "
  "Bước 2: từ trạng thái mới này áp dụng định luật đẳng tích cho lượng khí còn lại: "
  "T = 300·(12/6) = 600 K."),
]),

dict(
tag="Nội năng – phân biệt các khái niệm dễ nhầm",
stem="Xét các phát biểu về nội năng và các cách làm biến đổi nội năng.",
items=[
 ("Cọ xát hai vật vào nhau làm nội năng của cả hai vật cùng tăng; đây là cách làm biến đổi nội năng bằng "
  "thực hiện công.", True,
  "Đúng. Công của lực ma sát chuyển cơ năng thành nội năng của cả hai vật. Khác với truyền nhiệt (nội năng "
  "vật này tăng thì vật kia giảm), thực hiện công có thể làm nội năng của cả hai vật cùng tăng."),
 ("Nội năng của một lượng khí lí tưởng xác định chỉ phụ thuộc vào nhiệt độ của nó.", True,
  "Đúng. Theo mô hình động học phân tử của khí lí tưởng, các phân tử chỉ tương tác khi va chạm nên thế năng "
  "tương tác coi như bằng không; nội năng chỉ là tổng động năng chuyển động nhiệt, "
  "U = N·(3/2)kT — chỉ phụ thuộc T (và số phân tử N)."),
 ("Trong quá trình đẳng nhiệt của một lượng khí lí tưởng, khí nhận được bao nhiêu nhiệt lượng thì sinh ra "
  "bấy nhiêu công.", True,
  "Đúng. Đẳng nhiệt ⟹ T không đổi; mà nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên ΔU = 0. "
  "Định luật I: 0 = A + Q ⟹ Q = −A = A′. Toàn bộ "
  "nhiệt lượng nhận vào được chuyển hết thành công mà khí sinh ra."),
 ("Một vật có nhiệt độ cao hơn thì luôn có nội năng lớn hơn một vật có nhiệt độ thấp hơn.", False,
  "Sai. Nội năng phụ thuộc cả nhiệt độ, khối lượng và bản chất của vật. Một cốc nước 100 g ở 90 °C có nội "
  "năng nhỏ hơn nhiều so với một bể nước 100 kg ở 20 °C. Nhiệt độ chỉ quyết định CHIỀU truyền nhiệt giữa "
  "hai vật tiếp xúc, không quyết định vật nào có nội năng lớn hơn."),
]),

dict(
tag="Đồ thị p–V đường thẳng – khảo sát nhiệt độ",
stem="Một lượng khí lí tưởng xác định biến đổi từ A(1 L; 4·10⁵ Pa) đến B(4 L; 1·10⁵ Pa) theo đường thẳng "
     "trên giản đồ (p, V) như hình vẽ dưới đây.",
fig="b1_pV_duong_thang",
cap="Quá trình biến đổi theo đường thẳng AB; nét đứt là đường đẳng nhiệt qua A",
items=[
 ("Nhiệt độ của khí ở trạng thái A bằng nhiệt độ của khí ở trạng thái B.", True,
  "Đúng. p_A V_A = 4·10⁵·1·10⁻³ = 400 J và p_B V_B = 1·10⁵·4·10⁻³ = 400 J. Vì T ∝ pV nên T_A = T_B. "
  "Hai điểm A và B cùng nằm trên một đường đẳng nhiệt."),
 ("Vì áp suất giảm liên tục từ A đến B nên nhiệt độ của khí cũng giảm liên tục.", False,
  "Sai. Áp suất giảm nhưng thể tích tăng; đại lượng quyết định nhiệt độ là TÍCH pV chứ không phải riêng p. "
  "Trên đoạn AB, pV = 100·V(5 − V) (J, với V tính bằng L) tăng rồi mới giảm."),
 ("Nhiệt độ của khí đạt giá trị lớn nhất khi thể tích bằng 2,5 L.", True,
  "Đúng. Trên đoạn thẳng AB có p = (5 − V)·10⁵ Pa. Do đó pV ∝ V(5 − V), là tam thức bậc hai có hệ số của "
  "V² âm, đạt cực đại tại đỉnh V = 5/2 = 2,5 L (khi đó p = 2,5·10⁵ Pa)."),
 ("Tỉ số giữa nhiệt độ lớn nhất và nhiệt độ ở trạng thái A bằng 1,5625.", True,
  "Đúng. (pV)_max = 2,5·10⁵ · 2,5·10⁻³ = 625 J, còn (pV)_A = 400 J. "
  "T_max/T_A = 625/400 = 1,5625 (tăng 56,25%)."),
]),

dict(
tag="Bối cảnh thực tế – ấm điện và hiệu suất",
stem="Một ấm điện có công suất 1500 W được dùng để đun 1,5 kg nước ở 25 °C. Chỉ 80% công suất điện được "
     "truyền hữu ích cho nước, phần còn lại hao phí ra môi trường và làm nóng vỏ ấm. Cho "
     "c_nước = 4200 J/(kg·K), nhiệt hoá hơi riêng của nước L = 2,26·10⁶ J/kg. Coi hiệu suất không đổi.",
items=[
 ("Trong giai đoạn nước đang sôi, nhiệt độ của nước không đổi nên ấm không còn truyền nhiệt cho nước nữa.", False,
  "Sai. Ấm vẫn tiếp tục truyền nhiệt với công suất hữu ích 1200 W như trước, nhưng nhiệt lượng đó dùng để "
  "hoá hơi nước (thắng lực hút giữa các phân tử để đưa chúng ra khỏi khối chất lỏng) chứ không dùng để "
  "tăng nhiệt độ. Nhiệt độ không đổi không có nghĩa là không có sự truyền nhiệt."),
 ("Thời gian đun nước từ 25 °C đến khi bắt đầu sôi là 393,75 s.", True,
  "Đúng. Công suất hữu ích P_ci = 0,8·1500 = 1200 W. "
  "Q = m·c·Δt = 1,5·4200·(100 − 25) = 472 500 J ⟹ t = 472 500/1200 = 393,75 s ≈ 6 phút 34 s."),
 ("Nếu tiếp tục đun thêm 5 phút sau khi nước đã sôi thì khối lượng nước hoá hơi vào khoảng 0,199 kg.", False,
  "Sai. Phải dùng công suất CÓ ÍCH chứ không phải công suất định mức của ấm: "
  "Q = P_ci·t = 1200·300 = 360 000 J ⟹ m_hơi = Q/L = 360 000/2,26·10⁶ ≈ 0,159 kg ≈ 159 g.\n"
  "Con số 0,199 kg ứng với việc dùng thẳng 1500 W (bỏ quên hiệu suất 80%)."),
 ("Nếu thay bằng 3,0 kg nước (vẫn ở 25 °C) thì thời gian đun tới lúc sôi tăng gấp đôi và nhiệt lượng "
  "hao phí ra môi trường trong giai đoạn đó cũng tăng gấp đôi.", True,
  "Đúng. Nhiệt lượng có ích tỉ lệ thuận với m nên với công suất hữu ích không đổi, thời gian tăng gấp đôi "
  "(787,5 s). Công suất hao phí là 300 W không đổi, mà thời gian tăng gấp đôi nên nhiệt lượng hao phí "
  "Q_hp = 300·t cũng tăng gấp đôi. (Giả thiết “hiệu suất không đổi” đã bảo đảm điều này.)"),
]),
]


# =====================================================================
# PHẦN III – TRẮC NGHIỆM TRẢ LỜI NGẮN
# =====================================================================
P3 = [

dict(
tag="Đọc đồ thị – tỉ số khử được ẩn số",
q="Một mẫu chất rắn được nung bằng thiết bị có công suất không đổi, đồ thị nhiệt độ theo thời gian như hình "
  "bên. Bỏ qua hao phí. Tỉ số giữa nhiệt nóng chảy riêng λ và nhiệt dung riêng ở thể rắn c_rắn của chất đó "
  "bằng bao nhiêu kelvin?",
fig="b1_do_thi_dun_nong",
cap="Nhiệt độ của mẫu chất theo thời gian",
ans="250",
sol="Giai đoạn 1: P·t₁ = m·c_rắn·ΔT₁ với t₁ = 120 s, ΔT₁ = 60 − (−40) = 100 K.\n"
    "Giai đoạn 2: P·t₂ = m·λ với t₂ = 420 − 120 = 300 s.\n"
    "Chia vế theo vế, P và m bị khử:\n"
    "  λ/c_rắn = t₂·ΔT₁/t₁ = 300·100/120 = 250 K.\n"
    "Đơn vị: [λ]/[c] = (J/kg)/(J/(kg·K)) = K — đúng là một nhiệt độ."),

dict(
tag="Ống thuỷ ngân – nghiệm phương trình bậc hai",
q="Ống thuỷ tinh dài 60 cm, một đầu kín, chứa cột thuỷ ngân dài 10 cm. Khi ống thẳng đứng, miệng hướng lên, "
  "cột khí bị giam dài 40 cm; áp suất khí quyển p₀ = 75 cmHg, nhiệt độ không đổi. Lộn ngược ống cho miệng "
  "hướng xuống. Chiều dài cột thuỷ ngân còn lại trong ống bằng bao nhiêu xentimét (làm tròn đến chữ số "
  "thập phân thứ nhất)?",
fig="b1_ong_thuy_ngan",
cap="Ba vị trí đặt ống",
ans="8,7",
sol="Bước 1 – hằng số Boyle: p₁ = 75 + 10 = 85 cmHg, ℓ₁ = 40 cm ⟹ p₁ℓ₁ = 3400.\n"
    "Bước 2 – KIỂM TRA điều kiện. Nếu thuỷ ngân không tràn: p₃ = 75 − 10 = 65 cmHg, "
    "ℓ₃ = 3400/65 ≈ 52,3 cm. Nhưng chỗ trống tối đa cho khí chỉ là 60 − 10 = 50 cm. Mâu thuẫn ⟹ một phần "
    "thuỷ ngân đã chảy ra ngoài.\n"
    "Bước 3 – đặt ẩn cho trạng thái thật. Gọi x là chiều dài cột thuỷ ngân còn lại. Thuỷ ngân nằm sát miệng "
    "ống nên cột khí dài (60 − x) và áp suất khí p = p₀ − x = 75 − x:\n"
    "  (75 − x)(60 − x) = 3400 ⟺ x² − 135x + 1100 = 0\n"
    "  x = (135 − √(135² − 4400))/2 = (135 − √13825)/2 ≈ (135 − 117,58)/2 ≈ 8,7 cm.\n"
    "Nghiệm x ≈ 126,3 cm bị loại vì vượt quá chiều dài ống."),

dict(
tag="Xilanh hai ngăn",
q="Xilanh nằm ngang dài 100 cm được chia đôi bởi một pit-tông mỏng, dịch chuyển không ma sát. Hai ngăn "
  "cùng chứa khí lí tưởng ở 27 °C và 1,0·10⁵ Pa. Giữ ngăn phải ở 27 °C và nung ngăn trái lên 127 °C. "
  "Pit-tông dịch chuyển một đoạn bằng bao nhiêu xentimét (làm tròn đến chữ số thập phân thứ nhất)?",
fig="b1_xilanh_hai_ngan",
cap="Xilanh nằm ngang với pit-tông ngăn cách hai lượng khí",
ans="7,1",
sol="Pit-tông cân bằng ⟹ hai ngăn cùng áp suất p′. Hai ngăn ban đầu giống hệt nhau nên có cùng số mol n. "
    "Ở trạng thái cuối:\n"
    "  V_trái/V_phải = (nRT_trái/p′)/(nRT_phải/p′) = T_trái/T_phải = 400/300 = 4/3.\n"
    "Đặt độ dịch chuyển là x thì hai ngăn dài (50 + x) và (50 − x):\n"
    "  3(50 + x) = 4(50 − x) ⟹ 150 + 3x = 200 − 4x ⟹ x = 50/7 ≈ 7,1 cm.\n"
    "(Áp suất chung lúc sau p′ = 1,0·10⁵·50/42,86 ≈ 1,17·10⁵ Pa — pit-tông tự do KHÔNG có nghĩa là quá "
    "trình đẳng áp.)"),

dict(
tag="Cân bằng nhiệt – nóng chảy một phần",
q="Thả 300 g nước đá ở −10 °C vào 400 g nước ở 25 °C đựng trong một bình cách nhiệt lí tưởng (bỏ qua nhiệt "
  "dung của bình). Cho c_đá = 2100 J/(kg·K), c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg. Khi hệ đã cân bằng "
  "nhiệt, khối lượng nước đá còn lại là bao nhiêu gam (làm tròn đến hàng đơn vị)?",
ans="195",
sol="Bước 1 – so sánh ngân sách nhiệt.\n"
    "  Nước toả ra khi hạ xuống 0 °C: 0,4·4200·25 = 42 000 J.\n"
    "  Đưa nước đá từ −10 °C lên 0 °C cần: 0,3·2100·10 = 6 300 J.\n"
    "  Còn lại cho nóng chảy: 42 000 − 6 300 = 35 700 J.\n"
    "  Nóng chảy toàn bộ 300 g đá cần: 0,3·3,4·10⁵ = 102 000 J > 35 700 J ⟹ đá chỉ chảy một phần, "
    "nhiệt độ cân bằng là 0 °C.\n"
    "Bước 2 – khối lượng đá đã chảy: Δm = 35 700/3,4·10⁵ = 0,105 kg = 105 g.\n"
    "Bước 3 – đá còn lại: 300 − 105 = 195 g."),

dict(
tag="Bối cảnh thực tế – khinh khí cầu",
q="Một khinh khí cầu có thể tích 1000 m³, phần vỏ và giỏ nặng tổng cộng 200 kg. Không khí bên ngoài ở "
  "27 °C, áp suất 1,0·10⁵ Pa; đáy cầu hở nên áp suất khí bên trong luôn bằng áp suất bên ngoài. Khối lượng "
  "mol của không khí M = 29 g/mol, R = 8,31 J/(mol·K). Phải đốt nóng không khí trong cầu tới nhiệt độ tối "
  "thiểu bằng bao nhiêu kelvin (làm tròn đến hàng đơn vị) thì cầu bắt đầu bay lên?",
fig="b1_khinh_khi_cau",
cap="Các lực tác dụng lên khinh khí cầu",
ans="362",
sol="Khối lượng riêng của khí lí tưởng: ρ = m/V = pM/(RT).\n"
    "• Không khí ngoài: ρ_ng = (1,0·10⁵ · 0,029)/(8,31·300) = 2900/2493 ≈ 1,1633 kg/m³.\n"
    "• Điều kiện để cầu bắt đầu bay lên: lực đẩy Archimedes ≥ tổng trọng lượng\n"
    "  ρ_ng·V·g ≥ (m_vỏ + ρ_tr·V)·g ⟹ ρ_tr ≤ ρ_ng − m_vỏ/V = 1,1633 − 200/1000 = 0,9633 kg/m³.\n"
    "• Nhiệt độ tương ứng: T = pM/(R·ρ_tr) = 2900/(8,31·0,9633) ≈ 362 K (khoảng 89 °C).\n"
    "Lưu ý: áp suất trong và ngoài bằng nhau, nên chỉ có nhiệt độ mới làm khối lượng riêng bên trong khác "
    "bên ngoài."),

dict(
tag="Thực nghiệm – dùng mô hình đã hiệu chỉnh để dự đoán",
q="Với bộ thí nghiệm kiểm chứng định luật Boyle có thể tích chết V₀ = 5,0 cm³ và hằng số "
  "p(V + V₀) = 60·10⁵ Pa·cm³, nếu nén khí đến áp suất 4,0·10⁵ Pa thì số chỉ thể tích đọc được trên thang "
  "chia độ của xilanh là bao nhiêu xentimét khối?",
fig="b1_V_theo_1p",
cap="Đồ thị V theo 1/p của bộ số liệu đã hiệu chỉnh",
ans="10",
sol="Áp dụng đúng mô hình đã hiệu chỉnh chứ không dùng p·V = const:\n"
    "  p(V + V₀) = 60·10⁵ ⟹ V + 5 = 60/4,0 = 15 cm³ ⟹ V = 10 cm³.\n"
    "Nếu dùng nhầm p·V = 55·10⁵ (giá trị pV ở lần đo đầu) sẽ ra V = 13,75 cm³ — sai khoảng 37%."),

dict(
tag="Quá trình lặp – bất phương trình mũ",
q="Dùng bơm hút có thể tích xilanh V₀ = 1 L để hút khí ra khỏi một bình thể tích V = 4 L, ban đầu ở áp suất "
  "p₀. Nhiệt độ không đổi. Phải bơm ít nhất bao nhiêu lần để áp suất khí trong bình giảm xuống dưới "
  "p₀/4?",
fig="b1_bom_hut",
cap="Sơ đồ bơm hút khí",
ans="7",
sol="Sau mỗi lần bơm, áp suất được nhân với hệ số k = V/(V + V₀) = 4/5 = 0,8, nên "
    "p_n = p₀·0,8ⁿ.\n"
    "Yêu cầu: 0,8ⁿ < 0,25 ⟺ n·lg0,8 < lg0,25 ⟺ n > lg0,25/lg0,8 = (−0,6021)/(−0,0969) ≈ 6,21.\n"
    "Vì n nguyên nên n = 7. Kiểm tra: 0,8⁶ = 0,262 > 0,25 (chưa đạt); 0,8⁷ = 0,210 < 0,25 (đạt)."),

dict(
tag="Kết hợp chương I và II",
q="Nung nóng đẳng áp 0,5 mol khí lí tưởng đơn nguyên tử từ 27 °C lên 177 °C bằng một xilanh có pit-tông "
  "nhẹ, không ma sát. Cho R = 8,31 J/(mol·K) và nội năng của khí lí tưởng đơn nguyên tử U = (3/2)nRT. "
  "Nhiệt lượng khí nhận được bằng bao nhiêu jun (làm tròn đến hàng đơn vị)?",
ans="1558",
sol="ΔT = 177 − 27 = 150 K.\n"
    "• Công khí sinh ra (đẳng áp): A′ = p·ΔV = nR·ΔT = 0,5·8,31·150 = 623,25 J.\n"
    "• Độ tăng nội năng: ΔU = (3/2)nR·ΔT = 1,5·623,25 = 934,875 J.\n"
    "• Định luật I (ΔU = A + Q, với A = −A′): Q = ΔU + A′ = 934,875 + 623,25 = 1558,125 ≈ 1558 J.\n"
    "Nhận xét: chỉ 40% nhiệt lượng nhận vào chuyển thành công, 60% còn lại làm tăng nội năng."),

dict(
tag="Hai chặng – giai đoạn đẳng tích",
q="Xilanh thẳng đứng chứa khí lí tưởng dưới một pit-tông nhẹ, không ma sát; cột khí ban đầu cao 20 cm ở "
  "27 °C, áp suất 1,2·10⁵ Pa. Vấu chặn đặt cách pit-tông 5 cm. Đun nóng khí thật chậm đến 500 K. Áp suất "
  "khí trong xilanh khi đó bằng bao nhiêu (tính theo đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ nhất)?",
fig="b1_xilanh_chan",
cap="Xilanh thẳng đứng có vấu chặn",
ans="1,6",
sol="Chặng 1 – đẳng áp cho tới khi pit-tông chạm vấu (cột khí 20 → 25 cm):\n"
    "  T₂ = 300·25/20 = 375 K < 500 K, nên pit-tông chắc chắn đã chạm vấu trước khi tới 500 K.\n"
    "Chặng 2 – đẳng tích từ 375 K lên 500 K:\n"
    "  p₃ = p₂·T₃/T₂ = 1,2·10⁵ · 500/375 = 1,6·10⁵ Pa.\n"
    "Bẫy: nếu bỏ qua chặng đẳng áp và dùng ngay p = 1,2·10⁵·500/300 = 2,0·10⁵ Pa thì sai."),

dict(
tag="Hai thí nghiệm – khử nhiệt dung của bình",
q="Thí nghiệm 1: nhiệt lượng kế đang chứa 200 g nước, cả bình và nước ở 20 °C; đổ thêm 100 g nước ở 80 °C "
  "thì nhiệt độ cân bằng là 38 °C. Thí nghiệm 2: làm lại từ đầu với 200 g nước ở 20 °C trong chính bình đó, "
  "rồi thả vào một miếng kim loại khối lượng 200 g đang ở 100 °C, nhiệt độ cân bằng là 26 °C. Cho "
  "c_nước = 4200 J/(kg·K); bỏ qua trao đổi nhiệt với môi trường. Nhiệt dung riêng của kim loại bằng bao "
  "nhiêu J/(kg·K) (làm tròn đến hàng đơn vị)?",
fig="b1_nhiet_luong_ke",
cap="Nhiệt lượng kế dùng cho cả hai thí nghiệm",
ans="397",
sol="Thí nghiệm 1 dùng để đo nhiệt dung C của bình — đại lượng bị “giấu” trong thí nghiệm 2.\n"
    "  Nước nóng toả: 0,1·4200·42 = 17 640 J; nước lạnh thu: 0,2·4200·18 = 15 120 J.\n"
    "  Bình thu: 17 640 − 15 120 = 2 520 J ⟹ C = 2 520/18 = 140 J/K.\n"
    "Thí nghiệm 2 (độ tăng nhiệt độ của nước và bình là 6 K, độ giảm của kim loại là 74 K):\n"
    "  0,2·c·74 = 0,2·4200·6 + 140·6 = 5 040 + 840 = 5 880 J\n"
    "  ⟹ c = 5 880/14,8 ≈ 397 J/(kg·K).\n"
    "Nếu bỏ qua nhiệt dung của bình sẽ ra c ≈ 341 J/(kg·K), sai khoảng 14%."),

dict(
tag="Suy luận ngược – lượng khí thay đổi",
q="Một bình kín thể tích 5 L chứa khí lí tưởng ở 27 °C, áp suất 2,0·10⁵ Pa. Mở van cho khí thoát bớt ra "
  "ngoài; khi đóng van lại thì áp suất khí trong bình còn 1,2·10⁵ Pa và nhiệt độ là 7 °C. Phần trăm khối "
  "lượng khí đã thoát ra khỏi bình là bao nhiêu (làm tròn đến chữ số thập phân thứ nhất)?",
ans="35,7",
sol="Không dùng được pV/T = const vì lượng khí thay đổi; phải dùng pV = (m/M)RT cho từng trạng thái với "
    "cùng V và M:\n"
    "  m ∝ p/T.\n"
    "  m₁ ∝ 2,0·10⁵/300;  m₂ ∝ 1,2·10⁵/280.\n"
    "  m₂/m₁ = (1,2/2,0)·(300/280) = 0,6·1,0714 ≈ 0,6429.\n"
    "Phần trăm khí đã thoát ra: (1 − 0,6429)·100% ≈ 35,7%.\n"
    "Bẫy: chỉ so sánh áp suất (1 − 1,2/2,0 = 40%) là quên mất nhiệt độ cũng đã giảm."),

dict(
tag="Kết hợp chương I và II – bình cứng cách nhiệt",
q="Một bình cứng, cách nhiệt, thể tích 20 L, chứa khí lí tưởng đơn nguyên tử ở 300 K và áp suất "
  "1,5·10⁵ Pa. Một điện trở đặt bên trong bình cung cấp cho khí nhiệt lượng 900 J. Biết nội năng của khí "
  "lí tưởng đơn nguyên tử bằng U = (3/2)pV. Nhiệt độ của khí sau đó bằng bao nhiêu kelvin?",
ans="360",
sol="Bình cứng ⟹ thể tích không đổi ⟹ khí không nhận và không sinh công: A = 0.\n"
    "Định luật I: ΔU = Q = 900 J.\n"
    "  U₁ = (3/2)p₁V = 1,5·1,5·10⁵·0,020 = 4 500 J.\n"
    "  U₂ = 4 500 + 900 = 5 400 J.\n"
    "Vì U tỉ lệ thuận với T (U = (3/2)nRT):\n"
    "  T₂ = T₁·U₂/U₁ = 300·5400/4500 = 360 K.\n"
    "(Kiểm tra: p₂ = p₁·T₂/T₁ = 1,5·10⁵·1,2 = 1,8·10⁵ Pa; U₂ = 1,5·1,8·10⁵·0,02 = 5 400 J ✓)"),
]
