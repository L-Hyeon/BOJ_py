import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(rr, cc, num):
    q = deque([[rr, cc]])
    ret = pop[rr][cc]
    union = [(rr, cc)]
    un[rr][cc] = num
    unSize = 1
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
          union.append((i, j))
    
    if (unSize != 1):
      x = ret//unSize
      for r, c in union:
        pop[r][c] = x
      return True
    
    return False

  N, L, R = map(int, input().split())
  pop = list(list(map(int, input().split())) for i in range(N))

  res = 0
  while (True):
    un = list(list(-1 for i in range(N)) for j in range(N))
    cnt = 0
    for i in range(N):
      for j in range(N):
        if (un[i][j] == -1):
          if (bfs(i, j, cnt)):
            cnt += 1
    
    if (cnt == 0):
      break
    
    res += 1

  print(res)

def fast():
  def bfs(rr, cc, num):
    q = deque([(rr, cc)])
    union = [(rr, cc)]
    un[rr][cc] = num
    ret = pop[rr][cc]
    unSize = 1
    while (q):
      r, c = q.popleft()
      for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        i += r
        j += c
        if (0 <= i < N) and (0 <= j < N) and (un[i][j] != num) and (L <= abs(pop[r][c] - pop[i][j]) <= R):
          un[i][j] = num
          q.append([i, j])
          union.append((i, j))
          ret += pop[i][j]
          unSize += 1
    
    if (unSize != 1):
      x = ret//unSize
      for r, c in union:
        pop[r][c] = x
        queue.append((r, c))
      return True
    
    return False

  N, L, R = map(int, input().split())
  pop = list(list(map(int, input().split())) for i in range(N))
  queue = deque()
  for i in range(N):
    for j in range(N):
      queue.append((i, j))

  res = 0
  un = list(list(-1 for i in range(N)) for j in range(N))
  while (True):
    isChanged = False
    for _ in range(len(queue)):
      i, j = queue.popleft()
      if (un[i][j] != res):
        if (bfs(i, j, res)):
          isChanged = True
    
    if (not isChanged):
      break
    
    res += 1

  print(res)

fast()
