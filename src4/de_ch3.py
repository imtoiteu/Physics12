# -*- coding: utf-8 -*-
"""NĂM ĐỀ KIỂM TRA CHƯƠNG III – TỪ TRƯỜNG (Vật lí 12, GDPT 2018).

Cấu trúc mỗi đề giống hệt đề thi tốt nghiệp THPT môn Vật lí (Quyết định
764/QĐ-BGDĐT): 28 câu / 40 lệnh hỏi / 50 phút
    • Phần I : 18 câu trắc nghiệm nhiều phương án lựa chọn (0,25 đ/câu → 4,5 đ)
    • Phần II:  4 câu trắc nghiệm đúng/sai, mỗi câu 4 ý (0,1–0,25–0,5–1,0 đ → 4,0 đ)
    • Phần III: 6 câu trả lời ngắn (0,25 đ/câu → 1,5 đ)

Phạm vi: Bài 14 (Từ trường) → Bài 19 (Điện từ trường) của sách Kết nối tri thức:
từ trường và đường sức từ; lực từ và cảm ứng từ; từ thông và cảm ứng điện từ;
máy phát điện xoay chiều và dòng điện xoay chiều; máy biến áp và truyền tải điện
năng; điện từ trường và sóng điện từ.

Lời giải luôn dẫn chiếu NỘI DUNG phương án, không dẫn chiếu chữ cái.
"""

HANG_SO = ("Cho biết: cảm ứng từ B đo bằng tesla (T), từ thông Φ đo bằng weber (Wb), "
           "suất điện động đo bằng vôn (V). Với dòng điện và điện áp xoay chiều, giá trị "
           "hiệu dụng liên hệ với giá trị cực đại bởi I = I₀/√2 và U = U₀/√2. Lấy "
           "π ≈ 3,14; √2 ≈ 1,414; tốc độ ánh sáng trong chân không c = 3·10⁸ m/s. Các "
           "máy biến áp trong đề đều được coi là lí tưởng.")


# ===================================================================================
#                        ĐỀ SỐ 01 – KIẾN THỨC NỀN TẢNG
# ===================================================================================

DE1_P1 = [
    dict(q="Từ trường tồn tại ở xung quanh",
         o=["nam châm và dòng điện.", "mọi vật mang khối lượng.",
            "các điện tích đứng yên.", "vật nhiễm điện đặt cố định."],
         a="A",
         sol="Từ trường là dạng vật chất tồn tại xung quanh nam châm và xung quanh dòng "
             "điện (tổng quát hơn là xung quanh điện tích chuyển động). Điện tích đứng "
             "yên chỉ tạo ra điện trường chứ không tạo ra từ trường; khối lượng thì liên "
             "quan tới trường hấp dẫn."),

    dict(q="Hình vẽ biểu diễn các đường sức từ của một nam châm thẳng. Ở phía ngoài nam "
           "châm, các đường sức từ",
         fig="t31a",
         o=["đi ra từ cực Bắc và đi vào cực Nam.",
            "đi ra từ cực Nam và đi vào cực Bắc.",
            "đều hướng từ trái sang phải song song với nhau.",
            "xuất phát từ cả hai cực và đi ra vô cùng."],
         a="A",
         sol="Quy ước: bên ngoài nam châm, đường sức từ đi ra khỏi cực Bắc (N) và đi vào "
             "cực Nam (S); bên trong nam châm chúng đi từ cực Nam sang cực Bắc, khép kín "
             "đường sức. Trên hình, các mũi tên đúng theo quy ước đó."),

    dict(q="Trong hệ SI, đơn vị của cảm ứng từ là",
         o=["tesla (T).", "weber (Wb).", "vôn (V).", "ampe (A)."],
         a="A",
         sol="Cảm ứng từ B có đơn vị tesla: từ F = BIℓ suy ra 1 T = 1 N/(A·m). Weber là "
             "đơn vị của từ thông, vôn là đơn vị của suất điện động, ampe là đơn vị của "
             "cường độ dòng điện."),

    dict(q="Lực từ tác dụng lên một đoạn dây dẫn thẳng dài ℓ mang dòng điện I đặt trong "
           "từ trường đều B có độ lớn là",
         o=["F = B·I·ℓ·sinθ.", "F = B·I·ℓ·cosθ.",
            "F = B·I·ℓ·tanθ.", "F = B·I/(ℓ·sinθ)."],
         a="A",
         sol="F = B·I·ℓ·sinθ, trong đó θ là góc hợp bởi đoạn dây và vectơ cảm ứng từ. "
             "Lực từ lớn nhất khi θ = 90° (dây vuông góc với B) và bằng 0 khi θ = 0 "
             "(dây song song với B)."),

    dict(q="Trong hệ SI, đơn vị của từ thông là",
         o=["weber (Wb).", "tesla (T).", "henry (H).", "culông (C)."],
         a="A",
         sol="Từ thông Φ có đơn vị weber: 1 Wb = 1 T·m². Tesla là đơn vị cảm ứng từ, "
             "culông là đơn vị điện tích."),

    dict(q="Từ thông qua một khung dây phẳng gồm N vòng, diện tích mỗi vòng S, đặt trong "
           "từ trường đều B, được tính bằng công thức",
         o=["Φ = N·B·S·cosα.", "Φ = N·B·S·sinα.",
            "Φ = B·S·cosα/N.", "Φ = N·B/(S·cosα)."],
         a="A",
         sol="Φ = N·B·S·cosα, với α là góc giữa vectơ pháp tuyến của mặt phẳng khung dây "
             "và vectơ cảm ứng từ. Khi α = 0 thì Φ đạt độ lớn cực đại N·B·S; khi α = 90° "
             "(mặt phẳng khung chứa các đường sức) thì Φ = 0."),

    dict(q="Dòng điện cảm ứng xuất hiện trong một mạch kín khi",
         o=["từ thông qua mạch kín đó biến thiên.",
            "từ thông qua mạch kín đó có giá trị rất lớn.",
            "mạch kín được đặt trong một từ trường mạnh.",
            "mạch kín được nối với một nguồn điện ngoài."],
         a="A",
         sol="Điều kiện xuất hiện dòng điện cảm ứng là sự BIẾN THIÊN của từ thông qua "
             "mạch kín, chứ không phải độ lớn của từ thông. Một khung dây nằm yên trong "
             "từ trường rất mạnh nhưng không đổi thì vẫn không có dòng điện cảm ứng."),

    dict(q="Theo định luật Faraday, độ lớn của suất điện động cảm ứng trong một mạch kín "
           "tỉ lệ thuận với",
         o=["tốc độ biến thiên của từ thông qua mạch.",
            "giá trị của từ thông qua mạch tại thời điểm đang xét.",
            "điện trở của mạch kín đó.",
            "diện tích của mạch kín đó."],
         a="A",
         sol="Định luật Faraday: e = −ΔΦ/Δt, nên độ lớn suất điện động cảm ứng bằng tốc "
             "độ biến thiên của từ thông. Điện trở của mạch không ảnh hưởng tới suất điện "
             "động (nó chỉ quyết định cường độ dòng điện I = e/R)."),

    dict(q="Hình vẽ mô tả một đoạn dây dẫn mang dòng điện I đặt trong từ trường đều. Nếu "
           "giữ nguyên từ trường mà đổi chiều dòng điện trong đoạn dây thì lực từ tác "
           "dụng lên đoạn dây sẽ",
         fig="t31b",
         o=["đổi chiều, hướng xuống dưới và giữ nguyên độ lớn.",
            "giữ nguyên cả phương, chiều và độ lớn như cũ.",
            "đổi chiều và đồng thời tăng gấp đôi độ lớn.",
            "trở thành bằng không vì hai chiều dòng điện triệt tiêu nhau."],
         a="A",
         sol="Theo quy tắc bàn tay trái, chiều của lực từ phụ thuộc đồng thời vào chiều "
             "của dòng điện và chiều của cảm ứng từ. Đổi chiều dòng điện mà giữ nguyên B "
             "thì lực từ đổi chiều (từ hướng lên thành hướng xuống). Độ lớn F = BIℓsinθ "
             "không đổi vì B, I, ℓ và θ đều không đổi."),

    dict(q="Đường sức từ có tính chất nào sau đây?",
         o=["Là những đường cong khép kín và không cắt nhau.",
            "Là những đường cong hở, có điểm đầu và điểm cuối.",
            "Có thể cắt nhau tại những nơi từ trường mạnh.",
            "Luôn là những đường thẳng song song với nhau."],
         a="A",
         sol="Đường sức từ luôn khép kín (đi ra từ cực Bắc, vòng qua không gian bên ngoài "
             "rồi trở về cực Nam và đi xuyên qua lòng nam châm) và không bao giờ cắt "
             "nhau, vì tại mỗi điểm vectơ cảm ứng từ chỉ có một hướng xác định. Chỉ trong "
             "từ trường đều các đường sức mới là những đường thẳng song song cách đều."),

    dict(q="Hình vẽ biểu diễn một khung dây phẳng đặt trong từ trường đều; α là góc giữa "
           "pháp tuyến của khung và vectơ cảm ứng từ. Từ thông qua khung có độ lớn lớn "
           "nhất khi",
         fig="t31c",
         o=["α = 0°.", "α = 30°.", "α = 60°.", "α = 90°."],
         a="A",
         sol="Φ = B·S·cosα có độ lớn lớn nhất khi |cosα| = 1, tức α = 0° (pháp tuyến song "
             "song với B, mặt phẳng khung vuông góc với các đường sức). Khi α = 90° thì "
             "cosα = 0 và Φ = 0."),

    dict(q="Kim của la bàn luôn định hướng gần theo phương Bắc – Nam địa lí vì",
         o=["Trái Đất có từ trường.",
            "kim la bàn được chế tạo bằng vật liệu đặc biệt.",
            "Mặt Trời hút kim la bàn về phía Bắc.",
            "không khí quanh kim la bàn bị nhiễm điện."],
         a="A",
         sol="Trái Đất giống như một nam châm khổng lồ, tạo ra từ trường bao quanh nó. "
             "Kim la bàn là một nam châm nhỏ có thể quay tự do nên định hướng dọc theo "
             "đường sức từ trường Trái Đất, tức gần theo phương Bắc – Nam địa lí."),

    dict(q="Một đoạn dây dẫn dài 20 cm mang dòng điện 4,0 A đặt vuông góc với các đường "
           "sức của một từ trường đều có B = 0,50 T. Lực từ tác dụng lên đoạn dây có độ "
           "lớn là",
         o=["0,40 N.", "0,20 N.", "4,0 N.", "0,04 N."],
         a="A",
         sol="Dây vuông góc với B nên sinθ = 1:\n"
             "F = B·I·ℓ = 0,50 × 4,0 × 0,20 = 0,40 N.\n"
             "Chú ý đổi chiều dài ra mét: 20 cm = 0,20 m."),

    dict(q="Một khung dây phẳng một vòng, diện tích 0,050 m², đặt trong từ trường đều "
           "B = 0,20 T; pháp tuyến của khung hợp với B một góc 60°. Từ thông qua khung là",
         o=["5,0·10⁻³ Wb.", "1,0·10⁻² Wb.",
            "8,7·10⁻³ Wb.", "2,5·10⁻³ Wb."],
         a="A",
         sol="Φ = B·S·cosα = 0,20 × 0,050 × cos60° = 0,20 × 0,050 × 0,50 "
             "= 5,0·10⁻³ Wb.\n"
             "Nếu dùng nhầm sin60° ≈ 0,866 sẽ ra 8,7·10⁻³ Wb — đó chính là phương án nhiễu."),

    dict(q="Từ thông qua một khung dây kín biến thiên đều 0,60 Wb trong khoảng thời gian "
           "0,20 s. Độ lớn suất điện động cảm ứng trong khung là",
         o=["3,0 V.", "0,12 V.", "0,30 V.", "12 V."],
         a="A",
         sol="Áp dụng định luật Faraday cho độ lớn suất điện động cảm ứng:\n"
             "|e| = |ΔΦ|/Δt = 0,60/0,20 = 3,0 V.\n"
             "Chú ý ở đây chỉ cần biết ĐỘ BIẾN THIÊN của từ thông và thời gian biến "
             "thiên, không cần biết giá trị từ thông tại từng thời điểm."),

    dict(q="Một cuộn dây gồm 200 vòng. Từ thông qua mỗi vòng dây biến thiên đều từ 0 đến "
           "4,0·10⁻³ Wb trong thời gian 0,10 s. Độ lớn suất điện động cảm ứng trong cuộn "
           "dây là",
         o=["8,0 V.", "0,040 V.", "0,80 V.", "80 V."],
         a="A",
         sol="|e| = N·|ΔΦ₁ vòng|/Δt = 200 × (4,0·10⁻³)/0,10 = 200 × 0,040 = 8,0 V.\n"
             "Nếu quên nhân với số vòng N sẽ chỉ ra 0,040 V."),

    dict(q="Một đoạn dây dẫn dài 50 cm mang dòng điện 5,0 A đặt trong từ trường đều "
           "B = 0,40 T; đoạn dây hợp với các đường sức từ một góc 30°. Lực từ tác dụng "
           "lên đoạn dây là",
         o=["0,50 N.", "1,0 N.", "0,87 N.", "0,25 N."],
         a="A",
         sol="F = B·I·ℓ·sinθ = 0,40 × 5,0 × 0,50 × sin30° = 0,40 × 5,0 × 0,50 × 0,50 "
             "= 0,50 N.\n"
             "Giá trị 1,0 N ứng với việc bỏ quên sin30°, còn 0,87 N ứng với việc dùng "
             "nhầm cos30°."),

    dict(q="Một đoạn dây dẫn mang dòng điện được đặt song song với các đường sức của một "
           "từ trường đều. Lực từ tác dụng lên đoạn dây khi đó",
         o=["bằng không.", "đạt giá trị lớn nhất.",
            "bằng một nửa giá trị lớn nhất.", "có phương song song với đoạn dây."],
         a="A",
         sol="Khi đoạn dây song song với B thì θ = 0, do đó sinθ = 0 và F = B·I·ℓ·sinθ "
             "= 0. Đây cũng là cách xác định phương của vectơ cảm ứng từ bằng thực "
             "nghiệm: quay đoạn dây tới vị trí lực từ triệt tiêu."),
]

