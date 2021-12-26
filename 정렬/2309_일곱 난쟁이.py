import sys
from itertools import combinations
input = sys.stdin.readline

def do():
  lst = sorted(list(int(input()) for i in range(9)))
  for e in combinations(lst, 7):
    if (sum(e) == 100):
      print(*e, sep = '\n')
      break

def oth():
  lst = sorted(list(int(input()) for i in range(9)))
  for i in lst:
    for j in lst:
      if (i + j == sum(lst) - 100):
        lst.remove(i)
        lst.remove(j)

  for i in lst:
    print(i)

oth()
