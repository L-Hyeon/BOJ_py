import sys
from itertools import product
input = sys.stdin.readline

def do():
  def isMadeOfK(a):
    for e in str(a):
      if (e not in K):
        return False
    return True

  N, t = map(int, input().split())
  K = set(input().split())
  res = N
  while (True):
    if (isMadeOfK(res)):
      print(res)
      break
    res -= 1

def fast():
  N, t = map(int, input().split())
  K = list(input().split())
  l = len(str(N))
  while (True):
    lst = list(product(K, repeat=l))
    res = list()
    for e in lst:
      t = int(''.join(e))
      if (t <= N):
        res.append(t)
    if (len(res) != 0):
      print(max(res))
      break
    else:
      l -= 1

fast()
