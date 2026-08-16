# -*- coding: utf-8 -*-
"""BÀI TẬP LÍ THUYẾT – CHƯƠNG IV: VẬT LÍ HẠT NHÂN."""

MC4 = {

"Mức 1 – NHẬN BIẾT": [
dict(q="Hạt nhân nguyên tử được cấu tạo từ",
 o=["proton và electron.", "proton và neutron.", "neutron và electron.", "chỉ các proton."],
 a="B",
 sol="Hạt nhân gồm các nucleon là proton (mang điện +e) và neutron (không mang điện). "
     "Electron chuyển động ở lớp vỏ nguyên tử, không nằm trong hạt nhân."),

dict(q="Trong kí hiệu hạt nhân, số khối A cho biết",
 o=["số proton của hạt nhân.", "số neutron của hạt nhân.",
    "tổng số nucleon của hạt nhân.", "số electron của nguyên tử trung hoà."],
 a="C",
 sol="A là số khối, bằng tổng số nucleon (proton và neutron). Số proton là Z, số neutron là N = A − Z."),

dict(q="Hạt nhân có số khối A và số proton Z thì số neutron của nó là",
 o=["A + Z.", "A − Z.", "Z − A.", "A·Z."],
 a="B",
 sol="Vì A là tổng số nucleon và Z là số proton nên số neutron N = A − Z."),

dict(q="Các hạt nhân đồng vị là những hạt nhân có",
 o=["cùng số neutron nhưng khác số proton.",
    "cùng số proton nhưng khác số neutron.",
    "cùng số khối nhưng khác số proton.",
    "cùng số proton và cùng số neutron."],
 a="B",
 sol="Đồng vị có cùng số proton Z (nên cùng vị trí trong bảng tuần hoàn, cùng tính chất hoá học) "
     "nhưng khác số neutron, do đó khác số khối A."),

dict(q="Đơn vị khối lượng nguyên tử u được định nghĩa bằng",
 o=["khối lượng của một proton.",
    "khối lượng của một nguyên tử hydrogen.",
    "1/12 khối lượng của một nguyên tử đồng vị carbon-12.",
    "1/16 khối lượng của một nguyên tử oxygen-16."],
 a="C",
 sol="Theo định nghĩa, 1 u bằng 1/12 khối lượng của một nguyên tử đồng vị ¹²C, xấp xỉ 1,66055·10⁻²⁷ kg."),

dict(q="Hệ thức liên hệ giữa đơn vị khối lượng nguyên tử và đơn vị năng lượng là",
 o=["1 u·c² ≈ 931,5 MeV.", "1 u·c² ≈ 9,315 MeV.",
    "1 u·c² ≈ 1,6·10⁻¹⁹ MeV.", "1 u·c² ≈ 6,02·10²³ MeV."],
 a="A",
 sol="Áp dụng E = mc² với m = 1 u = 1,66055·10⁻²⁷ kg ta được E ≈ 1,49·10⁻¹⁰ J ≈ 931,5 MeV. "
     "Vì vậy thường viết 1 u ≈ 931,5 MeV/c²."),

dict(q="Đặc điểm nào sau đây KHÔNG phải của lực hạt nhân?",
 o=["Là lực hút rất mạnh giữa các nucleon.",
    "Chỉ có tác dụng trong phạm vi cỡ kích thước hạt nhân.",
    "Không phụ thuộc vào điện tích của các nucleon.",
    "Có bản chất là lực tĩnh điện giữa các hạt mang điện."],
 a="D",
 sol="Lực hạt nhân là một loại lực riêng (biểu hiện của tương tác mạnh), không cùng bản chất với lực tĩnh điện "
     "hay lực hấp dẫn. Nếu là lực tĩnh điện thì các proton đã đẩy nhau và hạt nhân không thể tồn tại."),

dict(q="Độ hụt khối của một hạt nhân được tính bằng công thức",
 o=["Δm = m_hn − [Z·m_p + (A − Z)·m_n].",
    "Δm = Z·m_p + (A − Z)·m_n − m_hn.",
    "Δm = Z·m_p − (A − Z)·m_n.",
    "Δm = A·m_p − Z·m_n."],
 a="B",
 sol="Độ hụt khối là hiệu giữa tổng khối lượng các nucleon riêng rẽ và khối lượng của hạt nhân: "
     "Δm = Z·m_p + (A − Z)·m_n − m_hn, luôn dương đối với hạt nhân bền."),

dict(q="Năng lượng liên kết của một hạt nhân là",
 o=["năng lượng toả ra khi hạt nhân đó phân rã.",
    "năng lượng tối thiểu cần cung cấp để phá vỡ hạt nhân thành các nucleon riêng rẽ.",
    "năng lượng của các electron chuyển động quanh hạt nhân.",
    "động năng của các nucleon trong hạt nhân."],
 a="B",
 sol="Năng lượng liên kết E_lk = Δm·c² vừa là năng lượng toả ra khi các nucleon riêng rẽ kết hợp thành hạt nhân, "
     "vừa là năng lượng tối thiểu cần cung cấp để tách hạt nhân thành các nucleon riêng rẽ."),

dict(q="Năng lượng liên kết riêng của một hạt nhân là",
 o=["tích của năng lượng liên kết với số khối.",
    "thương của năng lượng liên kết chia cho số khối.",
    "thương của năng lượng liên kết chia cho số proton.",
    "hiệu giữa năng lượng liên kết và số khối."],
 a="B",
 sol="Năng lượng liên kết riêng ε = E_lk/A là năng lượng liên kết tính trung bình cho một nucleon; "
     "đại lượng này dùng để so sánh độ bền vững giữa các hạt nhân."),

dict(q="Hiện tượng phóng xạ là quá trình",
 o=["hạt nhân hấp thụ neutron rồi vỡ ra.",
    "hạt nhân không bền vững tự phát phân rã, phát ra tia phóng xạ và biến đổi thành hạt nhân khác.",
    "các electron ở lớp vỏ nguyên tử bị bứt ra.",
    "hai hạt nhân nhẹ kết hợp thành một hạt nhân nặng hơn."],
 a="B",
 sol="Phóng xạ là quá trình phân rã TỰ PHÁT của hạt nhân không bền vững. Việc hấp thụ neutron rồi vỡ ra là "
     "phân hạch, còn kết hợp hai hạt nhân nhẹ là nhiệt hạch — cả hai đều không phải phóng xạ."),

dict(q="Tia α thực chất là dòng các",
 o=["hạt nhân helium-4.", "electron.", "positron.", "photon năng lượng cao."],
 a="A",
 sol="Tia α là dòng hạt nhân ⁴₂He, mang điện tích +2e. Electron là tia β⁻, positron là tia β⁺, "
     "photon năng lượng cao là tia γ."),

dict(q="Tia β⁻ là dòng các",
 o=["proton.", "neutron.", "electron.", "hạt nhân hydrogen."],
 a="C",
 sol="Tia β⁻ là dòng electron mang điện tích −e, được sinh ra ngay trong hạt nhân từ quá trình một neutron "
     "biến đổi thành một proton."),

dict(q="Tia γ có bản chất là",
 o=["dòng hạt mang điện dương.", "dòng hạt mang điện âm.",
    "sóng điện từ có bước sóng rất ngắn.", "dòng neutron chuyển động nhanh."],
 a="C",
 sol="Tia γ là sóng điện từ (dòng photon) có bước sóng rất ngắn, không mang điện tích nên không bị lệch trong "
     "điện trường và từ trường."),

dict(q="Định luật phóng xạ được biểu diễn bởi công thức nào sau đây (T là chu kì bán rã)?",
 o=["N = N₀·2^(t/T).", "N = N₀·2^(−t/T).", "N = N₀·(1 − 2^(−t/T)).", "N = N₀·t/T."],
 a="B",
 sol="Số hạt nhân còn lại giảm theo hàm mũ: N = N₀·2^(−t/T) = N₀·e^(−λt). "
     "Công thức N₀(1 − 2^(−t/T)) là số hạt nhân ĐÃ phân rã, không phải số hạt còn lại."),

dict(q="Chu kì bán rã của một chất phóng xạ là khoảng thời gian để",
 o=["toàn bộ số hạt nhân của mẫu chất bị phân rã.",
    "một nửa số hạt nhân của mẫu chất bị phân rã.",
    "độ phóng xạ của mẫu chất tăng gấp đôi.",
    "khối lượng mẫu chất tăng gấp đôi."],
 a="B",
 sol="Theo định nghĩa, sau mỗi chu kì bán rã T thì một nửa số hạt nhân ban đầu đã phân rã, "
     "tức số hạt nhân còn lại chỉ bằng một nửa."),

dict(q="Đơn vị của độ phóng xạ trong hệ SI là",
 o=["becơren (Bq).", "curie (Ci).", "gray (Gy).", "tesla (T)."],
 a="A",
 sol="Đơn vị SI của độ phóng xạ là becơren: 1 Bq = 1 phân rã trong một giây. Curie là đơn vị thực dụng "
     "với 1 Ci = 3,7·10¹⁰ Bq."),

dict(q="Phản ứng phân hạch là phản ứng trong đó",
 o=["hai hạt nhân nhẹ kết hợp thành một hạt nhân nặng hơn.",
    "một hạt nhân rất nặng vỡ thành hai hạt nhân có số khối trung bình.",
    "một hạt nhân tự phát phóng ra hạt α.",
    "một hạt nhân hấp thụ photon rồi phát ra electron."],
 a="B",
 sol="Phân hạch là quá trình một hạt nhân rất nặng (như ²³⁵U) hấp thụ neutron rồi vỡ thành hai hạt nhân trung "
     "bình, kèm theo 2 – 3 neutron và năng lượng lớn. Kết hợp hai hạt nhân nhẹ là phản ứng nhiệt hạch."),
],

"Mức 2 – THÔNG HIỂU": [
dict(q="Trong một phản ứng hạt nhân, các đại lượng nào sau đây được bảo toàn?",
 o=["Số nucleon và điện tích.", "Khối lượng nghỉ và số proton.",
    "Số neutron và động năng.", "Khối lượng nghỉ và số nucleon."],
 a="A",
 sol="Bốn đại lượng bảo toàn là số nucleon (số khối), điện tích, năng lượng toàn phần và động lượng. "
     "Khối lượng nghỉ, số proton riêng rẽ, số neutron riêng rẽ và động năng đều KHÔNG được bảo toàn."),

dict(q="Phát biểu nào sau đây về phản ứng hạt nhân là SAI?",
 o=["Tổng số nucleon trước và sau phản ứng bằng nhau.",
    "Tổng điện tích trước và sau phản ứng bằng nhau.",
    "Tổng khối lượng nghỉ trước và sau phản ứng bằng nhau.",
    "Năng lượng toàn phần trước và sau phản ứng bằng nhau."],
 a="C",
 sol="Tổng khối lượng nghỉ nói chung THAY ĐỔI trong phản ứng hạt nhân; chính độ chênh lệch đó nhân với c² "
     "cho ra năng lượng toả ra hoặc thu vào của phản ứng. Nếu khối lượng được bảo toàn thì phản ứng hạt nhân "
     "sẽ không thể là nguồn năng lượng."),

dict(q="Trong các hạt nhân sau, hạt nhân nào bền vững nhất, biết năng lượng liên kết riêng của chúng lần lượt là "
       "⁴He: 7,07 MeV/nucleon; ⁵⁶Fe: 8,79 MeV/nucleon; ²³⁵U: 7,59 MeV/nucleon; ⁷Li: 5,61 MeV/nucleon?",
 o=["⁴He.", "⁵⁶Fe.", "²³⁵U.", "⁷Li."],
 a="B",
 sol="Hạt nhân có năng lượng liên kết RIÊNG lớn nhất là bền vững nhất. Ở đây ⁵⁶Fe có ε = 8,79 MeV/nucleon "
     "lớn nhất, đúng như vị trí đỉnh của đường cong năng lượng liên kết riêng."),

dict(q="Hạt nhân ²³⁵U có năng lượng liên kết khoảng 1784 MeV, còn hạt nhân ⁴He có năng lượng liên kết khoảng "
       "28,3 MeV. Kết luận nào sau đây đúng?",
 o=["²³⁵U bền vững hơn ⁴He vì có năng lượng liên kết lớn hơn.",
    "⁴He bền vững hơn ²³⁵U vì có số nucleon ít hơn.",
    "Phải so sánh năng lượng liên kết riêng; kết quả là ²³⁵U bền hơn ⁴He một chút.",
    "Không thể so sánh được độ bền vững của hai hạt nhân này."],
 a="C",
 sol="Năng lượng liên kết toàn phần lớn chỉ vì hạt nhân có nhiều nucleon. Phải dùng ε = E_lk/A: "
     "ε(²³⁵U) = 1784/235 ≈ 7,59 MeV/nucleon, còn ε(⁴He) = 28,3/4 ≈ 7,07 MeV/nucleon. "
     "Vậy ²³⁵U bền hơn ⁴He một chút, nhưng cả hai đều kém bền hơn ⁵⁶Fe."),

dict(q="Tốc độ phân rã của một chất phóng xạ KHÔNG phụ thuộc vào yếu tố nào sau đây?",
 o=["Bản chất của hạt nhân phóng xạ.",
    "Số hạt nhân phóng xạ hiện có trong mẫu.",
    "Nhiệt độ, áp suất và trạng thái hoá học của mẫu chất.",
    "Hằng số phóng xạ của chất đó."],
 a="C",
 sol="Phóng xạ là quá trình tự phát, do cấu trúc bên trong hạt nhân quyết định, hoàn toàn không phụ thuộc các "
     "điều kiện bên ngoài như nhiệt độ, áp suất hay việc hạt nhân đó nằm trong hợp chất hoá học nào. "
     "Độ phóng xạ H = λN thì phụ thuộc λ (bản chất) và N (số hạt hiện có)."),

dict(q="Sắp xếp các tia phóng xạ theo thứ tự khả năng ĐÂM XUYÊN tăng dần, ta được",
 o=["α, β, γ.", "γ, β, α.", "β, α, γ.", "α, γ, β."],
 a="A",
 sol="Tia α bị chặn bởi một tờ giấy, tia β bị chặn bởi vài milimét nhôm, tia γ phải cần vài centimét chì mới "
     "giảm đáng kể. Vậy khả năng đâm xuyên tăng dần là α < β < γ."),

dict(q="Sắp xếp các tia phóng xạ theo thứ tự khả năng ION HOÁ môi trường giảm dần, ta được",
 o=["γ, β, α.", "α, β, γ.", "β, γ, α.", "γ, α, β."],
 a="B",
 sol="Khả năng ion hoá biến thiên NGƯỢC chiều với khả năng đâm xuyên: tia α ion hoá mạnh nhất nên mất năng lượng "
     "rất nhanh và đi được quãng đường ngắn; tia γ ion hoá yếu nhất nên xuyên sâu."),

dict(q="Cho ba loại tia phóng xạ đi vào một từ trường đều theo phương vuông góc với đường sức. Tia không bị lệch "
       "khỏi phương ban đầu là",
 o=["tia α.", "tia β⁻.", "tia β⁺.", "tia γ."],
 a="D",
 sol="Tia γ là sóng điện từ, không mang điện tích nên không chịu lực từ và đi thẳng. Tia α (điện tích +2e) và "
     "tia β (điện tích ±e) đều bị lệch; tia β lệch nhiều hơn vì khối lượng nhỏ hơn rất nhiều."),

dict(q="Sau một phân rã α, so với hạt nhân mẹ thì hạt nhân con có",
 o=["số khối giảm 4 và số proton giảm 2.",
    "số khối giảm 4 và số proton giảm 4.",
    "số khối không đổi và số proton giảm 2.",
    "số khối giảm 2 và số proton giảm 4."],
 a="A",
 sol="Hạt α chính là hạt nhân ⁴₂He, mang đi 4 nucleon và 2 đơn vị điện tích dương. Do đó A giảm 4 và Z giảm 2."),

dict(q="Sau một phân rã β⁻, so với hạt nhân mẹ thì hạt nhân con có",
 o=["số khối không đổi, số proton tăng 1.",
    "số khối không đổi, số proton giảm 1.",
    "số khối giảm 1, số proton không đổi.",
    "số khối tăng 1, số proton tăng 1."],
 a="A",
 sol="Trong phân rã β⁻, một neutron biến thành một proton kèm phát ra electron: n → p + e⁻ + phản neutrino. "
     "Tổng số nucleon không đổi nên A giữ nguyên, còn số proton tăng thêm 1."),

dict(q="Sau khoảng thời gian bằng hai chu kì bán rã, số hạt nhân còn lại của một mẫu chất phóng xạ bằng",
 o=["một nửa số hạt nhân ban đầu.", "một phần tư số hạt nhân ban đầu.",
    "một phần tám số hạt nhân ban đầu.", "không, mẫu chất đã phân rã hết."],
 a="B",
 sol="Sau mỗi chu kì bán rã số hạt nhân giảm một nửa, nên sau 2T còn lại (1/2)² = 1/4 số hạt nhân ban đầu. "
     "Về lí thuyết, mẫu chất không bao giờ phân rã hết hoàn toàn."),

dict(q="Hằng số phóng xạ λ và chu kì bán rã T liên hệ với nhau bởi hệ thức",
 o=["λ = T/ln2.", "λ = ln2/T.", "λ = T·ln2.", "λ = 2/T."],
 a="B",
 sol="Từ N = N₀e^(−λt) và điều kiện N = N₀/2 khi t = T, ta được e^(−λT) = 1/2, suy ra λT = ln2, "
     "tức λ = ln2/T ≈ 0,693/T."),

dict(q="Độ phóng xạ H của một mẫu chất phóng xạ liên hệ với số hạt nhân N còn lại trong mẫu bởi hệ thức",
 o=["H = N/λ.", "H = λ/N.", "H = λ·N.", "H = λ·N²."],
 a="C",
 sol="Độ phóng xạ là số phân rã trong một giây và tỉ lệ thuận với số hạt nhân hiện có: H = λN. "
     "Vì N giảm theo hàm mũ nên H cũng giảm theo cùng quy luật với cùng chu kì bán rã."),

dict(q="Bán kính hạt nhân được tính gần đúng theo công thức R ≈ 1,2·10⁻¹⁵·A^(1/3) (m). Từ đó suy ra khối lượng "
       "riêng của các hạt nhân khác nhau thì",
 o=["tỉ lệ thuận với số khối A.", "tỉ lệ nghịch với số khối A.",
    "xấp xỉ như nhau đối với mọi hạt nhân.", "tỉ lệ với A²."],
 a="C",
 sol="Thể tích hạt nhân V ~ R³ ~ A, trong khi khối lượng cũng xấp xỉ tỉ lệ với A. Vì vậy tỉ số khối lượng trên "
     "thể tích gần như không phụ thuộc A: mọi hạt nhân đều có khối lượng riêng cỡ 2·10¹⁷ kg/m³."),

dict(q="Hai đồng vị của cùng một nguyên tố thì",
 o=["có tính chất hoá học giống nhau nhưng tính chất phóng xạ có thể rất khác nhau.",
    "có tính chất hoá học khác nhau nhưng tính chất phóng xạ giống nhau.",
    "hoàn toàn giống nhau về mọi tính chất.",
    "có cùng số khối nhưng khác số proton."],
 a="A",
 sol="Tính chất hoá học do số electron (bằng Z) quyết định nên các đồng vị giống nhau về hoá học. "
     "Nhưng độ bền của hạt nhân phụ thuộc cả số neutron, nên có đồng vị bền và có đồng vị phóng xạ "
     "(ví dụ ¹²C bền còn ¹⁴C phóng xạ)."),

dict(q="Trong lò phản ứng hạt nhân, người ta dùng chất làm chậm (nước thường, nước nặng, than chì) nhằm mục đích",
 o=["hấp thụ bớt neutron để dập tắt phản ứng.",
    "làm giảm tốc độ của các neutron, tăng khả năng chúng bị hạt nhân uranium hấp thụ.",
    "làm nguội lò phản ứng.",
    "ngăn không cho tia γ thoát ra ngoài."],
 a="B",
 sol="Neutron sinh ra từ phân hạch có tốc độ rất lớn, khó bị ²³⁵U hấp thụ. Chất làm chậm giảm tốc chúng thành "
     "neutron chậm (neutron nhiệt), làm tăng mạnh xác suất gây phân hạch tiếp theo. "
     "Việc hấp thụ bớt neutron là nhiệm vụ của thanh điều khiển."),

dict(q="Hệ số nhân neutron k của một lò phản ứng hạt nhân được duy trì ở giá trị nào để lò hoạt động ổn định?",
 o=["k < 1.", "k = 1.", "k > 1.", "k = 0."],
 a="B",
 sol="k = 1 nghĩa là trung bình mỗi phân hạch gây ra đúng một phân hạch tiếp theo, phản ứng dây chuyền tự duy trì "
     "ở mức ổn định. k < 1 làm phản ứng tắt dần, còn k > 1 làm năng lượng tăng vọt không kiểm soát."),

dict(q="Phản ứng nhiệt hạch chỉ xảy ra ở nhiệt độ rất cao vì",
 o=["cần nhiệt độ cao để các hạt nhân bị phá vỡ.",
    "cần động năng rất lớn để các hạt nhân thắng được lực đẩy Coulomb và tiến lại đủ gần nhau.",
    "ở nhiệt độ thấp lực hạt nhân không tồn tại.",
    "cần nhiệt độ cao để tạo ra neutron chậm."],
 a="B",
 sol="Hai hạt nhân đều mang điện dương nên đẩy nhau rất mạnh khi lại gần. Chỉ khi có động năng cực lớn "
     "(ứng với nhiệt độ hàng trăm triệu độ) chúng mới tiến vào khoảng cách cỡ 10⁻¹⁵ m để lực hạt nhân phát huy "
     "tác dụng và kết hợp lại."),

dict(q="Ba nguyên tắc cơ bản để bảo đảm an toàn khi làm việc với nguồn phóng xạ là",
 o=["giảm thời gian tiếp xúc, tăng khoảng cách, dùng vật liệu che chắn.",
    "tăng thời gian tiếp xúc, giảm khoảng cách, không cần che chắn.",
    "hạ nhiệt độ nguồn, tăng áp suất, dùng che chắn.",
    "chỉ cần đeo khẩu trang và găng tay."],
 a="A",
 sol="Ba nguyên tắc là THỜI GIAN – KHOẢNG CÁCH – CHE CHẮN. Việc hạ nhiệt độ hay tăng áp suất hoàn toàn không "
     "ảnh hưởng đến quá trình phóng xạ."),

dict(q="Electron phát ra trong phân rã β⁻ có nguồn gốc từ đâu?",
 o=["Từ lớp vỏ electron của nguyên tử bị bứt ra.",
    "Từ sự biến đổi của một neutron trong hạt nhân thành một proton.",
    "Từ môi trường xung quanh bị ion hoá.",
    "Từ sự vỡ đôi của một proton trong hạt nhân."],
 a="B",
 sol="Electron của tia β⁻ được sinh ra ngay trong hạt nhân theo quá trình n → p + e⁻ + phản neutrino, "
     "chứ không phải electron ở lớp vỏ nguyên tử. Đây là điểm phân biệt bản chất rất hay được hỏi."),

dict(q="Phóng xạ γ",
 o=["làm số khối giảm 4 và số proton giảm 2.",
    "làm số proton tăng thêm 1.",
    "không làm thay đổi số khối và số proton của hạt nhân.",
    "biến hạt nhân thành một nguyên tố hoàn toàn khác."],
 a="C",
 sol="Tia γ là photon nên không mang theo nucleon hay điện tích: A và Z đều không đổi. "
     "Phóng xạ γ chỉ là sự chuyển hạt nhân con từ trạng thái kích thích về trạng thái cơ bản, "
     "luôn đi kèm phân rã α hoặc β chứ không xảy ra độc lập."),

dict(q="Trên đường cong biểu diễn năng lượng liên kết riêng theo số khối, các hạt nhân bền vững nhất nằm ở vùng",
 o=["số khối rất nhỏ (A < 10).", "số khối trung bình (A ≈ 50 ÷ 95).",
    "số khối rất lớn (A > 230).", "số khối bằng 0."],
 a="B",
 sol="Đường cong đạt cực đại ở vùng A ≈ 50 ÷ 95, với đỉnh ở ⁵⁶Fe (ε ≈ 8,79 MeV/nucleon). "
     "Chính vì thế các hạt nhân rất nhẹ có xu hướng tổng hợp lại và các hạt nhân rất nặng có xu hướng phân hạch, "
     "cả hai đều tiến về phía vùng bền vững này."),
],

"Mức 3 – VẬN DỤNG": [
dict(q="Hạt nhân ²¹⁰₈₄Po phóng xạ α. Hạt nhân con tạo thành là",
 o=["²⁰⁶₈₂Pb.", "²⁰⁶₈₄Po.", "²¹⁰₈₂Pb.", "²⁰⁸₈₂Pb."],
 a="A",
 sol="Áp dụng bảo toàn số khối và điện tích: A = 210 − 4 = 206; Z = 84 − 2 = 82. "
     "Nguyên tố có Z = 82 là chì (Pb), vậy hạt nhân con là ²⁰⁶₈₂Pb."),

dict(q="Hạt nhân ²³⁸₉₂U phân rã thành ²⁰⁶₈₂Pb sau một chuỗi các phân rã α và β⁻. Số phân rã α và số phân rã β⁻ "
       "trong chuỗi đó lần lượt là",
 o=["8 và 6.", "6 và 8.", "8 và 10.", "10 và 6."],
 a="A",
 sol="Chỉ phân rã α làm thay đổi số khối: ΔA = 238 − 206 = 32, mà mỗi phân rã α giảm 4 nên có 32/4 = 8 phân rã α. "
     "Tám phân rã α làm Z giảm 16, tức từ 92 xuống 76; nhưng Z cuối là 82 nên phải có thêm 82 − 76 = 6 phân rã β⁻ "
     "(mỗi phân rã β⁻ làm Z tăng 1)."),

dict(q="Sau thời gian bằng 3 chu kì bán rã, phần trăm số hạt nhân của một mẫu chất phóng xạ ĐÃ bị phân rã là",
 o=["12,5%.", "25%.", "75%.", "87,5%."],
 a="D",
 sol="Số hạt còn lại chiếm (1/2)³ = 1/8 = 12,5%. Do đó số hạt đã phân rã chiếm 100% − 12,5% = 87,5%. "
     "Bẫy ở đây là chọn 12,5% — đó là phần CÒN LẠI chứ không phải phần đã phân rã."),

dict(q="Sau thời gian bằng 2 chu kì bán rã, tỉ số giữa số hạt nhân đã phân rã và số hạt nhân còn lại của một mẫu "
       "chất phóng xạ bằng",
 o=["1/3.", "3.", "1/4.", "4."],
 a="B",
 sol="Sau 2T, số hạt còn lại là N₀/4, số hạt đã phân rã là N₀ − N₀/4 = 3N₀/4. "
     "Tỉ số cần tìm bằng (3N₀/4)/(N₀/4) = 3."),

dict(q="Để xác định chu kì bán rã của một mẫu chất phóng xạ, người ta đo độ phóng xạ H tại nhiều thời điểm t "
       "rồi vẽ đồ thị lnH theo t. Đồ thị thu được là một đường thẳng có hệ số góc a. Chu kì bán rã được tính bằng",
 o=["T = a/ln2.", "T = −ln2/a.", "T = ln2·a.", "T = −a·ln2."],
 a="B",
 sol="Từ H = H₀e^(−λt) suy ra lnH = lnH₀ − λt, nên hệ số góc a = −λ, tức λ = −a (a mang giá trị âm). "
     "Do đó T = ln2/λ = −ln2/a."),

dict(q="Một phản ứng hạt nhân có tổng khối lượng nghỉ của các hạt trước phản ứng lớn hơn tổng khối lượng nghỉ "
       "của các hạt sau phản ứng. Kết luận nào sau đây đúng?",
 o=["Phản ứng thu năng lượng.",
    "Phản ứng toả năng lượng, các hạt sinh ra bền vững hơn.",
    "Phản ứng không trao đổi năng lượng.",
    "Phản ứng vi phạm định luật bảo toàn năng lượng."],
 a="B",
 sol="Năng lượng toả ra W = (m_trước − m_sau)c² > 0, nên phản ứng toả năng lượng. Phần khối lượng nghỉ bị hụt "
     "đi đã chuyển thành động năng và bức xạ. Tổng năng lượng liên kết sau lớn hơn trước, nghĩa là các hạt sinh ra "
     "bền vững hơn. Năng lượng TOÀN PHẦN vẫn được bảo toàn."),

dict(q="Năng lượng toả ra khi phân hạch một hạt nhân ²³⁵U là khoảng 200 MeV, còn khi tổng hợp một cặp hạt nhân "
       "deuterium – tritium là khoảng 17,6 MeV. So sánh nào sau đây là ĐÚNG?",
 o=["Xét trên mỗi phản ứng, phân hạch toả năng lượng lớn hơn; xét trên mỗi nucleon, nhiệt hạch toả năng lượng lớn hơn.",
    "Nhiệt hạch toả năng lượng lớn hơn phân hạch trên cả hai phương diện.",
    "Phân hạch toả năng lượng lớn hơn nhiệt hạch trên cả hai phương diện.",
    "Hai loại phản ứng toả năng lượng như nhau trên mỗi nucleon."],
 a="A",
 sol="Trên mỗi phản ứng: 200 MeV > 17,6 MeV, phân hạch thắng. Trên mỗi nucleon: phân hạch cho 200/236 ≈ 0,85 "
     "MeV/nucleon, còn nhiệt hạch cho 17,6/5 ≈ 3,5 MeV/nucleon, tức nhiệt hạch lớn hơn khoảng 4 lần. "
     "Đây là lí do nhiệt hạch được coi là nguồn năng lượng tương lai."),

dict(q="Một mẫu gỗ cổ có độ phóng xạ do ¹⁴C bằng 1/4 độ phóng xạ của một mẫu gỗ tươi cùng loại và cùng khối lượng. "
       "Biết chu kì bán rã của ¹⁴C là 5730 năm. Tuổi của mẫu gỗ cổ xấp xỉ",
 o=["2865 năm.", "5730 năm.", "11460 năm.", "22920 năm."],
 a="C",
 sol="Độ phóng xạ giảm còn 1/4 = (1/2)² ứng với thời gian bằng 2 chu kì bán rã: t = 2·5730 = 11460 năm. "
     "Cơ sở của phương pháp: khi cây còn sống, tỉ lệ ¹⁴C được duy trì như trong khí quyển; khi cây chết, "
     "¹⁴C chỉ giảm dần theo quy luật phóng xạ."),

dict(q="Độ phóng xạ của một mẫu chất giảm còn 1/8 giá trị ban đầu sau 24 ngày. Chu kì bán rã của chất đó là",
 o=["3 ngày.", "6 ngày.", "8 ngày.", "12 ngày."],
 a="C",
 sol="1/8 = (1/2)³ nên khoảng thời gian 24 ngày tương ứng với 3 chu kì bán rã, suy ra T = 24/3 = 8 ngày. "
     "Bẫy: chọn 3 ngày do nhầm số chu kì với chu kì."),

dict(q="Một nguồn phóng xạ phát ra tia có khả năng bị chặn hoàn toàn bởi một tờ giấy dày. Nguồn đó phát ra",
 o=["tia α.", "tia β⁻.", "tia γ.", "tia X."],
 a="A",
 sol="Chỉ tia α mới bị chặn bởi một tờ giấy do khả năng đâm xuyên rất yếu. Tia β cần vài milimét nhôm, "
     "còn tia γ và tia X cần vài centimét chì mới bị suy giảm đáng kể."),

dict(q="Vì sao một nguồn phát tia α có thể ít nguy hiểm khi ở ngoài cơ thể nhưng lại rất nguy hiểm nếu bị hít hoặc "
       "nuốt vào bên trong cơ thể?",
 o=["Vì bên trong cơ thể tia α chuyển thành tia γ.",
    "Vì lớp da đã chặn được tia α từ bên ngoài, còn khi ở bên trong, tia α ion hoá rất mạnh và giải phóng toàn bộ "
    "năng lượng vào một thể tích mô nhỏ.",
    "Vì bên trong cơ thể nhiệt độ cao làm chu kì bán rã giảm.",
    "Vì tia α chỉ gây hại khi có nước."],
 a="B",
 sol="Tia α có khả năng đâm xuyên rất yếu nên quần áo và lớp sừng của da đủ để chặn nó từ bên ngoài. "
     "Nhưng khả năng ion hoá của nó lại mạnh nhất; khi nguồn nằm trong cơ thể, toàn bộ năng lượng được hấp thụ "
     "trực tiếp bởi các tế bào sống ở ngay cạnh, gây tổn thương nặng."),

dict(q="Trong lò phản ứng hạt nhân, thanh điều khiển làm bằng boron hoặc cadmium có tác dụng",
 o=["làm chậm các neutron.", "hấp thụ bớt neutron để điều chỉnh hệ số nhân neutron.",
    "tải nhiệt ra khỏi vùng hoạt động.", "phản xạ neutron trở lại vùng nhiên liệu."],
 a="B",
 sol="Boron và cadmium hấp thụ neutron rất mạnh. Đưa thanh điều khiển vào sâu thì số neutron gây phân hạch giảm, "
     "k giảm; rút ra thì k tăng. Nhờ đó giữ được k = 1 để lò hoạt động ổn định. "
     "Việc làm chậm neutron là nhiệm vụ của chất làm chậm."),

dict(q="Ba tia phóng xạ α, β⁻ và γ cùng đi vào một từ trường đều theo phương vuông góc với đường sức từ. "
       "Nhận xét nào sau đây đúng?",
 o=["Tia α và tia β⁻ bị lệch về cùng một phía, tia γ đi thẳng.",
    "Tia α và tia β⁻ bị lệch về hai phía ngược nhau, tia γ đi thẳng.",
    "Cả ba tia đều bị lệch về cùng một phía.",
    "Cả ba tia đều đi thẳng."],
 a="B",
 sol="Tia α mang điện dương còn tia β⁻ mang điện âm, nên lực từ tác dụng lên chúng ngược chiều nhau và chúng "
     "lệch về hai phía đối nhau. Tia γ không mang điện nên không bị lệch. "
     "Ngoài ra tia β⁻ lệch nhiều hơn tia α vì khối lượng nhỏ hơn rất nhiều."),

dict(q="Đồ thị biểu diễn số hạt nhân còn lại của một mẫu chất phóng xạ theo thời gian được cho như hình vẽ. "
       "Từ đồ thị có thể xác định trực tiếp đại lượng nào sau đây?",
 fig="f20_dinh_luat_phong_xa",
 o=["Khối lượng ban đầu của mẫu tính bằng gam.",
    "Chu kì bán rã, bằng thời gian để số hạt nhân giảm còn một nửa giá trị ban đầu.",
    "Số proton của hạt nhân phóng xạ.",
    "Loại tia phóng xạ mà mẫu chất phát ra."],
 a="B",
 sol="Từ đồ thị N(t), ta tìm hoành độ ứng với tung độ N₀/2, đó chính là chu kì bán rã T; từ T suy ra λ = ln2/T. "
     "Đồ thị không cho biết gì về loại tia phóng xạ hay số proton của hạt nhân."),

dict(q="Hai mẫu chất phóng xạ của CÙNG một chất, mẫu thứ nhất có khối lượng gấp đôi mẫu thứ hai. So sánh nào sau "
       "đây là đúng?",
 o=["Mẫu thứ nhất có chu kì bán rã gấp đôi mẫu thứ hai.",
    "Hai mẫu có cùng chu kì bán rã, nhưng độ phóng xạ ban đầu của mẫu thứ nhất gấp đôi.",
    "Hai mẫu có cùng độ phóng xạ ban đầu.",
    "Mẫu thứ nhất có hằng số phóng xạ lớn gấp đôi."],
 a="B",
 sol="Chu kì bán rã T và hằng số phóng xạ λ là đặc trưng của loại hạt nhân, hoàn toàn không phụ thuộc khối lượng "
     "mẫu. Nhưng H = λN tỉ lệ với số hạt nhân, nên mẫu có khối lượng gấp đôi thì độ phóng xạ ban đầu cũng gấp đôi."),

dict(q="Xét phản ứng hạt nhân: ¹⁴₇N + ⁴₂He → X + ¹₁H. Hạt nhân X là",
 o=["¹⁷₈O.", "¹⁶₈O.", "¹⁷₉F.", "¹⁸₈O."],
 a="A",
 sol="Bảo toàn số khối: 14 + 4 = A + 1 ⟹ A = 17. Bảo toàn điện tích: 7 + 2 = Z + 1 ⟹ Z = 8. "
     "Vậy X là ¹⁷₈O. Đây chính là phản ứng hạt nhân nhân tạo đầu tiên do Rutherford thực hiện."),

dict(q="Một mẫu chất phóng xạ có chu kì bán rã T. Trong khoảng thời gian từ thời điểm t = T đến thời điểm t = 2T, "
       "số hạt nhân bị phân rã bằng",
 o=["N₀/2.", "N₀/4.", "N₀/8.", "3N₀/4."],
 a="B",
 sol="Tại t = T còn N₀/2 hạt; tại t = 2T còn N₀/4 hạt. Vậy trong khoảng thời gian đó có N₀/2 − N₀/4 = N₀/4 hạt "
     "phân rã. Lưu ý trong chu kì bán rã ĐẦU TIÊN có N₀/2 hạt phân rã — số hạt phân rã trong mỗi chu kì "
     "giảm dần chứ không phải như nhau."),

dict(q="Khối lượng của hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tạo thành nó. Điều này chứng tỏ",
 o=["một phần vật chất đã biến mất hoàn toàn.",
    "khi các nucleon liên kết thành hạt nhân, hệ đã toả ra một năng lượng bằng Δm·c².",
    "phép đo khối lượng hạt nhân luôn có sai số.",
    "các nucleon bị nén lại nên nhẹ đi."],
 a="B",
 sol="Khi các nucleon riêng rẽ kết hợp thành hạt nhân, hệ chuyển sang trạng thái có năng lượng thấp hơn và "
     "toả ra năng lượng E_lk = Δm·c². Năng lượng giảm đi kéo theo khối lượng của hệ giảm tương ứng theo hệ thức "
     "Einstein — không có vật chất nào biến mất."),
],

"Mức 4 – VẬN DỤNG CAO": [
dict(q="Phát biểu nào sau đây về chu kì bán rã là ĐÚNG?",
 o=["Sau hai chu kì bán rã, toàn bộ mẫu chất phóng xạ đã phân rã hết.",
    "Chu kì bán rã phụ thuộc vào khối lượng ban đầu của mẫu chất.",
    "Trong mỗi chu kì bán rã liên tiếp, số hạt nhân bị phân rã đều bằng nhau.",
    "Trong mỗi chu kì bán rã, một nửa số hạt nhân CÒN LẠI ở đầu chu kì đó bị phân rã."],
 a="D",
 sol="Quy luật phân rã là hàm mũ: trong mỗi chu kì, một nửa số hạt nhân còn lại tại đầu chu kì bị phân rã. "
     "Vì thế số hạt phân rã trong các chu kì liên tiếp là N₀/2, N₀/4, N₀/8… giảm dần chứ không bằng nhau, "
     "và mẫu chất về lí thuyết không bao giờ phân rã hết. Chu kì bán rã cũng không phụ thuộc khối lượng mẫu."),

dict(q="Hai mẫu chất phóng xạ khác nhau có khối lượng ban đầu khác nhau. Đại lượng nào sau đây chỉ phụ thuộc "
       "vào tỉ số t/T mà KHÔNG phụ thuộc khối lượng ban đầu của mẫu?",
 o=["Số hạt nhân còn lại N.", "Độ phóng xạ H.",
    "Tỉ số N/N₀ giữa số hạt nhân còn lại và số hạt nhân ban đầu.", "Số hạt nhân đã phân rã ΔN."],
 a="C",
 sol="Từ N = N₀·2^(−t/T) suy ra N/N₀ = 2^(−t/T), chỉ phụ thuộc tỉ số t/T. Các đại lượng N, ΔN và H đều tỉ lệ "
     "thuận với N₀ nên phụ thuộc khối lượng ban đầu. Nhận xét này rất hữu ích khi so sánh hai mẫu chất."),

dict(q="Một mẫu ²²⁶Ra được đưa vào một lò nung ở 1000 °C, một mẫu khác cùng loại được nén ở áp suất rất cao, "
       "mẫu thứ ba được cho phản ứng tạo thành hợp chất hoá học. So với mẫu để ở điều kiện thường, chu kì bán rã "
       "của ba mẫu này",
 o=["đều giảm.", "đều tăng.", "đều không thay đổi.", "thay đổi khác nhau tuỳ theo tác động."],
 a="C",
 sol="Phóng xạ là quá trình xảy ra bên trong hạt nhân, hoàn toàn không phụ thuộc trạng thái của lớp vỏ electron "
     "hay điều kiện ngoại cảnh. Nhiệt độ, áp suất và liên kết hoá học đều không làm thay đổi chu kì bán rã. "
     "Đây là điểm khác biệt căn bản giữa phản ứng hạt nhân và phản ứng hoá học."),

dict(q="Trong phân rã β⁻ của một hạt nhân, nhận định nào sau đây là ĐÚNG?",
 o=["Số proton và số neutron của hạt nhân đều được bảo toàn.",
    "Số proton tăng 1, số neutron giảm 1, nhưng tổng số nucleon không đổi.",
    "Số nucleon giảm 1 vì hạt nhân mất một electron.",
    "Cả số nucleon và điện tích của hạt nhân đều không đổi."],
 a="B",
 sol="Phân rã β⁻ thực chất là n → p + e⁻ + phản neutrino. Vì một neutron biến thành một proton nên số proton "
     "tăng 1, số neutron giảm 1, còn tổng số nucleon A không đổi. Điện tích của hạt nhân tăng thêm 1 đơn vị, "
     "nhưng tổng điện tích của cả hệ (kể cả electron phát ra) vẫn được bảo toàn."),

dict(q="Hạt nhân ⁴He có số khối nhỏ hơn hạt nhân ⁷Li nhưng năng lượng liên kết riêng lại lớn hơn "
       "(7,07 MeV/nucleon so với 5,61 MeV/nucleon). Điều này cho thấy",
 o=["năng lượng liên kết riêng luôn giảm khi số khối tăng.",
    "năng lượng liên kết riêng không phải là hàm đơn điệu của số khối; một số hạt nhân như ⁴He bền vững "
    "bất thường so với các hạt nhân lân cận.",
    "phép đo năng lượng liên kết của ⁷Li bị sai.",
    "⁷Li không thể tồn tại trong tự nhiên."],
 a="B",
 sol="Đường cong năng lượng liên kết riêng nhìn chung tăng ở vùng A nhỏ, nhưng có những “đỉnh nhô” cục bộ ở các "
     "hạt nhân có số proton và số neutron đều chẵn và bằng nhau như ⁴He, ¹²C, ¹⁶O. Chính vì ⁴He bền vững bất thường "
     "mà nó được phát ra nguyên vẹn dưới dạng hạt α trong phóng xạ."),

dict(q="Dựa vào đường cong năng lượng liên kết riêng, quá trình nào sau đây KHÔNG thể toả năng lượng?",
 fig="f19_nllk_rieng",
 o=["Hai hạt nhân deuterium kết hợp thành hạt nhân helium.",
    "Hạt nhân ²³⁵U vỡ thành hai hạt nhân có số khối trung bình.",
    "Hạt nhân ⁵⁶Fe vỡ thành hai hạt nhân nhẹ hơn.",
    "Hạt nhân ²³⁸U phóng xạ α tạo thành ²³⁴Th."],
 a="C",
 sol="Năng lượng chỉ toả ra khi hệ tiến về phía đỉnh của đường cong, tức làm tăng năng lượng liên kết riêng. "
     "⁵⁶Fe đã nằm ở đỉnh nên mọi cách chia nhỏ nó đều cho các mảnh có ε NHỎ HƠN, tức phải THU năng lượng. "
     "Ba quá trình còn lại đều đi về phía vùng bền vững hơn nên toả năng lượng."),

dict(q="Một phản ứng hạt nhân có tổng khối lượng nghỉ sau phản ứng lớn hơn trước phản ứng. Phản ứng này",
 o=["không bao giờ xảy ra được vì vi phạm bảo toàn năng lượng.",
    "là phản ứng thu năng lượng, chỉ xảy ra khi các hạt tương tác được cung cấp đủ động năng.",
    "là phản ứng toả năng lượng.",
    "chỉ xảy ra trong lòng các ngôi sao."],
 a="B",
 sol="W = (m_trước − m_sau)c² < 0 nên đây là phản ứng thu năng lượng. Nó vẫn xảy ra được nếu ta cung cấp năng lượng "
     "từ bên ngoài, thường bằng cách tăng tốc hạt bắn vào để nó có đủ động năng — đó chính là nguyên lí hoạt động "
     "của các máy gia tốc. Định luật bảo toàn năng lượng toàn phần vẫn được tôn trọng."),

dict(q="Một mẫu chất phóng xạ được theo dõi trong thời gian dài. Người ta nhận thấy độ phóng xạ của mẫu giảm dần "
       "theo thời gian. Nguyên nhân là",
 o=["hằng số phóng xạ λ của chất đó giảm dần.",
    "chu kì bán rã của chất đó tăng dần.",
    "số hạt nhân phóng xạ còn lại trong mẫu giảm dần, trong khi λ không đổi.",
    "các hạt nhân còn lại trở nên bền vững hơn theo thời gian."],
 a="C",
 sol="H = λN với λ là hằng số đặc trưng của chất, không thay đổi theo thời gian. Độ phóng xạ giảm chỉ vì số hạt "
     "nhân phóng xạ N còn lại giảm dần theo quy luật hàm mũ. Các hạt nhân chưa phân rã không hề “già đi” hay "
     "trở nên bền hơn — xác suất phân rã của mỗi hạt trong một đơn vị thời gian luôn như nhau."),

dict(q="Về tính ngẫu nhiên của hiện tượng phóng xạ, phát biểu nào sau đây là ĐÚNG?",
 o=["Có thể dự đoán chính xác thời điểm phân rã của từng hạt nhân nếu biết đủ dữ kiện.",
    "Không thể dự đoán thời điểm phân rã của một hạt nhân cụ thể, nhưng có thể dự đoán khá chính xác tỉ lệ "
    "hạt nhân còn lại của một mẫu chứa rất nhiều hạt nhân.",
    "Các hạt nhân trong mẫu phân rã lần lượt theo thứ tự từ ngoài vào trong.",
    "Hạt nhân nào tồn tại càng lâu thì xác suất phân rã trong giây tiếp theo càng lớn."],
 a="B",
 sol="Phóng xạ tuân theo quy luật thống kê: mỗi hạt nhân có cùng một xác suất phân rã trong mỗi đơn vị thời gian, "
     "không phụ thuộc “tuổi” của nó, và không thể biết trước hạt nào sẽ phân rã khi nào. Nhưng với số hạt nhân "
     "rất lớn, quy luật trung bình N = N₀2^(−t/T) lại rất chính xác."),

dict(q="So sánh phản ứng phân hạch và phản ứng phóng xạ α, nhận định nào sau đây ĐÚNG?",
 o=["Cả hai đều là quá trình tự phát, không cần tác động bên ngoài.",
    "Phóng xạ α là quá trình tự phát, còn phân hạch trong lò phản ứng cần được kích thích bằng neutron.",
    "Cả hai đều cần được kích thích bằng neutron.",
    "Cả hai đều làm số khối của hạt nhân giảm đi đúng 4 đơn vị."],
 a="B",
 sol="Phóng xạ α xảy ra tự phát, không thể can thiệp được. Phân hạch dùng trong lò phản ứng là phản ứng kích thích: "
     "hạt nhân ²³⁵U phải hấp thụ một neutron chậm mới vỡ ra, nhờ đó con người mới điều khiển được tốc độ phản ứng "
     "bằng thanh điều khiển."),

dict(q="Trong một mẫu chất phóng xạ, nhận định nào sau đây về mối quan hệ giữa số hạt nhân còn lại N và độ phóng "
       "xạ H là ĐÚNG?",
 o=["N và H giảm theo hai quy luật khác nhau với hai chu kì bán rã khác nhau.",
    "N giảm theo hàm mũ còn H giảm tuyến tính theo thời gian.",
    "N và H giảm theo cùng một quy luật hàm mũ với cùng một chu kì bán rã.",
    "H không đổi trong khi N giảm dần."],
 a="C",
 sol="Vì H = λN với λ là hằng số, H luôn tỉ lệ thuận với N. Do đó H = H₀·2^(−t/T) giảm theo đúng quy luật và đúng "
     "chu kì bán rã như N. Chính vì thế người ta có thể xác định T bằng cách đo độ phóng xạ mà không cần đếm "
     "số hạt nhân."),

dict(q="Xét hai hạt nhân X và Y có cùng số khối A. Hạt nhân X có độ hụt khối lớn hơn hạt nhân Y. Kết luận đúng là",
 o=["X kém bền vững hơn Y.", "X bền vững hơn Y.",
    "hai hạt nhân bền vững như nhau vì cùng số khối.", "không so sánh được độ bền vững."],
 a="B",
 sol="E_lk = Δm·c² nên độ hụt khối lớn hơn đồng nghĩa với năng lượng liên kết lớn hơn. Vì hai hạt nhân có CÙNG "
     "số khối A, so sánh E_lk cũng tương đương so sánh ε = E_lk/A. Vậy X bền vững hơn Y. "
     "Lưu ý điều kiện “cùng số khối” là mấu chốt — nếu khác A thì bắt buộc phải so sánh ε."),

dict(q="Một nguồn phóng xạ được đặt cách nhân viên y tế một khoảng d. Nếu nhân viên lùi ra xa để khoảng cách tăng "
       "gấp 3 lần thì cường độ bức xạ mà người đó nhận được giảm còn",
 o=["1/3 giá trị ban đầu.", "1/6 giá trị ban đầu.", "1/9 giá trị ban đầu.", "1/27 giá trị ban đầu."],
 a="C",
 sol="Bức xạ phát ra đều theo mọi hướng nên năng lượng phân bố trên mặt cầu có diện tích 4πd². Cường độ bức xạ "
     "tỉ lệ nghịch với bình phương khoảng cách, do đó tăng khoảng cách 3 lần thì cường độ giảm 3² = 9 lần. "
     "Đây là cơ sở định lượng của nguyên tắc “khoảng cách” trong an toàn phóng xạ."),

dict(q="Nhận định nào sau đây về nhà máy điện hạt nhân là ĐÚNG?",
 o=["Nhà máy điện hạt nhân hoạt động nhờ phản ứng nhiệt hạch có điều khiển.",
    "Năng lượng từ phản ứng phân hạch được dùng để đun nước tạo hơi làm quay tuabin của máy phát điện.",
    "Lò phản ứng biến đổi trực tiếp năng lượng hạt nhân thành điện năng mà không qua giai đoạn nhiệt.",
    "Nhà máy điện hạt nhân không tạo ra chất thải phóng xạ."],
 a="B",
 sol="Nhà máy điện hạt nhân hiện nay dùng phản ứng PHÂN HẠCH có điều khiển (k = 1). Năng lượng phân hạch làm nóng "
     "chất tải nhiệt, chất này đun nước thành hơi, hơi làm quay tuabin nối với máy phát điện — vẫn phải qua giai "
     "đoạn nhiệt. Chất thải phóng xạ là vấn đề lớn cần xử lí lâu dài. Nhiệt hạch có điều khiển thì chưa được "
     "thương mại hoá."),
],
}

