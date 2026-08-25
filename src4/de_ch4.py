# -*- coding: utf-8 -*-
"""NĂM ĐỀ KIỂM TRA CHƯƠNG IV – VẬT LÍ HẠT NHÂN (Vật lí 12, GDPT 2018).

Cấu trúc mỗi đề giống hệt đề thi tốt nghiệp THPT môn Vật lí (Quyết định
764/QĐ-BGDĐT): 28 câu / 40 lệnh hỏi / 50 phút
    • Phần I : 18 câu trắc nghiệm nhiều phương án lựa chọn
    • Phần II:  4 câu trắc nghiệm đúng/sai, mỗi câu 4 ý
    • Phần III: 6 câu trả lời ngắn

Phạm vi: Bài 20 (Cấu trúc hạt nhân) → Bài 23 (Công nghiệp hạt nhân) của sách Kết
nối tri thức: cấu tạo hạt nhân và đồng vị; độ hụt khối, năng lượng liên kết và
năng lượng liên kết riêng; phản ứng hạt nhân; hiện tượng phóng xạ và định luật
phóng xạ; phân hạch, nhiệt hạch và an toàn bức xạ.

Hằng số dùng thống nhất: m_p = 1,00728 u; m_n = 1,00866 u; 1 u = 931,5 MeV/c²;
N_A = 6,02·10²³ mol⁻¹; 1 MeV = 1,6·10⁻¹³ J; c = 3·10⁸ m/s; ln2 ≈ 0,693.
"""

HANG_SO = ("Cho biết: khối lượng proton m_p = 1,00728 u; khối lượng neutron "
           "m_n = 1,00866 u; 1 u = 931,5 MeV/c²; số Avogadro N_A = 6,02·10²³ mol⁻¹; "
           "1 eV = 1,6·10⁻¹⁹ J và 1 MeV = 1,6·10⁻¹³ J; tốc độ ánh sáng trong chân không "
           "c = 3·10⁸ m/s; ln2 ≈ 0,693. Bỏ qua động năng của các hạt trước phản ứng nếu "
           "đề không nói rõ.")


# ===================================================================================
#                        ĐỀ SỐ 01 – CẤU TRÚC HẠT NHÂN
# ===================================================================================

DE1_P1 = [
    dict(q="Hạt nhân nguyên tử được cấu tạo từ",
         o=["các proton và các neutron.", "các proton và các electron.",
            "các neutron và các electron.", "các proton, neutron và electron."],
         a="A",
         sol="Hạt nhân gồm các nuclon, tức các proton (mang điện dương) và các neutron "
             "(không mang điện). Electron không nằm trong hạt nhân mà chuyển động ở lớp "
             "vỏ, xung quanh hạt nhân."),

    dict(q="Hình vẽ là mô hình cấu tạo của một nguyên tử. Hạt mang điện tích dương trong "
           "hạt nhân là",
         fig="t41a",
         o=["proton.", "neutron.", "electron.", "nuclon."],
         a="A",
         sol="Trong hạt nhân, proton mang điện tích +e còn neutron trung hoà về điện. "
             "Electron mang điện âm nhưng nằm ở lớp vỏ. “Nuclon” là tên gọi chung cho cả "
             "proton lẫn neutron nên không chỉ riêng hạt mang điện dương."),

    dict(q="Trong kí hiệu hạt nhân ᴬ_Z X, các đại lượng A và Z lần lượt là",
         o=["số khối (số nuclon) và số proton.",
            "số proton và số neutron.",
            "số neutron và số khối.",
            "số electron và số proton."],
         a="A",
         sol="A là số khối, bằng tổng số nuclon (proton và neutron) trong hạt nhân; Z là "
             "số proton, cũng là số thứ tự của nguyên tố trong bảng tuần hoàn. Số neutron "
             "được tính bằng N = A − Z."),

    dict(q="Hạt nhân ²³₁₁Na có",
         o=["11 proton và 12 neutron.", "11 proton và 23 neutron.",
            "12 proton và 11 neutron.", "23 proton và 11 neutron."],
         a="A",
         sol="Z = 11 nên hạt nhân có 11 proton; A = 23 nên số neutron là "
             "N = A − Z = 23 − 11 = 12."),

    dict(q="Các hạt nhân đồng vị là những hạt nhân",
         o=["có cùng số proton nhưng khác số neutron.",
            "có cùng số neutron nhưng khác số proton.",
            "có cùng số khối nhưng khác số proton.",
            "có cùng cả số proton lẫn số neutron."],
         a="A",
         sol="Đồng vị là những hạt nhân của cùng một nguyên tố (cùng Z, tức cùng số "
             "proton) nhưng có số neutron khác nhau, do đó số khối A khác nhau. Ví dụ "
             "¹²C, ¹³C và ¹⁴C đều là đồng vị của carbon."),

    dict(q="Đơn vị khối lượng nguyên tử u được định nghĩa bằng",
         o=["1/12 khối lượng của một nguyên tử đồng vị ¹²C.",
            "khối lượng của một nguyên tử hydrogen.",
            "khối lượng của một proton ở trạng thái nghỉ.",
            "1/12 khối lượng của một hạt nhân đồng vị ¹⁶O."],
         a="A",
         sol="Theo quy ước quốc tế, 1 u bằng 1/12 khối lượng của một nguyên tử carbon-12, "
             "xấp xỉ 1,66·10⁻²⁷ kg. Khối lượng proton (1,00728 u) và neutron (1,00866 u) "
             "đều gần bằng 1 u nhưng không đúng bằng 1 u."),

    dict(q="Độ hụt khối của một hạt nhân ᴬ_Z X có khối lượng m được tính bằng",
         o=["Δm = Z·m_p + (A − Z)·m_n − m.",
            "Δm = m − Z·m_p − (A − Z)·m_n.",
            "Δm = A·m_p + Z·m_n − m.",
            "Δm = Z·m_p + A·m_n − m."],
         a="A",
         sol="Độ hụt khối là hiệu giữa tổng khối lượng các nuclon khi còn riêng rẽ và "
             "khối lượng của hạt nhân đã tạo thành:\n"
             "Δm = Z·m_p + (A − Z)·m_n − m.\n"
             "Với mọi hạt nhân bền, Δm luôn dương: khối lượng hạt nhân nhỏ hơn tổng khối "
             "lượng các nuclon riêng lẻ."),

    dict(q="Năng lượng liên kết của một hạt nhân có độ hụt khối Δm được tính bằng",
         o=["E_lk = Δm·c².", "E_lk = Δm/c².",
            "E_lk = Δm·c.", "E_lk = Δm²·c."],
         a="A",
         sol="Theo hệ thức Einstein giữa khối lượng và năng lượng, E_lk = Δm·c². Nếu Δm "
             "tính theo u thì có thể dùng ngay 1 u = 931,5 MeV/c², khi đó E_lk (MeV) "
             "= Δm (u) × 931,5."),

    dict(q="Hình vẽ mô tả thí nghiệm tán xạ hạt α của Rutherford. Kết quả thí nghiệm này "
           "cho thấy",
         fig="t41b",
         o=["nguyên tử có một hạt nhân rất nhỏ, mang điện dương và tập trung hầu hết khối "
            "lượng.",
            "điện tích dương phân bố đều trong toàn bộ thể tích của nguyên tử.",
            "electron chuyển động trên những quỹ đạo tròn có bán kính xác định.",
            "hạt nhân nguyên tử được cấu tạo từ proton và neutron."],
         a="A",
         sol="Phần lớn hạt α đi thẳng qua lá vàng chứng tỏ nguyên tử hầu như rỗng; một số "
             "rất ít bị lệch mạnh hoặc bật ngược trở lại chứng tỏ có một tâm rất nhỏ, "
             "mang điện dương và rất nặng — đó là hạt nhân. Thí nghiệm này không cho biết "
             "gì về neutron (được phát hiện muộn hơn nhiều) hay về quỹ đạo electron."),

    dict(q="Năng lượng liên kết riêng của một hạt nhân được tính bằng ε = E_lk/A. Hạt "
           "nhân có năng lượng liên kết riêng càng lớn thì",
         o=["càng bền vững.", "càng kém bền vững.",
            "càng có số khối lớn.", "càng dễ bị phóng xạ."],
         a="A",
         sol="Năng lượng liên kết riêng là năng lượng liên kết tính trung bình cho mỗi "
             "nuclon, nên nó chính là thước đo mức độ bền vững của hạt nhân: ε càng lớn "
             "thì muốn tách một nuclon ra khỏi hạt nhân càng phải tốn nhiều năng lượng."),

    dict(q="Hình vẽ là đồ thị năng lượng liên kết riêng theo số khối. Các hạt nhân bền "
           "vững nhất nằm ở vùng có số khối",
         fig="t41c",
         o=["khoảng 50 – 80.", "nhỏ hơn 10.",
            "khoảng 100 – 150.", "lớn hơn 200."],
         a="A",
         sol="Đồ thị đạt cực đại (khoảng 8,8 MeV/nucleon) ở vùng số khối A ≈ 50 – 80, "
             "quanh sắt và nickel. Đây chính là lí do các hạt nhân rất nặng có xu hướng "
             "phân hạch còn các hạt nhân rất nhẹ có xu hướng kết hợp (nhiệt hạch): cả hai "
             "quá trình đều đưa hệ về phía vùng bền vững hơn."),

    dict(q="So sánh kích thước của hạt nhân với kích thước của nguyên tử, ta thấy bán "
           "kính hạt nhân",
         o=["nhỏ hơn bán kính nguyên tử khoảng mười nghìn lần.",
            "xấp xỉ bằng bán kính của nguyên tử.",
            "lớn hơn bán kính nguyên tử khoảng mười nghìn lần.",
            "nhỏ hơn bán kính nguyên tử khoảng mười lần."],
         a="A",
         sol="Bán kính hạt nhân cỡ 10⁻¹⁵ – 10⁻¹⁴ m, còn bán kính nguyên tử cỡ 10⁻¹⁰ m, "
             "tức chênh nhau khoảng 10⁴ – 10⁵ lần. Vì thế nguyên tử hầu như rỗng, phù hợp "
             "với kết quả thí nghiệm tán xạ của Rutherford."),

    dict(q="Hạt nhân ⁴₂He có khối lượng 4,0015 u. Năng lượng liên kết của hạt nhân này "
           "xấp xỉ",
         o=["28,3 MeV.", "14,2 MeV.", "7,08 MeV.", "56,6 MeV."],
         a="A",
         sol="Độ hụt khối:\n"
             "Δm = 2 × 1,00728 + 2 × 1,00866 − 4,0015 = 4,03188 − 4,0015 = 0,03038 u.\n"
             "Năng lượng liên kết: E_lk = 0,03038 × 931,5 ≈ 28,3 MeV.\n"
             "Con số 7,08 MeV chính là năng lượng liên kết RIÊNG (E_lk/A), không phải "
             "năng lượng liên kết."),

    dict(q="Vẫn với hạt nhân ⁴₂He nói trên, năng lượng liên kết riêng của nó xấp xỉ",
         o=["7,07 MeV/nucleon.", "28,3 MeV/nucleon.",
            "14,2 MeV/nucleon.", "3,54 MeV/nucleon."],
         a="A",
         sol="ε = E_lk/A = 28,3/4 ≈ 7,07 MeV/nucleon.\n"
             "Đây là một giá trị khá lớn so với các hạt nhân nhẹ lân cận, cho thấy hạt "
             "nhân helium-4 rất bền — điều này giải thích vì sao nó được phát ra nguyên "
             "vẹn trong phóng xạ α."),

    dict(q="Số neutron có trong hạt nhân ²³⁵₉₂U là",
         o=["143.", "92.", "235.", "327."],
         a="A",
         sol="Số khối A = 235 là tổng số nuclon, còn Z = 92 là số proton, nên số "
             "neutron là\n"
             "N = A − Z = 235 − 92 = 143 neutron.\n"
             "Tỉ số N/Z ≈ 1,55 cho thấy hạt nhân nặng cần rất nhiều neutron “thừa” để "
             "cân bằng lực đẩy Coulomb giữa các proton."),

    dict(q="Số nguyên tử có trong 2,0 g helium (khối lượng mol 4,0 g/mol) xấp xỉ",
         o=["3,01·10²³.", "6,02·10²³.",
            "1,20·10²⁴.", "1,51·10²³."],
         a="A",
         sol="Số mol: n = m/M = 2,0/4,0 = 0,50 mol.\n"
             "Số nguyên tử: N = n·N_A = 0,50 × 6,02·10²³ = 3,01·10²³."),

    dict(q="Một hạt nhân có độ hụt khối 0,30 u. Năng lượng liên kết của hạt nhân đó xấp xỉ",
         o=["279 MeV.", "31 MeV.", "2795 MeV.", "93 MeV."],
         a="A",
         sol="Dùng trực tiếp quy đổi 1 u = 931,5 MeV/c² nên không cần đổi Δm ra "
             "kilôgam:\n"
             "E_lk = Δm·c² = 0,30 × 931,5 = 279,45 MeV ≈ 279 MeV.\n"
             "Đây là bậc độ lớn điển hình của năng lượng liên kết một hạt nhân trung "
             "bình."),

    dict(q="Phát biểu nào sau đây là đúng khi so sánh mức độ bền vững của các hạt nhân?",
         o=["Hạt nhân có số khối lớn hơn không nhất thiết bền vững hơn.",
            "Hạt nhân có số khối càng lớn thì càng bền vững.",
            "Hạt nhân có năng lượng liên kết càng lớn thì càng bền vững.",
            "Mọi hạt nhân có cùng số khối đều bền vững như nhau."],
         a="A",
         sol="Thước đo độ bền vững là năng lượng liên kết RIÊNG ε = E_lk/A chứ không phải "
             "số khối hay năng lượng liên kết. Chẳng hạn ²³⁸U có E_lk rất lớn (khoảng "
             "1800 MeV) nhưng ε chỉ khoảng 7,6 MeV/nucleon, kém bền hơn ⁵⁶Fe có E_lk chỉ "
             "khoảng 492 MeV nhưng ε tới 8,8 MeV/nucleon."),
]

