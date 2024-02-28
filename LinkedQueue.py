# 큐(FIFO)를 단순 연결 구조로 구현
class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None
    
    def isFull(self):
        return False
    
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.link
            return data
        
    def peek(self):
        if not self.isEmpty():
            return self.front.data