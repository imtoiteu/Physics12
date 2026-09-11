# -*- coding: utf-8 -*-
"""LỚP 12 – CHƯƠNG 3: TỪ TRƯỜNG.  10 đề luyện tập, độ khó tăng dần.

Hằng số và quy ước dùng thống nhất trong cả bộ:
  g = 10 m/s²;  √2 ≈ 1,414;  π ≈ 3,1416.
  Mọi giá trị điện áp, cường độ dòng điện ghi trên thiết bị đều là GIÁ TRỊ HIỆU DỤNG.
"""
from qbase import mc, ds, sa, D, TB, K, RK

# =====================================================================  ĐỀ 1
DE1 = dict(
ma="12C3-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Nhận biết từ trường, đường sức từ, lực từ, từ thông và các công thức cơ bản",
P1=[
mc("Từ trường tồn tại ở xung quanh",
   ["mọi vật mang khối lượng.",
    "nam châm và dòng điện.",
    "các điện tích đứng yên.",
    "mọi vật nhiễm điện."],
   "B",
   "Từ trường chỉ tồn tại quanh nam châm và quanh dòng điện, tức quanh các điện tích CHUYỂN ĐỘNG. "
   "Điện tích đứng yên chỉ sinh ra điện trường, không sinh ra từ trường.",
   "Khái niệm từ trường", D),

mc("Đơn vị của cảm ứng từ trong hệ SI là",
   ["vêbe (Wb).", "tesla (T).", "henry (H).", "vôn (V)."],
   "B",
   "Cảm ứng từ B đo bằng tesla. Vêbe là đơn vị của từ thông, vôn là đơn vị của suất điện động.",
   "Đơn vị cảm ứng từ", D),

mc("Để nhận biết tại một điểm trong không gian có từ trường hay không, người ta dùng",
   ["một quả cầu tích điện.", "một kim nam châm thử.",
    "một nhiệt kế.", "một điện nghiệm."],
   "B",
   "Kim nam châm thử đặt trong từ trường sẽ bị lệch và nằm cân bằng theo một hướng xác định. "
   "Quả cầu tích điện và điện nghiệm chỉ dùng để nhận biết điện trường.",
   "Nhận biết từ trường", D),

mc("Bên ngoài một nam châm thẳng, các đường sức từ có chiều",
   ["đi ra ở cực Nam và đi vào ở cực Bắc.",
    "đi ra ở cực Bắc và đi vào ở cực Nam.",
    "luôn hướng từ trên xuống dưới.",
    "hướng vào tâm của nam châm."],
   "B",
   "Quy ước: bên ngoài nam châm, đường sức từ đi RA từ cực Bắc và đi VÀO cực Nam; "
   "trong lòng nam châm thì ngược lại, nhờ đó đường sức khép kín.",
   "Đường sức từ", D, fig="t_sd_duongsuc_ncthang", cap="Đường sức từ của nam châm thẳng"),

mc("Phát biểu nào sau đây về đường sức từ là SAI?",
   ["Qua mỗi điểm trong từ trường chỉ vẽ được một đường sức từ.",
    "Hai đường sức từ có thể cắt nhau tại một điểm.",
    "Nơi từ trường mạnh thì các đường sức từ được vẽ dày hơn.",
    "Các đường sức từ là những đường cong khép kín."],
   "B",
   "Nếu hai đường sức cắt nhau thì tại giao điểm sẽ có hai hướng của vectơ cảm ứng từ, "
   "trong khi kim nam châm thử chỉ nằm cân bằng theo một hướng duy nhất. Vậy đường sức từ "
   "không bao giờ cắt nhau.",
   "Tính chất đường sức từ", D),

mc("Quy tắc nắm tay phải được dùng để xác định",
   ["chiều của lực từ tác dụng lên dây dẫn.",
    "chiều của đường sức từ do dòng điện sinh ra.",
    "độ lớn của cảm ứng từ.",
    "chiều của từ thông qua khung dây."],
   "B",
   "Nắm bàn tay phải, ngón cái chỉ chiều dòng điện thì bốn ngón khum lại chỉ chiều đường sức từ. "
   "Chiều lực từ được xác định bằng quy tắc bàn tay TRÁI.",
   "Quy tắc nắm tay phải", D, fig="t_sd_duongsuc_daythang",
   cap="Đường sức từ quanh dòng điện thẳng"),

mc("Lực từ tác dụng lên một đoạn dây dẫn thẳng mang dòng điện đặt trong từ trường đều "
   "có độ lớn được tính bằng công thức",
   ["F = BIℓ·cosα.", "F = BIℓ·sinα.", "F = BI/ℓ.", "F = B·ℓ/I."],
   "B",
   "F = B·I·ℓ·sinα với α là góc hợp bởi đoạn dây và vectơ cảm ứng từ. "
   "Chỉ thành phần từ trường vuông góc với dây mới gây ra lực từ, nên công thức chứa sinα.",
   "Công thức lực từ", D),

mc("Một đoạn dây dẫn mang dòng điện được đặt song song với các đường sức từ. "
   "Lực từ tác dụng lên đoạn dây đó",
   ["có giá trị lớn nhất.", "bằng không.",
    "bằng một nửa giá trị lớn nhất.", "có phương song song với dây."],
   "B",
   "Dây song song với đường sức nên α = 0°, do đó sinα = 0 và F = 0. "
   "Có thể hiểu trực quan: không tồn tại thành phần từ trường vuông góc với dây.",
   "Lực từ – trường hợp đặc biệt", D, fig="t_sd_goc_alpha",
   cap="Dây dẫn hợp góc α với đường sức từ"),

mc("Đặt bàn tay trái sao cho các đường sức từ xuyên vào lòng bàn tay, chiều từ cổ tay đến ngón "
   "giữa là chiều dòng điện. Khi đó ngón cái choãi ra 90° chỉ",
   ["chiều của lực từ tác dụng lên dòng điện.",
    "chiều đường sức từ của ống dây.",
    "chiều của dòng điện cảm ứng.",
    "độ lớn của từ thông."],
   "A",
   "Đặt bàn tay trái sao cho đường sức từ xuyên vào lòng bàn tay, chiều từ cổ tay đến ngón giữa "
   "là chiều dòng điện, ngón cái choãi 90° chỉ chiều lực từ.",
   "Quy tắc bàn tay trái", D, fig="t_sd_luctu", cap="Lực từ tác dụng lên dây dẫn"),

mc("Đơn vị của từ thông trong hệ SI là",
   ["tesla (T).", "vêbe (Wb).", "ampe (A).", "jun (J)."],
   "B",
   "Từ thông đo bằng vêbe: 1 Wb = 1 T·m². Tesla là đơn vị của cảm ứng từ.",
   "Đơn vị từ thông", D),

mc("Từ thông qua một khung dây phẳng diện tích S đặt trong từ trường đều B được tính bằng",
   ["Φ = B·S·sinθ với θ là góc giữa B và mặt phẳng khung.",
    "Φ = B·S·cosθ với θ là góc giữa B và vectơ pháp tuyến của khung.",
    "Φ = B/S.", "Φ = B·S·tanθ."],
   "B",
   "Φ = B·S·cosθ, trong đó θ là góc hợp bởi vectơ cảm ứng từ và vectơ PHÁP TUYẾN của mặt phẳng khung. "
   "Lưu ý phân biệt với góc giữa B và mặt phẳng khung.",
   "Công thức từ thông", D, fig="t_sd_tuthong", cap="Từ thông qua khung dây"),

mc("Từ thông qua một khung dây bằng không khi vectơ cảm ứng từ",
   ["vuông góc với mặt phẳng khung.",
    "nằm trong mặt phẳng khung.",
    "hợp với mặt phẳng khung một góc 60°.",
    "có độ lớn rất nhỏ nhưng khác không."],
   "B",
   "Khi B nằm trong mặt phẳng khung thì B vuông góc với pháp tuyến, θ = 90°, nên cosθ = 0 và Φ = 0. "
   "Lúc đó không có đường sức nào xuyên qua khung.",
   "Từ thông – trường hợp đặc biệt", D),

mc("Dòng điện cảm ứng xuất hiện trong một mạch kín khi",
   ["mạch được đặt trong từ trường mạnh.",
    "từ thông qua mạch biến thiên.",
    "mạch có điện trở nhỏ.",
    "mạch chuyển động với tốc độ lớn."],
   "B",
   "Điều kiện duy nhất để có dòng điện cảm ứng là từ thông qua mạch kín BIẾN THIÊN. "
   "Một mạch đặt yên trong từ trường rất mạnh cũng không có dòng cảm ứng.",
   "Điều kiện có dòng cảm ứng", D, fig="t_sd_tn_faraday",
   cap="Thí nghiệm về cảm ứng điện từ"),

mc("Theo định luật Lenz, dòng điện cảm ứng có chiều sao cho từ trường do nó sinh ra",
   ["cùng chiều với từ trường ban đầu trong mọi trường hợp.",
    "chống lại nguyên nhân đã sinh ra nó.",
    "vuông góc với từ trường ban đầu.",
    "có độ lớn bằng từ trường ban đầu."],
   "B",
   "Định luật Lenz là biểu hiện của định luật bảo toàn năng lượng: dòng cảm ứng luôn chống lại "
   "sự biến thiên từ thông. Khi từ thông tăng, B cảm ứng ngược chiều B; khi giảm thì cùng chiều.",
   "Định luật Lenz", D, fig="t_sd_lenz", cap="Chiều dòng điện cảm ứng"),

mc("Suất điện động cảm ứng trong một cuộn dây N vòng được tính bằng công thức",
   ["e = N·ΔΦ·Δt.", "e = −N·ΔΦ/Δt.", "e = −ΔΦ/(N·Δt).", "e = N/(ΔΦ·Δt)."],
   "B",
   "Định luật Faraday: e = −N·ΔΦ/Δt. Dấu trừ diễn tả định luật Lenz. "
   "Với cuộn N vòng, từ thông qua mỗi vòng đều đóng góp nên phải nhân với N.",
   "Định luật Faraday", D),

mc("Đơn vị của suất điện động cảm ứng là",
   ["ampe (A).", "vôn (V).", "oát (W).", "culông (C)."],
   "B",
   "Suất điện động là một đại lượng đặc trưng cho khả năng sinh công của nguồn điện, "
   "đo bằng vôn giống như hiệu điện thế.",
   "Đơn vị suất điện động", D),

mc("Mối liên hệ giữa giá trị hiệu dụng U và giá trị cực đại U₀ của điện áp xoay chiều là",
   ["U = U₀·√2.", "U = U₀/√2.", "U = 2U₀.", "U = U₀/2."],
   "B",
   "U = U₀/√2 ≈ 0,707·U₀. Mạng điện dân dụng 220 V là giá trị hiệu dụng, "
   "giá trị cực đại tương ứng khoảng 311 V.",
   "Giá trị hiệu dụng", D, fig="t_dt_u_i_hieudung", cap="Điện áp tức thời và giá trị hiệu dụng"),

mc("Máy biến áp chỉ hoạt động được với",
   ["dòng điện không đổi.", "dòng điện xoay chiều.",
    "cả hai loại dòng điện trên.", "dòng điện có cường độ rất lớn."],
   "B",
   "Máy biến áp hoạt động dựa trên hiện tượng cảm ứng điện từ, đòi hỏi từ thông qua cuộn thứ cấp "
   "phải biến thiên. Dòng không đổi tạo từ thông không đổi nên cuộn thứ cấp không có điện áp.",
   "Máy biến áp", D, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),
],
P2=[
ds("Một nam châm thẳng được đặt trên bàn. Xét từ trường do nam châm này sinh ra.",
   [("Đường sức từ ở gần hai cực của nam châm dày hơn ở giữa thân nam châm.", True,
     "Đúng. Từ trường mạnh nhất ở hai cực nên đường sức được vẽ dày nhất tại đó."),
    ("Bên ngoài nam châm, đường sức từ đi từ cực Nam sang cực Bắc.", False,
     "Sai. Bên ngoài nam châm, đường sức đi RA ở cực Bắc và đi VÀO cực Nam. "
     "Chiều từ Nam sang Bắc là chiều của đường sức TRONG LÒNG nam châm."),
    ("Đường sức từ là những đường cong khép kín.", True,
     "Đúng. Đây là điểm khác biệt cơ bản so với đường sức điện của điện tích điểm, "
     "vốn không khép kín."),
    ("Nếu bẻ đôi nam châm, ta sẽ thu được một mẩu chỉ có cực Bắc và một mẩu chỉ có cực Nam.", False,
     "Sai. Bẻ đôi nam châm ta được hai nam châm nhỏ, mỗi mẩu đều có đủ cả hai cực. "
     "Không tồn tại cực từ đơn lẻ.")],
   "Từ trường và đường sức từ", D),

ds("Một đoạn dây dẫn thẳng dài 10 cm mang dòng điện 2,0 A được đặt trong từ trường đều "
   "có cảm ứng từ B = 0,50 T.",
   [("Nếu dây vuông góc với đường sức từ thì lực từ tác dụng lên dây bằng 0,10 N.", True,
     "Đúng. F = B·I·ℓ = 0,50 · 2,0 · 0,10 = 0,10 N."),
    ("Nếu dây song song với đường sức từ thì lực từ bằng 0,10 N.", False,
     "Sai. Khi dây song song với đường sức thì α = 0° nên sinα = 0 và lực từ bằng 0."),
    ("Lực từ luôn vuông góc với đoạn dây dẫn.", True,
     "Đúng. Theo quy tắc bàn tay trái, lực từ vuông góc với cả đoạn dây lẫn vectơ cảm ứng từ."),
    ("Nếu đổi chiều dòng điện thì lực từ đổi chiều.", True,
     "Đúng. Trong quy tắc bàn tay trái, đảo chiều dòng điện thì ngón cái quay ngược lại, "
     "nên lực từ đổi chiều.")],
   "Lực từ – tính toán và nhận định", D),

ds("Một khung dây phẳng hình vuông cạnh 20 cm được đặt trong từ trường đều B = 0,10 T.",
   [("Diện tích khung dây bằng 0,04 m².", True,
     "Đúng. S = 0,20 · 0,20 = 0,04 m²."),
    ("Khi mặt phẳng khung vuông góc với đường sức từ, từ thông qua khung bằng 4,0·10⁻³ Wb.", True,
     "Đúng. Lúc đó pháp tuyến song song với B, θ = 0°, nên Φ = B·S = 0,10 · 0,04 = 4,0·10⁻³ Wb."),
    ("Khi mặt phẳng khung song song với đường sức từ, từ thông qua khung đạt giá trị lớn nhất.", False,
     "Sai. Khi mặt phẳng khung song song với B thì pháp tuyến vuông góc với B, θ = 90°, "
     "nên từ thông bằng 0 — đó là giá trị NHỎ NHẤT về độ lớn."),
    ("Từ thông là một đại lượng vô hướng, có thể nhận giá trị âm.", True,
     "Đúng. Từ thông là đại lượng đại số; dấu của nó phụ thuộc cách chọn chiều pháp tuyến.")],
   "Từ thông qua khung dây", D),

ds("Mạng điện dân dụng ở Việt Nam có điện áp 220 V và tần số 50 Hz.",
   [("Chu kì của dòng điện trong mạng là 0,02 s.", True,
     "Đúng. T = 1/f = 1/50 = 0,02 s."),
    ("Giá trị 220 V là giá trị cực đại của điện áp.", False,
     "Sai. Con số ghi trên thiết bị và số chỉ của vôn kế đều là GIÁ TRỊ HIỆU DỤNG. "
     "Giá trị cực đại là 220·√2 ≈ 311 V."),
    ("Trong mỗi giây, dòng điện đổi chiều 100 lần.", True,
     "Đúng. Mỗi chu kì dòng điện đổi chiều 2 lần; 50 chu kì trong một giây cho 100 lần đổi chiều."),
    ("Ampe kế xoay chiều mắc trong mạch chỉ giá trị hiệu dụng của cường độ dòng điện.", True,
     "Đúng. Mọi đồng hồ đo xoay chiều thông dụng đều được khắc độ theo giá trị hiệu dụng.")],
   "Dòng điện xoay chiều – đại cương", D),
],
P3=[
sa("Một đoạn dây dẫn dài 25 cm mang dòng điện 4,0 A đặt vuông góc với các đường sức của từ trường "
   "đều có B = 0,20 T. Lực từ tác dụng lên đoạn dây bằng bao nhiêu niutơn?",
   "0,2",
   "Dây vuông góc với đường sức nên α = 90°, sinα = 1.\n"
   "F = B·I·ℓ = 0,20 · 4,0 · 0,25 = 0,20 N.",
   "Tính lực từ", D),

sa("Một khung dây phẳng có diện tích 50 cm² đặt vuông góc với các đường sức của từ trường đều "
   "B = 0,40 T. Từ thông qua khung bằng bao nhiêu vêbe?",
   "0,002",
   "Đổi đơn vị: S = 50 cm² = 50·10⁻⁴ m² = 5,0·10⁻³ m².\n"
   "Khung vuông góc với đường sức ⇒ pháp tuyến song song B ⇒ θ = 0°.\n"
   "Φ = B·S = 0,40 · 5,0·10⁻³ = 2,0·10⁻³ Wb = 0,002 Wb.",
   "Tính từ thông", D),

sa("Từ thông qua một vòng dây kín biến thiên đều từ 0,060 Wb xuống 0,020 Wb trong thời gian 0,20 s. "
   "Độ lớn suất điện động cảm ứng trong vòng dây bằng bao nhiêu vôn?",
   "0,2",
   "|ΔΦ| = |0,020 − 0,060| = 0,040 Wb.\n"
   "|e| = |ΔΦ|/Δt = 0,040/0,20 = 0,20 V.",
   "Định luật Faraday", D),

sa("Một điện áp xoay chiều có giá trị hiệu dụng 110 V. Giá trị cực đại của điện áp này bằng bao nhiêu "
   "vôn (làm tròn đến hàng đơn vị)? Lấy √2 ≈ 1,414.",
   "156",
   "U₀ = U·√2 = 110 · 1,414 ≈ 155,5 ≈ 156 V.",
   "Giá trị hiệu dụng", D),

sa("Một dòng điện xoay chiều có tần số 60 Hz. Chu kì của dòng điện đó bằng bao nhiêu giây "
   "(làm tròn đến chữ số thập phân thứ tư)?",
   "0,0167",
   "T = 1/f = 1/60 ≈ 0,01667 s ≈ 0,0167 s.",
   "Chu kì và tần số", D),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng và cuộn thứ cấp 250 vòng. "
   "Đặt vào hai đầu cuộn sơ cấp điện áp xoay chiều 220 V thì điện áp hiệu dụng ở hai đầu cuộn "
   "thứ cấp bằng bao nhiêu vôn?",
   "55",
   "Máy biến áp lí tưởng: U₂/U₁ = N₂/N₁.\n"
   "U₂ = U₁·N₂/N₁ = 220 · 250/1000 = 220 · 0,25 = 55 V.",
   "Máy biến áp", D),
])