DS4 = [
dict(stem="Hình vẽ biểu diễn năng lượng liên kết riêng của các hạt nhân theo số khối A. Xét các nhận định sau.",
 fig="f19_nllk_rieng",
 items=[
  ("Hạt nhân ⁵⁶Fe nằm gần đỉnh của đường cong nên thuộc nhóm các hạt nhân bền vững nhất.", True,
   "Đỉnh của đường cong ứng với ε lớn nhất (≈ 8,79 MeV/nucleon), tức hạt nhân bền vững nhất."),
  ("Hạt nhân ²³⁵U có năng lượng liên kết lớn hơn hạt nhân ⁴He nhưng lại kém bền vững hơn ⁵⁶Fe.", True,
   "E_lk của ²³⁵U ≈ 1784 MeV lớn hơn nhiều so với 28,3 MeV của ⁴He vì có nhiều nucleon hơn; "
   "nhưng ε của ²³⁵U (≈ 7,59) nhỏ hơn của ⁵⁶Fe (≈ 8,79) nên kém bền hơn."),
  ("Khi hai hạt nhân rất nhẹ tổng hợp thành một hạt nhân nặng hơn, năng lượng liên kết riêng tăng lên nên "
   "phản ứng toả năng lượng.", True,
   "Ở vùng A nhỏ, đường cong đi lên, nên sản phẩm có ε lớn hơn các hạt ban đầu; hệ chuyển sang trạng thái bền "
   "vững hơn và toả năng lượng."),
  ("Có thể thu được năng lượng bằng cách phân chia hạt nhân ⁵⁶Fe thành hai hạt nhân nhẹ hơn.", False,
   "⁵⁶Fe đã ở đỉnh đường cong; mọi mảnh vỡ của nó đều có ε nhỏ hơn, nên quá trình này THU năng lượng "
   "chứ không toả năng lượng."),
 ]),

dict(stem="Một nhóm học sinh đo độ phóng xạ H của một mẫu chất theo thời gian và thu được bảng số liệu: "
          "t = 0 h: H = 800 Bq; t = 1 h: 566 Bq; t = 2 h: 400 Bq; t = 3 h: 283 Bq; t = 4 h: 200 Bq; "
          "t = 5 h: 141 Bq; t = 6 h: 100 Bq. Xét các nhận định sau.",
 fig="f25_semilog",
 items=[
  ("Chu kì bán rã của mẫu chất là 2 giờ.", True,
   "Độ phóng xạ giảm một nửa sau mỗi 2 giờ: 800 → 400 → 200 → 100 Bq tại t = 0; 2; 4; 6 h."),
  ("Đồ thị biểu diễn lnH theo t là một đường thẳng có hệ số góc âm.", True,
   "Từ H = H₀e^(−λt) suy ra lnH = lnH₀ − λt, là hàm bậc nhất của t với hệ số góc −λ < 0."),
  ("Hằng số phóng xạ của mẫu chất xấp xỉ 0,35 giờ⁻¹.", True,
   "λ = ln2/T = 0,693/2 ≈ 0,35 giờ⁻¹, phù hợp với hệ số góc của đồ thị tuyến tính hoá."),
  ("Sau 10 giờ kể từ lúc bắt đầu đo, độ phóng xạ của mẫu vẫn còn lớn hơn 50 Bq.", False,
   "10 giờ ứng với 5 chu kì bán rã: H = 800·2⁻⁵ = 25 Bq < 50 Bq."),
 ]),

dict(stem="Đồng vị ²¹⁰₈₄Po là chất phóng xạ α với chu kì bán rã T = 138 ngày. Xét các nhận định sau.",
 items=[
  ("Hạt nhân con tạo thành sau phân rã là ²⁰⁶₈₂Pb.", True,
   "Bảo toàn số khối: 210 − 4 = 206; bảo toàn điện tích: 84 − 2 = 82, ứng với nguyên tố chì."),
  ("Hạt nhân ²¹⁰₈₄Po có 126 neutron.", True, "N = A − Z = 210 − 84 = 126."),
  ("Sau 276 ngày, đã có 75% số hạt nhân Po ban đầu bị phân rã.", True,
   "276 ngày = 2T, số hạt còn lại bằng 1/4 nên số hạt đã phân rã chiếm 3/4 = 75%."),
  ("Tia α do Po phát ra có khả năng đâm xuyên mạnh hơn tia γ.", False,
   "Tia α có khả năng đâm xuyên yếu nhất trong ba loại tia, bị chặn ngay bởi một tờ giấy, "
   "trong khi tia γ cần vài centimét chì."),
 ]),

dict(stem="Trong khảo cổ học, người ta dùng đồng vị phóng xạ ¹⁴C (chu kì bán rã 5730 năm) để xác định niên đại "
          "của các mẫu vật có nguồn gốc sinh vật. Một mẫu gỗ cổ có độ phóng xạ bằng 1/4 độ phóng xạ của mẫu gỗ "
          "tươi cùng loại và cùng khối lượng. Xét các nhận định sau.",
 items=[
  ("Hạt nhân ¹⁴₆C có 8 neutron.", True,
   "Số neutron bằng hiệu giữa số khối và số proton: N = A − Z = 14 − 6 = 8."),
  ("Tuổi của mẫu gỗ cổ khoảng 11460 năm.", True,
   "Độ phóng xạ giảm còn 1/4 = (1/2)² ứng với 2 chu kì bán rã: t = 2 × 5730 = 11460 năm."),
  ("Khi cây còn sống, tỉ lệ ¹⁴C trong cơ thể nó được duy trì gần như không đổi nhờ quá trình trao đổi chất "
   "với môi trường.", True,
   "Cây liên tục hấp thụ carbon từ khí quyển, nơi tỉ lệ ¹⁴C/¹²C gần như ổn định, nên tỉ lệ này trong cơ thể "
   "cũng ổn định; khi cây chết, ¹⁴C không được bổ sung nữa mà chỉ phân rã."),
  ("Nếu bảo quản mẫu gỗ ở nhiệt độ rất thấp thì chu kì bán rã của ¹⁴C trong mẫu sẽ tăng lên, làm phép xác định "
   "niên đại sai lệch.", False,
   "Chu kì bán rã không phụ thuộc nhiệt độ hay bất kì điều kiện bên ngoài nào, nên việc bảo quản lạnh không "
   "ảnh hưởng đến kết quả."),
 ]),

dict(stem="Trong lò phản ứng của một nhà máy điện hạt nhân, hạt nhân ²³⁵U hấp thụ một neutron chậm rồi phân hạch, "
          "toả ra khoảng 200 MeV và phát ra 2 – 3 neutron mới. Xét các nhận định sau.",
 fig="f22_phan_hach",
 items=[
  ("Neutron chậm dễ bị hạt nhân ²³⁵U hấp thụ hơn neutron nhanh.", True,
   "Neutron chậm ở gần hạt nhân lâu hơn nên xác suất bị hấp thụ lớn hơn nhiều; vì thế lò phản ứng cần chất làm chậm."),
  ("Các thanh điều khiển bằng boron hoặc cadmium hấp thụ bớt neutron để giữ hệ số nhân neutron bằng 1.", True,
   "Nhờ điều chỉnh độ sâu của thanh điều khiển, người ta giữ k = 1 để phản ứng dây chuyền diễn ra ổn định."),
  ("Nếu hệ số nhân neutron k nhỏ hơn 1 thì phản ứng dây chuyền vẫn tự duy trì ổn định.", False,
   "Với k < 1, số phân hạch giảm dần qua các thế hệ nên phản ứng dây chuyền tắt dần. Chỉ k = 1 mới cho chế độ ổn định."),
  ("Năng lượng thu được khi 1 g ²³⁵U phân hạch hoàn toàn lớn hơn rất nhiều so với khi đốt cháy 1 g than.", True,
   "1 g ²³⁵U chứa khoảng 2,6·10²¹ hạt nhân, toả ra cỡ 8·10¹⁰ J, trong khi 1 g than chỉ cho khoảng 3·10⁴ J — "
   "chênh nhau hàng triệu lần."),
 ]),

dict(stem="Xét phản ứng tổng hợp hạt nhân: ²₁H + ³₁H → ⁴₂He + ¹₀n, toả ra năng lượng 17,6 MeV.",
 fig="f23_nhiet_hach",
 items=[
  ("Tổng số nucleon trước và sau phản ứng đều bằng 5.", True,
   "Trước: 2 + 3 = 5; sau: 4 + 1 = 5, phù hợp định luật bảo toàn số nucleon."),
  ("Đây là phản ứng toả năng lượng nên tổng khối lượng nghỉ của các hạt sau phản ứng nhỏ hơn trước phản ứng.", True,
   "W = (m_trước − m_sau)c² = 17,6 MeV > 0 nên m_sau < m_trước."),
  ("Tính trên mỗi nucleon, năng lượng toả ra của phản ứng này lớn hơn của phản ứng phân hạch ²³⁵U.", True,
   "Ở đây 17,6/5 ≈ 3,5 MeV/nucleon, trong khi phân hạch cho khoảng 200/236 ≈ 0,85 MeV/nucleon."),
  ("Phản ứng này dễ thực hiện ở nhiệt độ phòng vì các hạt nhân tham gia đều rất nhẹ.", False,
   "Dù nhẹ, hai hạt nhân vẫn mang điện dương và đẩy nhau rất mạnh. Cần nhiệt độ cỡ hàng trăm triệu độ để chúng "
   "tiến đủ gần nhau, nên nhiệt hạch có điều khiển đến nay vẫn chưa được thương mại hoá."),
 ]),

dict(stem="Trong xạ trị ung thư, người ta thường dùng nguồn ⁶⁰₂₇Co phát tia γ để chiếu vào khối u nằm sâu trong "
          "cơ thể bệnh nhân. Xét các nhận định sau.",
 fig="f24_bien_bao",
 items=[
  ("Hạt nhân ⁶⁰₂₇Co có 33 neutron.", True, "N = A − Z = 60 − 27 = 33."),
  ("Tia γ được chọn vì có khả năng đâm xuyên mạnh, tới được khối u nằm sâu bên trong cơ thể.", True,
   "Tia α và tia β sẽ bị các lớp mô bên ngoài hấp thụ gần hết, không tới được khối u."),
  ("Khi không làm việc, nguồn phóng xạ được cất trong hộp chì dày và nhân viên đứng sau tấm chắn chì.", True,
   "Chì có khối lượng riêng lớn nên hấp thụ tia γ hiệu quả; đây là ứng dụng của nguyên tắc che chắn."),
  ("Nếu nhân viên y tế lùi ra xa nguồn để khoảng cách tăng gấp đôi thì cường độ bức xạ nhận được giảm còn một nửa.", False,
   "Cường độ bức xạ tỉ lệ nghịch với BÌNH PHƯƠNG khoảng cách, nên khi khoảng cách tăng gấp đôi, cường độ giảm "
   "còn 1/4 chứ không phải 1/2."),
 ]),

dict(stem="Đồ thị biểu diễn số hạt nhân còn lại N của một mẫu chất phóng xạ theo thời gian t (tính theo chu kì "
          "bán rã T). Xét các nhận định sau.",
 fig="f20_dinh_luat_phong_xa",
 items=[
  ("Sau thời gian 3T, số hạt nhân còn lại bằng 1/8 số hạt nhân ban đầu.", True,
   "Áp dụng N = N₀·2^(−t/T) với t = 3T: N = N₀·2⁻³ = N₀/8, đúng như giá trị đọc được trên đồ thị."),
  ("Sau thời gian 3T, số hạt nhân đã phân rã bằng 7/8 số hạt nhân ban đầu.", True,
   "Số hạt đã phân rã bằng hiệu giữa số ban đầu và số còn lại: ΔN = N₀ − N₀/8 = 7N₀/8, tức 87,5%."),
  ("Sau thời gian 2T, tỉ số giữa số hạt nhân đã phân rã và số hạt nhân còn lại bằng 3.", True,
   "Sau 2T còn lại N₀/4, nên số đã phân rã là N₀ − N₀/4 = 3N₀/4; tỉ số (3N₀/4)/(N₀/4) = 3."),
  ("Đồ thị cắt trục hoành tại t = 4T, chứng tỏ sau 4 chu kì bán rã mẫu chất đã phân rã hết.", False,
   "Đồ thị hàm mũ tiệm cận trục hoành chứ không cắt nó; sau 4T vẫn còn N₀/16 số hạt nhân. "
   "Về lí thuyết mẫu chất không bao giờ phân rã hết hoàn toàn."),
 ]),
]
