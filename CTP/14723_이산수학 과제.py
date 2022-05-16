import sys
input = sys.stdin.readline

def do():
  N = int(input())
  i = 1
  while (i*(i + 1)//2 < N):
    i += 1
  b = N - (i - 1)*i//2
  a = i + 1 - b
  print(a, b)

do()