DE1_P2 = [
    dict(stem="Hình vẽ là mô hình cấu tạo của một nguyên tử, gồm hạt nhân ở giữa và các "
              "electron chuyển động xung quanh.",
         fig="t41a",
         items=[
             ("Hạt nhân gồm các proton mang điện dương và các neutron không mang điện.",
              True,
              "Đó là cấu tạo cơ bản của hạt nhân. Hai loại hạt này được gọi chung là "
              "nuclon và liên kết với nhau bằng lực hạt nhân."),
             ("Trong một nguyên tử trung hoà về điện, số electron ở lớp vỏ bằng số proton "
              "trong hạt nhân.", True,
              "Mỗi electron mang điện −e, mỗi proton mang +e. Nguyên tử trung hoà nghĩa "
              "là tổng điện tích bằng 0, nên số electron phải bằng số proton, tức bằng Z."),
             ("Khối lượng của nguyên tử tập trung chủ yếu ở lớp vỏ electron.", False,
              "Ngược lại, khối lượng tập trung gần như hoàn toàn ở hạt nhân. Khối lượng "
              "một electron chỉ bằng khoảng 1/1836 khối lượng một proton, nên toàn bộ lớp "
              "vỏ chỉ chiếm một phần rất nhỏ khối lượng nguyên tử."),
             ("Kích thước của hạt nhân xấp xỉ bằng kích thước của cả nguyên tử.", False,
              "Bán kính hạt nhân cỡ 10⁻¹⁴ m, còn bán kính nguyên tử cỡ 10⁻¹⁰ m — chênh "
              "nhau khoảng mười nghìn lần. Nếu phóng to nguyên tử bằng một sân vận động "
              "thì hạt nhân chỉ bằng một hạt đậu ở giữa sân."),
         ]),

    dict(stem="Hình vẽ mô tả thí nghiệm tán xạ hạt α trên lá vàng mỏng do Rutherford và "
              "các cộng sự thực hiện.",
         fig="t41b",
         items=[
             ("Phần lớn các hạt α đi thẳng qua lá vàng, chứng tỏ nguyên tử hầu như rỗng.",
              True,
              "Nếu vật chất đặc kín thì các hạt α đã bị chặn lại hoặc lệch hướng hàng "
              "loạt. Việc đa số đi thẳng cho thấy giữa các hạt nhân là không gian gần như "
              "trống rỗng."),
             ("Một số rất ít hạt α bị bật ngược trở lại, chứng tỏ trong nguyên tử có một "
              "tâm rất nhỏ, mang điện dương và rất nặng.", True,
              "Muốn đẩy ngược một hạt α đang bay nhanh thì vật cản phải vừa đẩy nó (cùng "
              "dấu điện tích, tức mang điện dương) vừa nặng hơn nó nhiều lần. Chính suy "
              "luận này đã dẫn Rutherford tới mô hình hạt nhân nguyên tử."),
             ("Các hạt α bị lệch hướng là do va chạm với các electron trong nguyên tử "
              "vàng.", False,
              "Electron nhẹ hơn hạt α khoảng 7000 lần nên va chạm với electron gần như "
              "không làm hạt α đổi hướng, giống như viên bi thép va vào hạt bụi. Nguyên "
              "nhân gây lệch là lực đẩy Coulomb của hạt nhân mang điện dương."),
             ("Thí nghiệm này cho phép xác định trực tiếp số neutron trong hạt nhân "
              "vàng.", False,
              "Thí nghiệm chỉ cho biết về sự tồn tại, kích thước và điện tích của hạt "
              "nhân. Neutron mãi tới năm 1932 mới được Chadwick phát hiện, sau thí nghiệm "
              "của Rutherford hơn hai mươi năm."),
         ]),

    dict(stem="Xét hạt nhân ⁷₃Li có khối lượng 7,0160 u.",
         items=[
             ("Hạt nhân này có 3 proton và 4 neutron.", True,
              "Trong kí hiệu ⁷₃Li, chỉ số dưới Z = 3 cho biết số proton, chỉ số trên "
              "A = 7 là số khối. Số neutron: N = A − Z = 7 − 3 = 4."),
             ("Độ hụt khối của hạt nhân là 0,0421 u.", False,
              "Δm = 3 × 1,00728 + 4 × 1,00866 − 7,0160\n"
              "   = 3,02184 + 4,03464 − 7,0160 = 7,05648 − 7,0160 = 0,0405 u,\n"
              "chứ không phải 0,0421 u."),
             ("Năng lượng liên kết của hạt nhân xấp xỉ 37,7 MeV.", True,
              "Dùng độ hụt khối đúng Δm = 0,0405 u vừa tính ở ý trên:\n"
              "E_lk = Δm × 931,5 = 0,0405 × 931,5 ≈ 37,7 MeV.\n"
              "Đây là năng lượng cần cung cấp để tách hạt nhân ⁷Li thành 7 nuclon "
              "riêng rẽ."),
             ("Năng lượng liên kết riêng của hạt nhân xấp xỉ 12,6 MeV/nucleon.", False,
              "Phải chia cho SỐ KHỐI A = 7 chứ không phải cho số proton Z = 3:\n"
              "ε = 37,7/7 ≈ 5,39 MeV/nucleon.\n"
              "Con số 12,6 MeV/nucleon chính là 37,7/3, tức kết quả sai do dùng nhầm Z."),
         ]),

    dict(stem="Hình vẽ là đồ thị năng lượng liên kết riêng ε theo số khối A của các hạt "
              "nhân.",
         fig="t41c",
         items=[
             ("Các hạt nhân có số khối càng lớn thì càng bền vững.", False,
              "Đồ thị cho thấy ε tăng ở vùng số khối nhỏ, đạt cực đại quanh A ≈ 56 rồi "
              "GIẢM dần về phía số khối lớn. Vì vậy các hạt nhân rất nặng như uranium lại "
              "kém bền hơn sắt."),
             ("Hạt nhân ²³⁸U có năng lượng liên kết riêng lớn hơn hạt nhân ⁵⁶Fe.", False,
              "Đọc trên đồ thị: ε(²³⁸U) ≈ 7,6 MeV/nucleon còn ε(⁵⁶Fe) ≈ 8,8 MeV/nucleon. "
              "Vậy uranium có ε NHỎ hơn sắt, tức kém bền hơn."),
             ("Năng lượng liên kết của ²³⁸U lớn hơn năng lượng liên kết của ⁵⁶Fe.", True,
              "E_lk = ε·A nên:\n"
              "E_lk(²³⁸U) ≈ 7,6 × 238 ≈ 1810 MeV; E_lk(⁵⁶Fe) ≈ 8,8 × 56 ≈ 493 MeV.\n"
              "Đây là chỗ cần phân biệt rõ: năng lượng liên kết TỔNG của uranium lớn hơn, "
              "nhưng tính trên mỗi nuclon thì nó lại nhỏ hơn."),
             ("Hạt nhân deuterium ²H kém bền vững hơn hạt nhân ⁴He.", True,
              "Trên đồ thị, ε(²H) ≈ 1,1 MeV/nucleon, thấp hơn hẳn ε(⁴He) ≈ 7,1 "
              "MeV/nucleon. Chênh lệch lớn này chính là nguồn năng lượng của phản ứng "
              "nhiệt hạch tổng hợp helium từ các hạt nhân nhẹ."),
         ]),
]

DE1_P3 = [
    dict(q="Hạt nhân ²³⁵₉₂U có bao nhiêu neutron?",
         ans="143",
         sol="Trong kí hiệu ²³⁵₉₂U, số khối A = 235 là tổng số nuclon và Z = 92 là số "
             "proton, nên\n"
             "N = A − Z = 235 − 92 = 143 neutron."),

    dict(q="Hạt nhân ⁴₂He có khối lượng 4,0015 u. Tính độ hụt khối của hạt nhân này (theo "
           "10⁻² u, làm tròn đến hàng phần trăm).",
         ans="3,04",
         sol="Δm = Z·m_p + (A − Z)·m_n − m\n"
             "   = 2 × 1,00728 + 2 × 1,00866 − 4,0015\n"
             "   = 2,01456 + 2,01732 − 4,0015 = 4,03188 − 4,0015 = 0,03038 u.\n"
             "Vậy Δm = 3,038·10⁻² u ≈ 3,04·10⁻² u."),

    dict(q="Hạt nhân ⁷₃Li có khối lượng 7,0160 u. Tính năng lượng liên kết của hạt nhân "
           "này (theo MeV, làm tròn đến hàng phần mười).",
         ans="37,7",
         sol="Δm = 3 × 1,00728 + 4 × 1,00866 − 7,0160 = 7,05648 − 7,0160 = 0,04048 u.\n"
             "E_lk = Δm × 931,5 = 0,04048 × 931,5 ≈ 37,7 MeV."),

    dict(q="Hạt nhân ¹⁶₈O có khối lượng 15,9905 u. Tính năng lượng liên kết riêng của hạt "
           "nhân này (theo MeV/nucleon, làm tròn đến hàng phần trăm).",
         ans="7,98",
         sol="Δm = 8 × 1,00728 + 8 × 1,00866 − 15,9905\n"
             "   = 8,05824 + 8,06928 − 15,9905 = 16,12752 − 15,9905 = 0,13702 u.\n"
             "E_lk = 0,13702 × 931,5 ≈ 127,6 MeV.\n"
             "ε = E_lk/A = 127,6/16 ≈ 7,98 MeV/nucleon."),

    dict(q="Tính số nguyên tử có trong 2,0 g helium, biết khối lượng mol của helium là "
           "4,0 g/mol. (Kết quả theo 10²³ nguyên tử, làm tròn đến hàng phần trăm.)",
         ans="3,01",
         sol="Số mol: n = m/M = 2,0/4,0 = 0,50 mol.\n"
             "Số nguyên tử: N = n·N_A = 0,50 × 6,02·10²³ = 3,01·10²³."),

    dict(q="Một hạt nhân có độ hụt khối 0,30 u. Tính năng lượng liên kết của hạt nhân đó "
           "(theo MeV, làm tròn đến hàng đơn vị).",
         ans="279",
         sol="E_lk = Δm·c² = 0,30 × 931,5 = 279,45 MeV ≈ 279 MeV.\n"
             "Ở đây ta dùng trực tiếp 1 u = 931,5 MeV/c² nên không cần đổi Δm ra "
             "kilôgam."),
]

DE1 = dict(code="C4-01", so="01", chuong=4,
           title="ĐỀ KIỂM TRA CHƯƠNG IV – ĐỀ SỐ 01",
           subtitle="Chương IV – Vật lí hạt nhân",
           p1=DE1_P1, p2=DE1_P2, p3=DE1_P3)


# ===================================================================================
#                    ĐỀ SỐ 02 – HIỆN TƯỢNG PHÓNG XẠ
# ===================================================================================

DE2_P1 = [
    dict(q="Hiện tượng phóng xạ là quá trình",
         o=["hạt nhân không bền vững tự phát phân rã và phát ra tia phóng xạ.",
            "hạt nhân hấp thụ neutron rồi vỡ thành hai mảnh nhẹ hơn.",
            "hai hạt nhân nhẹ kết hợp lại thành một hạt nhân nặng hơn.",
            "nguyên tử mất bớt electron ở lớp vỏ và trở thành ion dương."],
         a="A",
         sol="Phóng xạ là quá trình TỰ PHÁT: hạt nhân không bền vững tự biến đổi thành "
             "hạt nhân khác, đồng thời phát ra các tia α, β hoặc γ. Việc hạt nhân hấp thụ "
             "neutron rồi vỡ ra là phân hạch, còn việc hai hạt nhân nhẹ kết hợp là nhiệt "
             "hạch — cả hai đều không tự phát."),

    dict(q="Tia α là dòng các hạt",
         o=["nhân helium ⁴₂He.", "electron.", "positron.", "photon năng lượng cao."],
         a="A",
         sol="Tia α là dòng hạt nhân helium ⁴₂He, mang điện tích +2e và có khối lượng khá "
             "lớn. Electron là tia β⁻, positron là tia β⁺, còn photon năng lượng cao "
             "chính là tia γ."),

    dict(q="Hạt được phát ra từ hạt nhân trong phóng xạ β⁻ là",
         o=["electron.", "proton.", "neutron.", "hạt nhân helium."],
         a="A",
         sol="Tia β⁻ là dòng electron ⁰₋₁e phát ra từ hạt nhân, sinh ra khi một neutron "
             "trong hạt nhân biến thành một proton. Electron này không phải electron của "
             "lớp vỏ nguyên tử."),

    dict(q="Tia γ có bản chất là",
         o=["sóng điện từ có bước sóng rất ngắn.",
            "dòng hạt mang điện tích dương.",
            "dòng hạt mang điện tích âm.",
            "dòng neutron chuyển động rất nhanh."],
         a="A",
         sol="Tia γ là bức xạ điện từ có bước sóng cực ngắn (nhỏ hơn 10⁻¹¹ m), không mang "
             "điện nên không bị lệch trong điện trường hay từ trường. Chính vì không mang "
             "điện và có năng lượng lớn nên nó đâm xuyên rất mạnh."),

    dict(q="Định luật phóng xạ được biểu diễn bằng công thức",
         o=["N = N₀·2^(−t/T).", "N = N₀·2^(t/T).",
            "N = N₀·(1 − t/T).", "N = N₀/(1 + t/T)."],
         a="A",
         sol="N = N₀·2^(−t/T) = N₀·e^(−λt), với T là chu kì bán rã và λ = ln2/T. Sau mỗi "
             "khoảng thời gian bằng T, số hạt nhân chưa phân rã giảm đi một nửa. Quy luật "
             "này là hàm mũ chứ không phải hàm bậc nhất."),

    dict(q="Chu kì bán rã của một chất phóng xạ là",
         o=["thời gian để một nửa số hạt nhân của mẫu bị phân rã.",
            "thời gian để toàn bộ số hạt nhân của mẫu bị phân rã.",
            "thời gian sống trung bình của một hạt nhân trong mẫu.",
            "khoảng thời gian giữa hai lần phân rã liên tiếp."],
         a="A",
         sol="Theo định nghĩa, sau mỗi chu kì bán rã T thì số hạt nhân phóng xạ còn lại "
             "giảm đi một nửa. Về lí thuyết mẫu chất không bao giờ phân rã hết hoàn toàn, "
             "vì sau mỗi T lại còn lại một nửa của phần trước."),

    dict(q="Hình vẽ mô tả ba chùm tia phóng xạ phát ra từ cùng một nguồn, đi vào vùng "
           "điện trường đều giữa hai bản kim loại tích điện trái dấu (hình vẽ không theo "
           "tỉ lệ). Ba chùm (1), (2), (3) lần lượt là",
         fig="t42d",
         o=["tia α, tia γ và tia β.", "tia β, tia γ và tia α.",
            "tia γ, tia α và tia β.", "tia α, tia β và tia γ."],
         a="A",
         sol="Chùm (2) đi thẳng nên không mang điện: đó là tia γ.\n"
             "Chùm (1) lệch về phía bản âm nên mang điện DƯƠNG: đó là tia α (điện tích "
             "+2e).\n"
             "Chùm (3) lệch về phía bản dương nên mang điện ÂM: đó là tia β⁻ (dòng "
             "electron).\n"
             "Ngoài ra, độ lệch tỉ lệ với thương q/m: hạt β nhẹ hơn hạt α hàng nghìn lần "
             "nên lệch mạnh hơn hẳn, phù hợp với hình vẽ."),

    dict(q="Tia α có khả năng đâm xuyên yếu nhất trong ba loại tia phóng xạ vì",
         o=["hạt α có khối lượng lớn và điện tích lớn nên bị hãm mạnh trong vật chất.",
            "hạt α chuyển động với tốc độ lớn hơn hẳn các hạt khác.",
            "hạt α không mang điện nên không tương tác với vật chất.",
            "hạt α có năng lượng nhỏ hơn nhiều so với tia β và tia γ."],
         a="A",
         sol="Hạt α mang điện tích +2e và có khối lượng gấp khoảng 7000 lần electron, nên "
             "khi đi qua vật chất nó ion hoá rất mạnh các nguyên tử trên đường đi và mất "
             "năng lượng rất nhanh. Chính khả năng ion hoá mạnh này khiến quãng đường đi "
             "của nó rất ngắn, chỉ vài xentimét trong không khí."),

    dict(q="Trong phân rã α, so với hạt nhân mẹ thì hạt nhân con có",
         o=["số khối giảm 4 đơn vị và số proton giảm 2 đơn vị.",
            "số khối giảm 2 đơn vị và số proton giảm 4 đơn vị.",
            "số khối không đổi và số proton giảm 2 đơn vị.",
            "số khối giảm 4 đơn vị và số proton không đổi."],
         a="A",
         sol="Hạt α chính là ⁴₂He, mang đi 4 nuclon trong đó có 2 proton. Áp dụng bảo "
             "toàn số nuclon và bảo toàn điện tích: A giảm 4 và Z giảm 2. Ví dụ: "
             "²³⁸₉₂U → ⁴₂He + ²³⁴₉₀Th."),

    dict(q="Sau một phân rã β⁻, hạt nhân con khác hạt nhân mẹ ở chỗ nó có",
         o=["số khối không đổi và số proton tăng 1 đơn vị.",
            "số khối không đổi và số proton giảm 1 đơn vị.",
            "số khối giảm 1 đơn vị và số proton không đổi.",
            "cả số khối lẫn số proton đều tăng 1 đơn vị."],
         a="A",
         sol="Trong hạt nhân, một neutron biến thành một proton và phát ra một electron: "
             "¹₀n → ¹₁p + ⁰₋₁e. Tổng số nuclon vẫn là A nhưng số proton tăng thêm 1. Ví "
             "dụ: ¹⁴₆C → ⁰₋₁e + ¹⁴₇N."),

    dict(q="Hình vẽ là đồ thị phần trăm số hạt nhân còn lại của một mẫu chất phóng xạ "
           "theo thời gian. Sau một chu kì bán rã, phần trăm số hạt nhân còn lại là",
         fig="t42b",
         o=["50 %.", "25 %.", "75 %.", "100 %."],
         a="A",
         sol="Theo định nghĩa của chu kì bán rã, sau mỗi khoảng thời gian T thì số hạt "
             "nhân còn lại giảm đi một nửa, tức còn 50 %. Trên đồ thị, đó là điểm ứng với "
             "t = 6 ngày."),

    dict(q="Có thể làm thay đổi tốc độ phân rã của một mẫu chất phóng xạ bằng cách nào "
           "sau đây?",
         o=["Không có cách nào trong các cách nêu ở đây.",
            "Nung nóng mẫu chất tới nhiệt độ vài trăm độ C.",
            "Nén mẫu chất phóng xạ dưới áp suất rất lớn.",
            "Tăng khối lượng ban đầu của mẫu chất phóng xạ."],
         a="A",
         sol="Không cách nào trong ba cách nêu trên làm thay đổi được tốc độ phân rã. "
             "Phóng xạ là một quá trình xảy ra bên trong hạt nhân, ở thang năng lượng cỡ "
             "MeV, trong khi các tác động hoá học hay nhiệt học chỉ ở thang eV — nhỏ hơn "
             "hàng triệu lần. Vì vậy chu kì bán rã là một hằng số đặc trưng cho từng loại "
             "hạt nhân, không thể thay đổi bằng các biện pháp thông thường."),

    dict(q="Từ đồ thị ở Câu 11, chu kì bán rã của chất phóng xạ này là",
         fig="t42b",
         o=["6 ngày.", "3 ngày.", "12 ngày.", "9 ngày."],
         a="A",
         sol="Đọc trên đồ thị: phần trăm số hạt nhân còn lại giảm từ 100 % xuống 50 % sau "
             "6 ngày, rồi tiếp tục xuống 25 % sau 12 ngày. Vậy chu kì bán rã T = 6 ngày."),

    dict(q="Cũng theo đồ thị đó, sau 18 ngày phần trăm số hạt nhân còn lại là",
         o=["12,5 %.", "25 %.", "6,25 %.", "16,7 %."],
         a="A",
         sol="18 ngày ứng với 18/6 = 3 chu kì bán rã.\n"
             "Phần còn lại: (1/2)³ = 1/8 = 12,5 %."),

    dict(q="Hạt nhân ²³⁸₉₂U phóng xạ α. Hạt nhân con tạo thành là",
         o=["²³⁴₉₀Th.", "²³⁴₉₂U.", "²³⁸₉₀Th.", "²³⁴₈₈Ra."],
         a="A",
         sol="Bảo toàn số nuclon: 238 = 4 + A ⇒ A = 234.\n"
             "Bảo toàn điện tích: 92 = 2 + Z ⇒ Z = 90, tức nguyên tố thorium.\n"
             "Vậy hạt nhân con là ²³⁴₉₀Th."),

    dict(q="Hạt nhân ¹⁴₆C phóng xạ β⁻. Hạt nhân con tạo thành là",
         o=["¹⁴₇N.", "¹⁴₅B.", "¹³₆C.", "¹⁰₄Be."],
         a="A",
         sol="Bảo toàn số nuclon: 14 = 0 + A ⇒ A = 14.\n"
             "Bảo toàn điện tích: 6 = (−1) + Z ⇒ Z = 7, tức nguyên tố nitrogen.\n"
             "Vậy hạt nhân con là ¹⁴₇N. Đây chính là phản ứng được dùng trong phương pháp "
             "xác định niên đại bằng carbon phóng xạ."),

    dict(q="Một mẫu chất phóng xạ có chu kì bán rã 8 ngày. Sau 24 ngày, số hạt nhân phóng "
           "xạ còn lại trong mẫu bằng",
         o=["1/8 số hạt nhân ban đầu.", "1/3 số hạt nhân ban đầu.",
            "1/16 số hạt nhân ban đầu.", "1/24 số hạt nhân ban đầu."],
         a="A",
         sol="24 ngày ứng với 24/8 = 3 chu kì bán rã.\n"
             "N/N₀ = (1/2)³ = 1/8.\n"
             "Sai lầm thường gặp là lấy 24/8 = 3 rồi kết luận “còn 1/3” — quy luật ở đây "
             "là hàm mũ chứ không phải tỉ lệ nghịch."),

    dict(q="Sau khoảng thời gian bằng hai lần chu kì bán rã, phần trăm số hạt nhân của "
           "một mẫu phóng xạ đã bị phân rã là",
         o=["75 %.", "25 %.", "50 %.", "100 %."],
         a="A",
         sol="Sau 2T, số hạt nhân còn lại là (1/2)² = 1/4 = 25 % số ban đầu.\n"
             "Phần đã phân rã: 100 % − 25 % = 75 %.\n"
             "Chú ý phân biệt “còn lại” và “đã phân rã” — đây là chỗ rất dễ nhầm."),
]

