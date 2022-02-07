import sys
from collections import deque
input = sys.stdin.readline

def do():
  N = int(input())
  graph = list(list(map(int, input().split())) for i in range(N))

  for k in range(N):
    for i in range(N):
      for j in range(N):
        if (graph[i][j]) or (graph[i][k] and graph[k][j]):
          graph[i][j] = 1
  
  for r in graph:
    print(' '.join(map(str, r)))

do()
