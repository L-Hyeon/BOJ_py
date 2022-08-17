import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  res = 0
  l = 1
  r = l + M - 1
  for i in range(int(input())):
    nxt = int(input())
    while (nxt < l or r < nxt):
      if (r < nxt):
        l += 1
        r += 1
      elif (nxt < l):
        l -= 1
        r -= 1
      res += 1
  print(res)

do()
