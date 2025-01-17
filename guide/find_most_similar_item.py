from rapidfuzz import process

choices = ["python programming", "java programming", "c++ programming", "javascript"]
query = "pythn programing"

results = process.extract(query, choices, limit=len(choices))
for match, score, index in results:
    print(f"매칭: {match}, 점수: {score}")