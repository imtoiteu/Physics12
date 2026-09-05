# -*- coding: utf-8 -*-
"""LỚP 11 – CHƯƠNG 1: DAO ĐỘNG.  10 đề, độ khó tăng dần.

Công thức dùng thống nhất:
  x = A·cos(ωt + φ);  v = −ωA·sin(ωt + φ);  a = −ω²A·cos(ωt + φ) = −ω²x
  ω = 2π/T = 2πf;  v_max = ωA;  a_max = ω²A;  A² = x² + v²/ω²
  W = ½mω²A² = ½kA²;  Wt = ½mω²x²;  Wđ = ½mv²
  Con lắc lò xo: ω = √(k/m), T = 2π√(m/k);  Con lắc đơn: T = 2π√(ℓ/g)
"""
from de_12c1 import mc, ds, sa, D, TB, K, RK


# =====================================================================
DE1 = dict(
ma="11C1-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Khái niệm dao động điều hoà, các đại lượng đặc trưng và công thức cơ bản",
P1=[
mc("Dao động điều hoà là dao động trong đó li độ của vật là một hàm",
   ["bậc nhất của thời gian.", "bậc hai của thời gian.",
    "côsin (hay sin) của thời gian.", "mũ của thời gian."],
   "C",
   "Định nghĩa: dao động điều hoà là dao động trong đó li độ của vật biến thiên theo hàm côsin (hoặc sin) "
   "của thời gian: x = A·cos(ωt + φ).",
   "Định nghĩa dao động điều hoà", D),

mc("Trong phương trình dao động điều hoà x = A·cos(ωt + φ), đại lượng A được gọi là",
   ["li độ.", "biên độ.", "pha ban đầu.", "tần số góc."],
   "B", "A là biên độ — giá trị lớn nhất của độ lớn li độ; (ωt + φ) là pha, φ là pha ban đầu.",
   "Các đại lượng đặc trưng", D),

mc("Chu kì của dao động điều hoà là",
   ["số dao động toàn phần thực hiện trong 1 giây.",
    "khoảng thời gian vật thực hiện một dao động toàn phần.",
    "quãng đường vật đi được trong một dao động.",
    "li độ lớn nhất của vật."],
   "B", "Chu kì T là thời gian thực hiện một dao động toàn phần; tần số f = 1/T là số dao động trong 1 s.",
   "Các đại lượng đặc trưng", D),

mc("Mối liên hệ giữa tần số góc ω, chu kì T và tần số f là",
   ["ω = 2πT.", "ω = 2π/T = 2πf.", "ω = T/(2π).", "ω = f/(2π)."],
   "B", "ω = 2π/T = 2πf, đơn vị rad/s.", "Các đại lượng đặc trưng", D),

mc("Một vật dao động điều hoà với phương trình x = 5cos(4πt) cm (t tính bằng s). Biên độ dao động là",
   ["4 cm.", "5 cm.", "4π cm.", "10 cm."],
   "B", "So sánh với x = A·cos(ωt + φ) ⟹ A = 5 cm.", "Đọc phương trình dao động", D),

mc("Vẫn với dao động ở câu trên, chu kì dao động là",
   ["0,25 s.", "0,50 s.", "2,00 s.", "4,00 s."],
   "B", "ω = 4π rad/s ⟹ T = 2π/ω = 2π/(4π) = 0,50 s.", "Đọc phương trình dao động", D),

mc("Vẫn với dao động đó, tần số dao động là",
   ["0,5 Hz.", "1,0 Hz.", "2,0 Hz.", "4,0 Hz."],
   "C", "f = 1/T = 1/0,50 = 2,0 Hz (hoặc f = ω/(2π) = 4π/(2π) = 2 Hz).",
   "Đọc phương trình dao động", D),

mc("Vận tốc của vật dao động điều hoà đạt giá trị cực đại khi vật ở",
   ["vị trí biên.", "vị trí cân bằng.", "li độ bằng nửa biên độ.", "li độ bất kì."],
   "B",
   "v = −ωA·sin(ωt + φ) có độ lớn cực đại ωA khi sin = ±1, tức khi x = 0 — vị trí cân bằng. "
   "Ở vị trí biên vận tốc bằng 0.",
   "Vận tốc trong dao động điều hoà", D),

mc("Gia tốc của vật dao động điều hoà đạt độ lớn cực đại khi vật ở",
   ["vị trí cân bằng.", "vị trí biên.", "li độ bằng nửa biên độ.", "mọi vị trí như nhau."],
   "B", "a = −ω²x nên |a| cực đại khi |x| cực đại, tức tại vị trí biên; ở vị trí cân bằng a = 0.",
   "Gia tốc trong dao động điều hoà", D),

mc("Trong dao động điều hoà, gia tốc và li độ liên hệ với nhau bởi hệ thức",
   ["a = ω²x.", "a = −ω²x.", "a = −ωx.", "a = ω²x²."],
   "B",
   "a = −ω²x: gia tốc luôn ngược dấu với li độ (luôn hướng về vị trí cân bằng) và tỉ lệ với độ lớn li độ.",
   "Gia tốc trong dao động điều hoà", D),

mc("Một vật dao động điều hoà với biên độ 4 cm và tần số góc 10 rad/s. Tốc độ cực đại của vật là",
   ["0,4 m/s.", "0,8 m/s.", "4,0 m/s.", "40 m/s."],
   "A", "v_max = ωA = 10 · 0,04 = 0,4 m/s.", "Vận tốc trong dao động điều hoà", D),

mc("Vẫn với vật ở câu trên, gia tốc cực đại của vật là",
   ["0,4 m/s².", "4,0 m/s².", "40 m/s².", "400 m/s²."],
   "B", "a_max = ω²A = 10² · 0,04 = 100 · 0,04 = 4,0 m/s².",
   "Gia tốc trong dao động điều hoà", D),

mc("Cơ năng của một vật dao động điều hoà",
   ["biến thiên tuần hoàn theo thời gian.", "được bảo toàn (không đổi) nếu bỏ qua ma sát.",
    "bằng động năng của vật ở vị trí biên.", "tỉ lệ thuận với biên độ."],
   "B",
   "Nếu bỏ qua ma sát, cơ năng W = Wđ + Wt được bảo toàn. Cơ năng tỉ lệ với BÌNH PHƯƠNG biên độ "
   "(W = ½mω²A²), không phải tỉ lệ thuận với A.",
   "Năng lượng trong dao động điều hoà", D),

mc("Trong dao động điều hoà của con lắc lò xo, động năng của vật đạt cực đại khi vật ở",
   ["vị trí biên dương.", "vị trí biên âm.", "vị trí cân bằng.", "li độ bằng nửa biên độ."],
   "C", "Wđ = ½mv² cực đại khi tốc độ cực đại, tức khi vật qua vị trí cân bằng.",
   "Năng lượng trong dao động điều hoà", D),

mc("Chu kì dao động của con lắc lò xo được tính bằng công thức",
   ["T = 2π√(k/m).", "T = 2π√(m/k).", "T = 2π√(ℓ/g).", "T = 2π√(g/ℓ)."],
   "B", "T = 2π√(m/k); công thức T = 2π√(ℓ/g) là của con lắc đơn.",
   "Con lắc lò xo", D, fig="d_sd_loxo_ngang", cap="Con lắc lò xo nằm ngang"),

mc("Chu kì dao động nhỏ của con lắc đơn được tính bằng công thức",
   ["T = 2π√(ℓ/g).", "T = 2π√(g/ℓ).", "T = 2π√(m/k).", "T = 2π√(m/g)."],
   "A",
   "T = 2π√(ℓ/g) — chu kì con lắc đơn KHÔNG phụ thuộc khối lượng vật nặng, chỉ phụ thuộc chiều dài dây "
   "và gia tốc trọng trường.",
   "Con lắc đơn", D, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Dao động tắt dần là dao động có",
   ["biên độ giảm dần theo thời gian.", "chu kì giảm dần theo thời gian.",
    "tần số tăng dần theo thời gian.", "biên độ không đổi."],
   "A",
   "Do lực cản của môi trường, cơ năng của hệ giảm dần nên biên độ giảm dần. Chu kì gần như không đổi "
   "khi lực cản nhỏ.",
   "Dao động tắt dần", D, fig="d_dt_tatdan", cap="Đồ thị li độ của dao động tắt dần"),

mc("Hiện tượng cộng hưởng cơ xảy ra khi",
   ["biên độ ngoại lực rất lớn.",
    "tần số của lực cưỡng bức bằng tần số dao động riêng của hệ.",
    "lực cản của môi trường bằng không.",
    "hệ dao động tự do."],
   "B",
   "Cộng hưởng xảy ra khi f = f₀ (tần số lực cưỡng bức bằng tần số riêng); khi đó biên độ dao động cưỡng "
   "bức đạt cực đại. Lực cản càng nhỏ, đỉnh cộng hưởng càng nhọn và cao.",
   "Hiện tượng cộng hưởng", D, fig="d_dt_conghuong",
   cap="Đường cộng hưởng ứng với hai mức ma sát khác nhau"),
],
P2=[
ds("Một vật dao động điều hoà với phương trình x = 5cos(4πt) cm (t tính bằng s).",
   [("Biên độ dao động của vật là 5 cm.", True,
     "Đúng. So sánh với x = A·cos(ωt + φ) ta được A = 5 cm."),
    ("Tần số góc của dao động là 4π rad/s và chu kì là 0,5 s.", True,
     "Đúng. ω = 4π rad/s ⟹ T = 2π/ω = 0,5 s."),
    ("Pha ban đầu của dao động bằng π/2 rad.", False,
     "Sai. Phương trình không có số hạng cộng thêm trong ngoặc nên φ = 0. Điều đó cũng có nghĩa tại "
     "t = 0 vật ở đúng biên dương x = +5 cm."),
    ("Tốc độ cực đại của vật là 20π cm/s.", True,
     "Đúng. v_max = ωA = 4π · 5 = 20π cm/s ≈ 62,8 cm/s.")],
   "Đọc phương trình dao động", D),

ds("Xét các đại lượng đặc trưng của dao động điều hoà.",
   [("Chu kì và tần số là hai đại lượng nghịch đảo của nhau.", True,
     "Đúng. f = 1/T; nếu T tính bằng giây thì f tính bằng héc."),
    ("Gia tốc của vật luôn hướng về vị trí cân bằng.", True,
     "Đúng. a = −ω²x nên a luôn ngược dấu với x, tức luôn hướng về gốc toạ độ (vị trí cân bằng)."),
    ("Ở vị trí biên, cả vận tốc và gia tốc của vật đều bằng không.", False,
     "Sai. Ở vị trí biên vận tốc bằng 0 nhưng gia tốc có ĐỘ LỚN CỰC ĐẠI (a_max = ω²A). Ngược lại, ở vị "
     "trí cân bằng thì gia tốc bằng 0 còn tốc độ cực đại."),
    ("Tốc độ cực đại của vật bằng ωA và gia tốc cực đại bằng ω²A.", True,
     "Đúng, suy ra trực tiếp từ v = −ωA·sin(ωt + φ) và a = −ω²A·cos(ωt + φ).")],
   "Vận tốc – gia tốc trong dao động điều hoà", TB),

ds("Xét năng lượng của một vật dao động điều hoà (bỏ qua ma sát).",
   [("Cơ năng của vật được bảo toàn trong suốt quá trình dao động.", True,
     "Đúng. Khi bỏ qua ma sát, W = Wđ + Wt = ½mω²A² không đổi."),
    ("Động năng cực đại khi vật qua vị trí cân bằng và bằng 0 ở vị trí biên.", True,
     "Đúng. Wđ = ½mv² mà tốc độ cực đại ở vị trí cân bằng và bằng 0 ở biên."),
    ("Thế năng cực đại ở vị trí biên và bằng cơ năng của vật.", True,
     "Đúng. Ở biên động năng bằng 0 nên toàn bộ cơ năng ở dạng thế năng."),
    ("Cơ năng của vật tỉ lệ thuận với biên độ dao động.", False,
     "Sai. W = ½mω²A² tỉ lệ với BÌNH PHƯƠNG biên độ: tăng biên độ gấp đôi thì cơ năng tăng gấp bốn.")],
   "Năng lượng trong dao động điều hoà", TB,
   fig="d_dt_nangluong_x", cap="Động năng và thế năng theo li độ"),

ds("Xét dao động tắt dần, dao động cưỡng bức và hiện tượng cộng hưởng.",
   [("Dao động tắt dần có biên độ giảm dần vì cơ năng của hệ giảm dần do lực cản.", True,
     "Đúng. Công của lực cản luôn âm nên cơ năng giảm, kéo theo biên độ giảm."),
    ("Trong dao động cưỡng bức ổn định, tần số dao động của vật bằng tần số của lực cưỡng bức.", True,
     "Đúng. Sau giai đoạn chuyển tiếp, hệ dao động với đúng tần số của ngoại lực, không phải tần số riêng."),
    ("Cộng hưởng xảy ra khi tần số của lực cưỡng bức bằng tần số dao động riêng của hệ.", True,
     "Đúng. Khi f = f₀, biên độ dao động cưỡng bức đạt giá trị cực đại."),
    ("Cộng hưởng luôn là hiện tượng có hại nên phải tránh trong mọi trường hợp.", False,
     "Sai. Cộng hưởng có thể có hại (làm gãy cầu, hỏng máy) nhưng cũng rất có lợi: hộp cộng hưởng của đàn "
     "ghi ta, lò vi sóng, mạch chọn sóng của radio đều hoạt động nhờ cộng hưởng.")],
   "Dao động tắt dần – cưỡng bức – cộng hưởng", TB,
   fig="d_dt_conghuong", cap="Đường cộng hưởng"),
],
P3=[
sa("Một vật dao động điều hoà với phương trình x = 6cos(5πt) cm. Biên độ dao động bằng bao nhiêu "
   "xentimét?",
   "6", "So sánh với x = A·cos(ωt + φ) ⟹ A = 6 cm.", "Đọc phương trình dao động", D),

sa("Một vật dao động điều hoà với tần số góc 4π rad/s. Chu kì dao động bằng bao nhiêu giây "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "0,5", "T = 2π/ω = 2π/(4π) = 0,5 s.", "Các đại lượng đặc trưng", D),

sa("Một vật dao động điều hoà với biên độ 5 cm và tần số góc 20 rad/s. Tốc độ cực đại của vật bằng bao "
   "nhiêu mét trên giây?",
   "1", "v_max = ωA = 20 · 0,05 = 1,0 m/s.", "Vận tốc trong dao động điều hoà", D),

sa("Vẫn với vật ở câu trên, gia tốc cực đại của vật bằng bao nhiêu mét trên giây bình phương?",
   "20", "a_max = ω²A = 20² · 0,05 = 400 · 0,05 = 20 m/s².",
   "Gia tốc trong dao động điều hoà", D),

sa("Một con lắc lò xo gồm lò xo có độ cứng 40 N/m và vật nặng khối lượng 0,10 kg. Tần số góc của dao "
   "động bằng bao nhiêu rad/s?",
   "20", "ω = √(k/m) = √(40/0,10) = √400 = 20 rad/s.", "Con lắc lò xo", TB,
   fig="d_sd_loxo_ngang", cap="Con lắc lò xo nằm ngang"),

sa("Một con lắc đơn có chiều dài dây 1,0 m dao động nhỏ tại nơi có g = 9,8 m/s². Chu kì dao động bằng bao "
   "nhiêu giây (làm tròn đến chữ số thập phân thứ nhất)?",
   "2,0", "T = 2π√(ℓ/g) = 2π√(1,0/9,8) = 2π · 0,3194 ≈ 2,0 s.", "Con lắc đơn", TB,
   fig="d_sd_cldon", cap="Con lắc đơn"),
])


