import sys
input = sys.stdin.readline

def do():
  A, B = input().split()
  print(int(str(int(A[::-1]) + int(B[::-1]))[::-1]))

do()
