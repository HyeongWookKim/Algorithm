# 스택(LIFO)을 단순 연결 구조로 구현
class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None
    
    def push(self, item):
        self.top = Node(item, self.top)

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        
    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data