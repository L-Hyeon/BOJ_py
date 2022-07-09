import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    s = input().strip()
    print(s[0] + s[-1])

do()
