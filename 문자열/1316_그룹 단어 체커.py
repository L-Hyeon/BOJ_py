import sys
input = sys.stdin.readline

def do():
  res = 0
  for _ in range(int(input())):
    S = input().strip()
    alpha = set()
    pre = ''
    res += 1
    for e in S:
      if (pre == ''):
        alpha.add(e)
      elif (pre != e):
        if (e in alpha):
          res -= 1
          break
        else:
          alpha.add(e)
      pre = e

  print(res)

do()
