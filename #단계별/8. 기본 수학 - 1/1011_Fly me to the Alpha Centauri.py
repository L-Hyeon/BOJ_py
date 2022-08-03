import sys
input = sys.stdin.readline

dct = dict()

for _ in range(int(input())):
    x, y = map(int, input().split())
    TOTAL = y - x

    if (TOTAL in dct):
        print(dct[TOTAL])

    k = int(TOTAL ** 0.5)
    if (TOTAL - k*k > 0):
        if (TOTAL - k*k <= k):
            print(2*k)
            dct[TOTAL] = 2*k
        else:
            print(2*k + 1)
            dct[TOTAL] = 2*k + 1
    else:
        print(2*k - 1)
        dct[TOTAL] = 2*k - 1
