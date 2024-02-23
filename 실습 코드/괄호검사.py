import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    s = [0]
    asd = list(input())
    cnt = 0
    for a in asd:
        if a in '({':
            s.append(a)
        elif a == ')':
            if s[-1] == '(':
                s.pop()
            else:
                break
        elif a == '}':
            if s[-1] == '{':
                s.pop()
            else:
                break
    else:
        if len(s) == 1:
            cnt = 1
    print(f'#{tc} {cnt}')