import sys
input = sys.stdin.readline

def do():
  cost = list(map(int, input().split()))
  lst = list(tuple(map(int, input().split())) for i in range(3))
  mx = max(lst[0][1], lst[1][1], lst[2][1])
  parking = [0]*mx

  for tup in lst:
    for i in range(tup[0], tup[1]):
      parking[i] += 1

  res = 0
  for e in parking:
    if (e == 0):
      continue
    res += e*cost[e - 1]
  print(res)

do()
