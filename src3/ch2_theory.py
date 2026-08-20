# -*- coding: utf-8 -*-
"""Tài liệu dạy học Chương II - KHÍ LÍ TƯỞNG (Vật lí 12, GDPT 2018)."""

CH2 = [
    ("h1", "CHƯƠNG II – KHÍ LÍ TƯỞNG"),
    ("p", "Chương II là chương có mật độ bài tập định lượng cao nhất của học kì I. "
          "Toàn chương xoay quanh một câu hỏi: khi một lượng khí xác định chuyển từ trạng thái "
          "này sang trạng thái khác, ba đại lượng p, V, T liên hệ với nhau như thế nào? "
          "Câu trả lời được xây dựng theo hai con đường song song — con đường thực nghiệm "
          "(ba định luật chất khí) và con đường lí thuyết (mô hình động học phân tử)."),
    ("box", "PHẠM VI CHƯƠNG II THEO CHƯƠNG TRÌNH GDPT 2018",
     "Bài 8. Mô hình động học phân tử chất khí\n"
     "Bài 9. Định luật Boyle\n"
     "Bài 10. Định luật Charles\n"
     "Bài 11. Phương trình trạng thái của khí lí tưởng\n"
     "Bài 12. Áp suất khí theo mô hình động học phân tử. Quan hệ giữa động năng phân tử "
     "và nhiệt độ\n"
     "Bài 13. Bài tập về khí lí tưởng"),

    # =============================================================== §1
    ("h2", "§1. MÔ HÌNH ĐỘNG HỌC PHÂN TỬ CHẤT KHÍ"),

    ("h3", "1.1. Chuyển động Brown – bằng chứng thực nghiệm"),
    ("fig", "h15_chuyen_dong_brown", "Hình 2.1. Quỹ đạo gấp khúc của hạt trong chuyển động Brown"),
    ("p", "Năm 1827, Robert Brown quan sát các hạt phấn hoa lơ lửng trong nước và thấy chúng "
          "chuyển động hỗn loạn không ngừng. Giải thích: các phân tử nước chuyển động nhiệt "
          "va chạm vào hạt phấn hoa từ mọi phía; do số va chạm ở các phía không cân bằng nhau "
          "tại mỗi thời điểm nên hạt bị đẩy theo những hướng ngẫu nhiên."),
    ("b", "Nhiệt độ càng cao → phân tử chuyển động càng nhanh → chuyển động Brown càng mạnh."),
    ("b", "Hạt càng nhỏ → sự mất cân bằng tương đối càng lớn → chuyển động Brown càng rõ. "
          "Hạt lớn thì các va chạm bù trừ nhau nên gần như đứng yên."),
    ("trap",
     "Sai lầm thường gặp: nói rằng “hạt phấn hoa tự chuyển động” hoặc “hạt phấn hoa chuyển động "
     "vì nó sống”. Chính Brown đã bác bỏ giả thuyết này bằng cách lặp lại thí nghiệm với bột "
     "khoáng vô cơ và vẫn thấy hiện tượng. Nguyên nhân duy nhất là va chạm của các phân tử "
     "môi trường."),

    ("h3", "1.2. Các giả thuyết của thuyết động học phân tử chất khí"),
    ("b", "Chất khí gồm rất nhiều phân tử; kích thước của mỗi phân tử rất nhỏ so với khoảng "
          "cách trung bình giữa chúng, nên có thể coi phân tử là chất điểm."),
    ("b", "Các phân tử chuyển động hỗn loạn không ngừng theo mọi phương với mọi tốc độ."),
    ("b", "Khi chưa va chạm, lực tương tác giữa các phân tử là không đáng kể; phân tử chuyển "
          "động thẳng đều."),
    ("b", "Các phân tử va chạm đàn hồi với nhau và với thành bình; động năng được bảo toàn "
          "trong va chạm."),
    ("box", "KHÍ LÍ TƯỞNG LÀ GÌ?",
     "Khí lí tưởng là chất khí mà các phân tử được coi là chất điểm và chỉ tương tác với nhau "
     "khi va chạm.\n\n"
     "Điều kiện để một khí thực gần đúng là khí lí tưởng: áp suất KHÔNG quá cao và nhiệt độ "
     "KHÔNG quá thấp (xa nhiệt độ hoá lỏng).\n"
     "• Áp suất cao → khoảng cách phân tử giảm → không bỏ qua được thể tích riêng và lực hút.\n"
     "• Nhiệt độ thấp → động năng nhỏ → lực hút giữ được phân tử lại → khí sắp hoá lỏng.\n"
     "Ở điều kiện thường, không khí, oxygen, nitrogen, helium đều gần đúng là khí lí tưởng."),

    ("h3", "1.3. Ba thông số trạng thái"),
    ("tbl", "Bảng 2.1. Ba thông số trạng thái của một lượng khí",
     ["Thông số", "Kí hiệu", "Đơn vị SI", "Đơn vị khác thường gặp"],
     [["Áp suất", "p", "Pa (N/m²)", "1 atm = 1,013·10⁵ Pa; 1 atm = 76 cmHg; 1 bar = 10⁵ Pa"],
      ["Thể tích", "V", "m³", "1 L = 1 dm³ = 10⁻³ m³; 1 mL = 1 cm³ = 10⁻⁶ m³"],
      ["Nhiệt độ tuyệt đối", "T", "K", "T = t(°C) + 273"]]),
    ("exam",
     "Nguyên tắc đổi đơn vị an toàn trong Chương II:\n"
     "• Trong các định luật dạng tỉ số (p₁V₁ = p₂V₂, V₁/T₁ = V₂/T₂, p₁V₁/T₁ = p₂V₂/T₂), "
     "p và V CHỈ CẦN cùng đơn vị ở hai vế, không nhất thiết phải là SI. Có thể để nguyên atm "
     "và lít, tính rất nhanh.\n"
     "• Nhưng T thì LUÔN LUÔN phải là Kelvin, không có ngoại lệ.\n"
     "• Trong phương trình pV = nRT với R = 8,31 J/(mol·K) thì BẮT BUỘC p tính bằng Pa, "
     "V bằng m³, T bằng K."),

    # =============================================================== §2
    ("h2", "§2. ĐỊNH LUẬT BOYLE – QUÁ TRÌNH ĐẲNG NHIỆT"),

    ("h3", "2.1. Phát biểu và biểu thức"),
    ("p", "Ở nhiệt độ không đổi, tích của áp suất và thể tích của một lượng khí xác định "
          "là hằng số."),
    ("f", "p·V = hằng số      ⟺      p₁V₁ = p₂V₂      (khi T và lượng khí không đổi)"),
    ("p", "Cách phát biểu tương đương: khi nhiệt độ không đổi, áp suất tỉ lệ nghịch với thể tích."),
    ("fig", "h17_thi_nghiem_boyle", "Hình 2.2. Bộ thí nghiệm khảo sát định luật Boyle"),
    ("box", "GIẢI THÍCH BẰNG MÔ HÌNH ĐỘNG HỌC PHÂN TỬ",
     "Giữ nhiệt độ không đổi → tốc độ trung bình của phân tử không đổi → mỗi va chạm truyền "
     "cùng một xung lượng cho thành bình.\n"
     "Nén khí (V giảm) → mật độ phân tử tăng → SỐ va chạm lên một đơn vị diện tích thành bình "
     "trong một đơn vị thời gian tăng → áp suất tăng.\n"
     "Điểm cần nhấn mạnh: khi nén đẳng nhiệt, áp suất tăng KHÔNG phải vì phân tử chuyển động "
     "nhanh hơn (tốc độ không đổi), mà vì va chạm xảy ra DÀY hơn."),

    ("h3", "2.2. Đồ thị và kĩ thuật tuyến tính hoá"),
    ("fig", "h18_do_thi_boyle", "Hình 2.3. Đường đẳng nhiệt trong hệ (p,V) và trong hệ (p, 1/V)"),
    ("p", "Trong hệ toạ độ (p, V), đường đẳng nhiệt là một nhánh hypebol. Đường đẳng nhiệt ứng "
          "với nhiệt độ cao hơn nằm XA gốc toạ độ hơn — đây là một câu hỏi rất hay gặp."),
    ("p", "Trong hệ toạ độ (p, 1/V), đường đẳng nhiệt trở thành đường THẲNG đi qua gốc toạ độ, "
          "vì p = (hằng số)·(1/V). Kĩ thuật biến một quan hệ cong thành đường thẳng gọi là "
          "tuyến tính hoá, và là phương pháp chuẩn khi xử lí số liệu thực nghiệm."),
    ("fig", "h30_do_thi_boyle_thuc_nghiem",
     "Hình 2.4. Vì sao phải tuyến tính hoá khi xử lí số liệu thí nghiệm"),
    ("exam",
     "Câu hỏi thí nghiệm mẫu: “Vì sao khi kiểm chứng định luật Boyle, người ta vẽ đồ thị p theo "
     "1/V chứ không vẽ p theo V?”\n"
     "Trả lời chuẩn: mắt người rất khó phân biệt một hypebol thật với một đường cong gần giống "
     "nó, nhưng lại phân biệt rất tốt đường thẳng với đường cong. Vẽ p theo 1/V, nếu các điểm "
     "thực nghiệm nằm trên một đường thẳng ĐI QUA GỐC TOẠ ĐỘ thì định luật được nghiệm đúng; "
     "hệ số góc của đường thẳng chính là hằng số pV."),

    ("h3", "2.3. Điều kiện áp dụng – nơi ra bẫy nhiều nhất"),
    ("trap",
     "Định luật Boyle chỉ đúng khi đồng thời thoả mãn:\n"
     "• Nhiệt độ KHÔNG đổi. Nén nhanh một chất khí là quá trình gần đoạn nhiệt chứ không phải "
     "đẳng nhiệt — khí nóng lên, và pV không còn là hằng số. Muốn đẳng nhiệt thì phải nén CHẬM.\n"
     "• LƯỢNG KHÍ không đổi. Nếu bơm thêm khí vào hoặc khí rò rỉ ra ngoài thì không dùng được. "
     "Bài toán bơm xe đạp phải xử lí bằng cách coi tổng lượng khí bơm vào là một khối khí ban đầu.\n"
     "• Khí gần đúng là khí lí tưởng."),

    # =============================================================== §3
    ("h2", "§3. ĐỊNH LUẬT CHARLES – QUÁ TRÌNH ĐẲNG ÁP"),

    ("h3", "3.1. Phát biểu và biểu thức"),
    ("p", "Khi áp suất của một lượng khí xác định không đổi, thể tích của khí tỉ lệ thuận với "
          "nhiệt độ tuyệt đối của nó."),
    ("f", "V / T = hằng số      ⟺      V₁/T₁ = V₂/T₂      (khi p và lượng khí không đổi)"),
    ("fig", "h19_thi_nghiem_charles", "Hình 2.5. Bộ thí nghiệm minh hoạ định luật Charles"),
    ("p", "Chi tiết quan trọng trong thiết kế thí nghiệm: giọt thuỷ ngân (hoặc pit-tông nhẹ) "
          "có thể di chuyển tự do, nhờ đó áp suất của khí luôn cân bằng với áp suất khí quyển "
          "cộng trọng lượng giọt — tức là KHÔNG ĐỔI. Nếu bịt kín ống thì thí nghiệm trở thành "
          "đẳng tích chứ không còn là đẳng áp."),

    ("h3", "3.2. Đồ thị – cái bẫy về gốc toạ độ"),
    ("fig", "h20_do_thi_charles", "Hình 2.6. Đồ thị đẳng áp trong hệ (V,T) và trong hệ (V,t)"),
    ("box", "PHÂN BIỆT HAI ĐỒ THỊ – RẤT HAY BỊ HỎI",
     "• Trong hệ (V, T) với T tính bằng KELVIN: đường đẳng áp là đường thẳng ĐI QUA gốc toạ độ. "
     "Đây là biểu hiện của quan hệ tỉ lệ THUẬN.\n"
     "• Trong hệ (V, t) với t tính bằng °C: vẫn là đường thẳng nhưng KHÔNG đi qua gốc toạ độ. "
     "Nó cắt trục tung tại V₀ (thể tích ở 0 °C) và nếu kéo dài về phía trái sẽ cắt trục hoành "
     "tại t = −273,15 °C.\n"
     "Phần kéo dài đó chỉ có ý nghĩa NGOẠI SUY: trên thực tế khí đã hoá lỏng từ lâu trước khi "
     "đạt tới nhiệt độ đó. Chính phép ngoại suy này đã dẫn tới khái niệm độ không tuyệt đối."),
    ("trap",
     "Bẫy số học kinh điển: “Nung nóng đẳng áp một lượng khí từ 27 °C lên 54 °C thì thể tích "
     "tăng gấp đôi.” — SAI. Phải đổi ra Kelvin: 300 K → 327 K, thể tích chỉ tăng 9 %. "
     "Muốn thể tích tăng gấp đôi thì nhiệt độ tuyệt đối phải tăng gấp đôi, tức là từ 300 K lên "
     "600 K, tương ứng từ 27 °C lên 327 °C."),

    ("h3", "3.3. Quá trình đẳng tích"),
    ("p", "Tuy chương trình không tách thành một bài riêng, quá trình đẳng tích được suy ra trực "
          "tiếp từ phương trình trạng thái và xuất hiện thường xuyên trong đề thi:"),
    ("f", "p / T = hằng số      ⟺      p₁/T₁ = p₂/T₂      (khi V và lượng khí không đổi)"),
    ("fig", "h26_do_thi_p_T_dang_tich", "Hình 2.7. Đường đẳng tích trong hệ (p, T)"),
    ("p", "Giải thích vi mô: giữ thể tích không đổi, tăng nhiệt độ làm phân tử chuyển động nhanh "
          "hơn. Mỗi va chạm truyền xung lượng lớn hơn, đồng thời số va chạm trong một đơn vị thời "
          "gian cũng tăng. Cả hai hiệu ứng đều làm áp suất tăng."),
    ("exam",
     "Ứng dụng thực tế hay được đưa vào đề dưới dạng bối cảnh:\n"
     "• Không được ném bình xịt, bật lửa ga vào lửa: thể tích bình không đổi, nhiệt độ tăng "
     "làm áp suất tăng vọt tới mức gây nổ.\n"
     "• Lốp xe căng hơn sau khi chạy đường dài: ma sát làm nhiệt độ khí trong lốp tăng, "
     "thể tích gần như không đổi nên áp suất tăng.\n"
     "• Nồi áp suất có van an toàn để giới hạn áp suất khi nhiệt độ tăng cao."),

    # =============================================================== §4
    ("h2", "§4. PHƯƠNG TRÌNH TRẠNG THÁI CỦA KHÍ LÍ TƯỞNG"),

    ("h3", "4.1. Phương trình trạng thái"),
    ("p", "Kết hợp định luật Boyle và định luật Charles bằng cách cho lượng khí đi qua một "
          "trạng thái trung gian, ta thu được:"),
    ("f", "p·V / T = hằng số      ⟺      p₁V₁/T₁ = p₂V₂/T₂"),
    ("p", "Đây là phương trình trạng thái của khí lí tưởng, áp dụng cho một LƯỢNG KHÍ XÁC ĐỊNH "
          "chuyển từ trạng thái 1 sang trạng thái 2 theo bất kì cách nào."),
    ("box", "BA ĐẲNG QUÁ TRÌNH LÀ TRƯỜNG HỢP RIÊNG",
     "Từ p₁V₁/T₁ = p₂V₂/T₂:\n"
     "• Cho T₁ = T₂ → p₁V₁ = p₂V₂ (định luật Boyle)\n"
     "• Cho p₁ = p₂ → V₁/T₁ = V₂/T₂ (định luật Charles)\n"
     "• Cho V₁ = V₂ → p₁/T₁ = p₂/T₂ (quá trình đẳng tích)\n"
     "Lời khuyên: chỉ cần thuộc phương trình trạng thái, ba định luật kia tự suy ra. "
     "Điều này giúp tránh nhầm lẫn giữa chúng."),

    ("h3", "4.2. Phương trình Clapeyron – Mendeleev"),
    ("f", "p·V = n·R·T = (m/M)·R·T = N·k_B·T"),
    ("tbl", "Bảng 2.2. Các hằng số cần nhớ",
     ["Hằng số", "Giá trị", "Ý nghĩa"],
     [["R", "8,31 J/(mol·K)", "Hằng số khí lí tưởng"],
      ["N_A", "6,02·10²³ mol⁻¹", "Số Avogadro – số phân tử trong 1 mol"],
      ["k_B", "1,38·10⁻²³ J/K", "Hằng số Boltzmann, k_B = R/N_A"],
      ["V_mol ở đktc", "22,4 L/mol", "Thể tích 1 mol khí ở 0 °C, 1 atm"]]),
    ("p", "Điểm khác biệt cốt lõi: phương trình pV/T = hằng số chỉ dùng khi LƯỢNG KHÍ KHÔNG ĐỔI. "
          "Còn pV = nRT dùng được cả khi lượng khí thay đổi, vì n xuất hiện tường minh. "
          "Bài toán “bơm khí vào bình”, “khí rò rỉ khỏi bình” bắt buộc phải dùng pV = nRT."),
    ("exam",
     "Kĩ thuật giải nhanh bài toán rò rỉ khí: bình kín thể tích V, nhiệt độ T không đổi. "
     "Vì V và T không đổi nên p tỉ lệ thuận với n. Do đó:\n"
     "n₂/n₁ = p₂/p₁, và phần trăm khí đã thoát ra bằng (p₁ − p₂)/p₁ · 100 %.\n"
     "Không cần biết V, T hay bản chất khí."),

    ("h3", "4.3. Ba đẳng quá trình trong ba hệ toạ độ"),
    ("p", "Bảng hình dưới đây là công cụ tra cứu bắt buộc phải thuộc. Rất nhiều câu hỏi trắc "
          "nghiệm chỉ cần nhìn dạng đồ thị là chọn được đáp án."),
    ("fig", "h21_ba_dang_qua_trinh",
     "Hình 2.8. Dạng đồ thị của ba đẳng quá trình trong ba hệ toạ độ"),
    ("box", "MẸO NHỚ BẢNG ĐỒ THỊ",
     "Quy tắc 1: Nếu trục hoành hoặc trục tung chính là đại lượng được GIỮ KHÔNG ĐỔI, "
     "đường biểu diễn phải vuông góc với trục đó (nằm ngang hoặc thẳng đứng).\n"
     "Quy tắc 2: Trong hệ có trục T, quan hệ p–T (đẳng tích) và V–T (đẳng áp) đều là tỉ lệ "
     "thuận, nên là đường thẳng QUA GỐC toạ độ.\n"
     "Quy tắc 3: Chỉ có duy nhất một đường cong trong cả bảng — hypebol của đẳng nhiệt "
     "trong hệ (p, V)."),
    ("fig", "h22_chu_trinh_pV", "Hình 2.9. Một chu trình ba giai đoạn trên giản đồ (p, V)"),
    ("exam",
     "Dạng bài chuyển hệ toạ độ: cho chu trình trong hệ (p,V), yêu cầu vẽ lại trong hệ (V,T) "
     "hoặc (p,T). Quy trình bốn bước:\n"
     "1. Lập bảng ba thông số p, V, T cho từng đỉnh, dùng pV/T = const để tìm giá trị còn thiếu.\n"
     "2. Xác định loại của từng đoạn (đẳng nhiệt / đẳng tích / đẳng áp).\n"
     "3. Chấm các đỉnh lên hệ toạ độ mới.\n"
     "4. Nối bằng đúng dạng đường theo bảng Hình 2.8, và ĐÁNH MŨI TÊN chỉ chiều diễn biến. "
     "Việc quên mũi tên là lỗi mất điểm phổ biến trong phần tự luận."),

    ("h3", "4.4. Bài toán pit-tông – hai phương trình cho hai ẩn"),
    ("fig", "h27_pit_tong_hai_ngan", "Hình 2.10. Xilanh chia hai ngăn bởi pit-tông di động"),
    ("box", "CHÌA KHOÁ CỦA MỌI BÀI TOÁN PIT-TÔNG",
     "Bài toán pit-tông luôn có hai ẩn, nên cần hai phương trình:\n"
     "• Phương trình ĐỘNG LỰC HỌC: điều kiện cân bằng của pit-tông cho biết quan hệ giữa "
     "áp suất hai bên. Nếu pit-tông nhẹ, không ma sát, nằm ngang thì p_A = p_B. Nếu pit-tông "
     "có khối lượng và đặt thẳng đứng thì p_dưới = p_trên + mg/S.\n"
     "• Phương trình HÌNH HỌC: tổng thể tích (hoặc tổng chiều dài cột khí) không đổi, "
     "V_A + V_B = const. Nếu pit-tông dịch một đoạn x thì V_A tăng S·x và V_B giảm S·x.\n"
     "Sau đó áp dụng phương trình trạng thái cho từng ngăn riêng biệt."),
    ("fig", "h24_ong_chu_U", "Hình 2.11. Cột khí bị nhốt bởi thuỷ ngân trong ống thẳng đứng"),
    ("p", "Với bài toán cột thuỷ ngân, quy tắc dấu rất đơn giản nhưng hay nhầm: cột thuỷ ngân "
          "nằm PHÍA TRÊN khí thì đè xuống, áp suất khí bằng p₀ + h; cột thuỷ ngân nằm PHÍA DƯỚI "
          "khí (miệng ống quay xuống) thì kéo xuống, áp suất khí bằng p₀ − h. "
          "Khi ống nằm ngang, cột thuỷ ngân không gây thêm áp suất nên p = p₀."),
    ("trap",
     "Bẫy hay gặp với ống thuỷ ngân: đề hỏi “khi lật ngược ống thì cột khí dài bao nhiêu” và "
     "học sinh quên rằng chiều dài cột thuỷ ngân KHÔNG đổi, chỉ có cột khí thay đổi. "
     "Nếu ống quá ngắn thì thuỷ ngân có thể tràn ra ngoài — khi đó lượng thuỷ ngân giảm và "
     "bài toán phải xử lí khác. Luôn kiểm tra tổng chiều dài."),

    # =============================================================== §5
    ("h2", "§5. ÁP SUẤT KHÍ THEO MÔ HÌNH ĐỘNG HỌC PHÂN TỬ"),

    ("h3", "5.1. Nguồn gốc vi mô của áp suất"),
    ("fig", "h16_mo_hinh_dong_hoc", "Hình 2.12. Va chạm phân tử với thành bình sinh ra áp suất"),
    ("p", "Mỗi phân tử va chạm đàn hồi với thành bình sẽ đổi chiều thành phần vận tốc vuông góc "
          "với thành, do đó truyền cho thành một xung lượng 2mv. Áp suất chính là tổng hợp thống "
          "kê của vô số va chạm như vậy."),
    ("f", "p·V = (1/3)·N·m·v̄²      hay      p = (1/3)·ρ·v̄²"),
    ("p", "Trong đó N là số phân tử, m là khối lượng một phân tử, v̄² là trung bình của bình "
          "phương tốc độ, ρ = Nm/V là khối lượng riêng của khí."),
    ("box", "BA YẾU TỐ QUYẾT ĐỊNH ÁP SUẤT KHÍ",
     "Từ p = (1/3)·(N/V)·m·v̄², áp suất tăng khi:\n"
     "• Mật độ phân tử N/V tăng (nhiều phân tử hơn trong cùng thể tích, hoặc nén khí lại).\n"
     "• Khối lượng phân tử m lớn (mỗi va chạm truyền xung lượng lớn hơn).\n"
     "• Tốc độ phân tử lớn, tức nhiệt độ cao.\n"
     "Lưu ý hệ số 1/3 xuất phát từ tính đẳng hướng: chuyển động hỗn loạn chia đều cho ba "
     "phương x, y, z."),

    ("h3", "5.2. Tốc độ căn quân phương"),
    ("f", "v_rms = √(v̄²)"),
    ("p", "Tốc độ căn quân phương là căn bậc hai của trung bình bình phương tốc độ. Đây KHÔNG "
          "phải là tốc độ trung bình theo nghĩa số học thông thường, mà là đại lượng gắn trực "
          "tiếp với động năng trung bình của phân tử."),
    ("fig", "h23_phan_bo_toc_do", "Hình 2.13. Phân bố tốc độ phân tử ở hai nhiệt độ khác nhau"),
    ("p", "Đồ thị phân bố cho thấy: ở một nhiệt độ xác định, các phân tử KHÔNG chuyển động cùng "
          "một tốc độ mà trải trên một dải rộng. Khi nhiệt độ tăng, đỉnh của đường phân bố dịch "
          "về phía tốc độ lớn và đường phân bố trở nên thấp, rộng hơn."),

    ("h3", "5.3. Quan hệ giữa động năng phân tử và nhiệt độ"),
    ("p", "So sánh hai biểu thức pV = (1/3)Nm v̄² và pV = N·k_B·T, ta rút ra kết quả trung tâm "
          "của Chương II:"),
    ("f", "W̄_đ = (1/2)·m·v̄² = (3/2)·k_B·T"),
    ("f", "v_rms = √(3k_B·T/m) = √(3RT/M)"),
    ("box", "Ý NGHĨA CỦA CÔNG THỨC W̄ = (3/2)k_B·T",
     "Đây chính là ĐỊNH NGHĨA VI MÔ CỦA NHIỆT ĐỘ: nhiệt độ tuyệt đối là thước đo trực tiếp của "
     "động năng tịnh tiến trung bình của phân tử.\n\n"
     "Ba hệ quả quan trọng:\n"
     "• Động năng trung bình chỉ phụ thuộc NHIỆT ĐỘ, không phụ thuộc loại khí. Ở cùng nhiệt độ, "
     "một phân tử hydrogen và một phân tử oxygen có động năng trung bình BẰNG NHAU.\n"
     "• Nhưng tốc độ thì khác nhau: v_rms ∝ 1/√M. Phân tử nhẹ chuyển động nhanh hơn. "
     "Đây là lí do khí hydrogen và helium dễ thoát khỏi khí quyển Trái Đất.\n"
     "• Ở 0 K thì W̄ = 0 — độ không tuyệt đối là trạng thái chuyển động nhiệt dừng lại. "
     "Đây là cơ sở vật lí cho việc không thể có nhiệt độ âm trên thang Kelvin."),
    ("trap",
     "Sai lầm 1: cho rằng “nhiệt độ tăng gấp đôi thì tốc độ phân tử tăng gấp đôi”. SAI. "
     "Vì v_rms ∝ √T nên T tăng gấp 4 lần thì v_rms mới tăng gấp đôi.\n"
     "Sai lầm 2: cho rằng ở cùng nhiệt độ thì mọi khí có cùng tốc độ phân tử. SAI — cùng ĐỘNG "
     "NĂNG chứ không cùng tốc độ.\n"
     "Sai lầm 3: dùng công thức với t tính bằng °C. Mọi công thức trong mục này đều bắt buộc "
     "dùng Kelvin."),
    ("p", "Với khí lí tưởng đơn nguyên tử, nội năng bằng tổng động năng tịnh tiến của tất cả "
          "các phân tử:"),
    ("f", "U = N·W̄_đ = (3/2)·N·k_B·T = (3/2)·n·R·T"),
    ("p", "Công thức này khép lại vòng liên hệ giữa Chương I và Chương II: nó chứng minh chặt chẽ "
          "rằng nội năng của khí lí tưởng CHỈ phụ thuộc nhiệt độ, điều đã được sử dụng khi bàn về "
          "quá trình đẳng nhiệt ở Chương I."),

    # =============================================================== §6
    ("h2", "§6. ỨNG DỤNG THỰC TIỄN"),
    ("fig", "h25_bom_xe_va_binh_khi", "Hình 2.14. Hai ứng dụng quen thuộc của định luật chất khí"),
    ("b", "Bơm xe, máy nén khí: nén khí để tăng áp suất; nếu nén nhanh thì khí nóng lên rõ rệt "
          "vì quá trình gần đoạn nhiệt."),
    ("b", "Bình khí nén y tế, bình dưỡng khí thợ lặn: nhờ nén ở áp suất rất cao mà một bình nhỏ "
          "chứa được lượng khí lớn. Bài toán thường gặp: tính thể tích khí ở điều kiện thường "
          "mà bình cung cấp được, và thời gian sử dụng."),
    ("b", "Khinh khí cầu: đốt nóng không khí trong khí cầu ở áp suất không đổi làm thể tích tăng, "
          "khối lượng riêng giảm, lực đẩy Archimedes thắng trọng lực."),
    ("b", "Bóng thám không: khi lên cao, áp suất khí quyển giảm mạnh làm bóng nở ra; đây là lí do "
          "bóng không được bơm căng ngay từ mặt đất."),
    ("b", "Lốp xe, bình xịt, nồi áp suất: các bài toán đẳng tích với cảnh báo an toàn."),

    # =============================================================== §7
    ("h2", "§7. TỔNG KẾT CHƯƠNG II"),
    ("tbl", "Bảng 2.3. Hệ thống công thức Chương II",
     ["Nội dung", "Công thức", "Điều kiện áp dụng"],
     [["Định luật Boyle", "p₁V₁ = p₂V₂", "T và lượng khí không đổi"],
      ["Định luật Charles", "V₁/T₁ = V₂/T₂", "p và lượng khí không đổi"],
      ["Quá trình đẳng tích", "p₁/T₁ = p₂/T₂", "V và lượng khí không đổi"],
      ["Phương trình trạng thái", "p₁V₁/T₁ = p₂V₂/T₂", "Lượng khí không đổi"],
      ["Phương trình Clapeyron–Mendeleev", "pV = nRT = (m/M)RT", "Dùng được cả khi lượng khí đổi"],
      ["Dạng theo số phân tử", "pV = N·k_B·T", "N là số phân tử"],
      ["Áp suất theo mô hình phân tử", "pV = (1/3)N·m·v̄²", "Khí lí tưởng"],
      ["Động năng tịnh tiến trung bình", "W̄ = (3/2)k_B·T", "T tính bằng Kelvin"],
      ["Tốc độ căn quân phương", "v_rms = √(3RT/M)", "M tính bằng kg/mol"],
      ["Nội năng khí lí tưởng đơn nguyên tử", "U = (3/2)nRT", "Chỉ phụ thuộc T"],
      ["Áp suất khí bị nhốt bởi thuỷ ngân", "p = p₀ ± h", "Cộng khi thuỷ ngân ở trên khí"]]),
    ("box", "MƯỜI LỖI SAI THƯỜNG GẶP NHẤT CỦA CHƯƠNG II",
     "1. Quên đổi nhiệt độ sang Kelvin.\n"
     "2. Cộng 273 vào độ biến thiên nhiệt độ.\n"
     "3. Dùng p₁V₁ = p₂V₂ cho quá trình nhiệt độ thay đổi.\n"
     "4. Dùng pV/T = const cho bài toán có bơm thêm hoặc rò rỉ khí.\n"
     "5. Nhầm dạng đồ thị: cho rằng đường đẳng nhiệt trong hệ (p,T) là hypebol "
     "(thực ra là đường thẳng đứng).\n"
     "6. Cho rằng đường đẳng áp trong hệ (V,t °C) đi qua gốc toạ độ.\n"
     "7. Cho rằng nhiệt độ tăng gấp đôi thì tốc độ phân tử tăng gấp đôi.\n"
     "8. Cho rằng cùng nhiệt độ thì mọi khí có cùng tốc độ phân tử.\n"
     "9. Sai dấu khi tính áp suất khí bị nhốt bởi cột thuỷ ngân.\n"
     "10. Trong bài pit-tông, chỉ viết một phương trình trạng thái mà quên ràng buộc "
     "tổng thể tích không đổi."),
    ("exam",
     "Định hướng ôn tập Chương II theo định dạng đề thi tốt nghiệp THPT:\n"
     "• Phần trắc nghiệm nhiều lựa chọn: nhận dạng đồ thị, phát biểu định luật và điều kiện "
     "áp dụng, giải thích vi mô, so sánh tốc độ và động năng phân tử của hai khí.\n"
     "• Phần đúng/sai: thường xây quanh một bối cảnh thực tế (lốp xe, bình khí nén, bóng bay "
     "lên cao) hoặc một đồ thị/bảng số liệu, với bốn ý gồm cả định tính và định lượng.\n"
     "• Phần trả lời ngắn: bài toán hai hoặc ba trạng thái, bài toán pit-tông, bài toán tính "
     "v_rms hoặc số phân tử. Hãy đặc biệt cẩn thận với bậc mười của N (cỡ 10²³) và với đơn vị "
     "khối lượng mol (kg/mol chứ không phải g/mol)."),
]
