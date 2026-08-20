# -*- coding: utf-8 -*-
"""Kiểm tra ĐỘC LẬP mọi con số định lượng trong bộ tài liệu học kì I.

Mỗi phép kiểm tra được tính lại từ đầu bằng vật lí, rồi đối chiếu với con số đã ghi
trong đề bài hoặc lời giải. Mục đích là phát hiện lỗi số học, lỗi đổi đơn vị và lỗi
sao chép, chứ không phải để minh hoạ lời giải.
"""
import math

C_W, C_ICE, C_STEAM = 4200.0, 2100.0, 2010.0
C_AL, C_FE, C_CU, C_PB = 880.0, 460.0, 380.0, 130.0
LAM, LV = 3.34e5, 2.26e6
R, NA, KB = 8.31, 6.02e23, 1.38e-23

ok, bad = 0, []


def chk(label, got, want, tol=0.012):
    """So sánh tương đối; tol mặc định 1,2 % để chấp nhận làm tròn trong lời giải."""
    global ok
    if want == 0:
        good = abs(got) < 1e-9
    else:
        good = abs(got - want) / abs(want) <= tol
    if good:
        ok += 1
    else:
        bad.append("%-58s tính được %.6g  ≠  đã ghi %.6g" % (label, got, want))


def mix2(m1, c1, t1, m2, c2, t2):
    return (m1 * c1 * t1 + m2 * c2 * t2) / (m1 * c1 + m2 * c2)


# ==================================================== CHƯƠNG I – lí thuyết
chk("LT1 ví dụ mẫu: đun 0,5 kg đá −20 °C thành hơi (kJ)",
    (0.5 * C_ICE * 20 + 0.5 * LAM + 0.5 * C_W * 100 + 0.5 * LV) / 1e3, 1528.0)
chk("LT1 tỉ lệ chặng hoá hơi trong tổng (%)",
    100 * (0.5 * LV) / (0.5 * C_ICE * 20 + 0.5 * LAM + 0.5 * C_W * 100 + 0.5 * LV), 74.0, 0.02)
chk("LT1 tỉ số L/λ của nước", LV / LAM, 6.8, 0.01)
chk("LT1 c_nước / c_nhôm", C_W / C_AL, 4.8, 0.01)
chk("LT1 hình h10: c từ hệ số góc 0,42 kJ/K với m = 0,20 kg", 420.0 / 0.20, 2100.0)

# ==================================================== CHƯƠNG I – MC1
chk("MC1 khí nhận 300 J, sinh công 500 J → ΔU", -500 + 300, -200)
chk("MC1 nước đá 0,5 kg −10 °C, cấp 1,0e5 J → khối lượng tan (kg)",
    (1.0e5 - 0.5 * C_ICE * 10) / LAM, 0.268, 0.02)
chk("MC1 trộn 100 g 20 °C + 300 g 80 °C", mix2(0.1, C_W, 20, 0.3, C_W, 80), 65.0)
chk("MC1 tan 200 g đá rồi lên 20 °C (kJ)", (0.2 * LAM + 0.2 * C_W * 20) / 1e3, 83.6)
chk("MC1 đun 1 kg nước 20→100 rồi hoá hơi: tỉ số", LV / (C_W * 80), 6.7, 0.01)
chk("MC1 vật 2 kg rơi 10 m, c = 500 → ΔT", 2 * 10 * 10 / (2 * 500.0), 0.20)
chk("MC1 ấm 1500 W đun 1,5 kg 25→100 (s)", 1.5 * C_W * 75 / 1500.0, 315.0)
chk("MC1 L4 tỉ số L/c từ 4 phút và 12 phút, ΔT = 40 K", 40 * 12 / 4.0, 120.0)
chk("MC1 L4 nhiệt lượng kế 150 J/K: c kim loại",
    (0.30 * C_W * 6 + 200 * 6) / (0.20 * 74), 592.0, 0.01)
