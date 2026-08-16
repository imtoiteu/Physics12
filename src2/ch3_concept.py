# -*- coding: utf-8 -*-
"""BÀI TẬP LÍ THUYẾT – CHƯƠNG III: TỪ TRƯỜNG."""

# Mỗi câu: dict(q, o=[4 phương án], a='A'..'D', sol='lời giải')
MC3 = {

"Mức 1 – NHẬN BIẾT": [
dict(q="Từ trường tồn tại trong không gian xung quanh",
 o=["mọi vật mang khối lượng.", "nam châm hoặc dòng điện.", "mọi điện tích đứng yên.", "một vật nhiễm điện do cọ xát."],
 a="B",
 sol="Từ trường là dạng vật chất tồn tại quanh nam châm hoặc dòng điện (tổng quát hơn: quanh điện tích chuyển động). "
     "Điện tích đứng yên chỉ gây ra điện trường, không gây ra từ trường."),

dict(q="Tính chất cơ bản của từ trường là",
 o=["gây ra lực đẩy Ác-si-mét lên vật nhúng trong nó.",
    "làm nóng mọi vật đặt trong nó.",
    "gây ra lực từ tác dụng lên nam châm hoặc dòng điện đặt trong nó.",
    "làm nhiễm điện các vật đặt trong nó."],
 a="C",
 sol="Theo định nghĩa, biểu hiện cụ thể của từ trường là lực từ tác dụng lên một nam châm hay một dòng điện "
     "đặt trong nó. Đây cũng là cách duy nhất để phát hiện sự tồn tại của từ trường."),

dict(q="Phát biểu nào sau đây về đường sức từ là đúng?",
 o=["Các đường sức từ là những đường cong khép kín hoặc vô hạn ở hai đầu.",
    "Các đường sức từ xuất phát từ cực Nam và kết thúc ở cực Bắc của nam châm.",
    "Qua một điểm trong từ trường có thể vẽ được vô số đường sức từ.",
    "Các đường sức từ có thể cắt nhau tại những điểm có từ trường mạnh."],
 a="A",
 sol="Do không tồn tại “từ tích” nên đường sức từ luôn khép kín, không có điểm đầu và điểm cuối. "
     "Bên ngoài nam châm chúng đi ra từ cực Bắc và đi vào cực Nam. Qua mỗi điểm chỉ vẽ được một đường sức "
     "nên chúng không bao giờ cắt nhau."),

dict(q="Đơn vị của cảm ứng từ trong hệ SI là",
 o=["vêbe (Wb).", "vôn (V).", "henry (H).", "tesla (T)."],
 a="D",
 sol="Cảm ứng từ có đơn vị tesla, với 1 T = 1 N/(A·m). Vêbe là đơn vị của từ thông, vôn là đơn vị của "
     "suất điện động."),

dict(q="Đơn vị của từ thông trong hệ SI là",
 o=["vêbe (Wb).", "tesla (T).", "tesla trên mét vuông (T/m²).", "niutơn trên ampe (N/A)."],
 a="A",
 sol="Từ thông Φ = NBScosα có đơn vị là vêbe: 1 Wb = 1 T·m² (chứ không phải T/m²)."),

dict(q="Lực từ tác dụng lên một đoạn dây dẫn thẳng dài ℓ mang dòng điện I đặt trong từ trường đều có "
       "cảm ứng từ B, với θ là góc giữa dây dẫn và vectơ cảm ứng từ, được tính bằng công thức",
 o=["F = BIℓcosθ.", "F = BIℓtanθ.", "F = BIℓsinθ.", "F = BIℓ/sinθ."],
 a="C",
 sol="Công thức lực từ là F = BIℓsinθ. Lực đạt cực đại BIℓ khi θ = 90° và bằng không khi dây song song "
     "với đường sức từ (θ = 0° hoặc 180°)."),

dict(q="Chiều của lực từ tác dụng lên một đoạn dây dẫn mang dòng điện đặt trong từ trường được xác định bằng",
 o=["quy tắc nắm tay phải.", "quy tắc bàn tay trái.", "quy tắc bàn tay phải.", "định luật Lenz."],
 a="B",
 sol="Quy tắc bàn tay trái dùng để xác định chiều lực từ: đường sức từ hướng vào lòng bàn tay, chiều từ cổ tay "
     "đến ngón giữa là chiều dòng điện, ngón cái choãi ra chỉ chiều lực từ. Quy tắc nắm tay phải dùng để xác định "
     "chiều đường sức từ do dòng điện sinh ra."),

dict(q="Đường sức từ của dòng điện chạy trong một dây dẫn thẳng dài có dạng",
 o=["những đường thẳng song song với dây dẫn.",
    "những đường tròn đồng tâm nằm trong mặt phẳng vuông góc với dây dẫn, tâm nằm trên dây.",
    "những đường tròn nằm trong mặt phẳng chứa dây dẫn.",
    "những đường xoắn ốc quấn quanh dây dẫn."],
 a="B",
 sol="Từ trường của dòng điện thẳng dài có các đường sức là những đường tròn đồng tâm, tâm trên dây dẫn và "
     "nằm trong mặt phẳng vuông góc với dây; chiều xác định bằng quy tắc nắm tay phải."),

dict(q="Từ trường đều là từ trường mà",
 o=["cảm ứng từ tại mọi điểm đều có cùng độ lớn nhưng khác hướng.",
    "các đường sức từ là những đường tròn đồng tâm.",
    "vectơ cảm ứng từ tại mọi điểm đều bằng nhau, đường sức là các đường thẳng song song cách đều.",
    "cảm ứng từ giảm đều theo khoảng cách."],
 a="C",
 sol="Từ trường đều có vectơ cảm ứng từ như nhau tại mọi điểm (cùng phương, cùng chiều, cùng độ lớn), "
     "biểu diễn bằng các đường sức thẳng, song song và cách đều nhau."),

dict(q="Biểu thức của định luật Faraday về cảm ứng điện từ là",
 o=["e = −Φ·Δt.", "e = −ΔΦ/Δt.", "e = −Δt/ΔΦ.", "e = −Φ/S."],
 a="B",
 sol="Suất điện động cảm ứng tỉ lệ với tốc độ biến thiên của từ thông qua mạch: e = −ΔΦ/Δt. "
     "Dấu trừ biểu diễn định luật Lenz."),

dict(q="Định luật Lenz phát biểu rằng dòng điện cảm ứng có chiều sao cho từ trường do nó sinh ra",
 o=["có tác dụng chống lại sự biến thiên của từ thông qua mạch.",
    "cùng chiều với từ trường ban đầu trong mọi trường hợp.",
    "ngược chiều với từ trường ban đầu trong mọi trường hợp.",
    "vuông góc với từ trường ban đầu."],
 a="A",
 sol="Định luật Lenz: từ trường cảm ứng chống lại SỰ BIẾN THIÊN của từ thông. Vì thế nó ngược chiều từ trường "
     "ban đầu khi từ thông tăng, nhưng lại cùng chiều khi từ thông giảm — không phải luôn ngược chiều."),

dict(q="Từ thông qua một khung dây phẳng gồm N vòng, diện tích S, đặt trong từ trường đều có cảm ứng từ B "
       "được tính bằng công thức (α là góc giữa pháp tuyến của mặt phẳng khung và vectơ cảm ứng từ)",
 o=["Φ = NBS·tanα.", "Φ = NBS·sinα.", "Φ = NBS/cosα.", "Φ = NBS·cosα."],
 a="D",
 sol="Từ thông Φ = NBScosα. Lưu ý α là góc giữa PHÁP TUYẾN của mặt phẳng khung và B, không phải góc giữa "
     "mặt phẳng khung và B."),

dict(q="Điều kiện để trong một mạch kín xuất hiện dòng điện cảm ứng là",
 o=["từ thông qua mạch phải rất lớn.",
    "từ thông qua mạch phải biến thiên.",
    "mạch phải đặt trong từ trường mạnh và đứng yên.",
    "mạch phải được nối với một nguồn điện."],
 a="B",
 sol="Dòng điện cảm ứng chỉ xuất hiện khi từ thông qua mạch kín BIẾN THIÊN. Một mạch kín đứng yên trong từ trường "
     "rất mạnh nhưng không đổi thì không có dòng điện cảm ứng."),

dict(q="Cường độ dòng điện hiệu dụng I của dòng điện xoay chiều có cường độ cực đại I₀ liên hệ với nhau bởi",
 o=["I = I₀√2.", "I = I₀/2.", "I = I₀/√2.", "I = 2I₀."],
 a="C",
 sol="Giá trị hiệu dụng bằng giá trị cực đại chia cho căn bậc hai của 2: I = I₀/√2 ≈ 0,707I₀. "
     "Tương tự cho điện áp và suất điện động."),

dict(q="Với một máy biến áp lí tưởng có số vòng dây cuộn sơ cấp N₁ và cuộn thứ cấp N₂, hệ thức đúng là",
 o=["U₁/U₂ = N₂/N₁.", "U₁/U₂ = N₁/N₂.", "U₁·U₂ = N₁·N₂.", "U₁/N₂ = U₂/N₁."],
 a="B",
 sol="Với máy biến áp lí tưởng, điện áp hiệu dụng ở mỗi cuộn tỉ lệ thuận với số vòng dây của cuộn đó: "
     "U₁/U₂ = N₁/N₂."),

dict(q="Sóng điện từ là",
 o=["sóng dọc, chỉ truyền được trong môi trường vật chất.",
    "sóng ngang, truyền được cả trong chân không.",
    "sóng dọc, truyền được cả trong chân không.",
    "sóng ngang, không truyền được trong chân không."],
 a="B",
 sol="Sóng điện từ là sóng ngang vì vectơ E và vectơ B luôn vuông góc với phương truyền sóng; "
     "nó truyền được trong chân không với tốc độ c ≈ 3·10⁸ m/s."),

dict(q="Trong sóng điện từ, quan hệ giữa vectơ cường độ điện trường E, vectơ cảm ứng từ B và phương truyền sóng là",
 o=["E song song với B và cùng vuông góc với phương truyền sóng.",
    "E và B cùng phương với phương truyền sóng.",
    "E vuông góc với B, cả hai cùng vuông góc với phương truyền sóng.",
    "E vuông góc với phương truyền sóng còn B song song với phương truyền sóng."],
 a="C",
 sol="Ba vectơ E, B và vận tốc truyền sóng v tạo thành một tam diện thuận: E ⊥ B, đồng thời cả E và B đều "
     "vuông góc với phương truyền sóng. Ngoài ra E và B dao động cùng pha."),

dict(q="Dòng điện Foucault là",
 o=["dòng điện cảm ứng chạy thành vòng xoáy khép kín trong khối vật dẫn đặt trong từ trường biến thiên.",
    "dòng điện không đổi chạy trong dây dẫn thẳng.",
    "dòng điện xoay chiều trong cuộn sơ cấp của máy biến áp.",
    "dòng điện do các electron tự do chuyển động nhiệt tạo ra."],
 a="A",
 sol="Dòng Foucault (dòng điện xoáy) là dòng cảm ứng khép kín xuất hiện trong khối vật dẫn khi từ thông qua nó "
     "biến thiên. Nó gây hao phí trong lõi máy biến áp nhưng lại được ứng dụng trong bếp từ và phanh điện từ."),

dict(q="Nhận định nào sau đây về từ trường Trái Đất là đúng?",
 o=["Cực Bắc địa từ trùng với cực Bắc địa lí.",
    "Cực từ nằm gần cực Bắc địa lí thực chất là một cực từ Nam.",
    "Từ trường Trái Đất có cảm ứng từ cỡ vài tesla.",
    "Trái Đất không có từ trường, kim la bàn chỉ hướng nhờ lực hấp dẫn."],
 a="B",
 sol="Cực Bắc của kim nam châm bị hút về phía Bắc địa lí, mà hai cực khác tên mới hút nhau, nên cực từ ở gần "
     "Bắc địa lí phải là cực từ Nam. Cảm ứng từ của từ trường Trái Đất chỉ cỡ 5·10⁻⁵ T."),

dict(q="Dòng điện xoay chiều dùng trong mạng điện dân dụng ở Việt Nam có tần số",
 o=["50 Hz.", "60 Hz.", "100 Hz.", "220 Hz."],
 a="A",
 sol="Mạng điện dân dụng Việt Nam có điện áp hiệu dụng 220 V và tần số 50 Hz, tức chu kì T = 0,02 s."),
],

"Mức 2 – THÔNG HIỂU": [
dict(q="Một đoạn dây dẫn thẳng mang dòng điện được đặt SONG SONG với các đường sức của một từ trường đều. "
       "Lực từ tác dụng lên đoạn dây đó",
 o=["đạt giá trị cực đại.", "bằng không.", "có độ lớn BIℓ.", "hướng dọc theo dây dẫn."],
 a="B",
 sol="Khi dây song song với B thì θ = 0° hoặc 180°, do đó sinθ = 0 và F = BIℓsinθ = 0. "
     "Đây là trường hợp đặc biệt học sinh hay bỏ sót khi làm bài."),

dict(q="Lực từ tác dụng lên một đoạn dây dẫn mang dòng điện đặt trong từ trường có phương",
 o=["trùng với phương của dòng điện.",
    "trùng với phương của vectơ cảm ứng từ.",
    "vuông góc với dây dẫn nhưng song song với vectơ cảm ứng từ.",
    "vuông góc với mặt phẳng chứa dây dẫn và vectơ cảm ứng từ."],
 a="D",
 sol="Theo quy tắc bàn tay trái, lực từ luôn vuông góc đồng thời với cả dây dẫn và vectơ cảm ứng từ, "
     "tức vuông góc với mặt phẳng chứa hai vectơ đó. Nhầm lực từ cùng phương với B là sai lầm rất phổ biến."),

dict(q="Ở nơi các đường sức từ được vẽ dày hơn thì",
 o=["cảm ứng từ có độ lớn lớn hơn.", "cảm ứng từ có độ lớn nhỏ hơn.",
    "từ trường có chiều ngược lại.", "từ thông luôn bằng không."],
 a="A",
 sol="Quy ước vẽ đường sức từ: mật độ đường sức tỉ lệ với độ lớn cảm ứng từ, nên nơi đường sức dày hơn thì "
     "từ trường mạnh hơn."),

dict(q="Một khung dây phẳng đặt trong từ trường đều sao cho mặt phẳng khung SONG SONG với các đường sức từ. "
       "Khi đó từ thông qua khung",
 o=["đạt giá trị cực đại.", "bằng không.", "bằng một nửa giá trị cực đại.", "có giá trị âm."],
 a="B",
 sol="Mặt phẳng khung song song với B nghĩa là pháp tuyến n vuông góc với B, tức α = 90°, do đó "
     "Φ = NBScos90° = 0. Không có đường sức nào xuyên qua khung."),

dict(q="Cách nào sau đây KHÔNG làm cho từ thông qua một khung dây kín đặt trong từ trường thay đổi?",
 o=["Quay khung dây quanh một trục nằm trong mặt phẳng khung và vuông góc với đường sức từ.",
    "Tịnh tiến khung dây trong một từ trường đều theo phương bất kì.",
    "Bóp méo khung dây làm diện tích của nó giảm đi.",
    "Thay đổi cường độ dòng điện chạy trong nam châm điện đang tạo ra từ trường."],
 a="B",
 sol="Trong từ trường ĐỀU, khi tịnh tiến khung thì B, S và α đều không đổi nên từ thông không đổi, "
     "không có dòng điện cảm ứng. Ba cách còn lại lần lượt làm thay đổi α, S và B."),

dict(q="Điểm khác nhau cơ bản giữa đường sức của từ trường và đường sức của điện trường tĩnh là",
 o=["đường sức từ là đường khép kín, còn đường sức điện tĩnh là đường hở.",
    "đường sức từ có thể cắt nhau còn đường sức điện thì không.",
    "đường sức từ luôn là đường thẳng còn đường sức điện luôn cong.",
    "chỉ đường sức điện mới có chiều xác định."],
 a="A",
 sol="Đường sức điện tĩnh xuất phát từ điện tích dương và kết thúc ở điện tích âm nên là đường hở; "
     "đường sức từ luôn khép kín vì không tồn tại đơn cực từ. Cả hai loại đều không cắt nhau và đều có chiều xác định."),

dict(q="Máy biến áp lí tưởng làm thay đổi đại lượng nào sau đây của dòng điện xoay chiều?",
 o=["Tần số.", "Chu kì.", "Điện áp hiệu dụng.", "Công suất truyền đi."],
 a="C",
 sol="Máy biến áp làm thay đổi điện áp (và do đó cả cường độ dòng điện) nhưng KHÔNG làm thay đổi tần số "
     "hay chu kì. Với máy lí tưởng, công suất ở hai cuộn bằng nhau nên công suất cũng không đổi."),

dict(q="Vì sao không thể dùng máy biến áp để làm thay đổi hiệu điện thế của nguồn điện một chiều không đổi?",
 o=["Vì dòng điện một chiều làm cháy cuộn sơ cấp.",
    "Vì dòng một chiều không đổi tạo ra từ thông không đổi nên không sinh ra suất điện động cảm ứng ở cuộn thứ cấp.",
    "Vì lõi thép chỉ dẫn được từ thông biến thiên.",
    "Vì dòng một chiều không tạo ra từ trường."],
 a="B",
 sol="Máy biến áp hoạt động dựa trên cảm ứng điện từ, đòi hỏi từ thông qua cuộn thứ cấp phải biến thiên. "
     "Dòng điện không đổi tạo ra từ trường không đổi, do đó ΔΦ = 0 và không có suất điện động cảm ứng. "
     "Dòng một chiều vẫn tạo ra từ trường, chỉ là từ trường đó không biến thiên."),

dict(q="Số chỉ của một ampe kế xoay chiều mắc trong mạch điện cho biết",
 o=["giá trị cực đại của cường độ dòng điện.",
    "giá trị trung bình của cường độ dòng điện trong một chu kì.",
    "giá trị hiệu dụng của cường độ dòng điện.",
    "giá trị tức thời của cường độ dòng điện."],
 a="C",
 sol="Các dụng cụ đo điện xoay chiều thông dụng đều chỉ giá trị hiệu dụng. Giá trị trung bình của dòng xoay "
     "chiều trong một chu kì bằng không nên không dùng để đặc trưng cho dòng điện."),

dict(q="Mạng điện dân dụng có điện áp 220 V. Giá trị điện áp cực đại của mạng điện này xấp xỉ",
 o=["220 V.", "156 V.", "311 V.", "440 V."],
 a="C",
 sol="220 V là giá trị hiệu dụng, do đó U₀ = U√2 = 220√2 ≈ 311 V. Đây là lí do các thiết bị điện phải được "
     "thiết kế để chịu được điện áp đỉnh lớn hơn 220 V khá nhiều."),

dict(q="Bếp từ chỉ đun nấu được với những loại nồi có đáy làm bằng vật liệu nhiễm từ. Nguyên nhân là",
 o=["chỉ vật liệu nhiễm từ mới dẫn nhiệt tốt.",
    "chỉ trong đáy nồi bằng vật liệu nhiễm từ mới xuất hiện dòng điện Foucault đủ mạnh để làm nóng nồi.",
    "vật liệu nhiễm từ hấp thụ được sóng điện từ do bếp phát ra.",
    "vật liệu nhiễm từ có nhiệt dung riêng rất nhỏ."],
 a="B",
 sol="Bếp từ tạo từ trường biến thiên nhanh; từ trường này chỉ tập trung và biến thiên mạnh trong đáy nồi bằng "
     "vật liệu nhiễm từ, sinh dòng Foucault lớn làm nồi nóng lên. Nồi thuỷ tinh hay nhôm không nhiễm từ nên "
     "hầu như không nóng lên."),

dict(q="Lõi của máy biến áp được làm bằng nhiều lá thép mỏng ghép cách điện với nhau nhằm mục đích",
 o=["tăng cường độ từ thông qua lõi.", "làm cho máy nhẹ hơn.",
    "hạn chế dòng điện Foucault, giảm hao phí năng lượng do toả nhiệt trong lõi.",
    "tăng tần số của dòng điện ở cuộn thứ cấp."],
 a="C",
 sol="Ghép các lá thép mỏng cách điện làm tăng điện trở đối với các dòng xoáy khép kín trong lõi, nhờ đó giảm "
     "mạnh dòng Foucault và giảm hao phí toả nhiệt. Tần số thì không bao giờ bị máy biến áp thay đổi."),

dict(q="Đưa cực Bắc của một thanh nam châm lại gần một vòng dây dẫn kín. Dòng điện cảm ứng xuất hiện trong "
       "vòng dây có chiều sao cho",
 o=["mặt vòng dây đối diện nam châm trở thành cực Bắc, đẩy nam châm ra xa.",
    "mặt vòng dây đối diện nam châm trở thành cực Nam, hút nam châm lại gần.",
    "vòng dây không tác dụng lực nào lên nam châm.",
    "vòng dây bị hút hay bị đẩy tuỳ theo tốc độ đưa nam châm lại gần."],
 a="A",
 sol="Từ thông qua vòng dây đang tăng nên theo định luật Lenz, dòng cảm ứng sinh ra từ trường ngược chiều "
     "từ trường của nam châm, làm mặt đối diện thành cực Bắc và đẩy nam châm ra — chống lại nguyên nhân "
     "sinh ra nó là sự lại gần của nam châm."),

dict(q="Một khung dây quay đều trong từ trường đều quanh trục vuông góc với đường sức. Tại thời điểm từ thông "
       "qua khung đạt giá trị cực đại thì suất điện động cảm ứng trong khung",
 o=["đạt giá trị cực đại.", "bằng không.", "bằng một nửa giá trị cực đại.", "đổi dấu đột ngột."],
 a="B",
 sol="Suất điện động tỉ lệ với TỐC ĐỘ biến thiên của từ thông. Khi Φ đạt cực đại thì đồ thị Φ(t) có tiếp tuyến "
     "nằm ngang, tốc độ biến thiên bằng không, nên e = 0. Đây là hệ quả của việc e trễ pha π/2 so với Φ."),

dict(q="Điện trường xoáy xuất hiện tại nơi có",
 o=["điện tích đứng yên.", "từ trường biến thiên theo thời gian.",
    "từ trường không đổi theo thời gian.", "dòng điện không đổi."],
 a="B",
 sol="Tại nơi có từ trường biến thiên theo thời gian sẽ xuất hiện một điện trường xoáy — điện trường có các "
     "đường sức khép kín, khác với điện trường tĩnh do điện tích đứng yên gây ra (đường sức hở)."),

dict(q="Điểm khác biệt cơ bản giữa sóng điện từ và sóng cơ là",
 o=["sóng điện từ truyền được trong chân không còn sóng cơ thì không.",
    "sóng điện từ là sóng dọc còn sóng cơ là sóng ngang.",
    "sóng điện từ không mang năng lượng còn sóng cơ thì có.",
    "sóng điện từ không bị phản xạ còn sóng cơ thì bị phản xạ."],
 a="A",
 sol="Sóng cơ bắt buộc cần môi trường vật chất đàn hồi để truyền, còn sóng điện từ truyền được cả trong chân "
     "không. Cả hai đều mang năng lượng và đều tuân theo các quy luật phản xạ, khúc xạ, giao thoa."),

dict(q="Một thanh dẫn thẳng dài ℓ trượt đều với tốc độ v trên hai thanh ray nằm ngang, trong từ trường đều B "
       "vuông góc với mặt phẳng chứa hai ray. Suất điện động cảm ứng xuất hiện trên thanh có độ lớn",
 o=["e = Bℓ/v.", "e = Bℓv.", "e = B/(ℓv).", "e = Bv/ℓ."],
 a="B",
 sol="Trong thời gian Δt, thanh quét thêm diện tích ΔS = ℓvΔt nên |ΔΦ| = BℓvΔt, do đó e = |ΔΦ|/Δt = Bℓv."),

dict(q="Cho dòng điện chạy qua một ống dây. Muốn xác định cực từ của ống dây, ta dùng",
 o=["quy tắc bàn tay trái.",
    "quy tắc nắm tay phải: khum bốn ngón theo chiều dòng điện, ngón cái chỉ về phía cực Bắc.",
    "định luật Faraday.",
    "quy tắc bàn tay trái với ngón cái chỉ chiều dòng điện."],
 a="B",
 sol="Quy tắc nắm tay phải cho ống dây: khum bốn ngón tay phải theo chiều dòng điện trong các vòng dây, "
     "ngón cái choãi ra chỉ chiều đường sức từ trong lòng ống, tức chỉ về phía cực Bắc của ống dây."),

dict(q="Một điện tích đứng yên được đặt trong một từ trường đều. Lực từ tác dụng lên điện tích đó",
 o=["bằng không.", "có độ lớn tỉ lệ với độ lớn điện tích.",
    "hướng dọc theo đường sức từ.", "làm điện tích chuyển động tròn đều."],
 a="A",
 sol="Từ trường chỉ tác dụng lực lên điện tích CHUYỂN ĐỘNG. Điện tích đứng yên trong từ trường không chịu "
     "lực từ; nếu nó chịu lực thì đó là lực điện do một điện trường nào đó gây ra."),

dict(q="Từ hệ thức định nghĩa cảm ứng từ, đơn vị tesla có thể viết lại là",
 o=["N·A·m.", "N/(A·m).", "A·m/N.", "N/(A·m²)."],
 a="B",
 sol="Từ B = F/(Iℓ) suy ra đơn vị của B là N/(A·m). Vậy 1 T = 1 N/(A·m), cũng bằng 1 Wb/m²."),

dict(q="Dòng điện xoay chiều có tần số 50 Hz. Trong mỗi giây, dòng điện này đổi chiều",
 o=["25 lần.", "50 lần.", "100 lần.", "200 lần."],
 a="C",
 sol="Trong mỗi chu kì, dòng điện xoay chiều đổi chiều 2 lần (khi i đi qua giá trị 0). Với f = 50 Hz, "
     "mỗi giây có 50 chu kì nên dòng điện đổi chiều 2 × 50 = 100 lần."),

dict(q="Một dây dẫn dài 60 cm mang dòng điện, nhưng chỉ có đoạn 25 cm nằm lọt giữa hai cực của một nam châm "
       "hình chữ U. Khi tính lực từ tác dụng lên dây, đại lượng ℓ phải lấy bằng",
 o=["0,60 m.", "0,25 m.", "0,85 m.", "0,35 m."],
 a="B",
 sol="Trong công thức F = BIℓsinθ, ℓ là chiều dài phần dây dẫn NẰM TRONG từ trường. Phần dây ở ngoài vùng có "
     "từ trường không chịu lực từ, nên ℓ = 0,25 m. Đây là bẫy rất phổ biến."),

dict(q="Bẻ đôi một thanh nam châm thẳng thành hai phần. Kết quả thu được là",
 o=["một phần chỉ có cực Bắc, phần kia chỉ có cực Nam.",
    "hai nam châm mới, mỗi nam châm đều có đủ hai cực Bắc và Nam.",
    "hai thanh kim loại mất hoàn toàn từ tính.",
    "một nam châm mạnh hơn và một thanh không có từ tính."],
 a="B",
 sol="Không tồn tại đơn cực từ trong tự nhiên. Dù chia nhỏ đến đâu, mỗi mảnh vẫn là một nam châm đủ hai cực. "
     "Đây cũng chính là lí do sâu xa khiến các đường sức từ luôn khép kín."),

dict(q="Nhận định nào sau đây về từ thông là ĐÚNG?",
 o=["Từ thông luôn là một đại lượng dương.",
    "Từ thông là đại lượng đại số, có thể dương, âm hoặc bằng không tuỳ theo chiều pháp tuyến được chọn.",
    "Từ thông là đại lượng vectơ có phương trùng với vectơ cảm ứng từ.",
    "Từ thông chỉ khác không khi mạch điện kín."],
 a="B",
 sol="Φ = NBScosα là đại lượng vô hướng nhưng có dấu (đại số): dương khi α < 90°, bằng 0 khi α = 90°, "
     "âm khi α > 90°. Từ thông vẫn được định nghĩa cho một diện tích bất kì, không nhất thiết là mạch kín."),
],

"Mức 3 – VẬN DỤNG": [
dict(q="Một đoạn dây dẫn mang dòng điện đặt trong từ trường đều. Khi góc θ giữa dây dẫn và vectơ cảm ứng từ "
       "tăng từ 30° lên 60° thì lực từ tác dụng lên dây",
 o=["giảm đi.", "tăng lên √3 lần.", "tăng lên 2 lần.", "không thay đổi."],
 a="B",
 sol="F tỉ lệ với sinθ. Tỉ số F₂/F₁ = sin60°/sin30° = (√3/2)/(1/2) = √3 ≈ 1,73. Vậy lực từ tăng √3 lần. "
     "Sai lầm hay gặp là cho rằng F tỉ lệ thuận với θ nên tăng 2 lần."),

dict(q="Từ thông qua một vòng dây dẫn kín biến thiên theo thời gian như đồ thị Hình 1. Trong giai đoạn nào "
       "độ lớn suất điện động cảm ứng trong vòng dây là lớn nhất?",
 fig="f15_phi_gap_khuc",
 o=["Giai đoạn (1), từ 0 đến 2 s.", "Giai đoạn (2), từ 2 s đến 4 s.",
    "Giai đoạn (3), từ 4 s đến 5 s.", "Giai đoạn (4), từ 5 s đến 8 s."],
 a="C",
 sol="Độ lớn suất điện động bằng độ lớn hệ số góc của đồ thị Φ(t). Giai đoạn (1): |ΔΦ/Δt| = 0,8/2 = 0,4 V; "
     "giai đoạn (2) và (4): Φ không đổi nên e = 0; giai đoạn (3): |ΔΦ/Δt| = 0,6/1 = 0,6 V. "
     "Vậy giai đoạn (3) có suất điện động lớn nhất, dù ở đó từ thông đang GIẢM và có giá trị nhỏ."),

dict(q="Một vòng dây kín có điện trở R đặt trong từ trường biến thiên. Điện lượng chuyển qua tiết diện dây "
       "trong thời gian từ thông biến thiên một lượng ΔΦ là q = |ΔΦ|/R. Từ hệ thức này suy ra rằng điện lượng q",
 o=["càng lớn nếu từ thông biến thiên càng nhanh.",
    "không phụ thuộc vào việc từ thông biến thiên nhanh hay chậm.",
    "tỉ lệ thuận với thời gian biến thiên.",
    "bằng không nếu từ thông biến thiên chậm."],
 a="B",
 sol="Biểu thức q = |ΔΦ|/R chỉ chứa độ biến thiên từ thông và điện trở, không chứa thời gian. "
     "Biến thiên nhanh thì cường độ dòng điện lớn nhưng thời gian ngắn, biến thiên chậm thì dòng nhỏ nhưng "
     "kéo dài — tích của chúng không đổi. Đây là kết quả nâng cao thường bị hiểu sai."),

dict(q="Trong thí nghiệm đo cảm ứng từ bằng cân dòng điện, người ta đo số chỉ tăng thêm Δm của cân ứng với "
       "các giá trị cường độ dòng điện I khác nhau rồi vẽ đồ thị lực từ F theo I. Đồ thị thu được là",
 o=["một đường thẳng đi qua gốc toạ độ, hệ số góc bằng Bℓ.",
    "một đường thẳng không đi qua gốc toạ độ.",
    "một nhánh parabol.", "một nhánh hypebol."],
 a="A",
 sol="Vì F = BIℓ với B và ℓ không đổi, F là hàm bậc nhất thuần nhất của I, đồ thị là đường thẳng qua gốc toạ độ "
     "có hệ số góc bằng Bℓ. Từ hệ số góc chia cho ℓ ta được B — cách xử lí này dùng được nhiều điểm số liệu "
     "nên chính xác hơn việc chỉ đo một lần."),

dict(q="Trong thí nghiệm cân dòng điện, nếu đoạn dây dẫn không được đặt thật vuông góc với vectơ cảm ứng từ mà "
       "hợp với nó một góc nhỏ hơn 90°, nhưng người làm thí nghiệm vẫn tính theo công thức B = Δm·g/(I·ℓ) thì "
       "giá trị cảm ứng từ thu được sẽ",
 o=["lớn hơn giá trị thực.", "nhỏ hơn giá trị thực.",
    "bằng giá trị thực.", "sai lệch ngẫu nhiên, không xác định được chiều."],
 a="B",
 sol="Lực từ thực tế là F = BIℓsinθ với sinθ < 1, nên F nhỏ hơn BIℓ và Δm đo được nhỏ hơn giá trị lẽ ra phải có. "
     "Khi vẫn chia cho Iℓ (tức ngầm coi sinθ = 1), giá trị B tính được nhỏ hơn giá trị thực. "
     "Đây là sai số hệ thống có chiều xác định."),

dict(q="Thả một thanh nam châm rơi thẳng đứng qua lòng một ống dây bằng đồng có mạch kín. So với khi rơi tự do "
       "cùng độ cao trong không khí, thời gian rơi của nam châm qua ống dây sẽ",
 o=["ngắn hơn.", "dài hơn.", "bằng nhau.", "dài hơn hoặc ngắn hơn tuỳ cực nam châm hướng xuống."],
 a="B",
 sol="Khi nam châm rơi qua ống, từ thông qua ống biến thiên nên xuất hiện dòng cảm ứng. Theo định luật Lenz, "
     "dòng này sinh lực từ chống lại chuyển động của nam châm, tức lực cản hướng lên. Gia tốc rơi nhỏ hơn g "
     "nên thời gian rơi dài hơn. Kết quả này không phụ thuộc cực nào hướng xuống, vì lực luôn cản trở chuyển động."),

dict(q="Đưa một nam châm lại gần hai vòng nhôm giống hệt nhau, một vòng KÍN và một vòng bị CẮT hở một đoạn nhỏ. "
       "Hiện tượng quan sát được là",
 o=["cả hai vòng đều bị đẩy ra như nhau.",
    "chỉ vòng kín bị đẩy ra, vòng hở gần như đứng yên.",
    "chỉ vòng hở bị đẩy ra.",
    "cả hai vòng đều bị hút lại gần nam châm."],
 a="B",
 sol="Suất điện động cảm ứng xuất hiện ở cả hai vòng, nhưng chỉ vòng KÍN mới có dòng điện cảm ứng chạy qua "
     "(vòng hở bị hở mạch nên i = 0). Không có dòng thì không có lực từ, nên vòng hở gần như không bị đẩy. "
     "Thí nghiệm này phân biệt rõ “có suất điện động cảm ứng” và “có dòng điện cảm ứng”."),

dict(q="Khi truyền tải một công suất điện xác định đi xa, nếu tăng điện áp ở nơi truyền đi lên 2 lần "
       "(hệ số công suất không đổi) thì công suất hao phí trên đường dây",
 o=["giảm 2 lần.", "giảm 4 lần.", "tăng 4 lần.", "không đổi."],
 a="B",
 sol="Công suất hao phí ΔP = RP²/(U²cos²φ) tỉ lệ nghịch với bình phương điện áp truyền đi. Tăng U lên 2 lần "
     "thì ΔP giảm 2² = 4 lần. Đây chính là lí do phải dùng máy tăng áp trước khi truyền tải điện đi xa."),

dict(q="Với một máy biến áp lí tưởng đang hoạt động ổn định, nếu giữ nguyên cuộn sơ cấp và tăng số vòng dây "
       "cuộn thứ cấp thì",
 o=["điện áp thứ cấp tăng và cường độ dòng điện thứ cấp giảm.",
    "cả điện áp và cường độ dòng điện thứ cấp đều tăng.",
    "điện áp thứ cấp giảm và cường độ dòng điện thứ cấp tăng.",
    "tần số của dòng điện thứ cấp tăng."],
 a="A",
 sol="Từ U₁/U₂ = N₁/N₂, tăng N₂ làm U₂ tăng. Với máy lí tưởng, công suất bảo toàn: U₁I₁ = U₂I₂, nên khi U₂ tăng "
     "thì I₂ giảm tương ứng. Tần số luôn giữ nguyên."),

dict(q="Một khung dây dẫn kín mềm đặt trong từ trường đều, mặt phẳng khung vuông góc với đường sức từ. "
       "Dùng tay bóp cho khung biến dạng làm diện tích khung giảm dần. Trong khung",
 o=["không có dòng điện cảm ứng vì từ trường không đổi.",
    "có dòng điện cảm ứng vì từ thông qua khung giảm.",
    "có dòng điện cảm ứng nhưng chỉ ở thời điểm bắt đầu bóp.",
    "chỉ có suất điện động cảm ứng mà không có dòng điện."],
 a="B",
 sol="Từ thông Φ = BScosα biến thiên khi S thay đổi, dù B hoàn toàn không đổi. Trong suốt thời gian diện tích "
     "còn đang thay đổi, khung kín có dòng điện cảm ứng. Đây là ví dụ cho thấy “từ trường không đổi” không đồng "
     "nghĩa với “từ thông không đổi”."),

dict(q="Một máy phát điện xoay chiều có khung dây quay đều trong từ trường. Nếu tăng tốc độ quay của khung lên "
       "gấp đôi thì suất điện động cực đại và tần số của suất điện động lần lượt",
 o=["tăng 2 lần và không đổi.", "không đổi và tăng 2 lần.",
    "cùng tăng 2 lần.", "cùng tăng 4 lần."],
 a="C",
 sol="E₀ = NBSω tỉ lệ thuận với ω, còn tần số f = ω/(2π) cũng tỉ lệ thuận với ω. Vậy khi tốc độ quay tăng gấp đôi, "
     "cả suất điện động cực đại lẫn tần số đều tăng gấp đôi."),

dict(q="Hai vòng dây dẫn kín đặt đồng trục cạnh nhau. Vòng thứ nhất được nối với nguồn điện qua một khoá K. "
       "Tại thời điểm NGẮT khoá K, trong vòng thứ hai",
 o=["không có dòng điện vì vòng thứ hai không nối với nguồn.",
    "xuất hiện dòng điện cảm ứng cùng chiều với dòng điện đang tắt ở vòng thứ nhất.",
    "xuất hiện dòng điện cảm ứng ngược chiều với dòng điện đang tắt ở vòng thứ nhất.",
    "xuất hiện dòng điện không đổi và tồn tại mãi."],
 a="B",
 sol="Khi ngắt K, dòng ở vòng 1 giảm nhanh về 0, từ thông qua vòng 2 GIẢM. Theo định luật Lenz, dòng cảm ứng ở "
     "vòng 2 phải sinh từ trường CÙNG chiều từ trường ban đầu để chống lại sự giảm đó, nghĩa là dòng cảm ứng "
     "cùng chiều với dòng đang tắt. Nó chỉ tồn tại trong thời gian ngắn khi dòng ở vòng 1 còn đang biến thiên."),

dict(q="Một sóng điện từ có tần số 100 MHz truyền trong chân không. Bước sóng của nó bằng",
 o=["3 m.", "0,3 m.", "30 m.", "300 m."],
 a="A",
 sol="λ = c/f = 3·10⁸/(100·10⁶) = 3 m. Chú ý đổi 100 MHz = 10⁸ Hz."),

dict(q="Một thanh dẫn trượt đều trên hai ray trong từ trường đều, mạch kín có điện trở R. Để thanh chuyển động "
       "ĐỀU thì ngoại lực tác dụng lên thanh phải",
 o=["bằng không vì thanh chuyển động đều.",
    "có độ lớn bằng B²ℓ²v/R và cùng chiều chuyển động.",
    "có độ lớn bằng Bℓv và ngược chiều chuyển động.",
    "tăng dần theo thời gian."],
 a="B",
 sol="Dòng cảm ứng i = Bℓv/R làm xuất hiện lực từ F = Biℓ = B²ℓ²v/R cản trở chuyển động. Muốn thanh chuyển động "
     "đều (hợp lực bằng không), ngoại lực phải cân bằng lực cản này, tức cùng độ lớn nhưng cùng chiều chuyển động. "
     "Công của ngoại lực chính là nguồn gốc của điện năng sinh ra trong mạch."),

dict(q="Ở phanh điện từ của tàu hoả, khi tốc độ tàu giảm dần thì lực hãm điện từ",
 o=["giữ nguyên độ lớn.", "giảm dần vì lực hãm tỉ lệ với tốc độ.",
    "tăng dần vì thời gian hãm kéo dài.", "đổi chiều khi tàu chậm lại."],
 a="B",
 sol="Suất điện động cảm ứng, do đó dòng Foucault và lực hãm, đều tỉ lệ với tốc độ chuyển động. Khi tàu chậm lại, "
     "lực hãm giảm theo. Vì thế phanh điện từ hãm rất hiệu quả ở tốc độ cao nhưng không thể giữ tàu đứng yên "
     "hoàn toàn, nên vẫn phải kết hợp với phanh cơ khí."),

dict(q="Một khung dây phẳng diện tích S đặt trong từ trường đều B, pháp tuyến của khung hợp với B một góc 60°. "
       "So với trường hợp pháp tuyến song song với B, từ thông qua khung lúc này",
 o=["bằng một nửa.", "bằng √3/2 lần.", "không đổi.", "bằng 0."],
 a="A",
 sol="Φ = BScosα. Với α = 60°, cosα = 0,5 nên Φ = 0,5·BS, tức bằng một nửa giá trị cực đại BS ứng với α = 0. "
     "Phương án √3/2 là bẫy do dùng nhầm sin60°."),

dict(q="Trong một máy phát điện xoay chiều, để tăng suất điện động cực đại mà KHÔNG làm thay đổi tần số của "
       "dòng điện phát ra, ta có thể",
 o=["tăng tốc độ quay của rôto.", "tăng số vòng dây của phần ứng.",
    "giảm diện tích khung dây.", "giảm cảm ứng từ của phần cảm."],
 a="B",
 sol="E₀ = NBSω. Tần số chỉ phụ thuộc ω, nên muốn giữ nguyên tần số thì không được đổi ω. Tăng N (hoặc B, hoặc S) "
     "đều làm E₀ tăng mà không ảnh hưởng tần số. Giảm S hay giảm B thì E₀ lại giảm."),

dict(q="Đặt một khung dây dẫn kín trong từ trường đều rồi cho khung quay đều quanh một trục VUÔNG GÓC với mặt "
       "phẳng khung và song song với vectơ cảm ứng từ. Trong khung",
 o=["xuất hiện suất điện động xoay chiều hình sin.",
    "không xuất hiện suất điện động cảm ứng.",
    "xuất hiện suất điện động không đổi.",
    "xuất hiện dòng điện có chiều thay đổi liên tục."],
 a="B",
 sol="Trục quay vuông góc với mặt phẳng khung nên pháp tuyến của khung trùng với trục quay, luôn song song với B; "
     "góc α không đổi (bằng 0), diện tích và cảm ứng từ cũng không đổi, nên từ thông hoàn toàn không biến thiên. "
     "Không có biến thiên từ thông thì không có suất điện động cảm ứng, dù khung vẫn đang quay."),

dict(q="Hai khung dây có hình dạng và kích thước giống hệt nhau, một làm bằng đồng và một làm bằng nhôm "
       "(nhôm có điện trở suất lớn hơn), được đặt trong cùng một từ trường biến thiên như nhau. Khi đó",
 o=["suất điện động cảm ứng ở hai khung khác nhau, dòng điện cảm ứng như nhau.",
    "suất điện động cảm ứng ở hai khung như nhau, dòng điện cảm ứng ở khung đồng lớn hơn.",
    "cả suất điện động và dòng điện cảm ứng đều như nhau.",
    "khung nhôm không có dòng điện cảm ứng."],
 a="B",
 sol="Suất điện động cảm ứng e = −ΔΦ/Δt chỉ phụ thuộc tốc độ biến thiên từ thông và hình học của khung, hoàn toàn "
     "không phụ thuộc vật liệu. Nhưng dòng cảm ứng i = e/R lại phụ thuộc điện trở: khung đồng có điện trở nhỏ hơn "
     "nên dòng lớn hơn."),

dict(q="Một khung dây dẫn kín chuyển động thẳng đều đi ra khỏi một vùng từ trường đều theo phương vuông góc với "
       "các đường sức. Dòng điện cảm ứng trong khung xuất hiện",
 o=["trong suốt quá trình khung còn nằm hoàn toàn trong vùng từ trường.",
    "chỉ trong khoảng thời gian khung đang cắt qua ranh giới của vùng từ trường.",
    "trong suốt quá trình chuyển động, kể cả khi đã ra hẳn ngoài.",
    "không xuất hiện vì khung chuyển động đều."],
 a="B",
 sol="Khi khung nằm hoàn toàn trong vùng từ trường đều, diện tích nằm trong từ trường không đổi nên Φ không đổi, "
     "không có dòng cảm ứng. Chỉ khi khung đang cắt ranh giới, phần diện tích nằm trong từ trường mới thay đổi, "
     "làm Φ biến thiên và sinh dòng cảm ứng."),
],

"Mức 4 – VẬN DỤNG CAO": [
dict(q="Một khung dây quay đều trong từ trường đều tạo ra suất điện động e = E₀sinωt trong khi từ thông qua khung "
       "là Φ = Φ₀cosωt. Tại thời điểm từ thông có độ lớn bằng một nửa giá trị cực đại thì độ lớn suất điện động bằng",
 o=["E₀/2.", "E₀/√2.", "E₀√3/2.", "E₀."],
 a="C",
 sol="Vì e và Φ vuông pha nên (Φ/Φ₀)² + (e/E₀)² = 1. Với |Φ| = Φ₀/2 ta được (e/E₀)² = 1 − 1/4 = 3/4, "
     "suy ra |e| = E₀√3/2. Bẫy ở đây là suy luận tuyến tính “Φ giảm một nửa thì e cũng bằng một nửa”, "
     "trong khi hai đại lượng vuông pha chứ không tỉ lệ."),

dict(q="Giả sử định luật Lenz có dấu ngược lại, nghĩa là dòng điện cảm ứng sinh ra từ trường ỦNG HỘ sự biến thiên "
       "của từ thông. Hệ quả nào sau đây sẽ xảy ra?",
 o=["Định luật bảo toàn điện tích bị vi phạm.",
    "Một nam châm chỉ cần được đẩy nhẹ vào ống dây sẽ tự tăng tốc mãi, tạo ra năng lượng từ hư không.",
    "Suất điện động cảm ứng sẽ luôn bằng không.",
    "Hiện tượng cảm ứng điện từ sẽ không còn xảy ra."],
 a="B",
 sol="Nếu từ trường cảm ứng hỗ trợ sự biến thiên, lực từ sẽ cùng chiều chuyển động, làm nam châm tăng tốc, "
     "từ thông biến thiên nhanh hơn, dòng cảm ứng mạnh hơn... quá trình tự khuếch đại vô hạn và sinh ra năng lượng "
     "mà không tiêu tốn gì. Điều đó vi phạm định luật bảo toàn năng lượng. Vậy định luật Lenz chính là hệ quả của "
     "bảo toàn năng lượng."),

dict(q="Một vòng dây dẫn kín đặt vuông góc với một từ trường đều có cảm ứng từ TĂNG ĐỀU theo thời gian "
       "(B = kt với k là hằng số dương). Cường độ dòng điện cảm ứng trong vòng dây",
 o=["tăng đều theo thời gian.", "giảm dần theo thời gian.",
    "không đổi theo thời gian.", "bằng không vì vòng dây đứng yên."],
 a="C",
 sol="Φ = B·S = k·S·t nên tốc độ biến thiên ΔΦ/Δt = kS là một hằng số. Do đó suất điện động e = kS không đổi và "
     "dòng điện i = kS/R cũng không đổi. Bẫy: nhiều học sinh cho rằng “B tăng đều thì i tăng đều”, quên rằng "
     "suất điện động phụ thuộc TỐC ĐỘ biến thiên chứ không phụ thuộc giá trị của B."),

dict(q="Phát biểu nào sau đây về dòng điện cảm ứng là ĐÚNG?",
 o=["Dòng điện cảm ứng luôn sinh ra từ trường ngược chiều với từ trường ban đầu.",
    "Dòng điện cảm ứng sinh ra từ trường ngược chiều từ trường ban đầu khi từ thông tăng, và cùng chiều khi từ thông giảm.",
    "Dòng điện cảm ứng luôn có chiều sao cho từ trường của nó cùng chiều từ trường ban đầu.",
    "Chiều dòng điện cảm ứng phụ thuộc vào điện trở của mạch."],
 a="B",
 sol="Định luật Lenz nói rằng dòng cảm ứng chống lại SỰ BIẾN THIÊN chứ không phải chống lại bản thân từ trường. "
     "Khi Φ tăng, từ trường cảm ứng ngược chiều để hãm sự tăng; khi Φ giảm, nó cùng chiều để duy trì từ thông. "
     "Điện trở chỉ ảnh hưởng độ lớn dòng điện, không ảnh hưởng chiều."),

dict(q="Một nam châm và một ống dây dẫn kín cùng chuyển động thẳng đều với CÙNG vận tốc theo cùng một hướng, "
       "khoảng cách giữa chúng luôn không đổi. Trong ống dây",
 o=["xuất hiện dòng điện cảm ứng vì cả hai đều đang chuyển động.",
    "không xuất hiện dòng điện cảm ứng.",
    "xuất hiện dòng điện cảm ứng có cường độ tỉ lệ với vận tốc chung.",
    "xuất hiện dòng điện cảm ứng đổi chiều liên tục."],
 a="B",
 sol="Hiện tượng cảm ứng điện từ chỉ phụ thuộc sự biến thiên của từ thông qua mạch. Khi nam châm và ống dây đứng "
     "yên TƯƠNG ĐỐI với nhau, từ thông qua ống dây hoàn toàn không đổi dù cả hệ đang chuyển động so với mặt đất. "
     "Không có biến thiên từ thông thì không có dòng cảm ứng."),

dict(q="Một dòng điện có cường độ biến thiên tuần hoàn nhưng KHÔNG theo quy luật hình sin (ví dụ dạng xung vuông). "
       "Với dòng điện này, hệ thức I = I₀/√2",
 o=["vẫn luôn đúng vì đó là định nghĩa của giá trị hiệu dụng.",
    "không còn đúng, vì hệ thức đó chỉ được thiết lập cho dòng điện biến thiên điều hoà.",
    "vẫn đúng nếu tần số đủ lớn.",
    "chỉ đúng khi điện trở của mạch đủ nhỏ."],
 a="B",
 sol="Định nghĩa giá trị hiệu dụng dựa trên tác dụng nhiệt (trung bình của i² trong một chu kì), áp dụng cho mọi "
     "dòng điện tuần hoàn. Nhưng kết quả cụ thể I = I₀/√2 chỉ suy ra được khi i biến thiên theo hàm sin (cosin). "
     "Với dạng xung vuông lí tưởng, giá trị hiệu dụng lại bằng chính I₀."),

dict(q="Với một máy biến áp lí tưởng đang được nối vào nguồn xoay chiều, nếu để HỞ mạch cuộn thứ cấp thì",
 o=["điện áp ở hai đầu cuộn thứ cấp bằng không.",
    "cường độ dòng điện qua cuộn sơ cấp coi như bằng không, còn điện áp thứ cấp vẫn khác không.",
    "cường độ dòng điện qua cuộn sơ cấp đạt giá trị lớn nhất.",
    "máy biến áp không tạo ra từ thông trong lõi."],
 a="B",
 sol="Thứ cấp hở nên I₂ = 0. Với máy lí tưởng, U₁I₁ = U₂I₂ = 0 nên I₁ cũng coi như bằng không (thực tế chỉ còn một "
     "dòng từ hoá rất nhỏ). Tuy vậy từ thông biến thiên trong lõi vẫn tồn tại, nên cuộn thứ cấp vẫn có suất điện "
     "động cảm ứng, tức vẫn đo được điện áp ở hai đầu — đó là lí do đầu ra máy biến áp không tải vẫn nguy hiểm."),

dict(q="Nhận định nào sau đây về mối quan hệ giữa từ thông và suất điện động cảm ứng là ĐÚNG?",
 o=["Từ thông qua mạch càng lớn thì suất điện động cảm ứng càng lớn.",
    "Có thể có thời điểm từ thông qua mạch bằng không nhưng suất điện động cảm ứng đạt giá trị cực đại.",
    "Khi từ thông đạt cực đại thì suất điện động cũng đạt cực đại.",
    "Suất điện động cảm ứng luôn cùng dấu với từ thông."],
 a="B",
 sol="Với khung dây quay đều, Φ = Φ₀cosωt và e = E₀sinωt là hai đại lượng vuông pha. Tại thời điểm Φ = 0 "
     "(mặt phẳng khung song song với B) thì tốc độ biến thiên của Φ lớn nhất, nên |e| cực đại. "
     "Ngược lại khi Φ cực đại thì e = 0. Suất điện động phụ thuộc tốc độ biến thiên, không phụ thuộc giá trị từ thông."),

dict(q="Trong chân không, sóng điện từ truyền với tốc độ c. Khi truyền từ chân không vào nước, tần số và tốc độ "
       "truyền của sóng điện từ lần lượt",
 o=["không đổi và giảm.", "giảm và không đổi.", "cùng giảm.", "cùng không đổi."],
 a="A",
 sol="Tần số của sóng do nguồn phát quyết định nên không đổi khi sóng truyền qua các môi trường khác nhau. "
     "Tốc độ truyền trong môi trường có chiết suất n là v = c/n < c, nên tốc độ giảm; kéo theo bước sóng "
     "λ = v/f cũng giảm."),

dict(q="Một vòng dây kín được đặt trong từ trường đều sao cho mặt phẳng vòng dây song song với các đường sức từ. "
       "Người ta cho vòng dây tịnh tiến đều theo phương của các đường sức. Trong vòng dây",
 o=["có dòng điện cảm ứng vì vòng dây đang chuyển động.",
    "không có dòng điện cảm ứng vì từ thông luôn bằng không và không đổi.",
    "có dòng điện cảm ứng đổi chiều liên tục.",
    "có suất điện động cảm ứng nhưng không có dòng điện."],
 a="B",
 sol="Mặt phẳng vòng dây song song với B nên α = 90° và Φ = 0 tại mọi thời điểm. Trong từ trường đều, việc tịnh "
     "tiến không làm B, S hay α thay đổi, nên Φ luôn bằng 0 — đã không đổi thì ΔΦ = 0 và không có suất điện động. "
     "Cần phân biệt “từ thông bằng không” với “từ thông biến thiên”."),

dict(q="Trong thí nghiệm đưa nam châm vào lòng ống dây nối với điện kế, nếu đưa nam châm vào NHANH GẤP ĐÔI "
       "so với lần trước (cùng quãng đường, cùng nam châm) thì",
 o=["độ lớn suất điện động cảm ứng tăng gấp đôi, còn điện lượng chuyển qua mạch không đổi.",
    "cả suất điện động lẫn điện lượng chuyển qua mạch đều tăng gấp đôi.",
    "suất điện động không đổi còn điện lượng tăng gấp đôi.",
    "cả hai đại lượng đều không đổi."],
 a="A",
 sol="Cùng một độ biến thiên từ thông |ΔΦ| nhưng thời gian giảm một nửa nên |e| = |ΔΦ|/Δt tăng gấp đôi, kim điện kế "
     "lệch nhiều hơn. Trong khi đó điện lượng q = |ΔΦ|/R chỉ phụ thuộc |ΔΦ| và R nên không đổi. "
     "Đây là câu hỏi phân biệt hai đại lượng rất dễ bị gộp làm một."),

dict(q="Hai dây dẫn thẳng dài song song đặt gần nhau, mang hai dòng điện CÙNG CHIỀU. Lực từ mà chúng tác dụng lên "
       "nhau và giải thích tương ứng là",
 o=["đẩy nhau, vì hai dòng điện cùng chiều tạo ra từ trường cùng chiều.",
    "hút nhau, vì từ trường do dây này gây ra tại vị trí dây kia tác dụng lực hướng vào nhau lên dây đó.",
    "không tác dụng lực, vì hai dây song song.",
    "hút nhau nếu cường độ hai dòng điện bằng nhau và đẩy nhau nếu khác nhau."],
 a="B",
 sol="Hai dòng điện song song cùng chiều thì hút nhau, ngược chiều thì đẩy nhau. Cơ chế: dòng I₁ tạo từ trường tại "
     "vị trí dây 2, từ trường đó tác dụng lực từ lên dây 2 theo quy tắc bàn tay trái, kết quả là lực hướng về phía "
     "dây 1. Độ lớn dòng điện chỉ ảnh hưởng độ lớn lực, không ảnh hưởng bản chất hút hay đẩy."),

dict(q="Một đĩa kim loại đặc quay trong từ trường của một nam châm. Người ta thấy đĩa quay chậm dần rồi dừng lại. "
       "Nếu xẻ trên đĩa nhiều rãnh sâu theo phương bán kính rồi lặp lại thí nghiệm thì đĩa sẽ",
 o=["dừng lại nhanh hơn.", "quay lâu hơn trước khi dừng.",
    "quay mãi không dừng.", "không quay được nữa."],
 a="B",
 sol="Đĩa đặc cho phép dòng Foucault chạy thành các vòng xoáy lớn, sinh lực hãm mạnh và tiêu tán nhanh động năng. "
     "Các rãnh xẻ cắt đứt đường đi của các vòng xoáy đó, làm dòng Foucault giảm mạnh nên lực hãm giảm và đĩa quay "
     "lâu hơn. Đây cũng là nguyên lí của việc ghép lõi biến áp từ các lá thép mỏng."),

dict(q="Xét một đoạn dây dẫn mang dòng điện đặt trong từ trường đều. Nhận định nào sau đây là ĐÚNG?",
 o=["Nếu tăng cường độ dòng điện lên 2 lần và giảm góc θ từ 90° xuống 30° thì lực từ không đổi.",
    "Nếu tăng cường độ dòng điện lên 2 lần và giảm góc θ từ 90° xuống 30° thì lực từ giảm 2 lần.",
    "Nếu tăng cường độ dòng điện lên 2 lần và giảm góc θ từ 90° xuống 30° thì lực từ tăng 2 lần.",
    "Lực từ không phụ thuộc góc θ khi cường độ dòng điện đã thay đổi."],
 a="A",
 sol="F = BIℓsinθ. Ban đầu F₁ = BIℓ·sin90° = BIℓ. Sau đó F₂ = B(2I)ℓ·sin30° = 2BIℓ·0,5 = BIℓ. "
     "Vậy hai tác dụng bù trừ nhau đúng bằng nhau và lực từ không đổi."),

dict(q="Khi nói về sự khác nhau giữa suất điện động cảm ứng và dòng điện cảm ứng, phát biểu nào sau đây ĐÚNG?",
 o=["Ở đâu có suất điện động cảm ứng thì ở đó chắc chắn có dòng điện cảm ứng.",
    "Suất điện động cảm ứng có thể xuất hiện ngay cả khi mạch hở, còn dòng điện cảm ứng thì chỉ có khi mạch kín.",
    "Dòng điện cảm ứng có thể tồn tại ngay cả khi suất điện động cảm ứng bằng không.",
    "Cả hai đại lượng đều phụ thuộc vào điện trở của mạch."],
 a="B",
 sol="Suất điện động cảm ứng sinh ra bởi sự biến thiên từ thông, tồn tại kể cả khi mạch hở (khi đó chỉ đo được "
     "hiệu điện thế mà không có dòng). Dòng điện cảm ứng i = e/R chỉ chạy được khi mạch kín. "
     "Suất điện động không phụ thuộc điện trở, chỉ dòng điện mới phụ thuộc."),

dict(q="Một khung dây dẫn kín quay đều quanh trục vuông góc với từ trường đều. Trong MỘT chu kì quay, "
       "số lần suất điện động cảm ứng trong khung đổi chiều và số lần từ thông qua khung bằng không lần lượt là",
 o=["1 và 1.", "2 và 2.", "2 và 4.", "4 và 2."],
 a="B",
 sol="Cả Φ và e đều biến thiên điều hoà với cùng chu kì T. Trong một chu kì, một đại lượng biến thiên điều hoà "
     "đi qua giá trị 0 đúng 2 lần, và suất điện động cũng đổi chiều đúng 2 lần (mỗi lần nó qua 0). "
     "Vậy cả hai con số đều bằng 2."),
],
}

