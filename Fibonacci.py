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

# Memoization(메모이제이션)을 이용한 피보나치 수열
def fib_dp_mem(n):
    if mem[n] == None: # 처음 푸는 문제면, 문제를 푼 뒤에 메모리에 저장
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n - 1) + fib_dp_mem(n - 2)
    return mem[n] # 저장된 답을 반환

# Tabulation(테이블화)을 이용한 피보나치 수열
def fib_dp_tab(n):
    # 답을 저장할 테이블을 만들고, 알려진 답을 저장 (나머지는 모두 None으로 초기화)
    f = [None] * (n + 1)
    f[0] = 0
    f[1] = 1
    
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# 피보나치 수열(반복 구조)
def fib_iter(n):
    if n < 2:
        return n
    
    last = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += last
        last = tmp
    return current


# 피보나치 수열 테스트 프로그램
n1 = 31
print(f'Fibonacci({n1}) 거듭제곱 = {fib_mat(n1)}')
print(f'Fibonacci({n1}) 분할 정복 = {fib(n1)}')

n2 = 8
mem = [None] * (n2 + 1)
print('Fibonacci(%d) 메모이제이션 = '%n2, fib_dp_mem(n2))
print('Fibonacci(%d) 반복 구조 = '%n2, fib_iter(n2))