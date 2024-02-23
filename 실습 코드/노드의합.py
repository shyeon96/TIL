T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = []
    node = [0] * (N + 1)
    # N 노드의 개수 M 리프 노드의 개수 L 출력할 노드 번호
    for _ in range(M):  # 각 리프노드에 입력
        n1, n2 = map(int, input().split())
        node[n1] = n2
    for a in range(N-1, 0, -1):
        if node[a] == 0 and a*2+1 < (N+1):
            node[a] = node[a*2] + node[a*2+1]
        elif node[a] == 0 and a*2+1 <= (N+1):
            node[a] = node[a*2]
        elif a < L:
            break
    print(f'#{tc} {node[L]}')