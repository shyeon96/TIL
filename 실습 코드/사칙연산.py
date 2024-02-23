for tc in range(1, 11):
    N = int(input())
    node = [0] * (N+1)
    arr = [0]
    for b in range(1,(N+1)):
        arr += [list(input().split())]
        node[int(arr[b][0])] = arr[b][1]
    for a in range(N, 0, -1):
        if node[a].isdigit():
            node[a] = int(node[a])
        elif node[a] in '+-*/':
            if node[a] == '+':
                node[a] = node[int(arr[a][2])] + int(node[int(arr[a][3])])
            elif node[a] == '-':
                node[a] = int(node[int(arr[a][2])]) - int(node[int(arr[a][3])])
            elif node[a] == '*':
                node[a] = int(node[int(arr[a][2])]) * int(node[int(arr[a][3])])
            elif node[a] == '/':
                node[a] = int(node[int(arr[a][2])]) / int(node[int(arr[a][3])])
    print(f'#{tc} {int(node[1])}')