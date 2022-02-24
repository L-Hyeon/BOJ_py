import sys
input = sys.stdin.readline

def do():
  N, M =map(int, input().split())
  num, name = dict(), dict()
  for i in range(1, N + 1):
    t = input().strip()
    num[i] = t
    name[t] = i
  for i in range(M):
    q = input().strip()
    try:
      q = int(q)
      print(num[q])
    except:
      print(name[q])

do()
