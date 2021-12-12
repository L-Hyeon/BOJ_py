import sys
input = sys.stdin.readline

def do():
  R, S = map(int, input().split())
  print(2*S - R)

do()
