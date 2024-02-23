for tc in range(1, 11):
    N = int(input())    # 덤프횟수
    box = list(map(int, input().split()))
    for _ in range(N):
        box.sort()
        if box[-1] - box[0] <= 1:
            print(f'#{tc} {box[-1] - box[0]}')
        box[0] += 1
        box[-1] -= 1
    box.sort()
    print(f'#{tc} {box[-1] - box[0]}')