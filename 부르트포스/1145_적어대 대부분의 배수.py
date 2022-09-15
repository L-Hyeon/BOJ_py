import sys
from math import lcm
input = sys.stdin.readline

def do():
  lst = sorted(list(map(int, input().split())))
  res = lst[0]

  while (True):
    flag = 0
    for e in lst:
      if (res % e == 0):
        flag += 1
      if (flag == 3):
        print(res)
        return
    res += 1

def fast():
  lst = list(map(int, input().split()))
  res = 10**7
  for i in range(3):
    for j in range(i + 1, 4):
      for k in range(j + 1, 5):
        t = lcm(lcm(lst[i], lst[j]), lst[k])
        if (t < res):
          res = t
  print(res)

fast()
