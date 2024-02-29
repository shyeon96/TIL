T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    p = []
    q = []
    r = []
    cnt = 0
    add = 0
    for a in range(N):
        if arr[a] < arr[a+1]:
            cnt += 1        # 긴 줄기의 길이
            add += arr[a]   # 긴 줄기 - 1 까지의 고구마 개수
        else:
            p += [cnt]   # 긴 줄기가 끝나면 p에 긴 줄기의 길이를 저장
            cnt = 0         # 길이 초기화
            add += arr[a]   # 마지막 줄기의 고구마 개수를 더하고
            q += [add]   # q에 긴 줄기에 달려있는 고구마 개수 저장
            add = 0         # 고구마 개수 초기화
    p = [i for i in p if i != 0]    # p에서 길이가 0 인 줄기들 삭제
    # print(p)
    # print(q)
    for a in range(len(p)): # 긴 줄기에서
        if p[a] == max(p):  # 가장 긴 줄기에 달린
            r += [q[a]]  # 고구마 개수를 저장
    print(f'#{tc} {len(p)} {max(r)}')     # 각각 tc, 긴 줄기의 개수, 고구마 개수 출력