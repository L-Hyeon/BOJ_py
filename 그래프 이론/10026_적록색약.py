import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(a, b):
    q = deque([[a, b]])
    visited[a][b] = True
    t = lst[a][b]
    while (q):
      x, y = q.popleft()
      for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        i += x
        j += y
        if (0 <= i < N) and (0<= j < N) and (lst[i][j] == t) and (visited[i][j] == False):
          visited[i][j] = True
          q.append([i, j])
    
  N = int(input())
  lst = list(list(input().strip()) for i in range(N))
  visited = list(list(False for i in range(N)) for j in range(N))
  color = 0
  for i in range(N):
    for j in range(N):
      if (visited[i][j] == False):
        color += 1
        bfs(i, j)
  
  for i in range(N):
    for j in range(N):
      if (lst[i][j] == 'G'):
        lst[i][j] = 'R'

  visited = list(list(False for i in range(N)) for j in range(N))
  nonColor = 0
  for i in range(N):
    for j in range(N):
      if (visited[i][j] == False):
        nonColor += 1
        bfs(i, j)

  print(color, nonColor)

do()
