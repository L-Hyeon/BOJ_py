import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  lst = sorted(list(S[i:] for i in range(len(S))))
  print('\n'.join(lst))

do()
