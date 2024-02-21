# 1) 반복 구조의 팩토리얼 함수
def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result *= k # result에 반복적으로 곱하기
    return result


# 2) 순환 구조의 팩토리얼 함수
def factorial(n):
    if n == 1: # 종료 조건: 순환을 멈추는 부분
        return 1
    else:
        return n * factorial(n - 1) # 자기 자신을 순환적으로 호출
    

print('Factorial - 순환(3) = ', factorial(3))
print('Factorial - 반복(3) = ', factorial_iter(3))

print('Factorial - 순환(10) = ', factorial(10))
print('Factorial - 반복(10) = ', factorial_iter(10))