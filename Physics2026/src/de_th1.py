# -*- coding: utf-8 -*-
"""ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG.  Đề 01 – 05 (Dễ → Trung bình).

Mỗi đề gồm 28 câu / 40 lệnh hỏi, phân bố đều bốn chương:
  Chương I – Vật lí nhiệt   •  Chương II – Khí lí tưởng
  Chương III – Từ trường    •  Chương IV – Vật lí hạt nhân
"""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 01
DE1 = dict(
ma="TH-Đề 01", ten="ĐỀ THI THỬ SỐ 01", muc="Dễ",
trongtam="Kiểm tra nền tảng cả bốn chương: khái niệm, công thức và đơn vị cơ bản",
P1=[
mc("Nội năng của một vật là",
   ["tổng động năng chuyển động của cả vật và thế năng trọng trường.",
    "tổng động năng chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng.",
    "nhiệt lượng mà vật nhận được từ môi trường.",
    "công mà vật thực hiện lên môi trường."],
   "B",
   "Nội năng gồm động năng chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng. "
   "Nó không bao gồm động năng chuyển động của cả vật cũng như thế năng trọng trường.",
   "Nội năng", D),

mc("Trong quá trình chất rắn kết tinh đang nóng chảy, nhiệt độ của chất",
   ["tăng đều.", "không đổi.", "giảm đều.", "tăng rồi giảm."],
   "B",
   "Trong suốt quá trình nóng chảy, nhiệt lượng thu vào dùng để phá vỡ mạng tinh thể (tăng thế năng "
   "tương tác) nên nhiệt độ giữ nguyên ở nhiệt độ nóng chảy.",
   "Sự chuyển thể", D, fig="n_dt_nuocda", cap="Đồ thị nhiệt độ theo thời gian khi đun nước đá"),

mc("Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn một vật rắn đang ở nhiệt độ nóng chảy "
   "được tính bằng",
   ["Q = mcΔT.", "Q = mλ.", "Q = mL.", "Q = m/λ."],
   "B",
   "Q = mλ với λ là nhiệt nóng chảy riêng. Công thức Q = mcΔT dùng khi nhiệt độ thay đổi, "
   "còn Q = mL dùng cho quá trình hoá hơi.",
   "Nhiệt nóng chảy riêng", D),

mc("Hệ thức của định luật I nhiệt động lực học là",
   ["ΔU = A − Q.", "ΔU = A + Q.", "ΔU = Q − A.", "ΔU = A·Q."],
   "B",
   "ΔU = A + Q: độ biến thiên nội năng bằng tổng công và nhiệt lượng mà vật NHẬN được. "
   "Quy ước: mũi tên hướng vào vật thì đại lượng mang dấu dương.",
   "Định luật I nhiệt động lực học", D, fig="n_sd_dl1", cap="Quy ước dấu của A và Q"),

mc("Trong hệ SI, nhiệt độ tuyệt đối được đo bằng đơn vị",
   ["độ Celsius (°C).", "kelvin (K).", "độ Fahrenheit (°F).", "jun (J)."],
   "B",
   "Thang nhiệt độ tuyệt đối là thang Kelvin, với T(K) = t(°C) + 273. "
   "Trong mọi công thức chất khí, T bắt buộc phải tính bằng kelvin.",
   "Thang nhiệt độ", D, fig="n_sd_thang", cap="Đối chiếu thang Celsius và Kelvin"),

mc("Định luật Boyle được phát biểu cho quá trình",
   ["đẳng tích.", "đẳng nhiệt.", "đẳng áp.", "đoạn nhiệt."],
   "B",
   "Định luật Boyle áp dụng cho quá trình ĐẲNG NHIỆT: pV = hằng số, tức p₁V₁ = p₂V₂.",
   "Định luật Boyle", D, fig="k_dt_dangnhiet", cap="Đường đẳng nhiệt trong hệ (p, V)"),

mc("Phương trình trạng thái của một lượng khí lí tưởng xác định là",
   ["pV = const.", "p₁V₁/T₁ = p₂V₂/T₂.", "V/T = const.", "p/T = const."],
   "B",
   "Phương trình trạng thái p₁V₁/T₁ = p₂V₂/T₂ áp dụng cho một lượng khí xác định khi cả ba thông "
   "số đều thay đổi. Ba đáp án còn lại là các trường hợp riêng.",
   "Phương trình trạng thái", D, fig="k_sd_ba_trang_thai",
   cap="Liên hệ giữa hai trạng thái của cùng một lượng khí"),

mc("Trong mô hình động học phân tử chất khí, áp suất của chất khí sinh ra do",
   ["trọng lượng của các phân tử khí.",
    "va chạm của các phân tử khí vào thành bình.",
    "lực hút giữa các phân tử.",
    "sự nở vì nhiệt của bình chứa."],
   "B",
   "Áp suất khí là kết quả của vô số va chạm của các phân tử lên thành bình. Mật độ phân tử càng "
   "lớn và nhiệt độ càng cao thì áp suất càng lớn.",
   "Áp suất chất khí", D, fig="k_sd_vacham_thanh", cap="Va chạm phân tử lên thành bình"),

mc("Đơn vị của cảm ứng từ là",
   ["vêbe (Wb).", "tesla (T).", "vôn (V).", "ampe (A)."],
   "B",
   "Cảm ứng từ B đo bằng tesla. Vêbe là đơn vị của từ thông.",
   "Đơn vị cảm ứng từ", D),

mc("Lực từ tác dụng lên một đoạn dây dẫn thẳng dài ℓ mang dòng điện I đặt trong từ trường đều B, "
   "hợp với đường sức góc α, có độ lớn",
   ["F = BIℓ·cosα.", "F = BIℓ·sinα.", "F = BI/ℓ.", "F = Bℓ/I."],
   "B",
   "F = BIℓ·sinα. Chỉ thành phần từ trường vuông góc với dây mới gây ra lực từ nên công thức "
   "chứa sinα; khi dây song song với B thì F = 0.",
   "Lực từ", D, fig="t_sd_luctu", cap="Lực từ tác dụng lên dây dẫn"),

mc("Dòng điện cảm ứng xuất hiện trong một mạch kín khi",
   ["mạch nằm trong từ trường mạnh.", "từ thông qua mạch biến thiên.",
    "mạch có điện trở nhỏ.", "mạch chuyển động nhanh."],
   "B",
   "Điều kiện duy nhất là từ thông qua mạch kín BIẾN THIÊN. Một mạch đứng yên trong từ trường "
   "rất mạnh nhưng không đổi thì vẫn không có dòng cảm ứng.",
   "Hiện tượng cảm ứng điện từ", D, fig="t_sd_tn_faraday", cap="Thí nghiệm Faraday"),

mc("Giá trị hiệu dụng của điện áp xoay chiều liên hệ với giá trị cực đại theo hệ thức",
   ["U = U₀·√2.", "U = U₀/√2.", "U = 2U₀.", "U = U₀/2."],
   "B",
   "U = U₀/√2. Mạng điện 220 V là giá trị hiệu dụng, giá trị cực đại tương ứng khoảng 311 V.",
   "Giá trị hiệu dụng", D, fig="t_dt_u_i_hieudung", cap="Điện áp tức thời và giá trị hiệu dụng"),

mc("Hạt nhân nguyên tử gồm",
   ["prôtôn và electron.", "prôtôn và nơtron.",
    "nơtron và electron.", "chỉ có nơtron."],
   "B",
   "Hạt nhân gồm các nuclêôn là prôtôn (mang điện dương) và nơtron (không mang điện). "
   "Electron chuyển động bên ngoài hạt nhân.",
   "Cấu tạo hạt nhân", D, fig="h_sd_cautruc", cap="Cấu tạo hạt nhân"),

mc("Năng lượng liên kết riêng của một hạt nhân được tính bằng",
   ["W(lk)·A.", "W(lk)/A.", "Δm·A.", "A/W(lk)."],
   "B",
   "ε = W(lk)/A là năng lượng liên kết tính trên một nuclêôn. Đây mới là thước đo độ bền vững "
   "của hạt nhân, không phải W(lk).",
   "Năng lượng liên kết riêng", D, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Tia phóng xạ nào sau đây là dòng hạt nhân heli?",
   ["Tia β⁻.", "Tia α.", "Tia γ.", "Tia X."],
   "B",
   "Tia α chính là dòng hạt nhân ⁴₂He, mang điện tích +2e, bị chặn lại bởi một tờ giấy.",
   "Ba loại tia phóng xạ", D, fig="h_sd_tia_phongxa", cap="Ba loại tia phóng xạ"),

mc("Chu kì bán rã của một chất phóng xạ là khoảng thời gian để",
   ["toàn bộ hạt nhân phân rã hết.", "một nửa số hạt nhân ban đầu bị phân rã.",
    "độ phóng xạ tăng gấp đôi.", "số hạt nhân giảm còn một phần tư."],
   "B",
   "Sau mỗi chu kì bán rã, số hạt nhân chưa phân rã giảm đi một nửa. Sau 2T mới còn một phần tư.",
   "Chu kì bán rã", D, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),

mc("Phản ứng nhiệt hạch là phản ứng trong đó",
   ["một hạt nhân nặng vỡ thành hai hạt nhân trung bình.",
    "hai hạt nhân rất nhẹ kết hợp thành một hạt nhân nặng hơn.",
    "một hạt nhân tự phát phát ra tia phóng xạ.",
    "electron bị bứt ra khỏi nguyên tử."],
   "B",
   "Nhiệt hạch là sự kết hợp hai hạt nhân rất nhẹ, đòi hỏi nhiệt độ cực cao. "
   "Phương án đầu mô tả phản ứng phân hạch.",
   "Phản ứng nhiệt hạch", D, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Máy biến áp hoạt động dựa trên hiện tượng",
   ["nhiễm điện do cọ xát.", "cảm ứng điện từ.",
    "tác dụng nhiệt của dòng điện.", "phóng xạ."],
   "B",
   "Từ thông biến thiên trong lõi thép làm xuất hiện suất điện động cảm ứng ở cuộn thứ cấp. "
   "Vì vậy máy biến áp chỉ hoạt động với dòng điện xoay chiều.",
   "Máy biến áp", D, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),
],
P2=[
ds("Một ấm nhôm khối lượng 0,50 kg chứa 2,0 kg nước ở 25 °C. Cho c(nhôm) = 880 J/(kg·K); "
   "c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng cần cung cấp để đun nước tới 100 °C (bỏ qua ấm) là 630 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · (100 − 25) = 2,0 · 4200 · 75 = 630 000 J = 630 kJ."),
    ("Nhiệt lượng mà riêng ấm nhôm thu vào khi nóng từ 25 °C lên 100 °C là 33 kJ.", True,
     "Đúng. Q = 0,50 · 880 · 75 = 33 000 J = 33 kJ."),
    ("Tổng nhiệt lượng cần cung cấp cho cả ấm và nước là 663 kJ.", True,
     "Đúng. 630 + 33 = 663 kJ."),
    ("Nếu dùng bếp có hiệu suất 80 % thì nhiệt lượng bếp phải toả ra nhỏ hơn 663 kJ.", False,
     "Sai. Có hao phí nên bếp phải toả ra NHIỀU hơn: 663/0,80 ≈ 829 kJ. "
     "Đây là bẫy nhân – chia rất quen thuộc.")],
   "Nhiệt lượng và hiệu suất", D, fig="n_sd_hieu_suat", cap="Hiệu suất của quá trình đun nóng"),

