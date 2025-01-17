from rapidfuzz import process

def clean_duplicate_entries(entries):
    unique_entries = []
    for entry in entries:
        
        matches = process.extract(entry, unique_entries, limit=1)
        if not matches or matches[0][1] < 90:
            unique_entries.append(entry)
    return unique_entries

data = ["신촌역", "신촌 역", "신촌역 (2호선)", "홍대입구역", "홍대 입구"]
cleaned_data = clean_duplicate_entries(data)
print("정제된 데이터:", cleaned_data)