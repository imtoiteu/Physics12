# -*- coding: utf-8 -*-
"""NĂM ĐỀ KIỂM TRA CHƯƠNG I – VẬT LÍ NHIỆT (Vật lí 12, GDPT 2018).

Mỗi đề mô phỏng đúng cấu trúc đề thi tốt nghiệp THPT môn Vật lí (Quyết định
764/QĐ-BGDĐT): 28 câu / 40 lệnh hỏi / 50 phút
    • Phần I : 18 câu trắc nghiệm nhiều phương án lựa chọn (0,25 đ/câu → 4,5 đ)
    • Phần II:  4 câu trắc nghiệm đúng/sai, mỗi câu 4 ý (0,1–0,25–0,5–1,0 đ → 4,0 đ)
    • Phần III: 6 câu trả lời ngắn (0,25 đ/câu → 1,5 đ)

Hằng số dùng thống nhất trong cả năm đề:
    c_nước = 4200 ; c_đá = 2100 ; c_nhôm = 880 ; c_sắt = 460 ; c_đồng = 380 ;
    c_chì  = 130  J/(kg·K) ;  λ_nước đá = 3,34·10⁵ J/kg ;  L_nước = 2,26·10⁶ J/kg.

Quy ước dữ liệu:
    mc    = dict(q, o=[4 phương án], a="A".."D", sol, fig?, tbl?)
    đúng/sai = dict(stem, items=[(nội dung, True/False, giải thích) × 4], fig?, tbl?)
    ngắn  = dict(q, ans, sol, fig?, tbl?)

Lời giải luôn dẫn chiếu NỘI DUNG phương án, không dẫn chiếu chữ cái, để không sai
khi trình biên dịch hoán vị vị trí đáp án.
"""

HANG_SO = ("Cho biết: nhiệt dung riêng của nước 4200 J/(kg·K); của nước đá 2100 J/(kg·K); "
           "của nhôm 880 J/(kg·K); của sắt 460 J/(kg·K); của đồng 380 J/(kg·K); của chì "
           "130 J/(kg·K). Nhiệt nóng chảy riêng của nước đá 3,34·10⁵ J/kg; nhiệt hoá hơi "
           "riêng của nước 2,26·10⁶ J/kg. Áp suất khí quyển chuẩn; nước sôi ở 100 °C và "
           "nước đá nóng chảy ở 0 °C.")


# ===================================================================================
#                        ĐỀ SỐ 01 – KIẾN THỨC NỀN TẢNG
# ===================================================================================

DE1_P1 = [
    dict(q="Phát biểu nào sau đây về cấu tạo chất là đúng?",
         o=["Các phân tử chuyển động hỗn loạn không ngừng, nhiệt độ càng cao thì chuyển "
            "động càng nhanh.",
            "Các phân tử ở thể rắn nằm yên hoàn toàn tại các vị trí cân bằng của chúng.",
            "Giữa các phân tử của một chất chỉ có lực hút mà không có lực đẩy.",
            "Ở thể khí, khoảng cách giữa các phân tử xấp xỉ bằng kích thước phân tử."],
         a="A",
         sol="Nội dung cơ bản của mô hình động học phân tử: các chất được cấu tạo từ những "
             "hạt riêng biệt chuyển động hỗn loạn không ngừng; chuyển động này càng nhanh "
             "khi nhiệt độ càng cao. Phân tử chất rắn vẫn dao động quanh vị trí cân bằng "
             "chứ không nằm yên. Giữa các phân tử có cả lực hút và lực đẩy. Ở thể khí, "
             "khoảng cách giữa các phân tử lớn hơn rất nhiều lần kích thước phân tử."),

    dict(q="Nội năng của một vật là",
         o=["tổng động năng và thế năng tương tác của các phân tử cấu tạo nên vật.",
            "tổng động năng chuyển động nhiệt của các phân tử cấu tạo nên vật.",
            "nhiệt lượng mà vật nhận được trong suốt quá trình truyền nhiệt.",
            "tổng động năng và thế năng của vật trong trường trọng lực Trái Đất."],
         a="A",
         sol="Theo định nghĩa trong sách giáo khoa, nội năng của một vật là tổng động năng "
             "chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng. Thiếu "
             "phần thế năng tương tác thì định nghĩa chưa đủ. Nhiệt lượng là phần nội năng "
             "được truyền đi chứ không phải bản thân nội năng. Cơ năng của vật (động năng "
             "và thế năng của cả vật) không thuộc nội năng."),

    dict(q="Trong hệ SI, đơn vị của nhiệt dung riêng là",
         o=["J/(kg·K).", "J/kg.", "J/K.", "J·kg/K."],
         a="A",
         sol="Từ Q = mcΔT suy ra c = Q/(mΔT), đơn vị là J/(kg·K). Đơn vị J/kg là của nhiệt "
             "nóng chảy riêng và nhiệt hoá hơi riêng; J/K là của nhiệt dung (của cả vật)."),

    dict(q="Nhiệt độ 0 K trong thang Kelvin ứng với nhiệt độ Celsius bằng",
         o=["−273,15 °C.", "0 °C.", "100 °C.", "273,15 °C."],
         a="A",
         sol="Liên hệ giữa hai thang: T(K) = t(°C) + 273,15, do đó t = T − 273,15 = "
             "0 − 273,15 = −273,15 °C. Đây là nhiệt độ không tuyệt đối, giới hạn dưới của "
             "nhiệt độ mà mọi hệ vật chất không thể đạt tới."),

    dict(q="Trong suốt quá trình nóng chảy của một chất rắn kết tinh ở áp suất không đổi, "
           "nhiệt độ của chất",
         o=["không thay đổi cho tới khi chất nóng chảy hoàn toàn.",
            "tăng đều theo thời gian cho tới khi nóng chảy hết.",
            "giảm dần vì chất phải thu nhiệt để nóng chảy.",
            "tăng nhanh lúc đầu rồi giảm dần về sau."],
         a="A",
         sol="Chất rắn kết tinh có nhiệt độ nóng chảy xác định. Trong khi nóng chảy, toàn "
             "bộ nhiệt lượng cung cấp dùng để phá vỡ mạng tinh thể (làm tăng thế năng "
             "tương tác phân tử) chứ không làm tăng động năng chuyển động nhiệt, vì vậy "
             "nhiệt độ giữ nguyên. Chất vẫn thu nhiệt nên nhiệt độ không thể giảm."),

    dict(q="Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn một vật rắn kết tinh khối "
           "lượng m đang ở đúng nhiệt độ nóng chảy được tính bằng công thức",
         o=["Q = λm.", "Q = Lm.", "Q = mcΔT.", "Q = λm + mcΔT."],
         a="A",
         sol="λ là nhiệt nóng chảy riêng nên Q = λm. Công thức Q = Lm dùng cho sự hoá hơi "
             "(L là nhiệt hoá hơi riêng). Q = mcΔT chỉ dùng khi nhiệt độ của vật thay đổi "
             "mà không có chuyển thể; ở đây vật đã ở đúng nhiệt độ nóng chảy nên ΔT = 0."),

    dict(q="Nhiệt hoá hơi riêng của một chất lỏng cho biết",
           o=["nhiệt lượng cần cung cấp để 1 kg chất lỏng đó hoá hơi hoàn toàn ở nhiệt độ "
              "sôi của nó.",
              "nhiệt lượng cần cung cấp để 1 kg chất lỏng đó tăng thêm 1 K nhiệt độ.",
              "nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn 1 kg chất đó.",
              "nhiệt lượng toả ra khi 1 kg hơi của chất đó ngưng tụ ở nhiệt độ bất kì."],
         a="A",
         sol="Định nghĩa: nhiệt hoá hơi riêng L của một chất lỏng là nhiệt lượng cần cung "
             "cấp để 1 kg chất lỏng đó hoá hơi hoàn toàn ở nhiệt độ sôi. Nhiệt lượng làm "
             "1 kg chất tăng 1 K là nhiệt dung riêng; làm nóng chảy 1 kg là nhiệt nóng "
             "chảy riêng. Ý cuối sai ở chỗ “nhiệt độ bất kì”: giá trị L chỉ được xác định "
             "tại nhiệt độ sôi ứng với áp suất đang xét."),

    dict(q="Theo định luật I của nhiệt động lực học ΔU = A + Q, quy ước dấu nào sau đây là "
           "đúng?",
         o=["Q > 0 khi vật nhận nhiệt lượng từ bên ngoài.",
            "Q > 0 khi vật truyền nhiệt lượng ra bên ngoài.",
            "A > 0 khi vật thực hiện công lên các vật khác.",
            "ΔU > 0 khi nhiệt độ của vật giảm đi."],
         a="A",
         sol="Trong biểu thức ΔU = A + Q, cả A và Q đều là những đại lượng mà hệ NHẬN được: "
             "Q > 0 khi hệ nhận nhiệt, Q < 0 khi hệ toả nhiệt; A > 0 khi hệ nhận công (bị "
             "nén, bị cọ xát), A < 0 khi hệ thực hiện công lên bên ngoài. ΔU > 0 nghĩa là "
             "nội năng tăng, thường ứng với nhiệt độ tăng chứ không phải giảm."),

    dict(q="Khi xoa mạnh hai bàn tay vào nhau, ta thấy tay nóng lên. Nội năng của tay tăng "
           "lên chủ yếu là do",
         o=["thực hiện công.", "truyền nhiệt.",
            "bức xạ nhiệt từ môi trường.", "đối lưu của không khí quanh tay."],
         a="A",
         sol="Có hai cách làm biến đổi nội năng của một vật: thực hiện công và truyền "
             "nhiệt. Khi xoa hai bàn tay, lực ma sát sinh công lên tay, phần công này "
             "chuyển thành nội năng làm tay nóng lên. Không khí xung quanh có nhiệt độ "
             "thấp hơn tay nên không thể truyền nhiệt làm tay nóng thêm."),

    dict(q="Nhận định nào sau đây so sánh đúng sự bay hơi và sự sôi của một chất lỏng?",
         o=["Bay hơi xảy ra ở mọi nhiệt độ, chỉ trên mặt thoáng; sôi xảy ra ở nhiệt độ "
            "xác định, cả trong lòng chất lỏng.",
            "Cả hai hiện tượng đều chỉ xảy ra ngay trên mặt thoáng của khối chất lỏng "
            "đang xét.",
            "Bay hơi chỉ xảy ra ở nhiệt độ sôi, còn sự sôi thì xảy ra ở mọi nhiệt độ của "
            "chất lỏng.",
            "Cả hai hiện tượng đều chỉ xảy ra ở một nhiệt độ xác định, khác nhau với mỗi "
            "chất lỏng."],
         a="A",
         sol="Sự bay hơi xảy ra ở bất kì nhiệt độ nào và chỉ diễn ra trên mặt thoáng. Sự "
             "sôi chỉ xảy ra ở nhiệt độ sôi (ứng với áp suất đang xét) và diễn ra đồng "
             "thời cả trên mặt thoáng lẫn trong lòng chất lỏng dưới dạng các bọt hơi."),

    dict(q="Nước có nhiệt dung riêng lớn nên được dùng làm chất tải nhiệt trong hệ thống "
           "làm mát động cơ. Lí do chính là",
         o=["với cùng khối lượng và cùng độ tăng nhiệt độ, nước hấp thụ được nhiều nhiệt "
            "lượng hơn.",
            "nước có khối lượng riêng nhỏ nên chảy dễ dàng trong các ống dẫn hẹp của "
            "động cơ.",
            "nước có nhiệt độ sôi thấp nên dễ bay hơi và mang nhiệt đi khỏi động cơ rất "
            "nhanh.",
            "nước dẫn nhiệt tốt hơn hẳn các kim loại dùng để chế tạo thân của động cơ."],
         a="A",
         sol="Từ Q = mcΔT: với cùng m và cùng ΔT, chất có c càng lớn thì hấp thụ được càng "
             "nhiều nhiệt. Nước có c = 4200 J/(kg·K), lớn hơn hầu hết chất lỏng thông "
             "dụng, nên chỉ cần nóng lên ít độ đã lấy đi được nhiều nhiệt của động cơ. "
             "Nước dẫn nhiệt kém hơn kim loại rất nhiều và nhiệt độ sôi của nước không hề "
             "thấp so với nhiều chất lỏng khác."),

    dict(q="Nhiệt độ của một vật tăng từ 27 °C lên 57 °C. Độ tăng nhiệt độ của vật tính "
           "theo thang Kelvin là",
         o=["30 K.", "84 K.", "303 K.", "330 K."],
         a="A",
         sol="Vì T(K) = t(°C) + 273,15 nên khi lấy hiệu, hằng số 273,15 triệt tiêu: "
             "ΔT = T₂ − T₁ = (57 + 273,15) − (27 + 273,15) = 57 − 27 = 30 K. Sai lầm phổ "
             "biến là cộng thêm 273 vào độ chênh lệch nhiệt độ; cần nhớ một ĐỘ CHÊNH LỆCH "
             "nhiệt độ có cùng trị số trong hai thang Celsius và Kelvin."),

    dict(q="Nhiệt lượng cần cung cấp để làm 2,0 kg nước nóng lên từ 25 °C đến 75 °C là",
         o=["420 kJ.", "210 kJ.", "630 kJ.", "840 kJ."],
         a="A",
         sol="Q = mcΔT = 2,0 × 4200 × (75 − 25) = 2,0 × 4200 × 50 = 420 000 J = 420 kJ."),

    dict(q="Nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn 0,50 kg nước đá đang ở "
           "0 °C là",
         o=["1,67·10⁵ J.", "8,35·10⁴ J.", "3,34·10⁵ J.", "6,68·10⁵ J."],
         a="A",
         sol="Nước đá đã ở đúng nhiệt độ nóng chảy nên chỉ cần cung cấp nhiệt nóng chảy: "
             "Q = λm = 3,34·10⁵ × 0,50 = 1,67·10⁵ J."),

    dict(q="Một lượng khí nhận nhiệt lượng 200 J, đồng thời dãn nở và thực hiện công 120 J "
           "lên môi trường bên ngoài. Độ biến thiên nội năng của lượng khí đó là",
         o=["80 J.", "−80 J.", "320 J.", "−320 J."],
         a="A",
         sol="Khí nhận nhiệt nên Q = +200 J. Khí thực hiện công lên bên ngoài nên công mà "
             "khí NHẬN là A = −120 J. Do đó ΔU = A + Q = −120 + 200 = 80 J: nội năng của "
             "khí tăng thêm 80 J."),

    dict(q="Trộn 0,50 kg nước ở 20 °C với 0,50 kg nước ở 80 °C trong một bình cách nhiệt. "
           "Bỏ qua nhiệt dung của bình, nhiệt độ của nước khi cân bằng nhiệt là",
         o=["50 °C.", "40 °C.", "45 °C.", "60 °C."],
         a="A",
         sol="Hai khối nước cùng chất, cùng khối lượng nên nhiệt độ cân bằng là trung bình "
             "cộng: t = (20 + 80)/2 = 50 °C. Kiểm tra bằng phương trình cân bằng nhiệt: "
             "0,50 × 4200 × (t − 20) = 0,50 × 4200 × (80 − t) ⇒ t = 50 °C."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo thời gian của một khối nước đá được đun bằng "
           "nguồn nhiệt có công suất không đổi. Giai đoạn nào ứng với quá trình nước đá "
           "đang nóng chảy?",
         fig="t11a",
         o=["Giai đoạn II.", "Giai đoạn I.", "Giai đoạn III.", "Giai đoạn IV."],
         a="A",
         sol="Nước đá nóng chảy ở 0 °C và trong suốt quá trình nóng chảy nhiệt độ giữ "
             "nguyên, ứng với đoạn nằm ngang ở mức 0 °C, tức giai đoạn II. Giai đoạn I là "
             "nước đá nóng dần từ −20 °C lên 0 °C; giai đoạn III là nước lỏng nóng dần từ "
             "0 °C lên 100 °C; giai đoạn IV (nằm ngang ở 100 °C) là nước đang sôi."),

    dict(q="Nhiệt lượng cần cung cấp để 0,20 kg nước đang ở 100 °C hoá hơi hoàn toàn là",
         o=["4,52·10⁵ J.", "4,52·10⁴ J.", "2,26·10⁵ J.", "1,13·10⁶ J."],
         a="A",
         sol="Nước đã ở đúng nhiệt độ sôi nên Q = Lm = 2,26·10⁶ × 0,20 = 4,52·10⁵ J."),
]