DE1_P2 = [
    dict(stem="Hình vẽ biểu diễn các đường sức từ của một nam châm thẳng.",
         fig="t31a",
         items=[
             ("Ở phía ngoài nam châm, các đường sức từ đi ra từ cực Bắc và đi vào cực "
              "Nam.", True,
              "Đây là quy ước về chiều của đường sức từ. Nó phù hợp với chiều mà cực Bắc "
              "của một kim nam châm thử sẽ chỉ khi đặt tại điểm đang xét."),
             ("Các đường sức từ có thể cắt nhau tại những điểm ở gần nam châm, nơi từ "
              "trường mạnh.", False,
              "Đường sức từ không bao giờ cắt nhau, dù ở gần hay xa nam châm. Nếu hai "
              "đường sức cắt nhau thì tại giao điểm sẽ có hai hướng của vectơ cảm ứng từ, "
              "trong khi tại mỗi điểm từ trường chỉ có một hướng xác định."),
             ("Nơi các đường sức từ càng dày thì từ trường tại đó càng mạnh.", True,
              "Mật độ đường sức từ được quy ước biểu diễn độ lớn của cảm ứng từ. Trên "
              "hình, các đường sức dày nhất ở sát hai cực của nam châm — đó cũng là nơi "
              "từ trường mạnh nhất."),
             ("Đường sức từ là những đường cong hở, bắt đầu ở cực Bắc và kết thúc ở cực "
              "Nam.", False,
              "Đường sức từ luôn KHÉP KÍN: ra khỏi cực Bắc, vòng trong không gian bên "
              "ngoài về cực Nam rồi đi xuyên qua lòng nam châm từ cực Nam trở lại cực "
              "Bắc. Đây là điểm khác biệt căn bản so với đường sức điện của điện tích "
              "điểm."),
         ]),

    dict(stem="Hình vẽ mô tả một đoạn dây dẫn dài ℓ = 20 cm mang dòng điện I = 4,0 A, đặt "
              "vuông góc với các đường sức của từ trường đều có cảm ứng từ B = 0,50 T.",
         fig="t31b",
         items=[
             ("Lực từ tác dụng lên đoạn dây có độ lớn 0,40 N.", True,
              "Vì đoạn dây vuông góc với B nên sinθ = 1:\n"
              "F = B·I·ℓ = 0,50 × 4,0 × 0,20 = 0,40 N."),
             ("Nếu tăng cường độ dòng điện lên gấp đôi và đồng thời giảm chiều dài đoạn "
              "dây đi một nửa thì lực từ tăng gấp đôi.", False,
              "F tỉ lệ thuận với tích I·ℓ. Khi I tăng 2 lần còn ℓ giảm 2 lần thì tích I·ℓ "
              "KHÔNG ĐỔI, nên lực từ giữ nguyên 0,40 N chứ không tăng gấp đôi."),
             ("Nếu quay đoạn dây để nó nằm song song với các đường sức từ thì lực từ đạt "
              "giá trị cực đại.", False,
              "Ngược lại: khi dây song song với B thì θ = 0, sinθ = 0 và F = 0. Lực từ "
              "đạt cực đại khi dây VUÔNG GÓC với B, tức đúng như vị trí trên hình."),
             ("Lực từ có phương vuông góc với cả đoạn dây lẫn vectơ cảm ứng từ.", True,
              "Đó là đặc điểm cơ bản của lực từ và được thể hiện trong quy tắc bàn tay "
              "trái: lực từ vuông góc với mặt phẳng chứa đoạn dây và vectơ cảm ứng từ. "
              "Trên hình, B hướng vào trang, I hướng sang phải nên F hướng lên trên."),
         ]),

    dict(stem="Hình vẽ mô tả một khung dây phẳng một vòng, diện tích S = 0,040 m², đặt "
              "trong từ trường đều có cảm ứng từ B = 0,50 T; α là góc giữa pháp tuyến của "
              "khung và vectơ cảm ứng từ.",
         fig="t31c",
         items=[
             ("Khi α = 0° thì từ thông qua khung dây bằng 0,020 Wb.", True,
              "Φ = B·S·cosα = 0,50 × 0,040 × cos0° = 0,020 Wb. Đây cũng là giá trị lớn "
              "nhất mà từ thông qua khung có thể đạt được."),
             ("Khi α = 60° thì từ thông qua khung dây bằng 0,010 Wb.", True,
              "Φ = 0,50 × 0,040 × cos60° = 0,020 × 0,50 = 0,010 Wb, đúng một nửa giá trị "
              "cực đại."),
             ("Khi α = 90° thì từ thông qua khung dây đạt giá trị lớn nhất.", False,
              "Khi α = 90° thì cos90° = 0 nên Φ = 0, tức là giá trị NHỎ nhất về độ lớn. "
              "Lúc này mặt phẳng khung chứa các đường sức từ, không có đường sức nào "
              "xuyên qua khung."),
             ("Nếu khung dây có 50 vòng thì từ thông qua khung khi α = 0° vẫn là "
              "0,020 Wb.", False,
              "Với khung nhiều vòng, Φ = N·B·S·cosα = 50 × 0,020 = 1,0 Wb, tức lớn gấp "
              "50 lần. Số vòng dây là một thừa số không được bỏ quên."),
         ]),

    dict(stem="Xét các phát biểu về hiện tượng cảm ứng điện từ.",
         items=[
             ("Dòng điện cảm ứng chỉ xuất hiện trong mạch kín khi từ thông qua mạch biến "
              "thiên.", True,
              "Đây chính là điều kiện xuất hiện dòng điện cảm ứng. Sự biến thiên có thể "
              "do B thay đổi, do diện tích mạch thay đổi, hoặc do mạch quay làm góc α "
              "thay đổi."),
             ("Nếu từ thông qua một mạch kín có giá trị rất lớn nhưng không đổi theo thời "
              "gian thì trong mạch vẫn có dòng điện cảm ứng.", False,
              "Không có. Suất điện động cảm ứng bằng TỐC ĐỘ BIẾN THIÊN của từ thông, "
              "e = −ΔΦ/Δt. Nếu Φ không đổi thì ΔΦ = 0 nên e = 0 và không có dòng điện "
              "cảm ứng, dù Φ lớn tới đâu."),
             ("Suất điện động cảm ứng càng lớn khi từ thông qua mạch biến thiên càng "
              "nhanh.", True,
              "Từ e = −ΔΦ/Δt: với cùng một độ biến thiên ΔΦ, thời gian Δt càng ngắn thì "
              "|e| càng lớn. Đó là lí do khi đưa nam châm lại gần ống dây càng nhanh thì "
              "kim điện kế lệch càng nhiều."),
             ("Dòng điện cảm ứng có chiều sao cho từ trường do nó sinh ra luôn cùng chiều "
              "với từ trường ngoài.", False,
              "Theo định luật Lenz, dòng điện cảm ứng có chiều sao cho từ trường do nó "
              "sinh ra CHỐNG LẠI sự biến thiên của từ thông đã sinh ra nó: ngược chiều "
              "từ trường ngoài khi từ thông tăng, cùng chiều khi từ thông giảm. Nếu luôn "
              "cùng chiều thì hiện tượng sẽ tự khuếch đại vô hạn, trái với định luật bảo "
              "toàn năng lượng."),
         ]),
]

DE1_P3 = [
    dict(q="Một đoạn dây dẫn dài 25 cm mang dòng điện 6,0 A được đặt vuông góc với các "
           "đường sức của một từ trường đều có cảm ứng từ 0,40 T. Tính độ lớn lực từ tác "
           "dụng lên đoạn dây (theo N, làm tròn đến hàng phần mười).",
         ans="0,6",
         sol="Đoạn dây vuông góc với B nên sinθ = 1:\n"
             "F = B·I·ℓ = 0,40 × 6,0 × 0,25 = 0,60 N.\n"
             "Chú ý đổi 25 cm = 0,25 m trước khi thay số."),

    dict(q="Một khung dây phẳng một vòng hình vuông cạnh 20 cm được đặt trong từ trường "
           "đều có cảm ứng từ 0,25 T sao cho mặt phẳng khung vuông góc với các đường sức "
           "từ. Tính từ thông qua khung (theo 10⁻³ Wb, làm tròn đến hàng đơn vị).",
         ans="10",
         sol="Diện tích khung: S = 0,20 × 0,20 = 0,040 m².\n"
             "Mặt phẳng khung vuông góc với đường sức nghĩa là pháp tuyến song song với "
             "B, tức α = 0 và cosα = 1:\n"
             "Φ = B·S = 0,25 × 0,040 = 0,010 Wb = 10·10⁻³ Wb."),

    dict(q="Từ thông qua một khung dây kín giảm đều từ 0,80 Wb xuống còn 0,20 Wb trong "
           "0,50 s. Tính độ lớn suất điện động cảm ứng xuất hiện trong khung (theo V, làm "
           "tròn đến hàng phần mười).",
         ans="1,2",
         sol="|ΔΦ| = 0,80 − 0,20 = 0,60 Wb.\n"
             "|e| = |ΔΦ|/Δt = 0,60/0,50 = 1,2 V."),

    dict(q="Một cuộn dây gồm 500 vòng. Từ thông qua mỗi vòng dây biến thiên đều một lượng "
           "2,0·10⁻⁴ Wb trong thời gian 0,10 s. Tính độ lớn suất điện động cảm ứng trong "
           "cuộn dây (theo V, làm tròn đến hàng phần mười).",
         ans="1,0",
         sol="|e| = N·|ΔΦ₁ vòng|/Δt = 500 × (2,0·10⁻⁴)/0,10 = 500 × (2,0·10⁻³) = 1,0 V."),

    dict(q="Một đoạn dây dẫn dài 40 cm mang dòng điện 2,5 A được đặt trong từ trường đều "
           "có cảm ứng từ 0,60 T; đoạn dây hợp với các đường sức từ một góc 30°. Tính độ "
           "lớn lực từ tác dụng lên đoạn dây (theo N, làm tròn đến hàng phần trăm).",
         ans="0,30",
         sol="F = B·I·ℓ·sinθ = 0,60 × 2,5 × 0,40 × sin30°\n"
             "  = 0,60 × 2,5 × 0,40 × 0,50 = 0,30 N."),

    dict(q="Một khung dây gồm 100 vòng, diện tích mỗi vòng 50 cm², được đặt trong từ "
           "trường đều có cảm ứng từ 0,20 T sao cho pháp tuyến của khung song song với "
           "vectơ cảm ứng từ. Tính từ thông qua khung dây (theo Wb, làm tròn đến hàng "
           "phần trăm).",
         ans="0,10",
         sol="Đổi đơn vị diện tích: S = 50 cm² = 50·10⁻⁴ m² = 5,0·10⁻³ m².\n"
             "Pháp tuyến song song với B nên α = 0, cosα = 1:\n"
             "Φ = N·B·S = 100 × 0,20 × 5,0·10⁻³ = 0,10 Wb."),
]

DE1 = dict(code="C3-01", so="01", chuong=3,
           title="ĐỀ KIỂM TRA CHƯƠNG III – ĐỀ SỐ 01",
           subtitle="Chương III – Từ trường",
           p1=DE1_P1, p2=DE1_P2, p3=DE1_P3)


# ===================================================================================
#              ĐỀ SỐ 02 – CẢM ỨNG ĐIỆN TỪ VÀ ĐỊNH LUẬT LENZ
# ===================================================================================

