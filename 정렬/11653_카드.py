import sys
input = sys.stdin.readline

def do():
  dct = dict()
  minVal, minIdx = 0, 0
  for i in range(int(input())):
    x = int(input())
    if (x in dct):
      dct[x] += 1
    else:
      dct[x] = 1
    if (minVal < dct[x]):
      minVal = dct[x]
      minIdx = x
    elif (minVal == dct[x]):
      if (x < minIdx):
        minIdx = x
  
  print(minIdx)

do()
