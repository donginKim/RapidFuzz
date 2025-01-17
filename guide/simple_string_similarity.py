from rapidfuzz import fuzz

ratio = fuzz.ratio("hello world", "hello wold")
print(f"유사도: {ratio}")

partial_ratio = fuzz.partial_ratio("hello world", "world")
print(f"부분 유사도: {partial_ratio}")