chk("MC1 L4 nếu quên bình nhiệt lượng kế", (0.30 * C_W * 6) / (0.20 * 74), 511.0, 0.01)
chk("MC1 L4 hỗn hợp 0,5 kg đá + cấp 1,0e5 J → đá còn lại (kg)",
    0.50 - 1.0e5 / LAM, 0.20, 0.02)

# ==================================================== CHƯƠNG I – DS1
chk("DS1.1 giai đoạn ① với m = 0,40 kg (kJ)", 0.40 * C_ICE * 20 / 1e3, 16.8)
chk("DS1.1 Q₄/Q₂", (0.40 * LV) / (0.40 * LAM), 6.8, 0.01)
chk("DS1.1 tổng Q (MJ)",
    (0.40 * C_ICE * 20 + 0.40 * LAM + 0.40 * C_W * 100 + 0.40 * LV) / 1e6, 1.2224, 0.01)
chk("DS1.2 quá trình (I): ΔU", 200 + 500, 700)
chk("DS1.3 c từ P=40 W, m=0,25 kg, ΔT/t = 0,040 K/s", 40 / (0.25 * 0.040), 4000.0)
chk("DS1.3 nước c=4200: ΔT sau 300 s", 40 * 300 / (0.25 * C_W), 11.4, 0.01)
chk("DS1.4 tan 0,50 kg đá (kJ)", 0.50 * LAM / 1e3, 167.0)
chk("DS1.4 2,0 kg nước 50→0 (kJ)", 2.0 * C_W * 50 / 1e3, 420.0)
chk("DS1.4 nhiệt độ cân bằng", (2.0 * C_W * 50 - 0.50 * LAM) / (2.0 * C_W + 0.50 * C_W), 24.1, 0.01)
chk("DS1.6 cân bằng hai vật c=900/450", mix2(0.5, 900, 20, 0.5, 450, 80), 40.0)
chk("DS1.6 tỉ số độ biến thiên nhiệt độ", 900 / 450.0, 2.0)
chk("DS1.8 thả viên đá 50 g vào 1,0 kg nước 90 °C",
    (1.0 * C_W * 90 - 0.050 * LAM) / (1.0 * C_W + 0.050 * C_W), 81.9, 0.01)

# ==================================================== CHƯƠNG I – CALC1
chk("C1 D1 đun 2 kg 25→75 (kJ)", 2.0 * C_W * 50 / 1e3, 420.0)
chk("C1 D1 ấm 2000 W H=80 % đun 2 kg 20→100 (s)", 2.0 * C_W * 80 / (0.8 * 2000), 420.0)
chk("C1 D1 toả 150 J, nhận công 400 J → ΔU", 400 - 150, 250)
chk("C1 D1 nhôm 0,5 kg 100 °C vào 1 kg nước 20 °C",
    mix2(0.5, C_AL, 100, 1.0, C_W, 20), 27.6, 0.01)
chk("C1 D1 tan 2 kg đá (kJ)", 2.0 * LAM / 1e3, 668.0)
chk("C1 D1 0,5 kg đá −10 → nước 20 (kJ)",
    (0.5 * C_ICE * 10 + 0.5 * LAM + 0.5 * C_W * 20) / 1e3, 219.5)
chk("C1 D1 vật 5 kg rơi 20 m, 60 %, c=400 → ΔT", 0.60 * 5 * 10 * 20 / (5 * 400.0), 0.30)
chk("C1 D1 P=50 W, 168 s, m=0,4 kg, ΔT=10 → c", 50 * 168 / (0.40 * 10), 2100.0)
chk("C1 D1 trộn 300 g 90 °C + 200 g 20 °C", mix2(0.3, C_W, 90, 0.2, C_W, 20), 62.0)
chk("C1 D1 nhiệt lượng kế đồng 200 g + nước 500 g, ΔT=10 (J)",
    0.5 * C_W * 10 + 0.2 * C_CU * 10, 21760.0)
chk("C1 D1 tỉ số λ/c từ 8 phút và 2 phút, ΔT=40", 40 * 8 / 2.0, 160.0)
chk("C1 D1 100 g đá vào 400 g nước 50 °C",
    (0.4 * C_W * 50 - 0.1 * LAM) / (0.4 * C_W + 0.1 * C_W), 24.1, 0.01)
