import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  r, c, d = map(int, input().split())
  lst = list(list(map(int, input().split())) for i in range(N))
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  cnt = 0
  while (True):
    if (lst[r][c] == 0):
      lst[r][c] = -1
      cnt += 1

    flag = False
    for i in range(4):
      d = (d - 1) % 4
      if (lst[r + dx[d]][c + dy[d]] == 0):
        r += dx[d]
        c += dy[d]
        flag = True
        break
    
    if (not flag):
      nd = (d + 2) % 4
      if (lst[r + dx[nd]][c + dy[nd]] == -1):
        r += dx[nd]
        c += dy[nd]
      else:
        break
  
  print(cnt)

do()
