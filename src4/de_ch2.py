# -*- coding: utf-8 -*-
"""NĂM ĐỀ KIỂM TRA CHƯƠNG II – KHÍ LÍ TƯỞNG (Vật lí 12, GDPT 2018).

Cấu trúc mỗi đề giống hệt đề thi tốt nghiệp THPT môn Vật lí: 28 câu / 40 lệnh hỏi /
50 phút (18 câu Phần I + 4 câu đúng–sai Phần II + 6 câu trả lời ngắn Phần III).

Hằng số dùng thống nhất:
    R = 8,31 J/(mol·K) ; k_B = 1,38·10⁻²³ J/K ; N_A = 6,02·10²³ mol⁻¹ ;
    1 atm = 1,013·10⁵ Pa = 76 cmHg ; 0 °C = 273,15 K (làm tròn 273 K khi đề cho phép).
"""

HANG_SO = ("Cho biết: hằng số khí lí tưởng R = 8,31 J/(mol·K); hằng số Boltzmann "
           "k_B = 1,38·10⁻²³ J/K; số Avogadro N_A = 6,02·10²³ mol⁻¹; áp suất khí quyển "
           "chuẩn p₀ = 1,0·10⁵ Pa ≈ 76 cmHg; gia tốc trọng trường g = 10 m/s². Khi đổi "
           "sang thang Kelvin lấy T = t + 273 (trừ khi đề nói rõ dùng 273,15). Mọi chất "
           "khí trong đề đều được coi là khí lí tưởng.")


# ===================================================================================
#                        ĐỀ SỐ 01 – KIẾN THỨC NỀN TẢNG
# ===================================================================================

DE1_P1 = [
    dict(q="Chuyển động Brown của các hạt phấn hoa lơ lửng trong nước là bằng chứng thực "
           "nghiệm cho thấy",
         o=["các phân tử nước chuyển động hỗn loạn không ngừng.",
            "các hạt phấn hoa tự chuyển động được nhờ năng lượng riêng.",
            "giữa các phân tử nước luôn tồn tại lực hút rất mạnh.",
            "nước là một chất lỏng có khối lượng riêng rất nhỏ."],
         a="A",
         sol="Hạt phấn hoa bị các phân tử nước xung quanh va chạm liên tục và không đều "
             "nhau từ mọi phía; hợp lực của các va chạm đó luôn thay đổi ngẫu nhiên khiến "
             "hạt chuyển động zíc zắc không ngừng. Vậy chuyển động Brown là bằng chứng "
             "trực tiếp cho chuyển động nhiệt hỗn loạn của các phân tử."),

    dict(q="Khí lí tưởng là chất khí trong đó",
         o=["các phân tử được coi là chất điểm và chỉ tương tác với nhau khi va chạm.",
            "các phân tử có kích thước đáng kể và luôn hút nhau bằng lực rất mạnh.",
            "các phân tử đứng yên và chỉ chuyển động khi bị đun nóng lên.",
            "các phân tử va chạm với nhau nhưng không va chạm với thành bình."],
         a="A",
         sol="Mô hình khí lí tưởng gồm ba giả thuyết: kích thước phân tử rất nhỏ so với "
             "khoảng cách giữa chúng (coi là chất điểm); các phân tử chuyển động hỗn loạn "
             "không ngừng; chúng chỉ tương tác với nhau khi va chạm và va chạm là đàn hồi. "
             "Va chạm với thành bình chính là nguyên nhân gây ra áp suất nên không thể bỏ "
             "qua."),

    dict(q="Định luật Boyle phát biểu rằng, với một lượng khí xác định ở nhiệt độ không "
           "đổi thì",
         o=["áp suất tỉ lệ nghịch với thể tích, tức pV = hằng số.",
            "áp suất tỉ lệ thuận với thể tích, tức p/V = hằng số.",
            "áp suất tỉ lệ thuận với nhiệt độ, tức p/T = hằng số.",
            "thể tích tỉ lệ thuận với nhiệt độ, tức V/T = hằng số."],
         a="A",
         sol="Định luật Boyle mô tả quá trình đẳng nhiệt: pV = hằng số, tức p tỉ lệ nghịch "
             "với V. Hệ thức p/T = hằng số là quá trình đẳng tích, còn V/T = hằng số là "
             "định luật Charles cho quá trình đẳng áp."),

    dict(q="Định luật Charles áp dụng cho một lượng khí xác định trong quá trình",
         o=["đẳng áp, với hệ thức V/T = hằng số.",
            "đẳng nhiệt, với hệ thức pV = hằng số.",
            "đẳng tích, với hệ thức p/T = hằng số.",
            "bất kì, với hệ thức pV/T = hằng số."],
         a="A",
         sol="Định luật Charles: với một lượng khí xác định giữ ở áp suất không đổi, thể "
             "tích tỉ lệ thuận với nhiệt độ tuyệt đối, V/T = hằng số. Lưu ý T phải tính "
             "theo Kelvin."),

    dict(q="Ở cùng một nhiệt độ, động năng tịnh tiến trung bình của phân tử hai chất khí "
           "khác nhau thì",
         o=["bằng nhau, vì đại lượng đó chỉ phụ thuộc nhiệt độ.",
            "khác nhau, khí có khối lượng mol lớn hơn thì lớn hơn.",
            "khác nhau, khí có khối lượng mol nhỏ hơn thì lớn hơn.",
            "khác nhau, khí có áp suất lớn hơn thì lớn hơn."],
         a="A",
         sol="Động năng tịnh tiến trung bình của một phân tử khí lí tưởng là "
             "W̄ = (3/2)k_B·T, chỉ phụ thuộc nhiệt độ tuyệt đối chứ không phụ thuộc bản "
             "chất chất khí, khối lượng mol hay áp suất. Điều khác nhau giữa hai khí là "
             "TỐC ĐỘ: phân tử nhẹ hơn phải chuyển động nhanh hơn để có cùng động năng "
             "đó."),

    dict(q="Ba thông số trạng thái dùng để mô tả một lượng khí xác định là",
         o=["áp suất, thể tích và nhiệt độ tuyệt đối.",
            "áp suất, khối lượng và nhiệt độ tuyệt đối.",
            "thể tích, khối lượng riêng và nhiệt độ Celsius.",
            "áp suất, thể tích và số phân tử của lượng khí."],
         a="A",
         sol="Trạng thái của một lượng khí xác định được đặc trưng bởi bộ ba (p, V, T). "
             "Khối lượng khí đã được cố định khi nói “một lượng khí xác định” nên không "
             "còn là thông số trạng thái nữa; nhiệt độ phải dùng thang tuyệt đối để các "
             "định luật chất khí có dạng tỉ lệ đơn giản."),

    dict(q="Phương trình trạng thái của một lượng khí lí tưởng xác định có dạng",
         o=["pV/T = hằng số.", "pT/V = hằng số.",
            "VT/p = hằng số.", "p + V + T = hằng số."],
         a="A",
         sol="Kết hợp ba định luật chất khí ta được phương trình trạng thái "
             "p₁V₁/T₁ = p₂V₂/T₂, tức pV/T = hằng số đối với một lượng khí xác định. Đây là "
             "công thức tổng quát, ba định luật chất khí đều là trường hợp riêng của nó."),

    dict(q="Định luật Boyle chỉ được áp dụng khi",
         o=["khối lượng khí không đổi và nhiệt độ của khí không đổi.",
            "khối lượng khí không đổi và áp suất của khí không đổi.",
            "thể tích của khí không đổi trong suốt quá trình biến đổi.",
            "khí được nén thật nhanh để không kịp trao đổi nhiệt."],
         a="A",
         sol="Hai điều kiện bắt buộc: lượng khí không đổi (bình kín, không rò rỉ) và nhiệt "
             "độ không đổi (quá trình đẳng nhiệt). Nén thật nhanh lại làm khí nóng lên, "
             "phá vỡ điều kiện đẳng nhiệt — vì vậy trong thí nghiệm phải nén CHẬM để khí "
             "kịp cân bằng nhiệt với môi trường."),

    dict(q="Hình vẽ biểu diễn hai trạng thái (1) và (2) của một lượng khí lí tưởng nằm "
           "trên cùng một đường đẳng nhiệt. Giá trị của tích pV ở hai trạng thái đó lần "
           "lượt là",
         fig="t21a",
         o=["6 atm·lít và 6 atm·lít.", "3 atm·lít và 1 atm·lít.",
            "2 atm·lít và 6 atm·lít.", "6 atm·lít và 3 atm·lít."],
         a="A",
         sol="Từ đồ thị: trạng thái (1) có p₁ = 3 atm, V₁ = 2 lít nên p₁V₁ = 6 atm·lít; "
             "trạng thái (2) có p₂ = 1 atm, V₂ = 6 lít nên p₂V₂ = 6 atm·lít. Hai giá trị "
             "bằng nhau đúng như định luật Boyle đòi hỏi vì hai trạng thái cùng nằm trên "
             "một đường đẳng nhiệt."),

    dict(q="Trong hệ toạ độ (p, V), đường đẳng nhiệt của một lượng khí lí tưởng xác định là",
         o=["một nhánh hypebol.", "một đường thẳng đi qua gốc toạ độ.",
            "một đường thẳng song song với trục hoành.", "một đường parabol."],
         a="A",
         sol="Từ pV = hằng số suy ra p = hằng số/V, đồ thị là một nhánh hypebol (nhánh nằm "
             "trong góc phần tư thứ nhất vì p và V đều dương). Đường thẳng song song trục "
             "hoành trong hệ (p, V) ứng với quá trình đẳng áp."),

    dict(q="Hình vẽ là đồ thị thể tích theo nhiệt độ tuyệt đối của một lượng khí lí tưởng "
           "trong quá trình đẳng áp. Đặc điểm quan trọng của đồ thị này là",
         fig="t21c",
         o=["đường kéo dài của nó đi qua gốc toạ độ.",
            "nó là một nhánh hypebol nhận hai trục làm tiệm cận.",
            "nó cắt trục tung tại một giá trị dương khác không.",
            "nó song song với trục hoành trong suốt quá trình."],
         a="A",
         sol="Định luật Charles cho V = (hằng số)·T, tức V tỉ lệ THUẬN với nhiệt độ tuyệt "
             "đối. Đồ thị V–T vì thế là một đường thẳng mà nếu kéo dài sẽ đi qua gốc toạ "
             "độ (T = 0 K thì V = 0). Đây chính là cơ sở thực nghiệm để xác định nhiệt độ "
             "không tuyệt đối."),

    dict(q="Không nên đặt bình chứa khí nén gần nguồn nhiệt vì",
         o=["nhiệt độ tăng làm áp suất khí trong bình tăng, bình có thể bị nổ.",
            "nhiệt độ tăng làm thể tích của bình giảm nên khí bị nén thêm.",
            "nhiệt độ tăng làm khối lượng khí trong bình tăng lên nhanh chóng.",
            "nhiệt độ tăng làm các phân tử khí dính vào nhau và ngưng tụ lại."],
         a="A",
         sol="Bình chứa khí nén có thể tích gần như không đổi nên khí trong bình biến đổi "
             "đẳng tích: p/T = hằng số. Khi T tăng thì p tăng tỉ lệ thuận, có thể vượt quá "
             "giới hạn chịu đựng của vỏ bình và gây nổ. Khối lượng khí trong bình kín "
             "không thay đổi khi đun nóng."),

    dict(q="Nén đẳng nhiệt một lượng khí lí tưởng từ thể tích 6,0 lít ở áp suất 1,0 atm "
           "xuống còn 2,0 lít. Áp suất của khí lúc này là",
         o=["3,0 atm.", "0,33 atm.", "2,0 atm.", "12 atm."],
         a="A",
         sol="Quá trình đẳng nhiệt nên p₁V₁ = p₂V₂ ⇒ p₂ = p₁V₁/V₂ = 1,0 × 6,0/2,0 "
             "= 3,0 atm. Thể tích giảm 3 lần thì áp suất tăng 3 lần."),

    dict(q="Một lượng khí lí tưởng có thể tích 3,0 lít ở nhiệt độ 300 K. Đun nóng đẳng áp "
           "lượng khí đó tới 360 K thì thể tích của nó bằng",
         fig="t21c",
         o=["3,6 lít.", "2,5 lít.", "3,3 lít.", "4,2 lít."],
         a="A",
         sol="Đẳng áp nên V₁/T₁ = V₂/T₂ ⇒ V₂ = V₁·T₂/T₁ = 3,0 × 360/300 = 3,6 lít. Nhiệt "
             "độ tuyệt đối tăng 20 % thì thể tích cũng tăng 20 %."),

    dict(q="Một bình kín thể tích không đổi chứa khí ở 27 °C và áp suất 2,0 atm. Đun nóng "
           "bình tới 127 °C thì áp suất của khí xấp xỉ",
         o=["2,67 atm.", "9,41 atm.", "1,50 atm.", "2,00 atm."],
         a="A",
         sol="Đổi sang thang Kelvin: T₁ = 300 K, T₂ = 400 K. Quá trình đẳng tích nên "
             "p₁/T₁ = p₂/T₂ ⇒ p₂ = 2,0 × 400/300 ≈ 2,67 atm.\n"
             "Sai lầm điển hình là lấy tỉ số nhiệt độ Celsius 127/27 ≈ 4,7 và ra 9,41 atm "
             "— luôn phải đổi sang Kelvin trước."),

    dict(q="Một lượng khí lí tưởng ở trạng thái p₁ = 1,0 atm, V₁ = 5,0 lít, T₁ = 300 K "
           "được đưa tới trạng thái p₂ = 2,0 atm, T₂ = 360 K. Thể tích V₂ bằng",
         o=["3,0 lít.", "2,1 lít.", "4,2 lít.", "6,0 lít."],
         a="A",
         sol="Áp dụng phương trình trạng thái p₁V₁/T₁ = p₂V₂/T₂:\n"
             "V₂ = V₁ × (p₁/p₂) × (T₂/T₁) = 5,0 × (1,0/2,0) × (360/300) = 5,0 × 0,50 × "
             "1,20 = 3,0 lít.\n"
             "Áp suất tăng 2 lần làm thể tích giảm 2 lần, nhiệt độ tăng 1,2 lần làm thể "
             "tích tăng 1,2 lần; kết quả là 5,0 × 0,6 = 3,0 lít."),

    dict(q="Thể tích của 1,0 mol khí lí tưởng ở 0 °C và áp suất 1,0·10⁵ Pa xấp xỉ",
         o=["22,7 lít.", "24,9 lít.", "2,27 lít.", "11,4 lít."],
         a="A",
         sol="Từ pV = nRT ⇒ V = nRT/p = 1,0 × 8,31 × 273/1,0·10⁵ = 2268,6/10⁵ "
             "= 2,269·10⁻² m³ ≈ 22,7 lít.\n"
             "Đây chính là thể tích mol ở điều kiện chuẩn theo định nghĩa hiện hành "
             "(0 °C, 1 bar)."),

    dict(q="Khi đun nóng đẳng tích một lượng khí lí tưởng xác định, đại lượng nào sau đây "
           "KHÔNG thay đổi?",
         o=["Khối lượng riêng của khí.",
            "Áp suất của khí lên thành bình.",
            "Động năng trung bình của các phân tử khí.",
            "Số va chạm của các phân tử lên thành bình trong mỗi giây."],
         a="A",
         sol="Đẳng tích nghĩa là V không đổi; lượng khí xác định nên m cũng không đổi, do "
             "đó khối lượng riêng ρ = m/V không đổi. Khi nhiệt độ tăng, các phân tử chuyển "
             "động nhanh hơn nên động năng trung bình tăng, số va chạm mỗi giây và cường "
             "độ mỗi va chạm đều tăng, dẫn tới áp suất tăng."),
]