chk("C1 D1 3,0e6 J đun nước 20→100 (kg)", 3.0e6 / (C_W * 80), 8.93, 0.01)
chk("C1 D1 hoá hơi 0,5 kg nước (MJ)", 0.5 * LV / 1e6, 1.13)
chk("C1 D1 hai vật c=900/450 ở 20 và 80 °C", mix2(1, 900, 20, 1, 450, 80), 40.0)
chk("C1 D1 hơi 100 °C ngưng tụ vào 2 kg nước 20→40 °C (g)",
    1000 * (2.0 * C_W * 20) / (LV + C_W * 60), 67.0, 0.05)
chk("C1 D1 chu trình nhận 2500 toả 1800 → công sinh", 2500 - 1800, 700)

chk("C1 D2.1 đá 1,5 kg −20→0 (kJ)", 1.5 * C_ICE * 20 / 1e3, 63.0)
chk("C1 D2.1 thời gian tới khi bắt đầu tan (s)", 1.5 * C_ICE * 20 / 800.0, 78.75)
chk("C1 D2.1 tan hết 1,5 kg đá (kJ)", 1.5 * LAM / 1e3, 501.0)
chk("C1 D2.1 tổng thời gian tới 100 °C (s)",
    (1.5 * C_ICE * 20 + 1.5 * LAM + 1.5 * C_W * 100) / 800.0, 1492.5)
chk("C1 D2.2 đá 3 viên 20 g từ −18 → 0 °C (J)", 0.060 * C_ICE * 18, 2268.0)
chk("C1 D2.2 tan hết 60 g đá (kJ)", 0.060 * LAM / 1e3, 20.04)
chk("C1 D2.2 nhiệt độ cuối của cốc cà phê",
    (0.250 * C_W * 70 - 0.060 * C_ICE * 18 - 0.060 * LAM) / (0.250 * C_W + 0.060 * C_W),
    39.3, 0.01)
chk("C1 D2.4 nước thu (J)", 0.200 * C_W * 6.0, 5040.0)
chk("C1 D2.4 bình thu (J)", 150 * 6.0, 900.0)
chk("C1 D2.4 c kim loại", (5040 + 900) / (0.150 * 72), 550.0)
chk("C1 D2.4 nếu bỏ qua bình", 5040 / (0.150 * 72), 467.0, 0.01)
chk("C1 D2.6 tỉ số λ/(c·30) từ 10 phút và 4 phút", 10 / 4.0, 2.5)

chk("C1 D3 đun 3 kg 30→80 (kJ)", 3.0 * C_W * 50 / 1e3, 630.0)
chk("C1 D3 nhận 500 sinh công 200 → ΔU", 500 - 200, 300)
chk("C1 D3 kim loại 200 g 120 °C vào 400 g nước 25→30 → c",
    0.4 * C_W * 5 / (0.2 * 90), 467.0, 0.01)
chk("C1 D3 1 kg đá 0 °C → hơi 100 °C (MJ)", (LAM + C_W * 100 + LV) / 1e6, 3.01, 0.01)
chk("C1 D3 ấm 1200 W đun 1 kg 20→100 (s)", C_W * 80 / 1200.0, 280.0)
chk("C1 D3 45 °C sang K", 45 + 273, 318)
chk("C1 D3 500 g đá vào 2 kg nước 60 °C",
    (2.0 * C_W * 60 - 0.5 * LAM) / (2.0 * C_W + 0.5 * C_W), 32.1, 0.01)
