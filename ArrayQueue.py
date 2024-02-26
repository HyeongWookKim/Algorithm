# 원형 큐 클래스 정의 (1)
class ArrayQueue:
    def __init__(self, capacity = 10): # capacity 기본 값을 10으로 지정
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0 # 맨 처음 큐는 공백이 되어야 하므로, front는 0으로 초기화
        self.rear = 0 # 맨 처음 큐는 공백이 되어야 하므로, rear는 0으로 초기화

    # 공백 상태 검사
    def isEmpty(self):
        return self.front == self.rear
    
    # 포화 상태 검사
    # >> front = rear 인 경우를 포화 상태로 보면, 공백 상태와 겹침
    # >> 따라서 한 자리를 비워두는 방식 적용 -> 즉, front가 rear의 바로 다음에 있으면 포화 상태
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    # 삽입 연산
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity # rear를 시계 방향으로 한 칸 회전
            self.array[self.rear] = item # 회전한 위치에 새로운 요소 복사

        else:
            pass # Overflow 오류 처리 안 함

    # 삭제 연산
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

        else:
            pass # Underflow 오류 처리 안 함

    # 상단 들여다보기 연산
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

        else:
            pass # Underflow 오류 처리 안 함

    # 전체 요소의 수
    def size(self):
        # 선형 큐라면 전체 요소의 수는 "rear - front"인데, 원형 큐에서는 "rear - front" 값이 음수가 나올 수 있음
        # 따라서 "rear - front" 값이 음수인 경우, 추가로 capacity 값을 더해서 양수로 만들어줘야 함
        return (self.rear - self.front + self.capacity) % self.capacity
    
    # 전체 요소를 화면으로 출력
    def display(self, msg):
        print(msg, end = '= [')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end = ' ')
            print(']')

    
# 원형 큐의 동작 확인 테스트 프로그램
import random
if __name__ == '__main__':
    q = ArrayQueue(8)

    q.display('초기 상태')
    while not q.isFull(): # 큐가 포화 상태가 될 때까지 while문 실행
        q.enqueue(random.randint(0, 100))
    q.display('포화 상태')

    print('삭제 순서: ', end = '')
    while not q.isEmpty(): # 큐가 공백 상태가 될 때까지 while문 실행
        print(q.dequeue(), end = ' ')
    print()