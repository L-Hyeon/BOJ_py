import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  graph = list(list(0 for i in range(N + 1)) for j in range(N + 1))
  for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
  
  for k in range(1, N + 1):
    for i in range(1, N + 1):
      for j in range(1, N + 1):
        if (i == j):
          continue
        if (graph[i][k] and graph[k][j]):
          if (graph[i][j] == 0):
            graph[i][j] = graph[i][k] + graph[k][j]
          else:
            if (graph[i][j] > graph[i][k] + graph[k][j]):
              graph[i][j] = graph[i][k] + graph[k][j]
  
  person = 0
  mn = 10**9
  for i in range(1, N + 1):
    temp = sum(graph[i])
    if (mn > temp):
      person = i
      mn = temp
  print(person)

do()
