"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
# TODO 1: Tao 4 bien
ten = "Loi"
tuoi = 19
diem_tb = 8.5
dang_hoc = True

print("Ten:", ten, type(ten))
print("Tuoi:", tuoi, type(tuoi))
print("Diem trung binh:", diem_tb, type(diem_tb))
print("Dang hoc:", dang_hoc, type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
# TODO 2: Hoan doi 2 bien
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
# TODO 3: Augmented assignment
x = 100

x += 10
print("Sau += :", x)

x -= 5
print("Sau -= :", x)

x *= 2
print("Sau *= :", x)

x //= 3
print("Sau //= :", x)

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"




# TODO 4: Multiple assignment
ho, ten, tuoi = "Nguyen", "Loi", 19

print(f"Ho ten: {ho} {ten}, {tuoi} tuoi")
