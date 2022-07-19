import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(input().strip() for i in range(N))
  res = [0, 0]

  for i in range(N):
    t = 0
    pre = -1
    for j in range(N):
      if (lst[i][j] == '.'):
        if (pre == -1):
          pre = 1
        elif (pre == 1):
          t += 1
          pre = 0
      elif (pre != -1):
        pre = -1
    res[0] += t

  for i in range(N):
    t = 0
    pre = -1
    for j in range(N):
      if (lst[j][i] == '.'):
        if (pre == -1):
          pre = 1
        elif (pre == 1):
          t += 1
          pre = 0
      elif (pre != -1):
        pre = -1
    res[1] += t
  print(*res)

do()
