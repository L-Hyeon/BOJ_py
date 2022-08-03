import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    y = N % H
    x = N // H + 1
    if (y == 0):
        y = H
        x -= 1
    print(100*y + x)
