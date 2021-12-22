import sys
input = sys.stdin.readline

def do():
  N = int(input())
  for i in range(N):
    print(' '*i + "*"*(N - i))

do()
