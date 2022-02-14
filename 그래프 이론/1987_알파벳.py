import sys
input = sys.stdin.readline

mov = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def do():
  def bfs(a, b):
    q = set()
    q.add((a, b, lst[a][b]))
    ret = 0
    while (q):
      y, x, trace = q.pop()
      ret = max(ret, len(trace))
      if (ret == 26): return 26

      for i, j in mov:
        i += y
        j += x
        if (0 <= i < N) and (0 <= j < M) and (lst[i][j] not in trace):
          q.add((i, j, trace + lst[i][j]))
    
    return ret
  
  N, M = map(int, input().split())
  lst = list(list(input().strip()) for i in range(N))

  print(bfs(0, 0))

do()
