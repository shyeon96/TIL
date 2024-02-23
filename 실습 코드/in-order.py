def in_order(t):
    if t:
        in_order(left[t])
        print(word[t], end = '')
        in_order(right[t])

for tc in range(1, 11):
    N = int(input())    # 정점의 총 수
    word = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    arr = [[0]*4 for _ in range(N)]
    for a in range(N):
        arr[a] = input().split()
        while len(arr[a]) != 4:
            arr[a] += [0]

    for a in range(N):
        word[int(arr[a][0])] = arr[a][1]

        if arr[a][2] != 0:
            left[int(arr[a][0])] = int(arr[a][2])
        if arr[a][3] != 0:
            right[int(arr[a][0])] = int(arr[a][3])

    print(f'#{tc}', end = ' ')
    in_order(1)
    print()