import sys
from collections import deque
input = sys.stdin.readline

def do():
  def move(y, x, d):
    ret = 0
    while (lst[y + dy[d]][x + dx[d]] != '#' and lst[y][x] != 'O'):
      y += dy[d]
      x += dx[d]
      ret += 1
    return y, x, ret

  N, M = map(int, input().split())
  lst = list(input().strip() for i in range(N))
  chk = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
  q = deque()

  ry, rx, by, bx = 0, 0, 0, 0
  for i in range(N):
    for j in range(M):
      if (lst[i][j] == 'R'):
        ry, rx = i, j
      elif (lst[i][j] == 'B'):
        by, bx = i, j
  chk[ry][rx][by][bx] = True
  q.append((ry, rx, by, bx, 1))

  while (q):
    ry, rx, by, bx, cnt = q.popleft()
    if (cnt > 10):
      break
    for i in range(4):
      nry, nrx, rc = move(ry, rx, i)
      nby, nbx, bc = move(by, bx, i)
      if (lst[nby][nbx] == 'O'):
        continue
      if (lst[nry][nrx] == 'O'):
        print(cnt)
        return
      if (nrx == nbx) and (nry == nby):
        if (rc < bc):
          nby -= dy[i]
          nbx -= dx[i]
        else:
          nry -= dy[i]
          nrx -= dx[i]
      
      if (not chk[nry][nrx][nby][nbx]):
        chk[nry][nrx][nby][nbx] = True
        q.append((nry, nrx, nby, nbx, cnt + 1))
  
  print(-1)

do()