ds("Một lượng khí lí tưởng có thể tích 8,0 L ở áp suất 1,0·10⁵ Pa và nhiệt độ 27 °C.",
   [("Nhiệt độ của khí theo thang Kelvin là 300 K.", True,
     "Đúng. T = 27 + 273 = 300 K."),
    ("Nén đẳng nhiệt khối khí xuống còn 2,0 L thì áp suất tăng lên 4,0·10⁵ Pa.", True,
     "Đúng. p₁V₁ = p₂V₂ ⇒ p₂ = 1,0·10⁵ · 8,0/2,0 = 4,0·10⁵ Pa."),
    ("Nung nóng đẳng tích khối khí lên 127 °C thì áp suất tăng lên 1,33·10⁵ Pa.", True,
     "Đúng. p₂ = p₁·T₂/T₁ = 1,0·10⁵ · 400/300 ≈ 1,33·10⁵ Pa."),
    ("Nung nóng đẳng áp khối khí từ 27 °C lên 54 °C thì thể tích tăng gấp đôi.", False,
     "Sai. Phải dùng thang Kelvin: V₂ = 8,0 · 327/300 ≈ 8,7 L, chỉ tăng khoảng 9 %. "
     "Nhân đôi nhiệt độ Celsius không có nghĩa là nhân đôi nhiệt độ tuyệt đối.")],
   "Các định luật chất khí", D, fig="k_dt_ba_he_truc",
   cap="Ba quá trình trên các hệ trục khác nhau"),

ds("Một khung dây phẳng diện tích 0,020 m² đặt vuông góc với từ trường đều B = 0,50 T.",
   [("Từ thông qua khung bằng 0,010 Wb.", True,
     "Đúng. Φ = B·S = 0,50 · 0,020 = 0,010 Wb (pháp tuyến song song với B)."),
    ("Nếu quay khung sao cho mặt phẳng khung song song với đường sức thì từ thông bằng 0.", True,
     "Đúng. Lúc đó pháp tuyến vuông góc với B nên cosθ = 0."),
    ("Nếu từ thông giảm đều về 0 trong 0,050 s thì suất điện động cảm ứng bằng 0,20 V.", True,
     "Đúng. |e| = 0,010/0,050 = 0,20 V."),
    ("Trong quá trình từ thông giảm, dòng điện cảm ứng sinh ra từ trường ngược chiều với "
     "từ trường ban đầu.", False,
     "Sai. Từ thông GIẢM nên theo định luật Lenz, dòng cảm ứng phải chống lại sự giảm bằng cách "
     "sinh ra từ trường CÙNG chiều với từ trường ban đầu.")],
   "Từ thông và cảm ứng điện từ", D, fig="t_sd_lenz", cap="Hai trường hợp của định luật Lenz"),

ds("Một mẫu chất phóng xạ có chu kì bán rã 5,0 ngày, khối lượng ban đầu 160 gam.",
   [("Sau 5,0 ngày, khối lượng còn lại là 80 gam.", True,
     "Đúng. Sau một chu kì bán rã, khối lượng còn một nửa."),
    ("Sau 15 ngày, khối lượng còn lại là 20 gam.", True,
     "Đúng. n = 15/5,0 = 3 ⇒ m = 160/8 = 20 g."),
    ("Sau 15 ngày, khối lượng đã phân rã là 140 gam.", True,
     "Đúng. 160 − 20 = 140 g."),
    ("Nếu bảo quản mẫu ở nhiệt độ thấp thì chu kì bán rã sẽ dài hơn.", False,
     "Sai. Chu kì bán rã là hằng số đặc trưng của đồng vị, hoàn toàn không phụ thuộc nhiệt độ, "
     "áp suất hay trạng thái hoá học.")],
   "Định luật phóng xạ", D),
],
P3=[
sa("Cần cung cấp bao nhiêu kilôjun nhiệt lượng để đun 3,0 kg nước từ 20 °C lên 70 °C? "
   "Cho c(nước) = 4200 J/(kg·K).",
   "630",
   "Q = m·c·ΔT = 3,0 · 4200 · (70 − 20) = 3,0 · 4200 · 50 = 630 000 J = 630 kJ.",
   "Nhiệt lượng", D),

sa("Một lượng khí ở nhiệt độ 27 °C được nung nóng đẳng tích tới 177 °C. Áp suất khí tăng lên "
   "bao nhiêu lần (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,5",
   "Đổi sang kelvin: T₁ = 300 K;  T₂ = 177 + 273 = 450 K.\n"
   "Đẳng tích nên p tỉ lệ thuận với T:  p₂/p₁ = 450/300 = 1,5 lần.",
   "Định luật Gay-Lussac", D),

sa("Một đoạn dây dẫn dài 50 cm mang dòng điện 2,0 A đặt vuông góc với từ trường đều B = 0,30 T. "
   "Lực từ tác dụng lên đoạn dây bằng bao nhiêu niutơn?",
   "0,3",
   "F = B·I·ℓ = 0,30 · 2,0 · 0,50 = 0,30 N.",
   "Lực từ", D),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 2000 vòng, cuộn thứ cấp 100 vòng, đặt dưới điện áp "
   "xoay chiều 220 V. Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng bao nhiêu vôn?",
   "11",
   "U₂ = U₁·N₂/N₁ = 220 · 100/2000 = 220/20 = 11 V.",
   "Máy biến áp", D, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

sa("Hạt nhân ⁴⁰₁₈Ar có bao nhiêu nơtron?",
   "22",
   "N = A − Z = 40 − 18 = 22 nơtron.",
   "Cấu tạo hạt nhân", D),

sa("Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ. Sau 12 giờ, số hạt nhân chưa phân rã còn lại "
   "bằng bao nhiêu phần trăm so với ban đầu (làm tròn đến chữ số thập phân thứ nhất)?",
   "12,5",
   "Số chu kì: n = 12/4,0 = 3.\n"
   "Tỉ lệ còn lại: 2⁻³ = 1/8 = 0,125 = 12,5 %.",
   "Định luật phóng xạ", D),
])


