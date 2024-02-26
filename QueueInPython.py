# 파이썬 queue 모듈 사용
import queue
import random

q = queue.Queue(maxsize = 8) # maxsize = capacity (maxsize = 0이면, size가 용량의 제한이 없는 무한대를 의미함)

print('삽입 순서: ', end = '')
while not q.full():
    v = random.randint(0, 100) # 난수 생성 (0 ~ 100)
    q.put(v) # 삽입
    print(v, end = ' ')
print()

print('삭제 순서: ', end = '')
while not q.empty():
    print(q.get(), end = ' ')
print()


# 파이썬 collections 모듈의 deque 클래스 사용
import collections

dq = collections.deque() # 용량이 "무한대"인 덱 객체 생성

print('덱은 공백 상태가 아님' if dq else '덱은 공백 상태임') # dq에 값이 존재하는 경우, True 반환
for i in range(9):
    # 짝수면 후단(rear), 홀수면 전단(front)으로 삽입
    if i % 2 == 0:
        dq.append(i)
    else:
        dq.appendleft(i)
print('홀수는 전단(front), 짝수는 후단(rear)으로 삽입', dq)

for j in range(2):
    dq.popleft() # 전단(front) 삭제
for k in range(3):
    dq.pop() # 후단(rear) 삭제
print('전단(front) 삭제 2번, 후단(rear) 삭제 3번', dq)

for l in range(9, 14):
    dq.appendleft(l)
print('전단(front)에 9 ~ 13 삽입        ', dq)

print('덱은 공백 상태가 아님' if dq else '덱은 공백 상태임')