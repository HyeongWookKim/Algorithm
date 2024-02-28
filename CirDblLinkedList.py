# 이중 원형 연결 구조로 리스트 구현
class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next


class CirDblLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def insert(self, pos, elem):
        if self.isEmpty(): # 공백 상태면 무조건 맨 앞에 추가
            self.head = Node(elem)
            self.head.prev = self.head.next = self.head

        else:
            p = self.getNode(pos)
            node = Node(elem, p.prev, p)
            node.prev.next = node
            node.next.prev = node
            if pos == 0:
                self.head = node
    
    def delete(self, pos):
        if self.isEmpty():
            return None
        
        p = self.getNode(pos)
        if p == None:
            return None
        
        data = p.data # 반환할 자료

        if self.head.next == self.head: # 요소가 하나뿐인 경우
            self.head = None
        else:
            p.prev.next = p.next
            p.next.prev = p.prev
            if p == self.head:
                self.head = p.next

        return data