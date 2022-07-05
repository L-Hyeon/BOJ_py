import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  lst = ["c=", "c-", "dz=", "lj", "nj", "s=", "d-", "z="]
  for e in lst:
    S = S.replace(e, 'a')
  print(len(S))

do()
