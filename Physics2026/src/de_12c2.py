# -*- coding: utf-8 -*-
"""LỚP 12 – CHƯƠNG 2: KHÍ LÍ TƯỞNG.  10 đề, độ khó tăng dần.

Hằng số dùng thống nhất: R = 8,31 J/(mol·K); k = 1,38·10⁻²³ J/K;
N_A = 6,02·10²³ mol⁻¹; áp suất khí quyển chuẩn 10⁵ Pa; 1 atm ≈ 10⁵ Pa.
"""
from qbase import mc, ds, sa, D, TB, K, RK


# =====================================================================
DE1 = dict(
ma="12C2-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Mô hình động học phân tử chất khí và ba định luật chất khí ở mức nhận biết",
P1=[
mc("Theo mô hình động học phân tử chất khí, các phân tử khí",
   ["đứng yên ở những vị trí xác định.",
    "chuyển động hỗn loạn không ngừng và chỉ tương tác khi va chạm.",
    "chuyển động theo những quỹ đạo tròn quanh tâm bình.",
    "liên kết chặt chẽ với nhau bằng lực hút mạnh."],
   "B",
   "Ba nội dung của mô hình: phân tử khí có kích thước rất nhỏ so với khoảng cách giữa chúng; chuyển động "
   "hỗn loạn không ngừng; chỉ tương tác đáng kể khi va chạm.",
   "Mô hình động học phân tử chất khí", D, fig="k_sd_mohinh",
   cap="Các phân tử khí chuyển động hỗn loạn và va chạm vào thành bình"),

mc("Khí lí tưởng là chất khí trong đó",
   ["các phân tử có kích thước rất lớn.",
    "bỏ qua kích thước phân tử và tương tác giữa chúng ngoài lúc va chạm.",
    "các phân tử luôn hút nhau.",
    "áp suất luôn bằng không."],
   "B",
   "Khí lí tưởng là mô hình đơn giản hoá: coi phân tử như chất điểm và bỏ qua mọi tương tác trừ va chạm. "
   "Các khí thực ở áp suất không quá lớn và nhiệt độ không quá thấp đều gần đúng là khí lí tưởng.",
   "Khí lí tưởng", D),

mc("Định luật Boyle phát biểu: với một lượng khí xác định ở nhiệt độ không đổi thì",
   ["áp suất tỉ lệ thuận với thể tích.", "áp suất tỉ lệ nghịch với thể tích.",
    "áp suất tỉ lệ thuận với nhiệt độ.", "thể tích tỉ lệ thuận với nhiệt độ."],
   "B",
   "pV = hằng số, tức p tỉ lệ NGHỊCH với V: nén khí (V giảm) thì áp suất tăng.",
   "Định luật Boyle", D),

mc("Trong hệ toạ độ (p, V), đường đẳng nhiệt của một lượng khí lí tưởng xác định là",
   ["đường thẳng đi qua gốc toạ độ.", "đường thẳng song song với trục V.",
    "một nhánh hypebol.", "đường parabol."],
   "C",
   "Từ pV = hằng số suy ra p = const/V — đồ thị là một nhánh hypebol.",
   "Định luật Boyle – đồ thị", D, fig="k_dt_dangnhiet",
   cap="Hai đường đẳng nhiệt ứng với hai nhiệt độ khác nhau"),

mc("Định luật Charles áp dụng cho quá trình",
   ["đẳng nhiệt.", "đẳng tích.", "đẳng áp.", "bất kì."],
   "C",
   "Định luật Charles: với lượng khí xác định ở áp suất không đổi thì V/T = hằng số.",
   "Định luật Charles", D),

mc("Phương trình trạng thái của một lượng khí lí tưởng xác định là",
   ["pV = hằng số.", "p/T = hằng số.", "V/T = hằng số.", "pV/T = hằng số."],
   "D",
   "pV/T = hằng số là hệ thức tổng quát; ba định luật chất khí là các trường hợp riêng khi giữ T, V hoặc "
   "p không đổi.",
   "Phương trình trạng thái", D),

mc("Đơn vị của áp suất trong hệ SI là",
   ["niutơn (N).", "pascan (Pa).", "jun (J).", "oát (W)."],
   "B", "1 Pa = 1 N/m². Các đơn vị khác thường gặp: 1 atm ≈ 1,013·10⁵ Pa; 1 mmHg ≈ 133,3 Pa.",
   "Áp suất", D),

mc("Nhiệt độ 57 °C ứng với nhiệt độ tuyệt đối là",
   ["300 K.", "320 K.", "330 K.", "350 K."],
   "C", "T = 57 + 273 = 330 K. Mọi định luật chất khí đều phải dùng nhiệt độ tuyệt đối.",
   "Thang nhiệt độ tuyệt đối", D),

mc("Nén đẳng nhiệt một lượng khí từ thể tích 6,0 L xuống 2,0 L. Nếu áp suất ban đầu là 1,0·10⁵ Pa thì "
   "áp suất sau khi nén là",
   ["0,33·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa.", "6,0·10⁵ Pa."],
   "C", "p₁V₁ = p₂V₂ ⟹ p₂ = 1,0·10⁵ · 6,0/2,0 = 3,0·10⁵ Pa.",
   "Định luật Boyle", D),

mc("Đun nóng đẳng áp một lượng khí từ 27 °C lên 87 °C. Nếu thể tích ban đầu là 3,0 L thì thể tích sau đó là",
   ["2,5 L.", "3,6 L.", "4,2 L.", "9,7 L."],
   "B",
   "T₁ = 300 K, T₂ = 360 K. V₁/T₁ = V₂/T₂ ⟹ V₂ = 3,0 · 360/300 = 3,6 L.\n"
   "Bẫy: dùng nhiệt độ Celsius sẽ cho 3,0 · 87/27 ≈ 9,7 L — hoàn toàn sai.",
   "Định luật Charles", D),

mc("Một bình kín thể tích không đổi chứa khí ở 300 K, áp suất 2,0·10⁵ Pa. Đun nóng khí tới 450 K thì áp "
   "suất bằng",
   ["1,3·10⁵ Pa.", "2,5·10⁵ Pa.", "3,0·10⁵ Pa.", "4,5·10⁵ Pa."],
   "C", "Thể tích không đổi ⟹ p/T = hằng số ⟹ p₂ = 2,0·10⁵ · 450/300 = 3,0·10⁵ Pa.",
   "Quá trình đẳng tích", D),

mc("Một lượng khí ở 1,0·10⁵ Pa, 8,0 L, 300 K được đưa tới trạng thái có thể tích 4,0 L và nhiệt độ 450 K. "
   "Áp suất lúc sau là",
   ["1,5·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa.", "4,0·10⁵ Pa."],
   "C",
   "p₁V₁/T₁ = p₂V₂/T₂ ⟹ p₂ = p₁V₁T₂/(T₁V₂) = 1,0·10⁵ · 8,0 · 450/(300 · 4,0) = 3,0·10⁵ Pa.",
   "Phương trình trạng thái", TB),

mc("Trong hệ toạ độ (p, V), hai đường đẳng nhiệt ứng với nhiệt độ T₁ và T₂ như hình vẽ. Kết luận đúng là",
   ["T₁ > T₂.", "T₁ < T₂.", "T₁ = T₂.", "chưa đủ dữ kiện để so sánh."],
   "B",
   "Với cùng một thể tích, đường nào cho áp suất lớn hơn thì ứng với nhiệt độ cao hơn (vì pV = nRT). "
   "Đường T₂ nằm xa gốc toạ độ hơn nên T₂ > T₁.",
   "Đọc đồ thị đẳng nhiệt", TB, fig="k_dt_dangnhiet", cap="Hai đường đẳng nhiệt"),

mc("Kéo dài đường biểu diễn quá trình đẳng tích của một lượng khí trong hệ toạ độ (p, t), với t đo bằng "
   "độ Celsius, về phía nhiệt độ thấp thì đường này cắt trục hoành tại giá trị",
   ["−273 °C.", "0 °C.", "−100 °C.", "273 °C."],
   "A",
   "Đẳng tích: p tỉ lệ thuận với nhiệt độ tuyệt đối T = t + 273.\n"
   "Ngoại suy tới p = 0 ta được T = 0 K, tức t = −273 °C — độ không tuyệt đối.\n"
   "Trên thực tế khí đã hoá lỏng trước khi tới nhiệt độ đó nên phần cuối của đường chỉ là ngoại suy.",
   "Độ không tuyệt đối – ngoại suy đồ thị", TB, fig="k_dt_dangtich",
   cap="Hai đường đẳng tích ứng với hai thể tích khác nhau"),

mc("Động năng tịnh tiến trung bình của một phân tử khí lí tưởng liên hệ với nhiệt độ theo hệ thức",
   ["W̄đ = kT.", "W̄đ = (2/3)kT.", "W̄đ = (3/2)kT.", "W̄đ = 3kT."],
   "C",
   "W̄đ = (3/2)kT với k = 1,38·10⁻²³ J/K. Hệ thức này cho thấy nhiệt độ tuyệt đối là số đo động năng "
   "chuyển động nhiệt trung bình của phân tử.",
   "Động năng phân tử và nhiệt độ", D),

mc("Ở nhiệt độ 300 K, động năng tịnh tiến trung bình của một phân tử khí lí tưởng bằng "
   "(k = 1,38·10⁻²³ J/K)",
   ["2,07·10⁻²¹ J.", "4,14·10⁻²¹ J.", "6,21·10⁻²¹ J.", "1,24·10⁻²⁰ J."],
   "C", "W̄đ = (3/2)kT = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J.",
   "Động năng phân tử và nhiệt độ", D),

mc("Áp suất mà chất khí tác dụng lên thành bình được giải thích là do",
   ["trọng lượng của khối khí.",
    "các phân tử khí liên tục va chạm vào thành bình.",
    "lực hút giữa các phân tử khí và thành bình.",
    "sự dãn nở vì nhiệt của thành bình."],
   "B",
   "Mỗi va chạm truyền cho thành bình một xung lượng; vô số va chạm trong mỗi giây tạo nên một lực trung "
   "bình phân bố đều — đó chính là áp suất khí.",
   "Áp suất theo mô hình động học phân tử", D, fig="k_sd_mohinh",
   cap="Áp suất khí là kết quả của các va chạm phân tử"),

mc("Khi bơm không khí vào lốp xe đạp, lốp căng lên. Nguyên nhân chủ yếu là",
   ["nhiệt độ không khí trong lốp tăng lên.",
    "số phân tử khí trong lốp tăng lên nên số va chạm lên thành lốp mỗi giây tăng.",
    "khối lượng mỗi phân tử khí tăng lên.",
    "thể tích mỗi phân tử khí tăng lên."],
   "B",
   "Bơm thêm khí làm mật độ phân tử (N/V) tăng, do đó số va chạm lên mỗi đơn vị diện tích thành lốp trong "
   "mỗi giây tăng lên, áp suất tăng.",
   "Áp suất – thực tiễn", D, fig="k_sd_bomxe", cap="Bơm không khí vào lốp xe"),
],
P2=[
ds("Xét mô hình động học phân tử chất khí và khái niệm khí lí tưởng.",
   [("Các phân tử khí chuyển động hỗn loạn không ngừng về mọi phía.", True,
     "Đúng. Đây là nội dung cơ bản của mô hình động học phân tử, được xác nhận bằng chuyển động Brown và "
     "hiện tượng khuếch tán."),
    ("Trong mô hình khí lí tưởng, các phân tử chỉ tương tác với nhau khi va chạm.", True,
     "Đúng. Bỏ qua lực tương tác ở khoảng cách xa chính là điều làm cho mô hình trở nên đơn giản."),
    ("Chất khí luôn chiếm toàn bộ thể tích bình chứa vì các phân tử khí đẩy nhau rất mạnh.", False,
     "Sai ở phần giải thích. Chất khí chiếm toàn bộ bình chứa vì các phân tử chuyển động tự do và hầu như "
     "không có lực liên kết giữ chúng lại, chứ không phải vì chúng “đẩy nhau rất mạnh”."),
    ("Các khí thực ở áp suất không quá lớn và nhiệt độ không quá thấp có thể coi gần đúng là khí lí tưởng.", True,
     "Đúng. Khi đó khoảng cách giữa các phân tử đủ lớn để bỏ qua kích thước phân tử và lực tương tác.")],
   "Mô hình động học phân tử – khí lí tưởng", D, fig="k_sd_mohinh",
   cap="Mô hình phân tử chất khí"),

ds("Nén đẳng nhiệt một lượng khí lí tưởng xác định từ thể tích 6,0 L xuống 2,0 L, áp suất ban đầu là "
   "1,0·10⁵ Pa.",
   [("Áp suất khí sau khi nén là 3,0·10⁵ Pa.", True,
     "Đúng. p₂ = p₁V₁/V₂ = 1,0·10⁵ · 6,0/2,0 = 3,0·10⁵ Pa."),
    ("Trong quá trình này, tích pV của khối khí không đổi.", True,
     "Đúng, đó chính là nội dung định luật Boyle khi nhiệt độ và lượng khí không đổi."),
    ("Số phân tử khí trong bình tăng lên 3 lần.", False,
     "Sai. Lượng khí không đổi nên số phân tử N không đổi; cái tăng 3 lần là MẬT ĐỘ phân tử N/V, và chính "
     "điều đó làm áp suất tăng 3 lần."),
    ("Động năng tịnh tiến trung bình của mỗi phân tử khí không đổi trong quá trình nén này.", True,
     "Đúng. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ; quá trình đẳng nhiệt nên W̄đ không đổi.")],
   "Định luật Boyle – mô hình phân tử", TB),

ds("Một bình kín thể tích không đổi chứa khí lí tưởng ở 300 K, áp suất 2,0·10⁵ Pa. Đun nóng khí tới 450 K.",
   [("Áp suất khí sau khi đun là 3,0·10⁵ Pa.", True,
     "Đúng. Thể tích không đổi ⟹ p/T = hằng số ⟹ p₂ = 2,0·10⁵ · 450/300 = 3,0·10⁵ Pa."),
    ("Nếu tính theo thang Celsius, ta có p₂ = p₁ · 177/27, tức khoảng 13,1·10⁵ Pa.", False,
     "Sai. Định luật chỉ đúng với nhiệt độ TUYỆT ĐỐI. Dùng nhiệt độ Celsius cho kết quả vô lí — chỉ cần "
     "thử với t₁ = 0 °C là thấy ngay điều phi lí."),
    ("Động năng tịnh tiến trung bình của mỗi phân tử khí tăng 1,5 lần.", True,
     "Đúng. W̄đ = (3/2)kT tỉ lệ thuận với T; T tăng từ 300 K lên 450 K tức tăng 1,5 lần."),
    ("Trong hệ toạ độ (p, T), quá trình này được biểu diễn bằng một đoạn thẳng nằm trên đường thẳng đi "
     "qua gốc toạ độ.", True,
     "Đúng. Đẳng tích ⟹ p = (nR/V)T là hàm bậc nhất thuần nhất của T nên đồ thị đi qua gốc toạ độ.")],
   "Quá trình đẳng tích", TB, fig="k_dt_dangtich", cap="Đường đẳng tích trong hệ (p, T)"),

ds("Xét mối liên hệ giữa động năng phân tử và nhiệt độ của khí lí tưởng "
   "(k = 1,38·10⁻²³ J/K).",
   [("Ở 300 K, động năng tịnh tiến trung bình của một phân tử khí bằng 6,21·10⁻²¹ J.", True,
     "Đúng. W̄đ = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J."),
    ("Ở cùng nhiệt độ, phân tử hiđrô và phân tử oxi có động năng tịnh tiến trung bình bằng nhau.", True,
     "Đúng. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ, không phụ thuộc loại khí. (Tốc độ của chúng thì khác "
     "nhau vì khối lượng phân tử khác nhau.)"),
    ("Muốn động năng tịnh tiến trung bình của phân tử tăng gấp đôi, phải tăng nhiệt độ Celsius lên gấp đôi.", False,
     "Sai. Phải tăng nhiệt độ TUYỆT ĐỐI lên gấp đôi. Ví dụ từ 300 K (27 °C) phải lên 600 K (327 °C), "
     "chứ không phải lên 54 °C."),
    ("Ở 0 K, chuyển động nhiệt của các phân tử coi như dừng lại.", True,
     "Đúng. Từ W̄đ = (3/2)kT, khi T → 0 thì W̄đ → 0. Đó là ý nghĩa của độ không tuyệt đối.")],
   "Động năng phân tử và nhiệt độ", TB),
],
P3=[
sa("Nhiệt độ 87 °C ứng với bao nhiêu kelvin?",
   "360", "T = 87 + 273 = 360 K.", "Thang nhiệt độ tuyệt đối", D),

sa("Nén đẳng nhiệt một lượng khí từ 5,0 L xuống 2,0 L. Áp suất ban đầu là 1,2·10⁵ Pa. Áp suất sau khi nén "
   "bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "3", "p₂ = p₁V₁/V₂ = 1,2·10⁵ · 5,0/2,0 = 3,0·10⁵ Pa.", "Định luật Boyle", D),

sa("Đun nóng đẳng áp một lượng khí từ 27 °C lên 127 °C. Thể tích ban đầu là 4,5 L. Thể tích sau đó bằng "
   "bao nhiêu lít?",
   "6", "T₁ = 300 K, T₂ = 400 K ⟹ V₂ = V₁·T₂/T₁ = 4,5 · 400/300 = 6,0 L.", "Định luật Charles", D),

sa("Một bình kín thể tích không đổi chứa khí ở 27 °C, áp suất 1,5·10⁵ Pa. Đun nóng tới 127 °C thì áp suất "
   "bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "2", "p₂ = p₁·T₂/T₁ = 1,5·10⁵ · 400/300 = 2,0·10⁵ Pa.", "Quá trình đẳng tích", D),

sa("Một lượng khí ở 2,0·10⁵ Pa, 6,0 L, 300 K được đưa tới trạng thái 1,0·10⁵ Pa và 400 K. Thể tích lúc "
   "sau bằng bao nhiêu lít?",
   "16",
   "p₁V₁/T₁ = p₂V₂/T₂ ⟹ V₂ = p₁V₁T₂/(T₁p₂) = 2,0·10⁵ · 6,0 · 400/(300 · 1,0·10⁵) = 16 L.",
   "Phương trình trạng thái", TB),

sa("Ở nhiệt độ 600 K, động năng tịnh tiến trung bình của một phân tử khí lí tưởng bằng bao nhiêu "
   "(đơn vị 10⁻²¹ J, làm tròn đến chữ số thập phân thứ hai)? Cho k = 1,38·10⁻²³ J/K.",
   "12,42", "W̄đ = (3/2)kT = 1,5 · 1,38·10⁻²³ · 600 = 1,242·10⁻²⁰ J = 12,42·10⁻²¹ J.",
   "Động năng phân tử và nhiệt độ", D),
])


# =====================================================================
DE2 = dict(
ma="12C2-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Vận dụng ba định luật chất khí và phương trình Clapeyron trong tình huống quen thuộc",
P1=[
mc("Điều kiện áp dụng của định luật Boyle là",
   ["khối lượng khí không đổi và nhiệt độ không đổi.",
    "khối lượng khí không đổi và áp suất không đổi.",
    "thể tích không đổi.",
    "chỉ cần chất khí là khí lí tưởng."],
   "A",
   "Định luật Boyle pV = hằng số chỉ đúng cho MỘT LƯỢNG KHÍ XÁC ĐỊNH ở NHIỆT ĐỘ KHÔNG ĐỔI. Đây là điều "
   "kiện thường bị bỏ sót nhất khi giải bài tập.",
   "Định luật Boyle – điều kiện áp dụng", D),

mc("Một bọt khí có thể tích 2,0 cm³ ở đáy hồ, nơi áp suất là 3,0·10⁵ Pa, nổi lên mặt nước nơi áp suất là "
   "1,0·10⁵ Pa. Coi nhiệt độ không đổi. Thể tích bọt khí ở mặt nước là",
   ["0,67 cm³.", "1,5 cm³.", "4,0 cm³.", "6,0 cm³."],
   "D",
   "p₁V₁ = p₂V₂ ⟹ V₂ = 3,0·10⁵ · 2,0/1,0·10⁵ = 6,0 cm³.\n"
   "Bọt khí nở ra khi nổi lên vì áp suất bên ngoài giảm — đó cũng là lí do thợ lặn phải thở ra khi ngoi lên.",
   "Định luật Boyle – thực tiễn", D),

mc("Đun nóng đẳng áp một lượng khí từ 27 °C lên 57 °C. Thể tích ban đầu 2,0 L. Thể tích lúc sau là",
   ["2,2 L.", "2,5 L.", "3,0 L.", "4,2 L."],
   "A", "T₁ = 300 K, T₂ = 330 K ⟹ V₂ = 2,0 · 330/300 = 2,2 L.", "Định luật Charles", D),

mc("Một bình kín thể tích không đổi chứa khí ở 27 °C, áp suất 1,5·10⁵ Pa. Nhiệt độ tăng lên 87 °C thì áp "
   "suất bằng",
   ["1,2·10⁵ Pa.", "1,8·10⁵ Pa.", "2,4·10⁵ Pa.", "4,8·10⁵ Pa."],
   "B", "p₂ = p₁·T₂/T₁ = 1,5·10⁵ · 360/300 = 1,8·10⁵ Pa.", "Quá trình đẳng tích", D),

mc("Phương trình Clapeyron của khí lí tưởng có dạng",
   ["pV = nR/T.", "pV = nRT.", "p/V = nRT.", "pVT = nR."],
   "B", "pV = nRT với n là số mol và R = 8,31 J/(mol·K) là hằng số khí lí tưởng.",
   "Phương trình Clapeyron", D),

mc("Một bình thể tích 8,31 L chứa khí lí tưởng ở 300 K và áp suất 3,0·10⁵ Pa. Số mol khí trong bình là "
   "(R = 8,31 J/(mol·K))",
   ["0,5 mol.", "1,0 mol.", "1,5 mol.", "2,0 mol."],
   "B",
   "n = pV/(RT) = 3,0·10⁵ · 8,31·10⁻³/(8,31 · 300) = 2493/2493 = 1,0 mol.\n"
   "Chú ý đổi thể tích ra m³: 8,31 L = 8,31·10⁻³ m³.",
   "Phương trình Clapeyron", TB),

mc("Số phân tử có trong 1,0 mol khí bất kì là (N_A = 6,02·10²³ mol⁻¹)",
   ["6,02·10²¹.", "6,02·10²².", "6,02·10²³.", "6,02·10²⁴."],
   "C", "Theo định nghĩa số Avogadro, mỗi mol chất chứa N_A = 6,02·10²³ hạt.",
   "Số Avogadro", D),

mc("Trong hệ toạ độ (V, T), đường đẳng áp của một lượng khí lí tưởng xác định là",
   ["đường thẳng đi qua gốc toạ độ.", "đường thẳng song song với trục T.",
    "nhánh hypebol.", "đường tròn."],
   "A",
   "Từ V = (nR/p)·T, khi p không đổi thì V tỉ lệ thuận với T: đồ thị là đường thẳng qua gốc toạ độ.",
   "Định luật Charles – đồ thị", D, fig="k_dt_dangap",
   cap="Hai đường đẳng áp ứng với hai áp suất khác nhau"),

mc("Trên hình vẽ có hai đường đẳng áp ứng với áp suất p₁ và p₂. Kết luận đúng là",
   ["p₁ > p₂.", "p₁ < p₂.", "p₁ = p₂.", "chưa đủ dữ kiện."],
   "B",
   "V = (nR/p)·T nên hệ số góc nR/p tỉ lệ NGHỊCH với áp suất: đường càng dốc thì áp suất càng nhỏ. "
   "Đường p₁ dốc hơn ⟹ p₁ < p₂.",
   "Đọc đồ thị đẳng áp", TB, fig="k_dt_dangap", cap="Hai đường đẳng áp"),

mc("Nén một lượng khí lí tưởng ở nhiệt độ không đổi. Đại lượng nào sau đây KHÔNG đổi?",
   ["Áp suất.", "Thể tích.", "Mật độ phân tử.", "Động năng tịnh tiến trung bình của phân tử."],
   "D",
   "Đẳng nhiệt nên W̄đ = (3/2)kT không đổi. Áp suất và mật độ phân tử đều tăng, thể tích giảm.",
   "Mô hình động học phân tử", TB),

mc("Một quả bóng cao su chứa khí ở 27 °C được đưa vào tủ lạnh ở −3 °C. Coi áp suất trong bóng không đổi. "
   "Thể tích bóng sẽ",
   ["giảm còn 90% giá trị ban đầu.", "giảm còn 89% giá trị ban đầu.",
    "tăng lên 111% giá trị ban đầu.", "không đổi."],
   "A",
   "T₁ = 300 K, T₂ = 270 K ⟹ V₂/V₁ = 270/300 = 0,90, tức còn 90%.\n"
   "Bẫy: dùng nhiệt độ Celsius (−3/27) cho kết quả vô nghĩa (âm).",
   "Định luật Charles – thực tiễn", TB),

mc("Một lượng khí ở 3,0·10⁵ Pa, 2,0 L, 300 K được nén tới 1,0 L và làm nóng tới 400 K. Áp suất lúc sau là",
   ["4,0·10⁵ Pa.", "6,0·10⁵ Pa.", "8,0·10⁵ Pa.", "9,0·10⁵ Pa."],
   "C", "p₂ = p₁V₁T₂/(T₁V₂) = 3,0·10⁵ · 2,0 · 400/(300 · 1,0) = 8,0·10⁵ Pa.",
   "Phương trình trạng thái", TB),

mc("Ở cùng nhiệt độ, so sánh tốc độ chuyển động trung bình của phân tử hiđrô (M = 2 g/mol) và phân tử "
   "oxi (M = 32 g/mol):",
   ["Phân tử hiđrô chuyển động nhanh hơn.",
    "Phân tử oxi chuyển động nhanh hơn.",
    "Hai loại phân tử chuyển động nhanh như nhau.",
    "Chưa đủ dữ kiện để so sánh."],
   "A",
   "Cùng nhiệt độ ⟹ cùng động năng trung bình (1/2)mv̄² = (3/2)kT. Phân tử nhẹ hơn phải chuyển động nhanh "
   "hơn để có cùng động năng: v ∝ 1/√M nên hiđrô nhanh hơn oxi khoảng √16 = 4 lần.",
   "Động năng phân tử – so sánh", TB),

mc("Khi nhiệt độ tuyệt đối của một lượng khí lí tưởng tăng gấp 4 lần thì động năng tịnh tiến trung bình "
   "của mỗi phân tử",
   ["tăng 2 lần.", "tăng 4 lần.", "tăng 8 lần.", "tăng 16 lần."],
   "B", "W̄đ = (3/2)kT tỉ lệ THUẬN với T nên cũng tăng 4 lần.",
   "Động năng phân tử và nhiệt độ", D),

mc("Một bình chứa khí có van an toàn tự mở khi áp suất đạt 5,0·10⁵ Pa. Ở 27 °C áp suất trong bình là "
   "2,5·10⁵ Pa. Van sẽ mở khi nhiệt độ đạt",
   ["54 °C.", "327 °C.", "600 °C.", "873 °C."],
   "B",
   "Thể tích không đổi ⟹ T₂ = T₁·p₂/p₁ = 300 · 5,0/2,5 = 600 K ⟹ t₂ = 600 − 273 = 327 °C.\n"
   "Bẫy: nhân đôi nhiệt độ Celsius cho 54 °C — sai hoàn toàn.",
   "Quá trình đẳng tích – an toàn", TB, fig="k_sd_binhkhi",
   cap="Bình khí nén có van an toàn"),

mc("Trong quá trình đẳng nhiệt, nếu thể tích khí giảm 3 lần thì mật độ phân tử khí",
   ["giảm 3 lần.", "không đổi.", "tăng 3 lần.", "tăng 9 lần."],
   "C",
   "Số phân tử N không đổi, thể tích giảm 3 lần nên mật độ phân tử thay đổi theo tỉ số\n"
   "n₂/n₁ = (N/V₂)/(N/V₁) = V₁/V₂ = 3 ⟹ mật độ tăng 3 lần.\n"
   "Đó cũng chính là lí do áp suất tăng 3 lần trong quá trình đẳng nhiệt.",
   "Mô hình động học phân tử", TB),

mc("Đơn vị nào sau đây KHÔNG phải là đơn vị của áp suất?",
   ["Pa.", "N/m².", "mmHg.", "N·m."],
   "D", "N·m là đơn vị của công (jun). Pa, N/m² và mmHg đều là đơn vị áp suất.",
   "Đơn vị áp suất", D),

mc("Nếu giữ nguyên nhiệt độ và thể tích của bình mà bơm thêm khí vào thì",
   ["áp suất không đổi.", "áp suất tăng vì mật độ phân tử tăng.",
    "áp suất giảm.", "động năng trung bình của phân tử tăng."],
   "B",
   "pV = nRT với V, T không đổi ⟹ p tỉ lệ thuận với n. Về mặt vi mô: mật độ phân tử tăng nên số va chạm "
   "lên thành bình mỗi giây tăng. Động năng trung bình mỗi phân tử vẫn không đổi vì nhiệt độ không đổi.",
   "Phương trình Clapeyron – mô hình phân tử", TB),
],
P2=[
ds("Một bọt khí có thể tích 2,0 cm³ ở đáy một hồ nước, nơi áp suất là 3,0·10⁵ Pa. Bọt khí nổi lên mặt "
   "nước, nơi áp suất là 1,0·10⁵ Pa. Coi nhiệt độ nước không đổi theo độ sâu.",
   [("Có thể áp dụng định luật Boyle cho bọt khí trong quá trình này.", True,
     "Đúng. Lượng khí trong bọt không đổi và nhiệt độ được coi là không đổi — đúng hai điều kiện của "
     "định luật Boyle."),
    ("Thể tích bọt khí khi lên tới mặt nước là 6,0 cm³.", True,
     "Đúng. V₂ = p₁V₁/p₂ = 3,0·10⁵ · 2,0/1,0·10⁵ = 6,0 cm³."),
    ("Trong quá trình nổi lên, mật độ phân tử khí trong bọt tăng dần.", False,
     "Sai. Số phân tử không đổi mà thể tích tăng lên nên mật độ phân tử GIẢM dần — đó chính là nguyên "
     "nhân làm áp suất trong bọt giảm."),
    ("Nếu nhiệt độ nước ở mặt hồ cao hơn ở đáy hồ thì thể tích bọt khí ở mặt nước lớn hơn 6,0 cm³.", True,
     "Đúng. Khi đó phải dùng phương trình trạng thái pV/T = hằng số; T₂ > T₁ làm V₂ lớn hơn giá trị "
     "6,0 cm³ tính theo định luật Boyle.")],
   "Định luật Boyle – thực tiễn", TB),

ds("Một bình kín có van an toàn tự mở khi áp suất đạt 5,0·10⁵ Pa. Ở 27 °C áp suất khí trong bình là "
   "2,5·10⁵ Pa. Thể tích bình coi như không đổi.",
   [("Quá trình khi đun nóng bình là quá trình đẳng tích.", True,
     "Đúng. Bình kín, thể tích không đổi và lượng khí không đổi (khi van chưa mở)."),
    ("Van an toàn sẽ mở khi nhiệt độ khí đạt 600 K.", True,
     "Đúng. T₂ = T₁·p₂/p₁ = 300 · 5,0/2,5 = 600 K."),
    ("Nhiệt độ đó tương ứng với 54 °C.", False,
     "Sai. 600 K tương ứng với 600 − 273 = 327 °C. Giá trị 54 °C là kết quả của sai lầm nhân đôi nhiệt "
     "độ Celsius."),
    ("Nếu ban đầu bình chỉ chứa một nửa lượng khí nói trên (vẫn ở 27 °C) thì van sẽ mở ở nhiệt độ cao hơn.", True,
     "Đúng. Nửa lượng khí ở cùng V và T cho áp suất ban đầu 1,25·10⁵ Pa; khi đó T₂ = 300 · 5,0/1,25 = "
     "1200 K, cao hơn nhiều.")],
   "Quá trình đẳng tích – an toàn kĩ thuật", TB, fig="k_sd_binhkhi",
   cap="Bình khí nén có van an toàn"),

ds("Xét các đường biểu diễn quá trình của khí lí tưởng trong các hệ toạ độ khác nhau.",
   [("Trong hệ (p, V), đường đẳng nhiệt là một nhánh hypebol.", True,
     "Đúng. pV = hằng số ⟹ p = const/V."),
    ("Trong hệ (V, T), đường đẳng áp là đường thẳng đi qua gốc toạ độ.", True,
     "Đúng. V = (nR/p)T là hàm bậc nhất thuần nhất của T."),
    ("Trong hệ (V, T), đường đẳng áp ứng với áp suất càng lớn thì càng dốc.", False,
     "Sai. Hệ số góc nR/p tỉ lệ NGHỊCH với áp suất, nên áp suất càng lớn thì đường càng THOẢI."),
    ("Trong hệ (p, T), đường đẳng tích ứng với thể tích càng nhỏ thì càng dốc.", True,
     "Đúng. Hệ số góc nR/V tỉ lệ nghịch với V nên thể tích càng nhỏ, đường càng dốc.")],
   "Đồ thị các đẳng quá trình", TB, fig="k_dt_dangap",
   cap="Đường đẳng áp trong hệ toạ độ (V, T)"),

ds("Một bình thể tích 8,31 L chứa khí lí tưởng ở 300 K và áp suất 3,0·10⁵ Pa. "
   "Cho R = 8,31 J/(mol·K), N_A = 6,02·10²³ mol⁻¹, k = 1,38·10⁻²³ J/K.",
   [("Số mol khí trong bình là 1,0 mol.", True,
     "Đúng. n = pV/(RT) = 3,0·10⁵ · 8,31·10⁻³/(8,31 · 300) = 1,0 mol."),
    ("Số phân tử khí trong bình là 6,02·10²³.", True,
     "Đúng. N = n·N_A = 1,0 · 6,02·10²³ = 6,02·10²³ phân tử."),
    ("Động năng tịnh tiến trung bình của một phân tử là 6,21·10⁻²¹ J.", True,
     "Đúng. W̄đ = (3/2)kT = 1,5 · 1,38·10⁻²³ · 300 = 6,21·10⁻²¹ J."),
    ("Nếu bơm thêm khí cùng loại vào bình mà vẫn giữ 300 K thì động năng tịnh tiến trung bình của mỗi "
     "phân tử tăng lên.", False,
     "Sai. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ. Bơm thêm khí làm tăng số phân tử và do đó tăng áp suất, "
     "nhưng động năng trung bình của MỖI phân tử không đổi.")],
   "Phương trình Clapeyron – số phân tử – động năng", TB),
],
P3=[
sa("Một bọt khí thể tích 3,0 cm³ ở nơi áp suất 4,0·10⁵ Pa nổi lên nơi áp suất 1,0·10⁵ Pa (nhiệt độ không "
   "đổi). Thể tích bọt khí lúc đó bằng bao nhiêu cm³?",
   "12", "V₂ = p₁V₁/p₂ = 4,0·10⁵ · 3,0/1,0·10⁵ = 12 cm³.", "Định luật Boyle", D),

sa("Đun nóng đẳng áp một lượng khí, thể tích tăng từ 4,0 L lên 5,0 L. Nhiệt độ ban đầu là 27 °C. "
   "Nhiệt độ lúc sau bằng bao nhiêu độ Celsius?",
   "102", "Đẳng áp: T₂ = T₁ · V₂/V₁ = 300 · 5,0/4,0 = 375 K ⟹ t₂ = 375 − 273 = 102 °C.",
   "Định luật Charles – bài toán ngược", D),

sa("Một bình kín thể tích không đổi chứa khí ở 27 °C, áp suất 2,5·10⁵ Pa. Van an toàn mở khi áp suất đạt "
   "5,0·10⁵ Pa. Van sẽ mở khi nhiệt độ đạt bao nhiêu độ C?",
   "327", "T₂ = 300 · 5,0/2,5 = 600 K ⟹ t₂ = 600 − 273 = 327 °C.",
   "Quá trình đẳng tích", TB),

sa("Một lượng khí ở 3,0·10⁵ Pa, 2,0 L, 300 K được nén tới 1,0 L và đun tới 400 K. Áp suất lúc sau bằng "
   "bao nhiêu (đơn vị 10⁵ Pa)?",
   "8", "p₂ = p₁V₁T₂/(T₁V₂) = 3,0·10⁵ · 2,0 · 400/(300 · 1,0) = 8,0·10⁵ Pa.",
   "Phương trình trạng thái", TB),

sa("Một bình 16,62 L chứa khí lí tưởng ở 300 K, áp suất 1,0·10⁵ Pa. Số mol khí trong bình bằng bao nhiêu "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho R = 8,31 J/(mol·K).",
   "0,7",
   "n = pV/(RT) = 1,0·10⁵ · 16,62·10⁻³/(8,31 · 300) = 1662/2493 ≈ 0,67 ≈ 0,7 mol.",
   "Phương trình Clapeyron", TB),

sa("Ở nhiệt độ nào (tính bằng kelvin) thì động năng tịnh tiến trung bình của một phân tử khí lí tưởng "
   "bằng 8,28·10⁻²¹ J? Cho k = 1,38·10⁻²³ J/K.",
   "400",
   "W̄đ = (3/2)kT ⟹ T = 2W̄đ/(3k) = 2 · 8,28·10⁻²¹/(3 · 1,38·10⁻²³) = 1,656·10⁻²⁰/4,14·10⁻²³ = 400 K.",
   "Động năng phân tử và nhiệt độ", TB),
])


BOYLE_TBL = ("Số liệu thí nghiệm kiểm chứng định luật Boyle (nhiệt độ phòng không đổi)",
             ["V (cm³)", "10", "12", "15", "20", "30"],
             [["p (10⁵ Pa)", "6,0", "5,0", "4,0", "3,0", "2,0"],
              ["1/V (10⁻² cm⁻³)", "10,0", "8,33", "6,67", "5,00", "3,33"]])

CHARLES_TBL = ("Số liệu thí nghiệm kiểm chứng định luật Charles (áp suất không đổi)",
               ["t (°C)", "0", "20", "40", "60", "80"],
               [["V (cm³)", "20,0", "21,5", "22,9", "24,4", "25,9"],
                ["T (K)", "273", "293", "313", "333", "353"]])


# =====================================================================
DE3 = dict(
ma="12C2-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Xử lí số liệu và đồ thị của hai thí nghiệm kiểm chứng định luật Boyle và định luật Charles",
P1=[
mc("Bảng số liệu bên là kết quả thí nghiệm kiểm chứng định luật Boyle. Đại lượng nào giữ nguyên giá trị "
   "trong cả năm lần đo?",
   ["p + V.", "p·V.", "p/V.", "V/p."],
   "B",
   "Nhân từng cặp: 6,0·10 = 5,0·12 = 4,0·15 = 3,0·20 = 2,0·30 = 60 (10⁵ Pa·cm³). Tích p·V là hằng số, "
   "đúng như định luật Boyle.",
   "Xử lí số liệu thực nghiệm", D, tbl=BOYLE_TBL),

mc("Với bộ số liệu đó, nếu vẽ đồ thị p theo 1/V thì đồ thị có dạng",
   ["đường thẳng đi qua gốc toạ độ.", "đường thẳng không đi qua gốc toạ độ.",
    "nhánh hypebol.", "đường parabol."],
   "A",
   "Từ pV = C suy ra p = C·(1/V) — hàm bậc nhất thuần nhất của biến 1/V, nên đồ thị là đường thẳng đi "
   "qua gốc toạ độ với hệ số góc C.",
   "Biến đổi đồ thị", TB, fig="k_dt_boyle_1V",
   cap="Đồ thị p theo 1/V dựng từ số liệu thực nghiệm"),

mc("Hệ số góc của đường thẳng p theo 1/V trong thí nghiệm trên bằng",
   ["20·10⁵ Pa·cm³.", "40·10⁵ Pa·cm³.", "60·10⁵ Pa·cm³.", "120·10⁵ Pa·cm³."],
   "C",
   "Hệ số góc chính là hằng số C = p·V = 60·10⁵ Pa·cm³ (đọc trực tiếp từ bảng số liệu).",
   "Xử lí số liệu thực nghiệm", TB, fig="k_dt_boyle_1V", cap="Đồ thị p theo 1/V"),

mc("Dùng chính bộ số liệu trên, nếu nén khí tới thể tích 8,0 cm³ (nhiệt độ không đổi) thì áp suất khí bằng",
   ["6,0·10⁵ Pa.", "7,5·10⁵ Pa.", "8,0·10⁵ Pa.", "9,6·10⁵ Pa."],
   "B", "p = C/V = 60·10⁵/8,0 = 7,5·10⁵ Pa.", "Định luật Boyle – dự đoán", TB, tbl=BOYLE_TBL),

mc("Bảng số liệu thí nghiệm kiểm chứng định luật Charles cho thấy đại lượng nào là hằng số?",
   ["V·T.", "V/T.", "V/t (t tính bằng °C).", "V − T."],
   "B",
   "Tính V/T cho từng cột: 20,0/273 ≈ 21,5/293 ≈ 22,9/313 ≈ 24,4/333 ≈ 25,9/353 ≈ 0,0733 cm³/K. "
   "Chú ý phải dùng nhiệt độ tuyệt đối T, không dùng t (°C).",
   "Xử lí số liệu thực nghiệm", TB, tbl=CHARLES_TBL),

mc("Trong thí nghiệm kiểm chứng định luật Charles, nếu vẽ đồ thị V theo t (°C) rồi kéo dài đường thẳng "
   "về phía nhiệt độ thấp thì nó cắt trục hoành tại",
   ["0 °C.", "−100 °C.", "−273 °C.", "không cắt trục hoành."],
   "C",
   "V = (nR/p)(t + 273) triệt tiêu khi t = −273 °C. Chính phép ngoại suy này là một trong những cách "
   "lịch sử để xác định độ không tuyệt đối.",
   "Định luật Charles – ngoại suy", TB, fig="k_dt_charles",
   cap="Đồ thị V theo t và phép ngoại suy tới −273 °C"),

mc("Trong thí nghiệm ở hình bên, cột khí bị giam bởi một giọt thuỷ ngân trong ống nghiệm nhúng trong nước. "
   "Vai trò của giọt thuỷ ngân là",
   ["làm tăng áp suất khí bị giam.",
    "giữ cho lượng khí không đổi và bảo đảm áp suất khí luôn bằng áp suất khí quyển cộng thêm một lượng "
    "không đổi.",
    "đo nhiệt độ của khí.",
    "làm giảm thể tích khí."],
   "B",
   "Giọt thuỷ ngân vừa “nút” không cho khí thoát ra (lượng khí không đổi), vừa dịch chuyển tự do nên áp "
   "suất khí giữ nguyên — nhờ đó thí nghiệm là quá trình ĐẲNG ÁP, đúng điều kiện của định luật Charles.",
   "Thiết kế thí nghiệm", TB, fig="k_sd_tn_charles",
   cap="Thí nghiệm kiểm chứng định luật Charles"),

mc("Trong thí nghiệm kiểm chứng định luật Boyle bằng xilanh, để bảo đảm quá trình là đẳng nhiệt, cần",
   ["nén thật nhanh để khí không kịp trao đổi nhiệt.",
    "nén thật chậm và chờ một lúc trước mỗi lần đọc số liệu.",
    "làm nóng xilanh trước khi nén.",
    "để xilanh trong nước đá."],
   "B",
   "Nén chậm và chờ cân bằng nhiệt với môi trường thì nhiệt độ khí luôn bằng nhiệt độ phòng. Nén nhanh "
   "làm khí nóng lên (quá trình gần đoạn nhiệt), khi đó pV KHÔNG còn là hằng số.",
   "Thiết kế thí nghiệm", K, fig="k_sd_tn_boyle",
   cap="Bộ thí nghiệm kiểm chứng định luật Boyle"),

mc("Một lượng khí ở 27 °C có thể tích 5,0 L. Làm lạnh đẳng áp tới thể tích 4,0 L. Nhiệt độ lúc sau là",
   ["−33 °C.", "−13 °C.", "21,6 °C.", "240 °C."],
   "A",
   "T₂ = T₁·V₂/V₁ = 300 · 4,0/5,0 = 240 K ⟹ t₂ = 240 − 273 = −33 °C.",
   "Định luật Charles", TB),

mc("Một khối khí lí tưởng biến đổi từ trạng thái (p₁, V₁, T₁) sang (p₂, V₂, T₂). Hệ thức nào sau đây "
   "luôn đúng nếu lượng khí không đổi?",
   ["p₁V₁ = p₂V₂.", "V₁/T₁ = V₂/T₂.", "p₁/T₁ = p₂/T₂.", "p₁V₁/T₁ = p₂V₂/T₂."],
   "D",
   "Ba hệ thức đầu chỉ đúng trong các trường hợp riêng (đẳng nhiệt, đẳng áp, đẳng tích). Hệ thức tổng "
   "quát cho mọi quá trình của một lượng khí xác định là pV/T = hằng số.",
   "Phương trình trạng thái", TB),

mc("Trong hệ toạ độ (p, V), quá trình đẳng tích được biểu diễn bằng",
   ["đoạn thẳng song song với trục V.", "đoạn thẳng song song với trục p.",
    "nhánh hypebol.", "đường thẳng qua gốc toạ độ."],
   "B",
   "Đẳng tích nghĩa là V không đổi, nên trên hệ (p, V) điểm biểu diễn chỉ di chuyển theo phương thẳng "
   "đứng — đoạn thẳng song song với trục p.",
   "Đồ thị các đẳng quá trình", TB, fig="k_dt_baquatrinh",
   cap="Ba quá trình xuất phát từ cùng trạng thái M"),

mc("Hình vẽ biểu diễn ba quá trình (a), (b), (c) xuất phát từ cùng trạng thái M của một lượng khí lí "
   "tưởng. Quá trình nào là đẳng nhiệt?",
   ["Quá trình (a).", "Quá trình (b).", "Quá trình (c).", "Không quá trình nào."],
   "C",
   "Đường (a) thẳng đứng ⟹ đẳng tích; đường (b) nằm ngang ⟹ đẳng áp; đường (c) là nhánh hypebol ⟹ "
   "đẳng nhiệt.",
   "Nhận dạng quá trình trên đồ thị", TB, fig="k_dt_baquatrinh",
   cap="Ba quá trình xuất phát từ cùng trạng thái M"),

mc("Áp suất khí theo mô hình động học phân tử được tính bằng công thức p = (1/3)·μ·m·v̄², trong đó μ là",
   ["khối lượng của một phân tử.", "số phân tử trong một đơn vị thể tích.",
    "tổng số phân tử trong bình.", "khối lượng riêng của khí."],
   "B",
   "μ = N/V là MẬT ĐỘ phân tử (số phân tử trong một đơn vị thể tích), m là khối lượng một phân tử và "
   "v̄² là trung bình bình phương tốc độ.",
   "Áp suất theo mô hình động học phân tử", TB),

mc("Nếu giữ nguyên nhiệt độ mà tăng mật độ phân tử khí lên 2 lần thì áp suất khí",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "giảm 2 lần."],
   "B",
   "p = (1/3)μ·m·v̄². Nhiệt độ không đổi ⟹ v̄² không đổi ⟹ p tỉ lệ thuận với μ, nên áp suất tăng 2 lần.",
   "Áp suất theo mô hình động học phân tử", TB),

mc("Một lượng khí lí tưởng có khối lượng m và khối lượng mol M. Số mol khí bằng",
   ["thương của khối lượng mol chia cho khối lượng khí.",
    "thương của khối lượng khí chia cho khối lượng mol.",
    "tích của khối lượng khí và khối lượng mol.",
    "tích của khối lượng khí và số Avogadro."],
   "B",
   "n = m/M. Ví dụ 64 g khí oxi (M = 32 g/mol) ứng với n = 64/32 = 2 mol. Từ đó phương trình Clapeyron "
   "thường được viết là pV = (m/M)RT.",
   "Số mol", D),

mc("Trong bình kín chứa 32 g khí oxi (M = 32 g/mol) ở 300 K, thể tích 8,31 L. Áp suất khí trong bình là "
   "(R = 8,31 J/(mol·K))",
   ["1,0·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa.", "5,0·10⁵ Pa."],
   "C",
   "n = 32/32 = 1,0 mol ⟹ p = nRT/V = 1,0 · 8,31 · 300/(8,31·10⁻³) = 2493/8,31·10⁻³ = 3,0·10⁵ Pa.",
   "Phương trình Clapeyron", TB),

mc("Hai bình giống hệt nhau, cùng nhiệt độ, một bình chứa khí hiđrô, bình kia chứa khí oxi, áp suất trong "
   "hai bình bằng nhau. Kết luận nào sau đây ĐÚNG?",
   ["Hai bình chứa cùng số phân tử khí.",
    "Bình chứa oxi có nhiều phân tử hơn.",
    "Bình chứa hiđrô có nhiều phân tử hơn.",
    "Hai bình có cùng khối lượng khí."],
   "A",
   "Từ p = (N/V)kT, khi p, V, T như nhau thì N như nhau — không phụ thuộc loại khí. Khối lượng khí thì "
   "khác nhau vì khối lượng mỗi phân tử khác nhau.",
   "Phương trình trạng thái – so sánh", K),

mc("Ở cùng điều kiện nhiệt độ và áp suất, so sánh khối lượng riêng của khí oxi (M = 32 g/mol) và khí "
   "heli (M = 4 g/mol):",
   ["Bằng nhau.", "Oxi lớn gấp 8 lần heli.",
    "Heli lớn gấp 8 lần oxi.", "Oxi lớn gấp 4 lần heli."],
   "B",
   "Từ pV = (m/M)RT suy ra ρ = m/V = pM/(RT). Ở cùng p và T, ρ tỉ lệ thuận với M:\n"
   "ρ_O₂/ρ_He = 32/4 = 8.",
   "Khối lượng riêng của khí", K),
],
P2=[
ds("Bảng bên là số liệu của một nhóm học sinh khi kiểm chứng định luật Boyle ở nhiệt độ phòng không đổi.",
   [("Tích p·V của cả năm lần đo đều bằng 60·10⁵ Pa·cm³.", True,
     "Đúng. 6,0·10 = 5,0·12 = 4,0·15 = 3,0·20 = 2,0·30 = 60 (10⁵ Pa·cm³)."),
    ("Đồ thị p theo V là một đường thẳng.", False,
     "Sai. p = C/V nên đồ thị p theo V là một nhánh HYPEBOL. Muốn có đường thẳng phải vẽ p theo 1/V."),
    ("Đồ thị p theo 1/V là đường thẳng đi qua gốc toạ độ, hệ số góc bằng 60·10⁵ Pa·cm³.", True,
     "Đúng. p = C·(1/V) với C = 60·10⁵ Pa·cm³ chính là hệ số góc."),
    ("Nếu tiếp tục nén tới V = 8,0 cm³ thì áp suất dự đoán là 7,5·10⁵ Pa.", True,
     "Đúng. p = 60·10⁵/8,0 = 7,5·10⁵ Pa.")],
   "Xử lí số liệu – biến đổi đồ thị", TB, tbl=BOYLE_TBL,
   fig="k_dt_boyle_1V", cap="Đồ thị p theo 1/V"),

ds("Bảng bên là số liệu của thí nghiệm kiểm chứng định luật Charles ở áp suất không đổi.",
   [("Tỉ số V/t (với t tính bằng °C) là hằng số.", False,
     "Sai. Ở cột đầu t = 0 °C nên V/t không xác định. Đại lượng là hằng số phải là V/T với T là nhiệt độ "
     "TUYỆT ĐỐI: V/T ≈ 0,0733 cm³/K ở cả năm lần đo."),
    ("Tỉ số V/T của cả năm lần đo đều xấp xỉ 0,0733 cm³/K.", True,
     "Đúng. 20,0/273 ≈ 0,0733; 21,5/293 ≈ 0,0734; 22,9/313 ≈ 0,0732; 24,4/333 ≈ 0,0733; "
     "25,9/353 ≈ 0,0734."),
    ("Đồ thị V theo T (K) là đường thẳng đi qua gốc toạ độ.", True,
     "Đúng. V = (nR/p)·T là hàm bậc nhất thuần nhất của T."),
    ("Kéo dài đồ thị V theo t (°C) về phía nhiệt độ thấp, nó cắt trục hoành tại −273 °C.", True,
     "Đúng. Thể tích ngoại suy triệt tiêu ở độ không tuyệt đối; đây là một cách xác định giá trị −273 °C "
     "bằng thực nghiệm.")],
   "Xử lí số liệu – ngoại suy", K, tbl=CHARLES_TBL, fig="k_dt_charles",
   cap="Đồ thị V theo t và phép ngoại suy"),

ds("Xét cách bố trí và tiến hành hai thí nghiệm kiểm chứng định luật Boyle và định luật Charles.",
   [("Trong thí nghiệm Boyle, phải nén khí chậm và chờ cân bằng nhiệt trước mỗi lần đọc số liệu.", True,
     "Đúng. Chỉ khi đó nhiệt độ khí mới luôn bằng nhiệt độ phòng, bảo đảm quá trình là đẳng nhiệt."),
    ("Trong thí nghiệm Charles, giọt thuỷ ngân vừa giữ kín lượng khí vừa bảo đảm áp suất khí không đổi.", True,
     "Đúng. Giọt thuỷ ngân dịch chuyển tự do nên áp suất khí luôn bằng áp suất khí quyển cộng thêm phần "
     "do trọng lượng giọt gây ra — một lượng không đổi."),
    ("Trong thí nghiệm Charles, cần nhúng ống nghiệm vào nước và khuấy đều để nhiệt độ khí bằng nhiệt độ "
     "nước đo được bằng nhiệt kế.", True,
     "Đúng. Khuấy đều bảo đảm nước có nhiệt độ đồng nhất và khí trong ống đạt cùng nhiệt độ đó, nếu không "
     "số chỉ nhiệt kế sẽ không đại diện cho nhiệt độ khí."),
    ("Nếu trong thí nghiệm Boyle có một chỗ hở nhỏ làm khí thoát dần ra ngoài thì tích p·V vẫn là hằng số.", False,
     "Sai. Định luật Boyle chỉ đúng với LƯỢNG KHÍ XÁC ĐỊNH. Khí thoát bớt ra thì n giảm, tích pV = nRT "
     "cũng giảm dần theo.")],
   "Thiết kế và phân tích thí nghiệm", K, fig="k_sd_tn_boyle",
   cap="Bộ thí nghiệm kiểm chứng định luật Boyle"),

ds("Hình bên biểu diễn ba quá trình (a), (b), (c) của một lượng khí lí tưởng xác định, đều xuất phát từ "
   "trạng thái M trên giản đồ (p, V).",
   [("Quá trình (a) là quá trình đẳng tích.", True,
     "Đúng. Đường (a) là đoạn thẳng đứng: thể tích không đổi, áp suất tăng."),
    ("Trong quá trình (a), nhiệt độ của khí tăng lên.", True,
     "Đúng. V không đổi mà p tăng thì tích pV tăng, do đó nhiệt độ tăng."),
    ("Quá trình (b) là quá trình đẳng áp và nhiệt độ khí giảm.", False,
     "Sai ở vế sau. Đường (b) nằm ngang nên đúng là đẳng áp, nhưng thể tích TĂNG (đi sang phải) nên tích "
     "pV tăng, nhiệt độ khí TĂNG chứ không giảm."),
    ("Trong quá trình (c), tích p·V giữ nguyên giá trị.", True,
     "Đúng. (c) là nhánh hypebol, tức quá trình đẳng nhiệt, nên pV = hằng số.")],
   "Nhận dạng quá trình trên đồ thị", K, fig="k_dt_baquatrinh",
   cap="Ba quá trình xuất phát từ trạng thái M"),
],
P3=[
sa("Từ bộ số liệu thí nghiệm Boyle (p·V = 60·10⁵ Pa·cm³), nếu nén khí tới thể tích 5,0 cm³ thì áp suất "
   "khí bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "12", "p = C/V = 60·10⁵/5,0 = 12·10⁵ Pa.", "Định luật Boyle – dự đoán", TB, tbl=BOYLE_TBL),

sa("Một lượng khí ở 27 °C có thể tích 5,0 L. Làm lạnh đẳng áp tới 4,0 L. Nhiệt độ lúc sau bằng bao nhiêu "
   "kelvin?",
   "240", "T₂ = T₁·V₂/V₁ = 300 · 4,0/5,0 = 240 K (tức −33 °C).", "Định luật Charles", TB),

sa("Bình kín 8,31 L chứa 32 g khí oxi (M = 32 g/mol) ở 300 K. Áp suất khí trong bình bằng bao nhiêu "
   "(đơn vị 10⁵ Pa)? Cho R = 8,31 J/(mol·K).",
   "3",
   "n = 32/32 = 1,0 mol ⟹ p = nRT/V = 1,0 · 8,31 · 300/(8,31·10⁻³) = 3,0·10⁵ Pa.",
   "Phương trình Clapeyron", TB),

sa("Ở cùng nhiệt độ và áp suất, khối lượng riêng của khí oxi (M = 32 g/mol) lớn gấp bao nhiêu lần khối "
   "lượng riêng của khí heli (M = 4 g/mol)?",
   "8", "ρ = pM/(RT) nên ở cùng p, T thì ρ tỉ lệ thuận với M: 32/4 = 8 lần.",
   "Khối lượng riêng của khí", K),

sa("Từ số liệu thí nghiệm Charles (V/T ≈ 0,0733 cm³/K), thể tích cột khí ở 100 °C bằng bao nhiêu cm³ "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "27,3",
   "T = 100 + 273 = 373 K ⟹ V = 0,0733 · 373 ≈ 27,3 cm³.",
   "Định luật Charles – dự đoán", TB, tbl=CHARLES_TBL),

sa("Nếu giữ nguyên nhiệt độ và tăng mật độ phân tử khí lên 2,5 lần thì áp suất khí tăng bao nhiêu lần?",
   "2,5",
   "p = (1/3)μ·m·v̄². Nhiệt độ không đổi nên v̄² không đổi, p tỉ lệ thuận với mật độ μ ⟹ tăng 2,5 lần.",
   "Áp suất theo mô hình động học phân tử", TB),
])


# =====================================================================
DE4 = dict(
ma="12C2-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Áp suất khí trong xilanh có pit-tông; chu trình trên giản đồ p–V; bơm khí và bóng thám không",
P1=[
mc("Một xilanh thẳng đứng, miệng hướng lên, chứa khí bị nhốt dưới một pit-tông khối lượng m, tiết diện S, "
   "dịch chuyển không ma sát. Áp suất khí quyển là p₀. Áp suất khí trong xilanh bằng",
   ["p₀.", "p₀ + mg/S.", "p₀ − mg/S.", "mg/S."],
   "B",
   "Pit-tông cân bằng dưới ba lực: trọng lực mg hướng xuống, lực do khí quyển p₀S hướng xuống và lực do "
   "khí bên trong pS hướng lên.\n"
   "pS = p₀S + mg ⟹ p = p₀ + mg/S.",
   "Áp suất khí trong xilanh", TB, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông và quả nặng"),

mc("Xilanh thẳng đứng có pit-tông khối lượng 2,0 kg, tiết diện 20 cm², miệng hướng lên. Áp suất khí quyển "
   "10⁵ Pa, g = 10 m/s². Áp suất khí trong xilanh là",
   ["0,90·10⁵ Pa.", "1,00·10⁵ Pa.", "1,10·10⁵ Pa.", "2,00·10⁵ Pa."],
   "C",
   "S = 20 cm² = 2,0·10⁻³ m²; mg/S = 2,0 · 10/2,0·10⁻³ = 1,0·10⁴ Pa.\n"
   "p = 10⁵ + 0,1·10⁵ = 1,10·10⁵ Pa.",
   "Áp suất khí trong xilanh", TB, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

mc("Vẫn với xilanh ở câu trên, nếu đặt thêm lên pit-tông một quả nặng 2,0 kg thì áp suất khí trong xilanh "
   "trở thành",
   ["1,10·10⁵ Pa.", "1,20·10⁵ Pa.", "1,30·10⁵ Pa.", "2,20·10⁵ Pa."],
   "B",
   "Tổng khối lượng đè lên khí là 4,0 kg ⟹ thêm áp suất 4,0 · 10/2,0·10⁻³ = 2,0·10⁴ Pa.\n"
   "p = 10⁵ + 0,2·10⁵ = 1,20·10⁵ Pa.",
   "Áp suất khí trong xilanh", TB, fig="k_sd_xilanh_quanang",
   cap="Xilanh có đặt thêm quả nặng"),

mc("Nếu lật ngược xilanh ở câu trên cho miệng hướng xuống (pit-tông vẫn dịch chuyển không ma sát) thì áp "
   "suất khí trong xilanh bằng",
   ["0,90·10⁵ Pa.", "1,00·10⁵ Pa.", "1,10·10⁵ Pa.", "1,20·10⁵ Pa."],
   "A",
   "Khi miệng hướng xuống, trọng lực của pit-tông kéo pit-tông ra xa khối khí nên áp suất khí NHỎ hơn "
   "áp suất khí quyển: p = p₀ − mg/S = 10⁵ − 0,1·10⁵ = 0,90·10⁵ Pa.",
   "Áp suất khí trong xilanh", K),

mc("Hình vẽ là chu trình 1 → 2 → 3 → 4 → 1 của một lượng khí lí tưởng. Quá trình 1 → 2 là",
   ["đẳng nhiệt.", "đẳng áp.", "đẳng tích.", "không phải đẳng quá trình nào."],
   "C",
   "Trên giản đồ (p, V), đoạn 1 → 2 thẳng đứng nghĩa là thể tích không đổi ⟹ quá trình đẳng tích "
   "(áp suất tăng từ 1·10⁵ Pa lên 3·10⁵ Pa).",
   "Nhận dạng quá trình trên đồ thị", D, fig="k_dt_chutrinh",
   cap="Chu trình gồm hai quá trình đẳng tích và hai quá trình đẳng áp"),

mc("Vẫn với chu trình ở hình trên, tỉ số giữa nhiệt độ ở trạng thái (3) và nhiệt độ ở trạng thái (1) bằng",
   ["3.", "6.", "9.", "12."],
   "C",
   "T tỉ lệ thuận với tích pV (lượng khí không đổi).\n"
   "(pV)₁ = 1 · 1 = 1;  (pV)₃ = 3 · 3 = 9 (đơn vị 10⁵ Pa·L)\n"
   "⟹ T₃/T₁ = 9.",
   "Đọc giản đồ p–V", TB, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Vẫn với chu trình đó, hai trạng thái nào có cùng nhiệt độ?",
   ["(1) và (3).", "(2) và (4).", "(1) và (2).", "(3) và (4)."],
   "B",
   "(pV)₂ = 1 · 3 = 3 và (pV)₄ = 3 · 1 = 3 (đơn vị 10⁵ Pa·L) ⟹ T₂ = T₄.\n"
   "Hai trạng thái này nằm trên cùng một đường đẳng nhiệt.",
   "Đọc giản đồ p–V", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

mc("Dùng bơm tay có thể tích xilanh 0,20 L để bơm không khí ở áp suất 10⁵ Pa vào một quả bóng có thể tích "
   "không đổi 2,0 L, trong bóng đã có sẵn không khí ở 10⁵ Pa. Sau 10 lần bơm (nhiệt độ không đổi), áp "
   "suất khí trong bóng là",
   ["1,5·10⁵ Pa.", "2,0·10⁵ Pa.", "2,5·10⁵ Pa.", "3,0·10⁵ Pa."],
   "B",
   "Toàn bộ lượng khí cuối cùng trong bóng gồm khí có sẵn và khí được bơm vào; ở cùng nhiệt độ ta cộng "
   "được các tích pV:\n"
   "p·2,0 = 10⁵ · 2,0 + 10 · 10⁵ · 0,20 = 2,0·10⁵ + 2,0·10⁵ = 4,0·10⁵ (Pa·L)\n"
   "⟹ p = 2,0·10⁵ Pa. Bẫy thường gặp là quên phần khí đã có sẵn trong bóng.",
   "Bơm khí – phương trình trạng thái", K, fig="k_sd_bomxe", cap="Bơm khí vào lốp/bóng"),

mc("Một bóng thám không có thể tích 10 m³ ở mặt đất (áp suất 10⁵ Pa, nhiệt độ 27 °C). Khi lên tới độ cao "
   "mà áp suất còn 0,50·10⁵ Pa và nhiệt độ là −13 °C, thể tích bóng là",
   ["13,0 m³.", "15,6 m³.", "17,3 m³.", "20,0 m³."],
   "C",
   "T₁ = 300 K, T₂ = 260 K.\n"
   "V₂ = V₁·p₁·T₂/(p₂·T₁) = 10 · 10⁵ · 260/(0,50·10⁵ · 300) = 10 · 260/150 ≈ 17,3 m³.\n"
   "Áp suất giảm làm bóng nở ra, nhiệt độ giảm làm bóng co lại; tác dụng của áp suất mạnh hơn.",
   "Phương trình trạng thái – thực tiễn", K, fig="k_sd_bongbay",
   cap="Bóng thám không ở mặt đất và ở độ cao lớn"),

mc("Một lượng khí lí tưởng thực hiện quá trình đẳng áp. Nếu nhiệt độ tuyệt đối tăng 25% thì thể tích khí",
   ["tăng 25%.", "tăng 20%.", "giảm 20%.", "không đổi."],
   "A", "Đẳng áp ⟹ V tỉ lệ thuận với T, nên T tăng 25% thì V cũng tăng 25%.",
   "Định luật Charles", TB),

mc("Trong hệ toạ độ (p, T), quá trình đẳng áp được biểu diễn bằng",
   ["đường thẳng qua gốc toạ độ.", "đường thẳng song song với trục T.",
    "đường thẳng song song với trục p.", "nhánh hypebol."],
   "B",
   "Đẳng áp nghĩa là p không đổi, nên trên hệ (p, T) điểm biểu diễn di chuyển theo phương ngang — đường "
   "thẳng song song với trục T.",
   "Đồ thị các đẳng quá trình", TB),

mc("Ở điều kiện tiêu chuẩn (0 °C; 1,013·10⁵ Pa), thể tích của 1 mol khí lí tưởng gần nhất với "
   "(R = 8,31 J/(mol·K))",
   ["11,2 L.", "22,4 L.", "24,0 L.", "44,8 L."],
   "B",
   "V = nRT/p = 1 · 8,31 · 273/1,013·10⁵ ≈ 2268/1,013·10⁵ ≈ 2,24·10⁻² m³ = 22,4 L.\n"
   "Đây là con số quen thuộc: thể tích mol ở điều kiện tiêu chuẩn.",
   "Phương trình Clapeyron", TB),

mc("Khi nhiệt độ khí trong một bình kín tăng lên, số va chạm của phân tử khí lên thành bình trong mỗi "
   "giây và động lượng mỗi va chạm sẽ",
   ["đều giảm.", "đều tăng.", "số va chạm tăng, động lượng mỗi va chạm giảm.",
    "số va chạm giảm, động lượng mỗi va chạm tăng."],
   "B",
   "Nhiệt độ tăng làm tốc độ phân tử tăng: chúng vừa va chạm thường xuyên hơn, vừa truyền cho thành bình "
   "một động lượng lớn hơn mỗi lần va chạm. Cả hai đều làm áp suất tăng.",
   "Áp suất theo mô hình động học phân tử", TB, fig="k_sd_mohinh",
   cap="Va chạm phân tử lên thành bình"),

mc("Một lượng khí có khối lượng 4,0 g, khối lượng mol 16 g/mol, ở 300 K và thể tích 4,155 L. Áp suất khí là "
   "(R = 8,31 J/(mol·K))",
   ["0,5·10⁵ Pa.", "1,0·10⁵ Pa.", "1,5·10⁵ Pa.", "2,0·10⁵ Pa."],
   "C",
   "n = 4,0/16 = 0,25 mol.\n"
   "p = nRT/V = 0,25 · 8,31 · 300/(4,155·10⁻³) = 623,25/4,155·10⁻³ = 1,5·10⁵ Pa.",
   "Phương trình Clapeyron", TB),

mc("Nếu tăng nhiệt độ tuyệt đối của khí lên 4 lần thì tốc độ căn quân phương của phân tử khí",
   ["tăng 2 lần.", "tăng 4 lần.", "tăng 8 lần.", "tăng 16 lần."],
   "A",
   "Từ (1/2)m·v̄² = (3/2)kT suy ra v ∝ √T. Nhiệt độ tăng 4 lần thì tốc độ tăng √4 = 2 lần.",
   "Động năng phân tử – tốc độ", K),

mc("Hai bình kín cùng thể tích, cùng nhiệt độ, chứa cùng một loại khí. Áp suất trong bình A gấp đôi bình B. "
   "Kết luận nào đúng?",
   ["Khối lượng khí trong bình A gấp đôi bình B.",
    "Động năng trung bình của phân tử trong bình A gấp đôi bình B.",
    "Tốc độ trung bình của phân tử trong bình A gấp đôi bình B.",
    "Thể tích mỗi phân tử trong bình A gấp đôi bình B."],
   "A",
   "p = (N/V)kT: cùng V và T thì p tỉ lệ thuận với N, do đó số phân tử và khối lượng khí trong A gấp đôi B. "
   "Động năng và tốc độ trung bình chỉ phụ thuộc nhiệt độ nên bằng nhau ở hai bình.",
   "Phương trình trạng thái – mô hình phân tử", K),

mc("Một quả bóng bay chứa khí heli được thả ra và bay lên cao. Nguyên nhân bóng nở to dần rồi có thể nổ là",
   ["nhiệt độ không khí tăng theo độ cao.",
    "áp suất khí quyển giảm theo độ cao nên khí bên trong nở ra.",
    "khối lượng khí trong bóng tăng lên.",
    "vỏ bóng co lại vì lạnh."],
   "B",
   "Càng lên cao áp suất khí quyển càng giảm; áp suất bên ngoài giảm thì khí bên trong giãn nở để cân "
   "bằng, làm bóng phồng to dần. Nhiệt độ giảm theo độ cao chỉ làm giảm bớt phần nào hiệu ứng này.",
   "Phương trình trạng thái – thực tiễn", TB, fig="k_sd_bongbay",
   cap="Bóng bay ở mặt đất và ở độ cao lớn"),

mc("Trong quá trình đẳng nhiệt của một lượng khí lí tưởng, đồ thị nào sau đây là một đường thẳng?",
   ["p theo V.", "p theo 1/V.", "V theo T.", "p theo T."],
   "B",
   "pV = C ⟹ p = C·(1/V) là hàm bậc nhất của biến 1/V. Còn p theo V là hypebol; V theo T và p theo T "
   "không có ý nghĩa vì T không đổi.",
   "Biến đổi đồ thị", TB, fig="k_dt_boyle_1V", cap="Đồ thị p theo 1/V"),
],
P2=[
ds("Một xilanh thẳng đứng, tiết diện S = 20 cm², chứa khí bị nhốt dưới một pit-tông khối lượng 2,0 kg "
   "dịch chuyển không ma sát. Áp suất khí quyển 10⁵ Pa, g = 10 m/s².",
   [("Khi miệng xilanh hướng lên, áp suất khí trong xilanh là 1,10·10⁵ Pa.", True,
     "Đúng. p = p₀ + mg/S = 10⁵ + 2,0 · 10/(2,0·10⁻³) = 10⁵ + 10⁴ = 1,10·10⁵ Pa."),
    ("Khi lật ngược cho miệng xilanh hướng xuống, áp suất khí trong xilanh là 0,90·10⁵ Pa.", True,
     "Đúng. Lúc này trọng lực pit-tông kéo pit-tông ra xa khối khí: p = p₀ − mg/S = 0,90·10⁵ Pa."),
    ("Nếu đặt thêm quả nặng 2,0 kg lên pit-tông (miệng hướng lên) thì áp suất khí tăng thêm 0,2·10⁵ Pa "
     "so với khi chưa đặt.", False,
     "Sai. Quả nặng 2,0 kg chỉ làm áp suất tăng thêm 2,0 · 10/(2,0·10⁻³) = 0,1·10⁵ Pa (từ 1,10·10⁵ Pa "
     "lên 1,20·10⁵ Pa)."),
    ("Khi đặt xilanh nằm ngang, áp suất khí trong xilanh bằng đúng áp suất khí quyển.", True,
     "Đúng. Khi đó trọng lực pit-tông vuông góc với trục xilanh nên không tham gia vào phương trình cân "
     "bằng theo phương trục: p = p₀ = 10⁵ Pa.")],
   "Áp suất khí trong xilanh", K, fig="k_sd_xilanh_quanang",
   cap="Xilanh thẳng đứng có pit-tông"),

ds("Hình bên là chu trình 1 → 2 → 3 → 4 → 1 của một lượng khí lí tưởng xác định, với "
   "1(1 L; 1·10⁵ Pa), 2(1 L; 3·10⁵ Pa), 3(3 L; 3·10⁵ Pa), 4(3 L; 1·10⁵ Pa).",
   [("Quá trình 2 → 3 là quá trình đẳng áp và nhiệt độ khí tăng lên.", True,
     "Đúng. Áp suất giữ nguyên 3·10⁵ Pa còn thể tích tăng từ 1 L lên 3 L nên tích pV tăng, nhiệt độ tăng."),
    ("Nhiệt độ ở trạng thái (3) gấp 9 lần nhiệt độ ở trạng thái (1).", True,
     "Đúng. T ∝ pV: (pV)₃/(pV)₁ = (3·3)/(1·1) = 9."),
    ("Trạng thái (2) và trạng thái (4) có cùng nhiệt độ.", True,
     "Đúng. (pV)₂ = 1·3 = 3 và (pV)₄ = 3·1 = 3 nên T₂ = T₄; hai điểm này nằm trên cùng một đường đẳng nhiệt."),
    ("Trong quá trình 4 → 1, nhiệt độ của khí tăng lên.", False,
     "Sai. Quá trình 4 → 1 là đẳng áp ở p = 1·10⁵ Pa với thể tích giảm từ 3 L xuống 1 L, nên tích pV "
     "giảm ba lần và nhiệt độ GIẢM ba lần (từ T₄ về T₁).")],
   "Đọc giản đồ p–V", K, fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

ds("Dùng bơm tay có thể tích xilanh 0,20 L bơm không khí ở 10⁵ Pa vào một quả bóng thể tích không đổi "
   "2,0 L, trong bóng đã có sẵn không khí ở 10⁵ Pa. Nhiệt độ coi như không đổi.",
   [("Sau 10 lần bơm, áp suất khí trong bóng là 2,0·10⁵ Pa.", True,
     "Đúng. p·2,0 = 10⁵·2,0 + 10·10⁵·0,20 = 4,0·10⁵ (Pa·L) ⟹ p = 2,0·10⁵ Pa."),
    ("Sau 20 lần bơm, áp suất khí trong bóng là 3,0·10⁵ Pa.", True,
     "Đúng. p·2,0 = 10⁵·2,0 + 20·10⁵·0,20 = 6,0·10⁵ ⟹ p = 3,0·10⁵ Pa. Mỗi lần bơm làm áp suất tăng "
     "thêm đúng 0,1·10⁵ Pa."),
    ("Nếu quên phần không khí có sẵn trong bóng thì kết quả sau 10 lần bơm sẽ là 1,0·10⁵ Pa.", True,
     "Đúng. Khi đó p·2,0 = 10·10⁵·0,20 = 2,0·10⁵ ⟹ p = 1,0·10⁵ Pa — nhỏ hơn kết quả đúng đúng bằng "
     "áp suất ban đầu."),
    ("Áp suất trong bóng tăng theo cấp số nhân theo số lần bơm.", False,
     "Sai. Mỗi lần bơm đưa thêm cùng một lượng khí nên áp suất tăng theo CẤP SỐ CỘNG (thêm 0,1·10⁵ Pa "
     "mỗi lần), chứ không phải cấp số nhân.")],
   "Bơm khí – phương trình trạng thái", K, fig="k_sd_bomxe", cap="Bơm khí vào bóng"),

ds("Một bóng thám không thể tích 10 m³ ở mặt đất (10⁵ Pa; 27 °C) được thả lên cao, tới nơi có áp suất "
   "0,50·10⁵ Pa và nhiệt độ −13 °C. Vỏ bóng đàn hồi, khí trong bóng không thoát ra.",
   [("Phải dùng phương trình trạng thái pV/T = hằng số vì cả áp suất lẫn nhiệt độ đều thay đổi.", True,
     "Đúng. Không thể dùng riêng định luật Boyle hay Charles vì không có đại lượng nào được giữ không đổi."),
    ("Thể tích bóng ở độ cao đó vào khoảng 17,3 m³.", True,
     "Đúng. V₂ = 10 · 10⁵ · 260/(0,50·10⁵ · 300) ≈ 17,3 m³."),
    ("Việc áp suất giảm làm bóng nở ra, còn việc nhiệt độ giảm làm bóng co lại.", True,
     "Đúng. Hai tác dụng ngược chiều nhau; ở đây tác dụng của áp suất (nở 2 lần) mạnh hơn tác dụng của "
     "nhiệt độ (co còn 260/300 ≈ 0,87 lần)."),
    ("Khối lượng riêng của khí trong bóng ở độ cao đó lớn hơn ở mặt đất.", False,
     "Sai. Khối lượng khí không đổi mà thể tích tăng nên khối lượng riêng GIẢM "
     "(còn khoảng 10/17,3 ≈ 58% giá trị ở mặt đất).")],
   "Phương trình trạng thái – thực tiễn", K, fig="k_sd_bongbay",
   cap="Bóng thám không lên cao"),
],
P3=[
sa("Xilanh thẳng đứng miệng hướng lên, tiết diện 25 cm², pit-tông khối lượng 5,0 kg dịch chuyển không ma "
   "sát. Áp suất khí quyển 10⁵ Pa, g = 10 m/s². Áp suất khí trong xilanh bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "1,2",
   "S = 25 cm² = 2,5·10⁻³ m²; mg/S = 5,0 · 10/2,5·10⁻³ = 2,0·10⁴ Pa.\n"
   "p = 10⁵ + 0,2·10⁵ = 1,2·10⁵ Pa.",
   "Áp suất khí trong xilanh", TB, fig="k_sd_xilanh_quanang", cap="Xilanh có pit-tông"),

sa("Với chu trình ở hình bên, công mà khí sinh ra sau một chu trình bằng bao nhiêu jun?",
   "400",
   "Chu trình là hình chữ nhật trên giản đồ p–V nên công có ích bằng diện tích hình đó:\n"
   "A = Δp · ΔV = (3 − 1)·10⁵ · (3 − 1)·10⁻³ = 2,0·10⁵ · 2,0·10⁻³ = 400 J.",
   "Công trong chu trình kín", TB,
   fig="k_dt_chutrinh", cap="Chu trình trên giản đồ p–V"),

sa("Dùng bơm có thể tích xilanh 0,20 L bơm không khí ở 10⁵ Pa vào quả bóng thể tích 2,0 L đang chứa không "
   "khí ở 10⁵ Pa. Cần bơm bao nhiêu lần để áp suất trong bóng đạt 2,5·10⁵ Pa (nhiệt độ không đổi)?",
   "15",
   "p·V = p₀·V + n·p₀·V₀ ⟹ 2,5·10⁵·2,0 = 10⁵·2,0 + n·10⁵·0,20\n"
   "⟹ 5,0 = 2,0 + 0,20n (đơn vị 10⁵ Pa·L) ⟹ n = 15 lần.",
   "Bơm khí", K, fig="k_sd_bomxe", cap="Bơm khí vào bóng"),

sa("Một bóng thám không thể tích 8,0 m³ ở mặt đất (10⁵ Pa; 27 °C) lên tới nơi có áp suất 0,40·10⁵ Pa và "
   "nhiệt độ −23 °C. Thể tích bóng lúc đó bằng bao nhiêu m³ (làm tròn đến chữ số thập phân thứ nhất)?",
   "16,7",
   "T₁ = 300 K, T₂ = 250 K.\nV₂ = 8,0 · 10⁵ · 250/(0,40·10⁵ · 300) = 8,0 · 250/120 ≈ 16,7 m³.",
   "Phương trình trạng thái – thực tiễn", K, fig="k_sd_bongbay", cap="Bóng thám không"),

sa("Ở điều kiện tiêu chuẩn (0 °C; 1,013·10⁵ Pa), thể tích của 1,0 mol khí lí tưởng bằng bao nhiêu lít "
   "(làm tròn đến chữ số thập phân thứ nhất)? Cho R = 8,31 J/(mol·K).",
   "22,4",
   "V = nRT/p = 1,0 · 8,31 · 273/1,013·10⁵ ≈ 2,24·10⁻² m³ = 22,4 L.",
   "Phương trình Clapeyron", TB),

sa("Nếu tăng nhiệt độ tuyệt đối của một lượng khí lí tưởng lên 9 lần thì tốc độ căn quân phương của phân "
   "tử khí tăng bao nhiêu lần?",
   "3", "v ∝ √T (từ (1/2)m·v̄² = (3/2)kT) ⟹ v tăng √9 = 3 lần.",
   "Động năng phân tử – tốc độ", K),
])


# =====================================================================
DE5 = dict(
ma="12C2-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Cột khí bị giam bởi thuỷ ngân; khối lượng riêng của khí; tốc độ phân tử",
P1=[
mc("Một ống thuỷ tinh nằm ngang, một đầu kín, chứa cột khí dài 20 cm bị giam bởi một cột thuỷ ngân dài "
   "10 cm. Áp suất khí quyển 75 cmHg. Áp suất của cột khí bị giam là",
   ["65 cmHg.", "75 cmHg.", "85 cmHg.", "150 cmHg."],
   "B",
   "Khi ống nằm ngang, cột thuỷ ngân không gây thêm áp suất theo phương trục ống (trọng lực của nó vuông "
   "góc với trục ống). Do đó p = p₀ = 75 cmHg.",
   "Cột khí bị giam", TB, fig="k_sd_ong_khi",
   cap="Ống nằm ngang và ống thẳng đứng chứa cột khí bị giam"),

mc("Vẫn với ống trên, dựng ống thẳng đứng, miệng hướng lên. Áp suất cột khí bị giam trở thành",
   ["65 cmHg.", "75 cmHg.", "85 cmHg.", "95 cmHg."],
   "C",
   "Khí bị giam ở đáy phải đỡ cả khí quyển lẫn cột thuỷ ngân phía trên:\n"
   "p = p₀ + h = 75 + 10 = 85 cmHg.",
   "Cột khí bị giam", TB, fig="k_sd_ong_khi", cap="Ống thẳng đứng, miệng hướng lên"),

mc("Vẫn với ống đó (nhiệt độ không đổi), khi dựng thẳng đứng miệng hướng lên thì chiều dài cột khí bị giam là",
   ["15,8 cm.", "17,6 cm.", "20,0 cm.", "23,1 cm."],
   "B",
   "Áp dụng định luật Boyle giữa hai trạng thái:\n"
   "p₁ℓ₁ = p₂ℓ₂ ⟹ 75 · 20 = 85 · ℓ₂ ⟹ ℓ₂ = 1500/85 ≈ 17,6 cm.\n"
   "(Tiết diện ống không đổi nên tỉ số thể tích cũng là tỉ số chiều dài.)",
   "Cột khí bị giam – định luật Boyle", K, fig="k_sd_ong_khi",
   cap="Ống thẳng đứng, miệng hướng lên"),

mc("Vẫn với ống đó, khi dựng thẳng đứng miệng hướng XUỐNG thì chiều dài cột khí bị giam là",
   ["17,6 cm.", "20,0 cm.", "23,1 cm.", "26,5 cm."],
   "C",
   "Miệng hướng xuống thì trọng lượng cột thuỷ ngân kéo nó ra xa khối khí, làm áp suất khí giảm:\n"
   "p₃ = p₀ − h = 75 − 10 = 65 cmHg ⟹ ℓ₃ = 1500/65 ≈ 23,1 cm.",
   "Cột khí bị giam – định luật Boyle", K, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

mc("Khối lượng riêng của một chất khí lí tưởng được tính theo công thức",
   ["ρ = pM/(RT).", "ρ = RT/(pM).", "ρ = pRT/M.", "ρ = M/(pRT)."],
   "A",
   "Từ pV = (m/M)RT suy ra m/V = pM/(RT), tức ρ = pM/(RT). Khối lượng riêng của khí tỉ lệ thuận với áp "
   "suất và tỉ lệ nghịch với nhiệt độ tuyệt đối.",
   "Khối lượng riêng của khí", TB),

mc("Khối lượng riêng của không khí ở 27 °C và 10⁵ Pa gần nhất với (M = 29 g/mol, R = 8,31 J/(mol·K))",
   ["0,86 kg/m³.", "1,16 kg/m³.", "1,29 kg/m³.", "2,32 kg/m³."],
   "B",
   "ρ = pM/(RT) = 10⁵ · 0,029/(8,31 · 300) = 2900/2493 ≈ 1,16 kg/m³.",
   "Khối lượng riêng của khí", TB),

mc("Tốc độ căn quân phương của phân tử khí lí tưởng được tính bằng",
   ["v = √(3RT/M).", "v = √(RT/3M).", "v = 3RT/M.", "v = √(2RT/M)."],
   "A",
   "Từ (1/2)m·v̄² = (3/2)kT, nhân cả tử và mẫu với N_A ta được v = √(3kT/m) = √(3RT/M), trong đó M là "
   "khối lượng mol tính bằng kg/mol.",
   "Tốc độ phân tử", TB),

mc("Tốc độ căn quân phương của phân tử khí nitơ (M = 28 g/mol) ở 300 K gần nhất với "
   "(R = 8,31 J/(mol·K))",
   ["298 m/s.", "421 m/s.", "517 m/s.", "735 m/s."],
   "C",
   "v = √(3RT/M) = √(3 · 8,31 · 300/0,028) = √(7479/0,028) = √267 107 ≈ 517 m/s.\n"
   "Chú ý đổi khối lượng mol ra kg/mol.",
   "Tốc độ phân tử", K),

mc("Hai bình A và B nối với nhau bằng ống có khoá. Bình A thể tích 2,0 L chứa khí ở 3,0·10⁵ Pa; bình B "
   "thể tích 3,0 L chứa cùng loại khí ở 1,0·10⁵ Pa. Nhiệt độ hai bình bằng nhau và không đổi. Mở khoá, "
   "áp suất chung sau đó là",
   ["1,5·10⁵ Pa.", "1,8·10⁵ Pa.", "2,0·10⁵ Pa.", "2,4·10⁵ Pa."],
   "B",
   "Ở cùng nhiệt độ, tổng “lượng khí” được bảo toàn nên tổng các tích pV không đổi:\n"
   "p(V_A + V_B) = p_A V_A + p_B V_B ⟹ p · 5,0 = 3,0·10⁵ · 2,0 + 1,0·10⁵ · 3,0 = 9,0·10⁵ (Pa·L)\n"
   "⟹ p = 1,8·10⁵ Pa.\n"
   "Bẫy: lấy trung bình cộng hai áp suất (2,0·10⁵ Pa) là sai vì hai bình có thể tích khác nhau.",
   "Hai bình thông nhau", K),

mc("Một lượng khí lí tưởng được nén đẳng nhiệt tới thể tích bằng 1/3 giá trị ban đầu. Khối lượng riêng "
   "của khí khi đó",
   ["giảm 3 lần.", "không đổi.", "tăng 3 lần.", "tăng 9 lần."],
   "C",
   "Khối lượng khí không đổi mà thể tích giảm 3 lần ⟹ ρ = m/V tăng 3 lần. (Cũng phù hợp với "
   "ρ = pM/(RT): T không đổi, p tăng 3 lần.)",
   "Khối lượng riêng của khí", TB),

mc("Đun nóng đẳng áp một lượng khí lí tưởng từ 27 °C lên 327 °C. Khối lượng riêng của khí",
   ["tăng 2 lần.", "giảm 2 lần.", "tăng 12 lần.", "giảm 12 lần."],
   "B",
   "T₁ = 300 K, T₂ = 600 K. Đẳng áp ⟹ ρ = pM/(RT) tỉ lệ nghịch với T ⟹ ρ giảm 2 lần.\n"
   "Đây chính là nguyên lí hoạt động của khinh khí cầu: đốt nóng làm khí trong cầu nhẹ đi.",
   "Khối lượng riêng của khí", K),

mc("Trong một bình kín, nếu tăng nhiệt độ tuyệt đối lên 2 lần và đồng thời bơm thêm khí để số phân tử "
   "tăng 3 lần thì áp suất khí",
   ["tăng 5 lần.", "tăng 6 lần.", "tăng 1,5 lần.", "giảm 1,5 lần."],
   "B",
   "p = (N/V)kT với V không đổi ⟹ p tỉ lệ thuận với tích N·T ⟹ p tăng 3 · 2 = 6 lần.",
   "Phương trình trạng thái – mô hình phân tử", K),

mc("Một lượng khí có thể tích 10 L ở áp suất 2,0·10⁵ Pa. Nén đẳng nhiệt tới áp suất 5,0·10⁵ Pa. Thể tích "
   "khí đã giảm đi",
   ["2 L.", "4 L.", "6 L.", "8 L."],
   "C",
   "V₂ = p₁V₁/p₂ = 2,0·10⁵ · 10/5,0·10⁵ = 4,0 L.\n"
   "Độ giảm thể tích: 10 − 4 = 6 L. (Bẫy: nhiều học sinh trả lời 4 L — đó là thể tích CÒN LẠI.)",
   "Định luật Boyle", TB),

mc("Trong hệ toạ độ (V, T), một lượng khí lí tưởng biến đổi theo đường thẳng đi qua gốc toạ độ. Quá trình "
   "đó là",
   ["đẳng nhiệt.", "đẳng tích.", "đẳng áp.", "không xác định được."],
   "C",
   "V = (nR/p)T là đường thẳng qua gốc toạ độ khi và chỉ khi p không đổi ⟹ quá trình đẳng áp.",
   "Đồ thị các đẳng quá trình", TB, fig="k_dt_dangap", cap="Đường đẳng áp trong hệ (V, T)"),

mc("Hai lượng khí lí tưởng khác nhau có cùng nhiệt độ. Đại lượng nào của phân tử hai khí đó chắc chắn "
   "bằng nhau?",
   ["Tốc độ căn quân phương.", "Động năng tịnh tiến trung bình.",
    "Khối lượng phân tử.", "Động lượng trung bình về độ lớn."],
   "B",
   "W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ nên bằng nhau. Tốc độ, khối lượng phân tử và độ lớn động lượng "
   "đều phụ thuộc loại khí.",
   "Động năng phân tử – so sánh", TB),

mc("Một bình kín chứa khí ở 27 °C. Muốn áp suất khí tăng 20% (thể tích và lượng khí không đổi) thì phải "
   "nâng nhiệt độ lên",
   ["32,4 °C.", "57,0 °C.", "87,0 °C.", "327,0 °C."],
   "C",
   "p/T = hằng số ⟹ T₂ = T₁ · 1,2 = 300 · 1,2 = 360 K ⟹ t₂ = 360 − 273 = 87 °C.\n"
   "Bẫy: tăng nhiệt độ Celsius lên 20% cho 32,4 °C — sai.",
   "Quá trình đẳng tích", TB),

mc("Đại lượng nào sau đây của một lượng khí lí tưởng xác định KHÔNG thay đổi trong quá trình đẳng nhiệt?",
   ["Áp suất.", "Khối lượng riêng.", "Nội năng.", "Mật độ phân tử."],
   "C",
   "Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên không đổi trong quá trình đẳng nhiệt. Áp suất, khối "
   "lượng riêng và mật độ phân tử đều thay đổi khi thể tích thay đổi.",
   "Nội năng khí lí tưởng", K),

mc("Ở cùng nhiệt độ và áp suất, 1 lít khí heli và 1 lít khí nitơ chứa",
   ["cùng số phân tử và cùng khối lượng.",
    "cùng số phân tử nhưng khối lượng khác nhau.",
    "số phân tử khác nhau nhưng cùng khối lượng.",
    "số phân tử và khối lượng đều khác nhau."],
   "B",
   "Từ p = (N/V)kT: cùng p, V, T thì cùng N (định luật Avogadro). Nhưng khối lượng mỗi phân tử khác nhau "
   "(4 và 28 g/mol) nên khối lượng hai lượng khí khác nhau 7 lần.",
   "Định luật Avogadro", K),
],
P2=[
ds("Một ống thuỷ tinh một đầu kín, chứa cột khí dài 20 cm bị giam bởi cột thuỷ ngân dài 10 cm. Áp suất "
   "khí quyển 75 cmHg, nhiệt độ không đổi trong mọi thao tác.",
   [("Khi ống nằm ngang, áp suất cột khí bị giam bằng 75 cmHg.", True,
     "Đúng. Trọng lực của cột thuỷ ngân vuông góc với trục ống nên không gây thêm áp suất theo phương đó."),
    ("Khi dựng ống thẳng đứng, miệng hướng lên, cột khí dài khoảng 17,6 cm.", True,
     "Đúng. p₂ = 75 + 10 = 85 cmHg ⟹ ℓ₂ = 75 · 20/85 ≈ 17,6 cm."),
    ("Khi dựng ống thẳng đứng, miệng hướng xuống, cột khí dài khoảng 23,1 cm.", True,
     "Đúng. p₃ = 75 − 10 = 65 cmHg ⟹ ℓ₃ = 1500/65 ≈ 23,1 cm."),
    ("Khi nghiêng ống 30° so với phương ngang (miệng ở trên), áp suất cột khí bằng 75 + 10·cos30° cmHg.", False,
     "Sai. Cột thuỷ ngân chỉ gây thêm áp suất bằng CHIỀU CAO THEO PHƯƠNG THẲNG ĐỨNG của nó, tức "
     "10·sin30° = 5 cmHg, nên p = 80 cmHg chứ không phải dùng cos30°.")],
   "Cột khí bị giam", K, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam bởi thuỷ ngân"),

ds("Hai bình A và B nối nhau bằng ống có khoá, cùng nhiệt độ và nhiệt độ không đổi. Bình A: V = 2,0 L, "
   "p = 3,0·10⁵ Pa; bình B: V = 3,0 L, p = 1,0·10⁵ Pa. Coi thể tích ống nối không đáng kể.",
   [("Sau khi mở khoá, tổng số phân tử khí trong hệ không đổi.", True,
     "Đúng. Hệ kín, khí chỉ phân bố lại giữa hai bình chứ không mất đi."),
    ("Áp suất chung sau khi mở khoá là 1,8·10⁵ Pa.", True,
     "Đúng. p·5,0 = 3,0·10⁵·2,0 + 1,0·10⁵·3,0 = 9,0·10⁵ ⟹ p = 1,8·10⁵ Pa."),
    ("Áp suất chung bằng trung bình cộng của hai áp suất ban đầu, tức 2,0·10⁵ Pa.", False,
     "Sai. Chỉ khi hai bình có thể tích BẰNG NHAU thì áp suất chung mới là trung bình cộng. Ở đây phải "
     "lấy trung bình có trọng số theo thể tích."),
    ("Sau khi mở khoá, khí đi từ bình A sang bình B.", True,
     "Đúng. Bình A có áp suất cao hơn nên khí chảy sang bình B cho tới khi hai bình cùng áp suất 1,8·10⁵ Pa.")],
   "Hai bình thông nhau", K),

ds("Xét khối lượng riêng và tốc độ phân tử của khí lí tưởng. Cho R = 8,31 J/(mol·K).",
   [("Khối lượng riêng của khí lí tưởng được tính bằng ρ = pM/(RT).", True,
     "Đúng, suy ra trực tiếp từ pV = (m/M)RT bằng cách chia hai vế cho V."),
    ("Khối lượng riêng của không khí (M = 29 g/mol) ở 27 °C và 10⁵ Pa vào khoảng 1,16 kg/m³.", True,
     "Đúng. ρ = 10⁵ · 0,029/(8,31 · 300) ≈ 1,16 kg/m³."),
    ("Đun nóng đẳng áp một lượng khí từ 27 °C lên 327 °C thì khối lượng riêng của nó giảm 2 lần.", True,
     "Đúng. Đẳng áp thì ρ tỉ lệ nghịch với T: 300 K → 600 K nên ρ giảm 2 lần. Đây là cơ sở của khinh "
     "khí cầu."),
    ("Ở cùng nhiệt độ, phân tử khí nitơ (M = 28 g/mol) chuyển động nhanh hơn phân tử khí heli "
     "(M = 4 g/mol).", False,
     "Sai. v = √(3RT/M) tỉ lệ nghịch với √M, nên phân tử NHẸ hơn chuyển động nhanh hơn: heli nhanh hơn "
     "nitơ khoảng √7 ≈ 2,6 lần.")],
   "Khối lượng riêng – tốc độ phân tử", K),

ds("Một bình kín thể tích không đổi chứa khí lí tưởng ở 27 °C.",
   [("Muốn áp suất tăng 20% thì phải nâng nhiệt độ lên 360 K.", True,
     "Đúng. p/T = hằng số ⟹ T₂ = 300 · 1,2 = 360 K (tức 87 °C)."),
    ("Nếu vừa nâng nhiệt độ tuyệt đối lên 2 lần vừa bơm thêm khí để số phân tử tăng 3 lần thì áp suất "
     "tăng 6 lần.", True,
     "Đúng. p = (N/V)kT với V không đổi nên p tỉ lệ thuận với tích N·T: 3 · 2 = 6 lần."),
    ("Muốn áp suất tăng 20% thì phải nâng nhiệt độ Celsius lên 20%, tức lên 32,4 °C.", False,
     "Sai. Mọi định luật chất khí đều dùng nhiệt độ TUYỆT ĐỐI. Nâng lên 32,4 °C (305,4 K) chỉ làm áp "
     "suất tăng khoảng 1,8%."),
    ("Nếu chỉ bơm thêm khí mà giữ nguyên nhiệt độ thì động năng tịnh tiến trung bình của mỗi phân tử "
     "không đổi.", True,
     "Đúng. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ; số phân tử tăng chỉ làm tăng áp suất.")],
   "Quá trình đẳng tích – mô hình phân tử", K),
],
P3=[
sa("Ống thuỷ tinh một đầu kín, nằm ngang, cột khí dài 20 cm bị giam bởi cột thuỷ ngân 10 cm; p₀ = 75 cmHg. "
   "Dựng ống thẳng đứng, miệng hướng lên. Chiều dài cột khí lúc đó bằng bao nhiêu cm (làm tròn đến chữ số "
   "thập phân thứ nhất)?",
   "17,6",
   "p₁ℓ₁ = p₂ℓ₂ với p₁ = 75 cmHg, p₂ = 75 + 10 = 85 cmHg\n⟹ ℓ₂ = 75 · 20/85 ≈ 17,6 cm.",
   "Cột khí bị giam", K, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

sa("Vẫn với ống ở câu trên, khi dựng thẳng đứng miệng hướng xuống thì cột khí dài bao nhiêu cm "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "23,1",
   "p₃ = 75 − 10 = 65 cmHg ⟹ ℓ₃ = 75 · 20/65 = 1500/65 ≈ 23,1 cm.",
   "Cột khí bị giam", K, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

sa("Hai bình nối nhau qua khoá, cùng nhiệt độ. Bình A: 2,0 L ở 3,0·10⁵ Pa; bình B: 3,0 L ở 1,0·10⁵ Pa. "
   "Mở khoá, áp suất chung bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "1,8",
   "p(V_A + V_B) = p_A V_A + p_B V_B ⟹ 5,0p = 6,0 + 3,0 = 9,0 (đơn vị 10⁵ Pa·L) ⟹ p = 1,8·10⁵ Pa.",
   "Hai bình thông nhau", K),

sa("Khối lượng riêng của không khí (M = 29 g/mol) ở 27 °C và 10⁵ Pa bằng bao nhiêu kg/m³ (làm tròn đến "
   "chữ số thập phân thứ hai)? Cho R = 8,31 J/(mol·K).",
   "1,16", "ρ = pM/(RT) = 10⁵ · 0,029/(8,31 · 300) = 2900/2493 ≈ 1,16 kg/m³.",
   "Khối lượng riêng của khí", TB),

sa("Tốc độ căn quân phương của phân tử khí nitơ (M = 28 g/mol) ở 300 K bằng bao nhiêu m/s (làm tròn đến "
   "hàng đơn vị)? Cho R = 8,31 J/(mol·K).",
   "517", "v = √(3RT/M) = √(3 · 8,31 · 300/0,028) = √267 107 ≈ 517 m/s.",
   "Tốc độ phân tử", K),

sa("Một bình kín chứa khí ở 27 °C. Muốn áp suất khí tăng 20% thì phải nâng nhiệt độ lên bao nhiêu độ C?",
   "87", "T₂ = 300 · 1,2 = 360 K ⟹ t₂ = 360 − 273 = 87 °C.", "Quá trình đẳng tích", TB),
])


# =====================================================================
DE6 = dict(
ma="12C2-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Lượng khí thay đổi; bơm hút; chuyển đổi giữa các hệ toạ độ p–V, p–T, V–T",
P1=[
mc("Một bình kín thể tích 10 L chứa khí ở 27 °C, áp suất 5,0·10⁵ Pa. Mở van cho khí thoát ra tới khi áp "
   "suất còn 2,0·10⁵ Pa, nhiệt độ vẫn giữ 27 °C. Phần trăm khối lượng khí đã thoát ra là",
   ["40%.", "50%.", "60%.", "75%."],
   "C",
   "Không dùng được pV/T = hằng số vì lượng khí thay đổi. Phải dùng pV = (m/M)RT với V, T, M không đổi "
   "⟹ m tỉ lệ thuận với p.\n"
   "m₂/m₁ = p₂/p₁ = 2,0/5,0 = 0,40 ⟹ đã thoát ra 60% khối lượng khí.",
   "Lượng khí thay đổi", K),

mc("Vẫn với bình trên, nếu sau khi xả khí nhiệt độ giảm còn 7 °C (áp suất 2,0·10⁵ Pa) thì phần trăm khối "
   "lượng khí đã thoát ra gần nhất với",
   ["42,9%.", "50,0%.", "57,1%.", "64,3%."],
   "C",
   "m ∝ p/T (vì V và M không đổi):\n"
   "m₂/m₁ = (p₂/p₁)·(T₁/T₂) = (2,0/5,0) · (300/280) ≈ 0,4286\n"
   "⟹ đã thoát ra 1 − 0,4286 = 0,5714, tức khoảng 57,1%.",
   "Lượng khí thay đổi", K),

mc("Dùng bơm hút để hút khí ra khỏi một bình thể tích V. Mỗi lần bơm, khí trong bình giãn chiếm thêm thể "
   "tích xilanh V₀ rồi phần khí trong xilanh bị đẩy ra ngoài. Sau n lần bơm, áp suất khí trong bình là",
   ["p₀·(V/(V + V₀))ⁿ.", "p₀·(V₀/V)ⁿ.", "p₀ − n·V₀/V.", "p₀·(1 − nV₀/V)."],
   "A",
   "Mỗi lần bơm là một quá trình giãn đẳng nhiệt từ V sang V + V₀:\n"
   "p·V = p′·(V + V₀) ⟹ p′ = p·V/(V + V₀).\n"
   "Áp suất được nhân với cùng một hệ số sau mỗi lần bơm nên p_n = p₀·(V/(V + V₀))ⁿ — một cấp số nhân, "
   "không phải hiệu số không đổi.",
   "Bơm hút – quá trình lặp", K),

mc("Bình thể tích 4,0 L ở áp suất 10⁵ Pa được hút bằng bơm có thể tích xilanh 1,0 L. Sau 2 lần bơm, áp "
   "suất khí trong bình là",
   ["0,50·10⁵ Pa.", "0,64·10⁵ Pa.", "0,80·10⁵ Pa.", "0,90·10⁵ Pa."],
   "B",
   "Hệ số mỗi lần bơm: V/(V + V₀) = 4,0/5,0 = 0,80.\n"
   "p₂ = 10⁵ · 0,80² = 0,64·10⁵ Pa.",
   "Bơm hút – quá trình lặp", K),

mc("Trên giản đồ (p, V), một lượng khí lí tưởng đi từ A(1 L; 4·10⁵ Pa) tới B(4 L; 1·10⁵ Pa) rồi tới "
   "C(4 L; 3·10⁵ Pa) như hình vẽ. Quá trình A → B là",
   ["đẳng tích.", "đẳng áp.", "đẳng nhiệt.", "không phải đẳng quá trình nào."],
   "C",
   "(pV)_A = 4 · 1 = 4 và (pV)_B = 1 · 4 = 4 (đơn vị 10⁵ Pa·L). Hai trạng thái có cùng tích pV nên cùng "
   "nhiệt độ; đường nối chúng trên hình là một nhánh hypebol ⟹ quá trình đẳng nhiệt.",
   "Đọc giản đồ p–V", TB, fig="k_dt_pV_docso",
   cap="Quá trình A → B → C của một lượng khí lí tưởng"),

mc("Vẫn với hình trên, tỉ số nhiệt độ T_C/T_B bằng",
   ["1/3.", "1.", "3.", "4."],
   "C",
   "B và C có cùng thể tích 4 L; áp suất tăng từ 1·10⁵ Pa lên 3·10⁵ Pa nên nhiệt độ tăng 3 lần: "
   "T_C/T_B = 3.",
   "Đọc giản đồ p–V", TB, fig="k_dt_pV_docso", cap="Quá trình A → B → C"),

mc("Quá trình đẳng áp của một lượng khí lí tưởng được biểu diễn trên giản đồ (p, T) bằng",
   ["đường thẳng qua gốc toạ độ.", "đoạn thẳng song song với trục T.",
    "đoạn thẳng song song với trục p.", "nhánh hypebol."],
   "B", "Đẳng áp ⟹ p không đổi, điểm biểu diễn di chuyển theo phương ngang trên hệ (p, T).",
   "Chuyển đổi hệ toạ độ", TB),

mc("Một quá trình đẳng tích của khí lí tưởng khi biểu diễn trên hệ (V, T) sẽ là",
   ["đường thẳng qua gốc toạ độ.", "đoạn thẳng song song với trục T.",
    "đoạn thẳng song song với trục V.", "nhánh hypebol."],
   "B", "Đẳng tích ⟹ V không đổi; trên hệ (V, T) điểm biểu diễn di chuyển theo phương ngang.",
   "Chuyển đổi hệ toạ độ", TB),

mc("Nén đẳng nhiệt một lượng khí sao cho áp suất tăng thêm 50%. Thể tích khí lúc sau bằng bao nhiêu phần "
   "thể tích ban đầu?",
   ["1/2.", "2/3.", "3/4.", "3/2."],
   "B",
   "p₂ = 1,5p₁ ⟹ V₂ = p₁V₁/p₂ = V₁/1,5 = (2/3)V₁.",
   "Định luật Boyle", TB),

mc("Một bình chứa hỗn hợp gồm 0,20 mol khí heli và 0,30 mol khí nitơ ở 300 K, thể tích 4,155 L. Áp suất "
   "của hỗn hợp là (R = 8,31 J/(mol·K))",
   ["1,0·10⁵ Pa.", "2,0·10⁵ Pa.", "3,0·10⁵ Pa.", "5,0·10⁵ Pa."],
   "C",
   "Áp suất chỉ phụ thuộc TỔNG số mol: n = 0,20 + 0,30 = 0,50 mol.\n"
   "p = nRT/V = 0,50 · 8,31 · 300/(4,155·10⁻³) = 1246,5/4,155·10⁻³ = 3,0·10⁵ Pa.",
   "Phương trình Clapeyron – hỗn hợp khí", K),

mc("Trong quá trình nào sau đây, cả áp suất và thể tích của một lượng khí lí tưởng xác định đều tăng?",
   ["Đẳng nhiệt.", "Đẳng tích.", "Đẳng áp.", "Vừa đun nóng vừa cho khí giãn nở chậm ở áp suất tăng dần."],
   "D",
   "Ba đẳng quá trình đều có một đại lượng giữ nguyên. Muốn cả p và V cùng tăng thì tích pV tăng mạnh, "
   "tức nhiệt độ phải tăng — chỉ có quá trình tổng quát (không phải đẳng quá trình) mới làm được.",
   "Phương trình trạng thái", TB),

mc("Một lượng khí lí tưởng có nhiệt độ tăng 2 lần và thể tích tăng 3 lần. Áp suất khí",
   ["tăng 6 lần.", "tăng 1,5 lần.", "giảm 1,5 lần.", "giảm 6 lần."],
   "C",
   "pV/T = hằng số ⟹ p₂/p₁ = (T₂/T₁)·(V₁/V₂) = 2 · (1/3) = 2/3 ⟹ áp suất giảm 1,5 lần.",
   "Phương trình trạng thái", TB),

mc("Khi hút bớt khí ra khỏi một bình kín (giữ nguyên nhiệt độ), đại lượng nào của khí còn lại trong bình "
   "KHÔNG đổi?",
   ["Áp suất.", "Khối lượng riêng.", "Mật độ phân tử.",
    "Động năng tịnh tiến trung bình của mỗi phân tử."],
   "D",
   "Nhiệt độ không đổi nên W̄đ = (3/2)kT không đổi. Số phân tử giảm nên áp suất, mật độ phân tử và khối "
   "lượng riêng đều giảm.",
   "Mô hình động học phân tử", TB),

mc("Bình A thể tích V chứa khí ở áp suất p; bình B thể tích 2V là chân không. Nối hai bình bằng ống nhỏ "
   "(nhiệt độ không đổi). Áp suất chung sau đó là",
   ["p/3.", "p/2.", "2p/3.", "p."],
   "A",
   "Lượng khí không đổi, nhiệt độ không đổi ⟹ pV = p′·(V + 2V) = 3p′V ⟹ p′ = p/3.",
   "Hai bình thông nhau", TB),

mc("Trong hệ toạ độ (p, T), hai đường đẳng tích của cùng một lượng khí ứng với thể tích V₁ và V₂. Đường "
   "ứng với V₁ dốc hơn. Kết luận đúng là",
   ["V₁ > V₂.", "V₁ < V₂.", "V₁ = V₂.", "chưa đủ dữ kiện."],
   "B",
   "p = (nR/V)·T nên hệ số góc nR/V tỉ lệ NGHỊCH với thể tích: đường càng dốc thì thể tích càng nhỏ.",
   "Đọc đồ thị đẳng tích", TB, fig="k_dt_dangtich", cap="Hai đường đẳng tích"),

mc("Một quả bóng bơm căng để ngoài nắng có thể nổ. Nguyên nhân chính là",
   ["khối lượng khí trong bóng tăng lên.",
    "nhiệt độ khí trong bóng tăng làm áp suất tăng trong khi thể tích bị vỏ bóng hạn chế.",
    "vỏ bóng co lại vì nóng.",
    "áp suất khí quyển giảm khi trời nắng."],
   "B",
   "Vỏ bóng đã căng nên thể tích gần như không tăng thêm được; quá trình gần như đẳng tích, nhiệt độ tăng "
   "kéo theo áp suất tăng cho tới khi vượt quá sức bền của vỏ.",
   "Quá trình đẳng tích – thực tiễn", TB),

mc("Cho 1,0 mol khí lí tưởng ở 300 K. Nếu tăng nhiệt độ lên 600 K và giữ nguyên thể tích thì tổng động "
   "năng tịnh tiến của tất cả các phân tử",
   ["không đổi.", "tăng 2 lần.", "tăng 4 lần.", "giảm 2 lần."],
   "B",
   "Tổng động năng W = N·(3/2)kT = (3/2)nRT tỉ lệ thuận với nhiệt độ tuyệt đối; T tăng 2 lần thì W tăng "
   "2 lần.",
   "Động năng phân tử", TB),

mc("Đại lượng nào sau đây KHÔNG xuất hiện trong phương trình Clapeyron pV = nRT?",
   ["Số mol khí.", "Nhiệt độ tuyệt đối.", "Khối lượng mol.", "Thể tích khí."],
   "C",
   "Phương trình pV = nRT chỉ chứa n, R, T, p, V. Khối lượng mol M chỉ xuất hiện khi thay n = m/M, tức "
   "khi viết pV = (m/M)RT.",
   "Phương trình Clapeyron", D),
],
P2=[
ds("Một bình kín thể tích 10 L chứa khí ở 27 °C, áp suất 5,0·10⁵ Pa. Mở van xả bớt khí.",
   [("Không thể dùng hệ thức pV/T = hằng số cho quá trình xả khí này.", True,
     "Đúng. Hệ thức đó chỉ áp dụng cho MỘT LƯỢNG KHÍ XÁC ĐỊNH; ở đây lượng khí trong bình giảm đi."),
    ("Nếu xả tới áp suất 2,0·10⁵ Pa mà vẫn giữ 27 °C thì 60% khối lượng khí đã thoát ra.", True,
     "Đúng. Với V, T, M không đổi thì m ∝ p: m₂/m₁ = 2,0/5,0 = 0,40 ⟹ thoát 60%."),
    ("Nếu sau khi xả, nhiệt độ giảm còn 7 °C và áp suất là 2,0·10⁵ Pa thì lượng khí thoát ra ít hơn 60%.", True,
     "Đúng. m ∝ p/T ⟹ m₂/m₁ = (2,0/5,0)(300/280) ≈ 0,4286, tức chỉ thoát khoảng 57,1%. Nhiệt độ thấp "
     "hơn nghĩa là cùng áp suất đó chứa được nhiều khí hơn."),
    ("Trong quá trình xả khí, động năng tịnh tiến trung bình của mỗi phân tử còn lại trong bình giảm đi "
     "vì áp suất giảm.", False,
     "Sai. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ, không phụ thuộc áp suất. Nếu nhiệt độ được giữ 27 °C thì "
     "W̄đ không đổi.")],
   "Lượng khí thay đổi", K),

ds("Dùng bơm hút có thể tích xilanh V₀ = 1,0 L để hút khí ra khỏi bình thể tích V = 4,0 L đang ở áp suất "
   "10⁵ Pa. Nhiệt độ coi như không đổi.",
   [("Sau mỗi lần bơm, áp suất khí trong bình được nhân với hệ số 0,80.", True,
     "Đúng. Mỗi lần bơm khí giãn đẳng nhiệt từ 4,0 L sang 5,0 L: p′ = p·4,0/5,0 = 0,80p."),
    ("Sau 2 lần bơm, áp suất khí trong bình là 0,64·10⁵ Pa.", True,
     "Đúng. p₂ = 10⁵ · 0,80² = 0,64·10⁵ Pa."),
    ("Sau mỗi lần bơm, áp suất giảm đi một lượng không đổi bằng 0,2·10⁵ Pa.", False,
     "Sai. Áp suất giảm theo CẤP SỐ NHÂN (nhân 0,80 mỗi lần) chứ không phải giảm một lượng cố định: "
     "lần 1 giảm 0,20·10⁵ Pa, lần 2 chỉ giảm thêm 0,16·10⁵ Pa."),
    ("Về nguyên tắc, không thể hút để áp suất trong bình bằng đúng 0 bằng cách bơm hữu hạn lần.", True,
     "Đúng. p_n = p₀·0,80ⁿ luôn dương với mọi n hữu hạn; áp suất chỉ tiến dần tới 0 chứ không bao giờ "
     "bằng 0.")],
   "Bơm hút – quá trình lặp", K, fig="k_sd_bomxe", cap="Nguyên tắc của bơm"),

ds("Trên giản đồ (p, V), một lượng khí lí tưởng đi từ A(1 L; 4·10⁵ Pa) tới B(4 L; 1·10⁵ Pa) theo đường "
   "đẳng nhiệt, rồi từ B tới C(4 L; 3·10⁵ Pa).",
   [("Nhiệt độ ở A bằng nhiệt độ ở B.", True,
     "Đúng. (pV)_A = 4 · 1 = 4 = 1 · 4 = (pV)_B (đơn vị 10⁵ Pa·L) nên T_A = T_B."),
    ("Quá trình B → C là quá trình đẳng tích và nhiệt độ tăng 3 lần.", True,
     "Đúng. Thể tích giữ nguyên 4 L; áp suất tăng từ 1·10⁵ lên 3·10⁵ Pa nên T tăng 3 lần."),
    ("Nhiệt độ ở C gấp 3 lần nhiệt độ ở A.", True,
     "Đúng. T_C/T_A = (pV)_C/(pV)_A = (3·4)/(4·1) = 3."),
    ("Trên giản đồ (V, T), quá trình A → B là một đoạn thẳng đi qua gốc toạ độ.", False,
     "Sai. A → B là đẳng nhiệt: nhiệt độ không đổi, nên trên hệ (V, T) nó là đoạn thẳng SONG SONG với "
     "trục V (thẳng đứng nếu V là trục tung), chứ không đi qua gốc toạ độ.")],
   "Đọc giản đồ và chuyển hệ toạ độ", K, fig="k_dt_pV_docso",
   cap="Quá trình A → B → C trên giản đồ p–V"),

ds("Xét cách biểu diễn các đẳng quá trình của khí lí tưởng trên ba hệ toạ độ (p, V), (p, T) và (V, T).",
   [("Quá trình đẳng nhiệt là nhánh hypebol trên hệ (p, V) nhưng là đoạn thẳng đứng (T không đổi) trên hệ "
     "(V, T).", True,
     "Đúng. Cùng một quá trình có hình dạng khác nhau trên các hệ toạ độ khác nhau; điều bất biến là "
     "T không đổi."),
    ("Quá trình đẳng tích là đường thẳng qua gốc toạ độ trên hệ (p, T).", True,
     "Đúng. p = (nR/V)T là hàm bậc nhất thuần nhất của T."),
    ("Quá trình đẳng áp trên hệ (p, T) là một đoạn thẳng song song với trục T.", True,
     "Đúng. Áp suất không đổi nên tung độ p giữ nguyên khi T thay đổi."),
    ("Trên hệ (p, T), một đường thẳng bất kì đều biểu diễn một quá trình đẳng tích.", False,
     "Sai. Chỉ đường thẳng ĐI QUA GỐC TOẠ ĐỘ mới là đẳng tích. Một đường thẳng cắt trục p tại giá trị "
     "khác 0 sẽ cho p ≠ 0 khi T = 0 K — điều không thể xảy ra với một lượng khí lí tưởng xác định giữ "
     "nguyên thể tích.")],
   "Chuyển đổi hệ toạ độ", K, fig="k_dt_dangtich",
   cap="Đường đẳng tích trong hệ (p, T)"),
],
P3=[
sa("Bình kín 10 L chứa khí ở 27 °C, áp suất 5,0·10⁵ Pa. Xả bớt khí tới áp suất 2,0·10⁵ Pa, nhiệt độ vẫn "
   "27 °C. Phần trăm khối lượng khí đã thoát ra bằng bao nhiêu?",
   "60", "V, T, M không đổi ⟹ m ∝ p. m₂/m₁ = 2,0/5,0 = 0,40 ⟹ thoát ra 60%.",
   "Lượng khí thay đổi", K),

sa("Bình 4,0 L ở áp suất 10⁵ Pa được hút bằng bơm có thể tích xilanh 1,0 L. Sau 3 lần bơm, áp suất khí "
   "trong bình bằng bao nhiêu (đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ ba)?",
   "0,512", "p₃ = 10⁵ · (4,0/5,0)³ = 10⁵ · 0,512 = 0,512·10⁵ Pa.",
   "Bơm hút – quá trình lặp", K),

sa("Một bình chứa hỗn hợp 0,20 mol heli và 0,30 mol nitơ ở 300 K, thể tích 4,155 L. Áp suất hỗn hợp bằng "
   "bao nhiêu (đơn vị 10⁵ Pa)? Cho R = 8,31 J/(mol·K).",
   "3",
   "n = 0,20 + 0,30 = 0,50 mol ⟹ p = nRT/V = 0,50 · 8,31 · 300/(4,155·10⁻³) = 3,0·10⁵ Pa.",
   "Hỗn hợp khí", K),

sa("Bình A thể tích 2,0 L chứa khí ở 6,0·10⁵ Pa được nối với bình B thể tích 4,0 L là chân không "
   "(nhiệt độ không đổi). Áp suất chung sau đó bằng bao nhiêu (đơn vị 10⁵ Pa)?",
   "2", "pV = p′(V_A + V_B) ⟹ 6,0 · 2,0 = p′ · 6,0 ⟹ p′ = 2,0·10⁵ Pa.",
   "Hai bình thông nhau", TB),

sa("Một lượng khí lí tưởng có nhiệt độ tuyệt đối tăng 2 lần và thể tích tăng 3 lần. Áp suất khí giảm bao "
   "nhiêu lần (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,5", "p₂/p₁ = (T₂/T₁)(V₁/V₂) = 2/3 ⟹ áp suất giảm 3/2 = 1,5 lần.",
   "Phương trình trạng thái", TB),

sa("Bình kín 10 L chứa khí ở 27 °C, áp suất 5,0·10⁵ Pa. Sau khi xả, áp suất còn 2,0·10⁵ Pa và nhiệt độ "
   "còn 7 °C. Phần trăm khối lượng khí đã thoát ra bằng bao nhiêu (làm tròn đến chữ số thập phân thứ nhất)?",
   "57,1",
   "m ∝ p/T ⟹ m₂/m₁ = (2,0/5,0)(300/280) ≈ 0,4286 ⟹ thoát ra (1 − 0,4286)·100% ≈ 57,1%.",
   "Lượng khí thay đổi", K),
])


# =====================================================================
DE7 = dict(
ma="12C2-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Xilanh hai ngăn; pit-tông có vấu chặn; khinh khí cầu; suy luận trên đồ thị",
P1=[
mc("Một xilanh nằm ngang dài 60 cm được chia thành hai ngăn bằng pit-tông mỏng, dịch chuyển không ma sát. "
   "Ban đầu hai ngăn dài bằng nhau, cùng chứa khí ở 300 K và 10⁵ Pa. Giữ ngăn phải ở 300 K, nung ngăn "
   "trái lên 360 K. Ở trạng thái cân bằng mới, áp suất hai ngăn",
   ["vẫn đều bằng 10⁵ Pa.", "bằng nhau nhưng lớn hơn 10⁵ Pa.",
    "ngăn trái lớn hơn ngăn phải.", "ngăn phải lớn hơn ngăn trái."],
   "B",
   "Pit-tông cân bằng ⟹ áp suất hai bên luôn BẰNG NHAU. Nhưng ngăn phải bị nén lại nên áp suất chung "
   "phải tăng so với 10⁵ Pa. “Pit-tông tự do” không có nghĩa là quá trình đẳng áp.",
   "Xilanh hai ngăn", K, fig="k_sd_xilanh_quanang", cap="Xilanh có pit-tông dịch chuyển được"),

mc("Với xilanh ở câu trên, pit-tông dịch chuyển một đoạn gần nhất với",
   ["1,8 cm.", "2,7 cm.", "3,3 cm.", "5,0 cm."],
   "B",
   "Hai ngăn ban đầu giống hệt nhau nên có cùng số mol; ở trạng thái cuối chúng có cùng áp suất nên\n"
   "V_trái/V_phải = T_trái/T_phải = 360/300 = 1,2.\n"
   "Đặt độ dịch chuyển x: (30 + x)/(30 − x) = 1,2 ⟹ 30 + x = 36 − 1,2x ⟹ 2,2x = 6 ⟹ x ≈ 2,7 cm.",
   "Xilanh hai ngăn", K),

mc("Vẫn với xilanh đó, áp suất chung ở trạng thái cân bằng mới gần nhất với",
   ["1,00·10⁵ Pa.", "1,10·10⁵ Pa.", "1,20·10⁵ Pa.", "1,44·10⁵ Pa."],
   "B",
   "Xét ngăn phải (đẳng nhiệt): p₀·30 = p′·(30 − 2,727) ⟹ p′ = 10⁵ · 30/27,27 ≈ 1,10·10⁵ Pa.",
   "Xilanh hai ngăn", K),

mc("Một xilanh thẳng đứng chứa cột khí cao 30 cm ở 27 °C, áp suất 10⁵ Pa, phía trên là pit-tông nhẹ dịch "
   "chuyển không ma sát; cách pit-tông 6 cm có các vấu chặn. Đun nóng khí thật chậm. Nhiệt độ khi pit-tông "
   "vừa chạm vấu chặn là",
   ["330 K.", "360 K.", "390 K.", "450 K."],
   "B",
   "Trước khi chạm vấu, pit-tông còn tự do nên quá trình là ĐẲNG ÁP:\n"
   "T₂ = T₁·ℓ₂/ℓ₁ = 300 · 36/30 = 360 K.",
   "Xilanh có vấu chặn – hai chặng", K),

mc("Vẫn với xilanh ở câu trên, tiếp tục đun tới khi áp suất khí đạt 1,5·10⁵ Pa. Nhiệt độ khi đó là",
   ["450 K.", "480 K.", "540 K.", "600 K."],
   "C",
   "Sau khi chạm vấu, thể tích không tăng được nữa ⟹ quá trình ĐẲNG TÍCH từ 360 K:\n"
   "T₃ = T₂·p₃/p₂ = 360 · 1,5/1,0 = 540 K.\n"
   "Bẫy: áp thẳng định luật đẳng tích từ trạng thái đầu cho 300 · 1,5 = 450 K — sai vì chặng đầu thể tích "
   "đã thay đổi.",
   "Xilanh có vấu chặn – hai chặng", RK),

mc("Một khinh khí cầu có thể tích 500 m³, đáy hở nên áp suất khí bên trong luôn bằng áp suất khí quyển "
   "10⁵ Pa. Không khí ngoài ở 27 °C. Đốt nóng khí trong cầu lên 87 °C. Cho M = 29 g/mol, "
   "R = 8,31 J/(mol·K), g = 10 m/s². Lực nâng (hiệu giữa lực đẩy Archimedes và trọng lượng khí trong cầu) "
   "gần nhất với",
   ["484 N.", "620 N.", "968 N.", "1163 N."],
   "C",
   "ρ = pM/(RT): ρ_ngoài = 2900/(8,31 · 300) ≈ 1,163 kg/m³; ρ_trong = 2900/(8,31 · 360) ≈ 0,969 kg/m³.\n"
   "Lực nâng = (ρ_ngoài − ρ_trong)·V·g = (1,163 − 0,969) · 500 · 10 ≈ 968 N.",
   "Khối lượng riêng của khí – khinh khí cầu", RK),

mc("Khi đốt nóng không khí trong khinh khí cầu có đáy hở (thể tích và áp suất không đổi) thì",
   ["khối lượng khí trong cầu không đổi.",
    "một phần khí thoát ra ngoài nên khối lượng khí trong cầu giảm.",
    "khối lượng khí trong cầu tăng lên.",
    "áp suất khí trong cầu tăng lên."],
   "B",
   "Từ m = pVM/(RT) với p, V, M không đổi: T tăng thì m GIẢM. Phần khí “thừa” thoát ra qua miệng hở — "
   "chính vì vậy khí trong cầu nhẹ đi và cầu bay lên.",
   "Khối lượng riêng của khí – thực tiễn", K),

mc("Trên giản đồ (p, V), một lượng khí lí tưởng xác định biến đổi theo đoạn thẳng từ A(1 L; 4·10⁵ Pa) tới "
   "B(4 L; 1·10⁵ Pa). Nhận xét nào về nhiệt độ khí là ĐÚNG?",
   ["Nhiệt độ giảm đều từ A tới B.", "Nhiệt độ tăng đều từ A tới B.",
    "Nhiệt độ không đổi vì p_A·V_A = p_B·V_B.",
    "Nhiệt độ tăng rồi giảm, đạt cực đại tại V = 2,5 L."],
   "D",
   "Phương trình đoạn thẳng AB (p tính theo 10⁵ Pa, V theo L): p = 5 − V.\n"
   "pV = V(5 − V) là tam thức bậc hai có hệ số của V² âm, đạt cực đại tại V = 2,5 L.\n"
   "Ở hai đầu mút pV đều bằng 4, nên T_A = T_B — nhưng quá trình KHÔNG đẳng nhiệt vì đường đẳng nhiệt là "
   "hypebol chứ không phải đoạn thẳng.",
   "Suy luận trên giản đồ p–V", RK),

mc("Nén đẳng nhiệt một lượng khí lí tưởng làm thể tích giảm 40%. Áp suất khí",
   ["tăng 40%.", "tăng 60%.", "tăng khoảng 66,7%.", "giảm 40%."],
   "C",
   "V₂ = 0,60V₁ ⟹ p₂ = p₁V₁/V₂ = p₁/0,60 ≈ 1,667p₁, tức tăng khoảng 66,7%.",
   "Định luật Boyle", TB),

mc("Hai bình giống nhau chứa cùng loại khí ở cùng nhiệt độ, áp suất lần lượt là p và 3p. Nối hai bình "
   "bằng ống nhỏ (nhiệt độ không đổi). Áp suất chung là",
   ["1,5p.", "2p.", "2,5p.", "3p."],
   "B",
   "Hai bình cùng thể tích V: p′·2V = pV + 3pV = 4pV ⟹ p′ = 2p (trung bình cộng, vì thể tích bằng nhau).",
   "Hai bình thông nhau", TB),

mc("Trong quá trình đẳng áp, nếu thể tích khí tăng 25% thì nhiệt độ Celsius của khí ban đầu là 27 °C sẽ "
   "trở thành",
   ["33,75 °C.", "102 °C.", "375 °C.", "112 °C."],
   "B",
   "T₂ = 1,25·T₁ = 1,25 · 300 = 375 K ⟹ t₂ = 375 − 273 = 102 °C.\n"
   "Bẫy: tăng nhiệt độ Celsius 25% cho 33,75 °C — sai.",
   "Định luật Charles", TB),

mc("Một bình kín chứa khí lí tưởng. Nếu đồng thời giảm thể tích còn một nửa và giảm nhiệt độ tuyệt đối "
   "còn một nửa thì áp suất khí",
   ["không đổi.", "tăng 2 lần.", "giảm 2 lần.", "giảm 4 lần."],
   "A",
   "p₂/p₁ = (T₂/T₁)·(V₁/V₂) = (1/2) · 2 = 1 ⟹ áp suất không đổi.",
   "Phương trình trạng thái", TB),

mc("Một lượng khí lí tưởng ở 27 °C. Muốn tốc độ căn quân phương của phân tử tăng 50% thì nhiệt độ phải "
   "nâng lên",
   ["450 K.", "540 K.", "675 K.", "900 K."],
   "C",
   "v ∝ √T ⟹ v₂/v₁ = 1,5 ⟹ T₂/T₁ = 1,5² = 2,25 ⟹ T₂ = 300 · 2,25 = 675 K.",
   "Tốc độ phân tử", K),

mc("Trong bình kín thể tích không đổi, nếu áp suất tăng 3 lần trong khi số phân tử không đổi thì tổng "
   "động năng tịnh tiến của các phân tử",
   ["không đổi.", "tăng 1,73 lần.", "tăng 3 lần.", "tăng 9 lần."],
   "C",
   "Từ pV = (2/3)W_tổng suy ra W_tổng = (3/2)pV. Thể tích không đổi nên W_tổng tỉ lệ thuận với p ⟹ "
   "tăng 3 lần (cũng chính là vì nhiệt độ tăng 3 lần).",
   "Áp suất – động năng phân tử", K),

mc("Người ta nén khí trong xilanh của động cơ diesel rất nhanh. Quá trình đó KHÔNG phải là đẳng nhiệt vì",
   ["áp suất thay đổi quá nhanh.",
    "khí không kịp trao đổi nhiệt với môi trường nên nhiệt độ khí tăng mạnh.",
    "thể tích khí giảm.",
    "khối lượng khí trong xilanh thay đổi."],
   "B",
   "Nén nhanh ⟹ quá trình gần đoạn nhiệt (Q ≈ 0). Khí nhận công nên nội năng và nhiệt độ tăng mạnh — đủ "
   "để đốt cháy nhiên liệu mà không cần bugi.",
   "Điều kiện áp dụng định luật Boyle", K),

mc("Một quả bóng thể tích không đổi 3,0 L chứa khí ở 27 °C, áp suất 2,0·10⁵ Pa. Cần lấy ra bao nhiêu phần "
   "trăm lượng khí để áp suất còn 1,2·10⁵ Pa ở cùng nhiệt độ?",
   ["20%.", "30%.", "40%.", "60%."],
   "C",
   "Với V, T không đổi thì m ∝ p: m₂/m₁ = 1,2/2,0 = 0,60 ⟹ đã lấy ra 40% lượng khí.",
   "Lượng khí thay đổi", TB),

mc("Trong hệ toạ độ (p, V), đường đẳng nhiệt ứng với nhiệt độ càng cao thì",
   ["càng gần gốc toạ độ.", "càng xa gốc toạ độ.",
    "trùng với trục hoành.", "có dạng đường thẳng."],
   "B",
   "pV = nRT: nhiệt độ càng cao thì tích pV càng lớn, nhánh hypebol càng nằm xa gốc toạ độ.",
   "Đọc đồ thị đẳng nhiệt", TB, fig="k_dt_dangnhiet", cap="Hai đường đẳng nhiệt"),

mc("Một lượng khí lí tưởng thực hiện quá trình sao cho tích p·V tăng gấp đôi. Kết luận nào ĐÚNG?",
   ["Áp suất khí tăng gấp đôi.", "Thể tích khí tăng gấp đôi.",
    "Nhiệt độ tuyệt đối của khí tăng gấp đôi.", "Khối lượng khí tăng gấp đôi."],
   "C",
   "Với lượng khí xác định, pV = nRT nên pV tỉ lệ thuận với T. Tích pV tăng gấp đôi nghĩa là nhiệt độ "
   "TUYỆT ĐỐI tăng gấp đôi; riêng p và V có thể thay đổi theo nhiều cách khác nhau.",
   "Phương trình trạng thái", TB),
],
P2=[
ds("Một xilanh nằm ngang dài 60 cm, pit-tông mỏng ở chính giữa dịch chuyển không ma sát, hai ngăn cùng "
   "chứa khí lí tưởng ở 300 K và 10⁵ Pa. Giữ ngăn phải ở 300 K và nung ngăn trái lên 360 K.",
   [("Ở trạng thái cân bằng mới, áp suất khí hai ngăn vẫn bằng 10⁵ Pa vì pit-tông dịch chuyển tự do.", False,
     "Sai. Pit-tông tự do chỉ bảo đảm áp suất hai bên BẰNG NHAU chứ không bảo đảm giữ nguyên giá trị cũ. "
     "Ngăn phải bị nén nên áp suất chung tăng lên khoảng 1,10·10⁵ Pa."),
    ("Ở trạng thái cuối, thể tích ngăn trái gấp 1,2 lần thể tích ngăn phải.", True,
     "Đúng. Hai ngăn có cùng số mol và cùng áp suất nên V_trái/V_phải = T_trái/T_phải = 360/300 = 1,2."),
    ("Pit-tông dịch chuyển về phía ngăn phải khoảng 2,7 cm.", True,
     "Đúng. (30 + x)/(30 − x) = 1,2 ⟹ 2,2x = 6 ⟹ x ≈ 2,7 cm."),
    ("Áp suất chung ở trạng thái cuối vào khoảng 1,10·10⁵ Pa.", True,
     "Đúng. Xét ngăn phải đẳng nhiệt: p′ = 10⁵ · 30/27,27 ≈ 1,10·10⁵ Pa.")],
   "Xilanh hai ngăn", RK),

ds("Một xilanh thẳng đứng chứa cột khí cao 30 cm ở 27 °C, áp suất 10⁵ Pa, phía trên là pit-tông nhẹ dịch "
   "chuyển không ma sát; cách pit-tông 6 cm có vấu chặn. Đun nóng khí thật chậm.",
   [("Giai đoạn đầu (trước khi pit-tông chạm vấu) là quá trình đẳng áp.", True,
     "Đúng. Pit-tông còn tự do nên áp suất khí luôn bằng áp suất khí quyển cộng phần do pit-tông gây ra "
     "— một giá trị không đổi."),
    ("Sau khi pit-tông chạm vấu, tiếp tục đun thì quá trình trở thành đẳng tích.", True,
     "Đúng. Vấu chặn giữ pit-tông lại nên thể tích không tăng được nữa; từ đó áp suất mới bắt đầu tăng."),
    ("Ở giai đoạn sau, muốn áp suất khí tăng thêm 50 % thì phải tăng nhiệt độ tuyệt đối thêm 50 %.", True,
     "Đúng. Giai đoạn sau là đẳng tích nên p tỉ lệ thuận với T: p tăng 1,5 lần thì T cũng tăng 1,5 lần "
     "(lưu ý: tính theo nhiệt độ tuyệt đối, không phải theo độ Celsius)."),
    ("Nếu các vấu chặn được đặt cách pit-tông 12 cm thay vì 6 cm thì pit-tông sẽ chạm vấu ở nhiệt độ "
     "thấp hơn.", False,
     "Sai. Vấu càng xa thì khí phải giãn nhiều hơn mới chạm tới, mà ở giai đoạn đẳng áp thể tích tỉ lệ "
     "thuận với nhiệt độ tuyệt đối, nên pit-tông chạm vấu ở nhiệt độ CAO hơn.")],
   "Xilanh có vấu chặn – hai chặng", RK),

ds("Một khinh khí cầu thể tích 500 m³ có đáy hở nên áp suất khí bên trong luôn bằng áp suất khí quyển "
   "10⁵ Pa. Không khí ngoài ở 27 °C; đốt nóng khí trong cầu lên 87 °C. Cho M = 29 g/mol, "
   "R = 8,31 J/(mol·K), g = 10 m/s².",
   [("Khối lượng riêng của không khí ngoài vào khoảng 1,16 kg/m³.", True,
     "Đúng. ρ = pM/(RT) = 2900/(8,31 · 300) ≈ 1,163 kg/m³."),
    ("Khối lượng riêng của khí trong cầu sau khi đốt nóng vào khoảng 0,97 kg/m³.", True,
     "Đúng. ρ = 2900/(8,31 · 360) ≈ 0,969 kg/m³."),
    ("Khi đốt nóng, khối lượng khí trong cầu không đổi vì cầu kín.", False,
     "Sai. Cầu có đáy HỞ nên p và V không đổi; từ m = pVM/(RT), nhiệt độ tăng thì khối lượng khí trong "
     "cầu GIẢM — một phần khí thoát ra ngoài. Đó chính là cơ chế làm cầu nhẹ đi."),
    ("Lực nâng của cầu vào khoảng 968 N, tương ứng nâng được khoảng 96,8 kg.", True,
     "Đúng. F = (ρ_ngoài − ρ_trong)·V·g = (1,163 − 0,969) · 500 · 10 ≈ 968 N ⟹ khối lượng nâng được "
     "968/10 ≈ 96,8 kg (gồm vỏ cầu, giỏ và người).")],
   "Khối lượng riêng của khí – khinh khí cầu", RK),

ds("Trên giản đồ (p, V), một lượng khí lí tưởng xác định biến đổi theo ĐOẠN THẲNG từ A(1 L; 4·10⁵ Pa) tới "
   "B(4 L; 1·10⁵ Pa).",
   [("Nhiệt độ ở A bằng nhiệt độ ở B.", True,
     "Đúng. p_A V_A = 4 · 1 = 4 và p_B V_B = 1 · 4 = 4 (đơn vị 10⁵ Pa·L) nên T_A = T_B."),
    ("Vì T_A = T_B nên toàn bộ quá trình là đẳng nhiệt.", False,
     "Sai. Đường đẳng nhiệt trên giản đồ (p, V) là nhánh HYPEBOL, còn đây là ĐOẠN THẲNG. Hai điểm A, B "
     "chỉ tình cờ nằm trên cùng một đường đẳng nhiệt."),
    ("Nhiệt độ khí đạt giá trị lớn nhất khi thể tích bằng 2,5 L.", True,
     "Đúng. Trên đoạn AB có p = 5 − V (đơn vị 10⁵ Pa và L), nên pV = V(5 − V) đạt cực đại tại đỉnh "
     "V = 2,5 L."),
    ("Tỉ số giữa nhiệt độ lớn nhất và nhiệt độ ở A bằng 1,5625.", True,
     "Đúng. (pV)_max = 2,5 · 2,5 = 6,25 và (pV)_A = 4 ⟹ tỉ số 6,25/4 = 1,5625.")],
   "Suy luận trên giản đồ p–V", RK),
],
P3=[
sa("Xilanh nằm ngang dài 60 cm, pit-tông ở giữa, hai ngăn cùng khí ở 300 K và 10⁵ Pa. Giữ ngăn phải ở "
   "300 K, nung ngăn trái lên 360 K. Pit-tông dịch chuyển bao nhiêu cm (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "2,7",
   "V_trái/V_phải = T_trái/T_phải = 1,2 ⟹ (30 + x)/(30 − x) = 1,2 ⟹ 2,2x = 6 ⟹ x ≈ 2,7 cm.",
   "Xilanh hai ngăn", RK),

sa("Một xilanh nằm ngang có pit-tông nhẹ dịch chuyển không ma sát, bên trong là cột khí dài 20 cm ở "
   "27 °C. Làm lạnh khí tới −13 °C. Cột khí khi đó dài bao nhiêu xentimét "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "17,3",
   "Pit-tông tự do và xilanh nằm ngang nên áp suất khí luôn bằng áp suất khí quyển: quá trình đẳng áp.\n"
   "T₁ = 300 K; T₂ = 260 K ⟹ ℓ₂ = ℓ₁ · T₂/T₁ = 20 · 260/300 ≈ 17,3 cm.",
   "Quá trình đẳng áp – xilanh nằm ngang", K),

sa("Khinh khí cầu thể tích 500 m³, đáy hở, áp suất trong luôn bằng 10⁵ Pa. Không khí ngoài 27 °C, khí "
   "trong cầu 87 °C. Cho M = 29 g/mol, R = 8,31 J/(mol·K), g = 10 m/s². Lực nâng của cầu bằng bao nhiêu "
   "niutơn (làm tròn đến hàng đơn vị)?",
   "968",
   "ρ_ngoài = 2900/(8,31·300) ≈ 1,1633; ρ_trong = 2900/(8,31·360) ≈ 0,9694 kg/m³.\n"
   "F = (ρ_ngoài − ρ_trong)·V·g ≈ 0,1939 · 500 · 10 ≈ 968 N.",
   "Khinh khí cầu", RK),

sa("Một lượng khí lí tưởng ở 27 °C. Muốn tốc độ căn quân phương của phân tử tăng 50% thì phải nâng nhiệt "
   "độ lên bao nhiêu kelvin?",
   "675", "v ∝ √T ⟹ T₂ = T₁ · 1,5² = 300 · 2,25 = 675 K.", "Tốc độ phân tử", K),

sa("Trên giản đồ (p, V), một lượng khí biến đổi theo đoạn thẳng từ A(1 L; 4·10⁵ Pa) tới B(4 L; 1·10⁵ Pa). "
   "Nhiệt độ khí đạt giá trị lớn nhất khi thể tích bằng bao nhiêu lít?",
   "2,5",
   "Trên đoạn AB: p = 5 − V (10⁵ Pa, L) ⟹ pV = V(5 − V), là tam thức bậc hai hệ số âm, đạt cực đại tại "
   "đỉnh V = 5/2 = 2,5 L.",
   "Suy luận trên giản đồ p–V", RK),

sa("Quả bóng thể tích không đổi 3,0 L chứa khí ở 27 °C, áp suất 2,0·10⁵ Pa. Thay vì lấy bớt khí ra, "
   "người ta làm lạnh quả bóng để áp suất còn 1,2·10⁵ Pa. Khi đó nhiệt độ của khí bằng bao nhiêu kelvin?",
   "180",
   "Lượng khí và thể tích đều không đổi nên quá trình là đẳng tích:\n"
   "T₂ = T₁ · p₂/p₁ = 300 · 1,2/2,0 = 180 K.",
   "Quá trình đẳng tích", TB),
])


# =====================================================================
DE8 = dict(
ma="12C2-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Mô hình động học phân tử ở mức định lượng; hai bình ở nhiệt độ khác nhau",
P1=[
mc("Áp suất khí lí tưởng theo mô hình động học phân tử được viết là p = (1/3)·μ·m·v̄², trong đó μ là mật "
   "độ phân tử, m là khối lượng một phân tử. Biểu thức này có thể viết lại thành",
   ["p = (1/3)·ρ·v̄².", "p = (2/3)·ρ·v̄².", "p = 3ρ·v̄².", "p = ρ·v̄²."],
   "A",
   "Tích μ·m = (N/V)·m = m_tổng/V chính là khối lượng riêng ρ của khí, nên p = (1/3)ρ·v̄².",
   "Áp suất theo mô hình động học phân tử", K),

mc("Một chất khí có mật độ phân tử 2,4·10²⁵ m⁻³, khối lượng mỗi phân tử 5,0·10⁻²⁶ kg và tốc độ căn quân "
   "phương 500 m/s. Áp suất khí đó bằng",
   ["0,5·10⁵ Pa.", "1,0·10⁵ Pa.", "1,5·10⁵ Pa.", "3,0·10⁵ Pa."],
   "B",
   "p = (1/3)·μ·m·v̄² = (1/3) · 2,4·10²⁵ · 5,0·10⁻²⁶ · 500²\n"
   "  = (1/3) · 1,2 · 2,5·10⁵ = 1,0·10⁵ Pa.",
   "Áp suất theo mô hình động học phân tử", K),

mc("Không khí ở áp suất 10⁵ Pa có khối lượng riêng 1,2 kg/m³. Tốc độ căn quân phương của phân tử không "
   "khí khi đó bằng",
   ["289 m/s.", "408 m/s.", "500 m/s.", "707 m/s."],
   "C",
   "Từ p = (1/3)ρ·v̄² suy ra v̄² = 3p/ρ = 3 · 10⁵/1,2 = 2,5·10⁵ ⟹ v = 500 m/s.",
   "Áp suất – tốc độ phân tử", K),

mc("Bình A thể tích 2,0 L và bình B thể tích 3,0 L nối nhau bằng ống nhỏ, ban đầu cả hệ chứa khí ở 300 K "
   "và 10⁵ Pa. Giữ bình A ở 300 K và nung bình B lên 400 K. Áp suất chung của hệ khi đó gần nhất với",
   ["1,00·10⁵ Pa.", "1,18·10⁵ Pa.", "1,25·10⁵ Pa.", "1,33·10⁵ Pa."],
   "B",
   "Tổng số mol khí trong hệ không đổi. Viết n = pV/(RT) cho từng bình:\n"
   "Trước: n = 10⁵ · 5,0·10⁻³/(R · 300).\n"
   "Sau:   n = p · 2,0·10⁻³/(R · 300) + p · 3,0·10⁻³/(R · 400).\n"
   "⟹ 10⁵ · 5,0/300 = p(2,0/300 + 3,0/400) = p · 0,014167\n"
   "⟹ p = 1666,7/0,014167 ≈ 1,18·10⁵ Pa.\n"
   "Chú ý: không thể dùng pV/T = hằng số cho cả hệ vì hai phần có nhiệt độ khác nhau.",
   "Hai bình ở nhiệt độ khác nhau", RK),

mc("Một ống thuỷ tinh dài 38 cm, một đầu kín, đặt nằm ngang chứa cột khí dài 20 cm bị giam bởi cột thuỷ "
   "ngân dài 15 cm. Áp suất khí quyển 75 cmHg, nhiệt độ không đổi. Dựng ống thẳng đứng, miệng hướng lên. "
   "Chiều dài cột khí khi đó gần nhất với",
   ["15,0 cm.", "16,7 cm.", "18,2 cm.", "20,0 cm."],
   "B",
   "Nằm ngang: p₁ = 75 cmHg, ℓ₁ = 20 cm ⟹ p₁ℓ₁ = 1500.\n"
   "Miệng hướng lên: p₂ = 75 + 15 = 90 cmHg ⟹ ℓ₂ = 1500/90 ≈ 16,7 cm.\n"
   "Kiểm tra: 16,7 + 15 = 31,7 cm < 38 cm nên thuỷ ngân không tràn ra.",
   "Cột khí bị giam", K, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

mc("Vẫn với ống ở câu trên, khi dựng thẳng đứng miệng hướng XUỐNG thì",
   ["cột khí dài 25,0 cm, thuỷ ngân vẫn còn nguyên 15 cm.",
    "cột khí dài 23,0 cm, thuỷ ngân vẫn còn nguyên 15 cm.",
    "một phần thuỷ ngân chảy ra ngoài.",
    "cột khí ngắn lại còn 12,5 cm."],
   "C",
   "Nếu thuỷ ngân còn nguyên: p₃ = 75 − 15 = 60 cmHg ⟹ ℓ₃ = 1500/60 = 25 cm.\n"
   "Nhưng chỗ trống tối đa dành cho khí chỉ là 38 − 15 = 23 cm < 25 cm ⟹ mâu thuẫn.\n"
   "Vậy khí giãn ra đẩy thuỷ ngân tới miệng ống và một phần thuỷ ngân bị chảy ra ngoài.",
   "Cột khí bị giam – điều kiện ẩn", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

mc("Với ống ở hai câu trên, khi dựng thẳng đứng miệng hướng xuống, chiều dài cột thuỷ ngân còn lại trong "
   "ống gần nhất với",
   ["10,4 cm.", "12,1 cm.", "13,6 cm.", "15,0 cm."],
   "C",
   "Gọi x là chiều dài cột thuỷ ngân còn lại; thuỷ ngân nằm sát miệng ống nên cột khí dài (38 − x) và "
   "áp suất khí là p = 75 − x.\n"
   "(75 − x)(38 − x) = 1500 ⟹ x² − 113x + 1350 = 0\n"
   "⟹ x = (113 − √7369)/2 ≈ (113 − 85,84)/2 ≈ 13,6 cm (nghiệm còn lại lớn hơn chiều dài ống, bị loại).",
   "Cột khí bị giam – điều kiện ẩn", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

mc("Ở cùng nhiệt độ, tỉ số tốc độ căn quân phương của phân tử khí hiđrô (M = 2 g/mol) và khí oxi "
   "(M = 32 g/mol) bằng",
   ["1/4.", "1/16.", "4.", "16."],
   "C", "v ∝ 1/√M ⟹ v_H₂/v_O₂ = √(32/2) = √16 = 4.", "Tốc độ phân tử", K),

mc("Trong một bình kín, nếu tăng nhiệt độ tuyệt đối lên 4 lần thì tổng động năng tịnh tiến của các phân "
   "tử khí và áp suất khí lần lượt",
   ["đều tăng 4 lần.", "tăng 4 lần và tăng 2 lần.",
    "tăng 2 lần và tăng 4 lần.", "đều tăng 2 lần."],
   "A",
   "W_tổng = (3/2)nRT tỉ lệ thuận với T ⟹ tăng 4 lần.\n"
   "Thể tích không đổi nên p = nRT/V cũng tỉ lệ thuận với T ⟹ tăng 4 lần. "
   "(Đại lượng chỉ tăng 2 lần là TỐC ĐỘ căn quân phương.)",
   "Động năng phân tử – áp suất", K),

mc("Một bình 5,0 L chứa 2,0 g khí hiđrô (M = 2 g/mol) ở 27 °C. Áp suất khí trong bình là "
   "(R = 8,31 J/(mol·K))",
   ["2,49·10⁵ Pa.", "4,99·10⁵ Pa.", "9,97·10⁵ Pa.", "1,25·10⁵ Pa."],
   "B",
   "n = 2,0/2 = 1,0 mol ⟹ p = nRT/V = 1,0 · 8,31 · 300/(5,0·10⁻³) = 2493/5,0·10⁻³ ≈ 4,99·10⁵ Pa.",
   "Phương trình Clapeyron", TB),

mc("Nếu nén một lượng khí lí tưởng đẳng nhiệt tới thể tích bằng 1/4 ban đầu thì tốc độ căn quân phương "
   "của phân tử khí",
   ["tăng 2 lần.", "tăng 4 lần.", "giảm 2 lần.", "không đổi."],
   "D",
   "Tốc độ căn quân phương chỉ phụ thuộc nhiệt độ (v = √(3RT/M)); quá trình đẳng nhiệt nên v không đổi. "
   "Cái tăng 4 lần là mật độ phân tử và áp suất.",
   "Tốc độ phân tử", TB),

mc("Trong bình kín, nếu số phân tử khí giảm một nửa nhưng nhiệt độ tuyệt đối tăng gấp đôi thì áp suất khí",
   ["giảm 4 lần.", "giảm 2 lần.", "không đổi.", "tăng 2 lần."],
   "C",
   "p = (N/V)kT với V không đổi ⟹ p tỉ lệ thuận với tích N·T: (1/2) · 2 = 1 ⟹ áp suất không đổi.",
   "Phương trình trạng thái – mô hình phân tử", TB),

mc("Hai bình kín cùng thể tích, cùng áp suất, chứa cùng một loại khí nhưng bình A ở 300 K và bình B ở "
   "600 K. So sánh số phân tử trong hai bình:",
   ["Bình A gấp đôi bình B.", "Bình B gấp đôi bình A.",
    "Hai bình bằng nhau.", "Chưa đủ dữ kiện."],
   "A",
   "p = (N/V)kT: cùng p và V thì N tỉ lệ NGHỊCH với T ⟹ N_A/N_B = T_B/T_A = 600/300 = 2.",
   "Phương trình trạng thái – so sánh", K),

mc("Một lượng khí thực hiện quá trình từ (p₁, V₁, T₁) đến (p₂, V₂, T₂) với p₂ = 2p₁ và T₂ = 3T₁. "
   "Thể tích V₂ bằng",
   ["V₁/6.", "1,5V₁.", "2V₁/3.", "6V₁."],
   "B",
   "pV/T = hằng số ⟹ V₂ = V₁·(p₁/p₂)·(T₂/T₁) = V₁ · (1/2) · 3 = 1,5V₁.",
   "Phương trình trạng thái", TB),

mc("Khi nói “nhiệt độ tuyệt đối là số đo động năng chuyển động nhiệt trung bình của phân tử”, ta dựa vào "
   "hệ thức",
   ["pV = nRT.", "W̄đ = (3/2)kT.", "pV = hằng số.", "V/T = hằng số."],
   "B",
   "Hệ thức W̄đ = (3/2)kT thiết lập trực tiếp mối liên hệ giữa đại lượng vĩ mô (nhiệt độ) và đại lượng "
   "vi mô (động năng trung bình của phân tử).",
   "Động năng phân tử và nhiệt độ", TB),

mc("Trong thí nghiệm kiểm chứng định luật Boyle, nếu do sơ suất mà xilanh bị hở nhẹ làm khí thoát dần ra "
   "ngoài trong quá trình nén thì tích p·V đo được sẽ",
   ["vẫn là hằng số.", "giảm dần khi tiếp tục nén.",
    "tăng dần khi tiếp tục nén.", "lúc tăng lúc giảm."],
   "B",
   "pV = nRT: nhiệt độ không đổi nhưng n giảm dần do khí thoát ra, nên tích pV giảm dần. Đây là một sai "
   "số hệ thống nhận biết được ngay từ bảng số liệu.",
   "Phân tích sai số thí nghiệm", K, fig="k_sd_tn_boyle",
   cap="Bộ thí nghiệm kiểm chứng định luật Boyle"),

mc("Một xilanh chứa khí ở 27 °C được nén nhanh làm thể tích giảm một nửa. Áp suất khí sau khi nén",
   ["đúng bằng 2 lần áp suất ban đầu.", "lớn hơn 2 lần áp suất ban đầu.",
    "nhỏ hơn 2 lần áp suất ban đầu.", "không đổi."],
   "B",
   "Nén NHANH ⟹ khí không kịp toả nhiệt ⟹ nhiệt độ tăng. Từ pV/T = hằng số với V giảm 2 lần và T tăng, "
   "áp suất tăng NHIỀU HƠN 2 lần. Định luật Boyle chỉ cho đúng hệ số 2 khi nén chậm (đẳng nhiệt).",
   "Điều kiện áp dụng định luật Boyle", K),

mc("Đại lượng nào sau đây của khí lí tưởng phụ thuộc vào LOẠI khí?",
   ["Động năng tịnh tiến trung bình của phân tử ở một nhiệt độ cho trước.",
    "Tốc độ căn quân phương của phân tử ở một nhiệt độ cho trước.",
    "Số phân tử trong một mol.",
    "Tích pV của một mol khí ở một nhiệt độ cho trước."],
   "B",
   "v = √(3RT/M) phụ thuộc khối lượng mol M, tức phụ thuộc loại khí. Ba đại lượng còn lại đều như nhau "
   "với mọi khí lí tưởng ở cùng nhiệt độ.",
   "So sánh các khí", K),
],
P2=[
ds("Một chất khí lí tưởng có mật độ phân tử μ = 2,4·10²⁵ m⁻³, khối lượng mỗi phân tử m = 5,0·10⁻²⁶ kg, "
   "tốc độ căn quân phương v = 500 m/s.",
   [("Khối lượng riêng của khí đó là 1,2 kg/m³.", True,
     "Đúng. ρ = μ·m = 2,4·10²⁵ · 5,0·10⁻²⁶ = 1,2 kg/m³."),
    ("Áp suất của khí bằng 1,0·10⁵ Pa.", True,
     "Đúng. p = (1/3)ρ·v̄² = (1/3) · 1,2 · 500² = (1/3) · 1,2 · 2,5·10⁵ = 1,0·10⁵ Pa."),
    ("Nếu giữ nguyên nhiệt độ mà nén khí tới mật độ 4,8·10²⁵ m⁻³ thì áp suất tăng gấp đôi.", True,
     "Đúng. Nhiệt độ không đổi ⟹ v̄² không đổi ⟹ p = (1/3)μ·m·v̄² tỉ lệ thuận với μ."),
    ("Nếu giữ nguyên mật độ mà tăng nhiệt độ tuyệt đối gấp đôi thì tốc độ căn quân phương tăng gấp đôi.", False,
     "Sai. v ∝ √T nên nhiệt độ tăng 2 lần thì tốc độ chỉ tăng √2 ≈ 1,41 lần. Cái tăng gấp đôi là áp suất "
     "và động năng trung bình.")],
   "Áp suất theo mô hình động học phân tử", RK),

ds("Bình A (2,0 L) và bình B (3,0 L) nối nhau bằng ống nhỏ; ban đầu cả hệ chứa khí ở 300 K và 10⁵ Pa. "
   "Giữ bình A ở 300 K, nung bình B lên 400 K. Bỏ qua thể tích ống nối.",
   [("Không thể áp dụng hệ thức pV/T = hằng số cho toàn hệ vì hai phần có nhiệt độ khác nhau.", True,
     "Đúng. Hệ thức đó chỉ dùng cho một lượng khí ở một nhiệt độ xác định. Ở đây phải viết số mol riêng "
     "cho từng bình rồi cộng lại."),
    ("Sau khi nung, áp suất trong hai bình vẫn bằng nhau.", True,
     "Đúng. Hai bình thông nhau nên khí luôn tự phân bố lại cho tới khi áp suất cân bằng."),
    ("Áp suất chung sau khi nung vào khoảng 1,18·10⁵ Pa.", True,
     "Đúng. 10⁵ · 5,0/300 = p(2,0/300 + 3,0/400) ⟹ p ≈ 1,18·10⁵ Pa."),
    ("Sau khi nung, số mol khí trong bình B nhiều hơn trước khi nung.", False,
     "Sai. Bình B nóng lên nên khí trong đó nở ra và một phần chuyển sang bình A: số mol trong B GIẢM. "
     "(Kiểm tra: n_B sau = 1,18·10⁵ · 3,0·10⁻³/(R·400) < n_B trước = 10⁵ · 3,0·10⁻³/(R·300).)")],
   "Hai bình ở nhiệt độ khác nhau", RK),

ds("Một ống thuỷ tinh dài 38 cm, một đầu kín, nằm ngang, chứa cột khí dài 20 cm bị giam bởi cột thuỷ ngân "
   "dài 15 cm. Áp suất khí quyển 75 cmHg, nhiệt độ không đổi.",
   [("Hằng số Boyle của cột khí bị giam là 1500 (cmHg·cm).", True,
     "Đúng. Nằm ngang thì p = p₀ = 75 cmHg nên p·ℓ = 75 · 20 = 1500."),
    ("Khi dựng ống thẳng đứng, miệng hướng lên, cột khí dài khoảng 16,7 cm.", True,
     "Đúng. p = 75 + 15 = 90 cmHg ⟹ ℓ = 1500/90 ≈ 16,7 cm; tổng 16,7 + 15 = 31,7 cm < 38 cm nên hợp lệ."),
    ("Khi dựng ống thẳng đứng, miệng hướng xuống, cột khí dài đúng 25 cm và thuỷ ngân còn nguyên.", False,
     "Sai. Nếu thuỷ ngân còn nguyên thì cột khí phải dài 1500/60 = 25 cm, nhưng chỗ trống tối đa chỉ là "
     "38 − 15 = 23 cm. Mâu thuẫn này cho thấy một phần thuỷ ngân đã chảy ra ngoài."),
    ("Khi dựng ống miệng hướng xuống, cột thuỷ ngân còn lại dài khoảng 13,6 cm.", True,
     "Đúng. (75 − x)(38 − x) = 1500 ⟹ x² − 113x + 1350 = 0 ⟹ x ≈ 13,6 cm; khi đó cột khí dài 24,4 cm "
     "và áp suất khí là 61,4 cmHg (kiểm tra: 61,4 · 24,4 ≈ 1500 ✓).")],
   "Cột khí bị giam – điều kiện ẩn", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam bởi thuỷ ngân"),

ds("So sánh các đại lượng của hai khối khí lí tưởng khác loại ở cùng nhiệt độ.",
   [("Động năng tịnh tiến trung bình của phân tử hai khí bằng nhau.", True,
     "Đúng. W̄đ = (3/2)kT chỉ phụ thuộc nhiệt độ."),
    ("Tốc độ căn quân phương của phân tử hiđrô lớn gấp 4 lần của phân tử oxi.", True,
     "Đúng. v ∝ 1/√M ⟹ v_H₂/v_O₂ = √(32/2) = 4."),
    ("Ở cùng nhiệt độ và áp suất, hai bình cùng thể tích chứa hai khí khác loại có cùng số phân tử.", True,
     "Đúng, đó là nội dung định luật Avogadro, suy ra trực tiếp từ p = (N/V)kT."),
    ("Ở cùng nhiệt độ và áp suất, hai bình cùng thể tích chứa hai khí khác loại có cùng khối lượng khí.", False,
     "Sai. Cùng số phân tử nhưng khối lượng mỗi phân tử khác nhau nên khối lượng khí khác nhau, tỉ lệ với "
     "khối lượng mol M.")],
   "So sánh các khí", K),
],
P3=[
sa("Một chất khí có khối lượng mỗi phân tử 5,0·10⁻²⁶ kg và tốc độ căn quân phương 500 m/s. Động năng "
   "tịnh tiến trung bình của một phân tử khí đó bằng bao nhiêu (đơn vị 10⁻²¹ J, làm tròn đến chữ số "
   "thập phân thứ hai)?",
   "6,25",
   "Wđ = (1/2)·m·v̄² = 0,5 · 5,0·10⁻²⁶ · 500² = 0,5 · 5,0·10⁻²⁶ · 2,5·10⁵ = 6,25·10⁻²¹ J.",
   "Động năng phân tử", K),

sa("Ở cùng áp suất 10⁵ Pa, một chất khí có khối lượng riêng 4,8 kg/m³ — gấp bốn lần khối lượng riêng "
   "1,2 kg/m³ của không khí. Tốc độ căn quân phương của phân tử chất khí đó bằng bao nhiêu m/s?",
   "250",
   "Từ p = (1/3)ρv̄² suy ra v̄² = 3p/ρ, nên v tỉ lệ nghịch với căn bậc hai của khối lượng riêng.\n"
   "v̄² = 3·10⁵/4,8 = 6,25·10⁴ ⟹ v = 250 m/s, đúng bằng một nửa giá trị 500 m/s của không khí.",
   "Áp suất – tốc độ phân tử", K),

sa("Bình A (2,0 L) và bình B (3,0 L) nối nhau, ban đầu cả hệ ở 300 K và 10⁵ Pa. Giữ A ở 300 K, nung B lên "
   "400 K. Áp suất chung bằng bao nhiêu (đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ hai)?",
   "1,18",
   "Bảo toàn số mol: 10⁵·5,0/300 = p(2,0/300 + 3,0/400)\n"
   "⟹ 1666,7 = p · 0,014167 ⟹ p ≈ 1,18·10⁵ Pa.",
   "Hai bình ở nhiệt độ khác nhau", RK),

sa("Ống dài 38 cm, một đầu kín, nằm ngang, cột khí 20 cm bị giam bởi cột thuỷ ngân 15 cm; p₀ = 75 cmHg. "
   "Dựng ống thẳng đứng miệng hướng xuống. Chiều dài cột thuỷ ngân còn lại bằng bao nhiêu cm (làm tròn đến "
   "chữ số thập phân thứ nhất)?",
   "13,6",
   "Kiểm tra: nếu Hg còn nguyên thì ℓ = 1500/60 = 25 cm > 38 − 15 = 23 cm ⟹ Hg tràn ra.\n"
   "Gọi x là phần Hg còn lại: (75 − x)(38 − x) = 1500 ⟹ x² − 113x + 1350 = 0 ⟹ x ≈ 13,6 cm.",
   "Cột khí bị giam – điều kiện ẩn", RK, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

sa("Một bình 5,0 L chứa 2,0 g khí hiđrô (M = 2 g/mol) ở 27 °C. Áp suất khí trong bình bằng bao nhiêu "
   "(đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ hai)? Cho R = 8,31 J/(mol·K).",
   "4,99", "n = 1,0 mol ⟹ p = nRT/V = 8,31 · 300/(5,0·10⁻³) = 2493/0,005 ≈ 4,99·10⁵ Pa.",
   "Phương trình Clapeyron", TB),

sa("Ở cùng nhiệt độ, tốc độ căn quân phương của phân tử khí hiđrô (M = 2 g/mol) lớn gấp bao nhiêu lần của "
   "phân tử khí oxi (M = 32 g/mol)?",
   "4", "v ∝ 1/√M ⟹ v_H₂/v_O₂ = √(32/2) = √16 = 4.", "Tốc độ phân tử", K),
])


DEADV_TBL = ("Số liệu đo: V là thể tích đọc trên thang chia độ của xilanh",
             ["p (10⁵ Pa)", "1,0", "1,5", "2,0", "3,0", "6,0"],
             [["V đọc được (cm³)", "56", "36", "26", "16", "6"],
              ["p·V (10⁵ Pa·cm³)", "56", "54", "52", "48", "36"]])


# =====================================================================
DE9 = dict(
ma="12C2-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Xác định khối lượng mol; pit-tông gắn lò xo; chu trình nhiều chặng; ống nghiêng",
P1=[
mc("Một bình 2,0 L chứa 3,2 g một chất khí ở 27 °C, áp suất 1,25·10⁵ Pa. Khối lượng mol của khí đó gần "
   "nhất với (R = 8,31 J/(mol·K))",
   ["2 g/mol.", "16 g/mol.", "32 g/mol.", "44 g/mol."],
   "C",
   "Từ pV = (m/M)RT ⟹ M = mRT/(pV)\n"
   "M = 3,2·10⁻³ · 8,31 · 300/(1,25·10⁵ · 2,0·10⁻³) = 7,978/250 ≈ 0,0319 kg/mol ≈ 32 g/mol (khí oxi).",
   "Xác định khối lượng mol", K),

mc("Một xilanh nằm ngang tiết diện 10 cm², chứa cột khí dài 20 cm ở 300 K; pit-tông nối với một lò xo có "
   "độ cứng 100 N/m, ban đầu lò xo không biến dạng và áp suất khí bằng áp suất khí quyển 10⁵ Pa. Đun nóng "
   "khí làm pit-tông dịch chuyển 2,0 cm. Áp suất khí khi đó là",
   ["1,00·10⁵ Pa.", "1,02·10⁵ Pa.", "1,20·10⁵ Pa.", "2,00·10⁵ Pa."],
   "B",
   "Khi pit-tông dịch x, lò xo bị nén và đẩy ngược lại, làm áp suất khí phải lớn hơn áp suất khí quyển:\n"
   "p = p₀ + kx/S = 10⁵ + 100 · 0,020/(10·10⁻⁴) = 10⁵ + 2,0·10³ = 1,02·10⁵ Pa.",
   "Pit-tông gắn lò xo", RK),

mc("Vẫn với xilanh ở câu trên, nhiệt độ của khí khi pit-tông dịch chuyển 2,0 cm gần nhất với",
   ["320 K.", "330 K.", "337 K.", "360 K."],
   "C",
   "Trạng thái 1: p₁ = 10⁵ Pa, ℓ₁ = 20 cm, T₁ = 300 K.\n"
   "Trạng thái 2: p₂ = 1,02·10⁵ Pa, ℓ₂ = 22 cm.\n"
   "p₁ℓ₁/T₁ = p₂ℓ₂/T₂ ⟹ T₂ = 300 · (1,02 · 22)/(1,00 · 20) = 300 · 22,44/20 ≈ 337 K.",
   "Pit-tông gắn lò xo", RK),

mc("Một nhóm học sinh kiểm chứng định luật Boyle nhưng quên tính phần khí nằm ở đầu xilanh và trong ống "
   "nối. Bảng số liệu cho thấy tích p·V giảm dần khi p tăng. Giả thiết lượng khí bị nhốt còn chiếm thêm "
   "một thể tích V₀ không đổi, giá trị của V₀ là",
   ["2 cm³.", "4 cm³.", "6 cm³.", "8 cm³."],
   "B",
   "Định luật Boyle đúng phải viết p(V + V₀) = C. Lấy hai cặp số liệu ở hai đầu bảng:\n"
   "1,0(56 + V₀) = 6,0(6 + V₀) ⟹ 56 + V₀ = 36 + 6V₀ ⟹ 5V₀ = 20 ⟹ V₀ = 4 cm³.\n"
   "Kiểm tra toàn bảng: p(V + 4) = 1,0·60 = 1,5·40 = 2,0·30 = 3,0·20 = 6,0·10 = 60 ✓.",
   "Sai số hệ thống trong thí nghiệm", RK, tbl=DEADV_TBL, fig="k_sd_tn_boyle",
   cap="Thể tích “chết” ở đầu xilanh và trong ống nối"),

mc("Với bộ số liệu ở câu trên (V₀ = 4 cm³), hằng số của định luật Boyle cho lượng khí bị nhốt là",
   ["36·10⁵ Pa·cm³.", "48·10⁵ Pa·cm³.", "56·10⁵ Pa·cm³.", "60·10⁵ Pa·cm³."],
   "D", "C = p(V + V₀) = 1,0·(56 + 4) = 60·10⁵ Pa·cm³ (giống nhau ở cả năm lần đo).",
   "Sai số hệ thống trong thí nghiệm", K, tbl=DEADV_TBL),

mc("Một ống thuỷ tinh một đầu kín dài 50 cm chứa cột thuỷ ngân dài 10 cm. Khi ống thẳng đứng, miệng hướng "
   "lên, cột khí dài 30 cm; áp suất khí quyển 75 cmHg. Nghiêng ống sao cho trục ống hợp với phương ngang "
   "góc 30° (miệng vẫn ở trên). Chiều dài cột khí khi đó là",
   ["25,5 cm.", "30,0 cm.", "31,9 cm.", "34,0 cm."],
   "C",
   "Thẳng đứng: p₁ = 75 + 10 = 85 cmHg, ℓ₁ = 30 ⟹ p₁ℓ₁ = 2550.\n"
   "Nghiêng 30°: cột thuỷ ngân chỉ gây thêm áp suất bằng CHIỀU CAO thẳng đứng của nó, "
   "10·sin30° = 5 cmHg ⟹ p₂ = 80 cmHg.\n"
   "ℓ₂ = 2550/80 ≈ 31,9 cm. Kiểm tra 31,9 + 10 = 41,9 cm < 50 cm nên thuỷ ngân không tràn.",
   "Cột khí bị giam – ống nghiêng", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

mc("Trên giản đồ (p, V), một lượng khí lí tưởng đi từ M(2 L; 1·10⁵ Pa) theo ba quá trình khác nhau: "
   "(a) đẳng tích tới 2,6·10⁵ Pa; (b) đẳng áp tới 4 L; (c) đẳng nhiệt tới 4 L. Quá trình nào làm nhiệt độ "
   "khí tăng NHIỀU nhất?",
   ["Quá trình (a).", "Quá trình (b).", "Quá trình (c).", "Cả ba như nhau."],
   "A",
   "T tỉ lệ thuận với tích pV; (pV)_M = 2 · 1 = 2 (đơn vị 10⁵ Pa·L).\n"
   "(a): pV = 2 · 2,6 = 5,2 ⟹ T tăng 2,6 lần.\n"
   "(b): pV = 4 · 1 = 4 ⟹ T tăng 2,0 lần.\n"
   "(c): đẳng nhiệt ⟹ T không đổi.\n"
   "Vậy quá trình (a) làm nhiệt độ tăng nhiều nhất.",
   "So sánh các quá trình trên giản đồ", K, fig="k_dt_baquatrinh",
   cap="Ba quá trình xuất phát từ trạng thái M"),

mc("Hai bình giống nhau, mỗi bình thể tích V, nối bằng ống có khoá. Bình A chứa khí ở áp suất p và nhiệt "
   "độ T; bình B là chân không. Mở khoá rồi giữ cả hệ ở nhiệt độ T. Áp suất chung là",
   ["p.", "p/2.", "p/4.", "2p."],
   "B", "Lượng khí không đổi, nhiệt độ không đổi: pV = p′·2V ⟹ p′ = p/2.",
   "Hai bình thông nhau", TB),

mc("Một khối khí lí tưởng có thể tích 4,0 L ở 27 °C và 2,0·10⁵ Pa. Nén đẳng nhiệt tới 1,0 L rồi làm lạnh "
   "đẳng tích tới 150 K. Áp suất cuối cùng là",
   ["2,0·10⁵ Pa.", "4,0·10⁵ Pa.", "6,0·10⁵ Pa.", "8,0·10⁵ Pa."],
   "B",
   "Chặng 1 (đẳng nhiệt): p = 2,0·10⁵ · 4,0/1,0 = 8,0·10⁵ Pa.\n"
   "Chặng 2 (đẳng tích, 300 K → 150 K): p′ = 8,0·10⁵ · 150/300 = 4,0·10⁵ Pa.",
   "Quá trình nhiều chặng", K),

mc("Một bình kín chứa khí ở 27 °C, áp suất p. Người ta bơm thêm khí cùng loại vào bình và đồng thời nâng "
   "nhiệt độ lên 127 °C, kết quả áp suất tăng lên 2p. Khối lượng khí trong bình đã tăng",
   ["1,5 lần.", "1,6 lần.", "2,0 lần.", "2,7 lần."],
   "A",
   "p = (m/M)RT/V ⟹ m ∝ pV/T. Với V không đổi:\n"
   "m₂/m₁ = (p₂/p₁)·(T₁/T₂) = 2 · (300/400) = 1,5 lần.",
   "Lượng khí thay đổi", K),

mc("Ở cùng áp suất, khối lượng riêng của một khí ở 27 °C lớn gấp bao nhiêu lần khối lượng riêng của chính "
   "khí đó ở 327 °C?",
   ["1,2 lần.", "2,0 lần.", "6,0 lần.", "12,1 lần."],
   "B", "ρ = pM/(RT) tỉ lệ nghịch với T: ρ₁/ρ₂ = T₂/T₁ = 600/300 = 2.",
   "Khối lượng riêng của khí", TB),

mc("Một quả bóng cao su đàn hồi được bơm khí. Khi bơm thêm khí, cả áp suất và thể tích bóng đều tăng. Nếu "
   "áp suất tăng 1,2 lần, thể tích tăng 1,5 lần và nhiệt độ không đổi thì số phân tử khí trong bóng",
   ["tăng 1,25 lần.", "tăng 1,8 lần.", "tăng 2,7 lần.", "không đổi."],
   "B",
   "pV = NkT với T không đổi ⟹ N tỉ lệ thuận với tích pV: N₂/N₁ = 1,2 · 1,5 = 1,8 lần.",
   "Phương trình trạng thái – mô hình phân tử", K),

mc("Trong quá trình nén nhanh khí trong xilanh (coi như không trao đổi nhiệt), so với quá trình nén chậm "
   "tới cùng thể tích thì áp suất cuối và nhiệt độ cuối lần lượt",
   ["đều nhỏ hơn.", "đều lớn hơn.", "áp suất lớn hơn, nhiệt độ bằng nhau.",
    "áp suất bằng nhau, nhiệt độ lớn hơn."],
   "B",
   "Nén nhanh: khí nhận công mà không kịp toả nhiệt ⟹ nhiệt độ tăng. Cùng thể tích cuối nhưng nhiệt độ "
   "cao hơn thì theo pV = nRT áp suất cũng cao hơn.",
   "Điều kiện áp dụng định luật Boyle", K),

mc("Trong bình kín thể tích V chứa N phân tử khí ở nhiệt độ T. Nếu vừa giảm thể tích còn V/2 vừa giảm "
   "nhiệt độ còn T/2 thì mật độ phân tử và áp suất khí lần lượt",
   ["tăng 2 lần và không đổi.", "tăng 2 lần và tăng 2 lần.",
    "không đổi và giảm 2 lần.", "tăng 2 lần và giảm 2 lần."],
   "A",
   "Mật độ N/V tăng 2 lần (N không đổi, V giảm một nửa).\n"
   "p = (N/V)kT: mật độ tăng 2 lần nhưng T giảm 2 lần ⟹ áp suất không đổi.",
   "Mô hình động học phân tử", K),

mc("Một lượng khí lí tưởng thực hiện quá trình mà đồ thị trong hệ (p, T) là đoạn thẳng đi qua gốc toạ độ. "
   "Trong quá trình đó, thể tích khí",
   ["tăng.", "giảm.", "không đổi.", "tăng rồi giảm."],
   "C",
   "Đường thẳng qua gốc toạ độ trên hệ (p, T) nghĩa là p/T = hằng số, tức nR/V = hằng số ⟹ thể tích "
   "không đổi (quá trình đẳng tích).",
   "Đọc đồ thị", TB, fig="k_dt_dangtich", cap="Đường đẳng tích trong hệ (p, T)"),

mc("Cần bơm bao nhiêu lần bằng bơm có thể tích xilanh 0,25 L (khí ở 10⁵ Pa) để áp suất trong một bình "
   "thể tích 5,0 L tăng từ 10⁵ Pa lên 2,0·10⁵ Pa (nhiệt độ không đổi)?",
   ["10 lần.", "15 lần.", "20 lần.", "25 lần."],
   "C",
   "p·V = p₀V + n·p₀V₀ ⟹ 2,0·10⁵ · 5,0 = 10⁵ · 5,0 + n · 10⁵ · 0,25\n"
   "⟹ 10 = 5,0 + 0,25n (đơn vị 10⁵ Pa·L) ⟹ n = 20 lần.",
   "Bơm khí", K),

mc("Một chất khí có khối lượng mol M ở nhiệt độ T. Nếu thay bằng khí khác có khối lượng mol 4M ở cùng "
   "nhiệt độ thì động năng tịnh tiến trung bình của phân tử và tốc độ căn quân phương lần lượt",
   ["không đổi và giảm 2 lần.", "không đổi và giảm 4 lần.",
    "giảm 4 lần và giảm 2 lần.", "giảm 4 lần và không đổi."],
   "A",
   "W̄đ = (3/2)kT chỉ phụ thuộc T ⟹ không đổi.\nv = √(3RT/M) ∝ 1/√M ⟹ M tăng 4 lần thì v giảm √4 = 2 lần.",
   "Động năng – tốc độ phân tử", K),

mc("Điều kiện nào sau đây KHÔNG cần thiết để áp dụng hệ thức pV/T = hằng số?",
   ["Lượng khí không đổi.", "Khí được coi là khí lí tưởng.",
    "Nhiệt độ tính theo thang Kelvin.", "Quá trình phải diễn ra rất chậm."],
   "D",
   "pV/T = hằng số liên hệ hai TRẠNG THÁI CÂN BẰNG, không phụ thuộc quá trình đi giữa chúng nhanh hay "
   "chậm. Ba điều kiện còn lại đều bắt buộc.",
   "Điều kiện áp dụng phương trình trạng thái", K),
],
P2=[
ds("Một xilanh nằm ngang tiết diện 10 cm² chứa cột khí dài 20 cm ở 300 K; pit-tông nối với lò xo độ cứng "
   "100 N/m, ban đầu lò xo không biến dạng và áp suất khí bằng áp suất khí quyển 10⁵ Pa. Đun nóng khí.",
   [("Khi pit-tông dịch chuyển một đoạn x, áp suất khí bằng p₀ + kx/S.", True,
     "Đúng. Pit-tông cân bằng dưới ba lực: áp lực khí bên trong pS, áp lực khí quyển p₀S và lực đàn hồi "
     "kx cùng chiều với áp lực khí quyển."),
    ("Khi pit-tông dịch 2,0 cm, áp suất khí là 1,02·10⁵ Pa.", True,
     "Đúng. p = 10⁵ + 100 · 0,020/(10·10⁻⁴) = 10⁵ + 2000 = 1,02·10⁵ Pa."),
    ("Khi pit-tông dịch 2,0 cm, nhiệt độ khí vào khoảng 337 K.", True,
     "Đúng. T₂ = 300 · (1,02 · 22)/(1,00 · 20) ≈ 337 K (dùng chiều dài thay cho thể tích vì tiết diện "
     "không đổi)."),
    ("Quá trình đun nóng này là quá trình đẳng áp vì pit-tông dịch chuyển được.", False,
     "Sai. Lò xo càng bị nén càng đẩy mạnh, nên áp suất khí TĂNG dần theo độ dịch chuyển. Đây không phải "
     "quá trình đẳng áp mà là quá trình có p tăng tuyến tính theo thể tích.")],
   "Pit-tông gắn lò xo", RK),

ds("Bảng bên là số liệu của một nhóm học sinh khi kiểm chứng định luật Boyle; nhóm đã quên không tính phần "
   "khí ở đầu xilanh và trong ống nối (thể tích V₀ không đổi).",
   [("Việc tích p·V giảm dần khi p tăng chứng tỏ chất khí không tuân theo định luật Boyle.", False,
     "Sai. Chất khí vẫn tuân theo định luật; cái sai nằm ở PHÉP ĐO. Thể tích thật của lượng khí bị nhốt "
     "là V + V₀ chứ không phải số đọc V."),
    ("Thể tích “chết” V₀ bằng 4 cm³.", True,
     "Đúng. 1,0(56 + V₀) = 6,0(6 + V₀) ⟹ 5V₀ = 20 ⟹ V₀ = 4 cm³."),
    ("Khi cộng thêm 4 cm³ vào mọi giá trị thể tích đọc được thì tích p(V + 4) là hằng số 60·10⁵ Pa·cm³.", True,
     "Đúng. 1,0·60 = 1,5·40 = 2,0·30 = 3,0·20 = 6,0·10 = 60 ở cả năm lần đo."),
    ("Nếu vẽ đồ thị V theo 1/p thì đường thẳng thu được cắt trục V tại −4 cm³.", True,
     "Đúng. Từ p(V + V₀) = C ⟹ V = C·(1/p) − V₀, tung độ gốc là −V₀ = −4 cm³. Đây là kĩ thuật thực nghiệm "
     "để đo thể tích chết mà không cần tháo dụng cụ.")],
   "Sai số hệ thống trong thí nghiệm", RK, tbl=DEADV_TBL, fig="k_sd_tn_boyle",
   cap="Thể tích chết ở đầu xilanh"),

ds("Một ống thuỷ tinh một đầu kín dài 50 cm chứa cột thuỷ ngân dài 10 cm; khi ống thẳng đứng miệng hướng "
   "lên thì cột khí dài 30 cm. Áp suất khí quyển 75 cmHg, nhiệt độ không đổi.",
   [("Áp suất cột khí bị giam khi ống thẳng đứng miệng hướng lên là 85 cmHg.", True,
     "Đúng. p = p₀ + h = 75 + 10 = 85 cmHg; hằng số Boyle là 85 · 30 = 2550."),
    ("Khi đặt ống nằm ngang, cột khí dài 34 cm.", True,
     "Đúng. p = 75 cmHg ⟹ ℓ = 2550/75 = 34 cm; kiểm tra 34 + 10 = 44 cm < 50 cm nên hợp lệ."),
    ("Khi nghiêng ống 30° so với phương ngang (miệng ở trên), cột khí dài khoảng 31,9 cm.", True,
     "Đúng. Cột thuỷ ngân chỉ gây thêm áp suất bằng chiều cao thẳng đứng 10·sin30° = 5 cmHg ⟹ p = 80 cmHg "
     "⟹ ℓ = 2550/80 ≈ 31,9 cm."),
    ("Khi lộn ngược ống cho miệng hướng xuống thì cột khí dài khoảng 39,2 cm; kết quả này vẫn đúng nếu "
     "ống chỉ dài 45 cm.", False,
     "Vế đầu đúng: p = 75 − 10 = 65 cmHg ⟹ ℓ = 2550/65 ≈ 39,2 cm, và với ống dài 50 cm thì chỗ trống tối "
     "đa cho khí là 50 − 10 = 40 cm > 39,2 cm nên thuỷ ngân không tràn.\n"
     "Nhưng vế sau SAI: nếu ống chỉ dài 45 cm thì chỗ trống tối đa chỉ là 45 − 10 = 35 cm < 39,2 cm, "
     "khí sẽ đẩy thuỷ ngân tới miệng và một phần thuỷ ngân chảy ra ngoài; khi đó phải giải phương trình "
     "bậc hai cho phần thuỷ ngân còn lại.")],
   "Cột khí bị giam – ống nghiêng", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

ds("Một lượng khí lí tưởng xác định biến đổi qua nhiều chặng. Cho R = 8,31 J/(mol·K).",
   [("Nén đẳng nhiệt 4,0 L ở 2,0·10⁵ Pa xuống 1,0 L thì áp suất trở thành 8,0·10⁵ Pa.", True,
     "Đúng. p = 2,0·10⁵ · 4,0/1,0 = 8,0·10⁵ Pa."),
    ("Tiếp tục làm lạnh đẳng tích từ 300 K xuống 150 K thì áp suất còn 4,0·10⁵ Pa.", True,
     "Đúng. p′ = 8,0·10⁵ · 150/300 = 4,0·10⁵ Pa."),
    ("Sau cả hai chặng, tích pV của khối khí bằng đúng giá trị ban đầu.", False,
     "Sai. Ban đầu pV = 2,0·10⁵ · 4,0·10⁻³ = 800 J; cuối cùng pV = 4,0·10⁵ · 1,0·10⁻³ = 400 J, "
     "giảm một nửa — phù hợp với việc nhiệt độ giảm từ 300 K xuống 150 K."),
    ("Một bình kín chứa khí ở 27 °C và áp suất p; bơm thêm khí đồng thời nâng nhiệt độ lên 127 °C làm áp "
     "suất tăng thành 2p thì khối lượng khí trong bình tăng 1,5 lần.", True,
     "Đúng. m ∝ pV/T với V không đổi: m₂/m₁ = 2 · 300/400 = 1,5.")],
   "Quá trình nhiều chặng – lượng khí thay đổi", K),
],
P3=[
sa("Một bình 2,0 L chứa 3,2 g khí ở 27 °C, áp suất 1,25·10⁵ Pa. Khối lượng mol của khí bằng bao nhiêu "
   "g/mol (làm tròn đến hàng đơn vị)? Cho R = 8,31 J/(mol·K).",
   "32",
   "M = mRT/(pV) = 3,2·10⁻³ · 8,31 · 300/(1,25·10⁵ · 2,0·10⁻³) = 7,978/250 ≈ 0,0319 kg/mol ≈ 32 g/mol.",
   "Xác định khối lượng mol", K),

sa("Xilanh nằm ngang tiết diện 10 cm², cột khí dài 20 cm ở 300 K, pit-tông nối lò xo k = 100 N/m (ban đầu "
   "không biến dạng, p = 10⁵ Pa). Đun nóng làm pit-tông dịch 2,0 cm. Nhiệt độ khí khi đó bằng bao nhiêu "
   "kelvin (làm tròn đến hàng đơn vị)?",
   "337",
   "p₂ = 10⁵ + kx/S = 10⁵ + 100·0,020/10⁻³ = 1,02·10⁵ Pa.\n"
   "T₂ = T₁·p₂ℓ₂/(p₁ℓ₁) = 300 · (1,02 · 22)/(1,00 · 20) ≈ 337 K.",
   "Pit-tông gắn lò xo", RK),

sa("Từ bảng số liệu có thể tích “chết”, giá trị V₀ bằng bao nhiêu cm³?",
   "4",
   "p(V + V₀) = C. Lấy hai cặp biên: 1,0(56 + V₀) = 6,0(6 + V₀) ⟹ 5V₀ = 20 ⟹ V₀ = 4 cm³.",
   "Sai số hệ thống trong thí nghiệm", RK, tbl=DEADV_TBL),

sa("Ống thuỷ tinh một đầu kín dài 50 cm, cột thuỷ ngân 10 cm; khi ống thẳng đứng miệng hướng lên thì cột "
   "khí dài 30 cm (p₀ = 75 cmHg). Nghiêng ống 30° so với phương ngang, miệng ở trên. Cột khí dài bao nhiêu "
   "cm (làm tròn đến chữ số thập phân thứ nhất)?",
   "31,9",
   "p₁ℓ₁ = 85 · 30 = 2550. Nghiêng 30°: p₂ = 75 + 10·sin30° = 80 cmHg ⟹ ℓ₂ = 2550/80 ≈ 31,9 cm.",
   "Cột khí bị giam – ống nghiêng", RK, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

sa("Một bình thể tích 5,0 L đang chứa khí ở 10⁵ Pa. Người ta bơm thêm 30 lần bằng bơm có thể tích "
   "xilanh 0,25 L, mỗi lần đưa vào bình lượng khí ở 10⁵ Pa. Áp suất trong bình khi đó bằng bao nhiêu "
   "(đơn vị 10⁵ Pa, làm tròn đến chữ số thập phân thứ nhất)? Nhiệt độ không đổi.",
   "2,5",
   "Tổng lượng khí quy về cùng áp suất (đơn vị 10⁵ Pa·L):\n"
   "p · 5,0 = 1,0 · 5,0 + 30 · 1,0 · 0,25 = 5,0 + 7,5 = 12,5 ⟹ p = 12,5/5,0 = 2,5·10⁵ Pa.",
   "Bơm khí", K),

sa("Một bình kín chứa khí ở 27 °C và áp suất p. Bơm thêm khí cùng loại và nâng nhiệt độ lên 127 °C, áp "
   "suất trở thành 2p. Khối lượng khí trong bình đã tăng bao nhiêu lần (làm tròn đến chữ số thập phân "
   "thứ nhất)?",
   "1,5", "m ∝ pV/T với V không đổi ⟹ m₂/m₁ = 2 · (300/400) = 1,5 lần.",
   "Lượng khí thay đổi", K),
])


# =====================================================================
DE10 = dict(
ma="12C2-Đ10", ten="ĐỀ SỐ 10", muc="Khó / thử thách",
trongtam="Hệ nhiều phần ở nhiệt độ khác nhau; van xả; bài toán ngược và biện luận điều kiện",
P1=[
mc("Một xilanh nằm ngang dài 100 cm, pit-tông mỏng ở chính giữa, hai ngăn cùng chứa khí ở 300 K và "
   "10⁵ Pa. Nung ngăn trái lên 400 K và ngăn phải lên 350 K. Pit-tông dịch chuyển một đoạn gần nhất với",
   ["2,5 cm.", "3,3 cm.", "4,2 cm.", "6,7 cm."],
   "B",
   "Hai ngăn ban đầu giống hệt nhau nên cùng số mol; ở trạng thái cuối chúng có cùng áp suất p′ nên\n"
   "V_trái/V_phải = T_trái/T_phải = 400/350 = 8/7.\n"
   "Đặt độ dịch chuyển x: (50 + x)/(50 − x) = 8/7 ⟹ 350 + 7x = 400 − 8x ⟹ 15x = 50 ⟹ x ≈ 3,3 cm.",
   "Xilanh hai ngăn", RK),

mc("Với xilanh ở câu trên, áp suất chung ở trạng thái cuối gần nhất với",
   ["1,10·10⁵ Pa.", "1,17·10⁵ Pa.", "1,25·10⁵ Pa.", "1,33·10⁵ Pa."],
   "C",
   "Xét ngăn phải: p₀V₀/T₀ = p′V′/T′ ⟹ 10⁵ · 50/300 = p′ · 46,67/350\n"
   "⟹ p′ = 10⁵ · 50 · 350/(300 · 46,67) ≈ 1,25·10⁵ Pa.\n"
   "(Kiểm tra bằng ngăn trái: 10⁵ · 50/300 = 1,25·10⁵ · 53,33/400 ✓)",
   "Xilanh hai ngăn", RK),

mc("Một bình kín thể tích không đổi chứa khí ở 300 K, áp suất 1,5·10⁵ Pa; bình có van xả tự mở khi áp "
   "suất đạt 3,0·10⁵ Pa và giữ áp suất trong bình không vượt quá giá trị đó. Nhiệt độ khi van bắt đầu mở là",
   ["450 K.", "600 K.", "750 K.", "900 K."],
   "B",
   "Trước khi van mở, lượng khí không đổi và thể tích không đổi ⟹ p/T = hằng số:\n"
   "T = 300 · 3,0/1,5 = 600 K.",
   "Van xả – quá trình đẳng tích", K),

mc("Vẫn với bình ở câu trên, tiếp tục đun tới 900 K (van vẫn mở, áp suất giữ 3,0·10⁵ Pa). Phần trăm khối "
   "lượng khí đã thoát ra khỏi bình so với ban đầu là",
   ["25,0%.", "33,3%.", "50,0%.", "66,7%."],
   "B",
   "Khối lượng khí trong bình tỉ lệ với pV/T (V, M không đổi):\n"
   "m_đầu ∝ 1,5·10⁵/300 = 500;  m_cuối ∝ 3,0·10⁵/900 ≈ 333,3.\n"
   "m_cuối/m_đầu = 333,3/500 = 0,667 ⟹ đã thoát ra khoảng 33,3%.",
   "Van xả – lượng khí thay đổi", RK),

mc("Một lượng khí lí tưởng được nung nóng đẳng áp thêm 60 K thì thể tích tăng 20%. Nhiệt độ ban đầu của "
   "khí là",
   ["27 °C.", "47 °C.", "57 °C.", "77 °C."],
   "A",
   "Đẳng áp ⟹ V tỉ lệ thuận với T: (T + 60)/T = 1,20 ⟹ 0,20T = 60 ⟹ T = 300 K ⟹ t = 27 °C.",
   "Định luật Charles – bài toán ngược", K),

mc("Bình A thể tích 1,0 L chứa khí ở 300 K, áp suất 4,0·10⁵ Pa; bình B thể tích 3,0 L là chân không. Nối "
   "hai bình bằng ống nhỏ rồi giữ bình A ở 300 K nhưng bình B ở 400 K. Áp suất chung sau đó gần nhất với",
   ["1,00·10⁵ Pa.", "1,23·10⁵ Pa.", "1,33·10⁵ Pa.", "1,60·10⁵ Pa."],
   "B",
   "Tổng số mol khí không đổi; phải viết số mol RIÊNG cho từng bình vì chúng ở hai nhiệt độ khác nhau.\n"
   "Trước khi mở: n = 4,0·10⁵ · 1,0·10⁻³/(R · 300).\n"
   "Sau khi mở:  n = p · 1,0·10⁻³/(R · 300) + p · 3,0·10⁻³/(R · 400).\n"
   "⟹ 4,0·10⁵ · 1,0/300 = p(1,0/300 + 3,0/400)\n"
   "⟹ 1333,3 = p · 0,0108333 ⟹ p ≈ 1,23·10⁵ Pa.\n"
   "Bẫy: bỏ qua chênh lệch nhiệt độ (chỉ dùng định luật Boyle) cho 1,00·10⁵ Pa; coi cả hệ ở 400 K cho "
   "1,33·10⁵ Pa.",
   "Hai bình ở nhiệt độ khác nhau", RK),

mc("Một quả bóng đàn hồi có áp suất khí bên trong luôn tỉ lệ thuận với thể tích của nó (p = aV). Khi nung "
   "nóng bóng từ 300 K lên 432 K thì thể tích bóng",
   ["tăng 1,2 lần.", "tăng 1,44 lần.", "tăng 1,73 lần.", "tăng 2,0 lần."],
   "A",
   "Thay p = aV vào pV = nRT: aV² = nRT ⟹ V ∝ √T.\n"
   "V₂/V₁ = √(432/300) = √1,44 = 1,2 lần.",
   "Quá trình phi tuyến", RK),

mc("Trên giản đồ (p, T), một lượng khí lí tưởng biến đổi theo đoạn thẳng KHÔNG đi qua gốc toạ độ, cắt "
   "trục p tại giá trị dương. Trong quá trình đó, thể tích khí",
   ["không đổi.", "tăng liên tục.", "giảm liên tục.", "tăng rồi giảm."],
   "B",
   "Giả sử p = p₀ + bT với p₀ > 0. Khi đó V = nRT/p = nRT/(p₀ + bT). Chia tử và mẫu cho T:\n"
   "V = nR/(p₀/T + b). Khi T tăng, p₀/T giảm nên mẫu số giảm ⟹ V TĂNG liên tục.\n"
   "Đường thẳng qua gốc toạ độ mới là đẳng tích; ở đây p₀ ≠ 0 nên chắc chắn không đẳng tích.",
   "Đọc đồ thị – suy luận", RK),

mc("Một bình chứa khí lí tưởng. Nếu tăng nhiệt độ tuyệt đối thêm 20% và giảm thể tích đi 20% thì áp suất "
   "khí tăng",
   ["40%.", "44%.", "50%.", "60%."],
   "C",
   "p₂/p₁ = (T₂/T₁)·(V₁/V₂) = 1,20/0,80 = 1,50 ⟹ áp suất tăng 50%.\n"
   "Bẫy: cộng dồn 20% + 20% = 40% là sai.",
   "Phương trình trạng thái", K),

mc("Hai bình kín A và B có thể tích bằng nhau, chứa cùng loại khí. Bình A: 300 K, áp suất p. Bình B: "
   "600 K, áp suất 3p. Tỉ số số phân tử khí trong bình B và bình A là",
   ["0,5.", "1,0.", "1,5.", "3,0."],
   "C",
   "p = (N/V)kT ⟹ N ∝ p/T (V như nhau).\n"
   "N_B/N_A = (3p/600)/(p/300) = (3/600)·(300/1) = 1,5.",
   "Mô hình động học phân tử – so sánh", K),

mc("Một cột khí bị giam trong ống nằm ngang bởi cột thuỷ ngân dài h. Khi dựng ống thẳng đứng miệng hướng "
   "lên, chiều dài cột khí giảm 20%. Nếu áp suất khí quyển là 75 cmHg thì h bằng",
   ["12,5 cm.", "15,0 cm.", "18,75 cm.", "20,0 cm."],
   "C",
   "Nằm ngang: p₁ = 75. Thẳng đứng miệng lên: p₂ = 75 + h.\n"
   "Cột khí giảm 20% nghĩa là ℓ₂ = 0,80ℓ₁, mà p₁ℓ₁ = p₂ℓ₂:\n"
   "75ℓ₁ = (75 + h)·0,80ℓ₁ ⟹ 75 = 60 + 0,80h ⟹ h = 15/0,80 = 18,75 cm.",
   "Cột khí bị giam – bài toán ngược", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),

mc("Khi đun nóng đẳng áp một lượng khí lí tưởng, đại lượng nào sau đây giảm?",
   ["Thể tích.", "Nhiệt độ.", "Khối lượng riêng.", "Động năng trung bình của phân tử."],
   "C",
   "Đẳng áp: T tăng, V tăng, W̄đ tăng. Khối lượng khí không đổi mà thể tích tăng nên khối lượng riêng "
   "ρ = m/V GIẢM (cũng thấy từ ρ = pM/(RT) tỉ lệ nghịch với T).",
   "Khối lượng riêng của khí", K),

mc("Nếu đồng thời tăng nhiệt độ tuyệt đối lên 2 lần và tăng số phân tử lên 2 lần trong một bình có thể "
   "tích tăng 4 lần thì áp suất khí",
   ["không đổi.", "tăng 2 lần.", "giảm 2 lần.", "tăng 4 lần."],
   "A",
   "p = (N/V)kT ⟹ p₂/p₁ = (N₂/N₁)·(V₁/V₂)·(T₂/T₁) = 2 · (1/4) · 2 = 1 ⟹ áp suất không đổi.",
   "Mô hình động học phân tử", K),

mc("Một lượng khí lí tưởng thực hiện quá trình sao cho áp suất tỉ lệ nghịch với bình phương thể tích "
   "(p = a/V²). Khi thể tích tăng 2 lần thì nhiệt độ tuyệt đối",
   ["tăng 2 lần.", "giảm 2 lần.", "giảm 4 lần.", "không đổi."],
   "B",
   "T ∝ pV = (a/V²)·V = a/V ⟹ T tỉ lệ nghịch với V. Thể tích tăng 2 lần thì nhiệt độ giảm 2 lần.",
   "Quá trình phi tuyến", RK),

mc("Một bình kín chứa hỗn hợp khí gồm n₁ mol khí X và n₂ mol khí Y ở nhiệt độ T, thể tích V. Áp suất của "
   "hỗn hợp bằng",
   ["(n₁ − n₂)RT/V.", "(n₁ + n₂)RT/V.", "n₁n₂RT/V.", "√(n₁n₂)·RT/V."],
   "B",
   "Áp suất do TẤT CẢ các phân tử va chạm vào thành bình gây ra, không phân biệt loại; chỉ phụ thuộc "
   "tổng số mol: p = (n₁ + n₂)RT/V.",
   "Hỗn hợp khí", K),

mc("Một quả bóng bay chứa khí heli được thả từ mặt đất. Nếu vỏ bóng không đàn hồi (thể tích cố định) thì "
   "khi lên cao, so với khi vỏ đàn hồi, bóng sẽ",
   ["nổ sớm hơn.", "nổ muộn hơn hoặc không nổ nhưng lực nâng giảm nhanh hơn.",
    "bay cao hơn.", "không có gì khác biệt."],
   "B",
   "Vỏ cố định ⟹ thể tích không đổi ⟹ lực đẩy Archimedes ρ_ngoài·V·g giảm nhanh theo độ cao (vì ρ_ngoài "
   "giảm) mà không được bù bởi việc bóng nở ra. Bóng cũng không bị căng vỡ do khí nở.",
   "Phương trình trạng thái – thực tiễn", K, fig="k_sd_bongbay",
   cap="Bóng bay ở các độ cao khác nhau"),

mc("Muốn tăng áp suất khí trong một bình kín lên 4 lần mà chỉ được phép thay đổi nhiệt độ, phải",
   ["tăng nhiệt độ Celsius lên 4 lần.", "tăng nhiệt độ tuyệt đối lên 4 lần.",
    "tăng nhiệt độ tuyệt đối lên 2 lần.", "tăng nhiệt độ tuyệt đối lên 16 lần."],
   "B", "Thể tích và lượng khí không đổi ⟹ p tỉ lệ thuận với T (tuyệt đối) ⟹ phải tăng T lên 4 lần.",
   "Quá trình đẳng tích", TB),

mc("Trong bốn phát biểu sau về khí lí tưởng, phát biểu nào SAI?",
   ["Áp suất khí tỉ lệ thuận với mật độ phân tử khi nhiệt độ không đổi.",
    "Động năng tịnh tiến trung bình của phân tử tỉ lệ thuận với nhiệt độ tuyệt đối.",
    "Tốc độ căn quân phương của phân tử tỉ lệ thuận với nhiệt độ tuyệt đối.",
    "Ở cùng nhiệt độ và áp suất, các thể tích bằng nhau của mọi khí chứa cùng số phân tử."],
   "C",
   "Tốc độ căn quân phương tỉ lệ với CĂN BẬC HAI của nhiệt độ tuyệt đối (v ∝ √T), không tỉ lệ thuận với "
   "T. Ba phát biểu còn lại đều đúng.",
   "Tổng hợp lí thuyết khí lí tưởng", K),
],
P2=[
ds("Một xilanh nằm ngang dài 100 cm, pit-tông mỏng ở giữa, hai ngăn cùng chứa khí ở 300 K và 10⁵ Pa. "
   "Nung ngăn trái lên 400 K và ngăn phải lên 350 K.",
   [("Ở trạng thái cân bằng mới, áp suất hai ngăn bằng nhau.", True,
     "Đúng. Pit-tông mỏng, dịch chuyển không ma sát nên chỉ cân bằng khi áp lực hai bên bằng nhau."),
    ("Tỉ số thể tích hai ngăn (trái : phải) bằng 8 : 7.", True,
     "Đúng. Cùng số mol, cùng áp suất ⟹ V ∝ T: 400 : 350 = 8 : 7."),
    ("Pit-tông dịch chuyển về phía ngăn phải khoảng 3,3 cm.", True,
     "Đúng. (50 + x)/(50 − x) = 8/7 ⟹ 15x = 50 ⟹ x ≈ 3,3 cm."),
    ("Áp suất chung ở trạng thái cuối vẫn bằng 10⁵ Pa vì hai ngăn được nung như nhau về “tỉ lệ”.", False,
     "Sai. Xét ngăn phải: 10⁵ · 50/300 = p′ · 46,67/350 ⟹ p′ ≈ 1,25·10⁵ Pa. Cả hai ngăn đều nóng lên "
     "nên áp suất chung tăng lên đáng kể.")],
   "Xilanh hai ngăn", RK),

ds("Một bình kín thể tích không đổi chứa khí ở 300 K, áp suất 1,5·10⁵ Pa. Bình có van xả tự mở khi áp "
   "suất đạt 3,0·10⁵ Pa và giữ cho áp suất không vượt quá giá trị đó.",
   [("Trước khi van mở, quá trình là đẳng tích với lượng khí không đổi.", True,
     "Đúng. Bình kín, thể tích không đổi và chưa có khí thoát ra."),
    ("Van bắt đầu mở khi nhiệt độ khí đạt 600 K.", True,
     "Đúng. p/T = hằng số ⟹ T = 300 · 3,0/1,5 = 600 K."),
    ("Sau khi van mở, nếu tiếp tục đun thì áp suất khí trong bình tiếp tục tăng.", False,
     "Sai. Van giữ áp suất không vượt quá 3,0·10⁵ Pa; khi đun tiếp, khí thoát bớt ra ngoài để duy trì áp "
     "suất đó, tức quá trình trở thành đẳng áp với lượng khí giảm dần."),
    ("Khi nhiệt độ đạt 900 K, khoảng 33% khối lượng khí ban đầu đã thoát ra ngoài.", True,
     "Đúng. m ∝ p/T (V, M không đổi): m_cuối/m_đầu = (3,0/900)/(1,5/300) = 0,667 ⟹ thoát ra ≈ 33,3%.")],
   "Van xả – lượng khí thay đổi", RK),

ds("Xét một số quá trình phi tuyến của khí lí tưởng (không phải ba đẳng quá trình).",
   [("Nếu áp suất tỉ lệ thuận với thể tích (p = aV) thì thể tích tỉ lệ với căn bậc hai của nhiệt độ "
     "tuyệt đối.", True,
     "Đúng. Thay p = aV vào pV = nRT: aV² = nRT ⟹ V ∝ √T."),
    ("Với quá trình p = aV, khi nung khí từ 300 K lên 432 K thì thể tích tăng 1,2 lần.", True,
     "Đúng. V₂/V₁ = √(432/300) = √1,44 = 1,2."),
    ("Nếu áp suất tỉ lệ nghịch với bình phương thể tích (p = a/V²) thì khi thể tích tăng 2 lần, nhiệt độ "
     "tuyệt đối giảm 2 lần.", True,
     "Đúng. T ∝ pV = a/V ⟹ T tỉ lệ nghịch với V."),
    ("Trên giản đồ (p, T), một đoạn thẳng cắt trục p tại giá trị dương biểu diễn quá trình đẳng tích.", False,
     "Sai. Chỉ đường thẳng ĐI QUA GỐC TOẠ ĐỘ mới là đẳng tích. Với p = p₀ + bT (p₀ > 0), ta có "
     "V = nR/(p₀/T + b) tăng liên tục khi T tăng, tức thể tích thay đổi.")],
   "Quá trình phi tuyến – đọc đồ thị", RK),

ds("Một cột khí bị giam trong ống một đầu kín bởi cột thuỷ ngân dài h. Áp suất khí quyển là 75 cmHg, "
   "nhiệt độ không đổi.",
   [("Khi dựng ống thẳng đứng miệng hướng lên, áp suất khí bị giam là 75 + h (cmHg).", True,
     "Đúng. Khí ở đáy phải đỡ cả khí quyển lẫn trọng lượng cột thuỷ ngân phía trên."),
    ("Nếu khi dựng thẳng đứng (miệng lên) chiều dài cột khí giảm 20% so với khi nằm ngang thì h = 18,75 cm.", True,
     "Đúng. 75ℓ = (75 + h)·0,80ℓ ⟹ 75 = 60 + 0,80h ⟹ h = 18,75 cm."),
    ("Nếu khi dựng thẳng đứng (miệng lên) chiều dài cột khí giảm 50% thì h = 75 cm.", True,
     "Đúng. 75ℓ = (75 + h)·0,50ℓ ⟹ 150 = 75 + h ⟹ h = 75 cm — cột thuỷ ngân dài bằng đúng áp suất khí "
     "quyển tính theo cmHg."),
    ("Khi lật ống cho miệng hướng xuống, chiều dài cột khí cũng nhỏ hơn khi ống nằm ngang.", False,
     "Sai. Lúc đó khí chỉ còn chịu áp suất 75 − h (cmHg), nhỏ hơn khi nằm ngang, nên theo định luật "
     "Boyle cột khí phải DÀI ra chứ không ngắn lại. Chỉ khi miệng ống hướng LÊN cột khí mới ngắn đi.")],
   "Cột khí bị giam – bài toán ngược", RK, fig="k_sd_ong_khi",
   cap="Ống chứa cột khí bị giam"),
],
P3=[
sa("Xilanh nằm ngang dài 100 cm, pit-tông ở giữa, hai ngăn cùng khí ở 300 K và 10⁵ Pa. Nung ngăn trái lên "
   "400 K, ngăn phải lên 350 K. Pit-tông dịch chuyển bao nhiêu cm (làm tròn đến chữ số thập phân thứ nhất)?",
   "3,3",
   "V_trái/V_phải = 400/350 = 8/7 ⟹ (50 + x)/(50 − x) = 8/7 ⟹ 15x = 50 ⟹ x ≈ 3,3 cm.",
   "Xilanh hai ngăn", RK),

sa("Với xilanh ở câu trên, áp suất chung ở trạng thái cuối bằng bao nhiêu (đơn vị 10⁵ Pa, làm tròn đến "
   "chữ số thập phân thứ hai)?",
   "1,25",
   "Xét ngăn phải: 10⁵ · 50/300 = p′ · 46,67/350 ⟹ p′ = 10⁵ · 50 · 350/(300 · 46,67) ≈ 1,25·10⁵ Pa.",
   "Xilanh hai ngăn", RK),

sa("Bình kín thể tích không đổi chứa khí ở 300 K, áp suất 1,5·10⁵ Pa; van xả mở khi áp suất đạt "
   "3,0·10⁵ Pa. Đun tới 900 K. Phần trăm khối lượng khí đã thoát ra bằng bao nhiêu (làm tròn đến chữ số "
   "thập phân thứ nhất)?",
   "33,3",
   "m ∝ p/T ⟹ m_cuối/m_đầu = (3,0/900)/(1,5/300) = 0,3333/0,5 = 0,6667 ⟹ thoát ra 33,3%.",
   "Van xả – lượng khí thay đổi", RK),

sa("Nung nóng đẳng áp một lượng khí lí tưởng đang ở 27 °C cho tới khi khối lượng riêng của khí giảm "
   "20 % so với ban đầu. Nhiệt độ của khí khi đó bằng bao nhiêu kelvin?",
   "375",
   "Khối lượng khí không đổi nên khối lượng riêng tỉ lệ nghịch với thể tích:\n"
   "ρ₂ = 0,80·ρ₁ ⟹ V₂ = V₁/0,80 = 1,25·V₁.\n"
   "Đẳng áp: T₂ = T₁ · V₂/V₁ = 300 · 1,25 = 375 K.",
   "Đẳng áp – khối lượng riêng của khí", K),

sa("Một cột khí bị giam trong ống một đầu kín bởi cột thuỷ ngân dài h. Khi dựng ống thẳng đứng miệng "
   "hướng lên, chiều dài cột khí giảm 20% so với khi ống nằm ngang. Áp suất khí quyển 75 cmHg. Giá trị "
   "của h bằng bao nhiêu cm (làm tròn đến chữ số thập phân thứ hai)?",
   "18,75",
   "75ℓ₁ = (75 + h)·0,80ℓ₁ ⟹ 75 = 60 + 0,80h ⟹ h = 15/0,80 = 18,75 cm.",
   "Cột khí bị giam – bài toán ngược", RK, fig="k_sd_ong_khi", cap="Ống chứa cột khí bị giam"),

sa("Một quả bóng đàn hồi có áp suất khí bên trong luôn tỉ lệ thuận với thể tích (p = aV). Nung bóng từ "
   "300 K lên 432 K thì thể tích tăng bao nhiêu lần (làm tròn đến chữ số thập phân thứ nhất)?",
   "1,2", "aV² = nRT ⟹ V ∝ √T ⟹ V₂/V₁ = √(432/300) = √1,44 = 1,2 lần.",
   "Quá trình phi tuyến", RK),
])


NHOM = dict(
    ten_nhom="LỚP 12 – CHƯƠNG 2: KHÍ LÍ TƯỞNG",
    mo_ta="Bộ 10 đề luyện tập, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó / thử thách)",
    pham_vi=(
        "Bài 8. Mô hình động học phân tử chất khí  •  Bài 9. Định luật Boyle\n"
        "Bài 10. Định luật Charles  •  Bài 11. Phương trình trạng thái của khí lí tưởng\n"
        "Bài 12. Áp suất khí theo mô hình động học phân tử. Quan hệ giữa động năng phân tử và nhiệt độ\n"
        "Bài 13. Bài tập về khí lí tưởng\n"
        "Hằng số dùng thống nhất: R = 8,31 J/(mol·K); k = 1,38·10⁻²³ J/K; N_A = 6,02·10²³ mol⁻¹; "
        "g = 10 m/s²; áp suất khí quyển 10⁵ Pa (hoặc 75 cmHg)."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
