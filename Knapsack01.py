# 배낭 채우기(분할 정복)
def knapSack_dc(W, wt, val, n):
    '''
        W: 배낭의 용량
        n: 물건 개수(E1 ~ En)
        wt: 물건의 무게
        val: 물건의 가치
    '''
    if n == 0 or W == 0:
        return 0
    
    if wt[n - 1] > W: # 마지막 물건을 넣을 용량이 부족한 경우
        # 해당 물건을 제외한 최대가치 계산
        return knapSack_dc(W, wt, val, n - 1)
    
    else: # 마지막 물건을 넣는 경우와 넣지 않는 경우의 최대가치를 계산해서, 둘 중 더 큰 값을 반환
        valWithout = knapSack_dc(W, wt, val, n - 1)
        valWith = val[n - 1] + knapSack_dc(W - wt[n - 1], wt, val, n - 1)
        return max(valWith, valWithout)

# 배낭 채우기(동적 계획법)
def knapSack_dp(W, wt, val, n):
    '''
        W: 배낭의 용량
        n: 물건 개수(E1 ~ En)
        wt: 물건의 무게
        val: 물건의 가치
    '''
    # (n + 1) x (W + 1) 크기의 2차원 배열 생성 (모든 요소는 0으로 초기화)
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w: # i번째 물건이 용량을 초과한 경우
                A[i][w] = A[i - 1][w]
                
            else: # i번째 물건을 넣을 수 있는 경우
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]] # 물건을 넣는 경우
                valWithout = A[i - 1][w] # 물건을 빼는 경우
                A[i][w] = max(valWith, valWithout)

    return A[n][W]


# 배낭 채우기 테스트 프로그램
val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print("0-1 배낭 문제(분할 정복): ", knapSack_dc(W, wt, val, n))
print("0-1 배낭 문제(동적 계획): ", knapSack_dp(W, wt, val, n))