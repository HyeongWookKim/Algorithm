# 피보나치 수열(분할 정복)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2) # 분할과 병합

# 행렬 거듭제곱을 이용한 피보나치 수열
from powerMat import *
def fib_mat(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 초기 피보나치 행렬
    mat = [[1, 1], 
           [1, 0]]
    result = powerMat(mat, n) # 축소 정복 방식
    return result[0][1] # fib(n) 부분을 반환 -> result[1][0]을 반환해도 동일함


# 피보나치 수열 테스트 프로그램
n = 31
print(f'Fibonacci({n}) 거듭제곱 = {fib_mat(n)}')
print(f'Fibonacci({n}) 분할 정복 = {fib(n)}')