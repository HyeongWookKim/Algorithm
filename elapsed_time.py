# 세 개의 숫자 중, 가장 큰 값을 찾는 함수
def find_max(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

# 실행시간 측정
import time
st_time = time.time()
for _ in range(1000000):
    find_max(2, 1, 3)
end_time = time.time()
print(f'실행 시간: {end_time - st_time}')