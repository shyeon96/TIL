T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            add = 0
            for k in range(N):
                add += arr[i][k]
                add += arr[k][j]
            add -= arr[i][j]
            if ans <= add:
                ans = add
    print(f'#{tc} {ans}')