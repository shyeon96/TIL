T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(N):
        for j in range(N):
            if (i < j) and (i + j < N-1):
                a += arr[i][j]
            elif (i > j) and (i + j < N-1):
                b += arr[i][j]
            elif (i > j) and (i + j > N-1):
                c += arr[i][j]
            else:
                d += arr[i][j]
    result = max(a, b, c, d) - min(a, b, c, d)
    print(f'#{tc} {result}')