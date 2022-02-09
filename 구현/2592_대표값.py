import sys
input = sys.stdin.readline

def do():
  dct = dict()
  avg = 0
  cnt = 0
  mode = 0
  for i in range(10):
    x = int(input())
    if (x not in dct):
      dct[x] = 1
    else:
      dct[x] += 1
    if (cnt < dct[x]):
      cnt = dct[x]
      mode = x
    avg += x
  
  print(avg//10)
  print(mode)

do()