DE2_P1 = [
    dict(q="Trong hệ SI, đơn vị của suất điện động cảm ứng là",
         o=["vôn (V).", "weber (Wb).", "tesla (T).", "oát (W)."],
         a="A",
         sol="Suất điện động cảm ứng cũng là một suất điện động nên có đơn vị vôn (V). Từ "
             "e = ΔΦ/Δt ta thấy 1 V = 1 Wb/s. Oát là đơn vị công suất."),

    dict(q="Biểu thức của định luật Faraday về cảm ứng điện từ là",
         o=["e = −ΔΦ/Δt.", "e = −Δt/ΔΦ.", "e = ΔΦ·Δt.", "e = −Φ/t."],
         a="A",
         sol="e = −ΔΦ/Δt. Dấu trừ thể hiện định luật Lenz: suất điện động cảm ứng có "
             "chiều chống lại sự biến thiên của từ thông. Khi chỉ cần độ lớn ta viết "
             "|e| = |ΔΦ|/Δt."),

    dict(q="Dòng điện Foucault (dòng điện xoáy) xuất hiện trong",
         o=["khối vật dẫn đặt trong từ trường biến thiên.",
            "khối chất cách điện đặt trong từ trường mạnh.",
            "khối vật dẫn đặt trong từ trường đều không đổi.",
            "chất khí bị đốt nóng tới nhiệt độ rất cao."],
         a="A",
         sol="Khi từ thông qua một khối vật dẫn biến thiên, trong lòng khối vật dẫn xuất "
             "hiện những dòng điện cảm ứng khép kín gọi là dòng Foucault. Chất cách điện "
             "không cho dòng điện chạy qua nên không có dòng Foucault; từ trường không "
             "đổi thì không có sự biến thiên từ thông."),

    dict(q="Nam châm điện đơn giản gồm",
         o=["một ống dây có dòng điện chạy qua, thường có lõi sắt bên trong.",
            "một thanh sắt được nung nóng rồi làm nguội nhanh.",
            "hai bản kim loại phẳng đặt song song và tích điện trái dấu.",
            "một khối nam châm vĩnh cửu được mài thành hình ống."],
         a="A",
         sol="Nam châm điện là ống dây có dòng điện chạy qua; lõi sắt non đặt bên trong "
             "làm từ trường mạnh lên rất nhiều. Ưu điểm của nam châm điện là có thể bật – "
             "tắt và điều chỉnh độ mạnh bằng cách thay đổi cường độ dòng điện."),

    dict(q="Hình vẽ mô tả thí nghiệm với một nam châm và một ống dây nối với điện kế. Khi "
           "giữ nam châm đứng yên bên trong ống dây thì",
         fig="t32a",
         o=["kim điện kế chỉ số 0 vì từ thông qua ống dây không biến thiên.",
            "kim điện kế lệch mạnh vì từ thông qua ống dây có giá trị lớn.",
            "kim điện kế lệch nhẹ và giữ nguyên vị trí đó mãi.",
            "kim điện kế dao động liên tục quanh vị trí số 0."],
         a="A",
         sol="Nam châm đứng yên nên từ thông qua ống dây tuy khác 0 nhưng KHÔNG ĐỔI theo "
             "thời gian. Do đó ΔΦ = 0, suất điện động cảm ứng bằng 0 và không có dòng "
             "điện cảm ứng: kim điện kế chỉ số 0. Đây là thí nghiệm then chốt cho thấy "
             "điều kiện là sự biến thiên chứ không phải bản thân từ thông."),

    dict(q="Vẫn với thí nghiệm ở hình vẽ trên. Nếu rút nam châm ra xa ống dây với tốc độ "
           "lớn hơn trước thì",
         fig="t32a",
         o=["kim điện kế lệch nhiều hơn vì từ thông biến thiên nhanh hơn.",
            "kim điện kế lệch ít hơn vì thời gian tác dụng ngắn hơn.",
            "kim điện kế lệch như cũ vì nam châm không thay đổi.",
            "kim điện kế không lệch vì nam châm đang đi ra xa."],
         a="A",
         sol="Rút nhanh hơn nghĩa là cùng một độ biến thiên từ thông ΔΦ nhưng thời gian "
             "Δt ngắn hơn, do đó |e| = |ΔΦ|/Δt lớn hơn và dòng điện cảm ứng mạnh hơn. Kim "
             "điện kế vì thế lệch nhiều hơn (nhưng lệch về phía ngược với khi đưa nam "
             "châm lại gần)."),

    dict(q="Hình vẽ mô tả một nam châm được đưa lại gần một vòng dây kín, cực Bắc hướng "
           "về phía vòng dây. Dòng điện cảm ứng xuất hiện trong vòng dây có chiều sao cho",
         fig="t32c",
         o=["mặt vòng dây hướng về nam châm trở thành cực Bắc.",
            "mặt vòng dây hướng về nam châm trở thành cực Nam.",
            "vòng dây bị hút mạnh về phía nam châm.",
            "từ trường do nó sinh ra cùng chiều với từ trường của nam châm."],
         a="A",
         sol="Nam châm lại gần làm từ thông qua vòng dây tăng. Theo định luật Lenz, dòng "
             "điện cảm ứng phải chống lại sự tăng đó, nghĩa là sinh ra từ trường ngược "
             "chiều với từ trường của nam châm trong lòng vòng dây. Muốn vậy, mặt vòng "
             "dây quay về phía nam châm phải trở thành cực Bắc để đẩy cực Bắc của nam "
             "châm ra xa."),

    dict(q="Khi đưa một nam châm lại gần một vòng dây kín, luôn xuất hiện lực cản trở "
           "chuyển động của nam châm. Điều này phù hợp với",
         o=["định luật Lenz và định luật bảo toàn năng lượng.",
            "định luật Ohm cho toàn mạch điện kín.",
            "quy tắc bàn tay trái xác định chiều lực từ.",
            "định luật Coulomb về tương tác giữa các điện tích."],
         a="A",
         sol="Theo định luật Lenz, dòng điện cảm ứng luôn chống lại nguyên nhân sinh ra "
             "nó, ở đây là chuyển động tương đối giữa nam châm và vòng dây. Nhờ có lực "
             "cản này, muốn duy trì chuyển động ta phải thực hiện công; chính công đó "
             "chuyển thành điện năng rồi thành nhiệt trong vòng dây — hoàn toàn phù hợp "
             "với định luật bảo toàn năng lượng."),

    dict(q="Hình vẽ là đồ thị từ thông qua một khung dây theo thời gian. Trong giai đoạn "
           "②, suất điện động cảm ứng trong khung",
         fig="t32b",
         o=["bằng 0 vì từ thông không biến thiên.",
            "đạt giá trị lớn nhất vì từ thông đang lớn nhất.",
            "có giá trị 0,80 V vì từ thông bằng 0,80 Wb.",
            "biến thiên đều theo thời gian trong suốt giai đoạn đó."],
         a="A",
         sol="Trong giai đoạn ② đồ thị nằm ngang: từ thông giữ nguyên giá trị 0,80 Wb, "
             "tức ΔΦ = 0. Do đó |e| = |ΔΦ|/Δt = 0 và trong khung không có dòng điện cảm "
             "ứng. Giá trị lớn của Φ không hề tạo ra suất điện động."),

    dict(q="Suất điện động cảm ứng trong một mạch kín",
         o=["phụ thuộc tốc độ biến thiên của từ thông, không phụ thuộc giá trị từ thông.",
            "phụ thuộc giá trị từ thông, không phụ thuộc tốc độ biến thiên của nó.",
            "tỉ lệ nghịch với tốc độ biến thiên của từ thông qua mạch.",
            "chỉ phụ thuộc điện trở của mạch kín đang xét."],
         a="A",
         sol="Từ e = −ΔΦ/Δt, đại lượng quyết định là TỐC ĐỘ biến thiên ΔΦ/Δt. Hai mạch có "
             "cùng tốc độ biến thiên từ thông sẽ có cùng suất điện động cảm ứng, dù giá "
             "trị từ thông tức thời của chúng khác nhau bao nhiêu. Điện trở chỉ quyết "
             "định cường độ dòng điện chứ không quyết định suất điện động."),

    dict(q="Vẫn với đồ thị từ thông ở hình vẽ trên, độ lớn suất điện động cảm ứng trong "
           "giai đoạn ① là",
         fig="t32b",
         o=["0,40 V.", "0,80 V.", "1,6 V.", "0,20 V."],
         a="A",
         sol="Trong giai đoạn ①, từ thông tăng đều từ 0 lên 0,80 Wb trong 2,0 s:\n"
             "|e| = |ΔΦ|/Δt = 0,80/2,0 = 0,40 V."),

    dict(q="Cũng theo đồ thị đó, độ lớn suất điện động cảm ứng trong giai đoạn ③ là",
         o=["0,30 V.", "0,60 V.", "0,10 V.", "0,40 V."],
         a="A",
         sol="Trong giai đoạn ③, từ thông giảm đều từ 0,80 Wb xuống 0,20 Wb trong khoảng "
             "thời gian từ 5,0 s đến 7,0 s, tức Δt = 2,0 s:\n"
             "|e| = |ΔΦ|/Δt = 0,60/2,0 = 0,30 V.\n"
             "Nếu lấy nhầm |ΔΦ| = 0,60 Wb chia cho 1,0 s sẽ ra 0,60 V."),

    dict(q="Một khung dây gồm 250 vòng, diện tích mỗi vòng 100 cm², đặt trong từ trường "
           "đều có phương vuông góc với mặt phẳng khung. Cảm ứng từ tăng đều từ 0 đến "
           "0,40 T trong 0,20 s. Độ lớn suất điện động cảm ứng trong khung là",
         o=["5,0 V.", "0,020 V.", "0,50 V.", "50 V."],
         a="A",
         sol="Diện tích: S = 100 cm² = 100·10⁻⁴ m² = 0,010 m².\n"
             "Độ biến thiên từ thông qua mỗi vòng: ΔΦ₁ = ΔB·S = 0,40 × 0,010 "
             "= 4,0·10⁻³ Wb.\n"
             "|e| = N·ΔΦ₁/Δt = 250 × (4,0·10⁻³)/0,20 = 250 × 0,020 = 5,0 V."),

    dict(q="Một vòng dây tròn bán kính 10 cm được đặt trong từ trường đều B = 0,30 T sao "
           "cho mặt phẳng vòng dây vuông góc với các đường sức từ. Lấy π = 3,14. Từ thông "
           "qua vòng dây xấp xỉ",
         o=["9,4·10⁻³ Wb.", "3,0·10⁻² Wb.",
            "9,4·10⁻² Wb.", "1,9·10⁻² Wb."],
         a="A",
         sol="Diện tích vòng dây: S = πr² = 3,14 × (0,10)² = 3,14·10⁻² m².\n"
             "Mặt phẳng vòng dây vuông góc với đường sức nên α = 0:\n"
             "Φ = B·S = 0,30 × 3,14·10⁻² ≈ 9,4·10⁻³ Wb."),

    dict(q="Một khung dây kín có điện trở 2,0 Ω. Từ thông qua khung giảm đều 0,40 Wb "
           "trong 0,10 s. Cường độ dòng điện cảm ứng chạy trong khung là",
         o=["2,0 A.", "0,20 A.", "8,0 A.", "0,80 A."],
         a="A",
         sol="Suất điện động cảm ứng: |e| = 0,40/0,10 = 4,0 V.\n"
             "Cường độ dòng điện cảm ứng: I = |e|/R = 4,0/2,0 = 2,0 A."),

    dict(q="Một khung dây phẳng đặt trong từ trường đều, pháp tuyến song song với vectơ "
           "cảm ứng từ. Nếu đồng thời tăng cảm ứng từ lên gấp đôi và giảm diện tích khung "
           "còn một nửa thì từ thông qua khung",
         o=["không thay đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn lần."],
         a="A",
         sol="Φ = B·S·cosα với cosα = 1. Khi B tăng 2 lần và S giảm 2 lần thì tích B·S "
             "giữ nguyên, do đó từ thông không đổi. Chú ý: từ thông không đổi nghĩa là "
             "trong quá trình biến đổi vẫn có thể xuất hiện dòng điện cảm ứng nếu hai sự "
             "thay đổi không diễn ra đồng bộ."),

    dict(q="Một vòng dây kín nhỏ chuyển động đều và đi hoàn toàn vào bên trong một vùng "
           "từ trường đều rộng. Trong khoảng thời gian vòng dây nằm trọn vẹn bên trong "
           "vùng từ trường đó,",
         o=["không có dòng điện cảm ứng vì từ thông qua vòng dây không đổi.",
            "có dòng điện cảm ứng không đổi vì vòng dây vẫn đang chuyển động.",
            "có dòng điện cảm ứng tăng dần theo quãng đường đi được.",
            "có dòng điện cảm ứng đổi chiều liên tục theo thời gian."],
         a="A",
         sol="Khi vòng dây đã nằm trọn trong vùng từ trường đều, diện tích phần vòng dây "
             "có đường sức xuyên qua không đổi, cảm ứng từ cũng không đổi, nên từ thông "
             "không biến thiên và không có dòng điện cảm ứng. Dòng điện cảm ứng chỉ xuất "
             "hiện lúc vòng dây đi VÀO và lúc đi RA khỏi vùng từ trường."),

    dict(q="Ứng dụng nào sau đây dựa trên tác dụng của dòng điện Foucault?",
         o=["Phanh điện từ trên các xe tải hạng nặng.",
            "Nam châm vĩnh cửu gắn trên cánh cửa tủ lạnh.",
            "Cầu chì bảo vệ trong mạch điện gia đình.",
            "Điện trở nhiệt dùng trong bàn là điện."],
         a="A",
         sol="Trong phanh điện từ, một đĩa kim loại gắn với trục quay được đặt trong từ "
             "trường; dòng Foucault sinh ra trong đĩa tạo lực cản (theo định luật Lenz) "
             "làm đĩa quay chậm lại mà không cần ma sát cơ học. Nam châm cửa tủ lạnh, cầu "
             "chì và điện trở nhiệt đều hoạt động theo những nguyên tắc khác."),
]

DE2_P2 = [
    dict(stem="Hình vẽ mô tả thí nghiệm của Faraday: một nam châm thẳng được dịch chuyển "
              "so với một ống dây nối với điện kế G.",
         fig="t32a",
         items=[
             ("Khi đưa nam châm lại gần ống dây, kim điện kế bị lệch khỏi số 0.", True,
              "Nam châm lại gần làm từ thông qua ống dây tăng, xuất hiện suất điện động "
              "cảm ứng và dòng điện cảm ứng chạy qua điện kế, làm kim lệch."),
             ("Khi giữ nam châm đứng yên bên trong ống dây, kim điện kế vẫn lệch vì có từ "
              "thông qua ống dây.", False,
              "Từ thông tuy khác 0 nhưng KHÔNG BIẾN THIÊN, nên ΔΦ = 0 và e = 0. Kim điện "
              "kế trở về số 0. Đây là điểm mấu chốt của hiện tượng cảm ứng điện từ: "
              "nguyên nhân là sự biến thiên chứ không phải bản thân từ thông."),
             ("Nếu đưa nam châm ra xa với tốc độ lớn hơn thì kim điện kế lệch ít hơn.",
              False,
              "Ngược lại. Tốc độ lớn hơn nghĩa là Δt nhỏ hơn với cùng ΔΦ, nên "
              "|e| = |ΔΦ|/Δt LỚN hơn và kim điện kế lệch NHIỀU hơn."),
             ("Nếu đổi đầu nam châm, đưa cực Nam vào trước, thì kim điện kế lệch về phía "
              "ngược lại.", True,
              "Đổi cực làm chiều của từ trường xuyên qua ống dây đảo ngược, do đó chiều "
              "biến thiên của từ thông cũng đảo, kéo theo chiều của dòng điện cảm ứng đảo "
              "và kim điện kế lệch về phía ngược lại."),
         ]),

    dict(stem="Hình vẽ là đồ thị từ thông qua một khung dây kín gồm một vòng, có điện trở "
              "0,50 Ω, theo thời gian.",
         fig="t32b",
         items=[
             ("Trong giai đoạn ①, độ lớn suất điện động cảm ứng là 0,40 V.", True,
              "Từ thông tăng đều từ 0 lên 0,80 Wb trong 2,0 s:\n"
              "|e| = 0,80/2,0 = 0,40 V. Trên đồ thị, độ lớn suất điện động chính là độ "
              "dốc của đoạn thẳng."),
             ("Trong giai đoạn ②, từ thông qua khung bằng 0 nên không có dòng điện cảm "
              "ứng.", False,
              "Kết luận “không có dòng điện cảm ứng” là đúng, nhưng LÍ DO nêu ra thì sai: "
              "trong giai đoạn ② từ thông giữ nguyên giá trị 0,80 Wb chứ không phải bằng "
              "0. Nguyên nhân thực sự là từ thông KHÔNG BIẾN THIÊN (đồ thị nằm ngang)."),
             ("Trong giai đoạn ③, độ lớn suất điện động cảm ứng là 0,60 V.", False,
              "Trong giai đoạn ③, từ thông giảm 0,60 Wb trong 2,0 s (từ giây thứ 5 đến "
              "giây thứ 7):\n"
              "|e| = 0,60/2,0 = 0,30 V chứ không phải 0,60 V. Con số 0,60 V là kết quả "
              "sai do quên chia cho khoảng thời gian 2,0 s."),
             ("Cường độ dòng điện cảm ứng trong giai đoạn ① là 0,80 A.", True,
              "Suất điện động cảm ứng trong giai đoạn ① là |e| = 0,80/2,0 = 0,40 V, "
              "do đó I = |e|/R = 0,40/0,50 = 0,80 A. Dòng điện này giữ nguyên độ lớn "
              "trong suốt giai đoạn ① vì đồ thị Φ là một đoạn thẳng."),
         ]),

    dict(stem="Hình vẽ mô tả một nam châm được đưa lại gần một vòng dây kim loại kín, cực "
              "Bắc hướng về phía vòng dây.",
         fig="t32c",
         items=[
             ("Từ thông qua vòng dây tăng lên trong quá trình nam châm lại gần.", True,
              "Càng lại gần nam châm, cảm ứng từ tại vị trí vòng dây càng lớn nên từ "
              "thông xuyên qua vòng dây tăng."),
             ("Trong vòng dây xuất hiện dòng điện cảm ứng và dòng này tiếp tục tồn tại "
              "mãi sau khi nam châm đã dừng lại.", False,
              "Dòng điện cảm ứng chỉ tồn tại trong thời gian từ thông biến thiên. Khi nam "
              "châm dừng lại, từ thông giữ nguyên giá trị mới, ΔΦ = 0 nên dòng điện cảm "
              "ứng tắt ngay."),
             ("Mặt vòng dây hướng về phía nam châm trở thành cực Nam nên hút nam châm lại "
              "gần hơn.", False,
              "Theo định luật Lenz, dòng điện cảm ứng phải CHỐNG LẠI sự lại gần, nên mặt "
              "vòng dây hướng về nam châm phải trở thành cực BẮC để ĐẨY cực Bắc của nam "
              "châm ra xa. Nếu nó hút nam châm thì chuyển động sẽ tự tăng tốc mãi, tạo ra "
              "năng lượng từ hư không."),
             ("Nếu giữ nam châm cố định và đưa vòng dây ra xa thì dòng điện cảm ứng có "
              "chiều ngược với trường hợp trên.", True,
              "Chỉ chuyển động TƯƠNG ĐỐI giữa nam châm và vòng dây mới quyết định hiện "
              "tượng. Đưa vòng dây ra xa làm từ thông GIẢM, ngược với trường hợp ban đầu "
              "(từ thông tăng), nên dòng điện cảm ứng có chiều ngược lại."),
         ]),

    dict(stem="Một khung dây phẳng gồm 200 vòng, diện tích mỗi vòng 80 cm², được đặt "
              "trong từ trường đều có phương vuông góc với mặt phẳng khung. Cảm ứng từ "
              "tăng đều từ 0 đến 0,50 T trong 0,20 s. Khung có điện trở tổng cộng 4,0 Ω.",
         items=[
             ("Từ thông qua toàn bộ khung dây ở cuối quá trình là 4,0·10⁻³ Wb.", False,
              "Giá trị 4,0·10⁻³ Wb là từ thông qua MỘT vòng: Φ₁ = B·S = 0,50 × 80·10⁻⁴ "
              "= 4,0·10⁻³ Wb.\n"
              "Từ thông qua toàn bộ khung phải nhân với số vòng: "
              "Φ = 200 × 4,0·10⁻³ = 0,80 Wb."),
             ("Suất điện động cảm ứng xuất hiện trong khung là 4,0 V.", True,
              "|e| = N·ΔΦ₁/Δt = 200 × (4,0·10⁻³)/0,20 = 200 × 0,020 = 4,0 V."),
             ("Cường độ dòng điện cảm ứng chạy trong khung là 0,50 A.", False,
              "Suất điện động cảm ứng đã tính được ở ý trên là 4,0 V, nên\n"
              "I = |e|/R = 4,0/4,0 = 1,0 A chứ không phải 0,50 A. Điện trở của khung "
              "chỉ ảnh hưởng tới cường độ dòng điện, không ảnh hưởng tới suất điện "
              "động."),
             ("Nếu thời gian tăng từ trường kéo dài gấp đôi thì suất điện động cảm ứng "
              "giảm đi một nửa.", True,
              "|e| = N·ΔΦ₁/Δt tỉ lệ nghịch với Δt khi ΔΦ₁ không đổi. Δt tăng 2 lần thì "
              "|e| giảm còn một nửa, tức 2,0 V."),
         ]),
]

