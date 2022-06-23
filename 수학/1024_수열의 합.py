import sys
input = sys.stdin.readline

def do():
  N, L = map(int, input().split())
  x = -1
  idx = 0
  for i in range(L, 101):
    temp = (i*i - i)/2
    if ((N - temp) % i == 0) and ((N - temp)//i >= 0):
      x = (N - temp)//i
      idx = i
      break
  if (x == -1):
    print(-1)
  else:
    for i in range(idx):
      print(int(x + i), end = ' ')

do()
