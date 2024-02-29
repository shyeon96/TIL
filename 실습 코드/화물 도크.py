T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())    # s 시작시간 e 종료시간
        arr.append([s, e])
    arr.sort(key = lambda x: x[1])
    start = 0
    cnt = 0
    for i in range(N):      # arr 을 순회하면서
        if start <= arr[i][0]:  # 작업 가능 시간이 시작시간보다 작으면
            cnt += 1            # 작업 추가
            start = arr[i][1]   # 작업 가능 시간은 종료시간으로 갱신
    print(f'#{tc} {cnt}')