DE2_P2 = [
    dict(stem="Hình vẽ so sánh khả năng đâm xuyên của ba loại tia phóng xạ α, β và γ qua "
              "các vật liệu khác nhau.",
         fig="t42a",
         items=[
             ("Tia α bị chặn lại bởi một tờ giấy mỏng.", True,
              "Hạt α ion hoá rất mạnh nên mất hết năng lượng chỉ sau một quãng đường rất "
              "ngắn: vài xentimét trong không khí hoặc một tờ giấy."),
             ("Tia γ có khả năng đâm xuyên mạnh nhất trong ba loại tia.", True,
              "Tia γ không mang điện và có năng lượng lớn nên tương tác với vật chất yếu "
              "hơn nhiều so với tia α và tia β; muốn chắn nó phải dùng lớp chì dày hoặc "
              "bê tông."),
             ("Tia β là dòng hạt nhân helium chuyển động với tốc độ rất lớn.", False,
              "Dòng hạt nhân helium chính là tia α. Tia β⁻ là dòng ELECTRON (và tia β⁺ là "
              "dòng positron) phát ra từ hạt nhân."),
             ("Loại tia nào đâm xuyên càng mạnh thì khả năng ion hoá môi trường của nó "
              "càng mạnh.", False,
              "Quan hệ là NGƯỢC lại. Tia α ion hoá rất mạnh nên mất năng lượng cực nhanh "
              "và đâm xuyên yếu nhất; tia γ ion hoá yếu nên đi được rất sâu vào vật "
              "chất. Chính vì thế nguồn α nằm ngoài cơ thể thì gần như vô hại, nhưng nếu "
              "hít hay nuốt phải lại rất nguy hiểm."),
         ]),

    dict(stem="Hình vẽ là đồ thị phần trăm số hạt nhân còn lại của một mẫu chất phóng xạ "
              "theo thời gian.",
         fig="t42b",
         items=[
             ("Chu kì bán rã của chất phóng xạ này là 6 ngày.", True,
              "Đọc trên đồ thị: sau 6 ngày còn 50 %, sau 12 ngày còn 25 %, sau 18 ngày "
              "còn 12,5 %. Khoảng thời gian để số hạt nhân giảm đi một nửa luôn là 6 "
              "ngày."),
             ("Sau 12 ngày, trong mẫu còn lại 25 % số hạt nhân ban đầu.", True,
              "12 ngày = 2 chu kì bán rã, nên phần còn lại là (1/2)² = 1/4 = 25 %."),
             ("Sau 18 ngày, số hạt nhân đã bị phân rã chiếm 12,5 % số hạt nhân ban đầu.",
              False,
              "12,5 % là phần CÒN LẠI sau 18 ngày (3 chu kì bán rã). Phần đã phân rã là "
              "100 % − 12,5 % = 87,5 %."),
             ("Sau 24 ngày, trong mẫu không còn hạt nhân phóng xạ nào.", False,
              "Sau 24 ngày = 4 chu kì bán rã, phần còn lại là (1/2)⁴ = 6,25 %. Về mặt lí "
              "thuyết, quy luật hàm mũ khiến số hạt nhân không bao giờ giảm về đúng bằng "
              "0."),
         ]),

    dict(stem="Xét các quá trình phân rã phóng xạ.",
         items=[
             ("Trong phân rã α, hạt nhân con có số khối nhỏ hơn hạt nhân mẹ 4 đơn vị.",
              True,
              "Hạt α là ⁴₂He nên mang đi 4 nuclon. Theo bảo toàn số nuclon, số khối của "
              "hạt nhân con giảm đúng 4 đơn vị."),
             ("Trong phân rã β⁻, số proton của hạt nhân giảm đi 1 đơn vị.", False,
              "Ngược lại, số proton TĂNG thêm 1: một neutron trong hạt nhân biến thành "
              "một proton và phát ra electron. Số khối thì không đổi. Chỉ trong phân rã "
              "β⁺ số proton mới giảm đi 1."),
             ("Trong phân rã β⁻, electron phát ra được lấy từ lớp vỏ electron của nguyên "
              "tử.", False,
              "Electron này được SINH RA ngay trong hạt nhân, theo quá trình "
              "¹₀n → ¹₁p + ⁰₋₁e (kèm một phản neutrino). Nó không liên quan gì tới các "
              "electron ở lớp vỏ."),
             ("Phóng xạ γ không làm thay đổi số proton và số neutron của hạt nhân.", True,
              "Phóng xạ γ chỉ là sự chuyển của hạt nhân từ trạng thái kích thích về trạng "
              "thái có năng lượng thấp hơn, kèm phát ra photon. Cấu tạo hạt nhân (A và Z) "
              "giữ nguyên, nên tia γ thường đi kèm sau một phân rã α hoặc β."),
         ]),

    dict(stem="Một mẫu chất phóng xạ có chu kì bán rã T = 8,0 ngày, khối lượng ban đầu "
              "40 g.",
         items=[
             ("Sau 4,0 ngày, khối lượng chất phóng xạ còn lại là 20 g.", False,
              "4,0 ngày chỉ là NỬA chu kì bán rã chứ không phải một chu kì:\n"
              "m = 40 × 2^(−4/8) = 40 × 2^(−0,5) = 40/1,414 ≈ 28,3 g.\n"
              "Khối lượng 20 g chỉ đạt được sau trọn 8,0 ngày."),
             ("Sau 24 ngày, khối lượng chất phóng xạ còn lại là 5,0 g.", True,
              "24 ngày = 3 chu kì bán rã, nên m = 40 × (1/2)³ = 40/8 = 5,0 g."),
             ("Sau 16 ngày, khối lượng chất đã bị phân rã là 10 g.", False,
              "16 ngày = 2 chu kì bán rã, khối lượng CÒN LẠI là 40/4 = 10 g. Khối lượng "
              "ĐÃ PHÂN RÃ là 40 − 10 = 30 g. Đây là chỗ dễ nhầm giữa hai đại lượng."),
             ("Sau 40 ngày, khối lượng chất phóng xạ còn lại nhỏ hơn 2,0 g.", True,
              "40 ngày = 5 chu kì bán rã, nên m = 40 × (1/2)⁵ = 40/32 = 1,25 g < 2,0 g."),
         ]),
]

DE2_P3 = [
    dict(q="Từ đồ thị ở Câu 11, hãy xác định chu kì bán rã của chất phóng xạ (theo ngày, "
           "làm tròn đến hàng đơn vị).",
         fig="t42b",
         ans="6",
         sol="Đọc trên đồ thị: phần trăm số hạt nhân còn lại giảm từ 100 % xuống 50 % sau "
             "6 ngày. Đó chính là định nghĩa của chu kì bán rã: T = 6 ngày.\n"
             "Có thể kiểm tra lại: sau 12 ngày còn 25 %, sau 18 ngày còn 12,5 % — hoàn "
             "toàn phù hợp."),

    dict(q="Một mẫu chất phóng xạ có chu kì bán rã 12 giờ. Tính phần trăm số hạt nhân còn "
           "lại trong mẫu sau 36 giờ (theo %, làm tròn đến hàng phần mười).",
         ans="12,5",
         sol="Số chu kì bán rã đã trôi qua: t/T = 36/12 = 3.\n"
             "N/N₀ = (1/2)³ = 1/8 = 0,125 = 12,5 %."),

    dict(q="Hạt nhân ²³⁸₉₂U phóng xạ α tạo thành một hạt nhân con. Hạt nhân con đó có bao "
           "nhiêu proton?",
         ans="90",
         sol="Phương trình phân rã: ²³⁸₉₂U → ⁴₂He + ᴬ_Z X.\n"
             "Bảo toàn điện tích: 92 = 2 + Z ⇒ Z = 90.\n"
             "(Đồng thời bảo toàn số nuclon cho A = 234; hạt nhân con là ²³⁴₉₀Th.)"),

    dict(q="Hạt nhân ¹⁴₆C phóng xạ β⁻. Trong hạt nhân con tạo thành có bao nhiêu "
           "neutron?",
         ans="7",
         sol="Phương trình phân rã: ¹⁴₆C → ⁰₋₁e + ᴬ_Z X.\n"
             "Bảo toàn số nuclon: 14 = 0 + A ⇒ A = 14.\n"
             "Bảo toàn điện tích: 6 = (−1) + Z ⇒ Z = 7, vậy hạt nhân con là ¹⁴₇N.\n"
             "Số neutron của nó: N = A − Z = 14 − 7 = 7."),

    dict(q="Một mẫu chất phóng xạ ban đầu có 8,0·10²⁰ hạt nhân và chu kì bán rã 5,0 ngày. "
           "Tính số hạt nhân còn lại sau 15 ngày (theo 10²⁰ hạt nhân, làm tròn đến hàng "
           "phần mười).",
         ans="1,0",
         sol="Số chu kì bán rã: t/T = 15/5,0 = 3.\n"
             "N = N₀·(1/2)³ = 8,0·10²⁰/8 = 1,0·10²⁰ hạt nhân."),

    dict(q="Một mẫu chất phóng xạ có khối lượng ban đầu 64 g và chu kì bán rã 3,0 giờ. "
           "Sau bao lâu thì khối lượng chất phóng xạ còn lại trong mẫu là 4,0 g? (Kết quả "
           "theo giờ, làm tròn đến hàng đơn vị.)",
         ans="12",
         sol="Tỉ số khối lượng: m₀/m = 64/4,0 = 16 = 2⁴.\n"
             "Vậy đã trôi qua 4 chu kì bán rã: t = 4T = 4 × 3,0 = 12 giờ."),
]

