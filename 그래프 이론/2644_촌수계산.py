import sys
from collections import deque
input = sys.stdin.readline

def do():
  def bfs(s, end):
    q = deque([[s]])
    visited = [False]*(N + 1)
    visited[s] = True
    ret = 0
    while (q):
      temp = list()
      ret += 1
      for e in q.popleft():
        for d in graph[e]:
          if (d == end):
            return ret
          if (visited[d]):
            continue
          temp.append(d)
          visited[d] = True
      
      if (temp):
        q.append(temp)
    return -1
  
  N = int(input())
  s, e = map(int, input().split())
  graph = dict()
  for i in range(int(input())):
    a, b = map(int, input().split())
    if (a in graph):
      graph[a] += [b]
    else:
      graph[a] = [b]
    
    if (b in graph):
      graph[b] += [a]
    else:
      graph[b] = [a]
  
  print(bfs(s, e))

do()
