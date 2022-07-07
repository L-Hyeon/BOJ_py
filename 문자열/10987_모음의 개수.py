import sys
input = sys.stdin.readline

def do():
  res = 0
  s = {'a', 'e', 'i', 'o', 'u'}
  for e in input().strip():
    if (e in s):
      res += 1

  print(res)

do()
