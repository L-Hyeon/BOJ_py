import sys
input = sys.stdin.readline

def do():
  N, C = map(int, input().split())
  dct = dict()
  for i, e in zip(range(0, N), map(int, input().split())):
    if (e in dct):
      dct[e][0] += 1
    else:
      dct[e] = [1, i]
  dct = sorted(dct.items(), key=lambda x: (-x[1][0], x[1][1]))
  for e in dct:
    for i in range(e[1][0]):
      print(e[0], end = ' ')

do()
