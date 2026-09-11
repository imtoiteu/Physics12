# Physics2026 — Bộ tài liệu dạy ôn thi tốt nghiệp THPT 2026, môn Vật lí

Tài liệu hoàn chỉnh cho **bốn chương đầu của Vật lí 12** (Chương trình GDPT 2018), biên soạn
theo đúng **cấu trúc định dạng đề thi tốt nghiệp THPT từ năm 2025**: 28 câu hỏi / 40 lệnh hỏi /
50 phút / 10 điểm.

| Phần | Sản phẩm | Quy mô |
|---|---|---|
| Bài giảng | 21 tệp `.pptx` | 233 slide, 98 lượt nhúng hình |
| Luyện tập theo chương | 8 tệp `.docx` | 40 đề × 28 câu = **1120 câu** |
| Thi thử tổng hợp | 72 tệp `.docx` | 30 đề × 28 câu = **840 câu** |
| Hình vẽ gốc | 88 tệp `.png` | sinh bằng matplotlib, nhúng trực tiếp |

Tổng cộng **1960 câu hỏi**, mỗi câu đều có đáp án, lời giải chi tiết, mức độ
(Dễ / Trung bình / Khó / Rất khó) và kiến thức – kĩ năng được kiểm tra.

---

## 1. Cấu trúc thư mục

```
Physics2026/
├── Slides/
│   ├── 00_Dinh_huong_ky_thi_tot_nghiep_THPT_2026.pptx
│   ├── Chuong01/   C01_Buoi1 … C01_Buoi5      (Vật lí nhiệt)
│   ├── Chuong02/   C02_Buoi1 … C02_Buoi5      (Khí lí tưởng)
│   ├── Chuong03/   C03_Buoi1 … C03_Buoi5      (Từ trường)
│   └── Chuong04/   C04_Buoi1 … C04_Buoi5      (Vật lí hạt nhân)
├── BaiTapTheoChuong/
│   ├── Chuong01/   CHUONG1_VAT_LI_NHIET_10_DE_LUYEN_TAP.docx
│   │               CHUONG1_VAT_LI_NHIET_10_DE_LOI_GIAI_CHI_TIET.docx
│   ├── Chuong02/   … KHI_LI_TUONG …
│   ├── Chuong03/   … TU_TRUONG …
│   └── Chuong04/   … VAT_LI_HAT_NHAN …
├── DeThiTongHop/
│   ├── De01/       DE01_DE_THI.docx  +  DE01_DAP_AN_VA_LOI_GIAI.docx
│   ├── …
│   ├── De30/
│   └── TronBo/     6 tập gộp, mỗi tập 5 đề (tiện in hàng loạt)
├── figs/           88 hình minh hoạ (.png)
├── formulas/       ảnh công thức đã kết xuất (bộ nhớ đệm)
└── src/            toàn bộ mã nguồn sinh tài liệu
```

---

## 2. Bộ slide bài giảng (21 buổi dạy)

Mỗi chương được chia thành **5 buổi dạy thực tế**, mỗi buổi một tệp `.pptx` riêng, cộng thêm
một tệp mở đầu về định hướng kì thi.

| Chương | Buổi 1 | Buổi 2 | Buổi 3 | Buổi 4 | Buổi 5 |
|---|---|---|---|---|---|
| I. Vật lí nhiệt | Cấu trúc của chất, sự chuyển thể | Nội năng, định luật I | Thang nhiệt độ, nhiệt kế | Nhiệt dung riêng, nóng chảy, hoá hơi | Luyện tập tổng hợp |
| II. Khí lí tưởng | Mô hình động học phân tử | Ba định luật chất khí | Phương trình trạng thái, Clapeyron | Áp suất và động năng phân tử | Luyện tập tổng hợp |
| III. Từ trường | Từ trường, đường sức từ | Lực từ, cảm ứng từ | Từ thông, cảm ứng điện từ | Đại cương dòng điện xoay chiều | Luyện tập và ứng dụng |
| IV. Vật lí hạt nhân | Cấu trúc hạt nhân, năng lượng liên kết | Phóng xạ, định luật phóng xạ | Phản ứng hạt nhân, phân hạch, nhiệt hạch | Ứng dụng và an toàn phóng xạ | Luyện tập tổng hợp |

Mỗi buổi dạy đi theo mạch: **slide mở đầu → các mục kiến thức → hình minh hoạ/mô phỏng →
bảng công thức → ví dụ có lời giải từng bước → câu hỏi kiểm tra nhanh → tổng kết và bài về nhà.**
Một số slide có **ghi chú cho giáo viên** (phần Notes của PowerPoint).

### Cách hiển thị công thức — không có LaTeX thô, không lỗi font

Hai quy ước được áp dụng nhất quán và được máy kiểm tra tự động:

