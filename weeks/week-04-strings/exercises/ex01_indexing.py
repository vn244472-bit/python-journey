"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]

# TODO 1
s = "Python Journey"

print("Ky tu dau:", s[0])
print("Ky tu cuoi:", s[-1])
print("5 ky tu dau:", s[:5])


# TODO 2
print("Journey:", s[7:])
print("Dao nguoc:", s[::-1])
print("Moi ky tu thu 2:", s[::2])


# TODO 3
# Chi dung ma gia lap de thu bai, khong nhap CCCD that
cccd = input("Nhap chuoi 12 chu so gia lap: ")

if len(cccd) == 12 and cccd.isdigit():
    print("Ma tinh:", cccd[:2])
    print("Ma gioi tinh:", cccd[2])
    print("Nam sinh (2 so):", cccd[3:5])
else:
    print("Chuoi khong hop le")


# TODO 4
chuoi = input("Nhap chuoi: ").lower().replace(" ", "")

if chuoi == chuoi[::-1]:
    print(True)
else:
    print(False)
