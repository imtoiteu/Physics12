# -*- coding: utf-8 -*-
"""Tài liệu dạy học CHƯƠNG III – TỪ TRƯỜNG (Vật lí 12, GDPT 2018)."""

CH3 = [
("h1", "CHƯƠNG III – TỪ TRƯỜNG"),
("p", "Chương III tương ứng với các bài 14 – 20 của sách giáo khoa Vật lí 12 (bộ Kết nối tri thức "
      "với cuộc sống) và với chủ đề “Từ trường” trong Chương trình GDPT 2018. Đây là chương có mật độ "
      "câu hỏi lớn trong đề thi tốt nghiệp THPT, đặc biệt ở dạng câu hỏi đúng/sai gắn với thí nghiệm và "
      "đồ thị. Toàn chương xoay quanh một trục logic duy nhất: "
      "dòng điện (hoặc nam châm) sinh ra từ trường → từ trường tác dụng lực lên dòng điện → "
      "từ trường biến thiên sinh ra dòng điện → dòng điện xoay chiều và các ứng dụng kĩ thuật."),
("box", "TRỤC LOGIC CỦA CẢ CHƯƠNG",
 "Nguồn sinh từ trường (nam châm, dòng điện) → mô tả từ trường bằng vectơ cảm ứng từ B và đường sức từ "
 "→ biểu hiện của từ trường là lực từ F = BIℓsinθ → khi từ thông Φ qua mạch kín biến thiên thì xuất hiện "
 "suất điện động cảm ứng e = −ΔΦ/Δt → ứng dụng: máy phát điện xoay chiều, máy biến áp, bếp từ… "
 "→ mở rộng: điện từ trường và sóng điện từ."),

# =============================================================== §1
("h2", "§1. TỪ TRƯỜNG – ĐƯỜNG SỨC TỪ"),

("h3", "1.1. Tương tác từ"),
("b", "Nam châm hút được sắt, nickel, cobalt… Hai nam châm đặt gần nhau: các cực cùng tên đẩy nhau, "
      "các cực khác tên hút nhau."),
("b", "Thí nghiệm Oersted (1820): đặt kim nam châm song song dưới một dây dẫn thẳng; khi cho dòng điện "
      "chạy qua dây, kim nam châm bị lệch. Kết luận: dòng điện cũng gây ra tác dụng từ."),
("b", "Hai dây dẫn song song mang dòng điện cùng chiều thì hút nhau, ngược chiều thì đẩy nhau."),
("p", "Ba loại tương tác trên (nam châm – nam châm, dòng điện – nam châm, dòng điện – dòng điện) "
      "đều được gọi chung là tương tác từ. Điều đó gợi ý bản chất từ tính của vật chất gắn liền với "
      "chuyển động của các hạt mang điện."),

("h3", "1.2. Khái niệm từ trường"),
("box", "ĐỊNH NGHĨA",
 "Từ trường là một dạng vật chất tồn tại trong không gian xung quanh nam châm hoặc xung quanh dòng điện "
 "(tổng quát hơn: xung quanh điện tích chuyển động), mà biểu hiện cụ thể của nó là sự xuất hiện lực từ "
 "tác dụng lên một nam châm hay một dòng điện đặt trong đó."),
("b", "Tính chất cơ bản của từ trường: tác dụng lực từ lên nam châm hoặc lên dòng điện đặt trong nó. "
      "Đây cũng chính là cách duy nhất để phát hiện sự có mặt của từ trường."),
("b", "Đại lượng đặc trưng cho từ trường tại một điểm về phương diện tác dụng lực là vectơ cảm ứng từ B."),
("b", "Quy ước hướng của từ trường tại một điểm: là hướng Nam – Bắc của kim nam châm nhỏ nằm cân bằng "
      "tại điểm đó (vectơ B hướng từ cực Nam sang cực Bắc của kim)."),
("trap", "Sai lầm phổ biến: coi từ trường là “thứ do nam châm phát ra và bay đi”. Từ trường không phải "
         "vật chất dạng hạt chuyển động; nó là một dạng vật chất đặc biệt tồn tại đồng thời trong cả vùng "
         "không gian quanh nguồn, không cần môi trường truyền và tồn tại cả trong chân không."),

("h3", "1.3. Đường sức từ – từ phổ"),
("b", "Đường sức từ là những đường vẽ trong không gian có từ trường sao cho tiếp tuyến tại mỗi điểm "
      "trùng với phương của vectơ cảm ứng từ tại điểm đó, chiều của đường sức là chiều của B."),
("b", "Từ phổ: hình ảnh các mạt sắt sắp xếp trong từ trường, cho phép “nhìn thấy” dạng của các đường sức từ."),
("fig", "f01_nam_cham_thang", "Hình 3.1. Từ phổ và đường sức từ của một nam châm thẳng."),
("box", "BỐN TÍNH CHẤT CỦA ĐƯỜNG SỨC TỪ (rất hay được hỏi)",
 "(1) Qua mỗi điểm trong từ trường chỉ vẽ được một đường sức từ.\n"
 "(2) Các đường sức từ là những đường cong khép kín hoặc vô hạn ở hai đầu — chúng KHÔNG có điểm bắt đầu "
 "và điểm kết thúc. Bên ngoài nam châm, đường sức đi ra từ cực Bắc và đi vào cực Nam; bên trong nam châm "
 "chúng đi từ cực Nam sang cực Bắc để khép kín.\n"
 "(3) Chiều của đường sức từ tuân theo những quy tắc xác định (quy tắc nắm tay phải cho dòng điện).\n"
 "(4) Nơi nào cảm ứng từ lớn hơn thì các đường sức từ vẽ dày hơn, nơi nào B nhỏ thì đường sức thưa hơn."),
("trap", "Phân biệt then chốt với đường sức điện: đường sức điện (trường tĩnh điện) là đường hở, xuất phát "
         "từ điện tích dương và kết thúc ở điện tích âm; còn đường sức từ luôn khép kín. Nguyên nhân sâu xa: "
         "trong tự nhiên chưa tìm thấy “từ tích” (đơn cực từ) — cắt đôi một nam châm ta luôn được hai nam "
         "châm mới, mỗi cái vẫn đủ hai cực."),

("h3", "1.4. Từ trường đều"),
("b", "Từ trường đều là từ trường mà vectơ cảm ứng từ tại mọi điểm đều bằng nhau (cùng phương, cùng chiều, "
      "cùng độ lớn). Đường sức từ của từ trường đều là những đường thẳng song song và cách đều nhau."),
("b", "Nơi tạo được từ trường đều gần đúng: khoảng không gian giữa hai cực của một nam châm hình chữ U, "
      "vùng giữa lòng ống dây dài có dòng điện chạy qua."),

("h3", "1.5. Từ trường của dòng điện – quy tắc nắm tay phải"),
("fig", "f02_dong_dien_thang", "Hình 3.2. Đường sức từ của dòng điện thẳng dài là các đường tròn đồng tâm "
                              "nằm trong mặt phẳng vuông góc với dây dẫn."),
("b", "Dòng điện thẳng dài: đường sức từ là những đường tròn đồng tâm nằm trong mặt phẳng vuông góc với "
      "dây dẫn, tâm nằm trên dây. Càng xa dây, các đường tròn càng thưa (B càng nhỏ)."),
("b", "Quy tắc nắm tay phải cho dòng điện thẳng: nắm bàn tay phải sao cho ngón cái choãi ra chỉ chiều "
      "dòng điện, khi đó các ngón tay còn lại khum lại chỉ chiều của đường sức từ."),
("fig", "f03_ong_day", "Hình 3.3. Từ trường của ống dây có dòng điện chạy qua: giống hệt từ trường của "
                       "một nam châm thẳng."),
("b", "Ống dây có dòng điện: bên trong lòng ống dây dài, từ trường coi như đều; bên ngoài, dạng đường sức "
      "giống của nam châm thẳng. Đầu ống dây mà đường sức đi ra là cực Bắc, đầu đường sức đi vào là cực Nam."),
("b", "Quy tắc nắm tay phải cho ống dây: khum bốn ngón tay phải theo chiều dòng điện chạy trong các vòng dây, "
      "ngón cái choãi ra chỉ chiều đường sức từ trong lòng ống dây, tức chỉ về phía cực Bắc của ống dây."),

("h3", "1.6. Từ trường Trái Đất"),
("b", "Trái Đất có từ trường; đó là lí do kim la bàn luôn định hướng gần đúng theo phương Bắc – Nam."),
("b", "Điểm cần nhớ để tránh bẫy: cực Bắc địa từ nằm gần cực Nam địa lí và ngược lại. Cực Bắc của kim "
      "nam châm bị hút về phía Bắc địa lí, mà các cực khác tên mới hút nhau, nên ở gần Bắc địa lí phải là "
      "một cực từ Nam."),
("b", "Độ lớn cảm ứng từ của từ trường Trái Đất ở gần mặt đất vào cỡ 5·10⁻⁵ T — rất nhỏ so với từ trường "
      "của một nam châm vĩnh cửu thông thường (10⁻² ÷ 10⁻¹ T) hay của nam châm điện mạnh (vài T)."),
("b", "Ứng dụng và hiện tượng liên quan: la bàn, sự định hướng di cư của một số loài vật, vành đai bức xạ "
      "che chắn hạt tích điện từ Mặt Trời, cực quang."),
("exam", "Ghi nhớ cho phần thi: câu hỏi về Chương III thường mở đầu bằng nhận biết dạng đường sức từ và "
         "chiều của nó. Hãy thuộc: (a) đường sức từ khép kín; (b) chiều đường sức trong lòng ống dây xác "
         "định bằng quy tắc nắm tay phải; (c) mật độ đường sức tỉ lệ với độ lớn B."),

# =============================================================== §2
("h2", "§2. LỰC TỪ TÁC DỤNG LÊN DÂY DẪN MANG DÒNG ĐIỆN – CẢM ỨNG TỪ"),

("h3", "2.1. Công thức lực từ"),
("fig", "f04_luc_tu", "Hình 3.4. Lực từ tác dụng lên đoạn dây dẫn mang dòng điện đặt trong từ trường đều."),
("f", "F = B · I · ℓ · sinθ"),
("b", "F: độ lớn lực từ (N); B: độ lớn cảm ứng từ (T); I: cường độ dòng điện (A); "
      "ℓ: chiều dài đoạn dây dẫn nằm trong từ trường (m); "
      "θ: góc hợp bởi đoạn dây dẫn (hướng dòng điện) và vectơ cảm ứng từ B."),
("box", "ĐIỀU KIỆN ÁP DỤNG CÔNG THỨC F = BIℓsinθ",
 "• Đoạn dây dẫn phải thẳng.\n"
 "• Từ trường trong vùng chứa đoạn dây phải là từ trường đều.\n"
 "• ℓ là phần chiều dài NẰM TRONG từ trường, không phải toàn bộ chiều dài dây dẫn. Đây là bẫy rất hay gặp: "
 "dây dài 50 cm nhưng chỉ có 20 cm nằm giữa hai cực nam châm thì ℓ = 0,20 m."),
("fig", "f05_goc_theta", "Hình 3.5. Sự phụ thuộc của lực từ vào góc θ giữa dây dẫn và vectơ cảm ứng từ."),
("b", "θ = 90° (dây vuông góc với B): F đạt cực đại, F_max = BIℓ."),
("b", "θ = 0° hoặc 180° (dây song song với đường sức từ): F = 0. Đây là trường hợp học sinh hay quên nhất."),
("b", "F là hàm của sinθ nên biến thiên không tuyến tính theo θ: khi θ tăng từ 0° đến 90° thì F tăng, "
      "khi θ tăng tiếp từ 90° đến 180° thì F giảm về 0."),

("h3", "2.2. Cảm ứng từ – định nghĩa và đơn vị"),
("box", "ĐỊNH NGHĨA CẢM ỨNG TỪ",
 "Thương số F/(I·ℓ) khi đoạn dây đặt vuông góc với đường sức từ không phụ thuộc vào I và ℓ mà chỉ phụ thuộc "
 "từ trường tại vị trí khảo sát. Thương số đó được dùng để định nghĩa độ lớn cảm ứng từ:\n"
 "B = F / (I·ℓ)   (khi θ = 90°),  tổng quát  B = F / (I·ℓ·sinθ)."),
("b", "Đơn vị cảm ứng từ trong hệ SI là tesla (T): 1 T = 1 N/(A·m). Một tesla là cảm ứng từ của một từ "
      "trường đều sao cho một đoạn dây dài 1 m mang dòng điện 1 A đặt vuông góc với đường sức chịu lực từ 1 N."),
("b", "Cảm ứng từ là đại lượng VECTƠ: phương và chiều của B là phương chiều của từ trường tại điểm khảo sát, "
      "được xác định bằng kim nam châm thử; độ lớn xác định theo công thức trên."),
("tbl", "Bảng 3.1. Một số đơn vị và giá trị cần nhớ trong phần từ trường",
 ["Đại lượng", "Kí hiệu", "Đơn vị SI", "Giá trị tham khảo"],
 [["Cảm ứng từ", "B", "tesla (T) = N/(A·m)", "Trái Đất ≈ 5·10⁻⁵ T; nam châm vĩnh cửu ≈ 10⁻² ÷ 10⁻¹ T"],
  ["Lực từ", "F", "niutơn (N)", "—"],
  ["Từ thông", "Φ", "vêbe (Wb) = T·m²", "—"],
  ["Suất điện động cảm ứng", "e", "vôn (V)", "—"],
  ["Cường độ dòng điện", "I", "ampe (A)", "—"]]),

("h3", "2.3. Quy tắc bàn tay trái (xác định chiều lực từ)"),
("box", "PHÁT BIỂU",
 "Đặt bàn tay trái duỗi thẳng sao cho các đường sức từ hướng vào lòng bàn tay, chiều từ cổ tay đến ngón tay "
 "giữa là chiều dòng điện; khi đó ngón tay cái choãi ra 90° chỉ chiều của lực từ tác dụng lên dây dẫn."),
("b", "Hệ quả hình học quan trọng: lực từ F luôn vuông góc đồng thời với cả dây dẫn (hướng I) và với vectơ "
      "cảm ứng từ B, nghĩa là F vuông góc với mặt phẳng chứa I và B."),
("trap", "Sai lầm rất phổ biến: cho rằng lực từ cùng phương với B (“từ trường kéo dây dẫn theo đường sức”). "
         "Điều đó sai — lực từ luôn vuông góc với B. Cũng sai khi cho rằng lực từ hướng theo chiều dòng điện."),

("h3", "2.4. Thí nghiệm đo cảm ứng từ bằng “cân dòng điện”"),
("fig", "f06_can_dong_dien", "Hình 3.6. Sơ đồ nguyên tắc phép đo cảm ứng từ bằng cân dòng điện."),
("b", "Ý tưởng: đặt một đoạn dây dẫn thẳng chiều dài ℓ nằm ngang, vuông góc với từ trường của nam châm hình "
      "chữ U; nam châm đặt trên đĩa cân điện tử. Khi cho dòng điện I chạy qua dây, lực từ tác dụng lên dây "
      "hướng lên (hoặc xuống); theo định luật III Newton, dây tác dụng ngược lại lên nam châm một lực "
      "cùng độ lớn, làm số chỉ của cân thay đổi một lượng Δm."),
("f", "F = Δm · g = B · I · ℓ   ⟹   B = Δm·g / (I·ℓ)"),
("b", "Cách xử lí số liệu chuẩn: đo Δm ứng với nhiều giá trị I khác nhau, vẽ đồ thị F theo I. Đồ thị là "
      "đường thẳng đi qua gốc toạ độ, hệ số góc bằng B·ℓ, từ đó suy ra B = (hệ số góc)/ℓ. "
      "Cách này khử được sai số ngẫu nhiên tốt hơn việc chỉ đo một lần."),
("b", "Nguồn sai số cần thảo luận: đoạn dây không thật vuông góc với B (làm F nhỏ đi vì sinθ < 1, dẫn tới "
      "B đo được nhỏ hơn giá trị thật); từ trường ở mép nam châm không đều; dây dẫn bị nóng làm I thay đổi; "
      "cân chưa được hiệu chỉnh về 0 trước khi đóng mạch."),
("exam", "Dạng câu hỏi thực nghiệm thường gặp: cho bảng số liệu (I, Δm), yêu cầu vẽ/nhận xét đồ thị và tính B. "
         "Nhớ đổi đơn vị khối lượng sang kilôgam và lấy g = 9,8 hoặc 9,81 m/s² theo đề."),

("h3", "2.5. Mở rộng nâng cao: lực từ tác dụng lên khung dây"),
("b", "Với một khung dây kín mang dòng điện đặt trong từ trường ĐỀU, tổng hợp các lực từ tác dụng lên các "
      "cạnh bằng không, nhưng chúng tạo thành một ngẫu lực làm khung quay cho đến khi mặt phẳng khung "
      "vuông góc với B. Đây chính là nguyên tắc hoạt động của động cơ điện một chiều và của điện kế khung quay."),
("b", "Nếu từ trường không đều, hợp lực nói chung khác không — đó là lí do nam châm hút được vụn sắt "
      "(vụn sắt bị nhiễm từ rồi bị kéo về phía từ trường mạnh hơn)."),

# =============================================================== §3
("h2", "§3. TỪ THÔNG – HIỆN TƯỢNG CẢM ỨNG ĐIỆN TỪ"),

("h3", "3.1. Từ thông"),
("fig", "f07_tu_thong", "Hình 3.7. Từ thông qua một khung dây phẳng đặt trong từ trường đều."),
("f", "Φ = N · B · S · cosα"),
("b", "S: diện tích của mạch kín (m²); N: số vòng dây; α: góc hợp bởi vectơ pháp tuyến n của mặt phẳng khung "
      "và vectơ cảm ứng từ B. Đơn vị của từ thông là vêbe (Wb); 1 Wb = 1 T·m²."),
("box", "PHÂN BIỆT HAI CÁCH VIẾT — TRÁNH NHẦM HỆ SỐ N",
 "• Từ thông qua MỘT vòng dây: Φ₁ = B·S·cosα. Khi đó suất điện động của khung N vòng là e = −N·ΔΦ₁/Δt.\n"
 "• Từ thông (toàn phần) qua khung N vòng: Φ = N·B·S·cosα. Khi đó e = −ΔΦ/Δt.\n"
 "Hai cách viết cho cùng một kết quả; điều tối kị là vừa nhân N vào từ thông vừa nhân thêm N vào công thức "
 "suất điện động (khi đó kết quả bị lớn gấp N lần). Khi đọc đề, hãy xác định rõ đại lượng cho trong đề là "
 "từ thông qua một vòng hay qua cả khung."),
("b", "Ý nghĩa vật lí: từ thông tỉ lệ với số đường sức từ xuyên qua diện tích S. Vì vậy nói “từ thông tăng” "
      "cũng có nghĩa là “số đường sức xuyên qua mạch tăng lên”."),
("b", "Từ thông là đại lượng ĐẠI SỐ, có thể dương, âm hoặc bằng không tuỳ theo cách chọn chiều pháp tuyến: "
      "α < 90° thì Φ > 0; α = 90° (mặt phẳng khung chứa các đường sức) thì Φ = 0; α > 90° thì Φ < 0."),
("b", "Ba cách làm biến thiên từ thông qua một mạch kín: thay đổi B (dịch chuyển nam châm, thay đổi dòng điện "
      "trong nam châm điện), thay đổi S (bóp méo hoặc kéo giãn khung), thay đổi α (quay khung trong từ trường)."),

("h3", "3.2. Hiện tượng cảm ứng điện từ"),
("fig", "f08_thi_nghiem_faraday", "Hình 3.8. Thí nghiệm cơ bản về hiện tượng cảm ứng điện từ."),
("box", "ĐỊNH NGHĨA",
 "Khi từ thông qua một mạch kín biến thiên thì trong mạch xuất hiện một suất điện động cảm ứng, do đó "
 "xuất hiện dòng điện cảm ứng. Hiện tượng đó gọi là hiện tượng cảm ứng điện từ."),
("b", "Điều kiện tiên quyết: từ thông phải BIẾN THIÊN. Nếu nam châm và ống dây đứng yên tương đối với nhau "
      "thì dù từ thông rất lớn cũng không có dòng điện cảm ứng."),
("b", "Dòng điện cảm ứng chỉ tồn tại trong thời gian từ thông biến thiên; khi sự biến thiên ngừng lại thì "
      "dòng điện cảm ứng cũng mất."),

("h3", "3.3. Định luật Faraday"),
("f", "e = − ΔΦ/Δt      (độ lớn:  |e| = |ΔΦ| / Δt )"),
("b", "Phát biểu: suất điện động cảm ứng trong mạch kín tỉ lệ với TỐC ĐỘ biến thiên của từ thông qua mạch."),
("b", "Dấu “trừ” trong công thức là biểu diễn toán học của định luật Lenz, thể hiện chiều của suất điện động "
      "cảm ứng chứ không phải một hệ số tính toán."),
("b", "Nếu mạch kín có điện trở R thì cường độ dòng điện cảm ứng là i = |e|/R; điện lượng chuyển qua mạch "
      "trong thời gian Δt là q = i·Δt = |ΔΦ|/R — chú ý q chỉ phụ thuộc độ biến thiên từ thông và điện trở, "
      "KHÔNG phụ thuộc thời gian biến thiên nhanh hay chậm. Đây là một kết quả nâng cao rất hay được khai thác."),
("trap", "Ba nhầm lẫn kinh điển:\n"
         "(1) “Từ thông càng lớn thì suất điện động càng lớn” — SAI. e phụ thuộc ΔΦ/Δt chứ không phụ thuộc Φ.\n"
         "(2) “Từ thông bằng 0 thì e bằng 0” — SAI. Khi khung quay qua vị trí mặt phẳng khung song song với B "
         "thì Φ = 0 nhưng tốc độ biến thiên của Φ lại cực đại nên |e| cực đại.\n"
         "(3) “Từ thông cực đại thì e cực đại” — SAI, ngược lại: lúc đó ΔΦ/Δt = 0 nên e = 0."),
("fig", "f11_phi_e", "Hình 3.9. Quan hệ về pha giữa từ thông và suất điện động cảm ứng trong khung dây quay đều."),
("h3", "3.3b. Kĩ thuật đọc đồ thị từ thông – dạng bài rất hay gặp"),
("fig", "f15_phi_gap_khuc", "Hình 3.10. Đồ thị từ thông biến thiên theo thời gian gồm nhiều đoạn thẳng."),
("b", "Khi Φ(t) là đường gấp khúc gồm các đoạn thẳng thì trên mỗi đoạn, |e| bằng đúng ĐỘ LỚN HỆ SỐ GÓC "
      "của đoạn thẳng đó. Đoạn nằm ngang ứng với e = 0; đoạn càng dốc thì |e| càng lớn."),
("b", "Với đồ thị ở Hình 3.10: giai đoạn (1) cho |e| = 0,8/2 = 0,4 V; giai đoạn (2) cho e = 0; "
      "giai đoạn (3) cho |e| = 0,6/1 = 0,6 V; giai đoạn (4) cho e = 0. Như vậy giai đoạn có từ thông NHỎ nhất "
      "lại cho suất điện động LỚN nhất — minh hoạ trực tiếp cho việc e phụ thuộc tốc độ biến thiên."),
("b", "Đồ thị e(t) tương ứng có dạng bậc thang, và đổi dấu khi từ thông chuyển từ tăng sang giảm."),

("h3", "3.4. Định luật Lenz"),
("fig", "f09_lenz", "Hình 3.10. Minh hoạ định luật Lenz cho hai trường hợp nam châm lại gần và ra xa ống dây."),
("box", "PHÁT BIỂU",
 "Dòng điện cảm ứng xuất hiện trong mạch kín có chiều sao cho từ trường do nó sinh ra có tác dụng CHỐNG LẠI "
 "sự biến thiên của từ thông ban đầu qua mạch kín đó."),
("b", "Quy trình vận dụng gồm bốn bước: (1) xác định chiều của B ban đầu qua mạch; (2) xét xem từ thông đang "
      "tăng hay giảm; (3) suy ra chiều của từ trường cảm ứng — ngược chiều B ban đầu nếu Φ tăng, cùng chiều "
      "B ban đầu nếu Φ giảm; (4) dùng quy tắc nắm tay phải để suy ra chiều dòng điện cảm ứng."),
("b", "Dạng phát biểu tương đương rất tiện dùng khi có chuyển động cơ học: dòng điện cảm ứng luôn có tác dụng "
      "chống lại nguyên nhân đã sinh ra nó. Vì thế khi đưa nam châm lại gần vòng dây, vòng dây đẩy nam châm; "
      "khi đưa nam châm ra xa, vòng dây hút giữ nam châm lại."),
("b", "Cơ sở sâu xa của định luật Lenz là định luật bảo toàn năng lượng: muốn duy trì chuyển động tương đối "
      "ta phải sinh công thắng lực cản từ, công đó chuyển hoá thành điện năng rồi thành nhiệt trên mạch."),
("trap", "Nếu định luật Lenz có dấu ngược lại (dòng cảm ứng “ủng hộ” sự biến thiên) thì chỉ cần một cú hích ban "
         "đầu, hệ sẽ tự tăng tốc mãi mãi và sinh năng lượng từ hư không. Lập luận này thường được dùng làm câu "
         "hỏi vận dụng cao về mối liên hệ giữa định luật Lenz và bảo toàn năng lượng."),

("h3", "3.5. Suất điện động cảm ứng trên thanh dẫn chuyển động"),
("fig", "f16_thanh_truot", "Hình 3.11. Thanh dẫn trượt trên hai ray trong từ trường đều."),
("f", "e = B · ℓ · v      (thanh vuông góc với B và với vận tốc v)"),
("b", "Cách hiểu bằng từ thông: sau thời gian Δt thanh quét thêm diện tích ΔS = ℓ·v·Δt nên "
      "|ΔΦ| = B·ℓ·v·Δt, chia cho Δt được ngay e = Bℓv."),
("b", "Nếu mạch kín có điện trở R thì i = Bℓv/R, và lực từ tác dụng lên thanh có độ lớn "
      "F = B·i·ℓ = B²ℓ²v/R, luôn hướng ngược chiều chuyển động (đúng theo định luật Lenz). "
      "Muốn thanh chuyển động đều, ngoại lực phải cân bằng lực từ này."),

("h3", "3.6. Dòng điện Foucault (dòng điện xoáy)"),
("b", "Khi một khối kim loại đặc chuyển động trong từ trường hoặc đặt trong từ trường biến thiên, trong khối "
      "kim loại xuất hiện các dòng điện cảm ứng chạy thành vòng xoáy khép kín, gọi là dòng Foucault."),
("b", "Tác dụng có hại: gây toả nhiệt làm hao phí năng lượng trong lõi máy biến áp, động cơ điện. "
      "Cách khắc phục: làm lõi bằng nhiều lá thép mỏng ghép cách điện với nhau để tăng điện trở đối với dòng xoáy."),
("b", "Tác dụng có lợi: phanh điện từ trên tàu cao tốc và xe tải hạng nặng, lò cảm ứng nấu kim loại, bếp từ, "
      "công tơ điện kiểu cảm ứng."),

# =============================================================== §4
("h2", "§4. MÁY PHÁT ĐIỆN XOAY CHIỀU – DÒNG ĐIỆN XOAY CHIỀU"),

("h3", "4.1. Nguyên tắc tạo ra dòng điện xoay chiều"),
("fig", "f10_may_phat", "Hình 3.12. Sơ đồ nguyên tắc của máy phát điện xoay chiều."),
("b", "Cho một khung dây dẫn kín N vòng, diện tích S quay đều với tốc độ góc ω quanh một trục vuông góc với "
      "vectơ cảm ứng từ B của một từ trường đều."),
("b", "Từ thông qua khung biến thiên tuần hoàn theo thời gian: Φ = N·B·S·cos(ωt + φ₀)."),
("f", "e = − ΔΦ/Δt  ⟹  e = E₀·sin(ωt + φ₀)   với   E₀ = N·B·S·ω"),
("b", "Nhận xét quan trọng về pha: e trễ pha π/2 so với Φ. Khi Φ đạt cực đại thì e = 0 và ngược lại "
      "(xem lại Hình 3.9)."),
("b", "Cấu tạo thực tế gồm phần cảm (tạo từ trường, thường là nam châm) và phần ứng (các cuộn dây xuất hiện "
      "suất điện động). Bộ phận đứng yên gọi là stato, bộ phận quay gọi là rôto. Trong máy phát công suất lớn, "
      "người ta cho nam châm quay còn cuộn dây đứng yên để tránh phải dùng vành khuyên – chổi quét cho dòng lớn."),

("h3", "4.2. Các đại lượng đặc trưng của dòng điện xoay chiều"),
("b", "Dòng điện xoay chiều là dòng điện có cường độ biến thiên điều hoà theo thời gian: i = I₀·cos(ωt + φᵢ)."),
("b", "I₀ là cường độ dòng điện cực đại (biên độ); ω là tần số góc (rad/s); "
      "chu kì T = 2π/ω (s); tần số f = 1/T = ω/(2π) (Hz). Mạng điện dân dụng Việt Nam có f = 50 Hz."),
("fig", "f12_hieu_dung", "Hình 3.13. Giá trị cực đại và giá trị hiệu dụng của dòng điện xoay chiều."),
("box", "GIÁ TRỊ HIỆU DỤNG",
 "Cường độ hiệu dụng của dòng điện xoay chiều là đại lượng có giá trị bằng cường độ của một dòng điện không "
 "đổi, sao cho khi đi qua cùng một điện trở R thì công suất toả nhiệt trung bình của hai dòng điện là như nhau.\n"
 "I = I₀/√2 ;   U = U₀/√2 ;   E = E₀/√2 ."),
("b", "Ý nghĩa thực tiễn: các ampe kế, vôn kế xoay chiều đều chỉ giá trị hiệu dụng. Điện áp 220 V của mạng "
      "điện dân dụng là giá trị hiệu dụng; giá trị cực đại tương ứng là U₀ = 220√2 ≈ 311 V. Đây là lí do "
      "thiết bị điện phải được thiết kế chịu được điện áp đỉnh lớn hơn 220 V."),
("b", "Công suất toả nhiệt trung bình trên điện trở R: P = I²·R = U²/R (dùng giá trị hiệu dụng), "
      "không dùng I₀ và U₀."),
("trap", "Giá trị hiệu dụng KHÔNG phải giá trị trung bình. Giá trị trung bình của i trong một chu kì bằng 0 "
         "(vì dòng đổi chiều), còn giá trị hiệu dụng được định nghĩa qua tác dụng nhiệt (trung bình của i²) "
         "nên luôn dương và bằng I₀/√2."),
("b", "Một kết quả nâng cao hay được hỏi: trong mỗi chu kì dòng điện xoay chiều đổi chiều 2 lần, nên trong "
      "1 giây dòng điện đổi chiều 2f lần (với f = 50 Hz thì 100 lần)."),

# =============================================================== §5
("h2", "§5. ỨNG DỤNG CỦA HIỆN TƯỢNG CẢM ỨNG ĐIỆN TỪ"),

("h3", "5.1. Máy biến áp"),
("fig", "f13_bien_ap", "Hình 3.14. Cấu tạo và kí hiệu của máy biến áp."),
("b", "Cấu tạo: hai cuộn dây có số vòng khác nhau (cuộn sơ cấp N₁, cuộn thứ cấp N₂) quấn trên một lõi thép "
      "kín ghép từ các lá thép mỏng cách điện."),
("b", "Nguyên tắc: dòng điện xoay chiều ở cuộn sơ cấp tạo ra từ thông biến thiên trong lõi thép; từ thông này "
      "xuyên qua cuộn thứ cấp và gây ra suất điện động cảm ứng ở đó."),
("f", "U₁/U₂ = N₁/N₂ ;   nếu bỏ qua hao phí:  U₁·I₁ = U₂·I₂  ⟹  I₁/I₂ = N₂/N₁"),
("b", "N₂ > N₁: máy tăng áp; N₂ < N₁: máy hạ áp. Máy biến áp KHÔNG làm thay đổi tần số của dòng điện."),
("trap", "Máy biến áp không hoạt động được với dòng điện không đổi: dòng không đổi tạo ra từ thông không đổi "
         "trong lõi, không có biến thiên nên không có suất điện động cảm ứng ở cuộn thứ cấp. Đây là câu hỏi "
         "phân biệt bản chất rất hay xuất hiện."),
("b", "Ứng dụng then chốt — truyền tải điện năng đi xa: công suất hao phí trên đường dây "
      "ΔP = R·P²/(U²·cos²φ). Vì ΔP tỉ lệ nghịch với U², tăng điện áp truyền tải lên n lần thì hao phí giảm "
      "n² lần. Do đó người ta dùng máy tăng áp ở đầu đường dây và máy hạ áp ở nơi tiêu thụ."),

("h3", "5.2. Các ứng dụng khác"),
("b", "Đàn ghi ta điện: mỗi dây đàn bằng thép được đặt cạnh một cuộn dây quấn quanh nam châm nhỏ. Dây đàn bị "
      "từ hoá, khi rung sẽ làm từ thông qua cuộn dây biến thiên, sinh ra suất điện động cảm ứng biến thiên "
      "cùng tần số với dao động của dây; tín hiệu này được khuếch đại và đưa ra loa."),
("b", "Bếp từ: cuộn dây dưới mặt bếp được cấp dòng điện xoay chiều tần số cao, tạo từ trường biến thiên nhanh; "
      "từ trường này gây dòng Foucault ngay trong đáy nồi bằng vật liệu nhiễm từ, làm nồi nóng lên. "
      "Vì thế bếp từ chỉ dùng được với nồi có đáy nhiễm từ, và mặt bếp không tự nóng."),
("b", "Sạc không dây, micro điện động, máy dò kim loại, phanh điện từ, công tơ điện — tất cả đều dựa trên "
      "hiện tượng cảm ứng điện từ."),

# =============================================================== §6
("h2", "§6. ĐIỆN TỪ TRƯỜNG – MÔ HÌNH SÓNG ĐIỆN TỪ"),
("b", "Tại nơi có từ trường biến thiên theo thời gian thì xuất hiện một điện trường xoáy — điện trường có các "
      "đường sức khép kín, khác hẳn điện trường tĩnh có đường sức hở."),
("b", "Ngược lại, tại nơi có điện trường biến thiên theo thời gian thì xuất hiện một từ trường. Thí nghiệm "
      "kinh điển minh hoạ: dòng điện xoay chiều vẫn “chạy qua” tụ điện, giữa hai bản tụ không có dòng các "
      "hạt mang điện nhưng vẫn tồn tại từ trường."),
("b", "Điện trường biến thiên và từ trường biến thiên luôn tồn tại đồng thời, chuyển hoá lẫn nhau và liên hệ "
      "mật thiết với nhau; chúng là hai mặt của một trường thống nhất gọi là điện từ trường."),
("fig", "f14_song_dien_tu", "Hình 3.15. Mô hình sóng điện từ lan truyền trong không gian."),
("box", "TÍNH CHẤT CỦA SÓNG ĐIỆN TỪ",
 "• Sóng điện từ là sự lan truyền của điện từ trường biến thiên trong không gian.\n"
 "• Là SÓNG NGANG: vectơ E và vectơ B luôn vuông góc với nhau và cùng vuông góc với phương truyền sóng.\n"
 "• E và B tại một điểm luôn dao động cùng pha.\n"
 "• Truyền được trong chân không với tốc độ c ≈ 3·10⁸ m/s; bước sóng λ = c/f (trong chân không).\n"
 "• Mang năng lượng; tuân theo các quy luật phản xạ, khúc xạ, giao thoa, nhiễu xạ như sóng ánh sáng."),
("trap", "Điểm phân biệt cốt lõi với sóng cơ: sóng cơ (âm thanh, sóng trên mặt nước) BẮT BUỘC cần môi trường "
         "vật chất để truyền, còn sóng điện từ truyền được cả trong chân không. Đó là lí do ta nhận được sóng "
         "vô tuyến và ánh sáng từ các thiên thể nhưng không nghe được tiếng nổ ngoài vũ trụ."),
("b", "Thang sóng điện từ (theo bước sóng giảm dần): sóng vô tuyến → vi sóng → hồng ngoại → ánh sáng nhìn thấy "
      "→ tử ngoại → tia X → tia gamma. Bản chất giống nhau, chỉ khác tần số nên khác về tác dụng."),

# =============================================================== §7
("h2", "§7. TỔNG KẾT CHƯƠNG III"),
("tbl", "Bảng 3.2. Hệ thống công thức trọng tâm của Chương III",
 ["Nội dung", "Công thức", "Điều kiện áp dụng / lưu ý"],
 [["Lực từ", "F = B·I·ℓ·sinθ", "Dây thẳng, từ trường đều; ℓ là phần dây nằm trong từ trường"],
  ["Cảm ứng từ", "B = F/(I·ℓ·sinθ)", "Định nghĩa; đơn vị T = N/(A·m)"],
  ["Từ thông", "Φ = N·B·S·cosα", "α là góc giữa pháp tuyến n và B; Φ là đại lượng đại số"],
  ["Định luật Faraday", "e = −ΔΦ/Δt", "Mạch kín; dấu trừ thể hiện định luật Lenz"],
  ["Dòng điện cảm ứng", "i = |e|/R", "Mạch kín có điện trở R"],
  ["Điện lượng cảm ứng", "q = |ΔΦ|/R", "Không phụ thuộc thời gian biến thiên"],
  ["Thanh dẫn chuyển động", "e = B·ℓ·v", "Thanh vuông góc với B và với v"],
  ["Máy phát điện", "E₀ = N·B·S·ω", "Khung quay đều quanh trục vuông góc với B"],
  ["Giá trị hiệu dụng", "I = I₀/√2 ; U = U₀/√2", "Dòng điện biến thiên điều hoà"],
  ["Máy biến áp", "U₁/U₂ = N₁/N₂", "Máy lí tưởng, chỉ dùng cho dòng xoay chiều"],
  ["Hao phí truyền tải", "ΔP = R·P²/(U²cos²φ)", "Tăng U lên n lần thì ΔP giảm n² lần"],
  ["Sóng điện từ", "λ = c/f, c ≈ 3·10⁸ m/s", "Trong chân không"]]),
("box", "MƯỜI LỖI SAI THƯỜNG GẶP NHẤT CỦA CHƯƠNG III",
 "1. Dùng toàn bộ chiều dài dây thay vì phần dây nằm trong từ trường khi tính F.\n"
 "2. Quên rằng F = 0 khi dây dẫn song song với đường sức từ.\n"
 "3. Nhầm góc θ trong công thức lực từ (giữa dây và B) với góc α trong công thức từ thông (giữa pháp tuyến và B).\n"
 "4. Nhân hệ số N hai lần khi tính suất điện động của khung nhiều vòng.\n"
 "5. Cho rằng từ thông lớn thì suất điện động lớn.\n"
 "6. Cho rằng khi Φ = 0 thì e = 0 (thực tế lúc đó |e| cực đại với khung quay đều).\n"
 "7. Xác định sai chiều dòng điện cảm ứng do bỏ qua bước “từ thông đang tăng hay giảm”.\n"
 "8. Lẫn lộn giá trị hiệu dụng với giá trị cực đại (220 V và 311 V).\n"
 "9. Cho rằng máy biến áp làm thay đổi tần số, hoặc hoạt động được với dòng điện không đổi.\n"
 "10. Cho rằng sóng điện từ cần môi trường vật chất để truyền."),
("exam", "Định hướng ra đề 2026 cho Chương III: phần trắc nghiệm nhiều lựa chọn thường kiểm tra đường sức từ, "
         "quy tắc xác định chiều, công thức lực từ và giá trị hiệu dụng. Phần đúng/sai thường gắn với một thí "
         "nghiệm cụ thể (nam châm – ống dây – điện kế, cân dòng điện, khung dây quay) hoặc một đồ thị Φ(t), i(t), "
         "và yêu cầu đánh giá bốn nhận định về chiều dòng điện, độ lớn suất điện động, sự phụ thuộc các đại lượng. "
         "Phần trả lời ngắn thường là bài toán về lực từ, suất điện động cảm ứng, máy biến áp hoặc truyền tải điện."),
]
