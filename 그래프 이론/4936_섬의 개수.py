import sys
from collections import deque
input = sys.stdin.readline

def do():
  res = []
  def bfs(a, b):
    q = deque([[a, b]])
    lst[a][b] = 0

    while(q):
      y, x = q.popleft()
      for i, j in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        i += y
        j += x
        if (0 <= i < H) and (0 <= j < W) and (lst[i][j] == 1):
          q.append((i, j))
          lst[i][j] = 0

  W, H = map(int, input().split())
  while (W != 0 and H != 0):
    lst = list(list(map(int, input().split())) for i in range(H))
    cnt = 0
    for i in range(H):
      for j in range(W):
        if (lst[i][j] == 1):
          cnt += 1
          bfs(i, j)
    res += [cnt]

    W, H = map(int, input().split())
  
  print('\n'.join(map(str, res)))

do()
