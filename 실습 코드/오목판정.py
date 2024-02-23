import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    di = [0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]
    ans = 'NO'
    # for a in range(N):
    #     print(omok[a])
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':   # 바둑알을 발견하면
                for k in range(8):  # 주변을 탐색함
                    cnt = 0
                    ni = i + di[k]
                    nj = j + dj[k]
                    if (0 <= ni < N) and (0 <= nj < N):
                        if omok[ni][nj] == 'o':  # 바둑알이 있으면
                            for _ in range(3):   # 이게 오목인지 확인
                                ni += di[k]
                                nj += dj[k]
                                if (0 <= ni < N) and (0 <= nj < N):
                                    if omok[ni][nj] != 'o':
                                        break
                                    else:
                                        cnt += 1
                            if cnt == 3:
                                ans = 'YES'
                                break
            if ans == 'YES':
                break
    print(f'#{tc} {ans}')