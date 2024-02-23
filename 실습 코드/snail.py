T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i = 0
    j = 0
    a = 0
    a = a % 4
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 1
    while True:
        while arr[i][j] == 0:
            arr[i][j] = cnt
            cnt += 1
            i += di[a]
            j += dj[a]
            if (0 > i) or (i >= N) or (0 > j) or (j >= N):
                break
        i -= di[a]
        j -= dj[a]
        a += 1
        a = a % 4
        i += di[a]
        j += dj[a]
        if cnt > N ** 2:
            break
    print(f'#{tc}')
    for a in arr:
        print(*a)