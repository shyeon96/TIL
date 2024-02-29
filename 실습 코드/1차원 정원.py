T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())    # N 꽃의 개수 D 물의 범위
    start = 0
    cnt = 0
    while start < N:
        start += (2 * D) + 1
        cnt += 1
    print(f'#{tc} {cnt}')