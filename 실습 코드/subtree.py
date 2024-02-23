def f(N):
    global cnt
    if N:
        cnt += 1
        f(left[N])
        f(right[N])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    arr = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)
    par = [0] * (V+1)
    cnt = 0
    for a in range(E):
        r, c = arr[a*2], arr[a*2+1]
        if left[r] == 0:
            left[r] = c
        else:
            right[r] = c
        par[c] = r

    f(N)
    print(f'#{tc} {cnt}')