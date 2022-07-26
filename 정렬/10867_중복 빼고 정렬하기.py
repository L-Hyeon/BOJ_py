import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = set(map(int, input().split()))
  lst = sorted(lst)
  print(*lst)

do()
