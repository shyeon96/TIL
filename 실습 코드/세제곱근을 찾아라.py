T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = -1
    n = round(N ** (1/3))
    if n ** 3 == N:
        ans = n
    print(f'#{tc} {ans}')