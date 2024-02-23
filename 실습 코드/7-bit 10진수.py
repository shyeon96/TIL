import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    bin = input()
    s = 0
    print(f'#{tc}', end = ' ')
    while s < 70:
        dec = ''
        for a in range(7):
            dec += bin[a+s]
        s += 7
        ans = 0
        for b in range(6,-1,-1):
            if dec[b] == '1':
                ans += 2 ** (6 - b)
        print(ans, end = ' ')
    print()