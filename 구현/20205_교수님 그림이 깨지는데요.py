import sys
input = sys.stdin.readline

def do():
  N, K = map(int, input().split())
  lst = list(list(input().split()) for i in range(N))
  for i in range(N):
    line = list()
    for j in range(N):
      line += [lst[i][j]]*K
    for j in range(K):
      print(' '.join(line))

do()
