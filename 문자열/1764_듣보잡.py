import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  D = set(input().strip() for i in range(N))
  B = set(input().strip() for i in range(M))
  D = D.intersection(B)
  print(len(D))
  for e in sorted(D):
    print(e)

do()
