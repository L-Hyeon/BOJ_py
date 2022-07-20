import sys
input = sys.stdin.readline

def do():
  print(*sorted(list(map(int, input().split()))))

do()
