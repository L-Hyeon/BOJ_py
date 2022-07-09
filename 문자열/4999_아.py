import sys
input = sys.stdin.readline

def do():
  A, B = input().strip(), input().strip()
  print('go' if (len(A) >= len(B)) else "no")

do()
