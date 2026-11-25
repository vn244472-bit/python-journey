"""Starter for the Week 03 Decision Ticket."""

name = input("Tên: ").strip()
age_text = input("Tuổi: ").strip()
ticket_type = input("Loại vé (standard/vip): ").strip().lower()

if not name:
    print("Tên không được rỗng")
elif not age_text.isdigit():
    print("Tuổi cần là số nguyên không âm")
else:
    age = int(age_text)
    if age > 120 or ticket_type not in ("standard", "vip"):
        print("Input không hợp lệ")
    elif age < 12:
        print(f"{name}: vé trẻ em")
    elif ticket_type == "vip":
        print(f"{name}: vé VIP")
    else:
        print(f"{name}: vé standard")

print("===== DECISION TICKET =====")

name = input("Ten: ").strip()
age_text = input("Tuoi: ").strip()
ticket_type = input("Loai ve (standard/vip): ").strip().lower()

if not name:
    print("Ten khong duoc rong")
elif not age_text.isdigit():
    print("Tuoi can la so nguyen khong am")
elif ticket_type not in ("standard", "vip"):
    print("Loai ve khong hop le")
else:
    age = int(age_text)

    if age > 120:
        print("Tuoi khong hop le")
    else:
        if ticket_type == "vip":
            price = 120000
        else:
            price = 80000

        if age < 12:
            price *= 0.5

        print("Ten:", name)
        print("Loai ve:", ticket_type)
        print("Gia ve:", int(price), "VND")
