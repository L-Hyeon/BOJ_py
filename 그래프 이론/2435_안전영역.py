import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def do():
  def bfs(a, b, k):
    q = deque([[a, b]])
    visited[a][b] = True

    while(q):
      y, x = q.popleft()
      for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        i += y
        j += x
        if (0 <= i < N) and (0 <= j < N) and (not visited[i][j]) and (lst[i][j] > k):
          q.append((i, j))
          visited[i][j] = True

  N = int(input())
  lst = list(list(map(int, input().split())) for i in range(N))
  mx, mn = 0, 100
  for i in range(N):
    for j in range(N):
      if (lst[i][j] < mn):
        mn = lst[i][j]
      elif (lst[i][j] > mx):
        mx = lst[i][j]
  
  res = 1
  for k in range(mn, mx + 1):
    visited = list(list(False for i in range(N)) for j in range(N))
    cnt = 0
    for i in range(N):
      for j in range(N):
        if (lst[i][j] > k) and (visited[i][j] == False):
          cnt += 1
          bfs(i, j, k)
  
    res = max(res, cnt)
  
  print(res)

def fast():
  def find(x):
    if root[x] == x: return x
    root[x] = root[find(root[x])]
    return root[x]

  def union(x1, x2):
    root[find(x2)] = find(x1)

  
  N = int(input())
  P = 1
  W = N + 2*P
  root = {}
  dic = defaultdict(list)
  for i in range(1, N+1):
      for j, k in zip(list(map(int, input().split())), range(W*i+1, W*(i+1) - 1)):
          dic[j].append(k)
  
  heights = sorted(dic, reverse = True)
  cnt = 1
  safe = list()
  for h in heights:
    for i in dic[h]:
      root[i] = i
    
    for i in dic[h]:
      for j in [i - W, i - 1, i + 1, i + W]:
        if j in root:
          union(i,j)

    safe = list(i for i in safe if root[i] == i)
    for i in dic[h]:
      if root[i] == i:
          safe.append(i)
      cnt = max(cnt, len(safe))
  
  print(cnt)

fast()
