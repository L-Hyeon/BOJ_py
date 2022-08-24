import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    N = int(input())
    cnt = 0
    i = 5
    while (i <= N):
      cnt += N//i
      i *= 5
    print(cnt)

do()
