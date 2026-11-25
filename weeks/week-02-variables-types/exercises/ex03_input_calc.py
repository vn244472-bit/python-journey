"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)

# TODO 1: May tinh co ban
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

print("Tong:", a + b)
print("Hieu:", a - b)
print("Tich:", a * b)

if b != 0:
    print("Thuong:", a / b)
else:
    print("Khong the chia cho 0")


# TODO 2: Tinh hinh tron
pi = 3.14159

r = float(input("Nhap ban kinh: "))

dien_tich = pi * r ** 2
chu_vi = 2 * pi * r

print("Dien tich:", dien_tich)
print("Chu vi:", chu_vi)


# TODO 3: Tinh gia sau giam gia
gia_goc = float(input("Nhap gia goc: "))
giam_gia = float(input("Nhap phan tram giam gia: "))

gia_sau_giam = gia_goc - gia_goc * giam_gia / 100

print("Gia sau giam:", gia_sau_giam)


# TODO 4: May doi tien
vnd = float(input("Nhap so tien VND: "))
ty_gia = float(input("Nhap ty gia USD/VND: "))

usd = vnd / ty_gia

print(f"So tien USD: {usd:.2f}")