DE1_P2 = [
    dict(stem="Hình vẽ là đồ thị nhiệt độ theo thời gian của một khối nước đá lấy từ tủ "
              "đông ra rồi đun liên tục bằng một nguồn nhiệt có công suất không đổi, ở áp "
              "suất khí quyển chuẩn.",
         fig="t11a",
         items=[
             ("Ở đầu giai đoạn I, khối nước đá có nhiệt độ −20 °C.", True,
              "Đồ thị bắt đầu tại giá trị −20 °C trên trục nhiệt độ, đúng như phát biểu."),
             ("Trong giai đoạn II, nhiệt lượng cung cấp được dùng để làm tăng nhiệt độ của "
              "nước đá.", False,
              "Giai đoạn II là đoạn nằm ngang ở 0 °C: nhiệt độ KHÔNG tăng. Toàn bộ nhiệt "
              "lượng cung cấp dùng để phá vỡ liên kết trong mạng tinh thể, tức làm nước đá "
              "nóng chảy, chứ không làm tăng động năng chuyển động nhiệt của phân tử."),
             ("Trong giai đoạn III, chất trong bình hoàn toàn ở thể lỏng.", True,
              "Giai đoạn II kết thúc khi toàn bộ nước đá đã nóng chảy hết. Sang giai đoạn "
              "III nhiệt độ mới tăng trở lại, chứng tỏ chỉ còn nước ở thể lỏng đang nóng "
              "dần từ 0 °C lên 100 °C."),
             ("Trong giai đoạn IV, nội năng của hệ không đổi vì nhiệt độ của hệ không đổi.",
              False,
              "Giai đoạn IV là quá trình sôi: nhiệt độ giữ nguyên 100 °C nhưng hệ vẫn liên "
              "tục nhận nhiệt. Nhiệt lượng này làm tăng thế năng tương tác giữa các phân "
              "tử khi nước chuyển thành hơi, nên nội năng của hệ vẫn tăng. Nhiệt độ không "
              "đổi chỉ có nghĩa là phần động năng chuyển động nhiệt trung bình không đổi."),
         ]),

    dict(stem="Hình vẽ là sơ đồ bộ thí nghiệm xác định nhiệt dung riêng của một khối kim "
              "loại. Khối kim loại khối lượng 200 g được nung nóng tới 100 °C rồi thả thật "
              "nhanh vào 300 g nước ở 25 °C đựng trong nhiệt lượng kế. Khuấy đều, nhiệt độ "
              "khi cân bằng nhiệt đo được là 30,0 °C. Trong các ý a, b, c hãy bỏ qua nhiệt "
              "lượng mà nhiệt lượng kế, que khuấy và nhiệt kế nhận được.",
         fig="t11b",
         items=[
             ("Trong quá trình tiến tới cân bằng nhiệt, nước thu nhiệt còn khối kim loại "
              "toả nhiệt.", True,
              "Khối kim loại (100 °C) nóng hơn nước (25 °C) nên nhiệt tự truyền từ kim "
              "loại sang nước: kim loại toả nhiệt và nguội đi, nước thu nhiệt và nóng lên, "
              "cho tới khi cả hai cùng đạt 30,0 °C."),
             ("Nhiệt lượng nước thu vào trong thí nghiệm là 6,30 kJ.", True,
              "Q_thu = m_nước·c_nước·Δt = 0,300 × 4200 × (30,0 − 25) = 0,300 × 4200 × 5,0 "
              "= 6300 J = 6,30 kJ."),
             ("Nhiệt dung riêng của kim loại xác định được từ thí nghiệm là 450 J/(kg·K).",
              True,
              "Phương trình cân bằng nhiệt: Q_toả = Q_thu ⇒ m_kl·c_kl·(100 − 30,0) = 6300 "
              "⇒ 0,200 × c_kl × 70,0 = 6300 ⇒ c_kl = 6300/14,0 = 450 J/(kg·K)."),
             ("Nếu tính thêm nhiệt lượng mà nhiệt lượng kế thu vào thì giá trị nhiệt dung "
              "riêng tính được của kim loại sẽ nhỏ hơn 450 J/(kg·K).", False,
              "Khi kể thêm nhiệt lượng kế thì vế thu nhiệt tăng lên: Q_toả = Q_nước + "
              "Q_nlk (nlk là nhiệt lượng kế) > 6300 J. Vì m_kl và độ giảm nhiệt độ 70,0 K "
              "không đổi nên "
              "c_kl = Q_toả/(0,200 × 70,0) phải LỚN hơn 450 J/(kg·K). Bỏ qua nhiệt lượng "
              "kế luôn làm giá trị đo được nhỏ hơn giá trị thực."),
         ]),

    dict(stem="Xét các tình huống biến đổi nội năng của một hệ theo định luật I của nhiệt "
              "động lực học ΔU = A + Q.",
         items=[
             ("Một lượng khí nhận nhiệt lượng 500 J mà không trao đổi công với bên ngoài "
              "thì nội năng của khí tăng thêm 500 J.", True,
              "A = 0 nên ΔU = Q = +500 J. Đây chính là quá trình đẳng tích: toàn bộ nhiệt "
              "lượng nhận được chuyển thành độ tăng nội năng."),
             ("Nếu nén một lượng khí trong điều kiện không trao đổi nhiệt với bên ngoài "
              "thì nội năng của khí giảm.", False,
              "Nén khí nghĩa là bên ngoài thực hiện công lên khí, khí NHẬN công nên A > 0. "
              "Không trao đổi nhiệt nghĩa là Q = 0. Vậy ΔU = A > 0: nội năng của khí TĂNG "
              "(khí nóng lên). Đây chính là hiện tượng bơm xe bị nóng lên khi bơm nhanh."),
             ("Một lượng khí dãn nở, nhận nhiệt lượng 300 J và đồng thời thực hiện công "
              "300 J lên môi trường thì nội năng của khí không đổi.", True,
              "Q = +300 J, A = −300 J ⇒ ΔU = −300 + 300 = 0. Nhiệt nhận vào vừa đúng bằng "
              "công mà khí sinh ra nên nội năng giữ nguyên."),
             ("Khi truyền cho một vật một nhiệt lượng Q > 0 thì chắc chắn nhiệt độ của vật "
              "tăng lên.", False,
              "Không chắc chắn. Nếu vật đang chuyển thể (nước đá đang tan, nước đang sôi) "
              "thì nhiệt lượng nhận được dùng cho chuyển thể và nhiệt độ giữ nguyên. Ngoài "
              "ra nếu vật vừa nhận nhiệt vừa dãn nở sinh công đủ lớn thì nội năng, và do "
              "đó nhiệt độ, thậm chí có thể giảm."),
         ]),

    dict(stem="Hình vẽ mô tả cách sắp xếp các phân tử ở ba thể của cùng một chất.",
         fig="t11c",
         items=[
             ("Ở thể rắn, các phân tử sắp xếp trật tự và chỉ dao động quanh những vị trí "
              "cân bằng xác định.", True,
              "Đây là đặc điểm cơ bản của chất rắn kết tinh: các phân tử liên kết chặt "
              "chẽ, có trật tự xa, mỗi phân tử chỉ dao động quanh một nút mạng cố định. "
              "Nhờ đó chất rắn có hình dạng và thể tích riêng xác định."),
             ("Ở thể lỏng, khoảng cách trung bình giữa các phân tử lớn hơn nhiều lần so "
              "với ở thể rắn.", False,
              "Khoảng cách trung bình giữa các phân tử ở thể lỏng chỉ lớn hơn ở thể rắn "
              "một chút (vì vậy khối lượng riêng của chất lỏng và chất rắn của cùng một "
              "chất xấp xỉ nhau). Điểm khác biệt chính là chất lỏng mất trật tự xa nên các "
              "phân tử có thể trượt lên nhau. Chỉ ở thể khí khoảng cách mới lớn gấp hàng "
              "chục lần."),
             ("Ở thể khí, lực tương tác giữa các phân tử rất yếu nên chất khí không có "
              "hình dạng riêng và không có thể tích riêng.", True,
              "Khoảng cách giữa các phân tử khí rất lớn so với kích thước phân tử nên lực "
              "tương tác hầu như không đáng kể (trừ lúc va chạm). Các phân tử chuyển động "
              "tự do và chiếm toàn bộ thể tích bình chứa, vì thế chất khí không có hình "
              "dạng lẫn thể tích riêng."),
             ("Khi chất chuyển từ thể rắn sang thể lỏng rồi sang thể khí, khoảng cách "
              "trung bình giữa các phân tử tăng dần nên thế năng tương tác phân tử giảm "
              "dần.", False,
              "Ngược lại: muốn tách các phân tử ra xa nhau phải thắng lực hút giữa chúng, "
              "tức phải cung cấp năng lượng, nên thế năng tương tác TĂNG dần. Chính vì vậy "
              "nóng chảy và hoá hơi đều là các quá trình thu nhiệt, và với cùng khối "
              "lượng, cùng nhiệt độ thì hơi có nội năng lớn hơn lỏng, lỏng lớn hơn rắn."),
         ]),
]

DE1_P3 = [
    dict(q="Một ấm nhôm khối lượng 0,40 kg chứa 1,5 kg nước, tất cả đang ở 20 °C. Bỏ qua "
           "sự trao đổi nhiệt với môi trường, tính nhiệt lượng tối thiểu (theo kJ) cần "
           "cung cấp để đun sôi ấm nước này. (Kết quả làm tròn đến hàng đơn vị.)",
         ans="532",
         sol="Ấm và nước cùng nóng lên từ 20 °C tới 100 °C, tức Δt = 80 K.\n"
             "Q = (m_nhôm·c_nhôm + m_nước·c_nước)·Δt = (0,40 × 880 + 1,5 × 4200) × 80\n"
             "  = (352 + 6300) × 80 = 6652 × 80 = 532 160 J ≈ 532 kJ."),

    dict(q="Thả một miếng kim loại khối lượng 500 g đã được nung nóng tới 120 °C vào 400 g "
           "nước ở 22 °C đựng trong một bình cách nhiệt. Nhiệt độ khi cân bằng nhiệt là "
           "32 °C. Bỏ qua nhiệt dung của bình. Tính nhiệt dung riêng của kim loại theo đơn "
           "vị J/(kg·K). (Kết quả làm tròn đến hàng đơn vị.)",
         ans="382",
         sol="Nhiệt lượng nước thu vào: Q_thu = 0,400 × 4200 × (32 − 22) = 16 800 J.\n"
             "Nhiệt lượng kim loại toả ra: Q_toả = 0,500 × c × (120 − 32) = 44,0·c.\n"
             "Phương trình cân bằng nhiệt Q_toả = Q_thu cho 44,0·c = 16 800\n"
             "⇒ c = 16 800/44,0 ≈ 381,8 ≈ 382 J/(kg·K). Giá trị này rất gần nhiệt dung "
             "riêng của đồng, 380 J/(kg·K)."),

    dict(q="Người ta thả 300 g nước đá ở 0 °C vào 1,0 kg nước ở 60 °C đựng trong một bình "
           "cách nhiệt. Xác định nhiệt độ của hỗn hợp khi cân bằng nhiệt (theo °C, làm "
           "tròn đến hàng phần mười).",
         ans="27,8",
         sol="Bước 1 – kiểm tra nước đá có tan hết không.\n"
             "Nhiệt lượng lớn nhất mà 1,0 kg nước ở 60 °C có thể toả ra khi hạ tới 0 °C: "
             "Q_max = 1,0 × 4200 × 60 = 252 000 J.\n"
             "Nhiệt lượng cần để làm tan hết 300 g nước đá: Q_λ = 0,300 × 3,34·10⁵ "
             "= 100 200 J.\n"
             "Vì 252 000 J > 100 200 J nên nước đá tan hết và nhiệt độ cuối lớn hơn 0 °C.\n"
             "Bước 2 – lập phương trình cân bằng nhiệt với nhiệt độ cuối t:\n"
             "100 200 + 0,300 × 4200 × t = 1,0 × 4200 × (60 − t)\n"
             "100 200 + 1260t = 252 000 − 4200t ⇒ 5460t = 151 800 ⇒ t ≈ 27,8 °C."),

    dict(q="Một bếp điện có công suất 800 W được dùng để đun 1,5 kg nước từ 25 °C. Hiệu "
           "suất của bếp là 70 %. Tính thời gian cần thiết để đun nước tới 100 °C (theo "
           "phút, làm tròn đến hàng phần mười).",
         ans="14,1",
         sol="Nhiệt lượng có ích cần cung cấp cho nước:\n"
             "Q_ích = mcΔt = 1,5 × 4200 × (100 − 25) = 472 500 J.\n"
             "Vì hiệu suất H = Q_ích/Q_toàn phần = 70 % nên nhiệt lượng bếp phải toả ra:\n"
             "Q_tp = 472 500/0,70 = 675 000 J.\n"
             "Thời gian: τ = Q_tp/P = 675 000/800 = 843,75 s ≈ 14,1 phút."),

    dict(q="Tính nhiệt lượng (theo kJ) cần cung cấp để biến 200 g nước đá ở −10 °C thành "
           "nước ở 20 °C. (Kết quả làm tròn đến hàng phần mười.)",
         ans="87,8",
         sol="Quá trình gồm ba giai đoạn nối tiếp:\n"
             "• Làm nóng nước đá từ −10 °C lên 0 °C: Q₁ = 0,200 × 2100 × 10 = 4200 J.\n"
             "• Làm nóng chảy hoàn toàn nước đá ở 0 °C: Q₂ = 0,200 × 3,34·10⁵ = 66 800 J.\n"
             "• Làm nóng nước từ 0 °C lên 20 °C: Q₃ = 0,200 × 4200 × 20 = 16 800 J.\n"
             "Tổng cộng: Q = 4200 + 66 800 + 16 800 = 87 800 J = 87,8 kJ.\n"
             "Lưu ý: giai đoạn đầu phải dùng nhiệt dung riêng của NƯỚC ĐÁ (2100), giai "
             "đoạn cuối mới dùng nhiệt dung riêng của nước (4200)."),

    dict(q="Một lượng khí trải qua hai giai đoạn liên tiếp. Giai đoạn một: khí nhận nhiệt "
           "lượng 750 J, dãn nở và thực hiện công 480 J lên pit-tông. Giai đoạn hai: khí "
           "bị nén, nhận công 260 J từ bên ngoài và toả ra môi trường nhiệt lượng 190 J. "
           "Tính độ biến thiên nội năng tổng cộng của lượng khí sau hai giai đoạn (theo J).",
         ans="340",
         sol="Áp dụng ΔU = A + Q cho từng giai đoạn, với quy ước A và Q là phần hệ NHẬN "
             "được.\n"
             "Giai đoạn 1: Q₁ = +750 J (nhận nhiệt), A₁ = −480 J (thực hiện công lên bên "
             "ngoài) ⇒ ΔU₁ = −480 + 750 = +270 J.\n"
             "Giai đoạn 2: Q₂ = −190 J (toả nhiệt), A₂ = +260 J (nhận công) "
             "⇒ ΔU₂ = 260 − 190 = +70 J.\n"
             "Nội năng là hàm trạng thái nên độ biến thiên tổng cộng bằng tổng các độ biến "
             "thiên: ΔU = 270 + 70 = 340 J."),
]

DE1 = dict(code="C1-01", so="01", chuong=1,
           title="ĐỀ KIỂM TRA CHƯƠNG I – ĐỀ SỐ 01",
           subtitle="Chương I – Vật lí nhiệt",
           p1=DE1_P1, p2=DE1_P2, p3=DE1_P3)


# ===================================================================================
#                    ĐỀ SỐ 02 – CƠ BẢN VÀ VẬN DỤNG
# ===================================================================================

