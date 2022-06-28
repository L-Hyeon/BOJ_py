import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    for s in input().split():
      print(s[::-1], end = ' ')
    print()

do()
