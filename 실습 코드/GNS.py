T = int(input())
for _ in range(T):
    tc, N = input().split()
    arr = list(input().split())
    trans = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6,
             "SVN": 7, "EGT": 8, "NIN": 9}
    ttrans = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX",
              7: "SVN", 8: "EGT", 9: "NIN"}
    arrr = []
    for a in arr:
        arrr += [trans[a]]
    arrr.sort()
    arr.clear()
    for b in arrr:
        arr += [ttrans[b]]
    print(tc)
    print(*arr)