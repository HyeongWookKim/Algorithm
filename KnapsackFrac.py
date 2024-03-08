# 분할 가능한 배낭 채우기(탐욕적 기법)
# >> wgt: 물건 별 무게 리스트(단위 무게당 가격 내림차순 정렬), val: 물건 별 가치 리스트(단위 무게당 가격 내림차순 정렬), W: 제한 용량
def KnapSackFrac(wgt, val, W):
    best_val = 0 # 최대 가치 초깃값
    
    for i in range(len(wgt)):
        if W <= 0: # 배낭 용량이 다 찬 경우, break
            break

        if W >= wgt[i]: # 물건 전체를 넣을 수 있는 경우, 
            # 전체 다 넣고(최대 가치 증가시킴), 남은 용량(W) 갱신
            W -= wgt[i]
            best_val += val[i]
        
        else: # 물건의 일부만 넣을 수 있는 경우,
            # 추가로 더 넣을 수 있는 최대 비율을 계산하고, 최대한 채움(최대 가치 증가시킴)
            fraction = W / wgt[i]
            best_val += val[i] * fraction
            break
    
    return best_val


# 분할 가능한 배낭 채우기(탐욕적 기법) 테스트 프로그램
weight = [12,  10, 8] # 물건 별 무게 ("가치/무게"의 내림차순으로 정렬됨)
value = [120, 80, 60] # 물건 별 가치 ("가치/무게"의 내림차순으로 정렬됨)
W = 18 # 배낭의 제한 용량
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W)) 