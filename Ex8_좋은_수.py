import sys
input = sys.stdin.readline

N = int(input())
result = 0
tmp_list = list(map(int, input().split()))
tmp_list.sort()

for k in range(N):
    find = tmp_list[k]
    i = 0
    j = N - 1

    while i < j:
        if tmp_list[i] + tmp_list[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif tmp_list[i] + tmp_list[j] < find:
            i += 1
        else:
            j -= 1

print(result)