# Tuyển tập bài tập VẬN DỤNG CAO — Vật lí 12

Hai bộ đề độc lập gồm **80 câu hỏi gốc** ở mức vận dụng và vận dụng cao, biên soạn theo
Chương trình GDPT 2018 và cấu trúc đề thi tốt nghiệp THPT từ 2025, hướng tới kì thi
tốt nghiệp THPT và đánh giá năng lực **2026 – 2027**.

> Thư mục này hoàn toàn độc lập với các tài liệu khác trong kho; nó không dùng chung và
> không sửa đổi bất kì tệp nào bên ngoài `elite/`.

## Sản phẩm

| Tệp | Nội dung |
|---|---|
| `BO1_DE_BAI_VAN_DUNG_CAO_CHUONG_1_VA_2.docx` | Đề bài — Chương I (Vật lí nhiệt) + Chương II (Khí lí tưởng) |
| `BO1_LOI_GIAI_CHI_TIET_CHUONG_1_VA_2.docx` | Đáp án và lời giải chi tiết cho bộ 1 |
| `BO2_DE_BAI_VAN_DUNG_CAO_CHUONG_3_VA_4.docx` | Đề bài — Chương III (Từ trường) + Chương IV (Vật lí hạt nhân) |
| `BO2_LOI_GIAI_CHI_TIET_CHUONG_3_VA_4.docx` | Đáp án và lời giải chi tiết cho bộ 2 |

Mỗi bộ gồm 40 câu, chia theo đúng ba phần của đề thi:

* **Phần I** – 18 câu trắc nghiệm nhiều phương án lựa chọn
* **Phần II** – 10 câu trắc nghiệm đúng/sai (40 ý)
* **Phần III** – 12 câu trắc nghiệm trả lời ngắn

Mã số câu (`Câu I.1`, `Câu II.3`, `Câu III.7`, …) trùng khớp tuyệt đối giữa tệp đề bài và
tệp lời giải tương ứng.

## Nguyên tắc biên soạn

* **Khó vì tư duy vật lí, không khó vì số học.** Mọi công cụ toán học đều nằm trong chương
  trình phổ thông: tam thức bậc hai, logarit, lượng giác cơ bản. Không dùng giải tích,
  phương trình vi phân hay kiến thức đại học. Khi một bài cần công thức nằm ngoài phần
  bắt buộc (ví dụ nội năng khí lí tưởng đơn nguyên tử `U = (3/2)nRT`), công thức đó được
  cho ngay trong đề.
* **Điều kiện ẩn và bẫy khái niệm.** Nhiều câu chỉ giải đúng nếu học sinh phát hiện được
  một ràng buộc không được nói ra: thuỷ ngân tràn khỏi ống, nước đá chỉ nóng chảy một
  phần, pit-tông chạm vấu chặn giữa chừng, pit-tông tự do không đồng nghĩa với đẳng áp,
  khung dây nằm trọn trong vùng từ trường thì không có dòng cảm ứng.
* **Phương án nhiễu có nguồn gốc.** Mỗi phương án sai được dựng từ một sai lầm cụ thể và
  được giải thích trong lời giải, nên có thể dùng để chẩn đoán lỗ hổng kiến thức.
* **Chống đoán mò.** Đáp án Phần I được phân bố đều giữa A–D; ở Phần II, số ý sai thay
  đổi giữa các câu (1 hoặc 2 ý) và vị trí ý sai trải đều trên cả bốn vị trí a)–d).
* **Hình vẽ gốc.** 33 hình (đồ thị, sơ đồ thí nghiệm, giản đồ) đều được sinh bằng
  matplotlib và nhúng trực tiếp vào tệp Word, không dùng liên kết ngoài.

## Mã nguồn

```
src/figbase.py       tiện ích vẽ hình dùng chung
src/figs_b1.py       17 hình cho bộ 1        →  figs/b1_*.png
src/figs_b2.py       16 hình cho bộ 2        →  figs/b2_*.png
src/book1.py         toàn bộ nội dung bộ 1 (P1, P2, P3)
src/book2.py         toàn bộ nội dung bộ 2 (P1, P2, P3)
src/build_elite.py   sinh 4 tệp .docx, cân bằng vị trí đáp án
src/qc.py            kiểm tra chất lượng: cấu trúc + TÍNH LẠI ĐỘC LẬP mọi con số
src/verify_docx.py   kiểm tra lại chính các tệp .docx đã sinh
```

### Dựng lại toàn bộ

```bash
cd src
python3 figs_b1.py && python3 figs_b2.py   # sinh 33 hình
python3 qc.py                              # 176 phép kiểm tra số liệu
python3 build_elite.py                     # sinh 4 tệp .docx
python3 verify_docx.py                     # đối chiếu lại các tệp đã sinh
```

Yêu cầu: `python-docx`, `matplotlib`, `Pillow`.

## Kiểm soát chất lượng

`qc.py` tính lại độc lập **176 giá trị** — không đọc lại con số trong lời giải mà dựng
lại từ dữ kiện đề bài — và đối chiếu với những gì đề, đáp án, lời giải đang ghi. Nó cũng
kiểm tra:

* mỗi câu Phần I có đúng 4 phương án phân biệt và một đáp án hợp lệ;
* mỗi câu Phần II có đúng 4 ý, mỗi ý có nhãn đúng/sai và lời giải thích riêng;
* mọi hình được tham chiếu đều tồn tại, mọi bảng số liệu đều khớp số cột;
* không có cặp câu nào trùng lặp quá 82% nội dung.

Ngoài các giá trị đúng, `qc.py` còn kiểm tra cả các **giá trị bẫy** (ví dụ 0,199 kg khi
quên hiệu suất; 0,2 A khi quên nhân số vòng dây; 3,13 MeV khi cộng trừ trực tiếp năng
lượng liên kết riêng) để bảo đảm mỗi phương án nhiễu thật sự tương ứng với một sai lầm
xác định chứ không phải một con số tuỳ tiện.

`verify_docx.py` mở lại bốn tệp `.docx` đã sinh và đối chiếu: danh sách mã câu giữa đề
bài và lời giải, từng dòng “Đáp án:” so với dữ liệu nguồn, số hình nhúng và số bảng.
