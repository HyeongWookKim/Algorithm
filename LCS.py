# LCS의 길이(분할 정복)
def lcs_recur(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]: # 마지막 문자가 같으면, 이들을 제외하고 계산한 다음 1을 더한 값이 답임
        return lcs_recur(X, Y, m - 1, n - 1) + 1
    else: # 마지막 문자가 서로 다르면, X와 Y 각각에 대해 마지막 문자를 하나씩 뺐을 때의 LCS를 계산해서 더 큰 값이 답임
        return max(lcs_recur(X, Y, m - 1, n), lcs_recur(X, Y, m, n - 1))

# LCS의 길이(동적 계획법)
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for _ in range(m + 1)] # 테이블 생성

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0: # 답을 이미 알고 있는 경우
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]: # 마지막 글자가 같은 경우
                L[i][j] = L[i - 1][j - 1] + 1
            else: # 마지막 글자가 다른 경우
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    for i in range(m + 1):
        print(L[i])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    print(f'LCS = "{lcs_dp_traceback(X, Y, L)}"')

    return L[m][n]

# LCS 테이블에서 LCS를 추적하는 알고리즘
def lcs_dp_traceback(X, Y, L):
    lcs = ''
    i = len(X)
    j = len(Y)

    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs
        elif v == L[i][j - 1] and v > L[i - 1][j]:
            j -= 1
        else:
            i -= 1
    return lcs


# LCS 테스트 프로그램
X = 'GAME OVER'
Y = 'HELLO WORLD'
print('X = ', X)
print('Y = ', Y)
print('LCS(분할 정복)', lcs_recur(X , Y, len(X), len(Y)))
print('LCS(동적 계획)', lcs_dp(X , Y))
print('-' * 50)

X = 'ABCDGH'
Y = 'AEDFHR'
print('LCS(동적 계획)', lcs_dp(X , Y))
print('-' * 50)

X = 'AGGTAB'
Y = 'GXTXAYB'
print('LCS(동적 계획)', lcs_dp(X , Y))