DE2_P1 = [
    dict(q="Đơn vị đo nhiệt nóng chảy riêng của một chất trong hệ SI là",
         o=["J/kg.", "J/(kg·K).", "J/K.", "J."],
         a="A",
         sol="Từ Q = λm suy ra λ = Q/m, đơn vị J/kg. Đơn vị J/(kg·K) là của nhiệt dung "
             "riêng, còn J/K là của nhiệt dung của một vật."),

    dict(q="Nhiệt độ của một vật là đại lượng đặc trưng cho",
         o=["mức độ chuyển động nhiệt của các phân tử cấu tạo nên vật.",
            "tổng nội năng chứa trong toàn bộ khối lượng của vật.",
            "khả năng dẫn nhiệt của chất cấu tạo nên vật đó.",
            "tổng số phân tử chứa trong một đơn vị thể tích của vật."],
         a="A",
         sol="Nhiệt độ là số đo mức độ chuyển động nhiệt (động năng chuyển động nhiệt "
             "trung bình) của các phân tử. Nội năng phụ thuộc cả vào khối lượng nên hai "
             "vật cùng nhiệt độ vẫn có thể có nội năng rất khác nhau."),

    dict(q="Trong thang Kelvin, nhiệt độ của nước đá đang tan ở áp suất chuẩn là",
         o=["273,15 K.", "0 K.", "100 K.", "373,15 K."],
         a="A",
         sol="Nước đá tan ở 0 °C, đổi sang thang Kelvin: T = 0 + 273,15 = 273,15 K. "
             "373,15 K là nhiệt độ nước sôi (100 °C)."),

    dict(q="Quá trình chuyển từ thể lỏng sang thể rắn của một chất được gọi là sự",
         o=["đông đặc.", "nóng chảy.", "ngưng tụ.", "hoá hơi."],
         a="A",
         sol="Lỏng → rắn là sự đông đặc (toả nhiệt); rắn → lỏng là sự nóng chảy (thu "
             "nhiệt); hơi → lỏng là sự ngưng tụ; lỏng → hơi là sự hoá hơi."),

    dict(q="Trong công thức tính nhiệt lượng Q = mcΔt, đại lượng c được gọi là",
         o=["nhiệt dung riêng của chất cấu tạo nên vật.",
            "nhiệt nóng chảy riêng của chất cấu tạo nên vật.",
            "nhiệt hoá hơi riêng của chất cấu tạo nên vật.",
            "nhiệt dung của toàn bộ vật đang xét."],
         a="A",
         sol="c là nhiệt dung riêng, đơn vị J/(kg·K), cho biết nhiệt lượng cần cung cấp để "
             "1 kg chất đó tăng thêm 1 K. Tích m·c mới là nhiệt dung của vật, đơn vị J/K."),

    dict(q="Nhiệt lượng là",
         o=["phần nội năng vật nhận thêm hay mất bớt đi trong quá trình truyền nhiệt.",
            "phần nội năng vật nhận thêm hay mất bớt đi khi có công được thực hiện.",
            "tổng nội năng mà vật đang chứa ở một nhiệt độ xác định nào đó.",
            "đại lượng đo mức độ chuyển động nhiệt của các phân tử trong vật."],
         a="A",
         sol="Định nghĩa: nhiệt lượng là số đo độ biến thiên nội năng của vật trong quá "
             "trình TRUYỀN NHIỆT. Nếu nội năng biến đổi do thực hiện công thì đại lượng đo "
             "là công chứ không phải nhiệt lượng. Cũng không được nói “vật chứa một nhiệt "
             "lượng”: vật chứa nội năng, còn nhiệt lượng chỉ xuất hiện khi có sự truyền."),

    dict(q="Nói nhiệt dung riêng của đồng là 380 J/(kg·K) có nghĩa là",
         o=["cần cung cấp 380 J để 1 kg đồng tăng thêm 1 K nhiệt độ.",
            "cần cung cấp 380 J để làm nóng chảy hoàn toàn 1 kg đồng.",
            "cần cung cấp 380 J để 1 g đồng tăng thêm 1 K nhiệt độ.",
            "trong mỗi kilôgam đồng luôn chứa một nội năng bằng 380 J."],
         a="A",
         sol="Theo định nghĩa c = Q/(mΔT), giá trị 380 J/(kg·K) nghĩa là muốn 1 kg đồng "
             "nóng thêm 1 K (cũng là 1 °C) phải cung cấp 380 J. Đơn vị đã ghi rõ “kg” chứ "
             "không phải “g”. Nhiệt lượng làm nóng chảy 1 kg đồng là nhiệt nóng chảy riêng "
             "chứ không phải nhiệt dung riêng."),

    dict(q="Khi hai vật tiếp xúc nhiệt với nhau và đã đạt trạng thái cân bằng nhiệt thì "
           "hai vật đó",
         o=["có cùng nhiệt độ.", "có cùng nội năng.",
            "có cùng nhiệt dung riêng.", "đã trao đổi hết nội năng cho nhau."],
         a="A",
         sol="Cân bằng nhiệt được đặc trưng bởi sự bằng nhau về NHIỆT ĐỘ; khi đó không còn "
             "sự truyền nhiệt có hướng giữa hai vật. Nội năng của hai vật nói chung vẫn "
             "khác nhau vì còn phụ thuộc khối lượng và bản chất của chúng."),

    dict(q="Khi đun nước bằng ấm điện, nếu tiếp tục đun sau khi nước đã sôi thì",
         o=["nhiệt độ của nước không tăng thêm, nhiệt lượng cung cấp dùng để hoá hơi nước.",
            "nhiệt độ của nước tiếp tục tăng đều cho tới khi nước cạn hết trong ấm.",
            "nhiệt độ của nước giảm dần vì nước bay hơi mạnh và mang nhiệt đi.",
            "nội năng của lượng nước trong ấm không thay đổi nữa vì nhiệt độ không đổi."],
         a="A",
         sol="Trong suốt quá trình sôi, nhiệt độ chất lỏng giữ nguyên ở nhiệt độ sôi. Toàn "
             "bộ nhiệt lượng tiếp tục cung cấp dùng để thắng lực liên kết giữa các phân "
             "tử, biến nước thành hơi. Nội năng của hệ vẫn tăng vì thế năng tương tác phân "
             "tử tăng, dù nhiệt độ không đổi."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo thời gian khi làm nguội một lượng naphtalene "
           "đang ở thể lỏng. Trong khoảng thời gian từ phút thứ 4 đến phút thứ 14, "
           "naphtalene",
         fig="t12b",
         o=["đang đông đặc, tồn tại đồng thời cả thể lỏng và thể rắn.",
            "hoàn toàn ở thể lỏng và đang nguội đi rất chậm.",
            "hoàn toàn ở thể rắn và có nhiệt độ giữ nguyên 80 °C.",
            "đang nóng chảy nên nhiệt độ của nó không thay đổi."],
         a="A",
         sol="Đoạn nằm ngang ở 80 °C trong quá trình LÀM NGUỘI ứng với sự đông đặc: chất "
             "toả nhiệt ra môi trường nhưng nhiệt độ giữ nguyên vì nhiệt lượng toả ra lấy "
             "từ phần thế năng tương tác giảm khi các phân tử liên kết lại thành mạng tinh "
             "thể. Trong suốt đoạn này chất tồn tại đồng thời ở hai thể. Đây là quá trình "
             "làm nguội nên không thể là nóng chảy."),

    dict(q="Khi bước ra khỏi hồ bơi, dù trời không có gió ta vẫn cảm thấy lạnh. Nguyên "
           "nhân chính là",
         o=["nước trên da bay hơi và thu nhiệt lượng từ cơ thể.",
            "nhiệt độ của nước trong hồ luôn thấp hơn nhiệt độ cơ thể.",
            "không khí dẫn nhiệt tốt hơn nước nên lấy nhiệt của da nhanh hơn.",
            "áp suất khí quyển tác dụng lên da làm nội năng của da giảm đi."],
         a="A",
         sol="Sự bay hơi là quá trình THU NHIỆT. Lớp nước mỏng trên da bay hơi lấy nhiệt "
             "hoá hơi từ chính cơ thể, làm da lạnh đi. Đây cũng là nguyên lí làm mát bằng "
             "bay hơi. Thực tế không khí dẫn nhiệt kém hơn nước rất nhiều."),

    dict(q="Hai vật A và B làm bằng cùng một chất, đang ở cùng một nhiệt độ. Khối lượng "
           "của A gấp đôi khối lượng của B. So sánh nội năng của hai vật, ta có",
         o=["nội năng của A gấp đôi nội năng của B.",
            "nội năng của A bằng nội năng của B vì cùng nhiệt độ.",
            "nội năng của A bằng một nửa nội năng của B.",
            "không thể so sánh vì còn phụ thuộc vào hình dạng của hai vật."],
         a="A",
         sol="Nội năng là tổng động năng và thế năng tương tác của TẤT CẢ các phân tử nên "
             "tỉ lệ với số phân tử, tức tỉ lệ với khối lượng khi cùng chất và cùng nhiệt "
             "độ. Vậy U_A = 2U_B. Cùng nhiệt độ chỉ có nghĩa là động năng trung bình của "
             "MỖI phân tử như nhau, không có nghĩa là tổng nội năng bằng nhau."),

    dict(q="Hình vẽ là đồ thị nhiệt lượng cung cấp theo độ tăng nhiệt độ của hai chất lỏng "
           "X và Y có cùng khối lượng 1,0 kg. Tỉ số giữa nhiệt dung riêng của X và của Y là",
         fig="t12a",
         o=["2,5.", "0,4.", "1,5.", "5,0."],
         a="A",
         sol="Với cùng khối lượng và cùng độ tăng nhiệt độ Δt = 40 °C, đồ thị cho "
             "Q_X = 84 kJ và Q_Y = 33,6 kJ. Vì Q = mcΔt nên với cùng m và cùng Δt thì Q tỉ "
             "lệ thuận với c: c_X/c_Y = Q_X/Q_Y = 84/33,6 = 2,5. (Cũng có thể tính riêng: "
             "c_X = 84 000/(1,0 × 40) = 2100 và c_Y = 33 600/(1,0 × 40) = 840 J/(kg·K).)"),

    dict(q="Nhiệt lượng toả ra khi 0,80 kg hơi nước ở 100 °C ngưng tụ hoàn toàn thành nước "
           "ở 100 °C là",
         o=["1,808·10⁶ J.", "9,040·10⁵ J.", "2,260·10⁶ J.", "3,360·10⁵ J."],
         a="A",
         sol="Ngưng tụ là quá trình ngược của hoá hơi nên nhiệt lượng toả ra cũng tính "
             "bằng Q = Lm = 2,26·10⁶ × 0,80 = 1,808·10⁶ J. Vì nhiệt độ không đổi (đều ở "
             "100 °C) nên không có thành phần mcΔt."),

    dict(q="Trộn 2,0 kg nước ở 90 °C với 3,0 kg nước ở 20 °C trong một bình cách nhiệt. Bỏ "
           "qua nhiệt dung của bình, nhiệt độ của hỗn hợp khi cân bằng nhiệt là",
         o=["48 °C.", "42 °C.", "55 °C.", "60 °C."],
         a="A",
         sol="Vì cùng chất nên có thể dùng công thức trung bình có trọng số theo khối "
             "lượng: t = (m₁t₁ + m₂t₂)/(m₁ + m₂) = (2,0 × 90 + 3,0 × 20)/5,0 = "
             "(180 + 60)/5,0 = 48 °C. Nhiệt độ cân bằng lệch về phía khối nước có khối "
             "lượng lớn hơn."),

    dict(q="Một thanh sắt khối lượng 2,0 kg toả ra nhiệt lượng 92 kJ khi nguội đi. Độ giảm "
           "nhiệt độ của thanh sắt là",
         o=["100 °C.", "50 °C.", "200 °C.", "46 °C."],
         a="A",
         sol="Từ Q = mcΔt suy ra Δt = Q/(mc) = 92 000/(2,0 × 460) = 92 000/920 = 100 °C. "
             "(Cũng là 100 K, vì một độ chênh lệch nhiệt độ có cùng trị số trong hai "
             "thang.)"),

    dict(q="Nhiệt lượng cần cung cấp để làm 250 g nước đá ở 0 °C tan hết rồi tiếp tục nóng "
           "lên tới 20 °C là",
         o=["104,5 kJ.", "83,5 kJ.", "21,0 kJ.", "125,5 kJ."],
         a="A",
         sol="Quá trình gồm hai giai đoạn:\n"
             "• Nóng chảy ở 0 °C: Q₁ = λm = 3,34·10⁵ × 0,250 = 83 500 J.\n"
             "• Nước nóng từ 0 °C lên 20 °C: Q₂ = 0,250 × 4200 × 20 = 21 000 J.\n"
             "Tổng: Q = 83 500 + 21 000 = 104 500 J = 104,5 kJ."),

    dict(q="Trong thí nghiệm đo nhiệt dung riêng của nước bằng oát kế, nhiệt kế và dây đốt "
           "nhúng trong cốc nước, nguyên nhân chính gây sai số là",
         o=["một phần nhiệt lượng truyền ra môi trường và truyền cho cốc, nhiệt kế.",
            "nước trong cốc luôn có nhiệt độ đồng đều nên nhiệt kế đo rất chính xác.",
            "dây đốt biến toàn bộ điện năng tiêu thụ thành nhiệt lượng cấp cho nước.",
            "khối lượng nước trong cốc được cân bằng cân điện tử có sai số rất nhỏ."],
         a="A",
         sol="Trong tính toán ta thường coi toàn bộ nhiệt lượng do dây đốt cung cấp đều "
             "truyền cho nước. Thực tế một phần truyền cho cốc, nhiệt kế, dây đốt và toả "
             "ra không khí, làm giá trị c đo được lớn hơn giá trị thực. Cách khắc phục: "
             "dùng bình cách nhiệt, đun trong thời gian ngắn, khuấy đều và hiệu chỉnh theo "
             "nhiệt dung của bình."),
]

DE2_P2 = [
    dict(stem="Hình vẽ là đồ thị nhiệt độ theo thời gian khi làm nguội một lượng "
              "naphtalene ở thể lỏng trong không khí.",
         fig="t12b",
         items=[
             ("Nhiệt độ đông đặc của naphtalene là 80 °C.", True,
              "Đoạn nằm ngang của đồ thị làm nguội ứng với quá trình đông đặc, và nó nằm ở "
              "mức 80 °C. Vậy nhiệt độ đông đặc (cũng là nhiệt độ nóng chảy) của "
              "naphtalene bằng 80 °C."),
             ("Trong 4 phút đầu tiên, naphtalene ở thể rắn và đang nguội dần.", False,
              "Trong 4 phút đầu, nhiệt độ giảm từ 95 °C xuống 80 °C, tức vẫn cao hơn nhiệt "
              "độ đông đặc. Ở giai đoạn này naphtalene còn hoàn toàn ở thể LỎNG và đang "
              "nguội dần; nó chỉ bắt đầu đông đặc khi nhiệt độ chạm 80 °C."),
             ("Trong quá trình đông đặc, naphtalene vẫn toả nhiệt ra môi trường nhưng "
              "nhiệt độ của nó không đổi.", True,
              "Naphtalene luôn nóng hơn môi trường nên vẫn liên tục toả nhiệt. Nhiệt lượng "
              "toả ra này lấy từ phần thế năng tương tác phân tử giảm đi khi các phân tử "
              "sắp xếp lại thành mạng tinh thể, chứ không lấy từ động năng chuyển động "
              "nhiệt, nên nhiệt độ giữ nguyên 80 °C."),
             ("Sau phút thứ 14, naphtalene ở thể lỏng và tiếp tục nguội đi.", False,
              "Phút thứ 14 là lúc kết thúc đoạn nằm ngang, tức naphtalene vừa đông đặc "
              "hoàn toàn. Sau đó nhiệt độ lại giảm, ứng với khối naphtalene RẮN đang nguội "
              "dần từ 80 °C xuống."),
         ]),

    dict(stem="Hình vẽ là sơ đồ bộ thí nghiệm đo nhiệt nóng chảy riêng của nước đá. Một "
              "điện trở đun có công suất 40 W được đặt trong khối nước đá đang tan ở 0 °C. "
              "Sau 8,0 phút, cân điện tử cho biết khối lượng nước chảy xuống cốc hứng tăng "
              "thêm 56 g. Bỏ qua mọi hao phí nhiệt.",
         fig="t12c",
         items=[
             ("Trong suốt thí nghiệm, nhiệt độ của khối nước đá không đổi và bằng 0 °C.",
              True,
              "Khối nước đá đang tan luôn giữ nhiệt độ 0 °C cho tới khi tan hết. Nhờ vậy "
              "toàn bộ nhiệt lượng của điện trở chỉ dùng cho sự nóng chảy, không mất một "
              "phần vào việc làm tăng nhiệt độ — đó chính là lí do phải bắt đầu thí nghiệm "
              "với nước đá đang tan."),
             ("Nhiệt lượng mà điện trở cung cấp trong 8,0 phút là 320 J.", False,
              "Phải đổi thời gian ra giây: 8,0 phút = 480 s. Nhiệt lượng cung cấp là "
              "Q = P·τ = 40 × 480 = 19 200 J = 19,2 kJ. Giá trị 320 J là kết quả sai do "
              "lấy 40 × 8 mà quên đổi đơn vị thời gian."),
             ("Nhiệt nóng chảy riêng của nước đá xác định được từ thí nghiệm này xấp xỉ "
              "3,43·10⁵ J/kg.", True,
              "λ = Q/m = 19 200/0,056 ≈ 3,43·10⁵ J/kg. Kết quả này lớn hơn giá trị quy "
              "chiếu 3,34·10⁵ J/kg khoảng 2,7 %, sai lệch hợp lí với một thí nghiệm học "
              "sinh."),
             ("Nếu có thêm một phần nước đá bị tan do nhiệt của môi trường truyền vào thì "
              "giá trị λ đo được sẽ lớn hơn giá trị thực.", False,
              "Nhiệt của môi trường làm tan thêm nước đá, khiến khối lượng m cân được LỚN "
              "hơn khối lượng đáng lẽ chỉ do điện trở làm tan. Trong khi đó Q = P·τ vẫn "
              "giữ nguyên, nên λ = Q/m tính được sẽ NHỎ hơn giá trị thực. Vì vậy phải bọc "
              "cách nhiệt cho phễu và làm thí nghiệm nhanh."),
         ]),

    dict(stem="Xét các phát biểu về nhiệt độ và thang nhiệt độ.",
         items=[
             ("Nhiệt độ 37 °C tương ứng với 310,15 K.", True,
              "Công thức chuyển thang: T = t + 273,15 = 37 + 273,15 = 310,15 K. Phải "
              "CỘNG chứ không nhân, và cộng đúng hằng số 273,15 (nhiều bài toán cho "
              "phép làm tròn thành 273). Đây cũng là thân nhiệt bình thường của "
              "người."),
             ("Một độ chia của thang Kelvin có độ lớn bằng một độ chia của thang Celsius, "
              "do đó một độ chênh lệch nhiệt độ có cùng trị số trong hai thang.", True,
              "Hai thang chỉ khác nhau ở gốc (0 K ứng với −273,15 °C) chứ không khác nhau "
              "ở độ lớn mỗi độ chia. Khi lấy hiệu hai nhiệt độ, hằng số 273,15 triệt tiêu "
              "nên ΔT(K) = Δt(°C). Đây là lí do trong công thức Q = mcΔT ta có thể thay "
              "trực tiếp độ chênh lệch tính bằng °C."),
             ("Nói một vật có nhiệt độ 0 °C nghĩa là vật đó không còn nội năng.", False,
              "0 °C tương ứng 273,15 K, hoàn toàn không phải nhiệt độ không tuyệt đối. Ở "
              "0 °C các phân tử vẫn chuyển động nhiệt mạnh và vật vẫn có nội năng rất lớn. "
              "Chỉ ở 0 K (−273,15 °C) chuyển động nhiệt mới về mức thấp nhất, mà nhiệt độ "
              "này không thể đạt tới được."),
             ("Khi hai vật có cùng nhiệt độ được đặt tiếp xúc nhau thì vật có khối lượng "
              "lớn hơn sẽ truyền nhiệt cho vật kia.", False,
              "Chiều truyền nhiệt được quyết định bởi NHIỆT ĐỘ chứ không phải khối lượng "
              "hay nội năng. Hai vật cùng nhiệt độ đã ở trạng thái cân bằng nhiệt nên "
              "không có sự truyền nhiệt có hướng giữa chúng, dù nội năng của chúng rất "
              "khác nhau."),
         ]),

    dict(stem="Một học sinh thả 100 g nước đá ở 0 °C vào 500 g nước ở 30 °C đựng trong "
              "bình cách nhiệt. Bỏ qua nhiệt dung của bình.",
         items=[
             ("Nhiệt lượng cần cung cấp để làm tan hết 100 g nước đá là 33,4 kJ.", True,
              "Q = λm = 3,34·10⁵ × 0,100 = 33 400 J = 33,4 kJ. Nước đá đã ở đúng 0 °C nên "
              "không cần giai đoạn làm nóng nước đá."),
             ("Nhiệt lượng lớn nhất mà 500 g nước ở 30 °C có thể toả ra khi hạ xuống 0 °C "
              "là 63,0 kJ.", True,
              "Q_max = mcΔt = 0,500 × 4200 × 30 = 63 000 J = 63,0 kJ. So sánh hai con số "
              "này là bước bắt buộc để biết nước đá có tan hết hay không."),
             ("Nước đá không tan hết và hỗn hợp có nhiệt độ cuối cùng bằng 0 °C.", False,
              "Vì 63,0 kJ > 33,4 kJ nên nhiệt lượng nước toả ra thừa sức làm tan hết nước "
              "đá; phần dư 29,6 kJ tiếp tục làm nóng hỗn hợp lên trên 0 °C. Giải phương "
              "trình cân bằng nhiệt: 33 400 + 0,100 × 4200 × t = 0,500 × 4200 × (30 − t) "
              "⇒ 2520t = 29 600 ⇒ t ≈ 11,7 °C."),
             ("Nếu thay 100 g nước đá bằng 100 g nước ở 0 °C thì nhiệt độ cân bằng của hỗn "
              "hợp sẽ thấp hơn.", False,
              "Ngược lại, nhiệt độ cân bằng sẽ CAO hơn. Nước ở 0 °C chỉ thu nhiệt để nóng "
              "lên, không cần nhiệt nóng chảy: t = (0,500 × 30 + 0,100 × 0)/0,600 = 25 °C, "
              "lớn hơn hẳn 11,7 °C. Chính nhiệt nóng chảy 33,4 kJ mới là nguyên nhân khiến "
              "nước đá làm lạnh hiệu quả hơn nước cùng nhiệt độ."),
         ]),
]

DE2_P3 = [
    dict(q="Tính nhiệt lượng (theo kJ) cần cung cấp để làm 3,0 kg nước nóng lên từ 28 °C "
           "đến 88 °C. (Kết quả làm tròn đến hàng đơn vị.)",
         ans="756",
         sol="Q = mcΔt = 3,0 × 4200 × (88 − 28) = 3,0 × 4200 × 60 = 756 000 J = 756 kJ."),

    dict(q="Thả một khối đồng khối lượng 800 g đang ở 150 °C vào 1,2 kg nước ở 25 °C đựng "
           "trong bình cách nhiệt. Bỏ qua nhiệt dung của bình. Tính nhiệt độ khi cân bằng "
           "nhiệt (theo °C, làm tròn đến hàng phần mười).",
         ans="32,1",
         sol="Gọi t là nhiệt độ cân bằng. Phương trình cân bằng nhiệt:\n"
             "m_đồng·c_đồng·(150 − t) = m_nước·c_nước·(t − 25)\n"
             "0,800 × 380 × (150 − t) = 1,2 × 4200 × (t − 25)\n"
             "304(150 − t) = 5040(t − 25) ⇒ 45 600 − 304t = 5040t − 126 000\n"
             "⇒ 5344t = 171 600 ⇒ t ≈ 32,1 °C.\n"
             "Nhận xét: dù khối đồng rất nóng, nhiệt độ nước chỉ tăng khoảng 7 °C vì nhiệt "
             "dung riêng của đồng nhỏ hơn của nước hơn 11 lần."),

    dict(q="Một ấm điện có công suất 1200 W đun 1,8 kg nước từ 20 °C đến sôi ở 100 °C "
           "trong 9,0 phút. Tính hiệu suất của ấm (theo %, làm tròn đến hàng đơn vị).",
         ans="93",
         sol="Nhiệt lượng có ích: Q_ích = 1,8 × 4200 × 80 = 604 800 J.\n"
             "Điện năng ấm tiêu thụ: Q_tp = P·τ = 1200 × (9,0 × 60) = 1200 × 540 "
             "= 648 000 J.\n"
             "Hiệu suất: H = Q_ích/Q_tp = 604 800/648 000 = 0,9333 ≈ 93 %."),

    dict(q="Cần bao nhiêu gam nước đá ở 0 °C để hạ nhiệt độ của 500 g nước từ 35 °C xuống "
           "còn 5 °C trong một bình cách nhiệt? Biết nước đá tan hết. (Kết quả làm tròn "
           "đến hàng đơn vị.)",
         ans="177",
         sol="Nhiệt lượng nước toả ra: Q_toả = 0,500 × 4200 × (35 − 5) = 63 000 J.\n"
             "Nước đá phải trải qua hai giai đoạn: nóng chảy ở 0 °C rồi nóng lên tới 5 °C:\n"
             "Q_thu = m·3,34·10⁵ + m × 4200 × 5 = m(334 000 + 21 000) = 355 000·m.\n"
             "Cho Q_thu = Q_toả: 355 000·m = 63 000 ⇒ m ≈ 0,1775 kg ≈ 177 g.\n"
             "Lưu ý: nếu quên phần nhiệt để hâm nóng nước vừa tan từ 0 °C lên 5 °C sẽ ra "
             "kết quả 189 g, lớn hơn thực tế."),

    dict(q="Một lượng khí dãn nở và thực hiện công 350 J lên môi trường bên ngoài; trong "
           "quá trình đó nội năng của khí giảm 120 J. Tính nhiệt lượng mà khí nhận được "
           "(theo J).",
         ans="230",
         sol="Áp dụng ΔU = A + Q với quy ước A, Q là phần khí NHẬN.\n"
             "Khí thực hiện công lên bên ngoài nên A = −350 J; nội năng giảm nên "
             "ΔU = −120 J.\n"
             "Q = ΔU − A = −120 − (−350) = +230 J. Dấu dương cho biết khí thực sự nhận "
             "nhiệt: khí vừa nhận 230 J nhiệt vừa “tiêu” thêm 120 J nội năng của mình để "
             "sinh ra công 350 J."),

    dict(q="Tính nhiệt lượng (theo kJ) toả ra khi 400 g hơi nước ở 100 °C ngưng tụ hoàn "
           "toàn rồi nguội xuống 40 °C. (Kết quả làm tròn đến hàng đơn vị.)",
         ans="1005",
         sol="Quá trình gồm hai giai đoạn:\n"
             "• Ngưng tụ ở 100 °C: Q₁ = Lm = 2,26·10⁶ × 0,400 = 904 000 J.\n"
             "• Nước nguội từ 100 °C xuống 40 °C: Q₂ = 0,400 × 4200 × 60 = 100 800 J.\n"
             "Tổng: Q = 904 000 + 100 800 = 1 004 800 J ≈ 1005 kJ.\n"
             "Có thể thấy phần nhiệt ngưng tụ chiếm gần 90 % tổng nhiệt lượng — đó là lí "
             "do bỏng hơi nước nguy hiểm hơn hẳn bỏng nước sôi."),
]

