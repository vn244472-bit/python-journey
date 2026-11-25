"""Starter for the Week 05 Collection Workflow."""

tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]
tasks.append(("Practice unpacking", "todo"))

first_title, first_status = tasks[0]
print(f"first={first_title}, status={first_status}")

copied_tasks = tasks.copy()
tasks[1] = ("Observe mutability", "done")

print(f"current={tasks}")
print(f"copy={copied_tasks}")
"""Mini-project: Collection Workflow."""

tasks = [
    ("Learn lists", "done"),
    ("Observe mutability", "doing")
]

# Thêm công việc
tasks.append(("Practice unpacking", "todo"))

# Hiển thị công việc đầu tiên
first_title, first_status = tasks[0]
print(f"first={first_title}, status={first_status}")

# Cập nhật công việc
tasks[1] = ("Observe mutability", "done")

# Tạo bản copy
copied_tasks = tasks.copy()

# Xóa công việc cuối
tasks.pop()

print("Current:", tasks)
print("Copy:", copied_tasks)

# Kiểm tra alias và copy
alias_tasks = tasks
alias_tasks.append(("Learn Python", "doing"))

print("Alias:", alias_tasks)
print("Copy:", copied_tasks)