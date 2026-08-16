# -*- coding: utf-8 -*-
"""BÀI TẬP TÍNH TOÁN – CHƯƠNG IV: VẬT LÍ HẠT NHÂN.
Quy ước hằng số dùng chung: m_p = 1,00728 u; m_n = 1,00866 u; 1 u = 931,5 MeV/c²;
N_A = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J; c = 3·10⁸ m/s.
Các khối lượng hạt nhân cho trong đề là khối lượng HẠT NHÂN (đã trừ khối lượng electron)."""

CALC4 = {

"Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn": [
dict(q="Hạt nhân ²³⁵₉₂U có số neutron bằng",
 o=["92.", "143.", "235.", "327."],
 a="B",
 sol="N = A − Z = 235 − 92 = 143 neutron."),

dict(q="Số hạt nhân có trong 2,0 g uranium ²³⁵U (lấy N_A = 6,02·10²³ mol⁻¹) xấp xỉ",
 o=["5,12·10²¹.", "5,12·10²².", "1,20·10²³.", "6,02·10²³."],
 a="A",
 sol="Số mol: n = m/A = 2,0/235 ≈ 8,51·10⁻³ mol.\n"
     "N = n·N_A = 8,51·10⁻³ · 6,02·10²³ ≈ 5,12·10²¹ hạt nhân."),

dict(q="Cho khối lượng hạt nhân ⁴₂He là 4,0015 u. Độ hụt khối của hạt nhân này xấp xỉ",
 o=["0,0304 u.", "0,0152 u.", "0,3040 u.", "0,0038 u."],
 a="A",
 sol="Δm = 2m_p + 2m_n − m_He = 2·1,00728 + 2·1,00866 − 4,0015\n"
     "  = 2,01456 + 2,01732 − 4,0015 = 4,03188 − 4,0015 = 0,0304 u."),

dict(q="Với độ hụt khối của hạt nhân ⁴₂He là 0,0304 u, năng lượng liên kết của hạt nhân này xấp xỉ",
 o=["7,08 MeV.", "14,2 MeV.", "28,3 MeV.", "56,6 MeV."],
 a="C",
 sol="E_lk = Δm·c² = 0,0304 · 931,5 ≈ 28,3 MeV.\n"
     "Giá trị 7,08 MeV là năng lượng liên kết RIÊNG, không phải năng lượng liên kết toàn phần."),

dict(q="Năng lượng liên kết của hạt nhân ⁴₂He là 28,3 MeV. Năng lượng liên kết riêng của hạt nhân này bằng",
 o=["28,3 MeV/nucleon.", "14,15 MeV/nucleon.", "7,08 MeV/nucleon.", "113,2 MeV/nucleon."],
 a="C",
 sol="ε = E_lk/A = 28,3/4 ≈ 7,08 MeV/nucleon."),

dict(q="Sau khoảng thời gian bằng 3 chu kì bán rã, phần trăm số hạt nhân còn lại của một mẫu chất phóng xạ so với "
       "ban đầu bằng",
 o=["12,5%.", "25%.", "50%.", "87,5%."],
 a="A",
 sol="N/N₀ = 2⁻³ = 1/8 = 0,125 = 12,5%.\n"
     "Giá trị 87,5% là phần ĐÃ phân rã — cần đọc kĩ đề để không nhầm hai đại lượng này."),

dict(q="Một mẫu chất phóng xạ có chu kì bán rã 8 ngày, khối lượng ban đầu 16 g. Sau 24 ngày, khối lượng chất "
       "phóng xạ còn lại là",
 o=["1 g.", "2 g.", "4 g.", "8 g."],
 a="B",
 sol="t/T = 24/8 = 3 nên m = m₀·2⁻³ = 16/8 = 2 g."),

dict(q="Độ phóng xạ ban đầu của một mẫu chất là 4·10⁵ Bq. Sau khoảng thời gian bằng hai chu kì bán rã, độ phóng "
       "xạ của mẫu bằng",
 o=["2·10⁵ Bq.", "10⁵ Bq.", "5·10⁴ Bq.", "0 Bq."],
 a="B",
 sol="H = H₀·2⁻² = 4·10⁵/4 = 10⁵ Bq. Độ phóng xạ giảm theo cùng quy luật và cùng chu kì bán rã với số hạt nhân."),

dict(q="Một chất phóng xạ có chu kì bán rã T = 5,0 giờ. Hằng số phóng xạ của chất này xấp xỉ",
 o=["0,139 giờ⁻¹.", "0,200 giờ⁻¹.", "3,47 giờ⁻¹.", "7,21 giờ⁻¹."],
 a="A",
 sol="λ = ln2/T = 0,693/5,0 ≈ 0,139 giờ⁻¹."),

dict(q="Biết mỗi phân hạch của hạt nhân ²³⁵U toả ra khoảng 200 MeV. Năng lượng toả ra khi 1,0 g ²³⁵U phân hạch "
       "hoàn toàn xấp xỉ",
 o=["8,2·10⁷ J.", "8,2·10¹⁰ J.", "8,2·10¹³ J.", "5,1·10²³ J."],
 a="B",
 sol="Số hạt nhân: N = (1,0/235)·6,02·10²³ ≈ 2,56·10²¹.\n"
     "Năng lượng: E = N · 200 MeV = 2,56·10²¹ · 200 · 1,6·10⁻¹³ J ≈ 8,2·10¹⁰ J.\n"
     "Con số này tương đương năng lượng đốt cháy khoảng 2,7 tấn than đá."),

dict(q="Bán kính của hạt nhân ²⁷₁₃Al, tính theo công thức R ≈ 1,2·10⁻¹⁵·A^(1/3) m, xấp xỉ bằng",
 o=["1,2·10⁻¹⁵ m.", "3,6·10⁻¹⁵ m.", "3,2·10⁻¹⁴ m.", "1,2·10⁻¹⁴ m."],
 a="B",
 sol="A^(1/3) = 27^(1/3) = 3. Vậy R = 1,2·10⁻¹⁵ · 3 = 3,6·10⁻¹⁵ m."),

dict(q="Tỉ số bán kính của hai hạt nhân có số khối lần lượt là 27 và 8 bằng",
 o=["1,5.", "3,4.", "2,25.", "3,375."],
 a="A",
 sol="R tỉ lệ với A^(1/3) nên R₁/R₂ = (27/8)^(1/3) = 3/2 = 1,5.\n"
     "Sai lầm hay gặp là lấy tỉ số 27/8 = 3,375 mà quên khai căn bậc ba."),

dict(q="Trong phản ứng phân hạch ²³⁵₉₂U + ¹₀n → ¹³⁹₅₄Xe + ⁹⁵₃₈Sr + k·¹₀n, giá trị của k là",
 o=["1.", "2.", "3.", "4."],
 a="B",
 sol="Bảo toàn số khối: 235 + 1 = 139 + 95 + k ⟹ 236 = 234 + k ⟹ k = 2.\n"
     "Kiểm tra bảo toàn điện tích: 92 + 0 = 54 + 38 + 0 ⟹ 92 = 92 ✓."),

dict(q="Nếu 1,0 g vật chất được chuyển hoá hoàn toàn thành năng lượng thì năng lượng thu được xấp xỉ",
 o=["9·10¹³ J.", "9·10¹⁶ J.", "3·10⁸ J.", "9·10¹⁰ J."],
 a="A",
 sol="E = mc² = 1,0·10⁻³ · (3·10⁸)² = 10⁻³ · 9·10¹⁶ = 9·10¹³ J.\n"
     "Đây là năng lượng khổng lồ, tương đương khoảng 21 000 tấn thuốc nổ TNT."),

dict(q="Một hạt nhân có độ hụt khối 0,3 u. Năng lượng liên kết của hạt nhân đó bằng",
 o=["27,9 MeV.", "93,15 MeV.", "279,45 MeV.", "2794,5 MeV."],
 a="C",
 sol="E_lk = Δm·c² = 0,3 · 931,5 = 279,45 MeV."),

dict(q="Một mẫu gỗ cổ có độ phóng xạ do ¹⁴C bằng 1/8 độ phóng xạ của mẫu gỗ tươi cùng loại, cùng khối lượng. "
       "Biết chu kì bán rã của ¹⁴C là 5730 năm. Tuổi của mẫu gỗ xấp xỉ",
 o=["5730 năm.", "11 460 năm.", "17 190 năm.", "45 840 năm."],
 a="C",
 sol="H/H₀ = 1/8 = (1/2)³ nên t = 3T = 3 · 5730 = 17 190 năm."),

dict(q="Sau khoảng thời gian đúng bằng một chu kì bán rã, tỉ lệ phần trăm số hạt nhân của mẫu chất phóng xạ ĐÃ "
       "bị phân rã là",
 o=["25%.", "50%.", "75%.", "100%."],
 a="B",
 sol="Sau một chu kì bán rã, còn lại 50% số hạt nhân ban đầu, nên số hạt nhân đã phân rã cũng chiếm 50%."),

dict(q="Cho phản ứng ²₁H + ³₁H → ⁴₂He + ¹₀n với các khối lượng hạt nhân: m_D = 2,01355 u; m_T = 3,01550 u; "
       "m_He = 4,00150 u; m_n = 1,00866 u. Năng lượng toả ra của phản ứng xấp xỉ",
 o=["3,25 MeV.", "17,6 MeV.", "28,3 MeV.", "200 MeV."],
 a="B",
 sol="m_trước = 2,01355 + 3,01550 = 5,02905 u;  m_sau = 4,00150 + 1,00866 = 5,01016 u.\n"
     "Δm = 5,02905 − 5,01016 = 0,01889 u > 0 nên phản ứng toả năng lượng.\n"
     "W = 0,01889 · 931,5 ≈ 17,6 MeV."),
],

"Dạng 2 – Câu trắc nghiệm đúng/sai": [
dict(stem="Cho hạt nhân ⁶₃Li có khối lượng hạt nhân m = 6,01348 u. Biết m_p = 1,00728 u; m_n = 1,00866 u; "
          "1 u = 931,5 MeV/c².",
 items=[
  ("Hạt nhân ⁶₃Li có 3 neutron.", True,
   "Số neutron bằng hiệu giữa số khối và số proton: N = A − Z = 6 − 3 = 3."),
  ("Độ hụt khối của hạt nhân này xấp xỉ 0,0343 u.", True,
   "Δm = 3·1,00728 + 3·1,00866 − 6,01348 = 3,02184 + 3,02598 − 6,01348 = 0,03434 u."),
  ("Năng lượng liên kết của hạt nhân này xấp xỉ 32,0 MeV.", True,
   "E_lk = 0,03434 · 931,5 ≈ 31,99 MeV ≈ 32,0 MeV."),
  ("Năng lượng liên kết riêng của hạt nhân này xấp xỉ 8,0 MeV/nucleon.", False,
   "ε = 31,99/6 ≈ 5,33 MeV/nucleon, nhỏ hơn nhiều so với 8,0 MeV/nucleon. "
   "⁶Li là hạt nhân nhẹ nên nằm ở phần thấp của đường cong năng lượng liên kết riêng."),
 ]),

dict(stem="Một mẫu chất phóng xạ có chu kì bán rã T = 15 giờ và khối lượng ban đầu m₀ = 32 g.",
 fig="f20_dinh_luat_phong_xa",
 items=[
  ("Sau 30 giờ, khối lượng chất phóng xạ còn lại là 8 g.", True,
   "t/T = 30/15 = 2 nên m = 32·2⁻² = 8 g."),
  ("Sau 45 giờ, khối lượng chất phóng xạ đã phân rã là 28 g.", True,
   "t/T = 3 nên còn lại m = 32·2⁻³ = 4 g; khối lượng đã phân rã là 32 − 4 = 28 g."),
  ("Hằng số phóng xạ của chất này xấp xỉ 0,0462 giờ⁻¹.", True, "λ = ln2/T = 0,693/15 ≈ 0,0462 giờ⁻¹."),
  ("Sau 60 giờ, mẫu chất đã phân rã hết hoàn toàn.", False,
   "t/T = 4 nên vẫn còn m = 32·2⁻⁴ = 2 g. Về lí thuyết, mẫu chất không bao giờ phân rã hết."),
 ]),

dict(stem="Một nhà máy điện hạt nhân có công suất điện 500 MW, hiệu suất chuyển hoá từ năng lượng hạt nhân "
          "thành điện năng là 30%. Biết mỗi phân hạch ²³⁵U toả ra 200 MeV; 1 MeV = 1,6·10⁻¹³ J; "
          "N_A = 6,02·10²³ mol⁻¹.",
 fig="f22_phan_hach",
 items=[
  ("Công suất nhiệt mà lò phản ứng phải cung cấp xấp xỉ 1667 MW.", True,
   "P_nhiệt = P_điện/H = 500/0,30 ≈ 1667 MW."),
  ("Số phân hạch xảy ra trong lò mỗi giây xấp xỉ 5,2·10¹⁹.", True,
   "Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
   "Số phân hạch mỗi giây = 1,667·10⁹/3,2·10⁻¹¹ ≈ 5,2·10¹⁹."),
  ("Khối lượng ²³⁵U tiêu thụ mỗi ngày xấp xỉ 1,8 kg.", True,
   "Số phân hạch mỗi ngày: 5,2·10¹⁹ · 86400 ≈ 4,5·10²⁴.\n"
   "m = (4,5·10²⁴/6,02·10²³) · 235 ≈ 7,48 · 235 ≈ 1758 g ≈ 1,8 kg."),
  ("Nếu nâng hiệu suất lên 40% mà vẫn giữ công suất điện 500 MW thì lượng ²³⁵U tiêu thụ mỗi ngày sẽ tăng lên.", False,
   "Hiệu suất cao hơn nghĩa là cần ít năng lượng hạt nhân hơn để tạo ra cùng công suất điện, nên lượng nhiên liệu "
   "tiêu thụ GIẢM (còn khoảng 1,3 kg/ngày)."),
 ]),

dict(stem="Hạt nhân ²³⁸₉₂U phân rã qua một chuỗi các phân rã α và β⁻ để cuối cùng biến thành hạt nhân bền "
          "²⁰⁶₈₂Pb. Chu kì bán rã của ²³⁸U là khoảng 4,5 tỉ năm.",
 fig="f26_so_do_NZ",
 items=[
  ("Trong toàn bộ chuỗi phân rã có 8 phân rã α và 6 phân rã β⁻.", True,
   "Số khối chỉ giảm do phân rã α: (238 − 206)/4 = 8 phân rã α. "
   "Tám phân rã α làm Z giảm 16 (từ 92 còn 76), nhưng Z cuối là 82 nên cần thêm 82 − 76 = 6 phân rã β⁻."),
  ("Khi 1 mol ²³⁸U phân rã hết thành ²⁰⁶Pb thì tổng số hạt α được phát ra là 8·6,02·10²³.", True,
   "Mỗi hạt nhân ²³⁸U phát ra 8 hạt α trong cả chuỗi, mà 1 mol có 6,02·10²³ hạt nhân."),
  ("Trong chuỗi phân rã này có xuất hiện cả phân rã β⁺.", False,
   "Chuỗi này chỉ gồm phân rã α và β⁻. Các hạt nhân nặng dư neutron nên phân rã theo hướng β⁻ "
   "(neutron biến thành proton), chứ không phải β⁺."),
  ("Vì chu kì bán rã của ²³⁸U xấp xỉ tuổi của Trái Đất nên ngày nay ²³⁸U vẫn còn tồn tại đáng kể trong tự nhiên.", True,
   "Trái Đất khoảng 4,6 tỉ năm tuổi, tức chỉ hơn một chu kì bán rã, nên vẫn còn khoảng một nửa lượng ²³⁸U "
   "ban đầu — đó là lí do uranium vẫn khai thác được."),
 ]),

dict(stem="Một nguồn ⁶⁰₂₇Co dùng trong chiếu xạ công nghiệp có độ phóng xạ ban đầu H₀ = 3,7·10¹⁴ Bq và chu kì "
          "bán rã T = 5,27 năm. Biết 1 Ci = 3,7·10¹⁰ Bq.",
 fig="f24_bien_bao",
 items=[
  ("Độ phóng xạ ban đầu của nguồn bằng 10⁴ Ci.", True, "H₀ = 3,7·10¹⁴/3,7·10¹⁰ = 10⁴ Ci."),
  ("Sau 5,27 năm, độ phóng xạ của nguồn còn 1,85·10¹⁴ Bq.", True,
   "Sau đúng một chu kì bán rã, độ phóng xạ giảm còn một nửa: 3,7·10¹⁴/2 = 1,85·10¹⁴ Bq."),
  ("Sau 10,54 năm, độ phóng xạ của nguồn vẫn còn lớn hơn 1,85·10¹⁴ Bq.", False,
   "10,54 năm ứng với 2 chu kì bán rã: H = 3,7·10¹⁴/4 = 9,25·10¹³ Bq, nhỏ hơn 1,85·10¹⁴ Bq."),
  ("Hạt nhân ⁶⁰₂₇Co có 33 neutron.", True, "N = A − Z = 60 − 27 = 33."),
 ]),

dict(stem="Trong phương pháp xác định niên đại bằng ¹⁴C (chu kì bán rã 5730 năm), người ta đo được độ phóng xạ "
          "riêng của một mẫu xương cổ là 12,0 phân rã/phút trên mỗi gam carbon, trong khi mẫu sinh vật còn sống "
          "cùng loại cho giá trị 15,3 phân rã/phút trên mỗi gam carbon.",
 items=[
  ("Tỉ số giữa độ phóng xạ của mẫu xương cổ và mẫu sống xấp xỉ 0,78.", True,
   "H/H₀ = 12,0/15,3 ≈ 0,784. Vì độ phóng xạ riêng tỉ lệ với số hạt nhân ¹⁴C còn lại nên tỉ số này "
   "cũng chính là tỉ số N/N₀."),
  ("Tuổi của mẫu xương cổ vào khoảng 2000 năm.", True,
   "Từ H/H₀ = 2^(−t/T) ⟹ t = T·log₂(H₀/H) = 5730 · log₂(1,275) ≈ 5730 · 0,350 ≈ 2010 năm."),
  ("Nếu độ phóng xạ riêng đo được là 7,65 phân rã/phút trên mỗi gam carbon thì tuổi của mẫu đúng bằng 5730 năm.", True,
   "7,65 = 15,3/2, tức độ phóng xạ giảm còn một nửa, ứng với đúng một chu kì bán rã."),
  ("Có thể dùng phương pháp ¹⁴C để xác định niên đại của các hoá thạch khủng long cách đây khoảng 100 triệu năm.", False,
   "Sau khoảng 50 000 – 60 000 năm (tức hơn 10 chu kì bán rã), lượng ¹⁴C còn lại quá nhỏ để đo chính xác. "
   "Với mẫu hàng triệu năm phải dùng các đồng vị có chu kì bán rã rất dài như ²³⁸U hoặc ⁴⁰K."),
 ]),
],

"Dạng 3 – Câu trả lời ngắn": [
dict(q="Hạt nhân ²⁰⁷₈₂Pb có bao nhiêu neutron?",
 ans="125",
 sol="N = A − Z = 207 − 82 = 125 neutron."),

dict(q="Tính số hạt nhân có trong 4,7 g uranium ²³⁵U. Lấy N_A = 6,02·10²³ mol⁻¹ (kết quả làm tròn đến ba chữ số "
       "có nghĩa, đơn vị: hạt nhân).",
 ans="1,20·10²²",
 sol="Số mol: n = 4,7/235 = 0,020 mol.\nN = 0,020 · 6,02·10²³ = 1,204·10²² ≈ 1,20·10²² hạt nhân."),

dict(q="Cho khối lượng hạt nhân ¹⁶₈O là 15,99052 u; m_p = 1,00728 u; m_n = 1,00866 u. Tính độ hụt khối của hạt "
       "nhân này (đơn vị: u, làm tròn đến năm chữ số thập phân).",
 ans="0,13700 u",
 sol="Δm = 8·1,00728 + 8·1,00866 − 15,99052 = 8,05824 + 8,06928 − 15,99052 = 16,12752 − 15,99052 = 0,13700 u."),

dict(q="Với độ hụt khối của hạt nhân ¹⁶₈O là 0,137 u, tính năng lượng liên kết riêng của hạt nhân này "
       "(đơn vị: MeV/nucleon, làm tròn đến hai chữ số thập phân).",
 ans="7,98 MeV/nucleon",
 sol="E_lk = 0,137 · 931,5 ≈ 127,6 MeV.\nε = E_lk/A = 127,6/16 ≈ 7,98 MeV/nucleon."),

dict(q="Một chất phóng xạ có chu kì bán rã 12 giờ. Sau bao lâu thì số hạt nhân của mẫu chất còn lại 25% so với "
       "ban đầu? (đơn vị: giờ)",
 ans="24 giờ",
 sol="25% = 1/4 = (1/2)² nên t = 2T = 2 · 12 = 24 giờ."),

dict(q="Một chất phóng xạ có chu kì bán rã 4 ngày. Sau 12 ngày, phần trăm số hạt nhân còn lại của mẫu chất so với "
       "ban đầu là bao nhiêu? (đơn vị: %)",
 ans="12,5%",
 sol="t/T = 12/4 = 3 nên N/N₀ = 2⁻³ = 1/8 = 12,5%."),

dict(q="Một chất phóng xạ có chu kì bán rã 30 năm. Tính hằng số phóng xạ của chất này "
       "(đơn vị: năm⁻¹, làm tròn đến bốn chữ số thập phân).",
 ans="0,0231 năm⁻¹",
 sol="λ = ln2/T = 0,693/30 = 0,0231 năm⁻¹."),

dict(q="Một mẫu chất phóng xạ có chu kì bán rã 6 giờ và độ phóng xạ ban đầu 8·10⁶ Bq. Tính độ phóng xạ của mẫu "
       "sau 18 giờ (đơn vị: Bq).",
 ans="10⁶ Bq",
 sol="t/T = 18/6 = 3 nên H = H₀·2⁻³ = 8·10⁶/8 = 10⁶ Bq."),

dict(q="Một mẫu chất phóng xạ ban đầu có 4·10²⁰ hạt nhân. Sau khoảng thời gian bằng hai chu kì bán rã, số hạt "
       "nhân ĐÃ bị phân rã là bao nhiêu?",
 ans="3·10²⁰",
 sol="Số hạt nhân còn lại: N = 4·10²⁰·2⁻² = 10²⁰.\nSố hạt nhân đã phân rã: ΔN = 4·10²⁰ − 10²⁰ = 3·10²⁰."),

dict(q="Một mẫu gỗ cổ có độ phóng xạ do ¹⁴C bằng một nửa độ phóng xạ của mẫu gỗ tươi cùng loại và cùng khối "
       "lượng. Biết chu kì bán rã của ¹⁴C là 5730 năm. Tính tuổi của mẫu gỗ (đơn vị: năm).",
 ans="5730 năm",
 sol="Độ phóng xạ giảm còn một nửa ứng với đúng một chu kì bán rã, nên t = T = 5730 năm."),

dict(q="Tính năng lượng toả ra nếu 2,0 g vật chất được chuyển hoá hoàn toàn thành năng lượng "
       "(lấy c = 3·10⁸ m/s, đơn vị: J).",
 ans="1,8·10¹⁴ J",
 sol="E = mc² = 2,0·10⁻³ · (3·10⁸)² = 2,0·10⁻³ · 9·10¹⁶ = 1,8·10¹⁴ J."),

dict(q="Tính bán kính của hạt nhân ⁶⁴₂₉Cu theo công thức R ≈ 1,2·10⁻¹⁵·A^(1/3) m "
       "(đơn vị: m, làm tròn đến một chữ số thập phân của phần hệ số).",
 ans="4,8·10⁻¹⁵ m",
 sol="A^(1/3) = 64^(1/3) = 4.\nR = 1,2·10⁻¹⁵ · 4 = 4,8·10⁻¹⁵ m."),

dict(q="Tính tỉ số bán kính của hạt nhân ²³⁸U và hạt nhân ⁴He (làm tròn đến một chữ số thập phân).",
 ans="3,9",
 sol="R_U/R_He = (238/4)^(1/3) = (59,5)^(1/3) ≈ 3,9."),

dict(q="Tính năng lượng toả ra khi 1,0 kg ²³⁵U phân hạch hoàn toàn, biết mỗi phân hạch toả 200 MeV "
       "(đơn vị: J, làm tròn đến hai chữ số có nghĩa).",
 ans="8,2·10¹³ J",
 sol="N = (1000/235)·6,02·10²³ ≈ 2,56·10²⁴ hạt nhân.\n"
     "E = 2,56·10²⁴ · 200 · 1,6·10⁻¹³ ≈ 8,2·10¹³ J."),

dict(q="Một mẫu chất phóng xạ chứa 10²⁰ hạt nhân, chu kì bán rã của chất là 10⁸ s. Tính độ phóng xạ của mẫu "
       "(đơn vị: Bq, làm tròn đến hai chữ số có nghĩa).",
 ans="6,9·10¹¹ Bq",
 sol="λ = ln2/T = 0,693/10⁸ = 6,93·10⁻⁹ s⁻¹.\nH = λN = 6,93·10⁻⁹ · 10²⁰ ≈ 6,9·10¹¹ Bq."),

dict(q="Một hạt nhân có năng lượng liên kết 492 MeV. Tính độ hụt khối của hạt nhân đó "
       "(đơn vị: u, làm tròn đến ba chữ số thập phân).",
 ans="0,528 u",
 sol="Δm = E_lk/931,5 = 492/931,5 ≈ 0,528 u."),

dict(q="Trong phản ứng ¹⁴₇N + ⁴₂He → ¹⁷₈O + X, hạt X là hạt gì? (viết kí hiệu đầy đủ)",
 ans="¹₁H (proton)",
 sol="Bảo toàn số khối: 14 + 4 = 17 + A ⟹ A = 1.\nBảo toàn điện tích: 7 + 2 = 8 + Z ⟹ Z = 1.\n"
     "Vậy X là hạt ¹₁H, tức một proton."),

dict(q="Cho khối lượng hạt nhân ⁷₃Li là 7,01436 u; m_p = 1,00728 u; m_n = 1,00866 u. Tính năng lượng liên kết "
       "riêng của hạt nhân ⁷Li (đơn vị: MeV/nucleon, làm tròn đến hai chữ số thập phân).",
 ans="5,61 MeV/nucleon",
 sol="Δm = 3·1,00728 + 4·1,00866 − 7,01436 = 3,02184 + 4,03464 − 7,01436 = 0,04212 u.\n"
     "E_lk = 0,04212 · 931,5 ≈ 39,24 MeV.\nε = 39,24/7 ≈ 5,61 MeV/nucleon."),
],

"Dạng 4 – Bài tập tự luận và vận dụng cao": [
dict(q="Cho khối lượng hạt nhân ⁵⁶₂₆Fe là 55,92066 u và khối lượng hạt nhân ²³⁸₉₂U là 238,00028 u.\n"
       "a) Tính năng lượng liên kết và năng lượng liên kết riêng của mỗi hạt nhân.\n"
       "b) Hạt nhân nào bền vững hơn? Vì sao không thể kết luận chỉ dựa vào năng lượng liên kết toàn phần?\n"
       "c) Từ kết quả trên, hãy giải thích vì sao hạt nhân ²³⁸U có xu hướng phân rã còn ⁵⁶Fe thì không.",
 fig="f19_nllk_rieng",
 ans="a) Fe: 492 MeV và 8,79 MeV/nucleon; U: 1801 MeV và 7,57 MeV/nucleon.  b) ⁵⁶Fe bền vững hơn.",
 sol="a) Với ⁵⁶Fe (Z = 26, N = 30):\n"
     "  Δm = 26·1,00728 + 30·1,00866 − 55,92066 = 26,18928 + 30,25980 − 55,92066 = 0,52842 u\n"
     "  E_lk = 0,52842 · 931,5 ≈ 492,2 MeV;  ε = 492,2/56 ≈ 8,79 MeV/nucleon.\n"
     "  Với ²³⁸U (Z = 92, N = 146):\n"
     "  Δm = 92·1,00728 + 146·1,00866 − 238,00028 = 92,66976 + 147,26436 − 238,00028 = 1,93384 u\n"
     "  E_lk = 1,93384 · 931,5 ≈ 1801,4 MeV;  ε = 1801,4/238 ≈ 7,57 MeV/nucleon.\n"
     "b) ⁵⁶Fe bền vững hơn vì có năng lượng liên kết RIÊNG lớn hơn (8,79 so với 7,57 MeV/nucleon). "
     "Không thể so sánh bằng E_lk toàn phần vì đại lượng này tỉ lệ với số nucleon: ²³⁸U có E_lk lớn gấp gần 4 lần "
     "chỉ vì nó có nhiều hơn 182 nucleon, chứ không phải vì liên kết chặt hơn.\n"
     "c) ⁵⁶Fe nằm ở đỉnh đường cong năng lượng liên kết riêng nên mọi biến đổi (vỡ ra hay kết hợp thêm) đều làm "
     "ε giảm, tức phải THU năng lượng — do đó nó bền vững. Ngược lại, ²³⁸U nằm ở phía bên phải đỉnh nên khi phân rã "
     "hoặc phân hạch, các sản phẩm có ε lớn hơn, quá trình TOẢ năng lượng và xảy ra tự phát."),

dict(q="Một mẫu quặng chứa ²³⁸U (chu kì bán rã 4,5·10⁹ năm) và sản phẩm cuối cùng bền là ²⁰⁶Pb. Giả thiết toàn bộ "
       "chì trong mẫu đều do uranium phân rã tạo ra và mẫu không mất mát chất nào. Người ta đo được tỉ số số hạt "
       "nhân ²⁰⁶Pb trên số hạt nhân ²³⁸U trong mẫu bằng 0,6.\n"
       "a) Lập biểu thức liên hệ giữa tỉ số N_Pb/N_U và thời gian t.\n"
       "b) Tính tuổi của mẫu quặng.\n"
       "c) Nêu một giả thiết có thể bị vi phạm trong thực tế và ảnh hưởng của nó đến kết quả.",
 ans="b) t ≈ 3,05·10⁹ năm.",
 sol="a) Gọi N₀ là số hạt nhân ²³⁸U ban đầu. Sau thời gian t: N_U = N₀·2^(−t/T) và mỗi hạt nhân U đã phân rã tạo "
     "ra đúng một hạt nhân Pb, nên N_Pb = N₀ − N_U.\n"
     "  Do đó: N_Pb/N_U = (N₀ − N_U)/N_U = N₀/N_U − 1 = 2^(t/T) − 1.\n"
     "b) Từ 2^(t/T) − 1 = 0,6 suy ra 2^(t/T) = 1,6, do đó t/T = log₂1,6 = ln1,6/ln2 ≈ 0,4700/0,6931 ≈ 0,678.\n"
     "  t = 0,678 · 4,5·10⁹ ≈ 3,05·10⁹ năm, tức khoảng 3,05 tỉ năm.\n"
     "c) Giả thiết dễ bị vi phạm nhất là “mẫu quặng là hệ kín”. Nếu trong quá trình địa chất một phần chì bị rửa "
     "trôi thì N_Pb đo được nhỏ hơn thực tế, dẫn tới tuổi tính được NHỎ hơn tuổi thật; ngược lại nếu mẫu có sẵn "
     "một lượng chì ban đầu không do phân rã thì tuổi tính được sẽ LỚN hơn tuổi thật."),

dict(q="Một nhà máy điện hạt nhân có công suất điện 1000 MW, hiệu suất chuyển hoá năng lượng hạt nhân thành "
       "điện năng là 33%. Mỗi phân hạch ²³⁵U toả ra 200 MeV.\n"
       "a) Tính công suất nhiệt của lò phản ứng.\n"
       "b) Tính số phân hạch xảy ra mỗi giây.\n"
       "c) Tính khối lượng ²³⁵U mà nhà máy tiêu thụ trong một ngày.\n"
       "d) So sánh với lượng than đá cần thiết để tạo ra cùng lượng điện năng, biết 1 kg than toả 3·10⁷ J và "
       "nhà máy nhiệt điện than có hiệu suất 40%.",
 fig="f22_phan_hach",
 ans="a) ≈ 3030 MW.  b) ≈ 9,5·10¹⁹ phân hạch/s.  c) ≈ 3,2 kg.  d) khoảng 7200 tấn than.",
 sol="a) P_nhiệt = P_điện/H = 1000/0,33 ≈ 3030 MW = 3,03·10⁹ W.\n"
     "b) Năng lượng mỗi phân hạch: 200 · 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
     "  Số phân hạch mỗi giây: 3,03·10⁹/3,2·10⁻¹¹ ≈ 9,5·10¹⁹.\n"
     "c) Số phân hạch trong một ngày: 9,5·10¹⁹ · 86400 ≈ 8,2·10²⁴.\n"
     "  Số mol tương ứng: 8,2·10²⁴/6,02·10²³ ≈ 13,6 mol ⟹ m = 13,6 · 235 ≈ 3195 g ≈ 3,2 kg.\n"
     "d) Điện năng trong một ngày: W = 10⁹ · 86400 = 8,64·10¹³ J.\n"
     "  Nhiệt năng cần từ than: 8,64·10¹³/0,40 = 2,16·10¹⁴ J.\n"
     "  Khối lượng than: 2,16·10¹⁴/3·10⁷ = 7,2·10⁶ kg = 7200 tấn.\n"
     "  Nhận xét: chỉ hơn 3 kg uranium thay thế được hơn 7000 tấn than mỗi ngày — chênh nhau khoảng hai triệu lần "
     "về khối lượng. Đó là ưu thế nổi bật của năng lượng hạt nhân, đi kèm thách thức về an toàn và chất thải "
     "phóng xạ."),

dict(q="Một nhóm học sinh đo độ phóng xạ H của một mẫu chất theo thời gian và thu được bảng số liệu sau:\n"
       "t (giờ):   0     2     4     6     8\n"
       "H (Bq):  1000   707   500   354   250\n"
       "a) Chứng tỏ rằng số liệu phù hợp với định luật phóng xạ và xác định chu kì bán rã của mẫu chất.\n"
       "b) Trình bày cách xác định chu kì bán rã bằng đồ thị lnH theo t và tính hằng số phóng xạ λ.\n"
       "c) Vì sao phương pháp tuyến tính hoá (vẽ lnH theo t) cho kết quả đáng tin cậy hơn so với việc chỉ đọc "
       "trực tiếp một cặp số liệu?",
 fig="f25_semilog",
 ans="a) T = 4 giờ.  b) λ ≈ 0,173 giờ⁻¹.",
 sol="a) So sánh các giá trị: H(0) = 1000 Bq, H(4) = 500 Bq = H(0)/2, H(8) = 250 Bq = H(4)/2. "
     "Cứ sau mỗi 4 giờ độ phóng xạ lại giảm một nửa, đúng như quy luật H = H₀·2^(−t/T). Vậy T = 4 giờ.\n"
     "  (Kiểm tra thêm: H(2) = 1000·2^(−0,5) = 1000/1,414 ≈ 707 Bq ✓)\n"
     "b) Lấy logarit tự nhiên: lnH = lnH₀ − λt. Vẽ đồ thị lnH theo t sẽ được một đường thẳng có hệ số góc bằng −λ.\n"
     "  Dùng hai điểm đầu và cuối: lnH(0) = ln1000 ≈ 6,908; lnH(8) = ln250 ≈ 5,521.\n"
     "  Hệ số góc: (5,521 − 6,908)/(8 − 0) = −1,387/8 ≈ −0,173 ⟹ λ ≈ 0,173 giờ⁻¹.\n"
     "  Kiểm tra: T = ln2/λ = 0,693/0,173 ≈ 4,0 giờ ✓\n"
     "c) Vì phương pháp tuyến tính hoá sử dụng TẤT CẢ các điểm số liệu để dựng một đường thẳng khớp nhất, "
     "nên các sai số ngẫu nhiên của từng phép đo được bù trừ lẫn nhau. Ngược lại, nếu chỉ dùng một cặp số liệu "
     "thì sai số của riêng hai phép đo đó truyền thẳng vào kết quả. Ngoài ra, việc đồ thị có thẳng hay không "
     "còn là bằng chứng kiểm tra chính quy luật hàm mũ."),

dict(q="Xét phản ứng tổng hợp hạt nhân: ²₁H + ²₁H → ³₂He + ¹₀n, toả ra năng lượng 3,25 MeV cho mỗi phản ứng.\n"
       "a) Tính số phản ứng xảy ra khi 1,0 g deuterium tham gia phản ứng hoàn toàn.\n"
       "b) Tính năng lượng toả ra khi đó.\n"
       "c) So sánh với năng lượng toả ra khi phân hạch hoàn toàn 1,0 g ²³⁵U (biết mỗi phân hạch toả 200 MeV) và "
       "giải thích kết quả bằng đường cong năng lượng liên kết riêng.",
 fig="f23_nhiet_hach",
 ans="a) ≈ 1,5·10²³ phản ứng.  b) ≈ 7,8·10¹⁰ J.  c) Lớn hơn khoảng 5% so với 8,2·10¹⁰ J của U-235.",
 sol="a) Số hạt nhân deuterium trong 1,0 g: N_D = (1,0/2)·6,02·10²³ = 3,01·10²³.\n"
     "  Mỗi phản ứng tiêu thụ 2 hạt nhân D nên số phản ứng: N_pư = 3,01·10²³/2 ≈ 1,5·10²³.\n"
     "b) E = 1,5·10²³ · 3,25 · 1,6·10⁻¹³ ≈ 7,8·10¹⁰ J.\n"
     "c) Với 1,0 g ²³⁵U: E' ≈ 8,2·10¹⁰ J (đã tính ở phần trước). Hai giá trị khá gần nhau, thậm chí uranium "
     "còn nhỉnh hơn một chút với phản ứng D–D này.\n"
     "  Tuy vậy nếu xét theo phản ứng D–T (toả 17,6 MeV cho 5 nucleon, tức 3,5 MeV/nucleon) thì nhiệt hạch vượt "
     "trội hẳn so với phân hạch (0,85 MeV/nucleon). Nguyên nhân nằm ở đường cong năng lượng liên kết riêng: "
     "đoạn đi lên ở vùng A nhỏ rất DỐC, nên tổng hợp các hạt nhân nhẹ làm ε tăng mạnh; còn đoạn đi xuống ở vùng "
     "A lớn rất THOẢI, nên phân hạch chỉ làm ε tăng ít. Thêm vào đó, nhiên liệu deuterium có thể tách từ nước biển "
     "nên gần như vô tận."),

dict(q="Một mẫu ²²⁶Ra tinh khiết có khối lượng 1,00 g được đo thấy có độ phóng xạ 3,7·10¹⁰ Bq.\n"
       "a) Tính số hạt nhân ²²⁶Ra có trong mẫu.\n"
       "b) Tính hằng số phóng xạ và chu kì bán rã của ²²⁶Ra (ra kết quả theo năm; lấy 1 năm ≈ 3,156·10⁷ s).\n"
       "c) Nếu để mẫu này trong 1600 năm thì độ phóng xạ còn lại xấp xỉ bao nhiêu?",
 ans="a) 2,66·10²¹ hạt nhân.  b) λ ≈ 1,39·10⁻¹¹ s⁻¹; T ≈ 1580 năm.  c) ≈ 1,9·10¹⁰ Bq.",
 sol="a) N = (m/A)·N_A = (1,00/226) · 6,02·10²³ ≈ 2,66·10²¹ hạt nhân.\n"
     "b) Từ H = λN suy ra λ = H/N = 3,7·10¹⁰/2,66·10²¹ ≈ 1,39·10⁻¹¹ s⁻¹.\n"
     "  T = ln2/λ = 0,693/1,39·10⁻¹¹ ≈ 4,99·10¹⁰ s.\n"
     "  Đổi ra năm: T = 4,99·10¹⁰/3,156·10⁷ ≈ 1580 năm (giá trị thực nghiệm là khoảng 1600 năm).\n"
     "c) 1600 năm xấp xỉ đúng một chu kì bán rã, nên độ phóng xạ còn khoảng một nửa: "
     "H ≈ 3,7·10¹⁰/2 ≈ 1,9·10¹⁰ Bq.\n"
     "Ghi chú lịch sử: chính giá trị độ phóng xạ của 1 g radium đã được lấy làm định nghĩa ban đầu của đơn vị "
     "curie (1 Ci = 3,7·10¹⁰ Bq)."),

dict(q="Một kĩ thuật viên phải làm việc gần một nguồn phóng xạ γ. Người đó cân nhắc hai phương án:\n"
       "  Phương án A: đứng cách nguồn 1,0 m trong 10 phút.\n"
       "  Phương án B: đứng cách nguồn 4,0 m trong 60 phút.\n"
       "Biết cường độ bức xạ tỉ lệ nghịch với bình phương khoảng cách và liều nhận được tỉ lệ với tích của cường "
       "độ bức xạ và thời gian chiếu.\n"
       "a) Lập biểu thức so sánh liều nhận được trong hai phương án.\n"
       "b) Phương án nào an toàn hơn và an toàn hơn bao nhiêu lần?\n"
       "c) Nêu thêm một biện pháp có thể áp dụng để giảm liều mà không cần thay đổi thời gian hay khoảng cách.",
 fig="f24_bien_bao",
 ans="b) Phương án B an toàn hơn khoảng 2,7 lần.",
 sol="a) Liều D tỉ lệ với t/d². Đặt hệ số tỉ lệ là k:\n"
     "  D_A = k · 10/1,0² = 10k;  D_B = k · 60/4,0² = 60k/16 = 3,75k.\n"
     "b) D_A/D_B = 10/3,75 ≈ 2,67. Vậy cách làm việc ở xa 4,0 m cho liều nhỏ hơn khoảng 2,7 lần, an toàn hơn — "
     "dù thời gian làm việc dài gấp 6 lần. Điều này cho thấy yếu tố KHOẢNG CÁCH có tác dụng rất mạnh vì cường độ "
     "giảm theo bình phương khoảng cách.\n"
     "c) Áp dụng nguyên tắc CHE CHẮN: đặt một tấm chì (hoặc tường bê tông) giữa người và nguồn. Với tia γ, "
     "chì là vật liệu che chắn hiệu quả nhờ khối lượng riêng lớn. Đây là nguyên tắc thứ ba bên cạnh thời gian "
     "và khoảng cách."),

dict(q="Một bệnh viện nhận về một nguồn ⁹⁹ᵐTc dùng để chụp ảnh chẩn đoán, có chu kì bán rã 6,0 giờ và độ phóng xạ "
       "ban đầu 8,0·10⁹ Bq lúc 6 giờ sáng.\n"
       "a) Tính độ phóng xạ của nguồn lúc 12 giờ trưa và lúc 6 giờ chiều cùng ngày.\n"
       "b) Ca chụp cần nguồn có độ phóng xạ tối thiểu 1,0·10⁹ Bq. Hỏi có thể sử dụng nguồn này muộn nhất đến "
       "mấy giờ trong ngày?\n"
       "c) Giải thích vì sao trong y học chẩn đoán người ta ưu tiên dùng đồng vị có chu kì bán rã ngắn "
       "(vài giờ) thay vì đồng vị có chu kì bán rã rất dài.",
 ans="a) 4,0·10⁹ Bq lúc 12 giờ trưa và 2,0·10⁹ Bq lúc 6 giờ chiều.  b) Muộn nhất đến 0 giờ (nửa đêm) ngày hôm sau.",
 sol="a) Từ 6 giờ sáng đến 12 giờ trưa là 6,0 giờ = 1 chu kì bán rã: H = 8,0·10⁹/2 = 4,0·10⁹ Bq.\n"
     "  Từ 6 giờ sáng đến 6 giờ chiều là 12 giờ = 2 chu kì bán rã: H = 8,0·10⁹/4 = 2,0·10⁹ Bq.\n"
     "b) Cần H ≥ 1,0·10⁹ Bq, tức H₀/H ≤ 8 = 2³, ứng với t ≤ 3T = 18 giờ. "
     "Vậy có thể dùng đến 6 giờ sáng + 18 giờ = 0 giờ (nửa đêm) của ngày hôm sau.\n"
     "c) Đồng vị có chu kì bán rã ngắn cho độ phóng xạ đủ mạnh để ghi hình rõ nét trong thời gian chụp, "
     "nhưng sau đó suy giảm rất nhanh nên bệnh nhân chỉ chịu liều chiếu trong thời gian ngắn. "
     "Nếu dùng đồng vị chu kì bán rã dài, chất phóng xạ sẽ tồn tại trong cơ thể hàng tháng hoặc hàng năm, "
     "gây tổn hại tích luỹ không cần thiết. Đây là sự dung hoà giữa chất lượng hình ảnh và an toàn phóng xạ."),
],
}
