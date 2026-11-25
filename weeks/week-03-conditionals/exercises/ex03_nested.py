"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng

# TODO 1: Mo phong ATM
so_du = float(input("Nhap so du: "))
so_tien = float(input("Nhap so tien muon rut: "))

if so_tien <= 0:
    print("So tien khong hop le")
elif so_tien > so_du:
    print("Khong du so du")
elif so_tien % 50000 != 0:
    print("So tien phai la boi so cua 50000")
else:
    print("Rut tien thanh cong")
    print("So du con lai:", so_du - so_tien)


# TODO 2: Tinh BMI tham khao
# BMI khong duoc dung de tu ket luan tinh trang suc khoe,
# dac biet voi nguoi dang trong do tuoi phat trien.
chieu_cao = float(input("Nhap chieu cao (m): "))
can_nang = float(input("Nhap can nang (kg): "))

if chieu_cao <= 0 or can_nang <= 0:
    print("Du lieu khong hop le")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print("Chi so BMI tham khao:", round(bmi, 2))
    print("Can duoc danh gia suc khoe boi nguoi co chuyen mon.")


# TODO 3: May ban ve xem phim
loai_ve = input("Loai ve (thuong/vip): ").lower()
ngay = input("Ngay (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Nhap tuoi: "))

if loai_ve not in ("thuong", "vip"):
    print("Loai ve khong hop le")
elif ngay not in ("thuong", "cuoi_tuan"):
    print("Ngay khong hop le")
elif tuoi < 0:
    print("Tuoi khong hop le")
else:
    if loai_ve == "vip":
        gia = 120000
    else:
        gia = 80000

    if ngay == "cuoi_tuan":
        gia = gia * 1.3

    if tuoi < 12 or tuoi >= 65:
        gia = gia * 0.5
    elif 18 <= tuoi <= 25:
        gia = gia * 0.8

    print("Gia ve:", int(gia), "VND")
