import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  stk = list()
  mx, cur = [0, 0], [0, 0]
  for e in S:
    x, y = -1, -1
    if (e == 'K'):
      x, y = 0, 1
    else:
      x, y = 1, 0
    
    if (cur[y] != 0):
      cur[y] -= 1
    else:
      if (cur[x] < mx[x]):
        cur[x] += 1
      else:
        mx[x] += 1
        cur[x] += 1
  print(sum(mx))

def fast():
  S = input().strip()
  curK, curP = 0, 0
  for e in S:
    if (e == "K"):
      curK += 1
      if (curP):
        curP -= 1
    else:
      curP += 1
      if (curK):
        curK -= 1
  print(curK + curP)

fast()
