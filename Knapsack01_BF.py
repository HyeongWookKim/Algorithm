# 배낭 채우기(억지 기법)
def Knapsack01_BF(wgt, val, W): # wgt: 물건 별 무게 리스트, val: 물건 별 가치 리스트, W: 제한 용량
    '''
        n개의 물건의 집합에 대한 모든 부분집합의 수가 2^n 이기 때문에,
        숫자를 0부터 2^n - 1까지 만들고, 각 숫자에 대한 이진수의 각 비트 정보를 이용!
    '''
    n = len(wgt) # 전체 물건 개수
    best_val = 0 # 최대 가치 초깃값

    for i in range(2 ** n): # n(A) = n 일 때, 집합 A의 부분집합 개수 = 2^n, 진부분집합(자기 자신 제외) 개수 = 2^n - 1
        # i를 이진수로 변환했을 때, 각 자릿수를 리스트에 역순으로 저장 (ex. 6은 이진수로 110이므로 [0, 1, 1]로 저장)
        s = [0] * n
        for d in range(n):
            s[d] = i % 2
            i = i // 2
        
        # i에 대한 물건의 총 무게(sum_wgt)와 총 가치(sum_val) 계산
        sum_wgt = 0
        sum_val = 0
        for d in range(n):
            if s[d] == 1: # ex) 6은 이진수로 110이므로 [0, 1, 1]로 저장되는데, 값이 1인 경우가 물건을 넣는 경우에 해당함
                sum_wgt += wgt[d]
                sum_val += val[d]
        
        if sum_wgt <= W: # 총 무게 합이 배낭의 용량(W)을 초과할 수 없음
            # 총 가치 합이 최대 가치보다 크면, 최대 가치 갱신(update)
            if sum_val > best_val:
                best_val = sum_val

    return best_val # 최대 가치 반환


# 배낭 채우기(억지 기법) 테스트 프로그램
if __name__ == '__main__':
    weight = [10, 20, 30, 25, 35] # 물건 별 무게
    value = [60, 100, 120, 70, 85] # 물건 별 가치
    W = 80 # 배낭의 제한 용량

    print('Knapsack01-BruteForce:', Knapsack01_BF(weight, value, W))