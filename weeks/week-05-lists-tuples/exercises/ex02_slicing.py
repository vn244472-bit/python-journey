"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = []
last_three: list[int] = []

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = []
copied: list[int] = []

# TODO: append through alias and explain which lists change.
print(first_three, last_three, alias, copied)
"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# Lấy 3 phần tử đầu và 3 phần tử cuối
first_three = numbers[:3]
last_three = numbers[-3:]

# Alias và copy
alias = numbers
copied = numbers.copy()

# Thêm phần tử thông qua alias
alias.append(7)

print("Danh sach ban dau:", numbers)
print("3 phan tu dau:", first_three)
print("3 phan tu cuoi:", last_three)
print("Alias:", alias)
print("Copy:", copied)