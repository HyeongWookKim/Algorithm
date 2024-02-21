# 스택 클래스 정의
class ArrayStack:
    # 생성자 정의
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    # 스택 클래스의 연산
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print('Stack Overflow')
            exit()

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print('Stack Underflow')
            exit()
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print('Stack Underflow')
            exit()

    def size(self):
        return self.top + 1
    

if __name__ == '__main__':
    s = ArrayStack(100) # 스택 객체 생성

    msg = input('문자열 입력: ')
    for m in msg:
        s.push(m)

    print('문자열 출력: ', end = '')
    while not s.isEmpty():
        print(s.pop(), end = '')
    print()