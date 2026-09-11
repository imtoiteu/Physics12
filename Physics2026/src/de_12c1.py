# -*- coding: utf-8 -*-
"""LỚP 12 – CHƯƠNG 1: VẬT LÍ NHIỆT.  10 đề, độ khó tăng dần.

Hằng số dùng thống nhất trong cả bộ:
  c_nước = 4200, c_nước đá = 2100, c_nhôm = 880, c_đồng = 380, c_sắt = 460,
  c_chì = 130 J/(kg·K);  λ_nước đá = 3,4·10⁵ J/kg;  L_nước = 2,26·10⁶ J/kg;
  λ_chì = 0,25·10⁵ J/kg;  g = 10 m/s².
"""

from qbase import mc, ds, sa, D, TB, K, RK


# =====================================================================
DE1 = dict(
ma="12C1-Đ01", ten="ĐỀ SỐ 1", muc="Dễ",
trongtam="Nhận biết cấu trúc chất, nội năng, thang nhiệt độ và ba công thức nhiệt cơ bản",
P1=[
mc("Trong chất rắn kết tinh, các hạt cấu tạo nên chất được sắp xếp",
   ["hoàn toàn hỗn độn, chuyển động tự do về mọi phía.",
    "theo một trật tự hình học xác định và chỉ dao động quanh vị trí cân bằng cố định.",
    "theo trật tự gần, vị trí cân bằng của mỗi hạt luôn thay đổi.",
    "sát nhau và đứng yên hoàn toàn."],
   "B",
   "Chất rắn kết tinh có cấu trúc mạng tinh thể: các hạt sắp xếp trật tự xa và dao động nhiệt quanh vị "
   "trí cân bằng cố định. “Trật tự gần, vị trí cân bằng thay đổi” là đặc điểm của chất lỏng.",
   "Cấu trúc của chất", D, fig="n_sd_cautruc", cap="Mô hình sắp xếp hạt ở ba thể"),

mc("Tính chất nào sau đây là của chất khí?",
   ["Có thể tích riêng và hình dạng riêng xác định.",
    "Có thể tích riêng xác định nhưng không có hình dạng riêng.",
    "Không có thể tích riêng và không có hình dạng riêng, luôn chiếm toàn bộ bình chứa.",
    "Có hình dạng riêng nhưng không có thể tích riêng."],
   "C",
   "Ở thể khí, khoảng cách giữa các phân tử rất lớn so với kích thước phân tử, lực tương tác rất yếu nên "
   "chất khí luôn chiếm toàn bộ thể tích bình chứa.",
   "Đặc điểm ba thể của chất", D),

mc("Sự nóng chảy là quá trình chuyển thể",
   ["từ thể rắn sang thể lỏng.", "từ thể lỏng sang thể rắn.",
    "từ thể lỏng sang thể khí.", "từ thể rắn sang thể khí."],
   "A",
   "Nóng chảy: rắn → lỏng (thu nhiệt). Chiều ngược lại là đông đặc.",
   "Sự chuyển thể", D, fig="n_sd_chuyenthe", cap="Sơ đồ các quá trình chuyển thể"),

mc("Đơn vị của nhiệt dung riêng trong hệ SI là",
   ["J/kg.", "J/(kg·K).", "J·kg/K.", "J/K."],
   "B",
   "Từ Q = mcΔT suy ra c = Q/(mΔT), đơn vị là J/(kg·K).",
   "Nhiệt dung riêng", D),

mc("Nhiệt lượng cần cung cấp để làm nóng một vật khối lượng m, nhiệt dung riêng c, từ nhiệt độ t₁ lên t₂ là",
   ["Q = mc(t₂ − t₁).", "Q = mc(t₂ + t₁).", "Q = m(t₂ − t₁)/c.", "Q = c(t₂ − t₁)/m."],
   "A",
   "Công thức nhiệt lượng: Q = m·c·Δt với Δt = t₂ − t₁.",
   "Nhiệt dung riêng", D),

mc("Nội năng của một vật là",
   ["tổng động năng của chuyển động có hướng của vật.",
    "tổng động năng chuyển động nhiệt và thế năng tương tác của các phân tử cấu tạo nên vật.",
    "tổng cơ năng của vật trong trọng trường.",
    "nhiệt lượng mà vật đã nhận được."],
   "B",
   "Nội năng gồm động năng chuyển động nhiệt và thế năng tương tác giữa các phân tử. Nội năng khác nhiệt "
   "lượng: nhiệt lượng là phần nội năng được trao đổi trong quá trình truyền nhiệt.",
   "Nội năng", D),

mc("Định luật I của nhiệt động lực học được viết là",
   ["ΔU = A + Q.", "ΔU = A − Q.", "ΔU = Q − A.", "ΔU = A·Q."],
   "A",
   "ΔU = A + Q, trong đó A là công và Q là nhiệt lượng mà hệ NHẬN được.",
   "Định luật I nhiệt động lực học", D, fig="n_sd_dl1",
   cap="Quy ước dấu của công và nhiệt lượng"),

mc("Theo quy ước, khi hệ nhận nhiệt lượng từ bên ngoài thì",
   ["Q > 0.", "Q < 0.", "Q = 0.", "A < 0."],
   "A",
   "Quy ước: hệ nhận nhiệt thì Q > 0, hệ toả nhiệt thì Q < 0; hệ nhận công thì A > 0, hệ sinh công thì A < 0.",
   "Định luật I nhiệt động lực học", D),

mc("Nhiệt độ 27 °C ứng với nhiệt độ tuyệt đối là",
   ["246 K.", "270 K.", "300 K.", "327 K."],
   "C",
   "T (K) = t (°C) + 273 = 27 + 273 = 300 K.",
   "Thang nhiệt độ", D, fig="n_sd_thang", cap="Đối chiếu thang Celsius và thang Kelvin"),

mc("Nhiệt độ 0 K (độ không tuyệt đối) tương ứng với",
   ["0 °C.", "−100 °C.", "−273 °C.", "100 °C."],
   "C",
   "0 K = −273 °C. Đây là giới hạn dưới của nhiệt độ, ở đó chuyển động nhiệt của các phân tử coi như "
   "dừng lại.",
   "Thang nhiệt độ", D),

mc("Đơn vị của nhiệt nóng chảy riêng là",
   ["J.", "J/kg.", "J/(kg·K).", "kg/J."],
   "B",
   "Từ Q = λm suy ra λ = Q/m, đơn vị J/kg. Chú ý phân biệt với nhiệt dung riêng có đơn vị J/(kg·K).",
   "Nhiệt nóng chảy riêng", D),

mc("Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn khối lượng m của một chất rắn ở đúng nhiệt độ "
   "nóng chảy là",
   ["Q = mcΔT.", "Q = λm.", "Q = Lm.", "Q = λ/m."],
   "B",
   "Q = λ·m với λ là nhiệt nóng chảy riêng. Q = L·m là nhiệt lượng hoá hơi; Q = mcΔT dùng khi nhiệt độ "
   "thay đổi.",
   "Nhiệt nóng chảy riêng", D),

mc("Nhiệt hoá hơi riêng của nước rất lớn (2,26·10⁶ J/kg). Điều này có nghĩa là",
   ["cần 2,26·10⁶ J để đun 1 kg nước tăng thêm 1 °C.",
    "cần 2,26·10⁶ J để làm 1 kg nước ở nhiệt độ sôi hoá hơi hoàn toàn.",
    "cần 2,26·10⁶ J để làm nóng chảy 1 kg nước đá.",
    "nước sôi ở nhiệt độ 2,26·10⁶ °C."],
   "B",
   "Nhiệt hoá hơi riêng L là nhiệt lượng cần để làm cho 1 kg chất lỏng ở nhiệt độ sôi hoá hơi hoàn toàn.",
   "Nhiệt hoá hơi riêng", D),

mc("Sự bay hơi của chất lỏng",
   ["chỉ xảy ra ở nhiệt độ sôi.",
    "xảy ra ở mọi nhiệt độ và chỉ diễn ra trên mặt thoáng.",
    "chỉ xảy ra khi chất lỏng được đun nóng.",
    "xảy ra đồng thời trong lòng và trên mặt thoáng ở mọi nhiệt độ."],
   "B",
   "Bay hơi xảy ra ở mọi nhiệt độ và chỉ trên mặt thoáng. Sự sôi mới là hoá hơi xảy ra đồng thời cả trên "
   "mặt thoáng lẫn trong lòng chất lỏng, và chỉ ở nhiệt độ sôi.",
   "Bay hơi và sôi", D),

mc("Cần cung cấp nhiệt lượng bằng bao nhiêu để đun 2,0 kg nước từ 25 °C lên 55 °C? "
   "Cho c = 4200 J/(kg·K).",
   ["126 kJ.", "252 kJ.", "420 kJ.", "504 kJ."],
   "B",
   "Q = mcΔt = 2,0 · 4200 · (55 − 25) = 2,0 · 4200 · 30 = 252 000 J = 252 kJ.",
   "Nhiệt dung riêng", D),

mc("Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn 0,50 kg nước đá đang ở 0 °C là bao nhiêu? "
   "Cho λ = 3,4·10⁵ J/kg.",
   ["85 kJ.", "170 kJ.", "340 kJ.", "680 kJ."],
   "B",
   "Q = λm = 3,4·10⁵ · 0,50 = 1,7·10⁵ J = 170 kJ. Nước đá đã ở đúng 0 °C nên không cần thêm giai đoạn "
   "làm nóng.",
   "Nhiệt nóng chảy riêng", D),

mc("Hình vẽ là đồ thị nhiệt độ theo thời gian khi nung nóng liên tục 0,50 kg nước đá bằng một thiết bị có "
   "công suất không đổi. Đoạn nằm ngang của đồ thị ứng với quá trình",
   ["nước đá nóng lên.", "nước đá đang nóng chảy.", "nước nóng lên.", "nước đang sôi."],
   "B",
   "Trong đoạn nằm ngang, nhiệt độ giữ nguyên 0 °C trong khi vẫn được cung cấp nhiệt: toàn bộ nhiệt lượng "
   "dùng để phá vỡ mạng tinh thể, tức là nước đá đang nóng chảy.",
   "Đọc đồ thị chuyển thể", D, fig="n_dt_nuocda",
   cap="Nhiệt độ của 0,50 kg nước đá theo thời gian nung"),

mc("Hai vật A và B tiếp xúc nhau, nhiệt độ của A là 60 °C, của B là 330 K. Khi đó",
   ["nhiệt truyền từ A sang B.", "nhiệt truyền từ B sang A.",
    "không có sự truyền nhiệt vì hai vật đã cân bằng nhiệt.",
    "chưa đủ dữ kiện để kết luận."],
   "A",
   "Phải đưa về cùng thang đo: t_B = 330 − 273 = 57 °C < 60 °C. Nhiệt luôn tự truyền từ vật có nhiệt độ "
   "cao hơn sang vật có nhiệt độ thấp hơn, tức là từ A sang B.",
   "Thang nhiệt độ – truyền nhiệt", TB),
],
P2=[
ds("Xét cấu trúc của chất và các quá trình chuyển thể.",
   [("Ở thể lỏng, các phân tử sắp xếp theo trật tự gần và có thể trượt lên nhau, vì vậy chất lỏng có thể "
     "tích riêng xác định nhưng không có hình dạng riêng.", True,
     "Đúng. Lực liên kết ở thể lỏng đủ mạnh để giữ các phân tử gần nhau (thể tích xác định) nhưng không đủ "
     "để cố định vị trí của chúng (không có hình dạng riêng)."),
    ("Quá trình đông đặc là quá trình toả nhiệt.", True,
     "Đúng. Đông đặc là chiều ngược của nóng chảy: các phân tử sắp xếp lại thành mạng tinh thể và giải "
     "phóng năng lượng ra môi trường."),
    ("Trong suốt quá trình nóng chảy của một chất rắn kết tinh, nhiệt độ của chất không đổi.", True,
     "Đúng. Chất rắn kết tinh có nhiệt độ nóng chảy xác định; trong khi đang nóng chảy, nhiệt lượng nhận "
     "vào dùng để phá vỡ mạng tinh thể chứ không làm tăng nhiệt độ."),
    ("Sự thăng hoa là quá trình chuyển từ thể khí trực tiếp sang thể rắn.", False,
     "Sai. Thăng hoa là chuyển trực tiếp từ thể RẮN sang thể KHÍ (ví dụ băng phiến, nước đá khô). "
     "Chiều ngược lại (khí → rắn) gọi là ngưng kết.")],
   "Cấu trúc của chất – sự chuyển thể", D,
   fig="n_sd_chuyenthe", cap="Sơ đồ các quá trình chuyển thể"),

ds("Xét nội năng và các cách làm biến đổi nội năng của một vật.",
   [("Nội năng của một vật có thể thay đổi bằng cách thực hiện công hoặc bằng cách truyền nhiệt.", True,
     "Đúng. Đó là hai cách làm biến đổi nội năng: thực hiện công (cọ xát, nén khí…) và truyền nhiệt "
     "(cho tiếp xúc với vật nóng hơn…)."),
    ("Khi cọ xát một miếng kim loại lên mặt bàn, nội năng của miếng kim loại tăng lên.", True,
     "Đúng. Công của lực ma sát chuyển hoá thành nội năng làm miếng kim loại nóng lên."),
    ("Nếu hệ nhận nhiệt lượng Q = 500 J và đồng thời nhận công A = 300 J thì nội năng của hệ tăng 800 J.", True,
     "Đúng. ΔU = A + Q = 300 + 500 = 800 J > 0, nội năng tăng."),
    ("Nhiệt lượng là một dạng năng lượng được chứa sẵn trong vật.", False,
     "Sai. Vật chứa NỘI NĂNG chứ không “chứa nhiệt lượng”. Nhiệt lượng là phần nội năng được TRAO ĐỔI "
     "trong quá trình truyền nhiệt, chỉ có nghĩa khi nói về một quá trình.")],
   "Nội năng – định luật I nhiệt động lực học", TB),

ds("Đun nóng 1,5 kg nước từ 20 °C bằng một ấm điện. Cho nhiệt dung riêng của nước "
   "c = 4200 J/(kg·K) và bỏ qua mọi hao phí.",
   [("Nhiệt lượng cần cung cấp để nước đạt 100 °C là 504 kJ.", True,
     "Đúng. Q = mcΔt = 1,5 · 4200 · (100 − 20) = 1,5 · 4200 · 80 = 504 000 J = 504 kJ."),
    ("Nếu chỉ đun 0,75 kg nước cũng từ 20 °C lên 100 °C thì nhiệt lượng cần cung cấp giảm một nửa.", True,
     "Đúng. Với c và Δt không đổi, Q tỉ lệ thuận với khối lượng m nên khối lượng giảm một nửa thì Q "
     "giảm một nửa (252 kJ)."),
    ("Muốn tính nhiệt lượng trên, có thể thay Δt = 80 K bằng Δt = 80 °C mà kết quả không đổi.", True,
     "Đúng. Độ CHÊNH LỆCH nhiệt độ tính theo thang Celsius và thang Kelvin là như nhau, vì hai thang chỉ "
     "khác nhau ở gốc: ΔT (K) = Δt (°C)."),
    ("Nếu tiếp tục cung cấp nhiệt sau khi nước đã sôi thì nhiệt độ của nước tiếp tục tăng đều.", False,
     "Sai. Khi nước đã sôi, nhiệt độ giữ nguyên 100 °C (ở áp suất chuẩn); nhiệt lượng cung cấp thêm dùng "
     "để hoá hơi nước chứ không làm tăng nhiệt độ.")],
   "Nhiệt dung riêng – sự sôi", TB),

ds("Hình vẽ là đồ thị nhiệt độ theo thời gian khi nung 0,50 kg nước đá ban đầu ở −20 °C bằng thiết bị có "
   "công suất không đổi P = 420 W (bỏ qua hao phí).",
   [("Trong 50 giây đầu, nước đá nóng lên từ −20 °C đến 0 °C.", True,
     "Đúng. Đồ thị đi từ −20 °C lên 0 °C trong khoảng thời gian từ 0 đến 50 s."),
    ("Quá trình nóng chảy của nước đá kéo dài 400 giây.", True,
     "Đúng. Đoạn nằm ngang ở 0 °C kéo dài từ t = 50 s đến t = 450 s, tức là 400 s."),
    ("Nhiệt lượng cần để làm nóng chảy hoàn toàn khối nước đá là 168 kJ.", True,
     "Đúng. Q = P·t = 420 · 400 = 168 000 J = 168 kJ (ứng với λ = Q/m = 168 000/0,50 = 3,36·10⁵ J/kg, "
     "phù hợp với giá trị thực của nước đá)."),
    ("Ở thời điểm t = 300 s, trong bình chỉ còn nước ở thể lỏng.", False,
     "Sai. Thời điểm t = 300 s nằm trong đoạn nằm ngang (từ 50 s đến 450 s), tức là nước đá đang nóng "
     "chảy dở: trong bình đồng thời có cả nước đá và nước.")],
   "Đọc đồ thị nung nóng – chuyển thể", TB,
   fig="n_dt_nuocda", cap="Nhiệt độ của 0,50 kg nước đá theo thời gian nung"),
],
P3=[
sa("Nhiệt độ cơ thể người bình thường là 37 °C. Nhiệt độ này ứng với bao nhiêu kelvin?",
   "310", "T = t + 273 = 37 + 273 = 310 K.", "Thang nhiệt độ", D),

sa("Cần cung cấp cho 0,50 kg nước một nhiệt lượng bằng bao nhiêu kilôjun để nhiệt độ của nó tăng từ "
   "20 °C lên 80 °C? Cho c = 4200 J/(kg·K).",
   "126", "Q = mcΔt = 0,50 · 4200 · 60 = 126 000 J = 126 kJ.", "Nhiệt dung riêng", D),

sa("Một vật bằng đồng khối lượng 0,50 kg đang ở 20 °C nhận được nhiệt lượng 5700 J. Nhiệt độ của vật "
   "sau đó bằng bao nhiêu độ C? Cho c_đồng = 380 J/(kg·K).",
   "50",
   "Δt = Q/(mc) = 5700/(0,50 · 380) = 5700/190 = 30 °C ⟹ nhiệt độ cuối là 20 + 30 = 50 °C.",
   "Nhiệt dung riêng", D),

sa("Nhiệt lượng cần cung cấp để làm hoá hơi hoàn toàn 100 g nước đang ở 100 °C bằng bao nhiêu kilôjun? "
   "Cho L = 2,26·10⁶ J/kg.",
   "226", "Q = Lm = 2,26·10⁶ · 0,100 = 226 000 J = 226 kJ.", "Nhiệt hoá hơi riêng", D),

sa("Đổ 100 g nước ở 90 °C vào 200 g nước ở 30 °C trong một bình cách nhiệt (bỏ qua nhiệt dung của bình). "
   "Nhiệt độ của nước khi cân bằng nhiệt bằng bao nhiêu độ C?",
   "50",
   "Phương trình cân bằng nhiệt: m₁c(90 − t) = m₂c(t − 30) ⟹ 100(90 − t) = 200(t − 30)\n"
   "⟹ 9000 − 100t = 200t − 6000 ⟹ 300t = 15 000 ⟹ t = 50 °C.\n"
   "(Nhiệt dung riêng c giống nhau nên bị khử; có thể tính nhanh bằng trung bình có trọng số.)",
   "Cân bằng nhiệt", TB),

sa("Một khối khí nhận nhiệt lượng 200 J, đồng thời nhận công 150 J do bị nén. Độ biến thiên nội năng của "
   "khối khí bằng bao nhiêu jun?",
   "350",
   "ΔU = A + Q. Hệ nhận nhiệt nên Q = +200 J; hệ nhận công nên A = +150 J.\n"
   "ΔU = 150 + 200 = 350 J (nội năng tăng).",
   "Định luật I nhiệt động lực học", D),
])


