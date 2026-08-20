# -*- coding: utf-8 -*-
"""Kéo dài các phương án nhiễu để đáp án đúng không bị lộ vì dài vượt trội.

Mỗi cặp là (chuỗi cũ, chuỗi mới). Nội dung sai của phương án nhiễu được giữ
nguyên bản chất, chỉ diễn đạt đầy đủ hơn cho cân xứng với đáp án đúng.
"""
import io, sys

PATCHES = {
"ch1_concept.py": [
 ("Cốc nước có nội năng lớn hơn nên nhiệt sẽ truyền từ cốc nước sang giọt nước.",
  "Cốc nước có nội năng lớn hơn giọt nước nên nhiệt sẽ truyền từ cốc nước sang "
  "giọt nước cho tới khi cân bằng."),
 ("Giọt nước có nội năng lớn hơn vì nhiệt độ của nó cao hơn.",
  "Giọt nước có nội năng lớn hơn cốc nước vì nhiệt độ của nó cao hơn nhiều, "
  "nên nhiệt truyền từ giọt sang cốc."),
 ("Hai vật có nội năng bằng nhau vì cùng là nước.",
  "Hai vật có nội năng bằng nhau vì cùng là nước, do đó không có nhiệt truyền "
  "giữa chúng khi tiếp xúc."),

 ("Vì nhiệt độ sôi (100 °C) cao hơn nhiệt độ nóng chảy (0 °C).",
  "Vì nhiệt độ sôi của nước (100 °C) cao hơn hẳn nhiệt độ nóng chảy (0 °C), mà nhiệt "
  "lượng cần cung cấp thì tỉ lệ với nhiệt độ xảy ra quá trình."),
 ("Vì hơi nước có khối lượng riêng nhỏ hơn nước lỏng.",
  "Vì hơi nước có khối lượng riêng nhỏ hơn nước lỏng rất nhiều, nên cùng một khối "
  "lượng thì hơi chiếm thể tích lớn hơn và cần nhiều năng lượng hơn."),
 ("Vì quá trình sôi diễn ra trong thời gian dài hơn quá trình nóng chảy.",
  "Vì trên thực tế quá trình sôi luôn diễn ra trong thời gian dài hơn quá trình nóng "
  "chảy, nên tổng nhiệt lượng phải cung cấp cũng lớn hơn."),

 ("khối lượng khí trong bơm tăng lên nên nội năng tăng.",
  "khối lượng khí bên trong thân bơm tăng lên sau mỗi lần đẩy pit-tông, mà nội năng "
  "tỉ lệ với số phân tử nên nội năng của khí tăng theo."),
 ("khí trong bơm nhận nhiệt lượng từ không khí bên ngoài nên nóng lên.",
  "khí trong bơm nhận nhiệt lượng truyền từ không khí bên ngoài qua thành bơm bằng "
  "kim loại, vì kim loại dẫn nhiệt rất tốt."),
 ("khí trong bơm dãn nở nên sinh công và nóng lên.",
  "khí trong bơm dãn nở khi được đẩy qua van vào lốp, quá trình sinh công này làm nội "
  "năng và nhiệt độ của khí tăng lên."),

 ("Sự bay hơi chỉ xảy ra khi chất lỏng đạt tới nhiệt độ sôi.",
  "Sự bay hơi chỉ xảy ra khi chất lỏng được đun tới đúng nhiệt độ sôi xác định của nó."),
 ("Sự bay hơi làm cho phần chất lỏng còn lại nóng lên.",
  "Sự bay hơi là quá trình toả nhiệt nên làm cho phần chất lỏng còn lại nóng lên."),
 ("Tốc độ bay hơi không phụ thuộc vào diện tích mặt thoáng.",
  "Tốc độ bay hơi không phụ thuộc diện tích mặt thoáng mà chỉ phụ thuộc nhiệt độ."),

 ("áp suất cao làm nhiệt dung riêng của nước giảm mạnh.",
  "áp suất cao trong nồi làm nhiệt dung riêng của nước giảm mạnh nên nước nóng lên "
  "nhanh hơn hẳn."),
 ("áp suất trong nồi cao làm nước sôi nhanh hơn, tiết kiệm thời gian đun.",
  "áp suất trong nồi cao làm nước sôi nhanh hơn hẳn so với nồi thường, nhờ đó tiết "
  "kiệm được thời gian đun."),
 ("nồi áp suất truyền nhiệt tốt hơn nồi thường nhiều lần.",
  "thành nồi áp suất dày và kín nên truyền nhiệt vào thức ăn tốt hơn nồi thường "
  "nhiều lần."),

 ("Nước đá có cùng khối lượng riêng với nước lỏng nên lơ lửng.",
  "Nước đá có khối lượng riêng đúng bằng nước lỏng nên nó lơ lửng ở giữa chứ không "
  "nổi hẳn lên mặt nước."),
 ("Nước đá nổi trên nước lỏng vì mọi chất rắn đều nhẹ hơn chất lỏng của nó.",
  "Nước đá nổi trên nước lỏng vì mọi chất rắn đều có khối lượng riêng nhỏ hơn chất "
  "lỏng của chính nó."),
 ("Nước đá chìm trong nước lỏng vì chất rắn có khoảng cách phân tử nhỏ hơn.",
  "Nước đá chìm trong nước lỏng vì ở thể rắn khoảng cách giữa các phân tử nhỏ hơn "
  "nên khối lượng riêng lớn hơn."),

 ('"Nhiệt độ của nước.",', '"Nhiệt độ của khối nước trong bình.",'),
 ('"Khối lượng nước.",', '"Khối lượng của khối nước trong bình.",'),
 ('"Thể của nước (lỏng hay hơi)."', '"Thể của nước trong bình (lỏng hay hơi)."'),

 ("khí nhận nhiệt từ môi trường nên nội năng tăng và nhiệt độ giảm.",
  "khí nhận nhiệt lượng từ môi trường xung quanh nên nội năng của nó tăng lên, đồng "
  "thời nhiệt độ tại miệng bình giảm xuống."),
 ("khối lượng khí trong bình giảm nên nhiệt độ khí giảm theo tỉ lệ.",
  "khối lượng khí còn lại trong bình giảm đi nhanh chóng, mà nhiệt độ tỉ lệ thuận "
  "với khối lượng nên nhiệt độ cũng giảm."),
 ("khí bị nén mạnh khi ra khỏi bình nên nhiệt độ giảm.",
  "khí bị nén mạnh khi phải chui qua khe hẹp ở miệng bình, quá trình nén này làm "
  "nhiệt độ của nó giảm xuống."),

 ("Để khối lượng nước đá kịp giảm xuống một giá trị đã biết trước.",
  "Để khối lượng nước đá trong bình kịp giảm xuống đúng một giá trị đã biết trước "
  "khi bắt đầu phép đo."),
 ("Để nước đá kịp hấp thụ nhiệt từ không khí, giúp thí nghiệm nhanh hơn.",
  "Để nước đá kịp hấp thụ nhiệt lượng từ không khí xung quanh, nhờ đó rút ngắn được "
  "thời gian làm thí nghiệm."),
 ("Để điện trở nung kịp đạt trạng thái ổn định về điện.",
  "Để dòng điện qua điện trở nung kịp đạt trạng thái ổn định, giúp công suất đọc "
  "trên oát kế được chính xác."),

 ("nước đông đặc dần thành đá.",
  "nước trong cốc sẽ đông đặc dần thành nước đá và toả nhiệt."),
 ("nước đá tan dần thành nước.",
  "cục nước đá sẽ tan dần thành nước lỏng ở nhiệt độ 0 °C."),
 ("nhiệt độ của cả hệ giảm xuống dưới 0 °C.",
  "nhiệt độ của cả hệ sẽ giảm dần xuống thấp hơn 0 °C."),

 ("phải đổi thành 303 rồi mới thay vào công thức.",
  "phải đổi thành 303 K rồi mới thay vào công thức tính nhiệt lượng."),
 ("phải đổi thành 243 rồi mới thay vào công thức.",
  "phải đổi thành 243 K rồi mới thay vào công thức tính nhiệt lượng."),
 ("phải chia cho 273 rồi mới thay vào công thức.",
  "phải chia giá trị đó cho 273 rồi mới thay vào công thức tính nhiệt lượng."),

 ("Lập luận hoàn toàn đúng.",
  "Lập luận hoàn toàn đúng, cả ở tiền đề lẫn ở kết luận được rút ra."),
 ("Lập luận sai ở tiền đề: nội năng khí lí tưởng còn phụ thuộc thể tích.",
  "Lập luận sai ngay ở tiền đề: nội năng của khí lí tưởng còn phụ thuộc cả vào thể "
  "tích của khối khí."),
 ("Lập luận sai vì khí lí tưởng không thể dãn nở đẳng nhiệt.",
  "Lập luận sai vì trên thực tế khí lí tưởng không thể thực hiện được quá trình dãn "
  "nở đẳng nhiệt."),

 ("Mỗi cục đá thả sau làm nhiệt độ giảm nhiều hơn cục trước.",
  "Mỗi cục đá thả sau làm nhiệt độ của bình giảm nhiều hơn cục trước đó, vì nước "
  "trong bình đã nguội sẵn."),
 ("Nhiệt độ giảm đều cho tới khi đạt 0 °C rồi mọi cục đá sau đều tan hết.",
  "Nhiệt độ giảm đều đặn cho tới khi đạt 0 °C, sau đó mọi cục đá thả thêm vào đều "
  "vẫn tiếp tục tan hết."),

 ("để nước không bị sôi trong quá trình đo.",
  "để nước trong nhiệt lượng kế không bị sôi trong suốt quá trình đo đạc."),
 ("để nhiệt kế hoạt động chính xác hơn ở gần nhiệt độ phòng.",
  "để nhiệt kế hoạt động chính xác hơn, do nó được hiệu chuẩn ở gần nhiệt độ phòng."),
 ("để rút ngắn thời gian làm thí nghiệm.",
  "để rút ngắn thời gian làm thí nghiệm, nhờ đó giảm được sai số ngẫu nhiên khi đọc số."),

 ("hỗn hợp nước và đá ở khoảng 5 °C.",
  "hỗn hợp nước và đá ở nhiệt độ khoảng 5 °C."),
 ("toàn bộ là nước ở khoảng 0 °C.",
  "toàn bộ chuyển thành nước ở nhiệt độ khoảng 0 °C."),
 ("toàn bộ là nước ở khoảng 12 °C.",
  "toàn bộ chuyển thành nước ở nhiệt độ khoảng 12 °C."),

 ("đúng, vì cọ xát chỉ làm nóng bề mặt còn nung lửa làm nóng toàn bộ.",
  "đúng, vì cọ xát chỉ làm nóng lớp bề mặt của vật còn nung bằng lửa thì làm nóng "
  "toàn bộ vật."),
 ("đúng, vì cọ xát là thực hiện công còn nung lửa là truyền nhiệt.",
  "đúng, vì cọ xát là thực hiện công còn nung bằng lửa là truyền nhiệt, hai cách cho "
  "kết quả khác nhau."),
 ("sai, vì cọ xát không thể làm tăng nội năng của vật.",
  "sai, vì cọ xát không phải là cách có thể làm tăng nội năng của một vật rắn."),
],

"ch2_concept.py": [
 ("lực hút giữa các phân tử tăng lên khi chúng ở gần nhau hơn.",
  "lực hút giữa các phân tử khí tăng lên đáng kể khi chúng bị dồn lại gần nhau hơn, "
  "làm cho áp suất tăng."),
 ("tốc độ trung bình của các phân tử tăng nên mỗi va chạm mạnh hơn.",
  "tốc độ trung bình của các phân tử tăng lên nên mỗi va chạm vào thành bình đều "
  "truyền một xung lượng lớn hơn."),
 ("cả mật độ phân tử và tốc độ phân tử đều tăng.",
  "cả mật độ phân tử lẫn tốc độ chuyển động nhiệt của phân tử đều tăng lên khi thể "
  "tích bị thu nhỏ lại."),

 ("Cả động năng trung bình và tốc độ căn quân phương của hai loại phân tử đều "
  "bằng nhau.",
  "Cả động năng tịnh tiến trung bình lẫn tốc độ căn quân phương của hai loại phân tử "
  "đều bằng nhau."),
 ("Phân tử oxygen có động năng trung bình lớn hơn vì khối lượng lớn hơn.",
  "Phân tử oxygen có động năng tịnh tiến trung bình lớn hơn vì khối lượng phân tử của "
  "nó lớn hơn nhiều."),
 ("Phân tử hydrogen có động năng trung bình lớn hơn vì chuyển động nhanh hơn.",
  "Phân tử hydrogen có động năng tịnh tiến trung bình lớn hơn vì nó chuyển động nhanh "
  "hơn hẳn phân tử oxygen."),

 ("đồ thị p theo V không thể vẽ được vì hai đại lượng khác đơn vị.",
  "đồ thị p theo V không thể vẽ được vì hai đại lượng này có đơn vị khác nhau nên "
  "không so sánh được với nhau."),
 ("định luật Boyle chỉ đúng khi biểu diễn theo 1/V.",
  "định luật Boyle chỉ được nghiệm đúng khi biểu diễn áp suất theo nghịch đảo của "
  "thể tích chứ không theo thể tích."),
 ("đại lượng 1/V dễ đo hơn đại lượng V trong thí nghiệm.",
  "đại lượng 1/V dễ đo trực tiếp hơn đại lượng V trong bộ thí nghiệm khảo sát định "
  "luật Boyle."),

 ("đo nhiệt độ của khí trong ống.",
  "đo nhiệt độ của cột khí bị nhốt bên trong ống nghiệm."),
 ("làm tăng áp suất khí trong ống theo nhiệt độ.",
  "làm cho áp suất của khí trong ống tăng dần lên theo nhiệt độ."),
 ("giữ cho thể tích khí trong ống không đổi.",
  "giữ cho thể tích của cột khí trong ống luôn không đổi."),

 ("khí trong lốp nở ra làm lốp căng hơn nhưng áp suất giảm.",
  "khí trong lốp nở ra làm cho lốp căng hơn nhưng áp suất bên trong lại giảm đi."),

 ("thể tích hai ngăn bằng nhau, còn áp suất có thể khác nhau.",
  "thể tích hai ngăn bằng nhau, còn áp suất và nhiệt độ thì có thể khác nhau."),

 ("không thể thực hiện được vì cả p và V đều thay đổi.",
  "không thể thực hiện được vì cả áp suất lẫn thể tích đều thay đổi cùng lúc."),

 ("Vì nhiệt độ trong chai cao hơn bên ngoài nên khí dãn nở.",
  "Vì nhiệt độ của chất lỏng trong chai cao hơn nhiệt độ bên ngoài nên khí hoà tan "
  "trong đó dãn nở và thoát ra."),
 ("Vì thể tích chai tăng lên khi mở nút.",
  "Vì thể tích phần chứa khí trong chai tăng lên đột ngột ngay khi nút chai được mở ra."),
 ("Vì khí quyển tràn vào chai làm áp suất trong chai tăng.",
  "Vì không khí bên ngoài tràn vào chai làm áp suất phía trên mặt chất lỏng trong chai "
  "tăng lên."),

 ("Cả kết luận và lí do đều đúng.",
  "Cả kết luận lẫn lí do mà học sinh đó đưa ra đều hoàn toàn chính xác."),
 ("Kết luận sai vì nén đẳng nhiệt làm áp suất giảm.",
  "Kết luận sai, vì nén một lượng khí ở nhiệt độ không đổi thì áp suất của nó giảm đi "
  "chứ không tăng lên."),
 ("Kết luận đúng và lí do đúng, nhưng còn thiếu vai trò của lực hút phân tử.",
  "Kết luận đúng và lí do cũng đúng, nhưng lập luận còn thiếu vai trò của lực hút giữa "
  "các phân tử khí."),

 ("ba đoạn thẳng đều đi qua gốc toạ độ.",
  "ba đoạn thẳng và cả ba đều đi qua gốc toạ độ."),
 ("một đoạn nằm ngang, một hypebol và một đoạn thẳng đứng.",
  "một đoạn nằm ngang, một nhánh hypebol và một đoạn thẳng đứng."),
 ("một hypebol và hai đoạn thẳng nằm ngang.",
  "một nhánh hypebol và hai đoạn thẳng nằm ngang song song."),

 ("Cả hai vế đều đúng hoàn toàn.",
  "Cả hai vế của lập luận đó đều hoàn toàn chính xác về mặt vật lí."),
 ("Vế đầu sai vì ở 0 K phân tử vẫn chuyển động rất nhanh.",
  "Vế đầu sai, vì ngay cả ở 0 K thì các phân tử khí vẫn tiếp tục chuyển động nhiệt "
  "rất nhanh."),
 ("Cả hai vế đều sai vì công thức v_rms không áp dụng được cho khí thực.",
  "Cả hai vế đều sai, vì công thức tính tốc độ căn quân phương không áp dụng được cho "
  "bất kì khí thực nào."),

 ("tăng lên vì thể tích bóng tăng.",
  "tăng lên đáng kể vì thể tích của quả bóng tăng dần theo độ cao."),
 ("giảm đi vì khối lượng riêng không khí giảm.",
  "giảm đi vì khối lượng riêng của không khí xung quanh giảm dần theo độ cao."),
 ("giảm về 0 ngay khi bóng vượt qua tầng đối lưu.",
  "giảm dần về 0 ngay khi quả bóng vượt qua ranh giới của tầng đối lưu."),

 ("trên thực tế tất cả các phân tử đều chuyển động với cùng một tốc độ.",
  "trên thực tế tất cả các phân tử trong khối khí đều chuyển động với cùng một tốc độ "
  "như nhau."),
 ("các phân tử nhanh và chậm luôn triệt tiêu tác dụng của nhau.",
  "tác dụng của các phân tử chuyển động nhanh và của các phân tử chậm luôn triệt tiêu "
  "lẫn nhau."),
 ("chỉ những phân tử có tốc độ đúng bằng v_rms mới va chạm với thành bình.",
  "chỉ những phân tử có tốc độ đúng bằng v_rms mới thực sự va chạm được với thành bình."),
],

"combined_calc12.py": [
 ("Nội năng khí tăng vì thể tích tăng.",
  "Nội năng của khí tăng lên vì thể tích của nó đã tăng gấp đôi."),
 ("Nội năng khí giảm vì khí sinh công.",
  "Nội năng của khí giảm đi vì khí đã sinh công đẩy pit-tông."),
 ("Khí không trao đổi nhiệt với môi trường.",
  "Khí hoàn toàn không trao đổi nhiệt lượng nào với môi trường."),
],
}

fail = 0
for fname, pairs in PATCHES.items():
    path = "src3/" + fname
    s = io.open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old not in s:
            print("KHÔNG TÌM THẤY trong %s: %r" % (fname, old[:70]))
            fail += 1
            continue
        s = s.replace(old, new, 1)
    io.open(path, "w", encoding="utf-8").write(s)
    print("Đã vá:", fname, "-", len(pairs), "phương án")

sys.exit(1 if fail else 0)
