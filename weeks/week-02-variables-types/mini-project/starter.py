
"""
Mini-project: The sinh vien - Week 02
"""

# TODO 1: Nhap thong tin sinh vien
name = input("Ho ten: ").strip()
student_id = input("Ma sinh vien: ").strip()
major = input("Nganh hoc: ").strip()
start_year_text = input("Nam nhap hoc: ").strip()

# TODO 2: Kiem tra nam nhap hoc
if start_year_text.isdigit():

    # TODO 3: Chuyen sang int
    start_year = int(start_year_text)

    # TODO 4: Tinh nam tot nghiep
    graduation_year = start_year + 4

    # TODO 5: In the sinh vien
    print("\n" + "=" * 35)
    print("         THE SINH VIEN")
    print("=" * 35)
    print(f"Ho ten: {name}")
    print(f"Ma sinh vien: {student_id}")
    print(f"Nganh hoc: {major}")
    print(f"Khoa: {start_year} - {graduation_year}")
    print("=" * 35)

else:
    print("Nam nhap hoc can gom cac chu so!")
