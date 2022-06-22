import sys
input = sys.stdin.readline

def do():
  N = int(input())
  A = list(map(int, input().split()))
  sortedA = sorted(A)
  P = list()
  for e in A:
    idx = sortedA.index(e)
    P.append(idx)
    sortedA[idx] = -1
  
  print(*P)

do()
