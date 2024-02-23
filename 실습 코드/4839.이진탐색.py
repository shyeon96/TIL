T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt = 0
    s1 = 1
    s2 = 1
    P1 = P
    P2 = P
    while True:
        cal1 = int((s1 + P1) / 2)
        cal2 = int((s2 + P2) / 2)
        if cal1 <= Pa:
            s1 = cal1
        else:
            P1 = cal1
        if cal2 <= Pb:
            s2 = cal2
        else:
            P2 = cal2
        cnt += 1
        if (cal1 == Pa) or (cal2 == Pb):
            break
    if (Pa == cal1) and (Pb == cal2):
        winner = 0
    elif Pa == cal1:
        winner = 'A'
    elif Pb == cal2:
        winner = 'B'
    print(f'#{tc} {winner}')