# =====================================================================
DE2 = dict(
ma="11C1-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Đọc đồ thị li độ – thời gian và viết phương trình dao động điều hoà",
P1=[
mc("Hình bên là đồ thị li độ theo thời gian của một vật dao động điều hoà. Biên độ dao động của vật là",
   ["2 cm.", "4 cm.", "8 cm.", "0,4 cm."],
   "B", "Giá trị lớn nhất của li độ đọc trên trục tung là 4 cm ⟹ A = 4 cm.",
   "Đọc đồ thị li độ – thời gian", D, fig="d_dt_xt",
   cap="Đồ thị li độ theo thời gian của một vật dao động điều hoà"),

mc("Vẫn với đồ thị trên, chu kì dao động của vật là",
   ["0,2 s.", "0,4 s.", "0,8 s.", "1,0 s."],
   "B",
   "Đồ thị lặp lại sau mỗi 0,4 s (từ đỉnh này tới đỉnh kế tiếp) ⟹ T = 0,4 s.",
   "Đọc đồ thị li độ – thời gian", D, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Vẫn với đồ thị trên, tần số góc của dao động là",
   ["2,5π rad/s.", "5π rad/s.", "10π rad/s.", "0,4π rad/s."],
   "B", "ω = 2π/T = 2π/0,4 = 5π rad/s ≈ 15,7 rad/s.",
   "Đọc đồ thị li độ – thời gian", D, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Vẫn với đồ thị trên, tại thời điểm t = 0 vật ở",
   ["vị trí cân bằng.", "biên dương.", "biên âm.", "li độ bằng nửa biên độ."],
   "B", "Đồ thị bắt đầu ở giá trị lớn nhất x = +4 cm ⟹ vật ở biên dương, pha ban đầu φ = 0.",
   "Đọc đồ thị li độ – thời gian", D, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Phương trình dao động ứng với đồ thị trên là",
   ["x = 4cos(5πt) cm.", "x = 4cos(5πt + π/2) cm.",
    "x = 4cos(2,5πt) cm.", "x = 8cos(5πt) cm."],
   "A", "A = 4 cm, ω = 5π rad/s, φ = 0 (vì t = 0 vật ở biên dương) ⟹ x = 4cos(5πt) cm.",
   "Viết phương trình dao động", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Một vật dao động điều hoà có đồ thị li độ như hình bên (đồ thị thứ hai). Pha ban đầu của dao động là",
   ["0.", "π/2 rad.", "−π/2 rad.", "π rad."],
   "C",
   "Tại t = 0 vật ở vị trí cân bằng (x = 0) và đang chuyển động theo chiều dương (li độ tăng lên ngay sau "
   "đó). Với x = A·cos(ωt + φ), điều kiện đó cho cos φ = 0 và sin φ < 0 ⟹ φ = −π/2 rad.",
   "Xác định pha ban đầu", TB, fig="d_dt_xt2",
   cap="Đồ thị li độ của một dao động khác"),

mc("Vẫn với đồ thị thứ hai, biên độ và chu kì dao động lần lượt là",
   ["4 cm và 0,4 s.", "5 cm và 0,6 s.", "5 cm và 1,2 s.", "2,5 cm và 0,6 s."],
   "B", "Giá trị cực đại của li độ là 5 cm; đồ thị lặp lại sau 0,6 s ⟹ A = 5 cm, T = 0,6 s.",
   "Đọc đồ thị li độ – thời gian", D, fig="d_dt_xt2", cap="Đồ thị li độ theo thời gian"),

mc("Hai dao động điều hoà cùng chu kì có đồ thị li độ như hình bên. Nhận xét nào ĐÚNG?",
   ["Hai dao động cùng pha.", "Hai dao động ngược pha.",
    "Dao động (2) trễ pha π/2 so với dao động (1).",
    "Dao động (2) sớm pha π/2 so với dao động (1)."],
   "C",
   "Dao động (1) đạt cực đại tại t = 0; dao động (2) đạt cực đại muộn hơn một phần tư chu kì "
   "(tại t = 0,1 s). Trễ một phần tư chu kì tương ứng với trễ pha π/2.",
   "Độ lệch pha", TB, fig="d_dt_lechpha",
   cap="Hai dao động cùng chu kì lệch pha nhau"),

mc("Một vật dao động điều hoà với chu kì 0,4 s. Trong 2,0 giây vật thực hiện được",
   ["2 dao động.", "4 dao động.", "5 dao động.", "8 dao động."],
   "C", "Số dao động = t/T = 2,0/0,4 = 5 dao động toàn phần.", "Chu kì – tần số", D),

mc("Một vật dao động điều hoà thực hiện 30 dao động trong 12 giây. Chu kì dao động là",
   ["0,25 s.", "0,40 s.", "2,50 s.", "0,60 s."],
   "B", "T = t/N = 12/30 = 0,40 s (tần số f = 2,5 Hz).", "Chu kì – tần số", D),

mc("Trong một chu kì dao động điều hoà, quãng đường vật đi được bằng",
   ["A.", "2A.", "3A.", "4A."],
   "D", "Trong một chu kì vật đi từ biên này sang biên kia rồi quay lại: tổng cộng 4 lần biên độ.",
   "Quãng đường trong dao động điều hoà", D),

mc("Một vật dao động điều hoà với biên độ 6 cm. Trong nửa chu kì, quãng đường vật đi được là",
   ["6 cm.", "12 cm.", "18 cm.", "24 cm."],
   "B", "Nửa chu kì ⟹ quãng đường bằng 2A = 2 · 6 = 12 cm.",
   "Quãng đường trong dao động điều hoà", D),

mc("Vật dao động điều hoà đi từ vị trí cân bằng ra biên mất khoảng thời gian ngắn nhất bằng",
   ["T/8.", "T/4.", "T/2.", "T."],
   "B", "Từ vị trí cân bằng ra biên là một phần tư chu kì.",
   "Thời gian trong dao động điều hoà", D),

mc("Một vật dao động điều hoà với phương trình x = 3cos(10t + π/3) cm. Li độ của vật tại t = 0 là",
   ["3,0 cm.", "1,5 cm.", "2,6 cm.", "0 cm."],
   "B", "x(0) = 3cos(π/3) = 3 · 0,5 = 1,5 cm.", "Đọc phương trình dao động", TB),

mc("Đại lượng nào sau đây KHÔNG thay đổi khi ta thay đổi biên độ dao động của một con lắc lò xo (giữ "
   "nguyên lò xo và vật nặng)?",
   ["Cơ năng.", "Tốc độ cực đại.", "Gia tốc cực đại.", "Chu kì dao động."],
   "D",
   "T = 2π√(m/k) chỉ phụ thuộc khối lượng và độ cứng, không phụ thuộc biên độ. Ba đại lượng còn lại đều "
   "phụ thuộc A.",
   "Con lắc lò xo", TB, fig="d_sd_loxo_ngang", cap="Con lắc lò xo nằm ngang"),

mc("Chu kì dao động nhỏ của con lắc đơn KHÔNG phụ thuộc vào",
   ["chiều dài dây treo.", "gia tốc trọng trường tại nơi treo con lắc.",
    "khối lượng vật nặng.", "vị trí địa lí nơi đặt con lắc."],
   "C",
   "T = 2π√(ℓ/g) không chứa khối lượng m. (Vị trí địa lí có ảnh hưởng vì g thay đổi theo vĩ độ và độ cao.)",
   "Con lắc đơn", TB, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Một con lắc đơn dao động nhỏ với chu kì 2,0 s. Nếu tăng chiều dài dây lên 4 lần thì chu kì trở thành",
   ["1,0 s.", "2,0 s.", "4,0 s.", "8,0 s."],
   "C", "T ∝ √ℓ ⟹ chiều dài tăng 4 lần thì chu kì tăng √4 = 2 lần: T = 4,0 s.",
   "Con lắc đơn", TB),

mc("Trong dao động điều hoà, vận tốc và li độ",
   ["luôn cùng dấu.", "luôn ngược dấu.",
    "vuông pha với nhau (lệch pha π/2).", "cùng pha với nhau."],
   "C",
   "x = A·cos(ωt + φ) còn v = −ωA·sin(ωt + φ) = ωA·cos(ωt + φ + π/2): vận tốc sớm pha π/2 so với li độ.",
   "Độ lệch pha giữa x, v, a", TB, fig="d_dt_xva",
   cap="Đồ thị li độ, vận tốc và gia tốc của cùng một dao động"),
],
P2=[
ds("Hình bên là đồ thị li độ theo thời gian của một vật dao động điều hoà.",
   [("Biên độ dao động của vật là 4 cm.", True,
     "Đúng. Giá trị lớn nhất của li độ trên đồ thị là 4 cm."),
    ("Chu kì dao động là 0,4 s và tần số là 2,5 Hz.", True,
     "Đúng. Đồ thị lặp lại sau 0,4 s ⟹ T = 0,4 s; f = 1/T = 2,5 Hz."),
    ("Phương trình dao động của vật là x = 4cos(5πt + π) cm.", False,
     "Sai ở pha ban đầu. Tại t = 0 vật ở biên DƯƠNG (x = +4 cm) nên φ = 0, phương trình là "
     "x = 4cos(5πt) cm. Với φ = π thì tại t = 0 vật phải ở biên âm."),
    ("Tốc độ cực đại của vật xấp xỉ 62,8 cm/s.", True,
     "Đúng. v_max = ωA = 5π · 4 = 20π ≈ 62,8 cm/s.")],
   "Đọc đồ thị – viết phương trình", TB, fig="d_dt_xt",
   cap="Đồ thị li độ theo thời gian"),

ds("Hình bên là đồ thị li độ của một vật dao động điều hoà khác.",
   [("Biên độ dao động là 5 cm và chu kì là 0,6 s.", True,
     "Đúng, đọc trực tiếp từ đồ thị."),
    ("Tại thời điểm t = 0, vật ở vị trí cân bằng và đang chuyển động theo chiều dương.", True,
     "Đúng. Đồ thị xuất phát từ x = 0 và đi lên phía li độ dương."),
    ("Pha ban đầu của dao động là +π/2 rad.", False,
     "Sai. Với x = A·cos(ωt + φ), điều kiện x(0) = 0 và v(0) > 0 cho φ = −π/2 rad. Nếu φ = +π/2 thì tại "
     "t = 0 vật đi qua vị trí cân bằng theo chiều ÂM."),
    ("Tần số góc của dao động xấp xỉ 10,5 rad/s.", True,
     "Đúng. ω = 2π/T = 2π/0,6 ≈ 10,47 rad/s.")],
   "Đọc đồ thị – xác định pha ban đầu", TB, fig="d_dt_xt2",
   cap="Đồ thị li độ theo thời gian"),

ds("Hai dao động điều hoà cùng chu kì 0,4 s có đồ thị li độ như hình bên.",
   [("Hai dao động có cùng chu kì nhưng khác biên độ.", True,
     "Đúng. Cả hai đều lặp lại sau 0,4 s; biên độ lần lượt là 4 cm và 3 cm."),
    ("Dao động (2) trễ pha π/2 so với dao động (1).", True,
     "Đúng. Dao động (2) đạt cực đại muộn hơn một phần tư chu kì (0,1 s), tương ứng độ lệch pha π/2."),
    ("Hai dao động luôn đạt li độ cực đại cùng lúc.", False,
     "Sai. Chúng lệch pha π/2 nên khi dao động (1) ở biên thì dao động (2) đang ở vị trí cân bằng và "
     "ngược lại."),
    ("Ở thời điểm dao động (1) có li độ bằng 0 thì dao động (2) có độ lớn li độ cực đại.", True,
     "Đúng, đó là hệ quả trực tiếp của việc hai dao động vuông pha.")],
   "Độ lệch pha", TB, fig="d_dt_lechpha", cap="Hai dao động lệch pha"),

ds("Xét con lắc lò xo và con lắc đơn dao động nhỏ.",
   [("Chu kì con lắc lò xo không phụ thuộc biên độ dao động.", True,
     "Đúng. T = 2π√(m/k) chỉ phụ thuộc m và k."),
    ("Chu kì con lắc đơn không phụ thuộc khối lượng vật nặng.", True,
     "Đúng. T = 2π√(ℓ/g) không chứa m — đó cũng là lí do con lắc đơn được dùng để đo g."),
    ("Nếu tăng chiều dài dây con lắc đơn lên 4 lần thì chu kì tăng 4 lần.", False,
     "Sai. T ∝ √ℓ nên chu kì chỉ tăng √4 = 2 lần."),
    ("Nếu tăng khối lượng vật nặng của con lắc lò xo lên 4 lần thì chu kì tăng 2 lần.", True,
     "Đúng. T ∝ √m nên khối lượng tăng 4 lần thì chu kì tăng √4 = 2 lần.")],
   "Con lắc lò xo – con lắc đơn", TB, fig="d_sd_cldon", cap="Con lắc đơn"),
],
P3=[
sa("Từ đồ thị li độ – thời gian ở hình bên, chu kì dao động của vật bằng bao nhiêu giây "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "0,4", "Đồ thị lặp lại sau mỗi 0,4 s ⟹ T = 0,4 s.", "Đọc đồ thị li độ – thời gian", D,
   fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

sa("Vẫn với đồ thị đó, tốc độ cực đại của vật bằng bao nhiêu xentimét trên giây (làm tròn đến chữ số "
   "thập phân thứ nhất)?",
   "62,8", "ω = 2π/0,4 = 5π rad/s; v_max = ωA = 5π · 4 ≈ 62,8 cm/s.",
   "Vận tốc trong dao động điều hoà", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

sa("Một vật dao động điều hoà thực hiện 30 dao động trong 12 giây. Tần số dao động bằng bao nhiêu héc "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "2,5", "f = N/t = 30/12 = 2,5 Hz.", "Chu kì – tần số", D),

sa("Một vật dao động điều hoà với biên độ 6 cm. Quãng đường vật đi được trong một chu kì bằng bao nhiêu "
   "xentimét?",
   "24", "S = 4A = 4 · 6 = 24 cm.", "Quãng đường trong dao động điều hoà", D),

sa("Một con lắc đơn dao động nhỏ với chu kì 2,0 s. Nếu tăng chiều dài dây lên 9 lần thì chu kì bằng bao "
   "nhiêu giây?",
   "6", "T ∝ √ℓ ⟹ T′ = 2,0 · √9 = 6,0 s.", "Con lắc đơn", TB),

sa("Một vật dao động điều hoà với phương trình x = 3cos(10t + π/3) cm. Li độ của vật tại thời điểm t = 0 "
   "bằng bao nhiêu xentimét (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,5", "x(0) = 3·cos(π/3) = 3 · 0,5 = 1,5 cm.", "Đọc phương trình dao động", TB),
])


# =====================================================================
DE3 = dict(
ma="11C1-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Vận tốc, gia tốc và hệ thức độc lập với thời gian",
P1=[
mc("Trong dao động điều hoà, hệ thức liên hệ giữa li độ x, vận tốc v, biên độ A và tần số góc ω là",
   ["A² = x² + v²ω².", "A² = x² + v²/ω².", "A² = x²/ω² + v².", "A = x + v/ω."],
   "B",
   "Từ x = A·cos(ωt + φ) và v = −ωA·sin(ωt + φ), bình phương rồi cộng lại:\n"
   "x² + v²/ω² = A²(cos² + sin²) = A². Đây là hệ thức độc lập với thời gian.",
   "Hệ thức độc lập với thời gian", TB),

mc("Một vật dao động điều hoà với biên độ 5 cm, tần số góc 10 rad/s. Khi li độ là 3 cm thì tốc độ của vật là",
   ["20 cm/s.", "30 cm/s.", "40 cm/s.", "50 cm/s."],
   "C", "v = ω√(A² − x²) = 10 · √(5² − 3²) = 10 · 4 = 40 cm/s.",
   "Hệ thức độc lập với thời gian", TB, fig="d_dt_v_x",
   cap="Đồ thị vận tốc theo li độ (đường elip)"),

mc("Vẫn với vật ở câu trên, khi tốc độ là 30 cm/s thì li độ có độ lớn bằng",
   ["2 cm.", "3 cm.", "4 cm.", "4,5 cm."],
   "C", "x = √(A² − v²/ω²) = √(25 − 900/100) = √(25 − 9) = 4 cm.",
   "Hệ thức độc lập với thời gian", TB, fig="d_dt_v_x", cap="Đồ thị vận tốc theo li độ"),

mc("Đồ thị biểu diễn vận tốc theo li độ của một vật dao động điều hoà có dạng",
   ["đường thẳng.", "đường parabol.", "đường elip.", "đường hypebol."],
   "C",
   "Từ x²/A² + v²/(ωA)² = 1 — đây là phương trình đường elip với hai bán trục A và ωA.",
   "Hệ thức độc lập với thời gian", TB, fig="d_dt_v_x", cap="Đồ thị v theo x"),

mc("Từ đồ thị v theo x ở hình bên, biên độ và tốc độ cực đại của vật lần lượt là",
   ["5 cm và 50 cm/s.", "5 cm và 10 cm/s.", "10 cm và 50 cm/s.", "2,5 cm và 25 cm/s."],
   "A",
   "Elip cắt trục hoành tại x = ±5 cm ⟹ A = 5 cm; cắt trục tung tại v = ±50 cm/s ⟹ v_max = 50 cm/s. "
   "(Từ đó ω = v_max/A = 10 rad/s.)",
   "Đọc đồ thị v – x", TB, fig="d_dt_v_x", cap="Đồ thị v theo x"),

mc("Trong dao động điều hoà, gia tốc và li độ",
   ["cùng pha.", "ngược pha.", "vuông pha.", "lệch pha π/4."],
   "B", "a = −ω²x nên a và x luôn trái dấu và tỉ lệ với nhau: hai đại lượng ngược pha.",
   "Độ lệch pha giữa x, v, a", TB, fig="d_dt_xva",
   cap="Đồ thị li độ, vận tốc, gia tốc của cùng một dao động"),

mc("Hình bên là đồ thị li độ, vận tốc và gia tốc của cùng một vật dao động điều hoà. Khi li độ đạt cực "
   "đại thì",
   ["vận tốc cực đại, gia tốc bằng 0.", "vận tốc bằng 0, gia tốc có độ lớn cực đại.",
    "cả vận tốc và gia tốc đều cực đại.", "cả vận tốc và gia tốc đều bằng 0."],
   "B",
   "Ở biên (li độ cực đại): vật đổi chiều nên v = 0; còn a = −ω²x có độ lớn cực đại ω²A và hướng về vị "
   "trí cân bằng.",
   "Đọc đồ thị x, v, a", TB, fig="d_dt_xva", cap="Đồ thị x, v, a"),

mc("Một vật dao động điều hoà với phương trình x = 4cos(5πt) cm. Phương trình vận tốc của vật là",
   ["v = 20πcos(5πt) cm/s.", "v = −20πsin(5πt) cm/s.",
    "v = 20πsin(5πt) cm/s.", "v = −100π²cos(5πt) cm/s."],
   "B", "v = x′ = −Aω·sin(ωt + φ) = −4 · 5π · sin(5πt) = −20π·sin(5πt) cm/s.",
   "Vận tốc trong dao động điều hoà", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Vẫn với dao động ở câu trên, phương trình gia tốc của vật là",
   ["a = −100π²cos(5πt) cm/s².", "a = 100π²cos(5πt) cm/s².",
    "a = −20πsin(5πt) cm/s².", "a = 20πcos(5πt) cm/s²."],
   "A", "a = −ω²x = −(5π)² · 4cos(5πt) = −100π²·cos(5πt) cm/s².",
   "Gia tốc trong dao động điều hoà", TB),

mc("Một vật dao động điều hoà có gia tốc cực đại 8 m/s² và tốc độ cực đại 0,4 m/s. Tần số góc của dao "
   "động là",
   ["10 rad/s.", "20 rad/s.", "3,2 rad/s.", "0,05 rad/s."],
   "B", "ω = a_max/v_max = 8/0,4 = 20 rad/s (vì a_max = ω²A và v_max = ωA).",
   "Vận tốc – gia tốc cực đại", K),

mc("Vẫn với vật ở câu trên, biên độ dao động là",
   ["0,02 m.", "0,04 m.", "0,20 m.", "2,00 m."],
   "A", "A = v_max/ω = 0,4/20 = 0,02 m = 2 cm.", "Vận tốc – gia tốc cực đại", K),

mc("Một vật dao động điều hoà, khi li độ bằng nửa biên độ thì tốc độ của vật bằng",
   ["v_max/2.", "v_max·√3/2.", "v_max/√2.", "v_max·√2/2."],
   "B",
   "v = ω√(A² − x²) = ω√(A² − A²/4) = ωA·√3/2 = v_max·√3/2 ≈ 0,87·v_max.",
   "Hệ thức độc lập với thời gian", K),

mc("Một vật dao động điều hoà với chu kì 0,4 s và biên độ 4 cm. Tốc độ trung bình của vật trong một chu "
   "kì là",
   ["10 cm/s.", "20 cm/s.", "40 cm/s.", "62,8 cm/s."],
   "C",
   "Tốc độ trung bình = quãng đường/thời gian = 4A/T = 4 · 4/0,4 = 40 cm/s.\n"
   "Chú ý phân biệt với tốc độ CỰC ĐẠI (62,8 cm/s) và với vận tốc trung bình (bằng 0 trong một chu kì).",
   "Tốc độ trung bình", K),

mc("Vận tốc trung bình của một vật dao động điều hoà trong một chu kì bằng",
   ["v_max.", "4A/T.", "0.", "2A/T."],
   "C",
   "Vận tốc trung bình = độ dịch chuyển/thời gian. Sau một chu kì vật trở về vị trí cũ nên độ dịch chuyển "
   "bằng 0 ⟹ vận tốc trung bình bằng 0. Đại lượng 4A/T là TỐC ĐỘ trung bình.",
   "Tốc độ trung bình – vận tốc trung bình", K),

mc("Một vật dao động điều hoà với ω = 10 rad/s. Tại thời điểm vật có li độ 4 cm và tốc độ 30 cm/s thì "
   "biên độ dao động là",
   ["4 cm.", "5 cm.", "6 cm.", "7 cm."],
   "B", "A = √(x² + v²/ω²) = √(16 + 900/100) = √(16 + 9) = 5 cm.",
   "Hệ thức độc lập với thời gian", TB),

mc("Trong dao động điều hoà, khi vật chuyển động từ biên về vị trí cân bằng thì",
   ["tốc độ tăng, độ lớn gia tốc tăng.", "tốc độ tăng, độ lớn gia tốc giảm.",
    "tốc độ giảm, độ lớn gia tốc tăng.", "tốc độ giảm, độ lớn gia tốc giảm."],
   "B",
   "Đi từ biên về vị trí cân bằng: |x| giảm nên |a| = ω²|x| giảm; đồng thời v = ω√(A² − x²) tăng, đạt cực "
   "đại tại vị trí cân bằng.",
   "Vận tốc – gia tốc", TB),

mc("Một chất điểm dao động điều hoà với biên độ A. Quãng đường vật đi được trong một phần tư chu kì, tính "
   "từ vị trí cân bằng, bằng",
   ["A/2.", "A.", "2A.", "A√2/2."],
   "B", "Từ vị trí cân bằng, sau T/4 vật đến đúng vị trí biên, quãng đường đi được là A.",
   "Quãng đường trong dao động điều hoà", TB),

mc("Hai đại lượng nào sau đây trong dao động điều hoà luôn vuông pha với nhau?",
   ["Li độ và gia tốc.", "Li độ và vận tốc.",
    "Vận tốc và gia tốc.", "Cả li độ – vận tốc và vận tốc – gia tốc."],
   "D",
   "v sớm pha π/2 so với x; a sớm pha π/2 so với v (và ngược pha với x). Vậy cả hai cặp (x, v) và (v, a) "
   "đều vuông pha.",
   "Độ lệch pha giữa x, v, a", K, fig="d_dt_xva", cap="Đồ thị x, v, a"),
],
P2=[
ds("Một vật dao động điều hoà với biên độ 5 cm và tần số góc 10 rad/s; đồ thị vận tốc theo li độ như "
   "hình bên.",
   [("Đồ thị v theo x là một đường elip vì x²/A² + v²/(ωA)² = 1.", True,
     "Đúng, đó là hệ thức độc lập với thời gian viết ở dạng chính tắc của elip."),
    ("Tốc độ cực đại của vật là 50 cm/s.", True,
     "Đúng. v_max = ωA = 10 · 5 = 50 cm/s, đúng bằng giao điểm của elip với trục tung."),
    ("Khi li độ bằng 3 cm thì tốc độ của vật là 40 cm/s.", True,
     "Đúng. v = ω√(A² − x²) = 10√(25 − 9) = 40 cm/s."),
    ("Khi tốc độ bằng 25 cm/s thì li độ có độ lớn bằng 2,5 cm.", False,
     "Sai. x = √(A² − v²/ω²) = √(25 − 625/100) = √18,75 ≈ 4,33 cm, chứ không phải 2,5 cm. "
     "Quan hệ giữa x và v KHÔNG tuyến tính.")],
   "Hệ thức độc lập với thời gian", K, fig="d_dt_v_x", cap="Đồ thị v theo x"),

ds("Hình bên là đồ thị li độ, vận tốc và gia tốc theo thời gian của cùng một vật dao động điều hoà.",
   [("Khi li độ cực đại thì vận tốc bằng 0 và độ lớn gia tốc cực đại.", True,
     "Đúng. Ở biên vật đổi chiều nên v = 0; còn a = −ω²x đạt độ lớn ω²A."),
    ("Khi vật qua vị trí cân bằng thì tốc độ cực đại và gia tốc bằng 0.", True,
     "Đúng. x = 0 ⟹ a = −ω²x = 0, đồng thời v = ω√(A² − x²) đạt giá trị lớn nhất ωA."),
    ("Vận tốc sớm pha π/2 so với li độ, còn gia tốc ngược pha với li độ.", True,
     "Đúng. v = ωA·cos(ωt + φ + π/2) và a = ω²A·cos(ωt + φ + π)."),
    ("Gia tốc và vận tốc luôn cùng dấu với nhau.", False,
     "Sai. Hai đại lượng này vuông pha nên khi một đại lượng cực đại thì đại lượng kia bằng 0; dấu của "
     "chúng thay đổi độc lập theo từng phần tư chu kì.")],
   "Đọc đồ thị x, v, a", K, fig="d_dt_xva", cap="Đồ thị x, v, a"),

ds("Một vật dao động điều hoà có gia tốc cực đại 8 m/s² và tốc độ cực đại 0,4 m/s.",
   [("Tần số góc của dao động là 20 rad/s.", True,
     "Đúng. ω = a_max/v_max = 8/0,4 = 20 rad/s."),
    ("Biên độ dao động là 2 cm.", True,
     "Đúng. A = v_max/ω = 0,4/20 = 0,02 m = 2 cm."),
    ("Chu kì dao động xấp xỉ 0,31 s.", True,
     "Đúng. T = 2π/ω = 2π/20 ≈ 0,314 s."),
    ("Khi vật ở vị trí có li độ 1 cm thì tốc độ của vật là 0,20 m/s.", False,
     "Sai. v = ω√(A² − x²) = 20·√(0,02² − 0,01²) = 20 · 0,01732 ≈ 0,35 m/s, tức khoảng 0,87 lần tốc độ "
     "cực đại (không phải 0,5 lần).")],
   "Vận tốc – gia tốc cực đại", K),

ds("Xét các đại lượng trung bình trong dao động điều hoà với biên độ A và chu kì T.",
   [("Tốc độ trung bình trong một chu kì bằng 4A/T.", True,
     "Đúng. Quãng đường trong một chu kì là 4A, chia cho thời gian T."),
    ("Vận tốc trung bình trong một chu kì bằng 0.", True,
     "Đúng. Độ dịch chuyển sau một chu kì bằng 0."),
    ("Tốc độ trung bình trong một chu kì bằng tốc độ cực đại.", False,
     "Sai. 4A/T = 4A·ω/(2π) = (2/π)·ωA ≈ 0,64·v_max, nhỏ hơn tốc độ cực đại."),
    ("Tốc độ trung bình khi vật đi từ vị trí cân bằng ra biên bằng 4A/T.", True,
     "Đúng. Quãng đường A trong thời gian T/4 ⟹ tốc độ trung bình = A/(T/4) = 4A/T, đúng bằng giá trị "
     "trong cả chu kì.")],
   "Tốc độ trung bình – vận tốc trung bình", K),
],
P3=[
sa("Một vật dao động điều hoà với biên độ 5 cm, tần số góc 10 rad/s. Khi li độ là 3 cm thì tốc độ của vật "
   "bằng bao nhiêu xentimét trên giây?",
   "40", "v = ω√(A² − x²) = 10√(25 − 9) = 40 cm/s.", "Hệ thức độc lập với thời gian", TB,
   fig="d_dt_v_x", cap="Đồ thị v theo x"),

sa("Một vật dao động điều hoà với ω = 10 rad/s; tại một thời điểm vật có li độ 4 cm và tốc độ 30 cm/s. "
   "Biên độ dao động bằng bao nhiêu xentimét?",
   "5", "A = √(x² + v²/ω²) = √(16 + 9) = 5 cm.", "Hệ thức độc lập với thời gian", TB),

sa("Một vật dao động điều hoà có gia tốc cực đại 8 m/s² và tốc độ cực đại 0,4 m/s. Tần số góc của dao "
   "động bằng bao nhiêu rad/s?",
   "20", "ω = a_max/v_max = 8/0,4 = 20 rad/s.", "Vận tốc – gia tốc cực đại", K),

sa("Vẫn với vật ở câu trên, biên độ dao động bằng bao nhiêu xentimét?",
   "2", "A = v_max/ω = 0,4/20 = 0,02 m = 2 cm.", "Vận tốc – gia tốc cực đại", K),

sa("Một vật dao động điều hoà với chu kì 0,4 s và biên độ 4 cm. Tốc độ trung bình của vật trong một chu "
   "kì bằng bao nhiêu xentimét trên giây?",
   "40", "Tốc độ trung bình = 4A/T = 16/0,4 = 40 cm/s.", "Tốc độ trung bình", K),

sa("Một vật dao động điều hoà với biên độ 6 cm. Khi li độ bằng 3 cm thì tỉ số giữa tốc độ của vật và tốc "
   "độ cực đại bằng bao nhiêu (làm tròn đến chữ số thập phân thứ hai)?",
   "0,87",
   "v/v_max = √(A² − x²)/A = √(36 − 9)/6 = √27/6 = 3√3/6 = √3/2 ≈ 0,87.",
   "Hệ thức độc lập với thời gian", K),
])


# =====================================================================
DE4 = dict(
ma="11C1-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Động năng, thế năng, cơ năng; con lắc lò xo và con lắc đơn",
P1=[
mc("Cơ năng của một vật dao động điều hoà khối lượng m, tần số góc ω, biên độ A được tính bằng",
   ["W = ½mωA².", "W = ½mω²A².", "W = mω²A².", "W = ½mω²A."],
   "B", "W = ½mω²A² = ½kA² (với con lắc lò xo, k = mω²).",
   "Năng lượng trong dao động điều hoà", D),

mc("Một con lắc lò xo có độ cứng 100 N/m dao động với biên độ 4 cm. Cơ năng của con lắc là",
   ["0,04 J.", "0,08 J.", "0,16 J.", "0,80 J."],
   "B", "W = ½kA² = ½ · 100 · (0,04)² = ½ · 100 · 1,6·10⁻³ = 0,08 J = 80 mJ.",
   "Năng lượng con lắc lò xo", TB, fig="d_dt_nangluong_x",
   cap="Động năng và thế năng theo li độ (W = 80 mJ, A = 4 cm)"),

mc("Hình bên là đồ thị động năng và thế năng theo li độ của một vật dao động điều hoà. Cơ năng của vật là",
   ["40 mJ.", "60 mJ.", "80 mJ.", "160 mJ."],
   "C",
   "Đường nằm ngang W biểu diễn cơ năng, có giá trị 80 mJ. Cũng có thể đọc: ở li độ x = ±4 cm (biên) "
   "thế năng đạt cực đại 80 mJ và bằng cơ năng.",
   "Đọc đồ thị năng lượng", TB, fig="d_dt_nangluong_x",
   cap="Động năng và thế năng theo li độ"),

mc("Vẫn với đồ thị trên, tại li độ x = 0 thì",
   ["động năng bằng 0, thế năng bằng 80 mJ.", "động năng bằng 80 mJ, thế năng bằng 0.",
    "động năng và thế năng đều bằng 40 mJ.", "động năng và thế năng đều bằng 0."],
   "B",
   "Ở vị trí cân bằng (x = 0), thế năng bằng 0 và toàn bộ cơ năng ở dạng động năng: Wđ = W = 80 mJ.",
   "Đọc đồ thị năng lượng", TB, fig="d_dt_nangluong_x", cap="Đồ thị năng lượng theo li độ"),

mc("Vẫn với đồ thị trên, tại li độ nào thì động năng bằng thế năng?",
   ["x = ±2,00 cm.", "x = ±2,83 cm.", "x = ±3,46 cm.", "x = ±4,00 cm."],
   "B",
   "Wđ = Wt = W/2 ⟹ ½kx² = ½·(½kA²) ⟹ x² = A²/2 ⟹ x = ±A/√2 = ±4/√2 ≈ ±2,83 cm.\n"
   "Trên đồ thị đó là giao điểm của hai đường parabol, ở mức 40 mJ.",
   "Năng lượng trong dao động điều hoà", K, fig="d_dt_nangluong_x",
   cap="Đồ thị năng lượng theo li độ"),

mc("Một vật dao động điều hoà với biên độ A. Tại li độ nào thì động năng bằng 3 lần thế năng?",
   ["x = ±A/2.", "x = ±A/√2.", "x = ±A√3/2.", "x = ±A/4."],
   "A",
   "Wđ = 3Wt ⟹ W = Wđ + Wt = 4Wt ⟹ ½kA² = 4 · ½kx² ⟹ x² = A²/4 ⟹ x = ±A/2.",
   "Năng lượng trong dao động điều hoà", K),

mc("Hình bên là đồ thị động năng và thế năng theo thời gian của một vật dao động điều hoà có chu kì 0,4 s. "
   "Chu kì biến thiên của động năng là",
   ["0,1 s.", "0,2 s.", "0,4 s.", "0,8 s."],
   "B",
   "Wđ = ½mv² ∝ sin²(ωt + φ) = ½[1 − cos(2ωt + 2φ)] nên động năng biến thiên với tần số góc 2ω, tức chu "
   "kì bằng một nửa chu kì dao động: T′ = T/2 = 0,2 s.",
   "Đọc đồ thị năng lượng theo thời gian", K, fig="d_dt_nangluong_t",
   cap="Động năng và thế năng theo thời gian (T = 0,4 s)"),

mc("Vẫn với đồ thị năng lượng theo thời gian đó, tại những thời điểm động năng bằng thế năng thì mỗi loại "
   "năng lượng bằng",
   ["20 mJ.", "40 mJ.", "60 mJ.", "80 mJ."],
   "B", "Wđ = Wt = W/2 = 80/2 = 40 mJ — đó cũng là các giao điểm của hai đường trên đồ thị.",
   "Đọc đồ thị năng lượng theo thời gian", TB, fig="d_dt_nangluong_t",
   cap="Đồ thị năng lượng theo thời gian"),

mc("Một con lắc lò xo gồm lò xo độ cứng 50 N/m và vật nặng 0,20 kg. Chu kì dao động của con lắc là",
   ["0,20 s.", "0,40 s.", "0,63 s.", "1,26 s."],
   "B",
   "T = 2π√(m/k) = 2π√(0,20/50) = 2π√(4,0·10⁻³) = 2π · 0,0632 ≈ 0,397 s ≈ 0,40 s.",
   "Con lắc lò xo", TB, fig="d_sd_loxo_ngang", cap="Con lắc lò xo"),

mc("Một con lắc lò xo treo thẳng đứng, khi vật ở vị trí cân bằng lò xo dãn thêm 4,0 cm. Lấy g = 10 m/s². "
   "Chu kì dao động của con lắc là",
   ["0,20 s.", "0,40 s.", "0,63 s.", "1,26 s."],
   "B",
   "Ở vị trí cân bằng: k·Δℓ₀ = mg ⟹ m/k = Δℓ₀/g.\n"
   "T = 2π√(m/k) = 2π√(Δℓ₀/g) = 2π√(0,040/10) = 2π · 0,0632 ≈ 0,40 s.\n"
   "Công thức T = 2π√(Δℓ₀/g) rất tiện khi biết độ dãn của lò xo ở vị trí cân bằng.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Một con lắc đơn có chiều dài 0,64 m dao động nhỏ tại nơi có g = 10 m/s². Chu kì dao động gần nhất với",
   ["1,26 s.", "1,59 s.", "2,01 s.", "2,51 s."],
   "B", "T = 2π√(ℓ/g) = 2π√(0,064) = 2π · 0,253 ≈ 1,59 s.",
   "Con lắc đơn", TB, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Nếu đưa một con lắc đơn từ mặt đất lên cao (nơi g nhỏ hơn) mà giữ nguyên chiều dài dây thì chu kì "
   "dao động của nó",
   ["tăng.", "giảm.", "không đổi.", "chưa xác định được."],
   "A", "T = 2π√(ℓ/g) tỉ lệ nghịch với √g; g giảm thì T tăng (đồng hồ quả lắc sẽ chạy chậm lại).",
   "Con lắc đơn", TB),

mc("Một con lắc lò xo dao động điều hoà. Nếu tăng biên độ lên gấp đôi (giữ nguyên lò xo và vật) thì cơ "
   "năng của con lắc",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "tăng 8 lần."],
   "C", "W = ½kA² tỉ lệ với BÌNH PHƯƠNG biên độ ⟹ A tăng 2 lần thì W tăng 4 lần.",
   "Năng lượng con lắc lò xo", TB),

mc("Một vật khối lượng 0,25 kg dao động điều hoà với biên độ 8 cm và tần số góc 10 rad/s. Cơ năng của "
   "vật là",
   ["0,04 J.", "0,08 J.", "0,16 J.", "0,80 J."],
   "B", "W = ½mω²A² = ½ · 0,25 · 100 · (0,08)² = ½ · 25 · 6,4·10⁻³ = 0,08 J.",
   "Năng lượng trong dao động điều hoà", TB),

mc("Trong dao động điều hoà, khi vật đi từ vị trí cân bằng ra biên thì",
   ["động năng tăng, thế năng giảm.", "động năng giảm, thế năng tăng.",
    "cả hai đều tăng.", "cả hai đều giảm."],
   "B",
   "Ra xa vị trí cân bằng: |x| tăng nên thế năng tăng; tốc độ giảm nên động năng giảm. Tổng của chúng "
   "(cơ năng) không đổi.",
   "Năng lượng trong dao động điều hoà", D),

mc("Một con lắc lò xo có cơ năng 0,10 J và biên độ 5 cm. Độ cứng của lò xo là",
   ["40 N/m.", "80 N/m.", "100 N/m.", "200 N/m."],
   "B", "k = 2W/A² = 2 · 0,10/(0,05)² = 0,20/2,5·10⁻³ = 80 N/m.",
   "Năng lượng con lắc lò xo", TB),

mc("Hai con lắc đơn có chiều dây lần lượt là ℓ và 4ℓ, dao động nhỏ tại cùng một nơi. Tỉ số chu kì của "
   "chúng là",
   ["1 : 2.", "1 : 4.", "2 : 1.", "1 : 16."],
   "A", "T ∝ √ℓ ⟹ T₁ : T₂ = √ℓ : √(4ℓ) = 1 : 2.", "Con lắc đơn", TB),

mc("Đại lượng nào sau đây của con lắc lò xo dao động điều hoà biến thiên tuần hoàn với chu kì bằng NỬA "
   "chu kì dao động?",
   ["Li độ.", "Vận tốc.", "Gia tốc.", "Động năng."],
   "D",
   "Li độ, vận tốc và gia tốc đều biến thiên với chu kì T. Riêng động năng (và thế năng) chứa bình phương "
   "của hàm sin/côsin nên biến thiên với chu kì T/2.",
   "Năng lượng trong dao động điều hoà", K, fig="d_dt_nangluong_t",
   cap="Đồ thị năng lượng theo thời gian"),
],
P2=[
ds("Hình bên là đồ thị động năng và thế năng theo li độ của một vật dao động điều hoà.",
   [("Cơ năng của vật là 80 mJ và biên độ dao động là 4 cm.", True,
     "Đúng. Đường nằm ngang cho W = 80 mJ; hai parabol gặp trục hoành/đạt cực đại tại x = ±4 cm."),
    ("Ở vị trí cân bằng, động năng bằng cơ năng và thế năng bằng 0.", True,
     "Đúng. Tại x = 0 thì Wt = ½kx² = 0 nên Wđ = W = 80 mJ."),
    ("Động năng và thế năng bằng nhau tại li độ x = ±2 cm.", False,
     "Sai. Wđ = Wt = W/2 ⟹ x = ±A/√2 ≈ ±2,83 cm. Li độ x = ±2 cm = ±A/2 ứng với Wđ = 3Wt "
     "(thế năng chỉ bằng 20 mJ)."),
    ("Nếu độ cứng của lò xo là 100 N/m thì cơ năng 80 mJ ứng với biên độ 4 cm.", True,
     "Đúng. W = ½kA² = ½ · 100 · 0,04² = 0,08 J = 80 mJ.")],
   "Đọc đồ thị năng lượng theo li độ", K, fig="d_dt_nangluong_x",
   cap="Động năng và thế năng theo li độ"),

ds("Hình bên là đồ thị động năng và thế năng theo thời gian của một vật dao động điều hoà có chu kì 0,4 s "
   "và cơ năng 80 mJ.",
   [("Động năng và thế năng biến thiên tuần hoàn với chu kì 0,2 s.", True,
     "Đúng. Chúng chứa bình phương của hàm sin/côsin nên chu kì bằng một nửa chu kì dao động."),
    ("Tại mọi thời điểm, tổng động năng và thế năng luôn bằng 80 mJ.", True,
     "Đúng. Đó là sự bảo toàn cơ năng khi bỏ qua ma sát; trên đồ thị hai đường luôn “bù” cho nhau."),
    ("Ở những thời điểm hai đường cắt nhau, mỗi loại năng lượng bằng 40 mJ.", True,
     "Đúng. Wđ = Wt = W/2 = 40 mJ."),
    ("Trong một chu kì dao động, động năng đạt cực đại một lần.", False,
     "Sai. Vật đi qua vị trí cân bằng HAI lần trong mỗi chu kì nên động năng đạt cực đại hai lần "
     "(phù hợp với việc chu kì của động năng chỉ bằng T/2).")],
   "Đọc đồ thị năng lượng theo thời gian", K, fig="d_dt_nangluong_t",
   cap="Đồ thị năng lượng theo thời gian"),

ds("Xét con lắc lò xo treo thẳng đứng: lò xo độ cứng k, vật nặng khối lượng m, ở vị trí cân bằng lò xo "
   "dãn thêm Δℓ₀ = 4,0 cm. Lấy g = 10 m/s².",
   [("Ở vị trí cân bằng, lực đàn hồi của lò xo cân bằng với trọng lực: k·Δℓ₀ = mg.", True,
     "Đúng, đó là điều kiện cân bằng của vật khi treo yên."),
    ("Chu kì dao động của con lắc có thể tính bằng T = 2π√(Δℓ₀/g).", True,
     "Đúng. Từ k·Δℓ₀ = mg suy ra m/k = Δℓ₀/g, thay vào T = 2π√(m/k)."),
    ("Chu kì dao động của con lắc xấp xỉ 0,40 s.", True,
     "Đúng. T = 2π√(0,040/10) = 2π · 0,0632 ≈ 0,397 s."),
    ("Nếu treo thêm một vật nữa để khối lượng tăng gấp đôi thì chu kì cũng tăng gấp đôi.", False,
     "Sai. T ∝ √m nên khối lượng tăng gấp đôi thì chu kì chỉ tăng √2 ≈ 1,41 lần (khoảng 0,56 s).")],
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

ds("Xét con lắc đơn dao động nhỏ với chu kì T = 2π√(ℓ/g).",
   [("Chu kì con lắc đơn không phụ thuộc khối lượng vật nặng.", True,
     "Đúng, công thức không chứa m — đây là cơ sở để dùng con lắc đơn đo gia tốc trọng trường."),
    ("Nếu tăng chiều dài dây lên 4 lần thì chu kì tăng 2 lần.", True,
     "Đúng. T ∝ √ℓ."),
    ("Đưa con lắc lên cao (g giảm) thì chu kì giảm.", False,
     "Sai. T tỉ lệ nghịch với √g nên g giảm thì chu kì TĂNG; đồng hồ quả lắc trên núi cao sẽ chạy chậm lại."),
    ("Chu kì con lắc đơn cũng không phụ thuộc biên độ, với điều kiện dao động là dao động nhỏ.", True,
     "Đúng. Công thức T = 2π√(ℓ/g) chỉ áp dụng cho dao động nhỏ; khi biên độ góc lớn thì chu kì tăng lên "
     "chút ít và công thức không còn chính xác.")],
   "Con lắc đơn", TB, fig="d_sd_cldon", cap="Con lắc đơn"),
],
P3=[
sa("Một con lắc lò xo có độ cứng 100 N/m dao động với biên độ 4 cm. Cơ năng của con lắc bằng bao nhiêu "
   "milijun?",
   "80", "W = ½kA² = ½ · 100 · (0,04)² = 0,08 J = 80 mJ.", "Năng lượng con lắc lò xo", TB,
   fig="d_dt_nangluong_x", cap="Đồ thị năng lượng theo li độ"),

sa("Một vật dao động điều hoà với biên độ 4 cm. Tại li độ nào (tính bằng xentimét, lấy giá trị dương, làm "
   "tròn đến chữ số thập phân thứ hai) thì động năng bằng thế năng?",
   "2,83", "Wđ = Wt ⟹ x = A/√2 = 4/√2 = 2√2 ≈ 2,83 cm.",
   "Năng lượng trong dao động điều hoà", K),

sa("Một con lắc lò xo gồm lò xo độ cứng 50 N/m và vật nặng 0,20 kg. Chu kì dao động bằng bao nhiêu giây "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,40", "T = 2π√(m/k) = 2π√(0,20/50) = 2π · 0,0632 ≈ 0,40 s.", "Con lắc lò xo", TB),

sa("Một con lắc lò xo treo thẳng đứng, ở vị trí cân bằng lò xo dãn thêm 4,0 cm. Lấy g = 10 m/s². Chu kì "
   "dao động bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ hai)?",
   "0,40", "T = 2π√(Δℓ₀/g) = 2π√(0,040/10) ≈ 0,40 s.", "Con lắc lò xo treo thẳng đứng", K,
   fig="d_sd_loxo_doc", cap="Con lắc lò xo treo thẳng đứng"),

sa("Một con lắc đơn dài 0,64 m dao động nhỏ tại nơi có g = 10 m/s². Chu kì dao động bằng bao nhiêu giây "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "1,59", "T = 2π√(ℓ/g) = 2π√0,064 = 2π · 0,2530 ≈ 1,59 s.", "Con lắc đơn", TB),

sa("Một con lắc lò xo có cơ năng 0,10 J và biên độ 5 cm. Độ cứng của lò xo bằng bao nhiêu N/m?",
   "80", "k = 2W/A² = 0,20/(0,05)² = 0,20/0,0025 = 80 N/m.", "Năng lượng con lắc lò xo", TB),
])


# =====================================================================
DE5 = dict(
ma="11C1-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Thời gian và quãng đường trong dao động điều hoà; tỉ số động năng – thế năng",
P1=[
mc("Một vật dao động điều hoà với chu kì T. Thời gian ngắn nhất để vật đi từ vị trí cân bằng tới vị trí "
   "có li độ bằng nửa biên độ là",
   ["T/12.", "T/8.", "T/6.", "T/4."],
   "A",
   "Dùng liên hệ với chuyển động tròn đều: li độ x = A/2 ứng với góc quay 30° kể từ vị trí cân bằng "
   "(vì cos60° = 1/2 tính từ biên, tương đương 30° tính từ vị trí cân bằng).\n"
   "Δt = (30°/360°)·T = T/12.",
   "Thời gian trong dao động điều hoà", K, fig="d_sd_vongtron",
   cap="Liên hệ giữa dao động điều hoà và chuyển động tròn đều"),

mc("Một vật dao động điều hoà với chu kì T. Thời gian ngắn nhất để vật đi từ biên dương tới vị trí có li "
   "độ bằng nửa biên độ là",
   ["T/12.", "T/8.", "T/6.", "T/4."],
   "C",
   "Từ biên (góc 0°) tới li độ A/2 ứng với góc quay 60° trên đường tròn ⟹ Δt = (60°/360°)·T = T/6.",
   "Thời gian trong dao động điều hoà", K, fig="d_sd_vongtron",
   cap="Liên hệ với chuyển động tròn đều"),

mc("Một vật dao động điều hoà với chu kì 0,6 s và biên độ 8 cm. Quãng đường vật đi được trong 0,3 s "
   "(nửa chu kì) là",
   ["8 cm.", "16 cm.", "24 cm.", "32 cm."],
   "B", "Trong nửa chu kì, quãng đường luôn bằng 2A = 16 cm, bất kể xuất phát từ đâu.",
   "Quãng đường trong dao động điều hoà", TB),

mc("Vẫn với vật ở câu trên, quãng đường vật đi được trong 1,5 s là",
   ["40 cm.", "60 cm.", "80 cm.", "120 cm."],
   "C",
   "1,5 s = 2,5T. Trong 2 chu kì đi được 2 · 4A = 64 cm; trong nửa chu kì còn lại đi được 2A = 16 cm.\n"
   "Tổng: 64 + 16 = 80 cm.",
   "Quãng đường trong dao động điều hoà", K),

mc("Một vật dao động điều hoà với biên độ A. Tại li độ nào thì thế năng bằng 3 lần động năng?",
   ["x = ±A/2.", "x = ±A/√2.", "x = ±A√3/2.", "x = ±A/4."],
   "C",
   "Wt = 3Wđ ⟹ W = Wt + Wđ = (4/3)Wt ⟹ ½kA² = (4/3)·½kx² ⟹ x² = (3/4)A² ⟹ x = ±A√3/2 ≈ ±0,87A.",
   "Năng lượng trong dao động điều hoà", K),

mc("Một vật dao động điều hoà. Tỉ số giữa động năng và thế năng khi vật ở li độ x = A/2 là",
   ["1/3.", "1.", "3.", "4."],
   "C",
   "Wt/W = x²/A² = 1/4 ⟹ Wt = W/4 và Wđ = 3W/4 ⟹ Wđ/Wt = 3.",
   "Năng lượng trong dao động điều hoà", K),

mc("Một vật dao động điều hoà với biên độ 10 cm. Khi động năng bằng 3 lần thế năng, tốc độ của vật bằng "
   "bao nhiêu phần tốc độ cực đại?",
   ["1/2.", "√3/2.", "1/√2.", "3/4."],
   "B",
   "Wđ = 3Wt ⟹ Wđ = (3/4)W ⟹ ½mv² = (3/4)·½mv²_max ⟹ v = v_max·√3/2 ≈ 0,87·v_max.",
   "Năng lượng trong dao động điều hoà", K),

mc("Một vật dao động điều hoà với phương trình x = 6cos(4πt − π/3) cm. Pha ban đầu và tần số của dao "
   "động là",
   ["−π/3 rad và 2 Hz.", "π/3 rad và 2 Hz.", "−π/3 rad và 4 Hz.", "π/3 rad và 4 Hz."],
   "A", "φ = −π/3 rad; ω = 4π rad/s ⟹ f = ω/(2π) = 2 Hz.", "Đọc phương trình dao động", TB),

mc("Vẫn với dao động ở câu trên, li độ của vật tại thời điểm t = 0 là",
   ["6,0 cm.", "3,0 cm.", "−3,0 cm.", "5,2 cm."],
   "B", "x(0) = 6·cos(−π/3) = 6 · 0,5 = 3,0 cm.", "Đọc phương trình dao động", TB),

mc("Một vật dao động điều hoà với chu kì T. Khoảng thời gian ngắn nhất giữa hai lần liên tiếp động năng "
   "bằng thế năng là",
   ["T/8.", "T/4.", "T/2.", "T."],
   "B",
   "Động năng bằng thế năng khi x = ±A/√2, tức 4 vị trí trong mỗi chu kì, chia đều nhau. Khoảng thời "
   "gian giữa hai lần liên tiếp là T/4.",
   "Thời gian trong dao động điều hoà", K),

mc("Một vật dao động điều hoà với tần số 2 Hz. Trong 1 giây, vật đi qua vị trí cân bằng bao nhiêu lần?",
   ["1 lần.", "2 lần.", "4 lần.", "8 lần."],
   "C",
   "Mỗi chu kì vật qua vị trí cân bằng 2 lần; trong 1 s có 2 chu kì ⟹ 2 · 2 = 4 lần.",
   "Chu kì – tần số", TB),

mc("Một vật dao động điều hoà với biên độ 5 cm, chu kì 0,4 s. Tốc độ trung bình của vật khi đi từ vị trí "
   "cân bằng tới biên là",
   ["25 cm/s.", "50 cm/s.", "62,8 cm/s.", "78,5 cm/s."],
   "B",
   "Từ vị trí cân bằng ra biên mất T/4 = 0,1 s và đi được quãng đường A = 5 cm.\n"
   "Tốc độ trung bình = 5/0,1 = 50 cm/s.",
   "Tốc độ trung bình", TB),

mc("Trong dao động điều hoà, khi động năng của vật giảm thì",
   ["thế năng giảm.", "thế năng tăng.", "cơ năng giảm.", "cơ năng tăng."],
   "B", "Cơ năng không đổi nên khi động năng giảm thì thế năng phải tăng đúng bằng phần giảm đó.",
   "Năng lượng trong dao động điều hoà", D),

mc("Một con lắc lò xo dao động điều hoà. Nếu giảm biên độ còn một nửa thì cơ năng của con lắc",
   ["giảm còn một nửa.", "giảm còn một phần tư.", "không đổi.", "tăng gấp đôi."],
   "B", "W = ½kA² tỉ lệ với A² ⟹ A giảm 2 lần thì W giảm 4 lần.",
   "Năng lượng con lắc lò xo", TB),

mc("Một vật dao động điều hoà với chu kì 0,5 s. Thời gian ngắn nhất để vật đi từ li độ x = −A tới li độ "
   "x = +A là",
   ["0,125 s.", "0,250 s.", "0,375 s.", "0,500 s."],
   "B", "Đi từ biên này sang biên kia mất nửa chu kì: Δt = T/2 = 0,25 s.",
   "Thời gian trong dao động điều hoà", TB),

mc("Một vật dao động điều hoà với chu kì T và biên độ A. Quãng đường vật đi được trong khoảng thời gian "
   "T/4 kể từ khi vật ở biên là",
   ["A/2.", "A.", "A√2/2.", "2A."],
   "B", "Từ biên, sau T/4 vật tới đúng vị trí cân bằng, quãng đường đi được là A.",
   "Quãng đường trong dao động điều hoà", TB),

mc("Một vật dao động điều hoà. Số lần vật có động năng bằng thế năng trong một chu kì là",
   ["2 lần.", "4 lần.", "6 lần.", "8 lần."],
   "B",
   "Wđ = Wt khi x = ±A/√2 — mỗi giá trị li độ này được vật đi qua 2 lần trong một chu kì (một lần theo "
   "mỗi chiều), tổng cộng 4 lần.",
   "Năng lượng trong dao động điều hoà", K),

mc("Trong dao động điều hoà, đại lượng nào sau đây luôn dương?",
   ["Li độ.", "Vận tốc.", "Gia tốc.", "Cơ năng."],
   "D",
   "Li độ, vận tốc và gia tốc đều đổi dấu trong quá trình dao động. Cơ năng W = ½mω²A² luôn dương "
   "(và không đổi khi bỏ qua ma sát).",
   "Năng lượng trong dao động điều hoà", D),
],
P2=[
ds("Một vật dao động điều hoà với biên độ A và chu kì T. Xét các khoảng thời gian và quãng đường đặc "
   "trưng của dao động.",
   [("Thời gian ngắn nhất để vật đi từ vị trí cân bằng tới li độ A/2 là T/12.", True,
     "Đúng. Trên đường tròn pha, quãng đó ứng với góc quay 30°: Δt = T·30°/360° = T/12."),
    ("Thời gian ngắn nhất để vật đi từ biên tới li độ A/2 là T/6.", True,
     "Đúng, ứng với góc quay 60° trên đường tròn pha."),
    ("Quãng đường vật đi được trong nửa chu kì luôn bằng 2A, không phụ thuộc vị trí xuất phát.", True,
     "Đúng. Đây là một tính chất rất hữu ích: trong T/2 quãng đường luôn là 2A, trong T luôn là 4A."),
    ("Quãng đường vật đi được trong một phần tư chu kì luôn bằng A, không phụ thuộc vị trí xuất phát.", False,
     "Sai. Chỉ đúng khi xuất phát từ vị trí cân bằng hoặc từ biên. Ví dụ xuất phát từ x = A/2 đi theo "
     "chiều dương, sau T/4 quãng đường đi được khác A.")],
   "Thời gian – quãng đường", K, fig="d_sd_vongtron",
   cap="Đường tròn pha và liên hệ với dao động điều hoà"),

ds("Một vật dao động điều hoà với biên độ A, cơ năng W.",
   [("Khi li độ x = A/2 thì thế năng bằng W/4 và động năng bằng 3W/4.", True,
     "Đúng. Wt/W = x²/A² = 1/4."),
    ("Khi động năng bằng thế năng thì li độ bằng ±A/√2.", True,
     "Đúng. Wt = W/2 ⟹ x²/A² = 1/2 ⟹ x = ±A/√2 ≈ ±0,707A."),
    ("Khi thế năng bằng 3 lần động năng thì li độ bằng ±A√3/2.", True,
     "Đúng. Wt = (3/4)W ⟹ x²/A² = 3/4 ⟹ x = ±A√3/2 ≈ ±0,87A."),
    ("Khi động năng bằng 3 lần thế năng thì tốc độ của vật bằng nửa tốc độ cực đại.", False,
     "Sai. Wđ = (3/4)W ⟹ v²/v²_max = 3/4 ⟹ v = (√3/2)v_max ≈ 0,87·v_max, chứ không phải 0,5·v_max. "
     "(Li độ khi đó mới bằng A/2.)")],
   "Tỉ số động năng – thế năng", K, fig="d_dt_nangluong_x",
   cap="Động năng và thế năng theo li độ"),

ds("Một vật dao động điều hoà với chu kì 0,6 s và biên độ 8 cm.",
   [("Quãng đường vật đi được trong 0,3 s là 16 cm.", True,
     "Đúng. 0,3 s = T/2 ⟹ S = 2A = 16 cm."),
    ("Quãng đường vật đi được trong 1,5 s là 80 cm.", True,
     "Đúng. 1,5 s = 2,5T ⟹ S = 2 · 4A + 2A = 64 + 16 = 80 cm."),
    ("Tốc độ trung bình của vật trong một chu kì xấp xỉ 53,3 cm/s.", True,
     "Đúng. v_tb = 4A/T = 32/0,6 ≈ 53,3 cm/s."),
    ("Vận tốc trung bình của vật trong 1,5 s bằng 53,3 cm/s.", False,
     "Sai. Vận tốc trung bình tính theo ĐỘ DỊCH CHUYỂN. Sau 2,5 chu kì vật ở vị trí đối xứng qua vị trí "
     "cân bằng so với lúc đầu, độ dịch chuyển nói chung khác 4A·2,5; giá trị 53,3 cm/s là TỐC ĐỘ trung "
     "bình chứ không phải vận tốc trung bình.")],
   "Quãng đường – tốc độ trung bình", K),

ds("Xét số lần xảy ra các sự kiện trong một chu kì dao động điều hoà.",
   [("Trong một chu kì, vật đi qua vị trí cân bằng 2 lần.", True,
     "Đúng, một lần theo chiều dương và một lần theo chiều âm."),
    ("Trong một chu kì, vật ở vị trí biên 2 lần.", True,
     "Đúng: một lần ở biên dương và một lần ở biên âm."),
    ("Trong một chu kì, có 4 thời điểm động năng bằng thế năng.", True,
     "Đúng. Điều kiện x = ±A/√2 cho 2 giá trị li độ, mỗi giá trị được đi qua 2 lần."),
    ("Trong một chu kì, động năng của vật đạt cực đại 1 lần.", False,
     "Sai. Động năng cực đại khi vật qua vị trí cân bằng — điều này xảy ra 2 lần trong mỗi chu kì, "
     "phù hợp với việc động năng biến thiên với chu kì T/2.")],
   "Số lần các sự kiện trong một chu kì", K, fig="d_dt_nangluong_t",
   cap="Động năng và thế năng theo thời gian"),
],
P3=[
sa("Một vật dao động điều hoà với chu kì 0,6 s và biên độ 8 cm. Quãng đường vật đi được trong 1,5 s bằng "
   "bao nhiêu xentimét?",
   "80", "1,5 s = 2,5T ⟹ S = 2·4A + 2A = 64 + 16 = 80 cm.",
   "Quãng đường trong dao động điều hoà", K),

sa("Một vật dao động điều hoà với biên độ 10 cm. Tại li độ nào (tính bằng xentimét, lấy giá trị dương, "
   "làm tròn đến chữ số thập phân thứ hai) thì thế năng bằng 3 lần động năng?",
   "8,66", "Wt = 3Wđ ⟹ x²/A² = 3/4 ⟹ x = A√3/2 = 10 · 0,866 = 8,66 cm.",
   "Năng lượng trong dao động điều hoà", K),

sa("Một vật dao động điều hoà với chu kì 0,48 s. Thời gian ngắn nhất để vật đi từ vị trí cân bằng tới li "
   "độ bằng nửa biên độ bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ hai)?",
   "0,04", "Δt = T/12 = 0,48/12 = 0,04 s.", "Thời gian trong dao động điều hoà", K,
   fig="d_sd_vongtron", cap="Đường tròn pha"),

sa("Một vật dao động điều hoà với biên độ 5 cm và chu kì 0,4 s. Tốc độ trung bình khi vật đi từ vị trí "
   "cân bằng tới biên bằng bao nhiêu xentimét trên giây?",
   "50", "Quãng đường A = 5 cm trong thời gian T/4 = 0,1 s ⟹ v_tb = 5/0,1 = 50 cm/s.",
   "Tốc độ trung bình", TB),

sa("Một vật dao động điều hoà với tần số 2,5 Hz. Trong 2 giây, vật đi qua vị trí cân bằng bao nhiêu lần?",
   "10", "Số chu kì: 2 · 2,5 = 5; mỗi chu kì qua vị trí cân bằng 2 lần ⟹ 5 · 2 = 10 lần.",
   "Chu kì – tần số", TB),

sa("Một vật dao động điều hoà với biên độ 6 cm. Khi động năng bằng 3 lần thế năng thì li độ của vật có độ "
   "lớn bằng bao nhiêu xentimét?",
   "3", "Wđ = 3Wt ⟹ Wt = W/4 ⟹ x²/A² = 1/4 ⟹ x = A/2 = 3 cm.",
   "Năng lượng trong dao động điều hoà", K),
])


# =====================================================================
DE6 = dict(
ma="11C1-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Lực kéo về; con lắc lò xo treo thẳng đứng; khai thác đồ thị li độ – thời gian",
P1=[
mc("Lực kéo về (lực gây ra dao động điều hoà) tác dụng lên vật có biểu thức",
   ["F = kx.", "F = −mω²x.", "F = mω²x.", "F = −mωx."],
   "B",
   "Theo định luật II Newton: F = ma = m·(−ω²x) = −mω²x. Lực kéo về luôn hướng về vị trí cân bằng và có "
   "độ lớn tỉ lệ với li độ.",
   "Lực kéo về", TB),

mc("Một vật khối lượng 0,25 kg dao động điều hoà với tần số góc 20 rad/s và biên độ 4 cm. Độ lớn cực đại "
   "của lực kéo về là",
   ["1,0 N.", "2,0 N.", "4,0 N.", "8,0 N."],
   "C", "F_max = mω²A = 0,25 · 20² · 0,04 = 0,25 · 400 · 0,04 = 4,0 N.",
   "Lực kéo về", TB),

mc("Lực kéo về tác dụng lên vật dao động điều hoà bằng 0 khi vật ở",
   ["vị trí biên.", "vị trí cân bằng.", "li độ bằng nửa biên độ.", "mọi vị trí."],
   "B", "F = −mω²x = 0 khi x = 0, tức tại vị trí cân bằng — cũng là nơi gia tốc bằng 0.",
   "Lực kéo về", D),

mc("Một con lắc lò xo treo thẳng đứng gồm lò xo độ cứng 40 N/m và vật nặng 0,40 kg, lấy g = 10 m/s². Ở vị "
   "trí cân bằng lò xo dãn thêm",
   ["4,0 cm.", "6,0 cm.", "10,0 cm.", "16,0 cm."],
   "C", "Δℓ₀ = mg/k = 0,40 · 10/40 = 0,10 m = 10 cm.",
   "Con lắc lò xo treo thẳng đứng", TB, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Vẫn với con lắc ở câu trên, tần số góc của dao động là",
   ["5 rad/s.", "10 rad/s.", "20 rad/s.", "100 rad/s."],
   "B", "ω = √(k/m) = √(40/0,40) = √100 = 10 rad/s (cũng bằng √(g/Δℓ₀) = √(10/0,10)).",
   "Con lắc lò xo treo thẳng đứng", TB, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Vẫn với con lắc đó, cho vật dao động với biên độ 5 cm. Lực đàn hồi cực đại của lò xo là",
   ["2,0 N.", "4,0 N.", "6,0 N.", "8,0 N."],
   "C",
   "Khi vật ở vị trí thấp nhất, độ dãn lò xo lớn nhất: Δℓ_max = Δℓ₀ + A = 10 + 5 = 15 cm.\n"
   "F_max = k·Δℓ_max = 40 · 0,15 = 6,0 N.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Vẫn với con lắc đó (A = 5 cm, Δℓ₀ = 10 cm), lực đàn hồi cực tiểu của lò xo là",
   ["0 N.", "2,0 N.", "4,0 N.", "6,0 N."],
   "B",
   "Vì A = 5 cm < Δℓ₀ = 10 cm nên lò xo LUÔN dãn; độ dãn nhỏ nhất là Δℓ₀ − A = 5 cm.\n"
   "F_min = 40 · 0,05 = 2,0 N. (Nếu A > Δℓ₀ thì lò xo có lúc bị nén và lực đàn hồi cực tiểu bằng 0.)",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Từ đồ thị li độ – thời gian ở hình bên (A = 4 cm, T = 0,4 s), phương trình vận tốc của vật là",
   ["v = 20πcos(5πt) cm/s.", "v = −20πsin(5πt) cm/s.",
    "v = 20πsin(5πt) cm/s.", "v = −20πcos(5πt) cm/s."],
   "B",
   "x = 4cos(5πt) cm ⟹ v = x′ = −4 · 5π · sin(5πt) = −20π·sin(5πt) cm/s (tốc độ cực đại 20π ≈ 62,8 cm/s).",
   "Đọc đồ thị – viết phương trình", K, fig="d_dt_xt",
   cap="Đồ thị li độ theo thời gian"),

mc("Vẫn với đồ thị đó, tại thời điểm t = 0,1 s vật có",
   ["li độ cực đại, vận tốc bằng 0.", "li độ bằng 0, tốc độ cực đại.",
    "li độ bằng nửa biên độ.", "li độ âm cực đại."],
   "B",
   "t = 0,1 s = T/4. Xuất phát từ biên dương, sau T/4 vật tới vị trí cân bằng: x = 0 và tốc độ cực đại.",
   "Đọc đồ thị li độ – thời gian", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Một vật dao động điều hoà với biên độ 4 cm và chu kì 0,4 s. Gia tốc cực đại của vật gần nhất với",
   ["0,63 m/s².", "6,28 m/s².", "9,87 m/s².", "98,7 m/s²."],
   "C", "ω = 2π/0,4 = 5π rad/s ⟹ a_max = ω²A = (5π)² · 0,04 = 246,7 · 0,04 ≈ 9,87 m/s².",
   "Gia tốc trong dao động điều hoà", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

mc("Một con lắc lò xo nằm ngang dao động điều hoà. Ở vị trí biên, lực đàn hồi của lò xo",
   ["bằng 0.", "có độ lớn cực đại và bằng kA.",
    "có độ lớn cực đại và bằng mg.", "hướng ra xa vị trí cân bằng."],
   "B",
   "Với con lắc lò xo NẰM NGANG, lò xo không biến dạng ở vị trí cân bằng nên lực đàn hồi bằng lực kéo về: "
   "F = k|x|, cực đại bằng kA ở vị trí biên và luôn hướng về vị trí cân bằng.",
   "Con lắc lò xo nằm ngang", TB, fig="d_sd_loxo_ngang", cap="Con lắc lò xo nằm ngang"),

mc("Một con lắc lò xo có k = 100 N/m, dao động với biên độ 5 cm. Lực kéo về cực đại tác dụng lên vật là",
   ["2,5 N.", "5,0 N.", "10,0 N.", "500 N."],
   "B", "F_max = kA = 100 · 0,05 = 5,0 N.", "Lực kéo về", TB),

mc("Một con lắc đơn dao động nhỏ. Đại lượng nào sau đây đóng vai trò “lực kéo về”?",
   ["Toàn bộ trọng lực của vật.", "Lực căng dây.",
    "Thành phần của trọng lực theo phương chuyển động.", "Lực đàn hồi của dây."],
   "C",
   "Trọng lực được phân tích thành hai thành phần: một thành phần theo phương dây (cùng với lực căng gây "
   "ra gia tốc hướng tâm) và một thành phần tiếp tuyến với quỹ đạo — chính thành phần này đóng vai trò "
   "lực kéo về, luôn hướng về vị trí cân bằng.",
   "Con lắc đơn", K, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Một vật dao động điều hoà. Nếu tăng tần số góc lên gấp đôi (giữ nguyên biên độ và khối lượng) thì lực "
   "kéo về cực đại",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "giảm 2 lần."],
   "C", "F_max = mω²A tỉ lệ với BÌNH PHƯƠNG tần số góc ⟹ tăng 4 lần.", "Lực kéo về", K),

mc("Một con lắc lò xo treo thẳng đứng có Δℓ₀ = 4 cm, dao động với biên độ 6 cm. Trong quá trình dao động, "
   "lò xo",
   ["luôn dãn.", "luôn bị nén.", "có lúc dãn, có lúc bị nén.", "không biến dạng."],
   "C",
   "Vì A = 6 cm > Δℓ₀ = 4 cm nên khi vật đi lên quá vị trí lò xo có chiều dài tự nhiên (cách vị trí cân "
   "bằng 4 cm), lò xo bắt đầu bị NÉN. Lực đàn hồi cực tiểu khi đó bằng 0.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Trong dao động điều hoà, lực kéo về và gia tốc",
   ["luôn cùng chiều.", "luôn ngược chiều.", "vuông góc với nhau.", "lệch pha π/2."],
   "A", "F = ma nên lực kéo về luôn CÙNG chiều với gia tốc (và cùng ngược chiều với li độ).",
   "Lực kéo về – gia tốc", TB),

mc("Một vật dao động điều hoà với chu kì 0,4 s. Nếu tăng khối lượng vật lên 4 lần mà giữ nguyên lò xo thì "
   "chu kì trở thành",
   ["0,20 s.", "0,40 s.", "0,80 s.", "1,60 s."],
   "C", "T = 2π√(m/k) ∝ √m ⟹ khối lượng tăng 4 lần thì chu kì tăng 2 lần: T′ = 0,80 s.",
   "Con lắc lò xo", TB),

mc("Với con lắc lò xo treo thẳng đứng, công thức nào sau đây tính đúng chu kì dao động?",
   ["T = 2π√(g/Δℓ₀).", "T = 2π√(Δℓ₀/g).", "T = 2π√(k/m).", "T = 2π√(A/g)."],
   "B",
   "Ở vị trí cân bằng k·Δℓ₀ = mg nên m/k = Δℓ₀/g, thay vào T = 2π√(m/k) được T = 2π√(Δℓ₀/g). "
   "Công thức này rất giống công thức con lắc đơn với Δℓ₀ đóng vai trò chiều dài.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),
],
P2=[
ds("Một con lắc lò xo treo thẳng đứng gồm lò xo độ cứng 40 N/m và vật nặng 0,40 kg; lấy g = 10 m/s². "
   "Cho vật dao động điều hoà với biên độ 5 cm.",
   [("Ở vị trí cân bằng, lò xo dãn thêm 10 cm.", True,
     "Đúng. Δℓ₀ = mg/k = 0,40 · 10/40 = 0,10 m."),
    ("Chu kì dao động của con lắc xấp xỉ 0,63 s.", True,
     "Đúng. ω = √(k/m) = 10 rad/s ⟹ T = 2π/10 ≈ 0,63 s (cũng bằng 2π√(Δℓ₀/g))."),
    ("Trong quá trình dao động, lò xo có lúc bị nén.", False,
     "Sai. Biên độ A = 5 cm nhỏ hơn Δℓ₀ = 10 cm nên độ dãn nhỏ nhất vẫn là 10 − 5 = 5 cm > 0: lò xo "
     "LUÔN dãn."),
    ("Lực đàn hồi của lò xo biến thiên từ 2,0 N tới 6,0 N.", True,
     "Đúng. F_min = k(Δℓ₀ − A) = 40 · 0,05 = 2,0 N; F_max = k(Δℓ₀ + A) = 40 · 0,15 = 6,0 N.")],
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

ds("Xét lực kéo về trong dao động điều hoà của một vật khối lượng m, tần số góc ω, biên độ A.",
   [("Lực kéo về có biểu thức F = −mω²x và luôn hướng về vị trí cân bằng.", True,
     "Đúng, suy ra từ định luật II Newton và hệ thức a = −ω²x."),
    ("Lực kéo về bằng 0 khi vật đi qua vị trí cân bằng.", True,
     "Đúng. x = 0 ⟹ F = 0 (đồng thời gia tốc cũng bằng 0 còn tốc độ cực đại)."),
    ("Độ lớn cực đại của lực kéo về là mω²A.", True,
     "Đúng, đạt được ở hai vị trí biên."),
    ("Lực kéo về luôn ngược chiều với gia tốc của vật.", False,
     "Sai. F = ma nên lực kéo về luôn CÙNG chiều với gia tốc; cả hai cùng ngược chiều với li độ.")],
   "Lực kéo về", TB),

ds("Hình bên là đồ thị li độ theo thời gian của một vật dao động điều hoà (A = 4 cm, T = 0,4 s).",
   [("Tần số góc của dao động là 5π rad/s.", True,
     "Đúng. ω = 2π/T = 2π/0,4 = 5π rad/s ≈ 15,7 rad/s."),
    ("Phương trình vận tốc của vật là v = −20π·sin(5πt) cm/s.", True,
     "Đúng. v = x′ với x = 4cos(5πt) cm."),
    ("Gia tốc cực đại của vật xấp xỉ 9,87 m/s².", True,
     "Đúng. a_max = ω²A = (5π)² · 0,04 ≈ 246,7 · 0,04 ≈ 9,87 m/s²."),
    ("Tại thời điểm t = 0,1 s, vật ở vị trí biên âm.", False,
     "Sai. t = 0,1 s = T/4; xuất phát từ biên dương, sau T/4 vật tới VỊ TRÍ CÂN BẰNG (x = 0) chứ không "
     "phải biên âm (phải mất T/2 mới tới biên âm).")],
   "Khai thác đồ thị li độ – thời gian", K, fig="d_dt_xt",
   cap="Đồ thị li độ theo thời gian"),

ds("So sánh con lắc lò xo nằm ngang và con lắc lò xo treo thẳng đứng.",
   [("Với con lắc nằm ngang, ở vị trí cân bằng lò xo không biến dạng.", True,
     "Đúng, vì trọng lực vuông góc với phương dao động nên không làm lò xo biến dạng."),
    ("Với con lắc treo thẳng đứng, ở vị trí cân bằng lò xo đã dãn một đoạn Δℓ₀ = mg/k.", True,
     "Đúng, đó là điều kiện cân bằng của vật."),
    ("Chu kì dao động của hai loại con lắc đều tính bằng T = 2π√(m/k).", True,
     "Đúng. Trọng lực chỉ làm dịch vị trí cân bằng chứ không ảnh hưởng tới chu kì."),
    ("Với con lắc treo thẳng đứng, lực đàn hồi của lò xo luôn bằng lực kéo về.", False,
     "Sai. Lực kéo về là HỢP LỰC của trọng lực và lực đàn hồi, có độ lớn k|x| tính từ vị trí cân bằng. "
     "Lực đàn hồi riêng nó bằng k|Δℓ₀ + x| — hai đại lượng khác nhau. Chỉ với con lắc NẰM NGANG thì hai "
     "lực này mới trùng nhau.")],
   "So sánh hai loại con lắc lò xo", RK,
   fig="d_sd_loxo_ngang", cap="Con lắc lò xo nằm ngang"),
],
P3=[
sa("Một vật khối lượng 0,25 kg dao động điều hoà với tần số góc 20 rad/s và biên độ 4 cm. Độ lớn cực đại "
   "của lực kéo về bằng bao nhiêu niutơn (làm tròn đến chữ số thập phân thứ nhất)?",
   "4,0", "F_max = mω²A = 0,25 · 400 · 0,04 = 4,0 N.", "Lực kéo về", TB),

sa("Một con lắc lò xo treo thẳng đứng gồm lò xo 40 N/m và vật 0,40 kg, g = 10 m/s². Ở vị trí cân bằng lò "
   "xo dãn thêm bao nhiêu xentimét?",
   "10", "Δℓ₀ = mg/k = 0,40 · 10/40 = 0,10 m = 10 cm.", "Con lắc lò xo treo thẳng đứng", TB,
   fig="d_sd_loxo_doc", cap="Con lắc lò xo treo thẳng đứng"),

sa("Vẫn với con lắc đó, cho dao động với biên độ 5 cm. Lực đàn hồi cực đại của lò xo bằng bao nhiêu "
   "niutơn (làm tròn đến chữ số thập phân thứ nhất)?",
   "6,0", "Δℓ_max = Δℓ₀ + A = 15 cm ⟹ F_max = 40 · 0,15 = 6,0 N.",
   "Con lắc lò xo treo thẳng đứng", K),

sa("Vẫn với con lắc đó, lực đàn hồi cực tiểu của lò xo bằng bao nhiêu niutơn (làm tròn đến chữ số thập "
   "phân thứ nhất)?",
   "2,0",
   "Vì A = 5 cm < Δℓ₀ = 10 cm nên lò xo luôn dãn; Δℓ_min = 10 − 5 = 5 cm ⟹ F_min = 40 · 0,05 = 2,0 N.",
   "Con lắc lò xo treo thẳng đứng", K),

sa("Một vật dao động điều hoà với biên độ 4 cm và chu kì 0,4 s. Gia tốc cực đại của vật bằng bao nhiêu "
   "m/s² (làm tròn đến chữ số thập phân thứ hai)?",
   "9,87", "ω = 5π rad/s ⟹ a_max = ω²A = (5π)² · 0,04 ≈ 9,87 m/s².",
   "Gia tốc trong dao động điều hoà", TB, fig="d_dt_xt", cap="Đồ thị li độ theo thời gian"),

sa("Một con lắc lò xo có k = 100 N/m dao động với biên độ 5 cm. Lực kéo về cực đại tác dụng lên vật bằng "
   "bao nhiêu niutơn (làm tròn đến chữ số thập phân thứ nhất)?",
   "5,0", "F_max = kA = 100 · 0,05 = 5,0 N.", "Lực kéo về", TB),
])


CLD_TBL = ("Số liệu thí nghiệm đo gia tốc trọng trường bằng con lắc đơn",
           ["ℓ (m)", "0,40", "0,60", "0,80", "1,00", "1,20"],
           [["T (s)", "1,27", "1,55", "1,79", "2,01", "2,20"],
            ["T² (s²)", "1,61", "2,42", "3,22", "4,03", "4,83"]])


# =====================================================================
DE7 = dict(
ma="11C1-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Thí nghiệm đo gia tốc trọng trường bằng con lắc đơn; xử lí số liệu và đồ thị",
P1=[
mc("Trong thí nghiệm đo gia tốc trọng trường bằng con lắc đơn, người ta đo chu kì T ứng với các chiều dài "
   "dây ℓ khác nhau. Để có một đồ thị ĐƯỜNG THẲNG, nên vẽ",
   ["T theo ℓ.", "T² theo ℓ.", "T theo ℓ².", "T theo 1/ℓ."],
   "B",
   "Từ T = 2π√(ℓ/g) suy ra T² = (4π²/g)·ℓ — hàm bậc nhất thuần nhất của ℓ, đồ thị là đường thẳng đi qua "
   "gốc toạ độ với hệ số góc 4π²/g. Đồ thị T theo ℓ là đường cong (căn bậc hai).",
   "Thiết kế thí nghiệm – biến đổi đồ thị", K, fig="d_dt_T2_l",
   cap="Đồ thị T² theo ℓ dựng từ số liệu thực nghiệm"),

mc("Với bộ số liệu ở bảng bên, hệ số góc của đường thẳng T² theo ℓ gần nhất với",
   ["2,0 s²/m.", "3,2 s²/m.", "4,0 s²/m.", "4,8 s²/m."],
   "C",
   "Lấy hai điểm biên: k = (4,83 − 1,61)/(1,20 − 0,40) = 3,22/0,80 ≈ 4,03 s²/m.\n"
   "(Có thể kiểm tra bằng từng cặp: 1,61/0,40 = 4,03; 4,03/1,00 = 4,03 ✓)",
   "Xử lí số liệu thực nghiệm", K, tbl=CLD_TBL, fig="d_dt_T2_l",
   cap="Đồ thị T² theo ℓ"),

mc("Từ hệ số góc đó, gia tốc trọng trường xác định được gần nhất với",
   ["9,60 m/s².", "9,80 m/s².", "10,00 m/s².", "10,20 m/s²."],
   "B",
   "T² = (4π²/g)·ℓ ⟹ g = 4π²/k = 4 · 9,8696/4,03 = 39,478/4,03 ≈ 9,80 m/s².",
   "Xử lí số liệu thực nghiệm", K, tbl=CLD_TBL, fig="d_dt_T2_l", cap="Đồ thị T² theo ℓ"),

mc("Trong thí nghiệm trên, vì sao người ta thường đo thời gian của 10 (hoặc 20) dao động rồi chia cho số "
   "dao động thay vì đo trực tiếp một chu kì?",
   ["Để con lắc dao động ổn định hơn.",
    "Để giảm ảnh hưởng của sai số khi bấm giờ, vì sai số đó được chia cho số dao động.",
    "Để tăng biên độ dao động.",
    "Để chu kì không phụ thuộc chiều dài dây."],
   "B",
   "Sai số khi bấm đồng hồ (khoảng 0,2 s do phản xạ của người) là như nhau dù đo 1 hay 20 dao động. Chia "
   "cho 20 thì sai số của mỗi chu kì chỉ còn 0,01 s. Đây là kĩ thuật giảm SAI SỐ NGẪU NHIÊN cơ bản.",
   "Sai số trong thí nghiệm", K, fig="d_sd_do_chuki",
   cap="Đo chu kì con lắc đơn bằng cổng quang điện và đồng hồ hiện số"),

mc("Trong thí nghiệm đo g bằng con lắc đơn, phải giữ biên độ góc nhỏ (thường dưới 10°) vì",
   ["dây treo dễ đứt khi biên độ lớn.",
    "công thức T = 2π√(ℓ/g) chỉ đúng cho dao động nhỏ.",
    "biên độ lớn làm con lắc dao động nhanh hơn nhiều lần.",
    "cổng quang điện không đo được khi biên độ lớn."],
   "B",
   "Con lắc đơn chỉ dao động ĐIỀU HOÀ khi biên độ góc nhỏ (sinα ≈ α). Với biên độ lớn, chu kì tăng lên "
   "chút ít và công thức trên cho kết quả sai lệch — một sai số hệ thống.",
   "Điều kiện áp dụng công thức", K, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Một học sinh đo được chiều dài dây 1,00 m và thời gian 20 dao động là 40,1 s. Gia tốc trọng trường "
   "học sinh đó tính được gần nhất với",
   ["9,60 m/s².", "9,81 m/s².", "9,95 m/s².", "10,10 m/s²."],
   "B",
   "T = 40,1/20 = 2,005 s ⟹ g = 4π²ℓ/T² = 39,478 · 1,00/(2,005)² = 39,478/4,020 ≈ 9,82 m/s², "
   "gần nhất với 9,81 m/s².",
   "Xử lí số liệu thực nghiệm", K, fig="d_sd_do_chuki", cap="Bộ thí nghiệm đo chu kì"),

mc("Nếu trong thí nghiệm, học sinh đo chiều dài dây nhưng QUÊN cộng thêm bán kính của quả nặng thì giá "
   "trị g tính được sẽ",
   ["lớn hơn giá trị thật.", "nhỏ hơn giá trị thật.",
    "không đổi.", "lúc lớn hơn lúc nhỏ hơn."],
   "B",
   "Chiều dài thật của con lắc đơn là từ điểm treo tới TÂM quả nặng. Quên bán kính ⟹ ℓ dùng để tính nhỏ "
   "hơn thật ⟹ g = 4π²ℓ/T² tính được NHỎ hơn giá trị thật. Đây là một sai số hệ thống điển hình.",
   "Sai số hệ thống", RK, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Đường thẳng T² theo ℓ trong thí nghiệm đi qua gốc toạ độ. Nếu do sai số hệ thống mà đường thẳng cắt "
   "trục T² tại một giá trị dương thì nguyên nhân có thể là",
   ["đồng hồ chạy nhanh.",
    "chiều dài dây đo được luôn nhỏ hơn chiều dài thật một lượng không đổi.",
    "quả nặng quá nhẹ.", "biên độ dao động quá nhỏ."],
   "B",
   "Nếu ℓ_thật = ℓ_đo + c với c > 0 không đổi thì T² = (4π²/g)(ℓ_đo + c) = (4π²/g)ℓ_đo + (4π²/g)c — "
   "đường thẳng bị “nâng lên”, cắt trục T² tại giá trị dương. Đây chính là dấu hiệu nhận biết sai số hệ "
   "thống trong phép đo chiều dài.",
   "Sai số hệ thống", RK, fig="d_dt_T2_l", cap="Đồ thị T² theo ℓ"),

mc("Với bộ số liệu ở bảng, nếu dùng dây dài 1,60 m thì chu kì dao động dự đoán gần nhất với",
   ["2,20 s.", "2,40 s.", "2,54 s.", "2,80 s."],
   "C", "T² = 4,03 · 1,60 = 6,45 s² ⟹ T = √6,45 ≈ 2,54 s.",
   "Dự đoán từ mô hình thực nghiệm", K, tbl=CLD_TBL),

mc("Chu kì con lắc đơn tại nơi có g = 9,8 m/s² với dây dài 1,0 m là 2,0 s. Muốn chu kì là 1,0 s thì chiều "
   "dài dây phải là",
   ["0,125 m.", "0,250 m.", "0,500 m.", "2,000 m."],
   "B", "T ∝ √ℓ ⟹ chu kì giảm 2 lần thì chiều dài giảm 4 lần: ℓ = 1,0/4 = 0,25 m.",
   "Con lắc đơn", TB),

mc("Một con lắc đơn dao động với chu kì 2,0 s tại mặt đất. Đưa lên nơi có gia tốc trọng trường bằng 0,25 "
   "lần giá trị ở mặt đất thì chu kì trở thành",
   ["1,0 s.", "2,0 s.", "4,0 s.", "8,0 s."],
   "C", "T ∝ 1/√g ⟹ g giảm 4 lần thì T tăng √4 = 2 lần: T′ = 4,0 s.", "Con lắc đơn", TB),

mc("Trong thí nghiệm đo g bằng con lắc đơn, đại lượng nào KHÔNG cần đo?",
   ["Chiều dài dây treo.", "Thời gian của một số dao động.",
    "Khối lượng quả nặng.", "Số dao động đã đếm."],
   "C",
   "Công thức g = 4π²ℓ/T² không chứa khối lượng. Đây cũng là ưu điểm của phương pháp con lắc đơn: không "
   "cần cân quả nặng.",
   "Thiết kế thí nghiệm", TB, fig="d_sd_do_chuki", cap="Bộ thí nghiệm đo chu kì"),

mc("Cổng quang điện được dùng trong thí nghiệm đo chu kì con lắc nhằm",
   ["làm con lắc dao động lâu hơn.",
    "ghi thời gian tự động, loại bỏ sai số do phản xạ của người bấm đồng hồ.",
    "đo chiều dài dây chính xác hơn.",
    "giữ biên độ dao động không đổi."],
   "B",
   "Người bấm đồng hồ luôn có độ trễ phản xạ khoảng 0,2 s; cổng quang điện ghi thời gian tự động với độ "
   "chính xác tới phần nghìn giây, loại bỏ hoàn toàn nguồn sai số này.",
   "Dụng cụ thí nghiệm", TB, fig="d_sd_do_chuki",
   cap="Cổng quang điện và đồng hồ đo thời gian hiện số"),

mc("Hai con lắc đơn có chiều dài 1,00 m và 1,44 m dao động tại cùng một nơi. Tỉ số chu kì T₂/T₁ bằng",
   ["1,10.", "1,20.", "1,44.", "2,07."],
   "B", "T ∝ √ℓ ⟹ T₂/T₁ = √(1,44/1,00) = 1,20.", "Con lắc đơn", TB),

mc("Một con lắc đơn có chu kì 2,00 s. Nếu tăng chiều dài dây thêm 21% thì chu kì mới gần nhất với",
   ["2,10 s.", "2,20 s.", "2,42 s.", "1,82 s."],
   "B",
   "T ∝ √ℓ ⟹ T′ = T·√(ℓ′/ℓ) = 2,00 · √1,21 = 2,00 · 1,10 = 2,20 s.\n"
   "Bẫy: cộng thẳng 21% vào chu kì cho 2,42 s; lấy một nửa của 21% cho 2,10 s.",
   "Con lắc đơn", K),

mc("Trong bốn phép đo sau của thí nghiệm đo g, phép đo nào gây sai số lớn nhất nếu thực hiện cẩu thả?",
   ["Đo khối lượng quả nặng.", "Đo chiều dài dây treo.",
    "Đếm số dao động.", "Đo nhiệt độ phòng."],
   "B",
   "Khối lượng và nhiệt độ không xuất hiện trong công thức g = 4π²ℓ/T². Đếm số dao động dễ chính xác. "
   "Còn chiều dài dây (phải tính tới TÂM quả nặng) rất dễ đo sai và ảnh hưởng trực tiếp tới g.",
   "Phân tích sai số", K),

mc("Chu kì của con lắc đơn dài 1,0 m tại nơi có g = 9,8 m/s² là 2,006 s. Nếu đồng hồ quả lắc dùng con lắc "
   "này chạy đúng ở mặt đất, khi đưa lên núi cao (g giảm) thì đồng hồ sẽ",
   ["chạy nhanh.", "chạy chậm.", "chạy đúng.", "dừng lại."],
   "B",
   "g giảm ⟹ T tăng ⟹ mỗi “giây” của đồng hồ dài hơn giây thật ⟹ đồng hồ đếm được ít hơn: đồng hồ chạy "
   "CHẬM.",
   "Con lắc đơn – thực tiễn", K),

mc("Nếu vẽ đồ thị T² theo ℓ và đường thẳng thu được có hệ số góc 4,03 s²/m thì đơn vị của hệ số góc đó "
   "được giải thích là",
   ["s²/m, đúng bằng 4π²/g.", "s/m, đúng bằng 2π/√g.",
    "m/s², đúng bằng g/(4π²).", "không có đơn vị."],
   "A", "Từ T² = (4π²/g)·ℓ, hệ số góc là 4π²/g với đơn vị s²/m.",
   "Xử lí số liệu thực nghiệm", TB, fig="d_dt_T2_l", cap="Đồ thị T² theo ℓ"),
],
P2=[
ds("Bảng bên là số liệu của một nhóm học sinh khi đo gia tốc trọng trường bằng con lắc đơn.",
   [("Muốn có đồ thị đường thẳng, phải vẽ T² theo ℓ chứ không phải T theo ℓ.", True,
     "Đúng. T² = (4π²/g)·ℓ là hàm bậc nhất của ℓ; còn T = 2π√(ℓ/g) là hàm căn bậc hai."),
    ("Hệ số góc của đường thẳng T² theo ℓ vào khoảng 4,03 s²/m.", True,
     "Đúng. k = (4,83 − 1,61)/(1,20 − 0,40) = 4,03 s²/m; kiểm tra bằng từng cặp đều cho cùng giá trị."),
    ("Gia tốc trọng trường tính được vào khoảng 9,80 m/s².", True,
     "Đúng. g = 4π²/k = 39,478/4,03 ≈ 9,80 m/s²."),
    ("Đường thẳng T² theo ℓ cắt trục tung tại một giá trị dương, chứng tỏ phép đo rất chính xác.", False,
     "Sai. Với phép đo tốt, đường thẳng phải đi qua GỐC toạ độ (vì ℓ = 0 thì T = 0). Việc nó cắt trục "
     "tung ở giá trị dương lại là DẤU HIỆU của sai số hệ thống trong phép đo chiều dài.")],
   "Xử lí số liệu thực nghiệm", K, tbl=CLD_TBL, fig="d_dt_T2_l",
   cap="Đồ thị T² theo ℓ"),

ds("Xét cách bố trí và các nguồn sai số trong thí nghiệm đo g bằng con lắc đơn.",
   [("Đo thời gian của 20 dao động rồi chia cho 20 giúp giảm sai số ngẫu nhiên khi bấm đồng hồ.", True,
     "Đúng. Sai số bấm giờ (~0,2 s) không đổi nhưng khi chia cho 20 thì sai số của mỗi chu kì chỉ còn "
     "khoảng 0,01 s."),
    ("Phải giữ biên độ góc nhỏ vì công thức T = 2π√(ℓ/g) chỉ đúng cho dao động nhỏ.", True,
     "Đúng. Với biên độ góc lớn, chu kì tăng lên và công thức cho kết quả sai lệch."),
    ("Chiều dài dây phải đo từ điểm treo tới TÂM quả nặng.", True,
     "Đúng. Quên bán kính quả nặng sẽ làm ℓ nhỏ hơn thật, dẫn tới g tính được nhỏ hơn thật."),
    ("Cần cân chính xác khối lượng quả nặng vì g phụ thuộc khối lượng đó.", False,
     "Sai. Công thức g = 4π²ℓ/T² không chứa khối lượng; đó chính là ưu điểm của phương pháp này.")],
   "Sai số trong thí nghiệm", K, fig="d_sd_do_chuki",
   cap="Bộ thí nghiệm đo chu kì con lắc đơn"),

ds("Một học sinh đo được chiều dài dây 1,00 m và thời gian 20 dao động là 40,1 s.",
   [("Chu kì dao động của con lắc là 2,005 s.", True,
     "Đúng. T = 40,1/20 = 2,005 s."),
    ("Gia tốc trọng trường tính được vào khoảng 9,82 m/s².", True,
     "Đúng. g = 4π²ℓ/T² = 39,478/4,020 ≈ 9,82 m/s²."),
    ("Nếu học sinh quên cộng bán kính quả nặng (khoảng 1,0 cm) vào chiều dài dây thì giá trị g tính được "
     "sẽ nhỏ hơn thật.", True,
     "Đúng. ℓ thật là 1,01 m, cho g = 39,478 · 1,01/4,020 ≈ 9,92 m/s². Dùng ℓ = 1,00 m cho kết quả nhỏ "
     "hơn khoảng 1%."),
    ("Nếu học sinh chỉ đo thời gian của 1 dao động thì kết quả cũng chính xác như khi đo 20 dao động.", False,
     "Sai. Sai số bấm giờ khoảng 0,2 s sẽ gây sai số 10% cho một chu kì 2 s, kéo theo sai số khoảng 20% "
     "cho g — lớn hơn rất nhiều so với khi đo 20 dao động.")],
   "Xử lí số liệu và sai số", RK, fig="d_sd_do_chuki",
   cap="Bộ thí nghiệm đo chu kì"),

ds("Xét ảnh hưởng của chiều dài dây và gia tốc trọng trường tới chu kì con lắc đơn dao động nhỏ.",
   [("Muốn chu kì giảm một nửa, phải giảm chiều dài dây đi bốn lần.", True,
     "Đúng. T ∝ √ℓ nên ℓ giảm 4 lần thì T giảm 2 lần."),
    ("Tăng chiều dài dây thêm 21% thì chu kì tăng khoảng 10%.", True,
     "Đúng. T′/T = √1,21 = 1,10, tức tăng 10%."),
    ("Đưa đồng hồ quả lắc lên núi cao thì đồng hồ chạy chậm lại.", True,
     "Đúng. g giảm nên chu kì tăng, đồng hồ đếm được ít “giây” hơn trong cùng một khoảng thời gian thật."),
    ("Thay quả nặng bằng quả khác nặng gấp đôi thì chu kì tăng √2 lần.", False,
     "Sai. Chu kì con lắc đơn không phụ thuộc khối lượng: T = 2π√(ℓ/g) không chứa m. "
     "(Quy tắc T ∝ √m là của con lắc LÒ XO.)")],
   "Con lắc đơn", K, fig="d_sd_cldon", cap="Con lắc đơn"),
],
P3=[
sa("Từ bộ số liệu thí nghiệm đo g bằng con lắc đơn, hệ số góc của đường thẳng T² theo ℓ bằng bao nhiêu "
   "s²/m (làm tròn đến chữ số thập phân thứ hai)?",
   "4,03", "k = (4,83 − 1,61)/(1,20 − 0,40) = 3,22/0,80 ≈ 4,03 s²/m.",
   "Xử lí số liệu thực nghiệm", K, tbl=CLD_TBL, fig="d_dt_T2_l", cap="Đồ thị T² theo ℓ"),

sa("Từ hệ số góc đó, gia tốc trọng trường xác định được bằng bao nhiêu m/s² (làm tròn đến chữ số thập "
   "phân thứ hai)?",
   "9,80", "g = 4π²/k = 39,478/4,03 ≈ 9,80 m/s².", "Xử lí số liệu thực nghiệm", K, tbl=CLD_TBL),

sa("Một học sinh đo chiều dài dây 1,00 m và thời gian 20 dao động là 40,1 s. Gia tốc trọng trường tính "
   "được bằng bao nhiêu m/s² (làm tròn đến chữ số thập phân thứ hai)?",
   "9,82", "T = 40,1/20 = 2,005 s ⟹ g = 4π²ℓ/T² = 39,478/4,020 ≈ 9,82 m/s².",
   "Xử lí số liệu thực nghiệm", K),

sa("Với hệ số góc 4,03 s²/m, chu kì dự đoán của con lắc đơn dài 1,60 m bằng bao nhiêu giây (làm tròn đến "
   "chữ số thập phân thứ hai)?",
   "2,54", "T² = 4,03 · 1,60 = 6,448 s² ⟹ T = √6,448 ≈ 2,54 s.",
   "Dự đoán từ mô hình thực nghiệm", K, tbl=CLD_TBL),

sa("Một con lắc đơn dài 1,0 m có chu kì 2,0 s. Muốn chu kì là 1,0 s thì chiều dài dây phải bằng bao nhiêu "
   "mét (làm tròn đến chữ số thập phân thứ hai)?",
   "0,25", "T ∝ √ℓ ⟹ chu kì giảm 2 lần thì chiều dài giảm 4 lần: ℓ = 1,0/4 = 0,25 m.",
   "Con lắc đơn", TB),

sa("Hai con lắc đơn dài 1,00 m và 1,44 m dao động tại cùng một nơi. Tỉ số chu kì của con lắc dài chia cho "
   "con lắc ngắn bằng bao nhiêu (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,2", "T ∝ √ℓ ⟹ tỉ số = √(1,44/1,00) = 1,2.", "Con lắc đơn", TB),
])


# =====================================================================
DE8 = dict(
ma="11C1-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Dao động tắt dần, dao động cưỡng bức và hiện tượng cộng hưởng",
P1=[
mc("Nguyên nhân làm cho dao động của một con lắc trong không khí tắt dần là",
   ["lực kéo về giảm dần.", "lực cản của môi trường làm cơ năng giảm dần.",
    "khối lượng vật giảm dần.", "chu kì dao động tăng dần."],
   "B",
   "Công của lực cản luôn âm nên cơ năng của hệ giảm dần; vì W = ½mω²A² nên biên độ cũng giảm dần theo.",
   "Dao động tắt dần", D, fig="d_dt_tatdan", cap="Đồ thị li độ của dao động tắt dần"),

mc("Hình bên là đồ thị li độ theo thời gian của một dao động tắt dần. Biên độ ban đầu và chu kì dao động "
   "lần lượt là",
   ["6 cm và 0,6 s.", "3 cm và 0,6 s.", "6 cm và 1,2 s.", "12 cm và 0,6 s."],
   "A",
   "Giá trị lớn nhất của li độ ở đầu đồ thị là 6 cm; khoảng cách giữa hai đỉnh liên tiếp là 0,6 s ⟹ "
   "A₀ = 6 cm, T = 0,6 s (chu kì của dao động tắt dần coi như không đổi khi lực cản nhỏ).",
   "Đọc đồ thị dao động tắt dần", TB, fig="d_dt_tatdan",
   cap="Đồ thị li độ của dao động tắt dần"),

mc("Vẫn với đồ thị trên, trong 6 giây đầu vật thực hiện được số dao động là",
   ["6.", "10.", "12.", "36."],
   "B", "Số dao động = t/T = 6/0,6 = 10 dao động.",
   "Đọc đồ thị dao động tắt dần", TB, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

mc("Vẫn với đồ thị đó, tại thời điểm t = 2,4 s biên độ dao động còn khoảng 2,2 cm. Cơ năng của hệ khi đó "
   "so với cơ năng ban đầu còn khoảng",
   ["13%.", "27%.", "37%.", "50%."],
   "A",
   "Cơ năng tỉ lệ với BÌNH PHƯƠNG biên độ: W/W₀ = (A/A₀)² = (2,2/6)² ≈ 0,134, tức khoảng 13%.\n"
   "Bẫy: lấy tỉ số biên độ 2,2/6 ≈ 37% mà quên bình phương.",
   "Dao động tắt dần – năng lượng", K, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

mc("Trong dao động tắt dần, đại lượng nào sau đây gần như KHÔNG đổi (khi lực cản nhỏ)?",
   ["Biên độ.", "Cơ năng.", "Chu kì.", "Tốc độ cực đại."],
   "C",
   "Lực cản nhỏ chỉ làm biên độ và cơ năng giảm dần, còn chu kì (do đó cả tần số) gần như giữ nguyên giá "
   "trị của dao động riêng.",
   "Dao động tắt dần", TB, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

mc("Dao động cưỡng bức ở giai đoạn ổn định có tần số bằng",
   ["tần số riêng của hệ.", "tần số của lực cưỡng bức.",
    "trung bình cộng của hai tần số trên.", "hiệu của hai tần số trên."],
   "B",
   "Sau giai đoạn chuyển tiếp, hệ dao động với đúng tần số của ngoại lực cưỡng bức, bất kể tần số riêng "
   "của nó là bao nhiêu. Tần số riêng chỉ quyết định BIÊN ĐỘ của dao động cưỡng bức.",
   "Dao động cưỡng bức", TB),

mc("Hình bên là đường biểu diễn biên độ dao động cưỡng bức theo tần số của ngoại lực, ứng với hai mức ma "
   "sát. Tần số riêng của hệ là",
   ["1 Hz.", "2 Hz.", "3 Hz.", "4 Hz."],
   "B", "Cả hai đường đều đạt cực đại tại f = 2 Hz — đó chính là tần số riêng f₀ của hệ.",
   "Đọc đường cộng hưởng", TB, fig="d_dt_conghuong",
   cap="Đường cộng hưởng ứng với hai mức ma sát"),

mc("Vẫn với hình trên, đường có đỉnh cao và nhọn hơn ứng với",
   ["ma sát lớn hơn.", "ma sát nhỏ hơn.", "khối lượng lớn hơn.", "biên độ ngoại lực nhỏ hơn."],
   "B",
   "Ma sát càng nhỏ thì năng lượng mất đi mỗi chu kì càng ít, biên độ tại cộng hưởng càng lớn và đỉnh "
   "cộng hưởng càng nhọn. Ma sát lớn làm đỉnh thấp và tù đi.",
   "Đọc đường cộng hưởng", K, fig="d_dt_conghuong", cap="Đường cộng hưởng"),

mc("Hiện tượng cộng hưởng xảy ra rõ nét nhất khi",
   ["biên độ ngoại lực lớn và ma sát lớn.",
    "tần số ngoại lực bằng tần số riêng và ma sát nhỏ.",
    "tần số ngoại lực lớn hơn nhiều tần số riêng.",
    "hệ không chịu ngoại lực."],
   "B",
   "Điều kiện cộng hưởng là f = f₀; mức độ “rõ nét” (đỉnh cao và nhọn) phụ thuộc ma sát: ma sát càng nhỏ, "
   "cộng hưởng càng rõ.",
   "Hiện tượng cộng hưởng", TB, fig="d_dt_conghuong", cap="Đường cộng hưởng"),

mc("Một con lắc đơn treo trên trần một toa tàu, có chu kì dao động riêng 1,5 s. Đường ray gồm các thanh "
   "dài 12,5 m. Con lắc dao động mạnh nhất khi tàu chạy với tốc độ",
   ["6,25 m/s.", "8,33 m/s.", "12,5 m/s.", "18,75 m/s."],
   "B",
   "Mỗi khi qua một chỗ nối ray, toa tàu bị “xóc” một lần, tạo ra ngoại lực cưỡng bức có chu kì "
   "T = d/v.\nCộng hưởng khi T = T₀ ⟹ v = d/T₀ = 12,5/1,5 ≈ 8,33 m/s (khoảng 30 km/h).",
   "Cộng hưởng – bài toán thực tiễn", K, fig="d_sd_congHuong_thuctien",
   cap="Cộng hưởng trong thực tiễn"),

mc("Trường hợp nào sau đây cộng hưởng là CÓ LỢI?",
   ["Cầu bị rung mạnh khi đoàn người bước đều qua.",
    "Hộp cộng hưởng của đàn ghi ta làm âm thanh to hơn.",
    "Bệ máy rung mạnh khi động cơ chạy ở một tốc độ nhất định.",
    "Toa tàu rung lắc mạnh ở một tốc độ nhất định."],
   "B",
   "Hộp đàn được thiết kế để cộng hưởng với dao động của dây, làm âm thanh to và ấm hơn. Ba trường hợp "
   "còn lại đều là cộng hưởng có hại, cần tránh bằng cách thay đổi tần số riêng hoặc tăng lực cản.",
   "Cộng hưởng – lợi và hại", TB, fig="d_sd_congHuong_thuctien",
   cap="Cộng hưởng khi đoàn người bước đều qua cầu"),

mc("Vì sao khi đi qua cầu, đoàn quân được lệnh phải bước không đều nhau?",
   ["Để đi nhanh hơn.",
    "Để tránh tạo ra ngoại lực tuần hoàn có tần số trùng tần số riêng của cầu.",
    "Để giảm khối lượng tác dụng lên cầu.",
    "Để giữ trật tự."],
   "B",
   "Bước đều tạo ra một ngoại lực tuần hoàn; nếu tần số bước trùng với tần số riêng của cầu thì xảy ra "
   "cộng hưởng, biên độ dao động của cầu tăng rất mạnh và có thể gây sập cầu.",
   "Cộng hưởng – thực tiễn", TB, fig="d_sd_congHuong_thuctien",
   cap="Đoàn người bước đều qua cầu"),

mc("Một hệ dao động có tần số riêng 5 Hz, chịu tác dụng lần lượt của bốn ngoại lực tuần hoàn cùng biên độ "
   "với tần số 2 Hz; 4 Hz; 5 Hz; 8 Hz. Biên độ dao động cưỡng bức lớn nhất ứng với ngoại lực có tần số",
   ["2 Hz.", "4 Hz.", "5 Hz.", "8 Hz."],
   "C", "Biên độ cưỡng bức đạt cực đại khi tần số ngoại lực bằng tần số riêng: f = f₀ = 5 Hz.",
   "Hiện tượng cộng hưởng", TB),

mc("Trong dao động tắt dần, sau mỗi chu kì cơ năng của hệ",
   ["không đổi.", "giảm một lượng bằng công của lực cản.",
    "tăng do lực cản sinh công dương.", "giảm rồi lại tăng."],
   "B", "Độ giảm cơ năng đúng bằng độ lớn công của lực cản thực hiện trong chu kì đó.",
   "Dao động tắt dần – năng lượng", TB),

mc("Một dao động tắt dần có biên độ giảm còn một nửa sau một khoảng thời gian nào đó. Khi đó cơ năng của "
   "hệ còn",
   ["1/2.", "1/4.", "1/8.", "3/4."],
   "B", "W ∝ A² ⟹ A giảm 2 lần thì W giảm 4 lần, tức còn 1/4 giá trị ban đầu.",
   "Dao động tắt dần – năng lượng", TB),

mc("Muốn giảm tác hại của cộng hưởng đối với một máy móc, biện pháp nào sau đây KHÔNG hiệu quả?",
   ["Thay đổi tần số riêng của bệ máy.", "Tăng ma sát, dùng đệm giảm chấn.",
    "Tránh cho máy chạy ở tốc độ gây cộng hưởng.", "Tăng biên độ của ngoại lực cưỡng bức."],
   "D",
   "Tăng biên độ ngoại lực chỉ làm dao động mạnh hơn nữa. Ba biện pháp còn lại đều nhằm hoặc tách f khỏi "
   "f₀, hoặc làm tù đỉnh cộng hưởng.",
   "Cộng hưởng – lợi và hại", TB),

mc("Dao động duy trì khác dao động cưỡng bức ở chỗ",
   ["dao động duy trì có biên độ giảm dần.",
    "dao động duy trì được bù năng lượng đúng bằng phần mất đi và giữ nguyên tần số riêng của hệ.",
    "dao động duy trì không cần cung cấp năng lượng.",
    "dao động duy trì có tần số bằng tần số ngoại lực."],
   "B",
   "Trong dao động duy trì (ví dụ đồng hồ quả lắc), người ta cung cấp năng lượng đúng bằng phần mất đi "
   "sau mỗi chu kì để biên độ không đổi, nhưng hệ vẫn dao động với TẦN SỐ RIÊNG của nó.",
   "Dao động duy trì – cưỡng bức", K),

mc("Một con lắc lò xo dao động tắt dần trong không khí. So với khi dao động trong chân không (nếu có thể), "
   "chu kì dao động sẽ",
   ["nhỏ hơn nhiều.", "gần như không đổi.", "lớn hơn nhiều.", "bằng 0."],
   "B",
   "Lực cản của không khí nhỏ nên chỉ ảnh hưởng đáng kể tới biên độ; chu kì gần như giữ nguyên giá trị "
   "T = 2π√(m/k).",
   "Dao động tắt dần", TB, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),
],
P2=[
ds("Hình bên là đồ thị li độ theo thời gian của một dao động tắt dần với biên độ ban đầu 6 cm và chu kì "
   "0,6 s.",
   [("Chu kì của dao động tắt dần này gần như không đổi theo thời gian.", True,
     "Đúng. Khi lực cản nhỏ, khoảng cách giữa hai đỉnh liên tiếp trên đồ thị gần như bằng nhau."),
    ("Trong 6 giây đầu, vật thực hiện được 10 dao động.", True,
     "Đúng. N = t/T = 6/0,6 = 10."),
    ("Tại t = 2,4 s biên độ còn khoảng 2,2 cm, khi đó cơ năng còn khoảng 37% giá trị ban đầu.", False,
     "Sai. Cơ năng tỉ lệ với BÌNH PHƯƠNG biên độ: W/W₀ = (2,2/6)² ≈ 0,13, tức khoảng 13%. Giá trị 37% "
     "là tỉ số BIÊN ĐỘ."),
    ("Phần cơ năng mất đi đã chuyển thành nhiệt do lực cản của môi trường.", True,
     "Đúng. Công của lực cản chuyển cơ năng thành nội năng của vật và môi trường.")],
   "Dao động tắt dần", K, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

ds("Hình bên là đường biểu diễn biên độ dao động cưỡng bức theo tần số ngoại lực, ứng với hai mức ma sát "
   "khác nhau.",
   [("Cả hai đường đều đạt cực đại tại cùng một tần số, đó là tần số riêng của hệ (2 Hz).", True,
     "Đúng. Vị trí đỉnh cộng hưởng được quyết định bởi tần số riêng, không phụ thuộc mức ma sát."),
    ("Đường có đỉnh cao và nhọn hơn ứng với ma sát nhỏ hơn.", True,
     "Đúng. Ma sát càng nhỏ, năng lượng mất đi mỗi chu kì càng ít nên biên độ cộng hưởng càng lớn."),
    ("Ở giai đoạn ổn định, hệ dao động với tần số riêng của nó chứ không phải tần số ngoại lực.", False,
     "Sai. Dao động cưỡng bức ổn định có tần số bằng tần số của NGOẠI LỰC. Tần số riêng chỉ quyết định "
     "biên độ lớn hay nhỏ."),
    ("Khi tần số ngoại lực rất khác tần số riêng, biên độ dao động cưỡng bức nhỏ dù ngoại lực vẫn tác "
     "dụng.", True,
     "Đúng, đọc được ngay trên đồ thị: hai cánh của đường cộng hưởng đều thấp.")],
   "Đường cộng hưởng", K, fig="d_dt_conghuong", cap="Đường cộng hưởng"),

ds("Một con lắc đơn treo trên trần toa tàu có chu kì dao động riêng 1,5 s. Đường ray gồm các thanh dài "
   "12,5 m; mỗi lần bánh xe qua chỗ nối ray, toa tàu bị xóc một lần.",
   [("Chu kì của ngoại lực cưỡng bức tác dụng lên con lắc bằng d/v với d = 12,5 m.", True,
     "Đúng. Thời gian giữa hai lần xóc liên tiếp là thời gian tàu đi hết một thanh ray."),
    ("Con lắc dao động mạnh nhất khi tàu chạy với tốc độ khoảng 8,33 m/s.", True,
     "Đúng. Cộng hưởng khi d/v = T₀ ⟹ v = 12,5/1,5 ≈ 8,33 m/s (khoảng 30 km/h)."),
    ("Nếu tàu chạy nhanh hơn hoặc chậm hơn tốc độ đó thì biên độ dao động của con lắc giảm.", True,
     "Đúng. Khi f khác f₀, biên độ dao động cưỡng bức nhỏ đi — đúng như hai cánh của đường cộng hưởng."),
    ("Nếu rút ngắn dây treo con lắc thì tốc độ gây cộng hưởng cũng giảm.", False,
     "Sai. Rút ngắn dây làm chu kì riêng T₀ GIẢM, mà v = d/T₀ nên tốc độ gây cộng hưởng lại TĂNG.")],
   "Cộng hưởng – bài toán thực tiễn", RK, fig="d_sd_congHuong_thuctien",
   cap="Cộng hưởng trong thực tiễn"),

ds("Phân biệt dao động tắt dần, dao động duy trì và dao động cưỡng bức.",
   [("Dao động tắt dần có biên độ giảm dần vì cơ năng chuyển dần thành nhiệt.", True,
     "Đúng, do công của lực cản."),
    ("Dao động duy trì có biên độ không đổi và tần số bằng tần số riêng của hệ.", True,
     "Đúng. Năng lượng được bù đúng bằng phần mất đi mà không làm thay đổi tần số — ví dụ đồng hồ quả lắc."),
    ("Dao động cưỡng bức ổn định có tần số bằng tần số của ngoại lực.", True,
     "Đúng, đây là điểm khác biệt cốt lõi so với dao động duy trì."),
    ("Cộng hưởng luôn có hại nên trong kĩ thuật người ta luôn tìm cách triệt tiêu nó.", False,
     "Sai. Cộng hưởng có hại trong nhiều trường hợp (cầu, bệ máy) nhưng lại rất có ích trong hộp đàn, "
     "lò vi sóng, mạch chọn sóng… Kĩ thuật là biết KHAI THÁC hoặc TRÁNH tuỳ tình huống.")],
   "Phân biệt các loại dao động", K),
],
P3=[
sa("Từ đồ thị dao động tắt dần ở hình bên (T = 0,6 s), trong 6 giây đầu vật thực hiện được bao nhiêu dao "
   "động?",
   "10", "N = t/T = 6/0,6 = 10 dao động.", "Đọc đồ thị dao động tắt dần", TB,
   fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

sa("Một dao động tắt dần có biên độ ban đầu 6 cm; tại thời điểm t biên độ còn 2,2 cm. Cơ năng của hệ khi "
   "đó còn bao nhiêu phần trăm cơ năng ban đầu (làm tròn đến hàng đơn vị)?",
   "13", "W/W₀ = (A/A₀)² = (2,2/6)² ≈ 0,134 ⟹ khoảng 13%.",
   "Dao động tắt dần – năng lượng", K, fig="d_dt_tatdan", cap="Đồ thị dao động tắt dần"),

sa("Một con lắc đơn treo trên toa tàu có chu kì riêng 1,5 s; đường ray gồm các thanh dài 12,5 m. Con lắc "
   "dao động mạnh nhất khi tàu chạy với tốc độ bao nhiêu m/s (làm tròn đến chữ số thập phân thứ hai)?",
   "8,33", "Cộng hưởng khi d/v = T₀ ⟹ v = d/T₀ = 12,5/1,5 ≈ 8,33 m/s.",
   "Cộng hưởng – bài toán thực tiễn", K, fig="d_sd_congHuong_thuctien",
   cap="Cộng hưởng trong thực tiễn"),

sa("Từ đường cộng hưởng ở hình bên, tần số riêng của hệ dao động bằng bao nhiêu héc?",
   "2", "Cả hai đường (ứng với hai mức ma sát) đều đạt cực đại tại f = 2 Hz, đó là tần số riêng f₀.",
   "Đọc đường cộng hưởng", TB, fig="d_dt_conghuong", cap="Đường cộng hưởng"),

sa("Một dao động tắt dần có biên độ giảm còn một nửa. Cơ năng của hệ khi đó còn bao nhiêu phần trăm giá "
   "trị ban đầu?",
   "25", "W ∝ A² ⟹ W/W₀ = (1/2)² = 0,25 = 25%.", "Dao động tắt dần – năng lượng", TB),

sa("Một con lắc đơn treo trên toa tàu có chu kì riêng 2,0 s; đường ray gồm các thanh dài 12,5 m. Tốc độ "
   "gây cộng hưởng bằng bao nhiêu m/s (làm tròn đến chữ số thập phân thứ hai)?",
   "6,25", "v = d/T₀ = 12,5/2,0 = 6,25 m/s (khoảng 22,5 km/h).",
   "Cộng hưởng – bài toán thực tiễn", K),
])


# =====================================================================
DE9 = dict(
ma="11C1-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Dùng đường tròn pha: thời điểm, thời gian thoả điều kiện, quãng đường lớn nhất – nhỏ nhất",
P1=[
mc("Một vật dao động điều hoà với phương trình x = 4cos(5πt) cm (t tính bằng s). Thời điểm ĐẦU TIÊN vật "
   "đi qua vị trí có li độ 2 cm là",
   ["1/30 s.", "1/15 s.", "1/10 s.", "1/6 s."],
   "B",
   "x = 2 cm ⟹ cos(5πt) = 0,5 ⟹ 5πt = ±π/3 + k2π.\n"
   "Nghiệm dương nhỏ nhất: 5πt = π/3 ⟹ t = 1/15 s ≈ 0,067 s.\n"
   "Trên đường tròn pha, đó là góc quay 60° kể từ biên dương, tức T/6 = 0,4/6 = 1/15 s.",
   "Thời điểm – đường tròn pha", K, fig="d_sd_vongtron",
   cap="Đường tròn pha"),

mc("Vẫn với dao động ở câu trên, thời điểm vật đi qua vị trí có li độ 2 cm lần thứ HAI là",
   ["1/15 s.", "2/15 s.", "1/3 s.", "7/15 s."],
   "C",
   "Các nghiệm dương: t = 1/15; t = 0,4 − 1/15 = 1/3; t = 0,4 + 1/15 = 7/15; …\n"
   "Lần thứ hai ứng với t = 1/3 s ≈ 0,333 s (vật quay lại li độ 2 cm khi đi theo chiều dương từ biên âm "
   "về).",
   "Thời điểm – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với chu kì T và biên độ A. Trong một chu kì, khoảng thời gian mà độ lớn li "
   "độ NHỎ HƠN A/2 là",
   ["T/6.", "T/4.", "T/3.", "T/2."],
   "C",
   "|x| < A/2 ⟺ |cosθ| < 1/2 ⟺ θ nằm trong hai cung (60°; 120°) và (240°; 300°).\n"
   "Tổng số đo hai cung: 2 · 60° = 120° ⟹ Δt = (120°/360°)·T = T/3.",
   "Thời gian thoả điều kiện – đường tròn pha", RK, fig="d_sd_vongtron",
   cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với chu kì T. Trong một chu kì, khoảng thời gian mà động năng LỚN HƠN thế "
   "năng là",
   ["T/4.", "T/3.", "T/2.", "2T/3."],
   "C",
   "Wđ > Wt ⟺ |x| < A/√2 ⟺ |cosθ| < √2/2 ⟺ θ thuộc hai cung (45°; 135°) và (225°; 315°).\n"
   "Tổng: 2 · 90° = 180° ⟹ Δt = T/2. (Kết quả này hợp lí: trong một chu kì, động năng lớn hơn thế năng "
   "đúng một nửa thời gian.)",
   "Thời gian thoả điều kiện – năng lượng", RK, fig="d_dt_nangluong_t",
   cap="Động năng và thế năng theo thời gian"),

mc("Một vật dao động điều hoà với biên độ 6 cm và chu kì T. Quãng đường LỚN NHẤT vật đi được trong khoảng "
   "thời gian T/3 là",
   ["6,0 cm.", "8,5 cm.", "10,4 cm.", "12,0 cm."],
   "C",
   "Quãng đường lớn nhất trong Δt đạt được khi vật đi ĐỐI XỨNG qua vị trí cân bằng (nơi vật chạy nhanh "
   "nhất).\nGóc quay tương ứng: Δθ = ωΔt = 2π/3 (tức 120°).\n"
   "S_max = 2A·sin(Δθ/2) = 2 · 6 · sin60° = 12 · 0,866 ≈ 10,4 cm.",
   "Quãng đường lớn nhất – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Vẫn với vật ở câu trên, quãng đường NHỎ NHẤT vật đi được trong khoảng thời gian T/3 là",
   ["6,0 cm.", "8,5 cm.", "10,4 cm.", "12,0 cm."],
   "A",
   "Quãng đường nhỏ nhất đạt được khi vật đi đối xứng qua VỊ TRÍ BIÊN (nơi vật chạy chậm nhất).\n"
   "S_min = 2A(1 − cos(Δθ/2)) = 2 · 6 · (1 − cos60°) = 12 · 0,5 = 6,0 cm.",
   "Quãng đường nhỏ nhất – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với biên độ 5 cm, chu kì 0,4 s. Tại t = 0 vật có li độ 2,5 cm và đang "
   "chuyển động theo chiều âm. Phương trình dao động của vật là",
   ["x = 5cos(5πt − π/3) cm.", "x = 5cos(5πt + π/3) cm.",
    "x = 5cos(5πt + π/6) cm.", "x = 5cos(5πt − π/6) cm."],
   "B",
   "ω = 2π/T = 5π rad/s. Tại t = 0: 5cos φ = 2,5 ⟹ cos φ = 0,5 ⟹ φ = ±π/3.\n"
   "Vật đi theo chiều âm ⟹ v(0) = −5ω·sin φ < 0 ⟹ sin φ > 0 ⟹ chọn φ = +π/3.",
   "Viết phương trình dao động", K, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với chu kì T. Khoảng thời gian ngắn nhất để vật đi từ li độ x = −A/2 tới "
   "li độ x = +A/2 (đi qua vị trí cân bằng) là",
   ["T/12.", "T/6.", "T/4.", "T/3."],
   "B",
   "Trên đường tròn pha, hai vị trí này ứng với các góc 120° và 60°; đi trực tiếp qua vị trí cân bằng "
   "ứng với góc quay 60° ⟹ Δt = T/6.",
   "Thời gian – đường tròn pha", K, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với chu kì 0,4 s và biên độ 8 cm. Quãng đường vật đi được trong 0,7 s kể từ "
   "khi vật ở biên là",
   ["40 cm.", "48 cm.", "56 cm.", "64 cm."],
   "C",
   "0,7 s = 1,75T = T + 0,75T. Trong 1 chu kì: 4A = 32 cm.\n"
   "Trong 0,75T = 3·(T/4) kể từ biên: vật đi biên → cân bằng (A) → biên kia (A) → cân bằng (A) = 3A = "
   "24 cm.\nTổng: 32 + 24 = 56 cm.",
   "Quãng đường trong dao động điều hoà", RK),

mc("Trong một chu kì dao động, khoảng thời gian mà tốc độ của vật lớn hơn nửa tốc độ cực đại là",
   ["T/3.", "T/2.", "2T/3.", "3T/4."],
   "C",
   "v > v_max/2 ⟺ |sinθ| > 1/2 ⟺ θ thuộc (30°;150°) và (210°;330°): tổng 2 · 120° = 240°.\n"
   "Δt = (240°/360°)·T = 2T/3.",
   "Thời gian thoả điều kiện – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với phương trình x = 6cos(10πt + π/2) cm. Tại t = 0, vật",
   ["ở biên dương.", "ở biên âm.",
    "ở vị trí cân bằng và đi theo chiều dương.",
    "ở vị trí cân bằng và đi theo chiều âm."],
   "D",
   "x(0) = 6cos(π/2) = 0 ⟹ vật ở vị trí cân bằng.\n"
   "v(0) = −6 · 10π · sin(π/2) = −60π < 0 ⟹ vật đi theo chiều âm.",
   "Viết phương trình – pha ban đầu", K),

mc("Hai vật dao động điều hoà cùng biên độ, cùng chu kì nhưng lệch pha π/3. Khi vật thứ nhất ở biên dương "
   "thì vật thứ hai có li độ",
   ["A.", "A/2.", "A√3/2.", "0."],
   "B",
   "Khi vật 1 ở biên dương thì pha của nó bằng 0; pha của vật 2 lệch π/3 nên li độ của nó là "
   "x₂ = A·cos(±π/3) = A/2.",
   "Độ lệch pha", K, fig="d_dt_lechpha", cap="Hai dao động lệch pha"),

mc("Một vật dao động điều hoà với biên độ A. Khoảng thời gian ngắn nhất giữa hai lần liên tiếp vật có tốc "
   "độ cực đại là",
   ["T/4.", "T/2.", "3T/4.", "T."],
   "B",
   "Tốc độ cực đại khi vật qua vị trí cân bằng — xảy ra 2 lần trong mỗi chu kì, cách đều nhau ⟹ khoảng "
   "cách thời gian là T/2.",
   "Thời gian trong dao động điều hoà", TB),

mc("Một vật dao động điều hoà với chu kì 0,6 s. Khoảng thời gian ngắn nhất để vật đi từ vị trí có động "
   "năng bằng thế năng tới vị trí biên gần nhất là",
   ["0,050 s.", "0,075 s.", "0,100 s.", "0,150 s."],
   "B",
   "Wđ = Wt ⟹ x = ±A/√2, ứng với góc 45° trên đường tròn pha. Từ đó tới biên là góc quay 45°:\n"
   "Δt = (45°/360°)·T = T/8 = 0,6/8 = 0,075 s.",
   "Thời gian – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một vật dao động điều hoà với biên độ 4 cm. Trong một chu kì, số lần vật có li độ 2 cm là",
   ["1 lần.", "2 lần.", "3 lần.", "4 lần."],
   "B",
   "Li độ x = +2 cm (một giá trị cụ thể, có dấu) được vật đi qua đúng 2 lần trong mỗi chu kì: một lần "
   "theo chiều âm, một lần theo chiều dương. (Nếu hỏi |x| = 2 cm thì mới là 4 lần.)",
   "Số lần các sự kiện trong một chu kì", K),

mc("Một vật dao động điều hoà. Trong một chu kì, khoảng thời gian mà thế năng lớn hơn động năng là",
   ["T/4.", "T/3.", "T/2.", "2T/3."],
   "C",
   "Wt > Wđ ⟺ |x| > A/√2, ứng với hai cung mỗi cung 90° quanh hai biên: tổng 180° ⟹ Δt = T/2.\n"
   "Kết hợp với kết quả “Wđ > Wt trong T/2”, ta thấy hai trạng thái này chia đôi chu kì.",
   "Thời gian thoả điều kiện – năng lượng", RK),

mc("Một vật dao động điều hoà với chu kì T. Quãng đường lớn nhất vật đi được trong T/6 là",
   ["A/2.", "A.", "A√2.", "A√3."],
   "B",
   "Δθ = ωΔt = 2π/6 = π/3 (60°).\nS_max = 2A·sin(Δθ/2) = 2A·sin30° = 2A · 0,5 = A.",
   "Quãng đường lớn nhất – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Vì sao quãng đường lớn nhất trong một khoảng thời gian Δt < T/2 lại đạt được khi vật đi đối xứng qua "
   "vị trí cân bằng?",
   ["Vì ở đó lực kéo về lớn nhất.", "Vì ở đó vật chuyển động nhanh nhất.",
    "Vì ở đó gia tốc lớn nhất.", "Vì ở đó thế năng lớn nhất."],
   "B",
   "Trong cùng một khoảng thời gian, vật đi được quãng đường dài nhất ở vùng nó chuyển động NHANH nhất — "
   "đó là vùng quanh vị trí cân bằng. Ngược lại, quãng đường nhỏ nhất đạt được ở vùng quanh biên, nơi vật "
   "chạy chậm nhất.",
   "Quãng đường lớn nhất – lí giải", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),
],
P2=[
ds("Một vật dao động điều hoà với phương trình x = 4cos(5πt) cm (t tính bằng s).",
   [("Chu kì dao động là 0,4 s.", True,
     "Đúng. T = 2π/ω = 2π/(5π) = 0,4 s."),
    ("Thời điểm đầu tiên vật đi qua li độ 2 cm là 1/15 s.", True,
     "Đúng. cos(5πt) = 0,5 ⟹ 5πt = π/3 ⟹ t = 1/15 s ≈ 0,067 s (ứng với góc quay 60° từ biên dương)."),
    ("Thời điểm vật đi qua li độ 2 cm lần thứ hai là 2/15 s.", False,
     "Sai. Các nghiệm dương lần lượt là 1/15; 1/3; 7/15; … Lần thứ hai là t = 1/3 s ≈ 0,333 s. "
     "Giá trị 2/15 s không phải nghiệm của phương trình."),
    ("Trong một chu kì, vật đi qua li độ 2 cm đúng 2 lần.", True,
     "Đúng: một lần khi đi theo chiều âm và một lần khi đi theo chiều dương.")],
   "Thời điểm – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

ds("Một vật dao động điều hoà với biên độ A và chu kì T. Xét các khoảng thời gian thoả mãn những điều "
   "kiện khác nhau trong MỘT chu kì.",
   [("Khoảng thời gian mà |x| < A/2 bằng T/3.", True,
     "Đúng. |cosθ| < 1/2 ứng với hai cung 60°, tổng 120° = T/3."),
    ("Khoảng thời gian mà động năng lớn hơn thế năng bằng T/2.", True,
     "Đúng. Wđ > Wt ⟺ |x| < A/√2 ⟺ hai cung 90°, tổng 180° = T/2."),
    ("Khoảng thời gian mà tốc độ lớn hơn nửa tốc độ cực đại bằng T/3.", False,
     "Sai. v > v_max/2 ⟺ |sinθ| > 1/2 ⟺ hai cung 120°, tổng 240° ⟹ khoảng thời gian là 2T/3 chứ "
     "không phải T/3."),
    ("Khoảng thời gian mà thế năng lớn hơn động năng cũng bằng T/2.", True,
     "Đúng, vì hai trạng thái Wđ > Wt và Wt > Wđ chia đôi chu kì.")],
   "Thời gian thoả điều kiện – đường tròn pha", RK, fig="d_sd_vongtron",
   cap="Đường tròn pha"),

ds("Một vật dao động điều hoà với biên độ 6 cm và chu kì T.",
   [("Quãng đường lớn nhất vật đi được trong T/3 là khoảng 10,4 cm.", True,
     "Đúng. S_max = 2A·sin(Δθ/2) với Δθ = 120°: S_max = 12·sin60° ≈ 10,4 cm."),
    ("Quãng đường nhỏ nhất vật đi được trong T/3 là 6,0 cm.", True,
     "Đúng. S_min = 2A(1 − cos60°) = 12 · 0,5 = 6,0 cm."),
    ("Quãng đường lớn nhất đạt được khi vật đi đối xứng qua vị trí biên.", False,
     "Sai, ngược lại. Quãng đường LỚN NHẤT đạt được khi vật đi đối xứng qua VỊ TRÍ CÂN BẰNG (nơi chạy "
     "nhanh nhất); đi đối xứng qua biên mới cho quãng đường NHỎ NHẤT."),
    ("Quãng đường vật đi được trong nửa chu kì luôn bằng 12 cm, không có giá trị lớn nhất hay nhỏ nhất.", True,
     "Đúng. Trong T/2 quãng đường luôn bằng 2A = 12 cm bất kể xuất phát từ đâu — đây là mốc rất tiện để "
     "kiểm tra kết quả.")],
   "Quãng đường lớn nhất – nhỏ nhất", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

ds("Một vật dao động điều hoà với biên độ 5 cm, chu kì 0,4 s; tại t = 0 vật có li độ 2,5 cm và đang "
   "chuyển động theo chiều âm.",
   [("Tần số góc của dao động là 5π rad/s.", True, "Đúng. ω = 2π/T = 2π/0,4 = 5π rad/s."),
    ("Pha ban đầu của dao động là +π/3 rad.", True,
     "Đúng. cos φ = 2,5/5 = 0,5 ⟹ φ = ±π/3; vật đi theo chiều âm nên v(0) < 0 ⟹ sin φ > 0 ⟹ φ = +π/3."),
    ("Phương trình dao động là x = 5cos(5πt + π/3) cm.", True,
     "Đúng, ghép A = 5 cm, ω = 5π rad/s và φ = π/3."),
    ("Vì một phần tư chu kì bằng 0,1 s nên thời điểm đầu tiên vật đi qua vị trí cân bằng là 0,1 s.", False,
     "Sai. Cách lập luận này chỉ đúng khi vật XUẤT PHÁT TỪ BIÊN. Ở đây vật xuất phát từ li độ 2,5 cm với "
     "pha ban đầu π/3, nên phải giải: 5πt + π/3 = π/2 ⟹ 5πt = π/6 ⟹ t = 1/30 s ≈ 0,033 s — sớm hơn "
     "nhiều so với 0,1 s.")],
   "Viết phương trình dao động", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),
],
P3=[
sa("Một vật dao động điều hoà với phương trình x = 4cos(5πt) cm. Thời điểm đầu tiên vật đi qua li độ 2 cm "
   "bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ ba)?",
   "0,067", "cos(5πt) = 0,5 ⟹ 5πt = π/3 ⟹ t = 1/15 ≈ 0,067 s (tức T/6).",
   "Thời điểm – đường tròn pha", K, fig="d_sd_vongtron", cap="Đường tròn pha"),

sa("Một vật dao động điều hoà với biên độ 6 cm. Quãng đường LỚN NHẤT vật đi được trong khoảng thời gian "
   "T/3 bằng bao nhiêu xentimét (làm tròn đến chữ số thập phân thứ nhất)?",
   "10,4", "Δθ = 120° ⟹ S_max = 2A·sin(Δθ/2) = 12·sin60° = 12 · 0,866 ≈ 10,4 cm.",
   "Quãng đường lớn nhất", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

sa("Vẫn với vật đó, quãng đường NHỎ NHẤT vật đi được trong khoảng thời gian T/3 bằng bao nhiêu xentimét?",
   "6", "S_min = 2A(1 − cos(Δθ/2)) = 12 · (1 − cos60°) = 12 · 0,5 = 6,0 cm.",
   "Quãng đường nhỏ nhất", RK),

sa("Một vật dao động điều hoà với chu kì 0,4 s và biên độ 8 cm. Quãng đường vật đi được trong 0,7 s kể từ "
   "khi vật ở biên bằng bao nhiêu xentimét?",
   "56",
   "0,7 s = 1,75T. Trong 1 chu kì: 4A = 32 cm; trong 0,75T còn lại (kể từ biên): 3A = 24 cm.\n"
   "Tổng: 32 + 24 = 56 cm.",
   "Quãng đường trong dao động điều hoà", RK),

sa("Một vật dao động điều hoà với chu kì 0,6 s. Khoảng thời gian ngắn nhất để vật đi từ vị trí có động "
   "năng bằng thế năng tới vị trí biên gần nhất bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ ba)?",
   "0,075", "Vị trí Wđ = Wt ứng với góc 45° trên đường tròn pha; tới biên là góc 45° ⟹ Δt = T/8 = 0,075 s.",
   "Thời gian – đường tròn pha", RK),

sa("Trong một chu kì dao động điều hoà có chu kì 0,6 s, khoảng thời gian mà tốc độ của vật lớn hơn nửa "
   "tốc độ cực đại bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ nhất)?",
   "0,4", "v > v_max/2 ⟺ hai cung tổng 240° ⟹ Δt = (240/360)·0,6 = 0,4 s.",
   "Thời gian thoả điều kiện", RK),
])


# =====================================================================
DE10 = dict(
ma="11C1-Đ10", ten="ĐỀ SỐ 10", muc="Khó / thử thách",
trongtam="Con lắc lò xo thẳng đứng có lò xo nén; điều kiện không trượt; bài toán ngược nhiều bước",
P1=[
mc("Một con lắc lò xo treo thẳng đứng, ở vị trí cân bằng lò xo dãn 2 cm. Lấy g = 10 m/s². Tần số góc của "
   "dao động gần nhất với",
   ["10,0 rad/s.", "15,8 rad/s.", "22,4 rad/s.", "31,6 rad/s."],
   "C",
   "Ở vị trí cân bằng k·Δℓ₀ = mg ⟹ k/m = g/Δℓ₀.\n"
   "ω = √(k/m) = √(g/Δℓ₀) = √(10/0,02) = √500 ≈ 22,4 rad/s.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Vẫn với con lắc ở câu trên, chu kì dao động gần nhất với",
   ["0,20 s.", "0,28 s.", "0,40 s.", "0,63 s."],
   "B", "T = 2π/ω = 2π/22,36 ≈ 0,281 s ≈ 0,28 s.", "Con lắc lò xo treo thẳng đứng", K),

mc("Vẫn với con lắc đó (Δℓ₀ = 2 cm), cho vật dao động với biên độ 4 cm. Trong quá trình dao động, lò xo",
   ["luôn dãn.", "luôn bị nén.", "có lúc dãn, có lúc bị nén.", "không biến dạng."],
   "C",
   "Chọn trục Ox hướng xuống, gốc tại vị trí cân bằng. Lò xo có chiều dài tự nhiên khi x = −Δℓ₀ = −2 cm.\n"
   "Vì biên độ A = 4 cm > 2 cm nên vật đi lên quá vị trí đó và lò xo bị NÉN trong một phần chu kì.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Vẫn với con lắc đó, trong một chu kì, khoảng thời gian lò xo bị nén chiếm",
   ["T/6.", "T/4.", "T/3.", "T/2."],
   "C",
   "Lò xo bị nén khi x < −Δℓ₀, tức A·cosθ < −2 ⟺ cosθ < −0,5 ⟺ θ ∈ (120°; 240°).\n"
   "Cung tương ứng có số đo 120° ⟹ khoảng thời gian nén bằng (120°/360°)·T = T/3.",
   "Con lắc lò xo treo thẳng đứng – đường tròn pha", RK, fig="d_sd_vongtron",
   cap="Đường tròn pha"),

mc("Vẫn với con lắc đó (T ≈ 0,281 s), khoảng thời gian lò xo bị nén trong một chu kì gần nhất với",
   ["0,047 s.", "0,070 s.", "0,094 s.", "0,141 s."],
   "C", "Δt = T/3 ≈ 0,281/3 ≈ 0,094 s.", "Con lắc lò xo treo thẳng đứng", RK),

mc("Một vật nhỏ đặt trên một tấm ván nằm ngang; tấm ván dao động điều hoà theo phương ngang với tần số góc "
   "10 rad/s. Hệ số ma sát nghỉ cực đại giữa vật và ván là 0,40; lấy g = 10 m/s². Để vật KHÔNG trượt trên "
   "ván, biên độ dao động lớn nhất là",
   ["2 cm.", "4 cm.", "8 cm.", "40 cm."],
   "B",
   "Vật chỉ dao động cùng ván nhờ lực ma sát nghỉ; lực này phải đủ lớn để tạo ra gia tốc cực đại của "
   "dao động:\n"
   "m·a_max ≤ μmg ⟹ ω²A ≤ μg ⟹ A ≤ μg/ω² = 0,40 · 10/100 = 0,04 m = 4 cm.",
   "Điều kiện không trượt", RK),

mc("Một con lắc lò xo treo thẳng đứng dao động với biên độ 5 cm; trong một chu kì thời gian lò xo bị nén "
   "bằng T/3. Độ dãn của lò xo ở vị trí cân bằng là",
   ["1,25 cm.", "2,50 cm.", "3,54 cm.", "4,33 cm."],
   "B",
   "Thời gian nén bằng T/3 ứng với cung 120°, tức cosθ < −0,5 ⟹ Δℓ₀/A = 0,5 ⟹ Δℓ₀ = A/2 = 2,5 cm.",
   "Bài toán ngược – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Với con lắc ở câu trên (Δℓ₀ = 2,5 cm, g = 10 m/s²), chu kì dao động gần nhất với",
   ["0,20 s.", "0,31 s.", "0,45 s.", "0,63 s."],
   "B", "T = 2π√(Δℓ₀/g) = 2π√(0,025/10) = 2π · 0,05 ≈ 0,314 s ≈ 0,31 s.",
   "Con lắc lò xo treo thẳng đứng", K),

mc("Một vật dao động điều hoà. Biết trong một chu kì, khoảng thời gian mà độ lớn gia tốc không vượt quá "
   "một nửa gia tốc cực đại là T/3. Điều đó tương ứng với điều kiện",
   ["|x| ≤ A/2.", "|x| ≤ A/√2.", "|x| ≤ A√3/2.", "|x| ≤ A/4."],
   "A",
   "|a| = ω²|x| nên |a| ≤ a_max/2 ⟺ |x| ≤ A/2. Khoảng thời gian tương ứng đúng bằng T/3 (đã tính ở đề "
   "trước), phù hợp với dữ kiện.",
   "Gia tốc – đường tròn pha", K),

mc("Một con lắc lò xo nằm ngang dao động điều hoà với biên độ A. Khi vật ở li độ x = A/2, tỉ số giữa lực "
   "kéo về và lực kéo về cực đại là",
   ["1/4.", "1/2.", "√3/2.", "3/4."],
   "B", "F = k|x| nên F/F_max = |x|/A = 1/2. (Chú ý tỉ số THẾ NĂNG mới là 1/4.)",
   "Lực kéo về", K),

mc("Một vật dao động điều hoà với chu kì T. Trong khoảng thời gian T/4, quãng đường vật đi được có thể "
   "nhận giá trị nào sau đây?",
   ["Chỉ đúng bằng A.", "Bất kì giá trị nào từ A√2·(1 − …) tới A√2.",
    "Nằm trong khoảng từ A(2 − √2) tới A√2.", "Luôn lớn hơn A√2."],
   "C",
   "Với Δt = T/4 ⟹ Δθ = 90°:\n"
   "S_max = 2A·sin45° = A√2 ≈ 1,41A;  S_min = 2A(1 − cos45°) = A(2 − √2) ≈ 0,59A.\n"
   "Quãng đường thực tế nằm giữa hai giá trị này, chỉ bằng đúng A khi xuất phát từ biên hoặc từ vị trí "
   "cân bằng.",
   "Quãng đường lớn nhất – nhỏ nhất", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một con lắc đơn dao động nhỏ với chu kì 2,0 s. Người ta giữ cố định điểm chính giữa của dây treo (khi "
   "vật đang ở vị trí cân bằng). Chu kì dao động mới của con lắc gần nhất với",
   ["1,00 s.", "1,41 s.", "2,00 s.", "2,83 s."],
   "B",
   "Giữ điểm chính giữa làm chiều dài hiệu dụng còn một nửa: ℓ′ = ℓ/2.\n"
   "T ∝ √ℓ ⟹ T′ = T/√2 = 2,0/1,414 ≈ 1,41 s.",
   "Con lắc đơn – bài toán biến đổi", RK, fig="d_sd_cldon", cap="Con lắc đơn"),

mc("Một vật dao động điều hoà với biên độ 10 cm. Trong một chu kì, khoảng thời gian mà vật cách vị trí cân "
   "bằng không quá 5 cm là 0,4 s. Chu kì dao động của vật là",
   ["0,8 s.", "1,0 s.", "1,2 s.", "1,6 s."],
   "C",
   "|x| ≤ A/2 ứng với khoảng thời gian T/3 trong mỗi chu kì.\nT/3 = 0,4 s ⟹ T = 1,2 s.",
   "Bài toán ngược – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Một con lắc lò xo dao động điều hoà với cơ năng 0,20 J. Khi động năng bằng 3 lần thế năng, thế năng "
   "của vật bằng",
   ["0,05 J.", "0,10 J.", "0,15 J.", "0,20 J."],
   "A", "Wđ = 3Wt ⟹ W = 4Wt ⟹ Wt = W/4 = 0,20/4 = 0,05 J.",
   "Năng lượng trong dao động điều hoà", K),

mc("Hai vật dao động điều hoà cùng biên độ A, cùng chu kì T nhưng ngược pha nhau. Khoảng cách lớn nhất "
   "giữa hai vật theo phương dao động là",
   ["A.", "A√2.", "2A.", "4A."],
   "C",
   "Ngược pha ⟹ x₂ = −x₁ nên khoảng cách |x₁ − x₂| = 2|x₁|, lớn nhất khi |x₁| = A: khoảng cách bằng 2A "
   "(hai vật ở hai biên đối diện).",
   "Độ lệch pha", K, fig="d_dt_lechpha", cap="Hai dao động lệch pha"),

mc("Một con lắc lò xo treo thẳng đứng có Δℓ₀ = 4 cm, dao động với biên độ 8 cm. Tỉ số giữa lực đàn hồi "
   "cực đại và lực đàn hồi cực tiểu của lò xo là",
   ["2.", "3.", "không xác định vì lực đàn hồi cực tiểu bằng 0.", "6."],
   "C",
   "Vì A = 8 cm > Δℓ₀ = 4 cm nên trong quá trình dao động có lúc lò xo có chiều dài tự nhiên, khi đó lực "
   "đàn hồi bằng 0. Tỉ số F_max/F_min không xác định (chia cho 0).\n"
   "(Nếu A < Δℓ₀ thì tỉ số bằng (Δℓ₀ + A)/(Δℓ₀ − A).)",
   "Con lắc lò xo treo thẳng đứng", RK, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

mc("Một vật dao động điều hoà với chu kì T. Gọi t₁ là khoảng thời gian ngắn nhất vật đi từ vị trí cân "
   "bằng tới li độ A/2 và t₂ là khoảng thời gian ngắn nhất vật đi từ li độ A/2 tới biên. Tỉ số t₂/t₁ bằng",
   ["1/2.", "1.", "2.", "3."],
   "C",
   "t₁ = T/12 (góc 30°); t₂ = T/6 (góc 60°) ⟹ t₂/t₁ = 2.\n"
   "Kết quả này phản ánh việc vật chạy chậm dần khi tiến ra biên.",
   "Thời gian – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

mc("Trong dao động điều hoà, phát biểu nào sau đây SAI?",
   ["Gia tốc luôn hướng về vị trí cân bằng.",
    "Vận tốc và gia tốc luôn vuông pha với nhau.",
    "Động năng và thế năng biến thiên với chu kì bằng nửa chu kì dao động.",
    "Tốc độ của vật tỉ lệ thuận với khoảng cách từ vật tới vị trí cân bằng."],
   "D",
   "Tốc độ là v = ω√(A² − x²): nó GIẢM khi vật ra xa vị trí cân bằng, và quan hệ không phải tỉ lệ thuận. "
   "Đại lượng tỉ lệ thuận với |x| là gia tốc và lực kéo về.",
   "Tổng hợp lí thuyết dao động", K),
],
P2=[
ds("Một con lắc lò xo treo thẳng đứng, ở vị trí cân bằng lò xo dãn 2 cm; cho vật dao động với biên độ "
   "4 cm. Lấy g = 10 m/s².",
   [("Tần số góc của dao động là √(g/Δℓ₀) ≈ 22,4 rad/s và chu kì khoảng 0,28 s.", True,
     "Đúng. ω = √(10/0,02) = √500 ≈ 22,36 rad/s ⟹ T = 2π/ω ≈ 0,281 s."),
    ("Trong quá trình dao động, có những lúc lò xo bị nén.", True,
     "Đúng. Biên độ 4 cm lớn hơn độ dãn 2 cm ở vị trí cân bằng nên vật đi lên quá vị trí lò xo có chiều "
     "dài tự nhiên."),
    ("Trong một chu kì, khoảng thời gian lò xo bị nén bằng T/6.", False,
     "Sai. Lò xo nén khi A·cosθ < −Δℓ₀ ⟺ cosθ < −0,5 ⟺ cung 120° ⟹ thời gian nén là T/3 ≈ 0,094 s, "
     "chứ không phải T/6."),
    ("Lực đàn hồi của lò xo có lúc bằng 0 trong quá trình dao động.", True,
     "Đúng. Khi vật đi qua vị trí lò xo có chiều dài tự nhiên (x = −2 cm), lực đàn hồi triệt tiêu — dù "
     "lực kéo về khi đó vẫn khác 0.")],
   "Con lắc lò xo treo thẳng đứng có lò xo nén", RK, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

ds("Một vật nhỏ đặt trên tấm ván nằm ngang; tấm ván dao động điều hoà theo phương ngang. Hệ số ma sát "
   "nghỉ cực đại giữa vật và ván là μ; lấy g = 10 m/s².",
   [("Lực duy nhất theo phương ngang tác dụng lên vật là lực ma sát nghỉ của ván.", True,
     "Đúng. Chính lực ma sát nghỉ này “kéo” vật dao động cùng với ván."),
    ("Điều kiện để vật không trượt trên ván là ω²A ≤ μg.", True,
     "Đúng. Lực ma sát nghỉ cực đại μmg phải đủ để gây ra gia tốc cực đại a_max = ω²A: mω²A ≤ μmg."),
    ("Với ω = 10 rad/s và μ = 0,40, biên độ lớn nhất để vật không trượt là 4 cm.", True,
     "Đúng. A ≤ μg/ω² = 0,40 · 10/100 = 0,04 m = 4 cm."),
    ("Nếu tăng tần số góc lên gấp đôi mà giữ nguyên biên độ thì vật vẫn không trượt.", False,
     "Sai. a_max = ω²A tăng 4 lần, vượt xa μg nên vật CHẮC CHẮN trượt. Muốn giữ nguyên điều kiện, biên độ "
     "phải giảm 4 lần.")],
   "Điều kiện không trượt", RK),

ds("Một con lắc lò xo treo thẳng đứng dao động điều hoà; gọi Δℓ₀ là độ dãn của lò xo ở vị trí cân bằng và "
   "A là biên độ dao động.",
   [("Nếu A < Δℓ₀ thì lò xo luôn dãn và tỉ số F_max/F_min = (Δℓ₀ + A)/(Δℓ₀ − A).", True,
     "Đúng. Độ dãn biến thiên từ (Δℓ₀ − A) tới (Δℓ₀ + A), luôn dương."),
    ("Nếu A > Δℓ₀ thì lực đàn hồi cực tiểu bằng 0.", True,
     "Đúng. Có thời điểm lò xo trở về chiều dài tự nhiên nên lực đàn hồi triệt tiêu."),
    ("Nếu trong một chu kì thời gian lò xo bị nén bằng T/3 thì Δℓ₀ = A/2.", True,
     "Đúng. Thời gian nén T/3 ứng với cung 120° ⟹ cosθ < −0,5 ⟹ Δℓ₀/A = 0,5."),
    ("Lực đàn hồi của lò xo luôn bằng lực kéo về tác dụng lên vật.", False,
     "Sai. Lực kéo về là HỢP LỰC của trọng lực và lực đàn hồi, có độ lớn k|x| tính từ vị trí cân bằng; "
     "còn lực đàn hồi riêng nó bằng k|Δℓ₀ + x|. Hai lực này chỉ trùng nhau ở con lắc lò xo NẰM NGANG.")],
   "Con lắc lò xo treo thẳng đứng", RK, fig="d_sd_loxo_doc",
   cap="Con lắc lò xo treo thẳng đứng"),

ds("Xét một số bài toán ngược trong dao động điều hoà.",
   [("Nếu trong một chu kì, khoảng thời gian mà vật cách vị trí cân bằng không quá A/2 là 0,4 s thì chu "
     "kì dao động là 1,2 s.", True,
     "Đúng. Điều kiện |x| ≤ A/2 ứng với T/3 trong mỗi chu kì ⟹ T = 3 · 0,4 = 1,2 s."),
    ("Nếu giữ cố định điểm chính giữa dây treo của một con lắc đơn có chu kì 2,0 s thì chu kì mới là "
     "khoảng 1,41 s.", True,
     "Đúng. Chiều dài hiệu dụng giảm một nửa nên T′ = T/√2 ≈ 1,41 s."),
    ("Với Δt = T/4, quãng đường vật đi được luôn bằng đúng biên độ A.", False,
     "Sai. Quãng đường trong T/4 nằm trong khoảng từ A(2 − √2) ≈ 0,59A tới A√2 ≈ 1,41A; chỉ bằng đúng A "
     "khi vật xuất phát từ biên hoặc từ vị trí cân bằng."),
    ("Tỉ số giữa thời gian đi từ li độ A/2 tới biên và thời gian đi từ vị trí cân bằng tới li độ A/2 "
     "bằng 2.", True,
     "Đúng. Hai khoảng thời gian đó lần lượt là T/6 và T/12; tỉ số bằng 2 vì vật chạy chậm dần khi ra "
     "gần biên.")],
   "Bài toán ngược – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),
],
P3=[
sa("Một con lắc lò xo treo thẳng đứng, ở vị trí cân bằng lò xo dãn 2 cm; lấy g = 10 m/s². Chu kì dao động "
   "bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ ba)?",
   "0,281", "ω = √(g/Δℓ₀) = √(10/0,02) = √500 ≈ 22,36 rad/s ⟹ T = 2π/22,36 ≈ 0,281 s.",
   "Con lắc lò xo treo thẳng đứng", K, fig="d_sd_loxo_doc", cap="Con lắc lò xo treo thẳng đứng"),

sa("Vẫn với con lắc đó, cho dao động với biên độ 4 cm. Trong một chu kì, khoảng thời gian lò xo bị nén "
   "bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ ba)?",
   "0,094",
   "Lò xo nén khi 4cosθ < −2 ⟺ cosθ < −0,5 ⟺ cung 120° ⟹ Δt = T/3 ≈ 0,281/3 ≈ 0,094 s.",
   "Con lắc lò xo treo thẳng đứng – đường tròn pha", RK, fig="d_sd_vongtron", cap="Đường tròn pha"),

sa("Một vật nhỏ đặt trên tấm ván dao động điều hoà theo phương ngang với tần số góc 10 rad/s; hệ số ma "
   "sát nghỉ cực đại là 0,40, g = 10 m/s². Biên độ dao động lớn nhất để vật không trượt bằng bao nhiêu "
   "xentimét?",
   "4", "ω²A ≤ μg ⟹ A ≤ μg/ω² = 0,40 · 10/100 = 0,04 m = 4 cm.", "Điều kiện không trượt", RK),

sa("Một con lắc lò xo treo thẳng đứng dao động với biên độ 5 cm; trong một chu kì thời gian lò xo bị nén "
   "bằng T/3. Độ dãn của lò xo ở vị trí cân bằng bằng bao nhiêu xentimét (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "2,5", "Thời gian nén T/3 ⟺ cung 120° ⟺ Δℓ₀/A = 0,5 ⟹ Δℓ₀ = 2,5 cm.",
   "Bài toán ngược – đường tròn pha", RK),

sa("Một vật dao động điều hoà với biên độ 10 cm. Trong một chu kì, khoảng thời gian mà vật cách vị trí "
   "cân bằng không quá 5 cm là 0,4 s. Chu kì dao động bằng bao nhiêu giây (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "1,2", "|x| ≤ A/2 ứng với T/3 trong mỗi chu kì ⟹ T = 3 · 0,4 = 1,2 s.",
   "Bài toán ngược – đường tròn pha", RK),

sa("Một con lắc đơn dao động nhỏ với chu kì 2,0 s. Giữ cố định điểm chính giữa của dây treo. Chu kì dao "
   "động mới bằng bao nhiêu giây (làm tròn đến chữ số thập phân thứ hai)?",
   "1,41", "Chiều dài hiệu dụng giảm một nửa ⟹ T′ = T/√2 = 2,0/1,414 ≈ 1,41 s.",
   "Con lắc đơn – bài toán biến đổi", RK, fig="d_sd_cldon", cap="Con lắc đơn"),
])


NHOM = dict(
    ten_nhom="LỚP 11 – CHƯƠNG 1: DAO ĐỘNG",
    mo_ta="Bộ 10 đề luyện tập, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó / thử thách)",
    pham_vi=(
        "Bài 1. Dao động điều hoà  •  Bài 2. Mô tả dao động điều hoà\n"
        "Bài 3. Vận tốc, gia tốc trong dao động điều hoà  •  Bài 4. Bài tập về dao động điều hoà\n"
        "Bài 5. Động năng. Thế năng. Sự chuyển hoá năng lượng trong dao động điều hoà "
        "(cơ năng của con lắc lò xo và con lắc đơn)\n"
        "Bài 6. Dao động tắt dần. Dao động cưỡng bức. Hiện tượng cộng hưởng\n"
        "Công thức dùng thống nhất: x = A·cos(ωt + φ); v = −ωA·sin(ωt + φ); a = −ω²x; ω = 2π/T = 2πf; "
        "A² = x² + v²/ω²; W = ½mω²A² = ½kA²; con lắc lò xo T = 2π√(m/k); con lắc đơn T = 2π√(ℓ/g); "
        "g = 10 m/s² (trừ khi đề ghi khác)."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
