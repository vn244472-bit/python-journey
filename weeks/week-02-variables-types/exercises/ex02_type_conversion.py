
"""
Bài tập 02: Chuyển đổi kiểu dữ liệu
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Chuyen chuoi sang so nguyen
so_text = "42"

so = int(so_text)
so = so + 8

print("Ket qua:", so)

# TODO 2: Chuyen float sang int
pi = 3.14159

print("Pi:", int(pi))

# TODO 3: Kiem tra bool()
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2]))

# TODO 4: Nhap chieu cao va can nang
chieu_cao = float(input("Nhap chieu cao (m): "))
can_nang = float(input("Nhap can nang (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"BMI: {bmi:.1f}")

# TODO 5: Doi giay sang gio, phut, giay
tong_giay = int(input("Nhap so giay: "))

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{gio} gio {phut} phut {giay} giay")
