import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for a in range(N):
        if M & (1<<a):
            pass
        else:
            print(f'#{tc}', 'OFF')
            break
    else:
        print(f'#{tc}', 'ON')