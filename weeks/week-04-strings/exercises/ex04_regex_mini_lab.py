"""Exercise 04: a small regular-expression lab."""

import re  # noqa: F401 — learner uses this import to complete the TODOs.

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# TODO 1: use re.findall and r"PJ-\d{3}" to extract both course codes.
codes: list[str] = []

# TODO 2: use re.search to find the first number sequence.
first_number = None

# TODO 3: use re.fullmatch to validate W followed by exactly two digits.
candidate = "W04"
is_week_code = False

print(codes)
print(first_number)
print(is_week_code)

import re

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# TODO 1
codes = re.findall(r"PJ-\d{3}", text)

# TODO 2
ket_qua = re.search(r"\d+", text)

if ket_qua:
    first_number = ket_qua.group()
else:
    first_number = None

# TODO 3
candidate = "W04"
is_week_code = bool(re.fullmatch(r"W\d{2}", candidate))

print(codes)
print(first_number)
print(is_week_code)
