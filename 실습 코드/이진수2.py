import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    a = 1
    bin = ''
    while N != 0:
        if N >= (1 / (2**a)):
            N -= (1 / (2**a))
            bin += '1'
        else:
            bin += '0'
        a += 1
        if len(bin) >= 13:
            print(f'#{tc}', 'overflow')
            break
    else:
        print(f'#{tc}', bin)