# -*- coding: utf-8 -*-
"""Kiểm tra ĐỘC LẬP toàn bộ số liệu định lượng trong 10 đề kiểm tra.

Mỗi phép kiểm tra ở đây được tính lại từ đầu bằng Python, hoàn toàn không đọc kết quả
đã ghi trong tệp đề. Nếu một con số nào đó trong đề bị sai thì phép kiểm tra tương ứng
sẽ báo LỖI.
"""
from math import sqrt

CW, CI, CAL, CFE, CCU, CPB = 4200.0, 2100.0, 880.0, 460.0, 380.0, 130.0
LAM, LV = 3.34e5, 2.26e6
R, KB, NA = 8.31, 1.38e-23, 6.02e23

OK, BAD = [], []


def chk(label, got, want, tol=0.012):
    """So sánh tương đối; tol là sai số tương đối cho phép (mặc định 1,2 %)."""
    if want == 0:
        good = abs(got) < 1e-9
    else:
        good = abs(got - want) / abs(want) <= tol
    (OK if good else BAD).append((label, got, want))


def mix2(m1, c1, t1, m2, c2, t2):
    """Nhiệt độ cân bằng của hai vật trao đổi nhiệt, không chuyển thể."""
    return (m1 * c1 * t1 + m2 * c2 * t2) / (m1 * c1 + m2 * c2)


# ======================================================= CHƯƠNG I – ĐỀ 01
chk("C1-01 MC13 Q đun 2 kg nước 25→75", 2.0 * CW * 50 / 1000, 420)
chk("C1-01 MC14 nóng chảy 0,5 kg đá", 0.5 * LAM, 1.67e5)
chk("C1-01 MC15 ΔU = A + Q", -120 + 200, 80)
chk("C1-01 MC16 trộn 2 khối nước bằng nhau", mix2(0.5, CW, 20, 0.5, CW, 80), 50)
chk("C1-01 MC18 hoá hơi 0,2 kg nước", 0.2 * LV, 4.52e5)
chk("C1-01 MC12 ΔT theo Kelvin", 57 - 27, 30)
chk("C1-01 ĐS2b Q nước thu", 0.300 * CW * 5.0, 6300)
chk("C1-01 ĐS2c c kim loại", 6300 / (0.200 * 70.0), 450)
chk("C1-01 P3.1 ấm nhôm + nước", (0.40 * CAL + 1.5 * CW) * 80 / 1000, 532.16)
chk("C1-01 P3.2 c kim loại", (0.400 * CW * 10) / (0.500 * 88), 381.8)
# 300 g đá 0 °C + 1,0 kg nước 60 °C
_t = (1.0 * CW * 60 - 0.300 * LAM) / (1.0 * CW + 0.300 * CW)
chk("C1-01 P3.3 nhiệt độ cân bằng", _t, 27.80)
chk("C1-01 P3.4 thời gian đun (phút)", (1.5 * CW * 75 / 0.70) / 800 / 60, 14.06)
chk("C1-01 P3.5 đá −10 °C → nước 20 °C",
    (0.200 * CI * 10 + 0.200 * LAM + 0.200 * CW * 20) / 1000, 87.8)
chk("C1-01 P3.6 ΔU tổng", (750 - 480) + (260 - 190), 340)

# ======================================================= CHƯƠNG I – ĐỀ 02
chk("C1-02 MC13 tỉ số c_X/c_Y", 84.0 / 33.6, 2.5)
chk("C1-02 MC13' c_X từ đồ thị", 84000 / (1.0 * 40), 2100)
chk("C1-02 MC13'' c_Y từ đồ thị", 33600 / (1.0 * 40), 840)
chk("C1-02 MC14 ngưng tụ 0,8 kg hơi", 0.80 * LV, 1.808e6)
chk("C1-02 MC15 trộn 2 + 3 kg nước", mix2(2.0, CW, 90, 3.0, CW, 20), 48)
chk("C1-02 MC16 Δt thanh sắt", 92000 / (2.0 * CFE), 100)
chk("C1-02 MC17 đá 0 °C → nước 20 °C",
    (0.250 * LAM + 0.250 * CW * 20) / 1000, 104.5)