DE2 = dict(code="C1-02", so="02", chuong=1,
           title="ĐỀ KIỂM TRA CHƯƠNG I – ĐỀ SỐ 02",
           subtitle="Chương I – Vật lí nhiệt",
           p1=DE2_P1, p2=DE2_P2, p3=DE2_P3)


# ===================================================================================
#              ĐỀ SỐ 03 – ĐỌC ĐỒ THỊ VÀ SUY LUẬN THỰC NGHIỆM
# ===================================================================================

DE3_P1 = [
    dict(q="Nội năng của một vật phụ thuộc vào",
         o=["nhiệt độ và thể tích của vật.",
            "chỉ riêng nhiệt độ của vật.",
            "chỉ riêng khối lượng của vật.",
            "vận tốc chuyển động của vật so với mặt đất."],
         a="A",
         sol="Nội năng gồm động năng chuyển động nhiệt (phụ thuộc nhiệt độ) và thế năng "
             "tương tác phân tử (phụ thuộc khoảng cách giữa các phân tử, tức phụ thuộc thể "
             "tích). Vận tốc chuyển động của cả vật liên quan tới động năng của vật, không "
             "thuộc nội năng."),

    dict(q="Trong một quá trình đẳng tích (thể tích của hệ không đổi), định luật I của "
           "nhiệt động lực học được viết thành",
         o=["ΔU = Q.", "ΔU = A.", "ΔU = 0.", "Q = −A."],
         a="A",
         sol="Thể tích không đổi nên hệ không trao đổi công với bên ngoài, A = 0, do đó "
             "ΔU = Q: toàn bộ nhiệt lượng nhận được chuyển thành độ tăng nội năng. Dạng "
             "ΔU = A ứng với quá trình đoạn nhiệt (Q = 0), còn Q = −A ứng với quá trình "
             "đẳng nhiệt của khí lí tưởng (ΔU = 0)."),

    dict(q="Trong hệ SI, đơn vị của nhiệt hoá hơi riêng là",
         o=["J/kg.", "J/(kg·K).", "W/kg.", "J·kg."],
         a="A",
         sol="Từ Q = Lm suy ra L = Q/m, đơn vị J/kg — giống đơn vị của nhiệt nóng chảy "
             "riêng. W/kg là đơn vị của công suất trên một đơn vị khối lượng, không liên "
             "quan."),

    dict(q="Trong biểu thức ΔU = A + Q, khi hệ thực hiện công lên môi trường bên ngoài thì",
         o=["A mang giá trị âm.", "A mang giá trị dương.",
            "Q mang giá trị âm.", "ΔU luôn mang giá trị âm."],
         a="A",
         sol="A trong biểu thức là công mà hệ NHẬN được. Khi hệ thực hiện công lên bên "
             "ngoài (khí dãn nở đẩy pit-tông) thì hệ mất năng lượng dưới dạng công, nên "
             "A < 0. Giá trị Q phụ thuộc vào việc hệ có trao đổi nhiệt hay không, còn ΔU "
             "phụ thuộc vào tổng A + Q nên chưa thể kết luận dấu."),

    dict(q="Khi nung nóng một chất rắn vô định hình như thuỷ tinh hoặc nhựa đường thì chất "
           "đó",
         o=["mềm dần rồi chuyển sang thể lỏng, không có nhiệt độ nóng chảy xác định.",
            "nóng chảy ở một nhiệt độ hoàn toàn xác định giống chất rắn kết tinh.",
            "giữ nguyên thể rắn cho tới khi bị phân huỷ ở nhiệt độ rất cao.",
            "chuyển thẳng từ thể rắn sang thể khí mà không qua thể lỏng."],
         a="A",
         sol="Chất rắn vô định hình không có cấu trúc mạng tinh thể trật tự xa nên không "
             "có nhiệt độ nóng chảy xác định: khi nung, nó mềm dần rồi hoá lỏng trong một "
             "khoảng nhiệt độ. Đồ thị nhiệt độ theo thời gian của chúng không có đoạn nằm "
             "ngang, khác hẳn chất rắn kết tinh."),

    dict(q="Nhiệt kế hoạt động dựa trên nguyên tắc",
         o=["một tính chất vật lí của vật thay đổi theo nhiệt độ một cách xác định.",
            "vật có nhiệt độ càng cao thì càng chứa nhiều nhiệt lượng bên trong.",
            "nhiệt luôn tự truyền từ vật nóng hơn sang vật lạnh hơn khi tiếp xúc.",
            "mọi chất đều nở ra khi nóng lên và co lại khi lạnh đi như nhau."],
         a="A",
         sol="Nguyên tắc chung của nhiệt kế là dựa vào sự phụ thuộc đơn trị của một tính "
             "chất vật lí (thể tích chất lỏng, điện trở, suất điện động nhiệt điện, bức xạ "
             "hồng ngoại…) vào nhiệt độ, kèm theo việc để nhiệt kế cân bằng nhiệt với vật "
             "cần đo. Các chất khác nhau nở vì nhiệt khác nhau, nên ý cuối sai."),

    dict(q="Vào mùa đông, khi sờ tay vào một thanh kim loại và một miếng gỗ đặt cạnh nhau "
           "trong cùng một phòng, ta thấy thanh kim loại lạnh hơn. Nguyên nhân là",
         o=["kim loại dẫn nhiệt tốt hơn nên lấy nhiệt từ tay nhanh hơn gỗ.",
            "nhiệt độ của thanh kim loại thấp hơn nhiệt độ của miếng gỗ.",
            "nhiệt dung riêng của kim loại lớn hơn nhiệt dung riêng của gỗ.",
            "nội năng chứa trong thanh kim loại nhỏ hơn trong miếng gỗ."],
         a="A",
         sol="Cùng đặt trong một phòng lâu ngày thì hai vật đã cân bằng nhiệt, tức có CÙNG "
             "nhiệt độ. Cảm giác lạnh phụ thuộc tốc độ mất nhiệt của da: kim loại dẫn "
             "nhiệt tốt hơn gỗ hàng trăm lần nên rút nhiệt từ tay nhanh hơn, khiến ta thấy "
             "lạnh hơn. Đây là một ví dụ điển hình cho thấy cảm giác nóng lạnh không phải "
             "là phép đo nhiệt độ đáng tin cậy."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo nhiệt lượng đã cung cấp cho 0,50 kg một chất "
           "rắn. Đoạn NP của đồ thị ứng với quá trình",
         fig="t13a",
         o=["nóng chảy của chất.", "chất rắn nóng dần lên.",
            "chất lỏng nóng dần lên.", "hoá hơi của chất."],
         a="A",
         sol="Đoạn NP nằm ngang ở 0 °C: chất tiếp tục nhận nhiệt (Q tăng từ 32,5 kJ lên "
             "137,5 kJ) nhưng nhiệt độ không đổi. Đó là dấu hiệu của quá trình chuyển thể. "
             "Vì trước đó chất ở thể rắn (đoạn MN đi lên từ −50 °C) và sau đó là thể lỏng "
             "(đoạn PQ), nên NP là quá trình nóng chảy."),

    dict(q="Hình vẽ mô tả hai cách làm tăng nội năng của một khối kim loại. Nhận xét nào "
           "sau đây là đúng?",
         fig="t13b",
         o=["Ở (a) nội năng tăng do thực hiện công, ở (b) nội năng tăng do truyền nhiệt.",
            "Cả hai trường hợp nội năng đều tăng do quá trình truyền nhiệt cho vật.",
            "Ở (a) nhiệt độ của khối kim loại không đổi, ở (b) nhiệt độ của nó tăng lên.",
            "Chỉ có cách (b) mới thực sự làm tăng được nội năng của khối kim loại."],
         a="A",
         sol="Có đúng hai cách làm biến đổi nội năng. Hình (a): lực ma sát khi cọ xát thực "
             "hiện công lên khối kim loại, A > 0. Hình (b): nguồn nhiệt truyền nhiệt lượng "
             "cho khối kim loại, Q > 0. Cả hai đều làm nội năng tăng, và trong cả hai "
             "trường hợp nhiệt độ khối kim loại đều tăng lên."),

    dict(q="Đun hai chất lỏng khác nhau có cùng khối lượng bằng hai bếp giống hệt nhau. "
           "Chất lỏng nào có nhiệt dung riêng lớn hơn thì",
         o=["nóng lên chậm hơn chất lỏng kia.",
            "nóng lên nhanh hơn chất lỏng kia.",
            "có nhiệt độ ban đầu thấp hơn chất lỏng kia.",
            "cần ít nhiệt lượng hơn để tăng cùng số độ."],
         a="A",
         sol="Từ Δt = Q/(mc): với cùng nhiệt lượng cung cấp trong mỗi đơn vị thời gian và "
             "cùng khối lượng, chất có c lớn hơn sẽ có Δt nhỏ hơn, tức nóng lên chậm hơn. "
             "Đó cũng là lí do nước (c lớn) mất nhiều thời gian để sôi hơn dầu."),

    dict(q="Vật A nóng hơn vật B. Đặt hai vật tiếp xúc nhau trong một bình cách nhiệt "
           "cho tới khi chúng cân bằng nhiệt. Kết luận nào sau đây là đúng?",
         o=["Nhiệt lượng vật A toả ra bằng nhiệt lượng vật B thu vào.",
            "Độ giảm nhiệt độ của vật A bằng độ tăng nhiệt độ của vật B.",
            "Nội năng của vật A sau khi cân bằng nhiệt bằng nội năng của vật B.",
            "Vật có khối lượng lớn hơn sẽ luôn là vật toả nhiệt trong quá trình đó."],
         a="A",
         sol="Bình cách nhiệt nghĩa là hệ hai vật không trao đổi nhiệt với bên ngoài, nên "
             "theo định luật bảo toàn năng lượng, toàn bộ nhiệt lượng vật nóng toả ra được "
             "vật lạnh thu vào: Q_toả = Q_thu. Độ biến thiên NHIỆT ĐỘ của hai vật nói "
             "chung khác nhau vì còn phụ thuộc tích m·c của mỗi vật."),

    dict(q="Trong quá trình một chất lỏng đang sôi, mặc dù ta tiếp tục cung cấp nhiệt "
           "nhưng nhiệt độ của nó không đổi. Lí do là",
         o=["nhiệt lượng cung cấp dùng để thắng lực liên kết giữa các phân tử chất lỏng.",
            "chất lỏng đã đạt tới nhiệt độ cao nhất mà nó có thể có được.",
            "nhiệt lượng cung cấp bị toả hết ra môi trường xung quanh bình.",
            "nội năng của chất lỏng đã đạt giá trị cực đại nên không thể tăng thêm."],
         a="A",
         sol="Ở nhiệt độ sôi, nhiệt lượng cung cấp được dùng để tách các phân tử khỏi lực "
             "hút lẫn nhau, biến chất lỏng thành hơi (làm tăng thế năng tương tác phân "
             "tử), chứ không làm tăng động năng chuyển động nhiệt trung bình — mà chính "
             "đại lượng này mới quyết định nhiệt độ. Nội năng của hệ vẫn tăng đều trong "
             "suốt quá trình sôi."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo nhiệt lượng đã cung cấp cho 0,50 kg một chất. "
           "Nhiệt dung riêng của chất này ở thể rắn là",
         fig="t13a",
         o=["1300 J/(kg·K).", "650 J/(kg·K).", "2600 J/(kg·K).", "1625 J/(kg·K)."],
         a="A",
         sol="Trên đoạn MN, chất còn ở thể rắn và nóng từ −50 °C lên 0 °C, tức ΔT = 50 K, "
             "nhận nhiệt lượng Q = 32,5 kJ = 32 500 J.\n"
             "c_rắn = Q/(mΔT) = 32 500/(0,50 × 50) = 32 500/25 = 1300 J/(kg·K)."),

    dict(q="Vẫn với đồ thị của 0,50 kg chất nói trên, nhiệt nóng chảy riêng của chất là",
         fig="t13a",
         o=["2,1·10⁵ J/kg.", "1,05·10⁵ J/kg.", "4,2·10⁵ J/kg.", "0,65·10⁵ J/kg."],
         a="A",
         sol="Đoạn NP nằm ngang ứng với sự nóng chảy, nhiệt lượng cần dùng là "
             "Q = 137,5 − 32,5 = 105 kJ = 105 000 J cho khối lượng m = 0,50 kg.\n"
             "λ = Q/m = 105 000/0,50 = 2,1·10⁵ J/kg.\n"
             "Sai lầm thường gặp là lấy thẳng 105 000 J làm λ (quên chia cho khối lượng), "
             "dẫn tới kết quả 1,05·10⁵ J/kg."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo thời gian của hai vật A và B đặt tiếp xúc nhau "
           "trong bình cách nhiệt. Vật A có khối lượng 1,0 kg, vật B là 2,0 kg nước. Nhiệt "
           "dung riêng của vật A là",
         fig="t13c",
         o=["2100 J/(kg·K).", "4200 J/(kg·K).", "1050 J/(kg·K).", "8400 J/(kg·K)."],
         a="A",
         sol="Từ đồ thị: vật A nguội từ 90 °C xuống 34 °C (ΔT_A = 56 K); vật B nóng từ "
             "20 °C lên 34 °C (ΔT_B = 14 K).\n"
             "Nhiệt lượng B thu: Q = 2,0 × 4200 × 14 = 117 600 J.\n"
             "Bình cách nhiệt nên Q_toả = Q_thu: 1,0 × c_A × 56 = 117 600 "
             "⇒ c_A = 2100 J/(kg·K)."),

    dict(q="Thả 200 g nước đá ở −5 °C vào 800 g nước ở 45 °C trong bình cách nhiệt. Nhiệt "
           "độ của hỗn hợp khi cân bằng nhiệt xấp xỉ",
         o=["19,6 °C.", "16,4 °C.", "22,3 °C.", "24,8 °C."],
         a="A",
         sol="Bước 1 – nước đá có tan hết không?\n"
             "Nhiệt lượng nước có thể toả tối đa: 0,800 × 4200 × 45 = 151 200 J.\n"
             "Nhiệt lượng để đưa nước đá lên 0 °C rồi tan hết: 0,200 × 2100 × 5 + "
             "0,200 × 3,34·10⁵ = 2100 + 66 800 = 68 900 J < 151 200 J ⇒ nước đá tan hết.\n"
             "Bước 2 – phương trình cân bằng nhiệt với nhiệt độ cuối t:\n"
             "68 900 + 0,200 × 4200 × t = 0,800 × 4200 × (45 − t)\n"
             "68 900 + 840t = 151 200 − 3360t ⇒ 4200t = 82 300 ⇒ t ≈ 19,6 °C."),

    dict(q="Một bình cách nhiệt chứa 2,0 kg nước ở 20 °C. Thả vào bình một khối sắt khối "
           "lượng 1,5 kg đang ở 300 °C. Bỏ qua nhiệt dung của bình, nhiệt độ khi cân bằng "
           "nhiệt xấp xỉ",
         o=["41,3 °C.", "36,7 °C.", "45,8 °C.", "52,4 °C."],
         a="A",
         sol="Phương trình cân bằng nhiệt: 1,5 × 460 × (300 − t) = 2,0 × 4200 × (t − 20)\n"
             "690(300 − t) = 8400(t − 20) ⇒ 207 000 − 690t = 8400t − 168 000\n"
             "⇒ 9090t = 375 000 ⇒ t ≈ 41,3 °C."),

    dict(q="Trong 1,0 phút, một bếp cung cấp đều 30 kJ cho 500 g một chất lỏng và làm "
           "nhiệt độ chất lỏng đó tăng thêm 24 °C. Bỏ qua mọi hao phí, nhiệt dung riêng "
           "của chất lỏng là",
         o=["2500 J/(kg·K).", "1250 J/(kg·K).", "720 J/(kg·K).", "5000 J/(kg·K)."],
         a="A",
         sol="c = Q/(mΔt) = 30 000/(0,500 × 24) = 30 000/12 = 2500 J/(kg·K)."),
]

