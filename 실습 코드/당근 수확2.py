T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 밭의 개수 M 수레에 실을 수 있는 용량
    arr = [0] + list(map(int, input().split()))     # 각 밭에 있는 당근의 개수
    size = 0
    move = 0    # 일꾼이 움직인 거리
    for i in range(1, N+1):  # 밭을 다 돌면서
        size += arr[i]       # 당근을 더해준다
        while size >= M:
            size -= M
            move += 2 * i
    if size > 0:              # 밭을 다 돌았는데 당근이 남았으면
        move += 2 * N         # 한번 더 옮겨준다
    print(f'#{tc} {move}')