chk("C1-02 ĐS2b Q điện trở 8 phút", 40 * 480, 19200)
chk("C1-02 ĐS2c λ thực nghiệm", 19200 / 0.056, 3.43e5)
chk("C1-02 ĐS4a nhiệt tan 100 g đá", 0.100 * LAM / 1000, 33.4)
chk("C1-02 ĐS4b Q toả tối đa 500 g nước", 0.500 * CW * 30 / 1000, 63.0)
_t = (0.500 * CW * 30 - 0.100 * LAM) / (0.500 * CW + 0.100 * CW)
chk("C1-02 ĐS4c nhiệt độ cân bằng", _t, 11.746)
chk("C1-02 ĐS4d thay đá bằng nước 0 °C", mix2(0.5, CW, 30, 0.1, CW, 0), 25.0)
chk("C1-02 P3.1 Q đun 3 kg nước", 3.0 * CW * 60 / 1000, 756)
chk("C1-02 P3.2 đồng 150 °C + nước", mix2(0.800, CCU, 150, 1.2, CW, 25), 32.11)
chk("C1-02 P3.3 hiệu suất ấm (%)", 100 * (1.8 * CW * 80) / (1200 * 540), 93.33)
chk("C1-02 P3.4 khối lượng đá (g)",
    1000 * (0.500 * CW * 30) / (LAM + CW * 5), 177.46)
chk("C1-02 P3.5 Q khí nhận", -120 - (-350), 230)
chk("C1-02 P3.6 ngưng tụ + nguội",
    (0.400 * LV + 0.400 * CW * 60) / 1000, 1004.8)

# ======================================================= CHƯƠNG I – ĐỀ 03
chk("C1-03 MC13 c rắn từ đồ thị", 32500 / (0.50 * 50), 1300)
chk("C1-03 MC14 λ từ đồ thị", (137.5 - 32.5) * 1000 / 0.50, 2.1e5)
chk("C1-03 MC15 c của vật A", (2.0 * CW * 14) / (1.0 * 56), 2100)
# 200 g đá −5 °C + 800 g nước 45 °C
_qtoa = 0.800 * CW * 45
_qcan = 0.200 * CI * 5 + 0.200 * LAM
chk("C1-03 MC16 kiểm tra đá tan hết", 1.0 if _qtoa > _qcan else 0.0, 1.0)
_t = (_qtoa - _qcan) / (0.800 * CW + 0.200 * CW)
chk("C1-03 MC16 nhiệt độ cân bằng", _t, 19.595)
chk("C1-03 MC17 sắt 300 °C + nước", mix2(1.5, CFE, 300, 2.0, CW, 20), 41.25)
chk("C1-03 MC18 c chất lỏng", 30000 / (0.500 * 24), 2500)
chk("C1-03 ĐS1d c lỏng từ đồ thị", (190 - 137.5) * 1000 / (0.50 * 40), 2625)
chk("C1-03 ĐS2c Q vật B thu", 2.0 * CW * 14 / 1000, 117.6)
chk("C1-03 ĐS3a ΔU = 150 + 400", 150 + 400, 550)
chk("C1-03 ĐS3b ΔU = 250 − 90", 250 - 90, 160)
chk("C1-03 P3.1 thời gian nóng chảy (phút)", 105000 / 500 / 60, 3.5)
# chì 300 g 98 °C + 250 g nước 24 °C + nhiệt lượng kế 80 J/K
_t = (0.300 * CPB * 98 + (0.250 * CW + 80) * 24) / (0.300 * CPB + 0.250 * CW + 80)
chk("C1-03 P3.2 nhiệt độ cân bằng", _t, 26.469)
chk("C1-03 P3.3 khối lượng nước (g)", 1000 * 3.0e5 / (LAM + CI * 8), 855.2)
chk("C1-03 P3.4 thời gian đun sôi (phút)", (2.5 * CW * 70) / 700 / 60, 17.5)
chk("C1-03 P3.5 ΔU tổng", (600 - 250) + (-400), -50)
chk("C1-03 P3.6 nước 95 °C + bình nhôm", mix2(1.2, CW, 95, 0.500, CAL, 25), 89.38)

