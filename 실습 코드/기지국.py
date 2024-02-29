def z(n):
    global arr
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if n == 'A':
        len = 1
    elif n == 'B':
        len = 2
    elif n == 'C':
        len = 3
    for a in range(4):
        for b in range(1, len + 1):
            ni = i + (di[a] * b)
            nj = j + (dj[a] * b)
            if (0 <= ni < N) and (0 <= nj < N):
                arr[ni][nj] = 'X'



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] in 'ABC':
                z(arr[i][j])

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')