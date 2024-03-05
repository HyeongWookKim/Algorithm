# 수식 트리: 산술식을 트리 형태로 표현한 이진 트리
# >> 하나의 연산자가 2개의 피연산자를 갖는다고 가정함
# >> 피연산자는 단말(leaf) 노드에 저장되고, 연산자는 루트나 가지 노드에 배치
# >> 자식을 먼저 처리해야 부모 노드를 처리할 수 있기 때문에, 후위순회(postorder traversal)가 사용됨
from BinaryTree import *

# 수식 트리 계산 함수
def evaluate(node):
    if node is None: # 공백인 트리라면 0을 반환
        return 0
    
    elif node.isLeaf(): # 단말(leaf) 노드이면 피연산자에 해당
        return node.data
    
    else: # 루트나 가지 노드라면 연산자에 해당
        op1 = evaluate(node.left) # 왼쪽 서브 트리 계산
        op2 = evaluate(node.right) # 오른쪽 서브 트리 계산
        
        if node.data == '+':
            return op1 + op2
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2
        
# 후위표기 수식을 이용한 수식 트리 만들기
def buildETree(expr): # 후위표기 수식을 입력 받음 -> ex) ['1', '3', '+', '4', '2', '/', '*']
    if len(expr) == 0:
        return None

    # 후위순회는 수식을 뒤에서 앞으로 처리함
    # 따라서 pop()로 맨 뒤 요소를 꺼냄
    token = expr.pop()
    if token in '+-*/': # 연산자인 경우, 노드 생성
        node = BTNode(token)
        # 반드시 오른쪽 자식부터 처리하고, 그 다음에 왼쪽 자식 순으로 처리해줘야 함
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else: # 피연산자(즉, 단말 노드)인 경우, 노드를 만들어서 바로 반환
        return BTNode(float(token))
    
# 전위표기 수식을 이용해서 수식 트리를 만들고 루트를 반환하기
def buildETree2(expr):
    if len(expr) == 0:
        return None
    
    # 전위순회는 수식을 앞에서 뒤로 처리함
    # 따라서 pop(0)으로 첫 번째 요소를 꺼냄
    token = expr.pop(0)
    if token in '+-*/': # 연산자인 경우, 노드 생성
        node = BTNode(token)
        # 후위순회와 반대로, "왼쪽 자식 -> 오른쪽 자식" 순으로 처리해줘야 함
        node.left = buildETree2(expr)
        node.right = buildETree2(expr)
        return node
    else: # 피연산자(즉, 단말 노드)인 경우, 노드를 만들어서 바로 반환
        return BTNode(float(token))


# 수식 트리 테스트 프로그램
if __name__ == '__main__':
    input_str = input('입력(후위표기): ')
    expr = input_str.split() # 입력 받은 문자를 토큰 리스트로 변환
    print(f'토큰 분리(expr): {expr}')
    
    root = buildETree(expr) # 후위표기 수식을 수식 트리로 생성하고 루트 반환
    print('\n전위 순회: ', end = ''); preorder(root)
    print('\n중위 순회: ', end = ''); inorder(root)
    print('\n후위 순회: ', end = ''); postorder(root)
    print('\n계산 결과 : ', evaluate(root))	# 수식 트리 계산