# ======================================================= CHƯƠNG I – ĐỀ 04
chk("C1-04 MC10 c mẫu I", 250 * 360 / (0.50 * 60), 3000)
chk("C1-04 MC11 tỉ số c_II/c_I", 10.0 / 6.0, 1.667)
_P = LAM * 0.400 / 600
chk("C1-04 MC12 công suất bếp", _P, 222.67)
chk("C1-04 MC13 thời gian đun bình (phút)",
    (5.0 * CW * 48) / (0.85 * 1500) / 60, 13.18)
chk("C1-04 MC14 trộn ba lượng nước",
    (1.0 * 20 + 2.0 * 40 + 3.0 * 70) / 6.0, 51.667)
# 500 g đá −10 °C + 500 g nước 20 °C
_du = 0.500 * CW * 20 - 0.500 * CI * 10
chk("C1-04 MC15 đá còn lại (g)", 1000 * (0.500 - _du / LAM), 405.7)
chk("C1-04 MC16 Q toả tối đa của hệ", (0.150 * CCU + 0.250 * CW) * 20, 22140)
chk("C1-04 MC16' Q cần tan hết đá", 0.100 * LAM, 33400)
# 50 g hơi 100 °C + 1 kg nước 20 °C
_t = (0.050 * LV + 0.050 * CW * 100 + 1.0 * CW * 20) / (0.050 * CW + 1.0 * CW)
chk("C1-04 MC17 nhiệt độ cân bằng", _t, 49.43)
chk("C1-04 MC18 Q sau 7 phút", 800 * 420, 336000)
chk("C1-04 MC18' Q để sôi", 1.0 * CW * 75, 315000)
chk("C1-04 ĐS1c c mẫu II", 250 * 600 / (0.50 * 60), 5000)
chk("C1-04 ĐS1d Δt sau 4 phút", 250 * 240 / (0.50 * 3000), 40)
chk("C1-04 ĐS2b công suất bếp", _P, 222.67)
chk("C1-04 ĐS2d tốc độ tăng nhiệt (°C/phút)", _P * 60 / (0.400 * CW), 7.95)
chk("C1-04 ĐS3a Q dây đốt 10 phút (kJ)", 1500 * 600 / 1000, 900)
chk("C1-04 ĐS3b Q cho nước (kJ)", 5.0 * CW * 48 / 1000, 1008)
_t1 = (5.0 * CW * 48) / (0.85 * 1500) / 60
_t2 = (5.0 * CW * 48) / (0.95 * 1500) / 60
chk("C1-04 ĐS3d độ giảm thời gian (phút)", _t1 - _t2, 1.39, tol=0.03)
chk("C1-04 ĐS4a hâm 400 g đá −8 °C lên 0 °C (kJ)", 0.400 * CI * 8 / 1000, 6.72)
chk("C1-04 ĐS4a' bẫy dùng nhầm c nước (kJ)", 0.400 * CW * 8 / 1000, 13.44)
chk("C1-04 ĐS4b Q toả tối đa (kJ)", 0.600 * CW * 25 / 1000, 63.0)
chk("C1-04 ĐS4c Q cần tan hết 400 g đá (kJ)", 0.400 * LAM / 1000, 133.6)
_du4 = 0.600 * CW * 25 - 0.400 * CI * 8
chk("C1-04 ĐS4d đá còn lại (g)", 1000 * (0.400 - _du4 / LAM), 231.5)
chk("C1-04 P3.1 thời gian đun tới 50 °C (phút)", (0.400 * CW * 50) / _P / 60, 6.29)
chk("C1-04 P3.2 c kim loại",
    ((0.600 * CW + 120) * 15.0) / (0.400 * 215.0), 460.5)
chk("C1-04 P3.3 khối lượng đá (kg)",
    (1.5 * CW * 40) / (LAM + CW * 40), 0.502)
_t = (0.800 * CW * 15 + 0.300 * CAL * 100 + 0.500 * CCU * 80) \
     / (0.800 * CW + 0.300 * CAL + 0.500 * CCU)
chk("C1-04 P3.4 nhiệt độ cân bằng ba vật", _t, 24.12)
chk("C1-04 P3.5 công khí thực hiện", 1200 - 450, 750)
chk("C1-04 P3.6 khối lượng hơi (g)",
    1000 * (900 * 540 - 1.2 * CW * 70) / LV, 58.94)

