T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # N 컨테이너 수 M 트럭 수
    w = list(map(int, input().split()))         # 컨테이너 별 화물의 무게
    t = list(map(int, input().split()))         # 화물의 적재 용량
    w.sort()
    t.sort()
    # print(w)
    # print(t)
    add = 0
    while w and t:    # 화물이랑 트럭이 남아있을때까지 반복
        if t[-1] >= w[-1]:  # 트럭의 적재 용량이 화물 무게보다 크면
            t.pop()         # 화물을 실어서 보낸다
            b = w.pop()
            add += b
        elif t[-1] < w[-1]: # 화물이 더 무거우면
            b = w.pop()         # 화물을 재낀다
    print(f'#{tc} {add}')