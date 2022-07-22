import sys
input = sys.stdin.readline

def do():
  N, K = map(int, input().split())
  print(sorted(list(map(int, input().split())))[K - 1])

do()
