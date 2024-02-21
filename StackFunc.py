# 스택을 위한 데이터
capacity = 10 # 스택으로 담아줄 용량
array = [None] * capacity # 요소 배열
top = -1 # top 위치의 index를 -1로 초기화

# 스택의 공백 상태 검사
def isEmpty():
    if top == -1:
        return True
    else:
        return False
    
# 스택의 포화 상태 검사
def isFull():
    return top == capacity - 1 # 포화 상태: top = capacity - 1

# 스택의 삽입 연산
def push(e):
    global top
    if not isFull(): # 포화 상태가 아닌 경우
        top += 1
        array[top] = e
    else:
        print('Stack Overflow') # 포화 상태 (더 이상 채울 수 없음)
        exit()

# 스택의 삭제 연산
def pop():
    global top
    if not isEmpty(): # 공백 상태가 아닌 경우
        top -= 1
        return array[top + 1] # 이전 위치(top + 1)의 요소 반환
    else:
        print('Stack Underflow') # 공백 상태 (더 이상 빼낼 수 없음)
        exit()

# 스택의 peek() 연산 -> peek: 스택의 맨 위에 있는 항목을 삭제하지 않고 반환
def peek():
    if not isEmpty(): # 공백 상태가 아닌 경우
        return array[top]
    else:
        pass # Stack Underflow 예외처리 X

# 스택의 size() 연산 -> size: capacity와 같은 의미
def size():
    return top + 1


if __name__ == '__main__':
    msg = input('문자열 입력: ')
    for m in msg:
        push(m)

    print('문자열 출력: ', end = '')
    while not isEmpty():
        print(pop(), end = '')
    print()