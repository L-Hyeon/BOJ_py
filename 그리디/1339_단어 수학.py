import sys
input = sys.stdin.readline

def do():
  N = int(input())
  words = list(list(input().strip()) for i in range(N))
  dct = dict()

  for i in range(N):
    l = len(words[i])
    for j in range(l):
      if (words[i][j] in dct):
        dct[words[i][j]] += 10**(l - j - 1)
      else:
        dct[words[i][j]] = 10**(l - j - 1)
  
  res = 0
  cnt = 9
  for e in sorted(dct.values(), reverse = True):
    res += cnt*e
    cnt -= 1
  
  print(res)

do()
