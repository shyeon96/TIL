def f(compare, cnt):
    if cnt == change:
        return
    a = max(compare)
    if compare != arr:
        add = -1
        for i in range(len(compare) - 1, add, -1):
            if compare[i] == a:
                max_i = i
                break
        add += 1
        compare[add], compare[max_i] = compare[max_i], compare[add]
        if add != max_i:
            cnt += 1
    else:
        compare[-1], compare[-2] = compare[-2], compare[-1]
        cnt += 1
    f(compare, cnt)


T = int(input())
for tc in range(1, T+1):
    num, change = map(int, input().split())
    arr = list(map(int, str(num)))
    compare = arr[::]
    arr.sort(reverse=True)
    f(compare, 0)
    print(compare)