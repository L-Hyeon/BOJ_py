#import sys
#input = sys.stdin.readline

def brute():
  S = input()
  P = input()
  res = 0
  i = 0
  while (i <= (len(S) - len(P))):
    if (S[i:i + len(P)] == P):
      res += 1
      i += len(P)
    else:
      i += 1
  print(res)

brute()
