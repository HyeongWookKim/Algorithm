# 단순 연결 구조의 Node 클래스
class Node:
    # 생성자 정의
    def __init__(self, elem, link = None): # 인수가 전달되지 않으면 link는 default 값으로 None이 됨
        self.data = elem # 데이터
        self.link = link # 링크

    # 새로운 node를 뒤에 추가하는 append(node) 연산
    def append(self, node):
        if node is not None:
            node.link = self.link
        self.link = node

    # 다음 node를 연결 구조에서 꺼내는 popNext() 연산
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    

# 단순 연결 구조의 List 클래스
class LinkedList:
    # 생성자 정의
    def __init__(self):
        self.head = None # 맨 처음에는 공백 상태가 되어야 하므로 head(헤더 포인터)는 None으로 초기화

    # 공백 상태 검사
    def isEmpty(self):
        return self.head == None # head 값이 None이면 공백
    
    # 포화 상태 검사
    # >> 연결된(Linked) 구조에서는 메모리만 남아 있다면, 언제든지 node 추가 가능
    # >> 따라서 포화 상태가 존재할 수 없음!
    def isFull(self):
        return False
    
    # pos번째 node를 반환하는 getNode(pos) 연산
    def getNode(self, pos):
        if pos < 0:
            return None # pos가 유효하지 않은 위치인 경우, None 반환
        
        ptr = self.head # 최초 시작 위치는 head
        for i in range(pos):
            if ptr == None: # pos 위치가 리스트의 크기보다 큰 경우, None 반환
                return None
            ptr = ptr.link # head node부터 link를 따라 pos번 이동하면 pos 위치의 node에 도착 (위치는 0부터 시작)
        return ptr # 최종 node 반환
    
    # pos번째 요소를 반환하는 getEntry(pos) 연산
    def getEntry(self, pos):
        node = self.getNode(pos) # pos 위치의 node
        if node == None: # 해당 node가 없는 경우(즉, 유효하지 않은 node인 경우), None 반환
            return None
        else:
            return node.data # 해당 node의 data 반환
        
    # pos 위치의 요소를 변경하는 replace() 연산
    def replace(self, pos, elem):
        node = self.getNode(pos) # pos 위치의 node
        if node != None:
            node.data = elem

    # 특정 요소를 갖고 있는 node를 찾는 find() 연산
    def find(self, val):
        node = self.head # node를 head node로 초기화
        while node is not None:
            if node.data == val: # 입력 받은 요소 값이 해당 node의 데이터와 일치하면, 해당 node 반환
                return node
            node = node.link # link를 따라 다음 node를 방문
        return node
        
    # pos 위치에 새로운 요소를 삽입하는 insert(pos, e) 연산
    def insert(self, pos, elem):
        node = Node(elem, None) # 삽입할 새로운 node 생성
        before = self.getNode(pos - 1) # 삽입할 위치 이전 node 탐색 (삽입 과정에서 변경되어야 하는 것은 pos - 1 위치 node의 link)
        
        # 삽입할 위치의 이전 node가 없다면, 리스트의 맨 앞에 추가해줘야 함
        if before == None:
            node.link = self.head # head node가 변경되었으니, head 포인터가 수정되어야 함! (node의 link가 head node를 가리킴)
            self.head = node # 이제 node가 head node가 됨

        else:
            before.append(node) # 삽입할 위치의 이전 node가 있으면 그냥 before 다음에 해당 node를 추가해주면 됨

    # pos 위치의 요소를 삭제하는 delete(pos) 연산
    def delete(self, pos):
        before = self.getNode(pos - 1) # 삭제할 위치 이전 node 탐색 (삭제 과정에서 변경되어야 하는 것은 pos - 1 위치 node의 link)
        
        # head node가 삭제되는 경우, head 포인터가 수정되어야 함!
        # 즉, head node가 삭제되면 head가 다음 node로 변경됨
        if before == None:
            if self.head is not None: # head가 공백 상태가 아니라면,
                self.head = self.head.link # head node 갱신
            return before # 삭제된 head node를 반환
        
        else:
            return before.popNext() # before의 다음 node 삭제
        
    # 전체 요소의 수를 구하는 size() 연산
    def size(self):
        # head node에서부터 link를 따라 전체 node를 방문하여 node의 개수를 탐색
        ptr = self.head
        count = 0
        while ptr is not None: # ptr이 None이면 중지하고 count 값 반환
            ptr = ptr.link
            count += 1
        return count
    
    # 리스트를 보기 좋게 화면에 출력하는 display() 연산
    def display(self, msg = 'LinkedList:'):
        print(msg, end = '')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->') # head node부터 link를 따라 None이 될 때까지 이동하면서 현재 node의 data를 출력
            ptr = ptr.link
        print('None')


### LinkedList와 파이썬 리스트 비교 ###
# >> 5개의 요소를 삽입하고, 하나의 요소를 교체한 후에 3개의 요소를 삭제하는 프로그램
# 1) 단순 연결 리스트(LinkedList) 사용
s = LinkedList()
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