"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
# TODO: loop through 1..10, skip multiples of 3 and stop after 8.

print(remaining)
# Dem nguoc tu 5 ve 1
while remaining >= 1:
    print(remaining)
    remaining -= 1

# Bo qua so chia het cho 3 va dung sau so 8
number = 0

while number < 10:
    number += 1

    if number % 3 == 0:
        continue

    if number > 8:
        break

    print(number)

print(remaining)
