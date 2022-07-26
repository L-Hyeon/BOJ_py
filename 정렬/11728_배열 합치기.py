import sys
input = sys.stdin.readline

def do():
  N, M = map(int, input().split())
  A = sorted(list(map(int, input().split())))
  B = sorted(list(map(int, input().split())))
  
  idxA, idxB = 0, 0
  for i in range(N + M):
    if (idxA == N):
      sys.stdout.write(str(B[idxB]))
      idxB += 1
    elif (idxB == M):
      sys.stdout.write(str(A[idxA]))
      idxA += 1
    elif (A[idxA] < B[idxB]):
      sys.stdout.write(str(A[idxA]))
      idxA += 1
    else:
      sys.stdout.write(str(B[idxB]))
      idxB += 1
    sys.stdout.write(' ')

def trick():
  N, M = map(int, input().split())
  lst = sorted(list(map(int, sys.stdin.read().split())))
  print(*lst)

trick()
