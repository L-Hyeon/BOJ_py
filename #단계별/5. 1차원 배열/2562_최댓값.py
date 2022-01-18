import sys
input = sys.stdin.readline

res, idx = 0, 0
for i in range(1, 10):
    n = int(input())
    if (res < n):
        res = n
        idx = i
print(res, idx, sep = '\n')