DE1_P2 = [
    dict(stem="Hình vẽ biểu diễn quá trình biến đổi đẳng nhiệt của một lượng khí lí tưởng "
              "xác định từ trạng thái (1) sang trạng thái (2).",
         fig="t21a",
         items=[
             ("Nhiệt độ của khí ở trạng thái (1) bằng nhiệt độ ở trạng thái (2).", True,
              "Hai trạng thái nằm trên cùng một đường đẳng nhiệt, theo định nghĩa đó là "
              "đường nối các trạng thái có cùng nhiệt độ."),
             ("Tích pV của khí ở cả hai trạng thái đều bằng 6 atm·lít.", True,
              "p₁V₁ = 3 × 2 = 6 atm·lít; p₂V₂ = 1 × 6 = 6 atm·lít. Sự bằng nhau này chính "
              "là nội dung định luật Boyle."),
             ("Khi thể tích của khí tăng gấp 3 lần thì áp suất của nó cũng tăng gấp 3 lần.",
              False,
              "Ở nhiệt độ không đổi, p tỉ lệ NGHỊCH với V. Từ (1) sang (2) thể tích tăng "
              "3 lần (2 → 6 lít) thì áp suất giảm 3 lần (3 → 1 atm), đúng như hình vẽ."),
             ("Khối lượng riêng của khí ở trạng thái (2) lớn hơn ở trạng thái (1).", False,
              "Lượng khí không đổi nên khối lượng m giữ nguyên; thể tích tăng từ 2 lít lên "
              "6 lít nên ρ = m/V GIẢM 3 lần. Khí dãn ra thì loãng đi, không thể đặc hơn."),
         ]),

    dict(stem="Hình vẽ là sơ đồ bộ thí nghiệm khảo sát định luật Boyle. Cột khí bị giam "
              "trong xi lanh có chiều dài ℓ và tiết diện S không đổi; áp kế đo áp suất p "
              "của khí; thí nghiệm được thực hiện ở nhiệt độ phòng ổn định.",
         fig="t21b",
         items=[
             ("Vì tiết diện S không đổi nên có thể thay thể tích V bằng chiều dài ℓ, tức "
              "kiểm tra hệ thức p·ℓ = hằng số.", True,
              "V = S·ℓ với S là hằng số, nên pV = p·S·ℓ = hằng số kéo theo p·ℓ = hằng số. "
              "Nhờ đó chỉ cần một chiếc thước là đo được “thể tích”, đây là mẹo thực "
              "nghiệm rất thông dụng."),
             ("Có thể nén thật nhanh và thật mạnh mà kết quả thí nghiệm vẫn chính xác, vì "
              "nhiệt độ phòng không đổi.", False,
              "Nhiệt độ PHÒNG không đổi không đồng nghĩa với nhiệt độ KHÍ trong xi lanh "
              "không đổi. Nén nhanh làm khí nhận công mà chưa kịp truyền nhiệt ra ngoài "
              "nên nóng lên, quá trình không còn đẳng nhiệt và tích p·ℓ sẽ lớn hơn giá trị "
              "đúng. Phải nén chậm để khí kịp cân bằng nhiệt với môi trường."),
             ("Đồ thị biểu diễn p theo 1/ℓ là một đường thẳng đi qua gốc toạ độ.", True,
              "Từ p·ℓ = C suy ra p = C·(1/ℓ), tức p tỉ lệ thuận với 1/ℓ. Việc “tuyến tính "
              "hoá” như vậy giúp kiểm tra định luật dễ hơn nhiều so với vẽ nhánh hypebol."),
             ("Nếu xi lanh bị hở làm khí thoát dần ra ngoài thì tích p·ℓ đo được sẽ tăng "
              "dần.", False,
              "Khí thoát ra làm lượng khí giảm; ở cùng nhiệt độ, tích pV tỉ lệ thuận với "
              "số mol khí (pV = nRT) nên p·ℓ sẽ GIẢM dần. Dấu hiệu này giúp phát hiện xi "
              "lanh bị hở trong khi làm thí nghiệm."),
         ]),

    dict(stem="Xét các phát biểu về mô hình động học phân tử chất khí.",
         items=[
             ("Các phân tử khí chuyển động hỗn loạn không ngừng, va chạm với nhau và va "
              "chạm với thành bình.", True,
              "Đây là nội dung cơ bản của mô hình động học phân tử. Chuyển động này không "
              "bao giờ dừng lại, chỉ chậm đi khi nhiệt độ hạ thấp."),
             ("Áp suất mà chất khí tác dụng lên thành bình là do các phân tử khí va chạm "
              "vào thành bình gây ra.", True,
              "Mỗi va chạm truyền cho thành bình một xung lượng; số va chạm trong một giây "
              "lên mỗi đơn vị diện tích rất lớn nên tổng hợp lại cho một lực gần như liên "
              "tục và đều đặn, đó chính là áp suất."),
             ("Ở cùng một nhiệt độ, mọi phân tử khí trong bình đều chuyển động với cùng "
              "một tốc độ.", False,
              "Tốc độ các phân tử phân bố trong một dải rất rộng, có phân tử rất chậm và "
              "có phân tử rất nhanh; chỉ có tốc độ TRUNG BÌNH (và động năng trung bình) "
              "mới được xác định bởi nhiệt độ."),
             ("Kích thước của mỗi phân tử khí lớn hơn nhiều so với khoảng cách trung bình "
              "giữa các phân tử.", False,
              "Hoàn toàn ngược lại: ở điều kiện thường, khoảng cách trung bình giữa các "
              "phân tử khí lớn hơn kích thước phân tử hàng chục lần. Chính điều đó cho "
              "phép coi phân tử khí là chất điểm và bỏ qua lực tương tác giữa chúng."),
         ]),

    dict(stem="Một lượng khí lí tưởng xác định ở nhiệt độ 27 °C, áp suất 1,0·10⁵ Pa và có "
              "thể tích 4,0 lít.",
         items=[
             ("Nhiệt độ tuyệt đối của lượng khí đó là 273 K.", False,
              "T = t + 273 = 27 + 273 = 300 K. Giá trị 273 K ứng với 0 °C chứ không phải "
              "27 °C."),
             ("Nếu nén đẳng nhiệt lượng khí đó tới thể tích 1,0 lít thì áp suất của nó trở "
              "thành 4,0·10⁵ Pa.", True,
              "p₂ = p₁V₁/V₂ = 1,0·10⁵ × 4,0/1,0 = 4,0·10⁵ Pa. Thể tích giảm 4 lần thì áp "
              "suất tăng 4 lần."),
             ("Nếu đun nóng đẳng tích lượng khí đó tới 327 °C thì áp suất của nó trở thành "
              "1,2·10⁵ Pa.", False,
              "T₂ = 327 + 273 = 600 K, gấp đôi T₁ = 300 K. Đẳng tích nên áp suất cũng gấp "
              "đôi: p₂ = 2,0·10⁵ Pa chứ không phải 1,2·10⁵ Pa."),
             ("Nếu đun nóng đẳng áp lượng khí đó tới 87 °C thì thể tích của nó trở thành "
              "4,8 lít.", True,
              "T₂ = 87 + 273 = 360 K ⇒ V₂ = V₁·T₂/T₁ = 4,0 × 360/300 = 4,8 lít."),
         ]),
]

DE1_P3 = [
    dict(q="Nén đẳng nhiệt một lượng khí lí tưởng từ thể tích 8,0 lít ở áp suất 1,5 atm "
           "xuống còn 3,0 lít. Tính áp suất của khí sau khi nén (theo atm, làm tròn đến "
           "hàng phần mười).",
         ans="4,0",
         sol="Định luật Boyle: p₁V₁ = p₂V₂\n"
             "p₂ = 1,5 × 8,0/3,0 = 12/3,0 = 4,0 atm."),

    dict(q="Một lượng khí lí tưởng ở 20 °C có thể tích 2,5 lít. Đun nóng đẳng áp lượng khí "
           "đó tới 80 °C. Tính thể tích của khí lúc đó (theo lít, làm tròn đến hàng phần "
           "trăm).",
         ans="3,01",
         sol="Đổi sang thang Kelvin: T₁ = 293 K; T₂ = 353 K.\n"
             "Định luật Charles: V₂ = V₁·T₂/T₁ = 2,5 × 353/293 ≈ 3,01 lít.\n"
             "Lưu ý nếu dùng nhầm tỉ số nhiệt độ Celsius 80/20 = 4 sẽ ra 10 lít, sai hoàn "
             "toàn."),

    dict(q="Một bình kín thể tích không đổi chứa khí lí tưởng ở 27 °C, áp suất 2,0·10⁵ Pa. "
           "Đun nóng bình tới 177 °C. Tính áp suất của khí lúc đó (theo 10⁵ Pa, làm tròn "
           "đến hàng phần mười).",
         ans="3,0",
         sol="T₁ = 300 K; T₂ = 177 + 273 = 450 K.\n"
             "Quá trình đẳng tích: p₂ = p₁·T₂/T₁ = 2,0·10⁵ × 450/300 = 3,0·10⁵ Pa."),

    dict(q="Một lượng khí lí tưởng có p₁ = 1,0 atm, V₁ = 6,0 lít, T₁ = 300 K được biến đổi "
           "tới trạng thái có p₂ = 2,5 atm và T₂ = 450 K. Tính thể tích V₂ (theo lít, làm "
           "tròn đến hàng phần mười).",
         ans="3,6",
         sol="Phương trình trạng thái: p₁V₁/T₁ = p₂V₂/T₂\n"
             "V₂ = V₁ × (p₁/p₂) × (T₂/T₁) = 6,0 × (1,0/2,5) × (450/300)\n"
             "  = 6,0 × 0,40 × 1,50 = 3,6 lít."),

    dict(q="Tính số mol khí lí tưởng chứa trong một bình kín dung tích 10 lít ở 27 °C, áp "
           "suất 2,49·10⁵ Pa. (Kết quả làm tròn đến hàng phần mười.)",
         ans="1,0",
         sol="Phương trình Clapeyron – Mendeleev: pV = nRT\n"
             "n = pV/(RT) = (2,49·10⁵ × 10·10⁻³)/(8,31 × 300) = 2490/2493 ≈ 1,0 mol.\n"
             "Chú ý phải đổi thể tích ra mét khối: 10 lít = 10·10⁻³ m³."),

    dict(q="Một bóng thám không chứa 5,0 m³ khí ở mặt đất, nơi có áp suất 1,0·10⁵ Pa và "
           "nhiệt độ 300 K. Khi bóng lên tới độ cao mà áp suất chỉ còn 0,50·10⁵ Pa và "
           "nhiệt độ là 240 K, thể tích khí trong bóng là bao nhiêu (theo m³, làm tròn đến "
           "hàng phần mười)?",
         ans="8,0",
         sol="Phương trình trạng thái: V₂ = V₁ × (p₁/p₂) × (T₂/T₁)\n"
             "V₂ = 5,0 × (1,0/0,50) × (240/300) = 5,0 × 2,0 × 0,80 = 8,0 m³.\n"
             "Áp suất giảm một nửa làm thể tích tăng gấp đôi, nhiệt độ giảm còn 0,8 lần "
             "kéo thể tích xuống 0,8 lần; kết quả là tăng 1,6 lần."),
]

DE1 = dict(code="C2-01", so="01", chuong=2,
           title="ĐỀ KIỂM TRA CHƯƠNG II – ĐỀ SỐ 01",
           subtitle="Chương II – Khí lí tưởng",
           p1=DE1_P1, p2=DE1_P2, p3=DE1_P3)


# ===================================================================================
#              ĐỀ SỐ 02 – ĐẲNG TÍCH, ĐẲNG ÁP VÀ ĐỌC ĐỒ THỊ
# ===================================================================================

DE2_P1 = [
    dict(q="Với một lượng khí lí tưởng xác định giữ ở thể tích không đổi, hệ thức nào sau "
           "đây là đúng?",
         o=["p/T = hằng số.", "pT = hằng số.",
            "V/T = hằng số.", "pV = hằng số."],
         a="A",
         sol="Quá trình đẳng tích tuân theo định luật Gay-Lussac: áp suất tỉ lệ thuận với "
             "nhiệt độ tuyệt đối, p/T = hằng số. Hệ thức pV = hằng số dành cho quá trình "
             "đẳng nhiệt, còn V/T = hằng số dành cho quá trình đẳng áp."),

    dict(q="Giải thích theo mô hình động học phân tử, khi nén một lượng khí ở nhiệt độ "
           "không đổi thì áp suất tăng lên là vì",
         o=["mật độ phân tử tăng nên số va chạm lên mỗi đơn vị diện tích thành bình trong "
            "một giây tăng.",
            "tốc độ trung bình của các phân tử khí tăng lên nên mỗi va chạm mạnh hơn.",
            "khối lượng của mỗi phân tử khí tăng lên khi thể tích của khối khí giảm.",
            "lực hút giữa các phân tử khí tăng lên và kéo chúng về phía thành bình."],
         a="A",
         sol="Nhiệt độ không đổi nên tốc độ trung bình (và động năng trung bình) của phân "
             "tử không đổi, tức mỗi va chạm mạnh như cũ. Điều thay đổi là mật độ: cùng số "
             "phân tử trong thể tích nhỏ hơn nên tần suất va chạm lên thành bình tăng, dẫn "
             "tới áp suất tăng."),

    dict(q="Nhiệt độ 27 °C tương ứng với nhiệt độ tuyệt đối bằng",
         o=["300 K.", "246 K.", "273 K.", "327 K."],
         a="A",
         sol="T = t + 273 = 27 + 273 = 300 K. Đây là một giá trị rất hay gặp trong các bài "
             "toán chất khí, nên nhớ sẵn: 27 °C = 300 K, 127 °C = 400 K, "
             "−73 °C = 200 K."),

    dict(q="Đường đẳng tích của một lượng khí lí tưởng xác định, khi vẽ trong hệ toạ "
           "độ (p, T), có dạng",
         o=["một đường thẳng mà đường kéo dài của nó đi qua gốc toạ độ.",
            "một nhánh hypebol nhận hai trục toạ độ làm tiệm cận.",
            "một đường thẳng song song với trục hoành OT.",
            "một đường thẳng song song với trục tung Op."],
         a="A",
         sol="Từ p/T = hằng số suy ra p = (hằng số)·T, tức p tỉ lệ thuận với T. Đồ thị là "
             "đường thẳng qua gốc toạ độ. Trong hệ (p, T), đường song song với trục OT lại "
             "là đường đẳng áp."),

    dict(q="Phương trình Clapeyron – Mendeleev cho một lượng khí lí tưởng có dạng",
         o=["pV = nRT.", "pV = nR/T.", "p/V = nRT.", "pVT = nR."],
         a="A",
         sol="pV = nRT, trong đó n là số mol, R = 8,31 J/(mol·K) là hằng số khí lí tưởng "
             "và T là nhiệt độ TUYỆT ĐỐI (K). Không được thay T bằng nhiệt độ Celsius t. "
             "Có thể nhớ nhanh: với n cố định, pV/T = nR = hằng số, đúng bằng phương "
             "trình trạng thái đã học."),

    dict(q="Theo mô hình động học phân tử, khi nhiệt độ tuyệt đối của một lượng khí lí "
           "tưởng tăng lên thì",
         o=["động năng tịnh tiến trung bình của các phân tử khí tăng lên.",
            "khối lượng của mỗi phân tử khí trong bình tăng lên.",
            "số phân tử khí chứa trong bình kín tăng lên.",
            "kích thước của mỗi phân tử khí tăng lên."],
         a="A",
         sol="Nhiệt độ là số đo mức độ chuyển động nhiệt của các phân tử: "
             "W̄ = (3/2)k_B·T, nên T tăng thì động năng tịnh tiến trung bình tăng theo, "
             "tỉ lệ thuận. Khối lượng, kích thước phân tử và số phân tử trong bình kín "
             "đều là những đại lượng không đổi khi đun nóng. Giá trị các hằng số "
             "R = 8,31 J/(mol·K) và k_B = 1,38·10⁻²³ J/K liên hệ với nhau qua "
             "R = k_B·N_A."),

    dict(q="Hình vẽ là đồ thị áp suất theo nhiệt độ Celsius của một lượng khí lí tưởng "
           "đựng trong bình kín. Việc đường kéo dài của đồ thị cắt trục hoành tại −273 °C "
           "cho thấy",
         fig="t22a",
         o=["ở −273 °C áp suất khí lí tưởng bằng 0; đó là cơ sở của thang nhiệt độ Kelvin.",
            "ở −273 °C mọi chất khí đều hoá lỏng nên không còn gây ra áp suất nữa.",
            "áp suất của chất khí có thể nhận cả những giá trị âm khi nhiệt độ rất thấp.",
            "chất khí trong bình đã bị rò rỉ hết ra ngoài khi nhiệt độ xuống rất thấp."],
         a="A",
         sol="Ngoại suy đường đẳng tích của khí lí tưởng về phía nhiệt độ thấp thì áp suất "
             "tiến tới 0 tại −273,15 °C. Nhiệt độ này được chọn làm gốc của thang Kelvin "
             "(0 K), nhờ đó p tỉ lệ THUẬN với T tuyệt đối. Đây chỉ là phép ngoại suy lí "
             "thuyết vì khí thực đã hoá lỏng từ trước khi tới nhiệt độ đó."),

    dict(q="Hình vẽ là ba đường đẳng nhiệt của cùng một lượng khí lí tưởng ứng với ba "
           "nhiệt độ T₁, T₂, T₃. Thứ tự đúng là",
         fig="t22c",
         o=["T₃ > T₂ > T₁.", "T₁ > T₂ > T₃.", "T₂ > T₃ > T₁.", "T₁ = T₂ = T₃."],
         a="A",
         sol="Với cùng một thể tích V, phương trình pV = nRT cho p tỉ lệ thuận với T. Trên "
             "hình, tại mọi giá trị V thì đường T₃ nằm cao nhất (p lớn nhất), rồi tới T₂, "
             "thấp nhất là T₁. Vậy T₃ > T₂ > T₁: đường đẳng nhiệt càng xa gốc toạ độ thì "
             "ứng với nhiệt độ càng cao."),

    dict(q="Lốp xe ô tô dễ bị nổ hơn khi chạy đường dài giữa trưa nắng. Nguyên nhân chính là",
         o=["nhiệt độ khí trong lốp tăng trong khi thể tích gần như không đổi nên áp suất "
            "tăng.",
            "khối lượng không khí trong lốp tăng lên do bị nắng chiếu vào liên tục.",
            "áp suất khí quyển bên ngoài giảm mạnh khi trời nắng nên lốp bị phồng ra.",
            "cao su của lốp bị nóng nên co lại, làm thể tích khí trong lốp giảm mạnh."],
         a="A",
         sol="Ma sát với mặt đường và nắng nóng làm nhiệt độ khí trong lốp tăng đáng kể. "
             "Thể tích lốp gần như không đổi nên khí biến đổi đẳng tích: p tỉ lệ thuận với "
             "T tuyệt đối, áp suất tăng có thể vượt sức chịu của lốp. Vì vậy không nên bơm "
             "lốp quá căng trước chuyến đi xa vào ngày nắng."),

    dict(q="Trong quá trình nén một lượng khí, nếu có một phần khí bị rò ra ngoài (nhiệt "
           "độ giữ không đổi) thì tích pV đo được sẽ",
         o=["giảm dần trong quá trình nén.",
            "tăng dần trong quá trình nén.",
            "vẫn giữ nguyên vì nhiệt độ không đổi.",
            "lúc tăng lúc giảm tuỳ theo tốc độ nén."],
         a="A",
         sol="Ở nhiệt độ không đổi, pV = nRT tỉ lệ thuận với số mol n. Khí rò ra ngoài "
             "khiến n giảm nên pV giảm dần. Định luật Boyle chỉ đúng cho một lượng khí "
             "KHÔNG ĐỔI — đây là điều kiện áp dụng hay bị bỏ quên nhất."),

    dict(q="Hình vẽ là bộ thí nghiệm khảo sát định luật Charles: cột khí bị giam trong ống "
           "nghiệm bởi một giọt thuỷ ngân, ống đặt thẳng đứng, đầu hở lên trên. Trong suốt "
           "thí nghiệm, áp suất của cột khí bị giam",
         fig="t22b",
         o=["không đổi, bằng áp suất khí quyển cộng với áp suất do trọng lượng giọt thuỷ "
            "ngân.",
            "không đổi và đúng bằng áp suất khí quyển tại nơi làm thí nghiệm.",
            "tăng dần khi cột khí dãn ra đẩy giọt thuỷ ngân lên cao hơn.",
            "giảm dần vì thể tích của cột khí trong ống tăng lên khi bị đun nóng."],
         a="A",
         sol="Giọt thuỷ ngân luôn cân bằng nên áp suất cột khí bằng áp suất khí quyển cộng "
             "với áp suất do trọng lượng giọt thuỷ ngân đè xuống: p = p₀ + ρgh. Cả hai số "
             "hạng đều không đổi (giọt thuỷ ngân không đổi khi trượt dọc ống tiết diện "
             "đều) nên p là hằng số — đó chính là điều kiện đẳng áp cần thiết để kiểm "
             "chứng định luật Charles."),

    dict(q="Nén đẳng nhiệt một lượng khí lí tưởng. Phát biểu nào sau đây là SAI?",
         o=["Động năng trung bình của các phân tử khí tăng lên.",
            "Mật độ phân tử khí trong bình tăng lên.",
            "Áp suất của khí lên thành bình tăng lên.",
            "Khối lượng riêng của khối khí tăng lên."],
         a="A",
         sol="Động năng tịnh tiến trung bình của phân tử chỉ phụ thuộc nhiệt độ "
             "(W̄ = 3k_BT/2). Quá trình đẳng nhiệt có T không đổi nên động năng trung bình "
             "KHÔNG đổi — phát biểu này sai. Ba đại lượng còn lại đều tăng vì thể tích "
             "giảm."),

    dict(q="Một lượng khí trong bình kín có áp suất 1,5·10⁵ Pa ở 27 °C. Phải đun nóng khí "
           "tới nhiệt độ nào để áp suất của nó là 2,0·10⁵ Pa?",
         o=["127 °C.", "36 °C.", "400 °C.", "177 °C."],
         a="A",
         sol="Đẳng tích: T₂ = T₁·p₂/p₁ = 300 × (2,0/1,5) = 400 K.\n"
             "Đổi lại thang Celsius: t₂ = 400 − 273 = 127 °C.\n"
             "Bẫy thường gặp: lấy 27 × 2,0/1,5 = 36 °C, tức tính tỉ lệ trên thang Celsius."),

    dict(q="Vẫn với lượng khí trong đồ thị đẳng tích ở Câu 7 (ở 0 °C áp suất là 1,00 atm). "
           "Ở 150 °C, áp suất của khí xấp xỉ",
         fig="t22a",
         o=["1,55 atm.", "1,15 atm.", "2,00 atm.", "1,00 atm."],
         a="A",
         sol="Đẳng tích nên p tỉ lệ thuận với nhiệt độ tuyệt đối:\n"
             "p₂ = p₁·T₂/T₁ = 1,00 × (150 + 273,15)/273,15 = 1,00 × 423,15/273,15 "
             "≈ 1,55 atm."),

    dict(q="Một xi lanh chứa 3,0 lít khí lí tưởng ở áp suất 2,0 atm và nhiệt độ 300 K. Nén "
           "khí xuống còn 1,0 lít đồng thời đun nóng tới 400 K. Áp suất của khí lúc này là",
         o=["8,0 atm.", "4,5 atm.", "6,0 atm.", "2,7 atm."],
         a="A",
         sol="Phương trình trạng thái: p₂ = p₁ × (V₁/V₂) × (T₂/T₁)\n"
             "p₂ = 2,0 × (3,0/1,0) × (400/300) = 2,0 × 3,0 × 1,333 = 8,0 atm.\n"
             "Thể tích giảm 3 lần làm p tăng 3 lần; nhiệt độ tăng 4/3 lần làm p tăng thêm "
             "4/3 lần."),

    dict(q="Một bình kín dung tích 8,31 lít chứa 4,0 g khí helium (khối lượng mol 4,0 "
           "g/mol) ở 300 K. Áp suất khí trong bình là",
         o=["3,0·10⁵ Pa.", "3,0·10² Pa.", "1,0·10⁵ Pa.", "2,5·10⁵ Pa."],
         a="A",
         sol="Số mol: n = m/M = 4,0/4,0 = 1,0 mol. Thể tích: V = 8,31 lít "
             "= 8,31·10⁻³ m³.\n"
             "p = nRT/V = (1,0 × 8,31 × 300)/(8,31·10⁻³) = 2493/(8,31·10⁻³) "
             "= 3,0·10⁵ Pa."),

    dict(q="Trên ba đường đẳng nhiệt trong hình vẽ, tại cùng một giá trị thể tích V₀ ta "
           "đọc được ba giá trị áp suất p₁, p₂, p₃. Khi đó",
         fig="t22c",
         o=["T₁ : T₂ : T₃ = p₁ : p₂ : p₃.",
            "T₁ : T₂ : T₃ = p₃ : p₂ : p₁.",
            "T₁ : T₂ : T₃ = p₁² : p₂² : p₃².",
            "không thể so sánh vì chưa biết số mol khí."],
         a="A",
         sol="Vẫn cùng một lượng khí nên pV = nRT với n không đổi. Tại cùng V = V₀ ta có "
             "p = (nR/V₀)·T, tức p tỉ lệ THUẬN với T. Do đó tỉ số các áp suất đọc được "
             "trên cùng một đường thẳng đứng chính bằng tỉ số các nhiệt độ."),

    dict(q="Một bình 20 lít chứa khí ở áp suất 5,0·10⁵ Pa và 300 K. Mở van cho khí thoát "
           "ra tới khi áp suất trong bình còn 2,0·10⁵ Pa, nhiệt độ vẫn giữ 300 K. Phần "
           "trăm khối lượng khí đã thoát ra khỏi bình là",
         o=["60 %.", "40 %.", "30 %.", "250 %."],
         a="A",
         sol="Thể tích bình và nhiệt độ không đổi nên từ pV = nRT suy ra n tỉ lệ thuận với "
             "p, mà khối lượng khí tỉ lệ thuận với n.\n"
             "Tỉ lệ khối lượng còn lại: 2,0/5,0 = 0,40 = 40 %.\n"
             "Vậy phần đã thoát ra là 100 % − 40 % = 60 %."),
]

