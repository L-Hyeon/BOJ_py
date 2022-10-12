import sys
input = sys.stdin.readline

def do():
  N = int(input())
  demand = list(map(int, input().split()))
  points = set(tuple(map(int, input().split())) for _ in range(N))
  cnt = 0
  for x, y in points:
      if ((x + demand[0], y) in points) and ((x, y + demand[1]) in points) and ((x + demand[0],y + demand[1]) in points):
        cnt += 1
  print(cnt)

do()
