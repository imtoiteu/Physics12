# -*- coding: utf-8 -*-
"""LỚP 12 – ĐỀ TỔNG HỢP CHƯƠNG 1 + CHƯƠNG 2.  10 đề, độ khó tăng dần.

Mỗi đề đều có những câu BẮT BUỘC phải dùng đồng thời kiến thức của cả hai chương:
định luật I nhiệt động lực học (chương 1) và phương trình trạng thái / mô hình động
học phân tử (chương 2).
Quy ước dùng chung: nội năng khí lí tưởng đơn nguyên tử U = (3/2)nRT = (3/2)pV;
công khí sinh ra trong quá trình đẳng áp A′ = p·ΔV.
"""
from de_12c1 import mc, ds, sa, D, TB, K, RK


# =====================================================================
DE1 = dict(
ma="MIX-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Nối kết nội năng – nhiệt độ – trạng thái khí ở mức nhận biết và thông hiểu",
P1=[
mc("Nội năng của một lượng khí lí tưởng xác định phụ thuộc vào",
   ["áp suất của khí.", "thể tích của khí.", "nhiệt độ của khí.", "khối lượng riêng của khí."],
   "C",
   "Với khí lí tưởng, thế năng tương tác phân tử được bỏ qua nên nội năng chỉ là tổng động năng chuyển "
   "động nhiệt — đại lượng chỉ phụ thuộc nhiệt độ.",
   "Nội năng khí lí tưởng (C1 + C2)", D),

mc("Cung cấp nhiệt lượng Q cho khí trong một bình kín có thể tích không đổi. Khi đó",
   ["ΔU = Q.", "ΔU = −Q.", "ΔU = 0.", "ΔU = 2Q."],
   "A",
   "Thể tích không đổi ⟹ khí không nhận và không sinh công (A = 0) ⟹ ΔU = A + Q = Q.\n"
   "Toàn bộ nhiệt lượng chuyển thành nội năng, làm nhiệt độ và áp suất khí tăng.",
   "Định luật I + quá trình đẳng tích", D),

mc("Trong quá trình đẳng nhiệt của một lượng khí lí tưởng, độ biến thiên nội năng của khí bằng",
   ["Q.", "A.", "0.", "A + 2Q."],
   "C",
   "Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ; đẳng nhiệt nên T không đổi ⟹ ΔU = 0 (khi đó Q = −A).",
   "Định luật I + quá trình đẳng nhiệt", D),

mc("Công mà khí sinh ra khi giãn nở đẳng áp ở áp suất p, thể tích tăng thêm ΔV, bằng",
   ["A′ = p/ΔV.", "A′ = p·ΔV.", "A′ = ΔV/p.", "A′ = p + ΔV."],
   "B", "A′ = p·ΔV; đơn vị Pa·m³ = J, đúng thứ nguyên của công.",
   "Công của khí (C1 + C2)", D),

mc("Một khối khí giãn nở đẳng áp ở áp suất 2,0·10⁵ Pa, thể tích tăng từ 2,0 L lên 5,0 L. Công khí sinh ra là",
   ["300 J.", "600 J.", "1000 J.", "1400 J."],
   "B", "A′ = p·ΔV = 2,0·10⁵ · (5,0 − 2,0)·10⁻³ = 2,0·10⁵ · 3,0·10⁻³ = 600 J.",
   "Công của khí (C1 + C2)", D),

mc("Nhiệt độ 127 °C ứng với nhiệt độ tuyệt đối là",
   ["300 K.", "350 K.", "400 K.", "450 K."],
   "C", "T = 127 + 273 = 400 K.", "Thang nhiệt độ", D),

mc("Nén đẳng nhiệt một lượng khí lí tưởng từ 6,0 L xuống 3,0 L. Nếu áp suất ban đầu là 1,0·10⁵ Pa thì áp "
   "suất sau khi nén là",
   ["0,5·10⁵ Pa.", "1,5·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa."],
   "C", "p₂ = p₁V₁/V₂ = 1,0·10⁵ · 6,0/3,0 = 2,0·10⁵ Pa.", "Định luật Boyle", D),

mc("Đun nóng đẳng áp một lượng khí từ 300 K lên 450 K. Thể tích ban đầu 4,0 L. Thể tích lúc sau là",
   ["2,7 L.", "5,0 L.", "6,0 L.", "9,0 L."],
   "C", "V₂ = V₁·T₂/T₁ = 4,0 · 450/300 = 6,0 L.", "Định luật Charles", D),

mc("Nhiệt lượng cần cung cấp để đun 1,0 kg nước từ 20 °C lên 70 °C là (c = 4200 J/(kg·K))",
   ["84 kJ.", "126 kJ.", "168 kJ.", "210 kJ."],
   "D", "Q = mcΔt = 1,0 · 4200 · 50 = 210 000 J = 210 kJ.", "Nhiệt dung riêng", D),

mc("Động năng tịnh tiến trung bình của một phân tử khí lí tưởng ở nhiệt độ T là "
   "(k = 1,38·10⁻²³ J/K)",
   ["kT.", "(3/2)kT.", "(2/3)kT.", "3kT."],
   "B", "W̄đ = (3/2)kT. Đây là cầu nối giữa đại lượng vĩ mô (nhiệt độ) và vi mô (động năng phân tử).",
   "Động năng phân tử – nhiệt độ", D),

mc("Khi bơm xe đạp, thân bơm nóng lên chủ yếu vì",
   ["ma sát giữa pit-tông và thành bơm là nguyên nhân duy nhất.",
    "ta thực hiện công nén khí, làm nội năng và nhiệt độ khối khí tăng, sau đó khí truyền nhiệt cho thân bơm.",
    "không khí bên ngoài nóng hơn thân bơm.",
    "khối lượng khí trong bơm tăng lên."],
   "B",
   "Nén nhanh ⟹ Q ≈ 0, khí nhận công A > 0 nên ΔU = A > 0: nhiệt độ khí tăng rồi truyền nhiệt cho thân "
   "bơm. Ma sát chỉ đóng góp một phần nhỏ.",
   "Định luật I + nén khí (C1 + C2)", TB),

mc("Nội năng của một khối khí lí tưởng đơn nguyên tử được tính bằng U = (3/2)pV. Một bình 2,0 L chứa khí "
   "này ở áp suất 1,0·10⁵ Pa. Nội năng của khối khí bằng",
   ["100 J.", "200 J.", "300 J.", "600 J."],
   "C", "U = (3/2)pV = 1,5 · 1,0·10⁵ · 2,0·10⁻³ = 1,5 · 200 = 300 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Một khối khí nhận nhiệt lượng 500 J và sinh công 200 J. Độ biến thiên nội năng của khối khí là",
   ["+700 J.", "+300 J.", "−300 J.", "−700 J."],
   "B", "Q = +500 J, A = −200 J ⟹ ΔU = A + Q = +300 J.",
   "Định luật I nhiệt động lực học", D),

mc("Trong bình kín thể tích không đổi, khi đun nóng khí thì đại lượng nào sau đây KHÔNG đổi?",
   ["Áp suất.", "Nhiệt độ.", "Nội năng.", "Mật độ phân tử."],
   "D",
   "Số phân tử và thể tích đều không đổi nên mật độ phân tử N/V không đổi. Áp suất, nhiệt độ và nội năng "
   "đều tăng.",
   "Đẳng tích – mô hình phân tử (C1 + C2)", TB),

mc("Một lượng khí lí tưởng ở 300 K. Nếu nâng nhiệt độ lên 600 K thì nội năng của khối khí",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "giảm 2 lần."],
   "B",
   "U = (3/2)nRT tỉ lệ thuận với nhiệt độ TUYỆT ĐỐI: T tăng 2 lần thì U tăng 2 lần.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Muốn tính công mà khí sinh ra trong một quá trình bất kì trên giản đồ (p, V), ta xác định",
   ["chiều dài đoạn đường biểu diễn quá trình.",
    "diện tích hình giới hạn bởi đường biểu diễn quá trình và trục V.",
    "hiệu áp suất đầu và cuối.", "tích của áp suất đầu và thể tích cuối."],
   "B",
   "Công khí sinh ra bằng diện tích dưới đường biểu diễn quá trình trên giản đồ (p, V). Với quá trình "
   "đẳng áp, diện tích đó là hình chữ nhật p·ΔV.",
   "Công của khí trên giản đồ p–V", TB),

mc("Đại lượng nào sau đây của một lượng khí lí tưởng đồng thời liên quan tới cả nội năng (chương 1) và "
   "trạng thái khí (chương 2)?",
   ["Khối lượng riêng.", "Áp suất.", "Nhiệt độ.", "Thể tích."],
   "C",
   "Nhiệt độ vừa quyết định nội năng U = (3/2)nRT (chương 1) vừa là một thông số trạng thái trong "
   "pV = nRT (chương 2). Nó cũng là số đo động năng trung bình của phân tử.",
   "Cầu nối hai chương", TB),

mc("Khi giãn nở đẳng nhiệt, khí lí tưởng nhận nhiệt lượng 400 J. Công mà khí sinh ra là",
   ["0 J.", "200 J.", "400 J.", "800 J."],
   "C", "Đẳng nhiệt ⟹ ΔU = 0 ⟹ A = −Q = −400 J, tức khí sinh công đúng 400 J.",
   "Định luật I + đẳng nhiệt", TB),
],
P2=[
ds("Xét mối liên hệ giữa nội năng, nhiệt độ và trạng thái của một lượng khí lí tưởng xác định.",
   [("Nội năng của khí lí tưởng chỉ phụ thuộc nhiệt độ tuyệt đối của nó.", True,
     "Đúng. Bỏ qua thế năng tương tác phân tử nên nội năng chỉ là tổng động năng chuyển động nhiệt, "
     "U = (3/2)nRT."),
    ("Trong quá trình đẳng nhiệt, nội năng của khí không đổi nên khí không trao đổi nhiệt với bên ngoài.", False,
     "Sai ở vế sau. ΔU = 0 chỉ cho A + Q = 0; khí vẫn nhận nhiệt và sinh công đúng bằng nhau. Nếu khí "
     "giãn đẳng nhiệt thì nó nhận nhiệt và sinh công cùng một giá trị."),
    ("Trong quá trình đẳng tích, toàn bộ nhiệt lượng cung cấp cho khí đều làm tăng nội năng.", True,
     "Đúng. Thể tích không đổi ⟹ A = 0 ⟹ ΔU = Q."),
    ("Nếu nhiệt độ tuyệt đối của khí tăng gấp đôi thì nội năng của nó cũng tăng gấp đôi.", True,
     "Đúng. U = (3/2)nRT tỉ lệ thuận với T.")],
   "Nội năng khí lí tưởng (C1 + C2)", TB),

ds("Một khối khí lí tưởng giãn nở đẳng áp ở áp suất 2,0·10⁵ Pa, thể tích tăng từ 2,0 L lên 5,0 L. "
   "Khí nhận được nhiệt lượng 1500 J.",
   [("Công mà khí sinh ra là 600 J.", True,
     "Đúng. A′ = p·ΔV = 2,0·10⁵ · 3,0·10⁻³ = 600 J."),
    ("Độ biến thiên nội năng của khí là 900 J.", True,
     "Đúng. ΔU = A + Q = −600 + 1500 = 900 J."),
    ("Nhiệt độ tuyệt đối của khí tăng 2,5 lần.", True,
     "Đúng. Đẳng áp ⟹ T ∝ V ⟹ T₂/T₁ = 5,0/2,0 = 2,5."),
    ("Vì khí nhận nhiệt nên toàn bộ nhiệt lượng 1500 J đều biến thành nội năng.", False,
     "Sai. Khí đồng thời giãn nở và sinh công 600 J, nên chỉ 900 J trong số đó làm tăng nội năng.")],
   "Định luật I + đẳng áp (C1 + C2)", TB),

ds("Một bình kín thể tích không đổi 2,0 L chứa khí lí tưởng đơn nguyên tử ở áp suất 1,0·10⁵ Pa. "
   "Cho U = (3/2)pV.",
   [("Nội năng ban đầu của khối khí là 300 J.", True,
     "Đúng. U = 1,5 · 1,0·10⁵ · 2,0·10⁻³ = 300 J."),
    ("Nếu cung cấp cho khí nhiệt lượng 150 J thì nội năng trở thành 450 J.", True,
     "Đúng. Bình kín ⟹ A = 0 ⟹ ΔU = Q = 150 J ⟹ U = 300 + 150 = 450 J."),
    ("Khi đó áp suất khí trở thành 1,5·10⁵ Pa.", True,
     "Đúng. U = (3/2)pV với V không đổi nên p tỉ lệ thuận với U: p₂ = 1,0·10⁵ · 450/300 = 1,5·10⁵ Pa."),
    ("Khi đó nhiệt độ khí giảm vì khí đã nhận nhiệt và giãn nở.", False,
     "Sai. Bình kín nên khí không giãn nở; nhận nhiệt làm nội năng tăng, do đó nhiệt độ TĂNG "
     "(tăng 1,5 lần cùng với áp suất).")],
   "Nội năng – đẳng tích (C1 + C2)", TB),

ds("Xét các hiện tượng nhiệt và khí trong đời sống.",
   [("Khi bơm xe nhanh, thân bơm nóng lên vì ta đã thực hiện công lên khối khí.", True,
     "Đúng. Nén nhanh ⟹ Q ≈ 0, ΔU = A > 0 nên nhiệt độ khí tăng và truyền nhiệt cho thân bơm."),
    ("Khi mở van một bình khí nén, khí phụt ra giãn nở nhanh và lạnh đi.", True,
     "Đúng. Khí giãn nở nhanh thì gần như không kịp nhận nhiệt (Q ≈ 0) trong khi sinh công đẩy không khí "
     "xung quanh (A < 0), nên ΔU < 0 và nhiệt độ giảm."),
    ("Đun nóng một bình khí kín làm cả nội năng, nhiệt độ và áp suất khí đều tăng.", True,
     "Đúng. Đẳng tích: ΔU = Q > 0 ⟹ T tăng, và p = nRT/V cũng tăng theo."),
    ("Nội năng của khí trong lốp xe đạp tăng lên chủ yếu do khối lượng khí trong lốp tăng khi bơm.", False,
     "Sai. Nội năng tăng chủ yếu do NHIỆT ĐỘ khí tăng khi bị nén (thực hiện công). Việc thêm khí làm "
     "tăng tổng nội năng nhưng không phải là cơ chế làm khí nóng lên.")],
   "Vận dụng thực tiễn (C1 + C2)", TB),
],
P3=[
sa("Một khối khí giãn nở đẳng áp ở 2,5·10⁵ Pa, thể tích tăng từ 1,0 L lên 3,0 L. Công khí sinh ra bằng "
   "bao nhiêu jun?",
   "500", "A′ = p·ΔV = 2,5·10⁵ · 2,0·10⁻³ = 500 J.", "Công của khí (C1 + C2)", D),

sa("Một bình kín 3,0 L chứa khí lí tưởng đơn nguyên tử ở áp suất 2,0·10⁵ Pa. Nội năng của khối khí bằng "
   "bao nhiêu jun? Cho U = (3/2)pV.",
   "900", "U = 1,5 · 2,0·10⁵ · 3,0·10⁻³ = 1,5 · 600 = 900 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

sa("Một khối khí nhận nhiệt lượng 800 J và sinh công 350 J. Nội năng của khối khí tăng bao nhiêu jun?",
   "450", "ΔU = A + Q = −350 + 800 = 450 J.", "Định luật I nhiệt động lực học", D),

sa("Nén đẳng nhiệt một lượng khí từ 8,0 L xuống 2,0 L. Áp suất ban đầu là 1,5·10⁵ Pa. Áp suất sau khi nén "
   "bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "6", "p₂ = p₁V₁/V₂ = 1,5·10⁵ · 8,0/2,0 = 6,0·10⁵ Pa.", "Định luật Boyle", D),

sa("Đun 2,0 kg nước từ 25 °C lên 75 °C. Nhiệt lượng cần cung cấp bằng bao nhiêu kilôjun? "
   "Cho c = 4200 J/(kg·K).",
   "420", "Q = 2,0 · 4200 · 50 = 420 000 J = 420 kJ.", "Nhiệt dung riêng", D),

sa("Trong quá trình giãn nở đẳng nhiệt, một khối khí lí tưởng nhận nhiệt lượng 650 J. Công mà khí sinh ra "
   "bằng bao nhiêu jun?",
   "650", "Đẳng nhiệt ⟹ ΔU = 0 ⟹ A = −Q ⟹ khí sinh công đúng bằng nhiệt lượng nhận vào: 650 J.",
   "Định luật I + đẳng nhiệt", TB),
])


# =====================================================================
DE2 = dict(
ma="MIX-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Nhiệt lượng, công và nội năng trong các đẳng quá trình của khí lí tưởng",
P1=[
mc("Trong quá trình đẳng áp, nhiệt lượng khí nhận được dùng để",
   ["chỉ làm tăng nội năng của khí.", "chỉ sinh công đẩy pit-tông.",
    "vừa làm tăng nội năng vừa sinh công.", "làm giảm nội năng của khí."],
   "C",
   "Đẳng áp mà nhận nhiệt thì khí vừa nóng lên (ΔU > 0) vừa giãn nở đẩy pit-tông (A′ > 0): "
   "Q = ΔU + A′.",
   "Định luật I + đẳng áp", D),

mc("Một khối khí toả ra nhiệt lượng 400 J và nhận công 250 J. Nội năng của khối khí",
   ["tăng 650 J.", "tăng 150 J.", "giảm 150 J.", "giảm 650 J."],
   "C", "ΔU = A + Q = (+250) + (−400) = −150 J: nội năng giảm 150 J.",
   "Định luật I nhiệt động lực học", D),

mc("Một bình kín chứa khí lí tưởng đơn nguyên tử; U = (3/2)pV. Nếu áp suất khí tăng gấp đôi (thể tích "
   "không đổi) thì nội năng khí",
   ["không đổi.", "tăng gấp đôi.", "tăng 4 lần.", "giảm một nửa."],
   "B", "U = (3/2)pV với V không đổi ⟹ U tỉ lệ thuận với p ⟹ tăng gấp đôi.",
   "Nội năng khí lí tưởng (C1 + C2)", D),

mc("Đun nóng đẳng tích một lượng khí từ 300 K lên 500 K. Áp suất khí ban đầu 1,2·10⁵ Pa. Áp suất lúc sau là",
   ["0,72·10⁵ Pa.", "1,50·10⁵ Pa.", "2,00·10⁵ Pa.", "2,40·10⁵ Pa."],
   "C", "p₂ = p₁·T₂/T₁ = 1,2·10⁵ · 500/300 = 2,0·10⁵ Pa.", "Quá trình đẳng tích", D),

mc("Trên giản đồ (p, V), công mà khí sinh ra trong quá trình đẳng áp bằng diện tích hình",
   ["tam giác.", "chữ nhật.", "thang.", "tròn."],
   "B", "Đẳng áp: đường biểu diễn nằm ngang nên hình dưới nó là hình chữ nhật có diện tích p·ΔV.",
   "Công của khí trên giản đồ p–V", D),

mc("Nhiệt lượng cần để làm nóng chảy hoàn toàn 0,30 kg nước đá ở 0 °C là (λ = 3,4·10⁵ J/kg)",
   ["68 kJ.", "102 kJ.", "136 kJ.", "170 kJ."],
   "B", "Q = λm = 3,4·10⁵ · 0,30 = 102 000 J = 102 kJ.", "Nhiệt nóng chảy riêng", D),

mc("Một lượng khí lí tưởng ở 2,0·10⁵ Pa, 3,0 L, 300 K được đưa tới 400 K và 4,0 L. Áp suất lúc sau là",
   ["1,5·10⁵ Pa.", "2,0·10⁵ Pa.", "2,5·10⁵ Pa.", "3,0·10⁵ Pa."],
   "B", "p₂ = p₁V₁T₂/(T₁V₂) = 2,0·10⁵ · 3,0 · 400/(300 · 4,0) = 2,0·10⁵ Pa.",
   "Phương trình trạng thái", TB),

mc("Ở 300 K, động năng tịnh tiến trung bình của phân tử khí là 6,21·10⁻²¹ J. Ở 450 K, giá trị đó là",
   ["4,14·10⁻²¹ J.", "9,32·10⁻²¹ J.", "1,24·10⁻²⁰ J.", "1,40·10⁻²⁰ J."],
   "B", "W̄đ tỉ lệ thuận với T: 6,21·10⁻²¹ · 450/300 = 9,32·10⁻²¹ J.",
   "Động năng phân tử – nhiệt độ", D),

mc("Khi khí giãn nở đẩy pit-tông đi lên thì theo quy ước ΔU = A + Q,",
   ["A > 0.", "A < 0.", "Q < 0.", "ΔU > 0."],
   "B", "A là công khí NHẬN được; khi khí sinh công thì A mang dấu âm.",
   "Quy ước dấu của định luật I", D),

mc("Đun nóng đẳng áp 0,50 mol khí lí tưởng đơn nguyên tử từ 300 K lên 400 K. Công mà khí sinh ra là "
   "(R = 8,31 J/(mol·K))",
   ["208 J.", "312 J.", "416 J.", "624 J."],
   "C",
   "Đẳng áp: A′ = p·ΔV = nR·ΔT = 0,50 · 8,31 · 100 ≈ 416 J.\n"
   "(Đây là chỗ nối trực tiếp giữa phương trình trạng thái và công của khí.)",
   "Công của khí (C1 + C2)", TB),

mc("Vẫn với khối khí ở câu trên, độ tăng nội năng của khí là",
   ["208 J.", "416 J.", "624 J.", "1040 J."],
   "C", "ΔU = (3/2)nRΔT = 1,5 · 0,50 · 8,31 · 100 ≈ 623 J ≈ 624 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Vẫn với khối khí đó, nhiệt lượng khí nhận được là",
   ["416 J.", "624 J.", "1040 J.", "1456 J."],
   "C", "Q = ΔU + A′ = 623 + 416 ≈ 1040 J. (Chỉ 60% nhiệt lượng biến thành nội năng.)",
   "Định luật I + đẳng áp (C1 + C2)", TB),

mc("Cùng đưa một lượng khí lí tưởng từ nhiệt độ T₁ lên T₂, quá trình nào cần nhiều nhiệt lượng hơn?",
   ["Đẳng tích.", "Đẳng áp.", "Hai quá trình cần như nhau.", "Chưa đủ dữ kiện."],
   "B",
   "Cùng ΔT thì ΔU như nhau. Nhưng quá trình đẳng áp còn phải sinh thêm công đẩy pit-tông nên "
   "Q_đẳng áp = ΔU + A′ > Q_đẳng tích = ΔU.",
   "So sánh hai quá trình (C1 + C2)", TB),

mc("Một chiếc nồi áp suất nấu nhanh hơn nồi thường vì",
   ["áp suất cao làm nước sôi ở nhiệt độ cao hơn 100 °C.",
    "nồi áp suất có nhiệt dung riêng nhỏ hơn.",
    "khối lượng nước trong nồi ít hơn.",
    "nồi áp suất dẫn nhiệt tốt hơn."],
   "A",
   "Nồi kín, hơi nước sinh ra làm áp suất tăng; nhiệt độ sôi tăng theo áp suất nên thức ăn được nấu ở "
   "110 – 120 °C và chín nhanh hơn.",
   "Sự sôi – áp suất (C1 + C2)", TB),

mc("Một lượng khí lí tưởng có nội năng 600 J ở 300 K. Ở 500 K, nội năng của nó là",
   ["360 J.", "800 J.", "1000 J.", "1200 J."],
   "C", "U ∝ T ⟹ U₂ = 600 · 500/300 = 1000 J.", "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trong một chu trình kín của khối khí, tổng độ biến thiên nội năng bằng",
   ["tổng nhiệt lượng nhận vào.", "tổng công sinh ra.", "0.", "tổng công nhận vào."],
   "C", "Nội năng là hàm trạng thái; trở về trạng thái đầu thì ΔU = 0 (khi đó Q_tổng = A′_tổng).",
   "Định luật I – chu trình", TB),

mc("Muốn giảm nội năng của một khối khí lí tưởng, cần",
   ["tăng thể tích của khí.", "tăng áp suất của khí.",
    "giảm nhiệt độ của khí.", "giảm khối lượng riêng của khí."],
   "C", "Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên chỉ có cách hạ nhiệt độ mới chắc chắn giảm U.",
   "Nội năng khí lí tưởng (C1 + C2)", D),

mc("Cho 0,20 kg nước đá ở 0 °C vào 0,50 kg nước ở 30 °C trong bình cách nhiệt. Cho λ = 3,4·10⁵ J/kg, "
   "c = 4200 J/(kg·K). Trạng thái cuối của hệ là",
   ["nước ở 0 °C, đá tan hết vừa đủ.", "hỗn hợp nước và đá ở 0 °C.",
    "nước ở khoảng 4,5 °C.", "nước ở 15 °C."],
   "B",
   "Nước chỉ nhường được tối đa Q = 0,50 · 4200 · 30 = 63 000 J (khi hạ tới 0 °C), trong khi làm tan hết "
   "0,20 kg đá cần 0,20 · 3,4·10⁵ = 68 000 J.\n"
   "Vì 63 000 J < 68 000 J nên đá chỉ tan một phần: Δm = 63 000/3,4·10⁵ ≈ 0,185 kg, vẫn còn khoảng 15 g "
   "đá chưa tan.\n"
   "Khi trong bình đồng thời có nước và nước đá thì nhiệt độ đúng bằng 0 °C.",
   "Cân bằng nhiệt – biện luận", K),
],
P2=[
ds("Đun nóng đẳng áp 0,50 mol khí lí tưởng đơn nguyên tử từ 300 K lên 400 K. Cho R = 8,31 J/(mol·K); "
   "nội năng U = (3/2)nRT.",
   [("Công mà khí sinh ra là khoảng 416 J.", True,
     "Đúng. Đẳng áp: A′ = p·ΔV = nRΔT = 0,50 · 8,31 · 100 ≈ 416 J."),
    ("Độ tăng nội năng của khí là khoảng 623 J.", True,
     "Đúng. ΔU = (3/2)nRΔT = 1,5 · 415,5 ≈ 623 J."),
    ("Nhiệt lượng khí nhận được là khoảng 1040 J.", True,
     "Đúng. Q = ΔU + A′ = 623 + 416 ≈ 1040 J."),
    ("Nếu đun cùng khối khí đó từ 300 K lên 400 K nhưng giữ thể tích không đổi thì cũng cần khoảng 1040 J.", False,
     "Sai. Đẳng tích thì A = 0 nên chỉ cần Q = ΔU ≈ 623 J. Quá trình đẳng áp luôn tốn nhiều nhiệt lượng "
     "hơn vì phải sinh thêm công.")],
   "Định luật I + đẳng áp (C1 + C2)", TB),

ds("Xét quy ước dấu và cách vận dụng định luật I nhiệt động lực học ΔU = A + Q.",
   [("Khi khí giãn nở sinh công thì A mang dấu âm.", True,
     "Đúng. A là công mà hệ NHẬN được; hệ sinh công nghĩa là nhận công âm."),
    ("Một khối khí toả nhiệt 400 J và nhận công 250 J thì nội năng giảm 150 J.", True,
     "Đúng. ΔU = 250 − 400 = −150 J."),
    ("Nếu ΔU = 0 thì khí không trao đổi nhiệt và cũng không trao đổi công với bên ngoài.", False,
     "Sai. ΔU = 0 chỉ có nghĩa A + Q = 0. Ví dụ khí giãn đẳng nhiệt nhận 500 J nhiệt và sinh 500 J công."),
    ("Trong một chu trình kín, tổng nhiệt lượng khí nhận được bằng tổng công khí sinh ra.", True,
     "Đúng. ΔU = 0 sau một chu trình ⟹ Q_tổng = −A_tổng = A′_tổng.")],
   "Định luật I nhiệt động lực học", TB),

ds("Một bình kín thể tích không đổi chứa khí lí tưởng đơn nguyên tử; ban đầu p = 1,2·10⁵ Pa, "
   "T = 300 K, V = 2,0 L. Cho U = (3/2)pV.",
   [("Nội năng ban đầu của khối khí là 360 J.", True,
     "Đúng. U = 1,5 · 1,2·10⁵ · 2,0·10⁻³ = 360 J."),
    ("Đun nóng đẳng tích tới 500 K thì áp suất trở thành 2,0·10⁵ Pa.", True,
     "Đúng. p₂ = 1,2·10⁵ · 500/300 = 2,0·10⁵ Pa."),
    ("Nhiệt lượng cần cung cấp cho quá trình đó là 240 J.", True,
     "Đúng. U₂ = 1,5 · 2,0·10⁵ · 2,0·10⁻³ = 600 J ⟹ ΔU = 600 − 360 = 240 J; đẳng tích nên Q = ΔU = 240 J."),
    ("Trong quá trình đó khí sinh công 240 J.", False,
     "Sai. Thể tích không đổi nên khí không sinh và không nhận công: A = 0.")],
   "Nội năng – đẳng tích (C1 + C2)", TB),

ds("Cho 0,20 kg nước đá ở 0 °C vào 0,50 kg nước ở 30 °C trong bình cách nhiệt lí tưởng. "
   "Cho λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng lớn nhất mà nước có thể nhường là 63 kJ.", True,
     "Đúng. Q = 0,50 · 4200 · 30 = 63 000 J khi nước hạ tới 0 °C."),
    ("Nhiệt lượng cần để làm tan hết 0,20 kg nước đá là 68 kJ.", True,
     "Đúng. Q = λm = 3,4·10⁵ · 0,20 = 68 000 J."),
    ("Toàn bộ nước đá sẽ tan hết và nhiệt độ cân bằng cao hơn 0 °C.", False,
     "Sai. 63 kJ < 68 kJ nên đá chỉ tan được khoảng 0,185 kg; trong bình vẫn còn khoảng 15 g đá và "
     "nhiệt độ cân bằng đúng bằng 0 °C."),
    ("Khối lượng nước đá còn lại khi cân bằng nhiệt vào khoảng 15 g.", True,
     "Đúng. Δm = 63 000/3,4·10⁵ ≈ 0,185 kg ⟹ còn lại 0,200 − 0,185 = 0,015 kg = 15 g.")],
   "Cân bằng nhiệt – biện luận", K),
],
P3=[
sa("Đun nóng đẳng áp 0,50 mol khí lí tưởng đơn nguyên tử từ 300 K lên 400 K. Nhiệt lượng khí nhận được "
   "bằng bao nhiêu jun (làm tròn đến hàng đơn vị)? Cho R = 8,31 J/(mol·K), U = (3/2)nRT.",
   "1039",
   "A′ = nRΔT = 0,50 · 8,31 · 100 = 415,5 J; ΔU = 1,5 · 415,5 = 623,25 J.\n"
   "Q = ΔU + A′ = 623,25 + 415,5 = 1038,75 ≈ 1039 J.",
   "Định luật I + đẳng áp (C1 + C2)", TB),

sa("Một bình kín 2,0 L chứa khí lí tưởng đơn nguyên tử ở 1,2·10⁵ Pa. Đun nóng đẳng tích tới khi áp suất "
   "đạt 2,0·10⁵ Pa. Nhiệt lượng cần cung cấp bằng bao nhiêu jun? Cho U = (3/2)pV.",
   "240",
   "U₁ = 1,5 · 1,2·10⁵ · 2,0·10⁻³ = 360 J; U₂ = 1,5 · 2,0·10⁵ · 2,0·10⁻³ = 600 J.\n"
   "Đẳng tích ⟹ A = 0 ⟹ Q = ΔU = 600 − 360 = 240 J.",
   "Nội năng – đẳng tích (C1 + C2)", TB),

sa("Một khối khí toả nhiệt 400 J và nhận công 250 J. Nội năng của khối khí giảm bao nhiêu jun?",
   "150", "ΔU = A + Q = 250 − 400 = −150 J ⟹ nội năng giảm 150 J.",
   "Định luật I nhiệt động lực học", D),

sa("Cho 0,20 kg nước đá ở 0 °C vào 0,50 kg nước ở 30 °C trong bình cách nhiệt. Khối lượng nước đá còn lại "
   "khi cân bằng nhiệt bằng bao nhiêu gam? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "15",
   "Nước nhường tối đa 63 000 J < 68 000 J cần để tan hết ⟹ đá tan một phần, t = 0 °C.\n"
   "Δm = 63 000/3,4·10⁵ ≈ 0,185 kg ⟹ còn lại 200 − 185 = 15 g.",
   "Cân bằng nhiệt – biện luận", K),

sa("Một lượng khí lí tưởng có nội năng 600 J ở 300 K. Ở 500 K nội năng của nó bằng bao nhiêu jun?",
   "1000", "U ∝ T ⟹ U₂ = 600 · 500/300 = 1000 J.", "Nội năng khí lí tưởng (C1 + C2)", TB),

sa("Đun nóng đẳng tích một lượng khí từ 300 K lên 500 K; áp suất ban đầu 1,2·10⁵ Pa. Áp suất lúc sau bằng "
   "bao nhiêu (đơn vị 10⁵ Pa)?",
   "2", "p₂ = p₁T₂/T₁ = 1,2·10⁵ · 500/300 = 2,0·10⁵ Pa.", "Quá trình đẳng tích", D),
])