# =====================================================================
DE2 = dict(
ma="12C1-Đ02", ten="ĐỀ SỐ 2", muc="Dễ",
trongtam="Chuyển động nhiệt, nhiệt kế, cân bằng nhiệt và ba công thức nhiệt lượng",
P1=[
mc("Chuyển động Brown của các hạt phấn hoa trong nước là bằng chứng trực tiếp cho thấy",
   ["nước có khối lượng riêng lớn.",
    "các phân tử nước chuyển động hỗn loạn không ngừng.",
    "nước có nhiệt dung riêng lớn.",
    "giữa các phân tử nước có lực hút."],
   "B",
   "Các hạt phấn hoa bị các phân tử nước va chạm từ mọi phía một cách không đều nhau nên chuyển động "
   "zic-zăc. Đây là bằng chứng thực nghiệm cho chuyển động nhiệt hỗn loạn của phân tử.",
   "Mô hình động học phân tử", D),

mc("Khi khoảng cách giữa hai phân tử nhỏ hơn khoảng cách cân bằng r₀ thì lực tương tác giữa chúng là",
   ["lực hút.", "lực đẩy.", "bằng không.", "lúc hút lúc đẩy."],
   "B",
   "Khi r < r₀ lực đẩy chiếm ưu thế (đẩy hai phân tử ra xa), khi r > r₀ lực hút chiếm ưu thế. Tại r = r₀ "
   "lực tương tác tổng hợp bằng không.",
   "Lực tương tác phân tử", D),

mc("Nhiệt kế thuỷ ngân hoạt động dựa trên hiện tượng",
   ["dãn nở vì nhiệt của chất lỏng.", "dẫn nhiệt của kim loại.",
    "bay hơi của chất lỏng.", "thay đổi điện trở theo nhiệt độ."],
   "A",
   "Thuỷ ngân trong bầu nhiệt kế dãn nở khi nhiệt độ tăng, dâng lên trong ống mao dẫn; độ dâng tỉ lệ với "
   "độ tăng nhiệt độ.",
   "Nhiệt kế", D),

mc("Đơn vị của nhiệt hoá hơi riêng là",
   ["J/(kg·K).", "J/kg.", "J·K/kg.", "W/kg."],
   "B",
   "Từ Q = Lm suy ra L = Q/m, đơn vị J/kg — giống đơn vị của nhiệt nóng chảy riêng.",
   "Nhiệt hoá hơi riêng", D),

mc("Trong hệ SI, đơn vị của nhiệt độ là",
   ["độ Celsius (°C).", "kelvin (K).", "độ Fahrenheit (°F).", "jun (J)."],
   "B",
   "Kelvin là đơn vị nhiệt độ trong hệ SI. Độ Celsius vẫn được dùng phổ biến nhưng không phải đơn vị SI.",
   "Thang nhiệt độ", D),

mc("Nhiệt độ nước đang sôi ở áp suất tiêu chuẩn là 100 °C, ứng với",
   ["173 K.", "273 K.", "373 K.", "473 K."],
   "C",
   "T = 100 + 273 = 373 K.",
   "Thang nhiệt độ", D),

mc("Hai vật được coi là đã cân bằng nhiệt với nhau khi",
   ["chúng có cùng nội năng.", "chúng có cùng khối lượng.",
    "chúng có cùng nhiệt độ.", "chúng có cùng nhiệt dung riêng."],
   "C",
   "Dấu hiệu của cân bằng nhiệt là hai vật có cùng nhiệt độ, khi đó không còn sự truyền nhiệt giữa chúng. "
   "Nội năng của hai vật vẫn có thể rất khác nhau.",
   "Cân bằng nhiệt", D),

mc("Một vật toả nhiệt ra môi trường. Theo quy ước dấu của định luật I nhiệt động lực học thì",
   ["Q > 0.", "Q < 0.", "A > 0.", "ΔU > 0."],
   "B",
   "Hệ toả nhiệt tức là nhiệt lượng hệ nhận được mang giá trị âm: Q < 0.",
   "Định luật I nhiệt động lực học", D),

mc("Khi dùng bơm tay nén nhanh không khí trong xilanh, thân bơm nóng lên. Nguyên nhân chính là",
   ["không khí truyền nhiệt cho thân bơm từ bên ngoài.",
    "ta đã thực hiện công lên khối khí, làm nội năng của khối khí tăng.",
    "khối lượng của khối khí tăng lên.",
    "khối khí đã hoá lỏng."],
   "B",
   "Nén nhanh nên hầu như không kịp trao đổi nhiệt (Q ≈ 0). Ta thực hiện công lên khí (A > 0) nên "
   "ΔU = A + Q > 0: nội năng và nhiệt độ khối khí tăng, sau đó truyền nhiệt làm nóng thân bơm.",
   "Định luật I – thực hiện công", TB),

mc("Nước có nhiệt dung riêng rất lớn (4200 J/(kg·K)). Vì vậy nước thường được dùng làm",
   ["chất cách nhiệt trong xây dựng.",
    "chất tải nhiệt trong hệ thống làm mát động cơ.",
    "chất bôi trơn cho máy móc.",
    "vật liệu chế tạo lò nung."],
   "B",
   "Nhiệt dung riêng lớn nghĩa là cùng một khối lượng, nước hấp thụ được nhiều nhiệt mà nhiệt độ tăng ít, "
   "rất thích hợp để mang nhiệt đi khỏi động cơ.",
   "Nhiệt dung riêng – ứng dụng", D),

mc("Cung cấp nhiệt lượng 84 kJ cho một lượng nước thì nhiệt độ của nó tăng thêm 20 °C. Khối lượng nước là "
   "(cho c = 4200 J/(kg·K))",
   ["0,5 kg.", "1,0 kg.", "1,5 kg.", "2,0 kg."],
   "B",
   "m = Q/(cΔt) = 84 000/(4200 · 20) = 84 000/84 000 = 1,0 kg.",
   "Nhiệt dung riêng", D),

mc("Để làm nóng chảy hoàn toàn 0,40 kg một chất rắn ở đúng nhiệt độ nóng chảy cần 136 kJ. Nhiệt nóng chảy "
   "riêng của chất đó là",
   ["1,7·10⁵ J/kg.", "2,7·10⁵ J/kg.", "3,4·10⁵ J/kg.", "5,4·10⁵ J/kg."],
   "C",
   "λ = Q/m = 136 000/0,40 = 3,4·10⁵ J/kg (đây chính là giá trị của nước đá).",
   "Nhiệt nóng chảy riêng", D),

mc("Cần 1130 kJ để làm hoá hơi hoàn toàn một lượng nước đang ở 100 °C. Khối lượng nước đó là "
   "(cho L = 2,26·10⁶ J/kg)",
   ["0,25 kg.", "0,50 kg.", "1,00 kg.", "2,00 kg."],
   "B",
   "m = Q/L = 1 130 000/2,26·10⁶ = 0,50 kg.",
   "Nhiệt hoá hơi riêng", D),

mc("Hình vẽ là đồ thị nhiệt độ theo thời gian của một chất lỏng để nguội trong không khí. Nhiệt độ đông "
   "đặc của chất đó là",
   ["60 °C.", "70 °C.", "80 °C.", "90 °C."],
   "C",
   "Đoạn nằm ngang của đường nguội lạnh ứng với quá trình đông đặc; đọc trên trục tung ⟹ nhiệt độ đông "
   "đặc = 80 °C.",
   "Đọc đồ thị đông đặc", D, fig="n_dt_dongdac",
   cap="Nhiệt độ của một chất lỏng để nguội theo thời gian"),

mc("Vẫn với đồ thị ở câu trên, thời gian đông đặc của chất lỏng kéo dài",
   ["120 phút.", "180 phút.", "240 phút.", "360 phút."],
   "C",
   "Đoạn nằm ngang kéo dài từ phút thứ 120 đến phút thứ 360, tức là 360 − 120 = 240 phút.",
   "Đọc đồ thị đông đặc", D, fig="n_dt_dongdac",
   cap="Nhiệt độ của một chất lỏng để nguội theo thời gian"),

mc("Nhiệt lượng kế là dụng cụ dùng để",
   ["đo nhiệt độ của vật.",
    "tạo ra nhiệt lượng.",
    "hạn chế trao đổi nhiệt với môi trường khi khảo sát các quá trình nhiệt.",
    "đo công suất của nguồn nhiệt."],
   "C",
   "Nhiệt lượng kế có vỏ cách nhiệt, giúp coi hệ bên trong là cô lập về nhiệt để áp dụng được phương "
   "trình cân bằng nhiệt. Dụng cụ đo nhiệt độ là nhiệt kế.",
   "Nhiệt lượng kế", D, fig="n_sd_nhietluongke", cap="Cấu tạo nhiệt lượng kế"),

mc("Thả một miếng đồng khối lượng 0,20 kg ở 100 °C vào 0,50 kg nước ở 20 °C đựng trong bình cách nhiệt "
   "(bỏ qua nhiệt dung của bình). Cho c_đồng = 380 J/(kg·K), c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng "
   "nhiệt gần nhất với giá trị nào sau đây?",
   ["21,4 °C.", "22,8 °C.", "25,6 °C.", "30,2 °C."],
   "B",
   "Phương trình cân bằng nhiệt: 0,20 · 380 · (100 − t) = 0,50 · 4200 · (t − 20)\n"
   "⟹ 76(100 − t) = 2100(t − 20) ⟹ 7600 − 76t = 2100t − 42 000 ⟹ 2176t = 49 600 ⟹ t ≈ 22,8 °C.\n"
   "Nhiệt độ cân bằng rất gần nhiệt độ nước ban đầu vì “nhiệt dung” của nước (2100 J/K) lớn hơn nhiều "
   "so với của miếng đồng (76 J/K).",
   "Cân bằng nhiệt", TB),

mc("Phát biểu nào sau đây về sự bay hơi và sự sôi là ĐÚNG?",
   ["Cả hai đều chỉ xảy ra ở nhiệt độ sôi.",
    "Bay hơi chỉ xảy ra trên mặt thoáng và ở mọi nhiệt độ; sự sôi xảy ra cả trong lòng chất lỏng và chỉ ở "
    "nhiệt độ sôi.",
    "Bay hơi xảy ra trong lòng chất lỏng, sự sôi xảy ra trên mặt thoáng.",
    "Trong khi sôi, nhiệt độ chất lỏng tăng đều."],
   "B",
   "Đây là hai dấu hiệu phân biệt quan trọng nhất: VỊ TRÍ xảy ra (mặt thoáng ↔ cả trong lòng) và ĐIỀU "
   "KIỆN nhiệt độ (mọi nhiệt độ ↔ đúng nhiệt độ sôi). Trong khi sôi, nhiệt độ chất lỏng không đổi.",
   "Bay hơi và sôi", TB),
],
P2=[
ds("Xét nhiệt kế và các thang nhiệt độ đang được sử dụng.",
   [("Trong thang Celsius, 0 °C là nhiệt độ nước đá đang tan và 100 °C là nhiệt độ nước đang sôi ở áp "
     "suất tiêu chuẩn.", True,
     "Đúng. Đó chính là hai mốc dùng để chia thang Celsius."),
    ("Một độ chia trong thang Kelvin có độ lớn bằng một độ chia trong thang Celsius.", True,
     "Đúng. Hai thang chỉ khác nhau ở gốc (0 K = −273 °C), còn khoảng chia thì bằng nhau, do đó "
     "ΔT (K) = Δt (°C)."),
    ("Nhiệt độ −300 °C là một nhiệt độ có thể đạt được trong phòng thí nghiệm hiện đại.", False,
     "Sai. −300 °C thấp hơn độ không tuyệt đối (−273 °C), là nhiệt độ không thể tồn tại."),
    ("Nhiệt kế y tế thường có thang đo từ 35 °C đến 42 °C vì nhiệt độ cơ thể người chỉ thay đổi trong "
     "khoảng hẹp quanh 37 °C.", True,
     "Đúng. Thu hẹp thang đo cho phép chia độ nhỏ hơn (thường 0,1 °C), tăng độ chính xác trong vùng cần đo.")],
   "Nhiệt kế – thang nhiệt độ", D, fig="n_sd_thang", cap="Đối chiếu hai thang nhiệt độ"),

ds("Hình vẽ là đồ thị nhiệt độ theo thời gian của 0,60 kg một chất lỏng để nguội trong không khí.",
   [("Chất lỏng bắt đầu đông đặc ở phút thứ 120.", True,
     "Đúng. Tại t = 120 phút nhiệt độ ngừng giảm và giữ nguyên 80 °C — dấu hiệu bắt đầu đông đặc."),
    ("Trong khoảng từ phút thứ 120 đến phút thứ 360, chất này vừa toả nhiệt ra môi trường vừa giữ nguyên "
     "nhiệt độ.", True,
     "Đúng. Chất vẫn toả nhiệt (vì môi trường lạnh hơn), nhưng nhiệt lượng toả ra là do các phân tử sắp "
     "xếp lại thành mạng tinh thể chứ không làm hạ nhiệt độ."),
    ("Ở phút thứ 200, toàn bộ khối chất đã ở thể rắn.", False,
     "Sai. Phút thứ 200 nằm giữa đoạn nằm ngang nên quá trình đông đặc mới diễn ra một phần: trong bình "
     "đồng thời có cả thể lỏng và thể rắn."),
    ("Sau phút thứ 360, nhiệt độ tiếp tục giảm vì chất rắn vẫn toả nhiệt ra môi trường.", True,
     "Đúng. Khi đã đông đặc hoàn toàn, nhiệt lượng toả ra làm giảm nhiệt độ của khối chất rắn (đồ thị "
     "lại đi xuống).")],
   "Đọc đồ thị đông đặc", TB, fig="n_dt_dongdac",
   cap="Nhiệt độ của chất lỏng để nguội theo thời gian"),

ds("Nhiệt hoá hơi riêng của nước là L = 2,26·10⁶ J/kg, nhiệt nóng chảy riêng của nước đá là "
   "λ = 3,4·10⁵ J/kg, nhiệt dung riêng của nước là 4200 J/(kg·K).",
   [("Để làm hoá hơi hoàn toàn 1 kg nước ở 100 °C cần nhiều năng lượng hơn để làm nóng chảy hoàn toàn "
     "1 kg nước đá ở 0 °C.", True,
     "Đúng. 2,26·10⁶ J so với 3,4·10⁵ J, tức là lớn hơn khoảng 6,6 lần. Hoá hơi phải tách hẳn các phân tử "
     "ra khỏi nhau nên tốn nhiều năng lượng hơn nhiều so với chỉ phá vỡ trật tự tinh thể."),
    ("Nhiệt lượng để đun 1 kg nước từ 0 °C lên 100 °C nhỏ hơn nhiệt lượng để làm hoá hơi hoàn toàn 1 kg "
     "nước ở 100 °C.", True,
     "Đúng. Đun nóng cần 1 · 4200 · 100 = 4,2·10⁵ J, nhỏ hơn nhiều so với 2,26·10⁶ J cần cho hoá hơi."),
    ("Mồ hôi bay hơi làm mát cơ thể vì quá trình bay hơi thu nhiệt từ da.", True,
     "Đúng. Muốn bay hơi, các phân tử nước phải nhận năng lượng; năng lượng đó lấy từ da nên da mất nhiệt "
     "và ta thấy mát."),
    ("Vì nhiệt hoá hơi riêng lớn nên hơi nước ở 100 °C và nước lỏng ở 100 °C gây bỏng như nhau.", False,
     "Sai. Hơi nước ở 100 °C nguy hiểm hơn nhiều: khi ngưng tụ trên da, mỗi kilôgam hơi còn giải phóng "
     "thêm 2,26·10⁶ J, lớn hơn rất nhiều so với nhiệt lượng do nước lỏng nguội đi toả ra.")],
   "Nhiệt hoá hơi riêng – ứng dụng thực tiễn", TB),

ds("Xét các cách làm biến đổi nội năng của một khối khí.",
   [("Nếu khối khí nhận công 400 J và toả ra nhiệt lượng 100 J thì nội năng của nó tăng 300 J.", True,
     "Đúng. A = +400 J, Q = −100 J ⟹ ΔU = 400 − 100 = 300 J > 0."),
    ("Nếu khối khí nhận nhiệt lượng 250 J và sinh công 250 J thì nội năng của nó không đổi.", True,
     "Đúng. Q = +250 J, A = −250 J ⟹ ΔU = −250 + 250 = 0."),
    ("Khi giữ thể tích khối khí không đổi và cung cấp nhiệt lượng Q thì toàn bộ nhiệt lượng đó làm tăng "
     "nội năng của khí.", True,
     "Đúng. Thể tích không đổi nên khí không nhận và không sinh công: A = 0, do đó ΔU = Q."),
    ("Nội năng của một vật chỉ có thể thay đổi bằng cách truyền nhiệt.", False,
     "Sai. Còn cách thứ hai là thực hiện công (cọ xát, nén, khuấy…). Thí nghiệm Joule về chuyển hoá cơ "
     "năng thành nội năng của nước là ví dụ kinh điển.")],
   "Định luật I nhiệt động lực học", TB, fig="n_sd_dl1", cap="Quy ước dấu"),
],
P3=[
sa("Nhiệt độ 373 K ứng với bao nhiêu độ C?",
   "100", "t = T − 273 = 373 − 273 = 100 °C.", "Thang nhiệt độ", D),

sa("Cung cấp nhiệt lượng 105 kJ cho một lượng nước thì nhiệt độ của nó tăng thêm 25 °C. Khối lượng nước "
   "bằng bao nhiêu kilôgam? Cho c = 4200 J/(kg·K).",
   "1", "m = Q/(cΔt) = 105 000/(4200 · 25) = 105 000/105 000 = 1,0 kg.", "Nhiệt dung riêng", D),

sa("Cần 85 kJ để làm nóng chảy hoàn toàn 0,25 kg một chất rắn ở đúng nhiệt độ nóng chảy. Nhiệt nóng chảy "
   "riêng của chất đó bằng bao nhiêu (tính theo đơn vị 10⁵ J/kg)?",
   "3,4", "λ = Q/m = 85 000/0,25 = 340 000 J/kg = 3,4·10⁵ J/kg.", "Nhiệt nóng chảy riêng", D),

sa("Cần cung cấp nhiệt lượng bằng bao nhiêu kilôjun để biến 0,20 kg nước đá ở 0 °C thành nước ở 20 °C? "
   "Cho λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   "84,8",
   "Quá trình gồm hai giai đoạn:\n"
   "• Nóng chảy ở 0 °C: Q₁ = λm = 3,4·10⁵ · 0,20 = 68 000 J.\n"
   "• Đun nước từ 0 °C lên 20 °C: Q₂ = mcΔt = 0,20 · 4200 · 20 = 16 800 J.\n"
   "Q = Q₁ + Q₂ = 84 800 J = 84,8 kJ.",
   "Nhiệt nóng chảy riêng – nhiệt dung riêng", TB),

sa("Một khối khí giãn nở, sinh công 200 J và đồng thời toả ra môi trường nhiệt lượng 300 J. Nội năng của "
   "khối khí GIẢM bao nhiêu jun?",
   "500",
   "ΔU = A + Q với A = −200 J (khí sinh công) và Q = −300 J (khí toả nhiệt).\n"
   "ΔU = −200 − 300 = −500 J, tức nội năng giảm 500 J.",
   "Định luật I nhiệt động lực học", TB),

sa("Một chậu tắm chứa sẵn 4,0 kg nước ở 24 °C. Người ta rót thêm vào 1,0 kg nước vừa đun sôi (100 °C). "
   "Bỏ qua trao đổi nhiệt với chậu và môi trường. Nhiệt độ nước trong chậu bằng bao nhiêu độ C "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "39,2",
   "t = (4,0 · 24 + 1,0 · 100)/(4,0 + 1,0) = (96 + 100)/5 = 39,2 °C.\n"
   "(Cùng một chất nên nhiệt độ cân bằng là trung bình có trọng số theo khối lượng.)",
   "Cân bằng nhiệt – thực tiễn", TB),
])


# =====================================================================
DE3 = dict(
ma="12C1-Đ03", ten="ĐỀ SỐ 3", muc="Dễ → Trung bình",
trongtam="Đọc đồ thị và bảng số liệu để xác định nhiệt dung riêng; bài toán nhiệt hai giai đoạn",
P1=[
mc("Chất khí dễ bị nén hơn chất lỏng rất nhiều, nguyên nhân là do",
   ["phân tử khí có khối lượng nhỏ hơn phân tử chất lỏng.",
    "khoảng cách giữa các phân tử khí rất lớn so với kích thước phân tử.",
    "phân tử khí chuyển động nhanh hơn.",
    "chất khí không có khối lượng riêng."],
   "B",
   "Nén một chất là làm giảm khoảng cách giữa các phân tử. Ở thể khí khoảng cách này rất lớn nên còn "
   "nhiều “chỗ trống” để nén; ở thể lỏng các phân tử đã gần như sát nhau.",
   "Cấu trúc của chất", TB),

mc("Nội năng của một lượng khí lí tưởng xác định",
   ["chỉ phụ thuộc vào thể tích của khí.",
    "chỉ phụ thuộc vào nhiệt độ của khí.",
    "chỉ phụ thuộc vào áp suất của khí.",
    "không phụ thuộc vào trạng thái của khí."],
   "B",
   "Với khí lí tưởng, thế năng tương tác giữa các phân tử được bỏ qua nên nội năng chỉ là tổng động năng "
   "chuyển động nhiệt — đại lượng chỉ phụ thuộc nhiệt độ.",
   "Nội năng của khí lí tưởng", TB),

mc("Cung cấp nhiệt lượng Q cho một khối khí đựng trong bình kín có thể tích không đổi. Khi đó",
   ["ΔU = 0.", "ΔU = Q.", "ΔU = −Q.", "ΔU = 2Q."],
   "B",
   "Thể tích không đổi nên khí không nhận và cũng không sinh công: A = 0. Định luật I cho ΔU = A + Q = Q: "
   "toàn bộ nhiệt lượng làm tăng nội năng.",
   "Định luật I nhiệt động lực học", TB),

mc("Hình vẽ là đồ thị nhiệt lượng cung cấp Q theo độ tăng nhiệt độ ΔT của hai chất lỏng X và Y, mỗi mẫu "
   "đều có khối lượng 0,50 kg. Kết luận nào sau đây đúng?",
   ["Nhiệt dung riêng của X lớn hơn của Y.",
    "Nhiệt dung riêng của Y lớn hơn của X.",
    "Hai chất có nhiệt dung riêng bằng nhau.",
    "Chưa đủ dữ kiện để so sánh."],
   "A",
   "Hệ số góc của đường thẳng Q–ΔT bằng m·c. Hai mẫu cùng khối lượng nên đường nào dốc hơn thì nhiệt dung "
   "riêng lớn hơn. Đường X dốc hơn ⟹ c_X > c_Y.",
   "Đọc đồ thị Q–ΔT", TB, fig="n_dt_QdT",
   cap="Nhiệt lượng cung cấp theo độ tăng nhiệt độ của hai chất lỏng"),

mc("Vẫn với đồ thị ở câu trên, nhiệt dung riêng của chất X bằng",
   ["1200 J/(kg·K).", "2100 J/(kg·K).", "2400 J/(kg·K).", "4200 J/(kg·K)."],
   "D",
   "Hệ số góc của đường X: k = 105 kJ/50 K = 2,1 kJ/K = 2100 J/K.\n"
   "Mà k = m·c ⟹ c = k/m = 2100/0,50 = 4200 J/(kg·K) (chính là nước).",
   "Đọc đồ thị Q–ΔT", TB, fig="n_dt_QdT",
   cap="Nhiệt lượng cung cấp theo độ tăng nhiệt độ của hai chất lỏng"),

mc("Ba mẫu chất lỏng (1), (2), (3) có cùng khối lượng 0,50 kg được đun bằng cùng một thiết bị có công "
   "suất không đổi. Đồ thị nhiệt độ theo thời gian như hình vẽ. Chất nào có nhiệt dung riêng LỚN NHẤT?",
   ["Chất (1).", "Chất (2).", "Chất (3).", "Ba chất có nhiệt dung riêng bằng nhau."],
   "C",
   "Cùng công suất P và cùng khối lượng m thì P = m·c·(ΔT/Δt), suy ra hệ số góc ΔT/Δt = P/(mc) tỉ lệ "
   "NGHỊCH với c. Đường (3) thoải nhất ⟹ nóng lên chậm nhất ⟹ nhiệt dung riêng lớn nhất.",
   "Đọc đồ thị T–t", TB, fig="n_dt_batchat",
   cap="Nhiệt độ của ba mẫu chất lỏng theo thời gian đun"),

mc("Một nhóm học sinh đo nhiệt dung riêng của nước bằng phương pháp điện: dùng điện trở nung có công suất "
   "P = 42 W đặt trong 0,20 kg nước, ghi nhiệt độ theo thời gian và thu được đồ thị bên (hệ số góc của "
   "đường thẳng khớp số liệu là 0,05 K/s). Bỏ qua hao phí. Nhiệt dung riêng của nước đo được là",
   ["2100 J/(kg·K).", "3150 J/(kg·K).", "4200 J/(kg·K).", "8400 J/(kg·K)."],
   "C",
   "Trong thời gian Δt, nhiệt lượng cung cấp P·Δt làm nước tăng ΔT: P·Δt = m·c·ΔT.\n"
   "⟹ c = P/(m · ΔT/Δt) = 42/(0,20 · 0,05) = 42/0,01 = 4200 J/(kg·K).",
   "Thí nghiệm đo nhiệt dung riêng", K, fig="n_dt_tn_dunnuoc",
   cap="Số liệu thực nghiệm: nhiệt độ nước theo thời gian đun"),

mc("Hai vật cùng khối lượng, làm bằng đồng (c = 380 J/(kg·K)) và nhôm (c = 880 J/(kg·K)), nhận cùng một "
   "nhiệt lượng. So sánh độ tăng nhiệt độ của chúng:",
   ["Vật bằng đồng tăng nhiệt độ nhiều hơn.",
    "Vật bằng nhôm tăng nhiệt độ nhiều hơn.",
    "Hai vật tăng nhiệt độ như nhau.",
    "Chưa đủ dữ kiện để so sánh."],
   "A",
   "Từ ΔT = Q/(mc), với Q và m như nhau thì ΔT tỉ lệ nghịch với c. Đồng có c nhỏ hơn nên nóng lên nhiều "
   "hơn (khoảng 880/380 ≈ 2,3 lần).",
   "Nhiệt dung riêng", TB),

mc("Cần cung cấp nhiệt lượng bằng bao nhiêu để biến 0,50 kg nước đá ở −10 °C thành nước ở 0 °C? "
   "Cho c_đá = 2100 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   ["170,0 kJ.", "180,5 kJ.", "190,0 kJ.", "250,0 kJ."],
   "B",
   "Hai giai đoạn:\n"
   "• Đưa nước đá từ −10 °C lên 0 °C: Q₁ = 0,50 · 2100 · 10 = 10 500 J.\n"
   "• Nóng chảy hoàn toàn ở 0 °C: Q₂ = 3,4·10⁵ · 0,50 = 170 000 J.\n"
   "Q = 180 500 J = 180,5 kJ. Sai lầm thường gặp là bỏ quên giai đoạn làm nóng nước đá.",
   "Nhiệt nóng chảy riêng", TB),

mc("Cần cung cấp nhiệt lượng bằng bao nhiêu để biến 0,20 kg nước ở 80 °C thành hơi nước hoàn toàn ở "
   "100 °C? Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
   ["452,0 kJ.", "468,8 kJ.", "485,0 kJ.", "520,0 kJ."],
   "B",
   "• Đun nước từ 80 °C lên 100 °C: Q₁ = 0,20 · 4200 · 20 = 16 800 J.\n"
   "• Hoá hơi hoàn toàn ở 100 °C: Q₂ = 2,26·10⁶ · 0,20 = 452 000 J.\n"
   "Q = 468 800 J = 468,8 kJ.",
   "Nhiệt hoá hơi riêng", TB),

mc("Thả một miếng nhôm khối lượng 0,30 kg ở 120 °C vào 0,60 kg nước ở 25 °C trong bình cách nhiệt (bỏ qua "
   "nhiệt dung của bình). Cho c_nhôm = 880 J/(kg·K), c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt "
   "gần nhất với",
   ["29,5 °C.", "34,0 °C.", "41,2 °C.", "55,0 °C."],
   "B",
   "0,30 · 880 · (120 − t) = 0,60 · 4200 · (t − 25)\n"
   "⟹ 264(120 − t) = 2520(t − 25) ⟹ 31 680 − 264t = 2520t − 63 000\n"
   "⟹ 2784t = 94 680 ⟹ t ≈ 34,0 °C.",
   "Cân bằng nhiệt", TB),

mc("Tốc độ bay hơi của một chất lỏng KHÔNG phụ thuộc vào yếu tố nào sau đây?",
   ["Nhiệt độ của chất lỏng.", "Diện tích mặt thoáng.",
    "Gió trên mặt thoáng.", "Thể tích của bình chứa nằm dưới mặt thoáng."],
   "D",
   "Bay hơi chỉ xảy ra trên mặt thoáng nên phụ thuộc nhiệt độ, diện tích mặt thoáng, gió và độ ẩm không "
   "khí. Phần chất lỏng nằm sâu bên dưới không tham gia trực tiếp vào quá trình bay hơi.",
   "Sự bay hơi", TB),

mc("Vào những ngày trời lạnh, ta nhìn thấy “khói trắng” khi thở ra. Hiện tượng này là do",
   ["hơi nước trong hơi thở ngưng tụ thành các giọt nước rất nhỏ.",
    "hơi thở của người chứa khói.",
    "không khí lạnh bị đốt nóng và bốc cháy.",
    "hơi nước trong không khí thăng hoa."],
   "A",
   "Hơi thở chứa nhiều hơi nước ở nhiệt độ cơ thể; gặp không khí lạnh, hơi nước bị làm lạnh đột ngột và "
   "ngưng tụ thành sương mù các giọt nước li ti mà ta nhìn thấy.",
   "Sự ngưng tụ – thực tiễn", TB),

mc("Nhiệt kế điện trở hoạt động dựa trên tính chất nào?",
   ["Điện trở của vật dẫn thay đổi theo nhiệt độ.",
    "Thể tích của chất lỏng thay đổi theo nhiệt độ.",
    "Áp suất chất khí thay đổi theo nhiệt độ.",
    "Màu sắc của vật thay đổi theo nhiệt độ."],
   "A",
   "Nhiệt kế điện trở đo nhiệt độ gián tiếp qua giá trị điện trở, thường dùng để đo nhiệt độ cao hoặc "
   "trong các hệ tự động hoá.",
   "Nhiệt kế", D),

mc("Một nhiệt kế X được chia độ tuỳ ý. Đồ thị bên cho biết mối liên hệ giữa số chỉ của nhiệt kế X và "
   "nhiệt độ Celsius. Khi nhiệt kế X chỉ 20 °X thì nhiệt độ của vật là",
   ["10 °C.", "20 °C.", "30 °C.", "45 °C."],
   "B",
   "Từ đồ thị, quan hệ là bậc nhất. Hai mốc dễ đọc: t = 0 °C ứng với −10 °X; t = 100 °C ứng với 140 °X.\n"
   "Hệ số góc: (140 − (−10))/100 = 1,5 ⟹ số chỉ X = −10 + 1,5·t.\n"
   "Với X = 20: 20 = −10 + 1,5t ⟹ t = 20 °C.",
   "Đọc đồ thị – thang nhiệt độ", K, fig="n_dt_hainhietke",
   cap="Số chỉ nhiệt kế X theo nhiệt độ Celsius"),

mc("Một khối khí nhận nhiệt lượng 500 J và giãn nở sinh công 300 J. Độ biến thiên nội năng của khối khí là",
   ["+800 J.", "+200 J.", "−200 J.", "−800 J."],
   "B",
   "Q = +500 J (nhận nhiệt), A = −300 J (sinh công).\nΔU = A + Q = −300 + 500 = +200 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Ở vùng ven biển, ban ngày đất liền nóng lên nhanh hơn mặt biển. Nguyên nhân chủ yếu là",
   ["nước biển có nhiệt dung riêng lớn hơn nhiều so với đất, cát.",
    "Mặt Trời chiếu vào đất liền mạnh hơn chiếu vào biển.",
    "đất có khối lượng riêng nhỏ hơn nước.",
    "nước biển phản xạ toàn bộ ánh sáng Mặt Trời."],
   "A",
   "Nhiệt dung riêng của nước (4200 J/(kg·K)) lớn hơn nhiều so với đất, cát (khoảng 800 J/(kg·K)). Cùng "
   "nhận một nhiệt lượng như nhau, đất nóng lên nhanh hơn nước rất nhiều. Đây cũng là nguồn gốc của gió "
   "đất – gió biển.",
   "Nhiệt dung riêng – thực tiễn", TB),

mc("Đại lượng nào sau đây KHÔNG phụ thuộc vào khối lượng của vật?",
   ["Nhiệt lượng cần để làm nóng vật thêm 1 °C.",
    "Nội năng của vật.",
    "Nhiệt dung riêng của chất làm nên vật.",
    "Nhiệt lượng cần để làm nóng chảy hoàn toàn vật."],
   "C",
   "Nhiệt dung riêng là đặc trưng của CHẤT, không phụ thuộc khối lượng hay hình dạng vật. Ba đại lượng "
   "còn lại đều tỉ lệ thuận với khối lượng.",
   "Phân biệt các đại lượng nhiệt", TB),
],
P2=[
ds("Hình vẽ là đồ thị nhiệt lượng cung cấp Q theo độ tăng nhiệt độ ΔT của hai chất lỏng X và Y; mỗi mẫu "
   "có khối lượng 0,50 kg.",
   [("Cả hai đồ thị đều là đường thẳng đi qua gốc toạ độ vì Q tỉ lệ thuận với ΔT.", True,
     "Đúng. Q = mcΔT với m, c không đổi nên Q tỉ lệ thuận với ΔT; khi ΔT = 0 thì Q = 0."),
    ("Nhiệt dung riêng của chất Y bằng 2400 J/(kg·K).", True,
     "Đúng. Hệ số góc của đường Y: k = 60 kJ/50 K = 1,2 kJ/K = 1200 J/K ⟹ c = k/m = 1200/0,50 = "
     "2400 J/(kg·K)."),
    ("Để cùng tăng thêm 40 K, chất X cần nhiều hơn chất Y là 36 kJ.", True,
     "Đúng. Q_X = 0,50 · 4200 · 40 = 84 kJ; Q_Y = 0,50 · 2400 · 40 = 48 kJ; hiệu bằng 36 kJ. "
     "Có thể đọc trực tiếp trên đồ thị: 84 − 48 = 36 kJ."),
    ("Nếu thay mẫu X bằng mẫu cùng chất nhưng khối lượng 1,0 kg thì đồ thị của nó sẽ thoải hơn.", False,
     "Sai. Hệ số góc k = m·c tăng gấp đôi khi khối lượng tăng gấp đôi, nên đồ thị DỐC HƠN chứ không "
     "thoải hơn.")],
   "Đọc và phân tích đồ thị Q–ΔT", TB, fig="n_dt_QdT",
   cap="Nhiệt lượng cung cấp theo độ tăng nhiệt độ"),

ds("Một ấm điện có công suất 800 W được dùng để đun 2,0 kg nước ở 20 °C. Hiệu suất của ấm là 90%. "
   "Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
   [("Công suất có ích dùng để làm nóng nước là 720 W.", True,
     "Đúng. P_ci = H·P = 0,90 · 800 = 720 W."),
    ("Nhiệt lượng cần cung cấp cho nước để nó đạt 100 °C là 672 kJ.", True,
     "Đúng. Q = mcΔt = 2,0 · 4200 · (100 − 20) = 672 000 J = 672 kJ."),
    ("Thời gian đun nước đến khi sôi vào khoảng 933 giây.", True,
     "Đúng. t = Q/P_ci = 672 000/720 ≈ 933 s ≈ 15 phút 33 giây."),
    ("Nếu tiếp tục đun thêm 5 phút sau khi nước sôi thì toàn bộ 2,0 kg nước sẽ hoá hơi hết.", False,
     "Sai. Nhiệt lượng cung cấp thêm là 720 · 300 = 216 000 J, chỉ đủ làm hoá hơi "
     "m = 216 000/2,26·10⁶ ≈ 0,096 kg, tức khoảng 96 g — chưa tới 5% lượng nước.")],
   "Nhiệt dung riêng – hiệu suất – nhiệt hoá hơi riêng", TB),

ds("Xét ba mẫu chất lỏng (1), (2), (3) cùng khối lượng 0,50 kg, được đun bằng cùng một thiết bị có công "
   "suất không đổi P = 210 W (bỏ qua hao phí). Đồ thị nhiệt độ theo thời gian như hình vẽ.",
   [("Chất (1) nóng lên nhanh nhất nên có nhiệt dung riêng nhỏ nhất.", True,
     "Đúng. Hệ số góc ΔT/Δt = P/(mc) tỉ lệ nghịch với c; đường (1) dốc nhất nên c nhỏ nhất."),
    ("Nhiệt dung riêng của chất (3) bằng 4200 J/(kg·K).", True,
     "Đúng. Hệ số góc của đường (3) là 0,10 K/s ⟹ c = P/(m · 0,10) = 210/(0,50 · 0,10) = "
     "4200 J/(kg·K) — chất (3) chính là nước."),
    ("Sau cùng một khoảng thời gian đun, ba mẫu nhận được những nhiệt lượng khác nhau.", False,
     "Sai. Cùng một thiết bị, cùng công suất P và cùng thời gian t thì nhiệt lượng nhận được "
     "Q = P·t là NHƯ NHAU. Chúng chỉ khác nhau ở độ tăng nhiệt độ, vì nhiệt dung riêng khác nhau."),
    ("Nhiệt dung riêng của chất (1) bằng 1400 J/(kg·K).", True,
     "Đúng. Hệ số góc đường (1) là 0,30 K/s ⟹ c = 210/(0,50 · 0,30) = 1400 J/(kg·K).")],
   "Đọc đồ thị T–t – nhiệt dung riêng", K, fig="n_dt_batchat",
   cap="Nhiệt độ ba mẫu chất lỏng theo thời gian đun"),

ds("Xét quá trình biến đổi nội năng của một khối khí trong xilanh có pit-tông.",
   [("Nếu khối khí bị nén và đồng thời được giữ ở nhiệt độ không đổi thì nội năng của nó không đổi.", True,
     "Đúng. Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ; nhiệt độ không đổi thì ΔU = 0 (khi đó khí nhận "
     "công bao nhiêu sẽ toả ra nhiệt lượng bấy nhiêu)."),
    ("Khi khí giãn nở đẩy pit-tông đi lên thì khí sinh công, tức là A < 0.", True,
     "Đúng. Theo quy ước ΔU = A + Q với A là công khí NHẬN được; khi khí sinh công thì A mang dấu âm."),
    ("Một khối khí nhận nhiệt lượng 600 J và nhận công 200 J thì nội năng tăng 400 J.", False,
     "Sai. Cả hai đều dương nên ΔU = A + Q = 200 + 600 = 800 J. Giá trị 400 J là kết quả khi lấy hiệu "
     "thay vì lấy tổng."),
    ("Có thể làm tăng nội năng của khối khí mà không cần truyền nhiệt cho nó.", True,
     "Đúng. Chỉ cần thực hiện công lên khí, ví dụ nén nhanh khí trong một bình cách nhiệt: khi đó Q = 0 "
     "nhưng ΔU = A > 0.")],
   "Định luật I nhiệt động lực học", TB),
],
P3=[
sa("Từ đồ thị Q–ΔT của hai chất lỏng X và Y (mỗi mẫu 0,50 kg), nhiệt dung riêng của chất Y bằng bao nhiêu "
   "J/(kg·K)?",
   "2400",
   "Hệ số góc của đường Y: k = 60 kJ/50 K = 1200 J/K. Mà k = m·c nên c = 1200/0,50 = 2400 J/(kg·K).",
   "Đọc đồ thị Q–ΔT", TB, fig="n_dt_QdT", cap="Đồ thị Q theo ΔT"),

sa("Một ấm điện công suất 800 W, hiệu suất 90%, dùng để đun 2,0 kg nước từ 20 °C đến khi sôi (100 °C). "
   "Thời gian đun bằng bao nhiêu giây (làm tròn đến hàng đơn vị)? Cho c = 4200 J/(kg·K).",
   "933",
   "Q = mcΔt = 2,0 · 4200 · 80 = 672 000 J.\n"
   "Công suất có ích: P_ci = 0,90 · 800 = 720 W.\n"
   "t = Q/P_ci = 672 000/720 ≈ 933 s.",
   "Nhiệt dung riêng – hiệu suất", TB),

sa("Cung cấp 51 kJ cho một khối nước đá đang ở 0 °C thì nó vừa vặn tan hết, nước tạo thành vẫn ở 0 °C. "
   "Khối lượng của khối nước đá đó bằng bao nhiêu gam? Cho λ = 3,4·10⁵ J/kg.",
   "150",
   "Toàn bộ nhiệt lượng dùng cho quá trình nóng chảy: Q = λm\n"
   "⟹ m = Q/λ = 51 000/3,4·10⁵ = 0,15 kg = 150 g.",
   "Nhiệt nóng chảy riêng – bài toán ngược", TB),

sa("Thả miếng nhôm 0,30 kg ở 120 °C vào 0,60 kg nước ở 25 °C trong bình cách nhiệt. Cho "
   "c_nhôm = 880 J/(kg·K), c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt bằng bao nhiêu độ C "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "34,0",
   "0,30 · 880 · (120 − t) = 0,60 · 4200 · (t − 25)\n"
   "⟹ 264(120 − t) = 2520(t − 25) ⟹ 2784t = 94 680 ⟹ t ≈ 34,0 °C.",
   "Cân bằng nhiệt", TB),

sa("Một khối khí nhận nhiệt lượng 700 J và giãn nở sinh công 400 J. Nội năng của khối khí TĂNG bao nhiêu jun?",
   "300",
   "Q = +700 J, A = −400 J ⟹ ΔU = A + Q = −400 + 700 = +300 J.",
   "Định luật I nhiệt động lực học", TB),

sa("Ba mẫu chất lỏng cùng khối lượng được đun bằng cùng một thiết bị (đồ thị T–t ở phần trên). Tỉ số giữa "
   "nhiệt dung riêng của chất (3) và chất (1) bằng bao nhiêu?",
   "3",
   "Cùng P và cùng m thì hệ số góc ΔT/Δt = P/(mc) tỉ lệ nghịch với c, do đó\n"
   "c₃/c₁ = (hệ số góc đường 1)/(hệ số góc đường 3) = 0,30/0,10 = 3.",
   "Đọc đồ thị – suy luận tỉ lệ", K, fig="n_dt_batchat", cap="Đồ thị T theo t của ba mẫu"),
])