DE2_P2 = [
    dict(stem="Hình vẽ là đồ thị áp suất theo nhiệt độ Celsius của một lượng khí lí tưởng "
              "đựng trong bình kín có thể tích không đổi; ở 0 °C áp suất của khí là "
              "1,00 atm.",
         fig="t22a",
         items=[
             ("Đồ thị là một đoạn thẳng nên áp suất p tỉ lệ thuận với nhiệt độ Celsius t.",
              False,
              "Đồ thị đúng là đường thẳng, nhưng nó KHÔNG đi qua gốc toạ độ của hệ (p, t) "
              "— nó cắt trục hoành tại −273 °C. Quan hệ ở đây là hàm bậc nhất "
              "p = p₀(1 + t/273) chứ không phải tỉ lệ thuận. Chỉ khi dùng nhiệt độ tuyệt "
              "đối T thì p mới TỈ LỆ THUẬN với T."),
             ("Đường kéo dài của đồ thị cắt trục hoành tại −273 °C.", True,
              "Đây là kết quả ngoại suy: p = 0 khi T = 0 K, tức t = −273 °C. Đó là cách "
              "xác định nhiệt độ không tuyệt đối bằng thực nghiệm với nhiệt kế khí."),
             ("Ở 273 °C, áp suất của khí là 2,00 atm.", True,
              "T₂ = 273 + 273,15 = 546,15 K; T₁ = 273,15 K.\n"
              "p₂ = 1,00 × 546,15/273,15 ≈ 2,00 atm. Nhiệt độ tuyệt đối tăng gấp đôi nên "
              "áp suất tăng gấp đôi."),
             ("Nếu tăng thể tích bình lên gấp đôi (vẫn lượng khí đó) thì đồ thị mới nằm "
              "phía trên đồ thị đã cho.", False,
              "Ở cùng một nhiệt độ, p = nRT/V nên thể tích tăng gấp đôi làm áp suất giảm "
              "một nửa. Đường đẳng tích mới vẫn là đường thẳng qua −273 °C nhưng có độ dốc "
              "nhỏ hơn, tức nằm phía DƯỚI đồ thị cũ."),
         ]),

    dict(stem="Hình vẽ là bộ thí nghiệm khảo sát mối liên hệ giữa thể tích và nhiệt độ của "
              "một lượng khí (định luật Charles). Cột khí bị giam trong ống nghiệm bởi một "
              "giọt thuỷ ngân; ống đặt thẳng đứng, đầu hở lên trên; nước trong cốc được "
              "đun nóng từ từ.",
         fig="t22b",
         items=[
             ("Áp suất của cột khí bị giam trong ống không đổi trong suốt thí nghiệm.",
              True,
              "Giọt thuỷ ngân luôn ở trạng thái cân bằng nên p_khí = p₀ + (trọng lượng "
              "giọt thuỷ ngân)/(tiết diện ống). Cả hai số hạng đều là hằng số, nên đây "
              "đúng là một quá trình đẳng áp."),
             ("Khi nhiệt độ tăng, giọt thuỷ ngân dịch chuyển lên phía trên.", True,
              "Đẳng áp nên V tỉ lệ thuận với T: nhiệt độ tăng làm cột khí dài ra, đẩy giọt "
              "thuỷ ngân đi lên. Việc đo chiều dài cột khí ℓ chính là cách đo thể tích "
              "trong thí nghiệm này."),
             ("Nếu tăng nhiệt độ của nước từ 27 °C lên 54 °C thì chiều dài cột khí tăng "
              "gấp đôi.", False,
              "Phải dùng nhiệt độ tuyệt đối: T₁ = 300 K, T₂ = 327 K.\n"
              "ℓ₂/ℓ₁ = 327/300 = 1,09, tức cột khí chỉ dài thêm khoảng 9 %. Nhiệt độ "
              "Celsius tăng gấp đôi hoàn toàn không có nghĩa là nhiệt độ tuyệt đối tăng "
              "gấp đôi."),
             ("Phải đun thật nhanh để cột khí kịp dãn nở trước khi bị mất nhiệt ra môi "
              "trường.", False,
              "Ngược lại, phải đun TỪ TỪ. Nhiệt độ ghi trên nhiệt kế là nhiệt độ của nước; "
              "chỉ khi đun chậm thì khí trong ống mới kịp cân bằng nhiệt với nước, khiến "
              "số đo mới đúng với nhiệt độ của khí. Đun nhanh làm khí trong ống “trễ” hơn "
              "nước, gây sai số hệ thống."),
         ]),

    dict(stem="Một bình kín dung tích 10 lít chứa 0,40 mol khí lí tưởng ở 27 °C.",
         items=[
             ("Áp suất của khí trong bình xấp xỉ 1,0·10⁵ Pa.", True,
              "p = nRT/V = (0,40 × 8,31 × 300)/(10·10⁻³) = 997,2/0,010 = 99 720 Pa "
              "≈ 1,0·10⁵ Pa."),
             ("Nếu đun nóng bình tới 54 °C thì áp suất của khí tăng gấp đôi.", False,
              "T₂ = 54 + 273 = 327 K, chỉ gấp 327/300 = 1,09 lần T₁ = 300 K, nên áp suất "
              "cũng chỉ tăng khoảng 9 %. Muốn áp suất tăng gấp đôi phải đưa nhiệt độ lên "
              "600 K, tức 327 °C."),
             ("Nếu bơm thêm 0,20 mol khí cùng loại vào bình và giữ nhiệt độ 27 °C thì áp "
              "suất tăng gấp đôi.", False,
              "Ở cùng V và T, áp suất tỉ lệ thuận với số mol. Số mol tăng từ 0,40 lên "
              "0,60 mol, tức gấp 1,5 lần, nên áp suất cũng chỉ tăng 1,5 lần. Muốn gấp đôi "
              "phải bơm thêm đúng 0,40 mol."),
             ("Số phân tử khí trong bình xấp xỉ 2,4·10²³.", True,
              "N = n·N_A = 0,40 × 6,02·10²³ = 2,408·10²³ ≈ 2,4·10²³ phân tử."),
         ]),

    dict(stem="Một quả bóng cao su chứa khí lí tưởng, có thể tích 2,0 lít ở 27 °C và áp "
              "suất 1,2·10⁵ Pa. Lượng khí trong bóng không đổi trong mọi tình huống dưới "
              "đây.",
         items=[
             ("Nếu nhúng bóng vào nước đá đang tan (0 °C) mà thể tích của nó không đổi thì "
              "áp suất khí trong bóng còn khoảng 1,00·10⁵ Pa.", False,
              "Đẳng tích: p₂ = p₁·T₂/T₁ = 1,2·10⁵ × 273/300 = 1,092·10⁵ Pa, tức khoảng "
              "1,09·10⁵ Pa chứ không phải 1,00·10⁵ Pa."),
             ("Nếu giữ nhiệt độ không đổi và bóp cho thể tích còn 1,5 lít thì áp suất khí "
              "là 1,6·10⁵ Pa.", True,
              "Lượng khí và nhiệt độ đều không đổi nên áp dụng được định luật Boyle: "
              "p₂ = p₁V₁/V₂ = 1,2·10⁵ × 2,0/1,5 = 1,6·10⁵ Pa. Thể tích giảm 1,33 lần "
              "thì áp suất tăng đúng 1,33 lần."),
             ("Nếu vừa đun nóng bóng tới 87 °C vừa để bóng nở tới 2,4 lít thì áp suất khí "
              "trong bóng không đổi.", True,
              "T₂/T₁ = (87 + 273)/300 = 360/300 = 1,20 và V₂/V₁ = 2,4/2,0 = 1,20. Thể tích "
              "và nhiệt độ tuyệt đối tăng cùng một tỉ lệ nên theo pV/T = hằng số, áp suất "
              "giữ nguyên: đây đúng là một quá trình đẳng áp."),
             ("Khi đun nóng quả bóng, số phân tử khí bên trong bóng tăng lên.", False,
              "Bóng kín nên lượng khí, tức số phân tử, hoàn toàn không đổi. Đun nóng chỉ "
              "làm các phân tử chuyển động nhanh hơn chứ không sinh thêm phân tử mới."),
         ]),
]

DE2_P3 = [
    dict(q="Tính số phân tử khí lí tưởng chứa trong một bình kín dung tích 2,0 lít ở "
           "27 °C, áp suất 1,0·10⁵ Pa. (Kết quả theo 10²² phân tử, làm tròn đến hàng phần "
           "mười.)",
         ans="4,8",
         sol="Số mol khí: n = pV/(RT) = (1,0·10⁵ × 2,0·10⁻³)/(8,31 × 300) = 200/2493 "
             "≈ 0,08023 mol.\n"
             "Số phân tử: N = n·N_A = 0,08023 × 6,02·10²³ ≈ 4,83·10²² phân tử.\n"
             "Vậy kết quả cần điền là 4,8."),

    dict(q="Nén đẳng nhiệt một lượng khí lí tưởng từ 5,0 lít xuống còn 2,0 lít thì áp suất "
           "của khí tăng thêm 1,8·10⁵ Pa. Tính áp suất ban đầu của khí (theo 10⁴ Pa, làm "
           "tròn đến hàng đơn vị).",
         ans="12",
         sol="Gọi p₁ là áp suất ban đầu, khi đó p₂ = p₁ + 1,8·10⁵.\n"
             "Định luật Boyle: p₁ × 5,0 = (p₁ + 1,8·10⁵) × 2,0\n"
             "5,0p₁ = 2,0p₁ + 3,6·10⁵ ⇒ 3,0p₁ = 3,6·10⁵ ⇒ p₁ = 1,2·10⁵ Pa = 12·10⁴ Pa.\n"
             "Kiểm tra: p₂ = 3,0·10⁵ Pa và 1,2 × 5,0 = 3,0 × 2,0 = 6,0."),

    dict(q="Một lượng khí lí tưởng có p₁ = 2,0·10⁵ Pa, V₁ = 4,0 lít ở nhiệt độ 27 °C. Sau "
           "khi biến đổi, khí có p₂ = 5,0·10⁵ Pa và V₂ = 2,4 lít. Tính nhiệt độ của khí "
           "sau khi biến đổi (theo °C, làm tròn đến hàng đơn vị).",
         ans="177",
         sol="Phương trình trạng thái: T₂ = T₁ × (p₂V₂)/(p₁V₁)\n"
             "T₂ = 300 × (5,0 × 2,4)/(2,0 × 4,0) = 300 × 12/8,0 = 450 K.\n"
             "t₂ = 450 − 273 = 177 °C."),

    dict(q="Tính khối lượng khí oxygen (khối lượng mol 32 g/mol) chứa trong một bình kín "
           "dung tích 5,0 lít ở 27 °C, áp suất 4,0·10⁵ Pa. (Kết quả theo gam, làm tròn đến "
           "hàng đơn vị.)",
         ans="26",
         sol="Số mol: n = pV/(RT) = (4,0·10⁵ × 5,0·10⁻³)/(8,31 × 300) = 2000/2493 "
             "≈ 0,8023 mol.\n"
             "Khối lượng: m = n·M = 0,8023 × 32 ≈ 25,7 g ≈ 26 g."),

    dict(q="Một bình dung tích 20 lít chứa khí ở áp suất 6,0·10⁵ Pa và 300 K. Người ta xả "
           "bớt khí ra ngoài cho tới khi áp suất trong bình còn 2,4·10⁵ Pa, nhiệt độ vẫn "
           "giữ 300 K. Tính phần trăm khối lượng khí đã xả ra (theo %, làm tròn đến hàng "
           "đơn vị).",
         ans="60",
         sol="V và T không đổi nên số mol (và khối lượng) khí tỉ lệ thuận với áp suất.\n"
             "Tỉ lệ khối lượng còn lại: 2,4/6,0 = 0,40.\n"
             "Phần đã xả ra: 1 − 0,40 = 0,60 = 60 %."),

    dict(q="Một cột khí bị giam trong ống nghiệm đặt thẳng đứng, đầu hở lên trên, ngăn "
           "cách với bên ngoài bởi một giọt thuỷ ngân. Ở 27 °C cột khí dài 20,0 cm. Đun "
           "nóng khí tới 87 °C. Tính chiều dài cột khí lúc đó (theo cm, làm tròn đến hàng "
           "phần mười).",
         ans="24,0",
         sol="Giọt thuỷ ngân trượt tự do nên áp suất cột khí không đổi: đây là quá trình "
             "đẳng áp. Vì tiết diện ống không đổi, thể tích tỉ lệ thuận với chiều dài cột "
             "khí.\n"
             "ℓ₂ = ℓ₁·T₂/T₁ = 20,0 × (87 + 273)/(27 + 273) = 20,0 × 360/300 = 24,0 cm."),
]