chk("C1 D3 vật 4 kg rơi 25 m, c=500 → ΔT", 4 * 10 * 25 / (4 * 500.0), 0.50)
chk("C1 D3 tan 750 g đá (kJ)", 0.750 * LAM / 1e3, 250.5)
chk("C1 D3 trộn 1,2 kg 85 °C + 0,8 kg 25 °C", mix2(1.2, C_W, 85, 0.8, C_W, 25), 61.0)
chk("C1 D3 toả 300 J, ΔU = −500 → công sinh", -(-500 - (-300)), 200)
chk("C1 D3 P=60 W, 350 s, m=0,25, ΔT=20 → c", 60 * 350 / (0.25 * 20), 4200.0)
chk("C1 D3 bình 180 J/K + 0,4 kg nước, ΔT=10 (kJ)", (0.4 * C_W * 10 + 180 * 10) / 1e3, 18.6)
chk("C1 D3 hoá hơi 0,30 kg nước (kJ)", 0.30 * LV / 1e3, 678.0)

# CALC1 D4
t1 = (2.0 * C_W * 70 - 0.100 * LAM) / (2.0 * C_W + 0.100 * C_W)
chk("C1 D4.1a viên đá thứ nhất vào 2 kg nước 70 °C", t1, 62.9, 0.01)
t2 = (2.1 * C_W * t1 - 0.100 * LAM) / (2.1 * C_W + 0.100 * C_W)
chk("C1 D4.1b viên đá thứ hai", t2, 56.4, 0.01)
chk("C1 D4.1d khối lượng đá tối đa (kg)", 2.0 * C_W * 70 / LAM, 1.76, 0.01)
chk("C1 D4.2a đun 1,5 kg 25→100 (kJ)", 1.5 * C_W * 75 / 1e3, 472.5)
chk("C1 D4.2b hiệu suất (%)", 100 * (1.5 * C_W * 75) / (1500 * 360), 87.5)
chk("C1 D4.2c khối lượng hoá hơi trong 300 s (kg)", 0.875 * 1500 * 300 / LV, 0.174, 0.01)
chk("C1 D4.3a c_rắn", 250 * 120 / (0.60 * 60), 833.0, 0.01)
chk("C1 D4.3b λ", 250 * 360 / 0.60, 1.50e5)
chk("C1 D4.3c c_lỏng", 250 * 180 / (0.60 * 40), 1875.0)
chk("C1 D4.4a công suất tải nhiệt (kW)", 0.20 * C_W * 50 / 1e3, 42.0)
chk("C1 D4.4b lưu lượng chất lỏng c=2000 (kg/s)", 42000 / (2000 * 50), 0.42)
chk("C1 D4.5b λ từ 36,0 g trong 300 s ở 40 W", 40 * 300 / 0.0360, 3.33e5, 0.01)
chk("C1 D4.5c sai lệch nếu bỏ đối chứng (%)",
    100 * (40 * 300 / 0.0360 - 40 * 300 / 0.0420) / (40 * 300 / 0.0360), 14.3, 0.01)
chk("C1 D4.6a khối lượng không khí (kg)", 1.2 * 60, 72.0)
chk("C1 D4.6b nhiệt lượng sưởi (kJ)", 72 * 1000 * 10 / 1e3, 720.0)
chk("C1 D4.6b thời gian sưởi (s)", 720000 / 2000.0, 360.0)
chk("C1 D4.6d đun 2 lít nước 25→100 (kJ)", 2.0 * C_W * 75 / 1e3, 630.0)

