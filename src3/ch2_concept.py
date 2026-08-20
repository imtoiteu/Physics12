# -*- coding: utf-8 -*-
"""Bài tập lí thuyết - Chương II: KHÍ LÍ TƯỞNG."""

L1 = "Mức 1 – NHẬN BIẾT"
L2 = "Mức 2 – THÔNG HIỂU"
L3 = "Mức 3 – VẬN DỤNG"
L4 = "Mức 4 – VẬN DỤNG CAO"

MC2 = {
    # ------------------------------------------------------------------ MỨC 1
    L1: [
        dict(q="Định luật Boyle phát biểu rằng ở nhiệt độ không đổi, đối với một lượng khí "
               "xác định thì",
             o=["tích của áp suất và thể tích là một hằng số.",
                "thương của áp suất và thể tích là một hằng số.",
                "tổng của áp suất và thể tích là một hằng số.",
                "hiệu của áp suất và thể tích là một hằng số."],
             a="A",
             e="Định luật Boyle khẳng định pV = hằng số khi nhiệt độ và lượng khí không đổi, "
               "tức là áp suất tỉ lệ nghịch với thể tích. Các phép toán thương, tổng, hiệu đều "
               "không có ý nghĩa vật lí ở đây, thậm chí tổng và hiệu còn không hợp lệ về thứ "
               "nguyên vì áp suất và thể tích khác đơn vị."),

        dict(q="Biểu thức của định luật Charles cho một lượng khí xác định ở áp suất không đổi là",
             o=["V₁/T₁ = V₂/T₂.", "p₁/T₁ = p₂/T₂.", "p₁V₁ = p₂V₂.", "V₁·T₁ = V₂·T₂."],
             a="A",
             e="Định luật Charles mô tả quá trình đẳng áp: thể tích tỉ lệ thuận với nhiệt độ "
               "tuyệt đối, tức V/T là hằng số. Biểu thức p/T = const là quá trình đẳng tích, "
               "còn pV = const là định luật Boyle."),

        dict(q="Trong phương trình pV = nRT, hằng số R có giá trị và đơn vị là",
             o=["8,31 J/(mol·K).", "1,38·10⁻²³ J/K.",
                "6,02·10²³ mol⁻¹.", "9,8 J/(mol·K)."],
             a="A",
             e="R là hằng số khí lí tưởng, bằng 8,31 J/(mol·K). Giá trị 1,38·10⁻²³ J/K là hằng "
               "số Boltzmann k_B, còn 6,02·10²³ mol⁻¹ là số Avogadro. Ba hằng số này liên hệ với "
               "nhau bởi k_B = R/N_A."),

        dict(q="Trong hệ toạ độ (p, V), đường đẳng nhiệt của một lượng khí lí tưởng có dạng",
             o=["một nhánh hypebol.", "một đường thẳng đi qua gốc toạ độ.",
                "một đường thẳng song song với trục hoành.", "một đường thẳng song song với trục tung."],
             a="A",
             e="Từ pV = hằng số suy ra p = const/V, đồ thị là một nhánh hypebol. "
               "Đây là đường cong duy nhất trong bảng đồ thị của ba đẳng quá trình."),

        dict(q="Đơn vị của áp suất trong hệ SI là",
             o=["pascal (Pa).", "atmosphere (atm).", "milimét thuỷ ngân (mmHg).", "bar."],
             a="A",
             e="Đơn vị SI của áp suất là pascal, bằng N/m². Các đơn vị atm, mmHg và bar đều được "
               "dùng phổ biến nhưng không phải đơn vị SI: 1 atm = 1,013·10⁵ Pa = 760 mmHg, "
               "1 bar = 10⁵ Pa."),

        dict(q="Công thức liên hệ giữa động năng tịnh tiến trung bình của một phân tử khí và "
               "nhiệt độ tuyệt đối là",
             o=["W̄ = (3/2)·k_B·T.", "W̄ = (1/3)·k_B·T.",
                "W̄ = (2/3)·k_B·T.", "W̄ = 3·k_B·T²."],
             a="A",
             e="Từ việc so sánh pV = (1/3)Nmv̄² với pV = N·k_B·T ta rút ra "
               "(1/2)mv̄² = (3/2)k_B·T. Hệ số 3/2 xuất phát từ ba bậc tự do tịnh tiến của phân tử."),

        dict(q="Khí lí tưởng là chất khí trong đó",
             o=["các phân tử được coi là chất điểm và chỉ tương tác với nhau khi va chạm.",
                "các phân tử đứng yên và không tương tác với nhau.",
                "các phân tử có kích thước lớn và luôn hút nhau.",
                "các phân tử chuyển động theo cùng một hướng với cùng tốc độ."],
             a="A",
             e="Hai đặc điểm định nghĩa của khí lí tưởng là bỏ qua kích thước riêng của phân tử "
               "(coi là chất điểm) và bỏ qua lực tương tác trừ lúc va chạm. Các phân tử vẫn "
               "chuyển động hỗn loạn không ngừng theo mọi hướng với mọi tốc độ."),

        dict(q="Trong hệ toạ độ (V, T) với T tính bằng kelvin, đường đẳng áp là",
             o=["một đường thẳng đi qua gốc toạ độ.", "một nhánh hypebol.",
                "một đường thẳng song song với trục hoành.",
                "một đường thẳng cắt trục tung tại một điểm khác gốc."],
             a="A",
             e="Định luật Charles cho V/T = hằng số, tức V tỉ lệ thuận với T. Đồ thị của quan hệ "
               "tỉ lệ thuận là đường thẳng đi qua gốc toạ độ. Chỉ khi vẽ theo nhiệt độ Celsius "
               "thì đường thẳng mới không qua gốc."),

        dict(q="Một lượng khí xác định chuyển từ trạng thái 1 sang trạng thái 2. Phương trình "
               "trạng thái của khí lí tưởng có dạng",
             o=["p₁V₁/T₁ = p₂V₂/T₂.", "p₁T₁/V₁ = p₂T₂/V₂.",
                "V₁T₁/p₁ = V₂T₂/p₂.", "p₁V₁T₁ = p₂V₂T₂."],
             a="A",
             e="Phương trình trạng thái khẳng định đại lượng pV/T là bất biến đối với một lượng "
               "khí xác định. Có thể kiểm tra nhanh bằng cách cho T₁ = T₂: biểu thức đúng phải "
               "rút gọn thành định luật Boyle p₁V₁ = p₂V₂."),

        dict(q="Số Avogadro N_A cho biết",
             o=["số phân tử chứa trong 1 mol chất, bằng 6,02·10²³.",
                "khối lượng của 1 mol chất, tính bằng gam.",
                "thể tích của 1 mol khí ở điều kiện tiêu chuẩn, bằng 22,4 L.",
                "số mol chất chứa trong 1 kg chất."],
             a="A",
             e="Số Avogadro là số hạt (phân tử, nguyên tử) trong một mol, bằng 6,02·10²³ mol⁻¹. "
               "Thể tích 22,4 L/mol là thể tích mol ở điều kiện tiêu chuẩn, một đại lượng khác."),

        dict(q="Tốc độ căn quân phương của phân tử khí được định nghĩa là",
             o=["căn bậc hai của trung bình bình phương tốc độ các phân tử.",
                "bình phương của tốc độ trung bình các phân tử.",
                "trung bình cộng tốc độ của tất cả các phân tử.",
                "tốc độ lớn nhất mà một phân tử có thể đạt được."],
             a="A",
             e="Theo định nghĩa v_rms = √(v̄²), tức lấy trung bình của các bình phương tốc độ "
               "rồi mới khai căn. Đại lượng này khác với trung bình cộng đơn thuần của các tốc độ, "
               "và nó gắn trực tiếp với động năng trung bình của phân tử."),

        dict(q="Trong quá trình đẳng tích của một lượng khí xác định thì",
             o=["áp suất tỉ lệ thuận với nhiệt độ tuyệt đối.",
                "áp suất tỉ lệ nghịch với nhiệt độ tuyệt đối.",
                "áp suất không đổi khi nhiệt độ thay đổi.",
                "áp suất tỉ lệ thuận với bình phương nhiệt độ tuyệt đối."],
             a="A",
             e="Từ pV/T = hằng số với V không đổi suy ra p/T = hằng số, tức p tỉ lệ thuận với T. "
               "Trong hệ (p,T), đồ thị là đường thẳng đi qua gốc toạ độ."),

        dict(q="Điều kiện để một chất khí thực có thể coi gần đúng là khí lí tưởng là",
             o=["áp suất không quá cao và nhiệt độ không quá thấp.",
                "áp suất rất cao và nhiệt độ rất thấp.",
                "áp suất rất cao và nhiệt độ rất cao.",
                "khí phải là khí đơn nguyên tử."],
             a="A",
             e="Áp suất cao làm các phân tử ở gần nhau, không còn bỏ qua được thể tích riêng và "
               "lực hút; nhiệt độ thấp làm động năng nhỏ đi, lực hút giữ được phân tử lại và khí "
               "sắp hoá lỏng. Vì vậy điều kiện là áp suất không quá cao, nhiệt độ không quá thấp. "
               "Khí đa nguyên tử như không khí vẫn coi gần đúng là khí lí tưởng được."),

        dict(q="Áp suất của chất khí tác dụng lên thành bình được gây ra bởi",
             o=["sự va chạm của vô số phân tử khí vào thành bình.",
                "trọng lượng của khối khí đè lên thành bình.",
                "lực hút giữa các phân tử khí và thành bình.",
                "sự dãn nở vì nhiệt của thành bình."],
             a="A",
             e="Theo mô hình động học phân tử, mỗi phân tử va chạm đàn hồi với thành bình truyền "
               "cho thành một xung lượng; tổng hợp thống kê của vô số va chạm như vậy tạo ra một "
               "lực trung bình phân bố đều, chính là áp suất."),

        dict(q="Đổi 27 °C sang thang nhiệt độ Kelvin được",
             o=["300 K.", "273 K.", "246 K.", "27 K."],
             a="A",
             e="T = t + 273 = 27 + 273 = 300 K. Đây là một trong những giá trị xuất hiện nhiều "
               "nhất trong bài tập chất khí, nên đáng ghi nhớ."),

        dict(q="Nếu giữ nguyên nhiệt độ và giảm thể tích của một lượng khí xuống một nửa thì "
               "áp suất của khí sẽ",
             o=["tăng gấp đôi.", "giảm một nửa.", "không đổi.", "tăng gấp bốn lần."],
             a="A",
             e="Theo định luật Boyle, pV = hằng số nên p tỉ lệ nghịch với V. Thể tích giảm một "
               "nửa thì áp suất tăng gấp đôi."),

        dict(q="Giả thuyết nào sau đây KHÔNG thuộc thuyết động học phân tử chất khí?",
             o=["Các phân tử khí chuyển động theo quỹ đạo tròn quanh tâm bình chứa.",
                "Các phân tử khí chuyển động hỗn loạn không ngừng.",
                "Kích thước phân tử rất nhỏ so với khoảng cách giữa chúng.",
                "Các phân tử va chạm đàn hồi với nhau và với thành bình."],
             a="A",
             e="Đặc trưng cốt lõi của chuyển động nhiệt là tính HỖN LOẠN: phân tử chuyển động "
               "thẳng đều giữa hai va chạm, theo mọi phương với mọi tốc độ, hoàn toàn không có "
               "quỹ đạo tròn hay tâm quay nào."),

        dict(q="Hằng số Boltzmann k_B liên hệ với hằng số khí R và số Avogadro N_A theo hệ thức",
             o=["k_B = R/N_A.", "k_B = R·N_A.", "k_B = N_A/R.", "k_B = R + N_A."],
             a="A",
             e="Vì pV = nRT = N·k_B·T và N = n·N_A nên nR = N·k_B = n·N_A·k_B, suy ra "
               "k_B = R/N_A = 8,31/6,02·10²³ ≈ 1,38·10⁻²³ J/K."),
    ],

    # ------------------------------------------------------------------ MỨC 2
    L2: [
        dict(q="Nén đẳng nhiệt một lượng khí lí tưởng làm áp suất tăng. Giải thích vi mô đúng là",
             o=["mật độ phân tử tăng nên số va chạm lên một đơn vị diện tích thành bình trong "
                "một đơn vị thời gian tăng, còn tốc độ phân tử không đổi.",
                "tốc độ trung bình của các phân tử tăng lên nên mỗi va chạm vào thành bình đều truyền một xung lượng lớn hơn.",
                "cả mật độ phân tử lẫn tốc độ chuyển động nhiệt của phân tử đều tăng lên khi thể tích bị thu nhỏ lại.",
                "lực hút giữa các phân tử khí tăng lên đáng kể khi chúng bị dồn lại gần nhau hơn, làm cho áp suất tăng."],
             a="A",
             e="Đẳng nhiệt nghĩa là nhiệt độ không đổi, mà nhiệt độ quyết định động năng trung "
               "bình nên tốc độ phân tử KHÔNG đổi. Điều duy nhất thay đổi là mật độ N/V tăng, "
               "làm va chạm xảy ra dày hơn. Nếu tốc độ cũng tăng thì nhiệt độ đã phải tăng, "
               "mâu thuẫn với giả thiết đẳng nhiệt."),

        dict(q="Nung nóng đẳng áp một lượng khí từ 27 °C lên 54 °C. Thể tích khí sẽ",
             o=["tăng khoảng 9 %.", "tăng gấp đôi.", "tăng gấp bốn lần.", "giảm khoảng 9 %."],
             a="A",
             e="Phải đổi ra Kelvin: 27 °C = 300 K, 54 °C = 327 K. "
               "V₂/V₁ = T₂/T₁ = 327/300 = 1,09, tức tăng 9 %. Kết luận “tăng gấp đôi” là bẫy do "
               "nhìn thấy 54 = 2·27 mà quên rằng tỉ lệ thuận chỉ đúng với nhiệt độ TUYỆT ĐỐI."),

        dict(q="Điểm biểu diễn trạng thái của một lượng khí lí tưởng di chuyển trong hệ toạ độ "
               "(p, T) dọc theo một đoạn thẳng song song với trục Op. Quá trình đó là",
             o=["quá trình đẳng nhiệt, trong đó thể tích khí thay đổi.",
                "quá trình đẳng tích, trong đó thể tích khí không đổi.",
                "quá trình đẳng áp, trong đó áp suất khí không đổi.",
                "một quá trình không thể xảy ra với khí lí tưởng."],
             e="Đoạn thẳng song song với trục Op có mọi điểm cùng hoành độ, tức nhiệt độ T "
               "không đổi: đó là quá trình ĐẲNG NHIỆT. Trong quá trình này áp suất thay đổi, "
               "mà pV = nRT với T không đổi, nên thể tích bắt buộc phải thay đổi theo (tỉ lệ "
               "nghịch với áp suất). Nếu là đẳng tích thì đồ thị trong hệ (p, T) phải là đường "
               "thẳng đi qua gốc toạ độ, còn đẳng áp thì phải là đường nằm ngang.",
             a="A"),

        dict(q="Hai bình giống nhau, bình A chứa khí hydrogen (M = 2 g/mol), bình B chứa khí "
               "oxygen (M = 32 g/mol), ở cùng nhiệt độ. So sánh nào sau đây đúng?",
             o=["Động năng tịnh tiến trung bình của một phân tử ở hai bình bằng nhau, nhưng "
                "phân tử hydrogen có tốc độ căn quân phương lớn hơn.",
                "Cả động năng tịnh tiến trung bình lẫn tốc độ căn quân phương của hai loại "
                "phân tử đều bằng nhau.",
                "Phân tử oxygen có động năng tịnh tiến trung bình lớn hơn vì khối lượng phân tử của nó lớn hơn nhiều.",
                "Phân tử hydrogen có động năng tịnh tiến trung bình lớn hơn vì nó chuyển động nhanh hơn hẳn phân tử oxygen."],
             a="A",
             e="Động năng tịnh tiến trung bình W̄ = (3/2)k_B·T chỉ phụ thuộc nhiệt độ, không phụ "
               "thuộc loại khí, nên hai bình cho cùng giá trị. Nhưng v_rms = √(3RT/M) tỉ lệ nghịch "
               "với √M, nên phân tử hydrogen nhẹ hơn 16 lần sẽ có v_rms lớn hơn √16 = 4 lần."),

        dict(q="Một bóng thám không được bơm khí và thả lên cao. Khi bóng lên cao, thể tích của "
               "nó tăng lên chủ yếu vì",
             o=["áp suất khí quyển bên ngoài giảm mạnh theo độ cao.",
                "nhiệt độ không khí trên cao tăng lên.",
                "khối lượng khí trong bóng tăng lên.",
                "vỏ bóng dãn nở vì nhiệt."],
             a="A",
             e="Càng lên cao, áp suất khí quyển càng giảm nên khí trong bóng nở ra để áp suất "
               "bên trong cân bằng với bên ngoài. Nhiệt độ trên cao thực ra thường GIẢM, tác dụng "
               "này làm co bóng lại nhưng yếu hơn nhiều so với tác dụng của việc giảm áp suất. "
               "Đó là lí do bóng thám không không được bơm căng từ mặt đất."),

        dict(q="Trong hệ toạ độ (V, t) với t tính bằng độ Celsius, đường đẳng áp của một lượng "
               "khí lí tưởng khi kéo dài sẽ cắt trục hoành tại",
             o=["t = −273,15 °C.", "t = 0 °C.", "t = 273,15 °C.", "t = −100 °C."],
             a="A",
             e="Từ V = V₀(1 + t/273,15), thể tích ngoại suy bằng 0 khi t = −273,15 °C. "
               "Chính phép ngoại suy này dẫn tới khái niệm độ không tuyệt đối. Cần nhấn mạnh đây "
               "chỉ là ngoại suy toán học, vì trên thực tế khí đã hoá lỏng từ lâu trước đó."),

        dict(q="Vì sao không được ném bình xịt hoặc bật lửa ga đã dùng hết vào lửa?",
             o=["Vì thể tích bình không đổi, nhiệt độ tăng làm áp suất khí bên trong tăng vọt, "
                "có thể gây nổ.",
                "Vì khí trong bình sẽ dãn nở làm bình phồng lên rồi từ từ xẹp xuống.",
                "Vì nhiệt độ tăng làm áp suất khí bên trong giảm mạnh, tạo ra chân không hút cho bình "
                "bị méo lại.",
                "Vì khí trong bình sẽ hoá lỏng khi gặp nhiệt độ cao."],
             a="A",
             e="Bình kim loại có thể tích gần như không đổi nên đây là quá trình đẳng tích: "
               "p/T = hằng số. Nhiệt độ tăng nhanh làm áp suất tăng tỉ lệ, vượt quá sức chịu "
               "đựng của vỏ bình và gây nổ."),

        dict(q="Phát biểu nào sau đây SAI khi nói về mối liên hệ giữa nhiệt độ và tốc độ phân tử?",
             o=["Nhiệt độ tuyệt đối tăng gấp đôi thì tốc độ căn quân phương tăng gấp đôi.",
                "Nhiệt độ tuyệt đối tăng gấp bốn lần thì tốc độ căn quân phương tăng gấp đôi.",
                "Ở cùng nhiệt độ, phân tử có khối lượng nhỏ hơn thì chuyển động nhanh hơn.",
                "Ở 0 K, động năng tịnh tiến trung bình của phân tử bằng 0."],
             a="A",
             e="Vì v_rms = √(3k_B·T/m) tỉ lệ với căn bậc hai của T, nên T tăng gấp đôi chỉ làm "
               "v_rms tăng √2 ≈ 1,41 lần. Muốn v_rms tăng gấp đôi thì T phải tăng gấp bốn lần. "
               "Ba nhận định còn lại đều đúng."),

        dict(q="Một khối khí lí tưởng có áp suất p, thể tích V, nhiệt độ T. Nếu đồng thời tăng "
               "áp suất gấp đôi và tăng nhiệt độ tuyệt đối gấp đôi thì thể tích sẽ",
             o=["không đổi.", "tăng gấp đôi.", "giảm một nửa.", "tăng gấp bốn lần."],
             a="A",
             e="Từ pV/T = hằng số suy ra V = (hằng số)·T/p. Khi cả T và p đều tăng gấp đôi, "
               "tỉ số T/p không đổi nên V giữ nguyên. Đây là bài kiểm tra việc học sinh có nắm "
               "được cấu trúc của phương trình trạng thái hay chỉ nhớ máy móc từng định luật."),

        dict(q="Hai đường đẳng nhiệt của cùng một lượng khí lí tưởng ứng với hai nhiệt độ T₁ và "
               "T₂ được vẽ trong hệ (p, V). Đường ứng với nhiệt độ cao hơn",
             o=["nằm xa gốc toạ độ hơn.", "nằm gần gốc toạ độ hơn.",
                "cắt đường kia tại đúng một điểm.", "song song với đường kia."],
             a="A",
             e="Với cùng một thể tích V, khí ở nhiệt độ cao hơn có áp suất lớn hơn (vì "
               "p = nRT/V). Do đó đường đẳng nhiệt ứng với T lớn hơn nằm phía trên, tức xa gốc "
               "toạ độ hơn. Hai đường đẳng nhiệt của cùng một lượng khí không bao giờ cắt nhau, "
               "vì mỗi điểm (p,V) chỉ ứng với một nhiệt độ duy nhất."),

        dict(q="Khi kiểm chứng định luật Boyle bằng thực nghiệm, người ta thường vẽ đồ thị p theo "
               "1/V thay vì p theo V. Lí do chính là",
             o=["mắt người phân biệt đường thẳng với đường cong tốt hơn nhiều so với phân biệt "
                "hypebol với một đường cong gần giống nó.",
                "đồ thị p theo V không thể vẽ được vì hai đại lượng này có đơn vị khác nhau nên không so sánh được với nhau.",
                "định luật Boyle chỉ được nghiệm đúng khi biểu diễn áp suất theo nghịch đảo của thể tích chứ không theo thể tích.",
                "đại lượng 1/V dễ đo trực tiếp hơn đại lượng V trong bộ thí nghiệm khảo sát định luật Boyle."],
             a="A",
             e="Đây là kĩ thuật tuyến tính hoá. Một hypebol thật và một đường cong sai lệch nhẹ "
               "trông rất giống nhau, nhưng khi chuyển sang biến 1/V thì quan hệ trở thành đường "
               "thẳng qua gốc toạ độ — và độ lệch khỏi đường thẳng thì mắt phát hiện được ngay.",
             fig="h30_do_thi_boyle_thuc_nghiem"),

        dict(q="Trong thí nghiệm minh hoạ định luật Charles, người ta dùng một giọt thuỷ ngân "
               "để nút ống nghiệm chứa khí. Vai trò của giọt thuỷ ngân là",
             o=["nhốt kín lượng khí đồng thời di chuyển tự do được để giữ áp suất khí không đổi.",
                "làm cho áp suất của khí bên trong ống tăng dần lên theo nhiệt độ của nước.",
                "giữ cho thể tích của cột khí trong ống luôn không đổi.",
                "đo nhiệt độ của cột khí bị nhốt bên trong ống nghiệm."],
             a="A",
             e="Giọt thuỷ ngân vừa ngăn khí thoát ra, vừa trượt tự do trong ống nên áp suất khí "
               "luôn cân bằng với áp suất khí quyển cộng phần do trọng lượng giọt gây ra, tức là "
               "không đổi. Nhờ đó quá trình mới là đẳng áp. Nếu bịt kín ống thì thể tích không "
               "đổi và thí nghiệm trở thành đẳng tích.",
             fig="h19_thi_nghiem_charles"),

        dict(q="Một bình kín thể tích không đổi chứa khí ở nhiệt độ không đổi. Nếu một nửa số "
               "phân tử khí thoát ra ngoài thì áp suất khí trong bình",
             o=["giảm còn một nửa.", "không đổi.", "giảm còn một phần tư.", "tăng gấp đôi."],
             a="A",
             e="Dùng pV = N·k_B·T với V và T không đổi thì p tỉ lệ thuận với N. Số phân tử giảm "
               "một nửa thì áp suất giảm một nửa. Lưu ý bài này KHÔNG dùng được p₁V₁ = p₂V₂ vì "
               "lượng khí đã thay đổi."),

        dict(q="Cùng một lượng khí lí tưởng, quá trình nào sau đây có thể làm nhiệt độ tăng mà "
               "áp suất vẫn giữ nguyên?",
             o=["Quá trình đẳng áp với thể tích tăng.",
                "Quá trình đẳng tích với thể tích không đổi.",
                "Quá trình đẳng nhiệt với thể tích giảm.",
                "Không có quá trình nào như vậy."],
             a="A",
             e="Từ pV/T = hằng số, muốn giữ p cố định mà tăng T thì V phải tăng theo cùng tỉ lệ. "
               "Đó chính là quá trình đẳng áp — quá trình xảy ra khi khí được đun trong xilanh "
               "có pit-tông di chuyển tự do."),

        dict(q="Đường đẳng tích trong hệ toạ độ (p, T) của hai lượng khí giống nhau nhưng chứa "
               "trong hai bình có thể tích V₁ < V₂. So sánh độ dốc hai đường:",
             o=["Đường ứng với V₁ dốc hơn.", "Đường ứng với V₂ dốc hơn.",
                "Hai đường có cùng độ dốc.", "Hai đường song song với trục hoành."],
             a="A",
             e="Từ pV = nRT suy ra p = (nR/V)·T, hệ số góc là nR/V. Thể tích càng nhỏ thì hệ số "
               "góc càng lớn, đường càng dốc. Về mặt vật lí: cùng một lượng khí bị nhốt trong "
               "bình nhỏ hơn thì áp suất tăng nhanh hơn khi được nung nóng.",
             fig="h26_do_thi_p_T_dang_tich"),

        dict(q="Nhận định nào sau đây về nội năng của khí lí tưởng là ĐÚNG?",
             o=["Nội năng chỉ gồm động năng của các phân tử và chỉ phụ thuộc nhiệt độ.",
                "Nội năng gồm cả động năng và thế năng tương tác, phụ thuộc cả nhiệt độ lẫn "
                "thể tích.",
                "Nội năng chỉ gồm thế năng tương tác giữa các phân tử.",
                "Nội năng của khí lí tưởng luôn bằng 0."],
             a="A",
             e="Theo định nghĩa khí lí tưởng, các phân tử chỉ tương tác lúc va chạm nên thế năng "
               "tương tác coi như bằng 0. Nội năng chỉ còn tổng động năng: U = (3/2)n·R·T (với "
               "khí đơn nguyên tử), chỉ phụ thuộc nhiệt độ.",
             fig="h29_noi_nang_khi"),

        dict(q="Lốp xe máy sau khi chạy đường dài thường căng hơn lúc mới bơm. Giải thích đúng là",
             o=["ma sát làm nhiệt độ khí trong lốp tăng, thể tích gần như không đổi nên áp suất "
                "tăng.",
                "khí trong lốp nở ra làm cho lốp căng hơn nhưng áp suất bên trong lại giảm đi.",
                "một lượng khí từ ngoài đã lọt thêm vào trong lốp.",
                "cao su bị mòn nên thể tích lốp giảm mạnh làm áp suất tăng."],
             a="A",
             e="Ma sát giữa lốp và mặt đường cùng với biến dạng liên tục của cao su làm nhiệt độ "
               "khí trong lốp tăng. Vì lốp gần như không đổi thể tích, đây là quá trình đẳng tích: "
               "p/T = hằng số, nhiệt độ tăng kéo theo áp suất tăng. Đó là lí do khuyến cáo kiểm "
               "tra áp suất lốp khi lốp còn nguội."),

        dict(q="Trong công thức p = (1/3)·ρ·v̄², đại lượng ρ là",
             o=["khối lượng riêng của khối khí.", "áp suất riêng phần của khí.",
                "mật độ số phân tử trong một đơn vị thể tích.", "khối lượng của một phân tử khí."],
             a="A",
             e="Từ pV = (1/3)Nmv̄², chia hai vế cho V ta được p = (1/3)·(Nm/V)·v̄². "
               "Đại lượng Nm/V là tổng khối lượng chia cho thể tích, tức khối lượng riêng ρ của "
               "khối khí. Mật độ số phân tử là N/V, khác với ρ ở thừa số m."),

        dict(q="Một bình chứa khí được đun nóng đẳng tích. Phát biểu nào sau đây SAI?",
             o=["Khoảng cách trung bình giữa các phân tử khí tăng lên.",
                "Tốc độ căn quân phương của các phân tử tăng lên.",
                "Số va chạm của phân tử lên thành bình trong một đơn vị thời gian tăng lên.",
                "Áp suất khí tác dụng lên thành bình tăng lên."],
             a="A",
             e="Đẳng tích nghĩa là thể tích bình không đổi, mà số phân tử cũng không đổi, "
               "nên mật độ phân tử và do đó khoảng cách trung bình giữa chúng KHÔNG thay đổi. "
               "Ba hệ quả còn lại đều đúng: nhiệt độ tăng làm phân tử nhanh hơn, va chạm dày hơn "
               "và mạnh hơn nên áp suất tăng."),

        dict(q="Một cột khí bị nhốt trong ống thuỷ tinh thẳng đứng, phía trên khí là cột thuỷ "
               "ngân cao h, miệng ống mở hướng lên. Áp suất của cột khí là",
             o=["p = p₀ + h.", "p = p₀ − h.", "p = h − p₀.", "p = p₀ (cột thuỷ ngân không ảnh hưởng)."],
             a="A",
             e="Cột thuỷ ngân nằm phía trên nên đè xuống khối khí, cộng thêm áp suất của nó vào "
               "áp suất khí quyển. Nếu lật ngược ống cho miệng hướng xuống thì cột thuỷ ngân kéo "
               "khí xuống và áp suất khí là p₀ − h.",
             fig="h24_ong_chu_U"),
    ],

    # ------------------------------------------------------------------ MỨC 3
    L3: [
        dict(q="Một chu trình gồm ba giai đoạn được biểu diễn trong hệ (p, V) như hình vẽ. "
               "Nhận định nào sau đây đúng về giai đoạn (1)→(2)?",
             o=["Đó là quá trình đẳng tích, nhiệt độ tuyệt đối của khí giảm còn một phần ba.",
                "Đó là quá trình đẳng áp, nhiệt độ tuyệt đối của khí giảm còn một phần ba.",
                "Đó là quá trình đẳng nhiệt, thể tích khí giảm còn một phần ba.",
                "Đó là quá trình đẳng tích, nhiệt độ tuyệt đối của khí tăng gấp ba."],
             a="A",
             e="Đoạn (1)→(2) là đoạn thẳng đứng trong hệ (p,V): thể tích giữ nguyên 2 L trong khi "
               "áp suất giảm từ 3 atm xuống 1 atm. Đó là quá trình đẳng tích. "
               "Từ p/T = hằng số, áp suất giảm còn một phần ba thì nhiệt độ tuyệt đối cũng giảm "
               "còn một phần ba.",
             fig="h22_chu_trinh_pV"),

        dict(q="Nén một lượng khí lí tưởng RẤT NHANH từ thể tích V xuống V/2 trong một bình cách "
               "nhiệt. Áp suất sau khi nén sẽ",
             o=["lớn hơn 2p, vì nhiệt độ khí đã tăng lên.",
                "đúng bằng 2p, theo định luật Boyle.",
                "nhỏ hơn 2p, vì một phần năng lượng bị mất.",
                "không xác định được vì thiếu dữ kiện."],
             a="A",
             e="Nén rất nhanh trong bình cách nhiệt là quá trình gần đoạn nhiệt chứ không phải "
               "đẳng nhiệt: Q ≈ 0 và A > 0 nên nội năng và nhiệt độ tăng. "
               "Từ pV/T = hằng số, khi V giảm một nửa mà T lại tăng thì p phải tăng nhiều hơn "
               "gấp đôi. Định luật Boyle chỉ áp dụng được nếu nén CHẬM để nhiệt độ kịp cân bằng "
               "với môi trường."),

        dict(q="Một bình thể tích 20 L chứa khí ở áp suất 6,0·10⁵ Pa, nhiệt độ 27 °C. Người ta "
               "mở van cho khí thoát ra tới khi áp suất còn 2,0·10⁵ Pa, nhiệt độ vẫn giữ 27 °C. "
               "Phần trăm khối lượng khí đã thoát ra là",
             o=["66,7 %.", "33,3 %.", "50,0 %.", "25,0 %."],
             a="A",
             e="Bình có V và T không đổi nên từ pV = nRT suy ra n tỉ lệ thuận với p. "
               "Tỉ số khí còn lại: n₂/n₁ = p₂/p₁ = 2,0/6,0 = 1/3. Vậy đã thoát ra 2/3, "
               "tức 66,7 %. Bài này không dùng được p₁V₁ = p₂V₂ vì lượng khí thay đổi."),

        dict(q="Trong một xilanh nằm ngang, pit-tông nhẹ không ma sát chia xilanh thành hai ngăn "
               "chứa hai lượng khí khác nhau. Điều kiện cân bằng của pit-tông cho biết",
             o=["áp suất hai ngăn bằng nhau, còn nhiệt độ và thể tích hai ngăn có thể khác nhau.",
                "cả áp suất, thể tích và nhiệt độ hai ngăn đều bằng nhau.",
                "thể tích hai ngăn bằng nhau, còn áp suất và nhiệt độ thì có thể khác nhau.",
                "tích pV của hai ngăn bằng nhau."],
             a="A",
             e="Pit-tông nhẹ, không ma sát, nằm ngang nên hai lực áp lực từ hai phía phải cân "
               "bằng: p_A·S = p_B·S, suy ra p_A = p_B. Đây là ràng buộc DUY NHẤT mà điều kiện "
               "cân bằng đem lại; thể tích và nhiệt độ hai ngăn hoàn toàn có thể khác nhau. "
               "Ràng buộc thứ hai cần thiết cho bài toán là tổng thể tích không đổi.",
             fig="h27_pit_tong_hai_ngan"),

        dict(q="Một lượng khí lí tưởng thực hiện quá trình sao cho áp suất tỉ lệ thuận với thể "
               "tích, tức p = k·V. Trong quá trình này, nhiệt độ tuyệt đối của khí",
             o=["tỉ lệ thuận với bình phương thể tích.",
                "tỉ lệ thuận với thể tích.",
                "tỉ lệ nghịch với thể tích.",
                "không thay đổi."],
             a="A",
             e="Thay p = kV vào pV = nRT được kV² = nRT, suy ra T = kV²/(nR), tức T tỉ lệ thuận "
               "với V². Trên giản đồ (p,V) quá trình này là một đường thẳng đi qua gốc toạ độ, "
               "hoàn toàn khác với đường đẳng nhiệt là hypebol."),

        dict(q="Cho hai khí helium (M = 4 g/mol) và argon (M = 40 g/mol) ở cùng nhiệt độ. "
               "Tỉ số tốc độ căn quân phương v_He/v_Ar bằng",
             o=["√10 ≈ 3,16.", "10.", "1/√10 ≈ 0,316.", "1."],
             a="A",
             e="Từ v_rms = √(3RT/M), ở cùng nhiệt độ thì v tỉ lệ nghịch với √M. "
               "v_He/v_Ar = √(M_Ar/M_He) = √(40/4) = √10 ≈ 3,16. Kết quả 10 là quên khai căn, "
               "còn 0,316 là đảo ngược tỉ số."),

        dict(q="Trong hệ (p, V), điểm M có toạ độ (2 L; 3·10⁵ Pa) và điểm N có toạ độ "
               "(6 L; 1·10⁵ Pa) như hình vẽ. Quá trình đưa khí từ M tới N",
             o=["có thể là quá trình đẳng nhiệt, vì tích pV của hai trạng thái bằng nhau.",
                "chắc chắn là quá trình đẳng áp, vì áp suất giảm đều.",
                "chắc chắn là quá trình đẳng tích.",
                "không thể thực hiện được vì cả áp suất lẫn thể tích đều thay đổi cùng lúc."],
             a="A",
             e="Tính tích pV: tại A là 2·3 = 6 và tại B là 6·1 = 6 (cùng đơn vị L·10⁵ Pa). "
               "Hai tích bằng nhau nên hai trạng thái có cùng nhiệt độ, và tồn tại một quá trình "
               "đẳng nhiệt nối chúng. Lưu ý cách diễn đạt “có thể là” — hai trạng thái cùng nhiệt "
               "độ vẫn có thể được nối bằng nhiều đường khác nhau.",
             fig="h28_do_thi_pV_doc_hieu"),

        dict(q="Một khối khí lí tưởng ở 27 °C có tốc độ căn quân phương là 500 m/s. Để tốc độ "
               "căn quân phương đạt 1000 m/s thì nhiệt độ phải là",
             o=["927 °C.", "327 °C.", "600 °C.", "1200 °C."],
             a="A",
             e="Vì v_rms ∝ √T nên T₂/T₁ = (v₂/v₁)² = 2² = 4. "
               "T₁ = 300 K nên T₂ = 1200 K, tương ứng t₂ = 1200 − 273 = 927 °C. "
               "Đáp số 1200 là quên đổi ngược về Celsius, còn 327 °C ứng với việc chỉ nhân đôi "
               "nhiệt độ tuyệt đối."),

        dict(q="Ở điều kiện tiêu chuẩn (0 °C, 1 atm), 1 mol khí lí tưởng chiếm thể tích 22,4 L. "
               "Số phân tử khí trong 1 cm³ khí ở điều kiện đó xấp xỉ",
             o=["2,7·10¹⁹.", "6,0·10²³.", "2,7·10²².", "4,5·10¹⁶."],
             a="A",
             e="1 mol chiếm 22,4 L = 22 400 cm³ và chứa 6,02·10²³ phân tử. "
               "Số phân tử trong 1 cm³ = 6,02·10²³/22 400 ≈ 2,7·10¹⁹. "
               "Con số này (gọi là số Loschmidt) đáng nhớ để ước lượng nhanh."),

        dict(q="Một bình kín chứa khí ở 27 °C và áp suất 1,0·10⁵ Pa. Bình chịu được áp suất tối "
               "đa 3,0·10⁵ Pa. Nhiệt độ tối đa mà bình chịu được là",
             o=["627 °C.", "900 °C.", "81 °C.", "354 °C."],
             a="A",
             e="Bình kín nên đẳng tích: p/T = hằng số. T₂ = T₁·p₂/p₁ = 300·3 = 900 K, "
               "tương ứng t₂ = 900 − 273 = 627 °C. Đáp số 900 là quên đổi về Celsius, còn 81 °C "
               "là kết quả của việc nhân 27 với 3."),

        dict(q="Một quả bóng cao su chứa khí ở áp suất 1,2·10⁵ Pa, thể tích 2,0 L, nhiệt độ "
               "27 °C. Bóng được đưa xuống nước sâu nơi áp suất là 2,0·10⁵ Pa và nhiệt độ 7 °C. "
               "Thể tích của bóng khi đó là",
             o=["1,12 L.", "1,20 L.", "1,29 L.", "3,57 L."],
             a="A",
             e="Dùng p₁V₁/T₁ = p₂V₂/T₂ với T₁ = 300 K, T₂ = 280 K: "
               "V₂ = p₁V₁T₂/(p₂T₁) = 1,2·2,0·280/(2,0·300) = 672/600 = 1,12 L. "
               "Đáp số 1,20 L là chỉ dùng định luật Boyle mà bỏ qua thay đổi nhiệt độ."),

        dict(q="Trong hệ toạ độ (V, T), một lượng khí lí tưởng đi từ trạng thái 1 đến trạng thái "
               "2 theo một đường thẳng đi qua gốc toạ độ. Quá trình này là",
             o=["đẳng áp.", "đẳng nhiệt.", "đẳng tích.", "không phải đẳng quá trình nào."],
             a="A",
             e="Đường thẳng qua gốc trong hệ (V,T) nghĩa là V/T = hằng số, đó chính là biểu thức "
               "của định luật Charles cho quá trình đẳng áp. Đây là ứng dụng trực tiếp của bảng "
               "nhận dạng đồ thị ba đẳng quá trình.",
             fig="h21_ba_dang_qua_trinh"),

        dict(q="Một bình dung tích 5,0 L chứa khí oxygen ở 27 °C, áp suất 8,0·10⁵ Pa. "
               "Khối lượng khí trong bình là (M = 32 g/mol, R = 8,31 J/(mol·K))",
             o=["≈ 51,3 g.", "≈ 32,0 g.", "≈ 1,60 g.", "≈ 513 g."],
             a="A",
             e="Đổi đơn vị: V = 5,0·10⁻³ m³, T = 300 K. "
               "n = pV/(RT) = 8,0·10⁵ · 5,0·10⁻³/(8,31·300) = 4000/2493 ≈ 1,604 mol. "
               "m = n·M = 1,604·32 ≈ 51,3 g. Đáp số 1,60 là nhầm số mol thành khối lượng."),

        dict(q="Hai bình A và B nối với nhau bằng một ống nhỏ có khoá. Bình A thể tích V chứa "
               "khí ở áp suất p, bình B thể tích 2V đã hút chân không. Mở khoá cho khí phân bố "
               "đều, giữ nhiệt độ không đổi. Áp suất cuối cùng là",
             o=["p/3.", "p/2.", "2p/3.", "3p."],
             a="A",
             e="Lượng khí không đổi, nhiệt độ không đổi nên áp dụng định luật Boyle với thể tích "
               "tổng: p·V = p'·(V + 2V) = p'·3V, suy ra p' = p/3. "
               "Sai lầm thường gặp là chỉ tính thể tích bình B mà quên rằng khí chiếm cả hai bình."),

        dict(q="Vì sao khi mở nút chai nước ngọt có ga, ta nghe tiếng “xì” và thấy bọt khí nổi lên?",
             o=["Vì áp suất khí phía trên mặt nước trong chai lớn hơn áp suất khí quyển; khi mở "
                "nút, áp suất giảm đột ngột nên khí hoà tan thoát ra.",
                "Vì nhiệt độ của chất lỏng trong chai cao hơn nhiệt độ bên ngoài nên khí hoà tan trong đó dãn nở và thoát ra.",
                "Vì thể tích phần chứa khí trong chai tăng lên đột ngột ngay khi nút chai được mở ra.",
                "Vì không khí bên ngoài tràn vào chai làm áp suất phía trên mặt chất lỏng trong chai tăng lên."],
             a="A",
             e="Nước ngọt có ga được nạp CO₂ ở áp suất cao; lượng khí hoà tan tỉ lệ với áp suất "
               "phía trên chất lỏng. Khi mở nút, áp suất tụt xuống bằng áp suất khí quyển nên "
               "khả năng hoà tan giảm mạnh, CO₂ dư thoát ra thành bọt kèm tiếng xì của khí nén "
               "phía trên thoát ra ngoài."),

        dict(q="Trong hệ toạ độ (p, T), một lượng khí đi từ trạng thái 1 sang trạng thái 2 theo "
               "một đường thẳng KHÔNG đi qua gốc toạ độ. Kết luận nào sau đây đúng?",
             o=["Thể tích của khí đã thay đổi trong quá trình.",
                "Đó chắc chắn là quá trình đẳng tích.",
                "Đó chắc chắn là quá trình đẳng nhiệt.",
                "Quá trình đó không thể xảy ra."],
             a="A",
             e="Quá trình đẳng tích trong hệ (p,T) phải là đường thẳng ĐI QUA gốc toạ độ, vì "
               "p = (nR/V)·T. Nếu đường thẳng không qua gốc thì tỉ số p/T thay đổi, mà "
               "p/T = nR/V, nên V bắt buộc phải thay đổi trong quá trình."),
    ],

    # ------------------------------------------------------------------ MỨC 4
    L4: [
        dict(q="Một học sinh lập luận: “Khi nén khí đẳng nhiệt, các phân tử bị dồn lại gần nhau "
               "hơn nên chúng va chạm mạnh hơn, do đó áp suất tăng.” Nhận xét đúng là",
             o=["Kết luận đúng nhưng lí do sai: mỗi va chạm vẫn có cường độ như cũ vì tốc độ "
                "phân tử không đổi; áp suất tăng là do va chạm xảy ra DÀY hơn.",
                "Cả kết luận lẫn lí do mà học sinh đó đưa ra đều hoàn toàn chính xác.",
                "Kết luận sai, vì nén một lượng khí ở nhiệt độ không đổi thì áp suất của nó giảm đi chứ không tăng lên.",
                "Kết luận đúng và lí do cũng đúng, nhưng lập luận còn thiếu vai trò của lực hút giữa các phân tử khí."],
             a="A",
             e="Cường độ mỗi va chạm được quyết định bởi xung lượng 2mv, mà v chỉ phụ thuộc nhiệt "
               "độ. Đẳng nhiệt nghĩa là v không đổi nên mỗi va chạm “mạnh” như cũ. Cái tăng lên "
               "là TẦN SUẤT va chạm, do mật độ phân tử tăng. Phân biệt được “mạnh hơn” và "
               "“dày hơn” là dấu hiệu hiểu đúng bản chất."),

        dict(q="Một xilanh nằm ngang có pit-tông nhẹ không ma sát chia thành hai ngăn thể tích "
               "bằng nhau, mỗi ngăn chứa cùng một lượng khí ở cùng nhiệt độ T. Nếu chỉ nung nóng "
               "ngăn trái lên 2T và giữ ngăn phải ở T thì pit-tông sẽ",
             o=["dịch sang phải, và ở vị trí cân bằng mới thể tích ngăn trái gấp đôi ngăn phải.",
                "dịch sang phải, và ở vị trí cân bằng mới thể tích ngăn trái gấp bốn lần ngăn phải.",
                "đứng yên vì áp suất hai bên vẫn bằng nhau.",
                "dịch sang trái vì khí nóng có áp suất lớn hơn."],
             a="A",
             e="Ở cân bằng mới, áp suất hai ngăn vẫn bằng nhau (gọi là p') và tổng thể tích không "
               "đổi: V_T + V_P = 2V. Với cùng số mol n: p'V_T = nR·2T và p'V_P = nR·T. "
               "Chia hai vế: V_T/V_P = 2, kết hợp V_T + V_P = 2V cho V_T = 4V/3 và V_P = 2V/3. "
               "Vậy pit-tông dịch sang phải và thể tích ngăn trái gấp đôi ngăn phải.",
             fig="h27_pit_tong_hai_ngan"),

        dict(q="Một ống thuỷ tinh dài, một đầu kín, chứa cột khí dài 20 cm bị nhốt bởi cột thuỷ "
               "ngân dài 10 cm. Áp suất khí quyển là 75 cmHg. Khi ống đặt thẳng đứng miệng ở "
               "trên và khi đặt thẳng đứng miệng ở dưới, tỉ số chiều dài cột khí là",
             o=["ℓ_trên/ℓ_dưới = 65/85.", "ℓ_trên/ℓ_dưới = 85/65.",
                "ℓ_trên/ℓ_dưới = 1.", "ℓ_trên/ℓ_dưới = 75/85."],
             a="A",
             e="Khi miệng ở trên, thuỷ ngân đè lên khí: p₁ = 75 + 10 = 85 cmHg. "
               "Khi miệng ở dưới, thuỷ ngân kéo khí: p₂ = 75 − 10 = 65 cmHg. "
               "Nhiệt độ không đổi nên p·ℓ = hằng số (tiết diện không đổi): "
               "ℓ_trên/ℓ_dưới = p₂/p₁ = 65/85. Cột khí ở tư thế miệng trên bị nén ngắn hơn "
               "vì chịu áp suất lớn hơn.",
             fig="h24_ong_chu_U"),

        dict(q="Cùng một bình kín, người ta lần lượt chứa 1 mol khí helium rồi 1 mol khí oxygen, "
               "ở cùng nhiệt độ. So sánh nào sau đây đúng?",
             o=["Áp suất hai lần bằng nhau, nhưng tốc độ căn quân phương của helium lớn hơn.",
                "Áp suất khi chứa oxygen lớn hơn vì phân tử nặng hơn.",
                "Áp suất khi chứa helium lớn hơn vì phân tử chuyển động nhanh hơn.",
                "Cả áp suất lẫn tốc độ căn quân phương của hai khí đều bằng nhau."],
             a="A",
             e="Từ pV = nRT, với cùng n, V, T thì p như nhau bất kể loại khí — đây là một kết quả "
               "phản trực giác nhưng rất quan trọng. Về mặt vi mô: phân tử oxygen nặng hơn nên "
               "mỗi va chạm truyền xung lượng lớn hơn, nhưng nó lại chậm hơn nên va chạm thưa "
               "hơn; hai hiệu ứng bù trừ chính xác cho nhau. Còn v_rms = √(3RT/M) thì helium "
               "nhẹ hơn nên nhanh hơn."),

        dict(q="Một khối khí lí tưởng thực hiện chu trình gồm ba giai đoạn: đẳng tích tăng áp, "
               "đẳng áp dãn nở, rồi đẳng nhiệt trở về trạng thái đầu. Trong hệ toạ độ (V, T), "
               "chu trình này gồm",
             o=["một đoạn nằm ngang, một đoạn thẳng đi qua gốc toạ độ và một đoạn thẳng đứng.",
                "ba đoạn thẳng và cả ba đều đi qua gốc toạ độ.",
                "một đoạn nằm ngang, một nhánh hypebol và một đoạn thẳng đứng.",
                "một nhánh hypebol và hai đoạn thẳng nằm ngang song song."],
             a="A",
             e="Xét từng giai đoạn trong hệ (V, T). Đẳng tích: V không đổi, mà V là trục tung, "
               "nên đó là đoạn NẰM NGANG. Đẳng áp: V/T = hằng số, tỉ lệ thuận, nên là đoạn thẳng "
               "ĐI QUA GỐC toạ độ. Đẳng nhiệt: T không đổi, mà T là trục hoành, nên là đoạn "
               "THẲNG ĐỨNG. Hypebol chỉ xuất hiện với đường đẳng nhiệt trong hệ (p, V), "
               "không xuất hiện trong hệ (V, T).",
             fig="h21_ba_dang_qua_trinh"),

        dict(q="Hai bình giống hệt nhau nối bằng ống nhỏ có khoá, ban đầu cùng chứa khí ở 27 °C "
               "và 1,0·10⁵ Pa. Đóng khoá, nung bình A lên 127 °C còn bình B giữ 27 °C, rồi mở "
               "khoá. Áp suất chung sau khi mở khoá (bỏ qua thể tích ống, nhiệt độ mỗi bình "
               "giữ nguyên) là",
             o=["≈ 1,14·10⁵ Pa.", "≈ 1,00·10⁵ Pa.", "≈ 1,17·10⁵ Pa.", "≈ 1,33·10⁵ Pa."],
             a="A",
             e="Gọi mỗi bình có thể tích V, tổng số mol ban đầu n_tổng = 2·p₀V/(R·300). "
               "Sau khi mở khoá, áp suất chung p' nhưng nhiệt độ hai bình khác nhau: "
               "n_A = p'V/(R·400), n_B = p'V/(R·300). Bảo toàn số mol: "
               "p'V/R·(1/400 + 1/300) = 2p₀V/(R·300) → p'·(3 + 4)/1200 = 2p₀/300 "
               "→ p'·7/1200 = 8p₀/1200 → p' = 8p₀/7 ≈ 1,14·10⁵ Pa."),

        dict(q="Một học sinh cho rằng: “Vì v_rms = √(3RT/M) nên ở 0 K mọi phân tử đứng yên hoàn "
               "toàn, và ta có thể làm lạnh một chất khí tới 0 K.” Nhận xét đúng nhất là",
             o=["Vế đầu là hệ quả đúng của mô hình cổ điển, nhưng vế sau sai: 0 K là giới hạn "
                "lí thuyết không thể đạt tới trong thực tế.",
                "Cả hai vế của lập luận đó đều hoàn toàn chính xác về mặt vật lí.",
                "Vế đầu sai, vì ngay cả ở 0 K thì các phân tử khí vẫn tiếp tục chuyển động nhiệt rất nhanh.",
                "Cả hai vế đều sai, vì công thức tính tốc độ căn quân phương không áp dụng được cho bất kì khí thực nào."],
             a="A",
             e="Trong khuôn khổ mô hình động học phân tử cổ điển của chương trình, công thức "
               "v_rms = √(3RT/M) đúng là cho v_rms = 0 tại T = 0. Nhưng độ không tuyệt đối là "
               "một giới hạn không thể đạt tới: mọi quá trình làm lạnh chỉ tiệm cận nó. "
               "Ngoài ra ở nhiệt độ rất thấp, mọi khí thực đều đã hoá lỏng hoặc hoá rắn từ lâu "
               "nên mô hình khí lí tưởng không còn áp dụng được."),

        dict(q="Trong một thí nghiệm kiểm chứng định luật Boyle, học sinh thu được các cặp số "
               "liệu và tính tích pV cho từng cặp thì thấy pV giảm dần đều theo thời gian đo. "
               "Nguyên nhân hợp lí nhất là",
             o=["khí bị rò rỉ dần ra ngoài trong quá trình đo.",
                "nhiệt độ phòng đã tăng dần trong quá trình đo.",
                "áp kế bị lệch số 0 một lượng cố định về phía dương.",
                "học sinh đọc thể tích luôn lớn hơn giá trị thực một lượng cố định."],
             a="A",
             e="Với lượng khí xác định thì pV = nRT. Nếu pV giảm đều thì hoặc n giảm, hoặc T giảm. "
               "Rò rỉ khí làm n giảm dần, giải thích đúng xu hướng. Nhiệt độ phòng TĂNG sẽ làm pV "
               "tăng chứ không giảm. Còn hai loại sai số cố định (lệch số 0, đọc lệch) tạo ra "
               "sai lệch có hệ thống nhưng không gây xu hướng giảm ĐỀU theo thời gian đo."),

        dict(q="Một bình chứa hỗn hợp hai khí lí tưởng không phản ứng với nhau: n₁ mol khí A và "
               "n₂ mol khí B, ở nhiệt độ T, thể tích V. Áp suất của hỗn hợp là",
             o=["p = (n₁ + n₂)RT/V, bằng tổng áp suất riêng phần của hai khí.",
                "p = √(p₁·p₂), với p₁ và p₂ là áp suất riêng phần.",
                "p = n₁·n₂·RT/V.",
                "p bằng áp suất riêng phần của khí có số mol lớn hơn."],
             a="A",
             e="Vì các phân tử của hai khí không tương tác với nhau (giả thiết khí lí tưởng), "
               "mỗi khí gây áp suất độc lập như thể nó chiếm cả bình một mình. "
               "Tổng số va chạm lên thành bình là tổng của hai phần, nên p = p₁ + p₂ = "
               "n₁RT/V + n₂RT/V = (n₁+n₂)RT/V. Đây là nội dung định luật Dalton về áp suất "
               "riêng phần."),

        dict(q="Một quả bóng bay chứa khí helium được thả lên. Bỏ qua sức căng của vỏ bóng và "
               "coi nhiệt độ khí quyển không đổi theo độ cao. Khi bóng lên cao, thể tích bóng "
               "tăng còn lực đẩy Archimedes tác dụng lên bóng sẽ",
             o=["gần như không đổi, vì thể tích tăng đúng bằng tỉ lệ mà khối lượng riêng của "
                "không khí giảm.",
                "tăng lên đáng kể vì thể tích của quả bóng tăng dần theo độ cao.",
                "giảm đi vì khối lượng riêng của không khí xung quanh giảm dần theo độ cao.",
                "giảm dần về 0 ngay khi quả bóng vượt qua ranh giới của tầng đối lưu."],
             a="A",
             e="Lực đẩy Archimedes F = ρ_kk·g·V. Ở nhiệt độ không đổi, cả khí trong bóng và không "
               "khí bên ngoài đều tuân theo định luật Boyle, nên khi áp suất giảm k lần thì V của "
               "bóng tăng k lần trong khi ρ_kk giảm k lần. Tích ρ_kk·V do đó gần như không đổi, "
               "và F gần như giữ nguyên. Đây là một kết quả đẹp mà học sinh giỏi cần suy luận được."),

        dict(q="Cho đồ thị (p, V) với bốn điểm M(2 L; 3·10⁵ Pa), N(6 L; 1·10⁵ Pa), "
               "P(6 L; 3·10⁵ Pa), Q(2 L; 1·10⁵ Pa) như hình vẽ. Sắp xếp nhiệt độ của bốn trạng "
               "thái theo thứ tự tăng dần là",
             o=["T_Q < T_M = T_N < T_P.", "T_M < T_N < T_P < T_Q.",
                "T_Q < T_N < T_M < T_P.", "T_P < T_M = T_N < T_Q."],
             a="A",
             e="Với cùng lượng khí, T tỉ lệ thuận với tích pV. Tính tích (đơn vị L·10⁵ Pa): "
               "M: 2·3 = 6; N: 6·1 = 6; P: 6·3 = 18; Q: 2·1 = 2. "
               "Vậy T_Q (ứng với 2) nhỏ nhất, T_M = T_N (cùng bằng 6) ở giữa và bằng nhau, "
               "T_P (ứng với 18) lớn nhất.",
             fig="h28_do_thi_pV_doc_hieu"),

        dict(q="Một bình khí nén dung tích 40 L chứa oxygen ở áp suất 150 atm. Người ta dùng khí "
               "này để nạp vào các bình nhỏ 2,0 L ở áp suất 5,0 atm. Coi nhiệt độ không đổi và "
               "bình lớn dùng đến khi áp suất còn 5,0 atm. Số bình nhỏ nạp được là",
             o=["580 bình.", "600 bình.", "1500 bình.", "60 bình."],
             a="A",
             e="Lượng khí sử dụng được, quy về áp suất 5,0 atm: từ p₁V₁ = p·V, phần khí lấy ra "
               "tương ứng thể tích (150 − 5)·40/5,0 = 145·40/5,0 = 1160 L ở 5,0 atm. "
               "Mỗi bình nhỏ chứa 2,0 L ở 5,0 atm nên số bình = 1160/2,0 = 580. "
               "Đáp số 600 là quên trừ đi lượng khí còn lại trong bình lớn — đó chính là bẫy "
               "của bài toán này."),

        dict(q="Xét hai phát biểu: (I) “Ở cùng nhiệt độ và áp suất, hai bình có cùng thể tích "
               "chứa hai khí khác nhau thì có cùng số phân tử.” và (II) “Ở cùng nhiệt độ và áp "
               "suất, hai bình đó có cùng khối lượng khí.” Kết luận đúng là",
             o=["(I) đúng, (II) sai.", "(I) sai, (II) đúng.",
                "cả hai đều đúng.", "cả hai đều sai."],
             a="A",
             e="Từ pV = N·k_B·T, khi p, V, T như nhau thì N như nhau — đó chính là định luật "
               "Avogadro, nên (I) đúng. Nhưng khối lượng m = N·m₀ còn phụ thuộc khối lượng mỗi "
               "phân tử, mà hai khí khác nhau có m₀ khác nhau, nên (II) sai. Ví dụ 1 mol H₂ nặng "
               "2 g còn 1 mol O₂ nặng 32 g dù cùng chiếm 22,4 L ở điều kiện tiêu chuẩn."),

        dict(q="Một pit-tông khối lượng m, tiết diện S đóng kín một cột khí trong xilanh thẳng "
               "đứng, miệng xilanh hướng lên trên. Áp suất khí quyển là p₀. Nếu lật ngược xilanh "
               "cho miệng hướng xuống thì áp suất khí trong xilanh",
             o=["giảm đi một lượng 2mg/S.", "giảm đi một lượng mg/S.",
                "tăng lên một lượng 2mg/S.", "không thay đổi."],
             a="A",
             e="Miệng hướng lên: pit-tông đè lên khí nên p₁ = p₀ + mg/S. "
               "Miệng hướng xuống: pit-tông treo dưới khí, trọng lượng kéo nó xuống nên "
               "p₂ = p₀ − mg/S. Hiệu p₁ − p₂ = 2mg/S, tức áp suất giảm đi 2mg/S. "
               "Việc quên hệ số 2 là lỗi rất phổ biến khi làm dạng bài lật ngược này."),

        dict(q="Trong mô hình động học phân tử, việc thay thế mọi tốc độ phân tử bằng một đại "
               "lượng duy nhất v_rms trong công thức pV = (1/3)Nm·v̄² là hợp lí vì",
             o=["áp suất chỉ phụ thuộc trung bình của bình phương tốc độ, chứ không phụ thuộc "
                "chi tiết cách các tốc độ phân bố.",
                "trên thực tế tất cả các phân tử trong khối khí đều chuyển động với cùng một tốc độ như nhau.",
                "tác dụng của các phân tử chuyển động nhanh và của các phân tử chậm luôn triệt tiêu lẫn nhau.",
                "chỉ những phân tử có tốc độ đúng bằng v_rms mới thực sự va chạm được với thành bình."],
             a="A",
             e="Xung lượng mà mỗi phân tử truyền cho thành bình tỉ lệ với v, còn tần suất va chạm "
               "cũng tỉ lệ với v, nên đóng góp của mỗi phân tử tỉ lệ với v². Khi cộng cho tất cả "
               "các phân tử, chỉ có TỔNG các v² xuất hiện, tức là chỉ cần biết trung bình v̄². "
               "Đồ thị phân bố tốc độ cho thấy các phân tử thực ra có tốc độ rất khác nhau.",
             fig="h23_phan_bo_toc_do"),
    ],
}

