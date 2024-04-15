import sys
input = sys.stdin.readline

su_num, quiz_num = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0

# 합 배열 만들기
for n in numbers:
    tmp += n
    prefix_sum.append(tmp)

# 합 배열에서 구간 합 구하기
for i in range(quiz_num):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])