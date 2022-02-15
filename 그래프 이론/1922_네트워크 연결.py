import sys
input = sys.stdin.readline

def do():
  def find(x):
    if (x == root[x]):
      return x
    root[x] = find(root[x])
    return root[x]
  
  N = int(input())
  root = list(i for i in range(N + 1))
  M = int(input())
  lst = list(list(map(int, input().split())) for i in range(M))
  lst.sort(key = lambda x : x[2])

  res = 0
  i = 0
  for a, b, c in lst:
    x, y = find(a), find(b)
    if (x != y):
      res += c
      i += 1
      if (x < y):
        root[x] = y
      else:
        root[y] = x
    if (i == N - 1):
      break
  
  print(res)

do()
