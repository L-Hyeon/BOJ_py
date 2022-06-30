import sys
input = sys.stdin.readline

def do():
  height = 0
  pre = ''
  for c in input().strip():
    if (c == '('):
      if (pre == '('):
        height += 5
      else:
        height += 10
    elif (c == ')'):
      if (pre == ')'):
        height += 5
      else:
        height += 10
    pre = c
  print(height)

do()
