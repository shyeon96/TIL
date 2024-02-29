T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    cnt = 0
    while len(arr) != 1:
        a = arr.pop()
        if a == ')':
            if arr[-1] in '(|':
                cnt += 1
        elif a == '|':
            if arr[-1] in '(':
                cnt += 1
    print(f'#{tc} {cnt}')