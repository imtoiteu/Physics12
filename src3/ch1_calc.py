# -*- coding: utf-8 -*-
"""Bài tập tính toán và suy luận - Chương I: VẬT LÍ NHIỆT.

Hằng số dùng thống nhất trong toàn bộ tài liệu:
    c_nước  = 4200 J/(kg·K)      c_nước đá = 2100 J/(kg·K)   c_hơi nước = 2010 J/(kg·K)
    c_nhôm  =  880 J/(kg·K)      c_sắt     =  460 J/(kg·K)
    c_đồng  =  380 J/(kg·K)      c_chì     =  130 J/(kg·K)
    λ_nước đá = 3,34·10⁵ J/kg    L_nước    = 2,26·10⁶ J/kg
"""

D1 = "Dạng 1 – Trắc nghiệm nhiều phương án lựa chọn"
D2 = "Dạng 2 – Câu trắc nghiệm đúng/sai"
D3 = "Dạng 3 – Câu trả lời ngắn"
D4 = "Dạng 4 – Bài tập tự luận và vận dụng cao"

CALC1 = {
    # =============================================================== DẠNG 1
    D1: [
        dict(q="Cần cung cấp nhiệt lượng bao nhiêu để đun 2,0 kg nước từ 25 °C lên 75 °C? "
               "Cho c = 4200 J/(kg·K).",
             o=["420 kJ.", "210 kJ.", "630 kJ.", "840 kJ."],
             a="A",
             sol="Q = m·c·ΔT = 2,0 · 4200 · (75 − 25) = 2,0 · 4200 · 50 = 420 000 J = 420 kJ."),

        dict(q="Một ấm điện có công suất 2000 W, hiệu suất 80 %, dùng để đun 2,0 L nước "
               "(coi 1 L nước có khối lượng 1 kg) từ 20 °C tới sôi ở 100 °C. "
               "Thời gian đun là",
             o=["420 s.", "336 s.", "268 s.", "525 s."],
             a="A",
             sol="Nhiệt lượng cần: Q = m·c·ΔT = 2,0 · 4200 · 80 = 672 000 J.\n"
                 "Công suất có ích: P_ích = 0,80 · 2000 = 1600 W.\n"
                 "Thời gian: t = Q/P_ích = 672 000/1600 = 420 s = 7 phút."),

        dict(q="Một khối khí toả ra môi trường 150 J nhiệt lượng, đồng thời nhận công 400 J do "
               "bị nén. Độ biến thiên nội năng của khối khí là",
             o=["+250 J.", "−250 J.", "+550 J.", "−550 J."],
             a="A",
             sol="Khí TOẢ nhiệt nên Q = −150 J. Khí NHẬN công nên A = +400 J.\n"
                 "ΔU = A + Q = 400 + (−150) = +250 J: nội năng tăng 250 J."),

        dict(q="Thả một miếng nhôm khối lượng 0,50 kg ở 100 °C vào 1,0 kg nước ở 20 °C trong "
               "bình cách nhiệt (bỏ qua nhiệt dung của bình). Nhiệt độ cân bằng xấp xỉ",
             o=["27,6 °C.", "24,2 °C.", "31,4 °C.", "60,0 °C."],
             fig="h08_can_bang_nhiet",
             a="A",
             sol="Q_toả = 0,50 · 880 · (100 − t) = 440(100 − t).\n"
                 "Q_thu = 1,0 · 4200 · (t − 20) = 4200(t − 20).\n"
                 "Cân bằng: 44 000 − 440t = 4200t − 84 000 → 128 000 = 4640t → t ≈ 27,6 °C.\n"
                 "Nhận xét: nhiệt độ cân bằng lệch mạnh về phía nước vì tích m·c của nước "
                 "(4200) lớn hơn nhiều so với của nhôm (440)."),

        dict(q="Nhiệt lượng cần để làm nóng chảy hoàn toàn 2,0 kg nước đá đang ở 0 °C là "
               "(λ = 3,34·10⁵ J/kg)",
             o=["668 kJ.", "334 kJ.", "167 kJ.", "1336 kJ."],
             a="A",
             sol="Q = λ·m = 3,34·10⁵ · 2,0 = 6,68·10⁵ J = 668 kJ."),

        dict(q="Cần bao nhiêu nhiệt lượng để biến 0,50 kg nước đá ở −10 °C thành nước ở 20 °C?",
             o=["219,5 kJ.", "209,0 kJ.", "177,5 kJ.", "252,5 kJ."],
             a="A",
             sol="Chặng 1 (đá −10 → 0 °C): Q₁ = 0,50 · 2100 · 10 = 10 500 J.\n"
                 "Chặng 2 (đá tan ở 0 °C): Q₂ = 0,50 · 3,34·10⁵ = 167 000 J.\n"
                 "Chặng 3 (nước 0 → 20 °C): Q₃ = 0,50 · 4200 · 20 = 42 000 J.\n"
                 "Tổng: Q = 10 500 + 167 000 + 42 000 = 219 500 J = 219,5 kJ."),

        dict(q="Một vật khối lượng 5,0 kg rơi tự do từ độ cao 20 m và dừng lại trên nền. "
               "Giả sử 60 % cơ năng chuyển thành nội năng của vật, c = 400 J/(kg·K), "
               "g = 10 m/s². Nhiệt độ vật tăng thêm",
             o=["0,30 K.", "0,50 K.", "0,18 K.", "0,60 K."],
             a="A",
             sol="Cơ năng: W = mgh = 5,0 · 10 · 20 = 1000 J.\n"
                 "Phần chuyển thành nội năng của vật: 0,60 · 1000 = 600 J.\n"
                 "ΔT = 600/(m·c) = 600/(5,0 · 400) = 600/2000 = 0,30 K."),

        dict(q="Đun nóng đều một chất lỏng khối lượng 0,40 kg bằng nguồn nhiệt công suất 50 W. "
               "Sau 168 s, nhiệt độ chất lỏng tăng 10 K. Bỏ qua hao phí, nhiệt dung riêng của "
               "chất lỏng là",
             o=["2100 J/(kg·K).", "4200 J/(kg·K).", "840 J/(kg·K).", "1050 J/(kg·K)."],
             a="A",
             sol="Q = P·t = 50 · 168 = 8400 J.\n"
                 "c = Q/(m·ΔT) = 8400/(0,40 · 10) = 8400/4,0 = 2100 J/(kg·K)."),

        dict(q="Trộn 300 g nước ở 90 °C với 200 g nước ở 20 °C trong bình cách nhiệt. "
               "Nhiệt độ cân bằng là",
             o=["62 °C.", "55 °C.", "48 °C.", "70 °C."],
             a="A",
             sol="Vì cùng là nước nên c triệt tiêu:\n"
                 "t = (m₁t₁ + m₂t₂)/(m₁ + m₂) = (300·90 + 200·20)/500 = (27 000 + 4000)/500 "
                 "= 31 000/500 = 62 °C.\n"
                 "Kết quả lệch về phía 90 °C vì khối nước nóng có khối lượng lớn hơn."),

        dict(q="Một nhiệt lượng kế bằng đồng khối lượng 200 g chứa 500 g nước, cả hai đều ở "
               "20 °C. Nhiệt lượng cần cung cấp để đưa cả hệ lên 30 °C là "
               "(c_đồng = 380 J/(kg·K))",
             o=["21 760 J.", "21 000 J.", "760 J.", "26 000 J."],
             a="A",
             sol="Nước: Q₁ = 0,500 · 4200 · 10 = 21 000 J.\n"
                 "Bình đồng: Q₂ = 0,200 · 380 · 10 = 760 J.\n"
                 "Tổng: Q = 21 000 + 760 = 21 760 J. Bỏ quên nhiệt lượng của bình sẽ thiếu 760 J."),

        dict(q="Một khối khí lí tưởng dãn nở đẳng nhiệt và sinh công 800 J. Nhiệt lượng mà khí "
               "trao đổi với môi trường là",
             o=["nhận vào 800 J.", "toả ra 800 J.", "nhận vào 1600 J.", "bằng 0."],
             a="A",
             sol="Với khí lí tưởng, nội năng chỉ phụ thuộc nhiệt độ. Quá trình đẳng nhiệt có "
                 "T không đổi nên ΔU = 0.\n"
                 "Khí sinh công 800 J nghĩa là A = −800 J.\n"
                 "Từ ΔU = A + Q: 0 = −800 + Q → Q = +800 J, tức khí NHẬN 800 J nhiệt lượng.\n"
                 "Toàn bộ nhiệt lượng nhận vào được chuyển hết thành công."),

        dict(q="Một bếp cung cấp nhiệt đều. Khi đun một khối chất rắn, đoạn nóng chảy trên đồ "
               "thị nhiệt độ – thời gian kéo dài 8,0 phút, còn đoạn làm chất lỏng đó tăng từ "
               "nhiệt độ nóng chảy thêm 40 K kéo dài 2,0 phút. Tỉ số λ/c của chất bằng",
             o=["160 K.", "40 K.", "4 K.", "320 K."],
             a="A",
             sol="Giai đoạn nóng chảy: P·t₁ = λ·m với t₁ = 8,0 phút.\n"
                 "Giai đoạn nóng lên: P·t₂ = m·c·ΔT với t₂ = 2,0 phút, ΔT = 40 K.\n"
                 "Chia hai vế: t₁/t₂ = λ/(c·ΔT) → λ/c = ΔT · t₁/t₂ = 40 · 8,0/2,0 = 160 K.\n"
                 "Chú ý phải nhân với ΔT chứ không chỉ lấy tỉ số thời gian."),

        dict(q="Thả 100 g nước đá ở 0 °C vào 400 g nước ở 50 °C trong bình cách nhiệt. "
               "Trạng thái cuối cùng của hệ là",
             o=["toàn bộ là nước ở khoảng 24,1 °C.",
                "hỗn hợp nước và đá ở 0 °C.",
                "toàn bộ là nước ở khoảng 40,0 °C.",
                "toàn bộ là nước ở khoảng 10,0 °C."],
             a="A",
             sol="Bước kiểm tra: nhiệt lượng nước nóng toả ra khi hạ về 0 °C là "
                 "0,400 · 4200 · 50 = 84 000 J. Nhiệt lượng cần để tan hết đá là "
                 "0,100 · 3,34·10⁵ = 33 400 J. Vì 84 000 > 33 400 nên đá tan hoàn toàn.\n"
                 "Cân bằng nhiệt: 0,400·4200·(50 − t) = 33 400 + 0,100·4200·t\n"
                 "→ 84 000 − 1680t = 33 400 + 420t → 50 600 = 2100t → t ≈ 24,1 °C.\n"
                 "Nếu bỏ qua bước kiểm tra và vội kết luận “đá không tan hết, t = 0 °C” thì sẽ "
                 "chọn nhầm — đó chính là bẫy của bài này."),

        dict(q="Một máy lạnh lấy ra khỏi phòng 3,0·10⁶ J nhiệt lượng trong 1 giờ. Nếu dùng "
               "lượng nhiệt đó để đun nước từ 20 °C lên 100 °C thì khối lượng nước đun được là",
             o=["≈ 8,9 kg.", "≈ 7,1 kg.", "≈ 14,3 kg.", "≈ 3,6 kg."],
             a="A",
             sol="Từ Q = m·c·ΔT suy ra m = Q/(c·ΔT) = 3,0·10⁶/(4200 · 80) = 3,0·10⁶/336 000 "
                 "≈ 8,93 kg ≈ 8,9 kg."),

        dict(q="Trong quá trình đẳng tích, một khối khí nhận nhiệt lượng 600 J. Công mà khí "
               "sinh ra và độ biến thiên nội năng của khí lần lượt là",
             o=["0 J và +600 J.", "600 J và 0 J.", "600 J và +600 J.", "0 J và −600 J."],
             a="A",
             sol="Đẳng tích nghĩa là thể tích không đổi, khí không dãn cũng không bị nén nên "
                 "không trao đổi công: A = 0, công khí sinh ra cũng bằng 0.\n"
                 "Do đó ΔU = A + Q = 0 + 600 = +600 J."),

        dict(q="Đun 1,0 kg nước ở 100 °C cho tới khi bay hơi hết một nửa. Nhiệt lượng cần cung "
               "cấp là (L = 2,26·10⁶ J/kg)",
             o=["1,13 MJ.", "2,26 MJ.", "0,565 MJ.", "4,52 MJ."],
             a="A",
             sol="Nước đã ở đúng nhiệt độ sôi nên không cần nhiệt để tăng nhiệt độ.\n"
                 "Khối lượng hoá hơi: m = 0,50 kg.\n"
                 "Q = L·m = 2,26·10⁶ · 0,50 = 1,13·10⁶ J = 1,13 MJ."),

        dict(q="Hai vật cùng khối lượng, nhiệt dung riêng c₁ = 900 J/(kg·K) và "
               "c₂ = 450 J/(kg·K), ở nhiệt độ 20 °C và 80 °C, được cho tiếp xúc nhiệt. "
               "Nhiệt độ cân bằng là",
             o=["40 °C.", "50 °C.", "60 °C.", "35 °C."],
             a="A",
             sol="t = (m·c₁·t₁ + m·c₂·t₂)/(m·c₁ + m·c₂) = (900·20 + 450·80)/(900 + 450)\n"
                 "= (18 000 + 36 000)/1350 = 54 000/1350 = 40 °C.\n"
                 "Nhiệt độ cân bằng lệch về phía vật có tích m·c lớn hơn, tức vật ở 20 °C."),

        dict(q="Một bình chứa 2,0 kg nước ở 20 °C. Người ta cho hơi nước ở 100 °C ngưng tụ vào "
               "bình cho tới khi nhiệt độ đạt 40 °C. Bỏ qua nhiệt dung của bình, khối lượng hơi "
               "nước đã dùng xấp xỉ",
             o=["70 g.", "168 g.", "35 g.", "744 g."],
             a="A",
             sol="Nước lạnh thu: Q_thu = 2,0 · 4200 · 20 = 168 000 J.\n"
                 "Hơi nước toả gồm hai phần: ngưng tụ ở 100 °C và nguội từ 100 °C xuống 40 °C:\n"
                 "Q_toả = m·L + m·c·60 = m(2,26·10⁶ + 4200·60) = m(2,26·10⁶ + 252 000) "
                 "= 2 512 000·m.\n"
                 "Cân bằng: 2 512 000·m = 168 000 → m ≈ 0,0669 kg ≈ 67 g ≈ 70 g.\n"
                 "Lưu ý: nếu quên phần nguội đi của nước ngưng tụ thì được 74 g."),

        dict(q="Một khối khí thực hiện chu trình khép kín, trong đó nó nhận tổng cộng 2500 J "
               "nhiệt lượng và toả ra 1800 J nhiệt lượng. Công mà khối khí sinh ra trong một "
               "chu trình là",
             o=["700 J.", "4300 J.", "1800 J.", "0 J."],
             a="A",
             sol="Sau một chu trình khép kín, khí trở về trạng thái ban đầu nên ΔU = 0.\n"
                 "Tổng nhiệt lượng khí nhận: Q = 2500 − 1800 = +700 J.\n"
                 "Từ ΔU = A + Q: 0 = A + 700 → A = −700 J, nghĩa là khí SINH công 700 J."),
    ],

    # =============================================================== DẠNG 2
    D2: [
        dict(stem="Một bếp điện công suất 800 W (coi toàn bộ nhiệt lượng truyền cho nước) được "
                  "dùng để đun 1,5 kg nước đá lấy từ tủ đông ở −20 °C. "
                  "Cho c_đá = 2100 J/(kg·K), c_nước = 4200 J/(kg·K), λ = 3,34·10⁵ J/kg.",
             fig="h04_do_thi_dun_nuoc_da",
             items=[
                 ("Nhiệt lượng cần để đưa khối nước đá lên 0 °C là 63,0 kJ.", True,
                  "Q₁ = m·c_đá·ΔT = 1,5 · 2100 · 20 = 63 000 J = 63,0 kJ."),
                 ("Thời gian để nước đá bắt đầu tan là khoảng 78,8 s.", True,
                  "t₁ = Q₁/P = 63 000/800 = 78,75 s ≈ 78,8 s."),
                 ("Nhiệt lượng cần để làm tan hoàn toàn khối nước đá là 501 kJ.", True,
                  "Q₂ = λ·m = 3,34·10⁵ · 1,5 = 501 000 J = 501 kJ."),
                 ("Tổng thời gian từ lúc bắt đầu đun tới lúc nước đạt 100 °C là khoảng 705 s.",
                  False,
                  "Q₁ = 63 000 J; Q₂ = 501 000 J; Q₃ = 1,5·4200·100 = 630 000 J.\n"
                  "Tổng Q = 63 000 + 501 000 + 630 000 = 1 194 000 J.\n"
                  "t = Q/P = 1 194 000/800 = 1492,5 s ≈ 24,9 phút, chứ không phải 705 s. "
                  "Con số 705 s ứng với việc bỏ sót giai đoạn nóng chảy — giai đoạn tốn nhiều "
                  "thời gian nhất sau giai đoạn đun nước."),
             ]),

        dict(stem="Để làm mát nhanh đồ uống, một quán cà phê bỏ các viên đá lấy từ tủ đông ở "
                  "−18 °C vào cốc. Một cốc chứa 250 g cà phê ở 70 °C (coi nhiệt dung riêng của "
                  "cà phê bằng của nước) được bỏ vào 3 viên đá, mỗi viên 20 g. Bỏ qua trao đổi "
                  "nhiệt với cốc và không khí. Cho c_nước = 4200 J/(kg·K), "
                  "c_đá = 2100 J/(kg·K), λ = 3,34·10⁵ J/kg.",
             items=[
                 ("Nhiệt lượng cần để đưa 3 viên đá từ −18 °C lên 0 °C là 2268 J.", True,
                  "Tổng khối lượng đá: 3 · 20 = 60 g = 0,060 kg.\n"
                  "Q = m·c_đá·ΔT = 0,060 · 2100 · 18 = 2268 J."),
                 ("Nhiệt lượng cần để làm tan hết 3 viên đá sau khi chúng đã đạt 0 °C là "
                  "20,04 kJ.", True,
                  "Q = λ·m = 3,34·10⁵ · 0,060 = 20 040 J = 20,04 kJ."),
                 ("Vì đá lấy từ tủ đông ở −18 °C nên nhiệt độ cuối của cốc sẽ thấp hơn 0 °C.",
                  False,
                  "Cà phê có thể toả ra tới 0,250·4200·70 = 73 500 J khi hạ về 0 °C, "
                  "lớn hơn nhiều so với 2268 + 20 040 = 22 308 J cần để đá tan hết. "
                  "Vậy đá tan hoàn toàn và nhiệt độ cuối vẫn CAO HƠN 0 °C. Ngoài ra hỗn hợp "
                  "nước – đá không thể có nhiệt độ dưới 0 °C khi vẫn còn nước lỏng."),
                 ("Nhiệt độ cuối cùng của cốc xấp xỉ 39,3 °C.", True,
                  "Cân bằng: 0,250·4200·(70 − t) = 22 308 + 0,060·4200·t\n"
                  "→ 73 500 − 1050t = 22 308 + 252t → 51 192 = 1302t → t ≈ 39,3 °C.\n"
                  "Lưu ý vế phải phải có cả ba phần: hâm đá lên 0 °C, làm tan đá, rồi hâm nước "
                  "tan từ 0 °C lên nhiệt độ cân bằng."),
             ]),

        dict(stem="Một khối khí lí tưởng lần lượt trải qua ba quá trình độc lập, mỗi lần đều "
                  "xuất phát từ cùng một trạng thái ban đầu: (I) nhận 400 J nhiệt và sinh công "
                  "600 J; (II) toả 250 J nhiệt và nhận công 250 J; (III) bị nén trong bình cách "
                  "nhiệt, nhận công 350 J.",
             fig="h05_dinh_luat_1",
             items=[
                 ("Trong quá trình (I), nội năng của khí giảm 200 J.", True,
                  "Q = +400 J; khí sinh công nên A = −600 J. "
                  "ΔU = A + Q = −600 + 400 = −200 J: nội năng giảm 200 J, nhiệt độ khí giảm "
                  "dù nó vẫn nhận nhiệt."),
                 ("Trong quá trình (II), nội năng của khí không đổi.", True,
                  "Q = −250 J (toả) và A = +250 J (nhận công). "
                  "ΔU = 250 + (−250) = 0. Đây có thể là một quá trình đẳng nhiệt bị nén."),
                 ("Trong quá trình (III), nội năng của khí tăng 350 J.", True,
                  "Bình cách nhiệt nên Q = 0, quá trình là đoạn nhiệt. "
                  "ΔU = A = +350 J. Đây chính là cơ chế làm khí nóng lên khi bị nén nhanh."),
                 ("Cả ba quá trình đều làm nhiệt độ của khối khí tăng lên.", False,
                  "Quá trình (I) có ΔU < 0 nên nhiệt độ GIẢM; quá trình (II) có ΔU = 0 nên nhiệt "
                  "độ KHÔNG đổi. Chỉ quá trình (III) mới làm nhiệt độ tăng."),
             ]),

        dict(stem="Để xác định nhiệt dung riêng của một mẫu kim loại, học sinh nung mẫu tới "
                  "100 °C rồi thả nhanh vào nhiệt lượng kế. Số liệu: khối lượng kim loại "
                  "0,150 kg; khối lượng nước trong nhiệt lượng kế 0,200 kg ở 22,0 °C; "
                  "nhiệt dung của nhiệt lượng kế 150 J/K; nhiệt độ cân bằng đo được 28,0 °C.",
             fig="h09_do_nhiet_dung_rieng",
             items=[
                 ("Nhiệt lượng mà nước thu vào là 5040 J.", True,
                  "Q_nước = 0,200 · 4200 · (28,0 − 22,0) = 0,200 · 4200 · 6,0 = 5040 J."),
                 ("Nhiệt lượng mà nhiệt lượng kế thu vào là 900 J.", True,
                  "Q_bình = C·ΔT = 150 · 6,0 = 900 J."),
                 ("Nhiệt dung riêng của kim loại tính được xấp xỉ 550 J/(kg·K).", True,
                  "Q_toả = 0,150 · c · (100 − 28,0) = 10,8·c.\n"
                  "Cân bằng: 10,8·c = 5040 + 900 = 5940 → c = 5940/10,8 = 550 J/(kg·K)."),
                 ("Nếu học sinh bỏ qua nhiệt lượng kế thì giá trị c tính được sẽ lớn hơn "
                  "550 J/(kg·K).", False,
                  "Bỏ qua bình nghĩa là chỉ lấy Q_thu = 5040 J, khi đó c = 5040/10,8 "
                  "≈ 467 J/(kg·K), NHỎ hơn giá trị đúng 550 J/(kg·K). Bỏ sót một vật thu nhiệt "
                  "làm ta đánh giá thấp nhiệt lượng mà kim loại đã toả ra."),
             ]),

        dict(stem="Đồ thị bên biểu diễn nhiệt lượng Q cung cấp cho 0,20 kg một chất lỏng theo "
                  "độ tăng nhiệt độ ΔT của nó.",
             fig="h10_do_thi_Q_deltaT",
             items=[
                 ("Đồ thị là đường thẳng đi qua gốc toạ độ, chứng tỏ Q tỉ lệ thuận với ΔT.",
                  True,
                  "Các điểm thực nghiệm nằm trên một đường thẳng xuất phát từ gốc, phù hợp với "
                  "công thức Q = (m·c)·ΔT trong đó m·c là hằng số."),
                 ("Hệ số góc của đồ thị bằng 0,42 kJ/K.", True,
                  "Lấy hai điểm bất kì, chẳng hạn ΔT tăng từ 12,0 K lên 20,0 K thì Q tăng từ "
                  "5,04 kJ lên 8,40 kJ. Hệ số góc = 3,36/8,0 = 0,42 kJ/K."),
                 ("Nhiệt dung riêng của chất lỏng là 2100 J/(kg·K).", True,
                  "Hệ số góc chính là m·c = 420 J/K, do đó c = 420/0,20 = 2100 J/(kg·K)."),
                 ("Nếu thay bằng 0,40 kg cùng chất lỏng đó thì đồ thị mới sẽ có hệ số góc "
                  "nhỏ hơn.", False,
                  "Hệ số góc bằng m·c, tỉ lệ THUẬN với khối lượng. Tăng gấp đôi khối lượng thì "
                  "hệ số góc tăng gấp đôi, thành 0,84 kJ/K, tức đồ thị DỐC hơn."),
             ]),

        dict(stem="Xét quá trình làm nguội một chất lỏng như đồ thị bên. Khối lượng chất lỏng "
                  "là 0,50 kg và tốc độ toả nhiệt ra môi trường coi như không đổi trong suốt "
                  "quá trình.",
             fig="h14_do_thi_lam_nguoi",
             items=[
                 ("Nhiệt độ đông đặc của chất này là 60 °C.", True,
                  "Đoạn nằm ngang trên đồ thị làm nguội ứng với quá trình đông đặc; nó nằm ở "
                  "mức 60 °C."),
                 ("Quá trình đông đặc kéo dài 10 phút.", True,
                  "Đoạn nằm ngang kéo dài từ phút thứ 4 đến phút thứ 14, tức 10 phút."),
                 ("Trong 4 phút đầu, chất lỏng toả nhiệt còn trong 10 phút tiếp theo thì không.",
                  False,
                  "Trong suốt cả hai giai đoạn chất đều liên tục TOẢ nhiệt ra môi trường. "
                  "Ở giai đoạn đông đặc, nhiệt lượng toả ra lấy từ việc giảm thế năng tương tác "
                  "khi các phân tử sắp xếp lại thành mạng tinh thể, nên nhiệt độ không đổi."),
                 ("Nhiệt đông đặc riêng của chất lớn hơn tích c·ΔT của giai đoạn đầu "
                  "khoảng 2,5 lần.", True,
                  "Với tốc độ toả nhiệt không đổi, nhiệt lượng tỉ lệ với thời gian. "
                  "Giai đoạn đầu (4 phút) ứng với m·c·30 (từ 90 xuống 60 °C); giai đoạn đông đặc "
                  "(10 phút) ứng với λ·m. Tỉ số λ/(c·30) = 10/4 = 2,5."),
             ]),
    ],

    # =============================================================== DẠNG 3
    D3: [
        dict(q="Tính nhiệt lượng (theo kJ) cần cung cấp để đun 3,0 kg nước từ 30 °C lên 80 °C. "
               "Cho c = 4200 J/(kg·K). (Làm tròn đến hàng đơn vị.)",
             ans="630",
             sol="Q = m·c·ΔT = 3,0 · 4200 · 50 = 630 000 J = 630 kJ."),

        dict(q="Một khối khí nhận 500 J nhiệt lượng và sinh công 200 J. Độ biến thiên nội năng "
               "của khối khí bằng bao nhiêu jun?",
             ans="300",
             sol="Q = +500 J; khí sinh công nên A = −200 J.\n"
                 "ΔU = A + Q = −200 + 500 = +300 J."),

        dict(q="Thả 200 g kim loại ở 120 °C vào 400 g nước ở 25 °C trong bình cách nhiệt "
               "(bỏ qua nhiệt dung của bình), nhiệt độ cân bằng là 30 °C. Tính nhiệt dung riêng "
               "của kim loại theo J/(kg·K). (Làm tròn đến hàng đơn vị.)",
             ans="467",
             sol="Q_thu = 0,400 · 4200 · (30 − 25) = 8400 J.\n"
                 "Q_toả = 0,200 · c · (120 − 30) = 18·c.\n"
                 "Cân bằng: 18·c = 8400 → c ≈ 466,7 ≈ 467 J/(kg·K)."),

        dict(q="Tính nhiệt lượng (theo MJ, làm tròn đến hai chữ số thập phân) cần để biến "
               "1,0 kg nước đá ở 0 °C thành hơi nước ở 100 °C. "
               "Cho λ = 3,34·10⁵ J/kg, c = 4200 J/(kg·K), L = 2,26·10⁶ J/kg.",
             ans="3,01",
             sol="Q₁ (tan đá) = 3,34·10⁵ J.\n"
                 "Q₂ (0 → 100 °C) = 1,0 · 4200 · 100 = 4,20·10⁵ J.\n"
                 "Q₃ (hoá hơi) = 2,26·10⁶ J.\n"
                 "Tổng: 0,334 + 0,420 + 2,260 = 3,014 MJ ≈ 3,01 MJ."),

        dict(q="Một ấm điện công suất 1200 W đun 1,0 kg nước từ 20 °C. Bỏ qua hao phí, sau bao "
               "nhiêu giây nước bắt đầu sôi ở 100 °C? (Làm tròn đến hàng đơn vị.)",
             ans="280",
             sol="Q = 1,0 · 4200 · 80 = 336 000 J.\n"
                 "t = Q/P = 336 000/1200 = 280 s."),

        dict(q="Nhiệt độ của một vật là 45 °C. Nhiệt độ đó bằng bao nhiêu kelvin? "
               "(Lấy 0 °C = 273 K, làm tròn đến hàng đơn vị.)",
             ans="318",
             sol="T = t + 273 = 45 + 273 = 318 K."),

        dict(q="Thả 500 g nước đá ở 0 °C vào 2,0 kg nước ở 60 °C trong bình cách nhiệt. "
               "Tính nhiệt độ cân bằng theo °C. (Làm tròn đến một chữ số thập phân.)",
             ans="32,1",
             sol="Kiểm tra: nước nóng có thể toả 2,0·4200·60 = 504 000 J; cần để tan hết đá "
                 "0,500·3,34·10⁵ = 167 000 J. Vì 504 000 > 167 000 nên đá tan hết.\n"
                 "Cân bằng: 2,0·4200·(60 − t) = 167 000 + 0,500·4200·t\n"
                 "→ 504 000 − 8400t = 167 000 + 2100t → 337 000 = 10 500t → t ≈ 32,1 °C."),

        dict(q="Một vật khối lượng 4,0 kg, nhiệt dung riêng 500 J/(kg·K), rơi từ độ cao 25 m "
               "và dừng lại. Nếu toàn bộ cơ năng biến thành nội năng của vật, lấy g = 10 m/s², "
               "nhiệt độ vật tăng thêm bao nhiêu kelvin? (Làm tròn đến hai chữ số thập phân.)",
             ans="0,50",
             sol="W = mgh = 4,0 · 10 · 25 = 1000 J.\n"
                 "ΔT = W/(m·c) = 1000/(4,0 · 500) = 1000/2000 = 0,50 K."),

        dict(q="Cần cung cấp bao nhiêu kJ nhiệt lượng để làm nóng chảy hoàn toàn 750 g nước đá "
               "đang ở 0 °C? (Làm tròn đến một chữ số thập phân.)",
             ans="250,5",
             sol="Q = λ·m = 3,34·10⁵ · 0,750 = 250 500 J = 250,5 kJ."),

        dict(q="Trộn hai lượng nước có khối lượng 1,2 kg ở 85 °C và 0,80 kg ở 25 °C trong bình "
               "cách nhiệt. Tính nhiệt độ cân bằng theo °C. (Làm tròn đến hàng đơn vị.)",
             ans="61",
             sol="t = (1,2·85 + 0,80·25)/(1,2 + 0,80) = (102 + 20)/2,0 = 122/2,0 = 61 °C."),

        dict(q="Một khối khí toả ra 300 J nhiệt lượng và nội năng của nó giảm 500 J. "
               "Tính công mà khối khí đã sinh ra, theo jun.",
             ans="200",
             sol="Q = −300 J; ΔU = −500 J.\n"
                 "Từ ΔU = A + Q: A = ΔU − Q = −500 − (−300) = −200 J.\n"
                 "Giá trị âm cho biết khí SINH công, độ lớn 200 J."),

        dict(q="Một nguồn nhiệt công suất 60 W đun nóng 0,25 kg một chất lỏng. Sau 350 s, "
               "nhiệt độ chất lỏng tăng 20 K. Bỏ qua hao phí, tính nhiệt dung riêng của chất "
               "lỏng theo J/(kg·K). (Làm tròn đến hàng đơn vị.)",
             ans="4200",
             sol="Q = P·t = 60 · 350 = 21 000 J.\n"
                 "c = Q/(m·ΔT) = 21 000/(0,25 · 20) = 21 000/5,0 = 4200 J/(kg·K)."),

        dict(q="Một bình nhiệt lượng kế có nhiệt dung 180 J/K chứa 0,40 kg nước ở 18 °C. "
               "Cần cung cấp bao nhiêu kJ nhiệt lượng để đưa cả hệ lên 28 °C? "
               "(Làm tròn đến một chữ số thập phân.)",
             ans="18,6",
             sol="Nước: 0,40 · 4200 · 10 = 16 800 J.\n"
                 "Bình: 180 · 10 = 1800 J.\n"
                 "Tổng: 16 800 + 1800 = 18 600 J = 18,6 kJ."),

        dict(q="Đun 2,0 kg nước ở 100 °C, sau một thời gian còn lại 1,7 kg. "
               "Tính nhiệt lượng đã dùng để hoá hơi, theo kJ. (Làm tròn đến hàng đơn vị.)",
             ans="678",
             sol="Khối lượng đã hoá hơi: m = 2,0 − 1,7 = 0,30 kg.\n"
                 "Q = L·m = 2,26·10⁶ · 0,30 = 678 000 J = 678 kJ."),
    ],

    # =============================================================== DẠNG 4
    D4: [
        dict(q="Một bình cách nhiệt chứa 2,0 kg nước ở 70 °C. Người ta lần lượt thả vào bình "
               "các viên nước đá 0 °C, mỗi viên 100 g, mỗi lần đợi hệ cân bằng rồi mới thả viên "
               "tiếp theo.\n"
               "a) Tính nhiệt độ của bình sau khi thả viên đá thứ nhất.\n"
               "b) Tính nhiệt độ của bình sau khi thả viên đá thứ hai.\n"
               "c) Giải thích vì sao độ giảm nhiệt độ do mỗi viên đá gây ra ngày càng nhỏ.\n"
               "d) Tính tổng khối lượng nước đá tối đa có thể thả vào mà vẫn tan hết.",
             ans="a) ≈ 62,9 °C   b) ≈ 56,4 °C   d) ≈ 1,76 kg (17 viên)",
             sol="a) Gọi t₁ là nhiệt độ cân bằng. Nước toả: 2,0·4200·(70 − t₁). "
                 "Đá thu: 0,100·3,34·10⁵ + 0,100·4200·t₁ = 33 400 + 420t₁.\n"
                 "8400(70 − t₁) = 33 400 + 420t₁ → 588 000 − 8400t₁ = 33 400 + 420t₁\n"
                 "→ 554 600 = 8820t₁ → t₁ ≈ 62,9 °C.\n\n"
                 "b) Bây giờ bình chứa 2,1 kg nước ở 62,9 °C. Thả tiếp 0,100 kg đá:\n"
                 "2,1·4200·(62,9 − t₂) = 33 400 + 0,100·4200·t₂\n"
                 "→ 8820·62,9 − 8820t₂ = 33 400 + 420t₂ → 554 778 − 8820t₂ = 33 400 + 420t₂\n"
                 "→ 521 378 = 9240t₂ → t₂ ≈ 56,4 °C.\n"
                 "Độ giảm lần 1 là 7,1 K, lần 2 chỉ còn 6,5 K.\n\n"
                 "c) Sau mỗi lần, khối lượng nước trong bình TĂNG thêm 0,1 kg trong khi nhiệt "
                 "lượng mà một viên đá lấy đi thay đổi rất ít. Cùng một lượng nhiệt bị lấy đi "
                 "nhưng chia cho khối lượng lớn hơn nên độ giảm nhiệt độ nhỏ hơn. Ngoài ra "
                 "nhiệt độ bình càng thấp thì phần nhiệt dùng để hâm nóng nước tan cũng càng ít.\n\n"
                 "d) Gọi M là tổng khối lượng đá thả vào để nhiệt độ cuối vừa đúng 0 °C:\n"
                 "2,0·4200·70 = M·3,34·10⁵ → 588 000 = 334 000·M → M ≈ 1,76 kg.\n"
                 "Vậy tối đa khoảng 1,76 kg nước đá, tức 17 viên (viên thứ 18 sẽ không tan hết)."),

        dict(q="Một ấm điện công suất định mức 1500 W được dùng để đun 1,5 kg nước ở 25 °C.\n"
               "a) Tính nhiệt lượng cần để đưa nước tới 100 °C.\n"
               "b) Thực tế phải mất 6,0 phút nước mới sôi. Tính hiệu suất của ấm.\n"
               "c) Sau khi sôi, người ta tiếp tục đun thêm 5,0 phút với cùng hiệu suất. "
               "Tính khối lượng nước đã hoá hơi.\n"
               "d) Nêu hai biện pháp làm tăng hiệu suất của ấm và giải thích.",
             ans="a) 472,5 kJ   b) ≈ 87,5 %   c) ≈ 0,174 kg",
             sol="a) Q = m·c·ΔT = 1,5 · 4200 · 75 = 472 500 J = 472,5 kJ.\n\n"
                 "b) Năng lượng điện tiêu thụ: W = P·t = 1500 · 360 = 540 000 J.\n"
                 "H = Q/W = 472 500/540 000 = 0,875 = 87,5 %.\n\n"
                 "c) Năng lượng có ích trong 5,0 phút: "
                 "Q' = H·P·t = 0,875 · 1500 · 300 = 393 750 J.\n"
                 "Khối lượng hoá hơi: m = Q'/L = 393 750/2,26·10⁶ ≈ 0,174 kg ≈ 174 g.\n\n"
                 "d) Hai biện pháp:\n"
                 "• Đậy nắp ấm: giảm hao phí do bay hơi và do đối lưu không khí phía trên, "
                 "nhờ đó phần lớn nhiệt lượng ở lại trong nước.\n"
                 "• Bọc cách nhiệt vỏ ấm hoặc đun lượng nước vừa đủ: giảm nhiệt lượng truyền ra "
                 "môi trường qua thành ấm, đồng thời rút ngắn thời gian đun nên tổng hao phí "
                 "cũng giảm."),

        dict(q="Người ta đun một khối chất rắn khối lượng 0,60 kg bằng nguồn nhiệt có công suất "
               "không đổi 250 W và ghi lại: nhiệt độ tăng từ 20 °C lên nhiệt độ nóng chảy 80 °C "
               "trong 2,0 phút; sau đó nhiệt độ giữ nguyên 80 °C trong 6,0 phút; rồi tiếp tục "
               "tăng lên 120 °C trong 3,0 phút. Bỏ qua hao phí.\n"
               "a) Tính nhiệt dung riêng của chất ở thể rắn.\n"
               "b) Tính nhiệt nóng chảy riêng của chất.\n"
               "c) Tính nhiệt dung riêng của chất ở thể lỏng.\n"
               "d) Vẽ phác đồ thị nhiệt độ – thời gian và giải thích vì sao đoạn ứng với thể "
               "lỏng thoải hơn đoạn ứng với thể rắn.",
             ans="a) ≈ 833 J/(kg·K)   b) ≈ 1,50·10⁵ J/kg   c) ≈ 1875 J/(kg·K)",
             sol="a) Giai đoạn 1: Q₁ = P·t₁ = 250 · 120 = 30 000 J; ΔT = 60 K.\n"
                 "c_rắn = Q₁/(m·ΔT) = 30 000/(0,60 · 60) = 30 000/36 ≈ 833 J/(kg·K).\n\n"
                 "b) Giai đoạn 2: Q₂ = 250 · 360 = 90 000 J.\n"
                 "λ = Q₂/m = 90 000/0,60 = 150 000 = 1,50·10⁵ J/kg.\n\n"
                 "c) Giai đoạn 3: Q₃ = 250 · 180 = 45 000 J; ΔT = 40 K.\n"
                 "c_lỏng = 45 000/(0,60 · 40) = 45 000/24 = 1875 J/(kg·K).\n\n"
                 "d) Đồ thị gồm: đoạn thẳng đi lên từ 20 °C tới 80 °C, đoạn nằm ngang ở 80 °C, "
                 "rồi đoạn thẳng đi lên tới 120 °C.\n"
                 "Độ dốc của mỗi đoạn nghiêng là dT/dt = P/(m·c). Vì c_lỏng = 1875 lớn hơn "
                 "c_rắn ≈ 833 nên độ dốc ở thể lỏng nhỏ hơn, tức đoạn đó THOẢI hơn. "
                 "Nói cách khác, chất ở thể lỏng cần nhiều nhiệt lượng hơn để tăng cùng một "
                 "khoảng nhiệt độ."),

        dict(q="Một hệ thống làm mát dùng nước tuần hoàn để tải nhiệt cho một động cơ. "
               "Nước vào ở 30 °C, ra ở 80 °C, lưu lượng 0,20 kg/s.\n"
               "a) Tính công suất nhiệt mà nước mang đi khỏi động cơ.\n"
               "b) Nếu thay nước bằng một chất lỏng có c = 2000 J/(kg·K) mà vẫn muốn tải cùng "
               "công suất nhiệt với cùng độ chênh nhiệt độ, cần lưu lượng bao nhiêu?\n"
               "c) Giải thích vì sao trong kĩ thuật người ta thường chọn nước làm chất tải "
               "nhiệt.\n"
               "d) Nêu một trường hợp thực tế mà người ta buộc phải dùng chất khác thay nước.",
             fig="h13_so_sanh_nhiet_dung",
             ans="a) 42 kW   b) 0,42 kg/s",
             sol="a) Mỗi giây có 0,20 kg nước được nung từ 30 °C lên 80 °C:\n"
                 "P = (m/t)·c·ΔT = 0,20 · 4200 · 50 = 42 000 W = 42 kW.\n\n"
                 "b) Muốn cùng P và cùng ΔT: (m/t)“ = P/(c'·ΔT) = 42 000/(2000 · 50) "
                 "= 42 000/100 000 = 0,42 kg/s.\n"
                 "Cần lưu lượng gấp 2,1 lần, đúng bằng tỉ số 4200/2000.\n\n"
                 "c) Nước có nhiệt dung riêng rất lớn (4200 J/(kg·K)), nên cùng một lưu lượng "
                 "nó tải được nhiều nhiệt hơn hẳn các chất khác. Ngoài ra nước rẻ, sẵn có, "
                 "không độc, không cháy và có độ nhớt thấp nên dễ bơm.\n\n"
                 "d) Khi nhiệt độ làm việc xuống dưới 0 °C (ô tô ở xứ lạnh) thì nước sẽ đóng "
                 "băng và nở ra làm vỡ đường ống, nên phải dùng dung dịch chống đông "
                 "(hỗn hợp nước và ethylene glycol). Tương tự, ở nhiệt độ rất cao vượt quá "
                 "100 °C mà không muốn dùng áp suất lớn thì người ta dùng dầu tải nhiệt."),

        dict(q="Trong một thí nghiệm đo nhiệt nóng chảy riêng của nước đá, học sinh dùng một "
               "điện trở nung công suất 40 W nhúng trong hỗn hợp nước – nước đá đang tan. "
               "Trong 5,0 phút, khối lượng nước tan thêm đo được là 42,0 g. Một phép đo đối "
               "chứng không bật điện trở, trong cùng 5,0 phút, khối lượng nước tan thêm là "
               "6,0 g.\n"
               "a) Vì sao cần phép đo đối chứng?\n"
               "b) Tính nhiệt nóng chảy riêng của nước đá từ số liệu trên.\n"
               "c) Nếu bỏ qua phép đo đối chứng thì kết quả sai lệch bao nhiêu phần trăm?\n"
               "d) Nêu hai nguồn sai số khác của thí nghiệm.",
             fig="h11_do_nhiet_nong_chay",
             ans="b) ≈ 3,33·10⁵ J/kg   c) sai thấp khoảng 14,3 %",
             sol="a) Ngay cả khi không bật điện trở, nhiệt từ không khí và từ thành bình vẫn "
                 "truyền vào hỗn hợp và làm tan một phần nước đá. Phép đo đối chứng đo đúng "
                 "phần này, nhờ đó ta trừ đi được và chỉ giữ lại phần do điện trở gây ra.\n\n"
                 "b) Khối lượng tan do riêng điện trở: m = 42,0 − 6,0 = 36,0 g = 0,0360 kg.\n"
                 "Năng lượng điện: Q = P·t = 40 · 300 = 12 000 J.\n"
                 "λ = Q/m = 12 000/0,0360 ≈ 3,33·10⁵ J/kg. Rất sát giá trị chuẩn 3,34·10⁵ J/kg.\n\n"
                 "c) Nếu dùng thẳng 42,0 g: λ” = 12 000/0,0420 ≈ 2,86·10⁵ J/kg.\n"
                 "Sai lệch: (3,33 − 2,86)/3,33 ≈ 0,143 = 14,3 % — kết quả bị thấp đi.\n\n"
                 "d) Hai nguồn sai số khác:\n"
                 "• Nước tan chưa chảy hết ra khỏi khối đá khi cân, hoặc còn dính lại trên "
                 "phễu, làm khối lượng đo được nhỏ hơn thực tế.\n"
                 "• Công suất đọc trên oát kế có sai số, và một phần nhỏ năng lượng làm nóng "
                 "chính dây dẫn và điện trở chứ không truyền hết cho nước đá."),

        dict(q="Một căn phòng thể tích 60 m³ chứa không khí ở 15 °C. Người ta muốn sưởi ấm "
               "phòng lên 25 °C bằng một máy sưởi công suất 2,0 kW. Cho khối lượng riêng của "
               "không khí là 1,2 kg/m³ và nhiệt dung riêng của không khí là 1000 J/(kg·K).\n"
               "a) Tính khối lượng không khí trong phòng.\n"
               "b) Tính nhiệt lượng cần cung cấp và thời gian sưởi lí thuyết.\n"
               "c) Thực tế thời gian dài hơn nhiều. Nêu ba nguyên nhân.\n"
               "d) So sánh nhiệt lượng này với nhiệt lượng cần để đun sôi 2 lít nước từ 25 °C "
               "và bình luận.",
             ans="a) 72 kg   b) 720 kJ và 360 s",
             sol="a) m = ρ·V = 1,2 · 60 = 72 kg.\n\n"
                 "b) Q = m·c·ΔT = 72 · 1000 · 10 = 720 000 J = 720 kJ.\n"
                 "t = Q/P = 720 000/2000 = 360 s = 6 phút.\n\n"
                 "c) Ba nguyên nhân:\n"
                 "• Nhiệt truyền ra ngoài qua tường, cửa kính và khe hở; quá trình mất nhiệt "
                 "này diễn ra liên tục và tăng dần khi phòng càng ấm.\n"
                 "• Ngoài không khí, máy sưởi còn phải làm nóng cả tường, sàn, đồ đạc — tổng "
                 "nhiệt dung của chúng lớn hơn nhiều so với của không khí.\n"
                 "• Không khí trong phòng liên tục trao đổi với không khí lạnh bên ngoài do "
                 "thông gió và đối lưu.\n\n"
                 "d) Đun 2 lít nước từ 25 °C lên 100 °C cần: 2,0 · 4200 · 75 = 630 000 J "
                 "= 630 kJ, xấp xỉ bằng nhiệt lượng để sưởi cả căn phòng 60 m³ thêm 10 °C. "
                 "Bình luận: nước có nhiệt dung riêng lớn gấp 4,2 lần không khí và mật độ lớn "
                 "gấp gần 1000 lần, nên chỉ 2 kg nước đã “nặng kí” ngang 72 kg không khí về mặt "
                 "năng lượng. Đây là minh hoạ rất rõ cho việc vì sao nước là chất điều hoà "
                 "nhiệt tuyệt vời."),
    ],
}
