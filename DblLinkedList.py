# 이중 연결 구조의 List 클래스
# 이중 연결 구조를 위한 DNode 클래스
class DNode:
    # 생성자 정의
    def __init__(self, elem, next = None, prev = None):
        self.data = elem
        self.next = next # 다음 node를 위한 link
        self.prev = prev # 이전 node를 위한 link

    # 새로운 node를 추가하는 append() 연산
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None: # self의 다음 node가 있으면,
                node.next.prev = node # 해당 node의 이전 node는 node
        self.next = node

    # 다음 node를 연결 구조에서 꺼내는 popNext() 연산
    def popNext(self):
        node = self.next # 삭제할 node
        if node is not None:
            self.next = node.next
            if self.next is not None: # self의 next가 있으면,
                self.next.prev = self # 해당 node의 이전 node는 self
        return node
    

# 이중 연결 List 클래스
class DblLinkedList:
    # 생성자 정의
    def __init__(self):
        self.head = None # head node를 가리키는 head 값을 None으로 초기화

    # 공백 상태 검사
    def isEmpty(self):
        return self.head == None
    
    # 포화 상태 검사
    # >> 연결된(Linked) 구조에서는 포화 상태가 존재할 수 없음!
    def isFull(self):
        return False
    
    # 전체 요소의 개수
    def size(self):
        ptr = self.head # ptr은 head node에서 시작
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count
    
    # DblLinkedList 연산을 화면에 출력
    def display(self, msg = 'DblLinkedList:'):
        print(msg, end = '')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '<=>')
            ptr = ptr.next
        print('None')

    # pos번째 node 추출
    def getNode(self, pos):
        if pos < 0: # 유효하지 않은 pos 위치인 경우, None 반환
            return None
        ptr = self.head
        for i in range(pos):
            if ptr == None: # pos가 리스트 크기보다 큰 경우, None 반환
                return None
            ptr = ptr.next
        return ptr
    
    # pos번째 요소를 반환
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 node
        if node == None:
            return None
        else:
            return node.data
        
    # pos 위치의 요소 변경
    def replace(self, pos, elem):
        node = self.getNode(pos) # pos 위치의 node
        if node != None:
            node.data = elem

    # 특정 요소를 갖고 있는 node 탐색
    def find(self, val):
        node = self.head # node를 head node로 초기화
        while node is not None:
            if node.data == val: # 입력 받은 요소 값이 해당 node의 데이터와 일치하면, 해당 node 반환
                return node
            node = node.next # link(=next)를 따라 다음 node를 방문
        return node
    
    # pos 위치에 새로운 요소를 삽입
    def insert(self, pos, elem):
        node = DNode(elem)
        before = self.getNode(pos - 1) # 삽입할 위치 이전 node 탐색
        if before == None: # head node로 삽입하는 경우
            node.next = self.head # node의 link가 head node를 가리킴
            if node.next is not None: # node 다음 node가 있으면,
                node.next.prev = node # 해당 node의 이전 node는 node
            self.head = node # node가 head node가 됨
        else:
            before.append(node)

    # pos 위치의 요소 삭제
    def delete(self, pos):
        before = self.getNode(pos - 1) # 삭제할 위치 이전 node 탐색
        if before == None: # head node를 삭제하는 경우
            # head node를 삭제하면, head가 다음 node로 변경됨
            if self.head is not None:
                self.head = self.head.next # head node 갱신
                self.head.prev = None # head node는 이전 node가 존재하지 않음
        else:
            before.popNext()


### LinkedList와 파이썬 리스트 비교 ###
# >> 5개의 요소를 삽입하고, 하나의 요소를 교체한 후에 3개의 요소를 삭제하는 프로그램
# 1) 이중 연결 리스트(DblLinkedList) 사용
s = DblLinkedList()
s.display('연결 리스트(초기): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display('연결 리스트(삽입 x 5): ')
s.replace(2, 90)
s.display('연결 리스트(교체 x 1): ')
s.delete(2)
s.delete(3)
s.delete(0)
s.display('연결 리스트(삭제 x 3): ')

# 2) 파이썬 리스트 사용
l = []
print('파이썬 리스트(초기):', l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print('파이썬 리스트(삽입 x 5):', l)
l[2] = 90
print('파이썬 리스트(교체 x 1):', l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬 리스트(삭제 x 3):', l)