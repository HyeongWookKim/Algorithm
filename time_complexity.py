# 리스트에서 최댓값을 찾는 알고리즘
def find_max(arr):
    n = len(arr)
    max_value = arr[0]
    for i in range(n):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

# 리스트에서 특정 값을 찾는 알고리즘
def find_key(arr, key_value):
    n = len(arr)
    for i in range(n):
        if arr[i] == key_value:
            return i
    return -1


# 알고리즘 테스트
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print('find_max: ', find_max(data))
print('find_key: ', find_key(data, 5))
print('find_key: ', find_key(data, 10))