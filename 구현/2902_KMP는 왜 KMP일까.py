import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  res = S[0]
  for i in range(1, len(S)):
    if (S[i] == '-'):
      res += S[i + 1]

  print(res)

do()
