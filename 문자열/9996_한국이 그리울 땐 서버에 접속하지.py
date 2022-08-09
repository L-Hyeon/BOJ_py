import sys
input = sys.stdin.readline

def do():
  N = int(input())
  prefix, suffix = input().rstrip("\n").split('*')
  for _ in range(N):
    S = input().strip()
    if (len(prefix) + len(suffix) <= len(S)):
      if (S[:len(prefix)] == prefix and S[len(S) - len(suffix):] == suffix):
        print("DA")
      else:
        print("NE")
    else:
      print("NE")

do()
