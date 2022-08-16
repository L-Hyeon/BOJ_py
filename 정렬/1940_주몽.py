import sys
input = sys.stdin.readline

def do():
  N = int(input())
  M = int(input())
  lst = sorted(list(map(int, input().split())))
  l, r = 0, N - 1
  res = 0
  while (l < r):
    temp = lst[l] + lst[r]
    if (M < temp):
      r -= 1
    elif (temp < M):
      l += 1
    else:
      res += 1
      l += 1
      r -= 1
  print(res)

do()
