# -*- coding: utf-8 -*-
"""BÀI TẬP TÍNH TOÁN – CHƯƠNG III: TỪ TRƯỜNG."""

CALC3 = {

"Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn": [
dict(q="Một đoạn dây dẫn thẳng dài 20 cm mang dòng điện 5 A được đặt vuông góc với các đường sức của một từ "
       "trường đều có cảm ứng từ 0,02 T. Lực từ tác dụng lên đoạn dây có độ lớn",
 o=["0,002 N.", "0,02 N.", "0,2 N.", "2 N."],
 a="B",
 sol="Đổi ℓ = 20 cm = 0,2 m. Vì dây vuông góc với B nên θ = 90°, sinθ = 1.\n"
     "F = BIℓ = 0,02 · 5 · 0,2 = 0,02 N."),

dict(q="Một đoạn dây dẫn dài 50 cm mang dòng điện 2 A đặt vuông góc với từ trường đều thì chịu lực từ 0,04 N. "
       "Cảm ứng từ của từ trường đó bằng",
 o=["0,02 T.", "0,04 T.", "0,4 T.", "4 T."],
 a="B",
 sol="Từ F = BIℓ suy ra B = F/(Iℓ) = 0,04/(2 · 0,5) = 0,04 T."),

dict(q="Một đoạn dây dẫn dài 10 cm mang dòng điện 4 A đặt trong từ trường đều B = 0,5 T sao cho dây hợp với "
       "đường sức từ một góc 30°. Lực từ tác dụng lên đoạn dây bằng",
 o=["0,05 N.", "0,10 N.", "0,17 N.", "0,20 N."],
 a="B",
 sol="F = BIℓsinθ = 0,5 · 4 · 0,1 · sin30° = 0,5 · 4 · 0,1 · 0,5 = 0,10 N.\n"
     "Phương án 0,20 N ứng với sai lầm bỏ quên hệ số sinθ; phương án 0,17 N ứng với việc nhầm sang cos30°."),

dict(q="Một khung dây phẳng gồm 100 vòng, mỗi vòng có diện tích 0,05 m², đặt trong từ trường đều B = 0,4 T sao "
       "cho mặt phẳng khung vuông góc với các đường sức từ. Từ thông qua khung dây bằng",
 o=["0,02 Wb.", "0,2 Wb.", "2 Wb.", "20 Wb."],
 a="C",
 sol="Mặt phẳng khung vuông góc với đường sức nghĩa là pháp tuyến song song với B, tức α = 0 và cosα = 1.\n"
     "Φ = NBScosα = 100 · 0,4 · 0,05 · 1 = 2 Wb."),

dict(q="Từ thông qua mỗi vòng dây của một khung dây gồm 50 vòng giảm đều từ 0,06 Wb xuống 0,02 Wb trong thời "
       "gian 0,1 s. Suất điện động cảm ứng xuất hiện trong khung có độ lớn",
 o=["0,4 V.", "2 V.", "20 V.", "200 V."],
 a="C",
 sol="Độ biến thiên từ thông qua mỗi vòng: |ΔΦ₁| = 0,06 − 0,02 = 0,04 Wb.\n"
     "|e| = N·|ΔΦ₁|/Δt = 50 · 0,04/0,1 = 20 V."),

dict(q="Một thanh dẫn dài 0,5 m trượt đều với tốc độ 4 m/s trên hai thanh ray, trong từ trường đều B = 0,2 T "
       "vuông góc với mặt phẳng chứa hai ray. Suất điện động cảm ứng xuất hiện trên thanh bằng",
 o=["0,1 V.", "0,4 V.", "1,0 V.", "4,0 V."],
 a="B",
 sol="e = Bℓv = 0,2 · 0,5 · 4 = 0,4 V."),

dict(q="Một dòng điện xoay chiều có biểu thức i = 2√2·cos(100πt) (A), với t tính bằng giây. Cường độ dòng điện "
       "hiệu dụng và tần số của dòng điện lần lượt là",
 o=["2√2 A và 50 Hz.", "2 A và 50 Hz.", "2 A và 100 Hz.", "2√2 A và 100 Hz."],
 a="B",
 sol="Biên độ I₀ = 2√2 A nên I = I₀/√2 = 2 A.\n"
     "Tần số góc ω = 100π rad/s ⟹ f = ω/(2π) = 100π/(2π) = 50 Hz."),

dict(q="Điện áp giữa hai đầu một đoạn mạch có biểu thức u = 220√2·cos(100πt) (V). Điện áp hiệu dụng và chu kì "
       "của điện áp này lần lượt là",
 o=["220 V và 0,02 s.", "220√2 V và 0,02 s.", "220 V và 0,01 s.", "311 V và 0,02 s."],
 a="A",
 sol="U = U₀/√2 = 220√2/√2 = 220 V. Từ ω = 100π suy ra T = 2π/ω = 2π/(100π) = 0,02 s.\n"
     "Giá trị 311 V chính là U₀ = 220√2, không phải điện áp hiệu dụng."),

dict(q="Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng, cuộn thứ cấp 200 vòng. Đặt vào hai đầu cuộn sơ cấp "
       "điện áp xoay chiều có giá trị hiệu dụng 220 V. Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng",
 o=["44 V.", "110 V.", "440 V.", "1100 V."],
 a="A",
 sol="U₂ = U₁·N₂/N₁ = 220 · 200/1000 = 44 V. Vì N₂ < N₁ nên đây là máy hạ áp."),

dict(q="Một máy biến áp lí tưởng dùng để tăng điện áp từ 220 V lên 6600 V. Nếu cuộn sơ cấp có 400 vòng thì cuộn "
       "thứ cấp có số vòng là",
 o=["1200 vòng.", "6000 vòng.", "12 000 vòng.", "13 200 vòng."],
 a="C",
 sol="Từ U₁/U₂ = N₁/N₂ suy ra N₂ = N₁·U₂/U₁ = 400 · 6600/220 = 400 · 30 = 12 000 vòng."),

dict(q="Một khung dây gồm 200 vòng, diện tích mỗi vòng 0,02 m², quay đều trong từ trường đều B = 0,1 T với tần "
       "số góc ω = 100π rad/s quanh trục vuông góc với B. Suất điện động cực đại trong khung xấp xỉ",
 o=["12,6 V.", "40,0 V.", "125,7 V.", "400,0 V."],
 a="C",
 sol="E₀ = NBSω = 200 · 0,1 · 0,02 · 100π = 0,4 · 314,16 ≈ 125,7 V."),

dict(q="Một vòng dây kín có điện trở 0,4 Ω đặt trong từ trường biến thiên. Khi từ thông qua vòng dây biến thiên "
       "một lượng 0,02 Wb thì điện lượng chuyển qua tiết diện dây bằng",
 o=["0,008 C.", "0,05 C.", "0,5 C.", "8 C."],
 a="B",
 sol="q = |ΔΦ|/R = 0,02/0,4 = 0,05 C. Lưu ý điện lượng này không phụ thuộc vào việc từ thông biến thiên nhanh "
     "hay chậm, tức không phụ thuộc Δt."),

dict(q="Một sóng điện từ có tần số 90 MHz truyền trong chân không. Bước sóng của nó xấp xỉ",
 o=["0,33 m.", "3,33 m.", "33,3 m.", "333 m."],
 a="B",
 sol="λ = c/f = 3·10⁸/(90·10⁶) ≈ 3,33 m."),

dict(q="Truyền tải công suất điện 100 kW đi xa bằng đường dây có điện trở tổng cộng 5 Ω, điện áp ở nơi truyền đi "
       "là 10 kV, hệ số công suất bằng 1. Công suất hao phí trên đường dây bằng",
 o=["50 W.", "500 W.", "5 kW.", "50 kW."],
 a="B",
 sol="Cường độ dòng điện trên đường dây: I = P/U = 10⁵/10⁴ = 10 A.\n"
     "Công suất hao phí: ΔP = I²R = 10² · 5 = 500 W. (Có thể tính trực tiếp ΔP = RP²/U² = 5·(10⁵)²/(10⁴)² = 500 W.)"),

dict(q="Với dữ kiện của câu trên (P = 100 kW, ΔP = 500 W), hiệu suất truyền tải điện năng bằng",
 o=["95,0%.", "99,0%.", "99,5%.", "99,95%."],
 a="C",
 sol="H = (P − ΔP)/P = (100 000 − 500)/100 000 = 0,995 = 99,5%."),

dict(q="Một dòng điện xoay chiều có cường độ cực đại 4 A chạy qua một điện trở thuần 10 Ω. Công suất toả nhiệt "
       "trung bình trên điện trở bằng",
 o=["40 W.", "80 W.", "160 W.", "320 W."],
 a="B",
 sol="Cường độ hiệu dụng I = I₀/√2 = 4/√2 = 2√2 A, suy ra I² = 8 A².\n"
     "P = I²R = 8 · 10 = 80 W. Sai lầm hay gặp là dùng I₀ để tính, cho ra 160 W."),

dict(q="Một khung dây gồm 100 vòng, diện tích mỗi vòng 0,01 m², quay đều trong từ trường đều B = 0,2 T với tần số "
       "50 vòng/giây quanh trục vuông góc với B. Suất điện động cực đại trong khung xấp xỉ",
 o=["6,28 V.", "62,8 V.", "100 V.", "628 V."],
 a="B",
 sol="ω = 2πf = 2π·50 ≈ 314,16 rad/s.\n"
     "E₀ = NBSω = 100 · 0,2 · 0,01 · 314,16 = 0,2 · 314,16 ≈ 62,8 V."),

dict(q="Trong thí nghiệm cân dòng điện, một đoạn dây dài 4 cm nằm ngang trong từ trường đều B = 0,5 T, vuông góc "
       "với đường sức, mang dòng điện 2 A. Lấy g = 10 m/s². Số chỉ của cân thay đổi một lượng",
 o=["0,4 g.", "4 g.", "40 g.", "400 g."],
 a="B",
 sol="Lực từ: F = BIℓ = 0,5 · 2 · 0,04 = 0,04 N.\n"
     "Từ F = Δm·g suy ra Δm = F/g = 0,04/10 = 0,004 kg = 4 g."),
],

"Dạng 2 – Câu trắc nghiệm đúng/sai": [
dict(stem="Một đoạn dây dẫn thẳng dài ℓ = 0,20 m mang dòng điện I = 3,0 A được đặt trong một từ trường đều có "
          "cảm ứng từ B = 0,25 T. Gọi θ là góc giữa đoạn dây và vectơ cảm ứng từ.",
 fig="f05_goc_theta",
 items=[
  ("Khi θ = 90°, lực từ tác dụng lên đoạn dây có độ lớn 0,15 N.", True,
   "F = BIℓsin90° = 0,25 · 3,0 · 0,20 = 0,15 N."),
  ("Khi θ = 30°, lực từ tác dụng lên đoạn dây có độ lớn 0,075 N.", True,
   "F = 0,25 · 3,0 · 0,20 · sin30° = 0,15 · 0,5 = 0,075 N."),
  ("Khi đoạn dây được đặt song song với đường sức từ thì lực từ tác dụng lên nó bằng không.", True,
   "Khi đó θ = 0° hoặc 180°, sinθ = 0 nên F = 0."),
  ("Nếu tăng cường độ dòng điện lên gấp đôi đồng thời giảm chiều dài đoạn dây nằm trong từ trường còn một nửa "
   "(vẫn giữ θ = 90°) thì lực từ tăng gấp đôi.", False,
   "F = B(2I)(ℓ/2) = BIℓ, tức lực từ KHÔNG đổi vì hai tác dụng bù trừ nhau."),
 ]),

dict(stem="Một khung dây dẫn phẳng gồm N = 200 vòng, diện tích mỗi vòng S = 100 cm², đặt trong từ trường đều sao "
          "cho mặt phẳng khung vuông góc với các đường sức. Cảm ứng từ tăng đều từ 0 đến 0,50 T trong thời gian "
          "0,20 s. Điện trở của khung là R = 5,0 Ω.",
 items=[
  ("Độ biến thiên từ thông qua mỗi vòng dây là 0,005 Wb.", True,
   "S = 100 cm² = 0,01 m²; |ΔΦ₁| = ΔB·S = 0,50 · 0,01 = 0,005 Wb."),
  ("Suất điện động cảm ứng xuất hiện trong khung có độ lớn 5,0 V.", True,
   "|e| = N|ΔΦ₁|/Δt = 200 · 0,005/0,20 = 5,0 V."),
  ("Cường độ dòng điện cảm ứng chạy trong khung là 1,0 A.", True,
   "i = |e|/R = 5,0/5,0 = 1,0 A."),
  ("Nếu thời gian tăng cảm ứng từ kéo dài 0,40 s thay vì 0,20 s thì điện lượng chuyển qua khung tăng gấp đôi.", False,
   "q = N|ΔΦ₁|/R = 200 · 0,005/5,0 = 0,20 C, chỉ phụ thuộc độ biến thiên từ thông và điện trở, "
   "hoàn toàn không phụ thuộc thời gian. Điện lượng vẫn là 0,20 C."),
 ]),

dict(stem="Một máy phát điện xoay chiều có phần ứng gồm N = 500 vòng dây, diện tích mỗi vòng S = 200 cm², quay "
          "đều trong từ trường đều B = 0,20 T với tốc độ 600 vòng/phút quanh trục vuông góc với vectơ cảm ứng từ.",
 fig="f10_may_phat",
 items=[
  ("Tần số của suất điện động do máy phát ra là 10 Hz.", True,
   "n = 600 vòng/phút = 10 vòng/giây, ứng với f = 10 Hz và ω = 2π·10 ≈ 62,83 rad/s."),
  ("Suất điện động cực đại của máy xấp xỉ 126 V.", True,
   "S = 200 cm² = 0,02 m²; E₀ = NBSω = 500 · 0,20 · 0,02 · 62,83 = 2,0 · 62,83 ≈ 125,7 V."),
  ("Suất điện động hiệu dụng của máy xấp xỉ 88,9 V.", True,
   "E = E₀/√2 = 125,7/1,414 ≈ 88,9 V."),
  ("Nếu tăng tốc độ quay lên 1200 vòng/phút thì suất điện động hiệu dụng vẫn xấp xỉ 126 V.", False,
   "E₀ tỉ lệ thuận với ω nên khi tốc độ quay tăng gấp đôi, E₀ ≈ 251,3 V và E ≈ 177,8 V, không phải 126 V."),
 ]),

dict(stem="Cần truyền một công suất điện P = 200 kW từ nhà máy đến nơi tiêu thụ bằng đường dây có điện trở tổng "
          "cộng R = 4,0 Ω. Điện áp hiệu dụng ở nơi truyền đi là U = 5,0 kV, hệ số công suất của mạch bằng 1.",
 fig="f13_bien_ap",
 items=[
  ("Cường độ dòng điện hiệu dụng trên đường dây tải điện là 20 A.", False,
   "I = P/U = 200 000/5 000 = 40 A chứ không phải 20 A."),
  ("Công suất hao phí trên đường dây là 6,4 kW.", True,
   "ΔP = I²R = 40² · 4,0 = 6 400 W = 6,4 kW."),
  ("Hiệu suất của quá trình truyền tải điện năng là 96,8%.", True,
   "H = (200 − 6,4)/200 = 0,968 = 96,8%."),
  ("Nếu dùng máy tăng áp để nâng điện áp truyền đi lên 20 kV (giữ nguyên công suất truyền) thì công suất hao phí "
   "chỉ còn 0,4 kW.", True,
   "Điện áp tăng 4 lần nên hao phí giảm 4² = 16 lần: ΔP' = 6,4/16 = 0,4 kW."),
 ]),

dict(stem="Một thanh kim loại MN dài ℓ = 0,50 m trượt đều với tốc độ v = 6,0 m/s trên hai thanh ray nằm ngang, "
          "trong từ trường đều B = 0,40 T hướng vuông góc với mặt phẳng chứa hai ray. Mạch kín có điện trở tổng "
          "cộng R = 3,0 Ω, bỏ qua ma sát và điện trở của thanh.",
 fig="f16_thanh_truot",
 items=[
  ("Suất điện động cảm ứng xuất hiện trên thanh là 1,2 V.", True, "e = Bℓv = 0,40 · 0,50 · 6,0 = 1,2 V."),
  ("Cường độ dòng điện chạy trong mạch là 0,40 A.", True, "i = e/R = 1,2/3,0 = 0,40 A."),
  ("Lực từ tác dụng lên thanh có độ lớn 0,080 N và hướng ngược chiều chuyển động.", True,
   "F = Biℓ = 0,40 · 0,40 · 0,50 = 0,080 N; theo định luật Lenz lực này cản trở chuyển động."),
  ("Nếu tăng tốc độ của thanh lên gấp đôi thì công suất toả nhiệt trên mạch cũng tăng gấp đôi.", False,
   "P = e²/R tỉ lệ với v², nên khi v tăng gấp đôi thì công suất toả nhiệt tăng 4 lần (từ 0,48 W lên 1,92 W)."),
 ]),

dict(stem="Một máy biến áp lí tưởng có cuộn sơ cấp gồm 4000 vòng được mắc vào mạng điện xoay chiều 220 V – 50 Hz. "
          "Cuộn thứ cấp gồm 200 vòng và được nối với một điện trở thuần R = 11 Ω.",
 items=[
  ("Điện áp hiệu dụng ở hai đầu cuộn thứ cấp là 11 V.", True, "U₂ = U₁·N₂/N₁ = 220 · 200/4000 = 11 V."),
  ("Cường độ dòng điện hiệu dụng chạy qua điện trở là 1,0 A.", True, "I₂ = U₂/R = 11/11 = 1,0 A."),
  ("Cường độ dòng điện hiệu dụng ở cuộn sơ cấp là 0,05 A.", True,
   "Với máy lí tưởng U₁I₁ = U₂I₂ nên I₁ = U₂I₂/U₁ = 11 · 1,0/220 = 0,05 A."),
  ("Công suất tiêu thụ ở cuộn sơ cấp là 220 W.", False,
   "P₁ = U₁I₁ = 220 · 0,05 = 11 W, đúng bằng công suất tiêu thụ trên điện trở ở cuộn thứ cấp (P₂ = 11 · 1,0 = 11 W)."),
 ]),
],

"Dạng 3 – Câu trả lời ngắn": [
dict(q="Một đoạn dây dẫn thẳng dài 12 cm mang dòng điện 2,5 A đặt vuông góc với từ trường đều có cảm ứng từ "
       "0,8 T. Tính độ lớn lực từ tác dụng lên đoạn dây (đơn vị: N).",
 ans="0,24 N",
 sol="F = BIℓ = 0,8 · 2,5 · 0,12 = 0,24 N."),

dict(q="Một đoạn dây dẫn dài 25 cm đặt vuông góc với từ trường đều B = 0,3 T thì chịu lực từ có độ lớn 0,15 N. "
       "Tính cường độ dòng điện chạy qua dây (đơn vị: A).",
 ans="2 A",
 sol="I = F/(Bℓ) = 0,15/(0,3 · 0,25) = 0,15/0,075 = 2 A."),

dict(q="Một đoạn dây dẫn dài 30 cm mang dòng điện 6 A đặt trong từ trường đều B = 0,2 T, dây hợp với đường sức "
       "từ góc 45°. Tính độ lớn lực từ tác dụng lên đoạn dây (đơn vị: N, làm tròn đến hai chữ số thập phân).",
 ans="0,25 N",
 sol="F = BIℓsinθ = 0,2 · 6 · 0,3 · sin45° = 0,36 · 0,7071 ≈ 0,2546 N ≈ 0,25 N."),

dict(q="Một khung dây gồm 250 vòng, diện tích mỗi vòng 40 cm², đặt trong từ trường đều B = 0,05 T. Pháp tuyến "
       "của mặt phẳng khung hợp với vectơ cảm ứng từ một góc 60°. Tính từ thông qua khung dây (đơn vị: Wb).",
 ans="0,025 Wb",
 sol="S = 40 cm² = 4·10⁻³ m².\nΦ = NBScosα = 250 · 0,05 · 4·10⁻³ · cos60° = 0,05 · 0,5 = 0,025 Wb."),

dict(q="Từ thông qua một vòng dây dẫn kín giảm đều từ 0,12 Wb xuống 0 trong thời gian 0,05 s. Tính độ lớn suất "
       "điện động cảm ứng xuất hiện trong vòng dây (đơn vị: V).",
 ans="2,4 V",
 sol="|e| = |ΔΦ|/Δt = 0,12/0,05 = 2,4 V."),

dict(q="Một khung dây gồm 80 vòng. Từ thông qua mỗi vòng dây biến thiên một lượng 0,004 Wb trong thời gian 0,02 s. "
       "Tính độ lớn suất điện động cảm ứng trong khung (đơn vị: V).",
 ans="16 V",
 sol="|e| = N·|ΔΦ₁|/Δt = 80 · 0,004/0,02 = 16 V."),

dict(q="Khung dây ở câu trên có điện trở 8 Ω. Tính cường độ dòng điện cảm ứng chạy trong khung (đơn vị: A).",
 ans="2 A",
 sol="i = |e|/R = 16/8 = 2 A."),

dict(q="Trong một mạch kín có điện trở 6 Ω, từ thông qua mạch biến thiên một lượng 0,3 Wb. Tính điện lượng "
       "chuyển qua tiết diện thẳng của dây dẫn trong thời gian đó (đơn vị: C).",
 ans="0,05 C",
 sol="q = |ΔΦ|/R = 0,3/6 = 0,05 C."),

dict(q="Một thanh dẫn dài 0,6 m trượt đều trên hai ray đặt trong từ trường đều B = 0,3 T vuông góc với mặt phẳng "
       "chứa hai ray, tạo ra suất điện động cảm ứng 0,9 V. Tính tốc độ trượt của thanh (đơn vị: m/s).",
 ans="5 m/s",
 sol="Từ e = Bℓv suy ra v = e/(Bℓ) = 0,9/(0,3 · 0,6) = 0,9/0,18 = 5 m/s."),

dict(q="Một điện áp xoay chiều có biểu thức u = 120√2·cos(120πt) (V), t tính bằng giây. Tính tần số của điện áp "
       "này (đơn vị: Hz).",
 ans="60 Hz",
 sol="f = ω/(2π) = 120π/(2π) = 60 Hz."),

dict(q="Một dòng điện xoay chiều có biểu thức i = 5·cos(100πt) (A). Tính cường độ dòng điện hiệu dụng "
       "(đơn vị: A, làm tròn đến hai chữ số thập phân).",
 ans="3,54 A",
 sol="I = I₀/√2 = 5/1,414 ≈ 3,54 A."),

dict(q="Cho dòng điện ở câu trên chạy qua điện trở thuần R = 20 Ω. Tính công suất toả nhiệt trung bình trên "
       "điện trở (đơn vị: W).",
 ans="250 W",
 sol="I² = (I₀/√2)² = I₀²/2 = 25/2 = 12,5 A².\nP = I²R = 12,5 · 20 = 250 W."),

dict(q="Một máy biến áp lí tưởng có cuộn sơ cấp 2200 vòng được mắc vào điện áp xoay chiều 220 V. Muốn điện áp ở "
       "cuộn thứ cấp là 12 V thì cuộn thứ cấp phải có bao nhiêu vòng dây?",
 ans="120 vòng",
 sol="N₂ = N₁·U₂/U₁ = 2200 · 12/220 = 120 vòng."),

dict(q="Một máy phát điện xoay chiều có phần ứng gồm 400 vòng dây, diện tích mỗi vòng 0,015 m², quay đều trong "
       "từ trường đều B = 0,25 T với tốc độ 300 vòng/phút. Tính suất điện động cực đại của máy "
       "(đơn vị: V, làm tròn đến một chữ số thập phân).",
 ans="47,1 V",
 sol="n = 300 vòng/phút = 5 vòng/giây ⟹ ω = 2π·5 ≈ 31,42 rad/s.\n"
     "E₀ = NBSω = 400 · 0,25 · 0,015 · 31,42 = 1,5 · 31,42 ≈ 47,1 V."),

dict(q="Truyền tải công suất điện 500 kW đi xa với điện áp truyền đi 25 kV, hệ số công suất bằng 1, đường dây có "
       "điện trở tổng cộng 10 Ω. Tính công suất hao phí trên đường dây (đơn vị: kW).",
 ans="4 kW",
 sol="I = P/U = 5·10⁵/(2,5·10⁴) = 20 A.\nΔP = I²R = 20² · 10 = 4000 W = 4 kW."),

dict(q="Với dữ kiện câu trên, tính hiệu suất truyền tải điện năng (đơn vị: %, làm tròn đến một chữ số thập phân).",
 ans="99,2%",
 sol="H = (P − ΔP)/P = (500 − 4)/500 = 0,992 = 99,2%."),

dict(q="Một sóng điện từ truyền trong chân không có bước sóng 2 m. Tính tần số của sóng (đơn vị: MHz).",
 ans="150 MHz",
 sol="f = c/λ = 3·10⁸/2 = 1,5·10⁸ Hz = 150 MHz."),

dict(q="Trong thí nghiệm đo cảm ứng từ bằng cân dòng điện, đoạn dây dài 5,0 cm đặt vuông góc với đường sức từ, "
       "mang dòng điện 1,5 A thì số chỉ của cân thay đổi 3,06 g. Lấy g = 9,8 m/s². Tính cảm ứng từ trong khe nam "
       "châm (đơn vị: T, làm tròn đến hai chữ số thập phân).",
 fig="f06_can_dong_dien",
 ans="0,40 T",
 sol="F = Δm·g = 3,06·10⁻³ · 9,8 = 0,029988 N.\n"
     "B = F/(Iℓ) = 0,029988/(1,5 · 0,05) = 0,029988/0,075 ≈ 0,40 T."),
],

"Dạng 4 – Bài tập tự luận và vận dụng cao": [
dict(q="Từ thông qua một vòng dây dẫn kín có điện trở R = 0,20 Ω biến thiên theo thời gian như đồ thị.\n"
       "a) Tính độ lớn suất điện động cảm ứng trong vòng dây ở từng giai đoạn.\n"
       "b) Vẽ phác đồ thị biểu diễn suất điện động cảm ứng theo thời gian.\n"
       "c) Tính điện lượng chuyển qua tiết diện dây trong giai đoạn từ 4 s đến 5 s.",
 fig="f15_phi_gap_khuc",
 ans="a) 0,4 V; 0; 0,6 V; 0.  b) Đồ thị bậc thang.  c) q = 3 C.",
 sol="a) Độ lớn suất điện động bằng độ lớn hệ số góc của đồ thị Φ(t):\n"
     "  • Giai đoạn (1) từ 0 đến 2 s: Φ tăng từ 0 đến 0,8 Wb ⟹ |e| = 0,8/2 = 0,4 V.\n"
     "  • Giai đoạn (2) từ 2 s đến 4 s: Φ không đổi ⟹ |e| = 0.\n"
     "  • Giai đoạn (3) từ 4 s đến 5 s: Φ giảm từ 0,8 xuống 0,2 Wb ⟹ |e| = 0,6/1 = 0,6 V.\n"
     "  • Giai đoạn (4) từ 5 s đến 8 s: Φ không đổi ⟹ |e| = 0.\n"
     "b) Đồ thị e(t) có dạng bậc thang: bằng −0,4 V trong 0 – 2 s (dấu trừ vì Φ tăng), bằng 0 trong 2 – 4 s, "
     "bằng +0,6 V trong 4 – 5 s (Φ giảm nên dòng cảm ứng đổi chiều), bằng 0 trong 5 – 8 s.\n"
     "c) q = |ΔΦ|/R = 0,6/0,20 = 3 C.\n"
     "Nhận xét quan trọng: giai đoạn có từ thông NHỎ nhất lại cho suất điện động LỚN nhất, vì suất điện động "
     "phụ thuộc tốc độ biến thiên chứ không phụ thuộc giá trị của từ thông."),

dict(q="Một khung dây quay đều trong từ trường đều, tạo ra suất điện động e = E₀sinωt trong khi từ thông qua "
       "khung là Φ = Φ₀cosωt.\n"
       "a) Chứng minh rằng ở mọi thời điểm ta luôn có (Φ/Φ₀)² + (e/E₀)² = 1.\n"
       "b) Tại thời điểm từ thông có độ lớn bằng 0,6Φ₀, tính độ lớn suất điện động theo E₀.\n"
       "c) Giải thích vì sao khi từ thông bằng không thì suất điện động lại đạt cực đại.",
 fig="f11_phi_e",
 ans="b) |e| = 0,8·E₀.",
 sol="a) Ta có Φ/Φ₀ = cosωt và e/E₀ = sinωt. Cộng bình phương hai vế:\n"
     "  (Φ/Φ₀)² + (e/E₀)² = cos²ωt + sin²ωt = 1 (điều phải chứng minh).\n"
     "b) Thay Φ/Φ₀ = 0,6 vào hệ thức trên: (e/E₀)² = 1 − 0,36 = 0,64 ⟹ |e| = 0,8·E₀.\n"
     "c) Khi mặt phẳng khung song song với các đường sức thì Φ = 0. Đúng lúc đó, các cạnh của khung chuyển động "
     "vuông góc với đường sức nên quét được nhiều đường sức nhất trong một đơn vị thời gian, tức tốc độ biến thiên "
     "|ΔΦ/Δt| là lớn nhất, do đó |e| cực đại. Về mặt toán học, đồ thị Φ(t) có độ dốc lớn nhất tại điểm nó cắt trục "
     "hoành."),

dict(q="Một nhóm học sinh khác lặp lại phép đo cảm ứng từ bằng cân dòng điện với một nam châm hình chữ U rộng hơn: "
       "phần dây nằm trong từ trường dài ℓ = 10,0 cm, đặt vuông góc với các đường sức. Kết quả đo được như sau "
       "(lấy g = 9,8 m/s²):\n"
       "I (A):    0,5    1,0    1,5    2,0\n"
       "Δm (g):  1,53   3,06   4,59   6,12\n"
       "a) Tính lực từ ứng với mỗi giá trị của cường độ dòng điện.\n"
       "b) Nhận xét về dạng đồ thị F theo I và tính hệ số góc của đồ thị đó.\n"
       "c) Xác định cảm ứng từ B trong khe nam châm.\n"
       "d) Nêu hai nguyên nhân có thể gây sai số hệ thống trong phép đo này và cho biết chúng làm B đo được "
       "lớn hơn hay nhỏ hơn giá trị thực.",
 fig="f06_can_dong_dien",
 ans="a) 0,015; 0,030; 0,045; 0,060 N.  b) Đường thẳng qua gốc, hệ số góc 0,030 N/A.  c) B = 0,30 T.",
 sol="a) F = Δm·g:\n"
     "  I = 0,5 A: F = 1,53·10⁻³ · 9,8 ≈ 0,015 N\n"
     "  I = 1,0 A: F ≈ 0,030 N;  I = 1,5 A: F ≈ 0,045 N;  I = 2,0 A: F ≈ 0,060 N.\n"
     "b) Bốn điểm nằm trên một đường thẳng đi qua gốc toạ độ, phù hợp với F = (Bℓ)·I. "
     "Hệ số góc: k = ΔF/ΔI = (0,060 − 0,015)/(2,0 − 0,5) = 0,045/1,5 = 0,030 N/A.\n"
     "c) Vì k = Bℓ nên B = k/ℓ = 0,030/0,10 = 0,30 T.\n"
     "d) Hai nguyên nhân sai số hệ thống:\n"
     "  • Đoạn dây không thật vuông góc với đường sức: khi đó F thực = BIℓsinθ < BIℓ, số chỉ Δm nhỏ hơn, "
     "làm B đo được NHỎ HƠN giá trị thực.\n"
     "  • Chưa hiệu chỉnh cân về 0 trước khi đóng mạch, hoặc từ trường ở mép nam châm không đều nên phần dây "
     "ngoài vùng đều vẫn chịu lực: có thể làm B đo được lớn hơn hoặc nhỏ hơn tuỳ chiều lệch, cần khắc phục bằng "
     "cách đo nhiều lần và lấy trung bình."),

dict(q="Một khung dây dẫn hình vuông cạnh a = 0,20 m, điện trở R = 0,50 Ω, chuyển động thẳng đều với tốc độ "
       "v = 2,0 m/s ra khỏi một vùng từ trường đều B = 0,40 T (đường sức vuông góc với mặt phẳng khung), theo "
       "phương vuông góc với biên của vùng từ trường.\n"
       "a) Tính suất điện động cảm ứng và cường độ dòng điện cảm ứng trong khung khi khung đang ra khỏi vùng "
       "từ trường.\n"
       "b) Tính độ lớn lực từ tác dụng lên khung và cho biết chiều của nó.\n"
       "c) Tính nhiệt lượng toả ra trên khung trong toàn bộ quá trình khung ra khỏi vùng từ trường và so sánh "
       "với công của ngoại lực.",
 ans="a) e = 0,16 V; i = 0,32 A.  b) F = 0,0256 N, ngược chiều chuyển động.  c) Q = 5,12·10⁻³ J.",
 sol="a) Chỉ cạnh nằm trong vùng từ trường mới đóng vai trò thanh dẫn chuyển động:\n"
     "  e = Bav = 0,40 · 0,20 · 2,0 = 0,16 V;  i = e/R = 0,16/0,50 = 0,32 A.\n"
     "b) F = B·i·a = 0,40 · 0,32 · 0,20 = 0,0256 N. Theo định luật Lenz, lực này ngược chiều vận tốc, "
     "tức có xu hướng giữ khung lại trong vùng từ trường.\n"
     "c) Thời gian khung đi ra hết: t = a/v = 0,20/2,0 = 0,10 s.\n"
     "  Nhiệt lượng: Q = i²R·t = 0,32² · 0,50 · 0,10 = 0,1024 · 0,05 = 5,12·10⁻³ J.\n"
     "  Công của ngoại lực (bằng công thắng lực từ để khung đi đều): A = F·v·t = 0,0256 · 2,0 · 0,10 = 5,12·10⁻³ J.\n"
     "  Hai giá trị bằng nhau, thể hiện đúng định luật bảo toàn năng lượng: công cơ học của ngoại lực đã chuyển "
     "hoá hoàn toàn thành nhiệt năng trên khung."),

dict(q="Một thanh dẫn khối lượng m = 0,20 kg, chiều dài ℓ = 0,40 m, trượt không ma sát trên hai thanh ray nằm "
       "ngang trong từ trường đều B = 0,50 T vuông góc với mặt phẳng ray. Mạch kín có điện trở R = 2,0 Ω. "
       "Từ trạng thái nghỉ, người ta kéo thanh bằng một lực không đổi F = 0,50 N theo phương ngang.\n"
       "a) Giải thích vì sao tốc độ của thanh không tăng mãi mà tiến tới một giá trị giới hạn.\n"
       "b) Tính tốc độ giới hạn đó.\n"
       "c) Khi thanh đạt tốc độ giới hạn, tính công suất của lực kéo và công suất toả nhiệt trên mạch.",
 ans="b) v_max = 25 m/s.  c) P = 12,5 W cho cả hai.",
 sol="a) Khi thanh chuyển động, xuất hiện suất điện động e = Bℓv, dòng điện i = Bℓv/R và lực từ cản "
     "F_c = B²ℓ²v/R. Lực cản này TĂNG theo tốc độ. Khi tốc độ đủ lớn để F_c = F, hợp lực bằng không, "
     "gia tốc bằng không và thanh chuyển động đều với tốc độ giới hạn.\n"
     "b) Từ điều kiện F = B²ℓ²v_max/R:\n"
     "  v_max = F·R/(B²ℓ²) = 0,50 · 2,0/(0,50² · 0,40²) = 1,0/(0,25 · 0,16) = 1,0/0,04 = 25 m/s.\n"
     "c) Công suất của lực kéo: P = F·v_max = 0,50 · 25 = 12,5 W.\n"
     "  Suất điện động: e = Bℓv = 0,50 · 0,40 · 25 = 5,0 V; dòng điện i = 5,0/2,0 = 2,5 A;\n"
     "  Công suất toả nhiệt: P = i²R = 2,5² · 2,0 = 12,5 W.\n"
     "  Hai công suất bằng nhau vì ở chế độ chuyển động đều, động năng không đổi nên toàn bộ công của lực kéo "
     "chuyển thành nhiệt."),

dict(q="Một nhà máy điện phát ra công suất P = 1,0 MW ở điện áp 5,0 kV. Điện năng được đưa qua một máy tăng áp "
       "rồi truyền đi trên đường dây có điện trở tổng cộng R = 20 Ω. Coi các máy biến áp là lí tưởng và hệ số "
       "công suất bằng 1.\n"
       "a) Nếu truyền tải ngay ở điện áp 5,0 kV thì công suất hao phí trên đường dây là bao nhiêu? Nhận xét.\n"
       "b) Người ta dùng máy tăng áp có tỉ số vòng dây N₂/N₁ = 20. Tính điện áp truyền đi và công suất hao phí "
       "khi đó.\n"
       "c) Tính hiệu suất truyền tải trong trường hợp b).",
 fig="f13_bien_ap",
 ans="a) ΔP = 800 kW (80%).  b) U = 100 kV; ΔP = 2,0 kW.  c) H = 99,8%.",
 sol="a) I = P/U = 10⁶/(5·10³) = 200 A;  ΔP = I²R = 200² · 20 = 8,0·10⁵ W = 800 kW.\n"
     "  Nhận xét: hao phí chiếm tới 80% công suất phát — hoàn toàn không thể chấp nhận được trong thực tế. "
     "Đây chính là lí do bắt buộc phải tăng áp trước khi truyền tải.\n"
     "b) U' = U·N₂/N₁ = 5,0 · 20 = 100 kV.  I' = P/U' = 10⁶/10⁵ = 10 A.\n"
     "  ΔP' = I'²R = 10² · 20 = 2000 W = 2,0 kW.\n"
     "  (Kiểm tra nhanh: điện áp tăng 20 lần thì hao phí giảm 20² = 400 lần: 800/400 = 2,0 kW ✓)\n"
     "c) H = (P − ΔP')/P = (1000 − 2,0)/1000 = 0,998 = 99,8%."),

dict(q="Cần truyền công suất điện P = 120 kW đi xa trên đường dây có điện trở tổng cộng R = 6,0 Ω, hệ số công "
       "suất bằng 1. Yêu cầu hiệu suất truyền tải phải đạt ít nhất 98%.\n"
       "a) Tính công suất hao phí tối đa cho phép.\n"
       "b) Xác định điện áp tối thiểu phải dùng ở nơi truyền đi.\n"
       "c) Nếu máy phát tạo ra điện áp 600 V thì máy tăng áp phải có tỉ số số vòng dây giữa cuộn thứ cấp và "
       "cuộn sơ cấp tối thiểu bằng bao nhiêu?",
 ans="a) 2,4 kW.  b) U ≥ 6000 V.  c) N₂/N₁ ≥ 10.",
 sol="a) Hiệu suất H = (P − ΔP)/P ≥ 0,98 ⟹ ΔP ≤ 0,02·P = 0,02 · 120 000 = 2400 W = 2,4 kW.\n"
     "b) ΔP = RP²/U² ≤ 2400 ⟹ U² ≥ RP²/2400 = 6,0 · (1,2·10⁵)²/2400 = 6,0 · 1,44·10¹⁰/2400 = 3,6·10⁷.\n"
     "  Vậy U ≥ 6,0·10³ V = 6000 V.\n"
     "c) N₂/N₁ = U₂/U₁ ≥ 6000/600 = 10.\n"
     "Bài toán này thuộc dạng “suy luận ngược”: từ yêu cầu về hiệu suất tìm ra thông số kĩ thuật cần thiết, "
     "đúng với cách tư duy của kĩ sư khi thiết kế hệ thống truyền tải."),

dict(q="Một học sinh muốn tăng suất điện động cực đại của một máy phát điện xoay chiều lên gấp đôi và đề xuất "
       "hai phương án:\n"
       "  Phương án A: tăng tốc độ quay của rôto lên gấp đôi.\n"
       "  Phương án B: tăng số vòng dây của phần ứng lên gấp đôi.\n"
       "a) Cả hai cách làm có đạt được mục tiêu không? Giải thích bằng công thức.\n"
       "b) Hai phương án khác nhau ở điểm nào về tần số của dòng điện phát ra?\n"
       "c) Nếu máy phát này được dùng để cấp điện cho mạng điện dân dụng 50 Hz thì nên chọn phương án nào? Vì sao?",
 ans="a) Cả hai đều làm E₀ tăng gấp đôi.  b) Phương án A làm tần số tăng gấp đôi, phương án B không đổi.  "
     "c) Chọn phương án B.",
 sol="a) Suất điện động cực đại E₀ = NBSω tỉ lệ thuận với cả N và ω. Do đó:\n"
     "  • Cách thứ nhất: ω tăng 2 lần ⟹ E₀ tăng 2 lần.\n"
     "  • Cách thứ hai: N tăng 2 lần ⟹ E₀ tăng 2 lần.\n"
     "  Cả hai đều đạt mục tiêu về suất điện động.\n"
     "b) Tần số f = ω/(2π) chỉ phụ thuộc tốc độ quay. Cách tăng tốc độ quay làm tần số tăng gấp đôi "
     "(từ 50 Hz lên 100 Hz), còn cách tăng số vòng dây hoàn toàn không ảnh hưởng tần số.\n"
     "c) Phải chọn cách tăng số vòng dây. Mạng điện dân dụng yêu cầu tần số chuẩn 50 Hz; nếu tăng tốc độ quay "
     "thì tần số trở thành 100 Hz, làm các thiết bị điện (đặc biệt là động cơ điện và máy biến áp) hoạt động sai lệch. "
     "Đây là ví dụ cho thấy khi giải bài toán kĩ thuật, phải xét đồng thời nhiều ràng buộc chứ không chỉ một "
     "đại lượng mục tiêu."),
],
}
