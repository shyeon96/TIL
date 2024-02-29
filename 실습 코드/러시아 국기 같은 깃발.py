import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 세로(행) M 가로(열)
    arr = [list(input()) for _ in range(N)]
    min_cnt = M * N
    for a in range(N-2):
        for b in range(a+1, N-1):
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if (i <= a) and (arr[i][j] != 'W'):
                        cnt += 1
                    elif (a < i <= b) and (arr[i][j] != 'B'):
                        cnt += 1
                    elif (i > b) and (arr[i][j] != 'R'):
                        cnt += 1
            if min_cnt >= cnt:
                min_cnt = cnt
    print(f'#{tc} {min_cnt}')