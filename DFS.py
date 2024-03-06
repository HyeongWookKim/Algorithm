# 깊이 우선 탐색 (인접행렬 방식)
def DFS(vtx, adj, s, visited):
    '''
        vtx: 정점(vertex) 리스트
        adj: 인접행렬
        s: 시작 정점(vertex)
        visited: 방문 여부 기록 리스트 (정점 리스트와 길이 동일함; 초깃값은 모두 False)
    '''
    print(vtx[s], end = ' ') # 현재 정점 s는 방문했기 때문에 화면에 출력하고, 
    visited[s] = True # visited 값을 True로 갱신

    for v in range(len(vtx)):
        # (간선이 존재하는데) 방문하지 않은 이웃 정점 v가 있으면, 해당 정점을 시작으로 다시 DFS 호출
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)


# 깊이 우선 탐색 테스트 프로그램
vtx = ['U','V','W','X','Y']
edge = [[0,  1,  1,  0,  0],
        [1,  0,  1,  1,  0],
        [1,  1,  0,  0,  1],
        [0,  1,  0,  0,  0],
        [0,  0,  1,  0,  0]]

print('DFS(출발: U): ', end = '')
DFS(vtx, edge, 0, [False] * len(vtx))
print()