import sys
input = sys.stdin.readline

def do():
  N = int(input())
  if (N == 100):
    print(0)
    return
  M = int(input())
  if (M):
    broken = set(input().split())
  else:
    broken = set()
  
  res = abs(100 - N)
  for num in range(1000001):
    for e in str(num):
      if (e in broken):
        break
    else:
      res = min(res, len(str(num)) + abs(num - N))
  
  print(res)

def fast():
  n,m,*l=map(int,open(0).read().split())
  m = 10 - m
  l = [_ for _ in range(10) if _ not in l]
  l.sort()
  a = len(str(n))
  t=[]
  for i in l:
      t.append(int(str(i) * a))
  if l and a > 1:
      t.append(int( str(l[-1]) * (a - 1) ))
  if l and (l[0] != 0 or m > 1):    
      t.append(int( str( l[ l[0]<1 ] ) + str(l[0]) * a ))
  while t:
      t = list(set(t))
      z = []
      g = []
      for i in t:
          g.append((abs(n - i)+len(str(i)),i))
      g.sort()
      if len(g) > 1:
          t = [g[0][1],g[1][1]]
          z+=["0" if t[0] == 0 else str(t[0])[:-(a-1)]]
          z+=["0" if t[1] == 0 else str(t[1])[:-(a-1)]]
      elif len(g) > 0:
          t = [g[0][1]]
          z=["0" if t[0] == 0 else str(t[0])[:-(a-1)]]
          break
      else:
          break
      a-=1
      if a < 1:
          break
      for w in z:
          for i in l:
              t.append(int(w + str(i) * a))
  b=abs(n - 100)
  if t and b > g[0][0]:
      print(g[0][0])
  else:
      print(b)

fast()
