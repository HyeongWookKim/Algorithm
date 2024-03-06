# DFS(깊이 우선 탐색)을 이용한 신장 트리 (인접행렬 방식)
def ST_DFS(vtx, adj, s, visited):
    '''
        vtx: 정점(vertex) 리스트
        adj: 인접행렬
        s: 시작 정점(vertex)
        visited: 방문 여부 기록 리스트 (정점 리스트와 길이 동일함; 초깃값은 모두 False)
    '''
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0: # 모든 간선 (s, v)에 대해
            if visited[v] == False: # v를 아직 방문하지 않았으면
                print(f'({vtx[s]} {vtx[v]})', end = ' ') # 간선 출력
                ST_DFS(vtx, adj, v, visited)


# DFS(깊이 우선 탐색)를 이용한 신장 트리 테스트 프로그램
vtx = ['U','V','W','X','Y']
edge = [[0,  1,  1,  0,  0],
        [1,  0,  1,  1,  0],
        [1,  1,  0,  0,  1],
        [0,  1,  0,  0,  0],
        [0,  0,  1,  0,  0]]

print('ST_DFS_AM: ', end = '')
ST_DFS(vtx, edge, 0, [False] * len(vtx))
print()