# ======================================================= CHƯƠNG I – ĐỀ 05
chk("C1-05 MC9 chênh lệch nhiệt độ nước/dầu",
    42000 / 2000 - 42000 / CW, 11)
chk("C1-05 MC10 λ từ đồ thị", (84 - 24) * 1000 / 1.0, 6.0e4)
chk("C1-05 MC11 c lỏng từ đồ thị", (156 - 84) * 1000 / (1.0 * 30), 2400)
_Qlo = 900 * 240 + 500 * 360 + 300 * 360
chk("C1-05 MC12 tổng nhiệt lò (kJ)", _Qlo / 1000, 504)
# 200 g đá −20 °C + 300 g nước 25 °C
_du = 0.300 * CW * 25 - 0.200 * CI * 20
chk("C1-05 MC13 đá còn lại (g)", 1000 * (0.200 - _du / LAM), 130.8)
_tB = (3.0 * 20 + 1.0 * 80) / 4.0
chk("C1-05 MC14 nhiệt độ bình B", _tB, 35.0)
chk("C1-05 MC14' nhiệt độ cuối bình A", (1.0 * 80 + 1.0 * _tB) / 2.0, 57.5)
chk("C1-05 MC15 m nước 90 °C", 10.0 * 21.0 / (21.0 + 49.0), 3.0)
chk("C1-05 MC16 Q nước toả", 1.0 * CW * 10, 42000)
chk("C1-05 MC16' Q hâm đá −40 → 0", 0.500 * CI * 40, 42000)
chk("C1-05 MC17 khối lượng nước bay hơi (g)", 1000 * 0.60 * _Qlo / LV, 133.8)
chk("C1-05 MC18 nhiệt độ cân bằng với dầu", (200.0 + 180.0) / 11.0, 34.545)
chk("C1-05 ĐS1a c rắn từ đồ thị", 24000 / (1.0 * 40), 600)
chk("C1-05 ĐS1d Q cho 2 kg (kJ)", 2 * 156, 312)
chk("C1-05 ĐS2b 6 phút cuối (kJ)", 300 * 360 / 1000, 108)
chk("C1-05 ĐS2b' 4 phút đầu (kJ)", 900 * 240 / 1000, 216)
chk("C1-05 ĐS2c trung bình mỗi phút (kJ)", _Qlo / 1000 / 16, 31.5)
chk("C1-05 ĐS2d công suất trung bình (W)", _Qlo / 960, 525)
chk("C1-05 ĐS3a hâm 200 g đá (kJ)", 0.200 * CI * 20 / 1000, 8.4)
chk("C1-05 ĐS3d khối lượng đá đã tan (g)", 1000 * _du / LAM, 69.2)
chk("C1-05 P3.1 Q cho 2,5 kg (kJ)", 2.5 * 156, 390)
_t = (0.600 * CCU * 120 + (1.0 * CW + 0.400 * CAL) * 20) \
     / (0.600 * CCU + 1.0 * CW + 0.400 * CAL)
chk("C1-05 P3.2 nhiệt độ cân bằng", _t, 24.77)
chk("C1-05 P3.3 khối lượng hơi (g)",
    1000 * (2.0 * CW * 45) / (LV + CW * 40), 155.7)
chk("C1-05 P3.4 số viên đá tối thiểu",
    int((0.400 * CW * 30) / (0.020 * LAM)) + 1, 8)
chk("C1-05 P3.5 Q₂ toả ra", 500 + (800 - 300), 1000)
chk("C1-05 P3.6 thời gian (phút)",
    (0.800 * CI * 15 + 0.800 * LAM + 0.800 * CW * 100 + 0.800 * LV) / 1000 / 60, 40.607)