# =====================================================================
DE3 = dict(
ma="MIX-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Phân tích từng chặng của chu trình trên giản đồ p–V bằng định luật I",
P1=[
mc("Hình bên là chu trình 1 → 2 → 3 → 4 → 1 của một lượng khí lí tưởng đơn nguyên tử, với "
   "1(1 L; 1·10⁵ Pa), 2(1 L; 3·10⁵ Pa), 3(3 L; 3·10⁵ Pa), 4(3 L; 1·10⁵ Pa). Nội năng của khí ở trạng "
   "thái (1) bằng (U = (3/2)pV)",
   ["100 J.", "150 J.", "300 J.", "450 J."],
   "B", "U₁ = 1,5 · 1·10⁵ · 1·10⁻³ = 150 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB, fig="k_dt_chutrinh",
   cap="Chu trình gồm hai quá trình đẳng tích và hai quá trình đẳng áp"),

mc("Vẫn với chu trình trên, trong chặng 1 → 2 khí nhận nhiệt lượng bằng",
   ["150 J.", "300 J.", "450 J.", "600 J."],
   "B",
   "1 → 2 là đẳng tích ⟹ A = 0 ⟹ Q = ΔU.\n"
   "U₁ = 150 J; U₂ = 1,5 · 3·10⁵ · 1·10⁻³ = 450 J ⟹ Q = 450 − 150 = 300 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, công mà khí sinh ra trong chặng 2 → 3 bằng",
   ["200 J.", "400 J.", "600 J.", "900 J."],
   "C", "Đẳng áp ở 3·10⁵ Pa: A′ = p·ΔV = 3·10⁵ · (3 − 1)·10⁻³ = 600 J.",
   "Công của khí (C1 + C2)", TB, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, nhiệt lượng khí nhận được trong chặng 2 → 3 bằng",
   ["600 J.", "900 J.", "1200 J.", "1500 J."],
   "D",
   "U₂ = 450 J; U₃ = 1,5 · 3·10⁵ · 3·10⁻³ = 1350 J ⟹ ΔU = 900 J.\n"
   "Q = ΔU + A′ = 900 + 600 = 1500 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, công mà khí sinh ra trong CẢ CHU TRÌNH bằng",
   ["200 J.", "400 J.", "600 J.", "800 J."],
   "B",
   "Công của cả chu trình bằng diện tích hình chữ nhật mà chu trình bao quanh:\n"
   "A′ = Δp·ΔV = (3 − 1)·10⁵ · (3 − 1)·10⁻³ = 2·10⁵ · 2·10⁻³ = 400 J.",
   "Công trong chu trình (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, tổng nhiệt lượng mà khí nhận được trong cả chu trình bằng",
   ["0 J.", "400 J.", "800 J.", "1500 J."],
   "B",
   "Sau một chu trình khí trở về trạng thái đầu nên ΔU = 0 ⟹ Q_tổng = A′_tổng = 400 J.\n"
   "(Kiểm tra chi tiết: 300 + 1500 − 900 − 500 = 400 J ✓)",
   "Định luật I – chu trình (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Trong chặng 4 → 1 của chu trình trên, khí",
   ["nhận công 200 J và nhận nhiệt.", "nhận công 200 J và toả nhiệt.",
    "sinh công 200 J và nhận nhiệt.", "sinh công 200 J và toả nhiệt."],
   "B",
   "4 → 1 là đẳng áp ở 1·10⁵ Pa, thể tích giảm từ 3 L xuống 1 L ⟹ khí bị nén, NHẬN công "
   "A = 1·10⁵ · 2·10⁻³ = 200 J.\n"
   "U₄ = 450 J, U₁ = 150 J ⟹ ΔU = −300 J ⟹ Q = ΔU − A = −300 − 200 = −500 J: khí TOẢ nhiệt 500 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Nhiệt độ ở trạng thái (3) của chu trình gấp bao nhiêu lần nhiệt độ ở trạng thái (1)?",
   ["3 lần.", "6 lần.", "9 lần.", "12 lần."],
   "C", "T ∝ pV ⟹ T₃/T₁ = (3 · 3)/(1 · 1) = 9.",
   "Phương trình trạng thái", TB, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Nhiệt lượng cần cung cấp để đun 0,50 kg nước từ 20 °C lên 60 °C là (c = 4200 J/(kg·K))",
   ["42 kJ.", "84 kJ.", "126 kJ.", "168 kJ."],
   "B", "Q = 0,50 · 4200 · 40 = 84 000 J = 84 kJ.", "Nhiệt dung riêng", D),

mc("Một lượng khí lí tưởng đơn nguyên tử ở 1,5·10⁵ Pa chiếm thể tích 4,0 L. Nội năng của nó bằng "
   "(U = (3/2)pV)",
   ["600 J.", "750 J.", "900 J.", "1200 J."],
   "C", "U = 1,5 · 1,5·10⁵ · 4,0·10⁻³ = 1,5 · 600 = 900 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Nén đẳng nhiệt một lượng khí lí tưởng. Trong quá trình đó khí",
   ["nhận công và nhận nhiệt.", "nhận công và toả nhiệt.",
    "sinh công và nhận nhiệt.", "sinh công và toả nhiệt."],
   "B",
   "Nén ⟹ khí nhận công (A > 0). Đẳng nhiệt ⟹ ΔU = 0 ⟹ Q = −A < 0: khí toả nhiệt đúng bằng công "
   "nhận được.",
   "Định luật I + đẳng nhiệt", TB),

mc("Một lượng khí lí tưởng biến đổi từ trạng thái có pV = 400 J sang trạng thái có pV = 1000 J. Nội năng "
   "của khí (đơn nguyên tử) đã tăng",
   ["600 J.", "900 J.", "1500 J.", "400 J."],
   "B", "U = (3/2)pV ⟹ ΔU = 1,5 · (1000 − 400) = 900 J.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trên giản đồ (p, V), quá trình nào KHÔNG sinh công và cũng không nhận công?",
   ["Đẳng áp.", "Đẳng nhiệt.", "Đẳng tích.", "Mọi quá trình đều sinh công."],
   "C", "Công liên quan tới sự thay đổi thể tích; đẳng tích thì ΔV = 0 nên A = 0.",
   "Công của khí trên giản đồ p–V", D),

mc("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử, tỉ số giữa nhiệt lượng khí nhận được và độ "
   "tăng nội năng của khí bằng",
   ["1.", "5/3.", "3/2.", "2/3."],
   "B",
   "Đẳng áp: ΔU = (3/2)nRΔT và A′ = nRΔT ⟹ Q = ΔU + A′ = (5/2)nRΔT.\n"
   "Q/ΔU = (5/2)/(3/2) = 5/3.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Nhiệt lượng cần để làm hoá hơi hoàn toàn 0,20 kg nước ở 100 °C là (L = 2,26·10⁶ J/kg)",
   ["226 kJ.", "339 kJ.", "452 kJ.", "678 kJ."],
   "C", "Q = Lm = 2,26·10⁶ · 0,20 = 452 000 J = 452 kJ.", "Nhiệt hoá hơi riêng", D),

mc("Một khối khí lí tưởng có nhiệt độ tăng gấp ba. Động năng tịnh tiến trung bình của phân tử và nội năng "
   "của khối khí lần lượt",
   ["đều tăng 3 lần.", "tăng 3 lần và tăng 9 lần.",
    "tăng √3 lần và tăng 3 lần.", "đều tăng √3 lần."],
   "A",
   "W̄đ = (3/2)kT và U = N·W̄đ đều tỉ lệ thuận với nhiệt độ tuyệt đối nên cùng tăng 3 lần. "
   "(Đại lượng chỉ tăng √3 lần là tốc độ căn quân phương.)",
   "Động năng phân tử – nội năng (C1 + C2)", TB),

mc("Trong bình cách nhiệt, một khối khí lí tưởng bị nén nhanh. Kết luận nào ĐÚNG?",
   ["Nội năng giảm, nhiệt độ giảm.", "Nội năng tăng, nhiệt độ tăng.",
    "Nội năng không đổi.", "Nhiệt độ không đổi, áp suất tăng."],
   "B", "Cách nhiệt ⟹ Q = 0; bị nén ⟹ A > 0 ⟹ ΔU = A > 0: nội năng và nhiệt độ đều tăng.",
   "Định luật I + nén khí (C1 + C2)", TB),

mc("Muốn khí lí tưởng sinh công mà nội năng không đổi thì quá trình phải là",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "đoạn nhiệt."],
   "C", "ΔU = 0 ⟹ nhiệt độ không đổi ⟹ quá trình đẳng nhiệt; khi đó khí nhận nhiệt và sinh công bằng nhau.",
   "Định luật I + đẳng nhiệt", TB),
],
P2=[
ds("Chu trình 1 → 2 → 3 → 4 → 1 của một lượng khí lí tưởng đơn nguyên tử được cho như hình vẽ, với "
   "1(1 L; 1·10⁵ Pa), 2(1 L; 3·10⁵ Pa), 3(3 L; 3·10⁵ Pa), 4(3 L; 1·10⁵ Pa). Cho U = (3/2)pV.",
   [("Nội năng của khí ở các trạng thái (2) và (4) bằng nhau và bằng 450 J.", True,
     "Đúng. U₂ = 1,5 · 3·10⁵ · 1·10⁻³ = 450 J; U₄ = 1,5 · 1·10⁵ · 3·10⁻³ = 450 J. Hai trạng thái có "
     "cùng tích pV nên cùng nhiệt độ và cùng nội năng."),
    ("Trong chặng 2 → 3, khí nhận nhiệt lượng 1500 J.", True,
     "Đúng. ΔU = 1350 − 450 = 900 J; A′ = 3·10⁵ · 2·10⁻³ = 600 J ⟹ Q = 900 + 600 = 1500 J."),
    ("Trong chặng 3 → 4, khí toả nhiệt lượng 900 J.", True,
     "Đúng. Đẳng tích ⟹ A = 0; ΔU = 450 − 1350 = −900 J ⟹ Q = −900 J, khí toả 900 J."),
    ("Trong cả chu trình, khí sinh công 400 J và cũng toả nhiệt 400 J.", False,
     "Sai ở vế sau. ΔU = 0 sau một chu trình nên Q_tổng = +A′_tổng = +400 J: khí NHẬN nhiệt 400 J và "
     "biến toàn bộ thành công. Đây chính là nguyên tắc của động cơ nhiệt.")],
   "Phân tích chu trình bằng định luật I (C1 + C2)", K,
   fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

ds("Xét quá trình đẳng áp của một lượng khí lí tưởng đơn nguyên tử. Cho U = (3/2)nRT, A′ = p·ΔV.",
   [("Trong quá trình đẳng áp, công khí sinh ra bằng nRΔT.", True,
     "Đúng. A′ = p·ΔV = p·(V₂ − V₁) = nRT₂ − nRT₁ = nRΔT."),
    ("Tỉ số giữa nhiệt lượng khí nhận được và độ tăng nội năng bằng 5/3.", True,
     "Đúng. Q = ΔU + A′ = (3/2)nRΔT + nRΔT = (5/2)nRΔT ⟹ Q/ΔU = 5/3."),
    ("Trong quá trình đẳng áp, 60% nhiệt lượng nhận vào biến thành nội năng, 40% biến thành công.", True,
     "Đúng. ΔU/Q = (3/2)/(5/2) = 0,6 và A′/Q = 1/(5/2)·1 = 0,4."),
    ("Nếu đun cùng lượng khí đó từ cùng nhiệt độ đầu tới cùng nhiệt độ cuối theo quá trình đẳng tích thì "
     "cần nhiều nhiệt lượng hơn.", False,
     "Sai, ngược lại. Đẳng tích thì A = 0 nên Q = ΔU = (3/2)nRΔT, NHỎ hơn (5/2)nRΔT của quá trình "
     "đẳng áp.")],
   "So sánh hai quá trình (C1 + C2)", K),

ds("Một khối khí lí tưởng thực hiện các quá trình khác nhau. Cho quy ước ΔU = A + Q với A là công khí "
   "nhận được.",
   [("Nén đẳng nhiệt: khí nhận công và toả nhiệt với cùng độ lớn.", True,
     "Đúng. ΔU = 0 ⟹ Q = −A; A > 0 nên Q < 0."),
    ("Nén trong bình cách nhiệt: nhiệt độ khí tăng.", True,
     "Đúng. Q = 0, A > 0 ⟹ ΔU = A > 0 ⟹ nhiệt độ tăng."),
    ("Giãn nở đẳng áp: khí vừa sinh công vừa nhận nhiệt, và nội năng tăng.", True,
     "Đúng. Thể tích tăng nên T tăng (đẳng áp), do đó ΔU > 0; khí sinh công nên phải nhận nhiệt nhiều "
     "hơn cả ΔU."),
    ("Đẳng tích: khí sinh công đúng bằng nhiệt lượng nhận được.", False,
     "Sai. Đẳng tích thì A = 0, khí không sinh và cũng không nhận công; toàn bộ nhiệt lượng biến thành "
     "nội năng.")],
   "Định luật I – bốn quá trình", TB),

ds("Xét các đại lượng nối kết chương 1 và chương 2 của một lượng khí lí tưởng xác định.",
   [("Tích pV tỉ lệ thuận với nhiệt độ tuyệt đối và cũng tỉ lệ thuận với nội năng của khí đơn nguyên tử.", True,
     "Đúng. pV = nRT và U = (3/2)nRT = (3/2)pV."),
    ("Hai trạng thái có cùng tích pV thì có cùng nội năng.", True,
     "Đúng, vì cùng pV nghĩa là cùng nhiệt độ, mà nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ."),
    ("Nếu nội năng của khối khí tăng thì áp suất của nó chắc chắn tăng.", False,
     "Sai. Nội năng tăng nghĩa là nhiệt độ tăng, nhưng nếu khí đồng thời giãn nở đủ nhiều thì áp suất "
     "vẫn có thể giảm (ví dụ quá trình đẳng áp thì áp suất không đổi)."),
    ("Nếu tích pV không đổi thì nội năng của khối khí không đổi.", True,
     "Đúng. pV không đổi ⟹ T không đổi ⟹ U không đổi (quá trình đẳng nhiệt).")],
   "Cầu nối hai chương", K),
],
P3=[
sa("Với chu trình 1(1 L; 1·10⁵ Pa) → 2(1 L; 3·10⁵ Pa) → 3(3 L; 3·10⁵ Pa) → 4(3 L; 1·10⁵ Pa) → 1, "
   "công khí sinh ra trong cả chu trình bằng bao nhiêu jun?",
   "400", "A′ = Δp·ΔV = 2·10⁵ · 2·10⁻³ = 400 J (diện tích hình chữ nhật chu trình bao quanh).",
   "Công trong chu trình (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Vẫn với chu trình đó, nhiệt lượng khí nhận được trong chặng 2 → 3 bằng bao nhiêu jun? "
   "Cho U = (3/2)pV.",
   "1500",
   "U₂ = 450 J; U₃ = 1350 J ⟹ ΔU = 900 J. A′ = 3·10⁵ · 2·10⁻³ = 600 J.\nQ = 900 + 600 = 1500 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Vẫn với chu trình đó, nhiệt lượng khí TOẢ ra trong chặng 4 → 1 bằng bao nhiêu jun?",
   "500",
   "Đẳng áp ở 1·10⁵ Pa, khí bị nén nên nhận công A = 1·10⁵ · 2·10⁻³ = 200 J.\n"
   "ΔU = U₁ − U₄ = 150 − 450 = −300 J ⟹ Q = ΔU − A = −300 − 200 = −500 J, tức toả 500 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Một lượng khí lí tưởng đơn nguyên tử ở 1,5·10⁵ Pa chiếm 4,0 L. Nội năng của khối khí bằng bao nhiêu "
   "jun? Cho U = (3/2)pV.",
   "900", "U = 1,5 · 1,5·10⁵ · 4,0·10⁻³ = 900 J.", "Nội năng khí lí tưởng (C1 + C2)", TB),

sa("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử, khí nhận nhiệt lượng 2000 J. Độ tăng nội năng "
   "của khí bằng bao nhiêu jun?",
   "1200", "Đẳng áp: ΔU/Q = 3/5 ⟹ ΔU = 0,6 · 2000 = 1200 J (phần còn lại 800 J biến thành công).",
   "Định luật I + đẳng áp (C1 + C2)", K),

sa("Nhiệt lượng cần để làm hoá hơi hoàn toàn 0,20 kg nước ở 100 °C bằng bao nhiêu kilôjun? "
   "Cho L = 2,26·10⁶ J/kg.",
   "452", "Q = Lm = 2,26·10⁶ · 0,20 = 452 000 J = 452 kJ.", "Nhiệt hoá hơi riêng", D),
])


