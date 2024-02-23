def in_order(N):
    global num
    global node
    if N:
        in_order(left[N])
        node[N] = num
        num += 1
        in_order(right[N])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    node = [0] * (N+1)
    num = 1
    for a in range(1, N+1):
        if left[a] == 0:
            if 2*a <= N:
                left[a] = 2*a

            if 2*a+1 <= N:
                right[a] = 2*a+1
        if left[a] != 0:
            par[left[a]] = a
        if right[a] != 0:
            par[right[a]] = a
    in_order(1)
    print(f'#{tc} {node[1]} {node[N//2]}')