DE2_P3 = [
    dict(q="Từ thông qua một khung dây biến thiên theo đồ thị ở Câu 9. Tính độ lớn suất "
           "điện động cảm ứng trong giai đoạn ① (theo V, làm tròn đến hàng phần mười).",
         fig="t32b",
         ans="0,4",
         sol="Trong giai đoạn ①, từ thông tăng đều từ 0 lên 0,80 Wb trong khoảng thời "
             "gian 2,0 s:\n"
             "|e| = |ΔΦ|/Δt = 0,80/2,0 = 0,40 V."),

    dict(q="Một khung dây gồm 400 vòng, diện tích mỗi vòng 25 cm², đặt trong từ trường "
           "đều vuông góc với mặt phẳng khung. Cảm ứng từ giảm đều từ 0,80 T về 0 trong "
           "0,40 s. Tính độ lớn suất điện động cảm ứng trong khung (theo V, làm tròn đến "
           "hàng phần mười).",
         ans="2,0",
         sol="Diện tích mỗi vòng: S = 25 cm² = 25·10⁻⁴ m².\n"
             "Độ biến thiên từ thông qua mỗi vòng: ΔΦ₁ = 0,80 × 25·10⁻⁴ = 2,0·10⁻³ Wb.\n"
             "|e| = N·ΔΦ₁/Δt = 400 × (2,0·10⁻³)/0,40 = 400 × 5,0·10⁻³ = 2,0 V."),

    dict(q="Một vòng dây tròn bán kính 12 cm được đặt trong từ trường đều có cảm ứng từ "
           "0,25 T sao cho mặt phẳng vòng dây vuông góc với các đường sức từ. Lấy "
           "π = 3,14. Tính từ thông qua vòng dây (theo 10⁻³ Wb, làm tròn đến hàng phần "
           "mười).",
         ans="11,3",
         sol="Diện tích vòng dây: S = πr² = 3,14 × (0,12)² = 3,14 × 0,0144 "
             "= 0,045216 m².\n"
             "Φ = B·S = 0,25 × 0,045216 ≈ 0,01130 Wb = 11,3·10⁻³ Wb."),

    dict(q="Một khung dây kín có điện trở 5,0 Ω. Từ thông qua khung biến thiên đều một "
           "lượng 1,5 Wb trong khoảng thời gian 0,30 s. Tính cường độ dòng điện cảm ứng "
           "chạy trong khung (theo A, làm tròn đến hàng phần mười).",
         ans="1,0",
         sol="Suất điện động cảm ứng: |e| = |ΔΦ|/Δt = 1,5/0,30 = 5,0 V.\n"
             "Cường độ dòng điện cảm ứng: I = |e|/R = 5,0/5,0 = 1,0 A."),

    dict(q="Một ống dây gồm 800 vòng. Từ thông qua mỗi vòng tăng đều từ 1,0·10⁻⁴ Wb lên "
           "5,0·10⁻⁴ Wb trong khoảng thời gian 0,20 s. Tính độ lớn suất điện động cảm ứng "
           "trong ống dây (theo V, làm tròn đến hàng phần mười).",
         ans="1,6",
         sol="Độ biến thiên từ thông qua mỗi vòng:\n"
             "ΔΦ₁ = 5,0·10⁻⁴ − 1,0·10⁻⁴ = 4,0·10⁻⁴ Wb.\n"
             "|e| = N·ΔΦ₁/Δt = 800 × (4,0·10⁻⁴)/0,20 = 800 × (2,0·10⁻³) = 1,6 V."),

    dict(q="Một khung dây phẳng một vòng, diện tích 200 cm², được đặt trong từ trường đều "
           "có cảm ứng từ 0,40 T; pháp tuyến của khung hợp với vectơ cảm ứng từ một góc "
           "60°. Tính từ thông qua khung (theo 10⁻³ Wb, làm tròn đến hàng phần mười).",
         ans="4,0",
         sol="Diện tích: S = 200 cm² = 200·10⁻⁴ m² = 0,020 m².\n"
             "Φ = B·S·cosα = 0,40 × 0,020 × cos60° = 0,40 × 0,020 × 0,50 = 4,0·10⁻³ Wb."),
]

DE2 = dict(code="C3-02", so="02", chuong=3,
           title="ĐỀ KIỂM TRA CHƯƠNG III – ĐỀ SỐ 02",
           subtitle="Chương III – Từ trường",
           p1=DE2_P1, p2=DE2_P2, p3=DE2_P3)


# ===================================================================================
#        ĐỀ SỐ 03 – THANH DẪN CHUYỂN ĐỘNG VÀ DÒNG ĐIỆN XOAY CHIỀU
# ===================================================================================

DE3_P1 = [
    dict(q="Một thanh dẫn dài ℓ chuyển động với tốc độ v vuông góc với chính nó và vuông "
           "góc với vectơ cảm ứng từ B của một từ trường đều. Suất điện động cảm ứng xuất "
           "hiện trên thanh có độ lớn",
         o=["e = B·ℓ·v.", "e = B·ℓ/v.", "e = B·v/ℓ.", "e = B·ℓ·v²."],
         a="A",
         sol="Khi thanh dẫn quét một diện tích ΔS = ℓ·v·Δt trong thời gian Δt, từ thông "
             "biến thiên ΔΦ = B·ℓ·v·Δt, do đó |e| = ΔΦ/Δt = B·ℓ·v. Công thức chỉ đúng khi "
             "thanh, vectơ vận tốc và vectơ cảm ứng từ đôi một vuông góc với nhau."),

    dict(q="Dòng điện xoay chiều là dòng điện có",
         o=["cường độ biến thiên điều hoà theo thời gian.",
            "cường độ luôn tăng đều theo thời gian.",
            "chiều không đổi nhưng độ lớn thay đổi.",
            "cường độ và chiều đều không đổi theo thời gian."],
         a="A",
         sol="Dòng điện xoay chiều có cường độ biến thiên theo quy luật hàm sin (hoặc "
             "cos) của thời gian: i = I₀cos(ωt + φ). Do đó cả độ lớn lẫn chiều của dòng "
             "điện đều biến đổi tuần hoàn."),

    dict(q="Giá trị hiệu dụng I của một dòng điện xoay chiều có cường độ cực đại I₀ được "
           "tính bằng",
         o=["I = I₀/√2.", "I = I₀·√2.", "I = I₀/2.", "I = 2·I₀."],
         a="A",
         sol="I = I₀/√2 ≈ 0,707·I₀. Giá trị hiệu dụng được định nghĩa sao cho dòng điện "
             "xoay chiều và một dòng điện không đổi có cùng giá trị đó sẽ toả ra cùng một "
             "nhiệt lượng trên cùng một điện trở trong cùng thời gian. Các đồng hồ đo "
             "điện thông thường đều chỉ giá trị hiệu dụng."),

    dict(q="Tần số của dòng điện xoay chiều trong mạng điện dân dụng ở Việt Nam là",
         o=["50 Hz.", "60 Hz.", "100 Hz.", "220 Hz."],
         a="A",
         sol="Mạng điện dân dụng Việt Nam có điện áp hiệu dụng 220 V và tần số 50 Hz, ứng "
             "với chu kì T = 1/50 = 0,02 s. Giá trị 60 Hz được dùng ở một số nước như Hoa "
             "Kỳ, Nhật Bản; còn 220 là giá trị của điện áp chứ không phải tần số."),

    dict(q="Hình vẽ mô tả một thanh dẫn MN trượt trên hai thanh ray song song đặt trong "
           "từ trường đều. Khi thanh MN trượt sang phải, trong mạch xuất hiện dòng điện "
           "cảm ứng vì",
         fig="t33a",
         o=["diện tích mạch kín tăng nên từ thông qua mạch tăng.",
            "cảm ứng từ của từ trường tăng dần theo thời gian.",
            "điện trở của mạch kín giảm dần khi thanh trượt.",
            "thanh MN được nối trực tiếp với một nguồn điện."],
         a="A",
         sol="Từ trường không đổi, nhưng khi thanh MN trượt sang phải thì phần diện tích "
             "giới hạn bởi mạch kín (gồm điện trở R, hai ray và thanh MN) tăng lên. Từ "
             "thông Φ = B·S vì thế tăng, làm xuất hiện suất điện động cảm ứng. Đây là "
             "trường hợp từ thông biến thiên do DIỆN TÍCH thay đổi."),

    dict(q="Hình vẽ là đồ thị cường độ dòng điện xoay chiều theo thời gian. Chu kì của "
           "dòng điện này là",
         fig="t33b",
         o=["0,020 s.", "0,010 s.", "0,040 s.", "0,050 s."],
         a="A",
         sol="Đọc trên đồ thị: dòng điện lặp lại giá trị và chiều biến thiên sau mỗi "
             "20 ms, tức T = 20 ms = 0,020 s. Có thể kiểm tra bằng khoảng cách giữa hai "
             "đỉnh liên tiếp của đồ thị (từ 0 ms đến 20 ms)."),

    dict(q="Cũng theo đồ thị đó, cường độ dòng điện cực đại là",
         o=["4,0 A.", "2,8 A.", "8,0 A.", "2,0 A."],
         a="A",
         sol="Giá trị cực đại I₀ là biên độ của đồ thị, đọc được trên trục tung là 4,0 A. "
             "Giá trị 2,8 A chính là cường độ HIỆU DỤNG I = 4,0/√2 ≈ 2,83 A, dễ bị nhầm "
             "với cường độ cực đại."),

    dict(q="Hình vẽ là sơ đồ nguyên tắc của một máy phát điện xoay chiều. Bộ phận tạo ra "
           "từ trường trong máy được gọi là",
         fig="t33c",
         o=["phần cảm.", "phần ứng.", "bộ góp điện.", "stato."],
         a="A",
         sol="Trong máy phát điện xoay chiều, bộ phận tạo ra từ trường (nam châm hoặc nam "
             "châm điện) gọi là phần cảm; bộ phận trong đó xuất hiện suất điện động cảm "
             "ứng (khung dây) gọi là phần ứng. Bộ góp điện gồm các vành khuyên và chổi "
             "quét làm nhiệm vụ đưa dòng điện ra mạch ngoài."),

    dict(q="Nguyên tắc hoạt động của máy phát điện xoay chiều dựa trên",
         o=["hiện tượng cảm ứng điện từ.",
            "tác dụng của lực từ lên dòng điện.",
            "hiện tượng nhiễm điện do cọ xát.",
            "tác dụng nhiệt của dòng điện."],
         a="A",
         sol="Khi khung dây quay đều trong từ trường, từ thông qua khung biến thiên tuần "
             "hoàn, làm xuất hiện suất điện động cảm ứng biến thiên điều hoà. Đó chính là "
             "hiện tượng cảm ứng điện từ. Tác dụng của lực từ lên dòng điện lại là nguyên "
             "tắc hoạt động của động cơ điện."),

    dict(q="Trong mỗi chu kì, dòng điện xoay chiều đổi chiều bao nhiêu lần?",
         o=["2 lần.", "1 lần.", "4 lần.", "50 lần."],
         a="A",
         sol="Trong một chu kì, cường độ dòng điện đi qua giá trị 0 hai lần và mỗi lần đi "
             "qua 0 thì dòng điện đổi chiều, nên dòng điện đổi chiều 2 lần mỗi chu kì. Với "
             "tần số 50 Hz, trong 1 giây dòng điện đổi chiều 100 lần."),

    dict(q="Vẫn với hình vẽ thanh dẫn trượt ở Câu 5. Biết ℓ = 50 cm, v = 3,0 m/s và "
           "B = 0,40 T. Suất điện động cảm ứng xuất hiện trên thanh MN là",
         fig="t33a",
         o=["0,60 V.", "6,0 V.", "0,06 V.", "1,2 V."],
         a="A",
         sol="Thanh MN, vectơ vận tốc và vectơ cảm ứng từ đôi một vuông góc nên:\n"
             "e = B·ℓ·v = 0,40 × 0,50 × 3,0 = 0,60 V."),

    dict(q="Cũng với mạch điện đó, điện trở R = 0,20 Ω và bỏ qua điện trở của thanh MN và "
           "của hai ray. Cường độ dòng điện chạy qua R là",
         o=["3,0 A.", "0,12 A.", "0,30 A.", "1,2 A."],
         a="A",
         sol="Suất điện động cảm ứng e = B·ℓ·v = 0,40 × 0,50 × 3,0 = 0,60 V.\n"
             "Cường độ dòng điện: I = e/R = 0,60/0,20 = 3,0 A.\n"
             "Kết quả 0,12 A ứng với phép nhân e·R thay vì chia."),

    dict(q="Cũng theo đồ thị dòng điện xoay chiều ở Câu 6, cường độ dòng điện hiệu dụng "
           "xấp xỉ",
         o=["2,83 A.", "4,00 A.", "5,66 A.", "2,00 A."],
         a="A",
         sol="I = I₀/√2 = 4,0/1,414 ≈ 2,83 A. Đây là giá trị mà một ampe kế xoay chiều sẽ "
             "chỉ. Giá trị 5,66 A ứng với việc NHÂN thay vì chia cho √2."),

    dict(q="Cũng theo đồ thị đó, tần số của dòng điện là",
         o=["50 Hz.", "25 Hz.", "100 Hz.", "20 Hz."],
         a="A",
         sol="Từ đồ thị, chu kì T = 0,020 s, do đó f = 1/T = 1/0,020 = 50 Hz."),

    dict(q="Một suất điện động xoay chiều có biểu thức e = 220√2·cos(100πt) V, trong đó t "
           "tính bằng giây. Giá trị hiệu dụng của suất điện động này là",
         o=["220 V.", "311 V.", "110 V.", "220√2 V."],
         a="A",
         sol="Từ biểu thức, giá trị cực đại là E₀ = 220√2 V. Giá trị hiệu dụng:\n"
             "E = E₀/√2 = 220√2/√2 = 220 V.\n"
             "Con số 311 V chính là 220√2, tức giá trị cực đại chứ không phải hiệu dụng."),

    dict(q="Một khung dây gồm 500 vòng, diện tích mỗi vòng 200 cm², quay đều với tốc độ "
           "góc 100π rad/s quanh một trục vuông góc với từ trường đều B = 0,20 T. Lấy "
           "π = 3,14. Suất điện động cực đại của khung xấp xỉ",
         o=["628 V.", "200 V.", "314 V.", "1256 V."],
         a="A",
         sol="Diện tích mỗi vòng: S = 200 cm² = 0,020 m².\n"
             "E₀ = N·B·S·ω = 500 × 0,20 × 0,020 × 100π = 2,0 × 314 = 628 V.\n"
             "(Trước hết 500 × 0,20 × 0,020 = 2,0 Wb là từ thông cực đại qua cả khung.)"),

    dict(q="Vẫn với mạch thanh dẫn trượt trong hình vẽ ở Câu 5. Nếu tăng tốc độ trượt của "
           "thanh lên gấp đôi đồng thời giảm cảm ứng từ còn một nửa thì suất điện động "
           "cảm ứng sẽ",
         fig="t33a",
         o=["không thay đổi.", "tăng gấp đôi.",
            "giảm còn một nửa.", "tăng gấp bốn lần."],
         a="A",
         sol="e = B·ℓ·v tỉ lệ thuận với tích B·v. Khi v tăng 2 lần còn B giảm 2 lần thì "
             "tích B·v không đổi, nên suất điện động giữ nguyên. Tuy nhiên lực cản tác "
             "dụng lên thanh và công suất toả nhiệt trên R thì lại thay đổi, vì chúng phụ "
             "thuộc riêng vào B."),

    dict(q="Một dòng điện xoay chiều có biểu thức i = 2√2·cos(100πt + π/3) A, với t tính "
           "bằng giây. Tại thời điểm t = 0, cường độ dòng điện tức thời xấp xỉ",
         o=["1,41 A.", "2,83 A.", "2,00 A.", "2,45 A."],
         a="A",
         sol="Thay t = 0 vào biểu thức:\n"
             "i = 2√2·cos(π/3) = 2√2 × 0,50 = √2 ≈ 1,41 A.\n"
             "Con số 2,83 A là giá trị CỰC ĐẠI I₀ = 2√2 A, còn 2,00 A là giá trị HIỆU "
             "DỤNG — cả hai đều không phải giá trị tức thời tại t = 0."),
]