# ======================================================= CHƯƠNG II – ĐỀ 01
chk("C2-01 MC9 pV trạng thái 1", 3 * 2, 6)
chk("C2-01 MC9' pV trạng thái 2", 1 * 6, 6)
chk("C2-01 MC13 nén đẳng nhiệt", 1.0 * 6.0 / 2.0, 3.0)
chk("C2-01 MC14 đẳng áp 300→360 K", 3.0 * 360 / 300, 3.6)
chk("C2-01 MC15 đẳng tích 300→400 K", 2.0 * 400 / 300, 2.667)
chk("C2-01 MC16 phương trình trạng thái", 5.0 * (1.0 / 2.0) * (360 / 300), 3.0)
chk("C2-01 MC17 thể tích mol (lít)", 1.0 * R * 273 / 1.0e5 * 1000, 22.69)
chk("C2-01 ĐS4b nén đẳng nhiệt", 1.0e5 * 4.0 / 1.0, 4.0e5)
chk("C2-01 ĐS4c đẳng tích 300→600 K", 1.0e5 * 600 / 300, 2.0e5)
chk("C2-01 ĐS4d đẳng áp 300→360 K", 4.0 * 360 / 300, 4.8)
chk("C2-01 P3.1 định luật Boyle", 1.5 * 8.0 / 3.0, 4.0)
chk("C2-01 P3.2 đẳng áp 293→353 K", 2.5 * 353 / 293, 3.0119)
chk("C2-01 P3.3 đẳng tích 300→450 K", 2.0 * 450 / 300, 3.0)
chk("C2-01 P3.4 V₂", 6.0 * (1.0 / 2.5) * (450 / 300), 3.6)
chk("C2-01 P3.5 số mol", 2.49e5 * 10e-3 / (R * 300), 0.9988)
chk("C2-01 P3.6 bóng thám không", 5.0 * (1.0 / 0.50) * (240 / 300), 8.0)

# ======================================================= CHƯƠNG II – ĐỀ 02
chk("C2-02 MC13 nhiệt độ cần (°C)", 300 * (2.0 / 1.5) - 273, 127)
chk("C2-02 MC14 p ở 150 °C", 1.00 * 423.15 / 273.15, 1.549)
chk("C2-02 MC15 p sau biến đổi", 2.0 * (3.0 / 1.0) * (400 / 300), 8.0)
chk("C2-02 MC16 p của 1 mol He", 1.0 * R * 300 / 8.31e-3, 3.0e5)
chk("C2-02 MC18 phần trăm khí thoát", 100 * (1 - 2.0 / 5.0), 60)
chk("C2-02 ĐS1c p ở 273 °C", 1.00 * 546.15 / 273.15, 1.9995)
chk("C2-02 ĐS3a p trong bình", 0.40 * R * 300 / 10e-3, 99720)
chk("C2-02 ĐS3b tỉ số p khi 300→327 K", 327.0 / 300.0, 1.09)
chk("C2-02 ĐS3c tỉ số p khi thêm mol", 0.60 / 0.40, 1.5)
chk("C2-02 ĐS3d số phân tử", 0.40 * NA, 2.408e23)
chk("C2-02 ĐS4a p ở 0 °C", 1.2e5 * 273 / 300, 1.092e5)
chk("C2-02 ĐS4b p khi bóp còn 1,5 L", 1.2e5 * 2.0 / 1.5, 1.6e5)
chk("C2-02 ĐS4c kiểm tra đẳng áp", (2.4 / 2.0) / (360.0 / 300.0), 1.0)
chk("C2-02 P3.1 số phân tử (10²² hạt)",
    (1.0e5 * 2.0e-3 / (R * 300)) * NA / 1e22, 4.83)
chk("C2-02 P3.2 áp suất ban đầu (10⁴ Pa)", (2.0 * 1.8e5 / 3.0) / 1e4, 12)
chk("C2-02 P3.3 nhiệt độ (°C)", 300 * (5.0 * 2.4) / (2.0 * 4.0) - 273, 177)
chk("C2-02 P3.4 khối lượng O₂ (g)", (4.0e5 * 5.0e-3 / (R * 300)) * 32, 25.7)
chk("C2-02 P3.5 phần trăm xả ra", 100 * (1 - 2.4 / 6.0), 60)
chk("C2-02 P3.6 chiều dài cột khí (cm)", 20.0 * 360 / 300, 24.0)

# ======================================================= CHƯƠNG II – ĐỀ 03
chk("C2-03 MC6 tỉ số T₃/T₁", (1.0 * 2.0) / (3.0 * 2.0), 1.0 / 3.0)
chk("C2-03 MC11 áp suất cột khí (cmHg)", 75 + 12, 87)
chk("C2-03 MC12 T₃ (K)", 600 * (1.0 * 2.0) / (3.0 * 2.0), 200)
chk("C2-03 MC13 áp suất chung (10⁵ Pa)",
    (15.0 * 20 + 1.0 * 8.0) / 28.0, 11.0)