DE3_P2 = [
    dict(stem="Hình vẽ là đồ thị nhiệt độ theo nhiệt lượng đã cung cấp cho 0,50 kg một "
              "chất rắn, dùng nguồn nhiệt có công suất không đổi 500 W và bỏ qua hao phí.",
         fig="t13a",
         items=[
             ("Chất bắt đầu nóng chảy khi đã nhận được 32,5 kJ và nóng chảy hoàn toàn sau "
              "khi nhận thêm 137,5 kJ nữa.", False,
              "Điểm N (32,5 kJ) đúng là lúc bắt đầu nóng chảy, nhưng điểm P ứng với TỔNG "
              "nhiệt lượng đã cung cấp là 137,5 kJ, chứ không phải nhận thêm 137,5 kJ. "
              "Phần nhiệt dành riêng cho sự nóng chảy chỉ là 137,5 − 32,5 = 105 kJ."),
             ("Nhiệt dung riêng của chất ở thể rắn là 1300 J/(kg·K).", True,
              "Đoạn MN: ΔT = 0 − (−50) = 50 K với Q = 32,5 kJ.\n"
              "c_rắn = 32 500/(0,50 × 50) = 1300 J/(kg·K)."),
             ("Nhiệt nóng chảy riêng của chất là 1,05·10⁵ J/kg.", False,
              "Nhiệt lượng dùng cho sự nóng chảy là 105 kJ = 105 000 J, nhưng đó là cho cả "
              "0,50 kg. Phải chia cho khối lượng: λ = 105 000/0,50 = 2,1·10⁵ J/kg. Giá trị "
              "1,05·10⁵ J/kg là kết quả sai do quên chia cho m."),
             ("Ở thể lỏng, nhiệt dung riêng của chất lớn hơn ở thể rắn.", True,
              "Đoạn PQ: chất lỏng nóng từ 0 °C lên 40 °C (ΔT = 40 K) và nhận "
              "190 − 137,5 = 52,5 kJ.\n"
              "c_lỏng = 52 500/(0,50 × 40) = 2625 J/(kg·K) > 1300 J/(kg·K). Trên đồ thị "
              "điều này thể hiện ở chỗ đoạn PQ “thoải” hơn đoạn MN."),
         ]),

    dict(stem="Hai vật A và B được đặt tiếp xúc nhau trong một bình cách nhiệt. Vật A có "
              "khối lượng 1,0 kg; vật B là 2,0 kg nước. Hình vẽ là đồ thị nhiệt độ của hai "
              "vật theo thời gian.",
         fig="t13c",
         items=[
             ("Vật A toả nhiệt còn vật B thu nhiệt.", True,
              "Đồ thị cho thấy nhiệt độ vật A giảm (từ 90 °C) còn nhiệt độ vật B tăng (từ "
              "20 °C). Nhiệt tự truyền từ vật nóng hơn (A) sang vật lạnh hơn (B)."),
             ("Trong quá trình trao đổi nhiệt, độ giảm nhiệt độ của vật A bằng độ tăng "
              "nhiệt độ của vật B.", False,
              "Vật A giảm 90 − 34 = 56 K, còn vật B chỉ tăng 34 − 20 = 14 K, tức chênh "
              "nhau 4 lần. Nhiệt lượng trao đổi thì bằng nhau, nhưng độ biến thiên nhiệt "
              "độ tỉ lệ nghịch với tích m·c của mỗi vật."),
             ("Nhiệt lượng vật B thu vào là 117,6 kJ.", True,
              "Q_thu = m_B·c_nước·ΔT_B = 2,0 × 4200 × 14 = 117 600 J = 117,6 kJ."),
             ("Nhiệt dung riêng của vật A là 4200 J/(kg·K).", False,
              "Bình cách nhiệt nên Q_toả = Q_thu = 117 600 J.\n"
              "c_A = 117 600/(1,0 × 56) = 2100 J/(kg·K), chỉ bằng một nửa nhiệt dung riêng "
              "của nước."),
         ]),

    dict(stem="Áp dụng định luật I của nhiệt động lực học ΔU = A + Q cho các tình huống "
              "sau (A và Q là công và nhiệt lượng mà hệ nhận được).",
         items=[
             ("Một khối khí nhận nhiệt lượng 400 J, đồng thời bị nén và nhận công 150 J. "
              "Nội năng của khí tăng 550 J.", True,
              "Q = +400 J, A = +150 J ⇒ ΔU = 150 + 400 = +550 J. Cả hai cách truyền năng "
              "lượng đều làm tăng nội năng nên chúng cộng lại."),
             ("Một vật rắn được cọ xát, nhận công 250 J và đồng thời toả ra môi trường "
              "90 J. Nội năng của vật tăng 340 J.", False,
              "Q = −90 J (toả nhiệt), A = +250 J ⇒ ΔU = 250 − 90 = +160 J, chứ không phải "
              "340 J. Kết quả 340 J là do cộng thay vì trừ phần nhiệt toả ra."),
             ("Trong một quá trình đoạn nhiệt, độ biến thiên nội năng của hệ bằng công mà "
              "hệ nhận được.", True,
              "Đoạn nhiệt nghĩa là hệ không trao đổi nhiệt với bên ngoài, Q = 0, do đó "
              "ΔU = A. Nén đoạn nhiệt (A > 0) làm hệ nóng lên; dãn nở đoạn nhiệt (A < 0) "
              "làm hệ lạnh đi."),
             ("Nếu nội năng của một hệ không thay đổi thì hệ đó chắc chắn không trao đổi "
              "nhiệt lượng và cũng không trao đổi công với bên ngoài.", False,
              "ΔU = 0 chỉ có nghĩa là A + Q = 0, tức A = −Q. Hệ hoàn toàn có thể vừa nhận "
              "một nhiệt lượng Q vừa thực hiện một công đúng bằng Q lên bên ngoài. Đó "
              "chính là quá trình đẳng nhiệt của khí lí tưởng."),
         ]),

    dict(stem="Xét các phát biểu về sự chuyển thể và ứng dụng của nó trong đời sống.",
         items=[
             ("Nước đá ở 0 °C có nội năng nhỏ hơn cùng khối lượng nước ở 0 °C.", True,
              "Muốn biến nước đá 0 °C thành nước 0 °C phải cung cấp nhiệt nóng chảy "
              "3,34·10⁵ J/kg. Nhiệt độ như nhau nên phần động năng chuyển động nhiệt như "
              "nhau; phần chênh lệch nằm ở thế năng tương tác phân tử. Vậy nước ở 0 °C có "
              "nội năng lớn hơn."),
             ("Trong quá trình nước sôi ở 100 °C, nhiệt độ không đổi nên nội năng của hệ "
              "nước – hơi cũng không đổi.", False,
              "Hệ vẫn liên tục nhận nhiệt để hoá hơi, phần nhiệt này làm tăng thế năng "
              "tương tác phân tử nên nội năng của hệ TĂNG, dù nhiệt độ giữ nguyên. Nhiệt "
              "độ chỉ phản ánh phần động năng chuyển động nhiệt trung bình."),
             ("Ở vùng núi cao, nước sôi ở nhiệt độ thấp hơn 100 °C vì áp suất khí quyển ở "
              "đó nhỏ hơn.", True,
              "Nhiệt độ sôi phụ thuộc áp suất: áp suất càng nhỏ thì các bọt hơi càng dễ "
              "hình thành và lớn lên trong lòng chất lỏng, nên nước sôi ở nhiệt độ thấp "
              "hơn. Đó là lí do nấu ăn trên núi cao lâu chín và người ta phải dùng nồi áp "
              "suất."),
             ("Muốn làm nguội nhanh một cốc nước nóng thì nên đậy nắp lại.", False,
              "Đậy nắp làm hơi nước bị giữ lại phía trên mặt thoáng, hạn chế sự bay hơi — "
              "mà bay hơi là kênh thoát nhiệt rất hiệu quả vì mỗi kilôgam nước bay hơi lấy "
              "đi tới 2,26·10⁶ J. Vì vậy đậy nắp làm nước nguội CHẬM hơn. Muốn nguội "
              "nhanh nên mở nắp, khuấy đều hoặc thổi lên mặt thoáng."),
         ]),
]

DE3_P3 = [
    dict(q="Vẫn với chất rắn trong đồ thị của Câu 8 (0,50 kg, nguồn nhiệt công suất không "
           "đổi 500 W, bỏ qua hao phí). Tính thời gian (theo phút) kể từ lúc chất bắt đầu "
           "nóng chảy tới lúc nóng chảy hoàn toàn. (Kết quả làm tròn đến hàng phần mười.)",
         fig="t13a",
         ans="3,5",
         sol="Nhiệt lượng dành cho sự nóng chảy đọc trên đồ thị: "
             "Q = 137,5 − 32,5 = 105 kJ = 105 000 J.\n"
             "Thời gian: τ = Q/P = 105 000/500 = 210 s = 3,5 phút."),

    dict(q="Thả một quả cầu chì khối lượng 300 g đang ở 98 °C vào 250 g nước ở 24 °C đựng "
           "trong một nhiệt lượng kế có nhiệt dung 80 J/K (nhiệt lượng kế ban đầu cũng ở "
           "24 °C). Tính nhiệt độ khi cân bằng nhiệt (theo °C, làm tròn đến hàng phần "
           "mười).",
         ans="26,5",
         sol="Gọi t là nhiệt độ cân bằng. Vế thu nhiệt gồm cả nước lẫn nhiệt lượng kế:\n"
             "Q_thu = (0,250 × 4200 + 80)(t − 24) = (1050 + 80)(t − 24) = 1130(t − 24).\n"
             "Q_toả = 0,300 × 130 × (98 − t) = 39,0(98 − t).\n"
             "Cân bằng: 39,0(98 − t) = 1130(t − 24)\n"
             "3822 − 39t = 1130t − 27 120 ⇒ 1169t = 30 942 ⇒ t ≈ 26,5 °C.\n"
             "Nhận xét: chì có nhiệt dung riêng rất nhỏ (130) nên dù nóng tới 98 °C nó chỉ "
             "làm nước ấm lên khoảng 2,5 °C."),

    dict(q="Một tủ lạnh cần lấy đi 3,0·10⁵ J nhiệt lượng để chuyển một lượng nước đang ở "
           "0 °C thành nước đá ở 0 °C rồi tiếp tục làm lạnh khối nước đá đó xuống −8 °C. "
           "Tính khối lượng nước ban đầu (theo g, làm tròn đến hàng đơn vị).",
         ans="855",
         sol="Nhiệt lượng phải lấy đi gồm hai phần:\n"
             "• Đông đặc ở 0 °C: Q₁ = λm = 3,34·10⁵·m.\n"
             "• Làm lạnh nước đá từ 0 °C xuống −8 °C: Q₂ = m × 2100 × 8 = 16 800·m.\n"
             "Tổng: (334 000 + 16 800)·m = 350 800·m = 3,0·10⁵\n"
             "⇒ m = 300 000/350 800 ≈ 0,8552 kg ≈ 855 g."),

    dict(q="Người ta đun 2,5 kg nước từ 30 °C bằng một bếp cung cấp nhiệt với công suất "
           "hữu ích 700 W. Sau bao lâu (theo phút) nước bắt đầu sôi ở 100 °C? (Kết quả làm "
           "tròn đến hàng phần mười.)",
         ans="17,5",
         sol="Q = mcΔt = 2,5 × 4200 × (100 − 30) = 2,5 × 4200 × 70 = 735 000 J.\n"
             "τ = Q/P = 735 000/700 = 1050 s = 17,5 phút."),

    dict(q="Một khối khí lần lượt trải qua hai quá trình: (1) nhận nhiệt lượng 600 J và "
           "dãn nở, thực hiện công 250 J lên môi trường; (2) toả ra 400 J nhiệt lượng "
           "trong khi thể tích của khí được giữ không đổi. Tính độ biến thiên nội năng "
           "tổng cộng của khối khí (theo J).",
         ans="−50",
         sol="Quá trình 1: Q₁ = +600 J, A₁ = −250 J ⇒ ΔU₁ = −250 + 600 = +350 J.\n"
             "Quá trình 2: thể tích không đổi nên A₂ = 0; Q₂ = −400 J ⇒ ΔU₂ = −400 J.\n"
             "Tổng: ΔU = 350 − 400 = −50 J. Nội năng của khối khí giảm 50 J so với ban "
             "đầu."),

    dict(q="Đổ 1,2 kg nước ở 95 °C vào một bình nhôm khối lượng 500 g đang ở 25 °C. Bỏ qua "
           "sự trao đổi nhiệt với môi trường. Tính nhiệt độ khi cân bằng nhiệt (theo °C, "
           "làm tròn đến hàng phần mười).",
         ans="89,4",
         sol="Phương trình cân bằng nhiệt: 1,2 × 4200 × (95 − t) = 0,500 × 880 × (t − 25)\n"
             "5040(95 − t) = 440(t − 25) ⇒ 478 800 − 5040t = 440t − 11 000\n"
             "⇒ 5480t = 489 800 ⇒ t ≈ 89,4 °C.\n"
             "Nước chỉ nguội đi khoảng 5,6 °C vì nhiệt dung của bình nhôm (440 J/K) rất "
             "nhỏ so với nhiệt dung của lượng nước (5040 J/K)."),
]

DE3 = dict(code="C1-03", so="03", chuong=1,
           title="ĐỀ KIỂM TRA CHƯƠNG I – ĐỀ SỐ 03",
           subtitle="Chương I – Vật lí nhiệt",
           p1=DE3_P1, p2=DE3_P2, p3=DE3_P3)


# ===================================================================================
#                ĐỀ SỐ 04 – VẬN DỤNG VÀ PHÂN HOÁ
# ===================================================================================