DE3_P2 = [
    dict(stem="Hình vẽ mô tả một thanh dẫn MN dài ℓ = 50 cm trượt đều với tốc độ "
              "v = 3,0 m/s trên hai thanh ray song song, trong từ trường đều có cảm ứng "
              "từ B = 0,40 T vuông góc với mặt phẳng chứa hai ray. Điện trở R = 0,20 Ω; "
              "bỏ qua điện trở của thanh MN và của hai ray.",
         fig="t33a",
         items=[
             ("Khi thanh MN trượt sang phải, từ thông qua mạch giảm vì thanh đi ra xa "
              "điện trở R.", False,
              "Ngược lại: thanh trượt sang phải làm phần diện tích của mạch kín TĂNG lên, "
              "nên từ thông Φ = B·S cũng TĂNG. Khoảng cách tới điện trở R không phải là "
              "yếu tố quyết định."),
             ("Suất điện động cảm ứng xuất hiện trong mạch là 0,60 V.", True,
              "Thanh MN, vectơ vận tốc và vectơ cảm ứng từ đôi một vuông góc nên áp "
              "dụng được công thức e = B·ℓ·v:\n"
              "e = 0,40 × 0,50 × 3,0 = 0,60 V."),
             ("Cường độ dòng điện chạy qua điện trở R là 0,12 A.", False,
              "I = e/R = 0,60/0,20 = 3,0 A. Giá trị 0,12 A là kết quả của phép nhân "
              "0,60 × 0,20, tức nhầm công thức định luật Ohm."),
             ("Nếu thanh MN đứng yên thì trong mạch không có dòng điện, dù từ trường vẫn "
              "tồn tại.", True,
              "Thanh đứng yên thì diện tích mạch không đổi, cảm ứng từ cũng không đổi, do "
              "đó từ thông không biến thiên và không có suất điện động cảm ứng. Từ trường "
              "tồn tại nhưng không biến thiên thì không sinh ra dòng điện."),
         ]),

    dict(stem="Hình vẽ là đồ thị cường độ dòng điện xoay chiều chạy trong một đoạn mạch "
              "theo thời gian.",
         fig="t33b",
         items=[
             ("Chu kì của dòng điện là 0,020 s.", True,
              "Đọc trên đồ thị: đồ thị lặp lại sau mỗi 20 ms, tức T = 0,020 s. Tương ứng "
              "tần số f = 1/T = 50 Hz."),
             ("Cường độ dòng điện hiệu dụng là 4,0 A.", False,
              "4,0 A là giá trị CỰC ĐẠI đọc trên đồ thị. Giá trị hiệu dụng nhỏ hơn √2 "
              "lần: I = 4,0/√2 ≈ 2,83 A. Đây là chỗ nhầm lẫn rất phổ biến khi đọc đồ thị "
              "dòng điện xoay chiều."),
             ("Trong 1,0 s dòng điện đổi chiều 100 lần.", True,
              "Mỗi chu kì dòng điện đổi chiều 2 lần; trong 1,0 s có 50 chu kì nên số lần "
              "đổi chiều là 50 × 2 = 100 lần."),
             ("Tại thời điểm t = 10 ms, cường độ dòng điện đạt giá trị cực đại 4,0 A.",
              False,
              "Từ đồ thị, tại t = 10 ms (nửa chu kì) dòng điện có giá trị −4,0 A, tức đạt "
              "độ lớn cực đại nhưng theo chiều NGƯỢC lại. Giá trị +4,0 A chỉ đạt được ở "
              "t = 0 và t = 20 ms."),
         ]),

    dict(stem="Hình vẽ là sơ đồ nguyên tắc của một máy phát điện xoay chiều một pha.",
         fig="t33c",
         items=[
             ("Bộ phận tạo ra từ trường trong máy được gọi là phần ứng.", False,
              "Bộ phận tạo ra từ trường (nam châm) gọi là PHẦN CẢM. Phần ứng là bộ phận "
              "trong đó xuất hiện suất điện động cảm ứng, ở đây là khung dây quay."),
             ("Máy hoạt động dựa trên hiện tượng cảm ứng điện từ.", True,
              "Khung dây quay làm góc giữa pháp tuyến của khung và vectơ cảm ứng từ thay "
              "đổi liên tục, khiến từ thông qua khung biến thiên tuần hoàn và sinh ra "
              "suất điện động cảm ứng biến thiên điều hoà."),
             ("Suất điện động cảm ứng đạt giá trị cực đại khi mặt phẳng khung dây vuông "
              "góc với các đường sức từ.", False,
              "Khi mặt phẳng khung vuông góc với đường sức thì từ thông đạt CỰC ĐẠI, "
              "nhưng đúng lúc đó tốc độ biến thiên của từ thông lại bằng 0 nên suất điện "
              "động bằng 0. Suất điện động cực đại xảy ra khi mặt phẳng khung SONG SONG "
              "với các đường sức, tức khi từ thông bằng 0."),
             ("Nếu tăng tốc độ quay của khung dây lên gấp đôi thì cả tần số lẫn suất điện "
              "động cực đại đều tăng gấp đôi.", True,
              "Tần số f = ω/(2π) tỉ lệ thuận với tốc độ góc ω. Suất điện động cực đại "
              "E₀ = N·B·S·ω cũng tỉ lệ thuận với ω. Vì vậy cả hai đại lượng cùng tăng gấp "
              "đôi."),
         ]),

    dict(stem="Một khung dây phẳng gồm 400 vòng, diện tích mỗi vòng 250 cm², quay đều "
              "quanh một trục vuông góc với từ trường đều có cảm ứng từ B = 0,20 T, với "
              "tốc độ góc ω = 100π rad/s. Lấy π = 3,14.",
         items=[
             ("Tần số của suất điện động xoay chiều do khung tạo ra là 50 Hz.", True,
              "f = ω/(2π) = 100π/(2π) = 50 Hz, tương ứng chu kì T = 0,020 s."),
             ("Từ thông cực đại qua khung dây là 2,0 Wb.", True,
              "Φ₀ = N·B·S = 400 × 0,20 × 0,025 = 2,0 Wb (với S = 250 cm² = 0,025 m²)."),
             ("Suất điện động cực đại của khung là 200 V.", False,
              "E₀ = Φ₀·ω = 2,0 × 100π = 2,0 × 314 = 628 V chứ không phải 200 V."),
             ("Suất điện động hiệu dụng bằng suất điện động cực đại nhân với √2.", False,
              "Ngược lại: E = E₀/√2, tức giá trị hiệu dụng nhỏ hơn giá trị cực đại √2 "
              "lần. Ở đây E = 628/1,414 ≈ 444 V."),
         ]),
]

DE3_P3 = [
    dict(q="Với mạch thanh dẫn trượt ở Câu 5 (ℓ = 50 cm, v = 3,0 m/s, B = 0,40 T), tính "
           "suất điện động cảm ứng xuất hiện trên thanh MN (theo V, làm tròn đến hàng "
           "phần trăm).",
         fig="t33a",
         ans="0,60",
         sol="Thanh dẫn, vectơ vận tốc và vectơ cảm ứng từ đôi một vuông góc nên áp dụng "
             "được công thức e = B·ℓ·v:\n"
             "e = 0,40 × 0,50 × 3,0 = 0,60 V."),

    dict(q="Một thanh dẫn dài 80 cm trượt đều với tốc độ 2,5 m/s trên hai thanh ray nằm "
           "trong từ trường đều có cảm ứng từ 0,50 T vuông góc với mặt phẳng chứa hai "
           "ray. Tính suất điện động cảm ứng trên thanh (theo V, làm tròn đến hàng phần "
           "mười).",
         ans="1,0",
         sol="Thanh dẫn vuông góc với cả vectơ vận tốc lẫn vectơ cảm ứng từ nên dùng "
             "được công thức e = B·ℓ·v:\n"
             "e = 0,50 × 0,80 × 2,5 = 1,0 V.\n"
             "Nhớ đổi chiều dài thanh ra mét: 80 cm = 0,80 m."),

    dict(q="Từ đồ thị dòng điện xoay chiều ở Câu 6, tính cường độ dòng điện hiệu dụng "
           "(theo A, làm tròn đến hàng phần trăm).",
         fig="t33b",
         ans="2,83",
         sol="Đọc trên đồ thị: cường độ cực đại I₀ = 4,0 A.\n"
             "I = I₀/√2 = 4,0/1,414 ≈ 2,83 A."),

    dict(q="Một khung dây gồm 250 vòng, diện tích mỗi vòng 400 cm², quay đều với tốc độ "
           "góc 100π rad/s quanh một trục vuông góc với từ trường đều có cảm ứng từ "
           "0,10 T. Lấy π = 3,14. Tính suất điện động cực đại của khung (theo V, làm tròn "
           "đến hàng đơn vị).",
         ans="314",
         sol="Diện tích mỗi vòng: S = 400 cm² = 0,040 m².\n"
             "Từ thông cực đại: Φ₀ = N·B·S = 250 × 0,10 × 0,040 = 1,0 Wb.\n"
             "E₀ = Φ₀·ω = 1,0 × 100π = 314 V."),

    dict(q="Một dòng điện xoay chiều có biểu thức i = 5cos(120πt) A, với t tính bằng "
           "giây. Tính tần số của dòng điện (theo Hz, làm tròn đến hàng đơn vị).",
         ans="60",
         sol="Từ biểu thức, tốc độ góc ω = 120π rad/s.\n"
             "f = ω/(2π) = 120π/(2π) = 60 Hz."),

    dict(q="Một điện áp xoay chiều có biểu thức u = 220√2·cos(100πt) V, với t tính bằng "
           "giây. Tính giá trị hiệu dụng của điện áp (theo V, làm tròn đến hàng đơn vị).",
         ans="220",
         sol="Giá trị cực đại U₀ = 220√2 V.\n"
             "U = U₀/√2 = 220√2/√2 = 220 V. Đây chính là điện áp mà một vôn kế xoay chiều "
             "sẽ chỉ, và cũng là điện áp danh định của mạng điện dân dụng."),
]

DE3 = dict(code="C3-03", so="03", chuong=3,
           title="ĐỀ KIỂM TRA CHƯƠNG III – ĐỀ SỐ 03",
           subtitle="Chương III – Từ trường",
           p1=DE3_P1, p2=DE3_P2, p3=DE3_P3)


# ===================================================================================
#            ĐỀ SỐ 04 – MÁY BIẾN ÁP VÀ TRUYỀN TẢI ĐIỆN NĂNG
# ===================================================================================

