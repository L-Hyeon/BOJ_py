import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  print(N - 1 + N*(M - 1))

do()
