import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

if (C <= B):
    print(-1)
else:
    profit = C - B
    print(A // profit + 1)
