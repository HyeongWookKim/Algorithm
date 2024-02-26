# 원형 큐를 상속한 원형 덱 클래스 정의
from ArrayQueue import *

class CircularDeque(ArrayQueue):
    def __init__(self, capacity = 10):
        # 생성자는 상속되지 않기 때문에, 자식 클래스에서 다시 정의해야 함!
        super().__init__(capacity) # 부모 클래스의 데이터 초기화 (부모의 생성자 직접 호출)

    # 원형 큐와 동작이 동일한 연산
    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    # 원형 덱에 새로 추가된 연산
    def addFront(self, item):
        if not self.isFull():
            # 포화 상태가 아니면 front에 요소 삽입 후, front를 반시계 방향으로 회전
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def deleteRear(self):
        if not self.isEmpty():
            # 공백 상태가 아니면 rear 요소를 복사해 둔 뒤(반환해주기 위함), rear를 반시계 방향으로 회전 
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item # 후단 요소 반환
        else:
            pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear] # 후단 요소 반환
        else:
            pass

# 원형 덱의 테스트 프로그램
if __name__ == '__main__':
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0:
            dq.addRear(i)
        else:
            dq.addFront(i)
    dq.display('홀수는 전단(front), 짝수는 후단(rear) 삽입')

    for i in range(2):
        dq.deleteFront()
    for j in range(3):
        dq.deleteRear()
    dq.display('전단(front) 삭제 2번, 후단(rear) 삭제 3번')

    for k in range(9, 14):
        dq.addFront(k)
    dq.display('전단(front)에 9 ~ 13 삽입')