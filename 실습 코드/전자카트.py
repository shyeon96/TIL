def f(n, path, s, N):
    global min_s
    if s >= min_s:
        return
    if n == N-1:
        s = 0
        path = [1] + path + [1]
        # print(path)
        for a in range(len(path)-1):
            s += arr[path[a]-1][path[a+1]-1]
        if min_s >= s:
            min_s = s
        return

    for i in range(2, N+1):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        f(n + 1, path,s, N)
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_s = 999999
    path = []
    used = [0 for _ in range(N + 2)]
    f(0, path, 0, N)
    print(f'#{tc} {min_s}')