import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(rr, cc, num):
    q = deque([[rr, cc]])
    ret = 0
    unSize = 0
    while (q):
      r, c = q.popleft()
      for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        i += r
        j += c
        if (0 <= i < N) and (0 <= j < N) and (un[i][j] == -1) and (L <= abs(pop[r][c] - pop[i][j]) <= R):
          q.append([i, j])
          un[i][j] = num
          ret += pop[i][j]
          unSize += 1
    
    if (unSize):
      unPop.append(ret//unSize)

  N, L, R = map(int, input().split())
  pop = list(list(map(int, input().split())) for i in range(N))

  res = 0
  while (True):
    un = list(list(-1 for i in range(N)) for j in range(N))
    unPop = list()

    for i in range(N):
      for j in range(N):
        if (un[i][j] == -1):
          bfs(i, j, len(unPop))
    
    if (len(unPop) == 0):
      break

    for i in range(N):
      for j in range(N):
        if (un[i][j] != -1):
          pop[i][j] = unPop[un[i][j]]
    
    res += 1

  print(res)

do()
