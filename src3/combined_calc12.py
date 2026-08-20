# -*- coding: utf-8 -*-
"""Bài tập TỔNG HỢP Chương I + Chương II.

Hai chương gặp nhau ở ba chỗ có ý nghĩa vật lí thực sự:
  (1) Định luật I nhiệt động lực học áp dụng cho chất khí, với các đẳng quá trình
      của Chương II làm điều kiện ràng buộc (A = 0 khi đẳng tích, ΔU = 0 khi đẳng
      nhiệt của khí lí tưởng).
  (2) Nội năng khí lí tưởng U = (3/2)nRT nối trực tiếp khái niệm nội năng của
      Chương I với phương trình trạng thái của Chương II.
  (3) Bài toán thực tế trong đó vừa có trao đổi nhiệt (nhiệt dung riêng, chuyển thể)
      vừa có biến đổi trạng thái khí.
"""

D1 = "Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn"
D2 = "Dạng 2 – Câu trắc nghiệm đúng/sai"
D3 = "Dạng 3 – Câu trả lời ngắn"
D4 = "Dạng 4 – Bài tập tự luận và vận dụng cao"

CALC12 = {
    # =============================================================== DẠNG 1
    D1: [
        dict(q="Một mol khí lí tưởng đơn nguyên tử được nung nóng đẳng tích từ 300 K lên 400 K. "
               "Nhiệt lượng khí nhận được là (R = 8,31 J/(mol·K))",
             o=["≈ 1247 J.", "≈ 831 J.", "≈ 2078 J.", "≈ 0 J."],
             a="A",
             sol="Đẳng tích nên A = 0, do đó Q = ΔU.\n"
                 "Với khí lí tưởng đơn nguyên tử, U = (3/2)nRT nên "
                 "ΔU = (3/2)·n·R·ΔT = 1,5 · 1 · 8,31 · 100 ≈ 1247 J.\n"
                 "Vậy Q ≈ 1247 J. Đây là chỗ Chương I và Chương II gặp nhau: điều kiện đẳng tích "
                 "của Chương II cho A = 0, còn công thức nội năng cho ΔU."),

        dict(q="Một khối khí lí tưởng dãn nở đẳng nhiệt từ thể tích V lên 2V. Kết luận nào sau "
               "đây đúng?",
             o=["Nội năng khí không đổi, khí nhận nhiệt và sinh công với độ lớn bằng nhau.",
                "Nội năng của khí tăng lên vì thể tích của nó đã tăng gấp đôi.",
                "Nội năng của khí giảm đi vì khí đã sinh công đẩy pit-tông.",
                "Khí hoàn toàn không trao đổi nhiệt lượng nào với môi trường."],
             a="A",
             sol="Nội năng khí lí tưởng chỉ phụ thuộc nhiệt độ; đẳng nhiệt nên ΔU = 0.\n"
                 "Từ ΔU = A + Q suy ra Q = −A. Khí dãn nở nên A < 0, do đó Q > 0: "
                 "khí nhận nhiệt và sinh công với độ lớn bằng nhau. "
                 "Nói khí không trao đổi nhiệt là nhầm ΔU = 0 với Q = 0."),

        dict(q="Nén nhanh (đoạn nhiệt) một khối khí trong bơm xe, công thực hiện lên khí là "
               "150 J. Nội năng của khí",
             o=["tăng 150 J.", "giảm 150 J.", "không đổi.", "tăng 300 J."],
             a="A",
             sol="Nén nhanh nên khí gần như không kịp trao đổi nhiệt: Q ≈ 0 (đoạn nhiệt).\n"
                 "ΔU = A + Q = 150 + 0 = +150 J, nội năng tăng 150 J và khí nóng lên. "
                 "Đây là cơ sở vật lí của việc thân bơm xe nóng lên khi bơm."),

        dict(q="Hai mol khí lí tưởng đơn nguyên tử ở 27 °C. Nội năng của khối khí là "
               "(R = 8,31 J/(mol·K))",
             o=["≈ 7479 J.", "≈ 4986 J.", "≈ 2493 J.", "≈ 3740 J."],
             a="A",
             sol="U = (3/2)·n·R·T = 1,5 · 2 · 8,31 · 300 = 7479 J.\n"
                 "Lưu ý phải dùng nhiệt độ tuyệt đối 300 K chứ không phải 27."),

        dict(q="Một khối khí lí tưởng nhận nhiệt lượng 800 J trong quá trình đẳng áp và sinh "
               "công 320 J. Độ biến thiên nội năng của khí là",
             o=["+480 J.", "+1120 J.", "−480 J.", "+800 J."],
             a="A",
             sol="Q = +800 J; khí sinh công nên A = −320 J.\n"
                 "ΔU = A + Q = −320 + 800 = +480 J.\n"
                 "Trong quá trình đẳng áp, một phần nhiệt lượng nhận vào biến thành công dãn nở, "
                 "phần còn lại làm tăng nội năng."),

        dict(q="Người ta đun nóng 1,0 kg nước từ 20 °C lên 100 °C rồi cho toàn bộ hoá hơi ở "
               "100 °C. Coi hơi nước là khí lí tưởng, thể tích hơi tạo thành ở 100 °C và "
               "1,0·10⁵ Pa xấp xỉ (M = 18 g/mol, R = 8,31 J/(mol·K))",
             o=["≈ 1,72 m³.", "≈ 1,26 m³.", "≈ 0,022 m³.", "≈ 22,4 m³."],
             a="A",
             sol="Số mol hơi nước: n = m/M = 1000/18 ≈ 55,56 mol.\n"
                 "T = 373 K.\n"
                 "V = nRT/p = 55,56 · 8,31 · 373/1,0·10⁵ = 172 210/1,0·10⁵ ≈ 1,72 m³.\n"
                 "Kết quả cho thấy 1 lít nước lỏng biến thành khoảng 1700 lít hơi — hệ số nở "
                 "hơn 1700 lần, đó là lí do hơi nước có sức công phá lớn trong nồi hơi."),

        dict(q="Một khối khí lí tưởng thực hiện chu trình khép kín. Trong chu trình đó khí nhận "
               "tổng cộng 1200 J nhiệt và toả 800 J nhiệt. Công khí sinh ra trong một chu trình là",
             o=["400 J.", "2000 J.", "800 J.", "0 J."],
             a="A",
             sol="Chu trình khép kín nên ΔU = 0 (nội năng là hàm trạng thái).\n"
                 "Tổng nhiệt lượng nhận: Q = 1200 − 800 = +400 J.\n"
                 "Từ ΔU = A + Q: A = −400 J, tức khí SINH công 400 J."),

        dict(q="So sánh nội năng của 1 mol khí helium và 1 mol khí argon (đều đơn nguyên tử, "
               "đều là khí lí tưởng) ở cùng nhiệt độ:",
             o=["Bằng nhau, vì nội năng khí lí tưởng đơn nguyên tử chỉ phụ thuộc n và T.",
                "Argon có nội năng lớn hơn vì khối lượng mol của nó lớn hơn nhiều.",
                "Helium lớn hơn vì phân tử chuyển động nhanh hơn.",
                "Không thể so sánh được nếu chưa biết thể tích của hai khối khí đó."],
             a="A",
             sol="U = (3/2)nRT chỉ chứa số mol và nhiệt độ, hoàn toàn không chứa khối lượng mol. "
                 "Argon nặng hơn nên phân tử chậm hơn, nhưng mỗi phân tử vẫn có cùng động năng "
                 "trung bình (3/2)k_B·T; hai hiệu ứng bù trừ chính xác cho nhau."),
    ],

    # =============================================================== DẠNG 2
    D2: [
        dict(stem="Một xilanh cách nhiệt chứa 0,50 mol khí lí tưởng đơn nguyên tử ở 300 K, "
                  "đóng kín bởi pit-tông có thể trượt không ma sát. "
                  "Cho R = 8,31 J/(mol·K).",
             fig="h29_noi_nang_khi",
             items=[
                 ("Nội năng ban đầu của khối khí xấp xỉ 1870 J.", True,
                  "U = (3/2)nRT = 1,5 · 0,50 · 8,31 · 300 = 1869,75 J ≈ 1870 J."),
                 ("Nếu giữ chặt pit-tông và cung cấp cho khí 500 J nhiệt lượng thì nhiệt độ khí "
                  "tăng thêm khoảng 80,2 K.", True,
                  "Giữ chặt pit-tông là đẳng tích nên A = 0 và ΔU = Q = 500 J.\n"
                  "Từ ΔU = (3/2)nR·ΔT: ΔT = 500/(1,5 · 0,50 · 8,31) = 500/6,2325 ≈ 80,2 K."),
                 ("Nếu nén khí bằng cách đẩy pit-tông với công 300 J trong khi xilanh vẫn cách "
                  "nhiệt thì nội năng khí giảm 300 J.", False,
                  "Xilanh cách nhiệt nên Q = 0 và ΔU = A. Khí NHẬN công nên A = +300 J, "
                  "do đó ΔU = +300 J: nội năng TĂNG 300 J và khí nóng lên, chứ không giảm."),
                 ("Nếu để khí dãn nở đẳng nhiệt ở 300 K thì nội năng khí không đổi.", True,
                  "Với khí lí tưởng, U = (3/2)nRT chỉ phụ thuộc T. Nhiệt độ giữ nguyên 300 K nên "
                  "ΔU = 0, dù thể tích và áp suất đều thay đổi."),
             ]),

        dict(stem="Một nồi áp suất chứa 1,5 kg nước ở 20 °C và một lượng không khí phía trên "
                  "mặt nước. Khi đun, van an toàn của nồi mở khi áp suất bên trong đạt "
                  "2,0·10⁵ Pa, lúc đó nhiệt độ sôi của nước là 120 °C. "
                  "Cho c_nước = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
             items=[
                 ("Nhiệt lượng cần để đưa nước từ 20 °C lên 120 °C là 630 kJ.", True,
                  "Q = m·c·ΔT = 1,5 · 4200 · 100 = 630 000 J = 630 kJ."),
                 ("Nước trong nồi áp suất sôi ở nhiệt độ cao hơn 100 °C vì áp suất bên trong "
                  "lớn hơn áp suất khí quyển.", True,
                  "Nhiệt độ sôi tăng theo áp suất trên mặt thoáng. Ở 2,0·10⁵ Pa (gần gấp đôi "
                  "áp suất khí quyển), nước sôi ở khoảng 120 °C. Đó chính là lí do nồi áp suất "
                  "nấu nhanh nhừ: thức ăn được nấu ở nhiệt độ cao hơn."),
                 ("Nồi áp suất giúp nấu nhanh vì nó làm nước sôi nhanh hơn nồi thường.", False,
                  "Thực tế nồi áp suất làm nước sôi CHẬM hơn (phải đun tới 120 °C thay vì "
                  "100 °C, cần thêm nhiệt lượng). Ưu điểm của nó là nấu ở NHIỆT ĐỘ CAO HƠN, "
                  "nhờ đó phản ứng làm mềm thực phẩm diễn ra nhanh hơn nhiều."),
                 ("Nếu sau khi van mở, nồi tiếp tục nhận thêm 452 kJ nhiệt lượng thì khoảng "
                  "0,20 kg nước đã hoá hơi.", True,
                  "Khi van đã mở, áp suất và nhiệt độ giữ không đổi, toàn bộ nhiệt lượng dùng "
                  "để hoá hơi: m = Q/L = 452 000/2,26·10⁶ = 0,20 kg."),
             ]),

        dict(stem="Một bình kín cách nhiệt thể tích 20 L chứa 0,80 mol khí lí tưởng đơn nguyên "
                  "tử ở 300 K. Bên trong bình có một điện trở nung công suất 25 W. "
                  "Cho R = 8,31 J/(mol·K).",
             items=[
                 ("Áp suất ban đầu của khí trong bình xấp xỉ 0,997·10⁵ Pa.", True,
                  "p = nRT/V = 0,80 · 8,31 · 300/(20·10⁻³) = 1994,4/0,020 = 99 720 Pa "
                  "≈ 0,997·10⁵ Pa."),
                 ("Nội năng ban đầu của khối khí xấp xỉ 2992 J.", True,
                  "U = (3/2)nRT = 1,5 · 0,80 · 8,31 · 300 = 2991,6 J ≈ 2992 J."),
                 ("Sau khi bật điện trở trong 2,0 phút, nhiệt độ khí tăng thêm khoảng 301 K.",
                  True,
                  "Bình kín cách nhiệt, thể tích không đổi nên toàn bộ năng lượng điện biến "
                  "thành nội năng của khí: Q = P·t = 25 · 120 = 3000 J.\n"
                  "ΔT = Q/((3/2)nR) = 3000/(1,5 · 0,80 · 8,31) = 3000/9,972 ≈ 300,8 K ≈ 301 K."),
                 ("Trong quá trình đó, áp suất khí trong bình không đổi vì bình kín.", False,
                  "Bình kín nghĩa là THỂ TÍCH và lượng khí không đổi, tức quá trình ĐẲNG TÍCH. "
                  "Khi đó p/T = hằng số, mà nhiệt độ tăng gấp đôi (từ 300 K lên khoảng 601 K) "
                  "nên áp suất cũng TĂNG gấp đôi, lên khoảng 2,0·10⁵ Pa."),
             ]),
    ],

    # =============================================================== DẠNG 3
    D3: [
        dict(q="Một mol khí lí tưởng đơn nguyên tử được nung đẳng tích từ 300 K lên 500 K. "
               "Tính nhiệt lượng khí nhận được theo jun. Cho R = 8,31 J/(mol·K). "
               "(Làm tròn đến hàng đơn vị.)",
             ans="2493",
             sol="Đẳng tích nên A = 0 và Q = ΔU = (3/2)nRΔT = 1,5 · 1 · 8,31 · 200 = 2493 J."),

        dict(q="Một khối khí lí tưởng nhận 900 J nhiệt lượng và sinh công 350 J. Tính độ biến "
               "thiên nội năng của khí theo jun.",
             ans="550",
             sol="Q = +900 J; A = −350 J (khí sinh công).\n"
                 "ΔU = A + Q = −350 + 900 = +550 J."),

        dict(q="Tính nội năng (theo jun) của 3,0 mol khí lí tưởng đơn nguyên tử ở 127 °C. "
               "Cho R = 8,31 J/(mol·K). (Làm tròn đến hàng đơn vị.)",
             ans="14958",
             sol="T = 127 + 273 = 400 K.\n"
                 "U = (3/2)nRT = 1,5 · 3,0 · 8,31 · 400 = 14 958 J."),

        dict(q="Cho 2,0 kg nước ở 100 °C hoá hơi hoàn toàn. Coi hơi nước là khí lí tưởng "
               "(M = 18 g/mol), tính thể tích hơi thu được ở 100 °C và áp suất 1,0·10⁵ Pa, "
               "theo m³. (Làm tròn đến hai chữ số thập phân.)",
             ans="3,44",
             sol="n = 2000/18 ≈ 111,1 mol; T = 373 K.\n"
                 "V = nRT/p = 111,1 · 8,31 · 373/1,0·10⁵ = 344 400/1,0·10⁵ ≈ 3,44 m³."),

        dict(q="Một khối khí lí tưởng bị nén đoạn nhiệt, nhận công 620 J. Nội năng của khí thay "
               "đổi bao nhiêu jun?",
             ans="620",
             sol="Đoạn nhiệt nên Q = 0, do đó ΔU = A = +620 J: nội năng tăng 620 J."),

        dict(q="Một khối khí lí tưởng dãn nở đẳng nhiệt và nhận 750 J nhiệt lượng. Tính công "
               "mà khí đã sinh ra, theo jun.",
             ans="750",
             sol="Đẳng nhiệt của khí lí tưởng nên ΔU = 0.\n"
                 "Từ ΔU = A + Q: A = −Q = −750 J, tức khí sinh công 750 J."),

        dict(q="Một mol khí lí tưởng đơn nguyên tử ở 300 K được nung đẳng áp, nhận 1500 J nhiệt "
               "lượng và sinh công 600 J. Nhiệt độ cuối của khí bằng bao nhiêu kelvin? "
               "Cho R = 8,31 J/(mol·K). (Làm tròn đến hàng đơn vị.)",
             ans="372",
             sol="ΔU = A + Q = −600 + 1500 = +900 J.\n"
                 "Từ ΔU = (3/2)nRΔT: ΔT = 900/(1,5 · 1 · 8,31) = 900/12,465 ≈ 72,2 K.\n"
                 "T₂ = 300 + 72,2 ≈ 372 K."),
    ],

    # =============================================================== DẠNG 4
    D4: [
        dict(q="Một xilanh đặt thẳng đứng, miệng hướng lên, chứa 0,40 mol khí lí tưởng đơn "
               "nguyên tử, đóng kín bởi một pit-tông nhẹ trượt không ma sát. Áp suất khí trong "
               "xilanh luôn bằng 1,0·10⁵ Pa. Ban đầu khí ở 300 K. Người ta cung cấp cho khí "
               "1500 J nhiệt lượng. Cho R = 8,31 J/(mol·K).\n"
               "a) Tính thể tích khí ban đầu.\n"
               "b) Tính độ tăng nhiệt độ của khí, biết rằng trong quá trình đẳng áp khí sinh "
               "công A' = p·ΔV = nR·ΔT.\n"
               "c) Tính công khí sinh ra và độ biến thiên nội năng.\n"
               "d) Nhận xét về tỉ lệ giữa phần nhiệt lượng biến thành công và phần làm tăng "
               "nội năng.",
             fig="h05_dinh_luat_1",
             ans="a) ≈ 9,97 L   b) ≈ 180,5 K   c) A' ≈ 600 J, ΔU ≈ 900 J",
             sol="a) V₁ = nRT₁/p = 0,40 · 8,31 · 300/(1,0·10⁵) = 997,2/1,0·10⁵ "
                 "= 9,972·10⁻³ m³ ≈ 9,97 L.\n\n"
                 "b) Trong quá trình đẳng áp, nhiệt lượng chia làm hai phần:\n"
                 "Q = ΔU + A' = (3/2)nR·ΔT + nR·ΔT = (5/2)nR·ΔT.\n"
                 "ΔT = 2Q/(5nR) = 2 · 1500/(5 · 0,40 · 8,31) = 3000/16,62 ≈ 180,5 K.\n"
                 "Nhiệt độ cuối: T₂ ≈ 300 + 180,5 = 480,5 K.\n\n"
                 "c) Công khí sinh ra: A' = nR·ΔT = 0,40 · 8,31 · 180,5 ≈ 600 J.\n"
                 "Độ biến thiên nội năng: ΔU = (3/2)nR·ΔT = 1,5 · 0,40 · 8,31 · 180,5 ≈ 900 J.\n"
                 "Kiểm tra: ΔU + A' = 900 + 600 = 1500 J = Q ✓.\n\n"
                 "d) Tỉ lệ A'/Q = 600/1500 = 40 % và ΔU/Q = 900/1500 = 60 %.\n"
                 "Với khí lí tưởng ĐƠN NGUYÊN TỬ, tỉ lệ này luôn cố định: "
                 "A'/Q = (nRΔT)/((5/2)nRΔT) = 2/5 = 40 %, không phụ thuộc n, T hay p. "
                 "Đó là lí do nhiệt dung mol đẳng áp lớn hơn nhiệt dung mol đẳng tích: "
                 "trong quá trình đẳng áp, một phần nhiệt lượng “bị mất” cho công dãn nở."),

        dict(q="Trong một nồi hơi công nghiệp, nước ở 25 °C được đun tới sôi ở 100 °C rồi hoá "
               "hơi hoàn toàn. Hơi nước tạo thành được dẫn vào một bình chứa. Mỗi giờ nồi xử lí "
               "500 kg nước. Cho c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg, M = 18 g/mol, "
               "R = 8,31 J/(mol·K).\n"
               "a) Tính công suất nhiệt tối thiểu của nồi hơi.\n"
               "b) Tính thể tích hơi nước tạo ra trong mỗi giờ, ở 100 °C và 1,0·10⁵ Pa.\n"
               "c) Nếu nén lượng hơi đó vào bình 20 m³ ở 200 °C thì áp suất trong bình bằng "
               "bao nhiêu?\n"
               "d) Trong hai giai đoạn đun nóng và hoá hơi, giai đoạn nào tiêu tốn nhiều năng "
               "lượng hơn và gấp bao nhiêu lần?",
             ans="a) ≈ 358 kW   b) ≈ 861 m³   c) ≈ 5,46·10⁶ Pa   d) hoá hơi, gấp ≈ 7,17 lần",
             sol="a) Đun nóng: Q₁ = 500 · 4200 · 75 = 157 500 000 J = 157,5 MJ.\n"
                 "Hoá hơi: Q₂ = 500 · 2,26·10⁶ = 1 130 000 000 J = 1130 MJ.\n"
                 "Tổng mỗi giờ: Q = 1287,5 MJ.\n"
                 "P = Q/t = 1,2875·10⁹/3600 ≈ 3,576·10⁵ W ≈ 358 kW.\n\n"
                 "b) n = 500 000/18 ≈ 27 778 mol; T = 373 K.\n"
                 "V = nRT/p = 27 778 · 8,31 · 373/(1,0·10⁵) = 86 097 000/1,0·10⁵ ≈ 861 m³.\n\n"
                 "c) Cùng lượng khí, dùng phương trình trạng thái với T' = 473 K, V' = 20 m³:\n"
                 "p' = nRT'/V' = 27 778 · 8,31 · 473/20 = 109 178 000/20 ≈ 5,46·10⁶ Pa.\n"
                 "Kiểm tra bằng cách khác: p' = p·(V/V')·(T'/T) = 1,0·10⁵ · (861/20) · (473/373) "
                 "= 1,0·10⁵ · 43,05 · 1,268 ≈ 5,46·10⁶ Pa. Vậy áp suất khoảng 5,46·10⁶ Pa, "
                 "tức gần 54 atm — một con số cho thấy vì sao nồi hơi phải được thiết kế rất "
                 "chắc chắn và có van an toàn.\n\n"
                 "d) Q₂/Q₁ = 1130/157,5 ≈ 7,17 lần. Giai đoạn HOÁ HƠI tốn năng lượng gấp hơn "
                 "7 lần giai đoạn đun nóng, dù nhiệt độ không hề tăng thêm. Đây là hệ quả trực "
                 "tiếp của việc nhiệt hoá hơi riêng của nước rất lớn."),

        dict(q="Một bình cách nhiệt cứng, thể tích 30 L, được chia thành hai ngăn bằng một vách "
               "ngăn mỏng. Ngăn A thể tích 10 L chứa 0,50 mol khí lí tưởng đơn nguyên tử ở "
               "400 K; ngăn B thể tích 20 L là chân không. Người ta chọc thủng vách ngăn cho "
               "khí tràn đầy bình. Cho R = 8,31 J/(mol·K).\n"
               "a) Tính áp suất khí trong ngăn A trước khi chọc thủng vách.\n"
               "b) Trong quá trình khí tràn vào chân không, khí có sinh công không? Có trao đổi "
               "nhiệt không? Từ đó suy ra nhiệt độ cuối cùng của khí.\n"
               "c) Tính áp suất cuối cùng của khí.\n"
               "d) So sánh quá trình này với quá trình dãn nở đẳng nhiệt thông thường và giải "
               "thích sự khác nhau.",
             ans="a) ≈ 1,66·10⁵ Pa   b) A = 0, Q = 0 nên T không đổi, T = 400 K   "
                 "c) ≈ 0,554·10⁵ Pa",
             sol="a) p_A = nRT/V_A = 0,50 · 8,31 · 400/(10·10⁻³) = 1662/0,010 = 166 200 Pa "
                 "≈ 1,66·10⁵ Pa.\n\n"
                 "b) Khí tràn vào CHÂN KHÔNG nên không có gì để nó đẩy: khí không sinh công, "
                 "A = 0. Bình cách nhiệt và cứng nên cũng không trao đổi nhiệt với bên ngoài, "
                 "Q = 0.\n"
                 "Từ định luật I: ΔU = A + Q = 0, nội năng không đổi. Với khí lí tưởng, "
                 "U chỉ phụ thuộc T nên NHIỆT ĐỘ KHÔNG ĐỔI: T₂ = 400 K.\n"
                 "(Quá trình này gọi là dãn nở tự do, hay dãn nở Joule.)\n\n"
                 "c) p₂ = nRT/V_tổng = 0,50 · 8,31 · 400/(30·10⁻³) = 1662/0,030 = 55 400 Pa "
                 "≈ 0,554·10⁵ Pa.\n"
                 "Có thể kiểm tra nhanh: nhiệt độ không đổi, thể tích tăng gấp ba nên áp suất "
                 "giảm còn một phần ba: 1,66/3 ≈ 0,554·10⁵ Pa ✓.\n\n"
                 "d) Cả hai quá trình đều có ΔU = 0 và nhiệt độ không đổi, nhưng khác nhau căn "
                 "bản ở dòng năng lượng:\n"
                 "• Dãn nở ĐẲNG NHIỆT thông thường: khí đẩy pit-tông nên SINH công (A < 0), "
                 "đồng thời phải NHẬN nhiệt từ nguồn (Q = −A > 0) để giữ nhiệt độ. "
                 "Có trao đổi năng lượng mạnh theo cả hai chiều.\n"
                 "• Dãn nở TỰ DO vào chân không: A = 0 và Q = 0, hoàn toàn không có trao đổi "
                 "năng lượng nào. Khí không sinh được chút công có ích nào.\n"
                 "Đây là ví dụ kinh điển cho thấy “nội năng không đổi” không hề đồng nghĩa với "
                 "“không có gì xảy ra”, và cũng cho thấy dãn nở tự do là quá trình không thuận "
                 "nghịch: khí không bao giờ tự quay về ngăn A."),

        dict(q="Một quả bóng bay cao su chứa 0,10 mol khí helium, được thả trong một căn phòng "
               "ở 27 °C. Sau đó người ta mang quả bóng ra ngoài trời lạnh −13 °C. Coi áp suất "
               "khí trong bóng luôn bằng áp suất khí quyển 1,0·10⁵ Pa và không đổi. "
               "Cho R = 8,31 J/(mol·K).\n"
               "a) Tính thể tích quả bóng trong phòng và ngoài trời.\n"
               "b) Coi helium là khí lí tưởng đơn nguyên tử, tính độ biến thiên nội năng của "
               "khí trong bóng.\n"
               "c) Tính công mà khí quyển đã thực hiện lên khối khí trong bóng.\n"
               "d) Từ đó tính nhiệt lượng mà khối khí đã trao đổi với môi trường và cho biết "
               "khí toả hay thu nhiệt.",
             ans="a) ≈ 2,49 L và ≈ 2,16 L   b) ΔU ≈ −49,9 J   c) A ≈ +33,2 J   "
                 "d) Q ≈ −83,1 J, khí TOẢ nhiệt",
             sol="a) Trong phòng (T₁ = 300 K):\n"
                 "V₁ = nRT₁/p = 0,10 · 8,31 · 300/(1,0·10⁵) = 249,3/1,0·10⁵ = 2,493·10⁻³ m³ "
                 "≈ 2,49 L.\n"
                 "Ngoài trời (T₂ = 260 K):\n"
                 "V₂ = 0,10 · 8,31 · 260/(1,0·10⁵) = 216,06/1,0·10⁵ ≈ 2,16 L.\n\n"
                 "b) ΔU = (3/2)nR·ΔT = 1,5 · 0,10 · 8,31 · (260 − 300) = 1,2465 · (−40) "
                 "≈ −49,9 J. Nội năng giảm vì khí lạnh đi.\n\n"
                 "c) Bóng co lại nên khí quyển ép vào và thực hiện công DƯƠNG lên khối khí:\n"
                 "A = −p·ΔV = −1,0·10⁵ · (2,16·10⁻³ − 2,493·10⁻³) = −1,0·10⁵ · (−0,332·10⁻³) "
                 "≈ +33,2 J.\n"
                 "Dấu dương xác nhận khí NHẬN công.\n\n"
                 "d) Từ ΔU = A + Q: Q = ΔU − A = −49,9 − 33,2 = −83,1 J.\n"
                 "Giá trị âm cho biết khí TOẢ ra môi trường 83,1 J nhiệt lượng.\n"
                 "Nhận xét: dù được khí quyển nén (nhận công 33,2 J), khối khí vẫn nguội đi, "
                 "vì lượng nhiệt nó toả ra lớn hơn công nhận vào. Đây là minh hoạ tốt cho việc "
                 "phải cộng ĐẠI SỐ hai kênh năng lượng chứ không thể xét riêng từng kênh."),

        dict(q="Một bình thép kín thể tích 50 L chứa 2,0 kg nước ở 20 °C và phần còn lại là "
               "không khí ở áp suất 1,0·10⁵ Pa, nhiệt độ 20 °C. Bỏ qua sự bay hơi của nước và "
               "sự nở vì nhiệt của bình và của nước. Cho khối lượng riêng của nước là "
               "1000 kg/m³, c_nước = 4200 J/(kg·K).\n"
               "a) Tính thể tích phần không khí trong bình.\n"
               "b) Đun bình lên 80 °C. Tính áp suất của không khí trong bình.\n"
               "c) Tính nhiệt lượng cần cung cấp cho riêng khối nước.\n"
               "d) Nếu bình chỉ chịu được áp suất 2,0·10⁵ Pa thì nhiệt độ tối đa cho phép là "
               "bao nhiêu? Nhận xét về tính an toàn của giả thiết “bỏ qua sự bay hơi”.",
             ans="a) 48 L   b) ≈ 1,20·10⁵ Pa   c) 504 kJ   d) 586 K (313 °C)",
             sol="a) Thể tích nước: V_nước = m/ρ = 2,0/1000 = 2,0·10⁻³ m³ = 2,0 L.\n"
                 "Thể tích không khí: V_kk = 50 − 2,0 = 48 L.\n\n"
                 "b) Bình thép kín và bỏ qua nở vì nhiệt nên thể tích khí không đổi: đẳng tích.\n"
                 "T₁ = 293 K, T₂ = 353 K.\n"
                 "p₂ = p₁·T₂/T₁ = 1,0·10⁵ · 353/293 ≈ 1,205·10⁵ Pa ≈ 1,20·10⁵ Pa.\n\n"
                 "c) Q = m·c·ΔT = 2,0 · 4200 · 60 = 504 000 J = 504 kJ.\n\n"
                 "d) Đẳng tích: T_max = T₁·p_max/p₁ = 293 · 2,0/1,0 = 586 K, tức 313 °C.\n"
                 "Nhận xét về tính an toàn: giả thiết “bỏ qua sự bay hơi” là RẤT KHÔNG an toàn "
                 "trong thực tế. Trong bình kín, khi nhiệt độ vượt quá 100 °C, nước bay hơi mạnh "
                 "và áp suất hơi nước bão hoà tăng rất nhanh theo nhiệt độ — ở 180 °C áp suất "
                 "hơi nước đã khoảng 10·10⁵ Pa, vượt xa mức 2,0·10⁵ Pa. Vì vậy áp suất thực tế "
                 "sẽ đạt giới hạn của bình ở nhiệt độ THẤP HƠN 313 °C rất nhiều. "
                 "Bài toán này minh hoạ vì sao mọi bình chịu áp có chứa chất lỏng bay hơi đều "
                 "bắt buộc phải có van an toàn."),
    ],
}
