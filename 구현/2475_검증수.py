import sys
input = sys.stdin.readline

def do():
  res = 0
  for e in map(int, input().split()):
    res += e*e
  
  print(res % 10)

do()
