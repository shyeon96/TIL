T = int(input())
result = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    ans = min(B, D) - max(A, C)
    if ans < 0:
        ans = 0
    result.append(ans)
for i in range(T):
    print(f'#{i+1} {result[i]}')