DE2 = dict(code="C2-02", so="02", chuong=2,
           title="ĐỀ KIỂM TRA CHƯƠNG II – ĐỀ SỐ 02",
           subtitle="Chương II – Khí lí tưởng",
           p1=DE2_P1, p2=DE2_P2, p3=DE2_P3)


# ===================================================================================
#        ĐỀ SỐ 03 – PHƯƠNG TRÌNH TRẠNG THÁI, CHU TRÌNH VÀ CỘT THUỶ NGÂN
# ===================================================================================

DE3_P1 = [
    dict(q="Phương trình p₁V₁/T₁ = p₂V₂/T₂ được áp dụng cho",
         o=["một lượng khí lí tưởng xác định, tức khối lượng khí không đổi.",
            "một lượng khí bất kì, kể cả khi có khí thoát ra hoặc bơm thêm vào.",
            "mọi chất khí thực ở áp suất rất lớn và nhiệt độ rất thấp.",
            "hỗn hợp gồm nhiều chất khí khác nhau có khối lượng thay đổi."],
         a="A",
         sol="Phương trình trạng thái được suy ra từ pV = nRT với n giữ nguyên, nên chỉ "
             "đúng khi lượng khí không đổi. Nếu có khí ra vào thì phải dùng trực tiếp "
             "pV = nRT cho từng trạng thái. Khí thực chỉ tuân theo gần đúng và chỉ khi áp "
             "suất không quá lớn, nhiệt độ không quá thấp."),

    dict(q="Áp suất khí quyển chuẩn 1 atm tương đương với",
         o=["76 cmHg.", "76 mmHg.", "7,6 cmHg.", "760 cmHg."],
         a="A",
         sol="1 atm = 760 mmHg = 76 cmHg = 1,013·10⁵ Pa. Cần cẩn thận khi đổi giữa mmHg và "
             "cmHg vì đây là chỗ rất hay nhầm trong các bài toán ống chữ U."),

    dict(q="Gọi N là số phân tử khí chứa trong thể tích V, m₀ là khối lượng một phân tử "
           "và v̄² là trung bình của bình phương tốc độ phân tử. Áp suất của chất khí "
           "được tính theo mô hình động học phân tử bằng biểu thức",
         o=["p = (1/3)·(N/V)·m₀·v̄².", "p = (3/2)·(N/V)·m₀·v̄².",
            "p = (1/2)·(N/V)·m₀·v̄².", "p = (1/3)·(N/V)·m₀·v̄."],
         a="A",
         sol="Công thức áp suất theo mô hình động học phân tử là p = (1/3)·(N/V)·m₀·v̄², "
             "cũng viết được thành p = (1/3)ρv̄² với ρ là khối lượng riêng của khí. Từ đó "
             "suy ra p = (2/3)·(N/V)·W̄: áp suất bằng hai phần ba tích của mật độ phân tử "
             "với động năng tịnh tiến trung bình của một phân tử."),

    dict(q="Trong một quá trình đẳng nhiệt của lượng khí lí tưởng xác định, đại lượng nào "
           "sau đây được bảo toàn?",
         o=["Tích pV.", "Thương p/V.", "Thương V/T.", "Tổng p + V."],
         a="A",
         sol="Định luật Boyle: pV = hằng số trong quá trình đẳng nhiệt. Thương V/T là hằng "
             "số trong quá trình đẳng áp, còn p/T là hằng số trong quá trình đẳng tích."),

    dict(q="Hình vẽ là chu trình biến đổi của một lượng khí lí tưởng. Quá trình (1) → (2) là",
         fig="t23a",
         o=["quá trình đẳng nhiệt.", "quá trình đẳng áp.",
            "quá trình đẳng tích.", "quá trình đoạn nhiệt."],
         a="A",
         sol="Đoạn (1) → (2) là một nhánh hypebol trong hệ (p, V) và thoả mãn "
             "p₁V₁ = 3 × 2 = 6 = p₂V₂ = 1 × 6 (atm·lít). Tích pV không đổi chính là dấu "
             "hiệu của quá trình đẳng nhiệt."),

    dict(q="Vẫn với chu trình trong hình vẽ đó, so với nhiệt độ ở trạng thái (1) thì nhiệt "
           "độ ở trạng thái (3)",
         fig="t23a",
         o=["nhỏ hơn 3 lần.", "lớn hơn 3 lần.", "nhỏ hơn 2 lần.", "bằng nhau."],
         a="A",
         sol="Trạng thái (1) và (3) có cùng thể tích 2 lít nhưng áp suất lần lượt là 3 atm "
             "và 1 atm. Với V không đổi, p tỉ lệ thuận với T nên T₃/T₁ = p₃/p₁ = 1/3, tức "
             "T₃ nhỏ hơn T₁ ba lần. (Cũng có thể so sánh tích pV: 6 so với 2.)"),

    dict(q="Khi bơm xe đạp, thể tích của khối khí trong bơm giảm nhưng áp suất tăng lên. "
           "Giải thích theo mô hình động học phân tử là",
         o=["mật độ phân tử tăng nên số va chạm lên một đơn vị diện tích thành bơm trong "
            "một giây tăng.",
            "kích thước của mỗi phân tử khí tăng lên khi thể tích khối khí bị giảm đi.",
            "các phân tử khí dính lại thành từng cụm lớn nên va chạm mạnh hơn nhiều.",
            "lực đẩy giữa các phân tử khí biến mất khi chúng bị nén lại gần nhau."],
         a="A",
         sol="Áp suất khí sinh ra từ các va chạm của phân tử lên thành bình; nó phụ thuộc "
             "vào mật độ phân tử N/V và động năng trung bình của mỗi phân tử. Khi nén, mật "
             "độ tăng nên tần suất va chạm tăng và áp suất tăng. Kích thước phân tử là đại "
             "lượng không đổi."),

    dict(q="Hình vẽ là một ống chữ U tiết diện đều chứa thuỷ ngân; nhánh trái kín giam một "
           "cột khí, nhánh phải hở ra khí quyển. Mực thuỷ ngân ở nhánh hở cao hơn nhánh "
           "kín một đoạn h. Áp suất của cột khí bị giam (tính theo cmHg) bằng",
         fig="t23b",
         o=["p₀ + h.", "p₀ − h.", "h − p₀.", "p₀."],
         a="A",
         sol="Xét mặt phẳng ngang đi qua mực thuỷ ngân THẤP hơn (ở nhánh kín). Áp suất tại "
             "đó tính từ phía nhánh kín là p_khí; tính từ phía nhánh hở là p₀ cộng với áp "
             "suất của cột thuỷ ngân cao h. Cân bằng cho p_khí = p₀ + h. Vì mực bên nhánh "
             "hở cao hơn nên khí bị giam có áp suất LỚN hơn khí quyển."),

    dict(q="Hai bình có cùng thể tích, chứa hai chất khí khác nhau ở cùng áp suất và cùng "
           "nhiệt độ. Khi đó",
         o=["số phân tử khí trong hai bình bằng nhau.",
            "khối lượng khí trong hai bình bằng nhau.",
            "khối lượng riêng của khí trong hai bình bằng nhau.",
            "tốc độ trung bình của phân tử trong hai bình bằng nhau."],
         a="A",
         sol="Từ pV = nRT: cùng p, V, T thì n bằng nhau, do đó số phân tử N = n·N_A cũng "
             "bằng nhau (định luật Avogadro). Khối lượng thì khác nhau vì khối lượng mol "
             "của hai khí khác nhau; do cùng thể tích nên khối lượng riêng cũng khác nhau; "
             "và ở cùng nhiệt độ, khí nhẹ hơn có tốc độ trung bình lớn hơn."),

    dict(q="Khí thực chỉ tuân theo gần đúng các định luật chất khí khi",
         o=["áp suất không quá lớn và nhiệt độ không quá thấp.",
            "áp suất rất lớn và nhiệt độ rất thấp.",
            "khí được chứa trong bình có thể tích rất nhỏ.",
            "khí đang ở gần điểm hoá lỏng của chính nó."],
         a="A",
         sol="Mô hình khí lí tưởng bỏ qua thể tích riêng của phân tử và lực tương tác giữa "
             "chúng. Hai điều này chỉ hợp lí khi các phân tử ở xa nhau, tức khi khí loãng: "
             "áp suất không quá lớn và nhiệt độ không quá thấp. Gần điểm hoá lỏng, lực hút "
             "giữa các phân tử trở nên quan trọng và mô hình sai lệch mạnh."),

    dict(q="Trong ống chữ U ở hình vẽ, áp suất khí quyển là p₀ = 75 cmHg và độ chênh lệch "
           "mực thuỷ ngân là h = 12 cm. Áp suất của cột khí bị giam bằng",
         fig="t23b",
         o=["87 cmHg.", "63 cmHg.", "75 cmHg.", "12 cmHg."],
         a="A",
         sol="Vì mực thuỷ ngân ở nhánh hở cao hơn nhánh kín nên áp suất khí bị giam lớn "
             "hơn áp suất khí quyển:\n"
             "p = p₀ + h = 75 + 12 = 87 cmHg.\n"
             "Kết quả 63 cmHg ứng với việc nhầm chiều chênh lệch."),

    dict(q="Vẫn với chu trình trong hình vẽ ở Câu 5. Biết ở trạng thái (1) khí có p₁ = "
           "3,0 atm, V₁ = 2,0 lít và T₁ = 600 K. Nhiệt độ của khí ở trạng thái (3) là",
         fig="t23a",
         o=["200 K.", "600 K.", "300 K.", "1800 K."],
         a="A",
         sol="Trạng thái (3) có p₃ = 1,0 atm, V₃ = 2,0 lít.\n"
             "Áp dụng phương trình trạng thái: T₃ = T₁ × (p₃V₃)/(p₁V₁) = "
             "600 × (1,0 × 2,0)/(3,0 × 2,0) = 600 × 2/6 = 200 K.\n"
             "(Trạng thái (2) cũng có nhiệt độ 600 K vì (1) → (2) là quá trình đẳng nhiệt.)"),

    dict(q="Dùng một bơm tay có thể tích mỗi lần bơm là 250 cm³ để bơm không khí ở áp "
           "suất 1,0·10⁵ Pa vào một quả bóng có thể tích 2,0 lít, ban đầu đã chứa không "
           "khí ở đúng áp suất 1,0·10⁵ Pa. Coi thể tích bóng và nhiệt độ không đổi. Sau "
           "20 lần bơm, áp suất khí trong bóng là",
         o=["3,5·10⁵ Pa.", "2,5·10⁵ Pa.", "5,0·10⁵ Pa.", "6,0·10⁵ Pa."],
         a="A",
         sol="Ở nhiệt độ không đổi, tổng tích pV của lượng khí được bảo toàn.\n"
             "Khí có sẵn trong bóng: 1,0·10⁵ × 2,0 = 2,0·10⁵ (Pa·lít).\n"
             "Khí bơm thêm: 20 × 1,0·10⁵ × 0,250 = 5,0·10⁵ (Pa·lít).\n"
             "Tổng lượng khí nằm gọn trong 2,0 lít của quả bóng:\n"
             "p × 2,0 = 2,0·10⁵ + 5,0·10⁵ = 7,0·10⁵ ⇒ p = 3,5·10⁵ Pa.\n"
             "Sai lầm thường gặp là quên phần không khí đã có sẵn trong bóng, dẫn tới kết "
             "quả 2,5·10⁵ Pa."),

    dict(q="Một bình kín dung tích 10 lít chứa 2,0 g khí hydrogen (khối lượng mol 2,0 "
           "g/mol) ở 27 °C. Áp suất của khí trong bình xấp xỉ",
         o=["2,49·10⁵ Pa.", "2,49·10⁴ Pa.", "4,99·10⁵ Pa.", "1,25·10⁵ Pa."],
         a="A",
         sol="n = m/M = 2,0/2,0 = 1,0 mol; V = 10·10⁻³ m³; T = 300 K.\n"
             "p = nRT/V = (1,0 × 8,31 × 300)/0,010 = 2493/0,010 = 2,493·10⁵ Pa "
             "≈ 2,49·10⁵ Pa."),

    dict(q="Một lượng khí lí tưởng ở 300 K, áp suất 1,0·10⁵ Pa và thể tích 3,0 lít được "
           "nén đẳng nhiệt xuống còn 1,0 lít, sau đó được đun nóng đẳng tích tới 600 K. Áp "
           "suất của khí ở cuối quá trình là",
         o=["6,0·10⁵ Pa.", "3,0·10⁵ Pa.", "1,5·10⁵ Pa.", "2,0·10⁵ Pa."],
         a="A",
         sol="Giai đoạn 1 (đẳng nhiệt): p′ = p₁V₁/V₂ = 1,0·10⁵ × 3,0/1,0 = 3,0·10⁵ Pa.\n"
             "Giai đoạn 2 (đẳng tích, 300 K → 600 K): p₂ = p′ × 600/300 = 6,0·10⁵ Pa."),

    dict(q="Một ống thuỷ tinh dài 60 cm, một đầu kín, đặt nằm ngang. Trong ống có một cột "
           "thuỷ ngân dài 10 cm ngăn cột khí kín dài 20 cm với không khí bên ngoài. Áp "
           "suất khí quyển là 75 cmHg. Áp suất của cột khí bị giam bằng",
         o=["75 cmHg.", "85 cmHg.", "65 cmHg.", "60 cmHg."],
         a="A",
         sol="Ống đặt NẰM NGANG nên cột thuỷ ngân không đè lên khí theo phương thẳng đứng: "
             "trọng lượng của nó được thành ống đỡ. Áp suất truyền qua cột thuỷ ngân theo "
             "phương ngang không thay đổi, nên p_khí = p₀ = 75 cmHg. Chỉ khi dựng ống "
             "thẳng đứng mới phải cộng hoặc trừ chiều dài cột thuỷ ngân."),

    dict(q="Vẫn với chiếc ống trong Câu 16. Nếu dựng ống thẳng đứng với đầu KÍN Ở TRÊN "
           "(nhiệt độ không đổi) thì chiều dài cột khí bị giam xấp xỉ",
         o=["23,1 cm.", "17,6 cm.", "20,0 cm.", "26,0 cm."],
         a="A",
         sol="Khi đầu kín ở trên, cột thuỷ ngân nằm phía dưới cột khí; trọng lượng của nó "
             "kéo xuống nên áp suất khí giảm:\n"
             "p₂ = p₀ − 10 = 75 − 10 = 65 cmHg.\n"
             "Nhiệt độ không đổi nên p₁ℓ₁ = p₂ℓ₂ (tiết diện đều):\n"
             "ℓ₂ = 75 × 20/65 ≈ 23,1 cm. Áp suất giảm nên cột khí dài ra, phù hợp với kết "
             "quả."),

    dict(q="Một bình kín thể tích không đổi chứa khí ở 27 °C, áp suất 3,0·10⁵ Pa. Người ta "
           "lấy ra một phần tư khối lượng khí trong bình, đồng thời hạ nhiệt độ xuống "
           "−23 °C. Áp suất khí còn lại trong bình là",
         o=["1,88·10⁵ Pa.", "2,25·10⁵ Pa.", "2,50·10⁵ Pa.", "1,50·10⁵ Pa."],
         a="A",
         sol="Thể tích không đổi nên từ pV = nRT suy ra p tỉ lệ thuận với tích n·T.\n"
             "Số mol còn lại: 3/4 số mol ban đầu. Nhiệt độ: T₂ = −23 + 273 = 250 K, "
             "T₁ = 300 K.\n"
             "p₂ = 3,0·10⁵ × (3/4) × (250/300) = 3,0·10⁵ × 0,75 × 0,8333 ≈ 1,88·10⁵ Pa.\n"
             "Nếu chỉ tính một trong hai yếu tố sẽ ra 2,25·10⁵ Pa hoặc 2,50·10⁵ Pa — đó là "
             "các phương án nhiễu."),
]

