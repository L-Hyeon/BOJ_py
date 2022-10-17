import sys
input = sys.stdin.readline

def do():
  N, K = map(int, input().split())
  lst = list(list(map(int, input().split())) for i in range(N))
  lst.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)
  rank, cnt = 1, 0
  for i in range(N):
    if (i != 0):
      if (lst[i][1:] == lst[i - 1][1:]):
        cnt += 1
      else:
        if (cnt):
          rank += cnt
          cnt = 0
        rank += 1
    if (lst[i][0] == K):
      print(rank)
      break

do()