chk("C2-03 MC14 p của 1 mol H₂", 1.0 * R * 300 / 10e-3, 2.493e5)
chk("C2-03 MC15 p cuối", (1.0e5 * 3.0 / 1.0) * 600 / 300, 6.0e5)
chk("C2-03 MC17 ℓ khi đầu kín ở trên (cm)", 75.0 * 20 / (75 - 10), 23.077)
chk("C2-03 MC18 p còn lại (10⁵ Pa)", 3.0 * 0.75 * (250.0 / 300.0), 1.875)
chk("C2-03 ĐS1c T₃ đẳng áp", 600 * 2.0 / 6.0, 200)
chk("C2-03 ĐS3c thể tích quy đổi (L)",
    (11.0 * 8.0 - 1.0 * 8.0) / 15.0, 5.333)
chk("C2-03 ĐS3d p ở 330 K (10⁵ Pa)", 11.0 * 330 / 300, 12.1)
chk("C2-03 ĐS4b p khi đun cả hai (10⁵ Pa)", 1.0 * 400 / 300, 1.333)
chk("C2-03 ĐS4c dịch chuyển pit-tông (cm)", 300.0 / 70.0, 4.286)
chk("C2-03 P3.1 p cuối (10⁵ Pa)", (1.0 * 5.0 / 2.0) * 200 / 300, 1.667)
chk("C2-03 P3.2 ℓ khi đầu kín ở dưới (cm)", 75.0 * 20 / (75 + 10), 17.647)
chk("C2-03 P3.3 p (10⁵ Pa)", 0.60 * R * 400 / 8.0e-3 / 1e5, 2.493)
chk("C2-03 P3.4 V₂ (lít)", 4.0 * (1.0 / 0.80) * (270 / 300), 4.5)
chk("C2-03 P3.5 p chung (10⁵ Pa)", 8.0 * 25 / 40, 5.0)
chk("C2-03 P3.6 nhiệt độ (K)", (2.0e5 * 6.0e-3) / (0.25 * R), 577.6)

# ======================================================= CHƯƠNG II – ĐỀ 04
chk("C2-04 MC5 hệ số góc pV", 3.0, 3.0)
chk("C2-04 MC8 v tăng khi T tăng 4 lần", sqrt(4.0), 2.0)
chk("C2-04 MC11 v_rms O₂ ở 300 K", sqrt(3 * R * 300 / 0.032), 483.4)
chk("C2-04 MC12 động năng trung bình 27 °C", 1.5 * KB * 300, 6.21e-21)
chk("C2-04 MC13 p của khí B", 1.0e5, 1.0e5)
chk("C2-04 MC14 dịch chuyển pit-tông (cm)", 160.0 / 64.0, 2.5)
chk("C2-04 MC15 U của 1 mol (kJ)", 1.5 * 1.0 * R * 300 / 1000, 3.7395)
chk("C2-04 MC16 p chung hai bình (10⁵ Pa)", (3.0 + 1.0) / 2.0, 2.0)
chk("C2-04 MC17 p khi V = 2,5 L", 3.0 / 2.5, 1.2)
chk("C2-04 MC18 nhiệt độ cần (°C)", 2 * 300 - 273, 327)
chk("C2-04 ĐS1c p khi V = 5 L", 3.0 / 5.0, 0.60)
chk("C2-04 ĐS2d tỉ số p_P/p_N", (600.0 / 4) / (300.0 / 4), 2.0)
chk("C2-04 ĐS4b v_rms N₂ ở 300 K", sqrt(3 * R * 300 / 0.028), 516.8)
chk("C2-04 ĐS4c tỉ số W̄ khi 300→400 K", 400.0 / 300.0, 1.333)
chk("C2-04 P3.1 v_rms He ở 300 K", sqrt(3 * R * 300 / 0.0040), 1367.4)
chk("C2-04 P3.2 W̄ ở 400 K (10⁻²¹ J)", 1.5 * KB * 400 / 1e-21, 8.28)
chk("C2-04 P3.3 V khi p = 2 atm", 3.0 / 2.0, 1.5)
chk("C2-04 P3.4 dịch chuyển pit-tông (cm)", 400.0 / 80.0, 5.0)
chk("C2-04 P3.5 U của 2 mol (kJ)", 1.5 * 2.0 * R * 300 / 1000, 7.479)
chk("C2-04 P3.6 p chung (10⁵ Pa)", (4.0 * 3.0 + 1.5 * 2.0) / 5.0, 3.0)