DE2 = dict(code="C4-02", so="02", chuong=4,
           title="ĐỀ KIỂM TRA CHƯƠNG IV – ĐỀ SỐ 02",
           subtitle="Chương IV – Vật lí hạt nhân",
           p1=DE2_P1, p2=DE2_P2, p3=DE2_P3)


# ===================================================================================
#         ĐỀ SỐ 03 – ĐỘ PHÓNG XẠ VÀ ĐỌC ĐỒ THỊ PHÂN RÃ
# ===================================================================================

DE3_P1 = [
    dict(q="Hằng số phóng xạ λ liên hệ với chu kì bán rã T bởi công thức",
         o=["λ = ln2/T.", "λ = T/ln2.", "λ = 2/T.", "λ = T·ln2."],
         a="A",
         sol="Từ N = N₀·2^(−t/T) = N₀·e^(−λt), so sánh hai dạng ta được λ = ln2/T "
             "≈ 0,693/T. Hằng số phóng xạ có đơn vị nghịch đảo thời gian (s⁻¹, giờ⁻¹…) và "
             "đặc trưng cho xác suất phân rã của mỗi hạt nhân trong một đơn vị thời gian."),

    dict(q="Độ phóng xạ H của một mẫu chất phóng xạ chứa N hạt nhân được tính bằng",
         o=["H = λ·N.", "H = N/λ.", "H = λ/N.", "H = λ·N²."],
         a="A",
         sol="Độ phóng xạ là số phân rã xảy ra trong một đơn vị thời gian: H = λ·N. Vì N "
             "giảm theo hàm mũ nên H cũng giảm theo đúng quy luật đó: H = H₀·2^(−t/T)."),

    dict(q="Trong hệ SI, đơn vị của độ phóng xạ là",
         o=["becquerel (Bq).", "curie (Ci).", "gray (Gy).", "sievert (Sv)."],
         a="A",
         sol="1 Bq = 1 phân rã trên giây. Curie là đơn vị cũ ngoài hệ SI "
             "(1 Ci = 3,7·10¹⁰ Bq). Gray và sievert là các đơn vị của liều hấp thụ và "
             "liều tương đương, dùng trong an toàn bức xạ chứ không đo độ phóng xạ."),

    dict(q="Dạng hàm mũ của định luật phóng xạ là",
         o=["N = N₀·e^(−λt).", "N = N₀·e^(λt).",
            "N = N₀·(1 − e^(−λt)).", "N = N₀·λ·e^(−t)."],
         a="A",
         sol="N = N₀·e^(−λt), tương đương với N = N₀·2^(−t/T) khi λ = ln2/T. Dấu trừ ở số "
             "mũ thể hiện số hạt nhân GIẢM theo thời gian. Biểu thức N₀(1 − e^(−λt)) lại "
             "cho số hạt nhân ĐÃ phân rã."),

    dict(q="Khi một mẫu chất phóng xạ phân rã, độ phóng xạ của mẫu",
         o=["giảm theo thời gian đúng theo quy luật giảm của số hạt nhân.",
            "giữ nguyên vì hằng số phóng xạ không đổi.",
            "tăng dần theo thời gian vì số hạt nhân con tăng lên.",
            "giảm đều theo thời gian như một hàm bậc nhất."],
         a="A",
         sol="Vì H = λ·N với λ là hằng số, độ phóng xạ tỉ lệ thuận với số hạt nhân chưa "
             "phân rã. Do đó H = H₀·2^(−t/T) giảm theo cùng quy luật hàm mũ với N, chứ "
             "không giảm đều theo hàm bậc nhất."),

    dict(q="Hình vẽ là đồ thị lnH theo thời gian t của một mẫu chất phóng xạ. Hệ số góc "
           "của đường thẳng này bằng",
         fig="t43a",
         o=["−λ, với λ là hằng số phóng xạ.",
            "−T, với T là chu kì bán rã.",
            "λ, với λ là hằng số phóng xạ.",
            "−H₀, với H₀ là độ phóng xạ ban đầu."],
         a="A",
         sol="Từ H = H₀·e^(−λt), lấy logarit tự nhiên hai vế:\n"
             "lnH = lnH₀ − λt.\n"
             "Đây là hàm bậc nhất theo t với hệ số góc bằng −λ và tung độ gốc bằng lnH₀. "
             "Cách vẽ bán logarit này cho phép xác định λ rất chính xác từ số liệu thực "
             "nghiệm."),

    dict(q="Một mẫu chất phóng xạ có độ phóng xạ 500 Bq. Điều đó có nghĩa là",
         o=["trong mỗi giây có 500 hạt nhân của mẫu bị phân rã.",
            "trong mẫu còn lại đúng 500 hạt nhân phóng xạ.",
            "cứ sau mỗi 500 giây lại có một hạt nhân bị phân rã.",
            "mẫu phát ra 500 tia phóng xạ trong mỗi chu kì bán rã."],
         a="A",
         sol="1 Bq = 1 phân rã/giây, nên 500 Bq nghĩa là trung bình mỗi giây có 500 hạt "
             "nhân trong mẫu bị phân rã. Số hạt nhân còn lại trong mẫu thường lớn hơn con "
             "số này rất nhiều lần."),

    dict(q="Đồng vị ¹⁴C được dùng để xác định niên đại của các mẫu vật cổ có nguồn gốc "
           "sinh vật vì",
         o=["nó có chu kì bán rã 5730 năm, phù hợp với thang thời gian khảo cổ.",
            "nó có chu kì bán rã rất ngắn nên độ phóng xạ giảm rất nhanh.",
            "nó là đồng vị bền nên số lượng trong mẫu không đổi theo thời gian.",
            "nó chỉ có mặt trong các mẫu vật đã bị chôn vùi lâu năm."],
         a="A",
         sol="Sinh vật sống liên tục trao đổi carbon với môi trường nên tỉ lệ ¹⁴C trong cơ "
             "thể gần như không đổi; khi chết, quá trình trao đổi dừng lại và ¹⁴C bắt đầu "
             "giảm theo định luật phóng xạ. Với T = 5730 năm, phương pháp này đo được "
             "tuổi từ vài trăm tới vài chục nghìn năm — đúng khoảng thời gian mà khảo cổ "
             "học quan tâm."),

    dict(q="Hình vẽ là đồ thị khối lượng chất phóng xạ còn lại theo thời gian. Chu kì bán "
           "rã của chất này là",
         fig="t43c",
         o=["8,0 ngày.", "16 ngày.", "4,0 ngày.", "24 ngày."],
         a="A",
         sol="Đọc trên đồ thị: khối lượng giảm từ 80 g xuống 40 g sau 8 ngày, rồi xuống "
             "20 g sau 16 ngày và 10 g sau 24 ngày. Cứ mỗi 8 ngày khối lượng lại giảm một "
             "nửa, nên T = 8,0 ngày."),

    dict(q="Hình vẽ là đồ thị độ phóng xạ của hai mẫu chất X và Y theo thời gian. So sánh "
           "chu kì bán rã của hai mẫu, ta thấy",
         fig="t44c",
         o=["mẫu X có chu kì bán rã nhỏ hơn mẫu Y.",
            "mẫu X có chu kì bán rã lớn hơn mẫu Y.",
            "hai mẫu có chu kì bán rã bằng nhau.",
            "không so sánh được vì độ phóng xạ ban đầu khác nhau."],
         a="A",
         sol="Đường của mẫu X giảm nhanh hơn hẳn đường của mẫu Y: X giảm còn một nửa sau "
             "5 giờ, còn Y phải mất tới 15 giờ. Chu kì bán rã càng nhỏ thì độ phóng xạ "
             "giảm càng nhanh, nên T_X < T_Y."),

    dict(q="Một chất phóng xạ có chu kì bán rã 4,0 giờ. Hằng số phóng xạ của chất này xấp "
           "xỉ",
         o=["0,173 giờ⁻¹.", "5,77 giờ⁻¹.", "0,250 giờ⁻¹.", "2,77 giờ⁻¹."],
         a="A",
         sol="λ = ln2/T = 0,693/4,0 ≈ 0,173 giờ⁻¹.\n"
             "Giá trị 0,250 giờ⁻¹ là kết quả của phép 1/T, tức quên nhân với ln2."),

    dict(q="Từ đồ thị lnH ở Câu 6, biết hệ số góc của đường thẳng là −0,173 giờ⁻¹. Chu kì "
           "bán rã của chất phóng xạ này xấp xỉ",
         fig="t43a",
         o=["4,0 giờ.", "5,8 giờ.", "1,7 giờ.", "0,17 giờ."],
         a="A",
         sol="Hệ số góc bằng −λ nên λ = 0,173 giờ⁻¹.\n"
             "T = ln2/λ = 0,693/0,173 ≈ 4,0 giờ.\n"
             "Giá trị 5,8 giờ ứng với phép 1/λ, tức quên nhân với ln2."),

    dict(q="Cũng theo đồ thị khối lượng ở Câu 9, khối lượng chất phóng xạ còn lại sau "
           "24 ngày là",
         fig="t43c",
         o=["10 g.", "20 g.", "5,0 g.", "40 g."],
         a="A",
         sol="24 ngày = 3 chu kì bán rã (T = 8 ngày).\n"
             "m = 80 × (1/2)³ = 80/8 = 10 g, đúng như giá trị đọc được trên đồ thị."),

    dict(q="Một mẫu chất phóng xạ chứa 2,0·10²⁰ hạt nhân, hằng số phóng xạ "
           "λ = 1,0·10⁻⁶ s⁻¹. Độ phóng xạ của mẫu là",
         o=["2,0·10¹⁴ Bq.", "2,0·10²⁶ Bq.",
            "2,0·10²⁰ Bq.", "5,0·10²⁵ Bq."],
         a="A",
         sol="Độ phóng xạ bằng số phân rã xảy ra trong mỗi giây và được tính bằng "
             "H = λ·N:\n"
             "H = 1,0·10⁻⁶ × 2,0·10²⁰ = 2,0·10¹⁴ Bq.\n"
             "Vì λ đã cho theo s⁻¹ nên kết quả có ngay đơn vị becquerel."),

    dict(q="Độ phóng xạ ban đầu của một mẫu chất là 800 Bq, chu kì bán rã 5,0 giờ. Sau "
           "15 giờ, độ phóng xạ của mẫu là",
         o=["100 Bq.", "200 Bq.", "267 Bq.", "50 Bq."],
         a="A",
         sol="Độ phóng xạ giảm theo đúng quy luật của số hạt nhân vì H = λN với λ "
             "không đổi.\n"
             "Số chu kì bán rã đã trôi qua: 15/5,0 = 3.\n"
             "H = H₀·(1/2)³ = 800/8 = 100 Bq."),

    dict(q="Vẫn với đồ thị độ phóng xạ của hai mẫu X và Y ở Câu 10. Tại thời điểm "
           "t = 15 giờ, so sánh độ phóng xạ của hai mẫu ta thấy",
         fig="t44c",
         o=["độ phóng xạ của Y lớn gấp đôi độ phóng xạ của X.",
            "độ phóng xạ của X lớn gấp đôi độ phóng xạ của Y.",
            "hai mẫu có độ phóng xạ bằng nhau.",
            "độ phóng xạ của Y lớn gấp bốn lần độ phóng xạ của X."],
         a="A",
         sol="Mẫu X: H₀ = 800 Bq, T = 5 giờ nên sau 15 giờ (3 chu kì) còn "
             "800/8 = 100 Bq.\n"
             "Mẫu Y: H₀ = 400 Bq, T = 15 giờ nên sau 15 giờ (1 chu kì) còn "
             "400/2 = 200 Bq.\n"
             "Vậy H_Y = 2·H_X, dù ban đầu mẫu X mới là mẫu có độ phóng xạ lớn hơn."),

    dict(q="Một mẫu gỗ cổ có độ phóng xạ của ¹⁴C bằng 1/4 độ phóng xạ của một mẫu gỗ tươi "
           "cùng khối lượng. Biết chu kì bán rã của ¹⁴C là 5730 năm. Tuổi của mẫu gỗ cổ "
           "xấp xỉ",
         o=["11 460 năm.", "5730 năm.", "1433 năm.", "22 920 năm."],
         a="A",
         sol="Mẫu gỗ tươi có độ phóng xạ đúng bằng độ phóng xạ ban đầu H₀ của mẫu cổ khi "
             "cây còn sống.\n"
             "H/H₀ = 1/4 = (1/2)² ⇒ đã trôi qua 2 chu kì bán rã.\n"
             "t = 2T = 2 × 5730 = 11 460 năm."),

    dict(q="Một mẫu chất phóng xạ có chu kì bán rã 10 ngày. Sau bao lâu thì trong mẫu chỉ "
           "còn lại 20 % số hạt nhân ban đầu?",
         o=["khoảng 23,2 ngày.", "khoảng 20 ngày.",
            "khoảng 50 ngày.", "khoảng 5,0 ngày."],
         a="A",
         sol="Từ N/N₀ = 2^(−t/T) = 0,20 suy ra 2^(t/T) = 5.\n"
             "t/T = ln5/ln2 = 1,609/0,693 ≈ 2,32.\n"
             "t = 2,32 × 10 ≈ 23,2 ngày.\n"
             "Nhận xét: kết quả phải nằm giữa 2T = 20 ngày (còn 25 %) và 3T = 30 ngày "
             "(còn 12,5 %) — hoàn toàn phù hợp."),
]