DE4_P1 = [
    dict(q="Khi hai vật có nhiệt độ khác nhau tiếp xúc nhiệt với nhau thì nhiệt",
         o=["tự truyền từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn.",
            "tự truyền từ vật có nội năng lớn hơn sang vật có nội năng nhỏ hơn.",
            "tự truyền từ vật có khối lượng lớn hơn sang vật có khối lượng nhỏ hơn.",
            "được truyền theo cả hai chiều với những lượng luôn bằng nhau."],
         a="A",
         sol="Chiều truyền nhiệt tự phát được quyết định bởi hiệu nhiệt độ, không phụ "
             "thuộc nội năng hay khối lượng. Một cốc nước sôi nhỏ vẫn truyền nhiệt cho một "
             "bể nước lạnh có nội năng lớn hơn nó rất nhiều."),

    dict(q="Nhiệt dung riêng của nước lớn hơn của dầu ăn. Điều đó có nghĩa là với cùng "
           "khối lượng và cùng độ tăng nhiệt độ thì",
         o=["nước cần nhận nhiều nhiệt lượng hơn dầu ăn.",
            "nước cần nhận ít nhiệt lượng hơn dầu ăn.",
            "nước nóng lên nhanh hơn dầu ăn khi đun cùng bếp.",
            "nước có nhiệt độ sôi cao hơn hẳn so với dầu ăn."],
         a="A",
         sol="Từ Q = mcΔt, với cùng m và cùng Δt thì Q tỉ lệ thuận với c. Nước có c lớn "
             "hơn nên cần nhiều nhiệt lượng hơn, và do đó khi đun bằng cùng một bếp nó "
             "nóng lên CHẬM hơn. Nhiệt độ sôi là một tính chất khác, không suy ra được từ "
             "nhiệt dung riêng (thực tế dầu ăn sôi ở nhiệt độ cao hơn nước)."),

    dict(q="Trong hệ SI, nhiệt lượng được đo bằng đơn vị",
         o=["jun (J).", "oát (W).", "kenvin (K).", "calo (cal)."],
         a="A",
         sol="Nhiệt lượng là một dạng truyền năng lượng nên có đơn vị SI là jun (J). Oát "
             "là đơn vị công suất, kenvin là đơn vị nhiệt độ; calo là đơn vị nhiệt lượng "
             "cũ, không thuộc hệ SI (1 cal ≈ 4,18 J)."),

    dict(q="Một hệ vừa nhận nhiệt lượng vừa dãn nở sinh công lên môi trường. Nội năng của "
           "hệ",
         o=["có thể tăng, giảm hoặc không đổi, tuỳ độ lớn của nhiệt lượng và của công.",
            "chắc chắn tăng vì hệ đã nhận thêm nhiệt lượng từ bên ngoài.",
            "chắc chắn giảm vì hệ đã mất năng lượng để thực hiện công.",
            "chắc chắn không đổi vì nhiệt lượng nhận vào bù đúng cho công sinh ra."],
         a="A",
         sol="ΔU = A + Q với Q > 0 và A < 0. Dấu của tổng phụ thuộc vào việc |A| lớn hơn, "
             "nhỏ hơn hay bằng Q. Ví dụ: Q = 500 J, A = −300 J cho ΔU = +200 J; nhưng "
             "Q = 500 J, A = −700 J lại cho ΔU = −200 J."),

    dict(q="Sau khi bơm xe đạp một lúc, ta thấy thân bơm nóng lên. Nguyên nhân chủ yếu là",
         o=["khí trong bơm bị nén nên nhận công, đồng thời có ma sát giữa pit-tông và "
            "thành bơm.",
            "không khí bên ngoài có nhiệt độ cao nên đã truyền nhiệt lượng vào thân bơm.",
            "áp suất khí quyển tăng lên làm nhiệt độ của thân bơm tăng theo.",
            "khối lượng khí bên trong bơm tăng lên nên nội năng của khối khí tăng."],
         a="A",
         sol="Đây là ví dụ điển hình của việc làm tăng nội năng bằng THỰC HIỆN CÔNG. Khi "
             "nén nhanh, khí gần như không kịp trao đổi nhiệt (quá trình gần đoạn nhiệt) "
             "nên ΔU ≈ A > 0, khí nóng lên và truyền nhiệt cho thân bơm; ma sát giữa "
             "pit-tông và thành bơm cũng sinh công làm nóng thêm."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo thời gian của hai mẫu chất lỏng I và II có "
           "cùng khối lượng, được đun bằng cùng một bếp cung cấp nhiệt đều. Kết luận nào "
           "sau đây là đúng?",
         fig="t14a",
         o=["Mẫu I có nhiệt dung riêng nhỏ hơn mẫu II.",
            "Mẫu I có nhiệt dung riêng lớn hơn mẫu II.",
            "Hai mẫu có nhiệt dung riêng bằng nhau vì cùng đạt 80 °C.",
            "Không so sánh được vì chưa biết công suất của bếp."],
         a="A",
         sol="Cùng bếp và cùng thời gian nghĩa là cùng nhiệt lượng cung cấp. Mẫu I chỉ cần "
             "6 phút để tăng 60 °C, còn mẫu II cần tới 10 phút cho cùng độ tăng đó, tức "
             "mẫu II “ngốn” nhiều nhiệt hơn. Với cùng khối lượng, chất nào cần nhiều nhiệt "
             "hơn cho cùng Δt thì có c lớn hơn: c_I < c_II. Việc chưa biết công suất bếp "
             "không cản trở việc SO SÁNH."),

    dict(q="Nhiệt kế thuỷ ngân đo được nhiệt độ là nhờ",
         o=["sự nở vì nhiệt của thuỷ ngân trong ống mao dẫn.",
            "sự thay đổi màu sắc của thuỷ ngân theo nhiệt độ.",
            "sự thay đổi khối lượng riêng của thuỷ tinh làm vỏ ống.",
            "sự thay đổi điện trở của cột thuỷ ngân theo nhiệt độ."],
         a="A",
         sol="Thuỷ ngân nở vì nhiệt gần như đều đặn trong một khoảng nhiệt độ rộng; chiều "
             "dài cột thuỷ ngân trong ống mao dẫn tiết diện nhỏ vì thế phụ thuộc đơn trị "
             "vào nhiệt độ và được dùng làm đại lượng đo. Nguyên tắc điện trở thay đổi "
             "theo nhiệt độ được dùng trong nhiệt kế điện trở, không phải nhiệt kế thuỷ "
             "ngân."),

    dict(q="Trong một bình cách nhiệt lí tưởng, tổng nhiệt lượng do các vật toả ra bằng "
           "tổng nhiệt lượng do các vật khác thu vào. Đây là hệ quả trực tiếp của",
         o=["định luật bảo toàn năng lượng.",
            "định luật bảo toàn khối lượng.",
            "nguyên lí truyền nhiệt từ nóng sang lạnh.",
            "định nghĩa của khái niệm nhiệt dung riêng."],
         a="A",
         sol="Bình cách nhiệt lí tưởng không cho năng lượng ra vào, cũng không có công "
             "được thực hiện, nên tổng nội năng của hệ bảo toàn. Năng lượng chỉ chuyển từ "
             "vật nóng sang vật lạnh, dẫn tới Q_toả = Q_thu. Nguyên lí truyền nhiệt chỉ "
             "cho biết CHIỀU truyền chứ không cho biết độ lớn."),

    dict(q="Khi đo nhiệt dung riêng của một kim loại bằng phương pháp hỗn hợp (thả khối "
           "kim loại đã nung nóng vào nước lạnh trong nhiệt lượng kế), nếu bỏ qua nhiệt "
           "lượng mà nhiệt lượng kế và môi trường nhận được thì giá trị tính được sẽ",
         o=["nhỏ hơn giá trị thực.", "lớn hơn giá trị thực.",
            "bằng đúng giá trị thực.", "lớn hơn hoặc nhỏ hơn tuỳ khối lượng nước."],
         a="A",
         sol="Thực tế Q_toả của kim loại = Q_nước + Q_nlk + Q_hp, trong đó nlk là nhiệt "
             "lượng kế còn hp là hao phí ra môi trường. Khi bỏ "
             "qua hai số hạng sau, ta chỉ lấy Q_toả = Q_nước, tức đánh giá thiếu nhiệt "
             "lượng mà kim loại đã toả. Vì c = Q_toả/(m·Δt) với m và Δt đã đo chính xác, "
             "giá trị c tính được sẽ NHỎ hơn giá trị thực. Đây là một sai số hệ thống, "
             "luôn lệch về một phía."),

    dict(q="Hai mẫu chất lỏng I và II trong đồ thị nói trên đều có khối lượng 0,50 kg và "
           "được đun bằng bếp cung cấp nhiệt hữu ích 250 W. Nhiệt dung riêng của mẫu I là",
         fig="t14a",
         o=["3000 J/(kg·K).", "1500 J/(kg·K).", "5000 J/(kg·K).", "6000 J/(kg·K)."],
         a="A",
         sol="Mẫu I tăng từ 20 °C lên 80 °C (Δt = 60 K) trong 6,0 phút = 360 s.\n"
             "Nhiệt lượng nhận được: Q = P·τ = 250 × 360 = 90 000 J.\n"
             "c_I = Q/(mΔt) = 90 000/(0,50 × 60) = 3000 J/(kg·K)."),

    dict(q="Vẫn với hai mẫu chất lỏng trong đồ thị đó, tỉ số giữa nhiệt dung riêng của mẫu "
           "II và của mẫu I xấp xỉ",
         fig="t14a",
         o=["1,67.", "0,60.", "1,25.", "2,50."],
         a="A",
         sol="Cùng khối lượng, cùng độ tăng nhiệt độ 60 K, cùng công suất bếp nên nhiệt "
             "lượng cần cung cấp tỉ lệ thuận với thời gian đun:\n"
             "c_II/c_I = τ_II/τ_I = 10/6 ≈ 1,67.\n"
             "Kiểm chứng: c_II = 250 × 600/(0,50 × 60) = 5000 J/(kg·K); "
             "5000/3000 ≈ 1,67."),

    dict(q="Hình vẽ là đồ thị khối lượng nước đá còn lại theo thời gian khi đun 400 g nước "
           "đá ở 0 °C bằng một bếp cung cấp nhiệt đều. Công suất hữu ích của bếp xấp xỉ",
         fig="t14c",
         o=["223 W.", "133 W.", "334 W.", "22,3 W."],
         a="A",
         sol="Đồ thị cho biết 400 g nước đá tan hết trong 10 phút = 600 s.\n"
             "Nhiệt lượng đã cung cấp: Q = λm = 3,34·10⁵ × 0,400 = 133 600 J.\n"
             "P = Q/τ = 133 600/600 ≈ 223 W. Giá trị 133 W là kết quả sai do nhầm 133,6 kJ "
             "với công suất."),

    dict(q="Hình vẽ là sơ đồ một bình đun nước nóng chứa 5,0 kg nước ở 22 °C, dây đốt có "
           "công suất điện 1500 W, hiệu suất của bình là 85 %. Thời gian cần thiết để đun "
           "nước tới 70 °C xấp xỉ",
         fig="t14b",
         o=["13,2 phút.", "11,2 phút.", "15,5 phút.", "9,5 phút."],
         a="A",
         sol="Nhiệt lượng có ích: Q = 5,0 × 4200 × (70 − 22) = 5,0 × 4200 × 48 "
             "= 1 008 000 J.\n"
             "Công suất hữu ích: P_ích = 0,85 × 1500 = 1275 W.\n"
             "τ = 1 008 000/1275 ≈ 790,6 s ≈ 13,2 phút.\n"
             "Nếu quên hiệu suất (lấy thẳng 1500 W) sẽ ra 11,2 phút — đó chính là cái bẫy "
             "của phương án nhiễu."),

    dict(q="Trộn ba lượng nước: 1,0 kg ở 20 °C, 2,0 kg ở 40 °C và 3,0 kg ở 70 °C trong một "
           "bình cách nhiệt. Nhiệt độ của hỗn hợp khi cân bằng nhiệt xấp xỉ",
         o=["51,7 °C.", "43,3 °C.", "56,7 °C.", "48,0 °C."],
         a="A",
         sol="Vì cùng chất nên nhiệt độ cân bằng là trung bình có trọng số theo khối "
             "lượng:\n"
             "t = (1,0 × 20 + 2,0 × 40 + 3,0 × 70)/(1,0 + 2,0 + 3,0) = "
             "(20 + 80 + 210)/6,0 = 310/6,0 ≈ 51,7 °C.\n"
             "Chú ý không được lấy trung bình cộng đơn thuần (20 + 40 + 70)/3 ≈ 43,3 °C — "
             "đó là phương án nhiễu."),

    dict(q="Thả 500 g nước đá ở −10 °C vào 500 g nước ở 20 °C đựng trong bình cách nhiệt. "
           "Trạng thái của hỗn hợp khi cân bằng nhiệt là",
         o=["0 °C, còn khoảng 406 g nước đá chưa tan.",
            "0 °C, toàn bộ nước đá vừa vặn tan hết.",
            "khoảng 2,4 °C, chỉ còn nước ở thể lỏng.",
            "khoảng −1,8 °C, toàn bộ hỗn hợp đã đông đặc."],
         a="A",
         sol="Nhiệt lượng lớn nhất mà nước có thể toả ra khi hạ từ 20 °C xuống 0 °C:\n"
             "Q_toả = 0,500 × 4200 × 20 = 42 000 J.\n"
             "Nhiệt lượng để đưa nước đá từ −10 °C lên 0 °C: 0,500 × 2100 × 10 = 10 500 J. "
             "Còn dư 42 000 − 10 500 = 31 500 J.\n"
             "Muốn tan hết 500 g nước đá cần 0,500 × 3,34·10⁵ = 167 000 J ≫ 31 500 J nên "
             "nước đá KHÔNG tan hết, hỗn hợp dừng ở 0 °C.\n"
             "Khối lượng đã tan: m = 31 500/334 000 ≈ 0,0943 kg ≈ 94 g, nên còn lại "
             "500 − 94 ≈ 406 g nước đá."),

    dict(q="Một nhiệt lượng kế bằng đồng khối lượng 150 g chứa 250 g nước, tất cả đang ở "
           "20 °C. Thả vào đó 100 g nước đá ở 0 °C. Nhiệt độ của hỗn hợp khi cân bằng "
           "nhiệt là",
         o=["0 °C và nước đá không tan hết.",
            "khoảng 3,2 °C và nước đá đã tan hết.",
            "khoảng 5,6 °C và nước đá đã tan hết.",
            "khoảng −2,1 °C và một phần nước đã đông đặc."],
         a="A",
         sol="Nhiệt dung của hệ “nhiệt lượng kế + nước”:\n"
             "C = 0,150 × 380 + 0,250 × 4200 = 57 + 1050 = 1107 J/K.\n"
             "Nhiệt lượng tối đa hệ này toả ra khi hạ từ 20 °C xuống 0 °C: "
             "Q_toả = 1107 × 20 = 22 140 J.\n"
             "Nhiệt lượng cần để làm tan hết 100 g nước đá: 0,100 × 3,34·10⁵ = 33 400 J.\n"
             "Vì 22 140 J < 33 400 J nên nước đá chỉ tan một phần và nhiệt độ cân bằng "
             "đúng bằng 0 °C. (Lượng đã tan: 22 140/334 000 ≈ 66 g.)"),

    dict(q="Dẫn 50 g hơi nước ở 100 °C vào 1,0 kg nước ở 20 °C đựng trong bình cách nhiệt. "
           "Nhiệt độ khi cân bằng nhiệt xấp xỉ",
         o=["49,4 °C.", "43,8 °C.", "46,7 °C.", "52,1 °C."],
         a="A",
         sol="Hơi nước toả nhiệt qua hai giai đoạn: ngưng tụ ở 100 °C rồi nguội từ 100 °C "
             "xuống t.\n"
             "Q_toả = 0,050 × 2,26·10⁶ + 0,050 × 4200 × (100 − t) = 113 000 + 210(100 − t)"
             "\nQ_thu = 1,0 × 4200 × (t − 20).\n"
             "113 000 + 21 000 − 210t = 4200t − 84 000 ⇒ 4410t = 218 000 ⇒ t ≈ 49,4 °C.\n"
             "Kết quả nhỏ hơn 100 °C nên giả thiết “hơi ngưng tụ hết” là hợp lí. Chú ý chỉ "
             "50 g hơi mà làm 1 kg nước nóng thêm gần 30 °C — đó là do nhiệt hoá hơi riêng "
             "rất lớn."),

    dict(q="Đun 1,0 kg nước từ 25 °C bằng một bếp có công suất hữu ích 800 W. Sau 7,0 phút "
           "đun liên tục, nhiệt độ của nước trong ấm là",
         o=["100 °C.", "105 °C.", "95 °C.", "80 °C."],
         a="A",
         sol="Nhiệt lượng đã cung cấp: Q = 800 × 420 = 336 000 J.\n"
             "Nhiệt lượng cần để đưa nước từ 25 °C tới 100 °C: "
             "Q₀ = 1,0 × 4200 × 75 = 315 000 J < 336 000 J.\n"
             "Vậy nước đã sôi trước khi hết 7,0 phút. Sau khi sôi, nhiệt độ giữ nguyên "
             "100 °C và phần nhiệt dư 21 000 J dùng để hoá hơi một lượng nước nhỏ. Nếu áp "
             "dụng máy móc Δt = Q/(mc) = 80 K sẽ ra 105 °C — một kết quả vô lí ở áp suất "
             "chuẩn, đó chính là cái bẫy của câu này."),
]

DE4_P2 = [
    dict(stem="Hai mẫu chất lỏng I và II, mỗi mẫu có khối lượng 0,50 kg, được đun bằng "
              "cùng một bếp cung cấp nhiệt đều với công suất hữu ích 250 W. Hình vẽ là đồ "
              "thị nhiệt độ của hai mẫu theo thời gian đun.",
         fig="t14a",
         items=[
             ("Mẫu I nóng lên nhanh hơn nên nhiệt dung riêng của nó lớn hơn của mẫu II.",
              False,
              "Ngược lại. Cùng nhận nhiệt như nhau mà mẫu I nóng lên nhanh hơn chứng tỏ nó "
              "cần ÍT nhiệt hơn cho mỗi độ tăng, tức nhiệt dung riêng của nó NHỎ hơn "
              "(c_I = 3000 < c_II = 5000 J/(kg·K))."),
             ("Nhiệt dung riêng của mẫu I là 3000 J/(kg·K).", True,
              "Mẫu I: Δt = 60 K trong 6,0 phút = 360 s.\n"
              "Q = 250 × 360 = 90 000 J ⇒ c_I = 90 000/(0,50 × 60) = 3000 J/(kg·K)."),
             ("Nhiệt dung riêng của mẫu II là 5000 J/(kg·K).", True,
              "Mẫu II: Δt = 60 K trong 10 phút = 600 s.\n"
              "Q = 250 × 600 = 150 000 J ⇒ c_II = 150 000/(0,50 × 60) = 5000 J/(kg·K)."),
             ("Nếu tiếp tục đun mẫu I thêm 4,0 phút nữa (chưa tới nhiệt độ sôi của nó) thì "
              "nhiệt độ của mẫu I tăng thêm 60 °C.", False,
              "Nhiệt lượng thêm: Q = 250 × 240 = 60 000 J.\n"
              "Δt = Q/(m·c_I) = 60 000/(0,50 × 3000) = 40 °C chứ không phải 60 °C. Cũng có "
              "thể suy nhanh từ đồ thị: mẫu I tăng 10 °C mỗi phút, nên 4 phút thì tăng "
              "40 °C."),
         ]),

    dict(stem="Đun 400 g nước đá đang ở 0 °C bằng một bếp cung cấp nhiệt đều. Hình vẽ biểu "
              "diễn khối lượng nước đá còn lại theo thời gian đun.",
         fig="t14c",
         items=[
             ("Trong 10 phút đầu, nhiệt độ của hỗn hợp trong bình không đổi và bằng 0 °C.",
              True,
              "Trong 10 phút đầu vẫn còn nước đá chưa tan, tức hệ đang ở trạng thái nước "
              "đá và nước cùng tồn tại. Ở áp suất chuẩn trạng thái đó chỉ có thể ứng với "
              "0 °C; toàn bộ nhiệt lượng cung cấp dùng cho sự nóng chảy."),
             ("Công suất hữu ích của bếp xấp xỉ 223 W.", True,
              "Nhiệt lượng để làm tan hết 400 g nước đá: Q = 3,34·10⁵ × 0,400 = 133 600 J, "
              "trong 10 phút = 600 s.\n"
              "P = 133 600/600 ≈ 223 W."),
             ("Nếu dùng 800 g nước đá ở 0 °C với cùng chiếc bếp đó thì thời gian tan hết "
              "vẫn là 10 phút.", False,
              "Nhiệt lượng cần thiết tỉ lệ thuận với khối lượng: gấp đôi khối lượng thì "
              "cần gấp đôi nhiệt lượng. Với cùng công suất bếp, thời gian tan hết sẽ là "
              "20 phút chứ không phải 10 phút."),
             ("Sau phút thứ 10, nếu tiếp tục đun thì nhiệt độ của nước tăng đều khoảng "
              "3,2 °C mỗi phút.", False,
              "Sau khi nước đá tan hết, ta có 400 g nước lỏng. Mỗi phút bếp cung cấp "
              "Q = 223 × 60 ≈ 13 360 J, làm nhiệt độ tăng\n"
              "Δt = 13 360/(0,400 × 4200) ≈ 7,95 °C mỗi phút, tức gần 8 °C chứ không phải "
              "3,2 °C."),
         ]),

    dict(stem="Hình vẽ là sơ đồ một bình đun nước nóng chứa 5,0 kg nước ở 22 °C. Dây đốt "
              "có công suất điện 1500 W; hiệu suất của bình là 85 %.",
         fig="t14b",
         items=[
             ("Nhiệt lượng mà dây đốt toả ra trong 10 phút là 765 kJ.", False,
              "Nhiệt lượng dây đốt toả ra tính theo công suất ĐIỆN: "
              "Q = 1500 × 600 = 900 000 J = 900 kJ.\n"
              "Con số 765 kJ = 1275 × 600 là phần nhiệt CÓ ÍCH truyền cho nước, tức đã trừ "
              "hao phí — không phải nhiệt lượng dây đốt toả ra."),
             ("Nhiệt lượng cần cung cấp cho nước để nó nóng từ 22 °C lên 70 °C là 1008 kJ.",
              True,
              "Q = 5,0 × 4200 × (70 − 22) = 5,0 × 4200 × 48 = 1 008 000 J = 1008 kJ."),
             ("Thời gian đun cần thiết xấp xỉ 11,2 phút.", False,
              "Công suất hữu ích chỉ bằng 0,85 × 1500 = 1275 W, nên\n"
              "τ = 1 008 000/1275 ≈ 790,6 s ≈ 13,2 phút. Kết quả 11,2 phút ứng với việc "
              "quên hiệu suất và lấy thẳng 1500 W."),
             ("Nếu bọc thêm lớp cách nhiệt để hiệu suất tăng lên 95 % thì thời gian đun sẽ "
              "giảm khoảng 1,4 phút.", True,
              "Với H = 95 %: P_ích = 0,95 × 1500 = 1425 W ⇒ "
              "τ′ = 1 008 000/1425 ≈ 707,4 s ≈ 11,79 phút.\n"
              "Độ giảm: 13,18 − 11,79 ≈ 1,4 phút."),
         ]),

    dict(stem="Để làm lạnh nhanh 600 g nước đang ở 25 °C, người ta thả vào đó 400 g "
              "nước đá lấy từ tủ đông, có nhiệt độ −8 °C. Bình đựng được coi là cách "
              "nhiệt hoàn toàn và có nhiệt dung không đáng kể.",
         items=[
             ("Nhiệt lượng cần để đưa toàn bộ khối nước đá từ −8 °C lên 0 °C là 13,4 kJ.",
              False,
              "Phải dùng nhiệt dung riêng của NƯỚC ĐÁ: "
              "Q = 0,400 × 2100 × 8 = 6720 J ≈ 6,7 kJ.\n"
              "Con số 13,4 kJ là kết quả sai do dùng nhầm c của nước (4200)."),
             ("Nhiệt lượng lớn nhất mà 600 g nước ở 25 °C có thể toả ra khi hạ xuống 0 °C "
              "là 63,0 kJ.", True,
              "Q_max = 0,600 × 4200 × 25 = 63 000 J = 63,0 kJ. Đây là “ngân sách nhiệt” "
              "tối đa của khối nước, dùng để đối chiếu xem nước đá tan được bao nhiêu."),
             ("Toàn bộ nước đá sẽ tan hết và nhiệt độ cân bằng lớn hơn 0 °C.", False,
              "Sau khi dùng 6,7 kJ để hâm nước đá lên 0 °C, chỉ còn 63,0 − 6,7 = 56,3 kJ, "
              "trong khi muốn làm tan hết 400 g nước đá cần tới "
              "0,400 × 334 = 133,6 kJ. Vậy nước đá chỉ tan một phần, hỗn hợp dừng lại "
              "đúng ở 0 °C."),
             ("Khi cân bằng nhiệt, khối lượng nước đá còn lại xấp xỉ 232 g.", True,
              "Khối lượng nước đá đã tan: m = 56 280/334 000 ≈ 0,1685 kg ≈ 168 g.\n"
              "Còn lại: 400 − 168 ≈ 232 g nước đá, cùng tồn tại với "
              "600 + 168 = 768 g nước ở 0 °C."),
         ]),
]

