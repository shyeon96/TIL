import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    iron = 0    # 겹쳐진 쇠막대기의 개수
    ir_on = 0   # 쇠막대기 조각의 총 개수
    stack = []
    for i in arr:
        if i == '(':
            stack.append(i)
            iron += 1
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
                iron -= 1
                ir_on += iron
                stack.append(i)
            else:
                iron -= 1
                ir_on += 1
    print(f'#{tc} {ir_on}')