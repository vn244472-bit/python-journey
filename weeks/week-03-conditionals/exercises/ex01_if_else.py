"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"


# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu


# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else

# TODO 1: Phân loại tuổi
tuoi = int(input("Nhap tuoi: "))

if tuoi < 13:
    print("Thieu nhi")
elif tuoi <= 17:
    print("Thieu nien")
elif tuoi <= 64:
    print("Nguoi lon")
else:
    print("Nguoi cao tuoi")


# TODO 2: Xep loai diem
diem = float(input("Nhap diem (0-10): "))

if diem < 0 or diem > 10:
    print("Khong hop le")
elif diem >= 9:
    print("Xuat sac")
elif diem >= 8:
    print("Gioi")
elif diem >= 6.5:
    print("Kha")
elif diem >= 5:
    print("Trung binh")
else:
    print("Yeu")


# TODO 3: Kiem tra nam nhuan
nam = int(input("Nhap nam: "))

if nam % 400 == 0:
    print("Nam nhuan")
elif nam % 100 == 0:
    print("Khong phai nam nhuan")
elif nam % 4 == 0:
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")


# TODO 4: Tim so lon nhat trong 3 so
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a >= b and a >= c:
    print("So lon nhat:", a)
elif b >= a and b >= c:
    print("So lon nhat:", b)
else:
    print("So lon nhat:", c)
