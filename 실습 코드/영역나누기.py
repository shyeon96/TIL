import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_result = 1000
    add_list = []
    if N > 2:
        for i in range(N-1):
            for j in range(N-1):
                add = 0
                for a in range(i+1):      # 2사분면 덧셈
                    for b in range(j+1):
                       add += arr[a][b]
                add_list.append(add)

                add = 0
                for a in range(i+1):      # 1사분면 덧셈
                    for b in range(j+1, N):
                        add += arr[a][b]
                add_list.append(add)

                add = 0
                for a in range(i+1, N):   # 3사분면 덧셈
                    for b in range(j+1):
                        add += arr[a][b]
                add_list.append(add)

                add = 0
                for a in range(i+1, N):   # 4사분면 덧셈
                    for b in range(j+1, N):
                        add += arr[a][b]
                add_list.append(add)

                result = max(add_list) - min(add_list)
                if min_result >= result:
                    min_result = result
    else:
        add = 0
        for a in range(N):
            for b in range(N):
                add_list.append(arr[a][b])
        result = max(add_list) - min(add_list)
        if min_result >= result:
            min_result = result

    print(f'#{tc} {min_result}')