1. **Kí hiệu nằm trong dòng chữ** dùng trực tiếp Unicode: `Δ`, `λ`, `μ`, `ω`, `°C`, `·10⁵`,
   `Nₐ`, `2⁻ⁿ`, `⁴He`. Không bao giờ viết kiểu mã nguồn như `c_đá`, `N_A`, `2^(-t/T)`.
2. **Công thức hai chiều** (phân số, căn, chỉ số phức tạp) được kết xuất thành **ảnh PNG
   420 dpi nền trong suốt** bằng bộ chữ toán học **STIX** rồi nhúng vào slide, nên hiển thị
   giống hệt nhau trên mọi máy, không phụ thuộc phông chữ cài sẵn.

`src/formula.py` chặn mọi công thức chứa kí tự ngoài ASCII: phần chữ tiếng Việt luôn nằm
ngoài ảnh công thức, nhờ vậy không bao giờ xuất hiện ô vuông thay cho dấu tiếng Việt.

### Chống tràn chữ

`src/deck.py` đo bề rộng thật của từng dòng bằng `PIL.ImageFont` với phông
**Liberation Sans** (tương thích số đo với Arial), tự động ngắt dòng, tự phóng to hoặc thu nhỏ
cỡ chữ cho vừa khung và căn giữa theo chiều dọc. Slide nào còn nguy cơ tràn sẽ được báo ngay
khi dựng.

### Đã mở lại và kiểm tra

* `src/slides_qc.py` đọc lại toàn bộ 21 tệp `.pptx`, quét từng ô chữ để phát hiện dấu gạch dưới
  kiểu `X_y`, dấu mũ kiểu `^2` và mã LaTeX còn sót (`\frac`, `$`). Kết quả cuối cùng:
  **21 tệp, 233 slide, 98 ảnh nhúng, 13 bảng — không phát hiện lỗi kí hiệu, lỗi font hay mã
  LaTeX thô.**
* `src/preview.py` chuyển `.pptx` → PDF → PNG (LibreOffice headless + `pdftoppm`) để xem lại
  từng trang bằng mắt, đúng như khi mở bằng PowerPoint.

---

## 3. Bộ đề luyện tập theo chương (40 đề, 1120 câu)

Mỗi chương có **10 đề**, mỗi đề đúng cấu trúc thi thật: **18 câu trắc nghiệm nhiều lựa chọn +
4 câu đúng/sai (16 ý) + 6 câu trả lời ngắn**.

Độ khó tăng dần trong từng bộ 10 đề:

| Đề | Mức độ |
|---|---|
| 01 – 02 | Dễ — kiểm tra nhận biết, làm quen cấu trúc |
| 03 – 05 | Trung bình — thông hiểu, tính toán một bước |
| 06 – 08 | Khá — vận dụng nhiều bước, đọc đồ thị, bảng số liệu |
| 09 – 10 | Khó / phân loại học sinh giỏi |

Mỗi tệp lời giải có: bảng đáp án nhanh, bảng thống kê mức độ, và với **từng câu** là mức độ,
kiến thức – kĩ năng được kiểm tra, lời giải chi tiết theo từng bước cùng phân tích phương pháp.
Với câu đúng/sai, **mỗi ý được giải thích riêng** vì sao đúng hoặc vì sao sai.

---

## 4. Bộ 30 đề thi thử tổng hợp (840 câu)

Cả 30 đề đều trộn kiến thức **cả bốn chương**, độ khó tăng dần:

| Đề | Mức độ | Tệp nguồn |
|---|---|---|
| 01 – 05 | Dễ → Trung bình | `src/de_th1.py` |
| 06 – 10 | Trung bình | `src/de_th2.py` |
| 11 – 15 | Trung bình → Khó | `src/de_th3.py` |
| 16 – 20 | Khó | `src/de_th4.py` |
| 21 – 25 | Khó | `src/de_th5.py` |
| 26 – 30 | Khó – phân loại học sinh giỏi | `src/de_th6.py` |

Toàn bộ câu hỏi là **nguyên bản**, không sao chép nguyên văn từ bất kì nguồn nào; chỉ bám theo
định dạng và tinh thần của đề tham khảo Bộ GD&ĐT. Dạng bài được đa dạng hoá có chủ ý: tính toán
nhiều giai đoạn, đọc đồ thị, đọc bảng số liệu, phân tích thí nghiệm, bài toán thực tiễn
(bếp từ, truyền tải điện, lò phản ứng, định tuổi bằng C-14), câu bẫy điều kiện ẩn
(thuỷ ngân tràn khỏi ống, nước đá chỉ tan một phần, khung dây nằm trọn trong từ trường).

Mỗi đề nằm trong thư mục riêng `De01 … De30` gồm hai tệp: **đề thi** và **đáp án + lời giải
chi tiết** (kèm ma trận độ khó và bảng thống kê mức độ của chính đề đó).