# =====================================================================
DE4 = dict(
ma="12C1-Đ04", ten="ĐỀ SỐ 4", muc="Dễ → Trung bình",
trongtam="Đồ thị nóng chảy của kim loại; nhiệt lượng kế; bài toán thực tiễn về đun nước",
P1=[
mc("Chất rắn vô định hình có đặc điểm nào sau đây?",
   ["Có cấu trúc tinh thể và nhiệt độ nóng chảy xác định.",
    "Không có cấu trúc tinh thể và không có nhiệt độ nóng chảy xác định.",
    "Có nhiệt độ nóng chảy xác định nhưng không có cấu trúc tinh thể.",
    "Luôn ở thể lỏng ở nhiệt độ phòng."],
   "B",
   "Chất rắn vô định hình (thuỷ tinh, nhựa, sáp…) có các hạt sắp xếp không theo trật tự xa nên khi nung "
   "nóng chúng mềm dần rồi chảy lỏng trong một khoảng nhiệt độ, không có nhiệt độ nóng chảy xác định.",
   "Cấu trúc của chất", D),

mc("Khi nung nóng, thuỷ tinh mềm dần rồi mới chảy lỏng chứ không có nhiệt độ nóng chảy xác định. "
   "Nguyên nhân là do",
   ["thuỷ tinh có khối lượng riêng lớn.",
    "các hạt trong thuỷ tinh sắp xếp không theo một trật tự xác định nên liên kết giữa chúng có độ bền "
    "rất khác nhau.",
    "thuỷ tinh dẫn nhiệt rất kém.",
    "thuỷ tinh có nhiệt dung riêng lớn."],
   "B",
   "Do không có mạng tinh thể, các liên kết trong thuỷ tinh mạnh yếu khác nhau; liên kết yếu bị phá vỡ "
   "trước ở nhiệt độ thấp hơn, liên kết mạnh bị phá vỡ sau, nên chất mềm dần trong một khoảng nhiệt độ.",
   "Cấu trúc của chất", TB),

mc("Hình vẽ là đồ thị nhiệt độ theo thời gian khi nung nóng 1,0 kg chì bằng thiết bị có công suất không "
   "đổi P = 100 W (bỏ qua hao phí). Nhiệt độ nóng chảy của chì là",
   ["27 °C.", "100 °C.", "327 °C.", "400 °C."],
   "C",
   "Đoạn nằm ngang của đồ thị ứng với quá trình nóng chảy; đọc trên trục tung ⟹ nhiệt độ nóng chảy "
   "= 327 °C.",
   "Đọc đồ thị nóng chảy", D, fig="n_dt_chi",
   cap="Nhiệt độ của 1,0 kg chì theo thời gian nung"),

mc("Vẫn với đồ thị ở câu trên, nhiệt dung riêng của chì ở thể rắn bằng",
   ["100 J/(kg·K).", "130 J/(kg·K).", "250 J/(kg·K).", "390 J/(kg·K)."],
   "B",
   "Giai đoạn đầu: chì rắn nóng lên từ 27 °C đến 327 °C (ΔT = 300 K) trong t₁ = 390 s.\n"
   "P·t₁ = m·c·ΔT ⟹ c = P·t₁/(m·ΔT) = 100 · 390/(1,0 · 300) = 130 J/(kg·K).",
   "Đọc đồ thị – nhiệt dung riêng", K, fig="n_dt_chi",
   cap="Nhiệt độ của 1,0 kg chì theo thời gian nung"),

mc("Vẫn với đồ thị trên, nhiệt nóng chảy riêng của chì bằng",
   ["0,13·10⁵ J/kg.", "0,25·10⁵ J/kg.", "0,39·10⁵ J/kg.", "3,40·10⁵ J/kg."],
   "B",
   "Đoạn nằm ngang kéo dài từ 390 s đến 640 s, tức t₂ = 250 s.\n"
   "P·t₂ = λ·m ⟹ λ = P·t₂/m = 100 · 250/1,0 = 25 000 J/kg = 0,25·10⁵ J/kg.",
   "Đọc đồ thị – nhiệt nóng chảy riêng", K, fig="n_dt_chi",
   cap="Nhiệt độ của 1,0 kg chì theo thời gian nung"),

mc("Vẫn với đồ thị trên, ở thời điểm t = 500 s, khối chì",
   ["hoàn toàn ở thể rắn.", "hoàn toàn ở thể lỏng.",
    "gồm cả thể rắn và thể lỏng.", "đã hoá hơi một phần."],
   "C",
   "Thời điểm 500 s nằm giữa đoạn nằm ngang (390 s → 640 s), tức quá trình nóng chảy đang diễn ra dở "
   "dang: trong nồi có cả chì rắn và chì lỏng ở cùng 327 °C.",
   "Đọc đồ thị – chuyển thể", TB, fig="n_dt_chi",
   cap="Nhiệt độ của 1,0 kg chì theo thời gian nung"),

mc("Một bình nước nóng chứa 20 lít nước ở 25 °C, dây đốt có công suất 2500 W. Coi 1 lít nước có khối "
   "lượng 1 kg và bỏ qua mọi hao phí. Thời gian để nước đạt 65 °C là",
   ["672 s.", "1008 s.", "1344 s.", "2016 s."],
   "C",
   "Q = mcΔt = 20 · 4200 · (65 − 25) = 20 · 4200 · 40 = 3 360 000 J.\n"
   "t = Q/P = 3 360 000/2500 = 1344 s ≈ 22,4 phút.",
   "Nhiệt dung riêng – thực tiễn", TB, fig="n_sd_binhnuocnong",
   cap="Bình nước nóng dùng dây đốt"),

mc("Trong một thí nghiệm dùng nhiệt lượng kế, người ta phải đậy nắp và dùng vỏ cách nhiệt nhằm mục đích",
   ["làm cho nước nóng nhanh hơn.",
    "hạn chế sự trao đổi nhiệt với môi trường để có thể coi hệ là cô lập về nhiệt.",
    "giữ cho khối lượng nước không đổi.",
    "làm cho nhiệt kế chỉ chính xác hơn."],
   "B",
   "Chỉ khi hệ được coi là cô lập về nhiệt thì mới áp dụng được phương trình cân bằng nhiệt "
   "Q_toả = Q_thu.",
   "Nhiệt lượng kế", D, fig="n_sd_nhietluongke", cap="Cấu tạo nhiệt lượng kế"),

mc("Nội dung nào sau đây KHÔNG thuộc nguyên lí truyền nhiệt?",
   ["Nhiệt tự truyền từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn.",
    "Sự truyền nhiệt dừng lại khi nhiệt độ hai vật bằng nhau.",
    "Nhiệt lượng vật này toả ra bằng nhiệt lượng vật kia thu vào.",
    "Vật có khối lượng lớn hơn luôn toả nhiệt cho vật có khối lượng nhỏ hơn."],
   "D",
   "Chiều truyền nhiệt chỉ do CHÊNH LỆCH NHIỆT ĐỘ quyết định, hoàn toàn không phụ thuộc khối lượng. "
   "Ba nội dung còn lại chính là ba ý của nguyên lí truyền nhiệt.",
   "Nguyên lí truyền nhiệt", D),

mc("Phương trình cân bằng nhiệt cho hệ cô lập gồm hai vật là",
   ["Q_toả = Q_thu.", "Q_toả + Q_thu = 0 với cả hai đều dương.",
    "Q_toả = 2Q_thu.", "Q_toả − Q_thu = ΔU."],
   "A",
   "Trong hệ cô lập, nhiệt lượng do vật nóng toả ra đúng bằng nhiệt lượng do vật lạnh thu vào.",
   "Cân bằng nhiệt", D),

mc("Thả một quả cân bằng sắt khối lượng 0,50 kg ở 100 °C vào 0,40 kg nước ở 20 °C trong nhiệt lượng kế "
   "(bỏ qua nhiệt dung của bình). Cho c_sắt = 460 J/(kg·K), c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng "
   "gần nhất với",
   ["27,1 °C.", "29,6 °C.", "33,5 °C.", "40,2 °C."],
   "B",
   "0,50 · 460 · (100 − t) = 0,40 · 4200 · (t − 20)\n"
   "⟹ 230(100 − t) = 1680(t − 20) ⟹ 23 000 − 230t = 1680t − 33 600\n"
   "⟹ 1910t = 56 600 ⟹ t ≈ 29,6 °C.",
   "Cân bằng nhiệt", TB),

mc("Nội năng của một vật chắc chắn tăng khi",
   ["vật được nâng lên cao.", "vật chuyển động nhanh hơn.",
    "nhiệt độ của vật tăng lên.", "thể tích của vật tăng lên."],
   "C",
   "Nội năng liên quan tới chuyển động nhiệt của các phân tử bên trong vật; nhiệt độ tăng thì động năng "
   "chuyển động nhiệt tăng nên nội năng tăng. Nâng cao vật hay làm vật chuyển động chỉ thay đổi CƠ NĂNG.",
   "Nội năng", TB),

mc("Đơn vị nào sau đây KHÔNG dùng để đo nhiệt lượng?",
   ["Jun (J).", "Kilôjun (kJ).", "Calo (cal).", "Oát (W)."],
   "D",
   "Oát là đơn vị của công suất (J/s), không phải của nhiệt lượng. Nhiệt lượng là một dạng năng lượng, "
   "đo bằng jun (hoặc calo).",
   "Đơn vị nhiệt lượng", D),

mc("Nhiệt dung riêng của nước là 4200 J/(kg·K), của nước đá là 2100 J/(kg·K). Điều đó có nghĩa là",
   ["nước đá luôn lạnh hơn nước.",
    "để cùng tăng thêm 1 °C, mỗi kilôgam nước cần nhiệt lượng gấp đôi mỗi kilôgam nước đá.",
    "nước đá nóng chảy nhanh gấp đôi.",
    "nước có khối lượng riêng gấp đôi nước đá."],
   "B",
   "Nhiệt dung riêng là nhiệt lượng cần để 1 kg chất tăng thêm 1 K. Tỉ số 4200/2100 = 2 cho biết nước "
   "“khó nóng lên” gấp đôi nước đá.",
   "Nhiệt dung riêng", TB),

mc("Phải lấy đi nhiệt lượng bằng bao nhiêu để làm 1,0 kg hơi nước ở 100 °C ngưng tụ hoàn toàn thành "
   "nước ở 100 °C? Cho L = 2,26·10⁶ J/kg.",
   ["420 kJ.", "1130 kJ.", "2260 kJ.", "4520 kJ."],
   "C",
   "Ngưng tụ là quá trình ngược của hoá hơi nên nhiệt lượng toả ra đúng bằng nhiệt lượng đã thu vào "
   "khi hoá hơi: Q = Lm = 2,26·10⁶ · 1,0 = 2 260 000 J = 2260 kJ.",
   "Nhiệt hoá hơi riêng – sự ngưng tụ", TB),

mc("Nồi áp suất nấu chín thức ăn nhanh hơn nồi thường vì",
   ["nồi áp suất dẫn nhiệt tốt hơn.",
    "áp suất trong nồi cao hơn làm nước sôi ở nhiệt độ cao hơn 100 °C.",
    "nồi áp suất có nhiệt dung riêng nhỏ hơn.",
    "trong nồi áp suất nước không bay hơi."],
   "B",
   "Nhiệt độ sôi của chất lỏng tăng theo áp suất trên mặt thoáng. Nồi kín làm áp suất tăng nên nước sôi "
   "ở khoảng 110 – 120 °C, thức ăn được nấu ở nhiệt độ cao hơn nên chín nhanh hơn.",
   "Sự sôi – thực tiễn", TB),

mc("Nước đựng trong bình bằng đất nung thường mát hơn nước đựng trong bình thuỷ tinh kín đặt cùng chỗ. "
   "Nguyên nhân chính là",
   ["đất nung có nhiệt dung riêng lớn hơn thuỷ tinh.",
    "nước thấm qua thành bình đất nung rồi bay hơi, quá trình bay hơi thu nhiệt làm nước trong bình lạnh đi.",
    "đất nung phản xạ ánh sáng tốt hơn.",
    "bình đất nung có thể tích lớn hơn."],
   "B",
   "Đây là ứng dụng của việc bay hơi thu nhiệt: các phân tử nước “mang” năng lượng đi khi rời khỏi bề mặt "
   "bình, làm phần nước còn lại nguội đi.",
   "Sự bay hơi – thực tiễn", TB),

mc("Đại lượng nào sau đây đặc trưng cho khả năng “khó nóng lên” của một chất?",
   ["Nhiệt nóng chảy riêng.", "Nhiệt hoá hơi riêng.",
    "Nhiệt dung riêng.", "Khối lượng riêng."],
   "C",
   "Nhiệt dung riêng c càng lớn thì cùng một nhiệt lượng chỉ làm chất tăng nhiệt độ càng ít, tức chất "
   "càng “khó nóng lên”.",
   "Phân biệt các đại lượng nhiệt", D),
],
P2=[
ds("Hình vẽ là đồ thị nhiệt độ theo thời gian khi nung nóng 1,0 kg chì bằng thiết bị công suất không đổi "
   "P = 100 W (bỏ qua hao phí).",
   [("Trong 390 giây đầu, toàn bộ khối chì ở thể rắn.", True,
     "Đúng. Nhiệt độ tăng từ 27 °C đến 327 °C và chưa đạt tới đoạn nằm ngang nên chì chưa bắt đầu nóng chảy."),
    ("Nhiệt lượng cần để làm nóng chảy hoàn toàn khối chì là 25 kJ.", True,
     "Đúng. Q = P·t₂ = 100 · (640 − 390) = 100 · 250 = 25 000 J = 25 kJ."),
    ("Nhiệt lượng cần để đưa khối chì từ nhiệt độ ban đầu tới nhiệt độ nóng chảy lớn hơn nhiệt lượng "
     "cần để làm nó nóng chảy hoàn toàn.", True,
     "Đúng. Giai đoạn làm nóng kéo dài 390 s (39 kJ), dài hơn giai đoạn nóng chảy 250 s (25 kJ); cùng công "
     "suất nên thời gian dài hơn nghĩa là nhiệt lượng lớn hơn."),
    ("Nếu nung 2,0 kg chì bằng chính thiết bị đó thì đoạn nằm ngang vẫn dài 250 giây.", False,
     "Sai. Nhiệt lượng cần để nóng chảy tỉ lệ thuận với khối lượng: Q = λm tăng gấp đôi, mà công suất "
     "không đổi nên thời gian nóng chảy tăng gấp đôi, thành 500 s.")],
   "Đọc đồ thị nóng chảy", K, fig="n_dt_chi",
   cap="Nhiệt độ của 1,0 kg chì theo thời gian nung"),

ds("Một bình nước nóng chứa 20 lít nước ở 25 °C, dây đốt công suất 2500 W, hiệu suất 90%. "
   "Coi 1 lít nước có khối lượng 1 kg; c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng cần cung cấp cho nước để nó đạt 65 °C là 3360 kJ.", True,
     "Đúng. Q = 20 · 4200 · 40 = 3 360 000 J = 3360 kJ."),
    ("Công suất có ích của dây đốt là 2250 W.", True,
     "Đúng. P_ci = 0,90 · 2500 = 2250 W."),
    ("Thời gian đun khoảng 24,9 phút.", True,
     "Đúng. t = 3 360 000/2250 ≈ 1493 s ≈ 24,9 phút."),
    ("Nếu chỉ cần đun 10 lít nước cũng từ 25 °C lên 65 °C thì thời gian đun không thay đổi.", False,
     "Sai. Q tỉ lệ thuận với khối lượng nước, mà công suất không đổi nên thời gian giảm một nửa, "
     "còn khoảng 12,4 phút.")],
   "Nhiệt dung riêng – hiệu suất – thực tiễn", TB, fig="n_sd_binhnuocnong",
   cap="Bình nước nóng gia đình"),

ds("Một thỏi đồng khối lượng 0,40 kg được nung tới 90 °C rồi thả nhanh vào 0,30 kg nước ở 25 °C đựng "
   "trong nhiệt lượng kế lí tưởng. Cho c_đồng = 380 J/(kg·K), c_nước = 4200 J/(kg·K).",
   [("“Nhiệt dung” của khối nước là 1260 J/K, lớn hơn nhiều so với của thỏi đồng (152 J/K).", True,
     "Đúng. m·c của nước là 0,30 · 4200 = 1260 J/K; của đồng là 0,40 · 380 = 152 J/K."),
    ("Nhiệt độ khi cân bằng nhiệt vào khoảng 32,0 °C.", True,
     "Đúng. 152(90 − t) = 1260(t − 25) ⟹ 13 680 − 152t = 1260t − 31 500 ⟹ 1412t = 45 180 ⟹ t ≈ 32,0 °C."),
    ("Nhiệt lượng thỏi đồng toả ra bằng khoảng 8,8 kJ.", True,
     "Đúng. Q = 0,40 · 380 · (90 − 32,0) = 152 · 58,0 ≈ 8816 J ≈ 8,8 kJ (đúng bằng nhiệt lượng nước "
     "thu vào: 1260 · 7,0 ≈ 8,8 kJ)."),
    ("Muốn nhiệt độ cân bằng cao hơn, chỉ cần tăng khối lượng nước trong bình.", False,
     "Sai, ngược lại. Tăng khối lượng nước làm “nhiệt dung” của vế thu nhiệt lớn hơn nên nhiệt độ cân "
     "bằng càng gần 25 °C, tức là THẤP hơn.")],
   "Cân bằng nhiệt", TB, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

ds("Xét các hiện tượng nhiệt trong đời sống.",
   [("Khi ra khỏi bể bơi, ta cảm thấy lạnh hơn khi có gió thổi.", True,
     "Đúng. Gió làm tăng tốc độ bay hơi của nước trên da; bay hơi thu nhiệt từ cơ thể nên ta thấy lạnh hơn."),
    ("Về mùa đông, mặc nhiều lớp áo mỏng ấm hơn mặc một lớp áo dày cùng tổng bề dày vì giữa các lớp áo có "
     "không khí dẫn nhiệt kém.", True,
     "Đúng. Không khí là chất dẫn nhiệt rất kém; các lớp không khí bị “nhốt” giữa các lớp áo đóng vai trò "
     "lớp cách nhiệt bổ sung."),
    ("Nước đá đang tan trong cốc luôn ở nhiệt độ 0 °C dù ta vẫn tiếp tục cung cấp nhiệt cho cốc.", True,
     "Đúng. Chừng nào còn nước đá và nước cùng tồn tại, nhiệt lượng cung cấp chỉ dùng cho quá trình nóng "
     "chảy nên nhiệt độ giữ nguyên 0 °C."),
    ("Đun nước trên núi cao mất nhiều thời gian hơn để nước sôi vì trên đó nước sôi ở nhiệt độ cao hơn.", False,
     "Sai ở phần giải thích. Trên núi cao áp suất khí quyển thấp nên nước sôi ở nhiệt độ THẤP hơn "
     "(dưới 100 °C), do đó nước sôi nhanh hơn — nhưng chính vì vậy mà nấu chín thức ăn lại lâu hơn.")],
   "Hiện tượng nhiệt trong thực tiễn", TB),
],
P3=[
sa("Từ đồ thị nung nóng 1,0 kg chì (P = 100 W), nhiệt dung riêng của chì ở thể rắn bằng bao nhiêu J/(kg·K)?",
   "130",
   "Giai đoạn 1 kéo dài 390 s, nhiệt độ tăng 300 K.\nc = P·t₁/(m·ΔT) = 100 · 390/(1,0 · 300) = 130 J/(kg·K).",
   "Đọc đồ thị – nhiệt dung riêng", K, fig="n_dt_chi", cap="Đồ thị nung nóng chì"),

sa("Vẫn với đồ thị trên, nhiệt nóng chảy riêng của chì bằng bao nhiêu (tính theo đơn vị 10⁵ J/kg, làm "
   "tròn đến chữ số thập phân thứ hai)?",
   "0,25",
   "Đoạn nằm ngang kéo dài t₂ = 640 − 390 = 250 s.\nλ = P·t₂/m = 100 · 250/1,0 = 25 000 J/kg = 0,25·10⁵ J/kg.",
   "Đọc đồ thị – nhiệt nóng chảy riêng", K, fig="n_dt_chi", cap="Đồ thị nung nóng chì"),

sa("Một bình nước nóng chứa 20 lít nước ở 25 °C, dây đốt 2500 W, bỏ qua hao phí. Thời gian để nước đạt "
   "65 °C bằng bao nhiêu giây? Coi 1 lít nước nặng 1 kg; c = 4200 J/(kg·K).",
   "1344",
   "Q = 20 · 4200 · 40 = 3 360 000 J ⟹ t = Q/P = 3 360 000/2500 = 1344 s.",
   "Nhiệt dung riêng – thực tiễn", TB),

sa("Thả quả cân sắt 0,50 kg ở 100 °C vào 0,40 kg nước ở 20 °C trong nhiệt lượng kế lí tưởng. "
   "Cho c_sắt = 460, c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng bằng bao nhiêu độ C (làm tròn đến chữ "
   "số thập phân thứ nhất)?",
   "29,6",
   "230(100 − t) = 1680(t − 20) ⟹ 23 000 − 230t = 1680t − 33 600 ⟹ 1910t = 56 600 ⟹ t ≈ 29,6 °C.",
   "Cân bằng nhiệt", TB),

sa("Đun 500 g nước ban đầu ở 30 °C. Sau khi cung cấp 63 kJ (bỏ qua hao phí), nhiệt độ của nước bằng "
   "bao nhiêu độ C?",
   "60",
   "Δt = Q/(mc) = 63 000/(0,500 · 4200) = 63 000/2100 = 30 °C ⟹ nhiệt độ cuối 30 + 30 = 60 °C.",
   "Nhiệt dung riêng", TB),

sa("Một máy khuấy thực hiện công 12 kJ lên 2,0 kg nước đựng trong bình cách nhiệt lí tưởng. Nhiệt độ của "
   "nước tăng thêm bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? Cho c = 4200 J/(kg·K).",
   "1,4",
   "Bình cách nhiệt nên Q = 0; nước chỉ nhận công: ΔU = A = 12 000 J.\n"
   "Độ tăng nội năng này làm nước nóng lên: ΔU = mcΔt ⟹ Δt = 12 000/(2,0 · 4200) ≈ 1,4 °C.\n"
   "(Đây chính là ý tưởng thí nghiệm Joule chứng minh cơ năng chuyển hoá thành nội năng.)",
   "Định luật I – thực hiện công", K),
])