DE3_P2 = [
    dict(stem="Một lượng khí lí tưởng thực hiện chu trình như hình vẽ. Ở trạng thái (1) "
              "khí có p₁ = 3,0 atm, V₁ = 2,0 lít và T₁ = 600 K.",
         fig="t23a",
         items=[
             ("Quá trình (1) → (2) là quá trình đẳng nhiệt, trong đó khí dãn nở.", True,
              "p₁V₁ = 3,0 × 2,0 = 6,0 và p₂V₂ = 1,0 × 6,0 = 6,0 (atm·lít), tích pV không "
              "đổi nên đây là quá trình đẳng nhiệt. Thể tích tăng từ 2,0 lên 6,0 lít nên "
              "khí dãn nở."),
             ("Ở trạng thái (2), nhiệt độ của khí là 200 K.", False,
              "Quá trình (1) → (2) là đẳng nhiệt nên T₂ = T₁ = 600 K. Giá trị 200 K là "
              "nhiệt độ của trạng thái (3) chứ không phải (2)."),
             ("Quá trình (2) → (3) là quá trình đẳng áp, khí bị nén và nhiệt độ giảm còn "
              "200 K.", True,
              "Trên đồ thị, (2) → (3) là đoạn nằm ngang ở p = 1,0 atm nên đẳng áp; thể "
              "tích giảm từ 6,0 xuống 2,0 lít nên khí bị nén.\n"
              "Đẳng áp: T₃ = T₂·V₃/V₂ = 600 × 2,0/6,0 = 200 K."),
             ("Quá trình (3) → (1) là quá trình đẳng tích, trong đó khí toả nhiệt.", False,
              "Đúng là đẳng tích (đoạn thẳng đứng tại V = 2,0 lít), nhưng nhiệt độ TĂNG từ "
              "200 K lên 600 K. Đẳng tích nên A = 0, do đó ΔU = Q > 0: khí NHẬN nhiệt chứ "
              "không toả nhiệt."),
         ]),

    dict(stem="Hình vẽ là một ống chữ U tiết diện đều chứa thuỷ ngân; nhánh trái kín giam "
              "một cột khí dài 20 cm, nhánh phải hở. Mực thuỷ ngân ở nhánh hở cao hơn "
              "nhánh kín một đoạn h = 12 cm. Áp suất khí quyển p₀ = 75 cmHg; nhiệt độ "
              "không đổi trong các ý a, b, c.",
         fig="t23b",
         items=[
             ("Áp suất của cột khí bị giam là 63 cmHg.", False,
              "Mực thuỷ ngân ở nhánh HỞ cao hơn, nghĩa là khí bị giam phải đẩy được cả cột "
              "thuỷ ngân dư đó, tức áp suất của nó LỚN hơn khí quyển:\n"
              "p = p₀ + h = 75 + 12 = 87 cmHg. Giá trị 63 cmHg = 75 − 12 ứng với trường "
              "hợp ngược lại (mực bên kín cao hơn)."),
             ("Nếu đổ thêm thuỷ ngân vào nhánh hở thì cột khí bị giam ngắn lại.", True,
              "Đổ thêm thuỷ ngân làm mực bên nhánh hở dâng lên, độ chênh h tăng, nên áp "
              "suất tác dụng lên cột khí tăng. Ở nhiệt độ không đổi, p tăng thì V giảm "
              "(định luật Boyle), tức cột khí ngắn lại."),
             ("Nếu áp suất khí quyển giảm còn 74 cmHg thì cột khí bị giam ngắn lại.", False,
              "Áp suất khí quyển giảm làm áp suất tác dụng lên cột khí giảm theo, nên cột "
              "khí phải DÀI RA chứ không ngắn lại. (Khi khí dãn ra, thuỷ ngân bị đẩy sang "
              "nhánh hở nên h cũng thay đổi, nhưng chiều biến đổi của thể tích thì vẫn là "
              "tăng.)"),
             ("Nếu đun nóng cột khí bị giam thì độ chênh lệch mực thuỷ ngân h tăng lên.",
              True,
              "Đun nóng làm khí dãn ra, đẩy mực thuỷ ngân ở nhánh kín xuống và dồn thuỷ "
              "ngân sang nhánh hở làm mực bên đó dâng lên. Cả hai chuyển động đều làm độ "
              "chênh lệch h tăng."),
         ]),

    dict(stem="Hình vẽ mô tả một bình khí nén dung tích 20 lít chứa khí ở 15·10⁵ Pa và "
              "300 K, được nối với một lốp xe dung tích 8,0 lít đang chứa khí cùng loại ở "
              "1,0·10⁵ Pa và 300 K. Mở van cho tới khi áp suất hai bên bằng nhau; nhiệt độ "
              "luôn giữ 300 K và thể tích lốp coi như không đổi.",
         fig="t23c",
         items=[
             ("Sau khi mở van, khối lượng khí trong bình bằng khối lượng khí trong lốp.",
              False,
              "Sau khi mở van, hai phần khí có cùng áp suất và cùng nhiệt độ nên khối "
              "lượng của chúng tỉ lệ thuận với thể tích. Bình 20 lít chứa khối lượng gấp "
              "20/8,0 = 2,5 lần lốp 8,0 lít, chứ không bằng nhau."),
             ("Áp suất chung sau khi mở van là 11·10⁵ Pa.", True,
              "Ở nhiệt độ không đổi, tổng số mol bảo toàn kéo theo tổng tích pV bảo toàn:\n"
              "p × 28 = 15·10⁵ × 20 + 1,0·10⁵ × 8,0 = 308·10⁵ ⇒ p = 11·10⁵ Pa."),
             ("Lượng khí đã chuyển từ bình sang lốp tương đương với 8,0 lít khí ở áp suất "
              "15·10⁵ Pa.", False,
              "Khí trong lốp có tích pV tăng từ 1,0·10⁵ × 8,0 = 8,0·10⁵ lên "
              "11·10⁵ × 8,0 = 88·10⁵, tức tăng 80·10⁵ (Pa·lít). Quy về áp suất 15·10⁵ Pa "
              "thì lượng đó ứng với 80·10⁵/15·10⁵ ≈ 5,3 lít chứ không phải 8,0 lít."),
             ("Nếu sau đó để cả hệ ngoài nắng cho nhiệt độ tăng lên 330 K thì áp suất "
              "chung tăng lên 12,1·10⁵ Pa.", True,
              "Tổng thể tích và tổng lượng khí không đổi nên hệ biến đổi đẳng tích:\n"
              "p′ = 11·10⁵ × 330/300 = 12,1·10⁵ Pa."),
         ]),

    dict(stem="Một xi lanh nằm ngang, hai đầu kín, được chia thành hai phần bằng nhau bởi "
              "một pit-tông mỏng, nhẹ, không ma sát. Mỗi phần dài 30 cm và chứa cùng một "
              "lượng khí lí tưởng ở 300 K, áp suất 1,0·10⁵ Pa.",
         items=[
             ("Ban đầu áp suất khí ở hai bên bằng nhau nên pit-tông đứng yên.", True,
              "Pit-tông nhẹ và không ma sát nên nó cân bằng khi và chỉ khi lực ép hai phía "
              "bằng nhau, tức áp suất hai bên bằng nhau. Điều kiện đó đang được thoả mãn."),
             ("Nếu đun nóng đồng thời cả hai phần lên 400 K thì pit-tông dịch sang phải và "
              "áp suất mỗi bên là 1,0·10⁵ Pa.", False,
              "Hai phần khí giống hệt nhau và được đun như nhau nên chúng luôn có áp suất "
              "bằng nhau, pit-tông ĐỨNG YÊN. Thể tích mỗi bên không đổi nên đó là quá "
              "trình đẳng tích: p = 1,0·10⁵ × 400/300 ≈ 1,33·10⁵ Pa chứ không phải "
              "1,0·10⁵ Pa."),
             ("Nếu chỉ đun nóng phần bên phải lên 400 K (giữ phần bên trái ở 300 K) thì "
              "pit-tông dịch sang trái khoảng 4,3 cm.", True,
              "Gọi x là độ dịch chuyển về phía trái. Áp suất hai bên phải bằng nhau:\n"
              "Trái (đẳng nhiệt 300 K): p = 1,0·10⁵ × 30/(30 − x).\n"
              "Phải (300 K → 400 K): p = 1,0·10⁵ × [30/(30 + x)] × (400/300) = "
              "1,0·10⁵ × 40/(30 + x).\n"
              "Cho bằng nhau: 30(30 + x) = 40(30 − x) ⇒ 70x = 300 ⇒ x ≈ 4,3 cm."),
             ("Trong trường hợp của ý c, áp suất cuối cùng ở hai phần khác nhau.", False,
              "Pit-tông nhẹ, không ma sát và đứng yên ở vị trí mới, nên điều kiện cân bằng "
              "buộc áp suất hai bên phải BẰNG nhau. Chính điều kiện này là phương trình "
              "dùng để tìm x."),
         ]),
]

DE3_P3 = [
    dict(q="Một lượng khí lí tưởng ở 27 °C, áp suất 1,0·10⁵ Pa và thể tích 5,0 lít được "
           "nén đẳng nhiệt xuống còn 2,0 lít, sau đó được làm lạnh đẳng tích tới −73 °C. "
           "Tính áp suất của khí ở cuối quá trình (theo 10⁵ Pa, làm tròn đến hàng phần "
           "trăm).",
         ans="1,67",
         sol="Giai đoạn 1 (đẳng nhiệt): p′ = p₁V₁/V₂ = 1,0·10⁵ × 5,0/2,0 = 2,5·10⁵ Pa.\n"
             "Giai đoạn 2 (đẳng tích): T₁ = 300 K, T₂ = −73 + 273 = 200 K.\n"
             "p₂ = 2,5·10⁵ × 200/300 ≈ 1,67·10⁵ Pa."),

    dict(q="Một ống thuỷ tinh một đầu kín, đặt nằm ngang, có cột khí bị giam dài 20 cm "
           "ngăn cách với bên ngoài bởi một cột thuỷ ngân dài 10 cm. Áp suất khí quyển là "
           "75 cmHg. Dựng ống thẳng đứng với đầu kín ở DƯỚI (nhiệt độ không đổi). Tính "
           "chiều dài cột khí bị giam lúc đó (theo cm, làm tròn đến hàng phần mười).",
         ans="17,6",
         sol="Khi nằm ngang: p₁ = 75 cmHg, ℓ₁ = 20 cm.\n"
             "Khi dựng đứng đầu kín ở dưới, cột thuỷ ngân nằm phía TRÊN cột khí và đè "
             "xuống, nên áp suất khí tăng:\n"
             "p₂ = p₀ + 10 = 85 cmHg.\n"
             "Định luật Boyle (tiết diện đều nên V tỉ lệ với ℓ): ℓ₂ = p₁ℓ₁/p₂ = "
             "75 × 20/85 ≈ 17,6 cm.\n"
             "Áp suất tăng thì cột khí ngắn lại, kết quả phù hợp về mặt định tính."),

    dict(q="Một bình kín dung tích 8,0 lít chứa 0,60 mol khí lí tưởng ở 127 °C. Tính áp "
           "suất của khí trong bình (theo 10⁵ Pa, làm tròn đến hàng phần trăm).",
         ans="2,49",
         sol="T = 127 + 273 = 400 K; V = 8,0·10⁻³ m³.\n"
             "p = nRT/V = (0,60 × 8,31 × 400)/(8,0·10⁻³) = 1994,4/0,0080 = 249 300 Pa "
             "≈ 2,49·10⁵ Pa."),

    dict(q="Một quả bóng bay chứa 4,0 lít khí helium ở mặt đất, nơi có áp suất 1,0·10⁵ Pa "
           "và nhiệt độ 300 K. Bóng bay lên tới nơi có áp suất 0,80·10⁵ Pa và nhiệt độ "
           "270 K. Tính thể tích của bóng lúc đó (theo lít, làm tròn đến hàng phần mười).",
         ans="4,5",
         sol="Phương trình trạng thái: V₂ = V₁ × (p₁/p₂) × (T₂/T₁)\n"
             "V₂ = 4,0 × (1,0/0,80) × (270/300) = 4,0 × 1,25 × 0,90 = 4,5 lít.\n"
             "Áp suất giảm làm bóng nở ra, nhiệt độ giảm lại kéo bóng co lại; ở đây tác "
             "dụng của áp suất mạnh hơn nên thể tích tăng."),

    dict(q="Một bình dung tích 25 lít chứa khí ở áp suất 8,0·10⁵ Pa và 300 K. Người ta nối "
           "bình đó với một bình rỗng đã hút chân không có dung tích 15 lít, nhiệt độ luôn "
           "giữ 300 K. Tính áp suất chung của khí sau khi mở van (theo 10⁵ Pa, làm tròn "
           "đến hàng phần mười).",
         ans="5,0",
         sol="Lượng khí và nhiệt độ không đổi, chỉ có thể tích tăng từ 25 lít lên "
             "25 + 15 = 40 lít. Đây là quá trình đẳng nhiệt:\n"
             "p₂ = p₁V₁/V₂ = 8,0·10⁵ × 25/40 = 5,0·10⁵ Pa."),

    dict(q="Một lượng khí lí tưởng có khối lượng 8,0 g và khối lượng mol 32 g/mol được "
           "chứa trong bình 6,0 lít, áp suất 2,0·10⁵ Pa. Tính nhiệt độ của khí (theo K, "
           "làm tròn đến hàng đơn vị).",
         ans="578",
         sol="Số mol: n = m/M = 8,0/32 = 0,25 mol.\n"
             "Từ pV = nRT: T = pV/(nR) = (2,0·10⁵ × 6,0·10⁻³)/(0,25 × 8,31) = "
             "1200/2,0775 ≈ 577,6 K ≈ 578 K."),
]

DE3 = dict(code="C2-03", so="03", chuong=2,
           title="ĐỀ KIỂM TRA CHƯƠNG II – ĐỀ SỐ 03",
           subtitle="Chương II – Khí lí tưởng",
           p1=DE3_P1, p2=DE3_P2, p3=DE3_P3)


# ===================================================================================
#     ĐỀ SỐ 04 – MÔ HÌNH ĐỘNG HỌC PHÂN TỬ, TUYẾN TÍNH HOÁ VÀ PIT-TÔNG
# ===================================================================================

