def f(arr):
    cnt_i = set()
    cnt_j = set()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':    # '#'을 발견하면 cnt 리스트에 추가
                cnt_i.add(i)
                cnt_j.add(j)
                cnt += 1
    root = (cnt ** 0.5)
    if root % 1 != 0:
        return 'no'

    if (max(cnt_i) - min(cnt_i)) != (max(cnt_j) - min(cnt_j)):  # 가로와 세로의 길이가 다르면
        return 'no'         #  'no'를 반환해
    cnt_i = list(cnt_i)
    cnt_j = list(cnt_j)
    for a in range(len(cnt_i)-1):   # 연속된 숫자가 아니면( # 이 변을 이루는게 아니라 따로따로있으면)
        if cnt_i[a]+1 != cnt_i[a+1]:  # no 반환
            return 'no'
    for b in range(len(cnt_j)-1):
        if cnt_j[b]+1 != cnt_j[b+1]:
            return 'no'
    return 'yes'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {f(arr)}')