# =====================================================================
DE5 = dict(
ma="12C1-Đ05", ten="ĐỀ SỐ 5", muc="Trung bình",
trongtam="Cân bằng nhiệt có chuyển thể; hiệu suất thiết bị đun; vận dụng định luật I",
P1=[
mc("Khi truyền nhiệt cho một vật rắn đang ở nhiệt độ nóng chảy, nhiệt lượng truyền vào được dùng để",
   ["làm tăng nhiệt độ của vật.",
    "làm tăng thế năng tương tác giữa các phân tử, phá vỡ mạng tinh thể.",
    "làm tăng động năng chuyển động nhiệt của các phân tử.",
    "làm giảm nội năng của vật."],
   "B",
   "Trong khi nóng chảy nhiệt độ không đổi nên động năng trung bình của phân tử không đổi; nhiệt lượng "
   "nhận vào làm tăng thế năng tương tác, phá vỡ trật tự mạng tinh thể. Nội năng vẫn TĂNG.",
   "Sự nóng chảy – nội năng", TB),

mc("Thả 0,10 kg nước đá ở 0 °C vào 0,50 kg nước ở 40 °C trong bình cách nhiệt lí tưởng. Cho "
   "λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt gần nhất với",
   ["0 °C.", "13,5 °C.", "19,8 °C.", "26,7 °C."],
   "C",
   "Kiểm tra trước: nhiệt lượng nước toả ra khi hạ tới 0 °C là 0,50 · 4200 · 40 = 84 000 J, "
   "lớn hơn nhiệt lượng cần để nóng chảy toàn bộ nước đá (0,10 · 3,4·10⁵ = 34 000 J) ⟹ đá tan hết.\n"
   "Cân bằng: 34 000 + 0,10 · 4200 · t = 0,50 · 4200 · (40 − t)\n"
   "⟹ 34 000 + 420t = 84 000 − 2100t ⟹ 2520t = 50 000 ⟹ t ≈ 19,8 °C.",
   "Cân bằng nhiệt có chuyển thể", TB),

mc("Một bếp điện công suất 1200 W, hiệu suất 75%, dùng để đun 1,5 kg nước từ 25 °C đến khi sôi. Thời gian "
   "đun là (c_nước = 4200 J/(kg·K))",
   ["394 s.", "473 s.", "525 s.", "700 s."],
   "C",
   "Q = 1,5 · 4200 · (100 − 25) = 472 500 J. Công suất có ích P_ci = 0,75 · 1200 = 900 W.\n"
   "t = 472 500/900 = 525 s.",
   "Nhiệt dung riêng – hiệu suất", TB),

mc("Vẫn với bếp ở câu trên (P_ci = 900 W), sau khi nước sôi cần đun thêm bao lâu để 0,20 kg nước hoá hơi? "
   "Cho L = 2,26·10⁶ J/kg.",
   ["251 s.", "377 s.", "502 s.", "628 s."],
   "C",
   "Q = Lm = 2,26·10⁶ · 0,20 = 452 000 J ⟹ t = 452 000/900 ≈ 502 s.",
   "Nhiệt hoá hơi riêng", TB),

mc("Một nhiệt lượng kế có nhiệt dung 80 J/K, đang chứa 0,30 kg nước, cả bình và nước ở 20 °C. Đổ thêm "
   "0,10 kg nước ở 90 °C. Nhiệt độ khi cân bằng nhiệt gần nhất với",
   ["34,2 °C.", "36,7 °C.", "37,5 °C.", "39,0 °C."],
   "B",
   "Vỏ bình cũng nóng lên cùng nước nên phải kể nhiệt dung của bình vào vế thu nhiệt:\n"
   "0,10 · 4200 · (90 − t) = (0,30 · 4200 + 80)(t − 20)\n"
   "⟹ 420(90 − t) = 1340(t − 20) ⟹ 37 800 − 420t = 1340t − 26 800 ⟹ 1760t = 64 600 ⟹ t ≈ 36,7 °C.\n"
   "Nếu bỏ qua nhiệt dung bình sẽ được 37,5 °C — sai lệch đáng kể.",
   "Cân bằng nhiệt có nhiệt lượng kế", K, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

mc("Một khối khí trong xilanh nhận nhiệt lượng 800 J. Khí giãn nở đẩy pit-tông và sinh công 500 J. "
   "Nội năng của khối khí",
   ["tăng 1300 J.", "tăng 300 J.", "giảm 300 J.", "không đổi."],
   "B",
   "Q = +800 J, A = −500 J ⟹ ΔU = A + Q = +300 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Trong quá trình đẳng nhiệt của một lượng khí lí tưởng, nếu khí nhận nhiệt lượng 400 J thì",
   ["nội năng khí tăng 400 J.", "khí sinh công 400 J.",
    "khí nhận công 400 J.", "khí toả nhiệt 400 J."],
   "B",
   "Đẳng nhiệt ⟹ nội năng khí lí tưởng không đổi ⟹ ΔU = 0.\n"
   "Từ ΔU = A + Q: A = −Q = −400 J, tức khí sinh công 400 J.",
   "Định luật I – quá trình đẳng nhiệt", K),

mc("Người ta trộn 200 g nước ở 80 °C với m gam nước ở 20 °C được hỗn hợp ở 50 °C. Giá trị của m là",
   ["100 g.", "150 g.", "200 g.", "300 g."],
   "C",
   "200(80 − 50) = m(50 − 20) ⟹ 200 · 30 = m · 30 ⟹ m = 200 g.\n"
   "Nhận xét: nhiệt độ cân bằng nằm đúng giữa 20 °C và 80 °C nên hai lượng nước phải bằng nhau.",
   "Cân bằng nhiệt", TB),

mc("Để xác định nhiệt dung riêng của một kim loại, cần đo những đại lượng nào?",
   ["Chỉ cần khối lượng và nhiệt độ ban đầu của kim loại.",
    "Khối lượng kim loại, nhiệt lượng cung cấp cho nó và độ tăng nhiệt độ của nó.",
    "Chỉ cần nhiệt lượng cung cấp và thời gian đun.",
    "Khối lượng riêng và thể tích của kim loại."],
   "B",
   "Từ c = Q/(m·ΔT), muốn tính c phải biết đồng thời ba đại lượng: khối lượng m, nhiệt lượng Q "
   "(thường suy từ P·t) và độ tăng nhiệt độ ΔT.",
   "Thí nghiệm đo nhiệt dung riêng", TB, fig="n_sd_dun_dien",
   cap="Đo nhiệt dung riêng bằng phương pháp điện"),

mc("Cùng cung cấp nhiệt lượng 42 kJ cho 1,0 kg nước và cho 1,0 kg dầu (c_dầu = 2100 J/(kg·K)). Độ tăng "
   "nhiệt độ của dầu so với của nước",
   ["bằng nhau.", "lớn gấp đôi.", "nhỏ bằng một nửa.", "lớn gấp bốn lần."],
   "B",
   "ΔT = Q/(mc). Với Q và m như nhau, ΔT tỉ lệ nghịch với c: ΔT_dầu/ΔT_nước = 4200/2100 = 2.\n"
   "(Cụ thể: nước tăng 10 °C, dầu tăng 20 °C.)",
   "Nhiệt dung riêng", TB),

mc("Trong quá trình chất lỏng sôi, phát biểu nào sau đây SAI?",
   ["Nhiệt độ của chất lỏng không đổi.",
    "Chất lỏng vẫn tiếp tục nhận nhiệt lượng.",
    "Nội năng của khối chất không đổi vì nhiệt độ không đổi.",
    "Sự hoá hơi xảy ra cả trên mặt thoáng lẫn trong lòng chất lỏng."],
   "C",
   "Nội năng vẫn TĂNG trong khi sôi: nhiệt lượng cung cấp làm tăng thế năng tương tác, tách các phân tử "
   "ra khỏi khối chất lỏng, dù nhiệt độ (tức động năng trung bình) không đổi.",
   "Sự sôi – nội năng", K),

mc("Một vật khối lượng 2,0 kg rơi từ độ cao 20 m xuống đất và nằm yên. Lấy g = 10 m/s². Nếu toàn bộ cơ "
   "năng chuyển thành nội năng của vật thì nội năng của vật tăng thêm",
   ["40 J.", "200 J.", "400 J.", "800 J."],
   "C",
   "Cơ năng ban đầu (thế năng): W = mgh = 2,0 · 10 · 20 = 400 J. Khi vật nằm yên trên đất, toàn bộ cơ năng "
   "này chuyển thành nội năng ⟹ ΔU = 400 J.",
   "Chuyển hoá cơ năng thành nội năng", TB),

mc("Vào mùa đông, cầm một thanh kim loại và một thanh gỗ cùng ở nhiệt độ phòng, ta thấy thanh kim loại "
   "lạnh hơn. Nguyên nhân là",
   ["thanh kim loại có nhiệt độ thấp hơn thanh gỗ.",
    "kim loại dẫn nhiệt tốt hơn nên lấy nhiệt từ tay nhanh hơn.",
    "kim loại có nhiệt dung riêng lớn hơn gỗ.",
    "gỗ toả nhiệt cho tay ta."],
   "B",
   "Hai thanh cùng nhiệt độ phòng. Cảm giác “lạnh” phản ánh TỐC ĐỘ mất nhiệt của da: kim loại dẫn nhiệt "
   "tốt nên rút nhiệt khỏi tay nhanh hơn nhiều so với gỗ.",
   "Dẫn nhiệt – thực tiễn", TB),

mc("Đun 0,50 kg nước từ 20 °C. Sau khi cung cấp 168 kJ (bỏ qua hao phí) thì nhiệt độ của nước là",
   ["60 °C.", "80 °C.", "100 °C.", "nước đã sôi và một phần hoá hơi."],
   "C",
   "Δt = Q/(mc) = 168 000/(0,50 · 4200) = 80 °C ⟹ nhiệt độ cuối là 20 + 80 = 100 °C, nước vừa đạt "
   "nhiệt độ sôi và chưa có phần nào hoá hơi (vì muốn hoá hơi cần thêm nhiệt lượng rất lớn).",
   "Nhiệt dung riêng", TB),

mc("Ở thời điểm nào trong quá trình nung nóng liên tục một khối nước đá từ −20 °C, nội năng của hệ tăng "
   "mà nhiệt độ không tăng?",
   ["Khi nước đá đang nóng lên.", "Khi nước đá đang nóng chảy.",
    "Khi nước đang nóng lên.", "Không có giai đoạn nào như vậy."],
   "B",
   "Trong giai đoạn nóng chảy, nhiệt độ giữ nguyên 0 °C trong khi nhiệt lượng vẫn được cung cấp liên tục "
   "nên nội năng của hệ tăng.",
   "Đọc đồ thị – nội năng", TB, fig="n_dt_nuocda",
   cap="Đường nung nóng nước đá"),

mc("Một hệ nhận nhiệt lượng Q và nội năng tăng đúng bằng Q. Kết luận nào sau đây là ĐÚNG?",
   ["Hệ đã sinh công.", "Hệ đã nhận công.",
    "Hệ không trao đổi công với bên ngoài.", "Hệ đã toả nhiệt."],
   "C",
   "ΔU = A + Q mà ΔU = Q nên A = 0: hệ không trao đổi công với bên ngoài (chẳng hạn khí trong bình kín "
   "thể tích không đổi).",
   "Định luật I nhiệt động lực học", TB),

mc("Muốn làm giảm thời gian đun sôi một ấm nước bằng bếp điện, cách nào sau đây KHÔNG hiệu quả?",
   ["Đậy nắp ấm để giảm hao phí.",
    "Dùng ấm có công suất lớn hơn.",
    "Giảm lượng nước cần đun.",
    "Dùng ấm làm bằng vật liệu có nhiệt dung riêng lớn hơn."],
   "D",
   "Ấm có nhiệt dung riêng lớn hơn sẽ “ngốn” thêm nhiệt lượng để làm nóng chính vỏ ấm, làm thời gian đun "
   "TĂNG lên. Ba cách còn lại đều giảm nhiệt lượng cần cung cấp hoặc tăng công suất.",
   "Hiệu suất – thực tiễn", TB),

mc("Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn 2,0 kg nước đá ở 0 °C bằng nhiệt lượng cần để đun "
   "nóng 2,0 kg nước lên thêm bao nhiêu độ? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   ["khoảng 40,5 °C.", "khoảng 61,0 °C.", "khoảng 81,0 °C.", "khoảng 100,0 °C."],
   "C",
   "Q = λm = 3,4·10⁵ · 2,0 = 680 000 J. Với cùng khối lượng nước:\n"
   "Δt = Q/(mc) = 680 000/(2,0 · 4200) ≈ 81,0 °C.\n"
   "Nghĩa là năng lượng để làm tan 1 kg nước đá đủ để đun 1 kg nước nóng thêm tới 81 °C.",
   "So sánh các đại lượng nhiệt", K),
],
P2=[
ds("Thả 0,10 kg nước đá ở 0 °C vào 0,50 kg nước ở 40 °C trong bình cách nhiệt lí tưởng. Cho "
   "λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng mà 0,50 kg nước toả ra khi hạ nhiệt độ từ 40 °C xuống 0 °C là 84 kJ.", True,
     "Đúng. Q = 0,50 · 4200 · 40 = 84 000 J = 84 kJ."),
    ("Nhiệt lượng cần để làm nóng chảy toàn bộ nước đá là 34 kJ.", True,
     "Đúng. Q = λm = 3,4·10⁵ · 0,10 = 34 000 J = 34 kJ."),
    ("Khi cân bằng nhiệt, trong bình vẫn còn nước đá chưa tan hết.", False,
     "Sai. Vì 84 kJ > 34 kJ nên lượng nhiệt nước toả ra thừa sức làm tan hết nước đá; nhiệt độ cân bằng "
     "cao hơn 0 °C (khoảng 19,8 °C)."),
    ("Nhiệt độ khi cân bằng nhiệt vào khoảng 19,8 °C.", True,
     "Đúng. 34 000 + 0,10 · 4200 · t = 0,50 · 4200 · (40 − t) ⟹ 2520t = 50 000 ⟹ t ≈ 19,8 °C.")],
   "Cân bằng nhiệt có chuyển thể", K),

ds("Một bếp điện có công suất 1200 W, hiệu suất 75%, dùng để đun 1,5 kg nước từ 25 °C. "
   "Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
   [("Công suất có ích của bếp là 900 W.", True,
     "Đúng. P_ci = H·P = 0,75 · 1200 = 900 W."),
    ("Thời gian đun nước tới lúc sôi là 525 giây.", True,
     "Đúng. Q = 1,5 · 4200 · 75 = 472 500 J ⟹ t = 472 500/900 = 525 s."),
    ("Trong 525 giây đó, phần năng lượng hao phí ra môi trường là khoảng 157,5 kJ.", True,
     "Đúng. Công suất hao phí là 1200 − 900 = 300 W ⟹ Q_hp = 300 · 525 = 157 500 J = 157,5 kJ. "
     "(Cũng bằng 25% của tổng điện năng 630 kJ.)"),
    ("Sau khi nước sôi, nếu tiếp tục đun thêm 502 giây thì toàn bộ 1,5 kg nước hoá hơi hết.", False,
     "Sai. Trong 502 s bếp chỉ cung cấp 900 · 502 ≈ 452 000 J, đủ làm hoá hơi "
     "m = 452 000/2,26·10⁶ = 0,20 kg, tức chỉ khoảng 13% lượng nước.")],
   "Hiệu suất – nhiệt hoá hơi riêng", TB),

ds("Xét việc áp dụng định luật I nhiệt động lực học ΔU = A + Q cho một khối khí lí tưởng.",
   [("Trong quá trình đẳng tích, toàn bộ nhiệt lượng khí nhận được đều làm tăng nội năng của khí.", True,
     "Đúng. Thể tích không đổi nên A = 0, do đó ΔU = Q."),
    ("Trong quá trình đẳng nhiệt, khí nhận nhiệt lượng bao nhiêu thì sinh công bấy nhiêu.", True,
     "Đúng. Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên ΔU = 0 ⟹ A = −Q, tức công khí sinh ra bằng "
     "đúng nhiệt lượng nhận vào."),
    ("Nếu một khối khí bị nén trong bình cách nhiệt thì nhiệt độ của nó giảm.", False,
     "Sai. Cách nhiệt nên Q = 0; bị nén nên khí NHẬN công, A > 0 ⟹ ΔU = A > 0: nội năng và nhiệt độ đều "
     "TĂNG. Đây là nguyên nhân làm nóng thân bơm xe khi bơm nhanh."),
    ("Một hệ có thể vừa nhận nhiệt vừa có nội năng giảm.", True,
     "Đúng, nếu công mà hệ sinh ra lớn hơn nhiệt lượng nhận vào. Ví dụ Q = +200 J nhưng A = −500 J thì "
     "ΔU = −300 J < 0.")],
   "Định luật I nhiệt động lực học", K, fig="n_sd_dl1", cap="Quy ước dấu"),

ds("Một nhiệt lượng kế có nhiệt dung 80 J/K đang chứa 0,30 kg nước, cả bình và nước cùng ở 20 °C. Đổ thêm "
   "vào bình 0,10 kg nước ở 90 °C. Cho c_nước = 4200 J/(kg·K).",
   [("Vỏ bình nhiệt lượng kế cũng thu nhiệt trong quá trình này.", True,
     "Đúng. Vỏ bình ban đầu ở 20 °C và nóng lên cùng với nước nên nó cũng thu một phần nhiệt lượng."),
    ("Nếu bỏ qua nhiệt dung của bình thì nhiệt độ cân bằng tính được là 37,5 °C.", True,
     "Đúng. 0,10(90 − t) = 0,30(t − 20) ⟹ 9 − 0,1t = 0,3t − 6 ⟹ 0,4t = 15 ⟹ t = 37,5 °C."),
    ("Khi kể đến nhiệt dung của bình, nhiệt độ cân bằng vào khoảng 36,7 °C.", True,
     "Đúng. 420(90 − t) = 1340(t − 20) ⟹ 1760t = 64 600 ⟹ t ≈ 36,7 °C. Kể thêm bình thì có thêm vật "
     "thu nhiệt nên nhiệt độ cân bằng thấp hơn."),
    ("Nhiệt dung của bình 80 J/K có nghĩa là bình được làm bằng chất có nhiệt dung riêng 80 J/(kg·K).", False,
     "Sai. Nhiệt dung (J/K) là đại lượng của cả VẬT, bằng tích m·c; muốn suy ra nhiệt dung riêng phải "
     "biết thêm khối lượng của bình.")],
   "Nhiệt lượng kế – phân biệt nhiệt dung và nhiệt dung riêng", K,
   fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),
],
P3=[
sa("Thả 0,10 kg nước đá ở 0 °C vào 0,50 kg nước ở 40 °C trong bình cách nhiệt lí tưởng. Cho "
   "λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt bằng bao nhiêu độ C (làm tròn đến "
   "chữ số thập phân thứ nhất)?",
   "19,8",
   "Kiểm tra: nước toả tối đa 84 kJ > 34 kJ cần cho nóng chảy ⟹ đá tan hết.\n"
   "34 000 + 420t = 84 000 − 2100t ⟹ 2520t = 50 000 ⟹ t ≈ 19,8 °C.",
   "Cân bằng nhiệt có chuyển thể", K),

sa("Bếp điện 1200 W, hiệu suất 75%, đun 1,5 kg nước từ 25 °C đến sôi. Thời gian đun bằng bao nhiêu giây?",
   "525",
   "Q = 1,5 · 4200 · 75 = 472 500 J; P_ci = 900 W ⟹ t = 472 500/900 = 525 s.",
   "Hiệu suất", TB),

sa("Trộn 200 g nước ở 80 °C với m gam nước ở 20 °C thu được nước ở 50 °C. Giá trị của m bằng bao nhiêu gam?",
   "200",
   "200(80 − 50) = m(50 − 20) ⟹ m = 200 g (nhiệt độ cân bằng ở đúng giữa nên hai khối lượng bằng nhau).",
   "Cân bằng nhiệt", TB),

sa("Một nhiệt lượng kế có nhiệt dung 80 J/K chứa 0,30 kg nước ở 20 °C. Đổ thêm 0,10 kg nước ở 90 °C. "
   "Nhiệt độ khi cân bằng bằng bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)?",
   "36,7",
   "420(90 − t) = (1260 + 80)(t − 20) ⟹ 37 800 − 420t = 1340t − 26 800 ⟹ 1760t = 64 600 ⟹ t ≈ 36,7 °C.",
   "Cân bằng nhiệt có nhiệt lượng kế", K),

sa("Một búa máy khối lượng 10 kg rơi từ độ cao 2,0 m đóng vào một đầu cọc bằng sắt khối lượng 0,50 kg. "
   "Biết 60% cơ năng của búa chuyển thành nội năng của đầu cọc. Lấy g = 10 m/s², "
   "c_sắt = 460 J/(kg·K). Sau một nhát búa, nhiệt độ đầu cọc tăng thêm bao nhiêu độ C "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "0,52",
   "Cơ năng của búa: W = mgh = 10 · 10 · 2,0 = 200 J.\n"
   "Phần chuyển thành nội năng đầu cọc: ΔU = 0,60 · 200 = 120 J.\n"
   "Δt = ΔU/(m_cọc · c) = 120/(0,50 · 460) = 120/230 ≈ 0,52 °C.",
   "Chuyển hoá cơ năng thành nội năng", K),

sa("Nhiệt lượng cần để làm nóng chảy hoàn toàn 2,0 kg nước đá ở 0 °C có thể đun 2,0 kg nước nóng thêm bao "
   "nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "81,0",
   "Q = λm = 680 000 J ⟹ Δt = Q/(mc) = 680 000/(2,0 · 4200) ≈ 81,0 °C.\n"
   "Kết quả này cho thấy nhiệt nóng chảy riêng của nước đá tương đương với việc đun nước nóng thêm 81 °C.",
   "So sánh các đại lượng nhiệt", K),
])


