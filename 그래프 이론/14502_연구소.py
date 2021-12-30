import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def do():
  def bfs(x):
    l = copy.deepcopy(lab)
    q = copy.deepcopy(virus)
    while (q):
      r, c = q.popleft()
      for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        i += r
        j += c
        if (0 <= i < N) and (0 <= j < M) and (l[i][j] == 0):
          l[i][j] = 2
          x -= 1
          q.append((i, j))
    
    if (res[0] < x):
      res[0] = x
    return
  
  def comb(w, c):
    if (w == 3):
      bfs(c - 3)
      return
    else:
      for i in range(N):
        for j in range(M):
          if (lab[i][j] == 0):
            lab[i][j] = 1
            comb(w + 1, c)
            lab[i][j] = 0

  N, M = map(int, input().split())
  lab = list(list(list(map(int, input().split())) for i in range(N)))

  virus = deque()
  cnt = 0
  for i in range(N):
    for j in range(M):
      if (lab[i][j] == 0):
        cnt += 1
      elif (lab[i][j] == 2):
        virus.append((i, j))

  res = [0]
  comb(0, cnt)
  print(res[0])

def fast():
  def comb(lst):
    l = copy.deepcopy(lab)
    for i, j in lst:
      l[i][j] = 1
    cnt = dfs(l, copy.deepcopy(virus), 0)

    if (cnt < mx[0]):
      mx[0] = cnt
  
  def dfs(l, q, cnt):
    while (q):
      r, c = q.pop()
      if (mx[0] <= cnt):
        return 64
      for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        i += r
        j += c
        if (0 <= i < N) and (0 <= j < M) and (l[i][j] == 0):
          q.append((i, j))
          l[i][j] = 2
          cnt += 1
    
    return cnt

  N, M = map(int, input().split())
  lab = list(list(list(map(int, input().split())) for i in range(N)))
  wall = list()
  virus = list()
  safe = 0
  mx = [64]

  for i in range(N):
    for j in range(M):
      if (lab[i][j] == 0):
        wall.append((i, j))
        safe += 1
      elif (lab[i][j] == 2):
        virus.append((i, j))
  
  for i in combinations(wall, 3):
    comb(i)

  print(safe - mx[0] - 3)

fast()