# ======================================================= CHƯƠNG II – ĐỀ 05
_pV = {"1": 1 * 1, "2": 4 * 1, "3": 4 * 4, "4": 1 * 4}
chk("C2-05 MC9 pV lớn nhất là trạng thái 3",
    1.0 if max(_pV, key=_pV.get) == "3" else 0.0, 1.0)
chk("C2-05 MC10 T₃ (K)", 300 * 16 / 1, 4800)
chk("C2-05 MC11 V bóng (m³)", 8.0 * (1.0 / 0.40) * (240 / 300), 16.0)
chk("C2-05 MC12 tỉ số T₃/T₁", (1.0 * 1.0) / (4.0 * 1.0), 0.25)
chk("C2-05 MC13 nhiệt độ (°C)", 4 * 300 - 273, 927)
chk("C2-05 MC14 p của 0,1 mol O₂", 0.10 * R * 400 / 5.0e-3, 66480)
chk("C2-05 MC15 p trong xi lanh", 1.0e5 + (2.0 * 10) / 50e-4, 1.04e5)
chk("C2-05 MC16 p mới (10⁵ Pa)", 2.0 * (1 / 0.75) * (400.0 / 300.0), 3.556)
chk("C2-05 MC17 tỉ số số mol",
    (1.8 * 3.5 / 310) / (1.2 * 3.0 / 300), 1.6935)
chk("C2-05 MC18 tỉ số áp suất", 0.80 * 1.25, 1.0)
chk("C2-05 ĐS1a T₂ (K)", 300 * 4 / 1, 1200)
chk("C2-05 ĐS1b T₃ (K)", 1200 * 4, 4800)
chk("C2-05 ĐS1c pV(2) = pV(4)", (4 * 1) - (1 * 4), 0)
chk("C2-05 ĐS2c tỉ số v_rms", sqrt(700.0 / 300.0), 1.528)
chk("C2-05 ĐS4a V ở độ cao (m³)", 8.0 * 2.5 * 0.80, 16.0)
chk("C2-05 ĐS4b tỉ số khối lượng riêng", 8.0 / 16.0, 0.5)
chk("C2-05 ĐS4d V ở 0,25·10⁵ Pa (m³)", 8.0 * 4.0 * (220.0 / 300.0), 23.47)
chk("C2-05 P3.1 ℓ cột khí (cm)", 30.0 * 351 / 300, 35.1)
chk("C2-05 P3.2 v_rms N₂ ở 400 K", sqrt(3 * R * 400 / 0.028), 596.8)
_p = (4.0 * 2.0 + 1.0 * 3.0) / 5.0
chk("C2-05 P3.3 p chung ở 300 K (10⁵ Pa)", _p, 2.2)
chk("C2-05 P3.3' p ở 400 K (10⁵ Pa)", _p * 400 / 300, 2.933)
chk("C2-05 P3.4 U (J)", 1.5 * 0.20 * R * 300, 747.9)
chk("C2-05 P3.5 p cuối (10⁵ Pa)", 3.0 * 600 / 300, 6.0)
chk("C2-05 P3.6 p (10⁵ Pa)", 2.4 * 0.70 * (400.0 / 300.0), 2.24)


if __name__ == "__main__":
    print("KIỂM TRA ĐỘC LẬP SỐ LIỆU CỦA 10 ĐỀ KIỂM TRA")
    print("=" * 66)
    for lab, got, want in BAD:
        print("  ✗ %-50s tính ra %s, đề ghi %s" % (lab, got, want))
    print("Số phép kiểm tra ĐẠT: %d" % len(OK))
    print("Số phép kiểm tra SAI: %d" % len(BAD))
    if not BAD:
        print("→ Toàn bộ số liệu định lượng đều nhất quán.")
