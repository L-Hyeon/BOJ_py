import sys
input = sys.stdin.readline

def do():
  N, L = map(int, input().split())
  lst = list(map(int, input().split()))
  lst.sort()
  ok = lst[0] - 0.5
  cnt = 0
  for e in lst:
    if (e < ok):
      continue
    cnt += 1
    ok = e - 0.5 + L
  
  print(cnt)

do()
