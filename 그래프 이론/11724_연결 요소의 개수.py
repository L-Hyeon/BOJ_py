import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def do():
  def get(x):
    if (p[x] == x):
      return x
    p[x] = get(p[x])
    return p[x]
  
  N, M = map(int, input().split())
  p = list(i for i in range(N + 1))
  
  for i in range(M):
    a, b = map(int, input().split())
    a, b = get(a), get(b)
    if (a != b):
      if (a < b):
        p[b] = a
      else:
        p[a] = b
  
  res = 0
  for i in range(1, N + 1):
    if (p[i] == i):
      res += 1
  
  print(res)

def oth():
  def dfs(c):
    visited[c] = True
    for n in range(1, N + 1):
      if (visited[n] == False) and (graph[c][n]):
        dfs(n)

  N, M = map(int, input().split())
  graph = list(list(0 for i in range(N + 1)) for i in range(N + 1))
  for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
  
  res = 0
  visited = [False]*(N + 1)
  for k in range(1, N + 1):
    if (visited[k]):
      continue
    dfs(k)
    res += 1
  
  print(res)

oth()
