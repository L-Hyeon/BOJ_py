import sys
from itertools import combinations
input = sys.stdin.readline

def do():
  N = int(input())
  stuff = list(list(map(int, input().split())) for i in range(N))
  gap = 10**9 + 1
  for i in range(1, N + 1):
    lst = list(combinations(range(N), i))
    for l in lst:
      s, b = 1, 0
      for e in l:
        s *= stuff[e][0]
        b += stuff[e][1]
      t = abs(s - b)
      if (t < gap):
        gap = t
  print(gap)

do()
