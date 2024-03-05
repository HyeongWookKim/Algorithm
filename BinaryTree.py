# 이진 트리 노드 클래스
# >> 이진 트리: 루트와 2개의 서브 트리로 구성되어 있으며, 서브 트리도 모두 이진 트리 (즉, 순환 조건)
class BTNode:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left # 왼쪽 자식을 위한 링크
        self.right = right # 오른쪽 자식을 위한 링크

    def isLeaf(self):
        return self.left is None and self.right is None


# 전위순회(preorder traversal): Root -> Left -> Right 순서
def preorder(n):
    if n is not None:
        print('(', end = ' ') # 중첩된 괄호 표현을 위한 출력
        print(n.data, end = ' ')
        preorder(n.left) # 왼쪽 서브 트리 처리
        preorder(n.right) # 오른쪽 서브 트리 처리
        print(')', end = ' ') # 중첩된 괄호 표현을 위한 출력

# 중위순회(inorder traversal): Left -> Root -> Right
def inorder(n):
    if n is not None:
        inorder(n.left) # 왼쪽 서브 트리 처리
        print(n.data, end = ' ')
        inorder(n.right) # 오른쪽 서브 트리 처리

# 후위순회(postorder traversal): Left -> Right -> Root
def postorder(n):
    if n is not None:
        postorder(n.left) # 왼쪽 서브 트리 처리
        postorder(n.right) # 오른쪽 서브 트리 처리
        print(n.data, end = ' ')

# 레벨순회(lever order): 루트의 레벨이 1이고 아래로 내려갈수록 레벨 증가
from ArrayQueue import *
def levelorder(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            # 왼쪽 -> 오른쪽 자식 순으로 넣기
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 이진 트리의 노드 수 구하기
def count_node(n):
    if n is None: # 공백인 트리면 0을 반환
        return 0
    else:
        # 순환 이용
        return count_node(n.left) + count_node(n.right) + 1 # 좌/우 서브 트리의 노드 수 합 + 1(=루트 노드)
    
# 이진 트리의 높이 구하기
def calc_height(n):
    if n is None: # 공백인 트리면 0을 반환
        return 0
    
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1 # 좌/우 서브 트리의 높이 중 더 큰 값 + 1


# 이진 트리 연산 테스트 프로그램
if __name__ == '__main__':
    d = BTNode('D', None, None)
    e = BTNode('E', None, None)
    b = BTNode('B', d, e)
    f = BTNode('F', None, None)
    c = BTNode('C', f, None)
    root = BTNode('A', b, c)

    print('\n In-Order : ', end = ''); inorder(root) # 중위순회
    print('\n Pre-Order : ', end = ''); preorder(root) # 전위순회
    print('\n Post-Order : ', end = ''); postorder(root) # 후위순회
    print('\n Level-Order : ', end = ''); levelorder(root) # 레벨순회
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 트리의 높이 = %d" % calc_height(root))