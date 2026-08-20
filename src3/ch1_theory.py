# -*- coding: utf-8 -*-
"""Tài liệu dạy học Chương I - VẬT LÍ NHIỆT (Vật lí 12, GDPT 2018).

Khối nội dung được viết dưới dạng danh sách các tuple:
    ("h1"|"h2"|"h3", text)      - tiêu đề các cấp
    ("p", text)                 - đoạn văn
    ("b", text)                 - gạch đầu dòng
    ("f", text)                 - công thức đặt giữa trang
    ("box", title, text)        - khung kiến thức
    ("trap", text)              - khung sai lầm thường gặp
    ("exam", text)              - khung lưu ý ôn thi
    ("fig", name, caption)      - chèn hình
    ("tbl", caption, hdr, rows) - bảng
"""

CH1 = [
    ("h1", "CHƯƠNG I – VẬT LÍ NHIỆT"),
    ("p", "Chương I mở đầu chương trình Vật lí 12 bằng việc nghiên cứu chất và các quá trình "
          "nhiệt từ hai góc nhìn bổ sung cho nhau: góc nhìn vi mô (mô hình động học phân tử) "
          "và góc nhìn vĩ mô (nội năng, nhiệt lượng, nhiệt độ, định luật I nhiệt động lực học). "
          "Toàn bộ các bài toán định lượng của chương đều xoay quanh một ý tưởng duy nhất: "
          "theo dõi dòng năng lượng đi vào và đi ra khỏi vật."),
    ("box", "PHẠM VI CHƯƠNG I THEO CHƯƠNG TRÌNH GDPT 2018",
     "Bài 1. Cấu trúc của chất. Sự chuyển thể\n"
     "Bài 2. Nội năng. Định luật I của nhiệt động lực học\n"
     "Bài 3. Nhiệt độ. Thang nhiệt độ – nhiệt kế\n"
     "Bài 4. Nhiệt dung riêng\n"
     "Bài 5. Nhiệt nóng chảy riêng\n"
     "Bài 6. Nhiệt hoá hơi riêng\n"
     "Bài 7. Bài tập về vật lí nhiệt"),

    # =============================================================== §1
    ("h2", "§1. CẤU TRÚC CỦA CHẤT VÀ MÔ HÌNH ĐỘNG HỌC PHÂN TỬ"),

    ("h3", "1.1. Ba luận điểm nền tảng"),
    ("p", "Mô hình động học phân tử là công cụ giải thích xuyên suốt cả Chương I lẫn "
          "Chương II. Mô hình gồm ba luận điểm:"),
    ("b", "Các chất được cấu tạo từ các hạt riêng biệt (nguyên tử, phân tử) vô cùng nhỏ; "
          "giữa chúng có khoảng cách."),
    ("b", "Các hạt chuyển động hỗn loạn, không ngừng. Chuyển động này gọi là chuyển động nhiệt. "
          "Nhiệt độ của vật càng cao thì các hạt chuyển động càng nhanh."),
    ("b", "Giữa các hạt có lực tương tác phân tử, gồm cả lực hút và lực đẩy. Độ lớn của lực "
          "này phụ thuộc khoảng cách giữa các hạt."),

    ("h3", "1.2. Lực tương tác phân tử – chìa khoá giải thích ba thể"),
    ("p", "Đồ thị thế năng tương tác dưới đây giải thích được hầu hết tính chất của ba thể. "
          "Đây là hình vẽ mà học sinh giỏi cần đọc được, không chỉ học thuộc."),
    ("fig", "h02_the_nang_tuong_tac",
     "Hình 1.1. Thế năng tương tác giữa hai phân tử theo khoảng cách $r$"),
    ("b", "Khi r < r₀: lực đẩy chiếm ưu thế và tăng rất nhanh khi r giảm. Đây là lí do chất rắn "
          "và chất lỏng gần như không nén được."),
    ("b", "Khi r = r₀: lực hút cân bằng lực đẩy, hợp lực bằng 0, thế năng cực tiểu. Phân tử "
          "trong chất rắn dao động quanh vị trí này."),
    ("b", "Khi r > r₀: lực hút chiếm ưu thế nhưng giảm rất nhanh theo khoảng cách. Khi r vượt "
          "quá vài lần r₀ thì lực tương tác coi như không đáng kể — đó chính là tình huống của "
          "chất khí, và là cơ sở của khái niệm khí lí tưởng ở Chương II."),

    ("h3", "1.3. So sánh ba thể của chất"),
    ("fig", "h01_cau_truc_chat",
     "Hình 1.2. Mô hình sắp xếp và chuyển động của phân tử trong ba thể"),
    ("tbl", "Bảng 1.1. So sánh cấu trúc và tính chất của ba thể",
     ["Đặc điểm", "Chất rắn (kết tinh)", "Chất lỏng", "Chất khí"],
     [["Khoảng cách giữa các phân tử", "Rất gần, cỡ kích thước phân tử",
       "Gần, xấp xỉ chất rắn", "Rất lớn so với kích thước phân tử"],
      ["Lực tương tác", "Rất mạnh", "Mạnh, yếu hơn chất rắn", "Rất yếu, hầu như bỏ qua"],
      ["Sắp xếp", "Trật tự xa (mạng tinh thể)", "Trật tự gần, mất trật tự xa", "Hoàn toàn hỗn loạn"],
      ["Chuyển động", "Dao động quanh vị trí cân bằng cố định",
       "Dao động quanh vị trí cân bằng nhưng vị trí này di chuyển", "Chuyển động thẳng tự do giữa hai va chạm"],
      ["Hình dạng", "Xác định", "Theo hình bình chứa", "Theo hình bình chứa"],
      ["Thể tích", "Xác định", "Xác định", "Bằng thể tích bình chứa"],
      ["Khả năng nén", "Rất khó", "Rất khó", "Dễ"]]),
    ("trap",
     "Sai lầm 1: cho rằng chất lỏng có khoảng cách phân tử lớn hơn hẳn chất rắn. Thực tế khối "
     "lượng riêng của nước lỏng và nước đá chênh nhau chưa tới 10 %, chứng tỏ khoảng cách phân "
     "tử gần như nhau. Điểm khác biệt cốt lõi là TRẬT TỰ SẮP XẾP và khả năng đổi chỗ, "
     "không phải khoảng cách.\n"
     "Sai lầm 2: nghĩ rằng chất lỏng chảy được vì phân tử ở xa nhau. Đúng ra: chất lỏng chảy "
     "được vì các phân tử có thể trượt qua nhau, do trật tự xa bị phá vỡ.\n"
     "Sai lầm 3: cho rằng nước đá nổi trên nước vì đá nhẹ hơn nước “do là chất rắn”. "
     "Nước đá nổi là trường hợp BẤT THƯỜNG: liên kết hydrogen tạo cấu trúc rỗng làm thể tích "
     "tăng khi đông đặc. Đa số chất khác thì thể tích giảm khi đông đặc."),

    ("h3", "1.4. Sự chuyển thể"),
    ("fig", "h03_so_do_chuyen_the", "Hình 1.3. Sáu quá trình chuyển thể và chiều trao đổi nhiệt"),
    ("p", "Bản chất năng lượng của chuyển thể: nhiệt lượng cung cấp trong quá trình chuyển thể "
          "được dùng để THẮNG LỰC TƯƠNG TÁC phân tử, tức là làm tăng thế năng tương tác, "
          "chứ không làm tăng động năng chuyển động nhiệt. Vì động năng trung bình không đổi "
          "nên nhiệt độ không đổi."),
    ("box", "TẠI SAO NHIỆT ĐỘ KHÔNG ĐỔI KHI ĐANG CHUYỂN THỂ?",
     "Nội năng gồm hai phần: động năng chuyển động nhiệt + thế năng tương tác phân tử.\n"
     "• Khi vật chỉ nóng lên (chưa chuyển thể): nhiệt lượng làm tăng ĐỘNG NĂNG → nhiệt độ tăng.\n"
     "• Khi vật đang chuyển thể: nhiệt lượng làm tăng THẾ NĂNG (phá vỡ liên kết) → "
     "động năng trung bình giữ nguyên → nhiệt độ giữ nguyên.\n"
     "Vậy trong khi nóng chảy hay sôi, vật VẪN nhận nhiệt và nội năng VẪN tăng, "
     "chỉ có nhiệt độ là không đổi."),
    ("p", "Đặc điểm quan trọng: chỉ chất RẮN KẾT TINH mới có nhiệt độ nóng chảy xác định. "
          "Chất rắn vô định hình (thuỷ tinh, nhựa đường, sáp nến) mềm dần rồi chảy lỏng "
          "trong một khoảng nhiệt độ, không có nhiệt độ nóng chảy xác định."),
    ("fig", "h12_bay_hoi_va_soi", "Hình 1.4. Phân biệt sự bay hơi và sự sôi"),
    ("tbl", "Bảng 1.2. Phân biệt bay hơi và sôi – nội dung rất hay ra đề",
     ["Tiêu chí", "Sự bay hơi", "Sự sôi"],
     [["Nơi xảy ra", "Chỉ ở mặt thoáng", "Cả ở mặt thoáng và trong lòng chất lỏng"],
      ["Nhiệt độ xảy ra", "Ở mọi nhiệt độ", "Chỉ ở nhiệt độ sôi xác định"],
      ["Nhiệt độ trong quá trình", "Chất lỏng có thể nguội đi", "Không đổi nếu áp suất không đổi"],
      ["Phụ thuộc áp suất", "Có (áp suất hơi trên mặt thoáng)", "Có, rất rõ: áp suất giảm thì nhiệt độ sôi giảm"],
      ["Yếu tố ảnh hưởng tốc độ", "Nhiệt độ, diện tích mặt thoáng, gió, độ ẩm", "Công suất cung cấp nhiệt"]]),
    ("exam",
     "Ba câu hỏi rất hay xuất hiện trong đề thi:\n"
     "• Vì sao trên đỉnh núi cao luộc trứng lâu chín? Vì áp suất khí quyển giảm → nước sôi ở "
     "nhiệt độ thấp hơn 100 °C → nhiệt độ nấu thấp hơn, không phải vì “ít oxygen”.\n"
     "• Vì sao nồi áp suất nấu nhanh nhừ? Vì áp suất trong nồi cao → nước sôi ở nhiệt độ trên "
     "100 °C. Nồi áp suất KHÔNG làm nước sôi nhanh hơn, mà làm nước sôi ở nhiệt độ CAO hơn.\n"
     "• Vì sao ra mồ hôi giúp cơ thể mát? Vì mồ hôi bay hơi lấy nhiệt hoá hơi từ cơ thể. "
     "Ngày trời nồm (độ ẩm cao) mồ hôi khó bay hơi nên ta cảm thấy oi bức."),

    # =============================================================== §2
    ("h2", "§2. NỘI NĂNG VÀ ĐỊNH LUẬT I NHIỆT ĐỘNG LỰC HỌC"),

    ("h3", "2.1. Nội năng"),
    ("p", "Nội năng của một vật là tổng động năng chuyển động nhiệt của các phân tử cấu tạo "
          "nên vật và thế năng tương tác giữa các phân tử đó. Kí hiệu U, đơn vị jun (J)."),
    ("f", "U = W_động (chuyển động nhiệt)  +  W_thế (tương tác phân tử)"),
    ("box", "NỘI NĂNG PHỤ THUỘC VÀO NHỮNG GÌ?",
     "• Nhiệt độ: nhiệt độ tăng → động năng phân tử tăng → nội năng tăng.\n"
     "• Thể tích: thể tích đổi → khoảng cách phân tử đổi → thế năng tương tác đổi → nội năng đổi.\n"
     "• Khối lượng (số phân tử): cùng nhiệt độ, vật có nhiều phân tử hơn thì nội năng lớn hơn.\n"
     "• Thể (rắn/lỏng/khí) của chất: cùng khối lượng, cùng nhiệt độ, hơi nước có nội năng lớn "
     "hơn nước lỏng vì thế năng tương tác lớn hơn.\n"
     "Nội năng KHÔNG phụ thuộc vận tốc chuyển động của cả vật và độ cao của vật — hai đại lượng "
     "đó thuộc về cơ năng, không thuộc nội năng."),
    ("trap",
     "Sai lầm kinh điển: đồng nhất “nội năng” với “nhiệt lượng”. Hai khái niệm hoàn toàn khác nhau:\n"
     "• Nội năng U là một HÀM TRẠNG THÁI: vật ở trạng thái nào thì có nội năng đó, không phụ "
     "thuộc cách đi tới trạng thái ấy. Nói “vật chứa 500 J nội năng” là hợp lệ.\n"
     "• Nhiệt lượng Q và công A là các đại lượng của QUÁ TRÌNH: chúng mô tả năng lượng đang "
     "được truyền. Nói “vật chứa 500 J nhiệt lượng” là SAI.\n"
     "Cách nhớ: nội năng giống như số tiền trong ví; nhiệt lượng và công giống như khoản tiền "
     "đang được chuyển vào hay ra khỏi ví."),
    ("p", "Cách phát biểu này cũng làm rõ vì sao câu “vật A nóng hơn nên có nội năng lớn hơn "
          "vật B” là sai nếu hai vật khác khối lượng. Một cốc nước 30 °C có nội năng lớn hơn "
          "một giọt nước 90 °C, vì số phân tử chênh lệch rất nhiều."),

    ("h3", "2.2. Hai cách làm biến đổi nội năng"),
    ("fig", "h06_hai_cach_doi_noi_nang", "Hình 1.5. Thực hiện công và truyền nhiệt"),
    ("b", "Thực hiện công: có sự chuyển hoá năng lượng từ dạng khác (cơ năng, điện năng) "
          "thành nội năng. Ví dụ: cọ xát hai bàn tay, nén nhanh khí trong bơm xe, khoan kim loại."),
    ("b", "Truyền nhiệt: nội năng truyền trực tiếp từ vật này sang vật khác, không có sự chuyển "
          "hoá dạng năng lượng. Ví dụ: đun nước, để cốc nước nóng nguội dần."),
    ("p", "Phân biệt hai cách này là một chủ đề ra đề rất phổ biến. Câu hỏi mấu chốt: có sự "
          "chuyển hoá từ dạng năng lượng khác sang nội năng hay không? Nếu có thì đó là thực "
          "hiện công; nếu chỉ là nội năng chuyển từ vật nóng sang vật lạnh thì đó là truyền nhiệt."),

    ("h3", "2.3. Định luật I của nhiệt động lực học"),
    ("fig", "h05_dinh_luat_1", "Hình 1.6. Phát biểu và quy ước dấu của định luật I"),
    ("f", "ΔU = A + Q"),
    ("p", "Trong đó ΔU = U₂ − U₁ là độ biến thiên nội năng, A là công mà hệ NHẬN được, "
          "Q là nhiệt lượng mà hệ NHẬN được. Đây chính là định luật bảo toàn năng lượng "
          "áp dụng cho các quá trình nhiệt."),
    ("tbl", "Bảng 1.3. Quy ước dấu – phải thuộc tuyệt đối chính xác",
     ["Đại lượng", "Mang dấu (+) khi", "Mang dấu (−) khi"],
     [["Q", "Hệ NHẬN nhiệt lượng (bị đun nóng)", "Hệ TOẢ nhiệt lượng (nguội đi)"],
      ["A", "Hệ NHẬN công (khí bị nén)", "Hệ SINH công (khí dãn nở, đẩy pit-tông)"],
      ["ΔU", "Nội năng tăng", "Nội năng giảm"]]),
    ("trap",
     "Sai lầm nguy hiểm nhất của Chương I: dùng nhầm quy ước dấu. Một số tài liệu cũ viết "
     "ΔU = Q − A với A là công hệ SINH ra. Chương trình GDPT 2018 dùng ΔU = A + Q với A là công "
     "hệ NHẬN. Hai cách viết cho cùng kết quả nhưng nếu trộn lẫn thì sai dấu.\n"
     "Quy tắc an toàn: luôn hỏi “hệ nhận hay hệ mất?”. Nhận thì cộng, mất thì trừ. "
     "Khi khí dãn nở đẩy pit-tông đi ra, khí MẤT năng lượng nên A < 0."),
    ("box", "BỐN TRƯỜNG HỢP RIÊNG PHẢI THUỘC",
     "• Quá trình đẳng tích (V không đổi): khí không dãn cũng không bị nén → A = 0 → ΔU = Q.\n"
     "• Quá trình đoạn nhiệt (hệ cách nhiệt, hoặc xảy ra rất nhanh): Q = 0 → ΔU = A.\n"
     "• Quá trình đẳng nhiệt của KHÍ LÍ TƯỞNG: nội năng chỉ phụ thuộc nhiệt độ nên ΔU = 0 "
     "→ Q = −A. Khí nhận bao nhiêu nhiệt thì sinh bấy nhiêu công.\n"
     "• Chu trình khép kín (trạng thái cuối trùng trạng thái đầu): ΔU = 0 → Q = −A."),
    ("fig", "h29_noi_nang_khi", "Hình 1.7. Vì sao khí lí tưởng đẳng nhiệt thì ΔU = 0"),
    ("exam",
     "Dạng câu hỏi đúng/sai rất hay gặp: “Khí nhận nhiệt thì nhiệt độ luôn tăng.” — SAI. "
     "Nếu khí vừa nhận nhiệt vừa dãn nở sinh công lớn hơn nhiệt nhận được thì ΔU < 0, nhiệt độ "
     "GIẢM. Cụ thể Q = 200 J, A = −300 J thì ΔU = −100 J.\n"
     "Ngược lại: “Khí bị nén thì nhiệt độ luôn tăng.” cũng SAI, vì có thể đồng thời toả nhiệt "
     "mạnh ra ngoài."),

    # =============================================================== §3
    ("h2", "§3. NHIỆT ĐỘ, THANG NHIỆT ĐỘ VÀ CÂN BẰNG NHIỆT"),

    ("h3", "3.1. Nhiệt độ và cân bằng nhiệt"),
    ("p", "Về mặt vi mô, nhiệt độ là đại lượng đặc trưng cho mức độ chuyển động nhiệt của các "
          "phân tử: nhiệt độ càng cao thì động năng trung bình của phân tử càng lớn. "
          "Về mặt vĩ mô, nhiệt độ là đại lượng cho biết chiều truyền nhiệt giữa hai vật."),
    ("fig", "h08_can_bang_nhiet", "Hình 1.8. Truyền nhiệt và trạng thái cân bằng nhiệt"),
    ("p", "Hai vật tiếp xúc nhiệt sẽ trao đổi nhiệt cho tới khi nhiệt độ bằng nhau — khi đó "
          "chúng ở trạng thái cân bằng nhiệt. Đây là nội dung của định luật 0 nhiệt động lực học."),
    ("trap",
     "Sai lầm rất phổ biến: “nhiệt truyền từ vật có nội năng lớn sang vật có nội năng nhỏ”. SAI. "
     "Nhiệt truyền theo CHÊNH LỆCH NHIỆT ĐỘ, hoàn toàn không quan tâm nội năng. "
     "Một chậu nước 20 °C có nội năng lớn hơn nhiều so với một chiếc đinh sắt nung 200 °C, "
     "nhưng nhiệt vẫn truyền từ đinh sang nước."),

    ("h3", "3.2. Thang nhiệt độ"),
    ("fig", "h07_thang_nhiet_do", "Hình 1.9. Đối chiếu ba thang nhiệt độ"),
    ("f", "T(K) = t(°C) + 273,15   ;   t(°F) = 1,8·t(°C) + 32"),
    ("box", "HAI CÔNG THỨC – MỘT SỰ KHÁC BIỆT SỐNG CÒN",
     "Chuyển GIÁ TRỊ nhiệt độ:  T(K) = t(°C) + 273,15\n"
     "Chuyển ĐỘ BIẾN THIÊN nhiệt độ:  ΔT(K) = Δt(°C)  — KHÔNG cộng 273!\n\n"
     "Lí do: hai thang có cùng độ chia (1 K = 1 °C về độ lớn), chỉ khác gốc. "
     "Khi lấy hiệu hai nhiệt độ thì hằng số 273,15 bị triệt tiêu.\n"
     "Hệ quả: trong công thức Q = mcΔT, ta có thể thay Δt tính bằng °C trực tiếp vào mà không "
     "cần đổi. Nhưng trong phương trình trạng thái khí lí tưởng thì BẮT BUỘC dùng Kelvin."),
    ("p", "Thang Kelvin là thang nhiệt độ tuyệt đối, có gốc 0 K là độ không tuyệt đối — "
          "trạng thái mà chuyển động nhiệt của các phân tử là nhỏ nhất có thể. "
          "Không tồn tại nhiệt độ âm trên thang Kelvin. Trong thực tế chưa bao giờ đạt được "
          "chính xác 0 K; đây là một giới hạn lí thuyết."),
    ("p", "Nguyên tắc hoạt động của nhiệt kế: dựa trên sự thay đổi của một tính chất vật lí "
          "theo nhiệt độ — sự nở vì nhiệt của chất lỏng (nhiệt kế thuỷ ngân, rượu), sự thay đổi "
          "điện trở (nhiệt kế điện trở), sức điện động nhiệt điện (cặp nhiệt điện), "
          "bức xạ hồng ngoại (nhiệt kế hồng ngoại)."),
    ("exam",
     "Bẫy tính toán hay gặp nhất của cả chương: đề cho “nhiệt độ tăng thêm 27 °C” và học sinh "
     "đổi thành 300 K. Đây là ĐỘ TĂNG, không phải giá trị, nên ΔT = 27 K.\n"
     "Ngược lại, đề cho “khí ở 27 °C” thì bắt buộc T = 300 K khi dùng phương trình trạng thái."),

    # =============================================================== §4
    ("h2", "§4. NHIỆT DUNG RIÊNG"),

    ("h3", "4.1. Định nghĩa và công thức"),
    ("p", "Nhiệt dung riêng của một chất là nhiệt lượng cần cung cấp để làm cho 1 kg chất đó "
          "tăng thêm 1 K (hay 1 °C) nhiệt độ."),
    ("f", "c = Q / (m·ΔT)      ⟺      Q = m·c·ΔT"),
    ("tbl", "Bảng 1.4. Các đại lượng trong công thức nhiệt lượng",
     ["Kí hiệu", "Tên gọi", "Đơn vị SI", "Ghi chú"],
     [["Q", "Nhiệt lượng thu vào hay toả ra", "J", "Q > 0 khi vật thu nhiệt"],
      ["m", "Khối lượng của vật", "kg", "Phải đổi từ g, tấn về kg"],
      ["c", "Nhiệt dung riêng của chất", "J/(kg·K)", "Là hằng số đặc trưng cho chất"],
      ["ΔT", "Độ biến thiên nhiệt độ", "K", "Dùng trực tiếp giá trị tính bằng °C được"]]),
    ("p", "Cần phân biệt nhiệt dung riêng c (đặc trưng cho CHẤT, đơn vị J/(kg·K)) với nhiệt dung "
          "C = m·c (đặc trưng cho VẬT cụ thể, đơn vị J/K). Hai vật cùng chất nhưng khác khối "
          "lượng có cùng c nhưng khác C."),
    ("fig", "h13_so_sanh_nhiet_dung", "Hình 1.10. Nhiệt dung riêng của một số chất"),
    ("box", "Ý NGHĨA VẬT LÍ CỦA GIÁ TRỊ c LỚN",
     "Nước có c = 4200 J/(kg·K), lớn hơn hầu hết các chất thông thường. Điều đó có nghĩa:\n"
     "• Nước rất “khó nóng lên” và cũng rất “khó nguội đi” — cùng một nhiệt lượng, nước tăng "
     "nhiệt độ ít hơn nhiều so với kim loại.\n"
     "• Vì thế nước được dùng làm chất tải nhiệt trong hệ thống làm mát động cơ, lò phản ứng.\n"
     "• Vì thế vùng ven biển có biên độ nhiệt ngày–đêm nhỏ hơn vùng sâu trong lục địa: "
     "biển hấp thụ và nhả nhiệt chậm, đóng vai trò điều hoà khí hậu.\n"
     "• Vì thế đi chân trần trên cát nóng bỏng rát trong khi nước biển bên cạnh vẫn mát: "
     "cát có c nhỏ nên nóng lên rất nhanh dưới cùng ánh nắng."),

    ("h3", "4.2. Phương trình cân bằng nhiệt"),
    ("p", "Khi các vật chỉ trao đổi nhiệt với nhau trong một hệ cách nhiệt, năng lượng được "
          "bảo toàn:"),
    ("f", "Q_toả = Q_thu      hay      ΣQ_i = 0 (dùng quy ước dấu)"),
    ("p", "Cách viết ΣQ = 0 an toàn hơn cho học sinh khá giỏi: mỗi vật đóng góp một số hạng "
          "Q_i = m_i·c_i·(t_cân bằng − t_i,ban đầu), vật nào nguội đi sẽ tự động cho Q_i âm. "
          "Cách này tránh phải đoán trước vật nào toả, vật nào thu."),
    ("box", "CÔNG THỨC NHIỆT ĐỘ CÂN BẰNG CỦA HAI VẬT",
     "Với hai vật trao đổi nhiệt và không có chuyển thể:\n\n"
     "t = (m₁c₁t₁ + m₂c₂t₂) / (m₁c₁ + m₂c₂)\n\n"
     "Đây là trung bình có TRỌNG SỐ theo tích m·c. Nhận xét quan trọng cho câu hỏi định tính: "
     "nhiệt độ cân bằng luôn nằm GIỮA hai nhiệt độ ban đầu, và lệch về phía vật có tích m·c lớn hơn."),
    ("trap",
     "Sai lầm 1: quên nhiệt lượng kế. Nếu đề cho khối lượng và nhiệt dung riêng của bình nhiệt "
     "lượng kế thì bình cũng tham gia trao đổi nhiệt và phải có mặt trong phương trình.\n"
     "Sai lầm 2: bỏ sót giai đoạn chuyển thể. Nếu bỏ nước đá 0 °C vào nước nóng, phải tính "
     "cả nhiệt nóng chảy λm rồi mới tính nhiệt để nước vừa tan nóng lên.\n"
     "Sai lầm 3: kết luận vội rằng đá tan hết. Phải KIỂM TRA bằng cách so sánh nhiệt lượng nước "
     "nóng có thể toả ra khi hạ về 0 °C với nhiệt lượng cần để làm tan hết đá."),
    ("exam",
     "Quy trình xử lí bài toán “thả nước đá vào nước nóng” — dạng vận dụng cao rất hay ra:\n"
     "Bước 1. Tính Q_A = nhiệt lượng nước nóng toả ra khi hạ tới 0 °C.\n"
     "Bước 2. Tính Q_B = nhiệt lượng cần để đưa đá lên 0 °C rồi làm tan HẾT đá.\n"
     "Bước 3. So sánh:\n"
     "  – Nếu Q_A > Q_B: đá tan hết, hỗn hợp là nước ở nhiệt độ t > 0 °C, giải phương trình "
     "cân bằng nhiệt bình thường.\n"
     "  – Nếu Q_A < Q_B: đá chỉ tan một phần, nhiệt độ cuối ĐÚNG BẰNG 0 °C. "
     "Khối lượng đá tan được tính từ m_tan = Q_A/λ.\n"
     "  – Nếu Q_A = Q_B: đá vừa vặn tan hết ở đúng 0 °C.\n"
     "Đây chính là chỗ nhiều học sinh mất điểm vì bỏ qua bước kiểm tra."),

    ("h3", "4.3. Thí nghiệm đo nhiệt dung riêng"),
    ("fig", "h09_do_nhiet_dung_rieng", "Hình 1.11. Bộ dụng cụ đo nhiệt dung riêng của nước"),
    ("p", "Nguyên tắc: cung cấp nhiệt lượng đã biết bằng dòng điện (đọc công suất P trên oát kế, "
          "đo thời gian t), đồng thời đo độ tăng nhiệt độ ΔT. Khi đó Q = P·t = m·c·ΔT."),
    ("p", "Kĩ thuật xử lí số liệu chuẩn xác nhất không phải là tính c cho từng lần đo rồi lấy "
          "trung bình, mà là vẽ đồ thị Q theo ΔT. Nếu đồ thị là đường thẳng qua gốc toạ độ thì "
          "định luật được nghiệm đúng, và c được suy ra từ hệ số góc."),
    ("fig", "h10_do_thi_Q_deltaT", "Hình 1.12. Xác định nhiệt dung riêng từ hệ số góc của đồ thị"),
    ("box", "CÁC NGUỒN SAI SỐ VÀ CÁCH KHẮC PHỤC",
     "• Hao phí nhiệt ra môi trường → kết quả đo c LỚN HƠN giá trị thực (vì phải tốn thêm "
     "nhiệt lượng cho cùng một ΔT). Khắc phục: dùng vỏ cách nhiệt, làm thí nghiệm nhanh, "
     "chọn nhiệt độ đầu thấp hơn nhiệt độ phòng và nhiệt độ cuối cao hơn nhiệt độ phòng "
     "một lượng bằng nhau để bù trừ.\n"
     "• Nhiệt lượng làm nóng bình, que khuấy và nhiệt kế → cũng làm c đo được lớn hơn thực tế. "
     "Khắc phục: tính thêm nhiệt dung của bình.\n"
     "• Nhiệt độ phân bố không đều trong chất lỏng → khuấy đều trước khi đọc nhiệt kế.\n"
     "• Đọc nhiệt kế sai do khúc xạ → đặt mắt ngang mực chất lỏng trong nhiệt kế."),

    # =============================================================== §5
    ("h2", "§5. NHIỆT NÓNG CHẢY RIÊNG VÀ NHIỆT HOÁ HƠI RIÊNG"),

    ("h3", "5.1. Hai định nghĩa và hai công thức"),
    ("p", "Nhiệt nóng chảy riêng λ của một chất là nhiệt lượng cần cung cấp để làm nóng chảy "
          "hoàn toàn 1 kg chất đó ở nhiệt độ nóng chảy."),
    ("f", "Q = λ·m        [λ] = J/kg"),
    ("p", "Nhiệt hoá hơi riêng L của một chất lỏng là nhiệt lượng cần cung cấp để làm cho 1 kg "
          "chất lỏng đó hoá hơi hoàn toàn ở nhiệt độ sôi."),
    ("f", "Q = L·m        [L] = J/kg"),
    ("tbl", "Bảng 1.5. Một số giá trị cần nhớ (dùng cho ước lượng nhanh)",
     ["Chất", "Nhiệt độ nóng chảy", "λ (J/kg)", "Nhiệt độ sôi", "L (J/kg)"],
     [["Nước", "0 °C", "3,34·10⁵", "100 °C", "2,26·10⁶"],
      ["Rượu etylic", "−114 °C", "1,08·10⁵", "78 °C", "0,86·10⁶"],
      ["Nhôm", "660 °C", "3,90·10⁵", "2519 °C", "1,05·10⁷"],
      ["Đồng", "1083 °C", "1,80·10⁵", "2562 °C", "4,73·10⁶"],
      ["Chì", "327 °C", "0,25·10⁵", "1749 °C", "8,60·10⁵"]]),
    ("box", "VÌ SAO L LỚN HƠN λ RẤT NHIỀU?",
     "Với nước, L/λ ≈ 2,26·10⁶ / 3,34·10⁵ ≈ 6,8 lần.\n"
     "Giải thích vi mô: khi nóng chảy, các phân tử chỉ cần thoát khỏi vị trí cố định trong mạng "
     "tinh thể nhưng VẪN nằm sát nhau, liên kết chỉ bị nới lỏng. Khi hoá hơi, phân tử phải "
     "thoát HẲN ra khỏi vùng ảnh hưởng của các phân tử khác, tức là phá vỡ hoàn toàn liên kết, "
     "đồng thời còn phải sinh công đẩy khí quyển để chiếm chỗ. Vì thế L ≫ λ.\n"
     "Hệ quả trên đồ thị: đoạn nằm ngang ứng với sự sôi dài hơn hẳn đoạn nằm ngang ứng với sự "
     "nóng chảy khi cung cấp nhiệt đều."),

    ("h3", "5.2. Bài toán nhiều giai đoạn – kĩ năng xương sống của chương"),
    ("fig", "h04_do_thi_dun_nuoc_da",
     "Hình 1.13. Đồ thị nhiệt độ – thời gian khi đun nước đá từ −20 °C thành hơi"),
    ("p", "Đây là hình vẽ trung tâm của Chương I. Mọi bài toán nhiều giai đoạn đều được giải "
          "bằng cách chia quá trình thành các chặng và cộng nhiệt lượng."),
    ("box", "QUY TRÌNH BỐN BƯỚC CHO BÀI TOÁN NHIỀU GIAI ĐOẠN",
     "Bước 1. Vẽ phác đồ thị nhiệt độ – thời gian, đánh dấu các mốc chuyển thể "
     "(0 °C và 100 °C với nước).\n"
     "Bước 2. Chia thành các chặng: chặng thay đổi nhiệt độ dùng Q = mcΔT; chặng chuyển thể "
     "dùng Q = λm hoặc Q = Lm.\n"
     "Bước 3. Chú ý đổi nhiệt dung riêng theo từng thể: nước đá c = 2100, nước lỏng c = 4200, "
     "hơi nước c ≈ 2010 J/(kg·K). Dùng nhầm c là lỗi phổ biến nhất.\n"
     "Bước 4. Cộng tất cả: Q_tổng = ΣQ_i."),
    ("p", "Ví dụ mẫu. Tính nhiệt lượng cần để biến 0,50 kg nước đá ở −20 °C thành hơi nước "
          "ở 100 °C."),
    ("b", "Chặng 1 (đá −20 → 0 °C): Q₁ = 0,50·2100·20 = 21 000 J = 21,0 kJ"),
    ("b", "Chặng 2 (đá tan ở 0 °C): Q₂ = 0,50·3,34·10⁵ = 167 000 J = 167,0 kJ"),
    ("b", "Chặng 3 (nước 0 → 100 °C): Q₃ = 0,50·4200·100 = 210 000 J = 210,0 kJ"),
    ("b", "Chặng 4 (nước sôi thành hơi): Q₄ = 0,50·2,26·10⁶ = 1 130 000 J = 1130,0 kJ"),
    ("b", "Tổng: Q = 21,0 + 167,0 + 210,0 + 1130,0 = 1528,0 kJ ≈ 1,53 MJ"),
    ("p", "Nhận xét sư phạm rất đáng nói với học sinh: riêng chặng hoá hơi đã chiếm khoảng 74 % "
          "tổng nhiệt lượng. Đó là lí do vì sao đun sôi một ấm nước thì nhanh, nhưng đun cho "
          "cạn hẳn thì rất lâu."),

    ("h3", "5.3. Thí nghiệm đo nhiệt nóng chảy riêng"),
    ("fig", "h11_do_nhiet_nong_chay", "Hình 1.14. Bộ dụng cụ đo nhiệt nóng chảy riêng của nước đá"),
    ("p", "Điểm tinh tế của thí nghiệm này: phải bắt đầu đo khi nước đá ĐÃ ở 0 °C và đang tan, "
          "để toàn bộ nhiệt lượng cung cấp chỉ dùng cho việc nóng chảy. Nếu đá còn ở nhiệt độ "
          "âm thì một phần nhiệt lượng bị dùng để làm nóng đá và kết quả λ đo được sẽ lớn hơn "
          "giá trị thực."),
    ("p", "Một cải tiến thường gặp trong đề thi: làm hai lần đo, một lần có bật điện trở nung "
          "và một lần không bật, trong cùng khoảng thời gian. Hiệu khối lượng nước tan giữa hai "
          "lần chính là phần do điện trở gây ra, nhờ đó loại trừ được ảnh hưởng của nhiệt "
          "từ môi trường."),

    ("h3", "5.4. Đọc đồ thị làm nguội"),
    ("fig", "h14_do_thi_lam_nguoi", "Hình 1.15. Đồ thị làm nguội của một chất lỏng"),
    ("p", "Kĩ năng đọc đồ thị cần rèn: (1) đoạn nằm ngang cho biết nhiệt độ chuyển thể; "
          "(2) độ dài đoạn nằm ngang tỉ lệ với λm hoặc Lm; (3) độ dốc của các đoạn nghiêng tỉ lệ "
          "nghịch với tích m·c, nên đoạn nào dốc hơn thì chất ở thể đó có nhiệt dung riêng nhỏ hơn."),
    ("exam",
     "Một câu hỏi rất hay để phân loại học sinh giỏi: trên đồ thị đun nóng, đoạn ứng với thể "
     "rắn dốc hơn đoạn ứng với thể lỏng. Hỏi so sánh c_rắn và c_lỏng.\n"
     "Trả lời: cùng một công suất cấp nhiệt, độ dốc dT/dt = P/(mc). Đoạn dốc hơn ứng với mc "
     "nhỏ hơn; khối lượng không đổi nên c_rắn < c_lỏng. Với nước đúng là 2100 < 4200."),

    # =============================================================== §6
    ("h2", "§6. TỔNG KẾT CHƯƠNG I"),
    ("tbl", "Bảng 1.6. Hệ thống công thức Chương I",
     ["Nội dung", "Công thức", "Điều kiện áp dụng"],
     [["Định luật I NĐLH", "ΔU = A + Q", "Mọi hệ; A, Q là đại lượng hệ NHẬN"],
      ["Đẳng tích", "ΔU = Q", "A = 0"],
      ["Đoạn nhiệt", "ΔU = A", "Q = 0, hệ cách nhiệt hoặc quá trình rất nhanh"],
      ["Đẳng nhiệt của khí lí tưởng", "Q = −A", "ΔU = 0 vì U chỉ phụ thuộc T"],
      ["Đổi thang nhiệt độ", "T(K) = t(°C) + 273,15", "Đổi GIÁ TRỊ nhiệt độ"],
      ["Đổi độ biến thiên", "ΔT(K) = Δt(°C)", "Đổi ĐỘ BIẾN THIÊN, không cộng 273"],
      ["Nhiệt lượng làm đổi nhiệt độ", "Q = m·c·ΔT", "Vật KHÔNG chuyển thể"],
      ["Nhiệt nóng chảy", "Q = λ·m", "Vật ở đúng nhiệt độ nóng chảy"],
      ["Nhiệt hoá hơi", "Q = L·m", "Chất lỏng ở đúng nhiệt độ sôi"],
      ["Cân bằng nhiệt", "Q_toả = Q_thu  hay  ΣQ = 0", "Hệ cách nhiệt, chỉ trao đổi nhiệt trong hệ"],
      ["Nhiệt độ cân bằng hai vật", "t = (m₁c₁t₁+m₂c₂t₂)/(m₁c₁+m₂c₂)", "Không có chuyển thể"],
      ["Nhiệt lượng từ điện", "Q = P·t = U·I·t", "Bỏ qua hao phí ra môi trường"]]),
    ("box", "MƯỜI LỖI SAI THƯỜNG GẶP NHẤT CỦA CHƯƠNG I",
     "1. Dùng sai quy ước dấu của A trong ΔU = A + Q (khí dãn nở thì A < 0).\n"
     "2. Cộng 273 vào ĐỘ BIẾN THIÊN nhiệt độ.\n"
     "3. Dùng c của nước lỏng cho nước đá hoặc cho hơi nước.\n"
     "4. Quên giai đoạn chuyển thể trong bài toán nhiều chặng.\n"
     "5. Không kiểm tra xem nước đá có tan hết hay không.\n"
     "6. Nhầm “nhiệt lượng” là một đại lượng mà vật “chứa”.\n"
     "7. Cho rằng khi đang nóng chảy thì nội năng không đổi (nhiệt độ không đổi, "
     "nhưng nội năng VẪN tăng).\n"
     "8. Cho rằng nhiệt truyền theo chiều nội năng lớn → nội năng nhỏ.\n"
     "9. Quên nhiệt lượng kế trong phương trình cân bằng nhiệt.\n"
     "10. Đổi đơn vị sai: khối lượng để nguyên gam, thể tích nước không đổi ra khối lượng "
     "(1 lít nước = 1 kg)."),
    ("exam",
     "Định hướng ôn tập Chương I theo định dạng đề thi tốt nghiệp THPT:\n"
     "• Phần trắc nghiệm nhiều lựa chọn thường hỏi: phân biệt ba thể, phân biệt bay hơi–sôi, "
     "quy ước dấu định luật I, ý nghĩa của c lớn, đổi thang nhiệt độ.\n"
     "• Phần đúng/sai thường xây quanh một thí nghiệm (đo c, đo λ) hoặc một đồ thị nhiệt độ – "
     "thời gian, với bốn ý trải đều từ nhận biết tới vận dụng.\n"
     "• Phần trả lời ngắn thường là bài toán cân bằng nhiệt hoặc bài toán nhiều giai đoạn, "
     "yêu cầu làm tròn tới một hoặc hai chữ số thập phân. Hãy tập thói quen ghi rõ đơn vị "
     "trung gian để không sai bậc mười."),
]
