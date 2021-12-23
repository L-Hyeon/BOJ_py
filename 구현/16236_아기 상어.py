import sys
from collections import deque
input = sys.stdin.readline

def do():
  def find(lst, baby):
    q = deque([[[baby[0], baby[1]]]])
    visited = list(list(0 for i in range(N)) for j in range(N))
    visited[baby[0]][baby[1]] = 1
    ate = list()

    while (q):
      temp = list()
      for e in q.popleft():
        r, c = e[0], e[1]
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          i += r
          j += c
          if (0 <= i < N) and (0 <= j < N) and (visited[i][j] == 0) and (lst[i][j] <= baby[2]):
            if (0 < lst[i][j] < baby[2]):
              ate.append([i, j])
            else:
              visited[i][j] = visited[r][c] + 1
              temp.append([i, j])
      
      if (ate):
        ate.sort()
        lst[ate[0][0]][ate[0][1]] = 0
        return ate[0][0], ate[0][1], visited[r][c]
      if (temp):
        q.append(temp)
    
    return -1, -1, -1

  N = int(input())
  lst = list(list() for i in range(N))
  baby = [-1, -1, 2, 0] # r, c, size, ate
  for i in range(N):
    lst[i] = list(map(int, input().split()))
    if (baby[0] == -1):
      for j in range(N):
        if (lst[i][j] == 9):
          baby[0] = i
          baby[1] = j
          lst[i][j] = 0
  
  res = 0
  while (True):
    baby[0], baby[1], dist = find(lst, baby)
    if (dist == -1):
      break
    res += dist
    baby[3] += 1
    if (baby[3] == baby[2]):
      baby[2] += 1
      baby[3] = 0
  
  print(res)

do()
