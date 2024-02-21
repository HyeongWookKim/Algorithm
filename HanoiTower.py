# 하노이의 탑
def hanoi_tower(n, fr, tmp, to):
    if n == 1: # 순환 호출을 멈추는 부분 (원판이 하나라면 바로 이동)
        print(f'원판 1: {fr} --> {to}')
    else:
        # Step 1. fr에 있는 (n - 1)개의 원판을 to를 임시 막대로 이용해서 tmp로 이동하는 단계
        # >> 맨 밑의 제일 큰 원반을 제외한 나머지 원반들을 보조 기둥으로 이동
        hanoi_tower(n - 1, fr, to, tmp)

        # Step 2. fr에 남은 하나의 원판을 to로 이동하는 단계
        # >> 가장 큰 원반을 목표 기둥으로 이동
        print(f'원판 {n}: {fr} --> {to}')

        # Step 3. tmp에 있는 (n - 1)개의 원판을 fr를 임시 막대로 이용해서 to로 이동하는 단계
        hanoi_tower(n - 1, tmp, fr, to)


hanoi_tower(4, 'A', 'B', 'C')