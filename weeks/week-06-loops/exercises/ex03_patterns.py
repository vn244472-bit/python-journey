"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# TODO: build squares for all numbers.
squares: list[int] = []
# TODO: build even_numbers with one filter.
even_numbers: list[int] = []
# TODO: rewrite one comprehension as a normal loop and compare readability.

print(squares, even_numbers)
# Tao danh sach binh phuong
squares: list[int] = [number ** 2 for number in numbers]

# Loc cac so chan
even_numbers: list[int] = [
    number for number in numbers if number % 2 == 0
]

# Viet lai bang vong lap thong thuong
even_numbers_loop: list[int] = []

for number in numbers:
    if number % 2 == 0:
        even_numbers_loop.append(number)

print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Even numbers using loop:", even_numbers_loop)
