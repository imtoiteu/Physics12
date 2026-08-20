# -*- coding: utf-8 -*-
"""Bài tập lí thuyết - Chương I: VẬT LÍ NHIỆT.

MC1: câu trắc nghiệm nhiều phương án lựa chọn, chia theo bốn mức độ.
DS1: câu trắc nghiệm đúng/sai, mỗi câu bốn ý.

Lời giải luôn dẫn chiếu NỘI DUNG phương án, không dẫn chiếu chữ cái,
để không bị sai khi hoán vị vị trí đáp án.
"""

L1 = "Mức 1 – NHẬN BIẾT"
L2 = "Mức 2 – THÔNG HIỂU"
L3 = "Mức 3 – VẬN DỤNG"
L4 = "Mức 4 – VẬN DỤNG CAO"

MC1 = {
    # ------------------------------------------------------------------ MỨC 1
    L1: [
        dict(q="Nội năng của một vật là",
             o=["tổng động năng chuyển động nhiệt của các phân tử và thế năng tương tác "
                "giữa chúng.",
                "tổng động năng và thế năng trọng trường của cả vật.",
                "nhiệt lượng mà vật đã nhận được từ môi trường bên ngoài.",
                "tổng động năng chuyển động nhiệt của tất cả các phân tử cấu tạo nên vật đó."],
             a="A",
             e="Nội năng gồm hai thành phần: động năng chuyển động nhiệt của các phân tử và "
               "thế năng tương tác giữa chúng. Phương án chỉ nhắc động năng đã bỏ sót thế năng "
               "tương tác. Phương án nói về động năng và thế năng trọng trường của cả vật là "
               "cơ năng, không phải nội năng. Nhiệt lượng là đại lượng của quá trình truyền "
               "năng lượng, không phải năng lượng chứa trong vật."),

        dict(q="Đơn vị của nhiệt dung riêng trong hệ SI là",
             o=["J/(kg·K).", "J/kg.", "J/K.", "J/(kg·°C²)."],
             a="A",
             e="Từ c = Q/(m·ΔT) suy ra đơn vị là J chia cho kg và cho K, tức J/(kg·K). "
               "Đơn vị J/kg là của nhiệt nóng chảy riêng và nhiệt hoá hơi riêng; J/K là đơn vị "
               "của nhiệt dung (của cả vật)."),

        dict(q="Công thức của định luật I nhiệt động lực học theo quy ước của chương trình "
               "hiện hành là",
             o=["ΔU = A + Q, với A và Q là công và nhiệt lượng mà hệ NHẬN được.",
                "ΔU = A − Q, với A là công mà hệ nhận được.",
                "ΔU = Q − A, với A là công mà hệ nhận được.",
                "ΔU = A · Q, với A và Q là công và nhiệt lượng hệ nhận được."],
             a="A",
             e="Định luật I là phát biểu của định luật bảo toàn năng lượng cho quá trình nhiệt: "
               "độ biến thiên nội năng bằng tổng công và nhiệt lượng mà hệ nhận được. "
               "Các cách viết có dấu trừ chỉ đúng khi A được định nghĩa là công hệ SINH RA, "
               "khác với quy ước đang dùng. Nội năng không thể là tích của công và nhiệt lượng "
               "vì như vậy đơn vị sẽ không phải là jun."),

        dict(q="Nhiệt nóng chảy riêng của một chất là nhiệt lượng cần cung cấp để",
             o=["làm nóng chảy hoàn toàn 1 kg chất đó ở nhiệt độ nóng chảy.",
                "làm nóng chảy hoàn toàn 1 kg chất đó ở nhiệt độ bất kì.",
                "làm cho 1 kg chất đó tăng thêm 1 K.",
                "làm cho 1 kg chất đó hoá hơi hoàn toàn ở nhiệt độ sôi."],
             a="A",
             e="Định nghĩa yêu cầu đủ hai điều kiện: khối lượng 1 kg và chất đang ở đúng nhiệt "
               "độ nóng chảy. Nếu chất chưa đạt nhiệt độ nóng chảy thì còn phải tốn thêm nhiệt "
               "lượng làm nóng nó. Nội dung về việc tăng 1 K là định nghĩa nhiệt dung riêng, "
               "còn nội dung về hoá hơi ở nhiệt độ sôi là định nghĩa nhiệt hoá hơi riêng."),

        dict(q="Công thức chuyển đổi từ thang Celsius sang thang Kelvin là",
             o=["T(K) = t(°C) + 273,15.", "T(K) = t(°C) − 273,15.",
                "T(K) = 1,8·t(°C) + 32.", "T(K) = t(°C)/273,15."],
             a="A",
             e="Hai thang có cùng độ chia nhưng gốc của thang Kelvin thấp hơn gốc của thang "
               "Celsius 273,15 đơn vị, nên phải cộng thêm 273,15. Biểu thức nhân 1,8 rồi cộng 32 "
               "là công thức đổi sang thang Fahrenheit."),

        dict(q="Chuyển động Brown là chuyển động",
             o=["hỗn loạn không ngừng của các hạt nhỏ lơ lửng trong chất lỏng hoặc chất khí.",
                "có hướng của các phân tử chất lỏng từ nơi nóng sang nơi lạnh.",
                "tròn đều của các phân tử quanh một vị trí cân bằng cố định.",
                "của các hạt phấn hoa do chúng là vật thể sống nên tự chuyển động được."],
             a="A",
             e="Chuyển động Brown là chuyển động hỗn loạn, không ngừng, theo mọi hướng của các "
               "hạt nhỏ lơ lửng, do va chạm không cân bằng của các phân tử môi trường. "
               "Brown đã bác bỏ giả thuyết “vật sống tự chuyển động” bằng cách lặp lại thí "
               "nghiệm với bột khoáng vô cơ."),

        dict(q="Trong quá trình đẳng tích, biểu thức của định luật I nhiệt động lực học trở thành",
             o=["ΔU = Q.", "ΔU = A.", "ΔU = 0.", "Q = −A."],
             a="A",
             e="Thể tích không đổi nghĩa là khí không dãn nở cũng không bị nén nên không trao "
               "đổi công, tức A = 0, do đó ΔU = Q. Biểu thức ΔU = A ứng với quá trình đoạn nhiệt "
               "(Q = 0); còn ΔU = 0 và Q = −A ứng với quá trình đẳng nhiệt của khí lí tưởng."),

        dict(q="Trong ba thể của cùng một chất, thứ tự tăng dần của khoảng cách trung bình "
               "giữa các phân tử thường là",
             o=["rắn, lỏng, khí.", "khí, lỏng, rắn.", "lỏng, rắn, khí.", "rắn, khí, lỏng."],
             a="A",
             e="Ở thể rắn các phân tử sắp xếp sít nhau nhất, ở thể lỏng khoảng cách chỉ lớn hơn "
               "một chút, còn ở thể khí khoảng cách lớn hơn hàng chục lần kích thước phân tử. "
               "Vì vậy thứ tự tăng dần là rắn, lỏng, khí."),

        dict(q="Nhiệt lượng cần cung cấp để làm cho một vật khối lượng m, nhiệt dung riêng c "
               "tăng nhiệt độ thêm ΔT (vật không chuyển thể) được tính bằng",
             o=["Q = m·c·ΔT.", "Q = λ·m.", "Q = L·m.", "Q = c·ΔT/m."],
             a="A",
             e="Đây là công thức cơ bản cho quá trình thay đổi nhiệt độ mà không đổi thể. "
               "Các biểu thức chứa λ và L chỉ dùng khi vật đang chuyển thể ở nhiệt độ không đổi."),

        dict(q="Sự sôi là quá trình hoá hơi xảy ra",
             o=["ở cả mặt thoáng và trong lòng chất lỏng, tại một nhiệt độ xác định.",
                "chỉ ở mặt thoáng của chất lỏng, tại mọi nhiệt độ.",
                "chỉ trong lòng chất lỏng, tại mọi nhiệt độ.",
                "ở cả mặt thoáng và trong lòng chất lỏng, tại mọi nhiệt độ."],
             a="A",
             e="Đặc trưng của sự sôi là hoá hơi xảy ra đồng thời ở mặt thoáng và trong lòng "
               "chất lỏng (tạo thành các bọt khí), và chỉ xảy ra khi đạt nhiệt độ sôi ứng với "
               "áp suất đang có. Quá trình hoá hơi chỉ ở mặt thoáng và xảy ra ở mọi nhiệt độ "
               "là sự bay hơi."),

        dict(q="Đại lượng nào sau đây là hàm trạng thái, tức là chỉ phụ thuộc vào trạng thái "
               "hiện tại của hệ mà không phụ thuộc cách hệ đạt tới trạng thái đó?",
             o=["Nội năng.", "Nhiệt lượng.", "Công.", "Cả nhiệt lượng và công."],
             a="A",
             e="Nội năng là hàm trạng thái: cứ ở một trạng thái xác định thì vật có một giá trị "
               "nội năng xác định. Nhiệt lượng và công là đại lượng của quá trình, chúng mô tả "
               "năng lượng đang được truyền chứ không phải năng lượng chứa trong vật."),

        dict(q="Độ không tuyệt đối tương ứng với nhiệt độ nào trên thang Celsius?",
             o=["−273,15 °C.", "0 °C.", "273,15 °C.", "−100 °C."],
             a="A",
             e="Độ không tuyệt đối là 0 K, ứng với −273,15 °C trên thang Celsius. Đây là giới hạn "
               "dưới của nhiệt độ, tại đó chuyển động nhiệt của các phân tử là nhỏ nhất có thể."),

        dict(q="Nhiệt hoá hơi riêng của nước ở 100 °C có giá trị xấp xỉ",
             o=["2,26·10⁶ J/kg.", "3,34·10⁵ J/kg.", "4,2·10³ J/kg.", "2,1·10³ J/kg."],
             a="A",
             e="Nhiệt hoá hơi riêng của nước là 2,26·10⁶ J/kg. Giá trị 3,34·10⁵ J/kg là nhiệt "
               "nóng chảy riêng của nước đá; các giá trị cỡ 10³ là nhiệt dung riêng của nước "
               "lỏng và nước đá, có đơn vị khác hẳn."),

        dict(q="Hai vật tiếp xúc nhau đạt trạng thái cân bằng nhiệt khi",
             o=["nhiệt độ của hai vật bằng nhau.",
                "nội năng của hai vật bằng nhau.",
                "nhiệt lượng của hai vật bằng nhau.",
                "khối lượng và nhiệt dung riêng của hai vật bằng nhau."],
             a="A",
             e="Cân bằng nhiệt được định nghĩa bằng sự bằng nhau của NHIỆT ĐỘ, vì khi đó không "
               "còn dòng nhiệt truyền giữa hai vật. Nội năng của chúng hoàn toàn có thể khác "
               "nhau rất nhiều nếu khối lượng hoặc bản chất khác nhau."),

        dict(q="Trong quá trình một chất kết tinh đang nóng chảy, nhiệt độ của nó",
             o=["không đổi.", "tăng đều.", "giảm đều.", "tăng rồi giảm."],
             a="A",
             e="Với chất rắn kết tinh, toàn bộ nhiệt lượng cung cấp trong giai đoạn nóng chảy "
               "được dùng để phá vỡ liên kết trong mạng tinh thể, tức là làm tăng thế năng "
               "tương tác, nên động năng trung bình của phân tử và do đó nhiệt độ không đổi."),

        dict(q="Cách nào sau đây làm biến đổi nội năng của vật bằng cách THỰC HIỆN CÔNG?",
             o=["Cọ xát hai bàn tay vào nhau.",
                "Đặt cốc nước nóng ra ngoài trời lạnh.",
                "Nhúng một thanh sắt nguội vào nước sôi.",
                "Phơi một tấm kim loại dưới ánh nắng."],
             a="A",
             e="Cọ xát chuyển hoá cơ năng thành nội năng, đó là thực hiện công. Ba tình huống "
               "còn lại đều là nội năng truyền trực tiếp từ vật này sang vật kia hoặc từ bức xạ "
               "sang vật mà không có sự chuyển hoá dạng năng lượng, tức là truyền nhiệt."),

        dict(q="Chất rắn nào sau đây KHÔNG có nhiệt độ nóng chảy xác định?",
             o=["Thuỷ tinh.", "Sắt.", "Nước đá.", "Đồng."],
             a="A",
             e="Thuỷ tinh là chất rắn vô định hình: khi nung nóng nó mềm dần rồi chảy lỏng trong "
               "cả một khoảng nhiệt độ chứ không có một nhiệt độ nóng chảy xác định. Sắt, đồng "
               "và nước đá đều là chất rắn kết tinh nên có nhiệt độ nóng chảy xác định."),

        dict(q="Trong hệ SI, nhiệt lượng có đơn vị là",
             o=["jun (J).", "oát (W).", "kelvin (K).", "pascal (Pa)."],
             a="A",
             e="Nhiệt lượng là một dạng năng lượng truyền đi nên có đơn vị jun. Oát là đơn vị "
               "công suất, kelvin là đơn vị nhiệt độ, pascal là đơn vị áp suất."),

        dict(q="Phát biểu nào sau đây đúng về lực tương tác giữa các phân tử?",
             o=["Gồm cả lực hút và lực đẩy; khi khoảng cách rất nhỏ thì lực đẩy chiếm ưu thế.",
                "Chỉ gồm lực hút và lực hút tăng khi khoảng cách tăng.",
                "Chỉ gồm lực đẩy và lực đẩy tăng khi khoảng cách tăng.",
                "Gồm cả lực hút và lực đẩy, nhưng luôn cân bằng nhau ở mọi khoảng cách."],
             a="A",
             e="Lực tương tác phân tử gồm cả hai thành phần. Khi khoảng cách nhỏ hơn khoảng cách "
               "cân bằng, lực đẩy trội hơn nên chất rắn và lỏng rất khó nén. Hai thành phần chỉ "
               "cân bằng nhau đúng tại một khoảng cách xác định chứ không phải ở mọi khoảng cách."),

        dict(q="Nhiệt dung riêng của nước lỏng ở điều kiện thường xấp xỉ bằng",
             o=["4200 J/(kg·K).", "2100 J/(kg·K).", "880 J/(kg·K).", "380 J/(kg·K)."],
             a="A",
             e="Nước lỏng có nhiệt dung riêng khoảng 4200 J/(kg·K), lớn hơn hầu hết các chất "
               "thông thường. Giá trị 2100 là của nước đá, 880 là của nhôm và 380 là của đồng."),
    ],

    # ------------------------------------------------------------------ MỨC 2
    L2: [
        dict(q="Một lượng khí nhận nhiệt lượng 300 J đồng thời sinh công 500 J để đẩy pit-tông "
               "đi ra. Nội năng của khí",
             o=["giảm 200 J.", "tăng 200 J.", "tăng 800 J.", "giảm 800 J."],
             a="A",
             e="Khí nhận nhiệt nên Q = +300 J. Khí SINH công nên công mà khí nhận được là "
               "A = −500 J. Do đó ΔU = A + Q = −500 + 300 = −200 J, nghĩa là nội năng giảm 200 J. "
               "Kết quả tăng 200 J ứng với việc đảo nhầm dấu, còn kết quả 800 J ứng với việc "
               "cộng hai độ lớn thay vì đại số."),

        dict(q="Phát biểu nào sau đây SAI?",
             o=["Khi vật nhận nhiệt lượng thì nhiệt độ của vật luôn tăng.",
                "Khi vật nhận nhiệt lượng thì nội năng của vật có thể không đổi.",
                "Nội năng của vật có thể tăng mà vật không nhận nhiệt lượng nào.",
                "Nhiệt độ của vật có thể không đổi trong khi vật vẫn nhận nhiệt lượng."],
             a="A",
             e="Vật nhận nhiệt vẫn có thể không tăng nhiệt độ, chẳng hạn khi nước đá đang tan "
               "hoặc khi nước đang sôi; hoặc nhiệt độ còn có thể giảm nếu vật đồng thời sinh "
               "công lớn hơn nhiệt lượng nhận vào. Ba nhận định còn lại đều đúng: nội năng có "
               "thể tăng nhờ thực hiện công (cọ xát), và nội năng có thể không đổi khi nhiệt "
               "nhận vào bằng công sinh ra."),

        dict(q="Vì sao khi đang nóng chảy, chất rắn kết tinh vẫn thu nhiệt mà nhiệt độ không tăng?",
             o=["Vì nhiệt lượng thu vào dùng để tăng thế năng tương tác, phá vỡ mạng tinh thể, "
                "không làm tăng động năng trung bình của phân tử.",
                "Vì nhiệt lượng thu vào bị toả hết ra môi trường xung quanh.",
                "Vì nhiệt lượng thu vào dùng để tăng động năng của phân tử, nhưng động năng "
                "tăng không làm nhiệt độ tăng.",
                "Vì nội năng của chất không thay đổi trong suốt quá trình nóng chảy."],
             a="A",
             e="Nhiệt độ là thước đo động năng trung bình của phân tử. Trong giai đoạn nóng chảy, "
               "nhiệt lượng cung cấp chuyển thành thế năng tương tác để phá vỡ liên kết trong "
               "mạng tinh thể, còn động năng trung bình giữ nguyên nên nhiệt độ giữ nguyên. "
               "Nội năng vẫn TĂNG chứ không phải không đổi, vì phần thế năng tăng lên."),

        dict(q="Một cốc nước 200 g ở 30 °C và một giọt nước 1 g ở 90 °C. So sánh nào sau đây đúng?",
             o=["Cốc nước có nội năng lớn hơn giọt nước, nhưng nhiệt sẽ truyền từ giọt nước "
                "sang cốc nước nếu cho tiếp xúc.",
                "Giọt nước có nội năng lớn hơn cốc nước vì nhiệt độ của nó cao hơn nhiều, nên nhiệt truyền từ giọt sang cốc.",
                "Cốc nước có nội năng lớn hơn giọt nước nên nhiệt sẽ truyền từ cốc nước sang giọt nước cho tới khi cân bằng.",
                "Hai vật có nội năng bằng nhau vì cùng là nước, do đó không có nhiệt truyền giữa chúng khi tiếp xúc."],
             a="A",
             e="Nội năng phụ thuộc cả nhiệt độ lẫn số phân tử; cốc nước nặng gấp 200 lần nên có "
               "nội năng lớn hơn nhiều. Nhưng chiều truyền nhiệt được quyết định bởi CHÊNH LỆCH "
               "NHIỆT ĐỘ chứ không phải bởi nội năng, nên nhiệt truyền từ vật 90 °C sang vật "
               "30 °C."),

        dict(q="Trên đỉnh núi cao, nước sôi ở nhiệt độ thấp hơn 100 °C. Nguyên nhân là",
             o=["áp suất khí quyển trên cao nhỏ hơn nên nhiệt độ sôi giảm.",
                "không khí trên cao loãng nên chứa ít oxygen hơn.",
                "nhiệt độ môi trường trên cao thấp hơn nên nước nguội nhanh.",
                "nhiệt hoá hơi riêng của nước trên cao nhỏ hơn."],
             a="A",
             e="Nhiệt độ sôi của một chất lỏng phụ thuộc áp suất trên mặt thoáng: áp suất càng "
               "nhỏ thì nhiệt độ sôi càng thấp. Lượng oxygen và nhiệt độ môi trường không quyết "
               "định nhiệt độ sôi, còn nhiệt hoá hơi riêng là đặc trưng của chất chứ không phụ "
               "thuộc độ cao theo cách đó."),

        dict(q="Đun nóng đều một vật rắn kết tinh, đồ thị nhiệt độ – thời gian có một đoạn nằm "
               "ngang. Trong khoảng thời gian ứng với đoạn nằm ngang đó, nội năng của vật",
             o=["tăng.", "giảm.", "không đổi.", "tăng rồi giảm."],
             a="A",
             e="Trong đoạn nằm ngang, vật vẫn liên tục nhận nhiệt lượng từ nguồn nên nội năng "
               "vẫn tăng; phần năng lượng nhận thêm được tích luỹ dưới dạng thế năng tương tác. "
               "Chỉ có nhiệt độ là không đổi. Nhầm “nhiệt độ không đổi” thành “nội năng không "
               "đổi' là một trong những sai lầm phổ biến nhất."),

        dict(q="Vì sao vùng ven biển thường có biên độ nhiệt ngày – đêm nhỏ hơn vùng sâu trong "
               "lục địa?",
             o=["Vì nước có nhiệt dung riêng lớn nên hấp thụ và nhả nhiệt mà nhiệt độ thay đổi ít.",
                "Vì nước có nhiệt dung riêng nhỏ nên nóng lên và nguội đi rất nhanh.",
                "Vì nước phản xạ toàn bộ ánh sáng Mặt Trời chiếu tới.",
                "Vì gió biển luôn thổi từ đất liền ra biển suốt cả ngày lẫn đêm."],
             a="A",
             e="Nước có nhiệt dung riêng khoảng 4200 J/(kg·K), lớn hơn nhiều so với đất, cát và "
               "đá. Cùng một nhiệt lượng trao đổi, khối nước biển thay đổi nhiệt độ ít hơn hẳn, "
               "nhờ đó điều hoà nhiệt độ vùng ven bờ."),

        dict(q="Nhiệt độ của một vật tăng từ 20 °C lên 80 °C. Độ biến thiên nhiệt độ của vật "
               "tính theo thang Kelvin là",
             o=["60 K.", "333 K.", "606,3 K.", "60,15 K."],
             a="A",
             e="Vì hai thang Celsius và Kelvin có cùng độ chia nên độ biến thiên nhiệt độ có "
               "cùng giá trị số: ΔT = 80 − 20 = 60 K. Việc cộng 273 vào độ biến thiên là sai, "
               "vì hằng số đó bị triệt tiêu khi lấy hiệu hai nhiệt độ."),

        dict(q="Vì sao nhiệt hoá hơi riêng của nước lớn hơn nhiều so với nhiệt nóng chảy riêng "
               "của nước đá?",
             o=["Vì khi hoá hơi, phân tử phải thoát hẳn khỏi lực hút của các phân tử khác, còn "
                "khi nóng chảy chúng chỉ rời khỏi vị trí cố định nhưng vẫn ở gần nhau.",
                "Vì nhiệt độ sôi của nước (100 °C) cao hơn hẳn nhiệt độ nóng chảy (0 °C), mà nhiệt lượng cần cung cấp thì tỉ lệ với nhiệt độ xảy ra quá trình.",
                "Vì hơi nước có khối lượng riêng nhỏ hơn nước lỏng rất nhiều, nên cùng một khối lượng thì hơi chiếm thể tích lớn hơn và cần nhiều năng lượng hơn.",
                "Vì trên thực tế quá trình sôi luôn diễn ra trong thời gian dài hơn quá trình nóng chảy, nên tổng nhiệt lượng phải cung cấp cũng lớn hơn."],
             a="A",
             e="Nguyên nhân nằm ở mức độ phá vỡ liên kết. Khi nóng chảy, các phân tử chỉ mất "
               "trật tự xa nhưng vẫn nằm sát nhau nên chỉ cần nới lỏng liên kết. Khi hoá hơi, "
               "phân tử phải thoát hoàn toàn khỏi vùng ảnh hưởng của các phân tử khác và còn "
               "sinh công đẩy khí quyển. Giá trị nhiệt độ hay thời gian không phải là nguyên "
               "nhân — thời gian dài hơn chính là HỆ QUẢ của việc cần nhiều năng lượng hơn."),

        dict(q="Một hệ được cách nhiệt hoàn toàn với môi trường. Kết luận nào sau đây đúng?",
             o=["Nội năng của hệ chỉ có thể thay đổi bằng cách thực hiện công.",
                "Nội năng của hệ chắc chắn không thay đổi.",
                "Nhiệt độ của hệ chắc chắn không thay đổi.",
                "Hệ không thể trao đổi năng lượng với bên ngoài dưới bất kì hình thức nào."],
             a="A",
             e="Cách nhiệt nghĩa là Q = 0, nên ΔU = A: hệ vẫn có thể thay đổi nội năng bằng cách "
               "nhận hay sinh công. Ví dụ nén nhanh khí trong bình cách nhiệt làm khí nóng lên. "
               "Vì vậy nội năng và nhiệt độ không nhất thiết giữ nguyên."),

        dict(q="Hình vẽ bên là đồ thị nhiệt độ theo thời gian khi làm nguội một chất lỏng. "
               "Nhiệt độ đông đặc của chất này và khoảng thời gian đông đặc lần lượt là",
             o=["60 °C và 10 phút.", "60 °C và 14 phút.", "90 °C và 10 phút.", "30 °C và 4 phút."],
             a="A",
             e="Đoạn nằm ngang trên đồ thị làm nguội ứng với quá trình đông đặc, cho biết nhiệt "
               "độ đông đặc là 60 °C. Đoạn này kéo dài từ phút thứ 4 đến phút thứ 14, tức là "
               "10 phút. Giá trị 14 phút là mốc thời gian kết thúc chứ không phải khoảng thời "
               "gian, còn 90 °C là nhiệt độ ban đầu.",
             fig="h14_do_thi_lam_nguoi"),

        dict(q="Khi bơm xe đạp, thân bơm nóng lên. Giải thích đúng nhất là",
             o=["ta thực hiện công nén khí rất nhanh nên khí gần như không kịp trao đổi nhiệt, "
                "nội năng khí tăng; đồng thời ma sát giữa pit-tông và thành bơm cũng sinh nhiệt.",
                "khí trong bơm nhận nhiệt lượng truyền từ không khí bên ngoài qua thành bơm bằng kim loại, vì kim loại dẫn nhiệt rất tốt.",
                "khối lượng khí bên trong thân bơm tăng lên sau mỗi lần đẩy pit-tông, mà nội năng tỉ lệ với số phân tử nên nội năng của khí tăng theo.",
                "khí trong bơm dãn nở khi được đẩy qua van vào lốp, quá trình sinh công này làm nội năng và nhiệt độ của khí tăng lên."],
             a="A",
             e="Nén nhanh là quá trình gần đoạn nhiệt: Q ≈ 0 và A > 0 nên ΔU > 0, khí nóng lên. "
               "Ma sát cơ học cũng góp thêm nội năng. Không khí bên ngoài lúc đầu lạnh hơn nên "
               "không thể là nguồn cấp nhiệt, và khí bị NÉN chứ không dãn nở."),

        dict(q="Cùng cung cấp một nhiệt lượng như nhau cho 1 kg nước và 1 kg nhôm (đều không "
               "chuyển thể), biết c_nước = 4200 J/(kg·K) và c_nhôm = 880 J/(kg·K). Kết luận nào đúng?",
             o=["Nhôm tăng nhiệt độ nhiều hơn nước khoảng 4,8 lần.",
                "Nước tăng nhiệt độ nhiều hơn nhôm khoảng 4,8 lần.",
                "Hai vật tăng nhiệt độ như nhau vì nhận cùng nhiệt lượng.",
                "Không so sánh được vì chưa biết nhiệt độ ban đầu."],
             a="A",
             e="Từ Q = mcΔT với m và Q như nhau, suy ra ΔT tỉ lệ nghịch với c. "
               "ΔT_nhôm/ΔT_nước = 4200/880 ≈ 4,8, nên nhôm nóng lên nhiều hơn. Chất có nhiệt "
               "dung riêng nhỏ thì dễ nóng lên hơn. Nhiệt độ ban đầu không ảnh hưởng đến độ tăng "
               "nhiệt độ trong khoảng mà c coi như hằng số."),

        dict(q="Phát biểu nào sau đây về sự bay hơi là ĐÚNG?",
             o=["Sự bay hơi xảy ra ở mọi nhiệt độ và làm cho phần chất lỏng còn lại có thể "
                "lạnh đi.",
                "Sự bay hơi chỉ xảy ra khi chất lỏng được đun tới đúng nhiệt độ sôi xác định của nó.",
                "Sự bay hơi là quá trình toả nhiệt nên làm cho phần chất lỏng còn lại nóng lên.",
                "Tốc độ bay hơi không phụ thuộc diện tích mặt thoáng mà chỉ phụ thuộc nhiệt độ."],
             a="A",
             e="Bay hơi xảy ra ở mọi nhiệt độ vì luôn có những phân tử ở mặt thoáng đủ nhanh để "
               "thoát ra. Chính những phân tử nhanh nhất ra đi làm động năng trung bình của phần "
               "còn lại giảm, nên chất lỏng lạnh đi — đó là cơ chế làm mát khi ra mồ hôi. "
               "Tốc độ bay hơi phụ thuộc rõ rệt vào diện tích mặt thoáng, nhiệt độ, gió và độ ẩm."),

        dict(q="Nồi áp suất giúp nấu thức ăn nhanh nhừ hơn vì",
             o=["áp suất trong nồi cao làm nước sôi ở nhiệt độ trên 100 °C, thức ăn được nấu "
                "ở nhiệt độ cao hơn.",
                "áp suất trong nồi cao làm nước sôi nhanh hơn hẳn so với nồi thường, nhờ đó tiết kiệm được thời gian đun.",
                "thành nồi áp suất dày và kín nên truyền nhiệt vào thức ăn tốt hơn nồi thường nhiều lần.",
                "áp suất cao trong nồi làm nhiệt dung riêng của nước giảm mạnh nên nước nóng lên nhanh hơn hẳn."],
             a="A",
             e="Nồi áp suất không làm nước “sôi nhanh hơn” mà làm nước sôi ở nhiệt độ CAO hơn "
               "(khoảng 110 – 120 °C). Thức ăn được nấu ở nhiệt độ cao hơn nên chín nhanh hơn. "
               "Đây là ứng dụng trực tiếp của sự phụ thuộc nhiệt độ sôi vào áp suất."),

        dict(q="Trong hai vật cùng khối lượng và cùng nhiệt độ, vật nào có nội năng lớn hơn?",
             o=["Vật ở thể hơi, vì thế năng tương tác giữa các phân tử lớn hơn.",
                "Vật ở thể lỏng, vì các phân tử ở gần nhau hơn.",
                "Hai vật có nội năng bằng nhau vì cùng nhiệt độ và cùng khối lượng.",
                "Không xác định được vì nội năng chỉ phụ thuộc nhiệt độ."],
             a="A",
             e="Cùng nhiệt độ nên động năng trung bình của phân tử như nhau, nhưng để chuyển từ "
               "thể lỏng sang thể hơi đã phải cung cấp nhiệt hoá hơi Lm; năng lượng đó được tích "
               "luỹ dưới dạng thế năng tương tác. Vì vậy hơi nước ở 100 °C có nội năng lớn hơn "
               "nước lỏng ở 100 °C cùng khối lượng."),

        dict(q="Nhận định nào sau đây về nhiệt dung riêng là ĐÚNG?",
             o=["Nhiệt dung riêng là đặc trưng của chất, còn nhiệt dung là đặc trưng của một "
                "vật cụ thể.",
                "Nhiệt dung riêng của một vật càng lớn khi khối lượng vật càng lớn.",
                "Hai vật làm cùng một chất nhưng khác khối lượng thì có nhiệt dung riêng khác nhau.",
                "Nhiệt dung riêng có cùng đơn vị với nhiệt dung."],
             a="A",
             e="Nhiệt dung riêng c chỉ phụ thuộc bản chất của chất, đơn vị J/(kg·K). "
               "Nhiệt dung C = m·c phụ thuộc thêm khối lượng, đơn vị J/K. Hai vật cùng chất luôn "
               "có cùng c dù khối lượng khác nhau."),

        dict(q="Đặt một thìa kim loại vào cốc nước nóng, một lúc sau cán thìa cũng nóng lên. "
               "Quá trình làm nội năng của cán thìa tăng ở đây là",
             o=["truyền nhiệt.", "thực hiện công.",
                "vừa truyền nhiệt vừa thực hiện công với vai trò ngang nhau.",
                "chuyển hoá cơ năng thành nội năng."],
             a="A",
             e="Nội năng được truyền trực tiếp từ nước nóng sang thìa rồi lan dọc theo cán thìa "
               "nhờ dẫn nhiệt, không có sự chuyển hoá từ dạng năng lượng khác sang nội năng. "
               "Đó là truyền nhiệt thuần tuý."),

        dict(q="Một chất lỏng bay hơi nhanh hơn khi",
             o=["nhiệt độ cao hơn, diện tích mặt thoáng lớn hơn và có gió thổi qua.",
                "nhiệt độ thấp hơn, diện tích mặt thoáng nhỏ hơn và không có gió thổi qua.",
                "độ ẩm không khí xung quanh cao hơn.",
                "chất lỏng được đựng trong bình kín."],
             a="A",
             e="Nhiệt độ cao làm nhiều phân tử đủ nhanh để thoát ra; mặt thoáng rộng làm tăng số "
               "phân tử có cơ hội thoát; gió cuốn hơi đi làm giảm số phân tử quay trở lại. "
               "Ngược lại, độ ẩm cao hoặc bình kín làm hơi tích tụ phía trên mặt thoáng, "
               "hạn chế bay hơi."),

        dict(q="Khi một khối khí bị nén đoạn nhiệt (không trao đổi nhiệt với bên ngoài) thì",
             o=["nội năng tăng và nhiệt độ tăng.",
                "nội năng giảm và nhiệt độ giảm.",
                "nội năng không đổi vì không trao đổi nhiệt.",
                "nội năng tăng nhưng nhiệt độ không đổi."],
             a="A",
             e="Đoạn nhiệt nghĩa là Q = 0 nên ΔU = A. Khí bị nén nên nhận công, A > 0, do đó "
               "ΔU > 0 và nhiệt độ tăng. Việc không trao đổi nhiệt hoàn toàn không đồng nghĩa "
               "với nội năng không đổi."),

        dict(q="Trong thí nghiệm đo nhiệt dung riêng của nước bằng cách đun bằng điện trở, "
               "nếu bỏ qua việc bình nhiệt lượng kế cũng nóng lên thì giá trị c đo được sẽ",
             o=["lớn hơn giá trị thực.", "nhỏ hơn giá trị thực.",
                "bằng đúng giá trị thực.", "lúc lớn hơn lúc nhỏ hơn một cách ngẫu nhiên."],
             a="A",
             e="Nhiệt lượng do điện trở cung cấp thực ra được chia cho cả nước lẫn bình, nhưng "
               "khi tính ta lại gán toàn bộ cho nước. Với cùng độ tăng nhiệt độ ΔT, tử số Q bị "
               "tính thừa nên c = Q/(mΔT) thu được lớn hơn giá trị thực. Đây là sai số hệ thống "
               "chứ không phải sai số ngẫu nhiên."),

        dict(q="Phát biểu nào sau đây về nước đá là ĐÚNG?",
             o=["Nước đá nổi trên nước lỏng vì khi đông đặc, cấu trúc tinh thể làm thể tích "
                "tăng nên khối lượng riêng giảm.",
                "Nước đá nổi trên nước lỏng vì mọi chất rắn đều có khối lượng riêng nhỏ hơn chất lỏng của chính nó.",
                "Nước đá chìm trong nước lỏng vì ở thể rắn khoảng cách giữa các phân tử nhỏ hơn nên khối lượng riêng lớn hơn.",
                "Nước đá có khối lượng riêng đúng bằng nước lỏng nên nó lơ lửng ở giữa chứ không nổi hẳn lên mặt nước."],
             a="A",
             e="Nước là chất bất thường: liên kết hydrogen tạo cấu trúc tinh thể rỗng nên khi "
               "đông đặc thể tích TĂNG khoảng 9 %, khối lượng riêng giảm nên đá nổi. "
               "Với hầu hết các chất khác thì thể tích giảm khi đông đặc và thể rắn chìm trong "
               "thể lỏng của chính nó."),

        dict(q="Hai vật A và B tiếp xúc nhiệt với nhau trong hệ cách nhiệt. Sau một thời gian, "
               "nhiệt độ của A giảm còn nhiệt độ của B tăng. Kết luận nào sau đây chắc chắn đúng?",
             o=["Nhiệt lượng A toả ra bằng nhiệt lượng B thu vào.",
                "Nội năng ban đầu của A lớn hơn nội năng ban đầu của B.",
                "Khối lượng của A lớn hơn khối lượng của B.",
                "Nhiệt dung riêng của A lớn hơn nhiệt dung riêng của B."],
             a="A",
             e="Trong hệ cách nhiệt, năng lượng được bảo toàn nên nhiệt lượng vật này toả ra "
               "đúng bằng nhiệt lượng vật kia thu vào. Chiều truyền nhiệt chỉ cho biết nhiệt độ "
               "ban đầu của A cao hơn của B, hoàn toàn không suy ra được điều gì về nội năng, "
               "khối lượng hay nhiệt dung riêng của chúng."),

        dict(q="Đại lượng nào sau đây KHÔNG ảnh hưởng tới nội năng của một khối nước xác định?",
             o=["Vận tốc chuyển động của cả bình nước so với mặt đất.",
                "Nhiệt độ của khối nước trong bình.",
                "Khối lượng của khối nước trong bình.",
                "Thể của nước trong bình (lỏng hay hơi)."],
             a="A",
             e="Nội năng chỉ liên quan tới chuyển động và tương tác của các phân tử BÊN TRONG "
               "vật. Vận tốc của cả bình so với mặt đất tạo ra động năng của vật (thuộc cơ năng), "
               "không làm thay đổi chuyển động nhiệt hỗn loạn bên trong nên không thuộc nội năng."),
    ],

    # ------------------------------------------------------------------ MỨC 3
    L3: [
        dict(q="Một khối khí thực hiện một quá trình trong đó nó nhận nhiệt lượng Q > 0 nhưng "
               "nhiệt độ lại giảm. Điều này chỉ có thể xảy ra khi",
             o=["khối khí dãn nở và sinh công có độ lớn lớn hơn Q.",
                "khối khí bị nén và nhận thêm công từ bên ngoài.",
                "khối khí giữ nguyên thể tích trong suốt quá trình.",
                "khối khí đồng thời toả ra một nhiệt lượng khác lớn hơn Q."],
             a="A",
             e="Nhiệt độ giảm nghĩa là ΔU < 0. Từ ΔU = A + Q với Q > 0, bắt buộc A < 0 và |A| > Q, "
               "tức khí phải sinh công lớn hơn nhiệt lượng nhận được — đó là quá trình dãn nở. "
               "Nếu khí bị nén thì A > 0, cộng với Q > 0 sẽ cho ΔU > 0. Nếu thể tích không đổi "
               "thì A = 0 và ΔU = Q > 0."),

        dict(q="Cho biết c_nước = 4200 J/(kg·K), c_đá = 2100 J/(kg·K), λ_đá = 3,34·10⁵ J/kg. "
               "Cùng nhận một nhiệt lượng 1,0·10⁵ J, khối lượng 0,50 kg nước đá ở −10 °C sẽ",
             o=["tan hết phần lớn nhưng chưa tan hoàn toàn, nhiệt độ cuối là 0 °C.",
                "tăng nhiệt độ lên tới khoảng 95 °C.",
                "tan hoàn toàn rồi tiếp tục nóng lên tới khoảng 40 °C.",
                "chỉ nóng lên tới khoảng −0,5 °C mà chưa bắt đầu tan."],
             a="A",
             e="Đưa đá từ −10 °C lên 0 °C cần 0,50·2100·10 = 10 500 J. Còn lại "
               "1,0·10⁵ − 10 500 = 89 500 J. Để tan hết cần 0,50·3,34·10⁵ = 167 000 J, "
               "lớn hơn phần còn lại. Vậy đá chỉ tan được 89 500/3,34·10⁵ ≈ 0,268 kg và nhiệt độ "
               "dừng ở 0 °C. Đây chính là bước kiểm tra “đá có tan hết không” mà nhiều học sinh "
               "bỏ qua."),

        dict(q="Đồ thị nhiệt lượng cung cấp Q theo độ tăng nhiệt độ ΔT của một chất lỏng khối "
               "lượng 0,20 kg là một đường thẳng qua gốc toạ độ có hệ số góc 0,42 kJ/K. "
               "Nhiệt dung riêng của chất lỏng đó là",
             o=["2100 J/(kg·K).", "420 J/(kg·K).", "4200 J/(kg·K).", "84 J/(kg·K)."],
             a="A",
             e="Hệ số góc của đồ thị Q theo ΔT chính là tích m·c, ở đây bằng 420 J/K. "
               "Do đó c = 420/0,20 = 2100 J/(kg·K). Việc lấy thẳng 420 làm đáp số là quên chia "
               "cho khối lượng, còn 84 là kết quả của việc nhân thay vì chia.",
             fig="h10_do_thi_Q_deltaT"),

        dict(q="Đun nóng đều một vật rắn cho tới khi nó nóng chảy hết rồi tiếp tục đun. "
               "Trên đồ thị nhiệt độ – thời gian, đoạn ứng với thể rắn có độ dốc lớn hơn đoạn "
               "ứng với thể lỏng. Kết luận đúng là",
             o=["nhiệt dung riêng của chất ở thể rắn nhỏ hơn ở thể lỏng.",
                "nhiệt dung riêng của chất ở thể rắn lớn hơn ở thể lỏng.",
                "nhiệt nóng chảy riêng của chất rất nhỏ.",
                "khối lượng của vật đã giảm đi sau khi nóng chảy."],
             a="A",
             e="Với công suất cấp nhiệt không đổi P, độ dốc của đồ thị là dT/dt = P/(m·c). "
               "Khối lượng không đổi nên đoạn dốc hơn ứng với c nhỏ hơn. Vậy c của thể rắn nhỏ "
               "hơn c của thể lỏng — đúng như trường hợp nước đá (2100) và nước lỏng (4200). "
               "Độ dốc của các đoạn nghiêng không cho thông tin gì về nhiệt nóng chảy riêng; "
               "đại lượng đó thể hiện ở ĐỘ DÀI đoạn nằm ngang."),

        dict(q="Người ta thả một miếng kim loại nóng vào nước lạnh trong nhiệt lượng kế. "
               "Nếu quên không tính đến nhiệt lượng mà bình nhiệt lượng kế thu vào, giá trị "
               "nhiệt dung riêng của kim loại tính được sẽ",
             o=["nhỏ hơn giá trị thực.", "lớn hơn giá trị thực.",
                "bằng giá trị thực.", "phụ thuộc vào nhiệt độ ban đầu của kim loại."],
             a="A",
             e="Thực tế nhiệt lượng kim loại toả ra được chia cho cả nước và bình. Nếu bỏ qua "
               "bình, ta gán toàn bộ nhiệt lượng thu vào chỉ cho nước, tức là ĐÁNH GIÁ THẤP "
               "nhiệt lượng mà kim loại đã toả ra. Vì c_kim loại tỉ lệ với nhiệt lượng toả ra "
               "này nên kết quả thu được nhỏ hơn giá trị thực. Lưu ý chiều sai số ở đây NGƯỢC "
               "với thí nghiệm đun nước bằng điện trở."),

        dict(q="Trộn m₁ = 100 g nước ở 20 °C với m₂ = 300 g nước ở 80 °C trong bình cách nhiệt. "
               "Nhiệt độ cân bằng là",
             o=["65 °C.", "50 °C.", "60 °C.", "35 °C."],
             a="A",
             e="Vì cùng là nước nên c triệt tiêu: t = (m₁t₁ + m₂t₂)/(m₁ + m₂) = "
               "(100·20 + 300·80)/400 = 26 000/400 = 65 °C. Kết quả 50 °C là trung bình cộng đơn "
               "thuần, sai vì đã bỏ qua trọng số khối lượng. Nhiệt độ cân bằng phải lệch về phía "
               "khối nước nhiều hơn, tức về phía 80 °C."),

        dict(q="Một động cơ nhiệt nhận 1000 J nhiệt lượng từ nguồn nóng, sinh công 300 J và "
               "toả phần còn lại cho nguồn lạnh. Sau một chu trình khép kín, độ biến thiên nội "
               "năng của chất công tác là",
             o=["0 J.", "300 J.", "700 J.", "1000 J."],
             a="A",
             e="Nội năng là hàm trạng thái. Sau một chu trình khép kín, chất công tác trở về "
               "đúng trạng thái ban đầu nên ΔU = 0, bất kể nó đã nhận và toả bao nhiêu năng "
               "lượng trong chu trình. Giá trị 700 J là nhiệt lượng toả cho nguồn lạnh, "
               "còn 300 J là công sinh ra."),

        dict(q="Cần cung cấp nhiệt lượng bao nhiêu để làm 200 g nước đá ở 0 °C tan hết rồi đưa "
               "nước thu được lên 20 °C? Cho λ = 3,34·10⁵ J/kg, c_nước = 4200 J/(kg·K).",
             o=["≈ 83,6 kJ.", "≈ 66,8 kJ.", "≈ 16,8 kJ.", "≈ 100,4 kJ."],
             a="A",
             e="Giai đoạn tan: Q₁ = 0,200·3,34·10⁵ = 66 800 J. Giai đoạn nóng lên: "
               "Q₂ = 0,200·4200·20 = 16 800 J. Tổng Q = 83 600 J ≈ 83,6 kJ. "
               "Hai giá trị 66,8 kJ và 16,8 kJ là kết quả của việc chỉ tính một giai đoạn."),

        dict(q="Một bình cách nhiệt chứa nước ở 0 °C và nước đá ở 0 °C đang cân bằng. "
               "Nếu cung cấp thêm một nhiệt lượng nhỏ cho bình thì",
             o=["một phần nước đá tan, nhiệt độ hỗn hợp vẫn giữ 0 °C.",
                "nhiệt độ hỗn hợp tăng ngay lập tức.",
                "một phần nước đông đặc, nhiệt độ vẫn giữ 0 °C.",
                "nhiệt độ nước tăng còn nhiệt độ nước đá giữ nguyên."],
             a="A",
             e="Chừng nào còn cả nước và nước đá cùng tồn tại, nhiệt lượng cung cấp được dùng "
               "toàn bộ để làm nóng chảy đá, nên nhiệt độ hỗn hợp giữ nguyên 0 °C. Nhiệt độ chỉ "
               "bắt đầu tăng sau khi toàn bộ đá đã tan. Trong một hỗn hợp cân bằng nhiệt, "
               "hai thành phần không thể có nhiệt độ khác nhau."),

        dict(q="Đun 1 kg nước từ 20 °C tới sôi rồi tiếp tục đun cho bay hơi hết. So sánh nhiệt "
               "lượng của hai giai đoạn (c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg):",
             o=["Giai đoạn hoá hơi cần nhiệt lượng lớn hơn khoảng 6,7 lần.",
                "Giai đoạn đun nóng cần nhiệt lượng lớn hơn khoảng 6,7 lần.",
                "Hai giai đoạn cần nhiệt lượng xấp xỉ nhau.",
                "Giai đoạn hoá hơi cần nhiệt lượng lớn hơn khoảng 2,7 lần."],
             a="A",
             e="Đun nóng: Q₁ = 1·4200·80 = 336 000 J. Hoá hơi: Q₂ = 1·2,26·10⁶ = 2 260 000 J. "
               "Tỉ số Q₂/Q₁ = 2 260 000/336 000 ≈ 6,7. Đây là lí do đun sôi ấm nước thì nhanh "
               "nhưng đun cạn hẳn lại rất lâu."),

        dict(q="Khi mở nắp một bình khí nén, khí phụt ra ngoài rất nhanh và ta thấy miệng bình "
               "lạnh đi. Giải thích đúng nhất là",
             o=["khí dãn nở rất nhanh nên gần như không kịp nhận nhiệt; nó sinh công đẩy không "
                "khí xung quanh nên nội năng giảm, nhiệt độ giảm.",
                "khí nhận nhiệt lượng từ môi trường xung quanh nên nội năng của nó tăng lên, đồng thời nhiệt độ tại miệng bình giảm xuống.",
                "khối lượng khí còn lại trong bình giảm đi nhanh chóng, mà nhiệt độ tỉ lệ thuận với khối lượng nên nhiệt độ cũng giảm.",
                "khí bị nén mạnh khi phải chui qua khe hẹp ở miệng bình, quá trình nén này làm nhiệt độ của nó giảm xuống."],
             a="A",
             e="Quá trình xảy ra rất nhanh nên gần đoạn nhiệt, Q ≈ 0. Khí dãn nở, sinh công đẩy "
               "không khí xung quanh nên A < 0, do đó ΔU < 0 và nhiệt độ giảm. Khí đi ra là DÃN "
               "chứ không phải bị nén, và việc giảm khối lượng không tự nó làm nhiệt độ giảm."),

        dict(q="Một vật khối lượng 2,0 kg rơi tự do từ độ cao 10 m xuống nền cứng và dừng lại. "
               "Giả sử toàn bộ cơ năng chuyển thành nội năng của vật, nhiệt dung riêng của vật "
               "là 500 J/(kg·K), lấy g = 10 m/s². Nhiệt độ của vật tăng thêm",
             o=["0,20 K.", "0,10 K.", "2,0 K.", "0,02 K."],
             a="A",
             e="Cơ năng chuyển thành nội năng: W = mgh = 2,0·10·10 = 200 J. "
               "Từ W = m·c·ΔT suy ra ΔT = 200/(2,0·500) = 0,20 K. Kết quả rất nhỏ này giải thích "
               "vì sao trong đời sống ta khó nhận thấy vật nóng lên sau khi rơi."),

        dict(q="Trong thí nghiệm đo nhiệt nóng chảy riêng của nước đá bằng điện trở nung, "
               "vì sao phải đợi cho nước đá bắt đầu tan rồi mới bắt đầu bấm giờ?",
             o=["Để toàn bộ nhiệt lượng cung cấp chỉ dùng cho việc nóng chảy, không bị dùng để "
                "làm nóng nước đá lên tới 0 °C.",
                "Để nước đá kịp hấp thụ nhiệt lượng từ không khí xung quanh, nhờ đó rút ngắn được thời gian làm thí nghiệm.",
                "Để dòng điện qua điện trở nung kịp đạt trạng thái ổn định, giúp công suất đọc trên oát kế được chính xác.",
                "Để khối lượng nước đá trong bình kịp giảm xuống đúng một giá trị đã biết trước khi bắt đầu phép đo."],
             a="A",
             e="Công thức λ = P·t/m chỉ đúng khi toàn bộ năng lượng P·t được dùng cho quá trình "
               "nóng chảy. Nếu bắt đầu đo lúc đá còn ở nhiệt độ âm thì một phần năng lượng bị "
               "dùng để làm nóng đá, khiến λ tính được lớn hơn giá trị thực.",
             fig="h11_do_nhiet_nong_chay"),

        dict(q="Thả một cục nước đá ở 0 °C vào một cốc nước ở 0 °C, cả hệ cách nhiệt. "
               "Sau một thời gian dài",
             o=["không có gì thay đổi, cả hai vẫn giữ nguyên trạng thái và nhiệt độ 0 °C.",
                "cục nước đá sẽ tan dần thành nước lỏng ở nhiệt độ 0 °C.",
                "nước trong cốc sẽ đông đặc dần thành nước đá và toả nhiệt.",
                "nhiệt độ của cả hệ sẽ giảm dần xuống thấp hơn 0 °C."],
             a="A",
             e="Hai vật cùng nhiệt độ 0 °C nên đã ở trạng thái cân bằng nhiệt, không có dòng "
               "nhiệt nào giữa chúng. Hệ lại cách nhiệt nên không có năng lượng từ ngoài vào. "
               "Không có nhiệt lượng thì không thể có nóng chảy hay đông đặc, vì cả hai quá "
               "trình đều đòi hỏi trao đổi nhiệt."),

        dict(q="Người ta cung cấp cùng một nhiệt lượng cho hai vật A và B cùng khối lượng, "
               "làm nhiệt độ vật A tăng 30 °C và vật B tăng 10 °C. Kết luận đúng là",
             o=["nhiệt dung riêng của B gấp 3 lần của A.",
                "nhiệt dung riêng của A gấp 3 lần của B.",
                "nội năng của B tăng gấp 3 lần nội năng của A.",
                "nhiệt dung riêng của hai vật bằng nhau."],
             a="A",
             e="Từ Q = mcΔT với Q và m như nhau, c tỉ lệ nghịch với ΔT. "
               "c_B/c_A = ΔT_A/ΔT_B = 30/10 = 3. Về nội năng, cả hai vật nhận cùng một nhiệt "
               "lượng và không sinh công nên độ TĂNG nội năng của chúng bằng nhau."),

        dict(q="Một khối khí lí tưởng thực hiện quá trình đẳng nhiệt và nhận nhiệt lượng 500 J. "
               "Công mà khối khí sinh ra là",
             o=["500 J.", "0 J.", "1000 J.", "250 J."],
             a="A",
             e="Nội năng của khí lí tưởng chỉ phụ thuộc nhiệt độ, mà quá trình đẳng nhiệt có "
               "T không đổi nên ΔU = 0. Từ ΔU = A + Q suy ra A = −Q = −500 J, nghĩa là khí sinh "
               "công 500 J. Toàn bộ nhiệt lượng nhận vào được chuyển thành công."),

        dict(q="Nếu thang nhiệt độ Kelvin được thay bằng một thang X sao cho X = 2·T(K), "
               "thì công thức nhiệt lượng Q = m·c·ΔT phải được viết lại thành",
             o=["Q = m·c·ΔX/2, với c giữ nguyên giá trị cũ.",
                "Q = m·c·ΔX, với c giữ nguyên giá trị cũ.",
                "Q = 2·m·c·ΔX, với c giữ nguyên giá trị cũ.",
                "Q = m·c·(ΔX + 273), với c giữ nguyên giá trị cũ."],
             a="A",
             e="Từ X = 2T suy ra ΔX = 2ΔT, tức ΔT = ΔX/2. Thay vào Q = mcΔT được Q = mc·ΔX/2. "
               "Vì X tỉ lệ thuần với T nên phép đổi độ biến thiên chỉ là nhân hệ số, không có "
               "số hạng cộng thêm 273."),

        dict(q="Một ấm điện công suất 1500 W đun 1,5 kg nước từ 25 °C. Bỏ qua mọi hao phí, "
               "thời gian để nước bắt đầu sôi là (c = 4200 J/(kg·K))",
             o=["315 s.", "210 s.", "420 s.", "630 s."],
             a="A",
             e="Nhiệt lượng cần: Q = 1,5·4200·(100 − 25) = 1,5·4200·75 = 472 500 J. "
               "Thời gian t = Q/P = 472 500/1500 = 315 s. Kết quả 420 s ứng với việc dùng nhầm "
               "ΔT = 100 °C thay vì 75 °C."),

        dict(q="Cùng để trong tủ lạnh một thời gian như nhau, một cốc nước và một cốc dầu ăn "
               "cùng khối lượng và cùng nhiệt độ ban đầu. Biết c_dầu < c_nước và tốc độ toả "
               "nhiệt của hai cốc là như nhau. Kết quả là",
             o=["dầu ăn nguội nhanh hơn nước.",
                "nước nguội nhanh hơn dầu ăn.",
                "hai cốc nguội với tốc độ như nhau.",
                "nước nguội nhanh hơn lúc đầu rồi chậm hơn về sau."],
             a="A",
             e="Với cùng nhiệt lượng toả ra trong cùng thời gian, độ giảm nhiệt độ ΔT = Q/(mc) "
               "tỉ lệ nghịch với c. Dầu có c nhỏ hơn nên nhiệt độ giảm nhanh hơn. Đây cũng là lí "
               "do dầu trong chảo nóng lên rất nhanh so với nước."),

        dict(q="Trong công thức Q = m·c·ΔT, nếu đề bài cho ΔT = 30 °C thì khi tính toán ta",
             o=["dùng trực tiếp giá trị 30, vì độ biến thiên nhiệt độ theo °C và theo K bằng nhau.",
                "phải đổi thành 303 K rồi mới thay vào công thức tính nhiệt lượng.",
                "phải đổi thành 243 K rồi mới thay vào công thức tính nhiệt lượng.",
                "phải chia giá trị đó cho 273 rồi mới thay vào công thức tính nhiệt lượng."],
             a="A",
             e="Thang Celsius và thang Kelvin có cùng độ chia, chỉ khác gốc. Khi lấy hiệu hai "
               "nhiệt độ, hằng số 273,15 bị triệt tiêu nên ΔT(K) = Δt(°C). Việc cộng 273 vào "
               "một ĐỘ BIẾN THIÊN là sai lầm rất phổ biến."),
    ],

    # ------------------------------------------------------------------ MỨC 4
    L4: [
        dict(q="Một học sinh lập luận: ”Vì nội năng của khí lí tưởng chỉ phụ thuộc nhiệt độ, "
               "nên khi khí lí tưởng dãn nở mà nhiệt độ không đổi thì nó không trao đổi năng "
               "lượng với bên ngoài.“ Nhận xét nào sau đây đúng?",
             o=["Lập luận sai ở kết luận: nội năng không đổi nhưng khí vẫn nhận nhiệt và sinh "
                "công với độ lớn bằng nhau.",
                "Lập luận hoàn toàn đúng, cả ở tiền đề lẫn ở kết luận được rút ra.",
                "Lập luận sai ngay ở tiền đề: nội năng của khí lí tưởng còn phụ thuộc cả vào thể tích của khối khí.",
                "Lập luận sai vì trên thực tế khí lí tưởng không thể thực hiện được quá trình dãn nở đẳng nhiệt."],
             a="A",
             e="Tiền đề đúng: với khí lí tưởng, U chỉ phụ thuộc T. Nhưng ΔU = 0 chỉ có nghĩa là "
               "TỔNG A + Q bằng không, chứ không có nghĩa cả hai đều bằng không. Thực tế khí "
               "nhận nhiệt Q > 0 và sinh công A = −Q, tức là có trao đổi năng lượng rất mạnh "
               "theo cả hai chiều nhưng chúng cân bằng nhau."),

        dict(q="Thả đồng thời vào một bình cách nhiệt chứa 1,0 kg nước ở 60 °C hai vật: một cục "
               "nước đá 0,10 kg ở 0 °C và một miếng nhôm 0,10 kg ở 0 °C. Cho λ = 3,34·10⁵ J/kg, "
               "c_nước = 4200, c_nhôm = 880 J/(kg·K). Nhận định nào sau đây đúng?",
             o=["Cục nước đá làm nhiệt độ cuối giảm nhiều hơn miếng nhôm, chủ yếu do nhiệt "
                "nóng chảy.",
                "Miếng nhôm làm nhiệt độ cuối giảm nhiều hơn vì kim loại dẫn nhiệt tốt hơn.",
                "Hai vật gây ra độ giảm nhiệt độ như nhau vì cùng khối lượng và cùng nhiệt độ.",
                "Cả hai vật đều không làm thay đổi nhiệt độ vì chúng ở 0 °C."],
             a="A",
             e="Nhiệt lượng cần để làm tan 0,10 kg đá đã là 0,10·3,34·10⁵ = 33 400 J, rồi còn "
               "phải làm nước tan nóng lên. Trong khi đó miếng nhôm chỉ thu 0,10·880·Δt, "
               "cỡ vài nghìn jun. Vậy cục nước đá “hút” nhiệt mạnh hơn hẳn, chủ yếu nhờ nhiệt "
               "nóng chảy. Khả năng dẫn nhiệt chỉ ảnh hưởng tới TỐC ĐỘ đạt cân bằng chứ không "
               "ảnh hưởng tới nhiệt độ cân bằng cuối cùng."),

        dict(q="Người ta đun một chất lỏng bằng nguồn nhiệt có công suất không đổi và ghi lại: "
               "trong 4 phút đầu nhiệt độ tăng từ 20 °C lên 60 °C, sau đó nhiệt độ giữ nguyên "
               "60 °C trong 12 phút. Bỏ qua hao phí. Tỉ số giữa nhiệt hoá hơi riêng L và nhiệt "
               "dung riêng c của chất lỏng đó là",
             o=["120 K.", "40 K.", "3 K.", "480 K."],
             a="A",
             e="Giai đoạn nóng lên: P·t₁ = m·c·ΔT với t₁ = 4 phút, ΔT = 40 K. "
               "Giai đoạn hoá hơi: P·t₂ = m·L với t₂ = 12 phút. "
               "Chia hai vế: t₂/t₁ = L/(c·ΔT) → L/c = ΔT·t₂/t₁ = 40·12/4 = 120 K. "
               "Kết quả 3 chỉ là tỉ số thời gian, còn thiếu thừa số ΔT."),

        dict(q="Một bình cách nhiệt chứa m gam nước ở 80 °C. Người ta thả vào đó lần lượt từng "
               "cục nước đá 10 g ở 0 °C, mỗi lần chờ cân bằng rồi mới thả cục tiếp theo. "
               "Nhận định nào sau đây đúng?",
             o=["Mỗi cục đá thả sau làm nhiệt độ giảm ít hơn cục trước, cho tới khi có cục "
                "không tan hết và nhiệt độ dừng ở 0 °C.",
                "Mỗi cục đá làm nhiệt độ giảm đúng bằng nhau vì cùng khối lượng và cùng nhiệt độ.",
                "Mỗi cục đá thả sau làm nhiệt độ của bình giảm nhiều hơn cục trước đó, vì nước trong bình đã nguội sẵn.",
                "Nhiệt độ giảm đều đặn cho tới khi đạt 0 °C, sau đó mọi cục đá thả thêm vào đều vẫn tiếp tục tan hết."],
             a="A",
             e="Sau mỗi lần, khối lượng nước trong bình TĂNG (do đá tan thành nước) trong khi "
               "nhiệt lượng mà một cục đá lấy đi gần như không đổi. Nhiệt lượng lấy đi chia cho "
               "khối lượng ngày càng lớn nên độ giảm nhiệt độ ngày càng nhỏ. Quá trình dừng khi "
               "nhiệt lượng nước còn có thể toả ra để về 0 °C không đủ làm tan hết cục đá tiếp theo."),

        dict(q="Hai bình cách nhiệt giống nhau, bình 1 chứa 1 kg nước ở 90 °C, bình 2 chứa 1 kg "
               "nước ở 10 °C. Người ta múc 100 g nước từ bình 1 sang bình 2, khuấy đều rồi múc "
               "lại 100 g hỗn hợp từ bình 2 trở về bình 1. So với ban đầu, tổng nội năng của "
               "hai bình",
             o=["không đổi, nhưng chênh lệch nhiệt độ giữa hai bình đã giảm.",
                "tăng lên vì đã thực hiện công khuấy.",
                "giảm đi vì một phần nhiệt đã bị mất khi chuyển nước.",
                "không đổi và chênh lệch nhiệt độ giữa hai bình cũng không đổi."],
             a="A",
             e="Hệ hai bình được cách nhiệt và không trao đổi năng lượng với bên ngoài (bỏ qua "
               "công khuấy), nên tổng nội năng bảo toàn. Tuy nhiên việc trộn đã làm nhiệt truyền "
               "từ phần nước nóng sang phần nước lạnh, khiến bình 1 nguội đi và bình 2 ấm lên, "
               "tức chênh lệch nhiệt độ giảm. Đây là biểu hiện của tính không thuận nghịch: "
               "năng lượng bảo toàn nhưng độ chênh lệch thì tự san bằng."),

        dict(q="Trong thí nghiệm đo nhiệt dung riêng của nước, một học sinh chọn nhiệt độ đầu "
               "thấp hơn nhiệt độ phòng 5 °C và dừng đo khi nhiệt độ cao hơn nhiệt độ phòng "
               "5 °C. Mục đích của cách làm này là",
             o=["để nhiệt lượng nhận từ môi trường ở nửa đầu bù trừ gần đúng với nhiệt lượng "
                "mất ra môi trường ở nửa sau.",
                "để nước trong nhiệt lượng kế không bị sôi trong suốt quá trình đo đạc.",
                "để nhiệt kế hoạt động chính xác hơn, do nó được hiệu chuẩn ở gần nhiệt độ phòng.",
                "để rút ngắn thời gian làm thí nghiệm, nhờ đó giảm được sai số ngẫu nhiên khi đọc số."],
             a="A",
             e="Khi nước lạnh hơn phòng, nó NHẬN thêm nhiệt từ môi trường; khi nước nóng hơn "
               "phòng, nó MẤT nhiệt ra môi trường. Chọn hai khoảng đối xứng qua nhiệt độ phòng "
               "làm hai sai số này gần bằng nhau về độ lớn nhưng ngược dấu nên triệt tiêu phần "
               "lớn. Đây là một kĩ thuật loại trừ sai số hệ thống rất kinh điển."),

        dict(q="Cho đồ thị đun nóng một chất từ thể rắn tới thể hơi, cung cấp nhiệt đều. "
               "So với đoạn nằm ngang ứng với nóng chảy, đoạn nằm ngang ứng với sự sôi dài hơn "
               "6,8 lần. Điều đó cho biết",
             o=["nhiệt hoá hơi riêng của chất lớn hơn nhiệt nóng chảy riêng khoảng 6,8 lần.",
                "nhiệt độ sôi của chất lớn hơn nhiệt độ nóng chảy khoảng 6,8 lần.",
                "nhiệt dung riêng của thể hơi lớn hơn của thể rắn khoảng 6,8 lần.",
                "khối lượng chất ở giai đoạn sôi lớn hơn 6,8 lần so với giai đoạn nóng chảy."],
             a="A",
             e="Với công suất cấp nhiệt P không đổi và khối lượng m không đổi, giai đoạn nóng "
               "chảy có P·t₁ = λm, giai đoạn sôi có P·t₂ = Lm. Chia hai vế: t₂/t₁ = L/λ. "
               "Vậy tỉ số độ dài hai đoạn nằm ngang chính là tỉ số L/λ ≈ 6,8 — đúng với trường "
               "hợp của nước.",
             fig="h04_do_thi_dun_nuoc_da"),

        dict(q="Một khối khí thực hiện quá trình sao cho nội năng của nó tăng 400 J trong khi "
               "nó toả ra môi trường 200 J nhiệt lượng. Công mà môi trường đã thực hiện lên "
               "khối khí là",
             o=["600 J.", "200 J.", "400 J.", "−600 J."],
             a="A",
             e="Khí TOẢ nhiệt nên Q = −200 J. Từ ΔU = A + Q suy ra A = ΔU − Q = 400 − (−200) "
               "= 600 J. Giá trị dương cho biết khí NHẬN công, tức môi trường đã thực hiện công "
               "600 J lên khí (khí bị nén). Kết quả 200 J ứng với việc trừ nhầm dấu."),

        dict(q="Hai vật A và B có cùng nhiệt dung C = m·c. Vật A ở 100 °C, vật B ở 0 °C. "
               "Nếu cho tiếp xúc trực tiếp thì nhiệt độ cân bằng là 50 °C. Nếu thay vào đó dùng "
               "một máy nhiệt lí tưởng hoạt động giữa hai vật để sinh công, nhiệt độ chung cuối "
               "cùng sẽ",
             o=["thấp hơn 50 °C, vì một phần năng lượng đã chuyển thành công.",
                "vẫn đúng bằng 50 °C, vì năng lượng luôn được bảo toàn.",
                "cao hơn 50 °C, vì máy nhiệt sinh thêm nhiệt do ma sát.",
                "bằng 0 °C, vì máy nhiệt lấy hết nhiệt của vật nóng."],
             a="A",
             e="Trong trường hợp tiếp xúc trực tiếp, toàn bộ nội năng ở lại trong hệ hai vật nên "
               "nhiệt độ cuối là trung bình 50 °C. Nếu chèn một máy nhiệt vào giữa, một phần "
               "năng lượng được lấy ra khỏi hệ dưới dạng công có ích, nên nội năng còn lại trong "
               "hai vật ít hơn và nhiệt độ chung cuối cùng thấp hơn 50 °C. Đây là một kết quả "
               "quan trọng của nhiệt động lực học."),

        dict(q="Người ta cho rằng: ”Trong bình cách nhiệt, khi trộn hai lượng nước thì nhiệt độ "
               "cân bằng luôn là trung bình cộng của hai nhiệt độ ban đầu.“ Nhận xét đúng là",
             o=["chỉ đúng khi hai lượng nước có khối lượng bằng nhau.",
                "luôn đúng vì nước có cùng nhiệt dung riêng.",
                "luôn sai vì nhiệt độ cân bằng phải nghiêng về phía nước nóng.",
                "chỉ đúng khi hai lượng nước có nhiệt độ chênh nhau không quá 10 °C."],
             a="A",
             e="Công thức đúng là t = (m₁t₁ + m₂t₂)/(m₁ + m₂), tức trung bình có TRỌNG SỐ theo "
               "khối lượng. Nó rút gọn thành trung bình cộng khi và chỉ khi m₁ = m₂. "
               "Nhiệt độ cân bằng nghiêng về phía lượng nước có khối lượng lớn hơn, chứ không "
               "phải luôn nghiêng về phía nóng."),

        dict(q="Một bình chứa hỗn hợp gồm 0,50 kg nước và 0,50 kg nước đá ở 0 °C. Người ta cung "
               "cấp cho bình nhiệt lượng 1,0·10⁵ J. Cho λ = 3,34·10⁵ J/kg, c = 4200 J/(kg·K). "
               "Trạng thái cuối của bình là",
             o=["hỗn hợp nước và đá ở 0 °C, với khoảng 0,20 kg đá còn lại.",
                "toàn bộ chuyển thành nước ở nhiệt độ khoảng 0 °C.",
                "toàn bộ chuyển thành nước ở nhiệt độ khoảng 12 °C.",
                "hỗn hợp nước và đá ở nhiệt độ khoảng 5 °C."],
             a="A",
             e="Để làm tan hết 0,50 kg đá cần 0,50·3,34·10⁵ = 167 000 J, lớn hơn 1,0·10⁵ J đã "
               "cung cấp nên đá không thể tan hết. Khối lượng đá tan được là "
               "1,0·10⁵/3,34·10⁵ ≈ 0,299 kg, còn lại 0,50 − 0,299 ≈ 0,20 kg đá. "
               "Vì trong bình vẫn tồn tại đồng thời nước và đá nên nhiệt độ bắt buộc giữ nguyên "
               "0 °C: một hỗn hợp nước – đá cân bằng không thể có nhiệt độ khác 0 °C."),

        dict(q="Một học sinh nói: ”Cùng một vật, nếu tôi nung nó bằng cách cọ xát thì nội năng "
               "của nó sẽ khác với khi tôi nung nó bằng lửa, dù nhiệt độ cuối như nhau.“ "
               "Nhận xét đúng là",
             o=["sai, vì nội năng là hàm trạng thái nên chỉ phụ thuộc trạng thái cuối, "
                "không phụ thuộc cách đạt tới.",
                "đúng, vì cọ xát là thực hiện công còn nung bằng lửa là truyền nhiệt, hai cách cho kết quả khác nhau.",
                "đúng, vì cọ xát chỉ làm nóng lớp bề mặt của vật còn nung bằng lửa thì làm nóng toàn bộ vật.",
                "sai, vì cọ xát không phải là cách có thể làm tăng nội năng của một vật rắn."],
             a="A",
             e="Đây chính là ý nghĩa của việc nội năng là HÀM TRẠNG THÁI: hai vật giống hệt nhau "
               "ở cùng nhiệt độ, cùng thể tích, cùng thể thì có cùng nội năng, bất kể lịch sử "
               "của chúng. Cách đưa năng lượng vào (công hay nhiệt) khác nhau, nhưng kết quả "
               "trạng thái thì như nhau."),

        dict(q="Cùng công suất cấp nhiệt, người ta đun hai bình: bình X chứa 1 kg nước, bình Y "
               "chứa 1 kg hỗn hợp gồm 0,5 kg nước và 0,5 kg nước đá, cả hai đều bắt đầu ở 0 °C. "
               "Sau 5 phút, so sánh nhiệt độ hai bình:",
             o=["Bình X có nhiệt độ cao hơn hẳn bình Y, và bình Y có thể vẫn ở 0 °C.",
                "Hai bình có nhiệt độ như nhau vì cùng khối lượng và cùng nhiệt độ đầu.",
                "Bình Y có nhiệt độ cao hơn vì nước đá dẫn nhiệt tốt hơn nước.",
                "Bình X ở 0 °C còn bình Y đã tăng nhiệt độ."],
             a="A",
             e="Ở bình X, toàn bộ nhiệt lượng dùng để tăng nhiệt độ nước. Ở bình Y, nhiệt lượng "
               "trước hết phải làm tan 0,5 kg đá, tiêu tốn 0,5·3,34·10⁵ = 167 000 J, tương đương "
               "với việc đun 1 kg nước tăng gần 40 °C. Trong 5 phút đầu rất có thể đá chưa tan "
               "hết nên bình Y vẫn giữ 0 °C."),

        dict(q="Nhận định nào sau đây về mối liên hệ giữa Chương I và Chương II là ĐÚNG?",
             o=["Kết quả W̄ = (3/2)k_B·T của Chương II chứng minh rằng nội năng khí lí tưởng chỉ "
                "phụ thuộc nhiệt độ, điều đã được dùng ở Chương I.",
                "Kết quả W̄ = (3/2)k_B·T cho thấy nội năng khí lí tưởng phụ thuộc cả nhiệt độ "
                "lẫn áp suất.",
                "Định luật I nhiệt động lực học chỉ áp dụng được cho chất rắn và chất lỏng, "
                "không áp dụng cho chất khí.",
                "Nhiệt dung riêng của khí lí tưởng bằng 0 vì các phân tử không tương tác."],
             a="A",
             e="Với khí lí tưởng, thế năng tương tác bằng 0 nên nội năng bằng tổng động năng của "
               "các phân tử: U = N·W̄ = (3/2)N·k_B·T, chỉ chứa T. Đây là chứng minh chặt chẽ cho "
               "khẳng định ΔU = 0 trong quá trình đẳng nhiệt mà Chương I đã sử dụng. "
               "Định luật I áp dụng cho mọi hệ, và khí lí tưởng vẫn có nhiệt dung riêng khác 0."),

        dict(q="Một bình nhiệt lượng kế có nhiệt dung 200 J/K chứa 0,30 kg nước ở 20 °C. "
               "Thả vào đó một vật kim loại 0,20 kg ở 100 °C, nhiệt độ cân bằng là 26 °C. "
               "Nhiệt dung riêng của kim loại là (c_nước = 4200 J/(kg·K))",
             o=["≈ 592 J/(kg·K).", "≈ 511 J/(kg·K).", "≈ 730 J/(kg·K).", "≈ 460 J/(kg·K)."],
             a="A",
             e="Nhiệt lượng thu vào gồm hai phần: nước 0,30·4200·6 = 7560 J và bình "
               "200·6 = 1200 J, tổng 8760 J. Nhiệt lượng kim loại toả ra: "
               "0,20·c·(100 − 26) = 14,8·c. Cân bằng nhiệt: 14,8·c = 8760 → "
               "c = 8760/14,8 ≈ 592 J/(kg·K). Nếu quên nhiệt lượng kế thì sẽ được "
               "7560/14,8 ≈ 511 J/(kg·K) — đó chính là bẫy của bài."),

        dict(q="Đun một ấm nước trên bếp, khi nước đã sôi ta vặn nhỏ lửa nhưng vẫn giữ cho nước "
               "sôi. So với lúc lửa to, lúc lửa nhỏ",
             o=["nhiệt độ nước vẫn là 100 °C nhưng nước bay hơi chậm hơn.",
                "nhiệt độ nước giảm xuống dưới 100 °C và nước bay hơi chậm hơn.",
                "nhiệt độ nước vẫn là 100 °C và tốc độ bay hơi không đổi.",
                "nhiệt độ nước tăng lên trên 100 °C vì nhiệt tích tụ lâu hơn."],
             a="A",
             e="Chừng nào nước còn sôi ở cùng áp suất thì nhiệt độ luôn là 100 °C, không phụ "
               "thuộc độ lớn của lửa. Điều thay đổi là công suất cấp nhiệt: lửa nhỏ cung cấp ít "
               "jun mỗi giây hơn nên khối lượng nước hoá hơi mỗi giây (m = P/L) nhỏ hơn, tức "
               "nước cạn chậm hơn. Đây là lí do vặn nhỏ lửa khi ninh giúp tiết kiệm mà thức ăn "
               "vẫn chín."),
    ],
}