# ==================================================== CHƯƠNG II
chk("MC2 W̄ ở 300 K (J)", 1.5 * KB * 300, 6.21e-21, 0.01)
chk("MC2 v_rms O2 ở 300 K", math.sqrt(3 * R * 300 / 0.032), 483.0, 0.01)
chk("MC2 v_rms He ở 300 K", math.sqrt(3 * R * 300 / 0.004), 1367.0, 0.01)
chk("MC2 v_rms H2 ở 300 K", math.sqrt(3 * R * 300 / 0.002), 1934.0, 0.01)
chk("MC2 tỉ số v_He/v_Ar", math.sqrt(40 / 4.0), 3.16, 0.01)
chk("MC2 tỉ số v_H2/v_O2", math.sqrt(32 / 2.0), 4.0)
chk("MC2 số phân tử trong 1 cm³ ở đktc", 6.02e23 / 22400.0, 2.7e19, 0.02)
chk("MC2 27→54 °C đẳng áp: tỉ lệ tăng (%)", 100 * (327 / 300.0 - 1), 9.0, 0.02)
chk("MC2 hai bình V và 2V, mở khoá → p'", 1 / 3.0, 0.3333, 0.01)
chk("MC2 bình 20 L 6e5 → 2e5: phần thoát (%)", 100 * (1 - 2.0 / 6.0), 66.7, 0.01)
chk("MC2 v_rms 500 → 1000 m/s: T mới (K)", 300 * 4, 1200)
chk("MC2 t mới (°C)", 300 * 4 - 273, 927)
chk("MC2 bình kín 1e5 Pa 27 °C, chịu 3e5 Pa → t max (°C)", 300 * 3 - 273, 627)
chk("MC2 bóng 1,2e5/2,0 L/300 K → 2,0e5/280 K (L)", 1.2 * 2.0 * 280 / (2.0 * 300), 1.12, 0.01)
chk("MC2 bình khí nén 40 L 150 atm → số bình 2,0 L 5,0 atm",
    (150 - 5) * 40 / 5.0 / 2.0, 580.0)
chk("MC2 ống thuỷ ngân lật: tỉ số 65/85", 65 / 85.0, 0.7647, 0.01)
chk("MC2 pit-tông hai ngăn 2T/T: V_A/V_B", 2.0, 2.0)
chk("MC2 hai bình 400 K và 300 K: p' = 8p0/7", 8 / 7.0, 1.1429, 0.01)

chk("C2 D1 Boyle 6 L 1e5 → 2 L", 1.0e5 * 6.0 / 2.0, 3.0e5)
chk("C2 D1 Charles 3 L 300→400 K", 3.0 * 400 / 300.0, 4.0)
chk("C2 D1 đẳng tích 1,5e5 Pa 300→450 K", 1.5e5 * 450 / 300.0, 2.25e5)
chk("C2 D1 phương trình trạng thái V2", 2.0 * 4.0 * 450 / (1.0 * 300), 12.0)
chk("C2 D1 n = pV/RT với 8,31 L, 300 K, 1e5 Pa", 1.0e5 * 8.31e-3 / (R * 300), 0.333, 0.01)
chk("C2 D1 W̄ ở 300 K", 1.5 * KB * 300, 6.21e-21, 0.01)
chk("C2 D1 bình 20 L 5e5 → 2e5: thoát (%)", 100 * (1 - 2.0 / 5.0), 60.0)
chk("C2 D1 bình 3 L 4e5 nối bình 5 L chân không", 4.0e5 * 3.0 / 8.0, 1.5e5)
chk("C2 D1 khối lượng 5 L N2 ở 2e5 Pa 300 K (g)",
    2.0e5 * 5.0e-3 / (R * 300) * 28, 11.2, 0.01)
chk("C2 D1 áp suất cột khí miệng trên (cmHg)", 75 + 15, 90)
chk("C2 D1 số phân tử trong 2 L ở 1e5 Pa 300 K",
    1.0e5 * 2.0e-3 / (KB * 300), 4.83e22, 0.01)
chk("C2 D1 v_rms tăng 3 lần → T (K)", 300 * 9, 2700)
chk("C2 D1 bóng 1,2e5/2 L/300 K → 3e5/280 K (L)", 1.2 * 2.0 * 280 / (3.0 * 300), 0.747, 0.01)
chk("C2 D1 p = ρv²/3 với ρ=1,25, v=500", 1.25 * 500 ** 2 / 3.0, 1.04e5, 0.01)
chk("C2 D1 nén giảm 40 % thể tích → tăng áp (%)", 100 * (1 / 0.60 - 1), 66.7, 0.01)
chk("C2 D1 n×1,5 và T×2 → p tăng", 1.5 * 2, 3.0)

