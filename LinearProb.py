# 문자열 탐색키에 대한 해시 함수 예시
def hashFnStr(key):
    sum = 0
    for c in key:
        sum += ord(c) # 문자열의 모든 문자에 대해, 해당 문자의 아스키 코드 값을 더하기
    return sum % M # 아스키 코드의 합에 제산 함수(mod; 나머지 연산 함수) 적용

# 선형 조사법의 삽입 알고리즘
M = 13
table = [None] * M # 크기가 M인 해시 테이블

def hashFn(key): # 해시 함수
    return key % M

def lp_insert(key):
    id = hashFn(key)
    # 계산된 주소부터 비어 있는 위치를 찾고, 비어 있지 않으면 다음 위치를 탐색 (최대 M번 진행)
    count = M
    while count > 0 and table[id] != None and table[id] != -1:
    # while count > 0 and table[id] != None:
        id = (id + 1 + M) % M # 다음 위치로 이동
        count -= 1 # 검사할 남은 위치 수

    # 빈 버킷을 찾으면 레코드 저장
    if count > 0:
        table[id] = key
    return

# 선형 조사법의 탐색 알고리즘
def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        # 찾는 레코드가 없는 경우, None 반환
        if table[id] == None:
            return None
        
        # 레코드를 찾은 경우, 찾은 레코드 반환
        if table[id] != -1 and table[id] == key:
        # if table[id] == key:
            return table[id]
        
        # 레코드를 찾지 못 한 경우, 버킷이 다른 키에 의해 사용되고 있는 경우이므로 다음 위치 탐색 (최대 M번 반복)
        id = (id + 1 + M) % M
        count -= 1
    return None

# 선형 조사법의 삭제 알고리즘
def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        # 삭제할 레코드가 테이블에 없는 경우
        if table[id] == None:
            return None
        
        # 삭제할 레코드를 찾은 경우, 버킷에 None이 아니라 -1을 저장함으로써 삭제된 것임을 표시
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return

        id = (id + 1 + M) % M
        count -= 1


# 선형 조사법 테스트 프로그램
print('   최초:', table)
lp_insert(45);  print('45 삽입:', table)
lp_insert(27);  print('27 삽입:', table)
lp_insert(88);  print('88 삽입:', table)
lp_insert(9);   print(' 9 삽입:', table)

lp_insert(71);  print('71 삽입:', table)
lp_insert(60);  print('60 삽입:', table)
lp_insert(46);  print('46 삽입:', table)
lp_insert(38);  print('38 삽입:', table)
lp_insert(24);  print('24 삽입:', table)
lp_delete(60);  print('60 삭제:', table)
print('46 탐색:', lp_search(46))