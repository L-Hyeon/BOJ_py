import sys
input = sys.stdin.readline

def do():
    left, right = map(int, input().split())

    sieve = [False, False] + [True]*(right - 1)
    for i in range(2, int(right**0.5) + 1):
        if (sieve[i]):
            for j in range(2*i, right + 1, i):
                sieve[j] = False

    res = list()
    if (left <= 2):
        res.append(2)
    for i in range(left + (left & 1 == 0), right + 1, 2):
        if (sieve[i]):
            res.append(i)

    print('\n'.join(map(str, res)))

def fast():
    left, right = map(int, input().split())

    sieve = [False] + [True]*((right - 1) // 2)
    for i in range(1, int(right**0.5 / 2 + 1)):
        if (sieve[i]):
            sieve[2*i*(i + 1) : : 2*i + 1] = [False]*((((right + 1) // 2) - 2*i*i) // (2*i + 1))

    if (left <= 2):
        print(2)
    
    print('\n'.join([f"{x}" for x, val in zip(range(left + (left & 1 == 0), right + 1, 2), sieve[left // 2:]) if (val)]))

do()
