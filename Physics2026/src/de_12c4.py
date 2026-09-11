# -*- coding: utf-8 -*-
"""LỚP 12 – CHƯƠNG 4: VẬT LÍ HẠT NHÂN.  10 đề luyện tập, độ khó tăng dần.

Hằng số dùng thống nhất trong cả bộ:
  1 u = 1,66055·10⁻²⁷ kg;  1 u·c² = 931,5 MeV;  c = 3,0·10⁸ m/s
  m(p) = 1,0073 u;  m(n) = 1,0087 u;  m(e) = 0,00055 u
  Nₐ = 6,02·10²³ mol⁻¹;  1 MeV = 1,6·10⁻¹³ J;  ln2 ≈ 0,693
"""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 1
DE1 = dict(
ma="12C4-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Nhận biết cấu tạo hạt nhân, ba loại tia phóng xạ và các công thức cơ bản",
P1=[
mc("Hạt nhân nguyên tử được cấu tạo từ",
   ["prôtôn và electron.", "prôtôn và nơtron.",
    "nơtron và electron.", "chỉ gồm prôtôn."],
   "B",
   "Hạt nhân gồm các nuclêôn: prôtôn mang điện tích dương và nơtron không mang điện. "
   "Electron chuyển động bên ngoài hạt nhân, không thuộc cấu tạo hạt nhân.",
   "Cấu tạo hạt nhân", D, fig="h_sd_cautruc", cap="Cấu tạo hạt nhân"),

mc("Trong kí hiệu hạt nhân, số Z ghi ở phía dưới bên trái kí hiệu nguyên tố cho biết",
   ["số nơtron trong hạt nhân.", "số prôtôn trong hạt nhân.",
    "tổng số nuclêôn.", "khối lượng của hạt nhân."],
   "B",
   "Z là số prôtôn, cũng chính là số thứ tự của nguyên tố trong bảng tuần hoàn. "
   "A là tổng số nuclêôn (số khối), còn số nơtron bằng N = A − Z.",
   "Kí hiệu hạt nhân", D),

mc("Hạt nhân ²³₁₁Na có bao nhiêu nơtron?",
   ["11 nơtron.", "12 nơtron.", "23 nơtron.", "34 nơtron."],
   "B",
   "Số nơtron N = A − Z = 23 − 11 = 12.",
   "Đếm nuclêôn", D),

mc("Các đồng vị của cùng một nguyên tố hoá học có",
   ["cùng số nơtron nhưng khác số prôtôn.",
    "cùng số prôtôn nhưng khác số nơtron.",
    "cùng số khối nhưng khác số prôtôn.",
    "khác cả số prôtôn lẫn số nơtron."],
   "B",
   "Đồng vị có cùng Z (nên cùng tính chất hoá học) nhưng khác số nơtron, do đó khác số khối A. "
   "Ví dụ ¹²C và ¹⁴C đều có Z = 6.",
   "Đồng vị", D),

mc("Đơn vị khối lượng nguyên tử u được định nghĩa bằng",
   ["khối lượng của một prôtôn.",
    "1/12 khối lượng của một nguyên tử đồng vị ¹²C.",
    "khối lượng của một nguyên tử hiđrô.",
    "1/16 khối lượng của một nguyên tử ôxi."],
   "B",
   "1 u = 1/12 khối lượng nguyên tử ¹²C ≈ 1,66055·10⁻²⁷ kg. "
   "Đây là đơn vị tiện dụng vì khối lượng mọi hạt nhân tính theo u đều xấp xỉ số khối A.",
   "Đơn vị khối lượng nguyên tử", D),

mc("Hệ thức liên hệ giữa đơn vị u và năng lượng là",
   ["1 u·c² = 931,5 eV.", "1 u·c² = 931,5 MeV.",
    "1 u·c² = 931,5 J.", "1 u·c² = 931,5 keV."],
   "B",
   "1 u·c² = 931,5 MeV. Hệ thức này cho phép đổi trực tiếp độ hụt khối tính bằng u sang năng lượng "
   "tính bằng MeV mà không cần nhân với c².",
   "Đổi đơn vị khối lượng – năng lượng", D),

mc("Độ hụt khối của một hạt nhân là",
   ["hiệu giữa khối lượng hạt nhân và khối lượng nguyên tử.",
    "hiệu giữa tổng khối lượng các nuclêôn riêng lẻ và khối lượng hạt nhân.",
    "tổng khối lượng của các prôtôn.",
    "khối lượng của các electron bị mất đi."],
   "B",
   "Δm = Z·m(p) + (A − Z)·m(n) − m(X). Phần khối lượng hụt đi đã chuyển thành năng lượng liên kết "
   "toả ra khi các nuclêôn kết hợp lại.",
   "Độ hụt khối", D, fig="h_sd_dohutkhoi", cap="Độ hụt khối của hạt nhân"),

mc("Năng lượng liên kết của hạt nhân được tính bằng công thức",
   ["W = Δm/c².", "W = Δm·c².", "W = Δm·c.", "W = m·c²."],
   "B",
   "W(lk) = Δm·c², trong đó Δm là độ hụt khối. Nếu Δm tính bằng u thì chỉ cần nhân với 931,5 "
   "để có kết quả theo MeV.",
   "Năng lượng liên kết", D),

mc("Đại lượng đặc trưng cho MỨC ĐỘ BỀN VỮNG của hạt nhân là",
   ["năng lượng liên kết.", "năng lượng liên kết riêng.",
    "độ hụt khối.", "số khối."],
   "B",
   "Năng lượng liên kết riêng ε = W(lk)/A mới là thước đo độ bền vững, vì nó tính trên MỘT nuclêôn. "
   "Hạt nhân nặng có W(lk) lớn nhưng chưa chắc bền hơn.",
   "Năng lượng liên kết riêng", D, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Tia α là",
   ["dòng electron.", "hạt nhân ⁴₂He.",
    "sóng điện từ.", "dòng prôtôn."],
   "B",
   "Tia α chính là dòng hạt nhân heli ⁴₂He, mang điện tích +2e. "
   "Dòng electron là tia β⁻, còn sóng điện từ là tia γ.",
   "Ba loại tia phóng xạ", D, fig="h_sd_tia_phongxa", cap="Ba loại tia phóng xạ"),

mc("Tia nào sau đây KHÔNG bị lệch trong điện trường?",
   ["Tia α.", "Tia γ.", "Tia β⁻.", "Tia β⁺."],
   "B",
   "Tia γ là sóng điện từ, không mang điện tích nên không chịu lực điện và đi thẳng. "
   "Ba tia còn lại đều mang điện nên bị lệch.",
   "Ba loại tia phóng xạ", D, fig="h_sd_tia_phongxa", cap="Ba tia trong điện trường"),

mc("Sắp xếp nào sau đây đúng về khả năng ĐÂM XUYÊN của ba loại tia phóng xạ?",
   ["α > β > γ.", "α < β < γ.", "β < α < γ.", "γ < β < α."],
   "B",
   "Khả năng đâm xuyên tăng dần α < β < γ: tia α bị tờ giấy chặn lại, tia β bị lá nhôm vài "
   "milimét chặn, còn tia γ phải cần lớp chì dày. Khả năng ion hoá thì ngược lại.",
   "Khả năng đâm xuyên", D, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),

mc("Trong phân rã α, so với hạt nhân mẹ, hạt nhân con có",
   ["Z giảm 2 và A giảm 4.", "Z giảm 4 và A giảm 2.",
    "Z tăng 1 và A không đổi.", "Z và A đều không đổi."],
   "A",
   "Phân rã α phát ra hạt ⁴₂He nên số khối giảm 4 và điện tích giảm 2 đơn vị, "
   "theo đúng hai định luật bảo toàn A và Z.",
   "Quy tắc dịch chuyển", D, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Chu kì bán rã T của một chất phóng xạ là khoảng thời gian để",
   ["toàn bộ số hạt nhân bị phân rã.",
    "một nửa số hạt nhân ban đầu bị phân rã.",
    "số hạt nhân giảm còn một phần tư.",
    "độ phóng xạ tăng gấp đôi."],
   "B",
   "Sau mỗi chu kì bán rã, số hạt nhân chưa phân rã giảm đi một nửa. "
   "Sau 2T mới còn một phần tư.",
   "Chu kì bán rã", D, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),

mc("Định luật phóng xạ được biểu diễn bằng công thức (đặt n = t/T)",
   ["N = N₀·2ⁿ.", "N = N₀·2⁻ⁿ.", "N = N₀·n.", "N = N₀/n."],
   "B",
   "N = N₀·2⁻ⁿ với n = t/T, tương đương N = N₀·e^(−λt) với λ = ln2/T. "
   "Số hạt nhân giảm theo quy luật hàm mũ chứ không giảm đều.",
   "Định luật phóng xạ", D),

mc("Quá trình phóng xạ KHÔNG phụ thuộc vào yếu tố nào sau đây?",
   ["Bản chất của đồng vị phóng xạ.", "Nhiệt độ và áp suất bên ngoài.",
    "Số hạt nhân ban đầu.", "Chu kì bán rã của chất đó."],
   "B",
   "Phóng xạ xảy ra bên trong hạt nhân nên hoàn toàn không phụ thuộc các tác động bên ngoài như "
   "nhiệt độ, áp suất hay trạng thái liên kết hoá học. Đây là điểm khác biệt cơ bản so với "
   "phản ứng hoá học.",
   "Đặc điểm của phóng xạ", D),

mc("Phản ứng phân hạch là phản ứng trong đó",
   ["hai hạt nhân nhẹ kết hợp thành hạt nhân nặng hơn.",
    "một hạt nhân rất nặng vỡ thành hai hạt nhân trung bình.",
    "một hạt nhân tự phát biến đổi và phát ra tia phóng xạ.",
    "electron bị bứt ra khỏi nguyên tử."],
   "B",
   "Phân hạch: hạt nhân rất nặng như ²³⁵U hấp thụ nơtron chậm rồi vỡ thành hai hạt nhân trung bình, "
   "đồng thời phát ra 2–3 nơtron mới. Phương án đầu mô tả phản ứng nhiệt hạch.",
   "Phân hạch", D, fig="h_sd_phan_hach", cap="Phản ứng phân hạch dây chuyền"),

mc("Phản ứng nhiệt hạch đòi hỏi điều kiện nào sau đây?",
   ["Nhiệt độ rất thấp, gần độ không tuyệt đối.",
    "Nhiệt độ rất cao, cỡ hàng trăm triệu độ.",
    "Áp suất khí quyển bình thường.",
    "Có nơtron chậm bắn vào."],
   "B",
   "Hai hạt nhân nhẹ đều mang điện dương nên đẩy nhau rất mạnh. Muốn chúng lại gần đủ để kết hợp, "
   "cần động năng rất lớn, tức nhiệt độ cỡ 10⁸ K. Nơtron chậm là điều kiện của phân hạch.",
   "Nhiệt hạch", D, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),
],
P2=[
ds("Xét hạt nhân ²³⁵₉₂U.",
   [("Hạt nhân này có 92 prôtôn.", True,
     "Đúng. Z = 92 chính là số prôtôn."),
    ("Hạt nhân này có 143 nơtron.", True,
     "Đúng. N = A − Z = 235 − 92 = 143."),
    ("Tổng số nuclêôn của hạt nhân là 327.", False,
     "Sai. Tổng số nuclêôn chính là số khối A = 235. Con số 327 là kết quả cộng nhầm 235 với 92."),
    ("Hạt nhân này và hạt nhân ²³⁸₉₂U là hai đồng vị của cùng một nguyên tố.", True,
     "Đúng. Cả hai đều có Z = 92 nhưng khác số khối, nên là hai đồng vị của urani.")],
   "Cấu tạo hạt nhân", D),

ds("Xét ba loại tia phóng xạ α, β và γ.",
   [("Tia α là dòng hạt nhân heli, mang điện tích dương.", True,
     "Đúng. Tia α chính là hạt nhân ⁴₂He với điện tích +2e."),
    ("Tia β⁻ là dòng electron, mang điện tích âm.", True,
     "Đúng. Đó là các electron phát ra từ hạt nhân trong phân rã β⁻."),
    ("Tia γ có khả năng ion hoá môi trường mạnh nhất trong ba loại tia.", False,
     "Sai. Tia γ có khả năng ion hoá YẾU nhất nhưng đâm xuyên MẠNH nhất. Tia α mới là tia "
     "ion hoá mạnh nhất."),
    ("Trong cùng một điện trường, tia α lệch ít hơn tia β.", True,
     "Đúng. Tuy điện tích của α lớn gấp đôi, khối lượng của nó lớn hơn electron khoảng 7000 lần "
     "nên gia tốc nhỏ hơn nhiều, do đó lệch ít hơn.")],
   "Ba loại tia phóng xạ", D, fig="h_sd_tia_phongxa", cap="Ba tia trong điện trường"),

ds("Một mẫu chất phóng xạ có chu kì bán rã T.",
   [("Sau thời gian T, số hạt nhân chưa phân rã còn lại một nửa so với ban đầu.", True,
     "Đúng. Đó chính là định nghĩa của chu kì bán rã."),
    ("Sau thời gian 2T, số hạt nhân chưa phân rã còn lại một phần tư.", True,
     "Đúng. Mỗi chu kì giảm một nửa nên sau hai chu kì còn (1/2)² = 1/4."),
    ("Sau thời gian 2T, toàn bộ số hạt nhân đã phân rã hết.", False,
     "Sai. Sau 2T vẫn còn 25 % số hạt nhân ban đầu. Về lí thuyết số hạt nhân giảm theo hàm mũ "
     "và không bao giờ bằng đúng 0."),
    ("Chu kì bán rã là đại lượng đặc trưng cho từng đồng vị phóng xạ.", True,
     "Đúng. Mỗi đồng vị có một chu kì bán rã xác định, không thay đổi theo điều kiện bên ngoài.")],
   "Định luật phóng xạ", D, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),

ds("So sánh phản ứng phân hạch và phản ứng nhiệt hạch.",
   [("Phân hạch xảy ra với hạt nhân rất nặng, nhiệt hạch xảy ra với hạt nhân rất nhẹ.", True,
     "Đúng. Nhìn vào đường cong năng lượng liên kết riêng: cả hai loại phản ứng đều đi TỚI vùng "
     "đỉnh nên đều toả năng lượng."),
    ("Cả hai loại phản ứng đều toả năng lượng.", True,
     "Đúng. Các hạt nhân sau phản ứng đều bền vững hơn các hạt nhân trước."),
    ("Tính trên mỗi nuclêôn, nhiệt hạch toả nhiều năng lượng hơn phân hạch.", True,
     "Đúng. Khoảng 3,5 MeV/nuclêôn so với 0,85 MeV/nuclêôn."),
    ("Con người đã điều khiển được phản ứng nhiệt hạch để sản xuất điện thương mại.", False,
     "Sai. Mới chỉ điều khiển được phản ứng phân hạch trong lò phản ứng hạt nhân. "
     "Nhiệt hạch có kiểm soát vẫn đang trong giai đoạn nghiên cứu.")],
   "Phân hạch và nhiệt hạch", D),
],
P3=[
sa("Một hạt nhân được cấu tạo từ 26 prôtôn và 30 nơtron. Số khối của hạt nhân đó bằng bao nhiêu?",
   "56",
   "Số khối bằng tổng số nuclêôn: A = Z + N = 26 + 30 = 56.\n"
   "Đó là hạt nhân sắt ⁵⁶₂₆Fe — hạt nhân bền vững vào loại nhất trong tự nhiên.",
   "Đếm nuclêôn", D),

sa("Một hạt nhân có độ hụt khối 0,20 u. Năng lượng liên kết của hạt nhân đó bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho 1 u·c² = 931,5 MeV.",
   "186,3",
   "W(lk) = Δm·c² = 0,20 · 931,5 = 186,3 MeV.",
   "Năng lượng liên kết", D),

sa("Một hạt nhân có số khối A = 16 và năng lượng liên kết 128 MeV. Năng lượng liên kết riêng của "
   "hạt nhân đó bằng bao nhiêu MeV trên một nuclêôn?",
   "8",
   "ε = W(lk)/A = 128/16 = 8,0 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", D),

sa("Một mẫu chất phóng xạ có chu kì bán rã 6,0 giờ. Sau 18 giờ, số hạt nhân chưa phân rã còn lại "
   "bằng bao nhiêu phần trăm so với ban đầu (làm tròn đến hàng đơn vị)?",
   "12",
   "Số chu kì đã trôi qua: n = 18/6,0 = 3.\n"
   "Tỉ lệ còn lại: 2⁻³ = 1/8 = 0,125 = 12,5 % ≈ 12 %.",
   "Định luật phóng xạ", D),

sa("Hạt nhân ²²⁶₈₈Ra phóng xạ α tạo thành hạt nhân con. Số khối của hạt nhân con bằng bao nhiêu?",
   "222",
   "Bảo toàn số khối: 226 = 4 + A ⇒ A = 222.\n"
   "Bảo toàn điện tích: 88 = 2 + Z ⇒ Z = 86, đó là hạt nhân radon ²²²₈₆Rn.",
   "Quy tắc dịch chuyển", D, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

sa("Ban đầu có 800 gam một chất phóng xạ có chu kì bán rã 5,0 ngày. Sau 15 ngày, khối lượng chất "
   "phóng xạ còn lại bằng bao nhiêu gam?",
   "100",
   "Số chu kì: n = 15/5,0 = 3.\n"
   "m = m₀·2⁻³ = 800/8 = 100 g.",
   "Định luật phóng xạ", D),
])


# =====================================================================  ĐỀ 2
DE2 = dict(
ma="12C4-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Củng cố khái niệm, viết phương trình phân rã và vận dụng công thức một bước",
P1=[
mc("Khối lượng của một prôtôn xấp xỉ",
   ["1,0073 u.", "1,0087 u.", "0,00055 u.", "12 u."],
   "A",
   "m(p) ≈ 1,0073 u; m(n) ≈ 1,0087 u (nơtron nặng hơn prôtôn một chút); "
   "m(e) ≈ 0,00055 u, nhỏ hơn nuclêôn khoảng 1836 lần.",
   "Khối lượng các hạt", D),

mc("Bán kính hạt nhân nguyên tử vào cỡ",
   ["10⁻¹⁰ m.", "10⁻¹⁵ m.", "10⁻⁶ m.", "10⁻³ m."],
   "B",
   "Hạt nhân có bán kính cỡ 10⁻¹⁵ m, nhỏ hơn bán kính nguyên tử (cỡ 10⁻¹⁰ m) khoảng 100 000 lần, "
   "nhưng lại chứa gần như toàn bộ khối lượng nguyên tử.",
   "Kích thước hạt nhân", D),

mc("Lực hạt nhân là lực",
   ["hấp dẫn giữa các nuclêôn.", "liên kết các nuclêôn, có bán kính tác dụng rất ngắn.",
    "đẩy Cu-lông giữa các prôtôn.", "từ giữa các nuclêôn chuyển động."],
   "B",
   "Lực hạt nhân là lực hút rất mạnh giữa các nuclêôn, chỉ có tác dụng trong phạm vi cỡ kích thước "
   "hạt nhân. Chính nó thắng lực đẩy Cu-lông giữa các prôtôn để giữ hạt nhân bền vững.",
   "Lực hạt nhân", D),

mc("Hạt nhân ¹⁴₆C phóng xạ β⁻. Hạt nhân con có kí hiệu là",
   ["¹⁴₅B.", "¹⁴₇N.", "¹⁰₄Be.", "¹³₆C."],
   "B",
   "Phân rã β⁻ phát ra electron ⁰₋₁e. Bảo toàn số khối: 14 = 0 + A ⇒ A = 14.\n"
   "Bảo toàn điện tích: 6 = −1 + Z ⇒ Z = 7, tức nitơ. Vậy hạt nhân con là ¹⁴₇N.",
   "Quy tắc dịch chuyển", D, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một hạt nhân phóng xạ β⁻. So với hạt nhân mẹ, hạt nhân con nằm ở vị trí nào trong bảng "
   "tuần hoàn và có số khối thế nào?",
   ["Lùi một ô, số khối không đổi.", "Tiến một ô, số khối không đổi.",
    "Tiến một ô, số khối tăng 1.", "Giữ nguyên ô, số khối không đổi."],
   "B",
   "Phân rã β⁻ phát ra electron mang điện tích −e nên để bảo toàn điện tích, Z của hạt nhân con "
   "phải tăng 1. Số khối không đổi vì electron có số khối bằng 0.",
   "Quy tắc dịch chuyển", D),

mc("Trong phân rã γ, hạt nhân",
   ["biến đổi thành hạt nhân của nguyên tố khác.",
    "không đổi về cả Z lẫn A, chỉ giải phóng năng lượng dư.",
    "mất đi hai prôtôn.", "nhận thêm một nơtron."],
   "B",
   "Phóng xạ γ là quá trình hạt nhân đang ở trạng thái kích thích chuyển về trạng thái cơ bản, "
   "phát ra phôtôn năng lượng cao. Cả Z và A đều không thay đổi.",
   "Phóng xạ gamma", D),

mc("Độ phóng xạ của một mẫu chất là",
   ["số hạt nhân còn lại trong mẫu.",
    "số phân rã xảy ra trong một giây.",
    "khối lượng chất phóng xạ còn lại.",
    "năng lượng toả ra trong một giây."],
   "B",
   "Độ phóng xạ H = λ·N là số phân rã trong một đơn vị thời gian, đơn vị là becơren (Bq). "
   "1 Bq ứng với một phân rã mỗi giây.",
   "Độ phóng xạ", D),

mc("Đơn vị của độ phóng xạ trong hệ SI là",
   ["gray (Gy).", "becơren (Bq).", "sivơ (Sv).", "culông (C)."],
   "B",
   "Becơren đo số phân rã mỗi giây. Gray đo liều hấp thụ, sivơ đo liều tương đương "
   "(có tính tới mức nguy hại sinh học).",
   "Đơn vị đo phóng xạ", D),

mc("Hằng số phóng xạ λ liên hệ với chu kì bán rã T theo hệ thức",
   ["λ = T/ln2.", "λ = ln2/T.", "λ = T·ln2.", "λ = 1/T."],
   "B",
   "λ = ln2/T ≈ 0,693/T. Hằng số phóng xạ càng lớn thì chất phân rã càng nhanh, "
   "tức chu kì bán rã càng ngắn.",
   "Hằng số phóng xạ", D),

mc("Trong phản ứng hạt nhân, đại lượng nào sau đây KHÔNG được bảo toàn?",
   ["Số khối A.", "Khối lượng nghỉ.", "Điện tích Z.", "Động lượng."],
   "B",
   "Khối lượng nghỉ KHÔNG bảo toàn trong phản ứng hạt nhân; chính phần chênh lệch khối lượng đã "
   "chuyển thành năng lượng theo hệ thức E = mc². Số khối, điện tích, năng lượng toàn phần "
   "và động lượng đều được bảo toàn.",
   "Định luật bảo toàn", D),

mc("Mỗi phản ứng phân hạch ²³⁵U toả ra năng lượng cỡ",
   ["200 eV.", "200 MeV.", "200 J.", "200 keV."],
   "B",
   "Mỗi phân hạch ²³⁵U toả khoảng 200 MeV, lớn gấp hàng chục triệu lần năng lượng của một phản ứng "
   "hoá học (cỡ vài eV).",
   "Năng lượng phân hạch", D, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Trong lò phản ứng hạt nhân, thanh điều khiển có tác dụng",
   ["làm chậm nơtron.", "hấp thụ bớt nơtron để giữ hệ số nhân nơtron bằng 1.",
    "tải nhiệt ra ngoài.", "cung cấp thêm nhiên liệu."],
   "B",
   "Thanh điều khiển làm bằng bo hoặc cađimi, hấp thụ mạnh nơtron. Đẩy thanh vào sâu thì phản ứng "
   "yếu đi, rút thanh ra thì phản ứng mạnh lên. Việc làm chậm nơtron do chất làm chậm đảm nhiệm.",
   "Lò phản ứng hạt nhân", D, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng hạt nhân"),

mc("Hệ số nhân nơtron k trong lò phản ứng hạt nhân được duy trì ở giá trị",
   ["k < 1.", "k = 1.", "k > 1.", "k = 0."],
   "B",
   "k = 1 nghĩa là mỗi phân hạch trung bình gây ra đúng một phân hạch tiếp theo, phản ứng duy trì "
   "ổn định. k < 1 thì phản ứng tắt, k > 1 thì phản ứng bùng nổ không kiểm soát.",
   "Hệ số nhân nơtron", D),

mc("Nguồn năng lượng của Mặt Trời chủ yếu đến từ",
   ["phản ứng phân hạch urani.", "phản ứng nhiệt hạch của các hạt nhân nhẹ.",
    "phản ứng hoá học đốt cháy.", "sự phóng xạ tự nhiên."],
   "B",
   "Trong lõi Mặt Trời, các hạt nhân hiđrô kết hợp thành hạt nhân heli ở nhiệt độ hàng chục triệu độ, "
   "toả ra năng lượng khổng lồ. Đó chính là phản ứng nhiệt hạch.",
   "Nhiệt hạch trong tự nhiên", D, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Phương pháp xác định tuổi mẫu vật khảo cổ bằng cacbon dựa trên đồng vị",
   ["¹²C.", "¹⁴C.", "¹³C.", "¹¹C."],
   "B",
   "¹⁴C là đồng vị phóng xạ có chu kì bán rã 5730 năm. Khi sinh vật còn sống, tỉ lệ ¹⁴C được duy "
   "trì; khi chết, ¹⁴C chỉ phân rã dần nên đo tỉ lệ còn lại là suy ra được tuổi.",
   "Ứng dụng phóng xạ", D, fig="h_dt_c14", cap="Xác định tuổi bằng cacbon-14"),

mc("Ba nguyên tắc cơ bản để bảo vệ con người khỏi bức xạ ion hoá là",
   ["tăng thời gian, giảm khoảng cách, không che chắn.",
    "giảm thời gian tiếp xúc, tăng khoảng cách, che chắn thích hợp.",
    "tăng nhiệt độ, giảm áp suất, dùng găng tay.",
    "dùng nước, ánh sáng và không khí sạch."],
   "B",
   "Ba nguyên tắc: rút ngắn THỜI GIAN tiếp xúc, tăng KHOẢNG CÁCH tới nguồn (liều giảm theo bình "
   "phương khoảng cách) và dùng vật liệu CHE CHẮN phù hợp với loại tia.",
   "An toàn bức xạ", D, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Trong y học, tia γ phát ra từ nguồn ⁶⁰Co được dùng chủ yếu để",
   ["chụp X-quang răng.", "xạ trị diệt tế bào ung thư nằm sâu trong cơ thể.",
    "đo huyết áp.", "khử trùng nước uống tại nhà."],
   "B",
   "Tia γ có khả năng đâm xuyên lớn nên tới được khối u nằm sâu. Người ta chiếu từ nhiều hướng "
   "cùng hội tụ vào khối u để mô lành chỉ nhận liều nhỏ.",
   "Ứng dụng trong y học", D, fig="h_sd_ung_dung", cap="Ứng dụng của đồng vị phóng xạ"),

mc("So với phản ứng hoá học, phản ứng hạt nhân có đặc điểm",
   ["toả năng lượng nhỏ hơn nhiều.",
    "toả năng lượng lớn hơn hàng triệu lần trên cùng khối lượng nhiên liệu.",
    "phụ thuộc mạnh vào nhiệt độ môi trường.",
    "chỉ làm thay đổi lớp electron ngoài cùng."],
   "B",
   "Phản ứng hoá học chỉ liên quan tới electron ngoài cùng, toả cỡ vài eV mỗi phản ứng; "
   "phản ứng hạt nhân làm biến đổi chính hạt nhân, toả cỡ hàng chục tới hàng trăm MeV.",
   "So sánh phản ứng hạt nhân và hoá học", D),
],
P2=[
ds("Xét hiện tượng phóng xạ của một đồng vị.",
   [("Phóng xạ là quá trình tự phát, không cần tác động từ bên ngoài.", True,
     "Đúng. Hạt nhân không bền tự biến đổi mà không cần kích thích nào."),
    ("Không thể dự đoán chính xác thời điểm một hạt nhân cụ thể sẽ phân rã.", True,
     "Đúng. Phân rã là quá trình ngẫu nhiên với từng hạt nhân; chỉ quy luật thống kê của số đông "
     "mới xác định được."),
    ("Đun nóng mẫu chất phóng xạ sẽ làm chu kì bán rã giảm đi.", False,
     "Sai. Chu kì bán rã là hằng số của từng đồng vị, không phụ thuộc nhiệt độ, áp suất hay "
     "trạng thái hoá học."),
    ("Quá trình phóng xạ luôn toả năng lượng.", True,
     "Đúng. Hạt nhân con và các hạt phát ra luôn có tổng khối lượng nghỉ nhỏ hơn hạt nhân mẹ.")],
   "Đặc điểm của phóng xạ", D),

ds("Hạt nhân ²³⁸₉₂U phóng xạ α tạo thành hạt nhân thori.",
   [("Phương trình phân rã là ²³⁸₉₂U → ⁴₂He + ²³⁴₉₀Th.", True,
     "Đúng. Bảo toàn số khối: 238 = 4 + 234; bảo toàn điện tích: 92 = 2 + 90."),
    ("Hạt nhân thori có 144 nơtron.", True,
     "Đúng. N = 234 − 90 = 144."),
    ("Số khối của hạt nhân con nhỏ hơn hạt nhân mẹ 2 đơn vị.", False,
     "Sai. Phân rã α làm số khối giảm 4 đơn vị (từ 238 xuống 234), còn điện tích mới giảm 2 đơn vị."),
    ("Tổng điện tích trước và sau phân rã bằng nhau.", True,
     "Đúng. Bảo toàn điện tích là một trong hai định luật cơ bản dùng để viết phương trình phân rã.")],
   "Viết phương trình phân rã", D, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

ds("Một lò phản ứng hạt nhân đang hoạt động ổn định.",
   [("Nhiên liệu thường dùng là ²³⁵U hoặc ²³⁹Pu.", True,
     "Đúng. Đó là hai đồng vị dễ bị phân hạch bởi nơtron chậm."),
    ("Chất làm chậm có nhiệm vụ giảm tốc độ nơtron để chúng dễ gây phân hạch hơn.", True,
     "Đúng. Nước thường, nước nặng hoặc than chì được dùng làm chất làm chậm."),
    ("Hệ số nhân nơtron được giữ lớn hơn 1 để lò sinh nhiều năng lượng hơn.", False,
     "Sai. k > 1 sẽ làm phản ứng bùng nổ mất kiểm soát. Lò luôn được điều khiển ở k = 1."),
    ("Nhiệt sinh ra trong lò được dùng để đun nước thành hơi, làm quay tua bin máy phát điện.", True,
     "Đúng. Chuỗi chuyển hoá là: năng lượng hạt nhân → nhiệt năng → cơ năng → điện năng.")],
   "Lò phản ứng hạt nhân", D, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

ds("Xét ứng dụng của các đồng vị phóng xạ trong đời sống.",
   [("Tia γ được dùng để tiệt trùng dụng cụ y tế nhờ khả năng đâm xuyên lớn.", True,
     "Đúng. Tia γ xuyên qua cả bao bì kín nên có thể tiệt trùng sau khi đã đóng gói."),
    ("Tia β được dùng để đo bề dày tấm kim loại mỏng trong nhà máy cán.", True,
     "Đúng. Cường độ tia β xuyên qua rất nhạy với bề dày của tấm mỏng."),
    ("Tia α thích hợp nhất để chiếu xạ khối u nằm sâu trong cơ thể.", False,
     "Sai. Tia α bị chặn ngay bởi lớp da nên không tới được khối u nằm sâu. "
     "Người ta dùng tia γ cho mục đích này."),
    ("Đồng vị dùng trong chẩn đoán hình ảnh thường có chu kì bán rã ngắn.", True,
     "Đúng. Chu kì ngắn giúp đồng vị nhanh chóng phân rã hết, giảm liều chiếu cho bệnh nhân.")],
   "Ứng dụng của đồng vị phóng xạ", D, fig="h_sd_ung_dung",
   cap="Ứng dụng của đồng vị phóng xạ"),
],
P3=[
sa("Hạt nhân ²¹⁰₈₄Po phóng xạ α. Điện tích hạt nhân con bằng bao nhiêu đơn vị điện tích nguyên tố?",
   "82",
   "Bảo toàn điện tích: 84 = 2 + Z ⇒ Z = 82, đó là hạt nhân chì ²⁰⁶₈₂Pb.",
   "Quy tắc dịch chuyển", D, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã của pôlôni"),

sa("Một chất phóng xạ có chu kì bán rã 10 ngày. Hằng số phóng xạ của chất đó bằng bao nhiêu "
   "trên ngày (làm tròn đến chữ số thập phân thứ tư)? Lấy ln2 ≈ 0,693.",
   "0,0693",
   "λ = ln2/T = 0,693/10 = 0,0693 (ngày⁻¹).",
   "Hằng số phóng xạ", D),

sa("Hạt nhân ⁷₃Li có khối lượng 7,0160 u. Độ hụt khối của hạt nhân này bằng bao nhiêu u "
   "(làm tròn đến chữ số thập phân thứ tư)? Cho m(p) = 1,0073 u; m(n) = 1,0087 u.",
   "0,0407",
   "Hạt nhân ⁷₃Li có 3 prôtôn và 7 − 3 = 4 nơtron.\n"
   "Tổng khối lượng các nuclêôn riêng lẻ:\n"
   "3 · 1,0073 + 4 · 1,0087 = 3,0219 + 4,0348 = 7,0567 u.\n"
   "Δm = 7,0567 − 7,0160 = 0,0407 u.",
   "Độ hụt khối", TB),

sa("Một mẫu chất phóng xạ ban đầu có 6,0·10²⁰ hạt nhân, chu kì bán rã 4,0 giờ. "
   "Sau 8,0 giờ, số hạt nhân chưa phân rã còn lại bằng bao nhiêu (viết dưới dạng x·10²⁰, "
   "chỉ ghi giá trị x)?",
   "1,5",
   "Số chu kì: n = 8,0/4,0 = 2.\n"
   "N = N₀·2⁻² = 6,0·10²⁰/4 = 1,5·10²⁰ hạt.",
   "Định luật phóng xạ", D),

sa("Một mẫu chất phóng xạ có độ phóng xạ ban đầu 800 kBq và chu kì bán rã 4,0 giờ. "
   "Sau 12 giờ, độ phóng xạ của mẫu bằng bao nhiêu kilôbecơren?",
   "100",
   "Số chu kì: n = 12/4,0 = 3.\n"
   "H = H₀·2⁻³ = 800/8 = 100 kBq.",
   "Độ phóng xạ", D, fig="h_dt_H_t", cap="Độ phóng xạ theo thời gian"),

sa("Cho phản ứng hạt nhân: ¹⁴₇N + ⁴₂He → X + ¹₁H. Số khối của hạt nhân X bằng bao nhiêu?",
   "17",
   "Bảo toàn số khối: 14 + 4 = A + 1 ⇒ A = 17.\n"
   "Bảo toàn điện tích: 7 + 2 = Z + 1 ⇒ Z = 8, tức hạt nhân ¹⁷₈O.",
   "Phản ứng hạt nhân", TB),
])


# =====================================================================  ĐỀ 3
DE3 = dict(
ma="12C4-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Tính năng lượng liên kết, so sánh độ bền vững, vận dụng định luật phóng xạ",
P1=[
mc("Hạt nhân ⁴₂He có khối lượng 4,0015 u. Cho m(p) = 1,0073 u; m(n) = 1,0087 u. "
   "Độ hụt khối của hạt nhân này bằng",
   ["0,0205 u.", "0,0305 u.", "0,0405 u.", "0,0505 u."],
   "B",
   "Tổng khối lượng nuclêôn riêng lẻ: 2 · 1,0073 + 2 · 1,0087 = 2,0146 + 2,0174 = 4,0320 u.\n"
   "Δm = 4,0320 − 4,0015 = 0,0305 u.",
   "Độ hụt khối", TB, fig="h_sd_dohutkhoi", cap="Độ hụt khối của hạt nhân heli"),

mc("Với độ hụt khối 0,0305 u, năng lượng liên kết của hạt nhân ⁴₂He xấp xỉ "
   "(cho 1 u·c² = 931,5 MeV)",
   ["14,2 MeV.", "28,4 MeV.", "56,8 MeV.", "7,10 MeV."],
   "B",
   "W(lk) = Δm·c² = 0,0305 · 931,5 ≈ 28,4 MeV.\n"
   "Giá trị 7,10 MeV là năng lượng liên kết RIÊNG (28,4/4), không phải năng lượng liên kết.",
   "Năng lượng liên kết", TB),

mc("Năng lượng liên kết riêng của hạt nhân ⁴₂He (W(lk) = 28,4 MeV) bằng",
   ["28,4 MeV/nuclêôn.", "7,10 MeV/nuclêôn.",
    "14,2 MeV/nuclêôn.", "113,6 MeV/nuclêôn."],
   "B",
   "ε = W(lk)/A = 28,4/4 = 7,10 MeV/nuclêôn. "
   "Giá trị này nhỏ hơn ε của sắt (≈ 8,8 MeV/nuclêôn) nên heli chưa phải hạt nhân bền nhất.",
   "Năng lượng liên kết riêng", TB),

mc("Trên đường cong năng lượng liên kết riêng theo số khối, các hạt nhân bền vững nhất nằm ở "
   "vùng số khối",
   ["A < 10.", "A ≈ 56.", "A ≈ 120.", "A > 200."],
   "B",
   "Đỉnh của đường cong nằm quanh A ≈ 56 (sắt, niken) với ε ≈ 8,8 MeV/nuclêôn. "
   "Đó là lí do cả nhiệt hạch (từ A nhỏ) lẫn phân hạch (từ A lớn) đều toả năng lượng.",
   "Đường cong năng lượng liên kết riêng", TB, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Hạt nhân X có W(lk) = 250 MeV, A = 30; hạt nhân Y có W(lk) = 500 MeV, A = 80. "
   "Kết luận nào đúng?",
   ["Y bền hơn X vì W(lk) lớn hơn.", "X bền hơn Y vì ε lớn hơn.",
    "Hai hạt nhân bền như nhau.", "Không so sánh được."],
   "B",
   "ε(X) = 250/30 ≈ 8,33 MeV/nuclêôn;  ε(Y) = 500/80 = 6,25 MeV/nuclêôn.\n"
   "X có năng lượng liên kết riêng lớn hơn nên bền vững hơn, dù W(lk) của nó nhỏ hơn. "
   "Chọn theo W(lk) là bẫy phổ biến nhất của chương này.",
   "So sánh độ bền vững", TB),

mc("Một mẫu chất phóng xạ sau 3 chu kì bán rã còn lại bao nhiêu phần trăm so với ban đầu?",
   ["25,0 %.", "12,5 %.", "33,3 %.", "6,25 %."],
   "B",
   "Sau n chu kì còn lại 2⁻ⁿ. Với n = 3: 2⁻³ = 1/8 = 12,5 %.",
   "Định luật phóng xạ", D),

mc("Ban đầu có N₀ hạt nhân. Sau 2 chu kì bán rã, tỉ số giữa số hạt nhân ĐÃ phân rã và số hạt nhân "
   "CÒN LẠI bằng",
   ["1 : 3.", "3 : 1.", "1 : 1.", "4 : 1."],
   "B",
   "Sau 2T còn N₀/4, đã rã 3N₀/4. Tỉ số 3 : 1.\n"
   "Công thức chung sau n chu kì: tỉ số (2ⁿ − 1) : 1.",
   "Định luật phóng xạ", TB, fig="h_dt_phanra", cap="Đồ thị phân rã phóng xạ"),

mc("Một chất phóng xạ có chu kì bán rã 20 phút. Sau bao lâu thì độ phóng xạ giảm còn 1/16 giá trị "
   "ban đầu?",
   ["60 phút.", "80 phút.", "40 phút.", "100 phút."],
   "B",
   "1/16 = 2⁻⁴ nên n = 4 chu kì.\n"
   "t = 4 · 20 = 80 phút.",
   "Định luật phóng xạ", TB),

mc("Số hạt nhân có trong 4,0 gam đồng vị ²⁰⁰X (khối lượng mol 200 g/mol) xấp xỉ "
   "(Nₐ = 6,02·10²³ mol⁻¹)",
   ["1,20·10²².", "1,20·10²¹.", "6,02·10²².", "2,41·10²²."],
   "A",
   "Số mol: n = 4,0/200 = 0,020 mol.\n"
   "N = n·Nₐ = 0,020 · 6,02·10²³ = 1,204·10²² ≈ 1,20·10²² hạt.",
   "Số hạt nhân trong một khối lượng", TB),

mc("Cho phản ứng: ⁹₄Be + ⁴₂He → ¹²₆C + X. Hạt X là",
   ["prôtôn.", "nơtron.", "electron.", "hạt α."],
   "B",
   "Bảo toàn số khối: 9 + 4 = 12 + A ⇒ A = 1.\n"
   "Bảo toàn điện tích: 4 + 2 = 6 + Z ⇒ Z = 0.\n"
   "Hạt có A = 1, Z = 0 chính là nơtron ¹₀n.",
   "Phản ứng hạt nhân", TB),

mc("Trong phản ứng hạt nhân toả năng lượng, tổng khối lượng nghỉ của các hạt sau phản ứng",
   ["lớn hơn tổng khối lượng nghỉ trước phản ứng.",
    "nhỏ hơn tổng khối lượng nghỉ trước phản ứng.",
    "bằng tổng khối lượng nghỉ trước phản ứng.",
    "không liên quan tới năng lượng toả ra."],
   "B",
   "Năng lượng toả ra chính là phần khối lượng nghỉ bị hụt đi: ΔE = (m trước − m sau)·c² > 0 "
   "khi m sau < m trước.",
   "Năng lượng phản ứng hạt nhân", TB),

mc("Một phản ứng hạt nhân có tổng khối lượng trước là 5,0296 u và sau là 5,0102 u. "
   "Năng lượng toả ra của phản ứng xấp xỉ",
   ["9,0 MeV.", "18,1 MeV.", "36,2 MeV.", "4,5 MeV."],
   "B",
   "Δm = 5,0296 − 5,0102 = 0,0194 u.\n"
   "ΔE = 0,0194 · 931,5 ≈ 18,1 MeV. Vì Δm > 0 nên phản ứng TOẢ năng lượng.",
   "Năng lượng phản ứng hạt nhân", TB, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Trong phản ứng phân hạch dây chuyền, mỗi phân hạch giải phóng trung bình",
   ["không có nơtron nào.", "2 đến 3 nơtron.",
    "hàng trăm nơtron.", "chỉ đúng 1 nơtron."],
   "B",
   "Mỗi phân hạch ²³⁵U giải phóng trung bình 2–3 nơtron. Chính các nơtron này gây ra các phân hạch "
   "tiếp theo, tạo thành phản ứng dây chuyền.",
   "Phản ứng dây chuyền", D, fig="h_sd_phan_hach", cap="Phản ứng dây chuyền"),

mc("Ưu điểm nổi bật của phản ứng nhiệt hạch so với phân hạch là",
   ["dễ điều khiển hơn.", "nhiên liệu dồi dào và ít chất thải phóng xạ sống lâu.",
    "xảy ra ở nhiệt độ thấp hơn.", "toả nhiều năng lượng hơn trên mỗi phản ứng."],
   "B",
   "Đơteri có sẵn trong nước biển gần như vô tận và sản phẩm chủ yếu là heli không phóng xạ. "
   "Tuy nhiên nhiệt hạch lại KHÓ điều khiển hơn và mỗi phản ứng toả ÍT năng lượng hơn "
   "(17,6 MeV so với 200 MeV).",
   "So sánh phân hạch và nhiệt hạch", TB),

mc("Một mẫu gỗ cổ có độ phóng xạ của ¹⁴C bằng một nửa mẫu gỗ tươi cùng khối lượng. "
   "Tuổi của mẫu gỗ xấp xỉ (chu kì bán rã của ¹⁴C là 5730 năm)",
   ["2865 năm.", "5730 năm.", "11 460 năm.", "17 190 năm."],
   "B",
   "Còn một nửa ứng với đúng một chu kì bán rã nên t = T = 5730 năm.",
   "Xác định tuổi bằng cacbon-14", TB, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

mc("Liều hấp thụ bức xạ được đo bằng đơn vị",
   ["becơren (Bq).", "gray (Gy).", "tesla (T).", "vêbe (Wb)."],
   "B",
   "Gray đo liều hấp thụ (năng lượng bức xạ mà 1 kg vật chất hấp thụ). Becơren đo độ phóng xạ "
   "của nguồn, còn sivơ đo liều tương đương có tính tới mức nguy hại sinh học.",
   "Đơn vị đo bức xạ", D, fig="h_sd_an_toan", cap="An toàn bức xạ"),

mc("Khi tăng khoảng cách tới một nguồn phóng xạ điểm lên gấp ba thì liều chiếu nhận được",
   ["giảm 3 lần.", "giảm 9 lần.", "giảm 6 lần.", "không đổi."],
   "B",
   "Liều chiếu từ nguồn điểm giảm theo bình phương khoảng cách. Khoảng cách tăng 3 lần thì "
   "liều giảm 3² = 9 lần. Đây là cơ sở của nguyên tắc “tăng khoảng cách”.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Để kiểm tra bề dày của tấm thép mỏng đang cán liên tục, người ta dùng nguồn phát",
   ["tia α.", "tia β.", "tia γ.", "sóng âm."],
   "B",
   "Tia α bị chặn ngay bởi tờ giấy nên không xuyên qua thép; tia γ xuyên qua gần như hoàn toàn "
   "nên không nhạy với thay đổi bề dày nhỏ. Tia β bị hấp thụ một phần nên cường độ xuyên qua "
   "rất nhạy với bề dày.",
   "Ứng dụng trong công nghiệp", TB, fig="h_sd_ung_dung",
   cap="Ứng dụng của đồng vị phóng xạ"),
],
P2=[
ds("Hạt nhân ⁴₂He có khối lượng 4,0015 u; cho m(p) = 1,0073 u; m(n) = 1,0087 u; "
   "1 u·c² = 931,5 MeV.",
   [("Tổng khối lượng của 2 prôtôn và 2 nơtron riêng lẻ là 4,0320 u.", True,
     "Đúng. 2 · 1,0073 + 2 · 1,0087 = 2,0146 + 2,0174 = 4,0320 u."),
    ("Độ hụt khối của hạt nhân là 0,0305 u.", True,
     "Đúng. Δm = 4,0320 − 4,0015 = 0,0305 u."),
    ("Năng lượng liên kết của hạt nhân xấp xỉ 28,4 MeV.", True,
     "Đúng. W(lk) = 0,0305 · 931,5 ≈ 28,4 MeV."),
    ("Năng lượng liên kết riêng của hạt nhân là 28,4 MeV/nuclêôn.", False,
     "Sai. Năng lượng liên kết riêng là ε = 28,4/4 = 7,10 MeV/nuclêôn. "
     "Giá trị 28,4 MeV là năng lượng liên kết của cả hạt nhân.")],
   "Độ hụt khối và năng lượng liên kết", TB, fig="h_sd_dohutkhoi",
   cap="Độ hụt khối của hạt nhân heli"),

ds("Một mẫu chất phóng xạ có chu kì bán rã 8,0 ngày, ban đầu có khối lượng 320 gam.",
   [("Sau 8,0 ngày, khối lượng còn lại là 160 gam.", True,
     "Đúng. Sau một chu kì bán rã, khối lượng còn một nửa: 320/2 = 160 g."),
    ("Sau 24 ngày, khối lượng còn lại là 40 gam.", True,
     "Đúng. n = 24/8,0 = 3 ⇒ m = 320/2³ = 320/8 = 40 g."),
    ("Sau 24 ngày, khối lượng đã phân rã là 280 gam.", True,
     "Đúng. 320 − 40 = 280 g."),
    ("Sau 32 ngày, toàn bộ chất phóng xạ đã phân rã hết.", False,
     "Sai. Sau 32 ngày (n = 4) vẫn còn 320/16 = 20 g. Theo lí thuyết, số hạt nhân giảm theo "
     "hàm mũ và không bao giờ bằng đúng 0.")],
   "Định luật phóng xạ", TB),

ds("Cho phản ứng hạt nhân: ²₁H + ³₁H → ⁴₂He + ¹₀n, với các khối lượng m(²H) = 2,0136 u; "
   "m(³H) = 3,0160 u; m(⁴He) = 4,0015 u; m(n) = 1,0087 u; 1 u·c² = 931,5 MeV.",
   [("Đây là phản ứng nhiệt hạch.", True,
     "Đúng. Hai hạt nhân rất nhẹ kết hợp thành hạt nhân nặng hơn."),
    ("Tổng khối lượng trước phản ứng là 5,0296 u.", True,
     "Đúng. 2,0136 + 3,0160 = 5,0296 u."),
    ("Phản ứng thu năng lượng vì tổng khối lượng sau lớn hơn tổng khối lượng trước.", False,
     "Sai. Tổng khối lượng sau là 4,0015 + 1,0087 = 5,0102 u, NHỎ hơn 5,0296 u, "
     "nên phản ứng TOẢ năng lượng."),
    ("Năng lượng toả ra của phản ứng xấp xỉ 18,1 MeV.", True,
     "Đúng. Δm = 5,0296 − 5,0102 = 0,0194 u ⇒ ΔE = 0,0194 · 931,5 ≈ 18,1 MeV.")],
   "Năng lượng phản ứng hạt nhân", TB, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

ds("Xét các biện pháp bảo vệ con người khỏi bức xạ ion hoá.",
   [("Rút ngắn thời gian tiếp xúc làm giảm liều chiếu nhận được.", True,
     "Đúng. Liều chiếu tỉ lệ thuận với thời gian tiếp xúc."),
    ("Tăng khoảng cách tới nguồn lên gấp đôi làm liều chiếu giảm 4 lần.", True,
     "Đúng. Liều chiếu từ nguồn điểm giảm theo bình phương khoảng cách."),
    ("Một tờ giấy mỏng đủ để chắn tia γ.", False,
     "Sai. Tờ giấy chỉ chắn được tia α. Tia γ cần lớp chì hoặc bê tông dày mới giảm được đáng kể."),
    ("Nguồn phát tia α đặc biệt nguy hiểm nếu bị hít hoặc nuốt vào cơ thể.", True,
     "Đúng. Khi ở ngoài cơ thể, tia α bị lớp da chặn lại; nhưng vào bên trong nó ion hoá rất mạnh "
     "ngay tại mô sống.")],
   "An toàn bức xạ", TB, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),
],
P3=[
sa("Hạt nhân ¹⁶₈O có khối lượng 15,9905 u. Năng lượng liên kết riêng của hạt nhân này bằng bao nhiêu "
   "MeV trên nuclêôn (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho m(p) = 1,0073 u; m(n) = 1,0087 u; 1 u·c² = 931,5 MeV.",
   "8,0",
   "Hạt nhân ¹⁶₈O có 8 prôtôn và 8 nơtron.\n"
   "Tổng khối lượng các nuclêôn riêng lẻ:\n"
   "8 · 1,0073 + 8 · 1,0087 = 8,0584 + 8,0696 = 16,1280 u.\n"
   "Δm = 16,1280 − 15,9905 = 0,1375 u.\n"
   "W(lk) = Δm · 931,5 = 0,1375 · 931,5 ≈ 128,08 MeV.\n"
   "ε = W(lk)/A = 128,08/16 ≈ 8,0 MeV/nuclêôn.",
   "Năng lượng liên kết riêng", TB),

sa("Một chất phóng xạ có chu kì bán rã 15 giờ. Sau bao nhiêu giờ thì số hạt nhân chưa phân rã "
   "còn lại 1/32 so với ban đầu?",
   "75",
   "1/32 = 2⁻⁵ nên n = 5 chu kì.\n"
   "t = 5 · 15 = 75 giờ.",
   "Định luật phóng xạ", TB),

sa("Ban đầu một mẫu chất phóng xạ nguyên chất có N₀ hạt nhân. Sau thời gian 4 chu kì bán rã, "
   "tỉ số giữa số hạt nhân con tạo thành và số hạt nhân mẹ còn lại bằng bao nhiêu?",
   "15",
   "Sau 4 chu kì, số hạt mẹ còn lại N = N₀/16.\n"
   "Số hạt con tạo thành bằng số hạt mẹ đã rã: N₀ − N₀/16 = 15N₀/16.\n"
   "Tỉ số: (15N₀/16)/(N₀/16) = 15.",
   "Tỉ số hạt nhân con và mẹ", TB),

sa("Tính số hạt nhân có trong 2,0 gam đồng vị ²³⁵U (khối lượng mol 235 g/mol). "
   "Cho Nₐ = 6,02·10²³ mol⁻¹. Viết kết quả dưới dạng x·10²¹ và chỉ ghi giá trị x "
   "(làm tròn đến chữ số thập phân thứ hai).",
   "5,12",
   "Số mol: n = 2,0/235 ≈ 8,511·10⁻³ mol.\n"
   "N = n·Nₐ = 8,511·10⁻³ · 6,02·10²³ ≈ 5,124·10²¹ ≈ 5,12·10²¹ hạt.",
   "Số hạt nhân trong một khối lượng", TB),

sa("Cho phản ứng hạt nhân: ²³₁₁Na + ¹₁H → ⁴₂He + X. Số khối của hạt nhân X bằng bao nhiêu?",
   "20",
   "Bảo toàn số khối: 23 + 1 = 4 + A ⇒ A = 20.\n"
   "Bảo toàn điện tích: 11 + 1 = 2 + Z ⇒ Z = 10, tức hạt nhân neon ²⁰₁₀Ne.",
   "Phản ứng hạt nhân", TB),

sa("Một mẫu gỗ cổ có độ phóng xạ của ¹⁴C bằng 12,5 % mẫu gỗ tươi cùng khối lượng. "
   "Tuổi của mẫu gỗ bằng bao nhiêu năm? Cho chu kì bán rã của ¹⁴C là 5730 năm.",
   "17190",
   "12,5 % = 1/8 = 2⁻³ nên n = 3 chu kì bán rã.\n"
   "t = 3 · 5730 = 17 190 năm.",
   "Xác định tuổi bằng cacbon-14", TB, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),
])


# =====================================================================  ĐỀ 4
DE4 = dict(
ma="12C4-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Độ phóng xạ, năng lượng hạt nhân, đọc đồ thị phân rã",
P1=[
mc("Độ phóng xạ của một mẫu chất được tính bằng công thức",
   ["H = N/λ.", "H = λ·N.", "H = λ/N.", "H = N·T."],
   "B",
   "H = λ·N với λ = ln2/T là hằng số phóng xạ và N là số hạt nhân chưa phân rã. "
   "Vì N giảm theo thời gian nên H cũng giảm theo đúng quy luật hàm mũ như N.",
   "Độ phóng xạ", D),

mc("Hai mẫu chất phóng xạ khác nhau có cùng số hạt nhân. Mẫu nào có chu kì bán rã NGẮN hơn thì",
   ["độ phóng xạ nhỏ hơn.", "độ phóng xạ lớn hơn.",
    "độ phóng xạ bằng nhau.", "không có độ phóng xạ."],
   "B",
   "H = λ·N = (ln2/T)·N. Với cùng N, chu kì bán rã T càng nhỏ thì λ càng lớn nên H càng lớn: "
   "chất phân rã nhanh hơn thì mỗi giây có nhiều phân rã hơn.",
   "Độ phóng xạ và chu kì bán rã", TB),

mc("Từ đồ thị độ phóng xạ theo thời gian, độ phóng xạ giảm từ 800 kBq xuống 400 kBq trong 4,0 giờ. "
   "Chu kì bán rã của chất đó bằng",
   ["2,0 giờ.", "4,0 giờ.", "8,0 giờ.", "1,0 giờ."],
   "B",
   "Độ phóng xạ giảm đúng một nửa nên khoảng thời gian đó chính là một chu kì bán rã: T = 4,0 giờ.",
   "Đọc đồ thị độ phóng xạ", TB, fig="h_dt_H_t", cap="Độ phóng xạ theo thời gian"),

mc("Đồ thị của lnH theo thời gian t đối với một chất phóng xạ là",
   ["đường cong lồi.", "đường thẳng có hệ số góc bằng −λ.",
    "đường thẳng nằm ngang.", "đường parabol."],
   "B",
   "Từ H = H₀·e^(−λt) lấy logarit tự nhiên: lnH = lnH₀ − λt. Đó là phương trình đường thẳng "
   "với hệ số góc −λ. Đây là cách xác định chu kì bán rã từ số liệu thực nghiệm.",
   "Đồ thị bán logarit", TB, fig="h_dt_H_t", cap="Đồ thị lnH theo thời gian"),

mc("Hạt nhân ²¹⁰₈₄Po phóng xạ α với chu kì bán rã 138 ngày, tạo thành hạt nhân chì bền. "
   "Sau 276 ngày, tỉ số giữa số hạt nhân chì và số hạt nhân pôlôni còn lại bằng",
   ["1.", "3.", "2.", "4."],
   "B",
   "276 ngày = 2 chu kì bán rã.\n"
   "Số hạt Po còn lại: N₀/4. Số hạt Pb tạo thành: N₀ − N₀/4 = 3N₀/4.\n"
   "Tỉ số: 3.",
   "Tỉ số hạt nhân con và mẹ", TB, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã của pôlôni"),

mc("Năng lượng toả ra khi phân hạch hoàn toàn 1,0 gam ²³⁵U xấp xỉ (mỗi phân hạch toả 200 MeV; "
   "Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J)",
   ["8,2·10⁷ J.", "8,2·10¹⁰ J.", "8,2·10¹³ J.", "8,2·10⁴ J."],
   "B",
   "Số hạt nhân trong 1,0 g: N = (1,0/235)·6,02·10²³ ≈ 2,56·10²¹ hạt.\n"
   "Tổng năng lượng: E = 2,56·10²¹ · 200 = 5,12·10²³ MeV.\n"
   "Đổi sang jun: E = 5,12·10²³ · 1,6·10⁻¹³ ≈ 8,2·10¹⁰ J.",
   "Năng lượng của nhiên liệu hạt nhân", TB, fig="h_sd_phan_hach",
   cap="Phản ứng phân hạch"),

mc("Trong lò phản ứng hạt nhân, chất làm chậm KHÔNG thể là",
   ["nước thường.", "chì.", "nước nặng.", "than chì."],
   "B",
   "Chất làm chậm phải gồm các hạt nhân NHẸ để nơtron mất nhiều năng lượng sau mỗi va chạm. "
   "Chì có hạt nhân rất nặng nên nơtron bật lại gần như không mất năng lượng; chì chỉ dùng "
   "để che chắn bức xạ.",
   "Lò phản ứng hạt nhân", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Một chất phóng xạ có chu kì bán rã T. Sau thời gian t = 3T, phần trăm số hạt nhân ĐÃ phân rã là",
   ["12,5 %.", "87,5 %.", "25,0 %.", "75,0 %."],
   "B",
   "Còn lại 2⁻³ = 12,5 %, do đó đã phân rã 100 % − 12,5 % = 87,5 %. "
   "Đọc kĩ đề hỏi phần CÒN LẠI hay phần ĐÃ RÃ.",
   "Định luật phóng xạ", TB),

mc("Cho biết năng lượng liên kết riêng của ²³⁵U là 7,6 MeV/nuclêôn. Năng lượng liên kết của hạt "
   "nhân này bằng",
   ["1786 MeV.", "1330 MeV.", "3572 MeV.", "893 MeV."],
   "A",
   "W(lk) = ε·A = 7,6 · 235 = 1786 MeV.\n"
   "Đây là năng lượng cần cung cấp để tách hoàn toàn hạt nhân ²³⁵U thành 235 nuclêôn riêng lẻ.",
   "Năng lượng liên kết", TB),

mc("Một hạt nhân đứng yên phóng xạ α. So sánh động lượng của hạt α và hạt nhân con:",
   ["hai động lượng bằng nhau về cả độ lớn lẫn hướng.",
    "hai động lượng có cùng độ lớn nhưng ngược hướng.",
    "động lượng hạt α lớn hơn.",
    "động lượng hạt nhân con lớn hơn."],
   "B",
   "Hạt nhân mẹ đứng yên nên tổng động lượng ban đầu bằng 0. Theo định luật bảo toàn động lượng, "
   "hai hạt sinh ra phải có động lượng cùng độ lớn và ngược hướng.",
   "Bảo toàn động lượng", TB),

mc("Trong phản ứng hạt nhân, năng lượng toả ra chủ yếu chuyển thành",
   ["thế năng của các hạt sản phẩm.", "động năng của các hạt sản phẩm và năng lượng bức xạ.",
    "khối lượng nghỉ của hạt nhân con.", "điện năng trực tiếp."],
   "B",
   "Năng lượng toả ra xuất hiện dưới dạng động năng của các mảnh vỡ và của các hạt phát ra, "
   "cùng với năng lượng của bức xạ γ. Trong lò phản ứng, động năng đó biến thành nhiệt.",
   "Năng lượng phản ứng hạt nhân", TB),

mc("Hạt nhân nào sau đây KHÔNG có nơtron?",
   ["²₁H.", "¹₁H.", "³₂He.", "⁴₂He."],
   "B",
   "¹₁H có A = 1 và Z = 1 nên N = A − Z = 0: hạt nhân chỉ gồm một prôtôn duy nhất. "
   "Đây là hạt nhân duy nhất không chứa nơtron.",
   "Cấu tạo hạt nhân", D),

mc("Trong công nghiệp, người ta dùng tia γ để kiểm tra khuyết tật bên trong mối hàn dày vì tia γ",
   ["có khả năng ion hoá mạnh nhất.", "có khả năng đâm xuyên lớn nhất.",
    "mang điện tích dương.", "có vận tốc nhỏ nhất."],
   "B",
   "Tia γ xuyên qua được lớp kim loại dày nên phát hiện được bọt khí hay vết nứt bên trong. "
   "Tia α và β đều bị chặn lại ngay từ bề mặt.",
   "Ứng dụng trong công nghiệp", D, fig="h_sd_dam_xuyen", cap="Khả năng đâm xuyên của ba tia"),

mc("Một nguồn phóng xạ có độ phóng xạ 3,7·10¹⁰ Bq nghĩa là trong mỗi giây có",
   ["3,7·10¹⁰ hạt nhân được tạo thành.", "3,7·10¹⁰ phân rã xảy ra.",
    "3,7·10¹⁰ jun năng lượng toả ra.", "3,7·10¹⁰ nguyên tử bị ion hoá."],
   "B",
   "1 becơren ứng với một phân rã mỗi giây. Vậy 3,7·10¹⁰ Bq nghĩa là mỗi giây có 3,7·10¹⁰ "
   "hạt nhân bị phân rã.",
   "Ý nghĩa của độ phóng xạ", D),

mc("Chất thải phóng xạ từ nhà máy điện hạt nhân cần được xử lí đặc biệt vì",
   ["chúng có nhiệt độ rất cao.", "chúng tiếp tục phát ra bức xạ ion hoá trong thời gian dài.",
    "chúng dễ cháy nổ.", "chúng dẫn điện rất tốt."],
   "B",
   "Nhiều sản phẩm phân hạch có chu kì bán rã rất dài, tiếp tục phát tia phóng xạ trong hàng trăm "
   "tới hàng nghìn năm, nên phải được lưu giữ và cách li nghiêm ngặt.",
   "An toàn hạt nhân", D),

mc("Phát biểu nào sau đây SAI?",
   ["Hạt nhân càng bền vững khi năng lượng liên kết riêng càng lớn.",
    "Hạt nhân càng bền vững khi năng lượng liên kết càng lớn.",
    "Độ hụt khối của một hạt nhân luôn dương.",
    "Năng lượng liên kết bằng tích độ hụt khối với bình phương tốc độ ánh sáng."],
   "B",
   "Độ bền vững được đo bằng năng lượng liên kết RIÊNG ε = W(lk)/A, không phải bằng W(lk). "
   "Hạt nhân urani có W(lk) rất lớn nhưng lại kém bền hơn hạt nhân sắt.",
   "So sánh độ bền vững", TB, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu H₀. Sau thời gian bằng 2 chu kì bán rã, "
   "độ phóng xạ của mẫu bằng",
   ["H₀/2.", "H₀/4.", "H₀/8.", "H₀/16."],
   "B",
   "Độ phóng xạ giảm theo cùng quy luật với số hạt nhân: H = H₀·2⁻ⁿ. "
   "Với n = 2 ta có H = H₀/4.",
   "Độ phóng xạ", D),

mc("Nếu tăng gấp đôi khối lượng mẫu chất phóng xạ (cùng loại đồng vị) thì chu kì bán rã của mẫu",
   ["tăng gấp đôi.", "không đổi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "Chu kì bán rã là đặc trưng riêng của từng đồng vị, không phụ thuộc khối lượng mẫu. "
   "Tăng khối lượng chỉ làm ĐỘ PHÓNG XẠ tăng gấp đôi vì N tăng gấp đôi.",
   "Đặc điểm của chu kì bán rã", TB),
],
P2=[
ds("Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ, độ phóng xạ ban đầu 800 kBq.",
   [("Hằng số phóng xạ của chất đó xấp xỉ 0,173 giờ⁻¹.", True,
     "Đúng. λ = ln2/T = 0,693/4,0 ≈ 0,173 (giờ⁻¹)."),
    ("Sau 4,0 giờ, độ phóng xạ của mẫu còn 400 kBq.", True,
     "Đúng. Sau đúng một chu kì bán rã, độ phóng xạ giảm một nửa."),
    ("Sau 8,0 giờ, độ phóng xạ của mẫu còn 200 kBq.", True,
     "Đúng. n = 2 ⇒ H = 800/4 = 200 kBq."),
    ("Đồ thị của độ phóng xạ theo thời gian là một đường thẳng đi xuống.", False,
     "Sai. H giảm theo hàm mũ nên đồ thị H(t) là đường cong. Chỉ đồ thị lnH theo t mới là "
     "đường thẳng với hệ số góc −λ.")],
   "Độ phóng xạ", TB, fig="h_dt_H_t", cap="Độ phóng xạ theo thời gian"),

ds("Hạt nhân ²¹⁰₈₄Po phóng xạ α với chu kì bán rã 138 ngày, biến thành hạt nhân chì bền.",
   [("Phương trình phân rã là ²¹⁰₈₄Po → ⁴₂He + ²⁰⁶₈₂Pb.", True,
     "Đúng. Bảo toàn số khối 210 = 4 + 206 và bảo toàn điện tích 84 = 2 + 82."),
    ("Sau 138 ngày, số hạt nhân chì tạo thành bằng số hạt nhân pôlôni còn lại.", True,
     "Đúng. Sau một chu kì, một nửa số hạt Po đã rã thành Pb, một nửa còn lại là Po."),
    ("Sau 414 ngày, tỉ số số hạt nhân chì trên số hạt nhân pôlôni còn lại bằng 7.", True,
     "Đúng. 414 ngày = 3 chu kì. Po còn N₀/8, Pb có 7N₀/8, tỉ số bằng 7."),
    ("Chu kì bán rã của pôlôni sẽ giảm nếu mẫu được nung nóng tới 500 °C.", False,
     "Sai. Chu kì bán rã hoàn toàn không phụ thuộc nhiệt độ hay bất kì tác động bên ngoài nào.")],
   "Phân rã của pôlôni", TB, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã của pôlôni"),

ds("Một nhà máy điện hạt nhân dùng nhiên liệu ²³⁵U, mỗi phân hạch toả 200 MeV.",
   [("Số hạt nhân trong 1,0 kg ²³⁵U xấp xỉ 2,56·10²⁴ hạt.", True,
     "Đúng. N = (1000/235)·6,02·10²³ ≈ 2,56·10²⁴ hạt."),
    ("Năng lượng toả ra khi phân hạch hoàn toàn 1,0 kg ²³⁵U xấp xỉ 8,2·10¹³ J.", True,
     "Đúng. E = 2,56·10²⁴ · 200 · 1,6·10⁻¹³ ≈ 8,2·10¹³ J."),
    ("Năng lượng đó lớn hơn nhiều lần năng lượng toả ra khi đốt cháy 1,0 kg than đá.", True,
     "Đúng. Đốt 1 kg than chỉ toả cỡ 3·10⁷ J, nhỏ hơn khoảng gần ba triệu lần."),
    ("Toàn bộ năng lượng đó được biến trực tiếp thành điện năng trong nhà máy.", False,
     "Sai. Năng lượng hạt nhân trước hết chuyển thành nhiệt, rồi qua hơi nước và tua bin mới thành "
     "điện năng; hiệu suất toàn phần chỉ khoảng 30–35 %.")],
   "Năng lượng của nhiên liệu hạt nhân", TB, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

ds("Xét một hạt nhân đứng yên phóng xạ α.",
   [("Tổng động lượng của hạt α và hạt nhân con bằng không.", True,
     "Đúng. Hạt nhân mẹ đứng yên nên tổng động lượng ban đầu bằng 0 và được bảo toàn."),
    ("Hai hạt sinh ra bay theo hai hướng ngược nhau.", True,
     "Đúng. Đó là hệ quả trực tiếp của việc tổng động lượng bằng không."),
    ("Hạt α có động năng lớn hơn hạt nhân con vì nó nhẹ hơn nhiều.", True,
     "Đúng. Với cùng độ lớn động lượng p, động năng W = p²/(2m) tỉ lệ nghịch với khối lượng, "
     "nên hạt nhẹ mang phần lớn động năng."),
    ("Tổng khối lượng nghỉ của hạt α và hạt nhân con bằng khối lượng nghỉ của hạt nhân mẹ.", False,
     "Sai. Tổng khối lượng nghỉ sau phân rã NHỎ hơn khối lượng hạt nhân mẹ; phần chênh lệch "
     "đã chuyển thành động năng của hai hạt.")],
   "Bảo toàn động lượng và năng lượng", K),
],
P3=[
sa("Một chất phóng xạ có hằng số phóng xạ 0,0231 giờ⁻¹. Chu kì bán rã của chất đó bằng bao nhiêu "
   "giờ (làm tròn đến hàng đơn vị)? Lấy ln2 ≈ 0,693.",
   "30",
   "Từ λ = ln2/T suy ra T = ln2/λ = 0,693/0,0231 = 30 giờ.",
   "Hằng số phóng xạ – bài toán ngược", TB),

sa("Một chất phóng xạ có chu kì bán rã 3,0 giờ, độ phóng xạ ban đầu 640 kBq. "
   "Sau 9,0 giờ, độ phóng xạ của mẫu bằng bao nhiêu kilôbecơren?",
   "80",
   "Số chu kì: n = 9,0/3,0 = 3.\n"
   "H = H₀·2⁻³ = 640/8 = 80 kBq.",
   "Độ phóng xạ", TB),

sa("Hạt nhân ²¹⁰₈₄Po phóng xạ α với chu kì bán rã 138 ngày. Sau 552 ngày, tỉ số giữa số hạt nhân "
   "chì tạo thành và số hạt nhân pôlôni còn lại bằng bao nhiêu?",
   "15",
   "Số chu kì: n = 552/138 = 4.\n"
   "Po còn lại N₀/16; Pb tạo thành N₀ − N₀/16 = 15N₀/16.\n"
   "Tỉ số bằng 15.",
   "Tỉ số hạt nhân con và mẹ", TB, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

sa("Năng lượng liên kết riêng của hạt nhân ⁵⁶₂₆Fe là 8,8 MeV/nuclêôn. Năng lượng liên kết của "
   "hạt nhân này bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ nhất)?",
   "492,8",
   "W(lk) = ε·A = 8,8 · 56 = 492,8 MeV.",
   "Năng lượng liên kết", TB),

sa("Năng lượng toả ra khi phân hạch hoàn toàn 0,50 gam ²³⁵U bằng bao nhiêu jun "
   "(viết dưới dạng x·10¹⁰, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ nhất)? "
   "Mỗi phân hạch toả 200 MeV; Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   "4,1",
   "Số hạt nhân: N = (0,50/235) · 6,02·10²³ ≈ 1,281·10²¹ hạt.\n"
   "Tổng năng lượng: E = 1,281·10²¹ · 200 = 2,562·10²³ MeV.\n"
   "Đổi sang jun: E = 2,562·10²³ · 1,6·10⁻¹³ ≈ 4,1·10¹⁰ J.",
   "Năng lượng của nhiên liệu hạt nhân", K),

sa("Trong một giờ, một mẫu chất phóng xạ có 1,8·10¹² phân rã xảy ra. Độ phóng xạ trung bình của "
   "mẫu trong giờ đó bằng bao nhiêu mêgabecơren (làm tròn đến hàng đơn vị)?",
   "500",
   "Đổi thời gian: 1 giờ = 3600 s.\n"
   "H = số phân rã / thời gian = 1,8·10¹²/3600 = 5,0·10⁸ Bq = 500 MBq.",
   "Ý nghĩa của độ phóng xạ", TB),
])


# =====================================================================  ĐỀ 5
DE5 = dict(
ma="12C4-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Bài toán logarit, năng lượng phản ứng theo nhiều cách, tỉ số khối lượng",
P1=[
mc("Một chất phóng xạ có chu kì bán rã 10 giờ. Sau bao lâu thì độ phóng xạ còn 30 % giá trị "
   "ban đầu (lấy ln2 ≈ 0,693)?",
   ["12,0 giờ.", "17,4 giờ.", "20,0 giờ.", "24,0 giờ."],
   "B",
   "Đặt n = t/T. Từ H = H₀·2⁻ⁿ và H/H₀ = 0,30 ⇒ 2⁻ⁿ = 0,30.\n"
   "n = ln(1/0,30)/ln2 = 1,204/0,693 ≈ 1,737.\n"
   "t = n·T = 1,737 · 10 ≈ 17,4 giờ.\n"
   "Kiểm tra hợp lí: 30 % nằm giữa 50 % (sau 1T) và 25 % (sau 2T) nên t phải nằm giữa 10 h và 20 h.",
   "Định luật phóng xạ – dùng logarit", TB),

mc("Một mẫu chất phóng xạ sau 20 ngày còn lại 1/8 số hạt nhân ban đầu. Chu kì bán rã của chất đó là",
   ["4,0 ngày.", "6,7 ngày.", "10 ngày.", "2,5 ngày."],
   "B",
   "1/8 = 2⁻³ nên n = 3 chu kì.\n"
   "T = t/n = 20/3 ≈ 6,7 ngày.",
   "Định luật phóng xạ – bài toán ngược", TB),

mc("Hạt nhân ²¹⁰₈₄Po phóng xạ α thành ²⁰⁶₈₂Pb. Sau 2 chu kì bán rã, tỉ số giữa KHỐI LƯỢNG chì "
   "tạo thành và khối lượng pôlôni còn lại xấp xỉ",
   ["3,00.", "2,94.", "3,06.", "1,50."],
   "B",
   "Sau 2 chu kì, số hạt Po còn N₀/4, số hạt Pb là 3N₀/4.\n"
   "Tỉ số khối lượng phải nhân thêm tỉ số số khối:\n"
   "m(Pb)/m(Po) = (3N₀/4 · 206)/(N₀/4 · 210) = 3 · 206/210 ≈ 2,94.\n"
   "Nếu quên hệ số số khối sẽ ra đúng 3,00 — đó là phương án nhiễu.",
   "Tỉ số khối lượng con và mẹ", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

mc("Cho phản ứng: ²³⁵₉₂U + ¹₀n → ⁹⁵₃₉Y + ¹³⁸₅₃I + k·¹₀n. Giá trị của k là",
   ["2.", "3.", "4.", "1."],
   "B",
   "Bảo toàn số khối: 235 + 1 = 95 + 138 + k ⇒ 236 = 233 + k ⇒ k = 3.\n"
   "Kiểm tra điện tích: 92 + 0 = 39 + 53 + 0 ⇒ 92 = 92 ✓.",
   "Phản ứng phân hạch", TB, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Biết năng lượng liên kết riêng của ²H là 1,11 MeV/nuclêôn, của ³H là 2,83 MeV/nuclêôn và của "
   "⁴He là 7,10 MeV/nuclêôn. Năng lượng toả ra của phản ứng ²₁H + ³₁H → ⁴₂He + ¹₀n xấp xỉ",
   ["12,4 MeV.", "17,6 MeV.", "22,1 MeV.", "8,8 MeV."],
   "B",
   "Năng lượng liên kết trước: 2 · 1,11 + 3 · 2,83 = 2,22 + 8,49 = 10,71 MeV "
   "(nơtron tự do có W(lk) = 0).\n"
   "Năng lượng liên kết sau: 4 · 7,10 = 28,40 MeV.\n"
   "ΔE = 28,40 − 10,71 = 17,69 ≈ 17,6 MeV.",
   "Năng lượng phản ứng theo W(lk)", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Một hạt nhân đứng yên phóng xạ α, toả ra năng lượng 5,4 MeV. Nếu bỏ qua bức xạ γ và coi khối "
   "lượng tỉ lệ với số khối, động năng của hạt α trong phân rã ²¹⁰Po → ²⁰⁶Pb xấp xỉ",
   ["0,10 MeV.", "5,30 MeV.", "2,70 MeV.", "5,40 MeV."],
   "B",
   "Bảo toàn động lượng: p(α) = p(Pb) nên W(α)·m(α) = W(Pb)·m(Pb).\n"
   "Suy ra W(α)/W(Pb) = m(Pb)/m(α) = 206/4.\n"
   "W(α) = ΔE · 206/(206 + 4) = 5,4 · 206/210 ≈ 5,30 MeV.\n"
   "Hạt nhẹ mang gần như toàn bộ năng lượng toả ra.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một mẫu chất phóng xạ nguyên chất ban đầu có khối lượng m₀. Sau thời gian t, khối lượng "
   "chất đó còn lại 25 % và tạo thành 1,2 gam hạt nhân con. Nếu số khối của mẹ và con xấp xỉ "
   "bằng nhau thì m₀ bằng",
   ["1,2 gam.", "1,6 gam.", "2,4 gam.", "4,8 gam."],
   "B",
   "Còn 25 % nghĩa là đã rã 75 %. Vì số khối gần bằng nhau nên khối lượng con ≈ khối lượng mẹ đã rã.\n"
   "0,75·m₀ = 1,2 ⇒ m₀ = 1,6 gam.",
   "Định luật phóng xạ – khối lượng", TB),

mc("Chất phóng xạ A có chu kì bán rã 2 giờ, chất B có chu kì bán rã 4 giờ. Ban đầu hai mẫu có "
   "cùng số hạt nhân. Sau 4 giờ, tỉ số số hạt nhân còn lại của A so với B bằng",
   ["1 : 1.", "1 : 2.", "2 : 1.", "1 : 4."],
   "B",
   "Sau 4 giờ, A trải qua 2 chu kì nên còn N₀/4; B trải qua 1 chu kì nên còn N₀/2.\n"
   "Tỉ số: (N₀/4)/(N₀/2) = 1 : 2.",
   "So sánh hai chất phóng xạ", TB),

mc("Trong phản ứng hạt nhân thu năng lượng, để phản ứng xảy ra được thì các hạt tới phải",
   ["đứng yên.", "có động năng đủ lớn.",
    "mang điện tích âm.", "có khối lượng nhỏ."],
   "B",
   "Phản ứng thu năng lượng có tổng khối lượng nghỉ sau lớn hơn trước, nên phải được cung cấp "
   "năng lượng từ động năng của các hạt tới. Nếu các hạt đứng yên thì phản ứng không thể xảy ra.",
   "Phản ứng thu năng lượng", TB),

mc("Một lò phản ứng hạt nhân có công suất nhiệt 2000 MW. Mỗi phân hạch toả 200 MeV "
   "(1 MeV = 1,6·10⁻¹³ J). Số phân hạch xảy ra trong một giây xấp xỉ",
   ["6,25·10¹⁸.", "6,25·10¹⁹.", "6,25·10²⁰.", "3,20·10¹⁹."],
   "B",
   "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "Số phân hạch mỗi giây: 2,0·10⁹/3,2·10⁻¹¹ = 6,25·10¹⁹.",
   "Công suất lò phản ứng", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Một mẫu chất phóng xạ có độ phóng xạ 1,0·10⁶ Bq và hằng số phóng xạ 2,0·10⁻⁴ s⁻¹. "
   "Số hạt nhân chưa phân rã trong mẫu bằng",
   ["2,0·10²  hạt.", "5,0·10⁹ hạt.", "2,0·10¹⁰ hạt.", "5,0·10⁸ hạt."],
   "B",
   "Từ H = λ·N suy ra N = H/λ = 1,0·10⁶/2,0·10⁻⁴ = 5,0·10⁹ hạt.",
   "Độ phóng xạ và số hạt nhân", TB),

mc("Hạt nhân nào sau đây bền vững nhất, biết năng lượng liên kết riêng lần lượt là: "
   "X: 7,6; Y: 8,8; Z: 7,1; T: 6,2 MeV/nuclêôn?",
   ["Hạt nhân X.", "Hạt nhân Y.", "Hạt nhân Z.", "Hạt nhân T."],
   "B",
   "Năng lượng liên kết riêng càng lớn thì hạt nhân càng bền vững. Y có ε = 8,8 MeV/nuclêôn "
   "lớn nhất nên bền vững nhất — đó chính là vùng số khối quanh A ≈ 56.",
   "So sánh độ bền vững", D, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Trong phân rã β⁻, hạt nhân phát ra electron. Electron này",
   ["vốn có sẵn trong lớp vỏ nguyên tử.",
    "được sinh ra từ quá trình một nơtron biến thành prôtôn trong hạt nhân.",
    "là một prôtôn mất điện tích.",
    "vốn có sẵn trong hạt nhân từ trước."],
   "B",
   "Hạt nhân không chứa sẵn electron. Trong phân rã β⁻, một nơtron biến thành prôtôn đồng thời "
   "sinh ra một electron (và một phản nơtrinô), giải thích vì sao Z tăng 1 còn A không đổi.",
   "Bản chất của phân rã beta", K),

mc("Một mẫu chất phóng xạ ban đầu có độ phóng xạ H₀. Sau 12 giờ, độ phóng xạ còn H₀/16. "
   "Chu kì bán rã của chất đó bằng",
   ["2,0 giờ.", "3,0 giờ.", "4,0 giờ.", "6,0 giờ."],
   "B",
   "1/16 = 2⁻⁴ nên n = 4 chu kì.\n"
   "T = 12/4 = 3,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB),

mc("Người ta dùng đồng vị có chu kì bán rã ngắn trong chẩn đoán y học nhằm",
   ["tăng độ chính xác của phép đo.", "giảm liều chiếu mà bệnh nhân phải nhận.",
    "giảm giá thành sản xuất.", "tăng khả năng đâm xuyên."],
   "B",
   "Chu kì bán rã ngắn giúp đồng vị phân rã hết nhanh chóng sau khi hoàn thành phép chụp, "
   "nên tổng liều chiếu mà bệnh nhân nhận được giảm đáng kể.",
   "Ứng dụng trong y học", TB, fig="h_sd_ung_dung", cap="Ứng dụng của đồng vị phóng xạ"),

mc("Trong một phản ứng hạt nhân, tổng độ hụt khối của các hạt trước là 0,0450 u và của các hạt sau "
   "là 0,0640 u. Phản ứng này",
   ["thu năng lượng 17,7 MeV.", "toả năng lượng 17,7 MeV.",
    "toả năng lượng 101,5 MeV.", "không trao đổi năng lượng."],
   "B",
   "ΔE = (Δm sau − Δm trước)·931,5 = (0,0640 − 0,0450) · 931,5 = 0,0190 · 931,5 ≈ 17,7 MeV.\n"
   "Độ hụt khối sau LỚN hơn nghĩa là các hạt nhân sau bền vững hơn, phản ứng TOẢ năng lượng.",
   "Năng lượng phản ứng theo độ hụt khối", K),

mc("Khi một hạt nhân bị bắn phá và vỡ ra, tổng số nuclêôn",
   ["tăng lên.", "được bảo toàn.", "giảm đi.", "thay đổi tuỳ phản ứng."],
   "B",
   "Định luật bảo toàn số khối luôn đúng trong mọi phản ứng hạt nhân: tổng số nuclêôn trước "
   "bằng tổng số nuclêôn sau. Chỉ có khối lượng nghỉ là không bảo toàn.",
   "Định luật bảo toàn", D),

mc("Hai mẫu của cùng một đồng vị phóng xạ có khối lượng lần lượt là m và 3m. So sánh CHU KÌ BÁN RÃ "
   "và ĐỘ PHÓNG XẠ ban đầu của hai mẫu:",
   ["chu kì bán rã khác nhau, độ phóng xạ bằng nhau.",
    "chu kì bán rã bằng nhau, độ phóng xạ mẫu thứ hai lớn gấp ba.",
    "cả hai đại lượng đều bằng nhau.",
    "cả hai đại lượng của mẫu thứ hai đều gấp ba."],
   "B",
   "Chu kì bán rã là hằng số của đồng vị, không phụ thuộc khối lượng mẫu. "
   "Độ phóng xạ H = λ·N tỉ lệ thuận với số hạt nhân, tức tỉ lệ thuận với khối lượng, "
   "nên mẫu 3m có độ phóng xạ gấp ba.",
   "Độ phóng xạ và khối lượng", TB),
],
P2=[
ds("Một chất phóng xạ có chu kì bán rã 12 giờ, ban đầu có 4,8·10²² hạt nhân.",
   [("Hằng số phóng xạ của chất đó xấp xỉ 0,0578 giờ⁻¹.", True,
     "Đúng. λ = 0,693/12 ≈ 0,05775 ≈ 0,0578 (giờ⁻¹)."),
    ("Sau 36 giờ, số hạt nhân còn lại là 6,0·10²¹ hạt.", True,
     "Đúng. n = 36/12 = 3 ⇒ N = 4,8·10²²/8 = 6,0·10²¹ hạt."),
    ("Sau 36 giờ, số hạt nhân đã phân rã là 4,2·10²² hạt.", True,
     "Đúng. ΔN = 4,8·10²² − 6,0·10²¹ = 4,2·10²² hạt."),
    ("Sau 48 giờ, số hạt nhân còn lại bằng đúng một phần năm số hạt ban đầu.", False,
     "Sai. n = 48/12 = 4 nên còn lại 1/16 số hạt ban đầu, tức 3,0·10²¹ hạt, "
     "không phải một phần năm.")],
   "Định luật phóng xạ", TB),

ds("Cho phản ứng nhiệt hạch ²₁H + ²₁H → ³₂He + ¹₀n với năng lượng liên kết riêng: "
   "²H là 1,11 MeV/nuclêôn và ³He là 2,57 MeV/nuclêôn.",
   [("Phản ứng bảo toàn số khối: 2 + 2 = 3 + 1.", True,
     "Đúng. Tổng số khối hai vế đều bằng 4."),
    ("Năng lượng liên kết tổng cộng của các hạt trước phản ứng là 4,44 MeV.", True,
     "Đúng. 2 hạt ²H, mỗi hạt có W(lk) = 2 · 1,11 = 2,22 MeV, tổng cộng 4,44 MeV."),
    ("Năng lượng liên kết của hạt ³He là 7,71 MeV.", True,
     "Đúng. W(lk) = 3 · 2,57 = 7,71 MeV; nơtron tự do có W(lk) = 0."),
    ("Phản ứng thu năng lượng 3,27 MeV.", False,
     "Sai về CHIỀU trao đổi. ΔE = 7,71 − 4,44 = 3,27 MeV nhưng vì năng lượng liên kết sau LỚN hơn "
     "trước nên phản ứng TOẢ năng lượng 3,27 MeV.")],
   "Năng lượng phản ứng theo W(lk)", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

ds("Một lò phản ứng hạt nhân có công suất nhiệt 1500 MW, dùng nhiên liệu ²³⁵U, "
   "mỗi phân hạch toả 200 MeV. Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   [("Năng lượng toả ra trong mỗi phân hạch là 3,2·10⁻¹¹ J.", True,
     "Đúng. 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J."),
    ("Số phân hạch xảy ra trong một giây xấp xỉ 4,69·10¹⁹.", True,
     "Đúng. 1,5·10⁹/3,2·10⁻¹¹ ≈ 4,69·10¹⁹ phân hạch mỗi giây."),
    ("Trong một ngày, lò tiêu thụ khoảng 1,58 kg ²³⁵U.", True,
     "Đúng. Số hạt trong một ngày: 4,69·10¹⁹ · 86 400 ≈ 4,05·10²⁴ hạt "
     "⇒ khối lượng ≈ (4,05·10²⁴/6,02·10²³) · 235 ≈ 1581 g ≈ 1,58 kg."),
    ("Toàn bộ 1500 MW đó là công suất điện mà lò phát lên lưới.", False,
     "Sai. Đó là công suất NHIỆT. Công suất điện chỉ bằng khoảng 30–35 % công suất nhiệt "
     "do giới hạn hiệu suất của chu trình hơi nước.")],
   "Công suất và nhiên liệu của lò phản ứng", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

ds("Một hạt nhân ²¹⁰Po đứng yên phóng xạ α, toả ra năng lượng 5,4 MeV. Bỏ qua bức xạ γ và coi "
   "khối lượng các hạt tỉ lệ với số khối.",
   [("Hai hạt sinh ra có động lượng cùng độ lớn, ngược hướng.", True,
     "Đúng. Hạt nhân mẹ đứng yên nên tổng động lượng bằng 0 và được bảo toàn."),
    ("Tỉ số động năng của hạt α và hạt nhân con bằng 206 : 4.", True,
     "Đúng. Với cùng độ lớn động lượng, W = p²/(2m) nên động năng tỉ lệ nghịch với khối lượng."),
    ("Động năng của hạt α xấp xỉ 5,30 MeV.", True,
     "Đúng. W(α) = 5,4 · 206/210 ≈ 5,30 MeV."),
    ("Động năng của hạt nhân con lớn hơn động năng của hạt α vì nó nặng hơn.", False,
     "Sai. Ngược lại: hạt NẶNG hơn mang ÍT động năng hơn. Động năng hạt nhân con chỉ khoảng "
     "5,4 − 5,30 = 0,10 MeV.")],
   "Bảo toàn động lượng trong phân rã", K),
],
P3=[
sa("Một chất phóng xạ có chu kì bán rã 8,0 giờ. Sau bao nhiêu giờ thì số hạt nhân chưa phân rã "
   "còn 20 % so với ban đầu (làm tròn đến chữ số thập phân thứ nhất)? Lấy ln2 ≈ 0,693.",
   "18,6",
   "Đặt n = t/T. Từ N = N₀·2⁻ⁿ và N/N₀ = 0,20 ⇒ 2⁻ⁿ = 0,20.\n"
   "n = ln5/ln2 = 1,609/0,693 ≈ 2,322.\n"
   "t = n·T = 2,322 · 8,0 ≈ 18,6 giờ.",
   "Định luật phóng xạ – dùng logarit", K),

sa("Hạt nhân ²¹⁰₈₄Po phóng xạ α thành ²⁰⁶₈₂Pb với chu kì bán rã 138 ngày. Sau 276 ngày, tỉ số giữa "
   "khối lượng chì tạo thành và khối lượng pôlôni còn lại bằng bao nhiêu (làm tròn đến chữ số "
   "thập phân thứ hai)?",
   "2,94",
   "Sau 276 ngày = 2 chu kì: Po còn N₀/4 hạt, Pb tạo thành 3N₀/4 hạt.\n"
   "Khối lượng tỉ lệ với tích số hạt × số khối:\n"
   "m(Pb)/m(Po) = (3N₀/4 · 206)/(N₀/4 · 210) = 3 · 206/210 = 618/210 ≈ 2,94.",
   "Tỉ số khối lượng con và mẹ", K, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

sa("Cho phản ứng: ²³⁵₉₂U + ¹₀n → ¹⁴⁰₅₄Xe + ⁹⁴₃₈Sr + k·¹₀n. Giá trị của k bằng bao nhiêu?",
   "2",
   "Bảo toàn số khối: 235 + 1 = 140 + 94 + k ⇒ 236 = 234 + k ⇒ k = 2.\n"
   "Kiểm tra điện tích: 92 + 0 = 54 + 38 + 0 ⇒ 92 = 92 ✓.",
   "Phản ứng phân hạch", TB, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

sa("Một mẫu chất phóng xạ có độ phóng xạ 2,4·10⁷ Bq và hằng số phóng xạ 4,0·10⁻⁵ s⁻¹. "
   "Số hạt nhân chưa phân rã trong mẫu bằng bao nhiêu (viết dưới dạng x·10¹¹, chỉ ghi giá trị x)?",
   "6",
   "Từ H = λ·N ⇒ N = H/λ = 2,4·10⁷/4,0·10⁻⁵ = 6,0·10¹¹ hạt.",
   "Độ phóng xạ và số hạt nhân", TB),

sa("Một lò phản ứng hạt nhân có công suất nhiệt 800 MW, mỗi phân hạch toả 200 MeV. "
   "Số phân hạch xảy ra trong một giây bằng bao nhiêu (viết dưới dạng x·10¹⁹, chỉ ghi giá trị x)? "
   "Cho 1 MeV = 1,6·10⁻¹³ J.",
   "2,5",
   "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "Số phân hạch mỗi giây: 8,0·10⁸/3,2·10⁻¹¹ = 2,5·10¹⁹.",
   "Công suất lò phản ứng", K),

sa("Biết năng lượng liên kết riêng của ²H là 1,11 MeV/nuclêôn và của ⁴He là 7,10 MeV/nuclêôn. "
   "Năng lượng toả ra của phản ứng ²₁H + ²₁H → ⁴₂He bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "23,96",
   "Năng lượng liên kết trước: 2 hạt ²H, mỗi hạt 2 · 1,11 = 2,22 MeV ⇒ tổng 4,44 MeV.\n"
   "Năng lượng liên kết sau: 4 · 7,10 = 28,40 MeV.\n"
   "ΔE = 28,40 − 4,44 = 23,96 MeV.",
   "Năng lượng phản ứng theo W(lk)", K),
])


# =====================================================================  ĐỀ 6
DE6 = dict(
ma="12C4-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Đọc đồ thị bán logarit, phản ứng hạt nhân có động năng, hai chất phóng xạ",
P1=[
mc("Đồ thị lnH theo thời gian của một chất phóng xạ là đường thẳng có hệ số góc −0,231 giờ⁻¹. "
   "Chu kì bán rã của chất đó bằng",
   ["1,5 giờ.", "3,0 giờ.", "4,5 giờ.", "6,0 giờ."],
   "B",
   "Hệ số góc của đường thẳng lnH theo t chính là −λ nên λ = 0,231 giờ⁻¹.\n"
   "T = ln2/λ = 0,693/0,231 = 3,0 giờ.",
   "Đồ thị bán logarit", TB, fig="h_dt_H_t", cap="Đồ thị lnH theo thời gian"),

mc("Chất phóng xạ A có chu kì bán rã 2 giờ, chất B có chu kì bán rã 4 giờ. Ban đầu số hạt nhân A "
   "gấp 4 lần số hạt nhân B. Sau bao lâu thì số hạt nhân của hai chất bằng nhau?",
   ["4 giờ.", "8 giờ.", "6 giờ.", "12 giờ."],
   "B",
   "Đặt số hạt ban đầu của B là N₀ thì của A là 4N₀.\n"
   "4N₀·2^(−t/2) = N₀·2^(−t/4)  ⇒  2² · 2^(−t/2) = 2^(−t/4).\n"
   "So sánh số mũ: 2 − t/2 = −t/4 ⇒ 2 = t/4 ⇒ t = 8 giờ.",
   "Hai chất phóng xạ", K),

mc("Cho phản ứng ¹₁H + ⁷₃Li → 2·⁴₂He. Biết m(p) = 1,0073 u; m(Li) = 7,0160 u; m(He) = 4,0015 u; "
   "1 u·c² = 931,5 MeV. Năng lượng toả ra của phản ứng xấp xỉ",
   ["9,5 MeV.", "18,9 MeV.", "28,4 MeV.", "37,8 MeV."],
   "B",
   "Tổng khối lượng trước: 1,0073 + 7,0160 = 8,0233 u.\n"
   "Tổng khối lượng sau: 2 · 4,0015 = 8,0030 u.\n"
   "Δm = 8,0233 − 8,0030 = 0,0203 u.\n"
   "ΔE = 0,0203 · 931,5 ≈ 18,9 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

mc("Một mẫu đá chứa ²³⁸U và sản phẩm cuối cùng ²⁰⁶Pb. Tỉ số số hạt nhân Pb trên số hạt nhân U "
   "còn lại là 0,60. Chu kì bán rã của ²³⁸U là 4,5·10⁹ năm. Tuổi của mẫu đá xấp xỉ",
   ["1,5·10⁹ năm.", "3,05·10⁹ năm.", "4,5·10⁹ năm.", "6,0·10⁹ năm."],
   "B",
   "Đặt n = t/T. Tỉ số con/mẹ bằng 2ⁿ − 1 = 0,60 ⇒ 2ⁿ = 1,60.\n"
   "n = ln1,60/ln2 = 0,470/0,693 ≈ 0,678.\n"
   "t = 0,678 · 4,5·10⁹ ≈ 3,05·10⁹ năm.",
   "Xác định tuổi mẫu đá", K),

mc("Khối lượng tương ứng với năng lượng 1 MeV bằng (c = 3,0·10⁸ m/s; 1 MeV = 1,6·10⁻¹³ J)",
   ["1,78·10⁻²⁸ kg.", "1,78·10⁻³⁰ kg.", "1,78·10⁻³² kg.", "5,33·10⁻²² kg."],
   "B",
   "Từ E = m·c² suy ra m = E/c² = 1,6·10⁻¹³/(9,0·10¹⁶) ≈ 1,78·10⁻³⁰ kg.\n"
   "Giá trị này xấp xỉ hai lần khối lượng electron, phù hợp với việc năng lượng nghỉ của "
   "electron là 0,511 MeV.",
   "Hệ thức khối lượng – năng lượng", K),

mc("Một mẫu chất phóng xạ ban đầu nguyên chất. Ở thời điểm t₁ tỉ lệ hạt nhân đã rã là 75 %; "
   "ở thời điểm t₂ = t₁ + 2T tỉ lệ đó là",
   ["87,5 %.", "93,75 %.", "81,25 %.", "96,875 %."],
   "B",
   "Đã rã 75 % nghĩa là còn 25 % = 2⁻², tức t₁ = 2T.\n"
   "t₂ = 2T + 2T = 4T ⇒ còn lại 2⁻⁴ = 6,25 % ⇒ đã rã 93,75 %.",
   "Định luật phóng xạ", TB),

mc("Trong phản ứng phân hạch, các mảnh vỡ thường là những hạt nhân",
   ["rất nhẹ như hiđrô và heli.", "trung bình, có số khối khoảng 90 đến 140.",
    "nặng hơn hạt nhân ban đầu.", "có số khối bằng nhau chính xác."],
   "B",
   "Hạt nhân ²³⁵U thường vỡ thành hai mảnh không bằng nhau, số khối nằm trong khoảng 90–140. "
   "Đây là vùng có năng lượng liên kết riêng lớn hơn nên phản ứng toả năng lượng.",
   "Phản ứng phân hạch", TB, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Nếu tính trên cùng một khối lượng nhiên liệu, phản ứng nào toả nhiều năng lượng nhất?",
   ["Đốt than đá.", "Phản ứng nhiệt hạch.",
    "Phản ứng phân hạch.", "Phản ứng hoá học tổng hợp amoniac."],
   "B",
   "Tính trên mỗi nuclêôn, nhiệt hạch toả khoảng 3,5 MeV còn phân hạch chỉ khoảng 0,85 MeV. "
   "Cả hai đều lớn hơn phản ứng hoá học (cỡ vài eV) hàng triệu lần.",
   "So sánh các nguồn năng lượng", TB, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Một nguồn phóng xạ điểm gây ra liều chiếu 8,0 mSv/giờ ở khoảng cách 1,0 m. "
   "Ở khoảng cách 4,0 m, liều chiếu bằng",
   ["2,0 mSv/giờ.", "0,50 mSv/giờ.", "1,0 mSv/giờ.", "0,25 mSv/giờ."],
   "B",
   "Liều chiếu giảm theo bình phương khoảng cách. Khoảng cách tăng 4 lần nên liều giảm 16 lần: "
   "8,0/16 = 0,50 mSv/giờ.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("Trong phản ứng hạt nhân, nếu tổng động năng của các hạt sau lớn hơn tổng động năng của các hạt "
   "trước thì phản ứng đó",
   ["thu năng lượng.", "toả năng lượng.",
    "không xảy ra được.", "không trao đổi năng lượng."],
   "B",
   "Năng lượng toả ra của phản ứng chuyển thành động năng của các hạt sản phẩm. "
   "Động năng tăng nghĩa là phản ứng đã lấy năng lượng từ phần khối lượng nghỉ bị hụt đi — "
   "phản ứng toả năng lượng.",
   "Năng lượng phản ứng hạt nhân", TB),

mc("Hai hạt nhân có cùng số khối A nhưng khác số prôtôn được gọi là",
   ["đồng vị.", "đồng khối.", "đồng lượng.", "cùng một nguyên tố."],
   "B",
   "Các hạt nhân cùng A khác Z gọi là đồng khối (ví dụ ¹⁴C và ¹⁴N). Đồng vị mới là các hạt nhân "
   "cùng Z khác A.",
   "Phân loại hạt nhân", TB),

mc("Một chất phóng xạ có chu kì bán rã T. Khoảng thời gian để số hạt nhân giảm từ N₀ xuống N₀/8 "
   "so với khoảng thời gian để giảm tiếp từ N₀/8 xuống N₀/64 thì",
   ["dài gấp đôi.", "bằng nhau.", "ngắn bằng một nửa.", "dài gấp ba."],
   "B",
   "Từ N₀ xuống N₀/8 mất 3T; từ N₀/8 xuống N₀/64 cũng giảm đi 8 lần nên cũng mất 3T. "
   "Đặc trưng của quy luật hàm mũ: thời gian để giảm cùng một TỈ LỆ luôn như nhau.",
   "Bản chất hàm mũ của phân rã", K),

mc("Trong lò phản ứng, nếu rút thanh điều khiển ra xa vùng hoạt động thì",
   ["hệ số nhân nơtron giảm.", "hệ số nhân nơtron tăng.",
    "hệ số nhân nơtron không đổi.", "phản ứng dừng ngay lập tức."],
   "B",
   "Thanh điều khiển hấp thụ nơtron. Rút thanh ra thì ít nơtron bị hấp thụ hơn, nhiều nơtron hơn "
   "tham gia gây phân hạch, nên hệ số nhân nơtron tăng và công suất lò tăng.",
   "Điều khiển lò phản ứng", TB, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),

mc("Khối lượng nghỉ của electron tương ứng với năng lượng",
   ["0,511 keV.", "0,511 MeV.", "5,11 MeV.", "931,5 MeV."],
   "B",
   "m(e) = 0,00055 u nên năng lượng nghỉ là 0,00055 · 931,5 ≈ 0,512 MeV, thường lấy 0,511 MeV.",
   "Năng lượng nghỉ", TB),

mc("Trong phân rã β⁺, hạt nhân phát ra pôzitron. So với hạt nhân mẹ, hạt nhân con có",
   ["Z tăng 1.", "Z giảm 1.", "A giảm 1.", "A tăng 1."],
   "B",
   "Pôzitron mang điện tích +e nên để bảo toàn điện tích, Z của hạt nhân con phải giảm 1. "
   "Số khối không đổi vì pôzitron có A = 0.",
   "Quy tắc dịch chuyển", TB, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một mẫu chất phóng xạ được chia thành hai phần bằng nhau. So với mẫu ban đầu, mỗi phần có",
   ["chu kì bán rã giảm một nửa và độ phóng xạ giảm một nửa.",
    "chu kì bán rã như cũ và độ phóng xạ giảm một nửa.",
    "chu kì bán rã như cũ và độ phóng xạ như cũ.",
    "chu kì bán rã tăng gấp đôi."],
   "B",
   "Chu kì bán rã là hằng số của đồng vị, không đổi khi chia nhỏ mẫu. "
   "Độ phóng xạ H = λN tỉ lệ với số hạt nhân nên giảm một nửa.",
   "Độ phóng xạ và chu kì bán rã", TB),

mc("Hạt nhân ²³⁸U trải qua một chuỗi phân rã gồm 8 lần phân rã α và 6 lần phân rã β⁻ để biến "
   "thành hạt nhân bền. Hạt nhân cuối cùng có số khối và điện tích là",
   ["A = 206, Z = 84.", "A = 206, Z = 82.", "A = 222, Z = 82.", "A = 210, Z = 84."],
   "B",
   "Mỗi phân rã α làm A giảm 4 và Z giảm 2; mỗi phân rã β⁻ làm Z tăng 1 và A không đổi.\n"
   "A = 238 − 8·4 = 238 − 32 = 206.\n"
   "Z = 92 − 8·2 + 6·1 = 92 − 16 + 6 = 82.\n"
   "Đó là hạt nhân chì ²⁰⁶₈₂Pb.",
   "Chuỗi phân rã", K),

mc("Một đồng vị phóng xạ có chu kì bán rã rất dài (hàng tỉ năm). So với một đồng vị có chu kì bán rã "
   "vài giờ (cùng số hạt nhân), độ phóng xạ của nó",
   ["lớn hơn nhiều.", "nhỏ hơn rất nhiều.",
    "bằng nhau.", "phụ thuộc nhiệt độ."],
   "B",
   "H = λN = (ln2/T)·N. Chu kì bán rã càng dài thì λ càng nhỏ nên độ phóng xạ càng thấp: "
   "chất phân rã rất chậm nên mỗi giây chỉ có rất ít phân rã.",
   "Độ phóng xạ và chu kì bán rã", TB),
],
P2=[
ds("Từ số liệu thực nghiệm, người ta vẽ được đồ thị lnH theo thời gian t của một mẫu chất phóng xạ "
   "và thu được đường thẳng đi xuống.",
   [("Việc đồ thị là đường thẳng chứng tỏ độ phóng xạ giảm theo quy luật hàm mũ.", True,
     "Đúng. Từ H = H₀·e^(−λt), lấy logarit được lnH = lnH₀ − λt, tức hàm bậc nhất theo t."),
    ("Hệ số góc của đường thẳng bằng −λ.", True,
     "Đúng. Nhờ đó có thể xác định hằng số phóng xạ trực tiếp từ đồ thị."),
    ("Nếu hệ số góc là −0,231 giờ⁻¹ thì chu kì bán rã là 3,0 giờ.", True,
     "Đúng. T = ln2/λ = 0,693/0,231 = 3,0 giờ."),
    ("Giao điểm của đường thẳng với trục tung cho biết chu kì bán rã.", False,
     "Sai. Giao điểm với trục tung có tung độ lnH₀, cho biết ĐỘ PHÓNG XẠ BAN ĐẦU chứ không phải "
     "chu kì bán rã.")],
   "Đồ thị bán logarit", K, fig="h_dt_H_t", cap="Đồ thị lnH theo thời gian"),

ds("Hạt nhân ²³⁸₉₂U biến đổi thành hạt nhân bền ²⁰⁶₈₂Pb qua một chuỗi các phân rã α và β⁻.",
   [("Tổng số lần phân rã α trong chuỗi là 8.", True,
     "Đúng. Chỉ phân rã α làm thay đổi số khối: (238 − 206)/4 = 8 lần."),
    ("Tổng số lần phân rã β⁻ trong chuỗi là 6.", True,
     "Đúng. Sau 8 lần α, Z còn 92 − 16 = 76; muốn tới Z = 82 phải tăng thêm 6 đơn vị, "
     "ứng với 6 lần phân rã β⁻."),
    ("Chuỗi phân rã này làm số nơtron của hạt nhân giảm đi 26.", False,
     "Sai. Số nơtron ban đầu là 238 − 92 = 146, số nơtron cuối là 206 − 82 = 124, "
     "nên chỉ giảm 22 chứ không phải 26. "
     "Có thể kiểm tra theo từng loại phân rã: 8 lần α mất 8·2 = 16 nơtron, "
     "6 lần β⁻ mất thêm 6 nơtron (mỗi lần một nơtron biến thành prôtôn), tổng cộng 22."),
    ("Hạt nhân chì cuối cùng có 124 nơtron.", True,
     "Đúng. N = 206 − 82 = 124 nơtron.")],
   "Chuỗi phân rã", K),

ds("Cho phản ứng ¹₁H + ⁷₃Li → 2·⁴₂He với m(p) = 1,0073 u; m(Li) = 7,0160 u; m(He) = 4,0015 u; "
   "1 u·c² = 931,5 MeV.",
   [("Phản ứng bảo toàn số khối vì 1 + 7 = 2 · 4.", True,
     "Đúng. Tổng số khối hai vế đều bằng 8."),
    ("Tổng khối lượng nghỉ giảm 0,0203 u sau phản ứng.", True,
     "Đúng. 8,0233 − 8,0030 = 0,0203 u."),
    ("Phản ứng toả năng lượng xấp xỉ 18,9 MeV.", True,
     "Đúng. ΔE = 0,0203 · 931,5 ≈ 18,9 MeV."),
    ("Nếu hạt prôtôn tới đứng yên thì phản ứng vẫn xảy ra được như bình thường.", False,
     "Sai. Prôtôn mang điện dương bị hạt nhân liti đẩy mạnh, cần có động năng đủ lớn mới tới gần "
     "được để phản ứng xảy ra.")],
   "Năng lượng phản ứng hạt nhân", K),

ds("Xét nguyên tắc sử dụng an toàn nguồn phóng xạ.",
   [("Ở khoảng cách gấp đôi, liều chiếu từ nguồn điểm giảm 4 lần.", True,
     "Đúng. Liều chiếu tỉ lệ nghịch với bình phương khoảng cách."),
    ("Giảm một nửa thời gian tiếp xúc thì liều chiếu nhận được giảm một nửa.", True,
     "Đúng. Liều chiếu tỉ lệ thuận với thời gian tiếp xúc."),
    ("Sivơ (Sv) là đơn vị đo độ phóng xạ của nguồn.", False,
     "Sai. Độ phóng xạ đo bằng becơren (Bq). Sivơ là đơn vị của liều tương đương, "
     "có tính tới mức nguy hại sinh học của từng loại bức xạ."),
    ("Khi làm việc với nguồn γ, chì là vật liệu che chắn hiệu quả hơn nhôm.", True,
     "Đúng. Chì có mật độ và số nguyên tử lớn nên hấp thụ tia γ mạnh hơn nhôm nhiều.")],
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),
],
P3=[
sa("Đồ thị lnH theo thời gian của một chất phóng xạ là đường thẳng có hệ số góc −0,0866 giờ⁻¹. "
   "Chu kì bán rã của chất đó bằng bao nhiêu giờ (làm tròn đến hàng đơn vị)? Lấy ln2 ≈ 0,693.",
   "8",
   "Hệ số góc bằng −λ nên λ = 0,0866 giờ⁻¹.\n"
   "T = ln2/λ = 0,693/0,0866 ≈ 8,0 giờ.",
   "Đồ thị bán logarit", TB),

sa("Độ phóng xạ của một mẫu chất giảm từ 960 Bq xuống 120 Bq trong 30 phút. "
   "Chu kì bán rã của chất đó bằng bao nhiêu phút?",
   "10",
   "Tỉ số giảm: 960/120 = 8 = 2³ nên đã trôi qua n = 3 chu kì bán rã.\n"
   "T = 30/3 = 10 phút.",
   "Định luật phóng xạ – bài toán ngược", TB),

sa("Một mẫu đá chứa ²³⁸U (chu kì bán rã 4,5·10⁹ năm) và ²⁰⁶Pb. Tỉ số số hạt nhân Pb trên số hạt "
   "nhân U còn lại bằng 3. Tuổi của mẫu đá bằng bao nhiêu tỉ năm?",
   "9",
   "Tỉ số con/mẹ bằng 2ⁿ − 1 = 3 ⇒ 2ⁿ = 4 ⇒ n = 2 chu kì.\n"
   "t = 2 · 4,5·10⁹ = 9,0·10⁹ năm = 9 tỉ năm.",
   "Xác định tuổi mẫu đá", K),

sa("Hạt nhân ²³²₉₀Th biến đổi thành hạt nhân bền ²⁰⁸₈₂Pb qua một chuỗi phân rã α và β⁻. "
   "Số lần phân rã α trong chuỗi bằng bao nhiêu?",
   "6",
   "Chỉ phân rã α mới làm thay đổi số khối, mỗi lần giảm 4 đơn vị:\n"
   "số lần α = (232 − 208)/4 = 24/4 = 6 lần.",
   "Chuỗi phân rã", K),

sa("Một nguồn phóng xạ điểm gây liều chiếu 12 mSv/giờ ở khoảng cách 2,0 m. Muốn liều chiếu chỉ còn "
   "0,75 mSv/giờ thì phải đứng cách nguồn bao nhiêu mét?",
   "8",
   "Liều chiếu tỉ lệ nghịch với bình phương khoảng cách: 12/0,75 = 16 lần.\n"
   "Khoảng cách phải tăng √16 = 4 lần: d = 4 · 2,0 = 8,0 m.",
   "An toàn bức xạ", K),

sa("Một chất phóng xạ có chu kì bán rã T. Sau thời gian 5T, phần trăm số hạt nhân đã bị phân rã "
   "bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ hai)?",
   "96,88",
   "Số hạt còn lại: 2⁻⁵ = 1/32 = 0,03125 = 3,125 %.\n"
   "Phần đã phân rã: 100 − 3,125 = 96,875 ≈ 96,88 %.",
   "Định luật phóng xạ", TB),
])


# =====================================================================  ĐỀ 7
DE7 = dict(
ma="12C4-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Số hạt phát ra, hỗn hợp đồng vị, năng lượng nhiệt hạch quy mô lớn",
P1=[
mc("Một mẫu chất phóng xạ ban đầu có N₀ hạt nhân, chu kì bán rã T. Số hạt α phát ra trong "
   "khoảng thời gian từ 0 đến 2T bằng",
   ["N₀/4.", "3N₀/4.", "N₀/2.", "N₀."],
   "B",
   "Mỗi phân rã α ứng với một hạt nhân mẹ bị rã, nên số hạt α phát ra bằng số hạt nhân đã phân rã.\n"
   "Sau 2T còn lại N₀/4 nên đã rã N₀ − N₀/4 = 3N₀/4.",
   "Số hạt phát ra", TB),

mc("Một mẫu chứa hai đồng vị phóng xạ X (chu kì bán rã 1,0 giờ) và Y (chu kì bán rã 2,0 giờ). "
   "Ban đầu độ phóng xạ của mỗi đồng vị đều bằng H₀. Sau 2,0 giờ, tổng độ phóng xạ của mẫu bằng",
   ["H₀/2.", "3H₀/4.", "H₀.", "H₀/4."],
   "B",
   "Sau 2,0 giờ: X trải qua 2 chu kì nên H(X) = H₀/4; Y trải qua 1 chu kì nên H(Y) = H₀/2.\n"
   "Tổng: H₀/4 + H₀/2 = 3H₀/4.",
   "Hỗn hợp hai đồng vị", K),

mc("Năng lượng toả ra khi tổng hợp được 1,0 gam heli từ phản ứng nhiệt hạch, biết mỗi hạt nhân "
   "heli tạo thành toả 17,6 MeV (Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J), xấp xỉ",
   ["4,24·10⁹ J.", "4,24·10¹¹ J.", "4,24·10¹³ J.", "4,24·10⁷ J."],
   "B",
   "Số hạt nhân heli trong 1,0 g: N = (1,0/4)·6,02·10²³ = 1,505·10²³ hạt.\n"
   "E = 1,505·10²³ · 17,6 · 1,6·10⁻¹³ ≈ 4,24·10¹¹ J.",
   "Năng lượng nhiệt hạch", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Độ phóng xạ của một mẫu chất đo được là 400 Bq lúc 8 giờ và 100 Bq lúc 12 giờ cùng ngày. "
   "Chu kì bán rã của chất đó bằng",
   ["1,0 giờ.", "2,0 giờ.", "3,0 giờ.", "4,0 giờ."],
   "B",
   "Độ phóng xạ giảm 4 lần = 2² trong 4 giờ, tức đã trôi qua 2 chu kì bán rã.\n"
   "T = 4,0/2 = 2,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB),

mc("Một phản ứng hạt nhân THU năng lượng 2,8 MeV. Để phản ứng xảy ra, tổng động năng của các hạt "
   "tới phải",
   ["bằng 0.", "không nhỏ hơn 2,8 MeV.",
    "bằng đúng 1,4 MeV.", "lớn hơn 931,5 MeV."],
   "B",
   "Phản ứng thu năng lượng chỉ xảy ra khi được cung cấp ít nhất lượng năng lượng đó từ động năng "
   "của các hạt tới. Trên thực tế còn cần thêm một phần để bảo toàn động lượng, nên ngưỡng "
   "thực sự còn cao hơn 2,8 MeV.",
   "Phản ứng thu năng lượng", K),

mc("Hai mẫu chất phóng xạ khác đồng vị có cùng độ phóng xạ ban đầu. Mẫu A có chu kì bán rã 2 giờ, "
   "mẫu B có chu kì bán rã 6 giờ. So sánh SỐ HẠT NHÂN ban đầu của hai mẫu:",
   ["bằng nhau.", "mẫu B nhiều gấp 3 lần mẫu A.",
    "mẫu A nhiều gấp 3 lần mẫu B.", "mẫu B nhiều gấp 9 lần mẫu A."],
   "B",
   "H = λ·N = (ln2/T)·N. Cùng H nên N tỉ lệ thuận với T.\n"
   "N(B)/N(A) = T(B)/T(A) = 6/2 = 3.",
   "Độ phóng xạ và số hạt nhân", K),

mc("Trong 1,0 giờ đầu tiên, một mẫu chất phóng xạ có chu kì bán rã 1,0 giờ phát ra 3,0·10¹⁸ hạt α. "
   "Số hạt nhân ban đầu của mẫu bằng",
   ["3,0·10¹⁸.", "6,0·10¹⁸.", "1,5·10¹⁸.", "1,2·10¹⁹."],
   "B",
   "Sau đúng một chu kì, một nửa số hạt nhân ban đầu đã rã, mỗi hạt rã phát ra một hạt α.\n"
   "N₀/2 = 3,0·10¹⁸ ⇒ N₀ = 6,0·10¹⁸ hạt.",
   "Số hạt phát ra", TB),

mc("Một mẫu chất phóng xạ nguyên chất sau thời gian t có tỉ số giữa số hạt nhân đã rã và số hạt "
   "nhân còn lại bằng 7. Sau thời gian 2t, tỉ số đó bằng",
   ["14.", "63.", "49.", "15."],
   "B",
   "Tỉ số 7 ứng với 2ⁿ − 1 = 7 ⇒ 2ⁿ = 8 ⇒ n = 3, tức t = 3T.\n"
   "Sau 2t = 6T: tỉ số = 2⁶ − 1 = 64 − 1 = 63.\n"
   "Nhân đôi thời gian KHÔNG làm tỉ số nhân đôi vì quy luật là hàm mũ.",
   "Tỉ số hạt nhân con và mẹ", K),

mc("Khối lượng của hạt nhân luôn nhỏ hơn tổng khối lượng các nuclêôn tạo thành nó. Điều này "
   "chứng tỏ",
   ["một số nuclêôn đã biến mất.",
    "một phần khối lượng đã chuyển thành năng lượng liên kết.",
    "phép cân khối lượng hạt nhân thiếu chính xác.",
    "các nuclêôn bị nén lại nên nhẹ hơn."],
   "B",
   "Khi các nuclêôn kết hợp lại, hệ toả ra năng lượng liên kết; theo hệ thức E = mc², "
   "năng lượng toả ra tương ứng với phần khối lượng bị hụt đi. Số nuclêôn luôn được bảo toàn.",
   "Ý nghĩa của độ hụt khối", TB, fig="h_sd_dohutkhoi", cap="Độ hụt khối"),

mc("Một nhà máy điện hạt nhân có công suất điện 600 MW, hiệu suất 30 %. Mỗi phân hạch toả 200 MeV. "
   "Khối lượng ²³⁵U tiêu thụ trong một ngày xấp xỉ",
   ["1,05 kg.", "2,11 kg.", "4,22 kg.", "0,63 kg."],
   "B",
   "Công suất nhiệt: P = 600/0,30 = 2000 MW = 2,0·10⁹ W.\n"
   "Số phân hạch mỗi giây: 2,0·10⁹/(200 · 1,6·10⁻¹³) = 2,0·10⁹/3,2·10⁻¹¹ = 6,25·10¹⁹.\n"
   "Trong một ngày: 6,25·10¹⁹ · 86 400 = 5,4·10²⁴ hạt.\n"
   "Khối lượng: (5,4·10²⁴/6,02·10²³) · 235 ≈ 8,97 · 235 ≈ 2108 g ≈ 2,11 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

mc("Sau khi phát ra một hạt α và hai hạt β⁻, hạt nhân ²³⁸₉₂U biến thành hạt nhân có",
   ["A = 234, Z = 92.", "A = 234, Z = 90.", "A = 234, Z = 88.", "A = 230, Z = 90."],
   "A",
   "A = 238 − 4 = 234 (chỉ phân rã α làm đổi số khối).\n"
   "Z = 92 − 2 + 2·1 = 92.\n"
   "Hạt nhân con vẫn là urani nhưng là đồng vị ²³⁴U.",
   "Chuỗi phân rã ngắn", K),

mc("Một chất phóng xạ có chu kì bán rã T. Gọi t₁ là thời gian để số hạt nhân giảm còn một nửa và "
   "t₂ là thời gian để số hạt nhân giảm còn một phần tư. Ta có",
   ["t₂ = 2·t₁.", "t₂ = 3·t₁.", "t₂ = 4·t₁.", "t₂ = t₁."],
   "A",
   "t₁ = T (còn một nửa);  t₂ = 2T (còn một phần tư).\n"
   "Vậy t₂ = 2·t₁. Lưu ý số hạt giảm 4 lần nhưng thời gian chỉ tăng gấp đôi — đặc trưng của "
   "quy luật hàm mũ.",
   "Bản chất hàm mũ của phân rã", TB),

mc("Trong phản ứng nhiệt hạch trên Mặt Trời, bốn hạt nhân hiđrô kết hợp tạo thành một hạt nhân "
   "heli và toả khoảng 26,7 MeV. Năng lượng toả ra tính trên mỗi nuclêôn xấp xỉ",
   ["26,7 MeV.", "6,7 MeV.", "13,4 MeV.", "3,3 MeV."],
   "B",
   "Có 4 nuclêôn tham gia nên năng lượng trên mỗi nuclêôn là 26,7/4 ≈ 6,7 MeV.\n"
   "So sánh: phân hạch ²³⁵U chỉ cho 200/235 ≈ 0,85 MeV mỗi nuclêôn.",
   "So sánh năng lượng trên nuclêôn", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Một người làm việc gần nguồn phóng xạ nhận liều 0,40 mSv mỗi giờ. Nếu giới hạn cho phép là "
   "20 mSv mỗi năm thì thời gian làm việc tối đa trong một năm là",
   ["25 giờ.", "50 giờ.", "80 giờ.", "100 giờ."],
   "B",
   "t = 20/0,40 = 50 giờ mỗi năm.\n"
   "Nếu muốn làm lâu hơn, phải tăng khoảng cách hoặc tăng che chắn để giảm suất liều.",
   "An toàn bức xạ", TB, fig="h_sd_an_toan", cap="Ba nguyên tắc an toàn bức xạ"),

mc("So với hạt nhân mẹ, hạt nhân con trong phóng xạ γ có",
   ["số khối giảm 4.", "cả A và Z đều không đổi.",
    "điện tích tăng 1.", "điện tích giảm 2."],
   "B",
   "Phóng xạ γ chỉ là sự chuyển từ trạng thái kích thích về trạng thái cơ bản, giải phóng phôtôn "
   "năng lượng cao. Thành phần hạt nhân hoàn toàn không thay đổi. Phóng xạ γ luôn đi kèm sau "
   "phóng xạ α hoặc β.",
   "Phóng xạ gamma", D),

mc("Hai hạt nhân ³₁H và ³₂He có cùng số khối. So sánh số nơtron của chúng:",
   ["bằng nhau.", "³₁H nhiều hơn 1 nơtron.",
    "³₂He nhiều hơn 1 nơtron.", "không so sánh được."],
   "B",
   "³₁H có N = 3 − 1 = 2 nơtron; ³₂He có N = 3 − 2 = 1 nơtron.\n"
   "Vậy triti nhiều hơn một nơtron. Đây là một cặp hạt nhân đồng khối.",
   "Đếm nuclêôn", TB),

mc("Trong một mẫu chất phóng xạ, số hạt nhân phân rã trong một đơn vị thời gian",
   ["không đổi theo thời gian.", "giảm dần theo thời gian.",
    "tăng dần theo thời gian.", "bằng số hạt nhân còn lại."],
   "B",
   "Số phân rã trong một giây chính là độ phóng xạ H = λN. Vì N giảm dần theo hàm mũ nên H cũng "
   "giảm theo đúng quy luật đó.",
   "Độ phóng xạ", TB),

mc("Khi tính năng lượng của phản ứng hạt nhân bằng công thức ΔE = (Δm sau − Δm trước)·c² "
   "với Δm là ĐỘ HỤT KHỐI, phản ứng toả năng lượng khi",
   ["tổng độ hụt khối sau nhỏ hơn trước.", "tổng độ hụt khối sau lớn hơn trước.",
    "hai tổng bằng nhau.", "độ hụt khối trước bằng 0."],
   "B",
   "Độ hụt khối lớn hơn nghĩa là năng lượng liên kết lớn hơn, tức các hạt nhân sau bền vững hơn. "
   "Khi đó phản ứng toả năng lượng. Chú ý phân biệt với cách tính theo KHỐI LƯỢNG NGHỈ, "
   "ở đó dấu ngược lại.",
   "Năng lượng phản ứng theo độ hụt khối", K),
],
P2=[
ds("Một mẫu chứa hai đồng vị phóng xạ độc lập X (chu kì bán rã 1,0 giờ) và Y (chu kì bán rã "
   "3,0 giờ). Ban đầu độ phóng xạ của mỗi đồng vị đều là 800 Bq.",
   [("Độ phóng xạ tổng của mẫu ban đầu là 1600 Bq.", True,
     "Đúng. Hai quá trình phân rã độc lập nên độ phóng xạ cộng lại: 800 + 800 = 1600 Bq."),
    ("Sau 3,0 giờ, độ phóng xạ của X còn 100 Bq.", True,
     "Đúng. X trải qua 3 chu kì: 800/2³ = 100 Bq."),
    ("Sau 3,0 giờ, độ phóng xạ của Y còn 400 Bq.", True,
     "Đúng. Y trải qua đúng 1 chu kì: 800/2 = 400 Bq."),
    ("Sau 3,0 giờ, độ phóng xạ tổng của mẫu bằng một nửa giá trị ban đầu.", False,
     "Sai. Tổng là 100 + 400 = 500 Bq, chỉ bằng 500/1600 = 31,25 % giá trị ban đầu chứ không "
     "phải 50 %.")],
   "Hỗn hợp hai đồng vị", K),

ds("Một nhà máy điện hạt nhân có công suất điện 600 MW, hiệu suất 30 %, dùng nhiên liệu ²³⁵U với "
   "mỗi phân hạch toả 200 MeV. Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   [("Công suất nhiệt của lò là 2000 MW.", True,
     "Đúng. P(nhiệt) = P(điện)/H = 600/0,30 = 2000 MW."),
    ("Số phân hạch xảy ra mỗi giây là 6,25·10¹⁹.", True,
     "Đúng. 2,0·10⁹/(200 · 1,6·10⁻¹³) = 2,0·10⁹/3,2·10⁻¹¹ = 6,25·10¹⁹."),
    ("Khối lượng ²³⁵U tiêu thụ trong một ngày xấp xỉ 2,11 kg.", True,
     "Đúng. Số hạt trong một ngày ≈ 5,4·10²⁴; khối lượng ≈ (5,4·10²⁴/6,02·10²³)·235 ≈ 2108 g."),
    ("Nếu nâng hiệu suất lên 60 % mà giữ nguyên công suất điện thì lượng nhiên liệu tiêu thụ "
     "cũng tăng gấp đôi.", False,
     "Sai. Hiệu suất cao hơn nghĩa là cần ít nhiệt hơn để tạo cùng công suất điện, "
     "nên lượng nhiên liệu tiêu thụ GIẢM một nửa chứ không tăng.")],
   "Nhiên liệu của nhà máy điện hạt nhân", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),

ds("Một mẫu chất phóng xạ nguyên chất có chu kì bán rã T, ban đầu có N₀ hạt nhân.",
   [("Số hạt nhân phân rã trong khoảng thời gian từ 0 đến T bằng N₀/2.", True,
     "Đúng. Sau một chu kì còn N₀/2 nên đã rã N₀/2."),
    ("Số hạt nhân phân rã trong khoảng thời gian từ T đến 2T bằng N₀/4.", True,
     "Đúng. Từ N₀/2 giảm còn N₀/4 nên đã rã thêm N₀/4."),
    ("Số hạt nhân phân rã trong khoảng từ T đến 2T bằng số hạt phân rã trong khoảng từ 0 đến T.", False,
     "Sai. N₀/4 chỉ bằng một nửa N₀/2. Trong các khoảng thời gian bằng nhau liên tiếp, "
     "số hạt phân rã giảm dần theo cấp số nhân."),
    ("Tổng số hạt α phát ra trong khoảng từ 0 đến 3T bằng 7N₀/8.", True,
     "Đúng. Sau 3T còn N₀/8 nên đã rã 7N₀/8, mỗi hạt rã phát ra một hạt α.")],
   "Số hạt phát ra theo từng khoảng", K),

ds("Xét việc so sánh các nguồn năng lượng.",
   [("Phản ứng phân hạch một hạt nhân ²³⁵U toả khoảng 200 MeV.", True,
     "Đúng. Đó là giá trị trung bình quen thuộc của phân hạch urani."),
    ("Phản ứng nhiệt hạch ²H + ³H toả khoảng 17,6 MeV mỗi phản ứng.", True,
     "Đúng. Đây là phản ứng nhiệt hạch được nghiên cứu nhiều nhất."),
    ("Vì 200 MeV lớn hơn 17,6 MeV nên phân hạch luôn là nguồn năng lượng hiệu quả hơn nhiệt hạch.", False,
     "Sai. Phải so sánh TRÊN MỘT NUCLÊÔN: phân hạch cho 200/235 ≈ 0,85 MeV còn nhiệt hạch cho "
     "17,6/5 ≈ 3,5 MeV. Nhiệt hạch hiệu quả hơn hẳn khi tính trên cùng khối lượng nhiên liệu."),
    ("Nhiên liệu cho nhiệt hạch có thể lấy từ nước biển nên gần như vô tận.", True,
     "Đúng. Đơteri chiếm khoảng một phần 6500 số nguyên tử hiđrô trong nước tự nhiên.")],
   "So sánh phân hạch và nhiệt hạch", K),
],
P3=[
sa("Một mẫu chất phóng xạ có chu kì bán rã 5,0 giờ, ban đầu có 8,0·10¹⁹ hạt nhân. "
   "Số hạt α phát ra trong 15 giờ đầu tiên bằng bao nhiêu (viết dưới dạng x·10¹⁹, "
   "chỉ ghi giá trị x)?",
   "7",
   "Số chu kì: n = 15/5,0 = 3.\n"
   "Số hạt còn lại: N = 8,0·10¹⁹/8 = 1,0·10¹⁹ hạt.\n"
   "Số hạt đã rã, cũng là số hạt α phát ra: 8,0·10¹⁹ − 1,0·10¹⁹ = 7,0·10¹⁹ hạt.",
   "Số hạt phát ra", TB),

sa("Một hạt nhân ²¹⁰₈₄Po đứng yên phóng xạ α, toả ra năng lượng 5,4 MeV. Bỏ qua bức xạ γ và coi "
   "khối lượng tỉ lệ với số khối. Động năng của hạt nhân con bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,10",
   "Bảo toàn động lượng cho hai hạt sinh ra: W tỉ lệ nghịch với khối lượng.\n"
   "W(con) = ΔE · m(α)/(m(α) + m(con)) = 5,4 · 4/(4 + 206) = 21,6/210 ≈ 0,10 MeV.\n"
   "Hạt nhân con nặng hơn nhiều nên chỉ mang một phần rất nhỏ năng lượng toả ra.",
   "Bảo toàn động lượng trong phân rã", K),

sa("Năng lượng toả ra khi tổng hợp được 2,0 gam heli từ phản ứng nhiệt hạch, biết mỗi hạt nhân "
   "heli tạo thành toả 17,6 MeV, bằng bao nhiêu jun (viết dưới dạng x·10¹¹, chỉ ghi giá trị x, "
   "làm tròn đến chữ số thập phân thứ hai)? Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   "8,48",
   "Số hạt nhân heli: N = (2,0/4) · 6,02·10²³ = 3,01·10²³ hạt.\n"
   "E = 3,01·10²³ · 17,6 · 1,6·10⁻¹³ = 3,01·10²³ · 2,816·10⁻¹² ≈ 8,476·10¹¹ ≈ 8,48·10¹¹ J.",
   "Năng lượng nhiệt hạch", K),

sa("Cho phản ứng ²₁H + ⁶₃Li → 2·⁴₂He. Biết m(²H) = 2,0136 u; m(⁶Li) = 6,0151 u; "
   "m(⁴He) = 4,0015 u; 1 u·c² = 931,5 MeV. Năng lượng toả ra của phản ứng bằng bao nhiêu MeV "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "23,9",
   "Tổng khối lượng trước: 2,0136 + 6,0151 = 8,0287 u.\n"
   "Tổng khối lượng sau: 2 · 4,0015 = 8,0030 u.\n"
   "Δm = 8,0287 − 8,0030 = 0,0257 u.\n"
   "ΔE = 0,0257 · 931,5 ≈ 23,9 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

sa("Hai mẫu chất phóng xạ thuộc hai đồng vị khác nhau có cùng độ phóng xạ ban đầu. "
   "Mẫu A có chu kì bán rã 4,0 giờ, mẫu B có chu kì bán rã 20 giờ. "
   "Số hạt nhân ban đầu của mẫu B gấp bao nhiêu lần mẫu A?",
   "5",
   "H = λ·N = (ln2/T)·N. Cùng độ phóng xạ nên N tỉ lệ thuận với T.\n"
   "N(B)/N(A) = T(B)/T(A) = 20/4,0 = 5.",
   "Độ phóng xạ và số hạt nhân", K),

sa("Một nhà máy điện hạt nhân có công suất điện 900 MW và hiệu suất 30 %. Mỗi phân hạch ²³⁵U toả "
   "200 MeV. Khối lượng ²³⁵U tiêu thụ trong một ngày bằng bao nhiêu kilôgam "
   "(làm tròn đến chữ số thập phân thứ hai)? Cho 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   "3,16",
   "Công suất nhiệt: 900/0,30 = 3000 MW = 3,0·10⁹ W.\n"
   "Số phân hạch mỗi giây: 3,0·10⁹/(3,2·10⁻¹¹) = 9,375·10¹⁹.\n"
   "Trong một ngày: 9,375·10¹⁹ · 86 400 = 8,10·10²⁴ hạt.\n"
   "Số mol: 8,10·10²⁴/6,02·10²³ ≈ 13,455 mol.\n"
   "Khối lượng: 13,455 · 235 ≈ 3162 g ≈ 3,16 kg.",
   "Nhiên liệu của nhà máy điện hạt nhân", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),
])


# =====================================================================  ĐỀ 8
DE8 = dict(
ma="12C4-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Công suất nguồn phóng xạ, phản ứng bắn phá, khối lượng hao hụt của Mặt Trời",
P1=[
mc("Một nguồn nhiệt dùng trong tàu vũ trụ chứa 1,0 gam ²¹⁰Po (chu kì bán rã 138 ngày). "
   "Mỗi phân rã toả 5,4 MeV. Công suất ban đầu của nguồn xấp xỉ "
   "(Nₐ = 6,02·10²³; 1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693)",
   ["14,4 W.", "144 W.", "1440 W.", "1,44 W."],
   "B",
   "Số hạt nhân: N₀ = (1,0/210)·6,02·10²³ ≈ 2,867·10²¹ hạt.\n"
   "Chu kì bán rã: T = 138 · 86 400 ≈ 1,192·10⁷ s ⇒ λ = 0,693/1,192·10⁷ ≈ 5,81·10⁻⁸ s⁻¹.\n"
   "Độ phóng xạ: H₀ = λ·N₀ ≈ 5,81·10⁻⁸ · 2,867·10²¹ ≈ 1,666·10¹⁴ Bq.\n"
   "Công suất: P = H₀ · 5,4 · 1,6·10⁻¹³ ≈ 1,666·10¹⁴ · 8,64·10⁻¹³ ≈ 144 W.",
   "Công suất của nguồn phóng xạ", RK),

mc("Mặt Trời bức xạ với công suất 3,8·10²⁶ W. Khối lượng mà Mặt Trời mất đi trong mỗi giây do "
   "chuyển thành năng lượng xấp xỉ (c = 3,0·10⁸ m/s)",
   ["4,2·10⁷ kg.", "4,2·10⁹ kg.", "4,2·10¹¹ kg.", "1,3·10¹⁸ kg."],
   "B",
   "Từ E = m·c² suy ra m = E/c² = 3,8·10²⁶/(9,0·10¹⁶) ≈ 4,2·10⁹ kg mỗi giây.\n"
   "Con số khổng lồ này vẫn rất nhỏ so với khối lượng Mặt Trời (2·10³⁰ kg).",
   "Hệ thức khối lượng – năng lượng", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),

mc("Cho phản ứng ⁴₂He + ¹⁴₇N → ¹⁷₈O + ¹₁H với m(He) = 4,0015 u; m(N) = 14,0031 u; "
   "m(O) = 16,9991 u; m(H) = 1,0073 u; 1 u·c² = 931,5 MeV. Phản ứng này",
   ["toả 1,68 MeV.", "thu 1,68 MeV.", "toả 16,8 MeV.", "thu 16,8 MeV."],
   "B",
   "Tổng khối lượng trước: 4,0015 + 14,0031 = 18,0046 u.\n"
   "Tổng khối lượng sau: 16,9991 + 1,0073 = 18,0064 u.\n"
   "Δm = 18,0046 − 18,0064 = −0,0018 u < 0 nên phản ứng THU năng lượng.\n"
   "|ΔE| = 0,0018 · 931,5 ≈ 1,68 MeV.",
   "Phản ứng thu năng lượng", K),

mc("Một mẫu gỗ cổ có tỉ lệ ¹⁴C bằng 40 % mẫu gỗ tươi. Tuổi của mẫu gỗ xấp xỉ "
   "(chu kì bán rã của ¹⁴C là 5730 năm; ln2 ≈ 0,693)",
   ["4580 năm.", "7576 năm.", "11 460 năm.", "2292 năm."],
   "B",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,40 ⇒ n = ln(1/0,40)/ln2 = 0,9163/0,693 ≈ 1,322.\n"
   "t = 1,322 · 5730 ≈ 7576 năm.\n"
   "Kiểm tra hợp lí: 40 % nằm giữa 50 % (1T) và 25 % (2T) nên t nằm giữa 5730 và 11 460 năm.",
   "Xác định tuổi bằng cacbon-14", K, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu H₀. Sau thời gian t, độ phóng xạ là H. "
   "Chu kì bán rã được tính bằng",
   ["T = t·ln(H₀/H)/ln2.", "T = t·ln2/ln(H₀/H).",
    "T = t·ln2·ln(H₀/H).", "T = ln2/(t·ln(H₀/H))."],
   "B",
   "Từ H = H₀·e^(−λt) ⇒ λ·t = ln(H₀/H) ⇒ λ = ln(H₀/H)/t.\n"
   "T = ln2/λ = t·ln2/ln(H₀/H).",
   "Định luật phóng xạ – công thức tổng quát", K),

mc("Một lượng ²³⁵U toả ra tổng cộng 8,2·10¹³ J khi phân hạch hoàn toàn. Khối lượng ²³⁵U đã dùng "
   "xấp xỉ (mỗi phân hạch toả 200 MeV; 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹)",
   ["100 g.", "1,0 kg.", "10 kg.", "100 kg."],
   "B",
   "Số phân hạch: 8,2·10¹³/(3,2·10⁻¹¹) ≈ 2,56·10²⁴.\n"
   "Số mol: 2,56·10²⁴/6,02·10²³ ≈ 4,25 mol.\n"
   "Khối lượng: 4,25 · 235 ≈ 999 g ≈ 1,0 kg.",
   "Năng lượng của nhiên liệu hạt nhân", K),

mc("Trong phản ứng hạt nhân, nếu hạt nhân bia đứng yên và hạt tới có động năng W, thì tổng động "
   "năng của các hạt sau phản ứng bằng",
   ["W.", "W + ΔE với ΔE là năng lượng toả ra.",
    "W − ΔE.", "ΔE."],
   "B",
   "Bảo toàn năng lượng toàn phần: tổng động năng sau = tổng động năng trước + năng lượng toả ra.\n"
   "Với phản ứng thu năng lượng, ΔE < 0 nên tổng động năng sau nhỏ hơn W.",
   "Bảo toàn năng lượng trong phản ứng hạt nhân", K),

mc("Hai mẫu của hai đồng vị phóng xạ khác nhau có cùng số hạt nhân ban đầu. Sau cùng một khoảng "
   "thời gian, mẫu có chu kì bán rã ngắn hơn sẽ",
   ["còn lại nhiều hạt nhân hơn.", "còn lại ít hạt nhân hơn.",
    "còn lại số hạt nhân bằng nhau.", "không thay đổi số hạt nhân."],
   "B",
   "Chu kì bán rã ngắn nghĩa là phân rã nhanh. Sau cùng một khoảng thời gian, mẫu đó đã trải qua "
   "nhiều chu kì hơn nên còn lại ít hạt nhân hơn.",
   "So sánh hai chất phóng xạ", TB),

mc("Trong một phản ứng hạt nhân toả năng lượng, nếu tổng động năng của các hạt trước bằng 0 thì",
   ["phản ứng không xảy ra.", "toàn bộ năng lượng toả ra biến thành động năng của các hạt sau.",
    "các hạt sau cũng đứng yên.", "năng lượng toả ra bằng 0."],
   "B",
   "Với phản ứng toả năng lượng, không cần cung cấp động năng ban đầu. Năng lượng lấy từ phần "
   "khối lượng nghỉ bị hụt đi chuyển hết thành động năng của các hạt sản phẩm (và bức xạ γ).",
   "Bảo toàn năng lượng", K),

mc("Hạt nhân ⁶⁰₂₇Co phóng xạ β⁻ rồi phát tiếp tia γ. Hạt nhân bền cuối cùng là",
   ["⁶⁰₂₆Fe.", "⁶⁰₂₈Ni.", "⁵⁶₂₆Fe.", "⁶⁰₂₇Co."],
   "B",
   "Phân rã β⁻ làm Z tăng 1, A không đổi: Z = 27 + 1 = 28, A = 60 ⇒ ⁶⁰₂₈Ni.\n"
   "Bức xạ γ sau đó không làm thay đổi Z và A, chỉ giải phóng năng lượng dư.",
   "Chuỗi phân rã", TB, fig="h_sd_dich_chuyen", cap="Quy tắc dịch chuyển"),

mc("Một nguồn phóng xạ có độ phóng xạ 5,0·10¹² Bq, mỗi phân rã toả 2,0 MeV. "
   "Công suất của nguồn xấp xỉ (1 MeV = 1,6·10⁻¹³ J)",
   ["0,80 W.", "1,60 W.", "3,20 W.", "0,40 W."],
   "B",
   "P = H · E(mỗi phân rã) = 5,0·10¹² · 2,0 · 1,6·10⁻¹³ = 5,0·10¹² · 3,2·10⁻¹³ = 1,6 W.",
   "Công suất của nguồn phóng xạ", K),

mc("Trong phản ứng phân hạch, tổng khối lượng nghỉ của các mảnh vỡ và nơtron so với khối lượng "
   "của hạt nhân mẹ cộng nơtron tới thì",
   ["lớn hơn.", "nhỏ hơn.", "bằng nhau.", "tuỳ từng phản ứng."],
   "B",
   "Phân hạch là phản ứng toả năng lượng nên khối lượng nghỉ sau phải nhỏ hơn trước; "
   "phần chênh lệch chuyển thành động năng của các mảnh vỡ và bức xạ.",
   "Năng lượng phân hạch", TB, fig="h_sd_phan_hach", cap="Phản ứng phân hạch"),

mc("Một chất phóng xạ có chu kì bán rã T. Ban đầu có N₀ hạt nhân. Số hạt nhân phân rã trong khoảng "
   "thời gian rất ngắn Δt ở thời điểm t xấp xỉ",
   ["λ·N₀·Δt.", "λ·N₀·2^(−t/T)·Δt.", "N₀·Δt/T.", "λ·Δt."],
   "B",
   "Số phân rã trong Δt bằng độ phóng xạ nhân thời gian: ΔN = H·Δt = λ·N(t)·Δt, "
   "trong đó N(t) = N₀·2^(−t/T).",
   "Độ phóng xạ", K),

mc("Hai đồng vị của cùng một nguyên tố có tính chất HOÁ HỌC giống nhau vì",
   ["chúng có cùng số nơtron.", "chúng có cùng số prôtôn nên cùng số electron.",
    "chúng có cùng khối lượng.", "chúng có cùng chu kì bán rã."],
   "B",
   "Tính chất hoá học được quyết định bởi lớp vỏ electron, mà số electron bằng số prôtôn. "
   "Các đồng vị có cùng Z nên cùng tính chất hoá học, nhưng tính chất HẠT NHÂN thì rất khác nhau.",
   "Đồng vị", TB),

mc("Một mẫu chất phóng xạ nguyên chất có khối lượng 10 gam, chu kì bán rã 6 giờ. Khối lượng chất "
   "phóng xạ đã bị phân rã sau 18 giờ bằng",
   ["1,25 gam.", "8,75 gam.", "2,50 gam.", "5,00 gam."],
   "B",
   "Số chu kì: n = 18/6 = 3 ⇒ còn lại 10/8 = 1,25 g.\n"
   "Khối lượng đã rã: 10 − 1,25 = 8,75 g.",
   "Định luật phóng xạ", TB),

mc("Trong máy gia tốc, người ta bắn hạt tới vào hạt nhân bia đứng yên. Việc cung cấp động năng "
   "cho hạt tới là cần thiết nhằm",
   ["làm tăng khối lượng nghỉ của hạt tới.",
    "thắng lực đẩy Cu-lông để hai hạt nhân lại gần nhau đủ mức.",
    "làm giảm chu kì bán rã của bia.",
    "tạo ra từ trường trong bia."],
   "B",
   "Hai hạt nhân đều mang điện dương nên đẩy nhau rất mạnh khi lại gần. Chỉ khi hạt tới có đủ "
   "động năng, nó mới vượt qua được hàng rào Cu-lông để lực hạt nhân phát huy tác dụng.",
   "Điều kiện xảy ra phản ứng hạt nhân", TB),

mc("Nếu một mẫu chất phóng xạ có độ phóng xạ giảm đi 1000 lần thì số chu kì bán rã đã trôi qua "
   "xấp xỉ (ln2 ≈ 0,693)",
   ["6,6 chu kì.", "10,0 chu kì.", "3,3 chu kì.", "13,3 chu kì."],
   "B",
   "2ⁿ = 1000 ⇒ n = ln1000/ln2 = 6,908/0,693 ≈ 9,97 ≈ 10,0 chu kì.\n"
   "Ghi nhớ hữu ích: cứ 10 chu kì bán rã thì độ phóng xạ giảm khoảng 1000 lần.",
   "Định luật phóng xạ – dùng logarit", K),

mc("Trong lò phản ứng hạt nhân, nếu không có chất làm chậm thì",
   ["phản ứng xảy ra nhanh hơn.", "xác suất gây phân hạch của nơtron giảm mạnh.",
    "nơtron bị hấp thụ hết.", "nhiệt độ lò giảm xuống 0."],
   "B",
   "Nơtron sinh ra từ phân hạch có động năng rất lớn (nơtron nhanh), khả năng gây phân hạch tiếp "
   "cho ²³⁵U lại rất thấp. Chất làm chậm hạ tốc độ chúng xuống mức nơtron nhiệt, "
   "làm xác suất phân hạch tăng lên hàng trăm lần.",
   "Lò phản ứng hạt nhân", K, fig="h_sd_lo_phan_ung", cap="Sơ đồ lò phản ứng"),
],
P2=[
ds("Một nguồn nhiệt đồng vị chứa 2,0 gam ²¹⁰Po (chu kì bán rã 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693.",
   [("Số hạt nhân pôlôni ban đầu xấp xỉ 5,73·10²¹ hạt.", True,
     "Đúng. N₀ = (2,0/210) · 6,02·10²³ ≈ 5,733·10²¹ hạt."),
    ("Hằng số phóng xạ của pôlôni xấp xỉ 5,81·10⁻⁸ s⁻¹.", True,
     "Đúng. T = 138 · 86 400 ≈ 1,192·10⁷ s ⇒ λ = 0,693/1,192·10⁷ ≈ 5,81·10⁻⁸ s⁻¹."),
    ("Công suất ban đầu của nguồn xấp xỉ 288 W.", True,
     "Đúng. H₀ = λN₀ ≈ 3,33·10¹⁴ Bq ⇒ P = 3,33·10¹⁴ · 8,64·10⁻¹³ ≈ 288 W."),
    ("Sau 138 ngày, công suất của nguồn vẫn giữ nguyên 288 W.", False,
     "Sai. Công suất tỉ lệ với độ phóng xạ nên sau một chu kì bán rã, công suất giảm còn một nửa, "
     "tức khoảng 144 W.")],
   "Công suất của nguồn phóng xạ", RK),

ds("Trong khí quyển, ¹⁴C được tạo ra liên tục nhờ phản ứng ¹⁴₇N + ¹₀n → ¹⁴₆C + ¹₁H. "
   "Cho m(¹⁴N) = 14,0031 u; m(n) = 1,0087 u; m(¹⁴C) = 14,0032 u; m(¹H) = 1,0073 u; "
   "1 u·c² = 931,5 MeV.",
   [("Phản ứng bảo toàn cả số khối lẫn điện tích.", True,
     "Đúng. Số khối: 14 + 1 = 14 + 1;  điện tích: 7 + 0 = 6 + 1."),
    ("Tổng khối lượng nghỉ giảm 0,0013 u sau phản ứng.", True,
     "Đúng. Trước: 14,0031 + 1,0087 = 15,0118 u;  sau: 14,0032 + 1,0073 = 15,0105 u; "
     "hiệu bằng 0,0013 u."),
    ("Phản ứng toả năng lượng khoảng 1,21 MeV.", True,
     "Đúng. ΔE = 0,0013 · 931,5 ≈ 1,21 MeV, và vì khối lượng nghỉ giảm nên phản ứng toả năng lượng."),
    ("Nhờ phản ứng này mà tỉ lệ ¹⁴C trong khí quyển giảm dần theo thời gian.", False,
     "Sai. Ngược lại, phản ứng này liên tục BỔ SUNG ¹⁴C, cân bằng với lượng ¹⁴C bị phân rã, "
     "nhờ đó tỉ lệ ¹⁴C trong khí quyển giữ gần như không đổi — đây chính là giả thiết nền tảng "
     "của phương pháp xác định tuổi bằng cacbon.")],
   "Nguồn gốc của ¹⁴C trong khí quyển", K),

ds("Một mẫu gỗ khảo cổ được xác định tuổi bằng ¹⁴C (chu kì bán rã 5730 năm).",
   [("Khi cây còn sống, tỉ lệ ¹⁴C trong cơ thể được duy trì gần như không đổi.", True,
     "Đúng. Cây liên tục trao đổi cacbon với khí quyển nên tỉ lệ ¹⁴C cân bằng với khí quyển."),
    ("Sau khi cây chết, ¹⁴C không được bổ sung nữa nên chỉ giảm dần theo quy luật phóng xạ.", True,
     "Đúng. Đó chính là cơ sở của phương pháp xác định tuổi."),
    ("Nếu mẫu gỗ còn 40 % lượng ¹⁴C thì tuổi của nó vào khoảng 7576 năm.", True,
     "Đúng. n = ln(1/0,40)/ln2 ≈ 1,322 ⇒ t ≈ 1,322 · 5730 ≈ 7576 năm."),
    ("Phương pháp này áp dụng tốt cho mẫu vật có tuổi hàng triệu năm.", False,
     "Sai. Sau khoảng 50 000 năm, lượng ¹⁴C còn lại quá nhỏ để đo chính xác. "
     "Với mẫu hàng triệu năm phải dùng các cặp đồng vị có chu kì bán rã dài hơn nhiều như U–Pb.")],
   "Xác định tuổi bằng cacbon-14", K, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

ds("Mặt Trời bức xạ với công suất 3,8·10²⁶ W nhờ phản ứng nhiệt hạch trong lõi. "
   "Cho c = 3,0·10⁸ m/s.",
   [("Mỗi giây Mặt Trời mất khoảng 4,2·10⁹ kg khối lượng.", True,
     "Đúng. m = E/c² = 3,8·10²⁶/9,0·10¹⁶ ≈ 4,2·10⁹ kg."),
    ("Khối lượng mất đi đó đã chuyển hoàn toàn thành năng lượng bức xạ.", True,
     "Đúng. Đây là biểu hiện trực tiếp của hệ thức E = mc²."),
    ("Trong một năm, Mặt Trời mất khoảng 1,3·10¹⁷ kg.", True,
     "Đúng. 4,2·10⁹ · 3,15·10⁷ ≈ 1,3·10¹⁷ kg mỗi năm."),
    ("Với tốc độ mất khối lượng đó, Mặt Trời sẽ cạn kiệt sau vài nghìn năm nữa.", False,
     "Sai. Khối lượng Mặt Trời khoảng 2·10³⁰ kg; mỗi năm chỉ mất 1,3·10¹⁷ kg, tức phần mất đi "
     "là vô cùng nhỏ. Mặt Trời còn hoạt động khoảng năm tỉ năm nữa.")],
   "Hệ thức khối lượng – năng lượng", K, fig="h_sd_nhiet_hach", cap="Phản ứng nhiệt hạch"),
],
P3=[
sa("Một nguồn phóng xạ có độ phóng xạ 2,5·10¹² Bq, mỗi phân rã toả 4,0 MeV. "
   "Công suất của nguồn bằng bao nhiêu oát (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho 1 MeV = 1,6·10⁻¹³ J.",
   "1,6",
   "Năng lượng mỗi phân rã: 4,0 · 1,6·10⁻¹³ = 6,4·10⁻¹³ J.\n"
   "P = H · E = 2,5·10¹² · 6,4·10⁻¹³ = 1,6 W.",
   "Công suất của nguồn phóng xạ", K),

sa("Một ngôi sao bức xạ với công suất 1,8·10²⁷ W. Khối lượng mà ngôi sao mất đi trong mỗi giây "
   "bằng bao nhiêu kilôgam (viết dưới dạng x·10¹⁰, chỉ ghi giá trị x)? Cho c = 3,0·10⁸ m/s.",
   "2",
   "m = E/c² = 1,8·10²⁷/(9,0·10¹⁶) = 2,0·10¹⁰ kg mỗi giây.",
   "Hệ thức khối lượng – năng lượng", K),

sa("Một mẫu chất phóng xạ có độ phóng xạ giảm 512 lần sau 36 giờ. Chu kì bán rã của chất đó "
   "bằng bao nhiêu giờ?",
   "4",
   "512 = 2⁹ nên n = 9 chu kì bán rã.\n"
   "T = 36/9 = 4,0 giờ.",
   "Định luật phóng xạ – bài toán ngược", TB),

sa("Cho phản ứng ⁹₄Be + ⁴₂He → ¹²₆C + ¹₀n với m(Be) = 9,0122 u; m(He) = 4,0015 u; "
   "m(C) = 12,0000 u; m(n) = 1,0087 u; 1 u·c² = 931,5 MeV. Năng lượng toả ra của phản ứng bằng "
   "bao nhiêu MeV (làm tròn đến chữ số thập phân thứ nhất)?",
   "4,7",
   "Tổng khối lượng trước: 9,0122 + 4,0015 = 13,0137 u.\n"
   "Tổng khối lượng sau: 12,0000 + 1,0087 = 13,0087 u.\n"
   "Δm = 13,0137 − 13,0087 = 0,0050 u.\n"
   "ΔE = 0,0050 · 931,5 ≈ 4,7 MeV.",
   "Năng lượng phản ứng hạt nhân", K),

sa("Một mẫu gỗ cổ còn lại 60 % lượng ¹⁴C so với mẫu gỗ tươi. Tuổi của mẫu gỗ bằng bao nhiêu năm "
   "(làm tròn đến hàng đơn vị)? Cho chu kì bán rã của ¹⁴C là 5730 năm; ln2 ≈ 0,693.",
   "4223",
   "Đặt n = t/T. Từ 2⁻ⁿ = 0,60 ⇒ n = ln(1/0,60)/ln2 = 0,5108/0,693 ≈ 0,7371.\n"
   "t = 0,7371 · 5730 ≈ 4223 năm.",
   "Xác định tuổi bằng cacbon-14", K, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

sa("Một khối lượng ²³⁵U phân hạch hoàn toàn toả ra 1,64·10¹⁴ J. Khối lượng ²³⁵U đã dùng bằng "
   "bao nhiêu kilôgam? Mỗi phân hạch toả 200 MeV; 1 MeV = 1,6·10⁻¹³ J; Nₐ = 6,02·10²³ mol⁻¹.",
   "2",
   "Số phân hạch: 1,64·10¹⁴/(200 · 1,6·10⁻¹³) = 1,64·10¹⁴/3,2·10⁻¹¹ = 5,125·10²⁴.\n"
   "Số mol: 5,125·10²⁴/6,02·10²³ ≈ 8,51 mol.\n"
   "Khối lượng: 8,51 · 235 ≈ 2000 g = 2,0 kg.",
   "Năng lượng của nhiên liệu hạt nhân", K),
])


# =====================================================================  ĐỀ 9
DE9 = dict(
ma="12C4-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Bảo toàn động lượng hai chiều, hỗn hợp đồng vị, năng lượng tích luỹ của nguồn",
P1=[
mc("Dùng prôtôn có động năng 5,45 MeV bắn vào hạt nhân ⁹₄Be đứng yên, sinh ra hạt α và hạt nhân "
   "⁶₃Li. Hạt α bay ra theo phương VUÔNG GÓC với phương của prôtôn và có động năng 4,00 MeV. "
   "Coi khối lượng tỉ lệ với số khối, động năng của hạt nhân liti xấp xỉ",
   ["2,13 MeV.", "3,58 MeV.", "5,45 MeV.", "1,45 MeV."],
   "B",
   "Vì hạt α vuông góc với prôtôn nên theo định lí Pi-ta-go: p(Li)² = p(p)² + p(α)².\n"
   "Với p² = 2mW và m tỉ lệ A, ta có A(Li)·W(Li) = A(p)·W(p) + A(α)·W(α).\n"
   "6·W(Li) = 1 · 5,45 + 4 · 4,00 = 5,45 + 16,00 = 21,45.\n"
   "W(Li) = 21,45/6 ≈ 3,58 MeV.",
   "Bảo toàn động lượng hai chiều", RK),

mc("Với bài toán ở câu trên, năng lượng mà phản ứng toả ra xấp xỉ",
   ["1,13 MeV.", "2,13 MeV.", "3,58 MeV.", "9,45 MeV."],
   "B",
   "Năng lượng toả ra bằng độ tăng tổng động năng:\n"
   "ΔE = (W(α) + W(Li)) − W(p) = (4,00 + 3,58) − 5,45 = 7,58 − 5,45 ≈ 2,13 MeV.",
   "Bảo toàn năng lượng trong phản ứng", RK),

mc("Một mẫu chứa hai đồng vị phóng xạ X (chu kì bán rã 1,0 giờ) và Y (chu kì bán rã 2,0 giờ). "
   "Sau 2,0 giờ, tổng số hạt nhân còn lại bằng 1/3 tổng số hạt nhân ban đầu. "
   "Tỉ số số hạt nhân X và Y lúc ban đầu là",
   ["1 : 2.", "2 : 1.", "1 : 1.", "3 : 1."],
   "B",
   "Sau 2,0 giờ: X còn N₁/4, Y còn N₂/2.\n"
   "(N₁/4 + N₂/2)/(N₁ + N₂) = 1/3 ⇒ 3(N₁/4 + N₂/2) = N₁ + N₂.\n"
   "0,75N₁ + 1,5N₂ = N₁ + N₂ ⇒ 0,5N₂ = 0,25N₁ ⇒ N₁ = 2N₂.\n"
   "Vậy tỉ số N₁ : N₂ = 2 : 1.",
   "Hỗn hợp hai đồng vị", RK),

mc("Một mẫu chất phóng xạ nguyên chất có N₀ hạt nhân, chu kì bán rã T. Số hạt α phát ra trong "
   "khoảng thời gian từ t₁ = T đến t₂ = 3T bằng",
   ["N₀/4.", "3N₀/8.", "N₀/2.", "7N₀/8."],
   "B",
   "Số hạt còn lại tại t₁ = T là N₀/2; tại t₂ = 3T là N₀/8.\n"
   "Số hạt đã rã trong khoảng đó: N₀/2 − N₀/8 = 4N₀/8 − N₀/8 = 3N₀/8.",
   "Số hạt phát ra trong một khoảng", K),

mc("Tổng năng lượng mà 1,0 gam ²¹⁰Po toả ra cho tới khi phân rã hết hoàn toàn xấp xỉ "
   "(mỗi phân rã toả 5,4 MeV; Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J)",
   ["2,48·10⁷ J.", "2,48·10⁹ J.", "2,48·10¹¹ J.", "2,48·10⁵ J."],
   "B",
   "Tổng số phân rã cho tới khi hết chính bằng số hạt nhân ban đầu:\n"
   "N₀ = (1,0/210)·6,02·10²³ ≈ 2,867·10²¹ hạt.\n"
   "E = 2,867·10²¹ · 5,4 · 1,6·10⁻¹³ = 2,867·10²¹ · 8,64·10⁻¹³ ≈ 2,48·10⁹ J.",
   "Năng lượng tích luỹ của nguồn", RK),

mc("Hạt nhân ²¹⁰₈₄Po phóng xạ α thành ²⁰⁶₈₂Pb, chu kì bán rã 138 ngày. Sau bao lâu thì tỉ số giữa "
   "KHỐI LƯỢNG chì và khối lượng pôlôni còn lại bằng 0,70 (ln2 ≈ 0,693)?",
   ["69 ngày.", "107 ngày.", "138 ngày.", "207 ngày."],
   "B",
   "Tỉ số khối lượng: (206/210)·(2ⁿ − 1) = 0,70 ⇒ 2ⁿ − 1 = 0,70 · 210/206 ≈ 0,7136.\n"
   "2ⁿ = 1,7136 ⇒ n = ln1,7136/ln2 = 0,5387/0,693 ≈ 0,777.\n"
   "t = 0,777 · 138 ≈ 107 ngày.",
   "Tỉ số khối lượng con và mẹ", RK, fig="h_sd_phan_ra_po", cap="Sơ đồ phân rã pôlôni"),

mc("Một nguồn phóng xạ có công suất ban đầu 120 W và chu kì bán rã 30 năm. Sau 90 năm, "
   "công suất của nguồn còn",
   ["30 W.", "15 W.", "40 W.", "60 W."],
   "B",
   "Công suất tỉ lệ thuận với độ phóng xạ nên cũng giảm theo cùng quy luật:\n"
   "n = 90/30 = 3 ⇒ P = 120/2³ = 15 W.",
   "Công suất nguồn phóng xạ theo thời gian", K),

mc("Dùng hạt α có động năng 7,7 MeV bắn vào hạt nhân ¹⁴₇N đứng yên, thu được hạt prôtôn và hạt "
   "nhân ¹⁷₈O. Phản ứng thu 1,2 MeV. Tổng động năng của hai hạt sau phản ứng bằng",
   ["8,9 MeV.", "6,5 MeV.", "7,7 MeV.", "1,2 MeV."],
   "B",
   "Bảo toàn năng lượng: tổng động năng sau = tổng động năng trước + ΔE.\n"
   "Với phản ứng THU năng lượng thì ΔE mang dấu âm:\n"
   "W(sau) = 7,7 − 1,2 = 6,5 MeV.",
   "Bảo toàn năng lượng trong phản ứng", K),

mc("Một chất phóng xạ có chu kì bán rã T. Tại thời điểm t, độ phóng xạ là H; tại thời điểm "
   "t + 3T, độ phóng xạ là",
   ["H/3.", "H/8.", "H/6.", "3H."],
   "B",
   "Sau mỗi khoảng 3T, độ phóng xạ giảm 2³ = 8 lần, bất kể mốc thời gian t là bao nhiêu. "
   "Đây là đặc trưng của quy luật hàm mũ.",
   "Bản chất hàm mũ của phân rã", TB),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu H₀. Sau thời gian t, độ phóng xạ còn H₀/5. "
   "Sau thời gian 2t (tính từ lúc đầu), độ phóng xạ của mẫu bằng",
   ["H₀/10.", "H₀/25.", "H₀/15.", "H₀/7."],
   "B",
   "Trong những khoảng thời gian bằng nhau, độ phóng xạ giảm theo cùng một TỈ LỆ.\n"
   "Sau t giảm 5 lần, nên sau 2t giảm 5 · 5 = 25 lần: H = H₀/25.\n"
   "Sai lầm thường gặp là nhân đôi mẫu số thành H₀/10 — đó là suy nghĩ tuyến tính, "
   "không đúng với quy luật hàm mũ.",
   "Bản chất hàm mũ của phân rã", K),

mc("Trong một chuỗi phân rã, hạt nhân ²³⁵₉₂U biến thành ²⁰⁷₈₂Pb. Số lần phân rã α và β⁻ lần lượt là",
   ["7 và 4.", "7 và 6.", "8 và 6.", "6 và 4."],
   "A",
   "Số lần α: (235 − 207)/4 = 28/4 = 7 lần.\n"
   "Sau 7 lần α, Z còn 92 − 14 = 78; cần tới Z = 82 nên phải có 82 − 78 = 4 lần β⁻.",
   "Chuỗi phân rã", K),

mc("Một mẫu chất phóng xạ nguyên chất, sau thời gian t₁ thì 20 % số hạt nhân đã rã. "
   "Sau thời gian t₂ = 2·t₁ thì phần trăm số hạt nhân đã rã bằng",
   ["40 %.", "36 %.", "44 %.", "20 %."],
   "B",
   "Còn lại sau t₁: 80 % = 0,80.\n"
   "Sau 2t₁, phần còn lại là (0,80)² = 0,64 = 64 %.\n"
   "Vậy đã rã 100 − 64 = 36 %. Nhân đôi thời gian KHÔNG làm nhân đôi phần đã rã.",
   "Bản chất hàm mũ của phân rã", K),

mc("Một hạt nhân đứng yên phân rã thành hai hạt có số khối A₁ và A₂, toả ra năng lượng ΔE. "
   "Động năng của hạt thứ nhất bằng",
   ["ΔE·A₁/(A₁ + A₂).", "ΔE·A₂/(A₁ + A₂).",
    "ΔE/2.", "ΔE·A₁/A₂."],
   "B",
   "Bảo toàn động lượng cho hai hạt có cùng độ lớn động lượng p.\n"
   "W = p²/(2m) nên W₁/W₂ = m₂/m₁ = A₂/A₁.\n"
   "Kết hợp W₁ + W₂ = ΔE được W₁ = ΔE·A₂/(A₁ + A₂): hạt NHẸ mang nhiều động năng hơn.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Một mẫu chất phóng xạ có độ phóng xạ ban đầu H₀. Tổng số phân rã xảy ra trong toàn bộ thời "
   "gian cho tới khi mẫu phân rã hết bằng",
   ["H₀·T.", "H₀/λ.", "H₀·λ.", "H₀·ln2."],
   "B",
   "Tổng số phân rã bằng đúng số hạt nhân ban đầu N₀.\n"
   "Từ H₀ = λ·N₀ ⇒ N₀ = H₀/λ. Có thể viết dưới dạng N₀ = H₀·T/ln2.",
   "Độ phóng xạ và tổng số phân rã", RK),

mc("Trong lò phản ứng, sản phẩm phân hạch thường có tỉ lệ nơtron trên prôtôn cao hơn mức bền vững, "
   "nên các mảnh vỡ thường tiếp tục phóng xạ",
   ["α.", "β⁻.", "β⁺.", "không phóng xạ nữa."],
   "B",
   "Thừa nơtron nên hạt nhân điều chỉnh bằng cách biến nơtron thành prôtôn, tức phóng xạ β⁻, "
   "để tỉ lệ nơtron/prôtôn trở về vùng bền vững. Đó là lí do chất thải hạt nhân phát tia β và γ "
   "trong thời gian dài.",
   "Chất thải phóng xạ", K),

mc("Một chất phóng xạ có chu kì bán rã 8,0 ngày. Khối lượng ban đầu 200 gam. Khối lượng phân rã "
   "trong ngày thứ 9 (tính từ đầu ngày thứ 9 đến cuối ngày thứ 9) xấp xỉ",
   ["12,3 gam.", "8,5 gam.", "25,0 gam.", "100 gam."],
   "B",
   "Khối lượng còn lại sau 8 ngày: 200/2 = 100 g.\n"
   "Sau 9 ngày: 200 · 2^(−9/8) = 200 · 2^(−1,125) ≈ 200 · 0,4576 ≈ 91,5 g.\n"
   "Khối lượng rã trong ngày thứ 9: 100 − 91,5 ≈ 8,5 g.",
   "Phân rã trong một khoảng ngắn", RK),

mc("Khi so sánh hai phương pháp xác định tuổi: dùng ¹⁴C (T = 5730 năm) và dùng ²³⁸U "
   "(T = 4,5 tỉ năm), nhận xét nào đúng?",
   ["¹⁴C phù hợp cho mẫu vật hàng tỉ năm tuổi.",
    "¹⁴C phù hợp cho mẫu vật khảo cổ vài nghìn năm, ²³⁸U phù hợp cho đá hàng tỉ năm.",
    "Hai phương pháp cho kết quả như nhau với mọi mẫu vật.",
    "²³⁸U phù hợp cho mẫu gỗ mới chặt."],
   "B",
   "Phương pháp chỉ chính xác khi thời gian cần đo cùng bậc với chu kì bán rã. "
   "Với mẫu quá già, ¹⁴C gần như hết; với mẫu quá trẻ, lượng chì sinh ra từ ²³⁸U quá ít để đo.",
   "Lựa chọn đồng vị xác định tuổi", K, fig="h_dt_c14", cap="Xác định tuổi bằng ¹⁴C"),

mc("Một hạt nhân phóng xạ α. So sánh động năng của hạt α trong hai trường hợp: hạt nhân mẹ đứng "
   "yên và hạt nhân mẹ đang chuyển động cùng chiều với hạt α:",
   ["hai trường hợp cho cùng động năng.",
    "trường hợp hạt nhân mẹ chuyển động cho động năng hạt α lớn hơn.",
    "trường hợp hạt nhân mẹ đứng yên cho động năng lớn hơn.",
    "không xác định được."],
   "B",
   "Trong hệ quy chiếu phòng thí nghiệm, vận tốc của hạt α bằng tổng vận tốc của hạt nhân mẹ và "
   "vận tốc mà phân rã truyền cho nó. Nếu hai vận tốc cùng chiều thì tốc độ tổng lớn hơn, "
   "nên động năng đo được lớn hơn.",
   "Tính tương đối của động năng", K),
],
P2=[
ds("Dùng prôtôn có động năng 5,45 MeV bắn vào hạt nhân ⁹₄Be đứng yên, sinh ra hạt α và hạt nhân "
   "⁶₃Li. Hạt α bay ra vuông góc với phương của prôtôn, động năng 4,00 MeV. "
   "Coi khối lượng tỉ lệ với số khối.",
   [("Phản ứng bảo toàn số khối: 1 + 9 = 4 + 6.", True,
     "Đúng. Tổng số khối hai vế đều bằng 10; điện tích 1 + 4 = 2 + 3 cũng khớp."),
    ("Vì hạt α vuông góc với prôtôn nên p(Li)² = p(p)² + p(α)².", True,
     "Đúng. Tổng động lượng được bảo toàn, và định lí Pi-ta-go áp dụng cho tam giác vuông "
     "tạo bởi ba vectơ động lượng."),
    ("Động năng của hạt nhân liti xấp xỉ 3,58 MeV.", True,
     "Đúng. 6·W(Li) = 1 · 5,45 + 4 · 4,00 = 21,45 ⇒ W(Li) ≈ 3,58 MeV."),
    ("Phản ứng này thu năng lượng khoảng 2,13 MeV.", False,
     "Sai về CHIỀU trao đổi. Tổng động năng sau (7,58 MeV) LỚN HƠN trước (5,45 MeV) nên phản ứng "
     "TOẢ năng lượng 2,13 MeV.")],
   "Bảo toàn động lượng hai chiều", RK),

ds("Một mẫu chứa hai đồng vị phóng xạ độc lập: X có chu kì bán rã 1,0 giờ và Y có chu kì bán rã "
   "2,0 giờ. Ban đầu số hạt nhân X gấp đôi số hạt nhân Y.",
   [("Sau 2,0 giờ, số hạt nhân X còn lại bằng một phần tư giá trị ban đầu của nó.", True,
     "Đúng. X trải qua 2 chu kì nên còn 2⁻² = 1/4."),
    ("Sau 2,0 giờ, số hạt nhân Y còn lại bằng một nửa giá trị ban đầu của nó.", True,
     "Đúng. Y trải qua đúng 1 chu kì."),
    ("Sau 2,0 giờ, tổng số hạt nhân còn lại bằng một phần ba tổng số hạt nhân ban đầu.", True,
     "Đúng. Đặt số hạt Y ban đầu là N thì X là 2N. Còn lại 2N/4 + N/2 = N, "
     "trên tổng ban đầu 3N ⇒ tỉ lệ 1/3."),
    ("Sau 2,0 giờ, số hạt nhân X còn lại nhiều hơn số hạt nhân Y còn lại.", False,
     "Sai. X còn 2N/4 = 0,5N; Y còn N/2 = 0,5N. Hai số bằng nhau chứ X không nhiều hơn.")],
   "Hỗn hợp hai đồng vị", RK),

ds("Một mẫu 1,0 gam ²¹⁰Po (chu kì bán rã 138 ngày), mỗi phân rã toả 5,4 MeV. "
   "Cho Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   [("Số hạt nhân ban đầu xấp xỉ 2,87·10²¹ hạt.", True,
     "Đúng. N₀ = (1,0/210) · 6,02·10²³ ≈ 2,867·10²¹ hạt."),
    ("Tổng năng lượng mà mẫu toả ra cho tới khi phân rã hết xấp xỉ 2,48·10⁹ J.", True,
     "Đúng. E = N₀ · 5,4 · 1,6·10⁻¹³ ≈ 2,48·10⁹ J."),
    ("Một nửa tổng năng lượng đó được toả ra trong 138 ngày đầu tiên.", True,
     "Đúng. Sau một chu kì bán rã, đúng một nửa số hạt nhân đã phân rã nên đã toả ra một nửa "
     "tổng năng lượng."),
    ("Công suất của mẫu không đổi trong suốt quá trình phân rã.", False,
     "Sai. Công suất tỉ lệ với độ phóng xạ nên giảm dần theo hàm mũ: sau 138 ngày chỉ còn một nửa.")],
   "Năng lượng tích luỹ của nguồn", RK),

ds("Xét chuỗi phân rã của ²³⁵₉₂U cho tới hạt nhân bền ²⁰⁷₈₂Pb.",
   [("Chuỗi gồm 7 lần phân rã α.", True,
     "Đúng. Chỉ phân rã α làm giảm số khối: (235 − 207)/4 = 7 lần."),
    ("Chuỗi gồm 4 lần phân rã β⁻.", True,
     "Đúng. Sau 7 lần α, Z = 92 − 14 = 78; cần thêm 4 đơn vị để đạt Z = 82."),
    ("Số nơtron của hạt nhân giảm tổng cộng 18 đơn vị trong toàn chuỗi.", True,
     "Đúng. Ban đầu N = 235 − 92 = 143; cuối cùng N = 207 − 82 = 125; giảm 18."),
    ("Trong chuỗi này, các phân rã β⁻ làm thay đổi số khối của hạt nhân.", False,
     "Sai. Phân rã β⁻ chỉ làm Z tăng 1, số khối A hoàn toàn không đổi vì electron có A = 0.")],
   "Chuỗi phân rã", K),
],
P3=[
sa("Dùng prôtôn có động năng 5,45 MeV bắn vào hạt nhân ⁹₄Be đứng yên, sinh ra hạt α và hạt nhân "
   "⁶₃Li. Hạt α bay vuông góc với phương prôtôn, động năng 4,00 MeV. Coi khối lượng tỉ lệ số khối. "
   "Động năng của hạt nhân liti bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)?",
   "3,58",
   "Hạt α vuông góc với prôtôn nên p(Li)² = p(p)² + p(α)².\n"
   "Vì p² = 2mW và m tỉ lệ với A:  A(Li)·W(Li) = A(p)·W(p) + A(α)·W(α).\n"
   "6·W(Li) = 1 · 5,45 + 4 · 4,00 = 21,45 ⇒ W(Li) = 21,45/6 ≈ 3,58 MeV.",
   "Bảo toàn động lượng hai chiều", RK),

sa("Tổng năng lượng mà 2,0 gam ²¹⁰Po toả ra cho tới khi phân rã hết bằng bao nhiêu jun "
   "(viết dưới dạng x·10⁹, chỉ ghi giá trị x, làm tròn đến chữ số thập phân thứ hai)? "
   "Mỗi phân rã toả 5,4 MeV; Nₐ = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J.",
   "4,95",
   "Số hạt nhân ban đầu: N₀ = (2,0/210) · 6,02·10²³ ≈ 5,733·10²¹ hạt.\n"
   "Tổng số phân rã bằng N₀.\n"
   "E = 5,733·10²¹ · 5,4 · 1,6·10⁻¹³ = 5,733·10²¹ · 8,64·10⁻¹³ ≈ 4,95·10⁹ J.",
   "Năng lượng tích luỹ của nguồn", RK),

sa("Một mẫu chứa hai đồng vị phóng xạ X (chu kì bán rã 2,0 giờ) và Y (chu kì bán rã 4,0 giờ). "
   "Sau 4,0 giờ, tổng số hạt nhân còn lại bằng 1/3 tổng số hạt nhân ban đầu. "
   "Ban đầu số hạt nhân X gấp bao nhiêu lần số hạt nhân Y?",
   "2",
   "Sau 4,0 giờ: X trải qua 2 chu kì nên còn N₁/4; Y trải qua 1 chu kì nên còn N₂/2.\n"
   "(N₁/4 + N₂/2)/(N₁ + N₂) = 1/3 ⇒ 0,75N₁ + 1,5N₂ = N₁ + N₂.\n"
   "0,5N₂ = 0,25N₁ ⇒ N₁ = 2N₂.",
   "Hỗn hợp hai đồng vị", RK),

sa("Hạt nhân ²³⁵₉₂U biến đổi thành hạt nhân bền ²⁰⁷₈₂Pb qua một chuỗi phân rã. "
   "Tổng số lần phân rã β⁻ trong chuỗi bằng bao nhiêu?",
   "4",
   "Số lần α: (235 − 207)/4 = 7 lần, làm Z giảm 14 đơn vị: 92 − 14 = 78.\n"
   "Muốn đạt Z = 82 phải tăng thêm 4 đơn vị, ứng với 4 lần phân rã β⁻.",
   "Chuỗi phân rã", K),

sa("Một nguồn phóng xạ có công suất ban đầu 640 W và chu kì bán rã 28 năm. Sau 112 năm, "
   "công suất của nguồn bằng bao nhiêu oát?",
   "40",
   "Số chu kì: n = 112/28 = 4.\n"
   "Công suất tỉ lệ với độ phóng xạ nên P = 640/2⁴ = 640/16 = 40 W.",
   "Công suất nguồn phóng xạ theo thời gian", K),

sa("Một mẫu chất phóng xạ nguyên chất, sau thời gian t₁ thì 30 % số hạt nhân đã phân rã. "
   "Sau thời gian 2·t₁, phần trăm số hạt nhân đã phân rã bằng bao nhiêu phần trăm?",
   "51",
   "Sau t₁ còn lại 70 % = 0,70.\n"
   "Sau 2t₁ còn lại (0,70)² = 0,49 = 49 %.\n"
   "Phần đã phân rã: 100 − 49 = 51 %.",
   "Bản chất hàm mũ của phân rã", RK),
])


# =====================================================================  ĐỀ 10
DE10 = dict(
ma="12C4-Đ10", ten="ĐỀ SỐ 10", muc="Khó – phân loại học sinh giỏi",
trongtam="Phản ứng bắn phá với ràng buộc động học, so sánh hai nguồn phóng xạ, tuổi mẫu đá",
P1=[
mc("Dùng hạt α có động năng 8,0 MeV bắn vào hạt nhân ²⁷₁₃Al đứng yên, thu được hạt nhân ³⁰₁₅P và "
   "một nơtron. Phản ứng thu 2,7 MeV. Hai hạt sinh ra bay đi với cùng tốc độ. "
   "Động năng của nơtron xấp xỉ",
   ["0,09 MeV.", "0,17 MeV.", "5,13 MeV.", "2,65 MeV."],
   "B",
   "Tổng động năng sau phản ứng: W = 8,0 − 2,7 = 5,3 MeV.\n"
   "Hai hạt cùng tốc độ nên động năng W = ½mv² tỉ lệ THUẬN với khối lượng, tức tỉ lệ với số khối:\n"
   "W(n) : W(P) = 1 : 30.\n"
   "W(n) = 5,3 · 1/31 ≈ 0,17 MeV.",
   "Phản ứng bắn phá có ràng buộc động học", RK),

mc("Một hạt nhân ²¹⁰₈₄Po đứng yên phóng xạ α. Phần trăm năng lượng toả ra mà hạt α mang đi "
   "xấp xỉ (coi khối lượng tỉ lệ với số khối)",
   ["1,9 %.", "98,1 %.", "50,0 %.", "95,2 %."],
   "B",
   "Bảo toàn động lượng: hai hạt có cùng độ lớn động lượng nên W tỉ lệ nghịch với khối lượng.\n"
   "W(α)/ΔE = m(con)/(m(α) + m(con)) = 206/210 ≈ 0,981 = 98,1 %.\n"
   "Hạt nhẹ mang gần như toàn bộ năng lượng toả ra.",
   "Bảo toàn động lượng trong phân rã", K, fig="h_sd_phan_ra_po",
   cap="Sơ đồ phân rã của pôlôni"),

mc("Mẫu A có độ phóng xạ ban đầu 1000 Bq, chu kì bán rã 2,0 giờ. Mẫu B có độ phóng xạ ban đầu "
   "250 Bq, chu kì bán rã 6,0 giờ. Sau bao lâu thì độ phóng xạ hai mẫu bằng nhau?",
   ["3,0 giờ.", "6,0 giờ.", "4,0 giờ.", "12,0 giờ."],
   "B",
   "1000 · 2^(−t/2) = 250 · 2^(−t/6)  ⇒  4 = 2^(t/2 − t/6) = 2^(t/3).\n"
   "2² = 2^(t/3) ⇒ t/3 = 2 ⇒ t = 6,0 giờ.\n"
   "Kiểm tra: sau 6 giờ, A còn 1000/8 = 125 Bq; B còn 250/2 = 125 Bq ✓.",
   "So sánh hai nguồn phóng xạ", RK),

mc("Một mẫu đá chứa ²³⁸U (chu kì bán rã 4,5 tỉ năm) và ²⁰⁶Pb. Tỉ số KHỐI LƯỢNG chì trên khối lượng "
   "urani còn lại là 0,10. Tuổi của mẫu đá xấp xỉ (ln2 ≈ 0,693)",
   ["3,5·10⁸ năm.", "7,1·10⁸ năm.", "1,4·10⁹ năm.", "4,5·10⁹ năm."],
   "B",
   "Tỉ số khối lượng: (206/238)·(2ⁿ − 1) = 0,10 ⇒ 2ⁿ − 1 = 0,10 · 238/206 ≈ 0,1155.\n"
   "2ⁿ = 1,1155 ⇒ n = ln1,1155/ln2 = 0,1093/0,693 ≈ 0,1577.\n"
   "t = 0,1577 · 4,5·10⁹ ≈ 7,1·10⁸ năm.",
   "Xác định tuổi mẫu đá", RK),

mc("Trong khoảng thời gian bằng một chu kì bán rã đầu tiên, tổng số phân rã của một mẫu chất "
   "phóng xạ nguyên chất có N₀ hạt nhân bằng",
   ["N₀.", "N₀/2.", "N₀/4.", "N₀·ln2."],
   "B",
   "Sau một chu kì bán rã, đúng một nửa số hạt nhân đã phân rã: ΔN = N₀ − N₀/2 = N₀/2. "
   "Mỗi hạt nhân phân rã ứng với một lần phân rã.",
   "Tổng số phân rã", K),

mc("Một hạt nhân đứng yên phóng xạ α. Gọi v(α) và v(con) là tốc độ của hai hạt sinh ra. "
   "Với phân rã ²¹⁰Po → ²⁰⁶Pb, tỉ số v(α)/v(con) bằng",
   ["4/206.", "206/4.", "1.", "√(206/4)."],
   "B",
   "Bảo toàn động lượng: m(α)·v(α) = m(con)·v(con).\n"
   "v(α)/v(con) = m(con)/m(α) = 206/4 = 51,5.\n"
   "Hạt nhẹ bay nhanh hơn đúng theo tỉ số khối lượng.",
   "Bảo toàn động lượng trong phân rã", K),

mc("Khi tính trên cùng 1,0 kg nhiên liệu, năng lượng của phản ứng nhiệt hạch ²H + ³H "
   "(17,6 MeV mỗi phản ứng, 5 nuclêôn tham gia) so với phân hạch ²³⁵U "
   "(200 MeV mỗi phản ứng, 235 nuclêôn) lớn hơn khoảng",
   ["2 lần.", "4 lần.", "10 lần.", "20 lần."],
   "B",
   "Nhiệt hạch: 17,6/5 = 3,52 MeV mỗi nuclêôn.\n"
   "Phân hạch: 200/235 ≈ 0,851 MeV mỗi nuclêôn.\n"
   "Tỉ số: 3,52/0,851 ≈ 4,1, tức khoảng 4 lần. Vì số nuclêôn tỉ lệ với khối lượng nên đây cũng "
   "là tỉ số năng lượng tính trên cùng một khối lượng nhiên liệu.",
   "So sánh phân hạch và nhiệt hạch", K, fig="h_dt_nllk_rieng",
   cap="Năng lượng liên kết riêng theo số khối"),

mc("Một chất phóng xạ có chu kì bán rã T. Số hạt nhân phân rã trong khoảng thời gian từ t đến "
   "t + T luôn bằng",
   ["N₀/2 với mọi t.", "một nửa số hạt nhân còn lại ở thời điểm t.",
    "N₀/4 với mọi t.", "không xác định được."],
   "B",
   "Tại thời điểm t còn N(t) hạt; sau thêm một chu kì còn N(t)/2. "
   "Số hạt phân rã trong khoảng đó là N(t)/2 — luôn bằng một nửa số hạt còn lại ở đầu khoảng, "
   "chứ không phải một giá trị cố định.",
   "Bản chất hàm mũ của phân rã", RK),

mc("Dùng prôtôn có động năng W bắn vào hạt nhân ⁷₃Li đứng yên, tạo thành hai hạt α giống nhau bay "
   "đối xứng qua phương của prôtôn. Nếu phản ứng toả năng lượng ΔE thì động năng mỗi hạt α bằng",
   ["(W + ΔE).", "(W + ΔE)/2.", "(W − ΔE)/2.", "ΔE/2."],
   "B",
   "Bảo toàn năng lượng: tổng động năng sau = W + ΔE.\n"
   "Hai hạt α giống nhau bay đối xứng nên chia đều động năng: mỗi hạt được (W + ΔE)/2.",
   "Bảo toàn năng lượng và đối xứng", RK),

mc("Một nguồn phóng xạ dùng trong y tế có chu kì bán rã 6,0 giờ. Bệnh viện nhận nguồn lúc 8 giờ "
   "sáng với độ phóng xạ 800 MBq. Muốn dùng nguồn khi độ phóng xạ còn ít nhất 200 MBq thì thời "
   "điểm muộn nhất có thể dùng là",
   ["14 giờ cùng ngày.", "20 giờ cùng ngày.", "2 giờ sáng hôm sau.", "8 giờ sáng hôm sau."],
   "B",
   "800 → 200 là giảm 4 lần = 2², tức 2 chu kì bán rã = 12 giờ.\n"
   "Thời điểm muộn nhất: 8 giờ + 12 giờ = 20 giờ cùng ngày.",
   "Ứng dụng thực tiễn của định luật phóng xạ", K),

mc("Hai đồng vị phóng xạ có chu kì bán rã T và 3T. Ban đầu số hạt nhân bằng nhau. "
   "Sau thời gian 3T, tỉ số số hạt nhân còn lại của đồng vị thứ nhất so với thứ hai bằng",
   ["1 : 2.", "1 : 4.", "1 : 8.", "2 : 1."],
   "B",
   "Đồng vị 1 trải qua 3 chu kì nên còn N₀/8.\n"
   "Đồng vị 2 trải qua 1 chu kì nên còn N₀/2.\n"
   "Tỉ số: (N₀/8)/(N₀/2) = 1/4 = 1 : 4.",
   "So sánh hai chất phóng xạ", K),

mc("Một mẫu chất phóng xạ nguyên chất có chu kì bán rã T. Thời gian để số hạt nhân giảm từ 90 % "
   "xuống 10 % giá trị ban đầu xấp xỉ (ln2 ≈ 0,693)",
   ["2,17·T.", "3,17·T.", "1,17·T.", "4,17·T."],
   "B",
   "Đặt n = t/T. Số hạt giảm từ 0,90N₀ xuống 0,10N₀, tức giảm 9 lần.\n"
   "2ⁿ = 9 ⇒ n = ln9/ln2 = 2,197/0,693 ≈ 3,17.\n"
   "Vậy t ≈ 3,17·T.",
   "Định luật phóng xạ – dùng logarit", RK),

mc("Trong phản ứng phân hạch, sản phẩm thường gồm hai mảnh vỡ có số khối rất chênh lệch. "
   "Nếu hai mảnh vỡ có số khối 95 và 138 thì tỉ số ĐỘNG NĂNG của chúng ngay sau phân hạch "
   "(bỏ qua động lượng của nơtron) xấp xỉ",
   ["95 : 138.", "138 : 95.", "1 : 1.", "138² : 95²."],
   "B",
   "Hai mảnh bay ngược chiều với cùng độ lớn động lượng, nên W = p²/(2m) tỉ lệ nghịch với khối lượng:\n"
   "W(95)/W(138) = 138/95.\n"
   "Mảnh NHẸ hơn mang nhiều động năng hơn.",
   "Bảo toàn động lượng trong phân hạch", RK, fig="h_sd_phan_hach",
   cap="Phản ứng phân hạch"),

mc("Một mẫu chất phóng xạ có độ phóng xạ 8000 Bq. Sau 10 phút, độ phóng xạ còn 1000 Bq. "
   "Độ phóng xạ của mẫu sau 25 phút kể từ lúc đầu bằng",
   ["125 Bq.", "44,2 Bq.", "62,5 Bq.", "31,3 Bq."],
   "B",
   "Giảm 8 lần trong 10 phút ⇒ 10 phút = 3 chu kì ⇒ T = 10/3 phút.\n"
   "Sau 25 phút: n = 25/(10/3) = 7,5 chu kì.\n"
   "H = 8000 · 2⁻⁷·⁵ = 8000/2⁷·⁵.  Vì 2⁷ = 128 và 2⁰·⁵ = 1,414 nên 2⁷·⁵ ≈ 181,0.\n"
   "H ≈ 8000/181,0 ≈ 44,2 Bq.",
   "Định luật phóng xạ – số mũ không nguyên", RK),

mc("Một hạt nhân X đứng yên phân rã thành hai hạt có số khối 4 và 206, toả ra năng lượng 5,4 MeV. "
   "Tổng động lượng của hai hạt sau phân rã bằng",
   ["một giá trị khác không.", "không.",
    "tỉ lệ với 5,4 MeV.", "tỉ lệ với 210."],
   "B",
   "Hạt nhân mẹ đứng yên nên tổng động lượng ban đầu bằng 0. Định luật bảo toàn động lượng cho "
   "biết tổng động lượng sau cũng bằng 0: hai hạt có động lượng cùng độ lớn, ngược hướng.",
   "Bảo toàn động lượng", K),

mc("Xét hai mẫu chất phóng xạ cùng đồng vị. Mẫu thứ hai được lấy muộn hơn mẫu thứ nhất một khoảng "
   "thời gian bằng 2 chu kì bán rã, với khối lượng ban đầu bằng nhau. Tại một thời điểm quan sát "
   "chung, độ phóng xạ của mẫu thứ hai so với mẫu thứ nhất",
   ["nhỏ hơn 4 lần.", "lớn hơn 4 lần.", "bằng nhau.", "nhỏ hơn 2 lần."],
   "B",
   "Mẫu thứ hai mới bắt đầu phân rã muộn hơn 2 chu kì, nên tại thời điểm quan sát nó đã phân rã "
   "ít hơn đúng 2 chu kì so với mẫu thứ nhất. Vì vậy độ phóng xạ của nó lớn gấp 2² = 4 lần.",
   "So sánh hai mẫu phóng xạ", RK),

mc("Một chất phóng xạ có chu kì bán rã T. Gọi Δ₁ là số hạt phân rã trong chu kì đầu tiên và Δ₂ là "
   "số hạt phân rã trong chu kì thứ hai. Tỉ số Δ₁/Δ₂ bằng",
   ["1.", "2.", "4.", "1/2."],
   "B",
   "Δ₁ = N₀ − N₀/2 = N₀/2;  Δ₂ = N₀/2 − N₀/4 = N₀/4.\n"
   "Δ₁/Δ₂ = 2. Trong các chu kì liên tiếp, số hạt phân rã giảm theo cấp số nhân với công bội 1/2.",
   "Số hạt phân rã theo từng chu kì", K),

mc("Trong một nhà máy điện hạt nhân, nếu nâng hiệu suất chuyển hoá từ 30 % lên 40 % mà giữ nguyên "
   "công suất điện thì lượng nhiên liệu tiêu thụ mỗi ngày",
   ["tăng 4/3 lần.", "giảm còn 3/4 lần.", "không đổi.", "giảm còn 1/2."],
   "B",
   "Công suất nhiệt cần thiết P(nhiệt) = P(điện)/H, tỉ lệ nghịch với hiệu suất.\n"
   "Hiệu suất tăng từ 0,30 lên 0,40 (tức nhân 4/3) nên nhiên liệu giảm còn 0,30/0,40 = 3/4 lần.",
   "Hiệu suất của nhà máy điện hạt nhân", K, fig="h_sd_lo_phan_ung",
   cap="Sơ đồ nhà máy điện hạt nhân"),
],
P2=[
ds("Một hạt nhân ²¹⁰₈₄Po đứng yên phóng xạ α, toả ra năng lượng 5,4 MeV. "
   "Coi khối lượng các hạt tỉ lệ với số khối.",
   [("Hai hạt sinh ra có động lượng cùng độ lớn và ngược hướng.", True,
     "Đúng. Hạt nhân mẹ đứng yên nên tổng động lượng ban đầu bằng 0 và được bảo toàn."),
    ("Tốc độ của hạt α lớn gấp 51,5 lần tốc độ của hạt nhân chì.", True,
     "Đúng. Từ m(α)·v(α) = m(Pb)·v(Pb) suy ra v(α)/v(Pb) = 206/4 = 51,5."),
    ("Hạt α mang khoảng 98,1 % năng lượng toả ra.", True,
     "Đúng. W(α)/ΔE = 206/210 ≈ 0,981."),
    ("Hạt nhân chì mang nhiều động năng hơn hạt α vì nó nặng hơn.", False,
     "Sai. Với cùng độ lớn động lượng, động năng W = p²/(2m) tỉ lệ NGHỊCH với khối lượng. "
     "Hạt nhân chì chỉ mang khoảng 5,4 − 5,30 = 0,10 MeV.")],
   "Bảo toàn động lượng trong phân rã", K, fig="h_sd_phan_ra_po",
   cap="Sơ đồ phân rã của pôlôni"),

ds("Mẫu A có độ phóng xạ ban đầu 1000 Bq và chu kì bán rã 2,0 giờ; mẫu B có độ phóng xạ ban đầu "
   "250 Bq và chu kì bán rã 6,0 giờ.",
   [("Ban đầu độ phóng xạ của A lớn gấp 4 lần của B.", True,
     "Đúng. 1000/250 = 4."),
    ("Số hạt nhân ban đầu của B lớn hơn của A.", False,
     "Sai. N = H·T/ln2 nên số hạt tỉ lệ với tích H·T:  "
     "với A là 1000 · 2,0 = 2000 (đơn vị quy ước), với B là 250 · 6,0 = 1500. "
     "Vậy mẫu A mới có nhiều hạt nhân hơn."),
    ("Sau 6,0 giờ, độ phóng xạ của hai mẫu bằng nhau và bằng 125 Bq.", True,
     "Đúng. A còn 1000/2³ = 125 Bq; B còn 250/2 = 125 Bq."),
    ("Sau 12 giờ, độ phóng xạ của B lớn hơn của A.", True,
     "Đúng. A còn 1000/2⁶ ≈ 15,6 Bq; B còn 250/2² = 62,5 Bq.")],
   "So sánh hai nguồn phóng xạ", RK),

ds("Một mẫu đá chứa ²³⁸U (chu kì bán rã 4,5 tỉ năm) và sản phẩm bền cuối cùng ²⁰⁶Pb.",
   [("Tỉ số SỐ HẠT NHÂN chì trên urani còn lại sau n chu kì bán rã bằng 2ⁿ − 1.", True,
     "Đúng. Số hạt con bằng số hạt mẹ đã rã: (N₀ − N)/N = 2ⁿ − 1."),
    ("Tỉ số KHỐI LƯỢNG chì trên urani phải nhân thêm hệ số 206/238.", True,
     "Đúng. Khối lượng bằng số hạt nhân nhân với số khối."),
    ("Nếu tỉ số khối lượng chì trên urani là 0,10 thì tuổi mẫu đá khoảng 7,1·10⁸ năm.", True,
     "Đúng. 2ⁿ − 1 = 0,10 · 238/206 ≈ 0,1155 ⇒ n ≈ 0,158 ⇒ t ≈ 7,1·10⁸ năm."),
    ("Phương pháp này chỉ dùng được cho mẫu vật dưới 50 000 năm tuổi.", False,
     "Sai. Giới hạn 50 000 năm là của phương pháp ¹⁴C. Với chu kì bán rã 4,5 tỉ năm, "
     "cặp U–Pb dùng để xác định tuổi các mẫu đá hàng trăm triệu tới hàng tỉ năm.")],
   "Xác định tuổi mẫu đá", RK),

ds("Xét quy luật phân rã của một mẫu chất phóng xạ nguyên chất có N₀ hạt nhân, chu kì bán rã T.",
   [("Số hạt phân rã trong chu kì đầu tiên gấp đôi số hạt phân rã trong chu kì thứ hai.", True,
     "Đúng. N₀/2 so với N₀/4."),
    ("Trong bất kì khoảng thời gian nào dài bằng T, số hạt phân rã đều bằng N₀/2.", False,
     "Sai. Số hạt phân rã trong khoảng đó bằng một nửa số hạt CÒN LẠI ở đầu khoảng, "
     "và số đó giảm dần theo thời gian."),
    ("Thời gian để số hạt giảm từ 90 % xuống 10 % ban đầu xấp xỉ 3,17·T.", True,
     "Đúng. Giảm 9 lần: n = ln9/ln2 ≈ 3,17."),
    ("Tổng số phân rã trong toàn bộ thời gian cho tới khi mẫu hết hẳn bằng N₀.", True,
     "Đúng. Mỗi hạt nhân chỉ phân rã một lần nên tổng số phân rã bằng đúng số hạt nhân ban đầu.")],
   "Bản chất hàm mũ của phân rã", RK),
],
P3=[
sa("Dùng hạt α có động năng 6,0 MeV bắn vào hạt nhân ²⁷₁₃Al đứng yên, thu được hạt nhân ³⁰₁₅P và "
   "một nơtron. Phản ứng thu 2,9 MeV. Hai hạt sinh ra bay đi với cùng tốc độ. "
   "Động năng của nơtron bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)?",
   "0,10",
   "Tổng động năng sau: W = 6,0 − 2,9 = 3,1 MeV.\n"
   "Hai hạt cùng tốc độ nên động năng tỉ lệ thuận với số khối: W(n) : W(P) = 1 : 30.\n"
   "W(n) = 3,1 · 1/31 = 0,10 MeV.",
   "Phản ứng bắn phá có ràng buộc động học", RK),

sa("Hai nguồn phóng xạ dùng trong phòng thí nghiệm được chuẩn bị cùng lúc. Nguồn thứ nhất có "
   "độ phóng xạ 1600 Bq và chu kì bán rã 3,0 giờ; nguồn thứ hai có độ phóng xạ 200 Bq và chu kì "
   "bán rã 9,0 giờ. Kể từ lúc chuẩn bị, sau bao nhiêu giờ thì hai nguồn có độ phóng xạ bằng nhau?",
   "13,5",
   "1600 · 2^(−t/3) = 200 · 2^(−t/9)  ⇒  8 = 2^(t/3 − t/9) = 2^(2t/9).\n"
   "2³ = 2^(2t/9) ⇒ 2t/9 = 3 ⇒ t = 13,5 giờ.\n"
   "Kiểm tra: A còn 1600·2^(−4,5) ≈ 70,7 Bq;  B còn 200·2^(−1,5) ≈ 70,7 Bq ✓.",
   "So sánh hai nguồn phóng xạ", RK),

sa("Một hạt nhân ²²⁶₈₈Ra đứng yên phóng xạ α, toả ra năng lượng 4,8 MeV. Động năng của hạt α "
   "bằng bao nhiêu MeV (làm tròn đến chữ số thập phân thứ hai)? Coi khối lượng tỉ lệ số khối.",
   "4,71",
   "Hạt nhân con là ²²²₈₆Rn.\n"
   "Bảo toàn động lượng ⇒ W(α)/ΔE = A(con)/(A(α) + A(con)) = 222/226.\n"
   "W(α) = 4,8 · 222/226 = 1065,6/226 ≈ 4,71 MeV.",
   "Bảo toàn động lượng trong phân rã", RK),

sa("Một mẫu chất phóng xạ nguyên chất có chu kì bán rã T. Thời gian để số hạt nhân giảm từ 80 % "
   "xuống 20 % giá trị ban đầu bằng bao nhiêu lần T?",
   "2",
   "Số hạt giảm từ 0,80N₀ xuống 0,20N₀, tức giảm đúng 4 lần = 2².\n"
   "Vậy khoảng thời gian đó bằng 2 chu kì bán rã: t = 2T.",
   "Định luật phóng xạ", K),

sa("Một mẫu đá chứa ²³⁸U (chu kì bán rã 4,5 tỉ năm) và ²⁰⁶Pb. Tỉ số khối lượng chì trên khối lượng "
   "urani còn lại bằng 0,26. Tuổi của mẫu đá bằng bao nhiêu tỉ năm "
   "(làm tròn đến chữ số thập phân thứ nhất)? Lấy ln2 ≈ 0,693.",
   "1,7",
   "(206/238)·(2ⁿ − 1) = 0,26 ⇒ 2ⁿ − 1 = 0,26 · 238/206 ≈ 0,3004.\n"
   "2ⁿ = 1,3004 ⇒ n = ln1,3004/ln2 = 0,2627/0,693 ≈ 0,379.\n"
   "t = 0,379 · 4,5 ≈ 1,7 tỉ năm.",
   "Xác định tuổi mẫu đá", RK),

sa("Một nguồn phóng xạ dùng trong xạ trị có chu kì bán rã 5,0 năm, độ phóng xạ ban đầu 3200 GBq. "
   "Bệnh viện chỉ sử dụng nguồn khi độ phóng xạ còn ít nhất 400 GBq. "
   "Nguồn được dùng trong tối đa bao nhiêu năm?",
   "15",
   "3200 → 400 là giảm 8 lần = 2³ ⇒ n = 3 chu kì bán rã.\n"
   "t = 3 · 5,0 = 15 năm.",
   "Ứng dụng thực tiễn của định luật phóng xạ", K),
])


NHOM = dict(
    ten_nhom="LỚP 12 – CHƯƠNG 4: VẬT LÍ HẠT NHÂN",
    mo_ta="Bộ 10 đề luyện tập, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó, phân loại học sinh giỏi)",
    pham_vi=(
        "Bài 18. Cấu trúc hạt nhân. Độ hụt khối. Năng lượng liên kết\n"
        "Bài 19. Hiện tượng phóng xạ. Định luật phóng xạ  •  "
        "Bài 20. Phản ứng hạt nhân. Phân hạch. Nhiệt hạch\n"
        "Bài 21. Ứng dụng của đồng vị phóng xạ. An toàn bức xạ\n"
        "Hằng số dùng thống nhất: 1 u = 1,66055·10⁻²⁷ kg; 1 u·c² = 931,5 MeV; c = 3,0·10⁸ m/s; "
        "m(p) = 1,0073 u; m(n) = 1,0087 u; m(e) = 0,00055 u; Nₐ = 6,02·10²³ mol⁻¹; "
        "1 MeV = 1,6·10⁻¹³ J; ln2 ≈ 0,693."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
