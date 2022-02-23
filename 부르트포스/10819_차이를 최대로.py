import sys
from itertools import permutations
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  
  res = 0
  for p in permutations(lst):
    temp = 0
    for i in range(N - 1):
      temp += abs(p[i] - p[i + 1])
    if (res < temp):
      res = temp
  
  print(res)

def fast():
  N = int(input())
  lst = sorted(list(map(int, input().split())))
  p = list()
  for i in range(N//2):
    if (i & 1):
      p.insert(0, lst[i])
      p.append(lst[-i - 1])
    else:
      p.insert(0, lst[-i - 1])
      p.append(lst[i])
  
  res = 0
  for i in range((N//2)*2 - 1):
    res += abs(p[i] - p[i + 1])
  
  print(res if (N % 2 == 0) else max(res + abs(lst[N//2] - p[0]), res + abs(lst[N//2] - p[-1])))

def oth():
  def dfs(depth):
    if (depth == N):
      res.append(sum(abs(p[i] - p[i + 1]) for i in range(N - 1)))
      return
    for i in range(N):
      if (visited[i]):
        continue
      p.append(lst[i])
      visited[i] = True
      dfs(depth + 1)
      p.pop()
      visited[i] = False

  N = int(input())
  lst = list(map(int, input().split()))
  visited = [False] * N
  p = list()
  res = list()

  dfs(0)
  print(max(res))

oth()
