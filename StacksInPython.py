# 1) 파이썬 리스트를 활용한 문자열 역순 출력
s = list()

msg = input('문자열 입력: ')
for m in msg:
    s.append(m)

print('문자열 출력: ', end = '')
while len(s) > 0:
    print(s.pop(), end = '')
print()


# 2) 파이썬 Queue 라이브러리를 활용한 문자열 역순 출력
import queue

s = queue.LifoQueue(maxsize = 100)

msg = input('문자열 입력: ')
for m in msg:
    s.put(m)

print('문자열 출력: ', end = '')
while not s.empty():
    print(s.get(), end = '')
print()