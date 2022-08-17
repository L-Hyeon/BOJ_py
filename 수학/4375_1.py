import sys
input = sys.stdin.readline

def do():
  while (True):
    try:
      N = int(input())
    except:
      break
    res = 1
    while (res % N != 0):
      res = 10*res + 1
    print(len(str(res)))

def fast():
  for line in sys.stdin:
    N = int(line)
    if (N == 1):
      print(1)
    else:
      l = 1
      temp = 1
      while (temp != 0):
        temp = (10*temp + 1) % N
        l += 1
      print(l)

fast()
