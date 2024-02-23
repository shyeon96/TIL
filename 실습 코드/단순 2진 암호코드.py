import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    check_dict = {(3,2,1,1): '0',(2,2,2,1): '1',(2,1,2,2): '2',
                  (1,4,1,1): '3',(1,1,3,2): '4',(1,2,3,1): '5',
                  (1,1,1,4): '6',(1,3,1,2): '7',(1,2,1,3): '8',
                  (3,1,1,2): '9'}
    c = []
    for a in range(N):  # 1이 있는 배열 찾기 (거꾸로)
        for b in range(M-1, -1, -1):
            if arr[a][b] == '1':    # 1을 발견하면 값을 저장후 순회 종료
                c += [a, b]
                break
        if c:
            break
    dec = []
    scan = ''
    for d in range(c[1]-55,c[1]+1, 7): # 암호문을 7개씩 나눔
        scan = arr[c[0]][d:d+7]
        check = [0, 0, 0, 0]

        # print(scan)
        f = 0
        check[f] = 1
        for e in range(1,7):  # 나눈 암호문을 스캔해서 암호코드로 바꿔줌
            if scan[e-1] == scan[e]:
                check[f] += 1
            else:
                f += 1
                check[f] += 1
        dec += [int(check_dict[tuple(check)])]
    # print(dec)
    ans = 0
    if ((dec[0] + dec[2] + dec[4] + dec[6])*3 + (dec[1] + dec[3] + dec[5]+ dec[7])) % 10 == 0:
    # 암호코드 판별
        for g in dec:
            ans += g
    else:
        ans = 0
    print(f'#{tc} {ans}')