DE4_P1 = [
    dict(q="Máy biến áp hoạt động dựa trên",
         o=["hiện tượng cảm ứng điện từ.",
            "tác dụng nhiệt của dòng điện.",
            "hiện tượng tự nhiễm điện của kim loại.",
            "lực từ tác dụng lên khung dây mang dòng điện."],
         a="A",
         sol="Dòng điện xoay chiều ở cuộn sơ cấp tạo ra từ thông biến thiên trong lõi "
             "thép; từ thông này xuyên qua cuộn thứ cấp và làm xuất hiện suất điện động "
             "cảm ứng ở đó. Đó chính là hiện tượng cảm ứng điện từ."),

    dict(q="Theo thuyết điện từ của Maxwell, khi một từ trường biến thiên theo thời gian "
           "thì trong vùng không gian xung quanh nó xuất hiện",
         o=["một điện trường xoáy.", "một dòng điện không đổi.",
            "một điện tích điểm dương.", "một trường hấp dẫn."],
         a="A",
         sol="Từ trường biến thiên sinh ra một điện trường xoáy — điện trường có các "
             "đường sức khép kín. Nếu trong vùng đó có một vòng dây kín thì chính điện "
             "trường xoáy này đẩy các electron chạy vòng quanh, tạo ra dòng điện cảm ứng. "
             "Ngược lại, điện trường biến thiên lại sinh ra từ trường; hai quá trình đó "
             "nối tiếp nhau tạo thành sóng điện từ lan truyền trong không gian."),

    dict(q="Với một máy biến áp lí tưởng, mối liên hệ giữa điện áp hiệu dụng và số vòng "
           "dây ở hai cuộn là",
         o=["U₁/U₂ = N₁/N₂.", "U₁/U₂ = N₂/N₁.",
            "U₁·U₂ = N₁·N₂.", "U₁ + U₂ = N₁ + N₂."],
         a="A",
         sol="U₁/U₂ = N₁/N₂: điện áp ở mỗi cuộn tỉ lệ thuận với số vòng dây của cuộn đó. "
             "Nếu N₂ > N₁ thì U₂ > U₁ và ta có máy tăng áp; ngược lại là máy hạ áp."),

    dict(q="Hình vẽ là sơ đồ một máy biến áp. Nếu cuộn thứ cấp có số vòng dây lớn hơn "
           "cuộn sơ cấp thì đó là",
         fig="t34a",
         o=["máy tăng áp.", "máy hạ áp.",
            "máy giữ nguyên điện áp.", "máy đổi tần số dòng điện."],
         a="A",
         sol="Từ U₂ = U₁·N₂/N₁: khi N₂ > N₁ thì U₂ > U₁, tức máy làm tăng điện áp — đó là "
             "máy tăng áp. Máy biến áp không bao giờ làm thay đổi tần số của dòng điện "
             "xoay chiều."),

    dict(q="Với máy biến áp lí tưởng, nếu điện áp ở cuộn thứ cấp tăng lên k lần so với "
           "cuộn sơ cấp thì cường độ dòng điện ở cuộn thứ cấp",
         o=["giảm đi k lần.", "tăng lên k lần.",
            "giảm đi k² lần.", "không thay đổi."],
         a="A",
         sol="Máy biến áp lí tưởng bảo toàn công suất: U₁·I₁ = U₂·I₂. Nếu U₂ = k·U₁ thì "
             "I₂ = I₁/k. Máy biến áp làm thay đổi điện áp và cường độ dòng điện theo hai "
             "chiều ngược nhau, chứ không tạo thêm công suất."),

    dict(q="Hình vẽ là sơ đồ truyền tải điện năng đi xa. Người ta phải dùng máy tăng áp ở "
           "đầu đường dây vì",
         fig="t34c",
         o=["tăng điện áp làm giảm cường độ dòng điện, do đó giảm hao phí toả nhiệt.",
            "tăng điện áp làm tăng công suất mà nhà máy điện phát ra được.",
            "tăng điện áp làm giảm điện trở của dây dẫn trên đường truyền.",
            "tăng điện áp giúp dòng điện truyền đi với tốc độ lớn hơn."],
         a="A",
         sol="Với cùng công suất truyền tải P, cường độ dòng điện I = P/U giảm khi U tăng. "
             "Công suất hao phí P_hp = I²R giảm theo bình phương, nên tăng điện áp là "
             "biện pháp hiệu quả nhất. Điện trở R của đường dây phụ thuộc vật liệu và "
             "kích thước dây, không phụ thuộc điện áp."),

    dict(q="Công suất hao phí do toả nhiệt trên đường dây tải điện có điện trở R khi "
           "truyền công suất P ở điện áp U (hệ số công suất bằng 1) được tính bằng",
         o=["P_hp = R·P²/U².", "P_hp = R·U²/P²",
            "P_hp = R·P/U.", "P_hp = R·P·U."],
         a="A",
         sol="Cường độ dòng điện trên đường dây I = P/U, do đó\n"
             "P_hp = I²·R = R·P²/U².\n"
             "Công thức cho thấy hao phí tỉ lệ NGHỊCH với bình phương điện áp truyền tải."),

    dict(q="Nếu tăng điện áp truyền tải lên 5 lần mà giữ nguyên công suất truyền đi và "
           "điện trở đường dây thì công suất hao phí trên đường dây",
         o=["giảm 25 lần.", "giảm 5 lần.", "tăng 25 lần.", "giảm 10 lần."],
         a="A",
         sol="P_hp = R·P²/U² tỉ lệ nghịch với U². Khi U tăng 5 lần thì U² tăng 25 lần, do "
             "đó hao phí giảm 25 lần. Đây là lí do các đường dây truyền tải cao thế dùng "
             "điện áp tới hàng trăm kilôvôn."),

    dict(q="Hình vẽ là đồ thị từ thông Φ và suất điện động cảm ứng e của một khung dây "
           "quay đều trong từ trường đều. Suất điện động đạt giá trị cực đại vào lúc",
         fig="t34b",
         o=["từ thông qua khung bằng 0.",
            "từ thông qua khung đạt giá trị cực đại.",
            "từ thông qua khung bằng một nửa giá trị cực đại.",
            "khung dây vừa bắt đầu quay từ trạng thái nghỉ."],
         a="A",
         sol="Trên đồ thị, đường e đạt đỉnh đúng vào những thời điểm đường Φ cắt trục "
             "hoành. Điều này phù hợp với e = −ΔΦ/Δt: suất điện động bằng tốc độ biến "
             "thiên của từ thông, mà từ thông biến thiên nhanh nhất khi nó đi qua giá trị "
             "0. Hai đại lượng lệch pha nhau π/2."),

    dict(q="Lõi thép của máy biến áp được ghép từ nhiều lá thép mỏng cách điện với nhau "
           "nhằm",
         o=["giảm hao phí năng lượng do dòng điện Foucault.",
            "làm tăng số vòng dây quấn được trên lõi.",
            "làm giảm điện trở của các cuộn dây.",
            "làm tăng tần số của dòng điện ở cuộn thứ cấp."],
         a="A",
         sol="Từ thông biến thiên trong lõi thép sinh ra dòng điện Foucault, làm nóng lõi "
             "và gây hao phí. Ghép lõi từ các lá thép mỏng sơn cách điện sẽ cắt nhỏ các "
             "đường dòng Foucault, làm điện trở của các mạch xoáy tăng lên và hao phí "
             "giảm mạnh."),

    dict(q="Một máy biến áp lí tưởng có cuộn sơ cấp 2000 vòng, cuộn thứ cấp 500 vòng. Đặt "
           "vào hai đầu cuộn sơ cấp một điện áp xoay chiều có giá trị hiệu dụng 220 V thì "
           "điện áp hiệu dụng ở hai đầu cuộn thứ cấp là",
         o=["55 V.", "880 V.", "110 V.", "44 V."],
         a="A",
         sol="U₂ = U₁·N₂/N₁ = 220 × 500/2000 = 220 × 0,25 = 55 V.\n"
             "Vì N₂ < N₁ nên đây là máy hạ áp và U₂ phải nhỏ hơn 220 V; kết quả 880 V "
             "(lấy tỉ số ngược) là vô lí."),

    dict(q="Một máy biến áp lí tưởng có điện áp hiệu dụng ở cuộn sơ cấp 220 V, ở cuộn thứ "
           "cấp 12 V. Cường độ dòng điện hiệu dụng ở cuộn thứ cấp là 5,0 A. Cường độ dòng "
           "điện hiệu dụng ở cuộn sơ cấp xấp xỉ",
         o=["0,27 A.", "5,0 A.", "92 A.", "2,7 A."],
         a="A",
         sol="Máy biến áp lí tưởng bảo toàn công suất: U₁·I₁ = U₂·I₂.\n"
             "I₁ = U₂·I₂/U₁ = 12 × 5,0/220 = 60/220 ≈ 0,27 A.\n"
             "Điện áp ở cuộn sơ cấp lớn hơn nên dòng điện ở cuộn sơ cấp phải nhỏ hơn."),

    dict(q="Người ta truyền một công suất điện 100 kW ở điện áp 10 kV trên một đường dây "
           "có điện trở 5,0 Ω, hệ số công suất bằng 1. Công suất hao phí trên đường dây là",
         o=["500 W.", "50 W.", "5,0 kW.", "1,0 kW."],
         a="A",
         sol="Cường độ dòng điện trên đường dây: I = P/U = 100·10³/(10·10³) = 10 A.\n"
             "Công suất hao phí: P_hp = I²·R = 10² × 5,0 = 500 W."),

    dict(q="Vẫn với đường dây truyền tải ở câu trên, hiệu suất của quá trình truyền tải "
           "điện năng là",
         o=["99,5 %.", "95,0 %.", "99,9 %.", "50,0 %."],
         a="A",
         sol="Hiệu suất H = (P − P_hp)/P = (100 000 − 500)/100 000 = 99 500/100 000 "
             "= 0,995 = 99,5 %."),

    dict(q="Với cùng công suất truyền tải và cùng điện trở đường dây, muốn giảm công suất "
           "hao phí từ 500 W xuống còn 125 W thì phải tăng điện áp truyền tải lên",
         o=["2 lần.", "4 lần.", "16 lần.", "√2 lần."],
         a="A",
         sol="P_hp tỉ lệ nghịch với U². Hao phí giảm 500/125 = 4 lần nghĩa là U² tăng "
             "4 lần, do đó U tăng √4 = 2 lần."),

    dict(q="Một máy biến áp lí tưởng có cuộn sơ cấp 1000 vòng, được mắc vào điện áp xoay "
           "chiều 240 V. Muốn điện áp ở cuộn thứ cấp là 6,0 V thì cuộn thứ cấp phải có",
         o=["25 vòng.", "40 vòng.", "250 vòng.", "160 vòng."],
         a="A",
         sol="Với máy biến áp lí tưởng, U₁/U₂ = N₁/N₂ nên\n"
             "N₂ = N₁·U₂/U₁ = 1000 × 6,0/240 = 1000/40 = 25 vòng.\n"
             "Điện áp giảm 40 lần thì số vòng dây cũng phải giảm đúng 40 lần."),

    dict(q="Vẫn với đồ thị ở Câu 9. Độ lệch pha giữa suất điện động cảm ứng e và từ thông "
           "Φ qua khung dây là",
         fig="t34b",
         o=["π/2.", "π.", "π/4.", "0."],
         a="A",
         sol="Nếu Φ = Φ₀·cos(ωt) thì e = −ΔΦ/Δt cho e = Φ₀·ω·sin(ωt) = "
             "E₀·cos(ωt − π/2). Vậy e trễ pha π/2 so với Φ. Trên đồ thị điều này thể hiện "
             "ở chỗ đỉnh của đường e nằm đúng tại vị trí đường Φ cắt trục hoành."),

    dict(q="Một trạm phát truyền đi công suất 200 kW ở điện áp 20 kV; công suất hao phí "
           "trên đường dây là 4,0 kW, hệ số công suất bằng 1. Điện trở của đường dây tải "
           "điện là",
         o=["40 Ω.", "20 Ω.", "10 Ω.", "80 Ω."],
         a="A",
         sol="Cường độ dòng điện: I = P/U = 200·10³/(20·10³) = 10 A.\n"
             "Từ P_hp = I²·R suy ra R = P_hp/I² = 4000/100 = 40 Ω."),
]

DE4_P2 = [
    dict(stem="Hình vẽ là sơ đồ một máy biến áp lí tưởng có cuộn sơ cấp N₁ = 1100 vòng, "
              "cuộn thứ cấp N₂ = 60 vòng. Đặt vào hai đầu cuộn sơ cấp một điện áp xoay "
              "chiều có giá trị hiệu dụng 220 V.",
         fig="t34a",
         items=[
             ("Đây là một máy hạ áp.", True,
              "Vì N₂ = 60 < N₁ = 1100 nên U₂ < U₁: máy làm giảm điện áp, tức máy hạ áp."),
             ("Điện áp hiệu dụng ở hai đầu cuộn thứ cấp là 12 V.", True,
              "U₂ = U₁·N₂/N₁ = 220 × 60/1100. Tỉ số vòng dây là 1100/60 ≈ 18,33 nên\n"
              "U₂ = 220/18,33 = 12 V. Đây chính là điện áp thường gặp ở các bộ nguồn "
              "một chiều 12 V dùng trong gia đình."),
             ("Nếu cuộn thứ cấp được nối với một tải tiêu thụ công suất 24 W thì cường độ "
              "dòng điện qua cuộn sơ cấp là 2,0 A.", False,
              "Máy lí tưởng nên công suất ở cuộn sơ cấp cũng bằng 24 W:\n"
              "I₁ = P/U₁ = 24/220 ≈ 0,11 A chứ không phải 2,0 A. Giá trị 2,0 A chính là "
              "cường độ dòng điện ở cuộn THỨ CẤP (24/12 = 2,0 A)."),
             ("Có thể dùng máy biến áp này với một nguồn điện không đổi 220 V để thu được "
              "12 V ở cuộn thứ cấp.", False,
              "Không được. Nguồn không đổi tạo ra từ thông không đổi trong lõi thép, nên "
              "không có suất điện động cảm ứng ở cuộn thứ cấp và điện áp ra bằng 0. Máy "
              "biến áp chỉ làm việc với dòng điện xoay chiều."),
         ]),

    dict(stem="Hình vẽ là sơ đồ truyền tải điện năng đi xa. Một trạm phát truyền công "
              "suất 500 kW ở điện áp 25 kV; đường dây có điện trở tổng cộng 20 Ω; hệ số "
              "công suất bằng 1.",
         fig="t34c",
         items=[
             ("Cường độ dòng điện chạy trên đường dây là 50 A.", False,
              "Cường độ dòng điện trên đường dây được tính từ công suất truyền tải và "
              "điện áp truyền tải:\n"
              "I = P/U = 500·10³/(25·10³) = 20 A chứ không phải 50 A."),
             ("Công suất hao phí trên đường dây là 8,0 kW.", True,
              "Dùng cường độ dòng điện đúng I = 20 A vừa tìm được:\n"
              "P_hp = I²·R = 20² × 20 = 400 × 20 = 8000 W = 8,0 kW.\n"
              "Đây là phần công suất bị biến thành nhiệt trên chính đường dây."),
             ("Hiệu suất của quá trình truyền tải là 98,4 %.", True,
              "H = (P − P_hp)/P = (500 − 8,0)/500 = 492/500 = 0,984 = 98,4 %."),
             ("Nếu tăng điện áp truyền tải lên 50 kV thì công suất hao phí giảm còn "
              "4,0 kW.", False,
              "Điện áp tăng 2 lần thì hao phí giảm 2² = 4 lần, tức còn "
              "8,0/4 = 2,0 kW chứ không phải 4,0 kW (4,0 kW mới ứng với việc giảm 2 lần)."),
         ]),

    dict(stem="Hình vẽ là đồ thị từ thông Φ qua một khung dây quay đều trong từ trường "
              "đều và suất điện động cảm ứng e xuất hiện trong khung, theo thời gian.",
         fig="t34b",
         items=[
             ("Suất điện động cảm ứng biến thiên điều hoà cùng tần số với từ thông.", True,
              "Hai đường trên đồ thị có cùng chu kì 20 ms, tức cùng tần số 50 Hz. Điều đó "
              "phù hợp với việc e là đạo hàm của Φ theo thời gian nên chỉ khác Φ ở biên "
              "độ và pha, không khác ở tần số."),
             ("Suất điện động đạt giá trị cực đại đúng vào lúc từ thông bằng 0.", True,
              "Trên đồ thị, đỉnh của đường e trùng với thời điểm đường Φ cắt trục hoành. "
              "Về mặt vật lí, từ thông biến thiên nhanh nhất khi nó đi qua giá trị 0, nên "
              "|e| = |ΔΦ/Δt| lớn nhất tại đó."),
             ("Suất điện động và từ thông luôn cùng pha với nhau.", False,
              "Chúng lệch pha nhau π/2 (một phần tư chu kì, tức 5 ms trên đồ thị này). "
              "Nếu chúng cùng pha thì hai đường sẽ đạt cực đại cùng lúc, trái với hình vẽ."),
             ("Khi từ thông qua khung đạt giá trị cực đại thì suất điện động cũng đạt giá "
              "trị cực đại.", False,
              "Khi Φ cực đại thì đồ thị Φ có tiếp tuyến nằm ngang, tức tốc độ biến thiên "
              "bằng 0, do đó e = 0. Đây là hệ quả trực tiếp của e = −ΔΦ/Δt."),
         ]),

    dict(stem="Xét các phát biểu về máy biến áp và ứng dụng của nó.",
         items=[
             ("Máy biến áp làm thay đổi điện áp xoay chiều nhưng không làm thay đổi tần "
              "số của dòng điện.", True,
              "Từ thông trong lõi thép biến thiên đúng theo nhịp của dòng điện sơ cấp, "
              "nên suất điện động cảm ứng ở cuộn thứ cấp có cùng tần số. Máy biến áp chỉ "
              "thay đổi cặp giá trị (U, I) chứ không thay đổi f."),
             ("Máy biến áp có thể làm tăng công suất điện truyền qua nó.", False,
              "Máy biến áp không phải nguồn năng lượng. Với máy lí tưởng, công suất ra "
              "bằng công suất vào (U₁I₁ = U₂I₂); với máy thực, công suất ra còn nhỏ hơn "
              "do hao phí ở lõi thép và cuộn dây."),
             ("Với máy biến áp lí tưởng, tỉ số cường độ dòng điện ở hai cuộn bằng tỉ số "
              "nghịch đảo của số vòng dây, tức I₁/I₂ = N₂/N₁.", True,
              "Từ U₁I₁ = U₂I₂ và U₁/U₂ = N₁/N₂ suy ra I₁/I₂ = U₂/U₁ = N₂/N₁. Cuộn nào có "
              "nhiều vòng hơn thì mang dòng điện nhỏ hơn, nên có thể quấn bằng dây mảnh "
              "hơn."),
             ("Lõi thép của máy biến áp được làm bằng một khối thép đặc để dẫn từ tốt "
              "nhất.", False,
              "Lõi được ghép từ nhiều lá thép mỏng sơn cách điện nhằm hạn chế dòng điện "
              "Foucault. Một khối thép đặc tuy dẫn từ tốt nhưng sẽ sinh dòng Foucault rất "
              "mạnh, làm lõi nóng lên và gây hao phí lớn."),
         ]),
]

