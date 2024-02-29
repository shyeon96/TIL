def f(i, j, s):
    global min_s
    if i == N or j == N:
        return
    if min_s <= s:
        return
    s += arr[i][j]
    if (i == N-1) and (j == N-1):
        if min_s >= s:
            min_s = s
    f(i+1, j, s)
    f(i, j+1, s)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_s = 9999999
    f(0, 0, 0)
    print(f'#{tc} {min_s}')

