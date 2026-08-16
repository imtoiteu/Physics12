# -*- coding: utf-8 -*-
"""Tài liệu dạy học CHƯƠNG IV – VẬT LÍ HẠT NHÂN (Vật lí 12, GDPT 2018)."""

CH4 = [
("h1", "CHƯƠNG IV – VẬT LÍ HẠT NHÂN"),
("p", "Chương IV tương ứng với các bài 21 – 25 của sách giáo khoa Vật lí 12 (bộ Kết nối tri thức với cuộc sống) "
      "và chủ đề “Vật lí hạt nhân và phóng xạ” trong Chương trình GDPT 2018. So với chương trình cũ, chương này "
      "giảm mạnh các bài toán động lực học phản ứng hạt nhân nhưng TĂNG rõ rệt yêu cầu về bản chất hiện tượng, "
      "an toàn phóng xạ, ứng dụng thực tiễn và khai thác đồ thị – bảng số liệu. Đề thi thường lấy bối cảnh thực: "
      "xác định niên đại bằng C-14, xạ trị, kiểm tra khuyết tật mối hàn, nhà máy điện hạt nhân."),
("box", "TRỤC LOGIC CỦA CẢ CHƯƠNG",
 "Cấu trúc hạt nhân (proton, neutron, lực hạt nhân) → độ hụt khối và năng lượng liên kết (vì sao hạt nhân bền) "
 "→ đường cong E_lk/A giải thích vì sao cả phân hạch lẫn nhiệt hạch đều toả năng lượng → phản ứng hạt nhân và "
 "các định luật bảo toàn → phóng xạ (quy luật thống kê, chu kì bán rã, độ phóng xạ) → ứng dụng và an toàn."),

# =============================================================== §1
("h2", "§1. CẤU TRÚC HẠT NHÂN"),

("h3", "1.1. Thí nghiệm tán xạ hạt α của Rutherford"),
("fig", "f18_rutherford", "Hình 4.1. Sơ đồ thí nghiệm tán xạ hạt α trên lá vàng mỏng."),
("b", "Bắn chùm hạt α vào một lá vàng rất mỏng và quan sát vệt sáng trên màn huỳnh quang bao quanh."),
("b", "Kết quả: đại đa số hạt α truyền thẳng gần như không lệch hướng; một số rất ít bị lệch góc lớn, "
      "thậm chí bật ngược trở lại."),
("b", "Suy luận: nếu điện tích dương phân bố đều trong toàn bộ nguyên tử thì không thể có hạt bị bật ngược. "
      "Vậy điện tích dương và hầu hết khối lượng phải tập trung trong một vùng cực kì nhỏ ở tâm nguyên tử — "
      "đó là hạt nhân. Phần còn lại của nguyên tử hầu như rỗng, nơi các electron chuyển động."),
("b", "Đánh giá kích thước: từ điều kiện hạt α bị đẩy dừng lại, ước tính được bán kính hạt nhân cỡ 10⁻¹⁴ ÷ 10⁻¹⁵ m, "
      "nhỏ hơn bán kính nguyên tử (cỡ 10⁻¹⁰ m) khoảng 10⁴ ÷ 10⁵ lần."),

("h3", "1.2. Cấu tạo hạt nhân"),
("fig", "f17_cau_tao_hat_nhan", "Hình 4.2. Cấu tạo hạt nhân và ý nghĩa của kí hiệu hạt nhân."),
("b", "Hạt nhân được tạo thành từ các nucleon gồm hai loại: proton (p) mang điện tích +e và neutron (n) không mang điện."),
("b", "Kí hiệu hạt nhân của nguyên tố X: A và Z lần lượt là số khối và số proton. "
      "Z gọi là số hiệu nguyên tử (bằng số proton, cũng bằng số electron của nguyên tử trung hoà); "
      "A là tổng số nucleon; số neutron N = A − Z."),
("b", "Đồng vị là những hạt nhân có cùng số proton Z nhưng khác số neutron N (do đó khác A). "
      "Các đồng vị có cùng tính chất hoá học nhưng tính chất hạt nhân (độ bền, tính phóng xạ) rất khác nhau. "
      "Ví dụ hydrogen có ba đồng vị: hydrogen thường (A = 1), deuterium (A = 2), tritium (A = 3, phóng xạ)."),
("f", "R ≈ 1,2·10⁻¹⁵ · A^(1/3)  (m)"),
("b", "Hệ quả rất đáng chú ý: vì thể tích tỉ lệ với R³ ~ A, khối lượng tỉ lệ với A, nên khối lượng riêng của "
      "mọi hạt nhân đều xấp xỉ như nhau và có giá trị khổng lồ, cỡ 2·10¹⁷ kg/m³ — tức khoảng 200 triệu tấn "
      "trên một centimét khối."),

("h3", "1.3. Đơn vị khối lượng nguyên tử và đơn vị năng lượng"),
("b", "Đơn vị khối lượng nguyên tử u được định nghĩa bằng 1/12 khối lượng của một nguyên tử đồng vị carbon-12: "
      "1 u ≈ 1,66055·10⁻²⁷ kg."),
("b", "Trong vật lí hạt nhân, năng lượng thường đo bằng electronvôn: 1 eV = 1,6·10⁻¹⁹ J; "
      "1 MeV = 10⁶ eV = 1,6·10⁻¹³ J."),
("f", "1 u · c² ≈ 931,5 MeV   ⟹   1 u ≈ 931,5 MeV/c²"),
("tbl", "Bảng 4.1. Một số hằng số cần nhớ của Chương IV",
 ["Đại lượng", "Kí hiệu", "Giá trị"],
 [["Khối lượng proton", "m_p", "1,00728 u"],
  ["Khối lượng neutron", "m_n", "1,00866 u"],
  ["Khối lượng electron", "m_e", "0,00055 u"],
  ["Đơn vị khối lượng nguyên tử", "u", "1,66055·10⁻²⁷ kg ≈ 931,5 MeV/c²"],
  ["Số Avogadro", "N_A", "6,02·10²³ mol⁻¹"],
  ["Tốc độ ánh sáng trong chân không", "c", "3·10⁸ m/s"],
  ["Đơn vị độ phóng xạ", "Bq", "1 Bq = 1 phân rã/giây; 1 Ci = 3,7·10¹⁰ Bq"]]),

("h3", "1.4. Lực hạt nhân"),
("b", "Trong hạt nhân, các proton đẩy nhau rất mạnh bằng lực Coulomb, vậy phải tồn tại một lực hút mạnh hơn "
      "giữ chúng lại — đó là lực hạt nhân (một biểu hiện của tương tác mạnh)."),
("b", "Đặc điểm: (1) là lực hút, mạnh hơn lực đẩy Coulomb rất nhiều; (2) chỉ có tác dụng trong phạm vi rất ngắn, "
      "cỡ kích thước hạt nhân (khoảng 10⁻¹⁵ m), ngoài khoảng đó thì hầu như bằng không; "
      "(3) không phụ thuộc điện tích — lực giữa p–p, p–n, n–n là như nhau; "
      "(4) không cùng bản chất với lực hấp dẫn hay lực tĩnh điện."),
("b", "Hệ quả: hạt nhân càng nhiều proton thì càng cần nhiều neutron để “pha loãng” lực đẩy Coulomb; "
      "vì thế các hạt nhân nặng đều có N > Z và các hạt nhân rất nặng thì không thể bền."),

# =============================================================== §2
("h2", "§2. ĐỘ HỤT KHỐI VÀ NĂNG LƯỢNG LIÊN KẾT"),

("h3", "2.1. Hệ thức Einstein giữa khối lượng và năng lượng"),
("f", "E = m·c²"),
("b", "Một vật có khối lượng m thì có năng lượng nghỉ tương ứng E = mc². Khối lượng và năng lượng là hai mặt "
      "của cùng một thực thể; trong các quá trình hạt nhân, một phần khối lượng có thể chuyển thành năng lượng "
      "và ngược lại."),

("h3", "2.2. Độ hụt khối"),
("f", "Δm = Z·m_p + (A − Z)·m_n − m_hn"),
("b", "Thực nghiệm cho thấy khối lượng của một hạt nhân luôn NHỎ HƠN tổng khối lượng các nucleon tạo thành nó. "
      "Hiệu số đó gọi là độ hụt khối Δm và luôn dương (với mọi hạt nhân bền)."),
("trap", "Sai lầm khái niệm: cho rằng “khối lượng bị mất đi”. Thực chất, khi các nucleon riêng rẽ kết hợp lại "
         "thành hạt nhân, hệ toả ra một năng lượng đúng bằng Δm·c²; do năng lượng giảm nên khối lượng của hệ "
         "giảm tương ứng. Không có gì biến mất — khối lượng đã chuyển thành năng lượng phát ra ngoài."),

("h3", "2.3. Năng lượng liên kết và năng lượng liên kết riêng"),
("f", "E_lk = Δm·c² = [Z·m_p + (A − Z)·m_n − m_hn]·c²"),
("b", "Năng lượng liên kết là năng lượng toả ra khi các nucleon riêng rẽ kết hợp thành hạt nhân; cũng chính là "
      "năng lượng tối thiểu cần cung cấp để phá vỡ hạt nhân thành các nucleon riêng rẽ."),
("f", "ε = E_lk / A   (năng lượng liên kết riêng, tính cho một nucleon)"),
("box", "TIÊU CHUẨN ĐÁNH GIÁ ĐỘ BỀN VỮNG",
 "Hạt nhân có năng lượng liên kết RIÊNG càng lớn thì càng bền vững. Không được dùng năng lượng liên kết "
 "toàn phần E_lk để so sánh độ bền của hai hạt nhân khác số khối."),
("trap", "Bẫy kinh điển: “Hạt nhân uranium-235 có năng lượng liên kết lớn hơn hạt nhân helium-4 nên bền hơn.” "
         "SAI. E_lk của U-235 (≈ 1784 MeV) lớn hơn của He-4 (≈ 28,3 MeV) chỉ vì U-235 có nhiều nucleon hơn; "
         "so sánh đúng phải dùng ε: ε(He-4) ≈ 7,07 MeV/nucleon còn ε(U-235) ≈ 7,59 MeV/nucleon — "
         "và cả hai đều kém bền hơn sắt-56 với ε ≈ 8,79 MeV/nucleon."),

("h3", "2.4. Đường cong năng lượng liên kết riêng – chìa khoá của cả chương"),
("fig", "f19_nllk_rieng", "Hình 4.3. Năng lượng liên kết riêng của các hạt nhân theo số khối A."),
("b", "Đường cong tăng nhanh ở vùng A nhỏ, đạt cực đại ở vùng A ≈ 50 ÷ 95 (đỉnh ở ⁵⁶Fe với ε ≈ 8,79 MeV/nucleon), "
      "rồi giảm chậm về phía các hạt nhân nặng."),
("box", "VÌ SAO CẢ HAI LOẠI PHẢN ỨNG ĐỀU TOẢ NĂNG LƯỢNG",
 "Mọi quá trình đưa hệ hạt nhân tiến về phía đỉnh của đường cong (tức làm tăng năng lượng liên kết riêng "
 "trung bình) đều toả năng lượng.\n"
 "• Hạt nhân rất nặng (A > 200) vỡ thành hai mảnh trung bình → ε tăng → PHÂN HẠCH toả năng lượng.\n"
 "• Hai hạt nhân rất nhẹ (A < 10) kết hợp lại → ε tăng → NHIỆT HẠCH (tổng hợp) toả năng lượng.\n"
 "• Ngược lại, không thể thu năng lượng bằng cách phá vỡ hạt nhân sắt hay tổng hợp từ hạt nhân sắt."),
("b", "Các hạt nhân có số khối là bội của 4 và có Z chẵn, N chẵn như ⁴He, ¹²C, ¹⁶O nằm cao bất thường trên đường "
      "cong — chúng bền hơn hẳn các hạt nhân lân cận. Đây là lí do hạt α (chính là hạt nhân ⁴He) được phát ra "
      "nguyên vẹn trong phóng xạ α."),

# =============================================================== §3
("h2", "§3. PHẢN ỨNG HẠT NHÂN"),

("h3", "3.1. Khái niệm và phân loại"),
("b", "Phản ứng hạt nhân là quá trình biến đổi của các hạt nhân, dẫn tới sự tạo thành các hạt nhân mới."),
("b", "Phản ứng hạt nhân tự phát: hạt nhân không bền tự biến đổi mà không cần tác động bên ngoài — đó chính là "
      "hiện tượng phóng xạ."),
("b", "Phản ứng hạt nhân kích thích: dùng hạt nhẹ (neutron, proton, hạt α…) bắn vào hạt nhân bia để gây phản ứng. "
      "Dạng tổng quát: A + B → C + D."),

("h3", "3.2. Các định luật bảo toàn"),
("box", "BỐN ĐẠI LƯỢNG ĐƯỢC BẢO TOÀN",
 "(1) Bảo toàn số nucleon (số khối): A₁ + A₂ = A₃ + A₄.\n"
 "(2) Bảo toàn điện tích: Z₁ + Z₂ = Z₃ + Z₄.\n"
 "(3) Bảo toàn năng lượng toàn phần (bao gồm cả năng lượng nghỉ).\n"
 "(4) Bảo toàn động lượng."),
("trap", "Ba đại lượng KHÔNG được bảo toàn trong phản ứng hạt nhân — đây là nguồn câu hỏi bẫy dồi dào nhất:\n"
         "• Khối lượng nghỉ: tổng khối lượng trước và sau phản ứng nói chung khác nhau (chính sự chênh lệch đó "
         "tạo ra năng lượng của phản ứng).\n"
         "• Số proton riêng rẽ và số neutron riêng rẽ: trong phân rã β⁻, một neutron biến thành một proton, "
         "nên số proton tăng, số neutron giảm, chỉ có tổng số nucleon là không đổi.\n"
         "• Động năng: động năng trước và sau phản ứng khác nhau, phần chênh lệch lấy từ (hoặc bù vào) năng lượng nghỉ."),

("h3", "3.3. Năng lượng của phản ứng hạt nhân"),
("f", "W = (m_trước − m_sau)·c² = (Δm_sau − Δm_trước)·c² = E_lk(sau) − E_lk(trước)"),
("b", "W > 0: phản ứng TOẢ năng lượng (tổng khối lượng nghỉ giảm; các hạt sinh ra bền vững hơn)."),
("b", "W < 0: phản ứng THU năng lượng — muốn phản ứng xảy ra phải cung cấp năng lượng, thường dưới dạng động năng "
      "của hạt bắn vào."),
("b", "Ba cách tính W đều tương đương; trong thực hành nên chọn cách nào phù hợp với dữ kiện đề cho: đề cho khối "
      "lượng các hạt thì dùng công thức thứ nhất; đề cho độ hụt khối thì dùng công thức thứ hai; đề cho năng lượng "
      "liên kết riêng thì dùng công thức thứ ba với E_lk = ε·A."),

# =============================================================== §4
("h2", "§4. HIỆN TƯỢNG PHÓNG XẠ"),

("h3", "4.1. Định nghĩa và đặc điểm"),
("b", "Phóng xạ là quá trình một hạt nhân không bền vững TỰ PHÁT phân rã, phát ra các tia phóng xạ và biến đổi "
      "thành hạt nhân khác."),
("box", "HAI ĐẶC ĐIỂM BẢN CHẤT",
 "• Tính TỰ PHÁT: quá trình phóng xạ do chính cấu trúc bên trong hạt nhân quyết định, hoàn toàn không phụ thuộc "
 "các tác động bên ngoài như nhiệt độ, áp suất, trạng thái hoá học của mẫu chất hay từ trường.\n"
 "• Tính NGẪU NHIÊN: không thể dự đoán được thời điểm phân rã của một hạt nhân cụ thể; chỉ có thể nói về xác suất "
 "và về quy luật thống kê đối với một số rất lớn hạt nhân."),
("trap", "Vì tính tự phát nói trên, mọi phương án kiểu “đun nóng mẫu chất để làm chậm/tăng tốc phóng xạ”, "
         "“nén mẫu để tăng độ phóng xạ”, “thay đổi chu kì bán rã bằng phản ứng hoá học” đều SAI. "
         "Đây là câu hỏi nhận biết – thông hiểu xuất hiện rất thường xuyên."),

("h3", "4.2. Các loại tia phóng xạ"),
("tbl", "Bảng 4.2. So sánh ba loại tia phóng xạ",
 ["Đặc điểm", "Tia α", "Tia β", "Tia γ"],
 [["Bản chất", "Hạt nhân ⁴₂He", "β⁻: electron ⁰₋₁e; β⁺: positron ⁰₊₁e", "Sóng điện từ (photon) bước sóng rất ngắn"],
  ["Điện tích", "+2e", "−e (β⁻) hoặc +e (β⁺)", "Không mang điện"],
  ["Lệch trong điện/từ trường", "Có, lệch ít (khối lượng lớn)", "Có, lệch nhiều", "Không lệch"],
  ["Khả năng ion hoá", "Rất mạnh", "Trung bình", "Yếu"],
  ["Khả năng đâm xuyên", "Yếu, bị chặn bởi tờ giấy", "Trung bình, bị chặn bởi vài mm nhôm", "Rất mạnh, cần vài cm chì"],
  ["Tốc độ", "≈ 2·10⁷ m/s", "Gần bằng tốc độ ánh sáng", "Bằng tốc độ ánh sáng"],
  ["Thay đổi hạt nhân", "A giảm 4, Z giảm 2", "A không đổi; Z tăng 1 (β⁻) hoặc giảm 1 (β⁺)", "A, Z không đổi"]]),
("fig", "f21_dam_xuyen", "Hình 4.4. So sánh khả năng đâm xuyên của các tia phóng xạ."),
("b", "Quy luật đáng nhớ: khả năng ion hoá và khả năng đâm xuyên biến thiên NGƯỢC chiều nhau. "
      "Tia α ion hoá mạnh nên mất năng lượng rất nhanh, do đó đi được quãng đường ngắn; "
      "tia γ ion hoá yếu nên xuyên sâu."),
("b", "Phương trình các phân rã (X là hạt nhân mẹ, Y là hạt nhân con):"),
("f", "α:  ᴬ_Z X → ⁴₂He + ᴬ⁻⁴_(Z−2) Y"),
("f", "β⁻:  ᴬ_Z X → ⁰₋₁e + ᴬ_(Z+1) Y      (bản chất: n → p + e⁻ + phản neutrino)"),
("f", "β⁺:  ᴬ_Z X → ⁰₊₁e + ᴬ_(Z−1) Y      (bản chất: p → n + e⁺ + neutrino)"),
("trap", "Electron của tia β⁻ KHÔNG phải electron ở lớp vỏ nguyên tử bứt ra; nó được sinh ra ngay trong hạt nhân "
         "từ sự biến đổi của một neutron thành một proton. Đây là nội dung phân biệt bản chất rất hay được hỏi."),
("b", "Tia γ không tồn tại độc lập: nó luôn phát ra kèm theo phân rã α hoặc β, khi hạt nhân con được tạo thành ở "
      "trạng thái kích thích rồi chuyển về trạng thái cơ bản. Vì A và Z không đổi nên phóng xạ γ không phải là "
      "sự biến đổi nguyên tố."),
("fig", "f26_so_do_NZ", "Hình 4.5. Sự dịch chuyển của hạt nhân trên giản đồ (N, Z) ứng với từng loại phân rã."),

("h3", "4.3. Định luật phóng xạ"),
("fig", "f20_dinh_luat_phong_xa", "Hình 4.6. Đồ thị số hạt nhân còn lại theo thời gian."),
("f", "N = N₀·2^(−t/T) = N₀·e^(−λt)      ;      m = m₀·2^(−t/T)"),
("b", "T là chu kì bán rã: khoảng thời gian để một nửa số hạt nhân của mẫu chất phóng xạ bị phân rã. "
      "λ là hằng số phóng xạ, đặc trưng cho từng chất, liên hệ với T bởi:"),
("f", "λ = ln2 / T ≈ 0,693 / T"),
("b", "Số hạt nhân ĐÃ phân rã sau thời gian t: ΔN = N₀ − N = N₀·(1 − 2^(−t/T))."),
("trap", "Ba nhầm lẫn thường gặp về chu kì bán rã:\n"
         "• Cho rằng sau thời gian 2T thì mẫu chất phân rã hết. SAI: sau 2T còn lại 1/4, sau 3T còn 1/8… "
         "về mặt lí thuyết không bao giờ hết hoàn toàn.\n"
         "• Nhầm “số hạt còn lại” với “số hạt đã phân rã”. Đề bài hỏi hai đại lượng này rất khác nhau.\n"
         "• Cho rằng chu kì bán rã phụ thuộc khối lượng mẫu chất. SAI: T là hằng số của mỗi loại hạt nhân."),

("h3", "4.4. Độ phóng xạ"),
("f", "H = λ·N = (ln2/T)·N     ;     H = H₀·2^(−t/T) = H₀·e^(−λt)"),
("b", "Độ phóng xạ (hoạt độ phóng xạ) H của một lượng chất phóng xạ là số phân rã trong một giây. "
      "Đơn vị SI là becơren (Bq): 1 Bq = 1 phân rã/giây. Đơn vị thực dụng: curie (Ci), 1 Ci = 3,7·10¹⁰ Bq."),
("b", "Vì H tỉ lệ với N nên độ phóng xạ cũng giảm theo cùng quy luật hàm mũ với cùng chu kì bán rã T. "
      "Điều này cho phép xác định T bằng thực nghiệm mà không cần đếm số hạt nhân."),
("box", "KĨ THUẬT XỬ LÍ SỐ LIỆU THỰC NGHIỆM (rất hay ra ở phần đúng/sai)",
 "Lấy logarit hai vế của H = H₀e^(−λt) ta được  ln H = ln H₀ − λ·t.\n"
 "Vậy đồ thị lnH theo t là một ĐƯỜNG THẲNG có hệ số góc bằng −λ. Từ hệ số góc suy ra λ rồi suy ra T = ln2/λ. "
 "Việc “tuyến tính hoá” này giúp dùng được nhiều điểm số liệu và giảm sai số so với việc chỉ đọc thời điểm "
 "độ phóng xạ giảm còn một nửa."),
("fig", "f25_semilog", "Hình 4.7. Xử lí số liệu đo độ phóng xạ: đồ thị H(t) và đồ thị tuyến tính hoá lnH(t)."),

("h3", "4.5. Ứng dụng của phóng xạ"),
("b", "Xác định niên đại bằng carbon-14 (T = 5730 năm): tỉ lệ ¹⁴C/¹²C trong khí quyển gần như không đổi; "
      "khi sinh vật còn sống, tỉ lệ này trong cơ thể bằng tỉ lệ trong khí quyển; khi sinh vật chết, ¹⁴C không "
      "được bổ sung nữa mà chỉ phân rã, nên đo độ phóng xạ còn lại sẽ suy ra được tuổi của mẫu vật."),
("b", "Trong y học: chụp ảnh chẩn đoán bằng đồng vị đánh dấu (technetium-99m), xạ trị ung thư bằng nguồn "
      "cobalt-60, khử trùng dụng cụ y tế."),
("b", "Trong công nghiệp và nông nghiệp: kiểm tra khuyết tật mối hàn và đường ống bằng tia γ, đo bề dày vật liệu "
      "trên dây chuyền, chiếu xạ bảo quản nông sản, tạo giống đột biến."),

("h3", "4.6. An toàn phóng xạ"),
("fig", "f24_bien_bao", "Hình 4.8. Biển cảnh báo khu vực có bức xạ ion hoá."),
("b", "Tác hại: các tia phóng xạ gây ion hoá, phá huỷ tế bào và làm biến đổi cấu trúc DNA, có thể gây bỏng phóng xạ, "
      "ung thư và đột biến di truyền. Mức độ tác hại phụ thuộc loại tia, liều lượng và thời gian chiếu."),
("box", "BA NGUYÊN TẮC AN TOÀN PHÓNG XẠ",
 "• THỜI GIAN: giảm tối đa thời gian ở gần nguồn phóng xạ.\n"
 "• KHOẢNG CÁCH: tăng khoảng cách tới nguồn (cường độ bức xạ giảm theo bình phương khoảng cách).\n"
 "• CHE CHẮN: dùng vật liệu chắn thích hợp — giấy, nhựa cho tia α; nhôm, thuỷ tinh hữu cơ cho tia β; "
 "chì hoặc bê tông dày cho tia γ."),
("b", "Ngoài ra: tuân thủ biển báo, đeo liều kế cá nhân, không ăn uống trong khu vực có phóng xạ, "
      "xử lí chất thải phóng xạ theo quy định."),
("trap", "Lưu ý nghịch lí quan trọng: tia α có khả năng đâm xuyên yếu nhất nên chiếu từ BÊN NGOÀI thì ít nguy hiểm "
         "(quần áo, lớp sừng của da đã đủ chặn). Nhưng nếu nguồn α lọt vào BÊN TRONG cơ thể (qua đường hô hấp, "
         "ăn uống) thì lại nguy hiểm nhất, vì khả năng ion hoá rất mạnh và toàn bộ năng lượng bị hấp thụ trong "
         "một thể tích mô nhỏ."),

# =============================================================== §5
("h2", "§5. CÔNG NGHIỆP HẠT NHÂN"),

("h3", "5.1. Phản ứng phân hạch"),
("fig", "f22_phan_hach", "Hình 4.9. Sơ đồ phản ứng phân hạch dây chuyền."),
("b", "Phân hạch là quá trình một hạt nhân rất nặng hấp thụ một neutron chậm rồi vỡ thành hai hạt nhân trung bình, "
      "đồng thời phát ra 2 – 3 neutron và toả năng lượng lớn (khoảng 200 MeV cho mỗi phân hạch của ²³⁵U)."),
("b", "Vì sao dùng neutron CHẬM: neutron không mang điện nên không bị hạt nhân đẩy; neutron càng chậm thì thời "
      "gian ở gần hạt nhân càng lâu, xác suất bị hấp thụ càng lớn. Trong lò phản ứng, người ta dùng chất làm chậm "
      "(nước thường, nước nặng, than chì) để giảm tốc neutron."),
("box", "PHẢN ỨNG DÂY CHUYỀN VÀ HỆ SỐ NHÂN NEUTRON k",
 "k là số neutron trung bình còn lại sau mỗi phân hạch và tiếp tục gây được phân hạch mới.\n"
 "• k < 1: phản ứng dây chuyền tắt dần.\n"
 "• k = 1: phản ứng dây chuyền tự duy trì ở mức ổn định — chế độ làm việc của nhà máy điện hạt nhân.\n"
 "• k > 1: phản ứng tăng vọt không kiểm soát — nguyên lí của bom nguyên tử.\n"
 "Muốn có phản ứng dây chuyền, khối lượng nhiên liệu phải đạt tối thiểu một giá trị gọi là khối lượng tới hạn."),
("b", "Nhà máy điện hạt nhân: lò phản ứng dùng thanh nhiên liệu uranium làm giàu, chất làm chậm, thanh điều khiển "
      "bằng boron hoặc cadmium (hấp thụ bớt neutron để giữ k = 1), chất tải nhiệt đưa nhiệt ra lò sinh hơi, "
      "hơi nước làm quay tuabin – máy phát điện. Toàn bộ được bao bọc bởi lớp bê tông chắn bức xạ."),

("h3", "5.2. Phản ứng nhiệt hạch"),
("fig", "f23_nhiet_hach", "Hình 4.10. Phản ứng tổng hợp hạt nhân deuterium – tritium."),
("b", "Nhiệt hạch (tổng hợp hạt nhân) là quá trình hai hạt nhân rất nhẹ kết hợp thành một hạt nhân nặng hơn và "
      "toả năng lượng. Đây là nguồn năng lượng của Mặt Trời và các ngôi sao."),
("b", "Điều kiện thực hiện: nhiệt độ cực cao (cỡ hàng trăm triệu độ) để các hạt nhân có đủ động năng thắng lực "
      "đẩy Coulomb và tiến đủ gần nhau cho lực hạt nhân phát huy tác dụng; đồng thời mật độ hạt và thời gian duy "
      "trì phải đủ lớn."),
("tbl", "Bảng 4.3. So sánh phân hạch và nhiệt hạch",
 ["Tiêu chí", "Phân hạch", "Nhiệt hạch"],
 [["Bản chất", "Hạt nhân nặng vỡ thành hai mảnh trung bình", "Hai hạt nhân nhẹ kết hợp thành hạt nhân nặng hơn"],
  ["Năng lượng mỗi phản ứng", "Lớn (≈ 200 MeV cho ²³⁵U)", "Nhỏ hơn mỗi phản ứng (≈ 17,6 MeV cho D–T)"],
  ["Năng lượng trên một nucleon", "≈ 0,85 MeV/nucleon", "≈ 3,5 MeV/nucleon — lớn hơn nhiều"],
  ["Nhiên liệu", "Uranium, plutonium — hữu hạn", "Deuterium từ nước biển — gần như vô tận"],
  ["Chất thải phóng xạ", "Nhiều, thời gian bán rã dài", "Rất ít, ít nguy hiểm hơn"],
  ["Điều kiện", "Neutron chậm, khối lượng tới hạn", "Nhiệt độ hàng trăm triệu độ"],
  ["Mức độ làm chủ", "Đã dùng trong nhà máy điện", "Chưa làm chủ ở quy mô thương mại"]]),
("trap", "So sánh đúng cách: xét trên MỖI PHẢN ỨNG thì phân hạch toả nhiều năng lượng hơn (200 MeV so với 17,6 MeV), "
         "nhưng xét trên MỖI ĐƠN VỊ KHỐI LƯỢNG nhiên liệu (mỗi nucleon) thì nhiệt hạch toả nhiều hơn hẳn — "
         "gấp khoảng 4 lần. Đề thi rất hay khai thác sự khác biệt giữa hai cách so sánh này."),

# =============================================================== §6
("h2", "§6. TỔNG KẾT CHƯƠNG IV"),
("tbl", "Bảng 4.4. Hệ thống công thức trọng tâm của Chương IV",
 ["Nội dung", "Công thức", "Lưu ý khi dùng"],
 [["Số neutron", "N = A − Z", "—"],
  ["Bán kính hạt nhân", "R ≈ 1,2·10⁻¹⁵·A^(1/3) m", "Suy ra khối lượng riêng hạt nhân gần như không đổi"],
  ["Số hạt nhân trong m gam", "N = (m/A)·N_A", "A là số khối, tính theo gam"],
  ["Độ hụt khối", "Δm = Z·m_p + (A−Z)·m_n − m_hn", "Luôn dương với hạt nhân bền"],
  ["Năng lượng liên kết", "E_lk = Δm·c²", "Đổi: 1 u·c² = 931,5 MeV"],
  ["Năng lượng liên kết riêng", "ε = E_lk/A", "Dùng để so sánh độ bền vững"],
  ["Bảo toàn trong phản ứng", "ΣA, ΣZ không đổi", "Khối lượng nghỉ KHÔNG bảo toàn"],
  ["Năng lượng phản ứng", "W = (m_trước − m_sau)c²", "W > 0: toả; W < 0: thu"],
  ["Định luật phóng xạ", "N = N₀·2^(−t/T) = N₀e^(−λt)", "t và T phải cùng đơn vị"],
  ["Hằng số phóng xạ", "λ = ln2/T", "Đơn vị nghịch đảo thời gian"],
  ["Số hạt đã phân rã", "ΔN = N₀(1 − 2^(−t/T))", "Phân biệt với số hạt còn lại"],
  ["Độ phóng xạ", "H = λN = H₀·2^(−t/T)", "Đơn vị Bq; 1 Ci = 3,7·10¹⁰ Bq"],
  ["Tuyến tính hoá số liệu", "lnH = lnH₀ − λt", "Hệ số góc của đồ thị lnH(t) bằng −λ"]]),
("box", "MƯỜI LỖI SAI THƯỜNG GẶP NHẤT CỦA CHƯƠNG IV",
 "1. So sánh độ bền vững bằng năng lượng liên kết toàn phần thay vì năng lượng liên kết riêng.\n"
 "2. Cho rằng khối lượng được bảo toàn trong phản ứng hạt nhân.\n"
 "3. Cho rằng số proton hoặc số neutron được bảo toàn riêng rẽ.\n"
 "4. Cho rằng phóng xạ phụ thuộc nhiệt độ, áp suất hoặc trạng thái hoá học.\n"
 "5. Cho rằng sau 2 chu kì bán rã thì chất phóng xạ phân rã hết.\n"
 "6. Nhầm số hạt nhân còn lại với số hạt nhân đã phân rã.\n"
 "7. Không đổi cùng đơn vị thời gian giữa t và T trước khi tính 2^(−t/T).\n"
 "8. Cho rằng tia β⁻ là electron bứt ra từ lớp vỏ nguyên tử.\n"
 "9. Cho rằng tia γ bị lệch trong điện trường hoặc từ trường.\n"
 "10. Kết luận tia α luôn ít nguy hiểm nhất mà quên trường hợp nguồn α xâm nhập vào bên trong cơ thể."),
("exam", "Định hướng ra đề 2026 cho Chương IV: phần trắc nghiệm nhiều lựa chọn tập trung vào cấu tạo hạt nhân, "
         "bản chất các tia phóng xạ, đặc điểm phản ứng phân hạch – nhiệt hạch và an toàn phóng xạ. "
         "Phần đúng/sai thường cho một bối cảnh thực tế (mẫu vật khảo cổ, nguồn xạ trị, bảng số liệu đo độ phóng xạ, "
         "đồ thị đường cong năng lượng liên kết riêng) kèm bốn nhận định cần đánh giá. "
         "Phần trả lời ngắn thường yêu cầu tính năng lượng liên kết riêng, năng lượng toả ra của một phản ứng, "
         "tuổi mẫu vật, khối lượng còn lại hoặc độ phóng xạ sau một khoảng thời gian."),
]
