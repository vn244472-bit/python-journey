"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.


# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2


# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %


# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"

# Bai tap 02: May tinh Python

# TODO 1: Tinh 2024 + 1000
print("2024 + 1000 =", 2024 + 1000)

# TODO 2: Tinh tien con lai
tien = 150000
gia_ca_phe = 35000
so_ly = 3

tien_con_lai = tien - gia_ca_phe * so_ly
print("So tien con lai:", tien_con_lai, "VND")

# TODO 3: Tinh dien tich hinh tron
ban_kinh = 7
dien_tich = 3.14159 * ban_kinh ** 2
print("Dien tich hinh tron:", round(dien_tich, 2))

# TODO 4: Chia 100 vien keo cho 7 nguoi
keo = 100
nguoi = 7

print("Moi nguoi duoc:", keo // nguoi, "vien")
print("So keo con du:", keo % nguoi)

# TODO 5: Doi Celsius sang Fahrenheit
C = 37
F = C * 9 / 5 + 32

print(str(C) + "°C =", F, "°F")

python weeks/week-01-hello-python/exercises/ex02_calculator.py
