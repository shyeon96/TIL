T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    A = []
    B = []
    ans = 0
    cnt = 0
    for i in range(12):
        if i % 2 == 0:          # 카드 나눠갖고
            A.append(arr[i])
            A.sort()
        else:
            B.append(arr[i])
            B.sort()
        if len(A) >= 3:         # 나눈 카드 갯수가 3장 이상이면
            for a in range(1, len(A)):  # A가 가진 카드에
                if A[a] == A[a-1] + 1:  # 연속된 3개의 숫자가 있는가?
                    cnt += 1
                    if cnt == 2:        # 있으면 A가 이김
                        ans = 1
                        break
                else:                   # 연속이 아니면 cnt 초기화
                    cnt = 0
                if A.count(arr[i]) == 3:  # 같은 숫자가 3개 있으면
                    ans = 1             # A가 이김
                    break
            if ans != 0:
                break
        cnt = 0
        if len(B) >= 3:
            for b in range(1, len(B)):
                if B[b] == B[b-1] + 1:  # 연속된 3개의 숫자가 있는가?
                    cnt += 1
                    if cnt == 2:        # 있으면 B가 이김
                        ans = 2
                        break
                else:
                    cnt = 0
                if B.count(arr[i]) == 3:  # 같은 숫자가 3개 있으면
                    ans = 2             # B가 이김
                    break
            if ans != 0:
                break
        cnt = 0
    print(f'#{tc} {ans}')