DE3_P2 = [
    dict(stem="Hình vẽ là đồ thị lnH theo thời gian t của một mẫu chất phóng xạ, trong đó "
              "H là độ phóng xạ của mẫu tính theo becquerel.",
         fig="t43a",
         items=[
             ("Đồ thị là một đường thẳng, chứng tỏ độ phóng xạ giảm đều theo thời gian.",
              False,
              "Cái giảm đều theo thời gian là lnH chứ không phải H. Chính vì "
              "lnH = lnH₀ − λt là hàm bậc nhất mà đồ thị mới là đường thẳng; còn bản thân "
              "H = H₀e^(−λt) giảm theo hàm MŨ, lúc đầu rất nhanh rồi chậm dần."),
             ("Hệ số góc của đường thẳng bằng −λ, với λ là hằng số phóng xạ.", True,
              "Lấy logarit tự nhiên hai vế của H = H₀e^(−λt) ta được lnH = lnH₀ − λt, "
              "trong đó hệ số của t chính là −λ."),
             ("Từ đồ thị, hằng số phóng xạ của chất này xấp xỉ 0,173 giờ⁻¹.", True,
              "Đọc hai điểm trên đường thẳng: tại t = 0 thì lnH = 9,20; tại t = 10 giờ "
              "thì lnH ≈ 7,47.\n"
              "λ = −(7,47 − 9,20)/10 = 1,73/10 = 0,173 giờ⁻¹."),
             ("Chu kì bán rã của chất phóng xạ này xấp xỉ 5,8 giờ.", False,
              "T = ln2/λ = 0,693/0,173 ≈ 4,0 giờ. Con số 5,8 giờ là kết quả của phép "
              "1/λ = 1/0,173, tức đã quên nhân với ln2."),
         ]),

    dict(stem="Hình vẽ là đồ thị khối lượng chất phóng xạ còn lại theo thời gian của một "
              "mẫu có khối lượng ban đầu 80 g.",
         fig="t43c",
         items=[
             ("Chu kì bán rã của chất là 16 ngày.", False,
              "Đọc trên đồ thị: khối lượng giảm từ 80 g còn 40 g chỉ sau 8 ngày. Vậy chu "
              "kì bán rã là T = 8,0 ngày; 16 ngày mới là HAI chu kì bán rã."),
             ("Sau 16 ngày, khối lượng chất phóng xạ còn lại là 20 g.", True,
              "16 ngày = 2 chu kì bán rã: m = 80 × (1/2)² = 20 g, đúng như giá trị đọc "
              "trên đồ thị."),
             ("Sau 32 ngày, khối lượng chất phóng xạ còn lại là 10 g.", False,
              "32 ngày = 4 chu kì bán rã: m = 80 × (1/2)⁴ = 80/16 = 5,0 g. Giá trị 10 g "
              "ứng với thời điểm 24 ngày."),
             ("Khối lượng chất đã bị phân rã sau 24 ngày là 70 g.", True,
              "Sau 24 ngày (3 chu kì bán rã), khối lượng còn lại là 80/8 = 10 g, nên khối "
              "lượng đã phân rã là 80 − 10 = 70 g."),
         ]),

    dict(stem="Một mẫu chất phóng xạ có chu kì bán rã 4,0 giờ, ban đầu chứa 6,0·10²⁰ hạt "
              "nhân phóng xạ.",
         items=[
             ("Hằng số phóng xạ của chất này xấp xỉ 0,173 s⁻¹.", False,
              "Giá trị 0,173 là hằng số phóng xạ tính theo GIỜ⁻¹ (λ = 0,693/4,0). Muốn "
              "tính theo s⁻¹ phải đổi chu kì ra giây:\n"
              "λ = 0,693/(4,0 × 3600) = 0,693/14 400 ≈ 4,81·10⁻⁵ s⁻¹."),
             ("Độ phóng xạ ban đầu của mẫu xấp xỉ 2,9·10¹⁶ Bq.", True,
              "H₀ = λ·N₀ = 4,81·10⁻⁵ × 6,0·10²⁰ ≈ 2,89·10¹⁶ Bq ≈ 2,9·10¹⁶ Bq (dùng λ "
              "tính theo s⁻¹ để kết quả có đơn vị Bq)."),
             ("Sau 12 giờ, số hạt nhân phóng xạ còn lại trong mẫu là 1,5·10²⁰.", False,
              "12 giờ = 3 chu kì bán rã, nên N = 6,0·10²⁰/8 = 7,5·10¹⁹ hạt nhân. Con số "
              "1,5·10²⁰ ứng với việc chỉ chia cho 4, tức nhầm sang 2 chu kì bán rã."),
             ("Sau 12 giờ, độ phóng xạ của mẫu giảm còn 1/8 giá trị ban đầu.", True,
              "Vì H = λ·N với λ không đổi, độ phóng xạ giảm theo đúng tỉ lệ của số hạt "
              "nhân: sau 3 chu kì bán rã thì cả N lẫn H đều còn (1/2)³ = 1/8 giá trị ban "
              "đầu."),
         ]),

    dict(stem="Hình vẽ là đồ thị độ phóng xạ theo thời gian của hai mẫu chất phóng xạ "
              "khác nhau, kí hiệu là X và Y.",
         fig="t44c",
         items=[
             ("Chu kì bán rã của mẫu X là 5,0 giờ.", True,
              "Đọc trên đồ thị: độ phóng xạ của X giảm từ 800 Bq xuống 400 Bq sau 5 giờ. "
              "Vậy T_X = 5,0 giờ."),
             ("Chu kì bán rã của mẫu Y là 10 giờ.", False,
              "Độ phóng xạ của Y giảm từ 400 Bq xuống 200 Bq sau 15 giờ, nên "
              "T_Y = 15 giờ chứ không phải 10 giờ."),
             ("Ở thời điểm ban đầu, độ phóng xạ của mẫu X bằng một nửa độ phóng xạ của "
              "mẫu Y.", False,
              "Ngược lại: ban đầu H_X = 800 Bq còn H_Y = 400 Bq, tức độ phóng xạ của X "
              "GẤP ĐÔI của Y."),
             ("Ở thời điểm t = 15 giờ, độ phóng xạ của mẫu Y lớn gấp đôi độ phóng xạ của "
              "mẫu X.", True,
              "Tại t = 15 giờ: X đã qua 3 chu kì bán rã nên H_X = 800/8 = 100 Bq; Y mới "
              "qua 1 chu kì bán rã nên H_Y = 400/2 = 200 Bq. Vậy H_Y = 2·H_X. Mẫu ban đầu "
              "“mạnh” hơn lại trở nên “yếu” hơn vì nó phân rã nhanh hơn."),
         ]),
]

DE3_P3 = [
    dict(q="Một chất phóng xạ có chu kì bán rã 4,0 giờ. Tính hằng số phóng xạ của chất "
           "này (theo 10⁻⁵ s⁻¹, làm tròn đến hàng phần trăm).",
         ans="4,81",
         sol="Đổi chu kì bán rã ra giây: T = 4,0 × 3600 = 14 400 s.\n"
             "λ = ln2/T = 0,693/14 400 ≈ 4,81·10⁻⁵ s⁻¹."),

    dict(q="Từ đồ thị lnH ở Câu 6, tính chu kì bán rã của chất phóng xạ (theo giờ, làm "
           "tròn đến hàng phần mười).",
         fig="t43a",
         ans="4,0",
         sol="Hệ số góc của đường thẳng: đọc hai điểm (0; 9,20) và (10; 7,47) ta được\n"
             "λ = (9,20 − 7,47)/10 = 0,173 giờ⁻¹.\n"
             "T = ln2/λ = 0,693/0,173 ≈ 4,0 giờ."),

    dict(q="Một mẫu chất phóng xạ chứa 5,0·10²⁰ hạt nhân và có hằng số phóng xạ "
           "2,0·10⁻⁶ s⁻¹. Tính độ phóng xạ của mẫu (theo 10¹⁴ Bq, làm tròn đến hàng đơn "
           "vị).",
         ans="10",
         sol="Độ phóng xạ là số phân rã trong mỗi giây: H = λ·N.\n"
             "H = 2,0·10⁻⁶ × 5,0·10²⁰ = 1,0·10¹⁵ Bq.\n"
             "Quy về đơn vị mà đề yêu cầu: 1,0·10¹⁵ = 10·10¹⁴ Bq, nên kết quả cần điền "
             "là 10."),

    dict(q="Độ phóng xạ ban đầu của một mẫu chất là 800 Bq và chu kì bán rã của chất đó là "
           "5,0 giờ. Tính độ phóng xạ của mẫu sau 15 giờ (theo Bq, làm tròn đến hàng đơn "
           "vị).",
         ans="100",
         sol="Số chu kì bán rã: t/T = 15/5,0 = 3.\n"
             "H = H₀·(1/2)³ = 800/8 = 100 Bq."),

    dict(q="Một mẫu gỗ cổ có độ phóng xạ của ¹⁴C bằng 1/4 độ phóng xạ của mẫu gỗ tươi "
           "cùng khối lượng. Chu kì bán rã của ¹⁴C là 5730 năm. Tính tuổi của mẫu gỗ cổ "
           "(theo 10³ năm, làm tròn đến hàng phần mười).",
         ans="11,5",
         sol="Độ phóng xạ của mẫu gỗ tươi chính là giá trị ban đầu H₀ của mẫu gỗ cổ.\n"
             "H/H₀ = 1/4 = (1/2)² ⇒ đã trôi qua 2 chu kì bán rã.\n"
             "t = 2T = 2 × 5730 = 11 460 năm = 11,46·10³ năm ≈ 11,5·10³ năm."),

    dict(q="Một mẫu chất phóng xạ có chu kì bán rã 10 ngày. Sau bao lâu thì trong mẫu chỉ "
           "còn lại 20 % số hạt nhân ban đầu? (Kết quả theo ngày, làm tròn đến hàng phần "
           "mười.)",
         ans="23,2",
         sol="N/N₀ = 2^(−t/T) = 0,20 ⇒ 2^(t/T) = 5.\n"
             "Lấy logarit: (t/T)·ln2 = ln5 ⇒ t/T = ln5/ln2 = 1,609/0,693 ≈ 2,322.\n"
             "t = 2,322 × 10 ≈ 23,2 ngày."),
]

DE3 = dict(code="C4-03", so="03", chuong=4,
           title="ĐỀ KIỂM TRA CHƯƠNG IV – ĐỀ SỐ 03",
           subtitle="Chương IV – Vật lí hạt nhân",
           p1=DE3_P1, p2=DE3_P2, p3=DE3_P3)


# ===================================================================================
#      ĐỀ SỐ 04 – PHẢN ỨNG HẠT NHÂN, PHÂN HẠCH VÀ NHIỆT HẠCH
# ===================================================================================

