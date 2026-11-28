"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
# TODO: print each topic with a one-based position using enumerate.
# TODO: pair topics and scores with zip(..., strict=True).

print(topics, scores)
# In cac so tu 1 den 5
for number in range(1, 6):
    print(number)

# In chu de kem so thu tu
for index, topic in enumerate(topics, start=1):
    print(index, topic)

# Ket hop topics va scores
for topic, score in zip(topics, scores, strict=True):
    print(topic, score)

print(topics, scores)
