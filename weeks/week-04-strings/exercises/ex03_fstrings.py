"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
ten = "An"
tuoi = 20
diem = 8.567


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50


# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/phải
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%

# TODO 1
ten = "An"
tuoi = 20
diem = 8.567

print(f"Hoc sinh {ten}, {tuoi} tuoi, diem TB: {diem:.2f}")


# TODO 2
for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>3}")


# TODO 3
print("=" * 35)
print(f"{'SAN PHAM':<20}{'GIA (VND)':>15}")
print("-" * 35)

san_pham = [
    ("Ca phe", 35000),
    ("Banh mi", 25000),
    ("Nuoc suoi", 10000)
]

tong = 0

for ten, gia in san_pham:
    print(f"{ten:<20}{gia:>15,}")
    tong += gia

print("-" * 35)
print(f"{'TONG CONG':<20}{tong:>15,}")
print("=" * 35)


# TODO 4
phan_tram = int(input("Nhap phan tram (0-100): "))

if 0 <= phan_tram <= 100:
    so_o_day = phan_tram // 5
    thanh = "█" * so_o_day
    trong = "░" * (20 - so_o_day)

    print(f"[{thanh}{trong}] {phan_tram}%")
else:
    print("Phan tram khong hop le")
