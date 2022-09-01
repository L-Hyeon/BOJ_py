import sys
input = sys.stdin.readline

left, right = int(input()), int(input())

sieve = [False, False] + [True]*(right - 1)
for i in range(2, right + 1):
    if (sieve[i]):
        for j in range(2*i, right + 1, i):
            sieve[j] = False

res = 0
mn = -1
for i in range(left, right + 1):
    if (sieve[i]):
        res += i
        if (mn == -1):
            mn = i

if (mn != -1):
    print(res, mn, sep = '\n')
else:
    print(-1)
