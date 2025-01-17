## RapidFuzz란?

RapidFuzz는 Levenshtein Distance 알고리즘을 활용해 문자열 유사도를 계산하는 Python 라이브러리입니다. C++로 개발되어 기존의 FuzzyWuzzy 라이브러리보다 훨씬 빠른 속도를 제공합니다.

## 주요 특징

1. **고성능**
   - C++로 구현되어 FuzzyWuzzy보다 최대 10배 이상 빠른 성능
   - 멀티스레딩 지원으로 대규모 데이터셋 처리 가능

2. **메모리 효율성**
   - 최적화된 메모리 사용으로 대용량 데이터 처리에 적합
   - 문자열 전처리 캐싱으로 반복 연산 최적화

3. **다양한 문자열 매칭 알고리즘**
   - Levenshtein Distance
   - Jaro-Winkler Distance
   - Longest Common Substring
   - 그 외 다수의 문자열 유사도 측정 알고리즘 지원

## 설치 방법

```bash
pip install rapidfuzz
```

## 사용 방법

### 1. 간단한 문자열 유사도 비교

```python
from rapidfuzz import fuzz

# 기본적인 문자열 유사도 계산
ratio = fuzz.ratio("hello world", "hello wold")
print(f"유사도: {ratio}")  # 출력: 유사도: 95.2380....

# 부분 문자열 매칭
partial_ratio = fuzz.partial_ratio("hello world", "world")
print(f"부분 유사도: {partial_ratio}")  # 출력: 부분 유사도: 100.0
```

### 2. 문자열 목록에서 가장 유사한 항목 찾기

```python
from rapidfuzz import process

choices = ["python programming", "java programming", "c++ programming", "javascript"]
query = "pythn programing"

# 가장 유사한 문자열 찾기
results = process.extract(query, choices, limit=len(choices))
for match, score, index in results:
    print(f"매칭: {match}, 점수: {score}")
```

### 3. 문자열 전처리

```python
from rapidfuzz.utils import default_process
from rapidfuzz import fuzz

# 대소문자 구분 없이 비교
text1 = "Hello World"
text2 = "hello world"
ratio = fuzz.ratio(text1, text2, processor=default_process)
print(f"전처리 후 유사도: {ratio}")  # 출력: 전처리 후 유사도: 100.0
```

## 사용 예제

### 1. 검색 엔진 개선

```python
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
```

### 2. 데이터 정제

```python
def clean_duplicate_entries(entries):
    unique_entries = []
    for entry in entries:
        # 유사도 90% 이상인 항목이 이미 있는지 확인
        matches = process.extract(entry, unique_entries, limit=1)
        if not matches or matches[0][1] < 90:
            unique_entries.append(entry)
    return unique_entries

data = ["신촌역", "신촌 역", "신촌역 (2호선)", "홍대입구역", "홍대 입구"]
cleaned_data = clean_duplicate_entries(data)
print("정제된 데이터:", cleaned_data)
```

## RapidFuzz의 모든 비교 알고리즘

### 1. Simple Ratio (fuzz.ratio)
기본적인 레벤슈타인 거리 기반 비교

```python
from rapidfuzz import fuzz

# 기본 비교
ratio = fuzz.ratio("hello world", "hello wold")  # 95.24
```

- **특징**: 전체 문자열을 정확히 비교
- **사용 사례**: 오타 교정, 비슷한 단어 찾기
- **시간 복잡도**: O(len1 * len2)

    
### 2. Partial Ratio (fuzz.partial_ratio)
더 짧은 문자열이 긴 문자열의 어느 부분과 가장 잘 매칭되는지 계산

```python
from rapidfuzz import fuzz

# 부분 문자열 매칭
ratio = fuzz.partial_ratio("hello world", "world")  # 100.0
```

- **특징**: 부분 문자열 매칭에 최적화
- **사용 사례**: 긴 텍스트 내 검색, 부분 매칭 필요 시
- **시간 복잡도**: O(len1 * min(len1, len2))