# =====================================================================
DE6 = dict(
ma="12C1-Đ06", ten="ĐỀ SỐ 6", muc="Trung bình",
trongtam="Nước đá tan một phần; hiệu suất nhiên liệu; khai thác trọn vẹn đồ thị nung nóng",
P1=[
mc("Khi hai vật tiếp xúc nhau, nhiệt luôn tự truyền từ vật này sang vật kia cho tới khi",
   ["hai vật có cùng nội năng.", "hai vật có cùng nhiệt độ.",
    "vật nóng hết nhiệt lượng.", "hai vật có cùng khối lượng."],
   "B", "Sự truyền nhiệt dừng lại khi hai vật cân bằng nhiệt, tức có cùng nhiệt độ.",
   "Nguyên lí truyền nhiệt", D),

mc("Cho 0,30 kg đá viên ở 0 °C vào một bình giữ nhiệt đang chứa 0,20 kg trà nóng ở 30 °C. Coi nhiệt dung "
   "riêng của trà bằng của nước và bỏ qua nhiệt dung của bình. Cho λ = 3,4·10⁵ J/kg, "
   "c = 4200 J/(kg·K). Nhiệt độ của hỗn hợp khi cân bằng nhiệt là",
   ["0 °C.", "5,2 °C.", "12,0 °C.", "−7,4 °C."],
   "A",
   "Trà chỉ toả được tối đa Q = 0,20 · 4200 · 30 = 25 200 J khi hạ tới 0 °C, "
   "trong khi làm tan hết 0,30 kg đá cần 0,30 · 3,4·10⁵ = 102 000 J.\n"
   "Vì 25 200 J < 102 000 J nên đá chỉ tan một phần; khi trong bình còn đồng thời cả đá và nước thì "
   "nhiệt độ bắt buộc là 0 °C.",
   "Cân bằng nhiệt – điều kiện ẩn", K),

mc("Với dữ kiện ở câu trên, khối lượng đá chưa tan khi cân bằng nhiệt gần nhất với",
   ["74 g.", "150 g.", "226 g.", "300 g."],
   "C",
   "Khối lượng đá đã tan: Δm = 25 200/3,4·10⁵ ≈ 0,0741 kg = 74,1 g.\n"
   "Đá còn lại: 300 − 74,1 ≈ 226 g.",
   "Cân bằng nhiệt – điều kiện ẩn", K),

mc("Dùng bếp ga đun 3,0 kg nước từ 20 °C đến sôi thì tiêu tốn 40 g ga. Biết năng suất toả nhiệt của ga là "
   "44·10⁶ J/kg, c_nước = 4200 J/(kg·K). Hiệu suất của bếp gần nhất với",
   ["42,5%.", "57,3%.", "68,0%.", "75,4%."],
   "B",
   "Nhiệt lượng có ích: Q_i = 3,0 · 4200 · 80 = 1 008 000 J.\n"
   "Nhiệt lượng do ga toả ra: Q_tp = 0,040 · 44·10⁶ = 1 760 000 J.\n"
   "H = Q_i/Q_tp = 1 008 000/1 760 000 ≈ 0,573 = 57,3%.",
   "Hiệu suất – thực tiễn", TB),

mc("Hình vẽ là đường nung nóng 0,50 kg nước đá ban đầu ở −20 °C bằng thiết bị công suất không đổi "
   "P = 420 W. Nhiệt dung riêng của nước đá xác định từ đồ thị bằng",
   ["1050 J/(kg·K).", "2100 J/(kg·K).", "3360 J/(kg·K).", "4200 J/(kg·K)."],
   "B",
   "Giai đoạn 1 kéo dài 50 s, nước đá tăng từ −20 °C lên 0 °C (ΔT = 20 K).\n"
   "c = P·t/(m·ΔT) = 420 · 50/(0,50 · 20) = 21 000/10 = 2100 J/(kg·K).",
   "Đọc đồ thị – nhiệt dung riêng", K, fig="n_dt_nuocda",
   cap="Nung nóng 0,50 kg nước đá bằng thiết bị 420 W"),

mc("Vẫn với đồ thị trên, nhiệt nóng chảy riêng của nước đá xác định được là",
   ["1,68·10⁵ J/kg.", "2,10·10⁵ J/kg.", "3,36·10⁵ J/kg.", "4,20·10⁵ J/kg."],
   "C",
   "Đoạn nằm ngang kéo dài 450 − 50 = 400 s.\nλ = P·t/m = 420 · 400/0,50 = 336 000 J/kg = 3,36·10⁵ J/kg.",
   "Đọc đồ thị – nhiệt nóng chảy riêng", K, fig="n_dt_nuocda",
   cap="Nung nóng 0,50 kg nước đá bằng thiết bị 420 W"),

mc("Nhiệt độ của một vật tăng lên chứng tỏ",
   ["vật đã nhận nhiệt lượng từ bên ngoài.",
    "động năng chuyển động nhiệt trung bình của các phân tử trong vật tăng lên.",
    "thế năng tương tác giữa các phân tử trong vật tăng lên.",
    "khối lượng của vật tăng lên."],
   "B",
   "Nhiệt độ là đại lượng đặc trưng cho động năng chuyển động nhiệt trung bình của phân tử. Nhiệt độ tăng "
   "chưa chắc do nhận nhiệt — có thể do được thực hiện công (nén, cọ xát).",
   "Nhiệt độ – mô hình động học phân tử", TB),

mc("Một khối khí bị nén đẳng nhiệt. Kết luận nào sau đây đúng?",
   ["Khí nhận công và nội năng tăng.", "Khí nhận công và toả nhiệt ra ngoài.",
    "Khí sinh công và nhận nhiệt.", "Khí không trao đổi nhiệt với bên ngoài."],
   "B",
   "Đẳng nhiệt ⟹ ΔU = 0. Khí bị nén ⟹ A > 0. Từ 0 = A + Q suy ra Q = −A < 0: khí toả nhiệt đúng bằng "
   "công nhận được.",
   "Định luật I – quá trình đẳng nhiệt", K),

mc("Một chiếc tủ lạnh hoạt động dựa trên nguyên tắc: chất làm lạnh bay hơi trong ngăn lạnh rồi ngưng tụ ở "
   "giàn nóng phía sau tủ. Vai trò của hai quá trình đó là",
   ["bay hơi toả nhiệt, ngưng tụ thu nhiệt.",
    "bay hơi thu nhiệt trong tủ, ngưng tụ toả nhiệt ra ngoài phòng.",
    "cả hai quá trình đều thu nhiệt.",
    "cả hai quá trình đều toả nhiệt."],
   "B",
   "Bay hơi thu nhiệt nên lấy nhiệt khỏi ngăn lạnh; ngưng tụ toả nhiệt nên nhả nhiệt ra không khí phòng. "
   "Vì vậy phòng kín sẽ NÓNG lên nếu ta mở cửa tủ lạnh.",
   "Chuyển thể – ứng dụng thực tiễn", TB),

mc("Trộn ba lượng nước: 1,0 kg ở 20 °C; 2,0 kg ở 50 °C và 1,0 kg ở 80 °C trong bình cách nhiệt lí tưởng. "
   "Nhiệt độ khi cân bằng là",
   ["45 °C.", "50 °C.", "55 °C.", "60 °C."],
   "B",
   "Cùng chất nên nhiệt độ cân bằng là trung bình có trọng số theo khối lượng:\n"
   "t = (1·20 + 2·50 + 1·80)/(1 + 2 + 1) = (20 + 100 + 80)/4 = 200/4 = 50 °C.",
   "Cân bằng nhiệt", TB),

mc("Cần cung cấp nhiệt lượng bằng bao nhiêu để biến 0,10 kg nước đá ở −20 °C thành hơi nước hoàn toàn ở "
   "100 °C? Cho c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵, L = 2,26·10⁶ J/kg.",
   ["260,0 kJ.", "302,4 kJ.", "306,2 kJ.", "342,0 kJ."],
   "C",
   "Bốn giai đoạn:\n"
   "Q₁ = 0,10 · 2100 · 20 = 4 200 J   (đá: −20 → 0 °C)\n"
   "Q₂ = 0,10 · 3,4·10⁵ = 34 000 J    (nóng chảy)\n"
   "Q₃ = 0,10 · 4200 · 100 = 42 000 J (nước: 0 → 100 °C)\n"
   "Q₄ = 0,10 · 2,26·10⁶ = 226 000 J  (hoá hơi)\n"
   "Q = 306 200 J = 306,2 kJ. Chú ý giai đoạn hoá hơi chiếm tới 74% tổng nhiệt lượng.",
   "Bài toán nhiệt nhiều giai đoạn", K),

mc("Một nhiệt kế X có quan hệ với thang Celsius như đồ thị bên. Khi nhiệt độ là 60 °C thì nhiệt kế X chỉ",
   ["50 °X.", "65 °X.", "80 °X.", "90 °X."],
   "C",
   "Từ đồ thị: t = 0 °C ↔ −10 °X và t = 100 °C ↔ 140 °X ⟹ X = −10 + 1,5t.\n"
   "Với t = 60 °C: X = −10 + 1,5 · 60 = 80 °X.",
   "Đọc đồ thị – thang nhiệt độ", TB, fig="n_dt_hainhietke",
   cap="Số chỉ nhiệt kế X theo nhiệt độ Celsius"),

mc("Trong công nghiệp, người ta thường dùng hơi nước ở nhiệt độ cao để truyền nhiệt đi xa. Lí do chính là",
   ["hơi nước nhẹ nên dễ vận chuyển.",
    "hơi nước khi ngưng tụ giải phóng một nhiệt lượng rất lớn.",
    "hơi nước có nhiệt dung riêng lớn nhất trong các chất.",
    "hơi nước không gây ăn mòn đường ống."],
   "B",
   "Mỗi kilôgam hơi nước khi ngưng tụ giải phóng 2,26·10⁶ J — lớn hơn rất nhiều so với nhiệt lượng thu "
   "được khi chỉ làm nguội nước lỏng, nên hơi nước là chất tải nhiệt rất hiệu quả.",
   "Nhiệt hoá hơi riêng – thực tiễn", TB),

mc("Một hệ có nội năng giảm 200 J trong khi vẫn nhận nhiệt lượng 300 J. Công mà hệ đã sinh ra là",
   ["100 J.", "200 J.", "300 J.", "500 J."],
   "D",
   "ΔU = A + Q ⟹ −200 = A + 300 ⟹ A = −500 J, tức hệ SINH công 500 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Đại lượng nào sau đây có cùng đơn vị với nhiệt nóng chảy riêng?",
   ["Nhiệt dung riêng.", "Nhiệt hoá hơi riêng.", "Nhiệt lượng.", "Công suất."],
   "B", "Cả nhiệt nóng chảy riêng λ và nhiệt hoá hơi riêng L đều có đơn vị J/kg.",
   "Đơn vị các đại lượng nhiệt", D),

mc("Người ta đun 1,0 kg nước bằng một thiết bị và ghi nhận: sau 3 phút nhiệt độ tăng từ 20 °C lên 50 °C. "
   "Nếu bỏ qua hao phí thì công suất của thiết bị là",
   ["420 W.", "700 W.", "840 W.", "1260 W."],
   "B",
   "Q = 1,0 · 4200 · 30 = 126 000 J trong t = 180 s ⟹ P = Q/t = 126 000/180 = 700 W.",
   "Nhiệt dung riêng – công suất", TB),

mc("Hai bình cách nhiệt giống nhau: bình A chứa 1 kg nước ở 80 °C, bình B chứa 1 kg dầu "
   "(c = 2100 J/(kg·K)) cũng ở 80 °C. Để nguội trong cùng điều kiện, nếu cả hai cùng toả ra một nhiệt "
   "lượng như nhau thì",
   ["nước nguội nhanh hơn dầu.", "dầu nguội nhanh hơn nước (nhiệt độ giảm nhiều hơn).",
    "hai chất nguội như nhau.", "chưa đủ dữ kiện."],
   "B",
   "Δt = Q/(mc); cùng Q và cùng m thì Δt tỉ lệ nghịch với c. Dầu có c bằng một nửa của nước nên nhiệt độ "
   "giảm gấp đôi.",
   "Nhiệt dung riêng", TB),

mc("Hiện tượng nào sau đây KHÔNG phải là bằng chứng cho thấy các phân tử chuyển động không ngừng?",
   ["Mùi nước hoa lan toả khắp phòng.",
    "Hạt phấn hoa chuyển động zic-zăc trong nước.",
    "Đường tan trong nước ngay cả khi không khuấy.",
    "Quả bóng rơi xuống đất rồi nảy lên."],
   "D",
   "Quả bóng nảy là hiện tượng cơ học của vật vĩ mô, không liên quan tới chuyển động nhiệt của phân tử. "
   "Ba hiện tượng còn lại đều là hiện tượng khuếch tán hoặc chuyển động Brown.",
   "Mô hình động học phân tử", D),
],
P2=[
ds("Để làm mát đồ uống, người ta bỏ 2 viên đá (mỗi viên 25 g) ở 0 °C vào một cốc cách nhiệt chứa 200 g "
   "nước ngọt ở 25 °C. Coi nhiệt dung riêng của nước ngọt bằng của nước; λ = 3,4·10⁵ J/kg, "
   "c = 4200 J/(kg·K).",
   [("Nhiệt lượng lớn nhất mà nước ngọt có thể nhường cho đá là 21 kJ.", True,
     "Đúng. Nước ngọt chỉ có thể hạ tới 0 °C: Q = 0,200 · 4200 · 25 = 21 000 J."),
    ("Cả hai viên đá đều tan hết.", True,
     "Đúng. Làm tan 50 g đá chỉ cần 0,050 · 3,4·10⁵ = 17 000 J < 21 000 J nên đá tan hết và vẫn còn dư "
     "nhiệt để hạ tiếp nhiệt độ hỗn hợp."),
    ("Nhiệt độ của đồ uống khi cân bằng nhiệt vào khoảng 3,8 °C.", True,
     "Đúng. Phần nhiệt còn lại 21 000 − 17 000 = 4000 J làm nóng toàn bộ 250 g nước từ 0 °C:\n"
     "t = 4000/(0,250 · 4200) ≈ 3,8 °C."),
    ("Nếu bỏ 4 viên đá (tổng 100 g) thì đá vẫn tan hết và nhiệt độ cuối vẫn xấp xỉ 0 °C.", False,
     "Sai. Làm tan 100 g đá cần 34 000 J, lớn hơn 21 000 J mà nước ngọt có thể cung cấp, nên đá chỉ tan "
     "một phần (khoảng 62 g) và trong cốc vẫn còn đá; nhiệt độ đúng bằng 0 °C nhưng phần khẳng định "
     "“đá vẫn tan hết” là sai.")],
   "Cân bằng nhiệt – điều kiện ẩn", K),

ds("Đường nung nóng 0,50 kg nước đá ban đầu ở −20 °C bằng thiết bị công suất không đổi P = 420 W "
   "(bỏ qua hao phí) được cho như hình vẽ.",
   [("Nhiệt dung riêng của nước đá xác định từ đồ thị là 2100 J/(kg·K).", True,
     "Đúng. c = P·t/(m·ΔT) = 420 · 50/(0,50 · 20) = 2100 J/(kg·K)."),
    ("Nhiệt nóng chảy riêng của nước đá xác định từ đồ thị là 3,36·10⁵ J/kg.", True,
     "Đúng. λ = P·t/m = 420 · 400/0,50 = 336 000 J/kg."),
    ("Nhiệt dung riêng của nước xác định từ đồ thị là 4200 J/(kg·K).", True,
     "Đúng. Giai đoạn cuối kéo dài 950 − 450 = 500 s, nước tăng từ 0 °C lên 100 °C:\n"
     "c = 420 · 500/(0,50 · 100) = 4200 J/(kg·K)."),
    ("Nếu tăng công suất thiết bị lên gấp đôi thì đồ thị giữ nguyên hình dạng nhưng nhiệt độ nóng chảy "
     "tăng lên.", False,
     "Sai. Tăng công suất chỉ làm mọi giai đoạn diễn ra nhanh gấp đôi (đồ thị bị “nén” lại theo trục thời "
     "gian); nhiệt độ nóng chảy là hằng số của chất, không đổi ở 0 °C.")],
   "Khai thác trọn vẹn đồ thị nung nóng", K, fig="n_dt_nuocda",
   cap="Nung nóng 0,50 kg nước đá bằng thiết bị 420 W"),

ds("Dùng bếp ga đun 3,0 kg nước từ 20 °C đến sôi thì tiêu tốn 40 g ga. Năng suất toả nhiệt của ga là "
   "44·10⁶ J/kg; c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng có ích truyền cho nước là 1008 kJ.", True,
     "Đúng. Q_i = 3,0 · 4200 · (100 − 20) = 1 008 000 J."),
    ("Nhiệt lượng toàn phần do ga toả ra là 1760 kJ.", True,
     "Đúng. Q_tp = m·q = 0,040 · 44·10⁶ = 1 760 000 J."),
    ("Hiệu suất của bếp vào khoảng 57%.", True,
     "Đúng. H = 1 008 000/1 760 000 ≈ 0,573, tức khoảng 57%."),
    ("Nếu đậy nắp nồi thì hiệu suất giảm vì hơi nước không thoát ra được.", False,
     "Sai, ngược lại. Đậy nắp làm giảm hao phí do bay hơi và do đối lưu không khí nóng, nên hiệu suất TĂNG "
     "và thời gian đun giảm.")],
   "Hiệu suất – thực tiễn", TB),

ds("Xét nội năng và các quá trình nhiệt của một khối khí lí tưởng.",
   [("Một hệ nhận nhiệt lượng 300 J mà nội năng lại giảm 200 J thì hệ đã sinh công 500 J.", True,
     "Đúng. ΔU = A + Q ⟹ −200 = A + 300 ⟹ A = −500 J, tức hệ sinh công 500 J."),
    ("Có thể làm nóng một khối khí mà không cần cho nó tiếp xúc với vật nóng hơn.", True,
     "Đúng. Chỉ cần nén khí (thực hiện công lên khí), ví dụ khi bơm xe hoặc trong kì nén của động cơ diesel."),
    ("Trong quá trình đẳng áp, khí nhận nhiệt lượng bao nhiêu thì nội năng tăng bấy nhiêu.", False,
     "Sai. Đẳng áp mà nhận nhiệt thì khí giãn nở và sinh công, nên chỉ MỘT PHẦN nhiệt lượng làm tăng nội "
     "năng: ΔU = Q + A với A < 0 nên ΔU < Q."),
    ("Nội năng của một lượng khí lí tưởng xác định tăng khi nhiệt độ tuyệt đối của nó tăng.", True,
     "Đúng. Nội năng khí lí tưởng chỉ là tổng động năng chuyển động nhiệt, tỉ lệ thuận với nhiệt độ "
     "tuyệt đối T.")],
   "Định luật I nhiệt động lực học", K),
],
P3=[
sa("Thả 0,30 kg nước đá ở 0 °C vào 0,20 kg nước ở 30 °C trong bình cách nhiệt lí tưởng. Cho "
   "λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K). Khối lượng nước đá còn lại khi cân bằng nhiệt bằng bao nhiêu gam "
   "(làm tròn đến hàng đơn vị)?",
   "226",
   "Nước toả tối đa 0,20 · 4200 · 30 = 25 200 J < 102 000 J cần để tan hết ⟹ đá tan một phần, t = 0 °C.\n"
   "Δm = 25 200/3,4·10⁵ ≈ 74 g ⟹ đá còn lại 300 − 74 ≈ 226 g.",
   "Cân bằng nhiệt – điều kiện ẩn", K),

sa("Từ đường nung nóng 0,50 kg nước đá bằng thiết bị 420 W, nhiệt nóng chảy riêng của nước đá bằng bao "
   "nhiêu (tính theo đơn vị 10⁵ J/kg, làm tròn đến chữ số thập phân thứ hai)?",
   "3,36",
   "Đoạn nằm ngang kéo dài 400 s ⟹ λ = P·t/m = 420 · 400/0,50 = 336 000 J/kg = 3,36·10⁵ J/kg.",
   "Đọc đồ thị – nhiệt nóng chảy riêng", K, fig="n_dt_nuocda", cap="Đường nung nóng nước đá"),

sa("Đun 3,0 kg nước từ 20 °C đến sôi bằng bếp ga tiêu tốn 40 g ga (năng suất toả nhiệt 44·10⁶ J/kg). "
   "Hiệu suất của bếp bằng bao nhiêu phần trăm (làm tròn đến chữ số thập phân thứ nhất)?",
   "57,3",
   "Q_i = 3,0 · 4200 · 80 = 1 008 000 J; Q_tp = 0,040 · 44·10⁶ = 1 760 000 J.\n"
   "H = 1 008 000/1 760 000 ≈ 0,573 = 57,3%.",
   "Hiệu suất – thực tiễn", TB),

sa("Một nồi bằng nhôm khối lượng 0,50 kg chứa 2,0 kg nước, cả nồi và nước cùng ở 25 °C. Cần cung cấp "
   "bao nhiêu kilôjun để đun sôi nồi nước này (100 °C)? Cho c_nhôm = 880, c_nước = 4200 J/(kg·K).",
   "663",
   "Cả nồi và nước cùng nóng lên 75 K nên đều thu nhiệt:\n"
   "Q = (m_nồi·c_nhôm + m_nước·c_nước)·Δt = (0,50·880 + 2,0·4200)·75 = (440 + 8400)·75 = 663 000 J\n"
   "  = 663 kJ. Phần nhiệt làm nóng nồi chiếm 33 kJ, khoảng 5%.",
   "Nhiệt dung riêng – hệ nhiều vật", TB),

sa("Trộn 1,0 kg nước ở 20 °C; 2,0 kg nước ở 50 °C và 1,0 kg nước ở 80 °C trong bình cách nhiệt lí tưởng. "
   "Nhiệt độ khi cân bằng bằng bao nhiêu độ C?",
   "50",
   "t = (1·20 + 2·50 + 1·80)/4 = 200/4 = 50 °C (trung bình có trọng số theo khối lượng).",
   "Cân bằng nhiệt", TB),

sa("Đun 1,0 kg nước, sau 3 phút nhiệt độ tăng từ 20 °C lên 50 °C. Bỏ qua hao phí. Công suất của thiết bị "
   "đun bằng bao nhiêu oát?",
   "700",
   "Q = 1,0 · 4200 · 30 = 126 000 J trong 180 s ⟹ P = 126 000/180 = 700 W.",
   "Nhiệt dung riêng – công suất", TB),
])


# =====================================================================
DE7 = dict(
ma="12C1-Đ07", ten="ĐỀ SỐ 7", muc="Trung bình → Khó",
trongtam="Khử ẩn số bằng hai thí nghiệm; lập tỉ số trên đồ thị; bài toán ngược",
P1=[
mc("Một nhóm học sinh làm hai thí nghiệm với cùng một nhiệt lượng kế. "
   "TN1: bình đang chứa 250 g nước, cả bình và nước ở 22 °C; đổ thêm 150 g nước ở 78 °C thì nhiệt độ cân "
   "bằng là 41,6 °C. Nhiệt dung của nhiệt lượng kế bằng",
   ["60 J/K.", "120 J/K.", "180 J/K.", "240 J/K."],
   "B",
   "Nước nóng toả: 0,150 · 4200 · (78 − 41,6) = 630 · 36,4 = 22 932 J.\n"
   "Vế thu nhiệt gồm nước lạnh VÀ vỏ bình, cùng tăng 41,6 − 22 = 19,6 K:\n"
   "(0,250 · 4200 + C) · 19,6 = 22 932 ⟹ 1050 + C = 1170 ⟹ C = 120 J/K.",
   "Nhiệt lượng kế – khử ẩn số", K, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

mc("Vẫn dùng nhiệt lượng kế đó (C = 120 J/K). TN2: bình chứa 250 g nước, cả bình và nước ở 22 °C; thả vào "
   "một vật kim loại khối lượng 300 g đang ở 95 °C thì nhiệt độ cân bằng là 30 °C. Nhiệt dung riêng của "
   "kim loại là",
   ["380 J/(kg·K).", "440 J/(kg·K).", "480 J/(kg·K).", "880 J/(kg·K)."],
   "C",
   "Nước và bình thu nhiệt: (0,250 · 4200 + 120) · (30 − 22) = 1170 · 8 = 9360 J.\n"
   "Kim loại toả nhiệt: 0,300 · c · (95 − 30) = 19,5c.\n"
   "⟹ c = 9360/19,5 = 480 J/(kg·K).\n"
   "Ý nghĩa của TN1 là đo trước nhiệt dung của bình — đại lượng bị “giấu” trong TN2.",
   "Nhiệt lượng kế – khử ẩn số", K, fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

mc("Đường nung nóng nước đá bằng thiết bị có công suất không đổi được cho như hình vẽ, nhưng KHÔNG biết "
   "khối lượng mẫu và công suất thiết bị. Đại lượng nào sau đây vẫn xác định được từ đồ thị?",
   ["Nhiệt dung riêng của nước đá.",
    "Nhiệt nóng chảy riêng của nước đá.",
    "Tỉ số giữa nhiệt nóng chảy riêng và nhiệt dung riêng của nước đá.",
    "Nhiệt lượng cần để làm nóng chảy hết mẫu."],
   "C",
   "Với t₁ = 50 s (ΔT₁ = 20 K) và t₂ = 400 s:\n"
   "c = P·t₁/(m·ΔT₁) và λ = P·t₂/m — cả hai đều chứa thừa số P/m chưa biết.\n"
   "Nhưng khi lập tỉ số thì P và m bị khử: λ/c = t₂·ΔT₁/t₁ = 400 · 20/50 = 160 K.",
   "Đọc đồ thị – khử ẩn số bằng tỉ số", K, fig="n_dt_nuocda",
   cap="Đường nung nóng nước đá (chưa biết m và P)"),

mc("Một ấm điện công suất 1000 W đun 1,0 kg nước từ 25 °C. Sau 5 phút nhiệt độ nước là 80 °C. Hiệu suất "
   "của ấm gần nhất với",
   ["65%.", "70%.", "77%.", "85%."],
   "C",
   "Q_i = 1,0 · 4200 · (80 − 25) = 231 000 J; Q_tp = P·t = 1000 · 300 = 300 000 J.\n"
   "H = 231 000/300 000 = 0,77 = 77%.",
   "Hiệu suất – bài toán ngược", TB),

mc("Cần thả bao nhiêu nước đá ở 0 °C vào 0,50 kg nước ở 60 °C để khi cân bằng nhiệt, nước đá vừa vặn tan "
   "hết và nhiệt độ hỗn hợp bằng đúng 0 °C? Cho λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   ["185 g.", "296 g.", "371 g.", "420 g."],
   "C",
   "Điều kiện “vừa tan hết và ở đúng 0 °C” nghĩa là toàn bộ nhiệt lượng nước toả ra khi hạ tới 0 °C được "
   "dùng hết cho quá trình nóng chảy:\n"
   "m·λ = 0,50 · 4200 · 60 = 126 000 J ⟹ m = 126 000/3,4·10⁵ ≈ 0,371 kg = 371 g.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Một khối khí thực hiện một quá trình trong đó nó nhận nhiệt lượng 900 J và nội năng tăng 400 J. "
   "Công mà khối khí sinh ra là",
   ["400 J.", "500 J.", "900 J.", "1300 J."],
   "B",
   "ΔU = A + Q ⟹ 400 = A + 900 ⟹ A = −500 J, tức khí sinh công 500 J.",
   "Định luật I nhiệt động lực học", TB),

mc("Đun nóng một chất lỏng bằng thiết bị công suất không đổi. Trong 4 phút đầu nhiệt độ tăng từ 20 °C lên "
   "60 °C. Nếu tiếp tục đun thêm 2 phút nữa (chất lỏng chưa sôi, bỏ qua hao phí) thì nhiệt độ đạt",
   ["70 °C.", "80 °C.", "90 °C.", "100 °C."],
   "B",
   "Cùng công suất và cùng khối lượng nên độ tăng nhiệt độ tỉ lệ thuận với thời gian đun:\n"
   "4 phút ↔ 40 °C ⟹ 2 phút ↔ 20 °C ⟹ nhiệt độ cuối 60 + 20 = 80 °C.",
   "Suy luận tỉ lệ", TB),

mc("Trong một thí nghiệm, người ta thấy phải cung cấp 2,52 kJ mới làm 0,20 kg của một chất lỏng nóng thêm "
   "3,0 °C. Nhiệt dung riêng của chất lỏng đó là",
   ["1400 J/(kg·K).", "2100 J/(kg·K).", "3200 J/(kg·K).", "4200 J/(kg·K)."],
   "D",
   "c = Q/(m·Δt) = 2520/(0,20 · 3,0) = 2520/0,6 = 4200 J/(kg·K).",
   "Nhiệt dung riêng", TB),

mc("Đổ m₁ gam nước ở 100 °C vào m₂ gam nước ở 20 °C được hỗn hợp ở 40 °C. Tỉ số m₁/m₂ bằng",
   ["1/2.", "1/3.", "1/4.", "2/3."],
   "B",
   "m₁(100 − 40) = m₂(40 − 20) ⟹ 60m₁ = 20m₂ ⟹ m₁/m₂ = 20/60 = 1/3.\n"
   "Lượng nước nóng chỉ bằng một phần ba lượng nước lạnh vì nó phải hạ 60 °C trong khi nước lạnh chỉ "
   "tăng 20 °C.",
   "Cân bằng nhiệt", TB),

mc("Người ta muốn hạ nhiệt độ 2,0 kg nước từ 30 °C xuống 10 °C bằng cách thả nước đá ở 0 °C vào. "
   "Khối lượng nước đá cần dùng ít nhất là (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["356 g.", "412 g.", "440 g.", "494 g."],
   "C",
   "Nhiệt lượng cần lấy đi khỏi 2,0 kg nước: Q = 2,0 · 4200 · 20 = 168 000 J.\n"
   "Nước đá vừa phải nóng chảy, vừa phải nóng lên tới 10 °C cùng với nước:\n"
   "m(3,4·10⁵ + 4200 · 10) = 168 000 ⟹ m · 382 000 = 168 000 ⟹ m ≈ 0,440 kg = 440 g.\n"
   "Bẫy: bỏ quên giai đoạn đun phần nước mới tan lên 10 °C sẽ cho 494 g.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Hai bình cách nhiệt A và B đựng cùng một chất lỏng. Bình A chứa 1 kg ở 20 °C, bình B chứa 3 kg ở "
   "60 °C. Trộn hai bình lại, nhiệt độ cân bằng là",
   ["30 °C.", "40 °C.", "45 °C.", "50 °C."],
   "D",
   "t = (1 · 20 + 3 · 60)/(1 + 3) = (20 + 180)/4 = 50 °C.\n"
   "Nhiệt độ cân bằng lệch về phía khối lượng lớn hơn.",
   "Cân bằng nhiệt", TB),

mc("Một tấm pin mặt trời có diện tích 2,0 m² nhận công suất bức xạ 800 W/m². Nếu 25% năng lượng này được "
   "dùng để đun nước thì sau 1 giờ có thể đun bao nhiêu kilôgam nước nóng thêm 40 °C?",
   ["4,3 kg.", "8,6 kg.", "12,3 kg.", "17,1 kg."],
   "B",
   "Công suất có ích: P = 0,25 · 800 · 2,0 = 400 W.\n"
   "Năng lượng trong 1 giờ: Q = 400 · 3600 = 1 440 000 J.\n"
   "m = Q/(c·Δt) = 1 440 000/(4200 · 40) ≈ 8,6 kg.",
   "Nhiệt dung riêng – năng lượng tái tạo", K),

mc("Trong quá trình nào sau đây nội năng của khối khí lí tưởng chắc chắn KHÔNG đổi?",
   ["Quá trình đẳng áp.", "Quá trình đẳng tích.",
    "Quá trình đẳng nhiệt.", "Quá trình khí bị nén trong bình cách nhiệt."],
   "C",
   "Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên chỉ có quá trình đẳng nhiệt mới bảo đảm ΔU = 0. "
   "Nén trong bình cách nhiệt làm nội năng TĂNG (A > 0, Q = 0).",
   "Nội năng khí lí tưởng", K),

mc("Một chất lỏng có nhiệt dung riêng c được đun bằng thiết bị công suất P. Nếu tăng khối lượng chất lỏng "
   "lên 1,5 lần và tăng công suất lên 3 lần thì thời gian để nhiệt độ tăng thêm cùng một lượng sẽ",
   ["tăng 2 lần.", "giảm 2 lần.", "tăng 4,5 lần.", "không đổi."],
   "B",
   "Từ P·t = m·c·ΔT ⟹ t = mcΔT/P. Với m tăng 1,5 lần và P tăng 3 lần thì t thay đổi theo hệ số "
   "1,5/3 = 0,5, tức là giảm 2 lần.",
   "Suy luận tỉ lệ", K),

mc("Trong một máy điều hoà nhiệt độ, môi chất lạnh nhận nhiệt từ không khí trong phòng và thải nhiệt ra "
   "ngoài trời. Để làm được điều đó, máy phải",
   ["không cần tiêu thụ năng lượng vì nhiệt tự truyền.",
    "tiêu thụ công (điện năng) để đưa nhiệt từ nơi lạnh hơn sang nơi nóng hơn.",
    "làm giảm nội năng của không khí ngoài trời.",
    "biến toàn bộ điện năng thành nhiệt lượng trong phòng."],
   "B",
   "Nhiệt chỉ TỰ truyền từ nơi nóng sang nơi lạnh. Muốn đi ngược chiều đó phải có máy thực hiện công, "
   "và điện năng tiêu thụ cuối cùng cũng bị thải ra ngoài trời cùng với nhiệt lấy từ phòng.",
   "Truyền nhiệt – ứng dụng", TB),

mc("Đại lượng nào sau đây của một chất KHÔNG thay đổi khi ta thay đổi khối lượng mẫu chất đó?",
   ["Nhiệt dung của mẫu.",
    "Nhiệt lượng cần để làm mẫu nóng chảy hoàn toàn.",
    "Nhiệt nóng chảy riêng.",
    "Nội năng của mẫu."],
   "C",
   "Nhiệt nóng chảy riêng λ là hằng số đặc trưng cho chất (J/kg). Nhiệt dung của mẫu (m·c), nhiệt lượng "
   "nóng chảy (λm) và nội năng đều tỉ lệ với khối lượng.",
   "Phân biệt đại lượng riêng và đại lượng của vật", TB),

mc("Cho 100 g hơi nước ở 100 °C ngưng tụ hoàn toàn rồi nguội tới 40 °C. Nhiệt lượng toả ra là "
   "(L = 2,26·10⁶ J/kg, c = 4200 J/(kg·K))",
   ["25,2 kJ.", "226,0 kJ.", "251,2 kJ.", "277,4 kJ."],
   "C",
   "Q₁ = Lm = 2,26·10⁶ · 0,100 = 226 000 J (ngưng tụ, toả nhiệt).\n"
   "Q₂ = mcΔt = 0,100 · 4200 · 60 = 25 200 J (nước nguội từ 100 °C xuống 40 °C).\n"
   "Q = 251 200 J = 251,2 kJ.",
   "Nhiệt hoá hơi riêng – ngưng tụ", K),

mc("Nhận định nào sau đây về nhiệt độ và nhiệt lượng là ĐÚNG?",
   ["Vật có nhiệt độ càng cao thì chứa càng nhiều nhiệt lượng.",
    "Hai vật cùng nhiệt độ thì có cùng nội năng.",
    "Nhiệt lượng chỉ có nghĩa khi nói về một quá trình truyền nhiệt.",
    "Nhiệt độ là số đo lượng nhiệt chứa trong vật."],
   "C",
   "Vật chứa NỘI NĂNG chứ không “chứa nhiệt lượng”. Nhiệt lượng là phần năng lượng được trao đổi trong "
   "một quá trình truyền nhiệt, nên chỉ nói tới nhiệt lượng khi gắn với một quá trình cụ thể.",
   "Phân biệt nhiệt độ – nhiệt lượng – nội năng", K),
],
P2=[
ds("Một nhóm học sinh đo nhiệt dung riêng của một kim loại bằng nhiệt lượng kế và thực hiện hai thí "
   "nghiệm. TN1: bình chứa 250 g nước, cả bình và nước ở 22 °C; đổ thêm 150 g nước ở 78 °C thì nhiệt độ "
   "cân bằng là 41,6 °C. TN2 (làm lại từ đầu): bình chứa 250 g nước ở 22 °C, thả vào vật kim loại 300 g ở "
   "95 °C thì nhiệt độ cân bằng là 30 °C. Cho c_nước = 4200 J/(kg·K).",
   [("TN1 nhằm mục đích xác định nhiệt dung của nhiệt lượng kế.", True,
     "Đúng. Trong TN1 mọi đại lượng khác đều đã biết nên ẩn số duy nhất là nhiệt dung C của bình."),
    ("Nhiệt dung của nhiệt lượng kế bằng 120 J/K.", True,
     "Đúng. 630 · 36,4 = (1050 + C) · 19,6 ⟹ 22 932 = 20 580 + 19,6C ⟹ C = 120 J/K."),
    ("Nhiệt dung riêng của kim loại bằng 480 J/(kg·K).", True,
     "Đúng. (1050 + 120) · 8 = 0,300 · c · 65 ⟹ 9360 = 19,5c ⟹ c = 480 J/(kg·K)."),
    ("Nếu bỏ qua nhiệt dung của bình trong TN2 thì giá trị nhiệt dung riêng tính được sẽ LỚN hơn 480 "
     "J/(kg·K).", False,
     "Sai. Bỏ qua bình tức là bỏ bớt một phần nhiệt lượng thu vào: c = 1050 · 8/19,5 ≈ 431 J/(kg·K), "
     "NHỎ hơn giá trị đúng khoảng 10%.")],
   "Nhiệt lượng kế – thiết kế thí nghiệm khử ẩn số", K,
   fig="n_sd_nhietluongke", cap="Nhiệt lượng kế dùng cho cả hai thí nghiệm"),

ds("Đường nung nóng một mẫu nước đá bằng thiết bị công suất không đổi được cho như hình vẽ. Giả sử "
   "KHÔNG biết khối lượng mẫu và công suất thiết bị.",
   [("Không thể xác định được nhiệt dung riêng của nước đá chỉ từ đồ thị này.", True,
     "Đúng. c = P·t₁/(m·ΔT₁) luôn chứa thừa số P/m chưa biết."),
    ("Tỉ số giữa nhiệt nóng chảy riêng và nhiệt dung riêng của nước đá bằng 160 K.", True,
     "Đúng. λ/c = t₂·ΔT₁/t₁ = 400 · 20/50 = 160 K (thừa số P/m bị khử). Kiểm tra bằng số liệu thật: "
     "3,36·10⁵/2100 = 160 ✓."),
    ("Tỉ số giữa nhiệt dung riêng của nước và của nước đá bằng 2.", True,
     "Đúng. c_nước/c_đá = (t₃/ΔT₃)/(t₁/ΔT₁) = (500/100)/(50/20) = 5/2,5 = 2 — cũng khử được P và m. "
     "Phù hợp với 4200/2100 = 2."),
    ("Tỉ số giữa nhiệt lượng cần cho giai đoạn nóng chảy và nhiệt lượng cần cho giai đoạn làm nóng nước "
     "đá từ −20 °C lên 0 °C bằng 4.", False,
     "Sai. Cùng một công suất nên nhiệt lượng tỉ lệ thuận với thời gian: Q₂/Q₁ = t₂/t₁ = 400/50 = 8, "
     "chứ không phải 4. Nói cách khác, làm tan hết khối nước đá tốn năng lượng gấp 8 lần việc hâm nó "
     "từ −20 °C lên 0 °C.")],
   "Đọc đồ thị – khử ẩn số", K, fig="n_dt_nuocda", cap="Đường nung nóng nước đá"),

ds("Một ấm điện công suất 1000 W dùng để đun 1,0 kg nước ở 25 °C. Sau 5 phút nhiệt độ nước đạt 80 °C. "
   "Cho c_nước = 4200 J/(kg·K).",
   [("Điện năng ấm tiêu thụ trong 5 phút là 300 kJ.", True,
     "Đúng. W = P·t = 1000 · 300 = 300 000 J = 300 kJ."),
    ("Nhiệt lượng nước thực sự nhận được là 231 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 55 = 231 000 J."),
    ("Hiệu suất của ấm là 77%.", True,
     "Đúng. H = 231/300 = 0,77 = 77%."),
    ("Công suất hao phí của ấm là 69 W.", False,
     "Sai. Công suất hao phí = 1000 − 770 = 230 W. Giá trị 69 W là kết quả nhầm lẫn khi lấy 23% của 300.")],
   "Hiệu suất – công suất hao phí", TB),

ds("Một cốc cách nhiệt chứa 0,50 kg nước ở 60 °C. Người ta lần lượt thử thả vào cốc những lượng đá ở "
   "0 °C khác nhau và xét trạng thái cuối cùng của hệ. Cho λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng lớn nhất mà 0,50 kg nước có thể toả ra là 126 kJ.", True,
     "Đúng. Nước chỉ hạ được tới 0 °C: Q = 0,50 · 4200 · 60 = 126 000 J."),
    ("Nếu thả 200 g nước đá thì toàn bộ nước đá sẽ tan hết.", True,
     "Đúng. Cần 0,200 · 3,4·10⁵ = 68 000 J < 126 000 J nên đá tan hết và nhiệt độ cân bằng cao hơn 0 °C."),
    ("Muốn nhiệt độ cân bằng đúng bằng 0 °C và nước đá vừa vặn tan hết thì phải thả khoảng 371 g nước đá.", True,
     "Đúng. m = 126 000/3,4·10⁵ ≈ 0,371 kg."),
    ("Nếu thả 500 g nước đá thì nhiệt độ cân bằng sẽ thấp hơn 0 °C.", False,
     "Sai. Với 500 g đá, nhiệt lượng cần để tan hết là 170 kJ > 126 kJ nên đá chỉ tan một phần; khi trong "
     "bình còn cả nước đá và nước thì nhiệt độ đúng bằng 0 °C, không thể thấp hơn.")],
   "Cân bằng nhiệt – phân tích các trường hợp", K),
],
P3=[
sa("TN1: nhiệt lượng kế chứa 250 g nước, cả bình và nước ở 22 °C; đổ thêm 150 g nước ở 78 °C thì nhiệt độ "
   "cân bằng là 41,6 °C. Nhiệt dung của nhiệt lượng kế bằng bao nhiêu J/K?",
   "120",
   "0,150·4200·(78 − 41,6) = (0,250·4200 + C)(41,6 − 22)\n"
   "⟹ 22 932 = (1050 + C)·19,6 ⟹ 1050 + C = 1170 ⟹ C = 120 J/K.",
   "Nhiệt lượng kế", K),

sa("Dùng chính nhiệt lượng kế đó (C = 120 J/K) chứa 250 g nước ở 22 °C, thả vào vật kim loại 300 g ở "
   "95 °C thì nhiệt độ cân bằng là 30 °C. Nhiệt dung riêng của kim loại bằng bao nhiêu J/(kg·K)?",
   "480",
   "(1050 + 120)·(30 − 22) = 0,300·c·(95 − 30) ⟹ 9360 = 19,5c ⟹ c = 480 J/(kg·K).",
   "Nhiệt lượng kế", K),

sa("Từ đường nung nóng nước đá (không biết khối lượng mẫu và công suất thiết bị), tỉ số giữa nhiệt nóng "
   "chảy riêng và nhiệt dung riêng của nước đá bằng bao nhiêu kelvin?",
   "160",
   "λ/c = (P·t₂/m) : (P·t₁/(m·ΔT₁)) = t₂·ΔT₁/t₁ = 400 · 20/50 = 160 K.",
   "Đọc đồ thị – khử ẩn số", K, fig="n_dt_nuocda", cap="Đường nung nóng nước đá"),

sa("Ấm điện 1000 W đun 1,0 kg nước từ 25 °C; sau 5 phút nước đạt 80 °C. Hiệu suất của ấm bằng bao nhiêu "
   "phần trăm?",
   "77",
   "Q_i = 1,0·4200·55 = 231 000 J; W = 1000·300 = 300 000 J ⟹ H = 231/300 = 77%.",
   "Hiệu suất", TB),

sa("Cần thả bao nhiêu gam nước đá ở 0 °C vào 0,50 kg nước ở 60 °C để nước đá vừa vặn tan hết và nhiệt độ "
   "hỗn hợp bằng đúng 0 °C? (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K); làm tròn đến hàng đơn vị)",
   "371",
   "m·λ = 0,50·4200·60 = 126 000 J ⟹ m = 126 000/3,4·10⁵ ≈ 0,371 kg = 371 g.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Một tấm pin mặt trời diện tích 2,0 m² nhận công suất bức xạ 800 W/m², trong đó 25% dùng để đun nước. "
   "Sau 1 giờ có thể đun được bao nhiêu kilôgam nước nóng thêm 40 °C (làm tròn đến chữ số thập phân thứ "
   "nhất)?",
   "8,6",
   "P_ci = 0,25·800·2,0 = 400 W ⟹ Q = 400·3600 = 1 440 000 J.\n"
   "m = Q/(cΔt) = 1 440 000/(4200·40) ≈ 8,6 kg.",
   "Nhiệt dung riêng – năng lượng tái tạo", K),
])