# =====================================================================  ĐỀ 2
DE2 = dict(
ma="12C3-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Củng cố khái niệm cơ bản, bắt đầu vận dụng công thức một bước",
P1=[
mc("Trong lòng một ống dây dài có dòng điện chạy qua, từ trường",
   ["bằng không.",
    "gần như đều, các đường sức song song và cách đều nhau.",
    "có đường sức là những đường tròn đồng tâm.",
    "mạnh nhất ở sát thành ống."],
   "B",
   "Với ống dây đủ dài, từ trường trong lòng ống gần như đều: đường sức là những đường thẳng "
   "song song, cách đều. Đường tròn đồng tâm là đặc điểm của từ trường quanh dây dẫn thẳng.",
   "Từ trường của ống dây", D, fig="t_sd_ongday", cap="Ống dây có dòng điện"),

mc("Một ống dây có dòng điện chạy qua hoạt động tương đương với",
   ["một điện tích điểm.", "một nam châm thẳng.",
    "một tụ điện.", "một điện trở thuần."],
   "B",
   "Ống dây có dòng điện có hai đầu đóng vai trò như hai cực từ, đường sức bên ngoài giống hệt "
   "nam châm thẳng. Đó chính là nguyên lí của nam châm điện.",
   "Nam châm điện", D),

mc("Kim la bàn luôn chỉ hướng Bắc địa lí vì",
   ["Trái Đất quay quanh trục của nó.",
    "gần cực Bắc địa lí có cực Nam từ của Trái Đất.",
    "gần cực Bắc địa lí có cực Bắc từ của Trái Đất.",
    "lực hấp dẫn kéo kim về phía Bắc."],
   "B",
   "Đầu Bắc của kim la bàn bị hút bởi cực NAM từ. Cực Nam từ của Trái Đất nằm gần cực Bắc địa lí, "
   "nên kim la bàn chỉ về phương Bắc địa lí.",
   "Từ trường Trái Đất", D, fig="t_sd_tutruong_traidat", cap="Từ trường của Trái Đất"),

mc("Cảm ứng từ tại một điểm trong từ trường là đại lượng",
   ["vô hướng, luôn dương.", "vectơ, có phương trùng trục kim nam châm thử nằm cân bằng.",
    "vô hướng, có thể âm.", "vectơ, luôn hướng thẳng đứng xuống dưới."],
   "B",
   "Vectơ cảm ứng từ có phương trùng với trục của kim nam châm thử nằm cân bằng tại điểm đó, "
   "chiều từ cực Nam sang cực Bắc của kim.",
   "Vectơ cảm ứng từ", D),

mc("Một đoạn dây dẫn mang dòng điện đặt trong từ trường đều. Khi tăng cường độ dòng điện lên "
   "gấp đôi và giữ nguyên các yếu tố khác thì lực từ tác dụng lên dây",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "F = B·I·ℓ·sinα tỉ lệ thuận bậc nhất với I, nên I tăng gấp đôi thì F tăng gấp đôi.",
   "Phụ thuộc của lực từ", D),

mc("Đặt một đoạn dây dẫn mang dòng điện hợp với đường sức từ góc 30°. So với khi dây đặt vuông góc "
   "với đường sức, lực từ lúc này",
   ["lớn gấp đôi.", "bằng một nửa.", "bằng nhau.", "bằng 0."],
   "B",
   "F tỉ lệ với sinα. sin30° = 0,5 còn sin90° = 1, nên lực từ chỉ bằng một nửa giá trị lớn nhất.",
   "Vai trò của góc α", D),

mc("Một khung dây kín chuyển động thẳng đều và nằm hoàn toàn bên trong một vùng từ trường đều. "
   "Trong khung",
   ["có dòng điện cảm ứng vì khung đang chuyển động.",
    "không có dòng điện cảm ứng vì từ thông không đổi.",
    "có dòng điện cảm ứng không đổi theo thời gian.",
    "có dòng điện cảm ứng chỉ khi khung chuyển động nhanh."],
   "B",
   "Từ trường đều nên B như nhau ở mọi điểm; khung nằm trọn bên trong nên S và góc đều không đổi. "
   "Từ thông không đổi ⇒ không có dòng cảm ứng. Dòng chỉ xuất hiện lúc khung đi vào hoặc đi ra "
   "khỏi vùng từ trường.",
   "Điều kiện có dòng cảm ứng", D, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường đều"),

mc("Đưa một nam châm lại gần một vòng dây kín thì trong vòng dây xuất hiện dòng điện cảm ứng. "
   "Nếu giữ nam châm đứng yên sát vòng dây thì",
   ["dòng cảm ứng vẫn giữ nguyên độ lớn.",
    "không còn dòng cảm ứng.",
    "dòng cảm ứng tăng lên vì khoảng cách nhỏ.",
    "dòng cảm ứng đổi chiều."],
   "B",
   "Khi nam châm đứng yên, từ thông qua vòng dây không còn biến thiên nên dòng cảm ứng biến mất, "
   "dù từ trường tại vị trí vòng dây vẫn rất mạnh.",
   "Điều kiện có dòng cảm ứng", D, fig="t_sd_tn_faraday", cap="Thí nghiệm Faraday"),

mc("Khi một nam châm rơi xuống gần một vòng dây kín đặt nằm ngang bên dưới, lực từ do dòng cảm ứng "
   "tác dụng lên nam châm có chiều",
   ["hướng xuống, làm nam châm rơi nhanh hơn.",
    "hướng lên, cản trở chuyển động của nam châm.",
    "nằm ngang.", "bằng không."],
   "B",
   "Theo định luật Lenz, dòng cảm ứng chống lại nguyên nhân sinh ra nó, tức chống lại sự lại gần "
   "của nam châm. Vì vậy lực từ hướng lên, làm nam châm rơi chậm hơn so với rơi tự do.",
   "Định luật Lenz – ứng dụng", D, fig="t_sd_nam_cham_roi",
   cap="Nam châm rơi gần vòng dây kín"),

mc("Đại lượng nào sau đây KHÔNG phụ thuộc vào cách chọn chiều pháp tuyến của khung dây?",
   ["Dấu của từ thông.", "Độ lớn của suất điện động cảm ứng.",
    "Dấu của suất điện động cảm ứng.", "Chiều dương quy ước của dòng điện trong khung."],
   "B",
   "Đổi chiều pháp tuyến thì dấu của Φ và dấu của e đều đổi, chiều dương quy ước cũng đổi theo. "
   "Chỉ ĐỘ LỚN của suất điện động là không phụ thuộc cách chọn.",
   "Quy ước dấu trong cảm ứng điện từ", TB),

mc("Máy phát điện xoay chiều hoạt động dựa trên",
   ["tác dụng nhiệt của dòng điện.", "hiện tượng cảm ứng điện từ.",
    "hiện tượng nhiễm điện do cọ xát.", "tác dụng hoá học của dòng điện."],
   "B",
   "Khung dây quay đều trong từ trường làm từ thông qua khung biến thiên điều hoà, "
   "theo định luật Faraday sẽ xuất hiện suất điện động cảm ứng biến thiên điều hoà.",
   "Máy phát điện xoay chiều", D, fig="t_sd_may_phat", cap="Nguyên lí máy phát điện xoay chiều"),

mc("Trong máy phát điện xoay chiều một pha, bộ phận nào giúp đưa dòng điện từ khung dây đang quay "
   "ra mạch ngoài?",
   ["Lõi thép kín.", "Vành khuyên và chổi quét.",
    "Cuộn thứ cấp.", "Bộ chỉnh lưu."],
   "B",
   "Vành khuyên gắn với khung dây và quay theo khung; chổi quét tì lên vành khuyên và nối với "
   "mạch ngoài đứng yên, nhờ đó dòng điện được đưa ra ngoài.",
   "Cấu tạo máy phát điện", D, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

mc("Dòng điện xoay chiều có cường độ tức thời i = 5,0·cos(100πt) (A). Giá trị cực đại của cường độ "
   "dòng điện là",
   ["5,0 A.", "100π A.", "khoảng 3,54 A.", "khoảng 7,07 A."],
   "A",
   "So sánh với dạng tổng quát i = I₀·cos(ωt + φ), ta có I₀ = 5,0 A. "
   "Giá trị 3,54 A là giá trị HIỆU DỤNG (5,0/√2), không phải cực đại.",
   "Đọc biểu thức dòng xoay chiều", D),

mc("Một dòng điện xoay chiều có biểu thức i = 2,0·cos(100πt) (A). Tần số của dòng điện này là",
   ["100 Hz.", "50 Hz.", "100π Hz.", "25 Hz."],
   "B",
   "ω = 100π rad/s ⇒ f = ω/(2π) = 100π/(2π) = 50 Hz.",
   "Tần số của dòng xoay chiều", D),

mc("Trong máy biến áp lí tưởng, nếu số vòng cuộn thứ cấp lớn hơn số vòng cuộn sơ cấp thì",
   ["điện áp giảm và cường độ dòng điện giảm.",
    "điện áp tăng và cường độ dòng điện giảm.",
    "điện áp tăng và cường độ dòng điện tăng.",
    "cả điện áp và cường độ dòng điện đều không đổi."],
   "B",
   "N₂ > N₁ nên U₂ > U₁: máy tăng áp. Với máy lí tưởng, công suất được bảo toàn nên "
   "U₁I₁ = U₂I₂, điện áp tăng kéo theo cường độ dòng điện giảm.",
   "Máy biến áp", D, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Người ta truyền tải điện năng đi xa ở điện áp cao nhằm mục đích",
   ["làm tăng công suất của nhà máy điện.",
    "giảm hao phí do toả nhiệt trên đường dây.",
    "giảm chiều dài đường dây.",
    "tăng cường độ dòng điện trên đường dây."],
   "B",
   "Công suất hao phí trên đường dây bằng R·I² với I = P/U, nên hao phí tỉ lệ nghịch với bình "
   "phương điện áp truyền tải. Tăng U làm I giảm, do đó hao phí giảm rất nhanh.",
   "Truyền tải điện năng", D, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

mc("Bếp từ làm nóng nồi dựa trên",
   ["bức xạ nhiệt từ mặt kính.",
    "dòng điện Foucault sinh ra trong đáy nồi.",
    "sự dẫn nhiệt từ cuộn dây sang nồi.",
    "hiện tượng đối lưu trong không khí."],
   "B",
   "Cuộn dây cao tần tạo từ trường biến thiên nhanh, làm xuất hiện dòng điện xoáy (Foucault) "
   "trong đáy nồi nhiễm từ. Dòng xoáy toả nhiệt ngay trong đáy nồi.",
   "Ứng dụng dòng Foucault", D, fig="t_sd_bep_tu", cap="Nguyên lí bếp từ"),

mc("Lõi của máy biến áp được ghép từ nhiều lá thép mỏng cách điện với nhau nhằm",
   ["tăng độ bền cơ học của lõi.",
    "hạn chế dòng điện Foucault, giảm hao phí toả nhiệt trong lõi.",
    "tăng số vòng dây quấn được.",
    "giúp máy hoạt động được với dòng điện không đổi."],
   "B",
   "Từ thông biến thiên sinh ra dòng xoáy trong khối lõi làm lõi nóng lên. Ghép nhiều lá mỏng "
   "cách điện sẽ cắt nhỏ đường đi của dòng xoáy, giảm mạnh hao phí.",
   "Dòng Foucault – tác hại", D, fig="t_sd_dong_fuco", cap="Dòng điện Foucault"),
],
P2=[
ds("Một ống dây thẳng dài có dòng điện không đổi chạy qua.",
   [("Từ trường trong lòng ống dây gần như đều.", True,
     "Đúng. Với ống dây đủ dài, các đường sức trong lòng ống song song và cách đều nhau."),
    ("Hai đầu ống dây đóng vai trò như hai cực của một nam châm thẳng.", True,
     "Đúng. Bên ngoài ống dây, đường sức có dạng giống hệt đường sức của nam châm thẳng."),
    ("Nếu đảo chiều dòng điện trong ống dây thì hai cực từ đổi chỗ cho nhau.", True,
     "Đúng. Theo quy tắc nắm tay phải, đổi chiều dòng điện làm chiều từ trường trong lòng ống "
     "đảo lại, nên hai cực đổi chỗ."),
    ("Ngắt dòng điện thì ống dây vẫn giữ nguyên từ tính như một nam châm vĩnh cửu.", False,
     "Sai. Ống dây không lõi mất từ tính ngay khi ngắt dòng. Đây chính là ưu điểm của nam châm "
     "điện so với nam châm vĩnh cửu: có thể bật tắt được.")],
   "Từ trường của ống dây", D),

ds("Một khung dây kín được kéo với tốc độ không đổi đi vào rồi đi hết qua một vùng từ trường đều "
   "có bề rộng lớn hơn cạnh khung.",
   [("Trong giai đoạn khung đang đi vào vùng từ trường, có dòng điện cảm ứng trong khung.", True,
     "Đúng. Diện tích phần khung nằm trong từ trường tăng dần nên từ thông tăng, sinh ra dòng cảm ứng."),
    ("Khi khung nằm trọn trong vùng từ trường, dòng điện cảm ứng đạt giá trị lớn nhất.", False,
     "Sai. Lúc đó từ thông qua khung không đổi nên KHÔNG có dòng cảm ứng."),
    ("Trong giai đoạn khung đang đi ra khỏi vùng từ trường, lại có dòng điện cảm ứng.", True,
     "Đúng. Từ thông giảm dần nên dòng cảm ứng xuất hiện trở lại."),
    ("Dòng cảm ứng lúc khung đi vào và lúc khung đi ra có chiều ngược nhau.", True,
     "Đúng. Lúc đi vào từ thông tăng, lúc đi ra từ thông giảm, nên theo định luật Lenz "
     "hai dòng cảm ứng có chiều ngược nhau.")],
   "Khung dây đi qua vùng từ trường", TB,
   fig="t_sd_khung_vao_B", cap="Khung dây đi vào vùng từ trường đều"),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 500 vòng, cuộn thứ cấp 2000 vòng. "
   "Đặt vào cuộn sơ cấp điện áp xoay chiều 110 V.",
   [("Đây là máy tăng áp.", True,
     "Đúng. N₂ = 2000 > N₁ = 500 nên điện áp ở thứ cấp lớn hơn ở sơ cấp."),
    ("Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng 440 V.", True,
     "Đúng. U₂ = U₁·N₂/N₁ = 110 · 2000/500 = 110 · 4 = 440 V."),
    ("Cường độ dòng điện hiệu dụng ở cuộn thứ cấp lớn gấp 4 lần ở cuộn sơ cấp.", False,
     "Sai. Máy lí tưởng bảo toàn công suất nên I₁/I₂ = N₂/N₁ = 4, tức dòng ở thứ cấp NHỎ hơn "
     "4 lần chứ không lớn hơn."),
    ("Nếu thay nguồn xoay chiều bằng nguồn một chiều 110 V thì điện áp ở cuộn thứ cấp bằng 0.", True,
     "Đúng. Dòng một chiều ổn định tạo từ thông không đổi, không có suất điện động cảm ứng "
     "ở cuộn thứ cấp.")],
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

ds("Một dòng điện xoay chiều có biểu thức i = 4,0·cos(120πt) (A), với t tính bằng giây.",
   [("Cường độ dòng điện cực đại là 4,0 A.", True,
     "Đúng. Theo dạng i = I₀cos(ωt + φ) ta có I₀ = 4,0 A."),
    ("Tần số của dòng điện là 60 Hz.", True,
     "Đúng. f = ω/(2π) = 120π/(2π) = 60 Hz."),
    ("Cường độ dòng điện hiệu dụng xấp xỉ 2,83 A.", True,
     "Đúng. I = I₀/√2 = 4,0/1,414 ≈ 2,83 A."),
    ("Chu kì của dòng điện là 0,02 s.", False,
     "Sai. T = 1/f = 1/60 ≈ 0,0167 s. Giá trị 0,02 s ứng với tần số 50 Hz.")],
   "Đọc biểu thức dòng xoay chiều", TB),
],
P3=[
sa("Một đoạn dây dẫn dài 40 cm mang dòng điện 3,0 A đặt trong từ trường đều B = 0,25 T sao cho dây "
   "hợp với đường sức từ góc 30°. Lực từ tác dụng lên đoạn dây bằng bao nhiêu niutơn?",
   "0,15",
   "F = B·I·ℓ·sinα = 0,25 · 3,0 · 0,40 · sin30° = 0,25 · 3,0 · 0,40 · 0,50 = 0,15 N.",
   "Lực từ có góc α", D),

sa("Một khung dây phẳng diện tích 200 cm² đặt trong từ trường đều B = 0,050 T sao cho vectơ pháp "
   "tuyến của khung hợp với đường sức từ góc 60°. Từ thông qua khung bằng bao nhiêu vêbe "
   "(viết dưới dạng x·10⁻⁴, chỉ ghi giá trị x)?",
   "5",
   "S = 200 cm² = 200·10⁻⁴ m² = 2,0·10⁻² m².\n"
   "Φ = B·S·cosθ = 0,050 · 2,0·10⁻² · cos60° = 0,050 · 2,0·10⁻² · 0,50 = 5,0·10⁻⁴ Wb.\n"
   "Vậy x = 5.",
   "Tính từ thông có góc", TB),

sa("Một cuộn dây gồm 100 vòng. Từ thông qua mỗi vòng biến thiên đều từ 0 lên 0,020 Wb trong "
   "thời gian 0,50 s. Độ lớn suất điện động cảm ứng trong cuộn dây bằng bao nhiêu vôn?",
   "4",
   "|e| = N·|ΔΦ|/Δt = 100 · 0,020 / 0,50 = 100 · 0,040 = 4,0 V.\n"
   "Lưu ý phải nhân với số vòng dây N.",
   "Định luật Faraday có N vòng", D),

sa("Một khung dây dẫn phẳng gồm 250 vòng, diện tích mỗi vòng 60 cm², quay đều quanh một trục vuông "
   "góc với từ trường đều B = 0,20 T với tần số 50 Hz. Suất điện động cực đại của khung bằng bao "
   "nhiêu vôn (làm tròn đến chữ số thập phân thứ nhất)? Lấy π ≈ 3,1416.",
   "94,2",
   "ω = 2πf = 2 · 3,1416 · 50 ≈ 314,16 rad/s.\n"
   "S = 60 cm² = 6,0·10⁻³ m².\n"
   "E₀ = ω·N·B·S = 314,16 · 250 · 0,20 · 6,0·10⁻³ = 314,16 · 0,30 ≈ 94,2 V.",
   "Suất điện động cực đại", TB),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 800 vòng đặt dưới điện áp xoay chiều 220 V. "
   "Muốn thu được điện áp 12 V ở cuộn thứ cấp thì cuộn thứ cấp phải quấn bao nhiêu vòng "
   "(làm tròn đến hàng đơn vị)?",
   "44",
   "N₂ = N₁·U₂/U₁ = 800 · 12/220 = 9600/220 ≈ 43,6 ≈ 44 vòng.",
   "Máy biến áp – bài toán ngược", TB),

sa("Truyền một công suất điện 50 kW đi xa bằng đường dây có điện trở tổng cộng 5,0 Ω ở điện áp "
   "hiệu dụng 5,0 kV. Coi hệ số công suất bằng 1. Công suất hao phí trên đường dây bằng bao nhiêu "
   "oát?",
   "500",
   "Cường độ dòng điện trên đường dây: I = P/U = 50 000/5000 = 10 A.\n"
   "Công suất hao phí: ΔP = R·I² = 5,0 · 10² = 500 W.",
   "Hao phí truyền tải", TB),
])


# =====================================================================  ĐỀ 3
DE3 = dict(
ma="12C3-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Đọc đồ thị từ thông, thanh dẫn chuyển động, cân bằng lực từ",
P1=[
mc("Một dây dẫn thẳng dài mang dòng điện I. Khi tăng khoảng cách từ điểm khảo sát tới dây lên "
   "gấp đôi thì cảm ứng từ tại đó",
   ["tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn.", "không đổi."],
   "B",
   "Cảm ứng từ do dòng điện thẳng dài gây ra tỉ lệ nghịch với khoảng cách r. "
   "r tăng gấp đôi thì B giảm một nửa.",
   "Từ trường dòng điện thẳng", TB, fig="t_sd_duongsuc_daythang",
   cap="Đường sức từ của dòng điện thẳng"),

mc("Đặt một khung dây phẳng trong từ trường đều sao cho MẶT PHẲNG khung hợp với đường sức từ "
   "góc 30°. Góc giữa vectơ pháp tuyến của khung và vectơ cảm ứng từ bằng",
   ["30°.", "60°.", "90°.", "120°."],
   "B",
   "Pháp tuyến vuông góc với mặt phẳng khung, nên góc giữa pháp tuyến và B bằng 90° − 30° = 60°. "
   "Nhầm lẫn giữa hai góc này là lỗi rất phổ biến khi tính từ thông.",
   "Phân biệt hai loại góc", TB, fig="t_sd_khung_nghieng",
   cap="Khung dây hợp góc với đường sức từ"),

mc("Một thanh dẫn dài ℓ chuyển động đều với tốc độ v theo phương vuông góc với chính nó và vuông "
   "góc với các đường sức của từ trường đều B. Suất điện động cảm ứng giữa hai đầu thanh bằng",
   ["B·ℓ/v.", "B·ℓ·v.", "B·v/ℓ.", "ℓ·v/B."],
   "B",
   "Trong thời gian Δt, thanh quét được diện tích ΔS = ℓ·v·Δt nên ΔΦ = B·ℓ·v·Δt. "
   "Suy ra |e| = ΔΦ/Δt = B·ℓ·v.",
   "Suất điện động của thanh dẫn", TB, fig="t_sd_ray_ngang",
   cap="Thanh dẫn trượt trên hai ray"),

mc("Trong máy phát điện xoay chiều, khi tăng tốc độ quay của khung dây lên gấp đôi thì suất điện "
   "động cực đại",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "E₀ = ω·N·B·S tỉ lệ thuận bậc nhất với ω. Tốc độ quay tăng gấp đôi thì ω tăng gấp đôi "
   "nên E₀ cũng tăng gấp đôi (đồng thời tần số cũng tăng gấp đôi).",
   "Máy phát điện xoay chiều", TB),

mc("Từ thông qua một vòng dây kín biến thiên theo đồ thị. Trong giai đoạn nào sau đây KHÔNG có "
   "dòng điện cảm ứng trong vòng dây?",
   ["Giai đoạn (I).", "Giai đoạn (II).", "Giai đoạn (III).", "Giai đoạn (IV)."],
   "B",
   "Giai đoạn (II) đồ thị nằm ngang: từ thông giữ nguyên giá trị 0,4 Wb nên ΔΦ = 0, "
   "không có suất điện động cảm ứng. Ba giai đoạn còn lại đồ thị đều có độ dốc khác không.",
   "Đọc đồ thị từ thông", TB, fig="t_dt_phi_t", cap="Từ thông qua vòng dây theo thời gian"),

mc("Vẫn với đồ thị từ thông ở câu trên, giai đoạn nào có suất điện động cảm ứng lớn nhất về độ lớn?",
   ["Giai đoạn (I).", "Giai đoạn (II).", "Giai đoạn (III).", "Giai đoạn (IV)."],
   "C",
   "Suất điện động tỉ lệ với độ dốc của đồ thị. Giai đoạn (III) từ thông giảm từ 0,4 Wb xuống 0 "
   "chỉ trong 1 s nên độ dốc có độ lớn 0,4 Wb/s — lớn hơn 0,2 Wb/s của hai giai đoạn (I) và (IV).",
   "Đọc đồ thị từ thông", TB, fig="t_dt_phi_t", cap="Từ thông qua vòng dây theo thời gian"),

mc("Một thanh dẫn nằm ngang trên hai ray, đặt trong từ trường đều thẳng đứng. Khi cho dòng điện "
   "chạy qua thanh thì lực từ tác dụng lên thanh có phương",
   ["thẳng đứng hướng lên.", "nằm ngang, vuông góc với thanh.",
    "nằm ngang, dọc theo thanh.", "thẳng đứng hướng xuống."],
   "B",
   "Lực từ vuông góc với cả dòng điện (dọc thanh, nằm ngang) lẫn cảm ứng từ (thẳng đứng), "
   "nên nó nằm ngang và vuông góc với thanh — đúng hướng làm thanh trượt trên ray.",
   "Phương của lực từ", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray nằm ngang"),

mc("Một đoạn dây dẫn nằm ngang mang dòng điện được đặt giữa hai cực của nam châm, phía trên một "
   "cái cân. Khi đóng mạch điện, số chỉ của cân thay đổi. Điều đó chứng tỏ",
   ["dòng điện làm nam châm nóng lên.",
    "lực từ tác dụng lên đoạn dây có thành phần thẳng đứng.",
    "khối lượng của đoạn dây thay đổi.",
    "cân bị nhiễm từ."],
   "B",
   "Theo định luật III Niu-tơn, đoạn dây chịu lực từ hướng lên hoặc xuống thì nam châm chịu phản "
   "lực ngược lại, làm áp lực lên cân thay đổi. Khối lượng vật không hề thay đổi.",
   "Cân dòng điện", TB, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

mc("Hiện tượng nào sau đây KHÔNG phải ứng dụng của hiện tượng cảm ứng điện từ?",
   ["Máy biến áp.", "Bếp từ.", "Sạc không dây.", "Bóng đèn dây tóc."],
   "D",
   "Bóng đèn dây tóc hoạt động nhờ tác dụng nhiệt của dòng điện (hiệu ứng Jun – Len-xơ), "
   "không liên quan tới cảm ứng điện từ. Ba thiết bị còn lại đều dựa trên từ thông biến thiên.",
   "Ứng dụng cảm ứng điện từ", D),

mc("Trong công thức tính công suất hao phí trên đường dây tải điện, khi tăng điện áp truyền tải "
   "lên 5 lần và giữ nguyên công suất truyền đi thì hao phí",
   ["giảm 5 lần.", "giảm 25 lần.", "tăng 5 lần.", "tăng 25 lần."],
   "B",
   "ΔP = R·I² với I = P/U nên ΔP tỉ lệ nghịch với U². U tăng 5 lần thì ΔP giảm 5² = 25 lần.",
   "Hao phí truyền tải", TB, fig="t_sd_truyen_tai", cap="Truyền tải điện năng đi xa"),

mc("Một vòng dây kín đặt trong từ trường đều. Từ thông qua vòng dây tăng dần. "
   "Dòng điện cảm ứng trong vòng dây sinh ra từ trường",
   ["cùng chiều với từ trường ban đầu.",
    "ngược chiều với từ trường ban đầu.",
    "vuông góc với từ trường ban đầu.",
    "bằng không."],
   "B",
   "Từ thông tăng nên theo định luật Lenz, dòng cảm ứng phải chống lại sự tăng đó bằng cách "
   "sinh ra từ trường ngược chiều với từ trường ban đầu.",
   "Định luật Lenz", TB, fig="t_sd_lenz", cap="Hai trường hợp của định luật Lenz"),

mc("Một máy biến áp có số vòng cuộn sơ cấp gấp 10 lần cuộn thứ cấp. Đây là máy",
   ["tăng áp, điện áp ra lớn gấp 10 lần.", "hạ áp, điện áp ra nhỏ hơn 10 lần.",
    "tăng áp, điện áp ra nhỏ hơn 10 lần.", "hạ áp, điện áp ra lớn gấp 10 lần."],
   "B",
   "N₁ = 10·N₂ nên U₂ = U₁·N₂/N₁ = U₁/10: điện áp giảm 10 lần, đây là máy hạ áp.",
   "Máy biến áp", D),

mc("Phanh điện từ trên xe tải hạng nặng hoạt động dựa trên",
   ["lực ma sát giữa má phanh và đĩa phanh.",
    "lực từ do dòng Foucault sinh ra trong đĩa kim loại quay.",
    "lực hấp dẫn giữa đĩa và nam châm.",
    "lực đẩy Ác-si-mét trong dầu phanh."],
   "B",
   "Nam châm điện tạo từ trường xuyên qua đĩa kim loại đang quay, sinh dòng Foucault trong đĩa. "
   "Theo định luật Lenz, lực từ tác dụng lên dòng này luôn cản trở chuyển động của đĩa.",
   "Dòng Foucault – ứng dụng", TB, fig="t_sd_dong_fuco", cap="Dòng điện Foucault"),

mc("Một khung dây quay đều trong từ trường đều quanh trục vuông góc với đường sức. "
   "Suất điện động cảm ứng đạt giá trị cực đại khi",
   ["mặt phẳng khung vuông góc với đường sức từ.",
    "mặt phẳng khung song song với đường sức từ.",
    "từ thông qua khung đạt cực đại.",
    "khung dừng lại."],
   "B",
   "Từ thông Φ = NBS·cos(ωt) còn e = ωNBS·sin(ωt): hai đại lượng lệch pha nhau 90°. "
   "Khi mặt phẳng khung song song với đường sức thì Φ = 0 và chính lúc đó e đạt cực đại.",
   "Máy phát điện – pha", TB, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

mc("Sạc không dây cho điện thoại truyền năng lượng từ đế sạc sang máy nhờ",
   ["dòng điện chạy qua không khí.", "từ trường biến thiên giữa hai cuộn dây.",
    "sóng âm tần số cao.", "tia hồng ngoại."],
   "B",
   "Cuộn sơ cấp trong đế sạc mang dòng xoay chiều tạo từ trường biến thiên. Từ thông qua cuộn thứ "
   "cấp trong điện thoại biến thiên, sinh suất điện động cảm ứng nạp cho pin — cùng nguyên lí "
   "với máy biến áp.",
   "Sạc không dây", D, fig="t_sd_sac_khong_day", cap="Nguyên lí sạc không dây"),

mc("Một dòng điện xoay chiều có cường độ hiệu dụng 3,0 A. Cường độ cực đại của dòng điện này "
   "xấp xỉ bằng",
   ["2,12 A.", "4,24 A.", "3,00 A.", "6,00 A."],
   "B",
   "I₀ = I·√2 = 3,0 · 1,414 ≈ 4,24 A. Giá trị 2,12 A ứng với việc chia cho √2 thay vì nhân.",
   "Giá trị hiệu dụng", D),

mc("Nhiệt lượng toả ra trên một điện trở R khi có dòng điện xoay chiều chạy qua trong thời gian t "
   "được tính bằng",
   ["Q = R·I₀²·t với I₀ là cường độ cực đại.",
    "Q = R·I²·t với I là cường độ hiệu dụng.",
    "Q = R·I₀·t.", "Q = R·I·t."],
   "B",
   "Giá trị hiệu dụng được định nghĩa đúng từ tác dụng nhiệt: dòng xoay chiều có cường độ hiệu dụng "
   "I toả nhiệt bằng dòng không đổi cường độ I. Dùng I₀ sẽ cho kết quả lớn gấp đôi giá trị thật.",
   "Ý nghĩa của giá trị hiệu dụng", TB),

mc("Khi mắc một bóng đèn vào mạng điện xoay chiều 220 V – 50 Hz, trong mỗi giây dòng điện qua đèn "
   "có cường độ bằng không",
   ["25 lần.", "50 lần.", "100 lần.", "200 lần."],
   "C",
   "Trong mỗi chu kì, cường độ dòng điện đi qua giá trị 0 đúng hai lần. Với 50 chu kì mỗi giây, "
   "ta có 100 lần. Mắt người không nhận ra vì hiện tượng lưu ảnh trên võng mạc.",
   "Dòng xoay chiều – tần số", TB),
],
P2=[
ds("Cho đồ thị biểu diễn từ thông qua một vòng dây dẫn kín có điện trở 0,10 Ω theo thời gian.",
   [("Trong giai đoạn (I), suất điện động cảm ứng có độ lớn 0,20 V.", True,
     "Đúng. Từ thông tăng từ 0 lên 0,40 Wb trong 2 s: |e| = 0,40/2 = 0,20 V."),
    ("Trong giai đoạn (II), cường độ dòng điện cảm ứng bằng 4,0 A.", False,
     "Sai. Giai đoạn (II) từ thông không đổi nên suất điện động bằng 0, do đó dòng điện cảm ứng "
     "cũng bằng 0."),
    ("Trong giai đoạn (III), cường độ dòng điện cảm ứng có độ lớn 4,0 A.", True,
     "Đúng. |e| = 0,40/1 = 0,40 V nên i = |e|/R = 0,40/0,10 = 4,0 A."),
    ("Dòng điện cảm ứng trong giai đoạn (I) và giai đoạn (III) có chiều ngược nhau.", True,
     "Đúng. Giai đoạn (I) từ thông tăng, giai đoạn (III) từ thông giảm, nên theo định luật Lenz "
     "hai dòng cảm ứng ngược chiều nhau.")],
   "Đọc đồ thị từ thông – tính dòng cảm ứng", TB,
   fig="t_dt_phi_t", cap="Từ thông qua vòng dây theo thời gian"),

ds("Một thanh dẫn dài 50 cm trượt đều với tốc độ 4,0 m/s trên hai ray nằm ngang, vuông góc với "
   "từ trường đều B = 0,30 T hướng thẳng đứng. Điện trở toàn mạch là 0,60 Ω.",
   [("Suất điện động cảm ứng trong mạch bằng 0,60 V.", True,
     "Đúng. e = B·ℓ·v = 0,30 · 0,50 · 4,0 = 0,60 V."),
    ("Cường độ dòng điện trong mạch bằng 1,0 A.", True,
     "Đúng. i = e/R = 0,60/0,60 = 1,0 A."),
    ("Lực từ tác dụng lên thanh có độ lớn 0,15 N và cùng chiều chuyển động của thanh.", False,
     "Sai về CHIỀU. Độ lớn đúng là F = B·i·ℓ = 0,30 · 1,0 · 0,50 = 0,15 N, nhưng theo định luật "
     "Lenz lực này luôn NGƯỢC chiều chuyển động, cản trở thanh."),
    ("Công suất toả nhiệt trên toàn mạch bằng 0,60 W.", True,
     "Đúng. P = e·i = 0,60 · 1,0 = 0,60 W, cũng bằng R·i² = 0,60 · 1,0² = 0,60 W.")],
   "Thanh dẫn trượt trên ray", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray nằm ngang"),

ds("Truyền tải điện năng từ một nhà máy có công suất phát 600 MW ở điện áp 20 kV. "
   "Người ta dùng máy tăng áp đưa điện áp lên 500 kV rồi truyền trên đường dây có điện trở 10 Ω.",
   [("Máy tăng áp có tỉ số số vòng dây thứ cấp trên sơ cấp bằng 25.", True,
     "Đúng. N₂/N₁ = U₂/U₁ = 500/20 = 25."),
    ("Cường độ dòng điện trên đường dây tải bằng 1200 A.", True,
     "Đúng. I = P/U = 600·10⁶ / (500·10³) = 1200 A."),
    ("Công suất hao phí trên đường dây bằng 14,4 MW.", True,
     "Đúng. ΔP = R·I² = 10 · 1200² = 10 · 1,44·10⁶ = 1,44·10⁷ W = 14,4 MW."),
    ("Nếu truyền trực tiếp ở 20 kV mà không tăng áp thì hao phí cũng chỉ khoảng 14,4 MW.", False,
     "Sai. Ở 20 kV thì I = 600·10⁶/(20·10³) = 30 000 A, hao phí ΔP = 10 · 30 000² = 9·10⁹ W "
     "= 9000 MW — lớn hơn cả công suất phát, nghĩa là hoàn toàn không thể truyền tải.")],
   "Truyền tải điện năng", TB, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),

ds("Xét hiện tượng dòng điện Foucault trong các thiết bị điện.",
   [("Dòng Foucault là dòng điện cảm ứng khép kín trong khối vật dẫn đặt trong từ trường "
     "biến thiên.", True,
     "Đúng. Đó chính là định nghĩa của dòng điện xoáy Foucault."),
    ("Trong bếp từ, dòng Foucault được tạo ra có chủ đích để làm nóng đáy nồi.", True,
     "Đúng. Đây là ứng dụng có lợi: nhiệt sinh ra ngay trong đáy nồi nên hiệu suất cao."),
    ("Trong lõi máy biến áp, dòng Foucault là có lợi vì giúp tăng từ thông.", False,
     "Sai. Trong lõi máy biến áp, dòng Foucault chỉ gây hao phí toả nhiệt. Vì thế người ta ghép "
     "lõi từ nhiều lá thép mỏng cách điện để hạn chế nó."),
    ("Nồi bằng thuỷ tinh hoặc nhôm nguyên chất thường không dùng được trên bếp từ thông thường.", True,
     "Đúng. Bếp từ cần đáy nồi bằng vật liệu nhiễm từ để từ thông tập trung và sinh dòng xoáy đủ "
     "mạnh; thuỷ tinh không dẫn điện còn nhôm không nhiễm từ.")],
   "Dòng Foucault", TB, fig="t_sd_dong_fuco", cap="Dòng điện Foucault trong khối kim loại"),
],
P3=[
sa("Một thanh dẫn dài 60 cm trượt đều với tốc độ 5,0 m/s trên hai ray nằm ngang đặt vuông góc với "
   "từ trường đều thẳng đứng B = 0,40 T. Suất điện động cảm ứng giữa hai đầu thanh bằng bao nhiêu vôn?",
   "1,2",
   "e = B·ℓ·v = 0,40 · 0,60 · 5,0 = 1,2 V.",
   "Thanh dẫn chuyển động", TB),

sa("Một tấm kim loại phẳng hình chữ nhật 10 cm × 20 cm được đặt trong từ trường đều B = 0,50 T "
   "sao cho pháp tuyến của tấm hợp với đường sức từ góc 60°. Từ thông qua tấm bằng bao nhiêu vêbe "
   "(làm tròn đến chữ số thập phân thứ ba)?",
   "0,005",
   "Diện tích tấm: S = 0,10 · 0,20 = 0,020 m².\n"
   "Φ = B·S·cos60° = 0,50 · 0,020 · 0,50 = 5,0·10⁻³ Wb = 0,005 Wb.",
   "Tính từ thông", TB),

sa("Một cuộn dây 400 vòng có điện trở 2,0 Ω. Từ thông qua mỗi vòng giảm đều từ 0,015 Wb xuống 0 "
   "trong 0,60 s. Cường độ dòng điện cảm ứng trong cuộn dây bằng bao nhiêu ampe?",
   "5",
   "|e| = N·|ΔΦ|/Δt = 400 · 0,015 / 0,60 = 400 · 0,025 = 10 V.\n"
   "i = |e|/R = 10/2,0 = 5,0 A.",
   "Faraday kết hợp định luật Ôm", TB),

sa("Một đoạn dây dẫn dài 5,0 cm nằm ngang, vuông góc với từ trường đều B = 0,80 T, được treo cân "
   "bằng trên một cái cân. Khi cho dòng điện 2,5 A chạy qua dây, lực từ tác dụng lên dây có độ lớn "
   "bằng bao nhiêu niutơn?",
   "0,1",
   "F = B·I·ℓ = 0,80 · 2,5 · 0,050 = 0,10 N.",
   "Cân dòng điện", TB, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

sa("Một máy phát điện xoay chiều có rôto quay với tốc độ 1500 vòng/phút. Tần số của suất điện động "
   "do máy tạo ra bằng bao nhiêu héc?",
   "25",
   "Đổi tốc độ quay: 1500 vòng/phút = 1500/60 = 25 vòng/giây.\n"
   "Mỗi vòng quay ứng với một chu kì của suất điện động nên f = 25 Hz.",
   "Tần số của máy phát", TB),

sa("Truyền công suất 200 kW đi xa trên đường dây có điện trở 8,0 Ω ở điện áp hiệu dụng 10 kV, "
   "hệ số công suất bằng 1. Hiệu suất truyền tải bằng bao nhiêu phần trăm?",
   "98,4",
   "I = P/U = 200 000/10 000 = 20 A.\n"
   "ΔP = R·I² = 8,0 · 20² = 3200 W = 3,2 kW.\n"
   "H = (P − ΔP)/P = (200 − 3,2)/200 = 196,8/200 = 0,984 = 98,4 %.",
   "Hiệu suất truyền tải", TB),
])


# =====================================================================  ĐỀ 4
DE4 = dict(
ma="12C3-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Vận dụng công thức nhiều bước, bài toán cân bằng lực và đọc đồ thị dòng xoay chiều",
P1=[
mc("Một đoạn dây dẫn thẳng dài 20 cm mang dòng điện 6,0 A đặt vuông góc với từ trường đều. "
   "Lực từ tác dụng lên dây là 0,36 N. Cảm ứng từ của từ trường bằng",
   ["0,15 T.", "0,30 T.", "0,60 T.", "1,20 T."],
   "B",
   "Từ F = B·I·ℓ suy ra B = F/(I·ℓ) = 0,36/(6,0 · 0,20) = 0,36/1,2 = 0,30 T.",
   "Tính cảm ứng từ", TB),

mc("Một khung dây 50 vòng, diện tích mỗi vòng 100 cm², đặt vuông góc với từ trường đều. "
   "Khi cảm ứng từ giảm đều từ 0,80 T về 0 trong 0,25 s, suất điện động cảm ứng có độ lớn",
   ["0,16 V.", "1,60 V.", "16,0 V.", "0,016 V."],
   "B",
   "S = 100 cm² = 0,010 m². ΔΦ mỗi vòng = 0,80 · 0,010 = 8,0·10⁻³ Wb.\n"
   "|e| = N·|ΔΦ|/Δt = 50 · 8,0·10⁻³/0,25 = 50 · 0,032 = 1,60 V.",
   "Định luật Faraday", TB),

mc("Trong đồ thị cường độ dòng điện xoay chiều theo thời gian, hai đường nằm ngang nét đứt ứng với "
   "các giá trị ±I₀/√2. Ý nghĩa của hai đường đó là",
   ["giá trị trung bình của dòng điện trong một chu kì.",
    "giá trị hiệu dụng của cường độ dòng điện.",
    "giá trị cực đại của cường độ dòng điện.",
    "giá trị của dòng điện tại thời điểm ban đầu."],
   "B",
   "I = I₀/√2 chính là giá trị hiệu dụng. Giá trị TRUNG BÌNH của dòng xoay chiều trong một chu kì "
   "bằng 0, nên phương án đầu sai.",
   "Đọc đồ thị dòng xoay chiều", TB, fig="t_dt_i_t",
   cap="Cường độ dòng điện xoay chiều theo thời gian"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 2200 vòng mắc vào mạng điện 220 V. "
   "Cuộn thứ cấp cung cấp điện áp 12 V cho một bóng đèn. Số vòng cuộn thứ cấp là",
   ["60 vòng.", "120 vòng.", "180 vòng.", "240 vòng."],
   "B",
   "N₂ = N₁·U₂/U₁ = 2200 · 12/220 = 2200 · 0,0545 = 120 vòng.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Một khung dây dẫn kín đặt trong từ trường đều. Muốn trong khung KHÔNG xuất hiện dòng điện "
   "cảm ứng khi khung quay, trục quay phải",
   ["vuông góc với đường sức từ.", "song song với đường sức từ.",
    "hợp với đường sức từ góc 45°.", "nằm trong mặt phẳng khung."],
   "B",
   "Nếu trục quay song song với B thì khi khung quay, góc giữa pháp tuyến và B không đổi, "
   "từ thông không đổi nên không có dòng cảm ứng. Trục vuông góc với B lại cho từ thông biến thiên "
   "mạnh nhất — đó là cấu hình của máy phát điện.",
   "Điều kiện có dòng cảm ứng", TB),

mc("Đặt vào hai đầu một điện trở R = 100 Ω một điện áp xoay chiều có giá trị hiệu dụng 220 V. "
   "Công suất toả nhiệt trên điện trở bằng",
   ["242 W.", "484 W.", "968 W.", "220 W."],
   "B",
   "P = U²/R = 220²/100 = 48 400/100 = 484 W. "
   "Vì dùng giá trị hiệu dụng nên công thức giống hệt dòng điện không đổi.",
   "Công suất dòng xoay chiều", TB),

mc("Một thanh dẫn khối lượng m nằm ngang trên hai ray nằm ngang trong từ trường đều thẳng đứng. "
   "Điều kiện để thanh bắt đầu trượt khi hệ số ma sát nghỉ cực đại là μ là",
   ["B·I·ℓ ≥ μ·m·g.", "B·I·ℓ ≥ m·g.", "B·I·ℓ ≥ μ·g.", "B·I·ℓ ≥ m·g/μ."],
   "A",
   "Vì từ trường thẳng đứng nên lực từ nằm ngang và không làm thay đổi áp lực N = mg. "
   "Thanh trượt khi lực từ thắng ma sát nghỉ cực đại: B·I·ℓ ≥ μ·N = μ·m·g.",
   "Cân bằng lực có ma sát", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một khung dây hình vuông cạnh 20 cm chuyển động đều với tốc độ 2,0 m/s đi vào vùng từ trường "
   "đều B = 0,40 T. Suất điện động cảm ứng trong khung khi đang đi vào vùng từ trường bằng",
   ["0,080 V.", "0,16 V.", "0,32 V.", "0,040 V."],
   "B",
   "Khi khung đang đi vào, chỉ cạnh trước nằm trong từ trường đóng vai trò nguồn: "
   "e = B·a·v = 0,40 · 0,20 · 2,0 = 0,16 V.",
   "Khung dây vào vùng từ trường", TB, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường đều"),

mc("Một nam châm được thả rơi thẳng đứng qua một vòng dây bằng đồng đặt nằm ngang. "
   "So với khi rơi tự do, thời gian rơi của nam châm",
   ["ngắn hơn.", "dài hơn.", "không đổi.", "bằng không."],
   "B",
   "Theo định luật Lenz, dòng cảm ứng trong vòng dây luôn tạo lực cản trở chuyển động của nam châm, "
   "cả lúc lại gần lẫn lúc ra xa. Vì thế nam châm rơi chậm hơn, thời gian rơi dài hơn.",
   "Định luật Lenz – ứng dụng", TB, fig="t_sd_nam_cham_roi",
   cap="Nam châm rơi qua vòng dây kín"),

mc("Trong một máy phát điện xoay chiều, nếu giữ nguyên tốc độ quay nhưng tăng số vòng dây của "
   "khung lên gấp ba thì suất điện động hiệu dụng",
   ["không đổi.", "tăng gấp ba.", "giảm ba lần.", "tăng gấp chín."],
   "B",
   "E₀ = ω·N·B·S tỉ lệ thuận với N, và E = E₀/√2 cũng vậy. Tăng N lên gấp ba thì suất điện động "
   "hiệu dụng tăng gấp ba. Tần số không đổi vì tốc độ quay giữ nguyên.",
   "Máy phát điện xoay chiều", TB),

mc("Hai vòng dây kín giống hệt nhau, một bằng đồng và một bằng nhựa, cùng đặt trong một từ trường "
   "biến thiên như nhau. Kết luận nào đúng?",
   ["Cả hai vòng đều có dòng điện cảm ứng như nhau.",
    "Chỉ vòng đồng có dòng điện cảm ứng đáng kể.",
    "Chỉ vòng nhựa có dòng điện cảm ứng.",
    "Không vòng nào có suất điện động cảm ứng."],
   "B",
   "Suất điện động cảm ứng xuất hiện trong CẢ HAI vòng vì từ thông đều biến thiên. "
   "Nhưng nhựa cách điện nên hầu như không có dòng điện chạy qua; chỉ vòng đồng mới có dòng cảm ứng "
   "đáng kể.",
   "Phân biệt suất điện động và dòng điện", TB),

mc("Một đoạn dây dẫn dài 10 cm mang dòng điện 5,0 A đặt trong từ trường đều B = 0,60 T. "
   "Lực từ tác dụng lên dây có độ lớn 0,15 N. Góc giữa dây và đường sức từ bằng",
   ["30°.", "45°.", "60°.", "90°."],
   "A",
   "sinα = F/(B·I·ℓ) = 0,15/(0,60 · 5,0 · 0,10) = 0,15/0,30 = 0,50 ⇒ α = 30°.",
   "Tìm góc từ lực từ", TB),

mc("Trong quá trình truyền tải điện năng, nếu giữ nguyên điện áp truyền tải nhưng tăng công suất "
   "truyền đi lên gấp đôi thì công suất hao phí",
   ["không đổi.", "tăng gấp bốn.", "tăng gấp đôi.", "giảm một nửa."],
   "B",
   "ΔP = R·(P/U)² tỉ lệ với BÌNH PHƯƠNG công suất truyền khi U không đổi. "
   "P tăng gấp đôi thì ΔP tăng gấp bốn.",
   "Hao phí truyền tải", TB),

mc("Một dòng điện xoay chiều có biểu thức i = 2,0·cos(100πt − π/3) (A). Tại thời điểm t = 0, "
   "cường độ dòng điện bằng",
   ["2,0 A.", "1,0 A.", "0 A.", "−1,73 A."],
   "B",
   "Thay t = 0: i = 2,0·cos(−π/3) = 2,0 · 0,5 = 1,0 A. "
   "Hàm cosin là hàm chẵn nên cos(−π/3) = cos(π/3) = 0,5.",
   "Giá trị tức thời", TB),

mc("Muốn tăng suất điện động cảm ứng trong một cuộn dây khi đưa nam châm lại gần, ta có thể",
   ["giữ nam châm đứng yên lâu hơn.", "đưa nam châm lại gần nhanh hơn.",
    "giảm số vòng dây.", "dùng cuộn dây có điện trở lớn hơn."],
   "B",
   "|e| = N·|ΔΦ|/Δt: muốn e lớn thì phải làm từ thông biến thiên NHANH hơn hoặc tăng số vòng dây. "
   "Điện trở chỉ ảnh hưởng tới cường độ dòng điện, không ảnh hưởng tới suất điện động.",
   "Các yếu tố ảnh hưởng tới e", D),

mc("Thiết bị nào sau đây biến đổi điện năng thành cơ năng dựa trên lực từ?",
   ["Máy biến áp.", "Động cơ điện.", "Bóng đèn LED.", "Ấm đun nước điện."],
   "B",
   "Trong động cơ điện, lực từ tác dụng lên khung dây mang dòng điện làm khung quay, "
   "biến điện năng thành cơ năng. Máy biến áp chỉ biến đổi điện áp, không tạo chuyển động.",
   "Ứng dụng lực từ", D),

mc("Một khung dây đặt trong từ trường đều, mặt phẳng khung song song với các đường sức. "
   "Momen lực từ tác dụng lên khung khi có dòng điện chạy qua",
   ["bằng không.", "đạt giá trị lớn nhất.",
    "bằng một nửa giá trị lớn nhất.", "phụ thuộc điện trở của khung."],
   "B",
   "Khi mặt phẳng khung song song với B, hai cạnh đối diện chịu hai lực từ ngược chiều tạo thành "
   "ngẫu lực với cánh tay đòn lớn nhất, nên momen quay đạt cực đại. Đây chính là vị trí khung "
   "quay mạnh nhất trong động cơ điện.",
   "Momen lực từ", TB),

mc("Khi đặt một vòng dây kín trong một từ trường đều KHÔNG đổi theo thời gian và vòng dây đứng yên, "
   "trong vòng dây",
   ["luôn có dòng điện cảm ứng.", "không có dòng điện cảm ứng.",
    "có dòng điện cảm ứng nếu từ trường đủ mạnh.",
    "có dòng điện cảm ứng nếu vòng dây bằng kim loại."],
   "B",
   "Cả B, S và góc đều không đổi nên từ thông không biến thiên: không có dòng cảm ứng. "
   "Độ mạnh của từ trường và vật liệu của vòng dây đều không thay đổi kết luận này.",
   "Điều kiện có dòng cảm ứng", D),
],
P2=[
ds("Một khung dây hình vuông cạnh a = 20 cm, có điện trở 0,20 Ω, chuyển động đều với tốc độ "
   "v = 2,0 m/s đi vào rồi đi ra khỏi một vùng từ trường đều B = 0,40 T rộng d = 50 cm, "
   "các đường sức vuông góc với mặt phẳng khung.",
   [("Khi khung bắt đầu đi vào vùng từ trường, suất điện động cảm ứng bằng 0,16 V.", True,
     "Đúng. e = B·a·v = 0,40 · 0,20 · 2,0 = 0,16 V."),
    ("Cường độ dòng điện cảm ứng lúc khung đi vào bằng 0,80 A.", True,
     "Đúng. i = e/R = 0,16/0,20 = 0,80 A."),
    ("Thời gian khung nằm trọn trong vùng từ trường là 0,25 s.", False,
     "Sai. Khung nằm trọn trong vùng khi cạnh sau đã vào (đi được a = 20 cm) cho tới khi cạnh trước "
     "chạm mép ra (đi được d = 50 cm), tức quãng đường 30 cm. "
     "Thời gian = 0,30/2,0 = 0,15 s."),
    ("Trong suốt thời gian khung nằm trọn trong vùng từ trường, không có dòng điện cảm ứng.", True,
     "Đúng. Lúc đó từ thông qua khung không đổi nên không có dòng cảm ứng.")],
   "Khung dây vào – ra vùng từ trường", TB,
   fig="t_sd_khung_vao_B", cap="Khung dây đi vào vùng từ trường đều"),

ds("Một khung dây phẳng gồm N = 200 vòng, diện tích mỗi vòng S = 50 cm², quay đều quanh trục vuông "
   "góc với từ trường đều B = 0,25 T, tốc độ quay 1200 vòng/phút. Lấy π ≈ 3,1416.",
   [("Tần số của suất điện động do khung tạo ra là 20 Hz.", True,
     "Đúng. 1200 vòng/phút = 1200/60 = 20 vòng/giây nên f = 20 Hz."),
    ("Tần số góc của khung xấp xỉ 125,7 rad/s.", True,
     "Đúng. ω = 2πf = 2 · 3,1416 · 20 ≈ 125,66 ≈ 125,7 rad/s."),
    ("Suất điện động cực đại xấp xỉ 31,4 V.", True,
     "Đúng. E₀ = ω·N·B·S = 125,66 · 200 · 0,25 · 5,0·10⁻³ = 125,66 · 0,25 ≈ 31,4 V."),
    ("Suất điện động hiệu dụng xấp xỉ 44,4 V.", False,
     "Sai. E = E₀/√2 = 31,4/1,414 ≈ 22,2 V. Giá trị 44,4 V ứng với việc NHÂN cho √2 thay vì chia.")],
   "Máy phát điện xoay chiều", TB, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

ds("Một đoạn dây dẫn thẳng dài 5,0 cm được đặt nằm ngang trong khe giữa hai cực của nam châm, "
   "vuông góc với từ trường đều B = 0,60 T. Nam châm đặt trên một cái cân điện tử. "
   "Lấy g = 10 m/s².",
   [("Khi chưa có dòng điện, lực từ tác dụng lên đoạn dây bằng 0.", True,
     "Đúng. Không có dòng điện thì I = 0 nên F = B·I·ℓ = 0."),
    ("Khi cho dòng điện 4,0 A chạy qua dây, lực từ tác dụng lên dây bằng 0,12 N.", True,
     "Đúng. F = B·I·ℓ = 0,60 · 4,0 · 0,050 = 0,12 N."),
    ("Số chỉ của cân thay đổi một lượng tương ứng với khối lượng 12 g.", True,
     "Đúng. Phản lực tác dụng lên nam châm có độ lớn 0,12 N, tương ứng Δm = F/g = 0,12/10 "
     "= 0,012 kg = 12 g."),
    ("Nếu đổi chiều dòng điện thì số chỉ của cân không thay đổi.", False,
     "Sai. Đổi chiều dòng điện thì lực từ đổi chiều, nên nếu trước đó số chỉ tăng 12 g thì "
     "bây giờ sẽ giảm 12 g — thay đổi tổng cộng 24 g.")],
   "Cân dòng điện", TB, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

ds("Một máy biến áp lí tưởng có N₁ = 1100 vòng, N₂ = 200 vòng, đặt dưới điện áp xoay chiều 220 V. "
   "Cuộn thứ cấp nối với một điện trở thuần R = 20 Ω.",
   [("Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng 40 V.", True,
     "Đúng. U₂ = U₁·N₂/N₁ = 220 · 200/1100 = 220/5,5 = 40 V."),
    ("Cường độ dòng điện hiệu dụng qua điện trở bằng 2,0 A.", True,
     "Đúng. I₂ = U₂/R = 40/20 = 2,0 A."),
    ("Công suất tiêu thụ ở mạch thứ cấp bằng 80 W.", True,
     "Đúng. P₂ = U₂·I₂ = 40 · 2,0 = 80 W."),
    ("Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng 2,0 A.", False,
     "Sai. Máy lí tưởng bảo toàn công suất: I₁ = P/U₁ = 80/220 ≈ 0,36 A. "
     "Có thể kiểm tra bằng I₁/I₂ = N₂/N₁ = 200/1100 ⇒ I₁ = 2,0 · 0,1818 ≈ 0,36 A.")],
   "Máy biến áp có tải", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),
],
P3=[
sa("Một đoạn dây dẫn dài 15 cm đặt vuông góc với từ trường đều B = 0,40 T. Muốn lực từ tác dụng lên "
   "dây đạt 0,30 N thì cường độ dòng điện qua dây phải bằng bao nhiêu ampe?",
   "5",
   "Từ F = B·I·ℓ ⇒ I = F/(B·ℓ) = 0,30/(0,40 · 0,15) = 0,30/0,060 = 5,0 A.",
   "Lực từ – bài toán ngược", TB),

sa("Một cuộn dây 150 vòng, diện tích mỗi vòng 40 cm², đặt vuông góc với từ trường đều. "
   "Cảm ứng từ tăng đều từ 0,20 T lên 0,60 T trong 0,30 s. Độ lớn suất điện động cảm ứng bằng "
   "bao nhiêu vôn?",
   "0,8",
   "S = 40 cm² = 4,0·10⁻³ m². ΔB = 0,60 − 0,20 = 0,40 T.\n"
   "|ΔΦ| mỗi vòng = ΔB·S = 0,40 · 4,0·10⁻³ = 1,6·10⁻³ Wb.\n"
   "|e| = N·|ΔΦ|/Δt = 150 · 1,6·10⁻³/0,30 = 150 · 5,333·10⁻³ = 0,80 V.",
   "Định luật Faraday", TB),

sa("Một thanh dẫn khối lượng 60 g, dài 30 cm nằm ngang trên hai ray nằm ngang trong từ trường đều "
   "thẳng đứng B = 0,50 T. Hệ số ma sát nghỉ cực đại giữa thanh và ray là 0,20. "
   "Cường độ dòng điện nhỏ nhất để thanh bắt đầu trượt bằng bao nhiêu ampe? Lấy g = 10 m/s².",
   "0,8",
   "Áp lực của thanh lên ray: N = m·g = 0,060 · 10 = 0,60 N (lực từ nằm ngang nên không đổi N).\n"
   "Ma sát nghỉ cực đại: F(ms) = μ·N = 0,20 · 0,60 = 0,12 N.\n"
   "Điều kiện trượt: B·I·ℓ ≥ 0,12 ⇒ 0,50 · I · 0,30 ≥ 0,12 ⇒ 0,15·I ≥ 0,12 ⇒ I ≥ 0,80 A.",
   "Cân bằng lực có ma sát", TB, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray nằm ngang"),

sa("Một máy biến áp lí tưởng cung cấp cho tải một công suất 660 W ở điện áp thứ cấp 110 V. "
   "Điện áp sơ cấp là 220 V. Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng bao nhiêu ampe?",
   "3",
   "Máy lí tưởng nên công suất sơ cấp bằng công suất thứ cấp: P₁ = P₂ = 660 W.\n"
   "I₁ = P₁/U₁ = 660/220 = 3,0 A.",
   "Máy biến áp – công suất", TB),

sa("Một dòng điện xoay chiều có cường độ hiệu dụng 2,0 A chạy qua điện trở 50 Ω trong 5,0 phút. "
   "Nhiệt lượng toả ra trên điện trở bằng bao nhiêu kilôjun?",
   "60",
   "Đổi thời gian: t = 5,0 phút = 300 s.\n"
   "Dùng giá trị HIỆU DỤNG: Q = R·I²·t = 50 · 2,0² · 300 = 50 · 4,0 · 300 = 60 000 J = 60 kJ.",
   "Tác dụng nhiệt của dòng xoay chiều", TB),

sa("Cần truyền công suất 120 kW đi xa trên đường dây có điện trở tổng 6,0 Ω. Muốn công suất hao phí "
   "không vượt quá 2,0 % công suất truyền đi thì điện áp truyền tải tối thiểu bằng bao nhiêu "
   "kilôvôn? Hệ số công suất bằng 1.",
   "6",
   "Hao phí cho phép: ΔP = 2,0 % · 120 000 = 2400 W.\n"
   "Từ ΔP = R·I² ⇒ I² = 2400/6,0 = 400 ⇒ I = 20 A.\n"
   "Điện áp tương ứng: U = P/I = 120 000/20 = 6000 V = 6,0 kV.\n"
   "Kiểm tra bằng công thức gộp: U² = R·P²/ΔP = 6,0·(1,2·10⁵)²/2400 = 3,6·10⁷ ⇒ U = 6000 V.",
   "Hao phí truyền tải – bài toán ngược", K),
])


# =====================================================================  ĐỀ 5
DE5 = dict(
ma="12C3-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Bài toán nhiều bước: cảm ứng điện từ, máy phát, máy biến áp có tải, truyền tải",
P1=[
mc("Một khung dây phẳng 80 vòng, diện tích mỗi vòng 25 cm², đặt trong từ trường đều B = 0,50 T "
   "sao cho pháp tuyến hợp với đường sức góc 60°. Từ thông qua khung dây bằng",
   ["5,0·10⁻³ Wb.", "5,0·10⁻² Wb.", "1,0·10⁻² Wb.", "1,0·10⁻¹ Wb."],
   "B",
   "Từ thông qua CẢ khung N vòng: Φ = N·B·S·cosθ.\n"
   "S = 25 cm² = 2,5·10⁻³ m²; cos60° = 0,50.\n"
   "Φ = 80 · 0,50 · 2,5·10⁻³ · 0,50 = 80 · 6,25·10⁻⁴ = 5,0·10⁻² Wb.",
   "Từ thông qua cuộn nhiều vòng", TB),

mc("Một vòng dây kín điện trở 0,50 Ω đặt trong từ trường đều. Từ thông qua vòng dây giảm đều "
   "0,15 Wb trong 0,30 s. Điện lượng chuyển qua tiết diện dây trong thời gian đó bằng",
   ["0,10 C.", "0,30 C.", "0,50 C.", "1,00 C."],
   "B",
   "i = |e|/R = (|ΔΦ|/Δt)/R nên điện lượng q = i·Δt = |ΔΦ|/R = 0,15/0,50 = 0,30 C.\n"
   "Điện lượng chỉ phụ thuộc độ biến thiên từ thông và điện trở, KHÔNG phụ thuộc thời gian biến thiên.",
   "Điện lượng cảm ứng", K),

mc("Một máy phát điện xoay chiều có 8 cặp cực, rôto quay với tốc độ 375 vòng/phút. "
   "Tần số của suất điện động do máy tạo ra là",
   ["25 Hz.", "50 Hz.", "60 Hz.", "100 Hz."],
   "B",
   "Với máy phát có p cặp cực quay n vòng/giây thì f = p·n.\n"
   "n = 375/60 = 6,25 vòng/giây ⇒ f = 8 · 6,25 = 50 Hz.",
   "Máy phát nhiều cặp cực", TB),

mc("Đặt điện áp u = 200·cos(100πt) (V) vào hai đầu điện trở R = 50 Ω. "
   "Công suất tiêu thụ trên điện trở bằng",
   ["200 W.", "400 W.", "800 W.", "566 W."],
   "B",
   "Giá trị hiệu dụng: U = U₀/√2 = 200/1,414 ≈ 141,4 V.\n"
   "P = U²/R = (141,4)²/50 = 20 000/50 = 400 W.\n"
   "Cách nhanh hơn: P = U₀²/(2R) = 40 000/100 = 400 W. "
   "Nếu lấy thẳng 200²/50 = 800 W là đã nhầm cực đại với hiệu dụng.",
   "Công suất dòng xoay chiều", TB),

mc("Trong đồ thị cường độ dòng điện xoay chiều theo thời gian, phần thời gian mà độ lớn cường độ "
   "dòng điện lớn hơn giá trị hiệu dụng chiếm tỉ lệ",
   ["đúng một nửa chu kì.", "đúng một nửa thời gian.",
    "nhỏ hơn một nửa thời gian.", "lớn hơn một nửa thời gian."],
   "B",
   "Với dao động hình sin, |i| vượt quá I₀/√2 đúng một nửa thời gian: trong mỗi chu kì có bốn "
   "khoảng, mỗi khoảng dài T/8, tổng cộng T/2. Các vùng tô đậm trên đồ thị minh hoạ điều này.",
   "Đọc đồ thị dòng xoay chiều", K, fig="t_dt_i_t",
   cap="Vùng tô đậm ứng với |i| lớn hơn giá trị hiệu dụng"),

mc("Một khung dây dẫn quay đều trong từ trường đều với tần số 50 Hz. Trong mỗi giây, độ lớn của "
   "suất điện động cảm ứng đạt giá trị cực đại",
   ["25 lần.", "50 lần.", "100 lần.", "200 lần."],
   "C",
   "Trong mỗi chu kì, |e| đạt cực đại hai lần (một lần dương, một lần âm). "
   "Với 50 chu kì mỗi giây ta có 100 lần.",
   "Chu kì của suất điện động", TB),

mc("Một máy biến áp lí tưởng có tỉ số vòng dây N₁ : N₂ = 5 : 1. Cuộn thứ cấp nối với một bóng đèn "
   "ghi 44 V – 88 W và đèn sáng bình thường. Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng",
   ["0,40 A.", "2,00 A.", "0,20 A.", "10,0 A."],
   "A",
   "Đèn sáng bình thường: I₂ = P/U₂ = 88/44 = 2,0 A.\n"
   "Máy lí tưởng: I₁/I₂ = N₂/N₁ = 1/5 ⇒ I₁ = 2,0/5 = 0,40 A.\n"
   "Kiểm tra: U₁ = 5 · 44 = 220 V và P = 220 · 0,40 = 88 W — khớp.",
   "Máy biến áp có tải", TB, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một thanh dẫn dài 40 cm trượt đều trên hai ray nằm ngang, vuông góc với từ trường đều thẳng "
   "đứng B = 0,25 T. Điện trở toàn mạch 0,20 Ω. Để duy trì tốc độ 3,0 m/s (bỏ qua ma sát), "
   "cần tác dụng một lực kéo có độ lớn",
   ["0,075 N.", "0,15 N.", "0,30 N.", "0,60 N."],
   "B",
   "e = B·ℓ·v = 0,25 · 0,40 · 3,0 = 0,30 V;  i = e/R = 0,30/0,20 = 1,5 A.\n"
   "Lực từ cản: F = B·i·ℓ = 0,25 · 1,5 · 0,40 = 0,15 N.\n"
   "Chuyển động đều, không ma sát nên lực kéo phải cân bằng lực từ cản: F(kéo) = 0,15 N.",
   "Thanh dẫn trượt – cân bằng lực", TB, fig="t_sd_ray_ngang",
   cap="Thanh dẫn trên hai ray nằm ngang"),

mc("Với bài toán thanh dẫn ở câu trên, công suất cơ học mà lực kéo cung cấp bằng",
   ["0,15 W.", "0,45 W.", "0,30 W.", "0,90 W."],
   "B",
   "P = F·v = 0,15 · 3,0 = 0,45 W.\n"
   "Kiểm tra bằng công suất điện: P = e·i = 0,30 · 1,5 = 0,45 W — toàn bộ công cơ học chuyển "
   "thành nhiệt trên điện trở mạch.",
   "Chuyển hoá năng lượng", K),

mc("Một đoạn dây dẫn dài 25 cm mang dòng điện 8,0 A được treo nằm ngang bằng hai sợi dây mảnh "
   "trong từ trường đều nằm ngang, vuông góc với đoạn dây. Để lực căng của hai sợi dây bằng 0, "
   "cảm ứng từ phải có độ lớn (dây có khối lượng 40 g, g = 10 m/s²)",
   ["0,10 T.", "0,20 T.", "0,40 T.", "0,80 T."],
   "B",
   "Lực căng bằng 0 nghĩa là lực từ phải cân bằng hoàn toàn trọng lực và hướng lên:\n"
   "B·I·ℓ = m·g ⇒ B · 8,0 · 0,25 = 0,040 · 10 = 0,40 N.\n"
   "B · 2,0 = 0,40 ⇒ B = 0,20 T.",
   "Cân bằng lực từ và trọng lực", TB),

mc("Đưa cực Bắc của một nam châm lại gần một vòng dây kín đặt trong mặt phẳng vuông góc với trục "
   "nam châm. Nhìn từ phía nam châm, dòng điện cảm ứng trong vòng dây có chiều",
   ["cùng chiều kim đồng hồ.", "ngược chiều kim đồng hồ.",
    "lúc đầu cùng chiều rồi đổi ngược.", "bằng không."],
   "B",
   "Từ thông hướng về phía người quan sát và đang tăng. Theo định luật Lenz, dòng cảm ứng phải sinh "
   "từ trường ngược lại, tức hướng ra xa người quan sát. Dùng quy tắc nắm tay phải, dòng điện phải "
   "chạy ngược chiều kim đồng hồ khi nhìn từ phía nam châm.",
   "Định luật Lenz – xác định chiều", K, fig="t_sd_lenz", cap="Chiều dòng điện cảm ứng"),

mc("Truyền một công suất 500 kW đi xa với hiệu suất truyền tải 96 %. Công suất hao phí trên đường "
   "dây bằng",
   ["10 kW.", "20 kW.", "24 kW.", "480 kW."],
   "B",
   "Hiệu suất 96 % nghĩa là hao phí chiếm 4 %: ΔP = 4 % · 500 = 20 kW. "
   "Giá trị 480 kW là công suất nơi tiêu thụ nhận được, không phải hao phí.",
   "Hiệu suất truyền tải", TB),

mc("Một khung dây phẳng đặt trong từ trường đều, mặt phẳng khung hợp với đường sức từ góc 60°. "
   "Nếu quay khung để mặt phẳng khung vuông góc với đường sức thì từ thông qua khung",
   ["giảm còn một nửa.", "tăng lên và gấp khoảng 1,15 lần giá trị cũ.",
    "không đổi.", "tăng gấp đôi."],
   "B",
   "Ban đầu góc giữa pháp tuyến và B là 30°, từ thông tỉ lệ cos30° ≈ 0,866.\n"
   "Sau khi quay, pháp tuyến song song B nên từ thông tỉ lệ cos0° = 1.\n"
   "Tỉ số 1/0,866 ≈ 1,15 lần.",
   "Từ thông – phân biệt góc", K, fig="t_sd_khung_nghieng",
   cap="Khung dây hợp góc với đường sức từ"),

mc("Trong một máy biến áp thực tế, hiệu suất luôn nhỏ hơn 100 % chủ yếu vì",
   ["số vòng dây thứ cấp ít hơn sơ cấp.",
    "hao phí do toả nhiệt trên cuộn dây và do dòng Foucault trong lõi.",
    "điện áp sơ cấp biến thiên.",
    "từ thông trong lõi là hằng số."],
   "B",
   "Hai nguồn hao phí chính là hiệu ứng Jun trên điện trở cuộn dây và dòng điện xoáy Foucault "
   "cùng hiện tượng từ trễ trong lõi thép. Tỉ số vòng dây không liên quan tới hiệu suất.",
   "Máy biến áp thực tế", TB),

mc("Một cuộn dây có 500 vòng, diện tích mỗi vòng 20 cm², được đặt trong từ trường đều B = 0,30 T "
   "với pháp tuyến song song đường sức. Người ta quay cuộn dây 90° trong 0,20 s. "
   "Suất điện động cảm ứng trung bình bằng",
   ["1,5 V.", "3,0 V.", "0,75 V.", "6,0 V."],
   "A",
   "S = 20 cm² = 2,0·10⁻³ m².\n"
   "Từ thông đầu (mỗi vòng): Φ₁ = 0,30 · 2,0·10⁻³ = 6,0·10⁻⁴ Wb; sau khi quay 90°: Φ₂ = 0.\n"
   "|e| = N·|ΔΦ|/Δt = 500 · 6,0·10⁻⁴/0,20 = 500 · 3,0·10⁻³ = 1,5 V.",
   "Faraday – quay khung", TB),

mc("Người ta dùng một nam châm điện thay cho nam châm vĩnh cửu trong một thí nghiệm cảm ứng điện từ "
   "vì nam châm điện",
   ["luôn mạnh hơn nam châm vĩnh cửu.",
    "cho phép thay đổi hoặc ngắt từ trường một cách dễ dàng.",
    "không cần nguồn điện.",
    "có hai cực cố định không đổi chỗ."],
   "B",
   "Ưu điểm cốt lõi của nam châm điện là điều khiển được: thay đổi cường độ dòng điện thì từ trường "
   "thay đổi, ngắt dòng thì từ tính biến mất, đảo chiều dòng thì hai cực đổi chỗ.",
   "Nam châm điện", TB, fig="t_sd_ongday", cap="Ống dây có dòng điện"),

mc("Một đoạn dây dẫn thẳng dài 10 cm mang dòng điện 3,0 A đặt trong từ trường đều B = 0,20 T. "
   "Khi quay dây từ vị trí song song đến vị trí vuông góc với đường sức, lực từ tác dụng lên dây",
   ["giảm từ 0,060 N về 0.", "tăng từ 0 lên 0,060 N.",
    "không đổi và bằng 0,060 N.", "tăng từ 0 lên 0,030 N."],
   "B",
   "Song song với đường sức: α = 0° ⇒ F = 0.\n"
   "Vuông góc: α = 90° ⇒ F = B·I·ℓ = 0,20 · 3,0 · 0,10 = 0,060 N.\n"
   "Vậy lực từ tăng từ 0 lên 0,060 N.",
   "Vai trò của góc α", TB, fig="t_sd_goc_alpha", cap="Dây hợp góc α với đường sức"),

mc("Khi truyền tải điện năng, người ta đặt máy tăng áp ở đầu đường dây và máy hạ áp ở cuối đường dây. "
   "Lí do đặt máy hạ áp ở cuối là",
   ["để tiếp tục giảm hao phí trên đường dây.",
    "để đưa điện áp về mức an toàn và phù hợp với thiết bị tiêu thụ.",
    "để tăng công suất truyền tải.",
    "để biến dòng xoay chiều thành dòng một chiều."],
   "B",
   "Hao phí chỉ xảy ra trên đường dây, phía sau máy hạ áp không còn đường dây dài nữa. "
   "Máy hạ áp có nhiệm vụ đưa điện áp hàng trăm kilôvôn về 220 V an toàn cho hộ tiêu thụ.",
   "Truyền tải điện năng", TB, fig="t_sd_truyen_tai", cap="Sơ đồ truyền tải điện năng"),
],
P2=[
ds("Một vòng dây dẫn kín, điện trở 0,25 Ω, đặt trong từ trường đều có các đường sức vuông góc với "
   "mặt phẳng vòng dây. Từ thông qua vòng dây biến thiên đều từ 0,10 Wb xuống 0,020 Wb trong 0,40 s.",
   [("Độ lớn suất điện động cảm ứng trong vòng dây bằng 0,20 V.", True,
     "Đúng. |e| = |ΔΦ|/Δt = (0,10 − 0,020)/0,40 = 0,080/0,40 = 0,20 V."),
    ("Cường độ dòng điện cảm ứng trong vòng dây bằng 0,80 A.", True,
     "Đúng. i = |e|/R = 0,20/0,25 = 0,80 A."),
    ("Điện lượng chuyển qua tiết diện vòng dây trong 0,40 s bằng 0,32 C.", True,
     "Đúng. q = i·Δt = 0,80 · 0,40 = 0,32 C, cũng bằng |ΔΦ|/R = 0,080/0,25 = 0,32 C."),
    ("Nếu thời gian biến thiên rút ngắn còn 0,20 s thì điện lượng chuyển qua tăng gấp đôi.", False,
     "Sai. Điện lượng q = |ΔΦ|/R không phụ thuộc thời gian biến thiên nên vẫn bằng 0,32 C. "
     "Chỉ có suất điện động và cường độ dòng điện tăng gấp đôi.")],
   "Điện lượng cảm ứng", K),

ds("Một máy phát điện xoay chiều một pha có phần cảm gồm 4 cặp cực, rôto quay 750 vòng/phút. "
   "Phần ứng gồm 120 vòng dây, diện tích mỗi vòng 60 cm², từ trường đều B = 0,20 T. Lấy π ≈ 3,1416.",
   [("Tần số của suất điện động do máy tạo ra bằng 50 Hz.", True,
     "Đúng. n = 750/60 = 12,5 vòng/giây;  f = p·n = 4 · 12,5 = 50 Hz."),
    ("Tần số góc của suất điện động xấp xỉ 314 rad/s.", True,
     "Đúng. ω = 2πf = 2 · 3,1416 · 50 ≈ 314,16 rad/s."),
    ("Suất điện động cực đại xấp xỉ 45,2 V.", True,
     "Đúng. E₀ = ω·N·B·S = 314,16 · 120 · 0,20 · 6,0·10⁻³ = 314,16 · 0,144 ≈ 45,2 V."),
    ("Nếu tăng tốc độ quay lên gấp đôi thì tần số tăng gấp đôi nhưng suất điện động cực đại "
     "không đổi.", False,
     "Sai. E₀ = ω·N·B·S tỉ lệ thuận với ω, nên khi tốc độ quay tăng gấp đôi thì cả tần số lẫn "
     "suất điện động cực đại đều tăng gấp đôi.")],
   "Máy phát điện xoay chiều", TB, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

ds("Một đường dây tải điện dài truyền công suất 1,0 MW từ nhà máy tới khu dân cư. "
   "Điện trở tổng của đường dây là 5,0 Ω, hệ số công suất bằng 1.",
   [("Nếu truyền ở điện áp 10 kV thì cường độ dòng điện trên dây là 100 A.", True,
     "Đúng. I = P/U = 1,0·10⁶/(10·10³) = 100 A."),
    ("Với điện áp 10 kV, công suất hao phí là 50 kW.", True,
     "Đúng. ΔP = R·I² = 5,0 · 100² = 50 000 W = 50 kW."),
    ("Nếu tăng điện áp lên 50 kV thì công suất hao phí chỉ còn 2,0 kW.", True,
     "Đúng. Điện áp tăng 5 lần nên hao phí giảm 25 lần: 50/25 = 2,0 kW."),
    ("Hiệu suất truyền tải ở 50 kV là 98 %.", False,
     "Sai. Hao phí 2,0 kW trên 1000 kW tương ứng 0,2 %, nên hiệu suất là 99,8 % chứ không phải 98 %.")],
   "Truyền tải điện năng", TB, fig="t_sd_truyen_tai", cap="Truyền tải điện năng đi xa"),

ds("Đặt điện áp xoay chiều u = 220√2·cos(100πt) (V) vào hai đầu một điện trở thuần R = 110 Ω.",
   [("Điện áp hiệu dụng ở hai đầu điện trở bằng 220 V.", True,
     "Đúng. Biểu thức có U₀ = 220√2 nên U = U₀/√2 = 220 V."),
    ("Cường độ dòng điện hiệu dụng qua điện trở bằng 2,0 A.", True,
     "Đúng. I = U/R = 220/110 = 2,0 A."),
    ("Công suất tiêu thụ trên điện trở bằng 440 W.", True,
     "Đúng. P = U·I = 220 · 2,0 = 440 W, cũng bằng U²/R = 48 400/110 = 440 W."),
    ("Nhiệt lượng toả ra trên điện trở trong 1 phút bằng 440 J.", False,
     "Sai. Q = P·t = 440 · 60 = 26 400 J. Giá trị 440 J là nhiệt lượng toả ra trong đúng 1 giây.")],
   "Mạch điện xoay chiều thuần trở", TB),
],
P3=[
sa("Một vòng dây kín có điện trở 0,40 Ω. Từ thông qua vòng dây giảm đều 0,24 Wb. "
   "Điện lượng chuyển qua tiết diện của vòng dây trong quá trình đó bằng bao nhiêu culông?",
   "0,6",
   "q = |ΔΦ|/R = 0,24/0,40 = 0,60 C.\n"
   "Điện lượng không phụ thuộc thời gian biến thiên của từ thông.",
   "Điện lượng cảm ứng", K),

sa("Một máy phát điện xoay chiều có 6 cặp cực. Muốn máy phát ra dòng điện tần số 50 Hz thì rôto "
   "phải quay với tốc độ bao nhiêu vòng mỗi phút?",
   "500",
   "f = p·n với n tính bằng vòng/giây ⇒ n = f/p = 50/6 ≈ 8,333 vòng/giây.\n"
   "Đổi sang vòng/phút: 8,333 · 60 = 500 vòng/phút.",
   "Máy phát nhiều cặp cực", TB),

sa("Một thanh dẫn dài 50 cm trượt đều với tốc độ 6,0 m/s trên hai ray nằm ngang, vuông góc với từ "
   "trường đều thẳng đứng B = 0,20 T. Điện trở toàn mạch 0,30 Ω. Bỏ qua ma sát. "
   "Công suất cơ học cần cung cấp để duy trì chuyển động bằng bao nhiêu oát?",
   "1,2",
   "e = B·ℓ·v = 0,20 · 0,50 · 6,0 = 0,60 V.\n"
   "i = e/R = 0,60/0,30 = 2,0 A.\n"
   "Bỏ qua ma sát nên toàn bộ công cơ học chuyển thành điện năng rồi thành nhiệt:\n"
   "P = e·i = 0,60 · 2,0 = 1,2 W.",
   "Chuyển hoá năng lượng", K),

sa("Một đoạn dây dẫn dài 20 cm, khối lượng 30 g được treo nằm ngang bằng hai sợi dây mảnh trong "
   "từ trường đều nằm ngang vuông góc với đoạn dây, B = 0,50 T. Cần cho dòng điện có cường độ bao "
   "nhiêu ampe chạy qua để lực căng hai sợi dây bằng 0? Lấy g = 10 m/s².",
   "3",
   "Lực từ phải hướng lên và cân bằng trọng lực:\n"
   "B·I·ℓ = m·g ⇒ 0,50 · I · 0,20 = 0,030 · 10 = 0,30 N.\n"
   "0,10·I = 0,30 ⇒ I = 3,0 A.",
   "Cân bằng lực từ – trọng lực", TB),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 1500 vòng nối với mạng 220 V. Cuộn thứ cấp cung cấp "
   "cho một động cơ hoạt động ở 110 V với công suất 550 W. Cường độ dòng điện hiệu dụng chạy "
   "trong cuộn sơ cấp bằng bao nhiêu ampe?",
   "2,5",
   "Máy lí tưởng nên công suất được bảo toàn: P₁ = P₂ = 550 W.\n"
   "I₁ = P₁/U₁ = 550/220 = 2,5 A.",
   "Máy biến áp – công suất", TB),

sa("Truyền công suất 900 kW đi xa trên đường dây có điện trở 4,0 Ω ở điện áp hiệu dụng 30 kV. "
   "Hiệu suất truyền tải bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ nhất)? "
   "Hệ số công suất bằng 1.",
   "99,6",
   "I = P/U = 900 000/30 000 = 30 A.\n"
   "ΔP = R·I² = 4,0 · 30² = 3600 W = 3,6 kW.\n"
   "H = (900 − 3,6)/900 = 896,4/900 = 0,9960 = 99,6 %.",
   "Hiệu suất truyền tải", TB),
])


# =====================================================================  ĐỀ 6
DE6 = dict(
ma="12C3-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Kết hợp lực từ với cơ học, khung dây nghiêng, đọc đồ thị và suy luận định tính sâu",
P1=[
mc("Hai dây dẫn thẳng song song dài đặt cạnh nhau, mang hai dòng điện CÙNG chiều. Hai dây sẽ",
   ["đẩy nhau.", "hút nhau.", "không tương tác.", "quay quanh nhau."],
   "B",
   "Dòng thứ nhất tạo từ trường tại vị trí dòng thứ hai; dùng quy tắc nắm tay phải rồi quy tắc "
   "bàn tay trái, lực từ tác dụng lên dây thứ hai hướng về phía dây thứ nhất. "
   "Hai dòng cùng chiều thì hút nhau, ngược chiều thì đẩy nhau.",
   "Tương tác giữa hai dòng điện", TB),

mc("Một khung dây hình chữ nhật mang dòng điện đặt trong từ trường đều sao cho mặt phẳng khung "
   "VUÔNG GÓC với đường sức từ. Momen lực từ tác dụng lên khung",
   ["đạt giá trị lớn nhất.", "bằng không.",
    "bằng một nửa giá trị lớn nhất.", "làm khung quay đều."],
   "B",
   "Khi mặt phẳng khung vuông góc với B, hai lực từ trên hai cạnh đối diện cùng nằm trên một đường "
   "thẳng nên không tạo thành ngẫu lực: momen bằng 0. Đây là vị trí cân bằng của khung.",
   "Momen lực từ", TB),

mc("Một thanh dẫn trượt không ma sát xuống một mặt phẳng nghiêng đặt trong từ trường đều vuông góc "
   "với mặt phẳng nghiêng. Khi tốc độ thanh tăng dần thì gia tốc của thanh",
   ["tăng dần.", "giảm dần rồi tiến tới 0.",
    "không đổi.", "đổi chiều."],
   "B",
   "Tốc độ tăng làm suất điện động e = Bℓv tăng, dòng i = e/R tăng, lực từ cản F = Biℓ tăng. "
   "Hợp lực (thành phần trọng lực dọc mặt nghiêng trừ lực cản) giảm dần nên gia tốc giảm, "
   "tiến tới 0 khi thanh đạt tốc độ ổn định.",
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trượt trên hai ray nghiêng"),

mc("Một cuộn dây được nối kín và đặt gần một cuộn dây khác đang có dòng điện KHÔNG ĐỔI chạy qua. "
   "Trong cuộn thứ nhất",
   ["luôn có dòng điện cảm ứng.",
    "chỉ có dòng điện cảm ứng vào lúc đóng hoặc ngắt mạch của cuộn thứ hai.",
    "không bao giờ có dòng điện cảm ứng.",
    "có dòng điện cảm ứng tăng dần theo thời gian."],
   "B",
   "Dòng không đổi tạo từ thông không đổi nên không sinh dòng cảm ứng. Chỉ trong khoảnh khắc đóng "
   "hoặc ngắt mạch, dòng điện (và do đó từ thông) thay đổi rất nhanh, làm xuất hiện dòng cảm ứng.",
   "Điều kiện có dòng cảm ứng", TB),

mc("Một khung dây phẳng có diện tích S đặt trong từ trường đều B. Khi quay khung quanh một trục "
   "nằm trong mặt phẳng khung và vuông góc với B, từ thông qua khung biến thiên theo quy luật",
   ["tuyến tính theo thời gian.", "điều hoà theo thời gian.",
    "hàm mũ theo thời gian.", "không biến thiên."],
   "B",
   "Góc giữa pháp tuyến và B thay đổi đều: θ = ωt, nên Φ = B·S·cos(ωt) biến thiên điều hoà. "
   "Đây chính là nguyên tắc của máy phát điện xoay chiều.",
   "Máy phát điện xoay chiều", TB, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),

mc("Đặt một điện áp xoay chiều có giá trị hiệu dụng không đổi vào hai đầu một điện trở. "
   "Nếu tăng tần số của điện áp lên gấp đôi thì công suất tiêu thụ trên điện trở",
   ["tăng gấp đôi.", "không đổi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "Với mạch chỉ có điện trở thuần, P = U²/R chỉ phụ thuộc giá trị hiệu dụng và điện trở, "
   "hoàn toàn không phụ thuộc tần số.",
   "Mạch thuần trở", TB),

mc("Một khung dây hình vuông cạnh 30 cm đặt trong từ trường đều B = 0,20 T, mặt phẳng khung hợp với "
   "đường sức góc 30°. Từ thông qua khung bằng",
   ["9,0·10⁻³ Wb.", "1,56·10⁻² Wb.", "1,8·10⁻² Wb.", "4,5·10⁻³ Wb."],
   "A",
   "S = 0,30² = 0,090 m². Góc giữa pháp tuyến và B là θ = 90° − 30° = 60°.\n"
   "Φ = B·S·cosθ = 0,20 · 0,090 · 0,50 = 9,0·10⁻³ Wb.\n"
   "Giá trị 1,56·10⁻² Wb ứng với việc nhầm dùng cos30° thay cho cos60°.",
   "Từ thông – phân biệt góc", TB, fig="t_sd_khung_nghieng",
   cap="Khung dây nghiêng trong từ trường"),

mc("Một ống dây có độ tự cảm lớn được mắc nối tiếp với một bóng đèn và nguồn một chiều. "
   "Khi NGẮT mạch, đèn loé sáng rồi tắt hẳn. Hiện tượng đó là do",
   ["nguồn điện đột ngột tăng công suất.",
    "suất điện động tự cảm trong ống dây duy trì dòng điện thêm một lúc.",
    "điện trở của đèn giảm đột ngột.",
    "không khí bị ion hoá."],
   "B",
   "Khi ngắt mạch, dòng điện qua ống dây giảm rất nhanh nên từ thông qua chính nó biến thiên mạnh, "
   "sinh ra suất điện động cảm ứng lớn chống lại sự giảm đó, tiếp tục đẩy dòng qua đèn.",
   "Cảm ứng điện từ – hiện tượng thực tế", K),

mc("Trong thí nghiệm cân dòng điện, khi tăng cường độ dòng điện qua đoạn dây lên gấp ba thì độ thay "
   "đổi số chỉ của cân",
   ["không đổi.", "tăng gấp ba.", "tăng gấp chín.", "giảm ba lần."],
   "B",
   "Lực từ F = B·I·ℓ tỉ lệ thuận bậc nhất với I, mà độ thay đổi số chỉ của cân đúng bằng F/g. "
   "Vậy I tăng gấp ba thì độ thay đổi số chỉ cũng tăng gấp ba.",
   "Cân dòng điện", TB, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

mc("Một máy biến áp lí tưởng đang hoạt động. Nếu quấn thêm vào cuộn thứ cấp một số vòng dây và giữ "
   "nguyên điện áp sơ cấp thì",
   ["điện áp thứ cấp giảm.", "điện áp thứ cấp tăng.",
    "điện áp thứ cấp không đổi.", "tần số dòng điện thay đổi."],
   "B",
   "U₂ = U₁·N₂/N₁, trong đó U₁ và N₁ giữ nguyên. Tăng N₂ làm U₂ tăng theo tỉ lệ thuận. "
   "Tần số luôn bằng tần số nguồn và không đổi qua máy biến áp.",
   "Máy biến áp", TB, fig="t_sd_may_bien_ap", cap="Sơ đồ máy biến áp"),

mc("Đồ thị từ thông qua một vòng dây theo thời gian gồm bốn giai đoạn. Suất điện động cảm ứng "
   "trong giai đoạn (I) và giai đoạn (IV) có đặc điểm",
   ["cùng độ lớn và cùng chiều.", "cùng độ lớn nhưng ngược chiều.",
    "khác độ lớn và cùng chiều.", "khác độ lớn và ngược chiều."],
   "B",
   "Giai đoạn (I): từ thông tăng 0,4 Wb trong 2 s, độ dốc +0,2 Wb/s.\n"
   "Giai đoạn (IV): từ thông giảm 0,6 Wb trong 3 s, độ dốc −0,2 Wb/s.\n"
   "Hai độ dốc cùng độ lớn nhưng trái dấu nên suất điện động cùng độ lớn 0,2 V và ngược chiều.",
   "Đọc đồ thị từ thông", K, fig="t_dt_phi_t", cap="Từ thông theo thời gian"),

mc("Một dòng điện xoay chiều i = I₀cos(ωt) chạy qua điện trở R. Nhiệt lượng toả ra trong một chu kì "
   "bằng",
   ["R·I₀²·T.", "R·I₀²·T/2.", "R·I₀²·T/4.", "R·I₀·T."],
   "B",
   "Dùng giá trị hiệu dụng I = I₀/√2: Q = R·I²·T = R·(I₀²/2)·T = R·I₀²·T/2.",
   "Tác dụng nhiệt của dòng xoay chiều", K),

mc("Khi một khung dây kim loại đặc chuyển động trong từ trường không đều, trong khung xuất hiện "
   "dòng điện Foucault làm khung nóng lên. Năng lượng nhiệt đó lấy từ",
   ["nội năng có sẵn của khung.", "công của lực kéo khung chuyển động.",
    "năng lượng của từ trường bị tiêu hao.", "năng lượng hoá học trong kim loại."],
   "B",
   "Theo định luật Lenz, dòng Foucault tạo lực cản chuyển động. Muốn duy trì chuyển động phải "
   "tác dụng lực kéo, và công của lực kéo chính là nguồn của nhiệt lượng toả ra.",
   "Bảo toàn năng lượng trong cảm ứng điện từ", K, fig="t_sd_dong_fuco",
   cap="Dòng điện Foucault"),

mc("Một đoạn dây dẫn dài 12 cm mang dòng điện 2,5 A đặt trong từ trường đều. Khi dây hợp với đường "
   "sức góc 45° thì lực từ bằng 0,0636 N. Cảm ứng từ của từ trường xấp xỉ bằng",
   ["0,15 T.", "0,30 T.", "0,45 T.", "0,60 T."],
   "B",
   "B = F/(I·ℓ·sinα) = 0,0636/(2,5 · 0,12 · 0,7071) = 0,0636/0,2121 ≈ 0,30 T.",
   "Tìm B từ lực từ", TB),

mc("Hai khung dây kín giống hệt nhau, khung thứ nhất có điện trở gấp đôi khung thứ hai, cùng đặt "
   "trong một từ trường biến thiên như nhau. So sánh suất điện động và cường độ dòng điện cảm ứng:",
   ["suất điện động và dòng điện đều bằng nhau.",
    "suất điện động bằng nhau, dòng điện ở khung thứ nhất nhỏ bằng một nửa.",
    "suất điện động ở khung thứ nhất lớn gấp đôi.",
    "suất điện động ở khung thứ nhất nhỏ bằng một nửa."],
   "B",
   "Suất điện động chỉ phụ thuộc tốc độ biến thiên từ thông và số vòng dây, không phụ thuộc điện trở. "
   "Cường độ dòng điện i = e/R nên khung có điện trở gấp đôi cho dòng nhỏ bằng một nửa.",
   "Phân biệt e và i", TB),

mc("Một khung dây quay đều trong từ trường đều. Tại thời điểm từ thông qua khung bằng không thì "
   "suất điện động cảm ứng",
   ["cũng bằng không.", "đạt giá trị cực đại về độ lớn.",
    "bằng một nửa giá trị cực đại.", "không xác định."],
   "B",
   "Φ = Φ₀cos(ωt) còn e = ωΦ₀sin(ωt): hai đại lượng lệch pha nhau 90°. "
   "Khi Φ = 0 thì |sin| = 1 nên |e| đạt cực đại.",
   "Lệch pha giữa Φ và e", K),

mc("Điều nào sau đây là ĐÚNG với một nam châm đang rơi qua một ống đồng dày thẳng đứng?",
   ["Nam châm rơi tự do vì đồng không nhiễm từ.",
    "Nam châm rơi chậm hơn nhiều so với rơi tự do do dòng Foucault trong ống.",
    "Nam châm bị đẩy bật ngược lên trên.",
    "Nam châm dừng lại hẳn giữa ống."],
   "B",
   "Dù đồng không nhiễm từ, nó vẫn dẫn điện tốt nên trong thành ống xuất hiện dòng Foucault mạnh. "
   "Theo định luật Lenz, dòng này tạo lực cản làm nam châm rơi chậm hẳn lại nhưng không dừng hẳn.",
   "Dòng Foucault – hiện tượng thực tế", K, fig="t_sd_dong_fuco", cap="Dòng Foucault"),

mc("Một khung dây dẫn kín đặt trong từ trường đều có B tăng đều theo thời gian. "
   "Nếu tăng gấp đôi diện tích khung (giữ nguyên mọi yếu tố khác) thì suất điện động cảm ứng",
   ["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn."],
   "B",
   "Φ = B·S nên ΔΦ = ΔB·S tỉ lệ thuận với S. Suất điện động |e| = ΔΦ/Δt cũng tăng gấp đôi "
   "khi diện tích tăng gấp đôi.",
   "Các yếu tố ảnh hưởng tới e", TB),
],
P2=[
ds("Một thanh dẫn khối lượng 80 g, dài 40 cm trượt không ma sát trên hai ray đặt trên mặt phẳng "
   "nghiêng góc 30°, trong từ trường đều B = 0,50 T vuông góc với mặt phẳng nghiêng. "
   "Điện trở toàn mạch 0,40 Ω. Lấy g = 10 m/s².",
   [("Thành phần trọng lực kéo thanh dọc mặt nghiêng có độ lớn 0,40 N.", True,
     "Đúng. P·sin30° = 0,080 · 10 · 0,50 = 0,40 N."),
    ("Khi thanh trượt với tốc độ v, lực từ cản có độ lớn 0,10·v (đơn vị SI).", True,
     "Đúng. e = Bℓv = 0,50·0,40·v = 0,20v;  i = e/R = 0,20v/0,40 = 0,50v;  "
     "F = Biℓ = 0,50·0,50v·0,40 = 0,10v."),
    ("Tốc độ lớn nhất mà thanh đạt được là 4,0 m/s.", True,
     "Đúng. Tốc độ lớn nhất khi gia tốc bằng 0: 0,10·v = 0,40 ⇒ v = 4,0 m/s."),
    ("Ngay khi bắt đầu thả, lực từ cản có độ lớn 0,40 N.", False,
     "Sai. Lúc bắt đầu thả, v = 0 nên chưa có suất điện động, chưa có dòng điện và lực từ cản "
     "bằng 0. Thanh bắt đầu chuyển động với gia tốc lớn nhất a = g·sin30° = 5,0 m/s².")],
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trượt trên hai ray nghiêng"),

ds("Một khung dây phẳng hình chữ nhật đặt trong từ trường đều, mặt phẳng khung hợp với các đường "
   "sức từ góc 30°. Diện tích khung là 0,050 m², cảm ứng từ B = 0,40 T.",
   [("Góc giữa vectơ pháp tuyến của khung và vectơ cảm ứng từ bằng 60°.", True,
     "Đúng. Pháp tuyến vuông góc mặt phẳng khung nên góc cần tìm là 90° − 30° = 60°."),
    ("Từ thông qua khung bằng 0,010 Wb.", True,
     "Đúng. Φ = B·S·cos60° = 0,40 · 0,050 · 0,50 = 0,010 Wb."),
    ("Nếu quay khung sao cho mặt phẳng khung vuông góc với đường sức thì từ thông tăng lên 0,020 Wb.", True,
     "Đúng. Lúc đó θ = 0°, Φ = B·S = 0,40 · 0,050 = 0,020 Wb."),
    ("Nếu quay khung sao cho mặt phẳng khung song song với đường sức thì từ thông đạt cực đại.", False,
     "Sai. Mặt phẳng khung song song với B nghĩa là pháp tuyến vuông góc với B, θ = 90°, "
     "nên từ thông bằng 0 — giá trị nhỏ nhất chứ không phải cực đại.")],
   "Từ thông và góc", TB, fig="t_sd_khung_nghieng", cap="Khung dây nghiêng"),

ds("Xét một máy phát điện xoay chiều một pha đang hoạt động ổn định.",
   [("Suất điện động cảm ứng và từ thông qua khung lệch pha nhau 90°.", True,
     "Đúng. Φ biến thiên theo hàm cosin còn e theo hàm sin của cùng một pha ωt."),
    ("Khi mặt phẳng khung song song với đường sức thì suất điện động đạt cực đại.", True,
     "Đúng. Lúc đó từ thông bằng 0 và do lệch pha 90° nên suất điện động đạt cực đại."),
    ("Tăng số cặp cực của phần cảm mà giữ nguyên tốc độ quay thì tần số dòng điện tăng.", True,
     "Đúng. f = p·n nên tần số tỉ lệ thuận với số cặp cực p."),
    ("Suất điện động hiệu dụng của máy bằng suất điện động cực đại nhân với √2.", False,
     "Sai. E = E₀/√2, tức hiệu dụng nhỏ hơn cực đại √2 lần chứ không lớn hơn.")],
   "Máy phát điện xoay chiều", TB, fig="t_sd_may_phat", cap="Nguyên lí máy phát điện"),

ds("Một nam châm được thả rơi thẳng đứng, đi qua một vòng dây dẫn kín đặt nằm ngang.",
   [("Khi nam châm đang lại gần vòng dây, lực từ tác dụng lên nam châm hướng lên trên.", True,
     "Đúng. Định luật Lenz: dòng cảm ứng chống lại sự lại gần nên đẩy nam châm ra, "
     "tức lực hướng lên, ngược chiều chuyển động."),
    ("Khi nam châm đã đi qua và đang ra xa vòng dây, lực từ tác dụng lên nam châm hướng xuống dưới.", False,
     "Sai. Lúc ra xa, dòng cảm ứng chống lại sự ra xa nên HÚT nam châm lại, tức lực hướng LÊN — "
     "vẫn ngược chiều chuyển động. Ở cả hai giai đoạn lực từ đều cản trở nam châm."),
    ("Tại thời điểm nam châm nằm đúng mặt phẳng vòng dây, dòng điện cảm ứng đổi chiều.", True,
     "Đúng. Đó là lúc từ thông qua vòng dây đạt cực đại và bắt đầu chuyển từ tăng sang giảm."),
    ("Cơ năng mà nam châm mất đi so với rơi tự do đã chuyển thành nhiệt toả ra trên vòng dây.", True,
     "Đúng. Đây là biểu hiện của định luật bảo toàn năng lượng trong hiện tượng cảm ứng điện từ.")],
   "Định luật Lenz – nam châm rơi", K, fig="t_sd_nam_cham_roi",
   cap="Nam châm rơi qua vòng dây kín"),
],
P3=[
sa("Một thanh dẫn khối lượng 100 g, dài 50 cm trượt không ma sát trên hai ray đặt trên mặt phẳng "
   "nghiêng góc 30°, trong từ trường đều B = 0,40 T vuông góc với mặt phẳng nghiêng. "
   "Điện trở toàn mạch 0,50 Ω. Tốc độ lớn nhất thanh đạt được bằng bao nhiêu mét trên giây? "
   "Lấy g = 10 m/s².",
   "6,25",
   "Thành phần trọng lực dọc mặt nghiêng: P·sin30° = 0,100 · 10 · 0,50 = 0,50 N.\n"
   "Khi thanh chạy với tốc độ v:  e = Bℓv = 0,40·0,50·v = 0,20v;  i = e/R = 0,40v;\n"
   "lực từ cản  F = Biℓ = 0,40 · 0,40v · 0,50 = 0,080v.\n"
   "Tốc độ lớn nhất đạt được khi gia tốc bằng 0, tức lực từ cản cân bằng thành phần trọng lực:\n"
   "0,080·v = 0,50 ⇒ v = 6,25 m/s.",
   "Thanh dẫn trên mặt nghiêng", K),

sa("Một khung dây phẳng diện tích 0,040 m² đặt trong từ trường đều B = 0,30 T, mặt phẳng khung hợp "
   "với đường sức góc 60°. Từ thông qua khung bằng bao nhiêu vêbe (làm tròn đến chữ số thập phân "
   "thứ tư)? Lấy √3 ≈ 1,732.",
   "0,0104",
   "Góc giữa pháp tuyến và B: θ = 90° − 60° = 30°.\n"
   "Φ = B·S·cos30° = 0,30 · 0,040 · 0,866 = 0,012 · 0,866 ≈ 0,01039 ≈ 0,0104 Wb.",
   "Từ thông – phân biệt góc", TB),

sa("Một dòng điện xoay chiều có cường độ cực đại 6,0 A chạy qua điện trở 20 Ω. "
   "Nhiệt lượng toả ra trên điện trở trong 2,0 phút bằng bao nhiêu kilôjun?",
   "43,2",
   "Cường độ hiệu dụng: I = I₀/√2 nên I² = I₀²/2 = 36/2 = 18 A².\n"
   "t = 2,0 phút = 120 s.\n"
   "Q = R·I²·t = 20 · 18 · 120 = 43 200 J = 43,2 kJ.",
   "Tác dụng nhiệt của dòng xoay chiều", K),

sa("Hai dây dẫn thẳng song song dài, cách nhau 20 cm, mang hai dòng điện cùng chiều có cường độ "
   "lần lượt 4,0 A và 6,0 A. Cảm ứng từ tổng hợp bằng không tại điểm nằm trên đường nối hai dây, "
   "cách dây mang dòng 4,0 A một khoảng bao nhiêu centimét?",
   "8",
   "Điểm triệt tiêu phải nằm GIỮA hai dây (vì hai dòng cùng chiều).\n"
   "Gọi khoảng cách tới dây 4,0 A là x thì tới dây 6,0 A là (20 − x).\n"
   "Điều kiện cân bằng: 4,0/x = 6,0/(20 − x) ⇒ 4,0(20 − x) = 6,0x ⇒ 80 = 10x ⇒ x = 8,0 cm.",
   "Từ trường của hai dòng điện", K),

sa("Một máy biến áp lí tưởng có hai cuộn dây với số vòng lần lượt 1200 và 300 vòng. "
   "Mắc cuộn 300 vòng vào mạng điện xoay chiều 110 V. Điện áp hiệu dụng ở hai đầu cuộn kia bằng "
   "bao nhiêu vôn?",
   "440",
   "Ở đây cuộn 300 vòng đóng vai trò SƠ CẤP, cuộn 1200 vòng là thứ cấp.\n"
   "U₂ = U₁·N₂/N₁ = 110 · 1200/300 = 110 · 4 = 440 V.",
   "Máy biến áp – đọc kĩ đề", TB),

sa("Một vòng dây kín điện trở 0,20 Ω đặt vuông góc với từ trường đều. Cảm ứng từ giảm đều từ 0,50 T "
   "về 0 trong 0,40 s, diện tích vòng dây là 0,080 m². Nhiệt lượng toả ra trên vòng dây trong thời "
   "gian đó bằng bao nhiêu milijun (làm tròn đến hàng đơn vị)?",
   "20",
   "|ΔΦ| = ΔB·S = 0,50 · 0,080 = 0,040 Wb.\n"
   "|e| = 0,040/0,40 = 0,10 V;  i = 0,10/0,20 = 0,50 A.\n"
   "Q = R·i²·t = 0,20 · 0,50² · 0,40 = 0,20 · 0,25 · 0,40 = 0,020 J = 20 mJ.",
   "Năng lượng trong cảm ứng điện từ", K),
])


# =====================================================================  ĐỀ 7
DE7 = dict(
ma="12C3-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Bài toán tổng hợp lực từ – cơ học, khung dây trên lò xo, truyền tải hai mức điện áp",
P1=[
mc("Một thanh dẫn nằm ngang được treo bằng hai lò xo giống nhau trong từ trường đều nằm ngang, "
   "vuông góc với thanh. Khi chưa có dòng điện mỗi lò xo giãn 4,0 cm; khi cho dòng điện qua thanh "
   "mỗi lò xo giãn 5,0 cm. Tỉ số giữa lực từ và trọng lượng thanh bằng",
   ["0,20.", "0,25.", "0,50.", "0,80."],
   "B",
   "Chưa có dòng: 2k·(4,0) = P.  Có dòng: 2k·(5,0) = P + F.\n"
   "Lấy hiệu hai phương trình: 2k·(1,0) = F.\n"
   "Vậy F/P = 1,0/4,0 = 0,25. Không cần biết k hay khối lượng thanh.",
   "Thanh dẫn treo trên lò xo", K, fig="t_sd_thanh_lo_xo",
   cap="Thanh dẫn treo trên hai lò xo"),

mc("Một khung dây hình vuông cạnh a chuyển động đều với tốc độ v đi vào một vùng từ trường đều B "
   "có bề rộng d > a. Đồ thị cường độ dòng điện cảm ứng theo thời gian có dạng",
   ["một đường hình sin liên tục.",
    "hai xung hình chữ nhật ngược dấu, cách nhau một khoảng không có dòng.",
    "một xung tam giác duy nhất.",
    "một đường thẳng nằm ngang khác không."],
   "B",
   "Lúc khung đi vào, dòng không đổi trong suốt thời gian a/v; khi khung nằm trọn trong vùng, "
   "dòng bằng 0; lúc đi ra, dòng lại không đổi nhưng ngược chiều. "
   "Vậy đồ thị gồm hai xung chữ nhật ngược dấu.",
   "Khung dây ra vào vùng từ trường", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường đều"),

mc("Truyền một công suất P đi xa trên đường dây có điện trở R. Ở điện áp U₁ hiệu suất truyền tải là "
   "80 %. Muốn hiệu suất đạt 95 % thì phải tăng điện áp lên gấp",
   ["1,5 lần.", "2,0 lần.", "2,5 lần.", "4,0 lần."],
   "B",
   "Hao phí tỉ lệ nghịch với U². Hao phí lúc đầu chiếm 20 %, lúc sau chiếm 5 %, tức giảm 4 lần.\n"
   "U² tăng 4 lần ⇒ U tăng 2,0 lần.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai",
   cap="Truyền tải điện năng đi xa"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp N₁ vòng, cuộn thứ cấp N₂ vòng. Nếu quấn thêm 60 vòng "
   "vào cuộn thứ cấp thì điện áp thứ cấp tăng từ 24 V lên 30 V (điện áp sơ cấp không đổi). "
   "Số vòng ban đầu của cuộn thứ cấp là",
   ["180 vòng.", "240 vòng.", "300 vòng.", "120 vòng."],
   "B",
   "Điện áp thứ cấp tỉ lệ thuận với số vòng: N₂/(N₂ + 60) = 24/30 = 0,80.\n"
   "N₂ = 0,80·N₂ + 48 ⇒ 0,20·N₂ = 48 ⇒ N₂ = 240 vòng.",
   "Máy biến áp – bài toán ngược", K, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một vòng dây kín đặt trong từ trường đều B. Người ta bóp méo vòng dây từ hình tròn bán kính "
   "10 cm thành hình vuông có cùng chu vi. Từ thông qua vòng dây",
   ["tăng lên.", "giảm đi.", "không đổi.", "bằng không."],
   "B",
   "Chu vi không đổi: 2π·0,10 ≈ 0,628 m. Hình tròn có S = π·0,10² ≈ 0,0314 m²; "
   "hình vuông cạnh 0,628/4 = 0,157 m có S ≈ 0,0247 m². Diện tích giảm nên từ thông giảm. "
   "Với cùng chu vi, hình tròn luôn có diện tích lớn nhất.",
   "Từ thông và diện tích", K),

mc("Đặt điện áp xoay chiều có giá trị hiệu dụng 120 V vào hai đầu đoạn mạch chỉ chứa điện trở. "
   "Trong 1 phút mạch tiêu thụ 14,4 kJ điện năng. Điện trở của mạch bằng",
   ["30 Ω.", "60 Ω.", "90 Ω.", "120 Ω."],
   "B",
   "Công suất: P = W/t = 14 400/60 = 240 W.\n"
   "R = U²/P = 120²/240 = 14 400/240 = 60 Ω.",
   "Mạch thuần trở", TB),

mc("Một khung dây phẳng 200 vòng quay đều trong từ trường đều B = 0,10 T quanh trục vuông góc với B. "
   "Diện tích mỗi vòng 50 cm². Suất điện động hiệu dụng của khung là 22,2 V. "
   "Tần số quay của khung xấp xỉ",
   ["25 Hz.", "50 Hz.", "60 Hz.", "100 Hz."],
   "B",
   "E₀ = E·√2 = 22,2 · 1,414 ≈ 31,4 V.\n"
   "Từ E₀ = ω·N·B·S ⇒ ω = 31,4/(200 · 0,10 · 5,0·10⁻³) = 31,4/0,10 = 314 rad/s.\n"
   "f = ω/(2π) = 314/6,283 ≈ 50 Hz.",
   "Máy phát – bài toán ngược", K),

mc("Hai dây dẫn thẳng song song dài mang hai dòng điện NGƯỢC chiều cùng cường độ I, cách nhau "
   "khoảng d. Cảm ứng từ tại điểm nằm chính giữa hai dây",
   ["bằng không.", "bằng hai lần cảm ứng từ do một dây gây ra.",
    "bằng cảm ứng từ do một dây gây ra.", "phụ thuộc chiều dài dây."],
   "B",
   "Tại điểm giữa, hai vectơ cảm ứng từ do hai dòng ngược chiều gây ra lại CÙNG hướng, "
   "nên chúng cộng lại: B = 2·B₁. Nếu hai dòng cùng chiều thì tại điểm giữa chúng triệt tiêu nhau.",
   "Từ trường của hai dòng điện", K),

mc("Một thanh dẫn nằm ngang dài 60 cm, khối lượng 120 g, trượt trên hai ray nằm ngang có hệ số ma "
   "sát 0,25, trong từ trường đều thẳng đứng B = 0,40 T. Cho dòng điện 8,0 A qua thanh. "
   "Gia tốc của thanh bằng (g = 10 m/s²)",
   ["8,0 m/s².", "13,5 m/s².", "16,0 m/s².", "10,5 m/s²."],
   "B",
   "Lực từ: F = B·I·ℓ = 0,40 · 8,0 · 0,60 = 1,92 N.\n"
   "Lực ma sát: F(ms) = μ·m·g = 0,25 · 0,120 · 10 = 0,30 N.\n"
   "a = (1,92 − 0,30)/0,120 = 1,62/0,120 = 13,5 m/s².",
   "Lực từ kết hợp động lực học", K, fig="t_sd_ray_ngang",
   cap="Thanh dẫn trên hai ray nằm ngang"),

mc("Trong một máy biến áp, người ta quấn NHẦM một số vòng của cuộn thứ cấp theo chiều ngược lại. "
   "So với thiết kế đúng, điện áp thứ cấp sẽ",
   ["không đổi.", "nhỏ hơn.", "lớn hơn.", "bằng không."],
   "B",
   "Các vòng quấn ngược sinh suất điện động ngược pha, triệt tiêu bớt suất điện động của các vòng "
   "quấn đúng. Số vòng có hiệu lực giảm đi 2n (n là số vòng quấn ngược), nên điện áp thứ cấp nhỏ hơn.",
   "Máy biến áp – tình huống thực tế", K, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một vòng dây dẫn kín đặt trong từ trường biến thiên đều theo thời gian. Nếu thay vòng dây bằng "
   "vòng khác cùng kích thước nhưng làm bằng vật liệu có điện trở suất lớn gấp đôi thì nhiệt lượng "
   "toả ra trong cùng thời gian",
   ["không đổi.", "giảm một nửa.", "tăng gấp đôi.", "giảm bốn lần."],
   "B",
   "Suất điện động e không đổi (chỉ phụ thuộc từ thông). Điện trở tăng gấp đôi nên "
   "Q = e²t/R giảm một nửa.",
   "Năng lượng trong cảm ứng điện từ", K),

mc("Một khung dây quay đều trong từ trường đều với tần số f. Nếu đồng thời tăng tần số quay lên "
   "gấp đôi và giảm diện tích khung còn một nửa thì suất điện động cực đại",
   ["giảm một nửa.", "không đổi.", "tăng gấp đôi.", "tăng gấp bốn."],
   "B",
   "E₀ = ω·N·B·S = 2πf·N·B·S. Tần số tăng gấp đôi làm E₀ tăng 2 lần, diện tích giảm một nửa làm "
   "E₀ giảm 2 lần. Hai tác động bù trừ nhau nên E₀ không đổi.",
   "Máy phát – phân tích tỉ lệ", TB),

mc("Đặt một vòng dây nhôm kín lên đầu một ống dây rồi đóng mạch cho dòng điện xoay chiều chạy qua "
   "ống dây. Vòng nhôm sẽ",
   ["đứng yên.", "bị bắn vọt lên.", "bị hút chặt xuống.", "quay tròn tại chỗ."],
   "B",
   "Từ trường biến thiên tạo dòng cảm ứng trong vòng nhôm; theo định luật Lenz, dòng này luôn "
   "chống lại sự biến thiên từ thông nên trung bình vòng nhôm bị ĐẨY ra xa ống dây, bắn vọt lên. "
   "Đây là thí nghiệm vòng nhảy Thomson kinh điển.",
   "Định luật Lenz – hiện tượng thực tế", K),

mc("Một đường dây tải điện có điện trở R truyền công suất P. Khi điện áp truyền tải là U thì hiệu "
   "suất là 90 %. Nếu giữ nguyên điện áp nhưng tăng công suất truyền lên gấp đôi thì hiệu suất",
   ["vẫn là 90 %.", "còn 80 %.", "còn 45 %.", "tăng lên 95 %."],
   "B",
   "Hao phí ΔP = R·P²/U² tỉ lệ với P². P tăng gấp đôi thì ΔP tăng gấp bốn.\n"
   "Ban đầu ΔP = 0,10·P. Sau đó ΔP' = 4·(0,10·P) = 0,40·P, trong khi công suất truyền là 2P.\n"
   "Tỉ lệ hao phí: 0,40P/2P = 20 % ⇒ hiệu suất còn 80 %.",
   "Hiệu suất truyền tải", K),

mc("Một khung dây dẫn kín, phẳng, nằm trong mặt phẳng thẳng đứng, được đặt trong từ trường đều nằm "
   "ngang. Khi khung rơi tự do theo phương thẳng đứng (vẫn nằm trọn trong vùng từ trường), "
   "trong khung",
   ["có dòng điện cảm ứng tăng dần.", "không có dòng điện cảm ứng.",
    "có dòng điện cảm ứng không đổi.", "có dòng điện cảm ứng đổi chiều liên tục."],
   "B",
   "Từ trường đều và khung nằm trọn bên trong nên B, S và góc đều không đổi. Từ thông không biến "
   "thiên nên không có dòng cảm ứng, bất kể khung chuyển động nhanh chậm thế nào.",
   "Điều kiện có dòng cảm ứng", TB),

mc("Một đoạn dây dẫn thẳng dài ℓ đặt trong từ trường đều B, mang dòng điện I. Khi quay dây trong "
   "mặt phẳng chứa B, lực từ tác dụng lên dây biến thiên theo góc α giữa dây và B. "
   "Đồ thị F theo α trên khoảng từ 0° đến 180° có dạng",
   ["đường thẳng tăng.", "một nửa đường hình sin, cực đại tại α = 90°.",
    "đường hypebol.", "đường nằm ngang."],
   "B",
   "F = B·I·ℓ·sinα. Trên khoảng 0° đến 180°, hàm sinα tăng từ 0 lên 1 rồi giảm về 0, "
   "tạo thành một nửa đường hình sin với cực đại tại α = 90°.",
   "Vai trò của góc α", TB, fig="t_sd_goc_alpha", cap="Dây hợp góc α với đường sức"),

mc("Một cuộn dây gồm 1000 vòng có điện trở 5,0 Ω, đặt trong từ trường đều vuông góc mặt phẳng cuộn. "
   "Diện tích mỗi vòng là 10 cm². Muốn dòng điện cảm ứng đạt 0,40 A thì tốc độ biến thiên của cảm "
   "ứng từ phải bằng",
   ["1,0 T/s.", "2,0 T/s.", "4,0 T/s.", "0,50 T/s."],
   "B",
   "e = i·R = 0,40 · 5,0 = 2,0 V.\n"
   "e = N·S·(ΔB/Δt) ⇒ ΔB/Δt = 2,0/(1000 · 1,0·10⁻³) = 2,0/1,0 = 2,0 T/s.",
   "Faraday – bài toán ngược", K),

mc("Trong máy phát điện xoay chiều ba pha, ba suất điện động có đặc điểm",
   ["cùng pha nhau.", "lệch pha nhau 120°.",
    "lệch pha nhau 90°.", "khác tần số nhau."],
   "B",
   "Ba cuộn dây đặt lệch nhau 120° trên vành stato nên ba suất điện động cùng biên độ, cùng tần số "
   "nhưng lệch pha nhau 2π/3 rad tức 120°.",
   "Máy phát ba pha", TB),
],
P2=[
ds("Một khung dây hình vuông cạnh 25 cm, điện trở 0,50 Ω, chuyển động đều với tốc độ 5,0 m/s theo "
   "phương vuông góc với biên của một vùng từ trường đều B = 0,60 T rộng 80 cm. "
   "Các đường sức vuông góc với mặt phẳng khung.",
   [("Thời gian khung đi hết vùng từ trường (từ lúc cạnh trước chạm mép vào tới lúc cạnh sau rời "
     "mép ra) là 0,21 s.", True,
     "Đúng. Quãng đường cần đi là d + a = 0,80 + 0,25 = 1,05 m; thời gian = 1,05/5,0 = 0,21 s."),
    ("Trong lúc khung đang đi vào, cường độ dòng điện cảm ứng bằng 1,5 A.", True,
     "Đúng. e = B·a·v = 0,60 · 0,25 · 5,0 = 0,75 V; i = 0,75/0,50 = 1,5 A."),
    ("Tổng thời gian có dòng điện cảm ứng trong khung là 0,10 s.", True,
     "Đúng. Dòng chỉ xuất hiện lúc vào và lúc ra, mỗi lần kéo dài a/v = 0,25/5,0 = 0,05 s, "
     "tổng cộng 0,10 s."),
    ("Trong lúc khung nằm trọn trong vùng từ trường, cường độ dòng cảm ứng vẫn bằng 1,5 A.", False,
     "Sai. Lúc đó từ thông không đổi nên không có dòng cảm ứng, cường độ bằng 0.")],
   "Khung dây ra vào vùng từ trường", K, fig="t_sd_khung_vao_B",
   cap="Khung dây đi vào vùng từ trường đều"),

ds("Một thanh dẫn nằm ngang dài 20 cm, khối lượng 50 g được treo cân bằng bởi hai lò xo giống nhau "
   "có độ cứng k = 25 N/m mỗi chiếc, đặt trong từ trường đều nằm ngang vuông góc với thanh, "
   "B = 0,50 T. Lấy g = 10 m/s².",
   [("Khi chưa có dòng điện, mỗi lò xo giãn 1,0 cm.", True,
     "Đúng. Hai lò xo cùng đỡ trọng lượng: 2k·Δℓ = mg ⇒ Δℓ = 0,50/(2·25) = 0,010 m = 1,0 cm."),
    ("Khi cho dòng điện 2,0 A chạy qua thanh, lực từ tác dụng lên thanh có độ lớn 0,20 N.", True,
     "Đúng. F = B·I·ℓ = 0,50 · 2,0 · 0,20 = 0,20 N."),
    ("Nếu lực từ hướng xuống thì mỗi lò xo giãn thêm 0,40 cm.", True,
     "Đúng. Độ giãn thêm: Δ = F/(2k) = 0,20/50 = 0,0040 m = 0,40 cm."),
    ("Nếu đổi chiều dòng điện thì độ giãn của mỗi lò xo tăng thêm 0,40 cm nữa.", False,
     "Sai. Đổi chiều dòng điện thì lực từ đổi chiều, hướng lên, nên lò xo GIÃN ÍT ĐI 0,40 cm "
     "so với khi chưa có dòng, tức còn 0,60 cm.")],
   "Thanh dẫn treo trên lò xo", K, fig="t_sd_thanh_lo_xo",
   cap="Thanh dẫn treo trên hai lò xo"),

ds("Một trạm phát điện truyền công suất 2,0 MW tới nơi tiêu thụ qua đường dây có điện trở tổng 8,0 Ω. "
   "Hệ số công suất bằng 1.",
   [("Nếu truyền ở điện áp 20 kV thì công suất hao phí là 80 kW.", True,
     "Đúng. I = 2,0·10⁶/(20·10³) = 100 A; ΔP = 8,0 · 100² = 80 000 W = 80 kW."),
    ("Hiệu suất truyền tải ở 20 kV là 96 %.", True,
     "Đúng. H = (2000 − 80)/2000 = 1920/2000 = 0,96 = 96 %."),
    ("Muốn nâng hiệu suất lên 99 % thì phải tăng điện áp lên 40 kV.", True,
     "Đúng. Hao phí phải giảm từ 4 % xuống 1 %, tức giảm 4 lần, nên U phải tăng √4 = 2 lần: "
     "từ 20 kV lên 40 kV."),
    ("Ở điện áp 40 kV, cường độ dòng điện trên đường dây vẫn là 100 A.", False,
     "Sai. I = P/U = 2,0·10⁶/(40·10³) = 50 A, tức giảm còn một nửa. Chính điều này làm hao phí "
     "giảm bốn lần.")],
   "Truyền tải điện năng", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

ds("Xét một khung dây dẫn kín mang dòng điện đặt trong từ trường đều.",
   [("Tổng hợp lực từ tác dụng lên khung bằng không.", True,
     "Đúng. Trong từ trường ĐỀU, các lực từ trên các cạnh đối diện triệt tiêu nhau từng đôi một "
     "nên hợp lực bằng 0; khung không tịnh tiến."),
    ("Momen lực từ tác dụng lên khung có thể khác không.", True,
     "Đúng. Tuy hợp lực bằng 0 nhưng hai lực trên hai cạnh đối diện có thể tạo thành ngẫu lực "
     "làm khung quay."),
    ("Momen lực từ đạt cực đại khi mặt phẳng khung song song với các đường sức từ.", True,
     "Đúng. Lúc đó cánh tay đòn của ngẫu lực lớn nhất."),
    ("Khi mặt phẳng khung vuông góc với đường sức, khung ở vị trí cân bằng nên momen cực đại.", False,
     "Sai. Vị trí cân bằng ứng với momen bằng KHÔNG, không phải cực đại. Hai lực lúc đó cùng nằm "
     "trên một đường thẳng nên không tạo ngẫu lực.")],
   "Momen lực từ tác dụng lên khung dây", K),
],
P3=[
sa("Một thanh dẫn dài 40 cm, khối lượng 150 g nằm trên hai ray nằm ngang có hệ số ma sát 0,20, "
   "đặt trong từ trường đều thẳng đứng B = 0,50 T. Cho dòng điện 6,0 A chạy qua thanh. "
   "Gia tốc của thanh bằng bao nhiêu mét trên giây bình phương? Lấy g = 10 m/s².",
   "6",
   "Lực từ: F = B·I·ℓ = 0,50 · 6,0 · 0,40 = 1,20 N.\n"
   "Lực ma sát: F(ms) = μ·m·g = 0,20 · 0,150 · 10 = 0,30 N.\n"
   "a = (1,20 − 0,30)/0,150 = 0,90/0,150 = 6,0 m/s².",
   "Lực từ và động lực học", K),

sa("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi. Khi cuộn thứ cấp có 100 vòng thì điện áp "
   "thứ cấp là 20 V. Muốn điện áp thứ cấp đạt 50 V thì phải quấn thêm bao nhiêu vòng vào cuộn thứ cấp?",
   "150",
   "Điện áp thứ cấp tỉ lệ thuận với số vòng: N₂' = 100 · 50/20 = 250 vòng.\n"
   "Số vòng cần quấn thêm: 250 − 100 = 150 vòng.",
   "Máy biến áp – bài toán ngược", K),

sa("Một khung dây hình vuông cạnh 20 cm, điện trở 0,40 Ω, chuyển động đều với tốc độ 4,0 m/s đi ra "
   "khỏi một vùng từ trường đều B = 0,50 T theo phương vuông góc với biên vùng. "
   "Nhiệt lượng toả ra trên khung trong suốt quá trình đi ra bằng bao nhiêu milijun?",
   "20",
   "Suất điện động khi đi ra: e = B·a·v = 0,50 · 0,20 · 4,0 = 0,40 V.\n"
   "Dòng điện: i = 0,40/0,40 = 1,0 A.\n"
   "Thời gian đi ra: t = a/v = 0,20/4,0 = 0,050 s.\n"
   "Q = R·i²·t = 0,40 · 1,0² · 0,050 = 0,020 J = 20 mJ.",
   "Năng lượng trong cảm ứng điện từ", K),

sa("Một đoạn dây dẫn thẳng dài 25 cm mang dòng điện 8,0 A đặt vuông góc với từ trường đều "
   "B = 0,40 T. Dưới tác dụng của lực từ, đoạn dây dịch chuyển được 12 cm theo đúng hướng của lực. "
   "Công của lực từ bằng bao nhiêu jun?",
   "0,096",
   "Lực từ: F = B·I·ℓ = 0,40 · 8,0 · 0,25 = 0,80 N.\n"
   "Công: A = F·s = 0,80 · 0,12 = 0,096 J.",
   "Công của lực từ", K),

sa("Một cuộn dây 800 vòng, điện trở 4,0 Ω, diện tích mỗi vòng 25 cm², đặt vuông góc với từ trường "
   "đều. Muốn cường độ dòng điện cảm ứng trong cuộn đạt 0,50 A thì cảm ứng từ phải biến thiên với "
   "tốc độ bao nhiêu tesla trên giây?",
   "1",
   "e = i·R = 0,50 · 4,0 = 2,0 V.\n"
   "S = 25 cm² = 2,5·10⁻³ m².\n"
   "e = N·S·(ΔB/Δt) ⇒ ΔB/Δt = 2,0/(800 · 2,5·10⁻³) = 2,0/2,0 = 1,0 T/s.",
   "Faraday – bài toán ngược", K),

sa("Một thanh dẫn nằm ngang được treo bằng hai lò xo giống nhau trong từ trường đều nằm ngang, "
   "vuông góc với thanh. Khi chưa có dòng điện mỗi lò xo giãn 6,0 cm. Cho dòng điện chạy qua theo "
   "chiều làm lực từ hướng lên thì mỗi lò xo chỉ còn giãn 4,5 cm. Lực từ bằng bao nhiêu phần trăm "
   "trọng lượng của thanh?",
   "25",
   "Chưa có dòng: 2k·6,0 = P.  Có dòng, lực từ hướng lên: 2k·4,5 = P − F.\n"
   "Lấy hiệu: 2k·1,5 = F.\n"
   "F/P = 1,5/6,0 = 0,25 = 25 %.",
   "Thanh dẫn treo trên lò xo", K, fig="t_sd_thanh_lo_xo", cap="Thanh dẫn treo trên hai lò xo"),
])


# =====================================================================  ĐỀ 8
DE8 = dict(
ma="12C3-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Tốc độ giới hạn, máy biến áp quấn ngược, truyền tải ngược, khung quay theo thời gian",
P1=[
mc("Một khung dây dẫn kín hình vuông cạnh a, khối lượng m, điện trở R rơi thẳng đứng và đang đi ra "
   "khỏi biên ngang của một vùng từ trường đều B nằm ngang vuông góc mặt phẳng khung. "
   "Tốc độ giới hạn của khung bằng",
   ["m·g·R/(B·a).", "m·g·R/(B²·a²).", "B²·a²/(m·g·R).", "m·g/(B·a·R)."],
   "B",
   "Ở tốc độ giới hạn, lực từ cản cân bằng trọng lực:  B²a²v/R = m·g  ⇒  v = m·g·R/(B²a²).\n"
   "Có thể kiểm tra bằng thứ nguyên hoặc bằng nhận xét: B càng lớn thì khung rơi càng chậm, "
   "phù hợp với việc B² nằm ở mẫu số.",
   "Tốc độ giới hạn của khung rơi", K),

mc("Một khung dây vuông cạnh 10 cm, khối lượng 20 g, điện trở 0,10 Ω rơi thẳng đứng đi ra khỏi "
   "vùng từ trường đều B = 0,50 T. Tốc độ giới hạn của khung bằng (g = 10 m/s²)",
   ["4,0 m/s.", "8,0 m/s.", "16,0 m/s.", "2,0 m/s."],
   "B",
   "v = m·g·R/(B²a²) = 0,020 · 10 · 0,10 / (0,50² · 0,10²)\n"
   "= 0,020 / (0,25 · 0,010) = 0,020/2,5·10⁻³ = 8,0 m/s.",
   "Tốc độ giới hạn của khung rơi", K),

mc("Một máy biến áp có cuộn sơ cấp 1000 vòng và cuộn thứ cấp theo thiết kế là 200 vòng. "
   "Do sơ suất, thợ quấn n vòng của cuộn thứ cấp theo chiều ngược lại. Đặt vào sơ cấp điện áp 220 V "
   "thì đo được điện áp thứ cấp 33 V. Số vòng bị quấn ngược là",
   ["15 vòng.", "25 vòng.", "50 vòng.", "35 vòng."],
   "B",
   "n vòng quấn ngược triệt tiêu n vòng quấn đúng nên số vòng có hiệu lực là 200 − 2n.\n"
   "(200 − 2n)/1000 = 33/220 = 0,15 ⇒ 200 − 2n = 150 ⇒ n = 25 vòng.",
   "Máy biến áp – quấn ngược", K, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một trạm phát truyền công suất 5,0 MW ở điện áp 25 kV, hiệu suất truyền tải 95 %. "
   "Điện trở tổng của đường dây bằng",
   ["3,125 Ω.", "6,25 Ω.", "12,5 Ω.", "25,0 Ω."],
   "B",
   "Hao phí: ΔP = 5 % · 5,0·10⁶ = 2,5·10⁵ W.\n"
   "Cường độ dòng điện: I = P/U = 5,0·10⁶/(25·10³) = 200 A.\n"
   "R = ΔP/I² = 2,5·10⁵/200² = 2,5·10⁵/4,0·10⁴ = 6,25 Ω.",
   "Truyền tải – bài toán ngược", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây quay đều tạo ra suất điện động e = E₀·sin(100πt) (V). Khoảng thời gian ngắn nhất "
   "kể từ lúc e = 0 đến lúc |e| = E₀/2 bằng",
   ["1/300 s.", "1/600 s.", "1/1200 s.", "1/100 s."],
   "B",
   "Từ sin(100πt) = 0,5 ⇒ 100πt = π/6 ⇒ t = 1/600 s.\n"
   "Kiểm tra bằng chu kì: T = 2π/(100π) = 0,02 s và t = T/12 = 0,02/12 = 1/600 s.",
   "Suất điện động theo thời gian", K),

mc("Một thanh dẫn khối lượng 200 g, dài 50 cm trượt trên hai ray nghiêng góc 37° (sin37° = 0,60; "
   "cos37° = 0,80), hệ số ma sát 0,20, trong từ trường đều B = 0,40 T vuông góc mặt phẳng nghiêng. "
   "Điện trở toàn mạch 0,10 Ω. Tốc độ lớn nhất mà thanh đạt được là (g = 10 m/s²)",
   ["1,1 m/s.", "2,2 m/s.", "3,0 m/s.", "4,4 m/s."],
   "B",
   "Thành phần trọng lực kéo xuống: m·g·sin37° = 0,200 · 10 · 0,60 = 1,20 N.\n"
   "Lực ma sát: μ·m·g·cos37° = 0,20 · 0,200 · 10 · 0,80 = 0,32 N.\n"
   "Hợp lực kéo còn lại: 1,20 − 0,32 = 0,88 N.\n"
   "Lực từ cản: F = B²ℓ²v/R = (0,40² · 0,50²/0,10)·v = (0,16 · 0,25/0,10)·v = 0,40v.\n"
   "Tốc độ lớn nhất: 0,40·v = 0,88 ⇒ v = 2,2 m/s.",
   "Thanh dẫn trên mặt nghiêng có ma sát", K, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trên hai ray nghiêng"),

mc("Trong một chu kì của dòng điện xoay chiều i = I₀·cos(ωt), khoảng thời gian mà độ lớn cường độ "
   "dòng điện không nhỏ hơn I₀/2 chiếm",
   ["một nửa chu kì.", "hai phần ba chu kì.",
    "một phần ba chu kì.", "ba phần tư chu kì."],
   "B",
   "|cos(ωt)| ≥ 0,5 khi pha nằm ngoài các khoảng quanh ±π/2. Trong mỗi nửa chu kì, điều kiện "
   "thoả mãn trên hai đoạn tổng cộng 2π/3 rad trong tổng π rad, tức tỉ lệ 2/3. "
   "Vậy cả chu kì chiếm hai phần ba.",
   "Đọc đồ thị dòng xoay chiều", K, fig="t_dt_i_t",
   cap="Cường độ dòng điện xoay chiều theo thời gian"),

mc("Một cuộn dây N vòng đặt trong từ trường biến thiên. Điện lượng chuyển qua tiết diện dây khi từ "
   "thông qua mỗi vòng biến thiên một lượng ΔΦ là",
   ["N·ΔΦ·R.", "N·ΔΦ/R.", "ΔΦ/(N·R).", "N·R/ΔΦ."],
   "B",
   "q = i·Δt = (N·ΔΦ/Δt)/R · Δt = N·ΔΦ/R. Điện lượng không phụ thuộc thời gian biến thiên, "
   "chỉ phụ thuộc độ biến thiên từ thông, số vòng và điện trở.",
   "Điện lượng cảm ứng", K),

mc("Hai dây dẫn thẳng dài song song đặt cách nhau 10 cm, mang hai dòng điện cùng chiều "
   "I₁ = 3,0 A và I₂ = 12,0 A. Điểm có cảm ứng từ tổng hợp bằng không nằm",
   ["ngoài khoảng hai dây, cách dây I₁ 10 cm.",
    "trong khoảng hai dây, cách dây I₁ 2,0 cm.",
    "trong khoảng hai dây, cách dây I₁ 8,0 cm.",
    "không tồn tại điểm nào như vậy."],
   "B",
   "Hai dòng cùng chiều nên điểm triệt tiêu nằm giữa hai dây và gần dây có dòng NHỎ hơn.\n"
   "3,0/x = 12,0/(10 − x) ⇒ 3,0(10 − x) = 12,0x ⇒ 30 = 15x ⇒ x = 2,0 cm.",
   "Từ trường của hai dòng điện", K),

mc("Một máy biến áp thực tế có công suất sơ cấp 1000 W và hiệu suất 92 %. Điện áp thứ cấp 24 V. "
   "Cường độ dòng điện hiệu dụng ở cuộn thứ cấp xấp xỉ",
   ["41,7 A.", "38,3 A.", "45,3 A.", "23,0 A."],
   "B",
   "Công suất ở thứ cấp: P₂ = 92 % · 1000 = 920 W.\n"
   "I₂ = P₂/U₂ = 920/24 ≈ 38,3 A.\n"
   "Giá trị 41,7 A là kết quả khi bỏ qua hao phí (1000/24).",
   "Máy biến áp có hao phí", K),

mc("Một vòng dây kín được đặt trong từ trường đều rồi được kéo ra khỏi từ trường theo hai cách: "
   "lần đầu kéo trong 1,0 s, lần sau kéo trong 4,0 s. So sánh điện lượng chuyển qua tiết diện vòng "
   "dây trong hai lần:",
   ["lần đầu lớn gấp 4 lần.", "hai lần bằng nhau.",
    "lần sau lớn gấp 4 lần.", "lần đầu lớn gấp 2 lần."],
   "B",
   "q = |ΔΦ|/R chỉ phụ thuộc độ biến thiên từ thông và điện trở, hoàn toàn không phụ thuộc thời gian. "
   "Chỉ có suất điện động và cường độ dòng điện khác nhau: lần đầu lớn gấp 4 lần.",
   "Điện lượng cảm ứng", K),

mc("Một khung dây 500 vòng quay đều trong từ trường đều B = 0,20 T quanh trục vuông góc với B, "
   "diện tích mỗi vòng 40 cm². Suất điện động cực đại của khung là 62,8 V. Tốc độ quay của khung là",
   ["1500 vòng/phút.", "3000 vòng/phút.", "750 vòng/phút.", "6000 vòng/phút."],
   "A",
   "ω = E₀/(N·B·S) = 62,8/(500 · 0,20 · 4,0·10⁻³) = 62,8/0,40 = 157 rad/s.\n"
   "f = ω/(2π) = 157/6,283 = 25 Hz ⇒ tốc độ quay = 25 · 60 = 1500 vòng/phút.\n"
   "Phương án 3000 vòng/phút ứng với việc quên chia cho 2π khi đổi từ ω sang f.",
   "Máy phát – bài toán ngược", K),

mc("Một đoạn dây dẫn thẳng dài 20 cm mang dòng điện 10 A được đặt trong từ trường đều B = 0,30 T. "
   "Công của lực từ khi đoạn dây dịch chuyển 5,0 cm theo hướng của lực từ bằng",
   ["0,015 J.", "0,030 J.", "0,060 J.", "0,300 J."],
   "B",
   "F = B·I·ℓ = 0,30 · 10 · 0,20 = 0,60 N.\n"
   "A = F·s = 0,60 · 0,050 = 0,030 J.",
   "Công của lực từ", TB),

mc("Một khung dây dẫn kín quay đều trong từ trường đều. Nếu tăng đồng thời số vòng dây lên gấp đôi "
   "và giảm tốc độ quay còn một nửa thì suất điện động HIỆU DỤNG và TẦN SỐ lần lượt",
   ["đều không đổi.", "không đổi và giảm một nửa.",
    "tăng gấp đôi và không đổi.", "giảm một nửa và tăng gấp đôi."],
   "B",
   "E₀ = ωNBS: N tăng 2 lần, ω giảm 2 lần nên E₀ (và E) không đổi. "
   "Tần số f = ω/(2π) tỉ lệ với ω nên giảm một nửa.",
   "Máy phát – phân tích tỉ lệ", K),

mc("Khi truyền tải điện năng, nếu dùng dây dẫn có tiết diện lớn gấp đôi (cùng vật liệu, cùng chiều "
   "dài) thì công suất hao phí",
   ["không đổi.", "giảm một nửa.", "tăng gấp đôi.", "giảm bốn lần."],
   "B",
   "Điện trở R = ρℓ/S tỉ lệ nghịch với tiết diện. Tiết diện tăng gấp đôi thì R giảm một nửa, "
   "kéo theo hao phí ΔP = R·I² giảm một nửa. Tuy nhiên cách này tốn kim loại nên đắt hơn nhiều "
   "so với tăng điện áp.",
   "Truyền tải – các biện pháp", TB),

mc("Một vòng dây dẫn kín đặt trong mặt phẳng ngang, phía trên có một nam châm đang được nhấc lên "
   "theo phương thẳng đứng. Lực từ do vòng dây tác dụng lên nam châm có chiều",
   ["hướng lên, hỗ trợ việc nhấc.", "hướng xuống, cản trở việc nhấc.",
    "nằm ngang.", "bằng không vì nam châm ở ngoài vòng dây."],
   "B",
   "Nam châm ra xa nên từ thông giảm; theo định luật Lenz dòng cảm ứng chống lại sự giảm đó bằng "
   "cách HÚT nam châm lại, tức lực hướng xuống. Người nhấc phải tốn thêm công, và công đó chuyển "
   "thành nhiệt trên vòng dây.",
   "Định luật Lenz", K, fig="t_sd_nam_cham_roi", cap="Nam châm chuyển động gần vòng dây"),

mc("Một cuộn dây 250 vòng, điện trở 2,5 Ω, có từ thông qua mỗi vòng giảm đều 4,0·10⁻³ Wb. "
   "Điện lượng chuyển qua tiết diện dây bằng",
   ["0,20 C.", "0,40 C.", "0,80 C.", "1,00 C."],
   "B",
   "q = N·|ΔΦ|/R = 250 · 4,0·10⁻³/2,5 = 1,0/2,5 = 0,40 C.",
   "Điện lượng cảm ứng", K),

mc("Trong thí nghiệm vòng nhôm nhảy khỏi ống dây (thí nghiệm Thomson), nếu thay vòng nhôm kín bằng "
   "một vòng nhôm bị CẮT ĐỨT một chỗ thì",
   ["vòng vẫn bật lên như cũ.", "vòng đứng yên.",
    "vòng bị hút mạnh xuống.", "vòng nóng chảy."],
   "B",
   "Vòng bị cắt đứt không còn là mạch kín nên không có dòng điện cảm ứng, do đó không có lực từ "
   "đẩy vòng lên. Suất điện động cảm ứng vẫn xuất hiện nhưng không có dòng chạy qua.",
   "Phân biệt suất điện động và dòng điện", K),
],
P2=[
ds("Một khung dây vuông cạnh 20 cm, khối lượng 50 g, điện trở 0,20 Ω rơi thẳng đứng trong mặt phẳng "
   "của mình, đi ra khỏi biên ngang dưới của một vùng từ trường đều B = 0,50 T nằm ngang, "
   "vuông góc mặt phẳng khung. Lấy g = 10 m/s².",
   [("Khi cạnh dưới của khung vừa ra khỏi vùng từ trường, trong khung bắt đầu có dòng cảm ứng.", True,
     "Đúng. Lúc đó diện tích phần khung còn nằm trong từ trường bắt đầu giảm nên từ thông biến thiên."),
    ("Ở tốc độ v, lực từ cản tác dụng lên khung có độ lớn 0,050·v (đơn vị SI).", True,
     "Đúng. F = B²a²v/R = (0,50² · 0,20²/0,20)·v = (0,25 · 0,040/0,20)·v = 0,050v."),
    ("Tốc độ giới hạn của khung là 10 m/s.", True,
     "Đúng. Ở tốc độ giới hạn: 0,050·v = m·g = 0,050 · 10 = 0,50 N ⇒ v = 10 m/s."),
    ("Khi đạt tốc độ giới hạn, khung tiếp tục tăng tốc nhưng chậm hơn.", False,
     "Sai. Ở tốc độ giới hạn, lực từ cản cân bằng hoàn toàn trọng lực nên hợp lực bằng 0, "
     "khung chuyển động THẲNG ĐỀU chứ không tăng tốc nữa.")],
   "Khung dây rơi qua biên từ trường", K),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 2000 vòng mắc vào mạng điện xoay chiều 220 V. "
   "Cuộn thứ cấp theo thiết kế có 400 vòng nhưng thợ quấn nhầm 20 vòng theo chiều ngược lại.",
   [("Nếu quấn đúng, điện áp thứ cấp là 44 V.", True,
     "Đúng. U₂ = 220 · 400/2000 = 44 V."),
    ("Số vòng có hiệu lực của cuộn thứ cấp sau khi quấn nhầm là 360 vòng.", True,
     "Đúng. Mỗi vòng quấn ngược triệt tiêu một vòng quấn đúng nên hiệu lực là 400 − 2·20 = 360 vòng."),
    ("Điện áp thứ cấp đo được thực tế là 39,6 V.", True,
     "Đúng. U₂ = 220 · 360/2000 = 220 · 0,18 = 39,6 V."),
    ("Điện áp thứ cấp đo được là 41,8 V vì chỉ mất đi 20 vòng.", False,
     "Sai. Vòng quấn ngược sinh suất điện động NGƯỢC PHA nên nó triệt tiêu một vòng quấn đúng: "
     "mất đi 40 vòng hiệu lực, không phải 20 vòng.")],
   "Máy biến áp – quấn ngược", K, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

ds("Một nhà máy truyền công suất 4,0 MW tới khu dân cư qua đường dây có điện trở tổng 10 Ω. "
   "Hệ số công suất bằng 1.",
   [("Ở điện áp truyền tải 40 kV, cường độ dòng điện trên dây là 100 A.", True,
     "Đúng. I = 4,0·10⁶/(40·10³) = 100 A."),
    ("Ở điện áp 40 kV, công suất hao phí là 100 kW, chiếm 2,5 % công suất truyền đi.", True,
     "Đúng. ΔP = 10 · 100² = 100 000 W = 100 kW;  100/4000 = 2,5 %."),
    ("Muốn hao phí chỉ còn 1,0 % thì cần tăng điện áp lên 80 kV.", False,
     "Sai. Hao phí phải giảm từ 2,5 % xuống 1,0 %, tức giảm 2,5 lần, nên U phải tăng √2,5 ≈ 1,58 lần: "
     "từ 40 kV lên khoảng 63,2 kV chứ không phải 80 kV."),
    ("Nếu tăng điện áp lên 80 kV thì hao phí chỉ còn 25 kW.", True,
     "Đúng. Điện áp tăng 2 lần thì hao phí giảm 4 lần: 100/4 = 25 kW.")],
   "Truyền tải điện năng", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

ds("Xét đồ thị cường độ dòng điện xoay chiều i = I₀·cos(2πt/T) theo thời gian, trong đó phần tô đậm "
   "ứng với các khoảng thời gian mà |i| lớn hơn giá trị hiệu dụng.",
   [("Giá trị hiệu dụng bằng I₀/√2 ≈ 0,707·I₀.", True,
     "Đúng. Đó là định nghĩa của giá trị hiệu dụng đối với dòng điện hình sin."),
    ("Trong mỗi chu kì có bốn khoảng thời gian mà |i| lớn hơn giá trị hiệu dụng.", True,
     "Đúng. Quanh mỗi cực đại dương và mỗi cực tiểu âm đều có một khoảng; trong một chu kì "
     "có hai cực trị nên tổng cộng bốn khoảng (hai khoảng ở hai đầu ghép lại thành một)."),
    ("Tổng thời gian đó bằng đúng một nửa chu kì.", True,
     "Đúng. Mỗi khoảng dài T/8, bốn khoảng cho tổng T/2."),
    ("Giá trị trung bình của cường độ dòng điện trong một chu kì bằng giá trị hiệu dụng.", False,
     "Sai. Giá trị trung bình của i trong một chu kì bằng 0 vì dòng đổi chiều đều đặn. "
     "Giá trị hiệu dụng được định nghĩa từ trung bình của i², không phải của i.")],
   "Đọc đồ thị dòng xoay chiều", K, fig="t_dt_i_t",
   cap="Cường độ dòng điện xoay chiều theo thời gian"),
],
P3=[
sa("Một khung dây vuông cạnh 25 cm, khối lượng 80 g, điện trở 0,25 Ω rơi thẳng đứng đi ra khỏi "
   "vùng từ trường đều B = 0,40 T nằm ngang vuông góc mặt phẳng khung. Tốc độ giới hạn của khung "
   "bằng bao nhiêu mét trên giây? Lấy g = 10 m/s².",
   "20",
   "Ở tốc độ giới hạn, lực từ cản cân bằng trọng lực: B²a²v/R = m·g.\n"
   "v = m·g·R/(B²a²) = 0,080 · 10 · 0,25 / (0,40² · 0,25²)\n"
   "= 0,20 / (0,16 · 0,0625) = 0,20/0,010 = 20 m/s.",
   "Tốc độ giới hạn của khung rơi", K),

sa("Một máy biến áp có cuộn sơ cấp 1500 vòng, cuộn thứ cấp thiết kế 300 vòng nhưng bị quấn ngược "
   "một số vòng. Đặt vào sơ cấp điện áp 220 V thì đo được điện áp thứ cấp 36,67 V. "
   "Số vòng bị quấn ngược bằng bao nhiêu?",
   "25",
   "Số vòng có hiệu lực: N = 1500 · 36,67/220 ≈ 250 vòng.\n"
   "Từ 300 − 2n = 250 ⇒ 2n = 50 ⇒ n = 25 vòng.",
   "Máy biến áp – quấn ngược", K),

sa("Một khung dây tròn 120 vòng, diện tích mỗi vòng 80 cm², điện trở tổng 1,6 Ω, đặt vuông góc "
   "với từ trường đều. Cảm ứng từ giảm đều từ 0,50 T về 0. Điện lượng chuyển qua tiết diện dây "
   "bằng bao nhiêu culông?",
   "0,3",
   "Độ biến thiên từ thông qua mỗi vòng: |ΔΦ| = ΔB·S = 0,50 · 8,0·10⁻³ = 4,0·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 120 · 4,0·10⁻³/1,6 = 0,48/1,6 = 0,30 C.",
   "Điện lượng cảm ứng", K),

sa("Truyền công suất 3,0 MW ở điện áp 30 kV trên đường dây có hiệu suất 96 %. "
   "Điện trở tổng của đường dây bằng bao nhiêu ôm?",
   "12",
   "Hao phí: ΔP = 4 % · 3,0·10⁶ = 1,2·10⁵ W.\n"
   "Cường độ dòng điện: I = P/U = 3,0·10⁶/(30·10³) = 100 A.\n"
   "R = ΔP/I² = 1,2·10⁵/100² = 1,2·10⁵/1,0·10⁴ = 12 Ω.",
   "Truyền tải – bài toán ngược", K),

sa("Một khung dây quay đều tạo ra suất điện động e = E₀·sin(120πt) (V). Khoảng thời gian ngắn nhất "
   "kể từ lúc suất điện động bằng 0 đến lúc độ lớn của nó bằng E₀/2 là bao nhiêu phần nghìn giây "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "1,39",
   "sin(120πt) = 0,5 ⇒ 120πt = π/6 ⇒ t = 1/720 ≈ 1,389·10⁻³ s ≈ 1,39 ms.",
   "Suất điện động theo thời gian", K),

sa("Một cuộn dây 600 vòng, điện trở 3,0 Ω. Từ thông qua mỗi vòng giảm đều 5,0·10⁻³ Wb. "
   "Điện lượng chuyển qua tiết diện dây bằng bao nhiêu culông?",
   "1",
   "q = N·|ΔΦ|/R = 600 · 5,0·10⁻³/3,0 = 3,0/3,0 = 1,0 C.\n"
   "Điện lượng không phụ thuộc thời gian biến thiên của từ thông.",
   "Điện lượng cảm ứng", K),
])


# =====================================================================  ĐỀ 9
DE9 = dict(
ma="12C3-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Tổng hợp nhiều kiến thức, bài toán hệ thống điện, suy luận nhiều bước",
P1=[
mc("Một nhà máy truyền công suất P đi xa. Ở điện áp U₁, hiệu suất truyền tải là 80 % và điện năng "
   "đến nơi tiêu thụ đủ cung cấp cho 8000 hộ dân. Nếu tăng điện áp lên 2U₁ (giữ nguyên P) thì "
   "số hộ dân được cung cấp là",
   ["8400 hộ.", "9500 hộ.", "10 000 hộ.", "9000 hộ."],
   "B",
   "Hao phí tỉ lệ nghịch với U². Ban đầu hao phí chiếm 20 %; tăng U gấp đôi thì hao phí giảm 4 lần, "
   "còn 5 %.\n"
   "Công suất tới nơi tiêu thụ tăng từ 80 % lên 95 % của P.\n"
   "Số hộ: 8000 · 95/80 = 8000 · 1,1875 = 9500 hộ.",
   "Truyền tải điện năng – bài toán thực tiễn", K, fig="t_sd_truyen_tai",
   cap="Sơ đồ truyền tải điện năng"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng nối vào mạng 220 V và hai cuộn thứ cấp riêng "
   "biệt 100 vòng và 50 vòng, lần lượt cung cấp cho hai điện trở 11 Ω và 5,5 Ω. "
   "Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng",
   ["0,20 A.", "0,30 A.", "0,40 A.", "0,50 A."],
   "B",
   "Cuộn thứ cấp 1: U = 220·100/1000 = 22 V ⇒ P₁ = 22²/11 = 44 W.\n"
   "Cuộn thứ cấp 2: U = 220·50/1000 = 11 V ⇒ P₂ = 11²/5,5 = 22 W.\n"
   "Tổng công suất: P = 44 + 22 = 66 W.\n"
   "I₁ = P/U₁ = 66/220 = 0,30 A.",
   "Máy biến áp nhiều cuộn thứ cấp", RK, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một khung dây quay đều trong từ trường đều với tần số 50 Hz, tạo ra suất điện động cực đại E₀. "
   "Trong mỗi giây, số lần độ lớn suất điện động bằng đúng E₀/2 là",
   ["100 lần.", "200 lần.", "50 lần.", "400 lần."],
   "B",
   "Trong mỗi chu kì, |e| = E₀/2 xảy ra 4 lần (hai lần khi e dương, hai lần khi e âm). "
   "Với 50 chu kì mỗi giây ta có 4 · 50 = 200 lần.",
   "Dòng xoay chiều – đếm số lần", K),

mc("Đồ thị từ thông qua một vòng dây gồm bốn giai đoạn. Tổng điện lượng chuyển qua tiết diện vòng "
   "dây trong giai đoạn (III) và giai đoạn (IV) (vòng dây có điện trở 0,20 Ω) bằng",
   ["2,0 C.", "5,0 C.", "3,0 C.", "1,0 C."],
   "B",
   "Giai đoạn (III): từ thông giảm từ 0,40 Wb xuống 0, |ΔΦ| = 0,40 Wb.\n"
   "Giai đoạn (IV): từ thông giảm từ 0 xuống −0,60 Wb, |ΔΦ| = 0,60 Wb.\n"
   "Hai giai đoạn cùng chiều biến thiên nên điện lượng cộng lại:\n"
   "q = (0,40 + 0,60)/0,20 = 1,00/0,20 = 5,0 C.",
   "Điện lượng cảm ứng – đọc đồ thị", RK, fig="t_dt_phi_t",
   cap="Từ thông qua vòng dây theo thời gian"),

mc("Một thanh dẫn dài 40 cm, khối lượng 100 g nằm ngang trên hai ray nằm ngang không ma sát, "
   "trong từ trường đều thẳng đứng B = 0,50 T. Điện trở toàn mạch 0,40 Ω. Thanh được truyền vận tốc "
   "ban đầu 5,0 m/s rồi thả tự do. Tổng điện lượng chuyển qua mạch cho tới khi thanh dừng hẳn bằng",
   ["1,25 C.", "2,50 C.", "0,50 C.", "5,00 C."],
   "B",
   "Xung lượng của lực từ bằng độ biến thiên động lượng của thanh:  B·ℓ·q = m·v₀.\n"
   "q = m·v₀/(B·ℓ) = 0,100 · 5,0 / (0,50 · 0,40) = 0,50/0,20 = 2,50 C.\n"
   "Kết quả không phụ thuộc điện trở mạch: điện trở chỉ quyết định thanh dừng NHANH hay CHẬM, "
   "không quyết định tổng điện lượng.",
   "Xung lượng của lực từ", RK, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Trong mặt phẳng chứa hai dây dẫn thẳng dài song song cách nhau 12 cm có dòng ngược chiều "
   "I₁ = 5,0 A và I₂ = 15,0 A, vị trí mà kim nam châm thử không bị lệch nằm",
   ["giữa hai dây, cách dây I₁ 3,0 cm.",
    "ngoài khoảng hai dây, về phía dây I₁, cách dây I₁ 6,0 cm.",
    "ngoài khoảng hai dây, về phía dây I₂, cách dây I₂ 6,0 cm.",
    "giữa hai dây, cách dây I₁ 9,0 cm."],
   "B",
   "Hai dòng ngược chiều nên điểm triệt tiêu nằm NGOÀI khoảng hai dây, về phía dây có dòng NHỎ hơn.\n"
   "Gọi khoảng cách tới dây I₁ là x thì tới dây I₂ là x + 12.\n"
   "5,0/x = 15,0/(x + 12) ⇒ 5,0(x + 12) = 15,0x ⇒ 60 = 10x ⇒ x = 6,0 cm.",
   "Từ trường của hai dòng điện", K),

mc("Một máy phát điện xoay chiều cung cấp công suất 200 kW cho một đường dây có điện trở 4,0 Ω "
   "qua máy tăng áp có tỉ số vòng 1 : 10. Điện áp ở hai đầu cuộn sơ cấp là 2,0 kV. "
   "Hiệu suất truyền tải trên đường dây bằng",
   ["96 %.", "99 %.", "98 %.", "90 %."],
   "B",
   "Điện áp trên đường dây: U = 10 · 2,0 = 20 kV.\n"
   "I = P/U = 200 000/20 000 = 10 A.\n"
   "ΔP = R·I² = 4,0 · 100 = 400 W.\n"
   "H = (200 000 − 400)/200 000 = 0,998 = 99,8 % ≈ 99 % (gần nhất trong bốn phương án).",
   "Hệ thống máy phát – biến áp – đường dây", RK),

mc("Một khung dây hình chữ nhật quay đều quanh trục đối xứng nằm trong mặt phẳng khung và vuông góc "
   "với từ trường đều. Biểu thức từ thông là Φ = 0,020·cos(100πt) (Wb). "
   "Biểu thức suất điện động cảm ứng là",
   ["e = 2,0·cos(100πt) V.", "e = 2π·sin(100πt) V.",
    "e = 0,020·sin(100πt) V.", "e = 100π·cos(100πt) V."],
   "B",
   "e = −dΦ/dt tương ứng với e = ω·Φ₀·sin(ωt) = 100π · 0,020 · sin(100πt) = 2π·sin(100πt) V "
   "≈ 6,28·sin(100πt) V.\n"
   "Suất điện động lệch pha π/2 so với từ thông, biên độ bằng ω·Φ₀.",
   "Quan hệ giữa Φ và e", K),

mc("Một cuộn dây N vòng quay đều trong từ trường đều. Nếu đồng thời tăng gấp đôi cảm ứng từ, "
   "giảm một nửa diện tích khung và tăng gấp bốn tốc độ quay thì suất điện động cực đại",
   ["không đổi.", "tăng gấp bốn.", "tăng gấp đôi.", "giảm một nửa."],
   "B",
   "E₀ = ω·N·B·S: B tăng 2 lần (×2), S giảm 2 lần (×0,5), ω tăng 4 lần (×4).\n"
   "Tổng hợp: 2 · 0,5 · 4 = 4 lần.",
   "Máy phát – phân tích tỉ lệ", K),

mc("Một vòng dây kín hình tròn bán kính 20 cm, điện trở 0,50 Ω, đặt vuông góc với từ trường đều. "
   "Cảm ứng từ tăng đều với tốc độ 2,0 T/s. Công suất toả nhiệt trên vòng dây xấp xỉ",
   ["0,063 W.", "0,126 W.", "0,252 W.", "0,032 W."],
   "B",
   "Diện tích: S = π·0,20² = 3,1416 · 0,040 ≈ 0,1257 m².\n"
   "e = S·(ΔB/Δt) = 0,1257 · 2,0 ≈ 0,2513 V.\n"
   "P = e²/R = 0,2513²/0,50 = 0,06316/0,50 ≈ 0,126 W.",
   "Công suất cảm ứng", K),

mc("Một thanh dẫn trượt trên hai ray nghiêng không ma sát, nối với một điện trở R. "
   "Nếu thay điện trở R bằng 2R thì tốc độ giới hạn của thanh",
   ["giảm một nửa.", "tăng gấp đôi.", "không đổi.", "tăng gấp bốn."],
   "B",
   "Tốc độ giới hạn v = m·g·sinα·R/(B²ℓ²) tỉ lệ THUẬN với R. "
   "Điện trở lớn hơn thì dòng cảm ứng nhỏ hơn, lực cản nhỏ hơn nên thanh phải chạy nhanh hơn "
   "mới cân bằng được.",
   "Thanh dẫn trên mặt nghiêng", K, fig="t_sd_ray_nghieng",
   cap="Thanh dẫn trên hai ray nghiêng"),

mc("Đặt điện áp u = U₀·cos(ωt) vào hai đầu điện trở R. Trong khoảng thời gian từ t = 0 đến "
   "t = T/4, điện lượng chuyển qua điện trở bằng",
   ["U₀/(ωR).", "U₀·T/(4R).", "2U₀/(ωR).", "0."],
   "A",
   "Trong khoảng từ 0 đến T/4, dòng điện không đổi chiều nên điện lượng bằng tích phân của i.\n"
   "Với i = (U₀/R)·cos(ωt), điện lượng trong một phần tư chu kì bằng (U₀/R)·(1/ω) = U₀/(ωR).\n"
   "Có thể kiểm chứng bằng thứ nguyên: [U/(ωR)] = V/(rad/s · Ω) = A·s = C.",
   "Điện lượng trong mạch xoay chiều", RK),

mc("Một khung dây vuông cạnh a, điện trở R, được kéo đều ra khỏi vùng từ trường đều B với tốc độ v. "
   "Công của lực kéo trong suốt quá trình đó bằng",
   ["B·a·v·R.", "B²·a³·v/R.", "B²·a²·v/R.", "B·a²·v²/R."],
   "B",
   "Lực kéo phải cân bằng lực từ cản: F = B²a²v/R.\n"
   "Quãng đường kéo bằng cạnh khung: s = a.\n"
   "A = F·s = B²a³v/R.\n"
   "Có thể kiểm chứng bằng năng lượng: A = nhiệt lượng toả ra = (e²/R)·(a/v) = "
   "(B²a²v²/R)·(a/v) = B²a³v/R.",
   "Công và năng lượng trong cảm ứng điện từ", RK),

mc("Một máy biến áp lí tưởng đang hoạt động. Nếu giảm số vòng của CẢ HAI cuộn đi một nửa và giữ "
   "nguyên điện áp sơ cấp thì điện áp thứ cấp",
   ["giảm một nửa.", "không đổi.", "tăng gấp đôi.", "bằng không."],
   "B",
   "U₂/U₁ = N₂/N₁ chỉ phụ thuộc TỈ SỐ số vòng. Giảm cả hai cuộn đi một nửa thì tỉ số không đổi "
   "nên điện áp thứ cấp giữ nguyên (bỏ qua giới hạn kĩ thuật về từ thông bão hoà).",
   "Máy biến áp – phân tích tỉ số", TB, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một đoạn dây dẫn thẳng dài 30 cm, khối lượng 60 g được treo nằm ngang bằng hai sợi dây nhẹ "
   "trong từ trường đều nằm ngang vuông góc với đoạn dây, B = 0,40 T. Cho dòng điện 4,0 A qua dây "
   "theo chiều làm lực từ hướng xuống. Lực căng tổng cộng của hai sợi dây bằng (g = 10 m/s²)",
   ["0,12 N.", "1,08 N.", "0,60 N.", "0,48 N."],
   "B",
   "Trọng lực: P = m·g = 0,060 · 10 = 0,60 N.\n"
   "Lực từ hướng xuống: F = B·I·ℓ = 0,40 · 4,0 · 0,30 = 0,48 N.\n"
   "Hai lực cùng hướng xuống nên lực căng tổng cộng của hai sợi dây:\n"
   "T = P + F = 0,60 + 0,48 = 1,08 N.\n"
   "Nếu dòng điện đổi chiều, lực từ hướng lên và lực căng chỉ còn 0,60 − 0,48 = 0,12 N.",
   "Cân bằng lực có lực từ", K),

mc("Một vòng dây kín được đặt trong từ trường đều có cảm ứng từ tăng đều theo thời gian. "
   "Nếu thay vòng dây bằng vòng cùng vật liệu, cùng tiết diện dây nhưng bán kính lớn gấp đôi thì "
   "cường độ dòng điện cảm ứng",
   ["không đổi.", "tăng gấp đôi.", "tăng gấp bốn.", "giảm một nửa."],
   "B",
   "Diện tích vòng tăng 4 lần nên suất điện động tăng 4 lần. Chu vi tăng 2 lần nên điện trở "
   "cũng tăng 2 lần. Cường độ i = e/R tăng 4/2 = 2 lần.",
   "Phân tích tỉ lệ trong cảm ứng điện từ", RK),

mc("Trong một chu kì của dòng điện xoay chiều, khoảng thời gian mà độ lớn cường độ dòng điện "
   "KHÔNG VƯỢT QUÁ một nửa giá trị cực đại chiếm",
   ["một phần ba chu kì.", "hai phần ba chu kì.",
    "một nửa chu kì.", "một phần tư chu kì."],
   "A",
   "Điều kiện |i| ≤ I₀/2 tương đương |cos(ωt)| ≤ 0,5, thoả mãn trên tổng cộng π/3 rad trong mỗi "
   "nửa chu kì π rad, tức tỉ lệ 1/3. Phần bù (|i| ≥ I₀/2) chiếm hai phần ba.",
   "Đọc đồ thị dòng xoay chiều", K, fig="t_dt_i_t",
   cap="Cường độ dòng điện xoay chiều theo thời gian"),

mc("Một khung dây dẫn kín đặt cố định, trong đó có một nam châm điện được cấp dòng điện tăng đều "
   "theo thời gian. Suất điện động cảm ứng trong khung dây",
   ["tăng đều theo thời gian.", "không đổi theo thời gian.",
    "giảm đều theo thời gian.", "bằng không."],
   "B",
   "Dòng trong nam châm điện tăng ĐỀU nên cảm ứng từ B tăng đều, từ thông Φ = B·S cũng tăng đều. "
   "Suất điện động tỉ lệ với TỐC ĐỘ biến thiên của từ thông, mà tốc độ này là hằng số, "
   "nên e không đổi theo thời gian.",
   "Phân biệt Φ và tốc độ biến thiên Φ", K),
],
P2=[
ds("Một nhà máy điện truyền công suất 10 MW đi xa qua đường dây có điện trở 20 Ω. "
   "Hệ số công suất bằng 1.",
   [("Ở điện áp truyền tải 100 kV, cường độ dòng điện trên dây là 100 A.", True,
     "Đúng. I = 10·10⁶/(100·10³) = 100 A."),
    ("Ở điện áp 100 kV, công suất hao phí là 200 kW, tức 2 % công suất truyền đi.", True,
     "Đúng. ΔP = 20 · 100² = 200 000 W = 200 kW;  200/10 000 = 2 %."),
    ("Nếu giảm điện áp xuống 50 kV thì hao phí tăng lên 800 kW.", True,
     "Đúng. Điện áp giảm 2 lần thì hao phí tăng 4 lần: 200 · 4 = 800 kW."),
    ("Nếu thay dây dẫn bằng dây cùng loại nhưng đường kính gấp đôi thì hao phí giảm 2 lần.", False,
     "Sai. Đường kính gấp đôi thì TIẾT DIỆN gấp bốn, nên điện trở giảm 4 lần và hao phí cũng "
     "giảm 4 lần chứ không phải 2 lần.")],
   "Truyền tải điện năng", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

ds("Một thanh dẫn dài 50 cm, khối lượng 200 g nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,40 T. Điện trở toàn mạch 0,50 Ω. "
   "Thanh được truyền vận tốc ban đầu 3,0 m/s rồi để tự do.",
   [("Ngay sau khi được truyền vận tốc, suất điện động cảm ứng trong mạch là 0,60 V.", True,
     "Đúng. e = B·ℓ·v = 0,40 · 0,50 · 3,0 = 0,60 V."),
    ("Lực từ tác dụng lên thanh lúc đó có độ lớn 0,24 N và hướng ngược chiều chuyển động.", True,
     "Đúng. i = 0,60/0,50 = 1,2 A; F = B·i·ℓ = 0,40 · 1,2 · 0,50 = 0,24 N; "
     "theo định luật Lenz lực này cản trở chuyển động."),
    ("Thanh chuyển động chậm dần rồi dừng hẳn.", True,
     "Đúng. Lực từ luôn cản trở nên thanh giảm tốc; khi v giảm thì lực cản cũng giảm, "
     "thanh tiệm cận trạng thái đứng yên."),
    ("Tổng nhiệt lượng toả ra trên mạch cho tới khi thanh dừng là 0,60 J.", False,
     "Sai. Toàn bộ động năng ban đầu chuyển thành nhiệt: "
     "Q = ½mv² = 0,5 · 0,200 · 3,0² = 0,90 J chứ không phải 0,60 J.")],
   "Bảo toàn năng lượng trong cảm ứng điện từ", RK, fig="t_sd_ray_ngang",
   cap="Thanh dẫn trên hai ray nằm ngang"),

ds("Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng nối vào mạng điện 220 V, "
   "hai cuộn thứ cấp độc lập gồm 100 vòng và 50 vòng.",
   [("Điện áp ở cuộn thứ cấp 100 vòng là 22 V.", True,
     "Đúng. U = 220 · 100/1000 = 22 V."),
    ("Điện áp ở cuộn thứ cấp 50 vòng là 11 V.", True,
     "Đúng. U = 220 · 50/1000 = 11 V."),
    ("Nếu hai cuộn thứ cấp lần lượt nối với điện trở 11 Ω và 5,5 Ω thì tổng công suất tiêu thụ "
     "là 66 W.", True,
     "Đúng. P₁ = 22²/11 = 44 W;  P₂ = 11²/5,5 = 22 W;  tổng 66 W."),
    ("Cường độ dòng điện hiệu dụng ở cuộn sơ cấp khi đó là 0,60 A.", False,
     "Sai. I₁ = P/U₁ = 66/220 = 0,30 A chứ không phải 0,60 A.")],
   "Máy biến áp nhiều cuộn thứ cấp", RK, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

ds("Xét quan hệ giữa từ thông Φ và suất điện động cảm ứng e trong một khung dây quay đều.",
   [("Khi Φ đạt giá trị cực đại thì e bằng 0.", True,
     "Đúng. Tại cực đại của Φ, tốc độ biến thiên của Φ bằng 0 nên e = 0."),
    ("Khi Φ bằng 0 thì |e| đạt giá trị cực đại.", True,
     "Đúng. Đó là lúc Φ biến thiên nhanh nhất."),
    ("Biên độ của e bằng tích của tần số góc với biên độ của Φ.", True,
     "Đúng. E₀ = ω·Φ₀, nên quay càng nhanh thì suất điện động càng lớn."),
    ("Φ và e luôn cùng pha nhau.", False,
     "Sai. Hai đại lượng lệch pha nhau đúng π/2 (tức 90°): Φ biến thiên theo cosin thì e theo sin.")],
   "Quan hệ giữa Φ và e", K, fig="t_sd_khung_quay", cap="Khung dây quay trong từ trường"),
],
P3=[
sa("Một nhà máy truyền công suất không đổi đi xa. Ở điện áp U₁ hiệu suất truyền tải là 75 %, "
   "điện năng tới nơi tiêu thụ đủ cấp cho 6000 hộ dân. Nếu tăng điện áp lên 5U₁ thì cấp được "
   "cho bao nhiêu hộ dân?",
   "7920",
   "Hao phí tỉ lệ nghịch với U². Ban đầu hao phí chiếm 25 %.\n"
   "Tăng điện áp 5 lần ⇒ hao phí giảm 25 lần, còn 25/25 = 1 %.\n"
   "Công suất tới nơi tiêu thụ tăng từ 75 % lên 99 %.\n"
   "Số hộ: 6000 · 99/75 = 6000 · 1,32 = 7920 hộ.",
   "Truyền tải điện năng – bài toán thực tiễn", RK),

sa("Một thanh dẫn dài 40 cm, khối lượng 120 g nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,60 T. Thanh được truyền vận tốc ban đầu 4,0 m/s rồi để tự do. "
   "Tổng điện lượng chuyển qua mạch cho tới khi thanh dừng hẳn bằng bao nhiêu culông?",
   "2",
   "Xung lượng của lực từ bằng độ biến thiên động lượng của thanh:\n"
   "B·ℓ·q = m·v₀  ⇒  q = m·v₀/(B·ℓ).\n"
   "q = 0,120 · 4,0/(0,60 · 0,40) = 0,48/0,24 = 2,0 C.",
   "Xung lượng của lực từ", RK),

sa("Một vòng dây kín hình tròn bán kính 30 cm, điện trở 0,60 Ω, đặt vuông góc với từ trường đều. "
   "Cảm ứng từ tăng đều với tốc độ 1,5 T/s. Công suất toả nhiệt trên vòng dây bằng bao nhiêu oát "
   "(làm tròn đến chữ số thập phân thứ ba)? Lấy π ≈ 3,1416.",
   "0,300",
   "S = π·0,30² = 3,1416 · 0,090 ≈ 0,28274 m².\n"
   "e = S·(ΔB/Δt) = 0,28274 · 1,5 ≈ 0,42412 V.\n"
   "P = e²/R = 0,42412²/0,60 = 0,17988/0,60 ≈ 0,29980 ≈ 0,300 W.",
   "Công suất cảm ứng", K),

sa("Một máy biến áp lí tưởng có cuộn sơ cấp 1200 vòng nối vào mạng 240 V và hai cuộn thứ cấp độc "
   "lập 60 vòng và 120 vòng, nối với hai điện trở lần lượt 6,0 Ω và 12 Ω. "
   "Cường độ dòng điện hiệu dụng ở cuộn sơ cấp bằng bao nhiêu ampe?",
   "0,3",
   "Cuộn 60 vòng: U = 240 · 60/1200 = 12 V ⇒ P₁ = 12²/6,0 = 24 W.\n"
   "Cuộn 120 vòng: U = 240 · 120/1200 = 24 V ⇒ P₂ = 24²/12 = 48 W.\n"
   "Tổng công suất lấy từ cuộn sơ cấp: P = 24 + 48 = 72 W.\n"
   "I₁ = P/U₁ = 72/240 = 0,30 A.",
   "Máy biến áp nhiều cuộn thứ cấp", RK),

sa("Một khung dây vuông cạnh 20 cm, điện trở 0,50 Ω, được kéo đều với tốc độ 3,0 m/s ra khỏi vùng "
   "từ trường đều B = 0,50 T. Công của lực kéo trong suốt quá trình đó bằng bao nhiêu milijun?",
   "12",
   "Lực kéo cân bằng lực từ cản: F = B²a²v/R = (0,50² · 0,20²/0,50)·3,0 = "
   "(0,25 · 0,040/0,50) · 3,0 = 0,020 · 3,0 = 0,060 N.\n"
   "Quãng đường kéo bằng cạnh khung: s = 0,20 m.\n"
   "A = F·s = 0,060 · 0,20 = 0,012 J = 12 mJ.",
   "Công và năng lượng trong cảm ứng điện từ", RK),

sa("Hai dây dẫn thẳng dài song song cách nhau 15 cm mang hai dòng điện ngược chiều có cường độ "
   "4,0 A và 10,0 A. Điểm có cảm ứng từ tổng hợp bằng không cách dây mang dòng 4,0 A một khoảng "
   "bao nhiêu centimét?",
   "10",
   "Hai dòng ngược chiều ⇒ điểm triệt tiêu nằm NGOÀI khoảng hai dây, về phía dây có dòng nhỏ hơn.\n"
   "Gọi khoảng cách tới dây 4,0 A là x thì tới dây 10,0 A là x + 15.\n"
   "4,0/x = 10,0/(x + 15) ⇒ 4,0(x + 15) = 10,0x ⇒ 60 = 6,0x ⇒ x = 10 cm.",
   "Từ trường của hai dòng điện", K),
])


# =====================================================================  ĐỀ 10
DE10 = dict(
ma="12C3-Đ10", ten="ĐỀ SỐ 10", muc="Khó – phân loại học sinh giỏi",
trongtam="Tổng hợp vectơ cảm ứng từ, hệ truyền tải hai cấp, khung dây qua vùng từ trường hẹp",
P1=[
mc("Hai dây dẫn thẳng dài song song, vuông góc với mặt phẳng hình vẽ, đi qua hai điểm A và B cách "
   "nhau 10 cm, mang hai dòng điện cùng chiều I₁ = I₂ = 6,0 A. Xét điểm M sao cho MA = 6,0 cm và "
   "MB = 8,0 cm. Cảm ứng từ tổng hợp tại M có độ lớn",
   ["0,50·10⁻⁵ T.", "2,5·10⁻⁵ T.", "3,5·10⁻⁵ T.", "1,5·10⁻⁵ T."],
   "B",
   "Vì 6² + 8² = 10² nên tam giác MAB vuông tại M, tức MA ⊥ MB.\n"
   "B₁ = 2·10⁻⁷ · 6,0/0,060 = 2,0·10⁻⁵ T;  B₂ = 2·10⁻⁷ · 6,0/0,080 = 1,5·10⁻⁵ T.\n"
   "Mỗi vectơ cảm ứng từ vuông góc với bán kính tương ứng, mà hai bán kính vuông góc nhau "
   "nên hai vectơ cũng vuông góc nhau.\n"
   "B = √(2,0² + 1,5²)·10⁻⁵ = √6,25 · 10⁻⁵ = 2,5·10⁻⁵ T.",
   "Tổng hợp vectơ cảm ứng từ", RK),

mc("Một khung dây vuông cạnh 30 cm chuyển động đều với tốc độ v đi qua một vùng từ trường đều "
   "có bề rộng chỉ 20 cm (nhỏ hơn cạnh khung), các đường sức vuông góc mặt phẳng khung. "
   "Trong quá trình đi qua, khoảng thời gian KHÔNG có dòng điện cảm ứng ứng với quãng đường",
   ["20 cm.", "10 cm.", "30 cm.", "0 cm — luôn có dòng."],
   "B",
   "Khi cạnh trước đã ra khỏi vùng mà cạnh sau vẫn chưa vào vùng, phần khung nằm trong từ trường "
   "luôn là một dải rộng đúng 20 cm nên từ thông không đổi, không có dòng cảm ứng.\n"
   "Giai đoạn đó kéo dài từ lúc khung đi được 20 cm tới lúc đi được 30 cm, tức quãng đường 10 cm.",
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

mc("Một khung dây N vòng, diện tích mỗi vòng S, điện trở R, đặt trong từ trường đều B vuông góc "
   "mặt phẳng khung. Quay khung đúng 180° quanh một trục nằm trong mặt phẳng khung. "
   "Điện lượng chuyển qua tiết diện dây bằng",
   ["N·B·S/R.", "2·N·B·S/R.", "N·B·S/(2R).", "4·N·B·S/R."],
   "B",
   "Từ thông ban đầu qua mỗi vòng là +B·S; sau khi quay 180° pháp tuyến đảo chiều nên từ thông "
   "là −B·S.\n"
   "|ΔΦ| mỗi vòng = 2·B·S ⇒ q = N·|ΔΦ|/R = 2·N·B·S/R.\n"
   "Nhiều học sinh chỉ lấy N·B·S/R vì quên rằng từ thông đổi DẤU chứ không chỉ về 0.",
   "Điện lượng khi quay khung 180°", RK),

mc("Một khung dây quay đều tạo suất điện động e = E₀·sin(ωt). Khoảng thời gian ngắn nhất giữa hai "
   "lần liên tiếp độ lớn suất điện động bằng E₀/√2 là",
   ["T/8.", "T/4.", "T/2.", "T/12."],
   "B",
   "|sin(ωt)| = 1/√2 khi ωt = π/4, 3π/4, 5π/4, 7π/4.\n"
   "Hai nghiệm liên tiếp cách nhau π/2 rad, ứng với thời gian T/4.",
   "Dòng xoay chiều – khoảng thời gian", K),

mc("Điện năng từ một nhà máy được truyền tới nơi tiêu thụ qua hai cấp biến áp. Máy tăng áp có tỉ số "
   "vòng 1 : 20, điện áp máy phát là 5,0 kV. Công suất truyền đi là 1,0 MW, điện trở đường dây 8,0 Ω. "
   "Máy hạ áp cuối đường dây có tỉ số vòng 40 : 1. Điện áp ở đầu ra của máy hạ áp xấp xỉ",
   ["2500 V.", "2480 V.", "2400 V.", "2000 V."],
   "B",
   "Điện áp đầu đường dây: U = 20 · 5,0 = 100 kV.\n"
   "Dòng trên đường dây: I = 10⁶/10⁵ = 10 A.\n"
   "Độ sụt áp trên đường dây: ΔU = R·I = 8,0 · 10 = 80 V.\n"
   "Điện áp cuối đường dây: 100 000 − 80 = 99 920 V.\n"
   "Qua máy hạ áp 40 : 1 ⇒ U(ra) = 99 920/40 = 2498 V ≈ 2480 V (phương án gần nhất).",
   "Hệ truyền tải hai cấp biến áp", RK, fig="t_sd_truyen_tai",
   cap="Sơ đồ truyền tải điện năng"),

mc("Một đoạn dây dẫn nằm ngang trong khe nam châm, đặt trên cân điện tử. Khi cho dòng điện chạy "
   "theo một chiều thì cân chỉ tăng thêm 15 g; khi đảo chiều dòng điện, so với lúc không có dòng "
   "thì số chỉ của cân",
   ["vẫn tăng 15 g.", "giảm 15 g.", "không đổi.", "giảm 30 g."],
   "B",
   "Đảo chiều dòng điện thì lực từ đổi chiều nhưng giữ nguyên độ lớn. Vì vậy thay vì ép thêm 15 g "
   "lên cân, nó nâng bớt 15 g: số chỉ giảm 15 g so với khi không có dòng. "
   "Chênh lệch giữa hai lần đo là 30 g.",
   "Cân dòng điện – đảo chiều", K, fig="t_sd_can_dong_dien", cap="Thí nghiệm cân dòng điện"),

mc("Một khung dây dẫn kín được kéo với tốc độ không đổi ra khỏi vùng từ trường đều. Nếu tăng tốc độ "
   "kéo lên gấp ba thì tổng NHIỆT LƯỢNG toả ra trên khung trong suốt quá trình",
   ["không đổi.", "tăng gấp ba.", "tăng gấp chín.", "giảm ba lần."],
   "B",
   "Nhiệt lượng Q = (e²/R)·Δt với e = B·a·v và Δt = a/v.\n"
   "Q = (B²a²v²/R)·(a/v) = B²a³v/R — tỉ lệ THUẬN với v.\n"
   "Tăng v gấp ba thì Q tăng gấp ba (dòng mạnh hơn 3 lần nhưng thời gian ngắn hơn 3 lần, "
   "kết quả là nhiệt lượng tăng 3 lần chứ không phải 9 lần).",
   "Năng lượng trong cảm ứng điện từ", RK),

mc("Hai dây dẫn thẳng dài song song cách nhau 20 cm mang hai dòng điện cùng chiều I₁ = 10 A, "
   "I₂ = 30 A. Cảm ứng từ tổng hợp bằng không tại điểm cách dây I₂ một khoảng",
   ["5,0 cm.", "15 cm.", "10 cm.", "20 cm."],
   "B",
   "Điểm triệt tiêu nằm giữa hai dây, gần dây có dòng nhỏ hơn. Gọi khoảng cách tới dây I₁ là x:\n"
   "10/x = 30/(20 − x) ⇒ 10(20 − x) = 30x ⇒ 200 = 40x ⇒ x = 5,0 cm.\n"
   "Vậy khoảng cách tới dây I₂ là 20 − 5,0 = 15 cm.",
   "Từ trường của hai dòng điện", K),

mc("Một khung dây 100 vòng, diện tích mỗi vòng 50 cm², điện trở 2,0 Ω, đặt vuông góc với từ trường "
   "đều B = 0,40 T. Quay khung 180° quanh trục nằm trong mặt phẳng khung. "
   "Điện lượng chuyển qua tiết diện dây bằng",
   ["0,10 C.", "0,20 C.", "0,40 C.", "0,05 C."],
   "B",
   "|ΔΦ| mỗi vòng = 2·B·S = 2 · 0,40 · 5,0·10⁻³ = 4,0·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 100 · 4,0·10⁻³/2,0 = 0,40/2,0 = 0,20 C.",
   "Điện lượng khi quay khung 180°", RK),

mc("Truyền tải điện năng với công suất và điện trở đường dây không đổi. Khi điện áp là U thì hiệu "
   "suất là 90 %. Muốn hiệu suất tăng lên 99 % thì điện áp phải tăng lên gấp",
   ["√10 lần.", "10 lần.", "3 lần.", "√5 lần."],
   "A",
   "Hao phí giảm từ 10 % xuống 1 %, tức giảm 10 lần.\n"
   "Vì hao phí tỉ lệ nghịch với U² nên U² tăng 10 lần ⇒ U tăng √10 ≈ 3,16 lần.",
   "Truyền tải – bài toán tỉ lệ", K, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một thanh dẫn khối lượng m nằm trên hai ray nằm ngang không ma sát trong từ trường đều thẳng "
   "đứng B, chiều dài thanh ℓ, điện trở toàn mạch R. Truyền cho thanh vận tốc ban đầu v₀. "
   "Tổng nhiệt lượng toả ra cho tới khi thanh dừng hẳn bằng",
   ["m·v₀·B·ℓ/R.", "½·m·v₀².", "B²ℓ²v₀/R.", "m·v₀²/R."],
   "B",
   "Không có ma sát và không có lực kéo nên toàn bộ động năng ban đầu của thanh chuyển hoá thành "
   "nhiệt trên điện trở mạch: Q = ½·m·v₀².\n"
   "Kết quả này hoàn toàn không phụ thuộc B, ℓ hay R — các đại lượng đó chỉ quyết định thanh dừng "
   "nhanh hay chậm.",
   "Bảo toàn năng lượng", RK, fig="t_sd_ray_ngang", cap="Thanh dẫn trên hai ray"),

mc("Một khung dây quay đều trong từ trường đều. Trong một chu kì, tỉ số giữa khoảng thời gian mà "
   "|e| ≥ E₀/√2 và khoảng thời gian mà |e| < E₀/√2 bằng",
   ["1 : 2.", "1 : 1.", "2 : 1.", "1 : 3."],
   "B",
   "Điều kiện |sin(ωt)| ≥ 1/√2 thoả mãn trên tổng cộng nửa chu kì; phần còn lại cũng đúng nửa "
   "chu kì. Vậy tỉ số là 1 : 1.",
   "Dòng xoay chiều – tỉ lệ thời gian", K, fig="t_dt_i_t",
   cap="Cường độ dòng điện xoay chiều theo thời gian"),

mc("Một máy biến áp lí tưởng có cuộn sơ cấp N₁ vòng. Khi cuộn thứ cấp có N₂ vòng thì điện áp thứ "
   "cấp là 20 V; khi bớt đi 30 vòng ở cuộn thứ cấp thì điện áp còn 17 V. Số vòng N₁ bằng "
   "(điện áp sơ cấp giữ nguyên 200 V)",
   ["1000 vòng.", "2000 vòng.", "1500 vòng.", "2500 vòng."],
   "B",
   "Mỗi vòng thứ cấp ứng với điện áp: (20 − 17)/30 = 0,10 V/vòng.\n"
   "Suy ra N₂ = 20/0,10 = 200 vòng.\n"
   "Từ U₂/U₁ = N₂/N₁ ⇒ N₁ = N₂·U₁/U₂ = 200 · 200/20 = 2000 vòng.",
   "Máy biến áp – hệ hai phương trình", RK, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

mc("Một khung dây quay đều trong từ trường đều, tạo ra suất điện động có giá trị cực đại E₀ và "
   "được nối với một điện trở thuần R. Công suất trung bình tiêu thụ trên điện trở bằng",
   ["E₀²/R.", "E₀²/(2R).", "2·E₀²/R.", "E₀²/(4R)."],
   "B",
   "Công suất trung bình được tính theo GIÁ TRỊ HIỆU DỤNG: P = E²/R với E = E₀/√2.\n"
   "P = (E₀/√2)²/R = E₀²/(2R).\n"
   "Lấy thẳng E₀²/R sẽ cho kết quả lớn gấp đôi giá trị thật — đây là sai lầm rất phổ biến.",
   "Công suất của máy phát", RK),

mc("Một đoạn dây dẫn thẳng dài 20 cm mang dòng điện 5,0 A được đặt trong từ trường đều B = 0,30 T "
   "sao cho lực từ có độ lớn 0,15 N. Có bao nhiêu giá trị của góc α (trong khoảng từ 0° đến 180°) "
   "thoả mãn điều kiện đó?",
   ["1 giá trị.", "2 giá trị.", "3 giá trị.", "4 giá trị."],
   "B",
   "sinα = F/(B·I·ℓ) = 0,15/(0,30 · 5,0 · 0,20) = 0,15/0,30 = 0,50.\n"
   "Trong khoảng 0° đến 180° phương trình sinα = 0,50 có hai nghiệm: α = 30° và α = 150°.",
   "Vai trò của góc α", K, fig="t_sd_goc_alpha", cap="Dây hợp góc α với đường sức"),

mc("Một nhà máy truyền công suất P đi xa. Khi tăng điện áp truyền tải lên gấp đôi thì số hộ dân "
   "được cung cấp điện tăng từ 6000 lên 7500 hộ. Hiệu suất truyền tải ban đầu bằng",
   ["60 %.", "80 %.", "75 %.", "90 %."],
   "C",
   "Gọi hiệu suất ban đầu là H thì hao phí chiếm (1 − H). Tăng U gấp đôi ⇒ hao phí giảm 4 lần, "
   "hiệu suất mới là 1 − (1 − H)/4.\n"
   "Số hộ tỉ lệ với công suất tới nơi tiêu thụ: [1 − (1 − H)/4]/H = 7500/6000 = 1,25.\n"
   "1 − (1 − H)/4 = 1,25H ⇒ 4 − 1 + H = 5H ⇒ 3 = 4H ⇒ H = 0,75.\n"
   "Kiểm tra: hiệu suất mới = 1 − 0,25/4 = 0,9375;  0,9375/0,75 = 1,25 ✓. "
   "Vậy hiệu suất ban đầu là 75 %.",
   "Truyền tải – bài toán ngược", RK, fig="t_sd_truyen_tai", cap="Truyền tải điện năng"),

mc("Một khung dây phẳng quay đều quanh trục nằm trong mặt phẳng khung và vuông góc với từ trường đều. "
   "So sánh suất điện động TRUNG BÌNH khi khung quay từ vị trí từ thông cực đại tới vị trí từ thông "
   "bằng 0 với suất điện động CỰC ĐẠI của khung:",
   ["trung bình lớn hơn cực đại.", "trung bình nhỏ hơn cực đại.",
    "hai giá trị bằng nhau.", "không so sánh được."],
   "B",
   "Suất điện động trung bình trong một phần tư chu kì: |e| = Φ₀/(T/4) = 4Φ₀/T = (2/π)·ωΦ₀ "
   "≈ 0,637·E₀.\n"
   "Giá trị này nhỏ hơn E₀ = ωΦ₀. Về nguyên tắc giá trị trung bình của một đại lượng luôn không "
   "vượt quá giá trị cực đại của nó.",
   "Phân biệt giá trị trung bình và cực đại", RK),

mc("Trong thí nghiệm thả một nam châm rơi qua ống đồng dày thẳng đứng, nếu cắt một rãnh dọc suốt "
   "chiều dài ống thì nam châm sẽ",
   ["rơi chậm hơn trước.", "rơi nhanh hơn hẳn, gần như rơi tự do.",
    "không rơi được.", "rơi với tốc độ không đổi ngay từ đầu."],
   "B",
   "Rãnh dọc cắt đứt đường đi khép kín của dòng điện xoáy quanh chu vi ống, nên dòng Foucault "
   "gần như biến mất. Không còn lực cản đáng kể, nam châm rơi gần như tự do.",
   "Dòng Foucault – thí nghiệm nâng cao", RK, fig="t_sd_dong_fuco", cap="Dòng điện Foucault"),
],
P2=[
ds("Một khung dây vuông cạnh 40 cm, điện trở 0,80 Ω, chuyển động đều với tốc độ 2,0 m/s theo phương "
   "vuông góc với biên của một vùng từ trường đều B = 0,50 T chỉ rộng 25 cm "
   "(hẹp hơn cạnh khung). Các đường sức vuông góc mặt phẳng khung.",
   [("Khi khung bắt đầu đi vào, suất điện động cảm ứng là 0,40 V.", True,
     "Đúng. e = B·a·v = 0,50 · 0,40 · 2,0 = 0,40 V (a là cạnh khung song song với biên vùng)."),
    ("Có một giai đoạn khung nằm vắt qua vùng từ trường mà trong khung không có dòng cảm ứng.", True,
     "Đúng. Khi cạnh trước đã ra khỏi vùng còn cạnh sau chưa vào, phần khung nằm trong từ trường "
     "luôn là dải rộng 25 cm nên từ thông không đổi."),
    ("Giai đoạn không có dòng cảm ứng kéo dài 0,075 s.", True,
     "Đúng. Giai đoạn đó ứng với quãng đường 40 − 25 = 15 cm, thời gian = 0,15/2,0 = 0,075 s."),
    ("Trong giai đoạn khung đi ra, dòng điện cảm ứng cùng chiều với lúc khung đi vào.", False,
     "Sai. Lúc vào từ thông tăng, lúc ra từ thông giảm, nên theo định luật Lenz hai dòng cảm ứng "
     "NGƯỢC chiều nhau.")],
   "Khung dây qua vùng từ trường hẹp", RK, fig="t_sd_khung_vao_B",
   cap="Khung dây đi qua vùng từ trường"),

ds("Một thanh dẫn khối lượng 150 g, dài 60 cm nằm trên hai ray nằm ngang không ma sát trong từ "
   "trường đều thẳng đứng B = 0,50 T. Điện trở toàn mạch 0,30 Ω. Truyền cho thanh vận tốc ban đầu "
   "4,0 m/s rồi để tự do.",
   [("Tổng nhiệt lượng toả ra trên mạch cho tới khi thanh dừng hẳn bằng 1,2 J.", True,
     "Đúng. Toàn bộ động năng chuyển thành nhiệt: Q = ½mv₀² = 0,5 · 0,150 · 4,0² = 1,2 J."),
    ("Tổng điện lượng chuyển qua mạch bằng 2,0 C.", True,
     "Đúng. B·ℓ·q = m·v₀ ⇒ q = 0,150 · 4,0/(0,50 · 0,60) = 0,60/0,30 = 2,0 C."),
    ("Nếu tăng điện trở mạch lên gấp đôi thì tổng nhiệt lượng toả ra giảm một nửa.", False,
     "Sai. Tổng nhiệt lượng luôn bằng động năng ban đầu, không phụ thuộc điện trở. "
     "Điện trở chỉ làm thanh dừng chậm hơn."),
    ("Nếu tăng điện trở mạch lên gấp đôi thì tổng điện lượng chuyển qua mạch giảm một nửa.", False,
     "Sai. Từ B·ℓ·q = m·v₀ suy ra q = m·v₀/(B·ℓ), hoàn toàn không chứa R. "
     "Điện lượng giữ nguyên 2,0 C; chỉ có thời gian dừng là dài gấp đôi.")],
   "Bảo toàn năng lượng và xung lượng", RK, fig="t_sd_ray_ngang",
   cap="Thanh dẫn trên hai ray nằm ngang"),

ds("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi 200 V. Khi cuộn thứ cấp có N₂ vòng thì "
   "điện áp thứ cấp là 20 V; khi bớt 30 vòng ở cuộn thứ cấp thì điện áp thứ cấp còn 17 V.",
   [("Mỗi vòng dây thứ cấp ứng với điện áp 0,10 V.", True,
     "Đúng. (20 − 17)/30 = 0,10 V mỗi vòng."),
    ("Số vòng ban đầu của cuộn thứ cấp là 200 vòng.", True,
     "Đúng. N₂ = 20/0,10 = 200 vòng."),
    ("Số vòng của cuộn sơ cấp là 2000 vòng.", True,
     "Đúng. N₁ = N₂·U₁/U₂ = 200 · 200/20 = 2000 vòng."),
    ("Muốn điện áp thứ cấp đạt 25 V thì phải quấn thêm 30 vòng nữa.", False,
     "Sai. Cần N = 25/0,10 = 250 vòng, tức phải quấn thêm 250 − 200 = 50 vòng chứ không phải 30.")],
   "Máy biến áp – hệ hai phương trình", RK, fig="t_sd_may_bien_ap", cap="Máy biến áp"),

ds("Xét quá trình truyền tải điện năng đi xa bằng dòng điện xoay chiều.",
   [("Công suất hao phí trên đường dây tỉ lệ nghịch với bình phương điện áp truyền tải.", True,
     "Đúng. ΔP = R·I² với I = P/U nên ΔP = R·P²/U²."),
    ("Muốn giảm hao phí 100 lần mà giữ nguyên công suất truyền đi thì phải tăng điện áp 10 lần.", True,
     "Đúng. Hao phí tỉ lệ nghịch với U² nên U phải tăng √100 = 10 lần."),
    ("Máy hạ áp đặt ở cuối đường dây cũng góp phần làm giảm hao phí trên đường dây.", False,
     "Sai. Hao phí chỉ sinh ra trên đoạn đường dây TRƯỚC máy hạ áp. Máy hạ áp chỉ có nhiệm vụ đưa "
     "điện áp về mức an toàn cho hộ tiêu thụ."),
    ("Với cùng một công suất truyền đi, dùng dây dẫn có tiết diện lớn hơn cũng làm giảm hao phí.", True,
     "Đúng. Tiết diện lớn hơn ⇒ điện trở nhỏ hơn ⇒ hao phí nhỏ hơn. Tuy nhiên cách này tốn nhiều "
     "kim loại nên đắt hơn nhiều so với việc tăng điện áp.")],
   "Truyền tải điện năng – nhận định", K),
],
P3=[
sa("Hai dây dẫn thẳng dài song song vuông góc với mặt phẳng hình vẽ, đi qua hai điểm A và B cách "
   "nhau 25 cm, mang hai dòng điện cùng chiều I₁ = I₂ = 10 A. Xét điểm M với MA = 15 cm và MB = 20 cm. "
   "Cảm ứng từ tổng hợp tại M bằng bao nhiêu micrôtesla (làm tròn đến hàng đơn vị)?",
   "17",
   "Vì 15² + 20² = 225 + 400 = 625 = 25² nên tam giác MAB vuông tại M, hai bán kính vuông góc nhau.\n"
   "B₁ = 2·10⁻⁷ · 10/0,15 ≈ 1,333·10⁻⁵ T;  B₂ = 2·10⁻⁷ · 10/0,20 = 1,0·10⁻⁵ T.\n"
   "Hai vectơ vuông góc nên B = √(1,333² + 1,0²)·10⁻⁵ = √2,777 · 10⁻⁵ ≈ 1,667·10⁻⁵ T = 17 μT.",
   "Tổng hợp vectơ cảm ứng từ", RK),

sa("Một khung dây 200 vòng, diện tích mỗi vòng 40 cm², điện trở 1,6 Ω, đặt vuông góc với từ trường "
   "đều B = 0,20 T. Quay khung đúng 180° quanh trục nằm trong mặt phẳng khung. "
   "Điện lượng chuyển qua tiết diện dây bằng bao nhiêu culông?",
   "0,2",
   "Từ thông qua mỗi vòng đổi từ +B·S sang −B·S nên |ΔΦ| = 2·B·S = 2 · 0,20 · 4,0·10⁻³ "
   "= 1,6·10⁻³ Wb.\n"
   "q = N·|ΔΦ|/R = 200 · 1,6·10⁻³/1,6 = 0,32/1,6 = 0,20 C.",
   "Điện lượng khi quay khung 180°", RK),

sa("Một máy biến áp lí tưởng có điện áp sơ cấp không đổi 240 V. Khi cuộn thứ cấp có N vòng thì điện "
   "áp thứ cấp là 24 V; khi quấn thêm 25 vòng thì điện áp thứ cấp là 29 V. "
   "Số vòng của cuộn sơ cấp bằng bao nhiêu?",
   "1200",
   "Mỗi vòng thứ cấp ứng với (29 − 24)/25 = 0,20 V.\n"
   "Số vòng ban đầu: N = 24/0,20 = 120 vòng.\n"
   "N₁ = N·U₁/U₂ = 120 · 240/24 = 1200 vòng.",
   "Máy biến áp – hệ hai phương trình", RK),

sa("Một thanh dẫn khối lượng 250 g nằm trên hai ray nằm ngang không ma sát trong từ trường đều "
   "thẳng đứng. Truyền cho thanh vận tốc ban đầu 6,0 m/s rồi để tự do. "
   "Tổng nhiệt lượng toả ra trên mạch cho tới khi thanh dừng hẳn bằng bao nhiêu jun?",
   "4,5",
   "Không có ma sát, không có lực kéo nên toàn bộ động năng ban đầu chuyển thành nhiệt:\n"
   "Q = ½·m·v₀² = 0,5 · 0,250 · 6,0² = 0,5 · 0,250 · 36 = 4,5 J.\n"
   "Kết quả không phụ thuộc B, ℓ hay R.",
   "Bảo toàn năng lượng", RK),

sa("Một thanh dẫn dài 40 cm, khối lượng 100 g được thả từ nghỉ trên hai ray nghiêng góc 30°, "
   "không ma sát, trong từ trường đều B = 0,50 T vuông góc với mặt phẳng nghiêng. "
   "Điện trở toàn mạch 0,20 Ω. Khi gia tốc của thanh còn bằng một nửa gia tốc lúc vừa thả, "
   "tốc độ của thanh bằng bao nhiêu mét trên giây? Lấy g = 10 m/s².",
   "1,25",
   "Lúc vừa thả, v = 0 nên chưa có lực từ: a₀ = g·sin30° = 10 · 0,50 = 5,0 m/s².\n"
   "Ở tốc độ v: m·a = m·g·sin30° − B²ℓ²v/R.\n"
   "B²ℓ²/R = 0,50² · 0,40²/0,20 = 0,25 · 0,16/0,20 = 0,20.\n"
   "Điều kiện a = a₀/2 = 2,5 m/s²:  0,100 · 2,5 = 0,100 · 5,0 − 0,20·v\n"
   "0,25 = 0,50 − 0,20·v ⇒ 0,20·v = 0,25 ⇒ v = 1,25 m/s.",
   "Thanh dẫn trên mặt nghiêng – gia tốc biến đổi", RK),

sa("Một khung dây vuông cạnh 50 cm chuyển động đều đi qua một vùng từ trường đều rộng 30 cm với "
   "tốc độ 2,5 m/s, các đường sức vuông góc mặt phẳng khung. Trong suốt quá trình đi qua, "
   "tổng thời gian KHÔNG có dòng điện cảm ứng trong khung bằng bao nhiêu giây?",
   "0,08",
   "Vì bề rộng vùng (30 cm) nhỏ hơn cạnh khung (50 cm) nên có giai đoạn cạnh trước đã ra khỏi vùng "
   "mà cạnh sau chưa vào: phần khung nằm trong từ trường luôn là dải rộng 30 cm, từ thông không đổi.\n"
   "Giai đoạn đó ứng với quãng đường 50 − 30 = 20 cm.\n"
   "Thời gian = 0,20/2,5 = 0,080 s.",
   "Khung dây qua vùng từ trường hẹp", RK),
])


NHOM = dict(
    ten_nhom="LỚP 12 – CHƯƠNG 3: TỪ TRƯỜNG",
    mo_ta="Bộ 10 đề luyện tập, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó, phân loại học sinh giỏi)",
    pham_vi=(
        "Bài 14. Từ trường. Đường sức từ  •  Bài 15. Lực từ. Cảm ứng từ\n"
        "Bài 16. Từ thông. Hiện tượng cảm ứng điện từ. Định luật Faraday và Lenz\n"
        "Bài 17. Đại cương về dòng điện xoay chiều  •  Ứng dụng: máy biến áp, truyền tải điện năng, "
        "dòng Foucault, bếp từ, sạc không dây\n"
        "Quy ước dùng thống nhất: g = 10 m/s²; √2 ≈ 1,414; π ≈ 3,1416. "
        "Mọi giá trị điện áp và cường độ dòng điện ghi trên thiết bị đều là GIÁ TRỊ HIỆU DỤNG."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