# =====================================================================  ĐỀ 02
DE2 = dict(
ma="TH-Đề 02", ten="ĐỀ THI THỬ SỐ 02", muc="Dễ",
trongtam="Nhận biết và hiểu: đọc đồ thị đơn giản, vận dụng công thức một bước cả bốn chương",
P1=[
mc("Trong chất rắn kết tinh, các hạt cấu tạo nên chất",
   ["chuyển động hỗn loạn tự do khắp bình chứa.",
    "dao động quanh những vị trí cân bằng cố định theo trật tự xác định.",
    "trượt lên nhau và đổi vị trí cân bằng liên tục.",
    "hoàn toàn đứng yên."],
   "B",
   "Chất rắn kết tinh có cấu trúc mạng tinh thể: các hạt sắp xếp trật tự và chỉ dao động nhiệt "
   "quanh vị trí cân bằng CỐ ĐỊNH. Phương án thứ ba mô tả chất lỏng.",
   "Cấu trúc của chất", D, fig="n_sd_cautruc", cap="Mô hình ba thể của chất"),

mc("Sự bay hơi khác sự sôi ở chỗ bay hơi",
   ["chỉ xảy ra ở nhiệt độ sôi.", "xảy ra ở mọi nhiệt độ và chỉ trên mặt thoáng.",
    "xảy ra trong lòng chất lỏng.", "không cần thu nhiệt."],
   "B",
   "Bay hơi xảy ra ở mọi nhiệt độ nhưng chỉ trên mặt thoáng; sôi chỉ xảy ra ở nhiệt độ sôi và "
   "diễn ra cả trong lòng chất lỏng. Cả hai đều là quá trình thu nhiệt.",
   "Bay hơi và sôi", D, fig="n_sd_bayhoi_soi", cap="So sánh bay hơi và sôi"),

mc("Khi nén khí trong xi lanh mà khí không trao đổi nhiệt với bên ngoài thì",
   ["nội năng của khí giảm.", "nội năng của khí tăng.",
    "nội năng của khí không đổi.", "nhiệt độ khí giảm."],
   "B",
   "Quá trình đoạn nhiệt có Q = 0 nên ΔU = A. Khí bị nén nên nhận công, A > 0, do đó nội năng "
   "tăng và nhiệt độ khí tăng.",
   "Định luật I nhiệt động lực học", D, fig="n_sd_cong_cua_khi", cap="Nén và giãn khí"),

mc("Nhiệt độ 27 °C tương ứng với nhiệt độ tuyệt đối",
   ["27 K.", "300 K.", "246 K.", "273 K."],
   "B",
   "T = t + 273 = 27 + 273 = 300 K.",
   "Thang nhiệt độ", D),

mc("Với một lượng khí xác định, khi giữ nhiệt độ không đổi và giảm thể tích còn một nửa thì "
   "áp suất",
   ["giảm một nửa.", "tăng gấp đôi.", "không đổi.", "tăng gấp bốn."],
   "B",
   "Định luật Boyle: pV không đổi nên p tỉ lệ nghịch với V. V giảm một nửa thì p tăng gấp đôi.",
   "Định luật Boyle", D, fig="k_dt_boyle_1V", cap="Đồ thị p theo 1/V"),

mc("Đường biểu diễn quá trình đẳng tích trong hệ toạ độ (p, T) là",
   ["một nhánh hypebol.", "đường thẳng đi qua gốc toạ độ.",
    "đường thẳng song song trục hoành.", "đường parabol."],
   "B",
   "Đẳng tích cho p/T = hằng số nên p tỉ lệ thuận với T: đồ thị là đường thẳng qua gốc toạ độ "
   "trong hệ (p, T).",
   "Đồ thị các quá trình", D, fig="k_dt_ba_he_truc", cap="Ba quá trình trên ba hệ trục"),

mc("Chuyển động Brown của hạt phấn hoa trong nước chứng tỏ",
   ["nước có khối lượng riêng lớn.",
    "các phân tử nước chuyển động hỗn loạn không ngừng.",
    "hạt phấn hoa mang điện tích.",
    "nước có lực đẩy Ác-si-mét."],
   "B",
   "Hạt phấn hoa bị các phân tử nước va chạm từ mọi phía; vì số va chạm các phía không cân bằng "
   "nên hạt chuyển động gấp khúc ngẫu nhiên. Đây là bằng chứng cho chuyển động nhiệt của phân tử.",
   "Chuyển động Brown", D, fig="k_sd_brown", cap="Quỹ đạo hạt phấn hoa"),

mc("Đường sức từ trong lòng một ống dây dài có dòng điện chạy qua",
   ["là những đường tròn đồng tâm.", "gần như song song và cách đều nhau.",
    "hội tụ về tâm ống dây.", "không tồn tại."],
   "B",
   "Trong lòng ống dây đủ dài, từ trường gần như đều nên đường sức là những đường thẳng song song, "
   "cách đều nhau.",
   "Từ trường của ống dây", D, fig="t_sd_ongday", cap="Ống dây có dòng điện"),

mc("Từ thông qua một khung dây phẳng đạt giá trị lớn nhất khi mặt phẳng khung",
   ["song song với các đường sức từ.", "vuông góc với các đường sức từ.",
    "hợp với đường sức góc 45°.", "nằm ngoài vùng từ trường."],
   "B",
   "Khi mặt phẳng khung vuông góc với đường sức, pháp tuyến song song với B nên θ = 0° và "
   "Φ = B·S đạt cực đại.",
   "Từ thông", D, fig="t_sd_tuthong", cap="Từ thông qua khung dây"),

mc("Trong máy phát điện xoay chiều, suất điện động được tạo ra nhờ",
   ["ma sát giữa các bộ phận.", "sự biến thiên từ thông qua khung dây quay.",
    "dòng điện một chiều từ ắc quy.", "hiện tượng nhiệt điện."],
   "B",
   "Khung dây quay đều trong từ trường làm góc giữa pháp tuyến và B thay đổi liên tục, "
   "từ thông biến thiên điều hoà nên xuất hiện suất điện động cảm ứng.",
   "Máy phát điện xoay chiều", D, fig="t_sd_may_phat", cap="Nguyên lí máy phát điện"),

mc("Để giảm hao phí khi truyền tải điện năng đi xa, biện pháp hiệu quả và kinh tế nhất là",
   ["dùng dây dẫn có tiết diện thật lớn.", "tăng điện áp truyền tải.",
    "giảm chiều dài đường dây.", "giảm công suất của nhà máy."],
   "B",
   "Hao phí ΔP = R·P²/U² tỉ lệ nghịch với bình phương điện áp, nên tăng U là cách giảm hao phí "
   "hiệu quả nhất. Tăng tiết diện dây cũng giảm hao phí nhưng rất tốn kim loại.",
   "Truyền tải điện năng", D, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

mc("Số khối A của một hạt nhân cho biết",
   ["số prôtôn.", "tổng số nuclêôn.", "số nơtron.", "số electron."],
   "B",
   "A là tổng số nuclêôn (prôtôn và nơtron). Số prôtôn là Z, số nơtron là N = A − Z.",
   "Cấu tạo hạt nhân", D),

mc("Đại lượng nào sau đây được bảo toàn trong phản ứng hạt nhân?",
   ["Khối lượng nghỉ.", "Số khối.",
    "Số prôtôn riêng rẽ.", "Số nơtron riêng rẽ."],
   "B",
   "Số khối và điện tích luôn được bảo toàn. Khối lượng nghỉ KHÔNG bảo toàn — phần hụt đi chuyển "
   "thành năng lượng. Số prôtôn và nơtron riêng rẽ có thể chuyển hoá cho nhau.",
   "Định luật bảo toàn", D),

mc("Tia phóng xạ có khả năng đâm xuyên mạnh nhất là",
   ["tia α.", "tia γ.", "tia β⁻.", "tia β⁺."],
   "B",
   "Thứ tự đâm xuyên tăng dần: α < β < γ. Tia γ cần lớp chì hoặc bê tông dày mới bị chặn đáng kể.",
   "Khả năng đâm xuyên", D, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),

mc("Trong phản ứng phân hạch dây chuyền, hệ số nhân nơtron k = 1 tương ứng với",
   ["phản ứng tắt dần.", "phản ứng duy trì ổn định.",
    "phản ứng bùng nổ.", "không có phản ứng."],
   "B",
   "k = 1 nghĩa là mỗi phân hạch trung bình gây ra đúng một phân hạch mới, phản ứng duy trì ổn định. "
   "Đây là chế độ hoạt động của lò phản ứng hạt nhân.",
   "Phản ứng dây chuyền", D, fig="h_sd_phan_hach", cap="Phản ứng dây chuyền"),

mc("Đơn vị becơren (Bq) dùng để đo",
   ["liều hấp thụ bức xạ.", "độ phóng xạ của một nguồn.",
    "năng lượng liên kết.", "khối lượng hạt nhân."],
   "B",
   "1 Bq ứng với một phân rã mỗi giây. Liều hấp thụ đo bằng gray (Gy), liều tương đương đo bằng "
   "sivơ (Sv).",
   "Đơn vị đo phóng xạ", D),

mc("Vì sao nước được dùng làm chất tải nhiệt trong nhiều hệ thống làm mát?",
   ["Vì nước có khối lượng riêng nhỏ.",
    "Vì nước có nhiệt dung riêng lớn nên chứa được nhiều nhiệt.",
    "Vì nước dẫn điện tốt.",
    "Vì nước sôi ở nhiệt độ thấp."],
   "B",
   "Nhiệt dung riêng của nước là 4200 J/(kg·K), thuộc loại lớn nhất trong các chất thông thường, "
   "nên cùng một khối lượng nước có thể mang đi rất nhiều nhiệt mà nhiệt độ tăng ít.",
   "Nhiệt dung riêng – thực tiễn", D),

mc("Bếp từ làm nóng nồi nhờ",
   ["bức xạ nhiệt từ mặt kính.", "dòng điện Foucault sinh ra trong đáy nồi.",
    "dẫn nhiệt trực tiếp từ cuộn dây.", "phản ứng hoá học."],
   "B",
   "Cuộn dây cao tần tạo từ trường biến thiên nhanh, làm xuất hiện dòng xoáy Foucault trong đáy nồi "
   "nhiễm từ; dòng này toả nhiệt ngay trong đáy nồi.",
   "Ứng dụng dòng Foucault", D, fig="t_sd_bep_tu", cap="Nguyên lí bếp từ"),
],
P2=[
ds("Người ta thả một miếng đồng khối lượng 0,20 kg ở 100 °C vào 0,50 kg nước ở 20 °C trong bình "
   "cách nhiệt. Cho c(đồng) = 380 J/(kg·K); c(nước) = 4200 J/(kg·K).",
   [("Miếng đồng toả nhiệt, nước thu nhiệt.", True,
     "Đúng. Nhiệt luôn truyền từ vật có nhiệt độ cao sang vật có nhiệt độ thấp."),
    ("Nhiệt độ khi cân bằng nằm trong khoảng từ 20 °C đến 100 °C.", True,
     "Đúng. Đây là phép kiểm tra bắt buộc với mọi bài cân bằng nhiệt."),
    ("Nhiệt độ khi cân bằng xấp xỉ 22,7 °C.", True,
     "Đúng. 0,20·380·(100 − t) = 0,50·4200·(t − 20) ⇒ 7600 − 76t = 2100t − 42 000 "
     "⇒ 2176t = 49 600 ⇒ t ≈ 22,8 °C, làm tròn được khoảng 22,7–22,8 °C."),
    ("Nước nóng lên rất nhiều vì khối lượng nước lớn hơn khối lượng đồng.", False,
     "Sai. Nước gần như không nóng lên, nguyên nhân chính là nhiệt dung riêng của nước lớn hơn "
     "đồng hơn 11 lần chứ không phải do khối lượng.")],
   "Phương trình cân bằng nhiệt", D, fig="n_sd_can_bang_nhiet",
   cap="Trao đổi nhiệt trong bình cách nhiệt"),

ds("Một bình kín thể tích không đổi chứa khí lí tưởng ở 27 °C, áp suất 2,0·10⁵ Pa.",
   [("Đây là điều kiện của quá trình đẳng tích.", True,
     "Đúng. Bình kín, thành cứng nên thể tích khí không đổi."),
    ("Khi đun nóng tới 327 °C, áp suất khí tăng lên 4,0·10⁵ Pa.", True,
     "Đúng. T₁ = 300 K, T₂ = 600 K ⇒ p₂ = 2,0·10⁵ · 600/300 = 4,0·10⁵ Pa."),
    ("Trong quá trình đun nóng đó, khí không thực hiện công.", True,
     "Đúng. Thể tích không đổi nên A = 0; toàn bộ nhiệt lượng làm tăng nội năng."),
    ("Khi đun nóng, mật độ phân tử khí trong bình tăng lên.", False,
     "Sai. Bình kín nên số phân tử và thể tích đều không đổi, do đó mật độ phân tử không đổi. "
     "Áp suất tăng là do phân tử chuyển động nhanh hơn.")],
   "Quá trình đẳng tích", D, fig="k_sd_binhkhi", cap="Khí trong bình kín"),

ds("Một cuộn dây gồm 200 vòng, diện tích mỗi vòng 30 cm², đặt vuông góc với từ trường đều. "
   "Cảm ứng từ giảm đều từ 0,40 T về 0 trong 0,20 s.",
   [("Diện tích mỗi vòng bằng 3,0·10⁻³ m².", True,
     "Đúng. 30 cm² = 30·10⁻⁴ m² = 3,0·10⁻³ m²."),
    ("Độ biến thiên từ thông qua mỗi vòng là 1,2·10⁻³ Wb.", True,
     "Đúng. |ΔΦ| = ΔB·S = 0,40 · 3,0·10⁻³ = 1,2·10⁻³ Wb."),
    ("Suất điện động cảm ứng trong cuộn dây bằng 1,2 V.", True,
     "Đúng. |e| = N·|ΔΦ|/Δt = 200 · 1,2·10⁻³/0,20 = 1,2 V."),
    ("Nếu số vòng dây giảm còn 100 vòng thì suất điện động vẫn bằng 1,2 V.", False,
     "Sai. Suất điện động tỉ lệ thuận với số vòng nên chỉ còn 0,60 V.")],
   "Định luật Faraday", D),

ds("Hạt nhân ¹³⁷₅₅Cs là một sản phẩm phân hạch phổ biến, phóng xạ β⁻ với chu kì bán rã 30 năm.",
   [("Hạt nhân này có 82 nơtron.", True,
     "Đúng. N = 137 − 55 = 82."),
    ("Sau phân rã β⁻, hạt nhân con có số khối 137 và điện tích 56.", True,
     "Đúng. β⁻ làm Z tăng 1 và A không đổi."),
    ("Sau 90 năm, độ phóng xạ của mẫu còn 12,5 % giá trị ban đầu.", True,
     "Đúng. n = 90/30 = 3 ⇒ còn 2⁻³ = 12,5 %."),
    ("Sau 60 năm, toàn bộ lượng ¹³⁷Cs đã phân rã hết.", False,
     "Sai. Sau 60 năm (2 chu kì) vẫn còn 25 % lượng ban đầu. Đây chính là lí do chất thải "
     "phóng xạ phải được lưu giữ hàng trăm năm.")],
   "Phóng xạ và chất thải hạt nhân", D),
],
P3=[
sa("Cần cung cấp bao nhiêu kilôjun để làm nóng chảy hoàn toàn 2,0 kg nước đá đang ở 0 °C? "
   "Cho λ = 3,4·10⁵ J/kg.",
   "680",
   "Q = m·λ = 2,0 · 3,4·10⁵ = 6,8·10⁵ J = 680 kJ.",
   "Nhiệt nóng chảy riêng", D),

sa("Một lượng khí có thể tích 5,0 L ở áp suất 2,0·10⁵ Pa. Nén đẳng nhiệt tới áp suất 5,0·10⁵ Pa. "
   "Thể tích khí lúc này bằng bao nhiêu lít?",
   "2",
   "p₁V₁ = p₂V₂ ⇒ V₂ = 2,0·10⁵ · 5,0/(5,0·10⁵) = 10/5,0 = 2,0 L.",
   "Định luật Boyle", D),

sa("Một khung dây phẳng diện tích 250 cm² đặt vuông góc với từ trường đều B = 0,80 T. "
   "Từ thông qua khung bằng bao nhiêu vêbe (làm tròn đến chữ số thập phân thứ hai)?",
   "0,02",
   "S = 250 cm² = 250·10⁻⁴ m² = 0,025 m².\n"
   "Φ = B·S = 0,80 · 0,025 = 0,020 Wb.",
   "Từ thông", D),

sa("Một dòng điện xoay chiều có cường độ cực đại 8,0 A. Cường độ hiệu dụng của dòng điện này bằng "
   "bao nhiêu ampe (làm tròn đến chữ số thập phân thứ hai)? Lấy √2 ≈ 1,414.",
   "5,66",
   "I = I₀/√2 = 8,0/1,414 ≈ 5,66 A.",
   "Giá trị hiệu dụng", D),

sa("Hạt nhân ²³⁵₉₂U phóng xạ α. Số khối của hạt nhân con bằng bao nhiêu?",
   "231",
   "Bảo toàn số khối: 235 = 4 + A ⇒ A = 231.\n"
   "Bảo toàn điện tích: 92 = 2 + Z ⇒ Z = 90, đó là hạt nhân thori ²³¹₉₀Th.",
   "Quy tắc dịch chuyển", D),

sa("Một hạt nhân có độ hụt khối 0,15 u. Năng lượng liên kết của hạt nhân đó bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)? Cho 1 u·c² = 931,5 MeV.",
   "139,73",
   "W(lk) = Δm · 931,5 = 0,15 · 931,5 = 139,725 ≈ 139,73 MeV.",
   "Năng lượng liên kết", D),
])


# =====================================================================  ĐỀ 03
DE3 = dict(
ma="TH-Đề 03", ten="ĐỀ THI THỬ SỐ 03", muc="Dễ → Trung bình",
trongtam="Đọc đồ thị, bài toán hai bước và tình huống thực tiễn",
P1=[
mc("Một bình nước nóng dùng điện có công suất 2000 W đun 4,0 kg nước. Bỏ qua hao phí, "
   "thời gian để nước tăng thêm 50 °C xấp xỉ",
   ["210 s.", "420 s.", "840 s.", "105 s."],
   "B",
   "Q = m·c·ΔT = 4,0 · 4200 · 50 = 840 000 J.\n"
   "t = Q/P = 840 000/2000 = 420 s (7 phút).",
   "Nhiệt lượng và công suất", TB, fig="n_sd_binhnuocnong", cap="Bình nước nóng dùng điện"),

mc("Đồ thị nhiệt độ theo thời gian của một chất được đun với công suất không đổi có một đoạn nằm "
   "ngang. Đoạn nằm ngang đó ứng với giai đoạn",
   ["chất đang nóng lên nhanh.", "chất đang chuyển thể.",
    "nguồn nhiệt bị ngắt.", "chất đang nguội đi."],
   "B",
   "Đoạn nằm ngang cho thấy nhiệt độ không đổi dù vẫn được cấp nhiệt liên tục — đó là đặc trưng "
   "của quá trình chuyển thể (nóng chảy hoặc sôi).",
   "Đọc đồ thị chuyển thể", D, fig="n_dt_nuocda", cap="Đồ thị nhiệt độ theo thời gian"),

mc("Cung cấp cho một khối khí nhiệt lượng 300 J, đồng thời khí sinh công 120 J. "
   "Độ biến thiên nội năng của khí bằng",
   ["+420 J.", "+180 J.", "−180 J.", "−420 J."],
   "B",
   "Khí THU nhiệt nên Q = +300 J; khí SINH công nên A = −120 J.\n"
   "ΔU = A + Q = −120 + 300 = +180 J.",
   "Định luật I nhiệt động lực học", TB, fig="n_sd_quy_uoc_dau", cap="Quy ước dấu của A và Q"),

mc("Hai chất lỏng có cùng khối lượng được đun bằng hai bếp giống hệt nhau. Sau cùng một thời gian, "
   "chất nào có nhiệt độ tăng nhiều hơn thì",
   ["nhiệt dung riêng lớn hơn.", "nhiệt dung riêng nhỏ hơn.",
    "khối lượng riêng lớn hơn.", "nhiệt độ sôi cao hơn."],
   "B",
   "Cùng nhiệt lượng và cùng khối lượng, từ ΔT = Q/(mc) thấy ΔT tỉ lệ nghịch với c. "
   "Chất tăng nhiệt độ nhiều hơn có nhiệt dung riêng nhỏ hơn.",
   "Nhiệt dung riêng", TB, fig="n_dt_batchat", cap="Đun ba chất bằng cùng một bếp"),

mc("Một lốp xe được bơm căng vào buổi sáng lúc trời mát. Đến trưa nắng, áp suất trong lốp",
   ["giảm vì khí giãn nở.", "tăng vì nhiệt độ khí tăng mà thể tích gần như không đổi.",
    "không đổi vì lốp kín.", "giảm vì khí thoát ra ngoài."],
   "B",
   "Lốp xe gần như có thể tích cố định nên quá trình là đẳng tích: p tỉ lệ thuận với T. "
   "Nhiệt độ tăng làm áp suất tăng, đó là lí do không nên bơm quá căng vào ngày nắng.",
   "Định luật Gay-Lussac – thực tiễn", TB, fig="k_sd_bomxe", cap="Bơm khí vào lốp xe"),

mc("Một khối khí lí tưởng có thể tích 4,0 L ở 27 °C. Nung nóng đẳng áp tới 127 °C, "
   "thể tích khí lúc này bằng",
   ["4,5 L.", "5,33 L.", "18,8 L.", "3,0 L."],
   "B",
   "Đẳng áp: V₁/T₁ = V₂/T₂ với T₁ = 300 K, T₂ = 400 K.\n"
   "V₂ = 4,0 · 400/300 ≈ 5,33 L.",
   "Định luật Charles", TB, fig="k_dt_charles", cap="Thể tích khí theo nhiệt độ"),

mc("Ở cùng một nhiệt độ, động năng tịnh tiến trung bình của phân tử khí hiđrô so với phân tử "
   "khí ôxi thì",
   ["lớn hơn 16 lần.", "bằng nhau.", "nhỏ hơn 16 lần.", "lớn hơn 4 lần."],
   "B",
   "W̄ₐ = 3/2·kT chỉ phụ thuộc nhiệt độ, không phụ thuộc loại khí. Vì vậy động năng trung bình "
   "bằng nhau; chỉ có TỐC ĐỘ trung bình của hiđrô lớn hơn 4 lần vì nó nhẹ hơn 16 lần.",
   "Động năng phân tử", TB, fig="k_dt_phan_bo_toc_do", cap="Phân bố tốc độ phân tử"),

mc("Một đoạn dây dẫn dài 20 cm mang dòng điện 4,0 A đặt vuông góc với từ trường đều. "
   "Lực từ tác dụng lên dây là 0,40 N. Cảm ứng từ của từ trường bằng",
   ["0,25 T.", "0,50 T.", "1,00 T.", "2,00 T."],
   "B",
   "B = F/(I·ℓ) = 0,40/(4,0 · 0,20) = 0,40/0,80 = 0,50 T.",
   "Lực từ – bài toán ngược", TB),

mc("Đưa nhanh một nam châm lại gần vòng dây kín rồi dừng lại. Trong vòng dây",
   ["dòng cảm ứng tồn tại mãi mãi.", "dòng cảm ứng chỉ tồn tại trong lúc nam châm chuyển động.",
    "không có dòng cảm ứng.", "dòng cảm ứng tăng dần sau khi nam châm dừng."],
   "B",
   "Dòng cảm ứng chỉ xuất hiện khi từ thông đang biến thiên, tức trong lúc nam châm chuyển động. "
   "Khi nam châm dừng, từ thông không đổi nên dòng biến mất ngay.",
   "Điều kiện có dòng cảm ứng", D, fig="t_sd_tn_faraday", cap="Thí nghiệm Faraday"),

mc("Một máy biến áp lí tưởng có N₁ = 1000 vòng, N₂ = 200 vòng, đặt dưới điện áp 220 V. "
   "Điện áp hiệu dụng ở cuộn thứ cấp bằng",
   ["22 V.", "44 V.", "110 V.", "1100 V."],
   "B",
   "U₂ = U₁·N₂/N₁ = 220 · 200/1000 = 220/5 = 44 V.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một dòng điện xoay chiều có biểu thức i = 3,0·cos(100πt) (A). Chu kì của dòng điện bằng",
   ["0,01 s.", "0,02 s.", "0,05 s.", "0,10 s."],
   "B",
   "ω = 100π ⇒ T = 2π/ω = 2π/(100π) = 0,02 s, tương ứng tần số 50 Hz.",
   "Dòng điện xoay chiều", D),

mc("Hạt nhân ⁷₃Li có khối lượng nhỏ hơn tổng khối lượng của 3 prôtôn và 4 nơtron riêng lẻ. "
   "Phần khối lượng chênh lệch đó",
   ["bị mất đi hoàn toàn.", "đã chuyển thành năng lượng liên kết.",
    "biến thành electron.", "là sai số của phép đo."],
   "B",
   "Đó chính là độ hụt khối. Khi các nuclêôn kết hợp lại, hệ toả ra năng lượng liên kết "
   "W(lk) = Δm·c².",
   "Độ hụt khối", TB, fig="h_sd_dohutkhoi", cap="Độ hụt khối của hạt nhân"),

mc("Hạt nhân X có năng lượng liên kết 90 MeV và số khối 10; hạt nhân Y có năng lượng liên kết "
   "160 MeV và số khối 20. Hạt nhân nào bền vững hơn?",
   ["Y, vì năng lượng liên kết lớn hơn.", "X, vì năng lượng liên kết riêng lớn hơn.",
    "Hai hạt nhân bền như nhau.", "Không so sánh được."],
   "B",
   "ε(X) = 90/10 = 9,0 MeV/nuclêôn;  ε(Y) = 160/20 = 8,0 MeV/nuclêôn.\n"
   "X có năng lượng liên kết riêng lớn hơn nên bền vững hơn.",
   "So sánh độ bền vững", TB, fig="h_dt_nllk_rieng", cap="Năng lượng liên kết riêng"),

mc("Một mẫu chất phóng xạ có chu kì bán rã 6,0 giờ. Sau 24 giờ, số hạt nhân còn lại bằng",
   ["1/8 ban đầu.", "1/16 ban đầu.", "1/4 ban đầu.", "1/32 ban đầu."],
   "B",
   "n = 24/6,0 = 4 chu kì ⇒ còn lại 2⁻⁴ = 1/16 số hạt ban đầu.",
   "Định luật phóng xạ", TB),

mc("Trong phân rã β⁻, hạt nhân con so với hạt nhân mẹ có",
   ["số khối giảm 4.", "số khối không đổi, điện tích tăng 1.",
    "số khối giảm 1.", "điện tích giảm 1."],
   "B",
   "β⁻ là dòng electron mang điện tích −e; để bảo toàn điện tích thì Z tăng 1, còn A không đổi "
   "vì electron có số khối bằng 0.",
   "Quy tắc dịch chuyển", D, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Người ta dùng tia γ từ nguồn ⁶⁰Co trong xạ trị ung thư vì tia γ",
   ["ion hoá mạnh nhất.", "đâm xuyên tốt nên tới được khối u nằm sâu.",
    "mang điện tích dương.", "có chu kì bán rã ngắn."],
   "B",
   "Tia γ có khả năng đâm xuyên lớn nhất nên tới được khối u nằm sâu trong cơ thể. "
   "Người ta chiếu từ nhiều hướng hội tụ vào khối u để hạn chế tổn thương mô lành.",
   "Ứng dụng trong y học", TB, fig="h_sd_ung_dung", cap="Ứng dụng của đồng vị phóng xạ"),

mc("Một khối khí lí tưởng thực hiện quá trình đẳng nhiệt. Nội năng của khối khí",
   ["tăng.", "không đổi.", "giảm.", "tăng rồi giảm."],
   "B",
   "Với khí lí tưởng, nội năng chỉ phụ thuộc nhiệt độ. Quá trình đẳng nhiệt có T không đổi nên "
   "ΔU = 0, do đó Q = −A: khí nhận bao nhiêu nhiệt thì sinh ra bấy nhiêu công.",
   "Nội năng của khí lí tưởng", TB),

mc("Lõi thép của máy biến áp được ghép từ nhiều lá mỏng cách điện với nhau nhằm",
   ["tăng từ thông qua lõi.", "giảm hao phí do dòng điện Foucault.",
    "tăng độ bền cơ học.", "giảm số vòng dây cần quấn."],
   "B",
   "Ghép lá mỏng cách điện cắt nhỏ đường đi khép kín của dòng xoáy trong lõi, làm giảm mạnh "
   "hao phí toả nhiệt.",
   "Dòng Foucault – tác hại", TB, fig="t_sd_dong_fuco", cap="Dòng điện Foucault"),
],
P2=[
ds("Thả 0,20 kg nước đá ở 0 °C vào 1,0 kg nước ở 30 °C trong bình cách nhiệt. "
   "Cho λ = 3,4·10⁵ J/kg; c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng cần để làm tan hết nước đá là 68 kJ.", True,
     "Đúng. Q = 0,20 · 3,4·10⁵ = 68 000 J = 68 kJ."),
    ("Nhiệt lượng tối đa mà nước có thể nhả ra khi hạ về 0 °C là 126 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 30 = 126 000 J = 126 kJ."),
    ("Nước đá tan hết và hỗn hợp có nhiệt độ cao hơn 0 °C.", True,
     "Đúng. Vì 126 kJ > 68 kJ nên nhiệt nước nhả ra đủ làm tan hết đá và còn dư để hâm nóng "
     "cả khối nước."),
    ("Nhiệt độ cân bằng của hỗn hợp là 0 °C.", False,
     "Sai. Chỉ khi nhiệt nhả ra KHÔNG đủ làm tan hết đá thì nhiệt độ cân bằng mới dừng ở 0 °C. "
     "Ở đây nhiệt dư nên nhiệt độ cân bằng cao hơn 0 °C (khoảng 11,5 °C).")],
   "Cân bằng nhiệt có chuyển thể", TB),

ds("Một lượng khí lí tưởng chuyển từ trạng thái 1 (p₁ = 1,0·10⁵ Pa; V₁ = 6,0 L; T₁ = 300 K) "
   "sang trạng thái 2 (V₂ = 3,0 L; T₂ = 450 K).",
   [("Lượng khí không đổi nên áp dụng được phương trình trạng thái.", True,
     "Đúng. Phương trình p₁V₁/T₁ = p₂V₂/T₂ chỉ đúng cho một lượng khí xác định."),
    ("Áp suất ở trạng thái 2 bằng 3,0·10⁵ Pa.", True,
     "Đúng. p₂ = p₁·(V₁/V₂)·(T₂/T₁) = 1,0·10⁵ · 2 · 1,5 = 3,0·10⁵ Pa."),
    ("Không cần đổi lít sang mét khối vì thể tích chỉ xuất hiện dưới dạng tỉ số.", True,
     "Đúng. Miễn là hai vế dùng cùng đơn vị thì kết quả không đổi."),
    ("Nhiệt độ có thể giữ nguyên đơn vị Celsius trong phép tính này.", False,
     "Sai. T bắt buộc phải tính bằng kelvin. Dùng Celsius (27 °C và 177 °C) sẽ cho tỉ số "
     "177/27 ≈ 6,6 thay vì 1,5, kết quả sai hoàn toàn.")],
   "Phương trình trạng thái", TB, fig="k_sd_ba_trang_thai", cap="Hai trạng thái của một lượng khí"),

ds("Một thanh dẫn dài 40 cm trượt đều với tốc độ 3,0 m/s trên hai ray nằm ngang, vuông góc với "
   "từ trường đều thẳng đứng B = 0,50 T. Điện trở toàn mạch 0,40 Ω.",
   [("Suất điện động cảm ứng trong mạch bằng 0,60 V.", True,
     "Đúng. e = B·ℓ·v = 0,50 · 0,40 · 3,0 = 0,60 V."),
    ("Cường độ dòng điện trong mạch bằng 1,5 A.", True,
     "Đúng. i = e/R = 0,60/0,40 = 1,5 A."),
    ("Lực từ tác dụng lên thanh có độ lớn 0,30 N và cản trở chuyển động.", True,
     "Đúng. F = B·i·ℓ = 0,50 · 1,5 · 0,40 = 0,30 N; theo định luật Lenz lực này ngược chiều "
     "chuyển động."),
    ("Nếu tăng tốc độ thanh lên gấp đôi thì lực từ cản cũng chỉ tăng gấp đôi về công suất toả "
     "nhiệt.", False,
     "Sai. Lực từ tăng gấp đôi nhưng công suất toả nhiệt P = e·i tăng gấp BỐN lần vì cả e và i "
     "đều tăng gấp đôi.")],
   "Thanh dẫn trượt trên ray", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

ds("Hạt nhân ⁴₂He có khối lượng 4,0015 u. Cho m(p) = 1,0073 u; m(n) = 1,0087 u; "
   "1 u·c² = 931,5 MeV.",
   [("Hạt nhân này gồm 2 prôtôn và 2 nơtron.", True,
     "Đúng. Z = 2 nên có 2 prôtôn; N = 4 − 2 = 2 nơtron."),
    ("Độ hụt khối của hạt nhân bằng 0,0305 u.", True,
     "Đúng. Δm = (2·1,0073 + 2·1,0087) − 4,0015 = 4,0320 − 4,0015 = 0,0305 u."),
    ("Năng lượng liên kết của hạt nhân xấp xỉ 28,4 MeV.", True,
     "Đúng. W(lk) = 0,0305 · 931,5 ≈ 28,4 MeV."),
    ("Muốn phá vỡ hạt nhân này thành các nuclêôn riêng lẻ thì hệ sẽ TOẢ ra 28,4 MeV.", False,
     "Sai. Phải CUNG CẤP đúng 28,4 MeV mới phá vỡ được hạt nhân. Năng lượng chỉ toả ra khi các "
     "nuclêôn kết hợp lại.")],
   "Độ hụt khối và năng lượng liên kết", TB, fig="h_sd_dohutkhoi", cap="Độ hụt khối"),
],
P3=[
sa("Một bếp điện công suất 1200 W đun 1,5 kg nước từ 25 °C tới khi sôi với hiệu suất 100 %. "
   "Thời gian đun bằng bao nhiêu giây? Cho c(nước) = 4200 J/(kg·K).",
   "394",
   "Q = 1,5 · 4200 · (100 − 25) = 1,5 · 4200 · 75 = 472 500 J.\n"
   "t = Q/P = 472 500/1200 = 393,75 ≈ 394 s.",
   "Nhiệt lượng và công suất", TB),

sa("Một lượng khí ở 27 °C có thể tích 3,0 L. Nung nóng đẳng áp tới 177 °C. "
   "Thể tích khí lúc này bằng bao nhiêu lít (làm tròn đến chữ số thập phân thứ nhất)?",
   "4,5",
   "T₁ = 300 K;  T₂ = 450 K.\n"
   "V₂ = V₁·T₂/T₁ = 3,0 · 450/300 = 4,5 L.",
   "Định luật Charles", TB),

sa("Một cuộn dây 500 vòng có từ thông qua mỗi vòng giảm đều từ 0,012 Wb về 0 trong 0,30 s. "
   "Độ lớn suất điện động cảm ứng bằng bao nhiêu vôn?",
   "20",
   "|e| = N·|ΔΦ|/Δt = 500 · 0,012/0,30 = 500 · 0,040 = 20 V.",
   "Định luật Faraday", TB),

sa("Truyền công suất 100 kW trên đường dây có điện trở 10 Ω ở điện áp hiệu dụng 10 kV. "
   "Công suất hao phí trên đường dây bằng bao nhiêu kilôoát?",
   "1",
   "I = P/U = 100 000/10 000 = 10 A.\n"
   "ΔP = R·I² = 10 · 10² = 1000 W = 1,0 kW.",
   "Hao phí truyền tải", TB),

sa("Cho phản ứng hạt nhân: ²⁷₁₃Al + ⁴₂He → ³⁰₁₅P + X. Số khối của hạt X bằng bao nhiêu?",
   "1",
   "Bảo toàn số khối: 27 + 4 = 30 + A ⇒ A = 1.\n"
   "Bảo toàn điện tích: 13 + 2 = 15 + Z ⇒ Z = 0. Vậy X là nơtron ¹₀n.",
   "Phản ứng hạt nhân", TB),

sa("Một mẫu chất phóng xạ có độ phóng xạ ban đầu 3200 Bq và chu kì bán rã 2,5 giờ. "
   "Sau 10 giờ, độ phóng xạ của mẫu bằng bao nhiêu becơren?",
   "200",
   "Số chu kì: n = 10/2,5 = 4.\n"
   "H = 3200/2⁴ = 3200/16 = 200 Bq.",
   "Độ phóng xạ", TB),
])


