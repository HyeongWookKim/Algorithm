# 너비 우선 탐색 (인접 리스트 방식)
from queue import Queue
def BFS_AL(vtx, aList, s):
    '''
        vtx: 정점(vertex) 리스트
        aList: 인접 리스트 (각 정점이 인접한 정점 리스트를 갖도록 하여 간선들을 표현한 리스트)
        s: 시작 정점
        visited: 정점 방분 여부 기록 리스트 (정점 리스트와 길이 동일함)
    '''
    n = len(vtx)
    visited = [False] * n

    # 큐를 생성하고, 맨 처음에 시작 정점 s만 큐에 삽입 후에 s는 방문했다고 표기
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty(): # 큐가 공백 상태가 될 때까지 반복
        s = q.get() # 큐에서 정점(vertex) 꺼내기
        print(vtx[s], end = ' ')
        for v in aList[s]:
            if visited[v] == False:
                q.put(v) # 아직 방문하지 않은 정점들을 모두 큐에 삽입
                visited[v] = True # 삽입 후에는 방문했다고 표기


# 너비 우선 탐색 테스트 프로그램
vtx = ['U','V','W','X','Y']
aList = [[1, 2], 
         [0, 2, 3],
         [0, 1, 4],
         [1],
         [2]]

print('BFS_AL(출발: U): ', end = '')
BFS_AL(vtx, aList, 0)
print()