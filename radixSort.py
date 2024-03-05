# 기수(숫자의 자릿수) 정렬 알고리즘
# >> 값들을 적절히 "배분"해 놓았다가 순서대로 다시 모으는 것
# >> 이를 위해 여러 개의 버킷(bucket)을 사용하는데, 큐(queue) 구조를 활용함
from collections import deque

def radix_sort(arr, buckets, digits):
    queues = []
    # 입력 받은 bucket 개수만큼 큐(덱)를 만들어서 리스트에 추가
    # >> ex) buckets = 10인 경우는 10진법을 사용한다는 것을 의미하므로, 0 ~ 9까지 총 10개의 버킷(bucket) 생성
    for i in range(buckets):
        queues.append(deque())

    n = len(arr)
    factor = 1 # 가장 낮은 자릿수부터 시작

    for d in range(digits): # 각 자릿수에 대해 처리
        # 모든 항목을 따라 큐(덱)에 삽입
        for i in range(n):
            queues[(arr[i] // factor) % buckets].append(arr[i])

        # 0번부터 모든 버킷(bucket)에 저장된 요소를 순서대로 꺼내서, 입력 리스트 arr에 다시 저장
        i = 0
        for b in range(buckets):
            while queues[b]:
                arr[i] = queues[b].popleft() # FIFO
                i += 1
        factor *= buckets # 그 다음 자릿수로 이동
        print(f'Step {d + 1} = {arr}')


# 기수 정렬 테스트 프로그램
import random

buckets = 10 # 10진법 사용
digits = 4 # 최대 4자릿수 숫자를 정렬

data = [random.randint(1, 9999) for _ in range(10)]
radix_sort(data, buckets, digits)
print(f'Radix Sort: {data}')