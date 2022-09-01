import sys
from bisect import bisect_right
input = sys.stdin.readline

def do():
    sieve = [False, False] + [True]*246911
    for i in range(2, 497):
        if (sieve[i]):
            for j in range(2*i, 246913, i):
                sieve[j] = False

    N = int(input())
    while (N != 0):
        res = 0
        for i in range(N + 1, 2*N + 1):
            if (sieve[i]):
                res += 1
        print(res)

        N = int(input())

def fast():
    sieve = [True]*123456
    for i in range(3, 497, 2):
        if (sieve[i // 2]):
            k = i*i
            sieve[k // 2 :: i] = [False]*((246913 - k - 1) // (2*i) + 1)
    prime = [2] + [(2*i + 1) for i in range(1, 123456) if sieve[i]]

    N = int(input())
    while (N != 0):
        print(bisect_right(prime, 2*N) - bisect_right(prime, N))
        N = int(input())

fast()
