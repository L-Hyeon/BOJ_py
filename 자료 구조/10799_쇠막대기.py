import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  stk = list()
  res = 0
  pre = ''
  for e in S:
    if (e == ')'):
      stk.pop()
      if (pre == '('):
        res += len(stk)
      else:
        res += 1
    else:
      stk.append(1)
    pre = e
  
  print(res)

do()