DS2 = [
    dict(stem="Một nhóm học sinh làm thí nghiệm khảo sát định luật Boyle với một lượng khí xác "
              "định giữ ở nhiệt độ phòng không đổi. Nhóm thay đổi thể tích khí bằng cách dịch "
              "chuyển chậm pit-tông và đọc áp suất tương ứng trên áp kế, thu được bảng số liệu.",
         tbl=("Bảng số liệu thí nghiệm định luật Boyle",
              ["V (cm³)", "20,0", "25,0", "30,0", "40,0", "50,0"],
              [["p (10⁵ Pa)", "1,50", "1,20", "1,00", "0,75", "0,60"]]),
         items=[
             ("Tích p·V của cả năm lần đo đều bằng 30,0 (đơn vị 10⁵ Pa·cm³).", True,
              "20,0·1,50 = 30,0; 25,0·1,20 = 30,0; 30,0·1,00 = 30,0; 40,0·0,75 = 30,0; "
              "50,0·0,60 = 30,0. Tích không đổi đúng như định luật Boyle dự đoán."),
             ("Nếu vẽ đồ thị p theo 1/V thì các điểm thực nghiệm nằm trên một đường thẳng đi "
              "qua gốc toạ độ.", True,
              "Vì p = 30,0·(1/V), quan hệ giữa p và 1/V là tỉ lệ thuận với hệ số tỉ lệ 30,0, "
              "nên đồ thị là đường thẳng qua gốc toạ độ. Đây chính là kĩ thuật tuyến tính hoá "
              "dùng để kiểm chứng định luật một cách thuyết phục."),
             ("Nếu nhóm nén pit-tông thật nhanh thay vì nén chậm thì tích p·V vẫn giữ nguyên "
              "giá trị 30,0.", False,
              "Nén nhanh là quá trình gần đoạn nhiệt: khí không kịp trao đổi nhiệt với môi "
              "trường, nhiệt độ tăng lên. Khi đó pV = nRT với T tăng nên pV cũng TĂNG chứ không "
              "còn là hằng số. Điều kiện “nhiệt độ không đổi” của định luật Boyle đòi hỏi phải "
              "nén chậm."),
             ("Khi thể tích khí là 60,0 cm³ thì áp suất dự đoán là 0,50·10⁵ Pa.", True,
              "p = 30,0/60,0 = 0,50 (đơn vị 10⁵ Pa). Phép ngoại suy này hợp lệ vì vẫn nằm trong "
              "vùng áp suất thấp, nơi khí gần đúng là khí lí tưởng."),
         ]),

    dict(stem="Một lượng khí lí tưởng thực hiện chu trình khép kín gồm ba giai đoạn như hình vẽ: "
              "(1)→(2) đẳng tích, (2)→(3) đẳng áp, (3)→(1) đẳng nhiệt. "
              "Biết trạng thái (1) có p₁ = 3,0 atm; V₁ = 2,0 L; T₁ = 600 K.",
         fig="h22_chu_trinh_pV",
         items=[
             ("Nhiệt độ ở trạng thái (2) là 200 K.", True,
              "Giai đoạn (1)→(2) là đẳng tích nên p/T = hằng số. "
              "T₂ = T₁·p₂/p₁ = 600·1,0/3,0 = 200 K."),
             ("Nhiệt độ ở trạng thái (3) bằng nhiệt độ ở trạng thái (1).", True,
              "Giai đoạn (2)→(3) là đẳng áp nên T₃ = T₂·V₃/V₂ = 200·6,0/2,0 = 600 K, đúng bằng "
              "T₁. Có thể kiểm tra nhanh bằng tích pV: tại (1) là 3,0·2,0 = 6,0 và tại (3) là "
              "1,0·6,0 = 6,0, hai giá trị bằng nhau nên hai trạng thái cùng nhiệt độ. "
              "Đó chính là điều kiện để đoạn (3)→(1) có thể là đẳng nhiệt."),
             ("Trong giai đoạn (2)→(3), khí bị nén nên nó nhận công từ bên ngoài.", False,
              "Thể tích tăng từ 2,0 L lên 6,0 L, tức khí DÃN NỞ và đẩy pit-tông đi ra, nên khí "
              "SINH công. Theo quy ước dấu, công mà khí nhận được mang giá trị âm."),
             ("Trong giai đoạn (3)→(1), nội năng của khí không thay đổi.", True,
              "Đây là quá trình đẳng nhiệt của khí lí tưởng, mà nội năng khí lí tưởng chỉ phụ "
              "thuộc nhiệt độ, nên ΔU = 0. Suy ra Q = −A: khí bị nén nhận công bao nhiêu thì "
              "toả ra môi trường bấy nhiêu nhiệt lượng."),
         ]),

    dict(stem="Xét một lượng khí lí tưởng gồm N phân tử, mỗi phân tử khối lượng m, chứa trong "
              "bình thể tích V ở nhiệt độ tuyệt đối T.",
         fig="h16_mo_hinh_dong_hoc",
         items=[
             ("Áp suất khí thoả mãn pV = (1/3)N·m·v̄², trong đó v̄² là trung bình bình phương "
              "tốc độ phân tử.", True,
              "Đây là kết quả cơ bản của mô hình động học phân tử, thu được từ việc tính tổng "
              "xung lượng mà các phân tử truyền cho thành bình. Hệ số 1/3 phản ánh tính đẳng "
              "hướng: chuyển động hỗn loạn chia đều cho ba phương."),
             ("Động năng tịnh tiến trung bình của một phân tử phụ thuộc cả vào nhiệt độ lẫn "
              "khối lượng phân tử.", False,
              "So sánh pV = (1/3)Nmv̄² với pV = N·k_B·T cho W̄ = (1/2)mv̄² = (3/2)k_B·T, "
              "biểu thức chỉ chứa T. Động năng trung bình KHÔNG phụ thuộc loại khí. "
              "Chính TỐC ĐỘ mới phụ thuộc khối lượng phân tử, theo v_rms = √(3k_B·T/m)."),
             ("Nếu giữ nguyên nhiệt độ và tăng gấp đôi số phân tử trong bình thì áp suất tăng "
              "gấp đôi.", True,
              "Từ pV = N·k_B·T với V và T không đổi, p tỉ lệ thuận với N. Về mặt vi mô: gấp đôi "
              "số phân tử làm gấp đôi số va chạm lên thành bình mỗi giây, trong khi mỗi va chạm "
              "vẫn truyền xung lượng như cũ."),
             ("Ở cùng nhiệt độ, phân tử hydrogen (M = 2 g/mol) có tốc độ căn quân phương lớn "
              "gấp 4 lần phân tử oxygen (M = 32 g/mol).", True,
              "v_rms tỉ lệ nghịch với √M nên tỉ số bằng √(32/2) = √16 = 4. "
              "Đây là lí do các khí nhẹ như hydrogen và helium dễ dàng thoát khỏi khí quyển "
              "Trái Đất trong thời gian địa chất."),
         ]),

    dict(stem="Một bình kín bằng thép dung tích 10 L chứa khí ở nhiệt độ 27 °C và áp suất "
              "2,0·10⁵ Pa. Cho R = 8,31 J/(mol·K).",
         items=[
             ("Số mol khí trong bình xấp xỉ 0,80 mol.", True,
              "n = pV/(RT) = 2,0·10⁵ · 10·10⁻³/(8,31·300) = 2000/2493 ≈ 0,802 mol."),
             ("Nếu nung bình lên 127 °C thì áp suất khí trong bình trở thành khoảng "
              "2,67·10⁵ Pa.", True,
              "Bình thép nên coi thể tích không đổi, quá trình là đẳng tích: p/T = hằng số. "
              "p₂ = p₁·T₂/T₁ = 2,0·10⁵ · 400/300 ≈ 2,67·10⁵ Pa."),
             ("Nếu nung bình từ 27 °C lên 54 °C thì áp suất khí tăng gấp đôi.", False,
              "Phải dùng nhiệt độ tuyệt đối: 300 K → 327 K, nên p₂/p₁ = 327/300 = 1,09, "
              "áp suất chỉ tăng 9 %. Nhìn thấy 54 = 2·27 rồi kết luận tăng gấp đôi là bẫy "
              "kinh điển của Chương II."),
             ("Nếu mở van cho một nửa số mol khí thoát ra và giữ nhiệt độ 27 °C thì áp suất "
              "trong bình còn 1,0·10⁵ Pa.", True,
              "Với V và T không đổi, từ pV = nRT suy ra p tỉ lệ thuận với n. "
              "Số mol giảm một nửa thì áp suất giảm một nửa, còn 1,0·10⁵ Pa."),
         ]),

    dict(stem="Xét các nhận định về dạng đồ thị của ba đẳng quá trình đối với một lượng khí "
              "lí tưởng xác định.",
         fig="h21_ba_dang_qua_trinh",
         items=[
             ("Trong hệ (p, V), đường đẳng nhiệt là hypebol còn đường đẳng tích là đường thẳng "
              "song song với trục Op.", True,
              "Đẳng nhiệt cho pV = const nên là hypebol. Đẳng tích có V cố định, mà V là trục "
              "hoành, nên tập hợp các điểm cùng hoành độ là đường thẳng đứng, tức song song với "
              "trục Op."),
             ("Trong hệ (p, T), đường đẳng tích là đường thẳng đi qua gốc toạ độ.", True,
              "Từ p = (nR/V)·T với V không đổi, p tỉ lệ thuận với T nên đồ thị là đường thẳng "
              "qua gốc, hệ số góc bằng nR/V."),
             ("Trong hệ (V, T), đường đẳng áp là đường thẳng cắt trục tung tại một điểm khác "
              "gốc toạ độ.", False,
              "Với T tính bằng KELVIN, định luật Charles cho V/T = const nên đường đẳng áp đi "
              "QUA gốc toạ độ. Chỉ khi vẽ theo nhiệt độ Celsius thì đường thẳng mới cắt trục "
              "tung tại V₀ ≠ 0 và cắt trục hoành tại −273,15 °C."),
             ("Trong hệ (p, T), hai đường đẳng tích ứng với hai thể tích khác nhau thì đường "
              "ứng với thể tích nhỏ hơn có độ dốc lớn hơn.", True,
              "Hệ số góc bằng nR/V nên tỉ lệ nghịch với V: thể tích càng nhỏ, đường càng dốc. "
              "Về mặt vật lí, cùng một lượng khí bị nhốt trong bình nhỏ hơn thì áp suất tăng "
              "nhanh hơn khi nung nóng."),
         ]),

    dict(stem="Một bóng thám không có vỏ mềm, khi ở mặt đất chứa 5,0 m³ khí helium ở áp suất "
              "1,0·10⁵ Pa và nhiệt độ 27 °C. Bóng bay lên độ cao nơi áp suất khí quyển là "
              "0,40·10⁵ Pa và nhiệt độ là −13 °C. Bỏ qua sức căng của vỏ bóng.",
         items=[
             ("Áp suất khí bên trong bóng ở độ cao đó xấp xỉ bằng 0,40·10⁵ Pa.", True,
              "Vỏ bóng mềm và bỏ qua sức căng nên khí bên trong luôn có áp suất cân bằng với "
              "áp suất khí quyển bên ngoài."),
             ("Thể tích của bóng ở độ cao đó là khoảng 10,8 m³.", True,
              "Dùng p₁V₁/T₁ = p₂V₂/T₂ với T₁ = 300 K, T₂ = 260 K: "
              "V₂ = p₁V₁T₂/(p₂T₁) = 1,0·5,0·260/(0,40·300) = 1300/120 ≈ 10,8 m³."),
             ("Vì nhiệt độ trên cao thấp hơn nên thể tích bóng phải nhỏ hơn lúc ở mặt đất.",
              False,
              "Hai yếu tố tác động ngược chiều: áp suất giảm 2,5 lần làm bóng nở ra, còn nhiệt độ "
              "giảm từ 300 K xuống 260 K làm bóng co lại chỉ 13 %. Tác dụng của áp suất trội hơn "
              "hẳn nên thể tích cuối cùng TĂNG, từ 5,0 m³ lên khoảng 10,8 m³."),
             ("Số phân tử khí trong bóng không thay đổi trong suốt quá trình bay lên.", True,
              "Bóng kín, không có khí thoát ra hay lọt vào, nên số phân tử được bảo toàn. "
              "Chính vì vậy mới dùng được phương trình trạng thái dạng p₁V₁/T₁ = p₂V₂/T₂."),
         ]),

    dict(stem="Xét các nhận định về điều kiện áp dụng của các định luật chất khí.",
         items=[
             ("Định luật Boyle chỉ áp dụng được khi nhiệt độ và lượng khí đều không đổi.", True,
              "Cả hai điều kiện đều cần thiết. Nếu nhiệt độ đổi thì pV = nRT thay đổi theo T; "
              "nếu lượng khí đổi thì n thay đổi. Trong cả hai trường hợp, tích pV không còn là "
              "hằng số."),
             ("Phương trình pV/T = hằng số áp dụng được cho bài toán bơm thêm khí vào một bình "
              "kín.", False,
              "Phương trình này chỉ đúng cho một LƯỢNG KHÍ XÁC ĐỊNH. Khi bơm thêm khí thì số mol "
              "thay đổi và phải dùng pV = nRT với n xuất hiện tường minh, hoặc coi toàn bộ lượng "
              "khí trước khi bơm (kể cả phần trong bơm) là một khối khí ban đầu."),
             ("Ở áp suất rất cao, khí thực không còn tuân theo phương trình khí lí tưởng vì "
              "không thể bỏ qua thể tích riêng của phân tử và lực hút giữa chúng.", True,
              "Áp suất cao làm khoảng cách giữa các phân tử giảm mạnh, khiến hai giả thiết nền "
              "tảng của mô hình khí lí tưởng (coi phân tử là chất điểm và bỏ qua tương tác) "
              "không còn hợp lệ."),
             ("Định luật Charles có thể viết là V₁/t₁ = V₂/t₂ với t tính bằng độ Celsius.", False,
              "Quan hệ tỉ lệ thuận chỉ đúng với nhiệt độ TUYỆT ĐỐI. Có thể kiểm tra ngay bằng "
              "phản ví dụ: với t₁ = 0 °C, vế trái sẽ là phép chia cho 0 — vô nghĩa. "
              "Bắt buộc phải dùng Kelvin."),
         ]),

    dict(stem="Một xilanh nằm ngang được chia thành hai ngăn A và B bởi một pit-tông mỏng, nhẹ, "
              "không ma sát và không dẫn nhiệt. Ban đầu hai ngăn có cùng thể tích V₀, cùng chứa "
              "n mol khí lí tưởng ở cùng nhiệt độ T₀.",
         fig="h27_pit_tong_hai_ngan",
         items=[
             ("Ban đầu áp suất trong hai ngăn bằng nhau.", True,
              "Pit-tông nhẹ, không ma sát và đang cân bằng nên hai lực áp lực từ hai phía phải "
              "cân bằng: p_A·S = p_B·S. Ngoài ra hai ngăn cùng n, cùng V₀, cùng T₀ nên áp suất "
              "bằng nhau cũng suy ra được từ pV = nRT."),
             ("Nếu nung nóng ngăn A lên nhiệt độ 2T₀ và giữ ngăn B ở T₀ thì pit-tông đứng yên "
              "vì tổng thể tích không đổi.", False,
              "Tổng thể tích không đổi là ràng buộc hình học, không phải lí do để pit-tông đứng "
              "yên. Khí ngăn A nóng lên có xu hướng dãn nở nên đẩy pit-tông dịch sang phía ngăn B "
              "cho tới khi áp suất hai bên lại cân bằng."),
             ("Ở trạng thái cân bằng mới (ngăn A ở 2T₀, ngăn B ở T₀), thể tích ngăn A gấp đôi "
              "thể tích ngăn B.", True,
              "Ở cân bằng, p_A = p_B = p'. Áp dụng pV = nRT cho từng ngăn với cùng n: "
              "p'V_A = nR·2T₀ và p'V_B = nR·T₀. Chia hai vế được V_A/V_B = 2."),
             ("Ở trạng thái cân bằng mới đó, thể tích ngăn A bằng 4V₀/3.", True,
              "Từ V_A/V_B = 2 và V_A + V_B = 2V₀, ta có 2V_B + V_B = 2V₀ nên V_B = 2V₀/3 và "
              "V_A = 4V₀/3."),
         ]),
]
