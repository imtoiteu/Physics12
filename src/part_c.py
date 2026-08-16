# -*- coding: utf-8 -*-
"""PHẦN C - MỨC ĐỘ VẬN DỤNG (30 câu)"""

PART_C = [
dict(
q="Dùng cùng một bếp có công suất không đổi để đun hai khối lượng bằng nhau của hai chất rắn kết tinh X và Y (ban đầu cả hai đều ở đúng nhiệt độ nóng chảy của chúng). Đoạn nằm ngang trên đồ thị nhiệt độ – thời gian của chất X dài gấp đôi của chất Y. Kết luận nào sau đây đúng?",
o=["Nhiệt nóng chảy riêng của X gấp đôi của Y.",
   "Nhiệt nóng chảy riêng của Y gấp đôi của X.",
   "Nhiệt độ nóng chảy của X gấp đôi của Y.",
   "Nhiệt dung riêng của X gấp đôi của Y."],
a="A",
e="Cùng công suất P nên nhiệt lượng cung cấp tỉ lệ với thời gian: Q = Pt. Trong đoạn nằm ngang, toàn bộ nhiệt lượng dùng cho sự nóng chảy: Pt = λm. Với m như nhau, thời gian dài gấp đôi ứng với λ lớn gấp đôi. Độ dài đoạn nằm ngang không liên quan đến nhiệt độ nóng chảy (đó là độ cao của đoạn đó) hay nhiệt dung riêng (thể hiện ở độ dốc các đoạn xiên)."),

dict(
q="Đun một chất bằng bếp có công suất không đổi. Trên đồ thị nhiệt độ – thời gian, đoạn ứng với chất ở thể rắn có độ dốc gấp đôi đoạn ứng với chất ở thể lỏng. Gọi cᵣ và cₗ lần lượt là nhiệt dung riêng của chất ở thể rắn và thể lỏng, ta có",
o=["cᵣ = 2cₗ.", "cᵣ = cₗ.", "cᵣ = cₗ/2.", "cᵣ = 4cₗ."],
a="C",
e="Trong các đoạn xiên: Pt = mcΔT, suy ra độ dốc ΔT/t = P/(mc), tức độ dốc tỉ lệ nghịch với nhiệt dung riêng. Đoạn có độ dốc gấp đôi ứng với nhiệt dung riêng nhỏ đi một nửa, vậy cᵣ = cₗ/2. Đây là bẫy phổ biến: nhiều học sinh cho rằng dốc hơn nghĩa là nhiệt dung riêng lớn hơn."),

dict(
q="Trộn 1 kg nước ở 20 °C với 2 kg nước ở 80 °C trong một bình cách nhiệt lí tưởng. Nhiệt độ của hỗn hợp khi cân bằng nhiệt là",
o=["50 °C.", "60 °C.", "40 °C.", "70 °C."],
a="B",
e="Phương trình cân bằng nhiệt: 1·c·(t − 20) = 2·c·(80 − t) ⇒ t − 20 = 160 − 2t ⇒ 3t = 180 ⇒ t = 60 °C. Nhiệt độ cân bằng là trung bình có trọng số theo khối lượng chứ không phải trung bình cộng 50 °C — đó chính là phương án bẫy."),

dict(
q="Thả 100 g nước đá ở 0 °C vào 100 g nước ở 100 °C trong bình cách nhiệt (bỏ qua nhiệt dung của bình). Cho c_nước = 4200 J/(kg·K), λ_nước đá = 3,34·10⁵ J/kg. Nhiệt độ khi cân bằng nhiệt xấp xỉ",
o=["0 °C.", "50 °C.", "10,2 °C.", "20,5 °C."],
a="C",
e="Nhiệt lượng nước nóng có thể toả ra khi hạ tới 0 °C là 0,1·4200·100 = 42 000 J, lớn hơn nhiệt lượng cần làm tan hết đá là 0,1·3,34·10⁵ = 33 400 J, nên đá tan hết và nhiệt độ cuối lớn hơn 0 °C. Cân bằng nhiệt: 0,1·4200·(100 − t) = 33 400 + 0,1·4200·t ⇒ 8 600 = 840t ⇒ t ≈ 10,2 °C. Đáp án 50 °C là bẫy do quên hoàn toàn nhiệt nóng chảy."),

dict(
q="Thả 100 g nước đá ở 0 °C vào 100 g nước ở 20 °C trong bình cách nhiệt (c_nước = 4200 J/(kg·K), λ = 3,34·10⁵ J/kg). Trạng thái cuối cùng của hỗn hợp là",
o=["toàn bộ ở thể lỏng, nhiệt độ khoảng 10 °C.",
   "toàn bộ ở thể lỏng, nhiệt độ 0 °C.",
   "hỗn hợp nước đá và nước, nhiệt độ 0 °C.",
   "toàn bộ ở thể rắn, nhiệt độ 0 °C."],
a="C",
e="Nhiệt lượng tối đa mà nước ở 20 °C có thể toả ra khi hạ xuống 0 °C là 0,1·4200·20 = 8 400 J, nhỏ hơn nhiều so với 33 400 J cần để làm tan hết đá. Do đó chỉ khoảng 8 400/(3,34·10⁵) ≈ 0,025 kg = 25 g đá tan; phần đá còn lại vẫn tồn tại và hệ dừng ở 0 °C. Khi còn cả nước và nước đá cùng tồn tại thì nhiệt độ hỗn hợp bắt buộc bằng nhiệt độ nóng chảy."),

dict(
q="Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg. So sánh nhiệt lượng Q₁ cần để đun 1 kg nước từ 20 °C đến 100 °C với nhiệt lượng Q₂ cần để hoá hơi hoàn toàn 1 kg nước đó ở 100 °C, ta thấy",
o=["Q₂ lớn hơn Q₁ khoảng 6,7 lần.",
   "Q₂ lớn hơn Q₁ khoảng 2,3 lần.",
   "Q₁ lớn hơn Q₂ khoảng 6,7 lần.",
   "Q₁ và Q₂ xấp xỉ bằng nhau."],
a="A",
e="Q₁ = 1·4200·80 = 3,36·10⁵ J; Q₂ = 1·2,26·10⁶ = 2,26·10⁶ J. Tỉ số Q₂/Q₁ ≈ 6,7. Kết quả này giải thích vì sao nước sôi cạn rất lâu so với thời gian đun tới sôi, và vì sao hơi nước ở 100 °C mang theo năng lượng lớn hơn nhiều so với nước ở 100 °C."),

dict(
q="Trong thí nghiệm đo nhiệt dung riêng của nước, người ta dùng điện trở đun nước trong một bình chứa và đo công của dòng điện. Nếu bình không được cách nhiệt tốt (một phần nhiệt hao phí ra môi trường) thì giá trị nhiệt dung riêng đo được sẽ",
o=["nhỏ hơn giá trị thực.",
   "lớn hơn giá trị thực.",
   "bằng đúng giá trị thực.",
   "lớn hơn hay nhỏ hơn tuỳ theo nhiệt độ phòng cao hay thấp."],
a="B",
e="Người làm thí nghiệm tính c = A_điện/(mΔt) với giả thiết toàn bộ điện năng biến thành nội năng của nước. Thực tế A_điện = Q_nước nhận + Q_hao phí, nên A_điện lớn hơn nhiệt lượng nước thực nhận, dẫn tới c đo được lớn hơn giá trị thực. Muốn giảm sai số này phải bọc cách nhiệt tốt và khuấy đều."),

dict(
q="Khi làm thí nghiệm đo nhiệt nóng chảy riêng của nước đá, một học sinh lấy nước đá từ ngăn đông ở −8 °C nhưng vẫn coi nước đá bắt đầu ở 0 °C. Giá trị nhiệt nóng chảy riêng thu được sẽ",
o=["nhỏ hơn giá trị thực.",
   "bằng giá trị thực vì nước đá vẫn tan hết.",
   "lớn hơn giá trị thực.",
   "không xác định được vì sai số ngẫu nhiên."],
a="C",
e="Một phần nhiệt lượng cung cấp thực ra được dùng để đưa nước đá từ −8 °C lên 0 °C, nhưng học sinh lại quy toàn bộ nhiệt lượng đó cho quá trình nóng chảy khi tính λ = Q/m. Vì tử số bị tính dư nên λ đo được lớn hơn giá trị thực. Đây là sai số hệ thống, không phải sai số ngẫu nhiên."),

dict(
q="Một bọt khí nổi lên từ đáy một hồ nước sâu 10 m. Coi nhiệt độ nước không đổi theo độ sâu, áp suất khí quyển là 1,0·10⁵ Pa, khối lượng riêng của nước 1000 kg/m³, g = 10 m/s². Khi lên tới mặt nước, thể tích bọt khí",
o=["không đổi.", "tăng 2 lần.", "tăng 10 lần.", "giảm 2 lần."],
a="B",
e="Áp suất ở đáy hồ: p₁ = p₀ + ρgh = 1,0·10⁵ + 1000·10·10 = 2,0·10⁵ Pa; ở mặt nước p₂ = 1,0·10⁵ Pa. Nhiệt độ không đổi nên theo định luật Boyle: V₂/V₁ = p₁/p₂ = 2. Bẫy thường gặp là chỉ lấy áp suất cột nước mà quên cộng áp suất khí quyển."),

dict(
q="Một cột khí bị giam trong ống nghiệm thẳng đứng bởi một cột thuỷ ngân, ban đầu miệng ống hướng lên trên. Lật ngược ống cho miệng hướng xuống dưới (thuỷ ngân không chảy ra, nhiệt độ không đổi). So với ban đầu, chiều dài cột khí sẽ",
o=["giảm đi.", "không đổi.", "tăng lên.", "tăng hay giảm tuỳ khối lượng thuỷ ngân."],
a="C",
e="Khi miệng ống hướng lên, áp suất cột khí là p = p₀ + p_Hg (khí đỡ cả khí quyển và cột thuỷ ngân). Khi lật ngược, p = p₀ − p_Hg, nhỏ hơn trước. Nhiệt độ và khối lượng khí không đổi nên theo định luật Boyle, áp suất giảm thì thể tích tăng, tức cột khí dài ra."),

dict(
q="Một khối khí được chứa trong xilanh đặt thẳng đứng, phía trên có pit-tông nhẹ chuyển động không ma sát và hở ra khí quyển. Khi đun nóng khối khí, quá trình biến đổi trạng thái của khí là",
o=["quá trình đẳng tích.", "quá trình đẳng nhiệt.", "quá trình đẳng áp.", "quá trình không có đại lượng nào không đổi."],
a="C",
e="Pit-tông nhẹ, không ma sát và tự do dịch chuyển nên luôn cân bằng, khi đó áp suất khí trong xilanh luôn bằng áp suất khí quyển cộng áp suất do trọng lượng pit-tông (đều không đổi). Vậy áp suất khí không đổi: quá trình là đẳng áp, khí giãn nở khi được đun nóng."),

dict(
q="Một bình kín, cứng chứa khí ở 27 °C có áp suất 1,0·10⁵ Pa. Nung khối khí đến 127 °C thì áp suất khí trong bình bằng",
o=["1,33·10⁵ Pa.", "4,70·10⁵ Pa.", "0,75·10⁵ Pa.", "2,00·10⁵ Pa."],
a="A",
e="Bình kín và cứng nên quá trình là đẳng tích: p₁/T₁ = p₂/T₂ với T₁ = 300 K, T₂ = 400 K. Suy ra p₂ = p₁·400/300 ≈ 1,33·10⁵ Pa. Đáp án 4,70·10⁵ Pa là bẫy do dùng tỉ số nhiệt độ Celsius 127/27."),

dict(
q="Một khối lượng khí lí tưởng xác định biến đổi từ trạng thái (p₁; V₁; T₁ = 300 K) sang trạng thái 2 có áp suất p₂ = 2p₁ và nhiệt độ T₂ = 600 K. Thể tích V₂ của khí",
o=["bằng 2V₁.", "bằng V₁/2.", "bằng 4V₁.", "bằng V₁."],
a="D",
e="Áp dụng phương trình trạng thái p₁V₁/T₁ = p₂V₂/T₂ ⇒ V₂ = V₁·(p₁/p₂)·(T₂/T₁) = V₁·(1/2)·2 = V₁. Tác dụng làm giãn của việc tăng nhiệt độ đúng bằng tác dụng nén của việc tăng áp suất, nên thể tích không đổi (quá trình đầu – cuối là đẳng tích)."),

dict(
q="Trên hệ toạ độ (p, V), một khối lượng khí lí tưởng xác định biến đổi từ trạng thái 1 sang trạng thái 2 dọc theo một đoạn thẳng có đường kéo dài đi qua gốc toạ độ, với V₂ > V₁. Trong quá trình đó nhiệt độ của khí",
o=["không đổi.", "tăng.", "giảm.", "tăng rồi giảm."],
a="B",
e="Đường thẳng qua gốc toạ độ trong hệ (p, V) có dạng p = aV. Khi đó T = pV/(nR) = aV²/(nR), tức nhiệt độ tỉ lệ với bình phương thể tích. Vì V tăng nên T tăng. Sai lầm thường gặp là nhầm đường thẳng này với đường đẳng nhiệt (thực ra đẳng nhiệt là hypebol)."),

dict(
q="Trong hệ toạ độ (V, T) vẽ hai đường đẳng áp của cùng một khối lượng khí lí tưởng ứng với hai áp suất p₁ và p₂. Đường ứng với p₁ có độ dốc lớn hơn. Kết luận nào đúng?",
o=["p₁ > p₂.", "p₁ < p₂.", "p₁ = p₂.", "Không so sánh được nếu chưa biết nhiệt độ."],
a="B",
e="Từ pV = nRT ⇒ V = (nR/p)·T, hệ số góc của đường đẳng áp trong hệ (V, T) là nR/p, tỉ lệ nghịch với áp suất. Đường có độ dốc lớn hơn ứng với áp suất nhỏ hơn, vậy p₁ < p₂. Nhiều học sinh nhầm 'dốc hơn ⇒ áp suất lớn hơn'."),

dict(
q="Ở nhiệt độ 27 °C và áp suất 1,0·10⁵ Pa, số phân tử khí lí tưởng có trong 1 m³ xấp xỉ bằng bao nhiêu? (k = 1,38·10⁻²³ J/K)",
o=["2,4·10²⁵ phân tử.", "6,0·10²³ phân tử.", "2,4·10¹⁹ phân tử.", "4,1·10²¹ phân tử."],
a="A",
e="Từ p = (N/V)kT suy ra N/V = p/(kT) = 1,0·10⁵/(1,38·10⁻²³·300) ≈ 2,4·10²⁵ phân tử/m³. Con số này cho thấy mật độ phân tử khí ở điều kiện thường là rất lớn; giá trị 6,0·10²³ chỉ là số phân tử trong 1 mol, không phải trong 1 m³."),

dict(
q="Tính tốc độ căn quân phương của phân tử khí nitrogen (M = 28 g/mol) ở nhiệt độ 27 °C. Lấy R = 8,31 J/(mol·K).",
o=["khoảng 52 m/s.", "khoảng 170 m/s.", "khoảng 517 m/s.", "khoảng 1 630 m/s."],
a="C",
e="Từ (1/2)mv² = (3/2)kT suy ra v = √(3RT/M) = √(3·8,31·300/0,028) ≈ √(2,67·10⁵) ≈ 517 m/s. Lỗi thường gặp là quên đổi M = 28 g/mol thành 0,028 kg/mol, dẫn tới kết quả nhỏ hơn khoảng 32 lần."),

dict(
q="Đun nóng một khối khí lí tưởng đựng trong bình kín, cứng. Phát biểu nào sau đây SAI?",
o=["Áp suất của khí tăng.",
   "Khối lượng riêng của khí không đổi.",
   "Số phân tử khí trong một đơn vị thể tích tăng.",
   "Động năng tịnh tiến trung bình của các phân tử khí tăng."],
a="C",
e="Bình kín, cứng nên cả khối lượng khí lẫn thể tích đều không đổi: khối lượng riêng và mật độ phân tử N/V giữ nguyên. Khi T tăng thì động năng tịnh tiến trung bình (3/2)kT tăng và áp suất p = (N/V)kT tăng. Vậy phát biểu về mật độ phân tử tăng là sai."),

dict(
q="Hai bình kín giống hệt nhau, giữ ở cùng nhiệt độ. Bình 1 chứa 4 g khí helium (M = 4 g/mol), bình 2 chứa 4 g khí oxygen (M = 32 g/mol). So sánh áp suất khí trong hai bình, ta có",
o=["p₁ = p₂ vì khối lượng khí bằng nhau.",
   "p₁ = 8p₂.",
   "p₂ = 8p₁.",
   "p₁ = 2p₂."],
a="B",
e="Ở cùng V và T, phương trình pV = nRT cho p tỉ lệ với số mol. Số mol helium n₁ = 4/4 = 1 mol; số mol oxygen n₂ = 4/32 = 0,125 mol. Vậy p₁/p₂ = n₁/n₂ = 8. Bẫy ở đây là suy luận từ khối lượng bằng nhau ra áp suất bằng nhau — áp suất phụ thuộc số phân tử chứ không phụ thuộc khối lượng khí."),

dict(
q="Một bình kín chứa khí lí tưởng bị rò rỉ làm mất 20% số phân tử khí, trong khi nhiệt độ được giữ không đổi. Áp suất khí trong bình lúc sau bằng",
o=["20% giá trị ban đầu.", "80% giá trị ban đầu.", "giá trị ban đầu.", "125% giá trị ban đầu."],
a="B",
e="Với thể tích và nhiệt độ không đổi, p = (N/V)kT tỉ lệ thuận với số phân tử N. Mất 20% số phân tử nghĩa là N còn 80%, do đó áp suất còn 80% giá trị ban đầu. Lưu ý ở đây không dùng được định luật Boyle vì khối lượng khí đã thay đổi."),

dict(
q="Với một khối lượng khí lí tưởng xác định ở nhiệt độ không đổi, đồ thị biểu diễn áp suất p theo 1/V là",
o=["một nhánh hypebol.",
   "một đường thẳng đi qua gốc toạ độ.",
   "một đường thẳng song song với trục hoành.",
   "một đường parabol."],
a="B",
e="Định luật Boyle cho pV = C, tức p = C·(1/V). Nếu chọn biến số là 1/V thì p là hàm bậc nhất thuần nhất của 1/V, đồ thị là đường thẳng qua gốc toạ độ có hệ số góc bằng C. Đây chính là cách xử lí số liệu để kiểm chứng định luật Boyle bằng thực nghiệm."),

dict(
q="Một khối khí thực hiện một chu trình khép kín rồi trở về đúng trạng thái ban đầu. Gọi Q và A là tổng nhiệt lượng và tổng công mà khí nhận được trong cả chu trình. Kết luận nào sau đây đúng?",
o=["Q = 0 và A = 0.", "Q = A.", "Q = −A.", "Q + A > 0 vì khí luôn nhận nhiệt."],
a="C",
e="Nội năng là hàm trạng thái, nên sau một chu trình khép kín ΔU = 0. Định luật I cho 0 = A + Q ⇒ Q = −A. Điều này không đòi hỏi từng đại lượng phải bằng 0: khí có thể nhận nhiệt và thực hiện công đúng bằng nhiệt lượng nhận được — đó là nguyên tắc của động cơ nhiệt."),

dict(
q="Cung cấp nhiệt lượng Q cho một khối khí lí tưởng trong quá trình đẳng áp, khí giãn nở. Gọi ΔU là độ biến thiên nội năng của khí. Kết luận nào sau đây đúng?",
o=["ΔU = Q.", "ΔU > Q.", "ΔU < Q.", "ΔU = 0."],
a="C",
e="Trong quá trình đẳng áp, khí vừa nóng lên vừa giãn nở nên vừa tăng nội năng vừa thực hiện công lên bên ngoài (A < 0). Từ ΔU = A + Q suy ra ΔU = Q − |A| < Q: chỉ một phần nhiệt lượng nhận vào làm tăng nội năng, phần còn lại chuyển thành công. Hệ thức ΔU = Q chỉ đúng cho quá trình đẳng tích."),

dict(
q="Muốn làm cho nhiệt độ của cùng một khối lượng khí lí tưởng tăng thêm cùng một lượng ΔT thì nhiệt lượng cần cung cấp trong quá trình đẳng áp so với trong quá trình đẳng tích sẽ",
o=["lớn hơn.", "nhỏ hơn.", "bằng nhau.", "nhỏ hơn nếu áp suất đủ lớn."],
a="A",
e="Cùng ΔT nên độ tăng nội năng ΔU như nhau trong cả hai quá trình (nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ). Ở quá trình đẳng tích Q = ΔU; ở quá trình đẳng áp khí còn phải sinh công giãn nở nên Q = ΔU + |A| > ΔU. Vậy quá trình đẳng áp cần nhiều nhiệt lượng hơn."),

dict(
q="Khinh khí cầu dùng khí nóng có phần đáy để hở. Khi đốt nóng không khí bên trong khí cầu thì",
o=["khối lượng không khí trong khí cầu không đổi, còn thể tích của khí cầu tăng lên rất mạnh nên khí cầu bay lên.",
   "một phần không khí thoát ra ngoài, khối lượng riêng của khí trong khí cầu giảm nên lực đẩy Archimedes thắng trọng lượng.",
   "áp suất của khí bên trong khí cầu tăng lên nhiều so với áp suất khí quyển, đẩy khí cầu đi lên cao.",
   "khối lượng riêng của không khí bên trong khí cầu tăng lên làm lực đẩy Archimedes tăng theo."],
a="B",
e="Vì đáy hở nên áp suất khí bên trong luôn xấp xỉ áp suất khí quyển và thể tích khí cầu gần như không đổi. Khi nhiệt độ tăng, một phần không khí thoát ra ngoài làm khối lượng khí bên trong giảm, do đó khối lượng riêng của khí nóng nhỏ hơn khối lượng riêng không khí lạnh bên ngoài; lực đẩy Archimedes vượt trọng lượng tổng cộng và khí cầu bay lên."),

dict(
q="Nồi áp suất nấu chín thức ăn nhanh hơn nồi thường chủ yếu vì",
o=["áp suất hơi trong nồi cao làm nhiệt độ sôi của nước tăng lên trên 100 °C.",
   "áp suất cao làm nhiệt dung riêng của nước giảm mạnh.",
   "nồi áp suất truyền nhiệt qua thành nồi nhanh hơn nhiều lần.",
   "áp suất cao làm nước sôi ở nhiệt độ thấp hơn nên tiết kiệm nhiệt."],
a="A",
e="Nhiệt độ sôi tăng khi áp suất trên mặt thoáng tăng. Nồi áp suất kín giữ hơi lại, nâng áp suất bên trong lên cao hơn áp suất khí quyển, nhờ đó nước sôi ở khoảng 120 °C. Nhiệt độ cao hơn làm tốc độ các quá trình làm chín thức ăn tăng mạnh, chứ không phải do vật liệu nồi dẫn nhiệt tốt hơn."),

dict(
q="Trên đỉnh núi cao, nước sôi ở nhiệt độ thấp hơn 100 °C. Nguyên nhân là",
o=["nhiệt độ không khí trên núi thấp hơn.",
   "áp suất khí quyển trên núi nhỏ hơn nên nhiệt độ sôi giảm.",
   "nhiệt hoá hơi riêng của nước trên núi lớn hơn.",
   "nước trên núi tinh khiết hơn nên dễ sôi hơn."],
a="B",
e="Nhiệt độ sôi là nhiệt độ mà tại đó áp suất hơi bão hoà của chất lỏng bằng áp suất trên mặt thoáng. Càng lên cao, áp suất khí quyển càng giảm nên chất lỏng đạt điều kiện sôi ở nhiệt độ thấp hơn. Nhiệt độ không khí xung quanh chỉ ảnh hưởng đến thời gian đun chứ không quyết định nhiệt độ sôi."),

dict(
q="Khi dùng nhiệt lượng kế để xác định nhiệt dung riêng của một miếng kim loại nóng thả vào nước, nếu bỏ qua nhiệt lượng mà bình nhiệt lượng kế hấp thụ thì giá trị nhiệt dung riêng của kim loại thu được sẽ",
o=["lớn hơn giá trị thực.",
   "nhỏ hơn giá trị thực.",
   "bằng giá trị thực.",
   "sai lệch ngẫu nhiên, không xác định được chiều."],
a="B",
e="Phương trình cân bằng nhiệt đúng là Q_kim loại toả = Q_nước thu + Q_nhiệt lượng kế thu. Nếu bỏ qua số hạng cuối, ta đánh giá thiếu nhiệt lượng thu vào, tức đánh giá thiếu nhiệt lượng do kim loại toả ra, dẫn tới c tính được nhỏ hơn giá trị thực. Đây là sai số hệ thống có chiều xác định."),

dict(
q="Khảo sát quá trình đẳng tích của một khối khí, người ta vẽ đồ thị áp suất p theo nhiệt độ Celsius t và thu được một đường thẳng. Kéo dài đường thẳng này về phía nhiệt độ thấp thì nó cắt trục hoành tại giá trị xấp xỉ",
o=["0 °C.", "−100 °C.", "−273 °C.", "−373 °C."],
a="C",
e="Trong quá trình đẳng tích, p tỉ lệ thuận với nhiệt độ tuyệt đối T = t + 273. Áp suất bằng 0 khi T = 0 K, tức t ≈ −273 °C. Việc ngoại suy các đường đẳng tích của nhiều chất khí đều cắt trục nhiệt độ tại cùng một điểm chính là cơ sở thực nghiệm để xác định độ không tuyệt đối."),

dict(
q="Khi làm thí nghiệm kiểm chứng định luật Boyle bằng xilanh có pit-tông, cần thay đổi thể tích khí một cách chậm rãi. Lí do là",
o=["để pit-tông không bị kẹt do ma sát lớn với thành xilanh, gây sai số khi đọc thể tích.",
   "để khí kịp trao đổi nhiệt với môi trường, giữ nhiệt độ gần như không đổi.",
   "để áp kế có đủ thời gian chỉ đúng giá trị áp suất của khối khí.",
   "để khối lượng khí bị giam trong xilanh không bị thay đổi trong quá trình đo."],
a="B",
e="Định luật Boyle chỉ đúng cho quá trình đẳng nhiệt. Nếu nén hoặc giãn quá nhanh, khí không kịp trao đổi nhiệt với môi trường, quá trình gần đoạn nhiệt và nhiệt độ khí thay đổi, làm số liệu p·V không còn là hằng số. Nén chậm giúp nhiệt độ khí luôn cân bằng với nhiệt độ phòng."),
]
