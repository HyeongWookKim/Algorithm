# 분할 정복을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k):
    pos = partition(A, left, right) # A에서 피벗의 인덱스

    if pos + 1 == left + k: # Case 1. 피벗이 k번째로 작은 수인 경우
        return A[pos]
    elif left + k < pos + 1: # Case 2. 답이 왼쪽 부분 리스트에 존재하는 경우
        return quick_select(A, left, pos - 1, k)
    else: # Case 3. 답이 오른쪽 부분 리스트에 존재하는 경우
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))

# 퀵 정렬의 피벗의 위치를 구하는 함수
def partition(A, left, right):
    low = left + 1 # 왼쪽 부분 리스트의 인덱스 (증가 방향)
    high = right # 오른쪽 부분 리스트의 인덱스 (감소 방향)
    pivot = A[left] # 피벗

    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while left <= high and pivot < A[high]:
            high -= 1
        
        if low < high: # 선택된 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left] # 마지막으로 high와 피벗 항목 교환
    return high # 피벗 위치 반환


# 분할 정복을 이용한 k번째 작은 수 찾기 테스트 프로그램
org = [27, 4, 26, 23, 34, 13, 42, 22, 48]
n = len(org) 
array = list(org)
print('입력 리스트 =', array) 
print('[축소 정복] 최솟값: ', quick_select(array, 0, n - 1, 1))
print()

array = list(org)
print('[축소 정복] 최댓값: ', quick_select(array, 0, n - 1, n))
print()

array = list(org)
print('[축소 정복] 중앙값: ', quick_select(array, 0, n - 1, 1 + (n - 1) // 2)) 
print()

array.sort()
print('정렬 리스트 =', array) 

array = [6, 5, 7, 9, 18, 3, 8]
n = 7
print('[축소정복] 중앙값: ', quick_select(array, 0, n - 1, 1 + (n - 1) // 2)) 
print()
