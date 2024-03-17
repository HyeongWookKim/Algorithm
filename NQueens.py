# N-Queen 문제의 유효성 검사
def isSafe(board, x, y): # (x, y) 위치에 퀸을 놓을 수 있는지 검사하는 함수
    n = len(board)

    for i in range(y):
        if board[i][x] == 1:
            return False
        for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(y - 1, -1, -1), range(x + 1, n)):
            if board[i][j] == 1:
                return False
            
    return True

# N-Queen
def solve_N_Queen(board, y):
    '''
        board: 현재 보드
        y: 처리할 행 번호
    '''
    n = len(board)
    if y == n: # 모든 행을 이미 채운 경우, 하나의 해를 완성했으므로 출력
        printBoard(board)
        return
    
    for x in range(n): # 현재 행의 모들 열(x)에 대해, 유효하지 않으면 백트래킹 처리
        if isSafe(board, x, y):
            board[y][x] = 1
            solve_N_Queen(board, y + 1)
            board[y][x] = 0

# 4-Queen 테스트 결과 출력
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print('Q', end = ' ')
            else:
                print('.', end = ' ')
        print()
    print()


# N-Queen 테스트 프로그램
N = 4
board = [[0 for i in range(N)] for j in range(N)]
solve_N_Queen(board, 0)