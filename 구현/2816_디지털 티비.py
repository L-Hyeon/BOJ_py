import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list()
  target = [-1, -1]
  for i in range(N):
    t = input().strip()
    if (t == 'KBS1'):
      target[0] = i
    elif (t == 'KBS2'):
      target[1] = i
    lst.append(t)
  
  if (target[1] < target[0]):
    target[1] += 1

  res = "1"*target[0] + "4"*target[0]
  if (target[1] != 1):
    res += "1"*target[1] + "4"*(target[1] - 1)
  
  print(res)

do()