# =====================================================================
DE8 = dict(
ma="12C1-Đ08", ten="ĐỀ SỐ 8", muc="Trung bình → Khó",
trongtam="Hệ nhiều vật và nhiều giai đoạn chuyển thể; biện luận điều kiện; bài toán ngược",
P1=[
mc("Hơi nước ở 100 °C gây bỏng nặng hơn nước lỏng ở 100 °C. Nguyên nhân là",
   ["hơi nước có nhiệt độ cao hơn nước lỏng.",
    "khi ngưng tụ trên da, mỗi kilôgam hơi nước còn giải phóng thêm 2,26·10⁶ J.",
    "hơi nước có nhiệt dung riêng lớn hơn nước lỏng.",
    "hơi nước dẫn nhiệt tốt hơn nước lỏng."],
   "B",
   "Cả hai cùng ở 100 °C. Nhưng hơi nước còn phải NGƯNG TỤ trên da, và quá trình ngưng tụ giải phóng "
   "nhiệt hoá hơi riêng — một lượng năng lượng rất lớn so với nhiệt lượng do nước nguội đi.",
   "Nhiệt hoá hơi riêng – thực tiễn", TB),

mc("Dẫn 20 g hơi nước ở 100 °C vào một bình cách nhiệt chứa 200 g nước đá ở 0 °C. Cho "
   "L = 2,26·10⁶ J/kg, λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng nhiệt là",
   ["0 °C.", "8,4 °C.", "17,5 °C.", "25,0 °C."],
   "A",
   "Nhiệt lượng tối đa hơi nước có thể nhường (ngưng tụ rồi nguội tới 0 °C):\n"
   "Q_toả = 0,020 · 2,26·10⁶ + 0,020 · 4200 · 100 = 45 200 + 8400 = 53 600 J.\n"
   "Nhiệt lượng cần để làm tan hết 200 g đá: 0,200 · 3,4·10⁵ = 68 000 J.\n"
   "Vì 53 600 J < 68 000 J nên nước đá chỉ tan một phần ⟹ trong bình còn cả đá và nước ⟹ t = 0 °C.",
   "Cân bằng nhiệt nhiều giai đoạn", K),

mc("Với dữ kiện ở câu trên, khối lượng nước đá còn lại khi cân bằng nhiệt gần nhất với",
   ["12 g.", "42 g.", "78 g.", "158 g."],
   "B",
   "Khối lượng đá đã tan: Δm = 53 600/3,4·10⁵ ≈ 0,1576 kg ≈ 158 g.\n"
   "Đá còn lại: 200 − 158 = 42 g. (158 g là bẫy — đó là phần đã TAN chứ không phải phần còn lại.)",
   "Cân bằng nhiệt nhiều giai đoạn", K),

mc("Có 0,40 kg nước ở 50 °C trong bình cách nhiệt lí tưởng. Thả vào đó nước đá ở −20 °C. Khối lượng nước "
   "đá LỚN NHẤT có thể tan hết hoàn toàn là (c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg)",
   ["176 g.", "198 g.", "220 g.", "247 g."],
   "C",
   "Nước chỉ có thể toả tối đa Q = 0,40 · 4200 · 50 = 84 000 J (khi hạ tới 0 °C).\n"
   "Mỗi kilôgam nước đá cần: 2100 · 20 + 3,4·10⁵ = 42 000 + 340 000 = 382 000 J để vừa nóng lên tới "
   "0 °C vừa tan hết.\n"
   "m_max = 84 000/382 000 ≈ 0,220 kg = 220 g.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Trộn 1,0 kg nước ở 20 °C với 0,50 kg nhôm và 0,50 kg đồng, cả hai kim loại đều đang ở 100 °C, trong "
   "bình cách nhiệt lí tưởng. Cho c_nhôm = 880, c_đồng = 380, c_nước = 4200 J/(kg·K). Nhiệt độ khi cân "
   "bằng gần nhất với",
   ["26,8 °C.", "30,4 °C.", "35,2 °C.", "42,0 °C."],
   "B",
   "Hai kim loại cùng toả nhiệt, cộng “nhiệt dung” của chúng lại:\n"
   "(0,50 · 880 + 0,50 · 380)(100 − t) = 1,0 · 4200 · (t − 20)\n"
   "⟹ 630(100 − t) = 4200(t − 20) ⟹ 63 000 − 630t = 4200t − 84 000\n"
   "⟹ 4830t = 147 000 ⟹ t ≈ 30,4 °C.",
   "Cân bằng nhiệt hệ nhiều vật", K),

mc("Trong đường nung nóng nước đá ở hình bên, tỉ số giữa nhiệt lượng cung cấp ở giai đoạn đun nước "
   "(0 → 100 °C) và nhiệt lượng cung cấp ở giai đoạn làm nóng nước đá (−20 → 0 °C) bằng",
   ["2.", "5.", "8.", "10."],
   "D",
   "Cùng công suất nên nhiệt lượng tỉ lệ thuận với thời gian:\n"
   "Q₃/Q₁ = t₃/t₁ = (950 − 450)/50 = 500/50 = 10.\n"
   "(Kiểm tra bằng số liệu: (4200 · 100)/(2100 · 20) = 420 000/42 000 = 10 ✓)",
   "Đọc đồ thị – lập tỉ số", K, fig="n_dt_nuocda",
   cap="Đường nung nóng 0,50 kg nước đá"),

mc("Một ấm điện đun 2,0 kg nước từ 20 °C. Sau 8 phút nước sôi. Nếu hiệu suất của ấm là 80% thì công suất "
   "của ấm là",
   ["1050 W.", "1400 W.", "1750 W.", "2100 W."],
   "C",
   "Q_i = 2,0 · 4200 · 80 = 672 000 J trong 480 s ⟹ công suất có ích P_ci = 672 000/480 = 1400 W.\n"
   "P = P_ci/H = 1400/0,80 = 1750 W.",
   "Hiệu suất – bài toán ngược", TB),

mc("Một khối khí thực hiện một chu trình kín rồi trở về đúng trạng thái ban đầu. Trong cả chu trình đó",
   ["nhiệt lượng khí nhận vào bằng 0.", "công khí sinh ra bằng 0.",
    "độ biến thiên nội năng bằng 0.", "cả ba đại lượng trên đều bằng 0."],
   "C",
   "Nội năng là hàm của trạng thái: trở về trạng thái ban đầu thì ΔU = 0. Khi đó A + Q = 0, nghĩa là công "
   "và nhiệt lượng có độ lớn bằng nhau nhưng nói chung KHÁC 0.",
   "Định luật I – chu trình", K),

mc("Muốn xác định nhiệt hoá hơi riêng của nước bằng thực nghiệm, cách làm hợp lí nhất là",
   ["đo nhiệt độ sôi của nước rồi tra bảng.",
    "đun nước đã sôi bằng thiết bị công suất P đã biết trong thời gian t, cân lượng nước đã hoá hơi.",
    "đo khối lượng nước trước và sau khi đun rồi chia cho thời gian.",
    "đo nhiệt độ nước trước và sau khi đun."],
   "B",
   "Khi nước ĐÃ SÔI, toàn bộ nhiệt lượng cung cấp dùng cho hoá hơi (nhiệt độ không đổi). Do đó "
   "L = P·t/Δm, chỉ cần đo công suất, thời gian và khối lượng nước đã bay hơi.",
   "Thiết kế thí nghiệm", K),

mc("Cho 100 g nước ở 20 °C và 100 g nước đá ở 0 °C vào bình cách nhiệt. Trạng thái cuối của hệ là",
   ["nước ở 10 °C.", "nước ở 0 °C, đá tan hết.",
    "hỗn hợp nước và nước đá ở 0 °C.", "nước đá ở 0 °C."],
   "C",
   "Nước toả tối đa 0,100 · 4200 · 20 = 8400 J; làm tan hết 100 g đá cần 34 000 J.\n"
   "Vì 8400 J < 34 000 J nên đá chỉ tan khoảng 24,7 g ⟹ trong bình còn cả nước và đá ở 0 °C.",
   "Cân bằng nhiệt – biện luận", K),

mc("Nhiệt lượng cần để đun sôi rồi làm bay hơi hoàn toàn 0,50 kg nước ban đầu ở 20 °C là "
   "(c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg)",
   ["1130,0 kJ.", "1198,0 kJ.", "1298,0 kJ.", "1465,0 kJ."],
   "C",
   "Q₁ = 0,50 · 4200 · 80 = 168 000 J (đun tới 100 °C).\n"
   "Q₂ = 0,50 · 2,26·10⁶ = 1 130 000 J (hoá hơi).\n"
   "Q = 1 298 000 J = 1298 kJ.",
   "Bài toán nhiệt nhiều giai đoạn", TB),

mc("Một hệ nhận công 250 J và toả ra nhiệt lượng 250 J. Nội năng của hệ",
   ["tăng 500 J.", "giảm 500 J.", "không đổi.", "tăng 250 J."],
   "C", "ΔU = A + Q = (+250) + (−250) = 0.", "Định luật I nhiệt động lực học", TB),

mc("Khi đun một chất lỏng, nếu tăng gấp đôi khối lượng chất lỏng đồng thời tăng gấp đôi công suất thiết "
   "bị thì thời gian để chất lỏng tăng thêm cùng một lượng nhiệt độ sẽ",
   ["tăng 4 lần.", "tăng 2 lần.", "không đổi.", "giảm 2 lần."],
   "C",
   "t = mcΔT/P. Khi m và P cùng tăng gấp đôi thì tỉ số m/P không đổi ⟹ thời gian không đổi.",
   "Suy luận tỉ lệ", TB),

mc("Trong bình cách nhiệt có 0,20 kg nước ở 0 °C và 0,20 kg nước đá ở 0 °C. Nếu cung cấp cho hệ 34 kJ thì "
   "trạng thái cuối là (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["0,40 kg nước ở 0 °C.", "0,40 kg nước ở 20 °C.",
    "0,30 kg nước và 0,10 kg đá ở 0 °C.", "0,40 kg nước ở 40 °C."],
   "C",
   "Nhiệt lượng cần để làm tan hết 0,20 kg đá là 0,20 · 3,4·10⁵ = 68 000 J, lớn hơn 34 000 J được cung "
   "cấp ⟹ đá chỉ tan một phần.\n"
   "Khối lượng đá tan: Δm = 34 000/3,4·10⁵ = 0,10 kg.\n"
   "Trạng thái cuối: 0,20 + 0,10 = 0,30 kg nước và 0,10 kg đá còn lại, tất cả ở 0 °C (chừng nào còn đá "
   "thì nhiệt độ không thể vượt quá 0 °C).",
   "Cân bằng nhiệt – biện luận", K),

mc("Người ta cần làm nguội 5,0 kg nước từ 80 °C xuống 40 °C bằng cách cho nước lạnh ở 20 °C chảy qua bộ "
   "trao đổi nhiệt. Khối lượng nước lạnh cần dùng là",
   ["5,0 kg.", "10,0 kg.", "15,0 kg.", "20,0 kg."],
   "B",
   "Nước nóng toả: 5,0 · 4200 · (80 − 40) = 840 000 J.\n"
   "Nước lạnh thu, nóng lên tới 40 °C: m · 4200 · (40 − 20) = 84 000m.\n"
   "⟹ 84 000m = 840 000 ⟹ m = 10,0 kg.",
   "Cân bằng nhiệt – thực tiễn", TB),

mc("Phát biểu nào sau đây về nhiệt nóng chảy riêng là ĐÚNG?",
   ["Nhiệt nóng chảy riêng phụ thuộc vào khối lượng của vật.",
    "Nhiệt nóng chảy riêng của mọi chất đều bằng nhau.",
    "Nhiệt nóng chảy riêng của một chất bằng nhiệt lượng cần để làm nóng chảy hoàn toàn 1 kg chất đó ở "
    "nhiệt độ nóng chảy.",
    "Nhiệt nóng chảy riêng có đơn vị J/(kg·K)."],
   "C",
   "Đó chính là định nghĩa. λ là hằng số của chất (không phụ thuộc khối lượng) và có đơn vị J/kg.",
   "Nhiệt nóng chảy riêng", D),

mc("Một động cơ nhiệt nhận 1000 J nhiệt lượng từ nguồn nóng, sinh công 300 J và thải phần còn lại cho "
   "nguồn lạnh. Nhiệt lượng thải ra là",
   ["300 J.", "500 J.", "700 J.", "1000 J."],
   "C",
   "Sau mỗi chu trình động cơ trở về trạng thái đầu nên ΔU = 0, do đó năng lượng được bảo toàn:\n"
   "Q_thải = Q_nhận − A_sinh = 1000 − 300 = 700 J.",
   "Định luật I – động cơ nhiệt", TB),

mc("Vì sao khi trời rét, người ta thường phun nước lên ruộng mạ để chống rét cho cây?",
   ["Nước làm cây hấp thụ được nhiều ánh sáng hơn.",
    "Nước có nhiệt dung riêng lớn nên nguội chậm, và khi đông đặc còn toả nhiệt giữ ấm cho cây.",
    "Nước ngăn không cho không khí lạnh tiếp xúc với cây.",
    "Nước làm tăng nhiệt độ không khí xung quanh cây."],
   "B",
   "Hai cơ chế: nhiệt dung riêng lớn nên lớp nước nguội chậm, giữ nhiệt độ ổn định; và nếu nhiệt độ hạ "
   "tới 0 °C, quá trình đông đặc còn TOẢ nhiệt (3,4·10⁵ J cho mỗi kilôgam nước), giữ cho cây không bị "
   "hạ xuống dưới 0 °C.",
   "Nhiệt dung riêng – nhiệt nóng chảy riêng – thực tiễn", K),
],
P2=[
ds("Dẫn 50 g hơi nước ở 100 °C vào một bình cách nhiệt chứa 1,0 kg nước ở 20 °C. Cho "
   "L = 2,26·10⁶ J/kg, c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng hơi nước toả ra khi ngưng tụ hoàn toàn ở 100 °C là 113 kJ.", True,
     "Đúng. Q = 0,050 · 2,26·10⁶ = 113 000 J = 113 kJ."),
    ("Khi cân bằng nhiệt, trong bình có 1,05 kg nước.", True,
     "Đúng. Toàn bộ hơi nước ngưng tụ thành nước: 1,0 + 0,050 = 1,05 kg."),
    ("Nhiệt độ khi cân bằng nhiệt xấp xỉ 49 °C.", True,
     "Đúng. 113 000 + 0,050 · 4200 · (100 − t) = 1,0 · 4200 · (t − 20)\n"
     "⟹ 113 000 + 21 000 + 84 000 = 4410t ⟹ t = 218 000/4410 ≈ 49,4 °C."),
    ("Nếu thay 50 g hơi nước bằng 50 g nước lỏng ở 100 °C thì nhiệt độ cân bằng vẫn như vậy.", False,
     "Sai. Nước lỏng không có nhiệt ngưng tụ nên chỉ toả 0,050 · 4200 · (100 − t) J:\n"
     "0,050(100 − t) = t − 20 ⟹ 25 = 1,05t ⟹ t ≈ 23,8 °C, thấp hơn hẳn 49 °C. "
     "Đó chính là lí do hơi nước gây bỏng nặng hơn nước sôi.")],
   "Cân bằng nhiệt nhiều giai đoạn", K),

ds("Trong bình cách nhiệt lí tưởng có 0,40 kg nước ở 50 °C. Người ta thả vào đó nước đá ở −20 °C với "
   "những khối lượng khác nhau. Cho c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng lớn nhất mà nước có thể nhường là 84 kJ.", True,
     "Đúng. Q = 0,40 · 4200 · 50 = 84 000 J khi nước hạ tới 0 °C."),
    ("Để làm tan hết 1 kg nước đá ở −20 °C cần 382 kJ.", True,
     "Đúng. Q = 1 · 2100 · 20 + 1 · 3,4·10⁵ = 42 000 + 340 000 = 382 000 J."),
    ("Khối lượng nước đá lớn nhất có thể tan hết hoàn toàn là khoảng 220 g.", True,
     "Đúng. m_max = 84 000/382 000 ≈ 0,220 kg."),
    ("Nếu thả 100 g nước đá ở −20 °C thì nhiệt độ cân bằng của hệ là 0 °C.", False,
     "Sai. Với 100 g đá chỉ cần 38,2 kJ < 84 kJ nên đá tan hết và vẫn còn dư nhiệt; nhiệt độ cân bằng "
     "cao hơn 0 °C (khoảng 21,8 °C).")],
   "Cân bằng nhiệt – biện luận theo khối lượng", K),

ds("Một ấm điện được dùng để đun 2,0 kg nước từ 20 °C; sau 8 phút thì nước sôi. Hiệu suất của ấm là 80%. "
   "Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
   [("Công suất có ích của ấm là 1400 W.", True,
     "Đúng. Q_i = 2,0 · 4200 · 80 = 672 000 J trong 480 s ⟹ P_ci = 1400 W."),
    ("Công suất định mức của ấm là 1750 W.", True,
     "Đúng. P = P_ci/H = 1400/0,80 = 1750 W."),
    ("Điện năng ấm tiêu thụ trong 8 phút là 840 kJ.", True,
     "Đúng. W = P·t = 1750 · 480 = 840 000 J = 840 kJ (trong đó 672 kJ là có ích, 168 kJ hao phí)."),
    ("Nếu để quên ấm thêm 10 phút sau khi nước sôi thì lượng nước hoá hơi khoảng 0,80 kg.", False,
     "Sai. Nhiệt lượng có ích thêm: 1400 · 600 = 840 000 J ⟹ m = 840 000/2,26·10⁶ ≈ 0,37 kg, "
     "tức khoảng 0,37 kg chứ không phải 0,80 kg.")],
   "Hiệu suất – nhiệt hoá hơi riêng", K),

