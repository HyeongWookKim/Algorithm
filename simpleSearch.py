# 순차 탐색 알고리즘
def sequential_search(arr, key, low, high):
    for i in range(low, high + 1):
        if arr[i] == key:
            return i
    return -1 # 탐색 실패 시, -1 반환

# 교환하기 전략이 추가된 순차 탐색 알고리즘
# >> 더 많이 탐색된 record가 앞으로도 더 많이 탐색될 가능성이 큰 경우에만 적용할 것!
def sequential_search_transpose(arr, key, low, high):
    for i in range(low, high + 1):
        if arr[i] == key:
            if i > low: # 맨 처음 요소가 아닌 경우
                arr[i], arr[i - 1] = arr[i - 1], arr[i] # 교환(transpose)
                i -= 1 # 한 칸 앞으로 이동
            return i
    return -1


# 이진 탐색 알고리즘 (순환 구조)
def binary_search(arr, key, low, high):
    if low <= high: # low와 high가 역전되면 탐색 실패 (즉, 종료 조건)
        middle = (low + high) // 2
        if arr[middle] == key:
            return middle
        elif key < arr[middle]: # 왼쪽 부분 리스트 탐색
            return binary_search(arr, key, low, middle - 1)
        else: # 오른쪽 부분 리스트 탐색
            return binary_search(arr, key, middle + 1, high)
    return -1

# 이진 탐색 알고리즘 (반복 구조)
def binary_search_iter(arr, key, low, high):
    while low <= high: # low와 high가 역전되면 탐색 실패 (즉, 종료 조건)
        middle = (low + high) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] < key: # 오른쪽 부분 리스트 탐색
            low = middle + 1
        else: # 왼쪽 부분 리스트 탐색
            high = middle - 1
    return -1


# <참고> 보간 탐색 중앙 요소 위치
# middle = int(low + (high - low) * (key - arr[low].key) / (arr[high].key - arr[low].key))

# 순차 탐색, 이진 탐색 테스트 프로그램
test_array = [3, 9, 15, 22, 31, 55, 67, 88, 91]
n = len(test_array)

print('입력 배열 = ', test_array)
search_num = int(input('탐색할 숫자를 입력하세요: '))

print('순차 탐색: ', sequential_search(test_array, search_num, 0, n - 1))
print('이진 탐색(순환 구조): ', binary_search(test_array, search_num, 0, n - 1))
print('이진 탐색(반복 구조): ', binary_search_iter(test_array, search_num, 0, n - 1))