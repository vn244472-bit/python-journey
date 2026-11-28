"""Starter for the Week 06 Iteration Report."""

topics = ["loops", "enumerate", "zip", "comprehensions"]
scores = [8, 9, 8, 7]

for position, (topic, score) in enumerate(
    zip(topics, scores, strict=True), start=1
):
    print(f"{position}. {topic}: {score}")

strong_scores = [score for score in scores if score >= 8]
print(f"strong_scores={strong_scores}")
# Tinh diem trung binh
average = sum(scores) / len(scores)

# Tim diem cao nhat
highest_score = max(scores)

# Dem so chu de dat tu 8 diem
strong_count = len(strong_scores)

print("--------------------")
print(f"Strong scores: {strong_scores}")
print(f"Average score: {average}")
print(f"Highest score: {highest_score}")
print(f"Strong topics: {strong_count}")
