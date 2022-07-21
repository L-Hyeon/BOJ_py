import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(list(input().split()) for i in range(N))
  for i in range(N):
    for j in range(1, 4):
      lst[i][j] = int(lst[i][j])
  lst.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
  for i in range(N):
    print(lst[i][0])

def fast():
  N = int(input())
  lst = list()
  for i in range(N):
    a, b, c, d = input().split()
    lst.append([a, int(b), int(c), int(d)])
  
  lst.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
  for i in range(N):
    print(lst[i][0])

fast()
