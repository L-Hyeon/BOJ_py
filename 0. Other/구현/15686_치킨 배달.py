import sys
from itertools import combinations
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  home = list()
  chicken = list()
  for i in range(N):
    t = list(map(int, input().split()))
    for j in range(N):
      if (t[j] == 1): home.append([i, j])
      elif (t[j] == 2): chicken.append([i, j])
  
  res = 10000
  for c in combinations(chicken, M):
    sumOfDist = 0
    for h in home:
      minDist = 10000
      for k in c:
        dist = abs(k[0] - h[0]) + abs(k[1] - h[1])
        if (dist < minDist):
          minDist = dist
      sumOfDist += minDist
    
    if (sumOfDist < res):
      res = sumOfDist
  
  print(res)

def fast():
  N, M = map(int, input().split())
  home, chicken = list(), list()
  for i in range(N):
    t = list(input().split())
    for j in range(N):
      if (t[j] == '1'): home += [[i, j]]
      elif (t[j] == '2'): chicken += [[i, j]]
  
  dist = list(list(map(lambda x : abs(x[0] - y[0]) + abs(x[1] - y[1]), home)) for y in chicken)
  res = 10000
  for c in combinations((i for i in range(len(chicken))), M):
    sumOfDist = sum(map(min, zip(*[dist[i] for i in c])))
    if (sumOfDist < res):
      res = sumOfDist
  
  print(res)

fast()