### 3. Token Sort Ratio (fuzz.token_sort_ratio)
단어들을 정렬 후 비교

```python
from rapidfuzz import fuzz

# 단어 순서 무관 비교
ratio = fuzz.token_sort_ratio("world hello", "hello world")  # 100.0
```

- **특징**: 단어 순서 무관한 비교
- **사용 사례**: 문장 유사도 비교, 키워드 매칭
- **시간 복잡도**: O(n log n) for sorting + O(len1 * len2) for comparison

### 4. Token Set Ratio (fuzz.token_set_ratio)
공통 토큰과 나머지 토큰을 분리하여 비교

```python
from rapidfuzz import fuzz

# 중복 단어 제거 후 비교
ratio = fuzz.token_set_ratio("hello hello world", "hello world")  # 100.0
```

- **특징**: 중복 단어 처리, 순서 무관
- **사용 사례**: 문서 유사도, 키워드 매칭
- **시간 복잡도**: O(n) for set operations + O(len1 * len2) for comparison

### 5. Partial Token Sort Ratio (fuzz.partial_token_sort_ratio)
Token Sort Ratio와 Partial Ratio의 조합

```python
from rapidfuzz import fuzz

# 정렬 후 부분 매칭
ratio = fuzz.partial_token_sort_ratio("hello world python", "world python")  # 100.0
```

- **특징**: 정렬 후 부분 매칭
- **사용 사례**: 긴 문장 내 키워드 검색
- **시간 복잡도**: O(n log n) + O(len1 * min(len1, len2))

### 6. Partial Token Set Ratio (fuzz.partial_token_set_ratio)
Token Set Ratio와 Partial Ratio의 조합

```python
from rapidfuzz import fuzz

# 중복 제거 후 부분 매칭
ratio = fuzz.partial_token_set_ratio("hello hello world python", "world python")  # 100.0
```

- **특징**: 중복 제거 후 부분 매칭
- **사용 사례**: 문서 내 키워드 검색
- **시간 복잡도**: O(n) + O(len1 * min(len1, len2))

### 7. WRatio (fuzz.WRatio)
가중치가 적용된 빠른 비교

```python
from rapidfuzz import fuzz

# 가중치 기반 비교
ratio = fuzz.WRatio("hello world", "hello wold")  # 95
```

- **특징**: 문자열 길이에 따른 가중치 적용
- **사용 사례**: 일반적인 문자열 비교
- **시간 복잡도**: Varies based on the string lengths

### 8. QRatio (fuzz.QRatio)
Quick Ratio - 빠른 비교

```python
from rapidfuzz import fuzz

# 빠른 비교
ratio = fuzz.QRatio("hello world", "hello wold")  # 95
```

- **특징**: 빠른 속도 우선
- **사용 사례**: 대량 데이터 처리
- **시간 복잡도**: O(min(len1, len2))


## 마치며

RapidFuzz는 강력한 성능과 다양한 기능을 제공하는 문자열 매칭 라이브러리입니다. 특히, 한글 데이터 처리에서도 뛰어난 성능을 발휘하여 한국어 기반의 데이터 처리에도 매우 적합합니다.

RapidFuzz에서 사용하는 문자열 비교 알고리즘은 다양한 상황에 맞게 활용할 수 있도록 설계되었습니다. 앞으로 이 알고리즘들에 대해 조금 더 깊이 공부하며, 각 비교 방식의 원리, 계산 방법, 그리고 특징에 대해 정리해 보려고 합니다. 이를 통해 RapidFuzz의 매칭 메커니즘을 더 잘 이해하고, 실무에서 효과적으로 활용할 수 있는 방법을 탐구해 보겠습니다.

## 참고 자료

- RapidFuzz 공식 문서: https://rapidfuzz.github.io/RapidFuzz
- GitHub 저장소: https://github.com/maxbachmann/RapidFuzz
- PyPI 페이지: https://pypi.org/project/rapidfuzz/