DE4_P1 = [
    dict(q="Trong hệ toạ độ (p, V) với V trên trục hoành, đường đẳng tích của một lượng "
           "khí lí tưởng xác định là",
         o=["đường thẳng song song với trục Op.",
            "đường thẳng song song với trục OV.",
            "một nhánh hypebol nhận hai trục làm tiệm cận.",
            "đường thẳng đi qua gốc toạ độ O."],
         a="A",
         sol="Đẳng tích nghĩa là V giữ một giá trị không đổi, còn p có thể thay đổi. Tập "
             "hợp các điểm có cùng hoành độ V là một đường thẳng đứng, tức song song với "
             "trục Op. Đường song song với trục OV lại là đường đẳng áp."),

    dict(q="Động năng tịnh tiến trung bình của một phân tử khí lí tưởng được tính theo "
           "công thức",
         o=["W̄ = (3/2)k_B·T.", "W̄ = (2/3)k_B·T.",
            "W̄ = (3/2)R·T.", "W̄ = (1/3)k_B·T."],
         a="A",
         sol="W̄ = (3/2)k_B·T, với k_B là hằng số Boltzmann và T là nhiệt độ tuyệt đối. "
             "Điểm quan trọng là W̄ chỉ phụ thuộc NHIỆT ĐỘ, không phụ thuộc bản chất chất "
             "khí. Nếu thay k_B bằng R thì công thức cho nội năng của 1 mol khí đơn nguyên "
             "tử chứ không phải của một phân tử."),

    dict(q="Hằng số Boltzmann có giá trị xấp xỉ",
         o=["1,38·10⁻²³ J/K.", "1,38·10²³ J/K.",
            "8,31·10⁻²³ J/K.", "6,02·10⁻²³ J/K."],
         a="A",
         sol="k_B ≈ 1,38·10⁻²³ J/K. Có thể kiểm tra qua liên hệ k_B = R/N_A = "
             "8,31/(6,02·10²³) ≈ 1,38·10⁻²³ J/K."),

    dict(q="Hình vẽ là kết quả thí nghiệm biểu diễn áp suất p theo 1/V của một lượng khí "
           "xác định ở nhiệt độ không đổi. Đồ thị là một đường thẳng đi qua gốc toạ độ, "
           "điều đó chứng tỏ",
         fig="t24a",
         o=["áp suất tỉ lệ nghịch với thể tích của lượng khí.",
            "áp suất tỉ lệ thuận với thể tích của lượng khí.",
            "áp suất tỉ lệ thuận với bình phương của thể tích.",
            "áp suất của lượng khí không phụ thuộc vào thể tích."],
         a="A",
         sol="Đồ thị p theo 1/V là đường thẳng qua gốc nghĩa là p = k·(1/V), tức p tỉ lệ "
             "THUẬN với 1/V, cũng chính là p tỉ lệ NGHỊCH với V. Đó là nội dung định luật "
             "Boyle. Cách vẽ này (tuyến tính hoá) được ưa dùng vì mắt người kiểm tra một "
             "đường thẳng dễ hơn nhiều so với một nhánh hypebol."),

    dict(q="Vẫn với đồ thị thực nghiệm đó, hệ số góc của đường thẳng có giá trị bằng",
         fig="t24a",
         o=["3,0 atm·lít, chính là tích pV của lượng khí.",
            "3,0 atm/lít, chính là thương p/V của lượng khí.",
            "0,33 lít/atm, chính là thương V/p của lượng khí.",
            "1,0 atm·lít, chính là áp suất của khí khi V = 1 lít."],
         a="A",
         sol="Phương trình đường thẳng là p = k·(1/V) nên hệ số góc k = pV, đơn vị "
             "atm·lít. Đọc trên đồ thị: khi 1/V = 1,0 L⁻¹ thì p = 3,0 atm, vậy "
             "k = 3,0 atm·lít. Đây chính là hằng số Boyle của lượng khí ở nhiệt độ đang "
             "xét."),

    dict(q="Hình vẽ là chu trình M → N → P → M của một lượng khí lí tưởng trong hệ toạ độ "
           "(T, V). Quá trình M → N là",
         fig="t24c",
         o=["quá trình đẳng nhiệt.", "quá trình đẳng áp.",
            "quá trình đẳng tích.", "quá trình đoạn nhiệt."],
         a="A",
         sol="Trên hình, M và N có cùng hoành độ T = 300 K nhưng khác tung độ V (2 lít và "
             "4 lít). Nhiệt độ không đổi nên đó là quá trình đẳng nhiệt, trong đó khí dãn "
             "nở từ 2 lít lên 4 lít."),

    dict(q="Giữ nguyên nhiệt độ và nén một lượng khí lí tưởng cho thể tích của nó giảm "
           "một nửa. Khi đó tốc độ căn quân phương của các phân tử khí",
         o=["không thay đổi.", "tăng √2 lần.", "giảm √2 lần.", "tăng gấp đôi."],
         a="A",
         sol="Tốc độ căn quân phương v = √(3RT/M) chỉ phụ thuộc nhiệt độ và khối lượng "
             "mol, hoàn toàn không phụ thuộc thể tích hay áp suất. Nén ĐẲNG NHIỆT nên T "
             "không đổi, do đó v không đổi. Áp suất vẫn tăng gấp đôi, nhưng đó là do mật "
             "độ phân tử tăng chứ không phải do phân tử chuyển động nhanh hơn."),

    dict(q="Nếu tăng nhiệt độ tuyệt đối của một lượng khí lí tưởng lên 4 lần thì tốc độ "
           "căn quân phương của các phân tử khí",
         o=["tăng 2 lần.", "tăng 4 lần.", "tăng 16 lần.", "giảm 2 lần."],
         a="A",
         sol="Từ v = √(3RT/M), tốc độ căn quân phương tỉ lệ với căn bậc hai của nhiệt độ "
             "tuyệt đối. Nhiệt độ tăng 4 lần thì v tăng √4 = 2 lần. (Động năng trung bình "
             "mới là đại lượng tăng đúng 4 lần.)"),

    dict(q="Ở cùng một nhiệt độ, so sánh hai chất khí có khối lượng mol khác nhau thì phân "
           "tử của khí có khối lượng mol nhỏ hơn sẽ có",
         o=["tốc độ căn quân phương lớn hơn nhưng động năng trung bình bằng nhau.",
            "tốc độ căn quân phương và động năng trung bình đều lớn hơn.",
            "tốc độ căn quân phương nhỏ hơn nhưng động năng trung bình lớn hơn.",
            "tốc độ căn quân phương và động năng trung bình đều bằng nhau."],
         a="A",
         sol="Động năng tịnh tiến trung bình W̄ = (3/2)k_B·T chỉ phụ thuộc nhiệt độ nên hai "
             "khí ở cùng T có W̄ bằng nhau. Nhưng W̄ = m₀v̄²/2, nên phân tử nhẹ hơn phải có "
             "tốc độ lớn hơn để cùng động năng đó: v = √(3RT/M) tỉ lệ nghịch với √M."),

    dict(q="Vẫn với chu trình trong hình vẽ ở Câu 6, quá trình P → M là",
         fig="t24c",
         o=["quá trình đẳng áp, khí bị nén và nhiệt độ giảm.",
            "quá trình đẳng nhiệt, khí bị nén và áp suất tăng.",
            "quá trình đẳng tích, khí toả nhiệt và áp suất giảm.",
            "quá trình vừa giảm áp suất vừa tăng thể tích của khí."],
         a="A",
         sol="P(600 K; 4 lít) và M(300 K; 2 lít) có V/T bằng nhau: 4/600 = 2/300 = 1/150. "
             "Theo định luật Charles đó là quá trình ĐẲNG ÁP. Đoạn PM trên hình đúng là "
             "một đoạn thẳng mà đường kéo dài đi qua gốc toạ độ. Thể tích giảm (khí bị "
             "nén) và nhiệt độ giảm từ 600 K xuống 300 K."),

    dict(q="Tốc độ căn quân phương của phân tử khí oxygen (khối lượng mol 32 g/mol) ở "
           "300 K xấp xỉ",
         o=["483 m/s.", "137 m/s.", "1367 m/s.", "234 m/s."],
         a="A",
         sol="v = √(3RT/M) = √(3 × 8,31 × 300/0,032) = √(7479/0,032) = √233 719 "
             "≈ 483 m/s.\n"
             "Chú ý đổi khối lượng mol sang kg/mol: 32 g/mol = 0,032 kg/mol. Nếu quên đổi "
             "sẽ ra kết quả lớn hơn khoảng 31,6 lần."),

    dict(q="Động năng tịnh tiến trung bình của một phân tử khí lí tưởng ở 27 °C xấp xỉ",
         o=["6,21·10⁻²¹ J.", "5,59·10⁻²² J.",
            "4,14·10⁻²¹ J.", "3,74·10³ J."],
         a="A",
         sol="T = 300 K. W̄ = (3/2)k_B·T = 1,5 × 1,38·10⁻²³ × 300 = 6,21·10⁻²¹ J. Giá trị "
             "3,74·10³ J chính là nội năng của 1 mol khí đơn nguyên tử ở nhiệt độ đó, khác "
             "hẳn về bậc độ lớn."),

    dict(q="Hình vẽ là một xi lanh nằm ngang, hai đầu kín, có một pit-tông mỏng không ma "
           "sát ngăn thành hai phần: khí A dài ℓ₁ = 40 cm ở áp suất 1,0·10⁵ Pa và khí B "
           "dài ℓ₂ = 20 cm; cả hai cùng ở 300 K. Áp suất của khí B bằng",
         fig="t24b",
         o=["1,0·10⁵ Pa.", "2,0·10⁵ Pa.", "0,5·10⁵ Pa.", "4,0·10⁵ Pa."],
         a="A",
         sol="Pit-tông mỏng, nhẹ, không ma sát và đang đứng yên nên hai lực ép lên hai mặt "
             "của nó phải cân bằng. Cùng tiết diện S nên p_A·S = p_B·S ⇒ p_B = p_A = "
             "1,0·10⁵ Pa.\n"
             "Sai lầm rất phổ biến là nghĩ áp suất tỉ lệ nghịch với chiều dài mà suy ra "
             "2,0·10⁵ Pa; điều đó chỉ đúng khi hai bên là CÙNG một lượng khí biến đổi đẳng "
             "nhiệt, còn ở đây là hai lượng khí độc lập."),

    dict(q="Vẫn với xi lanh nói trên. Đun nóng khí B lên 360 K trong khi giữ khí A ở "
           "300 K. Pit-tông dịch chuyển một đoạn bằng",
         fig="t24b",
         o=["2,5 cm về phía khí A.", "2,5 cm về phía khí B.",
            "5,0 cm về phía khí A.", "4,0 cm về phía khí A."],
         a="A",
         sol="Gọi x là độ dịch chuyển của pit-tông về phía khí A. Khi cân bằng, áp suất "
             "hai bên bằng nhau.\n"
             "Khí A (đẳng nhiệt 300 K): p = 1,0·10⁵ × 40/(40 − x).\n"
             "Khí B (300 K → 360 K): p = 1,0·10⁵ × [20/(20 + x)] × (360/300) = "
             "1,0·10⁵ × 24/(20 + x).\n"
             "Cho bằng nhau: 40(20 + x) = 24(40 − x) ⇒ 800 + 40x = 960 − 24x ⇒ 64x = 160 "
             "⇒ x = 2,5 cm. Khí B nóng lên nên nó nở ra và đẩy pit-tông về phía khí A."),

    dict(q="Nội năng của 1,0 mol khí lí tưởng đơn nguyên tử ở 300 K, tính theo công thức "
           "U = (3/2)nRT, xấp xỉ",
         o=["3,74 kJ.", "2,49 kJ.", "1,25 kJ.", "7,48 kJ."],
         a="A",
         sol="U = 1,5 × 1,0 × 8,31 × 300 = 3739,5 J ≈ 3,74 kJ. Với khí lí tưởng đơn nguyên "
             "tử, toàn bộ nội năng chính là tổng động năng tịnh tiến của các phân tử nên "
             "nó chỉ phụ thuộc nhiệt độ và số mol."),

    dict(q="Hai bình giống hệt nhau được nối bằng một ống nhỏ có khoá. Ban đầu khoá đóng: "
           "bình thứ nhất chứa khí ở 3,0·10⁵ Pa, bình thứ hai chứa cùng loại khí ở "
           "1,0·10⁵ Pa, cả hai cùng nhiệt độ. Mở khoá và giữ nhiệt độ không đổi thì áp "
           "suất chung là",
         o=["2,0·10⁵ Pa.", "4,0·10⁵ Pa.", "1,5·10⁵ Pa.", "3,0·10⁵ Pa."],
         a="A",
         sol="Ở nhiệt độ không đổi, tổng tích pV bảo toàn. Gọi V là thể tích mỗi bình:\n"
             "p(2V) = 3,0·10⁵·V + 1,0·10⁵·V = 4,0·10⁵·V ⇒ p = 2,0·10⁵ Pa.\n"
             "Vì hai bình bằng nhau nên kết quả đúng bằng trung bình cộng của hai áp suất "
             "ban đầu; nếu hai bình khác thể tích thì phải lấy trung bình có trọng số theo "
             "thể tích."),

    dict(q="Vẫn với lượng khí trong đồ thị p – 1/V ở Câu 4. Khi thể tích của khí là 2,5 "
           "lít thì áp suất của nó bằng",
         fig="t24a",
         o=["1,2 atm.", "0,83 atm.", "7,5 atm.", "2,5 atm."],
         a="A",
         sol="Hệ số góc của đồ thị cho pV = 3,0 atm·lít.\n"
             "Khi V = 2,5 lít: p = 3,0/2,5 = 1,2 atm."),

    dict(q="Một bình kín chứa khí lí tưởng ở 27 °C. Muốn động năng tịnh tiến trung bình "
           "của các phân tử khí tăng gấp đôi thì phải nung nóng khí tới",
         o=["327 °C.", "54 °C.", "600 °C.", "273 °C."],
         a="A",
         sol="W̄ = (3/2)k_B·T tỉ lệ thuận với nhiệt độ TUYỆT ĐỐI. Muốn W̄ tăng gấp đôi thì T "
             "phải tăng gấp đôi: T₂ = 2 × 300 = 600 K, tức t₂ = 600 − 273 = 327 °C.\n"
             "Đáp án 54 °C là bẫy do nhân đôi nhiệt độ Celsius; đáp án 600 °C là do quên "
             "đổi ngược 600 K về thang Celsius."),
]

DE4_P2 = [
    dict(stem="Hình vẽ là kết quả thí nghiệm khảo sát định luật Boyle với một lượng khí "
              "xác định ở nhiệt độ không đổi, được biểu diễn dưới dạng áp suất p theo 1/V.",
         fig="t24a",
         items=[
             ("Các điểm thực nghiệm nằm gần một đường thẳng, điều đó chứng tỏ áp suất tỉ "
              "lệ thuận với thể tích.", False,
              "Đại lượng đặt trên trục hoành là 1/V chứ không phải V. Đường thẳng qua gốc "
              "toạ độ trong hệ (1/V; p) nghĩa là p tỉ lệ thuận với 1/V, tức p tỉ lệ NGHỊCH "
              "với V. Nếu p tỉ lệ thuận với V thì đồ thị p theo 1/V phải là một nhánh "
              "hypebol."),
             ("Hệ số góc của đường thẳng là 3,0 atm·lít và bằng đúng tích pV của lượng "
              "khí.", True,
              "Từ p = k·(1/V) suy ra k = pV. Đọc trên đồ thị tại 1/V = 1,0 L⁻¹ ta được "
              "p = 3,0 atm, vậy k = 3,0 atm·lít. Có thể kiểm tra lại với điểm khác: "
              "1/V = 0,50 L⁻¹ cho p = 1,5 atm, tích vẫn bằng 3,0."),
             ("Khi thể tích của khí là 5,0 lít thì áp suất của nó là 1,5 atm.", False,
              "p = 3,0/V = 3,0/5,0 = 0,60 atm. Giá trị 1,5 atm ứng với V = 2,0 lít chứ "
              "không phải 5,0 lít."),
             ("Nếu lặp lại thí nghiệm với cùng lượng khí đó ở nhiệt độ cao hơn thì đồ thị "
              "vẫn là đường thẳng nhưng có hệ số góc lớn hơn.", True,
              "Ở nhiệt độ cao hơn, pV = nRT vẫn là hằng số (nên vẫn là đường thẳng qua gốc "
              "toạ độ) nhưng hằng số đó lớn hơn vì T lớn hơn. Do đó hệ số góc lớn hơn, "
              "đường thẳng dốc hơn."),
         ]),

    dict(stem="Một lượng khí lí tưởng xác định biến đổi theo chu trình M → N → P → M được "
              "biểu diễn trong hệ toạ độ (T, V) như hình vẽ.",
         fig="t24c",
         items=[
             ("Quá trình M → N là quá trình đẳng nhiệt; thể tích tăng gấp đôi nên áp suất "
              "giảm một nửa.", True,
              "M(300 K; 2 lít) và N(300 K; 4 lít) có cùng nhiệt độ nên đây là quá trình "
              "đẳng nhiệt. Theo định luật Boyle, V tăng gấp đôi thì p giảm một nửa."),
             ("Quá trình N → P là quá trình đẳng áp.", False,
              "N(300 K; 4 lít) và P(600 K; 4 lít) có cùng THỂ TÍCH nên đó là quá trình "
              "ĐẲNG TÍCH; áp suất tăng gấp đôi vì nhiệt độ tăng gấp đôi."),
             ("Quá trình P → M là quá trình đẳng áp, trong đó khí bị nén và nhiệt độ giảm.",
              True,
              "Kiểm tra thương V/T: tại P là 4/600 = 1/150, tại M là 2/300 = 1/150 — bằng "
              "nhau, đúng là đẳng áp. Trên hình, PM là đoạn thẳng mà đường kéo dài đi qua "
              "gốc toạ độ. Thể tích giảm từ 4 lít xuống 2 lít và nhiệt độ giảm từ 600 K "
              "xuống 300 K."),
             ("Áp suất của khí ở trạng thái P lớn gấp 4 lần áp suất ở trạng thái N.", False,
              "p tỉ lệ với T/V. Tại N: 300/4 = 75 (đơn vị tuỳ ý); tại P: 600/4 = 150. Vậy "
              "p_P chỉ gấp 2 lần p_N chứ không phải 4 lần — thể tích của hai trạng thái "
              "này bằng nhau nên chỉ có nhiệt độ (tăng 2 lần) quyết định."),
         ]),

    dict(stem="Hình vẽ là một xi lanh nằm ngang, hai đầu kín, tiết diện đều, có một "
              "pit-tông mỏng không ma sát chia thành hai phần: khí A dài 40 cm và khí B "
              "dài 20 cm, cả hai cùng ở 300 K; áp suất của khí A là 1,0·10⁵ Pa.",
         fig="t24b",
         items=[
             ("Áp suất của khí B cũng bằng 1,0·10⁵ Pa.", True,
              "Pit-tông nhẹ, không ma sát và đang cân bằng nên áp suất hai bên phải bằng "
              "nhau, bất kể chiều dài hai cột khí có khác nhau bao nhiêu."),
             ("Khí A và khí B có cùng số mol vì chúng có cùng áp suất và cùng nhiệt độ.",
              False,
              "Cùng p và T thì số mol tỉ lệ THUẬN với thể tích (pV = nRT). Khí A chiếm "
              "chiều dài gấp đôi khí B nên có số mol gấp đôi, tức n_A = 2n_B."),
             ("Nếu đun nóng khí B lên 360 K và giữ khí A ở 300 K thì pit-tông dịch về phía "
              "khí A một đoạn 2,5 cm.", True,
              "Điều kiện cân bằng cho áp suất hai bên bằng nhau. Với x là độ dịch về phía "
              "A:\n"
              "40/(40 − x) = [20/(20 + x)] × (360/300) = 24/(20 + x)\n"
              "⇒ 40(20 + x) = 24(40 − x) ⇒ 64x = 160 ⇒ x = 2,5 cm."),
             ("Nếu đun nóng đồng thời cả hai khí lên 360 K thì pit-tông dịch về phía khí "
              "B.", False,
              "Nếu pit-tông đứng yên thì cả hai phần đều biến đổi đẳng tích và áp suất mỗi "
              "bên đều tăng theo cùng tỉ lệ 360/300 = 1,2 lần, tức vẫn bằng nhau. Vậy "
              "trạng thái “pit-tông đứng yên” đã thoả mãn điều kiện cân bằng: pit-tông "
              "không dịch chuyển."),
         ]),

    dict(stem="Xét khí nitrogen (khối lượng mol 28 g/mol) ở nhiệt độ 27 °C, với "
              "R = 8,31 J/(mol·K), k_B = 1,38·10⁻²³ J/K.",
         items=[
             ("Động năng tịnh tiến trung bình của một phân tử nitrogen là 6,21·10⁻²¹ J.",
              True,
              "T = 27 + 273 = 300 K, do đó W̄ = (3/2)k_B·T = 1,5 × 1,38·10⁻²³ × 300 "
              "= 6,21·10⁻²¹ J. Giá trị này như nhau với mọi chất khí ở cùng nhiệt độ, "
              "hoàn toàn không phụ thuộc khối lượng mol của khí."),
             ("Tốc độ căn quân phương của phân tử nitrogen xấp xỉ 517 m/s.", True,
              "v = √(3RT/M) = √(3 × 8,31 × 300/0,028) = √(7479/0,028) = √267 107 "
              "≈ 516,8 m/s ≈ 517 m/s."),
             ("Nếu tăng nhiệt độ lên 127 °C thì động năng tịnh tiến trung bình của phân tử "
              "tăng gấp đôi.", False,
              "T tăng từ 300 K lên 400 K, tức chỉ gấp 4/3 lần, nên W̄ cũng chỉ tăng 4/3 "
              "lần (khoảng 33 %). Muốn W̄ tăng gấp đôi phải đưa nhiệt độ lên 600 K."),
             ("Ở cùng 27 °C, phân tử hydrogen (khối lượng mol 2 g/mol) có động năng tịnh "
              "tiến trung bình lớn hơn phân tử nitrogen.", False,
              "W̄ = (3/2)k_B·T chỉ phụ thuộc nhiệt độ, hoàn toàn không phụ thuộc khối lượng "
              "mol, nên hai loại phân tử có W̄ BẰNG nhau. Điều khác nhau là TỐC ĐỘ: phân tử "
              "hydrogen nhẹ hơn 14 lần nên có tốc độ căn quân phương lớn hơn √14 ≈ 3,7 "
              "lần."),
         ]),
]

