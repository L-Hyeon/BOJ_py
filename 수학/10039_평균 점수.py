import sys
input = sys.stdin.readline

def do():
  s = 0
  for i in range(5):
    t = int(input())
    s += t if (t > 40) else 40
  print(s//5)

do()
