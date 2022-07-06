import sys
input = sys.stdin.readline

def do():
  res = ''
  dct = dict()
  N = int(input())
  if (N < 5):
    print("PREDAJA")
    return
  for _ in range(N):
    S = input().strip()
    if (S[0] in dct):
      dct[S[0]] += 1
      if (dct[S[0]] == 5):
        res += S[0]
    else:
      dct[S[0]] = 1
  
  res = ''.join(sorted(res))
  print(res if (res) else "PREDAJA")

do()
