import sys
input = sys.stdin.readline

N = int(input())

cnt = 1
while (cnt*(cnt + 1) / 2 < N):
    cnt += 1
cnt -= 1

idx = cnt*(cnt + 1) // 2
cnt += 2
if (cnt & 1):
    a = cnt - (N - idx)
    print(f"{cnt - a}/{a}")
else:
    a = cnt - (N - idx)
    print(f"{a}/{cnt - a}")
