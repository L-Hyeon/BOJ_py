import sys
input = sys.stdin.readline

def do():
  def dfs(r, c, d, s):
    if (s + (3 - d)*x <= res[0]):
      return
    if (d == 3):
      if (res[0] < s):
        res[0] = s
      return
    else:
      for i, j in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
        i += r
        j += c
        if (0 <= i < N) and (0 <= j < M) and (visited[i][j] == 0):
          if (d == 1):
            visited[i][j] = 1
            dfs(r, c, d + 1, s + lst[i][j])
            visited[i][j] = 0
          visited[i][j] = 1
          dfs(i, j, d + 1, s + lst[i][j])
          visited[i][j] = 0

  N, M = map(int, input().split())
  lst = list(list(map(int, input().split())) for i in range(N))
  visited = list(list(0 for i in range(M)) for j in range(N))
  res = [0]
  x = max(map(max, lst))
  for i in range(N):
    for j in range(M):
      visited[i][j] = 1
      dfs(i, j, 0, lst[i][j])
      visited[i][j] = 0

  print(res[0])

do()
