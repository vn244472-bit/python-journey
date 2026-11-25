"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_text = "42"

so = int(so_text)
so = so + 8

print("Ket qua:", so)


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
# TODO 2: Chuyen float sang int
pi = 3.14159

print("Pi:", int(pi))

# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
# TODO 3: Kiem tra bool()
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2]))

# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
# TODO 4: Nhap chieu cao va can nang
chieu_cao = float(input("Nhap chieu cao (m): "))
can_nang = float(input("Nhap can nang (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"BMI: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"

# TODO 5: Doi giay sang gio, phut, giay
tong_giay = int(input("Nhap so giay: "))

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{gio} gio {phut} phut {giay} giay")