DE4_P3 = [
    dict(q="Tính tốc độ căn quân phương của phân tử khí helium (khối lượng mol 4,0 g/mol) "
           "ở 27 °C (theo m/s, làm tròn đến hàng đơn vị).",
         ans="1367",
         sol="v = √(3RT/M) với T = 300 K và M = 4,0·10⁻³ kg/mol.\n"
             "v = √(3 × 8,31 × 300/0,0040) = √(7479/0,0040) = √1 869 750 ≈ 1367 m/s.\n"
             "Helium rất nhẹ nên tốc độ phân tử của nó lớn hơn hẳn các khí thông thường — "
             "đó cũng là lí do helium dễ thoát khỏi khí quyển Trái Đất."),

    dict(q="Tính động năng tịnh tiến trung bình của một phân tử khí lí tưởng ở 127 °C "
           "(theo 10⁻²¹ J, làm tròn đến hàng phần trăm).",
         ans="8,28",
         sol="T = 127 + 273 = 400 K.\n"
             "W̄ = (3/2)k_B·T = 1,5 × 1,38·10⁻²³ × 400 = 8,28·10⁻²¹ J.\n"
             "Vậy kết quả cần điền là 8,28."),

    dict(q="Vẫn với lượng khí trong đồ thị p – 1/V ở Câu 4. Tính thể tích của lượng khí đó "
           "khi áp suất của nó là 2,0 atm (theo lít, làm tròn đến hàng phần mười).",
         fig="t24a",
         ans="1,5",
         sol="Hệ số góc của đồ thị cho pV = 3,0 atm·lít (hằng số Boyle của lượng khí ở "
             "nhiệt độ đang xét).\n"
             "V = 3,0/p = 3,0/2,0 = 1,5 lít."),

    dict(q="Một xi lanh nằm ngang, hai đầu kín, có pit-tông mỏng không ma sát chia thành "
           "hai phần: khí A dài 40 cm và khí B dài 20 cm, cả hai cùng ở 300 K và cùng áp "
           "suất. Đun nóng khí A lên 450 K trong khi giữ khí B ở 300 K. Tính độ dịch "
           "chuyển của pit-tông (theo cm, làm tròn đến hàng phần mười).",
         fig="t24b",
         ans="5,0",
         sol="Gọi x là độ dịch chuyển của pit-tông về phía khí B. Khi cân bằng, áp suất "
             "hai bên bằng nhau; gọi p₀ là áp suất ban đầu chung.\n"
             "Khí A (300 K → 450 K, dài ra thành 40 + x):\n"
             "p = p₀ × [40/(40 + x)] × (450/300) = p₀ × 60/(40 + x).\n"
             "Khí B (đẳng nhiệt 300 K, ngắn lại còn 20 − x): p = p₀ × 20/(20 − x).\n"
             "Cho bằng nhau: 60(20 − x) = 20(40 + x) ⇒ 1200 − 60x = 800 + 20x ⇒ 80x = 400 "
             "⇒ x = 5,0 cm."),

    dict(q="Tính nội năng của 2,0 mol khí lí tưởng đơn nguyên tử ở 27 °C theo công thức "
           "U = (3/2)nRT. (Kết quả theo kJ, làm tròn đến hàng phần trăm.)",
         ans="7,48",
         sol="T = 300 K.\n"
             "U = 1,5 × 2,0 × 8,31 × 300 = 7479 J = 7,479 kJ ≈ 7,48 kJ."),

    dict(q="Hai bình có thể tích 3,0 lít và 2,0 lít được nối với nhau bằng một ống nhỏ có "
           "khoá. Bình lớn chứa khí ở 4,0·10⁵ Pa, bình nhỏ chứa cùng loại khí ở 1,5·10⁵ "
           "Pa, cả hai cùng nhiệt độ. Mở khoá và giữ nhiệt độ không đổi. Tính áp suất "
           "chung (theo 10⁵ Pa, làm tròn đến hàng phần mười).",
         ans="3,0",
         sol="Nhiệt độ không đổi nên tổng tích pV được bảo toàn:\n"
             "p × (3,0 + 2,0) = 4,0·10⁵ × 3,0 + 1,5·10⁵ × 2,0 = (12 + 3,0)·10⁵ = 15·10⁵\n"
             "p = 15·10⁵/5,0 = 3,0·10⁵ Pa.\n"
             "Kết quả nằm giữa hai áp suất ban đầu và lệch về phía bình lớn — hợp lí."),
]

DE4 = dict(code="C2-04", so="04", chuong=2,
           title="ĐỀ KIỂM TRA CHƯƠNG II – ĐỀ SỐ 04",
           subtitle="Chương II – Khí lí tưởng",
           p1=DE4_P1, p2=DE4_P2, p3=DE4_P3)


# ===================================================================================
#          ĐỀ SỐ 05 – TỔNG HỢP TOÀN CHƯƠNG, PHÂN HOÁ CAO
# ===================================================================================

DE5_P1 = [
    dict(q="Phát biểu nào sau đây về khí lí tưởng là SAI?",
         o=["Khí lí tưởng chỉ tồn tại ở nhiệt độ rất thấp và áp suất rất lớn.",
            "Phân tử khí lí tưởng có kích thước rất nhỏ so với khoảng cách giữa chúng.",
            "Các phân tử khí lí tưởng chỉ tương tác với nhau khi chúng va chạm.",
            "Va chạm của phân tử khí lí tưởng với thành bình là va chạm đàn hồi."],
         a="A",
         sol="Khí lí tưởng là một MÔ HÌNH; khí thực càng gần mô hình đó khi càng loãng, "
             "tức khi áp suất KHÔNG quá lớn và nhiệt độ KHÔNG quá thấp. Ở nhiệt độ rất "
             "thấp và áp suất rất lớn, các phân tử ở gần nhau, lực tương tác trở nên quan "
             "trọng và mô hình sai lệch mạnh. Ba phát biểu còn lại đều là giả thuyết đúng "
             "của mô hình."),

    dict(q="Biểu thức p = (1/3)·(N/V)·m₀·v̄² cho thấy áp suất của chất khí phụ thuộc vào",
         o=["mật độ phân tử và động năng trung bình của phân tử khí.",
            "chỉ riêng mật độ phân tử của chất khí trong bình.",
            "chỉ riêng khối lượng của mỗi phân tử chất khí đó.",
            "thể tích của bình chứa và khối lượng mol của chất khí."],
         a="A",
         sol="Có thể viết lại p = (2/3)·(N/V)·(m₀v̄²/2) = (2/3)·(N/V)·W̄: áp suất bằng hai "
             "phần ba tích của MẬT ĐỘ phân tử N/V với ĐỘNG NĂNG TỊNH TIẾN TRUNG BÌNH của "
             "một phân tử. Đây là cầu nối giữa mô hình vi mô và các đại lượng vĩ mô đo "
             "được."),

    dict(q="Nội năng của một lượng khí lí tưởng đơn nguyên tử xác định",
         o=["chỉ phụ thuộc vào nhiệt độ của khí.",
            "chỉ phụ thuộc vào thể tích của khí.",
            "phụ thuộc vào cả nhiệt độ và thể tích của khí.",
            "phụ thuộc vào áp suất nhưng không phụ thuộc nhiệt độ."],
         a="A",
         sol="Ở khí lí tưởng, lực tương tác giữa các phân tử được bỏ qua nên thế năng "
             "tương tác bằng không; nội năng chỉ còn là tổng động năng chuyển động nhiệt: "
             "U = (3/2)nRT. Vì n cố định, U chỉ phụ thuộc T. Đó là điểm khác biệt quan "
             "trọng so với chất lỏng và chất rắn."),

    dict(q="Hình vẽ biểu diễn hai quá trình I và II cùng đưa một lượng khí lí tưởng từ "
           "trạng thái (1) sang trạng thái (2). Kết luận nào sau đây là đúng?",
         fig="t25d",
         o=["Độ biến thiên nội năng của khí trong hai quá trình là như nhau.",
            "Độ biến thiên nội năng trong quá trình I lớn hơn trong quá trình II.",
            "Trong quá trình II khí không hề trao đổi nhiệt với môi trường bên ngoài.",
            "Hai quá trình phải có cùng nhiệt lượng trao đổi vì cùng điểm đầu và cuối."],
         a="A",
         sol="Nội năng là một HÀM TRẠNG THÁI: giá trị của nó chỉ phụ thuộc trạng thái hiện "
             "tại chứ không phụ thuộc con đường đã đi. Hai quá trình có cùng trạng thái "
             "đầu và cùng trạng thái cuối nên ΔU bằng nhau. Trái lại, công A và nhiệt "
             "lượng Q phụ thuộc đường đi nên nói chung khác nhau giữa hai quá trình."),

    dict(q="Hình vẽ là phân bố tốc độ phân tử của cùng một lượng khí ở hai nhiệt độ "
           "T₁ = 300 K và T₂ = 700 K. So với đường ứng với T₁, đường ứng với T₂ có",
         fig="t25b",
         o=["đỉnh thấp hơn, dịch về phía tốc độ lớn và đường cong trải rộng hơn.",
            "đỉnh cao hơn, dịch về phía tốc độ lớn và đường cong hẹp lại.",
            "đỉnh cao hơn, dịch về phía tốc độ nhỏ và đường cong trải rộng hơn.",
            "hình dạng hoàn toàn giống hệt, chỉ tịnh tiến lên phía trên."],
         a="A",
         sol="Khi nhiệt độ tăng, các phân tử nhìn chung chuyển động nhanh hơn nên đỉnh của "
             "đường phân bố dịch về phía tốc độ lớn, đồng thời dải tốc độ trải rộng ra. Vì "
             "TỔNG số phân tử không đổi (diện tích dưới hai đường bằng nhau) nên đường "
             "trải rộng hơn buộc phải có đỉnh thấp hơn."),

    dict(q="Một bóng thám không bay lên cao thì thể tích của nó tăng lên. Nguyên nhân "
           "chính là",
         o=["áp suất khí quyển giảm nhanh hơn mức giảm của nhiệt độ theo độ cao.",
            "nhiệt độ không khí trên cao tăng lên làm khí trong bóng nở ra.",
            "khối lượng khí bên trong bóng tăng lên khi bóng bay lên cao.",
            "vỏ bóng bị lạnh nên co lại và ép cho khí bên trong nở ra."],
         a="A",
         sol="Theo pV/T = hằng số, V = (hằng số)·T/p. Lên cao, cả p và T đều giảm nhưng áp "
             "suất giảm nhanh hơn nhiều (có thể còn vài phần mười) trong khi nhiệt độ "
             "tuyệt đối chỉ giảm khoảng 20 – 25 %. Kết quả là thương T/p tăng, thể tích "
             "bóng tăng — đó là lí do bóng thám không được bơm rất non khi thả."),

    dict(q="Cho một lượng khí lí tưởng dãn nở đẳng nhiệt tới thể tích gấp ba lần ban đầu. "
           "Phát biểu nào sau đây là đúng?",
         o=["Áp suất giảm ba lần còn động năng trung bình của phân tử không đổi.",
            "Áp suất giảm ba lần và động năng trung bình của phân tử cũng giảm ba lần.",
            "Áp suất không đổi còn động năng trung bình của phân tử giảm ba lần.",
            "Áp suất giảm ba lần còn tốc độ căn quân phương của phân tử giảm √3 lần."],
         a="A",
         sol="Đẳng nhiệt nên pV = hằng số: thể tích tăng ba lần thì áp suất giảm ba lần. "
             "Mặt khác W̄ = (3/2)k_B·T và v = √(3RT/M) chỉ phụ thuộc nhiệt độ, mà T không "
             "đổi, nên cả động năng trung bình lẫn tốc độ căn quân phương đều giữ nguyên. "
             "Áp suất giảm là do mật độ phân tử N/V giảm, tức số va chạm lên thành bình "
             "trong mỗi giây giảm, chứ không phải do phân tử chậm lại."),

    dict(q="Hai bình có thể tích bằng nhau, cùng nhiệt độ, một bình chứa khí hydrogen, một "
           "bình chứa khí oxygen với cùng số mol. Khi đó",
         o=["áp suất hai bình bằng nhau nhưng tốc độ căn quân phương của phân tử hydrogen "
            "lớn hơn.",
            "áp suất bình hydrogen lớn hơn vì phân tử hydrogen chuyển động nhanh hơn.",
            "áp suất bình oxygen lớn hơn vì phân tử oxygen có khối lượng lớn hơn.",
            "áp suất hai bình bằng nhau và tốc độ căn quân phương của phân tử cũng bằng "
            "nhau."],
         a="A",
         sol="Từ pV = nRT: cùng n, V, T thì p bằng nhau, không phụ thuộc loại khí. Nhưng "
             "v = √(3RT/M) tỉ lệ nghịch với √M: hydrogen có M = 2 g/mol, oxygen có "
             "M = 32 g/mol, nên phân tử hydrogen nhanh hơn √16 = 4 lần. Hai hiệu ứng “phân "
             "tử nhẹ hơn nhưng nhanh hơn” bù trừ nhau đúng bằng nhau nên áp suất như "
             "nhau."),

    dict(q="Hình vẽ là chu trình (1) → (2) → (3) → (4) → (1) của một lượng khí lí tưởng. "
           "Trạng thái nào có nhiệt độ cao nhất?",
         fig="t25a",
         o=["Trạng thái (3).", "Trạng thái (1).",
            "Trạng thái (2).", "Trạng thái (4)."],
         a="A",
         sol="Với một lượng khí xác định, T tỉ lệ thuận với tích pV. Tính tích đó cho từng "
             "trạng thái (đơn vị atm·lít):\n"
             "(1): 1 × 1 = 1;  (2): 4 × 1 = 4;  (3): 4 × 4 = 16;  (4): 1 × 4 = 4.\n"
             "Vậy trạng thái (3) có tích pV lớn nhất nên nhiệt độ cao nhất."),

    dict(q="Vẫn với chu trình trong hình vẽ đó. Nếu nhiệt độ ở trạng thái (1) là 300 K thì "
           "nhiệt độ ở trạng thái (3) bằng",
         fig="t25a",
         o=["4800 K.", "1200 K.", "2400 K.", "300 K."],
         a="A",
         sol="T tỉ lệ thuận với pV nên T₃ = T₁ × (p₃V₃)/(p₁V₁) = 300 × (4 × 4)/(1 × 1) = "
             "300 × 16 = 4800 K."),

    dict(q="Một bóng thám không có thể tích 8,0 m³ ở mặt đất, nơi có áp suất 1,0·10⁵ Pa và "
           "nhiệt độ 300 K. Ở độ cao mà áp suất chỉ còn 0,40·10⁵ Pa và nhiệt độ là 240 K, "
           "thể tích của bóng bằng",
         fig="t25c",
         o=["16 m³.", "20 m³.", "25 m³.", "6,4 m³."],
         a="A",
         sol="V₂ = V₁ × (p₁/p₂) × (T₂/T₁) = 8,0 × (1,0/0,40) × (240/300) = "
             "8,0 × 2,50 × 0,80 = 16 m³."),

    dict(q="Trong hình vẽ, quá trình II gồm một đoạn đẳng tích rồi một đoạn đẳng áp, đi "
           "qua trạng thái trung gian (3) có p = 1,0 atm và V = 1,0 lít. So với nhiệt độ ở "
           "trạng thái (1), nhiệt độ ở trạng thái (3)",
         fig="t25d",
         o=["nhỏ hơn 4 lần.", "lớn hơn 4 lần.", "nhỏ hơn 2 lần.", "bằng nhau."],
         a="A",
         sol="T tỉ lệ thuận với tích pV. Trạng thái (1): 4,0 × 1,0 = 4,0 atm·lít; trạng "
             "thái (3): 1,0 × 1,0 = 1,0 atm·lít.\n"
             "Vậy T₃ = T₁/4, tức nhỏ hơn 4 lần. Trạng thái (3) là điểm lạnh nhất của cả "
             "quá trình II."),

    dict(q="Tốc độ căn quân phương của phân tử một chất khí ở 27 °C là 500 m/s. Ở nhiệt độ "
           "nào thì tốc độ đó bằng 1000 m/s?",
         o=["927 °C.", "327 °C.", "600 °C.", "1200 °C."],
         a="A",
         sol="v tỉ lệ với √T nên T₂/T₁ = (v₂/v₁)² = 2² = 4.\n"
             "T₂ = 4 × 300 = 1200 K ⇒ t₂ = 1200 − 273 = 927 °C.\n"
             "Bẫy ở đây là quên đổi 1200 K về thang Celsius (ra 1200 °C) hoặc nhân đôi "
             "nhiệt độ thay vì nhân bốn (ra 327 °C)."),

    dict(q="Một bình thép kín có dung tích 5,0 lít được nạp 3,2 g khí oxygen (khối lượng "
           "mol 32 g/mol). Ở nhiệt độ 127 °C, áp suất khí trong bình xấp xỉ",
         o=["6,65·10⁴ Pa.", "6,65·10⁵ Pa.", "1,66·10⁵ Pa.", "4,99·10⁴ Pa."],
         a="A",
         sol="n = m/M = 3,2/32 = 0,10 mol; T = 400 K; V = 5,0·10⁻³ m³.\n"
             "p = nRT/V = (0,10 × 8,31 × 400)/(5,0·10⁻³) = 332,4/0,0050 = 66 480 Pa "
             "≈ 6,65·10⁴ Pa."),

    dict(q="Một xi lanh thẳng đứng, đầu hở lên trên, có pit-tông khối lượng 2,0 kg và tiết "
           "diện 50 cm² giam một cột khí bên dưới. Áp suất khí quyển là 1,0·10⁵ Pa và "
           "g = 10 m/s². Áp suất của khí trong xi lanh bằng",
         o=["1,04·10⁵ Pa.", "0,96·10⁵ Pa.", "1,40·10⁵ Pa.", "1,00·10⁵ Pa."],
         a="A",
         sol="Pit-tông cân bằng dưới tác dụng của: áp lực khí bên dưới đẩy lên, áp lực khí "
             "quyển ép xuống và trọng lượng của chính nó.\n"
             "p·S = p₀·S + mg ⇒ p = p₀ + mg/S = 1,0·10⁵ + (2,0 × 10)/(50·10⁻⁴)\n"
             "  = 1,0·10⁵ + 20/0,0050 = 1,0·10⁵ + 4000 = 1,04·10⁵ Pa.\n"
             "Chú ý đổi tiết diện: 50 cm² = 50·10⁻⁴ m²."),

    dict(q="Một lượng khí lí tưởng ở 300 K có áp suất 2,0·10⁵ Pa. Người ta làm cho thể "
           "tích của khí giảm 25 % đồng thời nâng nhiệt độ lên 400 K. Áp suất của khí lúc "
           "này xấp xỉ",
         o=["3,56·10⁵ Pa.", "2,67·10⁵ Pa.", "2,00·10⁵ Pa.", "4,00·10⁵ Pa."],
         a="A",
         sol="Thể tích giảm 25 % nghĩa là V₂ = 0,75·V₁.\n"
             "p₂ = p₁ × (V₁/V₂) × (T₂/T₁) = 2,0·10⁵ × (1/0,75) × (400/300)\n"
             "  = 2,0·10⁵ × 1,333 × 1,333 ≈ 3,56·10⁵ Pa."),

    dict(q="Một quả bóng cao su có thể tích 3,0 lít chứa khí ở 1,2·10⁵ Pa và 300 K. Bơm "
           "thêm khí cùng loại vào bóng cho tới khi áp suất là 1,8·10⁵ Pa, thể tích 3,5 "
           "lít và nhiệt độ 310 K. Tỉ số giữa số mol khí trong bóng sau và trước khi bơm "
           "xấp xỉ",
         o=["1,69.", "1,50.", "1,75.", "1,45."],
         a="A",
         sol="Từ pV = nRT suy ra n = pV/(RT), nên n tỉ lệ thuận với thương pV/T.\n"
             "Trước khi bơm: (1,2 × 3,0)/300 = 3,6/300 = 0,0120.\n"
             "Sau khi bơm: (1,8 × 3,5)/310 = 6,3/310 ≈ 0,02032.\n"
             "Tỉ số: 0,02032/0,0120 ≈ 1,69.\n"
             "Nếu chỉ so sánh áp suất (1,8/1,2 = 1,5) thì đã bỏ sót cả sự thay đổi thể "
             "tích lẫn nhiệt độ."),

    dict(q="Một bình kín thể tích không đổi chứa khí lí tưởng. Nếu tăng nhiệt độ tuyệt đối "
           "của khí thêm 25 % và đồng thời rút bớt 20 % số phân tử khí ra khỏi bình thì áp "
           "suất của khí trong bình sẽ",
         o=["không thay đổi.", "tăng 5 %.", "giảm 5 %.", "tăng 25 %."],
         a="A",
         sol="Thể tích không đổi nên từ pV = Nk_BT suy ra p tỉ lệ thuận với tích N·T.\n"
             "N giảm còn 0,80 lần; T tăng thành 1,25 lần.\n"
             "Tỉ số áp suất: 0,80 × 1,25 = 1,00, tức áp suất giữ nguyên. Hai tác động đúng "
             "bằng nhau và ngược chiều nên triệt tiêu."),
]

