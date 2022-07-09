import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  while (S != "END"):
    print(S[::-1])
    S = input().strip()

do()