chk("C2 D2.2 n trong bình 20 L 4e5 Pa 300 K", 4.0e5 * 20e-3 / (R * 300), 3.209, 0.01)
chk("C2 D2.2 khối lượng O2 (g)", 4.0e5 * 20e-3 / (R * 300) * 32, 103.0, 0.01)
chk("C2 D2.2 nung 300→360 K", 4.0e5 * 360 / 300.0, 4.8e5)
chk("C2 D2.3 V_A/V_B = 450/300", 450 / 300.0, 1.5)
chk("C2 D2.3 V_A với tổng 600 cm³", 600 * 1.5 / 2.5, 360.0)
chk("C2 D2.3 áp suất ngăn B tăng", 300 / 240.0, 1.25)
chk("C2 D2.4 ℓ/T tại 0 °C", 10.0 / 273, 0.0366, 0.01)
chk("C2 D2.4 ℓ/T tại 100 °C", 13.7 / 373, 0.0367, 0.01)
chk("C2 D2.5 thể tích dùng được ở 1 atm (L)", (120 - 10) * 50 / 1.0, 5500.0)
chk("C2 D2.5 thời gian dùng (phút)", 5500 / 3.0, 1833.0, 0.01)
chk("C2 D2.6 v_rms He 300 K", math.sqrt(3 * R * 300 / 0.004), 1368.0, 0.01)

chk("C2 D3 Boyle 2e5 5 L → 8 L", 2.0 * 5.0 / 8.0, 1.25)
chk("C2 D3 27→327 °C đẳng áp", 600 / 300.0, 2.0)
chk("C2 D3 đẳng tích 1e5 → 2,5e5, T=300", 300 * 2.5, 750.0)
chk("C2 D3 n bình 10 L 2e5 Pa 300 K", 2.0e5 * 10e-3 / (R * 300), 0.80, 0.01)
chk("C2 D3 v_rms H2 300 K", math.sqrt(3 * R * 300 / 0.002), 1934.0, 0.01)
chk("C2 D3 T2 từ 3e5·2 L·300 K → 2e5·4,5 L", 300 * (2.0 * 4.5) / (3.0 * 2.0), 450.0)
chk("C2 D3 cột khí miệng dưới (cmHg)", 76 - 20, 56)
chk("C2 D3 W̄ ở 400 K (1e-21 J)", 1.5 * KB * 400 / 1e-21, 8.28, 0.01)
chk("C2 D3 bình 4 L 6e5 nối 6 L chân không", 6.0 * 4.0 / 10.0, 2.40)
chk("C2 D3 p = ρv²/3, ρ=1,2, v=450 (1e4 Pa)", 1.2 * 450 ** 2 / 3.0 / 1e4, 8.1, 0.01)
chk("C2 D3 lốp 2,5e5 Pa 300→330 K", 2.5 * 330 / 300.0, 2.75)
chk("C2 D3 N trong 1 cm³ ở 1e5 Pa 300 K (1e19)",
    1.0e5 * 1.0e-6 / (KB * 300) / 1e19, 2.4, 0.02)
chk("C2 D3 xả từ 8e5 xuống 3e5: đã xả (%)", 100 * (1 - 3.0 / 8.0), 62.5)
chk("C2 D3 áp suất ×4 → thể tích giảm (%)", 100 * (1 - 1 / 4.0), 75.0)

