import sys
input = sys.stdin.readline

def do():
  cnt = 0
  for i in range(8):
    if (i % 2 == 0):
      t = 0
    else:
      t = 1
    for e in input().strip():
      if (t % 2 == 0) and (e == 'F'):
        cnt += 1
      t += 1
  
  print(cnt)

do()
