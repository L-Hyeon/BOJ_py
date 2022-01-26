import sys
input = sys.stdin.readline

def do():
  for i in range(int(input())):
    x = input().strip()
    print(int(x[0]) + int(x[2]))

do()