# --- Câu hỏi đúng/sai (mỗi câu 4 ý) ---
DS3 = [
dict(stem="Một học sinh làm thí nghiệm: nối hai đầu một ống dây dẫn với một điện kế nhạy, rồi đưa một thanh nam "
          "châm lại gần và ra xa ống dây theo trục của ống. Xét các nhận định sau về thí nghiệm này.",
 fig="f08_thi_nghiem_faraday",
 items=[
  ("Khi nam châm và ống dây đứng yên tương đối với nhau thì kim điện kế không lệch, dù nam châm nằm sát ống dây.",
   True, "Từ thông qua ống dây khi đó không biến thiên nên không có suất điện động cảm ứng, kim điện kế đứng yên."),
  ("Đưa nam châm lại gần càng nhanh thì kim điện kế lệch càng nhiều.", True,
   "Tốc độ biến thiên từ thông càng lớn thì suất điện động cảm ứng càng lớn, dòng điện qua điện kế càng mạnh."),
  ("Nếu giữ nam châm đứng yên và dịch chuyển ống dây lại gần nam châm thì kim điện kế không lệch.", False,
   "Hiện tượng chỉ phụ thuộc chuyển động TƯƠNG ĐỐI giữa nam châm và ống dây. Dịch chuyển ống dây cũng làm từ thông "
   "qua ống biến thiên nên vẫn có dòng cảm ứng."),
  ("Khi đưa nam châm ra xa, dòng điện cảm ứng trong ống dây có chiều ngược với khi đưa nam châm lại gần.", True,
   "Lại gần thì từ thông tăng, ra xa thì từ thông giảm; hai sự biến thiên ngược nhau nên theo định luật Lenz, "
   "dòng cảm ứng có chiều ngược nhau."),
 ]),

dict(stem="Từ thông qua một vòng dây dẫn kín (chỉ một vòng) có điện trở R = 0,2 Ω biến thiên theo thời gian như "
          "đồ thị. Xét các nhận định sau.",
 fig="f15_phi_gap_khuc",
 items=[
  ("Trong giai đoạn từ 0 đến 2 s, độ lớn suất điện động cảm ứng trong vòng dây bằng 0,4 V.", True,
   "|e| = |ΔΦ|/Δt = 0,8/2 = 0,4 V."),
  ("Trong giai đoạn từ 2 s đến 4 s, trong vòng dây không có dòng điện cảm ứng.", True,
   "Từ thông giữ nguyên giá trị 0,8 Wb nên ΔΦ = 0, do đó e = 0 và i = 0."),
  ("Trong giai đoạn từ 4 s đến 5 s, độ lớn suất điện động cảm ứng nhỏ hơn trong giai đoạn từ 0 đến 2 s.", False,
   "Giai đoạn này |e| = 0,6/1 = 0,6 V, LỚN HƠN 0,4 V của giai đoạn đầu. Từ thông tuy đang giảm và có giá trị nhỏ "
   "nhưng tốc độ biến thiên lại lớn hơn."),
  ("Cường độ dòng điện cảm ứng trong vòng dây ở giai đoạn từ 4 s đến 5 s bằng 3 A.", True,
   "i = |e|/R = 0,6/0,2 = 3 A."),
 ]),

dict(stem="Để đo cảm ứng từ trong khe của một nam châm hình chữ U, một nhóm học sinh dùng phương pháp cân dòng "
          "điện với đoạn dây dẫn nằm ngang có chiều dài phần nằm trong từ trường ℓ = 5,0 cm, đặt vuông góc với "
          "các đường sức. Lấy g = 9,8 m/s². Kết quả đo được ghi trong bảng: I = 1,0 A ứng với Δm = 2,04 g; "
          "I = 2,0 A ứng với Δm = 4,08 g; I = 3,0 A ứng với Δm = 6,12 g; I = 4,0 A ứng với Δm = 8,16 g.",
 fig="f06_can_dong_dien",
 items=[
  ("Lực từ tác dụng lên đoạn dây khi I = 2,0 A có độ lớn xấp xỉ 0,04 N.", True,
   "F = Δm·g = 4,08·10⁻³ · 9,8 ≈ 0,0400 N."),
  ("Đồ thị biểu diễn lực từ F theo cường độ dòng điện I là một đường thẳng đi qua gốc toạ độ.", True,
   "F = BIℓ với B, ℓ không đổi nên F tỉ lệ thuận với I; các số liệu cho thấy Δm tăng đúng tỉ lệ với I."),
  ("Cảm ứng từ trong khe nam châm có độ lớn xấp xỉ 0,4 T.", True,
   "B = Δm·g/(I·ℓ) = (2,04·10⁻³·9,8)/(1,0·0,05) ≈ 0,40 T; các cặp số liệu khác cho cùng kết quả."),
  ("Nếu đặt đoạn dây hợp với đường sức từ một góc 30° thay vì 90° (giữ nguyên I = 1,0 A) thì số chỉ của cân "
   "vẫn thay đổi một lượng 2,04 g.", False,
   "Khi đó F = BIℓsin30° = 0,5·BIℓ, chỉ bằng một nửa, nên Δm chỉ còn khoảng 1,02 g."),
 ]),

dict(stem="Một khung dây dẫn phẳng gồm N vòng, diện tích S, quay đều với tốc độ góc ω quanh một trục nằm trong "
          "mặt phẳng khung và vuông góc với vectơ cảm ứng từ B của một từ trường đều. Xét các nhận định sau.",
 fig="f10_may_phat",
 items=[
  ("Từ thông qua khung biến thiên điều hoà với biên độ NBS.", True,
   "Φ = NBScos(ωt + φ₀), biên độ là Φ₀ = NBS."),
  ("Suất điện động cảm ứng cực đại trong khung là E₀ = NBSω.", True,
   "Vì e = −ΔΦ/Δt nên với Φ = NBScosωt ta được e = NBSω·sinωt, biên độ E₀ = NBSω."),
  ("Suất điện động cảm ứng và từ thông đạt giá trị cực đại tại cùng một thời điểm.", False,
   "Hai đại lượng này vuông pha với nhau: khi Φ cực đại thì e = 0 và ngược lại."),
  ("Nếu tăng tốc độ quay của khung lên 3 lần thì suất điện động hiệu dụng cũng tăng 3 lần.", True,
   "E₀ = NBSω tỉ lệ thuận với ω, mà E = E₀/√2 nên suất điện động hiệu dụng cũng tỉ lệ thuận với ω."),
 ]),

dict(stem="Một máy biến áp lí tưởng có cuộn sơ cấp gồm 2000 vòng, được mắc vào mạng điện xoay chiều có điện áp "
          "hiệu dụng 220 V, tần số 50 Hz. Cuộn thứ cấp có 100 vòng và được nối với một bóng đèn hoạt động bình "
          "thường. Xét các nhận định sau.",
 fig="f13_bien_ap",
 items=[
  ("Điện áp hiệu dụng ở hai đầu cuộn thứ cấp bằng 11 V.", True,
   "U₂ = U₁·N₂/N₁ = 220·100/2000 = 11 V."),
  ("Đây là một máy hạ áp.", True, "Vì N₂ < N₁ nên U₂ < U₁, máy làm giảm điện áp."),
  ("Dòng điện chạy qua bóng đèn có tần số 2,5 Hz.", False,
   "Máy biến áp không làm thay đổi tần số; dòng điện ở cuộn thứ cấp vẫn có tần số 50 Hz."),
  ("Cường độ dòng điện hiệu dụng ở cuộn thứ cấp lớn gấp 20 lần ở cuộn sơ cấp.", True,
   "Với máy lí tưởng U₁I₁ = U₂I₂ nên I₂/I₁ = U₁/U₂ = N₁/N₂ = 20."),
 ]),

dict(stem="Một thanh kim loại MN dài ℓ = 0,4 m trượt không ma sát với tốc độ không đổi v = 5 m/s trên hai thanh "
          "ray nằm ngang, trong từ trường đều B = 0,5 T hướng vuông góc với mặt phẳng chứa hai ray. Mạch kín có "
          "điện trở tổng cộng R = 2 Ω. Xét các nhận định sau.",
 fig="f16_thanh_truot",
 items=[
  ("Suất điện động cảm ứng xuất hiện trên thanh có độ lớn 1 V.", True,
   "e = Bℓv = 0,5·0,4·5 = 1 V."),
  ("Cường độ dòng điện chạy trong mạch là 0,5 A.", True,
   "Áp dụng định luật Ohm cho toàn mạch: i = e/R = 1/2 = 0,5 A."),
  ("Lực từ tác dụng lên thanh MN cùng chiều với vận tốc của thanh.", False,
   "Theo định luật Lenz, lực từ luôn chống lại chuyển động, tức ngược chiều vận tốc. "
   "Nếu cùng chiều thì thanh sẽ tự tăng tốc mãi, vi phạm bảo toàn năng lượng."),
  ("Để thanh chuyển động đều, ngoại lực tác dụng lên thanh phải có độ lớn 0,1 N.", True,
   "Lực từ cản F = B·i·ℓ = 0,5·0,5·0,4 = 0,1 N; ngoại lực phải cân bằng lực này."),
 ]),

dict(stem="Xét các nhận định sau về điện từ trường và sóng điện từ.",
 fig="f14_song_dien_tu",
 items=[
  ("Tại nơi có từ trường biến thiên theo thời gian thì xuất hiện một điện trường xoáy.", True,
   "Đây là nội dung cơ bản của thuyết điện từ: từ trường biến thiên sinh ra điện trường có đường sức khép kín."),
  ("Trong sóng điện từ, vectơ cường độ điện trường và vectơ cảm ứng từ dao động vuông pha với nhau.", False,
   "Hai vectơ này vuông góc với nhau về PHƯƠNG nhưng dao động CÙNG PHA về thời gian."),
  ("Sóng điện từ mang năng lượng và có thể truyền được trong chân không.", True,
   "Sóng điện từ mang năng lượng và truyền trong chân không với tốc độ c ≈ 3·10⁸ m/s."),
  ("Sóng vô tuyến, ánh sáng nhìn thấy và tia X có cùng bản chất.", True,
   "Chúng đều là sóng điện từ, chỉ khác nhau về tần số (bước sóng) nên khác nhau về tính chất và tác dụng."),
 ]),

dict(stem="Xét các nhận định về ứng dụng của hiện tượng cảm ứng điện từ trong đời sống và kĩ thuật.",
 items=[
  ("Bếp từ làm nóng trực tiếp đáy nồi nhờ dòng điện Foucault xuất hiện trong đáy nồi.", True,
   "Cuộn dây dưới mặt bếp tạo từ trường biến thiên nhanh, sinh dòng Foucault ngay trong đáy nồi nhiễm từ, "
   "làm nồi nóng lên; mặt bếp không tự nóng."),
  ("Có thể dùng máy biến áp để tăng hiệu điện thế của một bộ pin một chiều.", False,
   "Máy biến áp chỉ hoạt động với dòng điện biến thiên. Dòng một chiều không đổi tạo từ thông không đổi nên "
   "không sinh suất điện động cảm ứng ở cuộn thứ cấp."),
  ("Việc tăng điện áp trước khi truyền tải điện năng đi xa nhằm giảm công suất hao phí trên đường dây.", True,
   "ΔP = RP²/(U²cos²φ) tỉ lệ nghịch với U², nên tăng điện áp truyền tải làm giảm mạnh hao phí."),
  ("Trong đàn ghi ta điện, âm thanh được tạo ra do dây đàn làm biến thiên từ thông qua cuộn dây đặt bên dưới.", True,
   "Dây thép bị từ hoá dao động làm từ thông qua cuộn dây biến thiên, sinh suất điện động cảm ứng cùng tần số "
   "với dao động của dây; tín hiệu này được khuếch đại và phát ra loa."),
 ]),
]
