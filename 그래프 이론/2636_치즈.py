import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(a, b, N, M):
    q = deque([(a, b)])
    visited[a][b] = True
    modified = 0
    while (q):
      y, x = q.popleft()
      for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        i += y
        j += x
        if (0 <= i < N and 0 <= j < M and visited[i][j] == False):
          visited[i][j] = True
          if (lst[i][j] == 1):
            lst[i][j] = 0
            modified += 1
          else:
            q.append((i, j))
    return modified

  N, M = map(int, input().split())
  if (N <= 2 and M <= 2):
    print(0, 0, sep='\n')
    return
  lst = list(list(map(int, input().split())) for i in range(N))
  res, last = 0, 0
  while (True):
    visited = list(list(False for i in range(M)) for j in range(N))
    cnt = bfs(0, 0, N, M)
    if (cnt == 0):
      print(res, last, sep='\n')
      break
    last = cnt
    res += 1

do()
