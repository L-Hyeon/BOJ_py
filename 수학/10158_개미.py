import sys
input = sys.stdin.readline

def do():
  W, H = map(int, input().split())
  p, q = map(int, input().split())
  t = int(input())

  d1 = (p + t)//W
  d2 = (q + t)//H
  
  p = (p + t) % W
  if (d1 & 1):
    p = W - p
  q = (q + t) % H
  if (d2 & 1):
    q = H - q

  print(p, q)

do()