DE4_P1 = [
    dict(q="Mọi phản ứng hạt nhân đều tuân theo các định luật bảo toàn",
         o=["số nuclon và điện tích.", "số proton và số neutron.",
            "khối lượng nghỉ và số proton.", "số electron và số neutron."],
         a="A",
         sol="Bốn định luật bảo toàn luôn đúng trong phản ứng hạt nhân là: bảo toàn số "
             "nuclon (số khối A), bảo toàn điện tích (số Z), bảo toàn năng lượng toàn "
             "phần và bảo toàn động lượng. Số proton và số neutron RIÊNG RẼ không được "
             "bảo toàn — chẳng hạn trong phân rã β⁻ một neutron biến thành một proton."),

    dict(q="Phản ứng phân hạch là phản ứng trong đó",
         o=["một hạt nhân rất nặng vỡ thành hai hạt nhân có số khối trung bình.",
            "hai hạt nhân nhẹ kết hợp thành một hạt nhân nặng hơn.",
            "một hạt nhân tự phát phóng ra hạt α rồi biến thành hạt nhân khác.",
            "một hạt nhân hấp thụ photon rồi chuyển về trạng thái cơ bản."],
         a="A",
         sol="Phân hạch xảy ra khi một hạt nhân rất nặng (như ²³⁵U) hấp thụ một neutron "
             "rồi vỡ thành hai mảnh có số khối trung bình, kèm theo vài neutron và năng "
             "lượng lớn. Hai hạt nhân nhẹ kết hợp lại là nhiệt hạch; tự phát phóng ra hạt "
             "α là phóng xạ."),

    dict(q="Quá trình nào sau đây được gọi là phản ứng nhiệt hạch?",
         o=["Hai hạt nhân rất nhẹ kết hợp lại thành một hạt nhân nặng hơn.",
            "Một hạt nhân rất nặng vỡ thành hai hạt nhân nhẹ hơn.",
            "Một hạt nhân hấp thụ neutron chậm rồi phát ra tia γ.",
            "Một electron của lớp vỏ bị hạt nhân bắt giữ."],
         a="A",
         sol="Nhiệt hạch (tổng hợp hạt nhân) là quá trình hai hạt nhân rất nhẹ, chẳng hạn "
             "deuterium và tritium, kết hợp thành hạt nhân nặng hơn và toả năng lượng. "
             "Muốn xảy ra, các hạt nhân phải có động năng đủ lớn để thắng lực đẩy Coulomb, "
             "nên cần nhiệt độ hàng chục triệu độ — do đó mới có tên “nhiệt hạch”."),

    dict(q="Năng lượng toả ra của một phản ứng hạt nhân được tính bằng",
         o=["W = (m_trước − m_sau)·c².", "W = (m_sau − m_trước)·c².",
            "W = (m_trước + m_sau)·c².", "W = m_trước·c² ."],
         a="A",
         sol="Nếu tổng khối lượng nghỉ của các hạt trước phản ứng lớn hơn tổng khối lượng "
             "nghỉ sau phản ứng thì phần chênh lệch đã chuyển thành năng lượng: "
             "W = (m_trước − m_sau)·c² > 0, phản ứng TOẢ năng lượng. Nếu hiệu này âm thì "
             "phản ứng thu năng lượng."),

    dict(q="Hình vẽ mô tả phản ứng phân hạch dây chuyền. Điều kiện để phản ứng dây chuyền "
           "tự duy trì được là",
         fig="t43b",
         o=["hệ số nhân neutron k ≥ 1 và khối lượng nhiên liệu đạt khối lượng tới hạn.",
            "hệ số nhân neutron k < 1 và khối lượng nhiên liệu càng nhỏ càng tốt.",
            "nhiệt độ của khối nhiên liệu đạt tới hàng chục triệu độ.",
            "toàn bộ neutron sinh ra đều bị các thanh điều khiển hấp thụ."],
         a="A",
         sol="Mỗi phân hạch sinh ra trung bình 2 – 3 neutron; nếu trung bình có ít nhất "
             "một neutron gây được phân hạch tiếp theo (k ≥ 1) thì phản ứng tự duy trì. "
             "Ngoài ra khối nhiên liệu phải đủ lớn (đạt khối lượng tới hạn) để neutron "
             "không thoát ra ngoài trước khi kịp gặp hạt nhân. Nhiệt độ cực cao là điều "
             "kiện của nhiệt hạch chứ không phải phân hạch."),

    dict(q="Hình vẽ là sơ đồ nguyên lí của nhà máy điện hạt nhân. Trong nhà máy, năng "
           "lượng được chuyển hoá lần lượt theo trình tự",
         fig="t44a",
         o=["năng lượng hạt nhân → nhiệt năng → cơ năng → điện năng.",
            "năng lượng hạt nhân → điện năng → nhiệt năng → cơ năng.",
            "nhiệt năng → năng lượng hạt nhân → cơ năng → điện năng.",
            "năng lượng hạt nhân → điện năng, không qua giai đoạn trung gian."],
         a="A",
         sol="Lò phản ứng biến năng lượng hạt nhân thành nhiệt năng; bộ sinh hơi dùng "
             "nhiệt đó để tạo hơi nước áp suất cao; hơi nước làm quay tua bin (cơ năng); "
             "tua bin kéo máy phát điện tạo ra điện năng. Về phần biến cơ năng thành điện "
             "năng, nhà máy điện hạt nhân giống hệt nhà máy nhiệt điện thông thường."),

    dict(q="Hình vẽ mô tả phản ứng nhiệt hạch giữa deuterium và tritium. Muốn phản ứng "
           "này xảy ra, cần đưa hỗn hợp tới nhiệt độ rất cao để",
         fig="t44b",
         o=["các hạt nhân có đủ động năng thắng lực đẩy Coulomb và tiến lại gần nhau.",
            "các hạt nhân bị vỡ ra thành các nuclon riêng rẽ trước khi kết hợp.",
            "các electron trong nguyên tử bị bứt hết ra khỏi hạt nhân.",
            "khối lượng của các hạt nhân giảm đi để toả ra năng lượng."],
         a="A",
         sol="Hai hạt nhân đều mang điện dương nên đẩy nhau rất mạnh khi lại gần. Chỉ khi "
             "động năng chuyển động nhiệt đủ lớn (ứng với nhiệt độ hàng chục triệu độ) "
             "chúng mới tiến đủ gần để lực hạt nhân — vốn chỉ tác dụng ở khoảng cách rất "
             "ngắn — kéo chúng lại và kết hợp."),

    dict(q="So với phản ứng phân hạch, phản ứng nhiệt hạch có ưu điểm là",
         o=["nhiên liệu dồi dào và hầu như không tạo ra chất thải phóng xạ lâu dài.",
            "dễ thực hiện và điều khiển hơn trong điều kiện hiện nay.",
            "toả ra năng lượng nhỏ hơn nên an toàn hơn khi vận hành.",
            "không cần cung cấp năng lượng ban đầu để khởi động phản ứng."],
         a="A",
         sol="Nhiên liệu của nhiệt hạch là deuterium (có sẵn trong nước biển) và lithium "
             "để tạo tritium, gần như vô tận; sản phẩm chính là helium — một khí trơ "
             "không phóng xạ. Nhược điểm là rất khó thực hiện và điều khiển vì đòi hỏi "
             "nhiệt độ cực cao, đây là lí do tới nay chưa có nhà máy điện nhiệt hạch "
             "thương mại."),

    dict(q="Trong một phản ứng hạt nhân toả năng lượng, đại lượng nào sau đây KHÔNG được "
           "bảo toàn?",
         o=["Tổng khối lượng nghỉ của các hạt.", "Tổng số nuclon.",
            "Tổng điện tích.", "Tổng năng lượng toàn phần."],
         a="A",
         sol="Tổng khối lượng nghỉ giảm đi; chính phần khối lượng hụt này đã chuyển thành "
             "năng lượng toả ra theo hệ thức W = Δm·c². Số nuclon, điện tích, năng lượng "
             "toàn phần và động lượng thì luôn được bảo toàn."),

    dict(q="Trong lò phản ứng hạt nhân, các thanh điều khiển có vai trò",
         o=["hấp thụ bớt neutron để giữ hệ số nhân neutron xấp xỉ bằng 1.",
            "làm chậm neutron nhanh thành neutron nhiệt.",
            "tải nhiệt từ vùng hoạt của lò ra bộ sinh hơi.",
            "che chắn bức xạ để bảo vệ nhân viên vận hành."],
         a="A",
         sol="Thanh điều khiển (thường làm bằng boron hoặc cadmium) hấp thụ neutron rất "
             "mạnh. Đưa thanh vào sâu thì k giảm, rút thanh ra thì k tăng; nhờ vậy giữ "
             "được k ≈ 1 và lò hoạt động ổn định. Việc làm chậm neutron là nhiệm vụ của "
             "chất làm chậm, còn tải nhiệt là nhiệm vụ của chất tải nhiệt."),

    dict(q="Trong phản ứng ²³⁵₉₂U + ¹₀n → ¹³⁹₅₄Xe + ⁹⁵₃₈Sr + k·¹₀n, giá trị của k là",
         o=["2.", "1.", "3.", "4."],
         a="A",
         sol="Bảo toàn số nuclon: 235 + 1 = 139 + 95 + k ⇒ 236 = 234 + k ⇒ k = 2.\n"
             "Kiểm tra bảo toàn điện tích: 92 + 0 = 54 + 38 + 0 ⇒ 92 = 92 ✓."),

    dict(q="Trong phản ứng ²⁷₁₃Al + ⁴₂He → ³⁰₁₅P + X, hạt X là",
         o=["neutron ¹₀n.", "proton ¹₁p.",
            "electron ⁰₋₁e.", "hạt α ⁴₂He."],
         a="A",
         sol="Bảo toàn số nuclon: 27 + 4 = 30 + A ⇒ A = 1.\n"
             "Bảo toàn điện tích: 13 + 2 = 15 + Z ⇒ Z = 0.\n"
             "Hạt có A = 1 và Z = 0 chính là neutron ¹₀n. Đây là phản ứng lịch sử mà "
             "Joliot-Curie đã thực hiện, tạo ra đồng vị phóng xạ nhân tạo đầu tiên."),

    dict(q="Cho phản ứng nhiệt hạch ²₁D + ³₁T → ⁴₂He + ¹₀n với m_D = 2,0136 u; "
           "m_T = 3,0160 u; m_He = 4,0015 u; m_n = 1,00866 u. Năng lượng toả ra của phản "
           "ứng này xấp xỉ",
         o=["18,1 MeV.", "3,50 MeV.", "36,2 MeV.", "9,05 MeV."],
         a="A",
         sol="Tổng khối lượng trước: 2,0136 + 3,0160 = 5,0296 u.\n"
             "Tổng khối lượng sau: 4,0015 + 1,00866 = 5,01016 u.\n"
             "Δm = 5,0296 − 5,01016 = 0,01944 u.\n"
             "W = 0,01944 × 931,5 ≈ 18,1 MeV."),

    dict(q="Một nhà máy điện hạt nhân có công suất điện 500 MW và hiệu suất 30 %. Công "
           "suất nhiệt mà lò phản ứng phải cung cấp xấp xỉ",
         o=["1667 MW.", "150 MW.", "500 MW.", "1500 MW."],
         a="A",
         sol="Hiệu suất H = P_điện/P_nhiệt nên\n"
             "P_nhiệt = P_điện/H = 500/0,30 ≈ 1667 MW.\n"
             "Giá trị 150 MW là kết quả của phép nhân 500 × 0,30, tức đảo ngược công "
             "thức."),

    dict(q="Vẫn với nhà máy nói trên. Biết mỗi phân hạch ²³⁵U toả ra 200 MeV và "
           "1 MeV = 1,6·10⁻¹³ J. Số phân hạch xảy ra trong mỗi giây xấp xỉ",
         o=["5,2·10¹⁹.", "1,6·10¹⁹.", "5,2·10²².", "2,6·10¹⁹."],
         a="A",
         sol="Năng lượng mỗi phân hạch: 200 MeV = 200 × 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
             "Công suất nhiệt: P_nhiệt = 500/0,30 ≈ 1,667·10⁹ W.\n"
             "Số phân hạch mỗi giây: n = 1,667·10⁹/(3,2·10⁻¹¹) ≈ 5,2·10¹⁹."),

    dict(q="Cũng với nhà máy đó, khối lượng ²³⁵U bị phân hạch trong một ngày xấp xỉ",
         o=["1,76 kg.", "0,88 kg.", "17,6 kg.", "3,52 kg."],
         a="A",
         sol="Số phân hạch trong một ngày: N = 5,2·10¹⁹ × 86 400 ≈ 4,5·10²⁴.\n"
             "Số mol: n = 4,5·10²⁴/(6,02·10²³) ≈ 7,48 mol.\n"
             "Khối lượng: m = 7,48 × 235 ≈ 1757 g ≈ 1,76 kg.\n"
             "Chỉ chưa đầy 2 kg nhiên liệu mỗi ngày — đó là ưu thế nổi bật của năng lượng "
             "hạt nhân so với than đá."),

    dict(q="Năng lượng toả ra khi 1,0 kg ²³⁵U bị phân hạch hoàn toàn (mỗi phân hạch toả "
           "200 MeV) xấp xỉ",
         o=["8,2·10¹³ J.", "3,2·10¹¹ J.",
            "2,6·10²⁴ J.", "8,2·10¹⁰ J."],
         a="A",
         sol="Số hạt nhân trong 1,0 kg = 1000 g:\n"
             "N = (1000/235) × 6,02·10²³ ≈ 4,26 × 6,02·10²³ ≈ 2,56·10²⁴ hạt nhân.\n"
             "Năng lượng: W = N × 3,2·10⁻¹¹ ≈ 2,56·10²⁴ × 3,2·10⁻¹¹ ≈ 8,2·10¹³ J."),

    dict(q="So với việc đốt 1,0 kg than đá (toả khoảng 3,3·10⁷ J), phân hạch hoàn toàn "
           "1,0 kg ²³⁵U toả ra năng lượng lớn hơn khoảng",
         o=["2,5 triệu lần.", "2500 lần.", "250 lần.", "25 tỉ lần."],
         a="A",
         sol="Năng lượng của 1,0 kg ²³⁵U: W ≈ 8,2·10¹³ J.\n"
             "Tỉ số: 8,2·10¹³/(3,3·10⁷) ≈ 2,5·10⁶, tức khoảng 2,5 triệu lần.\n"
             "Đây chính là lí do một nhà máy điện hạt nhân chỉ cần vài tấn nhiên liệu mỗi "
             "năm, trong khi nhà máy nhiệt điện than cần hàng triệu tấn."),
]

DE4_P2 = [
    dict(stem="Hình vẽ mô tả sơ đồ một phản ứng phân hạch dây chuyền của ²³⁵U.",
         fig="t43b",
         items=[
             ("Mỗi phân hạch của ²³⁵U giải phóng thêm một số neutron, các neutron này lại "
              "có thể gây ra những phân hạch mới.", True,
              "Trung bình mỗi phân hạch ²³⁵U sinh ra 2 – 3 neutron. Chính những neutron "
              "này khiến số phân hạch có thể tăng lên theo cấp số nhân, tạo nên phản ứng "
              "dây chuyền."),
             ("Phản ứng dây chuyền tự duy trì được khi hệ số nhân neutron k ≥ 1.", True,
              "Hệ số nhân neutron k là số neutron trung bình của thế hệ sau gây được phân "
              "hạch, tính trên một phân hạch của thế hệ trước. Nếu k < 1 phản ứng tắt "
              "dần; k = 1 phản ứng duy trì ổn định (chế độ của lò phản ứng); k > 1 phản "
              "ứng bùng nổ."),
             ("Nếu khối lượng nhiên liệu nhỏ hơn khối lượng tới hạn thì phản ứng dây "
              "chuyền vẫn tự duy trì được.", False,
              "Với khối nhiên liệu quá nhỏ, phần lớn neutron thoát ra ngoài trước khi kịp "
              "gặp một hạt nhân ²³⁵U, làm k < 1 và phản ứng tắt. Vì vậy khối lượng nhiên "
              "liệu phải đạt tối thiểu khối lượng tới hạn."),
             ("Trong lò phản ứng hạt nhân, người ta điều khiển để k > 1 nhằm liên tục "
              "tăng công suất của lò.", False,
              "Lò phản ứng phải hoạt động ở chế độ k = 1 để công suất ổn định. Nếu duy "
              "trì k > 1 thì số phân hạch tăng theo cấp số nhân và lò sẽ mất kiểm soát. "
              "Các thanh điều khiển được đưa vào hay rút ra chính là để giữ k ≈ 1."),
         ]),

    dict(stem="Hình vẽ là sơ đồ nguyên lí của một nhà máy điện hạt nhân.",
         fig="t44a",
         items=[
             ("Trong lò phản ứng, năng lượng hạt nhân được chuyển hoá trực tiếp thành "
              "điện năng.", False,
              "Lò phản ứng chỉ biến năng lượng hạt nhân thành NHIỆT NĂNG. Sau đó nhiệt "
              "năng mới lần lượt chuyển thành cơ năng của tua bin rồi mới thành điện năng "
              "ở máy phát."),
             ("Bộ sinh hơi có nhiệm vụ biến nhiệt năng thành cơ năng của tua bin.", False,
              "Bộ sinh hơi dùng nhiệt từ lò phản ứng để đun nước thành hơi ở áp suất cao; "
              "nó vẫn ở giai đoạn nhiệt năng. Chính TUA BIN mới là bộ phận biến năng "
              "lượng của dòng hơi thành cơ năng quay."),
             ("Máy phát điện trong nhà máy hoạt động dựa trên hiện tượng cảm ứng điện "
              "từ.", True,
              "Máy phát điện của nhà máy điện hạt nhân không khác gì máy phát của nhà máy "
              "nhiệt điện hay thuỷ điện: khung dây (hoặc nam châm) quay làm từ thông biến "
              "thiên và sinh ra suất điện động cảm ứng."),
             ("Nhà máy điện hạt nhân không phát thải khí CO₂ khi vận hành nhưng lại sinh "
              "ra chất thải phóng xạ cần xử lí lâu dài.", True,
              "Đây là hai mặt của năng lượng hạt nhân. Quá trình phân hạch không đốt "
              "nhiên liệu hoá thạch nên không thải CO₂, nhưng các mảnh phân hạch là những "
              "hạt nhân phóng xạ, một số có chu kì bán rã rất dài, đòi hỏi lưu giữ và xử "
              "lí an toàn trong hàng nghìn năm."),
         ]),

    dict(stem="Cho phản ứng nhiệt hạch ²₁D + ³₁T → ⁴₂He + ¹₀n, với m_D = 2,0136 u; "
              "m_T = 3,0160 u; m_He = 4,0015 u; m_n = 1,00866 u.",
         fig="t44b",
         items=[
             ("Phản ứng này bảo toàn số nuclon và bảo toàn điện tích.", True,
              "Số nuclon: 2 + 3 = 4 + 1 = 5 ✓.\n"
              "Điện tích: 1 + 1 = 2 + 0 = 2 ✓.\n"
              "Đây là điều kiện bắt buộc để một phương trình phản ứng hạt nhân được viết "
              "đúng."),
             ("Tổng khối lượng nghỉ của các hạt sau phản ứng nhỏ hơn tổng khối lượng nghỉ "
              "của các hạt trước phản ứng.", True,
              "Trước: 2,0136 + 3,0160 = 5,0296 u. Sau: 4,0015 + 1,00866 = 5,01016 u.\n"
              "Khối lượng giảm đi 0,01944 u; phần hụt này đã chuyển thành năng lượng toả "
              "ra."),
             ("Năng lượng toả ra của phản ứng xấp xỉ 3,50 MeV.", False,
              "W = Δm × 931,5 = 0,01944 × 931,5 ≈ 18,1 MeV, lớn hơn 3,50 MeV khoảng "
              "5 lần. (Giá trị 3,5 MeV chỉ là động năng mà riêng hạt ⁴He nhận được sau "
              "phản ứng.)"),
             ("Đây là phản ứng thu năng lượng, vì phải cung cấp nhiệt độ rất cao mới thực "
              "hiện được.", False,
              "Đây là phản ứng TOẢ năng lượng: khối lượng nghỉ giảm nên năng lượng được "
              "giải phóng. Nhiệt độ cao chỉ là điều kiện để KHỞI ĐỘNG phản ứng, giúp các "
              "hạt nhân thắng lực đẩy Coulomb, chứ không có nghĩa phản ứng thu năng lượng "
              "về tổng thể."),
         ]),

    dict(stem="Một nhà máy điện hạt nhân có công suất điện 500 MW và hiệu suất 30 %. Biết "
              "mỗi phân hạch ²³⁵U toả ra 200 MeV; 1 MeV = 1,6·10⁻¹³ J và "
              "N_A = 6,02·10²³ mol⁻¹.",
         items=[
             ("Công suất nhiệt mà lò phản ứng phải cung cấp là 1500 MW.", False,
              "P_nhiệt = P_điện/H = 500/0,30 ≈ 1667 MW chứ không phải 1500 MW. Con số "
              "1500 MW ứng với hiệu suất 1/3 ≈ 33,3 %."),
             ("Năng lượng toả ra trong mỗi phân hạch là 3,2·10⁻¹¹ J.", True,
              "Chỉ cần đổi đơn vị năng lượng:\n"
              "200 MeV = 200 × 1,6·10⁻¹³ J = 3,2·10⁻¹¹ J.\n"
              "Một con số rất nhỏ, nhưng vì mỗi giây có tới hàng chục tỉ tỉ phân hạch "
              "nên tổng công suất mới lên tới hàng nghìn megaoát."),
             ("Số phân hạch xảy ra trong mỗi giây xấp xỉ 5,2·10¹⁹.", True,
              "n = P_nhiệt/W₁ = (1,667·10⁹)/(3,2·10⁻¹¹) ≈ 5,2·10¹⁹ phân hạch mỗi giây."),
             ("Khối lượng ²³⁵U bị phân hạch trong một ngày xấp xỉ 0,88 kg.", False,
              "Số phân hạch trong một ngày: 5,2·10¹⁹ × 86 400 ≈ 4,5·10²⁴.\n"
              "Số mol: 4,5·10²⁴/(6,02·10²³) ≈ 7,48 mol ⇒ m ≈ 7,48 × 235 ≈ 1757 g "
              "≈ 1,76 kg.\n"
              "Con số 0,88 kg chỉ bằng một nửa giá trị đúng."),
         ]),
]

