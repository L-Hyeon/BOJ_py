import sys
input = sys.stdin.readline

def do():
  lst = list((i, int(input())) for i in range(1, 9))
  lst.sort(key = lambda x : x[1], reverse = True)
  lst = lst[:5]
  s = 0
  res = list()
  for i, v in lst:
    s += v
    res.append(i)
  res.sort()
  print(s)
  print(*res)

do()
