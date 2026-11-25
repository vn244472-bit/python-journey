"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
# TODO: update the first subject.
# TODO: remove one known subject and pop the last subject.
# TODO: print the first, last and middle slice after each safe operation.

print(subjects)
"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# Thêm phần tử
subjects.append("Tin")
subjects.insert(1, "Lý")

# Cập nhật phần tử đầu tiên
subjects[0] = "Toán học"

# Xóa phần tử
subjects.remove("Văn")
subjects.pop()

# In kết quả
print("Danh sach:", subjects)
print("Phan tu dau:", subjects[0])
print("Phan tu cuoi:", subjects[-1])
print("Phan tu o giua:", subjects[1:3])