import sys
input = sys.stdin.readline

def do():
  N = input().strip()
  diff = 0
  for i in range(1, len(N)):
    if (N[i - 1] != N[i]):
      diff += 1
  print((diff + 1)//2)

do()
