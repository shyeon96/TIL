def f(n, start):
    global result
    if n == 2:
        weight = sum(path)
        if (weight <= M) and (weight >= result):
            result = weight
        return
    for i in range(start, N):
        path.append(arr[i])
        f(n + 1, i + 1)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 봉지 개수 M 무게 합 제한
    arr = list(map(int, input().split()))
    path = []
    result = -1
    f(0,0)
    print(f'#{tc} {result}')