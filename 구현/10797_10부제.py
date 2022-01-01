import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  print(lst.count(N))

do()
