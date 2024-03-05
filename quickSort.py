# 퀵 정렬 알고리즘
def quick_sort(arr, left, right):
    if left < right: # 정렬 범위가 2개 이상인 경우 (즉, 리스트가 2개 이상의 요소를 갖는 경우)
        # 분할 기준인 피벗을 중심으로 리스트를 두 부분으로 분할 후,
        # 왼쪽/오른쪽 부분 리스트 각각에 대해 정렬 진행
        q = partition(arr, left, right) # 분할 기준(피벗; pivot)의 인덱스
        quick_sort(arr, left, q - 1)
        quick_sort(arr, q + 1, right)

# 분할 정렬 알고리즘 ('탐색 -> 교환' 과정 반복)
def partition(arr, left, right):
    '''
        - 탐색은 low를 오른쪽으로, high를 왼쪽으로 이동시키면서 조건에 맞지 않는 요소를 찾는 과정임
        
        1. 왼쪽 부분 리스트
            - arr[low]가 pivot 값 이하이면 왼쪽 부분 리스트에 적합하기 때문에, low를 오른쪽으로 전진시키다가 arr[low]가 pivot보다 클 때 멈춤
        2. 오른쪽 부분 리스트
            - arr[high]가 pivot 값보다 크면 high를 왼쪽으로 전진시키다가 arr[high]가 pivot보다 작으면 멈춤
        3. 조건에 맞지 않는 arr[low]와 arr[high]를 교환
        
        * 1 ~ 3번 과정을 low가 high보다 더 클 때까지(즉, 역전될 때까지) 진행 (역전되면 '탐색 -> 교환' 과정 종료)

        4. pivot을 두 부분 리스트의 중앙으로 옮기기 (pivot과 arr[high]를 교환해주면 됨)
    '''
    pivot = arr[left] # 왼쪽 요소를 pivot으로 지정
    low = left + 1
    high = right

    while (low < high): # low와 high가 역전되지 않는 한 반복
        # 왼쪽 부분 리스트 처리 로직
        while low <= right and arr[low] <= pivot:
            low += 1
        # 오른쪽 부분 리스트 처리 로직
        while high >= left and arr[high] > pivot:
            high -= 1
        
        if low < high: # low와 high가 역전되지 않았으면 두 레코드 교환
            arr[low], arr[high] = arr[high], arr[low]

    # 피벗(분할 기준)과 high를 교환
    arr[left], arr[high] = arr[high], arr[left]
    return high # 피벗(분할 기준)의 인덱스 반환


# 퀵 정렬 테스트 프로그램
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(f'Original  : {data}')
quick_sort(data, 0, len(data) - 1)
print(f'QuickSort : {data}')