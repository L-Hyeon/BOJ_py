import sys
from collections import deque
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(list(0 for i in range(N)) for j in range(N))
  dx = [1, 0, -1, 0]
  dy = [0, -1, 0, 1]
  d = 3
  K = int(input())
  for i in range(K):
    r, c = map(int, input().split())
    lst[r - 1][c - 1] = -1
  L = int(input())
  move = dict()
  for i in range(L):
    a, b = input().split()
    move[int(a)] = b
  
  cnt = 0
  r, c = 0, 0
  lst[r][c] = 1
  snake = deque([[0, 0]])
  while (True):
    cnt += 1
    nr = dx[d] + r
    nc = dy[d] + c
    if not ((0 <= nr < N) and (0 <= nc < N)) or (lst[nr][nc] == 1):
      break
    
    if (lst[nr][nc] != -1):
      a, b = snake.popleft()
      lst[a][b] = 0
    lst[nr][nc] = 1
    snake.append([nr, nc])
    r, c = nr, nc
    if (cnt in move.keys()):
      if (move[cnt] == 'L'): d = (d - 1) % 4
      else: d = (d + 1) % 4

  print(cnt)

do()