# =====================================================================
DE4 = dict(
ma="MIX-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Xilanh có pit-tông: từ áp suất cơ học tới công, nội năng và nhiệt lượng",
P1=[
mc("Một xilanh thẳng đứng miệng hướng lên, tiết diện 50 cm², chứa khí dưới một pit-tông khối lượng 5,0 kg "
   "dịch chuyển không ma sát. Áp suất khí quyển 10⁵ Pa, g = 10 m/s². Áp suất khí trong xilanh là",
   ["0,90·10⁵ Pa.", "1,00·10⁵ Pa.", "1,10·10⁵ Pa.", "1,50·10⁵ Pa."],
   "C",
   "S = 50 cm² = 5,0·10⁻³ m²; mg/S = 5,0 · 10/5,0·10⁻³ = 1,0·10⁴ Pa.\n"
   "p = p₀ + mg/S = 10⁵ + 0,1·10⁵ = 1,10·10⁵ Pa.",
   "Áp suất khí trong xilanh (C2)", TB, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với xilanh trên, cột khí ban đầu cao 20 cm. Đun nóng khí làm pit-tông dâng lên thêm 10 cm. Công "
   "mà khí sinh ra bằng",
   ["27,5 J.", "55,0 J.", "82,5 J.", "110,0 J."],
   "B",
   "Quá trình là đẳng áp (pit-tông tự do): ΔV = S·Δh = 5,0·10⁻³ · 0,10 = 5,0·10⁻⁴ m³.\n"
   "A′ = p·ΔV = 1,10·10⁵ · 5,0·10⁻⁴ = 55,0 J.",
   "Công của khí (C1 + C2)", TB, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với quá trình trên (khí lí tưởng đơn nguyên tử, U = (3/2)pV), độ tăng nội năng của khí là",
   ["55,0 J.", "82,5 J.", "110,0 J.", "137,5 J."],
   "B",
   "V₁ = S·h₁ = 5,0·10⁻³ · 0,20 = 1,0·10⁻³ m³; V₂ = 1,5·10⁻³ m³.\n"
   "U₁ = 1,5 · 1,10·10⁵ · 1,0·10⁻³ = 165 J; U₂ = 1,5 · 1,10·10⁵ · 1,5·10⁻³ = 247,5 J.\n"
   "ΔU = 82,5 J. (Cũng bằng 1,5·A′ vì đẳng áp.)",
   "Nội năng khí lí tưởng (C1 + C2)", K, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với quá trình trên, nhiệt lượng khí nhận được là",
   ["55,0 J.", "82,5 J.", "137,5 J.", "192,5 J."],
   "C", "Q = ΔU + A′ = 82,5 + 55,0 = 137,5 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với quá trình trên, nếu nhiệt độ ban đầu là 300 K thì nhiệt độ cuối là",
   ["350 K.", "400 K.", "450 K.", "500 K."],
   "C", "Đẳng áp ⟹ T ∝ V (hay ∝ chiều cao cột khí): T₂ = 300 · 30/20 = 450 K.",
   "Định luật Charles", TB, fig="k_sd_xilanh_quanang", cap="Xilanh thẳng đứng có pit-tông"),

mc("Nếu lật ngược xilanh trên cho miệng hướng xuống (pit-tông vẫn dịch chuyển không ma sát) thì áp suất "
   "khí trong xilanh trở thành",
   ["0,90·10⁵ Pa.", "1,00·10⁵ Pa.", "1,10·10⁵ Pa.", "1,20·10⁵ Pa."],
   "A", "Miệng hướng xuống: trọng lực pit-tông kéo pit-tông ra xa khí ⟹ p = p₀ − mg/S = 0,90·10⁵ Pa.",
   "Áp suất khí trong xilanh (C2)", K),

mc("Một khinh khí cầu có đáy hở nên áp suất khí bên trong luôn bằng áp suất khí quyển. Khi đốt nóng khí "
   "trong cầu, khối lượng riêng của khí trong cầu",
   ["tăng vì nhiệt độ tăng.", "giảm vì ρ = pM/(RT) tỉ lệ nghịch với T.",
    "không đổi vì thể tích cầu không đổi.", "tăng vì một phần khí thoát ra ngoài."],
   "B",
   "ρ = pM/(RT): p và M không đổi nên ρ tỉ lệ nghịch với nhiệt độ tuyệt đối. Khí nhẹ đi nên lực đẩy "
   "Archimedes thắng trọng lượng và cầu bay lên.",
   "Khối lượng riêng của khí – thực tiễn (C1 + C2)", TB, fig="k_sd_bongbay",
   cap="Khinh khí cầu / bóng thám không"),

mc("Nhiệt lượng cần cung cấp để đun 1,0 kg nước từ 20 °C đến 100 °C là (c = 4200 J/(kg·K))",
   ["168 kJ.", "252 kJ.", "336 kJ.", "420 kJ."],
   "C", "Q = 1,0 · 4200 · 80 = 336 000 J = 336 kJ.", "Nhiệt dung riêng", D),

mc("So sánh nhiệt lượng cần để đun 1,0 kg nước từ 20 °C lên 100 °C (336 kJ) với công mà một khối khí sinh "
   "ra khi giãn nở đẳng áp ở 10⁵ Pa với ΔV = 1,0 L (100 J), ta thấy",
   ["hai giá trị xấp xỉ nhau.", "nhiệt lượng đun nước lớn hơn khoảng 3360 lần.",
    "công của khí lớn hơn.", "không so sánh được vì khác đơn vị."],
   "B",
   "336 000 J / 100 J = 3360 lần. So sánh này cho thấy các quá trình nhiệt trong đời sống thường liên quan "
   "tới năng lượng lớn hơn nhiều so với công cơ học của khí trong một lần giãn nở nhỏ.",
   "So sánh độ lớn năng lượng (C1 + C2)", TB),

mc("Trong quá trình đẳng tích, nếu áp suất khí tăng từ 1,0·10⁵ Pa lên 1,6·10⁵ Pa với thể tích 2,0 L thì "
   "nhiệt lượng khí nhận được là (U = (3/2)pV)",
   ["120 J.", "180 J.", "240 J.", "300 J."],
   "B",
   "U₁ = 1,5 · 1,0·10⁵ · 2,0·10⁻³ = 300 J; U₂ = 1,5 · 1,6·10⁵ · 2,0·10⁻³ = 480 J.\n"
   "Đẳng tích ⟹ A = 0 ⟹ Q = ΔU = 180 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

mc("Một lượng khí lí tưởng giãn nở đẳng nhiệt, thể tích tăng gấp đôi. Trong quá trình đó",
   ["nội năng tăng gấp đôi.", "nội năng không đổi, khí nhận nhiệt và sinh công bằng nhau.",
    "nội năng giảm một nửa.", "khí không trao đổi nhiệt."],
   "B", "Đẳng nhiệt ⟹ ΔU = 0 ⟹ Q = −A: nhiệt lượng nhận vào bằng đúng công sinh ra.",
   "Định luật I + đẳng nhiệt", TB),

mc("Đơn vị của tích p·V là",
   ["W.", "J.", "N.", "Pa."],
   "B", "Pa·m³ = (N/m²)·m³ = N·m = J. Vì vậy pV có thứ nguyên của một năng lượng, phù hợp với "
   "U = (3/2)pV.",
   "Thứ nguyên (C1 + C2)", D),

mc("Khi một khối khí lí tưởng có áp suất và thể tích cùng tăng gấp đôi thì nội năng của nó",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "tăng 8 lần."],
   "C", "U = (3/2)pV ⟹ U tỉ lệ thuận với tích pV: 2 · 2 = 4 lần.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Cần cung cấp nhiệt lượng bằng bao nhiêu để biến 0,10 kg nước đá ở 0 °C thành nước ở 20 °C? "
   "Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   ["34,0 kJ.", "42,4 kJ.", "50,8 kJ.", "76,4 kJ."],
   "B",
   "Q = λm + mcΔt = 3,4·10⁵ · 0,10 + 0,10 · 4200 · 20 = 34 000 + 8400 = 42 400 J = 42,4 kJ.",
   "Nhiệt nóng chảy riêng", TB),

mc("Nếu pit-tông trong xilanh bị hàn cứng (không dịch chuyển được) và ta đun nóng khí thì",
   ["khí sinh công đẩy pit-tông.", "khí không sinh công, toàn bộ nhiệt lượng làm tăng nội năng.",
    "áp suất khí không đổi.", "nội năng khí không đổi."],
   "B", "Pit-tông cố định ⟹ thể tích không đổi ⟹ A = 0 ⟹ Q = ΔU; áp suất tăng theo nhiệt độ.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

mc("Trong bốn đại lượng sau của một lượng khí lí tưởng, đại lượng nào KHÔNG phải là hàm của trạng thái?",
   ["Áp suất.", "Thể tích.", "Nội năng.", "Nhiệt lượng."],
   "D",
   "Nhiệt lượng (và công) phụ thuộc cách thực hiện quá trình chứ không chỉ phụ thuộc trạng thái đầu và "
   "cuối. Ba đại lượng còn lại đều xác định khi biết trạng thái của khí.",
   "Hàm trạng thái (C1 + C2)", K),

mc("Một khối khí lí tưởng đơn nguyên tử ở nhiệt độ 300 K có nội năng 750 J. Số mol khí bằng "
   "(R = 8,31 J/(mol·K))",
   ["0,10 mol.", "0,20 mol.", "0,30 mol.", "0,50 mol."],
   "B",
   "U = (3/2)nRT ⟹ n = 2U/(3RT) = 2 · 750/(3 · 8,31 · 300) = 1500/7479 ≈ 0,20 mol.",
   "Nội năng khí lí tưởng (C1 + C2)", K),

mc("Khi mở van một bình khí nén, luồng khí phụt ra rất lạnh. Nguyên nhân là",
   ["khí bị nén sẵn nên vốn đã lạnh.",
    "khí giãn nở nhanh, sinh công đẩy không khí xung quanh mà gần như không kịp nhận nhiệt.",
    "van kim loại hút nhiệt của khí.",
    "khối lượng khí giảm nên nhiệt độ giảm."],
   "B",
   "Giãn nở nhanh ⟹ Q ≈ 0 và A < 0 (khí sinh công) ⟹ ΔU < 0: nội năng và nhiệt độ giảm mạnh. Đây cũng "
   "là nguyên lí làm lạnh trong máy điều hoà và tủ lạnh.",
   "Định luật I – thực tiễn (C1 + C2)", TB),
],
P2=[
ds("Một xilanh thẳng đứng miệng hướng lên, tiết diện 50 cm², chứa cột khí lí tưởng đơn nguyên tử cao "
   "20 cm ở 300 K, dưới một pit-tông khối lượng 5,0 kg dịch chuyển không ma sát. Áp suất khí quyển 10⁵ Pa, "
   "g = 10 m/s². Đun nóng khí làm pit-tông dâng thêm 10 cm. Cho U = (3/2)pV.",
   [("Áp suất khí trong xilanh là 1,10·10⁵ Pa và không đổi trong suốt quá trình.", True,
     "Đúng. p = p₀ + mg/S = 10⁵ + 5,0·10/(5,0·10⁻³) = 1,10·10⁵ Pa; pit-tông tự do nên áp suất giữ nguyên "
     "⟹ quá trình đẳng áp."),
    ("Nhiệt độ khí sau khi đun là 450 K.", True,
     "Đúng. Đẳng áp ⟹ T ∝ chiều cao cột khí: T₂ = 300 · 30/20 = 450 K."),
    ("Công mà khí sinh ra là 55 J và độ tăng nội năng là 82,5 J.", True,
     "Đúng. A′ = p·ΔV = 1,10·10⁵ · 5,0·10⁻⁴ = 55 J; ΔU = 1,5·A′ = 82,5 J (vì đẳng áp thì ΔU = (3/2)pΔV)."),
    ("Nhiệt lượng khí nhận được bằng đúng công mà khí sinh ra.", False,
     "Sai. Q = ΔU + A′ = 82,5 + 55 = 137,5 J, lớn hơn công sinh ra. Chỉ trong quá trình ĐẲNG NHIỆT thì "
     "nhiệt lượng nhận vào mới bằng đúng công sinh ra.")],
   "Xilanh có pit-tông – định luật I (C1 + C2)", K,
   fig="k_sd_xilanh_quanang", cap="Xilanh thẳng đứng có pit-tông"),

ds("Xét một khinh khí cầu có đáy hở, thể tích không đổi, áp suất khí bên trong luôn bằng áp suất khí "
   "quyển. Cho ρ = pM/(RT).",
   [("Khi đốt nóng khí trong cầu, khối lượng riêng của khí trong cầu giảm.", True,
     "Đúng. p và M không đổi nên ρ tỉ lệ nghịch với T."),
    ("Khi đốt nóng, một phần khí trong cầu thoát ra ngoài qua miệng hở.", True,
     "Đúng. m = ρV với V không đổi và ρ giảm ⟹ khối lượng khí trong cầu giảm."),
    ("Lực đẩy Archimedes tác dụng lên cầu tăng lên khi đốt nóng khí bên trong.", False,
     "Sai. F_A = ρ_ngoài·V·g chỉ phụ thuộc khối lượng riêng của không khí BÊN NGOÀI và thể tích cầu — "
     "cả hai đều không đổi. Cầu bay lên là do TRỌNG LƯỢNG của khí bên trong giảm."),
    ("Nếu vỏ cầu kín hoàn toàn thì việc đốt nóng khí bên trong sẽ làm áp suất tăng chứ không làm cầu nhẹ "
     "đi.", True,
     "Đúng. Cầu kín ⟹ thể tích và khối lượng khí không đổi ⟹ quá trình đẳng tích, áp suất tăng nhưng "
     "trọng lượng khí bên trong không giảm nên không tạo được lực nâng.")],
   "Khối lượng riêng của khí – khinh khí cầu (C1 + C2)", K,
   fig="k_sd_bongbay", cap="Khinh khí cầu"),

ds("Xét bốn quá trình của cùng một lượng khí lí tưởng đơn nguyên tử. Cho U = (3/2)pV.",
   [("Đẳng tích từ 1,0·10⁵ Pa lên 1,6·10⁵ Pa với V = 2,0 L: khí nhận nhiệt 180 J.", True,
     "Đúng. ΔU = 1,5 · (1,6 − 1,0)·10⁵ · 2,0·10⁻³ = 180 J; A = 0 nên Q = ΔU = 180 J."),
    ("Nếu áp suất và thể tích của khối khí cùng tăng gấp đôi thì nội năng tăng 4 lần.", True,
     "Đúng. U = (3/2)pV tỉ lệ thuận với tích pV."),
    ("Đơn vị của tích p·V là jun.", True,
     "Đúng. Pa·m³ = N/m² · m³ = N·m = J, phù hợp với việc pV liên quan tới năng lượng."),
    ("Nhiệt lượng là hàm của trạng thái nên chỉ cần biết trạng thái đầu và cuối là tính được Q.", False,
     "Sai. Nhiệt lượng và công phụ thuộc ĐƯỜNG ĐI của quá trình. Chỉ nội năng mới là hàm trạng thái; "
     "muốn tính Q phải biết cả quá trình để tính được A.")],
   "Hàm trạng thái – định luật I (C1 + C2)", K),

ds("Xét các hiện tượng làm lạnh và làm nóng khí trong thực tiễn.",
   [("Khi mở van bình khí nén, luồng khí phụt ra lạnh đi vì khí sinh công mà gần như không kịp nhận nhiệt.", True,
     "Đúng. Q ≈ 0 và A < 0 ⟹ ΔU < 0 ⟹ nhiệt độ giảm."),
    ("Khi nén khí nhanh trong xilanh động cơ diesel, nhiệt độ khí tăng cao đủ để đốt cháy nhiên liệu.", True,
     "Đúng. Q ≈ 0 và A > 0 ⟹ ΔU > 0; nhiệt độ có thể lên tới 600 – 700 °C."),
    ("Nếu pit-tông bị hàn cứng và ta đun nóng khí thì khí vẫn sinh công đẩy pit-tông.", False,
     "Sai. Pit-tông cố định ⟹ thể tích không đổi ⟹ khí không sinh công; toàn bộ nhiệt lượng làm tăng nội "
     "năng và áp suất."),
    ("Nhiệt lượng cần để đun 1,0 kg nước từ 20 °C lên 100 °C lớn hơn hàng nghìn lần công mà một khối khí "
     "sinh ra khi giãn 1,0 L ở áp suất 10⁵ Pa.", True,
     "Đúng. 336 000 J so với 100 J, tức lớn hơn 3360 lần — cho thấy quy mô năng lượng rất khác nhau giữa "
     "hai loại quá trình.")],
   "Vận dụng thực tiễn (C1 + C2)", TB),
],
P3=[
sa("Xilanh thẳng đứng miệng hướng lên, tiết diện 50 cm², pit-tông 5,0 kg dịch chuyển không ma sát, "
   "p₀ = 10⁵ Pa, g = 10 m/s². Áp suất khí trong xilanh bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "1,1", "p = p₀ + mg/S = 10⁵ + 5,0·10/(5,0·10⁻³) = 1,1·10⁵ Pa.",
   "Áp suất khí trong xilanh (C2)", TB, fig="k_sd_xilanh_quanang", cap="Xilanh có pit-tông"),

sa("Vẫn với xilanh đó, cột khí cao 20 cm; đun nóng làm pit-tông dâng thêm 10 cm. Công khí sinh ra bằng "
   "bao nhiêu jun?",
   "55", "ΔV = S·Δh = 5,0·10⁻³ · 0,10 = 5,0·10⁻⁴ m³ ⟹ A′ = p·ΔV = 1,1·10⁵ · 5,0·10⁻⁴ = 55 J.",
   "Công của khí (C1 + C2)", TB),

sa("Vẫn với quá trình đó (khí đơn nguyên tử, U = (3/2)pV), nhiệt lượng khí nhận được bằng bao nhiêu jun "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "137,5", "ΔU = 1,5 · A′ = 1,5 · 55 = 82,5 J ⟹ Q = ΔU + A′ = 82,5 + 55 = 137,5 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

sa("Một khối khí lí tưởng đơn nguyên tử ở 300 K có nội năng 750 J. Số mol khí bằng bao nhiêu (làm tròn đến "
   "chữ số thập phân thứ nhất)? Cho R = 8,31 J/(mol·K).",
   "0,2", "n = 2U/(3RT) = 1500/(3 · 8,31 · 300) = 1500/7479 ≈ 0,20 mol.",
   "Nội năng khí lí tưởng (C1 + C2)", K),

sa("Đun nóng đẳng tích khí lí tưởng đơn nguyên tử trong bình 2,0 L từ 1,0·10⁵ Pa lên 1,6·10⁵ Pa. Nhiệt "
   "lượng khí nhận được bằng bao nhiêu jun?",
   "180", "ΔU = 1,5·ΔpV = 1,5 · 0,6·10⁵ · 2,0·10⁻³ = 180 J; đẳng tích nên Q = ΔU = 180 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

sa("Cần cung cấp bao nhiêu kilôjun để biến 0,10 kg nước đá ở 0 °C thành nước ở 20 °C? "
   "Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "42,4", "Q = 3,4·10⁵ · 0,10 + 0,10 · 4200 · 20 = 34 000 + 8400 = 42 400 J = 42,4 kJ.",
   "Nhiệt nóng chảy riêng", TB),
])


# =====================================================================
DE5 = dict(
ma="MIX-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Chu trình như một động cơ nhiệt: nhiệt nhận, nhiệt thải, công và hiệu suất",
P1=[
mc("Với chu trình 1(1 L; 1·10⁵ Pa) → 2(1 L; 3·10⁵ Pa) → 3(3 L; 3·10⁵ Pa) → 4(3 L; 1·10⁵ Pa) → 1 của khí "
   "lí tưởng đơn nguyên tử (U = (3/2)pV), tổng nhiệt lượng khí NHẬN VÀO trong cả chu trình là",
   ["400 J.", "1500 J.", "1800 J.", "2400 J."],
   "C",
   "Khí nhận nhiệt ở hai chặng đầu:\n"
   "1 → 2 (đẳng tích): Q = ΔU = 450 − 150 = 300 J.\n"
   "2 → 3 (đẳng áp): Q = ΔU + A′ = (1350 − 450) + 600 = 1500 J.\n"
   "Tổng nhiệt nhận vào: 300 + 1500 = 1800 J.",
   "Chu trình – động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh",
   cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, tổng nhiệt lượng khí TOẢ RA trong cả chu trình là",
   ["400 J.", "900 J.", "1400 J.", "1800 J."],
   "C",
   "3 → 4 (đẳng tích): Q = ΔU = 450 − 1350 = −900 J.\n"
   "4 → 1 (đẳng áp, bị nén): Q = ΔU − A = (150 − 450) − 200 = −500 J.\n"
   "Tổng toả ra: 900 + 500 = 1400 J.",
   "Chu trình – động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh",
   cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình trên, hiệu suất của chu trình (coi như một động cơ nhiệt) gần nhất với",
   ["16,7%.", "22,2%.", "28,6%.", "33,3%."],
   "B",
   "H = A′/Q_nhận = (1800 − 1400)/1800 = 400/1800 ≈ 0,222 = 22,2%.\n"
   "Kiểm tra: A′ cũng bằng diện tích hình chữ nhật 2·10⁵ · 2·10⁻³ = 400 J ✓",
   "Hiệu suất động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh",
   cap="Chu trình trên giản đồ p–V"),

mc("Một động cơ nhiệt nhận 2000 J từ nguồn nóng và thải 1400 J cho nguồn lạnh trong mỗi chu trình. Hiệu "
   "suất của động cơ là",
   ["20%.", "30%.", "40%.", "70%."],
   "B", "A′ = 2000 − 1400 = 600 J ⟹ H = 600/2000 = 30%.",
   "Hiệu suất động cơ nhiệt", TB),

mc("Trong chu trình ở các câu trên, trạng thái nào có nhiệt độ cao nhất?",
   ["Trạng thái (1).", "Trạng thái (2).", "Trạng thái (3).", "Trạng thái (4)."],
   "C",
   "T ∝ pV: (pV)₁ = 1; (pV)₂ = 3; (pV)₃ = 9; (pV)₄ = 3 (đơn vị 10⁵ Pa·L).\n"
   "Trạng thái (3) có tích pV lớn nhất nên nhiệt độ cao nhất.",
   "Đọc giản đồ p–V", TB, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Một khối khí lí tưởng nhận nhiệt lượng 1200 J và nội năng tăng 750 J. Công khí sinh ra là",
   ["450 J.", "750 J.", "1200 J.", "1950 J."],
   "A", "ΔU = A + Q ⟹ 750 = A + 1200 ⟹ A = −450 J: khí sinh công 450 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử, khí sinh công 500 J. Nhiệt lượng khí nhận được là",
   ["750 J.", "1000 J.", "1250 J.", "1500 J."],
   "C",
   "Đẳng áp: A′ = nRΔT = 500 J ⟹ ΔU = (3/2)nRΔT = 750 J ⟹ Q = ΔU + A′ = 1250 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Nhiệt lượng cần cung cấp để đun sôi rồi hoá hơi hoàn toàn 0,10 kg nước ban đầu ở 40 °C là "
   "(c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg)",
   ["226,0 kJ.", "251,2 kJ.", "276,4 kJ.", "302,0 kJ."],
   "B",
   "Q₁ = 0,10 · 4200 · 60 = 25 200 J; Q₂ = 2,26·10⁶ · 0,10 = 226 000 J.\nQ = 251 200 J = 251,2 kJ.",
   "Nhiệt hoá hơi riêng", TB),

mc("Một bình kín thể tích 5,0 L chứa khí lí tưởng đơn nguyên tử ở 2,0·10⁵ Pa. Cung cấp cho khí 300 J. "
   "Áp suất khí sau đó là (U = (3/2)pV)",
   ["2,2·10⁵ Pa.", "2,4·10⁵ Pa.", "2,6·10⁵ Pa.", "3,0·10⁵ Pa."],
   "B",
   "U₁ = 1,5 · 2,0·10⁵ · 5,0·10⁻³ = 1500 J. Đẳng tích ⟹ U₂ = 1500 + 300 = 1800 J.\n"
   "p₂ = p₁·U₂/U₁ = 2,0·10⁵ · 1800/1500 = 2,4·10⁵ Pa.",
   "Nội năng – đẳng tích (C1 + C2)", K),

mc("Hiệu suất của một động cơ nhiệt được định nghĩa là",
   ["tỉ số giữa nhiệt lượng thải ra và nhiệt lượng nhận vào.",
    "tỉ số giữa công sinh ra và nhiệt lượng nhận vào từ nguồn nóng.",
    "tỉ số giữa nhiệt lượng nhận vào và công sinh ra.",
    "hiệu giữa nhiệt lượng nhận vào và nhiệt lượng thải ra."],
   "B", "H = A′/Q_nóng. Vì luôn phải thải một phần nhiệt cho nguồn lạnh nên H luôn nhỏ hơn 100%.",
   "Hiệu suất động cơ nhiệt", TB),

mc("Trong một chu trình, nếu khí nhận 1800 J và thải 1400 J thì công khí sinh ra là",
   ["400 J.", "1400 J.", "1800 J.", "3200 J."],
   "A", "ΔU = 0 sau một chu trình ⟹ A′ = Q_nhận − Q_thải = 1800 − 1400 = 400 J.",
   "Định luật I – chu trình", TB),

mc("Một lượng khí lí tưởng thực hiện quá trình đẳng nhiệt, thể tích tăng từ 2,0 L lên 6,0 L ở nhiệt độ "
   "300 K. Trong quá trình đó",
   ["nội năng khí tăng.", "nội năng khí giảm.",
    "nội năng khí không đổi và khí nhận nhiệt.", "khí toả nhiệt."],
   "C",
   "Đẳng nhiệt ⟹ ΔU = 0. Khí giãn nở nên sinh công (A < 0) ⟹ Q = −A > 0: khí nhận nhiệt.",
   "Định luật I + đẳng nhiệt", TB),

mc("Trong một quá trình, khí lí tưởng có nhiệt độ giảm nhưng vẫn nhận nhiệt lượng. Điều đó xảy ra khi",
   ["quá trình là đẳng tích.", "quá trình là đẳng nhiệt.",
    "công mà khí sinh ra lớn hơn nhiệt lượng nhận vào.",
    "điều đó không thể xảy ra."],
   "C", "ΔU = A + Q < 0 khi |A| > Q với A < 0, tức khí sinh công nhiều hơn nhiệt lượng nhận được.",
   "Định luật I – phân tích tình huống", K),

mc("Nhiệt lượng cần để làm nóng chảy hoàn toàn 0,50 kg nước đá ở −10 °C là "
   "(c_đá = 2100 J/(kg·K), λ = 3,4·10⁵ J/kg)",
   ["170,0 kJ.", "180,5 kJ.", "190,0 kJ.", "200,5 kJ."],
   "B", "Q = 0,50 · 2100 · 10 + 3,4·10⁵ · 0,50 = 10 500 + 170 000 = 180 500 J = 180,5 kJ.",
   "Nhiệt nóng chảy riêng", TB),

mc("Nếu tăng nhiệt độ tuyệt đối của một lượng khí lí tưởng lên 1,5 lần thì nội năng và tốc độ căn quân "
   "phương của phân tử lần lượt",
   ["đều tăng 1,5 lần.", "tăng 1,5 lần và tăng 1,22 lần.",
    "tăng 2,25 lần và tăng 1,5 lần.", "đều tăng 1,22 lần."],
   "B",
   "U ∝ T ⟹ tăng 1,5 lần. v ∝ √T ⟹ tăng √1,5 ≈ 1,22 lần.",
   "Nội năng – tốc độ phân tử (C1 + C2)", K),

mc("Một khối khí lí tưởng thực hiện chu trình gồm ba chặng. Nếu hai chặng đầu khí nhận tổng cộng 900 J "
   "nhiệt và chặng cuối toả 500 J thì công khí sinh ra trong cả chu trình là",
   ["400 J.", "500 J.", "900 J.", "1400 J."],
   "A", "ΔU = 0 ⟹ A′ = Q_nhận − Q_thải = 900 − 500 = 400 J.",
   "Định luật I – chu trình", TB),

mc("Trong quá trình đẳng áp của khí lí tưởng đơn nguyên tử, tỉ số giữa công khí sinh ra và nhiệt lượng "
   "khí nhận được bằng",
   ["2/5.", "3/5.", "2/3.", "3/2."],
   "A", "A′ = nRΔT và Q = (5/2)nRΔT ⟹ A′/Q = 1/(5/2) = 2/5 = 40%.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Trong bốn quá trình sau, quá trình nào khí lí tưởng KHÔNG thể nhận nhiệt lượng?",
   ["Đẳng áp giãn nở.", "Đẳng tích tăng áp suất.",
    "Đẳng nhiệt giãn nở.", "Nén trong bình cách nhiệt."],
   "D", "Bình cách nhiệt nghĩa là Q = 0 theo định nghĩa; ba quá trình còn lại đều có Q > 0.",
   "Định luật I – bốn quá trình", TB),
],
P2=[
ds("Chu trình 1(1 L; 1·10⁵ Pa) → 2(1 L; 3·10⁵ Pa) → 3(3 L; 3·10⁵ Pa) → 4(3 L; 1·10⁵ Pa) → 1 của khí lí "
   "tưởng đơn nguyên tử; U = (3/2)pV.",
   [("Khí nhận nhiệt ở hai chặng 1 → 2 và 2 → 3, tổng cộng 1800 J.", True,
     "Đúng. Q₁₂ = ΔU = 300 J; Q₂₃ = ΔU + A′ = 900 + 600 = 1500 J; tổng 1800 J."),
    ("Khí toả nhiệt ở hai chặng 3 → 4 và 4 → 1, tổng cộng 1400 J.", True,
     "Đúng. Q₃₄ = ΔU = −900 J; Q₄₁ = ΔU − A = −300 − 200 = −500 J; tổng toả 1400 J."),
    ("Hiệu suất của chu trình khi coi như một động cơ nhiệt là khoảng 22,2%.", True,
     "Đúng. H = A′/Q_nhận = 400/1800 ≈ 22,2%."),
    ("Vì khí nhận 1800 J và sinh công 400 J nên 1400 J còn lại đã biến thành nội năng của khí.", False,
     "Sai. Sau một chu trình ΔU = 0 nên nội năng không hề tăng; 1400 J đó đã bị THẢI ra nguồn lạnh. "
     "Đây chính là giới hạn cơ bản của mọi động cơ nhiệt.")],
   "Chu trình như một động cơ nhiệt (C1 + C2)", K,
   fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

ds("Một bình kín thể tích 5,0 L chứa khí lí tưởng đơn nguyên tử ở áp suất 2,0·10⁵ Pa và nhiệt độ 300 K. "
   "Cung cấp cho khí nhiệt lượng 300 J. Cho U = (3/2)pV.",
   [("Nội năng ban đầu của khối khí là 1500 J.", True,
     "Đúng. U = 1,5 · 2,0·10⁵ · 5,0·10⁻³ = 1500 J."),
    ("Vì bình kín nên toàn bộ 300 J làm tăng nội năng của khí.", True,
     "Đúng. Thể tích không đổi ⟹ A = 0 ⟹ ΔU = Q = 300 J."),
    ("Áp suất khí sau khi cung cấp nhiệt là 2,4·10⁵ Pa.", True,
     "Đúng. U₂ = 1800 J; với V không đổi thì p ∝ U ⟹ p₂ = 2,0·10⁵ · 1800/1500 = 2,4·10⁵ Pa."),
    ("Nhiệt độ khí sau khi cung cấp nhiệt là 300 · 1800/1500 = 360 K, và khí đã sinh công 300 J.", False,
     "Vế đầu đúng (T₂ = 360 K vì U ∝ T), nhưng vế sau SAI: bình kín nên khí không sinh công, A = 0.")],
   "Nội năng – đẳng tích (C1 + C2)", K),

ds("Xét quá trình đẳng áp của một lượng khí lí tưởng đơn nguyên tử.",
   [("Công khí sinh ra chiếm 40% nhiệt lượng khí nhận được.", True,
     "Đúng. A′ = nRΔT, Q = (5/2)nRΔT ⟹ A′/Q = 2/5 = 40%."),
    ("Nếu khí sinh công 500 J thì nhiệt lượng nhận được là 1250 J.", True,
     "Đúng. Q = A′/0,4 = 500/0,4 = 1250 J (trong đó 750 J làm tăng nội năng)."),
    ("Trong quá trình đẳng áp, nhiệt độ khí tỉ lệ thuận với thể tích khí.", True,
     "Đúng, đó chính là định luật Charles: V/T = hằng số."),
    ("Trong quá trình đẳng áp, nội năng khí không đổi vì áp suất không đổi.", False,
     "Sai. Nội năng phụ thuộc NHIỆT ĐỘ, mà đẳng áp thì nhiệt độ thay đổi cùng với thể tích, nên nội năng "
     "cũng thay đổi.")],
   "Định luật I + đẳng áp (C1 + C2)", K),

ds("Xét việc phân tích các quá trình nhiệt bằng định luật I.",
   [("Một động cơ nhiệt nhận 2000 J và thải 1400 J mỗi chu trình thì hiệu suất là 30%.", True,
     "Đúng. A′ = 600 J ⟹ H = 600/2000 = 30%."),
    ("Nhiệt độ của khí lí tưởng có thể giảm ngay cả khi khí đang nhận nhiệt.", True,
     "Đúng, khi công khí sinh ra lớn hơn nhiệt lượng nhận vào: ΔU = A + Q < 0."),
    ("Trong quá trình giãn nở đẳng nhiệt, khí vừa nhận nhiệt vừa sinh công với độ lớn bằng nhau.", True,
     "Đúng. ΔU = 0 ⟹ Q = −A = A′."),
    ("Có thể chế tạo một động cơ nhiệt biến toàn bộ nhiệt lượng nhận được thành công, tức hiệu suất 100%.", False,
     "Sai. Mọi động cơ nhiệt đều phải thải một phần nhiệt cho nguồn lạnh; điều này được xác nhận bởi "
     "toàn bộ thực nghiệm và là nội dung của nguyên lí thứ hai nhiệt động lực học.")],
   "Định luật I – động cơ nhiệt", K),
],
P3=[
sa("Với chu trình 1(1 L; 1·10⁵ Pa) → 2(1 L; 3·10⁵ Pa) → 3(3 L; 3·10⁵ Pa) → 4(3 L; 1·10⁵ Pa) → 1 của khí "
   "lí tưởng đơn nguyên tử, tổng nhiệt lượng khí nhận vào trong cả chu trình bằng bao nhiêu jun?",
   "1800", "Q₁₂ = 300 J (đẳng tích) và Q₂₃ = 900 + 600 = 1500 J (đẳng áp) ⟹ tổng 1800 J.",
   "Chu trình – động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Vẫn với chu trình đó, hiệu suất của chu trình bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "22,2", "A′ = 400 J; Q_nhận = 1800 J ⟹ H = 400/1800 ≈ 22,2%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Đun nóng đẳng áp khí lí tưởng đơn nguyên tử, khí sinh công 500 J. Nhiệt lượng khí nhận được bằng bao "
   "nhiêu jun?",
   "1250", "ΔU = 1,5 · 500 = 750 J ⟹ Q = 750 + 500 = 1250 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

sa("Một bình kín 5,0 L chứa khí lí tưởng đơn nguyên tử ở 2,0·10⁵ Pa. Cung cấp cho khí 300 J. Áp suất khí "
   "sau đó bằng bao nhiêu (đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ nhất)? Cho U = (3/2)pV.",
   "2,4", "U₁ = 1500 J ⟹ U₂ = 1800 J; V không đổi nên p₂ = 2,0·10⁵ · 1800/1500 = 2,4·10⁵ Pa.",
   "Nội năng – đẳng tích (C1 + C2)", K),

sa("Nhiệt lượng cần để đun sôi rồi hoá hơi hoàn toàn 0,10 kg nước ban đầu ở 40 °C bằng bao nhiêu kilôjun "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
   "251,2", "Q = 0,10·4200·60 + 2,26·10⁶·0,10 = 25 200 + 226 000 = 251 200 J = 251,2 kJ.",
   "Nhiệt hoá hơi riêng", TB),

sa("Một động cơ nhiệt nhận 2000 J từ nguồn nóng và thải 1400 J cho nguồn lạnh mỗi chu trình. Hiệu suất "
   "của động cơ bằng bao nhiêu phần trăm?",
   "30", "A′ = 2000 − 1400 = 600 J ⟹ H = 600/2000 = 30%.", "Hiệu suất động cơ nhiệt", TB),
])


# =====================================================================
DE6 = dict(
ma="MIX-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Chu trình tam giác trên giản đồ p–V; công bằng diện tích; kết hợp bài toán nhiệt",
P1=[
mc("Hình bên là chu trình A → B → C → A của một lượng khí lí tưởng đơn nguyên tử, với A(1 L; 1·10⁵ Pa), "
   "B(1 L; 3·10⁵ Pa), C(3 L; 1·10⁵ Pa). Quá trình A → B là",
   ["đẳng áp.", "đẳng nhiệt.", "đẳng tích.", "không phải đẳng quá trình nào."],
   "C", "Đoạn AB thẳng đứng trên giản đồ (p, V) ⟹ thể tích không đổi ⟹ quá trình đẳng tích.",
   "Nhận dạng quá trình", D, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác A → B → C → A"),

mc("Vẫn với chu trình trên, hai trạng thái nào có cùng nhiệt độ?",
   ["A và B.", "B và C.", "A và C.", "Không có hai trạng thái nào."],
   "B",
   "T ∝ pV: (pV)_A = 1·1 = 1; (pV)_B = 1·3 = 3; (pV)_C = 3·1 = 3 (đơn vị 10⁵ Pa·L).\n"
   "Vậy B và C có cùng nhiệt độ (và cùng nội năng).",
   "Đọc giản đồ p–V", TB, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Vẫn với chu trình trên, công mà khí sinh ra trong chặng B → C bằng",
   ["200 J.", "300 J.", "400 J.", "600 J."],
   "C",
   "Công bằng diện tích hình thang dưới đoạn BC:\n"
   "A′ = ½(p_B + p_C)·ΔV = ½(3 + 1)·10⁵ · 2·10⁻³ = ½ · 4·10⁵ · 2·10⁻³ = 400 J.",
   "Công của khí trên giản đồ p–V", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Vẫn với chu trình trên, nhiệt lượng khí nhận được trong chặng B → C bằng",
   ["0 J.", "400 J.", "600 J.", "900 J."],
   "B",
   "B và C có cùng tích pV nên cùng nhiệt độ ⟹ ΔU = 0.\nQ = ΔU + A′ = 0 + 400 = 400 J.",
   "Định luật I trên giản đồ p–V", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Vẫn với chu trình trên, công mà khí sinh ra trong CẢ CHU TRÌNH bằng",
   ["100 J.", "200 J.", "400 J.", "600 J."],
   "B",
   "Công của cả chu trình bằng diện tích tam giác ABC:\n"
   "A′ = ½ · ΔV · Δp = ½ · 2·10⁻³ · 2·10⁵ = 200 J.\n"
   "(Kiểm tra: A′_BC − A_CA = 400 − 200 = 200 J ✓)",
   "Công trong chu trình", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Vẫn với chu trình trên, nhiệt lượng khí nhận được trong chặng A → B bằng (U = (3/2)pV)",
   ["150 J.", "300 J.", "450 J.", "600 J."],
   "B", "Đẳng tích ⟹ A = 0; U_A = 150 J, U_B = 450 J ⟹ Q = ΔU = 300 J.",
   "Định luật I + đẳng tích", TB, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Vẫn với chu trình trên, trong chặng C → A khí",
   ["nhận công 200 J và nhận nhiệt 500 J.", "nhận công 200 J và toả nhiệt 500 J.",
    "sinh công 200 J và toả nhiệt 500 J.", "sinh công 400 J và nhận nhiệt 100 J."],
   "B",
   "C → A là đẳng áp ở 1·10⁵ Pa, thể tích giảm từ 3 L xuống 1 L ⟹ khí NHẬN công "
   "A = 1·10⁵ · 2·10⁻³ = 200 J.\n"
   "ΔU = U_A − U_C = 150 − 450 = −300 J ⟹ Q = ΔU − A = −300 − 200 = −500 J: toả 500 J.",
   "Định luật I + đẳng áp", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

mc("Nhiệt lượng cần cung cấp để đun 2,0 kg nước từ 30 °C lên 90 °C là (c = 4200 J/(kg·K))",
   ["252 kJ.", "336 kJ.", "420 kJ.", "504 kJ."],
   "D", "Q = 2,0 · 4200 · 60 = 504 000 J = 504 kJ.", "Nhiệt dung riêng", D),

mc("Một lượng khí lí tưởng đơn nguyên tử có nội năng 900 J. Nếu nhiệt độ tuyệt đối giảm còn 2/3 giá trị "
   "ban đầu thì nội năng còn",
   ["300 J.", "450 J.", "600 J.", "675 J."],
   "C", "U ∝ T ⟹ U₂ = 900 · (2/3) = 600 J.", "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trong quá trình mà đường biểu diễn trên giản đồ (p, V) là đoạn thẳng đi xuống từ trái sang phải, khí",
   ["luôn nhận công.", "luôn sinh công.", "không trao đổi công.", "sinh công rồi nhận công."],
   "B",
   "Đường đi từ trái sang phải nghĩa là thể tích TĂNG, do đó khí giãn nở và sinh công (công bằng diện "
   "tích dưới đường biểu diễn).",
   "Công của khí trên giản đồ p–V", TB),

mc("Thả 0,10 kg nước đá ở 0 °C vào 0,40 kg nước ở 25 °C trong bình cách nhiệt. Cho λ = 3,4·10⁵ J/kg, "
   "c = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt gần nhất với",
   ["0 °C.", "3,7 °C.", "8,0 °C.", "12,5 °C."],
   "B",
   "Nước nhường tối đa 0,40 · 4200 · 25 = 42 000 J > 34 000 J cần để tan hết đá ⟹ đá tan hết.\n"
   "34 000 + 0,10 · 4200 · t = 0,40 · 4200 · (25 − t) ⟹ 34 000 + 420t = 42 000 − 1680t\n"
   "⟹ 2100t = 8000 ⟹ t ≈ 3,8 °C, gần nhất với 3,7 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

mc("Một khối khí lí tưởng thực hiện quá trình đẳng nhiệt. Trên giản đồ (p, V), công khí sinh ra bằng",
   ["0.", "p·ΔV với p là áp suất trung bình.",
    "diện tích dưới nhánh hypebol biểu diễn quá trình.", "ΔU."],
   "C",
   "Công luôn bằng diện tích dưới đường biểu diễn quá trình trên giản đồ (p, V). Với đẳng nhiệt, đường đó "
   "là nhánh hypebol nên công không tính được bằng công thức p·ΔV đơn giản.",
   "Công của khí trên giản đồ p–V", K),

mc("Đun nóng đẳng tích một khối khí lí tưởng đơn nguyên tử từ 1,0·10⁵ Pa lên 2,5·10⁵ Pa trong bình 4,0 L. "
   "Nhiệt lượng khí nhận được là (U = (3/2)pV)",
   ["600 J.", "750 J.", "900 J.", "1500 J."],
   "C", "ΔU = 1,5 · (2,5 − 1,0)·10⁵ · 4,0·10⁻³ = 1,5 · 600 = 900 J; đẳng tích nên Q = ΔU = 900 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

mc("Muốn tăng nội năng của một khối khí lí tưởng mà không cung cấp nhiệt cho nó, ta phải",
   ["cho khí giãn nở.", "nén khí.", "giữ thể tích không đổi.", "làm lạnh khí."],
   "B", "Q = 0 ⟹ ΔU = A; muốn ΔU > 0 phải có A > 0, tức phải thực hiện công NÉN khí.",
   "Định luật I – thực hiện công", TB),

mc("Trong một chu trình, khí nhận 700 J nhiệt và toả 500 J nhiệt. Hiệu suất của chu trình bằng",
   ["20,0%.", "28,6%.", "40,0%.", "71,4%."],
   "B", "A′ = 700 − 500 = 200 J ⟹ H = 200/700 ≈ 28,6%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", K),

mc("Nhiệt lượng cần để làm hoá hơi hoàn toàn 0,050 kg nước ở 100 °C bằng nhiệt lượng cần để đun bao nhiêu "
   "kilôgam nước từ 20 °C lên 100 °C? Cho L = 2,26·10⁶ J/kg, c = 4200 J/(kg·K).",
   ["0,24 kg.", "0,34 kg.", "0,45 kg.", "0,67 kg."],
   "B",
   "Q = Lm = 2,26·10⁶ · 0,050 = 113 000 J.\n"
   "m′ = Q/(cΔt) = 113 000/(4200 · 80) = 113 000/336 000 ≈ 0,34 kg.",
   "So sánh các đại lượng nhiệt", K),

mc("Một khối khí lí tưởng có áp suất tăng gấp đôi trong khi thể tích giảm một nửa. Nội năng của khí",
   ["tăng 4 lần.", "giảm 4 lần.", "không đổi.", "tăng 2 lần."],
   "C", "U = (3/2)pV; tích pV không đổi (2 · ½ = 1) ⟹ nhiệt độ và nội năng không đổi.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trong bốn phát biểu sau, phát biểu nào ĐÚNG?",
   ["Nhiệt lượng khí nhận được luôn bằng độ tăng nội năng của khí.",
    "Công khí sinh ra luôn bằng nhiệt lượng khí nhận được.",
    "Trong một chu trình kín, tổng công khí sinh ra bằng tổng nhiệt lượng khí nhận được.",
    "Nội năng của khí luôn tăng khi thể tích khí tăng."],
   "C",
   "Sau một chu trình ΔU = 0 nên A′_tổng = Q_tổng. Phát biểu 1 chỉ đúng cho đẳng tích, phát biểu 2 chỉ "
   "đúng cho đẳng nhiệt, phát biểu 4 sai vì nội năng phụ thuộc nhiệt độ chứ không phải thể tích.",
   "Định luật I – tổng hợp", K),
],
P2=[
ds("Chu trình A(1 L; 1·10⁵ Pa) → B(1 L; 3·10⁵ Pa) → C(3 L; 1·10⁵ Pa) → A của khí lí tưởng đơn nguyên tử; "
   "cho U = (3/2)pV.",
   [("Hai trạng thái B và C có cùng nhiệt độ và cùng nội năng.", True,
     "Đúng. (pV)_B = 1 · 3 = 3 = 3 · 1 = (pV)_C ⟹ T_B = T_C ⟹ U_B = U_C = 450 J."),
    ("Trong chặng B → C, khí sinh công 400 J và nhận nhiệt lượng đúng 400 J.", True,
     "Đúng. A′ = ½(3 + 1)·10⁵ · 2·10⁻³ = 400 J; ΔU = 0 (vì T_B = T_C) ⟹ Q = 400 J."),
    ("Công khí sinh ra trong cả chu trình bằng 400 J.", False,
     "Sai. Công của cả chu trình bằng diện tích TAM GIÁC ABC: A′ = ½ · 2·10⁻³ · 2·10⁵ = 200 J. "
     "Giá trị 400 J chỉ là công của riêng chặng B → C, chưa trừ công 200 J mà khí nhận lại ở chặng C → A."),
    ("Hiệu suất của chu trình khi coi như động cơ nhiệt là khoảng 28,6%.", True,
     "Đúng. Khí nhận nhiệt ở A → B (300 J) và B → C (400 J), tổng 700 J; A′ = 200 J ⟹ "
     "H = 200/700 ≈ 28,6%.")],
   "Chu trình tam giác – định luật I (C1 + C2)", K,
   fig="k_dt_chutrinh_tg", cap="Chu trình tam giác trên giản đồ p–V"),

ds("Thả 0,10 kg nước đá ở 0 °C vào 0,40 kg nước ở 25 °C trong bình cách nhiệt lí tưởng. "
   "Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   [("Nhiệt lượng lớn nhất mà nước có thể nhường là 42 kJ.", True,
     "Đúng. Q = 0,40 · 4200 · 25 = 42 000 J khi nước hạ tới 0 °C."),
    ("Toàn bộ nước đá sẽ tan hết.", True,
     "Đúng. Làm tan hết 0,10 kg đá chỉ cần 34 000 J < 42 000 J."),
    ("Nhiệt độ khi cân bằng nhiệt vào khoảng 3,8 °C.", True,
     "Đúng. 34 000 + 420t = 42 000 − 1680t ⟹ 2100t = 8000 ⟹ t ≈ 3,8 °C."),
    ("Nếu tăng khối lượng nước đá lên 0,20 kg thì nhiệt độ cân bằng vẫn cao hơn 0 °C.", False,
     "Sai. Với 0,20 kg đá cần 68 000 J để tan hết, lớn hơn 42 000 J mà nước có thể nhường ⟹ đá chỉ tan "
     "một phần và nhiệt độ cân bằng đúng bằng 0 °C.")],
   "Cân bằng nhiệt có chuyển thể", K),

ds("Xét cách tính công của khí trên giản đồ (p, V).",
   [("Công khí sinh ra bằng diện tích hình giới hạn bởi đường biểu diễn quá trình và trục V.", True,
     "Đúng, đó là ý nghĩa hình học của công trong quá trình biến đổi thể tích."),
    ("Với quá trình đẳng áp, diện tích đó là hình chữ nhật nên A′ = p·ΔV.", True,
     "Đúng. Đường biểu diễn nằm ngang nên hình dưới nó là hình chữ nhật."),
    ("Với quá trình biểu diễn bằng đoạn thẳng từ (V₁, p₁) tới (V₂, p₂), công bằng "
     "½(p₁ + p₂)(V₂ − V₁).", True,
     "Đúng. Hình dưới đoạn thẳng là hình thang có hai đáy p₁, p₂ và chiều cao (V₂ − V₁)."),
    ("Trong quá trình đẳng tích, công khí sinh ra bằng p·V.", False,
     "Sai. Đẳng tích thì ΔV = 0 nên A′ = 0; “diện tích” dưới một đoạn thẳng đứng bằng không.")],
   "Công của khí trên giản đồ p–V", K),

ds("Xét một số so sánh về độ lớn của các đại lượng nhiệt.",
   [("Nhiệt lượng để làm hoá hơi hoàn toàn 0,050 kg nước ở 100 °C bằng nhiệt lượng để đun khoảng 0,34 kg "
     "nước từ 20 °C lên 100 °C.", True,
     "Đúng. Q = 2,26·10⁶ · 0,050 = 113 000 J; m′ = 113 000/(4200 · 80) ≈ 0,34 kg."),
    ("Nhiệt lượng để đun 2,0 kg nước từ 30 °C lên 90 °C là 504 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · 60 = 504 000 J."),
    ("Công mà khí sinh ra khi giãn 2,0 L ở áp suất 10⁵ Pa là 200 J, tức nhỏ hơn hàng nghìn lần nhiệt "
     "lượng ở ý trên.", True,
     "Đúng. A′ = 10⁵ · 2,0·10⁻³ = 200 J; 504 000/200 = 2520 lần."),
    ("Vì công của khí nhỏ hơn nhiều so với nhiệt lượng nên trong định luật I có thể bỏ qua số hạng công.", False,
     "Sai. Việc số hạng nào lớn hơn phụ thuộc hoàn toàn vào từng bài toán cụ thể. Trong quá trình đẳng "
     "áp của khí lí tưởng đơn nguyên tử, công chiếm tới 40% nhiệt lượng nhận vào — không thể bỏ qua.")],
   "So sánh độ lớn năng lượng (C1 + C2)", K),
],
P3=[
sa("Với chu trình A(1 L; 1·10⁵ Pa) → B(1 L; 3·10⁵ Pa) → C(3 L; 1·10⁵ Pa) → A, công mà khí sinh ra trong "
   "chặng B → C bằng bao nhiêu jun?",
   "400", "A′ = ½(p_B + p_C)·ΔV = ½(3 + 1)·10⁵ · 2·10⁻³ = 400 J (diện tích hình thang).",
   "Công của khí trên giản đồ p–V", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

sa("Vẫn với chu trình đó, công mà khí sinh ra trong cả chu trình bằng bao nhiêu jun?",
   "200", "A′ = diện tích tam giác ABC = ½ · 2·10⁻³ · 2·10⁵ = 200 J.",
   "Công trong chu trình", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

sa("Vẫn với chu trình đó, hiệu suất của chu trình bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "28,6",
   "Khí nhận nhiệt ở A → B (Q = ΔU = 300 J) và B → C (Q = 400 J), tổng 700 J.\n"
   "H = A′/Q_nhận = 200/700 ≈ 28,6%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh_tg", cap="Chu trình tam giác"),

sa("Thả 0,10 kg nước đá ở 0 °C vào 0,40 kg nước ở 25 °C trong bình cách nhiệt. Nhiệt độ khi cân bằng bằng "
   "bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "3,8",
   "Đá tan hết (34 kJ < 42 kJ). 34 000 + 420t = 42 000 − 1680t ⟹ 2100t = 8000 ⟹ t ≈ 3,8 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

sa("Đun nóng đẳng tích khí lí tưởng đơn nguyên tử trong bình 4,0 L từ 1,0·10⁵ Pa lên 2,5·10⁵ Pa. Nhiệt "
   "lượng khí nhận được bằng bao nhiêu jun? Cho U = (3/2)pV.",
   "900", "ΔU = 1,5 · 1,5·10⁵ · 4,0·10⁻³ = 900 J; đẳng tích nên Q = ΔU = 900 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

sa("Nhiệt lượng để làm hoá hơi hoàn toàn 0,050 kg nước ở 100 °C có thể đun bao nhiêu kilôgam nước từ "
   "20 °C lên 100 °C (làm tròn đến chữ số thập phân thứ hai)? Cho L = 2,26·10⁶ J/kg, c = 4200 J/(kg·K).",
   "0,34", "Q = 2,26·10⁶ · 0,050 = 113 000 J ⟹ m = 113 000/(4200 · 80) ≈ 0,34 kg.",
   "So sánh các đại lượng nhiệt", K),
])


# =====================================================================
DE7 = dict(
ma="MIX-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Quá trình hai chặng có vấu chặn; trao đổi nhiệt giữa khí và nước; đường thẳng trên p–V",
P1=[
mc("Một xilanh thẳng đứng tiết diện 100 cm² chứa cột khí lí tưởng đơn nguyên tử cao 20 cm ở 300 K, áp "
   "suất 1,0·10⁵ Pa; pit-tông nhẹ dịch chuyển không ma sát, cách pit-tông 5 cm có vấu chặn. Đun nóng khí. "
   "Công khí sinh ra cho tới khi pit-tông chạm vấu là",
   ["25 J.", "50 J.", "75 J.", "125 J."],
   "B",
   "Chặng này là đẳng áp: ΔV = S·Δh = 100·10⁻⁴ · 0,05 = 5,0·10⁻⁴ m³.\n"
   "A′ = p·ΔV = 1,0·10⁵ · 5,0·10⁻⁴ = 50 J.",
   "Xilanh có vấu chặn + công (C1 + C2)", K, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với xilanh trên, nhiệt lượng khí nhận được trong chặng đẳng áp đó là (U = (3/2)pV)",
   ["50 J.", "75 J.", "125 J.", "200 J."],
   "C", "ΔU = 1,5 · A′ = 1,5 · 50 = 75 J (vì đẳng áp) ⟹ Q = ΔU + A′ = 75 + 50 = 125 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Vẫn với xilanh trên, nhiệt độ của khí khi pit-tông vừa chạm vấu chặn là",
   ["330 K.", "360 K.", "375 K.", "450 K."],
   "C", "Đẳng áp ⟹ T ∝ chiều cao cột khí: T₂ = 300 · 25/20 = 375 K.",
   "Định luật Charles", TB),

mc("Sau khi pit-tông chạm vấu, tiếp tục đun tới khi áp suất khí đạt 1,6·10⁵ Pa. Nhiệt lượng khí nhận thêm "
   "trong chặng này là",
   ["150 J.", "225 J.", "300 J.", "375 J."],
   "B",
   "Chặng này là đẳng tích (V = 100·10⁻⁴ · 0,25 = 2,5·10⁻³ m³) nên A = 0:\n"
   "Q = ΔU = 1,5 · Δp · V = 1,5 · (1,6 − 1,0)·10⁵ · 2,5·10⁻³ = 1,5 · 150 = 225 J.",
   "Định luật I + đẳng tích (C1 + C2)", K),

mc("Với hai chặng ở các câu trên, tổng nhiệt lượng khí đã nhận được là",
   ["225 J.", "275 J.", "350 J.", "425 J."],
   "C", "Q = Q₁ + Q₂ = 125 + 225 = 350 J.",
   "Quá trình hai chặng (C1 + C2)", K),

mc("Một bình cứng 10 L chứa khí lí tưởng đơn nguyên tử ở 5,0·10⁵ Pa và 600 K. Làm lạnh đẳng tích khí "
   "xuống 300 K. Nhiệt lượng khí toả ra là (U = (3/2)pV)",
   ["1875 J.", "3750 J.", "5625 J.", "7500 J."],
   "B",
   "U₁ = 1,5 · 5,0·10⁵ · 10·10⁻³ = 7500 J. Nhiệt độ giảm một nửa nên U₂ = 3750 J.\n"
   "Đẳng tích ⟹ A = 0 ⟹ Q = ΔU = −3750 J: khí toả 3750 J.",
   "Nội năng – đẳng tích (C1 + C2)", K),

mc("Nếu dùng toàn bộ nhiệt lượng 3750 J ở câu trên để đun nước nóng thêm 10 °C thì khối lượng nước đun "
   "được gần nhất với (c = 4200 J/(kg·K))",
   ["45 g.", "89 g.", "125 g.", "180 g."],
   "B", "m = Q/(c·Δt) = 3750/(4200 · 10) = 3750/42 000 ≈ 0,089 kg = 89 g.",
   "Nối khí – nhiệt (C1 + C2)", K),

mc("Một lượng khí lí tưởng đơn nguyên tử biến đổi theo ĐOẠN THẲNG trên giản đồ (p, V) từ A(1 L; 4·10⁵ Pa) "
   "tới B(4 L; 1·10⁵ Pa). Công mà khí sinh ra bằng",
   ["300 J.", "500 J.", "750 J.", "1200 J."],
   "C",
   "Công bằng diện tích hình thang dưới đoạn AB:\n"
   "A′ = ½(p_A + p_B)·ΔV = ½(4 + 1)·10⁵ · 3·10⁻³ = ½ · 5·10⁵ · 3·10⁻³ = 750 J.",
   "Công của khí trên giản đồ p–V", K),

mc("Vẫn với quá trình A → B ở câu trên, nhiệt lượng khí nhận được bằng (U = (3/2)pV)",
   ["0 J.", "375 J.", "750 J.", "1125 J."],
   "C",
   "U_A = 1,5 · 4·10⁵ · 1·10⁻³ = 600 J; U_B = 1,5 · 1·10⁵ · 4·10⁻³ = 600 J ⟹ ΔU = 0.\n"
   "Q = ΔU + A′ = 0 + 750 = 750 J. (Chú ý: ΔU = 0 nhưng quá trình KHÔNG đẳng nhiệt — nhiệt độ tăng rồi "
   "giảm về giá trị cũ.)",
   "Định luật I trên giản đồ p–V", RK),

mc("Vẫn với quá trình A → B đó, nội năng của khí đạt giá trị LỚN NHẤT khi thể tích bằng",
   ["1,0 L.", "2,0 L.", "2,5 L.", "4,0 L."],
   "C",
   "Trên đoạn AB có p = (5 − V)·10⁵ Pa (V tính bằng L). Vì U = (3/2)pV nên U ∝ V(5 − V), là tam thức bậc "
   "hai hệ số âm, đạt cực đại tại đỉnh V = 2,5 L.",
   "Suy luận trên giản đồ p–V (C1 + C2)", RK),

mc("Nhiệt lượng cần cung cấp để đun 0,80 kg nước từ 25 °C lên 85 °C là (c = 4200 J/(kg·K))",
   ["168 kJ.", "202 kJ.", "252 kJ.", "336 kJ."],
   "B", "Q = 0,80 · 4200 · 60 = 201 600 J ≈ 202 kJ.", "Nhiệt dung riêng", D),

mc("Một khối khí lí tưởng nhận công 300 J trong bình cách nhiệt. Nhiệt độ của khí",
   ["giảm.", "tăng.", "không đổi.", "chưa xác định được."],
   "B", "Cách nhiệt ⟹ Q = 0 ⟹ ΔU = A = +300 J > 0 ⟹ nội năng và nhiệt độ đều tăng.",
   "Định luật I – thực hiện công", TB),

mc("Một lượng khí lí tưởng đơn nguyên tử ở 400 K có nội năng 1000 J. Nếu làm lạnh đẳng tích xuống 250 K "
   "thì nhiệt lượng khí toả ra là",
   ["250 J.", "375 J.", "500 J.", "625 J."],
   "B", "U ∝ T ⟹ U₂ = 1000 · 250/400 = 625 J ⟹ |ΔU| = 375 J; đẳng tích nên khí toả đúng 375 J.",
   "Nội năng – đẳng tích (C1 + C2)", TB),

mc("Trong quá trình có ΔU = 0 nhưng khí vẫn nhận nhiệt và sinh công, quá trình đó",
   ["chắc chắn là đẳng nhiệt.",
    "có nhiệt độ đầu bằng nhiệt độ cuối nhưng có thể thay đổi ở giữa.",
    "chắc chắn là đẳng tích.", "không thể xảy ra."],
   "B",
   "ΔU = 0 chỉ cho biết nhiệt độ ĐẦU bằng nhiệt độ CUỐI. Đường thẳng AB ở các câu trên là ví dụ: nhiệt "
   "độ tăng tới cực đại ở V = 2,5 L rồi giảm về giá trị ban đầu.",
   "Hàm trạng thái – phân biệt (C1 + C2)", RK),

mc("Cần cung cấp bao nhiêu nhiệt lượng để biến 0,20 kg nước đá ở −10 °C thành nước ở 20 °C? "
   "Cho c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   ["68,0 kJ.", "76,4 kJ.", "89,0 kJ.", "104,0 kJ."],
   "C",
   "Ba giai đoạn:\n"
   "Q₁ = 0,20 · 2100 · 10 = 4200 J (hâm đá từ −10 °C lên 0 °C)\n"
   "Q₂ = 0,20 · 3,4·10⁵ = 68 000 J (nóng chảy)\n"
   "Q₃ = 0,20 · 4200 · 20 = 16 800 J (đun nước từ 0 °C lên 20 °C)\n"
   "Q = 89 000 J = 89,0 kJ.",
   "Bài toán nhiệt nhiều giai đoạn", TB),

mc("Một khối khí lí tưởng có tích pV tăng từ 400 J lên 900 J. Nhiệt độ tuyệt đối của khí đã",
   ["tăng 1,5 lần.", "tăng 2,25 lần.", "tăng 500 lần.", "tăng 2,0 lần."],
   "B", "T ∝ pV ⟹ T₂/T₁ = 900/400 = 2,25 lần.", "Phương trình trạng thái", TB),

mc("Trong quá trình đẳng áp của khí lí tưởng đơn nguyên tử, nếu nhiệt độ tuyệt đối tăng gấp đôi thì nội "
   "năng và thể tích khí lần lượt",
   ["đều tăng gấp đôi.", "tăng gấp đôi và không đổi.",
    "không đổi và tăng gấp đôi.", "tăng 4 lần và tăng gấp đôi."],
   "A", "U ∝ T và (đẳng áp) V ∝ T ⟹ cả hai cùng tăng gấp đôi.",
   "Nội năng – đẳng áp (C1 + C2)", TB),

mc("Muốn xác định nhiệt lượng khí trao đổi trong một quá trình, ngoài trạng thái đầu và cuối, ta còn cần "
   "biết",
   ["khối lượng mol của khí.", "cách thức (đường đi) của quá trình.",
    "áp suất khí quyển.", "nhiệt dung riêng của bình."],
   "B",
   "Nhiệt lượng không phải hàm trạng thái. Muốn tính Q = ΔU − A phải biết A, mà A phụ thuộc đường đi của "
   "quá trình trên giản đồ (p, V).",
   "Hàm trạng thái (C1 + C2)", K),
],
P2=[
ds("Một xilanh thẳng đứng tiết diện 100 cm² chứa cột khí lí tưởng đơn nguyên tử cao 20 cm ở 300 K và "
   "1,0·10⁵ Pa; pit-tông nhẹ dịch chuyển không ma sát, vấu chặn cách pit-tông 5 cm. Đun nóng khí tới khi "
   "áp suất đạt 1,6·10⁵ Pa. Cho U = (3/2)pV.",
   [("Quá trình gồm hai chặng: đẳng áp rồi đẳng tích.", True,
     "Đúng. Trước khi chạm vấu pit-tông còn tự do (đẳng áp); sau khi chạm vấu thể tích bị giữ nguyên "
     "(đẳng tích)."),
    ("Trong chặng đẳng áp, khí sinh công 50 J và nhận nhiệt 125 J.", True,
     "Đúng. A′ = 1,0·10⁵ · 5,0·10⁻⁴ = 50 J; ΔU = 1,5·50 = 75 J ⟹ Q = 125 J."),
    ("Nhiệt độ khí khi pit-tông chạm vấu là 375 K, và nhiệt độ cuối cùng là 600 K.", True,
     "Đúng. Đẳng áp: T₂ = 300 · 25/20 = 375 K. Đẳng tích: T₃ = 375 · 1,6/1,0 = 600 K."),
    ("Tổng nhiệt lượng khí nhận được trong cả quá trình là 275 J.", False,
     "Sai. Chặng đẳng tích cần thêm Q = ΔU = 1,5 · 0,6·10⁵ · 2,5·10⁻³ = 225 J, nên tổng là "
     "125 + 225 = 350 J.")],
   "Quá trình hai chặng (C1 + C2)", RK, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông và vấu chặn"),

ds("Một lượng khí lí tưởng đơn nguyên tử biến đổi theo ĐOẠN THẲNG trên giản đồ (p, V) từ A(1 L; 4·10⁵ Pa) "
   "tới B(4 L; 1·10⁵ Pa). Cho U = (3/2)pV.",
   [("Nội năng của khí ở A và ở B bằng nhau và bằng 600 J.", True,
     "Đúng. U_A = 1,5 · 4·10⁵ · 1·10⁻³ = 600 J; U_B = 1,5 · 1·10⁵ · 4·10⁻³ = 600 J."),
    ("Công khí sinh ra trong quá trình là 750 J.", True,
     "Đúng. A′ = ½(4 + 1)·10⁵ · 3·10⁻³ = 750 J (diện tích hình thang dưới đoạn AB)."),
    ("Nhiệt lượng khí nhận được trong quá trình là 750 J.", True,
     "Đúng. ΔU = 0 ⟹ Q = A′ = 750 J."),
    ("Vì ΔU = 0 nên quá trình này là quá trình đẳng nhiệt.", False,
     "Sai. Đẳng nhiệt trên giản đồ (p, V) phải là nhánh HYPEBOL. Ở đây nhiệt độ tăng tới cực đại tại "
     "V = 2,5 L (khi đó pV = 625 J, U = 937,5 J) rồi giảm về đúng giá trị ban đầu.")],
   "Đường thẳng trên giản đồ p–V (C1 + C2)", RK),

ds("Một bình cứng 10 L chứa khí lí tưởng đơn nguyên tử ở 5,0·10⁵ Pa và 600 K, được làm lạnh đẳng tích "
   "xuống 300 K. Cho U = (3/2)pV, c_nước = 4200 J/(kg·K).",
   [("Nội năng ban đầu của khối khí là 7500 J.", True,
     "Đúng. U = 1,5 · 5,0·10⁵ · 10·10⁻³ = 7500 J."),
    ("Khí toả ra nhiệt lượng 3750 J.", True,
     "Đúng. T giảm một nửa nên U giảm một nửa: ΔU = −3750 J; đẳng tích nên Q = ΔU."),
    ("Áp suất khí sau khi làm lạnh là 2,5·10⁵ Pa.", True,
     "Đúng. Đẳng tích ⟹ p ∝ T ⟹ p₂ = 5,0·10⁵ · 300/600 = 2,5·10⁵ Pa."),
    ("Nhiệt lượng đó đủ để đun 1,0 kg nước nóng thêm 10 °C.", False,
     "Sai. Đun 1,0 kg nước nóng thêm 10 °C cần 42 000 J, lớn hơn nhiều so với 3750 J. Lượng nước đun được "
     "chỉ khoảng 89 g.")],
   "Nối khí – nhiệt (C1 + C2)", K),

ds("Xét ý nghĩa của việc nội năng là hàm trạng thái còn công và nhiệt lượng thì không.",
   [("Nếu hai quá trình khác nhau đưa khí từ cùng một trạng thái đầu tới cùng một trạng thái cuối thì ΔU "
     "của chúng bằng nhau.", True,
     "Đúng, đó chính là định nghĩa của hàm trạng thái."),
    ("Với hai quá trình đó, công và nhiệt lượng nói chung khác nhau.", True,
     "Đúng. Công bằng diện tích dưới đường biểu diễn, mà hai đường khác nhau có diện tích khác nhau; do "
     "Q = ΔU − A nên Q cũng khác nhau."),
    ("Một quá trình có ΔU = 0 thì nhiệt độ khí không đổi trong suốt quá trình.", False,
     "Sai. ΔU = 0 chỉ nói nhiệt độ ĐẦU bằng nhiệt độ CUỐI; ở giữa nhiệt độ vẫn có thể thay đổi (ví dụ "
     "quá trình theo đoạn thẳng AB ở trên)."),
    ("Muốn tính nhiệt lượng trao đổi trong một quá trình, phải biết cả đường đi của quá trình đó.", True,
     "Đúng. Q = ΔU − A mà A phụ thuộc đường đi trên giản đồ (p, V).")],
   "Hàm trạng thái (C1 + C2)", RK),
],
P3=[
sa("Xilanh thẳng đứng tiết diện 100 cm², cột khí đơn nguyên tử cao 20 cm ở 300 K và 1,0·10⁵ Pa, vấu chặn "
   "cách pit-tông 5 cm. Đun nóng tới khi áp suất đạt 1,6·10⁵ Pa. Tổng nhiệt lượng khí nhận được bằng bao "
   "nhiêu jun? Cho U = (3/2)pV.",
   "350",
   "Chặng 1 (đẳng áp): A′ = 1,0·10⁵ · 5,0·10⁻⁴ = 50 J; ΔU = 75 J ⟹ Q₁ = 125 J.\n"
   "Chặng 2 (đẳng tích, V = 2,5·10⁻³ m³): Q₂ = ΔU = 1,5 · 0,6·10⁵ · 2,5·10⁻³ = 225 J.\n"
   "Tổng Q = 125 + 225 = 350 J.",
   "Quá trình hai chặng (C1 + C2)", RK),

sa("Một lượng khí lí tưởng đơn nguyên tử biến đổi theo đoạn thẳng trên giản đồ (p, V) từ A(1 L; 4·10⁵ Pa) "
   "tới B(4 L; 1·10⁵ Pa). Nhiệt lượng khí nhận được bằng bao nhiêu jun?",
   "750",
   "A′ = ½(4 + 1)·10⁵ · 3·10⁻³ = 750 J; U_A = U_B = 600 J nên ΔU = 0 ⟹ Q = 750 J.",
   "Định luật I trên giản đồ p–V", RK),

sa("Vẫn với quá trình A → B đó, nội năng lớn nhất của khí bằng bao nhiêu jun (làm tròn đến chữ số thập "
   "phân thứ nhất)? Cho U = (3/2)pV.",
   "937,5",
   "Trên đoạn AB: p = (5 − V)·10⁵ Pa (V tính bằng L) ⟹ pV = V(5 − V)·10² J, cực đại tại V = 2,5 L:\n"
   "(pV)_max = 2,5·10⁵ · 2,5·10⁻³ = 625 J ⟹ U_max = 1,5 · 625 = 937,5 J.",
   "Suy luận trên giản đồ p–V (C1 + C2)", RK),

sa("Một bình cứng 10 L chứa khí lí tưởng đơn nguyên tử ở 5,0·10⁵ Pa và 600 K. Làm lạnh đẳng tích xuống "
   "300 K. Nhiệt lượng khí toả ra bằng bao nhiêu jun? Cho U = (3/2)pV.",
   "3750", "U₁ = 7500 J; U₂ = 3750 J (vì U ∝ T) ⟹ khí toả |ΔU| = 3750 J (đẳng tích nên A = 0).",
   "Nội năng – đẳng tích (C1 + C2)", K),

sa("Nhiệt lượng 3750 J có thể đun bao nhiêu gam nước nóng thêm 10 °C (làm tròn đến hàng đơn vị)? "
   "Cho c = 4200 J/(kg·K).",
   "89", "m = Q/(cΔt) = 3750/42 000 ≈ 0,0893 kg ≈ 89 g.", "Nối khí – nhiệt (C1 + C2)", K),

sa("Một lượng khí lí tưởng đơn nguyên tử ở 400 K có nội năng 1000 J. Làm lạnh đẳng tích xuống 250 K. "
   "Nhiệt lượng khí toả ra bằng bao nhiêu jun?",
   "375", "U₂ = 1000 · 250/400 = 625 J ⟹ |ΔU| = 375 J; đẳng tích nên Q = −375 J.",
   "Nội năng – đẳng tích (C1 + C2)", TB),
])


# =====================================================================
DE8 = dict(
ma="MIX-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Chu trình có chặng đẳng nhiệt; khinh khí cầu định lượng; hơi nước gặp nước đá",
P1=[
mc("Hình bên là chu trình A → B → C → A của khí lí tưởng đơn nguyên tử, với A(1 L; 4·10⁵ Pa), "
   "B(4 L; 1·10⁵ Pa), C(1 L; 1·10⁵ Pa); A → B là đẳng nhiệt. Nội năng của khí ở A và B",
   ["bằng nhau và bằng 600 J.", "bằng nhau và bằng 150 J.",
    "khác nhau, U_A lớn hơn.", "khác nhau, U_B lớn hơn."],
   "A",
   "A → B đẳng nhiệt nên U_A = U_B. Cụ thể U = (3/2)pV = 1,5 · 4·10⁵ · 1·10⁻³ = 600 J "
   "(kiểm tra tại B: 1,5 · 1·10⁵ · 4·10⁻³ = 600 J ✓).",
   "Nội năng – đẳng nhiệt (C1 + C2)", TB, fig="k_dt_chutrinh_dn",
   cap="Chu trình có một chặng đẳng nhiệt"),

mc("Vẫn với chu trình trên, trong chặng đẳng nhiệt A → B khí nhận nhiệt lượng 555 J. Công khí sinh ra "
   "trong chặng đó bằng",
   ["0 J.", "255 J.", "555 J.", "855 J."],
   "C", "Đẳng nhiệt ⟹ ΔU = 0 ⟹ A′ = Q = 555 J: toàn bộ nhiệt lượng biến thành công.",
   "Định luật I + đẳng nhiệt", TB, fig="k_dt_chutrinh_dn", cap="Chu trình có chặng đẳng nhiệt"),

mc("Vẫn với chu trình trên, trong chặng đẳng áp B → C khí",
   ["nhận công 300 J và toả nhiệt 750 J.", "nhận công 300 J và nhận nhiệt 750 J.",
    "sinh công 300 J và toả nhiệt 450 J.", "sinh công 400 J và toả nhiệt 850 J."],
   "A",
   "B → C: đẳng áp ở 1·10⁵ Pa, thể tích giảm từ 4 L xuống 1 L ⟹ khí NHẬN công "
   "A = 1·10⁵ · 3·10⁻³ = 300 J.\n"
   "U_C = 1,5 · 1·10⁵ · 1·10⁻³ = 150 J ⟹ ΔU = 150 − 600 = −450 J\n"
   "⟹ Q = ΔU − A = −450 − 300 = −750 J: khí toả 750 J.",
   "Định luật I + đẳng áp (C1 + C2)", K, fig="k_dt_chutrinh_dn",
   cap="Chu trình có chặng đẳng nhiệt"),

mc("Vẫn với chu trình trên, trong chặng đẳng tích C → A khí nhận nhiệt lượng",
   ["150 J.", "300 J.", "450 J.", "600 J."],
   "C", "Đẳng tích ⟹ A = 0 ⟹ Q = ΔU = U_A − U_C = 600 − 150 = 450 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB, fig="k_dt_chutrinh_dn",
   cap="Chu trình có chặng đẳng nhiệt"),

mc("Vẫn với chu trình trên, công khí sinh ra trong cả chu trình bằng",
   ["105 J.", "255 J.", "555 J.", "855 J."],
   "B",
   "A′_tổng = 555 (chặng A → B) − 300 (công nhận lại ở chặng B → C) − 0 (đẳng tích) = 255 J.\n"
   "Kiểm tra bằng nhiệt: Q_tổng = 555 − 750 + 450 = 255 J = A′_tổng ✓ (vì ΔU = 0 sau một chu trình).",
   "Công trong chu trình (C1 + C2)", K, fig="k_dt_chutrinh_dn",
   cap="Chu trình có chặng đẳng nhiệt"),

mc("Vẫn với chu trình trên, hiệu suất của chu trình gần nhất với",
   ["21,4%.", "25,4%.", "34,0%.", "45,9%."],
   "B",
   "Khí nhận nhiệt ở chặng A → B (555 J) và chặng C → A (450 J), tổng 1005 J.\n"
   "H = A′/Q_nhận = 255/1005 ≈ 0,254 = 25,4%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", K, fig="k_dt_chutrinh_dn",
   cap="Chu trình có chặng đẳng nhiệt"),

mc("Một khinh khí cầu thể tích 800 m³ có đáy hở, áp suất khí bên trong luôn bằng 10⁵ Pa. Không khí ngoài "
   "ở 27 °C. Đốt nóng khí trong cầu lên 127 °C. Cho M = 29 g/mol, R = 8,31 J/(mol·K), g = 10 m/s². "
   "Lực nâng của cầu gần nhất với",
   ["1160 N.", "1750 N.", "2326 N.", "2910 N."],
   "C",
   "ρ_ngoài = pM/(RT) = 2900/(8,31 · 300) ≈ 1,1633 kg/m³;\n"
   "ρ_trong = 2900/(8,31 · 400) ≈ 0,8725 kg/m³.\n"
   "F = (ρ_ngoài − ρ_trong)·V·g ≈ 0,2908 · 800 · 10 ≈ 2326 N.",
   "Khối lượng riêng – khinh khí cầu (C1 + C2)", RK, fig="k_sd_bongbay",
   cap="Khinh khí cầu có đáy hở"),

mc("Dẫn 30 g hơi nước ở 100 °C vào bình cách nhiệt chứa 300 g nước đá ở 0 °C. Cho L = 2,26·10⁶ J/kg, "
   "λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt là",
   ["0 °C.", "5,4 °C.", "12,8 °C.", "20,0 °C."],
   "A",
   "Hơi nước nhường tối đa: 0,030 · 2,26·10⁶ + 0,030 · 4200 · 100 = 67 800 + 12 600 = 80 400 J.\n"
   "Làm tan hết 300 g đá cần 0,300 · 3,4·10⁵ = 102 000 J > 80 400 J ⟹ đá chỉ tan một phần ⟹ hệ ở 0 °C.",
   "Cân bằng nhiệt nhiều giai đoạn", K),

mc("Với dữ kiện ở câu trên, khối lượng nước đá còn lại khi cân bằng nhiệt gần nhất với",
   ["36 g.", "64 g.", "128 g.", "237 g."],
   "B",
   "Khối lượng đá đã tan: Δm = 80 400/3,4·10⁵ ≈ 0,2365 kg ≈ 236,5 g.\n"
   "Đá còn lại: 300 − 236,5 ≈ 64 g. (237 g là phần đã tan, không phải phần còn lại.)",
   "Cân bằng nhiệt nhiều giai đoạn", K),

mc("Một lượng khí lí tưởng đơn nguyên tử ở 300 K có nội năng 600 J. Nếu đun đẳng áp tới 500 K thì nhiệt "
   "lượng khí nhận được là",
   ["400 J.", "667 J.", "1000 J.", "1200 J."],
   "B",
   "ΔU = 600 · (500 − 300)/300 = 400 J. Đẳng áp: Q = (5/3)·ΔU = (5/3) · 400 ≈ 667 J.\n"
   "(Vì Q/ΔU = 5/3 với khí đơn nguyên tử ở quá trình đẳng áp.)",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Trong quá trình đẳng nhiệt, đại lượng nào sau đây của khí lí tưởng KHÔNG đổi?",
   ["Áp suất.", "Thể tích.", "Nội năng.", "Mật độ phân tử."],
   "C", "Đẳng nhiệt ⟹ T không đổi ⟹ nội năng không đổi; ba đại lượng còn lại đều thay đổi.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Nhiệt lượng cần để đun 1,5 kg nước từ 20 °C lên 80 °C là (c = 4200 J/(kg·K))",
   ["252 kJ.", "378 kJ.", "504 kJ.", "630 kJ."],
   "B", "Q = 1,5 · 4200 · 60 = 378 000 J = 378 kJ.", "Nhiệt dung riêng", D),

mc("Muốn khí lí tưởng nhận nhiệt mà nội năng không tăng, quá trình phải có",
   ["thể tích không đổi.", "áp suất không đổi.",
    "khí sinh công đúng bằng nhiệt lượng nhận vào.", "khí bị nén."],
   "C", "ΔU = A + Q = 0 khi A = −Q, tức công khí sinh ra bằng đúng nhiệt lượng nhận vào (đẳng nhiệt).",
   "Định luật I nhiệt động lực học", TB),

mc("Một khối khí lí tưởng đơn nguyên tử có nội năng 1200 J ở áp suất 2,0·10⁵ Pa. Thể tích của khối khí là "
   "(U = (3/2)pV)",
   ["2,0 L.", "3,0 L.", "4,0 L.", "6,0 L."],
   "C", "V = 2U/(3p) = 2 · 1200/(3 · 2,0·10⁵) = 2400/6,0·10⁵ = 4,0·10⁻³ m³ = 4,0 L.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trong một chu trình, khí nhận 1005 J nhiệt và sinh công 255 J. Nhiệt lượng khí thải ra bằng",
   ["255 J.", "450 J.", "750 J.", "1260 J."],
   "C", "ΔU = 0 sau chu trình ⟹ Q_thải = Q_nhận − A′ = 1005 − 255 = 750 J.",
   "Định luật I – chu trình", TB),

mc("Vì sao trong chu trình có chặng đẳng nhiệt ở nhiệt độ cao, hiệu suất thường lớn hơn chu trình chỉ gồm "
   "các chặng đẳng áp – đẳng tích cùng giới hạn áp suất và thể tích?",
   ["Vì quá trình đẳng nhiệt không cần cung cấp nhiệt.",
    "Vì trong chặng đẳng nhiệt, toàn bộ nhiệt lượng nhận vào đều biến thành công.",
    "Vì đẳng nhiệt làm nhiệt độ khí tăng liên tục.",
    "Vì đẳng nhiệt không sinh công."],
   "B",
   "Ở chặng đẳng nhiệt ΔU = 0 nên A′ = Q: không có phần nhiệt lượng nào “bị giữ lại” trong nội năng. "
   "Đó là lí do các chu trình lí tưởng hiệu suất cao đều dùng chặng đẳng nhiệt.",
   "Hiệu suất – phân tích (C1 + C2)", RK),

mc("Một bình cách nhiệt chứa khí lí tưởng. Khuấy khí bằng một cánh quạt, thực hiện công 500 J lên khối "
   "khí. Nội năng và nhiệt độ khí lần lượt",
   ["giảm và giảm.", "tăng 500 J và tăng.", "không đổi và không đổi.", "tăng 500 J và không đổi."],
   "B", "Cách nhiệt ⟹ Q = 0 ⟹ ΔU = A = +500 J; nội năng tăng nên nhiệt độ cũng tăng.",
   "Định luật I – thực hiện công", TB),

mc("Nếu tăng nhiệt độ tuyệt đối của khí lí tưởng đơn nguyên tử lên 3 lần thì nội năng, áp suất (thể tích "
   "không đổi) và tốc độ căn quân phương lần lượt",
   ["tăng 3, 3 và 3 lần.", "tăng 3, 3 và √3 lần.",
    "tăng 3, 9 và √3 lần.", "tăng 9, 3 và 3 lần."],
   "B",
   "U ∝ T ⟹ 3 lần; p ∝ T (V không đổi) ⟹ 3 lần; v ∝ √T ⟹ √3 ≈ 1,73 lần.",
   "Nội năng – áp suất – tốc độ phân tử (C1 + C2)", K),
],
P2=[
ds("Chu trình A(1 L; 4·10⁵ Pa) → B(4 L; 1·10⁵ Pa) → C(1 L; 1·10⁵ Pa) → A của khí lí tưởng đơn nguyên tử; "
   "A → B là đẳng nhiệt và trong chặng đó khí nhận nhiệt lượng 555 J. Cho U = (3/2)pV.",
   [("Nội năng của khí ở A bằng nội năng ở B và bằng 600 J.", True,
     "Đúng. A → B đẳng nhiệt nên U không đổi; U = 1,5 · 4·10⁵ · 1·10⁻³ = 600 J."),
    ("Trong chặng A → B, khí sinh công 555 J.", True,
     "Đúng. ΔU = 0 ⟹ A′ = Q = 555 J."),
    ("Trong chặng B → C, khí nhận công 300 J và toả nhiệt 750 J.", True,
     "Đúng. A = 1·10⁵ · 3·10⁻³ = 300 J; ΔU = 150 − 600 = −450 J ⟹ Q = −450 − 300 = −750 J."),
    ("Hiệu suất của chu trình bằng 255/555 ≈ 45,9%.", False,
     "Sai ở mẫu số. Phải lấy TỔNG nhiệt lượng khí nhận vào, gồm cả chặng đẳng tích C → A (450 J): "
     "Q_nhận = 555 + 450 = 1005 J ⟹ H = 255/1005 ≈ 25,4%.")],
   "Chu trình có chặng đẳng nhiệt (C1 + C2)", RK,
   fig="k_dt_chutrinh_dn", cap="Chu trình có chặng đẳng nhiệt"),

ds("Dẫn 30 g hơi nước ở 100 °C vào bình cách nhiệt chứa 300 g nước đá ở 0 °C. Cho L = 2,26·10⁶ J/kg, "
   "λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng hơi nước nhường khi ngưng tụ hoàn toàn ở 100 °C là 67,8 kJ.", True,
     "Đúng. Q = Lm = 2,26·10⁶ · 0,030 = 67 800 J."),
    ("Tổng nhiệt lượng mà 30 g hơi nước có thể nhường cho nước đá là 80,4 kJ.", True,
     "Đúng. Ngoài 67,8 kJ khi ngưng tụ, phần nước tạo thành còn nguội từ 100 °C xuống 0 °C, toả thêm "
     "0,030 · 4200 · 100 = 12 600 J."),
    ("Toàn bộ 300 g nước đá sẽ tan hết.", False,
     "Sai. Tan hết 300 g đá cần 102 kJ > 80,4 kJ nên đá chỉ tan khoảng 236,5 g."),
    ("Khi cân bằng nhiệt, trong bình có khoảng 266 g nước ở thể lỏng.", True,
     "Đúng. Lượng đá tan ≈ 236,5 g cộng với 30 g nước do hơi ngưng tụ: 236,5 + 30 ≈ 266,5 g; phần còn "
     "lại khoảng 63,5 g vẫn là đá, tất cả ở 0 °C.")],
   "Cân bằng nhiệt nhiều giai đoạn", RK),

ds("Một khinh khí cầu thể tích 800 m³, đáy hở nên áp suất khí bên trong luôn bằng 10⁵ Pa; không khí ngoài "
   "ở 27 °C, khí trong cầu được đốt nóng lên 127 °C. Cho M = 29 g/mol, R = 8,31 J/(mol·K), g = 10 m/s².",
   [("Khối lượng riêng của không khí ngoài là khoảng 1,163 kg/m³.", True,
     "Đúng. ρ = pM/(RT) = 2900/(8,31 · 300) ≈ 1,163 kg/m³."),
    ("Khối lượng riêng của khí trong cầu là khoảng 0,873 kg/m³.", True,
     "Đúng. ρ = 2900/(8,31 · 400) ≈ 0,8725 kg/m³."),
    ("Lực nâng của cầu vào khoảng 2326 N, tương ứng nâng được khoảng 233 kg.", True,
     "Đúng. F = (1,163 − 0,873) · 800 · 10 ≈ 2326 N ⟹ m = F/g ≈ 233 kg."),
    ("Nếu đốt nóng khí trong cầu lên cao hơn nữa thì lực nâng tăng không giới hạn.", False,
     "Sai. Khi T → rất lớn thì ρ_trong → 0, lực nâng tiến tới giá trị giới hạn ρ_ngoài·V·g ≈ 9306 N và "
     "không thể vượt qua; ngoài ra vật liệu vỏ cầu cũng không chịu được nhiệt độ quá cao.")],
   "Khinh khí cầu (C1 + C2)", RK, fig="k_sd_bongbay", cap="Khinh khí cầu có đáy hở"),

ds("Xét vai trò của chặng đẳng nhiệt trong một chu trình nhiệt.",
   [("Trong chặng đẳng nhiệt, toàn bộ nhiệt lượng khí nhận vào đều biến thành công.", True,
     "Đúng. ΔU = 0 ⟹ A′ = Q."),
    ("Trong chặng đẳng tích, toàn bộ nhiệt lượng khí nhận vào đều biến thành nội năng.", True,
     "Đúng. A = 0 ⟹ ΔU = Q."),
    ("Trong chặng đẳng áp của khí đơn nguyên tử, 40% nhiệt lượng nhận vào biến thành công.", True,
     "Đúng. A′/Q = 1/(5/2) = 2/5 = 40%."),
    ("Vì trong chặng đẳng nhiệt nhiệt lượng biến hoàn toàn thành công nên một chu trình chỉ gồm các chặng "
     "đẳng nhiệt sẽ có hiệu suất 100%.", False,
     "Sai. Một chu trình KHÔNG THỂ chỉ gồm các chặng đẳng nhiệt ở cùng nhiệt độ (khi đó nó không khép "
     "kín được). Muốn khép kín phải có chặng ở nhiệt độ thấp hơn, và ở chặng đó khí buộc phải THẢI nhiệt.")],
   "Hiệu suất – phân tích (C1 + C2)", RK),
],
P3=[
sa("Với chu trình A(1 L; 4·10⁵ Pa) → B(4 L; 1·10⁵ Pa) → C(1 L; 1·10⁵ Pa) → A (A → B đẳng nhiệt, khí nhận "
   "555 J ở chặng này), công khí sinh ra trong cả chu trình bằng bao nhiêu jun?",
   "255",
   "Chặng A → B: A′ = Q = 555 J (vì ΔU = 0).\nChặng B → C: khí NHẬN công 1·10⁵ · 3·10⁻³ = 300 J.\n"
   "Chặng C → A: đẳng tích, A = 0.\nA′_tổng = 555 − 300 = 255 J.",
   "Công trong chu trình (C1 + C2)", K, fig="k_dt_chutrinh_dn", cap="Chu trình có chặng đẳng nhiệt"),

sa("Vẫn với chu trình đó, hiệu suất của chu trình bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "25,4", "Q_nhận = 555 (A → B) + 450 (C → A) = 1005 J ⟹ H = 255/1005 ≈ 25,4%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", RK, fig="k_dt_chutrinh_dn", cap="Chu trình có chặng đẳng nhiệt"),

sa("Dẫn 30 g hơi nước ở 100 °C vào bình cách nhiệt chứa 300 g nước đá ở 0 °C. Khối lượng nước đá còn lại "
   "khi cân bằng nhiệt bằng bao nhiêu gam (làm tròn đến hàng đơn vị)? Cho L = 2,26·10⁶ J/kg, "
   "λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "64",
   "Hơi nhường tối đa 0,030·2,26·10⁶ + 0,030·4200·100 = 80 400 J < 102 000 J ⟹ đá tan một phần.\n"
   "Δm = 80 400/3,4·10⁵ ≈ 236,5 g ⟹ còn lại 300 − 236,5 ≈ 64 g.",
   "Cân bằng nhiệt nhiều giai đoạn", K),

sa("Khinh khí cầu thể tích 800 m³, đáy hở, p = 10⁵ Pa; không khí ngoài 27 °C, khí trong cầu 127 °C. "
   "Cho M = 29 g/mol, R = 8,31 J/(mol·K), g = 10 m/s². Lực nâng của cầu bằng bao nhiêu niutơn (làm tròn "
   "đến hàng đơn vị)?",
   "2326",
   "ρ_ngoài = 2900/(8,31·300) ≈ 1,1633; ρ_trong = 2900/(8,31·400) ≈ 0,8725 kg/m³.\n"
   "F = (1,1633 − 0,8725) · 800 · 10 ≈ 2326 N.",
   "Khinh khí cầu (C1 + C2)", RK),

sa("Một lượng khí lí tưởng đơn nguyên tử ở 300 K có nội năng 600 J. Đun đẳng áp tới 500 K. Nhiệt lượng "
   "khí nhận được bằng bao nhiêu jun (làm tròn đến hàng đơn vị)?",
   "667", "ΔU = 600 · 200/300 = 400 J; đẳng áp ⟹ Q = (5/3)ΔU = 666,7 ≈ 667 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

sa("Một khối khí lí tưởng đơn nguyên tử có nội năng 1200 J ở áp suất 2,0·10⁵ Pa. Thể tích khối khí bằng "
   "bao nhiêu lít? Cho U = (3/2)pV.",
   "4", "V = 2U/(3p) = 2400/(6,0·10⁵) = 4,0·10⁻³ m³ = 4,0 L.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),
])


# =====================================================================
DE9 = dict(
ma="MIX-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Bài toán ngược với định luật I; nối kết năng lượng khí với quá trình chuyển thể",
P1=[
mc("Đun nóng đẳng áp 1,0 mol khí lí tưởng đơn nguyên tử ở 300 K, khí nhận nhiệt lượng 2077,5 J. Nhiệt độ "
   "cuối của khí là (R = 8,31 J/(mol·K))",
   ["350 K.", "400 K.", "450 K.", "500 K."],
   "B",
   "Đẳng áp với khí đơn nguyên tử: Q = ΔU + A′ = (3/2)nRΔT + nRΔT = (5/2)nRΔT.\n"
   "ΔT = 2Q/(5nR) = 2 · 2077,5/(5 · 1,0 · 8,31) = 4155/41,55 = 100 K ⟹ T₂ = 400 K.",
   "Định luật I – bài toán ngược (C1 + C2)", K),

mc("Vẫn với quá trình trên, công mà khí sinh ra bằng",
   ["415,5 J.", "831,0 J.", "1246,5 J.", "2077,5 J."],
   "B", "A′ = nRΔT = 1,0 · 8,31 · 100 = 831 J (chiếm 40% nhiệt lượng nhận vào).",
   "Công của khí (C1 + C2)", K),

mc("Vẫn với quá trình trên, độ tăng nội năng của khí bằng",
   ["415,5 J.", "831,0 J.", "1246,5 J.", "2077,5 J."],
   "C", "ΔU = (3/2)nRΔT = 1,5 · 831 = 1246,5 J (chiếm 60% nhiệt lượng nhận vào).",
   "Nội năng khí lí tưởng (C1 + C2)", K),

mc("Một bình cứng 20 L chứa khí lí tưởng đơn nguyên tử ở 6,0·10⁵ Pa và 600 K, được làm lạnh đẳng tích "
   "xuống 300 K. Nếu dùng toàn bộ nhiệt lượng toả ra để làm tan nước đá ở 0 °C thì khối lượng đá tan được "
   "gần nhất với (U = (3/2)pV, λ = 3,4·10⁵ J/kg)",
   ["13 g.", "26 g.", "40 g.", "53 g."],
   "B",
   "U₁ = 1,5 · 6,0·10⁵ · 20·10⁻³ = 18 000 J; nhiệt độ giảm một nửa nên U₂ = 9000 J.\n"
   "Đẳng tích ⟹ Q_toả = |ΔU| = 9000 J.\nm = Q/λ = 9000/3,4·10⁵ ≈ 0,0265 kg ≈ 26 g.",
   "Nối khí – chuyển thể (C1 + C2)", RK),

mc("Một khối khí lí tưởng đơn nguyên tử thực hiện quá trình trong đó nhiệt lượng nhận vào bằng đúng công "
   "sinh ra. Quá trình đó là",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "đoạn nhiệt."],
   "C", "Q = A′ ⟺ ΔU = 0 ⟺ nhiệt độ đầu bằng nhiệt độ cuối; với quá trình đơn giản đó là đẳng nhiệt.",
   "Định luật I – nhận dạng quá trình", TB),

mc("Một khối khí nhận nhiệt lượng Q và sinh công A′ = 0,4Q. Khí đó thực hiện quá trình",
   ["đẳng tích.", "đẳng áp (khí đơn nguyên tử).", "đẳng nhiệt.", "trong bình cách nhiệt."],
   "B",
   "Với khí lí tưởng đơn nguyên tử trong quá trình đẳng áp: A′/Q = nRΔT/((5/2)nRΔT) = 2/5 = 0,4.",
   "Định luật I – nhận dạng quá trình (C1 + C2)", K),

mc("Trong bình cách nhiệt chứa 0,50 kg nước ở 30 °C, người ta nhúng vào một bình kim loại nhỏ chứa khí "
   "lí tưởng đơn nguyên tử (thể tích khí 5,0 L, áp suất 4,0·10⁵ Pa, nhiệt độ 600 K). Bỏ qua nhiệt dung "
   "của bình kim loại. Khi khí nguội tới 300 K (đẳng tích), nhiệt độ nước tăng thêm gần nhất với "
   "(U = (3/2)pV, c_nước = 4200 J/(kg·K))",
   ["0,7 °C.", "1,4 °C.", "2,1 °C.", "3,6 °C."],
   "A",
   "U₁ = 1,5 · 4,0·10⁵ · 5,0·10⁻³ = 3000 J; nhiệt độ giảm một nửa nên U₂ = 1500 J.\n"
   "Bình kim loại cứng ⟹ đẳng tích ⟹ A = 0 ⟹ nhiệt lượng khí toả ra Q = |ΔU| = 1500 J.\n"
   "Toàn bộ nhiệt lượng đó truyền cho nước: Δt = Q/(m·c) = 1500/(0,50 · 4200) ≈ 0,7 °C.\n"
   "Nhận xét: một bình khí nén ở 600 K cũng chỉ đủ hâm nửa lít nước lên chưa tới 1 °C — năng lượng "
   "chứa trong khí nhỏ hơn nhiều so với cảm nhận thông thường.",
   "Nối khí – nhiệt (C1 + C2)", RK),

mc("Một lượng khí lí tưởng đơn nguyên tử biến đổi sao cho nội năng tăng 900 J trong khi khí nhận công "
   "400 J. Nhiệt lượng khí nhận được bằng",
   ["500 J.", "900 J.", "1300 J.", "1700 J."],
   "A", "ΔU = A + Q ⟹ 900 = 400 + Q ⟹ Q = 500 J.", "Định luật I nhiệt động lực học", TB),

mc("Một chu trình có Q_nhận = 1200 J và hiệu suất 25%. Nhiệt lượng thải ra cho nguồn lạnh là",
   ["300 J.", "600 J.", "900 J.", "1200 J."],
   "C", "A′ = 0,25 · 1200 = 300 J ⟹ Q_thải = 1200 − 300 = 900 J.",
   "Hiệu suất động cơ nhiệt", TB),

mc("Một lượng khí lí tưởng đơn nguyên tử ở 300 K, áp suất 2,0·10⁵ Pa, thể tích 3,0 L. Nếu vừa đun tới "
   "450 K vừa giữ áp suất không đổi thì nhiệt lượng khí nhận được là (U = (3/2)pV)",
   ["300 J.", "450 J.", "750 J.", "1200 J."],
   "C",
   "Đẳng áp ⟹ V₂ = V₁·T₂/T₁ = 3,0 · 450/300 = 4,5 L, tức ΔV = 1,5 L.\n"
   "A′ = p·ΔV = 2,0·10⁵ · 1,5·10⁻³ = 300 J.\n"
   "ΔU = (3/2)·p·ΔV = 1,5 · 300 = 450 J.\n"
   "Q = ΔU + A′ = 450 + 300 = 750 J (cũng bằng (5/2)p·ΔV).\n"
   "Bẫy: dừng ở 300 J (chỉ công) hoặc 450 J (chỉ nội năng).",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Thả 0,25 kg nước đá ở 0 °C vào 0,60 kg nước ở 40 °C trong bình cách nhiệt. Cho λ = 3,4·10⁵ J/kg, "
   "c = 4200 J/(kg·K). Nhiệt độ khi cân bằng gần nhất với",
   ["0 °C.", "4,4 °C.", "6,3 °C.", "9,5 °C."],
   "B",
   "Nước nhường tối đa 0,60 · 4200 · 40 = 100 800 J, lớn hơn 85 000 J cần để tan hết đá ⟹ đá tan hết.\n"
   "85 000 + 0,25 · 4200 · t = 0,60 · 4200 · (40 − t)\n"
   "⟹ 85 000 + 1050t = 100 800 − 2520t ⟹ 3570t = 15 800 ⟹ t ≈ 4,4 °C.\n"
   "Bẫy: quên rằng phần nước mới tan (0,25 kg ở 0 °C) cũng phải được đun lên nhiệt độ cuối sẽ cho "
   "t ≈ 6,3 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

mc("Muốn một khối khí lí tưởng có nội năng giảm mà vẫn nhận nhiệt, quá trình phải thoả mãn",
   ["A > 0 và |A| > Q.", "A < 0 và |A| > Q.", "A = 0.", "Q < 0."],
   "B",
   "Nhận nhiệt nghĩa là Q > 0; muốn ΔU = A + Q < 0 thì A phải âm (khí sinh công) và có độ lớn lớn hơn Q.",
   "Định luật I – phân tích tình huống", K),

mc("Đun nóng đẳng tích 2,0 mol khí lí tưởng đơn nguyên tử từ 300 K lên 400 K. Nhiệt lượng khí nhận được "
   "gần nhất với (R = 8,31 J/(mol·K))",
   ["1247 J.", "1662 J.", "2493 J.", "4155 J."],
   "C", "Đẳng tích ⟹ Q = ΔU = (3/2)nRΔT = 1,5 · 2,0 · 8,31 · 100 = 2493 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

mc("Một lượng khí lí tưởng có nội năng 1500 J. Nếu nội năng của nó giảm 20% thì nhiệt độ tuyệt đối",
   ["giảm 20%.", "giảm 25%.", "giảm 40%.", "không đổi."],
   "A", "U ∝ T nên U giảm 20% thì T cũng giảm 20%.", "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Nhiệt lượng cần để làm nóng chảy hoàn toàn 0,15 kg nước đá ở 0 °C bằng công mà một khối khí sinh ra "
   "khi giãn nở đẳng áp ở 2,0·10⁵ Pa. Độ tăng thể tích của khối khí là (λ = 3,4·10⁵ J/kg)",
   ["0,17 L.", "0,26 L.", "255 L.", "0,34 L."],
   "C",
   "Q = λm = 3,4·10⁵ · 0,15 = 51 000 J.\n"
   "ΔV = A′/p = 51 000/2,0·10⁵ = 0,255 m³ = 255 L.\n"
   "Con số này cho thấy muốn sinh một công lớn bằng cơ chế giãn nở khí thì cần thể tích rất lớn.",
   "Nối khí – chuyển thể (C1 + C2)", RK),

mc("Trong quá trình nào sau đây của khí lí tưởng, tỉ số Q/ΔU KHÔNG xác định được nếu chỉ biết loại quá trình?",
   ["Đẳng tích.", "Đẳng áp.", "Đẳng nhiệt.", "Cả ba đều xác định được."],
   "C",
   "Đẳng tích: Q/ΔU = 1. Đẳng áp (đơn nguyên tử): Q/ΔU = 5/3. Đẳng nhiệt: ΔU = 0 nên tỉ số Q/ΔU không "
   "xác định (chia cho 0).",
   "Định luật I – phân tích", K),

mc("Một khối khí lí tưởng đơn nguyên tử ở 400 K có nội năng U. Nếu vừa tăng nhiệt độ lên 600 K vừa tăng "
   "số mol lên gấp đôi thì nội năng trở thành",
   ["1,5U.", "2U.", "3U.", "4U."],
   "C", "U = (3/2)nRT tỉ lệ thuận với tích n·T: (2) · (600/400) = 3 ⟹ nội năng bằng 3U.",
   "Nội năng khí lí tưởng (C1 + C2)", K),

mc("Trong một chu trình, khí sinh công 400 J. Nếu hiệu suất là 20% thì nhiệt lượng khí nhận được từ "
   "nguồn nóng là",
   ["500 J.", "800 J.", "2000 J.", "2400 J."],
   "C", "H = A′/Q_nhận ⟹ Q_nhận = A′/H = 400/0,20 = 2000 J.",
   "Hiệu suất động cơ nhiệt", TB),
],
P2=[
ds("Đun nóng đẳng áp 1,0 mol khí lí tưởng đơn nguyên tử từ 300 K; khí nhận nhiệt lượng 2077,5 J. "
   "Cho R = 8,31 J/(mol·K).",
   [("Nhiệt độ cuối của khí là 400 K.", True,
     "Đúng. Q = (5/2)nRΔT ⟹ ΔT = 2 · 2077,5/(5 · 8,31) = 100 K ⟹ T₂ = 400 K."),
    ("Công khí sinh ra là 831 J và độ tăng nội năng là 1246,5 J.", True,
     "Đúng. A′ = nRΔT = 831 J; ΔU = 1,5 · 831 = 1246,5 J; tổng đúng bằng 2077,5 J."),
    ("Trong quá trình này, 40% nhiệt lượng nhận vào biến thành công.", True,
     "Đúng. 831/2077,5 = 0,4 = 40%; phần còn lại 60% làm tăng nội năng."),
    ("Nếu đun cùng khối khí đó từ 300 K lên 400 K nhưng giữ thể tích không đổi thì cũng cần 2077,5 J.", False,
     "Sai. Đẳng tích thì A = 0 nên chỉ cần Q = ΔU = 1246,5 J — ít hơn đúng phần công 831 J.")],
   "Định luật I – bài toán ngược (C1 + C2)", K),

ds("Một bình cứng 20 L chứa khí lí tưởng đơn nguyên tử ở 6,0·10⁵ Pa và 600 K, được làm lạnh đẳng tích "
   "xuống 300 K. Cho U = (3/2)pV, λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nội năng ban đầu của khối khí là 18 000 J.", True,
     "Đúng. U = 1,5 · 6,0·10⁵ · 20·10⁻³ = 18 000 J."),
    ("Nhiệt lượng khí toả ra là 9000 J.", True,
     "Đúng. Nhiệt độ giảm một nửa nên U giảm một nửa; đẳng tích nên Q = ΔU = −9000 J."),
    ("Nhiệt lượng đó đủ làm tan khoảng 26 g nước đá ở 0 °C.", True,
     "Đúng. m = 9000/3,4·10⁵ ≈ 0,0265 kg ≈ 26 g."),
    ("Nhiệt lượng đó cũng đủ đun 1,0 kg nước nóng thêm 10 °C.", False,
     "Sai. Đun 1,0 kg nước nóng thêm 10 °C cần 42 000 J, lớn hơn nhiều so với 9000 J (chỉ đun được "
     "khoảng 214 g nước).")],
   "Nối khí – chuyển thể (C1 + C2)", RK),

ds("Xét việc nhận dạng quá trình của khí lí tưởng đơn nguyên tử từ tỉ lệ giữa Q, ΔU và A′.",
   [("Nếu Q = ΔU thì quá trình là đẳng tích.", True,
     "Đúng. Q = ΔU ⟺ A = 0 ⟺ thể tích không đổi."),
    ("Nếu A′ = Q thì quá trình có nhiệt độ đầu bằng nhiệt độ cuối.", True,
     "Đúng. A′ = Q ⟺ ΔU = 0 ⟺ T đầu = T cuối."),
    ("Nếu A′ = 0,4Q thì quá trình là đẳng áp.", True,
     "Đúng. Với khí đơn nguyên tử, quá trình đẳng áp cho A′/Q = 2/5 = 0,4."),
    ("Trong mọi quá trình, tỉ số Q/ΔU đều xác định được khi biết loại quá trình.", False,
     "Sai. Với quá trình đẳng nhiệt, ΔU = 0 nên tỉ số Q/ΔU không xác định.")],
   "Định luật I – nhận dạng quá trình", K),

ds("Thả 0,25 kg nước đá ở 0 °C vào 0,60 kg nước ở 40 °C trong bình cách nhiệt lí tưởng. "
   "Cho λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng lớn nhất mà nước có thể nhường là 100,8 kJ.", True,
     "Đúng. Q = 0,60 · 4200 · 40 = 100 800 J."),
    ("Nhiệt lượng cần để làm tan hết 0,25 kg nước đá là 85 kJ.", True,
     "Đúng. Q = λm = 3,4·10⁵ · 0,25 = 85 000 J."),
    ("Toàn bộ nước đá tan hết và nhiệt độ cân bằng cao hơn 0 °C.", True,
     "Đúng. 100,8 kJ > 85 kJ nên đá tan hết và vẫn còn dư nhiệt để nâng nhiệt độ hỗn hợp."),
    ("Nhiệt độ khi cân bằng nhiệt vào khoảng 8,8 °C.", False,
     "Sai. 85 000 + 1050t = 100 800 − 2520t ⟹ 3570t = 15 800 ⟹ t ≈ 4,4 °C, chứ không phải 8,8 °C "
     "(giá trị 8,8 °C là kết quả khi quên phần nước mới tan cũng phải nóng lên).")],
   "Cân bằng nhiệt có chuyển thể", K),
],
P3=[
sa("Đun nóng đẳng áp 1,0 mol khí lí tưởng đơn nguyên tử từ 300 K, khí nhận 2077,5 J. Nhiệt độ cuối của "
   "khí bằng bao nhiêu kelvin? Cho R = 8,31 J/(mol·K).",
   "400", "Q = (5/2)nRΔT ⟹ ΔT = 2 · 2077,5/(5 · 8,31) = 100 K ⟹ T₂ = 400 K.",
   "Định luật I – bài toán ngược (C1 + C2)", K),

sa("Một bình cứng 20 L chứa khí lí tưởng đơn nguyên tử ở 6,0·10⁵ Pa và 600 K, làm lạnh đẳng tích xuống "
   "300 K. Khối lượng nước đá ở 0 °C có thể làm tan bằng nhiệt lượng toả ra là bao nhiêu gam (làm tròn "
   "đến hàng đơn vị)? Cho U = (3/2)pV, λ = 3,4·10⁵ J/kg.",
   "26", "U₁ = 18 000 J ⟹ Q_toả = 9000 J ⟹ m = 9000/3,4·10⁵ ≈ 0,0265 kg ≈ 26 g.",
   "Nối khí – chuyển thể (C1 + C2)", RK),

sa("Thả 0,25 kg nước đá ở 0 °C vào 0,60 kg nước ở 40 °C trong bình cách nhiệt. Nhiệt độ khi cân bằng bằng "
   "bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "4,4",
   "Đá tan hết (85 kJ < 100,8 kJ).\n85 000 + 1050t = 100 800 − 2520t ⟹ 3570t = 15 800 ⟹ t ≈ 4,4 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

sa("Đun nóng đẳng tích 2,0 mol khí lí tưởng đơn nguyên tử từ 300 K lên 400 K. Nhiệt lượng khí nhận được "
   "bằng bao nhiêu jun (làm tròn đến hàng đơn vị)? Cho R = 8,31 J/(mol·K).",
   "2493", "Đẳng tích ⟹ Q = ΔU = 1,5 · 2,0 · 8,31 · 100 = 2493 J.",
   "Định luật I + đẳng tích (C1 + C2)", TB),

sa("Một chu trình có nhiệt lượng nhận vào 1200 J và hiệu suất 25%. Nhiệt lượng thải ra cho nguồn lạnh "
   "bằng bao nhiêu jun?",
   "900", "A′ = 0,25 · 1200 = 300 J ⟹ Q_thải = 1200 − 300 = 900 J.",
   "Hiệu suất động cơ nhiệt", TB),

sa("Nhiệt lượng cần để làm nóng chảy hoàn toàn 0,15 kg nước đá ở 0 °C bằng công mà khối khí sinh ra khi "
   "giãn nở đẳng áp ở 2,0·10⁵ Pa. Độ tăng thể tích của khối khí bằng bao nhiêu lít? "
   "Cho λ = 3,4·10⁵ J/kg.",
   "255", "Q = λm = 51 000 J ⟹ ΔV = A′/p = 51 000/2,0·10⁵ = 0,255 m³ = 255 L.",
   "Nối khí – chuyển thể (C1 + C2)", RK),
])


# =====================================================================
DE10 = dict(
ma="MIX-Đ10", ten="ĐỀ SỐ 10", muc="Khó / thử thách",
trongtam="Chu trình có chặng xiên; hiệu suất; biện luận trạng thái và bài toán ngược nhiều bước",
P1=[
mc("Hình bên là chu trình A → B → C → A của khí lí tưởng đơn nguyên tử, với A(1 L; 1·10⁵ Pa), "
   "B(3 L; 3·10⁵ Pa), C(3 L; 1·10⁵ Pa); A → B là một ĐOẠN THẲNG. Công khí sinh ra trong chặng A → B bằng",
   ["200 J.", "300 J.", "400 J.", "600 J."],
   "C",
   "Công bằng diện tích hình thang dưới đoạn AB:\n"
   "A′ = ½(p_A + p_B)·ΔV = ½(1 + 3)·10⁵ · 2·10⁻³ = ½ · 4·10⁵ · 2·10⁻³ = 400 J.",
   "Công của khí trên giản đồ p–V", K, fig="k_dt_chutrinh_xien",
   cap="Chu trình có một chặng xiên A → B"),

mc("Vẫn với chu trình trên, nhiệt lượng khí nhận được trong chặng A → B bằng (U = (3/2)pV)",
   ["400 J.", "1200 J.", "1600 J.", "2000 J."],
   "C",
   "U_A = 1,5 · 1·10⁵ · 1·10⁻³ = 150 J; U_B = 1,5 · 3·10⁵ · 3·10⁻³ = 1350 J ⟹ ΔU = 1200 J.\n"
   "Q = ΔU + A′ = 1200 + 400 = 1600 J.",
   "Định luật I trên giản đồ p–V (C1 + C2)", RK, fig="k_dt_chutrinh_xien",
   cap="Chu trình có chặng xiên"),

mc("Vẫn với chu trình trên, trạng thái nào có nhiệt độ cao nhất?",
   ["Trạng thái A.", "Trạng thái B.", "Trạng thái C.", "Một điểm nằm giữa A và B."],
   "B",
   "T ∝ pV. Trên đoạn AB có p = V (đơn vị 10⁵ Pa và L) nên pV = V², tăng đơn điệu ⟹ cực đại tại B.\n"
   "(pV)_A = 1; (pV)_B = 9; (pV)_C = 3 ⟹ B có nhiệt độ cao nhất.",
   "Biện luận trên giản đồ p–V", RK, fig="k_dt_chutrinh_xien",
   cap="Chu trình có chặng xiên"),

mc("Vẫn với chu trình trên, công khí sinh ra trong cả chu trình bằng",
   ["100 J.", "200 J.", "400 J.", "600 J."],
   "B",
   "A′_tổng = 400 (chặng A → B) − 200 (công khí nhận lại ở chặng đẳng áp C → A) − 0 (đẳng tích B → C) "
   "= 200 J.\nĐây cũng là diện tích tam giác ABC: ½ · 2·10⁻³ · 2·10⁵ = 200 J.",
   "Công trong chu trình", K, fig="k_dt_chutrinh_xien", cap="Chu trình có chặng xiên"),

mc("Vẫn với chu trình trên, hiệu suất của chu trình bằng",
   ["8,3%.", "12,5%.", "20,0%.", "25,0%."],
   "B",
   "Khí chỉ nhận nhiệt ở chặng A → B (1600 J); hai chặng còn lại đều toả nhiệt (900 J và 500 J).\n"
   "H = A′/Q_nhận = 200/1600 = 0,125 = 12,5%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", RK, fig="k_dt_chutrinh_xien",
   cap="Chu trình có chặng xiên"),

mc("Vẫn với chu trình trên, tổng nhiệt lượng khí toả ra bằng",
   ["500 J.", "900 J.", "1400 J.", "1600 J."],
   "C",
   "B → C (đẳng tích): Q = ΔU = 450 − 1350 = −900 J.\n"
   "C → A (đẳng áp, bị nén): A = 1·10⁵ · 2·10⁻³ = 200 J; ΔU = 150 − 450 = −300 J ⟹ Q = −500 J.\n"
   "Tổng toả: 900 + 500 = 1400 J (= 1600 − 200 ✓).",
   "Định luật I – chu trình (C1 + C2)", K, fig="k_dt_chutrinh_xien",
   cap="Chu trình có chặng xiên"),

mc("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử, khí nhận nhiệt lượng Q và thể tích tăng thêm "
   "ΔV ở áp suất p. Hệ thức nào sau đây đúng?",
   ["Q = p·ΔV.", "Q = (3/2)p·ΔV.", "Q = (5/2)p·ΔV.", "Q = 3p·ΔV."],
   "C",
   "A′ = p·ΔV; ΔU = (3/2)p·ΔV (vì ΔU = (3/2)Δ(pV) và p không đổi).\n"
   "Q = ΔU + A′ = (5/2)p·ΔV.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Dùng nhiệt lượng toả ra khi làm nguội đẳng tích một khối khí lí tưởng đơn nguyên tử (thể tích 25 L, "
   "áp suất giảm từ 8,0·10⁵ Pa xuống 2,0·10⁵ Pa) để làm bay hơi nước ở 100 °C. Khối lượng nước bay hơi "
   "gần nhất với (U = (3/2)pV, L = 2,26·10⁶ J/kg)",
   ["4,5 g.", "10,0 g.", "22,5 g.", "45,0 g."],
   "B",
   "Q_toả = |ΔU| = 1,5 · Δp · V = 1,5 · 6,0·10⁵ · 25·10⁻³ = 1,5 · 15 000 = 22 500 J.\n"
   "m = Q/L = 22 500/2,26·10⁶ ≈ 0,00996 kg ≈ 10,0 g.",
   "Nối khí – chuyển thể (C1 + C2)", RK),

mc("Một lượng khí lí tưởng đơn nguyên tử thực hiện quá trình trong đó nhiệt độ tăng gấp đôi và khí sinh "
   "công 600 J. Nếu nội năng ban đầu là 900 J thì nhiệt lượng khí nhận được là",
   ["600 J.", "900 J.", "1500 J.", "2400 J."],
   "C",
   "Nhiệt độ tăng gấp đôi ⟹ U₂ = 2U₁ = 1800 J ⟹ ΔU = 900 J.\nQ = ΔU + A′ = 900 + 600 = 1500 J.",
   "Định luật I – bài toán ngược (C1 + C2)", K),

mc("Trong bình cách nhiệt có 0,40 kg nước ở 10 °C. Người ta thả vào 0,10 kg nước đá ở −20 °C. Cho "
   "c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg. Trạng thái cuối của hệ là",
   ["hỗn hợp nước và nước đá ở 0 °C.", "nước ở khoảng 1,3 °C.",
    "nước ở khoảng 3,6 °C.", "nước đá ở dưới 0 °C."],
   "A",
   "Bước 1 – nước nhường tối đa: Q = 0,40 · 4200 · 10 = 16 800 J (khi hạ tới 0 °C).\n"
   "Bước 2 – hâm khối đá từ −20 °C lên 0 °C cần 0,10 · 2100 · 20 = 4200 J; phần nhiệt còn lại là "
   "16 800 − 4200 = 12 600 J.\n"
   "Bước 3 – muốn tan hết 0,10 kg đá cần 34 000 J, lớn hơn 12 600 J ⟹ đá chỉ tan khoảng "
   "12 600/3,4·10⁵ ≈ 37 g.\n"
   "Trong bình còn cả nước và nước đá nên nhiệt độ cân bằng đúng bằng 0 °C.",
   "Cân bằng nhiệt – biện luận", RK),

mc("Nếu một khối khí lí tưởng thực hiện quá trình mà tích pV không đổi thì",
   ["nội năng khí tăng.", "nội năng khí giảm.",
    "nội năng khí không đổi và Q = A′.", "khí không trao đổi nhiệt."],
   "C",
   "pV không đổi ⟹ T không đổi ⟹ ΔU = 0 ⟹ Q = −A = A′: nhiệt lượng nhận vào bằng đúng công sinh ra.",
   "Định luật I + đẳng nhiệt", TB),

mc("Một chu trình gồm ba chặng, khí nhận nhiệt ở một chặng (Q₁) và toả nhiệt ở hai chặng còn lại "
   "(Q₂, Q₃). Hiệu suất của chu trình bằng",
   ["(Q₁ − Q₂ − Q₃)/Q₁.", "(Q₁ + Q₂ + Q₃)/Q₁.", "Q₁/(Q₂ + Q₃).", "(Q₂ + Q₃)/Q₁."],
   "A",
   "A′ = Q₁ − (Q₂ + Q₃) với Q₂, Q₃ là độ lớn nhiệt lượng toả ra.\nH = A′/Q₁ = (Q₁ − Q₂ − Q₃)/Q₁.",
   "Hiệu suất động cơ nhiệt", K),

mc("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử ở 2,5·10⁵ Pa, thể tích tăng từ 2,0 L lên 5,0 L. "
   "Nhiệt lượng khí nhận được bằng",
   ["750 J.", "1125 J.", "1875 J.", "2250 J."],
   "C", "Q = (5/2)p·ΔV = 2,5 · 2,5·10⁵ · 3,0·10⁻³ = 2,5 · 750 = 1875 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

mc("Một lượng khí lí tưởng đơn nguyên tử có nội năng 1800 J, thể tích 6,0 L. Áp suất khí bằng "
   "(U = (3/2)pV)",
   ["1,0·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa.", "4,5·10⁵ Pa."],
   "B", "p = 2U/(3V) = 2 · 1800/(3 · 6,0·10⁻³) = 3600/0,018 = 2,0·10⁵ Pa.",
   "Nội năng khí lí tưởng (C1 + C2)", TB),

mc("Trong một quá trình, khí lí tưởng có nội năng không đổi nhưng nhiệt độ ở giữa quá trình lại thay đổi. "
   "Điều này chứng tỏ",
   ["quá trình đó là đẳng nhiệt.",
    "nhiệt độ đầu và nhiệt độ cuối bằng nhau nhưng quá trình không đẳng nhiệt.",
    "khí không trao đổi nhiệt.", "khí không sinh công."],
   "B",
   "ΔU = 0 chỉ so sánh hai đầu mút. Ví dụ điển hình là quá trình theo đoạn thẳng trên giản đồ (p, V) nối "
   "hai điểm cùng nằm trên một đường đẳng nhiệt: nhiệt độ tăng rồi giảm về giá trị cũ.",
   "Hàm trạng thái – phân biệt (C1 + C2)", RK),

mc("Muốn tăng hiệu suất của một chu trình nhiệt, biện pháp nào sau đây là hợp lí?",
   ["Tăng nhiệt lượng thải cho nguồn lạnh.",
    "Giảm phần nhiệt lượng bị thải ra ở các chặng toả nhiệt.",
    "Giảm công mà khí sinh ra.", "Tăng số chặng đẳng tích trong chu trình."],
   "B",
   "H = 1 − Q_thải/Q_nhận, nên giảm Q_thải (với Q_nhận không đổi) sẽ làm hiệu suất tăng. Đây là lí do "
   "các chu trình thực tế đều cố gắng hạ nhiệt độ nguồn lạnh và giảm tổn hao.",
   "Hiệu suất động cơ nhiệt", K),

mc("Một bình 10 L chứa khí lí tưởng đơn nguyên tử ở 300 K và 3,0·10⁵ Pa. Nếu vừa đun tới 450 K vừa cho "
   "khí giãn tới 20 L thì nội năng khí thay đổi thế nào? (U = (3/2)pV)",
   ["Không đổi.", "Tăng 2250 J.", "Tăng 4500 J.", "Giảm 2250 J."],
   "B",
   "U₁ = 1,5 · 3,0·10⁵ · 10·10⁻³ = 4500 J.\n"
   "Nội năng tỉ lệ thuận với nhiệt độ: U₂ = 4500 · 450/300 = 6750 J ⟹ ΔU = 2250 J.\n"
   "(Không cần biết áp suất cuối; chỉ cần biết nhiệt độ.)",
   "Nội năng khí lí tưởng (C1 + C2)", K),

mc("Trong bốn nhận định sau về một chu trình kín của khí lí tưởng, nhận định nào SAI?",
   ["Tổng độ biến thiên nội năng bằng 0.",
    "Tổng công khí sinh ra bằng tổng nhiệt lượng khí nhận được (kể cả dấu).",
    "Diện tích hình mà chu trình bao quanh trên giản đồ (p, V) bằng công của cả chu trình.",
    "Khí có thể biến toàn bộ nhiệt lượng nhận được từ nguồn nóng thành công."],
   "D",
   "Ba nhận định đầu đều đúng. Nhận định cuối sai: mọi chu trình đều phải có ít nhất một chặng toả nhiệt "
   "(nếu không chu trình không khép kín được), nên hiệu suất luôn nhỏ hơn 100%.",
   "Định luật I – chu trình", RK),
],
P2=[
ds("Chu trình A(1 L; 1·10⁵ Pa) → B(3 L; 3·10⁵ Pa) → C(3 L; 1·10⁵ Pa) → A của khí lí tưởng đơn nguyên tử, "
   "trong đó A → B là một đoạn thẳng. Cho U = (3/2)pV.",
   [("Công khí sinh ra trong chặng A → B là 400 J.", True,
     "Đúng. A′ = ½(1 + 3)·10⁵ · 2·10⁻³ = 400 J (diện tích hình thang)."),
    ("Nhiệt lượng khí nhận được trong chặng A → B là 1600 J.", True,
     "Đúng. ΔU = 1350 − 150 = 1200 J ⟹ Q = 1200 + 400 = 1600 J."),
    ("Trạng thái có nhiệt độ cao nhất trong chu trình là trạng thái C.", False,
     "Sai. T ∝ pV: (pV)_A = 1; (pV)_B = 9; (pV)_C = 3 (đơn vị 10⁵ Pa·L). Trạng thái B mới có nhiệt độ "
     "cao nhất."),
    ("Hiệu suất của chu trình bằng 12,5%.", True,
     "Đúng. Khí chỉ nhận nhiệt ở chặng A → B (1600 J); A′_tổng = 400 − 200 = 200 J ⟹ H = 200/1600 = 12,5%.")],
   "Chu trình có chặng xiên (C1 + C2)", RK,
   fig="k_dt_chutrinh_xien", cap="Chu trình có chặng xiên A → B"),

ds("Trong bình cách nhiệt có 0,40 kg nước ở 10 °C; thả vào 0,10 kg nước đá ở −20 °C. Cho c_đá = 2100, "
   "c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng lớn nhất mà nước có thể nhường là 16,8 kJ.", True,
     "Đúng. Q = 0,40 · 4200 · 10 = 16 800 J (khi nước hạ tới 0 °C)."),
    ("Nhiệt lượng cần để hâm khối nước đá từ −20 °C lên 0 °C là 4,2 kJ.", True,
     "Đúng. Q = 0,10 · 2100 · 20 = 4200 J."),
    ("Toàn bộ nước đá sẽ tan hết.", False,
     "Sai. Sau khi hâm đá lên 0 °C, phần nhiệt còn lại chỉ là 16 800 − 4200 = 12 600 J, làm tan được "
     "12 600/3,4·10⁵ ≈ 37 g trong tổng số 100 g đá."),
    ("Nhiệt độ khi cân bằng nhiệt bằng 0 °C và trong bình còn khoảng 63 g nước đá.", True,
     "Đúng. Còn cả nước và đá nên nhiệt độ đúng bằng 0 °C; đá còn lại 100 − 37 = 63 g.")],
   "Cân bằng nhiệt – biện luận nhiều bước", RK),

ds("Xét việc dùng năng lượng của khí để thực hiện các quá trình chuyển thể. "
   "Cho U = (3/2)pV, λ = 3,4·10⁵ J/kg, L = 2,26·10⁶ J/kg.",
   [("Làm nguội đẳng tích 25 L khí lí tưởng đơn nguyên tử từ 8,0·10⁵ Pa xuống 2,0·10⁵ Pa thì khí toả "
     "22,5 kJ.", True,
     "Đúng. Q = |ΔU| = 1,5 · (8,0 − 2,0)·10⁵ · 25·10⁻³ = 22 500 J."),
    ("Nhiệt lượng đó đủ làm bay hơi khoảng 10 g nước ở 100 °C.", True,
     "Đúng. m = 22 500/2,26·10⁶ ≈ 0,00996 kg ≈ 10 g."),
    ("Cũng nhiệt lượng đó có thể làm tan khoảng 66 g nước đá ở 0 °C.", True,
     "Đúng. m = 22 500/3,4·10⁵ ≈ 0,0662 kg ≈ 66 g. Làm tan đá “rẻ” hơn làm bay hơi nước khoảng 6,6 lần."),
    ("Vì nhiệt hoá hơi riêng lớn hơn nhiệt nóng chảy riêng nên cùng một nhiệt lượng sẽ làm bay hơi được "
     "nhiều nước hơn là làm tan đá.", False,
     "Sai, ngược lại. L lớn hơn λ nghĩa là mỗi kilôgam nước cần NHIỀU năng lượng hơn để bay hơi, nên "
     "cùng một nhiệt lượng chỉ làm bay hơi được ÍT nước hơn (10 g so với 66 g).")],
   "Nối khí – chuyển thể (C1 + C2)", RK),

ds("Xét các giới hạn cơ bản của một chu trình nhiệt.",
   [("Trong một chu trình kín, tổng độ biến thiên nội năng luôn bằng 0.", True,
     "Đúng, vì nội năng là hàm trạng thái và khí trở về đúng trạng thái ban đầu."),
    ("Diện tích hình mà chu trình bao quanh trên giản đồ (p, V) bằng công mà khí sinh ra trong cả chu "
     "trình.", True,
     "Đúng, với chu trình đi theo chiều kim đồng hồ. Nếu đi ngược chiều kim đồng hồ thì đó là công mà "
     "khí NHẬN (chu trình của máy lạnh)."),
    ("Hiệu suất của chu trình bằng tỉ số giữa công sinh ra và tổng nhiệt lượng khí nhận vào ở các chặng "
     "nhận nhiệt.", True,
     "Đúng, đó là định nghĩa H = A′/Q_nhận."),
    ("Có thể thiết kế một chu trình trong đó khí chỉ nhận nhiệt mà không toả nhiệt ở bất kì chặng nào.", False,
     "Sai. Nếu chỉ nhận nhiệt thì nhiệt độ (và tích pV) chỉ có thể tăng, chu trình không thể quay lại "
     "trạng thái ban đầu. Mọi chu trình đều bắt buộc có chặng toả nhiệt, do đó hiệu suất luôn < 100%.")],
   "Định luật I – chu trình", RK),
],
P3=[
sa("Với chu trình A(1 L; 1·10⁵ Pa) → B(3 L; 3·10⁵ Pa) → C(3 L; 1·10⁵ Pa) → A (A → B là đoạn thẳng), "
   "nhiệt lượng khí nhận được trong chặng A → B bằng bao nhiêu jun? Cho U = (3/2)pV.",
   "1600",
   "A′ = ½(1 + 3)·10⁵ · 2·10⁻³ = 400 J; ΔU = 1350 − 150 = 1200 J ⟹ Q = 1600 J.",
   "Định luật I trên giản đồ p–V", RK, fig="k_dt_chutrinh_xien", cap="Chu trình có chặng xiên"),

sa("Vẫn với chu trình đó, hiệu suất của chu trình bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "12,5", "A′_tổng = 400 − 200 = 200 J; Q_nhận = 1600 J ⟹ H = 200/1600 = 12,5%.",
   "Hiệu suất động cơ nhiệt (C1 + C2)", RK, fig="k_dt_chutrinh_xien", cap="Chu trình có chặng xiên"),

sa("Làm nguội đẳng tích 25 L khí lí tưởng đơn nguyên tử từ 8,0·10⁵ Pa xuống 2,0·10⁵ Pa. Khối lượng nước "
   "ở 100 °C có thể làm bay hơi bằng nhiệt lượng toả ra là bao nhiêu gam (làm tròn đến hàng đơn vị)? "
   "Cho U = (3/2)pV, L = 2,26·10⁶ J/kg.",
   "10",
   "Q = 1,5 · 6,0·10⁵ · 25·10⁻³ = 22 500 J ⟹ m = 22 500/2,26·10⁶ ≈ 0,00996 kg ≈ 10 g.",
   "Nối khí – chuyển thể (C1 + C2)", RK),

sa("Trong bình cách nhiệt có 0,40 kg nước ở 10 °C; thả vào 0,10 kg nước đá ở −20 °C. Khối lượng nước đá "
   "còn lại khi cân bằng nhiệt bằng bao nhiêu gam (làm tròn đến hàng đơn vị)? Cho c_đá = 2100, "
   "c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   "63",
   "Nước nhường tối đa 16 800 J; hâm đá lên 0 °C mất 4200 J, còn 12 600 J.\n"
   "Đá tan: 12 600/3,4·10⁵ ≈ 37 g ⟹ còn lại 100 − 37 = 63 g (hệ ở 0 °C).",
   "Cân bằng nhiệt – biện luận nhiều bước", RK),

sa("Đun nóng đẳng áp một lượng khí lí tưởng đơn nguyên tử ở 2,5·10⁵ Pa, thể tích tăng từ 2,0 L lên 5,0 L. "
   "Nhiệt lượng khí nhận được bằng bao nhiêu jun?",
   "1875", "Q = (5/2)p·ΔV = 2,5 · 2,5·10⁵ · 3,0·10⁻³ = 1875 J.",
   "Định luật I + đẳng áp (C1 + C2)", K),

sa("Một bình 10 L chứa khí lí tưởng đơn nguyên tử ở 300 K và 3,0·10⁵ Pa. Vừa đun tới 450 K vừa cho khí "
   "giãn tới 20 L. Nội năng khí tăng bao nhiêu jun? Cho U = (3/2)pV.",
   "2250",
   "U₁ = 1,5 · 3,0·10⁵ · 10·10⁻³ = 4500 J. Nội năng tỉ lệ thuận với nhiệt độ nên "
   "U₂ = 4500 · 450/300 = 6750 J ⟹ ΔU = 2250 J.",
   "Nội năng khí lí tưởng (C1 + C2)", K),
])


NHOM = dict(
    ten_nhom="LỚP 12 – ĐỀ TỔNG HỢP CHƯƠNG 1 + CHƯƠNG 2",
    mo_ta="Bộ 10 đề tổng hợp, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó / thử thách)",
    pham_vi=(
        "CHƯƠNG 1 – VẬT LÍ NHIỆT: cấu trúc chất và sự chuyển thể; nội năng và định luật I nhiệt động lực "
        "học; nhiệt độ và thang nhiệt độ; nhiệt dung riêng, nhiệt nóng chảy riêng, nhiệt hoá hơi riêng.\n"
        "CHƯƠNG 2 – KHÍ LÍ TƯỞNG: mô hình động học phân tử chất khí; định luật Boyle, định luật Charles; "
        "phương trình trạng thái và phương trình Clapeyron; áp suất khí và động năng phân tử.\n"
        "Điểm nối hai chương được khai thác xuyên suốt: U = (3/2)nRT = (3/2)pV cho khí lí tưởng đơn "
        "nguyên tử; công của khí A′ = p·ΔV (đẳng áp) hoặc bằng diện tích dưới đường biểu diễn trên giản "
        "đồ (p, V); ΔU = A + Q; hiệu suất chu trình H = A′/Q_nhận."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
