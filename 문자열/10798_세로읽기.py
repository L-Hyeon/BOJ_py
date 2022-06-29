import sys
input = sys.stdin.readline

def do():
  mxLen = 0
  lst = list()
  for i in range(5):
    lst.append(list(input().strip()))
    if (mxLen < len(lst[i])):
      mxLen = len(lst[i])
  
  for i in range(5):
    for j in range(mxLen - len(lst[i])):
      lst[i].append('')

  for j in range(len(lst[0])):
    for i in range(5):
      sys.stdout.write(lst[i][j])

do()