DE4_P3 = [
    dict(q="Cho phản ứng phân hạch ²³⁵₉₂U + ¹₀n → ¹⁴⁰₅₄Xe + ᴬ₃₈Sr + 2·¹₀n. Hãy xác định "
           "số khối A của hạt nhân strontium tạo thành.",
         ans="94",
         sol="Áp dụng định luật bảo toàn số nuclon:\n"
             "235 + 1 = 140 + A + 2 × 1 ⇒ 236 = 142 + A ⇒ A = 94.\n"
             "Kiểm tra bảo toàn điện tích: 92 + 0 = 54 + 38 + 0 ⇒ 92 = 92 ✓.\n"
             "Vậy hạt nhân đó là ⁹⁴₃₈Sr."),

    dict(q="Cho phản ứng nhiệt hạch ²₁D + ³₁T → ⁴₂He + ¹₀n với m_D = 2,0136 u; "
           "m_T = 3,0160 u; m_He = 4,0015 u; m_n = 1,00866 u. Tính năng lượng toả ra của "
           "phản ứng (theo MeV, làm tròn đến hàng phần mười).",
         fig="t44b",
         ans="18,1",
         sol="Tổng khối lượng trước phản ứng: 2,0136 + 3,0160 = 5,0296 u.\n"
             "Tổng khối lượng sau phản ứng: 4,0015 + 1,00866 = 5,01016 u.\n"
             "Δm = 5,0296 − 5,01016 = 0,01944 u.\n"
             "W = Δm × 931,5 = 0,01944 × 931,5 ≈ 18,1 MeV."),

    dict(q="Một nhà máy điện hạt nhân có công suất điện 500 MW và hiệu suất 30 %. Mỗi "
           "phân hạch ²³⁵U toả ra 200 MeV, với 1 MeV = 1,6·10⁻¹³ J. Tính số phân hạch xảy "
           "ra trong mỗi giây (theo 10¹⁹ phân hạch, làm tròn đến hàng phần mười).",
         ans="5,2",
         sol="Công suất nhiệt của lò: P = 500/0,30 ≈ 1,667·10⁹ W.\n"
             "Năng lượng mỗi phân hạch: W₁ = 200 × 1,6·10⁻¹³ = 3,2·10⁻¹¹ J.\n"
             "Số phân hạch mỗi giây: n = P/W₁ = (1,667·10⁹)/(3,2·10⁻¹¹) ≈ 5,2·10¹⁹."),

    dict(q="Vẫn với nhà máy điện hạt nhân ở Câu 3 của phần này. Tính khối lượng ²³⁵U bị "
           "phân hạch trong một ngày (theo kg, làm tròn đến hàng phần trăm).",
         ans="1,76",
         sol="Số phân hạch trong một ngày: N = 5,2083·10¹⁹ × 86 400 ≈ 4,50·10²⁴.\n"
             "Số mol tương ứng: n = 4,50·10²⁴/(6,02·10²³) ≈ 7,48 mol.\n"
             "Khối lượng: m = n × 235 ≈ 7,48 × 235 ≈ 1757 g ≈ 1,76 kg."),

    dict(q="Tính năng lượng toả ra khi 1,0 kg ²³⁵U bị phân hạch hoàn toàn, biết mỗi phân "
           "hạch toả 200 MeV và 1 MeV = 1,6·10⁻¹³ J. (Kết quả theo 10¹³ J, làm tròn đến "
           "hàng phần mười.)",
         ans="8,2",
         sol="Số hạt nhân ²³⁵U trong 1,0 kg:\n"
             "N = (1000/235) × 6,02·10²³ ≈ 4,255 × 6,02·10²³ ≈ 2,56·10²⁴.\n"
             "Năng lượng mỗi phân hạch: 3,2·10⁻¹¹ J.\n"
             "W = 2,56·10²⁴ × 3,2·10⁻¹¹ ≈ 8,2·10¹³ J."),

    dict(q="Trong phản ứng ²⁷₁₃Al + ⁴₂He → ³⁰₁₅P + X, hãy xác định số khối của hạt X.",
         ans="1",
         sol="Bảo toàn số nuclon: 27 + 4 = 30 + A ⇒ A = 31 − 30 = 1.\n"
             "Bảo toàn điện tích: 13 + 2 = 15 + Z ⇒ Z = 0.\n"
             "Vậy X là neutron ¹₀n, có số khối bằng 1."),
]

DE4 = dict(code="C4-04", so="04", chuong=4,
           title="ĐỀ KIỂM TRA CHƯƠNG IV – ĐỀ SỐ 04",
           subtitle="Chương IV – Vật lí hạt nhân",
           p1=DE4_P1, p2=DE4_P2, p3=DE4_P3)


# ===================================================================================
#           ĐỀ SỐ 05 – TỔNG HỢP TOÀN CHƯƠNG, PHÂN HOÁ CAO
# ===================================================================================

DE5_P1 = [
    dict(q="Lực hạt nhân là lực",
         o=["tương tác mạnh giữa các nuclon, chỉ tác dụng trong phạm vi rất ngắn.",
            "hút tĩnh điện giữa proton và electron trong nguyên tử.",
            "đẩy Coulomb giữa các proton trong hạt nhân.",
            "hấp dẫn giữa các nuclon, có bán kính tác dụng vô hạn."],
         a="A",
         sol="Lực hạt nhân (tương tác mạnh) liên kết các nuclon lại với nhau, mạnh hơn "
             "lực đẩy Coulomb rất nhiều nhưng chỉ tác dụng trong khoảng cách cỡ kích "
             "thước hạt nhân (khoảng 10⁻¹⁵ m). Chính đặc điểm “tầm ngắn” này giải thích "
             "vì sao các hạt nhân quá lớn lại trở nên kém bền."),

    dict(q="Trong lò phản ứng hạt nhân, chất làm chậm có vai trò",
         o=["giảm tốc độ của neutron để tăng xác suất gây phân hạch.",
            "hấp thụ hết neutron thừa nhằm dừng phản ứng dây chuyền.",
            "tải nhiệt từ vùng hoạt của lò ra bộ sinh hơi.",
            "che chắn bức xạ γ phát ra từ vùng hoạt của lò."],
         a="A",
         sol="Neutron sinh ra từ phân hạch có tốc độ rất lớn (neutron nhanh), trong khi "
             "²³⁵U lại dễ bị phân hạch bởi neutron chậm. Chất làm chậm (nước thường, nước "
             "nặng, than chì) làm neutron mất bớt động năng qua va chạm, nhờ đó phản ứng "
             "dây chuyền duy trì được. Việc hấp thụ neutron là nhiệm vụ của thanh điều "
             "khiển."),

    dict(q="Hình vẽ là một đoạn chuỗi phân rã biểu diễn trên giản đồ N – Z. Quá trình "
           "biến ²³⁸U thành ²³⁴Th là",
         fig="t45a",
         o=["phân rã α.", "phân rã β⁻.", "phân rã β⁺.", "phóng xạ γ."],
         a="A",
         sol="Từ ²³⁸₉₂U sang ²³⁴₉₀Th, số khối giảm 4 và số proton giảm 2 — đúng đặc trưng "
             "của phân rã α (hạt nhân phát ra một hạt ⁴₂He). Trên giản đồ N – Z, điểm "
             "biểu diễn dịch sang trái 2 ô và xuống dưới 2 ô."),

    dict(q="Cũng theo hình vẽ đó, quá trình biến ²³⁴Th thành ²³⁴Pa là",
         fig="t45a",
         o=["phân rã β⁻.", "phân rã α.", "phân rã β⁺.", "phóng xạ γ."],
         a="A",
         sol="Từ ²³⁴₉₀Th sang ²³⁴₉₁Pa, số khối KHÔNG đổi còn số proton TĂNG 1 — đó chính "
             "là đặc trưng của phân rã β⁻ (một neutron biến thành proton và phát ra "
             "electron). Trên giản đồ, điểm dịch sang phải 1 ô và xuống dưới 1 ô."),

    dict(q="Hình vẽ là giản đồ số neutron N theo số proton Z của các hạt nhân. Hạt nhân X "
           "nằm phía trên dải bền vững, tức thừa neutron, nên có xu hướng",
         fig="t42c",
         o=["phóng xạ β⁻ để biến một neutron thành một proton.",
            "phóng xạ β⁺ để biến một proton thành một neutron.",
            "phóng xạ α để giảm đồng thời cả số proton lẫn số neutron.",
            "hấp thụ thêm neutron để trở nên bền vững hơn."],
         a="A",
         sol="Hạt nhân thừa neutron muốn trở về dải bền vững thì phải giảm N và tăng Z. "
             "Phân rã β⁻ làm đúng điều đó: một neutron biến thành một proton, nên điểm "
             "biểu diễn dịch xuống dưới và sang phải, tiến về dải bền vững. Ngược lại, "
             "hạt nhân thừa proton sẽ phóng xạ β⁺."),

    dict(q="Trong y học hạt nhân, để chẩn đoán hình ảnh người ta thường chọn những đồng "
           "vị phóng xạ có chu kì bán rã ngắn vì",
         o=["độ phóng xạ trong cơ thể bệnh nhân giảm nhanh sau khi chụp, làm giảm liều "
            "chiếu.",
            "chúng rẻ tiền và dễ sản xuất hơn hẳn các đồng vị có chu kì bán rã dài.",
            "chúng phát ra tia α nên có khả năng đâm xuyên rất mạnh qua cơ thể.",
            "chúng có năng lượng liên kết riêng lớn nên rất bền và an toàn."],
         a="A",
         sol="Chất phóng xạ đưa vào cơ thể cần đủ hoạt độ để ghi được hình ảnh, nhưng "
             "sau đó phải suy giảm thật nhanh để bệnh nhân không phải chịu liều chiếu "
             "kéo dài. Chu kì bán rã ngắn (thường vài giờ) đáp ứng đúng yêu cầu đó. Tia "
             "α lại đâm xuyên rất yếu và ion hoá rất mạnh nên không dùng để chụp ảnh "
             "chẩn đoán."),

    dict(q="Hình vẽ so sánh năng lượng toả ra trên mỗi kilôgam nhiên liệu của ba quá "
           "trình. Nhận xét đúng là",
         fig="t45b",
         o=["nhiên liệu hạt nhân có mật độ năng lượng lớn hơn than đá hàng triệu lần.",
            "đốt than đá cho mật độ năng lượng lớn hơn phân hạch uranium.",
            "phân hạch và nhiệt hạch cho mật độ năng lượng xấp xỉ như nhau và bằng than "
            "đá.",
            "nhiệt hạch cho mật độ năng lượng nhỏ hơn phân hạch khoảng một nghìn lần."],
         a="A",
         sol="Trục tung của đồ thị dùng thang logarit. Đốt than cho khoảng 3·10⁷ J/kg, "
             "phân hạch cho khoảng 8·10¹³ J/kg và nhiệt hạch còn lớn hơn nữa — chênh nhau "
             "hàng triệu lần. Chú ý đọc thang logarit: mỗi vạch tương ứng gấp 10 lần chứ "
             "không phải cộng thêm một lượng bằng nhau."),

    dict(q="Trong một phản ứng hạt nhân toả năng lượng, tổng khối lượng nghỉ của các hạt "
           "sau phản ứng nhỏ hơn trước phản ứng vì",
         o=["một phần khối lượng đã chuyển thành năng lượng theo hệ thức E = mc².",
            "một số nuclon đã biến mất trong quá trình phản ứng.",
            "các hạt sau phản ứng chuyển động nhanh nên khối lượng giảm đi.",
            "một phần khối lượng đã bị các tia phóng xạ mang ra ngoài."],
         a="A",
         sol="Số nuclon luôn được bảo toàn nên không có nuclon nào biến mất. Điều xảy ra "
             "là khối lượng NGHỈ giảm, và phần hụt Δm chuyển thành năng lượng W = Δm·c², "
             "xuất hiện dưới dạng động năng của các hạt sản phẩm và năng lượng của bức "
             "xạ."),

    dict(q="Trong đoạn chuỗi phân rã từ ²³⁸U đến ²³⁰Th ở hình vẽ, số phân rã α và số phân "
           "rã β⁻ lần lượt là",
         fig="t45a",
         o=["2 và 2.", "2 và 1.", "1 và 2.", "3 và 1."],
         a="A",
         sol="Theo dõi chuỗi trên hình:\n"
             "²³⁸U → ²³⁴Th (A giảm 4, Z giảm 2: phân rã α);\n"
             "²³⁴Th → ²³⁴Pa (A không đổi, Z tăng 1: phân rã β⁻);\n"
             "²³⁴Pa → ²³⁴U (A không đổi, Z tăng 1: phân rã β⁻);\n"
             "²³⁴U → ²³⁰Th (A giảm 4, Z giảm 2: phân rã α).\n"
             "Tổng cộng: 2 phân rã α và 2 phân rã β⁻."),

    dict(q="Năng lượng nghỉ tương ứng với khối lượng 1 u là",
         o=["931,5 MeV.", "1,66·10⁻²⁷ MeV.", "1,6·10⁻¹³ MeV.", "3·10⁸ MeV."],
         a="A",
         sol="Theo quy ước quen dùng trong vật lí hạt nhân, 1 u = 931,5 MeV/c², nghĩa là "
             "năng lượng nghỉ ứng với 1 u đúng bằng 931,5 MeV. Nhờ hệ thức này ta có thể "
             "tính năng lượng liên kết trực tiếp từ độ hụt khối tính theo u."),

    dict(q="Một hạt nhân ²³⁸U có năng lượng liên kết riêng 7,57 MeV/nucleon. Năng lượng "
           "liên kết của hạt nhân này xấp xỉ",
         o=["1802 MeV.", "7,57 MeV.", "238 MeV.", "31,4 MeV."],
         a="A",
         sol="E_lk = ε·A = 7,57 × 238 ≈ 1802 MeV.\n"
             "Đây là một trong những hạt nhân có năng lượng liên kết TỔNG lớn nhất, dù "
             "năng lượng liên kết RIÊNG của nó lại thấp hơn của sắt."),

    dict(q="Năng lượng tương ứng với khối lượng 1,0 g theo hệ thức E = mc² là",
         o=["9,0·10¹³ J.", "3,0·10⁵ J.", "9,0·10¹⁶ J.", "3,0·10¹¹ J."],
         a="A",
         sol="Đổi khối lượng ra kilôgam: m = 1,0 g = 1,0·10⁻³ kg.\n"
             "E = mc² = 1,0·10⁻³ × (3·10⁸)² = 1,0·10⁻³ × 9·10¹⁶ = 9,0·10¹³ J.\n"
             "Con số 9,0·10¹⁶ J là kết quả sai do quên đổi gam sang kilôgam."),

    dict(q="Một mẫu ²¹⁰Po có chu kì bán rã 138 ngày, khối lượng ban đầu 2,0 g. Sau "
           "276 ngày, khối lượng ²¹⁰Po còn lại trong mẫu là",
         o=["0,50 g.", "1,0 g.", "0,25 g.", "1,5 g."],
         a="A",
         sol="276 ngày = 2 chu kì bán rã (276/138 = 2).\n"
             "m = 2,0 × (1/2)² = 2,0/4 = 0,50 g."),

    dict(q="Một mẫu chất phóng xạ sau 30 phút chỉ còn lại 25 % số hạt nhân ban đầu. Chu "
           "kì bán rã của chất này là",
         o=["15 phút.", "7,5 phút.", "30 phút.", "60 phút."],
         a="A",
         sol="Còn lại 25 % = 1/4 = (1/2)² nghĩa là đã trôi qua đúng 2 chu kì bán rã.\n"
             "2T = 30 phút ⇒ T = 15 phút."),

    dict(q="Trong một mẫu chất phóng xạ, tỉ số giữa số hạt nhân đã bị phân rã và số hạt "
           "nhân còn lại bằng 3. Thời gian đã trôi qua bằng",
         o=["2 chu kì bán rã.", "3 chu kì bán rã.",
            "1 chu kì bán rã.", "4 chu kì bán rã."],
         a="A",
         sol="Gọi N là số hạt nhân còn lại thì số đã phân rã là 3N, tổng ban đầu là "
             "N₀ = 4N.\n"
             "N/N₀ = 1/4 = (1/2)² ⇒ t = 2T.\n"
             "Chú ý cái bẫy: tỉ số 3 KHÔNG có nghĩa là 3 chu kì bán rã."),

    dict(q="Một mẫu chất phóng xạ có chu kì bán rã 20 ngày. Sau bao lâu thì độ phóng xạ "
           "của mẫu giảm còn 12,5 % giá trị ban đầu?",
         o=["60 ngày.", "40 ngày.", "80 ngày.", "160 ngày."],
         a="A",
         sol="12,5 % = 1/8 = (1/2)³ nên đã trôi qua 3 chu kì bán rã.\n"
             "t = 3T = 3 × 20 = 60 ngày.\n"
             "Độ phóng xạ giảm theo đúng quy luật của số hạt nhân vì H = λN với λ không "
             "đổi."),

    dict(q="So sánh hai hạt nhân ⁵⁶Fe (ε ≈ 8,79 MeV/nucleon) và ²³⁵U "
           "(ε ≈ 7,59 MeV/nucleon), kết luận đúng là",
         o=["⁵⁶Fe bền vững hơn nhưng ²³⁵U có năng lượng liên kết lớn hơn.",
            "⁵⁶Fe bền vững hơn và cũng có năng lượng liên kết lớn hơn.",
            "²³⁵U bền vững hơn và có năng lượng liên kết lớn hơn.",
            "hai hạt nhân bền vững như nhau vì cùng là hạt nhân tự nhiên."],
         a="A",
         sol="Độ bền vững được đo bằng năng lượng liên kết RIÊNG: 8,79 > 7,59 nên ⁵⁶Fe "
             "bền hơn.\n"
             "Năng lượng liên kết TỔNG: E_lk(⁵⁶Fe) = 8,79 × 56 ≈ 492 MeV, còn "
             "E_lk(²³⁵U) = 7,59 × 235 ≈ 1784 MeV, tức uranium lớn hơn nhiều. Đây là hai "
             "đại lượng khác nhau và không được lẫn lộn."),

    dict(q="Một bệnh nhân được tiêm một liều đồng vị phóng xạ có độ phóng xạ ban đầu "
           "2,0·10⁷ Bq, chu kì bán rã 6,0 giờ. Bỏ qua sự đào thải sinh học, sau 24 giờ độ "
           "phóng xạ còn lại trong cơ thể là",
         o=["1,25·10⁶ Bq.", "5,0·10⁶ Bq.",
            "2,5·10⁶ Bq.", "8,3·10⁵ Bq."],
         a="A",
         sol="24 giờ = 4 chu kì bán rã (24/6,0 = 4).\n"
             "H = H₀·(1/2)⁴ = 2,0·10⁷/16 = 1,25·10⁶ Bq.\n"
             "Trong y học hạt nhân, người ta chọn đồng vị có chu kì bán rã ngắn đúng vì "
             "lí do này: hoạt độ trong cơ thể bệnh nhân giảm nhanh sau khi chẩn đoán."),
]