---

## 5. Kiểm soát chất lượng

Ba tầng kiểm tra độc lập, chạy lại được bất cứ lúc nào:

| Công cụ | Kiểm tra |
|---|---|
| `src/qc.py` | Mỗi câu Phần I có 4 phương án **phân biệt** và đáp án hợp lệ; mỗi câu Phần II có đủ 4 ý kèm nhãn đúng/sai và lời giải thích riêng; **giá trị đáp án phải trùng với kết quả xuất hiện trong lời giải**; hình được tham chiếu phải tồn tại; bảng khớp số cột; không có cặp câu trùng nhau quá 88 %; không còn văn phong “tự sửa lời giải”. |
| `src/verify_docx.py` | **Mở lại 80 tệp `.docx` đã sinh**, đối chiếu số câu, thứ tự câu, nội dung đề bài, từng dòng “Đáp án:”, từng nhãn ĐÚNG/SAI, số hình nhúng và số bảng với dữ liệu nguồn. |
| `src/slides_qc.py` | Quét lại 21 tệp `.pptx`: kí hiệu, mã LaTeX thô, số slide, số ảnh, số bảng, ghi chú giáo viên. |

`qc.py` còn cảnh báo khi hai câu có nội dung giống nhau quá 88 %. Mọi trường hợp câu hỏi lặp
lại trong CÙNG một đề (câu Phần III hỏi lại đúng câu Phần I, hoặc một ý đúng/sai nêu sẵn đáp án
của câu trắc nghiệm) đều đã được viết lại. Chín cảnh báo còn lại là các câu **ở những đề khác
nhau** cùng kiểm tra một kĩ năng nhưng khác dữ kiện (ví dụ đọc đồ thị nóng chảy của chì ở đề này
và của chất X ở đề khác) — đây là chủ ý luyện tập lặp có giãn cách, không phải trùng lặp.

Vị trí đáp án A–D được **phân bố lại tự động** (`build.rebalance_group`) để chống đoán mò:
với bộ phương án là dãy số đã sắp thứ tự thì chỉ đảo chiều (giữ tính dễ đọc), với các bộ khác
thì hoán vị tự do. Kết quả: 30 đề thi thử có phân bố **A 150 / B 150 / C 120 / D 120**.

---

## 6. Dựng lại toàn bộ tài liệu

```bash
cd src

python3 figs_extra.py && python3 figs_tu.py \
  && python3 figs_hn.py && python3 figs_base_th.py   # 88 hình vào figs/

python3 make_slides.py        # 21 tệp .pptx vào Slides/
python3 slides_qc.py          # kiểm tra lại slide

python3 qc.py de_12c1 de_12c2 de_12c3 de_12c4 \
              de_th1 de_th2 de_th3 de_th4 de_th5 de_th6

python3 make_de.py            # 8 tệp .docx vào BaiTapTheoChuong/
python3 make_th.py            # 72 tệp .docx vào DeThiTongHop/
python3 verify_docx.py        # mở lại và đối chiếu mọi tệp .docx
```

Yêu cầu: `python-pptx`, `python-docx`, `matplotlib`, `Pillow`.
Riêng `preview.py` cần thêm LibreOffice và `pdftoppm` (gói `poppler-utils`).

### Bản đồ mã nguồn

```
src/formula.py        kết xuất công thức LaTeX → ảnh PNG (STIX, 420 dpi, có bộ nhớ đệm)
src/deck.py           bộ dựng slide: bố cục, đo chữ, tự co giãn cỡ chữ, 11 kiểu slide
src/slides_00.py      slide định hướng kì thi
src/slides_c1..c4.py  nội dung slide của bốn chương
src/make_slides.py    dựng toàn bộ 21 tệp .pptx
src/preview.py        .pptx → PDF → PNG để xem lại bằng mắt

src/figbase.py        tiện ích vẽ hình dùng chung
src/figgen.py         các khối hình cơ bản (xilanh, lò xo, nhiệt kế, đồ thị…)
src/figs_extra.py     12 hình Chương I – II
src/figs_tu.py        15 hình Chương III
src/figs_hn.py        12 hình Chương IV
src/figs_base_th.py   16 hình dùng lại cho Chương III – IV

src/qbase.py          hàm dựng câu hỏi: mc() / ds() / sa()
src/build.py          bộ dựng .docx: bìa, ma trận, bảng đáp án, cân bằng vị trí đáp án
src/de_12c1..c4.py    ngân hàng 40 đề luyện tập theo chương
src/de_th1..th6.py    ngân hàng 30 đề thi thử tổng hợp
src/make_de.py        dựng đề luyện tập theo chương
src/make_th.py        dựng 30 đề thi thử
src/qc.py             kiểm tra chất lượng câu hỏi
src/verify_docx.py    đối chiếu lại các tệp .docx đã sinh
```
