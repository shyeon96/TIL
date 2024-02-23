import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 배열의 세로크기 N 배열의 가로크기 M
    arr = [input() for _ in range(N)]
    decode = []         # 배열에서 암호코드를 추출하여 보관할 리스트
    start_i = []
    start_j = 0
    end_j = 0
    for a in range(N):
        for b in range(M):      # 앞과 뒤에서 코드가 시작되고 끝나는 부분을 찾고
            if arr[a][b] != '0':
                start_i.append(a)  # 암호코드가 있는 행 저장
                break
    for c in start_i:           # 암호코드가 있는 행을 순회하면서 암호만 추출
        for d in range(M):
            if arr[c][d] != '0':
                start_j = d
                break
        for e in range(M-1, -1, -1):
            if arr[c][e] != '0':
                end_j = e
                break
        iscode = arr[c][start_j: end_j + 1]     # 암호코드가 있는 부분 슬라이싱
        if iscode in decode:    # 중복된 코드면 지워줍니다
            pass
        else:
            decode.append(iscode)

    for f in range(len(decode)):    # 암호코드 중에 두 코드가 붙어있는것을 나눠줍니다
        if '0000000' in decode[f]:
            asd = decode.pop(f)
            decode.extend((asd.replace('0000000', ' ').split()))
    decode = list(set(decode))      # 중복된 암호코드 삭제
    print(decode)
    # for g in decode: