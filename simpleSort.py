# 1) 선택 정렬 알고리즘 (제자리 정렬 방식)
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        least = i
        # (i + 1)부터 (n - 1)까지의 요소 중, 최솟값의 인덱스 least를 구함
        for j in range(i + 1, n):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i] # 최솟값을 찾아서 위치 교환
        print(f'Step {i + 1} = {arr}') # 정렬되는 과정을 출력

# 선택 정렬 테스트 프로그램
print('\n선택 정렬 테스트')
data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print(f'Original: {data}')
selection_sort(data)
print(f'Selection: {data}')


# 2) 삽입 정렬 알고리즘
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # 삽입할 요소를 따로 저장해 둠
        
        j = i - 1 # (i - 1)번째 요소부터 비교해서 앞으로 진행
        while j >= 0 and arr[j] > key: # (i - 1)번째 요소가 key보다 더 크면, 뒤로 한 칸 옮김
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'Step {i} = {arr}')

# 삽입 정렬 테스트 프로그램
print('\n삽입 정렬 테스트')
data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print(f'Original: {data}')
insertion_sort(data)
print(f'Insertion: {data}')