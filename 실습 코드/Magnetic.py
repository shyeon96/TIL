def f(arr):
    global cnt
    for j in range(100):
        is_red = 0
        for i in range(100):
            if arr[i][j] == 1:
                is_red = 1
            elif (arr[i][j] == 2) and (is_red == 1):
                cnt += 1
                is_red = 0


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 1이 N극 2가 S극 N극이 위 S극이 아래
    cnt = 0
    f(arr)
    print(f'#{tc} {cnt}')