import sys
input = sys.stdin.readline

def do():
  A = int(input())
  o = input().strip()
  B = int(input())

  print(A*B if (o == '*') else A + B)

do()
