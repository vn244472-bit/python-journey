"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"

# TODO 1
email = "  User@Example.COM  "
email = email.strip().lower()
print(email)


# TODO 2
sentence = "hello world python programming"

print(sentence.title())
print("So ky tu o:", sentence.count("o"))
print(sentence.replace("python", "PYTHON"))


# TODO 3
ho_ten = input("Nhap ho ten: ").strip()
danh_sach = ho_ten.split()

if len(danh_sach) >= 2:
    print("Ho:", danh_sach[0])
    print("Ten:", danh_sach[-1])
else:
    print("Ho ten khong hop le")


# TODO 4
ten_file = input("Nhap ten file: ").strip().lower()

if ten_file.endswith((".py", ".txt", ".csv")):
    print("Ten file hop le")
else:
    print("Ten file khong hop le")


# TODO 5: Ma hoa Caesar
chuoi = input("Nhap chuoi: ")
shift = int(input("Nhap so buoc dich: "))

ket_qua = ""

for ky_tu in chuoi:
    if "a" <= ky_tu.lower() <= "z":
        co_so = ord("A") if ky_tu.isupper() else ord("a")
        moi = (ord(ky_tu) - co_so + shift) % 26
        ket_qua += chr(co_so + moi)
    else:
        ket_qua += ky_tu

print("Chuoi sau ma hoa:", ket_qua)