ds("Xét việc vận dụng định luật I nhiệt động lực học cho các quá trình.",
   [("Sau một chu trình kín, độ biến thiên nội năng của hệ bằng 0 nên công và nhiệt lượng của hệ có độ "
     "lớn bằng nhau.", True,
     "Đúng. ΔU = 0 ⟹ A + Q = 0 ⟹ |A| = |Q| (nhưng trái dấu nhau)."),
    ("Một động cơ nhiệt nhận 1000 J từ nguồn nóng và sinh công 300 J thì thải cho nguồn lạnh 700 J.", True,
     "Đúng. Bảo toàn năng lượng cho một chu trình: Q_thải = 1000 − 300 = 700 J."),
    ("Có thể chế tạo động cơ nhiệt biến toàn bộ nhiệt lượng nhận được thành công.", False,
     "Sai. Thực nghiệm cho thấy động cơ nhiệt luôn phải thải một phần nhiệt lượng cho nguồn lạnh; hiệu "
     "suất luôn nhỏ hơn 100%."),
    ("Nếu một hệ nhận công 250 J và toả nhiệt 250 J thì nội năng của hệ không đổi.", True,
     "Đúng. ΔU = (+250) + (−250) = 0.")],
   "Định luật I – chu trình và động cơ nhiệt", K),
],
P3=[
sa("Dẫn 20 g hơi nước ở 100 °C vào bình cách nhiệt chứa 200 g nước đá ở 0 °C. Cho L = 2,26·10⁶ J/kg, "
   "λ = 3,4·10⁵ J/kg, c_nước = 4200 J/(kg·K). Khối lượng nước đá còn lại khi cân bằng nhiệt bằng bao nhiêu "
   "gam (làm tròn đến hàng đơn vị)?",
   "42",
   "Hơi nước nhường tối đa: 0,020·2,26·10⁶ + 0,020·4200·100 = 45 200 + 8400 = 53 600 J.\n"
   "Cần 68 000 J mới tan hết ⟹ tan một phần: Δm = 53 600/3,4·10⁵ ≈ 158 g.\n"
   "Đá còn lại: 200 − 158 = 42 g (hệ ở 0 °C).",
   "Cân bằng nhiệt nhiều giai đoạn", K),

sa("Có 0,40 kg nước ở 50 °C trong bình cách nhiệt. Khối lượng nước đá ở −20 °C lớn nhất có thể thả vào mà "
   "vẫn tan hết hoàn toàn bằng bao nhiêu gam (làm tròn đến hàng đơn vị)? Cho c_đá = 2100, "
   "c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   "220",
   "Nước nhường tối đa 0,40·4200·50 = 84 000 J.\n"
   "Mỗi kg đá ở −20 °C cần 2100·20 + 3,4·10⁵ = 382 000 J để tan hết.\n"
   "m_max = 84 000/382 000 ≈ 0,220 kg = 220 g.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Trộn 1,0 kg nước ở 20 °C với 0,50 kg nhôm và 0,50 kg đồng cùng đang ở 100 °C trong bình cách nhiệt. "
   "Cho c_nhôm = 880, c_đồng = 380, c_nước = 4200 J/(kg·K). Nhiệt độ khi cân bằng bằng bao nhiêu độ C "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "30,4",
   "(0,50·880 + 0,50·380)(100 − t) = 1,0·4200·(t − 20)\n"
   "⟹ 630(100 − t) = 4200(t − 20) ⟹ 4830t = 147 000 ⟹ t ≈ 30,4 °C.",
   "Cân bằng nhiệt hệ nhiều vật", K),

sa("Một ấm điện đun 2,0 kg nước từ 20 °C, sau 8 phút thì nước sôi. Hiệu suất của ấm là 80%. Công suất "
   "định mức của ấm bằng bao nhiêu oát?",
   "1750",
   "P_ci = 2,0·4200·80/480 = 1400 W ⟹ P = 1400/0,80 = 1750 W.",
   "Hiệu suất – bài toán ngược", TB),

sa("Cần làm nguội 5,0 kg nước từ 80 °C xuống 40 °C bằng nước lạnh ở 20 °C. Khối lượng nước lạnh cần dùng "
   "bằng bao nhiêu kilôgam?",
   "10",
   "5,0·4200·40 = m·4200·20 ⟹ 840 000 = 84 000m ⟹ m = 10,0 kg.",
   "Cân bằng nhiệt – thực tiễn", TB),

sa("Trong đường nung nóng nước đá ở hình bên, tỉ số giữa nhiệt lượng làm tan hoàn toàn khối nước đá và "
   "nhiệt lượng làm nóng chính khối nước đá đó từ −20 °C lên 0 °C bằng bao nhiêu?",
   "8",
   "Cùng công suất nên nhiệt lượng tỉ lệ thuận với thời gian.\n"
   "Đoạn nằm ngang (nóng chảy) kéo dài 450 − 50 = 400 s; đoạn hâm nước đá kéo dài 50 s.\n"
   "Q(tan)/Q(hâm) = 400/50 = 8.\n"
   "(Kiểm tra bằng số liệu: 3,36·10⁵/(2100 · 20) = 336 000/42 000 = 8 ✓)",
   "Đọc đồ thị – lập tỉ số", K, fig="n_dt_nuocda", cap="Đường nung nóng nước đá"),
])


# =====================================================================
DE9 = dict(
ma="12C1-Đ09", ten="ĐỀ SỐ 9", muc="Khó",
trongtam="Tách công suất hao phí; xử lí số liệu thực nghiệm; quá trình nhiều bước và suy luận ngược",
P1=[
mc("Một thiết bị đun có công suất P không đổi, đồng thời hao phí ra môi trường một công suất P_hp coi như "
   "không đổi. Đun 1,0 kg nước từ 20 °C, sau 200 s nước đạt 40 °C. Tắt thiết bị, nước nguội từ 40 °C "
   "xuống 39 °C mất 42 s. Công suất hao phí P_hp bằng",
   ["42 W.", "100 W.", "150 W.", "420 W."],
   "B",
   "Khi đã tắt thiết bị, nguyên nhân duy nhất làm nước nguội là hao phí ra môi trường:\n"
   "P_hp · t = m·c·ΔT ⟹ P_hp = 1,0 · 4200 · 1/42 = 100 W.\n"
   "Đây là mẹo tách hao phí: dùng chính giai đoạn NGUỘI để đo công suất hao phí.",
   "Tách công suất hao phí", RK),

mc("Vẫn với thiết bị ở câu trên, công suất P của thiết bị đun bằng",
   ["420 W.", "480 W.", "520 W.", "620 W."],
   "C",
   "Trong giai đoạn đun, chỉ phần công suất (P − P_hp) làm nóng nước:\n"
   "(P − P_hp)·200 = 1,0 · 4200 · 20 = 84 000 J ⟹ P − 100 = 420 ⟹ P = 520 W.",
   "Tách công suất hao phí", RK),

mc("Một nhiệt lượng kế có nhiệt dung 100 J/K chứa 300 g nước, cả bình và nước ở 30 °C. Thả vào đó 50 g "
   "nước đá ở 0 °C thì nhiệt độ cân bằng đo được là 15,2 °C. Nhiệt nóng chảy riêng của nước đá xác định "
   "từ thí nghiệm này gần nhất với",
   ["2,4·10⁵ J/kg.", "2,9·10⁵ J/kg.", "3,4·10⁵ J/kg.", "4,0·10⁵ J/kg."],
   "C",
   "Vế toả nhiệt (nước và bình cùng hạ từ 30 °C xuống 15,2 °C):\n"
   "Q_toả = (0,300 · 4200 + 100)(30 − 15,2) = 1360 · 14,8 = 20 128 J.\n"
   "Vế thu nhiệt (đá tan rồi nước tạo thành nóng lên tới 15,2 °C):\n"
   "Q_thu = 0,050·λ + 0,050 · 4200 · 15,2 = 0,050λ + 3192.\n"
   "⟹ 0,050λ = 16 936 ⟹ λ ≈ 3,39·10⁵ J/kg ≈ 3,4·10⁵ J/kg.",
   "Thí nghiệm xác định nhiệt nóng chảy riêng", RK,
   fig="n_sd_nhietluongke", cap="Nhiệt lượng kế dùng trong thí nghiệm"),

mc("Để làm nguội nhanh một cốc nước, thả vào cốc mấy viên nước đá ở 0 °C có hiệu quả hơn hẳn so với rót "
   "thêm cùng khối lượng nước lỏng ở 0 °C, chủ yếu vì",
   ["nước đá có nhiệt dung riêng lớn hơn nước lỏng.",
    "nước đá thu thêm một nhiệt lượng lớn để nóng chảy mà nhiệt độ vẫn giữ nguyên 0 °C.",
    "nước đá dẫn nhiệt tốt hơn nước lỏng.",
    "nước đá có khối lượng riêng nhỏ hơn nước lỏng."],
   "B",
   "Mỗi kilôgam nước đá ở 0 °C phải nhận thêm λ = 3,4·10⁵ J để tan hết, trong khi cùng khối lượng nước "
   "lỏng ở 0 °C khi nóng lên tới t chỉ nhận 4200·t J.\n"
   "Ngay cả khi nước trong cốc ở 50 °C thì phần nhiệt nước lỏng nhận được cũng chỉ khoảng "
   "4200 · 50 = 2,1·10⁵ J, nhỏ hơn nhiệt nóng chảy. Vì vậy nước đá “rút” được nhiều nhiệt hơn.\n"
   "Các phương án còn lại đều không phải nguyên nhân chính: nhiệt dung riêng của nước đá còn NHỎ hơn "
   "của nước lỏng.",
   "Nhiệt nóng chảy riêng – thực tiễn", TB),

mc("Để đun 10 kg nước từ 20 °C lên 60 °C, người ta dẫn hơi nước ở 100 °C vào. Hơi ngưng tụ rồi hoà cùng "
   "khối nước. Khối lượng hơi nước cần dùng gần nhất với (L = 2,26·10⁶ J/kg, c = 4200 J/(kg·K))",
   ["0,58 kg.", "0,69 kg.", "0,74 kg.", "0,83 kg."],
   "B",
   "Nhiệt lượng cần cho 10 kg nước: Q = 10 · 4200 · 40 = 1 680 000 J.\n"
   "Mỗi kilôgam hơi nhường: 2,26·10⁶ (ngưng tụ) + 4200 · (100 − 60) = 2 260 000 + 168 000 = "
   "2 428 000 J.\n"
   "m = 1 680 000/2 428 000 ≈ 0,69 kg. (Bẫy: quên giai đoạn nước ngưng tụ nguội từ 100 °C xuống 60 °C.)",
   "Trao đổi nhiệt bằng hơi nước", K),

mc("Có 0,50 kg nước ở nhiệt độ t và 0,50 kg nước đá ở 0 °C trong bình cách nhiệt. Để đúng một nửa khối "
   "lượng nước đá tan ra thì t phải bằng (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["30,5 °C.", "35,0 °C.", "40,5 °C.", "45,0 °C."],
   "C",
   "Muốn đá tan đúng một nửa thì nhiệt độ cuối là 0 °C và nhiệt lượng nước nhường vừa đủ làm tan 0,25 kg:\n"
   "0,50 · 4200 · t = 0,25 · 3,4·10⁵ = 85 000 J ⟹ 2100t = 85 000 ⟹ t ≈ 40,5 °C.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Một khối khí thực hiện quá trình gồm hai chặng: chặng 1 nhận nhiệt 600 J và sinh công 200 J; chặng 2 "
   "toả nhiệt 300 J và nhận công 500 J. Độ biến thiên nội năng của khối khí sau cả hai chặng là",
   ["+200 J.", "+400 J.", "+600 J.", "+1000 J."],
   "C",
   "Chặng 1: ΔU₁ = −200 + 600 = +400 J. Chặng 2: ΔU₂ = +500 − 300 = +200 J.\n"
   "Tổng: ΔU = 400 + 200 = +600 J (nội năng là hàm trạng thái nên cộng được).",
   "Định luật I – quá trình nhiều chặng", K),

mc("Người ta đun 0,80 kg một chất lỏng chưa biết bằng thiết bị 500 W. Nhiệt độ chất lỏng tăng từ 25 °C "
   "lên 65 °C trong 128 s. Bỏ qua hao phí. Nhiệt dung riêng của chất lỏng là",
   ["1600 J/(kg·K).", "2000 J/(kg·K).", "2400 J/(kg·K).", "2800 J/(kg·K)."],
   "B",
   "Q = P·t = 500 · 128 = 64 000 J; ΔT = 40 K.\n"
   "c = Q/(m·ΔT) = 64 000/(0,80 · 40) = 64 000/32 = 2000 J/(kg·K).",
   "Nhiệt dung riêng", TB),

mc("Trong bình cách nhiệt chứa 0,60 kg nước ở 20 °C, người ta thả một vật kim loại khối lượng 0,20 kg ở "
   "100 °C. Sau khi cân bằng, thả tiếp một vật kim loại khác hoàn toàn giống hệt vật thứ nhất, cũng ở "
   "100 °C. Nhiệt độ cân bằng lần thứ hai so với lần thứ nhất sẽ",
   ["tăng thêm đúng bằng độ tăng của lần thứ nhất.",
    "tăng thêm ít hơn độ tăng của lần thứ nhất.",
    "tăng thêm nhiều hơn độ tăng của lần thứ nhất.",
    "không thay đổi."],
   "B",
   "Ở lần thứ hai, nước trong bình đã nóng hơn nên chênh lệch nhiệt độ giữa vật và nước nhỏ hơn, do đó "
   "nhiệt lượng vật nhường được ít hơn. Ngoài ra khối lượng “nước + vật cũ” đã lớn hơn nên cùng một nhiệt "
   "lượng cũng làm nhiệt độ tăng ít hơn. Cả hai lí do đều dẫn tới độ tăng nhỏ hơn.",
   "Cân bằng nhiệt – suy luận định tính", K),

mc("Đun nóng đẳng áp một khối khí lí tưởng, khí nhận nhiệt lượng 1000 J và giãn nở sinh công 400 J. "
   "Nếu đun chính khối khí đó từ cùng trạng thái đầu tới cùng nhiệt độ cuối nhưng giữ thể tích không đổi "
   "thì nhiệt lượng cần cung cấp là",
   ["400 J.", "600 J.", "1000 J.", "1400 J."],
   "B",
   "Quá trình đẳng áp: ΔU = A + Q = −400 + 1000 = 600 J.\n"
   "Nội năng chỉ phụ thuộc nhiệt độ, mà nhiệt độ đầu và cuối như nhau nên ΔU vẫn là 600 J.\n"
   "Quá trình đẳng tích: A = 0 ⟹ Q = ΔU = 600 J.",
   "Định luật I – so sánh hai quá trình", RK),

mc("Một cốc cách nhiệt chứa 200 g nước ở 25 °C. Người ta thả vào lần lượt từng viên đá 20 g ở 0 °C, mỗi "
   "lần chờ cân bằng rồi mới thả viên tiếp theo. Số viên đá nhiều nhất có thể tan hết hoàn toàn là "
   "(λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["2 viên.", "3 viên.", "4 viên.", "5 viên."],
   "B",
   "Thả từng viên hay thả cùng lúc đều cho kết quả như nhau vì hệ cách nhiệt. Nước nhường tối đa "
   "Q = 0,200 · 4200 · 25 = 21 000 J.\n"
   "Mỗi viên đá cần 0,020 · 3,4·10⁵ = 6800 J để tan hết.\n"
   "Số viên tan hết: 21 000/6800 ≈ 3,09 ⟹ 3 viên tan hết, viên thứ tư chỉ tan một phần.",
   "Cân bằng nhiệt – biện luận", K),

mc("Hai chất lỏng A và B có khối lượng bằng nhau, nhiệt dung riêng c_A = 2c_B. Trộn A ở 20 °C với B ở "
   "80 °C trong bình cách nhiệt. Nhiệt độ cân bằng là",
   ["35 °C.", "40 °C.", "50 °C.", "60 °C."],
   "B",
   "m·c_A(t − 20) = m·c_B(80 − t) ⟹ 2c_B(t − 20) = c_B(80 − t)\n"
   "⟹ 2t − 40 = 80 − t ⟹ 3t = 120 ⟹ t = 40 °C.\n"
   "Nhiệt độ cân bằng lệch về phía chất có “nhiệt dung” lớn hơn (chất A).",
   "Cân bằng nhiệt – so sánh nhiệt dung riêng", K),

mc("Một máy lạnh lấy đi 500 J nhiệt lượng từ trong tủ và tiêu thụ 150 J điện năng trong mỗi chu trình. "
   "Nhiệt lượng máy thải ra môi trường bên ngoài mỗi chu trình là",
   ["350 J.", "500 J.", "650 J.", "750 J."],
   "C",
   "Sau mỗi chu trình môi chất trở về trạng thái đầu nên ΔU = 0; năng lượng được bảo toàn:\n"
   "Q_thải = Q_lấy vào + A_tiêu thụ = 500 + 150 = 650 J.\n"
   "Đó là lí do mở cửa tủ lạnh làm phòng NÓNG lên chứ không mát đi.",
   "Định luật I – máy lạnh", K),

mc("Nhiệt độ của một vật giảm đi trong khi vật vẫn nhận nhiệt lượng từ bên ngoài. Điều này có thể xảy ra khi",
   ["vật đang nóng chảy.", "vật đồng thời sinh công lớn hơn nhiệt lượng nhận vào.",
    "vật có nhiệt dung riêng âm.", "điều này không bao giờ xảy ra."],
   "B",
   "Từ ΔU = A + Q: nếu công vật sinh ra (A < 0) lớn hơn nhiệt lượng nhận vào (Q > 0) thì ΔU < 0, nội năng "
   "và nhiệt độ giảm. Trong khi nóng chảy nhiệt độ KHÔNG đổi chứ không giảm.",
   "Định luật I – phân tích tình huống", RK),

mc("Đổ 300 g nước ở 90 °C vào một cốc thuỷ tinh khối lượng 200 g đang ở 25 °C. Cho c_thuỷ tinh = "
   "840 J/(kg·K), c_nước = 4200 J/(kg·K), bỏ qua trao đổi nhiệt với môi trường. Nhiệt độ cuối gần nhất với",
   ["78,6 °C.", "82,4 °C.", "85,1 °C.", "87,9 °C."],
   "B",
   "0,300 · 4200 · (90 − t) = 0,200 · 840 · (t − 25)\n"
   "⟹ 1260(90 − t) = 168(t − 25) ⟹ 113 400 − 1260t = 168t − 4200\n"
   "⟹ 1428t = 117 600 ⟹ t ≈ 82,4 °C.\n"
   "Chú ý: nếu bỏ qua nhiệt lượng mà cốc thuỷ tinh thu vào thì nước sẽ giữ nguyên 90 °C — các phương án "
   "78,6 °C và 85,1 °C ứng với việc dùng sai khối lượng hoặc sai nhiệt dung riêng của cốc.",
   "Cân bằng nhiệt có vỏ bình", K),

mc("Trong một quá trình, nội năng của khối khí không đổi. Kết luận nào sau đây CHẮC CHẮN đúng?",
   ["Khối khí không trao đổi nhiệt với bên ngoài.",
    "Khối khí không trao đổi công với bên ngoài.",
    "Công và nhiệt lượng mà khối khí nhận được có tổng bằng 0.",
    "Thể tích khối khí không đổi."],
   "C",
   "ΔU = 0 chỉ cho biết A + Q = 0. Khối khí vẫn có thể vừa nhận nhiệt vừa sinh công (quá trình đẳng "
   "nhiệt), nên ba kết luận còn lại đều không chắc chắn.",
   "Định luật I nhiệt động lực học", K),

mc("Người ta muốn nâng nhiệt độ của 1,0 kg nước lên thêm 1 °C bằng cách khuấy. Nếu công suất khuấy là "
   "70 W và toàn bộ công chuyển thành nội năng của nước thì thời gian cần thiết là",
   ["30 s.", "45 s.", "60 s.", "90 s."],
   "C",
   "ΔU = mcΔT = 1,0 · 4200 · 1 = 4200 J. Bình cách nhiệt nên Q = 0, ΔU = A = P·t.\n"
   "t = 4200/70 = 60 s.",
   "Định luật I – thực hiện công", TB),

mc("Trong bốn quá trình sau, quá trình nào KHÔNG làm thay đổi nội năng của một lượng khí lí tưởng xác định?",
   ["Nén đoạn nhiệt.", "Đun nóng đẳng tích.",
    "Giãn nở đẳng nhiệt.", "Đun nóng đẳng áp."],
   "C",
   "Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ. Đẳng nhiệt ⟹ T không đổi ⟹ ΔU = 0. Ba quá trình còn "
   "lại đều làm nhiệt độ thay đổi.",
   "Nội năng khí lí tưởng", K),
],
P2=[
ds("Một thiết bị đun có công suất P không đổi, hao phí ra môi trường công suất P_hp coi như không đổi. "
   "Đun 1,0 kg nước từ 20 °C, sau 200 s nước đạt 40 °C. Tắt thiết bị, nước nguội từ 40 °C xuống 39 °C "
   "trong 42 s. Cho c_nước = 4200 J/(kg·K).",
   [("Có thể xác định được công suất hao phí nhờ giai đoạn nước nguội đi.", True,
     "Đúng. Khi đã tắt thiết bị, nguyên nhân duy nhất làm nước nguội là hao phí, nên giai đoạn nguội "
     "chính là “phép đo” trực tiếp cho P_hp."),
    ("Công suất hao phí bằng 100 W.", True,
     "Đúng. P_hp = mcΔT/t = 1,0 · 4200 · 1/42 = 100 W."),
    ("Công suất của thiết bị đun bằng 420 W.", False,
     "Sai. 420 W là công suất CÓ ÍCH: (P − P_hp) = 4200 · 20/200 = 420 W. Công suất thiết bị là "
     "P = 420 + 100 = 520 W."),
    ("Hiệu suất của thiết bị trong giai đoạn đun vào khoảng 81%.", True,
     "Đúng. H = P_ci/P = 420/520 ≈ 0,808 ≈ 81%.")],
   "Tách công suất hao phí", RK),

ds("Một nhiệt lượng kế có nhiệt dung 100 J/K chứa 300 g nước, cả bình và nước ở 30 °C. Thả vào đó 50 g "
   "nước đá ở 0 °C, nhiệt độ cân bằng đo được là 15,2 °C. Cho c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng do nước và bình toả ra là 20 128 J.", True,
     "Đúng. Q = (0,300 · 4200 + 100)(30 − 15,2) = 1360 · 14,8 = 20 128 J."),
    ("Toàn bộ nước đá đã tan hết trong thí nghiệm này.", True,
     "Đúng. Nhiệt độ cân bằng 15,2 °C > 0 °C, điều đó chỉ xảy ra khi đá đã tan hết."),
    ("Nhiệt lượng dùng để làm nóng phần nước mới tan từ 0 °C lên 15,2 °C là 3192 J.", True,
     "Đúng. Q = 0,050 · 4200 · 15,2 = 3192 J."),
    ("Nhiệt nóng chảy riêng đo được trong thí nghiệm này vào khoảng 4,0·10⁵ J/kg.", False,
     "Sai. 0,050λ = 20 128 − 3192 = 16 936 ⟹ λ ≈ 3,39·10⁵ J/kg, tức khoảng 3,4·10⁵ J/kg — "
     "rất gần giá trị chuẩn của nước đá.")],
   "Thí nghiệm xác định nhiệt nóng chảy riêng", RK,
   fig="n_sd_nhietluongke", cap="Nhiệt lượng kế"),

ds("Bình 1 chứa 1,0 kg nước ở 80 °C, bình 2 chứa 1,0 kg nước ở 20 °C, cả hai đều cách nhiệt. Múc 0,5 kg "
   "nước từ bình 1 sang bình 2 và khuấy đều; sau đó múc 0,5 kg nước từ bình 2 trở lại bình 1.",
   [("Sau bước thứ nhất, nhiệt độ nước ở bình 2 là 40 °C.", True,
     "Đúng. t = (1,0 · 20 + 0,5 · 80)/1,5 = 60/1,5 = 40 °C."),
    ("Sau bước thứ hai, nhiệt độ nước ở bình 1 là 60 °C.", True,
     "Đúng. Bình 1 lúc này gồm 0,5 kg ở 80 °C và 0,5 kg ở 40 °C: t = (40 + 20)/1,0 = 60 °C."),
    ("Sau cả hai bước, hai bình có nhiệt độ bằng nhau.", False,
     "Sai. Bình 1 ở 60 °C còn bình 2 (còn lại 1,0 kg ở 40 °C) ở 40 °C — vẫn chênh nhau 20 °C. Muốn hai "
     "bình bằng nhau phải trộn toàn bộ, khi đó cả hai đều ở 50 °C."),
    ("Nếu lặp lại thao tác đó nhiều lần, nhiệt độ hai bình sẽ tiến dần tới 50 °C.", True,
     "Đúng. Mỗi lần trao đổi lại san bớt chênh lệch; sau vô số lần cả hệ tiến tới nhiệt độ cân bằng "
     "chung là trung bình 50 °C (tổng năng lượng của hệ không đổi).")],
   "Cân bằng nhiệt nhiều bước", K),

ds("Xét việc vận dụng định luật I nhiệt động lực học ΔU = A + Q cho khí lí tưởng.",
   [("Đun nóng đẳng áp một khối khí, khí nhận 1000 J và sinh công 400 J thì nội năng tăng 600 J.", True,
     "Đúng. ΔU = A + Q = −400 + 1000 = 600 J."),
    ("Vẫn khối khí đó, nếu đun đẳng tích từ cùng trạng thái đầu tới cùng nhiệt độ cuối thì cần cung cấp "
     "600 J.", True,
     "Đúng. Nội năng chỉ phụ thuộc nhiệt độ nên ΔU vẫn là 600 J; đẳng tích thì A = 0 nên Q = 600 J. "
     "Muốn đạt cùng nhiệt độ, quá trình đẳng áp luôn tốn nhiều nhiệt lượng hơn đẳng tích."),
    ("Một máy lạnh lấy 500 J từ trong tủ và tiêu thụ 150 J điện năng thì thải ra ngoài 350 J.", False,
     "Sai. Bảo toàn năng lượng cho một chu trình: Q_thải = 500 + 150 = 650 J. Toàn bộ điện năng tiêu thụ "
     "cũng bị thải ra ngoài cùng với nhiệt lấy từ tủ."),
    ("Nhiệt độ của một vật có thể giảm ngay cả khi vật đang nhận nhiệt lượng.", True,
     "Đúng, nếu vật đồng thời sinh công lớn hơn nhiệt lượng nhận vào: ΔU = A + Q < 0 khi |A| > Q.")],
   "Định luật I nhiệt động lực học", RK),
],
P3=[
sa("Một thiết bị đun công suất P không đổi, hao phí công suất P_hp không đổi. Đun 1,0 kg nước từ 20 °C, "
   "sau 200 s đạt 40 °C; tắt thiết bị thì nước nguội từ 40 °C xuống 39 °C trong 42 s. "
   "Công suất P của thiết bị bằng bao nhiêu oát? Cho c = 4200 J/(kg·K).",
   "520",
   "Giai đoạn nguội cho công suất hao phí: P_hp = 4200 · 1/42 = 100 W.\n"
   "Giai đoạn đun: (P − 100)·200 = 4200 · 20 = 84 000 ⟹ P − 100 = 420 ⟹ P = 520 W.",
   "Tách công suất hao phí", RK),

sa("Nhiệt lượng kế (nhiệt dung 100 J/K) chứa 300 g nước ở 30 °C; thả vào 50 g nước đá ở 0 °C thì nhiệt độ "
   "cân bằng là 15,2 °C. Nhiệt nóng chảy riêng của nước đá đo được bằng bao nhiêu (đơn vị 10⁵ J/kg, "
   "làm tròn đến chữ số thập phân thứ hai)?",
   "3,39",
   "(1260 + 100)(30 − 15,2) = 0,050λ + 0,050 · 4200 · 15,2\n"
   "⟹ 20 128 = 0,050λ + 3192 ⟹ 0,050λ = 16 936 ⟹ λ ≈ 3,39·10⁵ J/kg.",
   "Thí nghiệm xác định nhiệt nóng chảy riêng", RK),

sa("Bình 1 chứa 1,0 kg nước ở 80 °C, bình 2 chứa 1,0 kg nước ở 20 °C. Múc 0,5 kg từ bình 1 sang bình 2, "
   "khuấy đều, rồi múc 0,5 kg từ bình 2 trở lại bình 1. Nhiệt độ nước ở bình 1 lúc đó bằng bao nhiêu độ C?",
   "60",
   "Bước 1: bình 2 có t = (1,0·20 + 0,5·80)/1,5 = 40 °C.\n"
   "Bước 2: bình 1 có t = (0,5·80 + 0,5·40)/1,0 = 60 °C.",
   "Cân bằng nhiệt nhiều bước", K),

sa("Để đun 10 kg nước từ 20 °C lên 60 °C bằng cách dẫn hơi nước 100 °C vào, cần bao nhiêu kilôgam hơi "
   "nước (làm tròn đến chữ số thập phân thứ hai)? Cho L = 2,26·10⁶ J/kg, c = 4200 J/(kg·K).",
   "0,69",
   "Q_thu = 10 · 4200 · 40 = 1 680 000 J.\n"
   "Mỗi kg hơi nhường 2,26·10⁶ + 4200 · 40 = 2 428 000 J.\n"
   "m = 1 680 000/2 428 000 ≈ 0,69 kg.",
   "Trao đổi nhiệt bằng hơi nước", K),

sa("Có 0,50 kg nước ở nhiệt độ t và 0,50 kg nước đá ở 0 °C trong bình cách nhiệt. Để đúng một nửa lượng "
   "nước đá tan ra thì t bằng bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "40,5",
   "Nhiệt độ cuối là 0 °C; nước nhường vừa đủ để tan 0,25 kg đá:\n"
   "0,50 · 4200 · t = 0,25 · 3,4·10⁵ = 85 000 ⟹ t ≈ 40,5 °C.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Đổ 300 g nước ở 90 °C vào cốc thuỷ tinh 200 g đang ở 25 °C. Cho c_thuỷ tinh = 840, "
   "c_nước = 4200 J/(kg·K); bỏ qua trao đổi nhiệt với môi trường. Nhiệt độ cuối bằng bao nhiêu độ C "
   "(làm tròn đến chữ số thập phân thứ nhất)?",
   "82,4",
   "1260(90 − t) = 168(t − 25) ⟹ 113 400 − 1260t = 168t − 4200 ⟹ 1428t = 117 600 ⟹ t ≈ 82,4 °C.",
   "Cân bằng nhiệt có vỏ bình", K),
])


