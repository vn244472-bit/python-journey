"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"
# Viết if kiểm tra và in kết quả


# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?


# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)


# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó

# TODO 1: Kiem tra dieu kien
tuoi = int(input("Tuoi: "))
co_bang_lai = input("Co bang lai? (y/n): ").lower() == "y"
khong_say = input("Tinh tao? (y/n): ").lower() == "y"

if tuoi >= 18 and co_bang_lai and khong_say:
    print("Du dieu kien")
else:
    print("Khong du dieu kien")


# TODO 2: Phan loai tam giac
a = float(input("Canh a: "))
b = float(input("Canh b: "))
c = float(input("Canh c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Tam giac khong hop le")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Tam giac khong hop le")
elif a == b == c:
    print("Tam giac deu")
elif a == b or b == c or a == c:
    print("Tam giac can")
else:
    print("Tam giac thuong")


# TODO 3: Kiem tra mat khau manh
pw = input("Nhap mat khau: ")

co_chu_hoa = any(c.isupper() for c in pw)
co_chu_thuong = any(c.islower() for c in pw)
co_so = any(c.isdigit() for c in pw)

if len(pw) >= 8 and co_chu_hoa and co_chu_thuong and co_so:
    print("Mat khau manh")
else:
    print("Mat khau chua manh")


# TODO 4: FizzBuzz
n = int(input("Nhap n: "))

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
