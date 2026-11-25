
"""
Bài tập 01: Biến trong Python
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tao 4 bien
ten = "Loi"
tuoi = 19
diem_tb = 8.5
dang_hoc = True

print("Ten:", ten, type(ten))
print("Tuoi:", tuoi, type(tuoi))
print("Diem trung binh:", diem_tb, type(diem_tb))
print("Dang hoc:", dang_hoc, type(dang_hoc))

# TODO 2: Hoan doi 2 bien
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

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

# TODO 4: Multiple assignment
ho, ten, tuoi = "Nguyen", "Loi", 19

print(f"Ho ten: {ho} {ten}, {tuoi} tuoi")