# =====================================================================
DE10 = dict(
ma="12C1-Đ10", ten="ĐỀ SỐ 10", muc="Khó / thử thách",
trongtam="Biện luận trạng thái cuối của hệ; suy luận ngược nhiều bước; tình huống nước có thể đông đặc",
P1=[
mc("Cần cung cấp nhiệt lượng bao nhiêu để biến hoàn toàn 250 g nước ở 20 °C thành hơi nước ở 100 °C? "
   "Cho c_nước = 4200 J/(kg·K); nhiệt hoá hơi riêng L = 2,3·10⁶ J/kg.",
   ["659 kJ.", "575 kJ.", "84 kJ.", "743 kJ."],
   "A",
   "Giai đoạn 1 – đun nóng: Q₁ = 0,250 · 4200 · 80 = 84 000 J.\n"
   "Giai đoạn 2 – hoá hơi: Q₂ = 0,250 · 2,3·10⁶ = 575 000 J.\n"
   "Q = 84 000 + 575 000 = 659 000 J = 659 kJ.\n"
   "Phương án 575 kJ ứng với việc quên giai đoạn đun nóng, 84 kJ ứng với việc quên giai đoạn hoá hơi.",
   "Nhiệt hoá hơi riêng – hai giai đoạn", K),

mc("Với dữ kiện ở câu trên, khối lượng nước đã đông đặc gần nhất với",
   ["62 g.", "98 g.", "124 g.", "160 g."],
   "C",
   "Gọi x là khối lượng nước đông đặc. Nhiệt lượng nước nhường (hạ tới 0 °C rồi đông đặc một phần) phải "
   "vừa đủ hâm khối đá lên 0 °C:\n"
   "42 000 + x · 3,4·10⁵ = 84 000 ⟹ x = 42 000/3,4·10⁵ ≈ 0,1235 kg ≈ 124 g.",
   "Biện luận trạng thái cuối – nước đông đặc", RK),

mc("Thả m kg nước đá ở −10 °C vào 1,0 kg nước ở 20 °C trong bình cách nhiệt. Để khi cân bằng nhiệt trong "
   "bình vẫn còn cả nước và nước đá (nhiệt độ 0 °C) thì m phải thoả mãn "
   "(c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg)",
   ["m ≥ 0,233 kg.", "m ≤ 0,233 kg.", "m ≥ 0,247 kg.", "m ≤ 4,00 kg."],
   "A",
   "Nước nhường tối đa Q = 1,0 · 4200 · 20 = 84 000 J.\n"
   "Muốn còn đá dư (đá KHÔNG tan hết) thì nhiệt lượng ấy không đủ để vừa hâm vừa làm tan hết đá:\n"
   "84 000 ≤ m(2100 · 10 + 3,4·10⁵) = 361 000m ⟹ m ≥ 84 000/361 000 ≈ 0,233 kg.\n"
   "(Điều kiện m ≤ 4 kg để nước không bị đông đặc cũng phải kiểm tra, nhưng nó tự thoả mãn trong mọi "
   "trường hợp thực tế của bài.)",
   "Biện luận điều kiện", RK),

mc("Thả 0,50 kg một kim loại ở nhiệt độ t vào 1,0 kg nước ở 20 °C trong bình cách nhiệt lí tưởng, nhiệt "
   "độ cân bằng là 25 °C. Cho c_kim loại = 460 J/(kg·K), c_nước = 4200 J/(kg·K). Giá trị của t gần nhất với",
   ["96 °C.", "108 °C.", "116 °C.", "132 °C."],
   "C",
   "0,50 · 460 · (t − 25) = 1,0 · 4200 · (25 − 20)\n"
   "⟹ 230(t − 25) = 21 000 ⟹ t − 25 ≈ 91,3 ⟹ t ≈ 116 °C.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Thả 0,20 kg nước đá ở 0 °C vào 0,50 kg nước ở nhiệt độ t. Nhiệt độ cân bằng là 10 °C. Giá trị của t "
   "gần nhất với (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["36,4 °C.", "42,0 °C.", "46,4 °C.", "52,8 °C."],
   "C",
   "Nước đá tan hết rồi nóng lên tới 10 °C:\n"
   "Q_thu = 0,20 · 3,4·10⁵ + 0,20 · 4200 · 10 = 68 000 + 8400 = 76 400 J.\n"
   "Q_toả = 0,50 · 4200 · (t − 10) = 2100(t − 10).\n"
   "⟹ t − 10 ≈ 36,4 ⟹ t ≈ 46,4 °C. (Phương án 36,4 °C là bẫy: đó chỉ là độ giảm nhiệt độ.)",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Một khối khí lí tưởng thực hiện chu trình gồm ba chặng. Chặng 1: nhận nhiệt 800 J, nội năng tăng "
   "500 J. Chặng 2: đẳng nhiệt, sinh công 400 J. Chặng 3 đưa khí về trạng thái đầu. Độ biến thiên nội "
   "năng ở chặng 3 là",
   ["−900 J.", "−500 J.", "+500 J.", "+900 J."],
   "B",
   "Chu trình kín ⟹ tổng ΔU của ba chặng bằng 0.\n"
   "ΔU₁ = +500 J; chặng 2 đẳng nhiệt nên ΔU₂ = 0.\n"
   "⟹ ΔU₃ = −(500 + 0) = −500 J.",
   "Định luật I – chu trình", RK),

mc("Đun nóng liên tục một mẫu chất rắn bằng thiết bị công suất không đổi. Thời gian để nó nóng lên tới "
   "nhiệt độ nóng chảy là t₁, thời gian nóng chảy hoàn toàn là t₂. Nếu tăng gấp đôi khối lượng mẫu (giữ "
   "nguyên nhiệt độ ban đầu và công suất) thì",
   ["t₁ tăng gấp đôi, t₂ không đổi.",
    "t₁ không đổi, t₂ tăng gấp đôi.",
    "cả t₁ và t₂ đều tăng gấp đôi.",
    "cả t₁ và t₂ đều không đổi."],
   "C",
   "Cả hai nhiệt lượng đều tỉ lệ thuận với khối lượng: Q₁ = mcΔT và Q₂ = λm. Với công suất không đổi, "
   "thời gian tỉ lệ thuận với nhiệt lượng nên cả t₁ và t₂ đều tăng gấp đôi (tỉ số t₂/t₁ không đổi).",
   "Suy luận tỉ lệ", K),

mc("Trong bình cách nhiệt có 1,0 kg nước ở 10 °C. Người ta thả vào một cục nước đá ở −20 °C và thấy khi "
   "cân bằng nhiệt, khối lượng nước đá trong bình TĂNG lên so với cục đá ban đầu. Điều đó chứng tỏ",
   ["cục nước đá đã tan một phần.",
    "một phần nước đã đông đặc thành đá.",
    "nhiệt độ cân bằng cao hơn 0 °C.",
    "khối lượng của hệ đã tăng lên."],
   "B",
   "Khối lượng đá tăng chỉ có thể do một phần nước chuyển thành đá, tức là nước đã ĐÔNG ĐẶC. Điều này xảy "
   "ra khi cục đá đủ lớn và đủ lạnh để “hút” hết nhiệt của nước; khi đó nhiệt độ cân bằng đúng bằng 0 °C.",
   "Biện luận trạng thái cuối", K),

mc("Một bếp đun 2,0 kg nước từ 25 °C. Trong 5 phút đầu nhiệt độ tăng 30 °C, nhưng trong 5 phút tiếp theo "
   "chỉ tăng thêm 25 °C. Nguyên nhân hợp lí nhất là",
   ["công suất bếp giảm dần theo thời gian.",
    "nhiệt dung riêng của nước tăng theo nhiệt độ.",
    "nước càng nóng thì hao phí ra môi trường càng lớn nên phần nhiệt có ích giảm.",
    "khối lượng nước tăng lên do hơi nước ngưng tụ."],
   "C",
   "Công suất hao phí tăng theo chênh lệch nhiệt độ giữa nước và môi trường. Nước càng nóng, hao phí càng "
   "lớn, phần công suất còn lại để làm nóng nước càng nhỏ nên tốc độ tăng nhiệt độ giảm dần — đó cũng là "
   "lí do đường T(t) thực tế hơi cong xuống chứ không thẳng.",
   "Phân tích thí nghiệm thực", K),

mc("Cần trộn nước ở 15 °C với nước ở 85 °C theo tỉ lệ khối lượng nào để được nước ở 40 °C?",
   ["m₁ : m₂ = 5 : 9.", "m₁ : m₂ = 9 : 5.", "m₁ : m₂ = 5 : 2.", "m₁ : m₂ = 2 : 5."],
   "B",
   "m₁(40 − 15) = m₂(85 − 40) ⟹ 25m₁ = 45m₂ ⟹ m₁/m₂ = 45/25 = 9/5.\n"
   "Cần nhiều nước lạnh hơn vì nó chỉ phải tăng 25 °C trong khi nước nóng phải hạ tới 45 °C.",
   "Cân bằng nhiệt – tỉ lệ", K),

mc("Một khối nước đá ở 0 °C được đặt trong phòng 25 °C. Trong khi đá đang tan, nhiệt độ của hỗn hợp "
   "nước – nước đá",
   ["tăng dần từ 0 °C lên 25 °C.", "giữ nguyên 0 °C.",
    "giảm dần vì đá thu nhiệt.", "dao động quanh 0 °C."],
   "B",
   "Chừng nào còn nước đá, toàn bộ nhiệt lượng nhận từ phòng dùng cho quá trình nóng chảy nên nhiệt độ "
   "hỗn hợp giữ nguyên 0 °C. Chỉ sau khi đá tan hết thì nước mới bắt đầu nóng lên.",
   "Sự nóng chảy", TB),

mc("Người ta cần 5,0 kg nước ở 40 °C. Có sẵn nước ở 15 °C và nước sôi 100 °C. Khối lượng nước sôi cần dùng là",
   ["1,47 kg.", "1,72 kg.", "2,05 kg.", "2,50 kg."],
   "A",
   "Gọi m là khối lượng nước sôi, khi đó nước lạnh là (5,0 − m):\n"
   "m(100 − 40) = (5,0 − m)(40 − 15) ⟹ 60m = 125 − 25m ⟹ 85m = 125 ⟹ m ≈ 1,47 kg.",
   "Cân bằng nhiệt – bài toán ngược", K),

mc("Hai mẫu của cùng một chất, khối lượng m và 2m, được đun bằng hai thiết bị có công suất lần lượt là P "
   "và 3P. Sau cùng một khoảng thời gian, tỉ số độ tăng nhiệt độ ΔT₂/ΔT₁ bằng",
   ["2/3.", "3/2.", "1/6.", "6."],
   "B",
   "ΔT = P·t/(m·c). Với cùng t và cùng c:\n"
   "ΔT₂/ΔT₁ = (3P/2m)/(P/m) = 3/2.",
   "Suy luận tỉ lệ", K),

mc("Nội năng của một vật KHÔNG phụ thuộc vào yếu tố nào sau đây?",
   ["Nhiệt độ của vật.", "Khối lượng của vật.",
    "Bản chất của chất tạo nên vật.", "Vận tốc chuyển động của vật so với mặt đất."],
   "D",
   "Nội năng chỉ liên quan tới chuyển động và tương tác của các phân tử BÊN TRONG vật. Vận tốc chuyển "
   "động của cả vật thuộc về động năng (cơ năng), không thuộc nội năng.",
   "Nội năng", TB),

mc("Trong thí nghiệm xác định nhiệt dung riêng bằng phương pháp điện, sai số hệ thống lớn nhất thường "
   "đến từ",
   ["việc đọc nhiệt kế sai một vài phần mười độ.",
    "nhiệt lượng hao phí ra môi trường và nhiệt lượng làm nóng chính bình chứa.",
    "sai số của cân điện tử khi đo khối lượng nước.",
    "sự dao động của điện áp nguồn."],
   "B",
   "Hao phí ra môi trường và phần nhiệt làm nóng vỏ bình luôn làm nhiệt lượng “có ích” nhỏ hơn P·t, khiến "
   "giá trị c đo được LỚN hơn thực tế. Đây là sai số hệ thống (luôn lệch về một phía), khác với sai số "
   "ngẫu nhiên khi đọc dụng cụ.",
   "Phân tích sai số thí nghiệm", RK, fig="n_sd_dun_dien",
   cap="Bộ thí nghiệm đo nhiệt dung riêng bằng phương pháp điện"),

mc("Một tủ đông có công suất làm lạnh (nhiệt lượng lấy đi mỗi giây) là 200 W. Thời gian để đưa 1,0 kg "
   "nước ở 20 °C thành nước đá ở 0 °C là (λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K))",
   ["7 phút 0 giây.", "28 phút 20 giây.", "35 phút 20 giây.", "42 phút 0 giây."],
   "C",
   "Q = mcΔt + λm = 1,0 · 4200 · 20 + 3,4·10⁵ · 1,0 = 84 000 + 340 000 = 424 000 J.\n"
   "t = 424 000/200 = 2120 s = 35 phút 20 giây.\n"
   "Chú ý giai đoạn đông đặc chiếm tới 80% tổng nhiệt lượng phải lấy đi.",
   "Chuyển thể – thực tiễn", K),

mc("Khi so sánh nhiệt lượng cần để đun sôi 1 lít nước ở đồng bằng và trên đỉnh núi cao (cùng từ 25 °C), "
   "kết luận nào sau đây đúng?",
   ["Trên núi cần nhiều nhiệt lượng hơn vì không khí loãng.",
    "Trên núi cần ít nhiệt lượng hơn vì nước sôi ở nhiệt độ thấp hơn.",
    "Hai nơi cần nhiệt lượng như nhau vì cùng khối lượng nước.",
    "Không so sánh được vì phụ thuộc loại bếp."],
   "B",
   "Nhiệt độ sôi giảm khi áp suất giảm. Trên núi cao nước sôi ở dưới 100 °C nên Δt nhỏ hơn, "
   "Q = mcΔt cũng nhỏ hơn. (Tuy nhiên nấu chín thức ăn lại lâu hơn vì nhiệt độ nấu thấp hơn.)",
   "Sự sôi – thực tiễn", K),

mc("Đại lượng nào sau đây là hàm của TRẠNG THÁI (chỉ phụ thuộc trạng thái đầu và cuối, không phụ thuộc "
   "cách biến đổi)?",
   ["Nhiệt lượng Q.", "Công A.", "Nội năng U.", "Cả ba đại lượng trên."],
   "C",
   "Nội năng chỉ phụ thuộc trạng thái của hệ, nên ΔU giữa hai trạng thái là xác định dù đi theo quá trình "
   "nào. Ngược lại, A và Q phụ thuộc cách thực hiện quá trình — chính vì thế mới nói “vật chứa nội năng” "
   "chứ không nói “vật chứa nhiệt lượng”.",
   "Nội năng – hàm trạng thái", RK),
],
P2=[
ds("Thả 2,0 kg nước đá ở −20 °C vào 0,50 kg nước ở 20 °C trong bình cách nhiệt lí tưởng. Cho "
   "c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng cần để hâm khối nước đá từ −20 °C lên 0 °C là 84 kJ.", True,
     "Đúng. Q = 2,0 · 2100 · 20 = 84 000 J."),
    ("Toàn bộ 0,50 kg nước sẽ đông đặc thành nước đá.", False,
     "Sai. Nếu đông đặc hết, nước sẽ nhường tổng cộng 42 000 + 170 000 = 212 000 J, nhiều hơn hẳn 84 000 J "
     "mà khối đá cần. Vậy chỉ một phần nước đông đặc và hệ dừng ở 0 °C."),
    ("Khối lượng nước đã đông đặc vào khoảng 124 g.", True,
     "Đúng. 42 000 + x·3,4·10⁵ = 84 000 ⟹ x = 42 000/3,4·10⁵ ≈ 0,124 kg."),
    ("Nhiệt độ của hệ khi cân bằng nhiệt bằng 0 °C.", True,
     "Đúng. Khi hệ dừng lại ở trạng thái có cả nước và nước đá cùng tồn tại thì nhiệt độ đúng bằng nhiệt "
     "độ nóng chảy 0 °C.")],
   "Biện luận trạng thái cuối – nước đông đặc", RK),

ds("Một bình cách nhiệt lí tưởng đang chứa 1,0 kg nước ở 20 °C. Người ta lấy từ ngăn đông ra m kg nước đá "
   "ở −10 °C rồi thả vào bình. Cho c_đá = 2100, "
   "c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   [("Nhiệt lượng lớn nhất mà 1,0 kg nước có thể nhường là 84 kJ.", True,
     "Đúng. Q = 1,0 · 4200 · 20 = 84 000 J khi nước hạ tới 0 °C."),
    ("Với m = 0,10 kg thì toàn bộ nước đá tan hết.", True,
     "Đúng. Cần 0,10(2100 · 10 + 3,4·10⁵) = 36 100 J < 84 000 J nên đá tan hết và nhiệt độ cuối trên 0 °C."),
    ("Để khi cân bằng vẫn còn nước đá chưa tan thì phải có m ≥ 0,233 kg.", True,
     "Đúng. Điều kiện đá không tan hết: 84 000 ≤ m(21 000 + 340 000) = 361 000m ⟹ m ≥ 0,233 kg."),
    ("Dù m lớn đến đâu thì nhiệt độ cân bằng cũng không thể thấp hơn 0 °C.", False,
     "Sai. Nếu m rất lớn (ở đây m > 4 kg), nhiệt lượng nước nhường ra kể cả khi đông đặc hoàn toàn vẫn "
     "không đủ hâm khối đá lên 0 °C; khi đó toàn bộ hệ hoá rắn và nhiệt độ cân bằng THẤP hơn 0 °C.")],
   "Biện luận điều kiện", RK),

ds("Một bếp đun 2,0 kg nước từ 25 °C, ghi nhận: trong 5 phút đầu nhiệt độ tăng 30 °C, trong 5 phút tiếp "
   "theo chỉ tăng thêm 25 °C. Cho c_nước = 4200 J/(kg·K).",
   [("Nhiệt lượng nước thực nhận trong 5 phút đầu là 252 kJ.", True,
     "Đúng. Q = 2,0 · 4200 · 30 = 252 000 J."),
    ("Nhiệt lượng nước thực nhận trong 5 phút sau nhỏ hơn 5 phút đầu.", True,
     "Đúng. Q = 2,0 · 4200 · 25 = 210 000 J < 252 000 J."),
    ("Kết quả trên chứng tỏ nhiệt dung riêng của nước tăng theo nhiệt độ.", False,
     "Sai. Nhiệt dung riêng của nước gần như không đổi trong khoảng nhiệt độ này. Nguyên nhân thật là hao "
     "phí ra môi trường tăng lên khi nước nóng hơn, nên phần nhiệt lượng CÓ ÍCH giảm dần."),
    ("Nếu bọc cách nhiệt cho ấm thì độ chênh giữa hai giai đoạn sẽ giảm đi.", True,
     "Đúng. Bọc cách nhiệt làm giảm hao phí ở mọi nhiệt độ, nên tốc độ tăng nhiệt độ đều hơn và đường "
     "T(t) gần với đường thẳng hơn.")],
   "Phân tích thí nghiệm thực", K),

ds("Xét khái niệm hàm trạng thái và việc vận dụng định luật I nhiệt động lực học.",
   [("Nội năng là hàm của trạng thái, còn công và nhiệt lượng thì phụ thuộc quá trình.", True,
     "Đúng. Vì vậy ΔU giữa hai trạng thái là xác định, còn A và Q có thể khác nhau tuỳ đường đi."),
    ("Một khối khí lí tưởng đi từ trạng thái 1 sang trạng thái 2 theo hai quá trình khác nhau thì độ biến "
     "thiên nội năng trong hai quá trình là như nhau.", True,
     "Đúng, đó chính là hệ quả của việc nội năng là hàm trạng thái."),
    ("Trong một chu trình kín gồm ba chặng, nếu chặng 1 có ΔU = +500 J và chặng 2 đẳng nhiệt thì chặng 3 "
     "có ΔU = −500 J.", True,
     "Đúng. Chặng 2 đẳng nhiệt nên ΔU₂ = 0; tổng ba chặng bằng 0 nên ΔU₃ = −500 J."),
    ("Vì nội năng là hàm trạng thái nên trong một chu trình kín, nhiệt lượng mà hệ trao đổi cũng bằng 0.", False,
     "Sai. ΔU = 0 chỉ cho A + Q = 0. Hệ vẫn có thể nhận một nhiệt lượng lớn và sinh ra công đúng bằng "
     "nhiệt lượng đó — đây chính là nguyên tắc hoạt động của mọi động cơ nhiệt.")],
   "Nội năng – hàm trạng thái", RK),
],
P3=[
sa("Thả 2,0 kg nước đá ở −20 °C vào 0,50 kg nước ở 20 °C trong bình cách nhiệt lí tưởng. Khối lượng nước "
   "đã đông đặc bằng bao nhiêu gam (làm tròn đến hàng đơn vị)? Cho c_đá = 2100, c_nước = 4200 J/(kg·K), "
   "λ = 3,4·10⁵ J/kg.",
   "124",
   "Hâm khối đá lên 0 °C cần 2,0·2100·20 = 84 000 J, trong khi nước chỉ nhường được 0,50·4200·20 = "
   "42 000 J khi hạ tới 0 °C ⟹ phần thiếu phải lấy từ quá trình ĐÔNG ĐẶC của nước.\n"
   "42 000 + x·3,4·10⁵ = 84 000 ⟹ x = 42 000/3,4·10⁵ ≈ 0,124 kg = 124 g.",
   "Biện luận trạng thái cuối", RK),

sa("Thả 0,50 kg kim loại ở nhiệt độ t vào 1,0 kg nước ở 20 °C, nhiệt độ cân bằng là 25 °C. "
   "Cho c_kim loại = 460, c_nước = 4200 J/(kg·K). Giá trị của t bằng bao nhiêu độ C (làm tròn đến hàng "
   "đơn vị)?",
   "116",
   "0,50·460·(t − 25) = 1,0·4200·5 ⟹ 230(t − 25) = 21 000 ⟹ t ≈ 116 °C.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Thả 0,20 kg nước đá ở 0 °C vào 0,50 kg nước ở nhiệt độ t; nhiệt độ cân bằng là 10 °C. "
   "Giá trị của t bằng bao nhiêu độ C (làm tròn đến chữ số thập phân thứ nhất)? "
   "Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "46,4",
   "Q_thu = 0,20·3,4·10⁵ + 0,20·4200·10 = 76 400 J.\n"
   "0,50·4200·(t − 10) = 76 400 ⟹ t − 10 ≈ 36,4 ⟹ t ≈ 46,4 °C.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Cần bao nhiêu kilôgam nước sôi (100 °C) trộn với nước ở 15 °C để được 5,0 kg nước ở 40 °C "
   "(làm tròn đến chữ số thập phân thứ hai)?",
   "1,47",
   "m(100 − 40) = (5,0 − m)(40 − 15) ⟹ 60m = 125 − 25m ⟹ 85m = 125 ⟹ m ≈ 1,47 kg.",
   "Cân bằng nhiệt – bài toán ngược", K),

sa("Một tủ đông lấy đi nhiệt lượng với công suất 200 W. Thời gian để đưa 1,0 kg nước ở 20 °C thành nước "
   "đá ở 0 °C bằng bao nhiêu giây? Cho λ = 3,4·10⁵ J/kg, c = 4200 J/(kg·K).",
   "2120",
   "Q = 1,0·4200·20 + 3,4·10⁵·1,0 = 84 000 + 340 000 = 424 000 J ⟹ t = 424 000/200 = 2120 s.",
   "Chuyển thể – thực tiễn", K),

sa("Thả m kg nước đá ở −10 °C vào 1,0 kg nước ở 20 °C. Giá trị nhỏ nhất của m để khi cân bằng nhiệt trong "
   "bình vẫn còn nước đá bằng bao nhiêu kilôgam (làm tròn đến chữ số thập phân thứ ba)? "
   "Cho c_đá = 2100, c_nước = 4200 J/(kg·K), λ = 3,4·10⁵ J/kg.",
   "0,233",
   "Điều kiện để đá KHÔNG tan hết: nhiệt lượng nước nhường ra không đủ vừa hâm vừa làm tan hết đá:\n"
   "1,0·4200·20 ≤ m(2100·10 + 3,4·10⁵) ⟹ 84 000 ≤ 361 000m ⟹ m ≥ 0,233 kg.",
   "Biện luận điều kiện", RK),
])


NHOM = dict(
    ten_nhom="LỚP 12 – CHƯƠNG 1: VẬT LÍ NHIỆT",
    mo_ta="Bộ 10 đề luyện tập, độ khó tăng dần từ Đề 1 (Dễ) đến Đề 10 (Khó / thử thách)",
    pham_vi=(
        "Bài 1. Cấu trúc của chất. Sự chuyển thể  •  Bài 2. Nội năng. Định luật I của nhiệt động lực học\n"
        "Bài 3. Nhiệt độ. Thang nhiệt độ – nhiệt kế  •  Bài 4. Nhiệt dung riêng\n"
        "Bài 5. Nhiệt nóng chảy riêng  •  Bài 6. Nhiệt hoá hơi riêng  •  Bài 7. Bài tập về vật lí nhiệt\n"
        "Hằng số dùng thống nhất: c_nước = 4200; c_nước đá = 2100; c_nhôm = 880; c_đồng = 380; "
        "c_sắt = 460; c_chì = 130 J/(kg·K); λ_nước đá = 3,4·10⁵ J/kg; L_nước = 2,26·10⁶ J/kg; "
        "g = 10 m/s²."),
    tests=[DE1, DE2, DE3, DE4, DE5, DE6, DE7, DE8, DE9, DE10],
)