DE5_P2 = [
    dict(stem="Hình vẽ là một đoạn chuỗi phân rã của ²³⁸U, biểu diễn trên giản đồ số "
              "neutron N theo số proton Z.",
         fig="t45a",
         items=[
             ("Quá trình ²³⁸U → ²³⁴Th là phân rã α.", True,
              "Số khối giảm 4 (238 → 234) và số proton giảm 2 (92 → 90), đúng bằng số "
              "khối và điện tích của hạt ⁴₂He. Vậy đây là phân rã α."),
             ("Quá trình ²³⁴Th → ²³⁴Pa là phân rã β⁻ vì số khối không đổi còn số proton "
              "tăng 1 đơn vị.", True,
              "Đúng theo đặc trưng của phân rã β⁻: một neutron trong hạt nhân biến thành "
              "một proton, phát ra electron; A giữ nguyên còn Z tăng 1."),
             ("Trong đoạn chuỗi từ ²³⁸U đến ²³⁰Th có 2 phân rã α và 1 phân rã β⁻.", False,
              "Theo dõi cả bốn bước trên hình: α (²³⁸U → ²³⁴Th), β⁻ (²³⁴Th → ²³⁴Pa), β⁻ "
              "(²³⁴Pa → ²³⁴U), α (²³⁴U → ²³⁰Th). Vậy có 2 phân rã α và 2 phân rã β⁻ chứ "
              "không phải 1."),
             ("Sau mỗi phân rã β⁻, số khối của hạt nhân giảm đi 1 đơn vị.", False,
              "Trong phân rã β⁻, số khối KHÔNG đổi vì tổng số nuclon được bảo toàn: một "
              "neutron chỉ biến thành một proton chứ không rời khỏi hạt nhân. Chỉ có số "
              "proton tăng thêm 1."),
         ]),

    dict(stem="Hình vẽ là giản đồ số neutron N theo số proton Z, trên đó có vẽ dải các "
              "hạt nhân bền vững, đường N = Z và vị trí của hai hạt nhân X, Y.",
         fig="t42c",
         items=[
             ("Hạt nhân Y nằm trên đường N = Z, tức có số neutron bằng số proton.", True,
              "Theo cách vẽ giản đồ, mọi điểm nằm trên đường N = Z đều ứng với những hạt "
              "nhân có số neutron đúng bằng số proton."),
             ("Hạt nhân X nằm phía trên dải bền vững nên thừa neutron và có xu hướng "
              "phóng xạ β⁻.", True,
              "Muốn trở về dải bền vững, hạt nhân thừa neutron phải giảm N và tăng Z — "
              "đúng là hiệu quả của phân rã β⁻. Trên giản đồ, điểm biểu diễn dịch xuống "
              "dưới và sang phải."),
             ("Với các hạt nhân bền có số khối lớn, số neutron luôn bằng số proton.",
              False,
              "Chỉ các hạt nhân nhẹ mới có N ≈ Z. Khi Z tăng, lực đẩy Coulomb giữa các "
              "proton mạnh lên nên hạt nhân cần thêm neutron để giữ ổn định: dải bền vững "
              "trên hình cong lên phía trên đường N = Z, và với ²³⁸U thì N/Z ≈ 1,6."),
             ("Hạt nhân Y có Z = 55 nên chắc chắn là một hạt nhân bền vững.", False,
              "Trên hình, điểm Y nằm khá xa phía DƯỚI dải bền vững (thiếu neutron so với "
              "hạt nhân bền cùng Z), nên nó không bền và sẽ phóng xạ. Việc nằm trên đường "
              "N = Z không đồng nghĩa với bền vững khi Z đã lớn."),
         ]),

    dict(stem="Một mẫu ²¹⁰Po có chu kì bán rã 138 ngày, khối lượng ban đầu 2,0 g.",
         items=[
             ("Sau 138 ngày, khối lượng ²¹⁰Po còn lại là 1,0 g.", True,
              "138 ngày đúng bằng một chu kì bán rã nên khối lượng còn lại giảm một nửa: "
              "m = 2,0/2 = 1,0 g."),
             ("Sau 276 ngày, khối lượng ²¹⁰Po còn lại là 1,0 g.", False,
              "276 ngày = 2 chu kì bán rã, nên m = 2,0 × (1/2)² = 0,50 g chứ không phải "
              "1,0 g."),
             ("Sau 414 ngày, khối lượng ²¹⁰Po còn lại là 0,50 g.", False,
              "414 ngày = 3 chu kì bán rã, nên m = 2,0 × (1/2)³ = 0,25 g. Giá trị 0,50 g "
              "ứng với thời điểm 276 ngày."),
             ("Chu kì bán rã của mẫu không thay đổi dù ta đun nóng hay nén mạnh mẫu "
              "chất.", True,
              "Phóng xạ là quá trình xảy ra bên trong hạt nhân, ở thang năng lượng MeV, "
              "trong khi các tác động nhiệt hay cơ học chỉ ở thang eV. Vì vậy chu kì bán "
              "rã là hằng số đặc trưng của mỗi loại hạt nhân, không thể thay đổi bằng các "
              "biện pháp thông thường."),
         ]),

    dict(stem="Hình vẽ minh hoạ ba nguyên tắc cơ bản để bảo vệ con người khi làm việc với "
              "nguồn phóng xạ.",
         fig="t45c",
         items=[
             ("Rút ngắn thời gian tiếp xúc với nguồn phóng xạ làm giảm liều chiếu mà cơ "
              "thể nhận được.", True,
              "Liều chiếu tỉ lệ thuận với thời gian ở trong trường bức xạ, nên chỉ cần "
              "giảm một nửa thời gian thao tác là liều nhận được cũng giảm một nửa. Đây "
              "là biện pháp đơn giản và rẻ nhất."),
             ("Tăng khoảng cách tới nguồn phóng xạ không ảnh hưởng tới liều chiếu vì tia "
              "phóng xạ truyền đi rất xa.", False,
              "Với một nguồn nhỏ, cường độ bức xạ giảm theo bình phương khoảng cách: đứng "
              "xa gấp đôi thì liều nhận được chỉ còn một phần tư. Vì vậy tăng khoảng cách "
              "là một trong ba biện pháp bảo vệ hiệu quả nhất, và người ta thường dùng "
              "kẹp dài để thao tác với nguồn."),
             ("Chì được dùng làm vật liệu che chắn vì nó có khối lượng riêng lớn và số "
              "proton lớn.", True,
              "Khả năng hấp thụ tia γ tăng nhanh theo số nguyên tử Z và theo mật độ vật "
              "chất. Chì (Z = 82, khối lượng riêng 11,3 g/cm³) vì thế chắn bức xạ rất "
              "hiệu quả với một bề dày vừa phải."),
             ("Một tờ giấy mỏng đủ để che chắn an toàn cho mọi loại tia phóng xạ.", False,
              "Tờ giấy chỉ chặn được tia α. Tia β cần tấm nhôm vài milimét, còn tia γ "
              "phải dùng lớp chì dày vài xentimét hoặc bê tông. Một nguồn phóng xạ thực "
              "tế thường phát đồng thời nhiều loại tia."),
         ]),
]

DE5_P3 = [
    dict(q="Trong đoạn chuỗi phân rã từ ²³⁸U đến ²³⁰Th ở hình vẽ Câu 3, hãy cho biết tổng "
           "số phân rã β⁻ đã xảy ra.",
         fig="t45a",
         ans="2",
         sol="Theo dõi chuỗi: ²³⁸U →(α) ²³⁴Th →(β⁻) ²³⁴Pa →(β⁻) ²³⁴U →(α) ²³⁰Th.\n"
             "Vậy có 2 phân rã β⁻ (và cũng có 2 phân rã α).\n"
             "Có thể kiểm tra bằng bảo toàn: A giảm 8 nên số phân rã α là 8/4 = 2; Z giảm "
             "2 mà riêng hai phân rã α đã làm Z giảm 4, nên phải có 2 phân rã β⁻ làm Z "
             "tăng lại 2."),

    dict(q="Hạt nhân ²³⁸U có năng lượng liên kết riêng 7,57 MeV/nucleon. Tính năng lượng "
           "liên kết của hạt nhân này (theo MeV, làm tròn đến hàng đơn vị).",
         ans="1802",
         sol="Năng lượng liên kết riêng là năng lượng liên kết tính trung bình cho "
             "mỗi nuclon, nên năng lượng liên kết tổng bằng ε nhân với số nuclon:\n"
             "E_lk = ε·A = 7,57 × 238 = 1801,66 MeV ≈ 1802 MeV."),

    dict(q="Tính năng lượng tương ứng với khối lượng 1,0 g theo hệ thức E = mc², với "
           "c = 3·10⁸ m/s. (Kết quả theo 10¹³ J, làm tròn đến hàng phần mười.)",
         ans="9,0",
         sol="Đổi đơn vị: m = 1,0 g = 1,0·10⁻³ kg.\n"
             "E = mc² = 1,0·10⁻³ × (3·10⁸)² = 1,0·10⁻³ × 9·10¹⁶ = 9,0·10¹³ J.\n"
             "Con số khổng lồ này cho thấy vì sao chỉ cần một lượng rất nhỏ khối lượng "
             "chuyển thành năng lượng đã đủ cho một nhà máy điện hoạt động."),

    dict(q="Một mẫu chất phóng xạ sau 30 phút chỉ còn lại 25 % số hạt nhân ban đầu. Tính "
           "chu kì bán rã của chất này (theo phút, làm tròn đến hàng đơn vị).",
         ans="15",
         sol="N/N₀ = 25 % = 1/4 = (1/2)² nên đã trôi qua đúng 2 chu kì bán rã.\n"
             "2T = 30 phút ⇒ T = 15 phút."),

    dict(q="Trong một mẫu chất phóng xạ, tỉ số giữa số hạt nhân đã bị phân rã và số hạt "
           "nhân còn lại bằng 3. Tính thời gian đã trôi qua, tính theo đơn vị chu kì bán "
           "rã (làm tròn đến hàng đơn vị).",
         ans="2",
         sol="Gọi N là số hạt nhân còn lại; số đã phân rã là 3N nên số ban đầu "
             "N₀ = N + 3N = 4N.\n"
             "N/N₀ = 1/4 = (1/2)² ⇒ t/T = 2, tức đã trôi qua 2 chu kì bán rã.\n"
             "Cái bẫy ở đây là ngộ nhận tỉ số 3 ứng với 3 chu kì bán rã."),

    dict(q="Một bệnh nhân được tiêm một liều đồng vị phóng xạ có độ phóng xạ ban đầu "
           "2,0·10⁷ Bq và chu kì bán rã 6,0 giờ. Bỏ qua sự đào thải sinh học, tính độ "
           "phóng xạ còn lại sau 24 giờ (theo 10⁶ Bq, làm tròn đến hàng phần trăm).",
         ans="1,25",
         sol="Số chu kì bán rã: t/T = 24/6,0 = 4.\n"
             "H = H₀·(1/2)⁴ = 2,0·10⁷/16 = 1,25·10⁶ Bq."),
]

DE5 = dict(code="C4-05", so="05", chuong=4,
           title="ĐỀ KIỂM TRA CHƯƠNG IV – ĐỀ SỐ 05",
           subtitle="Chương IV – Vật lí hạt nhân",
           p1=DE5_P1, p2=DE5_P2, p3=DE5_P3)


DE_CH4 = [DE1, DE2, DE3, DE4, DE5]
