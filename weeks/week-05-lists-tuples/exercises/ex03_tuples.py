"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x = 0
y = 0

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("", 0, "")

# TODO: swap left and right using unpacking.
left = "A"
right = "B"

print(x, y, profile, left, right)
"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# Unpacking
x, y = coordinate

# Packing tuple
profile = ("An", 20, "Python")

# Unpacking profile
name, age, topic = profile

# Hoán đổi giá trị
left = "A"
right = "B"

left, right = right, left

print("Toa do:", x, y)
print("Ho so:", name, age, topic)
print("Left:", left)
print("Right:", right)