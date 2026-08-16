# -*- coding: utf-8 -*-
"""PHẦN B - MỨC ĐỘ THÔNG HIỂU (35 câu)"""

PART_B = [
dict(
q="Dùng một bếp có công suất không đổi để đun một cục nước đá ở −10 °C cho tới khi toàn bộ nước biến thành hơi ở 100 °C. Trên đồ thị biểu diễn nhiệt độ của mẫu chất theo thời gian, số đoạn nằm ngang là",
o=["0.", "1.", "2.", "3."],
a="C",
e="Nhiệt độ chỉ giữ nguyên trong các giai đoạn chuyển thể: nóng chảy ở 0 °C và sôi ở 100 °C. Vậy có 2 đoạn nằm ngang, xen giữa là ba đoạn dốc lên ứng với quá trình làm nóng nước đá, nước lỏng và hơi nước."),

dict(
q="Khi nước đá đang tan ở 0 °C, nhiệt lượng mà nó nhận được chủ yếu được dùng để",
o=["làm tăng động năng chuyển động nhiệt trung bình của các phân tử.",
   "làm tăng thế năng tương tác giữa các phân tử, phá vỡ cấu trúc mạng tinh thể.",
   "làm tăng đồng thời cả động năng và thế năng của các phân tử.",
   "sinh công đẩy không khí xung quanh ra xa."],
a="B",
e="Nhiệt độ không đổi trong quá trình tan chứng tỏ động năng chuyển động nhiệt trung bình của phân tử không đổi. Toàn bộ nhiệt lượng nhận vào được dùng để phá vỡ liên kết trong mạng tinh thể, tức làm tăng thế năng tương tác giữa các phân tử. Công đẩy không khí là không đáng kể vì thể tích thay đổi rất ít."),

dict(
q="Vừa bước ra khỏi bể bơi, ta thường cảm thấy lạnh hơn lúc còn ở dưới nước. Nguyên nhân chủ yếu là",
o=["không khí luôn có nhiệt độ thấp hơn nước trong bể.",
   "cơ thể mất nhiệt do bức xạ ra không gian rộng hơn.",
   "lớp nước bám trên da bay hơi và thu nhiệt lượng từ cơ thể.",
   "da bị co lại nên dẫn nhiệt tốt hơn."],
a="C",
e="Sự bay hơi là quá trình thu nhiệt: những phân tử nước có động năng lớn thoát khỏi mặt thoáng, lấy nhiệt của lớp nước còn lại và của da, làm da mất nhiệt nhanh nên ta thấy lạnh. Nhiệt hoá hơi riêng của nước rất lớn nên hiệu ứng này rất rõ; gió chỉ làm quá trình bay hơi mạnh thêm chứ không phải nguyên nhân gốc."),

dict(
q="Hai bình kín chứa cùng một loại khí lí tưởng, có cùng số phân tử và cùng nhiệt độ nhưng thể tích khác nhau nên áp suất khác nhau. So sánh nội năng U₁ và U₂ của hai khối khí, ta có",
o=["U₁ = U₂.",
   "khối khí có áp suất lớn hơn thì có nội năng lớn hơn.",
   "khối khí có thể tích lớn hơn thì có nội năng lớn hơn.",
   "không so sánh được vì thiếu dữ kiện về áp suất."],
a="A",
e="Nội năng của khí lí tưởng chỉ gồm động năng chuyển động nhiệt của các phân tử, bằng N·(3/2)kT. Vì hai khối khí có cùng số phân tử N và cùng nhiệt độ T nên nội năng bằng nhau, không phụ thuộc áp suất hay thể tích."),

dict(
q="Cọ xát mạnh một miếng kim loại lên mặt bàn, miếng kim loại nóng lên. Nội năng của miếng kim loại đã tăng chủ yếu do",
o=["truyền nhiệt từ mặt bàn sang miếng kim loại.",
   "thực hiện công của lực ma sát lên miếng kim loại.",
   "miếng kim loại nhận nhiệt lượng từ không khí xung quanh.",
   "khối lượng của miếng kim loại tăng lên."],
a="B",
e="Trước khi cọ xát, miếng kim loại và mặt bàn cùng nhiệt độ nên không thể có truyền nhiệt theo chiều làm kim loại nóng lên. Cơ năng của chuyển động được chuyển hoá thành nội năng thông qua công của lực ma sát — đây là cách làm biến đổi nội năng bằng thực hiện công."),

dict(
q="Khi bơm xe đạp, ta thấy thân bơm nóng lên. Giải thích nào sau đây đầy đủ và đúng nhất?",
o=["Chỉ do ma sát giữa pit-tông và thành bơm, còn khí trong bơm không hề đổi nhiệt độ.",
   "Chỉ do khí trong bơm nhận nhiệt lượng truyền từ tay người bơm qua thành bơm bằng kim loại.",
   "Do khí trong bơm bị nén nên nhận công làm nội năng tăng, đồng thời có ma sát giữa pit-tông và thành bơm.",
   "Do khối lượng khí chứa trong thân bơm tăng lên nên nội năng và nhiệt độ của khí đều tăng."],
a="C",
e="Có hai nguyên nhân đồng thời: khí bị nén nhanh nên nhận công (A > 0), gần như không kịp trao đổi nhiệt, làm nội năng và nhiệt độ khí tăng; ngoài ra ma sát giữa pit-tông và thành bơm cũng sinh nhiệt. Cả hai đều là quá trình thực hiện công."),

dict(
q="Một khối khí nhận nhiệt lượng 100 J, đồng thời thực hiện công 60 J lên môi trường bên ngoài. Độ biến thiên nội năng của khối khí là",
o=["160 J.", "40 J.", "−40 J.", "−160 J."],
a="B",
e="Khí thực hiện công 60 J lên bên ngoài nghĩa là công mà khí nhận được A = −60 J; nhiệt lượng khí nhận Q = +100 J. Theo định luật I: ΔU = A + Q = −60 + 100 = 40 J > 0, nội năng khí tăng 40 J. Sai lầm thường gặp là cộng cả hai giá trị thành 160 J."),

dict(
q="Trong quá trình đẳng tích, một khối khí nhận nhiệt lượng Q. Kết luận nào sau đây đúng?",
o=["ΔU = 0.", "ΔU = Q.", "ΔU = −Q.", "ΔU = Q/2."],
a="B",
e="Trong quá trình đẳng tích, thể tích không đổi nên khí không trao đổi công với bên ngoài (A = 0). Định luật I cho ΔU = A + Q = Q: toàn bộ nhiệt lượng nhận vào dùng để làm tăng nội năng, do đó nhiệt độ khí tăng."),

dict(
q="Nén đẳng nhiệt một khối khí lí tưởng. Kết luận nào sau đây đúng?",
o=["Khí đồng thời nhận công và nhận nhiệt lượng từ môi trường.",
   "Khí nhận công và toả ra nhiệt lượng có độ lớn bằng công nhận được.",
   "Khí hoàn toàn không trao đổi nhiệt lượng với môi trường bên ngoài.",
   "Nội năng của khí tăng lên vì khí nhận được công khi bị nén."],
a="B",
e="Đẳng nhiệt nên nhiệt độ không đổi, mà nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ nên ΔU = 0. Định luật I: 0 = A + Q ⇒ Q = −A. Khi nén, khí nhận công (A > 0) nên Q < 0, tức khí toả ra nhiệt lượng đúng bằng công nhận được. Vậy quá trình đẳng nhiệt không hề là quá trình không trao đổi nhiệt."),

dict(
q="Nén thật nhanh một khối khí trong một xilanh có vỏ cách nhiệt tốt. Nhiệt độ của khối khí sẽ",
o=["tăng lên.", "giảm đi.", "không đổi.", "tăng rồi giảm về giá trị ban đầu."],
a="A",
e="Vỏ cách nhiệt và quá trình xảy ra nhanh nên Q ≈ 0. Khi nén, khí nhận công A > 0, do đó ΔU = A > 0: nội năng tăng, kéo theo nhiệt độ khí tăng. Đây là nguyên tắc của động cơ Diesel và cũng là lí do khí trong bơm xe nóng lên."),

dict(
q="Nước được dùng phổ biến làm chất tải nhiệt trong hệ thống làm mát động cơ chủ yếu vì nước",
o=["có khối lượng riêng lớn.", "có nhiệt độ sôi cao.", "có nhiệt dung riêng rất lớn.", "dẫn điện tốt."],
a="C",
e="Nhiệt dung riêng của nước rất lớn (4200 J/(kg·K)), nên cùng một khối lượng, nước hấp thụ được nhiều nhiệt hơn hẳn các chất khác mà nhiệt độ tăng ít, do đó tải nhiệt hiệu quả khỏi động cơ. Khối lượng riêng và tính dẫn điện không phải lí do; nhiệt độ sôi cao chỉ là ưu điểm phụ."),

dict(
q="Nhiệt dung riêng của nhôm là 880 J/(kg·K). Con số này cho biết",
o=["1 kg nhôm chứa 880 J nội năng.",
   "cần cung cấp 880 J để 1 kg nhôm tăng thêm 1 K.",
   "cần cung cấp 880 J để nhôm nóng chảy hoàn toàn.",
   "1 kg nhôm toả ra 880 J khi hạ nhiệt độ xuống 0 K."],
a="B",
e="Định nghĩa nhiệt dung riêng: nhiệt lượng cần cung cấp cho 1 kg chất để nhiệt độ của nó tăng thêm 1 K (hay 1 °C). Cách hiểu “1 kg nhôm chứa 880 J nội năng” là sai vì không tồn tại khái niệm “nhiệt lượng chứa trong vật”; còn đại lượng ứng với sự nóng chảy hoàn toàn là nhiệt nóng chảy riêng."),

dict(
q="Vào ban ngày dưới cùng ánh nắng, mặt đất ở bờ biển nóng lên nhanh hơn nước biển. Nguyên nhân chính là",
o=["đất hấp thụ ánh sáng nhiều hơn nước tới hàng chục lần.",
   "nhiệt dung riêng của đất nhỏ hơn nhiều so với của nước.",
   "khối lượng riêng của đất lớn hơn của nước.",
   "nước biển luôn nhận thêm nhiệt từ đáy biển."],
a="B",
e="Với cùng nhiệt lượng hấp thụ trên mỗi kilôgam, độ tăng nhiệt độ Δt = Q/(mc) tỉ lệ nghịch với nhiệt dung riêng. Nhiệt dung riêng của nước (4200 J/(kg·K)) lớn hơn nhiều so với đất (khoảng 800 J/(kg·K)), nên đất nóng lên nhanh hơn (và ban đêm cũng nguội nhanh hơn)."),

dict(
q="Trong hệ toạ độ (p, T), đường đẳng tích của một khối lượng khí lí tưởng xác định là",
o=["một nhánh hypebol.",
   "một đường thẳng song song với trục OT.",
   "một đoạn thẳng mà nếu kéo dài sẽ đi qua gốc toạ độ.",
   "một đường thẳng song song với trục Op."],
a="C",
e="Với V không đổi, phương trình trạng thái cho p/T = hằng số, tức p = (hằng số)·T: đồ thị p theo T là đường thẳng đi qua gốc toạ độ. Đường song song trục OT ứng với quá trình đẳng áp trong hệ (p, T)."),

dict(
q="Trong hệ toạ độ (p, V), đường đẳng tích của một khối lượng khí lí tưởng xác định là",
o=["một đoạn thẳng song song với trục Op.",
   "một đoạn thẳng song song với trục OV.",
   "một nhánh hypebol.",
   "một đường thẳng đi qua gốc toạ độ."],
a="A",
e="Đẳng tích nghĩa là V = hằng số, nên trên hệ (p, V) mọi điểm biểu diễn đều có cùng hoành độ V: đồ thị là đoạn thẳng song song với trục Op (trục áp suất). Đoạn thẳng song song trục OV ứng với quá trình đẳng áp."),

dict(
q="Áp suất mà chất khí tác dụng lên thành bình chứa được gây ra bởi",
o=["trọng lượng của khối khí trong bình.",
   "lực hút giữa các phân tử khí và thành bình.",
   "sự nở vì nhiệt của thành bình.",
   "sự va chạm của vô số phân tử khí lên thành bình."],
a="D",
e="Theo mô hình động học phân tử, mỗi phân tử va chạm vào thành bình truyền cho thành bình một xung lượng; tổng hợp lực do vô số va chạm trong một đơn vị thời gian trên một đơn vị diện tích chính là áp suất khí. Trọng lượng khí là rất nhỏ và không giải thích được vì sao áp suất tác dụng lên mọi phía của thành bình."),

dict(
q="Nén đẳng nhiệt một khối khí lí tưởng đến khi thể tích chỉ còn bằng một phần ba thể tích ban đầu thì áp suất của khí",
o=["giảm 3 lần.", "tăng 3 lần.", "tăng 9 lần.", "không đổi."],
a="B",
e="Theo định luật Boyle p₁V₁ = p₂V₂. Với V₂ = V₁/3 ta được p₂ = p₁V₁/V₂ = 3p₁: áp suất tăng gấp 3 lần. Kết quả 9 lần là sai lầm do nhầm quan hệ bậc hai."),

dict(
q="Một khối lượng khí xác định được đun nóng đẳng áp từ 27 °C lên 327 °C. Thể tích của khí",
o=["tăng 12,1 lần.", "tăng 2 lần.", "tăng 300 lần.", "tăng 1,5 lần."],
a="B",
e="Phải đổi sang nhiệt độ tuyệt đối: T₁ = 300 K, T₂ = 600 K. Định luật Charles cho V₂/V₁ = T₂/T₁ = 2. Đáp án 12,1 lần là bẫy điển hình do lấy tỉ số nhiệt độ Celsius 327/27."),

dict(
q="Săm xe đạp bơm căng để ngoài trời nắng gắt dễ bị nổ. Nguyên nhân là",
o=["nhiệt độ tăng làm thể tích khí trong săm tăng mạnh, còn áp suất giảm.",
   "thể tích săm gần như không đổi, nhiệt độ khí tăng làm áp suất khí tăng.",
   "khối lượng khí trong săm tăng khi trời nắng.",
   "cao su bị nắng làm cho bền hơn nên áp suất khí giảm."],
a="B",
e="Săm đã bơm căng nên thể tích khí thay đổi rất ít, quá trình gần đúng là đẳng tích: p/T = hằng số. Khi nhiệt độ tuyệt đối tăng, áp suất khí tăng theo, có thể vượt quá giới hạn bền của săm gây nổ. Khối lượng khí trong săm không đổi."),

dict(
q="Hai bình có thể tích khác nhau, chứa hai chất khí khác nhau ở cùng áp suất và cùng nhiệt độ. Kết luận nào sau đây đúng?",
o=["Tổng số phân tử khí chứa trong hai bình là bằng nhau.",
   "Khối lượng khí chứa trong hai bình bằng nhau vì cùng áp suất.",
   "Số phân tử khí trong mỗi đơn vị thể tích của hai bình bằng nhau.",
   "Khối lượng riêng của hai chất khí trong hai bình bằng nhau."],
a="C",
e="Từ p = (N/V)kT, khi p và T như nhau thì mật độ phân tử N/V như nhau. Tổng số phân tử N thì khác nhau vì thể tích khác nhau; khối lượng và khối lượng riêng cũng khác nhau vì khối lượng mol của hai khí khác nhau."),

dict(
q="Ở cùng một nhiệt độ, so sánh các phân tử khí hydrogen (H₂) và oxygen (O₂), kết luận nào sau đây đúng?",
o=["Động năng tịnh tiến trung bình của phân tử H₂ lớn hơn của phân tử O₂.",
   "Động năng tịnh tiến trung bình bằng nhau, còn tốc độ trung bình của phân tử H₂ lớn hơn.",
   "Cả động năng tịnh tiến trung bình và tốc độ trung bình đều bằng nhau.",
   "Tốc độ trung bình của phân tử O₂ lớn hơn vì khối lượng phân tử lớn hơn."],
a="B",
e="Động năng tịnh tiến trung bình Eđ = (3/2)kT chỉ phụ thuộc nhiệt độ nên hai loại phân tử có Eđ bằng nhau. Từ (1/2)mv² = Eđ, phân tử có khối lượng nhỏ hơn phải có tốc độ lớn hơn; khối lượng phân tử H₂ nhỏ hơn O₂ khoảng 16 lần nên tốc độ căn quân phương của H₂ lớn hơn khoảng 4 lần."),

dict(
q="Khi nhiệt độ tuyệt đối của một khối khí lí tưởng tăng lên 4 lần thì tốc độ căn quân phương của các phân tử khí",
o=["tăng 4 lần.", "tăng 16 lần.", "tăng 2 lần.", "không đổi."],
a="C",
e="Từ (1/2)mv² = (3/2)kT suy ra v = √(3kT/m), tức tốc độ căn quân phương tỉ lệ với căn bậc hai của nhiệt độ tuyệt đối. Khi T tăng 4 lần thì v tăng √4 = 2 lần. Đại lượng tăng đúng 4 lần là động năng trung bình, không phải tốc độ."),

dict(
q="Nhiệt lượng là",
o=["một dạng năng lượng dự trữ sẵn trong vật.",
   "số đo phần nội năng mà vật nhận thêm hay mất bớt trong quá trình truyền nhiệt.",
   "phần năng lượng mà vật nhận được khi có lực tác dụng làm vật chuyển dời.",
   "tổng động năng của các phân tử cấu tạo nên vật."],
a="B",
e="Nhiệt lượng đặc trưng cho quá trình trao đổi năng lượng bằng cách truyền nhiệt, là số đo độ biến thiên nội năng trong quá trình đó. Nó không phải đại lượng trạng thái nên không thể nói 'vật chứa nhiệt lượng'. “Năng lượng nhận được khi có lực tác dụng làm vật chuyển dời” là định nghĩa của công, còn “tổng động năng các phân tử” chỉ là một phần của nội năng."),

dict(
q="Phát biểu nào sau đây SAI?",
o=["Nội năng của một vật có thể thay đổi bằng cách truyền nhiệt hoặc thực hiện công.",
   "Nhiệt độ càng cao thì các phân tử của vật chuyển động nhiệt càng nhanh.",
   "Vật có nhiệt độ càng cao thì chứa càng nhiều nhiệt lượng.",
   "Nội năng của vật phụ thuộc vào nhiệt độ và thể tích của vật."],
a="C",
e="Nhiệt lượng không phải đại lượng đặc trưng cho trạng thái của vật nên không thể nói vật 'chứa' nhiệt lượng; chỉ có thể nói về nhiệt lượng vật nhận hoặc toả trong một quá trình. Ba phát biểu còn lại đều đúng theo lí thuyết nhiệt động lực học."),

dict(
q="Nhiệt hoá hơi riêng của nước là 2,26·10⁶ J/kg. Con số này cho biết",
o=["cần cung cấp 2,26·10⁶ J để 1 kg nước tăng thêm 1 K.",
   "cần cung cấp 2,26·10⁶ J để làm cho 1 kg nước ở nhiệt độ sôi hoá hơi hoàn toàn.",
   "cần cung cấp 2,26·10⁶ J để 1 kg nước đá nóng chảy hoàn toàn.",
   "1 kg hơi nước chứa năng lượng 2,26·10⁶ J."],
a="B",
e="Nhiệt hoá hơi riêng L là nhiệt lượng cần cung cấp cho 1 kg chất lỏng ở nhiệt độ sôi để hoá hơi hoàn toàn (Q = Lm), đơn vị J/kg. Đại lượng ứng với sự tăng nhiệt độ là nhiệt dung riêng, ứng với sự nóng chảy là nhiệt nóng chảy riêng (nước đá: 3,34·10⁵ J/kg)."),

dict(
q="Quá trình nào sau đây là quá trình toả nhiệt?",
o=["Sự nóng chảy của một cục nước đá đặt trong không khí.",
   "Sự bay hơi của cồn y tế được xoa lên mu bàn tay.",
   "Sự ngưng tụ của hơi nước trên thành cốc nước lạnh.",
   "Sự sôi của nước trong ấm đang được đun trên bếp."],
a="C",
e="Ngưng tụ là quá trình ngược của hoá hơi nên toả ra nhiệt lượng đúng bằng nhiệt lượng đã thu vào khi hoá hơi cùng khối lượng ở cùng nhiệt độ. Nóng chảy, bay hơi và sôi đều là các quá trình thu nhiệt."),

dict(
q="Chất khí thực có thể coi gần đúng là khí lí tưởng trong điều kiện nào?",
o=["Áp suất rất lớn và nhiệt độ rất thấp.",
   "Áp suất không quá lớn và nhiệt độ không quá thấp.",
   "Áp suất rất lớn và nhiệt độ rất cao.",
   "Nhiệt độ càng gần 0 K càng chính xác."],
a="B",
e="Mô hình khí lí tưởng bỏ qua thể tích riêng của phân tử và tương tác giữa các phân tử. Điều đó chỉ hợp lí khi khoảng cách giữa các phân tử đủ lớn (áp suất không quá lớn) và động năng nhiệt đủ lớn so với thế năng tương tác (nhiệt độ không quá thấp). Ở áp suất rất lớn hoặc nhiệt độ rất thấp, khí thực dễ hoá lỏng và sai lệch nhiều so với mô hình."),

dict(
q="Định luật Boyle chỉ áp dụng được khi",
o=["khối lượng khí không đổi và nhiệt độ khí không đổi.",
   "khối lượng khí không đổi và áp suất khí không đổi.",
   "thể tích khí không đổi.",
   "khối lượng khí thay đổi nhưng nhiệt độ không đổi."],
a="A",
e="Định luật Boyle phát biểu cho một khối lượng khí xác định trong quá trình đẳng nhiệt: pV = hằng số. Nếu khối lượng khí thay đổi (khí rò rỉ, bơm thêm) hoặc nhiệt độ thay đổi thì hệ thức này không còn áp dụng được cho toàn bộ quá trình."),

dict(
q="Trong hệ toạ độ (p, V) vẽ hai đường đẳng nhiệt của cùng một khối lượng khí lí tưởng ứng với hai nhiệt độ T₁ và T₂. Đường ứng với T₂ nằm xa gốc toạ độ hơn. Kết luận nào đúng?",
o=["T₂ < T₁.", "T₂ = T₁.", "T₂ > T₁.", "Không kết luận được nếu chưa biết áp suất."],
a="C",
e="Trên đường đẳng nhiệt, tích pV = nRT là hằng số và tỉ lệ thuận với T. Đường nằm xa gốc toạ độ hơn ứng với giá trị tích pV lớn hơn, do đó ứng với nhiệt độ cao hơn: T₂ > T₁. Hai đường đẳng nhiệt của cùng một khối khí không bao giờ cắt nhau."),

dict(
q="Nguyên tắc hoạt động của nhiệt kế thuỷ ngân dựa trên",
o=["sự thay đổi màu sắc của thuỷ ngân theo nhiệt độ.",
   "sự nở vì nhiệt của thuỷ ngân trong ống thuỷ tinh.",
   "sự thay đổi khối lượng của thuỷ ngân theo nhiệt độ.",
   "sự thay đổi điện trở của thuỷ ngân theo nhiệt độ."],
a="B",
e="Nhiệt kế thuỷ ngân dùng tính chất nhiệt nở của chất lỏng: khi nhiệt độ tăng, thể tích thuỷ ngân tăng làm cột thuỷ ngân dâng lên trong ống mao dẫn có tiết diện nhỏ. Sự phụ thuộc của điện trở vào nhiệt độ là nguyên tắc của nhiệt kế điện trở."),

dict(
q="Nhiệt nóng chảy riêng của nước đá là 3,34·10⁵ J/kg. Để làm nóng chảy hoàn toàn 200 g nước đá đang ở 0 °C cần cung cấp nhiệt lượng",
o=["6,68·10⁴ J.", "3,34·10⁵ J.", "1,67·10⁶ J.", "6,68·10⁵ J."],
a="A",
e="Áp dụng Q = λm = 3,34·10⁵ · 0,2 = 6,68·10⁴ J. Lưu ý phải đổi 200 g = 0,2 kg; nếu quên đổi đơn vị hoặc nhân với 2 sẽ ra các đáp án sai còn lại. Vì nước đá đã ở đúng nhiệt độ nóng chảy nên không cần thêm phần nhiệt làm tăng nhiệt độ."),

dict(
q="Đun nóng đẳng áp một khối khí lí tưởng, khí giãn nở đẩy pit-tông đi lên. Nhận định nào sau đây đúng?",
o=["Khí nhận công từ bên ngoài nên công mà khí nhận được A > 0.",
   "Khí thực hiện công lên bên ngoài nên công khí nhận được A < 0.",
   "Khí không trao đổi công với bên ngoài vì áp suất không đổi.",
   "Nội năng của khí giảm đi vì khí phải sinh công đẩy pit-tông."],
a="B",
e="Khí giãn nở, đẩy pit-tông dịch chuyển theo chiều lực do khí tác dụng, tức khí thực hiện công lên bên ngoài; theo quy ước, công mà khí nhận được A < 0. Đồng thời nhiệt độ tăng nên ΔU > 0, do đó nhiệt lượng khí nhận Q = ΔU − A lớn hơn ΔU."),

dict(
q="Nội năng của một vật (nói chung, không chỉ khí lí tưởng) phụ thuộc vào",
o=["chỉ nhiệt độ của vật.",
   "chỉ thể tích của vật.",
   "nhiệt độ và thể tích của vật.",
   "áp suất khí quyển bên ngoài vật."],
a="C",
e="Nội năng gồm động năng chuyển động nhiệt của các phân tử (phụ thuộc nhiệt độ) và thế năng tương tác giữa các phân tử (phụ thuộc khoảng cách giữa chúng, tức phụ thuộc thể tích). Riêng với khí lí tưởng, do bỏ qua tương tác phân tử nên nội năng chỉ còn phụ thuộc nhiệt độ."),

dict(
q="Cho hai vật tiếp xúc nhiệt với nhau. Nhiệt lượng tự truyền theo chiều nào?",
o=["Từ vật có nội năng lớn hơn sang vật có nội năng nhỏ hơn.",
   "Từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn.",
   "Từ vật có khối lượng lớn hơn sang vật có khối lượng nhỏ hơn.",
   "Từ vật có nhiệt dung riêng lớn hơn sang vật có nhiệt dung riêng nhỏ hơn."],
a="B",
e="Chiều truyền nhiệt tự phát được quyết định bởi hiệu nhiệt độ, luôn từ nơi có nhiệt độ cao đến nơi có nhiệt độ thấp cho tới khi cân bằng nhiệt. Một vật có nội năng lớn hơn (ví dụ khối nước lớn ở 30 °C) vẫn có thể nhận nhiệt từ một vật nhỏ nóng hơn (miếng kim loại ở 200 °C)."),

dict(
q="Số phân tử có trong 0,5 mol khí lí tưởng là bao nhiêu? (lấy Nᴀ = 6,02·10²³ mol⁻¹)",
o=["1,204·10²⁴ phân tử.", "6,02·10²³ phân tử.", "3,01·10²³ phân tử.", "1,2·10²² phân tử."],
a="C",
e="Số phân tử N = n·Nᴀ = 0,5 · 6,02·10²³ = 3,01·10²³ phân tử. Kết quả 1,204·10²⁴ ứng với sai lầm nhân đôi thay vì chia đôi. Lưu ý số phân tử không phụ thuộc bản chất khí, chỉ phụ thuộc số mol."),
]