DE4_P3 = [
    dict(q="Một máy biến áp lí tưởng có cuộn sơ cấp gồm 1500 vòng được mắc vào điện áp "
           "xoay chiều 220 V; cuộn thứ cấp gồm 300 vòng. Tính điện áp hiệu dụng ở hai "
           "đầu cuộn thứ cấp (theo V, làm tròn đến hàng đơn vị).",
         ans="44",
         sol="Với máy biến áp lí tưởng, điện áp ở mỗi cuộn tỉ lệ thuận với số vòng "
             "dây của cuộn đó:\n"
             "U₂ = U₁·N₂/N₁ = 220 × 300/1500 = 220 × 0,20 = 44 V.\n"
             "Vì N₂ < N₁ nên đây là máy hạ áp, kết quả nhỏ hơn 220 V là hợp lí."),

    dict(q="Một máy biến áp lí tưởng có điện áp hiệu dụng ở cuộn sơ cấp 220 V và ở cuộn "
           "thứ cấp 12 V. Cuộn thứ cấp đang có dòng điện hiệu dụng 5,0 A. Tính cường độ "
           "dòng điện hiệu dụng ở cuộn sơ cấp (theo A, làm tròn đến hàng phần trăm).",
         ans="0,27",
         sol="Máy lí tưởng bảo toàn công suất: U₁·I₁ = U₂·I₂.\n"
             "I₁ = U₂·I₂/U₁ = 12 × 5,0/220 = 60/220 ≈ 0,27 A."),

    dict(q="Người ta truyền một công suất điện 120 kW ở điện áp 12 kV trên đường dây có "
           "điện trở 8,0 Ω, hệ số công suất bằng 1. Tính công suất hao phí trên đường dây "
           "(theo kW, làm tròn đến hàng phần mười).",
         ans="0,8",
         sol="Cường độ dòng điện: I = P/U = 120·10³/(12·10³) = 10 A.\n"
             "P_hp = I²·R = 10² × 8,0 = 800 W = 0,80 kW."),

    dict(q="Vẫn với đường dây truyền tải ở Câu 3 của phần này. Tính hiệu suất của quá "
           "trình truyền tải điện năng (theo %, làm tròn đến hàng phần mười).",
         ans="99,3",
         sol="H = (P − P_hp)/P = (120 − 0,80)/120 = 119,2/120 ≈ 0,99333 ≈ 99,3 %."),

    dict(q="Một trạm phát truyền đi công suất 200 kW ở điện áp 20 kV, hệ số công suất "
           "bằng 1. Công suất hao phí trên đường dây là 4,0 kW. Tính điện trở của đường "
           "dây tải điện (theo Ω, làm tròn đến hàng đơn vị).",
         ans="40",
         sol="Cường độ dòng điện: I = P/U = 200·10³/(20·10³) = 10 A.\n"
             "Từ P_hp = I²·R suy ra R = P_hp/I² = 4000/10² = 40 Ω."),

    dict(q="Muốn công suất hao phí trên một đường dây tải điện giảm đi 9 lần trong khi "
           "vẫn giữ nguyên công suất truyền tải và điện trở đường dây thì phải tăng điện "
           "áp truyền tải lên bao nhiêu lần?",
         ans="3",
         sol="P_hp = R·P²/U² tỉ lệ nghịch với U². Muốn P_hp giảm 9 lần thì U² phải tăng "
             "9 lần, do đó U tăng √9 = 3 lần."),
]

DE4 = dict(code="C3-04", so="04", chuong=3,
           title="ĐỀ KIỂM TRA CHƯƠNG III – ĐỀ SỐ 04",
           subtitle="Chương III – Từ trường",
           p1=DE4_P1, p2=DE4_P2, p3=DE4_P3)


# ===================================================================================
#           ĐỀ SỐ 05 – TỔNG HỢP TOÀN CHƯƠNG, PHÂN HOÁ CAO
# ===================================================================================

DE5_P1 = [
    dict(q="Nội dung cơ bản của thuyết điện từ Maxwell là",
         o=["điện trường biến thiên sinh ra từ trường và từ trường biến thiên sinh ra "
            "điện trường.",
            "điện trường và từ trường là hai trường hoàn toàn độc lập với nhau.",
            "chỉ có từ trường biến thiên mới sinh ra được điện trường xoáy.",
            "điện tích đứng yên cũng luôn sinh ra một từ trường quanh nó."],
         a="A",
         sol="Maxwell đã tổng quát hoá: từ trường biến thiên sinh ra điện trường xoáy (đó "
             "chính là hiện tượng cảm ứng điện từ) và ngược lại, điện trường biến thiên "
             "sinh ra từ trường. Hai trường này gắn bó với nhau thành một trường thống "
             "nhất gọi là điện từ trường."),

    dict(q="Sóng điện từ",
         o=["truyền được cả trong chân không.",
            "chỉ truyền được trong môi trường vật chất.",
            "là sóng dọc trong mọi môi trường truyền sóng.",
            "không mang theo năng lượng khi lan truyền."],
         a="A",
         sol="Sóng điện từ là sự lan truyền của điện từ trường, không cần môi trường vật "
             "chất, nên truyền được trong chân không với tốc độ c = 3·10⁸ m/s. Nhờ vậy "
             "ánh sáng và sóng vô tuyến mới truyền được từ các thiên thể tới Trái Đất. "
             "Sóng điện từ là sóng ngang và có mang năng lượng."),

    dict(q="Trong một sóng điện từ đang lan truyền, vectơ cường độ điện trường và vectơ "
           "cảm ứng từ",
         o=["vuông góc với nhau và cùng vuông góc với phương truyền sóng.",
            "song song với nhau và song song với phương truyền sóng.",
            "vuông góc với nhau nhưng một trong hai vectơ trùng phương truyền sóng.",
            "hợp với nhau một góc 45° và quay quanh phương truyền sóng."],
         a="A",
         sol="Trong sóng điện từ, ba vectơ E, B và vectơ vận tốc truyền sóng tạo thành "
             "một tam diện thuận, đôi một vuông góc. Vì E và B đều vuông góc với phương "
             "truyền nên sóng điện từ là sóng NGANG."),

    dict(q="Hình vẽ mô tả ba thiết bị quen thuộc. Bếp từ ở hình (a) làm nóng đáy nồi nhờ",
         fig="t35b",
         o=["dòng điện Foucault sinh ra trong đáy nồi do từ trường biến thiên.",
            "nhiệt lượng toả ra trên cuộn dây rồi truyền lên đáy nồi.",
            "bức xạ hồng ngoại phát ra từ mặt kính của bếp.",
            "ma sát giữa đáy nồi và mặt kính của bếp."],
         a="A",
         sol="Cuộn dây trong bếp từ được cấp dòng điện xoay chiều tần số cao, tạo ra từ "
             "trường biến thiên rất nhanh. Từ trường này sinh ra dòng điện Foucault ngay "
             "trong đáy nồi bằng vật liệu nhiễm từ, và chính dòng Foucault làm đáy nồi "
             "nóng lên. Mặt kính của bếp hầu như không nóng vì nó không dẫn điện."),

    dict(q="Vẫn với hình vẽ đó, bộ sạc không dây ở hình (b) truyền năng lượng từ đế sạc "
           "sang điện thoại nhờ",
         fig="t35b",
         o=["hiện tượng cảm ứng điện từ giữa hai cuộn dây.",
            "sự dẫn điện trực tiếp qua lớp không khí mỏng giữa hai thiết bị.",
            "chùm tia laser hồng ngoại phát ra từ đế sạc.",
            "lực hút tĩnh điện giữa đế sạc và mặt sau điện thoại."],
         a="A",
         sol="Cuộn dây trong đế sạc mang dòng điện xoay chiều tạo ra từ trường biến "
             "thiên; từ thông biến thiên này xuyên qua cuộn dây trong điện thoại và sinh "
             "ra suất điện động cảm ứng, tức năng lượng được truyền sang mà không cần dây "
             "nối. Về bản chất đây là một máy biến áp có lõi không khí."),

    dict(q="Hình vẽ mô tả bốn vị trí của một khung dây quay đều trong từ trường đều, với "
           "n là vectơ pháp tuyến của khung. Từ thông qua khung có độ lớn lớn nhất ở các "
           "vị trí",
         fig="t35c",
         o=["(1) và (3).", "(2) và (4).", "(1) và (2).", "(3) và (4)."],
         a="A",
         sol="Φ = B·S·cosα với α là góc giữa n và B. Ở vị trí (1), n cùng chiều B "
             "(α = 0); ở vị trí (3), n ngược chiều B (α = 180°). Cả hai trường hợp đều có "
             "|cosα| = 1 nên độ lớn từ thông cực đại. Ở (2) và (4), n vuông góc với B nên "
             "Φ = 0."),

    dict(q="Cũng với hình vẽ đó, suất điện động cảm ứng trong khung có độ lớn lớn nhất ở "
           "các vị trí",
         fig="t35c",
         o=["(2) và (4).", "(1) và (3).", "(1) và (2).", "cả bốn vị trí như nhau."],
         a="A",
         sol="Suất điện động bằng tốc độ biến thiên của từ thông. Từ thông biến thiên "
             "nhanh nhất khi nó đi qua giá trị 0, tức ở các vị trí (2) và (4). Ngược lại, "
             "ở (1) và (3) từ thông đạt cực đại nên tốc độ biến thiên bằng 0 và suất điện "
             "động bằng 0."),

    dict(q="Hình vẽ là đồ thị từ thông qua một khung dây theo thời gian, có dạng tam giác "
           "tuần hoàn. Suất điện động cảm ứng trong khung theo thời gian có dạng",
         fig="t35a",
         o=["gồm những đoạn nằm ngang, đổi dấu tuần hoàn (dạng bậc thang).",
            "biến thiên điều hoà theo quy luật hàm sin.",
            "cũng có dạng tam giác giống hệt đồ thị từ thông.",
            "tăng đều theo thời gian trong suốt quá trình."],
         a="A",
         sol="Trên mỗi đoạn thẳng của đồ thị Φ, tốc độ biến thiên ΔΦ/Δt là một hằng số, "
             "nên suất điện động e = −ΔΦ/Δt cũng là hằng số trên đoạn đó. Khi đồ thị Φ "
             "đổi hướng dốc thì e đổi dấu. Kết quả là e có dạng bậc thang (sóng vuông) "
             "chứ không phải hình sin."),

    dict(q="Vẫn với đồ thị đó, độ lớn suất điện động cảm ứng trong khoảng thời gian từ 0 "
           "đến 2 s là",
         fig="t35a",
         o=["0,30 V.", "0,60 V.", "0,15 V.", "1,20 V."],
         a="A",
         sol="Trong khoảng từ 0 đến 2 s, từ thông tăng đều từ 0 lên 0,60 Wb:\n"
             "|e| = |ΔΦ|/Δt = 0,60/2,0 = 0,30 V."),

    dict(q="Cũng theo đồ thị đó, chu kì biến thiên của từ thông qua khung dây là",
         o=["8,0 s.", "4,0 s.", "2,0 s.", "14 s."],
         a="A",
         sol="Đọc trên đồ thị: từ thông trở lại cùng một giá trị và cùng chiều biến thiên "
             "sau mỗi 8,0 s (chẳng hạn từ đỉnh 0,60 Wb tại t = 2 s tới đỉnh tiếp theo tại "
             "t = 10 s). Vậy T = 8,0 s."),

    dict(q="Một khung dây gồm 100 vòng quay đều trong từ trường đều với tần số 50 Hz. Từ "
           "thông cực đại qua mỗi vòng dây là 2,0·10⁻³ Wb. Lấy π = 3,14. Suất điện động "
           "cực đại của khung xấp xỉ",
         o=["62,8 V.", "0,20 V.", "31,4 V.", "125,6 V."],
         a="A",
         sol="Tốc độ góc: ω = 2πf = 2 × 3,14 × 50 = 314 rad/s.\n"
             "E₀ = N·Φ₀ ₁ vòng·ω = 100 × 2,0·10⁻³ × 314 = 0,20 × 314 = 62,8 V."),

    dict(q="Một máy biến áp lí tưởng dùng để hạ điện áp từ 6000 V xuống 220 V. Cuộn thứ "
           "cấp có 110 vòng. Số vòng dây của cuộn sơ cấp là",
         o=["3000 vòng.", "1500 vòng.", "6000 vòng.", "2200 vòng."],
         a="A",
         sol="N₁ = N₂·U₁/U₂ = 110 × 6000/220 = 110 × 27,27 = 3000 vòng.\n"
             "Kiểm tra: 6000/220 = 3000/110 ≈ 27,3 — hai tỉ số bằng nhau."),

    dict(q="Một khung dây kín, phẳng, diện tích 0,020 m², điện trở 0,40 Ω, được đặt trong "
           "từ trường đều có phương vuông góc với mặt phẳng khung. Cảm ứng từ tăng đều "
           "với tốc độ 0,50 T/s. Cường độ dòng điện cảm ứng trong khung là",
         o=["0,025 A.", "0,010 A.", "0,25 A.", "0,040 A."],
         a="A",
         sol="Suất điện động cảm ứng: |e| = S·(ΔB/Δt) = 0,020 × 0,50 = 0,010 V.\n"
             "Cường độ dòng điện: I = |e|/R = 0,010/0,40 = 0,025 A."),

    dict(q="Giữ nguyên công suất truyền tải và điện áp truyền tải, nếu thay dây dẫn bằng "
           "dây cùng chất liệu, cùng chiều dài nhưng có đường kính gấp đôi thì công suất "
           "hao phí trên đường dây sẽ",
         o=["giảm 4 lần.", "giảm 2 lần.", "tăng 4 lần.", "không thay đổi."],
         a="A",
         sol="Điện trở R = ρℓ/S tỉ lệ nghịch với tiết diện S = πd²/4. Đường kính tăng "
             "2 lần thì tiết diện tăng 4 lần, do đó R giảm 4 lần. Vì P_hp = I²R với I "
             "không đổi (P và U giữ nguyên), hao phí cũng giảm 4 lần."),

    dict(q="Một vòng dây kín được kéo đều ra khỏi một vùng từ trường đều rộng, mặt phẳng "
           "vòng dây luôn vuông góc với các đường sức. Trong suốt quá trình vòng dây đang "
           "đi ra khỏi vùng từ trường, dòng điện cảm ứng trong vòng dây",
         o=["có chiều không đổi và cường độ không đổi.",
            "có chiều không đổi nhưng cường độ tăng dần.",
            "đổi chiều liên tục theo thời gian.",
            "bằng không vì cảm ứng từ không thay đổi."],
         a="A",
         sol="Vòng dây chuyển động đều nên diện tích phần còn nằm trong vùng từ trường "
             "giảm với tốc độ không đổi, tức ΔΦ/Δt là một hằng số. Do đó suất điện động "
             "và dòng điện cảm ứng đều không đổi cả về chiều lẫn độ lớn cho tới khi vòng "
             "dây ra hẳn khỏi vùng từ trường."),

    dict(q="Một khung dây quay đều quanh một trục vuông góc với từ trường đều. Ở thời "
           "điểm suất điện động cảm ứng có độ lớn bằng một nửa giá trị cực đại, độ lớn từ "
           "thông qua khung bằng",
         o=["khoảng 0,87 lần từ thông cực đại.",
            "đúng một nửa từ thông cực đại.",
            "khoảng 0,71 lần từ thông cực đại.",
            "bằng 0."],
         a="A",
         sol="Với Φ = Φ₀·cos(ωt) thì e = E₀·sin(ωt).\n"
             "|e| = E₀/2 ⇒ |sin(ωt)| = 1/2 ⇒ |cos(ωt)| = √(1 − 1/4) = √3/2 ≈ 0,87.\n"
             "Do đó |Φ| = 0,87·Φ₀. Điểm mấu chốt là e và Φ lệch pha π/2 nên "
             "(e/E₀)² + (Φ/Φ₀)² = 1."),

    dict(q="Một điện áp xoay chiều 220 V được đưa qua một máy tăng áp có tỉ số vòng dây "
           "1 : 20, rồi tiếp tục qua một máy hạ áp có tỉ số vòng dây 40 : 1. Coi cả hai "
           "máy đều lí tưởng. Điện áp ở đầu ra cuối cùng là",
         o=["110 V.", "220 V.", "440 V.", "55 V."],
         a="A",
         sol="Sau máy tăng áp: U′ = 220 × 20 = 4400 V.\n"
             "Sau máy hạ áp: U″ = 4400/40 = 110 V.\n"
             "Cũng có thể gộp: U″ = 220 × 20/40 = 110 V."),

    dict(q="Một sóng điện từ có tần số 90 MHz truyền trong chân không. Bước sóng của nó "
           "xấp xỉ",
         o=["3,33 m.", "0,30 m.", "27 m.", "2,70 m."],
         a="A",
         sol="λ = c/f = (3·10⁸)/(90·10⁶) = 3·10⁸/9·10⁷ ≈ 3,33 m.\n"
             "Đây là dải sóng FM quen thuộc, có bước sóng vài mét."),
]