# =====================================================================  ĐỀ 04
DE4 = dict(
ma="TH-Đề 04", ten="ĐỀ THI THỬ SỐ 04", muc="Dễ → Trung bình",
trongtam="Bài toán hai bước, phân biệt các khái niệm dễ nhầm của cả bốn chương",
P1=[
mc("Khi đun một ấm nước, phần lớn nhiệt lượng cung cấp được dùng để",
   ["phá vỡ liên kết giữa các phân tử nước.", "làm tăng động năng chuyển động nhiệt của phân tử nước.",
    "làm tăng thế năng trọng trường của nước.", "làm nước bay hơi hoàn toàn."],
   "B",
   "Trong giai đoạn nước chưa sôi, nhiệt lượng làm tăng động năng chuyển động nhiệt của phân tử, "
   "biểu hiện ra ngoài là nhiệt độ tăng. Chỉ khi nước sôi, nhiệt lượng mới chuyển thành thế năng "
   "để tách phân tử khỏi khối chất lỏng.",
   "Nội năng và nhiệt độ", TB),

mc("Phát biểu nào sau đây về nhiệt độ là ĐÚNG?",
   ["Vật có nội năng lớn hơn thì nhiệt độ cao hơn.",
    "Nhiệt độ là thước đo động năng trung bình của phân tử.",
    "Nhiệt truyền từ vật có nội năng lớn sang vật có nội năng nhỏ.",
    "Hai vật cùng khối lượng thì có cùng nhiệt độ."],
   "B",
   "Nhiệt độ đo động năng TRUNG BÌNH của phân tử. Một bể nước 30 °C có nội năng lớn hơn cốc nước "
   "90 °C rất nhiều, nhưng nhiệt vẫn truyền từ cốc sang bể vì nhiệt truyền theo chênh lệch "
   "NHIỆT ĐỘ, không theo nội năng.",
   "Nhiệt độ và nội năng", TB),

mc("Đun nóng đẳng áp một lượng khí lí tưởng làm thể tích tăng 20 %. Nếu nhiệt độ ban đầu là 300 K "
   "thì nhiệt độ lúc sau bằng",
   ["320 K.", "360 K.", "250 K.", "375 K."],
   "B",
   "Đẳng áp: V tỉ lệ thuận với T.\n"
   "T₂ = T₁ · 1,20 = 300 · 1,20 = 360 K.",
   "Định luật Charles", TB),

mc("Một bóng bay chứa khí được đưa từ mặt đất lên cao, nơi áp suất khí quyển nhỏ hơn. "
   "Coi nhiệt độ không đổi, thể tích bóng sẽ",
   ["giảm.", "tăng.", "không đổi.", "giảm rồi tăng."],
   "B",
   "Áp suất bên ngoài giảm nên khí trong bóng giãn nở tới khi cân bằng: theo định luật Boyle, "
   "p giảm thì V tăng.",
   "Định luật Boyle – thực tiễn", TB, fig="k_sd_bongbay", cap="Bóng bay lên cao"),

mc("Trong hệ toạ độ (p, V), đường đẳng nhiệt ứng với nhiệt độ cao hơn nằm",
   ["gần gốc toạ độ hơn.", "xa gốc toạ độ hơn.",
    "trùng với trục hoành.", "cắt đường đẳng nhiệt kia."],
   "B",
   "Với cùng một thể tích, nhiệt độ càng cao thì áp suất càng lớn nên đường hypebol nằm xa gốc "
   "toạ độ hơn. Hai đường đẳng nhiệt không bao giờ cắt nhau.",
   "Đồ thị đẳng nhiệt", TB, fig="k_dt_dangnhiet", cap="Hai đường đẳng nhiệt"),

mc("Một xi lanh thẳng đứng có pit-tông tự do, bên trên đặt một quả nặng. Khi đun nóng khí bên trong, "
   "quá trình biến đổi trạng thái của khí là",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "đoạn nhiệt."],
   "B",
   "Pit-tông tự do nên luôn ở trạng thái cân bằng: p = p₀ + mg/S, cả ba đại lượng đều không đổi. "
   "Vậy áp suất khí không đổi — quá trình đẳng áp.",
   "Nhận dạng quá trình", TB, fig="k_sd_xilanh_quanang",
   cap="Xi lanh có quả nặng trên pit-tông"),

mc("Quy tắc bàn tay trái dùng để xác định chiều của",
   ["đường sức từ quanh dòng điện.", "lực từ tác dụng lên dòng điện.",
    "dòng điện cảm ứng.", "từ thông qua khung dây."],
   "B",
   "Đặt bàn tay trái sao cho đường sức xuyên vào lòng bàn tay, chiều từ cổ tay đến ngón giữa là "
   "chiều dòng điện, ngón cái choãi 90° chỉ chiều lực từ.",
   "Quy tắc bàn tay trái", D, fig="t_sd_luctu", cap="Lực từ tác dụng lên dây dẫn"),

mc("Một khung dây phẳng nằm trọn trong một vùng từ trường đều và chuyển động thẳng đều. "
   "Trong khung",
   ["luôn có dòng điện cảm ứng.", "không có dòng điện cảm ứng.",
    "có dòng cảm ứng tăng dần.", "có dòng cảm ứng đổi chiều liên tục."],
   "B",
   "Từ trường đều và khung nằm trọn bên trong nên B, S, góc đều không đổi, từ thông không biến thiên. "
   "Dòng chỉ xuất hiện lúc khung đi vào hoặc đi ra khỏi vùng từ trường.",
   "Điều kiện có dòng cảm ứng", TB, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường"),

mc("Một cuộn dây 100 vòng, diện tích mỗi vòng 20 cm², đặt vuông góc với từ trường đều. "
   "Cảm ứng từ tăng đều từ 0 lên 0,50 T trong 0,10 s. Suất điện động cảm ứng bằng",
   ["0,50 V.", "1,00 V.", "2,00 V.", "0,10 V."],
   "B",
   "S = 20 cm² = 2,0·10⁻³ m².\n"
   "|ΔΦ| mỗi vòng = 0,50 · 2,0·10⁻³ = 1,0·10⁻³ Wb.\n"
   "|e| = 100 · 1,0·10⁻³/0,10 = 1,00 V.",
   "Định luật Faraday", TB),

mc("Một máy biến áp lí tưởng hoạt động với điện áp sơ cấp 220 V. Nếu cường độ dòng điện ở cuộn "
   "sơ cấp là 0,50 A thì công suất mà máy nhận vào bằng",
   ["55 W.", "110 W.", "440 W.", "220 W."],
   "B",
   "P = U₁·I₁ = 220 · 0,50 = 110 W. Với máy lí tưởng, công suất ở thứ cấp cũng bằng 110 W.",
   "Máy biến áp – công suất", TB),

mc("Điện năng được truyền tải đi xa ở điện áp cao rồi hạ áp ở nơi tiêu thụ. Máy hạ áp có",
   ["số vòng thứ cấp nhiều hơn sơ cấp.", "số vòng thứ cấp ít hơn sơ cấp.",
    "hai cuộn dây bằng nhau.", "chỉ một cuộn dây."],
   "B",
   "Máy hạ áp có U₂ < U₁ nên N₂ < N₁. Đồng thời cường độ dòng điện ở thứ cấp lớn hơn ở sơ cấp.",
   "Máy biến áp", TB, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

mc("Số nơtron trong hạt nhân ²⁰⁶₈₂Pb bằng",
   ["82.", "124.", "206.", "288."],
   "B",
   "N = A − Z = 206 − 82 = 124 nơtron.",
   "Cấu tạo hạt nhân", D),

mc("Một hạt nhân phóng xạ α. Vị trí của hạt nhân con trong bảng tuần hoàn và số khối của nó "
   "thay đổi thế nào?",
   ["Lùi 4 ô, số khối giảm 2.", "Lùi 2 ô, số khối giảm 4.",
    "Tiến 2 ô, số khối giảm 4.", "Giữ nguyên ô, số khối giảm 4."],
   "B",
   "Phân rã α phát ra hạt ⁴₂He nên Z giảm 2 (lùi 2 ô trong bảng tuần hoàn) và A giảm 4.",
   "Quy tắc dịch chuyển", TB, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một chất phóng xạ có chu kì bán rã 3,0 ngày. Sau 9,0 ngày, khối lượng đã phân rã chiếm",
   ["12,5 % ban đầu.", "87,5 % ban đầu.", "25,0 % ban đầu.", "75,0 % ban đầu."],
   "B",
   "n = 9,0/3,0 = 3 ⇒ còn lại 12,5 % ⇒ đã rã 100 − 12,5 = 87,5 %. "
   "Đọc kĩ đề hỏi phần còn lại hay phần đã rã.",
   "Định luật phóng xạ", TB),

mc("Nhận định nào sau đây về phóng xạ là SAI?",
   ["Phóng xạ là quá trình tự phát.", "Phóng xạ luôn toả năng lượng.",
    "Tốc độ phóng xạ tăng khi nung nóng mẫu chất.",
    "Không dự đoán được thời điểm một hạt nhân cụ thể phân rã."],
   "C",
   "Phóng xạ xảy ra bên trong hạt nhân nên hoàn toàn không phụ thuộc nhiệt độ, áp suất hay "
   "trạng thái hoá học. Ba nhận định còn lại đều đúng.",
   "Đặc điểm của phóng xạ", TB),

mc("Trong lò phản ứng hạt nhân, nước thường có thể đóng vai trò",
   ["thanh điều khiển.", "chất làm chậm nơtron và chất tải nhiệt.",
    "nhiên liệu hạt nhân.", "lớp che chắn tia γ."],
   "B",
   "Nước có hạt nhân hiđrô rất nhẹ nên làm chậm nơtron hiệu quả, đồng thời có nhiệt dung riêng "
   "lớn nên tải nhiệt tốt. Thanh điều khiển làm bằng bo hoặc cađimi.",
   "Lò phản ứng hạt nhân", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Một khối kim loại và một khối nước có cùng khối lượng, cùng nhận một nhiệt lượng như nhau. "
   "So với nước, kim loại sẽ",
   ["nóng lên ít hơn.", "nóng lên nhiều hơn.",
    "nóng lên như nhau.", "không nóng lên."],
   "B",
   "ΔT = Q/(mc) tỉ lệ nghịch với nhiệt dung riêng. Kim loại có c nhỏ hơn nước nhiều lần nên "
   "nóng lên nhiều hơn hẳn.",
   "Nhiệt dung riêng", D),

mc("Trong một chu kì của dòng điện xoay chiều tần số 50 Hz, dòng điện đổi chiều",
   ["1 lần.", "2 lần.", "50 lần.", "100 lần."],
   "B",
   "Trong mỗi chu kì, cường độ dòng điện đi qua giá trị 0 và đổi chiều đúng 2 lần. "
   "Con số 100 là số lần đổi chiều trong MỘT GIÂY (50 chu kì).",
   "Dòng điện xoay chiều", TB),
],
P2=[
ds("Một nhiệt lượng kế chứa 0,80 kg nước ở 20 °C. Người ta thả vào đó một miếng kim loại khối "
   "lượng 0,50 kg ở 120 °C, nhiệt độ cân bằng là 25 °C. Bỏ qua nhiệt dung của nhiệt lượng kế. "
   "Cho c(nước) = 4200 J/(kg·K).",
   [("Nước thu nhiệt còn miếng kim loại toả nhiệt.", True,
     "Đúng. Kim loại nóng hơn nên toả nhiệt cho nước."),
    ("Nhiệt lượng nước thu vào là 16,8 kJ.", True,
     "Đúng. Q = 0,80 · 4200 · (25 − 20) = 0,80 · 4200 · 5 = 16 800 J = 16,8 kJ."),
    ("Nhiệt dung riêng của kim loại xấp xỉ 354 J/(kg·K).", True,
     "Đúng. 0,50 · c · (120 − 25) = 16 800 ⇒ 47,5·c = 16 800 ⇒ c ≈ 354 J/(kg·K)."),
    ("Kim loại đó có nhiệt dung riêng lớn hơn nước.", False,
     "Sai. 354 J/(kg·K) nhỏ hơn 4200 J/(kg·K) rất nhiều. Hầu hết kim loại đều có nhiệt dung riêng "
     "nhỏ hơn nước.")],
   "Thí nghiệm đo nhiệt dung riêng", TB, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

ds("Một lượng khí lí tưởng thực hiện chu trình gồm bốn đoạn: (1)→(2) đẳng tích, (2)→(3) đẳng áp, "
   "(3)→(4) đẳng tích, (4)→(1) đẳng áp. Ở trạng thái (1): V = 1,0 L; p = 1,0·10⁵ Pa; T = 300 K. "
   "Ở (2): p = 3,0·10⁵ Pa. Ở (3): V = 3,0 L.",
   [("Nhiệt độ ở trạng thái (2) bằng 900 K.", True,
     "Đúng. Đẳng tích: T₂ = T₁·p₂/p₁ = 300 · 3 = 900 K."),
    ("Nhiệt độ ở trạng thái (3) bằng 2700 K.", True,
     "Đúng. Đẳng áp: T₃ = T₂·V₃/V₂ = 900 · 3 = 2700 K."),
    ("Nhiệt độ ở trạng thái (4) bằng 900 K.", True,
     "Đúng. Đẳng tích từ (3) sang (4), áp suất giảm 3 lần nên T₄ = 2700/3 = 900 K."),
    ("Trong đoạn (1)→(2), khí sinh công.", False,
     "Sai. Đoạn (1)→(2) là đẳng tích nên thể tích không đổi, khí không sinh và cũng không nhận "
     "công: A = 0.")],
   "Chu trình kín của khí lí tưởng", TB, fig="k_dt_chutrinh", cap="Chu trình trong hệ (p, V)"),

ds("Một khung dây phẳng 300 vòng, diện tích mỗi vòng 40 cm², quay đều quanh trục vuông góc với "
   "từ trường đều B = 0,25 T, tốc độ 600 vòng/phút. Lấy π ≈ 3,1416.",
   [("Tần số của suất điện động là 10 Hz.", True,
     "Đúng. 600 vòng/phút = 10 vòng/giây."),
    ("Tần số góc xấp xỉ 62,8 rad/s.", True,
     "Đúng. ω = 2πf = 2 · 3,1416 · 10 ≈ 62,83 rad/s."),
    ("Suất điện động cực đại xấp xỉ 18,8 V.", True,
     "Đúng. E₀ = ω·N·B·S = 62,83 · 300 · 0,25 · 4,0·10⁻³ = 62,83 · 0,30 ≈ 18,85 V."),
    ("Suất điện động hiệu dụng xấp xỉ 26,7 V.", False,
     "Sai. E = E₀/√2 ≈ 18,85/1,414 ≈ 13,3 V. Giá trị 26,7 V là kết quả khi NHÂN với √2 "
     "thay vì chia.")],
   "Máy phát điện xoay chiều", TB, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

ds("Hạt nhân ²³⁸₉₂U phóng xạ α tạo thành hạt nhân thori, chu kì bán rã 4,5 tỉ năm.",
   [("Hạt nhân thori có kí hiệu ²³⁴₉₀Th.", True,
     "Đúng. A = 238 − 4 = 234; Z = 92 − 2 = 90."),
    ("Hạt nhân thori có 144 nơtron.", True,
     "Đúng. N = 234 − 90 = 144."),
    ("Sau 4,5 tỉ năm, một nửa lượng ²³⁸U ban đầu đã phân rã.", True,
     "Đúng. Đó chính là định nghĩa của chu kì bán rã."),
    ("Vì chu kì bán rã rất dài nên ²³⁸U có độ phóng xạ rất lớn.", False,
     "Sai. H = λN = (ln2/T)·N: chu kì bán rã càng dài thì λ càng nhỏ, độ phóng xạ càng THẤP. "
     "Đó là lí do urani tự nhiên tương đối an toàn khi cầm nắm ngắn hạn.")],
   "Phóng xạ và độ phóng xạ", TB, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),
],
P3=[
sa("Thả một miếng nhôm khối lượng 0,30 kg ở 100 °C vào 1,0 kg nước ở 20 °C. Nhiệt độ cân bằng "
   "bằng bao nhiêu độ Celsius (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho c(nhôm) = 880, c(nước) = 4200 J/(kg·K); bỏ qua nhiệt lượng bình thu vào.",
   "24,3",
   "0,30·880·(100 − t) = 1,0·4200·(t − 20)\n"
   "264·(100 − t) = 4200·(t − 20) ⇒ 26 400 − 264t = 4200t − 84 000\n"
   "4464t = 110 400 ⇒ t ≈ 24,3 °C.\n"
   "Kiểm tra: 20 < 24,3 < 100 — hợp lí.",
   "Phương trình cân bằng nhiệt", TB),

sa("Một khối khí ở 27 °C, áp suất 1,5·10⁵ Pa được nung nóng đẳng tích tới 177 °C. "
   "Áp suất khí lúc này bằng bao nhiêu (viết dưới dạng x·10⁵ Pa, chỉ ghi giá trị x, "
   "làm tròn đến chữ số thập phân thứ hai)?",
   "2,25",
   "T₁ = 300 K;  T₂ = 450 K.\n"
   "p₂ = p₁·T₂/T₁ = 1,5·10⁵ · 450/300 = 1,5·10⁵ · 1,5 = 2,25·10⁵ Pa.",
   "Định luật Gay-Lussac", TB),

sa("Một đoạn dây dẫn dài 30 cm mang dòng điện 5,0 A đặt trong từ trường đều B = 0,40 T, "
   "hợp với đường sức góc 30°. Lực từ tác dụng lên dây bằng bao nhiêu niutơn?",
   "0,3",
   "F = B·I·ℓ·sin30° = 0,40 · 5,0 · 0,30 · 0,50 = 0,30 N.",
   "Lực từ", TB),

sa("Một thanh dẫn dài 25 cm trượt đều với tốc độ 8,0 m/s vuông góc với từ trường đều B = 0,30 T. "
   "Suất điện động cảm ứng giữa hai đầu thanh bằng bao nhiêu vôn?",
   "0,6",
   "e = B·ℓ·v = 0,30 · 0,25 · 8,0 = 0,60 V.",
   "Thanh dẫn chuyển động", TB),

sa("Một hạt nhân có số khối 40 và năng lượng liên kết riêng 8,5 MeV/nuclêôn. "
   "Năng lượng liên kết của hạt nhân đó bằng bao nhiêu MeV?",
   "340",
   "W(lk) = ε·A = 8,5 · 40 = 340 MeV.",
   "Năng lượng liên kết", TB),

sa("Một mẫu chất phóng xạ ban đầu có 2,4·10²⁰ hạt nhân, chu kì bán rã 8,0 giờ. "
   "Sau 24 giờ, số hạt nhân đã phân rã bằng bao nhiêu (viết dưới dạng x·10²⁰, "
   "chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)?",
   "2,1",
   "Số chu kì: n = 24/8,0 = 3 ⇒ còn lại 2,4·10²⁰/8 = 0,3·10²⁰ hạt.\n"
   "Số hạt đã rã: 2,4·10²⁰ − 0,3·10²⁰ = 2,1·10²⁰ hạt.",
   "Định luật phóng xạ", TB),
])


# =====================================================================  ĐỀ 05
DE5 = dict(
ma="TH-Đề 05", ten="ĐỀ THI THỬ SỐ 05", muc="Trung bình",
trongtam="Vận dụng nhiều bước, bài toán hiệu suất và bài toán đồ thị",
P1=[
mc("Một bếp điện có hiệu suất 75 % dùng để đun 2,0 kg nước từ 20 °C tới 100 °C. "
   "Nhiệt lượng mà bếp phải toả ra bằng",
   ["504 kJ.", "896 kJ.", "672 kJ.", "840 kJ."],
   "B",
   "Nhiệt lượng có ích: Q(ci) = 2,0 · 4200 · 80 = 672 000 J = 672 kJ.\n"
   "Nhiệt lượng toàn phần: Q(tp) = Q(ci)/H = 672/0,75 = 896 kJ.\n"
   "Nhân với H thay vì chia sẽ ra 504 kJ — đó là bẫy quen thuộc.",
   "Hiệu suất đun nóng", TB, fig="n_sd_hieu_suat", cap="Dòng năng lượng khi đun nóng"),

mc("Để biến 0,50 kg nước đá ở 0 °C thành nước ở 20 °C cần nhiệt lượng "
   "(λ = 3,4·10⁵ J/kg; c = 4200 J/(kg·K))",
   ["170 kJ.", "212 kJ.", "42 kJ.", "128 kJ."],
   "B",
   "Giai đoạn 1 — làm tan hết đá: Q₁ = 0,50 · 3,4·10⁵ = 170 000 J.\n"
   "Giai đoạn 2 — hâm nước từ 0 °C lên 20 °C: Q₂ = 0,50 · 4200 · 20 = 42 000 J.\n"
   "Tổng: Q = 212 000 J = 212 kJ.",
   "Bài toán nhiều giai đoạn", TB),

mc("Nén đoạn nhiệt một khối khí, thực hiện lên khí công 500 J. Độ biến thiên nội năng của khí bằng",
   ["−500 J.", "+500 J.", "0.", "+1000 J."],
   "B",
   "Đoạn nhiệt nên Q = 0; khí bị nén nên nhận công A = +500 J.\n"
   "ΔU = A + Q = +500 J: nội năng tăng, nhiệt độ khí tăng.",
   "Định luật I nhiệt động lực học", TB),

mc("Nén một lượng khí lí tưởng từ 4,0 L xuống 2,0 L, đồng thời nung nóng khí từ 300 K lên 450 K. "
   "Biết áp suất ban đầu là 2,0·10⁵ Pa, áp suất lúc sau bằng",
   ["3,0·10⁵ Pa.", "6,0·10⁵ Pa.", "1,5·10⁵ Pa.", "9,0·10⁵ Pa."],
   "B",
   "p₂ = p₁ · (V₁/V₂) · (T₂/T₁) = 2,0·10⁵ · 2 · 1,5 = 6,0·10⁵ Pa.",
   "Phương trình trạng thái", TB),

mc("Một bình 10 L chứa khí ở 27 °C, áp suất 3,0·10⁵ Pa. Mở van cho khí thoát bớt tới khi áp suất "
   "còn 2,0·10⁵ Pa, nhiệt độ giữ nguyên. Phần khí đã thoát ra chiếm",
   ["50 % lượng khí ban đầu.", "33,3 % lượng khí ban đầu.",
    "66,7 % lượng khí ban đầu.", "20 % lượng khí ban đầu."],
   "B",
   "Với V và T không đổi, số mol khí trong bình tỉ lệ thuận với áp suất.\n"
   "n₂/n₁ = 2,0/3,0 = 0,667 ⇒ còn lại 66,7 %, đã thoát ra 33,3 %.",
   "Phương trình Clapeyron", K),

mc("Tính số mol khí có trong bình 8,31 L ở 27 °C và áp suất 2,0·10⁵ Pa "
   "(R = 8,31 J/(mol·K))",
   ["0,333 mol.", "0,667 mol.", "1,00 mol.", "2,00 mol."],
   "B",
   "Đổi đơn vị: V = 8,31·10⁻³ m³;  T = 300 K.\n"
   "n = pV/(RT) = (2,0·10⁵ · 8,31·10⁻³)/(8,31 · 300) = 1662/2493 ≈ 0,667 mol.",
   "Phương trình Clapeyron", K),

mc("Một khung dây phẳng diện tích 0,050 m² đặt trong từ trường đều B = 0,60 T, mặt phẳng khung "
   "hợp với đường sức góc 30°. Từ thông qua khung bằng",
   ["0,026 Wb.", "0,015 Wb.", "0,030 Wb.", "0,010 Wb."],
   "B",
   "Góc giữa pháp tuyến và B: θ = 90° − 30° = 60°.\n"
   "Φ = B·S·cos60° = 0,60 · 0,050 · 0,50 = 0,015 Wb.\n"
   "Dùng nhầm cos30° sẽ ra 0,026 Wb — bẫy phân biệt hai loại góc.",
   "Từ thông – phân biệt góc", TB, fig="t_sd_khung_nghieng", cap="Khung dây nghiêng"),

mc("Một thanh dẫn dài 50 cm trượt đều trên hai ray nằm ngang với tốc độ 4,0 m/s, vuông góc với "
   "từ trường đều thẳng đứng B = 0,40 T. Điện trở toàn mạch 0,50 Ω. Cường độ dòng điện trong mạch bằng",
   ["0,80 A.", "1,60 A.", "3,20 A.", "0,40 A."],
   "B",
   "e = B·ℓ·v = 0,40 · 0,50 · 4,0 = 0,80 V.\n"
   "i = e/R = 0,80/0,50 = 1,60 A.",
   "Thanh dẫn trượt trên ray", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Truyền công suất 200 kW đi xa trên đường dây có điện trở 5,0 Ω ở điện áp 20 kV. "
   "Hiệu suất truyền tải bằng",
   ["97,5 %.", "99,75 %.", "95,0 %.", "99,0 %."],
   "B",
   "I = P/U = 200 000/20 000 = 10 A.\n"
   "ΔP = R·I² = 5,0 · 100 = 500 W = 0,5 kW.\n"
   "H = (200 − 0,5)/200 = 0,9975 = 99,75 %.",
   "Hiệu suất truyền tải", TB, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một máy phát điện xoay chiều có rôto quay 3000 vòng/phút. Tần số của suất điện động bằng",
   ["25 Hz.", "50 Hz.", "60 Hz.", "100 Hz."],
   "B",
   "n = 3000/60 = 50 vòng/giây. Với máy một cặp cực, f = n = 50 Hz.",
   "Máy phát điện xoay chiều", TB),

mc("Đặt điện áp xoay chiều có giá trị hiệu dụng 200 V vào hai đầu điện trở 50 Ω. "
   "Công suất tiêu thụ trên điện trở bằng",
   ["400 W.", "800 W.", "1600 W.", "200 W."],
   "B",
   "P = U²/R = 200²/50 = 40 000/50 = 800 W. Dùng giá trị hiệu dụng nên công thức giống hệt "
   "dòng điện không đổi.",
   "Công suất dòng xoay chiều", TB),

mc("Hạt nhân ⁷₃Li có khối lượng 7,0160 u. Cho m(p) = 1,0073 u; m(n) = 1,0087 u; "
   "1 u·c² = 931,5 MeV. Năng lượng liên kết riêng của hạt nhân này xấp xỉ",
   ["37,9 MeV/nuclêôn.", "5,4 MeV/nuclêôn.",
    "7,1 MeV/nuclêôn.", "8,8 MeV/nuclêôn."],
   "B",
   "Δm = (3·1,0073 + 4·1,0087) − 7,0160 = 7,0567 − 7,0160 = 0,0407 u.\n"
   "W(lk) = 0,0407 · 931,5 ≈ 37,9 MeV.\n"
   "ε = 37,9/7 ≈ 5,4 MeV/nuclêôn. Giá trị 37,9 là năng lượng liên kết, không phải riêng.",
   "Năng lượng liên kết riêng", K),

mc("Một mẫu chất phóng xạ có chu kì bán rã 15 phút. Sau bao lâu thì độ phóng xạ còn 1/8 giá trị "
   "ban đầu?",
   ["30 phút.", "45 phút.", "60 phút.", "120 phút."],
   "B",
   "1/8 = 2⁻³ nên n = 3 chu kì.\n"
   "t = 3 · 15 = 45 phút.",
   "Định luật phóng xạ", TB),

mc("Cho phản ứng: ²₁H + ³₁H → ⁴₂He + ¹₀n với tổng khối lượng trước là 5,0296 u và sau là 5,0102 u. "
   "Năng lượng toả ra xấp xỉ",
   ["9,0 MeV.", "18,1 MeV.", "36,2 MeV.", "4,5 MeV."],
   "B",
   "Δm = 5,0296 − 5,0102 = 0,0194 u.\n"
   "ΔE = 0,0194 · 931,5 ≈ 18,1 MeV, và vì khối lượng giảm nên phản ứng TOẢ năng lượng.",
   "Năng lượng phản ứng hạt nhân", TB, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Số hạt nhân có trong 1,0 gam ²³⁸U (Nₐ = 6,02·10²³ mol⁻¹) xấp xỉ",
   ["2,53·10²².", "2,53·10²¹.", "6,02·10²³.", "2,38·10²³."],
   "B",
   "n = 1,0/238 ≈ 4,202·10⁻³ mol.\n"
   "N = 4,202·10⁻³ · 6,02·10²³ ≈ 2,53·10²¹ hạt.",
   "Số hạt nhân trong một khối lượng", TB),

mc("Một mẫu gỗ cổ còn 25 % lượng ¹⁴C so với gỗ tươi. Tuổi của mẫu gỗ bằng "
   "(chu kì bán rã của ¹⁴C là 5730 năm)",
   ["5730 năm.", "11 460 năm.", "17 190 năm.", "2865 năm."],
   "B",
   "25 % = 1/4 = 2⁻² nên n = 2 chu kì bán rã.\n"
   "t = 2 · 5730 = 11 460 năm.",
   "Xác định tuổi bằng cacbon-14", TB, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

mc("Trong một chu trình kín của khí lí tưởng, sau khi đi hết chu trình thì nội năng của khí",
   ["tăng.", "trở về giá trị ban đầu.", "giảm.", "bằng không."],
   "B",
   "Nội năng là hàm trạng thái, chỉ phụ thuộc trạng thái hiện tại. Đi hết chu trình kín, khí trở về "
   "đúng trạng thái ban đầu nên nội năng cũng trở về giá trị ban đầu: ΔU = 0.",
   "Chu trình kín", K, fig="k_dt_chutrinh", cap="Chu trình kín trong hệ (p, V)"),

mc("Một đoạn dây dẫn đặt trong từ trường đều, khi tăng góc giữa dây và đường sức từ từ 30° lên 90° "
   "thì lực từ tác dụng lên dây",
   ["giảm một nửa.", "tăng gấp đôi.", "không đổi.", "tăng gấp bốn."],
   "B",
   "F tỉ lệ với sinα. sin30° = 0,5 và sin90° = 1 nên lực từ tăng gấp đôi.",
   "Vai trò của góc α", TB, fig="t_sd_goc_alpha", cap="Dây hợp góc α với đường sức"),
],
P2=[
ds("Một ấm điện công suất 1500 W, hiệu suất 80 %, dùng để đun 2,0 kg nước từ 25 °C tới khi sôi. "
   "Cho c(nước) = 4200 J/(kg·K).",
   [("Nhiệt lượng có ích cần cung cấp là 630 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · (100 − 25) = 630 000 J."),
    ("Nhiệt lượng toàn phần mà ấm phải tiêu thụ là 787,5 kJ.", True,
     "Đúng. Q(tp) = 630/0,80 = 787,5 kJ."),
    ("Thời gian đun là 525 giây.", True,
     "Đúng. t = 787 500/1500 = 525 s ≈ 8 phút 45 giây."),
    ("Nếu hiệu suất tăng lên 100 % thì thời gian đun cũng tăng theo.", False,
     "Sai. Hiệu suất cao hơn nghĩa là ít hao phí hơn, nên thời gian đun GIẢM xuống còn "
     "630 000/1500 = 420 s.")],
   "Hiệu suất và công suất", TB),

ds("Một bình chứa khí nén dùng cho thợ lặn có thể tích 20 L, chứa khí lí tưởng ở 27 °C và "
   "áp suất 4,0·10⁵ Pa.",
   [("Nhiệt độ khí theo thang Kelvin là 300 K.", True,
     "Đúng. T = 27 + 273 = 300 K."),
    ("Nếu nung nóng đẳng tích tới 87 °C thì áp suất tăng lên 4,8·10⁵ Pa.", True,
     "Đúng. T₂ = 360 K ⇒ p₂ = 4,0·10⁵ · 360/300 = 4,8·10⁵ Pa."),
    ("Nếu mở van cho khí thoát bớt tới áp suất 3,0·10⁵ Pa ở nhiệt độ không đổi thì 25 % lượng khí "
     "ban đầu đã thoát ra.", True,
     "Đúng. Với V và T không đổi, số mol tỉ lệ với áp suất: còn lại 3,0/4,0 = 75 %, "
     "đã thoát ra 25 %."),
    ("Khi khí thoát bớt ra, vẫn có thể dùng phương trình p₁V₁/T₁ = p₂V₂/T₂ cho khí trong bình.", False,
     "Sai. Phương trình trạng thái chỉ áp dụng cho một LƯỢNG KHÍ KHÔNG ĐỔI. Khi khí thoát ra "
     "phải dùng phương trình Clapeyron pV = nRT cho từng thời điểm.")],
   "Phương trình Clapeyron", K),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 1100 vòng mắc vào mạng 220 V, cuộn thứ cấp 100 vòng "
   "nối với điện trở thuần 10 Ω.",
   [("Điện áp hiệu dụng ở cuộn thứ cấp bằng 20 V.", True,
     "Đúng. U₂ = 220 · 100/1100 = 20 V."),
    ("Cường độ dòng điện qua điện trở bằng 2,0 A.", True,
     "Đúng. I₂ = U₂/R = 20/10 = 2,0 A."),
    ("Công suất tiêu thụ ở mạch thứ cấp bằng 40 W.", True,
     "Đúng. P₂ = U₂·I₂ = 20 · 2,0 = 40 W."),
    ("Cường độ dòng điện ở cuộn sơ cấp cũng bằng 2,0 A.", False,
     "Sai. Máy lí tưởng bảo toàn công suất: I₁ = 40/220 ≈ 0,18 A, nhỏ hơn I₂ đúng 11 lần "
     "theo tỉ số vòng dây.")],
   "Máy biến áp có tải", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Hạt nhân ²¹⁰₈₄Po phóng xạ α với chu kì bán rã 138 ngày, tạo thành hạt nhân chì bền.",
   [("Hạt nhân chì tạo thành là ²⁰⁶₈₂Pb.", True,
     "Đúng. A = 210 − 4 = 206; Z = 84 − 2 = 82."),
    ("Sau 138 ngày, một nửa số hạt nhân pôlôni đã biến thành chì.", True,
     "Đúng. Đó chính là ý nghĩa của chu kì bán rã."),
    ("Sau 414 ngày, tỉ số số hạt nhân chì trên số hạt nhân pôlôni còn lại bằng 7.", True,
     "Đúng. n = 414/138 = 3 ⇒ Po còn N₀/8, Pb có 7N₀/8, tỉ số bằng 7."),
    ("Tỉ số KHỐI LƯỢNG chì trên khối lượng pôlôni sau 414 ngày cũng đúng bằng 7.", False,
     "Sai. Phải nhân thêm tỉ số số khối: (206/210)·7 ≈ 6,87, không bằng đúng 7.")],
   "Tỉ số hạt nhân con và mẹ", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),
],
P3=[
sa("Một bếp có hiệu suất 60 % dùng để đun 1,5 kg nước từ 30 °C tới 100 °C. Nhiệt lượng mà bếp phải "
   "toả ra bằng bao nhiêu kilôjun?",
   "735",
   "Nhiệt lượng có ích: Q(ci) = 1,5 · 4200 · 70 = 441 000 J = 441 kJ.\n"
   "Nhiệt lượng toàn phần: Q(tp) = 441/0,60 = 735 kJ.",
   "Hiệu suất đun nóng", TB),

sa("Một bình 5,0 L chứa khí ở áp suất 6,0·10⁵ Pa và nhiệt độ 27 °C. Mở van cho khí thoát bớt tới "
   "áp suất 2,0·10⁵ Pa ở cùng nhiệt độ. Phần trăm lượng khí đã thoát ra bằng bao nhiêu phần trăm?",
   "66,7",
   "V và T không đổi nên số mol khí tỉ lệ thuận với áp suất.\n"
   "Còn lại: 2,0/6,0 = 0,3333 = 33,3 %.\n"
   "Đã thoát ra: 100 − 33,3 = 66,7 %.",
   "Phương trình Clapeyron", K),

sa("Một khung dây 400 vòng, diện tích mỗi vòng 50 cm², quay đều quanh trục vuông góc với từ trường "
   "đều B = 0,30 T, tần số 50 Hz. Suất điện động cực đại bằng bao nhiêu vôn "
   "(làm tròn đến hàng đơn vị)? Lấy π ≈ 3,1416.",
   "188",
   "ω = 2πf = 2 · 3,1416 · 50 ≈ 314,16 rad/s.\n"
   "S = 50 cm² = 5,0·10⁻³ m².\n"
   "E₀ = ω·N·B·S = 314,16 · 400 · 0,30 · 5,0·10⁻³ = 314,16 · 0,60 ≈ 188 V.",
   "Máy phát điện xoay chiều", TB),

sa("Truyền công suất 400 kW trên đường dây có điện trở 4,0 Ω ở điện áp 40 kV. "
   "Công suất hao phí bằng bao nhiêu oát?",
   "400",
   "I = P/U = 400 000/40 000 = 10 A.\n"
   "ΔP = R·I² = 4,0 · 100 = 400 W.",
   "Hao phí truyền tải", TB),

sa("Hạt nhân ¹²₆C có khối lượng 11,9967 u. Độ hụt khối của hạt nhân này bằng bao nhiêu u "
   "(làm tròn đến chữ số thập phân thứ tư)? Cho m(p) = 1,0073 u; m(n) = 1,0087 u.",
   "0,0993",
   "Hạt nhân ¹²₆C có 6 prôtôn và 6 nơtron.\n"
   "Tổng khối lượng nuclêôn riêng lẻ: 6 · 1,0073 + 6 · 1,0087 = 6,0438 + 6,0522 = 12,0960 u.\n"
   "Δm = 12,0960 − 11,9967 = 0,0993 u.",
   "Độ hụt khối", TB),

sa("Một mẫu chất phóng xạ có chu kì bán rã 12 ngày. Sau bao nhiêu ngày thì số hạt nhân còn lại "
   "bằng 1/32 số hạt nhân ban đầu?",
   "60",
   "1/32 = 2⁻⁵ nên n = 5 chu kì bán rã.\n"
   "t = 5 · 12 = 60 ngày.",
   "Định luật phóng xạ", TB),
])


NHOM = dict(
    ten_nhom="ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 – TỔNG HỢP BỐN CHƯƠNG  (Đề 01 – 05)",
    mo_ta="Năm đề đầu tiên của bộ 30 đề, mức Dễ đến Trung bình – dùng để làm quen cấu trúc đề thi",
    pham_vi=(
        "Chương I. Vật lí nhiệt  •  Chương II. Khí lí tưởng  •  "
        "Chương III. Từ trường  •  Chương IV. Vật lí hạt nhân\n"
        "Mỗi đề gồm 28 câu / 40 lệnh hỏi, thời gian 50 phút, thang điểm 10, "
        "phân bố đều bốn chương.\n"
        "Hằng số: c(nước) = 4200 J/(kg·K); λ(nước đá) = 3,4·10⁵ J/kg; g = 10 m/s²; "
        "R = 8,31 J/(mol·K); Nₐ = 6,02·10²³ mol⁻¹; 1 u·c² = 931,5 MeV; π ≈ 3,1416; √2 ≈ 1,414."),
    tests=[DE1, DE2, DE3, DE4, DE5],
)
