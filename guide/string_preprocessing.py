from rapidfuzz.utils import default_process
from rapidfuzz import fuzz

text1 = "Hello World"
text2 = "hello world"
ratio = fuzz.ratio(text1, text2, processor=default_process)
print(f"전처리 후 유사도: {ratio}")