# 이진 탐색 트리를 위한 노드 클래스
class BSTNode:
    def __init__(self, key, value):
        self.key = key # 키(key)
        self.value = value # 값(value): 키를 제외한 데이터 부분
        self.left = None  # 왼쪽 자식에 대한 링크
        self.right = None # 오른쪽 자식에 대한 링크

    def __str__(self):
        return f'({self.key}:{self.value})'
    

# 이진 탐색 트리의 탐색 연산 (순환 구조)
def search_bst(n, key): # n을 루트로 갖는 이진 탐색 트리에서 키 값이 key인 노드를 찾는 순환 함수
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key: # 탐색 키가 n의 key보다 작은 경우
        return search_bst(n.left, key) # 왼쪽 서브 트리 탐색
    else: # 탐색 키가 n의 key보다 큰 경우
        return search_bst(n.right, key) # 오른쪽 서브 트리 탐색
    

# 이진 탐색 트리의 값(value)을 이용한 탐색 (전위순회)
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    
    res = search_value_bst(n.left, value) # 왼쪽 서브 트리에서 탐색
    if res is not None:
        return res
    else: # 왼쪽 서브 트리에서 탐색 실패하면, 오른쪽 탐색 결과 반환
        return search_value_bst(n.right, value)
    

# 이진 탐색 트리의 삽입 연산
def insert_bst(root, node):
    if root == None: # 공백 노드에 도달하면, 해당 위치에 삽입
        return node
    
    if node.key == root.key: # 동일한 키는 허용하지 않음 -> root를 바로 반환
        return root
    
    if node.key < root.key: # 왼쪽 서브 트리에 넣어야 하는 경우, 순환 호출하고 left 갱신
        root.left = insert_bst(root.left, node)
    else: # 오른쪽 서브 트리에 넣어야 하는 경우, 순환 호출하고 right를 갱신
        root.right = insert_bst(root.right, node)

    return root # 루트 노트 반환


# 이진 탐색 트리의 삭제 연산
def delete_bst(root, key):
    if root == None:
        return None
    
    # key가 루트보다 작으면 왼쪽 서브 트리에서 삭제하고 left를 갱신
    if key < root.key:
        root.left = delete_bst(root.left, key)
    
    # key가 루트보다 크면 오른쪽 서브 트리에서 삭제하고 right를 갱신
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    # key가 루트와 같으면 root를 삭제
    else:
        # Case 1. 단말 노드 또는 Case 2. 오른쪽 자식만 있는 경우
        if root.left == None:
            return root.right # 삭제할 노드 위치에 오른쪽 자식을 끌어올림
        
        # Case 2. 왼쪽 자식만 있는 경우
        if root.right == None:
            return root.left # 삭제할 노드 위치에 왼쪽 자식을 끌어올림
        
        # Case 3. 두 자식이 모두 있는 경우
        # 후계자(오른쪽 서브 트리 최소 노드)를 찾고
        succ = root.right
        while succ.left != None:
            succ = succ.left 

        # 후계자의 데이터(key & value)를 복사하고
        root.key = succ.key
        root.value = succ.value

        # 후계자 삭제(오른쪽 서브 트리에서 후계자 키 값을 가진 노드를 순환 호출로 삭제)
        root.right = delete_bst(root.right, succ.key)

    return root

# 트리 구조 출력 (전위순회)
def preorder(n):
    if n is not None:
        print('{', end = ' ')
        print(n, end = ' ')
        preorder(n.left)
        preorder(n.right)
        print('}', end = ' ')


# 이진 탐색 트리의 테스트 프로그램
def print_node(msg, n): # 노드 출력
    print(msg, n if n != None else '탐색 실패')

def print_tree(msg, r): # 트리 출력
    print(msg, end = '')
    preorder(r)
    print()

data = [
    (6, '여섯'), (8, '여덟'), (2, '둘'), (4, '넷'), 
    (7, '일곱'), (5, '다섯'), (1, '하나'), (9, '아홉'), 
    (3, '셋'), (0, '영')
]

root = None # 루트 노드 생성 및 초기화
for i in range(0, len(data)): # 노드 순서대로 추가하기
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree('최초: ', root) # 최초의 트리 출력

# key를 이용한 탐색
n = search_bst(root, 3);          print_node('srch 3: ', n)
n = search_bst(root, 8);          print_node('srch 8: ', n)
n = search_bst(root, 0);          print_node('srch 0: ', n)
n = search_bst(root, 10);         print_node('srch10: ', n)
n = search_value_bst(root, '둘'); print_node('srch둘: ', n)
n = search_value_bst(root, '열'); print_node('srch열: ', n)

# 값(value)을 이용한 탐색
root = delete_bst(root, 7);     print_tree('del 7: ', root)
root = delete_bst(root, 8);     print_tree('del 8: ', root)
root = delete_bst(root, 2);     print_tree('del 2: ', root)
root = delete_bst(root, 6);     print_tree('del 6: ', root)