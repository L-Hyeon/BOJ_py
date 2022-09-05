import sys
input = sys.stdin.readline

def do():
  def getSum(a, t):
    ret = 0
    while (a > 0):
      ret += a%t
      a = a//t
    return ret

  for i in range(1000, 10000):
    if (getSum(i, 10) == getSum(i, 12) == getSum(i, 16)):
      print(i)

do()
