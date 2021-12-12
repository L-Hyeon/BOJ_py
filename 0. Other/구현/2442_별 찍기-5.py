import sys
input = sys.stdin.readline

def do():
  N = int(input())
  for i in range(1, N + 1):
    print(' '*(N - i) + '*'*((2*i) - 1))

do()
