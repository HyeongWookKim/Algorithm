# 문자열 매칭(억지 기법)
def string_matching(T, P): # T는 입력 문자열, P는 패턴 문자열
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        # 현재 텍스트 위치(i)에서 패턴의 첫 문자(j = 0)부터 하나씩 텍스트 문자와 비교
        j = 0
        while j < m and P[j] == T[i + j]:
            j += 1

        if j == m: # 맨 끝(j == m)까지 일치하는 경우,
            return i # 매칭 성공
        
    return -1 # 매칭 실패


# 문자열 매칭(억지 기법) 테스트 프로그램
text = 'HELLO WORLD'
pattern = 'LO'
print(pattern, 'in', text, '-->', string_matching(text, pattern))
pattern = 'HI'
print(pattern, 'in', text, '-->', string_matching(text, pattern))