T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    killmax = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for a in range(i,i+M):
                for b in range(j,j+M):
                    fly += arr[a][b]
            if killmax <= fly:
                killmax = fly
    print(f'#{tc} {killmax}')