DE4_P3 = [
    dict(q="Vẫn với thí nghiệm đun 400 g nước đá ở 0 °C trong đồ thị của Câu 12 (công suất "
           "hữu ích của bếp không đổi). Sau khi nước đá tan hết, cần đun thêm bao nhiêu "
           "phút nữa để nước nóng lên tới 50 °C? (Kết quả làm tròn đến hàng phần mười.)",
         fig="t14c",
         ans="6,3",
         sol="Công suất hữu ích: P = λm/τ = (3,34·10⁵ × 0,400)/600 = 133 600/600 "
             "≈ 222,7 W.\n"
             "Nhiệt lượng cần để 400 g nước nóng từ 0 °C lên 50 °C:\n"
             "Q = 0,400 × 4200 × 50 = 84 000 J.\n"
             "τ = 84 000/222,7 ≈ 377,2 s ≈ 6,3 phút."),

    dict(q="Thả một khối kim loại khối lượng 400 g đang ở 250 °C vào 600 g nước ở 20 °C "
           "đựng trong nhiệt lượng kế có nhiệt dung 120 J/K (nhiệt lượng kế cũng ở 20 °C). "
           "Nhiệt độ khi cân bằng nhiệt là 35,0 °C. Tính nhiệt dung riêng của kim loại "
           "(theo J/(kg·K), làm tròn đến hàng đơn vị).",
         ans="460",
         sol="Nhiệt lượng nước và nhiệt lượng kế thu vào:\n"
             "Q_thu = (0,600 × 4200 + 120) × (35,0 − 20) = (2520 + 120) × 15,0 "
             "= 2640 × 15,0 = 39 600 J.\n"
             "Nhiệt lượng kim loại toả ra: Q_toả = 0,400 × c × (250 − 35,0) = 86,0·c.\n"
             "Cân bằng nhiệt: 86,0·c = 39 600 ⇒ c ≈ 460 J/(kg·K). Đây chính là nhiệt dung "
             "riêng của sắt."),

    dict(q="Một bình cách nhiệt chứa 1,5 kg nước ở 80 °C. Người ta thả vào bình một lượng "
           "nước đá ở 0 °C thì nhiệt độ khi cân bằng nhiệt là 40 °C. Tính khối lượng nước "
           "đá đã thả vào (theo kg, làm tròn đến hàng phần trăm).",
         ans="0,50",
         sol="Nhiệt lượng nước nóng toả ra: Q_toả = 1,5 × 4200 × (80 − 40) = 252 000 J.\n"
             "Nước đá thu nhiệt qua hai giai đoạn: nóng chảy ở 0 °C rồi nóng lên tới "
             "40 °C:\n"
             "Q_thu = m × 3,34·10⁵ + m × 4200 × 40 = m(334 000 + 168 000) = 502 000·m.\n"
             "Cân bằng: 502 000·m = 252 000 ⇒ m ≈ 0,502 kg ≈ 0,50 kg."),

    dict(q="Một nhiệt lượng kế (bỏ qua nhiệt dung) chứa 800 g nước ở 15 °C. Người ta thả "
           "đồng thời vào đó một khối nhôm 300 g đang ở 100 °C và một khối đồng 500 g đang "
           "ở 80 °C. Tính nhiệt độ khi cân bằng nhiệt (theo °C, làm tròn đến hàng phần "
           "mười).",
         ans="24,1",
         sol="Gọi t là nhiệt độ cân bằng. Viết phương trình cân bằng nhiệt dưới dạng tổng "
             "các nhiệt lượng THU vào bằng 0 (vật toả nhiệt sẽ có số hạng âm):\n"
             "0,800 × 4200 × (t − 15) + 0,300 × 880 × (t − 100) + 0,500 × 380 × (t − 80) "
             "= 0\n"
             "3360(t − 15) + 264(t − 100) + 190(t − 80) = 0\n"
             "3360t − 50 400 + 264t − 26 400 + 190t − 15 200 = 0\n"
             "3814t = 92 000 ⇒ t ≈ 24,1 °C.\n"
             "Kết quả nằm giữa 15 °C và 80 °C nên hợp lí: cả hai khối kim loại đều toả "
             "nhiệt, nước thu nhiệt."),

    dict(q="Một lượng khí nhận nhiệt lượng 1,2 kJ, đồng thời dãn nở và thực hiện công lên "
           "môi trường bên ngoài. Nội năng của khí tăng thêm 450 J. Tính công mà khí đã "
           "thực hiện lên môi trường (theo J).",
         ans="750",
         sol="Áp dụng ΔU = A + Q với A là công khí NHẬN được:\n"
             "450 = A + 1200 ⇒ A = −750 J.\n"
             "Dấu âm nghĩa là khí không nhận mà thực hiện công lên bên ngoài, độ lớn công "
             "đó là 750 J. Kiểm tra bằng bảo toàn năng lượng: trong 1200 J nhiệt nhận vào, "
             "450 J biến thành nội năng, còn 750 J biến thành công."),

    dict(q="Đun 1,2 kg nước từ 30 °C bằng một bếp có công suất hữu ích 900 W trong 9,0 "
           "phút liên tục ở áp suất chuẩn. Tính khối lượng nước đã hoá hơi (theo g, làm "
           "tròn đến hàng phần mười).",
         ans="58,9",
         sol="Nhiệt lượng bếp cung cấp: Q = 900 × 540 = 486 000 J.\n"
             "Nhiệt lượng để đưa nước từ 30 °C tới 100 °C: "
             "Q₀ = 1,2 × 4200 × 70 = 352 800 J.\n"
             "Vì Q > Q₀ nên nước đã sôi; phần nhiệt dư dùng để hoá hơi:\n"
             "Q_hơi = 486 000 − 352 800 = 133 200 J.\n"
             "m = Q_hơi/L = 133 200/2,26·10⁶ ≈ 0,0589 kg ≈ 58,9 g."),
]

DE4 = dict(code="C1-04", so="04", chuong=1,
           title="ĐỀ KIỂM TRA CHƯƠNG I – ĐỀ SỐ 04",
           subtitle="Chương I – Vật lí nhiệt",
           p1=DE4_P1, p2=DE4_P2, p3=DE4_P3)


# ===================================================================================
#         ĐỀ SỐ 05 – TỔNG HỢP TOÀN CHƯƠNG, PHÂN HOÁ CAO
# ===================================================================================

DE5_P1 = [
    dict(q="Trong quá trình đông đặc của một chất rắn kết tinh ở áp suất không đổi, chất",
         o=["toả nhiệt ra môi trường nhưng nhiệt độ của nó không đổi.",
            "thu nhiệt từ môi trường nhưng nhiệt độ của nó không đổi.",
            "toả nhiệt ra môi trường và nhiệt độ của nó giảm đều.",
            "không trao đổi nhiệt với môi trường xung quanh nó."],
         a="A",
         sol="Đông đặc là quá trình toả nhiệt (ngược với nóng chảy là thu nhiệt). Nhiệt "
             "lượng toả ra lấy từ phần thế năng tương tác phân tử giảm đi khi các phân tử "
             "sắp xếp lại thành mạng tinh thể, nên nhiệt độ giữ nguyên ở nhiệt độ đông "
             "đặc suốt quá trình."),

    dict(q="Ở cùng một áp suất, nhiệt độ nóng chảy và nhiệt độ đông đặc của một chất rắn "
           "kết tinh",
         o=["bằng nhau.", "chênh nhau đúng 273,15 độ.",
            "khác nhau, nhiệt độ nóng chảy luôn lớn hơn.",
            "khác nhau, nhiệt độ đông đặc luôn lớn hơn."],
         a="A",
         sol="Nóng chảy và đông đặc là hai quá trình ngược nhau của cùng một sự chuyển pha "
             "rắn ↔ lỏng, nên ở cùng áp suất chúng xảy ra ở cùng một nhiệt độ. Ví dụ nước "
             "đá nóng chảy và nước đông đặc đều ở 0 °C tại áp suất chuẩn."),

    dict(q="Phát biểu nào sau đây về mô hình động học phân tử là SAI?",
         o=["Các phân tử chất khí đứng yên khi nhiệt độ của khí bằng 0 °C.",
            "Các phân tử chuyển động càng nhanh khi nhiệt độ của vật càng cao.",
            "Giữa các phân tử của một chất luôn có cả lực hút và lực đẩy.",
            "Các chất được cấu tạo từ những hạt riêng biệt là phân tử, nguyên tử."],
         a="A",
         sol="0 °C tương ứng 273,15 K, hoàn toàn không phải nhiệt độ không tuyệt đối, nên "
             "ở nhiệt độ này các phân tử vẫn chuyển động rất mạnh (tốc độ trung bình của "
             "phân tử không khí ở 0 °C vào cỡ vài trăm mét mỗi giây). Ba phát biểu còn lại "
             "đều là nội dung đúng của mô hình động học phân tử."),

    dict(q="Hình vẽ là đồ thị nhiệt độ theo nhiệt lượng đã cung cấp cho 1,0 kg một chất. "
           "Giai đoạn ② ứng với quá trình",
         fig="t15a",
         o=["chất đang nóng chảy ở 0 °C.",
            "chất rắn đang nóng dần lên tới 0 °C.",
            "chất lỏng đang nóng dần lên tới 30 °C.",
            "chất đang hoá hơi ở nhiệt độ sôi của nó."],
         a="A",
         sol="Giai đoạn ② là đoạn nằm ngang ở 0 °C: chất tiếp tục nhận nhiệt (Q tăng từ "
             "24 kJ lên 84 kJ) mà nhiệt độ không đổi, đó là dấu hiệu của chuyển thể. Vì "
             "phía trước là thể rắn (giai đoạn ① đi lên từ −40 °C) và phía sau là thể lỏng "
             "(giai đoạn ③), nên ② là quá trình nóng chảy."),

    dict(q="Vì sao dùng nước đá ở 0 °C để làm lạnh lại hiệu quả hơn dùng cùng khối lượng "
           "nước lỏng cũng ở 0 °C?",
         o=["Vì ngoài phần nhiệt để nóng lên, nước đá còn thu thêm nhiệt nóng chảy khi tan.",
            "Vì nước đá có nhiệt dung riêng lớn hơn nhiệt dung riêng của nước lỏng.",
            "Vì nước đá có nhiệt độ thấp hơn nước lỏng nên hiệu nhiệt độ lớn hơn.",
            "Vì nước đá dẫn nhiệt tốt hơn nước lỏng nên trao đổi nhiệt nhanh hơn."],
         a="A",
         sol="Cả hai đều ở 0 °C nên hiệu nhiệt độ ban đầu như nhau. Điểm khác biệt quyết "
             "định là mỗi kilôgam nước đá còn “nuốt” thêm 3,34·10⁵ J để nóng chảy trước "
             "khi bắt đầu nóng lên — lượng này tương đương với việc làm 1 kg nước tăng gần "
             "80 °C. Nhiệt dung riêng của nước đá (2100) thực ra còn nhỏ hơn của nước "
             "(4200)."),

    dict(q="Hình vẽ mô tả một bình gốm xốp đựng nước đặt nơi khô ráo, thoáng gió. Nguyên "
           "lí làm mát của bình là",
         fig="t15b",
         o=["nước thấm ra mặt ngoài bình rồi bay hơi, thu nhiệt của bình và của nước bên "
            "trong.",
            "gốm xốp dẫn nhiệt rất tốt nên truyền nhanh nhiệt của nước ra không khí.",
            "không khí lạnh bên ngoài liên tục thấm qua thành gốm vào trong bình.",
            "nước trong bình chảy ra ngoài làm khối lượng giảm nên nội năng giảm."],
         a="A",
         sol="Thành gốm xốp cho nước thấm ra mặt ngoài. Lớp nước này bay hơi và mỗi "
             "kilôgam nước bay hơi lấy đi một nhiệt lượng rất lớn (cỡ 2,4·10⁶ J), phần "
             "nhiệt đó lấy từ bình và từ khối nước còn lại, nên nước trong bình lạnh đi. "
             "Đây là nguyên lí của các bình đựng nước truyền thống và của máy làm mát bay "
             "hơi hiện đại."),

    dict(q="Khi hơi nước trong không khí ngưng tụ thành những giọt sương trên mặt kính "
           "lạnh, quá trình đó",
         o=["toả nhiệt ra môi trường xung quanh.",
            "thu nhiệt từ môi trường xung quanh.",
            "không kèm theo sự trao đổi nhiệt nào cả.",
            "làm nhiệt độ của tấm kính giảm xuống."],
         a="A",
         sol="Ngưng tụ là quá trình ngược của hoá hơi, mà hoá hơi thu nhiệt, nên ngưng tụ "
             "TOẢ nhiệt. Chính vì thế mặt kính có sương đọng lại còn được sưởi ấm thêm một "
             "chút, chứ không lạnh đi."),

    dict(q="Định luật I của nhiệt động lực học là",
         o=["dạng phát biểu của định luật bảo toàn năng lượng cho các quá trình nhiệt.",
            "định luật cho biết nhiệt chỉ tự truyền từ vật nóng sang vật lạnh.",
            "định luật xác định chiều diễn biến của mọi quá trình trong tự nhiên.",
            "định luật khẳng định nội năng của một vật luôn luôn được bảo toàn."],
         a="A",
         sol="Nội dung ΔU = A + Q chính là sự bảo toàn năng lượng: độ tăng nội năng của hệ "
             "bằng tổng năng lượng hệ nhận vào dưới hai hình thức công và nhiệt. Định luật "
             "này không nói gì về CHIỀU diễn biến — đó là nội dung của định luật II nhiệt "
             "động lực học."),

    dict(q="Hai bình cách nhiệt giống nhau, một chứa 1,0 kg nước, một chứa 1,0 kg dầu có "
           "nhiệt dung riêng 2000 J/(kg·K); cả hai cùng ở 20 °C. Cung cấp cho mỗi bình "
           "cùng một nhiệt lượng 42 kJ. Khi đó",
         o=["nhiệt độ của dầu cao hơn nhiệt độ của nước 11 °C.",
            "nhiệt độ của nước cao hơn nhiệt độ của dầu 11 °C.",
            "nhiệt độ hai bình bằng nhau vì nhận cùng một nhiệt lượng.",
            "nhiệt độ của dầu cao hơn nhiệt độ của nước 21 °C."],
         a="A",
         sol="Nước: Δt = 42 000/(1,0 × 4200) = 10 °C ⇒ 30 °C.\n"
             "Dầu: Δt = 42 000/(1,0 × 2000) = 21 °C ⇒ 41 °C.\n"
             "Vậy dầu nóng hơn nước 41 − 30 = 11 °C. Con số 21 °C là độ tăng nhiệt độ của "
             "dầu chứ không phải độ chênh lệch giữa hai bình."),

    dict(q="Dựa vào đồ thị ở Câu 4, nhiệt nóng chảy riêng của chất đó bằng",
         fig="t15a",
         o=["6,0·10⁴ J/kg.", "2,4·10⁴ J/kg.", "1,56·10⁵ J/kg.", "8,4·10⁴ J/kg."],
         a="A",
         sol="Giai đoạn nóng chảy ứng với đoạn nằm ngang, từ Q = 24 kJ tới Q = 84 kJ, tức "
             "cần 60 kJ = 60 000 J cho m = 1,0 kg.\n"
             "λ = 60 000/1,0 = 6,0·10⁴ J/kg."),

    dict(q="Vẫn với đồ thị đó, nhiệt dung riêng của chất ở thể lỏng là",
         fig="t15a",
         o=["2400 J/(kg·K).", "600 J/(kg·K).", "1200 J/(kg·K).", "5200 J/(kg·K)."],
         a="A",
         sol="Giai đoạn ③: chất lỏng nóng từ 0 °C lên 30 °C (ΔT = 30 K), nhận nhiệt lượng "
             "156 − 84 = 72 kJ = 72 000 J.\n"
             "c_lỏng = 72 000/(1,0 × 30) = 2400 J/(kg·K).\n"
             "(So sánh: ở thể rắn c = 24 000/(1,0 × 40) = 600 J/(kg·K), nhỏ hơn 4 lần.)"),

    dict(q="Hình vẽ là đồ thị công suất cấp nhiệt của một lò sấy theo thời gian. Tổng "
           "nhiệt lượng lò đã cung cấp trong 16 phút là",
         fig="t15c",
         o=["504 kJ.", "480 kJ.", "1700 kJ.", "336 kJ."],
         a="A",
         sol="Nhiệt lượng bằng diện tích hình dưới đồ thị công suất – thời gian, tính theo "
             "từng khoảng:\n"
             "• 0 → 4 phút (240 s) ở 900 W: Q₁ = 900 × 240 = 216 000 J.\n"
             "• 4 → 10 phút (360 s) ở 500 W: Q₂ = 500 × 360 = 180 000 J.\n"
             "• 10 → 16 phút (360 s) ở 300 W: Q₃ = 300 × 360 = 108 000 J.\n"
             "Tổng: Q = 216 + 180 + 108 = 504 kJ."),

    dict(q="Thả một lượng nước đá ở 0 °C vào 600 g nước ở 40 °C đựng trong bình cách "
           "nhiệt thì nhiệt độ khi cân bằng nhiệt là 10 °C và nước đá đã tan hết. Khối "
           "lượng nước đá đã thả vào xấp xỉ",
         o=["201 g.", "165 g.", "189 g.", "226 g."],
         a="A",
         sol="Đây là bài toán suy ngược: đã biết kết quả cuối, phải tìm dữ kiện đầu vào.\n"
             "Nhiệt lượng nước nóng toả ra khi hạ từ 40 °C xuống 10 °C:\n"
             "Q_toả = 0,600 × 4200 × 30 = 75 600 J.\n"
             "Nước đá thu nhiệt qua hai giai đoạn: nóng chảy hết ở 0 °C rồi cùng nóng lên "
             "tới 10 °C:\n"
             "Q_thu = m × 3,34·10⁵ + m × 4200 × 10 = m(334 000 + 42 000) = 376 000·m.\n"
             "Cân bằng: 376 000·m = 75 600 ⇒ m ≈ 0,201 kg ≈ 201 g.\n"
             "Nếu bỏ sót phần nhiệt hâm nước tan từ 0 °C lên 10 °C sẽ ra 226 g — đó chính "
             "là phương án nhiễu được cài sẵn."),

    dict(q="Bình A chứa 2,0 kg nước ở 80 °C, bình B chứa 3,0 kg nước ở 20 °C; cả hai đều "
           "cách nhiệt. Người ta múc 1,0 kg nước từ A đổ sang B, khuấy đều cho cân bằng "
           "nhiệt, rồi múc 1,0 kg nước từ B đổ trở lại A. Nhiệt độ cuối cùng của nước "
           "trong bình A là",
         o=["57,5 °C.", "50,0 °C.", "60,0 °C.", "65,0 °C."],
         a="A",
         sol="Bước 1: đổ 1,0 kg nước 80 °C sang bình B (3,0 kg ở 20 °C).\n"
             "t_B = (3,0 × 20 + 1,0 × 80)/4,0 = 140/4,0 = 35 °C. Bình A còn 1,0 kg ở "
             "80 °C.\n"
             "Bước 2: múc 1,0 kg nước ở 35 °C từ B đổ về A.\n"
             "t_A = (1,0 × 80 + 1,0 × 35)/2,0 = 57,5 °C.\n"
             "Lưu ý phải làm tuần tự theo đúng thứ tự thao tác; nếu trộn gộp cả 5 kg một "
             "lần sẽ ra 44 °C, một kết quả khác hẳn."),

    dict(q="Người ta trộn nước ở 90 °C với nước ở 20 °C trong bình cách nhiệt, thu được "
           "10 kg hỗn hợp ở 41 °C. Khối lượng nước ở 90 °C đã dùng là",
         o=["3,0 kg.", "4,2 kg.", "5,0 kg.", "7,0 kg."],
         a="A",
         sol="Gọi m₁ là khối lượng nước nóng, m₂ = 10 − m₁ là khối lượng nước lạnh.\n"
             "Cân bằng nhiệt: m₁ × 4200 × (90 − 41) = m₂ × 4200 × (41 − 20)\n"
             "49m₁ = 21m₂ ⇒ m₁/m₂ = 21/49 = 3/7.\n"
             "Với m₁ + m₂ = 10 kg ⇒ m₁ = 10 × 3/10 = 3,0 kg (và m₂ = 7,0 kg).\n"
             "Nhận xét: nhiệt độ cân bằng 41 °C gần phía nước lạnh hơn, nên khối lượng "
             "nước lạnh phải lớn hơn — kết quả phù hợp."),

    dict(q="Một bình cách nhiệt chứa 1,0 kg nước ở 10 °C. Người ta thả vào đó 500 g nước "
           "đá ở −40 °C. Trạng thái của hỗn hợp khi cân bằng nhiệt là",
         o=["0 °C, khối lượng nước đá vẫn đúng 500 g và nước vẫn đúng 1,0 kg.",
            "0 °C, một phần nước đá đã tan thành nước.",
            "0 °C, một phần nước đã đông đặc thành nước đá.",
            "khoảng 2,5 °C, toàn bộ nước đá đã tan hết."],
         a="A",
         sol="Nhiệt lượng tối đa nước có thể toả khi hạ từ 10 °C xuống 0 °C:\n"
             "Q_toả = 1,0 × 4200 × 10 = 42 000 J.\n"
             "Nhiệt lượng cần để đưa 500 g nước đá từ −40 °C lên 0 °C:\n"
             "Q_thu = 0,500 × 2100 × 40 = 42 000 J.\n"
             "Hai giá trị bằng nhau đúng bằng nhau, nên khi cả hệ vừa đạt 0 °C thì “ngân "
             "sách nhiệt” cũng vừa hết: không còn nhiệt để làm tan nước đá, và cũng không "
             "cần lấy thêm nhiệt để nước đông đặc. Hệ dừng ở 0 °C với đúng 500 g nước đá "
             "và 1,0 kg nước cùng tồn tại."),

    dict(q="Vẫn với lò sấy trong đồ thị ở Câu 12. Nếu 60 % nhiệt lượng lò cung cấp được "
           "dùng để làm bay hơi nước ở 100 °C thì khối lượng nước bay hơi trong 16 phút "
           "xấp xỉ",
         fig="t15c",
         o=["133,8 g.", "80,3 g.", "223,0 g.", "26,8 g."],
         a="A",
         sol="Tổng nhiệt lượng lò cung cấp trong 16 phút: Q = 504 kJ = 504 000 J.\n"
             "Phần dùng để hoá hơi: Q_hơi = 0,60 × 504 000 = 302 400 J.\n"
             "m = Q_hơi/L = 302 400/2,26·10⁶ ≈ 0,1338 kg ≈ 133,8 g.\n"
             "Giá trị 223,0 g ứng với việc quên nhân hệ số 60 %."),

    dict(q="Một khối kim loại ở 100 °C được thả vào một khối lượng nước xác định ở 20 °C, "
           "nhiệt độ cân bằng là 28 °C. Nếu thả cùng khối kim loại đó (cũng ở 100 °C) vào "
           "một khối lượng dầu bằng đúng khối lượng nước nói trên, cũng ở 20 °C, thì nhiệt "
           "độ cân bằng xấp xỉ bao nhiêu? Cho nhiệt dung riêng của dầu là 2100 J/(kg·K), "
           "bỏ qua nhiệt dung của bình.",
         o=["34,5 °C.", "28,0 °C.", "32,7 °C.", "36,0 °C."],
         a="A",
         sol="Gọi C = m_kl·c_kl là nhiệt dung của khối kim loại và C_n = m·4200 là nhiệt "
             "dung của lượng nước.\n"
             "Với nước: C(100 − 28) = C_n(28 − 20) ⇒ 72C = 8C_n ⇒ C = C_n/9.\n"
             "Dầu có cùng khối lượng nhưng c chỉ bằng một nửa của nước: C_d = C_n/2.\n"
             "Với dầu: C(100 − t) = C_d(t − 20) ⇒ (C_n/9)(100 − t) = (C_n/2)(t − 20)\n"
             "⇒ 2(100 − t) = 9(t − 20) ⇒ 200 − 2t = 9t − 180 ⇒ 11t = 380 ⇒ t ≈ 34,5 °C.\n"
             "Điểm mấu chốt: không cần biết riêng m hay c_kl, chỉ cần TỈ SỐ giữa các nhiệt "
             "dung, và tỉ số đó được suy ra từ chính thí nghiệm thứ nhất."),
]

