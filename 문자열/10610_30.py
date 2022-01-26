import sys
input = sys.stdin.readline

def do():
  N = sorted(list(input().strip()), reverse = True) 
  haveZero = False
  s = 0
  for e in N:
    s += int(e)
    if (haveZero == False and e == '0'):
      haveZero = True

  if (haveZero and s % 3 == 0):
    print(''.join(N))
  else:
    print(-1)

do()
