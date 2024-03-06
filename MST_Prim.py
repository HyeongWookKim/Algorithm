# MST(최소 신장 트리)에 포함되지 않은 최소 dist의 정점 찾기
INF = 999
def getMinVertex(dist, selected):
    '''
        dist: 현재까지 구성된 MST와 정점 사이의 최단 거리가 담긴 리스트
        selected: 정점이 MST에 포함되었는지 기록된 값이 담긴 리스트
    '''
    minv = 0 # 시작 정점 값을 0으로 설정하고,
    mindist = INF # 나머지는 모두 무한대로 설정

    for v in range(len(dist)):
        # MST에 포함되지 않은 정점 중에서 최소 dist를 갖는 정점의 인덱스 minv를 구함
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

# Prim(프림)의 최소 신장 트리 알고리즘
def MSTPrim(vtx, adj):
    '''
        vtx: 정점 리스트
        adj: 인접행렬
    '''
    n = len(vtx)

    # dist와 selected 배열 초기화
    dist = [INF] * n
    dist[0] = 0 # 시작 정점 0을 제외하고 모두 INF를 갖도록 설정
    selected = [False] * n # 모두 False로 설정

    for _ in range(n): # 정점 리스트 개수만큼 MST에 추가하면 종료
        # 최소 dist 정점 u 찾아서 출력 후, 방문했다고 표기
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vtx[u], end = ' ')

        for v in range(n):
            # 간선 (u, v)가 있고, v가 MST에 포함되지 않으면
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]: # (u, v)가 dist[v] 보다 작으면
                    dist[v] = adj[u][v] # dist[v] 갱신
        
        print(f': {dist}') # 중간 결과 출력

    print()


# Prim(프림)의 MST 테스트 프로그램
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0, 25, INF,	12, INF, INF, INF],
          [25, 0, 10, INF,	15, INF, INF],
          [INF, 10, 0, INF, INF, INF, 16],
          [12,	INF, INF, 0, 17, 37, INF],
          [INF, 15, INF, 17, 0, 19, 14],
          [INF, INF, INF, 37, 19, 0, 42],
          [INF, INF, 16, INF, 14, 42, 0]]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)