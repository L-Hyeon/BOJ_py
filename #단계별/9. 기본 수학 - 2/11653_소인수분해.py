import sys
input = sys.stdin.readline

N = int(input())
r, i = int(N ** 0.5), 2

while (i <= r):
    while (not N % i):
        print(i)
        N //= i
    i += 1

if (N > 1):
    print(N)