DS1 = [
    dict(stem="Một học sinh làm thí nghiệm đun nóng đều một khối nước đá khối lượng 0,40 kg "
              "lấy từ tủ lạnh ở −20 °C bằng một bếp có công suất không đổi, thu được đồ thị "
              "nhiệt độ theo thời gian như hình vẽ. Cho c_đá = 2100 J/(kg·K), "
              "c_nước = 4200 J/(kg·K), λ = 3,34·10⁵ J/kg, L = 2,26·10⁶ J/kg.",
         fig="h04_do_thi_dun_nuoc_da",
         items=[
             ("Trong giai đoạn ② và giai đoạn ④, nhiệt độ của hệ không đổi nên nội năng của hệ "
              "cũng không đổi.", False,
              "Nhiệt độ không đổi chỉ có nghĩa là động năng trung bình của phân tử không đổi. "
              "Hệ vẫn liên tục nhận nhiệt lượng từ bếp và toàn bộ năng lượng đó được tích luỹ "
              "dưới dạng thế năng tương tác phân tử, nên nội năng VẪN TĂNG."),
             ("Nhiệt lượng cần cho giai đoạn ① là 16,8 kJ.", True,
              "Q₁ = m·c_đá·ΔT = 0,40·2100·20 = 16 800 J = 16,8 kJ."),
             ("Nhiệt lượng cần cho giai đoạn ④ lớn hơn nhiệt lượng cần cho giai đoạn ② "
              "khoảng 6,8 lần.", True,
              "Q₄ = m·L = 0,40·2,26·10⁶ = 904 000 J và Q₂ = m·λ = 0,40·3,34·10⁵ = 133 600 J. "
              "Tỉ số Q₄/Q₂ = 904 000/133 600 ≈ 6,77 ≈ 6,8. Vì bếp có công suất không đổi nên tỉ "
              "số này cũng chính là tỉ số độ dài hai đoạn nằm ngang trên đồ thị."),
             ("Tổng nhiệt lượng để đưa toàn bộ khối nước đá từ −20 °C thành hơi nước ở 100 °C "
              "xấp xỉ 1,22 MJ.", True,
              "Q₁ = 16 800 J; Q₂ = 133 600 J; Q₃ = 0,40·4200·100 = 168 000 J; Q₄ = 904 000 J. "
              "Tổng = 16 800 + 133 600 + 168 000 + 904 000 = 1 222 400 J ≈ 1,22 MJ."),
         ]),

    dict(stem="Một khối khí lí tưởng được chứa trong một xilanh có pit-tông. Người ta thực hiện "
              "ba quá trình khác nhau với khối khí này: quá trình (I) khí nhận 500 J nhiệt lượng "
              "và bị nén, môi trường thực hiện lên khí công 200 J; quá trình (II) khí bị giữ "
              "trong bình cứng và nhận 500 J nhiệt lượng; quá trình (III) khí dãn nở đẳng nhiệt "
              "và nhận 500 J nhiệt lượng.",
         items=[
             ("Trong quá trình (I), nội năng của khí tăng 700 J.", True,
              "Khí nhận nhiệt nên Q = +500 J; khí nhận công nên A = +200 J. "
              "ΔU = A + Q = 200 + 500 = 700 J, nội năng tăng 700 J."),
             ("Trong quá trình (II), nội năng của khí tăng 500 J.", True,
              "Bình cứng nên thể tích không đổi, A = 0. Do đó ΔU = Q = 500 J."),
             ("Trong quá trình (III), nội năng của khí tăng 500 J.", False,
              "Quá trình đẳng nhiệt của khí lí tưởng có nhiệt độ không đổi, mà nội năng khí lí "
              "tưởng chỉ phụ thuộc nhiệt độ nên ΔU = 0. Toàn bộ 500 J nhiệt lượng nhận vào được "
              "chuyển thành công khí sinh ra: A = −500 J."),
             ("Trong cả ba quá trình, khí đều nhận cùng một nhiệt lượng nên độ tăng nội năng "
              "của khí là như nhau.", False,
              "Ba quá trình cho ΔU lần lượt là 700 J, 500 J và 0 J. Nhiệt lượng chỉ là một trong "
              "hai kênh trao đổi năng lượng; kết quả còn phụ thuộc công trao đổi, nên cùng Q "
              "hoàn toàn không dẫn tới cùng ΔU."),
         ]),

    dict(stem="Để đo nhiệt dung riêng của một chất lỏng, một nhóm học sinh dùng nhiệt lượng kế "
              "có vỏ cách nhiệt, bên trong đặt một điện trở nung nối với oát kế. Nhóm đổ vào "
              "0,25 kg chất lỏng, bật nguồn với công suất 40 W và ghi lại độ tăng nhiệt độ "
              "theo thời gian, thu được bảng số liệu sau.",
         tbl=("Bảng số liệu thí nghiệm đo nhiệt dung riêng",
              ["Thời gian t (s)", "60", "120", "180", "240", "300"],
              [["Độ tăng nhiệt độ ΔT (K)", "2,4", "4,8", "7,2", "9,6", "12,0"]]),
         items=[
             ("Đồ thị ΔT theo t là một đường thẳng đi qua gốc toạ độ.", True,
              "Tỉ số ΔT/t ở cả năm lần đo đều bằng 0,040 K/s (2,4/60 = 4,8/120 = ... = 0,040). "
              "Tỉ số không đổi chứng tỏ quan hệ tỉ lệ thuận, đồ thị là đường thẳng qua gốc."),
             ("Nhiệt dung riêng của chất lỏng tính được từ số liệu là 4000 J/(kg·K).", True,
              "Từ P·t = m·c·ΔT suy ra c = P/(m·(ΔT/t)) = 40/(0,25·0,040) = 40/0,010 "
              "= 4000 J/(kg·K)."),
             ("Nếu vỏ cách nhiệt không hoàn hảo và chất lỏng bị mất nhiệt ra môi trường thì "
              "giá trị c đo được sẽ nhỏ hơn giá trị thực.", False,
              "Mất nhiệt ra ngoài làm độ tăng nhiệt độ nhỏ hơn đáng lẽ phải có, trong khi ta vẫn "
              "tính với toàn bộ năng lượng điện P·t. Mẫu số ΔT nhỏ đi nên c = P·t/(m·ΔT) thu được "
              "LỚN hơn giá trị thực, chứ không nhỏ hơn."),
             ("Nếu thay chất lỏng bằng cùng khối lượng nước có c = 4200 J/(kg·K) và giữ nguyên "
              "công suất thì sau 300 s độ tăng nhiệt độ sẽ nhỏ hơn 12,0 K.", True,
              "ΔT = P·t/(m·c) = 40·300/(0,25·4200) = 12 000/1050 ≈ 11,4 K < 12,0 K. "
              "Nước có nhiệt dung riêng lớn hơn nên nóng lên chậm hơn."),
         ]),

    dict(stem="Trong một bình cách nhiệt lí tưởng chứa 2,0 kg nước ở 50 °C, người ta thả vào "
              "0,50 kg nước đá ở 0 °C. Cho c_nước = 4200 J/(kg·K), λ = 3,34·10⁵ J/kg.",
         items=[
             ("Nhiệt lượng cần để làm tan hoàn toàn khối nước đá là 167 kJ.", True,
              "Q = λ·m = 3,34·10⁵ · 0,50 = 167 000 J = 167 kJ."),
             ("Nhiệt lượng mà 2,0 kg nước toả ra khi hạ từ 50 °C xuống 0 °C là 420 kJ.", True,
              "Q = m·c·ΔT = 2,0·4200·50 = 420 000 J = 420 kJ."),
             ("Nước đá không tan hết và nhiệt độ cuối cùng của hỗn hợp là 0 °C.", False,
              "Nước nóng có thể toả tới 420 kJ, lớn hơn 167 kJ cần để làm tan hết đá, "
              "nên đá TAN HOÀN TOÀN và nhiệt độ cuối cao hơn 0 °C."),
             ("Nhiệt độ cân bằng của hỗn hợp xấp xỉ 24,1 °C.", True,
              "Gọi t là nhiệt độ cân bằng. Nước nóng toả: 2,0·4200·(50 − t). "
              "Đá thu: 167 000 + 0,50·4200·t. Cân bằng: 8400(50 − t) = 167 000 + 2100t "
              "→ 420 000 − 8400t = 167 000 + 2100t → 253 000 = 10 500t → t ≈ 24,1 °C."),
         ]),

    dict(stem="Xét các phát biểu về sự bay hơi và sự sôi của chất lỏng.",
         fig="h12_bay_hoi_va_soi",
         items=[
             ("Sự bay hơi chỉ xảy ra ở mặt thoáng, còn sự sôi xảy ra cả ở mặt thoáng và trong "
              "lòng chất lỏng.", True,
              "Đây là điểm phân biệt cơ bản nhất giữa hai hiện tượng. Trong sự sôi, hơi hình "
              "thành thành các bọt khí ngay trong lòng chất lỏng rồi nổi lên vỡ ở mặt thoáng."),
             ("Sự bay hơi chỉ xảy ra khi chất lỏng đạt tới nhiệt độ sôi.", False,
              "Bay hơi xảy ra ở MỌI nhiệt độ, vì ở bất kì nhiệt độ nào cũng có những phân tử ở "
              "mặt thoáng có động năng đủ lớn để thắng lực hút và thoát ra. Quần áo phơi ngoài "
              "trời vẫn khô dù nhiệt độ xa 100 °C."),
             ("Trong suốt thời gian sôi ở áp suất không đổi, nhiệt độ của chất lỏng không đổi.",
              True,
              "Toàn bộ nhiệt lượng cung cấp được dùng để hoá hơi (Q = Lm), làm tăng thế năng "
              "tương tác chứ không làm tăng động năng trung bình, nên nhiệt độ giữ nguyên."),
             ("Khi mồ hôi bay hơi khỏi da, cơ thể nóng lên vì quá trình bay hơi toả nhiệt.",
              False,
              "Bay hơi là quá trình THU nhiệt: các phân tử phải nhận năng lượng để thoát khỏi "
              "chất lỏng, và năng lượng đó lấy từ cơ thể. Ngoài ra chính những phân tử nhanh "
              "nhất ra đi làm phần còn lại nguội đi. Vì vậy bay hơi mồ hôi làm cơ thể MÁT."),
         ]),

    dict(stem="Hai vật A và B làm bằng hai chất khác nhau, có cùng khối lượng m = 0,50 kg. "
              "Vật A có c_A = 900 J/(kg·K), vật B có c_B = 450 J/(kg·K). Ban đầu vật A ở 20 °C, "
              "vật B ở 80 °C. Cho hai vật tiếp xúc nhiệt với nhau trong bình cách nhiệt.",
         items=[
             ("Nhiệt sẽ truyền từ vật B sang vật A.", True,
              "Chiều truyền nhiệt được quyết định bởi chênh lệch nhiệt độ. Vật B ở 80 °C nóng "
              "hơn vật A ở 20 °C nên nhiệt truyền từ B sang A."),
             ("Nhiệt độ cân bằng của hệ là 50 °C.", False,
              "t = (m·c_A·t_A + m·c_B·t_B)/(m·c_A + m·c_B) = (900·20 + 450·80)/(900 + 450) "
              "= (18 000 + 36 000)/1350 = 54 000/1350 = 40 °C. Nhiệt độ cân bằng lệch về phía "
              "vật có tích m·c lớn hơn, tức về phía vật A (20 °C), nên phải nhỏ hơn 50 °C."),
             ("Độ giảm nhiệt độ của vật B lớn gấp đôi độ tăng nhiệt độ của vật A.", True,
              "Vì nhiệt lượng trao đổi bằng nhau: m·c_A·ΔT_A = m·c_B·ΔT_B, nên "
              "ΔT_B/ΔT_A = c_A/c_B = 900/450 = 2. Kiểm chứng bằng số: vật A tăng từ 20 lên 40, "
              "tức 20 K; vật B giảm từ 80 xuống 40, tức 40 K."),
             ("Tổng nội năng của hai vật sau khi cân bằng nhỏ hơn tổng nội năng ban đầu.", False,
              "Bình cách nhiệt nên hệ không trao đổi năng lượng với bên ngoài và không sinh công. "
              "Nội năng được bảo toàn: phần vật B mất đi đúng bằng phần vật A nhận thêm."),
         ]),

    dict(stem="Xét các nhận định về nội năng và các cách làm biến đổi nội năng.",
         fig="h06_hai_cach_doi_noi_nang",
         items=[
             ("Nội năng của một vật luôn có thể được xác định nếu biết trạng thái của vật, "
              "vì nội năng là hàm trạng thái.", True,
              "Nội năng chỉ phụ thuộc trạng thái hiện tại (nhiệt độ, thể tích, khối lượng, thể "
              "của chất) chứ không phụ thuộc quá trình đưa vật tới trạng thái đó."),
             ("Có thể làm tăng nội năng của một vật mà không cần truyền nhiệt cho nó.", True,
              "Thực hiện công là cách thứ hai: cọ xát hai bàn tay, nén nhanh khí, khoan kim loại "
              "đều làm nội năng tăng mà không có dòng nhiệt từ vật nóng hơn truyền sang."),
             ("Khi nói “vật này chứa nhiều nhiệt lượng hơn vật kia” là cách nói đúng về mặt "
              "vật lí.", False,
              "Nhiệt lượng là đại lượng của QUÁ TRÌNH, mô tả năng lượng đang được truyền, "
              "không phải đại lượng mà vật “chứa”. Cách nói đúng phải là ”vật này có nội năng "
              "lớn hơn vật kia'."),
             ("Đun nóng một vật bằng lửa và cọ xát vật đó tới cùng một nhiệt độ cuối sẽ cho "
              "cùng một giá trị nội năng, nếu các điều kiện khác như nhau.", True,
              "Vì nội năng là hàm trạng thái nên hai vật ở cùng trạng thái cuối có cùng nội năng, "
              "bất kể một bên nhận năng lượng bằng truyền nhiệt còn bên kia bằng thực hiện công."),
         ]),

    dict(stem="Một bình cách nhiệt chứa 1,0 kg nước ở 90 °C. Người ta thả lần lượt vào bình các "
              "cục nước đá 0 °C, mỗi cục 50 g, mỗi lần chờ hệ cân bằng rồi mới thả cục tiếp theo. "
              "Cho c_nước = 4200 J/(kg·K), λ = 3,34·10⁵ J/kg.",
         items=[
             ("Sau khi thả cục đá thứ nhất và hệ cân bằng, nhiệt độ của bình xấp xỉ 81,9 °C.",
              True,
              "Gọi t là nhiệt độ cân bằng. Nước toả: 1,0·4200·(90 − t) = 378 000 − 4200t. "
              "Đá thu: làm tan 0,050·3,34·10⁵ = 16 700 J rồi làm nước tan nóng lên "
              "0,050·4200·t = 210t. Cân bằng: 378 000 − 4200t = 16 700 + 210t "
              "→ 361 300 = 4410t → t ≈ 81,9 °C."),
             ("Mỗi cục đá thả về sau làm nhiệt độ của bình giảm ít hơn cục thả trước đó.", True,
              "Sau mỗi lần, khối lượng nước trong bình tăng lên (do đá tan thành nước) trong khi "
              "nhiệt lượng mà một cục đá lấy đi thay đổi không nhiều. Cùng một lượng nhiệt lấy "
              "đi chia cho khối lượng lớn hơn thì độ giảm nhiệt độ nhỏ hơn."),
             ("Nếu tiếp tục thả đá thì đến một lúc nào đó sẽ có cục đá không tan hết và nhiệt độ "
              "dừng lại ở 0 °C.", True,
              "Càng thả nhiều đá, nhiệt độ bình càng thấp nên nhiệt lượng mà nước có thể toả ra "
              "để hạ về 0 °C càng ít. Đến lúc lượng nhiệt đó không đủ làm tan hết cục đá tiếp "
              "theo thì hệ dừng ở trạng thái hỗn hợp nước – đá ở đúng 0 °C."),
             ("Vì bình được cách nhiệt nên nhiệt độ của bình không thể giảm xuống dưới nhiệt "
              "độ của nước ban đầu chia đôi, tức không thể thấp hơn 45 °C.", False,
              "Cách nhiệt chỉ ngăn trao đổi nhiệt với BÊN NGOÀI, hoàn toàn không đặt ra giới "
              "hạn nào cho nhiệt độ cân bằng bên trong. Nếu thả đủ nhiều đá, nhiệt độ có thể "
              "hạ tới tận 0 °C. Cái được bảo toàn ở đây là tổng nội năng của hệ (nước ban đầu "
              "cộng toàn bộ đá đã thả vào), chứ không phải nhiệt độ."),
         ]),
]
