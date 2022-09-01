import sys
input = sys.stdin.readline

sieve = [False, False] + [True]*(1000 - 1)
for i in range(2, 1001):
    if (sieve[i]):
        for j in range(2*i, 1001, i):
            sieve[j] = False

input()
res = 0
for p in list(map(int, input().split())):
    if (sieve[p]):
        res += 1

print(res)