chk("C2 D4.1a p = p0 + mg/S", 1.0e5 + 2.0 * 10 / 50e-4, 1.04e5)
chk("C2 D4.1b ℓ đẳng áp 300→360 K (cm)", 20 * 360 / 300.0, 24.0)
chk("C2 D4.1c p đẳng tích 300→360 K", 1.04e5 * 360 / 300.0, 1.248e5)
chk("C2 D4.1d ℓ khi lật ngược (cm)", 1.04e5 * 20 / 0.96e5, 21.7, 0.01)
chk("C2 D4.2a p cột khí miệng trên (cmHg)", 76 + 20, 96)
chk("C2 D4.2b ℓ khi lật ngược (cm)", 96 * 40 / 56.0, 68.6, 0.01)
chk("C2 D4.2b tổng chiều dài chiếm chỗ (cm)", 96 * 40 / 56.0 + 20, 88.6, 0.01)
chk("C2 D4.2c ℓ đẳng áp 300→360 K (cm)", 40 * 360 / 300.0, 48.0)
chk("C2 D4.3a bóng ở 0,5e5 Pa 270 K (m³)", 1.0 * 8.0 * 270 / (0.50 * 300), 14.4)
chk("C2 D4.3b bóng ở 0,25e5 Pa 240 K (m³)", 1.0 * 8.0 * 240 / (0.25 * 300), 25.6)
chk("C2 D4.3c p khi V = 30 m³ ở 220 K (1e5 Pa)", 1.0 * 8.0 * 220 / (30 * 300), 0.196, 0.01)
chk("C2 D4.4a n bình 10 L 1e5 Pa 300 K", 1.0e5 * 10e-3 / (R * 300), 0.401, 0.01)
chk("C2 D4.4a số phân tử", 1.0e5 * 10e-3 / (R * 300) * NA, 2.41e23, 0.01)
chk("C2 D4.4b số mol bơm thêm", 2 * 1.0e5 * 10e-3 / (R * 300), 0.802, 0.01)
chk("C2 D4.4c đẳng tích 3e5 Pa 300→400 K", 3.0e5 * 400 / 300.0, 4.0e5)
chk("C2 D4.4d T max cho 5e5 Pa (K)", 300 * 5.0 / 3.0, 500.0)
chk("C2 D4.5 chu trình: T2", 600 * 1.0 / 3.0, 200.0)
chk("C2 D4.5 chu trình: T3", 200 * 6.0 / 2.0, 600.0)
chk("C2 D4.6a n mỗi bình 5 L 2e5 Pa 300 K", 2.0e5 * 5e-3 / (R * 300), 0.401, 0.01)
chk("C2 D4.6b p_A sau khi nung 300→400 K", 2.0e5 * 400 / 300.0, 2.67e5, 0.01)
_ntot = 2 * 2.0e5 * 5e-3 / (R * 300)
_pp = _ntot / ((5e-3 / (R * 400)) + (5e-3 / (R * 300)))
chk("C2 D4.6c áp suất chung sau khi mở khoá", _pp, 2.285e5, 0.01)
chk("C2 D4.6d n_A", _pp * 5e-3 / (R * 400), 0.344, 0.01)
chk("C2 D4.6d n_B", _pp * 5e-3 / (R * 300), 0.458, 0.01)

# ==================================================== TỔNG HỢP I + II
chk("TH D1 1 mol đơn nguyên tử đẳng tích 300→400 K (J)", 1.5 * 1 * R * 100, 1247.0, 0.01)
chk("TH D1 U của 2 mol ở 300 K (J)", 1.5 * 2 * R * 300, 7479.0)
chk("TH D1 đẳng áp nhận 800 sinh công 320 → ΔU", 800 - 320, 480)
chk("TH D1 thể tích hơi từ 1 kg nước ở 373 K, 1e5 Pa (m³)",
    (1000 / 18.0) * R * 373 / 1.0e5, 1.72, 0.01)
chk("TH D1 chu trình nhận 1200 toả 800 → công", 1200 - 800, 400)
chk("TH D2.1 U ban đầu 0,5 mol 300 K (J)", 1.5 * 0.5 * R * 300, 1870.0, 0.01)
chk("TH D2.1 ΔT khi cấp 500 J đẳng tích (K)", 500 / (1.5 * 0.5 * R), 80.2, 0.01)
chk("TH D2.2 đun 1,5 kg nước 20→120 °C (kJ)", 1.5 * C_W * 100 / 1e3, 630.0)
chk("TH D2.2 452 kJ hoá hơi (kg)", 452000 / LV, 0.20, 0.01)
chk("TH D2.3 p ban đầu 0,8 mol 20 L 300 K (1e5 Pa)", 0.8 * R * 300 / 20e-3 / 1e5, 0.997, 0.01)
chk("TH D2.3 U ban đầu (J)", 1.5 * 0.8 * R * 300, 2992.0, 0.01)
chk("TH D2.3 ΔT khi cấp 3000 J (K)", 3000 / (1.5 * 0.8 * R), 301.0, 0.01)
chk("TH D3 1 mol đẳng tích 300→500 K (J)", 1.5 * R * 200, 2493.0)
chk("TH D3 nhận 900 sinh công 350 → ΔU", 900 - 350, 550)
chk("TH D3 U của 3 mol ở 400 K (J)", 1.5 * 3 * R * 400, 14958.0)
chk("TH D3 thể tích hơi từ 2 kg nước (m³)", (2000 / 18.0) * R * 373 / 1.0e5, 3.44, 0.01)
chk("TH D3 đẳng áp 1 mol: T cuối (K)",
    300 + (1500 - 600) / (1.5 * 1 * R), 372.0, 0.01)
