# x의 n 거듭제곱 구하기(억지 기법)
def slow_power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

# x의 거듭제곱 구하기(축소 정복)
def power(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)
    

# x의 n 거듭제곱 테스트 프로그램
import time
print('억지기법(2 ** 500) =', slow_power(2.0, 500))
print('축소 정복 기법(2 ** 500) =', power(2.0, 500))

t1 = time.time()

for i in range(100000):
    slow_power(2.0, 500) # 억지 기법 10만회

t2 = time.time()

for i in range(100000):
    power(2.0, 500) # 축소 정복 10만회 

t3 = time.time()

print('억지 기법 시간:', t2 - t1)
print('축소 정복 기법 시간:', t3 - t2)