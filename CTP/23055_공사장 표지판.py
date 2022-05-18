import sys
input = sys.stdin.readline

def do():
  N = int(input())
  for i in range(N):
    if (i == 0 or i == N - 1):
      print('*'*N)
      continue
    for j in range(N):
      if (j == i or j == N - 1 - i or j == 0 or j == N - 1):
        print('*', end = '')
      else:
        print(' ', end = '')
    print()

do()