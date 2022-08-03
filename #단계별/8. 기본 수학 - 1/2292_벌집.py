import sys
input = sys.stdin.readline

N = int(input())
k = (N - 1) / 6

cnt = 0
while (cnt*(cnt + 1) / 2 < k):
    cnt += 1

print(cnt + 1)
