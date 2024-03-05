# 1. N-링크 표현을 위한 노드 클래스 (링크의 저장을 위해 연결 리스트 사용)
class N_Node:
    def __init__(self, elem):
        self.data = elem
        self.link = []
    
    def addChild(self, node):
        self.link.append(node)


# 2. 왼쪽 자식 - 오른쪽 형제 표현을 위한 노드 클래스
class CS_Node:
    def __init__(self, elem, child = None, sibling = None):
        self.data = elem
        self.child = child
        self.sibling = sibling


# 3. 이진 트리에서 단말(leaf) 노드의 수를 구하는 연산을 순환 구조를 이용해서 구현
def count_leaf(n):
    if n in None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)
    

# 4. 영어 대문자와 숫자 모스 코드에 대해 인코딩 및 디코딩 함수 구현 
# 영어 대문자와 숫자를 포함하는 모스 코드 표
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..'),
    ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
    ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
    ('8', '---..'), ('9', '----.')
]

class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

# 인코딩 함수
def encode(ch):
    idx = ord(ch.upper()) - ord('A')
    if 0 <= idx < 26: # 영어 대문자 (A ~ Z0)
        return table[idx][1]
    
    idx = ord(ch) - ord('0')
    if 0 <= idx < 10: # 숫자 (0 ~ 9)
        return table[26 + idx][1]

# 모스 코드 디코딩을 위한 결정 트리 만들기
def make_morse_tree():
    '''
        <작업 순서>
        1. 빈 루트 노드를 만들고, 모스 코드 표의 각 문자를 하나씩 트리에 추가
        2. 문자를 추가할 때, 루트부터 시작해서 트리를 타고 내려감
            - 만약 타고 내려갈 자식 노드가 None이면 새로운 노드 추가
            - 단, 노드만 추가할 뿐이지 그 노드의 문자는 아직 결정할 수 없음
        3. 마지막 코드의 노드에 도달하면, 해당 노드에 문자를 할당
    '''
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1] # 모스 코드
        node = root # 루트 노트부터 탐색 시작
        for c in code:
            # "."이 나타나면 왼쪽 자식으로 움직이고, "-"이 나타나면 오른쪽 자식으로 움직임
            if c == '.':
                if node.left == None:
                    node.left = TNode(None, None, None) # 왼쪽 자식이 비었으면 빈 노드 추가
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None, None, None) # 오른쪽 자식이 비었으면 빈 노드 추가
                node = node.right

        node.data = tp[0] # 최종 노드에 문자 할당
    return root

# 결정 트리를 이용한 디코딩 함수
def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data # 문자 반환


# 5. 중위표기 수식을 후위표기 수식으로 변환하는 방법 (스택 사용)
# 연산자의 우선순위 계산 함수
def precedence(op):
    if (op == '(' or op == ')'):
        return 0
    elif (op == '+' or op == '-'):
        return 1
    elif (op == '*' or op == '/'):
        return 2
    else:
        return -1
    
# 중위표기 수식을 후위표기 수식으로 변환
from StackClass import *
def infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
            
        else: # 피연산자
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output