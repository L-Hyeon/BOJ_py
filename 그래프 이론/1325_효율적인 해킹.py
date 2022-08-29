import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def do():
  def bfs(a, N, M):
    q = deque([a])
    visited = [False]*(N + 1)
    visited[a] = True
    cnt = 1
    while (q):
      cur = q.popleft()
      for dest in graph[cur]:
        if (visited[dest]):
          continue
        visited[dest] = True
        cnt += 1
        q.append(dest)
    return cnt

  N, M = map(int, input().split())
  graph = defaultdict(list)
  for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

  mx = 0
  res = list()
  for i in range(1, N + 1):
    cnt = bfs(i, N, M)
    if (mx == cnt):
      res.append(i)
    elif (mx < cnt):
      res = [i]
      mx = cnt

  print(*res)

do()

