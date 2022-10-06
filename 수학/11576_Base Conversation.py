import sys
input = sys.stdin.readline

def do():
  A, B = map(int, input().split())
  int(input())
  idx = 0
  inTen = 0
  for e in reversed(list(map(int, input().split()))):
    inTen += e*(A**idx)
    idx += 1
  
  res = list()
  while (inTen):
    res += [str(inTen % B)]
    inTen //= B
  print(' '.join(reversed(res)))

do()
