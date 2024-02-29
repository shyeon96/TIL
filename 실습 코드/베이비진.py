T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    A = [0] * 10
    B = [0] * 10
    winner = 0
    for i in range(12):     # 카드중에서
        if i % 2 == 0:      # A가 받을 카드
            A[arr[i]] += 1  # 받은 카드의 숫자를 카운트
        else:
            B[arr[i]] += 1
        if i >= 4:  # A가 카드를 3장 받았을때 부터
            if 3 in A:  # 숫자가 똑같은 3장의 카드가 있으면
                winner = 1  # A 승리
                break
            for a in range(8):
                if (A[a] != 0) and (A[a+1] != 0) and (A[a+2] != 0):  # 받은 카드중에서 연속으로 3개의 숫자가 있으면
                    winner = 1  # A승리
                    break
            if 3 in B:  # 숫자가 똑같은 3장의 카드가 있으면
                winner = 2  # B 승리
                break
            for b in range(8):
                if (B[b] != 0) and (B[b+1] != 0) and (B[b+2] != 0):  # 받은 카드중에서 연속으로 3개의 숫자가 있으면
                    winner = 2  # A승리
                    break
        if winner != 0:
            break
    print(f'#{tc} {winner}')