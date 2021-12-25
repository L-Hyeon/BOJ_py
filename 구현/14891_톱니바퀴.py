import sys
from collections import deque
input = sys.stdin.readline

def do():
  def compareLeft(a, b, d):
    if (gear[a][2] != gear[b][6]):
      if (0 < a):
        compareLeft(a - 1, a, -d)
      gear[a].rotate(d)

  def compareRight(a, b, d):
    if (gear[a][2] != gear[b][6]):
      if (b < 3):
        compareRight(b, b + 1, -d)
      gear[b].rotate(d)

  gear = list(deque(map(int, input().strip())) for i in range(4))
  for _ in range(int(input())):
    n, d = map(int, input().split())
    n -= 1

    # 왼쪽 확인
    if (0 < n):
      compareLeft(n - 1, n, -d)
    # 오른쪽 확인
    if (n < 3):
      compareRight(n, n + 1, -d)
    gear[n].rotate(d)
  
  res = 0
  if (gear[0][0]): res += 1
  if (gear[1][0]): res += 2
  if (gear[2][0]): res += 4
  if (gear[3][0]): res += 8
  print(res)

do()
