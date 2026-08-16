# -*- coding: utf-8 -*-
"""PHẦN D - MỨC ĐỘ VẬN DỤNG CAO, CÂU HỎI PHÂN LOẠI (25 câu)"""

PART_D = [
dict(
q="Phát biểu nào sau đây là ĐÚNG?",
o=["Nhiệt lượng tự truyền từ vật có nội năng lớn hơn sang vật có nội năng nhỏ hơn.",
   "Hai vật có cùng nhiệt độ thì có cùng nội năng.",
   "Vật có nhiệt độ cao hơn thì luôn có nội năng lớn hơn.",
   "Hai vật ở cùng nhiệt độ tiếp xúc nhau thì giữa chúng không có sự truyền nhiệt theo một chiều xác định."],
a="D",
e="Chiều truyền nhiệt tự phát do hiệu nhiệt độ quyết định, nên khi hai vật cùng nhiệt độ thì không còn dòng nhiệt có hướng: đó là trạng thái cân bằng nhiệt. Nội năng là đại lượng cộng tính, phụ thuộc khối lượng và bản chất chất, nên hai vật cùng nhiệt độ hoàn toàn có thể có nội năng rất khác nhau, và vật nóng hơn chưa chắc có nội năng lớn hơn (một que diêm cháy so với cả một hồ nước)."),

dict(
q="Đặt một viên bi sắt khối lượng 10 g ở 200 °C vào một cốc chứa 1 kg nước ở 30 °C. Kết luận nào sau đây đúng?",
o=["Nhiệt lượng truyền từ viên bi sang nước vì viên bi có nhiệt độ cao hơn.",
   "Nhiệt lượng truyền từ nước sang viên bi vì nước có nội năng lớn hơn nhiều.",
   "Không có sự truyền nhiệt vì khối lượng viên bi quá nhỏ so với nước.",
   "Nhiệt truyền qua lại cho tới khi hai vật có nội năng bằng nhau."],
a="A",
e="Dù nội năng của cốc nước lớn hơn nội năng viên bi rất nhiều, chiều truyền nhiệt chỉ phụ thuộc hiệu nhiệt độ: nhiệt truyền từ viên bi nóng (200 °C) sang nước (30 °C) cho đến khi hai vật cùng nhiệt độ (chỉ tăng lên rất ít vì khối lượng nước lớn). Điều kiện dừng là cân bằng về nhiệt độ, không phải cân bằng về nội năng."),

dict(
q="Trong suốt quá trình nước đang sôi ở áp suất không đổi, phát biểu nào sau đây đúng?",
o=["Nước không nhận thêm nhiệt lượng nào nữa vì nhiệt độ của nước đã không còn tăng lên.",
   "Nội năng của lượng nước và hơi nước không đổi vì nhiệt độ của hệ được giữ nguyên ở 100 °C.",
   "Nước vẫn nhận nhiệt lượng và nội năng của hệ tăng, do thế năng tương tác giữa các phân tử tăng khi chuyển sang thể hơi.",
   "Động năng chuyển động nhiệt trung bình của các phân tử tăng dần theo thời gian vì nước liên tục nhận nhiệt."],
a="C",
e="Nhiệt độ không đổi chỉ có nghĩa động năng chuyển động nhiệt trung bình của phân tử không đổi. Nhiệt lượng vẫn liên tục được cung cấp và được dùng để tách các phân tử ra xa nhau khi chuyển từ thể lỏng sang thể hơi, tức làm tăng thế năng tương tác phân tử. Do đó nội năng của hệ tăng dù nhiệt độ đứng yên: 'nhiệt độ không đổi' không đồng nghĩa với 'nội năng không đổi'."),

dict(
q="Nén một khối khí lí tưởng từ thể tích V₁ xuống V₂ theo hai cách: (1) nén rất chậm trong xilanh dẫn nhiệt tốt; (2) nén rất nhanh trong xilanh cách nhiệt. So sánh áp suất khí ở cuối quá trình trong hai cách, ta có",
o=["áp suất trong cách (1) lớn hơn.",
   "áp suất trong cách (2) lớn hơn.",
   "hai áp suất bằng nhau vì thể tích cuối như nhau.",
   "hai áp suất bằng nhau vì khối lượng khí như nhau."],
a="B",
e="Cách (1) là quá trình đẳng nhiệt: nhiệt độ cuối bằng nhiệt độ đầu. Cách (2) gần đúng là đoạn nhiệt: khí nhận công mà không kịp toả nhiệt nên ΔU = A > 0, nhiệt độ cuối cao hơn. Với cùng thể tích cuối V₂, từ p = nRT/V₂ suy ra khí có nhiệt độ cao hơn sẽ có áp suất lớn hơn. Vậy nén nhanh cho áp suất cuối lớn hơn — thể tích cuối giống nhau không đủ để kết luận áp suất giống nhau."),

dict(
q="Đun nóng không khí chứa trong một bình miệng để hở thông với khí quyển, từ 27 °C lên 127 °C. Phát biểu nào sau đây đúng?",
o=["Áp suất không khí trong bình tăng 4/3 lần.",
   "Thể tích khối không khí trong bình tăng 4/3 lần còn khối lượng không đổi.",
   "Khối lượng không khí còn lại trong bình giảm đi.",
   "Có thể áp dụng hệ thức p₁V₁/T₁ = p₂V₂/T₂ cho toàn bộ không khí ban đầu trong bình."],
a="C",
e="Bình hở nên áp suất khí trong bình luôn bằng áp suất khí quyển (không đổi) và thể tích bình cũng không đổi. Từ p = (m/M)RT/V, khi T tăng mà p, V giữ nguyên thì m phải giảm: một phần không khí đã tràn ra ngoài. Phương trình trạng thái pV/T = hằng số chỉ áp dụng được cho một khối lượng khí xác định, nên không dùng được cho toàn bộ lượng khí ban đầu — đây là bẫy phổ biến nhất của dạng bài này."),

dict(
q="Một bình kín, thành cứng chứa khí lí tưởng được mang từ chân núi lên đỉnh núi cao, nhiệt độ khí được giữ không đổi. Áp suất khí bên trong bình sẽ",
o=["giảm vì áp suất khí quyển bên ngoài giảm.",
   "tăng vì áp suất khí quyển bên ngoài giảm.",
   "không đổi.",
   "giảm đúng bằng độ giảm của áp suất khí quyển."],
a="C",
e="Áp suất của khí trong bình được xác định bởi trạng thái của chính khối khí đó: p = (N/V)kT. Bình kín (N không đổi), thành cứng (V không đổi) và nhiệt độ không đổi nên p không đổi, hoàn toàn độc lập với áp suất khí quyển bên ngoài. Áp suất bên ngoài chỉ ảnh hưởng tới lực tác dụng lên thành bình chứ không quyết định áp suất khí bên trong."),

dict(
q="Một khối khí xác định được đun nóng đẳng áp từ 20 °C lên 40 °C. Một học sinh kết luận rằng thể tích khí tăng gấp đôi. Kết luận đúng phải là thể tích khí",
o=["tăng gấp đôi.", "tăng khoảng 6,8%.", "tăng khoảng 50%.", "không đổi."],
a="B",
e="Định luật Charles đòi hỏi dùng nhiệt độ tuyệt đối: T₁ = 293 K, T₂ = 313 K. Do đó V₂/V₁ = 313/293 ≈ 1,068, tức thể tích chỉ tăng khoảng 6,8%. Sai lầm của học sinh là lấy tỉ số nhiệt độ Celsius 40/20 = 2 — một trong những lỗi kinh điển nhất của phần khí lí tưởng."),

dict(
q="Trong hệ toạ độ (p, V), hai đường đẳng nhiệt ứng với hai nhiệt độ khác nhau của cùng một khối lượng khí lí tưởng",
o=["cắt nhau tại đúng một điểm.",
   "cắt nhau tại hai điểm.",
   "không bao giờ cắt nhau.",
   "có thể cắt nhau nếu áp suất đủ lớn."],
a="C",
e="Nếu hai đường cắt nhau tại một điểm thì tại điểm đó khối khí vừa có cặp giá trị (p, V) xác định vừa có hai nhiệt độ khác nhau — điều này mâu thuẫn với phương trình trạng thái T = pV/(nR), vốn cho mỗi cặp (p, V) đúng một giá trị T. Vậy các đường đẳng nhiệt của cùng một khối khí không bao giờ cắt nhau; đường ứng với nhiệt độ cao hơn nằm xa gốc toạ độ hơn."),

dict(
q="Đồ thị biểu diễn một quá trình biến đổi trạng thái của một khối lượng khí lí tưởng xác định trong hệ toạ độ (p, T) là một đường thẳng KHÔNG đi qua gốc toạ độ. Kết luận nào sau đây đúng?",
o=["Đó chắc chắn là quá trình đẳng tích của khối khí.",
   "Đó chắc chắn là quá trình đẳng áp của khối khí.",
   "Đó chắc chắn là quá trình đẳng nhiệt của khối khí.",
   "Thể tích của khối khí thay đổi trong quá trình đó."],
a="D",
e="Quá trình đẳng tích trong hệ (p, T) phải là đường thẳng đi qua gốc toạ độ vì p = (nR/V)T. Đường thẳng không qua gốc có dạng p = aT + b với b ≠ 0, khi đó V = nRT/p = nRT/(aT + b) thay đổi theo T. Vậy chắc chắn thể tích khí biến đổi; đây là bẫy đồ thị rất hay gặp vì học sinh chỉ nhớ 'đường thẳng trong (p, T) là đẳng tích'."),

dict(
q="Cung cấp cùng một nhiệt lượng cho 1 kg nước (c = 4200 J/(kg·K)) và 1 kg dầu (c = 2100 J/(kg·K)), cả hai đều không chuyển thể. Kết luận nào sau đây đúng?",
o=["Nước tăng nhiệt độ nhiều hơn dầu 2 lần.",
   "Dầu tăng nhiệt độ nhiều hơn nước 2 lần.",
   "Hai chất tăng nhiệt độ như nhau vì nhận cùng nhiệt lượng.",
   "Dầu tăng nhiệt độ nhiều hơn nước 4 lần."],
a="B",
e="Từ Q = mcΔT với Q và m như nhau, độ tăng nhiệt độ ΔT = Q/(mc) tỉ lệ nghịch với nhiệt dung riêng. Vì c_dầu chỉ bằng một nửa c_nước nên ΔT của dầu gấp đôi của nước. Đây cũng là lí do dầu trong chảo nóng lên rất nhanh so với nước."),

dict(
q="Bật một quạt điện chạy liên tục trong một căn phòng kín và cách nhiệt hoàn toàn với bên ngoài. Sau một thời gian dài, nhiệt độ không khí trong phòng sẽ",
o=["giảm vì quạt làm mát không khí.",
   "không đổi vì quạt chỉ làm không khí chuyển động.",
   "tăng lên chút ít.",
   "giảm rồi tăng trở lại giá trị ban đầu."],
a="C",
e="Phòng cách nhiệt nên năng lượng không thoát ra ngoài, trong khi quạt liên tục nhận điện năng và chuyển hoá nó thành động năng của dòng khí rồi cuối cùng thành nội năng của không khí (qua ma sát, nhớt) cùng với nhiệt toả ra từ động cơ. Vì vậy nội năng và nhiệt độ không khí tăng dần. Ta thấy mát khi đứng trước quạt là do gió làm mồ hôi bay hơi nhanh hơn, chứ không phải do quạt hạ nhiệt độ phòng."),

dict(
q="Vì sao hơi nước ở 100 °C gây bỏng nặng hơn nhiều so với nước lỏng ở 100 °C khi tiếp xúc với da?",
o=["Vì trên thực tế hơi nước bao giờ cũng có nhiệt độ cao hơn 100 °C.",
   "Vì hơi nước có nhiệt dung riêng lớn hơn nhiều so với nước lỏng.",
   "Vì hơi nước tiếp xúc và dẫn nhiệt vào da tốt hơn nhiều so với nước lỏng.",
   "Vì khi ngưng tụ trên da, hơi nước toả thêm một nhiệt lượng rất lớn bằng L·m."],
a="D",
e="Cả hai đều ở 100 °C nên phần nhiệt toả ra do hạ nhiệt độ xuống nhiệt độ của da là như nhau. Nhưng hơi nước còn phải ngưng tụ trước, quá trình này toả thêm nhiệt lượng Q = Lm với L = 2,26·10⁶ J/kg — lớn gấp nhiều lần phần nhiệt do hạ nhiệt độ. Chính lượng nhiệt ngưng tụ này gây bỏng nặng."),

dict(
q="Ở nhiệt độ phòng, tốc độ trung bình của phân tử khí vào cỡ hàng trăm mét trên giây. Tuy nhiên khi mở một lọ nước hoa ở góc phòng, phải mất khá lâu người ở góc đối diện mới ngửi thấy mùi. Nguyên nhân là",
o=["các phân tử nước hoa có khối lượng lớn nên chuyển động nhiệt chậm hơn hẳn phân tử không khí, phải rất lâu mới đi hết căn phòng.",
   "các phân tử nước hoa liên tục va chạm với phân tử không khí nên đi theo đường zic-zắc, quãng đường thực tế dài hơn rất nhiều khoảng cách thẳng.",
   "các phân tử nước hoa gần như đứng yên tại chỗ và chỉ chuyển động được khi có gió trong phòng thổi chúng đi xa.",
   "các phân tử nước hoa mất dần động năng do lực hút của Trái Đất nên chuyển động chậm dần rồi rơi xuống sàn nhà."],
a="B",
e="Trong không khí ở điều kiện thường, mật độ phân tử rất lớn (cỡ 10²⁵ phân tử/m³) nên quãng đường tự do trung bình chỉ khoảng 10⁻⁷ m: mỗi phân tử va chạm hàng tỉ lần mỗi giây và chuyển động theo đường gấp khúc hỗn loạn. Vì thế tốc độ khuếch tán theo một hướng nhỏ hơn rất nhiều tốc độ chuyển động nhiệt tức thời của phân tử."),

dict(
q="Một khối lượng khí lí tưởng xác định lần lượt ở bốn trạng thái: (1) p = 1·10⁵ Pa, V = 2 L; (2) p = 1·10⁵ Pa, V = 6 L; (3) p = 3·10⁵ Pa, V = 6 L; (4) p = 3·10⁵ Pa, V = 2 L. Phát biểu nào sau đây đúng?",
o=["Trạng thái 3 có nhiệt độ cao nhất và hai trạng thái 2, 4 có cùng nhiệt độ.",
   "Trạng thái 4 có nhiệt độ cao nhất vì có áp suất lớn nhất.",
   "Trạng thái 2 có nhiệt độ cao hơn trạng thái 4 vì có thể tích lớn hơn.",
   "Bốn trạng thái có nhiệt độ bằng nhau."],
a="A",
e="Vì T = pV/(nR) nên nhiệt độ tỉ lệ với tích pV. Tính tích pV (đơn vị 10⁵ Pa·L): trạng thái 1 được 2; trạng thái 2 được 6; trạng thái 3 được 18; trạng thái 4 được 6. Vậy trạng thái 3 nóng nhất, trạng thái 1 lạnh nhất, còn trạng thái 2 và 4 có cùng nhiệt độ dù p và V của chúng khác hẳn nhau. Sai lầm điển hình là so sánh nhiệt độ chỉ dựa vào riêng áp suất hoặc riêng thể tích."),

dict(
q="Một xilanh nằm ngang, cách nhiệt với bên ngoài, được chia thành hai phần chứa khí bởi một pit-tông mỏng, nhẹ, dẫn nhiệt kém và có thể trượt không ma sát. Đun nóng khí ở phần bên trái. Kết luận nào sau đây đúng?",
o=["Áp suất khí phần bên trái lớn hơn áp suất khí phần bên phải.",
   "Pit-tông dịch sang phải, áp suất khí ở hai phần luôn bằng nhau và cùng tăng lên.",
   "Pit-tông đứng yên vì khối lượng khí hai bên không đổi.",
   "Pit-tông dịch sang trái vì khí bên trái bị nén."],
a="B",
e="Pit-tông nhẹ, không ma sát nên tại mọi thời điểm nó cân bằng, tức áp suất khí hai bên luôn bằng nhau. Khí bên trái nóng lên và giãn ra, đẩy pit-tông sang phải; khí bên phải bị nén nên áp suất tăng, kéo theo áp suất bên trái cũng tăng đúng bằng như vậy. Bẫy ở đây là suy nghĩ 'bên nào bị đun nóng thì bên đó có áp suất lớn hơn'."),

dict(
q="Một bóng thám không chứa khí lí tưởng, ở mặt đất có p₁ = 1,0·10⁵ Pa và T₁ = 300 K. Khi lên tới độ cao mà p₂ = 0,25·10⁵ Pa và T₂ = 240 K (vỏ bóng đàn hồi, khí không thoát ra ngoài), thể tích của bóng",
o=["giảm 3,2 lần vì nhiệt độ giảm.",
   "tăng 4 lần vì áp suất giảm 4 lần.",
   "tăng 3,2 lần.",
   "tăng 5 lần."],
a="C",
e="Áp dụng phương trình trạng thái: V₂/V₁ = (p₁/p₂)·(T₂/T₁) = 4 · (240/300) = 4 · 0,8 = 3,2. Cả hai yếu tố cùng tác dụng nhưng ngược chiều: giảm áp suất làm khí giãn 4 lần, còn giảm nhiệt độ kéo lại 0,8 lần; kết quả thể tích vẫn tăng 3,2 lần. Chỉ nhìn một trong hai yếu tố sẽ dẫn tới hai phương án sai còn lại."),

dict(
q="So sánh nội năng của 1 kg nước đá ở 0 °C với nội năng của 1 kg nước lỏng ở 0 °C (cùng áp suất), ta có",
o=["nội năng của nước đá lớn hơn.",
   "nội năng của nước lỏng lớn hơn.",
   "hai nội năng bằng nhau vì cùng nhiệt độ.",
   "không so sánh được vì hai chất ở hai thể khác nhau."],
a="B",
e="Muốn biến 1 kg nước đá ở 0 °C thành 1 kg nước ở 0 °C phải cung cấp thêm nhiệt lượng nóng chảy λm = 3,34·10⁵ J mà nhiệt độ không đổi, tức không có công đáng kể nào được sinh ra. Theo định luật I, toàn bộ nhiệt lượng đó làm tăng nội năng (dưới dạng thế năng tương tác phân tử). Vậy nước lỏng ở 0 °C có nội năng lớn hơn nước đá ở 0 °C đúng một lượng λm — cùng nhiệt độ không có nghĩa là cùng nội năng."),

dict(
q="Đun nóng đẳng áp một khối khí lí tưởng từ 27 °C lên 327 °C. Khối lượng riêng của khối khí đó",
o=["tăng 2 lần.", "giảm 2 lần.", "không đổi.", "giảm 12,1 lần."],
a="B",
e="Trong quá trình đẳng áp với khối lượng khí không đổi, V tỉ lệ thuận với nhiệt độ tuyệt đối: T tăng từ 300 K lên 600 K nên V tăng 2 lần. Khối lượng riêng ρ = m/V với m không đổi nên ρ giảm 2 lần. Đây chính là cơ chế làm khí nóng bốc lên cao và làm khinh khí cầu bay được."),

dict(
q="Nhỏ vài giọt cồn lên mặt bàn trong một bình cách nhiệt kín; cồn bay hơi dần. Nhiệt độ của phần cồn lỏng còn lại sẽ giảm. Giải thích vi mô đúng nhất là",
o=["các phân tử cồn có động năng lớn nhất thoát ra khỏi mặt thoáng trước, làm động năng trung bình của các phân tử còn lại giảm.",
   "các phân tử cồn còn lại bị nén chặt hơn khi thể tích khối cồn giảm dần, nên chuyển động của chúng chậm hẳn lại.",
   "khối lượng cồn giảm dần trong quá trình bay hơi nên nhiệt dung riêng của khối cồn còn lại cũng giảm theo.",
   "hơi cồn bay lên thu nhiệt của không khí phía trên chứ không lấy nhiệt của phần cồn lỏng còn lại."],
a="A",
e="Ở mọi nhiệt độ, các phân tử chất lỏng có động năng phân bố khác nhau; chỉ những phân tử ở gần mặt thoáng có động năng đủ lớn để thắng lực hút của các phân tử xung quanh mới thoát ra được. Việc các phân tử 'nhanh nhất' liên tục rời đi làm động năng trung bình của phần chất lỏng còn lại giảm, tức nhiệt độ giảm. Đó là bản chất của hiện tượng bay hơi thu nhiệt."),

dict(
q="Khi hạ nhiệt độ xuống rất thấp, đồ thị thực nghiệm biểu diễn áp suất theo nhiệt độ của một chất khí thực (giữ thể tích không đổi) lệch khỏi đường thẳng lí thuyết. Nguyên nhân là",
o=["các dụng cụ đo áp suất và nhiệt độ luôn kém chính xác ở vùng nhiệt độ rất thấp, làm số liệu bị lệch khỏi đường thẳng.",
   "hằng số Boltzmann và hằng số khí lí tưởng đều giảm dần khi nhiệt độ của khối khí hạ xuống thấp hơn nhiệt độ phòng.",
   "ở nhiệt độ thấp, tương tác giữa các phân tử và kích thước phân tử không còn bỏ qua được, khí thực hoá lỏng nên mô hình khí lí tưởng không còn áp dụng được.",
   "khối lượng của mỗi phân tử khí giảm đi khi nhiệt độ giảm nên áp suất khí không còn tỉ lệ với nhiệt độ tuyệt đối."],
a="C",
e="Khí lí tưởng là mô hình gần đúng, chỉ hợp lí khi động năng nhiệt lớn hơn nhiều so với thế năng tương tác phân tử. Khi nhiệt độ giảm mạnh, lực hút giữa các phân tử trở nên đáng kể, chất khí ngưng tụ thành lỏng và các định luật chất khí không còn nghiệm đúng. Hằng số Boltzmann và khối lượng phân tử đều không phụ thuộc nhiệt độ."),

dict(
q="Một khối khí lí tưởng nhận được nhiệt lượng Q > 0 nhưng nội năng của nó lại giảm. Điều đó xảy ra khi",
o=["khí đồng thời nhận thêm công từ môi trường bên ngoài.",
   "khí đồng thời thực hiện công lên bên ngoài với độ lớn lớn hơn Q.",
   "khí biến đổi trạng thái theo một quá trình đẳng tích.",
   "điều này không bao giờ xảy ra đối với khí lí tưởng."],
a="B",
e="Định luật I: ΔU = A + Q. Với Q > 0 mà ΔU < 0 thì bắt buộc A < −Q < 0, tức khí thực hiện công lên bên ngoài với độ lớn lớn hơn nhiệt lượng nhận được (khí giãn nở mạnh và nguội đi). Nếu khí nhận thêm công (A > 0) thì ΔU chắc chắn dương; còn đẳng tích thì A = 0 nên ΔU = Q > 0."),

dict(
q="Giãn đẳng nhiệt một khối khí lí tưởng, áp suất khí giảm. Giải thích theo mô hình động học phân tử là",
o=["mỗi phân tử va chạm vào thành bình yếu hơn trước vì tốc độ của các phân tử giảm khi khí giãn nở, còn số va chạm thì giữ nguyên.",
   "lực hút giữa các phân tử khí tăng lên khi thể tích tăng, giữ các phân tử lại nên chúng ít va chạm vào thành bình hơn.",
   "khối lượng của mỗi phân tử khí giảm đi khi khí giãn nở nên xung lượng truyền cho thành bình trong mỗi va chạm giảm.",
   "động năng trung bình mỗi phân tử không đổi, nhưng mật độ phân tử giảm nên số va chạm lên mỗi đơn vị diện tích thành bình trong mỗi đơn vị thời gian giảm."],
a="D",
e="Nhiệt độ không đổi nên động năng tịnh tiến trung bình của mỗi phân tử (3/2)kT không đổi, tức mỗi va chạm vẫn 'mạnh' như trước. Khi thể tích tăng, mật độ phân tử N/V giảm, số va chạm lên một đơn vị diện tích thành bình trong một đơn vị thời gian giảm theo, do đó áp suất p = (2/3)(N/V)Eđ giảm. Giải thích “mỗi va chạm yếu đi do tốc độ phân tử giảm” là sai, vì trong quá trình đẳng nhiệt tốc độ phân tử không thay đổi."),

dict(
q="Đun nóng đẳng tích một khối khí lí tưởng làm áp suất tăng. Theo mô hình động học phân tử, nguyên nhân là",
o=["mật độ phân tử khí trong bình tăng lên khi nhiệt độ tăng nên số va chạm lên thành bình nhiều hơn.",
   "các phân tử chuyển động nhanh hơn nên vừa va chạm mạnh hơn, vừa va chạm vào thành bình thường xuyên hơn.",
   "các phân tử khí nở ra vì nhiệt nên chiếm nhiều chỗ hơn và ép mạnh hơn lên thành bình.",
   "lực đẩy giữa các phân tử khí tăng lên khi nhiệt độ tăng, đẩy các phân tử ép mạnh vào thành bình."],
a="B",
e="Đẳng tích và bình kín nên mật độ phân tử N/V không đổi. Khi nhiệt độ tăng, tốc độ trung bình của các phân tử tăng: mỗi va chạm truyền cho thành bình xung lượng lớn hơn, đồng thời số lần va chạm trong mỗi đơn vị thời gian cũng tăng. Cả hai yếu tố cùng làm áp suất tăng, đúng như hệ thức p = (N/V)kT. Kích thước phân tử và lực đẩy phân tử không phụ thuộc nhiệt độ theo cách nêu ở các phương án còn lại."),

dict(
q="Phát biểu nào sau đây là ĐÚNG với một khối lượng khí lí tưởng xác định?",
o=["Khi nhiệt độ của khí tăng thì áp suất của khí luôn tăng, dù thể tích thay đổi thế nào.",
   "Khi thể tích của khí giảm thì áp suất của khí luôn tăng, dù nhiệt độ thay đổi thế nào.",
   "Khi áp suất của khí tăng thì nhiệt độ của khí luôn tăng, dù thể tích thay đổi thế nào.",
   "Khi nhiệt độ và thể tích của khí cùng tăng thì áp suất có thể tăng, giảm hoặc không đổi."],
a="D",
e="Ba đại lượng p, V, T ràng buộc nhau bởi pV/T = hằng số, nên không thể kết luận về một đại lượng khi chỉ biết chiều biến đổi của một đại lượng khác. Phản ví dụ cho “nhiệt độ tăng thì áp suất luôn tăng”: đun nóng đẳng áp, T tăng mà p không đổi. Phản ví dụ cho “thể tích giảm thì áp suất luôn tăng”: nếu vừa giảm thể tích vừa hạ nhiệt độ thật mạnh (chẳng hạn V giảm 2 lần trong khi T giảm 4 lần) thì p vẫn giảm. Phản ví dụ cho “áp suất tăng thì nhiệt độ luôn tăng”: nén đẳng nhiệt làm p tăng mà T không đổi. Chỉ nhận định về trường hợp nhiệt độ và thể tích cùng tăng mới phản ánh đúng bản chất: khi T và V cùng tăng, p = nRT/V phụ thuộc vào việc đại lượng nào tăng nhanh hơn."),

dict(
q="Một khối lượng khí lí tưởng xác định biến đổi trạng thái sao cho áp suất của nó luôn tỉ lệ nghịch với nhiệt độ tuyệt đối. Nếu nhiệt độ tuyệt đối của khí tăng gấp đôi thì thể tích của khí",
o=["tăng 2 lần.", "tăng 4 lần.", "không đổi.", "giảm 2 lần."],
a="B",
e="Điều kiện p tỉ lệ nghịch với T nghĩa là p = a/T. Thay vào phương trình trạng thái pV/T = C: (a/T)·V/T = C ⇒ V = (C/a)·T², tức thể tích tỉ lệ với bình phương nhiệt độ tuyệt đối. Khi T tăng gấp đôi thì V tăng 2² = 4 lần. Phương án 'tăng 2 lần' là bẫy dành cho học sinh áp dụng máy móc định luật Charles mà quên rằng ở đây áp suất cũng đang thay đổi."),
]
