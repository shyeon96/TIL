T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    ei = [-1,1,1,-1]
    ej = [1,1,-1,-1]
    ans = 0
    for i in range(N):      # 파리가 있는 배열에서
        for j in range(N):
            add = arr[i][j]         # 잡은 파리의 수
            for l in range(4):    # 4방향으로
                ni = i  # 4방향 델타
                nj = j
                for k in range(M-1):  # M의 거리만큼 파리가 죽는다
                    ni += di[l]
                    nj += dj[l]
                    if (0 <= ni < N) and (0 <= nj < N): # 범위를 넘지 않는 선에서
                        add += arr[ni][nj]  # 죽은 파리를 더함
            if ans <= add:  # 이 값이 최대값이면 갱신해줘
                ans = add

            add = arr[i][j]
            for m in range(4):
                ni = i  # 이번엔 대각선을 구함
                nj = j
                for n in range(M-1):  # M의 거리만큼 파리가 죽는다
                    ni += ei[m]
                    nj += ej[m]
                    if (0 <= ni < N) and (0 <= nj < N): # 범위 안의 파리를
                        add += arr[ni][nj]  # 죽여
            if ans <= add:
                ans = add
    print(f'#{tc} {ans}')