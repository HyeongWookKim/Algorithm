# 영어 대문자에 대한 모스 코드 표
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..') 
]

class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

# 모스 코드 인코딩 함수
def encode(ch):
    idx = ord(ch.upper()) - ord('A') # table 리스트에서 입력 받은 문자가 위치한 인덱스 찾기
    return  table[idx][1]

# 단순한 방법의 모스 코드 디코딩 함수 (비효율적)
def decode_simple(morse):
    for tp in table:
        if morse == tp[1]:
            return tp[0]
        
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


# 모스 코드 인코딩과 디코딩 테스트 프로그램
morseCodeTree = make_morse_tree() # 모스 코드 결정 트리 생성 (루트 노트가 생성됨)
input_str = input('입력 문장: ')
mlist = []
for ch in input_str:
    code = encode(ch) # 입력 받은 문장을 모스 코드로 변환 (인코딩)
    mlist.append(code)

print(f'Morse Code: {mlist}')
print('Decoding: ', end = '')

for code in mlist:
    ch = decode(morseCodeTree, code) # 리스트의 모스 코드를 순서대로 문자로 변환 (디코딩)
    print(ch, end = '')
print()