T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    max_add = 0
    for i in range(N):
        for j in range(M):
            add = arr[i][j]
            for a in range(4):
                ni = i
                nj = j
                for b in range(arr[i][j]):
                    ni += di[a]
                    nj += dj[a]
                    if (0 <= ni < N) and (0 <= nj < M):
                        add += arr[ni][nj]
            if max_add <= add:
                max_add = add
    print(f'#{tc} {max_add}')