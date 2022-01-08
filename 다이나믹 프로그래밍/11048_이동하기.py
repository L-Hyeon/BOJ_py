import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  lst = list(list(map(int, input().split())) for i in range(N))
  memo = list(list(0 for i in range(M + 1)) for j in range(N + 1))
  for i in range(1, N + 1):
    for j in range(1, M + 1):
      memo[i][j] = lst[i - 1][j - 1] + max(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1])
  print(memo[-1][-1])

def fast():
  N, M = map(int, input().split())
  pre = [0]*M

  for i in range(N):
    cur = list(map(int, input().split()))
    for j in range(M):
      if (j == 0) or (cur[j - 1] < pre[j]):
        cur[j] += pre[j]
      else:
        cur[j] += cur[j - 1]
    pre = cur[:]
  
  print(pre[-1])

fast()