chk("TH D4.1a V1 của 0,4 mol ở 300 K, 1e5 Pa (L)", 0.4 * R * 300 / 1.0e5 * 1e3, 9.97, 0.01)
chk("TH D4.1b ΔT đẳng áp khi Q = 1500 J (K)", 2 * 1500 / (5 * 0.4 * R), 180.5, 0.01)
chk("TH D4.1c công sinh ra (J)", 0.4 * R * (2 * 1500 / (5 * 0.4 * R)), 600.0, 0.01)
chk("TH D4.1c ΔU (J)", 1.5 * 0.4 * R * (2 * 1500 / (5 * 0.4 * R)), 900.0, 0.01)
chk("TH D4.1d tỉ lệ công/nhiệt (%)", 100 * 2 / 5.0, 40.0)
chk("TH D4.2a công suất nồi hơi (kW)",
    (500 * C_W * 75 + 500 * LV) / 3600 / 1e3, 358.0, 0.01)
chk("TH D4.2b thể tích hơi mỗi giờ (m³)",
    (500000 / 18.0) * R * 373 / 1.0e5, 861.0, 0.01)
_n = 500000 / 18.0
chk("TH D4.2c p trong bình 20 m³ ở 473 K (1e6 Pa)", _n * R * 473 / 20 / 1e6, 5.46, 0.01)
chk("TH D4.2d tỉ số hoá hơi / đun nóng", (500 * LV) / (500 * C_W * 75), 7.17, 0.01)
chk("TH D4.3a p ngăn A 0,5 mol 10 L 400 K (1e5 Pa)", 0.5 * R * 400 / 10e-3 / 1e5, 1.66, 0.01)
chk("TH D4.3c p sau khi dãn vào 30 L (1e5 Pa)", 0.5 * R * 400 / 30e-3 / 1e5, 0.554, 0.01)
chk("TH D4.4a V bóng ở 300 K (L)", 0.10 * R * 300 / 1.0e5 * 1e3, 2.49, 0.01)
chk("TH D4.4a V bóng ở 260 K (L)", 0.10 * R * 260 / 1.0e5 * 1e3, 2.16, 0.01)
chk("TH D4.4b ΔU (J)", 1.5 * 0.10 * R * (260 - 300), -49.9, 0.01)
_dV = 0.10 * R * 260 / 1.0e5 - 0.10 * R * 300 / 1.0e5
chk("TH D4.4c công khí quyển thực hiện (J)", -1.0e5 * _dV, 33.2, 0.01)
chk("TH D4.4d nhiệt lượng trao đổi (J)",
    1.5 * 0.10 * R * (-40) - (-1.0e5 * _dV), -83.1, 0.01)
chk("TH D4.5a thể tích không khí (L)", 50 - 2.0, 48.0)
chk("TH D4.5b p sau khi đun 293→353 K (1e5 Pa)", 1.0 * 353 / 293.0, 1.205, 0.01)
chk("TH D4.5c nhiệt lượng cho nước (kJ)", 2.0 * C_W * 60 / 1e3, 504.0)
chk("TH D4.5d T max cho 2e5 Pa (K)", 293 * 2.0, 586.0)

print("Số phép kiểm tra ĐẠT:", ok)
print("Số phép kiểm tra SAI:", len(bad))
for b in bad:
    print("   ✗", b)
