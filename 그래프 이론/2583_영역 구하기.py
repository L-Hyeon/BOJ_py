import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(a, b):
    q = deque([[a, b]])
    lst[a][b] = 1
    ret = 1
    while (q):
      x, y = q.popleft()
      for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        i += x
        j += y
        if (0 <= i < N) and (0<= j < M) and (lst[i][j] == 0):
          lst[i][j] = 1
          q.append([i, j])
          ret += 1
    
    return ret

  N, M, K = map(int, input().split())
  lst = list(list(0 for i in range(M)) for j in range(N))
  for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
      for j in range(y1, y2):
        lst[j][i] = 1
  
  area = list()
  for i in range(N):
    for j in range(M):
      if (lst[i][j] == 0):
        area.append(bfs(i, j))

  print(len(area))
  print(*sorted(area))

do()
