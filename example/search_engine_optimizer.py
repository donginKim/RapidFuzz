from rapidfuzz import process, fuzz

def search_products(query, product_list):
    return process.extract(
        query,
        product_list,
        scorer=fuzz.partial_ratio,
        limit=5
    )

products = [
    "아이폰 13 프로",
    "갤럭시 S22 울트라",
    "아이폰 12",
    "갤럭시 S21"
]

results = search_products("아이폰", products)
for product, score, _ in results:
    print(f"제품: {product}, 매칭 점수: {score}")