DE5_P2 = [
    dict(stem="Một khung dây kín gồm một vòng, điện trở 0,10 Ω, được đặt trong một từ "
              "trường biến thiên. Từ thông qua khung biến đổi theo thời gian như đồ thị "
              "trong hình vẽ.",
         fig="t35a",
         items=[
             ("Chu kì biến thiên của từ thông là 4,0 s.", False,
              "Đọc trên đồ thị, từ thông lặp lại trạng thái sau mỗi 8,0 s (chẳng hạn từ "
              "đỉnh tại t = 2 s tới đỉnh tiếp theo tại t = 10 s). Vậy T = 8,0 s chứ không "
              "phải 4,0 s — 4,0 s chỉ là NỬA chu kì."),
             ("Trong khoảng từ 0 đến 2 s, độ lớn suất điện động cảm ứng là 0,30 V.", True,
              "|e| = |ΔΦ|/Δt = 0,60/2,0 = 0,30 V. Trên đồ thị, đây chính là độ dốc của "
              "đoạn thẳng đầu tiên."),
             ("Trong khoảng từ 2 s đến 6 s, độ lớn suất điện động cảm ứng là 0,15 V.",
              False,
              "Trong khoảng này từ thông giảm từ +0,60 Wb xuống −0,60 Wb, tức "
              "|ΔΦ| = 1,20 Wb trong Δt = 4,0 s:\n"
              "|e| = 1,20/4,0 = 0,30 V. Kết quả 0,15 V là do chỉ lấy |ΔΦ| = 0,60 Wb mà "
              "quên rằng từ thông đổi dấu."),
             ("Cường độ dòng điện cảm ứng trong khung có độ lớn không đổi và bằng 3,0 A.",
              True,
              "Vì đồ thị Φ gồm các đoạn thẳng có cùng độ dốc về độ lớn nên |e| = 0,30 V "
              "trong mọi giai đoạn.\n"
              "I = |e|/R = 0,30/0,10 = 3,0 A. Dòng điện chỉ đổi CHIỀU sau mỗi nửa chu kì "
              "chứ không đổi độ lớn."),
         ]),

    dict(stem="Hình vẽ mô tả bốn vị trí đặc biệt của một khung dây quay đều trong từ "
              "trường đều, với n là vectơ pháp tuyến của mặt phẳng khung.",
         fig="t35c",
         items=[
             ("Ở các vị trí (1) và (3), từ thông qua khung có độ lớn lớn nhất.", True,
              "Ở hai vị trí này pháp tuyến n cùng phương với B (cùng chiều ở (1), ngược "
              "chiều ở (3)), nên |cosα| = 1 và |Φ| = B·S đạt giá trị lớn nhất."),
             ("Ở các vị trí (2) và (4), từ thông qua khung bằng 0.", True,
              "Ở đó n vuông góc với B nên cosα = 0 và Φ = 0. Về hình học, mặt phẳng khung "
              "khi ấy chứa các đường sức từ nên không có đường sức nào xuyên qua khung."),
             ("Ở các vị trí (1) và (3), suất điện động cảm ứng có độ lớn lớn nhất.", False,
              "Ngược lại, ở (1) và (3) suất điện động bằng 0. Từ thông đang đạt cực trị "
              "nên tốc độ biến thiên của nó bằng 0, mà e = −ΔΦ/Δt."),
             ("Ở vị trí (2), suất điện động cảm ứng bằng 0 vì từ thông qua khung bằng 0.",
              False,
              "Kết luận sai và lí do cũng sai. Ở vị trí (2) từ thông bằng 0 nhưng nó đang "
              "biến thiên NHANH NHẤT, nên suất điện động đạt giá trị CỰC ĐẠI. Giá trị của "
              "từ thông không quyết định suất điện động; chỉ tốc độ biến thiên của nó mới "
              "quyết định."),
         ]),

    dict(stem="Hình vẽ mô tả ba thiết bị: (a) bếp từ, (b) bộ sạc không dây, (c) đèn pin "
              "lắc tay.",
         fig="t35b",
         items=[
             ("Ở bếp từ (a), đáy nồi nóng lên là do dòng điện Foucault sinh ra ngay trong "
              "đáy nồi.", True,
              "Cuộn dây của bếp tạo ra từ trường biến thiên tần số cao; từ trường này "
              "sinh dòng Foucault khép kín trong đáy nồi và chính dòng đó toả nhiệt làm "
              "nóng nồi. Nhờ vậy hiệu suất bếp từ rất cao và mặt bếp gần như không nóng."),
             ("Bếp từ (a) có thể đun nóng được cả nồi thuỷ tinh và nồi nhôm mỏng không "
              "nhiễm từ.", False,
              "Bếp từ chỉ hoạt động với nồi làm từ vật liệu nhiễm từ (thép, gang, inox "
              "nhiễm từ). Thuỷ tinh không dẫn điện nên không có dòng Foucault; nhôm không "
              "nhiễm từ thì ghép từ rất kém nên hầu như không nhận được năng lượng."),
             ("Ở bộ sạc không dây (b), năng lượng được truyền từ đế sạc sang điện thoại "
              "nhờ hiện tượng cảm ứng điện từ giữa hai cuộn dây.", True,
              "Đế sạc và điện thoại mỗi bên có một cuộn dây; chúng hoạt động như cuộn sơ "
              "cấp và cuộn thứ cấp của một máy biến áp có lõi không khí. Từ thông biến "
              "thiên do cuộn ở đế sinh ra làm xuất hiện suất điện động cảm ứng ở cuộn "
              "trong điện thoại."),
             ("Ở đèn pin lắc tay (c), điện năng được tạo ra nhờ ma sát giữa nam châm và "
              "cuộn dây bên trong đèn.", False,
              "Không phải ma sát. Khi lắc đèn, nam châm trượt qua lại bên trong cuộn dây "
              "làm từ thông qua cuộn dây biến thiên, sinh ra suất điện động cảm ứng. Công "
              "cơ học của tay được chuyển thành điện năng nhờ hiện tượng cảm ứng điện từ."),
         ]),

    dict(stem="Một trạm phát truyền đi công suất điện 400 kW ở điện áp 20 kV; đường dây "
              "tải điện có điện trở tổng cộng 25 Ω; hệ số công suất bằng 1.",
         items=[
             ("Cường độ dòng điện chạy trên đường dây là 25 A.", False,
              "I = P/U = 400·10³/(20·10³) = 20 A. Con số 25 là điện trở của đường dây "
              "chứ không phải cường độ dòng điện."),
             ("Công suất hao phí trên đường dây là 12,5 kW.", False,
              "P_hp = I²·R = 20² × 25 = 400 × 25 = 10 000 W = 10 kW chứ không phải "
              "12,5 kW."),
             ("Hiệu suất của quá trình truyền tải là 97,5 %.", True,
              "H = (P − P_hp)/P = (400 − 10)/400 = 390/400 = 0,975 = 97,5 %."),
             ("Muốn hiệu suất truyền tải đạt 99,375 % thì phải tăng điện áp truyền tải "
              "lên 40 kV.", True,
              "Hiệu suất 99,375 % nghĩa là hao phí chỉ còn 0,625 % của 400 kW, tức "
              "2,5 kW. So với 10 kW ban đầu, hao phí giảm 4 lần, nên U² phải tăng 4 lần, "
              "tức U tăng 2 lần: từ 20 kV lên 40 kV."),
         ]),
]

DE5_P3 = [
    dict(q="Từ đồ thị từ thông ở Câu 8, tính độ lớn suất điện động cảm ứng trong khoảng "
           "thời gian từ 0 đến 2 s (theo V, làm tròn đến hàng phần trăm).",
         fig="t35a",
         ans="0,30",
         sol="Trong khoảng từ 0 đến 2 s, từ thông tăng đều từ 0 lên 0,60 Wb:\n"
             "|e| = |ΔΦ|/Δt = 0,60/2,0 = 0,30 V."),

    dict(q="Một khung dây gồm 100 vòng quay đều trong từ trường đều với tần số 50 Hz. Từ "
           "thông cực đại qua mỗi vòng dây là 2,0·10⁻³ Wb. Lấy π = 3,14. Tính suất điện "
           "động cực đại của khung (theo V, làm tròn đến hàng phần mười).",
         ans="62,8",
         sol="Tốc độ góc: ω = 2πf = 2 × 3,14 × 50 = 314 rad/s.\n"
             "E₀ = N·Φ₀ ₁ vòng·ω = 100 × (2,0·10⁻³) × 314 = 0,20 × 314 = 62,8 V."),

    dict(q="Một khung dây kín phẳng có diện tích 0,020 m² và điện trở 0,40 Ω được đặt "
           "trong từ trường đều có phương vuông góc với mặt phẳng khung. Cảm ứng từ tăng "
           "đều với tốc độ 0,50 T/s. Tính cường độ dòng điện cảm ứng trong khung (theo "
           "10⁻² A, làm tròn đến hàng phần mười).",
         ans="2,5",
         sol="Suất điện động cảm ứng: |e| = S·(ΔB/Δt) = 0,020 × 0,50 = 0,010 V.\n"
             "Cường độ dòng điện: I = |e|/R = 0,010/0,40 = 0,025 A = 2,5·10⁻² A."),

    dict(q="Một máy biến áp lí tưởng hạ điện áp từ 6000 V xuống 220 V. Cuộn thứ cấp có "
           "110 vòng. Tính số vòng dây của cuộn sơ cấp (làm tròn đến hàng đơn vị).",
         ans="3000",
         sol="Từ U₁/U₂ = N₁/N₂ suy ra:\n"
             "N₁ = N₂·U₁/U₂ = 110 × 6000/220 = 110 × 27,27 = 3000 vòng."),

    dict(q="Một sóng điện từ có tần số 90 MHz truyền trong chân không với tốc độ "
           "3·10⁸ m/s. Tính bước sóng của nó (theo m, làm tròn đến hàng phần trăm).",
         ans="3,33",
         sol="Sóng điện từ truyền trong chân không với tốc độ c = 3·10⁸ m/s, và bước "
             "sóng liên hệ với tần số bởi λ = c/f:\n"
             "λ = (3·10⁸)/(90·10⁶) = (3·10⁸)/(9·10⁷) ≈ 3,33 m.\n"
             "Bước sóng vài mét là đặc trưng của dải sóng FM."),

    dict(q="Một khung dây quay đều quanh trục vuông góc với từ trường đều. Tại thời điểm "
           "suất điện động cảm ứng có độ lớn bằng một nửa giá trị cực đại, độ lớn từ "
           "thông qua khung bằng bao nhiêu phần trăm từ thông cực đại? (Làm tròn đến hàng "
           "đơn vị.)",
         ans="87",
         sol="Vì e và Φ lệch pha π/2 nên với Φ = Φ₀cos(ωt) ta có e = E₀sin(ωt), suy ra\n"
             "(e/E₀)² + (Φ/Φ₀)² = 1.\n"
             "Thay |e|/E₀ = 0,5: (Φ/Φ₀)² = 1 − 0,25 = 0,75 ⇒ |Φ|/Φ₀ = √0,75 ≈ 0,866.\n"
             "Vậy độ lớn từ thông bằng khoảng 87 % giá trị cực đại."),
]

DE5 = dict(code="C3-05", so="05", chuong=3,
           title="ĐỀ KIỂM TRA CHƯƠNG III – ĐỀ SỐ 05",
           subtitle="Chương III – Từ trường",
           p1=DE5_P1, p2=DE5_P2, p3=DE5_P3)


DE_CH3 = [DE1, DE2, DE3, DE4, DE5]
