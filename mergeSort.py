# 병합 정렬 알고리즘
def merge_sort(A, left, right):
    if left < right: # 항목이 2개 이상인 경우(즉, 부분 리스트 길이가 2 이상)
        mid = (left + right) // 2 # 리스트 균등 분할
        merge_sort(A, left, mid) # 왼쪽 부분 리스트 정렬
        merge_sort(A, mid + 1, right) # 오른쪽 부분 리스트 정렬
        merge(A, left, mid, right) # 병합
    # else에 해당하는 항목이 1개인 경우는 자동으로 정렬된 상태이므로 따로 처리 X
        
# 병합 과정
def merge(A, left, mid, right):
    i = left # 왼쪽 부분 리스트의 인덱스
    j = mid + 1 # 오른쪽 부분 리스트의 인덱스
    k = left # 병합을 위한 임시 리스트의 인덱스
    
    # 값이 작은 부분 리스트의 요소를 sorted_list에 복사하고,
    # 해당 리스트의 인덱스 증가시킴 (어느 한쪽 부분 리스트가 모두 처리될 때까지 진행)
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i += 1
            k += 1
        else:
            sorted_list[k] = A[j]
            j += 1
            k += 1

    # 1) 왼쪽 부분 리스트가 모두 처리된 경우, 오른쪽 부분 리스트의 남은 모든 요소를 sorted_list로 복사
    if mid < i:
        sorted_list[k: k + (right - j + 1)] = A[j: right + 1]
    # 2) 오른쪽 부분 리스트가 모두 처리된 경우, 왼쪽 부분 리스트의 남은 모든 요소를 sorted_list로 복사
    else:
        sorted_list[k: k + (mid - i + 1)] = A[i: mid + 1]

    A[left: right + 1] = sorted_list[left: right + 1] # 임시 리스트에 저장된 결과를 원래 리스트에 복사


# 병합 정렬 테스트 프로그램
data = [5, 3, 8, 4, 9, 1, 6, 2, 7] # 입력 리스트
sorted_list = [0] * len(data) # 입력 리스트와 동일한 길이의 임시 리스트 생성 (모든 요소 값을 0으로 초기화)
print('Original:', data)

merge_sort(data, 0, len(data) - 1) # 병합 정렬
print('MergeSort:', data)