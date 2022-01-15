import sys
input = sys.stdin.readline

N = int(input())
num = N
cycle = 0

while (True):
    l = num // 10
    r = num % 10
    temp = (l + r) % 10
    num = r*10 + temp
    cycle += 1

    if (N == num):
        break

print(cycle)
