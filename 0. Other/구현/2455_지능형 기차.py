import sys
input = sys.stdin.readline

def do():
  x, cur = 0, 0
  for i in range(4):
    down, up = map(int, input().split())
    cur = cur - down + up
    if (x < cur): x = cur
  
  print(x)

do()
