def enq(n):
    global last
    last += 1  # 마지막 노드 추가 (완전 이진트리 유지)
    h[last] = n  # 마지막 노드에 데이터 삽입
    c = last  # 부모 > 자식
    p = c // 2  # 부모 번호 계산
    while p >= 1 and h[p] > h[c]:  # 부모가 있는데 더 작으면
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    h = [0] * (N+1)
    last = 0
    ans = 0
    arr = list(map(int, input().split()))
    for a in range(N):
        enq(arr[a])
    while last > 0:
        last //= 2
        ans += h[last]
    print(f'#{tc} {ans}')