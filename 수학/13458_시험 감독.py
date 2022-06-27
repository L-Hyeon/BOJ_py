import sys
input = sys.stdin.readline

def do():
  N = int(input())
  people = list(map(int, input().split()))
  B, C = map(int, input().split())
  cnt = N
  for e in people:
    e -= B
    if (0 < e):
      cnt += e//C
      if (e % C):
        cnt += 1
  print(cnt)

do()
