import sys
from collections import deque
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  MAX = 100001
  q = deque([N])
  visited = [False]*MAX
  dist = [0]*MAX
  visited[N] = True
  while (q):
    x = q.popleft()
    t = 2*x
    if (t < MAX) and (visited[t] == False):
      dist[t] = dist[x]
      if (t == M): break
      visited[t] = True
      q.appendleft(t)
    t = x + 1
    if (t < MAX) and (visited[t] == False):
      dist[t] = dist[x] + 1
      if (t == M): break
      visited[t] = True
      q.append(t)
    t = x - 1
    if (0 <= t) and (visited[t] == False):
      dist[t] = dist[x] + 1
      if (t == M): break
      visited[t] = True
      q.append(t)

  print(dist[M])

do()