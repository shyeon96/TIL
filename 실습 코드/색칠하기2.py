import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for a in range(r1, r2 + 1):
            for b in range(c1, c2 + 1):
                arr[a][b] += c
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1 or arr[i][j] == 2:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if (0 <= ni < 10) and (0 <= nj < 10):
                        if arr[ni][nj] != arr[i][j]:
                            cnt += 1
                    else:
                        cnt += 1

    print(f'#{tc} {cnt}')