DE5_P2 = [
    dict(stem="Một lượng khí lí tưởng xác định thực hiện chu trình (1) → (2) → (3) → (4) → "
              "(1) như hình vẽ. Ở trạng thái (1) khí có p = 1,0 atm, V = 1,0 lít và "
              "T = 300 K.",
         fig="t25a",
         items=[
             ("Quá trình (1) → (2) là quá trình đẳng áp, trong đó nhiệt độ tăng lên 1200 K.",
              False,
              "Trên hình, (1) và (2) có cùng thể tích 1,0 lít nên đó là quá trình ĐẲNG "
              "TÍCH chứ không phải đẳng áp. Nhiệt độ thì đúng là tăng lên "
              "T₂ = 300 × 4/1 = 1200 K vì áp suất tăng 4 lần."),
             ("Quá trình (2) → (3) là quá trình đẳng áp, trong đó nhiệt độ tăng lên 4800 K.",
              True,
              "(2) và (3) cùng có p = 4 atm nên là quá trình đẳng áp. Thể tích tăng từ "
              "1,0 lên 4,0 lít nên T₃ = T₂ × 4,0/1,0 = 1200 × 4 = 4800 K."),
             ("Trạng thái (4) có nhiệt độ bằng trạng thái (2).", True,
              "Tích pV tại (2) là 4 × 1 = 4 atm·lít và tại (4) là 1 × 4 = 4 atm·lít. Với "
              "cùng lượng khí, pV bằng nhau kéo theo nhiệt độ bằng nhau: T₂ = T₄ = 1200 K. "
              "Vậy (2) và (4) nằm trên cùng một đường đẳng nhiệt."),
             ("Trong cả chu trình, trạng thái (1) có nhiệt độ thấp nhất và trạng thái (4) "
              "có nhiệt độ cao nhất.", False,
              "Trạng thái (1) đúng là lạnh nhất (pV = 1), nhưng trạng thái nóng nhất là "
              "(3) với pV = 16 chứ không phải (4) với pV = 4."),
         ]),

    dict(stem="Hình vẽ là đường phân bố tốc độ phân tử của cùng một lượng khí ở hai nhiệt "
              "độ T₁ = 300 K và T₂ = 700 K.",
         fig="t25b",
         items=[
             ("Ở nhiệt độ cao hơn, số phân tử có tốc độ lớn tăng lên.", True,
              "Phần đuôi bên phải của đường T₂ nằm cao hơn hẳn đường T₁, cho thấy tỉ lệ "
              "phân tử chuyển động rất nhanh tăng lên đáng kể khi đun nóng. Đây là cơ sở "
              "để giải thích vì sao tốc độ bay hơi và tốc độ phản ứng hoá học tăng nhanh "
              "theo nhiệt độ."),
             ("Ở nhiệt độ cao hơn, tất cả các phân tử khí đều chuyển động nhanh hơn.",
              False,
              "Chỉ có TỐC ĐỘ TRUNG BÌNH tăng. Ở nhiệt độ nào cũng vậy, luôn tồn tại các "
              "phân tử rất chậm và các phân tử rất nhanh; hai đường phân bố chồng lên nhau "
              "trong một dải rộng chứ không tách rời."),
             ("Tốc độ căn quân phương của phân tử ở T₂ lớn hơn ở T₁ khoảng 1,53 lần.", True,
              "v tỉ lệ với √T nên v₂/v₁ = √(700/300) = √2,333 ≈ 1,528 ≈ 1,53."),
             ("Diện tích phần nằm dưới hai đường cong là khác nhau vì nhiệt độ khác nhau.",
              False,
              "Diện tích dưới đường phân bố biểu diễn TỔNG số phân tử, mà đây vẫn là cùng "
              "một lượng khí nên tổng số phân tử không đổi. Vì thế hai diện tích BẰNG "
              "nhau; đó cũng chính là lí do đường ở nhiệt độ cao hơn phải thấp và bè hơn."),
         ]),

    dict(stem="Một lượng khí lí tưởng chuyển từ trạng thái (1) có p = 4,0 atm, V = 1,0 lít "
              "sang trạng thái (2) có p = 1,0 atm, V = 4,0 lít theo hai cách như hình vẽ: "
              "quá trình I là đẳng nhiệt; quá trình II gồm đẳng tích (1) → (3) rồi đẳng áp "
              "(3) → (2).",
         fig="t25d",
         items=[
             ("Nhiệt độ ở trạng thái (2) lớn gấp 4 lần nhiệt độ ở trạng thái (1).", False,
              "Tích pV tại (1) là 4,0 × 1,0 = 4,0 và tại (2) là 1,0 × 4,0 = 4,0 atm·lít — "
              "bằng nhau, nên T₁ = T₂. Chính vì thế quá trình I nối hai trạng thái này mới "
              "có thể là đẳng nhiệt."),
             ("Ở trạng thái trung gian (3), nhiệt độ của khí bằng một phần tư nhiệt độ ở "
              "trạng thái (1).", True,
              "Trạng thái (3) có p = 1,0 atm và V = 1,0 lít nên pV = 1,0 atm·lít, chỉ bằng "
              "một phần tư giá trị 4,0 atm·lít ở trạng thái (1). Vậy T₃ = T₁/4."),
             ("Độ biến thiên nội năng của khí trong quá trình I khác với trong quá trình "
              "II.", False,
              "Nội năng là hàm trạng thái nên ΔU chỉ phụ thuộc trạng thái đầu và trạng "
              "thái cuối. Hai quá trình có cùng điểm đầu (1) và cùng điểm cuối (2) nên "
              "ΔU_I = ΔU_II (và ở đây đều bằng 0 vì T₁ = T₂). Công và nhiệt lượng thì khác "
              "nhau."),
             ("Trong quá trình II, có giai đoạn khí bị làm lạnh và có giai đoạn khí được "
              "đun nóng.", True,
              "Giai đoạn (1) → (3) là đẳng tích với áp suất giảm 4 lần nên nhiệt độ giảm "
              "4 lần: khí bị làm lạnh. Giai đoạn (3) → (2) là đẳng áp với thể tích tăng "
              "4 lần nên nhiệt độ tăng trở lại 4 lần: khí được đun nóng."),
         ]),

    dict(stem="Một bóng thám không chứa khí helium, ở mặt đất có thể tích 8,0 m³, áp suất "
              "1,0·10⁵ Pa và nhiệt độ 300 K. Vỏ bóng có thể dãn nở tự do cho tới thể tích "
              "tối đa 20 m³, nếu vượt quá thì bóng vỡ. Lượng khí trong bóng không đổi.",
         fig="t25c",
         items=[
             ("Khi bóng lên tới nơi có áp suất 0,40·10⁵ Pa và nhiệt độ 240 K thì thể tích "
              "của bóng là 16 m³.", True,
              "V₂ = 8,0 × (1,0/0,40) × (240/300) = 8,0 × 2,50 × 0,80 = 16 m³."),
             ("Ở độ cao đó, khối lượng riêng của khí trong bóng bằng 0,4 lần so với khi ở "
              "mặt đất.", False,
              "Khối lượng khí không đổi nên ρ tỉ lệ nghịch với thể tích: "
              "ρ₂/ρ₁ = V₁/V₂ = 8,0/16 = 0,5, tức bằng MỘT NỬA chứ không phải 0,4 lần. Con "
              "số 0,4 chỉ là tỉ số áp suất, không phải tỉ số khối lượng riêng."),
             ("Bóng sẽ vỡ khi lên tới nơi có áp suất 0,40·10⁵ Pa và nhiệt độ 240 K.", False,
              "Ở đó thể tích của bóng mới là 16 m³, còn nhỏ hơn giới hạn 20 m³, nên bóng "
              "chưa vỡ."),
             ("Nếu tiếp tục lên cao tới nơi có áp suất 0,25·10⁵ Pa và nhiệt độ 220 K thì "
              "bóng bị vỡ.", True,
              "V = 8,0 × (1,0/0,25) × (220/300) = 8,0 × 4,00 × 0,7333 ≈ 23,5 m³ > 20 m³. "
              "Thể tích cần thiết vượt quá giới hạn của vỏ nên bóng vỡ."),
         ]),
]

DE5_P3 = [
    dict(q="Một xi lanh thẳng đứng, đầu hở lên trên, có pit-tông khối lượng 2,0 kg và tiết "
           "diện 50 cm² giam một cột khí dài 30 cm ở 300 K. Áp suất khí quyển là 1,0·10⁵ "
           "Pa; g = 10 m/s². Đun nóng khí tới 351 K. Tính chiều dài cột khí lúc đó (theo "
           "cm, làm tròn đến hàng phần mười).",
         ans="35,1",
         sol="Pit-tông tự do nên áp suất khí không đổi: p = p₀ + mg/S = 1,0·10⁵ + "
             "20/0,0050 = 1,04·10⁵ Pa. Đây là một quá trình đẳng áp.\n"
             "Tiết diện đều nên thể tích tỉ lệ thuận với chiều dài cột khí:\n"
             "ℓ₂ = ℓ₁·T₂/T₁ = 30 × 351/300 = 35,1 cm.\n"
             "Lưu ý: giá trị cụ thể của áp suất không cần dùng tới, chỉ cần khẳng định nó "
             "KHÔNG ĐỔI."),

    dict(q="Nitrogen chiếm khoảng 78 % số phân tử trong không khí. Tính tốc độ căn quân "
           "phương của phân tử nitrogen (khối lượng mol 28 g/mol) trong buồng sấy của "
           "một lò công nghiệp ở 127 °C (theo m/s, làm tròn đến hàng đơn vị).",
         ans="597",
         sol="T = 127 + 273 = 400 K; M = 28·10⁻³ kg/mol.\n"
             "v = √(3RT/M) = √(3 × 8,31 × 400/0,028) = √(9972/0,028) = √356 143 "
             "≈ 596,8 ≈ 597 m/s."),

    dict(q="Hai bình A (2,0 lít) và B (3,0 lít) được nối với nhau bằng một ống nhỏ có "
           "khoá, chứa cùng một loại khí. Ban đầu khoá đóng, bình A ở 4,0·10⁵ Pa và bình B "
           "ở 1,0·10⁵ Pa, cả hai cùng ở 300 K. Mở khoá rồi nâng nhiệt độ của cả hệ lên "
           "400 K. Tính áp suất chung lúc đó (theo 10⁵ Pa, làm tròn đến hàng phần trăm).",
         ans="2,93",
         sol="Bước 1 – mở khoá ở 300 K. Tổng tích pV bảo toàn:\n"
             "p′ × (2,0 + 3,0) = 4,0·10⁵ × 2,0 + 1,0·10⁵ × 3,0 = 11·10⁵\n"
             "p′ = 11·10⁵/5,0 = 2,2·10⁵ Pa.\n"
             "Bước 2 – đun nóng ở thể tích tổng không đổi (đẳng tích):\n"
             "p = 2,2·10⁵ × 400/300 ≈ 2,93·10⁵ Pa."),

    dict(q="Một bình kín dung tích 4,0 lít chứa 0,20 mol khí lí tưởng đơn nguyên tử ở "
           "300 K. Tính nội năng của lượng khí đó theo công thức U = (3/2)nRT. (Kết quả "
           "theo J, làm tròn đến hàng đơn vị.)",
         ans="748",
         sol="U = (3/2)nRT = 1,5 × 0,20 × 8,31 × 300 = 747,9 J ≈ 748 J.\n"
             "Chú ý dung tích 4,0 lít không tham gia vào công thức: nội năng của khí lí "
             "tưởng chỉ phụ thuộc số mol và nhiệt độ."),

    dict(q="Một lượng khí lí tưởng ở 27 °C có áp suất 1,0·10⁵ Pa và thể tích 6,0 lít. Nén "
           "đẳng nhiệt lượng khí đó tới áp suất 3,0·10⁵ Pa rồi đun nóng đẳng tích tới "
           "600 K. Tính áp suất của khí ở cuối quá trình (theo 10⁵ Pa, làm tròn đến hàng "
           "phần mười).",
         ans="6,0",
         sol="Giai đoạn 1 (đẳng nhiệt): áp suất tăng từ 1,0·10⁵ lên 3,0·10⁵ Pa; thể tích "
             "giảm còn V′ = 6,0 × 1,0/3,0 = 2,0 lít. Nhiệt độ vẫn là 300 K.\n"
             "Giai đoạn 2 (đẳng tích, 300 K → 600 K):\n"
             "p = 3,0·10⁵ × 600/300 = 6,0·10⁵ Pa."),

    dict(q="Một bình kín thể tích không đổi chứa khí lí tưởng ở 27 °C, áp suất 2,4·10⁵ Pa. "
           "Người ta xả bớt 30 % số phân tử khí ra ngoài rồi đun nóng phần khí còn lại tới "
           "127 °C. Tính áp suất khí trong bình lúc đó (theo 10⁵ Pa, làm tròn đến hàng "
           "phần trăm).",
         ans="2,24",
         sol="Thể tích không đổi nên từ pV = Nk_BT suy ra p tỉ lệ thuận với tích N·T.\n"
             "Số phân tử còn lại: 0,70 lần ban đầu. Nhiệt độ: từ 300 K lên 400 K, tức tăng "
             "4/3 lần.\n"
             "p = 2,4·10⁵ × 0,70 × (400/300) = 2,4·10⁵ × 0,9333 = 2,24·10⁵ Pa."),
]

DE5 = dict(code="C2-05", so="05", chuong=2,
           title="ĐỀ KIỂM TRA CHƯƠNG II – ĐỀ SỐ 05",
           subtitle="Chương II – Khí lí tưởng",
           p1=DE5_P1, p2=DE5_P2, p3=DE5_P3)


DE_CH2 = [DE1, DE2, DE3, DE4, DE5]