DE5_P2 = [
    dict(stem="Hình vẽ là đồ thị nhiệt độ theo nhiệt lượng đã cung cấp cho 1,0 kg một "
              "chất, ban đầu ở thể rắn tại −40 °C.",
         fig="t15a",
         items=[
             ("Nhiệt dung riêng của chất ở thể rắn là 1500 J/(kg·K).", False,
              "Giai đoạn ①: chất rắn nóng từ −40 °C lên 0 °C (ΔT = 40 K) và nhận 24 kJ.\n"
              "c_rắn = 24 000/(1,0 × 40) = 600 J/(kg·K), chứ không phải 1500 J/(kg·K)."),
             ("Nhiệt nóng chảy riêng của chất là 6,0·10⁴ J/kg.", True,
              "Đoạn nằm ngang (giai đoạn ②) kéo dài từ 24 kJ đến 84 kJ, tức cần 60 kJ để "
              "làm nóng chảy hoàn toàn 1,0 kg chất.\n"
              "λ = 60 000/1,0 = 6,0·10⁴ J/kg."),
             ("Nhiệt dung riêng của chất ở thể lỏng nhỏ hơn ở thể rắn.", False,
              "Giai đoạn ③ cho c_lỏng = 72 000/(1,0 × 30) = 2400 J/(kg·K), LỚN hơn "
              "600 J/(kg·K) ở thể rắn tới 4 lần. Trên đồ thị, độ dốc của giai đoạn ③ nhỏ "
              "hơn hẳn giai đoạn ① — dốc càng thoải thì nhiệt dung riêng càng lớn."),
             ("Để đưa 2,0 kg chất này từ thể rắn ở −40 °C lên thể lỏng ở 30 °C cần cung "
              "cấp 312 kJ.", True,
              "Với 1,0 kg, tổng nhiệt lượng đọc trên đồ thị là 156 kJ. Mọi số hạng "
              "(mcΔT và λm) đều tỉ lệ thuận với khối lượng nên với 2,0 kg cần "
              "2 × 156 = 312 kJ."),
         ]),

    dict(stem="Hình vẽ là đồ thị công suất cấp nhiệt của một lò sấy theo thời gian, trong "
              "16 phút hoạt động.",
         fig="t15c",
         items=[
             ("Tổng nhiệt lượng lò cung cấp trong 16 phút là 504 kJ.", True,
              "Q = 900 × 240 + 500 × 360 + 300 × 360 = 216 000 + 180 000 + 108 000 "
              "= 504 000 J = 504 kJ. Về mặt hình học, đó là tổng diện tích ba hình chữ "
              "nhật dưới đồ thị."),
             ("Nhiệt lượng lò cung cấp trong 6 phút cuối lớn hơn trong 4 phút đầu.", False,
              "6 phút cuối: 300 × 360 = 108 kJ; 4 phút đầu: 900 × 240 = 216 kJ. Mặc dù "
              "khoảng thời gian cuối dài hơn, công suất chỉ bằng một phần ba nên nhiệt "
              "lượng chỉ bằng một nửa."),
             ("Nhiệt lượng trung bình lò cung cấp trong mỗi phút của 16 phút đó là 31,5 kJ.",
              True,
              "Nhiệt lượng trung bình mỗi phút bằng tổng nhiệt lượng chia cho tổng "
              "thời gian: 504 kJ chia cho 16 phút được 31,5 kJ mỗi phút. Đây là giá "
              "trị trung bình cho cả quá trình chứ không phải của một phút cụ thể "
              "nào: bốn phút đầu lò cấp tới 54 kJ mỗi phút."),
             ("Công suất trung bình của lò trong 16 phút là 500 W.", False,
              "P_tb = Q/τ = 504 000/(16 × 60) = 504 000/960 = 525 W. Giá trị 500 W là "
              "trung bình cộng đơn thuần của ba mức công suất "
              "(900 + 500 + 300)/3 ≈ 567 W thì cũng không đúng; phải lấy trung bình có "
              "trọng số theo thời gian."),
         ]),

    dict(stem="Trong giờ thực hành, một học sinh lấy 200 g nước đá ở −20 °C từ ngăn "
              "đông của tủ lạnh rồi thả vào 300 g nước ở 25 °C đựng trong một bình "
              "cách nhiệt. Bỏ qua nhiệt dung của bình.",
         items=[
             ("Nhiệt lượng cần để đưa toàn bộ nước đá từ −20 °C lên 0 °C là 16,8 kJ.", False,
              "Phải dùng nhiệt dung riêng của nước đá: "
              "Q = 0,200 × 2100 × 20 = 8400 J = 8,4 kJ.\n"
              "Con số 16,8 kJ là kết quả sai do lấy nhầm c = 4200 J/(kg·K) của nước."),
             ("Nước đá tan hết và nhiệt độ cân bằng của hỗn hợp khoảng 1,8 °C.", False,
              "Nhiệt lượng tối đa mà 300 g nước có thể toả ra khi hạ tới 0 °C chỉ là "
              "31,5 kJ, trong khi để hâm nước đá lên 0 °C rồi làm tan hết nó cần "
              "8,4 + 66,8 = 75,2 kJ. Vậy nước đá KHÔNG tan hết."),
             ("Khi cân bằng nhiệt, nhiệt độ của hỗn hợp bằng 0 °C.", True,
              "Khi nước đá còn dư mà nước lỏng cũng còn, hệ nhất thiết dừng ở nhiệt độ "
              "chuyển thể, tức 0 °C. Đây là dấu hiệu quan trọng: hễ tính ra “nước đá không "
              "tan hết” thì nhiệt độ cân bằng luôn là 0 °C, không cần giải phương trình."),
             ("Khối lượng nước đá đã tan xấp xỉ 69 g.", True,
              "Sau khi hâm nước đá lên 0 °C, phần nhiệt còn lại là "
              "31 500 − 8400 = 23 100 J.\n"
              "m_tan = 23 100/334 000 ≈ 0,0692 kg ≈ 69 g."),
         ]),

    dict(stem="Hình vẽ mô tả một bình gốm xốp đựng nước, được đặt ở nơi khô ráo và thoáng "
              "gió để làm mát nước bên trong.",
         fig="t15b",
         items=[
             ("Nước thấm qua thành gốm xốp và bay hơi ở mặt ngoài của bình.", True,
              "Chính cấu trúc xốp cho phép nước rỉ ra mặt ngoài, tạo một lớp nước mỏng có "
              "diện tích bay hơi lớn. Đây là điều kiện tiên quyết để cơ chế làm mát hoạt "
              "động."),
             ("Quá trình bay hơi toả nhiệt nên làm nhiệt độ nước trong bình giảm đi.", False,
              "Sai ở dấu: bay hơi là quá trình THU nhiệt. Các phân tử nước muốn thoát khỏi "
              "mặt thoáng phải thắng lực hút của các phân tử lân cận, tức cần năng lượng; "
              "năng lượng đó lấy từ chính khối nước và thành bình nên chúng lạnh đi. Nếu "
              "bay hơi toả nhiệt thì bình đã phải nóng lên."),
             ("Nếu đặt bình trong một phòng kín, không khí ẩm và lặng gió thì hiệu quả làm "
              "mát sẽ tăng lên.", False,
              "Ngược lại, hiệu quả sẽ giảm mạnh. Tốc độ bay hơi tăng khi không khí khô và "
              "có gió (hơi nước được mang đi liên tục). Trong phòng kín, ẩm và lặng gió, "
              "không khí sát mặt bình nhanh chóng bão hoà hơi nước và sự bay hơi gần như "
              "dừng lại."),
             ("Nếu tăng diện tích mặt ngoài của bình mà giữ nguyên lượng nước bên trong "
              "thì nước sẽ lạnh nhanh hơn.", True,
              "Tốc độ bay hơi tỉ lệ với diện tích mặt thoáng. Diện tích mặt ngoài lớn hơn "
              "nghĩa là mỗi giây có nhiều phân tử nước thoát ra hơn, lấy đi nhiều nhiệt "
              "hơn từ cùng một lượng nước, nên nước lạnh nhanh hơn."),
         ]),
]

DE5_P3 = [
    dict(q="Vẫn với chất trong đồ thị ở Câu 4. Tính nhiệt lượng (theo kJ) cần cung cấp để "
           "đưa 2,5 kg chất đó từ thể rắn ở −40 °C thành thể lỏng ở 30 °C. (Kết quả làm "
           "tròn đến hàng đơn vị.)",
         fig="t15a",
         ans="390",
         sol="Với 1,0 kg, đồ thị cho biết tổng nhiệt lượng cần thiết là 156 kJ (gồm "
             "24 kJ hâm nóng chất rắn, 60 kJ nóng chảy và 72 kJ hâm nóng chất lỏng).\n"
             "Cả ba số hạng đều tỉ lệ thuận với khối lượng nên với 2,5 kg:\n"
             "Q = 2,5 × 156 = 390 kJ."),

    dict(q="Một bình cách nhiệt chứa 1,0 kg nước, bên trong có đặt sẵn một khối nhôm "
           "khối lượng 400 g; cả hai đang ở 20 °C. Người ta thả thêm vào bình một khối "
           "đồng 600 g đang ở 120 °C. Bỏ qua nhiệt dung của vỏ bình. Tính nhiệt độ khi "
           "cân bằng nhiệt (theo °C, làm tròn đến hàng phần mười).",
         ans="24,8",
         sol="Chỉ khối đồng toả nhiệt; nước và khối nhôm (cùng ở 20 °C) đều thu nhiệt.\n"
             "Q_toả = 0,600 × 380 × (120 − t) = 228(120 − t).\n"
             "Q_thu = (1,0 × 4200 + 0,400 × 880)(t − 20) = (4200 + 352)(t − 20) "
             "= 4552(t − 20).\n"
             "Cân bằng: 228(120 − t) = 4552(t − 20)\n"
             "27 360 − 228t = 4552t − 91 040 ⇒ 4780t = 118 400 ⇒ t ≈ 24,8 °C."),

    dict(q="Một bình cách nhiệt chứa 2,0 kg nước ở 15 °C. Người ta dẫn hơi nước ở 100 °C "
           "vào bình cho tới khi nhiệt độ của nước trong bình là 60 °C. Tính khối lượng "
           "hơi nước đã dẫn vào (theo g, làm tròn đến hàng đơn vị).",
         ans="156",
         sol="Nước trong bình thu nhiệt: Q_thu = 2,0 × 4200 × (60 − 15) = 378 000 J.\n"
             "Hơi nước toả nhiệt qua hai giai đoạn: ngưng tụ ở 100 °C rồi nguội xuống "
             "60 °C:\n"
             "Q_toả = m × 2,26·10⁶ + m × 4200 × 40 = m(2 260 000 + 168 000) = 2 428 000·m."
             "\nCân bằng: 2 428 000·m = 378 000 ⇒ m ≈ 0,1557 kg ≈ 156 g.\n"
             "Chú ý phần nhiệt ngưng tụ chiếm hơn 93 % nhiệt lượng mà hơi toả ra; nếu bỏ "
             "sót nó thì kết quả sẽ sai gấp hơn 14 lần."),

    dict(q="Một bình cách nhiệt chứa 400 g nước ở 30 °C. Người ta bỏ vào bình các viên "
           "nước đá ở 0 °C, mỗi viên có khối lượng 20 g. Hỏi phải bỏ vào ít nhất bao nhiêu "
           "viên để khi cân bằng nhiệt trong bình vẫn còn nước đá chưa tan?",
         ans="8",
         sol="Nhiệt lượng lớn nhất mà 400 g nước ở 30 °C có thể toả ra khi hạ tới 0 °C:\n"
             "Q_toả = 0,400 × 4200 × 30 = 50 400 J.\n"
             "Nhiệt lượng cần để làm tan hoàn toàn một viên nước đá 20 g:\n"
             "q = 0,020 × 3,34·10⁵ = 6680 J.\n"
             "Số viên mà lượng nhiệt đó đủ làm tan hết: 50 400/6680 ≈ 7,54 viên.\n"
             "Vậy với 7 viên thì nước đá tan hết (còn dư nhiệt), phải bỏ ít nhất 8 viên "
             "thì mới còn nước đá chưa tan; khi đó nhiệt độ cân bằng đúng bằng 0 °C."),

    dict(q="Một lượng khí trải qua hai giai đoạn. Giai đoạn một: khí nhận nhiệt lượng "
           "800 J và dãn nở, thực hiện công 300 J lên môi trường. Giai đoạn hai: khí bị "
           "nén, nhận công 500 J từ bên ngoài và toả ra môi trường nhiệt lượng Q₂. Biết "
           "sau hai giai đoạn nội năng của khí trở về đúng giá trị ban đầu. Tính Q₂ "
           "(theo J).",
         ans="1000",
         sol="Giai đoạn 1: ΔU₁ = A₁ + Q₁ = −300 + 800 = +500 J.\n"
             "Nội năng trở về giá trị ban đầu nghĩa là ΔU₁ + ΔU₂ = 0 ⇒ ΔU₂ = −500 J.\n"
             "Giai đoạn 2: ΔU₂ = A₂ + (−Q₂) ⇒ −500 = 500 − Q₂ ⇒ Q₂ = 1000 J.\n"
             "Vậy khí phải toả ra 1000 J nhiệt lượng ở giai đoạn hai."),

    dict(q="Một bếp có công suất hữu ích 1000 W được dùng để biến 800 g nước đá ở −15 °C "
           "thành hơi nước hoàn toàn ở 100 °C. Tính thời gian cần thiết (theo phút, làm "
           "tròn đến hàng phần mười).",
         ans="40,6",
         sol="Quá trình gồm bốn giai đoạn nối tiếp:\n"
             "• Hâm nước đá từ −15 °C lên 0 °C: Q₁ = 0,800 × 2100 × 15 = 25 200 J.\n"
             "• Nóng chảy ở 0 °C: Q₂ = 0,800 × 3,34·10⁵ = 267 200 J.\n"
             "• Hâm nước từ 0 °C lên 100 °C: Q₃ = 0,800 × 4200 × 100 = 336 000 J.\n"
             "• Hoá hơi hoàn toàn ở 100 °C: Q₄ = 0,800 × 2,26·10⁶ = 1 808 000 J.\n"
             "Tổng: Q = 25 200 + 267 200 + 336 000 + 1 808 000 = 2 436 400 J.\n"
             "τ = 2 436 400/1000 = 2436,4 s ≈ 40,6 phút.\n"
             "Đáng chú ý: riêng giai đoạn hoá hơi đã chiếm gần 75 % tổng thời gian."),
]

DE5 = dict(code="C1-05", so="05", chuong=1,
           title="ĐỀ KIỂM TRA CHƯƠNG I – ĐỀ SỐ 05",
           subtitle="Chương I – Vật lí nhiệt",
           p1=DE5_P1, p2=DE5_P2, p3=DE5_P3)


DE_CH1 = [DE1, DE2, DE3, DE4, DE5]
